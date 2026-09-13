ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-1301-dechetteries-france-fresque | PARENT_RUN_ID:20260830-1038-dechetteries-france-p0 | AS_OF:2026-08-30
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_dechetteries-france-fresque/2026-08-30_13-01_dechetteries-france-fresque_INPUT.md | SUBJECT_SLUG:dechetteries-france-fresque | SUBJECT_FP:sha256:2fd493f55a8bbfe6f8dfca991ffd8924ec3fc2ba545add140fb811aebddf74ff | INPUT_SHA256:sha256:d20a5aea2fb525b64fc9134c0cbdf59022d128c2743b7ceb958cf5f98311da5f
COMPLEXITY:9→APEX | CHECKPOINT_SEQ:9 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'domains': ['legislation', 'archives', 'institutions', 'operateurs', 'donnees'], 'geo': 'France metropole + DROM', 'period': '1967-2026', 'question': 'Fresque historique evolution dechetteries : concept vs mot, acte Gradignan, cadre legal, volume reseau, acteurs'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# KERNEL investigation UPDATE — Fresque de l'évolution des déchèteries en France

RUN_ID : 20260830-1301-dechetteries-france-fresque · PARENT_RUN_ID : 20260830-1038-dechetteries-france-p0
AS_OF : 2026-08-30 · INPUT_KIND : UPDATE · MISSION_MODE : INVESTIGATION · via KERNEL v2.10.6

## Résumé

Cette passe consolide la fresque historique du parc français de déchèteries en confrontant l'acte primaire (registres CUB 1980), le néologisme/politique 1987 (circulaire 87-63), le cadre réglementaire (lois 1975/1992, AGEC 2020, ICPE 2710) et un dénombrement réel du réseau (annuaire SINOE). Elle fait émerger deux découvertes probatoires majeures : (1) le mot « déchèterie » est absent des 6 registres CUB de 1980, remplacé par un « Centre de Recyclage et de Récupération des Déchets » ; (2) la date officielle « 17/11/1980 » à Gradignan ne correspond à aucune séance plénière et SINOE la date de 1981.

## Faits établis (verdict)

