#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Distribution des procedures SDEM/SOREGIES depuis le CSV detail."""
import csv
from collections import Counter

rows = list(csv.DictReader(open('/tmp/enr_angle_a/sdem_soregies_detail.csv',
                                encoding='utf-8')))
for ach in ['SDEM', 'SOREGIES']:
    sub = [r for r in rows if r['acheteur'] == ach]
    procs = Counter(r['procedure'] for r in sub)
    print('=== %s (%d marches) : procedures ===' % (ach, len(sub)))
    for p, c in procs.most_common():
        print('- %s : %d' % (p, c))
    # gros lots : procédures des montants >= 1 MEUR
    big = [r for r in sub if (float(r['montant'] or 0) >= 1000000)]
    print('-- gros lots >= 1 MEUR : %d --' % len(big))
    for p, c in Counter(r['procedure'] for r in big).most_common():
        print('- %s : %d' % (p, c))
