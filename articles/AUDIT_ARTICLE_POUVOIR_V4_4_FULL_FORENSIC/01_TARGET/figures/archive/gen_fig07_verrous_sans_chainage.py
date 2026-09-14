#!/usr/bin/env python3
# F2 / fig07 — Les quatre verrous sans chaînage (partie V du masterwork).
# L'information graphique est le VIDE : quatre blocs disjoints, aucune arête.
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

# ---------- contenu : les 14 instruments, verrous I-IV (matrice de la partie V) ----------
BLOCKS = {
    "I": ("VERROU I · INFRASTRUCTURE ET INGÉRENCE", [
        "Péage monétaire : BNP, 8,97 Md$ [10]",
        "Sur-conformité : TotalEnergies [11]",
        "Données : EUCS, Health Data Hub [51]",
        "eIDAS 45a, ePrivacy 2026/1881 [69]",
        "Influence : Alp, BlackCore, RRN [65][66][77]",
        "Stations de police : DGSI, 9 relais [67]",
    ]),
    "II": ("VERROU II · LAWFARE INDUSTRIEL", [
        "Alstom : FCPA, cession 2014 [44]",
        "Rockhopper : ISDS, 190 M€ [49]",
    ]),
    "III": ("VERROU III · NORMATIF ET CONSEIL", [
        "New IP bloqué : IETF, ISOC [28]",
        "Normes : Sénat 578, Deloitte [68][70]",
        "Agences : dépendance nationale [29][30]",
        "DSA art. 22 : signaleurs [34][35]",
    ]),
    "IV": ("VERROU IV · POROSITÉ DES ÉLITES", [
        "Pantouflage : Bailey, Djebbari [58][37]",
        "Lobbying : Farkas, Kroes, ELNET [36][39]",
    ]),
}

KICK_L = "FIG. 07 · LES QUATRE VERROUS"
KICK_R = "L’ÉTAT SOUS ASHPHYXIE"
TITLE = "Quatre blocs documentés, aucune pièce ne les relie"
SUBTITLE = "Chaque instrument tient sur sa pièce ; l’absence d’arête est le constat, pas un artifice de mise en page."
CENTER = "AUCUNE PIÈCE\nDE CHAÎNAGE\nENTRE LES VERROUS"
BANNER1 = "La convergence des verrous est la lecture proposée par l’article ;"
BANNER2 = "son chaînage reste ouvert — c’est ce lien qu’il faudrait documenter pour fermer la thèse."
TAGLINE = "INVENTAIRE DOCUMENTÉ ≠ SYSTÈME DÉMONTRÉ"

# ---------- porte de largeur ----------
BW, BH, PAD = 880, 356, 34
USABLE = BW - 2 * PAD   # 812
LIMIT_KICK, LS_KICK = 1000, 2.6
GAP_X = 460
GX0, GY0 = 90, 310
CENTER_W = GAP_X - 80
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
check("banner2", BANNER2, "heros", 26, 1780)
check("tagline", TAGLINE, "heros", 28, LIMIT_TAG, 700, 1.6)
check("centre-L1", CENTER.split("\n")[0], "heros", 22, CENTER_W, 700, 1.2)
check("centre-L2", CENTER.split("\n")[1], "heros", 22, CENTER_W, 700, 1.2)
check("centre-L3", CENTER.split("\n")[2], "heros", 22, CENTER_W, 700, 1.2)
for gid, (head, rows) in BLOCKS.items():
    check(f"B{gid}-entête", head, "heros", 24, USABLE, 700, 1.8)
    for j, r in enumerate(rows):
        check(f"B{gid}-{j}", r, "heros", 25, USABLE)
check("foot-L", "Figure de synthèse · d’après la matrice de la partie V de l’article", "termes", 23, 1150)
check("foot-R", "Méthode : blocs disjoints, aucune liaison dessinée", "termes", 23, 900)
if viol:
    print("DÉBORDEMENTS :")
    [print(" ", v) for v in viol]
    sys.exit(1)

# budget vertical
ROW = 44
assert max(len(r) for _, r in BLOCKS.values()) * ROW + 92 <= BH, "bloc trop petit"
BANNER_Y = GY0 + 2 * BH + 110 + 40
BANNER_H = 100
TAGLINE_Y = BANNER_Y + BANNER_H + 60
assert BANNER_Y + BANNER_H <= 1330, f"bannière déborde : {BANNER_Y + BANNER_H}"
assert TAGLINE_Y <= 1370, f"tagline trop basse : {TAGLINE_Y}"

