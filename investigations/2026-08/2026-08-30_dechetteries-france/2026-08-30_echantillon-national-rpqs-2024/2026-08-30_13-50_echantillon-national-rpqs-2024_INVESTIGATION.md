ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-1350-echantillon-national-rpqs-2024 | PARENT_RUN_ID:NONE | AS_OF:2026-08-30
INPUT_KIND:CLAIM | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_echantillon-national-rpqs-2024/2026-08-30_13-50_echantillon-national-rpqs-2024_INPUT.txt | SUBJECT_SLUG:echantillon-national-rpqs-2024 | SUBJECT_FP:sha256:a22a4f86d563c28e0fa795249d3433205ad819eba6ebe4634b271fc078e6074c | INPUT_SHA256:sha256:a22a4f86d563c28e0fa795249d3433205ad819eba6ebe4634b271fc078e6074c
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['Citeo', 'Valobat', 'Ecosystem', 'EcoDDS', 'CYCLEVIA', 'Ecomobilier', 'OCAD3E', 'CCST', 'Redon Agglomeration'], 'domains': ['economie', 'transparence_financiere', 'gestion_dechets', 'rep', 'pmcb'], 'exclusions': [], 'geo': 'Territoire de Belfort (90, CCST), Ille-et-Vilaine (35, Redon)', 'lead_question': 'Peut-on elargir la carte nationale des soutiens REP par decheterie avec des RPQS 2024 de nouveaux EPCI (diversite geographique et demographique) ?', 'limits': ['Redon : total decheterie exact non isole (57 % du tonnage total 31 750 t)', 'CCST : gros poste 520 863,21 € non identifie precisement (probablement Citeo emballages)', 'echantillon 13 EPCI : toujours pas representatif national'], 'object_question': 'Ajouter CCST Sud Territoire (90, 2 dechetteries, 8 171 t, soutiens 604 723,61 €) et Redon Agglomeration (35, soutiens par eco-org : Citeo 1 000 062 €, Valobat 54 299 €, Ecosystem 71 063 €, EcoDDS 7 865 €) aux 11 EPCI deja documentes -> 13 EPCI', 'period': '2024'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Élargissement de la carte nationale des soutiens REP — CCST et Redon (13 EPCI)

Run `20260830-1350-echantillon-national-rpqs-2024` · 2 FCT · 2 sources inspectées · 5 QRY (2 REFUTATION, toutes NONE) · G0..G10 PASS · FINAL

## Question

Peut-on élargir la carte nationale des soutiens REP par déchèterie avec des RPQS 2024 de nouveaux EPCI, au-delà des 11 déjà documentés ?

## Réponse — oui, 2 nouveaux EPCI documentés (13 au total)

