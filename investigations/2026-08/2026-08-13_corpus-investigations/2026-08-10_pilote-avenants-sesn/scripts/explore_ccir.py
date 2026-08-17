#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Avis 26-72571 (CCIR acheteur ferroviaire) + travaux plateforme Ribécourt (26-6458, 26-17661).
Usage : python3 scripts/explore_ccir.py
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

def show_avis(idweb):
    url = BASE + "?" + urllib.parse.urlencode({"where": f"idweb='{idweb}'", "limit": 2})
    body = curl(url)
    try:
        d = json.loads(body)
        for rec in d.get("results", []):
            r2 = rec.get("record", {}) if "record" in rec else rec
            f = r2.get("fields", r2)
            print(f"\n===== {idweb} =====")
            print("  objet:", (f.get("objet") or "")[:280])
            print("  nature:", f.get("nature_libelle"), "| date:", f.get("dateparution"))
            print("  acheteur:", (f.get("nomacheteur") or ""), "| titre:", (f.get("titulaire") or ""))
            dn = f.get("donnees")
            if dn:
                s = json.dumps(dn, ensure_ascii=False)
                for pat in ("REF_MARCHE", "OBJET_COMPLET", "TITULAIRE", "MONTANT", "VALEUR",
                            "DATE_ATTRIBUTION", "NB_OFFRE", "DUREE_MOIS", "ACCORD_CADRE", "CPV"):
                    for m in re.finditer(pat + r".{0,420}", s):
                        print(f"  [{pat}]:", m.group(0)[:420])
                        break
    except Exception as e:
        print(f"{idweb}: ERREUR {e}")

for idweb in ("26-72571", "26-6458", "26-17661"):
    show_avis(idweb)
