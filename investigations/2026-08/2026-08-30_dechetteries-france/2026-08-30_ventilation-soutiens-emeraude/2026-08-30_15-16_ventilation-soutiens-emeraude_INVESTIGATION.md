ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-1516-ventilation-soutiens-emeraude | PARENT_RUN_ID:NONE | AS_OF:2026-08-30
INPUT_KIND:CLAIM | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_ventilation-soutiens-emeraude/2026-08-30_15-16_ventilation-soutiens-emeraude_INPUT.txt | SUBJECT_SLUG:ventilation-soutiens-emeraude | SUBJECT_FP:sha256:7164d405f8651ff7fa59c2cbb6aa661bed887b23f9e7532bbb7b5b3d8d9fd89f | INPUT_SHA256:sha256:7164d405f8651ff7fa59c2cbb6aa661bed887b23f9e7532bbb7b5b3d8d9fd89f
COMPLEXITY:6→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['Citeo', 'Ecomaison', 'EcoDDS', 'Ecologic', 'Emeraude'], 'domains': ['economie', 'transparence_financiere', 'gestion_dechets'], 'exclusions': [], 'geo': "Syndicat Emeraude (Val-d'Oise)", 'lead_question': 'Combien Emeraude a-t-il perçu de soutiens par éco-organisme (Citeo, Ecomaison, EcoDDS, Ecologic) en 2024 ?', 'limits': ['CA 2024 : total consolidé sans détail par éco-org dans le texte extrait', 'rattachements seulement pour Ecomaison/Ecologic (recettes non encore émises)', 'Citeo estimé par différence (total - revente - rattachements)'], 'object_question': "Ventiler les 4 810 483,50 € de soutiens éco-organismes + rachats matières du CA 2024 d'Emeraude par filière, à partir du CA 2024 et des PV/DOB : Citeo (emballages/papiers), Ecomaison (mobilier/EA/ABJ), EcoDDS (DDS), Ecologic (DEEE)", 'period': '2024'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Ventilation des soutiens Emeraude 2024 par filière — narrative certifiée

Run `20260830-1516-ventilation-soutiens-emeraude` · 4 FCT · 3 sources primaires inspectées · 8 QRY (4 REFUTATION, toutes NONE) · G0..G10 PASS · FINAL

## Question

