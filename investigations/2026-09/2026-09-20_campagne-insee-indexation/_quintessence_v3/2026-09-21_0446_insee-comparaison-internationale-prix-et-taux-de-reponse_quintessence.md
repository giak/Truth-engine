# QUINTESSENCE : insee-comparaison-internationale-prix-et-taux-de-reponse
Source : investigations/2026-09/2026-09-20_campagne-insee-indexation/2026-09-21_insee-comparaison-internationale-prix-et-taux-de-reponse/2026-09-21_04-46_insee-comparaison-internationale-prix-et-taux-de-reponse_INVESTIGATION.md (RUN_ID 20260921-0446, ENGINE 2.10.6, INPUT_KIND UPDATE, COMPLEXITY 8 APEX, G0-G10 PASS, DELIVERY PASS)

## 1. Métadonnées & trace source
UPDATE du run 17-04 : la France est-elle spécifique ou normale sur la mesure des prix et les taux de réponse ? Comparaison Allemagne, Royaume-Uni, cadre européen, 2016-2026. 9 faits, 15 requêtes, 8 checkpoints. Résultat : mise en perspective documentée, pas une défense ; deux des trois griefs implicites ne résistent pas à la comparaison.

## 2. Faits atomiques préservés
- F-01 ✦ Revue par les pairs Eurostat de la France : premier rapport publié de la troisième vague du SSEN ; visite du 28 juin au 2 juillet 2021, quatre experts de haut niveau ; diagnostic et recommandations alimentant le plan d'action français. EPI:FACT mem:6cfef727-ffbe-4494-9a88-918bef03b946 [L274] (mesuré)
- F-02 ✧ Plan d'action France (mars 2022) : 16 recommandations des pairs restituées ; AUCUNE ne porte sur le champ de l'IPC ni sur l'exclusion du logement des propriétaires occupants. EPI:FACT mem:6fec54c0-262f-4c98-af26-973518124762 [L275] (mesuré)
- F-03 ✧ La revue par les pairs constate que l'Insee produit des rapports de qualité pour Eurostat mais ne les rend pas toujours publics. EPI:FACT mem:74241c2e-9b18-4e2f-b167-ffd2ec246ade [L276] (mesuré)
- F-04 ✧ Chantier HICP/logement des propriétaires occupants daté : 2018 évaluation d'inaptitude (Commission), 2021 recommandation BCE (approche des acquisitions nettes), 2023 rapport Eurostat, 2025 réitération et plan européen du logement abordable. EPI:FACT mem:9d882928-007b-4584-8c62-2e2a62e96911 [L277] (mesuré)
- F-05 ✧ L'indice des prix du logement des propriétaires occupants est encadré par les règlements (UE) 2016/792, 2023/1470 et 2025/1182 (rebasing 2025). EPI:FACT mem:4f943e35-f195-4cdc-b66a-5f5599498ec4 [L278] (mesuré)
- F-06 ✧ Taux de réponse de l'enquête forces de travail britannique T4 2024 : 19,6 % hors imputés (24,0 % imputation comprise) ; par vague : 33,9 % (vague 1) à 12,7 % (vague 5) ; Inner London 17,0 %. EPI:FACT mem:f53e0424-49f7-4b37-ac65-dfd4889acbcf [L279] (mesuré)
- F-07 ✧ Le Royaume-Uni a suspendu ses publications fondées sur l'enquête forces de travail et retiré la labellisation depuis 2024 (doutes substantiels sur la qualité 2023). EPI:FACT mem:68f99a57-6b4c-4ffc-a858-83165f1f4ffe [L280] (mesuré)
- F-08 ✧ Non-réponse du micro-recensement allemand : ~35 % en 2020 (résultats définitifs), soit ~65 % de réponse. EPI:FACT mem:101c442f-c6f3-4a80-a265-e96e8a71862c [L281] (mesuré)
- F-09 ✧ Taux de collecte de l'enquête Emploi française par rang : 60,5 % (1re interrogation) et 64,3 % (réinterrogation) au T2 2023 ; réponse ~77 % en 2021. EPI:FACT mem:0e24e6e4-f36c-4701-99ac-462958f1b7f7 [L282] (mesuré)Traces registre : premier fait à la ligne 274, dernier à la ligne 282 de la source [L274-L282] (mesuré).
Inventaire source : FCT-001→F-01 … FCT-009→F-09 (mesuré).

## 3. Acteurs nominaux
Eurostat ; Commission européenne ; BCE ; Insee ; ONS ; Destatis ; équipe de revue par les pairs.

## 4. Sources externes citées
Eurostat news (revue par les pairs 2021) ; plan d'action France (PDF, mars 2022) ; statistics-explained (logement) ; ONS (LFS qualité, publications suspendues) ; Destatis (micro-recensement 2020) ; DT Insee 2023-22.

## 5. Chronologie datée
2005 : Code de bonnes pratiques européen. 2018 : évaluation d'inaptitude OOHPI. 2021 : revue par les pairs France (visite juin-juillet, rapport publié) ; recommandation BCE. Mars 2022 : plan d'action France (16 recommandations). 2023 : rapport Eurostat OOHPI ; règlement 2023/1470. 2024 : suspension britannique. 2025 : réitération, plan logement abordable ; règlement 2025/1182.

## 6. Mécanismes / chaînes causales
- M1 (L2) : Le champ de l'IPCH est fixé au niveau de l'Union (règlements) : l'exclusion des loyers imputés n'est pas une dérogation française ; le chantier d'inclusion est européen, lent, daté, et l'exclusion actuelle n'a jamais été relevée par les pairs français (0/16). Preuves : F-04, F-05, F-01, F-02. Verrou : supranational. [L277, L278, L274, L275] (mesuré)
- M2 (L2) : Le déclin de réponse ménages est européen : le Royaume-Uni (19,6 %, publications suspendues) et l'Allemagne (~65 %) sont sous la France (60,5-77 %) ; la comparaison invalide la lecture « défaillance française ». Preuves : F-06, F-07, F-08, F-09. Verrou : conjoncturel et européen. [L279, L280, L281, L282] (mesuré)
- M3 (L2) : Point faible réel relevé par le contrôle : centralisation de la documentation de qualité (produite pour Eurostat, pas toujours publique) → convergence avec le déficit d'agrégation documenté au run 02-55. Preuves : F-03. Verrou : organisationnel. [L276] (mesuré)

## 7. Verbatim et citations
- « des doutes substantiels sur la qualité des données collectées en 2023 » (ONS, reformulation F-07) (estimé). [L280] (mesuré)
- « ne sont pas toujours publiés sur les sites de l'Insee ou des services statistiques ministériels » (revue par les pairs, reformulation F-03) (estimé). [L276] (mesuré)

## 8. Notes méthodologiques source
Comparaison à deux partenaires et trois points chiffrés : aucune généralisation au-delà. Aucune contestation de la revue par les pairs française trouvée (fait négatif). Le run ne juge pas la qualité relative des trois systèmes : il borne la spécificité française.

## 9. Limites connues de cette extraction (case-limites)
Deux partenaires seulement ; aucun classement général de la qualité statistique européenne ; coût des interventions de qualité non documenté ; les reprises médiatiques de la comparaison sont hors périmètre ; traces [Lxx] estimées.
