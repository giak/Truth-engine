#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""API OpenDataSoft BOAMP : avis genie ecologique secteur 2, tries par date.
Usage : python3 scripts/explore_smda14.py
"""
import json
import subprocess
import urllib.parse

UA = "Mozilla/5.0"
BASE = "https://boamp-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/boamp/records"


def query(url, out):
    subprocess.run(["curl", "-s", "-L", "--max-time", "60", "-A", UA, url, "-o", out],
                   capture_output=True)
    try:
        size = len(open(out, "rb").read())
    except OSError:
        size = 0
    print(f"[{size} o] {url[:120]}")
    return size


def show(path, n=30):
    try:
        d = json.load(open(path, encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"  ERR {e}")
        return
    print("  total_count:", d.get("total_count"))
    for r in d.get("results", [])[:n]:
        print("  -", r.get("idweb"), "|", r.get("dateparution", "?"), "|",
              (r.get("objet") or "")[:110])

# 1. Recherche texte "genie ecologique" + tri date desc
q = urllib.parse.quote("génie écologique")
query(f"{BASE}?q={q}&sort=-dateparution&limit=50", "/tmp/ods_ge1.json")
show("/tmp/ods_ge1.json")

# 2. Filtre where objet contains 'genie ecologique' + date >= 2025
w = urllib.parse.quote("objet like '%génie écologique%'")
query(f"{BASE}?where={w}&sort=-dateparution&limit=50", "/tmp/ods_ge2.json")
show("/tmp/ods_ge2.json")

# 3. Filtre plus large : Seine-Nord + 2026
w2 = urllib.parse.quote("objet like '%Seine-Nord%' and dateparution >= '2026-01-01'")
query(f"{BASE}?where={w2}&sort=-dateparution&limit=100", "/tmp/ods_sn2026.json")
show("/tmp/ods_sn2026.json", 40)
