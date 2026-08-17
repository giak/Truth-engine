#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Métadonnées complètes 19-178514 + routes d'accès au texte complet 18-50453 / 19-178514.
Usage : python3 scripts/explore_a3g.py
"""
import json
import re
import subprocess
import urllib.parse
import urllib.request

UA = "Mozilla/5.0"

def curl(url, out=None):
    cmd = ["curl", "-s", "-L", "--compressed", "--max-time", "50", "-A", UA]
    if out:
        cmd += ["-o", out]
        cmd.append(url)
        r = subprocess.run(cmd, capture_output=True)
        return r.returncode
    cmd.append(url)
    r = subprocess.run(cmd, capture_output=True)
    return r.stdout.decode("utf-8", errors="ignore")

BASE = "https://boamp-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/boamp/records"

# 1. Métadonnées complètes 19-178514
print("=== 19-178514 métadonnées ===")
url = BASE + "?" + urllib.parse.urlencode({"where": "idweb='19-178514'", "limit": 2})
body = curl(url)
try:
    d = json.loads(body)
    for rec in d.get("results", []):
        r2 = rec.get("record", {}) if "record" in rec else rec
        f = r2.get("fields", r2)
        for k in ("idweb", "objet", "filename", "famille", "dateparution", "datelimitereponse",
                  "nomacheteur", "titulaire", "type_procedure", "nature_libelle",
                  "type_marche", "descripteur_libelle", "procedure_categorise", "etat", "url_avis"):
            print(f"  {k}: {f.get(k)}")
        print("  donnees:", str(f.get("donnees"))[:1500])
except Exception as e:
    print("  ERREUR:", e, body[:200])

# 2. Routes d'accès au contenu complet
print("\n=== routes contenu complet ===")
routes = [
    "https://www.boamp.fr/avis/detail/18-50453",
    "https://www.boamp.fr/pages/avis/?q=idweb:18-50453",
    "https://echanges.dila.gouv.fr/OPENDATA/BOAMP/FluxHistorique/Boamp_v240/2018/04/15/18-50453.xml",
    "https://echanges.dila.gouv.fr/OPENDATA/BOAMP/FluxHistorique/Boamp_v240/2018/04/15/BOAMP-J-AO_2018_105004.xml",
]
for u in routes:
    r = curl(u, out="/tmp/a3route.bin")
    try:
        sz = len(open("/tmp/a3route.bin", "rb").read())
    except OSError:
        sz = 0
    print(f"  [{sz} o] {u}")

# 3. Tenter l'API data.gouv (ancienne API BOAMP) pour le XML
print("\n=== data.gouv API BOAMP ===")
for u in (
    "https://www.data.gouv.fr/api/1/datasets/boamp/",
):
    body = curl(u)
    print(f"  [{len(body)} o] {u}")
    print("  ", body[:300])
