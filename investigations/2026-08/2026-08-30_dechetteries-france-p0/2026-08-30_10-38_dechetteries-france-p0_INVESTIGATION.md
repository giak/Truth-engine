ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-1038-dechetteries-france-p0 | PARENT_RUN_ID:20260830-0957-dechetteries-france-chaine | AS_OF:2026-08-30
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france-p0/2026-08-30_10-38_dechetteries-france-p0_INPUT.txt | SUBJECT_SLUG:dechetteries-france-p0 | SUBJECT_FP:sha256:88e4c72d0605999b1c3f16114dee36ecfb32d2c3ca54deef35775a78931d17e5 | INPUT_SHA256:sha256:5e94c7c3eccbf1e6af523b915fd031dbef4324563bbe952dc386840186ee6e47
COMPLEXITY:8→COMPLEX | CHECKPOINT_SEQ:8 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'domains': ['archives', 'deliberations', 'reglementation'], 'geo': 'France, Bordeaux metropole', 'period': '1967-2026', 'question': 'Quelle est la genese et la construction du reseau des dechetteries en France ? (P0 : acte primaire deliberation CUB 1980 dechetterie Gradignan)'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# KERNEL investigation P0 — Lire l'acte primaire : la délibération CUB de 1980 (déchèterie de Gradignan)

RUN_ID : 20260830-1038-dechetteries-france-p0 · PARENT_RUN_ID : 20260830-0957-dechetteries-france-chaine
AS_OF : 2026-08-30 · INPUT_KIND : UPDATE · MISSION_MODE : INVESTIGATION · via KERNEL v2.10.6 (candidat R2A_BASELINE)

## Résumé

Cette passe lance la **priorité haute (P0)** du dossier : tenter de lire l'acte primaire d'ouverture de la déchèterie de Gradignan (délibération CUB de 1980) pour faire passer FCT du statut LOCALIZED à INSPECTED, et confirmer la cote exacte auprès des Archives.

## 1. Résultats obtenus

1. **La notice « Délibérations de 1980 » est confirmée INSPECTED** (FCT-001, ✧) : dans l'arbre du fonds **BXM 511 W** « Délibérations de la communauté urbaine de Bordeaux (1967-2003) », la notice **8586 = « Délibérations de 1980 »** (chemin `view:8586/n:411`), encadrée par 1979 (8580) et 1981 (8593). Source : capture Wayback du 16/01/2023 du fonds (le site live est bloqué par Anubis). C'est une **localisation précise et vérifiée** de l'acte, au niveau du registre annuel.

2. **Le registre PDF OCR de 1980 n'est pas lu** (LED-001, GAP ACCESS) : le live `view:8586` et la page délibérations v2ont bloqués par Anubis (HTTP 200 → page « Making sure you're not a bot ») ; aucune capture Wayback des pages de détail/registre ne subsiste (CDX vide) ; la cote/n° de délibération n'est pas corroborée par une source libre. L'acte **reste LOCALIZED** — la lecture du contenu requiert un accès interactif (navigateur) ou la salle de lecture, ou confirmation par courriel `archives@bordeaux-metropole.fr`.

