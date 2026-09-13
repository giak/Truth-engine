ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260831-1012-audit-rpqs-epci-quotas | PARENT_RUN_ID:NONE | AS_OF:2026-08-31
INPUT_KIND:NEW | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-31_audit-rpqs-epci-quotas/2026-08-31_10-12_audit-rpqs-epci-quotas_INPUT.txt | SUBJECT_SLUG:audit-rpqs-epci-quotas | SUBJECT_FP:sha256:45a6682dc76bb9c42959eed6352cbfcd654d3893bbf509eeeffb9d60de7ac74a | INPUT_SHA256:sha256:4c0cd26c1770b0af65a7bb3ac9f91d1b1c6aff18142a763410dc12089974044a
COMPLEXITY:0.6→MEDIUM | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors': ['Cyclad', 'Pays sabolien', 'Grand Avignon'], 'domains': ['dechets', 'decheterie', 'quotas', 'flux'], 'geo': 'France (17, Sarthe, Vaucluse/Gard)', 'lead_question': 'Structure des flux avant quota des 3 EPCI a passages + fenetre avant/apres', 'limits': 'quotas Cyclad/Grand Avignon actifs seulement en 2026', 'object_question': '(1) flux avant; (2) quota 24/18/18; (3) fenetre avant/apres'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# 🦊 RPQS 2024 de Cyclad, Pays sabolien, Grand Avignon : ligne de base des flux avant le quota

**Run `20260831-1012-audit-rpqs-epci-quotas`** — audit des documents publics (RPQS, chiffres clés, rapports) des 3 EPCI à quota de passages, pour établir la structure de leurs flux avant la mise en place du contrôle d'accès et tester s'il existe une fenêtre avant/après isolée. Comble partiellement le GAP de la passe 1002.

## Ce que l'audit établit

### 1. Les trois quotas et leur nature (FCT-001, FCT-002, FCT-005)

Les 3 EPCI ont tous un **quota générique de passages**, sans distinction fine de flux :
- **Pays sabolien** : 18 passages/an depuis 01/01/2025, badge, particuliers uniquement (pros → SOSAREC) ; facturation appliquée en 2026 : **5 €/passage (seuil 19-24), 50 €/passage (> 25)** ; moyenne réelle 2024 = **10 passages/an/foyer** → seuil à ~2× la moyenne, ne touchant que les gros apporteurs.
- **Cyclad** : Pass QR/badge, **24 passages** décomptés depuis 01/01/2026, 2 m³/passage.
- **Grand Avignon** : carte, **18 passages**, en vigueur 02/2026.

Découverte notable : au **Pays sabolien, le quota est encastré dans une redevance incitative (REOMi) en place depuis 2013** (comptage des levées du bac O m par puce). Le compteur O m existe donc sur ce territoire depuis douze ans ; le quota déchèterie (18 passages) l'étend au guichet de la déchèterie en 2025. C'est un cas de verrou double : le compteur O m devance le compteur déchèterie.

### 2. Les structures de flux « avant » sont établies et hétérogènes (FCT-003, FCT-006, FCT-007)

- **Grand Avignon** (rapport annuel 2022 INSPECTÉ, + SDD 2023 : gravats 29 %, verts 24,8 %) : gravats **26 %**, végétaux **23 %**, tout-venant **17 %**, DEA 11 %, bois 8 %, encombrants incinérables 7 %. Profil urbain/périurbain : gravats + végétaux = ~49 %.
- **Cyclad** (chiffres clés 2022 INSPECTÉ) : gravats **28 %**, végétaux **24 %**, déchèteries = **57 %** (53 % en 2025) des déchets du territoire, 75 % des matériaux valorisés.

**Les deux structures diffèrent** (même si gravats/végétaux dominent partout). Un quota générique de passages frappe donc en premier le flux le plus FRÉQUENT de chaque territoire, pas le même partout — confirmation, avec données EPCI, de la passe 1002 (le quota passages touche le tout-venant).

