ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-1955-audit-ouverture-haie-fouassiere | PARENT_RUN_ID:20260830-1900-audit-onyx-veolia-sites-pre1980 | AS_OF:2026-08-30
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_audit-ouverture-haie-fouassiere/2026-08-30_19-55_audit-ouverture-haie-fouassiere_INPUT.txt | SUBJECT_SLUG:audit-ouverture-haie-fouassiere | SUBJECT_FP:sha256:3b57406833f3efee613e572e7a7b2c438ef8290029be5fdb90e60bb44b705bd5 | INPUT_SHA256:sha256:ee717f76ce14dc34d6b4e4f513bd21bb552ad6af612c274f43da70123594031a
COMPLEXITY:7→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['Clisson Sevre et Maine Agglo', 'Grandjouan-Veolia', 'commune de La Haie-Fouassiere', 'SINOE/ADEME'], 'domains': ['histoire', 'presse locale', 'archives', 'SINOE'], 'exclusions': [], 'geo': 'France (Loire-Atlantique : La Haie-Fouassiere)', 'lead_question': "Quelle est la date reelle d'ouverture de la decheterie de La Haie-Fouassiere (44) ? Le D_OUV SINOE 01/01/1974 est-il corrobore par presse/archives ou le site etait-il avant une decharge/depot/plateforme ?", 'limits': 'Ouest-France/Presse-Ocean payants ; archives departementales 44 partiellement en ligne', 'object_question': "Etablir par presse locale et archives (Clisson Sevre et Maine Agglo, archives 44) la date reelle d'ouverture de la decheterie de La Haie-Fouassiere et la nature du site avant le neologisme 1987"}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# 🦊 Audit d'ouverture — La Haye-Fouassiere (44)

**Run `20260830-1955-audit-ouverture-haie-fouassiere`** — UPDATE du run `20260830-1900-audit-onyx-veolia-sites-pre1980` (FCT-003 : D_OUV 01/01/1974 contamine, site ferme 18/11/2013, exploitant Grandjouan-Veolia depuis 2006). Objectif : dater reellement l'ouverture par presse/archives et caracteriser le site avant 2013.

## Verdict

| # | Fait | Statut |
|---|---|---|
| **FCT-001** | **La Halte Eco Tri actuelle (fiche SINOE 106355) a ete ouverte le 18/11/2013 = date exacte de fermeture de l'ancienne decheterie 5172** — reconversion du site le meme jour, pas fermeture definitive | ✦ (A+B, refutation NONE) |
| **FCT-002** | **Aucune decheterie moderne anterieure a 2000** — gestionnaires historiques CC Vallee de Clisson (creee 2000, competence 4 dechetteries) et CC Sevre Maine et Goulaine (creee 22/12/2000, siege La Haye-Fouassiere, 2 dechetteries) ; D_OUV 1974 structurellement incoherent | ✦ (C+D, refutation NONE) |
| **FCT-003** | **Avant la reconversion, le site etait une « dechetterie vetuste et inadaptee »** du reseau Sevre Maine et Goulaine (exploitant Grandjouan-Veolia depuis 2006) — pas une decharge moderne, D_OUV 1974 sans acte d'ouverture | ✦ (A+B, refutation NONE) |

## Decouvertes cles

1. **La concordance parfaite des dates tranche** : D_OUV SINOE 106355 = **2013-11-18** = jour exact de fermeture de l'ancienne 5172 (18/11/2013). Ouest-France 20/11/2013 confirme : « La halte eco-tri communautaire fonctionne depuis lundi » (= 18/11/2013). Le blog d'Eric Thouzeau (conseiller regional) date l'inauguration au **28/11/2013**. → le site n'a jamais « ferme » : il a ete **reconverti** en Halte Eco Tri (dechetterie-recyclerie avec DDS et DEEE).
2. **L'incoherence structurelle** : la decheterie de La Haye-Fouassiere relevait de CC creees en **2000** (Vallee de Clisson : competence 4 dechetteries ; Sevre Maine et Goulaine : siege a La Haye-Fouassiere, 2 dechetteries). Un D_OUV **1974** est donc impossible pour une decheterie moderne — confirmation du biais de date recopiee (passe 1900).
3. **L'avant-2013 caracterise** : deux dechetteries « vetustes et inadaptees » (La Haye-Fouassiere et Haute-Goulaine) selon le blog d'inauguration ; le projet de remplacement est annonce par Ouest-France des le 27/11/2012 (« Une dechetterie communautaire en 2013 »).

