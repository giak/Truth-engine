#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase 2 : extraire toutes les cartes SCSNE + lire le PDF 26-14394 (AAPC suppose).
Usage : python3 scripts/explore_smda2.py
"""
import re
import subprocess

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"


def fetch(url, out, timeout=60):
    subprocess.run(
        ["curl", "-s", "-L", "--max-time", str(timeout), "-A", UA, url, "-o", out],
        capture_output=True,
    )
    try:
        size = len(open(out, "rb").read())
    except OSError:
        size = 0
    print(f"[{url[:90]}] -> {out} ({size} o)")
    return size


# 1. Extraire toutes les cartes (titres + liens) de la page SCSNE deja telechargee
t = open("/tmp/scsne_md.html", encoding="utf-8", errors="ignore").read()

print("=== Tous les titres de cartes marchés ===")
for m in re.finditer(r'public-contract-title">([^<]+)</h', t):
    print("  |", re.sub(r"\s+", " ", m.group(1))[:150])

print()
print("=== Toutes les URLs TED notices / BOAMP / detail dans la page ===")
urls = sorted(set(re.findall(r'https?://[^"\'\s<>]+', t)))
ted = [u for u in urls if "ted.europa.eu" in u or "notice" in u]
boamp = [u for u in urls if "boamp" in u]
detail = [u for u in urls if "detail" in u or "annonces" in u]
for u in ted[:30]:
    print("  TED:", u[:120])
for u in boamp[:20]:
    print("  BOAMP:", u[:120])
for u in detail[:20]:
    print("  DETAIL:", u[:120])

# 2. Lire le PDF BOAMP 26-14394 (fev 2026)
print()
print("=== PDF BOAMP 26-14394 ===")
size = fetch("https://www.boamp.fr/telechargements/FILES/PDF/2026/02/26-14394.pdf", "/tmp/boamp_26-14394.pdf")
if size:
    subprocess.run(["pdftotext", "-layout", "/tmp/boamp_26-14394.pdf", "/tmp/boamp_26-14394.txt"], capture_output=True)
    txt = open("/tmp/boamp_26-14394.txt", encoding="utf-8", errors="ignore").read()
    print(f"  texte: {len(txt)} chars")
    print(txt[:2500])

# 3. Chercher dans le HTML brut des cartes la structure : nom de marche + notice + idweb
print()
print("=== Blocs carte : nom + liens associes (echantillon) ===")
# on cherche les blocs <h3 ...>...</h3> suivis de liens
blocks = re.findall(r'public-contract-title">([^<]+)</h3>(.{0,1200})', t, re.S)
for name, body in blocks[:20]:
    name = re.sub(r"\s+", " ", name).strip()
    links = sorted(set(re.findall(r'https?://[^"\'\s<>]+', body)))
    tedl = [u for u in links if "ted" in u]
    boaml = [u for u in links if "boamp" in u]
    print(f"  {name[:80]}")
    for u in tedl[:2]:
        print(f"      TED: {u[:110]}")
    for u in boaml[:2]:
        print(f"      BOAMP: {u[:110]}")
