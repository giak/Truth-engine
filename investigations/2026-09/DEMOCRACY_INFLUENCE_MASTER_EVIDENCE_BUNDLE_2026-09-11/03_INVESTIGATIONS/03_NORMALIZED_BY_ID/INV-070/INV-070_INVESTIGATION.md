ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260909-2117-state-behavioural-sciences-nudges | PARENT_RUN_ID:NONE | AS_OF:2026-09-09
INPUT_KIND:RUN_CARD | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/inv070/runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-09_state-behavioural-sciences-nudges/2026-09-09_21-17_state-behavioural-sciences-nudges_INPUT.md | SUBJECT_SLUG:state-behavioural-sciences-nudges | SUBJECT_FP:sha256:387f04d005fcdeec5aa86f1863be1e1ea4d0b0824cbb37c0d0e222625fe78560 | INPUT_SHA256:sha256:bace59203795574a0813e3d755ea6eabfd334ebf10053ad16c45321a1893cbcd
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France, principalement 2017-2026. Tracer autorite/unite comportementale -> diagnostic -> intervention ou architecture de choix -> population cible -> exposition -> comportement mesure -> resultat de politique publique. Prioriser protocoles, experimentations, marches, documents DITP, evaluations et donnees. Gardes : nudge != coercion ; intention != effect ; behavior change != welfare gain ; experiment != population effect ; design choice != manipulation by default ; measured outcome != democratic effect.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/CONFIRMATION.md,clusters/NETWORK.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
## Question et résultat

L'enquête distingue cinq objets souvent fusionnés : l'usage de sciences comportementales par l'État, le nudge au sens strict, l'architecture de choix, les incitations économiques ou réglementaires, et la manipulation/coercition. Le corpus établit que la DITP et plusieurs administrations françaises conçoivent depuis plusieurs années des interventions comportementales explicites, souvent selon une séquence diagnostic -> prototype -> expérimentation -> évaluation. Cette infrastructure est réelle. Elle ne constitue pas, par sa seule existence, une preuve de manipulation clandestine ou de coercition généralisée.

Le résultat causal le plus élevé est plus étroit : dans plusieurs cas, une intervention identifiable est reliée à un changement de comportement mesuré. L'expérimentation HAS-DITP sur le repérage des violences conjugales observe environ 4,4 dépistages hebdomadaires contre 2,5 dans le contrôle. L'essai Pôle emploi sur la mention « entreprise handi-bienveillante » porte sur 111 534 employeurs et rapporte davantage de candidatures potentielles de personnes handicapées. L'expérimentation sur l'air intérieur rapporte un contraste entre information générique, qui change surtout la perception, et données personnalisées par capteur, associées à davantage de changements de pratiques.

## Ce qui est réellement déployé

Le pôle sciences comportementales de la DITP ne se présente pas comme une simple « nudge unit ». Ses interventions peuvent relever de la communication, d'outils numériques, de modifications de l'environnement de décision, voire d'évolutions réglementaires. La DITP indique sélectionner ses projets notamment selon l'importance de l'enjeu, l'existence de freins comportementaux, un consensus éthique, l'engagement du partenaire et la possibilité de mesurer l'impact.

Cette diversité oblige à classer l'instrument avant de juger sa légitimité. Un nudge au sens strict modifie l'architecture de choix sans interdire les options. Un signal tarifaire avec contrepartie financière relève d'une incitation économique. Une évolution réglementaire relève du droit. Le fait que des sciences comportementales aient contribué au design de l'un ou l'autre ne transforme pas ces instruments en une même catégorie.

## Effets : cas positifs, nuls et limites

Les résultats positifs existent, mais ils sont hétérogènes. L'indice de réparabilité fournit un bon contrôle interne : le premier test de visuel a été conduit à grande échelle en conditions réelles ; l'évaluation ultérieure trouve un effet positif significatif en ligne, mais un effet positif non significatif en magasin et un effet global qui n'est pas attribuable avec suffisamment de confiance au seul indice. L'étude ne pouvait pas encore mesurer la réparation effective des produits.

Le projet FAMINUM illustre une autre limite : l'étude pilote porte sur une centaine de familles volontaires et documente surtout l'accueil de l'outil, la discussion familiale et des perceptions positives. Elle ne ferme pas un effet comportemental populationnel. Le projet antibiotiques fournit un contre-exemple méthodologique explicite : la comparaison à des pairs, souvent présentée comme un levier comportemental efficace, est décrite comme potentiellement contre-productive auprès du corps médical. La synthèse DITP sur la fraude avertit aussi que des travaux réalisés en ligne ou à l'étranger ne sont pas directement transférables au contexte français.

Ces cas empêchent de résumer le portefeuille par « les nudges marchent ». La méta-analyse PNAS 2022 trouve un effet moyen positif des interventions d'architecture de choix, mais aussi une forte hétérogénéité et un biais de publication en faveur des résultats positifs. La preuve utile reste donc intervention par intervention, avec conservation des résultats nuls, non significatifs et inattendus.

## Éthique : influence, manipulation, coercition

L'intention de modifier un comportement est explicite dans les sciences comportementales appliquées. Ce fait suffit à parler d'influence intentionnelle, pas de manipulation par défaut. Le cadre éthique de l'OCDE ajoute des discriminants opérationnels : transparence de l'intervention et de son objectif, possibilité de sortie, intérêt public, voies de recours et responsabilité. Une influence non transparente et évitable se rapproche d'une manipulation de design ; une intervention transparente et évitable servant un intérêt public se situe dans une autre catégorie normative.

Le dossier HAS fournit un contrôle concret : l'objectif de questionner systématiquement les patientes sur les violences conjugales est une recommandation clinique publique préexistante ; la DITP intervient pour en améliorer l'appropriation. Le changement de comportement du médecin est mesuré, mais le corpus ne permet pas d'en déduire automatiquement une amélioration causale finale de la situation de chaque victime. Les baromètres ultérieurs de la HAS montrent en outre que le questionnement reste encore peu pratiqué malgré une bonne acceptabilité déclarée.

## Plafond causal et responsabilité

Le corpus permet de fermer : État/administration -> diagnostic comportemental -> intervention explicite -> exposition -> changement comportemental mesuré dans certains cas. Il ne permet pas de fermer de façon générale : intervention -> persistance à long terme -> gain de bien-être -> résultat de politique publique -> effet démocratique. Aucun cas inspecté ne documente une chaîne DITP -> dispositif comportemental clandestin et coercitif -> modification mesurée d'une préférence politique, d'un vote ou d'un résultat électoral.

