ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-1454-baremes-par-site-epci | PARENT_RUN_ID:NONE | AS_OF:2026-08-30
INPUT_KIND:CLAIM | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_baremes-par-site-epci/2026-08-30_14-54_baremes-par-site-epci_INPUT.txt | SUBJECT_SLUG:baremes-par-site-epci | SUBJECT_FP:sha256:f527cda14586c4418761ee597537909f21c943d3b1f3787a21a103e3f198353f | INPUT_SHA256:sha256:f527cda14586c4418761ee597537909f21c943d3b1f3787a21a103e3f198353f
COMPLEXITY:6→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['Citeo', 'Ecomaison', 'EcoDDS', 'Ecominero', 'Valobat', 'collectivites', 'EPCI', 'syndicats', 'AMORCE', 'ADEME'], 'domains': ['economie', 'reglementation', 'transparence_financiere', 'gestion_dechets'], 'exclusions': [], 'geo': 'France (EPCI/syndicats de déchets)', 'lead_question': 'Peut-on reconstituer la ventilation réelle des soutiens REP (€/t ou forfaits) par déchèterie à partir des délibérations territoriales et conventions éco-organismes par EPCI, malgré le champ SINOE LST_TYPE_DECHET vide ?', 'limits': ['LST_TYPE_DECHET SINOE vide 100% sites', 'barèmes par site non publiés nationalement', 'accès aux conventions territoriales inégal'], 'object_question': 'Identifier les mécanismes concrets de captation de la valeur au point de captage (déchèterie) : conventions éco-org par EPCI, délibérations de collectivités/syndicats mentionnant tonnages et soutiens, ventilation par site, et qui bénéficie réellement (cui bono)', 'period': '2019-2026'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Passe KERNEL — Ventilation des barèmes REP par déchèterie : contourner SINOE via délibérations et conventions par EPCI

**Run** : 20260830-1454-baremes-par-site-epci · **As-of** : 2026-08-30 · **Mode** : INVESTIGATION · **Complexité** : COMPLEX

## Question pilote

> Peut-on reconstituer la ventilation réelle des soutiens REP (€/t ou forfaits) par déchèterie, malgré le champ SINOE `LST_TYPE_DECHET` vide sur 100 % des sites, à partir des délibérations territoriales et conventions éco-organismes par EPCI ?

## Méthode

1. **Mémoire d'abord** (`MNEMO_Q`, mémoire saine 200-healthy, probe NONE — pas de snapshot exact à hydrater) ; les FCT de la passe barèmes (20260830-1416) restent des références chaudes.
2. **Axes** : AXS-001 (documents territoriaux par EPCI) ; AXS-002 (reconstitution de la ventilation par site + cui bono).
3. **Sources primaires inspectées** (4 documents territoriaux réels, famille A) : PV Comité Syndical **Emeraude** 10/02/2025 (bilan 2024), contrat-type **Ecomaison ABJ** v18/04/2025 (SIEDMTO, annexe 3B), délibération **SEROC** CS/2025-028 (reversement soutiens Citeo), délibérations **Tri-Action** CS 02/07/2025.
4. **Réfutation systématique** : contre-requêtes adverses par FCT (toutes NONE ; le 776 €/t plastique Tri-Action confirme indépendamment le barème OCAPEM de la passe précédente).
5. **Causation** : chaîne ENABLER→CAUSE→EFFECT posée ; AXS/CLM/LED SATURATED.

## Faits retenus (FCT, tier ✧, source territoriale inspectée)

