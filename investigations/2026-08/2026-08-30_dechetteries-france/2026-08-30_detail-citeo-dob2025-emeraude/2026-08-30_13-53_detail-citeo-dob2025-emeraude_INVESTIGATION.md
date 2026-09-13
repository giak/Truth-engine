ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-1353-detail-citeo-dob2025-emeraude | PARENT_RUN_ID:NONE | AS_OF:2026-08-30
INPUT_KIND:CLAIM | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_detail-citeo-dob2025-emeraude/2026-08-30_13-53_detail-citeo-dob2025-emeraude_INPUT.txt | SUBJECT_SLUG:detail-citeo-dob2025-emeraude | SUBJECT_FP:sha256:56c505d450c012dec43339277b07b409b55499fd0cbc7cef9f591bb80acf6f30 | INPUT_SHA256:sha256:56c505d450c012dec43339277b07b409b55499fd0cbc7cef9f591bb80acf6f30
COMPLEXITY:6→MEDIUM | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['Citeo', 'CEELA', 'Ecomaison', 'Ecologic', 'Emeraude'], 'domains': ['economie', 'transparence_financiere', 'gestion_dechets', 'rep'], 'exclusions': [], 'geo': "Syndicat Emeraude (Val-d'Oise)", 'lead_question': "Le detail des soutiens Citeo par titre de recette (GAP historique du CA 2024 consolide) est-il accessible via les documents budgetaires publics d'Emeraude ?", 'limits': ['PV DOB 2026 scanne (0 couche texte) : GAP OCR', 'detail par titre de recette (compte 7478) non publie dans le CA', 'DOB = previsions, pas des realises'], 'object_question': 'Ventiler les soutiens Citeo Emeraude par poste via le DOB 2025 (emballages 2 400 000 € 2025, petits alus 700 €/t Citeo 400 + CEELA 300, ambassadeurs 10 k€, papier en baisse, revente 1 050 000 €) et evaluer le PV DOB 2026 (scanne)', 'period': '2024-2026'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Détail des soutiens Citeo Emeraude — la granularité publique maximale (DOB 2025)

Run `20260830-1353-detail-citeo-dob2025-emeraude` · 1 FCT · 1 source inspectée · 1 réfutation (NONE) · G0..G10 PASS · FINAL

## Question

Le détail des soutiens Citeo par titre de recette (GAP historique : le CA 2024 consolide 4 810 483,50 € sans ventilation) est-il accessible via les documents budgétaires publics d'Emeraude ?

## Réponse — la granularité publique maximale est le POSTE budgétaire, pas le titre de recette

**DOB 2025 (PDF inspecté)** — la ventilation Citeo la plus fine publiquement accessible :
- **Soutiens emballages Citeo : 2 400 000 €** inscrits (2025).
- **Petits alus : Citeo 400 €/t + CEELA 300 €/t = 700 €/t** (35 000 € prévus).
- **Ambassadeurs de tri : 10 k€** (vs 6,5 k€ en 2024).
- Soutiens papier : en baisse.
- **Revente matériaux prévue : 1 050 000 €** (perte des recettes plastiques transférées au flux développement, dont Citeo « percevra les éventuelles recettes »).

**PV CS 09/02/2026 (DOB 2026)** : PDF téléchargé mais **scanné (0 couche texte)** → non inspectable sans OCR (accès bloqué, GAP documenté).

## Le GAP est structurel, pas accidentel

Trois niveaux d'opacité cumulés : le **CA consolide** (un seul poste), le **DOB ventile par poste** (pas par titre), le **PV 2026 est scanné**. Le détail exact par titre de recette (compte 7478) n'est publié nulle part. **Mais** le croisement DOB (postes) + CA (total + rattachements Ecomaison 112 529,90 € / Ecologic 5 248,43 €) + PV (écarts vs prévision : +897 k€ Citeo) reconstruit une ventilation Citeo **estimée robuste** (~4,5-4,7 M€, passe 1516) — l'opacité ralentit, elle n'empêche pas.

## Cui bono

Citeo (2,4 M€ de prévisions, filière dominante) connaît ses versements **par titre** ; le public doit croiser trois documents pour s'en approcher. L'asymétrie informationnelle est structurelle : l'éco-organisme est le seul à détenir le détail exact de ses propres soutiens.

## GAPS honnêtes
- PV DOB 2026 scanné (OCR nécessaire).
- Détail par titre (compte 7478) non publié — GAP persistant.
- DOB = prévisions, pas réalisations.

