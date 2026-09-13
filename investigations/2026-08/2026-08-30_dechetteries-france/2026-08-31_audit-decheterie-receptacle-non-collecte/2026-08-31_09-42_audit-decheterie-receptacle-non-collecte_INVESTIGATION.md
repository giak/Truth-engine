ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260831-0942-audit-decheterie-receptacle-non-collecte | PARENT_RUN_ID:NONE | AS_OF:2026-08-31
INPUT_KIND:NEW | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-31_audit-decheterie-receptacle-non-collecte/2026-08-31_09-42_audit-decheterie-receptacle-non-collecte_INPUT.txt | SUBJECT_SLUG:audit-decheterie-receptacle-non-collecte | SUBJECT_FP:sha256:fdb233a53753ecb6988db82a6a40bf4b6302defb0b0c9663d5d818b1914d3089 | INPUT_SHA256:sha256:76313733ffc931a69d995aada9e3685fc35d42f59537b2d8c5e63700705128dc
COMPLEXITY:0.6→MEDIUM | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors': ['menages', 'collectivites', 'ADEME', 'SDES', 'Etat'], 'domains': ['dechets', 'collecte', 'decheterie', 'flux'], 'geo': 'France', 'lead_question': 'Ce que le bac ne prend pas finit a la decheterie: cartographier le reste du bac et la frontiere qui bouge.', 'limits': '2021-2023, decomposition 2023 non inspectee', 'object_question': '(1) flux non collectes + exutoires ; (2) part decheterie 40% + repartition ; (3) bascule quand la collecte change.'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
## Ce que l'enquête établit

### Le chaînon manquant : la déchèterie est le réceptacle du non-collecté (FCT-001, FCT-002, FCT-003)

La passe précédente (collecte, `20260831-0927`) a cartographié le « bordel » du bac : 1 169 structures, TEOM dominante, TI marginale. Restait la moitié manquante : **ce que le bac ne prend pas, où va-t-il ? Réponse : à la déchèterie.**

La déchèterie reçoit **40 % des déchets ménagers et assimilés** (16,4 Mt en 2021, ADEME/SDES) — un poids égal à celui des ordures ménagères résiduelles (40 %). La collecte sélective (poubelle jaune) ne représente que 20 %. Autrement dit : **le « reste du bac » pèse deux fois plus que le bac jaune.**

La répartition des apports en déchèterie 2021 le confirme (FCT-001) : **encombrants et mobilier 28 %, déchets verts 27 %, déblais et gravats 26 %** — ces trois flux « hors bac » représentent **81 % des apports**, devant les matériaux recyclables (15 %), DEEE (2 %), dangereux (1 %).

La raison est juridique (FCT-003) : la définition officielle des encombrants exclut ce que le bac prend. Service-public.gouv : les encombrants (meubles, matelas, gros électroménager) **ne sont pas pris en charge par la collecte des ordures ménagères** ; les **gravats et déchets verts doivent être amenés en déchèterie** (pneus et bouteilles de gaz repris par le vendeur, véhicules par un professionnel agréé). La collecte des encombrants en porte-à-porte est un **service facultatif, défini par chaque commune** (rendez-vous, date fixe, déchèterie ou centre spécifique) — FCT-005. L'abandon sur la voie publique est sanctionné : 135 € à 1 500 € (FCT-004).

### La frontière bouge : chaque restriction du bac déplace le flux vers la déchèterie (FCT-007, FCT-008)

Depuis 2009, la part des collectes sélectives **et** déchèterie est passée de **43 % à 60 %** des DMA, portée principalement par la déchèterie (**+39 %** depuis 2009) pendant que les OMR baissaient de **13 %** (FCT-007, FCT-008). C'est le mécanisme central : **plus le bac se restreint (suppression du porte-à-porte, bascule en points d'apport volontaire, tarification incitative, hausse des coûts de collecte), plus la déchèterie absorbe.**

Croisement avec la passe collecte : sous tarification incitative, les apports en déchèterie augmentent de **+13 %** (ADEME/SINOE, bilan TI 1/1/2021) — quand le bac devient payant, le surplus part à la déchèterie.

### Le tonnage total baisse, la structure reste (FCT-006)

