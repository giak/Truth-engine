ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-0904-dechetteries-france | PARENT_RUN_ID:NONE | AS_OF:2026-08-30
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_09-04_dechetteries-france_INPUT.txt | SUBJECT_SLUG:dechetteries-france | SUBJECT_FP:sha256:aa54ac123f4837a8dc4140e5b38015ebd10e46310c23a66b3adcdb34bbf9a240 | INPUT_SHA256:sha256:aa54ac123f4837a8dc4140e5b38015ebd10e46310c23a66b3adcdb34bbf9a240
COMPLEXITY:7→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['ADEME', 'SINOE', 'collectivites', 'ecoorganismes-REP', 'ministere-ecologie', 'CEREMA', 'GIZC'], 'domains': ['dechets-menagers', 'reglementation-environnement', 'rep', 'collectivites-territoriales'], 'exclusions': ['dechetteries professionnelles-hors-flux-menagers', 'sites-particuliers-detailles'], 'geo': 'France métropolitaine et collectivités', 'lead_question': 'N/A(NO_INPUT_LEAD)', 'limits': ['donnees nationales SINOE partielles selon territoire', 'acces paywall/403 possibles'], 'object_question': 'Quel est l’état et la gouvernance du réseau des déchetteries en France (2026) : nombre/répartition, cadre réglementaire d’accès et de dépôt, financement et éco-organismes REP, et quels sont les écarts avérés (dépôts sauvages, restriction d’accès, non-conformité) ?', 'period': '2020-2026'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Investigation — Déchèteries en France : réseau, réglementation et financement

## RÉSUMÉ EXÉCUTIF

Cette investigation porte sur l'état et la gouvernance du réseau français des déchèteries, traitée comme un objet d'investigation (INPUT_KIND=TOPIC, MISSION_MODE=INVESTIGATION). Le lead fourni étant un thème sans source matérielle, LEAD_QUESTION=N/A(NO_INPUT_LEAD) et l'audit de source est N/A ; l'OBJECT_QUESTION est traité prioritairement.

Faits établis (tous **✧ PROBABLE**, famille de provenance unique — principalement officielle) :

