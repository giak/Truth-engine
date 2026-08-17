#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Objets complets des id 2706994/2707054/2707074 depuis decp-global.json (ijson).
Usage : python3 scripts/explore_a3l.py
"""
import json
import subprocess

# Vérifier si un dump local des lignes existe déjà
import os
for f in ("data/decp_sesn_raw.csv", "data/decp_sesn_raw_v2.csv"):
    if os.path.exists(f):
        print(f"### {f}")
        import csv
        with open(f, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if row.get("id") in ("2706994", "2707054", "2707074"):
                    print(f"\n[{row.get('id')}]")
                    print("  objet:", row.get("objet"))
                    print("  montant:", row.get("montant"), "| date:", row.get("dateNotification"))
