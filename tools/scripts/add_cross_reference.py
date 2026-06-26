#!/usr/bin/env python3
"""Ajoute cross_reference: + supprime les doublons de marquage: dans les fichiers d'enquete.

Problemes corriges:
1. Section detectee par 'REMONTEE_DES_FILS:' (YAML key, pas commentaire)
2. Doublons de marquage:/pelote_verification: supprimes (garde la derniere occurrence)
3. cross_reference: ajoutee apres chaque manifestation_dans_evenement:

Usage:
    python3 tools/scripts/add_cross_reference.py --write
    python3 tools/scripts/add_cross_reference.py  (dry-run)
"""

import os, sys

# Mapping fil letter -> coherence note
FIL_COHERENCE = {
    "A": "Acte 1803 confirme. Renforcements 1808, 1858, 1941, 1958 dans referentiel.",
    "B": "Acte 1791 confirme. Renforcements 1811, 1945, 1958 dans referentiel.",
    "C": "Acte 1791 confirme. Renforcements 1804, 1884, 1901 dans referentiel.",
    "D": "Acte 1804 confirme. Renforcements 1872, 1958 dans referentiel.",
    "E": "Acte 1811 confirme. Renforcements 1881, 1964 dans referentiel.",
    "F": "Acte 1808 confirme. Renforcements 1833, 1881, 1975 dans referentiel.",
    "G": "Acte 1789 confirme. Renforcements 1801, 1905, 1946 dans referentiel.",
    "H": "Acte 1660 confirme (RACINE ANCIENNE). Renforcements 1792, 1840, 1945 dans referentiel.",
    "I": "Acte 1992 confirme. Necessite pre-acte 1983 Virage rigueur documente.",
    "L": "Acte 1914 confirme (fil moderne). Renforcements 1945, 2007, 2017 dans referentiel.",
}


def fix_file(filepath, write_mode=False):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    new_lines = []
    current_fil = None
    in_remontee = False
    just_added_manifestation = False  # Track if we just added manifestation line
    modified = False

    for i, line in enumerate(lines):
        stripped = line.rstrip('\n')

        # Detect REMONTEE_DES_FILS section start
        if stripped.rstrip() == 'REMONTEE_DES_FILS:' or stripped.rstrip().startswith('REMONTEE_DES_FILS:'):
            in_remontee = True

        # Detect end of REMONTEE_DES_FILS section (next top-level YAML key starting with non-space)
        if in_remontee and stripped and not stripped[0].isspace() and not stripped.startswith('#'):
            if not stripped.startswith('REMONTEE_DES_FILS'):
                in_remontee = False

        # Detect fil: line within REMONTEE_DES_FILS
        if in_remontee and stripped.lstrip().startswith('- fil:'):
            # Extract fil letter from:     - fil: "X — Name"
            quote_content = stripped.split('"')
            if len(quote_content) >= 2:
                letter_part = quote_content[1].strip().split()[0] if quote_content[1] else ''
                current_fil = letter_part[0] if letter_part and letter_part.isalpha() else None
            just_added_manifestation = False

        # Handle duplicate marquage:/pelote_verification: lines within REMONTEE_DES_FILS
        # If we see a second marquage: while still in a fil block, skip it
        if in_remontee and current_fil and just_added_manifestation:
            # After manifestation_dans_evenement, reset
            pass

        # Check for duplicate marquage (skip duplicates)
        # Pattern: two consecutive marquage: lines at same indentation
        is_marquage = stripped.lstrip().startswith('marquage:')
        is_pelote = stripped.lstrip().startswith('pelote_verification:')

        # Skip if this is a duplicate marquage/pelote_verification and we've already seen one
        if is_marquage or is_pelote:
            # Check if the PREVIOUS line already had the same field
            if new_lines:
                prev = new_lines[-1].rstrip('\n')
                prev_field = prev.lstrip().split(':')[0] if ':' in prev else ''
                current_field = stripped.lstrip().split(':')[0] if ':' in stripped else ''
                if prev_field == current_field:
                    modified = True
                    continue  # Skip this duplicate

        new_lines.append(line)

        # After manifestation_dans_evenement: line, add cross_reference
        if in_remontee and current_fil and 'manifestation_dans_evenement:' in stripped:
            just_added_manifestation = True
            # Check if cross_reference already exists (look ahead up to 3 lines)
            already_has_ref = False
            for j in range(i + 1, min(i + 4, len(lines))):
                if lines[j].lstrip().startswith('cross_reference:'):
                    already_has_ref = True
                    break
                if lines[j].strip() and not lines[j].strip().startswith('#'):
                    # If we hit a non-empty, non-comment line that's not cross_reference, stop
                    if not lines[j].lstrip().startswith('manifestation_dans_evenement'):
                        break

            if not already_has_ref:
                note = FIL_COHERENCE.get(current_fil, "Verifier dans le referentiel.")
                ref_lines = [
                    f'      cross_reference:\n',
                    f'        referentiel: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"\n',
                    f'        coherence: "{note}"\n',
                ]
                new_lines.extend(ref_lines)
                modified = True
                current_fil = None  # Reset to avoid re-adding for same fil

    if modified and write_mode:
        with open(filepath, 'w') as f:
            f.writelines(new_lines)
        return True
    elif modified:
        return True
    return False


def main():
    write_mode = "--write" in sys.argv

    base_dir = "investigations/2026-06-25_fresque_systemique/02_enquetes"
    skip_patterns = ['responsability', 'ANALYSE', 'archive']

    files = sorted(os.listdir(base_dir))
    investigations = [f for f in files if f.endswith('.md')
                      and f.startswith('2026-06-26_')
                      and not any(p in f for p in skip_patterns)]

    print("Correction Pelote — dedup marquage + ajout cross_reference")
    print(f"Mode: {'ECRITURE' if write_mode else 'DRY-RUN'}")
    print(f"Fichiers: {len(investigations)}\n")

    modified = 0
    for inv_file in investigations:
        filepath = os.path.join(base_dir, inv_file)
        print(f"  {inv_file}: ", end='')
        if fix_file(filepath, write_mode):
            modified += 1
            print("MODIFIE" if write_mode else "SERAIT MODIFIE")
        else:
            print("OK")

    print(f"\nTotal: {modified}/{len(investigations)} fichiers modifies")


if __name__ == "__main__":
    main()
