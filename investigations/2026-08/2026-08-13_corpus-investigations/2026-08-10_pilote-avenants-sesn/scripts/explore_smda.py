#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recherche des avis BOAMP/TED des 2 marches SMDA (genie ecologique secteur 2).
Usage : python3 scripts/explore_smda.py [etape]
"""
import re
import subprocess
import sys

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"


def curl(url, out, timeout=50, ua=UA):
    r = subprocess.run(
        ["curl", "-s", "-L", "--max-time", str(timeout), "-A", ua, url, "-o", out],
        capture_output=True, text=True,
    )
    return r.returncode


def fetch(url, out, timeout=50):
    code = curl(url, out, timeout)
    try:
        size = len(open(out, "rb").read())
    except OSError:
        size = 0
    print(f"[HTTP {code}] {url} -> {out} ({size} o)")
    return size


etape = sys.argv[1] if len(sys.argv) > 1 else "1"

if etape == "1":
    # Page SCSNE : chercher genie ecologique / SMDA / liens
    size = fetch("https://www.canal-seine-nord-europe.fr/marches-publics/", "/tmp/scsne_md.html")
    if size:
        t = open("/tmp/scsne_md.html", encoding="utf-8", errors="ignore").read()
        print("=== occurrences genie ecologique / SMDA / 45100000 ===")
        for m in re.finditer(r"[^<]{0,100}(?:g[ée]nie [ée]cologique|SMDA|SOINS MODERNES|45100000|2\.1|2\.2)[^<]{0,100}", t, re.I):
            print("  |", re.sub(r"\s+", " ", m.group(0))[:200])
        print("=== liens PDF/avis ===")
        for m in sorted(set(re.findall(r'https?://[^"\'\s]+(?:pdf|xml)[^"\'\s]*', t)))[:15]:
            print("  ", m)
        print("=== liens idweb BOAMP ===")
        for m in sorted(set(re.findall(r"\d{2}-\d{6}", t)))[:20]:
            print("  ", m)

elif etape == "2":
    # Moteur BOAMP : recherche "genie ecologique" canal seine nord
    size = fetch(
        "https://www.boamp.fr/recherche?query=genie%20ecologique%20seine%20nord&type=marches",
        "/tmp/boamp_smda.html",
    )
    if size:
        t = open("/tmp/boamp_smda.html", encoding="utf-8", errors="ignore").read()
        print("=== liens resultats BOAMP ===")
        for m in sorted(set(re.findall(r'https?://www\.boamp\.fr/[^"\'\s]+', t)))[:20]:
            print("  ", m)
        for m in re.finditer(r"[^<>]{0,80}(?:g[ée]nie|SMDA|Seine[^<>]{0,40})[^<>]{0,80}", t):
            print("  |", re.sub(r"\s+", " ", m.group(0))[:180])

elif etape == "3":
    # Moteur TED
    size = fetch(
        "https://ted.europa.eu/en/search?keyword=g%C3%A9nie%20%C3%A9cologique%20Seine%20Nord&search=1",
        "/tmp/ted_smda.html",
    )
    if size:
        t = open("/tmp/ted_smda.html", encoding="utf-8", errors="ignore").read()
        print("=== occurrences ===")
        for m in re.finditer(r"[^<>]{0,100}(?:g[ée]nie|SMDA|Seine[^<>]{0,30}|45100000)[^<>]{0,100}", t):
            print("  |", re.sub(r"\s+", " ", m.group(0))[:200])
        print("=== liens notices ===")
        for m in sorted(set(re.findall(r"\d{6}-\d{4}", t)))[:20]:
            print("  ", m)

elif etape == "4":
    # Flux DILA 2026 : reperer la plage de numeros autour de mi-avril 2026
    import os
    for jour in ("2026/04/13", "2026/04/14", "2026/04/15", "2026/04/16", "2026/04/17",
                 "2026/04/20", "2026/04/21", "2026/04/22", "2026/04/23", "2026/04/24",
                 "2026/04/27", "2026/04/28", "2026/04/29", "2026/04/30"):
        out = f"/tmp/dila_{jour.replace('/', '_')}.html"
        fetch(f"https://echanges.dila.gouv.fr/OPENDATA/BOAMP/{jour}/", out, timeout=40)
        if os.path.exists(out):
            t = open(out, encoding="utf-8", errors="ignore").read()
            nums = sorted(set(re.findall(r"26-\d{5}", t)))
            print(f"  {jour}: {len(nums)} avis, plage {nums[0] if nums else '-'}..{nums[-1] if nums else '-'}")

elif etape == "5":
    # Flux DILA : telecharger les avis de la plage mi-avril et chercher SMDA / 45100000 / genie
    import os
    jours = ["2026/04/13", "2026/04/14", "2026/04/15", "2026/04/16", "2026/04/17",
             "2026/04/20", "2026/04/21", "2026/04/22", "2026/04/23", "2026/04/24",
             "2026/04/27", "2026/04/28", "2026/04/29", "2026/04/30"]
    found = 0
    for jour in jours:
        out = f"/tmp/dila_{jour.replace('/', '_')}.html"
        if not os.path.exists(out):
            fetch(f"https://echanges.dila.gouv.fr/OPENDATA/BOAMP/{jour}/", out, timeout=40)
        try:
            t = open(out, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        nums = sorted(set(re.findall(r"26-\d{5}", t)))
        for n in nums:
            if found > 120:
                break
            url = f"https://echanges.dila.gouv.fr/OPENDATA/BOAMP/{jour}/{n}.xml"
            fxml = f"/tmp/smda_{n}.xml"
            subprocess.run(["curl", "-s", "--max-time", "25", "-A", UA, url, "-o", fxml], capture_output=True)
            try:
                body = open(fxml, encoding="utf-8", errors="ignore").read()
            except OSError:
                continue
            if re.search(r"g[ée]nie [ée]cologique|45100000|SOINS|SMDA", body, re.I):
                print(f"  HIT {jour} {n}: {len(body)} o")
                obj = re.search(r"<(?:LIBELLE|OBJET|NOMORGANISME|DENOMINATION)>[^<]{0,140}", body)
                if obj:
                    print("     ", obj.group(0))
                found += 1
        if found > 120:
            break
    print(f"total HIT: {found}")

elif etape == "6":
    # recherche par moteur DDG sur les numeros d'avis eventuels
    import os
    for q in ("%22Soins+Modernes+des+Arbres%22+%22Seine-Nord%22",
              "%22SMDA%22+%22g%C3%A9nie+%C3%A9cologique%22+canal",
              "%22g%C3%A9nie+%C3%A9cologique%22+%22secteur+2%22+Seine-Nord"):
        out = f"/tmp/ddg_{q[:20].replace('%', '_')}.html"
        fetch(f"https://html.duckduckgo.com/html/?q={q}", out, timeout=45)
        t = open(out, encoding="utf-8", errors="ignore").read()
        print("=== DDG:", q[:40], "===")
        for m in re.finditer(r'result__a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', t):
            print("  ", re.sub(r"<[^>]+>", "", m.group(2))[:100], "|", m.group(1)[:100])
        for m in re.finditer(r'result__snippet[^>]*>(.*?)</a>', t):
            print("  #", re.sub(r"<[^>]+>", "", m.group(1))[:150])
