#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Signaux : offres uniques (candidature unique) et modifications
(avenants) avec montants, pour SDEM et SOREGIES."""
import json
import os
import time
import urllib.request
from collections import Counter

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
    print('\n========== %s ==========' % t)
    # 1. Offres uniques
    uniq = [r for r in recs if str(r.get('offresRecues')) == '1']
    print('--- MARCHES A OFFRE UNIQUE : %d ---' % len(uniq))
    tit_uniq = Counter()
    for r in uniq:
        for s in titulaires(r):
            tit_uniq[s[:9]] += 1
    for siren, c in tit_uniq.most_common(15):
        print('- %d x | %s = %s' % (c, siren, resolve(siren)))
    # montant total
    tot_uniq = sum(r.get('montant') or 0 for r in uniq)
    print('montant total offres uniques: %.0f EUR' % tot_uniq)
    # PV parmi les offres uniques
    pv_uniq = [r for r in uniq if 'photovolta' in (r.get('objet') or '').lower()]
    print('dont PV: %d, montant %.0f EUR' % (
        len(pv_uniq), sum(r.get('montant') or 0 for r in pv_uniq)))
    for r in uniq[:12]:
        print('  - id=%s | montant=%.0f | %s' % (
            r.get('id'), r.get('montant') or 0, (r.get('objet') or '')[:100]))

    # 2. Modifications avec montant
    print('\n--- MODIFICATIONS (AVENANTS) ---')
    mods = []
    for r in recs:
        for m in (r.get('modifications') or []):
            mm = m.get('modification', m)
            if mm.get('montant'):
                mods.append((mm.get('montant'), r.get('id'),
                             (r.get('objet') or '')[:90]))
    print('modifications avec montant:', len(mods))
    mods.sort(reverse=True)
    for montant, mid, obj in mods[:15]:
        print('- +%.0f EUR | id=%s | %s' % (montant, mid, obj))
    tot_mod = sum(x[0] for x in mods)
    print('total avenants avec montant: %.0f EUR' % tot_mod)
