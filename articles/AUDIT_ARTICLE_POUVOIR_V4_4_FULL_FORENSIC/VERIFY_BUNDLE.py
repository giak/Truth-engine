#!/usr/bin/env python3
from pathlib import Path
import hashlib,csv,re,sys
root=Path(__file__).resolve().parent
errors=[]
# required
required=[
 '01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md',
 '03_FORENSIC_INDEX/CORPUS_121_AUDIT.csv',
 '03_FORENSIC_INDEX/SOURCE_INDEX.csv',
 '03_FORENSIC_INDEX/RECONSTRUCTION_REPORT.md',
 '05_ALSTOM/INVESTIGATION_ALSTOM_GE_MACRON_2026-09-12.md',
]
for r in required:
    if not (root/r).exists(): errors.append('MISSING_REQUIRED '+r)
# article figure links
art=root/'01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md'
if art.exists():
    txt=art.read_text(encoding='utf-8')
    links=re.findall(r'!\[[^\]]*\]\((figures/[^)]+)\)',txt)
    if len(links)!=4: errors.append(f'FIGURE_LINK_COUNT {len(links)}')
    for l in links:
        if not (art.parent/l).exists(): errors.append('MISSING_FIGURE '+l)
# 113 physical corpus files
idx=root/'03_FORENSIC_INDEX/SOURCE_INDEX.csv'
if idx.exists():
    rows=list(csv.DictReader(idx.open(encoding='utf-8-sig')))
    if len(rows)!=113: errors.append(f'SOURCE_INDEX_ROWS {len(rows)}')
    names={p.name for p in (root/'10_A7_FULL_CORPUS').rglob('*') if p.is_file()}
    miss=[r['physical_source_file'] for r in rows if r['physical_source_file'] not in names]
    if miss: errors.append('MISSING_CORPUS_FILES '+','.join(miss))
# manifest (manifest intentionally excludes itself)
man=root/'MANIFEST.sha256'
if man.exists():
    for line in man.read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        h,rel=line.split('  ',1)
        p=root/rel
        if not p.exists(): errors.append('MANIFEST_MISSING '+rel); continue
        got=hashlib.sha256(p.read_bytes()).hexdigest()
        if got!=h: errors.append('SHA_MISMATCH '+rel)
else: errors.append('MISSING_MANIFEST')
if errors:
    print('FAIL')
    print('\n'.join(errors))
    sys.exit(1)
print('PASS')
print('article figures: 4/4')
print('forensic physical corpus: 113/113')
print('manifest: verified')
