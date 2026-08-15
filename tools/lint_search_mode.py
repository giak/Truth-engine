#!/usr/bin/env python3
"""lint_search_mode.py — Garde-fou : tout appel `search_memory(` doit passer `search_mode="hybrid"`.

Le serveur Mnemolite a pour défaut `search_mode="tag"` (lexical, `similarity_score: null`) — constaté
dans le conteneur `mnemo-mcp` : `server.py:1231` et `memory_tools.py:810` (`search_mode: str = "tag"`).
Tout call site qui omet `search_mode="hybrid"` retombe silencieusement en tag-only et perd la recherche
sémantique. Ce lint scanne les fichiers d'instruction (.md) et signale toute ligne contenant
`search_memory(` sans `"hybrid"` ni `'hybrid'`.

Limite assumée : vérification par ligne (les call sites des prompts sont mono-ligne). Un appel
multi-ligne avec `hybrid` sur la ligne suivante déclencherait un faux positif — préférable au
fallback silencieux en tag-only.

Usage :
  python3 tools/lint_search_mode.py [chemins...]
  Sans chemin : scanne les fichiers d'instruction VIVANTS (AGENTS.md, KERNEL, protocol,
  prompts v36-v38 + sub-prompts). Archives, rapports d'audit et sous-module book exclus.
Exit : 0 = tous conformes, 1 = call site(s) non conforme(s), 2 = aucun call site trouvé.
"""

import argparse
import os
import sys

DEFAULT_TARGETS = [
    "AGENTS.md",
    "truth-engine-v2/KERNEL.md",
    "truth-engine-v2/protocol",
    "tools/engines/sublimator/prompt-v36.md",
    "tools/engines/sublimator/prompt-v37_phase2.md",
    "tools/engines/sublimator/prompt-v38_phase3.md",
    "tools/engines/sublimator/prompt-phase2_5_raisonnement_narratif.md",
    "tools/engines/sublimator/prompts",
]


def find_md(paths):
    files = set()
    for p in paths:
        if os.path.isfile(p) and p.endswith(".md"):
            files.add(os.path.normpath(p))
        elif os.path.isdir(p):
            for root, _dirs, names in os.walk(p):
                for name in sorted(names):
                    if name.endswith(".md"):
                        files.add(os.path.normpath(os.path.join(root, name)))
    return sorted(files)


def count_sites(path):
    """Nombre total de lignes contenant `search_memory(`."""
    with open(path, "r", encoding="utf-8") as fh:
        return sum(1 for line in fh if "search_memory(" in line)


def check_file(path):
    """[(ligne, texte)] — call sites `search_memory(` sans hybrid."""
    violations = []
    with open(path, "r", encoding="utf-8") as fh:
        for i, line in enumerate(fh, 1):
            if "search_memory(" in line and '"hybrid"' not in line and "'hybrid'" not in line:
                violations.append((i, line.strip()))
    return violations


def main(argv):
    ap = argparse.ArgumentParser(description="Lint search_mode=hybrid des call sites.")
    ap.add_argument("paths", nargs="*",
                    default=DEFAULT_TARGETS,
                    help="Fichiers/dossiers à scanner (défaut : instructions vivantes)")
    args = ap.parse_args(argv)

    total_sites = 0
    bad = []
    for f in find_md(args.paths):
        total_sites += count_sites(f)
        bad.extend((f, lineno, text) for lineno, text in check_file(f))

    if total_sites == 0:
        print("AUCUN call site `search_memory(` trouvé.")
        return 2

    if not bad:
        print("OK : {0} call site(s) `search_memory(`, tous avec `search_mode=\"hybrid\"`.".format(
            total_sites))
        return 0

    for f, lineno, text in bad:
        print("NON CONFORME [{0}:{1}] {2}".format(f, lineno, text))
    print("{0} call site(s) sans `search_mode=\"hybrid\"`.".format(len(bad)))
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
