#!/usr/bin/env python3
"""
Audit adversarial — Orchestrateur v3 (Anti-Fragile).
10 phases, 5 modèles, SHARED routing tiercé, garde-fous anti-boucle/truncation.

Usage:
  python3 audit.py [--dry-run] [--resume] [--phase PHASE_ID] [--benchmark] <article.md>
  python3 audit.py --benchmark

  --phase PHASE_ID  Lance UNE seule phase (ex: --phase phase6_veto).
                    Charge les outputs sauvegardes des phases precedentes.
                    Necessite un run complet prealable (sans --phase).
"""

import json, os, sys, time, re
from pathlib import Path
import httpx

OLLAMA_BASE = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
PROMPT_FILE = Path(__file__).parent / "2026-06-14_audit_adversarial_prompt_v5.md"

# JSON Schema for table phases (G1, G2, G3) — Ollama format parameter
# Élimine les corruptions de tableau markdown. L'orchestrateur rend le JSON en table.
PROBLEMS_SCHEMA = {
    "type": "object",
    "properties": {
        "problemes": {
            "type": "array",
            "maxItems": 10,
            "items": {
                "type": "object",
                "properties": {
                    "ligne": {"type": "string"},
                    "citation": {"type": "string", "maxLength": 150},
                    "code": {"type": "string", "enum": ["FACT","LACUNA","SURETAB","CONTRA","BIAIS","LOGIC","GLISS","PRAG"]},
                    "gravite": {"type": "integer", "minimum": 1, "maximum": 5},
                    "confiance": {"type": "integer", "minimum": 1, "maximum": 5},
                    "correction": {"type": "string"}
                },
                "required": ["ligne","citation","code","gravite","confiance","correction"]
            }
        },
        "fatalites": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "ligne": {"type": "string"},
                    "citation": {"type": "string", "maxLength": 150},
                    "code": {"type": "string"},
                    "justification": {"type": "string"}
                },
                "required": ["ligne","citation","code","justification"]
            }
        },
        "solide": {"type": "array", "maxItems": 5, "items": {"type": "string"}},
        "cannot_assess": {"type": "array", "maxItems": 5, "items": {"type": "string"}}
    },
    "required": ["problemes","solide"]
}

TABLE_PHASES = {"g1_greffier", "g2_logicien", "g3_cartographe"}
# Phases de synthèse qui ne reçoivent PAS l'article complet (travaillent sur EXTRA uniquement)
NO_ARTICLE_PHASES = {"phase4_synthesis", "phase5_cannot_assess", "phase6_veto"}

# Benchmarks réels (Radeon 780M, Vulkan, FA+q8_0, 2026-06-14)
BENCHMARKS = {
    "phi4-mini:latest":         {"gen": 19.9, "pe": 181, "label": "Phi-4-mini"},
    "qwen3:8b":                 {"gen": 11.1, "pe": 103, "label": "Qwen3:8b"},
    "granite3.2:8b":            {"gen": 10.4, "pe": 100, "label": "Granite3.2:8b"},
    "gemma4-coder:12b":         {"gen": 8.1, "pe": 53, "label": "Gemma4-12B-Coder"},
    "gemma4-abliterated:12b":   {"gen": 8.3, "pe": 54, "label": "Gemma4-12B-Abliterated"},
    # 35B MoE retiré — ne génère aucun token sur Radeon 780M (saturation mémoire)
}

