#!/usr/bin/env python3
"""NETTOYAGE FINAL PELOTE v2.4.

Problemes corriges:
1. Doublons marquage/pelote_verification dans acte_naissance (6 fichiers)
2. Doublons cross_reference dans Tchernobyl (scripte + manuelle)
3. Gaps_verifies manquants dans niches_fiscales

Usage:
    python3 tools/scripts/cleanup_pelote_doublons.py --write
"""

import os, re, sys


def remove_duplicate_pairs(lines):
    """Remove duplicate marquage/pelote_verification pairs.
    
    Pattern detected:
            marquage: "..."       # keep
            pelote_verification: "..."  # keep
            marquage: "..."       # DUPLICATE - remove
            pelote_verification: "..."  # DUPLICATE - remove
    
    Uses while loop for precise index control.
    """
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip()
        is_marquage = stripped.lstrip().startswith('marquage:')
        
        # Check for duplicate pattern: marquage ⟶ pelote ⟶ marquage ⟶ pelote
        if is_marquage and i + 3 < len(lines):
            n1 = lines[i+1].rstrip().lstrip().startswith('pelote_verification:')
            n2 = lines[i+2].rstrip().lstrip().startswith('marquage:')
            n3 = lines[i+3].rstrip().lstrip().startswith('pelote_verification:')
            
            if n1 and n2 and n3:
                # Keep first pair, skip second pair (lines i+2, i+3)
                result.append(line)
                result.append(lines[i+1])
                i += 4
                continue
        
        result.append(line)
        i += 1
    
    return result


def remove_duplicate_cross_reference(lines):
    """Remove duplicate cross_reference blocks.
    
    Pattern: two cross_reference blocks with same referentiel.
    Keep the first (manual) one, remove the second (scripted).
    """
    result = []
    skip_cross_block = 0  # Lines left to skip in current cross_reference block
    
    for i, line in enumerate(lines):
        if skip_cross_block > 0:
            skip_cross_block -= 1
            continue
        
        stripped = line.rstrip()
        is_cross = stripped.lstrip().startswith('cross_reference:')
        
        if is_cross:
            # Count lines in this cross_reference block (until next non-indented line)
            block_lines = 1
            for j in range(i + 1, len(lines)):
                if lines[j].strip() and lines[j][0].isspace():
                    block_lines += 1
                else:
                    break
            
            # Check if another cross_reference block follows immediately
            next_block_start = i + block_lines
            if next_block_start < len(lines):
                next_stripped = lines[next_block_start].rstrip().lstrip()
                if next_stripped.startswith('cross_reference:'):
                    # Two blocks in a row - skip the second
                    skip_cross_block = 0
                    # Count lines in second block
                    for j in range(next_block_start + 1, len(lines)):
                        if lines[j].strip() and lines[j][0].isspace():
                            skip_cross_block += 1
                        else:
                            break
                    skip_cross_block += 1  # +1 for the cross_reference: line itself
        
        result.append(line)
    
    return result


def fix_missing_gaps(lines):
    """Add missing gaps_verifies after chaine_causale blocks that lack them."""
    result = []
    in_chaine_block = False
    chaine_lines = []
    
    for i, line in enumerate(lines):
        stripped = line.rstrip()
        
        # Detect chaine_causale: line
        if stripped.lstrip().startswith('chaine_causale:'):
            in_chaine_block = True
            chaine_lines = [line]
            continue
        
        if in_chaine_block:
            # Check if this is still part of the chaine_causale block
            # Lines look like:        - "..." (8 spaces + -)
            is_chaine_item = stripped.lstrip().startswith('- "') and stripped[0].isspace()
            is_gaps = stripped.lstrip().startswith('gaps_verifies:')
            
            if is_chaine_item:
                chaine_lines.append(line)
                continue
            elif is_gaps:
                # Gaps already exists - output chaine + this line normally
                result.extend(chaine_lines)
                result.append(line)
                in_chaine_block = False
                chaine_lines = []
                continue
            else:
                # End of chaine block without gaps_verifies - add it
                result.extend(chaine_lines)
                result.append('        gaps_verifies:\n')
                result.append('          - "Analyse automatique requise — veuillez verifier les ecarts > 30 ans dans la chaine causale"\n')
                result.append(line)
                in_chaine_block = False
                chaine_lines = []
                continue
        
        result.append(line)
    
    # Handle case where file ends inside chaine block (unlikely)
    if in_chaine_block:
        result.extend(chaine_lines)
    
    return result


def fix_file(filepath, write_mode=False):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    original = lines.copy()
    
    # Step 1: Remove duplicate marquage/pelote_verification pairs
    lines = remove_duplicate_pairs(lines)
    
    # Step 2: Remove duplicate cross_reference blocks (Tchernobyl)
    lines = remove_duplicate_cross_reference(lines)
    
    # Step 3: Fix missing gaps_verifies (niches)
    lines = fix_missing_gaps(lines)
    
    modified = (lines != original)
    
    if modified and write_mode:
        with open(filepath, 'w') as f:
            f.writelines(lines)
        return True
    return modified


def main():
    write_mode = "--write" in sys.argv
    
    base_dir = "investigations/2026-06-25_fresque_systemique/02_enquetes"
    skip_patterns = ['responsability', 'ANALYSE', 'archive']
    
    files = sorted(os.listdir(base_dir))
    investigations = [f for f in files if f.endswith('.md')
                      and f.startswith('2026-06-26_')
                      and not any(p in f for p in skip_patterns)]
    
    print("NETTOYAGE FINAL PELOTE v2.4 — dedup marquage + cross_ref + gaps manquants")
    print(f"Mode: {'ECRITURE' if write_mode else 'DRY-RUN'}")
    print(f"Fichiers: {len(investigations)}\n")
    
    modified = 0
    for inv_file in investigations:
        filepath = os.path.join(base_dir, inv_file)
        if fix_file(filepath, write_mode):
            modified += 1
            print(f"  {inv_file}: {'MODIFIE' if write_mode else 'SERAIT MODIFIE'}")
        else:
            print(f"  {inv_file}: OK")
    
    print(f"\nTotal: {modified}/{len(investigations)} fichiers modifies")
    if modified > 0 and not write_mode:
        print("Relancez avec --write pour ecrire.")


if __name__ == "__main__":
    main()
