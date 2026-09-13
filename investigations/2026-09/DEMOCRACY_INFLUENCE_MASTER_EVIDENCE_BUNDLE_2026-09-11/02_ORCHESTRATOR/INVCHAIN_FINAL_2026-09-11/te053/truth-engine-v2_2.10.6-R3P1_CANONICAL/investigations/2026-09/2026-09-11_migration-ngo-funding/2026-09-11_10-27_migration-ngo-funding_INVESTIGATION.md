ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260911-1027-migration-ngo-funding | PARENT_RUN_ID:NONE | AS_OF:2026-09-11
INPUT_KIND:RUN_CARD | MISSION_MODE:DEEPEN | INPUT_REF:PATH:/mnt/data/invchain/te053/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-11_migration-ngo-funding/2026-09-11_10-27_migration-ngo-funding_INPUT.md | SUBJECT_SLUG:migration-ngo-funding | SUBJECT_FP:sha256:f7f477819a59d584dfd649e51cc0de627cabf33d4f7abefc1fa895c0809e9ba1 | INPUT_SHA256:sha256:0570dcf1fd973566d9711d574e8829dc408aabbba0512a6d9b34c3d646e6a50b
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/UE, principalement 2015–2026. Tracer financeur -> ONG/programme -> activité financée -> cible institutionnelle ou population -> output/action -> décision/effet éventuel. Prioriser comptes, subventions, marchés, registres de lobbying, projets et évaluations. Gardes : financement != tasking ; assistance humanitaire != lobbying ; lobbying != capture ; proximité politique != coordination ; output != effet de politique publique.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/MONEY.md,clusters/NETWORK.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-053 — Financement des ONG liées aux migrations : capacité, plaidoyer et effet politique

## Objet
Tester la chaîne `financeur -> ONG/programme -> activité financée -> cible institutionnelle ou population -> output/action -> décision/effet`, en séparant strictement capacité opérationnelle, lobbying, accès institutionnel, tasking et causalité de politique publique.

## Résultat central
**FACT.** En France, les financements publics consacrés aux associations intervenant dans l'immigration, l'asile et l'intégration dépassent un milliard d'euros par an dans le périmètre examiné et ont fortement augmenté entre 2019 et 2023 (FCT-001). Quinze associations concentrent environ la moitié des crédits observés (FCT-002).

**FACT.** France Terre d'Asile a reçu en moyenne environ 57,5 M€ par an sur 2019-2023, principalement au titre de missions d'hébergement et d'accompagnement relevant du programme 303 (FCT-003). Les masses budgétaires 2023 montrent que l'essentiel du financement est attaché à des prestations opérationnelles d'hébergement et d'accompagnement (FCT-004).

**INFERENCE.** Ces flux ferment une arête robuste `financement public -> capacité opérationnelle`. Ils ne ferment ni `financement -> instruction politique`, ni `financement -> lobbying`, ni `financement -> décision publique capturée`.

## France Terre d'Asile : activité financée et plaidoyer explicite
**FACT.** France Terre d'Asile est inscrite au répertoire HATVP des représentants d'intérêts et dispose de personnels déclarés affectés à cette activité (FCT-005).

**FACT.** Ses déclarations recensent des actions menées pour son propre compte afin de transmettre des suggestions ou positions susceptibles d'influencer des décisions publiques, notamment sur le Pacte européen migration/asile et le projet de loi de finances (FCT-006).

**INFERENCE.** Le même organisme peut donc cumuler financement public d'activités opérationnelles et plaidoyer politique explicite. Cette coexistence établit `capacité financée + advocacy`, mais ne prouve pas que le financeur commande le plaidoyer : l'arête `financeur -> tasking politique` reste absente.

## Contrôle juridique : SOS Méditerranée
**FACT.** Le Conseil d'État a posé qu'une collectivité peut subventionner une activité internationale à caractère humanitaire à condition que la subvention soit destinée exclusivement à cette activité et ne finance pas des activités ou prises de position politiques (FCT-007).

**FACT.** Dans les contentieux examinés, les subventions de Paris et de l'Hérault ont été admises parce que leur affectation humanitaire était suffisamment ciblée, alors que celle de Montpellier a été annulée faute de garanties suffisantes sur cette affectation (FCT-008).

**FACT.** SOS Méditerranée a déclaré à la HATVP ne pas avoir exercé d'activité de représentation d'intérêts en France en 2024 et 2025 (FCT-009).

**INFERENCE.** Ce cas fournit un contrôle direct contre le raccourci `ONG migratoire financée -> lobbying financé`. Le droit et les pratiques déclaratives permettent au contraire de séparer financement humanitaire, activité politique et lobbying.

## ECRE et PICUM : financement multi-sources, accès et advocacy
**FACT.** ECRE reçoit des financements issus de programmes européens et de fondations privées (FCT-010). Son activité comprend explicitement du plaidoyer visant à influencer politiques et pratiques européennes ; l'organisation rapporte que certaines de ses recommandations ont été reprises dans des textes du Pacte (FCT-011).

