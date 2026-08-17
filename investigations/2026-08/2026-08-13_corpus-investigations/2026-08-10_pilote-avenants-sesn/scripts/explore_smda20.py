#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extraire seuil CA + nb max lots des AAPC 25-17720 / 25-38762.
Usage : python3 scripts/explore_smda20.py
"""
import re

for f in ("/tmp/smda_17720.xml", "/tmp/smda_38762.xml"):
    t = open(f, encoding="utf-8", errors="ignore").read()
    print(f"\n===== {f} =====")
    # Seuil CA : chercher des montants dans le contexte du CA annuel
    for m in re.finditer(r"[^<>|]{0,150}chiffre d'affaires[^<>|]{0,400}", t, re.I):
        s = re.sub(r"<[^>]+>", " ", m.group(0))
        s = re.sub(r"\s+", " ", s)
        print("  CA:", s[:320])
    # montants candidats (7-8 chiffres)
    for m in re.finditer(r"\b\d[\d\s]{6,9}(?:[.,]\d{2})?\b", t):
        pass
    # Nb max lots
    for m in re.finditer(r"[^<>|]{0,120}Nombre maximal de lots[^<>|]{0,200}", t, re.I):
        s = re.sub(r"<[^>]+>", " ", m.group(0))
        s = re.sub(r"\s+", " ", s)
        print("  NBMAX:", s[:260])
    # chercher dans le XML brut les montants pres de 'CA'
    for m in re.finditer(r".{0,120}CA.{0,220}", re.sub(r"<[^>]+>", " ", t)):
        s = re.sub(r"\s+", " ", m.group(0))
        if re.search(r"\d{3,}", s):
            print("  CA-ctx:", s[:280])
            break
