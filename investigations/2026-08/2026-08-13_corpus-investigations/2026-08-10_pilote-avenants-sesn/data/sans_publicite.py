#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lister les marches passes sans publicite ni mise en concurrence
(SDEM : 3, signal de la grille corruption_brainstorm §6)."""
import json

f = 'data/decp-global.json'
TARGETS = {'255601106': 'SDEM', '450889225': 'SOREGIES'}
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
    sp = [r for r in recs if 'sans publicit' in (r.get('procedure') or '').lower()
          or 'sans publicité' in (r.get('procedure') or '').lower()]
    print('=== %s : marches sans publicite (%d) ===' % (t, len(sp)))
    for r in sp:
        print('- id=%s | montant=%.0f | date=%s | %s' % (
            r.get('id'), r.get('montant') or 0, r.get('dateNotification'),
            (r.get('objet') or '')[:120]))
        tits = r.get('titulaires') or []
        for tt in tits:
            if isinstance(tt, dict):
                sub = tt.get('titulaire', tt)
                print('    titulaire:', sub.get('id', ''))
        print('    offres:', r.get('offresRecues'), '| duree:', r.get('dureeMois'))
