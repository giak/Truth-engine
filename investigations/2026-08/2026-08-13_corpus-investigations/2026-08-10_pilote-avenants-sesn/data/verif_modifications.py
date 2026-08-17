#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifier la structure des 'modifications' (avenants) SDEM :
le champ montant est-il un avenant unitaire ou un montant cumule ?
Compare avec le montant initial du marche."""
import json

f = 'data/decp-global.json'
target = '255601106'
recs = []
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
        if str(ach.get('id', '')).startswith(target):
            recs.append(obj)

# focus sur M2020-015 L3/L4 (grosses modifications)
for r in recs:
    mid = r.get('id', '')
    if '2020-015L3' in mid or '2020-015L4' in mid:
        print('=== id=%s ===' % mid)
        print('montant initial:', r.get('montant'))
        print('nature:', r.get('nature'))
        print('dateNotification:', r.get('dateNotification'))
        mods = r.get('modifications') or []
        print('nb modifications:', len(mods))
        for m in mods:
            mm = m.get('modification', m)
            print('  mod:', json.dumps(mm, ensure_ascii=False)[:300])
        print()
