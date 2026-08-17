#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Historique BOAMP : tous les avis Ribécourt + exploitation plateforme (avant 2025).
Usage : python3 scripts/explore_ribhist.py
"""
import json
import urllib.parse
import urllib.request

BASE = "https://boamp-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/boamp/records"

def api_get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

def show(d, n=40):
    print("  total:", d.get("total_count"))
    for rec in d.get("results", []):
        r = rec.get("record", {}) if "record" in rec else rec
        f = r.get("fields", r)
        print("  -", f.get("dateparution"), "|", f.get("idweb"), "|",
              (f.get("objet") or "")[:130], "|", (f.get("nomacheteur") or "")[:35])

# 1. Tous les avis avec Ribecourt dans l'objet, toutes années (asc = historique)
print("=== Tous les avis 'Ribecourt' (objet), date ASC (historique) ===")
d = api_get(BASE + "?" + urllib.parse.urlencode({"where": "objet like '%Ribecourt%'", "limit": 50, "sort": "dateparution"}))
show(d)

# 2. Ribecourt + exploitation
print("\n=== Ribecourt + (exploitation|exploiter|gestion) ===")
w = "objet like '%Ribecourt%' and (objet like '%exploitation%' or objet like '%gestion%')"
d = api_get(BASE + "?" + urllib.parse.urlencode({"where": w, "limit": 30, "sort": "dateparution"}))
show(d, 30)

# 3. Ribecourt + acheteur CCIR (CCIR ou CCI)
print("\n=== Ribecourt + acheteur CCI/CCIR ===")
w = "objet like '%Ribecourt%' and (nomacheteur like '%CCI%' or nomacheteur like '%CHAMBRE DE COMMERCE%')"
d = api_get(BASE + "?" + urllib.parse.urlencode({"where": w, "limit": 30, "sort": "dateparution"}))
show(d, 30)