- **FCT-001 (✧)** : Zéro occurrence du mot déchèterie dans les 6 registres CUB 1980 (BXM 511 W70-75, corpus complet OCR) ; les déchets hors-collecte relèvent de décharges contrôlées et d'un « Centre de Recyclage et de Récupération des Déchets » (affaire 80/151) sur le terrain de Gradignan (chemin d'Omon), commission Environnement 04/02/1980, adopté au Conseil 21/03/1980, précédé d'une délib 27/04/1979.
- **FCT-002 (✧)** : Aucune séance plénière CUB au 17/11/1980 (sessions d'automne 17/10, 21/11, 19/12) ; la date n'apparaît que comme date de commissions. La revendication officielle « 17/11/1980 » n'est pas appuyée par une séance plénière du registre.
- **FCT-003 (✧)** : Annuaire SINOE (45 169 enregistrements) : 4 635 sites ouverts au dernier millésime ; distribution : pionniers 1977-1989, décollage 1990-1993, boom 1994-2001 (pic 450 en 2001).
- **FCT-004 (✧)** : Circulaire interministérielle 87-63 du 26/06/1987 prescrit la création de « déchèteries, centres de réception des déchets encombrants... nouvel équipement communal » pour prévenir les dépôts sauvages ; 4,5 M habitants non desservis au 31/12/1985.
- **FCT-005 (✧)** : SINOE date la déchèterie de Gradignan à 1981-01-01, pas 1980 ; trois dates en conflit (21/03/1980 acte, 17/11/1980 revendication, 1981 SINOE).
- **FCT-006 (✧)** : sites fixes déclarés antérieurs à 1980 dans SINOE (Benais 1973, St-Aquilin 1973, Ivry-la-Bataille 1975, Arles 1977, outlier Longwy 1960, + 2 mobiles 1974) — autodéclarés, à vérifier.
- **FCT-007 (✧)** : ICPE rubrique 2710 régit les déchèteries (déclaration/enregistrement/autorisation) ; arrêté 1997 abrogé 01/07/2012 ; renforcement incendie 2023/2025.

Statut d'indépendance : tous les faits web sont à famille unique (AIDA/ADEME ou registres) ⇒ tier ✧ (pas ✦). Corroboration indépendante (presse, JORF, archives syndicat) reste GAP.

## Épistémique

- Le récit « Gradignan première déchèterie de France 1980 » est **fragilisé à trois niveaux** : le mot n'existe pas dans le registre 1980, la date plénière n'existe pas au 17/11, et SINOE retient 1981. Ce n'est pas une réfutation de l'antériorité conceptuelle (fait matériel du centre de recyclage dès 1979) mais une **fissure sur la date et le nom**.
- Le néologisme/politique de 1987 (circulaire 87-63) est confirmé comme acte fondateur du mot et de la promotion nationale de l'équipement.

## Limites
Famille unique par fait web ; presse payante (Sud Ouest/RetroNews) non sondée ; prime occurrence JORF du mot et attributions ANRED non corroborées nominativement ; D_OUV SINOE autodéclarés.

## Traçabilité
5 sources (SRC-001 à 005) · 7 QRY (5 FETCH, 2 WEB) · 7 faits ✧ · 3 LED · 3 AXS · 2 CLM · 1 CAU. Synchronisation registres + RAW SINOE en evidence.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:3|CLM:2|AXS:3|CAU:1|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_excerpt":"6 registres CUB 1980 lus, zero occurrence dechetterie ; affaire 80/151 Centre de Recyclage sur terrain Gradignan","kind":"EVENT","lead":"Lire l acte primaire reel 1980 et verifier le mot dechetterie dans le registre CUB","linked_ids":["AXS-001"],"locator":"registres CUB BXM 511 W70-75","materiality":"DECISIVE","routes":["EXPAND"],"source_id":"SRC-004","status":"SATURATED"}
LED-002 | {"evidence_excerpt":"4635 sites ouverts dernier millesime, pic 1994-2001","kind":"OBJECT","lead":"Denombrer le reseau reel ouvert et la distribution des ouvertures","linked_ids":["AXS-002"],"locator":"annuaire SINOE raw","materiality":"DECISIVE","routes":["EXPAND"],"source_id":"SRC-005","status":"SATURATED"}
LED-003 | {"evidence_excerpt":"Gradignan D_OUV=1981-01-01 ; acte registre 21/03/1980 ; revendication 17/11/1980 ; aucune seance pleniere au 17/11","gap":"date exacte Gradignan non discriminee : 21/03/1980 (acte) vs 17/11/1980 (revendic officielle) vs 1981 (SINOE) ; aucune seance pleniere au 17/11","gap_type":"INDEPENDENCE","kind":"RELATION","lead":"Confronter la date officielle (17/11/1980) aux dates SINOE/registre (1981/21-03-1980)","linked_ids":["AXS-003"],"locator":"annuaire SINOE raw Gradignan","materiality":"DECISIVE","routes":["EXPAND"],"source_id":"SRC-005","status":"GAP"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"La dechetterie de Gradignan est presentee par les Archives BM comme premiere de France, ouverte le 17/11/1980 ; le registre plenier CUB 1980 connait la date 21/03/1980 (acte 80/151 Centre de Recyclage) et SINOE date 1981","claimant":"Archives BM / registre / SINOE","counter":"date 17/11/1980 non attestee en seance pleniere ; 3 dates contradictoires (21/03/1980, 17/11/1980, 1981)","gap":"3 dates contradictoires ; absence de corroboration independante de la seance du 17/11","gap_type":"INDEPENDENCE","status":"GAP","support":"FCT-001,FCT-002,FCT-005"}
CLM-002 | {"claim":"Le mot dechetterie est un neologisme/politique introduit par la circulaire 87-63 (1987) ; le concept (centre de recyclage/reception) existait des 1979-80","claimant":"circulaire 87-63 AIDA","counter":"raconts alternatifs (Veolia 1986 ; ANRED stagiaires) ; quelques sites SINOE pre-1980 autodedares","gap":"prime occurrence JORF et attributions ANRED non corroborees","gap_type":"INDEPENDENCE","status":"GAP","support":"FCT-004,FCT-001"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-005"],"axis":"EVIDENCE_CASES","led_clm_links":["LED-001"],"question":"Le mot dechetterie apparait-il dans le registre plenier CUB 1980, et quel est l acte reel ?","sought_objects":"registres BXM 511 W70-75","status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-006"],"axis":"RESOURCES_FLOWS","led_clm_links":["LED-002"],"question":"Combien de dechetteries ouvertes en France aujourd hui, et quelle distribution temporelle ?","sought_objects":"annuaire SINOE complet","status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-005"],"axis":"COUNTER_HYPOTHESES","gap":"prime occurrence JORF , stagiaires ANRED , verite de la date non corroborees hors famille officielle","gap_type":"INDEPENDENCE","led_clm_links":["LED-003"],"question":"La primaute revendiquee de Gradignan 17/11/1980 est-elle corrobree hors source officielle ?","sought_objects":"date SINOE, seances registre, sites pre-1980","status":"GAP"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"l essor du reseau (pic 1994-2001) est aussi porte par la loi 92-646 et les plans departementaux, effet cumulatif non demele","from":"crise des depots sauvages et des decharges brutes (fin 1985 : 4,5M habitants non desservis)","gap":"effet loi 92-646 sur acceleration du reseau confondu avec progres general ; non demele etape par etape","gap_type":"CAUSALITY","link_type":"MECHANISM","mechanism":"la circulaire 87-63 transforme le depot d' apport volontaire en outil de police sanitaire et en nouvel equipement communal, promu par les prefets via les schemas departementaux","source":"FCT-004","status":"GAP","to":"politique nationale des dechetteries (1987+)"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:2|FETCH:5|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND | mnemolite | memories:voir-runs-precedents | MNEMO_Q
SYS-003 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-004 | SYS | PASS | runtime | SYS-002 | REPAIR_SYS
SYS-005 | SYS | PASS | runtime | SYS-003 | REPAIR_SYS
SYS-006 | SYS | SUPERSEDED | runtime | - | PERSIST_MANUAL_LEGACY
SYS-007 | SYS | PARTIAL | runtime | ATTEMPT-001 | PERSIST_REBIND
SYS-008 | SYS | SUPERSEDED | runtime | - | PERSIST_MANUAL_LEGACY
SYS-009 | SYS | PASS | runtime | ATTEMPT-002 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://aida.ineris.fr/reglementation/circulaire-ndeg-87-63-260687-relative-a-lelimination-ordures-menageres | FETCH AIDA circulaire 87-63 creation dechetteries
QRY-002 | FETCH | FOUND | SRC-002 | https://www.data.gouv.fr/api/1/datasets/sinoe-r-annuaire-des-decheteries-dma/ | FETCH data.gouv SINOE annuaire denombrement
QRY-003 | FETCH | FOUND | SRC-003 | https://aida.ineris.fr/reglementation/2710-installation-collecte-dechets-apportes-producteur-initial-dechets-a-lexclusion | FETCH AIDA ICPE 2710 regimes arrfiles
QRY-004 | WEB | FOUND | - | - | WEB nombre dechetteries France SINOE 2024 sites ouverts estimation reseau
QRY-005 | FETCH | FOUND | SRC-004 | https://archives.bordeaux-metropole.fr | FETCH registres CUB 1980 BXM 511 W70-75 : recherche dechetterie/encombrants/Gradignan (playwright pdftotext)
QRY-006 | FETCH | FOUND | SRC-005 | https://data.ademe.fr/data-fair/api/v1/datasets/sinoe-(r)-annuaire-des-decheteries-dma/raw | FETCH data.ademe raw csv annuaire decheteries (45169 enregistrements) analyse ouverture
QRY-007 | WEB | FOUND | - | - | WEB ressources recycleries RNRR Cycl-op nombre adherents paysage reemploi dechetterie

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:other:ademe-aida | https://aida.ineris.fr/reglementation/circulaire-ndeg-87-63-260687-relative-a-lelimination-ordures-menageres
SRC-002 | ◈ | fam:other:ademe-aida | https://www.data.gouv.fr/api/1/datasets/sinoe-r-annuaire-des-decheteries-dma/
SRC-003 | ◈ | fam:other:ademe-aida | https://aida.ineris.fr/reglementation/2710-installation-collecte-dechets-apportes-producteur-initial-dechets-a-lexclusion
SRC-004 | ◈ | fam:other:archives-bm | https://archives.bordeaux-metropole.fr
SRC-005 | ◈ | fam:other:ademe-aida | https://data.ademe.fr/data-fair/api/v1/datasets/sinoe-(r)-annuaire-des-decheteries-dma/raw

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://archives.bordeaux-metropole.fr | other:archives-bm | 1980 | registre-CUB-1980-zero-corpus-dechetterie | Lecture directe des 6 registres CUB 1980 (BXM 511 W70-75, corpus complet OCR) : ZERO occurrence du mot dechetterie et de toutes variantes OCR ; les dechets hors-collecte sont geres par decharges controlees et un Centre de Recyclage et de Recuperation des Dechets (affaire 80/151) sur terrain mis a disposition par la commune de Gradignan (chemin d'Omon), commission Environnement 04/02/1980, adopte Conseil 21/03/1980, precedee d'une deliber 27/04/1979 | 76d4a2b4-92be-4378-a7de-e2a331b8d210
FCT-002 | FACT | ✧ | https://archives.bordeaux-metropole.fr | other:archives-bm | 1980-11-17 | aucune-seance-pleniere-17-11-1980 | Aucune seance pleniere du Conseil CUB au 17/11/1980 dans le registre (sessions d'automne : 17/10, 21/11, 19/12). La date 17/11/1980 apparait uniquement comme date de commissions (Adjudications, Finances). La revendication officielle 'ouverte le 17 novembre 1980' n'est pas appuyee par une seance pleniere du registre. | 43ddef68-e1e3-4631-8f05-6b0f4c042bd3
FCT-003 | FACT | ✧ | https://data.ademe.fr/data-fair/api/v1/datasets/sinoe-(r)-annuaire-des-decheteries-dma/raw | other:ademe-aida | 2026 | reseau-dechetteries-ouvert-4635-sites | Analyse de l'annuaire SINOE (45169 enregistrements, series 2009-2026) : 4635 sites ouverts au dernier millesime (avec record >=2025 parmi 5217 services distincts). Distribution ouverture : pionniers 1977-1989, decollage 1990-1993, boom 1994-2001 (pic 450 en 2001), stabilisation apres 2010. Reseau actuel ~4600-4700 sites. | d4d620a8-3ca4-4413-9347-0801d33d0ca5
FCT-004 | FACT | ✧ | https://data.ademe.fr/data-fair/api/v1/datasets/sinoe-(r)-annuaire-des-decheteries-dma/raw | other:ademe-aida | 1981-01-01 | gradignan-sinoe-1981-pas-1980 | Annuaire SINOE : decheterie de Gradignan enregistree D_OUV = 1981-01-01 (ouverte aujourd'hui). Contradiction latente avec la revendication officielle 'ouverte 17/11/1980' (acte registre 21/03/1980). Trois dates en conflit pour le meme equipement. | 56c0f94d-770a-4400-8537-aa5f1e46adc6
FCT-005 | FACT | ✧ | https://data.ademe.fr/data-fair/api/v1/datasets/sinoe-(r)-annuaire-des-decheteries-dma/raw | other:ademe-aida | 1980 | sites-fixes-prealables-ailler-1980-dclares | Annuaire SINOE : sites fixes declares ouverts avant 1980 (D_OUV autodeclare par collectivites) : Benais 1973-11-26, Saint-Aquilin-de-Pacy 1973, Ivry-la-Bataille 1975, Arles 1977, + outlier Longwy '1960' suspect, + 2 mobiles 1974 (Jura). Concurrencent la primaute de Gradignan mais dates retro-datees possibles, a verifier niveau source nominative. | e3abd0aa-5a9d-49f9-809a-3c4d0806e2c1
FCT-006 | FACT | ✧ | https://aida.ineris.fr/reglementation/circulaire-ndeg-87-63-260687-relative-a-lelimination-ordures-menageres | other:ademe-aida | 1987-06-26 | circulaire-87-63-invention-mot-dechetterie-politique | Circulaire 87-63 26/06/1987 : prescrit la creation de dechetteries, centres de reception des dechets encombrants ouverts en permanence au public, nouvel equipement communal (AIDA). Acte fondateur politique nationale ; famille unique AIDA. | 8507827c-1355-48bc-b2af-dbe364d37509
FCT-007 | FACT | ✧ | https://aida.ineris.fr/reglementation/2710-installation-collecte-dechets-apportes-producteur-initial-dechets-a-lexclusion | other:ademe-aida | 2012 | icpe-2710-regime-dechetteries | ICPE rubrique 2710 : regimes declaration/enregistrement/autorisation (arretes 2012) ; arrete 02/04/97 dechetteries amenegees abroge 01/07/2012 ; renforcement incendie arretes 05-06/05/2025 (AIDA). Cadre norme moderne. | 98be4887-1ecc-4ef7-a5cd-22813b3affbc
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-004
FCT-002 | SRC-004
FCT-003 | SRC-005
FCT-004 | SRC-005
FCT-005 | SRC-005
FCT-006 | SRC-001
FCT-007 | SRC-003

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
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8
CP-003 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8
CP-004 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-005 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-006 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12;13
CP-007 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-008 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18
CP-009 | CORRECTION | PASS | LAST_COMPLETED:18b | NEXT_ACTION:18b

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T11:21:15.455696+00:00","fact_mem":{"FCT-001":"76d4a2b4-92be-4378-a7de-e2a331b8d210","FCT-002":"43ddef68-e1e3-4631-8f05-6b0f4c042bd3","FCT-003":"d4d620a8-3ca4-4413-9347-0801d33d0ca5","FCT-004":"56c0f94d-770a-4400-8537-aa5f1e46adc6","FCT-005":"e3abd0aa-5a9d-49f9-809a-3c4d0806e2c1","FCT-006":"8507827c-1355-48bc-b2af-dbe364d37509","FCT-007":"98be4887-1ecc-4ef7-a5cd-22813b3affbc"},"mnemo_row":"ed091dfe-bab3-45bc-bc6a-0d3ae64d2922","result":"PARTIAL","writeback_execution":[],"writeback_row":{"attempted":7,"blocked":0,"eligible":7,"failure":0,"success":7}}
ATTEMPT-002 | {"created_at":"2026-08-30T11:26:38.680572+00:00","fact_mem":{"FCT-001":"76d4a2b4-92be-4378-a7de-e2a331b8d210","FCT-002":"43ddef68-e1e3-4631-8f05-6b0f4c042bd3","FCT-003":"d4d620a8-3ca4-4413-9347-0801d33d0ca5","FCT-004":"56c0f94d-770a-4400-8537-aa5f1e46adc6","FCT-005":"e3abd0aa-5a9d-49f9-809a-3c4d0806e2c1","FCT-006":"8507827c-1355-48bc-b2af-dbe364d37509","FCT-007":"98be4887-1ecc-4ef7-a5cd-22813b3affbc"},"mnemo_row":"ed091dfe-bab3-45bc-bc6a-0d3ae64d2922","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"NONE","success":1}],"writeback_row":{"attempted":7,"blocked":0,"eligible":7,"failure":0,"success":7}}

PERSISTENCE_META: MNEMO_ROW:ed091dfe-bab3-45bc-bc6a-0d3ae64d2922 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:7;attempted:7;success:7;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[7 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
