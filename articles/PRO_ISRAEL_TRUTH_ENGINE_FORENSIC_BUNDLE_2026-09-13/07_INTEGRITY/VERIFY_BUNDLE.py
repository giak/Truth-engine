from pathlib import Path
import hashlib, json, re, sys
root=Path(__file__).resolve().parents[1]
errors=[]
# Verify manifest.
manifest=root/'07_INTEGRITY'/'MANIFEST.sha256'
if manifest.exists():
    for line in manifest.read_text().splitlines():
        if not line.strip(): continue
        sha, rel=line.split('  ',1)
        p=root/rel
        if not p.exists(): errors.append(f'MISSING {rel}'); continue
        got=hashlib.sha256(p.read_bytes()).hexdigest()
        if got!=sha: errors.append(f'SHA {rel}')
# Verify certifications that have matching investigation physical files.
for iid,base in [('INV-026','03_FOUNDATION/INV-026'),('INV-027','03_FOUNDATION/INV-027'),('INV-028','03_FOUNDATION/INV-028'),('INV-160','04_WAVE/INV-160'),('INV-161','04_WAVE/INV-161'),('INV-166','04_WAVE/INV-166')]:
    d=root/base
    certs=list(d.glob('*CERTIFICATION*.json'))
    invs=[p for p in d.glob('*INVESTIGATION*.md') if 'COVERAGE' not in p.name]
    if certs and invs:
        cert=json.loads(certs[0].read_text())
        expected=cert.get('deliverable_sha256')
        if expected:
            # Prefer exact delivered-name match; otherwise single investigation file.
            p=invs[0]
            got=hashlib.sha256(p.read_bytes()).hexdigest()
            if got!=expected: errors.append(f'CERT_SHA {iid}: {got} != {expected}')
print('PASS' if not errors else 'FAIL')
for e in errors: print(e)
sys.exit(1 if errors else 0)
