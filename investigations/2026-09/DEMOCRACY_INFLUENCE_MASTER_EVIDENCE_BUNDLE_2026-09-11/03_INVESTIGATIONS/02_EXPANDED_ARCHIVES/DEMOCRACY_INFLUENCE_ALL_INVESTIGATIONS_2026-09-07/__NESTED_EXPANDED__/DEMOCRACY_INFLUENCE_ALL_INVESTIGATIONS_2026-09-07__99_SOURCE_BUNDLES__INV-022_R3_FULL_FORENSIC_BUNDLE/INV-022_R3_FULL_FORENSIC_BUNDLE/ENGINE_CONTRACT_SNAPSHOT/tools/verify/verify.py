#!/usr/bin/env python3
"""verify.py — Moteur de vérification déterministe, générique et indépendant du projet.

Le moteur ne connaît AUCUNE règle de projet. Toutes les règles sont déclarées
dans `.verify/config.json` : commandes de test, commandes de contrôle
arbitraires, convention de nommage. C'est ce fichier qui rend l'outil
adaptable à n'importe quel projet.

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
  gate      check + certify, en une commande, sans revue LLM. Le verdict est
            le déterministe seul. Avec --kernel-contract pre|delivery, applique
            aussi les invariants machine du KERNEL dont la version est explicitement supportée par ce vérificateur,
            notamment NO_UNCERTIFIED_FINAL, SEMANTIC_IR_OK, FORENSIC_PROJECTION_OK, TRACE_COMPLETENESS_OK,
            INSPECTED_TRACE_OK, PROVENANCE_ACCOUNTING_OK, QUERY_ACCOUNTING_OK et WRITEBACK_BLOCK_REASON_OK. En 2.10.6, `query target/actual` est interdit; SEARCH_ACTIVITY_V1 et SEMANTIC_COUNTS_V1 sont dérivés des registres runtime.
            Code retour 0/1/2 comme check.

Usage :
  python3 tools/verify/verify.py check
  python3 tools/verify/verify.py state-id
  python3 tools/verify/verify.py certify --review PASS|FAIL|BLOCKED|N/A [--findings-file <fichier.json>]
  python3 tools/verify/verify.py gate [--file <livrable>] [--kernel-contract pre|delivery]
  (--findings-file : persiste les findings du reviewer dans result.json)
"""

import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

CONFIG_PATH = ".verify/config.json"
PENDING_PATH = ".verify/pending.json"
RESULT_PATH = ".verify/result.json"

VERDICTS = ("PASS", "FAIL", "BLOCKED")
SUPPORTED_KERNEL_VERSIONS = ("2.10.6",)
SUPPORTED_BUNDLE_REVISIONS = ("R3",)

CANONICAL_SECTIONS = (
    "TEMPORAL_STATE", "MANIPULATION_REPORT", "MODULE_EXECUTION", "SCOPING_REPORT", "CREDO",
    "LEAD_REGISTRY", "INVESTIGATION_MAP", "COGNITIVE_MAP", "DIALECTICAL_MAP",
    "CLAIM_REGISTRY", "RESOURCE_FLOW_MAP", "ACTOR_NETWORK_MAP", "CONTROL_MAP",
    "CAUSALITY_REGISTRY", "IMPACT_MAP", "STATUS_DELTA", "CONTRADICTION_LEDGER",
    "VERIFICATION_REPORT", "TRACE_MATRIX", "EDI_REPORT", "RESPONSIBILITY_MAP",
    "OPEN_GAPS", "NEXT_QUERIES", "GATE_STATUS_V1",
)
DERIVED_SECTIONS = {
    "LEAD_REGISTRY", "INVESTIGATION_MAP", "CLAIM_REGISTRY", "CONTROL_MAP",
    "CAUSALITY_REGISTRY", "STATUS_DELTA", "TRACE_MATRIX", "OPEN_GAPS",
}


DEFAULT_CONFIG = {
    "version": 1,
    "task": "default",
    "tests": [],
    "checks": [],
    "naming": {"enabled": False},
}


def eprint(*args):
    print(*args, file=sys.stderr)


def find_root(start):
    """Résoudre la racine Git en remontant depuis `start`.

    Accepte `.git` comme répertoire ou fichier afin de rester compatible avec
    les dispositions Git valides. La topologie Git n'influence jamais le verdict.
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

    head = current_head(root)
    if not head:
        results.append(_record("git", "BLOCKED", "pas de dépôt git ou aucun commit"))
        return "BLOCKED", results

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



def _kernel_text(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except OSError as exc:
        return None, f"livrable KERNEL illisible : {exc}"
    # Tolère un rendu Markdown échappé lors d'un copier-coller, sans modifier le fichier.
    for a, b in ((r"\|", "|"), (r"\_", "_"), (r"\:", ":")):
        text = text.replace(a, b)
    return text, None


def _file_sha256(path):
    """SHA-256 of one deliverable file, independent from repository STATE_ID."""
    try:
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                h.update(chunk)
        return h.hexdigest(), None
    except OSError as exc:
        return None, str(exc)


def _kernel_declared_versions(path):
    """Return ENGINE versions declared by a candidate KERNEL artifact."""
    import re
    text, err = _kernel_text(path)
    if err:
        return set(), err
    versions = set(re.findall(r"\b(?:ENGINE_VERSION|ENGINE)\s*[:=]\s*([0-9]+(?:\.[0-9]+){1,2})\b", text))
    return versions, None


def _looks_like_kernel_artifact(path):
    """Conservative detection used only to forbid generic certification."""
    import re
    text, err = _kernel_text(path)
    if err:
        return False
    return bool(
        re.search(r"\b(?:ENGINE_VERSION|ENGINE)\s*[:=]\s*[0-9]+(?:\.[0-9]+){1,2}\b", text)
        and re.search(r"\bRUN_ID\s*[:=]", text)
        and re.search(r"\bMISSION_MODE\s*[:=]", text)
    )


def _ints(pattern, text):
    import re
    return [int(x) for x in re.findall(pattern, text, flags=re.MULTILINE)]


def _kernel_fact_rows(text):
    """Parse FACT_REGISTRY_V1 machine rows into {id: fields}."""
    import re
    rows = {}
    duplicates = set()
    for raw in text.splitlines():
        line = raw.strip().lstrip("|").strip()
        if not re.match(r"^FCT-\d+\s*\|", line):
            continue
        parts = [p.strip() for p in line.split("|")]
        # FACT row = 9 fields and field 2 is an EPI, not QRY/ELIGIBLE.
        if len(parts) < 2 or parts[1] not in {
            "FACT", "EVIDENCE", "INFERENCE", "HYPOTHESIS", "SPECULATION", "UNKNOWN"
        }:
            continue
        try:
            n = int(parts[0].split("-")[1])
        except Exception:  # noqa: BLE001
            continue
        if n in rows:
            duplicates.add(n)
        rows[n] = parts
    return rows, duplicates


def _kernel_refutation_rows(text):
    import re
    rows = {}
    duplicates = set()
    rx = re.compile(r"^\s*\|?\s*FCT-(\d+)\s*\|\s*QRY-(\d+)\s*\|\s*(NONE|FOUND_RESOLVED)\s*\|?\s*$")
    for raw in text.splitlines():
        m = rx.match(raw)
        if not m:
            continue
        fct, qry, status = int(m[1]), int(m[2]), m[3]
        if fct in rows:
            duplicates.add(fct)
        rows[fct] = (qry, status)
    return rows, duplicates


def _kernel_writeback_plan(text):
    import re
    rows = {}
    duplicates = set()
    rx = re.compile(
        r"^\s*\|?\s*FCT-(\d+)\s*\|\s*(ELIGIBLE:CONFIRME|ELIGIBLE:VERIFIE|SKIP:[^|]+?)\s*\|?\s*$"
    )
    for raw in text.splitlines():
        m = rx.match(raw)
        if not m:
            continue
        fct, action = int(m[1]), m[2].strip()
        if fct in rows:
            duplicates.add(fct)
        rows[fct] = action
    return rows, duplicates


def _kernel_checkpoint_rows(text):
    import re
    rows = {}
    labels = []
    duplicates = set()
    rx = re.compile(r"^\s*\|?\s*CP-(\d+)\s*\|\s*([^|]+?)\s*\|\s*PASS\s*\|")
    for raw in text.splitlines():
        m = rx.match(raw)
        if not m:
            continue
        seq, label = int(m[1]), m[2].strip()
        if seq in rows:
            duplicates.add(seq)
        rows[seq] = label
        labels.append(label)
    return rows, labels, duplicates


def _kernel_checkpoint_details(text):
    """Parse canonical checkpoint rows including LAST_COMPLETED/NEXT_ACTION."""
    import re
    rows = {}
    rx = re.compile(
        r"^\s*\|?\s*CP-(\d+)\s*\|\s*([^|]+?)\s*\|\s*PASS\s*\|"
        r"\s*LAST_COMPLETED:([^|]+?)\s*\|\s*NEXT_ACTION:([^|]+?)\s*\|?\s*$"
    )
    for raw in text.splitlines():
        m = rx.match(raw)
        if not m:
            continue
        rows[int(m[1])] = {
            "label": m[2].strip(),
            "last_completed": m[3].strip(),
            "next_action": m[4].strip(),
            "raw": raw.strip(),
        }
    return rows


def _checkpoint_phase_rank(label):
    """Canonical ordering rank for successful KERNEL checkpoints."""
    u = (label or "").strip().upper()
    if u == "LEADS": return 5
    if u == "SCOPE": return 7
    if u.startswith("SEARCH"): return 9
    if u == "FACTS": return 10
    if u.startswith("CAUSAL"): return 11
    if u == "VERIFY": return 13
    if u == "INVESTIGATION_ACCOUNTABILITY": return 17
    if u.startswith("CORRECTION") or u.startswith("FINALIZATION_BLOCKED"): return 18
    return None


def _kernel_logged_queries(text):
    """REQUEST_LOG rows must start with QRY-### and contain exactly one material query id."""
    import re
    marker = re.search(r"(?mi)^#{1,6}\s+REQUEST_LOG\b", text)
    if not marker:
        return {}, {"missing_request_log"}
    body = text[marker.end():]
    rows = {}
    errors = set()
    rx = re.compile(r"^\s*\|?\s*QRY-(\d+)\s*\|")
    for raw in body.splitlines():
        m = rx.match(raw)
        if not m:
            continue
        q = int(m[1])
        if q in rows:
            errors.add(f"duplicate_qry_{q:03d}")
        rows[q] = raw.strip()
    return rows, errors


