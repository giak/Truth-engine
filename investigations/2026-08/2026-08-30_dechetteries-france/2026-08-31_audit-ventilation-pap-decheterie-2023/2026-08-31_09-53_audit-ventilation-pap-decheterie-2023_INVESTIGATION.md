ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260831-0953-audit-ventilation-pap-decheterie-2023 | PARENT_RUN_ID:NONE | AS_OF:2026-08-31
INPUT_KIND:NEW | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-31_audit-ventilation-pap-decheterie-2023/2026-08-31_09-53_audit-ventilation-pap-decheterie-2023_INPUT.txt | SUBJECT_SLUG:audit-ventilation-pap-decheterie-2023 | SUBJECT_FP:sha256:230391168747cb1977e705233e6ee7c83c104239bd1cd850024bb8204d284f15 | INPUT_SHA256:sha256:b83c612dc8203dc5611ebefeb8faf801b5a218fcdfd14d79683759387503975e
COMPLEXITY:0.6→MEDIUM | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors': ['ADEME', 'collectivites', 'INSEE', 'eco-organismes'], 'domains': ['dechets', 'collecte', 'decheterie', 'ventilation'], 'geo': 'France', 'lead_question': 'Ventilation 2023 PAP vs decheterie par flux (encombrants, verts, gravats, DEEE, dangereux).', 'limits': 'donnees 2023, croisements = calculs de l enquete', 'object_question': '(1) tableaux 6/10 2023 ; (2) ratio PAP vs decheterie ; (3) destination sortie decheterie.'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
## Ce que l'enquête établit — GAP 0942 COMBLÉ

### La ventilation 2023 PAP vs déchèterie, flux par flux (FCT-001, FCT-002, FCT-003)

Le rapport ADEME « La collecte des déchets par le service public en France – Résultats 2023 » (publié mai 2025, **PDF intégral inspecté**, 2 429 lignes extraites) permet enfin le croisement par flux que la passe 0942 avait identifié comme manquant.

**En 2023** : 37,8 Mt de DMA SPGD (559 kg/hab), répartis en **OMR 15 198 kt (225 kg/hab)**, **collectes séparées hors déchèteries 7 924 kt (117 kg/hab)**, **déchèteries 14 474 kt (214 kg/hab)** — la déchèterie porte **38 % du tonnage SPGD**.

**Collectes séparées hors déchèterie (Tableau 6)** : emballages et papiers 3,5 Mt (52,1 kg/hab), verre 2,2 Mt (32,6), biodéchets 1,1 Mt (16,8), **encombrants 0,5 Mt (7,7 kg/hab)**, dangereux < 0,01 Mt, autres 0,5 Mt.

**Déchèterie par flux (Tableau 10)** : déchets verts **4 148 kt** (63 kg/hab), déblais et gravats **3 746 kt** (58,5), encombrants/tout-venant **2 978 kt** (46), matériaux triés 2 144 kt (33), DEA mobilier 974 kt (16), DEEE 435 kt (7), dangereux 130 kt (2), autres 66 kt.

### Le ratio clé : les encombrants vont ~8 fois plus à la déchèterie qu'au bac (FCT-004)

**Encombrants : 0,5 Mt collectés en PAP/PAV vs 3 952 kt en déchèterie** (encombrants 2 978 + DEA 974), soit un **ratio ~8:1**. En 2021, l'écart était encore plus net : 0,7 Mt PAP vs 4 558 kt déchèterie. C'est la confirmation chiffrée du chaînon de la passe 0942 : **le bac ne prend pas les encombrants, la déchèterie les absorbe.**

