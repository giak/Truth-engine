#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifier les champs de date presents dans les records SDEM/SOREGIES."""
import json

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
    print('=== %s ===' % t)
    r0 = recs[0]
    print('cles du premier record:', sorted(r0.keys()))
    # lister tous les champs contenant date
    date_keys = set()
    for r in recs:
        for k in r.keys():
            if 'date' in k.lower() or 'delai' in k.lower():
                date_keys.add(k)
    print('champs date/delai:', sorted(date_keys))
    for k in sorted(date_keys):
        vals = [r.get(k) for r in recs if r.get(k)]
        print('  %s : %d renseignes, exemples %s' % (k, len(vals), vals[:3]))
