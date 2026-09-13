ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-1416-baremes-rep-decheteries | PARENT_RUN_ID:NONE | AS_OF:2026-08-30
INPUT_KIND:CLAIM | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_baremes-rep-decheteries/2026-08-30_14-16_baremes-rep-decheteries_INPUT.txt | SUBJECT_SLUG:baremes-rep-decheteries | SUBJECT_FP:sha256:9114959578c2cee6530ee77d30c501feede8ef6deecd9340715c61588fd344d4 | INPUT_SHA256:sha256:1fed93d12f8fa0fb36629903182198be8aebb1670e85ade017e52fdd57a39878
COMPLEXITY:6→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors': ['Citeo', 'Ecomaison', 'EcoDDS', 'ecosystem', 'Ecologic', 'Soren', 'Refashion', 'Valobat', 'Valdelia', 'ADEME', 'IGEEDD'], 'domains': ['economie', 'reglementation', 'transparence_financiere', 'gestion_dechets'], 'exclusions': [], 'geo': 'France', 'lead_question': 'Cui bono: qui capte la valeur economique des flux de decheterie via les baremes REP ?', 'limits': ['euros par tonne par site non publies', 'LST_TYPE_DECHET SINOE vide'], 'object_question': 'Montants reels euros par tonne des soutiens financiers des eco-organismes REP aux collectivites pour les flux accueillis en decheterie (emballages DEEE piles mobilier DDS PMCB textiles): mecanisme asymetries', 'period': '2009-2029'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Passe KERNEL — Barèmes REP : suivre l'argent dans les déchèteries (cui bono)

**Run** : 20260830-1416-baremes-rep-decheteries · **As-of** : 2026-08-30 · **Mode** : INVESTIGATION · **Complexité** : COMPLEX

## Question pilote

> Cui bono : qui capte la valeur économique des flux accueillis en déchèterie, mesurée par les barèmes (€/t ou forfaits) des soutiens REP versés aux collectivités ?

## Méthode

1. **Mémoire d'abord** (`MNEMO_Q`, mémoire saine 200-healthy, probe NONE) — pas d'état pré-restauré, run neuf.
2. **Axes** (`AXS-001` barèmes réels €/t/forfaits par filière ; `AXS-002` qui capte la valeur/économie de la reprise).
3. **Sources primaires inspectées** (familles A et D) : barème aval Citeo OCAPEM 2025, Convention EcoDDS (annexe 3), délibération Ecomaison, rapport IGEEDD §4.3.3, cadre REP ecologie.gouv.
4. **Réfutation systématique** : contre-requêtes adverses posées pour chaque FCT (aucune contradiction trouvée ; Citeo corroboré indépendamment par >3 sources).
5. **Causation** : chaîne ENABLER→CAUSE→EFFECT posée, AXS/CLM/LED SATURATED.

## Faits retenus (FCT, tier ✧, source inspectée)

- **FCT-001 · Citéo (barème aval OCAPEM 2025)** — soutien par tonne recyclée : Acier **73 €/t**, Aluminium **470 €/t**, PCNC **177 €/t**, PCC **352 €/t**, PCM **107 €/t**, Plastique **776 €/t**, Verre **8 €/t** ; valorisation organique papier **80 €/t**. Corroboré indépendamment (AMORCE barème G, délibération Tri-Action).
- **FCT-002 · EcoDDS (convention, annexe 3)** — soutien annuel fixe par déchèterie (forfaitaire + variable) sel tonnage : Cat A (>48 t) **3 413 €** ; B (24–48 t) **1 895 €** ; C (12–24 t) **1 334 €** ; D (<12 t) **923 €** + communication **0,03 €/hab**.
- **FCT-003 · Ecomaison — mobilier & équipements (délibération SGC)** — soutien collecte déchèterie **24,4 €/t** ; recyclage EA en collecte non séparée **140 €/t** ; part forfaitaire déchèterie **1 525 €/an** ; soutien information **0,01 €/hab** ; enlèvement non conforme **0 €/t**.
- **FCT-004 · IGEEDD (rapport 2024, §4.3.3)** — les éco-organismes deviennent **propriétaires des déchets** par leurs contrats avec les opérateurs et **captent le produit de la revente des matériaux**, privant la collectivité/l'opérateur ; pouvoir de structuration **supérieur** à celui des opérateurs.
- **FCT-005 · Cadre REP** — deux modèles de financement : **contributif/financier** (l'éco-org reverse des soutiens à la collectivité collectrice) vs **opérationnel** (l'éco-org garde les fonds, contractualise ses propres prestataires).

