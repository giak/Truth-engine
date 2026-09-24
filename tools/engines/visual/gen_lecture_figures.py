#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Page de relecture des figures Insee : HTML autonome, SVG inlinés.

Objet : voir les figures telles qu'elles seront lues (une par écran, légende
numérotée), sans dépendre d'un chemin de fichier ni d'un serveur. Chaque figure
porte son numéro, sa légende et son pied de provenance, comme dans l'article.

Usage : python3 tools/engines/visual/gen_lecture_figures.py
Sortie : articles/2026-09-23_insee_V5/LECTURE_FIGURES.html
"""

import os
import re

SRC = "articles/2026-09-23_06-00_insee-v5-v38_ce-que-linsee-ne-vous-dira-jamais_ARTICLE.md"
FIGDIR = "articles/2026-09-23_insee_V5/figures/svg"
OUT = "articles/2026-09-23_insee_V5/LECTURE_FIGURES.html"

with open(SRC, encoding="utf-8") as fh:
    article = fh.read()

ordered = [os.path.basename(m.group(1))
           for m in re.finditer(r"\((2026-09-23_insee_V5/figures/svg/[^)]+\.svg)\)", article)]
captions = {}
for m in re.finditer(r"!\[([^\]]+)\]\((2026-09-23_insee_V5/figures/svg/[^)]+\.svg)\)", article):
    captions[os.path.basename(m.group(2))] = m.group(1)

parts = ["""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<title>Figures — L'Insee publie, il n'explique pas (V5)</title>
<style>
  body{margin:0;background:#e9e9e9;font-family:Georgia,"Times New Roman",serif;color:#111}
  .wrap{max-width:1500px;margin:0 auto;padding:40px 24px 80px}
  h1{font-size:30px;font-weight:500;margin:0 0 6px}
  .intro{font-size:15px;color:#444;margin:0 0 34px}
  figure{margin:0 0 46px;background:#fff;border:1px solid #111;padding:18px}
  figure svg{width:100%;height:auto;display:block}
  figcaption{font-size:15px;color:#111;margin-top:14px;padding-top:10px;border-top:1px solid #ccc}
  .meta{font-size:13px;color:#666;margin-top:6px}
</style></head><body><div class="wrap">
<h1>Figures du dossier Insee — version de relecture</h1>
<p class="intro">Six figures, dans l'ordre où l'article les appelle : une tous les mille mots environ.
Contrôle mécanique des chiffres : <code>tools/engines/visual/check_figures_insee.py</code>.
Versions antérieures conservées dans <code>figures/svg/archive/</code>.</p>
"""]

for name in ordered:
    path = os.path.join(FIGDIR, name)
    if not os.path.exists(path):
        continue
    with open(path, encoding="utf-8") as fh:
        svg = fh.read()
    svg = re.sub(r"<\?xml[^>]*\?>\s*", "", svg)
    cap = captions.get(name, name)
    parts.append('<figure>%s<figcaption><strong>%s</strong>'
                 '<div class="meta">fichier %s</div></figcaption></figure>'
                 % (svg, cap, name))

parts.append("</div></body></html>")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as fh:
    fh.write("\n".join(parts))
print(os.path.getsize(OUT), OUT, "| figures :", len(ordered))