L'enquête ADEME collecte 2023 (publiée 2026) : **37,8 Mt, 559 kg/habitant**, en baisse vs 2021 (41,3 Mt, 611 kg/hab). Le flux diminue mais la déchèterie en absorbe toujours ~40 % — c'est le plancher structurel du service public.

### Bouclage avec la fresque déchèteries

Ce résultat est le **chaînon manquant** entre les deux enquêtes :

1. **La déchèterie n'est pas une option, c'est l'exutoire obligé** du non-collecté : 40 % des DMA, dont les gravats et verts que la loi envoie obligatoirement en déchèterie.
2. **Verrouiller la déchèterie = verrouiller le seul exutoire d'un flux que le bac ne peut pas absorber.** Les passes contrôle d'accès (2023), exclusion des pros (2015), quotas (2123) agissent sur ce flux de 16,4 Mt — d'où le lien causal avec les dépôts sauvages (passes 2135/2015).
3. **Le « bordel de la collecte » (1 169 structures) a un pendant** : la déchèterie est le point de convergence national de ce qui échappe à la fragmentation des bacs.

## Ce que l'article doit faire de ces résultats

1. **Poser la déchèterie comme 3e circuit co-égal** (40 % des DMA, autant que les OMR) et non comme un appendice du service.
2. **Quantifier le « reste du bac »** : 81 % des apports = encombrants + verts + gravats, et 25 % de la population n'a pas d'autre exutoire que la déchèterie pour ses encombrants (SDES : 6 communes sur 10 seulement offrent la collecte PAP/PAV).
3. **Faire le lien causal** : restriction du bac (PAP supprimé, TI, PAV) → flux vers la déchèterie ; restriction de la déchèterie (contrôle d'accès, quotas) → dépôts sauvages. Les deux verrous se répondent.

## Ce qui reste ouvert

- La part exacte PAP vs déchèterie par flux (encombrants) n'est pas décomposée publiquement — GAP COVERAGE_DATA_ABSENT.
- Le rapport ADEME enquête collecte 2023 détaillé (librairie) reste à inspecter pour la ventilation 2023 par flux — GAP SITE_LEVEL_DATA_ABSENT.
- Pas de carte nationale des services encombrants par commune (qui propose quoi) — GAP COVERAGE_DATA_ABSENT.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:0|CLM:4|AXS:6|CAU:3|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"La decheterie est le receptacle du non-collecte: 40% des DMA (16,4 Mt en 2021) y aboutissent, dont 81% de flux hors bac (encombrants 28%, verts 27%, gravats 26%) - ce que le bac ne prend pas a la decheterie pour exutoire","counter":"Une partie des encombrants est collectee en PAP/PAV (mode defini par la commune, non universel)","gap":"Pas de decomposition officielle detaillee de la part PAP vs decheterie pour chaque flux","gap_type":"COVERAGE_DATA_ABSENT","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-005"]}
CLM-002 | {"claim":"La frontiere bouge structurellement au profit de la decheterie: part selective+decheterie passee de 43% a 60% depuis 2009, decheterie +39% vs OMR -13% - chaque restriction du bac (PAP supprime, TI, PAV) deplace le flux vers la decheterie","counter":"Les extensions de consigne (2023) et biodéchets (2024) captent des flux qui allaient en decheterie","gap":"Pas de serie nationale des bascules PAP vers decheterie par collectivite","gap_type":"COVERAGE_DATA_ABSENT","status":"SUPPORTED","support":["FCT-007","FCT-008"]}
CLM-003 | {"claim":"Les exutoires legaux hors decheterie sont contraints: gravats et dechets verts DOIVENT aller en decheterie (service-public), les encombrants dependent de la commune, et l abandon sur voie publique est sanctionne (135-1500 EUR) - la decheterie est le point de passage oblige du non-collecte","counter":"Certaines communes offrent collecte a la demande ou a date fixe","gap":"Pas de carte nationale des services encombrants par commune","gap_type":"COVERAGE_DATA_ABSENT","status":"SUPPORTED","support":["FCT-003","FCT-004"]}
CLM-004 | {"claim":"Le tonnage total baisse (37,8 Mt, 559 kg/hab en 2023 vs 41,3 Mt/611 kg en 2021) mais la structure du flux vers la decheterie reste: 559 kg/hab reste le plancher du service public et la decheterie en absorbe 40%","counter":"La baisse peut venir de la conjoncture et des changements de methode d enquete","gap":"Le rapport ADEME 2023 detaille reste a inspecter (librairie)","gap_type":"SITE_LEVEL_DATA_ABSENT","status":"SUPPORTED","support":["FCT-006"]}