# Phase config v3: (phase_id, model, block_id_in_prompt, prompt_tok_est, gen_tok_est)
PHASE_CONFIG = [
    ("phase0_metatexte",     "phi4-mini:latest", "phase0_metatexte",      5700, 200),
    ("phase1_single_model",  "qwen3:8b",          "phase1_coldread",       5700, 600),
    ("g1_greffier",          "granite3.2:8b",     "regard_greffier",       6500, 1500),
    ("g2_logicien",           "qwen3:8b",          "regard_logicien",       6500, 1500),
    ("g3_cartographe",       "granite3.2:8b",     "regard_cartographe",    6500, 1500),
    ("g4_contrebandier",     "granite3.2:8b",     "regard_contrebandier",  6500, 800),
    # ── BLOC qwen3:8b (KV cache reuse) ──
    ("phase3_deepdive",      "qwen3:8b",          "phase3_deepdive",       7500, 2000),
    ("phase4_synthesis",     "qwen3:8b",          "synthesis",             4000, 2000),
    ("phase5_cannot_assess", "qwen3:8b",          "cannot_assess_final",   3000, 800),
    # ── Fin bloc qwen3:8b ──
    ("phase6_veto",          "qwen3:8b",          "critical_flaw_veto",    4000, 1500),
]

# SHARED block routing: quels SHARED blocks sont envoyés à quelles phases
SHARED_ROUTING = {
    "shared_taxonomy": [
        "g1_greffier", "g2_logicien", "g3_cartographe", "g4_contrebandier",
        "phase3_deepdive", "phase4_synthesis", "phase5_cannot_assess", "phase6_veto"
    ],
    "shared_rules": [
        "g1_greffier", "g2_logicien", "g3_cartographe", "g4_contrebandier"
    ],
    "shared_format_table": [
        "g1_greffier", "g2_logicien", "g3_cartographe"
    ],
    "shared_format_prose": [
        "g4_contrebandier"
    ],
}

# num_predict plafonné par phase (anti-boucle, anti-truncation)
PHASE_NUM_PREDICT = {
    "phase0_metatexte": 200,
    "phase1_single_model": 600,
    "g1_greffier": 1500,
    "g2_logicien": 1500,
    "g3_cartographe": 1500,
    "g4_contrebandier": 800,
    "phase3_deepdive": 2000,
    "phase4_synthesis": 2000,
    "phase5_cannot_assess": 800,
    "phase6_veto": 1500,
}



def validate_output(phase_id: str, output: str) -> tuple:
    """Retourne (is_valid, warning_message)."""
    warnings = []
    if phase_id in TABLE_PHASES:
        try:
            data = json.loads(output)
            n = len(data.get("problemes", []))
            if n > 10:
                warnings.append(f"DÉGÉNÉRESCENCE: {n} problèmes (max 10)")
            elif n == 0:
                warnings.append("VIDE: 0 problèmes identifiés")
        except json.JSONDecodeError:
            warnings.append("JSON INVALIDE: la sortie n'est pas du JSON valide")
    else:
        if len(output.strip()) < 20:
            warnings.append("VIDE: output < 20 caractères")
        if phase_id == "phase0_metatexte" and "|---" in output:
            warnings.append("ERREUR: Ph0 a produit un tableau (confusion de rôle)")
    return (len(warnings) == 0, "; ".join(warnings))


def compress_phase_output(output: str, max_chars: int = 500) -> str:
    """Compresse un output de phase en résumé pour EXTRA."""
    # JSON structuré (phases tableau G1-G3)
    try:
        data = json.loads(output)
        if "problemes" in data:
            lines = ["| # | Ligne | Citation | Code | Grav | Conf | Correction |",
                     "|---|-------|----------|------|------|------|------------|"]
            for i, p in enumerate(data["problemes"][:5], 1):
                lines.append(f"| {i} | {p.get('ligne','')} | {p.get('citation','')[:60]} | {p.get('code','')} | {p.get('gravite','')} | {p.get('confiance','')} | {p.get('correction','')[:40]} |")
            return "\n".join(lines)
    except (json.JSONDecodeError, TypeError):
        pass
    # Prose (G4, Ph5, Ph3, Ph4, Ph6)
    if '### ' in output:
        sections = re.split(r'\n(?=### )', output)
        summary = []
        for sec in sections[:8]:
            lines = sec.strip().split('\n')
            if not lines:
                continue
            sec_header = lines[0]
            first_sent = ""
            for line in lines[1:]:
                stripped = line.strip()
                if stripped and not stripped.startswith('#') and not stripped.startswith('```'):
                    first_sent = re.split(r'(?<=[.!?])\s', stripped, maxsplit=1)[0][:120]
                    break
            candidate = sec_header + ("\n" + first_sent if first_sent else "")
            if len('\n'.join(summary + [candidate])) > max_chars:
                break
            summary.append(candidate)
        return '\n'.join(summary)
    return output[:max_chars] + ('...' if len(output) > max_chars else '')


