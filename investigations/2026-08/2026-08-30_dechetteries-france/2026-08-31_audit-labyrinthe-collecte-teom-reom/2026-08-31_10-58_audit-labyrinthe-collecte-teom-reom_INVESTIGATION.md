ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260831-1058-audit-labyrinthe-collecte-teom-reom | PARENT_RUN_ID:NONE | AS_OF:2026-08-31
INPUT_KIND:NEW | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-31_audit-labyrinthe-collecte-teom-reom/2026-08-31_10-58_audit-labyrinthe-collecte-teom-reom_INPUT.txt | SUBJECT_SLUG:audit-labyrinthe-collecte-teom-reom | SUBJECT_FP:sha256:d96ba311eddda2b3f539c0a52fcc4780f4290f65962d74af7557a8d9314a8fe9 | INPUT_SHA256:sha256:ca9b101df1133eb90ea08575b93a9bb8df6b4198d247f43901b7fdd37e5d3d23
COMPLEXITY:0.6→MEDIUM | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors': ['ADEME', 'collectivites', 'EPCI', 'Syndicats mixtes', 'Senat'], 'domains': ['dechets', 'collecte', 'mode-mix', 'couleurs contenants', 'TEOM', 'REOM'], 'geo': 'France', 'lead_question': 'Les modalites de collecte, couleurs et regimes de financement sont-ils non harmonises et coexistent-ils pour un meme foyer/territoire ?', 'limits': 'pas de donnee nationale conteneurs enterres; perception usager non mesuree', 'object_question': '(1) mode-mix PAP/AV ADEME 2023 ; (2) couleurs OMR + harmonisation L541-10-18 ; (3) EPCI/syndicats coexistants (Senat).'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Le labyrinthe local de la collecte : coexistence structurelle des modes, couleurs et financements

**Run `20260831-1058-audit-labyrinthe-collecte-teom-reom`** (MEDIUM, passe courte). OBJECT : ancrer dans une donnee officielle le « labyrinthe local » decrit par la vignette d'ouverture de l'article (repas de famille : bac jaune, bac gris, bacs payants, conteneurs enters, chaque ville son systeme).

## Conclusion

Le labyrinthe n'est pas une impression : il est structurel, documente par l'enquete ADEME collecte 2023 (rapport 7907, INSPECTE 2429 lignes) et le rapport Senat PPL l25-049 (Paccaud, 21/10/2025, INSPECTE). Quatre mecanismes officiels, cumules :

## 1. Meme foyer, plusieurs modes de collecte (T1, ADEME 2023)
- 74 % des tonnages d'emballages et papiers sont collectes selon un **mode mixte** : boutique-a-boutique ET apport volontaire presents sur le meme territoire, pour le meme flux ou des flux differents (FCT-001).
- La majorite de la population a acces a un ramassage en porte-a-porte, ~70 % des quantites d'emballages et papiers collectees en PAP, ratio PAP toujours > AV (FCT-002).
- OMR : PAP pour au moins 59 % de la population en 2023, double par apport volontaire pour 20 %, avec **doubles services** (un habitant peut avoir a la fois un bac PAP et un conteneur AV). La part PAP est tombee de 77 % (2021) a 59 % avec le deploiement de l'AV (FCT-003).

