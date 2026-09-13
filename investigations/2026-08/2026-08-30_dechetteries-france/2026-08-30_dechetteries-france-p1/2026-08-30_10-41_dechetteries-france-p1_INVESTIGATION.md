ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-1041-dechetteries-france-p1 | PARENT_RUN_ID:20260830-0957-dechetteries-france-chaine | AS_OF:2026-08-30
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_dechetteries-france-p1/2026-08-30_10-41_dechetteries-france-p1_INPUT.txt | SUBJECT_SLUG:dechetteries-france-p1 | SUBJECT_FP:sha256:56ce475df48dcc868d618e98225739ce3048e15ae02390ebe809b9104f76eb8c | INPUT_SHA256:sha256:da8de8c2f52f1cd5eb3bd95942e1513386e79db7629df99cb107321c02c259fc
COMPLEXITY:8→COMPLEX | CHECKPOINT_SEQ:8 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'domains': ['presse', 'archives', 'histoire des dechets'], 'geo': 'France (Gironde, Bordeaux metropole + presse nationale)', 'period': '1979-1985', 'question': 'Quelle est la genese et la construction du reseau des dechetteries en France ? (P1 : corroboration presse independante Gradignan 17/11/1980)'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# P1 — Corroboration presse indépendante (Sud Ouest / RetroNews 1979-1981)

## Objet
Trouver une corroboration par la **presse quotidienne datée 1979-1985** de la revendication « première déchetterie de France à Gradignan, ouverte le 17/11/1980 », afin de rendre cette assertion indépendante de la seule famille officielle (Archives Bordeaux Métropole).

## Contexte du run
Suite du dossier `dechetteries-france` : la passe chaîne (20260830-0957) et la passe P0 (20260830-1038, lecture acte primaire) ont établi que l'acte reste **LOCALIZED** et que la corroboration presse indépendante datée 1980 était un **GAP INDEPENDENCE**. Le run P1 attaque ce gap.