def build_options(phase_id: str, num_predict: int) -> dict:
    """Construit les options Ollama par phase."""
    opts = {
        "temperature": 0,
        "num_predict": num_predict,
        "num_ctx": 16384,
        "num_batch": 2048,
        "repeat_penalty": 1.1,
        "stop": ["\n\n\n\n"],
    }
    if phase_id == "g2_logicien":
        opts["enable_thinking"] = False
    # Ph6 Veto: NE PAS désactiver thinking sur qwen3:8b sans JSON schema.
    # Règle: thinking model + enable_thinking=False + pas de JSON schema = 0 token.
    # Ph6 a besoin du thinking pour synthétiser 8 phases en verdict binaire.
    return opts


def parse_sections(prompt: str) -> dict:
    """Parse les sections BLOCK et SHARED du prompt markdown."""
    blocks = {}
    current_id = None
    current_label = None
    current_lines = []

    for line in prompt.split("\n"):
        m = re.match(r"^## (BLOCK|SHARED):(\w+)\s*(.*)$", line)
        if m:
            if current_id:
                blocks[current_id] = {
                    "label": current_label or current_id,
                    "content": "\n".join(current_lines).strip(),
                }
            current_id = m.group(2)
            current_label = m.group(3).strip() or current_id
            if m.group(1) == "SHARED":
                current_id = f"shared_{current_id}"
            current_lines = []
        elif current_id:
            current_lines.append(line)

    if current_id and current_lines:
        blocks[current_id] = {
            "label": current_label or current_id,
            "content": "\n".join(current_lines).strip(),
        }

    return blocks


def build_messages(blocks: dict, block: dict, article: str, phase_id: str, extra: str = "") -> list:
    """Construit les messages pour une phase avec SHARED routing tiercé.
    Les phases de synthèse (Ph4, Ph5, Ph6) ne reçoivent PAS l'article complet —
    elles travaillent uniquement sur EXTRA compressé pour éviter le dépassement
    de contexte (article 8K tok + EXTRA + prompt > 16K)."""
    parts = []
    for sid, phases in SHARED_ROUTING.items():
        if phase_id in phases and sid in blocks:
            parts.append(blocks[sid]["content"])
    parts.append(block["content"])
    if extra:
        parts.append(f"\n--- EXTRA ---\n{extra}\n")
    system = "\n\n".join(parts)
    if phase_id in NO_ARTICLE_PHASES:
        user = "[TRAVAILLE À PARTIR DES EXTRA INJECTÉS DANS LE PROMPT SYSTEM.]"
    else:
        user = f"[ARTICLE À AUDITER]\n\n{article}"
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


def extract_cannot_assess_zones(results: dict) -> str:
    """Extrait toutes les zones CANNOT_ASSESS des outputs précédents."""
    zones = []
    for pid, data in results.items():
        output = data.get("output", "")
        # JSON natif (G1-G3)
        try:
            j = json.loads(output)
            items = j.get("cannot_assess", [])
            if items:
                zones.append(f"--- {pid.upper()} ---\n" + "\n".join(f"- {c}" for c in items))
            continue
        except (json.JSONDecodeError, TypeError):
            pass
        # Regex fallback (phases prose)
        matches = re.findall(r'### CANNOT_ASSESS\n(.*?)(?=\n###|\n---|\Z)', output, re.DOTALL)
        if matches:
            zones.append(f"--- {pid.upper()} ---\n{matches[-1].strip()}")
    return "\n\n".join(zones) if zones else "Aucune zone CANNOT_ASSESS identifiée."


