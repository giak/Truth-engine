#!/usr/bin/env python3
"""verify.py — Moteur de vérification déterministe, générique et indépendant du projet.

Le moteur ne connaît AUCUNE règle de projet. Toutes les règles sont déclarées
dans `.verify/config.json` : branches protégées, commandes de test, commandes
de contrôle arbitraires, convention de nommage. C'est ce fichier qui rend
l'outil adaptable à n'importe quel projet.

Trois verdicts, et seulement trois : PASS / FAIL / BLOCKED. Pas de score.

STATE_ID := SHA256( HEAD + diff suivi + fichiers non suivis + leurs hash ).
Deux états différents peuvent partager le même HEAD ; STATE_ID capture l'état
complet, donc toute modification après review invalide le verdict.

Modes :
  check     Exécute les contrôles déterministes + calcule STATE_ID.
            Écrit `.verify/pending.json`, imprime un rapport JSON sur stdout.
            Code retour : 0 = PASS, 1 = FAIL, 2 = BLOCKED.
  state-id  Imprime le STATE_ID courant (sha256) uniquement.
  certify   Finalise : compare le STATE_ID courant à celui enregistré par
            `check`, enregistre le verdict du reviewer, écrit `.verify/result.json`.
            Code retour : 0 = PASS, 1 = FAIL, 2 = BLOCKED.
  gate      check + review-local (Ollama, stateless) + certify, en une commande.
            La revue LLM est advisory : convertie en verdict par des règles
            déterministes (jamais de faux PASS). Code retour 0/1/2 comme check.

Usage :
  python3 tools/verify/verify.py check
  python3 tools/verify/verify.py state-id
  python3 tools/verify/verify.py certify --review PASS|FAIL|BLOCKED [--findings-file <fichier.json>]
  python3 tools/verify/verify.py gate [--file <livrable>] [--model <modèle>]
  (--findings-file : persiste les findings du reviewer dans result.json)
"""

import hashlib
import json
import os
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone

CONFIG_PATH = ".verify/config.json"
PENDING_PATH = ".verify/pending.json"
RESULT_PATH = ".verify/result.json"
FINDINGS_PATH = ".verify/findings.json"

VERDICTS = ("PASS", "FAIL", "BLOCKED")

OLLAMA_URL = "http://localhost:11434/api/generate"
REVIEW_MODEL_DEFAULT = "qwen3.6:35b"
REVIEW_TIMEOUT = 300
REVIEW_TEMP = 0.3
REVIEW_NUM_PREDICT = 4096
REVIEW_POINTS = ("C1", "C2", "C3", "C4", "C5", "C6", "C7")
# Mapping modèle → options Ollama (spec gate §6). think:false est obligatoire
# pour qwen3.6:35b (hybrid-thinking : réponse vide sinon). Modèle inconnu :
# format:json seul, avec avertissement dans le certificat.
REVIEW_MODEL_OPTIONS = {
    "qwen3.6:35b": {"think": False, "format": "json"},
    "qwen3:8b": {"format": "json"},
    "gemma3:12b": {"format": "json"},
}

ROLE = """Tu es un reviewer indépendant et hostile au travail présenté. Tu n'as pas produit ce document. Tu es en lecture seule. Tu ne répareras rien.
Rends exactement UN verdict parmi trois : FAIL (défaut démontrable, chaque défaut documenté), BLOCKED (vérification impossible), PASS (aucun défaut matériel).
Interdits : scores, pourcentages, flatterie. Style direct. Seuls les défauts qui empêchent rationnellement la livraison vont dans findings."""

