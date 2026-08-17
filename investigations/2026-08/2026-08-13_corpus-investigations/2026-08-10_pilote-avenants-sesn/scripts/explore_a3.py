#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cas A3 : lignes DECP complètes + références 18TRI dans le recensement + recherche BOAMP.
Usage : python3 scripts/explore_a3.py
"""
import csv
import json
import re
import urllib.parse
import urllib.request

BASE = "https://boamp-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/boamp/records"

def api_get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

def main():
    # 1. Lignes DECP A3
    rows = list(csv.DictReader(open("data/decp_sesn_norm.csv", encoding="utf-8")))
    print("=== LIGNES A3 (ids 2706994, 2707054, 2707074) ===")
    for r in rows:
        if r.get("id") in ("2706994", "2707054", "2707074"):
            for k, v in r.items():
                if v:
                    print(f"  {k}: {v}")
            print("---")

    # 2. Références 18TRI / TRI / TOARC dans le recensement
    print("\n=== REFERENCES 18TRI / TRI / TOARC dans recensement_univers_v3.csv ===")
    for f in ("data/recensement_univers_v3.csv", "data/recensement_univers.csv"):
        try:
            with open(f, encoding="utf-8") as fh:
                for line in fh:
                    if re.search(r"18TRI|TOARC|TRI00|\bTRI\b", line, re.I):
                        print(f"  [{f}] {line.rstrip()[:200]}")
        except OSError:
            pass

    # 3. Recherche BOAMP : TOARC
    print("\n=== BOAMP: objet like '%TOARC%' ===")
    try:
        d = api_get(BASE + "?" + urllib.parse.urlencode({"where": "objet like '%TOARC%'", "limit": 20, "sort": "-dateparution"}))
        print("  total:", d.get("total_count"))
        for rec in d.get("results", []):
            r = rec.get("record", {}) if "record" in rec else rec
            f = r.get("fields", r)
            print("  -", f.get("dateparution"), "|", f.get("idweb"), "|", (f.get("objet") or "")[:130])
    except Exception as e:
        print("  ERREUR:", e)

    # 4. Recherche BOAMP : maitrise d'oeuvre / TRI / recherche 18TRI001
    print("\n=== BOAMP: objet like '%18TRI001%' ===")
    try:
        d = api_get(BASE + "?" + urllib.parse.urlencode({"where": "objet like '%18TRI001%'", "limit": 20, "sort": "-dateparution"}))
        print("  total:", d.get("total_count"))
        for rec in d.get("results", []):
            r = rec.get("record", {}) if "record" in rec else rec
            f = r.get("fields", r)
            print("  -", f.get("dateparution"), "|", f.get("idweb"), "|", (f.get("objet") or "")[:130])
    except Exception as e:
        print("  ERREUR:", e)

    # 5. Recherche BOAMP : Egis OR Arcadis OR Arcadis + Seine-Nord (maitrise d'oeuvre travaux)
    print("\n=== BOAMP: objet like '%maitrise d%oeuvre%' AND '%Seine-Nord%' ===")
    try:
        d = api_get(BASE + "?" + urllib.parse.urlencode({"where": "objet like '%maitrise d%oeuvre%' and objet like '%Seine-Nord%'", "limit": 30, "sort": "-dateparution"}))
        print("  total:", d.get("total_count"))
        for rec in d.get("results", []):
            r = rec.get("record", {}) if "record" in rec else rec
            f = r.get("fields", r)
            print("  -", f.get("dateparution"), "|", f.get("idweb"), "|", (f.get("objet") or "")[:130])
    except Exception as e:
        print("  ERREUR:", e)

if __name__ == "__main__":
    main()
