# QUINTESSENCE : indexation-conventions-gains-milliards
Source : investigations/2026-09/2026-09-20_campagne-insee-indexation/2026-09-20_indexation-conventions-gains-milliards/2026-09-20_21-10_indexation-conventions-gains-milliards_INVESTIGATION.md (RUN_ID 20260920-2110, ENGINE 2.10.6, INPUT_KIND UPDATE, COMPLEXITY 0.85 COMPLEX, G0-G10 PASS, certification DELIVERY PASS par UPDATE 20260921-1000)

## 1. Métadonnées & trace source
UPDATE de la lignée INSEE : chiffrage en milliards d'euros des gains annuels des conventions d'indexation françaises (SMIC, IRL, retraites, barème IR) ; gagnants et perdants par convention. 6 faits, 12 requêtes, 7 checkpoints. Première borne consolidée du coût/gain des conventions.

## 2. Faits atomiques préservés
- F-01 ✧ Mécanique SMIC : indexation sur l'IPC des 20 % des ménages les plus modestes + moitié du gain de pouvoir d'achat du salaire horaire moyen des ouvriers-employés ; hausse automatique en cours d'année si IPC +2 % (montants 2026 : 12,31 EUR/h brut). EPI:FACT mem:10487ed8-2257-4081-b372-450b218bdb1f [L169] (mesuré)
- F-02 ✧ Mécanique IRL : moyenne 12 mois de l'IPC hors tabac ET hors loyers (loi 89-462 art 17-1) ; le loyer des 7 millions de ménages locataires du privé suit les prix HORS leurs loyers. EPI:FACT mem:d3f212f5-4b6e-4859-a07e-f938d4d1c47d [L170] (mesuré)
- F-03 ✦ Retraites indexées sur les PRIX depuis 1987 (privé, L161-25 CSS : IPC hors tabac) et 2003 (public), sur pensions en cours ET salaires portés aux comptes ; sous Destinie, la législation pré-1993 (indexation salaires) donnerait 19,5 % de dépenses en plus à horizon (Insee DT 2025-08, Insee Analyses 109, COR). EPI:FACT mem:6a7cc60c-25c1-4998-8d63-4f83c35fd6c6 [L171] (mesuré)
- F-04 ✦ Barème IR indexé sur l'inflation ESTIMÉE de septembre n-1 sans régularisation : 8 années sur 13 en défaveur du contribuable, cumul -4,1 points de revalorisations manquées (2010-2022) ; trop-payé estimé 6 Md€ (2019-2023), 2,8-3,4 Md€ en incluant 2024 ; gel 2026 = +2 Md€ pour l'État et +200 000 foyers imposables. EPI:FACT mem:2f491e10-b0a4-4879-9cd5-9ed41a36776e [L172] (mesuré)
- F-05 ✧ Masses indexées : pensions ~390-407 Md€/an (Cour des comptes 02/2025 : dépenses 2023 = 388,4 Md€ ; COR 2024 : ~407) ; 17 millions de retraités ; 0,5 pt sur 400 Md€ = 2 Md€/an ; barème IR : chaque 0,1 pt de non-revalorisation ≈ 0,5 Md€. EPI:FACT mem:951a9a80-9ae0-44ef-9d9b-631a9f0357a9 [L173] (mesuré)
- F-06 ✧ Synthèse du chiffrage : SMIC → salariés au minimum (protégés) ; IRL → bailleurs contre locataires (loyers exclus de leur propre indexation) ; retraites → cotisants/État vs retraités (bascule 1987/2003 ≈ 4 Md€/an, 107 Md€ de niveau) ; barème IR → État via l'estimation de septembre (trop-payé 2,8-6 Md€). Aucune de ces conventions n'est cachée. EPI:FACT mem:f1ced8b7-6839-4a7f-8686-7f6c0996e404 [L174] (mesuré)Traces registre : premier fait à la ligne 169, dernier à la ligne 174 de la source [L169-L174] (mesuré).
Inventaire source : FCT-001→F-01 … FCT-006→F-06 (mesuré).

## 3. Acteurs nominaux
Insee ; COR ; Cour des comptes ; CNAV ; DGFiP ; ANIL ; Service-Public.gouv.fr ; IFRAP ; meilleurtaux.com ; législateur (loi 89-462, L161-25 CSS, CGI art 1649 A).

## 4. Sources externes citées
Fiche SMIC F2300 ; ANIL (IRL) ; Insee Analyses 109 et DT 2025-08 (PDF local) ; document COR doc07 (PDF local) ; circulaire CNAV (PDF local) ; rapport Cour des comptes 20-02-2025 ; IFRAP (barème IR) ; meilleurtaux (gel 2026) ; Code de la sécurité sociale (L161-25) ; loi 89-462 art 17-1.

## 5. Chronologie datée
1987 : indexation des retraites privées sur les prix. 2003 : extension à la fonction publique. 2010-2022 : cumul -4,1 pt de revalorisations manquées du barème IR. 2019-2023 : trop-payé barème ~6 Md€. 2022 : plafond IRL 3,5 %. 2024 : trop-payé réestimé 2,8-3,4 Md€. 2026 : gel du barème (+2 Md€, +200 000 foyers) ; SMIC 12,31 EUR/h.

## 6. Mécanismes / chaînes causales
- M1 (L2) : Choix de l'indice de référence (prix vs salaires) → transfert massif de long terme entre actifs/cotisants et retraités (~3,7 pts de PIB à horizon). Preuves : F-03, F-05. Verrou : législatif, 1987/2003. [L171, L173] (mesuré)
- M2 (L2) : Choix du calendrier d'estimation (septembre n-1 sans régularisation) → transfert annuel de l'ordre du milliard entre contribuables et État, direction variable mais biaisée documentée. Preuves : F-04. Verrou : législatif/fiscal. [L172] (mesuré)
- M3 (L2) : Choix du champ de l'indice (hors loyers pour l'IRL) → la composante la plus lourde du budget logement est exclue de sa propre indexation. Preuves : F-02. Verrou : législatif. [L170] (mesuré)
- M4 (L2) : Choix de la population de référence (20 % les plus modestes pour le SMIC) → protection ciblée. Preuves : F-01, F-06. Verrou : législatif, droit du travail. [L169, L174] (mesuré)

## 7. Verbatim et citations
- « indexées sur les prix (L161-25 CSS : IPC hors tabac) » (Code de la sécurité sociale, reformulation F-03) (estimé). [L171] (mesuré)
- « Aucune de ces conventions n'est cachée » (formulation du run F-06) (mesuré au sens source). [L174] (mesuré)

## 8. Notes méthodologiques source
Les masses consolidées par convention ne font l'objet d'aucune publication unique : le chiffrage est une arithmétique bornée à partir de masses publiées (pensions, loyers, recettes IR) et d'écarts d'indices documentés. Les PDF COR/DREES/CNAV inspectés localement portent la famille A ; l'estimation barème IR repose sur thinktank (famille other:thinktank) corrodée par service-public/legifrance.

## 9. Limites connues de cette extraction (case-limites)
Chiffrage en bornes, pas en mesure exacte ; l'élasticité comportementale (travail, épargne) est hors périmètre ; le transfert IRL locataires-bailleurs est clos séparément (cui-bono) ; traces [Lxx] estimées.
