#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHASE 4 v4 — robuste aux variantes Unicode apostrophe.

Strategie : pour chaque anchor qui peut piéger, on cherche le caractere
exact dans le fichier (chr(0x2019) typographique ou chr(0x0027) droite
ou chr(0x2018) typographique gauche). On utilise ensuite la variate trouvee.
"""

import re
import sys

F = "/home/giak/projects/truth-engine/articles/2026-07-08_22-00_ric_verrouillage_francais_anatomie_ARTICLE.md"

# Variantes apostrophes possibles dans le fichier
AP_TYPO_RIGHT = "\u2019"  # ' (typographique droit)
AP_TYPO_LEFT = "\u2018"   # ' (typographique gauche)
AP_STRAIGHT = "\u0027"    # ' (droite standard)
NBSP = "\u00a0"

VARIANTS_AP = [AP_TYPO_RIGHT, AP_TYPO_LEFT, AP_STRAIGHT]


def find_variant(content, motifs):
    """Cherche le premier motif dans content et retourne.
    motifs : liste de strings a essayer.
    Renvoie (anchor_trouve, position) ou (None, -1).
    """
    for m in motifs:
        idx = content.find(m)
        if idx >= 0:
            return m, idx
    return None, -1


def replace_first(content, old, new):
    """Premier remplacement, retourne (content_modifie, count)."""
    if isinstance(old, list):
        for variant in old:
            n = content.count(variant)
            if n == 1:
                return content.replace(variant, new, 1)
        # Si aucun variant ne match avec count=1, essayer d'autres counts
        for variant in old:
            n = content.count(variant)
            if n > 0:
                # Multiples occurrences : choisir le premier et continuer
                return content.replace(variant, new, 1)
        return content, 0
    else:
        n = content.count(old)
        if n == 0:
            return content, 0
        return content.replace(old, new, 1), n


with open(F, encoding="utf-8") as f:
    content = f.read()

before = len(content)
report = []


# ============================================================
# R1 - Saturation §3 : categoriser par segments courts via re.sub
# ============================================================
# Approche regex flexible : matcher "AJD" + espace + "Accueil des Jeunes"
# On utilise re.sub pour matcher les sequences AJD lanc\u00e9e en 2019... etc.
# On simplifie en remplacant le segment AJD par une categorisation.

# Segment 1 : AJD + lancement + essoufflement
pattern_ajd = re.compile(r"L[^\s]*Association[^,]+AJD[^)]*\)[^.]+essoufflement en 2021\.\s*M5S France tent[^.]+\.\s*Convergence Service Public[^.]+[\u00e9\u00e8]teint 2022\.\s*Les [^\s]*Emergents[^.]+\.\s*Mouraud sort[^.]+\.\s*Drouet et Nicolle[^.]+\.", re.DOTALL)

m_ajd = pattern_ajd.search(content)
if m_ajd:
    seg = m_ajd.group(0)
    repl = (
        "Trois formes d'" + AP_TYPO_RIGHT + "puisement se d" + AP_TYPO_RIGHT + "gagent. "
        + "Essoufflement associatif (AJD lanc" + AP_TYPO_RIGHT + "ee en 2019, essoufflement en 2021 ; "
        + "Convergence Service Public 2020-2022, " + AP_TYPO_RIGHT + "eteinte en 2022). "
        + AP_TYPO_RIGHT + "Echec d'importation italienne (M5S France tent" + AP_TYPO_RIGHT + "e en 2018-2020, dissolution de facto en 2020 ; "
        + "Les " + AP_TYPO_RIGHT + "Emergents lanc" + AP_TYPO_RIGHT + "es en 2019, dissous en 2020). "
        + "Judiciarisation des figures de rue (Drouet et Nicolle, poursuites judiciaires multiples 2019-2022). Mouraud sort des Gilets Jaunes en janvier 2019."
    )
    content = content.replace(seg, repl, 1)
    report.append((1, "R1 : saturation §3 categorisee en 3 typologies"))
else:
    # Fallback : essayer une approche simplifiee par phrases courtes
    # Strategie : remplacer seulement les phrases-cles pour ne pas tout casser
    print("ATTENTION R1 regex principale non matchee, fallback sur segments courts", file=sys.stderr)

    # Anchor court 1 : "AJD lancXee en 2019" peu importe X
    pattern_ajd_short = re.compile(r"AJD lanc.{1,2}ee en 2019", re.UNICODE)
    if pattern_ajd_short.search(content):
        content = pattern_ajd_short.sub("AJD lanc" + AP_TYPO_RIGHT + "ee en 2019", content, 1)
        report.append((1, "R1 fallback : AJD lancement normalise (chr)"))
    else:
        print("R1 fallback court egalement echou\u00e9", file=sys.stderr)
        report.append((0, "R1 : abandonnee"))

# ============================================================
# R2a - Titre categorie \u00a73
# ============================================================
old_r2a_variants = [
    "Ensuite, ceux qui meurent professionnellement de leur engagement pro-RIC.",
    "Ensuite, ceux qui meurent professionnellement de leur engagement pro-RIC.",  # avec apostrophe droite
]
content, n = replace_first(content, old_r2a_variants, "Ensuite, les porteurs neutralis" + AP_TYPO_RIGHT + "es institutionnellement.")
report.append((n, "R2a : 'qui meurent' -> 'neutralises institutionnellement'"))

# ============================================================
# R2b - Sous-titre bifurcation
# ============================================================
old_r2b_variants = [
    "Mort par bifurcation tactique.",
    "Mort par bifurcation tactique.",
]
content, n = replace_first(content, old_r2b_variants, "Bifurcation partisane.")
report.append((n, "R2b : 'Mort' supprimee"))

# ============================================================
# R2c - Sous-titre recyclage : regex flexible
# ============================================================
# On match toute combinaison d'apostrophe typographique ou droite
# "Recyclage p\u2019riph\u2019rique." ou "Recyclage p\u00e9riph\u00e9rique." (accents) ou "Recyclage p'riph'rique"
# En fait l'erreur précédente avait chr(0x2019) entre les segments, mais resultat "Recyclage p'riph'rique"
# La source de l'erreur est probablement que chr(0x2019) cree bien \u2019 mais le print l'affiche comme '
# L'erreur reelle : le fichier n'a PAS chr(0x2019) entre les segments, il a un autre caractere ou rien
# Strategie regex : matcher "Recyclage p<sep>riph<sep>rique" avec <sep> = [\u2019\u0027\u2018\-]

pattern_r2c = re.compile(
    r"Recyclage p[\u2019\u0027\u2018\u2013\u2014\-]?riph[\u2019\u0027\u2018\u2013\u2014\-]?rique\.",
    re.UNICODE
)
m_r2c = pattern_r2c.search(content)
if m_r2c:
    content = pattern_r2c.sub("Retrait post-carri" + AP_TYPO_RIGHT + "re.", content, 1)
    report.append((1, "R2c : 'Recyclage periphrique' -> 'Retrait post-carriere'"))
else:
    print("R2c regex non matchee, abandon", file=sys.stderr)
    report.append((0, "R2c abandonnee"))

# ============================================================
# R3 - Epithete M5S \u00a74 : tolerant d'apostrophes mixtes
# ============================================================
# Anchor : "Le Movimento 5 Stelle (M5S, parti populiste italien fond__e par Beppe Grillo en 2009) italien, fond__e en 2015"
# Le __e = e ou e avec apostrophe. Pour eviter pieges : pas d'apostrophe dans l'anchor.
# Mais l'original a "fondée" avec "\u00e9" ou "fond" + "\u00e9" + "e". La \u00e9 est un caractere francais sans apostrophe.

old_r3 = "Le Movimento 5 Stelle (M5S, parti populiste italien fond"
new_r3 = "Le Movimento 5 Stelle (M5S, mouvement d'initiative num" + AP_TYPO_RIGHT + "erique italien fond"

# On localise l'anchor dans le fichier en cherchant un fragment stable
# "parti populiste italien fond" peut etre suivi de chr(0x2019) + "e" ou de chr(0xE9) directement.

old_r3_pattern = re.compile(r"Le Movimento 5 Stelle \(M5S, parti populiste italien fond[\u2019\u0027\u2018]?e par Beppe Grillo en 2009\) italien, fond[\u2019\u0027\u2018]?e en 2015", re.UNICODE)
m_r3 = old_r3_pattern.search(content)
if m_r3:
    seg = m_r3.group(0)
    repl = "Le Movimento 5 Stelle (M5S, mouvement d'initiative num" + AP_TYPO_RIGHT + "erique italien fond" + AP_TYPO_RIGHT + "e par Beppe Grillo en 2009), structur" + AP_TYPO_RIGHT + "e en parti en 2013"
    content = content.replace(seg, repl, 1)
    report.append((1, "R3 : 'parti populiste' -> 'mouvement d\u2019initiative num\u00e9rique'"))
else:
    report.append((0, "R3 abandonnee (regex non matchee)"))

# ============================================================
# R4 - Coh\u00e9rence \u00a75 / Note d'auteur
# ============================================================
old_r4_variants = [
    "La port" + AP_TYPO_RIGHT + "ee du diagnostic s'arr" + AP_TYPO_RIGHT + "ete au constat du verrou. Ce que ce dossier prouve, ce qu'il ne prouve pas, et la m" + AP_TYPO_RIGHT + "ethode qu'il suit, sont consign" + AP_TYPO_RIGHT + "es dans la note d'auteur finale.",
]
content, n = replace_first(content, old_r4_variants, "La port" + AP_TYPO_RIGHT + "ee du diagnostic, ce que ce dossier prouve, ce qu'il ne prouve pas, et la m" + AP_TYPO_RIGHT + "ethode qu'il suit, sont consign" + AP_TYPO_RIGHT + "es dans la note d'auteur finale.")
report.append((n, "R4 : 's'arr\u00eate au constat' supprime"))

# ============================================================
# R5 - Sur-referencement (NBSP integre)
# ============================================================
old_r5_pattern = re.compile(
    r"Comme l[\u2019\u0027\u2018]esquisse \*\*\[L[\u2019\u0027\u2018]Adieu aux partis" + NBSP + r": du diagnostic de Weil",
    re.UNICODE
)
m_r5 = old_r5_pattern.search(content)
if m_r5:
    seg = m_r5.group(0)
    repl = "Quelques principes esquiss" + AP_TYPO_RIGHT + "es cadrent la r" + AP_TYPO_RIGHT + "eflexion prospective **[L" + AP_TYPO_RIGHT + "Adieu aux partis" + NBSP + ": du diagnostic de Weil"
    content = content.replace(seg, repl, 1)
    report.append((1, "R5 : 'Comme l\u2019esquisse' -> 'Quelques principes esquiss\u00e9s'"))
else:
    report.append((0, "R5 abandonnee (regex non matchee)"))

# ============================================================
# Persistance
# ============================================================
with open(F, "w", encoding="utf-8") as f:
    f.write(content)

after = len(content)

print("=" * 60)
print("RAPPORT APPLICATION v4 (regex tolerant apostrophes)")
print("=" * 60)
total = 0
for n, label in report:
    print("  - " + label + ": " + str(n))
    total += n
print("")
print("Total replacements : " + str(total))
print("Longueur avant : " + str(before))
print("Longueur apres : " + str(after))
print("Difference : " + str(after - before))

em_count = content.encode("utf-8").count(b"\xe2\x80\x94")
print("Em-dash (LOI 3 cible 0) : " + str(em_count))

print("")
print("PHASE 4 v4 (regex tolerant) termine.")
