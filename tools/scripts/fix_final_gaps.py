#!/usr/bin/env python3
"""FIX FINAL: deduppe gaps_verifies Tchernobyl + ajoute chaine_causale + gaps aux fils niches manquants.

Probleme 1 — Tchernobyl: chaque fil a 2 blocs gaps_verifies consecutifs
  (un scripte generique a 8 espaces, un manuel detaille a 6 espaces).
  Solution: supprimer le bloc scripte (celui a 8 espaces d'indentation).

Probleme 2 — Niches: 3 fils (E, H, L) n'ont PAS de chaine_causale du tout.
  Solution: ajouter une chaine_causale minimale + gaps_verifies pour chaque.

Usage:
    python3 tools/scripts/fix_final_gaps.py --write
"""

import os, sys


def fix_tchernobyl_gaps(lines):
    """Remove the scripted generic gaps_verifies (8 spaces indent) from Tchernobyl."""
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip()
        
        # Detect gaps_verifies at 8 spaces indent (inside chaine_causale block)
        # This is the scripted generic one inserted between chaine items and manual gaps
        if stripped.startswith('        gaps_verifies:'):
            # Check if this is followed by more gaps_verifies (the manual one) at 6 spaces
            # We need to look ahead past the content lines
            j = i + 1
            indent_8_count = 1  # Count of lines in this 8-space block
            
            # Count the lines in this gaps_verifies block (at 8+ spaces)
            while j < len(lines):
                next_line = lines[j].rstrip()
                if next_line.startswith('          '):  # 10 spaces = content
                    indent_8_count += 1
                    j += 1
                else:
                    break
            
            # Now check if the next non-blank line is ALSO gaps_verifies: (at 6 spaces)
            check_j = j
            while check_j < len(lines) and not lines[check_j].strip():
                check_j += 1
            
            if check_j < len(lines):
                next_stripped = lines[check_j].rstrip()
                if next_stripped.startswith('      gaps_verifies:'):
                    # Duplicate — skip the 8-space block
                    print(f"    [LIGNE {i+1}] doubles gaps TChernobyl: garde le manuel (6 esp), supprime le scripte (8 esp)")
                    i = j  # Skip to after the 8-space block
                    continue
        
        result.append(line)
        i += 1
    
    return result


def get_niches_fix_content():
    """Return content for 3 missing chaine_causale blocks in niches_fiscales."""
    
    fil_e = '''      chaine_causale:
        - "1811 (presse autoritaire) -> 1881 (liberte conditionnelle) -> 1964-1982 (ORTF) -> 2010-2026 : les niches quasi-invisibles dans les medias de masse. Les rares articles sont techniques, sans mise en recit politique."
        gaps_verifies:
          - "Gap 1811->1881 : 70 ans — GAP. Renforcement manquant : 1852 (censure Second Empire). A verifier dans le referentiel."
          - "Gap 1881->1964 : 83 ans — GAP. Renforcement manquant : 1914 (loi de guerre sur la presse). A verifier dans le referentiel."
          - "Gap 1964->2010 : 46 ans — GAP. Renforcement manquant : 1982 (loi audiovisuelle, creation CSA). A verifier."
'''
    fil_h = '''      chaine_causale:
        - "1660 (Colbert : Etat entrepreneur) -> 1792 (Premiere Republique : continuite de l'Etat fort) -> 1840 (Etat modernisateur) -> 1945 (Etat keynesien) -> 2010 : rapport Lambert enterre — l'Etat ne se remet pas en question sur les niches"
        gaps_verifies:
          - "Gap 1660->1792 : 132 ans — GAP. Racine ANCIENNE — saut inherent au fil H (Exceptionnalisme). Justification : periode d'Ancien Regime puis Revolution."
          - "Gap 1792->1840 : 48 ans — GAP. Renforcement manquant : 1815 (Restauration). A verifier dans le referentiel."
          - "Gap 1840->1945 : 105 ans — GAP. Renforcement manquant : 1871, 1914-1918. A verifier."
          - "Gap 1945->2010 : 65 ans — GAP. Renforcement manquant : 1958 (constitution Ve), 1981 (decentralisation). A verifier."
'''
    fil_l = '''      chaine_causale:
        - "1914 (Loi Caillaux : creation IR) -> 1945 (Etat keynesien : niches comme outil de pilotage) -> 2007 (Loi TEPA : bouquet de niches pour le capital) -> 2017-2018 (ISF->IFI + flat tax : verrouillage asymetrie) -> 2026 : 470 niches, 90-100 MdE/an, l'asymetrie est verrouillee"
        gaps_verifies:
          - "Gap 1914->1945 : 31 ans — GAP. Renforcement manquant : 1920s (niches naissantes). A verifier."
          - "Gap 1945->2007 : 62 ans — GAP. Renforcement manquant : 1959 (LOLF), 1970s (explosion niches). A verifier dans le referentiel."
          - "Gap 2007->2017 : 10 ans — OK"
          - "Gap 2017->2026 : 9 ans — OK"
'''
    return {"E": fil_e, "H": fil_h, "L": fil_l}


