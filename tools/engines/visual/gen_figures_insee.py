#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Générateur déterministe des figures de la V5 Insee (série quasi-LaTeX).

Six figures, pour 6 100 mots de corps : une image tous les mille mots environ.
Le corpus précédent en comptait onze, dont deux collées l'une à l'autre et trois
qui ne faisaient que redire le texte ; le détail des coupes et leurs critères est
consigné dans articles/2026-09-23_09-15_DECISION_FIGURES_INSEE_V5.md.

Convention de nommage : la fonction `figNN` écrit le fichier `figNN_*.svg` et porte
le cartouche `FIG. NN`. Une indexation croisée des deux (fig10 écrivant fig05) ne se
voit qu'au moment de retoucher une figure, c'est-à-dire trop tard.

Design system relevé dans le code des SVG de référence, non dans leur description :
  - articles/2026-08-26/IA_TRAVAIL_ARTICLE_ARCHIVE_2026-08-26/09_REFERENCE_STYLE_FACTCHECK/root_svg/
  - articles/AUDIT_ARTICLE_POUVOIR_V4_4_FULL_FORENSIC/01_TARGET/figures/svg/

Canevas 2400 x 1500, marges 90, header y=78, filet y=112, titre y=214, sous-titre y=278,
panneaux 400 x 380 aux abscisses 70/525/980/1435/1890, bandes étagées de 1780 de large à x=310
avec cellule grise de 250 et hauteurs variables (comme fig09_cascade_verite.svg), filet final
y=1410, pied y=1460. Latin Modern Roman/Sans, palette #111111 / #3d3d3d / #444444 / #555555 /
#f3f3f3, traits 2.4 / 1.7 / 3. Angles droits, aucun arrondi, aucune ombre.

