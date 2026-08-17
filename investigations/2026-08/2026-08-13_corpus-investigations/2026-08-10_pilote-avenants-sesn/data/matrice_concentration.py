#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NEXT-A1 (suite) : matrice de concentration des titulaires.
1. Comptage des apparitions de chaque titulaire sur tout le portefeuille
   SDEM (tous objets) et SOREGIES.
2. Croisement Lot 1 / Lot 2 PV (SDEM) : qui est sur les deux ?
3. Bloc SOREGIES complet.
4. Re-tentative de resolution des SIREN INCONNU (trois essais).
"""
import json
import re
import csv
import os
import time
import urllib.request
from collections import Counter, defaultdict

CACHE_FILE = '/tmp/enr_angle_a/siren_cache.json'

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


def titulaires(r):
    out = []
    for t in (r.get('titulaires') or []):
        if isinstance(t, dict):
            if 'titulaire' in t and isinstance(t['titulaire'], dict):
                out.append(t['titulaire'].get('id', ''))
            elif 'id' in t:
                out.append(t.get('id', ''))
    return out


siren_cache = {}
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, encoding='utf-8') as cf:
            siren_cache = json.load(cf)
    except Exception:
        siren_cache = {}


def resolve(siret, retries=3):
    if not siret:
        return 'VIDE'
    siren = siret[:9]
    if siren in siren_cache:
        return siren_cache[siren]
    name = 'INCONNU'
    for i in range(retries):
        try:
            url = ('https://recherche-entreprises.api.gouv.fr/search?q=' + siren)
            req = urllib.request.Request(url,
                                         headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=20) as resp:
                d = json.loads(resp.read().decode('utf-8'))
            res = d.get('results', [])
            if res:
                name = res[0]['nom_complet']
            break
        except Exception:
            time.sleep(2)
    siren_cache[siren] = name
    return name


def save_cache():
    try:
        os.makedirs('/tmp/enr_angle_a', exist_ok=True)
        with open(CACHE_FILE, 'w', encoding='utf-8') as cf:
            json.dump(siren_cache, cf, ensure_ascii=False)
    except Exception:
        pass


# ---- 1. Comptage des apparitions par titulaire (tout le portefeuille) ----
print('===== CONCENTRATION PAR TITULAIRE (apparitions sur tous objets) =====')
for t, recs in records.items():
    cnt = Counter()
    for r in recs:
        for s in titulaires(r):
            cnt[s] += 1
    print('\n-- %s : %d marches, %d apparitions titulaires --' % (
        t, len(recs), sum(cnt.values())))
    for siret, c in cnt.most_common():
        print('- %d x | %s = %s' % (c, siret, resolve(siret)))

# ---- 2. Croisement Lot 1 / Lot 2 PV SDEM ----
print('\n===== CROISEMENT LOT 1 (PV < 100 kW) / LOT 2 (PV > 100 kW) SDEM =====')
lot1 = set()
lot2 = set()
for r in records['255601106']:
    obj = (r.get('objet') or '')
    if 'centrales photovolta' in obj.lower():
        if 'lot 1' in obj.lower() or 'lot1' in obj.lower():
            lot1.update(titulaires(r))
        elif 'lot 2' in obj.lower() or 'lot2' in obj.lower():
            lot2.update(titulaires(r))
inter = lot1 & lot2
print('Lot 1 (%d titulaires) :' % len(lot1))
for s in sorted(lot1):
    print('  -', s, '=', resolve(s))
print('Lot 2 (%d titulaires) :' % len(lot2))
for s in sorted(lot2):
    print('  -', s, '=', resolve(s))
print('INTERSECTION (%d) :' % len(inter))
for s in sorted(inter):
    print('  -', s, '=', resolve(s))

save_cache()

# ---- 3. Bloc SOREGIES complet ----
print('\n===== SOREGIES : DETAIL PAR MARCHE =====')
for r in sorted(records['450889225'], key=lambda r: -(r.get('montant') or 0)):
    tits = titulaires(r)
    print('- id=%s | %.0f EUR | %s' % (r.get('id'), r.get('montant') or 0,
                                        (r.get('objet') or '')[:110]))
    for s in tits:
        print('    tit = %s = %s' % (s, resolve(s)))