def _kernel_logged_query_details(text):
    """Parse machine REQUEST_LOG QRY rows into mode/result/source/url/query fields."""
    import re
    marker = re.search(r"(?mi)^#{1,6}\s+REQUEST_LOG\b", text)
    if not marker:
        return {}
    body = text[marker.end():]
    rows = {}
    for raw in body.splitlines():
        line = raw.strip().lstrip("|").strip()
        if not re.match(r"^QRY-\d+\s*\|", line):
            continue
        parts = [p.strip() for p in line.split("|")]
        try:
            q = int(parts[0].split("-")[1])
        except Exception:  # noqa: BLE001
            continue
        rows[q] = {
            "mode": parts[1] if len(parts) > 1 else "",
            "result": parts[2] if len(parts) > 2 else "",
            "source": parts[3] if len(parts) > 3 else "",
            "url": parts[4] if len(parts) > 4 else "",
            "query": parts[5] if len(parts) > 5 else "",
            "raw": raw.strip(),
        }
    return rows


def _kernel_logged_sys_details(text):
    """Parse machine SYS rows from REQUEST_LOG."""
    import re
    marker = re.search(r"(?mi)^#{1,6}\s+REQUEST_LOG\b", text)
    if not marker:
        return []
    body = text[marker.end():]
    rows = []
    for raw in body.splitlines():
        line = raw.strip().lstrip("|").strip()
        if not re.match(r"^SYS-\d+\s*\|", line):
            continue
        parts = [p.strip() for p in line.split("|")]
        rows.append({
            "id": parts[0] if len(parts)>0 else "",
            "mode": parts[1] if len(parts)>1 else "",
            "result": parts[2] if len(parts)>2 else "",
            "tool": parts[3] if len(parts)>3 else "",
            "ref": parts[4] if len(parts)>4 else "",
            "call": parts[5] if len(parts)>5 else "",
            "raw": raw.strip(),
        })
    return rows


def _norm_url(value):
    value = (value or "").strip().replace("\\", "")
    if not value.lower().startswith(("http://", "https://")):
        return value
    return value.rstrip("/")


def _semantic_tokens(value):
    import unicodedata
    raw = unicodedata.normalize("NFKD", value or "")
    raw = "".join(ch for ch in raw if not unicodedata.combining(ch)).lower()
    return re.findall(r"[a-z0-9]+", raw)


def _refutation_alignment_error(subject, query_row):
    result = str(query_row.get("result", "")).strip().upper()
    if result.startswith(("FAIL", "ERROR", "BLOCKED", "UNEXECUTED")):
        return f"résultat QRY non exécuté ({result or 'EMPTY'})"
    query_text = str(query_row.get("query", "")).strip()
    if not re.match(r"(?i)^REFUTATION(?:\b|[_:-])", query_text):
        return "texte QRY sans préfixe REFUTATION"
    subject_tokens = _semantic_tokens(subject)
    query_tokens = set(_semantic_tokens(query_text))
    numeric = {t for t in subject_tokens if t.isdigit()}
    if not numeric.issubset(query_tokens):
        return "discriminateur numérique du sujet absent"
    stop = {
        "a", "an", "and", "control", "controle", "d", "de", "des", "du", "et",
        "fact", "fait", "la", "le", "les", "l", "of", "ou", "the", "un", "une",
    }
    anchors = {t for t in subject_tokens if not t.isdigit() and len(t) >= 3 and t not in stop}
    if not anchors:
        anchors = {t for t in subject_tokens if not t.isdigit() and len(t) >= 3}
    if not anchors or not (anchors & query_tokens):
        return "aucun ancrage lexical stable du sujet"
    return None


def _gap_is_typed(payload):
    gap_type = payload.get("gap_type") or payload.get("GAP_TYPE")
    gap_text = payload.get("gap") or payload.get("reason") or payload.get("question")
    return (
        str(gap_type or "").strip().upper() not in {"", "-", "NONE", "NULL", "UNSPECIFIED"}
        and bool(str(gap_text or "").strip())
    )


def _kernel_section_status(text):
    rows = re.findall(r"(?m)^\s*SECTION_STATUS_V1:(\{[^\n]+\})\s*$", text)
    if len(rows) != 1:
        return {}, [f"SECTION_STATUS_V1 attendu une fois, trouvé {len(rows)}"]
    try:
        status = json.loads(rows[0])
    except Exception as exc:  # noqa: BLE001
        return {}, [f"SECTION_STATUS_V1 JSON invalide: {exc}"]
    errors = []
    if set(status) != set(CANONICAL_SECTIONS):
        missing = sorted(set(CANONICAL_SECTIONS) - set(status))
        extra = sorted(set(status) - set(CANONICAL_SECTIONS))
        if missing: errors.append("sections absentes: " + ",".join(missing))
        if extra: errors.append("sections inconnues: " + ",".join(extra))
    for name in CANONICAL_SECTIONS:
        value = status.get(name)
        expected = {"DERIVED"} if name in DERIVED_SECTIONS else {"SET", "EMPTY"}
        if name == "GATE_STATUS_V1": expected = {"SET"}
        if value not in expected:
            errors.append(f"{name}:{value or 'ABSENT'}")
    return status, errors


def _kernel_writeback_attempts(text):
    heading = re.search(r"(?mi)^#{1,6}\s+WRITEBACK_ATTEMPT_LOG_V1\s*$", text)
    if not heading:
        return [], ["WRITEBACK_ATTEMPT_LOG_V1 absent"]
    tail = text[heading.end():]
    nxt = re.search(r"(?m)^#{1,6}\s+", tail)
    body = tail[:nxt.start()] if nxt else tail
    rows = []
    errors = []
    for raw in body.splitlines():
        m = re.match(r"^\s*ATTEMPT-(\d{3})\s*\|\s*(\{.*\})\s*$", raw)
        if not m:
            continue
        try:
            payload = json.loads(m[2])
        except Exception as exc:  # noqa: BLE001
            errors.append(f"ATTEMPT-{m[1]} JSON invalide: {exc}")
            continue
        payload["seq"] = int(m[1])
        rows.append(payload)
    if [x["seq"] for x in rows] != list(range(1, len(rows) + 1)):
        errors.append("tentatives de persistance non contiguës")
    return rows, errors


def _kernel_writeback_exec_rows(text):
    """Parse observed per-fact writeback execution rows."""
    import re
    rows = {}
    duplicates = set()
    rx = re.compile(
        r"^\s*\|?\s*FCT-(\d+)\s*\|\s*(ELIGIBLE:CONFIRME|ELIGIBLE:VERIFIE|SKIP(?::[^|]+)?)\s*\|"
        r"\s*attempted:(\d+)\s*\|\s*success:(\d+)\s*\|\s*failure:(\d+)\s*\|\s*blocked:(\d+)"
        r"(?:\s*\|\s*reason:([^|]+?))?\s*\|?\s*$"
    )
    for raw in text.splitlines():
        m = rx.match(raw)
        if not m:
            continue
        n = int(m[1])
        if n in rows:
            duplicates.add(n)
        rows[n] = {
            "action": m[2].strip(),
            "attempted": int(m[3]),
            "success": int(m[4]),
            "failure": int(m[5]),
            "blocked": int(m[6]),
            "reason": (m[7] or "").strip(),
        }
    return rows, duplicates



def _kernel_source_rows(text):
    """Parse canonical 9-field SRC rows with complete forensic provenance."""
    rows={}; duplicates=set(); errors=[]
    heading=re.search(r"(?mi)^#{1,6}\s+EVIDENCE_REGISTRY\s*$",text)
    if not heading: return {},set(),["EVIDENCE_REGISTRY absent"]
    tail=text[heading.end():]; nxt=re.search(r"(?m)^#{1,6}\s+",tail); body=tail[:nxt.start()] if nxt else tail
    for raw in body.splitlines():
        line=raw.strip().lstrip("|").strip()
        if not re.match(r"^SRC-\d+\s*\|",line): continue
        parts=[x.strip() for x in line.split("|")]
        try: sid=int(parts[0].split("-")[1])
        except Exception: continue
        if sid in rows: duplicates.add(sid); continue
        if len(parts)!=9:
            errors.append(f"SRC-{sid:03d}: 9 champs attendus, {len(parts)} trouvés")
            continue
        _id,role,fam_field,canonical_id,title,pub,checked,locator,url=parts
        if role not in {"◈","◉","○"}: errors.append(f"SRC-{sid:03d}: rôle source ambigu/absent")
        if not fam_field.startswith("fam:"): errors.append(f"SRC-{sid:03d}: fam: explicite absent"); family=""
        else: family=fam_field[4:].strip()
        if not re.fullmatch(r"(?:[A-E]|other:[a-z0-9][a-z0-9_-]{0,47})",family): errors.append(f"SRC-{sid:03d}: famille invalide")
        for label,val in (("canonical_id",canonical_id),("title",title),("publication_date",pub),("checked_at",checked),("locator",locator),("url/input_ref",url)):
            if not val: errors.append(f"SRC-{sid:03d}: {label} absent")
        rows[sid]={"role":role,"family":family,"url":_norm_url(url),"canonical_id":canonical_id,"title":title,"publication_date":pub,"checked_at":checked,"locator":locator,"raw":raw.strip()}
    return rows,duplicates,errors

