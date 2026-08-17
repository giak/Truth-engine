#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extraction complete avis 26-37280 : montants par lot, offres, id procedure, titulaires.
Usage : python3 scripts/explore_smda16.py
"""
import re
import html as H

t = open("/tmp/smda_37280.xml", encoding="utf-8", errors="ignore").read()
txt = re.sub(r"<[^>]+>", "|", t)
txt = re.sub(r"\|+", "|", txt)
txt = H.unescape(txt)
lines = [l.strip() for l in txt.split("|") if l.strip()]

print(f"=== AVIS 26-37280 : {len(lines)} segments ===")
for i, l in enumerate(lines):
    if re.search(r"(montant|offres|Offre|TEN|soumission|re[çc]ues|5\b|attribut|SMDA|378998363|EUR|€|Identifiant de la proc|identifiant interne|8f2de|Valeur totale|valeur totale)", l, re.I):
        ctx = [x for x in lines[max(0, i-2):i+3] if x]
        print("  |", " / ".join(ctx)[:230])

print("\n=== Identifiants UUID / procedure ===")
for m in re.finditer(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", t):
    print("  UUID:", m.group(0))
