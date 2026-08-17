#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Localiser 18-50453 (avril 2018) et 19-178514 (déc. 2019) dans les index DILA v240.
Usage : python3 scripts/explore_a3d.py
"""
import re
import subprocess

UA = "Mozilla/5.0"

def curl(url):
    r = subprocess.run(["curl", "-s", "--max-time", "40", "-A", UA, url],
                       capture_output=True)
    return r.stdout.decode("utf-8", errors="ignore")

# Balayage des index mensuels : chercher les fichiers dans les listings
# L'index v240 liste les fichiers par mois ? Testons l'index racine du mois.
for idweb, mois, annee, jours in (
    ("18-50453", "2018", "04", range(10, 21)),
    ("19-178514", "2019", "12", range(1, 12)),
):
    print(f"=== recherche {idweb} ===")
    found = False
    for j in jours:
        d = f"{annee}/{mois}/{j:02d}"
        url = f"https://echanges.dila.gouv.fr/OPENDATA/BOAMP/FluxHistorique/Boamp_v240/{d}/"
        body = curl(url)
        if idweb in body:
            print(f"  TROUVÉ dans index {d}")
            found = True
            break
    if not found:
        print("  non trouvé dans les jours testés")
