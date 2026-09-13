ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-1830-certification-primaute-dechetteries-france | PARENT_RUN_ID:20260830-1301-dechetteries-france-fresque | AS_OF:2026-08-30
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_certification-primaute-dechetteries-france/2026-08-30_18-30_certification-primaute-dechetteries-france_INPUT.txt | SUBJECT_SLUG:certification-primaute-dechetteries-france | SUBJECT_FP:sha256:9d65399f1508fad86a85cf58faad7b47b6c2646a2206bcb60bfb3031f4c5feff | INPUT_SHA256:sha256:9245e42a5b8aeaf3e56254929439b8b43a13d2b73341afe402fdb9fe8713faa6
COMPLEXITY:7→COMPLEX | CHECKPOINT_SEQ:9 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['CUB Bordeaux', "Commune d'Arles", 'SMIPE Benais', 'ADEME/SINOE', 'Archives Bordeaux Métropole', 'Veolia/Onyx'], 'domains': ['histoire', 'réglementation', 'archives', 'SINOE', 'presse', 'primauté'], 'exclusions': [], 'geo': 'France (Bordeaux/Gradignan, Arles, Benais, sites pré-1980)', 'lead_question': "Quelle est la primauté réelle des déchèteries en France (site, date, nature d'équipement) ?", 'limits': 'cote exacte délibération Gradignan en ligne non accessible (Anubis) ; presse locale payante pour 1970s', 'object_question': "Certifier le verdict de primauté : (1) Benais 1973 D_OUV contaminé par la date de création du syndicat/collecte OMR → rejet de la primauté absolue ; (2) Arles 1977 = décharge communale 1964-1999 avec apport-volontaire antérieur, pas de déchèterie moderne post-87 ; (3) Gradignan acte CUB 80/151 du 21/03/1980 = premier centre moderne urbain documenté par acte, récit 17/11/1980 fissuré, SINOE 1981 ; (4) verdict final = faisceau d'apports-volontaires antérieurs à la circulaire 87-63 du 26/06/1987.", 'period': '1960-1990 (ouverture des sites pionniers + néologisme 1987)'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Certification du verdict de primauté des déchèteries en France

## QUESTION OBJET

Certifier le verdict de primauté issu des audits d'antériorité (fresque 1301) : quel est le premier équipement d'apport volontaire / déchèterie de France, et que vaut le récit officiel « Gradignan, première déchèterie de France, 17/11/1980 » ?

## VERDICT CERTIFIÉ (5 FCT, 2 ✦ + 3 ✧, sources réouvertes par FETCH direct le 2026-08-30)

### 1. Benais (Indre-et-Loire) — D_OUV 1973 CONTAMINÉ, primauté absolue REJETÉE [FCT-001 ✧]

La date SINOE `D_OUV 1973-11-26` de la « Déchèterie de Benais » (service 4963) ne documente **pas** une ouverture de déchèterie :

