#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NEXT-A1 : analyse de concentration SDEM/SOREGIES.
- regroupe par objet normalise (marche/lot)
- extrait les titulaires (structure {"titulaire": {"id": SIRET}})
- resout les SIREN via API recherche-entreprises
"""
import json
import re
import csv
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


def norm_obj(o):
    return re.sub(r'[^a-z0-9]', '', (o or '').lower())[:100]


def titulaires(r):
    """Retourne la liste des SIRET titulaires."""
    out = []
    for t in (r.get('titulaires') or []):
        if isinstance(t, dict):
            if 'titulaire' in t and isinstance(t['titulaire'], dict):
                out.append(t['titulaire'].get('id', ''))
            elif 'id' in t:
                out.append(t.get('id', ''))
    return out


siren_cache = {}


def resolve(siret):
    siren = siret[:9]
    if siren in siren_cache:
        return siren_cache[siren]
    try:
        url = ('https://recherche-entreprises.api.gouv.fr/search?q=' + siren)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=20) as resp:
            d = json.loads(resp.read().decode('utf-8'))
        res = d.get('results', [])
        name = res[0]['nom_complet'] if res else 'INCONNU'
    except Exception:
        name = 'INCONNU'
    siren_cache[siren] = name
    return name


for t, recs in records.items():
    print('\n========== %s (%d marches) ==========' % (t, len(recs)))
    # regrouper par objet normalise
    groups = defaultdict(list)
    for r in recs:
        groups[norm_obj(r.get('objet'))].append(r)
    print('objets distincts:', len(groups))
    # somme par groupe et nombre de titulaires
    for key, grp in sorted(groups.items(),
                           key=lambda kv: -sum(r.get('montant') or 0
                                               for r in kv[1])):
        total = sum(r.get('montant') or 0 for r in grp)
        tits = [titulaires(r) for r in grp]
        flat = [x for sub in tits for x in sub]
        uniq = list(dict.fromkeys(flat))
        print('- [%d recs] total=%.0f EUR | %d titulaires distincts' % (
            len(grp), total, len(uniq)))
        print('  objet:', grp[0].get('objet', '')[:150])
        for siret in uniq:
            print('    - %s = %s' % (siret, resolve(siret)))
