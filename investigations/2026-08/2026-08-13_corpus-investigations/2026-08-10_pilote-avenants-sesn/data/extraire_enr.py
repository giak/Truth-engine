#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extraction des marches ENR (eolien/solaire) du DECP global.
Structure du fichier : {"marches": {"marche": [ {obj}, {obj}, ... ]}}
Un objet par ligne, certaines lignes se terminent par une virgule.
Sortie : /tmp/enr_angle_a/decp_enr_big.csv (dedup >= 1 MEUR) + stats.
"""
import json
import csv
import re
from collections import Counter

f = 'data/decp-global.json'
kw = ['eolien', 'eolienne', 'photovolta', 'centrale solaire', 'parc solaire',
      'ferme eolienne', 'aerogenerateur', 'aerogener', 'eoliennes']

records = []
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
        # retirer une virgule terminale si presente
        if s.endswith(','):
            s = s[:-1]
        try:
            obj = json.loads(s)
            parsed += 1
        except Exception:
            continue
        if not isinstance(obj, dict):
            continue
        low = (obj.get('objet') or '').lower()
        if any(k in low for k in kw):
            records.append(obj)

print('lignes JSON parsees:', parsed)
print('records ENR (objet):', len(records))

natures = Counter(r.get('nature', '?') for r in records)
print('natures:', dict(natures))

av = [r for r in records if 'avenant' in str(r.get('nature', '')).lower()]
print('avenants:', len(av))

big = [r for r in records if (r.get('montant') or 0) >= 1000000]
print('>= 1 MEUR:', len(big))


def norm(s):
    return re.sub(r'[^a-z0-9]', '', str(s).lower())[:120]


seen = set()
dedup = []
for r in sorted(big, key=lambda r: -(r.get('montant') or 0)):
    key = (norm(r.get('objet')), norm(r.get('acheteur', {}).get('id', '')),
           r.get('montant'))
    if key in seen:
        continue
    seen.add(key)
    dedup.append(r)
print('dedup >= 1 MEUR:', len(dedup))

with open('/tmp/enr_angle_a/decp_enr_big.csv', 'w', newline='',
          encoding='utf-8') as out:
    w = csv.writer(out)
    w.writerow(['id', 'nature', 'objet', 'montant', 'acheteur_id',
                'acheteur_nom', 'titulaires', 'codeCPV', 'date_notification',
                'source'])
    for r in dedup:
        ach = r.get('acheteur') or {}
        tits = ';'.join(str(t.get('id', '')) for t in (r.get('titulaires') or []))
        w.writerow([r.get('id', ''), r.get('nature', ''),
                    (r.get('objet') or '')[:200], r.get('montant'),
                    ach.get('id', ''), ach.get('nom', ''), tits,
                    r.get('codeCPV', ''), r.get('date_notification', ''),
                    r.get('source', '')])
print('CSV ecrit: /tmp/enr_angle_a/decp_enr_big.csv')

for r in dedup[:12]:
    print("- %.0f | %s | %s" % (r.get('montant') or 0, r.get('nature', '?'),
                                (r.get('objet') or '')[:90]))
