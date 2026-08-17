#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extraire seuil CA + nb max lots + conditions de capacité des AAPC 25-17720 / 25-38762.
Usage : python3 scripts/explore_smda21.py
"""
import re, html

def clean(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()

for f in ("/tmp/smda_25-17720.xml", "/tmp/smda_25-38762.xml"):
    t = open(f, encoding="utf-8", errors="ignore").read()
    t2 = clean(t)
    print(f"\n===== {f} =====")
    # 1. Chiffre d'affaires / capacité économique
    for m in re.finditer(r".{0,160}(?:chiffre d'affaires|chiffre d affaires|CA annuel|capacité économique|capacite economique|référence de niveau|reference de niveau).{0,400}", t2, re.I):
        print("  CA:", m.group(0)[:420])
    # 2. Montants candidats isolés proches de mentions de capacité (montants >= 1 M€)
    for m in re.finditer(r"\b\d{1,3}(?:\s?\d{3}){1,3}(?:[.,]\d{2})?\s*(?:€|EUR|euros)\b", t2):
        v = m.group(0)
        n = int(re.sub(r"[^\d]", "", v.replace(",", ".").split(".")[0])) if re.search(r"\d", v) else 0
        if n >= 100000:
            print("  MONTANT:", v, "| ctx:", t2[max(0, m.start()-120):m.end()+40][:220])
    # 3. Nombre maximal de lots
    for m in re.finditer(r".{0,160}Nombre maximal de lots.{0,300}", t2, re.I):
        print("  NBMAX:", m.group(0)[:380])
    # 4. Conditions de participation / capacités exigées (blocs)
    for m in re.finditer(r".{0,60}(?:conditions de participation|niveau\(x\) spécifique\(s\) minimal\(aux\) exigé\(s\)|critères de sélection|Criteres de selection).{0,600}", t2, re.I):
        print("  COND:", m.group(0)[:600])
