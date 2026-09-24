# QUINTESSENCE : dgcl-notes-elasticite-part-population
Source : investigations/2026-09/2026-09-20_campagne-insee-indexation/2026-09-20_dgcl-notes-elasticite-part-population/2026-09-20_20-50_dgcl-notes-elasticite-part-population_INVESTIGATION.md (RUN_ID 20260920-2050, ENGINE 2.10.6, INPUT_KIND UPDATE, COMPLEXITY 0.85 COMPLEX, G0-G10 PASS, certification DELIVERY PASS 20260921)

## 1. Métadonnées & trace source
UPDATE du run 20-08 : notes DGCL récentes sur les modes de calcul de la dotation forfaitaire (part population, écrêtement complément de garantie) et confrontation au barème théorique 2025/2026. Recheck matériel de la mécanique DGF parent. 5 faits, 11 requêtes, 7 checkpoints. Découverte material : l'écrêtement courant vise les communes dont le PF dépasse 85 % de la moyenne nationale (vs 0,75×PF dans la note 2015) + CPS aux EPCI depuis LF 2024. [L17] (mesuré)

## 2. Faits atomiques préservés
- F-01 ✦ Mécanique DGF courante : population DGF (Insee + résidences secondaires + caravanes), écrêtement PF ≥ 85 % moyenne nationale, CPS intégrale aux EPCI depuis LF 2024 (art 240, loi 2023-1322). EPI:FACT mem:c816fe89-31d9-4fba-ab45-edafa5d83b64 [L169] (mesuré)
- F-02 ✧ Série DGF totale Metzing 2018-2026 (OFGL) : 70 565 / 72 911 / 89 723 / 96 504 / 101 883 / 104 300 / 105 906 / 109 808 / 114 005 EUR. EPI:FACT mem:3aca8f0f-304a-4eec-94a4-148302ed12c7 [L170] (mesuré)
- F-03 ✧ Part dynamique de la population (part population) de Metzing 2018-2026 : 670 / 1076 / 606 / 472 / 473 / 338 / 271 / 1430 / 1093 EUR ; taux implicites 2025 ~89,4 et 2026 ~68,3 EUR/hab DGF ajouté ; plage 2018-2026 24,9-140,5 EUR/hab. EPI:FACT mem:ccc17301-4ca5-4aaf-9c37-355052a649eb [L171] (mesuré)
- F-04 ✦ Chiffrage parent confirmé en 2026 : élasticité mesurée 86,9 EUR/hab, plage 7 300-14 600 EUR/an pour 113 hab ; mécanique légiférée inchangée ; corroboration régionale moselle.tv (Bouzonville). EPI:FACT mem:3774495b-2225-4679-a3e0-e62f56ba2e72 [L172] (mesuré)
- F-05 ✧ Écrêtement : formulation 2015 (0,75 × PF moyen) vs règle courante (PF ≥ 85 % moyenne nationale + plafond 1 % des recettes réelles de fonctionnement, moyenne 0,49 % en 2025). EPI:FACT mem:9677d17c-4cbf-4528-9a6b-07a178a97f3f [L173] (mesuré)Traces registre : premier fait à la ligne 169, dernier à la ligne 173 de la source [L169-L173] (mesuré).
Inventaire source : FCT-001→F-01 … FCT-005→F-05 (mesuré).

## 3. Acteurs nominaux
DGCL ; OFGL ; maire-info ; préfecture des Landes ; AMF ; moselle.tv ; commune de Metzing.

## 4. Sources externes citées
Page canonique DGCL ; API OFGL dotations-communes (2 requêtes) ; note DGCL 07-05-2015 relayée par maire-info ; communiqué DGF 2026 (préfète des Landes, 31-03-2026) ; AMF (critères répartition 2026) ; moselle.tv.

## 5. Chronologie datée
07-05-2015 : note DGCL (écrêtement 0,75 × PF moyen). 2024 : LF art 240 (CPS aux EPCI). 31-03-2026 : communiqué DGF 2026 (écrêtement 85 %, plafond 1 %). Séries OFGL 2018-2026. [L21] (mesuré)

## 6. Mécanismes / chaînes causales
- M1 (L2) : Population DGF (estimée) → part dynamique de la dotation forfaitaire, à un taux implicite mesurable par commune. Preuves : F-01, F-03. Verrou : législatif/réglementaire. [L169, L171] (mesuré)
- M2 (L2) : Les paramètres bougent sans chiffrage public du changement : écrêtement resserré (0,75 → 85 % de la moyenne) et transfert CPS (2024) modifient la distribution sans publication d'impact consolidé. Preuves : F-05, F-01. Verrou : législatif, défaut de publication d'impact. [L173, L169] (mesuré)

## 7. Verbatim et citations
- « l'écrêtement des communes dont le PF > 85 % de la moyenne nationale » (page canonique DGCL, reformulation) (estimé).
- « l'intégrité des montants de part CPS restant dans la forfaitaire a été transférée aux EPCI par l'art 240 de la LF 2024 » (reformulation F-01) (estimé). [L169] (mesuré)

## 8. Notes méthodologiques source
Le run valide la mécanique parente par confrontation barème théorique vs séries réelles OFGL. Les taux implicites calculés (89,4 puis 68,3 EUR/hab DGF ajouté) restent dans la plage du barème ; les années sans ajout de population DGF sont signalées non interprétables. Corroboration famille D régionale maintenue.

## 9. Limites connues de cette extraction (case-limites)
Barème DGCL complet non inspecté (notes relayées) ; écrêtement par commune non calculable sans données complémentaires ; traces [Lxx] estimées.