CONTRACT = """CONTRAT DU PROJET (extraits canoniques de knowledge.md et truth-engine-v2/KERNEL.md) :
- Livrable final : STATE=FINAL, NEXT_ACTION=NONE. KERNEL §0 : « NEVER persist OPEN/PENDING as final ».
- Pipeline KERNEL obligatoire : ANALYZE §0 avec 15 symboles narratifs scorés, BIAS_TEST, CRÉDO/SCOPING, LEAD_REGISTRY, CLAIM_REGISTRY, EVIDENCE_REGISTRY.
- COMPLEXITY=SIMPLE : exactement 5 sections core (RÉSUMÉ EXÉCUTIF, CHRONOLOGIE, DOMAINES, CARTE DES PREUVES, PÉRIMÈTRE & LIMITES) + appendices SOURCES et REQUEST_LOG obligatoires.
- Traçabilité : bloc FACT_REGISTRY_V1 (id|epi|tier|url|families|date), identifiant FCT-###, source = URL de page spécifique cliquable / SRC-ID / locator exact.
- L4 (CONFIRMÉ) : L3 + gate EPI=FACT + recherche de contre-exemples + preuves matérielles dans le livrable (sources fetchées, recoupement ≥2 familles, FACT_REGISTRY_V1, REQUEST_LOG).
- Horodatage du nom de fichier = date/heure réelle de création (CEST), jamais inventé.
- Toute affirmation sans source vérifiable = violation grave."""

ENUM = """

PROCÉDURE OBLIGATOIRE, À EXÉCUTER DANS CET ORDRE :
1. Examine le livrable ci-dessous.
2. Pour CHACUN des 7 points C1..C7, tranche explicitement : C1:OK ou C1:VIOLATION, etc. (une ligne par point, dans l'ordre).
3. Convertis en findings UNIQUEMENT les points marqués VIOLATION (location + problem + evidence pour chacun).
4. Le verdict est FAIL si au moins un point est VIOLATION, sinon PASS, BLOCKED si le livrable est illisible.

Points à trancher :
C1. STATE du manifeste = FINAL ?
C2. Pipeline KERNEL présent (ANALYZE 15 symboles, BIAS_TEST, CRÉDO/SCOPING, registres) ?
C3. Structure SIMPLE complète (5 sections core + SOURCES + REQUEST_LOG) ?
C4. Traçabilité des faits (FACT_REGISTRY_V1, FCT-###, source URL/locator) ?
C5. Preuve matérielle de « vérifié L4 » ?
C6. Horodatage du nom de fichier cohérent ?
C7. Autre fabrication ou affirmation non étayée ?

RÉPONDS UNIQUEMENT EN JSON :
{"points": {"C1": "OK" ou "VIOLATION", ..., "C7": ...}, "verdict": "PASS" ou "FAIL" ou "BLOCKED", "findings": [{"location": "...", "problem": "...", "evidence": "..."}]}"""

DEFAULT_CONFIG = {
    "version": 1,
    "task": "default",
    "protected_branches": [],
    "tests": [],
    "checks": [],
    "naming": {"enabled": False},
}


def eprint(*args):
    print(*args, file=sys.stderr)


def find_root(start):
    """Résoudre la racine du dépôt git en remontant depuis `start`.

    Gère les worktrees : dans un worktree, `.git` est un FICHIER (gitlink),
    pas un répertoire. On accepte les deux, sinon le script remonterait à tort
    jusqu'au dépôt principal et lirait la mauvaise branche.
    """
    d = os.path.abspath(start)
    while True:
        git_path = os.path.join(d, ".git")
        if os.path.isdir(git_path) or os.path.isfile(git_path):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            return os.path.abspath(start)
        d = parent


def run(cmd, cwd):
    """Exécuter une commande shell. Retourne (exit_code, stdout, stderr)."""
    try:
        p = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return (
            p.returncode,
            p.stdout.decode("utf-8", "replace"),
            p.stderr.decode("utf-8", "replace"),
        )
    except Exception as exc:  # noqa: BLE001
        return 127, "", str(exc)


def git(cmd, cwd):
    """Sortie stdout de `git <cmd>` si le code retour est 0, sinon ''."""
    code, out, _err = run("git " + cmd, cwd)
    return out if code == 0 else ""


def current_branch(cwd):
    return git("rev-parse --abbrev-ref HEAD", cwd).strip()


def current_head(cwd):
    return git("rev-parse HEAD", cwd).strip()