La qualification correcte est donc instrument- et preuve-dépendante. L'État français dispose d'une capacité institutionnelle réelle de conception comportementale. Cette capacité peut influencer les comportements et produit parfois des effets mesurables. Elle doit être auditée par la transparence, l'évitabilité, la proportionnalité, les résultats nuls et les effets aval. Le saut vers « ingénierie sociale secrète », « manipulation généralisée » ou « coercition » n'est pas supporté par ce corpus.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:3|SRC_COMPLETE:14/14

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-09
- **notes:**
  - DITP behavioural-science programme documented from 2018 onward
  - 2026 electricity experiment outcome not yet available
- **status:** CURRENT
- **window:** 2017-2026

### MANIPULATION_REPORT
- **assumptions:**
  - sources can overstate their own program success
  - null results are material
  - official source is not interpretive privilege
- **clusters:**
  - POWER
  - CONFIRMATION
  - NETWORK
- **complexity:** HIGH
- **implicit:**
  - public intervention always alters choice context
  - ethical status cannot be inferred from soft/hard label alone
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - nudge conflation
  - effect inflation
  - welfare leap
  - scale-up leap
  - ethics-by-label
- **priorities:**
  - deployment
  - causal effect
  - instrument classification
  - ethics
  - scale and downstream effect
- **query_guidance:** Prefer DITP protocols/evaluations and independent methodological controls; separate measured behavior from welfare and democratic effect.
- **rhetorical:**
  - social-engineering umbrella
  - soft-control framing
  - success-story selection
- **speaker:**
  - **goal:** forensic mechanism decomposition
  - **target:** authority -> intervention -> exposure -> behavior -> outcome
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** authority
  - **S02:** diagnosis
  - **S03:** choice-architecture
  - **S04:** information
  - **S05:** incentive
  - **S06:** regulation
  - **S07:** transparency
  - **S08:** avoidability
  - **S09:** exposure
  - **S10:** behavior
  - **S11:** persistence
  - **S12:** welfare
  - **S13:** scale
  - **S14:** null-result
  - **S15:** democratic-effect
- **threats:**
  - nudge=coercion
  - intention=effect
  - behavior=welfare
  - experiment=population
  - design=manipulation
  - measured outcome=democratic effect

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - democratic effect
  - **input_ids:**
    - FCT-001
    - FCT-002
    - FCT-023
    - FCT-025
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no generalized coercive chain found
  - **not_computable:**
    - NONE
  - **operations_applied:**
    - authority->instrument decomposition
    - coercion boundary
  - **reason:** map authority, instrument and accountability without equating influence with coercion
  - **result_ids:**
    - CLM-002
    - CLM-005
    - CAU-005
  - **status:** PASS
  - **trigger:** state actor intentionally designs behavioral interventions
- **item 2:**
  - **gaps:**
    - field-wide denominator
  - **input_ids:**
    - FCT-009
    - FCT-014
    - FCT-015
    - FCT-016
    - FCT-019
    - FCT-028
  - **module:** clusters/CONFIRMATION.md
  - **negative_results:**
    - uniform efficacy not supported
  - **not_computable:**
    - NONE
  - **operations_applied:**
    - negative-case retention
    - publication-bias control
  - **reason:** retain null, non-significant and counterproductive evidence
  - **result_ids:**
    - CLM-007
    - CTRL-001
    - CTRL-010
  - **status:** PASS
  - **trigger:** portfolio contains published successes and claims of effectiveness
- **item 3:**
  - **gaps:**
    - complete project denominator
  - **input_ids:**
    - FCT-003
    - FCT-005
    - FCT-011
    - FCT-021
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - portfolio participation does not prove a single hidden campaign
  - **not_computable:**
    - NONE
  - **operations_applied:**
    - actor-role separation
    - partner mapping
  - **reason:** separate institutional portfolio from centralized command over outcomes
  - **result_ids:**
    - CLM-001
    - CAU-001
  - **status:** PASS
  - **trigger:** multiple administrations and partners participate in distinct projects

### SCOPING_REPORT
- **actors_institutions:**
  - DITP
  - HAS
  - Pôle emploi
  - CGDD
  - MILDECA
  - health and housing administrations
- **domains:**
  - health
  - environment
  - employment
  - digital use
  - fraud
  - energy
- **evidence_limits:**
  - DITP publications are partly self-reported
  - project-level evaluations are heterogeneous
  - several outcomes are intermediate or pilot-level
- **exclusions:**
  - generic psychology theory
  - foreign government programmes except methodological controls
  - party/electoral campaigning
- **geo:** France
- **period:** 2017-2026

### CREDO
- nudge != coercion
- intention != effect
- behavior change != welfare gain
- experiment != population effect
- design choice != manipulation by default
- measured outcome != democratic effect
- null results are material
- official source != interpretive privilege

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - diagnose
  - prototype
  - test
  - scale
- **priorities:**
  - actual deployment
  - effect
  - ethics
  - scale
- **query_guidance:** test successful and unsuccessful interventions symmetrically
- **speaker:**
  - **goal:** bounded causal mapping
  - **tone:** forensic
- **threats:**
  - label inflation
  - causal leap
  - success selection

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** Choice architecture can be manipulative and effects may be overstated.
  - **support:**
    - FCT-003
    - FCT-025
    - FCT-028
  - **synthesis:** Classify instrument, transparency and avoidability, then require causal outcome evidence case by case.
  - **thesis:** Behavioural science can improve implementation by testing real behavior.
- **item 2:**
  - **antithesis:** Other results are null, pilot-only or context-dependent.
  - **support:**
    - FCT-005
    - FCT-009
    - FCT-014
    - FCT-015
    - FCT-027
    - FCT-028
  - **synthesis:** No portfolio-wide efficacy claim is warranted.
  - **thesis:** Several French trials report positive behavior change.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **flow:** DITP/partner expertise -> diagnosis/prototype/evaluation
  - **resource:** behavioral-science capacity
  - **support:**
    - FCT-001
    - FCT-003
- **item 2:**
  - **flow:** public rule or service interface -> information/choice architecture/incentive -> users
  - **resource:** policy design
  - **support:**
    - FCT-002
    - FCT-023
- **item 3:**
  - **flow:** evaluation data -> scale/no-scale decision
  - **resource:** causal evidence
  - **support:**
    - FCT-003
    - FCT-012
    - FCT-019

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** DITP behavioral-science team
  - **relation:** design/evaluation support
  - **support:**
    - FCT-001
    - FCT-003
  - **to:** partner administrations
- **item 2:**
  - **from:** HAS
  - **relation:** pre-existing clinical recommendation plus behavioral implementation support
  - **support:**
    - FCT-021
    - FCT-005
  - **to:** general practitioners
- **item 3:**
  - **from:** CGDD/DITP
  - **relation:** repairability information design and evaluation
  - **support:**
    - FCT-007
    - FCT-009
  - **to:** consumers/market

### IMPACT_MAP
- **highest_supported_edge:** intervention -> measured behavior change in selected project-level evaluations
- **not_established:**
  - portfolio-wide effectiveness
  - general welfare gain
  - general covert manipulation
  - democratic or electoral effect