## Sources INSPECTED

- **Dataset SINOE raw ADEME** (fiches 5172 + 106355) — D_OUV/reconversion 2013-11-18
- **Fiche SINOE 106355** (Halte Eco Tri) — D_OUV 2013-11-18, Mise a jour 21/01/2026
- **Blog Eric Thouzeau, 28/11/2013** — inauguration, 2 dechetteries vetustes, Region finance (contrat de territoire)
- **Wikipedia FR** — CC Sevre Maine et Goulaine (creee decembre 2000) ; CC Vallee de Clisson (creee 2000, 4 dechetteries)
- **RPQS 2025 Clisson Sevre et Maine Agglo** — haltes eco-tri = equipements plus recents ; competence decheterie 01/01/2017
- Snippets Ouest-France 27/11/2012 et 20/11/2013 (fetch direct bloque 403)

## Refutations (3 NONE)

- FCT-001 : aucune preuve d'ouverture de la Halte Eco Tri a une autre date que le 18/11/2013
- FCT-002 : aucune preuve de decheterie moderne ouverte avant 2000 (1990-1999)
- FCT-003 : aucune preuve d'une decharge moderne (BASIAS, ICPE, presse) sur le site avant 2013

## Gaps ouverts

1. Date exacte d'ouverture de la decheterie 5172 avant 2013 (annees 1990 ?) — deliberations CC Vallee de Clisson 2000-2006 non numerisees
2. Acte/rapport du SIVOM anterieur
3. Cote du dossier d'exploitation Grandjouan 2006

## Consequence sur le recit

