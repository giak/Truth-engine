#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Retrouver l'AAPC du marche M230 (genie ecologique secteur 2).
Usage : python3 scripts/explore_smda17.py
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
    print(f"[{size} o] {url[:130]}")
    return size


def show(path, n=20):
    try:
        d = json.load(open(path, encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print("  ERR", e)
        return
    print("  total_count:", d.get("total_count"))
    for r in d.get("results", [])[:n]:
        print("  -", r.get("idweb"), "|", r.get("dateparution", "?"), "|",
              (r.get("objet") or "")[:110], "| famille:", r.get("famille"), "|", r.get("type", ""))

# 1. Recherche par identifiant de procedure (UUID)
q = urllib.parse.quote("1b836649-c3c6-43e8-a087-d673fdc3eb86")
query(f"{BASE}?q={q}&limit=10", "/tmp/ods_uuid.json")
show("/tmp/ods_uuid.json")

# 2. AAPC potentiel : titre exact sans 'attribution' en 2025
w = urllib.parse.quote("objet like '%aménagements de génie écologique - Secteur 2%'")
query(f"{BASE}?where={w}&limit=50", "/tmp/ods_ge_s2.json")
show("/tmp/ods_ge_s2.json", 30)

# 3. Tous les avis SCSNE 2025 avec 'genie ecologique'
w2 = urllib.parse.quote("objet like '%Seine-Nord%' and (objet like '%génie écologique%' or objet like '%aménagements écologiques%')")
query(f"{BASE}?where={w2}&sort=-dateparution&limit=50", "/tmp/ods_sn_ge_all.json")
show("/tmp/ods_sn_ge_all.json", 40)
