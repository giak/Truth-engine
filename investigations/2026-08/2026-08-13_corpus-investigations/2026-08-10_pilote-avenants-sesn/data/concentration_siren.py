#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NEXT-A1 : concentration par SIREN (groupe), pas par SIRET.
Regroupe les differents SIRET d'un meme SIREN (lecon pilote SESN :
normalisation SIREN). Calcule le poids de chaque groupe par nb
d'apparitions et par somme des montants plafonds.
"""
import json
import os
import time
import urllib.request
from collections import Counter, defaultdict

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


CACHE_FILE = '/tmp/enr_angle_a/siren_cache.json'
siren_cache = {}
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, encoding='utf-8') as cf:
            siren_cache = json.load(cf)
    except Exception:
        pass


def resolve(siret):
    if not siret:
        return 'VIDE'
    siren = siret[:9]
    if siren in siren_cache:
        return siren_cache[siren]
    name = 'INCONNU'
    try:
        url = ('https://recherche-entreprises.api.gouv.fr/search?q=' + siren)
        req = urllib.request.Request(url,
                                     headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            d = json.loads(resp.read().decode('utf-8'))
        res = d.get('results', [])
        if res:
            name = res[0]['nom_complet']
    except Exception:
        pass
    siren_cache[siren] = name
    return name


for t, recs in records.items():
    print('\n========== %s : CONCENTRATION PAR SIREN ==========' % t)
    # groupe -> {apparitions, nb marches, somme montants, siret distincts}
    grp = defaultdict(lambda: {'app': 0, 'marches': set(), 'montant': 0.0,
                               'sirets': set()})
    for r in recs:
        m = r.get('montant') or 0
        for siret in titulaires(r):
            if not siret or not siret[:9].isdigit():
                continue
            siren = siret[:9]
            g = grp[siren]
            g['app'] += 1
            g['marches'].add(r.get('id'))
            g['montant'] += m
            g['sirets'].add(siret)
    print('groupes SIREN distincts:', len(grp))
    total_app = sum(g['app'] for g in grp.values())
    print('total apparitions:', total_app)
    # tri par apparitions
    for siren, g in sorted(grp.items(),
                           key=lambda kv: -kv[1]['app'])[:20]:
        print('- %d app (%.1f %%) | %d marches | montant total %.0f EUR | %d SIRET | %s' % (
            g['app'], 100.0 * g['app'] / total_app, len(g['marches']),
            g['montant'], len(g['sirets']), resolve(siren)))