1. **Rôle des déchèteries dans le circuit de collecte** (FCT-001) : en 2021, environ 40 % du tonnage des déchets ménagers et assimilés (DMA) collectés par le service public est issu des dépôts en déchèterie (≈242 kg/hab sur 615 kg/hab). Sources : Insee Première n°2055 (juin 2025, SRC-001) et notre-environnement.gouv.fr (MTECT, SRC-002), ADEME (SRC-006). Corroboration AO official single family → ✧.
2. **Financement** (FCT-002) : en 2023, 22,0 Md€ consacrés à la gestion des déchets en France, dont 63 % (13,9 Md€) pour le service public (SPGD), financé surtout par la TEOM (8,9 Md€) et la REOM (0,9 Md€). Source : SDES (SRC-004). Trajectoire cohérente avec 21,6 Md€ en 2022 (presse reprenant SDES) → ✧.
3. **Cadre réglementaire** (FCT-003) : les déchèteries sont des installations classées (ICPE) de la rubrique 2710, dont le régime a été refondu par le décret n°2012-384 du 20/03/2012 (classification par volumes, régime d'enregistrement), avec prescriptions générales fixées par les arrêtés du 27/03/2012 (registre des déchets sortants, réception des déchets dangereux, contrôle périodique). Source : Enviroveille / CCI France (SRC-003). Texte officiel (Légifrance) inaccessible au bot (403 head-blocked) → source unique non-officielle → ✧.
4. **Accès des professionnels** (FCT-005) : la réglementation permet l'accès des artisans, commerçants et PME aux déchèteries, mais la décision d'accepter et les conditions (notamment tarifaires) relèvent du gestionnaire. Source : Enviroveille / CCI France (SRC-003) → ✧.
5. **Dépôts sauvages** (FCT-004) : le coût national de résorption des dépôts sauvages est estimé entre 30 et 90 M€ par an (Cerema, 2024). Source : ARBE Région Sud (SRC-005) → ✧.

**Gap principal** (CLM-005, AXS-001/007) : le **nombre exact de déchèteries ouvertes en France** n'a pas pu être ancré à une source inspectée dans cette passe. Les rapports ADEME (« La collecte des déchets par le service public ») sont illisibles au bot (aucun texte extractible), et l'annuaire SINOE (data.ademe.fr) agrège des enregistrements historiques cumulés sans total courant d'ouverture lisible. Ce gap est déclaré GAP_TYPE=INDEPENDENCE/SCOPE, non un refus du fait que le réseau est dense et central.

**Conclusion bornée** : en l'état, l'investigation établit (✧) le rôle structurant des déchèteries dans la collecte des DMA, leur encadrement ICPE, leur financement via le SPGD/TEOM et le coût des dépôts sauvages ; mais elle laisse ouvert, par honnêteté forensique, la question du décompte exact du maillage national. Aucune conclusion ne dépasse la force des preuves ; aucune inférence n'est présentée comme fait.

## CHRONOLOGIE

- **2005–…** : enquêtes bisannuelles « Collecte » coordonnées par l'ADEME auprès des EPCI compétents (domaine déchets) ; données consolidées dans SINOE (SRC-001, SRC-002).
- **20/03/2012** : décret n°2012-384 modifiant la nomenclature des ICPE ; la rubrique 2710 est reclassifiée par volumes présents (dangereux / non dangereux) et gagne un régime d'enregistrement (SRC-003).
- **27/03/2012** : arrêtés de prescriptions générales applicables aux installations de collecte (2710-1 et 2710-2) : clôture, réception des déchets dangereux par personnel habilité, registre des déchets sortants, contrôle périodique (SRC-003).
- **2021** : enquête Collecte 2021 ; les déchèteries concentrent ≈40 % du tonnage DMA collecté (≈242 kg/hab), Δ +65 kg/hab de tri sur 10 ans (SRC-001, SRC-002).
- **2023** : dépense intérieure de gestion des déchets = 22,0 Md€, dont 63 % pour le SPGD (13,9 Md€) ; TEOM 8,9 Md€, REOM 0,9 Md€ (SRC-004). 37 Mt de DMA collectées en métropole (SRC-006).
- **2024** : Cerema actualise l'estimation du coût de résorption des dépôts sauvages : 30–90 M€/an (SRC-005). Tri à la source des biodéchets généralisé au 01/01/2024.
- **19/12/2025** : communiqué ADEME MODECOM® 2024 : les déchèteries « jouent un rôle central » ; ~75 % du Tout-Venant en déchèterie relèverait de filières REP (SRC-006).

## DOMAINES

Présentation par axes d'investigation (INVESTIGATION_MAP en CARTE DES PREUVES).

### D1. Mécanismes de collecte / rôle des déchèteries (AXS-005, SATURATED)
FCT-001 établit qu'en 2021 la moitié environ des déchets triés des ménages passe par les déchèteries et colonnes d'apport volontaire, et que 40 % du tonnage DMA provient des dépôts en déchèterie (≈242 kg/hab). Les flux les plus concentrés : encombrants (88 %), déblais/gravats (99 %), déchets dangereux (69 %), déchets verts et biodéchets (78 %) (SRC-001). La déchèterie est donc non un site annexe mais un maillon central du tri des encombrants et déchets occasionnels.

### D2. Règles et contrôles (AXS-002, SATURATED)
FCT-003 et FCT-005 : cadre ICPE rubrique 2710, classement quantitatif (décret 2012-384), prescriptions des arrêtés du 27/03/2012, registre des déchets sortants, et liberté du gestionnaire sur l'accès des professionnels. Limite : le texte officiel (Légifrance) est en 403 au bot → source juriste/technique de second rang, d'où tier ✧ et non ✦.

### D3. Ressources / financement (AXS-004, SATURATED)
FCT-002 : la gestion des déchets mobilise 22,0 Md€ (2023), 63 % via le SPGD (13,9 Md€), principalement TEOM (8,9 Md€) + REOM (0,9 Md€) ; financement incidents : entreprises 41 %, ménages 35 %, administrations 24 %. La TEOM étant assise sur le foncier, les collectivités financent le réseau indépendamment des volumes déposés — un point à vérifier dans une passe ultérieure.

### D4. Acteurs (AXS-003, SATURATED)
Rôles : ADEME (opérateur national, enquêtes SINOE, centralisation des points d'apport REP), collectivités/EPCI (compétence et gestion des déchèteries), éco-organismes REP (alimentent les données), services de l'État (DREAL/DDT pour le contrôle ICPE). FCT-001 et SRC-006 (ADEME) étayent le rôle central de l'ADEME dans la donnée.

### D5. Impacts et écarts (AXS-006, SATURATED)
FCT-004 : coût national de résorption des dépôts sauvages estimé 30–90 M€/an (Cerema 2024). La restriction d'accès et le coût sont cités par les collectivités comme pistes aggravantes/préventives ; le lien causal n'est pas démontré (voir CHAÎNES).

### D6. Contro-hypothèses / maillage (AXS-007, GAP)
Le nombre exact de déchèteries ouvertes n'est pas établi (AXS-001/007 en GAP). Les données ouvertes (annuaire SINOE) sont cumulatives ; les rapports ADEME sont illisibles au bot. GAP_TYPE=INDEPENDENCE. Ceci borne — pas infirme — l'ampleur du réseau.

## RÉSEAU D'ACTEURS

ACTOR_NETWORK_MAP non peuplée en arêtes sourcées : l'investigation n'a pas établi de relations typées datées entre entités (pas de registre, procès-verbal ou contrat inspecté) au-delà du partage de données ADEME/éco-organismes (SRC-006). Cette absence est un gap explicite, non une présomption. RESOURCE_FLOW_MAP : chaîne de financement SPGD→collectivités (TEOM/REOM) et ADEME comme source de données consolidées (FCT-002, SRC-004).

## CHAÎNES / PELOTE

CAUSAL_ROUTE=OPTIONAL posée, résultat = CAUSALITY GAP (CAU-001). Aucune chaîne causale vérifiée : l'hypothèse « restriction d'accès / coût → dépôts sauvages » est documentée seulement comme piste de prévention par les collectivités (ARBE, FCT-004). COST_HARMS associés (30–90 M€) sont des estimations de résorption, pas une preuve de mécanisme causal. CORRELATION ≠ CAUSATION : le lien reste inexpliqué sans étude causale dédiée. Chaîne courte vérifiée préférée à une chaîne longue fabriquée : on s'arrête ici.

## CARTE DIALECTIQUE

- **P1 dominant/officiel** (ADEME, MTECT, SDES, Cerema) : le réseau des déchèteries fonctionne, progresse (tri +21 % en 10 ans) et s'affine avec la REP ; les déchèteries sont un levier de valorisation (SRC-001, SRC-002, SRC-004, SRC-006).
- **P2 critique/contradictoire** : les associations et collectivités signalent la persistance des dépôts sauvages (coût 30–90 M€/an), des marges de tri (69 % d'erreurs dans la poubelle grise) et un potentiel non capté (75 % du Tout-Venant relèverait de filières REP) (SRC-005, SRC-006).
- **P3 arbitrage par les preuves** : les deux perspectives reposent sur des données officielles compatibles ; la divergence porte sur l'interprétation (progrès vs gisement résiduel), pas sur des chiffres contradictoires. Aucune contradiction matérielle non résolue (CONTRADICTION_LEDGER vide). Poids inégal : les estimations de coût et de potentiel sont des ordres de grandeur, non des comptes.

## CARTE DES PREUVES

Voir ci-dessous les blocs machine émis par le runtime (registre des preuves, registre des faits, carte source→fait, registre des réfutations, plan de write-back, registres sémantiques LED/CLM/AXS/CAU, matrice de traçage, rapport EDI et journal des requêtes).

### LEAD_COVERAGE
LED-001 (rôle des déchèteries) → EXPAND → SATURATED (FCT-001). LED-002 (cadre réglementaire/gouvernance) → EXPAND → SATURATED (FCT-003, FCT-005). LED-003 (financement/impacts) → EXPAND → SATURATED (FCT-002, FCT-004). Aucune EXCLUDE : pas de lead hors périmètre.

### OBJECT_COVERAGE
L'OBJECT_QUESTION (état et gouvernance : réseau, réglementation, financement, écarts) est couvert par les axes RULES_CONTROLS/AXS-002, RESOURCES_FLOWS/AXS-004, MECHANISMS/AXS-005, IMPACT_RESPONSIBILITY/AXS-006. La dimension « nombre de sites » reste en GAP explicite (AXS-001/AXS-007). Pas de lead matériel laissé AUDIT-only.

### Fiabilité — notes
Tous les faits sont **✧ PROBABLE** (famille de provenance unique). Aucun ✦ : pour FCT-001/002/004 la famille est A (officielle) ; pour FCT-003/005 la famille est B (technique/juridique de second rang) car Légifrance est 403-blocked. La réfutation a cherché activement des contre-preuves (REFUTATION * , NONE trouvé) ; elle n'a pas trouvé de contradiction matérielle. TERM honnête : source unique → maximum ✧.

## PÉRIMÈTRE & LIMITES

- **Inclusions** : réseau national des déchèteries acceptant les DMA, cadre ICPE, financement SPGD, dépôts sauvages.
- **Exclusions** : déchèteries purement professionnelles hors flux ménagers ; sites détaillés cas par cas ; récit des filières REP par filière.
- **Limites d'accès** : Légifrance en 403 au bot ; rapports ADEME en librairie sans texte extractible ; donnée SINOE cumulative non exploitable pour un total courant ; pas de licence de données téléchargée dans cette passe.
- **Periode** : focus 2012–2026 avec ancrage statistique 2021 (tonnages) et 2023 (dépenses).
- **EDI** : corpus majoritairement officiel A (Insee, MTECT, SDES, ADEME, ARBE) + une source technique B (CCI France) ; pas de source dissidente, académique ou de terrain — pénalité MISSING_COUNTER et NO_DIRECT_EVIDENCE partielle. Le nombre de sites reste un point aveugle (GAP).

## AUDIT DU LEAD / SOURCE

N/A(NO_INPUT_LEAD) : le sujet « déchèteries en France » est un thème, sans document, claim ou URL fourni. Aucune source soumise à auditer ; les sources citées proviennent de la recherche objet.

## ÉTAT DES CONNAISSANCES

- **PROBABLE (✧)** : rôle des déchèteries dans 40 % du tonnage DMA (2021) ; dépense 22,0 Md€ / 63 % SPGD / TEOM 8,9 Md€ (2023) ; statut ICPE 2710 + décret 2012-384 + arrêtés 27/03/2012 ; accessibilité des professionnels relève du gestionnaire ; coût dépôts sauvages 30–90 M€/an (Cerema 2024).
- **UNKNOWN (GAP_TYPE=INDEPENDENCE)** : nombre exact de déchèteries ouvertes en France.
- **CAUSALITY GAP** : lien éventuel entre accès/coût et dépôts sauvages non démontré.
- Aucun fait REFUTE ; aucune contradiction matérielle non résolue.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:3|CLM:5|AXS:8|CAU:1|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_excerpt":"Thème objet dérivé du sujet : part du tonnage DMA via déchèterie et rôle du réseau (étayé par FCT-001).","kind":"OBJECT","lead":"Les déchèteries sont un maillon central de la collecte des déchets ménagers et assimilés en France (rôle dans le tonnage, rôle dans les flux).","linked_ids":["AXS-002","AXS-005","CLM-001"],"locator":"-","materiality":"DECISIVE","routes":["EXPAND"],"source_id":"-","status":"SATURATED"}
LED-002 | {"evidence_excerpt":"Thème objet dérivé du sujet : cadre ICPE 2710 et accès (étayé par FCT-003, FCT-005).","kind":"OBJECT","lead":"La gouvernance et le cadre réglementaire des déchèteries : statut ICPE (rubrique 2710), prescriptions, règles d accès particuliers/professionnels.","linked_ids":["AXS-002","AXS-003","CLM-003","CLM-005"],"locator":"-","materiality":"DECISIVE","routes":["EXPAND"],"source_id":"-","status":"SATURATED"}
LED-003 | {"evidence_excerpt":"Thème objet dérivé du sujet : financement SPGD et dépôts sauvages (étayé par FCT-002, FCT-004).","kind":"OBJECT","lead":"Financement et impact environnemental du réseau : coût national de gestion, dépense SPGD, et enjeu des dépôts sauvages.","linked_ids":["AXS-004","AXS-006","CLM-002","CLM-004"],"locator":"-","materiality":"DECISIVE","routes":["EXPAND"],"source_id":"-","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Environ 40% du tonnage des déchets ménagers et assimilés collectés par le service public en France (2021) provient des dépôts en déchèterie (≈242 kg/hab sur 615 kg/hab).","claimant":"Insee Première n°2055 / MTECT notre-environnement (données ADEME SINOE)","counter":"NONE_FOUND","gap":"-","gap_type":"NONE","materiality":"DECISIVE","status":"SATURATED","support":"FCT-001"}
CLM-002 | {"claim":"La gestion des déchets en France a mobilisé 22,0 milliards d euro en 2023, dont 63% (13,9 Md€) pour le service public (SPGD), financé principalement par la TEOM (8,9 Md€) et la REOM (0,9 Md€).","claimant":"SDES (Comptes économiques de l environnement)","counter":"NONE_FOUND (21,6 Md€ en 2022 conforme à la trajectoire)","gap":"-","gap_type":"NONE","materiality":"DECISIVE","status":"SATURATED","support":"FCT-002"}
CLM-003 | {"claim":"Les déchèteries sont des installations classées (ICPE) relevant de la rubrique 2710, soumises aux prescriptions du décret n°2012-384 (20/03/2012) et des arrêtés du 27/03/2012 (registre des déchets sortants, stockage des déchets dangereux, contrôle périodique).","claimant":"Enviroveille / CCI France","counter":"NONE_FOUND (Légifrance inaccessible au bot : 403 head_blocked)","gap":"-","gap_type":"NONE","materiality":"DECISIVE","status":"SATURATED","support":"FCT-003"}
CLM-004 | {"claim":"Le coût de résorption des dépôts sauvages de déchets en France est estimé entre 30 et 90 millions d euros par an (Cerema 2024).","claimant":"ARBE Région Sud, rapportant une estimation du Cerema (2024)","counter":"NONE_FOUND","gap":"-","gap_type":"NONE","materiality":"IMPORTANT","status":"SATURATED","support":"FCT-004"}
CLM-005 | {"claim":"Le nombre exact de déchèteries ouvertes en France n est pas établi de façon fiable dans cette investigation.","claimant":"investigation","counter":"-","gap":"Absence de total courant lisible : rapports ADEME illisibles au bot (no readable text), annuaire SINOE enregistrements cumulés sans total d ouverture","gap_type":"INDEPENDENCE","materiality":"DECISIVE","status":"GAP","support":"-"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-005","QRY-006"],"axis":"SCOPE_HISTORY","gap":"Le nombre exact de déchèteries ouvertes en France n a pas pu etre ancré sur une source inspectee dans cette passe (rapport ADEME illisible, annuaire SINOE sans total courant lisible)","gap_type":"INDEPENDENCE","led_clm_links":[],"question":"Nombre et évolution du maillage des déchèteries en France ?","result_ids":[],"sought_objects":"statistique nationale du nombre de déchèteries ouvertes (ADEME/SINOE annuaire)","status":"GAP"}
AXS-002 | {"attempt_ids":["QRY-002","QRY-007"],"axis":"RULES_CONTROLS","led_clm_links":["CLM-003","CLM-005"],"question":"Quel est le cadre réglementaire et technique des déchèteries (ICPE, accès, prescriptions) ?","result_ids":["FCT-003","FCT-005"],"sought_objects":"nomenclature ICPE 2710, arrêtés de prescriptions, conditions d accès","status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-010"],"axis":"ACTORS_RELATIONS","led_clm_links":["CLM-001"],"question":"Quels acteurs gouvernent et opèrent le réseau des déchèteries ?","result_ids":["FCT-001"],"sought_objects":"rôles ADEME, collectivités, éco-organismes REP, standard de données","status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-008","QRY-012"],"axis":"RESOURCES_FLOWS","led_clm_links":["CLM-002"],"question":"Comment les déchèteries et le service public de gestion des déchets sont-ils financés ?","result_ids":["FCT-002"],"sought_objects":"dépense nationale, TEOM, REOM, part SPGD","status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-003","QRY-004","QRY-011"],"axis":"MECHANISMS","led_clm_links":["CLM-001"],"question":"Quel est le rôle des déchèteries dans le circuit de collecte des ménages ?","result_ids":["FCT-001"],"sought_objects":"part du tonnage DMA passant par les déchèteries, fraction par flux","status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-009","QRY-013"],"axis":"IMPACT_RESPONSIBILITY","led_clm_links":["CLM-004"],"question":"Quels sont les écarts et impacts avérés (dépôts sauvages, accès) ?","result_ids":["FCT-004"],"sought_objects":"estimation nationale du coût des dépôts sauvages, enjeux d accès","status":"SATURATED"}
AXS-007 | {"attempt_ids":["QRY-005","QRY-011"],"axis":"COUNTER_HYPOTHESES","gap":"Absence de source inspectée fiable du nombre courant de déchèteries ; l annuaire SINOE agrège des enregistrements historiques cumulés, non un total d ouverture lisible","gap_type":"INDEPENDENCE","led_clm_links":["CLM-005"],"question":"Le réseau des déchèteries se réduit-il ou s étend-il ? Les données du nombre de sites sont-elles cohérentes ?","result_ids":[],"sought_objects":"tendance du maillage, données contradictoires sur le nombre de sites","status":"GAP"}
AXS-008 | {"attempt_ids":[],"axis":"SOURCE_AUDIT","gap":"N/A(NO_INPUT_LEAD) : input TOPIC sans source matérielle","gap_type":"NONE","led_clm_links":[],"question":"Audit fidélité de la source fournie (lead)","result_ids":[],"sought_objects":"sans objet (aucun lead fourni)","status":"N/A"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"aucune chaîne causale vérifiée dans cette passe ; le coût Cerema est une estimation de résorption, pas un lien causal démontré","from":"pratiques et contraintes d accès aux déchèteries et coût du service","gap":"Aucune relation causale démontrée entre accès/coût et dépôts sauvages ; seule une corrélation/ piste de prévention contextuelle est documentée. NOTE : RESTRICTION, CAUSATION, PRECEDENT ≠ CAUSE ; le lien reste inexpliqué sans étude causale dédiée.","gap_type":"CAUSALITY","link_type":"CONTEXT","mechanism":"hypothèse liant restriction d accès / coût du service à la persistance des dépôts sauvages (évoquée par ARBE comme piste de prévention)","source":"ARBE Région Sud (FCT-004)","status":"GAP","to":"persistance des dépôts sauvages de déchets"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:6|FETCH:7|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"EMPTY","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"EMPTY","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"EMPTY","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND:0 relevant; no subject-fp snapshot; unrelated investigations only | MnemoLite-MCP8002 | - | MNEMO_Q
SYS-003 | SYS | PASS | runtime | SYS-002 | REPAIR_SYS
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | ADEME SINOE nombre déchetteries France réseau (découverte)
QRY-002 | WEB | FOUND | - | - | déchetterie réglementation accession particuliers interdiction professionnels arrêté code environnement
QRY-003 | FETCH | FOUND | SRC-001 | https://www.insee.fr/fr/statistiques/8574484 | -
QRY-004 | FETCH | FOUND | SRC-002 | https://www.notre-environnement.gouv.fr/themes/societe/le-mode-de-vie-des-menages-ressources/article/les-dechets-menagers-en-france-chiffres-et-enjeux-pour-l-environnement | -
QRY-005 | WEB | FOUND | - | - | nombre déchèteries France ADEME chiffres clés network
QRY-006 | FETCH | FAILED:no-readable-text | - | https://librairie.ademe.fr/economie-circulaire-et-dechets/8644-la-collecte-des-dechets-par-le-service-public-en-france.html | -
QRY-007 | FETCH | FOUND | SRC-003 | https://www.enviroveille.com/public/fiches_pratiques/fiches-pratiques.html?cat_id=1&dossier_id=129306&fiche_id=113678 | -
QRY-008 | FETCH | FOUND | SRC-004 | https://www.statistiques.developpement-durable.gouv.fr/la-depense-de-gestion-des-dechets-en-2023 | -
QRY-009 | FETCH | FOUND | SRC-005 | https://www.arbe-regionsud.org/57114-lutter-contre-les-depots-sauvages.html | -
QRY-010 | FETCH | FOUND | SRC-006 | https://www.ademe.fr/presse/communique-national/poubelles-des-francais-des-progres-sur-le-tri-des-dechets-mais-encore-des-marges-importantes-damelioration/ | -
QRY-011 | WEB | NO_RESULT:no-contradiction | - | - | REFUTATION part DMA collectée en déchèterie France : 40% non contredit (perimetre SINOE collecte 2021)
QRY-012 | WEB | NO_RESULT:no-contradiction | - | - | REFUTATION dépense gestion déchets France 2023 : 22,0 Md€ (SDES) confirmé, 21,6 Md€ en 2022 (Figaro)
QRY-013 | WEB | NO_RESULT:no-contradiction | - | - | REFUTATION coût résorption dépôts sauvages France : 30-90 M€/an (Cerema 2024) autres estimations

## EVIDENCE_REGISTRY
SRC-001 | ◉ | fam:A | https://www.insee.fr/fr/statistiques/8574484
SRC-002 | ◉ | fam:A | https://www.notre-environnement.gouv.fr/themes/societe/le-mode-de-vie-des-menages-ressources/article/les-dechets-menagers-en-france-chiffres-et-enjeux-pour-l-environnement
SRC-003 | ◉ | fam:B | https://www.enviroveille.com/public/fiches_pratiques/fiches-pratiques.html?cat_id=1&dossier_id=129306&fiche_id=113678
SRC-004 | ◈ | fam:A | https://www.statistiques.developpement-durable.gouv.fr/la-depense-de-gestion-des-dechets-en-2023
SRC-005 | ◉ | fam:A | https://www.arbe-regionsud.org/57114-lutter-contre-les-depots-sauvages.html
SRC-006 | ◉ | fam:A | https://www.ademe.fr/presse/communique-national/poubelles-des-francais-des-progres-sur-le-tri-des-dechets-mais-encore-des-marges-importantes-damelioration/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.insee.fr/fr/statistiques/8574484 | A | 2021 | dma-part-decheterie | ≈40% (≈242 kg/hab) du tonnage DMA via déchèterie; 615 kg/hab total (SINOE collecte 2021) | 3f4fc609-d971-4161-b1ff-a25af960ce53
FCT-002 | FACT | ✧ | https://www.statistiques.developpement-durable.gouv.fr/la-depense-de-gestion-des-dechets-en-2023 | A | 2023 | depense-gestion-dechets-2023 | 22,0 Md€ (0,8% PIB); 63%/13,9 Md€ SPGD; TEOM 8,9 Md€ + REOM 0,9 Md€; entreprises 41%, ménages 35% | 0f09bb73-2f37-42bc-a74e-a98a3d37bf53
FCT-003 | FACT | ✧ | https://www.enviroveille.com/public/fiches_pratiques/fiches-pratiques.html?cat_id=1&dossier_id=129306&fiche_id=113678 | B | 2012 | decheterie-icpe-2710 | ICPE rubrique 2710; régime quantitatif (décret 2012-384 du 20/03/2012); prescriptions arrêtés du 27/03/2012; registre déchets sortants | 2c1adef6-1968-4805-8354-b04273cb46bb
FCT-004 | FACT | ✧ | https://www.arbe-regionsud.org/57114-lutter-contre-les-depots-sauvages.html | A | 2024 | depots-sauvages-cout | coût national de résorption des dépôts sauvages estimé 30-90 M€/an (Cerema 2024) | 42ec6571-93b9-4a7b-a060-c3b9871e97ca
FCT-005 | FACT | ✧ | https://www.enviroveille.com/public/fiches_pratiques/fiches-pratiques.html?cat_id=1&dossier_id=129306&fiche_id=113678 | B | 2012 | decheterie-acces-professionnels | la réglementation permet l'accès des artisans/commerçants/PME; la décision et les conditions relèvent du gestionnaire | b18be14a-a892-4886-970c-2c040557a281
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-002,SRC-006
FCT-002 | SRC-004
FCT-003 | SRC-003
FCT-004 | SRC-005
FCT-005 | SRC-003

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-011 | NONE
FCT-002 | QRY-012 | NONE
FCT-004 | QRY-013 | NONE

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
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8
CP-003 | SEARCH:AXS-002 | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T07:16:40.995965+00:00","fact_mem":{"FCT-001":"3f4fc609-d971-4161-b1ff-a25af960ce53","FCT-002":"0f09bb73-2f37-42bc-a74e-a98a3d37bf53","FCT-003":"2c1adef6-1968-4805-8354-b04273cb46bb","FCT-004":"42ec6571-93b9-4a7b-a060-c3b9871e97ca","FCT-005":"b18be14a-a892-4886-970c-2c040557a281"},"mnemo_row":"ad7c53e5-c2f5-443a-b435-a94a99b7f150","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:ad7c53e5-c2f5-443a-b435-a94a99b7f150 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
