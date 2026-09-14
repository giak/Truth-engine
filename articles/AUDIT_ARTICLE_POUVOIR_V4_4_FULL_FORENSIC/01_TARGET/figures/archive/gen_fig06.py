#!/usr/bin/env python3
# Générateur fig06 — la matrice des quatre verrous (partie V du masterwork).
# Méthode fig05 : chaque chaîne est mesurée avec les fontes réelles (PIL) ;
# la génération ÉCHOUE si une chaîne dépasse la largeur utile de sa colonne.
# Layout : 14 lignes à cellule unique (copie resserrée, la matrice intégrale
# verbatim reste dans l'article), 4 bandes de verrou, tagline de clôture.
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

# ---------- les 14 lignes : instrument + cas + pièce sur une seule phrase ----------
# (verrou, texte de la ligne) — resserré depuis la matrice de la partie V, état 94c93001.
ROWS = [
    ("G1", "Péage monétaire — amende de 8,97 Md$ contre BNP Paribas · DOJ, 30 juin 2014"),
    ("G1", "Sur-conformité — retrait de TotalEnergies de South Pars 11 ; arrêt Bank Melli · 16 mai 2018 ; CJUE, 21 déc. 2021"),
    ("G1", "Hébergement de données — EUCS expurgé ; Health Data Hub confié à Microsoft Azure · US Chamber of Commerce, 23 mai 2023"),
    ("G1", "Interception et identité numérique — règlement 2024/1183, art. 45a ; ePrivacy rétablie jusqu’au 3 avril 2028 · EUR-Lex 2024/1183 ; 2026/1881"),
    ("G1", "Influence clandestine — Alp Services ; BlackCore / Rokh Solis ; opération Doppelgänger · Mediapart ; VIGINUM 2023 et 2026"),
    ("G1", "Emprise territoriale — neuf relais de stations de police identifiés par la DGSI ; station du Fujian · question n° 1675 ; Conseil d’État"),
    ("G2", "Poursuite pénale extraterritoriale — enquête Alstom 2010, cession 2014, pénalité de 772,29 M$ · DOJ, 22 déc. 2014"),
    ("G2", "Arbitrage d’investissement — Rockhopper c. Italie : 190 M€ en 2022, sentence annulée le 2 juin 2025 · CIRDI, ARB/17/14"),
    ("G3", "Standards techniques privés — New IP bloqué (IETF / ISOC) ; composant logiciel retenu par le règlement 2023/1230 · ISOC, fév. 2022 ; DG GROW, juin 2020"),
    ("G3", "Sous-traitance de l’expertise publique — rapport du Sénat n° 578 ; étude d’impact Deloitte · Sénat, 2021 ; DG GROW, juin 2020"),
    ("G3", "Concentration des flux d’information — dépendance aux agences établie au niveau national (Pays-Bas, Suisse) · Boumans, 2018 ; Vogler, 2024"),
    ("G3", "Délégation du jugement de vérité — signaleurs de confiance de l’article 22 du DSA ; biais d’agenda · DSA, art. 22 ; JEEA, 2025"),
    ("G4", "Pantouflage des décideurs publics — Hugh Bailey ; Jean-Baptiste Djebbari de ministre à CMA CGM · GE France, 2019 ; HATVP, 17 mai 2022"),
    ("G4", "Lobbying d’influence structuré — ELNET France ; Adam Farkas de l’ABE à l’AFME ; Neelie Kroes pour Uber · HATVP ; Médiateur européen ; OLAF"),
]
GROUPS = {
    "G1": ("VERROU I · INFRASTRUCTURE ET INGÉRENCE", 6),
    "G2": ("VERROU II · LAWFARE INDUSTRIEL", 2),
    "G3": ("VERROU III · NORMATIF ET CONSEIL", 4),
    "G4": ("VERROU IV · POROSITÉ DES ÉLITES", 2),
}

# ---------- habillage ----------
KICK_L = "FIG. 06 · MATRICE DES QUATRE VERROUS"
KICK_R = "L’ÉTAT SOUS ASHPHYXIE"
TITLE = "Quatorze instruments, quatre verrous, aucune pièce de chaînage"
SUBTITLE = "L’inventaire documente des instruments, un par ligne ; il ne démontre pas un système."
BANNER1 = "Chaque ligne tient sur une pièce. Le lien entre les verrous n’en a aucune."
BANNER2 = "La thèse d’une architecture unique reste ouverte : c’est ce chaînage qu’il faudrait produire."
TAGLINE = "INVENTAIRE DOCUMENTÉ ≠ SYSTÈME DÉMONTRÉ"
FOOT_L = "Figure de synthèse · contenu d’après la matrice de la partie V de l’article"
FOOT_R = "Méthode : chaque instrument séparé, aucune architecture déduite"

# ---------- porte de largeur ----------
LIMIT_LINE = 2130   # lignes de matrice, titre, sous-titre
LIMIT_BAN1 = 1700
LIMIT_BAN2 = 1700
LIMIT_KICK = 1000
LS_KICK = 2.6

viol = []
def check(name, text, fam, size, limit, weight=400, ls=0.0):
    w = width(text, fam, size, weight) + ls * max(0, len(text) - 1)
    if w > limit:
        viol.append(f"{name}: {w:.0f}px > {limit}px  « {text[:70]} »")

