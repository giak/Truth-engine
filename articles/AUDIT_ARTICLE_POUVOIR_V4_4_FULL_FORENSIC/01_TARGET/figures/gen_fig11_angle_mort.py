#!/usr/bin/env python3
# C9 / fig11 — L'angle mort du droit pénal (partie IV.2 du masterwork).
# Deux colonnes : ce que les pièces documentent (HATVP, recommandations)
# vs ce que le pénal exige (432-11, 432-13). Le vide central, étiqueté,
# EST le point aveugle. Bandeau : la directive 2026/1021 ne referme pas
# l'écart (prise illégale d'intérêts hors noyau harmonisé).
# Méthode fig05 : chaque chaîne mesurée, échec sur tout débordement.
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
    return f"font-family:{HEROS};font-size:{size}px;font-weight:{weight};fill:{fill};letter-spacing:{ls}px;"

def serif(size, fill=GRAY, italic=True, weight=400):
    st = f"font-family:{TERMES};font-size:{size}px;font-weight:{weight};fill:{fill};"
    return st + ("font-style:italic;" if italic else "")

# ---------- colonne gauche : ce que les pièces documentent (partie IV) ----------
LEFT_HEAD = "CE QUE LES PIÈCES DOCUMENTENT"
LEFT_ROWS = [
    ("Orientations d’arbitrages sans pacte formel,", "accoutumance progressive", "[40]"),
    ("Bailey : cabinet de l’Économie → GE France (2019)", "chronologie documentée", "[58]"),
    ("Djebbari : présidence d’Hopium autorisée", "départ CMA CGM refusé par la HATVP", "[37] [38] [82] [83]"),
    ("Farkas : EBA → AFME", "mauvaise administration", "[36]"),
    ("Kroes : Commission → Uber", "violations éthiques", "[39]"),
]

# ---------- colonne droite : ce que le pénal exige (partie IV.2) ----------
RIGHT_HEAD = "CE QUE LE PÉNAL EXIGE"
RIGHT_ROWS = [
    ("432-11, corruption : un pacte", "antérieur à l’acte accompli", "[78]"),
    ("432-11, trafic d’influence : abus", "d’influence, sans pacte à établir", "[78]"),
    ("432-13 : surveillance ou contrôle effectif", "de l’entreprise concernée", "[79]"),
    ("432-13 : contrat ou avis dans le cadre", "des fonctions effectivement exercées", "[79]"),
    ("432-13 : trois ans après la cessation", "de fonctions — borne la reprise", "[79]"),
]

# ---------- centre : l'angle mort ----------
CENTER = ["L’ANGLE", "MORT", "aucune des deux", "mains ne saisit", "ce que l’autre", "documente"]

KICK_L = "FIG. 11 · L’ANGLE MORT"
KICK_R = "L’ÉTAT SOUS ASPHYXIE"
TITLE = "Pourquoi rien n’est poursuivable — et rien n’est normal"
SUBTITLE = "Ce que la partie IV.2 établit : un écart structurel entre le phénomène documenté et la preuve que le droit exige."
DIRECTIVE = "Portée : la directive (UE) 2026/1021 harmonise le noyau pénal mais laisse la prise illégale d’intérêts au volet prévention — l’angle mort est appelé à persister [42] [78] [79]."
TAGLINE = "ABSENCE DE POURSUITE ≠ ABSENCE DE PHÉNOMÈNE"

# ---------- porte de largeur ----------
COL_W, PAD = 890, 34
US = COL_W - 2 * PAD
CORRIDOR = 440                     # espace central (le vide étiqueté)
LX, RX = 90, 2310 - COL_W
CENTER_W = CORRIDOR - 60
LIMIT_KICK, LS_KICK = 1000, 2.6
LIMIT_TAG = 1900

viol = []
def check(name, text, fam, size, limit, weight=400, ls=0.0):
    w = width(text, fam, size, weight) + ls * max(0, len(text) - 1)
    if w > limit:
        viol.append(f"{name}: {w:.0f}px > {limit}px  « {text[:70]} »")

check("kicker-L", KICK_L, "heros", 27, LIMIT_KICK, 700, LS_KICK)
check("kicker-R", KICK_R, "heros", 27, LIMIT_KICK, 700, LS_KICK)
check("titre", TITLE, "termes", 60, 2130, 500)
check("sous-titre", SUBTITLE, "termes", 29, 2130)
check("directive", DIRECTIVE, "termes", 24, 1660)
check("tagline", TAGLINE, "heros", 28, LIMIT_TAG, 700, 1.6)
check("L-entête", LEFT_HEAD, "heros", 25, US, 700, 1.8)
check("R-entête", RIGHT_HEAD, "heros", 25, US, 700, 1.8)
for i, (a, b, ref) in enumerate(LEFT_ROWS):
    check(f"L{i}a", a, "heros", 24, US)
    check(f"L{i}b", b, "heros", 24, US)
    check(f"L{i}+ref", a, "heros", 24, US - width(ref, "heros", 21) - 16)
for i, (a, b, ref) in enumerate(RIGHT_ROWS):
    check(f"R{i}a", a, "heros", 24, US)
    check(f"R{i}b", b, "heros", 24, US)
    check(f"R{i}+ref", a, "heros", 24, US - width(ref, "heros", 21) - 16)
for j, ln in enumerate(CENTER):
    check(f"centre-{j}", ln, "heros" if j < 2 else "termes", 26 if j < 2 else 21, CENTER_W, 700 if j < 2 else 400, 1.2 if j < 2 else 0.0)
