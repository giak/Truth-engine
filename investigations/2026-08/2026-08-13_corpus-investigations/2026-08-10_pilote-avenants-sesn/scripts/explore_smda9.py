#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tester les routes de recherche BOAMP/TED pour l'AAPC + attribution SMDA.
Usage : python3 scripts/explore_smda9.py
"""
import re
import subprocess
import urllib.parse

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"


def fetch(url, out, timeout=60):
    r = subprocess.run(
        ["curl", "-s", "-L", "--max-time", str(timeout), "-A", UA, url, "-o", out],
        capture_output=True,
    )
    try:
        size = len(open(out, "rb").read())
    except OSError:
        size = 0
    print(f"[{size:>7} o] {url[:130]}")
    return size


def txt(out):
    try:
        return open(out, encoding="utf-8", errors="ignore").read()
    except OSError:
        return ""


def show_hits(t, label, pats):
    for pat in pats:
        hits = len(re.findall(pat, t, re.I))
        if hits:
            print(f"   HIT {label} {pat!r}: {hits}")


# 1. Recherche BOAMP texte simple
q = urllib.parse.quote("génie écologique secteur 2 Canal Seine-Nord")
fetch(f"https://www.boamp.fr/recherche?query={q}&type=marches", "/tmp/bm_rech1.html")
t = txt("/tmp/bm_rech1.html")
show_hits(t, "BOAMP-texte", [r"g[ée]nie", r"seine", r"45100000", r"aucun", r"r[ée]sultat"])
print("   extrait:", re.sub(r"<[^>]+>", " ", t)[:300])

# 2. Recherche BOAMP par CPV
fetch("https://www.boamp.fr/pages/avis/?q=45100000", "/tmp/bm_cpv.html")
t = txt("/tmp/bm_cpv.html")
show_hits(t, "BOAMP-CPV", [r"g[ée]nie", r"seine", r"45100000", r"SMDA", r"SOINS"])

# 3. Recherche BOAMP idweb (route validee sur la page SCSNE)
fetch("https://www.boamp.fr/pages/avis/?q=idweb:%2226-14394%22", "/tmp/bm_idweb.html")
t = txt("/tmp/bm_idweb.html")
show_hits(t, "BOAMP-idweb", [r"pi[ée]zom", r"d099", r"26-14394"])

# 4. TED recherche par mot-cle (page JS : verifier si contenu present)
fetch("https://ted.europa.eu/en/search?keyword=ecological%20engineering%20Seine%20North&search=1", "/tmp/ted_rech.html")
t = txt("/tmp/ted_rech.html")
show_hits(t, "TED", [r"g[ée]nie", r"seine", r"SMDA", r"results", r"notices"])

# 5. API BOAMP (a tester : endpoints connus)
for u in (
    "https://www.boamp.fr/api/v1/avis?query=genie%20ecologique",
    "https://www.boamp.fr/api/search?query=genie%20ecologique",
):
    fetch(u, "/tmp/bm_api.html")
    t = txt("/tmp/bm_api.html")
    print("   api extrait:", re.sub(r"<[^>]+>", " ", t)[:200])
