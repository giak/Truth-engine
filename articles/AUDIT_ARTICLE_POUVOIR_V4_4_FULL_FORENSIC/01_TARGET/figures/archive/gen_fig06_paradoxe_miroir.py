#!/usr/bin/env python3
# F1 / fig06 — Le miroir du paradoxe (prologue du masterwork).
# Méthode fig05 : chaque chaîne mesurée avec les fontes réelles (PIL) ;
# la génération ÉCHOUE si une chaîne dépasse la largeur utile de son panneau.
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

# ---------- contenu : 4 lignes du miroir (chaque cellule = phrase du prologue + renvoi) ----------
LEFT = [
    ("Dissuasion nucléaire océanique et aérienne", ""),
    ("2e rang mondial des exportateurs d’armement", "[81]"),
    ("Défense nationale : 57,1 Md€ en 2026", "[76]"),
    ("Siège permanent au Conseil de sécurité", ""),
]
RIGHT = [
    ("70 % du marché européen du cloud : 3 acteurs américains", "[80]"),
    ("Alstom cédé sous contrainte du FCPA", "[44]"),
    ("BNP Paribas : pénalité de 8,97 Md$ (2014)", "[10]"),
    ("Pantouflage de conseillers vers les acheteurs", ""),
]

KICK_L = "FIG. 06 · LE PARADOXE"
KICK_R = "L’ÉTAT SOUS ASHPHYXIE"
TITLE = "La souveraineté affichée, la dépendance documentée"
SUBTITLE = "Quatre atouts de puissance confrontés à quatre constats forensiques — chaque cellule porte sa pièce."
TAGLINE = "L’ÉCART ENTRE LE RANG ET LA PRISE EST LE SUJET DE CET ARTICLE"

# ---------- porte de largeur ----------
PANEL_W, PAD = 880, 34
USABLE = PANEL_W - 2 * PAD   # 812
LIMIT_KICK, LS_KICK = 1000, 2.6
LIMIT_TITLE, LIMIT_SUB = 2130, 2130
LIMIT_TAG = 1900
N = len(LEFT)
PANEL_H = 96 + N * 56 + 40
TOP_Y = 330

viol = []
def check(name, text, fam, size, limit, weight=400, ls=0.0):
    w = width(text, fam, size, weight) + ls * max(0, len(text) - 1)
    if w > limit:
        viol.append(f"{name}: {w:.0f}px > {limit}px  « {text[:70]} »")

check("kicker-L", KICK_L, "heros", 27, LIMIT_KICK, 700, LS_KICK)
check("kicker-R", KICK_R, "heros", 27, LIMIT_KICK, 700, LS_KICK)
check("titre", TITLE, "termes", 60, LIMIT_TITLE, 500)
check("sous-titre", SUBTITLE, "termes", 29, LIMIT_SUB)
check("tagline", TAGLINE, "heros", 28, LIMIT_TAG, 700, 1.6)
for side, rows in (("L", LEFT), ("R", RIGHT)):
    check(f"entête-{side}", "ATOUTS DE PUISSANCE AFFICHÉS" if side == "L" else "RÉALITÉS FORENSIQUES CONSTATÉES",
          "heros", 25, USABLE, 700, 2.2)
    for i, (txt, ref) in enumerate(rows):
        check(f"{side}{i}", txt, "heros", 26, USABLE)
check("foot-L", "Figure d’ouverture · cellules d’après le prologue de l’article", "termes", 23, 1150)
check("foot-R", "Méthode : chaque cellule porte sa pièce, aucune interprétation", "termes", 23, 900)
if viol:
    print("DÉBORDEMENTS :")
    [print(" ", v) for v in viol]
    sys.exit(1)

# budget vertical
BANNER_Y = TOP_Y + PANEL_H + 70
BANNER_H = 96
TAGLINE_Y = BANNER_Y + BANNER_H + 88
assert TOP_Y + PANEL_H < 1230, f"panneaux trop hauts : {PANEL_H}"
assert TAGLINE_Y <= 1370, f"tagline trop basse : {TAGLINE_Y}"