- **support:**
  - FCT-005
  - FCT-011
  - FCT-017
  - FCT-028

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** repairability aggregate non-significant, FAMINUM pilot only, antibiotics norm risk, publication bias
  - **issue:** positive case reports vs mixed/null outcomes
  - **pro:** several RCTs/pilots report behavior change
  - **resolution:** case-specific efficacy only
  - **support:**
    - FCT-005
    - FCT-009
    - FCT-014
    - FCT-015
    - FCT-028
- **item 2:**
  - **contra:** strict nudge preserves options and OECD ethics differentiates transparent/avoidable forms
  - **issue:** nudge as manipulation
  - **pro:** behavioral design intentionally influences choice context
  - **resolution:** classify transparency, avoidability and constraint rather than label
  - **support:**
    - FCT-004
    - FCT-025
    - FCT-026

### VERIFICATION_REPORT
- **circular_families:**
  - DITP programme family A
  - HAS family B
  - French legal family C
  - OECD ethics family D
  - academic meta-analysis family E
- **contradiction_ids:**
  - efficacy-mixed
  - nudge-manipulation-boundary
- **downgraded_ids:**
  - generalized social engineering
  - uniform nudge effectiveness
  - behavior=welfare
  - project=population
- **none_found_claims:**
  - general clandestine DITP manipulation chain
  - general democratic effect
  - uniform effect size across projects
- **remaining_gaps:**
  - complete project denominator
  - long-term persistence
  - welfare outcomes
  - democratic effect
- **verification:** 28 material facts resolve to 14 fresh FETCH sources across five provenance families; positive, null/limited and ethical-control evidence retained symmetrically.

### EDI_REPORT
- **corpus:** 14 sources / 28 facts
- **decisive_claim_coverage:**
  - CLM-004
  - CLM-007
  - CLM-008
- **diagnostic_not_truth:** true
- **dimensions:**
  - institutional
  - experimental
  - legal
  - ethical
  - meta-scientific
- **edi:** mixed official and methodological control corpus
- **source_counts:**
  - **A:** 10
  - **B:** 1
  - **C:** 1
  - **D:** 1
  - **E:** 1

### RESPONSIBILITY_MAP
- **boundary:** Designing an intervention, changing behavior, improving welfare, manipulating choice and coercing conduct are distinct responsibility claims.
- **not_established:**
  - general covert manipulation
  - population-wide coercion
  - uniform welfare improvement
  - democratic/electoral effect
- **verified:**
  - DITP and partner administrations intentionally design/test behavioral interventions
  - some project-level behavior changes are measured
  - ethical and scale limits are explicitly recognized in several sources

### NEXT_QUERIES
- Reopen only for a complete DITP project denominator with outcomes including nulls.
- Reopen for long-term replication or welfare outcomes of major scaled interventions.
- Reopen for authenticated evidence of non-transparent unavoidable behavioral intervention linked to a democratic outcome.

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010 | support:- | counter:- | results:FCT-001,FCT-003,FCT-005,FCT-007,FCT-011,FCT-013,FCT-015,FCT-017 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-009,QRY-014 | support:- | counter:- | results:FCT-005,FCT-009,FCT-011,FCT-013,FCT-017,FCT-027,FCT-028 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-001,QRY-002,QRY-012,QRY-013 | support:- | counter:- | results:FCT-001,FCT-004,FCT-023,FCT-024,FCT-025,FCT-026 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-005,QRY-006,QRY-007,QRY-010,QRY-011,QRY-014 | support:- | counter:- | results:FCT-010,FCT-012,FCT-014,FCT-019,FCT-022,FCT-028 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-015,QRY-016,QRY-017,QRY-018,QRY-020,QRY-022,QRY-023,SRC-001,SRC-002,SRC-003,SRC-004,SRC-006,SRC-008,SRC-009 | support:FCT-001,FCT-003,FCT-005,FCT-007,FCT-011,FCT-015,FCT-017 | counter:- | results:FCT-001,FCT-003,FCT-005,FCT-007,FCT-011,FCT-015,FCT-017 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-015,QRY-016,QRY-026,SRC-001,SRC-002,SRC-012 | support:FCT-002,FCT-004,FCT-023,FCT-024 | counter:- | results:FCT-002,FCT-004,FCT-023,FCT-024 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-017,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023,SRC-003,SRC-005,SRC-006,SRC-007,SRC-008,SRC-009 | support:FCT-005,FCT-011,FCT-017 | counter:FCT-009,FCT-014,FCT-016 | results:FCT-005,FCT-011,FCT-017,FCT-009,FCT-014,FCT-016 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-017,QRY-019,QRY-020,QRY-021,QRY-023,QRY-025,SRC-003,SRC-005,SRC-006,SRC-007,SRC-009,SRC-011 | support:FCT-006,FCT-010,FCT-012,FCT-014,FCT-018,FCT-022 | counter:- | results:FCT-006,FCT-010,FCT-012,FCT-014,FCT-018,FCT-022 | final:PARTIAL | gap:CAUSALITY
CLM-005 | attempts:QRY-016,QRY-026,SRC-002,SRC-012 | support:FCT-004,FCT-023,FCT-024 | counter:- | results:FCT-004,FCT-023,FCT-024 | final:SUPPORTED | gap:NONE
CLM-006 | attempts:QRY-027,SRC-013 | support:FCT-025,FCT-026 | counter:- | results:FCT-025,FCT-026 | final:SUPPORTED | gap:NONE
CLM-007 | attempts:QRY-017,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023,QRY-024,QRY-028,SRC-003,SRC-005,SRC-006,SRC-007,SRC-008,SRC-009,SRC-010,SRC-014 | support:FCT-009,FCT-014,FCT-015,FCT-016,FCT-019,FCT-020,FCT-027,FCT-028 | counter:FCT-005,FCT-011,FCT-017 | results:FCT-009,FCT-014,FCT-015,FCT-016,FCT-019,FCT-020,FCT-027,FCT-028,FCT-005,FCT-011,FCT-017 | final:SUPPORTED | gap:NONE
CLM-008 | attempts:QRY-015,QRY-016,QRY-017,QRY-019,QRY-020,QRY-021,QRY-023,QRY-025,QRY-027,SRC-001,SRC-002,SRC-003,SRC-005,SRC-006,SRC-007,SRC-009,SRC-011,SRC-013 | support:FCT-001,FCT-002,FCT-003 | counter:FCT-004,FCT-006,FCT-010,FCT-012,FCT-014,FCT-018,FCT-021,FCT-022,FCT-025,FCT-026 | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-006,FCT-010,FCT-012,FCT-014,FCT-018,FCT-021,FCT-022,FCT-025,FCT-026 | final:REFUTED | gap:NONE

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-004 | CLM | PARTIAL | CAUSALITY | Les effets aval sur bien-etre, adoption durable et resultats de politique publique ne sont pas mesures de facon uniforme dans le corpus.
CAU-004 | CAU | UNRESOLVED | CAUSALITY | Absence de chaine uniforme comportement local -> outcome final/welfare a echelle populationnelle.

