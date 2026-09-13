#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, sys
root = Path(__file__).resolve().parent
required = {
    'ARTICLE_PUBLICATION_VIEW.md','FOUNDATION/VISION.md','FOUNDATION/PFD.md',
    'SOURCE_INDEX.tsv','AUDIT_PROMPT.md','START_HERE.md','AUDIT_TARGET.json',
    'MANIFEST.tsv','SHA256SUMS.txt'
}
files={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()}
missing=sorted(required-files)
forbidden=['ARTICLE_PROTOCOL.md','STATE.json','TRACEABILITY_GRAPH.tsv','REPAIR_LOG','A5_S01','A5_S02','A7_S03','SUPPORT_MAP']
bad=[f for f in files if any(x.lower() in f.lower() for x in forbidden)]
target=json.loads((root/'AUDIT_TARGET.json').read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
checks=[
 ('product_sha',sha(root/'ARTICLE_PUBLICATION_VIEW.md')==target['product_sha256']),
 ('vision_sha',sha(root/'FOUNDATION/VISION.md')==target['vision_sha256']),
 ('pfd_sha',sha(root/'FOUNDATION/PFD.md')==target['pfd_sha256']),
 ('footnotes',target['footnote_definitions']==13),
 ('no_implementation_history',target['implementation_history_included'] is False and not bad),
 ('required_present',not missing),
]
print('A7-S04 COLD PRODUCT HANDOFF — INGÉRENCES')
for n,v in checks: print(('PASS' if v else 'FAIL'),n)
if bad: print('FORBIDDEN:',bad)
if missing: print('MISSING:',missing)
sys.exit(1 if any(not v for _,v in checks) else 0)