def build_extra(pid: str, results: dict) -> str:
    """Construit le contenu EXTRA pour une phase."""
    if pid == "phase1_single_model":
        meta = results.get("phase0_metatexte", {}).get("output", "")
        return f"[Métatexte extrait par Phase 0]:\n{meta}" if meta else ""
    elif pid == "phase3_deepdive":
        meta = results.get("phase0_metatexte", {}).get("output", "")
        return f"[Domaines critiques identifiés par Phase 0]:\n{meta}" if meta else ""
    elif pid == "phase4_synthesis":
        parts = []
        for pid2, model2, block_id2, _, _ in PHASE_CONFIG:
            if pid2 not in results or pid2 == pid:
                continue
            bench = BENCHMARKS.get(model2, {"label": model2})
            compressed = compress_phase_output(results[pid2]["output"])
            parts.append(f"=== {pid2.upper()} ({bench['label']}) ===\n{compressed}")
        return "\n\n".join(parts) if parts else ""
    elif pid == "phase6_veto":
        parts = []
        for pid2, model2, block_id2, _, _ in PHASE_CONFIG:
            if pid2 not in results or pid2 == pid:
                continue
            bench = BENCHMARKS.get(model2, {"label": model2})
            # Ph5 (CANNOT_ASSESS final) : output court, envoyer en entier
            if pid2 == "phase5_cannot_assess":
                content = results[pid2]["output"]
            else:
                content = compress_phase_output(results[pid2]["output"])
            parts.append(f"=== {pid2.upper()} ({bench['label']}) ===\n{content}")
        return "\n\n".join(parts) if parts else ""
    elif pid == "phase5_cannot_assess":
        return extract_cannot_assess_zones(results)
    return ""


def save_phase_output(outdir: Path, phase_id: str, output: str, is_complete: bool = True):
    """Sauvegarde l'output brut (JSON ou texte) + marqueur de complétion."""
    fpath = outdir / f"{phase_id}.json"
    fpath.write_text(output, encoding="utf-8")
    if is_complete:
        (outdir / f"{phase_id}._complete").write_text("")
    else:
        c = outdir / f"{phase_id}._complete"
        if c.exists():
            c.unlink()


