#!/usr/bin/env python3
"""Merge SUPPLEMENT_ARTICLES_DENSES_2.md events into HYPER_MATRICE_UNIFIEE.md.

Preserves exact original formatting for existing rows.
Inserts new events in sorted order (by dimension then description).
Recalculates all metadata tables from scratch.
"""

import re, os, shutil, copy
from collections import defaultdict, Counter
from datetime import datetime

BASE = "investigations/2026-06-25_fresque_systemique/01_donnees"
MATRIX_PATH = f"{BASE}/2026-06-25_17-00_france_1975-2026_HYPER_MATRICE_UNIFIEE.md"
SUPP_PATH = f"{BASE}/2026-06-25_23-59_SUPPLEMENT_ARTICLES_DENSES_2.md"
BACKUP_PATH = MATRIX_PATH.replace("_UNIFIEE.md", "_UNIFIEE_BACKUP_BEFORE_MERGE_DENSES2.md")

# ---- HELPERS ----

DIMS = ['POL', 'ÉCO', 'SOC', 'JUR', 'SANT', 'ÉDU', 'AGR', 'ENV', 'TEC', 'CUL',
        'IMM', 'SPO', 'REL', 'DÉMO', 'TRA', 'MIL', 'SCI', 'DIP', 'MÉD', 'TER']
DIM_SET = set(DIMS)
CODES = {'✅', '⚠', '❌', '💀'}

def normalize_code(c):
    """Remove variation selector-16 from emoji."""
    return c.replace('\ufe0f', '')

def word_tokens(s):
    """Tokenize description into lowercase words."""
    return set(re.findall(r'\w+', s.lower()))

def jaccard_sim(a, b):
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0

def get_base_year(year_key):
    """Extract base year from a year key (e.g., '2024-06' -> 2024, '2001-2009' -> 2001)."""
    m = re.match(r'^(\d{4})', str(year_key))
    return int(m.group(1)) if m else 0

def parse_event(line):
    """Parse a matrix table row into (year_key, dim, desc, code) or None."""
    parts = [p.strip() for p in line.split('|')]
    if len(parts) < 5:
        return None
    year_key = parts[1]
    if year_key in ('Année', '---', ''):
        return None
    dim = parts[2]
    if dim not in DIM_SET:
        return None
    desc = parts[3].rstrip('|').strip()
    code = normalize_code(parts[4].strip())
    if code not in CODES:
        return None
    return (year_key, dim, desc, code)

def format_event(year_key, dim, desc, code):
    return f'| {year_key} | {dim} | {desc} | {code} |'

# ---- PARSE SUPPLEMENT ----
print("📖 Parsing supplement...")
supp_events = []
for line in open(SUPP_PATH):
    line = line.strip()
    if not line.startswith('|') or '|' not in line[1:]:
        continue
    ev = parse_event(line)
    if ev:
        supp_events.append(ev)

print(f"   Found {len(supp_events)} events in supplement")

# Count by year
year_counts = Counter(get_base_year(e[0]) for e in supp_events)
print(f"   Year distribution: {dict(sorted(year_counts.items()))}")

# ---- PARSE MATRIX ----
print("📖 Parsing matrix...")
with open(MATRIX_PATH) as f:
    matrix_lines = f.readlines()

# Find the boundary between header and year sections
# Header ends at the line before '### 1975'
header_end = None
for i, line in enumerate(matrix_lines):
    if line.strip().startswith('### ') and re.match(r'^### \d{4}', line.strip()):
        header_end = i
        break

if header_end is None:
    print("❌ Could not find year sections in matrix!")
    exit(1)

print(f"   Header ends at line {header_end}, year sections start at line {header_end}")

# Parse year sections
# Each section: ### YEAR (possibly with blank lines before)
# Then optional blank line
# Then table: | Année | Dimension | Description | Code |
# Then separator: |---|---|---|---|
# Then data rows
# Then blank line(s) before next ### YEAR (or end of file)

class YearSection:
    def __init__(self, year_key, start_line):
        self.year_key = year_key  # e.g., '1975'
        self.start_line = start_line
        self.end_line = None
        self.header_line = None  # line index of | Année |...
        self.sep_line = None     # line index of |---|---|---|---|
        self.data_start = None   # first data row line index
        self.data_end = None     # last data row line index (inclusive)
        self.events = []         # list of (year_key, dim, desc, code)

