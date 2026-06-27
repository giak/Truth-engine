#!/usr/bin/env python3
"""
CLI outil pour ajouter, supprimer, scinder, déplacer et vérifier les faits dans les chroniques.

Usage:
  python3 tools/enrich_chronique.py <fichier> <fait> [<fait> ...]    Ajouter des faits
  python3 tools/enrich_chronique.py --remove <fichier> <ligne>      Supprimer une ligne
  python3 tools/enrich_chronique.py --split <fichier> <ancienne> <n1> [<n2> ...]   Scinder
  python3 tools/enrich_chronique.py --move <src> <dst> <ligne>      Déplacer d'un fichier à l'autre
  python3 tools/enrich_chronique.py --check [<fichier> | --all]     Vérifier les compteurs
  python3 tools/enrich_chronique.py --stdin < faits.txt             Ajouter depuis stdin
  python3 tools/enrich_chronique.py --dry-run <fichier> <fait>...   Simuler sans écrire

Exemples:
  # Ajouter
  python3 tools/enrich_chronique.py 2026_DIP.md "| 2026 | DIP | Macron a Nairobi | ❌ |"

  # Supprimer
  python3 tools/enrich_chronique.py --remove 2025_SANT.md "| 2025 | SANT | Ancienne ligne obsolete | ❌ |"

  # Scinder (auto-routage si l'année change)
  python3 tools/enrich_chronique.py --split 2025_SANT.md \
    "| 2025 | SANT | ONDAM 2025 execute a 265,4 MdE | ❌ |" \
    "| 2026 | SANT | CC : ONDAM 2025 tenu mais peu ambitieux | ❌ |"
  # -> la 2e ligne va automatiquement dans 2026_SANT.md (année différente)

  # Déplacer
  python3 tools/enrich_chronique.py --move 2025_SANT.md 2026_SANT.md \
    "| 2025 | SANT | Certains hopitaux : delais 250-300 jours | ❌ |"

  # Vérifier
  python3 tools/enrich_chronique.py --check 2025_SANT.md
  python3 tools/enrich_chronique.py --check --all
"""

import re
import sys
import unicodedata
from pathlib import Path

CHRONIQUES_DIR = Path(__file__).resolve().parent.parent / 'investigations' / '2026-06-25_fresque_systemique' / '01_donnees' / 'chroniques'


# ---------------------------------------------------------------------------
# Utilitaires
# ---------------------------------------------------------------------------

def parse_file_ref(ref):
    """Parse a file reference like '2026_DIP.md' or '2026/2026_DIP.md'."""
    ref = ref.strip()
    if '/' in ref:
        return Path(ref)
    year = ref.split('_')[0]
    return Path(year) / ref


def year_from_filename(filename):
    """Extract year from '2026_SANT.md' or path '2026/2026_SANT.md'."""
    stem = Path(filename).stem
    return stem.split('_')[0]


def dim_from_filename(filename):
    """Extract dimension from '2026_SANT.md'."""
    stem = Path(filename).stem
    parts = stem.split('_')
    return parts[1] if len(parts) > 1 else None


def end_year_from_range(year_str):
    """Extract end year from '2020-2024' -> '2024', or '2026' -> '2026'."""
    if '-' in year_str:
        parts = year_str.split('-')
        return parts[-1].strip()
    return year_str.strip()


def resolve_target_file(source_file, line):
    """Auto-route a line to the correct file based on its year column.
    
    If the line's year matches the source file's year, returns source_file.
    Otherwise, constructs the target from the end year + source dimension.
    """
    parts = [p.strip() for p in line.split('|')]
    if len(parts) < 2:
        return source_file
    year_col = parts[1]
    src_year = year_from_filename(str(source_file))
    dim = dim_from_filename(str(source_file))
    end_yr = end_year_from_range(year_col)
    
    if end_yr == src_year:
        return source_file
    
    if dim:
        target_name = f"{end_yr}_{dim}.md"
        return Path(end_yr) / target_name
    return source_file


def normalize_line(line):
    """Normalize a line for fuzzy comparison: strip accents, lowercase, collapse whitespace.
    
    This is the core AFP fix: LLM-produced data varies ('ÉDU' vs 'EDU', 'événement' vs 'evenement').
    Instead of exact string match, we normalize before comparing.
    """
    # Strip accents: é -> e, è -> e, etc.
    nfkd = unicodedata.normalize('NFKD', line.strip())
    ascii_text = nfkd.encode('ASCII', 'ignore').decode('ASCII')
    # Lowercase + collapse whitespace
    return ' '.join(ascii_text.lower().split())


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
            if yr in ('année', 'annee', '---') or dm == '---':
                continue
            count += 1
    return count


