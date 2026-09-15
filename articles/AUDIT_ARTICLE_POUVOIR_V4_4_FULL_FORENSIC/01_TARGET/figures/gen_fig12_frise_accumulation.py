#!/usr/bin/env python3
# F12 / fig12 — La frise de l'accumulation (prologue du masterwork).
# Quatre voies horizontales, une pièce datée par point, sur 2010-2026.
# Utilité propre : montrer l'accumulation que le texte affirme, au lieu de la
# raconter. Méthode fig05 : chaque étiquette est mesurée avec les fontes
# réelles ; la génération ÉCHOUE si deux étiquettes se recouvrent dans une
# même voie, si une étiquette sort du cadre, ou si un libellé déborde.
from PIL import ImageFont
import sys

FD = "/usr/share/texmf/fonts/opentype/public/tex-gyre/"
F = {
    ("heros", 400): FD + "texgyreheros-regular.otf",
    ("heros", 700): FD + "texgyreheros-bold.otf",
    ("termes", 400): FD + "texgyretermes-regular.otf",
    ("termes", 700): FD + "texgyretermes-bold.otf",
}
_cache = {}


def width(text, fam, size, weight=400):
    wkey = 700 if weight == 700 else 400
    ckey = (fam, wkey, size)
    if ckey not in _cache:
        _cache[ckey] = ImageFont.truetype(F[(fam, wkey)], size)
    return _cache[ckey].getlength(text)


BLACK, GRAY, LIGHT = "#111111", "#444444", "#F3F3F3"
HEROS = "TeXGyreHeros, 'TeX Gyre Heros', sans-serif"
TERMES = "TeXGyreTermes, 'TeX Gyre Termes', serif"


def sans(size, weight=400, fill=BLACK, ls=0.0):
    return (f"font-family:{HEROS};font-size:{size}px;font-weight:{weight};"
            f"fill:{fill};letter-spacing:{ls}px;")


def serif(size, fill=GRAY, italic=True, weight=400):
    st = f"font-family:{TERMES};font-size:{size}px;font-weight:{weight};fill:{fill};"
    return st + ("font-style:italic;" if italic else "")


# ---------- contenu : une pièce datée par point (faits et dates de l'article) ----------
EVENTS = [
    # Voie I — exécution
    (2014.5, 0, "BNP Paribas · 8,97 Md$", "[10] [75]"),
    (2018.4, 0, "Total · South Pars", "[11]"),
    (2021.97, 0, "Bank Melli · CJUE", "[12]"),
    (2023.4, 0, "EUCS · clauses retirées", "[51]"),
    (2023.62, 0, "campagne RRN · VIGINUM", "[77]"),
    (2024.5, 0, "eIDAS 2 · article 45a", "[69]"),
    (2026.2, 0, "dérogation ePrivacy", "[69]"),
    # Voie II — industrie
    (2010.5, 1, "Alstom · enquête FCPA", "[1] [44]"),
    (2013.3, 1, "Pierucci arrêté", "[53]"),
    (2014.85, 1, "IEF Alstom · 5 nov.", "[52]"),
    (2014.99, 1, "772,29 M$ · coupable", "[44]"),
    (2019.1, 1, "GE · 50 M€ de pénalité", "[72]"),
    (2022.6, 1, "Rockhopper · 190 M€", "[49]"),
    (2024.4, 1, "Arabelle racheté", "[55]"),
    (2025.42, 1, "sentence annulée", "[49]"),
    (2026.2, 1, "information judiciaire", "[57]"),
    # Voie III — norme
    (2018.5, 2, "Boumans · dépêches 75 %", "[29]"),
    (2019.7, 2, "New IP présenté", "[27]"),
    (2020.5, 2, "Deloitte · machines", "[70]"),
    (2021.3, 2, "Sénat · cabinets", "[68]"),
    (2023.6, 2, "règlement 2023/1230", "[70]"),
    (2025.3, 2, "JEEA · fact-checks", "[31]"),
    # Voie IV — élites
    (2019.3, 3, "Bailey · GE France", "[58] [59]"),
    (2020.4, 3, "Farkas · AFME", "[36]"),
    (2022.36, 3, "HATVP · CMA CGM", "[37] [82]"),
    (2022.52, 3, "Hopium · présidence", "[38] [83]"),
    (2024.9, 3, "HATVP · mobilités", "[40]"),
    (2025.37, 3, "Cour des comptes", "[84] [85]"),
]

