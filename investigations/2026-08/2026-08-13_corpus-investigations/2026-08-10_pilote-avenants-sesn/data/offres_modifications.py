#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extraire offresRecues et modifications (avenants) des records
SDEM/SOREGIES, focus sur les marches PV."""
import json
import re
from collections import Counter

TARGETS = {'255601106': 'SDEM', '450889225': 'SOREGIES'}
f = 'data/decp-global.json'
records = {k: [] for k in TARGETS}

with open(f, encoding='utf-8', errors='ignore') as fh:
    for line in fh:
        s = line.strip()
        if not s or s in ('{', '}', ']', ']},', '}]}'):
            continue
        if s == '"marches": {':
            continue
        if not s.startswith('{'):
            continue
        if s.endswith(','):
            s = s[:-1]
        try:
            obj = json.loads(s)
        except Exception:
            continue
        if not isinstance(obj, dict):
            continue
        ach = obj.get('acheteur') or {}
        aid = str(ach.get('id', ''))
        for target in TARGETS:
            if aid.startswith(target):
                records[target].append(obj)
                break

for t, recs in records.items():
    print('\n========== %s ==========' % t)
    # offresRecues : renseigne ?
    off = [r for r in recs if r.get('offresRecues') is not None]
    print('offresRecues renseignes:', len(off), '/', len(recs))
    c = Counter(str(r.get('offresRecues')) for r in recs if r.get('offresRecues') is not None)
    print('distribution offresRecues:', dict(c))

    # modifications (avenants)
    mod = [r for r in recs if r.get('modifications')]
    print('records avec modifications:', len(mod))
    for r in mod[:10]:
        print('- id=%s | %s' % (r.get('id'), json.dumps(r.get('modifications'), ensure_ascii=False)[:400]))

    # PV focus
    pv = [r for r in recs if 'photovolta' in (r.get('objet') or '').lower()]
    print('\n-- PV : %d marches --' % len(pv))
    off_pv = [r for r in pv if r.get('offresRecues') is not None]
    print('PV avec offresRecues:', len(off_pv))
    for r in off_pv:
        print('- id=%s | offres=%s | montant=%s | %s' % (
            r.get('id'), r.get('offresRecues'), r.get('montant'),
            (r.get('objet') or '')[:90]))
    mod_pv = [r for r in pv if r.get('modifications')]
    print('PV avec modifications:', len(mod_pv))
