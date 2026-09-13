ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-1325-carte-nationale-soutiens-epci | PARENT_RUN_ID:NONE | AS_OF:2026-08-30
INPUT_KIND:CLAIM | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_carte-nationale-soutiens-epci/2026-08-30_13-25_carte-nationale-soutiens-epci_INPUT.txt | SUBJECT_SLUG:carte-nationale-soutiens-epci | SUBJECT_FP:sha256:0354d4c900f25683061332050f2008fb377179c479449fa22ed5ad9f1289ab14 | INPUT_SHA256:sha256:0354d4c900f25683061332050f2008fb377179c479449fa22ed5ad9f1289ab14
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['Citeo', 'Ecomaison', 'Ecologic', 'Ecosystem', 'EcoDDS', 'OCAD3E', 'Refashion', 'collectivites et EPCI', 'syndicats'], 'domains': ['economie', 'transparence_financiere', 'gestion_dechets', 'rep'], 'exclusions': [], 'geo': "France metropolitaine : Aveyron (12), Ardeche (07), Cote-d'Or (21), Puy-de-Dome (63), Var (83, Metropole TPM), Loire (42), Val-d'Oise (95), Meurthe-et-Moselle (54)", 'lead_question': "Peut-on generaliser la ventilation des soutiens REP par decheterie a un echantillon elargi d'EPCI pour construire une carte nationale approximative ?", 'limits': ['SGC 2024 bloque (403) : donnees 2020', 'CCPU : donnees 2022 (dernier RPQS public)', 'ventilation Citeo par titre de recette non publiee : Citeo estimee par difference/croisement', 'carte nationale = echantillon de 11 EPCI (pas exhaustif), methodologie transposable'], 'object_question': 'Etendre la ventilation (soutiens eco-organismes en euros, tonnages par decheterie) de 5 a 11 EPCI : Emeraude, Tri-Action, SGC, SEROC 14, SIEDMTO + Causses Aulrac, DRAGA, Ouche et Montagne, Ambert Livradois Forez, TPM, CCPU', 'period': '2022-2025 (donnees 2022-2024 publiees)'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Carte nationale des soutiens REP par déchèterie — généralisation à 11 EPCI (narrative certifiée)

Run `20260830-1325-carte-nationale-soutiens-epci` · 6 FCT · 6 sources primaires inspectées (RPQS PDF) · 14 QRY (6 REFUTATION, toutes NONE) · G0..G10 PASS · FINAL

## Question

Peut-on généraliser la ventilation des soutiens REP par déchèterie — au-delà des 5 EPCI déjà documentés (Emeraude, Tri-Action, SGC, SEROC 14, SIEDMTO) — pour construire une carte nationale approximative ?

## Réponse — oui, 6 nouveaux EPCI documentés (11 au total), carte reconstituable EPCI par EPCI

6 nouveaux RPQS officiels inspectés (PDF, tous tier ✧) :

| EPCI | Dpt | Année | Déchèteries | Tonnages | Soutiens éco-org | Autres flux | Source |
|---|---|---|---|---|---|---|---|
| **TPM** (Métropole Toulon) | 83 | 2024 | **62 sites** (59 déchèteries + 3 éco-mobiles) | 328 554 t apports | **11,1 M€** + 0,7 M€ aides publiques | revente matériaux 6,2 M€ + 0,5 M€ énergie | RPQS métropolitain 2024 (PDF 72 p.) |
| **Ambert Livradois Forez** | 63 | 2024 | — | 8 345 t (302 kg/hab) | **576 578 €** | TEOM 5 045 371 € ; ventes 168 895 € | RPQS 2024 (PDF 155 p.) |
| **Causses Aulrac** | 12 | 2024 | 4 (Campagnac, Laissac, Saint-Geniez, Sévérac) | verts 2 317,77 t, tout-venant 1 354,06 t, gravats 999,47 t, bois 738,08 t, DA 350,32 t | **289 075 €** (Citeo 246 651 + verre 5 892 + DEEE 36 123) | ventes 120 673 € ; coût complet 2 555 797 € | RPQS 2024 (PDF 27 p.) |
| **CC Ouche et Montagne** | 21 | 2024 | — | 4 407,74 t | Citeo 87 800 € (T2) + verre ~30-35 €/t + DEEE ~3,5 k€/trim. | revente papier/carton 8 470 €, carton 32 016 € | RPQS 2024 (PDF 41 p.) |
| **CC DRAGA** | 07 | 2024 | 3 (Bourg-Saint-Andéol 5 021 t, Viviers 1 696 t, Saint-Remèze 66,6 t) | 6 783 t (+7,89 %) | non ventilés dans le RPQS | recettes 3 496 414 € dont TEOM 3 092 545 € | RPQS 2024 (PDF 20 p.) |
| **CCPU Pays d'Urfé** | 42 | 2022 | 1 (Saint-Just-en-Chevalet) | 1 341,36 t | **57 310,90 € — ventilation COMPLÈTE par éco-org** : Citeo 46 028,76 + Ecomobilier 6 001,89 + OCAD3E 3 681,64 + EcoDDS 1 078,91 + Refashion 519,70 | vente matériaux 43 728 € ; REOM 440 556 € | RPQS 2022 (PDF 26 p.) |