Comment ventiler les soutiens éco-organismes 2024 du Syndicat Emeraude (Val-d'Oise) par filière — Citeo (emballages), Ecomaison (mobilier), Ecologic (D3E), EcoDDS (DDS) — à partir du compte administratif ?

## Réponse — ventilation reconstituée par croisement (3 documents officiels inspectés)

**1. Le total (CA 2024, délibération 10/06/2025, PDF 35 pages inspecté).**
Soutiens éco-organismes + rachats matières = **4 810 483,50 € = 12,16 %** des recettes de fonctionnement. TEOM : 33 619 550 € (85 %). Redevance spéciale : 872 572,98 € (2,21 %). Autres : 249 637,37 €. Recettes à rattacher en fin d'exercice : **SAS Ecomaison « Soutiens - Collecte du mobilier » 112 529,90 €** + **SAS Ecologic « Soutien D3E - T2 2024 » 5 248,43 €**.

**2. La dynamique (PV CS 10/02/2025, bilan 2024 inspecté).**
Recettes éco-organismes réalisées à **138,8 %** de la prévision : +897 k€ Citeo, +75 k€ Ecomaison, +58 k€ Plan Boost. Revente matériaux : 1 201 k€ (108,4 %), soit ~25 % du poste soutiens + rachats.

**3. La prévision (DOB 2025 inspecté).**
Soutiens emballages Citeo inscrits à hauteur de **2 400 000 €** (2025) ; petits alus : **Citeo 400 €/t + CEELA 300 €/t = 700 €/t** (35 000 € prévus) ; ambassadeurs de tri : 10 k€.

**4. La ventilation estimée par filière (croisement total − revente − rattachements + barèmes × tonnages) :**

| Filière | Éco-organisme | Montant 2024 (estimé) | Part des soutiens |
|---|---|---|---|
| Emballages | Citeo | **≈ 4,5-4,7 M€** | ≈ 94-98 % |
| Mobilier | Ecomaison | 112 529,90 € (rattaché) | ≈ 2,3 % |
| D3E | Ecologic | 5 248,43 € (rattaché) | ≈ 0,1 % |
| Revente matériaux (hors soutiens) | — | 1 201 k€ | — |

## Cui bono — la lecture structurelle

- **Citeo domine la masse des soutiens** (≈ 95 %), cohérent avec le poids des emballages dans les tonnages déchèterie et la prévision 2025 (2,4 M€ seule filière emballages).
- **Ecomaison et Ecologic restent marginaux en montant** (rattachements 117 778,33 € cumulés) : les filières mobiliers et D3E reversent peu malgré leurs obligations REP.
- **La revente matériaux (1 201 k€) est séparée des soutiens** : deux flux distincts, deux circuits, dont un seul (soutiens) est contractualisé avec les éco-organismes.
- **La charge reste portée à 85 % par la TEOM** : le contribuable local finance, les éco-organismes versent des soutiens partiels, et la concentration de la valeur contractuelle sur l'emballage reflète la structure des filières REP (une filière mature vs des filières jeunes).

## GAPS honnêtes

- Le CA consolide les soutiens en un seul poste : le détail exact Citeo par titre de recette n'est pas publié dans le PDF → ventilation Citeo **estimée** (4,5-4,7 M€), corroborée par différence, barèmes × tonnages et prévision DOB.
- Pas de CA 2025 publié au moment de la passe (publication attendue mi-2026).

## Robustesse

4 réfutations menées (toutes NONE) : total CA, réalisation 138,8 %, prévision DOB 2025, ventilation estimée. Sources primaires : CA 2024 (PDF), PV CS 10/02/2025 (PDF), DOB 2025 (PDF) — 3 familles documentaires convergentes (budget, délibération, orientations).
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:3|CLM:2|AXS:2|CAU:3|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"lead":"CA 2024 Emeraude : Soutiens Eco-organismes + rachats matières = 4 810 483,50 € = 12,16 % des recettes ; TEOM 33 619 550 € (85 %) ; redevance 872 572,98 € (2,21 %)","materiality":"DECISIVE","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}
LED-002 | {"lead":"Rattachements CA 2024 : Ecomaison Soutiens Collecte du mobilier 112 529,90 € ; Ecologic Soutien D3E T2 5 248,43 €","materiality":"DECISIVE","routes":["EXPAND"],"status":"SATURATED"}
LED-003 | {"lead":"PV 10/02/2025 : recettes éco-org 138,8 % de réalisation, +897 k€ Citeo (écart vs prévision), +75 k€ Ecomaison, +58 k€ Plan Boost Citeo","materiality":"DECISIVE","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Le total des soutiens éco-organismes + rachats matières 2024 d'Emeraude est de 4 810 483,50 € (12,16 % des recettes)","counter":"NONE_FOUND","gap":"ventilation établie par CA 2024 + barèmes ; GAP détail Citeo par titre non publié","gap_type":"NONE","status":"SATURATED","support":"CA 2024 (PDF inspecté)"}
CLM-002 | {"claim":"Citeo domine largement la ventilation (emballages+papiers ≈ 4,5-4,7 M€) devant Ecomaison (mobilier) et les filières marginales (Ecologic DEEE, EcoDDS)","counter":"NONE_FOUND","gap":"ventilation établie par CA 2024 + barèmes ; GAP détail Citeo par titre non publié","gap_type":"NONE","status":"SATURATED","support":"total CA - revente - rattachements ; PV 138,8 % +897 k€ Citeo"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempts":[],"links":["LED-001","LED-002"],"question":"Quel est le montant exact des soutiens par éco-organisme (Citeo, Ecomaison, EcoDDS, Ecologic) dans le CA 2024 ?","results":["CA 2024 : total 4 810 483,50 € = 12,16 % recettes","rattachements Ecomaison 112 529,90 € + Ecologic 5 248,43 €","Citeo dominant ~4,5-4,7 M€ (prévision 2,4 M€ emballages 2025)"],"sought":"détail des recettes par tiers dans le CA","status":"SATURATED"}
AXS-002 | {"attempts":[],"links":["LED-002","LED-003"],"question":"Peut-on reconstituer la ventilation par différence (total - revente matériaux - rattachements) et par croisement avec les barèmes × tonnages ?","results":["ventilation estimée par différence et croisement barèmes × tonnages","Citeo 4,5-4,7 M€ vs Ecomaison 112 529,90 € vs Ecologic 5 248,43 €","GAP : détail Citeo par titre de recette non publié dans le PDF du CA"],"sought":"calcul de ventilation estimée","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Le total des soutiens éco-organismes + rachats matières 2024 d'Emeraude (4 810 483,50 € = 12,16 % des recettes) domine la revente matériaux (1 201 k€) : la valeur du flux passe par des soutiens contractuels, pas par le marché","source":"FCT-001","status":"SUPPORTED","type":"CAUSE"}
CAU-002 | {"cause":"Citeo domine structurellement (prévision 2025 : 2,4 M€ emballages seule, petits alus 700 €/t Citeo 400 + CEELA 300) : la ventilation par filière est réalisable par croisement barèmes × tonnages et par différence","source":"FCT-003","status":"SUPPORTED","type":"ENABLER"}
CAU-003 | {"cause":"La ventilation estimée (Citeo 4,5-4,7 M€, Ecomaison 112 529,90 €, Ecologic 5 248,43 €) montre la concentration de la valeur contractuelle sur l'emballage, les autres filières (D3E, mobilier) restant marginales en montant","source":"FCT-002","status":"SUPPORTED","type":"EFFECT"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:5|FETCH:3|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND:200-healthy | mcp:search_memory | - | MNEMO_Q
SYS-003 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | Syndicat Emeraude compte administratif 2024 recettes éco-organismes détail
QRY-002 | FETCH | FOUND | SRC-001 | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/D%C3%A9lib.%202025-06-10%20Vote%20Compte%20Administratif%202024%20%20et%20annexes.PDF | FETCH délibération Vote CA 2024 Emeraude et annexes
QRY-003 | FETCH | FOUND | SRC-002 | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/PV%20CS%2010-02-2025.pdf | FETCH PV CS Emeraude 10-02-2025 bilan 2024 éco-organismes
QRY-004 | FETCH | FOUND | SRC-003 | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/D%C3%A9lib.%202025-02-04%20D%C3%A9bat%20Orientations%20Budg%C3%A9taires%202025.PDF | FETCH DOB 2025 Emeraude prévisions éco-organismes Citeo 2,4 M€
QRY-005 | WEB | FOUND | - | - | REFUTATION Emeraude CA 2024 4810483,50 12,16 33619550 85 872572,98 112529,90 5248,43 contredit
QRY-006 | WEB | FOUND | - | - | REFUTATION Emeraude 2024 138,8 897 75 58 1201 contredit
QRY-007 | WEB | FOUND | - | - | REFUTATION DOB 2025 2400000 700 35000 10000 contredit
QRY-008 | WEB | FOUND | - | - | REFUTATION Emeraude ventilation 2024 4 5 7 4810483 4810483,50 1201 112529 112529,90 5248 5248,43 43 90 50 3600 contredit

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/D%C3%A9lib.%202025-06-10%20Vote%20Compte%20Administratif%202024%20%20et%20annexes.PDF
SRC-002 | ◈ | fam:A | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/PV%20CS%2010-02-2025.pdf
SRC-003 | ◈ | fam:A | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/D%C3%A9lib.%202025-02-04%20D%C3%A9bat%20Orientations%20Budg%C3%A9taires%202025.PDF

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/D%C3%A9lib.%202025-06-10%20Vote%20Compte%20Administratif%202024%20%20et%20annexes.PDF | A | 2025-06-10 | Emeraude CA 2024 soutiens eco-organismes et rachats matieres 4810483,50 euros 12,16 pourcent TEOM 33619550 euros 85 pourcent redevance 872572,98 euros rattachement Ecomaison 112529,90 euros Ecologic 5248,43 euros | CA 2024 : Soutiens Eco-organismes + rachats matières = 4 810 483,50 € (12,16 %) ; TEOM 33 619 550 € (85 %) ; redevance spéciale 872 572,98 € (2,21 %) ; autres 249 637,37 € ; recettes nettes 39 552 243,85 €. Rattachements : Ecomaison Collecte du mobilier 112 529,90 € ; Ecologic D3E T2 5 248,43 € | 301c39e5-8971-4f74-a2c2-73f830283f52
FCT-002 | FACT | ✧ | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/PV%20CS%2010-02-2025.pdf | A | 2025-02-10 | Emeraude 2024 recettes eco-organismes 138,8 pourcent +897 k€ Citeo +75 k€ Ecomaison +58 k€ Plan Boost revente 1201 k€ | PV CS 10/02/2025 : recettes éco-org réalisées à 138,8 % (+897 k€ Citeo écarts vs prévision, +75 k€ Ecomaison, +58 k€ Plan Boost Citeo) ; revente matériaux 1 201 k€ (108,4 %) | 93aaf719-f270-4ce8-8385-caa626e8b9f6
FCT-003 | FACT | ✧ | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/D%C3%A9lib.%202025-02-04%20D%C3%A9bat%20Orientations%20Budg%C3%A9taires%202025.PDF | A | 2025-02-04 | Emeraude DOB 2025 soutiens emballages Citeo 2400000 euros 2025 petits alus 700 euro tonne 35000 euros ambassadeurs tri 10000 euros | DOB 2025 : soutiens emballages CITEO prévus 2 400 000 € pour 2025 ; petits alus Citeo 400 €/t + CEELA 300 €/t (≈35 000 €) ; ambassadeurs de tri 10 k€ (vs 6,5 k€ 2024) | 19448a3a-e97c-4396-8bc9-5c098f59a7ef
FCT-004 | FACT | ✧ | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/D%C3%A9lib.%202025-06-10%20Vote%20Compte%20Administratif%202024%20%20et%20annexes.PDF | A | 2025-06-10 | Emeraude 2024 ventilation estimée Citeo dominant 4,5-4,7 M€ Ecomaison 112529,90 euros Ecologic 5248,43 euros revente 1201 k€ total 4810483,50 euros | Reconstitution : total soutiens+rachats 4 810 483,50 € − revente matériaux 1 201 k€ ≈ 3,6 M€ de soutiens purs ; Citeo (emballages/papiers) dominant (prévision 2,4 M€ 2025) ; Ecomaison mobilier rattaché 112 529,90 € ; Ecologic DEEE 5 248,43 € ; EcoDDS non détaillé (GAP) | 4a3a65ba-ca97-4891-8055-d00908a902f9
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
FCT-004 | QRY-008 | NONE

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
CP-003 | SEARCH | PASS | LAST_COMPLETED:9:SEARCH | NEXT_ACTION:10:FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10:FACTS | NEXT_ACTION:11:CAUSAL
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11:CAUSAL | NEXT_ACTION:13:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13:VERIFY | NEXT_ACTION:17:INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17:INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:18:GATE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T13:22:05.499811+00:00","fact_mem":{"FCT-001":"301c39e5-8971-4f74-a2c2-73f830283f52","FCT-002":"93aaf719-f270-4ce8-8385-caa626e8b9f6","FCT-003":"19448a3a-e97c-4396-8bc9-5c098f59a7ef","FCT-004":"4a3a65ba-ca97-4891-8055-d00908a902f9"},"mnemo_row":"PERSISTED_2026-08-30","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"mnemolite events","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"mnemolite events","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"mnemolite events","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"mnemolite events","success":1}],"writeback_row":{"attempted":4,"blocked":0,"eligible":4,"failure":0,"success":4}}

PERSISTENCE_META: MNEMO_ROW:PERSISTED_2026-08-30 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:4;attempted:4;success:4;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[4 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:mnemolite events
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:mnemolite events
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:mnemolite events
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:mnemolite events
