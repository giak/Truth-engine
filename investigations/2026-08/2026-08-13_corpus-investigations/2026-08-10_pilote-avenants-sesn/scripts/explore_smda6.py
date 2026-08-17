#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Texte lisible complet des notices 676593-2025 / 730066-2025 (AAPC candidates).
Usage : python3 scripts/explore_smda6.py
"""
import re
import html

for n in ("676593-2025", "730066-2025"):
    t = open(f"/tmp/expl_smda_{n}.xml", encoding="utf-8", errors="ignore").read()
    print(f"\n{'='*70}\nNOTICE {n}")
    # strip tags
    txt = re.sub(r"<[^>]+>", "|", t)
    txt = re.sub(r"\|+", "|", txt)
    txt = html.unescape(txt)
    lines = [l.strip() for l in txt.split("|") if l.strip()]
    # imprimer les segments interessants : contenant des mots-cles
    interesting = [l for l in lines if re.search(
        r"g[ée]nie|écol|45112500|terrassement|Seine|secteur|2\.1|2\.2|Nord|Sud|SMDA|SOINS|offre|lot|montant|201|202|Valeur|value", l, re.I)]
    seen = set()
    for l in interesting:
        if l not in seen and len(l) > 3:
            seen.add(l)
            print("  |", l[:220])