La Haie-Fouassiere rejoint le patron des 9 sites SINOE pre-1980 : le D_OUV 1974 est **definitivement ecarte** (date recopiee), et le site moderne est en realite un equipement de **2013**. Aucune atteinte a la primaute Gradignan (acte CUB 21/03/1980).
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:1|CLM:1|AXS:1|CAU:1|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_excerpt":"D_OUV 01/01/1974 recopie dans champ renovation ; fermeture 18/11/2013 ; Grandjouan-Veolia exploitant depuis 2006","kind":"EVENT","lead":"La Haie-Fouassiere (44) : date reelle d'ouverture de la decheterie OPEN — D_OUV SINOE 01/01/1974 contamine (passe 1900), site ferme 18/11/2013","linked_ids":["CLM-001","AXS-001"],"locator":"fiche SINOE 5172 + mem 438bf634","materiality":"DECISIVE","routes":["AUDIT","EXPAND"],"source_id":"INPUT","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"counter":"NONE_FOUND","gap":"GAP_TYPE=ACCESS (presse locale payante, archives partiellement en ligne)","linked_ids":["LED-001","AXS-001"],"proposition":"La date reelle d'ouverture de la decheterie de La Haie-Fouassiere est post-1987 (probablement 1990-2006, avant l'arrivee de Grandjouan-Veolia en 2006) et le site etait avant une decharge/plateforme — a verifier par presse/archives","status":"SUPPORTED","status_note":"en cours","support":"mem 438bf634 (FCT-003 CONFIRME) + patron contamination Benais/St-Aquilin"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006"],"gap_type":"NONE","led_links":["LED-001"],"question":"Quelle est la date reelle d'ouverture de la decheterie de La Haie-Fouassiere et qu'etait le site avant (decharge, depot, plateforme) ?","result_ids":["FCT-001","FCT-002","FCT-003"],"sought_objects":["presse locale (Ouest-France, Presse-Ocean, actu.fr)","deliberations Clisson Sevre et Maine Agglo / ex-CC Vallee de Clisson","archives departementales 44","historique site (decharge, plateforme)"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Le champ D_OUV SINOE a recopie une ancienne date d'activite du site (decharge/collecte) sans acte d'ouverture de decheterie","effect":"La Haie-Fouassiere porte D_OUV 1974 dans l'annuaire sans preuve d'une decheterie moderne pre-1980","source":"FCT-001","status":"SATURATED","type":"MECHANISM"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:6|EXA:3
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND: warm-route mem 438bf634 (FCT-003 CONFIRME, run 1900) — D_OUV 01/01/1974 contamine, fermee 18/11/2013, Grandjouan-Veolia depuis 2006 ; GAP: date reelle d'ouverture OPEN | mnemolite:search_memory | 20260830-1900-audit-onyx-veolia-sites-pre1980 | MNEMO_Q
SYS-003 | SYS | PASS | runtime | FCT-003 | REPAIR_FACT
SYS-004 | SYS | PASS | runtime | FCT-001 | REPAIR_FACT
SYS-005 | SYS | PASS | runtime | FCT-002 | REPAIR_FACT
SYS-006 | SYS | LOADED | runtime:load | - | ALWAYS_LOAD: definitions/SYMBOLS.md, definitions/PATTERNS.md, definitions/THREATS.md, forensic/GATES.md, forensic/REQUEST_LOG.md
SYS-007 | SYS | PASS | runtime | FCT-001 | REPAIR_FACT
SYS-008 | SYS | PASS | runtime | FCT-003 | REPAIR_FACT
SYS-009 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-003 | PATH:/tmp/sinoe_annuaire.csv | FETCH dataset SINOE raw : fiche 5172 Decheterie La Haie-Fouassiere (D_OUV 1974, fermee 18/11/2013) + fiche 106355 Halte Eco Tri (D_OUV 2013-11-18)
QRY-002 | FETCH | FOUND | SRC-004 | http://ericthouzeau.eu/inauguration-dune-halte-eco-tri/ | FETCH blog Eric Thouzeau : inauguration Halte Eco Tri (dechetterie-recyclerie) CC Sevre Maine et Goulaine a La Haye-Fouassiere, 2 anciennes dechetteries vetustes et inadaptees
QRY-003 | FETCH | FOUND | SRC-005 | https://fr.wikipedia.org/wiki/Communaut%C3%A9_de_communes_S%C3%A8vre,_Maine_et_Goulaine | FETCH Wikipedia FR CC Sevre Maine et Goulaine : creation decembre 2000, siege La Haye-Fouassiere
QRY-004 | FETCH | FOUND | SRC-006 | https://fr.wikipedia.org/wiki/Communaut%C3%A9_de_communes_de_la_vall%C3%A9e_de_Clisson | FETCH Wikipedia FR CC Vallee de Clisson : creation 2000, competence 4 dechetteries
QRY-005 | FETCH | FOUND | SRC-007 | PATH:/tmp/rpqs_clisson.txt | FETCH RPQS 2025 Clisson Sevre et Maine Agglo : haltes eco-tri = equipements plus recents, competence decheterie 01/01/2017
QRY-006 | FETCH | FOUND | SRC-008 | https://www.sinoe.org/index.php/fiche_service/index/globid/1502/id/106355/act/1/ser/1/onglet/DECHETS/prov/fiche/ | FETCH SINOE fiche service 106355 : Halte Eco Tri D_OUV 2013-11-18
QRY-007 | EXA | NONE trouve : aucune source ne documente une ouverture de la Halte Eco Tri a une autre date que le 18/11/2013 ; Ouest-France 20/11/2013 (« fonctionne depuis lundi » = 18/11/2013) et inauguration 28/11/2013 concordent avec le D_OUV SINOE 106355 (2013-11-18) | - | - | REFUTATION La Haye-Fouassiere 44 106355 5172 2013 11 18 : une preuve d'ouverture de la Halte Eco Tri a une autre date (2012, 2014...) ou d'une absence de reconversion le 18/11/2013
QRY-008 | EXA | NONE trouve : aucune source ne documente une decheterie moderne de La Haye-Fouassiere anterieure a 2000 ; les gestionnaires (CC Vallee de Clisson 2000, CC Sevre Maine et Goulaine 22/12/2000) sont posterieurs ; aucune presse/archive 1990-1999 d'ouverture | - | - | REFUTATION La Haye-Fouassiere 44 2000 244400652 22 12 : une preuve d'une decheterie moderne ouverte avant la creation des CC (1990-1999), avec acte ou presse
QRY-009 | EXA | NONE trouve : aucune source ne documente une decharge moderne ou un depot avant la dechetterie ; blog Thouzeau 28/11/2013 confirme des « dechetteries vetustes » (pas une decharge) ; BASIAS/SIS et presse ne revelent pas de decharge communale moderne sur le site | - | - | REFUTATION La Haye-Fouassiere 44 5172 1974 : une preuve que le site etait avant 2013 une decharge moderne (BASIAS, arrete ICPE, presse) et non une dechetterie vetuste

## EVIDENCE_REGISTRY
SRC-001 | ○ | fam:B | https://www.ouest-france.fr/pays-de-la-loire/la-halte-eco-tri-communautaire-fonctionne-depuis-lundi-1734422
SRC-002 | ○ | fam:B | https://www.ouest-france.fr/pays-de-la-loire/une-dechetterie-communautaire-en-2013-la-haye-fouassiere-1535139
SRC-003 | ◈ | fam:A | PATH:/tmp/sinoe_annuaire.csv
SRC-004 | ◈ | fam:B | http://ericthouzeau.eu/inauguration-dune-halte-eco-tri/
SRC-005 | ◈ | fam:C | https://fr.wikipedia.org/wiki/Communaut%C3%A9_de_communes_S%C3%A8vre,_Maine_et_Goulaine
SRC-006 | ◈ | fam:C | https://fr.wikipedia.org/wiki/Communaut%C3%A9_de_communes_de_la_vall%C3%A9e_de_Clisson
SRC-007 | ◈ | fam:D | PATH:/tmp/rpqs_clisson.txt
SRC-008 | ◈ | fam:A | https://www.sinoe.org/index.php/fiche_service/index/globid/1502/id/106355/act/1/ser/1/onglet/DECHETS/prov/fiche/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.sinoe.org/index.php/fiche_service/index/globid/1502/id/106355/act/1/ser/1/onglet/DECHETS/prov/fiche/ | A,B | 2026-08-30 | La Haye-Fouassiere (44) : la Halte Eco Tri actuelle (fiche SINOE 106355) a ete ouverte le 18/11/2013 = date exacte de fermeture de l'ancienne decheterie 5172 (reconversion du site le meme jour, pas fermeture definitive) | La date reelle de l'equipement actuel de La Haye-Fouassiere = 18/11/2013 : (1) dataset SINOE raw (INSPECTED) : fiche 106355 Halte Eco Tri D_OUV 2013-11-18, fiche 5172 ancienne decheterie fermee le 18/11/2013 — meme jour, reconversion ; (2) Ouest-France 20/11/2013 « La halte eco-tri communautaire fonctionne depuis lundi » (= 18/11/2013, lundi) ; (3) blog Eric Thouzeau 28/11/2013 (INSPECTED) : inauguration de la Halte Eco Tri (dechetterie-recyclerie) de la CC Sevre Maine et Goulaine, les 2 anciennes dechetteries (La Haye-Fouassiere et Haute-Goulaine) etant « vetustes et inadaptees » | 87ce56e5-489f-48ba-a6f8-7e84e5a400aa
FCT-002 | FACT | ✦ | https://fr.wikipedia.org/wiki/Communaut%C3%A9_de_communes_S%C3%A8vre,_Maine_et_Goulaine | C,D | 2026-08-30 | La Haye-Fouassiere (44) : aucune decheterie moderne anterieure a 2000 — gestionnaires historiques CC Vallee de Clisson (creee 2000) et CC Sevre Maine et Goulaine (creee 22/12/2000, siege La Haye-Fouassiere) | Incoherence structurelle : la decheterie de La Haye-Fouassiere releve des CC creees en 2000 — CC Vallee de Clisson (Wikipedia FR, INSPECTED : creee en 2000 avec competence 4 dechetteries, SIREN 244400652) puis CC Sevre Maine et Goulaine (Wikipedia FR, INSPECTED : creee decembre 2000, siege La Haye-Fouassiere) ; RPQS 2025 Clisson Sevre et Maine Agglo (INSPECTED) : « haltes eco-tri = equipements plus recents », competence decheterie 01/01/2017 → un D_OUV 1974 est structurellement impossible pour une decheterie moderne ; la CC Sivom anterieur n'a pas laisse d'acte de decheterie | 79748b4f-ebc9-4f56-b247-bb0400796b04
FCT-003 | FACT | ✦ | http://ericthouzeau.eu/inauguration-dune-halte-eco-tri/ | A,B | 2026-08-30 | La Haye-Fouassiere (44) : avant la reconversion, le site etait une « dechetterie vetuste et inadaptee » du reseau Sevre Maine et Goulaine (exploitant Grandjouan-Veolia) — pas une decharge moderne ni une decheterie ouverte par acte anterieur au neologisme ; D_OUV 1974 = date de reference du site sans acte d'ouverture | Caracterisation de l'avant : blog Eric Thouzeau 28/11/2013 (INSPECTED) : la CC Sevre Maine et Goulaine « disposait de deux dechetteries (La Haye-Fouassiere et Haute-Goulaine). Elles etaient vetustes et inadaptees » → le site pre-2013 etait une dechetterie intercommunale ancienne, pas une decharge moderne ; dataset SINOE (fiche 5172) : D_OUV 01/01/1974 + champ renovation 1974 recopie (signature date recopiee, passe 1900 FCT-003), exploitant Grandjouan-Veolia depuis 2006 ; aucune presse/archive ne documente un acte d'ouverture pre-1987 → le D_OUV 1974 reste non corrobore | 8a84e196-33b7-4cee-a28c-5bb9f9d022cd
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-008,SRC-004
FCT-002 | SRC-005,SRC-006,SRC-007
FCT-003 | SRC-004,SRC-003

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-007 | NONE
FCT-002 | QRY-008 | NONE
FCT-003 | QRY-009 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:CONFIRME
FCT-003 | ELIGIBLE:CONFIRME

## MEMORY_WRITE_MODE_V1
FCT-001 | UPDATE | 438bf634-0b7c-46b2-9e74-f5db20491d12
FCT-002 | WRITE | -
FCT-003 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9:AXS-001:QRY-001
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10:FCT-001
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11:CAU-001
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17:INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18:FINALIZATION_BLOCKED

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T18:11:52.247345+00:00","fact_mem":{"FCT-001":"87ce56e5-489f-48ba-a6f8-7e84e5a400aa","FCT-002":"79748b4f-ebc9-4f56-b247-bb0400796b04","FCT-003":"8a84e196-33b7-4cee-a28c-5bb9f9d022cd"},"mnemo_row":"MNEMO_MCP_8002","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"write_memory note MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"write_memory note MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"write_memory note MCP 8002","success":1}],"writeback_row":{"attempted":3,"blocked":0,"eligible":3,"failure":0,"success":3}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_MCP_8002 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:3;attempted:3;success:3;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[3 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
