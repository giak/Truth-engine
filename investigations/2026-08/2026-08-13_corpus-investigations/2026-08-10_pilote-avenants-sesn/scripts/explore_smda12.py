#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Interroger l'API OpenDataSoft BOAMP (decouverte via HTML boamp.fr).
Usage : python3 scripts/explore_smda12.py
"""
import json
import subprocess
import urllib.parse

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"


def get(url, out):
    subprocess.run(["curl", "-s", "-L", "--max-time", "60", "-A", UA, url, "-o", out],
                   capture_output=True)
    try:
        size = len(open(out, "rb").read())
    except OSError:
        size = 0
    print(f"[{size} o] {url[:140]}")
    return size


# 1. Decouvrir le dataset
get("https://boamp-datadila.opendatasoft.com/api/records/1.0/search/", "/tmp/ods_root.json")

# 2. Recherche "genie ecologique" + "Seine-Nord"
q = urllib.parse.quote("génie écologique Seine-Nord")
get(f"https://boamp-datadila.opendatasoft.com/api/records/1.0/search/?q={q}&rows=20", "/tmp/ods_search1.json")

# 3. Recherche par acheteur SCSNE
q2 = urllib.parse.quote("Canal Seine-Nord Europe")
get(f"https://boamp-datadila.opendatasoft.com/api/records/1.0/search/?q={q2}&rows=50&sort=-dateparution", "/tmp/ods_search2.json")

for path in ("/tmp/ods_root.json", "/tmp/ods_search1.json", "/tmp/ods_search2.json"):
    try:
        d = json.load(open(path, encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"{path}: {e}")
        continue
    print(f"\n=== {path} ===")
    print("  total:", d.get("total_count") or d.get("nhits") or "?")
    for rec in d.get("records", [])[:50]:
        f = rec.get("fields", {})
        ident = f.get("id", f.get("numero", "?"))
        titre = f.get("titre", f.get("objet", "?"))[:120]
        date = f.get("dateparution", f.get("date", "?"))
        acheteur = f.get("acheteur", f.get("nom_acheteur", "?"))[:60]
        print(f"  - {ident} | {date} | {titre} | {acheteur}")