SEMANTIC_COUNTS_V1:LED:0|CLM:8|AXS:4|CAU:5|CTRL:10|ACT:4

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"La DITP a institutionnalise un usage operationnel des sciences comportementales dans plusieurs politiques publiques françaises.","claimant":"INV-070","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-001","FCT-003","FCT-005","FCT-007","FCT-011","FCT-015","FCT-017"]}
CLM-002 | {"claim":"Les interventions comportementales de Etat ne se reduisent pas aux nudges et peuvent inclure information, outils, architecture de choix, incitations et changements reglementaires.","claimant":"INV-070","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-002","FCT-004","FCT-023","FCT-024"]}
CLM-003 | {"claim":"Certaines interventions françaises ont produit des changements de comportement mesurables dans des essais ou quasi-experiences.","claimant":"INV-070","counter":["FCT-009","FCT-014","FCT-016"],"gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-005","FCT-011","FCT-017"]}
CLM-004 | {"claim":"Un changement de comportement mesure dans un essai ne suffit pas a etablir un gain de bien-etre, une efficacite populationnelle durable ou un effet democratique.","claimant":"INV-070","counter":"NONE_FOUND","gap":"Les effets aval sur bien-etre, adoption durable et resultats de politique publique ne sont pas mesures de facon uniforme dans le corpus.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-006","FCT-010","FCT-012","FCT-014","FCT-018","FCT-022"]}
CLM-005 | {"claim":"Un nudge au sens strict preserve les options; coercition, incitation financiere et evolution reglementaire sont des instruments distincts meme si les sciences comportementales peuvent contribuer a leur design.","claimant":"INV-070","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-004","FCT-023","FCT-024"]}
CLM-006 | {"claim":"La frontiere entre architecture de choix legitime et manipulation depend notamment de transparence, evitabilite, interet public, voies de recours et responsabilisation.","claimant":"INV-070","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-025","FCT-026"]}
CLM-007 | {"claim":"Les effets des nudges sont heterogenes et sensibles au contexte; les resultats nuls, contre-productifs et le biais de publication interdisent une efficacite generale presumée.","claimant":"INV-070","counter":["FCT-005","FCT-011","FCT-017"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-009","FCT-014","FCT-015","FCT-016","FCT-019","FCT-020","FCT-027","FCT-028"]}
CLM-008 | {"claim":"Le corpus inspecte etablit une manipulation comportementale clandestine et coercitive generalisee de la population française par la DITP.","claimant":"strongest adverse hypothesis","counter":["FCT-004","FCT-006","FCT-010","FCT-012","FCT-014","FCT-018","FCT-021","FCT-022","FCT-025","FCT-026"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"REFUTED","support":["FCT-001","FCT-002","FCT-003"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010"],"axis":"deployment","links":["DITP","HAS","CGDD","Pôle emploi","MILDECA"],"question":"Quelles interventions ont ete effectivement testees ou deployees par Etat francais?","result_ids":["FCT-001","FCT-003","FCT-005","FCT-007","FCT-011","FCT-013","FCT-015","FCT-017"],"sought_objects":["protocoles","interventions","populations","exposition"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-009","QRY-014"],"axis":"effect","links":["violences","reparabilite","emploi","ecrans","air"],"question":"Quels changements de comportement sont mesures et avec quelle solidite causale?","result_ids":["FCT-005","FCT-009","FCT-011","FCT-013","FCT-017","FCT-027","FCT-028"],"sought_objects":["RCT","effet","non-significatif","pilote","resultat aval"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-001","QRY-002","QRY-012","QRY-013"],"axis":"ethics","links":["DITP","OECD","Legifrance"],"question":"Ou se situe la frontiere entre information, architecture de choix, manipulation et coercition?","result_ids":["FCT-001","FCT-004","FCT-023","FCT-024","FCT-025","FCT-026"],"sought_objects":["transparence","sortie","interet public","contrainte","incitation economique"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-005","QRY-006","QRY-007","QRY-010","QRY-011","QRY-014"],"axis":"scale","links":["DITP","HAS","PNAS"],"question":"Dans quelles limites les effets experimentaux peuvent-ils etre generalises ou traduits en welfare/politique publique?","result_ids":["FCT-010","FCT-012","FCT-014","FCT-019","FCT-022","FCT-028"],"sought_objects":["externalite","transferabilite","publication bias","scale-up"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"Des essais controles ou evaluations ferment le lien intervention->comportement pour certains cas.","counter":["FCT-009","FCT-014","FCT-016"],"limit":"Effets case-specific; la generalisation depend du contexte et du protocole.","mechanism":"autorite publique -> diagnostic comportemental -> prototype -> experimentation -> exposition -> changement de comportement local","status":"SUPPORTED","support":["FCT-003","FCT-005","FCT-011","FCT-017"]}
CAU-002 | {"causal_right":"Le corpus contient des contrastes internes ou groupes de comparaison fermant certains effets.","counter":["FCT-009","FCT-015"],"limit":"Le mecanisme varie selon population et support; des informations ou normes sociales peuvent ne pas fonctionner.","mechanism":"information personnalisee ou simplifiee -> saillance/comprehension -> action","status":"SUPPORTED","support":["FCT-005","FCT-017"]}
CAU-003 | {"causal_right":"Plusieurs interventions observent un changement sur indicateur comportemental directement cible.","counter":["FCT-009","FCT-012"],"limit":"Le comportement mesure est intermediaire et ne prouve pas a lui seul welfare ou effet systemique.","mechanism":"architecture de choix ou signal explicite -> modification des candidatures, achats ou depistages","status":"SUPPORTED","support":["FCT-005","FCT-011","FCT-007","FCT-008"]}
CAU-004 | {"counter":["FCT-006","FCT-010","FCT-012","FCT-014","FCT-018","FCT-022"],"gap":"Absence de chaine uniforme comportement local -> outcome final/welfare a echelle populationnelle.","gap_type":"CAUSALITY","limit":"Donnees aval et longitudinales insuffisantes ou non homogenes.","mechanism":"intervention comportementale -> changement durable populationnel -> gain de bien-etre ou resultat de politique publique","status":"UNRESOLVED","support":["FCT-005","FCT-011","FCT-017"]}
CAU-005 | {"causal_right":"Les preuves inspectees documentent experimentation et influence comportementale explicite, pas un mecanisme general clandestin/coercitif avec effet democratique.","counter":["FCT-004","FCT-021","FCT-023","FCT-024","FCT-025","FCT-026"],"limit":"Aucune chaine actor-specific du corpus ne ferme dissimulation+contrainte+effet democratique; instruments ethiques et juridiques sont heterogenes.","mechanism":"DITP/sciences comportementales -> manipulation clandestine ou coercition -> effet democratique","status":"REFUTED","support":["FCT-001","FCT-002"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Effet global reparabilite non significatif","status":"PASS","support":["FCT-009"]}
CTRL-002 | {"control":"Pas de mesure de reparation effective","status":"PASS","support":["FCT-010"]}
CTRL-003 | {"control":"Effet handi-bienveillante a revalider a plus grande echelle","status":"PASS","support":["FCT-012"]}
CTRL-004 | {"control":"FAMINUM pilote volontaire sans outcome comportemental populationnel ferme","status":"PASS","support":["FCT-013","FCT-014"]}
CTRL-005 | {"control":"Normes sociales potentiellement contre-productives chez medecins","status":"PASS","support":["FCT-015"]}
CTRL-006 | {"control":"Fraude: transfert etranger/online vers France explicitement borne","status":"PASS","support":["FCT-019","FCT-020"]}
CTRL-007 | {"control":"HAS: objectif normatif preexistant et adoption encore incomplete","status":"PASS","support":["FCT-021","FCT-022"]}
CTRL-008 | {"control":"Signaux tarifaires distingues du nudge pur et outcome futur","status":"PASS","support":["FCT-023","FCT-024"]}
CTRL-009 | {"control":"Ethique OECD: transparence et evitabilite discriminent manipulation","status":"PASS","support":["FCT-025","FCT-026"]}
CTRL-010 | {"control":"Meta-analyse: heterogeneite et biais de publication","status":"PASS","support":["FCT-027","FCT-028"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Classifier chaque intervention selon information, architecture de choix, incitation economique, reglementation ou coercition avant tout jugement ethique.","actor":"future investigations","intent":"eviter la fusion nudge=manipulation=coercition","status":"DONE","support":["FCT-002","FCT-004","FCT-023","FCT-024","FCT-025","FCT-026"]}
ACT-002 | {"action":"Exiger une echelle outcome explicite: exposition -> comportement -> persistance -> welfare -> resultat de politique -> effet democratique.","actor":"future investigations","intent":"eviter le saut comportement local vers effet politique","status":"DONE","support":["FCT-006","FCT-010","FCT-012","FCT-014","FCT-018","FCT-022"]}
ACT-003 | {"action":"Conserver resultats nuls, non significatifs, pilotes et contre-productifs dans tout bilan des sciences comportementales publiques.","actor":"future investigations","intent":"corriger biais de selection des succes","status":"DONE","support":["FCT-009","FCT-014","FCT-015","FCT-016","FCT-019","FCT-028"]}
ACT-004 | {"action":"Ne generaliser une intervention qu avec replication ou donnees de passage a echelle comparables au contexte cible.","actor":"future investigations","intent":"separer preuve experimentale locale et efficacite populationnelle","status":"DONE","support":["FCT-012","FCT-014","FCT-019","FCT-027","FCT-028"]}

SEARCH_ACTIVITY_V1:WEB:14|FETCH:14|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FAIL | MNEMO | MNEMO_UNAVAILABLE | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | PASS | - | - | DITP sciences comportementales criteres consensus ethique mesure impact
QRY-002 | WEB | PASS | - | - | DITP sciences comportementales diagnostic prototypage evaluation RCT
QRY-003 | WEB | PASS | - | - | DITP violences conjugales recommandation simplifiee 76 pourcent
QRY-004 | WEB | PASS | - | - | DITP indice reparabilite 140000 consommateurs essai randomise
QRY-005 | WEB | PASS | - | - | DITP indice reparabilite impact ventes significatif non significatif
QRY-006 | WEB | PASS | - | - | DITP entreprise handi-bienveillante 111534 employeurs randomise
QRY-007 | WEB | PASS | - | - | DITP FAMINUM cent familles pilote ecrans
QRY-008 | WEB | PASS | - | - | DITP antibiotiques normes sociales contre-productives
QRY-009 | WEB | PASS | - | - | DITP pollution air interieur donnees personnalisees comportement
QRY-010 | WEB | PASS | - | - | DITP fraude sciences comportementales 76 documents transfert France
QRY-011 | WEB | PASS | - | - | HAS reperage violences conjugales DITP barometre
QRY-012 | WEB | PASS | - | - | Legifrance 2026 339 signaux tarifaires 6600 consommateurs
QRY-013 | WEB | PASS | - | - | OECD ethical behavioural science public policy transparency avoidability
QRY-014 | WEB | PASS | - | - | PNAS nudging meta-analysis publication bias effect size
QRY-015 | FETCH | FOUND | SRC-001 | https://www.modernisation.gouv.fr/accompagner-les-administrations/laboratoires-interministeriels-dinnovation/sciences | https://www.modernisation.gouv.fr/accompagner-les-administrations/laboratoires-interministeriels-dinnovation/sciences
QRY-016 | FETCH | FOUND | SRC-002 | https://www.modernisation.gouv.fr/actualites/mettre-les-sciences-comportementales-au-coeur-de-laction-publique | https://www.modernisation.gouv.fr/actualites/mettre-les-sciences-comportementales-au-coeur-de-laction-publique
QRY-017 | FETCH | FOUND | SRC-003 | https://www.modernisation.gouv.fr/publications/comment-mieux-reperer-les-femmes-victimes-de-violences-conjugales-lapport-des-sciences | https://www.modernisation.gouv.fr/publications/comment-mieux-reperer-les-femmes-victimes-de-violences-conjugales-lapport-des-sciences
QRY-018 | FETCH | FOUND | SRC-004 | https://www.modernisation.gouv.fr/publications/consommation-durable-les-sciences-comportementales-testent-laffichage-dun-indice-de | https://www.modernisation.gouv.fr/publications/consommation-durable-les-sciences-comportementales-testent-laffichage-dun-indice-de
QRY-019 | FETCH | FOUND | SRC-005 | https://www.modernisation.gouv.fr/publications/indice-de-reparabilite-quel-impact-sur-lachat-de-produits-plus-reparables | https://www.modernisation.gouv.fr/publications/indice-de-reparabilite-quel-impact-sur-lachat-de-produits-plus-reparables
QRY-020 | FETCH | FOUND | SRC-006 | https://www.modernisation.gouv.fr/publications/linsertion-professionnelle-des-personnes-en-situation-de-handicap | https://www.modernisation.gouv.fr/publications/linsertion-professionnelle-des-personnes-en-situation-de-handicap
QRY-021 | FETCH | FOUND | SRC-007 | https://www.modernisation.gouv.fr/publications/promouvoir-une-utilisation-raisonnee-des-ecrans-par-les-enfants | https://www.modernisation.gouv.fr/publications/promouvoir-une-utilisation-raisonnee-des-ecrans-par-les-enfants
QRY-022 | FETCH | FOUND | SRC-008 | https://www.modernisation.gouv.fr/publications/comment-promouvoir-une-consommation-raisonnee-des-antibiotiques-grace-aux-sciences | https://www.modernisation.gouv.fr/publications/comment-promouvoir-une-consommation-raisonnee-des-antibiotiques-grace-aux-sciences
QRY-023 | FETCH | FOUND | SRC-009 | https://www.modernisation.gouv.fr/publications/pollution-de-lair-interieur-faciliter-les-changements-de-comportements-grace-aux | https://www.modernisation.gouv.fr/publications/pollution-de-lair-interieur-faciliter-les-changements-de-comportements-grace-aux
QRY-024 | FETCH | FOUND | SRC-010 | https://www.modernisation.gouv.fr/publications/lutte-contre-la-fraude-leclairage-des-sciences-comportementales | https://www.modernisation.gouv.fr/publications/lutte-contre-la-fraude-leclairage-des-sciences-comportementales
QRY-025 | FETCH | FOUND | SRC-011 | https://www.has-sante.fr/jcms/p_3104867/fr/reperage-des-femmes-victimes-de-violences-au-sein-du-couple | https://www.has-sante.fr/jcms/p_3104867/fr/reperage-des-femmes-victimes-de-violences-au-sein-du-couple
QRY-026 | FETCH | FOUND | SRC-012 | https://www.legifrance.gouv.fr/eli/decret/2026/4/30/2026-339/jo/texte | https://www.legifrance.gouv.fr/eli/decret/2026/4/30/2026-339/jo/texte
QRY-027 | FETCH | FOUND | SRC-013 | https://www.oecd.org/en/publications/good-practice-principles-for-ethical-behavioural-science-in-public-policy_e19a9be9-en.html | https://www.oecd.org/en/publications/good-practice-principles-for-ethical-behavioural-science-in-public-policy_e19a9be9-en.html
QRY-028 | FETCH | FOUND | SRC-014 | https://doi.org/10.1073/pnas.2107346118 | https://doi.org/10.1073/pnas.2107346118

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | DITP Sciences comportementales | DITP Sciences comportementales | UNKNOWN | 2026-09-09T19:24:00Z | Page expertise sciences comportementales | https://www.modernisation.gouv.fr/accompagner-les-administrations/laboratoires-interministeriels-dinnovation/sciences
SRC-002 | ◈ | fam:A | DITP Mettre les sciences comportementales au coeur de action publique | DITP Mettre les sciences comportementales au coeur de action publique | 2022-05-18 | 2026-09-09T19:24:00Z | Triptyque diagnostic-prototypage-evaluation | https://www.modernisation.gouv.fr/actualites/mettre-les-sciences-comportementales-au-coeur-de-laction-publique
SRC-003 | ◈ | fam:A | DITP Violences conjugales | DITP Violences conjugales | 2022-11-21 | 2026-09-09T19:24:00Z | Resultats de experimentation | https://www.modernisation.gouv.fr/publications/comment-mieux-reperer-les-femmes-victimes-de-violences-conjugales-lapport-des-sciences
SRC-004 | ◈ | fam:A | DITP Indice reparabilite test affichage | DITP Indice reparabilite test affichage | 2020-09-24 | 2026-09-09T19:24:00Z | Experimentation 140000 consommateurs | https://www.modernisation.gouv.fr/publications/consommation-durable-les-sciences-comportementales-testent-laffichage-dun-indice-de
SRC-005 | ◈ | fam:A | DITP Indice reparabilite evaluation impact | DITP Indice reparabilite evaluation impact | 2023-12-07 | 2026-09-09T19:24:00Z | Evaluation ventes 2020-2022 | https://www.modernisation.gouv.fr/publications/indice-de-reparabilite-quel-impact-sur-lachat-de-produits-plus-reparables
SRC-006 | ◈ | fam:A | DITP Insertion professionnelle handicap | DITP Insertion professionnelle handicap | 2022-01-27 | 2026-09-09T19:24:00Z | ERC 111534 employeurs | https://www.modernisation.gouv.fr/publications/linsertion-professionnelle-des-personnes-en-situation-de-handicap
SRC-007 | ◈ | fam:A | DITP FAMINUM ecrans enfants | DITP FAMINUM ecrans enfants | 2022-02-07 | 2026-09-09T19:24:00Z | Etude pilote familles | https://www.modernisation.gouv.fr/publications/promouvoir-une-utilisation-raisonnee-des-ecrans-par-les-enfants
SRC-008 | ◈ | fam:A | DITP Antibiotiques sciences comportementales | DITP Antibiotiques sciences comportementales | 2022-04-21 | 2026-09-09T19:24:00Z | Diagnostic et prototypes prescriptions | https://www.modernisation.gouv.fr/publications/comment-promouvoir-une-consommation-raisonnee-des-antibiotiques-grace-aux-sciences
SRC-009 | ◈ | fam:A | DITP Pollution air interieur donnees personnalisees | DITP Pollution air interieur donnees personnalisees | 2020-09-03 | 2026-09-09T19:24:00Z | Experimentation capteurs Ile-de-France | https://www.modernisation.gouv.fr/publications/pollution-de-lair-interieur-faciliter-les-changements-de-comportements-grace-aux
SRC-010 | ◈ | fam:A | DITP Lutte contre fraude eclairage sciences comportementales | DITP Lutte contre fraude eclairage sciences comportementales | 2025-05-07 | 2026-09-09T19:24:00Z | Synthese 76 documents et limites | https://www.modernisation.gouv.fr/publications/lutte-contre-la-fraude-leclairage-des-sciences-comportementales
SRC-011 | ◈ | fam:B | HAS Reperage violences conjugales | HAS Reperage violences conjugales | 2022-11-23 | 2026-09-09T19:24:00Z | Recommandation, appropriation et barometres | https://www.has-sante.fr/jcms/p_3104867/fr/reperage-des-femmes-victimes-de-violences-au-sein-du-couple
SRC-012 | ◈ | fam:C | Legifrance decret experimentation signaux tarifaires electricite | Legifrance decret experimentation signaux tarifaires electricite | 2026-05-05 | 2026-09-09T19:24:00Z | Decret 2026-339 experimentation 6600 consommateurs | https://www.legifrance.gouv.fr/eli/decret/2026/4/30/2026-339/jo/texte
SRC-013 | ◉ | fam:D | OECD Good practice principles ethical behavioural science | OECD Good practice principles ethical behavioural science | 2022-10-05 | 2026-09-09T19:24:00Z | Principes ethiques BI politique publique | https://www.oecd.org/en/publications/good-practice-principles-for-ethical-behavioural-science-in-public-policy_e19a9be9-en.html
SRC-014 | ◉ | fam:E | PNAS Effectiveness of nudging meta-analysis | PNAS Effectiveness of nudging meta-analysis | 2022-01-04 | 2026-09-09T19:24:00Z | Meta-analyse choice architecture et biais publication | https://doi.org/10.1073/pnas.2107346118

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.modernisation.gouv.fr/accompagner-les-administrations/laboratoires-interministeriels-dinnovation/sciences | A | 2026-09-09 | DITP selection de projets comportementaux | La DITP indique selectionner ses projets notamment selon importance de enjeu, freins comportementaux, consensus ethique, engagement du partenaire et possibilite de mesurer impact. | -
FCT-002 | FACT | ✧ | https://www.modernisation.gouv.fr/accompagner-les-administrations/laboratoires-interministeriels-dinnovation/sciences | A | 2026-09-09 | DITP palette interventions | La DITP decrit des solutions pouvant relever de communication, outils numeriques ou evolution reglementaire; le champ comportemental ne se reduit donc pas au nudge au sens strict. | -
FCT-003 | FACT | ✧ | https://www.modernisation.gouv.fr/actualites/mettre-les-sciences-comportementales-au-coeur-de-laction-publique | A | 2026-09-09 | Triptyque DITP | La DITP formalise un triptyque diagnostic, prototypage de solutions et evaluation, idealement par essais randomises controles avant passage a echelle. | -
FCT-004 | FACT | ✧ | https://www.modernisation.gouv.fr/actualites/mettre-les-sciences-comportementales-au-coeur-de-laction-publique | A | 2026-09-09 | Definition nudge DITP | La DITP decrit le nudge comme une modification de architecture de choix qui favorise une option sans interdire les autres, tout en indiquant que son approche actuelle est plus large que le nudge. | -
FCT-005 | FACT | ✧ | https://www.modernisation.gouv.fr/publications/comment-mieux-reperer-les-femmes-victimes-de-violences-conjugales-lapport-des-sciences | A | 2026-09-09 | Violences conjugales effet mesure | Dans experimentation HAS-DITP, le groupe avec outils simplifiés passe de 2.5 a 4.4 depistages hebdomadaires par medecin environ, soit une hausse annoncee de 76 pour cent. | -
FCT-006 | FACT | ✧ | https://www.modernisation.gouv.fr/publications/comment-mieux-reperer-les-femmes-victimes-de-violences-conjugales-lapport-des-sciences | A | 2026-09-09 | Violences conjugales limite aval | Plus de quatre medecins sur dix rapportent encore un malaise a questionner les patientes; le resultat mesure porte sur le depistage, pas sur une amelioration causale demontree de la situation finale des victimes. | -
FCT-007 | FACT | ✧ | https://www.modernisation.gouv.fr/publications/consommation-durable-les-sciences-comportementales-testent-laffichage-dun-indice-de | A | 2026-09-09 | Reparabilite essai grandeur reelle | Le test du visuel de indice de reparabilite a implique environ 140000 consommateurs Darty en conditions reelles avec evaluation de type essai randomise controle. | -
FCT-008 | FACT | ✧ | https://www.modernisation.gouv.fr/publications/consommation-durable-les-sciences-comportementales-testent-laffichage-dun-indice-de | A | 2026-09-09 | Reparabilite objectif choix | Le test cherchait a rendre indice visible, comprehensible et comparable et a observer les comportements achat; il s agit d une architecture informationnelle explicite, non d une contrainte sur le choix. | -
FCT-009 | FACT | ✧ | https://www.modernisation.gouv.fr/publications/indice-de-reparabilite-quel-impact-sur-lachat-de-produits-plus-reparables | A | 2026-09-09 | Reparabilite effet mixte | Evaluation 2023 trouve un effet global positif mais non statistiquement significatif sur ventes de produits plus reparables; effet positif significatif en ligne et positif non significatif en magasin. | -
FCT-010 | FACT | ✧ | https://www.modernisation.gouv.fr/publications/indice-de-reparabilite-quel-impact-sur-lachat-de-produits-plus-reparables | A | 2026-09-09 | Reparabilite limite welfare | Evaluation ne pouvait pas mesurer impact sur la reparation effective des produits; comportement achat et resultat final de durabilite restent distincts. | -
FCT-011 | FACT | ✧ | https://www.modernisation.gouv.fr/publications/linsertion-professionnelle-des-personnes-en-situation-de-handicap | A | 2026-09-09 | Handi-bienveillante RCT | Pôle emploi et DITP ont mene un essai randomise sur 44 departements, 111534 employeurs pendant cinq mois pour tester une mention entreprise handi-bienveillante. | -
FCT-012 | FACT | ✧ | https://www.modernisation.gouv.fr/publications/linsertion-professionnelle-des-personnes-en-situation-de-handicap | A | 2026-09-09 | Handi-bienveillante generalisation limitee | La DITP rapporte environ deux fois plus de candidatures potentielles de personnes handicapees sur les offres avec mention, tout en disant que effet doit etre verifie a plus grande echelle. | -
FCT-013 | FACT | ✧ | https://www.modernisation.gouv.fr/publications/promouvoir-une-utilisation-raisonnee-des-ecrans-par-les-enfants | A | 2026-09-09 | FAMINUM pilote | FAMINUM a ete teste dans une etude pilote avec environ cent familles volontaires apres une enquete aupres de plus de 800 parents. | -
FCT-014 | FACT | ✧ | https://www.modernisation.gouv.fr/publications/promouvoir-une-utilisation-raisonnee-des-ecrans-par-les-enfants | A | 2026-09-09 | FAMINUM preuve limitee | Les premiers resultats portent surtout sur accueil positif, discussion familiale et perception; la page dit que outil semble permettre de nouvelles pratiques sans etablir un effet comportemental populationnel causal. | -
FCT-015 | FACT | ✧ | https://www.modernisation.gouv.fr/publications/comment-promouvoir-une-consommation-raisonnee-des-antibiotiques-grace-aux-sciences | A | 2026-09-09 | Antibiotiques contexte dependance | Dans le travail DITP sur antibiotiques, comparaison a des pairs ou normes sociales, souvent efficace ailleurs, est decrite comme potentiellement contre-productive avec le corps medical. | -
FCT-016 | FACT | ✧ | https://www.modernisation.gouv.fr/publications/comment-promouvoir-une-consommation-raisonnee-des-antibiotiques-grace-aux-sciences | A | 2026-09-09 | Antibiotiques outcome non ferme | La page decrit un diagnostic, des prototypes et une experimentation annoncee du profil prescripteur; elle ne fournit pas sur cette page un effet causal ferme sur les volumes de prescriptions. | -
FCT-017 | FACT | ✧ | https://www.modernisation.gouv.fr/publications/pollution-de-lair-interieur-faciliter-les-changements-de-comportements-grace-aux | A | 2026-09-09 | Air interieur personnalisation | Dans experimentation chauffage au bois, information generique modifie surtout perception tandis que donnees personnalisees par capteur sont rapportees comme declenchant davantage de changements de pratiques. | -
FCT-018 | FACT | ✧ | https://www.modernisation.gouv.fr/publications/pollution-de-lair-interieur-faciliter-les-changements-de-comportements-grace-aux | A | 2026-09-09 | Air interieur limite transferabilite | Le resultat provient de foyers participants et mesure une intervention de communication personnalisee; il ne suffit pas a etablir un effet national durable ou un gain de bien-etre general. | -
FCT-019 | FACT | ✧ | https://www.modernisation.gouv.fr/publications/lutte-contre-la-fraude-leclairage-des-sciences-comportementales | A | 2026-09-09 | Fraude prudence transfert | La synthese DITP fraude s appuie sur 76 documents mais souligne que beaucoup etudes sont en ligne ou etrangeres et invite a tester localement avant transposition en France. | -
FCT-020 | FACT | ✧ | https://www.modernisation.gouv.fr/publications/lutte-contre-la-fraude-leclairage-des-sciences-comportementales | A | 2026-09-09 | Fraude stigmatisation limite | La DITP note des enjeux ethiques et indique que la stigmatisation est loin d avoir prouve son efficacite, notamment pour fraudeurs volontaires. | -
FCT-021 | FACT | ✧ | https://www.has-sante.fr/jcms/p_3104867/fr/reperage-des-femmes-victimes-de-violences-au-sein-du-couple | B | 2026-09-09 | HAS but normatif preexistant | La HAS recommande de questionner systematiquement les patientes et a sollicite la DITP pour faciliter appropriation de cette recommandation; intervention comportementale sert ici un objectif clinique public preexistant. | -
FCT-022 | FACT | ✧ | https://www.has-sante.fr/jcms/p_3104867/fr/reperage-des-femmes-victimes-de-violences-au-sein-du-couple | B | 2026-09-09 | HAS barometres mise en oeuvre | Les barometres HAS 2022, 2023 et 2025 indiquent que questionnement est bien percu par les femmes mais reste encore peu mis en oeuvre, montrant un ecart entre intervention et adoption generale. | -
FCT-023 | FACT | ✧ | https://www.legifrance.gouv.fr/eli/decret/2026/4/30/2026-339/jo/texte | C | 2026-09-09 | Signaux tarifaires 6600 | Le decret 2026-339 prevoit une experimentation sur 6600 consommateurs selectionnes aleatoirement pour analyser adaptation de consommation a des signaux tarifaires. | -
FCT-024 | FACT | ✧ | https://www.legifrance.gouv.fr/eli/decret/2026/4/30/2026-339/jo/texte | C | 2026-09-09 | Signaux tarifaires categorie instrument | Le dispositif inclut une contrepartie financiere et collecte de donnees de consommation, avec rapport public attendu au plus tard en 2028; il releve davantage d une incitation economique experimentee que d un nudge pur et son effet est encore inconnu. | -
FCT-025 | FACT | ✧ | https://www.oecd.org/en/publications/good-practice-principles-for-ethical-behavioural-science-in-public-policy_e19a9be9-en.html | D | 2026-09-09 | Ethique behavioural science | OCDE recommande d integrer ethique a toutes les etapes des sciences comportementales publiques, notamment transparence, possibilite de sortie, interet public et voies de recours. | -
FCT-026 | FACT | ✧ | https://www.oecd.org/en/publications/good-practice-principles-for-ethical-behavioural-science-in-public-policy_e19a9be9-en.html | D | 2026-09-09 | Frontiere manipulation | Le cadre OCDE distingue interventions transparentes ou non et evitables ou non; une influence non transparente mais evitable est generalement traitee comme manipulation de design et non comme simple incitation neutre. | -
FCT-027 | FACT | ✧ | https://doi.org/10.1073/pnas.2107346118 | E | 2026-09-09 | Meta analyse effet moyen | La meta-analyse PNAS 2022 estime un effet moyen positif des interventions architecture de choix mais documente une forte heterogeneite entre domaines et interventions. | -
FCT-028 | FACT | ✧ | https://doi.org/10.1073/pnas.2107346118 | E | 2026-09-09 | Meta analyse biais publication | La meme meta-analyse detecte un biais de publication favorisant les resultats positifs; des analyses de sensibilite attenuent substantiellement effet moyen, ce qui interdit de traiter les nudges comme uniformement efficaces. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-002
FCT-004 | SRC-002
FCT-005 | SRC-003
FCT-006 | SRC-003
FCT-007 | SRC-004
FCT-008 | SRC-004
FCT-009 | SRC-005
FCT-010 | SRC-005
FCT-011 | SRC-006
FCT-012 | SRC-006
FCT-013 | SRC-007
FCT-014 | SRC-007
FCT-015 | SRC-008
FCT-016 | SRC-008
FCT-017 | SRC-009
FCT-018 | SRC-009
FCT-019 | SRC-010
FCT-020 | SRC-010
FCT-021 | SRC-011
FCT-022 | SRC-011
FCT-023 | SRC-012
FCT-024 | SRC-012
FCT-025 | SRC-013
FCT-026 | SRC-013
FCT-027 | SRC-014
FCT-028 | SRC-014

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
FCT-014 | ELIGIBLE:VERIFIE
FCT-015 | ELIGIBLE:VERIFIE
FCT-016 | ELIGIBLE:VERIFIE
FCT-017 | ELIGIBLE:VERIFIE
FCT-018 | ELIGIBLE:VERIFIE
FCT-019 | ELIGIBLE:VERIFIE
FCT-020 | ELIGIBLE:VERIFIE
FCT-021 | ELIGIBLE:VERIFIE
FCT-022 | ELIGIBLE:VERIFIE
FCT-023 | ELIGIBLE:VERIFIE
FCT-024 | ELIGIBLE:VERIFIE
FCT-025 | ELIGIBLE:VERIFIE
FCT-026 | ELIGIBLE:VERIFIE
FCT-027 | ELIGIBLE:VERIFIE
FCT-028 | ELIGIBLE:VERIFIE

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
FCT-014 | WRITE | -
FCT-015 | WRITE | -
FCT-016 | WRITE | -
FCT-017 | WRITE | -
FCT-018 | WRITE | -
FCT-019 | WRITE | -
FCT-020 | WRITE | -
FCT-021 | WRITE | -
FCT-022 | WRITE | -
FCT-023 | WRITE | -
FCT-024 | WRITE | -
FCT-025 | WRITE | -
FCT-026 | WRITE | -
FCT-027 | WRITE | -
FCT-028 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:search
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:facts
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:causal
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:verify
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:accountability
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:finalize

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-09T19:28:04.265618+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":28,"eligible":28,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:28;attempted:0;success:0;failure:0;blocked:28} | WRITEBACK_EXECUTION_V1:[28 rows, see section]

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
FCT-014 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-015 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-016 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-017 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-018 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-019 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-020 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-021 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-022 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-023 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-024 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-025 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-026 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-027 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-028 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
