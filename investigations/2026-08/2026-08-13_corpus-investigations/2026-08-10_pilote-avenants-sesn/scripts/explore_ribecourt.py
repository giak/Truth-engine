#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exploration cas A2 Ribécourt : ligne DECP complète + recherche avis BOAMP/TED.
Usage : python3 scripts/explore_ribecourt.py
"""
import csv
import json
import re
import urllib.request
import urllib.parse

BASE = "https://boamp-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/boamp/records"

def api_get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def show(d, n=15):
    print("  total_count:", d.get("total_count"))
    for rec in d.get("results", [])[:n]:
        r = rec.get("record", {}) if isinstance(rec, dict) and "record" in rec else rec
        f = r.get("fields", r)
        print(" -", f.get("dateparution"), "|", f.get("idweb") or f.get("numeroavis"), "|",
              (f.get("objet") or "")[:110], "|", (f.get("acheteurnom") or "")[:40])
        # debug : si tout est vide, afficher les clés
        if not any([f.get("dateparution"), f.get("idweb"), f.get("objet")]):
            print("    KEYS:", list(r.keys())[:12])

def main():
    # 1. Ligne DECP A2 complète
    rows = list(csv.DictReader(open("data/decp_sesn_norm.csv", encoding="utf-8")))
    print("=== LIGNE A2 (Ribécourt) ===")
    for r in rows:
        if "Rib" in (r.get("objet") or "") or "130022718" in (r.get("titulaires_siren") or ""):
            for k, v in r.items():
                if v:
                    print(f"  {k}: {v}")
            print("---")
    # 2. Recherche texte "Ribecourt" (q=)
    print("\n=== RECHERCHE q=Ribécourt ===")
    try:
        d = api_get(BASE + "?" + urllib.parse.urlencode({"q": "Ribécourt", "limit": 15, "sort": "-dateparution"}))
        show(d)
    except Exception as e:
        print("  ERREUR:", e)
    # 3. where objet like 'plateforme trimodale'
    print("\n=== WHERE objet like 'plateforme trimodale' ===")
    try:
        d = api_get(BASE + "?" + urllib.parse.urlencode({"where": "objet like '%plateforme trimodale%'", "limit": 15, "sort": "-dateparution"}))
        show(d)
    except Exception as e:
        print("  ERREUR:", e)
    # 4. where objet like 'trimodale' AND Seine-Nord / 60170
    print("\n=== WHERE objet like '%trimodale%' ===")
    try:
        d = api_get(BASE + "?" + urllib.parse.urlencode({"where": "objet like '%trimodale%'", "limit": 30, "sort": "-dateparution"}))
        show(d, 25)
    except Exception as e:
        print("  ERREUR:", e)

if __name__ == "__main__":
    main()
