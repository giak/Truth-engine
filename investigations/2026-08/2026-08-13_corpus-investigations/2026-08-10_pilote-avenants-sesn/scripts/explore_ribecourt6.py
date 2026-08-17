#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pondérations qualité/prix + niveau CA minimal : AAPC vs attribution Ribécourt.
Usage : python3 scripts/explore_ribecourt6.py
"""
import re
import html

def clean(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()

for f in ("/tmp/rib_25-21716.xml", "/tmp/rib_26-68097.xml"):
    t2 = clean(open(f, encoding="utf-8", errors="ignore").read())
    print(f"\n===== {f} =====")
    # Blocs critères d'attribution complets
    print("--- critères d'attribution ---")
    for m in re.finditer(r"Critère d'attribution.{0,600}", t2):
        print("  ", m.group(0)[:600])
    # Niveau minimal de capacité
    print("--- niveau minimal de capacité ---")
    for m in re.finditer(r"Niveau minimal de capacité.{0,400}", t2, re.I):
        print("  ", m.group(0)[:400])
    # Montants (tous les formats possibles, y compris avec points séparateurs)
    print("--- tous montants >= 100000 ---")
    for m in re.finditer(r"\d[\d\s.,]{6,18}", t2):
        v = m.group(0)
        n = int(re.sub(r"[^\d]", "", v))
        if n >= 100000:
            print("  ", v[:30], "| ctx:", t2[max(0, m.start()-100):m.end()+40][:160])
