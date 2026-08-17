#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Afficher la structure brute du JSON donnees TOARC (clés en majuscules).
Usage : python3 scripts/explore_a3j.py
"""
import json

for f in ("/tmp/toarc_18-50453_donnees.json", "/tmp/toarc_19-178514_donnees.json"):
    print(f"\n===== {f} =====")
    d = json.load(open(f, encoding="utf-8"))
    print(json.dumps(d, ensure_ascii=False, indent=1)[:8000])