def compute_state_id(cwd):
    """STATE_ID de l'état complet du chantier (HEAD + diff + untracked)."""
    head = current_head(cwd)
    diff = git("diff --no-ext-diff HEAD", cwd)

    names = sorted(
        n
        for n in git("ls-files --others --exclude-standard", cwd).splitlines()
        if n.strip() and not (n == ".verify" or n.startswith(".verify/"))
    )
    untracked_lines = []
    for name in names:
        path = os.path.join(cwd, name)
        if os.path.isfile(path):
            try:
                with open(path, "rb") as f:
                    h = hashlib.sha256(f.read()).hexdigest()
            except OSError:
                h = "unreadable"
        else:
            h = "dir"
        untracked_lines.append(f"{name} {h}")

    canonical = (
        f"head={head}\n"
        f"diff={hashlib.sha256(diff.encode('utf-8', 'replace')).hexdigest()}\n"
        "untracked:\n"
        + "\n".join(untracked_lines)
    )
    state_id = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return state_id, head


def load_config(root):
    path = os.path.join(root, CONFIG_PATH)
    cfg = dict(DEFAULT_CONFIG)
    if not os.path.isfile(path):
        return cfg, None
    try:
        with open(path, encoding="utf-8") as f:
            user = json.load(f)
    except Exception as exc:  # noqa: BLE001
        return cfg, f"config illisible : {exc}"
    cfg.update(user)
    return cfg, None


def _record(name, verdict, detail):
    return {"name": name, "verdict": verdict, "detail": (detail or "")[:500]}


def run_checks(cfg, root):
    """Exécuter les contrôles déterministes déclarés. Retourne (verdict, results)."""
    results = []
    verdict = "PASS"

    branch = current_branch(root)
    head = current_head(root)
    if not head:
        results.append(_record("git", "BLOCKED", "pas de dépôt git ou aucun commit"))
        return "BLOCKED", results
    if branch in cfg.get("protected_branches", []):
        results.append(
            _record("protected_branch", "BLOCKED", f"sur branche protégée '{branch}'")
        )
        verdict = "BLOCKED"

    for t in cfg.get("tests", []):
        code, out, err = run(t, root)
        detail = (err or out).strip()
        if code == 0:
            results.append(_record(f"test: {t}", "PASS", detail))
        elif code == 127:
            results.append(_record(f"test: {t}", "BLOCKED", f"commande introuvable : {detail}"))
            if verdict != "FAIL":
                verdict = "BLOCKED"
        else:
            results.append(_record(f"test: {t}", "FAIL", detail))
            verdict = "FAIL"

    for c in cfg.get("checks", []):
        if not isinstance(c, dict):
            results.append(_record("check", "BLOCKED", "entrée de check invalide (non-objet)"))
            verdict = "BLOCKED" if verdict != "FAIL" else "FAIL"
            continue
        name = c.get("name", "check")
        cmd = c.get("cmd", "")
        if not cmd:
            results.append(_record(name, "BLOCKED", "commande vide"))
            verdict = "BLOCKED" if verdict != "FAIL" else "FAIL"
            continue
        code, out, err = run(cmd, root)
        detail = (err or out).strip()
        if code == 0:
            results.append(_record(name, "PASS", detail))
        elif code == 127:
            results.append(_record(name, "BLOCKED", f"commande introuvable : {detail}"))
            if verdict != "FAIL":
                verdict = "BLOCKED"
        else:
            msg = c.get("fail_message") or detail
            results.append(_record(name, "FAIL", msg))
            verdict = "FAIL"

    for name, v, detail in check_naming(cfg, root):
        results.append(_record(name, v, detail))
        if v == "FAIL":
            verdict = "FAIL"
        elif v == "BLOCKED" and verdict != "FAIL":
            verdict = "BLOCKED"

    for name, v, detail in check_content(cfg, root):
        results.append(_record(name, v, detail))
        if v == "FAIL":
            verdict = "FAIL"
        elif v == "BLOCKED" and verdict != "FAIL":
            verdict = "BLOCKED"

    return verdict, results


