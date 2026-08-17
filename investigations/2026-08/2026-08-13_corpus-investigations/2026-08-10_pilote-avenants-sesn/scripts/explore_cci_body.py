#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extraire le corps de l'article CCI Business Ribécourt (après le menu).
Usage : python3 scripts/explore_cci_body.py
"""
import re
import html

t = open("/tmp/cci1.html", encoding="utf-8", errors="ignore").read()
# Zones de contenu : main / article
for tag in ("<main", "<article", "node-content", "field--name-body"):
    i = t.find(tag)
    if i > 0:
        print(f"--- balise {tag} trouvée à {i} ---")
        t2 = t[i:i+60000]
        t2 = re.sub(r"<script[^>]*>.*?</script>", " ", t2, flags=re.S)
        t2 = re.sub(r"<style[^>]*>.*?</style>", " ", t2, flags=re.S)
        t2 = re.sub(r"<[^>]+>", " ", t2)
        t2 = html.unescape(t2)
        t2 = re.sub(r"[ \t]+", " ", t2)
        t2 = re.sub(r"\n\s*\n+", "\n", t2)
        # chercher les paragraphes contenant des mots clés
        for m in re.finditer(r"(?i).{0,100}(ribécourt|trimodale|exploitation|quai|ITE|terminal|CCIR|CCI|desserte|ferr).{0,250}", t2):
            s = " ".join(m.group(0).split())
            print("  *", s[:330])
        break