## 2. Des couleurs de contenants non harmonisees (T1, ADEME 2023)
- OMR : le bac est le principal contenant PAP (~35 M d'habitants) mais la couleur n'est PAS harmonisee : gris 42 %, noir, vert (FCT-004).
- L'article L541-10-18 exigeait une harmonisation nationale effective au plus tard le **31/12/2022** : en 2023 elle n'est pas atteinte (jaune pour multimateriaux, bleu pour papiers, pluriel des schemas) (FCT-005).

## 3. Une competence fragmentee sur ~1 265 EPCI et des syndicats mixtes (T2, Senat)
- La competence collecte-traitement est obligatoire pour les 1 265 EPCI a fiscalite propre ; mutualisable en syndicat mixte. « Au sein d'une meme structure peuvent donc coexister des modalites differentes de collecte » (FCT-006).
- Le mode de financement (TEOM ou REOM) est laisse au choix de chaque collectivite (FCT-006, confirme par la passe collecte 0927 : TEOM classique ~72 % de la pop, financement mixte TEOM+REOM legal sur un meme territoire).

## Bouclage article
La vignette « bac jaune, bac gris, conteneurs enterres, chaque ville son systeme » cesse d'etre une impression : l'enquete nationale la documente. Deux passerelles avec le reste de la fresque : (1) le labyrinthe pousse le hors-bac vers la decheterie, seul exutoire commun (liaison passe 0942/0953) ; (2) la fragmentation des modalites et des financements repond a la fragmentation des quotas d'acces (passes 2103/2123/1002) : meme logique locale, meme absence de referentiel national.

## Gaps
- Pas de donnee nationale sur les conteneurs enterres (nombre, part de population, nuit payante ni fiscalement visible).
- L'enquete ADEME ne mesure pas la perception usager (« bordel »).
- Refus de tri (802 kt, 22,7 %) documente mais non isolee par mode de collecte.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:2|CLM:2|AXS:2|CAU:1|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_key":"ADEME 2023 mode mixte 74% emballages/papiers; PAP 59%(OMR)+AV 20% doubles services; couleurs OMR non harmonisees (gris 42%); L541-10-18 31/12/2022 non atteint; 1265 EPCI + syndicats mixtes coexistants","note":"delta vs passes collecte 0927 (deja TEOM 72%, financement mixte legal) : ajoute la coexistence des MODES au niveau du foyer","routes":["modes collecte PAP/AV","couleurs contenants","regimes financement TEOM/REOM","harmonisation L541-10-18"],"status":"SATURATED","title":"Coexistence de modes, couleurs et regimes de financement non harmonises = labyrinthe structurel"}
LED-002 | {"evidence_key":"ADEME 2023 mode mixte 74% emballages/papiers; PAP 59%(OMR)+AV 20% doubles services; couleurs OMR non harmonisees (gris 42%); L541-10-18 31/12/2022 non atteint; 1265 EPCI + syndicats mixtes coexistants","note":"delta vs passes collecte 0927 (deja TEOM 72%, financement mixte legal) : ajoute la coexistence des MODES au niveau du foyer","routes":["modes collecte PAP/AV","couleurs contenants","regimes financement TEOM/REOM","harmonisation L541-10-18"],"status":"SATURATED","title":"Coexistence de modes, couleurs et regimes de financement non harmonises = labyrinthe structurel"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Le labyrinthe local de la collecte est structurel : un meme foyer ou un meme territoire peut combiner PAP et apport volontaire (par flux ou par zone), des couleurs de contenants non harmonisees, et relever de regimes de financement choisis localement.","counter":"L'article L541-10-18 visait une harmonisation nationale des consignes/couleurs au 31/12/2022 ; sa non-atteinte en 2023 (FCT-005) ne prouve pas a elle seule un labyrinthe percu, mais documente l'absence d'harmonisation effective.","gap":"pas de donnee nationale sur les conteneurs enterres (nombre, part population); l'enquete n'isole pas la perception usager du labyrinthe","gap_type":"COVERAGE_PARTIAL","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-006"]}
CLM-002 | {"claim":"Le labyrinthe local de la collecte est structurel : un meme foyer ou un meme territoire peut combiner PAP et apport volontaire (par flux ou par zone), des couleurs de contenants non harmonisees, et relever de regimes de financement choisis localement.","counter":"L'article L541-10-18 visait une harmonisation nationale des consignes/couleurs au 31/12/2022 ; sa non-atteinte en 2023 (FCT-005) ne prouve pas a elle seule un labyrinthe percu, mais documente l'absence d'harmonisation effective.","gap":"pas de donnee nationale sur les conteneurs enterres (nombre, part population); l'enquete n'isole pas la perception usager du labyrinthe","gap_type":"COVERAGE_PARTIAL","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-006"]}

### AXIS_REGISTRY_V1
AXS-001 | {"question":"Les modalites de collecte (PAP/AV/PAV/enterres), couleurs de contenants et regimes de financement sont-ils non harmonises et coexistent-ils pour un meme foyer/territoire ?","routes":["AUDIT","EXPAND"],"sought_objects":["modes collecte","couleurs contenants","regimes financement","EPCI/syndicats","harmonisation"],"status":"SATURATED"}
AXS-002 | {"question":"Les modalites de collecte (PAP/AV/PAV/enterres), couleurs de contenants et regimes de financement sont-ils non harmonises et coexistent-ils pour un meme foyer/territoire ?","routes":["AUDIT","EXPAND"],"sought_objects":["modes collecte","couleurs contenants","regimes financement","EPCI/syndicats","harmonisation"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"La fragmentation des modalites de collecte (74% mode mixte PAP+AV), des couleurs et des regimes de financement non harmonises","effect":"Un labyrinthe local ou chaque territoire/foyer compose son acces au service - et ou la decheterie est le seul exutoire commun pour les flux que le bac ne prend pas","mechanism":"ADEME 2023 (modes) + Senat (competence 1265 EPCI, syndicats mixtes) + L541-10-18 non atteint + liaison passe 0942/0953","status":"SUPPORTED","support":["FCT-001","FCT-003","FCT-004","FCT-005","FCT-006"]}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:4|FETCH:5|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"EMPTY","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"EMPTY","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"EMPTY","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND | runtime | warm-route-teom-reom-collecte | MNEMO_Q
SYS-003 | SYS | FOUND | runtime | teom-classique-72pct | MEMORY_PROBE
SYS-004 | SYS | FOUND | runtime | financement-mixte-legal | MEMORY_PROBE
SYS-005 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | OK | - | - | ADEME part collecte porte-a-porte vs points apport volontaire dechets menagers 2023 enquete collecte
QRY-002 | FETCH | INSPECTED | SRC-001 | https://librairie.ademe.fr/economie-circulaire-et-dechets/8644-la-collecte-des-dechets-par-le-service-public-en-france.html | ADEME enquete collecte 2023 resultats cles rapport
QRY-003 | WEB | OK | - | - | ADEME part collecte porte-a-porte vs points apport volontaire dechets menagers 2023 enquete collecte
QRY-004 | FETCH | INSPECTED | SRC-002 | https://librairie.ademe.fr/economie-circulaire-et-dechets/8644-la-collecte-des-dechets-par-le-service-public-en-france.html | ADEME enquete collecte 2023 resultats cles rapport
QRY-005 | WEB | OK | - | - | ADEME part collecte porte-a-porte vs points apport volontaire dechets menagers 2023 enquete collecte
QRY-006 | FETCH | INSPECTED | SRC-003 | https://librairie.ademe.fr/economie-circulaire-et-dechets/8644-la-collecte-des-dechets-par-le-service-public-en-france.html | ADEME enquete collecte 2023 resultats cles rapport
QRY-007 | FETCH | INSPECTED | SRC-004 | https://librairie.ademe.fr/index.php?controller=attachment&id_attachment=7907 | rapport ADEME enquete collecte 2023 2429 lignes modes collecte PAP AV OMR couleurs contenants
QRY-008 | WEB | OK | - | - | conteneurs enterres dechets France EPCI deploiement collecte
QRY-009 | FETCH | INSPECTED | SRC-005 | https://www.senat.fr/rap/l25-049/l25-0491.html | PPL qualite services gestion dechets Senat Paccaud 2025 EPCI 1265 coexistence modalites collecte financement TEOM REOM

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://librairie.ademe.fr/economie-circulaire-et-dechets/8644-la-collecte-des-dechets-par-le-service-public-en-france.html
SRC-002 | ◈ | fam:A | https://librairie.ademe.fr/economie-circulaire-et-dechets/8644-la-collecte-des-dechets-par-le-service-public-en-france.html
SRC-003 | ◈ | fam:A | https://librairie.ademe.fr/economie-circulaire-et-dechets/8644-la-collecte-des-dechets-par-le-service-public-en-france.html
SRC-004 | ◈ | fam:A | https://librairie.ademe.fr/index.php?controller=attachment&id_attachment=7907
SRC-005 | ◈ | fam:A | https://www.senat.fr/rap/l25-049/l25-0491.html

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://librairie.ademe.fr/index.php?controller=attachment&id_attachment=7907 | A | 2025-06-01 | ADEME collecte 2023 mode mixte 74% tonnages emballages papiers | Rapport ADEME enquete collecte 2023 (sec 3.3, Figure 24-29, loc: rapport.pdf ligne 828) : les collectes separees embarquent souvent plusieurs modes, 74 % des tonnages d'emballages et papiers collectes selon un mode mixte (porte-a-porte ET apport volontaire presents sur le territoire, meme flux ou flux differents, meme foyer). 74% = PREUVE de coexistence de modes pour un meme flux. | 7b4b18d4-81f7-4043-895e-569eaa64b69d
FCT-002 | FACT | ✧ | https://librairie.ademe.fr/index.php?controller=attachment&id_attachment=7907 | A | 2025-06-01 | ADEME collecte 2023 pres de 70% quantites emballages papiers en porte-a-porte | Rapport ADEME 2023 (sec 3.3, lignes 856-861) : la majorite de la population beneficie d'un ramassage en porte-a-porte (pour tout ou partie du flux) et pres de 70 % des quantites d'emballages et de papiers sont collectees en porte-a-porte. Le ratio PAP > AV quel que soit le schema. | 245ed84e-25c5-4cb0-942c-fb331f0131d8
FCT-003 | FACT | ✧ | https://librairie.ademe.fr/index.php?controller=attachment&id_attachment=7907 | A | 2025-06-01 | ADEME 2023 OMR majoritairement PAP 59% pop, AV 20% en complement, doubles services | Rapport ADEME 2023 (sec OMR, Fig 44-46, lignes 1344-1360) : le service de collecte des OMR reste majoritairement en porte-a-porte pour au moins 59 % de la population en 2023, complete par apport volontaire pour 20 %. Proportion PAP tombee de 77 % (2021) a 59 % avec le deploiement de l'apport volontaire (categorie mixte autre). Un habitant peut avoir acces a un service PAP ET a un service AV sur le meme territoire (doubles services). Contexte reglementaire R2224-24 : collecte hebdo PAP seulement en zones > 2000 hab, hors densite. | 31099c83-e318-41a8-8a8e-508dcdfa9708
FCT-004 | FACT | ✧ | https://librairie.ademe.fr/index.php?controller=attachment&id_attachment=7907 | A | 2025-06-01 | ADEME 2023 couleur contenants OMR non harmonisee gris 42% noir vert | Rapport ADEME 2023 (sec OMR, Fig 47-48, ligne 1378) : en 2023 le gris reste la couleur la plus employee pour la precollecte des OMR (42 % de la population), deux autres couleurs frequentes (noir, vert). La couleur des contenants OMR n'est pas harmonisee en 2023. Le bac est le principal contenant PAP (environ 35 M d'habitants, Fig 46). | ccd4de14-97e5-4993-ace7-2eb410b7a9bf
FCT-005 | FACT | ✧ | https://librairie.ademe.fr/index.php?controller=attachment&id_attachment=7907 | A | 2025-06-01 | ADEME 2023 harmonisation consignes L541-10-18 delai 31/12/2022 non atteint | Rapport ADEME 2023 (sec 3.3, lignes 1003-1025 + Fig 32) : l'Article L541-10-18 du Code de l'Environnement exigeait une harmonisation des consignes de tri et couleurs 'effective sur l'ensemble du territoire national au plus tard le 31/12/2022'. En 2023 la population reste servie par des contenants de couleurs et schemas multiples (jaune dominant pour multimateriaux, bleu pour papiers), et la couleur OMR n'est pas harmonisee (FCT-004). L'obligation legale d'harmonisation n'est pas atteinte en 2023. | ce5863d1-58f0-4439-8358-d1c5e42df1ae
FCT-006 | FACT | ✧ | https://www.senat.fr/rap/l25-049/l25-0491.html | A | 2025-10-21 | Senat 1265 EPCI syndicats mixtes coexistence modalites de collecte differentes meme structure | Rapport Senat PPL l25-049 (Paccaud, 21/10/2025, section LE DROIT EXISTANT, loc: l25-0491) : la competence collecte-traitement des dechets menagers est obligatoire pour les 1 265 EPCI a fiscalite propre ; ils peuvent la mutualiser dans un syndicat mixte sur le territoire duquel peuvent cohabiter des modes de collecte ou de traitement propres a une partie seulement du territoire. 'Au sein d'une meme structure peuvent donc coexister des modalites differentes de collecte.' Mode de financement (TEOM ou REOM) laisse au choix de chaque collectivite. | 0bb76e1b-8b62-4ca9-a0ff-f9dff45ab354
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-004
FCT-002 | SRC-004
FCT-003 | SRC-004
FCT-004 | SRC-004
FCT-005 | SRC-004
FCT-006 | SRC-005

## REFUTATION_REGISTRY_V1

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-31T09:11:01.796383+00:00","fact_mem":{"FCT-001":"7b4b18d4-81f7-4043-895e-569eaa64b69d","FCT-002":"245ed84e-25c5-4cb0-942c-fb331f0131d8","FCT-003":"31099c83-e318-41a8-8a8e-508dcdfa9708","FCT-004":"ccd4de14-97e5-4993-ace7-2eb410b7a9bf","FCT-005":"ce5863d1-58f0-4439-8358-d1c5e42df1ae","FCT-006":"0bb76e1b-8b62-4ca9-a0ff-f9dff45ab354"},"mnemo_row":"written investigation memory via API","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"NONE","success":1}],"writeback_row":{"attempted":6,"blocked":0,"eligible":6,"failure":0,"success":6}}

PERSISTENCE_META: MNEMO_ROW:written investigation memory via API | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:6;attempted:6;success:6;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[6 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
