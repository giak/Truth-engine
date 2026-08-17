#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lister les 52 avis TOARC + filtrer MOE Seine-Nord (accord-cadre parent A3).
Usage : python3 scripts/explore_a3b.py
"""
import json
import urllib.parse
import urllib.request

BASE = "https://boamp-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/boamp/records"

def api_get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

def show(d, n=60):
    print("  total:", d.get("total_count"))
    for rec in d.get("results", []):
        r = rec.get("record", {}) if "record" in rec else rec
        f = r.get("fields", r)
        print("  -", f.get("dateparution"), "|", f.get("idweb"), "|",
              (f.get("objet") or "")[:150], "|", (f.get("acheteurnom") or "")[:30])

# 1. Tous les TOARC (52)
print("=== TOUS les avis TOARC (52) ===")
d = api_get(BASE + "?" + urllib.parse.urlencode({"where": "objet like '%TOARC%'", "limit": 60, "sort": "-dateparution"}))
show(d)

# 2. TOARC + maitrise d'oeuvre / oeuvre
print("\n=== TOARC + (maitrise d'oeuvre|oeuvre|18TRI|secteur 2|secteur 3) ===")
w = "objet like '%TOARC%' and (objet like '%maitrise%' or objet like '%18TRI%' or objet like '%oeuvre%')"
d = api_get(BASE + "?" + urllib.parse.urlencode({"where": w, "limit": 40, "sort": "-dateparution"}))
show(d, 40)
