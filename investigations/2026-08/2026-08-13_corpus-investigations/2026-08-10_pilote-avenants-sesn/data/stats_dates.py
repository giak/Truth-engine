#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stats dates/sources sur le CSV detail SDEM/SOREGIES."""
import csv
from collections import Counter

rows = list(csv.DictReader(open('/tmp/enr_angle_a/sdem_soregies_detail.csv',
                                encoding='utf-8')))
print('total lignes:', len(rows))
print('sources:', dict(Counter(r['source'] for r in rows)))

dates = [r['date_publication'] for r in rows if r['date_publication']]
print('dates renseignees:', len(dates), 'sur', len(rows))
d2 = sorted(dates)
print('plage:', d2[0], '->', d2[-1] if d2 else '-')

natures = Counter(r['nature'] for r in rows)
print('natures:', dict(natures))

procs = Counter(r['procedure'] for r in rows)
print('procedures:', dict(procs))

# avenants potentiels : objets contenant avenant/modificatif
av = [r for r in rows if any(k in (r['objet'] or '').lower()
                             for k in ['avenant', 'modificat', 'revision'])]
print('objets avec avenant/modificat/revision:', len(av))

# montants du SDEM (acheteur) par plage
for ach in ['SDEM', 'SOREGIES']:
    sub = [r for r in rows if r['acheteur'] == ach]
    print('\n===', ach, ':', len(sub), 'lignes ===')
    total = sum(float(r['montant'] or 0) for r in sub)
    print('total brut: %.0f EUR' % total)
    real = [r for r in sub if (float(r['montant'] or 0) < 100000000)]
    print('hors montants >= 100 MEUR:', len(real),
          'total %.0f EUR' % sum(float(r['montant'] or 0) for r in real))
