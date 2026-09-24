#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Version de lecture du masterwork : HTML autonome, figures incorporées, paragraphes numérotés.

Objet : donner à l'auteur un support confortable pour la passe de ciselure (relecture à voix
haute). L'article de publication reste ARTICLE_MASTERWORK_SOUVERAINETE_2026.md : ce fichier
n'en est qu'une mise en page, régénérable à chaque édition.

Décisions de mise en page :
- le corps (prologue → épilogue) est rendu en premier, chaque paragraphe de prose numéroté
  dans la marge, afin que l'auteur puisse désigner un défaut par son numéro ;
- les figures sont incorporées en base64 : le fichier ne dépend d'aucun chemin ;
- le registre des pièces vient en fin, en corps réduit et déclaré « à ne pas lire » : c'est de
  l'appareil, pas de la prose, mais il reste contrôlable ;
- la ponctuation et les caractères typographiques de l'article ne sont pas touchés.

Usage : python3 gen_lecture_html.py   (depuis la racine du dépôt)
"""
import base64
import hashlib
import os
import re

SRC = "articles/AUDIT_ARTICLE_POUVOIR_V4_4_FULL_FORENSIC/01_TARGET/ARTICLE_MASTERWORK_SOUVERAINETE_2026.md"
OUT = "articles/AUDIT_ARTICLE_POUVOIR_V4_4_FULL_FORENSIC/01_TARGET/LECTURE_MASTERWORK_2026-09-15.html"
BASE = os.path.dirname(SRC)

IMGSVG = re.compile(r"^!\[(.*?)\]\((.*?)\)\s*$")
ENTRY = re.compile(r"^- \*\*\[\d+\]\*\*")
BULLET = re.compile(r"^- (.*)$")
NUMITEM = re.compile(r"^(\d+)\. (.*)$")


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline(t):
    t = esc(t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", t)
    return t.replace("*", "")


def img64(path):
    p = os.path.join(BASE, path)
    with open(p, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


def main():
    src = open(SRC, encoding="utf-8").read()
    md5 = hashlib.md5(src.encode("utf-8")).hexdigest()
    lines = src.split("\n")

    body, register = [], []
    in_register = False
    for ln in lines:
        if ENTRY.match(ln):
            in_register = True
        (register if in_register else body).append(ln)

    out, para_n = [], 0
    open_ul = open_ol = False
    i = 0

    def close_lists():
        nonlocal open_ul, open_ol
        if open_ul:
            out.append("</ul>")
            open_ul = False
        if open_ol:
            out.append("</ol>")
            open_ol = False

    while i < len(body):
        ln = body[i].rstrip()
        nxt = body[i + 1].strip() if i + 1 < len(body) else ""

        m = IMGSVG.match(ln)
        if m:
            close_lists()
            alt, path = m.group(1), m.group(2)
            kind = "png" if path.endswith(".png") else "svg+xml"
            out.append(
                '<figure><img alt="%s" src="data:image/%s;base64,%s">'
                '<figcaption>%s</figcaption></figure>' % (esc(alt), kind, img64(path), esc(alt))
            )
            i += 1
            continue

        if not ln.strip():
            close_lists()
            i += 1
            continue

        if ln.startswith("### "):
            close_lists()
            out.append("<h3>%s</h3>" % inline(ln[4:]))
        elif ln.startswith("## "):
            close_lists()
            out.append("<h2>%s</h2>" % inline(ln[3:]))
        elif ln.startswith("# "):
            close_lists()
            out.append("<h1>%s</h1>" % inline(ln[2:]))
        elif ln.strip() == "---":
            close_lists()
            out.append('<hr>')
        elif BULLET.match(ln):
            if not open_ul:
                close_lists()
                out.append("<ul>")
                open_ul = True
            out.append("<li>%s</li>" % inline(BULLET.match(ln).group(1)))
        elif NUMITEM.match(ln):
            if not open_ol:
                close_lists()
                out.append("<ol>")
                open_ol = True
            out.append("<li>%s</li>" % inline(NUMITEM.match(ln).group(2)))
        else:
            # paragraphe : on agrège les lignes non vides consécutives
            buf = [ln]
            j = i + 1
            while j < len(body) and body[j].strip() and not (
                body[j].startswith("#")
                or body[j].strip() == "---"
                or IMGSVG.match(body[j].rstrip())
                or BULLET.match(body[j].rstrip())
                or NUMITEM.match(body[j].rstrip())
            ):
                buf.append(body[j].rstrip())
                j += 1
            close_lists()
            para_n += 1
            out.append(
                '<p class="prose" data-n="%d"><span class="num">%d</span>%s</p>'
                % (para_n, para_n, inline(" ".join(buf)))
            )
            i = j - 1
        i += 1
    close_lists()

    reg = []
    for ln in register:
        if ln.strip():
            reg.append("<li>%s</li>" % inline(ln[2:]))
    reg_html = "<ul class=\"reg\">%s</ul>" % "\n".join(reg) if reg else ""

    html = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<title>Version de lecture — L'État sous asphyxie</title>
<style>
  :root {{ --ink:#111; --soft:#5b5b5b; --rule:#d8d8d8; }}
  html {{ background:#f4f4f4; }}
  body {{ margin:0 auto; max-width:44rem; padding:5rem 2.2rem 8rem; background:#fff; color:var(--ink);
         font:19px/1.78 "TeX Gyre Termes", Georgia, "Times New Roman", serif; }}
  .notice {{ font:13px/1.6 "TeX Gyre Heros", Arial, sans-serif; color:var(--soft); border:1px solid var(--rule);
             padding:.7rem .9rem; margin:0 0 3rem; }}
  h1 {{ font-size:2.15rem; line-height:1.24; margin:0 0 1.4rem; }}
  h2 {{ font-size:1.5rem; line-height:1.3; margin:3.4rem 0 1.1rem; padding-top:1.2rem; border-top:1px solid var(--rule); }}
  h3 {{ font-size:1.16rem; margin:2.4rem 0 .7rem; }}
  p.prose {{ position:relative; margin:0 0 1.25rem; }}
  p.prose .num {{ position:absolute; left:-3.4rem; width:2.6rem; text-align:right;
                  font:12px/2.6 "TeX Gyre Heros", Arial, sans-serif; color:#b0b0b0; }}
  em {{ font-style:italic; }}
  ul, ol {{ margin:0 0 1.35rem 1.3rem; }}
  li {{ margin:.35rem 0; }}
  figure {{ margin:2.6rem 0; }}
  figure img {{ width:100%; height:auto; border:1px solid var(--rule); }}
  figcaption {{ font:13.5px/1.55 "TeX Gyre Heros", Arial, sans-serif; color:var(--soft); margin-top:.6rem; }}
  hr {{ border:0; border-top:1px solid var(--rule); margin:3rem 0; }}
  a {{ color:#111; }}
  .reghead {{ margin-top:4.5rem; }}
  ul.reg {{ font:14.5px/1.6 "TeX Gyre Termes", Georgia, serif; color:#333; margin-left:1.1rem; }}
  @media print {{ body {{ max-width:none; padding:0; font-size:11.5pt; }} .notice {{ position:static; }}
                  p.prose .num {{ color:#999; }} figure {{ page-break-inside:avoid; }}
                  h2 {{ page-break-after:avoid; }} }}
</style></head><body>
<p class="notice">Version de lecture, générée automatiquement depuis
<code>ARTICLE_MASTERWORK_SOUVERAINETE_2026.md</code> à l'état <code>{md5}</code>. Les numéros en marge désignent
les paragraphes de prose, pour pouvoir nommer un défaut sans ambiguïté. Le registre, en fin de document,
est de l'appareil : il ne se lit pas à voix haute. L'article de publication reste le fichier Markdown.</p>
{body}
<h2 class="reghead">Registre des pièces</h2>
{reg}
</body></html>
""".format(md5=md5[:8] + "…", body="\n".join(out), reg=reg_html)

    open(OUT, "w", encoding="utf-8").write(html)
    print("OK — écrit %s (%d paragraphes de prose, %d entrées de registre, %.2f Mo)."
          % (OUT, para_n, len(reg), os.path.getsize(OUT) / 1048576))


if __name__ == "__main__":
    main()
