#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correction du doublon defectueux id=000 (source marches-publics_aws).

Decision (2026-08-10 12:47 CEST) : la ligne AWS 000 est un doublon du contrat
M214-Lot Q2 (quai neuf de Catigny, 4 228 416,00 EUR HT, attribue a Charier GC,
conclu 2025-11-20, avis BOAMP 25-132968 / JOUE 806579-2025).
Le montant 422 841 600,00 EUR est une erreur d'unite x100 (centimes/euros) :
4228416 x 100 = 422841600. Le libelle AWS reprend par erreur le lot Q1-M213
(rehabilitation 4 quais, SPIE Batignolles Nord, 2 999 530,10 EUR).
Aucun avis BOAMP/TED ne connait de marche de quais a 422 M EUR (total M215 = 7 227 946,10 EUR).

Action : marquer la ligne en DOUBLON_DEFECTUEUX, corriger le montant a 4228416.0
(montant reel du contrat), laisser la ligne pour tracabilite. Le cumul agr ge
Doit DEDUPLIQUER (ne compter le contrat qu'une fois, via la DECP PLACE 2844722).

Usage : python3 scripts/02_corriger_doublon.py
Sortie : data/decp_sesn_raw_v2.csv (46 lignes, montant corrige + colonne correction_doublon)
         data/decp_sesn_raw_v2.csv.sha256
"""
import csv, hashlib
from decimal import Decimal

SRC = 'data/decp_sesn_raw.csv'
DST = 'data/decp_sesn_raw_v2.csv'
TARGET_MONTANT = Decimal('422841600.0')
CORR_MONTANT = '4228416.0'

rows = list(csv.DictReader(open(SRC, encoding='utf-8')))
fieldnames = list(rows[0].keys()) + ['correction_doublon']

found = 0
for r in rows:
    m = Decimal(r['montant']) if r['montant'] else None
    if r['id'] == '000' and r['source'] == 'marches-publics_aws' and m == TARGET_MONTANT:
        r['montant'] = CORR_MONTANT
        r['correction_doublon'] = 'DOUBLON_DEFECTUEUX de 2844722 (M214-Q2) : erreur unite x100, montant ramene a 4228416.0 ; dedupliquer au cumul'
        found += 1
    else:
        r['correction_doublon'] = ''

assert found == 1, f'attendu 1 doublon, trouve {found}'

with open(DST, 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)

raw = open(DST, 'rb').read()
h = hashlib.sha256(raw).hexdigest()
open(DST + '.sha256', 'w').write(h + '  ' + DST + '\n')

# verification cumul
rows2 = list(csv.DictReader(open(DST, encoding='utf-8')))
somme_v2 = sum((Decimal(r['montant']) for r in rows2 if r['montant']), Decimal('0'))
# cumul deduplique : retirer le montant corrige (le contrat est deja compte via 2844722)
dedup = somme_v2 - Decimal(CORR_MONTANT)
print('lignes v2 :', len(rows2))
print('cumul v2 (montant corrige, SANS dedup) :', somme_v2)
print('cumul DEDUPLIQUE (reference Phase 3)  :', dedup)
print('sha256 :', h)
