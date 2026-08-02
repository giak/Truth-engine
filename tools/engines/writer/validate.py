#!/usr/bin/env python3
"""validate.py — Validation technique réutilisable pour les textes français du projet Truth Engine.

Usage:
    python3 tools/engines/writer/validate.py <fichier.md> [--cible-mots N] [--chiffres CHIFFRES] [--liens LIENS]

Vérifie :
    - 0 em-dash (U+2014)
    - 0 en-dash (U+2013)
    - 0 espace simple avant : ; ! ?
    - Guillemets français équilibrés (« = »)
    - Compte de mots (si --cible-mots fourni)
    - Chiffres clés présents (si --chiffres fourni, séparés par des virgules)
    - Liens/emails présents (si --liens fourni, séparés par des virgules)

Exit code : 0 si tout est OK, 1 si au moins une violation.
"""

import argparse
import re
import sys
import pathlib


def validate(filepath: str, cible_mots: int | None, chiffres: list[str] | None, liens: list[str] | None) -> int:
    p = pathlib.Path(filepath)
    if not p.exists():
        print(f"ERREUR: fichier introuvable: {filepath}")
        return 1

    raw = p.read_text(encoding="utf-8")
    t = raw.replace("\u00A0", " ").replace("\u2019", "'")
    violations = 0

    # 1. Em-dash
    count_em = raw.count("\u2014")
    if count_em > 0:
        print(f"VIOLATION: {count_em} em-dash (U+2014) trouvé(s)")
        violations += 1

    # 2. En-dash
    count_en = raw.count("\u2013")
    if count_en > 0:
        print(f"VIOLATION: {count_en} en-dash (U+2013) trouvé(s)")
        violations += 1

    # 3. Espace simple avant : ; ! ?
    bad_spaces = len(re.findall(r"[^\u00A0] [:;!?]", raw))
    if bad_spaces > 0:
        print(f"VIOLATION: {bad_spaces} espace(s) simple(s) avant ponctuation (: ; ! ?)")
        violations += 1

    # 4. Guillemets équilibrés
    opens = raw.count("\u00ab")
    closes = raw.count("\u00bb")
    if opens != closes:
        print(f"VIOLATION: guillemets déséquilibrés («={opens}, »={closes})")
        violations += 1

    # 5. Compte de mots
    words = len(t.split())
    print(f"INFO: {words} mots")
    if cible_mots is not None:
        marge = int(cible_mots * 0.15)
        if words < cible_mots - marge:
            print(f"VIOLATION: {words} mots < cible {cible_mots} (marge -{marge})")
            violations += 1
        elif words > cible_mots + marge:
            print(f"VIOLATION: {words} mots > cible {cible_mots} (marge +{marge})")
            violations += 1
        else:
            print(f"OK: mots dans la cible {cible_mots} ±{marge}")

    # 6. Chiffres clés
    if chiffres:
        for c in chiffres:
            c_stripped = c.strip()
            if c_stripped not in raw and c_stripped not in t:
                print(f"VIOLATION: chiffre attendu absent: '{c_stripped}'")
                violations += 1

    # 7. Liens / emails
    if liens:
        for l in liens:
            l_stripped = l.strip()
            if l_stripped not in raw:
                print(f"VIOLATION: lien/email attendu absent: '{l_stripped}'")
                violations += 1

    # 8. Doubles espaces
    doubles = len(re.findall(r"  ", raw))
    if doubles > 0:
        print(f"VIOLATION: {doubles} double(s) espace(s)")
        violations += 1

    if violations == 0:
        print("OK: toutes les contraintes validées.")
        return 0
    else:
        print(f"ERREUR: {violations} violation(s) au total.")
        return 1


def main():
    parser = argparse.ArgumentParser(description="Validation technique de texte français")
    parser.add_argument("fichier", help="Chemin du fichier à valider")
    parser.add_argument("--cible-mots", type=int, help="Nombre de mots cible (±15%%)")
    parser.add_argument("--chiffres", help="Chiffres clés attendus (séparés par |)")
    parser.add_argument("--liens", help="Liens/emails attendus (séparés par |)")
    args = parser.parse_args()

    chiffres_list = args.chiffres.split("|") if args.chiffres else None
    liens_list = args.liens.split("|") if args.liens else None

    sys.exit(validate(args.fichier, args.cible_mots, chiffres_list, liens_list))


if __name__ == "__main__":
    main()