# Find all year section boundaries
sections = []
current = None
in_table = False

for i, line in enumerate(matrix_lines):
    stripped = line.strip()
    
    # Detect section start
    m = re.match(r'^### (\d{4})$', stripped)
    if m:
        current = YearSection(m.group(1), i)
        sections.append(current)
        in_table = False
        continue
    
    if current is None:
        continue
    
    # Detect table header
    if stripped == '| Année | Dimension | Description | Code |':
        current.header_line = i
        in_table = True
        continue
    
    # Detect separator
    if stripped == '|---|---|---|---|':
        current.sep_line = i
        current.data_start = i + 1
        continue
    
    # Detect next section or end of content
    if stripped.startswith('### ') and re.match(r'^### \d{4}', stripped) and current:
        current.end_line = i
        in_table = False
        current = None
        continue

# Set end_line for last section
if sections:
    sections[-1].end_line = len(matrix_lines)

print(f"   Found {len(sections)} year sections: {[s.year_key for s in sections]}")

# Parse events from each section
existing_events = {}  # (year_key, dim, desc) -> True
section_events = defaultdict(list)  # year_key -> list of (year_key, dim, desc, code, line_idx)

for sec in sections:
    for i in range(sec.data_start, sec.end_line if sec.end_line else len(matrix_lines)):
        line = matrix_lines[i].strip()
        if not line or line.startswith('### ') or line.startswith('| Année') or line.startswith('|---|---'):
            continue
        ev = parse_event(line)
        if ev:
            key = (ev[0], ev[1], ev[2])
            existing_events[key] = True
            section_events[sec.year_key].append((ev[0], ev[1], ev[2], ev[3], i))

print(f"   Total existing events in matrix: {len(existing_events)}")

# ---- DEDUPLICATE ----
print("🔍 Deduplicating...")
events_to_add = []
dup_exact = 0
dup_similar = 0

for ev in supp_events:
    year_key, dim, desc, code = ev
    base_year = str(get_base_year(year_key))
    key = (year_key, dim, desc)
    
    # Exact duplicate?
    if key in existing_events:
        dup_exact += 1
        continue
    
    # Similar duplicate? (same base_year, same dim, Jaccard > 0.7)
    # Note: we match on base_year only (not full year_key) so that
    # '2024-06' events can be matched against existing '2024' events
    tokens = word_tokens(desc)
    found_similar = False
    for ex_ev in section_events.get(base_year, []):
        if ex_ev[1] == dim:
            if jaccard_sim(tokens, word_tokens(ex_ev[2])) > 0.7:
                dup_similar += 1
                found_similar = True
                break
    
    if not found_similar:
        events_to_add.append(ev)

print(f"   Exact duplicates skipped: {dup_exact}")
print(f"   Similar duplicates skipped: {dup_similar}")
print(f"   New events to add: {len(events_to_add)}")

if not events_to_add:
    print("✅ Nothing to add. Exiting.")
    exit(0)

# ---- BUILD NEW MATRIX ----
print("📝 Building updated matrix...")

# Group new events by their base year
new_by_year = defaultdict(list)
for ev in events_to_add:
    base_year = str(get_base_year(ev[0]))
    new_by_year[base_year].append(ev)

# Sort events within each year by dimension then description
for yr in new_by_year:
    new_by_year[yr].sort(key=lambda e: (DIMS.index(e[1]) if e[1] in DIMS else 99, e[2]))

# Create a set of year sections that need updating
years_with_new = set(new_by_year.keys())

# Check if we need to create new sections for years not in matrix
all_matrix_years = set(s.year_key for s in sections)
new_years_needed = years_with_new - all_matrix_years
print(f"   New year sections needed: {sorted(new_years_needed) if new_years_needed else 'None'}")

# Build new content: header + year sections
new_lines = []

# Copy header as-is
new_lines.extend(matrix_lines[:sections[0].start_line])

# Process each year section
existing_year_keys = [s.year_key for s in sections]