**Déchets verts** : 4 148 kt en déchèterie vs 1,1 Mt de biodéchets collectés séparément (dont verts d'entretien des parcs) — ratio ~4:1. **Déblais et gravats** : 3 746 kt en déchèterie, **totalement absents des collectes séparées** (Tableau 6 ne les liste pas) — exutoire exclusif.

### Sortie de déchèterie : la déchèterie valorise mieux que le reste (FCT-007)

En sortie de déchèterie 2023 : **44 % valorisation matière + 26 % valorisation organique = 70 % vers la valorisation** (en hausse), **stockage en baisse à 22 %** (25 % en 2021). Les matériaux triés en déchèterie : bois 55 % (1 167 kt), métaux 24 % (507 kt), papiers-cartons 19 % (410 kt). À comparer aux OMR (31 % incinération, 14 % stockage) : **la déchèterie est le circuit qui valorise le mieux ce qu'elle reçoit.**

### Le flux se tasse mais reste massif (FCT-006, FCT-008)

**Première baisse en 15 ans** : 16 440 kt (2021) → 14 644 kt (2023), retour aux niveaux 2017/2019 — expliquée par le ralentissement de la consommation (INSEE), les bennes DEA dédiées, les déchèteries pros et l'interdiction des tontes (-15 à -25 % localement). Le parc reste stable : **4 609 déchèteries en 2023**. Disparités territoriales fortes : **66 kg/hab en urbain dense vs ~240 kg/hab en rural** (Paris n'a pas de déchèterie).

## Ce que l'article doit faire de ces résultats

1. **Remplacer l'estimation par la donnée** : les « 81 % hors bac » de la passe 0942 (basés sur la décomposition 2021) sont confirmés par la ventilation 2023 flux par flux du rapport officiel.
2. **Le chiffre le plus fort** : encombrants 0,5 Mt au bac vs 3 952 kt à la déchèterie — la déchèterie est l'exutoire à ~88 % des encombrants ménagers.
3. **Corriger le récit environnemental** : la déchèterie n'est pas le trou noir du système — 70 % de ses sorties sont valorisées (matière + organique), mieux que les OMR. Le « 25 % enfoui » (passe 0800) devient **22 % en 2023**.
4. **Renforcer le verrou** : le contrôle d'accès agit sur un flux de 14,6 Mt qui n'a pas d'alternative au bac — les quotas frappent le circuit le plus valorisant du service public.

## Ce qui reste ouvert

