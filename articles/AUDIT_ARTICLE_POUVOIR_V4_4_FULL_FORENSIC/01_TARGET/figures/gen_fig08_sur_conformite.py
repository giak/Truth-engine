#!/usr/bin/env python3
# F3 / fig08 — La chaîne de la sur-conformité (partie I.2 du masterwork).
# Trois nœuds chaînés + recours défaillant (pointillé) sous le nœud central.
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

# ---------- contenu (partie I.2, chaque ligne = phrase de l'article + renvoi) ----------
NODES = [
    ("(a)  SANCTIONS SECONDAIRES", ["retrait américain du JCPOA", "mai 2018"]),
    ("(b)  RISQUE DE COUPURE", ["40 % du capital nord-américain [74]", "refinancement dépendant du marché $"]),
    ("(c)  RETRAIT PRÉVENTIF", ["TotalEnergies, 16 mai 2018 [11]", "South Pars 11 : 4,8 Md$ [11] [71]"]),
]
RECOURSE = ("RÈGLEMENT UE 2271/96", ["activé par l’UE, il n’offre", "aucune immunité effective", "constat d’impasse : CJUE [12] [13]"])

KICK_L = "FIG. 08 · LA SUR-CONFORMITÉ"
KICK_R = "L’ÉTAT SOUS ASHPHYXIE"
TITLE = "La contrainte sans ordre"
SUBTITLE = "Le mécanisme de la partie I.2 : la menace sur l’infrastructure produit la décision d’abandon."
BANNER1 = "Aucun ordre n’a été transmis : la contrainte s’exerce par l’infrastructure."
TAGLINE = "AUTOCENSURE PRÉVENTIVE ≠ ORDRE REÇU"

# ---------- porte de largeur ----------
BOX_W, BOX_H, PAD = 620, 210, 30
USABLE = BOX_W - 2 * PAD   # 560
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
check("banner1", BANNER1, "termes", 40, 1780, 500)
check("tagline", TAGLINE, "heros", 28, LIMIT_TAG, 700, 1.6)
for i, (head, lines) in enumerate(NODES):
    check(f"N{i}-entête", head, "heros", 25, USABLE, 700, 1.8)
    for j, ln in enumerate(lines):
        check(f"N{i}-{j}", ln, "heros", 26, USABLE)
check("R-entête", RECOURSE[0], "heros", 25, USABLE, 700, 1.8)
for j, ln in enumerate(RECOURSE[1]):
    check(f"R-{j}", ln, "heros", 25, USABLE)
check("foot-L", "Figure de mécanisme · d’après la partie I.2 de l’article", "termes", 23, 1150)
check("foot-R", "Méthode : chaîne documentée, recours défaillant en pointillé", "termes", 23, 900)
if viol:
    print("DÉBORDEMENTS :")
    [print(" ", v) for v in viol]
    sys.exit(1)

# ---------- géométrie ----------
XS = [90, 890, 1690]
BOX_Y = 480
ARROW_Y = BOX_Y + BOX_H // 2
REC_Y, REC_H = 790, 190
BANNER_Y, BANNER_H = 1060, 110
TAGLINE_Y = BANNER_Y + BANNER_H + 120
assert REC_Y + REC_H < BANNER_Y, "recours et bannière se chevauchent"
assert TAGLINE_Y <= 1370, f"tagline trop basse : {TAGLINE_Y}"

o = []
o.append('<svg xmlns="http://www.w3.org/2000/svg" width="2400" height="1500" viewBox="0 0 2400 1500">')
o.append('<rect width="2400" height="1500" fill="#FFFFFF"/>')
o.append('<defs><marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L12,6 L0,12 z" fill="#111111"/></marker></defs>')
o.append(f'<text x="90" y="78" text-anchor="start" style="{sans(27,700,ls=LS_KICK)}">{KICK_L}</text>')
o.append(f'<text x="2310" y="78" text-anchor="end" style="{sans(27,700,ls=LS_KICK)}">{KICK_R}</text>')
o.append('<line x1="90" y1="112" x2="2310" y2="112" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="1200" y="214" text-anchor="middle" style="{serif(60, BLACK, False, 500)}">{TITLE}</text>')
o.append(f'<text x="1200" y="278" text-anchor="middle" style="{serif(29, GRAY, False)}">{SUBTITLE}</text>')

