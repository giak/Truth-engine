#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifier structure decp-global.json + colonnes decp_sesn_raw.csv (ref avis SMDA)."""
import csv
import ijson

# 1. Structure du JSON : premier item
with open("data/decp-global.json", "rb") as f:
    head = f.read(4000)
print("=== debut JSON ===")
print(head[:500].decode("utf-8", errors="ignore"))

# 2. Premier item via ijson (racine)
try:
    with open("data/decp-global.json", "rb") as f:
        parser = ijson.items(f, "marches.item")
        first = next(parser)
        print("\n=== premier item: cles ===")
        print(sorted(first.keys()))
        print("\n=== id/valeur premier item ===")
        for k in ("id", "uid", "identifiant", "_id"):
            if k in first:
                print(f"  {k} = {first[k]}")
except StopIteration:
    print("aucun item sous 'marches.item'")

# 3. Colonnes du CSV brut
rows = list(csv.DictReader(open("data/decp_sesn_raw.csv", encoding="utf-8")))
print("\n=== colonnes decp_sesn_raw.csv ===")
print(list(rows[0].keys()))
print("\n=== ligne 2950343 complete ===")
for r in rows:
    if r.get("id") == "2950343":
        for k, v in r.items():
            if v:
                print(f"  {k}: {v}")