**FACT.** PICUM et ECRE ont conduit des actions conjointes de plaidoyer sur le financement européen et auprès de la Commission et du Parlement ; leurs publications rapportent des évolutions de positions institutionnelles cohérentes avec certaines de leurs demandes (FCT-012).

**FACT.** Le Forum européen sur la migration fournit par ailleurs un canal institutionnel structuré de dialogue et d'accès entre institutions et plus de 200 organisations de la société civile (FCT-013).

**INFERENCE.** La chaîne `financement multi-sources -> ressources organisationnelles -> advocacy/accès -> outputs` est établie. L'arête suivante, `advocacy -> modification précise de texte ou décision`, reste seulement partielle : les reprises revendiquées par les organisations sont des éléments de contribution, pas une attribution causale indépendante.

## Causalité et contrôles
Les cas examinés imposent cinq distinctions :

1. `financement -> capacité opérationnelle` : **établi**.
2. `organisation financée -> activité de lobbying/advocacy` : **établi dans certains cas**, notamment FTDA, ECRE et PICUM.
3. `financement -> tasking/commandement politique` : **non établi**.
4. `lobbying/advocacy -> accès et outputs institutionnels` : **établi**.
5. `advocacy -> décision publique spécifique attribuable` : **non fermé causalement** dans le corpus échantillonné.

Le contrôle SOS Méditerranée montre en outre que financement humanitaire et activité politique peuvent être juridiquement dissociés et que cette séparation est effectivement contrôlée par le juge.

## Verdict
Le modèle le mieux supporté est un système à étages : les financements publics et privés créent des capacités matérielles ; certaines ONG utilisent parallèlement leurs propres ressources et accès pour mener un plaidoyer explicite ; des canaux institutionnels offrent un accès réel aux décideurs. Mais aucun cas examiné ne démontre une chaîne `financeur -> instruction politique -> ONG -> décision capturée`.

La conclusion probatoire est donc : **financement != tasking ; assistance humanitaire != lobbying ; lobbying != capture ; accès != effet causal ; auto-attribution d'influence != preuve indépendante de causalité.**
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:6|SRC_COMPLETE:10/10

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-11
- **breaks:**
  - 2019-2023 hausse des crédits IAI associatifs
  - 2024 décisions Conseil d’État SOS Méditerranée
  - 2024-2026 formalisation HATVP du plaidoyer FTDA
  - 2024 Pacte UE et phase de mise en œuvre
- **status:** CURRENT
- **window:** France/UE principalement 2015-2026

### MANIPULATION_REPORT
- **assumptions:**
  - les montants publics décrivent des capacités et missions, pas une orientation politique par eux-mêmes
  - les déclarations HATVP décrivent l’activité revendiquée par l’organisation
  - les auto-attributions ECRE/PICUM ne valent pas attribution causale indépendante
- **clusters:**
  - MONEY
  - POWER
  - NETWORK
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - **I01:** un même acteur peut séparer opérations et plaidoyer
  - **I02:** pluralité de financeurs réduit l’inférence de commandement
  - **I03:** effet politique exige un delta décisionnel identifiable
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - **P01:** funding-to-capacity
  - **P02:** funding+advocacy coexistence
  - **P03:** access without causal closure
  - **P04:** legal separation humanitarian/political
- **priorities:**
  - tracer flux et finalité
  - séparer opérationnel et plaidoyer
  - exiger instruction pour tasking
  - exiger delta/counterfactual pour effet
- **query_guidance:** sources officielles pour financements et droit; registres de lobbying; rapports organisationnels seulement pour auto-description de l’advocacy
- **rhetorical:**
  - **R01:** agréger tous les financements comme influence
  - **R02:** confondre mission publique et relais politique
  - **R03:** transformer accès institutionnel en capture
- **speaker:**
  - **goal:** tester financeur->ONG->activité->output/décision
  - **target:** séparer capacité, lobbying, tasking et effet
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** financeur
  - **S02:** subvention
  - **S03:** marché
  - **S04:** ONG
  - **S05:** programme
  - **S06:** capacité
  - **S07:** bénéficiaire
  - **S08:** plaidoyer
  - **S09:** accès
  - **S10:** suggestion
  - **S11:** tasking
  - **S12:** décision
  - **S13:** effet
  - **S14:** contrôle
  - **S15:** contrefactuel
- **threats:**
  - funding=tasking
  - service=lobbying
  - lobbying=capture
  - access=effect
  - self-report=causal proof
  - grant amount=political alignment

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - full cross-organisation funding denominator
  - **input_ids:**
    - FCT-001
    - FCT-002
    - FCT-003
    - FCT-004
    - FCT-010
  - **module:** clusters/MONEY.md
  - **negative_results:**
    - no financial flow alone establishes tasking
  - **not_computable:**
    - share of total NGO budgets for all actors
  - **operations_applied:**
    - mapped funder->recipient->program/purpose
    - separated operational capacity from political effect
  - **reason:** distinguer ressource, affectation et dépendance
  - **result_ids:**
    - CLM-001
    - CLM-004
    - CAU-001
    - CAU-003
  - **status:** DONE
  - **trigger:** flux publics/UE/privés