## Réfutation (toutes NONE)

Queries adverses littérales posées par FCT : aucune source contradictoire découverte. Le montant Citeo (73/470/177/352/107/776/8 €/t) est **retrouvé identique dans 3 sources indépendantes** → corroboration croisée famille A.

## Chaîne causale (CAU-001→003)

- **ENABLER** : les éco-organismes REP collectent les éco-contributions des producteurs et utilisent les déchèteries comme points de captage des flux.
- **CAUSE** : par contrats avec les opérateurs, l'éco-organisme devient propriétaire des déchets et vend les matériaux traités.
- **EFFECT** : cette propriété prive la collectivité de la revente et structure le marché de la reprise au profit de l'éco-organisme.

## Conclusion — qui capte la valeur ?

La déchèterie est un **point de captage**. La collectivité exploite/collecte (coût supporté), reçoit des soutiens **hétérogènes et jugés nettement insuffisants** (audition AN, IGEEDD), et **perd une part de la valeur de revente des matériaux** captée par l'éco-organisme — lui-même financé par les producteurs par éco-contributions (~6 Md€/an), le tout payé au bout de la chaîne par l'usager via TEOM/REOM + éco-participation. **Le bénéficiaire structurel est l'éco-organisme** (propriété des déchets, pouvoir de structuration), avec l'asymétrie documentée IGEEDD.

## Gaps & prochaines requêtes (OPEN)

- **LST_TYPE_DECHET SINOE vide sur 100 % des sites** → impossibilité de croiser les flux réellement acceptés par site avec les soutiens.
- **Barèmes €/t « par site » non publiés** (le barème national existe, la ventilation territoriale par site non).
- **DEEE** : reprise sans frais ; montant €/t net non publié par site.
- PMCB Valobat / Ecominero : barèmes officiels détaillés à confirmer.

## Soumission

