#!/usr/bin/env python3
# C8 / fig10 — La grille de lecture des verrous (partie V du masterwork).
# Quatre questions filtres (les quatre verrous) → trois issues documentées
# (levé / subi / non clos). Utilité propre (critère c du plan §5) : rendre la
# thèse manipulable sur tout cas futur.
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

# ---------- contenu : questions filtres (dérivées des quatre verrous) ----------
QUESTIONS = [
    ("Q1", "Un canal essentiel (paiement, cloud, standard) échappe-t-il à la juridiction nationale ?", "VERROU I"),
    ("Q2", "Une procédure pénale ou d’arbitrage peut-elle viser l’actif ou le dirigeant ?", "VERROU II"),
    ("Q3", "Une instance de norme ou de certification peut-elle être capturée en amont ?", "VERROU III"),
    ("Q4", "Une trajectoire post-fonction est-elle en jeu, sans pacte prouvable ?", "VERROU IV"),
]

# ---------- contenu : les trois issues (partie V, resserré) ----------
OUTCOMES = [
    ("VERROU LEVÉ", "lorsqu’un outil dédié, une volonté politique et un coût jugé acceptable coexistent",
     ["Photonis : veto IEF, 2020 [24]", "New IP bloqué : coalition [28]", "Sortie du TCE [50] · VIGINUM [77]", "Lituanie face à la Chine [16] [17]"]),
    ("VERROU SUBI", "lorsqu’aucun de ces trois éléments n’est réuni au moment de la décision",
     ["BNP Paribas : 8,97 Md$ [10]", "TotalEnergies : South Pars [11]", "Alstom : cession 2014 [44]", "Health Data Hub sur Azure [51]"]),
    ("VERROU NON CLOS", "lorsque la pièce manque pour trancher dans un sens ou dans l’autre",
     ["EUCS : clauses retirées [51]", "DSA art. 22 : signaleurs [34] [35]", "Mobilités HATVP [37] [38] [58]"]),
]

KICK_L = "FIG. 10 · GRILLE DE LECTURE"
KICK_R = "L’ÉTAT SOUS ASPHYXIE"
TITLE = "Tester un cas : quatre questions, trois issues"
SUBTITLE = "Pour toute dépendance nouvelle, la méthode que la partie V de l’article nomme et applique."
CONDITIONS = "Les trois issues se départagent par trois conditions : un outil institutionnel dédié, une volonté politique explicite, un coût de résistance jugé acceptable."
TAGLINE = "UNE MÉTHODE DE LECTURE, PAS UNE MACHINE À PRÉDIRE"

# ---------- porte de largeur ----------
QX, QW, QPAD = 90, 2220, 34
QLBL_W = 96                        # colonne Q1-Q4
TAG_MAX, TAG_GAP = 145, 18         # réserve pour l’étiquette VERROU x
USQ = QW - 2 * QPAD - QLBL_W - TAG_MAX - TAG_GAP   # texte de question
OW, OPAD = 692, 30
USO = OW - 2 * OPAD
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
check("conditions", CONDITIONS, "termes", 24, 1780)
check("tagline", TAGLINE, "heros", 28, LIMIT_TAG, 700, 1.6)
for q, txt, tag in QUESTIONS:
    check(f"{q}-texte", txt, "heros", 26, USQ)
    check(f"{q}-tag", tag, "heros", 22, TAG_MAX, 700, 1.5)
for head, sub, cells in OUTCOMES:
    check(f"issue[{head}]-tête", head, "heros", 26, USO, 700, 1.5)
    for c in cells:
        check(f"issue[{head}]-cellule", c, "heros", 24, USO)
check("foot-L", "Figure d’usage · dérivée de la partie V de l’article", "termes", 23, 1150)
check("foot-R", "Méthode : questions et issues documentées, aucune prédiction", "termes", 23, 900)
if viol:
    print("DÉBORDEMENTS :")
    [print(" ", v) for v in viol]
    sys.exit(1)

# ---------- wrap des sous-textes d’issue (3 lignes max, mesuré) ----------
def wrap(text, fam, size, limit, weight=400, maxlines=3):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        cand = (cur + " " + w).strip()
        if width(cand, fam, size, weight) <= limit:
            cur = cand
        else:
            if cur:
                lines.append(cur)
            cur = w
            if len(lines) >= maxlines:
                return None
    if cur:
        lines.append(cur)
    return lines if len(lines) <= maxlines else None

SUBS = []
for head, sub, cells in OUTCOMES:
    wl = wrap(sub, "heros", 22, USO)
    if wl is None:
        print(f"DÉBORDEMENT : sous-texte de « {head} » nécessite >3 lignes")
        sys.exit(1)
    for ln in wl:
        if width(ln, "heros", 22) > USO:
            print(f"DÉBORDEMENT : « {ln} »")
            sys.exit(1)
    SUBS.append(wl)

# ---------- budget vertical ----------
QH, QG, QY = 56, 14, 330
q_bottom = QY + 4 * QH + 3 * QG
OY, OH = q_bottom + 130, 430
COND_Y = OY + OH + 46
TAG_Y = COND_Y + 64
assert TAG_Y <= 1370, f"tagline trop basse : {TAG_Y}"