for sec in sections:
    yr = sec.year_key
    
    # Add section header
    new_lines.append(matrix_lines[sec.start_line])
    
    # Add blank line if present in original
    if sec.start_line + 1 < sec.header_line:
        # There's content between ### and table header (blank lines or other)
        pass  # We'll handle below
    
    # Collect existing events in this section
    existing = []
    for i in range(sec.data_start, sec.end_line if sec.end_line else len(matrix_lines)):
        line = matrix_lines[i].rstrip('\n')
        if not line.strip() or line.strip().startswith('### '):
            break  # empty line or next section
        ev = parse_event(line)
        if ev:
            existing.append((ev[0], ev[1], ev[2], ev[3], line.rstrip()))
    
    # Add blank line before table
    new_lines.append('\n')
    
    # Add table header
    new_lines.append('| Année | Dimension | Description | Code |\n')
    new_lines.append('|---|---|---|---|\n')
    
    # Merge existing + new events
    new_for_year = new_by_year.get(yr, [])
    
    # Create combined sorted list
    all_entries = []
    
    # Add existing
    for ev in existing:
        all_entries.append((ev[0], ev[1], ev[2], ev[3], ev[4]))
    
    # Add new
    for ev in new_for_year:
        all_entries.append((ev[0], ev[1], ev[2], ev[3], None))
    
    # Sort by dim index, then year_key, then description
    def sort_key(e):
        dim_idx = DIMS.index(e[1]) if e[1] in DIMS else 99
        return (dim_idx, e[0], e[2])
    
    all_entries.sort(key=sort_key)
    
    # Write entries, keeping original line formatting for existing
    for entry in all_entries:
        if entry[4] is not None:
            # Original line - preserve exact formatting
            new_lines.append(entry[4] + '\n')
        else:
            # New event - format it
            new_lines.append(format_event(entry[0], entry[1], entry[2], entry[3]) + '\n')
    
    # Add one blank line between sections
    if sec != sections[-1]:
        new_lines.append('\n')

# Add new year sections (for years beyond 2026 like 2030)
for new_yr in sorted(new_years_needed, key=int):
    new_lines.append(f'### {new_yr}\n')
    new_lines.append('\n')
    new_lines.append('| Année | Dimension | Description | Code |\n')
    new_lines.append('|---|---|---|---|\n')
    
    for ev in new_by_year[new_yr]:
        new_lines.append(format_event(ev[0], ev[1], ev[2], ev[3]) + '\n')
    new_lines.append('\n')

# ---- RECALCULATE METADATA ----
print("📊 Recalculating metadata...")

# Parse all events from new_lines to get definitive counts
all_events = []
for line in new_lines:
    ev = parse_event(line.strip())
    if ev:
        all_events.append(ev)

total_events = len(all_events)
print(f"   Total events in new matrix: {total_events}")

# Decade breakdown
decades = [
    (1975, 1982, "1975-1982"),
    (1983, 1990, "1983-1990"),
    (1991, 1998, "1991-1998"),
    (1999, 2006, "1999-2006"),
    (2007, 2016, "2007-2016"),
    (2017, 2026, "2017-2026"),
]

def year_sort_key(ev):
    base = get_base_year(ev[0])
    # Handle precise dates to sort within year
    return base

# Count by decade and dimension
decade_counts = []
for start, end, label in decades:
    dim_counts = Counter()
    for ev in all_events:
        base = get_base_year(ev[0])
        if start <= base <= end:
            dim_counts[ev[1]] += 1
    row = [label]
    for dim in DIMS:
        row.append(dim_counts[dim])
    row.append(sum(dim_counts.values()))
    decade_counts.append(row)

# Total row
total_row = ["**TOTAL**"]
for dim in DIMS:
    total_row.append(sum(decade_counts[i][DIMS.index(dim)+1] for i in range(len(decades))))
total_row.append(total_events)

# Dimension summary
dim_summary = defaultdict(lambda: Counter())
for ev in all_events:
    dim_summary[ev[1]][ev[3]] += 1

dim_rows = []
for dim in DIMS:
    c = dim_summary[dim]
    dim_rows.append({
        'dim': dim,
        'total': sum(c.values()),
        'ok': c['✅'],
        'warn': c['⚠'],
        'bad': c['❌'],
        'death': c['💀']
    })

