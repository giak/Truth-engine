# QUINTESSENCE : insee-effet-controle-externe-et-analyse-independante
Source : investigations/2026-09/2026-09-20_campagne-insee-indexation/2026-09-21_insee-effet-controle-externe-et-analyse-independante/2026-09-21_03-47_insee-effet-controle-externe-et-analyse-independante_INVESTIGATION.md (RUN_ID 20260921-0347, ENGINE 2.10.6, INPUT_KIND UPDATE, COMPLEXITY 10 APEX, G0-G10 PASS, DELIVERY PASS)

## 1. Métadonnées & trace source
UPDATE du run 03-14 : deux branches ouvertes : le gap CAUSALITY du CAU-003 (effet du contrôle externe sur les taux de réponse) et la pénalité MISSING_COUNTER (analyse indépendante du SSP). 10 faits, 9 requêtes, 7 checkpoints. Réponse : la question causale est refermée en tant que question, non comblée par une mesure.

## 2. Faits atomiques préservés
- F-01 ✧ T1 2023 : taux de collecte 64 %, taux de réponse 77 % (l'écart vient des résidences non principales hors champ). EPI:FACT mem:e19bd438-9794-4f88-81b1-a47b6fa66e8e [L392] (mesuré)
- F-02 ✧ Collecte fortement affectée à partir de la fin T1 2020 (crise sanitaire) ; retour au niveau d'avant-crise depuis le T1 2022. EPI:FACT mem:bcf6304d-4489-49cf-87b9-1688abf2c72b [L393] (mesuré)
- F-03 ✧ T3 2025 : collecte 60,6 % (-1,1 pt sur un an), réponse 73,7 %, internet 46,4 % des réinterrogations. EPI:FACT mem:f8c3301b-b5ae-4e89-81e9-69ffcff82b0d [L394] (mesuré)
- F-04 ✦ Intervalle de confiance à 95 % du taux de chômage trimestriel : ±0,3 pt, en niveau comme en évolution ; publié par le producteur et restitué indépendamment par la commission d'enquête du Sénat (avec la nuance du producteur). EPI:FACT mem:a304c931-3b04-468e-9fe7-8499a15f37a7 [L395] (mesuré)
- F-05 ✧ Table de précision des principaux indicateurs non corrigés des variations saisonnières au T3 2025, par sexe et classe d'âge (chômage, halo, emploi). EPI:FACT mem:d8078d11-2fc3-4e6d-aa44-70c493f6f92a [L396] (mesuré)
- F-06 ✧ RSA : sous-estimation nette dans l'enquête Emploi jusqu'au T2 2024 ; à partir du T3 2024, couverture ~90 % via appariement Pasrau, série passée corrigée sans rupture. EPI:FACT mem:e8b973fc-3a7d-4451-a427-c43bd058e37c [L397] (mesuré)
- F-07 ✧ Suspension de la labellisation des nouvelles statistiques de demandeurs d'emploi inscrits du 1er janvier 2025 au 20 mai 2026 (ASP), stabilité et interprétabilité garanties seulement à l'issue de la transition. EPI:FACT mem:82b79206-911f-4d0f-a8da-f3c68de0455c [L398] (mesuré)
- F-08 ✧ L'ASP attire l'attention sur la nécessité d'un suivi et d'une analyse des impacts de la loi « Pour le plein emploi » sur les séries BIT. EPI:FACT mem:a336384f-cf59-42d6-bcee-bef177e0d55b [L399] (mesuré)
- F-09 ✧ L'ASP relève l'écart grandissant (relevé par des chercheurs) entre sources administratives d'emploi et actifs occupés de l'enquête Emploi, et juge importante l'explicitation des sources de divergence. EPI:FACT mem:41c7ee98-cf40-4c5f-ba99-842e4e40e6bf [L400] (mesuré)
- F-10 ✧ Incident de publication T1 2013 (Sénat, commission d'enquête) : trois facteurs identifiés par l'Insee (refonte de la chaîne de traitements, non-réponse liée au nouveau cadre d'emploi des enquêteurs, rénovation du questionnaire). EPI:FACT mem:58589655-de0e-4cb0-898e-9bb2f1a3c540 [L401] (mesuré)Traces registre : premier fait à la ligne 392, dernier à la ligne 401 de la source [L392-L401] (mesuré).
Inventaire source : FCT-001→F-01 … FCT-010→F-10 (mesuré).

## 3. Acteurs nominaux
Insee ; Autorité de la statistique publique ; CNIS ; commission d'enquête du Sénat (2016) ; Dares ; chercheurs (écart sources administratives/enquête) ; ménages répondants.

## 4. Sources externes citées
Note méthodologique EEC août 2023 ; note méthodologique T3 2025 ; rapport annuel ASP 2024 (famille D) ; avis CNIS 2020 (prolongation) ; rapport commission d'enquête Sénat r16-003 (famille B, 2016).

## 5. Chronologie datée
2013 : incident de publication T1. 2016 : commission d'enquête Sénat. 8-10-2020 : avis initial (aucune exigence sur les taux). 2020-2022 : crise sanitaire et retour. 2024 : correction RSA (couverture 90 %). 01-01-2025 → 20-05-2026 : suspension de labellisation des statistiques de demandeurs d'emploi. T3 2025 : collecte 60,6 %. 2026-2030 : cycle de contrôle avec exigences sur les taux (pour l'exercice 2027-2030).

## 6. Mécanismes / chaînes causales
- M1 (L2) : Le cycle de contrôle 2020-2025 ne formulait AUCUNE exigence relative aux taux de réponse → l'effet du contrôle sur les variations observées n'est pas identifiable (pas d'attribution, exigences postérieures, attributions concurrentes : crise sanitaire, causes opérationnelles). Preuves : F-01-F-03, F-10. Verrou : documentaire (fait négatif établi).
- M2 (L2) : L'effet établi du contrôle porte sur le STATUT de publication (suspension de labellisation 2025-2026), pas sur la valeur des indicateurs. Preuves : F-07, F-08. Verrou : institutionnel.
- M3 (L2) : Le chiffre conjoncturel est diffusé sans incertitude attachée ; ni le contrôle ni la commission n'abordent ce point (Ξ omission à 4). Preuves : F-04 vs diffusion (table de précision F-05 séparée). Verrou : éditorial/organisationnel.

## 7. Verbatim et citations
- « non identifiable dans les documents publics » n'est pas « inexistant » (formulation du run, limite de la réponse causale) (mesuré au sens source).
- « leur stabilité et leur interprétabilité ne pourront être garanties qu'à l'issue de la période de transition » (ASP, reformulation F-07) (estimé).

## 8. Notes méthodologiques source
Le fait clé négatif (aucune exigence sur les taux dans le cycle 2020-2025) est ce qui rend la mesure impossible sur la période : c'est un résultat, pas un échec. Perspective obtenue indépendante du producteur (famille D) mais non opposée : aucune source contestant l'intervalle publié. 6 faits sur 10 reposent au moins partiellement sur le producteur, signalé au seuil exact.

## 9. Limites connues de cette extraction (case-limites)
Figures de taux de réponse non extractibles en texte ; textes légaux et règlement UE non inspectés (NQ-002) ; aucune pièce budgétaire retrouvée (AXS-004) ; les actes institutionnels signés par des organes, pas des personnes ; traces [Lxx] estimées.
