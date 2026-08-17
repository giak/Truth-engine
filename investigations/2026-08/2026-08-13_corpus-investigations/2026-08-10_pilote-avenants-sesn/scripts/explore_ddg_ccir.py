#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recherches DDG : Ports de Lille CCIR + plateforme Ribécourt (URLs + snippets).
Usage : python3 scripts/explore_ddg_ccir.py
"""
import re
import html
import subprocess
import urllib.parse

def ddg(q, n=8):
    url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(q)
    r = subprocess.run(["curl", "-s", "-L", "--max-time", "45", "-A",
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)", url],
                       capture_output=True)
    body = r.stdout.decode("utf-8", errors="ignore")
    # extraire liens + snippets
    results = []
    for m in re.finditer(r'<a[^>]*class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', body):
        href, title = m.group(1), re.sub(r"<[^>]+>", "", m.group(2))
        results.append((html.unescape(href), html.unescape(title)))
    # snippets
    snips = [re.sub(r"<[^>]+>", "", s) for s in re.findall(r'class="result__snippet"[^>]*>(.*?)</a>', body, re.S)]
    for i, (href, title) in enumerate(results[:n]):
        s = html.unescape(snips[i]) if i < len(snips) else ""
        print(f"  [{i+1}] {title[:120]}")
        print(f"      {href[:160]}")
        print(f"      {s[:220]}")
    return len(results)

qs = [
    "Ports de Lille CCIR Hauts-de-France gestion ports fluviaux",
    "CCI Lille Métropole port de Lille concession VNF",
    "Lille Délivrance terminal multimodal gestionnaire CCI",
    "plateforme multimodale Ribécourt canal Seine-Nord Europe quais Oise",
    "Ribécourt-Dreslincourt terminal trimodal ITE SCSNE",
]
for q in qs:
    print(f"\n=== {q} ===")
    try:
        ddg(q)
    except Exception as e:
        print("  ERREUR:", e)
