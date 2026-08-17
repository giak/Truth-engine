#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rectificatif 25-38762 + conditions AAPC 25-17720 (nb lots max, seuil CA).
Usage : python3 scripts/explore_smda19.py
"""
import re
import subprocess
import html as H

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"


def dec(url, out):
    subprocess.run(["curl", "-s", "--max-time", "60", "-A", UA, url, "-o", out], capture_output=True)
    try:
        size = len(open(out, "rb").read())
    except OSError:
        size = 0
    print(f"\n[{size} o] {url}")
    if size < 500:
        print("  absent")
        return None
    t = open(out, encoding="utf-8", errors="ignore").read()
    txt = re.sub(r"<[^>]+>", "|", t)
    txt = re.sub(r"\|+", "|", txt)
    txt = H.unescape(txt)
    return [l.strip() for l in txt.split("|") if l.strip()]


# 1. Rectificatif 25-38762
for jour in ("2025/04/06", "2025/04/05", "2025/04/07", "2025/04/08"):
    lines = dec(f"https://echanges.dila.gouv.fr/OPENDATA/BOAMP/FluxHistorique/Boamp_v240/{jour}/25-38762.xml",
                f"/tmp/smda_38762.xml")
    if lines and len(open("/tmp/smda_38762.xml", "rb").read()) > 500:
        break

if lines:
    print("=== RECTIFICATIF 25-38762 ===")
    for l in lines:
        if re.search(r"(rectificatif|modifi|date limit|LOT-|2\.1|2\.2|2\.3|Sud|Nord|nouvelle|report|prolong)", l, re.I):
            print("   |", l[:190])

# 2. Conditions AAPC 25-17720 : nb max lots + seuil CA
lines2 = [l.strip() for l in
          open("/tmp/smda_17720.xml", encoding="utf-8", errors="ignore").read().split("|")
          if l.strip()]
print("\n=== AAPC 25-17720 : conditions ===")
for i, l in enumerate(lines2):
    if re.search(r"(Nombre maximal de lots|chiffre d'affaires annuel global|CA annuel|au moins égal|Lots? pour lesquels|attribu[ée]s [àa] un soumissionnaire|seuil|minimum)", l, re.I):
        ctx = [x for x in lines2[max(0, i-1):i+4] if x]
        print("   |", " / ".join(ctx)[:280])

# 3. Recherche du montant estime dans l'AAPC (peut etre absent)
print("\n=== AAPC 25-17720 : montants / valeur estimee ===")
for i, l in enumerate(lines2):
    if re.search(r"(Valeur estim|montant estim|Valeur totale|montant global|EUR|€|7\d{6}|1\d{7})", l):
        ctx = [x for x in lines2[max(0, i-2):i+3] if x]
        print("   |", " / ".join(ctx)[:200])
