#!/usr/bin/env python3
"""
CLI outil pour ajouter des faits dans les chroniques.

Usage:
  python3 tools/enrich_chronique.py <fichier> <fait> [<fait> ...]
  python3 tools/enrich_chronique.py --file 2026_DIP.md "| 2026 | DIP | Description | ❌ |"
  python3 tools/enrich_chronique.py --stdin < faits.txt

Exemples:
  # Ajouter un fait à un fichier existant
  python3 tools/enrich_chronique.py 2026_DIP.md "| 2026-05-10 | DIP | Macron a Nairobi : pre carre termine | ❌ |"

  # Ajouter plusieurs faits
  python3 tools/enrich_chronique.py 2026_DIP.md "| 2026-05-11 | DIP | Africa Forward 23 MdE | ❌ |" "| 2026-05-12 | DIP | Declaration Nairobi | ❌ |"

  # Créer un nouveau fichier (crée le dossier si nécessaire)
  python3 tools/enrich_chronique.py 1945_DIP.md "| 1945-12-26 | DIP | Creation du franc CFA | ❌ |"
"""

import os
import re
import sys
from pathlib import Path

CHRONIQUES_DIR = Path(__file__).resolve().parent.parent / 'investigations' / '2026-06-25_fresque_systemique' / '01_donnees' / 'chroniques'

def parse_file_ref(ref):
    """Parse a file reference like '2026_DIP.md' or '2026/2026_DIP.md'."""
    ref = ref.strip()
    if '/' in ref:
        parts = ref.split('/')
        return Path(*parts)
    # Extract year from filename: 2026_DIP.md -> year=2026
    year = ref.split('_')[0]
    return Path(year) / ref

def count_data_rows(content):
    """Count data rows in chronique file, excluding header and separator."""
    count = 0
    for line in content.split('\n'):
        stripped = line.strip()
        if not (stripped.startswith('|') and stripped.endswith('|')):
            continue
        parts = [p.strip() for p in stripped.split('|')]
        if len(parts) >= 5:
            yr = parts[1].strip().lower()
            dm = parts[2].strip() if len(parts) > 2 else ''
            # Accept both accented and unaccented headers
            if yr in ('année', 'annee', '---') or dm == '---':
                continue
            count += 1
    return count

def add_facts(file_path, new_lines, dry_run=False):
    """Add facts to a chronique file. Creates file if it doesn't exist."""
    fp = CHRONIQUES_DIR / file_path
    
    if not fp.exists():
        # Create parent directory
        fp.parent.mkdir(parents=True, exist_ok=True)
        # Infer year and dim from filename
        parts = fp.stem.split('_')
        year = parts[0]
        dim = parts[1] if len(parts) > 1 else '???'
        
        # Format with proper accents and em dash
        content = (
            f"# Chronique {year} — Dimension {dim}\n"
            f"\n"
            f"> Fait atomique extrait de l'HYPER-MATRICE FRANCE 1975-2026.\n"
            f"> 0 événement(s) classé(s) dans la dimension {dim} pour l'année {year}.\n"
            f"\n"
            f"| Année | Dimension | Description | Code |\n"
            f"|---|---|---|---|\n"
        )
    else:
        with open(fp, 'r') as f:
            content = f.read()
    
    # Check for duplicates
    existing_lines = set()
    for line in content.split('\n'):
        stripped = line.strip()
        if stripped.startswith('|') and stripped.endswith('|'):
            existing_lines.add(stripped)
    
    to_add = []
    for line in new_lines:
        stripped = line.strip()
        # Normalize: strip outer pipes and re-add for consistent comparison
        if stripped in existing_lines:
            print(f"  ⏭️  Doublon: {stripped[:80]}...", file=sys.stderr)
            continue
        to_add.append(line)
    
    if not to_add:
        print("  Rien à ajouter.", file=sys.stderr)
        return 0
    
    if dry_run:
        print(f"  Ajouterait {len(to_add)} ligne(s) à {fp.name}:", file=sys.stderr)
        for line in to_add:
            print(f"    {line.strip()[:100]}", file=sys.stderr)
        return len(to_add)
    
    # Append and recalculate header
    content = content.rstrip('\n') + '\n' + '\n'.join(to_add) + '\n'
    n = count_data_rows(content)
    
    # Update header count - try both accented and unaccented patterns
    content = re.sub(r'> (\d+) événement', f'> {n} événement', content)
    content = re.sub(r'> (\d+) evenement', f'> {n} evenement', content)
    
    with open(fp, 'w') as f:
        f.write(content)
    
    print(f"  ✅ {fp.name}: +{len(to_add)} ligne(s), total {n} événement(s)", file=sys.stderr)
    return len(to_add)

def main():
    if '--help' in sys.argv or '-h' in sys.argv:
        print(__doc__)
        return 0
    
    # Parse arguments
    dry_run = '--dry-run' in sys.argv
    stdin_mode = '--stdin' in sys.argv
    
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    
    if stdin_mode:
        facts = [line for line in sys.stdin.read().split('\n') if line.strip()]
        if not facts:
            print("Erreur: aucune donnée sur stdin.", file=sys.stderr)
            return 1
        file_ref = facts[0] if len(facts) > 1 else None
        lines = facts[1:] if len(facts) > 1 else []
    else:
        if len(args) < 2:
            print("Usage: enrich_chronique.py <fichier> <fait> [<fait> ...]", file=sys.stderr)
            print("       enrich_chronique.py --stdin < faits.txt", file=sys.stderr)
            print("       enrich_chronique.py --help", file=sys.stderr)
            return 1
        file_ref = args[0]
        lines = args[1:]
    
    file_path = parse_file_ref(file_ref)
    
    try:
        added = add_facts(file_path, lines, dry_run)
        return 0 if added is not None else 1
    except Exception as e:
        print(f"Erreur: {e}", file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
