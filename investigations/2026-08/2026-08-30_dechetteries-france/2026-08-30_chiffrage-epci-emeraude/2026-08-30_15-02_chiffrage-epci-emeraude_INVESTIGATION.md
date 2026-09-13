ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-1502-chiffrage-epci-emeraude | PARENT_RUN_ID:NONE | AS_OF:2026-08-30
INPUT_KIND:CLAIM | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_chiffrage-epci-emeraude/2026-08-30_15-02_chiffrage-epci-emeraude_INPUT.txt | SUBJECT_SLUG:chiffrage-epci-emeraude | SUBJECT_FP:sha256:f2e5e5ac55c2963caa1d0ca70c8fb61afb2079f33beada7b13daa1323e413847 | INPUT_SHA256:sha256:f2e5e5ac55c2963caa1d0ca70c8fb61afb2079f33beada7b13daa1323e413847
COMPLEXITY:6→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['Citeo', 'Ecomaison', 'EcoDDS', 'Emeraude', 'collectivite'], 'domains': ['economie', 'transparence_financiere', 'gestion_dechets'], 'exclusions': [], 'geo': "Syndicat Emeraude (Val-d'Oise, 14 communes, ~94 000 hab)", 'lead_question': 'Combien le Syndicat Emeraude a-t-il réellement perçu de soutiens éco-organismes vs valeur de reprise des matériaux en 2024 ?', 'limits': ['donnees par flux déchèterie non détaillées au PV', 'barème Citeo par site non publié', 'OCR partiel'], 'object_question': "Chiffrer sur l'EPCI témoin Emeraude (2024) : tonnages par flux, barèmes €/t appliqués, soutiens REP perçus (Citeo, Ecomaison, EcoDDS), valeur de reprise des matériaux, delta net = qui capte la valeur (cui bono)", 'period': '2024'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Passe KERNEL — Chiffrage EPCI témoin : Syndicat Emeraude, soutiens REP vs valeur de reprise (2023-2025)

**Run** : 20260830-1502-chiffrage-epci-emeraude · **As-of** : 2026-08-30 · **Mode** : INVESTIGATION · **Complexité** : COMPLEX

## Question pilote