def _kernel_fct_source_map(text):
    """Parse explicit FCT_SOURCE_MAP_V1 section."""
    import re
    heading = re.search(r"(?mi)^#{1,6}\s+FCT_SOURCE_MAP_V1\s*$", text)
    if not heading:
        return {}, set(), ["FCT_SOURCE_MAP_V1 absent"]
    tail = text[heading.end():]
    nxt = re.search(r"(?m)^#{1,6}\s+", tail)
    body = tail[:nxt.start()] if nxt else tail

    rows = {}
    duplicates = set()
    errors = []
    rx = re.compile(r"^\s*\|?\s*FCT-(\d+)\s*\|\s*([^|]+?)\s*\|?\s*$")
    for raw in body.splitlines():
        m = rx.match(raw)
        if not m:
            continue
        fid = int(m[1])
        if fid in rows:
            duplicates.add(fid)
        raw_refs = m[2].strip()
        if raw_refs in ("-", "—"):
            rows[fid] = []
            continue
        refs = []
        for token in [x.strip() for x in raw_refs.split(",") if x.strip()]:
            sm = re.fullmatch(r"SRC-(\d+)", token)
            if not sm:
                errors.append(f"FCT-{fid:03d}: mapping source invalide '{token}'")
                continue
            refs.append(int(sm[1]))
        if len(refs) != len(set(refs)):
            errors.append(f"FCT-{fid:03d}: SRC dupliqué dans mapping")
        rows[fid] = refs
    return rows, duplicates, errors


def _family_tokens(value):
    import re
    return {
        x.strip()
        for x in re.split(r"[+,;]", value or "")
        if x.strip() and x.strip() not in {"-", "—"}
    }


def _family_count(value):
    return len(_family_tokens(value))


def _fact_mem(parts):
    if len(parts) < 9:
        return None
    mem = parts[8].strip()
    if mem.startswith("mem:"):
        mem = mem[4:].strip()
    return mem


def _merge_result_rows(results):
    verdict = "PASS"
    for r in results:
        verdict = _merge_verdict(verdict, r[1])
    return verdict


def _kernel_gate_status(text):
    """Parse `GATE_STATUS_V1 | G0:PASS|...|G10:PASS`.

    Returns (mapping, errors). Exactly one machine row is expected in a FINAL.
    """
    import re
    rows = []
    for raw in text.splitlines():
        if re.match(r"^\s*GATE_STATUS_V1\s*\|", raw):
            rows.append(raw.strip())
    if not rows:
        return {}, ["GATE_STATUS_V1 absent"]
    if len(rows) > 1:
        return {}, [f"GATE_STATUS_V1 dupliqué ({len(rows)} rows)"]
    parts = [p.strip() for p in rows[0].split("|")[1:] if p.strip()]
    mapping = {}
    errors = []
    for part in parts:
        m = re.fullmatch(r"G(10|[0-9])\s*:\s*(PASS|FAIL|BLOCKED|PENDING|UNEXECUTED)", part)
        if not m:
            errors.append("token gate invalide: " + part)
            continue
        gid = int(m.group(1))
        if gid in mapping:
            errors.append(f"G{gid} dupliqué")
        mapping[gid] = m.group(2)
    expected = set(range(0, 11))
    missing = sorted(expected - set(mapping))
    extra = sorted(set(mapping) - expected)
    if missing:
        errors.append("gates absents: " + ",".join(f"G{x}" for x in missing))
    if extra:
        errors.append("gates hors plage: " + ",".join(f"G{x}" for x in extra))
    non_pass = [f"G{x}:{mapping[x]}" for x in sorted(mapping) if mapping[x] != "PASS"]
    if non_pass:
        errors.append("gates non-PASS: " + ",".join(non_pass))
    return mapping, errors


def _kernel_finalization_conflicts(text):
    """Detect explicit self-declarations that a serialized FINAL is not certifiable.

    Scope the textual heuristic to an explicit G0-G10/finalization status section to
    avoid flagging historical discussion elsewhere in the dossier.
    """
    import re
    conflicts = []
    heading = re.search(r"(?mi)^#{1,6}\s+(?:G0\s*[–-]\s*G10\s+status|FINALIZATION(?:_STATUS)?|FINALIZATION STATUS)\s*$", text)
    if not heading:
        return conflicts
    tail = text[heading.end():]
    nxt = re.search(r"(?m)^#{1,6}\s+", tail)
    section = tail[:nxt.start()] if nxt else tail
    if re.search(r"(?i)\b(BLOCKED|FAIL|PENDING|UNEXECUTED|non[- ]certifiable|non[- ]certifi(?:é|e|ed))\b", section):
        conflicts.append("section de finalisation déclare un état non certifiable")
    return conflicts


def _kernel_memory_write_modes(text):
    m=re.search(r"(?mi)^#{1,6}\s+MEMORY_WRITE_MODE_V1\s*$", text)
    if not m: return {},[],["MEMORY_WRITE_MODE_V1 absent"]
    tail=text[m.end():]
    end=re.search(r"(?m)^#{1,6}\s+", tail)
    sec=tail[:end.start()] if end else tail
    rows={}; dups=[]; errors=[]
    for n,mode,mid in re.findall(r"(?m)^\s*FCT-(\d+)\s*\|\s*(WRITE|UPDATE)\s*\|\s*([^|\n]+?)\s*$", sec):
        n=int(n); mid=mid.strip()
        if n in rows: dups.append(n)
        rows[n]=(mode,mid)
        if mode=="UPDATE" and mid in {"","-"}: errors.append(f"FCT-{n:03d}: UPDATE sans origin_memory_id")
        if mode=="WRITE" and mid not in {"","-"}: errors.append(f"FCT-{n:03d}: WRITE avec memory id inattendu")
    return rows,dups,errors



def _present(value):
    if value is None: return False
    if isinstance(value,str): return bool(value.strip())
    if isinstance(value,(list,tuple,set,dict)): return bool(value)
    return True


def _id_items(value):
    if value is None: return []
    if isinstance(value,list): return [str(x) for x in value if str(x).strip() not in {"","-","NONE","NONE_FOUND"}]
    if isinstance(value,str):
        v=value.strip()
        if v in {"","-","NONE","NONE_FOUND"}: return []
        return [x.strip() for x in v.split(",") if x.strip()]
    return []


def _semantic_payload_errors(kind,payload,oid):
    errors=[]; st=str(payload.get("status","")).strip().upper()
    def req(*keys):
        for k in keys:
            if k not in payload or not _present(payload.get(k)): errors.append(f"{oid} missing {k}")
    if kind=="LED":
        req("source_id","locator","lead","kind","materiality","routes","linked_ids","attempt_ids","result_ids","status")
        if str(payload.get("materiality","")).upper() in {"DECISIVE","IMPORTANT"}: req("evidence_excerpt")
        if st in {"SATURATED","GAP"} and not _id_items(payload.get("attempt_ids")): errors.append(f"{oid} terminal LED lacks attempt_ids")
        if st=="SATURATED" and not _id_items(payload.get("result_ids")): errors.append(f"{oid} SATURATED LED lacks result_ids")
    elif kind=="AXS":
        req("axis","question","sought_objects","links","attempt_ids","result_ids","status")
        if st in {"SATURATED","GAP"} and not _id_items(payload.get("attempt_ids")): errors.append(f"{oid} terminal AXS lacks attempt_ids")
        if st=="SATURATED" and not _id_items(payload.get("result_ids")): errors.append(f"{oid} SATURATED AXS lacks result_ids")
        if st in {"N/A","NA"} and not _present(payload.get("reason")): errors.append(f"{oid} N/A lacks reason")
    elif kind=="CLM":
        req("claim","claimant","materiality","support","counter","gap_type","gap","status")
        counter=payload.get("counter")
        if not (_present(counter) or (isinstance(counter,str) and counter.upper()=="NONE_FOUND")): errors.append(f"{oid} counter absent")
        gt=str(payload.get("gap_type","")).strip().upper()
        if gt in {"","NULL","UNSPECIFIED","-"}: errors.append(f"{oid} invalid gap_type")
        if gt!="NONE" and not _present(payload.get("gap")): errors.append(f"{oid} gap description absent")
        if gt=="NONE" and str(payload.get("gap","")).strip().upper() not in {"NONE","N/A"}: errors.append(f"{oid} no-gap claim must set gap=NONE")
    elif kind=="CAU":
        req("mechanism","support","counter","limit","status")
        if st in {"SUPPORTED","SATURATED","REFUTED"}: req("causal_right")
    elif kind=="CTRL": req("control","support","status")
    elif kind=="ACT": req("action","actor","intent","support","status")
    if st in {"GAP","UNKNOWN","UNRESOLVED"} and not _gap_is_typed(payload): errors.append(f"{oid}: GAP non typé ou sans description")
    return errors


def _kernel_semantic_payloads(text):
    kinds=("LED","CLM","AXS","CAU","CTRL","ACT")
    headings={"LED":"LEAD_REGISTRY_V1","CLM":"CLAIM_REGISTRY_V1","AXS":"AXIS_REGISTRY_V1","CAU":"CAUSALITY_REGISTRY_V1","CTRL":"CONTROL_REGISTRY_V1","ACT":"ACTION_REGISTRY_V1"}
    out={k:{} for k in kinds}
    for k,h in headings.items():
        m=re.search(rf"(?mi)^###\s+{re.escape(h)}\s*$",text)
        if not m: continue
        tail=text[m.end():]; end=re.search(r"(?m)^###\s+",tail); sec=tail[:end.start()] if end else tail
        for raw in sec.splitlines():
            rm=re.match(rf"^\s*({k}-\d{{3}})\s*\|\s*(\{{.*\}})\s*$",raw)
            if not rm: continue
            try: out[k][rm[1]]=json.loads(rm[2])
            except Exception: pass
    return out