- La **fiche acteur SINOE 857 (SMIPE Val Touraine Anjou)** — INSPECTED ce jour — liste les compétences : **01A Collecte OMR : 26/11/1973** (création du syndicat) ; 01B Collecte sélective : 01/01/1997 ; **01C Déchèterie : 02/06/1985**.
- Le D_OUV de la déchèterie reproduit **exactement** la date de la compétence Collecte OMR → **contamination** par la date de création du syndicat (même patron d'erreur que Longwy 1960 et Toulouse 1884).
- L'audit Benais (passe 1301) avait établi la déclaration préfectorale de la déchèterie à **12/01/1995** et le transfert de Benais à 1983.
- **Verdict** : l'ouverture réelle de la déchèterie de Benais se situe **~1985-1995** (compétence 02/06/1985 ; déclaration 12/01/1995). **Benais est écarté de la primauté absolue.**

### 2. Arles « Les Ségonnaux » (Bouches-du-Rhône) — décharge communale 1964-1999, apport-volontaire 1977 [FCT-002 ✦]

Triple corroboration indépendante (3 familles de provenance) :

- **SINOE fiche 3610** (INSPECTED, dataset raw ADEME) : `D_OUV 1977-01-01`, stable sur les 5 enquêtes 2009-2026. Apport-volontaire au public documenté.
- **La Provence, 25/02/2014** (INSPECTED) : « Décharge communale : la Ville tire un trait sur 35 ans d'excès » — « **Exploité entre 1964 et 1999**, le site est en cours de réhabilitation ». (famille presse indépendante)
- **ICPE préfecture 13** (INSPECTED) : objet « **Réhabilitation de l'ancienne décharge des Ségonnaux** » — arrêtés du **13/07/2017** (réhabilitation et suivi environnemental) et du **10/04/2020** (modification). **arles.fr** (INSPECTED) : arrêté préfectoral **n° 2020-201 PC** « travaux de réhabilitation et de suivi post exploitation de l'**ancienne décharge communale des Ségonnaux** » (publié 24/01/2022).

**Verdict** : le site était une **décharge communale** (1964-1999). L'apport-volontaire y est antérieur à Gradignan (1977 vs 1980) mais ce n'est **pas une déchèterie moderne** au sens post-87 (néologisme). La primauté de l'« équipement moderne » est **reformulée** ; l'antériorité de l'**apport-volontaire** est **confirmée**. Réfutation adversariale : NONE (aucun acte d'ouverture d'une déchèterie moderne à Arles avant 1980 trouvé).

### 3. Gradignan (Gironde) — acte CUB 80/151 du 21/03/1980, récit « 17/11/1980 » FISSURE [FCT-003 ✦]

- **SINOE fiche 5001** (INSPECTED) : « Déchèterie de Gradignan », site « Allée de Mégévie », **D_OUV 1981-01-01**, acteur Bordeaux Métropole (stable).
- **Registre BXM 511 W** (Archives BM, wayback INSPECTED + extrait certifié P0) : notice **8586 = « Délibérations de 1980 »** ; l'acte réel du **21/03/1980** (affaire **80/151**) porte sur un « **Centre de Recyclage et de Récupération** » sur terrain à Gradignan (chemin d'Omon) ; le registre CUB 1980 contient **zéro occurrence du mot « déchetterie »**.
- **TSM (AGHTM) septembre 1986** (Gallica INSPECTED) : dossier « LES DÉCHETTERIES », page **395** « Déchetterie de Gradignan » (photo « Doc. ANRED ») — corroboration presse technique indépendante.
- **Récit officiel Archives BM** : « création de la première déchetterie en France ouverte à Gradignan le **17/11/1980** » — **FISSURE** : aucune séance plénière CUB ce jour-là ; le registre 1980 ne contient pas le mot.

**Verdict** : Gradignan = **premier centre moderne urbain documenté par acte** (21/03/1980, aff. 80/151) mais **pas la « première déchèterie de France » absolue**. SINOE 1981-01-01. Réfutation adversariale : NONE (aucune source primaire attestant le mot « déchetterie » ou une ouverture le 17/11/1980 trouvée).

### 4. Circulaire 87-63 du 26/06/1987 — acte introductif du mot et de la politique [FCT-004 ✧]

**AIDA INSPECTED** (texte intégral) : « La prévention des dépôts sauvages passe notamment par la création de **déchetteries**, centres de réception des déchets encombrants **ouverts en permanence au public** ». État : en vigueur ; publiée 09/08/1987. C'est l'acte introductif national du néologisme et de la politique.

### 5. Verdict global — un FAISCEAU, pas un site unique [FCT-005 ✧]

La primauté absolue « Gradignan = première déchèterie de France (17/11/1980) » est **rejetée comme fait historique absolu**. Il existe un **faisceau d'apports-volontaires antérieurs à la circulaire 87-63** : Arles 1977 (décharge communale 1964-1999), Benais 1973 (date contaminée), St-Aquilin 1973, Ivry-la-Bataille 1975 (à vérifier), Longwy 1960 (outlier). Formulation certifiée :

> « Gradignan est **l'un des premiers équipements d'apport volontaire modernes et explicitement dédiés**, **premier du type au niveau intercommunal CUB**, documenté par acte du 21/03/1980 (aff. 80/151). Les récits "première de France" sont des revendications territoriales/patrimoniales à requalifier. »

## CAUSALITÉ (CAU-001, CAU-002)

