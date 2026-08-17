#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inspection brute des XML 25-21716 / 26-68097.
Usage : python3 scripts/explore_ribecourt4.py
"""
import re
import html

def clean(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()

t = open("/tmp/rib_26-68097.xml", encoding="utf-8", errors="ignore").read()
t2 = clean(t)
print("=== TAILLE texte propre:", len(t2))
print()
# Chercher toutes les occurrences de chiffres longs (montants possibles)
print("=== séquences chiffres+espaces ===")
for m in re.finditer(r"\d[\d\s.,]{5,20}", t2):
    s = m.group(0)[:40]
    print(" ", repr(s), "| ctx:", t2[max(0, m.start()-80):m.end()+60].replace("\n", " ")[:180])
