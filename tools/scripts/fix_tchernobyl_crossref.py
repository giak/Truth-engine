#!/usr/bin/env python3
"""Supprime les doublons cross_reference scriptes dans Tchernobyl.

Probleme: Tchernobyl a ete standardise manuellement avec cross_reference
AVANT manifestation_dans_evenement, puis le script add_cross_reference.py 
en a ajoute une seconde APRES manifestation_dans_evenement pour chaque fil.

Solution: Pour chaque fil, conserver la premiere cross_reference (manuelle)
et supprimer la seconde (scriptee).

Usage:
    python3 tools/scripts/fix_tchernobyl_crossref.py --write
"""

import os, sys


def fix_tchernobyl(filepath, write_mode=False):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    original = lines.copy()
    result = []
    
    in_remontee = False
    in_fil_block = False
    has_seen_manifestation = False
    has_seen_crossref_before_manifest = False
    skip_cross_block = 0  # Lines left to skip in current cross_reference block
    
    for i, line in enumerate(lines):
        stripped = line.rstrip()
        
        # Skip lines if we're skipping a cross_reference block
        if skip_cross_block > 0:
            skip_cross_block -= 1
            continue
        
        # Detect REMONTEE_DES_FILS section
        if stripped.rstrip() == 'REMONTEE_DES_FILS:' or stripped.rstrip().startswith('REMONTEE_DES_FILS:'):
            in_remontee = True
        
        # Detect end of REMONTEE_DES_FILS
        if in_remontee and stripped and not stripped[0].isspace() and not stripped.startswith('#'):
            if not stripped.startswith('REMONTEE_DES_FILS'):
                in_remontee = False
                in_fil_block = False
                has_seen_manifestation = False
                has_seen_crossref_before_manifest = False
        
        # Detect fil block start
        if in_remontee and stripped.lstrip().startswith('- fil:'):
            in_fil_block = True
            has_seen_manifestation = False
            has_seen_crossref_before_manifest = False
        
        # Track manifestation
        if in_remontee and in_fil_block and 'manifestation_dans_evenement:' in stripped:
            has_seen_manifestation = True
        
        # Track cross_reference BEFORE manifestation -> keep
        if in_remontee and in_fil_block and stripped.lstrip().startswith('cross_reference:'):
            if has_seen_manifestation:
                # This cross_reference is AFTER manifestation -> it's the scripted duplicate
                # Count lines in this block
                block_size = 1  # Current line
                for j in range(i + 1, len(lines)):
                    if lines[j].strip() and lines[j][0].isspace():
                        block_size += 1
                    else:
                        break
                # Skip this block
                skip_cross_block = block_size - 1  # -1 because current line is being processed
                print(f"  [LIGNE {i+1}] cross_reference scriptee supprimee ({block_size} lignes)")
                continue
            else:
                # cross_reference before manifestation -> manual, keep it
                has_seen_crossref_before_manifest = True
        
        result.append(line)
    
    modified = (result != original)
    
    if modified and write_mode:
        with open(filepath, 'w') as f:
            f.writelines(result)
    
    return modified


def main():
    write_mode = "--write" in sys.argv
    
    filepath = "investigations/2026-06-25_fresque_systemique/02_enquetes/2026-06-26_tchernobyl_bascule_INVESTIGATION.md"
    
    print("Fix Tchernobyl — suppression cross_reference scriptees (apres manifestation)")
    print(f"Mode: {'ECRITURE' if write_mode else 'DRY-RUN'}\n")
    
    modified = fix_tchernobyl(filepath, write_mode)
    
    if modified:
        print(f"\nFichier {'modifie' if write_mode else 'serait modifie'}")
    else:
        print("\nOK — aucun changement necessaire")


if __name__ == "__main__":
    main()