# ---------- rendu ----------
X1, X2 = 90, 2310
MID = 1200
LX, RX = 160, 2310 - 90 - PANEL_W   # panneaux : gauche aligné marge, droit en miroir
o = []
o.append('<svg xmlns="http://www.w3.org/2000/svg" width="2400" height="1500" viewBox="0 0 2400 1500">')
o.append('<rect width="2400" height="1500" fill="#FFFFFF"/>')
o.append(f'<text x="{X1}" y="78" text-anchor="start" style="{sans(27,700,ls=LS_KICK)}">{KICK_L}</text>')
o.append(f'<text x="{X2}" y="78" text-anchor="end" style="{sans(27,700,ls=LS_KICK)}">{KICK_R}</text>')
o.append('<line x1="90" y1="112" x2="2310" y2="112" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="{MID}" y="214" text-anchor="middle" style="{serif(60, BLACK, False, 500)}">{TITLE}</text>')
o.append(f'<text x="{MID}" y="278" text-anchor="middle" style="{serif(29, GRAY, False)}">{SUBTITLE}</text>')

def panel(x, head, rows):
    o.append(f'<rect x="{x}" y="{TOP_Y}" width="{PANEL_W}" height="{PANEL_H}" fill="#FFFFFF" stroke="#111111" stroke-width="2.4"/>')
    o.append(f'<rect x="{x}" y="{TOP_Y}" width="{PANEL_W}" height="64" fill="{LIGHT}"/>')
    o.append(f'<text x="{x+PAD}" y="{TOP_Y+41}" text-anchor="start" style="{sans(25,700,BLACK,2.2)}">{head}</text>')
    o.append(f'<line x1="{x}" y1="{TOP_Y+64}" x2="{x+PANEL_W}" y2="{TOP_Y+64}" stroke="#111111" stroke-width="2.4"/>')
    y = TOP_Y + 96 + 38
    for txt, ref in rows:
        o.append(f'<text x="{x+PAD}" y="{y}" text-anchor="start" style="{sans(26)}">{txt}</text>')
        if ref:
            w = width(txt, "heros", 26)
            o.append(f'<text x="{x+PAD+w+14:.0f}" y="{y}" text-anchor="start" style="{sans(24,400,GRAY)}">{ref}</text>')
        y += 56

LX = 90
RX = X2 - PANEL_W
panel(LX, "ATOUTS DE PUISSANCE AFFICHÉS", LEFT)
panel(RX, "RÉALITÉS FORENSIQUES CONSTATÉES", RIGHT)

# signes ≠ dans l'intervalle central
gy = TOP_Y + 96 + 38 + 14
for i in range(N):
    o.append(f'<text x="{MID}" y="{gy + i*56}" text-anchor="middle" style="{sans(34,700,GRAY)}">≠</text>')

# bandeau de tension
o.append(f'<rect x="310" y="{BANNER_Y}" width="1780" height="{BANNER_H}" fill="{LIGHT}" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="{MID}" y="{BANNER_Y+62}" text-anchor="middle" style="{sans(28,700,BLACK,1.6)}">{TAGLINE}</text>')

o.append('<line x1="90" y1="1410" x2="2310" y2="1410" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="{X1}" y="1460" text-anchor="start" style="{serif(23)}">Figure d’ouverture · cellules d’après le prologue de l’article</text>')
o.append(f'<text x="{X2}" y="1460" text-anchor="end" style="{serif(23)}">Méthode : chaque cellule porte sa pièce, aucune interprétation</text>')
o.append('</svg>')

out = "articles/AUDIT_ARTICLE_POUVOIR_V4_4_FULL_FORENSIC/01_TARGET/figures/svg/fig06_paradoxe_miroir.svg"
open(out, "w", encoding="utf-8").write("\n".join(o) + "\n")
print(f"OK — écrit {out} ({len(o)} éléments), panneaux h={PANEL_H}, bandeau y={BANNER_Y}.")
