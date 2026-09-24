# QUINTESSENCE : insee-avis-conformite-cnis-eec-gap-access
Source : investigations/2026-09/2026-09-20_campagne-insee-indexation/2026-09-21_insee-avis-conformite-cnis-eec-gap-access/2026-09-21_03-14_insee-avis-conformite-cnis-eec-gap-access_INVESTIGATION.md (RUN_ID 20260921-0314, ENGINE 2.10.6, INPUT_KIND UPDATE, COMPLEXITY 5 MEDIUM, G0-G10 PASS, DELIVERY PASS)

## 1. Métadonnées & trace source
UPDATE du run 02-55 : fermeture du gap ACCESS du CTRL-001, obtention et inspection de l'avis de conformité du Comité du label sur l'enquête Emploi (parent : HTTP 403). 9 faits, 7 requêtes, 7 checkpoints. Cause nommée : filtrage par user-agent, pas un mur d'accès.

## 2. Faits atomiques préservés
- F-01 ✧ Avis de conformité n° 2026_13068_DG75-L002 du 30 juin 2026 (réunion du 21 mai 2026) : label d'intérêt général et de qualité statistique Oui, caractère obligatoire Oui (proposition d'octroi), validité 2027-2030, publication au JO Oui, périodicité annuelle. EPI:FACT mem:1d7faea7-729e-4b35-8e45-95676d932501 [L365] (mesuré)
- F-02 ✧ Le Comité retient les taux de réponse parmi les indicateurs des analyses comparatives entre le test 2027 et l'enquête en production (avec nombre d'individus renseignés par logement et écarts sur questions majeures) ; décision avant fin 2027 sur une éventuelle enquête pilote. EPI:FACT mem:41d4fa27-9bef-42a6-8507-20f0563f1ff9 [L366] (mesuré)
- F-03 ✧ Le Comité demande que le prochain dossier précise l'impact de l'évolution de la qualité de la base de sondage sur le repérage des logements et la prise de contact. EPI:FACT mem:e4291886-6fdd-4367-b7e9-9c49242abe89 [L367] (mesuré)
- F-04 ✧ Le Comité salue l'investissement du service en faveur du maintien et de l'amélioration des taux de réponse. EPI:FACT mem:276fbc35-4f21-4ba0-8392-2263e816ebd6 [L368] (mesuré)
- F-05 ✧ Le Comité note la progression des réponses par internet en réinterrogation. EPI:FACT mem:abb11b0d-8d37-4d62-b483-e64ad0b587b4 [L369] (mesuré)
- F-06 ✧ Avis rectificatif du 01/10/2025 (conformité du 03-10-2025, n 2025_20777) prolongeant l'enquête Emploi pour 2026 ; avis initial du 8 octobre 2020 pour 2021-2025. EPI:FACT mem:3a7360b4-f440-4d6f-a292-2d7f1c4ba32f [L370] (mesuré)
- F-07 ✧ Avis de conformité EAR (n 2026_7588_DG75-L002, 01-04-2026) : validité 2027-2031, label Oui, obligatoire Oui, publication JO Oui. EPI:FACT mem:a08bdacf-ec10-4cc6-b065-3f753bb4ba32 [L371] (mesuré)
- F-08 ✧ Comité des utilisateurs annuel depuis 2021, appel à participation large (chercheurs Quetelet-Progedo, CASD). EPI:FACT mem:f3090852-7865-4b4c-aa3f-bae51cef2d19 [L372] (mesuré)
- F-09 ✦ Les taux de réponse font l'objet d'un suivi explicite comme indicateur de qualité, attesté de deux côtés indépendants : producteur (60,5 % / 64,3 %, DT2023-22 fig 25) et contrôle externe (indicateurs de comparabilité du test 2027). EPI:FACT mem:f477bb12-5df8-4077-bc2f-6f729d52f289 [L373] (mesuré)Traces registre : premier fait à la ligne 365, dernier à la ligne 373 de la source [L365-L373] (mesuré).
Inventaire source : FCT-001→F-01 … FCT-009→F-09 (mesuré).

## 3. Acteurs nominaux
Comité du label de la statistique publique (Cnis) ; Insee ; commission « Emploi, qualification et revenus du travail » ; Quetelet-Progedo ; CASD ; chercheurs utilisateurs.

## 4. Sources externes citées
Avis de conformité CNIS 2026 (PDF, 144 606 octets, sha256 vérifié) ; avis 2020 et rectificatif 2025 ; avis EAR 2026 ; DT2023-22.

## 5. Chronologie datée
8-10-2020 : avis initial EEC (2021-2025). 01/03-10-2025 : rectificatif (prolongation 2026). 11-02-2026 : réunion Comité (EAR). 01-04-2026 : avis EAR (2027-2031). 21-05-2026 : réunion Comité (EEC). 30-06-2026 : avis de conformité EEC (2027-2030).

## 6. Mécanismes / chaînes causales
- M1 (L2) : Contrôle externe sur pièces → avis public au JO avec exigences → le suivi de qualité (taux de réponse) est attesté par un organe indépendant, pas seulement déclaré par le producteur. Preuves : F-01, F-02, F-09. Verrou : institutionnel. [L365, L366, L373] (mesuré)
- M2 (L2) : Le contrôle introduit ses propres exigences (base de sondage → prise de contact) → déplace la charge vers l'amont de la chaîne de collecte. Preuves : F-03. Verrou : méthodologique. [L367] (mesuré)

## 7. Verbatim et citations
- « les analyses comparatives entre les résultats du test et l'enquête reposeront sur un ensemble d'indicateurs, incluant notamment les taux de réponse » (avis CNIS 2026, reformulation F-02) (estimé). [L366] (mesuré)
- « le contrôle porte sur la qualité » (limites du run : le contrôle atteste le dispositif, il ne mesure pas l'effet sur les valeurs publiées) (estimé).

## 8. Notes méthodologiques source
Le gap ACCESS est clos par acquisition avec en-tête navigateur (fait du run, pas une recommandation de contournement). F-09 ✦ scellé sur deux familles (A + D). Réfutation exécutée : aucune source contestant le suivi des taux (NONE). OWNERSHIP_CONCENTRATION (3 sources sur 4 du même émetteur) signalée.

## 9. Limites connues de cette extraction (case-limites)
Avis de 6 pages : les observations non retenues par le Comité n'y figurent pas nécessairement ; textes légaux (loi 1951, règlement 2019/1700) non inspectés à ce run ; l'effet mesuré du contrôle sur les taux reste non établi (CAU-003, clos par le run suivant en « non identifiable ») ; traces [Lxx] estimées.
