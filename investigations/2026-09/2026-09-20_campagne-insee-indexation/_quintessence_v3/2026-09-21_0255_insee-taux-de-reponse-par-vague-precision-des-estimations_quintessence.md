# QUINTESSENCE : insee-taux-de-reponse-par-vague-precision-des-estimations
Source : investigations/2026-09/2026-09-20_campagne-insee-indexation/2026-09-21_insee-taux-de-reponse-par-vague-precision-des-estimations/2026-09-21_02-55_insee-taux-de-reponse-par-vague-precision-des-estimations_INVESTIGATION.md (RUN_ID 20260921-0255, ENGINE 2.10.6, INPUT_KIND TOPIC, COMPLEXITY 12 APEX, G0-G10 PASS, DELIVERY PASS)

## 1. Métadonnées & trace source
Investigation TOPIC : taux de réponse par vague et précision des estimations publiées (chômage BIT, population légale, recensement, enquêtes ménages), France, 2003-2026. 9 faits, 11 requêtes, 7 checkpoints. Lead hérité réfuté dans sa formulation : le déficit est de centralisation, pas d'accès.

## 2. Faits atomiques préservés
- F-01 ✧ EEC 2021 : 77 % de réponse dans le champ, 56 % en résidences non principales. EPI:FACT mem:d422fb4d-9a88-4ccf-a99d-5ecfd01129ef [L390] (mesuré)
- F-02 ✧ T2 2023 : taux de collecte 60,5 % (1re interrogation) et 64,3 % (réinterrogation), France hors Mayotte (DT2023-22, figure 25). EPI:FACT mem:a95a5c49-17c4-48db-96b7-9d0e81213937 [L391] (mesuré)
- F-03 ✧ Précision publiée d'un effectif communal (RP 2018) : effectif 4 900 → écart-type 140, CV 3 %, intervalle 95 % [4 620 ; 5 180]. EPI:FACT mem:fadd770e-70ec-4e67-b5e7-ab6b46d7459f [L392] (mesuré)
- F-04 ✧ Erreur de sondage nationale : CV 0,01 %, soit ±17 500 personnes. EPI:FACT mem:2083635a-f7b7-4c19-b789-77f2c5086b36 [L393] (mesuré)
- F-05 ✧ Communes 10 000-19 999 hab : CV médian < 1,16 %. EPI:FACT mem:01274ca1-fe49-4720-aa8b-0490edca9eaf [L394] (mesuré)
- F-06 ✧ Non-réponse partielle selon le mode (EEC 2021) : 2,75 % des logements enquêtés par internet ; non-réponse individuelle ≈ 1 %. EPI:FACT mem:64a63224-5d71-4b4c-a075-4b4f-b508-955b8d922d4c [L395] (mesuré)
- F-07 ✧ Baromètre entreprises 2023 : 65 enquêtes, 1 171 871 questionnaires, taux de réponse moyen 70,2 % (+3,5 pts). EPI:FACT mem:8de4cc5b-d03a-4a4f-978d-83d02db94fce [L396] (mesuré)
- F-08 ✧ Déterminants de la non-réponse : résidences non principales, Paris, locataires, QPV ; variables explicatives : région, type de logement, nombre de pièces. EPI:FACT mem:dc619b96-975a-4c2e-93b9-07ac14d6c424 [L397] (mesuré)
- F-09 ✧ Non-réponse LFS dans l'UE (2011) : de 2,1 % (Allemagne) à 67,3 % (Luxembourg) ; le rapport qualité UE juge la comparaison impossible. EPI:FACT mem:423f9c24-49fc-4acd-b00c-4d8a2a3870fa [L398] (mesuré)Traces registre : premier fait à la ligne 390, dernier à la ligne 398 de la source [L390-L398] (mesuré).
Inventaire source : FCT-001→F-01 … FCT-009→F-09 (mesuré).

## 3. Acteurs nominaux
Insee ; Eurostat ; ménages échantillonnés ; entreprises enquêtées ; baromètre de charge de réponse ; ASP et CNIS (mentionnés, non inspectés à ce run).

## 4. Sources externes citées
Fiche précision recensement (PDF) ; DT2023-22 (PDF) ; baromètre de charge de réponse entreprises (page Insee) ; page enquête Emploi (5398681) ; Eurostat statistics-explained (LFS non-réponse).

## 5. Chronologie datée
2003-2026 : période de l'objet. 2016-2020 : enquêtes de la fiche précision. 2021 : nouvelle EEC (internet en réinterrogation ; 77 % du champ). T2 2023 : collecte par rang 60,5/64,3 %. 2023 : baromètre entreprises 70,2 %. Juin 2026 : avis CNIS identifié, non inspecté (HTTP 403, clos par le run suivant).

## 6. Mécanismes / chaînes causales
- M1 (L2) : Non-réponse différentielle (résidences non principales, Paris, locataires, QPV) → charge de la précision déplacée vers le modèle de correction. Preuves : F-08, F-01. Verrou : méthodologique. [L397, L390] (mesuré)
- M2 (L2) : Asymétrie documentaire entreprises/ménages : baromètre agrégé annuel publié pour les entreprises, équivalent absent pour les ménages → l'usager du chiffre conjoncturel supporte la reconstitution de l'incertitude. Preuves : F-07 vs F-01/F-02. Verrou : organisationnel, défaut de centralisation. [L396, L390, L391] (mesuré)
- M3 (L2) : Précision publiée mais non attachée au chiffre diffusé (CV, intervalles dans les fiches méthodo, pas dans les IR) → le chiffre circule sans son incertitude. Preuves : F-03, F-04, F-05. Verrou : éditorial/organisationnel. [L392, L393, L394] (mesuré)

## 7. Verbatim et citations
- « 60,5 % en première interrogation et 64,3 % en réinterrogation » (DT2023-22 figure 25, reformulation F-02) (estimé). [L391] (mesuré)
- « plus significatif » n'appartient pas à ce run (Observatoire des inégalités, autre run) : ne pas citer ici.

## 8. Notes méthodologiques source
8 faits sur 9 en famille A unique : pas de ✦, limite documentée (pas de contre-recherche requise). Le lead « les taux par vague ne sont pas publiés » est réfuté (F-02) ; la reformulation correcte est un déficit d'agrégation. L'effet chiffré de l'incertitude non attachée reste GAP_TYPE=CAUSALITY (AXS-008), comblé plus tard par le run chiffrage (0,3 Md€/0,1 pt sur la dette, 5 Md€/pt sur les prestations).

## 9. Limites connues de cette extraction (case-limites)
Aucun ✦ au run (famille unique) ; tableau PDF non OCR-isés ; l'absence d'équivalent ménages du baromètre est constatée dans le corpus inspecté, non établie comme absence générale ; traces [Lxx] estimées.
