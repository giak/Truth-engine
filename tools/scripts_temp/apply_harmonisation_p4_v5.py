#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHASE 4 — Harmonisation controlee v5.
Application byte-exact : anchors utilisant chr(0x2019) typographique (U+2019 right single quotation mark)
identique au caractere utilise dans le fichier source.

Substitutions visees :
  - P1.2 §2 : ajouter 5e strate supranationale (BCE/UE) — corrige defaut P1 non applique
  - R2a : titre §3 — qui meurent professionnellement -> neutralises institutionnellement
  - R2b : Mort par bifurcation tactique -> Bifurcation partisane
  - R2c : Recyclage periferhique -> Retrait post-carriere
  - R3 : M5S parti populiste italien -> mouvement d'initiative civique institutionnalise en parti de centre-gauche (PDS, F033)
  - R4 : suppression phrase parasite 'La portee du diagnostic s'arrete au constat du verrou'
  - R5 : Comme l'esquisse -> Quelques principes esquisses
  - R1 marqueur : ajout pivot syntaxique 'Trois formes' au debut du flux §3
"""
from pathlib import Path

F = Path('/home/giak/projects/truth-engine/articles/2026-07-08_22-00_ric_verrouillage_francais_anatomie_ARTICLE.md')

AP9 = '\u2019'  # right single quotation mark (typographique)

# Lecture
c = F.read_text(encoding='utf-8')

# Liste des substitutions : chaque item = (label, old, new)
OPS = []

# === P1.2 §2 : 5e strate supranationale ===
OPS.append((
    'P1.2_strate_supranationale',
    "Juridique-constitutionnelle d" + AP9 + "abord : quatre verrous cumul" + AP9 + "es, doctrine constante, jurispruden"
    "ce syst" + AP9 + "ematique.",
    "Juridique-constitutionnelle d" + AP9 + "abord : quatre verrous cumul" + AP9 + "es (art. 11 al. 3, art. 89 al. 4, "
    "art. 16, art. 61-1 QPC), une cinqui" + AP9 + "eme strate supranationale (BCE OMT 6 sept 2012 Draghi, "
    "TPI 21 juil 2022 Lagarde, art. 50 TUE retrait volontaire, BVerfG 5 mai 2020 OMT ultra vires), "
    "doctrine constante, jurisprudence syst" + AP9 + "ematique."
))

# === R2a : titre §3 ===
OPS.append((
    'R2a_titre_S3',
    "## §3. Les acteurs : ceux qui verrouillent, ceux qui meurent",
    "## §3. Les acteurs : ceux qui verrouillent, ceux qui sont neutralis" + AP9 + "es institutionnellement"
))

# === R2b : Mort par bifurcation tactique -> Bifurcation partisane ===
OPS.append((
    'R2b_bifurcation_partisane',
    "Mort par bifurcation tactique.",
    "Bifurcation partisane."
))

# === R2c : Recyclage peripherique -> Retrait post-carriere ===
OPS.append((
    'R2c_retrait_post_carriere',
    "Recyclage p" + AP9 + "riph" + AP9 + "erique.",
    "Retrait post-carri" + AP9 + "ere."
))

# === R3 : M5S mouvement d'initiative ===
OPS.append((
    'R3_m5s_mouvement',
    "Le Movimento 5 Stelle (M5S, parti populiste italien fond" + AP9 + "e par Beppe Grillo en 2009) italien",
    "Le Movimento 5 Stelle (M5S, mouvement d" + AP9 + "initiative civique italien fond" + AP9 + "e par Beppe Grillo "
    "le 4 octobre 2009, institutionnalis" + AP9 + "e en parti politique en 2015)"
))

# === R4 : suppression phrase parasite — utilise .replace avec count=1 puis strip ligne ===
OPS.append((
    'R4_suppression_phrase_parasite',
    "La port" + AP9 + "ee du diagnostic s" + AP9 + "arr" + AP9 + "ete au constat du verrou. ",
    ""
))

# === R5 : pivot syntaxique L'Adieu aux partis ===
OPS.append((
    'R5_pivot_adieux_partis',
    "Comme l" + AP9 + "esquisse",
    "Quelques principes esquiss" + AP9 + "s"
))

# === R1 marqueur §3 : insertion du pivot syntaxique "Trois formes d'extinction" ===
# On remplace l'amorce "Ensuite, ceux qui meurent professionnellement" par
# "Trois formes d'extinction des porteurs pro-RIC."
# Note : ne PAS dupliquer R2a — ici on transforme la phrase interne du paragraphe
OPS.append((
    'R1_marqueur_trois_formes',
    "Ensuite, ceux qui meurent professionnellement de leur engagement pro-RIC.",
    "Trois formes d" + AP9 + "extinction des porteurs pro-RIC sont document" + AP9 + "es."
))

# Application
applied = []
errors = []

for label, old, new in OPS:
    n_in = c.count(old)
    if n_in != 1:
        errors.append(f'{label}: count={n_in} (attendu 1). ECHEC.')
        continue
    c = c.replace(old, new, 1)
    applied.append(label)
    print(f'[OK] {label} : applique.')

# Ecriture
F.write_text(c, encoding='utf-8')

print()
print(f'TOTAL applique : {len(applied)}/{len(OPS)}')
for label in applied:
    print(f'  - {label}')
if errors:
    print()
    print('ERREURS :')
    for e in errors:
        print(f'  ! {e}')
