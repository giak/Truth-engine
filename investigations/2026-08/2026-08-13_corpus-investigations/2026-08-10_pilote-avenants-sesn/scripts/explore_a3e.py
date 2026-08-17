#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tester l'index DILA (structure) + balayage large pour localiser les avis TOARC.
Usage : python3 scripts/explore_a3e.py
"""
import re
import subprocess

UA = "Mozilla/5.0"

def curl(url):
    r = subprocess.run(["curl", "-s", "--max-time", "40", "-A", UA, url],
                       capture_output=True)
    return r.stdout.decode("utf-8", errors="ignore")

# 1. Tester un index du jour récent connu (26-37280 était à 2026/04/14)
print("=== test index 2026/04/14 ===")
body = curl("https://echanges.dila.gouv.fr/OPENDATA/BOAMP/2026/04/14/")
print("  taille:", len(body))
print("  contient 26-37280:", "26-37280" in body)
print("  aperçu:", re.sub(r"<[^>]+>", " ", body)[:300] if body else "VIDE")

# 2. Balayage 2018 avril : jours 1-30 (FluxHistorique v240)
print("\n=== balayage 18-50453 sur avril 2018 (jours 1-30) ===")
found = False
for j in range(1, 31):
    d = f"2018/04/{j:02d}"
    url = f"https://echanges.dila.gouv.fr/OPENDATA/BOAMP/FluxHistorique/Boamp_v240/{d}/"
    body = curl(url)
    if "18-50453" in body:
        print(f"  TROUVÉ dans {d}")
        found = True
        break
if not found:
    print("  non trouvé (30 jours balayés)")

# 3. Balayage 2019 décembre : jours 1-31
print("\n=== balayage 19-178514 sur décembre 2019 (jours 1-31) ===")
found = False
for j in range(1, 32):
    d = f"2019/12/{j:02d}"
    url = f"https://echanges.dila.gouv.fr/OPENDATA/BOAMP/FluxHistorique/Boamp_v240/{d}/"
    body = curl(url)
    if "19-178514" in body:
        print(f"  TROUVÉ dans {d}")
        found = True
        break
if not found:
    print("  non trouvé (31 jours balayés)")