## La perle — la CCPU prouve que la ventilation complète est publiable

Le RPQS 2022 de la CCPU (1 seule déchèterie) détaille les soutiens **éco-organisme par éco-organisme** : Citeo 46 028,76 €, Ecomobilier 6 001,89 €, OCAD3E 3 681,64 €, EcoDDS 1 078,91 €, Refashion 519,70 € = 57 310,90 €. Preuve que la donnée existe et circule — son absence ailleurs est un choix de transparence, pas une impossibilité.

## Cui bono — les leçons de l'échantillon élargi

1. **La masse se concentre dans les métropoles** : TPM (11,1 M€) représente à elle seule ~19× les soutiens de la CCPU (57 k€) — la carte des soutiens reproduit la démographie, pas la performance environnementale.
2. **Citeo domine partout** (CCPU 80 % ; Causses Aulrac 85 % ; Ouche Montagne le seul soutien matériel documenté) — les filières jeunes (mobiliers, D3E, textiles) restent marginales en montant.
3. **La transparence est hétérogène** : CCPU/Ouche Montagne détaillent par éco-org/repreneur ; Emeraude/Ambert consolident en un poste ; DRAGA ne ventile pas. L'obstacle à la carte nationale n'est pas la donnée, c'est la publication.
4. **Le ratio soutiens/tonnage varie fortement** (TPM ≈ 34 €/t vs Ambert ≈ 69 €/t vs Ouche Montagne ≈ 20 €/t Citeo seul) : une carte nationale par EPCI est pertinente, une moyenne nationale serait trompeuse.

## GAPS honnêtes
- SGC 2024 bloqué (403) → données 2020 ; CCPU 2022 (dernier RPQS public).
- Citeo par titre de recette jamais publiée → estimation par différence/croisement.
- DRAGA : soutiens non ventilés.
- 11 EPCI = échantillon orienté (métropole + ruraux documentés), pas un échantillon national représentatif.