def is_phase_complete(outdir: Path, phase_id: str) -> bool:
    """Vérifie si une phase est complète (fichier ._complete présent et .json valide)."""
    fpath = outdir / f"{phase_id}.json"
    cpath = outdir / f"{phase_id}._complete"
    if not fpath.exists() or not cpath.exists():
        return False
    # Vérifier que le JSON est valide (pour les phases tableau)
    if phase_id in TABLE_PHASES:
        try:
            json.loads(fpath.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return False
    return True


def json_to_table(json_output: str) -> str:
    """Convertit le JSON structuré en tableau markdown lisible."""
    try:
        data = json.loads(json_output)
    except json.JSONDecodeError:
        return json_output
    lines = []
    if data.get("problemes"):
        lines.append("### Problèmes identifiés")
        lines.append("| # | Ligne | Citation | Code | Grav (1-5) | Conf (1-5) | Correction ou question |")
        lines.append("|---|-------|----------|------|-----------|------------|----------------------|")
        for i, p in enumerate(data["problemes"], 1):
            lines.append(f"| {i} | {p.get('ligne','')} | « {p.get('citation','')} » | {p.get('code','')} | {p.get('gravite','')} | {p.get('confiance','')} | {p.get('correction','')} |")
    if data.get("fatalites"):
        lines.append("")
        lines.append("### FATALITÉS (Critical Flaw Veto)")
        lines.append("| # | Ligne | Citation | Code | Justification |")
        lines.append("|---|-------|----------|------|---------------|")
        for i, f in enumerate(data["fatalites"], 1):
            lines.append(f"| {i} | {f.get('ligne','')} | « {f.get('citation','')} » | {f.get('code','')} | {f.get('justification','')} |")
    if data.get("solide"):
        lines.append("")
        lines.append("### Où le texte est solide dans cette dimension")
        for s in data["solide"]:
            lines.append(f"- {s}")
    if data.get("cannot_assess"):
        lines.append("")
        lines.append("### CANNOT_ASSESS")
        for c in data["cannot_assess"]:
            lines.append(f"- {c}")
    return "\n".join(lines)


def call_ollama(messages: list, model: str, phase_id: str,
                bench: dict, pe_est: int,
                timeout: int = 3600) -> tuple:
    """Appel Ollama avec options par phase, streaming, et progression."""
    num_predict = PHASE_NUM_PREDICT.get(phase_id, 150)
    opts = build_options(phase_id, num_predict)
    payload = {
        "model": model,
        "messages": messages,
        "stream": True,
        "options": opts,
    }
    # Structured output for table phases
    if phase_id in TABLE_PHASES:
        payload["format"] = PROBLEMS_SCHEMA
    family = bench["label"]
    pe_speed_est = bench["pe"]
    est_pe = pe_est / pe_speed_est
    print(f"  ┌─ {family} | prompt eval ~{pe_est}tok @ {pe_speed_est}t/s ≈ {est_pe:.0f}s | num_predict={num_predict}")

    start = time.time()
    full_content = ""
    tok_count = 0
    last_progress = time.time()
    prompt_eval_done = False
    pe_duration = 0.0
    last_data = {}

    try:
        with httpx.Client(timeout=timeout) as client:
            with client.stream("POST", f"{OLLAMA_BASE}/api/chat", json=payload) as resp:
                for line in resp.iter_lines():
                    if not line:
                        continue
                    data = json.loads(line)
                    last_data = data
                    content = data.get("message", {}).get("content", "")
                    if content:
                        if not prompt_eval_done:
                            prompt_eval_done = True
                            pe_duration = time.time() - start
                        full_content += content
                        tok_count += 1

                    elapsed = time.time() - start
                    if tok_count > 0 and elapsed - last_progress >= 10:
                        speed = tok_count / (elapsed - pe_duration) if prompt_eval_done and (elapsed - pe_duration) > 0 else 0
                        pct = min(100, int(tok_count / max(1, num_predict) * 100))
                        bar = "█" * (pct // 4) + "░" * (25 - pct // 4)
                        print(f"  │ [{bar}] {pct:3d}% — {tok_count}/{num_predict} tok — {speed:.1f} t/s — {elapsed:.0f}s")
                        last_progress = elapsed

                    if data.get("done"):
                        break

        elapsed = time.time() - start
        gen_duration = elapsed - pe_duration if prompt_eval_done else 0
        speed = tok_count / gen_duration if gen_duration > 0 else 0

        if not full_content:
            done_reason = last_data.get("done_reason", "unknown")
            print(f"  └─ ⚠️  vide (done_reason={done_reason}) — {elapsed:.0f}s")
            return f"[TRONQUÉ: {done_reason}]", elapsed, 0, pe_duration

        # Console summary
        if phase_id in TABLE_PHASES:
            try:
                data = json.loads(full_content)
                n = len(data.get("problemes", []))
                nf = len(data.get("fatalites", []))
                ns = len(data.get("solide", []))
                nc = len(data.get("cannot_assess", []))
                print(f"  ✓ {n} problèmes, {nf} fatalités, {ns} solide, {nc} cannot_assess")
            except json.JSONDecodeError as e:
                print(f"  ⚠️  JSON invalide: {e}")
        print(f"  └─ {elapsed:.0f}s = PE {pe_duration:.0f}s + gen {gen_duration:.0f}s "
              f"— {tok_count}/{num_predict} tok ({speed:.1f} t/s)")
        return full_content, elapsed, tok_count, pe_duration

    except httpx.TimeoutException:
        elapsed = time.time() - start
        print(f"  └─ ⏰ TIMEOUT ({timeout}s)")
        return f"[TIMEOUT après {timeout}s]", elapsed, tok_count, pe_duration
    except Exception as e:
        elapsed = time.time() - start
        print(f"  └─ ❌ {e}")
        return f"[ERREUR: {e}]", elapsed, tok_count, pe_duration


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        return

    if sys.argv[1] == "--benchmark":
        run_benchmark()
        return

    dry_run = "--dry-run" in sys.argv[1:]
    resume_mode = "--resume" in sys.argv[1:]

    # --phase PHASE_ID : lance une seule phase (nécessite outputs sauvés)
    single_phase = None
    for j, arg in enumerate(sys.argv[1:], 1):
        if arg == "--phase" and j + 1 < len(sys.argv):
            single_phase = sys.argv[j + 1]
            break

    args = [a for a in sys.argv[1:] if not a.startswith("--") and a != single_phase]
    if not args:
        print("Usage: python3 audit.py [--dry-run] [--resume] <article.md>")
        return

    article_path = args[0]
    article_text = Path(article_path).read_text(encoding="utf-8")
    prompt_text = PROMPT_FILE.read_text(encoding="utf-8")
    name = Path(article_path).stem
    outdir = Path(article_path).parent / f"_audit_v3_{name}"
    if not dry_run:
        outdir.mkdir(parents=True, exist_ok=True)

    blocks = parse_sections(prompt_text)

    # Estimation header
    print()
    print("=" * 68)
    print("  AUDIT ADVERSARIAL — v3 (Anti-Fragile)")
    print(f"  Article : {name}")
    word_count = len(article_text.split())
    n_phases = len(PHASE_CONFIG)
    n_qwen = sum(1 for p in PHASE_CONFIG if p[1] == "qwen3:8b")
    print(f"  Mots    : ~{word_count}")
    if n_qwen > 1:
        print(f"  Phases  : {n_phases} ({n_qwen}x qwen3:8b dont {n_qwen-1} en KV warm)")
    else:
        print(f"  Phases  : {n_phases}")
    print(f"  Prompt  : v5 ({Path(PROMPT_FILE).name})")
    if resume_mode:
        print(f"  Mode    : REPRISE (vérification __AUDIT_COMPLETE__)")
    print("=" * 68)

    total_est = 0
    prev_model_est = None
    for i, (pid, model, block_id, pe_tok, gen_tok) in enumerate(PHASE_CONFIG):
        bench = BENCHMARKS.get(model, {"gen": 10, "pe": 50, "label": model})
        secs_pe = pe_tok / bench["pe"]
        secs_gen = gen_tok / bench["gen"]
        total = secs_pe + secs_gen
        total_est += total
        block = blocks.get(block_id, {})
        phase_label = block.get("label", pid)[:34]
        family = bench["label"]
        kv_warm = " [KV warm]" if model == prev_model_est else ""
        marker = ""
        np = PHASE_NUM_PREDICT.get(pid, "?")
        print(f"  {i+1:2d}/10 {phase_label:34s} {family:14s} "
              f"{secs_pe:.0f}s+{secs_gen:.0f}s={total:.0f}s np={np}{marker}{kv_warm}")
        prev_model_est = model

    print(f"\n  ⏱  Total estimé : ~{total_est:.0f}s (~{total_est/60:.0f} min)")

    if dry_run:
        print(f"\n  {'='*68}")
        print("  [DRY RUN] — Aucun appel LLM effectué.")
        print(f"  {'='*68}")
        return

    # ── Mode --phase : lance une seule phase ──
    if single_phase:
        # Charger les outputs sauvegardés
        results = {}
        missing = []
        for pid, model, block_id, _, _ in PHASE_CONFIG:
            if pid == single_phase:
                break
            fpath = outdir / f"{pid}.json"
            if fpath.exists():
                results[pid] = {"output": fpath.read_text(encoding="utf-8"), "model": model}
            else:
                missing.append(pid)
        if missing:
            print(f"  ❌ Outputs manquants : {', '.join(missing)}")
            print(f"  Lance d'abord un run complet : python3 audit.py <article.md>")
            sys.exit(3)
        # Trouver la config de la phase cible
        target = None
        for i, (pid, model, block_id, pe_tok, gen_tok) in enumerate(PHASE_CONFIG):
            if pid == single_phase:
                target = (i, pid, model, block_id, pe_tok, gen_tok)
                break
        if not target:
            print(f"  ❌ Phase inconnue : {single_phase}")
            print(f"  Phases valides : {', '.join(p[0] for p in PHASE_CONFIG)}")
            sys.exit(3)
        i, pid, model, block_id, pe_tok, gen_tok = target
        block = blocks.get(block_id, {})
        phase_label = block.get("label", pid)
        bench = BENCHMARKS.get(model, {"gen": 10, "pe": 50, "label": model})
        print(f"\n  ── Phase {single_phase} : {phase_label} (SOLO) ──")
        extra = build_extra(pid, results)
        messages = build_messages(blocks, block, article_text, pid, extra=extra)
        output, dt, tok_count, pe_actual = call_ollama(messages, model, pid, bench, pe_tok)
        is_valid, warning = validate_output(pid, output)
        if warning:
            print(f"  ⚠️  {warning}")
        save_phase_output(outdir, pid, output, is_complete=is_valid)
        print(f"  💾 → {pid}.json ({dt:.0f}s, {tok_count} tok)")
        print(f"\n=== OUTPUT ===\n{output}\n=== FIN ===")
        return

    print(f"\n  Démarrage de l'audit v3...\n")

    results = {}
    timings = {}
    prev_model = None
    consecutive_fails = 0

    for i, (pid, model, block_id, pe_tok, gen_tok) in enumerate(PHASE_CONFIG):
        block = blocks.get(block_id, {})
        if not block:
            print(f"  ⚠️  BLOCK '{block_id}' introuvable dans le prompt, skipping.")
            continue

        # Reprise : skip si déjà complet (vérifie .json + ._complete)
        if resume_mode and is_phase_complete(outdir, pid):
            existing = (outdir / f"{pid}.json").read_text(encoding="utf-8")
            results[pid] = {"output": existing, "model": model}
            timings[pid] = {"secs": 0, "tokens": len(existing.split()), "pe_secs": 0}
            phase_label = block.get("label", pid)
            print(f"\n  ── Phase {i+1}/10 : {phase_label} [REPRISE — déjà complet] ──")
            prev_model = model
            continue

        phase_label = block["label"]
        bench = BENCHMARKS.get(model, {"gen": 10, "pe": 50, "label": model})
        kv_warm = model == prev_model
        kv_label = " [KV warm]" if kv_warm else ""
        print(f"\n  ── Phase {i+1}/10 : {phase_label}{kv_label} ──")

        extra = build_extra(pid, results)
        messages = build_messages(blocks, block, article_text, pid, extra=extra)
        output, dt, tok_count, pe_actual = call_ollama(messages, model, pid, bench, pe_tok)

        # Validation post-phase
        is_valid, warning = validate_output(pid, output)
        if warning:
            print(f"  ⚠️  {warning}")

        results[pid] = {"output": output, "model": model}
        timings[pid] = {"secs": dt, "tokens": tok_count, "pe_secs": pe_actual, "warning": warning}

        if not dry_run:
            save_phase_output(outdir, pid, output, is_complete=is_valid)
            gen_speed = tok_count / dt if dt > 0 else 0
            print(f"  💾 → {pid}.json ({dt:.0f}s, {tok_count} tok, {gen_speed:.1f} tok/s)")

        prev_model = model

        # Détection de défaillances consécutives
        if not is_valid:
            consecutive_fails += 1
            if consecutive_fails >= 2:
                print(f"\n  ❌ HALTE: {consecutive_fails} phases défaillantes consécutives.")
                print(f"  Vérifie Ollama et les modèles, puis relance avec --resume.")
                sys.exit(2)
        else:
            consecutive_fails = 0

    # Summary
    print(f"\n{'='*68}")
    print(f"  RÉSUMÉ V3")
    print(f"{'='*68}")
    total_t = sum(t["secs"] for t in timings.values())
    total_tok = sum(t["tokens"] for t in timings.values())
    for pid, model, block_id, pe_tok, gen_tok in PHASE_CONFIG:
        t = timings.get(pid, {})
        block = blocks.get(block_id, {})
        label = block.get("label", pid)[:32]
        bench = BENCHMARKS.get(model, {"label": model})
        warn = f" ⚠️" if t.get("warning") else ""
        print(f"  {label:32s} {t.get('tokens',0):4d} tok  {t.get('secs',0):.0f}s  ({bench['label']}){warn}")
    print(f"  {'─'*68}")
    print(f"  {'TOTAL':32s} {total_tok:4d} tok  {total_t:.0f}s  ({total_t/60:.0f} min)")

    # Write final report (JSON → markdown rendering for table phases)
    report = [f"# Audit Adversarial v3 — {name}\n"
              f"**Date** : {time.strftime('%Y-%m-%d %H:%M')} | **10 phases, 5 modèles**\n"
              f"**Temps total** : {total_t:.0f}s ({total_t/60:.0f} min) | **Tokens** : {total_tok}\n"]
    for pid, model, block_id, _, _ in PHASE_CONFIG:
        if pid in results:
            block = blocks.get(block_id, {})
            label = block.get("label", pid)
            warn = timings.get(pid, {}).get("warning", "")
            warn_note = f" ⚠️ {warn}" if warn else ""
            report.append(f"\n## {label} (modèle: {BENCHMARKS.get(model, {}).get('label', model)}){warn_note}\n")
            output = results[pid]["output"]
            # Table phases: render JSON as markdown for the report
            if pid in TABLE_PHASES:
                output = json_to_table(output)
            report.append(output)
    report_path = outdir / f"audit_v3_{name}.md"
    report_path.write_text("\n".join(report), encoding="utf-8")
    print(f"\n✅ Rapport final : {report_path}")

    # Meta JSON
    meta = {
        "article": name,
        "date": time.strftime("%Y-%m-%d %H:%M"),
        "phases": {pid: {"model": model, "secs": timings.get(pid, {}).get("secs", 0),
                          "tokens": timings.get(pid, {}).get("tokens", 0),
                          "warning": timings.get(pid, {}).get("warning", "")}
                    for pid, model, _, _, _ in PHASE_CONFIG if pid in timings},
        "total_secs": total_t, "total_tokens": total_tok,
    }
    (outdir / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")


def run_benchmark():
    print(f"\n{'='*60}")
    print("  BENCHMARK — Mesure tok/s (génération courte)")
    print(f"{'='*60}\n")
    test_prompt = "Écris un paragraphe de 3 lignes sur la vérification des sources."
    for model, bench in BENCHMARKS.items():
        print(f"  Test: {bench['label']} ({model})")
        messages = [
            {"role": "system", "content": "Tu es un assistant concis."},
            {"role": "user", "content": test_prompt},
        ]
        payload = {
            "model": model,
            "messages": messages,
            "stream": False,
            "options": {"temperature": 0.2, "num_predict": 100, "num_ctx": 8192, "num_batch": 2048},
        }
        try:
            with httpx.Client(timeout=120) as client:
                resp = client.post(f"{OLLAMA_BASE}/api/chat", json=payload)
                d = resp.json()
                ec = d.get("eval_count", 0)
                ed = d.get("eval_duration", 0) / 1e9
                pd = d.get("prompt_eval_duration", 0) / 1e9
                pc = d.get("prompt_eval_count", 0)
                gen_s = ec / ed if ed > 0 else 0
                pe_s = pc / pd if pd > 0 else 0
                print(f"    Prompt eval: {pc} tok / {pd:.1f}s = {pe_s:.0f} t/s")
                print(f"    Generation:  {ec} tok / {ed:.1f}s = {gen_s:.1f} t/s")
        except Exception as e:
            print(f"    ❌ {e}")
        print()


if __name__ == "__main__":
    main()
