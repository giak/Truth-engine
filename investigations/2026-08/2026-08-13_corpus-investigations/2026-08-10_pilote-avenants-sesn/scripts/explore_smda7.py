#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inspecter decp-global.json pour les lignes SMDA 2950343/2950348 : identifier
le numero d'avis / identifiant de procedure / references BOAMP-TED.
Usage : python3 scripts/explore_smda7.py
"""
import ijson

PATH = "data/decp-global.json"
TARGETS = {"2950343", "2950348"}

# le fichier est volumineux (1 Go) : on filtre sur l'id exact
found = {}
with open(PATH, "rb") as f:
    parser = ijson.items(f, "marches.item")
    for i, m in enumerate(parser):
        mid = str(m.get("id", ""))
        if mid in TARGETS:
            found[mid] = m
            print(f"--- id {mid} ---")
            for k, v in m.items():
                if v not in (None, "", [], {}):
                    s = str(v)
                    print(f"  {k}: {s[:250]}")
        if len(found) == len(TARGETS):
            break

print("trouve:", list(found.keys()))