- **CAU-001 (mécanisme de contamination)** : le D_OUV SINOE de Benais (26/11/1973) reproduit la date de création du syndicat (compétence Collecte OMR) car le référentiel a recopié une date de compétence dans le champ ouverture de service → ouverture réelle ~1985-1995.
- **CAU-002 (mécanisme du récit)** : la revendication « première déchèterie de France 17/11/1980 » ne résiste pas à l'acte primaire (registre CUB 1980 sans le mot, pas de séance plénière ce jour) → requalification en « l'un des premiers équipements d'apport volontaire modernes, premier du type au niveau intercommunal CUB ».

## GAPS RESTANTS (tracés)

1. **Cote exacte de la délibération Gradignan 21/03/1980** aux Archives BM (courrier demandé) pour passer de « réouvert via registre » à acte numérisé complet.
2. **Actes d'ouverture St-Aquilin 1973 / Ivry 1975 / La Haie-Fouassière 1974** (faisceau Onyx/Veolia) — non réouverts dans cette passe.
3. **Acte municipal Arles 1977** (archives communales) — introuvable en ligne.
4. **Prime occurrence JORF** du mot « déchetterie » (post-1987).
5. **Presse locale Benais ~1985-1995** pour dater l'ouverture réelle de la déchèterie.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:5|CLM:5|AXS:5|CAU:2|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_excerpt":"Benais 1973 : D_OUV contaminé par date création syndicat/collecte OMR (compétence déchèterie 02/06/1985, déclaration 12/01/1995). Arles 1977 : décharge communale 1964-1999. Gradignan : acte CUB 80/151 21/03/1980.","kind":"CLAIM","lead":"Le verdict de primauté des déchèteries en France doit être certifié (Benais 1973 contaminé, Arles 1977 décharge communale, Gradignan 1980 acte CUB)","linked_ids":["CLM-001","AXS-001"],"locator":"dossier certification primauté 2026-08-30","materiality":"DECISIVE","routes":["AUDIT","EXPAND"],"source_id":"INPUT","status":"SATURATED"}
LED-002 | {"evidence_excerpt":"compétence déchèterie SMIPE 02/06/1985 ; déclaration préfectorale déchèterie 12/01/1995 ; D_OUV 1973-11-26 = date compétence 01A collecte OMR","kind":"EVENT","lead":"Benais 1973 : la date SINOE D_OUV 1973-11-26 est une contamination par la création du syndicat (collecte OMR), pas une ouverture de déchèterie","linked_ids":["CLM-001","AXS-002"],"locator":"audit Benais","materiality":"DECISIVE","routes":["AUDIT"],"source_id":"INPUT","status":"SATURATED"}
LED-003 | {"evidence_excerpt":"La Provence 2014 (décharge 1964-1999) ; ICPE préfecture 13 (réhabilitation ancienne décharge) ; SINOE D_OUV 1977-01-01 stable","kind":"EVENT","lead":"Arles Ségonnaux 1977 : décharge communale 1964-1999 avec apport-volontaire antérieur à 1980, pas de déchèterie moderne post-87","linked_ids":["CLM-002","AXS-003"],"locator":"audit Arles","materiality":"DECISIVE","routes":["AUDIT","EXPAND"],"source_id":"INPUT","status":"SATURATED"}
LED-004 | {"evidence_excerpt":"registre BXM 511 W notice 8586 ; zéro occurrence déchetterie dans registre CUB 1980 ; acte réel = Centre Recyclage/Récupération 80/151","kind":"EVENT","lead":"Gradignan : acte CUB aff. 80/151 21/03/1980 = premier centre moderne urbain documenté par acte ; récit 17/11/1980 fissuré ; SINOE 1981-01-01","linked_ids":["CLM-003","AXS-004"],"locator":"audit Gradignan","materiality":"DECISIVE","routes":["AUDIT","EXPAND"],"source_id":"INPUT","status":"SATURATED"}
LED-005 | {"evidence_excerpt":"AIDA circulaire n° 87-63 du 26/06/1987 relative à l'élimination des ordures ménagères ; prescrit création de déchetteries","kind":"EVENT","lead":"Circulaire 87-63 (26/06/1987) = acte introductif du mot et de la politique déchèterie","linked_ids":["CLM-004","AXS-005"],"locator":"circulaire 87-63","materiality":"IMPORTANT","routes":["EXPAND"],"source_id":"INPUT","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"counter":"NONE_FOUND","gap":"GAP_TYPE=ACCESS (acte d'ouverture déchèterie Benais non retrouvé en ligne)","linked_ids":["LED-002","AXS-002"],"proposition":"Le D_OUV SINOE 1973-11-26 de la déchèterie de Benais est contaminé : il reproduit la date de création du syndicat/compétence collecte OMR, pas une ouverture de déchèterie (compétence déchèterie SMIPE 02/06/1985 ; déclaration préfectorale 12/01/1995)","status":"SUPPORTED","status_note":"certifié FINAL 2026-08-30","support":"SINOE fiche acteur SMIPE compétences + fiche service 4963 autorisation"}
CLM-002 | {"counter":"NONE_FOUND","gap":"GAP_TYPE=ACCESS (acte municipal 1977 introuvable en ligne)","linked_ids":["LED-003","AXS-003"],"proposition":"Le site d'Arles Ségonnaux était une décharge communale (1964-1999) ; l'apport-volontaire y est documenté dès 1977-01-01 (SINOE) mais ce n'est pas une déchèterie moderne au sens post-87","status":"SUPPORTED","status_note":"certifié FINAL 2026-08-30","support":"SINOE fiche 3610 + La Provence 2014 + ICPE préfecture 13"}
CLM-003 | {"counter":"récit Archives BM 17/11/1980","gap":"GAP_TYPE=ACCESS (cote délibération en ligne Anubis)","linked_ids":["LED-004","AXS-004"],"proposition":"Gradignan : acte CUB aff. 80/151 du 21/03/1980 = premier centre moderne urbain documenté par acte ; le récit « première de France 17/11/1980 » est une fissure (pas de séance plénière ce jour) ; SINOE date 1981-01-01","status":"SUPPORTED","status_note":"certifié FINAL 2026-08-30","support":"registre BXM 511 W notice 8586 + SINOE"}
CLM-004 | {"counter":"NONE_FOUND","gap":"GAP_TYPE=NONE","linked_ids":["LED-005","AXS-005"],"proposition":"La circulaire 87-63 du 26/06/1987 est l'acte introductif du mot et de la politique « déchèterie »","status":"SUPPORTED","status_note":"certifié FINAL 2026-08-30","support":"AIDA circulaire 87-63"}
CLM-005 | {"counter":"récit Gradignan première absolue","gap":"GAP_TYPE=ACCESS (actes locaux 1970s partiellement en ligne)","linked_ids":["LED-001","AXS-001"],"proposition":"Verdict final : ni un site unique, mais un faisceau d'apports-volontaires antérieurs à la circulaire 87-63 (Benais 1973 contaminé, St-Aquilin 1973, Ivry 1975, Arles 1977, Longwy 1960 outlier) ; reformulation « l'un des premiers équipements d'apport volontaire modernes et explicitement dédiés »","status":"SUPPORTED","status_note":"certifié FINAL 2026-08-30","support":"croisement SINOE + audits + registre CUB"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008"],"gap_type":"NONE","led_links":["LED-002"],"question":"Benais 1973 : la date D_OUV SINOE est-elle une contamination par la création du syndicat (collecte OMR) plutôt qu'une ouverture de déchèterie ?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005"],"sought_objects":["SINOE fiche service 4963","SINOE fiche acteur SMIPE compétences","déclaration préfectorale déchèterie","presse/RA SMIPE"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008"],"gap_type":"NONE","led_links":["LED-003"],"question":"Arles 1977 : qu'était le site des Ségonnaux avant le néologisme 1987 (décharge communale ? apport-volontaire ?) et la date D_OUV 1977-01-01 est-elle fiable ?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005"],"sought_objects":["SINOE fiche service 3610","ICPE préfecture 13 arrêtés réhabilitation","presse La Provence","archives communales Arles"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008"],"gap_type":"NONE","led_links":["LED-004"],"question":"Gradignan : l'acte CUB aff. 80/151 du 21/03/1980 documente-t-il le premier centre moderne urbain ? Le récit « 17/11/1980 » tient-il face au registre ?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005"],"sought_objects":["registre BXM 511 W notice 8586","acte 80/151","SINOE Gradignan 1981","Archives BM exposition"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008"],"gap_type":"NONE","led_links":["LED-005"],"question":"La circulaire 87-63 du 26/06/1987 est-elle bien l'acte introductif du mot et de la politique « déchèterie » ?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005"],"sought_objects":["AIDA circulaire 87-63","texte intégral"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008"],"gap_type":"NONE","led_links":["LED-001"],"question":"Y a-t-il d'autres sites pré-1980 crédibles (St-Aquilin 1973, Ivry 1975, Longwy 1960) et que valent leurs dates SINOE ?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005"],"sought_objects":["SINOE dataset","presse locale","Veolia/Onyx revendications"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"La date D_OUV SINOE de Benais (1973-11-26) reproduit la date de creation du syndicat (competence collecte OMR) car le referentiel SINOE a recopie une date de competence dans le champ ouverture de service","effect":"Le D_OUV 1973 est une contamination ; la vraie ouverture decheterie se situe ~1985-1995 (competence 1985, declaration prefectorale 1995)","source":"FCT-001","status":"SATURATED","type":"MECHANISM"}
CAU-002 | {"cause":"La revendication « premiere dechetterie de France 17/11/1980 » (Archives BM) ne resisterait pas a un acte primaire : le registre CUB 1980 ne contient pas le mot et la seance pleniere du 17/11/1980 est absente","effect":"Le recit doit etre requalifie en « l'un des premiers equipements d'apport volontaire modernes et explicitement dedies, premier du type au niveau intercommunal CUB »","source":"FCT-003","status":"SATURATED","type":"CAUSATION"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:8|EXA:4
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND: 10 warm-route mems (registre CUB 80/151, SINOE Gradignan 1981, circulaire 87-63, sites pre-1980 Benais/St-Aquilin/Ivry/Arles/Longwy; aucune mem des audits Benais/Arles -> GAP a certifier) | mnemolite:search_memory | 20260830-1301-dechetteries-france-fresque | MNEMO_Q
SYS-003 | SYS | LOADED: SYMBOLS, PATTERNS, THREATS, GATES, REQUEST_LOG | runtime:load | - | ALWAYS_LOAD
SYS-004 | SYS | NONE (pas de snapshot fingerprint v2) | runtime:memory-probe | - | MEMORY_PROBE
SYS-005 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://data.ademe.fr/data-fair/api/v1/datasets/sinoe-(r)-annuaire-des-decheteries-dma/raw | FETCH dataset SINOE ADEME raw (Benais 4963 D_OUV 1973-11-26, Arles 3610 D_OUV 1977-01-01, Gradignan 5001 D_OUV 1981-01-01)
QRY-002 | FETCH | FOUND | SRC-002 | https://aida.ineris.fr/reglementation/circulaire-ndeg-87-63-260687-relative-a-lelimination-ordures-menageres | FETCH circulaire AIDA 87-63 (acte introductif déchetteries)
QRY-003 | FETCH | FOUND | SRC-003 | https://www.sinoe.org/index.php/fiche_acteur/set-onglet-content/id/857/act/1/ser//onglet/COMP_SERV/prov/fiche/origId/857/structactorig/208705/tactadh857po/asc/tactadh857ps/exclcol/tactadh857psp/ | FETCH SINOE fiche acteur 857 SMIPE (compétences: OMR 26/11/1973, Déchèterie 02/06/1985)
QRY-004 | FETCH | FOUND | SRC-004 | http://web.archive.org/web/20230116100622/https://archives.bordeaux-metropole.fr/archive/fonds/FR-ABM243300316 | FETCH wayback fonds BXM 511 W (Délibérations CUB 1967-2003, notice 8586 = 1980)
QRY-005 | FETCH | FOUND | SRC-005 | https://www.bouches-du-rhone.gouv.fr/Publications/Publications-environnementales/Installations-Classees-pour-la-Protection-de-l-Environnement-ICPE/Installations-Classees-soumises-a-autorisation-et-a-enregistrement-Carrieres-et-Geothermie/Arles | FETCH ICPE préfecture 13 — réhabilitation ancienne décharge Ségonnaux (arrêtés 13/07/2017, 10/04/2020)
QRY-006 | FETCH | FOUND | SRC-006 | https://arles.fr/publications/arrete-prefectoral-travaux-ancienne-decharge-segonnaux/ | FETCH arles.fr — arrêté 2020-201 PC travaux ancienne décharge Ségonnaux (24/01/2022)
QRY-007 | FETCH | FOUND | SRC-007 | https://www.laprovence.com/article/edition-arles/2768675/decharge-communale-la-ville-tire-un-trait-sur-35-ans-dexces.html | FETCH La Provence 25/02/2014 — décharge communale Ségonnaux exploité 1964-1999
QRY-008 | FETCH | FOUND | SRC-008 | https://gallica.bnf.fr/services/ContentSearch?ark=ark:/12148/bpt6k9608124h&query=Gradignan | FETCH Gallica TSM sept 1986 — LES DECHETTERIES p.395 Déchetterie de Gradignan
QRY-009 | EXA | NONE_FOUND | - | - | REFUTATION Arles 01 02 04 07 10 13 1964 1977 1999 201 2014 2017 2020 2022 24 25 5 87 : recherche d'un acte d'ouverture de dechetterie moderne a Arles avant 1980 (deliberation, arrete, presse locale) contredisant la qualification de decharge communale 1964-1999
QRY-010 | EXA | NONE_FOUND | - | - | REFUTATION Gradignan 01 11 151 17 1980 1981 1986 395 511 80 8586 : recherche d'une source primaire attestant le mot dechetterie ou une ouverture reelle le 17/11/1980 (registre BXM 511 W, presse 1980) contredisant SINOE 1981-01-01
QRY-011 | EXA | NONE_FOUND | - | - | REFUTATION Arles 01 02 04 07 10 13 1964 1977 1999 201 2014 2017 2020 2022 24 25 5 87 : un acte d'ouverture d'une veritable dechetterie moderne a Arles avant 1980 existe-t-il (deliberation, arrete, presse) contredisant la qualification de decharge communale 1964-1999 ?
QRY-012 | EXA | NONE_FOUND | - | - | REFUTATION Gradignan 01 11 151 17 1980 1981 1986 395 511 80 8586 : une source primaire attestant le mot dechetterie ou une ouverture reelle le 17/11/1980 existe-t-elle (registre BXM 511 W notice 8586, presse 1980) contredisant SINOE 1981-01-01 ?

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://data.ademe.fr/data-fair/api/v1/datasets/sinoe-(r)-annuaire-des-decheteries-dma/raw
SRC-002 | ◈ | fam:B | https://aida.ineris.fr/reglementation/circulaire-ndeg-87-63-260687-relative-a-lelimination-ordures-menageres
SRC-003 | ◈ | fam:A | https://www.sinoe.org/index.php/fiche_acteur/set-onglet-content/id/857/act/1/ser//onglet/COMP_SERV/prov/fiche/origId/857/structactorig/208705/tactadh857po/asc/tactadh857ps/exclcol/tactadh857psp/
SRC-004 | ◈ | fam:B | http://web.archive.org/web/20230116100622/https://archives.bordeaux-metropole.fr/archive/fonds/FR-ABM243300316
SRC-005 | ◈ | fam:A | https://www.bouches-du-rhone.gouv.fr/Publications/Publications-environnementales/Installations-Classees-pour-la-Protection-de-l-Environnement-ICPE/Installations-Classees-soumises-a-autorisation-et-a-enregistrement-Carrieres-et-Geothermie/Arles
SRC-006 | ◈ | fam:B | https://arles.fr/publications/arrete-prefectoral-travaux-ancienne-decharge-segonnaux/
SRC-007 | ◈ | fam:D | https://www.laprovence.com/article/edition-arles/2768675/decharge-communale-la-ville-tire-un-trait-sur-35-ans-dexces.html
SRC-008 | ◈ | fam:B | https://gallica.bnf.fr/services/ContentSearch?ark=ark:/12148/bpt6k9608124h&query=Gradignan

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.sinoe.org/index.php/fiche_acteur/set-onglet-content/id/857/act/1/ser//onglet/COMP_SERV/prov/fiche/origId/857/structactorig/208705/tactadh857po/asc/tactadh857ps/exclcol/tactadh857psp/ | A | 2026-08-30 | Benais D_OUV 1973-11-26 contamine : reproduit la date de creation du syndicat (competence 01A Collecte OMR 26/11/1973) ; competence decheterie SMIPE = 02/06/1985 ; declaration prefectorale decheterie Benais = 12/01/1995 | Contamination Benais : SINOE fiche service 4963 D_OUV=1973-11-26 ; SINOE fiche acteur 857 SMIPE (INSPECTED) : 01A Collecte OMR 26/11/1973, 01B Collecte selective 01/01/1997, 01C Decheterie 02/06/1985. Le D_OUV de la decheterie reproduit exactement la date de la competence OMR (creation du syndicat). L'ouverture reelle la plus probable se situe ~1985-1995 (competence 1985 ; declaration prefectorale 12/01/1995, attestee par l'audit Benais passe 1301). Primauté absolue de Benais REJETEE. | b056561e-5a08-45d4-a73c-d4fb2edca5e6
FCT-002 | FACT | ✦ | https://www.bouches-du-rhone.gouv.fr/Publications/Publications-environnementales/Installations-Classees-pour-la-Protection-de-l-Environnement-ICPE/Installations-Classees-soumises-a-autorisation-et-a-enregistrement-Carrieres-et-Geothermie/Arles | A,B,D | 2026-08-30 | Arles Segonnaux : decharge communale 1964-1999 (La Provence 25/02/2014 INSPECTED) ; apport-volontaire SINOE D_OUV 1977-01-01 (stable 5 lignes) ; ICPE pref. 13 arretes 13/07/2017 + 10/04/2020 rehabilitation ancienne decharge ; arret prefectoral 2020-201 PC (arles.fr 24/01/2022) — pas de decheterie moderne post-87 | Arles Segonnaux : triple corroboration independante — (1) SINOE fiche 3610 D_OUV=1977-01-01 stable (source officielle ADEME) ; (2) La Provence 25/02/2014 (INSPECTED) : « decharge communale, exploite entre 1964 et 1999, en cours de rehabilitation » (famille presse) ; (3) ICPE pref. 13 (INSPECTED) : objet « Rehabilitation de l'ancienne decharge des Segonnaux » + arretes 13/07/2017 et 10/04/2020 ; arles.fr (INSPECTED) : arret prefectoral 2020-201 PC « travaux de rehabilitation et de suivi post exploitation de l'ancienne decharge communale des Segonnaux » (24/01/2022). Verdict : apport-volontaire anterieur a 1980 (1977) MAIS site = decharge communale, pas de decheterie moderne au sens post-87 ; primauté de l'equipement moderne REFORMULEE, apport-volontaire CONFIRME. | f760b93d-e59f-4aef-9337-166c73293d84
FCT-003 | FACT | ✦ | https://data.ademe.fr/data-fair/api/v1/datasets/sinoe-(r)-annuaire-des-decheteries-dma/raw | A,B | 2026-08-30 | Gradignan : SINOE D_OUV=1981-01-01 (site Allee de Megevie, Bordeaux Metropole, stable) ; registre BXM 511 W notice 8586 = Deliberations de 1980, acte reel = Centre Recyclage/Recuperation aff. 80/151 terrain Gradignan, zero occurrence dechetterie (passe P0 certifiee) ; TSM sept 1986 p.395 « Dechetterie de Gradignan » (Gallica INSPECTED) ; recit Archives BM « premiere dechetterie de France 17/11/1980 » = fissure (pas de seance pleniere ce jour) | Gradignan : convergence 2 familles independantes — (1) SINOE ADEME fiche 5001 D_OUV=1981-01-01 (INSPECTED, dataset raw) ; (2) registre BXM 511 W (Archives BM, wayback INSPECTED + extrait certifie P0) : notice 8586 = Deliberations de 1980, l'acte reel du 21/03/1980 (aff. 80/151) est un « Centre de Recyclage et de Recuperation » sur terrain Gradignan chemin d'Omon, et le registre CUB 1980 contient zero occurrence du mot « dechetterie » ; (3) TSM/AGHTM sept 1986 p.395 « Dechetterie de Gradignan » photo « Doc. ANRED » (Gallica INSPECTED) = corroboration presse technique. Le recit officiel Archives BM « premiere dechetterie de France ouverte a Gradignan le 17/11/1980 » est une FISSURE : pas de seance pleniere ce jour-la (verifie P0). Verdict : premier centre moderne urbain documente par acte (21/03/1980) mais pas « premiere de France » absolue ; SINOE 1981. | 10697523-5d30-40c1-8f2e-8cb6b468e1b4
FCT-004 | FACT | ✧ | https://aida.ineris.fr/reglementation/circulaire-ndeg-87-63-260687-relative-a-lelimination-ordures-menageres | B | 2026-08-30 | Circulaire 87-63 du 26/06/1987 (AIDA INSPECTED, etat en vigueur) : « La prevention des depots sauvages passe notamment par la creation de dechetteries, centres de reception des dechets encombrants ouverts en permanence au public » = acte introductif national du mot et de la politique dechetterie | Circulaire n°87-63 du 26/06/87 relative a l'elimination des ordures menageres (AIDA INSPECTED, publiee 09/08/1987, etat en vigueur) : texte integral contenant « La prevention des depots sauvages passe notamment par la creation de dechetteries, centres de reception des dechets encombrants ouverts en permanence au public. Un courrier conjoint vient d'etre adresse aux maires par le ministre... ». Acte introductif national du mot et de la politique dechetterie (1987), borne basse du neologisme. | b53c590a-c455-46f9-8f69-4398bb28c133
FCT-005 | FACT | ✧ | https://data.ademe.fr/data-fair/api/v1/datasets/sinoe-(r)-annuaire-des-decheteries-dma/raw | A,B,D | 2026-08-30 | Verdict de primauté : ni un site unique ni une date unique, mais un FAISCEAU d'apports-volontaires anterieurs a la circulaire 87-63 — Benais 1973 (D_OUV contamine, rejete), St-Aquilin 1973, Ivry-la-Bataille 1975, Arles 1977 (decharge communale), Longwy 1960 (outlier) ; Gradignan 21/03/1980 = premier centre moderne urbain documente par acte | Verdict certifie : la primauté absolue « Gradignan = premiere dechetterie de France (17/11/1980) » est REJETEE comme fait historique absolu. Le registre CUB 1980 (BXM 511 W) ne contient aucune occurrence du mot « dechetterie » ; l'acte reel est un « Centre de Recyclage et de Recuperation » (aff. 80/151, 21/03/1980) ; SINOE date Gradignan 1981-01-01 ; la circulaire 87-63 n'intervient qu'en 1987. Les apports-volontaires anterieurs documentes (Arles 1977 sur decharge communale 1964-1999 ; Benais 1973 contamine ; St-Aquilin 1973, Ivry 1975 a verifier) forment un faisceau. Formulation exacte : Gradignan = « l'un des premiers equipements d'apport volontaire modernes et explicitement dedies, premier du type au niveau intercommunal CUB, documente par acte du 21/03/1980 ». Les recits « premiere de France » sont des revendications territoriales/patrimoniales a requalifier. | 50a9a497-cb20-450f-a760-70526cc45048
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-003
FCT-002 | SRC-001,SRC-005,SRC-006,SRC-007
FCT-003 | SRC-001,SRC-004,SRC-008
FCT-004 | SRC-002
FCT-005 | SRC-001,SRC-002,SRC-004,SRC-005,SRC-007

## REFUTATION_REGISTRY_V1
FCT-002 | QRY-011 | NONE
FCT-003 | QRY-012 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:CONFIRME
FCT-003 | ELIGIBLE:CONFIRME
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7
CP-002 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7
CP-003 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9:AXS-002:QRY-001
CP-004 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-005 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-006 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-007 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12
CP-008 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-009 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T16:46:16.250336+00:00","fact_mem":{"FCT-001":"b056561e-5a08-45d4-a73c-d4fb2edca5e6","FCT-002":"f760b93d-e59f-4aef-9337-166c73293d84","FCT-003":"10697523-5d30-40c1-8f2e-8cb6b468e1b4","FCT-004":"b53c590a-c455-46f9-8f69-4398bb28c133","FCT-005":"50a9a497-cb20-450f-a760-70526cc45048"},"mnemo_row":"PERSISTED_2026-08-30","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:PERSISTED_2026-08-30 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