- **item 2:**
  - **gaps:**
    - article-level legislative footprint and counterfactual
  - **input_ids:**
    - FCT-005
    - FCT-006
    - FCT-011
    - FCT-012
    - FCT-013
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no actor-specific captured decision closed
  - **not_computable:**
    - marginal probability of policy adoption caused by NGO advocacy
  - **operations_applied:**
    - separated access, advocacy, text claim and causal effect
    - tested legal/institutional counter-controls
  - **reason:** test whether resources convert into identifiable public decision
  - **result_ids:**
    - CLM-002
    - CLM-005
    - CAU-002
    - CAU-004
  - **status:** DONE
  - **trigger:** lobbying/access/decision claims
- **item 3:**
  - **gaps:**
    - authenticated instructions where any exist
  - **input_ids:**
    - FCT-003
    - FCT-009
    - FCT-010
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no authenticated financeur command chain
  - **not_computable:**
    - latent informal tasking not in public record
  - **operations_applied:**
    - separated funder, grantee, mandate and principal
    - used SOS as negative control
  - **reason:** prevent funding relation from substituting for tasking
  - **result_ids:**
    - CLM-003
    - CLM-006
    - CAU-005
  - **status:** DONE
  - **trigger:** financeur-recipient-principal inference

### SCOPING_REPORT
- **excluded:**
  - generic NGO ideology
  - all migration spending outside sampled chains
  - claims of capture without decision delta
  - foreign cases without France/UE relevance
- **included:**
  - French IAI association funding
  - FTDA HATVP advocacy
  - SOS Méditerranée subsidy jurisprudence
  - ECRE/PICUM funding+advocacy
  - EU civil-society access forum
- **reason:** actor/case-specific chains with traceable funding, activity and decision/output

### CREDO
- **forbidden_shortcuts:**
  - funding=command
  - humanitarian service=lobbying
  - advocacy=capture
  - access=causal effect
  - self-report=independent proof
- **rule:** trace money to funded activity, then separately prove tasking, advocacy and effect

### COGNITIVE_MAP
- **chain:**
  - financeur
  - instrument
  - bénéficiaire
  - activité financée
  - advocacy éventuelle
  - accès/output
  - décision
  - effet
- **rival_models:**
  - service delivery
  - autonomous advocacy
  - funder tasking
  - institutional co-production
  - capture

### DIALECTICAL_MAP
- **antithesis:** Une grande partie finance des missions opérationnelles; plaidoyer et financement peuvent coexister sans commandement ni capture.
- **synthesis:** Capacité opérationnelle et advocacy sont observables et parfois réunies chez le même acteur; la chaîne financeur->tasking->décision capturée n’est pas fermée dans l’échantillon.
- **thesis:** Le financement d’ONG migratoires peut convertir des ressources publiques/privées en influence politique non élective.

### RESOURCE_FLOW_MAP
- **flows:**
  - État français -> programmes 303/104 -> associations -> hébergement/accompagnement/intégration
  - financeurs UE/fondations -> ECRE/PICUM -> expertise/advocacy
  - collectivités -> SOS Méditerranée -> activité humanitaire ciblée
- **limits:**
  - flux != instruction
  - montant != effet politique
  - cofinancement != principal unique

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** État français / mission IAI
  - **relation:** finance missions opérationnelles
  - **support:**
    - FCT-001
    - FCT-003
    - FCT-004
  - **to:** FTDA et autres associations
- **item 2:**
  - **from:** FTDA
  - **relation:** plaidoyer déclaré pour son propre compte
  - **support:**
    - FCT-005
    - FCT-006
  - **to:** Parlement/Gouvernement/administration
- **item 3:**
  - **from:** UE + fondations
  - **relation:** financement multi-source
  - **support:**
    - FCT-010
    - FCT-011
    - FCT-012
  - **to:** ECRE/PICUM
- **item 4:**
  - **from:** institutions UE
  - **relation:** forum/dialogue structuré
  - **support:**
    - FCT-013
  - **to:** société civile migration

### IMPACT_MAP
- **established:**
  - financement public -> capacité opérationnelle
  - FTDA financement opérationnel + lobbying explicite
  - ECRE/PICUM financement + advocacy
  - contrôle juridique de séparation humanitaire/politique
- **not_established:**
  - financeur->tasking politique
  - capture d’une décision spécifique
  - effet politique général des financements
- **partial:**
  - auto-attributions de recommandations incorporées
  - accès institutionnel vers décisions

