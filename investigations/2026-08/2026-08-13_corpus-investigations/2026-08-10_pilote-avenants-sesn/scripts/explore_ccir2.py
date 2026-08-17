#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Donnees complètes 26-72571 : accord-cadre CCIR desserte ferroviaire terminal Ribécourt.
Usage : python3 scripts/explore_ccir2.py
"""
import json
import re
import subprocess
import urllib.parse

UA = "Mozilla/5.0"
BASE = "https://boamp-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/boamp/records"

def curl(url):
    r = subprocess.run(["curl", "-s", "-L", "--compressed", "--max-time", "60", "-A", UA, url],
                       capture_output=True)
    return r.stdout.decode("utf-8", errors="ignore")

url = BASE + "?" + urllib.parse.urlencode({"where": "idweb='26-72571'", "limit": 2})
body = curl(url)
d = json.loads(body)
for rec in d.get("results", []):
    r2 = rec.get("record", {}) if "record" in rec else rec
    f = r2.get("fields", r2)
    dn = f.get("donnees")
    s = json.dumps(dn, ensure_ascii=False) if dn else ""
    print("=== 26-72571 : donnees complètes ===")
    # Décoder la chaîne JSON imbriquée
    try:
        obj = json.loads(dn) if isinstance(dn, str) else dn
        if isinstance(obj, str):
            obj = json.loads(obj)
    except Exception:
        obj = dn
    print(json.dumps(obj, ensure_ascii=False, indent=1)[:6000])
