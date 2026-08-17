#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inspecter bm_cpv.html / ted_rech.html + scan DILA fin avril 2026 par contenu.
Usage : python3 scripts/explore_smda11.py
"""
import os
import re
import subprocess

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"


def show(path, label):
    try:
        t = open(path, encoding="utf-8", errors="ignore").read()
    except OSError:
        print(f"{label}: absent")
        return
    txt = re.sub(r"<[^>]+>", " ", t)
    txt = re.sub(r"\s+", " ", txt)
    print(f"\n=== {label} ({len(t)} o) ===")
    for pat in ("génie écologique", "SMDA", "SOINS", "45100000", "Seine-Nord", "secteur 2"):
        idx = txt.find(pat)
        if idx != -1:
            print(f"  '{pat}' @ {idx}: ...{txt[max(0,idx-120):idx+220]}...")
    # liens avis
    links = sorted(set(re.findall(r'https?://www\.boamp\.fr/avis/[^"\'\s<>]+', t)))
    for l in links[:15]:
        print("  LINK:", l)


show("/tmp/bm_cpv.html", "BOAMP CPV 45100000")
show("/tmp/ted_rech.html", "TED recherche")

# ---- Scan DILA fin avril 2026 : chercher Canal Seine-Nord par contenu
print("\n=== SCAN DILA 2026/04/20-30 (contenu 'Seine-Nord') ===")
jours = ["2026/04/20", "2026/04/21", "2026/04/22", "2026/04/23", "2026/04/24",
         "2026/04/27", "2026/04/28", "2026/04/29", "2026/04/30"]
found = 0
for jour in jours:
    idx_path = f"/tmp/dila_{jour.replace('/', '_')}.html"
    if not os.path.exists(idx_path):
        subprocess.run(["curl", "-s", "--max-time", "40", "-A", UA,
                        f"https://echanges.dila.gouv.fr/OPENDATA/BOAMP/{jour}/",
                        "-o", idx_path], capture_output=True)
    try:
        t = open(idx_path, encoding="utf-8", errors="ignore").read()
    except OSError:
        continue
    nums = sorted(set(re.findall(r"26-\d{5}", t)))
    for n in nums:
        url = f"https://echanges.dila.gouv.fr/OPENDATA/BOAMP/{jour}/{n}.xml"
        fxml = f"/tmp/sc_{n}.xml"
        subprocess.run(["curl", "-s", "--max-time", "20", "-A", UA, url, "-o", fxml],
                       capture_output=True)
        try:
            body = open(fxml, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        if re.search(r"Canal Seine-Nord|SCSNE|829535996", body):
            obj = re.search(r"<(?:LIBELLE|OBJET|TITRE)>[^<]{0,160}", body)
            typ = re.search(r"<TYPE_AVIS>[^<]{0,60}", body)
            print(f"  HIT {jour} {n}: {typ.group(0) if typ else ''} | {obj.group(0) if obj else ''}")
            found += 1
print(f"total hits Seine-Nord fin avril: {found}")
