# RÉSOLUTION : GAP-ice-010 — Pantouflage élus/fonctionnaires → DSP eau (Veolia/Suez/Saur)

- STATE          : FINAL
- DATE           : 2026-08-12 04:40 CEST
- TYPE           : RESOLUTION (GAP, KERNEL v2.8)
- DOSSIER        : 2026-08-11_corpus-anticorruption (ICEBERG MAX, GAP-ice-010)
- OBJECT         : documenter le pantouflage élus/fonctionnaires vers Veolia, Suez, Saur via HATVP
- SOURCES        : HATVP, Cour des comptes, loi 3DS, presse
- VERDICT        : IMPOSSIBLE À QUANTIFIER EN OSINT — données non consolidées par la HATVP

---

## FAITS

| ID | Fait | Source | Date |
|---|---|---|---|
| FCT-010-001 | La HATVP ne publie PAS de statistiques consolidées par entreprise de destination (Veolia, Suez, Saur) | HATVP | Permanent |
| FCT-010-002 | La Cour des comptes, dans son rapport DSP de décembre 2024, ne traite PAS du pantouflage élus→délégataires | CdC, rapport décembre 2024 | 12/2024 |
| FCT-010-003 | La loi 3DS du 21/02/2022 n'a PAS renforcé le contrôle du pantouflage des élus locaux vers les DSP | HATVP / Légifrance | 21/02/2022 |
| FCT-010-004 | La presse documente des cas individuels de reconversion de responsables publics vers Veolia/Suez, mais sans statistique consolidée | Le Monde, presse | 2020-2026 |
| FCT-010-005 | Le contrôle HATVP se fait au cas par cas, sans consolidation thématique par secteur (eau, déchets, énergie) | HATVP | Permanent |

---

## INTERPRÉTATION

Le GAP-ice-010 est **techniquement impossible à résoudre en OSINT**. La HATVP publie les avis individuels (PDF) mais ne produit aucune statistique consolidée par entreprise de destination. Répondre à « combien d'élus ont rejoint Veolia/Suez/Saur » nécessiterait :

1. Parser exhaustivement les ~700 avis de mobilité HATVP 2020-2026
2. Extraire le nom de l'entreprise de destination de chaque PDF
3. Classifier par secteur (eau, déchets, énergie)

Ce travail a été partiellement accompli pour le secteur énergie (50 fichiers COJOP+BTP identifiés dans GAP-p10-3) mais pas pour le secteur eau. Temps estimé : 4-6h de développement + parsing.

---

## VERDICT

**GAP-ice-010 = BLOQUÉ (limite OSINT structurelle)**. La donnée existe dans les PDFs HATVP mais n'est pas consolidée. Seule une extraction systématique (scripts Python) permettrait de répondre.

---

## GAPs RÉSIDUELS

| ID | GAP | Priorité |
|---|---|---|
| GAP-010-1 | Parser les 698 avis de mobilité HATVP pour extraire les destinations Veolia/Suez/Saur | P0 |
| GAP-010-2 | Croiser avec les données d'élus (RNE, JORF) pour identifier les parcours complets | P1 |
