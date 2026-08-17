#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lecture structurée des donnees TOARC : procédure, lots, titulaires, durée, montants.
Usage : python3 scripts/explore_a3i.py
"""
import json
import re

def walk(o, path=""):
    """Parcourir récursivement et imprimer les clés intéressantes."""
    if isinstance(o, dict):
        for k, v in o.items():
            p = f"{path}.{k}" if path else k
            if isinstance(v, (dict, list)):
                walk(v, p)
            else:
                s = str(v)
                if re.search(r"(dur|date|montant|valeur|prix|€|eur|titulaire|attributaire|marché|lot|accord|procédure|négoci|publicité|concurrence|an|mois)", s, re.I):
                    print(f"  {p}: {s[:200]}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, f"{path}[{i}]")

for f in ("/tmp/toarc_18-50453_donnees.json", "/tmp/toarc_19-178514_donnees.json"):
    print(f"\n===== {f} =====")
    d = json.load(open(f, encoding="utf-8"))
    walk(d)
