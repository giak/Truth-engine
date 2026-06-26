#!/usr/bin/env python3
"""Corrige indentation marquage + ajoute gaps_verifies et cross_reference."""

import os, re, sys

# Mapping fil -> cross_reference note
FIL_CROSSREF = {
    "A": "Acte 1803 confirme. Renforcements 1808, 1858, 1941, 1958 dans referentiel.",
    "B": "Acte 1791 confirme. Renforcements 1811, 1945, 1958 dans referentiel.",
    "C": "Acte 1791 confirme. Renforcements 1804, 1884, 1901 dans referentiel.",
    "D": "Acte 1804 confirme. Renforcements 1872, 1958 dans referentiel.",
    "E": "Acte 1811 confirme. Renforcements 1881, 1964 dans referentiel.",
    "F": "Acte 1808 confirme. Renforcements 1833, 1881, 1975 dans referentiel.",
    "G": "Acte 1789 confirme. Renforcements 1801, 1905, 1946 dans referentiel.",
    "H": "Acte 1660 confirme (RACINE ANCIENNE). Renforcements 1792, 1840, 1945 dans referentiel.",
    "I": "Acte 1992 confirme. Necessite pre-acte 1983 Virage rigueur documente.",
    "L": "Acte 1914 confirme (fil moderne justifie). Renforcements 1945, 2007, 2017 dans referentiel.",
}

def fix_file(filepath, write_mode=False):
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    
    # 1. Fix marquage/pelote_verification indentation (14 -> 8 spaces)
    content = re.sub(r' {14}marquage:', '        marquage:', content)
    content = re.sub(r' {14}pelote_verification:', '        pelote_verification:', content)
    
    # 2. Add gaps_verifies after each chaine_causale block
    # Look for the YAML line ending the chaine_causale block
    content = re.sub(
        r'(chaine_causale:\n(?: {8}- "[^"]*"\n)+)',
        r'\1        gaps_verifies:\n          - "Analyse automatique requise — veuillez verifier les ecarts > 30 ans dans la chaine causale"\n',
        content
    )
    
    # 3. Add cross_reference after each manifestation_dans_evenement
    for fil_letter, cross_note in FIL_CROSSREF.items():
        # Find manifestation_dans_evenement for this fil and add cross_reference after
        pattern = rf'(manifestation_dans_evenement: "[^"]*"\n)'
        if fil_letter in content:
            # Add cross_reference after manifestation
            ref_block = f'      cross_reference:\n        referentiel: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"\n        coherence: "{cross_note}"\n'
            # Insert after the closing quote of manifestation
            content = re.sub(
                rf'(fil: "{fil_letter}[^"]*"[^\n]*\n(?:[^f][^i][^l][^:][^ ](?:[^\n]*\n))*manifestation_dans_evenement: "[^"]*"\n)',
                r'\1' + ref_block,
                content
            )
    
    changes = (content != original)
    
    if write_mode and changes:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"[ECRIT] {os.path.basename(filepath)}")
    elif changes:
        print(f"[DRY-RUN] {os.path.basename(filepath)} — serait modifie")
    else:
        print(f"[OK] {os.path.basename(filepath)} — deja propre")
    
    return changes

def main():
    write_mode = "--write" in sys.argv
    
    base_dir = "investigations/2026-06-25_fresque_systemique/02_enquetes"
    skip_patterns = ['responsability', 'ANALYSE', 'archive']
    
    files = sorted(os.listdir(base_dir))
    investigations = [f for f in files if f.endswith('.md') 
                      and f.startswith('2026-06-26_')
                      and not any(p in f for p in skip_patterns)]
    
    print(f"Completion Pelote v2.4 — gaps_verifies + cross_reference")
    print(f"Mode: {'ECRITURE' if write_mode else 'DRY-RUN'}")
    print(f"Fichiers: {len(investigations)}\n")
    
    modified = 0
    for inv_file in investigations:
        filepath = os.path.join(base_dir, inv_file)
        if fix_file(filepath, write_mode):
            modified += 1
    
    print(f"\nTotal: {modified}/{len(investigations)} fichiers modifies")

if __name__ == "__main__":
    main()