- **FCT-001 · Emeraude (PV CS 10/02/2025)** — déchèterie du syndicat : **11 073 t en 2024** ; recettes de revente matériaux **1 201 k€** (pic 1 617 k€ en 2022) ; recettes éco-organismes **réalisées à 138,8 %** de la prévision (+897 k€ Citeo, +75 k€ Ecomaison) ; verre soutenu **18,15 €/t au T4 2024** (28,36 €/t T1 2024 → 10 €/t T1 2025).
- **FCT-002 · Ecomaison ABJ (contrat-type v18/04/2025, SIEDMTO annexe 3B)** — barème par déchèterie : **forfait 2 700 €/contenant >30 m³** (1 350 € si <30 m³), part variable **20 €/t enlèvement**, collecte + recyclage en déchèterie **65 €/t** (19 €/t inertes, 0 €/t ferrailles), zone réemploi **200 €**, communication **100 €** ; versements semestriels sur déclaration.
- **FCT-003 · SEROC (délib. CS/2025-028)** — chaîne de reversement Citeo→syndicat→adhérents : **10 000 €/ambassadeur de tri** (1 ADT/8 000 hab ; 16 ADT pour 130 645 hab), **SCC = +3 % du soutien à la tonne** ; reversement au prorata de la population.
- **FCT-004 · Tri-Action (délib. CS 02/07/2025)** — déchèterie de Bessancourt : **91 461 entrées / 10 443 t en 2024** (hors DT/REP) ; plastique **660 €/t avec extension vs 600 €/t hors extension, revalorisé 776 €/t pour 2025** (corrobore OCAPEM) ; contrat Ecomaison ABJ forfait 2 700 €/contenant.
- **FCT-005 · Captation territoriale (Emeraude, même PV)** — flux développement plastique : **Citeo fera son affaire du surtri/valorisation et en percevra les recettes** (collectivité soutenue 776 €/t) ; machines de déconsigne : la collectivité **« ne perçoit, ni recette matériaux, ni soutien au tri »** sur ces tonnages (8-12 t/an/machine).

## Réfutation (toutes NONE)

Contre-requêtes adverses littérales par FCT avec discriminants numériques : aucune contradiction découverte. Le montant **776 €/t plastique** (Tri-Action 2025) recoupe le barème aval OCAPEM déjà corroboré à la passe précédente → indépendance croisée famille A.

## Chaîne causale (CAU-001→003)

- **ENABLER** : les barèmes €/t et forfaits par déchèterie sont fixés par contrats-types des éco-organismes (Ecomaison ABJ 2 700 €/contenant + 20-65 €/t ; Citeo €/t par matériau) et versés semestriellement.
- **CAUSE** : les collectivités déclarent tonnages et entrées par site (Emeraude 11 073 t ; Bessancourt 91 461 entrées) → **la ventilation par site est reconstituable malgré SINOE vide**.
- **EFFECT** : sur certains flux (déconsigne, flux développement), l'éco-organisme capte les recettes de revente ; la collectivité ne perçoit ni recette matériaux ni soutien au tri.

## Conclusion — ventilation reconstituable, captation confirmée au niveau territorial

**Le contournement fonctionne** : les délibérations territoriales et conventions par EPCI permettent de reconstituer une ventilation concrète par déchèterie (tonnages/entrées × barèmes €/t/forfaits), là où SINOE `LST_TYPE_DECHET` reste vide. Trois EPCI témoins documentés : **Emeraude** (11 073 t, 1 201 k€ revente, soutiens 138,8 %), **Tri-Action** (10 443 t, 91 461 entrées), **SEROC** (mécanique de reversement Citeo→adhérents).

**Cui bono au point de captage** : la collectivité perçoit des soutiens (fixés par contrat-type, versés semestriellement) mais, sur les flux où l'éco-organisme organise le traitement (flux développement) ou sur les dispositifs qu'il ne soutient pas (déconsigne), **la valeur de revente échappe au service public** — documenté mot pour mot au PV Emeraude. Les montants sont volatils (verre 28,36→18,15→10 €/t en un an) et les recettes de revente dépendent de marchés (EMR 175,20→43,10 €/t en 2022).

## Gaps & limites (OPEN)

- **Échantillon limité** : 3 EPCI témoins (Emeraude, Tri-Action, SEROC) — pas de ventilation nationale par site.
- **Annexe 1 des contrats (liste des déchèteries)** : version publiée du contrat-type SIEDMTO sans conditions particulières → la ventilation exacte par site exige les conventions signées (portail TERRITEO).
- **Montants Citeo par déchèterie** : non publiés individuellement (reversement au syndicat, puis prorata population).
- SINOE `LST_TYPE_DECHET` vide : l'opacité de la donnée officielle demeure, contournée mais non comblée.

## Soumission

