#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Application des 4 corrections P1 restantes sur l'article RIC (PHASE 3 v2).
P1.2 §2 a deja ete appliquee (via str_replace).
P1.3 §5 allegement a deja ete appliquee (via str_replace silencieux).

Corrections restantes : P1.1, P1.3 paragraphe, P1.4 paragraphe x2.
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
        sys.exit(1)
    return content.replace(old, new, 1), n


with open(F, encoding="utf-8") as f:
    content = f.read()

before = len(content)
report = []

# -----------------------------------------------------
# P1.1 - Artefact "INFORMATION-COMBINATOIRE-philosophique"
# -----------------------------------------------------
content, n = apply(
    content,
    "INFORMATION-COMBINATOIRE-philosophique",
    "Doctrine-constitutionnelle",
    "P1.1"
)
report.append((n, "P1.1 artefact"))

# -----------------------------------------------------
# P1.3 paragraphe 6 strates (insertion apres fin paragraphe 3)
# -----------------------------------------------------
old3 = "pas l" + AP9 + "absence de rel\u00e8ve."
new3 = (
    "pas l" + AP9 + "absence de rel\u00e8ve.\n\n"
    "Six strates institutionnelles ou culturelles dessinent un alignement diffus sans coordination explicite. "
    "Les quatre cultes \u00e9tablis (\u00c9glise catholique, "
    + "F\u00e9d\u00e9ration protestante de France, Conseil fran\u00e7ais du culte musulman, "
    + "Consistoire central Isra\u00e9lite) manifestent concordamment une prudence publique "
    + "sur l" + AP9 + "extension de l" + AP9 + "initiative populaire. "
    + "La franc-ma\u00e7onnerie, par sa tradition r\u00e9publicaine centralisatrice ancienne, "
    + "nourrit un consensus parall\u00e8le. "
    + "Les organisations syndicales repr\u00e9sentatives (CGT, CFDT, FO), "
    + "h\u00e9riti\u00e8res de la Charte d" + AP9 + "Amiens de 1906, "
    + "ont construit une lecture parlementariste de la Ve R\u00e9publique depuis 1958 "
    + "peu compatible avec l" + AP9 + "initiative populaire directe. "
    + "Les cabinets de conseil (l" + AP9 + "Institut Montaigne, la *Chatham House Rule*) "
    + "et les lobbys \u00e9conomiques diffusent une pr\u00e9f\u00e9rence structurelle "
    + "pour la d\u00e9mocratie repr\u00e9sentative. "
    + "Aucune de ces six strates n" + AP9 + "a publi\u00e9 de prise de position commune officielle. "
    + "L" + AP9 + "alignement n" + AP9 + "est pas concert\u00e9. Il n" + AP9 + "en est pas moins lisible."
)
content, n = apply(content, old3, new3, "P1.3 paragraphe 6 strates")
report.append((n, "P1.3 paragraphe 6 strates"))

# -----------------------------------------------------
# P1.4 §4 - Statut CEDH intermediaire
# -----------------------------------------------------
old4 = (
    "La jurisprudence 2023-2024 en mati\u00e8re environnementale "
    "ouvre la voie \u00e0 un recours individuel contre les politiques publiques insuffisantes. "
    + "L" + AP9 + "extension au cas fran\u00e7ais reste conjecturale, mais l" + AP9 + "architecture existe"
    + NBSP
    + ": la CEDH peut servir de levier externe pour forcer le l\u00e9gislateur "
    + "fran\u00e7ais \u00e0 int\u00e9grer une proc\u00e9dure d" + AP9 + "initiative populaire "
    + "en mati\u00e8re de droits fondamentaux."
)
new4 = (
    "La jurisprudence 2023-2024 en mati\u00e8re environnementale "
    "dessine une voie externe dont le pr\u00e9c\u00e9dent appliqu\u00e9 fait encore d\u00e9faut. "
    + "L" + AP9 + "extension au cas fran\u00e7ais d\u00e9pend de facteurs jurisprudentiels "
    + "non encore jug\u00e9s"
    + NBSP
    + ": la voie est en construction, l" + AP9 + "architecture existe, "
    + "le pr\u00e9c\u00e9dent reste \u00e0 \u00e9tablir."
)
content, n = apply(content, old4, new4, "P1.4 paragraphe")
report.append((n, "P1.4 paragraphe"))

# -----------------------------------------------------
# P1.4 §5 - Statut CEDH effet direct -> en construction
# -----------------------------------------------------
old5 = "soit un levier supranational CEDH effet direct"
new5 = "soit une jurisprudence CEDH en construction (article 3, environnement 2023-2024)"
content, n = apply(content, old5, new5, "P1.4 liste")
report.append((n, "P1.4 liste"))

# -----------------------------------------------------
# Persistance
# -----------------------------------------------------
with open(F, "w", encoding="utf-8") as f:
    f.write(content)

after = len(content)

# -----------------------------------------------------
# Rapport
# -----------------------------------------------------
print("=" * 60)
print("RAPPORT APPLICATION 4 CORRECTIONS P1 RESTANTES")
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
print("PHASE 3 corrections restantes terminees.")
