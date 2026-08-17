#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Decryptage complet notices TED 417026-2026 + 850945-2025.
Usage : python3 scripts/explore_smda10.py
"""
import re
import html

for n in ("417026-2026", "850945-2025"):
    t = open(f"/tmp/expl_smda_{n}.xml", encoding="utf-8", errors="ignore").read()
    print(f"\n{'='*70}\nNOTICE {n} ({len(t)} o)")
    txt = re.sub(r"<[^>]+>", "|", t)
    txt = re.sub(r"\|+", "|", txt)
    txt = html.unescape(txt)
    lines = [l.strip() for l in txt.split("|") if l.strip()]
    # contexte : afficher tout ce qui suit le titre / InternalID
    for i, l in enumerate(lines):
        if re.search(r"(g[ée]nie|écol|compensat|terrassement|Canal Seine|Seine-Nord|2\.1|2\.2|secteur 2|Lots? A|Lots? B|Lots? C|SMDA|SOINS|PINSON|montant|Valeur)", l, re.I) and len(l) > 4:
            ctx = lines[max(0, i-1):i+2]
            print("  |", " / ".join(ctx)[:260])
