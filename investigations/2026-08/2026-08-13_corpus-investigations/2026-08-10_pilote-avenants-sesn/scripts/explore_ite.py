#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Avis ITE Ribécourt 22-146482 et 23-80795 : donnees complètes (attributaire, montant, objet).
Usage : python3 scripts/explore_ite.py
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

for idweb in ("22-146482", "23-80795"):
    url = BASE + "?" + urllib.parse.urlencode({"where": f"idweb='{idweb}'", "limit": 2})
    body = curl(url)
    try:
        d = json.loads(body)
        for rec in d.get("results", []):
            r2 = rec.get("record", {}) if "record" in rec else rec
            f = r2.get("fields", r2)
            print(f"\n===== {idweb} =====")
            print("  objet:", (f.get("objet") or "")[:250])
            print("  nature:", f.get("nature_libelle"), "| dateparution:", f.get("dateparution"))
            print("  type_procedure:", f.get("type_procedure"), "| titre:", (f.get("titulaire") or ""))
            dn = f.get("donnees")
            if dn:
                out = f"/tmp/ite_{idweb}_donnees.json"
                with open(out, "w", encoding="utf-8") as fh:
                    json.dump(dn, fh, ensure_ascii=False, indent=1)
                # Afficher les blocs ATTRIBUTION et OBJET
                s = json.dumps(dn, ensure_ascii=False)
                import re
                for pat in ("ATTRIBUTION", "TITULAIRE", "MONTANT", "VALEUR", "REF_MARCHE", "DATE_ATTRIBUTION", "DUREE", "ACCORD_CADRE", "NB_OFFRE"):
                    for m in re.finditer(pat + r".{0,400}", s):
                        print(f"  [{pat}]:", m.group(0)[:400])
                        break
    except Exception as e:
        print(f"{idweb}: ERREUR {e}")