check("kicker-L", KICK_L, "heros", 27, LIMIT_KICK, 700, LS_KICK)
check("kicker-R", KICK_R, "heros", 27, LIMIT_KICK, 700, LS_KICK)
check("titre", TITLE, "termes", 60, LIMIT_LINE, 500)
check("sous-titre", SUBTITLE, "termes", 29, LIMIT_LINE)
for i, (gid, line) in enumerate(ROWS):
    check(f"R{i:02d}", line, "heros", 25, LIMIT_LINE)
check("banner1", BANNER1, "termes", 44, LIMIT_BAN1, 500)
check("banner2", BANNER2, "heros", 27, LIMIT_BAN2)
check("tagline", TAGLINE, "heros", 28, LIMIT_LINE, 700, 1.6)
check("foot-L", FOOT_L, "termes", 23, 1150)
check("foot-R", FOOT_R, "termes", 23, 900)
if viol:
    print("DÉBORDEMENTS :")
    [print(" ", v) for v in viol]
    sys.exit(1)

# ---------- budget vertical ----------
N_ROWS, N_GROUPS = 14, 4
ROW_H, ROW_G = 36, 6
GROUP_H, GROUP_G = 42, 20
TOP_Y = 310
table_h = N_ROWS * ROW_H + (N_ROWS - N_GROUPS) * ROW_G + N_GROUPS * (GROUP_H + GROUP_G)
BANNER_Y = TOP_Y + table_h + 46
BANNER_H = 130
TAGLINE_Y = BANNER_Y + BANNER_H + 64
assert table_h + TOP_Y < 1290, f"table trop haute : table_h={table_h}"
assert BANNER_Y + BANNER_H <= 1330, f"bannière déborde : {BANNER_Y + BANNER_H}"
assert TAGLINE_Y <= 1370, f"tagline trop basse : {TAGLINE_Y}"

# ---------- rendu ----------
X1, X2 = 90, 2310
TABLE_W = 2220
o = []
o.append('<svg xmlns="http://www.w3.org/2000/svg" width="2400" height="1500" viewBox="0 0 2400 1500">')
o.append('<rect width="2400" height="1500" fill="#FFFFFF"/>')
o.append(f'<text x="{X1}" y="78" text-anchor="start" style="{sans(27,700,ls=LS_KICK)}">{KICK_L}</text>')
o.append(f'<text x="{X2}" y="78" text-anchor="end" style="{sans(27,700,ls=LS_KICK)}">{KICK_R}</text>')
o.append('<line x1="90" y1="112" x2="2310" y2="112" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="1200" y="214" text-anchor="middle" style="{serif(60, BLACK, False, 500)}">{TITLE}</text>')
o.append(f'<text x="1200" y="278" text-anchor="middle" style="{serif(29, GRAY, False)}">{SUBTITLE}</text>')

y = TOP_Y
prev_group = None
for gid, line in ROWS:
    if gid != prev_group:
        if prev_group is not None:
            y += GROUP_G - ROW_G
        label, nrows = GROUPS[gid]
        o.append(f'<rect x="{X1}" y="{y}" width="{TABLE_W}" height="{GROUP_H}" fill="{LIGHT}" stroke="#111111" stroke-width="2.4"/>')
        o.append(f'<text x="{X1+24}" y="{y+28}" text-anchor="start" style="{sans(25,700,BLACK,2.2)}">{label} · {nrows} INSTRUMENTS</text>')
        y += GROUP_H + ROW_G
        prev_group = gid
    o.append(f'<rect x="{X1}" y="{y}" width="{TABLE_W}" height="{ROW_H}" fill="#FFFFFF" stroke="#111111" stroke-width="1.7"/>')
    o.append(f'<text x="{X1+24}" y="{y+26}" text-anchor="start" style="{sans(25)}">{line}</text>')
    y += ROW_H + ROW_G

o.append(f'<line x1="{X1}" y1="{y-ROW_G+10}" x2="{X2}" y2="{y-ROW_G+10}" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<rect x="310" y="{BANNER_Y}" width="1780" height="{BANNER_H}" fill="{LIGHT}" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="1200" y="{BANNER_Y+56}" text-anchor="middle" style="{serif(44, BLACK, False, 500)}">{BANNER1}</text>')
o.append(f'<text x="1200" y="{BANNER_Y+108}" text-anchor="middle" style="{sans(27,400,GRAY)}">{BANNER2}</text>')
o.append(f'<text x="1200" y="{TAGLINE_Y}" text-anchor="middle" style="{sans(28,700,BLACK,1.6)}">{TAGLINE}</text>')
o.append('<line x1="90" y1="1410" x2="2310" y2="1410" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="{X1}" y="1460" text-anchor="start" style="{serif(23)}">{FOOT_L}</text>')
o.append(f'<text x="{X2}" y="1460" text-anchor="end" style="{serif(23)}">{FOOT_R}</text>')
o.append('</svg>')

out = "articles/AUDIT_ARTICLE_POUVOIR_V4_4_FULL_FORENSIC/01_TARGET/figures/svg/fig06_matrice_verrous_instruments.svg"
open(out, "w", encoding="utf-8").write("\n".join(o) + "\n")
print(f"OK — écrit {out} ({len(o)} éléments), table_h={table_h}px, bannière y={BANNER_Y}, tagline y={TAGLINE_Y}.")
