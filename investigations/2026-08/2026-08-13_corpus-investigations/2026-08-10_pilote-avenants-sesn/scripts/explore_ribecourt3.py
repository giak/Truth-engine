#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extraction ciblée des XML 25-21716 / 26-68097 : montants, offres, attributaire, durée, DUME.
Usage : python3 scripts/explore_ribecourt3.py
"""
import re
import html

def clean(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()

for f in ("/tmp/rib_25-21716.xml", "/tmp/rib_26-68097.xml"):
    t = open(f, encoding="utf-8", errors="ignore").read()
    t2 = clean(t)
    print(f"\n===== {f} =====")
    # Montants (tous, même petits)
    montants = []
    for m in re.finditer(r"(\d{1,3}(?:\s?\d{3})+(?:[.,]\d{2})?)\s*(€|EUR|euros)", t2):
        v, dev = m.group(1), m.group(2)
        n = int(re.sub(r"[^\d]", "", v.split(".")[0].replace(",", "")))
        ctx = t2[max(0, m.start()-140):m.end()+40]
        montants.append((n, v, ctx))
    seen = set()
    for n, v, ctx in sorted(montants, reverse=True):
        key = (v, ctx[:60])
        if key in seen:
            continue
        seen.add(key)
        print(f"  MONTANT {v} {ctx[:220]}")
    # Nb offres / candidats
    for pat in ("offres reçues", "Offres reçues", "candidatures", "Candidatures", "offres électroniques", "offres ont été"):
        for m in re.finditer(r".{0,80}" + pat + r".{0,120}", t2):
            print("  OFFRES:", m.group(0)[:220])
    # Attributaire / titulaire
    for pat in ("Attributaire", "Titulaire du marché", "Nom national", "Chambre de commerce", "CCIR"):
        for m in re.finditer(r".{0,80}" + pat + r".{0,140}", t2):
            print("  ATTRIB:", m.group(0)[:220])
    # Durée
    for m in re.finditer(r".{0,80}(Durée du marché|durée du marché|48 mois|quarante-huit).{0,120}", t2):
        print("  DUREE:", m.group(0)[:220])
    # Lot / division en lots
    for m in re.finditer(r".{0,60}(divisé en lots|Division en lots|Un seul lot|Pas de lot).{0,120}", t2):
        print("  LOTS:", m.group(0)[:220])
    # Motif de la négociation sans concurrence éventuel (si présent)
    for m in re.finditer(r".{0,100}(sans mise en concurrence|sans publicité|absence de concurrence).{0,200}", t2, re.I):
        print("  NEGOC-SANS-PUB?:", m.group(0)[:280])
