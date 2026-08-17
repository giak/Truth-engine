#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Essayer l'API Explore v2.1 OpenDataSoft du BOAMP + catalogue des datasets.
Usage : python3 scripts/explore_smda13.py
"""
import json
import subprocess
import urllib.parse

UA = "Mozilla/5.0"


def get(url, out, ua=UA):
    subprocess.run(["curl", "-s", "-L", "--max-time", "60", "-A", ua, url, "-o", out],
                   capture_output=True)
    try:
        size = len(open(out, "rb").read())
    except OSError:
        size = 0
    txt = ""
    try:
        txt = open(out, encoding="utf-8", errors="ignore").read()[:200]
    except OSError:
        pass
    print(f"[{size} o] {url[:130]}\n    -> {txt[:160]}")
    return size, txt


base = "https://boamp-datadila.opendatasoft.com"

# 1. Contenu brut du 50 o
get(f"{base}/api/records/1.0/search/?q=test", "/tmp/ods_t1.json", "Mozilla/5.0")

# 2. Catalogue datasets
get(f"{base}/api/datasets/1.0/search/?q=boamp", "/tmp/ods_ds1.json")
get(f"{base}/api/catalog/v1/datasets?limit=50", "/tmp/ods_cat.json")
get(f"{base}/api/explore/v2.1/catalog/datasets?limit=50", "/tmp/ods_cat2.json")

# 3. Explorer v2.1 avec dataset suppose boamp
q = urllib.parse.quote("Seine-Nord")
for ds in ("boamp", "boamp-avis", "avis"):
    get(f"{base}/api/explore/v2.1/catalog/datasets/{ds}/records?limit=5&q={q}",
        f"/tmp/ods_{ds}.json")

# 4. Analyser les resultats
import glob
for p in glob.glob("/tmp/ods_*.json"):
    try:
        d = json.load(open(p, encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        continue
    if isinstance(d, dict) and ("results" in d or "records" in d or "datasets" in d):
        print(f"\n=== {p} ===")
        print("  cles:", list(d.keys())[:8])
        results = d.get("results") or d.get("records") or d.get("datasets") or []
        print("  nb:", len(results))
        for r in results[:10]:
            print("  -", str(r)[:200])
