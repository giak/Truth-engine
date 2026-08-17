#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dumper le champ 'donnees' complet des avis TOARC MOE 18-50453 et 19-178514.
Usage : python3 scripts/explore_a3h.py
"""
import json
import subprocess
import urllib.parse

UA = "Mozilla/5.0"
BASE = "https://boamp-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/boamp/records"

def curl(url):
    r = subprocess.run(["curl", "-s", "-L", "--compressed", "--max-time", "60", "-A", UA, url],
                       capture_output=True)
    return r.stdout.decode("utf-8", errors="ignore")

for idweb in ("18-50453", "19-178514"):
    url = BASE + "?" + urllib.parse.urlencode({"where": f"idweb='{idweb}'", "limit": 2})
    body = curl(url)
    try:
        d = json.loads(body)
        for rec in d.get("results", []):
            r2 = rec.get("record", {}) if "record" in rec else rec
            f = r2.get("fields", r2)
            donnees = f.get("donnees")
            out = f"/tmp/toarc_{idweb}_donnees.json"
            with open(out, "w", encoding="utf-8") as fh:
                json.dump(donnees, fh, ensure_ascii=False, indent=1)
            print(f"{idweb}: donnees écrites dans {out} ({len(json.dumps(donnees, ensure_ascii=False))} chars)")
    except Exception as e:
        print(f"{idweb}: ERREUR {e}")
