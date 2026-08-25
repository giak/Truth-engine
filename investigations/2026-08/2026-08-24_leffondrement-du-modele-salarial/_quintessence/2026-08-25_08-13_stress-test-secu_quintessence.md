# SUBLIMATOR v36 — Quintessence Phase 1

**Source :** `2026-08-25_09-30_stress-test-secu_INVESTIGATION.md` (KERNEL COMPLEX, gate PASS)
**Horodatage extraction :** 2026-08-25 08:13 CEST

## 1. Métadonnées & trace source

Autorité : KERNEL COMPLEX, gate PASS. Loup : W-005. Verdict : −1 % emploi = −5,5 Md€ recettes Sécu. Déficit 21,6 Md€ piloté par dépense, pas IA. La Cour des comptes ne mentionne JAMAIS le lien IA → masse salariale → Sécu.

## 2. Faits atomiques préservés

- F-001 : Déficit Sécu 21,6 Md€ (2025), doublé en 2 ans, +haut depuis 2012 hors covid. EPI:FACT tier ✦ [L28] mem:25cd7d32
- F-002 : Recettes +2,6 % vs dépenses +3,6 % (2025). Le déficit est piloté par la dépense. EPI:FACT tier ✧ [L32] mem:25cd7d32
- F-003 : La Cour des comptes ne mentionne JAMAIS l'IA comme risque systémique dans son rapport mai 2026. EPI:GAP [L36] mem:-
- F-004 : FIPECO (juin 2026) : cotisations sociales = 443 Md€ (14,8 % PIB). 1 point de cotisation = 10,8 Md€. Élasticité 0,95. EPI:FACT tier ✧ [L40] mem:-
- F-005 : Chaque −1 % emploi = −5,5 Md€ recettes (cotisations + CSG). EPI:INFERENCE (calcul FIPECO) [L44] mem:-
- F-006 : Scénario érosion lente (−1,9 %) = 32 Md€ déficit total. Scénario médian (−4,9 %) = 49 Md€. Scénario noir 10 ans (−10 %) = 121 Md€. EPI:INFERENCE (bornes) [L48] mem:-
- F-007 : Allègements généraux cotisations 20,9→77 Md€ (2014-2024). EPI:FACT tier ✧ [L52] mem:-

## 3. Acteurs nominaux

- **Cour des comptes** : rapport mai 2026, pas de mention IA→Sécu
- **FIPECO** : données cotisations, élasticité
- **Gouvernement** : allègements 77 Md€ non conditionnés
- **Sénat** : rapport Coface/OEM 3,8-16,3 %

## 4. Sources externes citées

- Cour des comptes, 27 mai 2026 : Sécurité sociale 2026
- FIPECO, 20 juin 2026 : « Les cotisations sociales »
- Sénat r25-572 : Coface/OEM exposition IA

## 5. Chronologie datée

- 2014 : allègements 20,9 Md€
- 2024 : allègements 77 Md€
- 2025 : déficit Sécu 21,6 Md€
- Mai 2026 : rapport Cour des comptes (angle mort IA)
- Juin 2026 : FIPECO données 2025

## 6. Mécanismes / chaînes causales

**M1 : Angle mort IA dans prospective budgétaire** : Cour des comptes analyse déficit sans jamais modéliser lien IA → emploi → recettes → cet angle mort rend toute la prospective fragile. L1=absence mention, L2=absence modélisation, L3=verrou institutionnel (personne n'est mandaté). [§CAU:N]

**M2 : Dépense > recette, et l'IA aggravera** : déficit actuel = dépense (vieillissement, santé), pas IA. Mais si IA érode assiette, le déficit passe de « grave » à « catastrophe » sans que personne ne l'ait anticipé. L1=déficit structurel, L2=IA multiplicateur. [§CAU:N]

**M3 : Allègements 77 Md€ non conditionnés** : subvention massive au travail sans contrepartie emploi → si IA réduit emploi, les allègements restent → double peine (moins recettes + subventions maintenues). L1=conditionnalité absente. [§CAU:N]

## 7. Verbatim et citations

- **Cour des comptes** (mai 2026) : « Le déficit de la sécurité sociale a doublé en deux ans pour atteindre 21,6 Md€ en 2025 »
- **FIPECO** (juin 2026) : « Les cotisations sociales représentent 443 Md€, soit 14,8 % du PIB et 34,0 % des prélèvements obligatoires »

## 8. Notes méthodologiques source

- KERNEL COMPLEX, gate PASS.
- Bornes déficit = calcul élasticité FIPECO 0,95, pas prévisions.
- Nuance : élasticité exacte peut varier selon composition emploi détruit (cadres vs SMIC).

## 9. Limites connues de cette extraction (case-limites)

- −1 % = −5,5 Md€ = approximation (dépend du mix emploi détruit : cadres rapportent plus que SMIC).
- Bornes 32/49/121 Md€ = ordres grandeur, pas prédictions.
- Angle mort Cour des comptes = absence documentée, pas preuve absence (pourrait exister note interne).
- Traces (estimé).