LANES = [
    ("I. EXÉCUTION", "péage monétaire, numérique, ingérence"),
    ("II. INDUSTRIE", "coercition juridique sur les actifs"),
    ("III. NORME", "standards, expertise, information"),
    ("IV. ÉLITES", "trajectoires et influence"),
]

KICK_L = "FIG. 12 · L’ACCUMULATION"
KICK_R = "L’ÉTAT SOUS ASPHYXIE"
TITLE = "Quinze ans d’accumulation, quatre voies"
SUBTITLE = "Une pièce datée par point ; aucune des quatre voies ne se referme."
TAGLINE = "L’ACCUMULATION EST LE FAIT, LE CHAÎNAGE RESTE À ÉTABLIR"

# ---------- géométrie ----------
W, H = 2400, 1560
MARGIN = 90
LABEL_COL = 380                                  # colonne des libellés de voie
YEAR_MIN, YEAR_MAX = 2010.0, 2026.6
AXIS_LEFT = MARGIN + LABEL_COL
AXIS_RIGHT = W - MARGIN - 30
LANE_TOP, LANE_H, LANE_GAP = 300, 236, 22
ROWS, ROW_STEP = 4, 40
LABEL_FS, GAP, DOT_R = 23, 14, 9

viol = []


def x_of(year):
    return AXIS_LEFT + (year - YEAR_MIN) / (YEAR_MAX - YEAR_MIN) * (AXIS_RIGHT - AXIS_LEFT)


def check(name, text, fam, size, limit, weight=400, italic=False):
    w = width(text, fam, size, weight)
    if w > limit:
        viol.append(f"{name} : {w:.1f}px > {limit}px ({text[:48]!r})")
    return w


# en-tête et libellés mesurés
check("kick-R", KICK_R, "heros", 26, 900, 700)
check("titre", TITLE, "heros", 54, W - 2 * MARGIN, 700)
check("sous-titre", SUBTITLE, "termes", 32, 1500)
check("tagline", TAGLINE, "heros", 28, 1400, 700)
check("libellé de voie", max(LANES, key=lambda l: width(l[0], "heros", 30, 700))[0], "heros", 30, LABEL_COL - 34, 700)
check("sous-libellé de voie", max(LANES, key=lambda l: width(l[1], "termes", 21))[1], "termes", 21, LABEL_COL - 34)

# ---------- placement : une rangée par étiquette, aucun recouvrement dans une voie ----------
plan = []
occupied = {i: [] for i in range(len(LANES))}
for year, lane, label, ref in EVENTS:
    full = f"{label}  {ref}"
    lw = check(f"étiquette[{label[:22]}]", full, "heros", LABEL_FS, 900)
    xc = x_of(year)
    xl = min(max(xc, MARGIN + lw / 2), W - MARGIN - lw / 2)          # étiquette recadrée
    row = None
    for r in range(ROWS):
        libre = True
        for (x0, x1, r_) in occupied[lane]:
            if r_ != r:
                continue
            if xl - lw / 2 < x1 + GAP and xl + lw / 2 > x0 - GAP:
                libre = False
                break
        if libre:
            row = r
            break
    if row is None:
        viol.append(f"voie {LANES[lane][0]} : aucune rangée libre pour {label!r} ({year})")
        continue
    occupied[lane].append((xl - lw / 2, xl + lw / 2, row))
    if xl - lw / 2 < MARGIN or xl + lw / 2 > W - MARGIN:
        viol.append(f"voie {LANES[lane][0]} : étiquette hors cadre pour {label!r}")
    plan.append((year, lane, label, ref, xc, xl, row))

if viol:
    print("DÉBORDEMENTS :")
    for v in viol:
        print("  -", v)
    sys.exit(1)

# ---------- rendu ----------
o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
     f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>']