## Recherches exécutées (résumé réel)
- **Gallica SRU** : recherche `dechetterie` → **258 records** (corpus global). Le **TSM** (Techniques Sciences Méthodes, revue AGHTM) ressort avec `dechetterie` + `Gradignan`.
- **Fascicule TSM septembre 1986** (ARK `bpt6k9608124h`, notice datée 1986-09-01) : ContentSearch page **395 → « Déchetterie de Gradignan »**, mention de la **Communauté Urbaine de Bordeaux**, photo légendée « Doc. ANRED ».
- **RetroNews (BnF)** : site accessible (200) mais **API 401** (clé/SPA payante) ; couverture éditoriale **~1631-1945/1951** (droit d'auteur) → **la presse de 1980 n'est PAS disponible** sur ce corpus.
- **Sud Ouest archives** : page 200 (portail payant), contenus derrière abonnement, non indexables librement.
- Conclusion d'accès : la presse quotidienne de 1980 est **structurellement inaccessible en corpus libre** (right of auteur), ce n'est pas un simple paywall contournable.

## Faits
- **FCT-001 · ✧ (famille B — presse technique)** : TSM/AGHTM septembre 1986, p.395 « Déchetterie de Gradignan » (+ C.U. Bordeaux, photo ANRED). Confirme **l'existence réelle du site** de Gradignan et sa notoriété professionnelle en 1986, comme équipement référencé — **famille indépendante des Archives BM**.

## Verdict / status
- **Existence réelle du site de Gradignan** : **renforcée** (FCT-001 ✧, seconde famille indépendante).
- **Portée « première de France, 17/11/1980 »** : **non indépendante en corpus libre** ; la corroboration presse quotidienne datée 1980 reste un **GAP INDEPENDENCE structurel** (retroNews ~1950, Sud Ouest payant).
- **CAU-001** : la barrière est structurelle (droit d'auteur → numérisation ~1950 → presse 1980 sous paywall), documentée, non contournable par web libre.

## Gaps restants
- Corroboration presse quotidienne datée 1979-1981 → requiert **accès payant** (Sud Ouest archives) ou **consultation en salle de lecture**.
- Contenu OCR plein texte de la page 395 du TSM (citation exacte) — endpoint OCR non résolu.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:2|CLM:2|AXS:3|CAU:1|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_excerpt":"FCT-001 (TSM 1986) ; QRY-004/005/006 (accès presse)","gap":"Presse quotidienne de 1980 inaccessible en corpus libre : RetroNews (BnF) s'arrête à ~1945/1951 (droit d'auteur, BA n'existe pas pour 1980), API RetroNews 401 (payante), archives Sud Ouest derrière abonnement (page 200, contenus non indexables librement), Le Monde etc. pas libres après 1944 sur Gallica ; seule corroboration technique indépendante obtenue : TSM septembre 1986 (déchetterie de Gradignan, CUB Bordeaux)","gap_type":"INDEPENDENCE","kind":"LED","lead":"Corroboration presse quotidienne indépendante de la revendication « première déchetterie de France à Gradignan 17/11/1980 » (1979-1985)","linked_ids":["AXS-001","CLM-001"],"locator":"Sud Ouest archives, RetroNews BnF, presse nationale 1980","materiality":"DECISIVE","routes":["EXPAND"],"source_id":"-","status":"GAP"}
LED-002 | {"evidence_excerpt":"FCT-001 (TSM septembre 1986, p.395 « Déchetterie de Gradignan » + C.U. Bordeaux, photo ANRED) : existence réelle et notoriété professionnelle du site établies hors famille Archives BM","gap_type":"-","kind":"LED","lead":"Vérifier que l'existence réelle de la déchèterie de Gradignan (site) a une trace technique/presse indépendante de la famille Archives BM","linked_ids":["AXS-001","CLM-001"],"locator":"TSM 1986-09 (AGHTM), Gallica","materiality":"IMPORTANT","routes":["EXPAND"],"source_id":"SRC-001","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"La revendication « première déchetterie de France à Gradignan, ouverte le 17/11/1980 » reste fondée sur des documents officiels des Archives BM (2 supports inspectés) ; la corroboration indépendante par la presse quotidienne datée de 1980 n'est pas établie (barrière structurelle RetroNews ~1950 + Sud Ouest payant).","claimant":"convergence Archives BM + recherche presse","counter":"NONE_FOUND (presse 1980 inaccessible en corpus libre)","gap":"corroboration presse quotidienne datée 1980 absente : RetroNews s'arrête ~1945/1951, Sud Ouest payant, API 401","gap_type":"INDEPENDENCE","materiality":"DECISIVE","status":"SATURATED","support":"FCT-001 (site réel TSM 1986)"}
CLM-002 | {"claim":"L'existence réelle et la notoriété professionnelle du site de Gradignan (déchèterie de la C.U. de Bordeaux) sont confirmées par une famille technique indépendante : TSM (AGHTM) septembre 1986, page 395.","claimant":"TSM/AGHTM (gallica)","counter":"NONE_FOUND (pas de contradiction)","gap":"-","gap_type":"NONE","materiality":"IMPORTANT","status":"SATURATED","support":"FCT-001"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-006"],"axis":"COUNTER_HYPOTHESES","gap":"Aucun document de presse daté de 1979-1985 observé : RetroNews s'arrête ~1945/1951, API RetroNews 401, Sud Ouest payant ; seule trace indépendante trouvée : TSM septembre 1986 (famille presse technique AGHTM) confirmant l'existence du site, pas la date du 17/11/1980","gap_type":"INDEPENDENCE","led_clm_links":["LED-001","CLM-001"],"question":"Existe-t-il une annonce/appel d'ouverture de la déchèterie de Gradignan datée de novembre 1980 dans la presse (corroboration indépendante) ?","result_ids":["FCT-001"],"sought_objects":"presse quotidienne Gironde 1980 (Sud Ouest, presse régionale), presse nationale, presse professionnelle 1980-85","status":"GAP"}
AXS-002 | {"attempt_ids":["QRY-002","QRY-003"],"axis":"EVIDENCE_CASES","gap_type":"-","led_clm_links":["LED-002","CLM-001"],"question":"L'existence réelle de la déchèterie de Gradignan et de la CUB est-elle confirmée hors famille Archives BM ?","result_ids":["FCT-001"],"sought_objects":"revue professionnelle/dossier technique mentionnant le site de Gradignan","status":"SATURATED"}
AXS-003 | {"attempt_ids":[],"axis":"SOURCE_AUDIT","gap":"N/A(NO_INPUT_SOURCE) : input UPDATE sans source matérielle","gap_type":"NONE","led_clm_links":[],"question":"Audit de la source fournie (lead)","result_ids":[],"sought_objects":"sans objet","status":"N/A"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal":"La mise à disposition libre/numérique de la presse quotidienne française de 1980 étant structurellement bloquée par le droit d'auteur (RetroNews BnF s'arrête ~1945/1951, API 401, Sud Ouest payant, presse nationale post-1944 non libre sur Gallica), la corroboration indépendante datée du 17/11/1980 par la presse quotidienne ne peut pas être établie avec les corpus accessibles.","counter":"NONE_FOUND","gap":"GAP structurel : accès payé requis (Sud Ouest archives, archives départementales papier) ; documenté, non contournable par web libre.","gap_type":"INDEPENDENCE","linked_ids":["LED-001","AXS-001","CLM-001"],"mechanism":"Contrainte légale (droit d'auteur) → numérisation limitée (~1950) → presse 1979-1981 sous paywall → absence de corpus libre exploitable → GAP INDEPENDENCE structurel, non résoluble par recherche automatisée.","status":"SATURATED","support":"QRY-005 (RetroNews 401), QRY-006 (Sud Ouest payant), recherche BnF couverture ~1945/1951"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:1|FETCH:5|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FOUND | mnemolite | memories:8dbe8b46,29ed45bc,98c854f2,18f86cf5 | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | FCT-001 | REPAIR_FACT
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | - | https://gallica.bnf.fr/SRU?query=gallica%20all%20%22dechetterie%22%20and%20gallica%20all%20%22Gradignan%22 | FETCH gallica SRU dechetterie+Gradignan - corpus 258 records, TSM 1986-09 ressort
QRY-002 | FETCH | FOUND | - | https://gallica.bnf.fr/services/ContentSearch?ark=ark:/12148/bpt6k9608124h&query=dechetterie | FETCH gallica ContentSearch TSM 1986-09 dechetterie - page 383 dossier dechetteries, anred brochure nov 1985 citée
QRY-003 | FETCH | FOUND | SRC-001 | https://gallica.bnf.fr/services/ContentSearch?ark=ark:/12148/bpt6k9608124h&query=Gradignan | FETCH gallica ContentSearch TSM 1986-09 Gradignan - page 395 'Dechetterie de Gradignan' + CUB Bordeaux (Doc ANRED)
QRY-004 | FETCH | FAILED:API_401 | - | https://api.retronews.fr/v1/search?query=Gradignan&year=1980 | FETCH RetroNews API v1 search Gradignan 1980 - 401 key required (plateforme payante)
QRY-005 | FETCH | FAILED:PAYWALL | - | https://www.sudouest.fr/archives/ | FETCH Sud Ouest archives - contenus derriere abonnement (page 200 portail payant)
QRY-006 | WEB | NO_RESULT:presse-1980 | - | - | WEB presse quotidienne 1980 Gironde/Sud Ouest annonce ouverture dechetterie Gradignan - aucune source libre; RetroNews couvre jusqu'aux annees ~1950 (droit d'auteur)

## EVIDENCE_REGISTRY
SRC-001 | ◉ | fam:B | https://gallica.bnf.fr/services/ContentSearch?ark=ark:/12148/bpt6k9608124h&query=Gradignan

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://gallica.bnf.fr/services/ContentSearch?ark=ark:/12148/bpt6k9608124h&query=Gradignan | B | 1986-09-01 | dechetterie-gradignan-cub-bordeaux-tsm-1986 | Revue technique TSM (AGHTM), septembre 1986, dossier « Les déchetteries » : page 395 « Déchetterie de Gradignan » (photo légendée « Doc. ANRED ») et mentions de la Communauté Urbaine de Bordeaux ; confirme l'existence réelle du site de Gradignan et sa notoriété professionnelle en 1986, comme équipement de référence (corroboration famille presse technique, indépendante des Archives BM) | 856ea1f9-f5e6-43ae-9b90-ed22d590be32
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001

## REFUTATION_REGISTRY_V1

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | UPDATE | 856ea1f9-f5e6-43ae-9b90-ed22d590be32

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:recherche presse dechetterie renvoyee aux leads | NEXT_ACTION:checkpoints P1
CP-002 | SCOPE | PASS | LAST_COMPLETED:perimetre P1 presse 1979-1981 fige | NEXT_ACTION:checkpoints P1
CP-003 | SEARCH | PASS | LAST_COMPLETED:recherche presse reelle executee (Gallica/RetroNews/SudOuest) | NEXT_ACTION:checkpoints P1
CP-004 | FACTS | PASS | LAST_COMPLETED:fait TSM 1986 compile | NEXT_ACTION:checkpoints P1
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:gap structurel presse documente | NEXT_ACTION:checkpoints P1
CP-006 | VERIFY | PASS | LAST_COMPLETED:sources auditees, citation TSM confirmee | NEXT_ACTION:checkpoints P1
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:requetes et probes traces | NEXT_ACTION:checkpoints P1
CP-008 | CORRECTION | PASS | LAST_COMPLETED:aucune correction requise | NEXT_ACTION:checkpoints P1

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T08:49:31.688111+00:00","fact_mem":{"FCT-001":"856ea1f9-f5e6-43ae-9b90-ed22d590be32"},"mnemo_row":"7e1794b8-bdc2-41b3-8d72-bf128e2014a1","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"write_memory OK 856ea1f9 (TSM 1986) status VERIFIE","success":1}],"writeback_row":{"attempted":1,"blocked":0,"eligible":1,"failure":0,"success":1}}

PERSISTENCE_META: MNEMO_ROW:7e1794b8-bdc2-41b3-8d72-bf128e2014a1 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:1;attempted:1;success:1;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[1 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory OK 856ea1f9 (TSM 1986) status VERIFIE