# Code impact summary
code_total = Counter(ev[3] for ev in all_events)
total_all_codes = sum(code_total.values())

# Top years
year_primary_subject = {}
year_event_counts = Counter()
for ev in all_events:
    base_year = get_base_year(ev[0])
    year_event_counts[base_year] += 1

# Find primary subject per year
year_dim_counts = defaultdict(lambda: Counter())
for ev in all_events:
    base_year = get_base_year(ev[0])
    year_dim_counts[base_year][ev[1]] += 1

for yr in year_dim_counts:
    dim_counter = year_dim_counts[yr]
    max_count = max(dim_counter.values())
    primary_dims = [d for d, c in dim_counter.items() if c == max_count]
    year_primary_subject[yr] = primary_dims[0] if primary_dims else 'N/A'

# ---- UPDATE HEADER ----
print("📝 Updating header with new metadata...")

# Find the header section boundaries
meta_data_end = None
synth_dec_start = None
synth_dec_end = None
synth_dim_start = None
synth_dim_end = None
synth_code_start = None
synth_code_end = None
classement_start = None
classement_end = None

for i, line in enumerate(new_lines):
    stripped = line.strip()
    if stripped == '## MÉTA-DONNÉES':
        meta_data_start = i
    elif stripped == '## SYNTHÈSE PAR DÉCENNIE':
        synth_dec_start = i
    elif stripped == '## SYNTHÈSE PAR DIMENSION (toutes années)':
        synth_dim_start = i
    elif stripped == '## SYNTHÈSE PAR CODE D\'IMPACT':
        synth_code_start = i
    elif stripped == '## CLASSEMENT DES ANNÉES LES PLUS CHARGÉES':
        classement_start = i
    elif stripped.startswith('### 1975'):
        # boundary where year data starts
        pass

# Find actual section boundaries
sections_to_find = [
    ('meta', '## MÉTA-DONNÉES', '## SYNTHÈSE PAR DÉCENNIE'),
    ('synth_dec', '## SYNTHÈSE PAR DÉCENNIE', '## SYNTHÈSE PAR DIMENSION'),
    ('synth_dim', '## SYNTHÈSE PAR DIMENSION (toutes années)', '## SYNTHÈSE PAR CODE D\'IMPACT'),
    ('synth_code', '## SYNTHÈSE PAR CODE D\'IMPACT', '## CLASSEMENT DES ANNÉES LES PLUS CHARGÉES'),
    ('classement', '## CLASSEMENT DES ANNÉES LES PLUS CHARGÉES', '### 1975'),
]

section_bounds = {}
for name, start_marker, end_marker_prefix in sections_to_find:
    start_idx = None
    end_idx = None
    for i, line in enumerate(new_lines):
        if line.strip() == start_marker:
            start_idx = i
        if start_idx is not None and line.strip().startswith(end_marker_prefix) and i > start_idx:
            end_idx = i
            break
    if start_idx is not None and end_idx is None:
        end_idx = len(new_lines)  # until next marker
    section_bounds[name] = (start_idx, end_idx)

# ---- Build new header ----
header_lines = []

# Title section (before ## MÉTA-DONNÉES)
header_lines.append('# HYPER-MATRICE FRANCE 1975-2026\n')
header_lines.append('# Faits atomiques — Analyse systémique\n')
header_lines.append('\n')

# MÉTA-DONNÉES
header_lines.append('## MÉTA-DONNÉES\n')
header_lines.append(f'- Période : 1975-2026 (52 ans)\n')
header_lines.append(f'- Nombre total d\'événements : {total_events}\n')
header_lines.append(f'- Dimensions couvertes : {len(DIMS)}\n')
header_lines.append(f'- Date de génération : 2026-06-25\n')
header_lines.append('\n')

# SYNTHÈSE PAR DÉCENNIE
header_lines.append('## SYNTHÈSE PAR DÉCENNIE\n')
header_cols = '| Décennie | ' + ' | '.join(DIMS) + ' | TOTAL |\n'
header_lines.append(header_cols)
sep_cols = '|' + '---|' * (len(DIMS) + 2) + '\n'
header_lines.append(sep_cols)
for row in decade_counts:
    row_str = '| ' + ' | '.join(str(x) for x in row) + ' |\n'
    header_lines.append(row_str)
