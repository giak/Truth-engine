#!/usr/bin/env python3
# Générateur fig05 — grille des références, texte mesuré, zéro débordement toléré.
from PIL import ImageFont
import sys

FD = "/usr/share/texmf/fonts/opentype/public/tex-gyre/"
F = {
    ("heros", 400): FD + "texgyreheros-regular.otf",
    ("heros", 700): FD + "texgyreheros-bold.otf",
    ("termes", 400): FD + "texgyretermes-regular.otf",
    ("termes", 400): FD + "texgyretermes-regular.otf",
    ("termes-i", 400): FD + "texgyretermes-italic.otf",
    ("termes", 500): FD + "texgyretermes-regular.otf",
    ("termes", 700): FD + "texgyretermes-bold.otf",
}
_cache = {}
def width(text, fam, size, weight=400, ls=0.0, italic=False):
    wkey = 700 if weight == 700 else 400
    ckey = ("termes-i" if italic else fam, wkey, size)
    if ckey not in _cache:
        path = F[("termes-i", 400)] if italic else F[(fam, wkey)]
        _cache[ckey] = ImageFont.truetype(path, size)
    w = _cache[ckey].getlength(text)
    return w + ls * max(0, len(text) - 1)

BLACK, GRAY, LIGHT = "#111111", "#444444", "#F3F3F3"
HEROS = "TeXGyreHeros, 'TeX Gyre Heros', sans-serif"
TERMES = "TeXGyreTermes, 'TeX Gyre Termes', serif"

def sans(size, weight=400, fill=BLACK, ls=0.0):
    return f"font-family:{HEROS};font-size:{size}px;font-weight:{weight};fill:{fill};letter-spacing:{ls}px;"

def serif(size, fill=BLACK, italic=False, weight=400):
    st = f"font-family:{TERMES};font-size:{size}px;font-weight:{weight};fill:{fill};"
    return st + ("font-style:italic;" if italic else "")

# ---------- contenu (à mesurer) ----------
KICK_L = "FIG. 05 · CHAÎNE BORNÉE"
KICK_R = "L’ÉTAT SOUS ASPHYXIE"
TITLE = "L’étau et le verrou : la chaîne bornée d’Alstom"
SUBTITLE = "Chaque relation de la contrainte est documentée ; la chaîne s’arrête à l’engagement du dirigeant."
BANNER1 = "La chaîne est documentée jusqu’à l’engagement du dirigeant."
BANNER2 = "Le dessin d’ensemble, ce qui aurait lié l’enquête à la cession, reste hors des pièces."
TAGLINE = "CONTRAINTE DOCUMENTÉE ≠ DESSEIN ÉTABLI"
FOOT_L = "Figure conceptuelle · dates et montants d’après le registre de l’article [44] [52] [56] [72] [55] [57]"
FOOT_R = "Méthode : chaque relation séparée, aucune intention déduite"

PANELS = [
    ("(a)  L’ÉTAU", ["Enquête pénale", "ouverte (2010)"],
     ["• enquête FCPA du DOJ", "• arrestation à New York", "• amende redoutée : 1 Md$"],
     ["sans acte public, sans ordre"]),
    ("(b)  LA CÉSSION", ["Négociation", "exclusive (2014)"],
     ["• Énergie cédée à GE", "• Arabelle incluse", "• menace de faillite"],
     ["décision privée sous contrainte"]),
    ("(c)  LA SIGNATURE", ["Autorisation", "ministérielle"],
     ["• arrêté IEF : 5 nov. 2014", "• plaidoyer : 772 M$", "• l’État signe l’acte décisif"],
     ["fermé par un acte légal"]),
    ("(d)  LE COÛT", ["L’engagement trahi"],
     ["• 1 000 emplois promis", "• vingt-cinq créés", "• pénalité : 50 M€ exigés"],
     ["la sanction vient de l’État"]),
    ("(e)  LE RACHAT", ["Le retour", "payé (2024)"],
     ["• EDF rachète Arabelle", "• information judiciaire", "• partie civile (2026)"],
     ["dix ans pour réacheter l’essentiel"]),
]

# ---------- porte de largeur ----------
PANEL_W, PAD_L, PAD_R = 388, 28, 28
USABLE = PANEL_W - PAD_L - PAD_R  # 332
viol = []
def check(name, text, fam, size, limit, weight=400, ls=0.0, italic=False):
    w = width(text, fam, size, weight, ls, italic)
    if w > limit:
        viol.append(f"{name}: {w:.0f}px > {limit}px  « {text} »")