def scoped_files(root, spec, label):
    """Itérateur sur les fichiers couverts par une spec de périmètre.

    `spec` est un dict avec les clés optionnelles :
      dirs         dossiers racines à parcourir (obligatoire, non vide)
      dir_pattern  regex sur les composants du chemin relatif sous chaque dir ;
                   un dossier n'est parcouru que si au moins un composant matche
                   (ex: dossiers de chantier datés YYYY-MM-DD_<sujet>, nichés sous
                   YYYY-MM/).
      only_types   si présent, seuls les fichiers se terminant par _<TYPE>.md
                   (types en MAJUSCULES) sont retenus.
      since        date de coupure YYYY-MM-DD : seuls les fichiers dont le
                   préfixe date est >= since sont retenus.
      exclude      regex sur le chemin relatif complet : fichiers/dossiers exclus.

    Retourne (error_or_None, list_of_relative_paths).
    """
    import re

    dirs = spec.get("dirs", [])
    if not dirs:
        return f"{label}: dirs absents", []
    dir_rx = None
    if spec.get("dir_pattern"):
        try:
            dir_rx = re.compile(spec["dir_pattern"])
        except re.error as exc:
            return f"{label}: dir_pattern invalide : {exc}", []
    only_types = spec.get("only_types") or []
    since = spec.get("since")
    ex_rx = []
    for e in spec.get("exclude", []):
        try:
            ex_rx.append(re.compile(e))
        except re.error as exc:
            return f"{label}: exclude invalide '{e}' : {exc}", []
    files = []
    for d in dirs:
        base = os.path.join(root, d)
        if not os.path.isdir(base):
            continue
        for dirpath, _dirs, names in os.walk(base):
            if dir_rx is not None:
                parts = os.path.relpath(dirpath, base).split(os.sep)
                if parts != ["."] and not any(dir_rx.match(p) for p in parts):
                    continue
            for f in names:
                rel = os.path.relpath(os.path.join(dirpath, f), root)
                if any(e.search(rel) for e in ex_rx):
                    continue
                if only_types and not re.search(
                    r"_(" + "|".join(only_types) + r")\.md$", f
                ):
                    continue
                if since:
                    m = re.match(r"(\d{4}-\d{2}-\d{2})", f)
                    if not m or m.group(1) < since:
                        continue
                files.append(rel)
    return None, files


def _merge_verdict(cur, new):
    """FAIL > BLOCKED > PASS : un FAIL ne redevient jamais PASS/BLOCKED."""
    if cur == "FAIL" or new == "FAIL":
        return "FAIL"
    if cur == "BLOCKED" or new == "BLOCKED":
        return "BLOCKED"
    return "PASS"


def check_naming(cfg, root):
    """Contrôle de nommage, activé uniquement si configuré.

    Retourne une liste de (name, verdict, detail). Le verdict est FAIL si au
    moins un livrable viole la convention, BLOCKED si la config est invalide.
    Un PASS est toujours émis avec le nombre de fichiers scannés : un périmètre
    vide (0 fichier) est ainsi visible, jamais confondu avec une conformité.
    """
    n = cfg.get("naming", {}) or {}
    if not n.get("enabled"):
        return []
    pattern = n.get("pattern")
    if not pattern:
        return [("naming", "BLOCKED", "naming.enabled=true mais pattern absent")]
    import re

    try:
        rx = re.compile(pattern)
    except re.error as exc:
        return [("naming", "BLOCKED", f"pattern invalide : {exc}")]
    err, scoped = scoped_files(root, n, "naming")
    if err:
        return [("naming", "BLOCKED", err)]
    violations = [rel for rel in scoped if not rx.match(os.path.basename(rel))]
    if violations:
        return [("naming", "FAIL", f"{len(violations)} violation(s) sur {len(scoped)} fichier(s) : " + "; ".join(violations[:50]))]
    return [("naming", "PASS", f"{len(scoped)} fichier(s) scanné(s), 0 violation")]