# Total row
total_row_str = '| ' + ' | '.join(str(x) for x in total_row) + ' |\n'
header_lines.append(total_row_str)
header_lines.append('\n')

# SYNTHÈSE PAR DIMENSION
header_lines.append('## SYNTHÈSE PAR DIMENSION (toutes années)\n')
header_lines.append('| Dimension | Total | ✅ | ⚠️ | ❌ | 💀 |\n')
header_lines.append('|---|---|---|---|---|---|\n')
for r in dim_rows:
    header_lines.append(f'| {r["dim"]} | {r["total"]} | {r["ok"]} | {r["warn"]} | {r["bad"]} | {r["death"]} |\n')
header_lines.append('\n')

# SYNTHÈSE PAR CODE D'IMPACT
header_lines.append('## SYNTHÈSE PAR CODE D\'IMPACT\n')
header_lines.append('| Code | Total | % |\n')
header_lines.append('|---|---|---|\n')
for code in ['✅', '⚠', '❌', '💀']:
    cnt = code_total[code]
    pct = round(cnt / total_all_codes * 100, 1) if total_all_codes else 0
    header_lines.append(f'| {code} | {cnt} | {pct}% |\n')
header_lines.append(f'| **TOTAL** | {total_all_codes} | 100% |\n')
header_lines.append('\n')

# CLASSEMENT DES ANNÉES LES PLUS CHARGÉES
header_lines.append('## CLASSEMENT DES ANNÉES LES PLUS CHARGÉES\n')
header_lines.append('| Rang | Année | Total | Principal sujet |\n')
header_lines.append('|---|---|---|---|\n')

# Sort years by event count descending, take top 30
sorted_years = sorted(year_event_counts.items(), key=lambda x: (-x[1], -x[0]))
# Filter to only include years within 1975-2026 range for ranking
sorted_years_ranked = [(yr, cnt) for yr, cnt in sorted_years if 1975 <= yr <= 2026]
for rank, (yr, cnt) in enumerate(sorted_years_ranked[:30], 1):
    subject = year_primary_subject.get(yr, 'N/A')
    header_lines.append(f'| {rank} | {yr} | {cnt} | {subject} |\n')
header_lines.append('\n')

# ---- Replace header in new_lines ----
# Find the span from beginning to ### 1975
first_year_idx = None
for i, line in enumerate(new_lines):
    if line.strip().startswith('### ') and re.match(r'^### \d{4}', line.strip()):
        first_year_idx = i
        break

# Replace everything before first year section with new header
new_matrix = header_lines + new_lines[first_year_idx:]

# ---- WRITE ----
print(f"💾 Writing updated matrix ({len(new_matrix)} lines)...")
with open(MATRIX_PATH, 'w') as f:
    f.writelines(new_matrix)

# ---- VERIFY ----
print("\n🔍 Verification...")

# Parse final matrix
final_events = []
for line in new_matrix:
    ev = parse_event(line.strip())
    if ev:
        final_events.append(ev)

print(f"   Final event count: {len(final_events)}")
print(f"   Increase: {len(final_events) - 4861} (from original 4861)")

# Check by year
final_year_counts = Counter(get_base_year(e[0]) for e in final_events)
added_years = set()
for yr in sorted(new_by_year.keys(), key=int):
    before = year_event_counts.get(int(yr), 0)
    after = final_year_counts.get(int(yr), 0)
    added = after - before
    if added > 0:
        added_years.add(yr)
        print(f"   {yr}: +{added} events (now {after})")

# Check dims
final_dim_counts = Counter(e[1] for e in final_events)
print("   Dimensions:")
for dim in sorted(final_dim_counts.keys()):
    print(f"      {dim}: {final_dim_counts[dim]}")

# Check codes
final_code_counts = Counter(e[3] for e in final_events)
print("   Codes:")
for code in ['✅', '⚠', '❌', '💀']:
    print(f"      {code}: {final_code_counts[code]}")

print("\n✅ Merge complete!")
print(f"📁 Backup saved to: {BACKUP_PATH}")
print(f"📁 Updated matrix: {MATRIX_PATH}")
