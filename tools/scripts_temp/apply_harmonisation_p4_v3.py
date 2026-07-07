#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Application PHASE 4 v3 — 4 recommandations (R2-R5).
R1 SKIP : chaîne longue avec multiples pièges Unicode (apostrophes typographiques
    et NBSP), à traiter séparément ou abandonner.
R2 : 3 replacements (R2a/b/c) — anti-pamphletaire §3.
R3 : epithete M5S §4 (parti populiste -> mouvement d'initiative numerique).
R4 : coherence §5 / Note d'auteur (suppression phrase parasite).
R5 : sur-referencement Truth Engine §5 + NBSP integre.
"""

import sys

F = "/home/giak/projects/truth-engine/articles/2026-07-08_22-00_ric_verrouillage_francais_anatomie_ARTICLE.md"

# Caracteres typographiques pieges
AP9 = "\u2019"   # apostrophe typographique droite
NBSP = "\u00a0"  # espace insecable


def apply(content, old, new, label):
    """Remplace old par new en exigeant count == 1, sinon abort."""
    n = content.count(old)
    if n != 1:
        sys.stderr.write("ERREUR " + label + ": count=" + str(n) + ", attendu=1\n")
        sys.stderr.write("old (debut 120): " + old[:120] + "\n")
        sys.exit(1)
    return content.replace(old, new, 1), n


with open(F, encoding="utf-8") as f:
    content = f.read()

before = len(content)
report = []

# ============================================================
# R2a - Titre de categorie \u00a73
# ============================================================
old_r2a = "Ensuite, ceux qui meurent professionnellement de leur engagement pro-RIC."
new_r2a = "Ensuite, les porteurs neutralis" + AP9 + "es institutionnellement."
content, n = apply(content, old_r2a, new_r2a, "R2a titre")
report.append((n, "R2a : 'qui meurent' -> 'neutralises institutionnellement'"))

# ============================================================
# R2b - Sous-titre bifurcation
# ============================================================
old_r2b = "Mort par bifurcation tactique."
new_r2b = "Bifurcation partisane."
content, n = apply(content, old_r2b, new_r2b, "R2b bifurcation")
report.append((n, "R2b : 'Mort' supprimee, terme sobre"))

# ============================================================
# R2c - Sous-titre recyclage
# ============================================================
old_r2c = "Recyclage p" + AP9 + "riph" + AP9 + "rique."
new_r2c = "Retrait post-carri" + AP9 + "ere."
content, n = apply(content, old_r2c, new_r2c, "R2c recyclage")
report.append((n, "R2c : 'Recyclage periph' -> 'Retrait post-carriere'"))

# ============================================================
# R3 - Epithete M5S \u00a74
# ============================================================
old_r3 = (
    "Le Movimento 5 Stelle (M5S, parti populiste italien fond" + AP9 + "e par Beppe Grillo en 2009) italien, fond" + AP9 + "e en 2015"
)
new_r3 = (
    "Le Movimento 5 Stelle (M5S, mouvement d'initiative num" + AP9 + "erique italien fond" + AP9 + "e par Beppe Grillo en 2009), structur" + AP9 + "e en parti en 2013"
)
content, n = apply(content, old_r3, new_r3, "R3 epithete M5S")
report.append((n, "R3 : 'parti populiste' -> 'mouvement d\u2019initiative num\u00e9rique'"))

# ============================================================
# R4 - Coherence \u00a75 / Note d'auteur : suppression phrase parasite
# ============================================================
old_r4 = (
    "La port" + AP9 + "ee du diagnostic s'arr" + AP9 + "ete au constat du verrou. "
    + "Ce que ce dossier prouve, ce qu'il ne prouve pas, et la m" + AP9 + "ethode qu'il suit, sont consign" + AP9 + "es dans la note d'auteur finale."
)
new_r4 = (
    "La port" + AP9 + "ee du diagnostic, ce que ce dossier prouve, ce qu'il ne prouve pas, et la m" + AP9 + "ethode qu'il suit, sont consign" + AP9 + "es dans la note d'auteur finale."
)
content, n = apply(content, old_r4, new_r4, "R4 coherence finale")
report.append((n, "R4 : suppression phrase parasite 's'arr\u00eate au constat du verrou'"))

# ============================================================
# R5 - Sur-referencement Truth Engine \u00a75 (NBSP integre)
# ============================================================
old_r5 = (
    "Comme l" + AP9 + "esquisse **[L" + AP9 + "Adieu aux partis" + NBSP
    + ": du diagnostic de Weil"
)
new_r5 = (
    "Quelques principes esquiss" + AP9 + "es cadrent la r" + AP9 + "eflexion prospective **[L" + AP9 + "Adieu aux partis" + NBSP
    + ": du diagnostic de Weil"
)
content, n = apply(content, old_r5, new_r5, "R5 surref \u00a75")
report.append((n, "R5 : 'Comme l\u2019esquisse' -> 'Quelques principes esquiss\u00e9s cadrent la r\u00e9flexion prospective'"))

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
print("RAPPORT APPLICATION 4 RECOS PHASE 4 (R1 SKIPPED)")
print("=" * 60)
for n, label in report:
    print("  - " + label + ": " + str(n) + " remplacement")
print("")
print("Longueur avant : " + str(before))
print("Longueur apres : " + str(after))
print("Difference : " + str(after - before))

em_count = content.encode("utf-8").count(b"\xe2\x80\x94")
print("")
print("Em-dash (LOI 3 cible 0) : " + str(em_count))

print("")
print("Verification cible des 4 recos :")
print("  R2a 'neutralisees institutionnellement' present :", content.count("neutralis" + AP9 + "es institutionnellement"))
print("  R2b 'Bifurcation partisane' present :", content.count("Bifurcation partisane"))
print("  R2c 'Retrait post-carriere' present :", content.count("Retrait post-carri" + AP9 + "ere"))
print("  R3 'mouvement d\u2019initiative' present :", content.count("mouvement d\u2019initiative num" + AP9 + "erique"))
print("  R4 's\u2019arr\u00eate au constat' elimine :", content.count("s'arr" + AP9 + "ete au constat du verrou"))
print("  R5 'Quelques principes' present :", content.count("Quelques principes esquiss" + AP9 + "es"))

print("")
print("Residus R1 NON apprehende :")
print("  AJD + Lancement 2019 + essoufflement 2021 :", "inchange (R1 skip)")
print("")

print("PHASE 4 v3 4 recos appliquees (R1 differee).")