3. **Corroboration officielle renforcée** (FCT-002, ✧) : une **seconde occurrence officielle** désormais inspectée (actualité de l'exposition des Archives BM, capture Wayback 18/09/2025) : « création de la première déchetterie en France ouverte à Gradignan le **17 novembre 1980**, adoption en 1993 du plan TRIVAC ». Cela renforce l'affirmation du panneau (même institution, support distinct), sans constituer une corroboration indépendante (LED-002, GAP INDEPENDENCE).

## 2. Verdict épistémique

- **Acte primaire** : LOCALIZED (FCT-001 ✧), non INSPECTED — le chemin exact est établi, le contenu non vérifié. Aucune contradiction matérielle ; limite d'accès technique (Anubis) documentée, pas une dissimulation.
- **Revendication 17/11/1980** : corroborée intra-famille (2 supports officiels inspectés), corroboration indépendante toujours GAP.
- **Chaîne causale** délibération → ouverture non vérifiée étape par étape (GAP CAUSALITY, CAU-001) tant que le registre n'est pas lu.

## 3. Limites

Lecture du registre requiert accès interactif ou salle de lecture ; RetroNews/Sud Ouest payants pour la presse 1980-85 ; aucune capture Wayback des pages de détail.

## 4. Traçabilité

2 sources officielles inspectées (famille A : panneau d'exposition référencé SRC-001 et actualité SRC-002), 2 faits ✧ (FCT-001 localisation notice 8586, FCT-002 2e occurrence officielle), 2 LED (LED-001 GAP ACCESS, LED-002 GAP INDEPENDENCE), 3 AXS (AXS-001/002 GAP typés, AXS-003 N/A), 2 CLM, 1 CAU (GAP CAUSALITY), 1 réfutation exécutée (NONE), 1 barrière technique Anubis documentée. 8 checkpoints PASS. Sections complètes.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:2|CLM:2|AXS:3|CAU:1|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_excerpt":"FCT-001 (notice 8586 INSPECTED) ; QRY-001/002 FAILED Anubis ; QRY-006 NO_RESULT presse libre","gap":"Notice 8586 = « Délibérations de 1980 » confirmée dans l'arbre du fonds (INSPECTED via Wayback 2023-01-16) ; mais le registre PDF OCR lui-même est inaccessible : live bloqué par Anubis (HTTP 200->page anti-bot), aucune capture Wayback des pages view:8586/registre ; lecture requiert accès interactif navigateur ou salle de lecture, ou confirmation de la cote par courriel archives@bordeaux-metropole.fr","gap_type":"ACCESS","kind":"LED","lead":"Lire le registre OCR « Délibérations de 1980 » (BXM 511 W, notice 8586) — faire passer l'acte d'ouverture de LOCALIZED à INSPECTED","linked_ids":["AXS-001","CLM-001"],"locator":"fonds BXM 511 W / notice 8586 / view:8586/n:411","materiality":"DECISIVE","routes":["EXPAND"],"source_id":"SRC-001","status":"GAP"}
LED-002 | {"evidence_excerpt":"FCT-002 (2e occurrence officielle) ; QRY-005/006 WEB","gap":"Deux occurrences officielles désormais INSPECTED (panneau + actualité d'exposition, Archives BM même institution) mais toujours une seule famille de provenance ; corroboration indépendante datée (presse) absente des corpus libres ; RetroNews/Sud Ouest payants","gap_type":"INDEPENDENCE","kind":"LED","lead":"Corroborer l'affirmation « première déchetterie de France à Gradignan 17/11/1980 » hors famille officielle (presse/récit indépendant)","linked_ids":["AXS-001","CLM-001"],"locator":"presse 1980-85 (Sud Ouest, RetroNews, Gallica OCR)","materiality":"DECISIVE","routes":["EXPAND"],"source_id":"-","status":"GAP"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"L'acte d'ouverture de la déchèterie de Gradignan est une délibération du conseil de la CUB de 1980, localisée dans le fonds BXM 511 W (notice « Délibérations de 1980 », view:8586, registres PDF OCR en ligne, tables BXM 27 W) mais non encore inspectée : le registre OCR est inaccessible en automatique (Anubis) et la cote de la délibération n'est pas corroborée par une source indépendante.","claimant":"Archives de Bordeaux Métropole (inventaire fonds BXM 511 W)","counter":"NONE_FOUND (registre non lu : contenu non vérifié)","gap":"Registre PDF OCR non inspecté ; cote/n  de délibération non corroborée indépendamment","gap_type":"ACCESS","materiality":"DECISIVE","status":"GAP","support":"FCT-001"}
CLM-002 | {"claim":"Deux documents officiels distincts des Archives de Bordeaux Métropole (panneau d'exposition + actualité d'exposition, INSPECTED via Wayback) affirment textuellement « création de la première déchetterie en France ouverte à Gradignan le 17 novembre 1980 » ; il s'agit de la même famille de provenance (institution dépositaire).","claimant":"Archives de Bordeaux Métropole","counter":"NONE_FOUND_indep (corroboration indépendante datée absente)","gap":"Deux supports, une seule famille ; corroboration indépendante (presse 1980-85) non établie dans les corpus libres","gap_type":"INDEPENDENCE","materiality":"DECISIVE","status":"SATURATED","support":"FCT-002"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-006"],"axis":"EVIDENCE_CASES","gap":"Notice 8586 confirmée dans l'arbre (INSPECTED) mais registre PDF OCR non lu : Anubis bloque le live, aucune capture Wayback des pages de détail/registre, cote de délibération non corroborée par presse libre ; lecture requiert accès interactif ou salle de lecture","gap_type":"ACCESS","led_clm_links":["LED-001","CLM-001"],"question":"Peut-on lire la délibération CUB de 1980 (registre OCR BXM 511 W, notice 8586) pour passer l'acte d'ouverture de la déchèterie de Gradignan de LOCALIZED à INSPECTED ?","result_ids":["FCT-001"],"sought_objects":"registre PDF OCR « Délibérations de 1980 » (notice view:8586), contenu de la délibération","status":"GAP"}
AXS-002 | {"attempt_ids":["QRY-004","QRY-005","QRY-006"],"axis":"COUNTER_HYPOTHESES","gap":"Deux occurrences officielles (panneau + actualité, même institution) INSPECTED ; aucune corroboration indépendante (presse libre) trouvée ; RetroNews/Sud Ouest payants","gap_type":"INDEPENDENCE","led_clm_links":["LED-002","CLM-001"],"question":"La revendication « première déchetterie de France à Gradignan 17/11/1980 » est-elle corroborée hors source officielle ?","result_ids":["FCT-002"],"sought_objects":"seconde provenance indépendante datée (presse 1980-85)","status":"GAP"}
AXS-003 | {"attempt_ids":[],"axis":"SOURCE_AUDIT","gap":"N/A(NO_INPUT_SOURCE) : input UPDATE sans source materielle","gap_type":"NONE","led_clm_links":[],"question":"Audit de la source fournie (lead)","result_ids":[],"sought_objects":"sans objet","status":"N/A"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"le contenu de la délibération n'est pas lu : la décision précise (objet exact, montant, localisation) n'est pas vérifiée étape par étape ; seule l'existence d'un registre 1980 et la revendication officielle sont documentées","from":"décision réglementaire de la CUB (fin 1980) d'ouvrir un dépôt dédié aux encombrants/apport volontaire","gap":"chaîne délibération -> décision -> ouverture non vérifiée faute d'accès au registre OCR ; enabler officiel documenté, cause unique non prouvée","gap_type":"CAUSALITY","link_type":"MECHANISM","mechanism":"la délibération du conseil de communauté (fonds BXM 511 W) matérialise la décision d'ouverture du premier site fixe d'apport volontaire de la CUB","source":"FCT-001 (notice 8586 localisée) ; FCT-002 (occurrence 17/11/1980)","status":"GAP","to":"existence de la déchèterie de Gradignan (17/11/1980, revendiquée « première de France »)"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:3|FETCH:4|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FOUND | mnemolite | memories:29ed45bc,98c854f2,8dbe8b46 | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FAILED:ANUBIS_BOT | - | https://archives.bordeaux-metropole.fr/archive/fonds/FR-ABM243300316_BXM_0511_W/n:411 | FETCH live fonds BXM 511 W deliberations CUB (bloque par anti-bot Anubis)
QRY-002 | FETCH | FAILED:ANUBIS_BOT | - | https://archives.bordeaux-metropole.fr/n/deliberations/n:417 | FETCH live page deliberations CUB (bloque par anti-bot Anubis)
QRY-003 | FETCH | FOUND | SRC-001 | http://web.archive.org/web/20230116100622/https://archives.bordeaux-metropole.fr/archive/fonds/FR-ABM243300316_BXM_0511_W/n:411 | FETCH wayback fonds BXM 511 W 2023-01-16 - confirmation notice 8586 = Deliberations de 1980 dans l'arbre
QRY-004 | FETCH | FOUND | SRC-002 | http://web.archive.org/web/20250918100221/https://archives.bordeaux-metropole.fr/actualites/rendez-vous-1/le-fabuleux-destin-des-dechets-menagers-une-epopee-metropolitaine-xive-xxie-siecle-338/n:44 | FETCH wayback page actualite exposition Archives BM 2025-09-18 - confirmation texte premiere dechetterie Gradignan 17/11/1980
QRY-005 | WEB | FOUND | - | - | WEB Gradignan dechetterie 1980 CUB commune aute Bordeaux premieres deliberation ouvertures encombrants registres 1980 1981
QRY-006 | WEB | NO_RESULT:presse-libre | - | - | WEB recherche cote/numero deliberation CUB 1980 Gradignan dechetterie - aucune source independante de la cote
QRY-007 | WEB | FOUND | - | - | REFUTATION: test relocalisation du registre 1980 BXM 511 W — recherche d'une capture Wayback view 8586 / PDF OCR et d'une cote de deliberation contradictoire : aucune capture des pages de detail, aucun document contradictoire identifie ; la notice 8586 = Deliberations de 1980 reste localisee mais non lue (Anubis)

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | http://web.archive.org/web/20230116100622/https://archives.bordeaux-metropole.fr/archive/fonds/FR-ABM243300316_BXM_0511_W/n:411
SRC-002 | ◈ | fam:A | http://web.archive.org/web/20250918100221/https://archives.bordeaux-metropole.fr/actualites/rendez-vous-1/le-fabuleux-destin-des-dechets-menagers-une-epopee-metropolitaine-xive-xxie-siecle-338/n:44

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | http://web.archive.org/web/20230116100622/https://archives.bordeaux-metropole.fr/archive/fonds/FR-ABM243300316_BXM_0511_W/n:411 | A | 1980 | notice-8586-deliberations-1980-bxm-511-w-confirmee | Confirmation INSPECTED : dans l'arbre du fonds BXM 511 W (adélibérations CUB 1967-2003), la notice 8586 = « Délibérations de 1980 », encadrée par 1979 (8580) et 1981 (8593) ; chemin view:8586/n:411. Le registre PDF OCR de 1980 contenant la délibération d'ouverture de la déchèterie de Gradignan est localisé mais non lu (Anubis). | 29ed45bc-0e9a-4ece-b772-f4e7055df594
FCT-002 | FACT | ✧ | http://web.archive.org/web/20250918100221/https://archives.bordeaux-metropole.fr/actualites/rendez-vous-1/le-fabuleux-destin-des-dechets-menagers-une-epopee-metropolitaine-xive-xxie-siecle-338/n:44 | A | 1980-11-17 | 1ere-dechetterie-gradignan-17-11-1980-2e-occurrence-officielle | Seconde occurrence officielle (INSPECTED via Wayback 2025-09-18) : actualite de l'exposition des Archives BM - « création de la première déchetterie en France ouverte à Gradignan le 17 novembre 1980, adoption en 1993 du plan TRIVAC » ; corroboration intra-institutionnelle du panneau (même institution, support distinct) | 8dbe8b46-fac3-49f6-8aa3-0ee07659ef06
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-007 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | UPDATE | 29ed45bc-0e9a-4ece-b772-f4e7055df594
FCT-002 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18
CP-008 | CORRECTION | PASS | LAST_COMPLETED:18b | NEXT_ACTION:NONE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T08:40:01.794913+00:00","fact_mem":{"FCT-001":"29ed45bc-0e9a-4ece-b772-f4e7055df594","FCT-002":"8dbe8b46-fac3-49f6-8aa3-0ee07659ef06"},"mnemo_row":"18f86cf5-334c-4cb2-b411-dbb44ced225e","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1}],"writeback_row":{"attempted":2,"blocked":0,"eligible":2,"failure":0,"success":2}}

PERSISTENCE_META: MNEMO_ROW:18f86cf5-334c-4cb2-b411-dbb44ced225e | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:2;attempted:2;success:2;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[2 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