def _kernel_forensic_projection(text, section_status):
    errors=[]
    root=re.search(r"(?mi)^##\s+FORENSIC_SECTIONS_V1\s*$",text)
    if not root: return ["FORENSIC_SECTIONS_V1 absent"]
    tail=text[root.end():]; end=re.search(r"(?mi)^##\s+TRACE_MATRIX_V1\s*$",tail); body=tail[:end.start()] if end else tail
    report=[x for x in CANONICAL_SECTIONS if x not in DERIVED_SECTIONS and x!="GATE_STATUS_V1"]
    for name in report:
        matches=list(re.finditer(rf"(?mi)^###\s+{re.escape(name)}\s*$",body))
        if len(matches)!=1:
            errors.append(f"projection {name}: heading attendu une fois, trouvé {len(matches)}")
            continue
        start=matches[0].end(); nxt=re.search(r"(?m)^###\s+",body[start:]); sec=body[start:start+nxt.start()] if nxt else body[start:]
        content=sec.strip()
        st=section_status.get(name)
        if st=="SET" and (not content or content=="NONE"): errors.append(f"projection {name}: SET mais vide")
        if st=="EMPTY" and content!="NONE": errors.append(f"projection {name}: EMPTY doit rendre NONE")
    fc=re.findall(r"(?m)^FORENSIC_CONTRACT_V1:SYMBOLS:(\d+)\|MODULE_EXECUTION:(\d+)\|EDI_DECISIVE:(\d+)\|SRC_COMPLETE:(\d+)/(\d+)\s*$",text)
    if len(fc)!=1: errors.append("FORENSIC_CONTRACT_V1 absent/dupliqué")
    else:
        sym,mod,edi,complete,total=map(int,fc[0])
        if sym!=15: errors.append(f"FORENSIC_CONTRACT_V1 symbols={sym} != 15")
        if complete!=total: errors.append(f"FORENSIC_CONTRACT_V1 source completeness {complete}/{total}")
    return errors


def _kernel_trace_projection(text):
    errors=[]; payloads=_kernel_semantic_payloads(text)
    h=re.search(r"(?mi)^##\s+TRACE_MATRIX_V1\s*$",text)
    if not h: return ["TRACE_MATRIX_V1 absent"]
    tail=text[h.end():]; end=re.search(r"(?mi)^##\s+STATUS_DELTA_V1\s*$",tail); sec=tail[:end.start()] if end else tail
    rows={}
    rx=re.compile(r"^\s*((?:LED|AXS|CLM)-\d{3})\s*\|\s*attempts:([^|]+)\|\s*support:([^|]+)\|\s*counter:([^|]+)\|\s*results:([^|]+)\|\s*final:([^|]+)\|\s*gap:([^|]+)\s*$")
    for raw in sec.splitlines():
        m=rx.match(raw)
        if not m: continue
        if m[1] in rows: errors.append(f"TRACE_MATRIX duplicate {m[1]}")
        rows[m[1]]={"attempts":m[2].strip(),"support":m[3].strip(),"counter":m[4].strip(),"results":m[5].strip(),"final":m[6].strip(),"gap":m[7].strip()}
    expected=set(payloads["LED"])|set(payloads["AXS"])|set(payloads["CLM"])
    miss=sorted(expected-set(rows)); extra=sorted(set(rows)-expected)
    if miss: errors.append("TRACE_MATRIX missing: "+",".join(miss))
    if extra: errors.append("TRACE_MATRIX extra: "+",".join(extra))
    for oid,row in rows.items():
        if oid.startswith(("LED-","AXS-","CLM-")) and row["attempts"]=="-": errors.append(f"{oid} TRACE attempts absent")
        if oid.startswith(("LED-","AXS-")) and row["final"].upper()=="SATURATED" and row["results"]=="-": errors.append(f"{oid} TRACE results absent")
    if not re.search(r"(?mi)^##\s+STATUS_DELTA_V1\s*$",text): errors.append("STATUS_DELTA_V1 absent")
    if not re.search(r"(?mi)^##\s+OPEN_GAPS_V1\s*$",text): errors.append("OPEN_GAPS_V1 absent")
    return errors

def _kernel_semantic_registry(text):
    kinds = ("LED","CLM","AXS","CAU","CTRL","ACT")
    count_rows = re.findall(r"(?m)^\s*SEMANTIC_COUNTS_V1:([^\n]+)$", text)
    errors=[]
    declared={}
    if len(count_rows) != 1:
        errors.append(f"SEMANTIC_COUNTS_V1 attendu une fois, trouvé {len(count_rows)}")
    else:
        for tok in count_rows[0].split("|"):
            if ":" not in tok: continue
            k,v=tok.split(":",1)
            if k in kinds and v.isdigit(): declared[k]=int(v)
        if set(declared) != set(kinds):
            errors.append("SEMANTIC_COUNTS_V1 incomplet")
    headings={
        "LED":"LEAD_REGISTRY_V1","CLM":"CLAIM_REGISTRY_V1","AXS":"AXIS_REGISTRY_V1",
        "CAU":"CAUSALITY_REGISTRY_V1","CTRL":"CONTROL_REGISTRY_V1","ACT":"ACTION_REGISTRY_V1",
    }
    observed={}
    for k,h in headings.items():
        m=re.search(rf"(?mi)^###\s+{re.escape(h)}\s*$", text)
        if not m:
            errors.append(f"{h} absent")
            observed[k]=0
            continue
        tail=text[m.end():]
        end=re.search(r"(?m)^###\s+", tail)
        sec=tail[:end.start()] if end else tail
        ids=[]
        for raw in sec.splitlines():
            row_m = re.match(rf"^\s*{k}-(\d{{3}})\s*\|\s*(\{{.*\}})\s*$", raw)
            if not row_m:
                continue
            oid = int(row_m[1]); ids.append(oid)
            try:
                payload = json.loads(row_m[2])
            except Exception as exc:  # noqa: BLE001
                errors.append(f"{k}-{oid:03d}: payload JSON invalide ({exc})")
                continue
            errors.extend(_semantic_payload_errors(k,payload,f"{k}-{oid:03d}"))
        observed[k]=len(ids)
        if ids != list(range(1,len(ids)+1)):
            errors.append(f"{h} IDs non contigus")
        if k in declared and declared[k] != len(ids):
            errors.append(f"{h} count {len(ids)} != déclaré {declared[k]}")
    return declared,observed,errors