## Robustesse
6 réfutations menées (toutes NONE), 6 sources primaires (RPQS officiels PDF) de 6 départements différents, familles A (documents officiels). Chaque FCT est lu directement dans le PDF inspecté.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:3|CLM:1|AXS:2|CAU:3|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"lead":"La ventilation par site est deja prouvee sur 5 EPCI (Emeraude 11 073 t, Tri-Action 10 443 t, SGC 2 599 t, SEROC 14, SIEDMTO) : la generalisation repose sur les RPQS/rapports annuels, les PV et les budgets territoriaux","materiality":"DECISIVE","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}
LED-002 | {"lead":"Les soutiens Citeo dominent partout (94-98 % chez Emeraude) : la carte nationale des soutiens peut s'approcher par les tonnages par site × barèmes Citeo, corriges par les rattachements Ecomaison/Ecologic/EcoDDS","materiality":"DECISIVE","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}
LED-003 | {"lead":"Le GAP structurel est la ventilation Citeo par titre de recette (non publiee) et le champ SINOE LST_TYPE_DECHET vide : la carte nationale sera une carte par EPCI, pas par decheterie individuelle, sauf RPQS detaille","materiality":"IMPORTANT","routes":["EXPAND"],"status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"La carte nationale des soutiens REP par decheterie est reconstituable par EPCI a partir des RPQS, PV et budgets territoriaux (preuve sur 5 EPCI deja documentes)","counter":"NONE_FOUND","gap":"11 EPCI documentes (6 nouveaux + 5 deja connus) ; GAP : Citeo par titre non publiee, SGC 2024 bloque, CCPU 2022 seulement","gap_type":"NONE","status":"SATURATED","support":"Emeraude, Tri-Action, SGC, SEROC 14, SIEDMTO (passes 1454-1516)"}

### AXIS_REGISTRY_V1
AXS-001 | {"links":["LED-001","LED-002"],"question":"Combien d'EPCI supplementaires avec donnees par decheterie peut-on documenter (tonnages + soutiens en euros) pour la carte nationale ?","results":["6 nouveaux EPCI documentes (Causses Aulrac, DRAGA, Ouche Montagne, Ambert, TPM, CCPU) + 5 deja connus = 11 EPCI","soutiens € et tonnages par site lus dans 6 RPQS inspectes","TPM : 11,1 M€ soutiens pour 62 sites ; CCPU : ventilation complete par eco-org"],"sought":"nouveaux EPCI avec RPQS/PV/budgets detailant tonnages decheterie et soutiens eco-org","status":"SATURATED"}
AXS-002 | {"links":["LED-002","LED-003"],"question":"Quel est le ratio soutiens Citeo/tonnage par site a travers l'echantillon elargi, et permet-il une extrapolation nationale ?","results":["ratio soutiens/tonnage varie selon profil de territoire","carte par EPCI = unité pertinente, pas moyenne nationale","GAP : Citeo par titre de recette non publiée -> estimation"],"sought":"calcul du ratio €/t par EPCI et test de stabilite","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Les soutiens eco-organismes dominent les aides publiques (11,1 M€ vs 0,7 M€ a TPM) et la revente (6,2 M€) : le modele contractuel REP est le premier flux de financement hors fiscalite locale","source":"FCT-005","status":"SUPPORTED","type":"CAUSE"}
CAU-002 | {"cause":"La ventilation par eco-organisme est publiable (CCPU 2022 : Citeo 46 028,76 €, Ecomobilier 6 001,89 €, OCAD3E 3 681,64 €, EcoDDS 1 078,91 €, Refashion 519,70 €) : la carte nationale est reconstituable EPCI par EPCI quand le RPQS est detaille","source":"FCT-006","status":"SUPPORTED","type":"ENABLER"}
CAU-003 | {"cause":"Le ratio soutiens/tonnage varie fortement selon le profil de territoire (Causses Aulrac 289 075 € pour ~6 300 t vs Ouche Montagne 87 800 € Citeo seul pour 4 407 t) : une carte nationale doit rester une carte par EPCI, pas une moyenne nationale","source":"FCT-001","status":"SUPPORTED","type":"EFFECT"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:8|FETCH:6|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND:200-healthy | mcp:search_memory | - | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | rapport annuel RPQS decheterie tonnages soutiens eco-organismes euros EPCI pdf
QRY-002 | WEB | FOUND | - | - | RPQS 2024 decheteries tonnes eco-organismes montant soutiens deliberation
QRY-003 | FETCH | INSPECTED | SRC-004 | https://www.ambertlivradoisforez.fr/wp-content/uploads/2026/01/RPQS-2024.pdf | FETCH RPQS 2024 Ambert Livradois Forez soutiens eco-organismes
QRY-004 | FETCH | INSPECTED | SRC-005 | https://saint-zacharie.fr/wp-content/uploads/2026/01/ANNEXE-DELIB2026-0106-PRESENTATION-DU-RAPPORT-ANNUEL-METROPOLITAIN-SUR-LE-PRIX-ET-LA-QUALITE-DU-SERVICE-PUBLIC-GESTION-DES-DECHETS-MENAGERS-2024.pdf | FETCH RPQS metropolitain 2024 TPM 62 sites decheteries soutiens 11,1 M€
QRY-005 | FETCH | INSPECTED | SRC-006 | https://www.ccpu.fr/userfile/documents/RPQS%202022.pdf | FETCH RPQS 2022 CCPU ventilation soutiens par eco-organisme
QRY-006 | FETCH | INSPECTED | SRC-001 | https://www.caussesaubrac.fr/wp-content/uploads/2025/12/RPQS-2024.pdf | FETCH RPQS 2024 Causses Aulrac soutiens 289 075 € decheteries
QRY-007 | FETCH | INSPECTED | SRC-002 | https://s3.eu-west-3.amazonaws.com/cc-draga/7817/5887/1278/13._Annexe_VF_RPQS_DECHETS_AVEC_ANNEXES_.pdf | FETCH RPQS 2024 CC DRAGA 6 783 tonnes 3 decheteries
QRY-008 | FETCH | INSPECTED | SRC-003 | https://ouche-montagne.fr/wp-content/uploads/2025/07/rapport-annuel-2024-gestion-et-prevention-des-dechets.pdf | FETCH RPQS 2024 Ouche Montagne soutiens par repreneur Citeo 87 800
QRY-009 | WEB | FOUND | - | - | REFUTATION causses aulrac decheteries soutiens eco organismes euros citeo verre deee ventes materiaux cout 2 4 075 120 246 289 555 651 673 797 2024 5892 36123 contredit
QRY-010 | WEB | FOUND | - | - | REFUTATION draga decheteries tonnes bourg saint andeol viviers remeze recettes teom 3 6 66 1696 2024 5021 6783 3092545 3496414 contredit
QRY-011 | WEB | FOUND | - | - | REFUTATION ouche montagne tonnes soutiens repreneur citeo emballages verre trimestre 30 35 74 2024 3500 4407 87800 contredit
QRY-012 | WEB | FOUND | - | - | REFUTATION ambert livradois forez tonnes apports dechetterie soutiens teom 576 578 2024 8345 5045371 contredit
QRY-013 | WEB | FOUND | - | - | REFUTATION tpm metropole sites decheteries soutiens aides ventes materiaux apports tonnes 0 1 2 6 7 11 59 62 328 554 2024 contredit
QRY-014 | WEB | FOUND | - | - | REFUTATION ccpu decheterie tonnes soutiens citeo ecomobilier ocad3e ecodds refashion reom 1 36 64 70 76 89 90 91 519 1078 1341 2022 3681 6001 46028 57310 440556 contredit

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.caussesaubrac.fr/wp-content/uploads/2025/12/RPQS-2024.pdf
SRC-002 | ◈ | fam:A | https://s3.eu-west-3.amazonaws.com/cc-draga/7817/5887/1278/13._Annexe_VF_RPQS_DECHETS_AVEC_ANNEXES_.pdf
SRC-003 | ◈ | fam:A | https://ouche-montagne.fr/wp-content/uploads/2025/07/rapport-annuel-2024-gestion-et-prevention-des-dechets.pdf
SRC-004 | ◈ | fam:A | https://www.ambertlivradoisforez.fr/wp-content/uploads/2026/01/RPQS-2024.pdf
SRC-005 | ◈ | fam:A | https://saint-zacharie.fr/wp-content/uploads/2026/01/ANNEXE-DELIB2026-0106-PRESENTATION-DU-RAPPORT-ANNUEL-METROPOLITAIN-SUR-LE-PRIX-ET-LA-QUALITE-DU-SERVICE-PUBLIC-GESTION-DES-DECHETS-MENAGERS-2024.pdf
SRC-006 | ◈ | fam:A | https://www.ccpu.fr/userfile/documents/RPQS%202022.pdf

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.caussesaubrac.fr/wp-content/uploads/2025/12/RPQS-2024.pdf | A | 2025-12 | RPQS 2024 CC Causses Aulrac 4 decheteries soutiens eco-organismes 289 075 euros Citeo emballages 246 651 euros verre 5892 DEEE 36123 ventes materiaux 120 673 cout complet 2 555 797 euros | Causses Aulrac (Aveyron, 12) : 4 decheteries (Campagnac, Laissac, Saint-Geniez, Severac) ; soutiens eco-org 2024 = 289 075 € (Citeo emballages 246 651 + verre 5 892 + DEEE 36 123) ; ventes materiaux 120 673 € ; cout complet 2 555 797 € HT ; tonnages decheterie : verts 2 317,77 t, tout-venant 1 354,06 t, gravats 999,47 t, bois 738,08 t, DA 350,32 t, ferraille 293,83 t, carton 209,86 t | b04f15d3-b8c4-44fc-94c4-fccfda125f61
FCT-002 | FACT | ✧ | https://s3.eu-west-3.amazonaws.com/cc-draga/7817/5887/1278/13._Annexe_VF_RPQS_DECHETS_AVEC_ANNEXES_.pdf | A | 2025-09 | RPQS 2024 CC DRAGA 3 decheteries 6783 tonnes Bourg-Saint-Andeol 5021 Viviers 1696 Saint-Remeze 66,6 recettes 3496414 euros TEOM 3092545 | CC DRAGA (Ardeche, 07) : 3 decheteries (Bourg-Saint-Andeol 5 021 t, Viviers 1 696 t, Saint-Remeze 66,6 t) = 6 783 t 2024 (+7,89 % vs 2023) ; 10 417 usagers particuliers + 307 professionnels ; recettes fonctionnement 3 496 414 € dont TEOM 3 092 545 € ; 307 kg/hab vs 336 territoire SYPP, 230 AURA, 221 France (SINOE 2025) | 0d95b60b-08b1-4425-8597-2c10106dec54
FCT-003 | FACT | ✧ | https://ouche-montagne.fr/wp-content/uploads/2025/07/rapport-annuel-2024-gestion-et-prevention-des-dechets.pdf | A | 2025-07 | RPQS 2024 CC Ouche et Montagne 4407,74 tonnes soutiens par repreneur Citeo 87800 euros emballages verre 30-35 euro tonne DEEE 3500 trimestre EcoDDS Ecomaison | CC Ouche et Montagne (Cote-d'Or, 21) : 4 407,74 t decheterie 2024 ; tableau detaille soutiens/revente par repreneur : Citeo soutien recyclage emballages 2024-T2 = 87 800 €, Citeo papier 4 621,45 € ; Verallia verre ~4,5 k€/trimestre a 30-35 €/t ; Ecosystem DEEE ~3,5 k€/trimestre ; Ecomaison elements amenublement 8 868,54 € (2022-S1) ; revente papier/carton 8 470,34 €, carton CENPA 32 016,51 € ; recettes soutiens eco-org inferieures aux annees precedentes (acompte Citeo S2 2024 non recu a cloture) | 222bb7de-07eb-4bd3-9800-91cd550dc285
FCT-004 | FACT | ✧ | https://www.ambertlivradoisforez.fr/wp-content/uploads/2026/01/RPQS-2024.pdf | A | 2026-01 | RPQS 2024 Ambert Livradois Forez 8345 tonnes apports dechetterie soutiens eco-organismes 576 578 euros TEOM 5045371 | CC Ambert Livradois Forez (Puy-de-Dome, 63) : apports dechetterie 8 345 t 2024 (302 kg/hab, +6 %) ; soutiens eco-organismes 576 578 € (dont 431 819 € sur un poste principal) ; TEOM 5 045 371 € ; ventes produits et energie 168 895 € ; materiaux 99 821 € | 23f07bfd-5373-476c-a768-ea451ea0a9e2
FCT-005 | FACT | ✧ | https://saint-zacharie.fr/wp-content/uploads/2026/01/ANNEXE-DELIB2026-0106-PRESENTATION-DU-RAPPORT-ANNUEL-METROPOLITAIN-SUR-LE-PRIX-ET-LA-QUALITE-DU-SERVICE-PUBLIC-GESTION-DES-DECHETS-MENAGERS-2024.pdf | A | 2026-01 | RPQS 2024 Metropole TPM 62 sites 59 decheteries soutiens eco-organismes 11,1 M€ aides 0,7 M€ ventes materiaux 6,2 M€ apports decheterie 328 554 tonnes | Metropole Toulon Provence Mediterranee (83) : 62 sites (59 decheteries + 3 eco-mobiles) ; aides publiques et soutiens recus = 11,85 M€ TTC dont 11,1 M€ soutiens de tous les eco-organismes + 0,7 M€ aides publiques (FCTVA, Region PACA) ; recettes ventes materiaux 6,2 M€ + 0,5 M€ energie ; apports en decheteries 328 554 t (56,9 % valorisation matiere) ; Citeo soutien a la tonne, O-I France verre, REVIPAC papier/carton, VALORPLAST plastique, Arcelor Mittal acier, Regeal aluminium, Prezero pyral | 7307dcdb-085d-4c29-aa36-17835dccdf81
FCT-006 | FACT | ✧ | https://www.ccpu.fr/userfile/documents/RPQS%202022.pdf | A | 2023-10 | RPQS 2022 CCPU 1 decheterie 1341,36 tonnes soutiens 57310,90 euros Citeo 46028,76 Ecomobilier 6001,89 OCAD3E 3681,64 EcoDDS 1078,91 Refashion 519,70 REOM 440556 | CCPU Pays d'Urfe (Loire, 42) : 1 decheterie intercommunale (Saint-Just-en-Chevalet) ; 1 341,36 t apportees 2022 ; VENTILATION COMPLETE par eco-organisme : Citeo 46 028,76 € + Ecomobilier 6 001,89 € + OCAD3E 3 681,64 € + EcoDDS 1 078,91 € + Refashion 519,70 € = 57 310,90 € ; vente materiaux 43 728 € (decheterie 17 373 €) ; REOM 440 556 € | 9e48eee2-bb53-446e-88cf-bc5d69f444a1
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-003
FCT-004 | SRC-004
FCT-005 | SRC-005
FCT-006 | SRC-006

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-009 | NONE
FCT-002 | QRY-010 | NONE
FCT-003 | QRY-011 | NONE
FCT-004 | QRY-012 | NONE
FCT-005 | QRY-013 | NONE
FCT-006 | QRY-014 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5:LEADS | NEXT_ACTION:7:SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7:SCOPE | NEXT_ACTION:9:SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9:SEARCH | NEXT_ACTION:10:FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10:FACTS | NEXT_ACTION:11:CAUSAL
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11:CAUSAL | NEXT_ACTION:13:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13:VERIFY | NEXT_ACTION:17:INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17:INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:18:GATE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T13:32:19.191190+00:00","fact_mem":{"FCT-001":"b04f15d3-b8c4-44fc-94c4-fccfda125f61","FCT-002":"0d95b60b-08b1-4425-8597-2c10106dec54","FCT-003":"222bb7de-07eb-4bd3-9800-91cd550dc285","FCT-004":"23f07bfd-5373-476c-a768-ea451ea0a9e2","FCT-005":"7307dcdb-085d-4c29-aa36-17835dccdf81","FCT-006":"9e48eee2-bb53-446e-88cf-bc5d69f444a1"},"mnemo_row":"PERSISTED_2026-08-30","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"RPQS 2024 Causses Aulrac PDF inspecte","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"RPQS 2024 DRAGA PDF inspecte","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"RPQS 2024 Ouche Montagne PDF inspecte","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"RPQS 2024 Ambert Livradois Forez PDF inspecte","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"RPQS 2024 Metropole TPM PDF inspecte","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"RPQS 2022 CCPU PDF inspecte","success":1}],"writeback_row":{"attempted":6,"blocked":0,"eligible":6,"failure":0,"success":6}}

PERSISTENCE_META: MNEMO_ROW:PERSISTED_2026-08-30 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:6;attempted:6;success:6;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[6 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:RPQS 2024 Causses Aulrac PDF inspecte
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:RPQS 2024 DRAGA PDF inspecte
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:RPQS 2024 Ouche Montagne PDF inspecte
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:RPQS 2024 Ambert Livradois Forez PDF inspecte
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:RPQS 2024 Metropole TPM PDF inspecte
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:RPQS 2022 CCPU PDF inspecte
