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

Usage :
  python3 tools/verify/verify.py check
  python3 tools/verify/verify.py state-id
  python3 tools/verify/verify.py certify --review PASS|FAIL|BLOCKED
"""

import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

CONFIG_PATH = ".verify/config.json"
PENDING_PATH = ".verify/pending.json"
RESULT_PATH = ".verify/result.json"

VERDICTS = ("PASS", "FAIL", "BLOCKED")

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

    nverdict, nviolations = check_naming(cfg, root)
    if nviolations:
        results.append(_record("naming", nverdict, "; ".join(nviolations)))
        if nverdict == "FAIL":
            verdict = "FAIL"

    return verdict, results


def check_naming(cfg, root):
    """Contrôle de nommage, activé uniquement si configuré."""
    n = cfg.get("naming", {}) or {}
    if not n.get("enabled"):
        return "PASS", []
    pattern = n.get("pattern")
    dirs = n.get("dirs", [])
    if not pattern or not dirs:
        return "BLOCKED", ["naming.enabled=true mais pattern/dirs absents"]
    import re

    try:
        rx = re.compile(pattern)
    except re.error as exc:
        return "BLOCKED", [f"pattern invalide : {exc}"]
    violations = []
    for d in dirs:
        base = os.path.join(root, d)
        if not os.path.isdir(base):
            continue
        for dirpath, _dirs, files in os.walk(base):
            for f in files:
                if not rx.match(f):
                    violations.append(os.path.relpath(os.path.join(dirpath, f), root))
    if violations:
        return "FAIL", violations[:50]
    return "PASS", []


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


def cmd_certify(cfg, root, review):
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
    os.makedirs(os.path.dirname(os.path.join(root, RESULT_PATH)) or ".", exist_ok=True)
    with open(os.path.join(root, RESULT_PATH), "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return {"PASS": 0, "FAIL": 1, "BLOCKED": 2}[final]


def usage():
    print(
        "usage: verify.py check | state-id | certify --review PASS|FAIL|BLOCKED"
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
    if mode == "certify":
        review = "PASS"
        if "--review" in argv:
            i = argv.index("--review")
            if i + 1 < len(argv):
                review = argv[i + 1].upper()
        return cmd_certify(cfg, root, review)
    return usage()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