def check_kernel_contract(deliverable, phase):
    """Contrôles déterministes du contrat KERNEL supporté. phase = pre | delivery."""
    import re
    results = []
    text, err = _kernel_text(deliverable)
    if err:
        return "BLOCKED", [("kernel:file", "BLOCKED", err)]
    if phase not in ("pre", "delivery"):
        return "BLOCKED", [("kernel:phase", "BLOCKED", "--kernel-contract doit valoir pre ou delivery")]

    # Version compatibility is a tool/runtime contract, not a content-quality failure.
    declared_versions = set(re.findall(r"\b(?:ENGINE_VERSION|ENGINE)\s*[:=]\s*([0-9]+(?:\.[0-9]+){1,2})\b", text))
    supported = set(SUPPORTED_KERNEL_VERSIONS)
    if not declared_versions:
        results.append(("kernel:version", "BLOCKED", "ENGINE_VERSION/ENGINE absent; compatibilité indéterminable"))
    elif len(declared_versions) != 1:
        results.append(("kernel:version", "BLOCKED", "versions ENGINE contradictoires: " + ",".join(sorted(declared_versions))))
    else:
        declared = next(iter(declared_versions))
        if declared not in supported:
            results.append((
                "kernel:version",
                "BLOCKED",
                f"ENGINE {declared} non supporté; verify.py supporte {','.join(SUPPORTED_KERNEL_VERSIONS)}",
            ))
        else:
            results.append(("kernel:version", "PASS", f"ENGINE {declared} compatible verify.py"))
    bundle_rows=set(re.findall(r"\bBUNDLE_REVISION\s*[:=]\s*([A-Za-z0-9._-]+)", text))
    if len(bundle_rows)!=1:
        results.append(("kernel:bundle_revision","BLOCKED",f"BUNDLE_REVISION absent/contradictoire: {sorted(bundle_rows)}"))
    else:
        br=next(iter(bundle_rows))
        if br not in set(SUPPORTED_BUNDLE_REVISIONS):
            results.append(("kernel:bundle_revision","BLOCKED",f"BUNDLE_REVISION {br} non supportée; attendu {','.join(SUPPORTED_BUNDLE_REVISIONS)}"))
        else:
            results.append(("kernel:bundle_revision","PASS",br))

    if not re.search(r"\b(?:STATE\s*[:=]\s*FINAL|MANIFEST\s*:\s*FINAL)\b", text):
        results.append(("kernel:state", "FAIL", "STATE/MANIFEST FINAL absent"))
    else:
        results.append(("kernel:state", "PASS", "FINAL"))

    # NARRATIVE_STABILITY_OK: technical body is explicitly bounded and contains no
    # volatile request identifiers that can silently drift after a replay.
    starts = list(re.finditer(r"(?m)^<!-- NARRATIVE_START -->\s*$", text))
    ends = list(re.finditer(r"(?m)^<!-- NARRATIVE_END -->\s*$", text))
    narrative_errors = []
    if len(starts) != 1 or len(ends) != 1:
        narrative_errors.append(f"bornes narrative attendues 1/1, trouvées {len(starts)}/{len(ends)}")
    elif starts[0].end() >= ends[0].start():
        narrative_errors.append("bornes narrative inversées ou vides")
    else:
        narrative = text[starts[0].end():ends[0].start()]
        volatile = sorted(set(re.findall(r"\bQRY-\d{3}\b", narrative)))
        if volatile:
            narrative_errors.append("IDs QRY volatils dans le corps technique: " + ",".join(volatile))
    if narrative_errors:
        results.append(("kernel:narrative_stability", "FAIL", "; ".join(narrative_errors)))
    else:
        results.append(("kernel:narrative_stability", "PASS", "corps technique borné et sans ID QRY volatil"))

    # SECTION_COMPLETENESS_OK: NOT_INITIALIZED is never silently accepted in FINAL.
    _section_status, section_errors = _kernel_section_status(text)
    if section_errors:
        results.append(("kernel:section_completeness", "FAIL", "; ".join(section_errors)))
    else:
        results.append(("kernel:section_completeness", "PASS", f"{len(CANONICAL_SECTIONS)} sections SET/EMPTY/DERIVED"))

    forensic_errors=_kernel_forensic_projection(text,_section_status)
    if forensic_errors:
        results.append(("kernel:forensic_projection","FAIL","; ".join(forensic_errors)))
    else:
        results.append(("kernel:forensic_projection","PASS","sections forensiques déterministes présentes et cohérentes"))

    # INPUT_KIND_LOCK / ROUTE_OVERRIDE_OK: mechanically observable consistency only.
    route_errors = []
    input_kind_m = re.search(r"\bINPUT_KIND\s*[:=]\s*([A-Z_]+)", text)
    input_kind = input_kind_m[1] if input_kind_m else ""
    parent_m = re.search(r"\bPARENT_RUN_ID\s*[:=]\s*([^|\n]+)", text)
    parent = parent_m[1].strip() if parent_m else ""
    resume_m = re.search(r"\bRESUME_COUNT\s*[:=]\s*(\d+)", text)
    resume_count = int(resume_m[1]) if resume_m else None
    migration_tokens = re.findall(r"\bRESUME_MIGRATION_[A-Z0-9_]+\b", text)
    if not input_kind:
        route_errors.append("INPUT_KIND absent")
    if resume_count is None:
        route_errors.append("RESUME_COUNT absent")
    elif migration_tokens and resume_count == 0:
        route_errors.append("RESUME_MIGRATION_* présent avec RESUME_COUNT=0")
    if input_kind == "UPDATE":
        if parent in ("", "NONE", "PENDING"):
            route_errors.append(f"UPDATE avec PARENT_RUN_ID={parent or 'ABSENT'}")
    elif input_kind:
        if parent and parent != "NONE":
            route_errors.append(f"INPUT_KIND={input_kind} exige PARENT_RUN_ID=NONE, obtenu {parent}")
    if route_errors:
        results.append(("kernel:route_contract", "FAIL", "; ".join(route_errors)))
    else:
        results.append(("kernel:route_contract", "PASS", f"INPUT_KIND={input_kind}, RESUME_COUNT={resume_count}, overrides cohérents"))

    # NO_UNCERTIFIED_FINAL: a serialized FINAL must carry machine-observed G0..G10 PASS
    # and must not simultaneously declare itself blocked/non-certifiable.
    gate_status, gate_errors = _kernel_gate_status(text)
    gate_errors.extend(_kernel_finalization_conflicts(text))
    if gate_errors:
        results.append(("kernel:no_uncertified_final", "FAIL", "; ".join(gate_errors)))
    else:
        results.append(("kernel:no_uncertified_final", "PASS", "G0..G10=PASS; FINAL certifiable"))

    # DELIVERY_STATE_EXTERNAL_ONLY.
    forbidden = ["PRE_GATE_VERDICT", "PRE_STATE_ID", "GATE_VERDICT", "STATE_ID"]
    leaked = [k for k in forbidden if re.search(rf"\b{re.escape(k)}\b", text)]
    if leaked:
        results.append(("kernel:delivery_state_external", "FAIL", "champs runtime sérialisés : " + ", ".join(leaked)))
    else:
        results.append(("kernel:delivery_state_external", "PASS", "aucun verdict/hash runtime sérialisé"))

    # CHECKPOINT_LOG_V1 / CP_COVER_OK.
    cp_rows, cp_labels, cp_dups = _kernel_checkpoint_rows(text)
    seq_m = re.search(r"\bCHECKPOINT_SEQ\s*[:=]\s*(\d+)", text)
    cp_seq = int(seq_m[1]) if seq_m else None
    cp_errors = []
    if cp_dups:
        cp_errors.append("séquences dupliquées " + ",".join(map(str, sorted(cp_dups))))
    if cp_rows:
        expected_seq = list(range(1, max(cp_rows) + 1))
        if sorted(cp_rows) != expected_seq:
            cp_errors.append("séquence non contiguë")
    if cp_seq is None:
        cp_errors.append("CHECKPOINT_SEQ absent")
    elif cp_seq != len(cp_rows):
        cp_errors.append(f"CHECKPOINT_SEQ={cp_seq} mais {len(cp_rows)} rows PASS")

    input_kind_m = re.search(r"\bINPUT_KIND\s*[:=]\s*([A-Z_]+)", text)
    input_kind = input_kind_m[1] if input_kind_m else ""
    cx_m = re.search(r"\b(?:COMPLEXITY|complexity)\s*[:=]\s*[^\n|]*?(SIMPLE|MEDIUM|COMPLEX|APEX)\b", text)
    cx = cx_m[1] if cx_m else ""
    required = ["SCOPE", "FACTS", "VERIFY", "INVESTIGATION_ACCOUNTABILITY"]
    if input_kind == "DOCUMENT" or cx in ("COMPLEX", "APEX"):
        required.append("LEADS")
    all_qry_refs = _ints(r"\bQRY-(\d+)\b", text)
    if all_qry_refs:
        required.append("SEARCH")
    if re.search(r"\bCAU-\d+\b", text) or re.search(r"CAUSAL_ROUTE\s*[:=]\s*(?:REQUIRED|OPTIONAL)", text):
        required.append("CAUSAL")
    for req in required:
        if not any(label == req or label.startswith(req + ":") or (req == "CAUSAL" and label.startswith("CAUSAL_")) for label in cp_labels):
            cp_errors.append("checkpoint requis absent: " + req)
    if cp_errors:
        results.append(("kernel:checkpoints", "FAIL", "; ".join(cp_errors)))
    else:
        results.append(("kernel:checkpoints", "PASS", f"{len(cp_rows)} checkpoint(s), couverture route OK"))

    # CHECKPOINT_ORDER_OK: checkpoints cannot be retroactively inserted out of phase order.
    cp_order_errors = []
    cp_details = _kernel_checkpoint_details(text)
    if set(cp_details) != set(cp_rows):
        missing_detail = sorted(set(cp_rows) - set(cp_details))
        if missing_detail:
            cp_order_errors.append("rows checkpoint non parseables: " + ",".join(f"CP-{n:03d}" for n in missing_detail))
    prev_rank = -1
    prev_seq = None
    for seq in sorted(cp_details):
        row = cp_details[seq]
        rank = _checkpoint_phase_rank(row["label"])
        if rank is None:
            cp_order_errors.append(f"CP-{seq:03d}: label inconnu '{row['label']}'")
            continue
        if rank < prev_rank:
            cp_order_errors.append(
                f"CP-{seq:03d}: phase {rank} après CP-{prev_seq:03d} phase {prev_rank} (ordre rétroactif)"
            )
        # For canonical labels, LAST_COMPLETED must start with owning phase number.
        lm = re.match(r"\s*(\d+)", row["last_completed"])
        if lm and int(lm[1]) != rank and rank != 18:
            cp_order_errors.append(
                f"CP-{seq:03d}: {row['label']} LAST_COMPLETED={row['last_completed']} != phase {rank}"
            )
        prev_rank = max(prev_rank, rank)
        prev_seq = seq
    if cp_order_errors:
        results.append(("kernel:checkpoint_order", "FAIL", "; ".join(cp_order_errors)))
    else:
        results.append(("kernel:checkpoint_order", "PASS", "ordre canonique des checkpoints respecté"))

    # QUERY_TRACE_OK.
    logged_q, q_errors = _kernel_logged_queries(text)
    qry_errors = list(sorted(q_errors))
    if all_qry_refs:
        max_q = max(all_qry_refs)
        expected = set(range(1, max_q + 1))
        missing = sorted(expected - set(logged_q))
        extra = sorted(set(logged_q) - expected)
        if missing:
            qry_errors.append("QRY sans row exécutée: " + ",".join(f"QRY-{x:03d}" for x in missing[:30]))
        if extra:
            qry_errors.append("QRY loggées hors séquence: " + ",".join(f"QRY-{x:03d}" for x in extra[:30]))
    elif logged_q:
        qry_errors.append("REQUEST_LOG contient des QRY mais aucune référence d'enquête")
    if qry_errors:
        results.append(("kernel:query_trace", "FAIL", "; ".join(qry_errors)))
    else:
        results.append(("kernel:query_trace", "PASS", f"{len(logged_q)} QRY contiguës et tracées"))

    # SYS != QRY: research namespace cannot be used for lifecycle/internal calls.
    qns_errors = []
    query_details_for_ns = _kernel_logged_query_details(text)
    internal_tokens = ("SYS", "MNEMO", "READ_MEMORY", "CHECKPOINT", "WRITE", "HASH", "GATE", "MODULE")
    for q, row in sorted(query_details_for_ns.items()):
        mode = (row.get("mode") or "").upper()
        if any(tok in mode for tok in internal_tokens):
            qns_errors.append(f"QRY-{q:03d}: mode interne '{row.get('mode','')}' interdit dans namespace QRY")
    if qns_errors:
        results.append(("kernel:query_namespace", "FAIL", "; ".join(qns_errors)))
    else:
        results.append(("kernel:query_namespace", "PASS", "QRY réservé aux opérations de recherche/récupération"))

    # SYS_TRACE_OK: minimum lifecycle/memory audit must be machine-observable.
    sys_rows = _kernel_logged_sys_details(text)
    sys_calls = [r.get("call","") for r in sys_rows]
    sys_errors = []
    ids=[]
    for r in sys_rows:
        try: ids.append(int(r.get("id","").split("-")[1]))
        except Exception: sys_errors.append("SYS id invalide")
    if ids and ids != list(range(1,len(ids)+1)):
        sys_errors.append("SYS IDs non contigus")
    if sys_calls.count("MNEMO_Q") != 1:
        sys_errors.append("exactement un SYS MNEMO_Q requis")
    if not any(c in {"MEMORY_PROBE","HYDRATE"} for c in sys_calls):
        sys_errors.append("route mémoire SYS absente")
    persist_sys = [r for r in sys_rows if r.get("call") == "PERSIST_REBIND"]
    if phase == "delivery" and not persist_sys:
        sys_errors.append("SYS PERSIST_REBIND absent en delivery")
    elif phase == "delivery" and persist_sys[-1].get("result") != "PASS":
        sys_errors.append("dernier SYS PERSIST_REBIND non-PASS")
    if phase == "pre" and persist_sys:
        sys_errors.append("SYS PERSIST_REBIND interdit avant PRE gate")
    if sys_errors:
        results.append(("kernel:sys_trace", "FAIL", "; ".join(sys_errors)))
    else:
        results.append(("kernel:sys_trace", "PASS", f"{len(sys_rows)} SYS tracées; MNEMO_Q + route mémoire" + (" + persistence" if phase=="delivery" else "")))

    # SEMANTIC_IR_OK: semantic registries must be rendered from RUN_STATE and counts must reconcile.
    sem_declared, sem_observed, sem_errors = _kernel_semantic_registry(text)
    mission_m = re.search(r"\bMISSION_MODE\s*[:=]\s*([A-Z_]+)", text)
    mission = mission_m[1] if mission_m else ""
    if (input_kind == "DOCUMENT" or cx in ("COMPLEX","APEX")) and sem_observed.get("LED",0) == 0:
        sem_errors.append("LED runtime registry vide pour DOCUMENT/COMPLEX/APEX")
    if mission == "INVESTIGATION":
        if sem_observed.get("AXS",0) == 0: sem_errors.append("AXS runtime registry vide en INVESTIGATION")
        if sem_observed.get("CLM",0) == 0: sem_errors.append("CLM runtime registry vide en INVESTIGATION")
    if any(label == "CAUSAL" or label.startswith("CAUSAL_") for label in cp_labels) and sem_observed.get("CAU",0) == 0:
        sem_errors.append("CAU runtime registry vide malgré checkpoint causal")
    if sem_errors:
        results.append(("kernel:semantic_ir", "FAIL", "; ".join(sem_errors)))
    else:
        results.append(("kernel:semantic_ir", "PASS", "SEMANTIC_COUNTS_V1 et registres runtime cohérents"))

    trace_errors=_kernel_trace_projection(text)
    if trace_errors:
        results.append(("kernel:trace_completeness","FAIL","; ".join(trace_errors)))
    else:
        results.append(("kernel:trace_completeness","PASS","TRACE_MATRIX_V1 couvre LED/AXS/CLM"))

    # QUERY_ACCOUNTING_OK: QUERY_TARGET is planning-only; activity is derived from REQUEST_LOG modes.
    qa_errors = []
    legacy_qa = re.findall(r"(?i)query\s+target/actual\s*:\s*(\d+)\s*/\s*(\d+)", text)
    if legacy_qa:
        qa_errors.append("query target/actual interdit en 2.10.6; utiliser SEARCH_ACTIVITY_V1 si un compteur est affiché")

    query_details_for_activity = _kernel_logged_query_details(text)
    derived_activity = {"WEB": 0, "FETCH": 0, "EXA": 0}
    for row in query_details_for_activity.values():
        mode = (row.get("mode") or "").upper()
        if "FETCH" in mode:
            derived_activity["FETCH"] += 1
        elif mode.startswith("EXA"):
            derived_activity["EXA"] += 1
        elif mode.startswith("WEB"):
            derived_activity["WEB"] += 1

    activity_rows = re.findall(
        r"(?i)SEARCH_ACTIVITY_V1\s*:\s*WEB:(\d+)\s*\|\s*FETCH:(\d+)\s*\|\s*EXA:(\d+)",
        text,
    )
    normalized_activity = {(int(w), int(f), int(e)) for w, f, e in activity_rows}
    if len(normalized_activity) > 1:
        qa_errors.append("SEARCH_ACTIVITY_V1 contradictoire entre sections")
    for web_s, fetch_s, exa_s in activity_rows:
        declared = {"WEB": int(web_s), "FETCH": int(fetch_s), "EXA": int(exa_s)}
        if declared != derived_activity:
            qa_errors.append(f"SEARCH_ACTIVITY_V1 {declared} != REQUEST_LOG {derived_activity}")

    if qa_errors:
        results.append(("kernel:query_accounting", "FAIL", "; ".join(qa_errors)))
    else:
        suffix = "compteur absent" if not activity_rows else "SEARCH_ACTIVITY_V1 cohérent"
        results.append((
            "kernel:query_accounting", "PASS",
            f"QRY={len(logged_q)}; WEB={derived_activity['WEB']} FETCH={derived_activity['FETCH']} EXA={derived_activity['EXA']} ({suffix})"
        ))

    # FACT_REGISTRY_OK.
    facts, fact_dups = _kernel_fact_rows(text)
    fact_errors = []
    if fact_dups:
        fact_errors.append("FCT dupliqués: " + ",".join(f"FCT-{x:03d}" for x in sorted(fact_dups)))
    all_fct_refs = _ints(r"\bFCT-(\d+)\b", text)
    if all_fct_refs:
        max_f = max(all_fct_refs)
        missing = sorted(set(range(1, max_f + 1)) - set(facts))
        if missing:
            fact_errors.append("FCT référencés/attendus absents du registre: " + ",".join(f"FCT-{x:03d}" for x in missing[:30]))
    valid_epi = {"FACT", "EVIDENCE", "INFERENCE", "HYPOTHESIS", "SPECULATION", "UNKNOWN"}
    valid_tier = {"✦", "✧", "⁅", "❧"}
    star_ids = []
    for n, parts in sorted(facts.items()):
        if len(parts) != 9:
            fact_errors.append(f"FCT-{n:03d}: {len(parts)} champs, attendu 9")
            continue
        _fid, epi, tier, url, families, _date, _subject, _value, _mem = parts
        if epi not in valid_epi:
            fact_errors.append(f"FCT-{n:03d}: EPI invalide {epi}")
        if tier not in valid_tier:
            fact_errors.append(f"FCT-{n:03d}: tier invalide {tier}")
        if "..." in url or "…" in url or "<" in url or ">" in url or not url:
            fact_errors.append(f"FCT-{n:03d}: URL/path tronqué ou placeholder")
        if tier == "✦":
            star_ids.append(n)
            if epi != "FACT":
                fact_errors.append(f"FCT-{n:03d}: ✦ exige EPI=FACT")
            if _family_count(families) < 2:
                fact_errors.append(f"FCT-{n:03d}: ✦ avec moins de 2 familles indépendantes")

    refutes, refute_dups = _kernel_refutation_rows(text)
    refutation_queries = _kernel_logged_query_details(text)
    if refute_dups:
        fact_errors.append("refutations dupliquées: " + ",".join(f"FCT-{x:03d}" for x in sorted(refute_dups)))
    for n in star_ids:
        if n not in refutes:
            fact_errors.append(f"FCT-{n:03d}: REFUTATION_REGISTRY_V1 absent")
        else:
            q, _status = refutes[n]
            if q not in logged_q:
                fact_errors.append(f"FCT-{n:03d}: refutation QRY-{q:03d} non tracée")
            else:
                subject = facts[n][6] if len(facts[n]) > 6 else ""
                alignment = _refutation_alignment_error(subject, refutation_queries.get(q, {}))
                if alignment:
                    fact_errors.append(f"FCT-{n:03d}: QRY-{q:03d} sémantiquement mal alignée ({alignment})")
    if fact_errors:
        results.append(("kernel:fact_registry", "FAIL", "; ".join(fact_errors)))
    else:
        results.append(("kernel:fact_registry", "PASS", f"{len(facts)} FCT cohérents, {len(star_ids)} ✦ refutés/testés"))

    # INSPECTED_TRACE_OK: every web-backed ✦/✧ must have exact-URL FETCH evidence.
    inspect_errors = []
    query_details = _kernel_logged_query_details(text)
    fetched_urls = {
        _norm_url(row.get("url"))
        for row in query_details.values()
        if "FETCH" in row.get("mode", "").upper() and _norm_url(row.get("url")).lower().startswith(("http://", "https://"))
    }
    inspected_ids = []
    for n, parts in sorted(facts.items()):
        if len(parts) != 9:
            continue
        tier, url = parts[2], _norm_url(parts[3])
        if tier not in {"✦", "✧"}:
            continue
        if not url.lower().startswith(("http://", "https://")):
            continue
        inspected_ids.append(n)
        if url not in fetched_urls:
            inspect_errors.append(f"FCT-{n:03d}: aucun FETCH exact pour {url}")
    if inspect_errors:
        results.append(("kernel:inspected_trace", "FAIL", "; ".join(inspect_errors)))
    else:
        results.append(("kernel:inspected_trace", "PASS", f"{len(inspected_ids)} FCT web ✦/✧ avec FETCH exact"))

    # PROVENANCE_ACCOUNTING_OK: FCT family claims must be derived from mapped SRC rows.
    source_rows, source_dups, source_parse_errors = _kernel_source_rows(text)
    source_map, source_map_dups, source_map_errors = _kernel_fct_source_map(text)
    prov_errors = list(source_parse_errors) + list(source_map_errors)
    if source_dups:
        prov_errors.append("SRC dupliqués: " + ",".join(f"SRC-{x:03d}" for x in sorted(source_dups)))
    if source_map_dups:
        prov_errors.append("FCT_SOURCE_MAP dupliqué: " + ",".join(f"FCT-{x:03d}" for x in sorted(source_map_dups)))
    if set(source_map) != set(facts):
        miss = sorted(set(facts) - set(source_map))
        extra = sorted(set(source_map) - set(facts))
        if miss:
            prov_errors.append("mapping provenance absent: " + ",".join(f"FCT-{x:03d}" for x in miss))
        if extra:
            prov_errors.append("mapping provenance sans FCT: " + ",".join(f"FCT-{x:03d}" for x in extra))

    fetched_source_ids = set()
    for qrow in query_details.values():
        if "FETCH" not in qrow.get("mode", "").upper():
            continue
        for sm in re.finditer(r"SRC-(\d+)", qrow.get("source", "")):
            fetched_source_ids.add(int(sm.group(1)))

    for n, parts in sorted(facts.items()):
        if len(parts) != 9:
            continue
        tier = parts[2]
        fact_url = _norm_url(parts[3])
        declared = _family_tokens(parts[4])
        mapped = source_map.get(n, [])
        derived = set()
        mapped_urls = set()
        for sid in mapped:
            srow = source_rows.get(sid)
            if not srow:
                prov_errors.append(f"FCT-{n:03d}: SRC-{sid:03d} absent du registre source")
                continue
            if srow["family"]:
                derived.add(srow["family"])
            if srow["url"]:
                mapped_urls.add(srow["url"])
            if tier in {"✦", "✧"} and srow["url"].lower().startswith(("http://", "https://")) and sid not in fetched_source_ids:
                prov_errors.append(f"FCT-{n:03d}: SRC-{sid:03d} mappé mais aucun FETCH tracé")
        if declared != derived:
            prov_errors.append(
                f"FCT-{n:03d}: families déclarées {sorted(declared)} != dérivées {sorted(derived)}"
            )
        if tier in {"✦", "✧"}:
            if not mapped:
                prov_errors.append(f"FCT-{n:03d}: aucun SRC support mappé pour tier {tier}")
            if fact_url.lower().startswith(("http://", "https://")) and fact_url not in mapped_urls:
                prov_errors.append(f"FCT-{n:03d}: URL canonique absente des SRC support mappés")
        if tier == "✦" and len(derived) < 2:
            prov_errors.append(f"FCT-{n:03d}: ✦ avec {len(derived)} famille(s) dérivée(s)")

    corpus_families = {row["family"] for row in source_rows.values() if row["family"]}
    # Reject exact displayed family totals that disagree with the registry.
    for declared_count in [int(x) for x in re.findall(r"(?i)\bIND\s*=\s*(\d+)\s+familles?", text)]:
        if declared_count != len(corpus_families):
            prov_errors.append(f"IND familles={declared_count} != registre={len(corpus_families)}")
    for declared_count in [int(x) for x in re.findall(r"(?i)\bFAMILLES\s*:\s*(\d+)\b", text)]:
        if declared_count != len(corpus_families):
            prov_errors.append(f"FAMILLES déclarées={declared_count} != registre={len(corpus_families)}")
    # A range such as "4-5" is not deterministic and is therefore forbidden.
    if re.search(r"(?i)\bupstream\s+families\s*:\s*\d+\s*-\s*\d+", text):
        prov_errors.append("upstream families exprimé en fourchette au lieu d'un compte dérivé")
    for declared_count in [int(x) for x in re.findall(r"(?i)\bupstream\s+families\s*:\s*(\d+)\b(?!\s*-)", text)]:
        if declared_count != len(corpus_families):
            prov_errors.append(f"upstream families={declared_count} != registre={len(corpus_families)}")

    if prov_errors:
        results.append(("kernel:provenance_accounting", "FAIL", "; ".join(prov_errors)))
    else:
        results.append(
            ("kernel:provenance_accounting", "PASS",
             f"{len(source_rows)} SRC, {len(corpus_families)} familles, {len(source_map)} mappings FCT→SRC cohérents")
        )

    # WRITEBACK_PLAN_OK.
    plan, plan_dups = _kernel_writeback_plan(text)
    plan_errors = []
    if plan_dups:
        plan_errors.append("plans dupliqués: " + ",".join(f"FCT-{x:03d}" for x in sorted(plan_dups)))
    if set(plan) != set(facts):
        miss = sorted(set(facts) - set(plan))
        extra = sorted(set(plan) - set(facts))
        if miss:
            plan_errors.append("plan absent: " + ",".join(f"FCT-{x:03d}" for x in miss))
        if extra:
            plan_errors.append("plan sans FCT: " + ",".join(f"FCT-{x:03d}" for x in extra))
    expected_plan = {}
    for n, parts in facts.items():
        if len(parts) != 9:
            continue
        epi, tier = parts[1], parts[2]
        if epi == "FACT" and tier == "✦":
            expected_plan[n] = "ELIGIBLE:CONFIRME"
        elif epi == "FACT" and tier == "✧":
            expected_plan[n] = "ELIGIBLE:VERIFIE"
        else:
            expected_plan[n] = "SKIP"
    for n, expected_action in expected_plan.items():
        actual = plan.get(n, "")
        if expected_action == "SKIP":
            if actual and not actual.startswith("SKIP:"):
                plan_errors.append(f"FCT-{n:03d}: attendu SKIP, obtenu {actual}")
        elif actual != expected_action:
            plan_errors.append(f"FCT-{n:03d}: attendu {expected_action}, obtenu {actual or 'ABSENT'}")
    if plan_errors:
        results.append(("kernel:writeback_plan", "FAIL", "; ".join(plan_errors)))
    else:
        eligible_count = sum(1 for x in expected_plan.values() if x.startswith("ELIGIBLE:"))
        results.append(("kernel:writeback_plan", "PASS", f"{len(plan)} rows, {eligible_count} éligibles"))

    # MEMORY_WRITE_MODE_OK: deterministic idempotence hint from hydrated lineage.
    mw_rows,mw_dups,mw_errors=_kernel_memory_write_modes(text)
    eligible_ids={n for n,a in expected_plan.items() if a.startswith("ELIGIBLE:")}
    if mw_dups: mw_errors.append("modes dupliqués: "+",".join(f"FCT-{n:03d}" for n in sorted(set(mw_dups))))
    if set(mw_rows) != eligible_ids:
        miss=sorted(eligible_ids-set(mw_rows)); extra=sorted(set(mw_rows)-eligible_ids)
        if miss: mw_errors.append("mode mémoire absent: "+",".join(f"FCT-{n:03d}" for n in miss))
        if extra: mw_errors.append("mode mémoire sans fait éligible: "+",".join(f"FCT-{n:03d}" for n in extra))
    if mw_errors:
        results.append(("kernel:memory_write_mode", "FAIL", "; ".join(mw_errors)))
    else:
        upd=sum(1 for mode,_ in mw_rows.values() if mode=="UPDATE")
        results.append(("kernel:memory_write_mode", "PASS", f"{len(mw_rows)} rows; UPDATE={upd}, WRITE={len(mw_rows)-upd}"))

    # PERSISTENCE_META_OK: exact serialization boundary pre vs delivery.
    persistence_errors = []
    self_values = [x.strip() for x in re.findall(r"(?i)\bSELF_WRITE_ROW\s*[:=]\s*([^|\n]+)", text)]
    if not self_values:
        persistence_errors.append("SELF_WRITE_ROW absent")
    elif any(v != "PENDING_AT_SERIALIZATION" for v in self_values):
        persistence_errors.append("SELF_WRITE_ROW doit rester PENDING_AT_SERIALIZATION")

    mnemo_values = [x.strip() for x in re.findall(r"(?i)\bMNEMO_ROW\s*[:=]\s*([^|\n]+)", text)]
    writeback_pending = bool(re.search(r"\bWRITEBACK_ROW\s*[:=]\s*PENDING_PRE_GATE\b", text))
    exec_heading = bool(re.search(r"(?mi)^#{1,6}\s+WRITEBACK_EXECUTION_V1\s*$", text))
    exec_rows_now, _exec_dups_now = _kernel_writeback_exec_rows(text)
    attempts, attempt_errors = _kernel_writeback_attempts(text)
    persistence_errors.extend(attempt_errors)
    if phase == "pre":
        if not mnemo_values or any(v != "PENDING_PRE_GATE" for v in mnemo_values):
            persistence_errors.append("PRE: MNEMO_ROW doit être PENDING_PRE_GATE")
        if not writeback_pending:
            persistence_errors.append("PRE: WRITEBACK_ROW=PENDING_PRE_GATE absent")
        if not re.search(r"\bWRITEBACK_EXECUTION_V1\s*[:=]\s*\[\s*\]", text):
            persistence_errors.append("PRE: WRITEBACK_EXECUTION_V1=[] absent")
        if exec_rows_now:
            persistence_errors.append("PRE: WRITEBACK_EXECUTION_V1 doit être vide")
        if attempts:
            persistence_errors.append("PRE: historique de persistance doit être vide")
    else:
        if not mnemo_values:
            persistence_errors.append("DELIVERY: MNEMO_ROW absent")
        elif any(v == "PENDING_PRE_GATE" for v in mnemo_values):
            persistence_errors.append("DELIVERY: MNEMO_ROW encore PENDING_PRE_GATE")
        if writeback_pending:
            persistence_errors.append("DELIVERY: WRITEBACK_ROW encore PENDING_PRE_GATE")
        if not exec_heading:
            persistence_errors.append("DELIVERY: section WRITEBACK_EXECUTION_V1 absente")
        if not attempts:
            persistence_errors.append("DELIVERY: historique des tentatives de persistance absent")
        elif attempts[-1].get("result") != "PASS":
            persistence_errors.append("DELIVERY: dernière tentative de persistance non-PASS")
        if len(attempts) != len(persist_sys):
            persistence_errors.append(
                f"DELIVERY: {len(attempts)} tentative(s) mais {len(persist_sys)} SYS PERSIST_REBIND"
            )
    if persistence_errors:
        results.append(("kernel:persistence_meta", "FAIL", "; ".join(persistence_errors)))
    else:
        results.append(("kernel:persistence_meta", "PASS", f"frontière persistence {phase} cohérente"))

    # ACCOUNTING_OK: source-role/provenance counts derive from canonical source rows.
    role_counts = {"◈": 0, "◉": 0, "○": 0}
    seen_src = set(source_rows)
    for row in source_rows.values():
        if row["role"] in role_counts:
            role_counts[row["role"]] += 1
    acct_errors = []
    sm = re.search(r"\[SOURCES\]\s*◈\s*:\s*(\d+)\s*◉\s*:\s*(\d+)\s*○\s*:\s*(\d+)", text)
    if sm:
        declared = {"◈": int(sm[1]), "◉": int(sm[2]), "○": int(sm[3])}
        if seen_src and declared != role_counts:
            acct_errors.append(f"source roles déclarés {declared} != registre {role_counts}")

    eligible = [n for n, action in expected_plan.items() if action.startswith("ELIGIBLE:")]
    if phase == "pre":
        for n, parts in facts.items():
            mem = _fact_mem(parts)
            if mem not in ("-", "", None):
                acct_errors.append(f"PRE: FCT-{n:03d} mem déjà rebindé")
        if not re.search(r"\bWRITEBACK_ROW\s*[:=]\s*PENDING_PRE_GATE\b", text):
            acct_errors.append("PRE: WRITEBACK_ROW=PENDING_PRE_GATE absent")
    else:
        exec_rows, exec_dups = _kernel_writeback_exec_rows(text)
        if exec_dups:
            acct_errors.append("writeback execution rows dupliquées: " + ",".join(f"FCT-{x:03d}" for x in sorted(exec_dups)))
        allowed_block_reasons = {"UNSTABLE_EVIDENCE_KEY", "MNEMO_UNAVAILABLE", "TOOL_SCHEMA_UNAVAILABLE"}
        derived_attempted = derived_success = derived_failure = derived_blocked = 0
        for n in eligible:
            row = exec_rows.get(n)
            if not row:
                acct_errors.append(f"FCT-{n:03d}: execution writeback absente")
                continue
            expected_action = expected_plan[n]
            if row["action"] != expected_action:
                acct_errors.append(f"FCT-{n:03d}: action exécutée {row['action']} != {expected_action}")
            attempted, success, failure, blocked = row["attempted"], row["success"], row["failure"], row["blocked"]
            if attempted not in (0, 1) or success not in (0, 1) or failure not in (0, 1) or blocked not in (0, 1):
                acct_errors.append(f"FCT-{n:03d}: compteurs writeback non binaires")
            if attempted + blocked != 1:
                acct_errors.append(f"FCT-{n:03d}: eligible exige attempted=1 XOR blocked=1")
            if attempted != success + failure:
                acct_errors.append(f"FCT-{n:03d}: attempted != success + failure")
            if blocked:
                reason = row["reason"].upper().replace("-", "_").replace(" ", "_")
                if reason not in allowed_block_reasons:
                    acct_errors.append(f"FCT-{n:03d}: block reason illégal '{row['reason'] or 'ABSENT'}'")
            derived_attempted += attempted
            derived_success += success
            derived_failure += failure
            derived_blocked += blocked

        wm = re.search(
            r"\bWRITEBACK_ROW\s*[:=]\s*\{\s*eligible:(\d+)\s*;\s*attempted:(\d+)\s*;\s*success:(\d+)\s*;\s*failure:(\d+)\s*;\s*blocked:(\d+)\s*\}",
            text,
        )
        if not wm:
            acct_errors.append("DELIVERY: WRITEBACK_ROW structuré absent")
        else:
            e, a, ok, fail, blocked = map(int, wm.groups())
            if e != len(eligible):
                acct_errors.append(f"eligible={e} != plan {len(eligible)}")
            if (a, ok, fail, blocked) != (derived_attempted, derived_success, derived_failure, derived_blocked):
                acct_errors.append(
                    f"WRITEBACK_ROW {(a, ok, fail, blocked)} != execution rows "
                    f"{(derived_attempted, derived_success, derived_failure, derived_blocked)}"
                )
            if e != a + blocked:
                acct_errors.append("eligible != attempted + blocked")
            if a != ok + fail:
                acct_errors.append("attempted != success + failure")
            mem_success = sum(1 for n in eligible if _fact_mem(facts[n]) not in ("-", "", None))
            if ok != mem_success:
                acct_errors.append(f"success={ok} != FCT mem rebindés={mem_success}")
            for n in facts:
                if n not in eligible and _fact_mem(facts[n]) not in ("-", "", None):
                    acct_errors.append(f"FCT-{n:03d}: mem rebindé malgré SKIP")
    if acct_errors:
        results.append(("kernel:accounting", "FAIL", "; ".join(acct_errors)))
    else:
        results.append(("kernel:accounting", "PASS", f"phase={phase}, compteurs dérivés cohérents"))

    verdict = _merge_result_rows(results)
    return verdict, results


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
    if review not in VERDICTS and review != "N/A":
        eprint(f"--review doit être l'un de {VERDICTS} ou N/A")
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
    deliverable_changed = False
    pending_deliverable = pending.get("deliverable")
    pending_deliverable_sha256 = pending.get("deliverable_sha256")
    if pending_deliverable and pending_deliverable_sha256:
        candidate_path = pending_deliverable if os.path.isabs(pending_deliverable) else os.path.join(root, pending_deliverable)
        current_hash, _hash_err = _file_sha256(candidate_path)
        deliverable_changed = current_hash != pending_deliverable_sha256

    deterministic = pending.get("deterministic", "PASS")
    if state_changed or deliverable_changed:
        final = "FAIL"
    elif deterministic != "PASS":
        final = deterministic
    elif review == "N/A":
        final = deterministic  # pas de revue LLM : le déterministe fait foi
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
        "deliverable_changed": deliverable_changed,
        "kernel_contract": pending.get("kernel_contract"),
        "deliverable": pending.get("deliverable"),
        "deliverable_sha256": pending.get("deliverable_sha256"),
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


