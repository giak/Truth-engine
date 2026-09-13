#!/usr/bin/env python3
from pathlib import Path
import csv, hashlib, sys
root=Path(__file__).resolve().parent
manifest=root/'MANIFEST_SHA256.csv'
fail=[]
with manifest.open(encoding='utf-8',newline='') as f:
    for r in csv.DictReader(f):
        p=root/r['path']
        if not p.exists(): fail.append((r['path'],'MISSING')); continue
        h=hashlib.sha256(p.read_bytes()).hexdigest()
        if h!=r['sha256']: fail.append((r['path'],'SHA_MISMATCH'))
if fail:
    print('FAIL',*fail,sep='\n'); sys.exit(1)
print('PASS: manifest verified')
