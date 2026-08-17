#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extraction AAPC 25-21716 (Ribécourt) : conditions, critères, montants estimés, DUME.
Usage : python3 scripts/explore_ribecourt5.py
"""
import re
import html

def clean(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()

t = open("/tmp/rib_25-21716.xml", encoding="utf-8", errors="ignore").read()
t2 = clean(t)
print("=== TAILLE:", len(t2))
print()
pats = [
    "Date limite de réception des offres",
    "Durée estimée",
    "Date de début",
    "Durée du marché",
    "Valeur estimée",
    "Montant estimé",
    "Critères d'attribution",
    "Pondération",
    "Chiffre d'affaires",
    "Conditions de participation",
    "Capacité économique",
    "Liste des documents",
    "DUME",
    "Lots",
    "Accord-cadre",
    "Identifiant de l'avis",
    "avis antérieur",
    "Offres électroniques",
    "Langue",
    "Type de procédure",
    "critères de sélection",
]
for p in pats:
    for m in re.finditer(r".{0,90}" + p + r".{0,200}", t2, re.I):
        print(f"[{p}]:", m.group(0)[:300])
        break
