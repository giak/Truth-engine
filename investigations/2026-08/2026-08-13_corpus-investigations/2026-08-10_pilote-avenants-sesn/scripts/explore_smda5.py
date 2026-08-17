#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extraire objet/lots/montants des notices TED candidates pour identifier AAPC genie ecologique.
Usage : python3 scripts/explore_smda5.py
"""
import re

NOTICES = [
    "676593-2025", "730066-2025", "850945-2025", "417026-2026",
    "389639-2026", "485750-2026", "502268-2026", "747456-2025",
]

for n in NOTICES:
    path = f"/tmp/expl_smda_{n}.xml"
    try:
        t = open(path, encoding="utf-8", errors="ignore").read()
    except OSError:
        path = f"/tmp/ted_{n}.xml"
        try:
            t = open(path, encoding="utf-8", errors="ignore").read()
        except OSError:
            print(f"{n}: fichier absent")
            continue
    print(f"\n===== {n} =====")
    # InternalID
    ints = sorted(set(re.findall(r'<cbc:ID schemeName="InternalID">([^<]+)</', t)))
    print("  InternalID:", ints[:5])
    # type de notice (CustomizationID)
    cust = re.search(r"CustomizationID>([^<]+)", t)
    print("  Customization:", cust.group(1) if cust else "?")
    # ProcedureType
    for m in re.finditer(r"<(?:cbc:ProcurementTypeCode|cbc:ProcedureCode)[^>]*>([^<]+)</", t):
        pass
    # SecondStage
    ss = re.findall(r"SecondStageIndicator>([^<]+)</", t)
    if ss:
        print("  SecondStage:", ss)
    # descriptions / titres
    for m in re.finditer(r"<(?:cbc:Description|efbc:Title)>([^<]{15,400})</", t):
        d = m.group(1)
        if len(d) > 20:
            print("  TEXTE:", d[:280])
    # montants
    for m in re.finditer(r"<(?:efbc:TotalAmount|efbc:Amount)[^>]*>([^<]+)</", t):
        print("  MONTANT:", m.group(1))
    # lots
    lots = sorted(set(re.findall(r'<cbc:ID schemeName="Lot">([^<]+)</', t)))
    if lots:
        print("  LOTS:", lots[:10])
    # CPV
    cpvs = sorted(set(re.findall(r"<cbc:ItemClassificationCode[^>]*>([^<]+)</", t)))
    print("  CPV:", cpvs[:10])
