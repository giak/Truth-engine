#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Avis TOARC MOE 18-50453 (AAPC) + 19-178514 (attribution) : téléchargement DILA + extraction.
Usage : python3 scripts/explore_a3c.py
"""
import os
import re
import html
import subprocess

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

CANDIDATS = {
    "18-50453": ["2018/04/15", "2018/04/14", "2018/04/16"],
    "19-178514": ["2019/12/05", "2019/12/04", "2019/12/06"],
}

def try_download(idweb, date, out):
    for base in (
        f"https://echanges.dila.gouv.fr/OPENDATA/BOAMP/FluxHistorique/Boamp_v240/{date}/{idweb}.xml",
    ):
        subprocess.run(["curl", "-s", "-L", "--max-time", "50", "-A", UA, base, "-o", out],
                       capture_output=True)
        if os.path.exists(out) and os.path.getsize(out) > 1000:
            print(f"  OK [{os.path.getsize(out)} o] {base}")
            return True
    return False

def clean(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()

def extract(f):
    t2 = clean(open(f, encoding="utf-8", errors="ignore").read())
    print(f"\n===== {f} =====")
    for pat in ("Type de procédure", "Accord-cadre", "Nombre maximal", "Date limite de réception",
                "Durée", "Valeur estimée", "Montant", "Critères d'attribution", "Pondération",
                "Marchés subséquents", "remise en concurrence", "Attributaire", "Lauréat",
                "Nb max", "titulaires", "Opérateur économique", "Quantité maximale",
                "reconduction", "Renouvellement"):
        for m in re.finditer(r".{0,80}" + pat + r".{0,250}", t2, re.I):
            print(f"[{pat}]:", m.group(0)[:330])
            break

for idweb, dates in CANDIDATS.items():
    out = f"/tmp/toarc_{idweb}.xml"
    ok = False
    for d in dates:
        if try_download(idweb, d, out):
            ok = True
            break
    if ok:
        extract(out)
    else:
        print(f"\n=== {idweb} : introuvable aux dates {dates}")