check("foot-L", "Figure d’argument · dérivée de la partie IV.2 de l’article", "termes", 23, 1150)
check("foot-R", "Méthode : deux colonnes sourcées, le vide central n’est qu’un écart", "termes", 23, 900)
if viol:
    print("DÉBORDEMENTS :")
    [print(" ", v) for v in viol]
    sys.exit(1)

# ---------- budget vertical ----------
HEAD_H = 60
ROW_H, ROW_G = 96, 24
COLY = 350
rows = max(len(LEFT_ROWS), len(RIGHT_ROWS))
col_h = HEAD_H + rows * ROW_H + (rows - 1) * ROW_G + 36
DIR_Y = COLY + col_h + 62
DIR_H = 96
TAG_Y = DIR_Y + DIR_H + 82
assert TAG_Y <= 1370, f"tagline trop basse : {TAG_Y}"

# ---------- rendu ----------
o = []
o.append('<svg xmlns="http://www.w3.org/2000/svg" width="2400" height="1500" viewBox="0 0 2400 1500">')
o.append('<rect width="2400" height="1500" fill="#FFFFFF"/>')
o.append(f'<text x="90" y="78" text-anchor="start" style="{sans(27,700,ls=LS_KICK)}">{KICK_L}</text>')
o.append(f'<text x="2310" y="78" text-anchor="end" style="{sans(27,700,ls=LS_KICK)}">{KICK_R}</text>')
o.append(f'<line x1="90" y1="112" x2="2310" y2="112" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="1200" y="214" text-anchor="middle" style="{serif(60, BLACK, False, 500)}">{TITLE}</text>')
o.append(f'<text x="1200" y="278" text-anchor="middle" style="{serif(29, GRAY, False)}">{SUBTITLE}</text>')

def column(x, head, rows_, head_fill):
    o.append(f'<rect x="{x}" y="{COLY}" width="{COL_W}" height="{col_h}" fill="#FFFFFF" stroke="#111111" stroke-width="2.4"/>')
    o.append(f'<rect x="{x}" y="{COLY}" width="{COL_W}" height="{HEAD_H}" fill="{head_fill}"/>')
    o.append(f'<line x1="{x}" y1="{COLY+HEAD_H}" x2="{x+COL_W}" y2="{COLY+HEAD_H}" stroke="#111111" stroke-width="2.4"/>')
    o.append(f'<text x="{x+PAD}" y="{COLY+39}" text-anchor="start" style="{sans(25,700,BLACK,1.8)}">{head}</text>')
    y = COLY + HEAD_H + 42
    for a, b, ref in rows_:
        o.append(f'<text x="{x+PAD}" y="{y}" text-anchor="start" style="{sans(24)}">{a}</text>')
        o.append(f'<text x="{x+PAD}" y="{y+28}" text-anchor="start" style="{sans(24)}">{b}</text>')
        rw = max(width(a, "heros", 24), width(b, "heros", 24))
        o.append(f'<text x="{x+PAD+rw+16:.0f}" y="{y+14}" text-anchor="start" style="{sans(21,400,GRAY)}">{ref}</text>')
        y += ROW_H + ROW_G

column(LX, LEFT_HEAD, LEFT_ROWS, LIGHT)
column(RX, RIGHT_HEAD, RIGHT_ROWS, LIGHT)

# le vide central : étiquette verticale, pointillés de part et d'autre, AUCUNE flèche
ccx = 1200
o.append(f'<line x1="{LX + COL_W + 16}" y1="{COLY + col_h // 2}" x2="{RX - 16}" y2="{COLY + col_h // 2}" stroke="#555555" stroke-width="2" stroke-dasharray="3 12"/>')
ty = COLY + col_h // 2 - (len(CENTER) * 34) // 2 + 26
for j, ln in enumerate(CENTER):
    if j < 2:
        o.append(f'<text x="{ccx}" y="{ty + j*38}" text-anchor="middle" style="{sans(26,700,BLACK,1.2)}">{ln}</text>')
    else:
        o.append(f'<text x="{ccx}" y="{ty + 76 + (j-2)*26}" text-anchor="middle" style="{serif(21, GRAY)}">{ln}</text>')

# bandeau de portée directive
o.append(f'<rect x="310" y="{DIR_Y}" width="1780" height="{DIR_H}" fill="{LIGHT}" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="1200" y="{DIR_Y + 58}" text-anchor="middle" style="{serif(24, GRAY)}">{DIRECTIVE}</text>')
o.append(f'<text x="1200" y="{TAG_Y}" text-anchor="middle" style="{sans(28,700,BLACK,1.6)}">{TAGLINE}</text>')
o.append(f'<line x1="90" y1="1410" x2="2310" y2="1410" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="90" y="1460" text-anchor="start" style="{serif(23)}">Figure d’argument · dérivée de la partie IV.2 de l’article</text>')
o.append(f'<text x="2310" y="1460" text-anchor="end" style="{serif(23)}">Méthode : deux colonnes sourcées, le vide central n’est qu’un écart</text>')
o.append('</svg>')

out = "articles/AUDIT_ARTICLE_POUVOIR_V4_4_FULL_FORENSIC/01_TARGET/figures/svg/fig11_angle_mort.svg"
open(out, "w", encoding="utf-8").write("\n".join(o) + "\n")
print(f"OK — écrit {out} ({len(o)} éléments), colonnes y={COLY}-{COLY+col_h}, directive y={DIR_Y}, tagline y={TAG_Y}.")