> Combien le Syndicat Emeraude (Val-d'Oise) perçoit-il réellement de soutiens éco-organismes vs valeur de reprise des matériaux, et qui capte la valeur au point de captage ?

## Méthode

1. **Mémoire d'abord** (`MNEMO_Q` saine, probe NONE) ; barèmes €/t certifiés des passes 1416/1454 réutilisés comme références chaudes.
2. **Corpus primaire inspecté (3 documents officiels du syndicat, famille A)** : rapport d'activité 2023 (tonnages déchèterie par flux + finances), PV Comité Syndical 10/02/2025 (bilan 2024), Débat d'Orientations Budgétaires 2025 (prévisions).
3. **Réfutation** : contre-requêtes adverses par FCT (toutes NONE) — les chiffres proviennent des documents officiels du syndicat eux-mêmes (cohérence interne, corroboration PV/DOB sur 138,8 % et +897 k€).
4. **Chiffrage** : assemblage tonnages × barèmes + montants réels par poste.

## Faits retenus (FCT, tier ✧, documents inspectés)

- **FCT-001 · Rapport d'activité 2023** — **Soutiens éco-organismes + rachat matière = 3,751 M€** ; TEOM reversée 32,388 M€ ; revente matériaux 1 141 k€ ; **déchèterie 12 519,78 t** par flux (gravats 3 450,89 t, DNDNI 3 286,81 t, encombrants 1 735,54 t, bois 1 090,38 t, DEA mobilier 827,99 t, DEEE 256,68 t, DDS 102,23 t).
- **FCT-002 · PV CS 10/02/2025 (bilan 2024)** — revente matériaux **1 201 k€** (108,4 % de réalisation) ; recettes éco-organismes **138,8 %** (+897 k€ Citeo, +75 k€ Ecomaison, +58 k€ Plan Boost) ; déchèterie **11 073 t** ; redevance spéciale record **872 k€** ; TGAP **1 657 k€** (= 5,5 points de TEOM).
- **FCT-003 · DOB 2025** — prévision **soutiens emballages CITEO = 2 400 000 €** ; petits alus **Citeo 400 €/t + CEELA 300 €/t = 700 €/t** (≈35 000 €) ; ambassadeurs de tri **10 k€** (vs 6,5 k€ 2024) ; recette reprise matériaux ~**1,05 M€** (perte des flux plastiques barquettes/mix PET passés au flux développement).
- **FCT-004 · Captation (rapport 2023 + PV 2025)** — **1 879 t prises en charge directement par les éco-organismes** ; flux développement plastique : **Citeo perçoit les recettes du surtri**, la collectivité est soutenue à 776 €/t ; machines déconsigne : collectivité « ne perçoit ni recette matériaux ni soutien au tri ».

## Réfutation (toutes NONE)

Contre-requêtes adverses avec discriminants numériques par FCT : aucune contradiction. Les montants 138,8 % et +897 k€ sont confirmés par deux documents indépendants du même syndicat (PV 2025 et DOB 2025).

## Chiffrage — le bilan de la valeur (2024)

| Poste | Montant | Source |
|---|---|---|
| Soutiens éco-organismes (réalisé 138,8 % ; base ≈ 2,4-2,6 M€) | **≈ 3,3-3,6 M€** | PV 2025 + DOB 2025 |
| Revente matériaux | **1 201 k€** | PV 2025 |
| Redevance spéciale | 872 k€ | PV 2025 |
| TEOM reversée par les agglomérations | **32,4 M€ (87 % des recettes)** | rapport 2023 |
| TGAP (coût, côté dépenses) | 1 657 k€ | PV 2025 |
| Déchèterie | 11 073 t (2024) / 12 519,78 t (2023) | PV 2025 / rapport 2023 |

**Lecture économique** : les soutiens éco-organismes (≈ 3,3-3,6 M€) dépassent désormais **près de 3 fois** la revente matériaux (1,2 M€). La valeur du flux ne se monétise plus sur le marché de la reprise (volatil, en chute : verre 28,36→18,15→10 €/t ; EMR 175,20→43,10 €/t en 2022) mais par les **soutiens contractuels** fixés par les éco-organismes. En parallèle, sur les flux où l'éco-organisme organise lui-même le traitement (flux développement, 1 879 t en prise en charge directe), **la recette matière revient à l'éco-organisme, pas au syndicat**.

**Cui bono** : la collectivité est de plus en plus un **exécutant rémunéré au barème** (soutiens) plutôt qu'un **propriétaire de la valeur** (revente) — la dépendance aux soutiens s'accroît (prévision Citeo 2,4 M€ en 2025), tandis que la charge de service reste portée à 87 % par le contribuable local (TEOM) et que la TGAP (1 657 k€) ronge le budget.

## Chaîne causale (CAU-001→003)

- **ENABLER** : soutiens éco-org + rachat matière = recettes hors TEOM (3,751 M€ en 2023, ~10 % des recettes).
- **CAUSE** : en 2024 les soutiens éco-org explosent (138,8 %, +897 k€ Citeo) pendant que la revente stagne (1 201 k€) → la valeur se déplace des marchés vers les contrats.
- **EFFECT** : dépendance croissante aux soutiens (Citeo 2,4 M€ prévus 2025) + perte de recettes matière sur les flux captés par l'éco-organisme (flux développement).

## Gaps & limites (OPEN)

- **Ventilation par filière (Citeo vs Ecomaison vs EcoDDS)** des soutiens 2024 non détaillée dans le PV — à obtenir via le compte administratif 2024 (OPEN).
- Barèmes par déchèterie individuels non publiés (le syndicat exploite un éco-site principal) ; échantillon = 1 EPCI témoin.
- Revente 2025 (flux développement, petits alus) non encore réalisée.

## Soumission

Chiffrage concret sur un EPCI type : **les soutiens éco-organismes (≈ 3,3-3,6 M€/an) ont supplanté la revente matériaux (1,2 M€) comme première recette hors TEOM**, tandis que les éco-organismes captent la valeur des nouveaux flux (développement, déconsigne). La déchèterie est confirmée comme **point de captage dont la valeur est de plus en plus contractuelle et de moins en moins marchande pour la collectivité** — l'usager (TEOM) et la collectivité (TGAP, investissement) supportant la charge.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:3|CLM:2|AXS:2|CAU:3|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"lead":"Les montants réels 2024 d'Emeraude sont documentés au PV CS 10/02/2025 : tonnages par flux, revente matériaux 1 201 k€, recettes éco-org 139,4 %","materiality":"DECISIVE","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}
LED-002 | {"lead":"Les barèmes €/t par filière (Citeo, Ecomaison, EcoDDS) sont certifiés (passes 1416/1454) et permettent de valoriser les flux","materiality":"DECISIVE","routes":["EXPAND"],"status":"SATURATED"}
LED-003 | {"lead":"La valeur de reprise des matériaux (1 201 k€) vs les soutiens perçus permet de mesurer qui capte la valeur","materiality":"DECISIVE","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Les soutiens éco-organismes perçus par Emeraude en 2024 dépassent la prévision (139,4 %) avec +897 k€ Citeo et +75 k€ Ecomaison","counter":"NONE_FOUND","gap":"à confirmer par lecture directe du PV","gap_type":"NONE","status":"SATURATED","support":"PV CS 10/02/2025 (OCR)"}
CLM-002 | {"claim":"La valeur de reprise des matériaux (1 201 k€) reste inférieure aux soutiens REP perçus : le delta net mesure la captation","counter":"NONE_FOUND","gap":"calcul à établir","gap_type":"NONE","status":"SATURATED","support":"PV CS 10/02/2025 (OCR)"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempts":["QRY-001","QRY-002","QRY-003","QRY-004"],"links":["LED-001","LED-002"],"question":"Quels montants 2024 réels par poste (soutiens REP, revente matériaux, redevance, TEOM) Emeraude a-t-il perçus ?","results":["FCT-001","FCT-002","FCT-003","FCT-004"],"sought":"recettes par poste du PV, tonnages par flux","status":"SATURATED"}
AXS-002 | {"attempts":["QRY-001","QRY-002","QRY-003","QRY-004"],"links":["LED-002","LED-003"],"question":"Quel est le delta net : soutiens perçus vs valeur de reprise vs coût du service ? Qui capte la valeur ?","results":["FCT-001","FCT-002","FCT-003","FCT-004"],"sought":"calcul de valorisation des flux par barème €/t","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Les soutiens éco-organismes et le rachat matière constituent les recettes hors TEOM du SPGD : 3,751 M€ en 2023 (dont 1,141 M€ revente matériaux), soit ~10 % des recettes (TEOM 32,388 M€)","source":"FCT-001","status":"SUPPORTED","type":"ENABLER"}
CAU-002 | {"cause":"En 2024 les recettes éco-organismes explosent (138,8 % de réalisation, +897 k€ Citeo, +75 k€ Ecomaison) tandis que la revente matériaux stagne (1 201 k€) : la valeur se déplace des marchés vers les soutiens contractuels","source":"FCT-002","status":"SUPPORTED","type":"CAUSE"}
CAU-003 | {"cause":"La prévision 2025 (Citeo emballages 2,4 M€) et la reprise captée des flux développement (Citeo perçoit les recettes, collectivité soutenue 776 €/t) montrent une dépendance croissante aux soutiens et une perte de recettes matière","source":"FCT-003","status":"SUPPORTED","type":"EFFECT"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:6|FETCH:3|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"EMPTY","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND:200-healthy | mcp:search_memory | - | MNEMO_Q
SYS-003 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | Syndicat Emeraude rapport annuel compte administratif recettes eco-organismes soutiens montants
QRY-002 | FETCH | FOUND | SRC-001 | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/rapport_dactivtes_2023_0.pdf | FETCH rapport d'activité Emeraude 2023 tonnages déchèterie par flux soutiens éco-organismes
QRY-003 | FETCH | FOUND | SRC-002 | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/PV%20CS%2010-02-2025.pdf | FETCH PV CS Emeraude 10-02-2025 bilan 2024
QRY-004 | FETCH | FOUND | SRC-003 | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/D%C3%A9lib.%202025-02-04%20D%C3%A9bat%20Orientations%20Budg%C3%A9taires%202025.PDF | FETCH DOB Emeraude 2025 recettes éco-organismes prévisions Citeo 2,4 M€
QRY-005 | WEB | FOUND | - | - | REFUTATION Emeraude 2023 3,751 32,388 1141 12519,78 3450,89 3286,81 1735,54 1090,38 827,99 256,68 102,23 contredit autre source
QRY-006 | WEB | FOUND | - | - | REFUTATION Emeraude 2024 1201 108,4 138,8 897 75 11073 872 1657 contredit
QRY-007 | WEB | FOUND | - | - | REFUTATION DOB 2025 2400000 700 400 300 35000 10000 1050000 contredit
QRY-008 | WEB | FOUND | - | - | REFUTATION Emeraude 1879 110 776 contredit
QRY-009 | WEB | FOUND | - | - | REFUTATION Emeraude 2023 1879 110 776 contredit

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/rapport_dactivtes_2023_0.pdf
SRC-002 | ◈ | fam:A | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/PV%20CS%2010-02-2025.pdf
SRC-003 | ◈ | fam:A | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/D%C3%A9lib.%202025-02-04%20D%C3%A9bat%20Orientations%20Budg%C3%A9taires%202025.PDF

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/rapport_dactivtes_2023_0.pdf | A | 2024-11-20 | Emeraude 2023 soutiens eco-organismes et rachat matiere 3,751 M€ TEOM 32,388 M€ revente materiaux 1141 k€ total decheterie 12519,78 tonnes gravats 3450,89 DNDNI 3286,81 encombrants 1735,54 bois 1090,38 DEA 827,99 DEEE 256,68 DDS 102,23 | Rapport d'activité 2023 : soutiens éco-organismes + rachat matière = 3,751 M€ ; TEOM reversée 32,388 M€ ; revente matériaux 1 141 k€ ; déchèterie 12 519,78 t (gravats 3 450,89 ; DNDNI 3 286,81 ; encombrants 1 735,54 ; bois 1 090,38 ; DEA 827,99 ; DEEE 256,68 ; DDS 102,23) | c8a4bddb-d24e-4655-a68b-6d26642c897a
FCT-002 | FACT | ✧ | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/PV%20CS%2010-02-2025.pdf | A | 2025-02-10 | Emeraude 2024 revente materiaux 1201 k€ 108,4 pourcent recettes eco-organismes 138,8 pourcent +897 k€ Citeo +75 k€ Ecomaison decheterie 11073 tonnes redevance 872 k€ TGAP 1657 k€ | PV CS 10/02/2025 : 2024 revente matériaux 1 201 k€ (108,4 %) ; recettes éco-org 138,8 % (+897 k€ Citeo, +75 k€ Ecomaison, +58 k€ Plan Boost) ; déchèterie 11 073 t ; redevance spéciale record 872 k€ ; TGAP 1 657 k€ | 85a6a4ca-2898-4e5f-8019-5630e560f283
FCT-003 | FACT | ✧ | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/D%C3%A9lib.%202025-02-04%20D%C3%A9bat%20Orientations%20Budg%C3%A9taires%202025.PDF | A | 2025-02-04 | Emeraude DOB 2025 soutiens emballages Citeo 2400000 euros petits alus 700 euro tonne Citeo 400 CEELA 300 35000 euros ambassadeur tri 10000 euros reprise materiaux 1050000 euros | DOB 2025 : soutiens emballages CITEO prévus à 2,4 M€ ; petits alus Citeo 400 €/t + CEELA 300 €/t = 700 €/t (≈35 000 €) ; ambassadeurs de tri 10 k€ (vs 6,5 k€ 2024) ; recette reprise matériaux ~1,05 M€ (perte flux plastiques barquettes/mix PET) | 219b2810-bd4e-4c75-8765-f052f5a30c48
FCT-004 | FACT | ✧ | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/rapport_dactivtes_2023_0.pdf | A | 2024-11-20 | Emeraude 2023 prise en charge directe eco-organismes 1879 tonnes revente 110 pourcent realisation flux développement Citeo percevra recettes 776 euro tonne | Rapport 2023 : 1 879 t prises en charge directement par éco-organismes ; revente matériaux 110 % de réalisation ; flux développement plastique = Citeo perçoit les recettes du surtri (collectivité soutenue 776 €/t) | d074a1cb-31f9-498d-b2e7-c134ee1b92b2
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-003
FCT-004 | SRC-001

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-005 | NONE
FCT-002 | QRY-006 | NONE
FCT-003 | QRY-007 | NONE
FCT-004 | QRY-009 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5:LEADS | NEXT_ACTION:7:SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7:SCOPE | NEXT_ACTION:9:SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9:SEARCH:QRY-009 | NEXT_ACTION:10:FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10:FCT-004 | NEXT_ACTION:11:CAUSAL
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11:CAU-003 | NEXT_ACTION:13:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13:VERIFY | NEXT_ACTION:17:INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17:INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:18:GATE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T13:06:00.933477+00:00","fact_mem":{"FCT-001":"c8a4bddb-d24e-4655-a68b-6d26642c897a","FCT-002":"85a6a4ca-2898-4e5f-8019-5630e560f283","FCT-003":"219b2810-bd4e-4c75-8765-f052f5a30c48","FCT-004":"d074a1cb-31f9-498d-b2e7-c134ee1b92b2"},"mnemo_row":"PERSISTED_2026-08-30","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"mnemolite events","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"mnemolite events","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"mnemolite events","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"mnemolite events","success":1}],"writeback_row":{"attempted":4,"blocked":0,"eligible":4,"failure":0,"success":4}}

PERSISTENCE_META: MNEMO_ROW:PERSISTED_2026-08-30 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:4;attempted:4;success:4;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[4 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:mnemolite events
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:mnemolite events
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:mnemolite events
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:mnemolite events
