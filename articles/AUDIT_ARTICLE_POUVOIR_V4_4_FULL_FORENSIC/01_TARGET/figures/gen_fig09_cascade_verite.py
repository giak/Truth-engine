#!/usr/bin/env python3
# F4 / fig09 — La cascade de la vérité (partie III.3 du masterwork).
# Quatre étages verticaux ; la borne F11 (« hypothèse UE non mesurée ») est
# portée ENTRE les étages 1 et 2, pas en note.
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

# ---------- contenu (partie III.3 ; chaque étage = phrase de l'article + renvois) ----------
STAGES = [
    ("ÉTAGE 1 · PRODUCTION", ["Trois agences mondiales : AFP, Reuters, Associated Press"], "flux de dépêches"),
    ("ÉTAGE 2 · DIFFUSION", ["Rédactions en ligne dépendantes du matériel d’agence [29] [30]"], "sélection et reprise"),
    ("ÉTAGE 3 · CERTIFICATION", ["Fact-checkers certifiés IFCN / EFCSN [31]", "DSA art. 22 : signaleurs de confiance [34] [35]"], "traitement prioritaire"),
    ("ÉTAGE 4 · MODÉRATION", ["Les plateformes décident des suites [3] [34] [35]"], "effets non mesurés"),
]
BOUND = "dépendance mesurée aux Pays-Bas (jusqu’à 75 %) et en Suisse — l’hypothèse d’une dépendance comparable en Europe reste NON MESURÉE"

KICK_L = "FIG. 09 · LA CHAÎNE DE LA VÉRITÉ"
KICK_R = "L’ÉTAT SOUS ASPHYXIE"
TITLE = "D’où vient ce qui est tenu pour vrai"
SUBTITLE = "La chaîne de distribution de la partie III.3, étage par étage, avec sa borne documentaire."
BANNER1 = "La vérité descend une chaîne de dépendances ; chaque étage documenté porte sa pièce."
TAGLINE = "CHAÎNE DOCUMENTÉE ≠ DIRECTION DÉMONTRÉE"

# ---------- porte de largeur ----------
BOX_W, PAD = 1780, 34
USABLE = BOX_W - 2 * PAD   # 1712
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
check("borne", BOUND, "termes", 24, USABLE - 60)
for i, (head, lines, side) in enumerate(STAGES):
    for part in head.split(" · "):
        check(f"S{i}-label[{part}]", part, "heros", 24, 210, 700, 1.8)
    for j, ln in enumerate(lines):
        check(f"S{i}-{j}", ln, "heros", 26, USABLE - 260)
    check(f"S{i}-side", side, "termes", 22, 280)
check("foot-L", "Figure de flux · d’après la partie III.3 de l’article", "termes", 23, 1150)
check("foot-R", "Méthode : étages documentés, borne affichée entre étages 1 et 2", "termes", 23, 900)
if viol:
    print("DÉBORDEMENTS :")
    [print(" ", v) for v in viol]
    sys.exit(1)

# ---------- géométrie ----------
BX = 310
TOP_Y = 330
H2, H3 = 92, 130          # étages à 1 ou 2 lignes
STAGE_H = [H2, H2, H3, H2]
GAP = 56
GAP_BORNE = 96            # l'intervalle 1→2 porte la borne
ys = []
y = TOP_Y
for i, h in enumerate(STAGE_H):
    ys.append(y)
    y += h + (GAP_BORNE if i == 0 else GAP)
BANNER_Y = y + 10
BANNER_H = 100
TAGLINE_Y = BANNER_Y + BANNER_H + 84
assert BANNER_Y + BANNER_H <= 1330, f"bannière déborde : {BANNER_Y + BANNER_H}"
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

for i, (head, lines, side) in enumerate(STAGES):
    by, bh = ys[i], STAGE_H[i]
    o.append(f'<rect x="{BX}" y="{by}" width="{BOX_W}" height="{bh}" fill="#FFFFFF" stroke="#111111" stroke-width="2.4"/>')
    # bandeau latéral d'étage : libellé empilé sur deux lignes
    o.append(f'<rect x="{BX}" y="{by}" width="250" height="{bh}" fill="{LIGHT}"/>')
    o.append(f'<line x1="{BX+250}" y1="{by}" x2="{BX+250}" y2="{by+bh}" stroke="#111111" stroke-width="2.4"/>')
    parts = head.split(" · ")
    base = by + bh // 2 - (len(parts) - 1) * 16 + 2
    for k, part in enumerate(parts):
        o.append(f'<text x="{BX+24}" y="{base + k*32}" text-anchor="start" style="{sans(24,700,BLACK,1.8)}">{part}</text>')
    # contenu
    ly = by + (bh + 10) // 2 - (len(lines) - 1) * 21
    for ln in lines:
        o.append(f'<text x="{BX+290}" y="{ly}" text-anchor="start" style="{sans(26)}">{ln}</text>')
        ly += 42
    # mention de flux à droite
    o.append(f'<text x="{BX+BOX_W-24}" y="{by+38}" text-anchor="end" style="{serif(22)}">{side}</text>')

# flèches 2→3 et 3→4 (le 1→2 est la borne, sans flèche pleine)
for i in (1, 2):
    ax = 1200
    ay1 = ys[i] + STAGE_H[i]
    ay2 = ys[i + 1]
    o.append(f'<line x1="{ax}" y1="{ay1+6}" x2="{ax}" y2="{ay2-14}" stroke="#111111" stroke-width="3" marker-end="url(#arrow)"/>')

# la borne entre étages 1 et 2 : texte centré, sans flèche pleine
b_mid = (ys[0] + STAGE_H[0] + ys[1]) / 2
o.append(f'<text x="1200" y="{b_mid - 6:.0f}" text-anchor="middle" style="{serif(24, GRAY)}">{BOUND}</text>')

o.append(f'<rect x="{BX}" y="{BANNER_Y}" width="{BOX_W}" height="{BANNER_H}" fill="{LIGHT}" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="1200" y="{BANNER_Y+62}" text-anchor="middle" style="{serif(40, BLACK, False, 500)}">{BANNER1}</text>')
o.append(f'<text x="1200" y="{TAGLINE_Y}" text-anchor="middle" style="{sans(28,700,BLACK,1.6)}">{TAGLINE}</text>')
o.append('<line x1="90" y1="1410" x2="2310" y2="1410" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="90" y="1460" text-anchor="start" style="{serif(23)}">Figure de flux · d’après la partie III.3 de l’article</text>')
o.append(f'<text x="2310" y="1460" text-anchor="end" style="{serif(23)}">Méthode : étages documentés, borne affichée entre étages 1 et 2</text>')
o.append('</svg>')

out = "articles/AUDIT_ARTICLE_POUVOIR_V4_4_FULL_FORENSIC/01_TARGET/figures/svg/fig09_cascade_verite.svg"
open(out, "w", encoding="utf-8").write("\n".join(o) + "\n")
print(f"OK — écrit {out} ({len(o)} éléments), étages y={ys}, bannière y={BANNER_Y}.")