# ---------- rendu ----------
o = []
o.append('<svg xmlns="http://www.w3.org/2000/svg" width="2400" height="1500" viewBox="0 0 2400 1500">')
o.append('<rect width="2400" height="1500" fill="#FFFFFF"/>')
o.append(f'<text x="90" y="78" text-anchor="start" style="{sans(27,700,ls=LS_KICK)}">{KICK_L}</text>')
o.append(f'<text x="2310" y="78" text-anchor="end" style="{sans(27,700,ls=LS_KICK)}">{KICK_R}</text>')
o.append('<line x1="90" y1="112" x2="2310" y2="112" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="1200" y="214" text-anchor="middle" style="{serif(60, BLACK, False, 500)}">{TITLE}</text>')
o.append(f'<text x="1200" y="278" text-anchor="middle" style="{serif(29, GRAY, False)}">{SUBTITLE}</text>')

POS = {"I": (GX0, GY0), "II": (GX0 + BW + GAP_X, GY0), "III": (GX0, GY0 + BH + 110), "IV": (GX0 + BW + GAP_X, GY0 + BH + 110)}
for gid, (bx, by) in POS.items():
    head, rows = BLOCKS[gid]
    o.append(f'<rect x="{bx}" y="{by}" width="{BW}" height="{BH}" fill="#FFFFFF" stroke="#111111" stroke-width="2.4"/>')
    o.append(f'<rect x="{bx}" y="{by}" width="{BW}" height="56" fill="{LIGHT}"/>')
    o.append(f'<text x="{bx+PAD}" y="{by+36}" text-anchor="start" style="{sans(24,700,BLACK,1.8)}">{head}</text>')
    o.append(f'<line x1="{bx}" y1="{by+56}" x2="{bx+BW}" y2="{by+56}" stroke="#111111" stroke-width="2.4"/>')
    y = by + 56 + 42
    for r in rows:
        o.append(f'<text x="{bx+PAD}" y="{y}" text-anchor="start" style="{sans(25)}">{r}</text>')
        y += ROW

# le vide central : pointillés neutres + mention (pas de flèche, pas de liaison)
cx1, cx2 = GX0 + BW, GX0 + BW + GAP_X
cy = GY0 + BH // 2
o.append(f'<line x1="{cx1+20}" y1="{cy}" x2="{cx2-20}" y2="{cy}" stroke="#555555" stroke-width="2.4" stroke-dasharray="4 14"/>')
o.append(f'<line x1="{cx1+20}" y1="{cy+BH+110}" x2="{cx2-20}" y2="{cy+BH+110}" stroke="#555555" stroke-width="2.4" stroke-dasharray="4 14"/>')
ccx = (cx1 + cx2) / 2
ccy = GY0 + BH + 55
for k, line in enumerate(CENTER.split("\n")):
    o.append(f'<text x="{ccx}" y="{ccy - 34 + k*34}" text-anchor="middle" style="{sans(22,700,GRAY,1.2)}">{line}</text>')

o.append(f'<rect x="310" y="{BANNER_Y}" width="1780" height="{BANNER_H}" fill="{LIGHT}" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="1200" y="{BANNER_Y+40}" text-anchor="middle" style="{serif(40, BLACK, False, 500)}">{BANNER1}</text>')
o.append(f'<text x="1200" y="{BANNER_Y+84}" text-anchor="middle" style="{sans(26,400,GRAY)}">{BANNER2}</text>')
o.append(f'<text x="1200" y="{TAGLINE_Y}" text-anchor="middle" style="{sans(28,700,BLACK,1.6)}">{TAGLINE}</text>')
o.append('<line x1="90" y1="1410" x2="2310" y2="1410" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="90" y="1460" text-anchor="start" style="{serif(23)}">Figure de synthèse · d’après la matrice de la partie V de l’article</text>')
o.append(f'<text x="2310" y="1460" text-anchor="end" style="{serif(23)}">Méthode : blocs disjoints, aucune liaison dessinée</text>')
o.append('</svg>')

out = "articles/AUDIT_ARTICLE_POUVOIR_V4_4_FULL_FORENSIC/01_TARGET/figures/svg/fig07_verrous_sans_chainage.svg"
open(out, "w", encoding="utf-8").write("\n".join(o) + "\n")
print(f"OK — écrit {out} ({len(o)} éléments), bannière y={BANNER_Y}, tagline y={TAGLINE_Y}.")
