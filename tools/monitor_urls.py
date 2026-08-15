#!/usr/bin/env python3
"""monitor_urls.py — Moniteur d'URLs mortes du registre des faits (P4).

Scanne les dossiers d'investigation à la recherche des blocs `<!-- FACT_REGISTRY_V1 -->`,
HEAD-checke chaque URL (anti-SSRF, via `tools/verify_facts.classify_url`) et signale les
sources défuntes, invalides ou injoignables.

Une source `dead` déclenche la re-vérification du fait (FACT_VERIFICATION.md §6/§10) :
re-fetch (nouvelle URL ou confirmation) → `update_memory` (nouvelle verifie-date) ou
rétrogradation `lifecycle_state=doubt` si plus aucune source. Cette re-vérification est
un acte HUMAIN/LLM guidé par ce rapport : le script détecte, il ne juge pas le contenu.

Sortie : rapport texte (ou --json) + code retour :
  0 = toutes les URLs vivantes
  1 = au moins une anomalie (dead / unsafe / unreachable)
  2 = aucun registre trouvé

Usage :
  python3 tools/monitor_urls.py [chemin...] [--timeout N] [--offline] [--json]
  Sans chemin : scanne `investigations/` récursivement.
"""

import argparse
import json
import os
import sys

# Exécution directe (python3 tools/monitor_urls.py) : rendre `tools` importable.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.verify_facts import (
    classify_url,
    extract_registry,
    parse_line,
)

REGISTRY_START = "<!-- FACT_REGISTRY_V1 -->"

# status → action (cf. FACT_VERIFICATION.md §6/§10). head_blocked n'est pas une
# anomalie : le HEAD est refusé, la liveness reste inconnue (GET requis).
ACTION = {
    "dead": "re-vérifier : re-fetch (nouvelle URL ou confirmation) → update_memory "
            "(nouvelle verifie-date) ou rétrogradation lifecycle_state=doubt",
    "unsafe": "corriger l'URL (scheme/IP interdit par anti-SSRF)",
    "unreachable": "domaine non résolu ou réseau/timeout : retry ; re-vérifier si persistant",
    "head_blocked": "HEAD non autorisé : liveness inconnue via HEAD — confirmer par GET",
}

PROBLEM_STATUS = {"dead", "unsafe", "unreachable"}


def find_registry_files(paths):
    """Chemins .md contenant un bloc FACT_REGISTRY_V1 (fichiers ou arborescences)."""
    files = []
    for p in paths:
        if os.path.isfile(p):
            if p.endswith(".md"):
                files.append(p)
        elif os.path.isdir(p):
            for root, _dirs, names in os.walk(p):
                for name in sorted(names):
                    if name.endswith(".md"):
                        files.append(os.path.join(root, name))
    out = []
    for f in sorted(set(files)):
        try:
            with open(f, "r", encoding="utf-8") as fh:
                if REGISTRY_START in fh.read():
                    out.append(f)
        except OSError:
            continue
    return out


def scan_file(path, timeout, offline=False):
    """Liste des entrées (path, fid, url, status, detail) pour un fichier registre."""
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    entries = []
    for ln in extract_registry(text):
        rec = parse_line(ln)
        if rec is None:
            continue
        fid, _epi, _tier, url, _families, _date = rec
        if not url or url == "-":
            continue  # ❧ : pas d'URL, rien à monitorer
        if offline:
            entries.append((path, fid, url, "skipped", "offline"))
            continue
        status, detail = classify_url(url, timeout)
        entries.append((path, fid, url, status, detail))
    return entries


def run(paths, timeout, offline=False):
    """Retourne (files, entries). entries = liste complète des URL checkées."""
    files = find_registry_files(paths)
    entries = []
    for f in files:
        entries.extend(scan_file(f, timeout, offline=offline))
    return files, entries


def _problems(entries):
    return [e for e in entries if e[3] in PROBLEM_STATUS]


def _head_blocked(entries):
    return [e for e in entries if e[3] == "head_blocked"]


def report_text(files, entries):
    problems = _problems(entries)
    blocked = _head_blocked(entries)
    checked = [e for e in entries if e[3] != "skipped"]
    print("MONITEUR URLs — registre des faits (P4)")
    print("=" * 60)
    if not entries:
        print("Aucune URL à checker.")
        return 2 if not files else 0
    for path, fid, url, status, detail in problems + blocked:
        print("[{0}] {1}  {2}  ({3})".format(status, fid, url, detail))
        print("      → {0}".format(ACTION.get(status, "?")))
    n_dead = sum(1 for e in problems if e[3] == "dead")
    print("-" * 60)
    print("{0} problème(s) ({1} dead) + {2} HEAD-bloqué(s), sur {3} URL(s) checkées, {4} fichier(s).".format(
        len(problems), n_dead, len(blocked), len(checked), len(files)))
    return 1 if problems else 0


def report_json(files, entries):
    problems = _problems(entries)
    blocked = _head_blocked(entries)
    payload = {
        "files": files,
        "checked": len([e for e in entries if e[3] != "skipped"]),
        "problems": len(problems),
        "dead": sum(1 for e in problems if e[3] == "dead"),
        "head_blocked": len(blocked),
        "entries": [
            {"file": path, "fact": fid, "url": url,
             "status": status, "detail": detail,
             "action": ACTION.get(status, "")}
            for path, fid, url, status, detail in problems + blocked
        ],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 1 if problems else 0


def main(argv):
    ap = argparse.ArgumentParser(description="Moniteur d'URLs mortes du registre des faits.")
    ap.add_argument("paths", nargs="*", default=["investigations/"],
                    help="Fichiers ou dossiers à scanner (défaut : investigations/)")
    ap.add_argument("--timeout", type=int, default=5)
    ap.add_argument("--offline", action="store_true",
                    help="Saute les HEAD-check réseau (déterminisme sans réseau)")
    ap.add_argument("--json", action="store_true", help="Sortie machine-readable")
    args = ap.parse_args(argv)
    files, entries = run(args.paths, args.timeout, offline=args.offline)
    if args.json:
        return report_json(files, entries)
    return report_text(files, entries)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
