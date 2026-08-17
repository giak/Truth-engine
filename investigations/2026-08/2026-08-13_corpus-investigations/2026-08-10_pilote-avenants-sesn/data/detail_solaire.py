#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Detail des marches SOLAIRES >= 1 MEUR : distinguer parcs au sol vs
ombrieres/toitures, et lister les acheteurs."""
import csv

rows = list(csv.DictReader(open('/tmp/enr_angle_a/decp_enr_big.csv',
                                encoding='utf-8')))
sol = [r for r in rows if any(k in (r['objet'] or '').lower()
                              for k in ['photovolta', 'centrale solaire',
                                        'parc solaire', 'solaire']) and
       not any(k in (r['objet'] or '').lower()
               for k in ['eolien', 'eolienne'])]
sol.sort(key=lambda r: -float(r['montant'] or 0))
print('marches solaires >= 1 MEUR:', len(sol))
for r in sol:
    obj = (r['objet'] or '')
    print('- %.0f | ach=%s | %s' % (float(r['montant'] or 0),
                                    r['acheteur_id'], obj[:140]))