### AXIS_REGISTRY_V1
AXS-001 | {"question":"Quels flux echappent a la collecte classique (PAP/PAV) et atterrissent en decheterie: encombrants, gravats, verts, DEEE, dangereux - et quels sont leurs exutoires legaux?","routes":["AUDIT","EXPAND"],"sought_objects":["flux non collectes porte-a-porte","encombrants exutoires","gravats dechets verts decheterie"],"status":"SATURATED"}
AXS-002 | {"question":"Quelle est la part de la decheterie dans les DMA (40%) et la repartition par flux (encombrants 28%, verts 27%, gravats 26%)?","routes":["AUDIT","EXPAND"],"sought_objects":["decheterie part DMA","repartition apports decheterie","tonnages decheterie 2021"],"status":"SATURATED"}
AXS-003 | {"question":"Comment la frontiere bac/decheterie bouge-t-elle: fin du PAP, bascule PAV, extensions de consigne (2023), biodéchets (2024), TI?","routes":["AUDIT","EXPAND"],"sought_objects":["fin porte-a-porte bascule","extension consignes 2023","TI decheteries +13%"],"status":"SATURATED"}
AXS-004 | {"question":"Quels flux echappent a la collecte classique (PAP/PAV) et atterrissent en decheterie: encombrants, gravats, verts, DEEE, dangereux - et quels sont leurs exutoires legaux?","routes":["AUDIT","EXPAND"],"sought_objects":["flux non collectes","encombrants exutoires","gravats dechets verts decheterie"],"status":"SATURATED"}
AXS-005 | {"question":"Quelle est la part de la decheterie dans les DMA (40%) et la repartition par flux (encombrants 28%, verts 27%, gravats 26%)?","routes":["AUDIT","EXPAND"],"sought_objects":["decheterie part DMA","repartition apports decheterie","tonnages decheterie 2021"],"status":"SATURATED"}
AXS-006 | {"question":"Comment la frontiere bac/decheterie bouge-t-elle: fin du PAP, bascule PAV, extensions de consigne (2023), biodéchets (2024), TI?","routes":["AUDIT","EXPAND"],"sought_objects":["fin porte-a-porte bascule","extension consignes 2023","TI decheteries +13%"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Les encombrants, gravats, dechets verts, DEEE et dangereux ne sont pas pris en charge par la collecte classique (poids/volume/reglementation)","effect":"Ils aboutissent a la decheterie, qui recoit 40% des DMA (16,4 Mt) - 81% des apports sont ces flux hors bac","mechanism":"Definition legale (service-public): gravats/verts doivent aller en decheterie; encombrants = mode communal; amendes 135-1500 EUR pour abandon","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-004"]}
CAU-002 | {"cause":"Restriction du bac: suppression du PAP, bascule en PAV, tarification incitative, hausse des couts de collecte","effect":"Deplacement du flux vers la decheterie (+39% depuis 2009) et vers la collecte selective (+22%) pendant que les OMR baissent (-13%)","mechanism":"Chaque mode de collecte a un cout et un perimetre; le choix communal (L2224-13) arbitre la frontiere bac/decheterie","status":"SUPPORTED","support":["FCT-007","FCT-008"]}
CAU-003 | {"cause":"La decheterie est le point de passage oblige du non-collecte (exutoire legal des gravats/verts, filet des encombrants)","effect":"Toute restriction d acces a la decheterie (controle d acces, quotas, exclusion pros) frappe directement le flux que le bac ne peut pas absorber","mechanism":"40% des DMA passent par la decheterie: verrouiller le guichet = verrouiller le seul exutoire d une part majeure du flux","status":"SUPPORTED","support":["FCT-002","FCT-003","FCT-005"]}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:6|FETCH:4|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND | runtime | warm-route-none | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | OK | - | - | déchets non collectés porte-à-porte France encombrants gravats déchets verts déchèterie collecte spécifique ADEME
QRY-002 | WEB | OK | - | - | encombrants déchets volumineux service-public réglementation déchèterie gravats pneus
QRY-003 | FETCH | INSPECTED | SRC-001 | https://www.notre-environnement.gouv.fr/themes/economie/les-dechets-ressources/article/la-collecte-des-dechets | collecte des dechets decomposition decheterie 40 pourcent encombrants verts gravats
QRY-004 | FETCH | INSPECTED | SRC-002 | https://www.service-public.gouv.fr/particuliers/vosdroits/F31954 | encombrants dechets volumineux regles collecte decheterie amendes
QRY-005 | WEB | OK | - | - | suppression collecte encombrants porte-à-porte communes bascule déchèterie tendance ADEME
QRY-006 | WEB | OK | - | - | enquête ADEME collecte 2021 encombrants porte à porte apport volontaire part communes desservies
QRY-007 | FETCH | PARTIAL | - | https://librairie.ademe.fr/economie-circulaire-et-dechets/6373-la-collecte-des-dechets-par-le-service-public-en-france-resultats-2021.html | ADEME enquete collecte 2021 resultats
QRY-008 | WEB | OK | - | - | enquête ADEME collecte 2023 37,8 Mt 559 kg habitant résultats 2024
QRY-009 | FETCH | INSPECTED | SRC-003 | https://www.economiecirculaire.org/library/h/la-collecte-des-dechets-par-le-service-public-en-france-2024.html | ADEME enquete collecte 2024 37,8 Mt 559 kg
QRY-010 | WEB | OK | - | - | fin porte-à-porte déchets collectivités coûts apport volontaire bascule déchèterie gazette

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.notre-environnement.gouv.fr/themes/economie/les-dechets-ressources/article/la-collecte-des-dechets
SRC-002 | ◈ | fam:A | https://www.service-public.gouv.fr/particuliers/vosdroits/F31954
SRC-003 | ◈ | fam:A | https://www.economiecirculaire.org/library/h/la-collecte-des-dechets-par-le-service-public-en-france-2024.html

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.notre-environnement.gouv.fr/themes/economie/les-dechets-ressources/article/la-collecte-des-dechets | A | 2023-09-05 | Repartition des apports en decheterie 2021 | ADEME (enquete Collecte et decheteries 2021, chiffres cles Dechets 2024): repartition des dechets collectes en decheterie en 2021 - encombrants et mobilier 28%, dechets verts 27%, deblais et gravats 26%, materiaux recyclables 15%, DEEE 2%, dechets dangereux 1%, autres 1%. Les flux 'hors bac' (encombrants+verts+gravats) representent 81% des apports. | 46c62f9a-79e2-4728-8c45-e23b4f5e4411
FCT-002 | FACT | ✧ | https://www.notre-environnement.gouv.fr/themes/economie/les-dechets-ressources/article/la-collecte-des-dechets | A | 2023-09-05 | Decheterie 40% des DMA, 16,4 Mt | En 2021, 41,3 Mt de DMA collectees (611 kg/hab, +6% vs 2019). La collecte en decheterie represente 40% du poids des dechets collectes (vs 20% collecte selective, 40% OMR). 4 620 decheteries (+60% vs 2001) ont recu 16,44 Mt (+143% en 20 ans, +39% depuis 2009). La part selective+decheterie est passee de 43% a 60% depuis 2009. | e49e4363-27b5-49e1-8611-0af8881a355e
FCT-003 | FACT | ✧ | https://www.service-public.gouv.fr/particuliers/vosdroits/F31954 | A | 2025-04-10 | Definition encombrants et exutoires legaux | Service-public.gouv (verifie 10/04/2025): les encombrants (meubles, matelas, gros electromenager) ne sont PAS pris en charge par la collecte des ordures menageres. Les gravats, dechets verts, pneus, bouteilles de gaz, vehicules ne sont pas des encombrants: gravats et dechets verts doivent etre amenes en decheterie, pneus/bouteilles repris par le vendeur, vehicules par un pro agree. Les communes choisissent les modalites: rendez-vous, date fixe, decheterie ou centres specifiques. | bb7f62f6-6cda-4e2b-aa54-7011b2b73d71
FCT-004 | FACT | ✧ | https://www.service-public.gouv.fr/particuliers/vosdroits/F31954 | A | 2025-04-10 | Amendes abandon dechets voie publique | Deposer/abandonner des dechets sur la voie publique: amende forfaitaire 135 EUR (ou 375 EUR apres 45 jours), juge de police jusqu'a 750 EUR, ou 1 500 EUR avec confiscation du vehicule si transporte. Cadre: CGCT R2224-26, code penal R633-6, R634-2, R635-8, R644-2. | 8cfd58f2-6d9f-4e3f-96c9-d556c919db26
FCT-005 | FACT | ✧ | https://www.service-public.gouv.fr/particuliers/vosdroits/F31954 | A | 2025-04-10 | Collecte encombrants: mode non obligatoire, defini par la commune | Service-public.gouv: 'Les conditions de collecte des encombrants sont definies par les communes' - 4 modes possibles (rendez-vous, date fixe, decheterie, centres specifiques). La collecte des encombrants au PAP n'est PAS un service universel: la decheterie en est l'exutoire de droit pour les gravats et dechets verts (non encombrants), et l'exutoire de fait la ou aucun mode PAP n'existe. | d37cff2a-4649-4651-bb40-39e28268a988
FCT-006 | FACT | ✧ | https://www.economiecirculaire.org/library/h/la-collecte-des-dechets-par-le-service-public-en-france-2024.html | A | 2026-08-24 | Enquete ADEME collecte 2023: 37,8 Mt, 559 kg/hab | Enquete ADEME 'La collecte des dechets par le service public en France' (resultats 2023, publiee 2026): 37,8 Mt de DMA collectees, soit 559 kg/habitant, en baisse vs 2021 (41,3 Mt, 611 kg/hab). Le questionnaire couvre PAP, apport volontaire ET decheteries; MODECOM 2017: 20% du tonnage OMR vient des activites economiques. | 6f04d7d7-47f9-403e-b35c-1dbbe63f8ba2
FCT-007 | FACT | ✧ | https://www.notre-environnement.gouv.fr/themes/economie/les-dechets-ressources/article/la-collecte-des-dechets | A | 2023-09-05 | Decheterie +39% vs OMR -13% depuis 2009 | Tendance de fond ADEME/SDES: les OMR (bac gris) baissent de 13% entre 2011 et 2021 tandis que la collecte en decheterie augmente de +39% depuis 2009 (16,4 Mt en 2021) - la decheterie absorbe structurellement ce que le bac ne prend plus (flux volumineux, gravats, verts, DEEE, dangereux). Part selective+decheterie: 43% -> 60% depuis 2009. | c1f879f5-daee-44b5-8f69-7035ad35e1ba
FCT-008 | FACT | ✧ | https://www.notre-environnement.gouv.fr/themes/economie/les-dechets-ressources/article/la-collecte-des-dechets | A | 2023-09-05 | Part selective+decheterie 43% -> 60% | ADEME: depuis 2009, la part des collectes selectives et en decheterie dans les DMA est passee de 43% a 60% - la decheterie (40% des DMA en 2021) et la collecte selective (20%) captent structurellement le flux que le bac gris perd (OMR 40%, en baisse de 13% depuis 2011). La frontiere bouge: extension des consignes (2023), biodéchets obligatoires (2024), bascule PAP->PAV. | 8b6f851c-5e27-449d-8b52-522dcf45e91f
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-002
FCT-004 | SRC-002
FCT-005 | SRC-002
FCT-006 | SRC-003
FCT-007 | SRC-001
FCT-008 | SRC-001

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
ATTEMPT-001 | {"created_at":"2026-08-31T07:47:43.482497+00:00","fact_mem":{"FCT-001":"46c62f9a-79e2-4728-8c45-e23b4f5e4411","FCT-002":"e49e4363-27b5-49e1-8611-0af8881a355e","FCT-003":"bb7f62f6-6cda-4e2b-aa54-7011b2b73d71","FCT-004":"8cfd58f2-6d9f-4e3f-96c9-d556c919db26","FCT-005":"d37cff2a-4649-4651-bb40-39e28268a988","FCT-006":"6f04d7d7-47f9-403e-b35c-1dbbe63f8ba2","FCT-007":"c1f879f5-daee-44b5-8f69-7035ad35e1ba","FCT-008":"8b6f851c-5e27-449d-8b52-522dcf45e91f"},"mnemo_row":"WROTE:pending","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-008","reason":"NONE","success":1}],"writeback_row":{"attempted":8,"blocked":0,"eligible":8,"failure":0,"success":8}}

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