def check_deliverable_timestamp(deliverable):
    """Contrôle déterministe : l'horodatage du nom de fichier n'est pas dans le futur.

    La cohérence temporelle (date/heure réelle, jamais inventée) est une
    vérification mécanique, pas un jugement sémantique : le reviewer LLM n'a ni
    horloge ni outils et rejette à tort les dates réelles. Retourne
    (verdict, detail) avec verdict PASS/FAIL/BLOCKED.
    """
    import re

    name = os.path.basename(deliverable)
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})_(\d{2})-(\d{2})_", name)
    if not m:
        # Pas d'horodatage dans le nom : le format est du ressort du check
        # naming (déterministe). Ce contrôle ne vérifie que le non-futur.
        return "PASS", f"horodatage non applicable (pas d'horodatage parsable : {name})"
    try:
        ts = datetime(int(m[1]), int(m[2]), int(m[3]), int(m[4]), int(m[5]))
    except ValueError as exc:
        return "BLOCKED", f"horodatage invalide : {name} ({exc})"
    now = datetime.now()
    if ts > now:
        return "FAIL", f"horodatage dans le futur : {name} ({ts:%Y-%m-%d %H:%M}) > {now:%Y-%m-%d %H:%M}"
    return "PASS", f"horodatage non futur : {name}"