def update_header_n(content, n):
    """Update header line with new count n. Handle both accented and unaccented."""
    content = re.sub(r'> (\d+) événement', f'> {n} événement', content)
    content = re.sub(r'> (\d+) evenement', f'> {n} evenement', content)
    return content


def read_file(fp):
    """Read a chronique file and return content. Returns None if file doesn't exist."""
    if not fp.exists():
        return None
    with open(fp, 'r', encoding='utf-8') as f:
        return f.read()


def ensure_file(fp):
    """Read a chronique file, creating it with template if missing."""
    if not fp.exists():
        fp.parent.mkdir(parents=True, exist_ok=True)
        parts = fp.stem.split('_')
        year = parts[0]
        dim = parts[1] if len(parts) > 1 else '???'
        content = (
            f"# Chronique {year} — Dimension {dim}\n"
            f"\n"
            f"> Fait atomique extrait de l'HYPER-MATRICE FRANCE 1975-2026.\n"
            f"> 0 événement(s) classé(s) dans la dimension {dim} pour l'année {year}.\n"
            f"\n"
            f"| Année | Dimension | Description | Code |\n"
            f"|---|---|---|---|\n"
        )
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        return content
    with open(fp, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(fp, content):
    """Write file and log."""
    with open(fp, 'w') as f:
        f.write(content)
    n = count_data_rows(content)
    print(f"  ✅ {fp.name}: total {n} événement(s)", file=sys.stderr)


# ---------------------------------------------------------------------------
# Commandes
# ---------------------------------------------------------------------------

def cmd_add(file_path, new_lines, dry_run=False):
    """Ajouter des faits (commande par défaut)."""
    fp = CHRONIQUES_DIR / file_path
    content = ensure_file(fp)
    
    existing_norm = set()
    for line in content.split('\n'):
        stripped = line.strip()
        if stripped.startswith('|') and stripped.endswith('|'):
            existing_norm.add(normalize_line(stripped))
    
    to_add = []
    for line in new_lines:
        stripped = line.strip()
        if normalize_line(stripped) in existing_norm:
            print(f"  ⏭️  Doublon (normalisé): {stripped[:80]}...", file=sys.stderr)
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
    
    content = content.rstrip('\n') + '\n' + '\n'.join(to_add) + '\n'
    n = count_data_rows(content)
    content = update_header_n(content, n)
    write_file(fp, content)
    return len(to_add)


def cmd_remove(file_path, line_to_remove, dry_run=False):
    """Supprimer une ligne précise d'un fichier."""
    fp = CHRONIQUES_DIR / file_path
    if not fp.exists():
        print(f"  ❌ Fichier introuvable: {fp}", file=sys.stderr)
        return 1
    
    content = read_file(fp)
    if content is None:
        print(f"  ❌ Fichier introuvable: {fp}", file=sys.stderr)
        return 1
    stripped_target = line_to_remove.strip()
    
    norm_target = normalize_line(stripped_target)
    lines = content.split('\n')
    new_lines = []
    found = False
    for line in lines:
        if normalize_line(line) == norm_target:
            found = True
            continue
        new_lines.append(line)
    
    if not found:
        print(f"  ❌ Ligne introuvable dans {fp.name}: {stripped_target[:80]}...", file=sys.stderr)
        return 1
    
    if dry_run:
        print(f"  Supprimerait de {fp.name}: {stripped_target[:80]}...", file=sys.stderr)
        return 0
    
    new_content = '\n'.join(new_lines)
    n = count_data_rows(new_content)
    new_content = update_header_n(new_content, n)
    write_file(fp, new_content)
    print(f"  Supprimé: {stripped_target[:80]}...", file=sys.stderr)
    return 0


def cmd_split(file_path, old_line, new_lines, dry_run=False):
    """Scinder une ligne en plusieurs, avec auto-routage par année."""
    fp = CHRONIQUES_DIR / file_path
    stripped_old = old_line.strip()
    
    if not fp.exists():
        print(f"  ❌ Fichier introuvable: {fp}", file=sys.stderr)
        return 1
    
    content = read_file(fp)
    
    # Remove old line
    norm_old = normalize_line(stripped_old)
    lines = content.split('\n')
    new_content_lines = []
    found = False
    for line in lines:
        if normalize_line(line) == norm_old:
            found = True
            continue
        new_content_lines.append(line)
    
    if not found:
        print(f"  ❌ Ligne introuvable dans {fp.name}: {stripped_old[:80]}...", file=sys.stderr)
        return 1
    
    new_content = '\n'.join(new_content_lines)
    n = count_data_rows(new_content)
    new_content = update_header_n(new_content, n)
    
    if dry_run:
        print(f"  Enlèverait de {fp.name}: {stripped_old[:80]}...", file=sys.stderr)
    
    # Group new lines by target file
    targets = {}  # target_file -> list of lines
    for line in new_lines:
        target = resolve_target_file(fp, line)
        if target not in targets:
            targets[target] = []
        targets[target].append(line)
    
    if not dry_run:
        # Write source file
        write_file(fp, new_content)
        print(f"  Supprimé: {stripped_old[:80]}...", file=sys.stderr)
    
    # Add new lines to each target
    for target_fp_rel, add_lines in targets.items():
        target_fp = CHRONIQUES_DIR / target_fp_rel if not target_fp_rel.is_absolute() else target_fp_rel
        # If target is the source, it's already updated — add to it
        target_path = Path(target_fp_rel)
        
        tgt_content = ensure_file(target_fp) if not dry_run else read_file(target_fp)
        if tgt_content is None:
            # Dry run and file doesn't exist yet — just report
            if dry_run:
                print(f"  Ajouterait {len(add_lines)} ligne(s) dans {target_path.name} (fichier à créer):", file=sys.stderr)
                for line in add_lines:
                    print(f"    {line.strip()[:100]}", file=sys.stderr)
                continue
            tgt_content = ensure_file(target_fp)
        
        existing_lines = set()
        for line in tgt_content.split('\n'):
            stripped = line.strip()
            if stripped.startswith('|') and stripped.endswith('|'):
                existing_lines.add(normalize_line(stripped))
        
        actual_to_add = []
        for line in add_lines:
            if normalize_line(line.strip()) in existing_lines:
                if dry_run:
                    print(f"  ⏭️  (serait doublon dans {target_path.name})", file=sys.stderr)
                else:
                    print(f"  ⏭️  Doublon dans {target_path.name}: {line.strip()[:80]}...", file=sys.stderr)
                continue
            actual_to_add.append(line)
        
        if dry_run:
            if actual_to_add:
                print(f"  Ajouterait {len(actual_to_add)} ligne(s) dans {target_path.name}:", file=sys.stderr)
                for line in actual_to_add:
                    print(f"    {line.strip()[:100]}", file=sys.stderr)
        else:
            if actual_to_add:
                tgt_content = tgt_content.rstrip('\n') + '\n' + '\n'.join(actual_to_add) + '\n'
                tn = count_data_rows(tgt_content)
                tgt_content = update_header_n(tgt_content, tn)
                write_file(target_fp, tgt_content)
    
    return 0


def cmd_move(src_path, dst_path, line_to_move, dry_run=False):
    """Déplacer une ligne d'un fichier source vers un fichier destination."""
    src_fp = CHRONIQUES_DIR / src_path
    dst_fp = CHRONIQUES_DIR / dst_path
    stripped_line = line_to_move.strip()
    
    # Remove from source
    if not src_fp.exists():
        print(f"  ❌ Fichier source introuvable: {src_fp}", file=sys.stderr)
        return 1
    
    norm_line = normalize_line(stripped_line)
    content = read_file(src_fp)
    lines = content.split('\n')
    new_lines = []
    found = False
    for line in lines:
        if normalize_line(line) == norm_line:
            found = True
            continue
        new_lines.append(line)
    
    if not found:
        print(f"  ❌ Ligne introuvable dans {src_fp.name}: {stripped_line[:80]}...", file=sys.stderr)
        return 1
    
    new_content = '\n'.join(new_lines)
    n = count_data_rows(new_content)
    new_content = update_header_n(new_content, n)
    
    if dry_run:
        print(f"  Enlèverait de {src_fp.name}: {stripped_line[:80]}...", file=sys.stderr)
    else:
        write_file(src_fp, new_content)
        print(f"  Supprimé de {src_fp.name}: {stripped_line[:80]}...", file=sys.stderr)
    
    # Add to destination
    if not dry_run:
        dst_content = ensure_file(dst_fp)
        
        # Check duplicate (normalisé)
        already = False
        for line in dst_content.split('\n'):
            if normalize_line(line) == norm_line:
                already = True
                break
        
        if already:
            print(f"  ⏭️  Déjà présent dans {dst_fp.name}, pas de doublon créé", file=sys.stderr)
        else:
            dst_content = dst_content.rstrip('\n') + '\n' + stripped_line + '\n'
            dn = count_data_rows(dst_content)
            dst_content = update_header_n(dst_content, dn)
            write_file(dst_fp, dst_content)
            print(f"  Ajouté dans {dst_fp.name}: {stripped_line[:80]}...", file=sys.stderr)
    else:
        print(f"  Ajouterait dans {dst_fp.name}: {stripped_line[:80]}...", file=sys.stderr)
    
    return 0


def cmd_check(target=None, verbose=False):
    """Vérifier que l'en-tête correspond au nombre réel de lignes de données."""
    results = []
    
    if target and target != '--all':
        fp = CHRONIQUES_DIR / parse_file_ref(target)
        if not fp.exists():
            print(f"  ❌ Fichier introuvable: {fp}", file=sys.stderr)
            return 1
        files_to_check = [fp]
    else:
        # Check all year/*.md files + plages_annees.md
        files_to_check = sorted(CHRONIQUES_DIR.rglob('*.md'))
        files_to_check = [f for f in files_to_check if f.name != 'README.md' and 'PROTOCOLE' not in f.name]
    
    errors = 0
    for fp in files_to_check:
        content = read_file(fp)
        header_match = re.search(r'> (\d+) (événement|evenement)', content)
        header_n = int(header_match.group(1)) if header_match else -1
        data_n = count_data_rows(content)
        
        ok = header_n == data_n
        if not ok:
            errors += 1
        
        rel = fp.relative_to(CHRONIQUES_DIR)
        if not ok or verbose:
            status = '✅' if ok else '❌'
            print(f'{status} {rel}: header={header_n}, data={data_n}')
    
    if not verbose and errors == 0:
        total = len(files_to_check)
        print(f'  ✅ {total} fichiers vérifiés, tout OK')
    
    if errors > 0:
        print(f'  ⚠️  {errors} fichier(s) avec compteur décalé', file=sys.stderr)
        return 1
    
    return 0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = [a for a in sys.argv[1:]]
    
    if '--help' in args or '-h' in args or not args:
        print(__doc__)
        return 0
    
    dry_run = '--dry-run' in args
    args = [a for a in args if a != '--dry-run']
    
    # --check [file | --all]
    if '--check' in args:
        idx = args.index('--check')
        target = args[idx + 1] if idx + 1 < len(args) and not args[idx + 1].startswith('--') else None
        verbose = '--verbose' in args or '-v' in args
        return cmd_check(target, verbose)
    
    # --remove <file> <line>
    if '--remove' in args:
        idx = args.index('--remove')
        rest = args[idx + 1:]
        if len(rest) < 2:
            print("Usage: enrich_chronique.py --remove <fichier> <ligne>", file=sys.stderr)
            return 1
        file_ref = rest[0]
        line = ' '.join(rest[1:]) if len(rest) > 2 else rest[1]
        return cmd_remove(parse_file_ref(file_ref), line, dry_run)
    
    # --split <file> <old_line> <new_line1> [<new_line2> ...]
    if '--split' in args:
        idx = args.index('--split')
        rest = args[idx + 1:]
        if len(rest) < 3:
            print("Usage: enrich_chronique.py --split <fichier> <ancienne_ligne> <nouvelles_lignes...>", file=sys.stderr)
            return 1
        file_ref = rest[0]
        old_line = rest[1]
        new_lines = rest[2:]
        return cmd_split(parse_file_ref(file_ref), old_line, new_lines, dry_run)
    
    # --move <src> <dst> <line>
    if '--move' in args:
        idx = args.index('--move')
        rest = args[idx + 1:]
        if len(rest) < 3:
            print("Usage: enrich_chronique.py --move <source> <destination> <ligne>", file=sys.stderr)
            return 1
        src_ref = rest[0]
        dst_ref = rest[1]
        line = ' '.join(rest[2:]) if len(rest) > 3 else rest[2]
        return cmd_move(parse_file_ref(src_ref), parse_file_ref(dst_ref), line, dry_run)
    
    # Default: add facts (existing behavior)
    stdin_mode = '--stdin' in args
    args = [a for a in args if a != '--stdin']
    
    if stdin_mode:
        facts = [line for line in sys.stdin.read().split('\n') if line.strip()]
        if len(facts) < 2:
            print("Erreur: stdin doit contenir fichier + faits (1 ligne = fichier, suivantes = faits)", file=sys.stderr)
            return 1
        file_ref = facts[0]
        lines = facts[1:]
    else:
        file_ref = args[0]
        lines = args[1:]
    
    result = cmd_add(parse_file_ref(file_ref), lines, dry_run)
    return 0 if result >= 0 else result


if __name__ == '__main__':
    sys.exit(main())
