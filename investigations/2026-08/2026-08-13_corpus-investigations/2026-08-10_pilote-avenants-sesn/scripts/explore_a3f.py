#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Couverture du flux DILA v240 + champs du dataset boamp (recherche texte avis complet).
Usage : python3 scripts/explore_a3f.py
"""
import json
import re
import subprocess
import urllib.parse
import urllib.request

UA = "Mozilla/5.0"

def curl(url):
    r = subprocess.run(["curl", "-s", "--max-time", "40", "-A", UA, url],
                       capture_output=True)
    return r.stdout.decode("utf-8", errors="ignore")

# 1. Couverture v240 : lister l'index racine FluxHistorique
print("=== index FluxHistorique ===")
body = curl("https://echanges.dila.gouv.fr/OPENDATA/BOAMP/FluxHistorique/")
print("  aperçu:", re.sub(r"<[^>]+>", " ", body)[:600])

# 2. Champs du dataset boamp
print("\n=== schéma dataset boamp (premiers champs) ===")
url = "https://boamp-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/boamp"
try:
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60) as r:
        d = json.load(r)
    for f in d.get("fields", [])[:40]:
        print("  -", f.get("name"), "|", f.get("type"))
except Exception as e:
    print("  ERREUR:", e)

# 3. Récupérer l'avis 18-50453 complet via l'API (tous les champs)
print("\n=== avis 18-50453 complet ===")
url = BASE = "https://boamp-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/boamp/records"
w = urllib.parse.quote("idweb='18-50453'")
try:
    with urllib.request.urlopen(urllib.request.Request(BASE + "?" + urllib.parse.urlencode({"where": "idweb='18-50453'", "limit": 2}), headers={"User-Agent": UA}), timeout=60) as r:
        d = json.load(r)
    for rec in d.get("results", []):
        r2 = rec.get("record", {}) if "record" in rec else rec
        f = r2.get("fields", r2)
        for k, v in f.items():
            vs = str(v)
            print(f"  {k}: {vs[:400]}")
        print("---")
except Exception as e:
    print("  ERREUR:", e)