- La ventilation 2023 par flux au niveau EPCI (par site) reste non publiée — GAP conservé à l'échelle fine.
- Le taux de recyclage effectif (sortie d'installation) diffère du taux d'orientation (70 %) — refus de tri non ventilé par site.
- L'effet quantitatif de l'interdiction des tontes sur le flux verts (études locales seulement, -15 à -25 %).
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:0|CLM:4|AXS:3|CAU:3|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Le GAP de la passe 0942 est COMBLE: en 2023, les encombrants collectes en PAP/PAV = 0,5 Mt (7,7 kg/hab) vs 3 952 kt en decheterie (encombrants+DEA) - ratio ~8:1; la decheterie est l'exutoire quasi-exclusif des encombrants","counter":"La collecte PAP des encombrants existe (0,5 Mt) et des bennes DEA dediees reduisent les encombrants","gap":"NONE - ventilation documentee par le rapport ADEME 2023","gap_type":"NONE","status":"SUPPORTED","support":["FCT-002","FCT-003","FCT-004","FCT-006"]}
CLM-002 | {"claim":"Dechets verts (ratio ~4:1) et deblais/gravats (exclusif, absents des collectes separees) confirment: le bac ne prend pas les flux volumineux, la decheterie les absorbe","counter":"Biodéchets collectes separement 1,1 Mt (dont verts d'entretien parcs)","gap":"NONE","gap_type":"NONE","status":"SUPPORTED","support":["FCT-002","FCT-003","FCT-005"]}
CLM-003 | {"claim":"En sortie de decheterie 2023, 70% des flux vont en valorisation (44% matiere + 26% organique) et le stockage recule a 22% (vs 25% en 2021) - la decheterie valorise mieux que le reste du flux","counter":"22% encore stockes sans valorisation; le taux de recyclage effectif differe du taux d'orientation","gap":"NONE - rapport 5.3 inspecte","gap_type":"NONE","status":"SUPPORTED","support":["FCT-007"]}
CLM-004 | {"claim":"Le flux decheterie baisse pour la premiere fois en 15 ans (16 440 -> 14 644 kt) mais reste massif (38% du tonnage SPGD, 214 kg/hab) - le verrou d'acces agit sur un flux structurel","counter":"La baisse pourrait venir du ralentissement de la consommation des menages (INSEE 2023)","gap":"NONE","gap_type":"NONE","status":"SUPPORTED","support":["FCT-001","FCT-006","FCT-008"]}

### AXIS_REGISTRY_V1
AXS-001 | {"question":"Quelle est la ventilation 2023 par flux entre collecte separee (PAP/PAV) et decheterie?","routes":["AUDIT"],"sought_objects":["encombrants PAP vs decheterie","dechets verts decheterie","gravats exutoire"],"status":"SATURATED"}
AXS-002 | {"question":"Quelle est la destination en sortie de decheterie (valorisation vs stockage) et son evolution?","routes":["AUDIT"],"sought_objects":["sortie decheterie valorisation stockage","taux 2021 2023"],"status":"SATURATED"}
AXS-003 | {"question":"Comment le parc et les ratios decheterie varient-ils par territoire (urbain dense 66 vs rural 240 kg/hab)?","routes":["AUDIT"],"sought_objects":["ratios decheterie habitat","4 609 decheteries"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Les encombrants ne sont pas pris en charge par le bac (definition legale) et la collecte PAP/PAV en capte une part marginale (0,5 Mt)","effect":"3 952 kt d'encombrants+DEA aboutissent en decheterie chaque annee (ratio ~8:1)","mechanism":"Croisement Tableaux 6 et 10 du rapport ADEME 2023","status":"SUPPORTED","support":["FCT-002","FCT-003","FCT-004"]}
CAU-002 | {"cause":"Gravats et dechets verts exclus du bac (reglementation service-public, volume/poids)","effect":"Exutoires quasi-exclusifs: 3 746 kt gravats et 4 148 kt verts en decheterie","mechanism":"Croisement Tableaux 6/10; gravats absents des collectes separees","status":"SUPPORTED","support":["FCT-003","FCT-005"]}
CAU-003 | {"cause":"Bennes dediees, filieres REP, decheteries pros et interdiction des tontes","effect":"Premiere baisse des tonnages decheterie en 15 ans (2021->2023, -11%)","mechanism":"Rapport 5.1: ralentissement consommation + benne DEA + reprise gratuite inertes + interdiction tontes (-15 a -25% localement)","status":"SUPPORTED","support":["FCT-006","FCT-007"]}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:2|FETCH:3|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND | runtime | warm-route-none | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | OK | - | - | ADEME enquete collecte 2023 résultats PDF encombrants déchèterie ventilation flux
QRY-002 | FETCH | INSPECTED | SRC-001 | https://librairie.ademe.fr/economie-circulaire-et-dechets/8644-la-collecte-des-dechets-par-le-service-public-en-france.html | rapport enquete collecte 2023 telechargement
QRY-003 | FETCH | INSPECTED | SRC-002 | https://librairie.ademe.fr/index.php?controller=attachment&id_attachment=7907 | rapport PDF collecte 2023 2,79 Mo inspecte pdftotext
QRY-004 | FETCH | INSPECTED | SRC-003 | https://librairie.ademe.fr/index.php?controller=attachment&id_attachment=7915 | synthese resultats cles collecte 2023 PDF
QRY-005 | WEB | OK | - | - | ADEME collecte 2023 14 644 kt déchèterie 214 kg 225 kg OMR 117 kg

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://librairie.ademe.fr/economie-circulaire-et-dechets/8644-la-collecte-des-dechets-par-le-service-public-en-france.html
SRC-002 | ◈ | fam:A | https://librairie.ademe.fr/index.php?controller=attachment&id_attachment=7907
SRC-003 | ◈ | fam:A | https://librairie.ademe.fr/index.php?controller=attachment&id_attachment=7915

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://librairie.ademe.fr/index.php?controller=attachment&id_attachment=7907 | A | 2025-05-01 | DMA SPGD 2023 37,8 Mt: OMR 15 198 kt, CS 7 924 kt, decheteries 14 474 kt | Rapport ADEME enquete collecte 2023 (publie mai 2025, donnees 2023, INSPECTE): 37,8 Mt DMA SPGD, 559 kg/hab (-8,6% vs 2021). Repartition: OMR 15 198 kt (225 kg/hab), collectes separees hors decheteries 7 924 kt (117 kg/hab), decheteries 14 474 kt (214 kg/hab). La decheterie = 38% du tonnage SPGD 2023. | 3f0de648-1c9e-4c7d-a2a3-614cf7fca12c
FCT-002 | FACT | ✧ | https://librairie.ademe.fr/index.php?controller=attachment&id_attachment=7907 | A | 2025-05-01 | Collectes separees hors decheteries par flux 2023 (Tableau 6) | Tableau 6 du rapport (collectes separees hors decheteries, 2023): emballages et papiers 3,5 Mt (52,1 kg/hab), verre 2,2 Mt (32,6 kg/hab), biodéchets 1,1 Mt (16,8 kg/hab), ENCOMBRANTS 0,5 Mt (7,7 kg/hab), dechets dangereux <0,01 Mt, autres (textiles...) 0,5 Mt (7,9 kg/hab). Total 7,9 Mt (117 kg/hab). | 495a7162-3e6f-487e-a4e1-8593c7bb7cd6
FCT-003 | FACT | ✧ | https://librairie.ademe.fr/index.php?controller=attachment&id_attachment=7907 | A | 2025-05-01 | Decheterie par flux 2023 (Tableau 10/54) | Tableau 10 du rapport (DMA SPGD en decheterie par flux, 2023): dechets verts 4 148 kt (63 kg/hab), deblais et gravats 3 746 kt (58,5 kg/hab), encombrants/tout-venant 2 978 kt (46 kg/hab), dechets tries par materiaux 2 144 kt (33 kg/hab), DEA mobilier 974 kt (16 kg/hab), DEEE 435 kt (7 kg/hab), dechets dangereux 130 kt (2 kg/hab), autres 66 kt. Total 14 644 kt (220 kg/hab desservi; 216 avec gravats). | 087b25ef-479f-4351-ab72-966a681674ee
FCT-004 | FACT | ✧ | https://librairie.ademe.fr/index.php?controller=attachment&id_attachment=7907 | A | 2025-05-01 | Ratio PAP vs decheterie encombrants 2023: 0,5 Mt vs 3 952 kt | CROISEMENT Tableaux 6 et 10: en 2023, les encombrants collectes en porte-a-porte/apport volontaire = 0,5 Mt (7,7 kg/hab) vs encombrants+DEA en decheterie = 3 952 kt (2 978+974, ~62 kg/hab). Ratio ~8:1 au profit de la decheterie. En 2021: encombrants+DEA decheterie = 4 558 kt vs PAP 0,7 Mt. La decheterie est l'exutoire quasi-exclusif des encombrants. | 98ffd22e-68fb-4916-a21c-954d0da51d24
FCT-005 | FACT | ✧ | https://librairie.ademe.fr/index.php?controller=attachment&id_attachment=7907 | A | 2025-05-01 | Verts et gravats: exutoire quasi-exclusif = decheterie | CROISEMENT: dechets verts - biodéchets collectes separement 1,1 Mt (dont verts d'entretien parcs) vs 4 148 kt en decheterie (63 kg/hab) = ratio ~4:1 decheterie. Deblais et gravats: 3 746 kt en decheterie, ABSENTS des collectes separees (Tableau 6 ne les liste pas) - exutoire exclusif decheterie. Le rapport note l'interdiction des apports de tonte qui commence a s'instaurer (-15 a -25% localement). | 40fa2c20-40f8-470a-85c7-74778fc02507
FCT-006 | FACT | ✧ | https://librairie.ademe.fr/index.php?controller=attachment&id_attachment=7907 | A | 2025-05-01 | Decheterie 2021->2023: 16 440 -> 14 644 kt, premiere baisse | Rapport 5.1: apres une hausse de 15 ans, les tonnages decheterie baissent pour la premiere fois: 16 440 kt (2021) -> 14 644 kt (2023), retour aux niveaux 2017/2019. Parc stable: 4 609 decheteries en 2023 (peu de variation depuis 2017). Hors deblais et gravats: 164 kg/hab (216 avec). Benne DEA dediee: encombrants+DEA 3 952 kt en 2023 vs 4 558 kt en 2021 (DEA = ~7% des flux 2023, 974 kt). | 084e872f-85a9-4daa-b797-68327238544e
FCT-007 | FACT | ✧ | https://librairie.ademe.fr/index.php?controller=attachment&id_attachment=7907 | A | 2025-05-01 | Sortie decheterie 2023: 70% valorisation, 22% stockage | Rapport 5.3: en sortie de decheterie 2023, 44% valorisation matiere (hors organique) + 26% valorisation organique = 70% vers valorisation (en hausse); stockage 25% (2021) -> 22% (2023). Materiaux tries en decheterie: bois 55% (1 167 kt, 19,6 kg/hab), metaux 24% (507 kt), papiers-cartons 19% (410 kt), plastiques/textiles 1%. | b29d1fa3-24ac-4733-b581-6a68b2284ccf
FCT-008 | FACT | ✧ | https://librairie.ademe.fr/index.php?controller=attachment&id_attachment=7907 | A | 2025-05-01 | Ratios decheterie: 66 kg/hab urbain dense vs ~240 kg/hab rural | Rapport 5.1: hors deblais et gravats, les ratios varient fortement par typologie d'habitat: 66 kg/hab en urbain dense a ~240 kg/hab en zones rurales et mixtes a dominante rurale. Paris n'a pas de decheterie. Les zones touristiques ont les ratios les plus eleves (sauf touristiques urbaines). | 840fdb2b-f401-46b0-b2a1-09b44533a57e
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-002
FCT-002 | SRC-002
FCT-003 | SRC-002
FCT-004 | SRC-002
FCT-005 | SRC-002
FCT-006 | SRC-002
FCT-007 | SRC-002
FCT-008 | SRC-002

## REFUTATION_REGISTRY_V1

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE
FCT-008 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -
FCT-007 | WRITE | -
FCT-008 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-31T07:55:29.956437+00:00","fact_mem":{"FCT-001":"3f0de648-1c9e-4c7d-a2a3-614cf7fca12c","FCT-002":"495a7162-3e6f-487e-a4e1-8593c7bb7cd6","FCT-003":"087b25ef-479f-4351-ab72-966a681674ee","FCT-004":"98ffd22e-68fb-4916-a21c-954d0da51d24","FCT-005":"40fa2c20-40f8-470a-85c7-74778fc02507","FCT-006":"084e872f-85a9-4daa-b797-68327238544e","FCT-007":"b29d1fa3-24ac-4733-b581-6a68b2284ccf","FCT-008":"840fdb2b-f401-46b0-b2a1-09b44533a57e"},"mnemo_row":"WROTE:pending","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-008","reason":"NONE","success":1}],"writeback_row":{"attempted":8,"blocked":0,"eligible":8,"failure":0,"success":8}}

PERSISTENCE_META: MNEMO_ROW:WROTE:pending | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:8;attempted:8;success:8;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[8 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-008 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