### CONTRADICTION_LEDGER
- **item 1:**
  - **issue:** FTDA reçoit des fonds publics et lobbye
  - **resolution:** coexistence factuelle; ne pas inférer tasking sans instruction/condition politique
- **item 2:**
  - **issue:** ECRE/PICUM affirment avoir influencé des textes
  - **resolution:** retenir comme auto-attribution et output; causalité indépendante reste ouverte
- **item 3:**
  - **issue:** SOS reçoit des subventions mais HATVP indique aucune RI 2024-2025
  - **resolution:** contrôle contre funded NGO => lobbyist; ne pas inférer silence politique total
- **item 4:**
  - **issue:** Montpellier annulée mais Paris/Hérault validées
  - **resolution:** le ciblage juridique, pas l’identité de l’ONG, discrimine les décisions

### VERIFICATION_REPORT
- **facts:** 13
- **method:** official funding/judicial/lobbying records plus organization self-reports clearly labelled; causal edge tested separately
- **negative_checks:**
  - SOS HATVP no RI
  - Conseil d’État subsidy targeting
  - multi-funder ECRE
  - EC Forum access != effect
- **research_queries:** 10
- **sources_fetched:** 10
- **verdict:** sufficient to establish capacity, declared advocacy and access; insufficient to establish funder tasking or captured decision

### EDI_REPORT
- **corpus:** 10 accepted sources across 6 provenance families
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim:** CLM-001
    - **families:**
      - A
  - **item 2:**
    - **claim:** CLM-002
    - **families:**
      - A
      - B
  - **item 3:**
    - **claim:** CLM-003
    - **families:**
      - B
      - C
  - **item 4:**
    - **claim:** CLM-004
    - **families:**
      - D
      - E
  - **item 5:**
    - **claim:** CLM-005
    - **families:**
      - D
      - E
      - other:ec-home
  - **item 6:**
    - **claim:** CLM-006
    - **families:**
      - C
- **diagnostic_not_truth:** true
- **dimensions:**
  - French budget/mission execution
  - lobbying register
  - administrative jurisprudence
  - NGO funding disclosures
  - NGO advocacy reports
  - EU institutional access
- **edi:** DIVERSE_OFFICIAL_PLUS_SELF_REPORT_WITH_PROVENANCE_SEPARATED
- **source_counts:**
  - **A:** 2
  - **B:** 2
  - **C:** 2
  - **D:** 2
  - **E:** 1
  - **other:ec-home:** 1

### RESPONSIBILITY_MAP
- **item 1:**
  - **actor:** État français
  - **documented_action:** finance des missions d’asile/intégration exécutées par associations
  - **intent:** PROVEN
  - **scope:** capacity/service delivery; political tasking not established
  - **support:**
    - FCT-001
    - FCT-003
    - FCT-004
- **item 2:**
  - **actor:** France Terre d’Asile
  - **documented_action:** mène un plaidoyer explicite auprès des décideurs pour son propre compte
  - **intent:** PROVEN
  - **scope:** declared lobbying; funding causation not established
  - **support:**
    - FCT-005
    - FCT-006
- **item 3:**
  - **actor:** Conseil d’État
  - **documented_action:** contrôle la finalité humanitaire et le ciblage des subventions
  - **intent:** PROVEN
  - **scope:** legal control only
  - **support:**
    - FCT-007
    - FCT-008
- **item 4:**
  - **actor:** ECRE/PICUM
  - **documented_action:** mènent advocacy et revendiquent certains outputs politiques
  - **intent:** PROVEN
  - **scope:** self-reported contribution; marginal causal effect not established
  - **support:**
    - FCT-010
    - FCT-011
    - FCT-012