### 3. La baisse PRÉCÈDE le quota : le confondant confirmé (FCT-004)

**Grand Avignon : les apports de déchèterie (site Novalie) baissent de -6 % en 2024, première baisse depuis 2020, AVANT toute mise en place du quota de 18 passages (02/2026).** Cette donnée EPCI confirme ce que la passe 1002 inférait à l'échelle nationale (Loire Forez -13 % encombrants sans quota) : les tonnages peuvent baisser sans quota. Le -24 % médian du DT138 n'est donc pas entièrement attribuable au contrôle d'accès.

### 4. Le GAP, précision

La fenêtre « après » **n'est pas encore ouverte** : les quotas de Cyclad et du Grand Avignon ne produiront des chiffres annuels qu'en 2026-2027 ; le bilan 2025 du Pays sabolien (post-quota) n'a pas été trouvé publié. Le seul cas pré/post isolé reste **Point Fort (Manche)** (passes 0942/1002 : encombrants -34,7 %). Vérifié : les RPQS ne publient pas de ventilation flux avant/après sur un même EPCI, sauf circonstance exceptionnelle.

## GAPs restants

- Ventilation par flux avant/après sur un même EPCI : seul Point Fort exploitable ; à suivre pour Cyclad/Grand Avignon (RPQS 2026) et Pays sabolien (RPQS 2025).
- Pas de série longue par flux par EPCI.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:1|CLM:3|AXS:2|CAU:2|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_key":"structures flux avant (Grand Avignon gravats 26%/vegetaux 23%, Cyclad gravats 28%/vegetaux 24%) + quota passages (24/18/18)","note":"l'effet apres n'est pas encore publie (quotas 2026)","routes":["RPQS EPCI","chiffres cles","presse locale"],"status":"SATURATED","title":"Bases avant quota et fenetre apres : auditer les RPQS de Cyclad, Pays sabolien, Grand Avignon"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"La base 'avant' des 3 EPCI à quota est etablie et heterogene (Grand Avignon gravats 26-29%/vegetaux 23-25%, Cyclad gravats 28%/vegetaux 24%) : un quota passage generique (18-24/an) frappe en priorite le flux le plus frequent de chaque territoire, pas le meme partout","counter":"Les structures sont des photos a des annees differentes (2022/2023) et les typologies (urbain vs rural) varient","gap":"Pas de ventilation avant/après flux sur le meme EPCI isolee","gap_type":"COVERAGE_DATA_ABSENT","status":"SUPPORTED","support":["FCT-003","FCT-006","FCT-007"]}
CLM-002 | {"claim":"La baisse des tonnages PRECEDE le quota : Grand Avignon -6% d'apports decheterie en 2024 (1er baisse depuis 2020) AVANT le quota de 18 passages - le confondant de la passe 1002 est confirme par donnee EPCI","counter":"-6% est une seule annee sur un site (Novalie), d'autres facteurs (conjoncture, immobilier) peuvent peser","gap":"Pas de serie longue par flux sur meme EPCI","gap_type":"COVERAGE_DATA_ABSENT","status":"SUPPORTED","support":["FCT-004"]}
CLM-003 | {"claim":"Le quota du Pays sabolien (18 passages) est encastre dans une REOMi depuis 2013 (comptage leves bac OM) : la facturation au-delà (5/50 EUR) ne visait que les gros apporteurs (moyenne reelle 10 passages/foyer/an) - le verrou est double : compteur OM deja la depuis 12 ans, compteur decheterie ajoute en 2025","counter":"La REOMi date de 2013 mais le quota decheterie (18 passages) ne date que de 2025 : le nouveau verrou est distinct","gap":"NONE","gap_type":"NONE","status":"SUPPORTED","support":["FCT-001","FCT-002"]}