def check_content(cfg, root):
    """Contrôle de contenu interdit (ex: caractère U+2014), activé si configuré.

    Chaque entrée de cfg["content"] déclare :
      name       nom du check (affiché dans le rapport)
      forbidden  chaîne ou regex à chercher dans le contenu des fichiers scopés
      plus le périmètre commun (dirs, dir_pattern, only_types, since, exclude).

    Retourne une liste de (name, verdict, detail) par entrée. Le nom de la
    config est respecté (pas de "content" générique). Un PASS émet le nombre
    de fichiers scannés : un périmètre vide n'est pas une conformité.
    """
    import re

    entries = cfg.get("content", []) or []
    out = []
    for c in entries:
        if not isinstance(c, dict):
            out.append(("content", "BLOCKED", "entrée invalide (non-objet)"))
            continue
        name = c.get("name", "content")
        forbidden = c.get("forbidden")
        if not forbidden:
            out.append((name, "BLOCKED", "forbidden absent"))
            continue
        try:
            rx = re.compile(forbidden)
        except re.error as exc:
            out.append((name, "BLOCKED", f"forbidden invalide : {exc}"))
            continue
        err, scoped = scoped_files(root, c, name)
        if err:
            out.append((name, "BLOCKED", err))
            continue
        violations = []
        for rel in scoped:
            path = os.path.join(root, rel)
            try:
                with open(path, encoding="utf-8", errors="replace") as fh:
                    content = fh.read()
            except OSError as exc:
                violations.append(f"illisible {rel} : {exc}")
                continue
            if rx.search(content):
                violations.append(rel)
        if violations:
            out.append((name, "FAIL", f"{len(violations)} fichier(s) sur {len(scoped)} contiennent le contenu interdit : " + "; ".join(violations[:50])))
        else:
            out.append((name, "PASS", f"{len(scoped)} fichier(s) scanné(s), 0 occurrence"))
    return out


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def cmd_check(cfg, root):
    verdict, results = run_checks(cfg, root)
    state_id, head = compute_state_id(root)
    pending = {
        "schema": 1,
        "task": cfg.get("task", "default"),
        "deterministic": verdict,
        "head": head,
        "state_id": state_id,
        "created_at": now_iso(),
    }
    report = dict(pending)
    report["checks"] = results
    os.makedirs(os.path.dirname(os.path.join(root, PENDING_PATH)) or ".", exist_ok=True)
    with open(os.path.join(root, PENDING_PATH), "w", encoding="utf-8") as f:
        json.dump(pending, f, indent=2, ensure_ascii=False)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return {"PASS": 0, "FAIL": 1, "BLOCKED": 2}[verdict]


def cmd_state_id(cfg, root):
    state_id, _head = compute_state_id(root)
    print(state_id)
    return 0


def cmd_report(cfg, root):
    """Rapport de suivi lisible (markdown), sans effet de bord ni fichier."""
    verdict, results = run_checks(cfg, root)
    state_id, head = compute_state_id(root)
    branch = current_branch(root)
    out = [
        f"- Branche : `{branch or '?'}`",
        f"- Verdict déterministe : **{verdict}**",
        f"- STATE_ID : `{state_id}`",
        f"- HEAD : `{head[:12] if head else '?'}`",
        "",
        "| Check | Verdict |",
        "|---|---|",
    ]
    for r in results:
        out.append(f"| {r['name']} | {r['verdict']} |")
    print("\n".join(out))
    return {"PASS": 0, "FAIL": 1, "BLOCKED": 2}[verdict]


def _load_findings(root, findings_file):
    """Charger les findings du reviewer depuis un fichier JSON, si fourni.

    Retourne (findings, error). findings est une liste (possiblement vide) ;
    error est une chaîne non vide si le fichier est illisible/invalide.
    """
    if not findings_file:
        return [], None
    path = os.path.join(root, findings_file)
    if not os.path.isfile(path):
        return [], f"{findings_file} introuvable"
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except Exception as exc:  # noqa: BLE001
        return [], f"{findings_file} illisible : {exc}"
    if not isinstance(data, list):
        return [], f"{findings_file} doit contenir une liste de findings"
    return data, None


