#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NEXT-A1 : extraction complete des marches SDEM (255601106) et
SOREGIES (450889225) depuis decp-global.json.
Structure : {"marches": {"marche": [ {obj}, ... ]}}, un objet par ligne,
certaines lignes se terminent par une virgule.
"""
import json
import csv
from collections import Counter

TARGETS = {'255601106': 'SDEM', '450889225': 'SOREGIES'}
f = 'data/decp-global.json'

records = {k: [] for k in TARGETS}
parsed = 0
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
            parsed += 1
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

print('lignes JSON parsees:', parsed)
for t, recs in records.items():
    print('=== %s (%s) : %d marches ===' % (t, TARGETS[t], len(recs)))
    natures = Counter(r.get('nature', '?') for r in recs)
    print('  natures:', dict(natures))
    total = sum((r.get('montant') or 0) for r in recs)
    print('  total montants: %.0f EUR' % total)

# ecrire CSV detaille
with open('/tmp/enr_angle_a/sdem_soregies_detail.csv', 'w', newline='',
          encoding='utf-8') as out:
    w = csv.writer(out)
    w.writerow(['acheteur', 'id', 'objet', 'montant', 'procedure',
                'formePrix', 'codeCPV', 'dureeMois', 'date_notification',
                'date_publication', 'titulaires', 'source', 'nature',
                'origineUE', 'tauxAvance', 'ccag'])
    for t, recs in records.items():
        for r in recs:
            ach = r.get('acheteur') or {}
            tits = json.dumps(r.get('titulaires'), ensure_ascii=False)
            w.writerow([TARGETS[t], r.get('id', ''), (r.get('objet') or '')[:250],
                        r.get('montant'), r.get('procedure', ''),
                        r.get('formePrix', ''), r.get('codeCPV', ''),
                        r.get('dureeMois', ''), r.get('date_notification', ''),
                        r.get('date_publication', ''), tits, r.get('source', ''),
                        r.get('nature', ''), r.get('origineUE', ''),
                        r.get('tauxAvance', ''), r.get('ccag', '')])
print('CSV detail ecrit: /tmp/enr_angle_a/sdem_soregies_detail.csv')

# detail complet
for t, recs in records.items():
    print('\n=== DETAIL %s ===' % t)
    for r in sorted(recs, key=lambda r: -(r.get('montant') or 0)):
        ach = r.get('acheteur') or {}
        print('- id=%s | %.0f EUR | proc=%s | %s | src=%s' % (
            r.get('id'), r.get('montant') or 0, r.get('procedure', '?'),
            (r.get('objet') or '')[:110], r.get('source', '?')))
        print('  titulaires:', json.dumps(r.get('titulaires'), ensure_ascii=False)[:300])
        print('  duree=%s mois | date_notif=%s | CPV=%s' % (
            r.get('dureeMois', '?'), r.get('date_notification', '?'),
            r.get('codeCPV', '?')))