Faisceau convergent : barèmes contrat-type (T1) + tonnages/entrées déclarés par site + mécanique de reversement + captation documentée (flux développement, déconsigne) → la ventilation par déchèterie est **matériellement reconstituable** et la **captation de la valeur par l'éco-organisme est confirmée au niveau territorial**, pas seulement au niveau national (IGEEDD).
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:3|CLM:2|AXS:2|CAU:3|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"lead":"Les délibérations des collectivités et syndicats de déchets (EPCI) mentionnent tonnages et soutiens REP par déchèterie, permettant de ventiler les barèmes €/t par site","materiality":"DECISIVE","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}
LED-002 | {"lead":"Les conventions éco-organismes par EPCI (Citeo, Ecomaison, EcoDDS, Valobat, Ecominero) fixent les montants versés et les flux couverts","materiality":"DECISIVE","routes":["EXPAND"],"status":"SATURATED"}
LED-003 | {"lead":"Le champ SINOE LST_TYPE_DECHET est vide sur 100% des sites : la donnée officielle ne permet pas le croisement par flux","materiality":"IMPORTANT","routes":["CONTEXT"],"status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Les soutiens REP versés aux collectivités varient par flux et par tonnage (barèmes €/t ou forfaits par déchèterie)","counter":"NONE_FOUND","gap":"à confirmer par sources territoriales inspectées","gap_type":"NONE","status":"SATURATED","support":"barèmes cités en mémoire"}
CLM-002 | {"claim":"La ventilation réelle par site est reconstituable depuis les documents publics locaux malgré SINOE vide","counter":"NONE_FOUND","gap":"à établir sur 1-2 EPCI documentés","gap_type":"NONE","status":"SATURATED","support":"hypothèse de travail"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempts":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006"],"links":["LED-001","LED-002"],"question":"Quelles délibérations/conventions territoriales (par EPCI) documentent tonnages et soutiens REP par déchèterie ?","results":["FCT-001","FCT-002","FCT-003","FCT-004"],"sought":"délibérations, conventions, rapports annuels de service public déchets","status":"SATURATED"}
AXS-002 | {"attempts":["QRY-003","QRY-006"],"links":["LED-002","LED-003"],"question":"Peut-on reconstituer la ventilation €/t par site et mesurer la part captée (cui bono) sur un EPCI témoin ?","results":["FCT-001","FCT-005"],"sought":"montants par site, tonnages par flux, soutiens perçus vs valeur reprise","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Les barèmes €/t et forfaits par déchèterie sont fixés par contrat-type des éco-organismes (Ecomaison ABJ 2700 euros par contenant + 20-65 euros/t ; Citeo euros/t par matériau) et versés aux collectivités par semestre","source":"FCT-002","status":"SUPPORTED","type":"ENABLER"}
CAU-002 | {"cause":"Les collectivités déclarent tonnages et entrées par site (Emeraude 11073 t déchèterie, Bessancourt 91461 entrées) : la ventilation par site est donc reconstituable malgré SINOE vide","source":"FCT-001","status":"SUPPORTED","type":"CAUSE"}
CAU-003 | {"cause":"Sur certains flux (déconsigne, flux développement), l'éco-organisme capte les recettes de revente et la collectivité ne perçoit ni recette matériaux ni soutien au tri","source":"FCT-005","status":"SUPPORTED","type":"EFFECT"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:11|FETCH:4|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"EMPTY","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND:200-healthy | mcp:search_memory | - | MNEMO_Q
SYS-003 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | délibération convention Citeo 2025 syndicat déchets montant soutien euros tonne emballages collecte sélective tonnage déchèterie
QRY-002 | WEB | FOUND | - | - | convention EcoDDS Ecomaison déchèterie soutien montant euros collectivité délibération syndicat tonnages site 2024 2025
QRY-003 | FETCH | FOUND | SRC-001 | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/PV%20CS%2010-02-2025.pdf | FETCH PV Comité Syndical Emeraude 10-02-2025
QRY-004 | FETCH | FOUND | SRC-002 | https://www.siedmto.fr/media/071db2025-renouvellement-du-contrat-abj-avec-ecomaison-vannexee.pdf | FETCH contrat ABJ Ecomaison SIEDMTO annexe 3B barème soutiens
QRY-005 | FETCH | FOUND | SRC-003 | https://seroc14.fr/wp-content/uploads/2025/09/CSD2025_02820250916_CS_2025-028_Modalites_de_reversement_aux_adherents_des_soutiens_financiers_CITEO_pour_la_sensibilisation_et_la_maitrise_des_couts.pdf | FETCH délibération SEROC 2025-028 reversement soutiens CITEO aux adhérents
QRY-006 | FETCH | FOUND | SRC-004 | https://syndicat-tri-action.fr/wp-content/uploads/2025/07/deliberations-CS-020725.pdf | FETCH délibérations Tri-Action CS 02/07/2025 soutiens barèmes flux développement
QRY-007 | WEB | FOUND | - | - | barème aval Citeo 2025 776 plastique 660 extension tri corroboration
QRY-008 | WEB | FOUND | - | - | REFUTATION Emeraude 1201 k€ recettes revente materiaux 2024 verre 18,15 euro tonne T4 2024 11073 tonnes déchèterie contredit autre source
QRY-009 | WEB | FOUND | - | - | REFUTATION barème Ecomaison ABJ forfait déchèterie 2700 euros 20 euro tonne 65 euro tonne 200 euros zone réemploi contredit autre montant
QRY-010 | WEB | FOUND | - | - | REFUTATION Bessancourt 10443 tonnes 2024 91461 entrées plastique 776 euro tonne 2025 contredit
QRY-011 | WEB | FOUND | - | - | REFUTATION Emeraude bilan 2024 11073 tonnes déchèterie 1201 138 8 897 75 contredit
QRY-012 | WEB | FOUND | - | - | REFUTATION barème Ecomaison ABJ 2025 2700 30 20 65 200 contredit
QRY-013 | WEB | FOUND | - | - | REFUTATION SEROC 10000 8000 3 16 130645 contredit
QRY-014 | WEB | FOUND | - | - | REFUTATION Tri-Action 91461 10443 2024 776 2025 2700 contredit
QRY-015 | WEB | FOUND | - | - | REFUTATION Emeraude déconsigne 8 12 776 contredit

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/PV%20CS%2010-02-2025.pdf
SRC-002 | ◈ | fam:A | https://www.siedmto.fr/media/071db2025-renouvellement-du-contrat-abj-avec-ecomaison-vannexee.pdf
SRC-003 | ◈ | fam:A | https://seroc14.fr/wp-content/uploads/2025/09/CSD2025_02820250916_CS_2025-028_Modalites_de_reversement_aux_adherents_des_soutiens_financiers_CITEO_pour_la_sensibilisation_et_la_maitrise_des_couts.pdf
SRC-004 | ◈ | fam:A | https://syndicat-tri-action.fr/wp-content/uploads/2025/07/deliberations-CS-020725.pdf

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/PV%20CS%2010-02-2025.pdf | A | 2025-02-10 | Emeraude bilan 2024 déchèterie 11073 tonnes recettes revente materiaux 1201 k€ realisation recettes eco-organismes 138,8 pourcent Citeo +897 k€ Ecomaison +75 k€ | PV CS 10/02/2025 : déchèterie Emeraude 11 073 t en 2024 ; recettes revente matériaux 1 201 k€ (pic 1 617 k€ en 2022) ; recettes éco-org 138,8 % de la prévision (+897 k€ Citeo, +75 k€ Ecomaison) ; verre 18,15 €/t T4 2024 | f12a1298-84dd-44aa-af4f-5810ebc6f26f
FCT-002 | FACT | ✧ | https://www.siedmto.fr/media/071db2025-renouvellement-du-contrat-abj-avec-ecomaison-vannexee.pdf | A | 2025-04-18 | barème Ecomaison ABJ 2025 contrat type SIEDMTO forfait déchèterie 2700 euros contenant 30m3 part variable 20 euro tonne enlèvement 65 euro tonne collecte recyclée zone réemploi 200 euros | Annexe 3B contrat-type Ecomaison ABJ v18/04/2025 : forfait déchèterie 2 700 €/contenant >30 m³ (1 350 € si <30 m³), part variable enlèvement 20 €/t, collecte+recyclage déchèterie 65 €/t (19 €/t inertes, 0 €/t ferrailles), zone réemploi 200 € | 922d5d60-a060-4f36-a665-6ccf2326d460
FCT-003 | FACT | ✧ | https://seroc14.fr/wp-content/uploads/2025/09/CSD2025_02820250916_CS_2025-028_Modalites_de_reversement_aux_adherents_des_soutiens_financiers_CITEO_pour_la_sensibilisation_et_la_maitrise_des_couts.pdf | A | 2025-09-16 | SEROC reversement soutiens Citeo adhérents 10000 euros ambassadeur tri 8000 habitants SCC 3 pourcent soutien tonne plafond 16 ADT population 130645 | Délibération CS/2025-028 : Citeo reverse via le syndicat ; SAdt 10 000 €/ambassadeur (1 ADT/8 000 hab, 16 ADT pour 130 645 hab), SCC = majoration 3 % du soutien à la tonne ; reversement aux adhérents au prorata de la population | 9d423a5f-cbf6-457a-8bed-cb002ffdc928
FCT-004 | FACT | ✧ | https://syndicat-tri-action.fr/wp-content/uploads/2025/07/deliberations-CS-020725.pdf | A | 2025-07-02 | Tri-Action Bessancourt déchèterie 91461 entrées 10443 tonnes 2024 plastique flux développement 776 euro tonne 2025 forfait déchèterie 2700 euros Ecomaison | Délibérations Tri-Action 02/07/2025 : déchèterie Bessancourt 91 461 entrées / 10 443 t 2024 (hors DT/REP) ; plastique 660 €/t avec extension vs 600 €/t hors extension, revalorisé 776 €/t 2025 ; contrat Ecomaison ABJ forfait 2 700 €/contenant | b82acdc9-97e5-4bab-8d97-47f4ee6960dc
FCT-005 | FACT | ✧ | https://www.syndicat-emeraude.fr/sites/default/files/media/downloads/PV%20CS%2010-02-2025.pdf | A | 2025-02-10 | Emeraude déconsigne ni recette materiaux ni soutien tri machines 8-12 tonnes flux développement Citeo perçoit recettes surtri 776 euro tonne | PV CS 10/02/2025 : sur le flux développement plastique, Citeo fera son affaire du surtri/valorisation et en percevra les recettes (collectivité soutenue 776 €/t) ; machines déconsigne : collectivité ne perçoit ni recette matériaux ni soutien au tri (8-12 t/an/machine) | 8a857cfd-5717-4bdd-b1c9-bb91bfb0b472
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-003
FCT-004 | SRC-004
FCT-005 | SRC-001

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-011 | NONE
FCT-002 | QRY-012 | NONE
FCT-003 | QRY-013 | NONE
FCT-004 | QRY-014 | NONE
FCT-005 | QRY-015 | NONE

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
CP-001 | LEADS | PASS | LAST_COMPLETED:5:LEADS | NEXT_ACTION:7:SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7:SCOPE | NEXT_ACTION:9:SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9:SEARCH:QRY-015 | NEXT_ACTION:10:FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10:FCT-005 | NEXT_ACTION:11:CAUSAL
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11:CAU-003 | NEXT_ACTION:13:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13:VERIFY | NEXT_ACTION:17:INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17:INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:18:GATE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T13:00:17.026154+00:00","fact_mem":{"FCT-001":"f12a1298-84dd-44aa-af4f-5810ebc6f26f","FCT-002":"922d5d60-a060-4f36-a665-6ccf2326d460","FCT-003":"9d423a5f-cbf6-457a-8bed-cb002ffdc928","FCT-004":"b82acdc9-97e5-4bab-8d97-47f4ee6960dc","FCT-005":"8a857cfd-5717-4bdd-b1c9-bb91bfb0b472"},"mnemo_row":"PERSISTED_2026-08-30","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"mnemolite events","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"mnemolite events","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"mnemolite events","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"mnemolite events","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"mnemolite events","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:PERSISTED_2026-08-30 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:mnemolite events
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:mnemolite events
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:mnemolite events
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:mnemolite events
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:mnemolite events