### NEXT_QUERIES
- Pour fermer un effet politique, construire un legislative footprint article-par-article reliant recommandation datée, décideur, amendement et justification.
- Pour tester tasking, rechercher des conventions/subventions contenant des conditions de positionnement politique explicites ou des instructions authentifiées.
- Pour INV-052, utiliser séparément capacité opérationnelle, lobbying déclaré et absence de preuve de commandement.

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-007,FCT-008,FCT-009 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-003,QRY-006,QRY-007,QRY-008,QRY-009 | support:- | counter:- | results:FCT-003,FCT-005,FCT-006,FCT-009,FCT-010,FCT-011,FCT-012 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-003,QRY-004,QRY-005,QRY-008,QRY-009,QRY-010 | support:- | counter:- | results:FCT-006,FCT-007,FCT-008,FCT-011,FCT-012,FCT-013 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,SRC-001 | support:FCT-001,FCT-002,FCT-003,FCT-004 | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-001,QRY-003,QRY-006,SRC-001,SRC-003,SRC-006 | support:FCT-003,FCT-005,FCT-006 | counter:FCT-009 | results:FCT-003,FCT-005,FCT-006,FCT-009 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-003,QRY-004,QRY-005,QRY-006,SRC-003,SRC-004,SRC-005,SRC-006 | support:FCT-007,FCT-008,FCT-009 | counter:FCT-005,FCT-006 | results:FCT-007,FCT-008,FCT-009,FCT-005,FCT-006 | final:REFUTED | gap:NONE
CLM-004 | attempts:QRY-007,QRY-008,QRY-009,SRC-007,SRC-008,SRC-009 | support:FCT-010,FCT-011,FCT-012 | counter:- | results:FCT-010,FCT-011,FCT-012 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-008,QRY-009,QRY-010,SRC-008,SRC-009,SRC-010 | support:FCT-011,FCT-012 | counter:FCT-013 | results:FCT-011,FCT-012,FCT-013 | final:PARTIAL | gap:CAUSALITY
CLM-006 | attempts:QRY-004,QRY-005,SRC-004,SRC-005 | support:FCT-007,FCT-008 | counter:- | results:FCT-007,FCT-008 | final:SUPPORTED | gap:NONE

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-005 | CLM | PARTIAL | CAUSALITY | Les auto-attributions d’incorporation et l’accès institutionnel ne fournissent pas un contrefactuel ni une attribution indépendante article-par-article du delta décisionnel.
CAU-002 | CAU | UNRESOLVED | CAUSALITY | Aucune instruction du financeur ni médiation causale financeur->position de plaidoyer->décision n’est documentée dans les cas échantillonnés.
CAU-004 | CAU | UNRESOLVED | CAUSALITY | Manquent attribution indépendante du delta de texte, chronologie amendement par amendement et contrefactuel sans intervention.