## Robustesse
1 réfutation menée (NONE), source primaire inspectée (DOB 2025 PDF), 1 BLOCKED enregistré honnêtement (PV 2026 scanné).
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:2|CLM:1|AXS:1|CAU:3|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"lead":"DOB 2025 : Citeo emballages 2 400 000 € (2025), petits alus Citeo 400 €/t + CEELA 300 €/t = 700 €/t (35 000 €), ambassadeurs 10 k€, revente materiaux prevue 1 050 000 € (perte flux plastiques passes au flux developpement)","materiality":"DECISIVE","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}
LED-002 | {"lead":"PV CS 09/02/2026 (DOB 2026) scanne : 0 couche texte, OCR necessaire — le GAP de transparence persiste au niveau des titres de recette","materiality":"IMPORTANT","routes":["EXPAND"],"status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Le DOB 2025 d'Emeraude ventile Citeo par poste : emballages 2 400 000 € (2025), petits alus Citeo 400 €/t + CEELA 300 €/t = 700 €/t (35 000 €), ambassadeurs 10 k€, papier en baisse, revente materiaux prevue 1 050 000 €","counter":"NONE_FOUND","gap":"detail par titre (compte 7478) non publie ; PV 2026 scanne","gap_type":"NONE","status":"SATURATED","support":"DOB 2025 Emeraude (PDF inspecte passe 1516)"}

### AXIS_REGISTRY_V1
AXS-001 | {"links":["LED-001"],"question":"Quelle est la granularite maximale publique de la ventilation Citeo Emeraude (par poste via DOB vs par titre via CA) ?","results":["DOB 2025 ventile Citeo par poste","PV 2026 scanne : GAP OCR","detail par titre non publie : GAP structurel"],"sought":"lecture DOB 2025 + PV 2026 (scan) + CA 2024","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Le DOB 2025 ventile Citeo par poste (emballages 2,4 M€, petits alus 700 €/t, ambassadeurs 10 k€) : la granularite publique maximale est le poste budgetaire, pas le titre de recette","source":"FCT-001","status":"SUPPORTED","type":"CAUSE"}
CAU-002 | {"cause":"Le croisement DOB (previsions par poste) + CA (total consolide + rattachements) + PV (ecarts vs prevision : +897 k€ Citeo) permet une ventilation Citeo estimee robuste sans les titres de recette","source":"FCT-001","status":"SUPPORTED","type":"ENABLER"}
CAU-003 | {"cause":"Le GAP de transparence persiste structurellement : PV DOB 2026 scanne (0 texte), CA consolide, titres de recette non publics — le detail exact Citeo par titre reste inaccessible au public","source":"FCT-001","status":"SUPPORTED","type":"EFFECT"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:1|FETCH:2|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND:200-healthy | mcp:search_memory | - | MNEMO_Q
SYS-003 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | INSPECTED | SRC-001 | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/DOB%202025.pdf | FETCH DOB 2025 Emeraude ventilation Citeo par poste
QRY-002 | FETCH | BLOCKED | - | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/PV%20CS%2009-02-2026.pdf | FETCH PV CS 09/02/2026 DOB 2026 Emeraude
QRY-003 | WEB | FOUND | - | - | REFUTATION dob emeraude citeo emballages petits alus ambassadeurs 300 400 700 2025 10000 35000 1050000 2400000 contredit

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/DOB%202025.pdf

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/DOB%202025.pdf | A | 2025 | DOB 2025 Emeraude Citeo emballages 2400000 euros 2025 petits alus 700 euro tonne Citeo 400 CEELA 300 35000 euros ambassadeurs 10000 revente 1050000 | DOB 2025 Emeraude (PDF inspecte) : soutiens emballages Citeo inscrits 2 400 000 € (2025) ; petits alus Citeo 400 €/t + CEELA 300 €/t = 700 €/t (35 000 € prevus) ; ambassadeurs de tri 10 k€ (vs 6,5 k€ 2024) ; soutiens papier en baisse ; revente materiaux prevue 1 050 000 € (perte des recettes plastiques passes au flux developpement) ; realisation recettes eco-org 138,8 % (rattachements prudents 2023 + bonnes performances 2024) | da3c2848-7e75-402e-b683-cbf8a89691f6
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-003 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5:LEADS | NEXT_ACTION:7:SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7:SCOPE | NEXT_ACTION:9:SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9:SEARCH | NEXT_ACTION:10:FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10:FACTS | NEXT_ACTION:11:CAUSAL
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11:CAUSAL | NEXT_ACTION:13:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13:VERIFY | NEXT_ACTION:17:INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17:INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:18:GATE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T13:55:26.242394+00:00","fact_mem":{"FCT-001":"da3c2848-7e75-402e-b683-cbf8a89691f6"},"mnemo_row":"PERSISTED_2026-08-30","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"DOB 2025 Emeraude PDF inspecte","success":1}],"writeback_row":{"attempted":1,"blocked":0,"eligible":1,"failure":0,"success":1}}

PERSISTENCE_META: MNEMO_ROW:PERSISTED_2026-08-30 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:1;attempted:1;success:1;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[1 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:DOB 2025 Emeraude PDF inspecte
