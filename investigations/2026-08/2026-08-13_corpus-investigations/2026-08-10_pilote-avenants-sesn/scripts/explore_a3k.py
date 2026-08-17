#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Objets complets des 3 lignes A3 (2706994, 2707054, 2707074) + contexte titulaires.
Usage : python3 scripts/explore_a3k.py
"""
import csv
import json
import urllib.request

rows = list(csv.DictReader(open("data/decp_sesn_norm.csv", encoding="utf-8")))
print("=== OBJETS COMPLETS A3 ===")
for r in rows:
    if r.get("id") in ("2706994", "2707054", "2707074"):
        print(f"\n[{r['id']}] titulaire={r.get('titulaires_siret')} montant={r.get('montant')} date={r.get('dateNotification')}")
        print("  OBJET:", r.get("objet"))

# Vérifier EGIS 493334429 et groupement ONE 582132551 via API recherche-entreprises
print("\n=== API recherche-entreprises ===")
for s in ("493334429", "582132551", "401503792"):
    try:
        with urllib.request.urlopen(urllib.request.Request(
            f"https://recherche-entreprises.api.gouv.fr/search?q={s}&per_page=1",
            headers={"User-Agent": "Mozilla/5.0"}), timeout=30) as r:
            d = json.load(r)
        for res in d.get("results", [])[:1]:
            print(f"  {s}: {res.get('nom_complet')} | {res.get('nature_juridique')} | siège: {res.get('siege', {}).get('adresse')}")
    except Exception as e:
        print(f"  {s}: ERREUR {e}")