check("kicker-L", KICK_L, "heros", 27, 1000, 700, 2.6)
check("kicker-R", KICK_R, "heros", 27, 1000, 700, 2.6)
check("titre", TITLE, "termes", 60, 2130, 500)
check("sous-titre", SUBTITLE, "termes", 29, 2130)
check("banner1", BANNER1, "termes", 48, 1700, 500)
check("banner2", BANNER2, "heros", 29, 1700)
check("tagline", TAGLINE, "heros", 28, 1700, 700, 1.6)
check("foot-L", FOOT_L, "termes", 23, 1150, italic=True)
check("foot-R", FOOT_R, "termes", 23, 900, italic=True)
for i, (label, stitle, bullets, note) in enumerate(PANELS):
    check(f"P{i} label", label, "heros", 27, USABLE, 700, 1.5)
    for s in stitle:
        check(f"P{i} titre", s, "termes", 34, USABLE, 500)
    for b in bullets:
        check(f"P{i} puce", b, "heros", 26, USABLE)
    for n in note:
        check(f"P{i} note", n, "termes", 22, USABLE, italic=True)
if viol:
    print("DÉBORDEMENTS :")
    [print(" ", v) for v in viol]
    sys.exit(1)

# ---------- géométrie ----------
X = [90, 548, 1006, 1464, 1922]
W, H, Y = 388, 470, 390
GAPS = [(X[i] + W, X[i + 1]) for i in range(4)]
o = []
o.append('<svg xmlns="http://www.w3.org/2000/svg" width="2400" height="1500" viewBox="0 0 2400 1500">')
o.append('<rect width="2400" height="1500" fill="#FFFFFF"/>')
o.append('<defs><marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L12,6 L0,12 z" fill="#111111"/></marker></defs>')
o.append(f'<text x="90" y="78" text-anchor="start" style="{sans(27,700,ls=2.6)}">{KICK_L}</text>')
o.append(f'<text x="2310" y="78" text-anchor="end" style="{sans(27,700,ls=2.6)}">{KICK_R}</text>')
o.append('<line x1="90" y1="112" x2="2310" y2="112" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="1200" y="214" text-anchor="middle" style="{serif(60,weight=500)}">{TITLE}</text>')
o.append(f'<text x="1200" y="278" text-anchor="middle" style="{serif(29,fill=GRAY)}">{SUBTITLE}</text>')
for i, (label, stitle, bullets, note) in enumerate(PANELS):
    x = X[i]
    o.append(f'<rect x="{x}" y="{Y}" width="{W}" height="{H}" fill="#FFFFFF" stroke="#111111" stroke-width="2.4"/>')
    o.append(f'<text x="{x+PAD_L}" y="435" text-anchor="start" style="{sans(27,700,GRAY,1.5)}">{label}</text>')
    o.append(f'<line x1="{x+PAD_L}" y1="456" x2="{x+W-PAD_R}" y2="456" stroke="#555555" stroke-width="1.7"/>')
    ty = 508
    for s in stitle:
        o.append(f'<text x="{x+PAD_L}" y="{ty}" text-anchor="start" style="{serif(34,weight=500)}">{s}</text>')
        ty += 40
    by = max(615, ty + 67)
    for b in bullets:
        o.append(f'<text x="{x+PAD_L+4}" y="{by}" text-anchor="start" style="{sans(26)}">{b}</text>')
        by += 40
    o.append(f'<line x1="{x+PAD_L}" y1="791" x2="{x+W-PAD_R}" y2="791" stroke="#555555" stroke-width="1.7" stroke-dasharray="8 8"/>')
    ny = 826
    for n in note:
        o.append(f'<text x="{x+PAD_L}" y="{ny}" text-anchor="start" style="{serif(22,GRAY,italic=True)}">{n}</text>')
        ny += 27
for a, b in GAPS:
    mid = (a + b) / 2
    o.append(f'<line x1="{mid-23}" y1="625" x2="{mid+13}" y2="625" stroke="#111111" stroke-width="3" marker-end="url(#arrow)"/>')
o.append('<rect x="310" y="1035" width="1780" height="210" fill="#F3F3F3" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="1200" y="1115" text-anchor="middle" style="{serif(48,weight=500)}">{BANNER1}</text>')
o.append(f'<text x="1200" y="1182" text-anchor="middle" style="{sans(29,400,GRAY)}">{BANNER2}</text>')
o.append(f'<text x="1200" y="1328" text-anchor="middle" style="{sans(28,700,BLACK,1.6)}">{TAGLINE}</text>')
o.append('<line x1="90" y1="1410" x2="2310" y2="1410" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="90" y="1460" text-anchor="start" style="{serif(23,GRAY,italic=True)}">{FOOT_L}</text>')
o.append(f'<text x="2310" y="1460" text-anchor="end" style="{serif(23,GRAY,italic=True)}">{FOOT_R}</text>')
o.append('</svg>')

out = "articles/AUDIT_ARTICLE_POUVOIR_V4_4_FULL_FORENSIC/01_TARGET/figures/svg/fig05_alstom_chaine_bornee.svg"
open(out, "w", encoding="utf-8").write("\n".join(o) + "\n")
print(f"OK — écrit {out} ({len(o)} éléments), toutes largeurs ≤ limite.")
