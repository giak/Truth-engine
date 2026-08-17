#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Telecharger + decryptage avis BOAMP 25-17720 (16/02/2025) et 25-38762 (06/04/2025).
Usage : python3 scripts/explore_smda18.py
"""
import re
import subprocess
import html as H

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

# D'abord localiser les dates exactes dans le flux DILA 2025 (FluxHistorique v240)
for jour, n in (("2025/02/16", "25-17720"), ("2025/04/06", "25-38762")):
    url = f"https://echanges.dila.gouv.fr/OPENDATA/BOAMP/FluxHistorique/Boamp_v240/{jour}/{n}.xml"
    out = f"/tmp/smda_{n}.xml"
    subprocess.run(["curl", "-s", "--max-time", "60", "-A", UA, url, "-o", out], capture_output=True)
    try:
        size = len(open(out, "rb").read())
    except OSError:
        size = 0
    print(f"[{size} o] {url}")
    if size < 500:
        print("  absent, essai autre date...")
        # essai jour precedent/suivant
        for alt in ("2025/02/15", "2025/02/17", "2025/04/05", "2025/04/07"):
            u2 = f"https://echanges.dila.gouv.fr/OPENDATA/BOAMP/FluxHistorique/Boamp_v240/{alt}/{n}.xml"
            subprocess.run(["curl", "-s", "--max-time", "60", "-A", UA, u2, "-o", out], capture_output=True)
            size = len(open(out, "rb").read())
            if size > 500:
                print(f"  TROUVE au {alt} ({size} o)")
                break
        else:
            print("  introuvable dans le flux, on garde le XML vide")
            continue

    t = open(out, encoding="utf-8", errors="ignore").read()
    txt = re.sub(r"<[^>]+>", "|", t)
    txt = re.sub(r"\|+", "|", txt)
    txt = H.unescape(txt)
    lines = [l.strip() for l in txt.split("|") if l.strip()]
    print(f"  segments: {len(lines)}")
    for l in lines:
        if re.search(r"(Travaux d|g[ée]nie|secteur|2\.1|2\.2|Sud|Nord|SMDA|SOINS|378998363|estim|montant|EUR|lot|LOT|Date limit|2025-|proc[ée]dure|ouverte|Avis|Identifiant interne|M230|M231|M232|offres|Lots)", l, re.I):
            print("   |", l[:190])
    print()