### AXIS_REGISTRY_V1
AXS-001 | {"question":"Quelle est la structure des flux (encombrants/verts/gravats) avant quota des 3 EPCI a passages (Cyclad, Pays sabolien, Grand Avignon) ?","routes":["AUDIT","EXPAND"],"sought_objects":["structures flux avant","gravats vegetaux tout-venant","RPQS 2022 2024"],"status":"SATURATED"}
AXS-002 | {"question":"Y a-t-il une fenetre avant/après quota isolée et un effet publié ?","routes":["AUDIT","EXPAND"],"sought_objects":["apports avant abaissement","Grand Avignon -6% 2024","Pays sabolien 2025"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Quota generique de passages (18-24/an dans les 3 EPCI) sans distinction de flux","effect":"Frappe en premier le flux le plus frequent du territoire : a Grand Avignon comme a Cyclad, le tout-venant (flux des petits apports) est le plus expose, gravats/vegetaux via volume","mechanism":"L'unite de compte (passage) penalise la frequence ; la moyenne reelle (10/foyer) fixe le seuil a ~2x, n'excluant que les gros apporteurs","status":"SUPPORTED","support":["FCT-001","FCT-003","FCT-007"]}
CAU-002 | {"cause":"Conjoncture/meteo/perimetre (pas le quota, inexistant en 2024)","effect":"Apports decheterie -6% au Grand Avignon en 2024, 1er baisse depuis 2020","mechanism":"La baisse des tonnages a des causes non-quota ; isoter l'effet quota exige de neutraliser cette derive naturelle (encore non publiee post-quota)","status":"SUPPORTED","support":["FCT-004"]}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:3|FETCH:6|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND | runtime | warm-route-1ca3694a-dt138-1002-quotas | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | OK | - | - | Cyclad Charente-Maritime rapport annuel RPQS 2024 decheteries tonnages encombrants gravats verts
QRY-002 | WEB | OK | - | - | Pays Sabolien RPQS 2024 dechets decheteries quota 18 passages
QRY-003 | WEB | OK | - | - | Grand Avignon RPQS 2024 dechets decheteries tonnages encombrants dechets verts gravats
QRY-004 | FETCH | INSPECTED | SRC-001 | https://cyclad.org/actualites/les-chiffres-cles-2025/ | Cyclad chiffres cles 2025 22 decheteries 53% 75% valorisation
QRY-005 | FETCH | INSPECTED | SRC-002 | https://cyclad.org/app/uploads/2023/09/CHIFFRES-CLES-2022-WEB.pdf | Cyclad chiffres cles 2022 gravats 28% vegetaux 24% decheteries 57%
QRY-006 | FETCH | INSPECTED | SRC-003 | https://www.payssabolien.fr/le-pays-sabolien/competences/environnement/decheterie/ | Pays sabolien decheterie 18 passages 2025 facturation 5-50 EUR moyenne 10
QRY-007 | FETCH | INSPECTED | SRC-004 | https://www.payssabolien.fr/le-pays-sabolien/competences/environnement/redevance-gestion-des-dechets/ | Pays sabolien redevance incitative 2013 18 passages partie fixe
QRY-008 | FETCH | INSPECTED | SRC-005 | https://www.grandavignon.fr/sites/default/files/media/downloads/rapport_annuel_2022.pdf | Grand Avignon rapport annuel 2022 structure flux gravats 26% vegetaux 23% tout-venant 17%
QRY-009 | FETCH | INSPECTED | SRC-006 | https://www.grandavignon.fr/sites/default/files/media/downloads/rapport_dd2024-25.pdf | Grand Avignon rapport SDD 2024-25 Novalie decheterie 7716 t apports -6% 2024

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://cyclad.org/actualites/les-chiffres-cles-2025/
SRC-002 | ◈ | fam:A | https://cyclad.org/app/uploads/2023/09/CHIFFRES-CLES-2022-WEB.pdf
SRC-003 | ◈ | fam:A | https://www.payssabolien.fr/le-pays-sabolien/competences/environnement/decheterie/
SRC-004 | ◈ | fam:A | https://www.payssabolien.fr/le-pays-sabolien/competences/environnement/redevance-gestion-des-dechets/
SRC-005 | ◈ | fam:A | https://www.grandavignon.fr/sites/default/files/media/downloads/rapport_annuel_2022.pdf
SRC-006 | ◈ | fam:A | https://www.grandavignon.fr/sites/default/files/media/downloads/rapport_dd2024-25.pdf

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.payssabolien.fr/le-pays-sabolien/competences/environnement/decheterie/ | A | 2026-08-31 | Pays sabolien : quota 18 passages/an depuis 01/01/2025, facturation 2026, moyenne 2024 = 10 passages | Pays sabolien (page decheterie officielle INSPECTEE) : controle d'acces par badge, particuliers uniquement, pros renvoyes a la SOSAREC ; depuis le 01/01/2025 chaque foyer detenteur d'une carte a droit a 18 passages/an ; en cas de depassement, facturation appliquee en 2026 : 5 EUR/passage (seuil 19-24) et 50 EUR/passage au-dela de 25 ; 'le nombre de passages moyen en decheterie en 2024 est de 10 par an par foyer. En fixant un seuil de 18 passages, seuls les gros consommateurs du service sont impactes' - calibrage ~2x la moyenne reelle. | c56baf08-c442-46a2-9cc8-37e60a02c1fe
FCT-002 | FACT | ✧ | https://www.payssabolien.fr/le-pays-sabolien/competences/environnement/redevance-gestion-des-dechets/ | A | 2026-08-31 | Pays sabolien : redevance incitative depuis 2013, 18 passages decheterie dans la partie fixe | Pays sabolien (page redevance INSPECTEE) : Redevance Gestion des Dechets incitative depuis 2013, facturee a chaque usager, bac OM equipe d'une puce (comptage des leves) ; la partie fixe inclut 'les 18 passages en decheterie', les leves de bacs jaunes, l'acces au verre ; les passages decheterie hors forfait sont factures sur la premiere facture de l'annee suivante ; tarifs fixes par deliberation. Le quota passages est donc encastre dans un systeme complet de tarification incitative (REOMi) et non un dispositif isole. | 12d27084-9994-4493-acb9-5674110032ad
FCT-003 | FACT | ✧ | https://www.grandavignon.fr/sites/default/files/media/downloads/rapport_annuel_2022.pdf | A | 2022-12-31 | Grand Avignon : structure des flux decheterie 2022 (gravats 26%, vegetaux 23%, tout-venant 17%) | Grand Avignon rapport annuel 2022 (PDF INSPECTE) : repartition des tonnages decheterie 2022 = gravats 26%, vegetaux 23%, tout-venant 17%, DEA 11%, bois 8%, encombrants incinerables 7%, ferrailles 3%, DEEE 3%, cartons 2%, ampoules/neons et TLC ~0%. Profil urbain/periurbain ou gravats et vegetaux dominent (49% a eux deux) - ligne de base 'avant quota' (le quota de 18 passages arrive en 02/2026). | e7c37374-8dad-46ff-9d61-aeb8c6d3d541
FCT-004 | FACT | ✧ | https://www.grandavignon.fr/sites/default/files/media/downloads/rapport_dd2024-25.pdf | A | 2024-12-31 | Grand Avignon : apports decheterie en baisse -6% en 2024, premiere baisse depuis 2020, AVANT quota | Grand Avignon rapport SDD 2024-25 (PDF INSPECTE, ligne 3869) : la decheterie Novalie (site Vedene, geree en DSP par SUEZ, parties vauclusiennes) receptionne 7 716 t en 2024 ; 'Les apports sont en diminution pour la premiere fois depuis 2020 (-6%)'. Cette baisse survient AVANT la mise en place du quota de 18 passages (02/2026) : les tonnages peuvent donc baisser sans quota - renforce le confondant de la passe 1002. Le site Novalie 2024 = 253 724 t toutes activites, 96,7% valorisees (matiere+energie). | 73fc960b-2f00-4de3-a956-9f97359e3cba
FCT-005 | FACT | ✧ | https://cyclad.org/actualites/les-chiffres-cles-2025/ | A | 2026-05-19 | Cyclad : 22 decheteries = 53-57% des dechets du territoire, 75% des materiaux valorises | Cyclad chiffres cles 2025 (page INSPECTEE) : 22 decheteries receptionnent 53% des dechets produits (et jusqu'a 57% selon chiffres cles 2022) ; 7 intercommunalites, 233 communes, 235 104 hab ; 75% des materiaux deposes en decheterie valorises ; -3 kg OMR/hab entre 2024 et 2025 ; 1 533 t de biodechets. Pass CYCLAD : acces gratuit a 24 passages/an, decombres a partir du 01/01/2026 pour les particuliers (Facebook officiel). | faf878c6-621f-4b13-b039-73aaaea0dcda
FCT-006 | FACT | ✧ | https://cyclad.org/app/uploads/2023/09/CHIFFRES-CLES-2022-WEB.pdf | A | 2022-12-31 | Cyclad : structure des flux decheterie 2022 (gravats 28%, vegetaux 24%) | Cyclad chiffres cles 2022 (PDF INSPECTE) : gravats 28% des apports decheterie (recyclage en remblai 9 796 t + stockage ISDI 6 531 t), vegetaux 24% (compost 16 327 t) ; les decheteries receptionnent 57% des dechets produits sur le territoire. Profil rural/periurbain de Charente-Maritime : gravats et vegetaux dominent, comme au Grand Avignon. | e2474ab3-3362-4870-b257-02fad19a7f84
FCT-007 | FACT | ✧ | https://www.grandavignon.fr/sites/default/files/media/downloads/rapport_annuel_2022.pdf | A | 2026-08-31 | Les structures de flux avant quota des 3 EPCI diffèrent (Grand Avignon gravats 26-29%/vegetaux 23-25%, Cyclad gravats 28%/vegetaux 24%) | Croisement sources INSPECTEES : les 3 EPCI a quota ont des structures de flux 'avant' documentees et toutes DIFFERENTES - Grand Avignon gravats 26% (29% en 2023 SDD)/vegetaux 23% (24,8% en 2023), Cyclad gravats 28%/vegetaux 24%. Un quota GENERIQUE de passages (18-24/an, sans distinction de flux dans les 3 cas) frappe donc en premier le flux le plus FREQUENT de chaque territoire, qui n'est pas le meme partout - confirme la passe 1002 (un quota passages touche le tout-venant, flux des petits apports frequents). | 715fe463-415d-415d-95aa-2b665d2fd66d
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-003
FCT-002 | SRC-004
FCT-003 | SRC-005
FCT-004 | SRC-006
FCT-005 | SRC-001
FCT-006 | SRC-002
FCT-007 | SRC-005,SRC-002

## REFUTATION_REGISTRY_V1

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -
FCT-007 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-31T08:19:31.253988+00:00","fact_mem":{"FCT-001":"c56baf08-c442-46a2-9cc8-37e60a02c1fe","FCT-002":"12d27084-9994-4493-acb9-5674110032ad","FCT-003":"e7c37374-8dad-46ff-9d61-aeb8c6d3d541","FCT-004":"73fc960b-2f00-4de3-a956-9f97359e3cba","FCT-005":"faf878c6-621f-4b13-b039-73aaaea0dcda","FCT-006":"e2474ab3-3362-4870-b257-02fad19a7f84","FCT-007":"715fe463-415d-415d-95aa-2b665d2fd66d"},"mnemo_row":"WROTE:pending","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"NONE","success":1}],"writeback_row":{"attempted":7,"blocked":0,"eligible":7,"failure":0,"success":7}}

PERSISTENCE_META: MNEMO_ROW:WROTE:pending | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:7;attempted:7;success:7;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[7 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