SEMANTIC_COUNTS_V1:LED:0|CLM:6|AXS:3|CAU:5|CTRL:5|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Les financements publics français créent une capacité opérationnelle majeure pour l’hébergement, l’accompagnement et l’intégration liés à l’asile/migration.","claimant":"INV-053","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-004"]}
CLM-002 | {"claim":"France Terre d’Asile cumule des financements publics opérationnels significatifs et un plaidoyer/lobbying explicitement déclaré.","claimant":"INV-053","counter":["FCT-009"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-003","FCT-005","FCT-006"]}
CLM-003 | {"claim":"Le seul financement d’une ONG migratoire suffit à établir un tasking ou commandement politique par le financeur.","claimant":"hypothèse forte","counter":["FCT-005","FCT-006"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"REFUTED","support":["FCT-007","FCT-008","FCT-009"]}
CLM-004 | {"claim":"Dans l’écosystème UE, des organisations comme ECRE/PICUM cumulent financements institutionnels/privés et activités d’advocacy explicites.","claimant":"INV-053","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-010","FCT-011","FCT-012"]}
CLM-005 | {"claim":"Le plaidoyer d’ECRE/PICUM a causé des modifications précises de textes ou décisions de l’UE.","claimant":"organisations concernées / hypothèse causale","counter":["FCT-013"],"gap":"Les auto-attributions d’incorporation et l’accès institutionnel ne fournissent pas un contrefactuel ni une attribution indépendante article-par-article du delta décisionnel.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-011","FCT-012"]}
CLM-006 | {"claim":"Le droit français impose une séparation explicite entre subvention humanitaire locale et financement d’activités politiques.","claimant":"Conseil d’État","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-007","FCT-008"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006"],"axis":"PUBLIC_FUNDING_TO_OPERATIONAL_CAPACITY","links":["CLM-001","CAU-001"],"question":"Quels financements publics créent une capacité opérationnelle identifiable chez les associations migratoires, sans inférer plaidoyer ou tasking ?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-007","FCT-008","FCT-009"],"sought_objects":["funding","contract","service","beneficiaries","operational_output"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-003","QRY-006","QRY-007","QRY-008","QRY-009"],"axis":"FUNDING_AND_ADVOCACY_COEXISTENCE","links":["CLM-002","CLM-003","CLM-004","CAU-002","CAU-003"],"question":"Le même acteur peut-il recevoir des fonds publics/institutionnels et mener un plaidoyer explicite, et cela démontre-t-il un commandement du financeur ?","result_ids":["FCT-003","FCT-005","FCT-006","FCT-009","FCT-010","FCT-011","FCT-012"],"sought_objects":["funding_mix","advocacy","lobbying","tasking","command"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-003","QRY-004","QRY-005","QRY-008","QRY-009","QRY-010"],"axis":"ACCESS_TO_POLICY_EFFECT","links":["CLM-005","CLM-006","CAU-004","CAU-005"],"question":"Quelles traces ferment accès/advocacy -> output institutionnel -> delta de politique, et où la causalité reste-t-elle non isolée ?","result_ids":["FCT-006","FCT-007","FCT-008","FCT-011","FCT-012","FCT-013"],"sought_objects":["access","recommendation","text_delta","decision","counterfactual"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"crédit public affecté à des missions -> ressources associatives -> prestation opérationnelle mesurable","counter":"Le volume de financement ne renseigne pas à lui seul sur une consigne politique.","limit":"Chaîne capacité/service fermée; aucun tasking inféré.","mechanism":"financement public -> capacité opérationnelle -> hébergement/accompagnement/intégration","status":"SUPPORTED","support":["FCT-001","FCT-003","FCT-004"]}
CAU-002 | {"counter":["FCT-007","FCT-008","FCT-009"],"gap":"Aucune instruction du financeur ni médiation causale financeur->position de plaidoyer->décision n’est documentée dans les cas échantillonnés.","gap_type":"CAUSALITY","limit":"Coexistence financement+plaidoyer établie; commandement/capture non établi.","mechanism":"financement public -> dépendance -> tasking/lobbying -> décision publique","status":"UNRESOLVED","support":["FCT-003","FCT-005","FCT-006"]}
CAU-003 | {"causal_right":"ressources multi-financeurs -> capacité d’expertise/advocacy -> accès et productions institutionnelles","counter":"Pluralité de financeurs et mandat propre des organisations empêchent d’identifier un principal commanditaire par le seul flux financier.","limit":"Capacité, advocacy et accès fermés; tasking par un financeur non établi.","mechanism":"financement mixte institutionnel/privé -> ressources organisationnelles -> advocacy/accès -> outputs","status":"SUPPORTED","support":["FCT-010","FCT-011","FCT-012","FCT-013"]}
CAU-004 | {"counter":["FCT-013"],"gap":"Manquent attribution indépendante du delta de texte, chronologie amendement par amendement et contrefactuel sans intervention.","gap_type":"CAUSALITY","limit":"Contribution revendiquée/documentée; causalité marginale spécifique non isolée.","mechanism":"advocacy NGO -> recommandation -> modification de texte/décision UE","status":"UNRESOLVED","support":["FCT-011","FCT-012"]}
CAU-005 | {"causal_right":"condition légale de finalité -> contrôle juridictionnel du ciblage -> validation ou annulation de la subvention","counter":["FCT-009"],"limit":"Contrôle juridique spécifique établi; ne prouve pas la séparation parfaite de toutes les subventions existantes.","mechanism":"règle juridique de ciblage -> affectation de subvention humanitaire -> exclusion des activités politiques","status":"SUPPORTED","support":["FCT-007","FCT-008"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"financement != tasking","status":"PASS","support":["FCT-007","FCT-008","FCT-009"]}
CTRL-002 | {"control":"assistance humanitaire != lobbying","status":"PASS","support":["FCT-007","FCT-009"]}
CTRL-003 | {"control":"lobbying != capture","status":"PASS","support":["FCT-006","FCT-013"]}
CTRL-004 | {"control":"auto-attribution d’un delta de texte != preuve causale indépendante","status":"PASS","support":["FCT-011","FCT-012"]}
CTRL-005 | {"control":"absence de déclaration HATVP != absence de toute expression publique, mais réfute funded NGO => lobbying nécessaire","status":"PASS","support":["FCT-009"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:10|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | UNAVAILABLE | mnemolite | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | ACCEPTED | SRC-001 | https://www.senat.fr/rap/r24-326/r24-3262.html | INV-053 source fetch 1
QRY-002 | FETCH | ACCEPTED | SRC-002 | https://www.senat.fr/notice-rapport/2024/r24-326-notice.html | INV-053 source fetch 2
QRY-003 | FETCH | ACCEPTED | SRC-003 | https://www.hatvp.fr/fiche-organisation/?organisation=784547507 | INV-053 source fetch 3
QRY-004 | FETCH | ACCEPTED | SRC-004 | https://conseil-etat.fr/site/actualites/sos-mediterranee-les-collectivites-territoriales-peuvent-accorder-sous-conditions-une-subvention-a-une-action-humanitaire-internationale | INV-053 source fetch 4
QRY-005 | FETCH | ACCEPTED | SRC-005 | https://conseil-etat.fr/fr/arianeweb/CE/decision/2024-05-13/474507 | INV-053 source fetch 5
QRY-006 | FETCH | ACCEPTED | SRC-006 | https://www.hatvp.fr/fiche-organisation/?organisation=813744471 | INV-053 source fetch 6
QRY-007 | FETCH | ACCEPTED | SRC-007 | https://ecre.org/finance/ | INV-053 source fetch 7
QRY-008 | FETCH | ACCEPTED | SRC-008 | https://ecre.org/wp-content/uploads/2025/03/ECRE-Annual-Report-on-2024.pdf | INV-053 source fetch 8
QRY-009 | FETCH | ACCEPTED | SRC-009 | https://picum.org/wp-content/uploads/2024/12/PICUMs-Annual-Report-2024.pdf | INV-053 source fetch 9
QRY-010 | FETCH | ACCEPTED | SRC-010 | https://home-affairs.ec.europa.eu/news/2024-european-migration-forum-highlights-key-role-civil-society-implementing-pact-2024-12-18_en | INV-053 source fetch 10

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | SENAT-R24-326-2 | Sénat — suite à enquête Cour des comptes sur associations immigration/intégration | 2025-02-11 | 2026-09-11T08:27:00+00:00 | sections B.1-B.2 | https://www.senat.fr/rap/r24-326/r24-3262.html
SRC-002 | ◈ | fam:A | SENAT-R24-326-NOTICE | Sénat — notice rapport n°326 (2024-2025) | 2025-02-11 | 2026-09-11T08:27:00+00:00 | résumé | https://www.senat.fr/notice-rapport/2024/r24-326-notice.html
SRC-003 | ◈ | fam:B | HATVP-784547507 | HATVP — France Terre d’Asile | 2026-03-31 | 2026-09-11T08:27:00+00:00 | identité/actions 2024-2025 | https://www.hatvp.fr/fiche-organisation/?organisation=784547507
SRC-004 | ◈ | fam:C | CE-SOS-MEDITERRANEE-2024 | Conseil d’État — SOS Méditerranée, subventions humanitaires sous conditions | 2024-05-13 | 2026-09-11T08:27:00+00:00 | communiqué | https://conseil-etat.fr/site/actualites/sos-mediterranee-les-collectivites-territoriales-peuvent-accorder-sous-conditions-une-subvention-a-une-action-humanitaire-internationale
SRC-005 | ◈ | fam:C | CE-474507 | Conseil d’État — décision n°474507 | 2024-05-13 | 2026-09-11T08:27:00+00:00 | décision | https://conseil-etat.fr/fr/arianeweb/CE/decision/2024-05-13/474507
SRC-006 | ◈ | fam:B | HATVP-813744471 | HATVP — SOS Méditerranée France | 2024-03-29 | 2026-09-11T08:27:00+00:00 | identité/actions 2023-2025 | https://www.hatvp.fr/fiche-organisation/?organisation=813744471
SRC-007 | ◉ | fam:D | ECRE-FUNDING | ECRE — Funding | undated-current | 2026-09-11T08:27:00+00:00 | funding sources | https://ecre.org/finance/
SRC-008 | ◉ | fam:D | ECRE-AR-2024 | ECRE Annual Report 2024 | 2025-03 | 2026-09-11T08:27:00+00:00 | Activity 2 Advocacy | https://ecre.org/wp-content/uploads/2025/03/ECRE-Annual-Report-on-2024.pdf
SRC-009 | ◉ | fam:E | PICUM-AR-2024 | PICUM Annual Report 2024 | 2024-12 | 2026-09-11T08:27:00+00:00 | EU funding / advocacy | https://picum.org/wp-content/uploads/2024/12/PICUMs-Annual-Report-2024.pdf
SRC-010 | ◈ | fam:other:ec-home | EC-HOME-EMF-2024 | European Commission — 2024 European Migration Forum | 2024-12-18 | 2026-09-11T08:27:00+00:00 | civil society implementation forum | https://home-affairs.ec.europa.eu/news/2024-european-migration-forum-highlights-key-role-civil-society-implementing-pact-2024-12-18_en

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.senat.fr/rap/r24-326/r24-3262.html | A | 2025-02-11 | French public funding to migration/asylum associations | Les crédits versés aux associations via la mission Immigration, asile et intégration dépassent un milliard d’euros par an et ont fortement augmenté entre 2019 et 2023. | -
FCT-002 | FACT | ✧ | https://www.senat.fr/rap/r24-326/r24-3262.html | A | 2025-02-11 | Concentration of association funding | Sur 2019-2023, quinze associations concentrent en moyenne environ 50,3 % des crédits des programmes 104 et 303 dédiés aux associations. | -
FCT-003 | FACT | ✧ | https://www.senat.fr/rap/r24-326/r24-3262.html | A | 2025-02-11 | France Terre d’Asile public funding | France Terre d’Asile a reçu environ 57,5 M€ par an en moyenne sur 2019-2023, très majoritairement via le programme 303 pour l’hébergement et l’accompagnement des demandeurs d’asile. | -
FCT-004 | FACT | ✧ | https://www.senat.fr/rap/r24-326/r24-3262.html | A | 2025-02-11 | 2023 asylum housing and accompaniment funding | En 2023, environ 850 M€ ont été versés aux associations pour l’hébergement et l’accompagnement des demandeurs d’asile/réfugiés vulnérables, dont environ 263,8 M€ estimés pour l’accompagnement. | -
FCT-005 | FACT | ✧ | https://www.hatvp.fr/fiche-organisation/?organisation=784547507 | B | 2026-03-31 | France Terre d’Asile lobbying registration | France Terre d’Asile est inscrite au répertoire HATVP et identifie plusieurs personnes chargées du plaidoyer/représentation d’intérêts. | -
FCT-006 | FACT | ✧ | https://www.hatvp.fr/fiche-organisation/?organisation=784547507 | B | 2026-03-31 | France Terre d’Asile declared advocacy actions | Pour 2024-2025, France Terre d’Asile déclare pour son propre compte des actions consistant notamment à transmettre informations et suggestions afin d’influencer des décisions publiques relatives au Pacte migration/asile, aux PLF et à d’autres mesures migratoires. | -
FCT-007 | FACT | ✧ | https://conseil-etat.fr/site/actualites/sos-mediterranee-les-collectivites-territoriales-peuvent-accorder-sous-conditions-une-subvention-a-une-action-humanitaire-internationale | C | 2024-05-13 | Legal separation of humanitarian subsidies and political activity | Le Conseil d’État exige que les subventions locales à une action humanitaire internationale financent uniquement des activités réellement humanitaires et non des activités politiques. | -
FCT-008 | FACT | ✧ | https://conseil-etat.fr/site/actualites/sos-mediterranee-les-collectivites-territoriales-peuvent-accorder-sous-conditions-une-subvention-a-une-action-humanitaire-internationale | C | 2024-05-13 | SOS Méditerranée subsidy outcomes | Le Conseil d’État a validé les subventions de Paris et de l’Hérault à SOS Méditerranée mais annulé celle de Montpellier, jugée insuffisamment ciblée sur l’activité humanitaire. | -
FCT-009 | FACT | ✧ | https://www.hatvp.fr/fiche-organisation/?organisation=813744471 | B | 2026-03-31 | SOS Méditerranée lobbying negative control | SOS Méditerranée France, inscrite à la HATVP depuis 2024, déclare aucune activité de représentation d’intérêts pour 2024 et 2025. | -
FCT-010 | FACT | ✧ | https://ecre.org/finance/ | D | 2026-09-11 | ECRE mixed funding base | ECRE déclare recevoir des financements de plusieurs programmes de l’Union européenne ainsi que de multiples fondations philanthropiques et d’autres sources. | -
FCT-011 | FACT | ✧ | https://ecre.org/wp-content/uploads/2025/03/ECRE-Annual-Report-on-2024.pdf | D | 2025-03 | ECRE advocacy objective and self-reported incorporation | Le rapport annuel 2024 d’ECRE fixe explicitement l’objectif d’influencer les politiques/pratiques de l’UE et affirme que de nombreuses recommandations ont été incorporées dans les textes finaux du Pacte; cette dernière attribution est auto-déclarée par ECRE. | -
FCT-012 | FACT | ✧ | https://picum.org/wp-content/uploads/2024/12/PICUMs-Annual-Report-2024.pdf | E | 2024-12 | PICUM ECRE EU funding advocacy | PICUM rapporte un plaidoyer conjoint avec ECRE sur les fonds de l’UE, des retours à la Commission et des conseils aux eurodéputés, et s’attribue l’obtention de formulations plus fortes dans un avis du Parlement européen. | -
FCT-013 | FACT | ✧ | https://home-affairs.ec.europa.eu/news/2024-european-migration-forum-highlights-key-role-civil-society-implementing-pact-2024-12-18_en | other:ec-home | 2024-12-18 | Institutional access channel for civil society | Le Forum européen sur la migration 2024 a réuni plus de 200 organisations de la société civile avec des institutions européennes et nationales autour de la mise en œuvre du Pacte, établissant un canal institutionnel d’accès et de dialogue. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-001
FCT-005 | SRC-003
FCT-006 | SRC-003
FCT-007 | SRC-004
FCT-008 | SRC-004,SRC-005
FCT-009 | SRC-006
FCT-010 | SRC-007
FCT-011 | SRC-008
FCT-012 | SRC-009
FCT-013 | SRC-010

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
FCT-009 | ELIGIBLE:VERIFIE
FCT-010 | ELIGIBLE:VERIFIE
FCT-011 | ELIGIBLE:VERIFIE
FCT-012 | ELIGIBLE:VERIFIE
FCT-013 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -
FCT-007 | WRITE | -
FCT-008 | WRITE | -
FCT-009 | WRITE | -
FCT-010 | WRITE | -
FCT-011 | WRITE | -
FCT-012 | WRITE | -
FCT-013 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:SEARCH
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:FACTS
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:CAUSAL
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:VERIFY
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:INVESTIGATION_ACCOUNTABILITY
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:FINALIZE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-11T08:35:06.399926+00:00","fact_mem":{},"mnemo_row":"MNEMO_UNAVAILABLE — local memory service not available; no memory ids fabricated.","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":13,"eligible":13,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_UNAVAILABLE — local memory service not available; no memory ids fabricated. | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:13;attempted:0;success:0;failure:0;blocked:13} | WRITEBACK_EXECUTION_V1:[13 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-002 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-003 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-004 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-005 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-006 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-007 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-008 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-009 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-010 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-011 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-012 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-013 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