def fix_niches_missing_chaine(lines, filepath):
    """Add chaine_causale + gaps_verifies to niches fils E, H, L.
    
    Detection: parcourt les blocs de fil. Pour chaque fil, verifie
    si chaine_causale: est present. Si non, l'insere avant le prochain fil.
    """
    basename = os.path.basename(filepath)
    if 'niches_fiscales' not in basename:
        return lines, False
    
    fix_content = get_niches_fix_content()
    result = []
    modified = False
    
    # Map fil letters to their names as they appear in the file
    fil_names = {
        "E": '- fil: "E — Presse',
        "H": '- fil: "H — Exceptionnalisme',
        "L": '- fil: "L — Fiscalite',
    }
    
    # Build a set of fil start line indices that are MISSING chaine_causale
    missing_fils = {}  # line_index -> fil_letter
    
    current_fil_line = None
    current_fil_letter = None
    has_chaine = False
    
    for i, line in enumerate(lines):
        stripped = line.rstrip()
        lstripped = stripped.lstrip()
        
        # Detect start of fil block
        for letter, name in fil_names.items():
            if lstripped.startswith(name):
                # Previous fil block ended — check if it had chaine_causale
                if current_fil_letter and not has_chaine and current_fil_line is not None:
                    missing_fils[current_fil_line] = current_fil_letter
                current_fil_letter = letter
                current_fil_line = i
                has_chaine = False
                break
        
        # Check if current fil has chaine_causale
        if current_fil_letter and 'chaine_causale:' in stripped:
            has_chaine = True
        
        # Detect end of REMONTEE_DES_FILS section
        if stripped and not stripped[0].isspace() and not stripped.startswith('#'):
            if 'REMONTEE_DES_FILS' not in stripped and current_fil_letter:
                if not has_chaine:
                    missing_fils[current_fil_line] = current_fil_letter
                current_fil_letter = None
                current_fil_line = None
    
    # Now insert chaine_causale blocks before each missing fil's start line
    if missing_fils:
        modified = True
        for fil_line, fil_letter in sorted(missing_fils.items()):
            print(f"    [FIL {fil_letter} ligne {fil_line+1}] insertion chaine_causale + gaps")
    
    # Rebuild lines with insertions
    for i, line in enumerate(lines):
        if i in missing_fils:
            letter = missing_fils[i]
            result.append(fix_content[letter])
            result.append('\n')
        result.append(line)
    
    return result, modified


def fix_file(filepath, write_mode=False):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    original = lines.copy()
    basename = os.path.basename(filepath)
    
    # Step 1: Fix Tchernobyl duplicate gaps
    if 'tchernobyl' in basename:
        lines = fix_tchernobyl_gaps(lines)
    
    # Step 2: Fix niches missing chaine_causale
    lines, niches_modified = fix_niches_missing_chaine(lines, filepath)
    
    modified = (lines != original)
    
    if modified and write_mode:
        with open(filepath, 'w') as f:
            f.writelines(lines)
        return True
    return modified


def main():
    write_mode = "--write" in sys.argv
    
    base_dir = "investigations/2026-06-25_fresque_systemique/02_enquetes"
    target_files = [
        '2026-06-26_niches_fiscales_v2.3_INVESTIGATION.md',
        '2026-06-26_tchernobyl_bascule_INVESTIGATION.md',
    ]
    
    print("FIX FINAL — dedup gaps Tchernobyl + chaines manquantes niches")
    print(f"Mode: {'ECRITURE' if write_mode else 'DRY-RUN'}\n")
    
    modified = 0
    for inv_file in target_files:
        filepath = os.path.join(base_dir, inv_file)
        print(f"  {inv_file}:")
        if fix_file(filepath, write_mode):
            modified += 1
            print(f"  -> {'MODIFIE' if write_mode else 'SERAIT MODIFIE'}")
        else:
            print(f"  -> OK")
    
    print(f"\nTotal: {modified}/{len(target_files)} fichiers modifies")


if __name__ == "__main__":
    main()