**CCST Sud Territoire** (Territoire de Belfort, 90) — rapport d'activité 2024 (PDF inspecté) :
- **2 déchetteries** (Fêche-l'Église, Grandvillars), 23 filières.
- **8 171 t** en 2024 (+10 %) : verts 3 284 t · encombrants 1 746 t · gravats 1 307 t · bois 793 t · ferraille 357 t · cartons 278 t · plâtre 153 t · huisseries 62 t · acier 72 t · pneus 81 t · aluminium 21 t · DDS 13 t.
- **Soutiens éco-organismes : 604 723,61 €** (-3,4 %) = **74 €/t** ; ventes matériaux 100 896 €. Poste principal 520 863,21 € consolidé (non ventilé).

**Redon Agglomération** (Ille-et-Vilaine, 35) — rapport annuel 2024 (PDF 42 p. inspecté) : **ventilation COMPLÈTE par éco-organisme en euros** :
| Éco-organisme | Flux | Tonnage | Montant |
|---|---|---|---|
| **Citeo** | emballages | — | **1 000 062 €** (298 €/t, 16,73 €/hab) |
| Citeo-EcoDDS-CYCLEVIA-Ecomobilier | divers | — | 217 888 € (+112 %) |
| Citeo papier | papiers | — | 52 000 € (-20 %) |
| Citeo | autres | — | 37 939 € |
| **Valobat** | multimatériaux PMCB | 1 363 t | **54 299 €** |
| **Ecosystem** | D3E | 616 t | **71 063 €** |
| EcoDDS | DDS | 97 t | 7 865 € |
| CYCLEVIA | huiles | 32 t | 1 800 € |
| REP PMCB | (au 01/10/24) | 439 t | économie estimée 39 502 € |

## La perle — les filières jeunes sont chiffrables en euros au niveau territorial

Redon documente **Valobat (PMCB) 54 299 €** et **Ecosystem (D3E) 71 063 €** : la ventilation par éco-organisme existe et se publie, y compris pour les filières récentes. Les bennes multimatériaux Valobat (6 déchèteries) font prendre en charge transport et traitement **directement par l'éco-organisme** (133 t détournées du non valorisable) — une forme de captation de la valeur en amont.

## Cui bono — les leçons de l'échantillon à 13

1. **Diversité des ratios confirmée** : 74 €/t (CCST) vs 34 €/t (TPM) vs 69 €/t (Ambert) → carte par EPCI obligatoire.
2. **Citeo reste dominant** (Redon : 1 000 062 € ≈ 70 % du total documenté) mais la pluralisation s'accélère (+112 % sur le poste Citeo-EcoDDS-CYCLEVIA-Ecomobilier).
3. **L'opacité est un choix** : CCST consolide son poste principal (520 863,21 € non ventilé), Redon publie tout.

## GAPS honnêtes
- Gros poste CCST 520 863,21 € non identifié (probablement Citeo emballages, non confirmé).
- Total déchèteries Redon non isolé (57 % des 31 750 t).
- 13 EPCI : toujours un échantillon orienté, pas représentatif national.

## Robustesse
2 réfutations menées (toutes NONE), 2 sources primaires inspectées (famille A), chaque FCT lu directement dans le PDF.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:3|CLM:1|AXS:2|CAU:3|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"lead":"CCST Sud Territoire (90) RPQS 2024 : 2 dechetteries, 8 171 t (verts 3 284, encombrants 1 746, gravats 1 307, bois 793, ferraille 357, cartons 278, platre 153, huisseries 62, acier 72, pneus 81, alu 21, DDS 13), soutiens eco-org 604 723,61 € = 74 €/t","materiality":"DECISIVE","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}
LED-002 | {"lead":"Redon Agglomeration (35) rapport 2024 : soutiens ventiles par eco-org — Citeo 1 000 062 € (298 €/t), Citeo-EcoDDS-CYCLEVIA-Ecomobilier 217 888 € (+112 %), Citeo papier 52 000 €, Citeo 37 939 €, Ecosystem D3E 616 t = 71 063 €, Valobat multimat 1 363 t = 54 299 €, EcoDDS 97 t = 7 865 €, CYCLEVIA 1 800 € ; REP PMCB 439 t (economie 39 502 €)","materiality":"DECISIVE","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}
LED-003 | {"lead":"Redon documente des soutiens PMCB/D3E en euros (Valobat 54 299 €, Ecosystem 71 063 €) : preuve que la ventilation par eco-organisme existe au niveau territorial, y compris pour les filieres jeunes","materiality":"IMPORTANT","routes":["EXPAND"],"status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"La carte nationale des soutiens REP s'elargit : CCST 74 euro/t (8 171 t) et Redon avec ventilation complete par eco-org dont Valobat 54 299 euro et Ecosystem 71 063 euro","counter":"NONE_FOUND","gap":"total decheterie Redon non isole ; gros poste CCST 520 863,21 non identifie","gap_type":"NONE","status":"SATURATED","support":"RPQS CCST 2024 + rapport Redon 2024 (PDF inspectes)"}

### AXIS_REGISTRY_V1
AXS-001 | {"links":["LED-001","LED-002"],"question":"Les nouveaux EPCI (CCST, Redon) confirment-ils la diversite des ratios soutiens/tonnage et la ventilation par eco-organisme ?","results":["CCST 74 €/t confirme la diversite","Redon ventile par eco-org dont Valobat 54 299 € et Ecosystem 71 063 €","GAP : gros poste CCST 520 863,21 non identifie"],"sought":"lecture RPQS CCST 2024 et rapport Redon 2024","status":"SATURATED"}
AXS-002 | {"links":["LED-003"],"question":"Les soutiens des filieres jeunes (Valobat PMCB, Ecosystem D3E) sont-ils documentables en euros par site ?","results":["CCST 74 €/t confirme la diversite","Redon ventile par eco-org dont Valobat 54 299 € et Ecosystem 71 063 €","GAP : gros poste CCST 520 863,21 non identifie"],"sought":"montants Valobat/Ecosystem dans les rapports territoriaux","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Le ratio soutiens/tonnage varie encore (CCST 74 €/t vs TPM 34 €/t vs Ambert 69 €/t) : la carte nationale doit rester par EPCI, la moyenne nationale resterait trompeuse","source":"FCT-001","status":"SUPPORTED","type":"CAUSE"}
CAU-002 | {"cause":"Redon prouve que la ventilation par eco-organisme est publiee au niveau territorial, y compris pour les filieres jeunes : Valobat 54 299 € (1 363 t), Ecosystem 71 063 € (616 t), EcoDDS 7 865 € (97 t), CYCLEVIA 1 800 € — la carte nationale peut inclure les filieres hors Citeo quand le rapport est detaille","source":"FCT-002","status":"SUPPORTED","type":"ENABLER"}
CAU-003 | {"cause":"Les soutiens Citeo restent dominants (Redon 1 000 062 € = 70 % du total documente) mais la pluralisation s'accelere : Citeo-EcoDDS-CYCLEVIA-Ecomobilier +112 % et REP PMCB 439 t montrent la montee des filieres jeunes dans le financement des decheteries","source":"FCT-002","status":"SUPPORTED","type":"EFFECT"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:3|FETCH:2|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND:200-healthy | mcp:search_memory | - | MNEMO_Q
SYS-003 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | RPQS rapport annuel dechets 2024 decheterie soutiens eco-organismes euros EPCI pdf
QRY-002 | FETCH | INSPECTED | SRC-001 | https://www.cc-sud-territoire.fr/ged/rapport-d-activit---2024.pdf | FETCH rapport activite 2024 CCST Sud Territoire dechetteries soutiens
QRY-003 | FETCH | INSPECTED | SRC-002 | https://www.redon-agglomeration.bzh/sites/default/files/2026-03/rapport_annuel_2024_vf.pdf | FETCH rapport annuel 2024 Redon Agglomeration soutiens par eco-organisme
QRY-004 | WEB | FOUND | - | - | REFUTATION ccst sud territoire dechetteries tonnes soutiens citeo ecomobilier 2 21 61 76 88 2024 8171 21144 24240 38474 520863 604723 contredit
QRY-005 | WEB | FOUND | - | - | REFUTATION redon agglomeration soutiens citeo valobat ecosystem pmcb 97 298 439 616 1363 1800 2024 7865 37939 52000 54299 71063 217888 1000062 contredit

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.cc-sud-territoire.fr/ged/rapport-d-activit---2024.pdf
SRC-002 | ◈ | fam:A | https://www.redon-agglomeration.bzh/sites/default/files/2026-03/rapport_annuel_2024_vf.pdf

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.cc-sud-territoire.fr/ged/rapport-d-activit---2024.pdf | A | 2025 | CCST Sud Territoire 2024 2 dechetteries 8171 tonnes soutiens eco-organismes 604723,61 euros Citeo 38474,76 Citeo papier 24240,76 Ecomobilier 21144,88 520863,21 | CCST Sud Territoire (90, 23 560 hab) rapport activite 2024 : 2 dechetteries (Fêche-l'Eglise, Grandvillars) ; tonnages 2024 par materiau : verts 3 284 t, encombrants 1 746 t, gravats 1 307 t, bois 793 t, ferraille 357 t, cartons 278 t, platre 153 t, huisseries 62 t, acier 72 t, pneus 81 t, aluminium 21 t, DDS 13 t, batteries 4 t = total 8 171 t (+10 % vs 2023, verts +22 %) ; soutiens eco-organismes 604 723,61 € (-3,4 % vs 2023 = -20 585,39 €) : Citeo 38 474,76 € + Citeo papier 24 240,76 € + Ecomobilier 21 144,88 € + gros poste 520 863,21 € (poste principal, non identifie) ; ratio 74 €/t ; ventes materiaux 100 896 € (+10 361 €) | 25480fac-38e4-4098-9278-16c711163795
FCT-002 | FACT | ✧ | https://www.redon-agglomeration.bzh/sites/default/files/2026-03/rapport_annuel_2024_vf.pdf | A | 2026-03 | Redon Agglomeration 2024 soutiens Citeo 1000062 euros 298 euro tonne Citeo papier 52000 Citeo 37939 Citeo EcoDDS CYCLEVIA Ecomobilier 217888 Ecosystem D3E 616 tonnes 71063 euros Valobat multimat 1363 tonnes 54299 euros EcoDDS 97 tonnes 7865 CYCLEVIA 1800 REP PMCB 439 tonnes | Redon Agglomeration (35) rapport annuel 2024 : soutiens eco-organismes ventiles — Citeo 1 000 062 € (9,6 % recettes, 16,73 €/hab, 298 €/t) ; Citeo papier 52 000 € (-20 %) ; Citeo 37 939 € ; Citeo-EcoDDS-CYCLEVIA-Ecomobilier 217 888 € (+112,2 %, 3,64 €/hab, 12,02 €/t) ; Ecosystem D3E 616 t = 71 063 € ; Valobat multimateriaux 1 363 t = 54 299 € ; EcoDDS 97 t = 7 865 € ; CYCLEVIA huile 32 t = 1 800 € ; REP PMCB 439 t (au 01/10/24) avec economie estimee 39 502 € + recettes 17 305 € ; 147 520 passages decheteries (-16 %) ; dechets en decheteries = 57 % du tonnage total 31 750 t ; non valorisables enfouis 3 613 t ; TGAP 234 479 € | 91510559-5d9c-4916-96a9-348c2bb74027
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-004 | NONE
FCT-002 | QRY-005 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5:LEADS | NEXT_ACTION:7:SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7:SCOPE | NEXT_ACTION:9:SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9:SEARCH | NEXT_ACTION:10:FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10:FACTS | NEXT_ACTION:11:CAUSAL
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11:CAUSAL | NEXT_ACTION:13:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13:VERIFY | NEXT_ACTION:17:INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17:INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:18:GATE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T13:52:25.507261+00:00","fact_mem":{"FCT-001":"25480fac-38e4-4098-9278-16c711163795","FCT-002":"91510559-5d9c-4916-96a9-348c2bb74027"},"mnemo_row":"PERSISTED_2026-08-30","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"rapport CCST 2024 PDF inspecte","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"rapport Redon 2024 PDF inspecte","success":1}],"writeback_row":{"attempted":2,"blocked":0,"eligible":2,"failure":0,"success":2}}

PERSISTENCE_META: MNEMO_ROW:PERSISTED_2026-08-30 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:2;attempted:2;success:2;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[2 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:rapport CCST 2024 PDF inspecte
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:rapport Redon 2024 PDF inspecte
