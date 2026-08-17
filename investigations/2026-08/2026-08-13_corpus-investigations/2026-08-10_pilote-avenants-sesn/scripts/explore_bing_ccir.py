#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recherches Bing : Ports de Lille CCIR + plateforme Ribécourt (URLs + snippets).
Usage : python3 scripts/explore_bing_ccir.py
"""
import re
import html
import subprocess
import urllib.parse

def bing(q, n=8):
    url = "https://www.bing.com/search?q=" + urllib.parse.quote(q)
    r = subprocess.run(["curl", "-s", "-L", "--max-time", "45", "-A",
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)", url],
                       capture_output=True)
    body = r.stdout.decode("utf-8", errors="ignore")
    txt = re.sub(r"<script[^>]*>.*?</script>", " ", body, flags=re.S)
    txt = re.sub(r"<style[^>]*>.*?</style>", " ", txt, flags=re.S)
    # liens bing
    links = re.findall(r'<a[^>]*href="(http[^"]+)"[^>]*>(.*?)</a>', txt)
    count = 0
    for href, title in links:
        title = re.sub(r"<[^>]+>", "", title).strip()
        if not title or "bing.com" in href or "microsoft" in href:
            continue
        count += 1
        print(f"  [{count}] {html.unescape(title)[:130]}")
        print(f"      {href[:170]}")
        if count >= n:
            break
    if count == 0:
        # dump texte partiel pour debug
        txt2 = re.sub(r"<[^>]+>", " ", txt)
        txt2 = re.sub(r"\s+", " ", html.unescape(txt2))
        print("  (0 résultats ; texte:", txt2[:300], ")")
    return count

qs = [
    "Ports de Lille CCIR Hauts-de-France gestion ports fluviaux",
    "port de Lille Délivrance terminal multimodal CCI concession VNF",
    "plateforme multimodale Ribécourt canal Seine-Nord quais Oise",
    "CCIR Hauts-de-France plateforme Ribécourt exploitation",
]
for q in qs:
    print(f"\n=== {q} ===")
    try:
        bing(q)
    except Exception as e:
        print("  ERREUR:", e)
