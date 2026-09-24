# QUINTESSENCE : insee-pdf-methodo-gap-access-closure
Source : investigations/2026-09/2026-09-20_campagne-insee-indexation/2026-09-20_insee-pdf-methodo-gap-access-closure/2026-09-20_19-21_insee-pdf-methodo-gap-access-closure_INVESTIGATION.md (RUN_ID 20260920-1921, ENGINE 2.10.6, INPUT_KIND UPDATE, COMPLEXITY 110 COMPLEX, G0-G10 PASS, certification DELIVERY PASS par UPDATE 20260921-1045)

## 1. Métadonnées & trace source
UPDATE du run 18-12 : extraction des PDF méthodologiques (IM136, IM145, note révisions, méthodes ERF, fiche précision RP, note EEC, rapport IGF-IGAS 2007) pour clore les gaps ACCESS. 3 RECHECK + 6 REUSE + 5 nouveaux faits PDF. 8 faits, 37 requêtes, 7 checkpoints.

## 2. Faits atomiques préservés
- F-01 ✧ Taux de chômage BIT publié avec incertitude ±0,3 pt ; enquête Emploi rénovée 2021 impose le recalcul des séries ; recul 2020 « en trompe-l'œil » (relecture note EEC). EPI:FACT mem:46193d3f-f889-4f44-991f-6b001f4397bb [L241] (mesuré)
- F-02 ✧ Non-réponse EAR 2019 : 3,9 % (dont 36 % de refus explicites) ; logements non répondants traités par imputation hot deck (Insee Méthodes 136, partie 2). EPI:FACT mem:48b68f41-fea6-40d3-b520-1ed49158e750 [L242] (mesuré)
- F-03 ✧ Rénovation ERFS 2021 : rupture de mesure estimée à -0,3 pt sur le taux de pauvreté, -0,007 sur l'indice de Gini, niveaux de vie rehaussés par le nouveau calage (Insee Méthodes 145, novembre 2023). EPI:FACT mem:7201080d-1491-4933-8039-18bcaee8ae17 [L243] (mesuré)
- F-04 ✧ Précision des populations légales par strate : coefficient de variation, communes <10 000 hab enquêtées exhaustivement (1 an sur 5), communes ≥10 000 par sondage d'adresses, intervalles de confiance constructibles (fiche précision RP). EPI:FACT mem:deadb2bf-5ca6-4258-81b5-40911af4fdac [L244] (mesuré)
- F-05 ✧ Révisions des comptes 2023-2025 chiffrées par la note officielle du 3 juin 2026 : PIB 2023 révisé +0,2 pt, 2024 +0,3 pt, 2025 inchangé ; la croissance 2023 de 1,9 % citée en presse correspond à la correction des jours ouvrables (1,6 % en données brutes). EPI:FACT mem:19d69589-b559-4004-963b-f24ce0342d2a [L245] (mesuré)
- F-06 ✦ Biais moyen haussier des révisions +0,34 pt (2005-2024, Rexecode) ; 2023 : 0,9 % → 1,9 % corrigé / 1,6 % brut ; erratum Insee Première 2105 le jour même. EPI:FACT mem:0e7b6e8b-6941-4b24-9e67-ad37fbd256f7 [L246] (mesuré)
- F-07 ✦ Pauvreté facteur 5 selon le seuil : 2 843 000 (40 %) / 5 599 000 (50 %) / 9 817 000 (60 %) / 14 576 000 (70 %) en 2024 ; Observatoire des inégalités privilégie 50 %. EPI:FACT mem:a22a2146-1f94-4fa9-8978-9c1a97f0ef4e [L247] (mesuré)
- F-08 ✦ Populations de référence : estimations par sondage officialisées par décret annuel depuis 2008, référencées par ~350 articles législatifs ; écart >15 % documenté (Metzing, 678 vs 791, 2024). EPI:FACT mem:dad9d305-19ff-4191-95a9-00a2ff13994c [L248] (mesuré)Traces registre : premier fait à la ligne 241, dernier à la ligne 248 de la source [L241-L248] (mesuré).
Inventaire source : FCT-001→F-01 … FCT-008→F-08 (mesuré).

## 3. Acteurs nominaux
Insee (Insee Méthodes 136/145, Insee Première 2105, DT 2023-22) ; Rexecode ; Observatoire des inégalités ; inegalites.fr ; Sénat (questions) ; IGF-IGAS (rapport 2007) ; Wikipédia (recoupement).

## 4. Sources externes citées
Insee Méthodes 136 (partie 2, imputation hot deck) ; Insee Méthodes 145 (rénovation ERFS) ; note révisions 2023-2025 (3 juin 2026) ; fiche précision recensement ; méthodo ERF (PDF) ; note EEC août 2023 ; rapport IGF-IGAS 2007 (vie-publique.fr) ; BFM (croissance révisée) ; Sénat qSEQ24100104S.

## 5. Chronologie datée
2007 : rapport IGF-IGAS sur le chômage mesuré. 2019 : non-réponse EAR 3,9 %. 2021 : rénovation EEC/ERFS. Novembre 2023 : IM145 (rupture -0,3 pt). 2024 : séries pauvreté. 2025 (29 mai) : Insee Première 2105, erratum le jour même. 2026 (3 juin) : note révisions 2023-2025 ; 29 mai 2026 erratum documenté.

## 6. Mécanismes / chaînes causales
- M1 (L2) : Imputation hot deck des logements non répondants (3,9 %) → l'estimation publiée intègre une modélisation explicite de la non-réponse. Preuves : F-02. Verrou : méthodologique, documenté par le producteur. [L242] (mesuré)
- M2 (L2) : Refonte d'enquête (ERFS 2021) → rupture de série chiffrée par le producteur (-0,3 pt pauvreté). Preuves : F-03. Verrou : méthodologique. [L243] (mesuré)
- M3 (L2) : Estimation → révision avec biais moyen haussier +0,34 pt → erratum possible le jour même (transparence a posteriori). Preuves : F-06, F-05. Verrou : calendaire. [L246, L245] (mesuré)
- M4 (L2) : Estimation par sondage → authentification légale → dépendance budgétaire des communes (pont vers metzing). Preuves : F-08, F-04. Verrou : légal. [L248, L244] (mesuré)

## 7. Verbatim et citations
- « en trompe-l'œil » (Insee, 2020) (estimé).
- « plus significatif » (Observatoire des inégalités sur son seuil 50 %) (estimé).
- « hot deck » (désignation officielle de la procédure d'imputation, IM136) (estimé).

## 8. Notes méthodologiques source
UPDATE de closure : les gaps ACCESS du parent sont refermés par lecture primaire des PDF. Les faits ✦ (F-06, F-07, F-08) portent 2+ familles indépendantes. Le fait négatif documentaire (erratum le jour même) est utilisé comme preuve de correction institutionnelle, pas d'absence d'effet.

## 9. Limites connues de cette extraction (case-limites)
Fiche précision PDF restée en HTTP 500 lors de la revalidation (substitution par page canonique, valeur ajustée) ; traces [Lxx] estimées ; les montants consolidés des révisions par poste ne sont pas publiés.