o.append(f'<text x="{MARGIN}" y="86" style="{sans(26, 700, BLACK, 2.2)}">{KICK_L}</text>')
o.append(f'<text x="{W - MARGIN}" y="86" text-anchor="end" style="{sans(26, 700, GRAY, 2.2)}">{KICK_R}</text>')
o.append(f'<line x1="{MARGIN}" y1="108" x2="{W - MARGIN}" y2="108" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="{W // 2}" y="186" text-anchor="middle" style="{sans(54, 700)}">{TITLE}</text>')
o.append(f'<text x="{W // 2}" y="240" text-anchor="middle" style="{serif(32)}">{SUBTITLE}</text>')

for i, (name, sub) in enumerate(LANES):
    y0 = LANE_TOP + i * (LANE_H + LANE_GAP)
    ybase = y0 + LANE_H - 34
    o.append(f'<rect x="{MARGIN}" y="{y0}" width="{W - 2 * MARGIN}" height="{LANE_H}" fill="{LIGHT}"/>')
    o.append(f'<line x1="{MARGIN}" y1="{ybase}" x2="{W - MARGIN}" y2="{ybase}" stroke="#111111" stroke-width="1.6"/>')
    o.append(f'<text x="{MARGIN + 14}" y="{y0 + 46}" style="{sans(30, 700)}">{name}</text>')
    o.append(f'<text x="{MARGIN + 14}" y="{y0 + 76}" style="{serif(21)}">{sub}</text>')

for (year, lane, label, ref, xc, xl, row) in plan:
    y0 = LANE_TOP + lane * (LANE_H + LANE_GAP)
    ybase = y0 + LANE_H - 34
    yl = ybase - 26 - row * ROW_STEP
    o.append(f'<line x1="{xc:.1f}" y1="{ybase}" x2="{xl:.1f}" y2="{yl + 8:.1f}" stroke="{GRAY}" stroke-width="1.2"/>')
    o.append(f'<circle cx="{xc:.1f}" cy="{ybase}" r="{DOT_R}" fill="{BLACK}"/>')
    o.append(f'<text x="{xl:.1f}" y="{yl:.1f}" text-anchor="middle" style="{sans(LABEL_FS)}">{label}</text>')
    o.append(f'<text x="{xl:.1f}" y="{yl + 21:.1f}" text-anchor="middle" style="{serif(19)}">{ref}</text>')

yaxis = LANE_TOP + len(LANES) * (LANE_H + LANE_GAP) - LANE_GAP + 12
o.append(f'<line x1="{AXIS_LEFT}" y1="{yaxis}" x2="{AXIS_RIGHT}" y2="{yaxis}" stroke="#111111" stroke-width="2.4"/>')
for year in range(2010, 2027):
    x = x_of(year)
    o.append(f'<line x1="{x:.1f}" y1="{yaxis}" x2="{x:.1f}" y2="{yaxis + 12}" stroke="#111111" stroke-width="1.6"/>')
    o.append(f'<text x="{x:.1f}" y="{yaxis + 44}" text-anchor="middle" style="{sans(22)}">{year}</text>')

o.append(f'<text x="{W // 2}" y="{H - 96}" text-anchor="middle" style="{sans(28, 700, BLACK, 1.6)}">{TAGLINE}</text>')
o.append(f'<line x1="{MARGIN}" y1="{H - 62}" x2="{W - MARGIN}" y2="{H - 62}" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="{MARGIN}" y="{H - 26}" style="{serif(23)}">Figure d’accumulation · pièces datées des parties I à IV</text>')
o.append(f'<text x="{W - MARGIN}" y="{H - 26}" text-anchor="end" style="{serif(23)}">Lecture : chaque point est une pièce, pas une causalité</text>')
o.append('</svg>')

out = "articles/AUDIT_ARTICLE_POUVOIR_V4_4_FULL_FORENSIC/01_TARGET/figures/svg/fig12_frise_accumulation.svg"
open(out, "w", encoding="utf-8").write("\n".join(o) + "\n")
print(f"OK — écrit {out} ({len(o)} éléments), {len(EVENTS)} pièces, rangées utilisées : "
      f"{ {i: max(r for (_y, l, _a, _b, _c, _d, r) in plan if l == i) + 1 for i in range(len(LANES))} }")
