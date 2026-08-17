#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Telecharger + decryptage complet avis BOAMP 26-37280 (genie ecologique secteur 2).
Usage : python3 scripts/explore_smda15.py
"""
import re
import subprocess

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

URLS = [
    "https://echanges.dila.gouv.fr/OPENDATA/BOAMP/2026/04/14/26-37280.xml",
]
for url in URLS:
    out = "/tmp/smda_37280.xml"
    subprocess.run(["curl", "-s", "--max-time", "60", "-A", UA, url, "-o", out], capture_output=True)
    size = len(open(out, "rb").read())
    print(f"[{size} o] {url}")
    if size < 500:
        print("  absent ou vide")
        continue

    t = open(out, encoding="utf-8", errors="ignore").read()
    txt = re.sub(r"<[^>]+>", "|", t)
    txt = re.sub(r"\|+", "|", txt)
    import html as H
    txt = H.unescape(txt)
    lines = [l.strip() for l in txt.split("|") if l.strip()]
    print(f"\n=== AVIS 26-37280 : {len(lines)} segments ===")
    # Afficher les segments cles
    for i, l in enumerate(lines):
        if re.search(r"(Travaux d|g[ée]nie|secteur|2\.1|2\.2|Sud|Nord|SMDA|SOINS|378998363|attribu|montant|Valeur|EUR|lot|Date|2026-04|proc[ée]dure|Avis)", l, re.I):
            print(f"  {l[:200]}")
