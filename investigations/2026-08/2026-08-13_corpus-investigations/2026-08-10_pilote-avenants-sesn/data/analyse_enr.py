#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Analyse du CSV /tmp/enr_angle_a/decp_enr_big.csv :
- concentration par titulaire (>= 1 MEUR)
- marches eoliens vs solaires
- acheteurs les plus frequents
"""
import csv
from collections import Counter

rows = list(csv.DictReader(open('/tmp/enr_angle_a/decp_enr_big.csv',
                                encoding='utf-8')))
print('lignes:', len(rows))

# montant total
total = sum(float(r['montant'] or 0) for r in rows)
print('total >= 1 MEUR: %.0f EUR' % total)

# distinction eolien / solaire
eol = [r for r in rows if any(k in (r['objet'] or '').lower()
                              for k in ['eolien', 'eolienne', 'aerogener'])]
sol = [r for r in rows if any(k in (r['objet'] or '').lower()
                              for k in ['photovolta', 'centrale solaire',
                                        'parc solaire', 'solaire']) and
       not any(k in (r['objet'] or '').lower()
               for k in ['eolien', 'eolienne'])]
print('eolien:', len(eol), '| solaire:', len(sol))

# concentration par titulaire
tit = Counter()
for r in rows:
    for t in (r['titulaires'] or '').split(';'):
        if t:
            tit[t] += 1
print('=== top 10 titulaires (nb marches) ===')
for t, c in tit.most_common(10):
    print('-', t, ':', c)

# concentration par acheteur
ach = Counter(r['acheteur_id'] for r in rows)
print('=== top 10 acheteurs ===')
for a, c in ach.most_common(10):
    print('-', a, ':', c)

# montants par acheteur
ach_montant = Counter()
for r in rows:
    ach_montant[r['acheteur_id']] += float(r['montant'] or 0)
print('=== top 10 acheteurs par montant ===')
for a, m in ach_montant.most_common(10):
    print('-', a, ': %.0f EUR' % m)

# eoliens en detail
print('=== marches EOLIENS (>= 1 MEUR) ===')
for r in sorted(eol, key=lambda r: -float(r['montant'] or 0)):
    print('- %.0f | %s | ach=%s | %s' % (float(r['montant'] or 0),
                                         r['nature'], r['acheteur_id'],
                                         (r['objet'] or '')[:100]))
