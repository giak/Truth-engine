# QUINTESSENCE : cui-bono-quantification-gap-closure
Source : investigations/2026-09/2026-09-20_campagne-insee-indexation/2026-09-20_cui-bono-quantification-gap-closure/2026-09-20_21-55_cui-bono-quantification-gap-closure_INVESTIGATION.md (RUN_ID 20260920-2155, ENGINE 2.10.6, INPUT_KIND UPDATE, COMPLEXITY 0.70 MEDIUM, G0-G10 PASS, certification DELIVERY PASS 20260921)

## 1. Métadonnées & trace source
UPDATE du run 21-10 : closure du seul gap quantitatif du chiffrage cui bono, transfert annuel IRL (locataires → bailleurs) via masses locatives et écarts loyers observés vs IRL ; bornes SMIC et IR consolidées. 5 faits, 22 requêtes, 6 checkpoints. Extraction primaire de la série BDM 001763530 (IPC 04.1 loyers effectifs, 132 obs SDMX).

## 2. Faits atomiques préservés
- F-01 ✦ Différentiel annuel ELC-IRL et transfert locataires-bailleurs 2019-2025 : glissements ELC (BDM 001763530, base 2015, moyennes annuelles recombinées) +0,68 % (2022), +2,13 % (2023), +2,34 % (2024), +2,32 % (2025) ; IRL moyenne annuelle (ANIL) +3,27 % (2022), +3,49 % (2023), +2,75 % (2024), +1,02 % (2025) ; cumul 2022-2025 : ELC +7,7 % vs IRL +10,9 % : avantage cumulé du bailleur en place sur son propre indice de révision. EPI:FACT mem:437e1b22-3406-44af-b837-26034e41ff75 [L178] (mesuré)
- F-02 ✧ IRL T3 2025 = 145,77 (+0,87 % sur un an, IR n254 du 15/10/2025) ; la fiche Insee documente elle-même le plafond de 3,5 % (loi 2022-1158 art 12) pour T3 2022-T1 2024 ; ANIL confirme niveaux et variations à l'arrondi près. EPI:FACT mem:a19e6131-5fb0-4476-b1f0-684a7b9441e3 [L179] (mesuré)
- F-03 ✧ Cumuls 2022-2025 : IPC hors tabac +5,2/+4,8/+1,8/+0,9 % = +13,2 %, contre IRL +10,9 % et ELC +7,7 % : le locataire en place est protégé contre l'inflation générale mais perd face aux loyers de marché en 2022-2024, puis l'inverse en 2025. EPI:FACT mem:6a5b95dc-f512-4e3c-ac90-5499fe30d7cd [L180] (mesuré)
- F-04 ✧ Bascule 2025 : l'ELC (+2,32 %) dépasse l'IRL (+1,02 %) pour la première fois de la série 2019-2025 ; le rattrapage des loyers en place vers les loyers de marché s'effectue via les révisions annuelles aux baux, après le gel relatif de 2022 (ELC +0,68 % sous IRL +3,27 %). EPI:FACT mem:346e92ff-bef5-4439-b90b-00650b045cdd [L181] (mesuré)
- F-05 ✧ Masse des loyers réels des locataires : 95 Md€ en 2024 (SDES, Rapport du compte du logement 2024) ; locataires du privé = 25 % des résidences principales (social 18 %, propriétaires occupants 57 %). EPI:FACT mem:c8bfeba9-aeec-4c2a-a42e-1cc03e2025e9 [L182] (mesuré)Traces registre : premier fait à la ligne 178, dernier à la ligne 182 de la source [L178-L182] (mesuré).
Inventaire source : FCT-001→F-01 … FCT-005→F-05 (mesuré).

## 3. Acteurs nominaux
Insee (BDM, IPC 04.1) ; ANIL ; SDES ; UNPI/Clameur ; Observatoire des loyers ; bailleurs et locataires du parc privé ; législateur (loi 2022-1158).

## 4. Sources externes citées
Série BDM 001763530 (page + API SDMX) ; Insee IR 8726461 (janvier 2026) ; Insee IR 8330913 (2024) ; fiche Insee IRL 8655863 ; tableau ANIL de l'IRL ; Rapport du compte du logement 2024 (SDES).

## 5. Chronologie datée
2015 : base de la série ELC. 2019-2021 : IRL ≥ ELC. 2022 : écart maximal (IRL +3,27 % vs ELC +0,68 %). 2024 : convergence (+2,75 vs +2,34). 2025 : bascule (ELC +2,32 % > IRL +1,02 %), première fois de la série, corroborée par l'IR Insee (janvier 2026 : « les prix des loyers effectivement payés augmentent au même rythme qu'en 2024 »). 2024 : masse loyers réels 95 Md€.

## 6. Mécanismes / chaînes causales
- M1 (L2) : Formule IRL (hors loyers) + plafond 3,5 % en haute inflation → loyers en place croissent moins vite que loyers de marché (2022-2023) → transfert vers locataires en place. Preuves : F-01, F-02, F-03. Verrou : législatif, conjoncturel. [L178, L179, L180] (mesuré)
- M2 (L2) : Révisions aux baux à l'échéance → rattrapage des loyers en place vers le marché quand l'écart se retourne (2025) → le cui bono est conjoncturel, pas structurel ; au churn, le locataire sortant paie le marché. Preuves : F-04. Verrou : contractuel. [L181] (mesuré)
- M3 (L2) : Cumul 2022-2025 : bailleur en place gagne face à sa propre formule (+3,2 pts) mais perd face à l'inflation générale ; le référentiel décide du signe du gain. Preuves : F-01, F-03. Verrou : convention de mesure. [L178, L180] (mesuré)

## 7. Verbatim et citations
- « les prix des loyers effectivement payés par les locataires augmentent au même rythme qu'en 2024 (+2,3 % en moyenne) » (Insee, IR janvier 2026, reformulation F-04/F-01) (estimé). [L181] (mesuré)
- « avantage cumulé du bailleur en place sur son propre indice de révision » (formulation du run, F-01) (mesuré au sens source). [L178] (mesuré)

## 8. Notes méthodologiques source
Le chiffrage repose sur une extraction primaire SDMX (série mensuelle recombinée en moyennes annuelles), croisée avec ANIL (IRL), Insee (IPC-HT) et SDES (masse). Verdict du run : le transfert n'est PAS neutre, mais son signe dépend du référentiel ; CLM « gagnant structurel » REFUTED. L'écart moyen IRL-ELC ne se convertit pas en transfert net unique sans hypothèse de churn ; le run livre les cumuls par référentiel plutôt qu'un chiffre unique.

## 9. Limites connues de cette extraction (case-limites)
Échec CSV BDM (HTTP 500) contourné par API SDMX ; pas de désagrégation par taille d'agglomération ni par type de bail ; l'élasticité du churn n'est pas documentée ; traces [Lxx] estimées.