def cmd_certify(cfg, root, review, findings_file=None, review_note=None):
    if review not in VERDICTS:
        eprint(f"--review doit être l'un de {VERDICTS}")
        return 2
    pending_path = os.path.join(root, PENDING_PATH)
    if not os.path.isfile(pending_path):
        eprint(f"{PENDING_PATH} absent : lancer `check` d'abord")
        return 2
    with open(pending_path, encoding="utf-8") as f:
        try:
            pending = json.load(f)
        except Exception as exc:  # noqa: BLE001
            eprint(f"{PENDING_PATH} illisible : {exc}")
            return 2

    findings, findings_error = _load_findings(root, findings_file)
    if findings_error:
        eprint(f"BLOCKED: {findings_error}")
        return 2

    state_id, head = compute_state_id(root)
    pending_state = pending.get("state_id")
    state_changed = state_id != pending_state

    deterministic = pending.get("deterministic", "PASS")
    if state_changed:
        final = "FAIL"
    elif deterministic != "PASS":
        final = deterministic
    else:
        final = review

    result = {
        "schema": 1,
        "task": pending.get("task", cfg.get("task", "default")),
        "verdict": final,
        "head": head,
        "state_id": f"sha256:{state_id}",
        "deterministic": deterministic,
        "review": review,
        "state_changed": state_changed,
        "created_at": now_iso(),
    }
    if review_note:
        result["review_note"] = review_note
    if findings:
        result["findings"] = findings
    os.makedirs(os.path.dirname(os.path.join(root, RESULT_PATH)) or ".", exist_ok=True)
    with open(os.path.join(root, RESULT_PATH), "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return {"PASS": 0, "FAIL": 1, "BLOCKED": 2}[final]


def review_local(deliverable_path, model):
    """Revue sémantique stateless d'un livrable par Ollama.

    Retourne (verdict, findings, note). verdict est PASS/FAIL/BLOCKED ;
    findings est la liste brute du reviewer ; note est un motif de BLOCKED ou
    un avertissement (modèle hors table). La sortie LLM est strictement
    advisory : convertie en grammaire close (anti-fausse-précision,
    knowledge.md §3.5) : forme tolérante (fences), grammaire stricte
    (OK/VIOLATION, PASS/FAIL/BLOCKED), toute anomalie → BLOCKED, jamais PASS.
    """
    if not os.path.isfile(deliverable_path):
        return "BLOCKED", [], f"livrable introuvable : {deliverable_path}"
    try:
        with open(deliverable_path, encoding="utf-8") as f:
            doc = f.read()
    except OSError as exc:
        return "BLOCKED", [], f"livrable illisible : {exc}"

    name = os.path.basename(deliverable_path)
    prompt = ROLE + "\n" + CONTRACT + ENUM + "\n\n" + name + "\n\nLIVRABLE À EXAMINER :\n\n" + doc

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "options": {"temperature": REVIEW_TEMP, "num_predict": REVIEW_NUM_PREDICT},
    }
    payload.update(REVIEW_MODEL_OPTIONS.get(model, {"format": "json"}))
    warn = "" if model in REVIEW_MODEL_OPTIONS else f"modèle inconnu '{model}' : options par défaut"

    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=REVIEW_TIMEOUT) as resp:
            body = json.loads(resp.read().decode())
    except Exception as exc:  # noqa: BLE001
        return "BLOCKED", [], f"Ollama injoignable : {exc}"

    raw = body.get("response", "").strip()
    if raw.startswith("```"):
        raw = raw.strip("`")
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()
    try:
        data = json.loads(raw)
    except Exception as exc:  # noqa: BLE001
        return "BLOCKED", [], f"réponse non parsable en JSON : {exc}"

    points = data.get("points")
    verdict = data.get("verdict")
    findings = data.get("findings")
    if not isinstance(points, dict) or set(points.keys()) != set(REVIEW_POINTS):
        return "BLOCKED", [], f"points absents ou incomplets (attendu {','.join(REVIEW_POINTS)})"
    bad = [k for k in REVIEW_POINTS if points.get(k) not in ("OK", "VIOLATION")]
    if bad:
        return "BLOCKED", [], f"valeurs de points inconnues : {','.join(bad)}"
    if verdict not in VERDICTS:
        return "BLOCKED", [], f"verdict inconnu : {verdict!r}"
    if not isinstance(findings, list):
        return "BLOCKED", [], "findings doit être une liste"

    if verdict == "PASS":
        if any(points[k] == "VIOLATION" for k in REVIEW_POINTS):
            return "BLOCKED", findings, "verdict PASS incohérent avec des points VIOLATION"
        return "PASS", findings, warn or None
    if verdict == "FAIL":
        return "FAIL", findings, warn or None
    return "BLOCKED", findings, warn or "le reviewer a rendu BLOCKED"


