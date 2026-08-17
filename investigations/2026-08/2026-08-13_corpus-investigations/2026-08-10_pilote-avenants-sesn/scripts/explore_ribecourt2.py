#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Avis BOAMP 25-21716 (AAPC) + 26-68097 (attribution) : téléchargement DILA + extraction.
Usage : python3 scripts/explore_ribecourt2.py
"""
import re
import html
import subprocess
import os

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

# idweb -> (année, mois, jour) date de parution connue via l'API
CANDIDATS = {
    "25-21716": ["2025/02/26", "2025/02/25", "2025/02/27"],
    "26-68097": ["2026/07/09", "2026/07/08", "2026/07/10"],
}

def try_download(idweb, date, out):
    for base in (
        f"https://echanges.dila.gouv.fr/OPENDATA/BOAMP/FluxHistorique/Boamp_v240/{date}/{idweb}.xml",
        f"https://echanges.dila.gouv.fr/OPENDATA/BOAMP/{date}/{idweb}.xml",
    ):
        r = subprocess.run(["curl", "-s", "-L", "--max-time", "50", "-A", UA, base, "-o", out],
                           capture_output=True)
        if os.path.exists(out):
            size = os.path.getsize(out)
            if size > 1000:
                print(f"  OK [{size} o] {base}")
                return True
    return False

def clean(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()

def extract(f):
    t = open(f, encoding="utf-8", errors="ignore").read()
    t2 = clean(t)
    print(f"\n===== {f} ({os.path.getsize(f)} o) =====")
    # Type d'avis
    m = re.search(r"(Avis de marché|Avis d'attribution|Avis de préinformation|Réduction des délais|Rectificatif)[^.]{0,60}", t2)
    if m:
        print("  TYPE:", m.group(0)[:90])
    # Objet + procédure
    for pat in ("Objet du marché", "Procédure", "Nature du marché", "Type de procédure"):
        m = re.search(r"\.? ?" + pat + r"[^.]{0,200}", t2)
        if m:
            print(f"  {pat}:", m.group(0)[:220])
    # Montants
    for m in re.finditer(r"\b\d{1,3}(?:\s?\d{3})+(?:[.,]\d{2})?\s*(?:€|EUR|euros)\b", t2):
        v = m.group(0)
        n = int(re.sub(r"[^\d]", "", v.split(".")[0]))
        if n >= 100000:
            print("  MONTANT:", v, "| ctx:", t2[max(0, m.start()-100):m.end()+50][:200])
    # Attributaire
    m = re.search(r"(Attributaire|Titulaire|Nom national)[^.]{0,150}", t2)
    if m:
        print("  ATTRIB:", m.group(0)[:200])
    # Offres / candidats
    m = re.search(r"(Offres reçues|Nombre d'offres|Candidats)[^.]{0,120}", t2)
    if m:
        print("  OFFRES:", m.group(0)[:150])
    # Dates
    for m in re.finditer(r"(Date limite|Date d'envoi|Date de conclusion|Date de notification)[^.]{0,60}", t2):
        print("  DATE:", m.group(0)[:90])
    # Motif (si avis sans mise en concurrence)
    m = re.search(r"(Motif|Sans publicité|Sans mise en concurrence|négociation)[^.]{0,200}", t2, re.I)
    if m:
        print("  MOTIF?:", m.group(0)[:240])

for idweb, dates in CANDIDATS.items():
    out = f"/tmp/rib_{idweb}.xml"
    ok = False
    for d in dates:
        if try_download(idweb, d, out):
            ok = True
            break
    if ok:
        extract(out)
    else:
        print(f"\n=== {idweb} : introuvable aux dates testées {dates}")