for i, (head, lines) in enumerate(NODES):
    x = XS[i]
    o.append(f'<rect x="{x}" y="{BOX_Y}" width="{BOX_W}" height="{BOX_H}" fill="#FFFFFF" stroke="#111111" stroke-width="2.4"/>')
    o.append(f'<rect x="{x}" y="{BOX_Y}" width="{BOX_W}" height="56" fill="{LIGHT}"/>')
    o.append(f'<text x="{x+PAD}" y="{BOX_Y+37}" text-anchor="start" style="{sans(25,700,BLACK,1.8)}">{head}</text>')
    o.append(f'<line x1="{x}" y1="{BOX_Y+56}" x2="{x+BOX_W}" y2="{BOX_Y+56}" stroke="#111111" stroke-width="2.4"/>')
    y = BOX_Y + 104
    for ln in lines:
        o.append(f'<text x="{x+PAD}" y="{y}" text-anchor="start" style="{sans(26)}">{ln}</text>')
        y += 42

for i in range(2):
    mid = (XS[i] + BOX_W + XS[i + 1]) / 2
    o.append(f'<line x1="{mid-30}" y1="{ARROW_Y}" x2="{mid+18}" y2="{ARROW_Y}" stroke="#111111" stroke-width="3" marker-end="url(#arrow)"/>')

# recours défaillant : pointillé, sans flèche (il ne porte pas la décision)
rx = XS[1]
o.append(f'<line x1="1200" y1="{BOX_Y+BOX_H}" x2="1200" y2="{REC_Y}" stroke="#555555" stroke-width="2.4" stroke-dasharray="6 8"/>')
o.append(f'<rect x="{rx}" y="{REC_Y}" width="{BOX_W}" height="{REC_H}" fill="#FFFFFF" stroke="#555555" stroke-width="2.4" stroke-dasharray="10 8"/>')
o.append(f'<text x="{rx+PAD}" y="{REC_Y+40}" text-anchor="start" style="{sans(25,700,GRAY,1.8)}">{RECOURSE[0]}</text>')
y = REC_Y + 82
for ln in RECOURSE[1]:
    o.append(f'<text x="{rx+PAD}" y="{y}" text-anchor="start" style="{sans(25,400,GRAY)}">{ln}</text>')
    y += 36

o.append(f'<rect x="310" y="{BANNER_Y}" width="1780" height="{BANNER_H}" fill="{LIGHT}" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="1200" y="{BANNER_Y+68}" text-anchor="middle" style="{serif(40, BLACK, False, 500)}">{BANNER1}</text>')
o.append(f'<text x="1200" y="{TAGLINE_Y}" text-anchor="middle" style="{sans(28,700,BLACK,1.6)}">{TAGLINE}</text>')
o.append('<line x1="90" y1="1410" x2="2310" y2="1410" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="90" y="1460" text-anchor="start" style="{serif(23)}">Figure de mécanisme · d’après la partie I.2 de l’article</text>')
o.append(f'<text x="2310" y="1460" text-anchor="end" style="{serif(23)}">Méthode : chaîne documentée, recours défaillant en pointillé</text>')
o.append('</svg>')

out = "articles/AUDIT_ARTICLE_POUVOIR_V4_4_FULL_FORENSIC/01_TARGET/figures/svg/fig08_sur_conformite.svg"
open(out, "w", encoding="utf-8").write("\n".join(o) + "\n")
print(f"OK — écrit {out} ({len(o)} éléments), recours y={REC_Y}, bannière y={BANNER_Y}.")
