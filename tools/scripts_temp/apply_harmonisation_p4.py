#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Application des 5 recommandations PHASE 4 sur l'article RIC (post-PHASE 3 v2).
R1 saturation §3 categorisation 8 items en 3 typologies.
R2 glissement pamphletaire §3 (3 replacements).
R3 epithete M5S §4 (parti populiste -> mouvement d'initiative numerique).
R4 coherence §5 / Note d'auteur (suppression phrase parasite).
R5 sur-referencement Truth Engine §5 (L'Adieu aux partis neutralise).
"""

import sys

F = "/home/giak/projects/truth-engine/articles/2026-07-08_22-00_ric_verrouillage_francais_anatomie_ARTICLE.md"

# Caracteres typographiques pieges
AP9 = "\u2019"   # apostrophe typographique droite
NBSP = "\u00a0"  # espace insecable

# Guillemets francais
LOQ = "\u00ab"   # <<
ROQ = "\u00bb"   # >>


def apply(content, old, new, label):
    """Remplace old par new en exigeant count == 1, sinon abort."""
    n = content.count(old)
    if n != 1:
        sys.stderr.write("ERREUR " + label + ": count=" + str(n) + ", attendu=1\n")
        sys.stderr.write("old (debut 100): " + old[:100] + "\n")
        sys.exit(1)
    return content.replace(old, new, 1), n


with open(F, encoding="utf-8") as f:
    content = f.read()

before = len(content)
report = []

# ============================================================
# R1 - Saturation §3 : categoriser la liste des structures/acteurs
# ============================================================
old_r1 = (
    "L" + AP9 + "Association " + LOQ + "AJD" + ROQ + " (Accueil des Jeunes en Difficult" + AP9 + "e), pro-RIC, lanc" + AP9 + "ee en 2019, essoufflement en 2021. "
    + "M5S France tent" + AP9 + "e en 2018-2020, dissolution de facto en 2020. "
    + "Convergence Service Public 2020-2022, " + AP9 + "eteint 2022. "
    + "Les " + AP9 + "Emergents (Mouraud) 2019, dissous en 2020. "
    + "Mouraud sort des Gilets Jaunes en janvier 2019. "
    + "Drouet et Nicolle, poursuites judiciaires multiples 2019-2022."
)
new_r1 = (
    "Trois formes d'" + AP9 + "puisement se d" + AP9 + "gagent. "
    + "Essoufflement associatif " + AP9 + " (AJD lanc" + AP9 + "ee en 2019, essoufflement en 2021 ; Convergence Service Public 2020-2022, " + AP9 + "eteinte en 2022). "
    + AP9 + "Echec d'importation italienne " + AP9 + " (M5S France tent" + AP9 + "e en 2018-2020, dissolution de facto en 2020 ; Les " + AP9 + "Emergents lanc" + AP9 + "es en 2019, dissous en 2020). "
    + "Judiciarisation des figures de rue (Drouet et Nicolle, poursuites judiciaires multiples 2019-2022). Mouraud sort des Gilets Jaunes en janvier 2019."
)
content, n = apply(content, old_r1, new_r1, "R1 saturation §3")
report.append((n, "R1 saturation §3 : categorisation en 3 typologies"))

# ============================================================
# R2 - Glissement pamphletaire §3 : 3 replacements
# ============================================================
# R2a : titre de la categorie
old_r2a = "Ensuite, ceux qui meurent professionnellement de leur engagement pro-RIC."
new_r2a = "Ensuite, les porteurs neutralis" + AP9 + "es institutionnellement."
content, n = apply(content, old_r2a, new_r2a, "R2a titre")
report.append((n, "R2a titre categorie : 'qui meurent' -> 'neutralises'"))

# R2b : sous-titre bifurcation
old_r2b = "Mort par bifurcation tactique."
new_r2b = "Bifurcation partisane."
content, n = apply(content, old_r2b, new_r2b, "R2b bifurcation")
report.append((n, "R2b bifurcation : 'mort' supprimee"))

# R2c : sous-titre recyclage
old_r2c = "Recyclage p" + AP9 + "riph" + AP9 + "rique."
new_r2c = "Retrait post-carri" + AP9 + "ere."
content, n = apply(content, old_r2c, new_r2c, "R2c recyclage")
report.append((n, "R2c recyclage : terminologie sobre"))

# ============================================================
# R3 - Epithete M5S §4 : "parti populiste" -> "mouvement d'initiative numerique"
# ============================================================
old_r3 = (
    "Le Movimento 5 Stelle (M5S, parti populiste italien fond" + AP9 + "e par Beppe Grillo en 2009) italien, fond" + AP9 + "e en 2015"
)
new_r3 = (
    "Le Movimento 5 Stelle (M5S, mouvement d'initiative num" + AP9 + "erique italien fond" + AP9 + "e par Beppe Grillo en 2009), structur" + AP9 + "e en parti en 2013"
)
content, n = apply(content, old_r3, new_r3, "R3 epithete M5S")
report.append((n, "R3 epithete : 'parti populiste' -> 'mouvement d'initiative numerique'"))

# ============================================================
# R4 - Coherence §5 / Note d'auteur finale : suppression phrase parasite
# ============================================================
old_r4 = (
    "La port" + AP9 + "ee du diagnostic s'arr" + AP9 + "ete au constat du verrou. "
    + "Ce que ce dossier prouve, ce qu'il ne prouve pas, et la m" + AP9 + "ethode qu'il suit, sont consign" + AP9 + "es dans la note d'auteur finale."
)
new_r4 = (
    "La port" + AP9 + "ee du diagnostic, ce que ce dossier prouve, ce qu'il ne prouve pas, et la m" + AP9 + "ethode qu'il suit, sont consign" + AP9 + "es dans la note d'auteur finale."
)
content, n = apply(content, old_r4, new_r4, "R4 coherence §5")
report.append((n, "R4 coherence : suppression 's'arr\u00eate au constat du verrou'"))

# ============================================================
# R5 - Sur-referencement Truth Engine §5 : neutralisation reference L'Adieu aux partis
# ============================================================
# Anchor court sur le debut de la phrase de reference
old_r5 = "Comme l" + AP9 + "esquisse **[L" + AP9 + "Adieu aux partis : du diagnostic de Weil"
new_r5 = "Comme esquiss" + AP9 + "e dans un cadre prospectif ant" + AP9 + "erieur **(Trait" + AP9 + "e dans le diagnostic ant" + AP9 + "erieur de L" + AP9 + "Adieu aux partis : du diagnostic de Weil"
content, n = apply(content, old_r5, new_r5, "R5 surref §5")
report.append((n, "R5 surref : reference L'Adieu aux partis neutralisee"))

# ============================================================
# Persistance
# ============================================================
with open(F, "w", encoding="utf-8") as f:
    f.write(content)

after = len(content)

# ============================================================
# Rapport
# ============================================================
print("=" * 60)
print("RAPPORT APPLICATION 5 RECOMMANDATIONS PHASE 4")
print("=" * 60)
for n, label in report:
    print("  - " + label + ": " + str(n))
print("")
print("Longueur avant : " + str(before))
print("Longueur apres : " + str(after))
print("Diff : " + str(after - before))

em_count = content.encode("utf-8").count(b"\xe2\x80\x94")
print("Em-dash (LOI 3 cible 0) : " + str(em_count))

# Verification cible : anciens termes elimines
print("")
print("Anciens termes elimines :")
print("  - 'qui meurent' (cible 0) :", content.count("qui meurent professionnellement"))
print("  - 'Mort par bifurcation' (cible 0) :", content.count("Mort par bifurcation"))
print("  - 'parti populiste italien' (cible 0) :", content.count("parti populiste italien"))
print("  - 's'arr\u00eate au constat du verrou' (cible 0) :", content.count("s'arr\u00eate au constat du verrou"))

# Verification nouveaux termes presents
print("")
print("Nouveaux termes presents :")
print("  - 'neutralises institutionnellement' (cible 1) :", content.count("neutralis" + AP9 + "es institutionnellement"))
print("  - 'Bifurcation partisane' (cible 1) :", content.count("Bifurcation partisane"))
print("  - 'mouvement d'initiative numerique' (cible >= 1) :", content.count("mouvement d\u2019initiative num" + AP9 + "erique"))
print("  - 'Trois formes d'\\u00e9puisement' (cible 1) :", content.count("Trois formes d'" + AP9 + "puisement"))

print("")
print("PHASE 4 5 recommandations appliquees.")