def cmd_gate(cfg, root, deliverable=None, kernel_contract=None):
    """check + certify en une commande, sans revue LLM (gate déterministe seule).

    Le reviewer local Ollama a été supprimé (2026-08-18) : un LLM sans outils
    ne peut pas fact-checker. La conformité mécanique relève du déterministe
    seul. La revue sémantique premium reste le sous-agent Freebuff
    truth-reviewer (chemin spawn, .agents/truth-verifier.ts).
    """
    path = None
    if deliverable:
        path = deliverable if os.path.isabs(deliverable) else os.path.join(root, deliverable)

    # 0. A KERNEL artifact cannot be certified by a generic gate.
    generic_kernel_block = False
    if path and not kernel_contract and _looks_like_kernel_artifact(path):
        generic_kernel_block = True

    # 1. check déterministe (mêmes contrôles et STATE_ID que `check`)
    verdict, results = run_checks(cfg, root)
    if generic_kernel_block:
        results.append(_record(
            "gate:kernel_contract",
            "BLOCKED",
            "artefact KERNEL détecté : --kernel-contract pre|delivery obligatoire",
        ))
        verdict = _merge_verdict(verdict, "BLOCKED")

    # 2. contrat KERNEL explicitement supporté, uniquement si demandé.
    if kernel_contract:
        if not path:
            kc_verdict, kc_rows = "BLOCKED", [("kernel:file", "BLOCKED", "--kernel-contract exige --file")]
        else:
            kc_verdict, kc_rows = check_kernel_contract(path, kernel_contract)
        for name, v, detail in kc_rows:
            results.append(_record(name, v, detail))
        verdict = _merge_verdict(verdict, kc_verdict)

    # 3. horodatage déterministe du livrable (mécanique : l'horodatage du nom
    #    de fichier ne doit pas être dans le futur).
    if verdict == "PASS" and path:
        ts_verdict, ts_detail = check_deliverable_timestamp(path)
        if ts_verdict != "PASS":
            verdict = ts_verdict
            results.append(_record("gate:horodatage", ts_verdict, ts_detail))

    # 4. pending + STATE_ID + exact deliverable identity.
    state_id, head = compute_state_id(root)
    deliverable_sha256 = None
    deliverable_ref = None
    if path:
        deliverable_sha256, hash_err = _file_sha256(path)
        if hash_err:
            results.append(_record("gate:deliverable_hash", "BLOCKED", hash_err))
            verdict = _merge_verdict(verdict, "BLOCKED")
        try:
            deliverable_ref = os.path.relpath(path, root) if os.path.commonpath([os.path.abspath(path), os.path.abspath(root)]) == os.path.abspath(root) else os.path.abspath(path)
        except ValueError:
            deliverable_ref = os.path.abspath(path)
    pending = {
        "schema": 1,
        "task": cfg.get("task", "default"),
        "deterministic": verdict,
        "head": head,
        "state_id": state_id,
        "kernel_contract": kernel_contract,
        "deliverable": deliverable_ref,
        "deliverable_sha256": deliverable_sha256,
        "created_at": now_iso(),
    }
    os.makedirs(os.path.dirname(os.path.join(root, PENDING_PATH)) or ".", exist_ok=True)
    with open(os.path.join(root, PENDING_PATH), "w", encoding="utf-8") as f:
        json.dump(pending, f, indent=2, ensure_ascii=False)

    report = dict(pending)
    report["checks"] = results
    print(json.dumps(report, indent=2, ensure_ascii=False), file=sys.stderr)

    # 5. certify : verdict = déterministe seul (review=N/A, pas de revue LLM).
    note = None
    if not path:
        note = "pas de --file : contrôle d'horodatage et contrat KERNEL non exécutés"
    return cmd_certify(cfg, root, "N/A", None, review_note=note)


def usage():
    print(
        "usage: verify.py check | state-id | report | certify --review PASS|FAIL|BLOCKED|N/A [--findings-file <fichier.json>] | gate [--file <livrable>] [--kernel-contract pre|delivery]"
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
        kernel_contract = None
        if "--kernel-contract" in argv:
            i = argv.index("--kernel-contract")
            if i + 1 < len(argv):
                kernel_contract = argv[i + 1].lower()
        return cmd_gate(cfg, root, deliverable, kernel_contract)
    return usage()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