Mise en page : chaque bloc calcule sa propre hauteur et ajuste ses corps de texte
(`fit` pour l'horizontal, centrage vertical pour le vertical). Après la première
génération, un simple contrôle XML ne suffit pas : il faut regarder la page de
relecture (`gen_lecture_figures.py`), parce que le chevauchement de deux textes est
invisible pour un parseur.

Aucune valeur numérique n'est inventée : toutes proviennent de
articles/2026-09-23_06-00_insee-v5-v38_ce-que-linsee-ne-vous-dira-jamais_ARTICLE.md.
Contrôle : tools/engines/visual/check_figures_insee.py.

Les versions antérieures des figures restent sur disque dans
articles/2026-09-23_insee_V5/figures/svg/archive/ : ce dossier est une trace, il n'est
ni généré ni contrôlé.

Usage : python3 tools/engines/visual/gen_figures_insee.py
"""

import os

W, H = 2400, 1500
MX = 90
SERIF = '"Latin Modern Roman","LM Roman 10","TeX Gyre Termes","Times New Roman",serif'
SANS = '"Latin Modern Sans","LM Sans 10","TeX Gyre Heros",Arial,sans-serif'
INK, INK2, NOTE, THIN, PANEL = "#111111", "#3d3d3d", "#444444", "#555555", "#f3f3f3"
RULE, FIN, ARROW = 2.4, 1.7, 3.0
OUT = "articles/2026-09-23_insee_V5/figures/svg"

# largeur moyenne d'un caractère, en fraction de la taille de police (relevé à l'œil
# sur les références : Latin Modern Sans est plus étroit que le serif)
CW_SANS, CW_SERIF = 0.56, 0.54
TRACK = 1.3  # interlettrage des libellés (.tag), compté dans la largeur estimée


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def fit(s, avail, size, serif=False, tracking=0.0):
    """Réduit la taille de police si la ligne dépasse la largeur disponible."""
    est = len(s) * (size * (CW_SERIF if serif else CW_SANS) + tracking)
    if est <= avail:
        return size
    return max(15, int(size * avail / est))


def txt(x, y, s, cls, anchor="start", avail=None, size=None, serif=False, tracking=0.0):
    a = ' text-anchor="%s"' % anchor if anchor != "start" else ""
    st = ""
    if avail and size:
        st = ' style="font-size:%spx"' % fit(s, avail, size, serif, tracking)
    elif size:
        st = ' style="font-size:%spx"' % size
    return '<text x="%s" y="%s" class="%s"%s%s>%s</text>' % (x, y, cls, a, st, esc(s))


def wrap(s, n):
    words, lines, cur = s.split(), [], ""
    for w_ in words:
        cand = (cur + " " + w_).strip()
        if len(cand) <= n:
            cur = cand
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def rect(x, y, w, h, fill="#ffffff", stroke=INK, sw=RULE, hatch=False):
    f = "url(#hatch)" if hatch else fill
    st = ' stroke="%s" stroke-width="%s"' % (stroke, sw) if stroke else ""
    return '<rect x="%s" y="%s" width="%s" height="%s" fill="%s"%s/>' % (x, y, w, h, f, st)


def hline(x1, x2, y, sw=RULE, stroke=INK):
    return '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"/>' % (x1, y, x2, y, stroke, sw)


def vline(x, y1, y2, sw=RULE, stroke=INK):
    return '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"/>' % (x, y1, x, y2, stroke, sw)


def arrow_r(x1, x2, y):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#arrow)"/>' % (x1, y, x2, y, INK, ARROW))


def arrow_d(x, y1, y2):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#arrow)"/>' % (x, y1, x, y2, INK, ARROW))


def dot(x, y, r=9):
    return '<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (x, y, r, INK)


def head(kicker, kicker_r, title, sub, desc):
    p = [rect(0, 0, W, H, fill="#ffffff", stroke=None)]
    p.append(txt(MX, 78, kicker, "kicker"))
    p.append(txt(2310, 78, kicker_r, "kicker", "end"))
    p.append(hline(MX, 2310, 112))
    p.append(txt(1200, 214, title, "title", "middle", avail=2200, size=60, serif=True))
    for i, line in enumerate(sub):
        p.append(txt(1200, 278 + i * 38, line, "sub", "middle", avail=2200, size=29, serif=True))
    p.append('<desc>%s</desc>' % esc(desc))
    return p


def panel(x, y, w, h, tag, head_lines=(), body_lines=(), small_lines=(),
          note=None, fill="#ffffff", badge=None, hatch=False):
    """Panneau à grille de référence : tag, filet, bloc centré verticalement, note en pied."""
    p = [rect(x, y, w, h, fill=fill, hatch=hatch)]
    p.append(txt(x + 30, y + 46, tag, "tag", avail=w - 60, size=24))
    p.append(hline(x + 30, x + w - 30, y + 70, FIN, THIN))
    top = y + 96
    if badge:
        p.append(rect(x + 30, top, w - 60, 36, hatch=True, stroke=None))
        p.append(txt(x + w / 2, top + 26, badge, "small", "middle", avail=w - 80, size=22))
        top += 56
    bottom = y + h - (56 if note else 20)
    hs, bs, ss = 44, 40, 32
    gap_hb, gap_bs = 26, 20
    def block_h(hs_, bs_, ss_, g1, g2):
        return (len(head_lines) * hs_ + (g1 if head_lines and (body_lines or small_lines) else 0)
                + len(body_lines) * bs_ + (g2 if body_lines and small_lines else 0)
                + len(small_lines) * ss_)

    avail = bottom - top
    total = block_h(hs, bs, ss, gap_hb, gap_bs)
    if total > avail:
        # 1) les gouttières d'abord, 2) puis les corps, un point à la fois. Une compression
        # proportionnelle suivie d'un plancher ne revérifie rien : le bloc débordait et
        # venait toucher la note de pied (constat de rendu, FIG. 07, trois lignes de note).
        while total > avail and (gap_hb or gap_bs):
            gap_hb, gap_bs = max(0, gap_hb - 2), max(0, gap_bs - 2)
            total = block_h(hs, bs, ss, gap_hb, gap_bs)
        while total > avail and (hs > 30 or bs > 26 or ss > 20):
            hs, bs, ss = max(30, hs - 1), max(26, bs - 1), max(20, ss - 1)
            total = block_h(hs, bs, ss, gap_hb, gap_bs)
    cy = top + (avail - total) / 2.0
    for line in head_lines:
        cy += hs
        p.append(txt(x + w / 2, cy, line, "head", "middle", avail=w - 60, size=35, serif=True))
    cy += gap_hb
    for line in body_lines:
        cy += bs
        p.append(txt(x + w / 2, cy, line, "body", "middle", avail=w - 50, size=26))
    cy += gap_bs
    for line in small_lines:
        cy += ss
        p.append(txt(x + w / 2, cy, line, "small", "middle", avail=w - 50, size=22))
    if note:
        p.append(txt(x + w / 2, y + h - 28, note, "note", "middle", avail=w - 50, size=24, serif=True))
    return p


def band(x, y, w, h, label_lines, body_lines=(), sub=None, sub_lines=(), right=None,
         verdict_note=None, hatch_verdict=False, label_w=250, right_w=330):
    """Bande étagée : cellule grise de gauche, corps à gauche, valeur à droite."""
    p = [rect(x, y, w, h)]
    p.append(rect(x, y, label_w, h, fill=PANEL, stroke=None))
    p.append(vline(x + label_w, y, y + h, RULE, INK))
    ly = y + h / 2.0 - (len(label_lines) - 1) * 17 + 9
    for line in label_lines:
        p.append(txt(x + 24, ly, line, "tag", avail=label_w - 44, size=24, tracking=TRACK))
        ly += 34
    subs = list(sub_lines) + ([sub] if sub else [])
    body_x = x + label_w + 30
    body_avail = w - label_w - 60 - (right_w if right else 10)
    # empilement homogène : chaque ligne consomme sa propre hauteur, la dernière
    # baseline reste à l'intérieur du cadre (défaut corrigé après constat au rendu)
    lines = [("body", l, 26, 38, False) for l in body_lines] + \
            [("note", l, 23, 30, True) for l in subs]
    total = sum(x[3] for x in lines) or 38
    cur = y + (h - total) / 2.0 + 26
    for cls, line, size, lh, ser in lines:
        p.append(txt(body_x, cur, line, cls, avail=body_avail, size=size, serif=ser))
        cur += lh
    if right:
        if hatch_verdict:
            p.append(rect(x + w - right_w - 10, y + 6, right_w, h - 12, hatch=True, stroke=None))
        vx = x + w - 24
        if verdict_note:
            p.append(txt(vx, y + h / 2.0 - 2, right, "verdict", "end", avail=right_w - 20, size=28, serif=True))
            p.append(txt(vx, y + h / 2.0 + 34, verdict_note, "small", "end",
                         avail=right_w - 20, size=20))
        else:
            p.append(txt(vx, y + h / 2.0 + 10, right, "verdict", "end",
                         avail=right_w - 20, size=28, serif=True))
    return p


def synthesis(y, lines, h, serif=None):
    p = [rect(MX, y, W - 2 * MX, h, fill=PANEL)]
    cy = y + (h - len(lines) * 46) / 2.0 + 34
    for line in lines:
        p.append(txt(1200, cy, line, "synth", "middle", avail=W - 2 * MX - 60, size=34, serif=True))
        cy += 46
    if serif:
        p.append(txt(1200, min(y + h + 104, 1330), serif, "concl", "middle",
                     avail=W - 2 * MX, size=48, serif=True))
    return p


def concl(y, text):
    return [txt(1200, y, text, "concl", "middle", avail=W - 2 * MX, size=48, serif=True)]


def footer(left, right):
    p = [hline(MX, 2310, 1410)]
    p.append(txt(MX, 1460, left, "small", size=22, avail=W - 2 * MX - 620))
    p.append(txt(2310, 1460, right, "small", "end", size=22, avail=620))
    return p


def figure(name, kicker, kicker_r, title, sub, desc, parts, foot_l, foot_r):
    p = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<svg xmlns="http://www.w3.org/2000/svg" width="%s" height="%s" viewBox="0 0 %s %s" '
         'role="img" aria-labelledby="title desc">' % (W, H, W, H)]
    p.append('<title>%s</title>' % esc(title))
    p.append('<defs>')
    p.append('<marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4.5" '
             'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L9,4.5 L0,9 Z" fill="%s"/></marker>' % INK)
    p.append('<pattern id="hatch" width="14" height="14" patternUnits="userSpaceOnUse" '
             'patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="14" '
             'stroke="#c8c8c8" stroke-width="4"/></pattern>')
    p.append('<style><![CDATA[')
    p.append('  .rm{font-family:%s;fill:%s;}' % (SERIF, INK))
    p.append('  .sf{font-family:%s;fill:%s;}' % (SANS, INK))
    p.append('  .kicker{font-size:27px;letter-spacing:2.6px;font-weight:700;}')
    p.append('  .title{font-size:60px;font-weight:500;}')
    p.append('  .sub{font-size:29px;fill:%s;}' % INK2)
    p.append('  .tag{font-size:24px;font-weight:700;letter-spacing:1.3px;}')
    p.append('  .head{font-size:35px;font-weight:500;}')
    p.append('  .body{font-size:26px;}')
    p.append('  .small{font-size:22px;fill:%s;}' % NOTE)
    p.append('  .note{font-size:24px;font-style:italic;fill:%s;}' % NOTE)
    p.append('  .synth{font-size:34px;}')
    p.append('  .concl{font-size:48px;font-weight:500;}')
    p.append('  .verdict{font-size:28px;font-weight:500;}')
    p.append(']]></style>')
    p.append('</defs>')
    p += head(kicker, kicker_r, title, sub, desc)
    p += parts
    p += footer(foot_l, foot_r)
    p.append('</svg>')
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(p) + "\n")
    return path


X5 = [70, 525, 980, 1435, 1890]
X4 = [318, 773, 1228, 1683]
INSEE = "DOSSIER INSEE"


# --------------------------------------------------------------------------- FIG 01
def fig01():
    y, w, h = 390, 400, 380
    p = []
    p += panel(X5[0], y, w, h, "1  DÉFINIR", ["Chômeur", "au sens du BIT"],
               ["sans emploi", "disponible", "en recherche active"],
               ["110 000 personnes", "interrogées par trimestre"],
               "4 définitions concurrentes")
    p += panel(X5[1], y, w, h, "2  MESURER", ["8,3 % ± 0,3"],
               ["le niveau et son évolution", "portent la même marge"],
               ["« +/- 0,3 point près »", "légende du tableau"],
               "la marge est produite", fill=PANEL)
    p += panel(X5[2], y, w, h, "3  PUBLIER", ["Information", "rapide n° 192"],
               ["7 août 2026", "le matin"],
               ["la publication suivante", "est annoncée à 07h30"],
               "l'heure est un rituel")
    p += panel(X5[3], y, w, h, "4  REPRENDRE", ["Dépêche,", "puis titres"],
               ["dépêche horodatée 08h00", "« sixième trimestre", "consécutif, à 8,3% »"],
               ["contrefactuel ministériel :", "7,9 %"],
               "la marge s'arrête ici", fill=PANEL)
    p += panel(X5[4], y, w, h, "5  RESTER", ["Ce qui circule"],
               ["le niveau,", "sans sa marge"],
               ["0 mention sur 19 articles", "la marche d'un trimestre", "tient dans la marge"],
               "aucune pièce cachée trouvée")
    for i in range(4):
        p.append(arrow_r(X5[i] + w + 9, X5[i + 1] - 9, y + h / 2))
    p += synthesis(830, ["Le chiffre naît avec sa marge.", "Il la perd avant le petit déjeuner."],
                   170, "Presque tout est publié. Presque rien n'en est dit.")
    return figure("fig01_chaine_transmission.svg", "FIG. 01  ·  CHAÎNE DE TRANSMISSION", INSEE,
                  "Où le chiffre perd sa marge",
                  ["De la définition internationale au titre de presse, 5 étages,",
                   "et un seul disparaît sans trace."],
                  "Insee IR n° 192 du 7 août 2026 et sa légende ; Mediapart, fil du 7 août 2026 ; "
                  "Le Figaro, 7 août 2026 ; franceinfo, 7 août 2026 ; audit de médiation du 22 septembre 2026.",
                  p,
                  "Sources : Insee, IR n° 192 et légende du tableau ; franceinfo, 7 août 2026 ; Le Figaro, 7 août 2026 ; audit de médiation du 22/09/2026.",
                  "Dossier Insee · 23 septembre 2026")


# --------------------------------------------------------------------------- FIG 02
def fig02():
    p, y = [], 360
    rows = [
        (["MESURE 1", "BIT"], ["sans emploi, disponible, en recherche active"],
         "mesuré auprès de 110 000 personnes par trimestre", "2,23 M"),
        (["MESURE 2", "HALO"], ["souhaite travailler sans remplir tous les critères"],
         "inférieur au BIT : les ensembles se recoupent sans s'emboîter", "1,86 M"),
        (["MESURE 3", "CATÉGORIE A"], ["inscrits sur les listes de Pôle emploi, devenu France Travail"],
         "mesure administrative, et la plus haute des deux mesures du chômage", "3,14 M"),
        (["MESURE 4", "RECENSEMENT"], ["auto-déclaration de 14 à 70 ans"],
         "réservée aux comparaisons de structure : non comparable en niveau", "plus élevé"),
    ]
    for lab, body, sub, right in rows:
        p += band(310, y, 1780, 126, lab, body, sub=sub, right=right, label_w=250, right_w=280)
        y += 140
    p.append(rect(310, y + 6, 1780, 150, fill=PANEL))
    p.append(txt(340, y + 50, "2010-2022 : LES DEUX MESURES DIVERGENT", "tag", avail=1700, size=24))
    p.append(hline(340, 2060, y + 68, FIN, THIN))
    p.append(txt(340, y + 112, "BIT : moins 2 points", "head", avail=800, size=33, serif=True))
    p.append(txt(2060, y + 112, "catégorie A : plus 5 %", "head", "end", avail=800, size=33, serif=True))
    p.append(txt(340, y + 142, "Écart attribué par le producteur à des réformes intervenant "
                                "« indépendamment de la situation réelle ».",
                 "note", avail=1700, size=23, serif=True))
    p += synthesis(1090, ["4 chiffres officiels, la même année, la même maison.",
                          "Aucun n'est faux. Aucun n'est le même."], 150,
                   "Le mot ne désigne pas un fait : il désigne une convention.")
    return figure("fig02_quatre_nombres.svg", "FIG. 02  ·  LES DÉFINITIONS DU CHÔMAGE", INSEE,
                  "4 nombres officiels pour un seul mot",
                  ["France hors Mayotte, 2022. Les 4 ensembles se recoupent",
                   "partiellement : ils ne s'emboîtent pas."],
                  "Insee Flash Pays de la Loire n° 140, 31 août 2023 ; Insee, page définitions du chômage.",
                  p,
                  "Source : Insee Flash Pays de la Loire n° 140 du 31 août 2023, France hors Mayotte, 2022 ; Insee, définitions du chômage.",
                  "Dossier Insee · 23 septembre 2026")


# --------------------------------------------------------------------------- FIG 03
def fig03():
    """Les 4 vannes d'indexation, chacune datée : la frise des conventions est ici,
    dans le panneau qu'elle concerne, et non dans une seconde figure qui la redirait."""
    p = []
    p += band(310, 340, 1780, 150, ["ENTRÉE", "L'INDICE"],
              ["1 point d'inflation en plus : près de 5 Md€ de dépenses sociales indexées",
               "un dixième de la dette publique est indexé : environ 2,5 Md€ par point"],
              sub="Base indexée : environ 500 Md€ de prestations sociales", label_w=250)
    y, w, h = 570, 400, 430
    for x in X4:
        p.append(arrow_d(x + w / 2, 510, y - 12))
    p += panel(X4[0], y, w, h, "VANNE 1 · 2005", ["Loyers"],
               ["hors tabac, hors loyers", "remplace l'indice du coût", "de la construction en 2006",
                "plafonné à 3,5 % en 2022-2024"],
               ["environ 1,5 à 2 Md€ par an", "vers les locataires"],
               "7 millions de ménages du parc privé")
    p += panel(X4[1], y, w, h, "VANNE 2 · 2026", ["Impôt"],
               ["dérive : 8 années sur 13", "gel voté pour 2026"],
               ["environ 2 Md€ pour l'État", "200 000 foyers imposables"],
               "cumul défavorable : moins 4,1 points", fill=PANEL)
    p += panel(X4[2], y, w, h, "VANNE 3 · 1987", ["Retraites"],
               ["des salaires aux prix", "basculées en 1987"],
               ["environ 4 Md€ par an", "des retraités vers les cotisants"],
               "bascule de la règle d'indexation")
    p += panel(X4[3], y, w, h, "VANNE 4 · 2026", ["Salaire minimum"],
               ["indexé sur l'indice", "des prix, au 1er juin"],
               ["12,31 € l'heure", "depuis le 1er juin 2026"],
               "arrêté du 22 mai 2026", fill=PANEL)
    p += synthesis(1040, ["Aucune de ces vannes n'est tournée par l'institut. L'IRL est défini par la loi,",
                          "le plafond voté par le Parlement, le barème fixé en loi de finances,",
                          "les retraites décidées par décret."], 200,
                   "5 décisions, aucun tourneur commun : la manivelle est dans le droit.")
    return figure("fig03_manivelle.svg", "FIG. 03  ·  L'INDEXATION, UN TRANSFERT", INSEE,
                  "Un dixième de point vaut 500 millions",
                  ["4 conventions, 4 gagnants, aucune direction commune : leur date,",
                   "leur montant, et le fait que l'indice est produit ici, décidé ailleurs."],
                  "DG Trésor, Trésor-Info du 5 juillet 2022 ; FIPECO ; loi n° 2005-841 du 26 juillet 2005 ; "
                  "loi n° 2022-1158, article 12 ; loi de finances pour 2026 ; arrêté du 22 mai 2026 relatif au SMIC.",
                  p,
                  "Sources : Trésor-Info du 05/07/2022 (verbatim « près de 5 Md€ ») ; FIPECO ; loi 2005-841 art. 35 ; loi 2022-1158 art. 12 ; loi de finances pour 2026 ; arrêté SMIC du 22/05/2026.",
                  "Dossier Insee · 23 septembre 2026")


# --------------------------------------------------------------------------- FIG 04
def fig04():
    """Deux régimes d'erreur, et rien d'autre : la frise des trois valeurs de croissance
    est dans le texte, elle n'a pas besoin d'un tiers d'affiche pour être relue."""
    y, h = 390, 620
    p = []
    p += panel(170, y, 980, h, "RÉGIME 1  RÉVISIONS DE CROISSANCE", ["Une révision orientée"],
               ["+ 0,34 point en moyenne", "sur 20 ans, à la hausse"],
               ["le premier chiffre n'est pas faux :", "il est provisoire, ses corrections",
                "vont dans un seul sens"],
               "Rexecode, institut de conjoncture privé", fill=PANEL)
    p += panel(1250, y, 980, h, "RÉGIME 2  SURPRISES DE RECETTES", ["Des erreurs dans les deux sens"],
               ["2025 : 5,4 % prévu, 5,1 % réalisé",
                "déficit : 161 puis 152,5 Md€",
                "30,7 Md€ de recettes, dont 13,0 spontanées"],
               ["2023-2024 : recettes déçues,", "2,6 % contre 6,3 % de PIB nominal"],
               "elles ne s'additionnent pas, elles s'annulent")
    p += synthesis(1050, ["Ce que laissent ces deux régimes d'erreur, ce n'est pas",
                         "un programme, mais un problème de transmission."], 170,
                   "Le chiffre du matin a eu tout le pays.")
    return figure("fig04_revisions.svg", "FIG. 04  ·  RÉVISIONS DES COMPTES", INSEE,
                  "Deux régimes d'erreur qu'il ne faut pas confondre",
                  ["La révision pousse à la hausse ; l'erreur de recettes, elle, va dans les deux sens.",
                   "Plus forte révision depuis 2003, pour une année dont tout le monde avait conclu."],
                  "Comptes de la Nation 2023 et 2024 ; Insee Première n° 2105 et son erratum du 29 mai 2026 ; "
                  "note de révisions du 3 juin 2026 ; Cour des comptes, 22 avril 2026 ; Trésor-Éco n° 356 ; Rexecode.",
                  p,
                  "Sources : comptes 2023 et 2024 ; Insee Première n° 2105 et erratum du 29/05/2026 ; note de révisions du 03/06/2026 ; Cour des comptes du 22/04/2026 ; Rexecode.",
                  "Dossier Insee · 23 septembre 2026")


# --------------------------------------------------------------------------- FIG 05
def fig05():
    """Six bandes étagées, de hauteur variable selon le texte trouvé (comme la référence)."""
    p = []
    rows = [
        (["H1", "MENSONGE"], "espéré : le scandale",
         "trouvé : méthodologies complètes, erratum le jour même, indices alternatifs publiés, "
         "pression ministérielle de 2021 résistée",
         "morte", "absence de contre-preuve, non preuve d'intégrité", False),
        (["H2", "BÉNÉFICIAIRE UNIQUE"], "espéré : le siphon",
         "trouvé : chaque groupe gagne et perd selon la convention et l'année",
         "morte", "survit en version faible : chaque convention a un gagnant", False),
        (["H3", "OPACITÉ"], "espéré : des documents cachés",
         "trouvé : opacité d'expertise, intervalle absent de 19 articles, rapports Eurostat non "
         "publiés, labellisation suspendue",
         "reformulée", "accès différencié, non dissimulation", False),
        (["H4", "PIB MAQUILLÉ"], "espéré : le maquillage",
         "trouvé : PIB 2025 non révisé, surprise venue des recettes",
         "réfutée", "95 % de numérateur, aucun dénominateur", False),
        (["H5", "PÉRIMÈTRE"], "espéré : des dettes dissimulées",
         "trouvé : cessions de titres, aucune sortie d'entité documentée de 2010 à 2025",
         "close", "grief déplacé : aucun raccord public de série, plus de 100 Md€ de marches", True),
        (["H6", "LOYERS IMPUTÉS"], "espéré : l'inflation cachée",
         "trouvé : Focus n° 152, avec les loyers l'indice est plus bas : 1,6 % contre 1,8 %",
         "tuée", "tuée par la publication de l'accusé", True),
    ]
    y = 360
    for lab, espere, trouve, verdict, note, hatched in rows:
        lines = wrap(trouve, 86)
        h = 48 + 34 + 30 * len(lines) + 14
        p += band(310, y, 1780, h, lab, [espere], sub_lines=lines, right=verdict,
                  verdict_note=note, label_w=300, right_w=400, hatch_verdict=hatched)
        y += h + 16
    p += concl(1330, "6 accusations. 2 survivantes, de forme faible.")
    return figure("fig05_six_hypotheses.svg", "FIG. 05  ·  CONTRE-ÉPREUVE", INSEE,
                  "6 accusations, 2 survivantes de forme faible",
                  ["Ce que nous espérions, ce que nous avons trouvé, ce qu'il en reste :",
                   "H2, avec un gagnant par convention ; H3, l'opacité d'expertise."],
                  "Contre-épreuve conduite du 20 au 23 septembre 2026 ; "
                  "pièces citées : Eurostat (revue par les pairs, 2021), Autorité de la statistique publique (2024), Cour des comptes.",
                  p,
                  "Sources : Insee Focus n° 152 (18/04/2019) ; revue par les pairs d'Eurostat (2021) ; Autorité de la statistique publique (rapport annuel 2024) ; Cour des comptes du 22/04/2026.",
                  "Dossier Insee · 23 septembre 2026")


# --------------------------------------------------------------------------- FIG 06
def fig06():
    """La grille et les clés de révocation dans une seule figure : lire un chiffre et
    accepter d'être révoqué sont le même geste, à deux étages."""
    y, w, h = 380, 400, 430
    p = []
    p += panel(X4[0], y, w, h, "1  LA DÉFINITION", ["Quel chiffre", "pour ce mot ?"],
               ["« le chômage baisse » :", "BIT, catégorie A, recensement ?",
                "« la pauvreté augmente » :", "seuil de 40, 50, 60 ou 70 % ?"],
               ["2,23 / 1,86 / 3,14 M", "2,8 à 14,6 M"], "un titre qui ne précise pas ne dit rien")
    p += panel(X4[1], y, w, h, "2  LA MARGE", ["Quel intervalle", "accompagne le chiffre ?"],
               ["8,3 % ± 0,3 point, marge publiée",
                "sous la marge, pas d'événement"],
               ["recensement : ± 17 500 personnes,", "dénominateur absent du document"],
               "un chiffre sans marge est un titre", fill=PANEL)
    p += panel(X4[2], y, w, h, "3  SEUIL ET PÉRIMÈTRE", ["Quel seuil,", "quel périmètre ?"],
               ["610 Md€ et 356,4 Md€ :", "deux périmètres, aucun des deux faux"],
               ["le plus grand n'est pas le plus vrai :", "il est le plus large"],
               "un chiffre sans périmètre est un malentendu")
    p += panel(X4[3], y, w, h, "4  L'HISTORIQUE", ["Que sont devenues", "les versions précédentes ?"],
               ["0,9 puis 1,4 puis 1,6 / 1,9",
                "une refonte qui baisse la pauvreté",
                "de 0,3 point n'est pas une amélioration"],
               ["révisions de croissance :", "+ 0,34 point en moyenne"],
               "un chiffre a une histoire", fill=PANEL)
    p.append(rect(MX, 850, W - 2 * MX, 270, hatch=True))
    p.append(txt(120, 898, "ET POUR NOUS : LES 4 CONDITIONS DE RÉVOCATION", "tag", avail=1100, size=24))
    p.append(hline(120, 2280, 914, FIN, THIN))
    rows = [("EUROSTAT", "une réservation publiée sur les comptes français"),
            ("RÉPLICATION", "un échec de réplication du taux de chômage au sens du BIT, par un chercheur "
                            "indépendant accédant aux microdonnées"),
            ("RÉSIDU", "un résidu supérieur à 0,3 % du PIB non tracé dans l'identité comptable de la dette"),
            ("ASYMÉTRIE", "une asymétrie établie dans l'historique des révisions, corrections allant "
                          "toujours dans le même sens")]
    cy = 955
    for lab, body in rows:
        p.append(txt(120, cy + 26, lab, "tag", avail=290, size=22))
        p.append(txt(430, cy + 26, body, "body", avail=1820, size=24, serif=True))
        cy += 40
    p += synthesis(1140, ["Lire, puis répondre : les 4 questions d'un côté, nos 4 conditions de l'autre.",
                          "Un institut honnête n'a rien à craindre de lecteurs qui savent lire."], 130,
                   "Un chiffre a une biographie ; son acte de naissance ne suffit jamais.")
    return figure("fig06_grille_de_lecture.svg", "FIG. 06  ·  GRILLE DE LECTURE ET RÉVOCATION", INSEE,
                  "4 questions pour lire un chiffre, 4 conditions pour nous révoquer",
                  ["Applicables à n'importe quel chiffre officiel, y compris aux nôtres ;",
                   "publiées avec leur date, pour qu'on puisse nous tenir au mot."],
                  "Insee (Flash n° 140, IR n° 192 et sa légende, fiche de précision du recensement) ; "
                  "ERFS 2024 ; Cour des comptes ; notes de révision des comptes ; protocole d'audit "
                  "adversarial du dépôt, version 1, et verdict consolidé du 22 septembre 2026.",
                  p,
                  "Sources : Insee (IR n° 192 et légende, Flash n° 140, fiche de précision du recensement) ; ERFS 2024 ; Cour des comptes ; note de révisions du 03/06/2026 ; protocole d'audit du dépôt et verdict du 22/09/2026.",
                  "Dossier Insee · 23 septembre 2026")


def main():
    for path in [fig01(), fig02(), fig03(), fig04(), fig05(), fig06()]:
        print(os.path.getsize(path), path)


if __name__ == "__main__":
    main()
