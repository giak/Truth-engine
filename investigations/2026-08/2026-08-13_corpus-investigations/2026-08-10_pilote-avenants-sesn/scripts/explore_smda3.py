#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Telecharger les notices TED candidates et chercher genie ecologique / SMDA.
Usage : python3 scripts/explore_smda3.py
"""
import re
import subprocess

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

NOTICES = [
    "676593-2025", "730066-2025", "850945-2025", "417026-2026",
]


def fetch_udl(notice, out):
    url = f"https://ted.europa.eu/udl?uri=TED:NOTICE:{notice}:XML:FR:HTML"
    subprocess.run(
        ["curl", "-s", "-L", "--max-time", "90", "-A", UA, url, "-o", out],
        capture_output=True,
    )
    try:
        size = len(open(out, "rb").read())
    except OSError:
        size = 0
    print(f"[{notice}] -> {out} ({size} o)")
    return size


def show(notice, out):
    t = open(out, encoding="utf-8", errors="ignore").read()
    print(f"\n===== {notice} =====")
    # acheteur
    for m in re.finditer(r"<(?:cbc:Name|efac:ContractingParty|cac:PartyName)>([^<]{3,90})</", t):
        pass
    names = sorted(set(re.findall(r"<cbc:Name>([^<]{3,90})</cbc:Name>", t)))
    for n in names[:6]:
        print("  NAME:", n)
    # objet / titre
    for m in re.finditer(r"<(?:cbc:Description|efbc:Title)>([^<]{10,250})</", t):
        d = m.group(1)
        if re.search(r"g[ée]nie|écol|45100000|Seine|SMDA|SOINS", d, re.I):
            print("  DESC:", d[:200])
    # CPV
    cpvs = sorted(set(re.findall(r"<cbc:ItemClassificationCode[^>]*>([^<]+)</", t)))
    print("  CPV:", cpvs[:8])
    # recherche cible
    for pat, label in [("g[ée]nie [ée]cologique", "GENIE"), ("45100000", "CPV45"),
                       ("SOINS MODERNES", "SMDA"), ("SMDA", "SMDAx")]:
        hits = len(re.findall(pat, t, re.I))
        if hits:
            print(f"  HIT {label}: {hits}")
    # type de notice + date
    typ = re.search(r"CustomizationID>([^<]+)", t)
    if typ:
        print("  TYPE:", typ.group(1))
    internal = sorted(set(re.findall(r"<cbc:ID schemeName=\"InternalID\">([^<]+)</", t)))
    if internal:
        print("  InternalID:", internal[:4])
    pub = sorted(set(re.findall(r"<cbc:ID schemeName=\"Part\">([^<]+)</", t)))
    if pub:
        print("  Part/Publication:", pub[:4])


for n in NOTICES:
    out = f"/tmp/expl_smda_{n}.xml"
    if fetch_udl(n, out) > 1000:
        show(n, out)