# hauteur interne des blocs d’issue : vérification dynamique
for k, (head, _sub, cells) in enumerate(OUTCOMES):
    yy = 102 + len(SUBS[k]) * 30 + 18 + len(cells) * 38
    assert yy <= OH - 24, f"bloc d’issue {head} trop petit : contenu {yy}px > {OH-24}px"

# ---------- rendu ----------
o = []
o.append('<svg xmlns="http://www.w3.org/2000/svg" width="2400" height="1500" viewBox="0 0 2400 1500">')
o.append('<rect width="2400" height="1500" fill="#FFFFFF"/>')
o.append('<defs><marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L12,6 L0,12 z" fill="#111111"/></marker></defs>')
o.append(f'<text x="{QX}" y="78" text-anchor="start" style="{sans(27,700,ls=LS_KICK)}">{KICK_L}</text>')
o.append(f'<text x="2310" y="78" text-anchor="end" style="{sans(27,700,ls=LS_KICK)}">{KICK_R}</text>')
o.append(f'<line x1="{QX}" y1="112" x2="2310" y2="112" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="1200" y="214" text-anchor="middle" style="{serif(60, BLACK, False, 500)}">{TITLE}</text>')
o.append(f'<text x="1200" y="278" text-anchor="middle" style="{serif(29, GRAY, False)}">{SUBTITLE}</text>')

# bloc des quatre questions
o.append(f'<rect x="{QX}" y="{QY}" width="{QW}" height="{4*QH + 3*QG}" fill="#FFFFFF" stroke="#111111" stroke-width="2.4"/>')
yq = QY
for i, (q, txt, tag) in enumerate(QUESTIONS):
    if i > 0:
        o.append(f'<line x1="{QX}" y1="{yq}" x2="{QX + QW}" y2="{yq}" stroke="#555555" stroke-width="1.4"/>')
    qtxt_x = QX + QPAD + QLBL_W
    o.append(f'<text x="{QX + QPAD}" y="{yq + QH // 2 + 9}" text-anchor="start" style="{sans(26,700)}">{q}</text>')
    o.append(f'<text x="{qtxt_x}" y="{yq + QH // 2 + 9}" text-anchor="start" style="{sans(26)}">{txt}</text>')
    tw = width(txt, "heros", 26)
    o.append(f'<text x="{qtxt_x + tw + TAG_GAP:.0f}" y="{yq + QH // 2 + 9}" text-anchor="start" style="{sans(22,400,GRAY)}">{tag}</text>')
    yq += QH + QG

# trois flèches questions → issues (une seule segment par flèche, marker au bout)
qbx = QX + QW // 2
for ox in (90, 854, 1618):
    tx = ox + OW // 2
    o.append(f'<line x1="{qbx}" y1="{q_bottom + 10}" x2="{tx}" y2="{OY - 16}" stroke="#111111" stroke-width="2.4" marker-end="url(#arrow)"/>')

# trois blocs d’issues
for ox, (head, _sub, cells), sublines in zip((90, 854, 1618), OUTCOMES, SUBS):
    o.append(f'<rect x="{ox}" y="{OY}" width="{OW}" height="{OH}" fill="#FFFFFF" stroke="#111111" stroke-width="2.4"/>')
    o.append(f'<rect x="{ox}" y="{OY}" width="{OW}" height="60" fill="{LIGHT}"/>')
    o.append(f'<line x1="{ox}" y1="{OY + 60}" x2="{ox + OW}" y2="{OY + 60}" stroke="#111111" stroke-width="2.4"/>')
    o.append(f'<text x="{ox + OPAD}" y="{OY + 39}" text-anchor="start" style="{sans(26,700)}">{head}</text>')
    yy = OY + 102
    for ln in sublines:
        o.append(f'<text x="{ox + OPAD}" y="{yy}" text-anchor="start" style="{sans(22,400,GRAY)}">{ln}</text>')
        yy += 30
    yy += 18
    for c in cells:
        o.append(f'<text x="{ox + OPAD}" y="{yy}" text-anchor="start" style="{sans(24)}">{c}</text>')
        yy += 38

# conditions (sous les blocs) + tagline
o.append(f'<text x="1200" y="{COND_Y}" text-anchor="middle" style="{serif(24)}">{CONDITIONS}</text>')
o.append(f'<text x="1200" y="{TAG_Y}" text-anchor="middle" style="{sans(28,700,BLACK,1.6)}">{TAGLINE}</text>')
o.append(f'<line x1="{QX}" y1="1410" x2="2310" y2="1410" stroke="#111111" stroke-width="2.4"/>')
o.append(f'<text x="{QX}" y="1460" text-anchor="start" style="{serif(23)}">Figure d’usage · dérivée de la partie V de l’article</text>')
o.append(f'<text x="2310" y="1460" text-anchor="end" style="{serif(23)}">Méthode : questions et issues documentées, aucune prédiction</text>')
o.append('</svg>')

out = "articles/AUDIT_ARTICLE_POUVOIR_V4_4_FULL_FORENSIC/01_TARGET/figures/svg/fig10_grille_de_lecture.svg"
open(out, "w", encoding="utf-8").write("\n".join(o) + "\n")
print(f"OK — écrit {out} ({len(o)} éléments), questions y={QY}-{q_bottom}, issues y={OY}-{OY+OH}, tagline y={TAG_Y}.")