def cmd_gate(cfg, root, deliverable=None, model=None):
    """check + review-local + certify en une commande (spec gate, étape 9)."""
    model = model or REVIEW_MODEL_DEFAULT

    # 1. check déterministe (mêmes contrôles et STATE_ID que `check`)
    verdict, results = run_checks(cfg, root)
    state_id, head = compute_state_id(root)
    pending = {
        "schema": 1,
        "task": cfg.get("task", "default"),
        "deterministic": verdict,
        "head": head,
        "state_id": state_id,
        "created_at": now_iso(),
    }
    os.makedirs(os.path.dirname(os.path.join(root, PENDING_PATH)) or ".", exist_ok=True)
    with open(os.path.join(root, PENDING_PATH), "w", encoding="utf-8") as f:
        json.dump(pending, f, indent=2, ensure_ascii=False)
    report = dict(pending)
    report["checks"] = results
    print(json.dumps(report, indent=2, ensure_ascii=False), file=sys.stderr)

    # 2. check non PASS → arrêt : jamais de revue d'un état non conforme
    if verdict != "PASS":
        eprint(f"gate : check déterministe = {verdict} → pas de revue locale")
        return cmd_certify(
            cfg, root, "BLOCKED", None,
            review_note=f"revue locale non exécutée (check déterministe = {verdict})",
        )

    # 3. revue locale (advisory) sur le livrable demandé
    if not deliverable:
        eprint("gate : --file requis pour la revue sémantique (check déterministe = PASS)")
        return cmd_certify(
            cfg, root, "BLOCKED", None,
            review_note="revue locale non exécutée (--file absent)",
        )
    path = deliverable if os.path.isabs(deliverable) else os.path.join(root, deliverable)
    review, findings, note = review_local(path, model)
    eprint(f"gate : revue locale {model} → {review}")
    if note:
        eprint(f"gate : note : {note}")

    # 4. persister les findings puis certifier (format officiel)
    findings_file = None
    if findings:
        findings_file = FINDINGS_PATH
        with open(os.path.join(root, findings_file), "w", encoding="utf-8") as f:
            json.dump(findings, f, indent=2, ensure_ascii=False)
    return cmd_certify(cfg, root, review, findings_file, review_note=note)


def usage():
    print(
        "usage: verify.py check | state-id | report | certify --review PASS|FAIL|BLOCKED [--findings-file <fichier.json>] | gate [--file <livrable>] [--model <modèle>]"
    )
    return 2


def main(argv):
    if not argv:
        return usage()
    mode = argv[0]
    root = find_root(os.getcwd())
    cfg, cfg_error = load_config(root)
    if cfg_error:
        eprint(f"BLOCKED: {cfg_error}")
        return 2

    if mode in ("check", "verify"):
        return cmd_check(cfg, root)
    if mode == "state-id":
        return cmd_state_id(cfg, root)
    if mode == "report":
        return cmd_report(cfg, root)
    if mode == "certify":
        review = "BLOCKED"  # fail-safe : jamais PASS sans verdict de reviewer explicite
        if "--review" in argv:
            i = argv.index("--review")
            if i + 1 < len(argv):
                review = argv[i + 1].upper()
        findings_file = None
        if "--findings-file" in argv:
            i = argv.index("--findings-file")
            if i + 1 < len(argv):
                findings_file = argv[i + 1]
        return cmd_certify(cfg, root, review, findings_file)
    if mode == "gate":
        deliverable = None
        if "--file" in argv:
            i = argv.index("--file")
            if i + 1 < len(argv):
                deliverable = argv[i + 1]
        model = REVIEW_MODEL_DEFAULT
        if "--model" in argv:
            i = argv.index("--model")
            if i + 1 < len(argv):
                model = argv[i + 1]
        return cmd_gate(cfg, root, deliverable, model)
    return usage()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