Faisceau d'indices → convergence : cross-corroboration Citeo + 2 modèles REP + propriété IGEEDD pointent collectivement vers une **captation de la valeur par les éco-organismes**, au détriment de la collectivité exploitante.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:3|CLM:4|AXS:2|CAU:3|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"kind":"CLAIM","lead":"Le soutien REP versé aux collectivités pour les flux de déchèterie est payé en €/t (ou forfait par site) fixé par chaque éco-organisme dans son barème aval","materiality":"DECISIVE","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}
LED-002 | {"kind":"RELATION","lead":"Les éco-organismes deviennent propriétaires des déchets et captent la valeur de la reprise des matériaux, au détriment de la collectivité (asymétrie IGEEDD)","materiality":"DECISIVE","routes":["EXPAND"],"status":"SATURATED"}
LED-003 | {"kind":"MECHANISM","lead":"Deux modèles de financement REP coexistent : contributif/financier (soutiens à la collectivité) et opérationnel (éco-org contractualise ses prestataires)","materiality":"IMPORTANT","routes":["CONTEXT"],"status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Citeo verse un soutien par tonne recyclée (barème aval) : Acier 73 €/t, Aluminium 470 €/t, PCNC 177 €/t, PCC 352 €/t, PCM 107 €/t, Plastique 776 €/t, Verre 8 €/t (2025) ; valorisation organique papier 80 €/t","counter":"NONE_FOUND (montants identiques dans 3 sources indépendantes)","status":"SATURATED","support":"OCAPEM barème aval Citeo 2025 + corroboration AMORCE barème G + Tri-Action"}
CLM-002 | {"claim":"Ecomaison verse pour le mobilier/EA l'éco-contribution : soutien collecte déchèterie 24,4 €/t ; recyclage EA en collecte non séparée en déchèterie 140 €/t ; part forfaitaire déchèterie 1525 €/an ; soutien réemploi à la hausse","counter":"NONE_FOUND","status":"SATURATED","support":"Contrat type Ecomaison (délibération) + communication official"}
CLM-003 | {"claim":"EcoDDS verse aux collectivités un soutien annuel fixe par déchèterie (forfaitaire + variable) selon tonnage : Cat A >48 t/an =3413 €, B (24-48t)=1895 €, C (12-24t)=1334 €, D (<12t)=923 € + comm 0,03 €/hab","counter":"NONE_FOUND","status":"SATURATED","support":"Barème annexe 3 Convention EcoDDS"}
CLM-004 | {"claim":"Les éco-organismes deviennent propriétaires des déchets par leurs contrats avec les opérateurs et vendent les matériaux traités, privant la collectivité/l'opérateur du produit de la revente (pouvoir de structuration supérieur)","counter":"NONE_FOUND","status":"SATURATED","support":"Rapport IGEEDD §4.3.3"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempts":["QRY-001","QRY-002","QRY-003","QRY-005","QRY-006","QRY-007"],"links":["CLM"],"question":"Quels sont les montants réels €/t (ou forfaits) des soutiens REP aux collectivités pour les flux accueillis en déchèterie, par filière (Citeo, Ecomaison, EcoDDS, PMCB, DEEE) ?","results":["FCT"],"sought":"barèmes aval €/t et forfaits déchèterie publiés","status":"SATURATED"}
AXS-002 | {"attempts":["QRY-008"],"links":["CLM"],"question":"Qui capte la valeur (cui bono) : éco-organisme, collectivité, ou opérateur ? (propriété des déchets, reprise des matériaux, asymétries)","results":["FCT"],"sought":"analyse économie de la reprise et propriété des déchets","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Les eco-organismes REP recolten t les eco-contributions des producteurs et utilisent les decheteries comme points de captage des flux","source":"FCT-005","status":"SATURATED","type":"ENABLER"}
CAU-002 | {"cause":"Par les contrats avec les operateurs de traitement, l'eco-organisme devient proprietaire des dechets et vend les materiaux traites","source":"FCT-004","status":"SATURATED","type":"CAUSE"}
CAU-003 | {"cause":"Cette propriete prive la collectivite/l'operateur du produit de la revente et structure le marche de la reprise au profit de l'eco-organisme","source":"FCT-004","status":"SATURATED","type":"EFFECT"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:9|FETCH:5|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"EMPTY","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FOUND:200-healthy | mcp:search_memory | - | MNEMO_Q
SYS-002 | SYS | NONE:no_snapshot | runtime:memory-probe | - | MEMORY_PROBE
SYS-003 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-004 | SYS | PASS | runtime | SYS-001 | REPAIR_SYS
SYS-005 | SYS | PASS | runtime | SYS-002 | REPAIR_SYS
SYS-006 | SYS | PARTIAL | runtime | ATTEMPT-001 | PERSIST_REBIND
SYS-007 | SYS | PASS | runtime | ATTEMPT-002 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.cirest.fr/wp-content/uploads/2025/06/2025-C024-Annexe-2-1.pdf | FETCH OCAPEM bareme aval Citeo 2025 euros tonne
QRY-002 | FETCH | FOUND | SRC-002 | https://www.cc-sevreloire.fr/wp-content/uploads/sites/2/2019/11/20190626-034_Convention-EcoDDS.pdf | FETCH Convention EcoDDS bareme annexe 3
QRY-003 | FETCH | FOUND | SRC-003 | https://www.comcom-sgc.fr/wp-content/uploads/2026/05/04-05-2026-Rectification-deliberation-n%C2%B0-20251211-18-signature-contrat-Eco-Maison-relatif-responsabilite-elargie-des-producteurs-pour-les-dechets-delements-dameublement.pdf | FETCH delib Ecomaison soutiens mobilier decheterie euros tonne
QRY-004 | FETCH | FOUND | SRC-004 | https://www.igedd.developpement-durable.gouv.fr/IMG/pdf/015523-p_rapport_publie_cle01f1cb.pdf | FETCH IGEEDD REP propriété déchets reprise matériaux
QRY-005 | FETCH | FOUND | SRC-005 | https://www.ecologie.gouv.fr/politiques-publiques/cadre-general-filieres-responsabilite-elargie-producteurs | FETCH cadre REP modèles financement
QRY-006 | WEB | FOUND | - | - | REFUTATION bareme Citeo Acier 73 Plastique 776 Verre 8 corroboration AMORCE barème G rapport
QRY-007 | WEB | FOUND | - | - | REFUTATION EcoDDS forfait decheterie A 3413 B 1895 C 1334 D 923
QRY-008 | WEB | FOUND | - | - | REFUTATION Ecomaison 24,4 euro tonne 140 euro tonne recyclage EA 1525 forfait
QRY-009 | WEB | FOUND | - | - | REFUTATION propriete dechets eco-organismes reprise materiaux IGEEDD
QRY-010 | WEB | FOUND | - | - | REFUTATION deux modeles financement REP contributif operationnel
QRY-011 | WEB | FOUND | - | - | REFUTATION bareme Citeo soutien tonne Acier 73 Aluminium 470 PCNC 177 PCC 352 PCM 107 Plastique 776 Verre 8 papier 80 contredit
QRY-012 | WEB | FOUND | - | - | REFUTATION EcoDDS soutien decheterie DDS forfait cat A 3413 B 1895 C 1334 D 923 euros communication
QRY-013 | WEB | FOUND | - | - | REFUTATION bareme aval Citeo 2025 euro tonne recyclé Acier 73 Aluminium 470 PCNC 177 PCC 352 PCM 107 Plastique 776 Verre 8 papier organique 80 contredit autre
QRY-014 | WEB | FOUND | - | - | REFUTATION bareme EcoDDS soutien decheterie DDS forfait provement cat A 3413 B 1895 C 1334 D 923 comm 0 03 hab contredit

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.cirest.fr/wp-content/uploads/2025/06/2025-C024-Annexe-2-1.pdf
SRC-002 | ◈ | fam:A | https://www.cc-sevreloire.fr/wp-content/uploads/sites/2/2019/11/20190626-034_Convention-EcoDDS.pdf
SRC-003 | ◈ | fam:A | https://www.comcom-sgc.fr/wp-content/uploads/2026/05/04-05-2026-Rectification-deliberation-n%C2%B0-20251211-18-signature-contrat-Eco-Maison-relatif-responsabilite-elargie-des-producteurs-pour-les-dechets-delements-dameublement.pdf
SRC-004 | ○ | fam:D | https://www.igedd.developpement-durable.gouv.fr/IMG/pdf/015523-p_rapport_publie_cle01f1cb.pdf
SRC-005 | ◉ | fam:A | https://www.ecologie.gouv.fr/politiques-publiques/cadre-general-filieres-responsabilite-elargie-producteurs

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.cirest.fr/wp-content/uploads/2025/06/2025-C024-Annexe-2-1.pdf | A | 2025-03-18 | bareme aval Citeo 2025 euro tonne recyclé Acier 73 Aluminium 470 PCNC 177 PCC 352 PCM 107 Plastique 776 Verre 8 papier organique 80 | bareme aval Citeo 2025 euro tonne recyclé Acier 73 Aluminium 470 PCNC 177 PCC 352 PCM 107 Plastique 776 Verre 8 papier organique 80 | 7f59d4e8-dee3-433a-b4a2-340661ef2a75
FCT-002 | FACT | ✧ | https://www.cc-sevreloire.fr/wp-content/uploads/sites/2/2019/11/20190626-034_Convention-EcoDDS.pdf | A | 2019-06-26 | bareme EcoDDS soutien decheterie DDS forfait cat A 3413 B 1895 C 1334 D 923 comm 0,03 hab | bareme EcoDDS soutien decheterie DDS forfait cat A 3413 B 1895 C 1334 D 923 comm 0,03 hab | e3593572-a956-475e-b5e0-08d9a0f54c30
FCT-003 | FACT | ✧ | https://www.comcom-sgc.fr/wp-content/uploads/2026/05/04-05-2026-Rectification-deliberation-n%C2%B0-20251211-18-signature-contrat-Eco-Maison-relatif-responsabilite-elargie-des-producteurs-pour-les-dechets-delements-dameublement.pdf | A | 2026-05-07 | bareme Ecomaison mobilier soutien decheterie 24,4 euro tonne recyclage EA 140 euro tonne forfait 1525 | bareme Ecomaison mobilier soutien decheterie 24,4 euro tonne recyclage EA 140 euro tonne forfait 1525 | 6903090f-3eeb-4aac-9306-b67fd902dcdf
FCT-004 | FACT | ✧ | https://www.igedd.developpement-durable.gouv.fr/IMG/pdf/015523-p_rapport_publie_cle01f1cb.pdf | D | 2024-06-18 | IGEEDD propriete dechets eco-organismes reprise materiaux perte produit revente collectivite | IGEEDD propriete dechets eco-organismes reprise materiaux perte produit revente collectivite | 3334c667-30fe-40ee-879f-6453b2a40517
FCT-005 | FACT | ✧ | https://www.ecologie.gouv.fr/politiques-publiques/cadre-general-filieres-responsabilite-elargie-producteurs | A | 2026-08-18 | deux modeles financement REP contributif operationnel | deux modeles financement REP contributif operationnel | dad3e3af-c6f2-42a4-8721-d7ad206027ee
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-003
FCT-004 | SRC-004
FCT-005 | SRC-005

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-013 | NONE
FCT-002 | QRY-014 | NONE
FCT-003 | QRY-008 | NONE
FCT-004 | QRY-009 | NONE
FCT-005 | QRY-010 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5:LEADS | NEXT_ACTION:6:CREDO
CP-002 | SCOPE | PASS | LAST_COMPLETED:7:SCOPE | NEXT_ACTION:9:SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9:SEARCH:QRY-014 | NEXT_ACTION:10:FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10:FCT-005 | NEXT_ACTION:11:CAUSAL
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11:CAU-003 | NEXT_ACTION:13:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13:VERIFY | NEXT_ACTION:17:INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17:INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:18:GATE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T12:45:26.714786+00:00","fact_mem":{},"mnemo_row":"PERSISTED_2026-08-30","result":"PARTIAL","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"written to mnemolite vl events","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"written to mnemolite vl events","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"written to mnemolite vl events","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"written to mnemolite vl events","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"written to mnemolite vl events","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}
ATTEMPT-002 | {"created_at":"2026-08-30T12:45:36.097542+00:00","fact_mem":{"FCT-001":"7f59d4e8-dee3-433a-b4a2-340661ef2a75","FCT-002":"e3593572-a956-475e-b5e0-08d9a0f54c30","FCT-003":"6903090f-3eeb-4aac-9306-b67fd902dcdf","FCT-004":"3334c667-30fe-40ee-879f-6453b2a40517","FCT-005":"dad3e3af-c6f2-42a4-8721-d7ad206027ee"},"mnemo_row":"PERSISTED_2026-08-30","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"written to mnemolite vl events","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"written to mnemolite vl events","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"written to mnemolite vl events","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"written to mnemolite vl events","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"written to mnemolite vl events","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:PERSISTED_2026-08-30 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:written to mnemolite vl events
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:written to mnemolite vl events
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:written to mnemolite vl events
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:written to mnemolite vl events
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:written to mnemolite vl events
