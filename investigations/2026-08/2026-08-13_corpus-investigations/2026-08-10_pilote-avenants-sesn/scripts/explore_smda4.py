#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lecture detaillee des notices TED candidates AAPC genie ecologique secteur 2.
Usage : python3 scripts/explore_smda4.py
"""
import re

for n in ("676593-2025", "730066-2025"):
    t = open(f"/tmp/expl_smda_{n}.xml", encoding="utf-8", errors="ignore").read()
    print(f"\n{'='*70}\nNOTICE {n} ({len(t)} o)")
    # type de procede / titre / objet
    for m in re.finditer(r"<(?:cbc:Description|efbc:Title)>([^<]{10,400})</", t):
        print("  TEXTE:", m.group(1)[:300])
    print("  --- detail 1 (debut) ---")
    txt = re.sub(r"<[^>]+>", "|", t)
    txt = re.sub(r"\|+", "|", txt)
    print(txt[:2200])
