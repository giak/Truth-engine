ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260910-1022-cambridge-analytica-targeting | PARENT_RUN_ID:NONE | AS_OF:2026-09-10
INPUT_KIND:RUN_CARD | MISSION_MODE:DEEPEN | INPUT_REF:PATH:/mnt/data/inv017/runtime/investigations/2026-09/2026-09-10_cambridge-analytica-targeting/2026-09-10_10-22_cambridge-analytica-targeting_INPUT.md | SUBJECT_SLUG:cambridge-analytica-targeting | SUBJECT_FP:sha256:979abe2681e6fca9aa47eb584ab3e4fba39b2ed42b71c2c6baf441b955088e94 | INPUT_SHA256:sha256:25e9317a02093cefcfba6f17fed7e004a0feea88360aefd360d7087e4dd9daad
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:UK/US mainly 2014-2018 plus regulatory and academic follow-up; data -> profiling -> targeting -> ad/exposure -> persuasion -> vote; separate vendor capability from executed use and electoral effect.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/NETWORK.md,clusters/INFORMATION.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Analytic body

## Object
INV-017 tests the Cambridge Analytica chain data -> psychometric/profile construction -> targeting -> advertising -> exposure -> persuasion -> vote -> election outcome. The central discipline is to prevent a real upstream capability from being promoted into an unmeasured downstream causal effect.

## Data acquisition and modelling
FTC and ICO findings close the upstream mechanism. Kogan/GSR collected Facebook data at scale; Cambridge Analytica participated in the project; an algorithm generated personality scores; those scores were matched to US voter records and used for voter profiling/targeted-advertising services [FCT-001,FCT-002,FCT-005,FCT-006,FCT-007,FCT-008]. The privacy and consent failures are independently material [FCT-003,FCT-004,FCT-009]. Facebook estimated up to 87 million people may have had information improperly shared [FCT-019].

Independent academic work establishes that Facebook Likes can carry predictive signal about political attributes and personality [FCT-021,FCT-022]. This supports technical plausibility, not Cambridge Analytica's accuracy for every voter.

## Campaign execution
Campaign engagement was real. FEC records show multi-million-dollar payments from both Trump and Cruz campaigns [FCT-011]. Nix described the Cruz method as combining OCEAN/behavioural communications, data analytics and ad placement [FCT-012]. For Trump he described substantial data/analytics, digital and data-driven TV work plus large-scale survey operations, while denying that psychographics were incorporated [FCT-013,FCT-014].

Ripon had OCEAN-search functionality, but Vickery explicitly could not say it was used in the Trump campaign [FCT-015,FCT-016]. Wylie argued that Facebook-derived model derivatives persisted into later work; this remains witness evidence rather than an independently reconstructed Trump ad-exposure chain [FCT-017]. Therefore campaign analytics/targeting execution is supported, but Trump-specific psychographic deployment to identifiable impressions remains unresolved.

## Capability versus persuasion
The experimental literature blocks both denial and inflation. Psychological matching has produced material click and purchase effects in large field experiments [FCT-023], showing a real persuasion/response capability class. But Brexit-framed experiments found weak or no convincing evidence for psychological tailoring itself in political decision-making [FCT-024], while validation studies show targeted ads can miss intended groups, especially statistically modelled or third-party targets [FCT-025]. These studies cannot be promoted into a Cambridge Analytica vote effect.

## Electoral causality
No source in the inspected corpus closes Cambridge Analytica service -> verified individual exposure -> persuasion -> changed vote -> counterfactual election outcome. Campaign payments and a winning election establish neither marginal contribution nor causal necessity [FCT-011,FCT-018]. The appropriate terminal status for election-result attribution is UNRESOLVED.

## Negative control: Leave.EU
The UK Electoral Commission found no evidence that Cambridge Analytica provided input to Leave.EU referendum campaigning beyond preliminary scoping, despite public claims of a stronger relationship [FCT-010,FCT-026]. This is a direct demonstration that vendor/campaign claims cannot substitute for execution evidence.

## Result
Cambridge Analytica was neither an imaginary capability nor a proven election-determining machine. The strongest supported chain is large-scale data acquisition -> personality/voter profiling capability -> material campaign analytics/targeting services. The Trump psychographic impression-level chain and marginal electoral effect are not closed. Reopen only on authenticated campaign/platform delivery logs or a credible independent causal vote-effect design.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:7|SRC_COMPLETE:16/16

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-10
- **breaks:**
  - 2014 GSR collection
  - 2015-2016 US campaign deployment
  - 2018 public scandal/regulatory investigations
  - 2019 FTC final action
  - 2020 political-targeting experiments
- **status:** HISTORICAL_CASE_CLOSED_WITH_REGULATORY_AND_ACADEMIC_FOLLOWUP
- **window:** 2014-2020 core; later methodological relevance

### MANIPULATION_REPORT
- **assumptions:**
  - regulatory findings accurately describe recovered evidence
  - parliamentary testimony is evidence of statements, not automatically truth
  - academic effects generalize only within their designs
- **clusters:**
  - POWER
  - NETWORK
  - INFORMATION
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - large datasets can enable targeting without ensuring model accuracy
  - campaign analytics may matter operationally without measurable election-level effect
  - psychographic capability can exist without proof of Trump-specific deployment
  - platform optimization can confound advertiser-level attribution
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - data harvesting
  - personality inference
  - voter-file matching
  - microtargeting
  - campaign analytics
  - surveying
  - ad delivery
  - psychological tailoring
  - vendor claim inflation
  - counterfactual election attribution
- **priorities:**
  - close data-to-model pipeline
  - separate Cruz from Trump execution
  - test exposure and target accuracy
  - test persuasion evidence
  - seek counterfactual electoral effect
  - use LeaveEU as negative control
- **query_guidance:** prefer FTC/ICO/Electoral Commission/FEC, parliamentary evidence and peer-reviewed experimental work; require campaign/platform logs for exposure and counterfactual design for election effect
- **rhetorical:**
  - **AUTH:** FTC/ICO/Electoral Commission/FEC/Parliament plus peer-reviewed studies
  - **BF:** no independent CA election-effect estimate
  - **DEM:** retain campaign and platform co-determinants
  - **FAC:** separate data, model, targeting, exposure, persuasion, vote
  - **NUM:** reported user counts, payments, survey scale and experiment sample sizes
- **speaker:**
  - **goal:** forensic separation of capacity, execution, exposure, persuasion and electoral effect
  - **target:** data -> profile -> target -> ad -> exposure -> persuasion -> vote -> election result
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** Facebook/GSR data
  - **S02:** consent
  - **S03:** personality score
  - **S04:** voter file
  - **S05:** campaign contract
  - **S06:** target segment
  - **S07:** creative/ad
  - **S08:** platform delivery
  - **S09:** exposure
  - **S10:** click/response
  - **S11:** attitude
  - **S12:** vote
  - **S13:** election outcome
  - **S14:** vendor claim
  - **S15:** counterfactual
- **threats:**
  - data=accuracy
  - profile=target execution
  - target=exposure
  - click=vote
  - vendor claim=fact
  - payment=effect
  - campaign win=vendor causality
  - Brexit allegation=LeaveEU execution

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - platform delivery logs
    - political field effect
  - **input_ids:**
    - FCT-001
    - FCT-023
    - FCT-024
    - FCT-025
  - **module:** clusters/INFORMATION.md
  - **negative_results:**
    - political tailoring effect weak/no convincing evidence
  - **not_computable:**
    - CA ad-level exposure denominator
  - **operations_applied:**
    - mapped profile-to-target chain
    - bounded experimental external validity
  - **reason:** separate targeting, delivery and persuasion
  - **result_ids:**
    - CLM-001
    - CLM-005
    - CAU-001
    - CAU-005
  - **status:** DONE
  - **trigger:** microtargeting and persuasive messaging
- **item 2:**
  - **gaps:**
    - campaign/platform logs
  - **input_ids:**
    - FCT-001
    - FCT-006
    - FCT-011
    - FCT-012
    - FCT-014
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - LeaveEU execution refuted
  - **not_computable:**
    - complete campaign vendor contribution denominator
  - **operations_applied:**
    - mapped GSR->CA->campaign relationships
  - **reason:** map data and operational relationships
  - **result_ids:**
    - CLM-001
    - CLM-003
    - CAU-001
    - CAU-003
  - **status:** DONE
  - **trigger:** data/platform/campaign vendor chain
- **item 3:**
  - **gaps:**
    - independent counterfactual design
  - **input_ids:**
    - FCT-010
    - FCT-011
    - FCT-018
    - FCT-024
    - FCT-026
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no counterfactual election effect
    - no LeaveEU campaign input
  - **not_computable:**
    - marginal votes caused by CA
  - **operations_applied:**
    - tested vendor-effect claim
    - applied negative control
  - **reason:** test capability against decision/result causality
  - **result_ids:**
    - CLM-006
    - CLM-007
    - CAU-006
  - **status:** DONE
  - **trigger:** claims of election manipulation/control

### SCOPING_REPORT
- **exclusions:**
  - generic social-media persuasion beyond CA relevance
  - equating data scale with model accuracy
  - equating targeting with exposure
  - equating campaign engagement with election causality
- **geo:** United Kingdom and United States
- **object_coverage:** HIGH_FOR_DATA_PIPELINE; HIGH_FOR_CAMPAIGN_SERVICE; MODERATE_FOR_TRUMP_PSYCHOGRAPHIC_EXECUTION; LOW_FOR_ELECTORAL_CAUSAL_EFFECT
- **object_question:** Dans le cas Cambridge Analytica, quelles chaînes données -> profilage/psychométrie -> ciblage -> publicité -> exposition sont effectivement documentées, et quelles preuves permettent de séparer capacité revendiquée, ciblage réellement exécuté, persuasion mesurée et effet électoral ?
- **period:** principalement 2014-2018, suites réglementaires et académiques nécessaires
- **subject:** Cambridge Analytica : données, psychométrie, microtargeting et différence entre capacité revendiquée et efficacité démontrée

### CREDO
- data access != psychometric accuracy
- targeting capability != delivered exposure
- exposure != persuasion
- persuasion != vote
- vendor claim != validated effect
- campaign payment != efficacy
- election outcome != attributable causal effect
- absence of evidence != evidence of absence

### COGNITIVE_MAP
- **continuum:**
  - data acquisition
  - personality inference
  - voter matching
  - campaign service
  - target definition
  - ad delivery
  - exposure
  - response/persuasion
  - vote
  - election outcome
- **core_model:** Cambridge Analytica had real data/profiling and campaign-targeting capabilities and performed material campaign analytics. The evidence does not collapse those facts into proven Trump psychographic impression-level deployment or a measurable causal effect on an election result.
- **rival_models:**
  - Cambridge Analytica did nothing operationally
  - Cambridge Analytica psychographics deterministically won elections
  - all targeting was generic analytics with no psychological component
  - large data access itself proves persuasion

### DIALECTICAL_MAP
- **antithesis:** Campaign-specific psychographic execution, actual exposure and marginal electoral effects are much less well evidenced than the headline claims.
- **synthesis:** The strongest supported model is data/profiling capability plus campaign analytics/targeting service; persuasion and election-result attribution remain separate, unresolved causal layers.
- **thesis:** Cambridge Analytica built and sold a real data-driven profiling/targeting capability and worked materially for US campaigns.

### RESOURCE_FLOW_MAP
- **flows:**
  - Facebook/GSR-derived data -> Cambridge Analytica modelling assets
  - campaign funds -> Cambridge Analytica services
  - voter files/surveys -> campaign analytics
  - target segments/creative -> platform advertising delivery
- **limits:**
  - FEC payments do not identify efficacy
  - no complete ad-level spend/exposure mapping tied to psychographic scores
  - platform optimization and other vendors confound marginal attribution

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** GSR/Kogan
  - **relation:** Facebook-derived data and survey inputs
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
  - **to:** Cambridge Analytica
- **item 2:**
  - **from:** Cambridge Analytica
  - **relation:** profiling, analytics and targeting services
  - **support:**
    - FCT-001
    - FCT-011
    - FCT-012
    - FCT-013
  - **to:** US political campaigns
- **item 3:**
  - **from:** Facebook platform
  - **relation:** data access then ad delivery / later access restrictions
  - **support:**
    - FCT-019
    - FCT-020
  - **to:** users, developers and advertisers
- **item 4:**
  - **from:** academic psychometric research
  - **relation:** capability/external-validity benchmark only
  - **support:**
    - FCT-021
    - FCT-022
    - FCT-023
    - FCT-024
    - FCT-025
  - **to:** inference and persuasion claims

### IMPACT_MAP
- **established:**
  - large-scale personal-data misuse/regulatory harm
  - profiling and targeted-advertising capability
  - material campaign analytics engagement
  - platform/regulatory reforms
- **not_established:**
  - impression-level psychographic exposure chain for Trump
  - marginal vote change caused by Cambridge Analytica
  - counterfactual 2016 election-result effect
- **partial:**
  - Trump-specific psychographic execution
  - target delivery accuracy
  - political persuasion external validity

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** Nix denied psychographic use for Trump and Vickery could not directly verify Ripon use
  - **issue:** Trump psychographic use
  - **pro:** Ripon OCEAN functionality and whistleblower derivative claims
  - **resolution:** CAMPAIGN_ANALYTICS_SUPPORTED_TRUMP_PSYCHOGRAPHIC_EXECUTION_UNRESOLVED
  - **support:**
    - FCT-012
    - FCT-015
    - FCT-016
    - FCT-017
- **item 2:**
  - **contra:** political tailoring study weak/no convincing effect and target delivery can be noisy
  - **issue:** capability versus efficacy
  - **pro:** academic predictive and behavioural targeting effects
  - **resolution:** CAPABILITY_SUPPORTED_POLITICAL_EFFECT_UNRESOLVED
  - **support:**
    - FCT-021
    - FCT-022
    - FCT-023
    - FCT-024
    - FCT-025
- **item 3:**
  - **contra:** Electoral Commission found no input beyond scoping
  - **issue:** LeaveEU claims
  - **pro:** public statements claimed CA involvement
  - **resolution:** LEAVEEU_EXECUTION_REFUTED
  - **support:**
    - FCT-010
    - FCT-026

### VERIFICATION_REPORT
- **downgraded:**
  - 87m users means 87m targeted
  - psychographic capability means Trump deployment
  - targeting means exposure
  - commercial click effect means vote effect
  - Trump victory means CA causality
- **fact_count:** 26
- **negative_controls:**
  - LeaveEU regulator finding
  - Nix denial of Trump psychographics
  - Vickery inability to verify Trump Ripon use
  - political tailoring weak/no convincing evidence
  - target delivery imperfection
- **provenance_families:** 4
- **query_count:** 19
- **source_count:** 16
- **verification:** 26 bounded facts linked to 16 sources across regulators, parliamentary evidence, platform records and peer-reviewed research, plus three explicit negative searches.

### EDI_REPORT
- **corpus:**
  - **limits:**
    - no complete psychographic ad-impression log for Trump
    - no independent counterfactual election-effect design
    - witness evidence conflicts on Trump psychographic deployment
  - **strength:** multi-regulator findings, FEC spending, parliamentary testimony and peer-reviewed capability/effect studies
- **decisive_claim_coverage:**
  - CLM-001
  - CLM-002
  - CLM-003
  - CLM-004
  - CLM-005
  - CLM-006
  - CLM-007
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** GSR/Cambridge Analytica/campaign/platform depending stage
  - **perspective:** data capability, execution, exposure, persuasion, electoral causality
  - **stratification:** data -> model -> campaign -> platform -> voter -> election
  - **temporal:** 2014-2018 core with 2019-2020 validation
- **edi:**
  - **coverage:** HIGH_FOR_DATA_PIPELINE; HIGH_FOR_CAMPAIGN_ENGAGEMENT; MODERATE_FOR_TRUMP_PSYCHOGRAPHIC_EXECUTION; LOW_FOR_ELECTION_CAUSAL_EFFECT
  - **independence:** STRONG_REGULATORY_PLUS_PARLIAMENTARY_AND_ACADEMIC_COUNTEREVIDENCE
- **source_counts:**
  - **A:** 6
  - **B:** 4
  - **C:** 1
  - **D:** 5
  - **total:** 16

### RESPONSIBILITY_MAP
- **LeaveEU_execution:** REFUTED_BY_REGULATOR_EVIDENCE
- **Trump_psychographic_execution:** UNRESOLVED
- **campaign_service:** Cambridge Analytica plus campaign teams and other vendors
- **data_collection:** Kogan/GSR with Cambridge Analytica/Nix involvement per FTC/ICO
- **electoral_outcome:** MULTICAUSAL; CA marginal effect NOT_ESTABLISHED
- **platform_delivery:** Facebook advertising system; impression-level mapping incomplete
- **regulatory_harm:** FTC/ICO findings establish privacy/data-processing violations or serious concerns

### NEXT_QUERIES
- Acquire authenticated Trump campaign/Facebook ad logs linking a psychographic segment to a specific creative, delivery denominator and voter exposure.
- Locate any independent campaign experiment or natural experiment estimating vote/turnout effect attributable specifically to Cambridge Analytica targeting.
- For Cruz, obtain platform-level ad archives or campaign files linking OCEAN score bins to creatives and delivery.
- Do not reopen Leave.EU absent new authenticated contract, invoice, campaign asset or execution record contradicting regulator findings.

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-003,QRY-004,QRY-012,QRY-013 | support:FCT-001,FCT-002,FCT-003,FCT-005,FCT-006,FCT-007,FCT-008,FCT-021,FCT-022 | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-005,FCT-006,FCT-007,FCT-008,FCT-021,FCT-022 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-004,QRY-006,QRY-007,QRY-008,QRY-011,QRY-016,QRY-005 | support:FCT-001,FCT-006,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-019,FCT-025,FCT-026 | counter:- | results:FCT-001,FCT-006,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-019,FCT-025,FCT-026 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018,QRY-019 | support:FCT-021,FCT-022,FCT-023,FCT-024,FCT-025 | counter:- | results:FCT-021,FCT-022,FCT-023,FCT-024,FCT-025 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-005,QRY-006,QRY-007,QRY-008,QRY-010,QRY-015,QRY-017,QRY-018,QRY-019 | support:FCT-010,FCT-011,FCT-012,FCT-015,FCT-016,FCT-018,FCT-024,FCT-026 | counter:- | results:FCT-010,FCT-011,FCT-012,FCT-015,FCT-016,FCT-018,FCT-024,FCT-026 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,QRY-003,QRY-004,SRC-001,SRC-003,SRC-004 | support:FCT-001,FCT-002,FCT-005,FCT-006,FCT-007,FCT-008 | counter:CTRL-001 | results:FCT-001,FCT-002,FCT-005,FCT-006,FCT-007,FCT-008,CTRL-001 | final:SUPPORTED | gap:SCOPE
CLM-002 | attempts:QRY-012,QRY-013,SRC-012,SRC-013 | support:FCT-021,FCT-022 | counter:CTRL-002 | results:FCT-021,FCT-022,CTRL-002 | final:SUPPORTED | gap:EXTERNAL_VALIDITY
CLM-003 | attempts:QRY-006,QRY-007,SRC-006,SRC-007 | support:FCT-011,FCT-012,FCT-013,FCT-014 | counter:CTRL-003 | results:FCT-011,FCT-012,FCT-013,FCT-014,CTRL-003 | final:SUPPORTED | gap:SCOPE
CLM-004 | attempts:QRY-008,QRY-009,SRC-008,SRC-009 | support:FCT-015,FCT-016,FCT-017 | counter:CTRL-004 | results:FCT-015,FCT-016,FCT-017,CTRL-004 | final:PARTIAL | gap:EXECUTION
CLM-005 | attempts:QRY-014,QRY-015,QRY-016,SRC-014,SRC-015,SRC-016 | support:FCT-023,FCT-024,FCT-025 | counter:CTRL-005 | results:FCT-023,FCT-024,FCT-025,CTRL-005 | final:SUPPORTED | gap:EXTERNAL_VALIDITY
CLM-006 | attempts:QRY-006,QRY-010,SRC-006,SRC-010 | support:FCT-011,FCT-018 | counter:CTRL-006 | results:FCT-011,FCT-018,CTRL-006 | final:PARTIAL | gap:CAUSALITY
CLM-007 | attempts:QRY-005,SRC-005 | support:FCT-026 | counter:CTRL-007 | results:FCT-026,CTRL-007 | final:REFUTED | gap:EXECUTION

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-001 | CLM | SUPPORTED | SCOPE | Execution at every campaign/ad impression is not identified.
CLM-002 | CLM | SUPPORTED | EXTERNAL_VALIDITY | Predictive signal in research samples does not validate CA model accuracy for every voter.
CLM-003 | CLM | SUPPORTED | SCOPE | Service scope differs by campaign and psychographic use on Trump remains disputed.
CLM-004 | CLM | PARTIAL | EXECUTION | Direct authenticated Trump deployment/ad-impression mapping is absent; Nix denied psychographic use and Vickery could not directly verify Ripon use.
CLM-005 | CLM | SUPPORTED | EXTERNAL_VALIDITY | Political tailoring evidence is weak and ad target delivery itself can be noisy.
CLM-006 | CLM | PARTIAL | CAUSALITY | No credible counterfactual or independent vote-effect estimate isolates Cambridge Analytica marginal impact.
CLM-007 | CLM | REFUTED | EXECUTION | Electoral Commission and ICO evidence found no working campaign relationship beyond initial scoping.
CAU-004 | CAU | UNRESOLVED | EXECUTION | Need authenticated campaign/ad platform logs linking profile segment, creative, delivery and voter exposure.
CAU-005 | CAU | UNRESOLVED | EXTERNAL_VALIDITY | Need political field experiment or natural experiment tied to CA-like targeting and vote behaviour.
CAU-006 | CAU | UNRESOLVED | CAUSALITY | Need independent exposure denominator and counterfactual vote-effect design.

SEMANTIC_COUNTS_V1:LED:0|CLM:7|AXS:4|CAU:6|CTRL:8|ACT:4

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Cambridge Analytica participated in a documented pipeline from Facebook-derived data to personality scoring, voter-file matching and targeted-advertising services.","claimant":"INV-017 synthesis","counter":"CTRL-001","gap":"Execution at every campaign/ad impression is not identified.","gap_type":"SCOPE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-005","FCT-006","FCT-007","FCT-008"]}
CLM-002 | {"claim":"Digital traces such as Facebook Likes can carry measurable signal about personality and political attributes.","claimant":"INV-017 synthesis","counter":"CTRL-002","gap":"Predictive signal in research samples does not validate CA model accuracy for every voter.","gap_type":"EXTERNAL_VALIDITY","materiality":"HIGH","status":"SUPPORTED","support":["FCT-021","FCT-022"]}
CLM-003 | {"claim":"Cambridge Analytica performed material data/analytics and targeting work for US presidential campaigns, including Cruz and Trump.","claimant":"INV-017 synthesis","counter":"CTRL-003","gap":"Service scope differs by campaign and psychographic use on Trump remains disputed.","gap_type":"SCOPE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-011","FCT-012","FCT-013","FCT-014"]}
CLM-004 | {"claim":"Psychographic targeting was definitely deployed through Cambridge Analytica to Trump voters and can be mapped to individual ad exposures.","claimant":"INV-017 synthesis","counter":"CTRL-004","gap":"Direct authenticated Trump deployment/ad-impression mapping is absent; Nix denied psychographic use and Vickery could not directly verify Ripon use.","gap_type":"EXECUTION","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-015","FCT-016","FCT-017"]}
CLM-005 | {"claim":"Psychological matching can change online behaviour under some conditions, but this validates a capability class rather than Cambridge Analytica electoral persuasion.","claimant":"INV-017 synthesis","counter":"CTRL-005","gap":"Political tailoring evidence is weak and ad target delivery itself can be noisy.","gap_type":"EXTERNAL_VALIDITY","materiality":"HIGH","status":"SUPPORTED","support":["FCT-023","FCT-024","FCT-025"]}
CLM-006 | {"claim":"Cambridge Analytica caused a measurable change in the 2016 US presidential election outcome.","claimant":"INV-017 synthesis","counter":"CTRL-006","gap":"No credible counterfactual or independent vote-effect estimate isolates Cambridge Analytica marginal impact.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-011","FCT-018"]}
CLM-007 | {"claim":"Cambridge Analytica materially operated Leave.EU referendum campaigning.","claimant":"INV-017 synthesis","counter":"CTRL-007","gap":"Electoral Commission and ICO evidence found no working campaign relationship beyond initial scoping.","gap_type":"EXECUTION","materiality":"DECISIVE","status":"REFUTED","support":["FCT-026"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-003","QRY-004","QRY-012","QRY-013"],"axis":"data_and_model_pipeline","inv_id":"INV-017","links":["INV-017"],"question":"What data acquisition and psychometric/profile construction chain is documented?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-005","FCT-006","FCT-007","FCT-008","FCT-021","FCT-022"],"sought_objects":["GSR data","personality scores","voter matching","predictive validity"],"status":"SATURATED","support":["FCT-001","FCT-002","FCT-003","FCT-005","FCT-006","FCT-007","FCT-008","FCT-021","FCT-022"]}
AXS-002 | {"attempt_ids":["QRY-001","QRY-004","QRY-006","QRY-007","QRY-008","QRY-011","QRY-016","QRY-005"],"axis":"campaign_execution_and_exposure","inv_id":"INV-017","links":["INV-017"],"question":"Which campaigns actually used Cambridge Analytica services and what targeting/exposure is documented?","result_ids":["FCT-001","FCT-006","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-019","FCT-025","FCT-026"],"sought_objects":["payments","campaign service","ad targeting","survey operations","platform delivery"],"status":"SATURATED","support":["FCT-001","FCT-006","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-019","FCT-025","FCT-026"]}
AXS-003 | {"attempt_ids":["QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018","QRY-019"],"axis":"psychographic_effectiveness","inv_id":"INV-017","links":["INV-017"],"question":"Does psychological targeting/tailoring causally change behaviour or political choice?","result_ids":["FCT-021","FCT-022","FCT-023","FCT-024","FCT-025"],"sought_objects":["field experiments","political experiments","target accuracy"],"status":"SATURATED","support":["FCT-021","FCT-022","FCT-023","FCT-024","FCT-025"]}
AXS-004 | {"attempt_ids":["QRY-005","QRY-006","QRY-007","QRY-008","QRY-010","QRY-015","QRY-017","QRY-018","QRY-019"],"axis":"electoral_causality_and_claims","inv_id":"INV-017","links":["INV-017"],"question":"Can Cambridge Analytica be assigned a marginal causal effect on an election result?","result_ids":["FCT-010","FCT-011","FCT-012","FCT-015","FCT-016","FCT-018","FCT-024","FCT-026"],"sought_objects":["vote effect","counterfactual","negative controls","vendor claims"],"status":"SATURATED","support":["FCT-010","FCT-011","FCT-012","FCT-015","FCT-016","FCT-018","FCT-024","FCT-026"]}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"profiling/targeting capability","counter":"CTRL-001","limit":"Capability/service chain does not identify every ad exposure.","mechanism":"Facebook/GSR data -> personality scores -> voter-record matching -> targeted-advertising service capability","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-005","FCT-006","FCT-007","FCT-008"]}
CAU-002 | {"causal_right":"predictive signal","counter":"CTRL-002","limit":"Research-sample validity does not equal CA-specific voter accuracy.","mechanism":"Facebook Likes/digital footprints -> inferred political/personality attributes","status":"SUPPORTED","support":["FCT-021","FCT-022"]}
CAU-003 | {"causal_right":"campaign service execution","counter":"CTRL-003","limit":"Does not isolate psychographic component or electoral effect.","mechanism":"campaign contract/payment -> CA analytics/targeting operations -> campaign decision support","status":"SUPPORTED","support":["FCT-011","FCT-012","FCT-013","FCT-014"]}
CAU-004 | {"counter":"CTRL-004","gap":"Need authenticated campaign/ad platform logs linking profile segment, creative, delivery and voter exposure.","gap_type":"EXECUTION","limit":"Trump-specific psychographic deployment and impression-level chain not closed.","mechanism":"psychographic profile -> tailored Trump ad -> verified exposure -> persuasion/vote","status":"UNRESOLVED","support":["FCT-015","FCT-016","FCT-017"]}
CAU-005 | {"counter":"CTRL-005","gap":"Need political field experiment or natural experiment tied to CA-like targeting and vote behaviour.","gap_type":"EXTERNAL_VALIDITY","limit":"Supported for some nonpolitical outcomes; political tailoring evidence weak/no convincing interaction.","mechanism":"psychological matching -> stronger response behaviour","status":"UNRESOLVED","support":["FCT-023","FCT-024","FCT-025"]}
CAU-006 | {"counter":"CTRL-006","gap":"Need independent exposure denominator and counterfactual vote-effect design.","gap_type":"CAUSALITY","limit":"Election result cannot identify vendor marginal effect.","mechanism":"Cambridge Analytica services -> changed votes -> 2016 election result","status":"UNRESOLVED","support":["FCT-011","FCT-018"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Data access does not prove psychometric accuracy or campaign use.","status":"DONE","support":["FCT-002","FCT-021","FCT-022"]}
CTRL-002 | {"control":"Predictive validity in research samples does not validate Cambridge Analytica model accuracy for each voter.","status":"DONE","support":["FCT-021","FCT-022"]}
CTRL-003 | {"control":"Targeting capability does not prove delivered exposure.","status":"DONE","support":["FCT-001","FCT-025"]}
CTRL-004 | {"control":"Exposure does not prove persuasion or vote change.","status":"DONE","support":["FCT-023","FCT-024"]}
CTRL-005 | {"control":"Vendor testimony/marketing claims are not independent effect evidence.","status":"DONE","support":["FCT-012","FCT-016","FCT-017","FCT-026"]}
CTRL-006 | {"control":"Campaign payment establishes engagement, not efficacy.","status":"DONE","support":["FCT-011"]}
CTRL-007 | {"control":"Leave.EU is a negative control: explored relationship != executed campaign service.","status":"DONE","support":["FCT-010","FCT-026"]}
CTRL-008 | {"control":"Election outcome does not identify Cambridge Analytica marginal causal effect without counterfactual.","status":"DONE","support":["FCT-018","FCT-024"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Keep data->profiling->targeting capability distinct from ad exposure and vote effect.","actor":"routing/control plane","intent":"prevent causal inflation","status":"DONE","support":["FCT-001","FCT-006","FCT-021","FCT-025"]}
ACT-002 | {"action":"Treat Trump psychographic deployment as unresolved unless campaign/platform logs close the chain.","actor":"routing/control plane","intent":"execution discipline","status":"DONE","support":["FCT-012","FCT-015","FCT-016"]}
ACT-003 | {"action":"Use experimental targeting literature only as capability/external-validity evidence, not CA election-effect proof.","actor":"routing/control plane","intent":"external validity discipline","status":"DONE","support":["FCT-023","FCT-024","FCT-025"]}
ACT-004 | {"action":"Refute generic Leave.EU execution claim on regulator evidence.","actor":"routing/control plane","intent":"negative control","status":"DONE","support":["FCT-010","FCT-026"]}

SEARCH_ACTIVITY_V1:WEB:3|FETCH:16|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL | mnemo | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.ftc.gov/news-events/news/press-releases/2019/07/ftc-sues-cambridge-analytica-settles-former-ceo-app-developer | FETCH FTC-CA-2019-07
QRY-002 | FETCH | FOUND | SRC-002 | https://www.ftc.gov/news-events/news/press-releases/2019/12/ftc-grants-final-approval-settlement-former-cambridge-analytica-ceo-app-developer-over-allegations | FETCH FTC-CA-2019-12
QRY-003 | FETCH | FOUND | SRC-003 | https://www.ftc.gov/business-guidance/blog/2019/07/ftc-sues-cambridge-analytica-deceptive-claims-about-consumers-personal-information | FETCH FTC-CA-BLOG-2019
QRY-004 | FETCH | FOUND | SRC-004 | https://ico.org.uk/media2/migrated/2260271/investigation-into-the-use-of-data-analytics-in-political-campaigns-final-20181105.pdf | FETCH ICO-POLITICAL-DATA-2018
QRY-005 | FETCH | FOUND | SRC-005 | https://www.electoralcommission.org.uk/cy/node/648 | FETCH EC-LEAVEEU-2018
QRY-006 | FETCH | FOUND | SRC-006 | https://www.fec.gov/files/legal/murs/7351/7351_01.pdf | FETCH FEC-MUR7351
QRY-007 | FETCH | FOUND | SRC-007 | https://committees.parliament.uk/oralevidence/7660/html/ | FETCH UKP-NIX-2018-02
QRY-008 | FETCH | FOUND | SRC-008 | https://committees.parliament.uk/oralevidence/7921/html/ | FETCH UKP-VICKERY-2018-05
QRY-009 | FETCH | FOUND | SRC-009 | https://committees.parliament.uk/writtenevidence/89475/html/ | FETCH UKP-WYLIE-2018
QRY-010 | FETCH | FOUND | SRC-010 | https://publications.parliament.uk/pa/cm201719/cmselect/cmcumeds/1791/179104.htm | FETCH UKP-DCMS-2019
QRY-011 | FETCH | FOUND | SRC-011 | https://about.fb.com/news/2018/04/restricting-data-access/ | FETCH META-CA-2018
QRY-012 | FETCH | FOUND | SRC-012 | https://doi.org/10.1073/pnas.1218772110 | FETCH PNAS-LIKES-2013
QRY-013 | FETCH | FOUND | SRC-013 | https://pubmed.ncbi.nlm.nih.gov/25583507/ | FETCH PNAS-PERSONALITY-2015
QRY-014 | FETCH | FOUND | SRC-014 | https://doi.org/10.1073/pnas.1710966114 | FETCH PNAS-TARGETING-2017
QRY-015 | FETCH | FOUND | SRC-015 | https://www.cambridge.org/core/journals/experimental-results/article/evidence-of-psychological-targeting-but-not-psychological-tailoring-in-political-persuasion-around-brexit/55AFE19E5B1AC95BA4E02DC2DFDF25FC | FETCH CAMBRIDGE-BREXIT-2020
QRY-016 | FETCH | FOUND | SRC-016 | https://www.cambridge.org/core/journals/political-science-research-and-methods/article/missing-the-target-using-surveys-to-validate-social-media-ad-targeting/6D5793AD64168C6928F3B886F8A0C117 | FETCH PSRM-TARGETING-2019
QRY-017 | WEB | NON_TROUVE | - | - | Cambridge Analytica independent causal estimate psychographic targeting changed 2016 US election result vote counterfactual
QRY-018 | WEB | NON_TROUVE | - | - | Cambridge Analytica Leave.EU evidence campaign services contract beyond preliminary scoping
QRY-019 | WEB | NON_TROUVE | - | - | Cambridge Analytica Trump campaign authenticated psychographic ad exposure individual persuasion vote effect dataset

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | FTC-CA-2019-07 | FTC sues Cambridge Analytica | 2019-07-24 | 2026-09-10T08:45:35Z | data harvest personality scores voter records targeting | https://www.ftc.gov/news-events/news/press-releases/2019/07/ftc-sues-cambridge-analytica-settles-former-ceo-app-developer
SRC-002 | ◈ | fam:A | FTC-CA-2019-12 | FTC final settlement Kogan Nix | 2019-12-18 | 2026-09-10T08:45:35Z | final settlement deceptive collection | https://www.ftc.gov/news-events/news/press-releases/2019/12/ftc-grants-final-approval-settlement-former-cambridge-analytica-ceo-app-developer-over-allegations
SRC-003 | ◈ | fam:A | FTC-CA-BLOG-2019 | FTC detailed Cambridge Analytica case blog | 2019-07-24 | 2026-09-10T08:45:35Z | GSR app scale and workflow | https://www.ftc.gov/business-guidance/blog/2019/07/ftc-sues-cambridge-analytica-deceptive-claims-about-consumers-personal-information
SRC-004 | ◈ | fam:A | ICO-POLITICAL-DATA-2018 | ICO political data analytics investigation | 2018-11-06 | 2026-09-10T08:45:35Z | Cambridge Analytica data use and LeaveEU findings | https://ico.org.uk/media2/migrated/2260271/investigation-into-the-use-of-data-analytics-in-political-campaigns-final-20181105.pdf
SRC-005 | ◈ | fam:A | EC-LEAVEEU-2018 | Electoral Commission Leave.EU investigation | 2018-05-11 | 2026-09-10T08:45:35Z | no CA campaign input beyond scoping | https://www.electoralcommission.org.uk/cy/node/648
SRC-006 | ◈ | fam:A | FEC-MUR7351 | FEC MUR 7351 complaint record | 2020-09-01 | 2026-09-10T08:45:35Z | campaign disbursements to Cambridge Analytica | https://www.fec.gov/files/legal/murs/7351/7351_01.pdf
SRC-007 | ◈ | fam:B | UKP-NIX-2018-02 | UK Parliament oral evidence Alexander Nix 27 Feb 2018 | 2018-02-27 | 2026-09-10T08:45:35Z | Cruz psychographics Trump analytics testimony | https://committees.parliament.uk/oralevidence/7660/html/
SRC-008 | ◈ | fam:B | UKP-VICKERY-2018-05 | UK Parliament oral evidence Chris Vickery 2 May 2018 | 2018-05-02 | 2026-09-10T08:45:35Z | Ripon OCEAN functionality and uncertainty | https://committees.parliament.uk/oralevidence/7921/html/
SRC-009 | ◈ | fam:B | UKP-WYLIE-2018 | UK Parliament written evidence Christopher Wylie | 2018-04-01 | 2026-09-10T08:45:35Z | whistleblower claims on GSR derivatives | https://committees.parliament.uk/writtenevidence/89475/html/
SRC-010 | ◈ | fam:B | UKP-DCMS-2019 | UK Parliament Disinformation final report | 2019-02-18 | 2026-09-10T08:45:35Z | data misuse targeting inquiry scope | https://publications.parliament.uk/pa/cm201719/cmselect/cmcumeds/1791/179104.htm
SRC-011 | ◈ | fam:C | META-CA-2018 | Meta/Facebook restricting data access update | 2018-04-04 | 2026-09-10T08:45:35Z | up to 87 million and API restrictions | https://about.fb.com/news/2018/04/restricting-data-access/
SRC-012 | ◈ | fam:D | PNAS-LIKES-2013 | PNAS private traits from Facebook Likes | 2013-03-11 | 2026-09-10T08:45:35Z | predictive validity of Likes | https://doi.org/10.1073/pnas.1218772110
SRC-013 | ◈ | fam:D | PNAS-PERSONALITY-2015 | PNAS computer personality judgments | 2015-01-12 | 2026-09-10T08:45:35Z | personality prediction from Likes | https://pubmed.ncbi.nlm.nih.gov/25583507/
SRC-014 | ◈ | fam:D | PNAS-TARGETING-2017 | PNAS psychological targeting mass persuasion | 2017-11-13 | 2026-09-10T08:45:35Z | field experiments clicks purchases | https://doi.org/10.1073/pnas.1710966114
SRC-015 | ◈ | fam:D | CAMBRIDGE-BREXIT-2020 | Experimental Results Brexit targeting/tailoring | 2020-09-18 | 2026-09-10T08:45:35Z | weak/no tailoring political persuasion | https://www.cambridge.org/core/journals/experimental-results/article/evidence-of-psychological-targeting-but-not-psychological-tailoring-in-political-persuasion-around-brexit/55AFE19E5B1AC95BA4E02DC2DFDF25FC
SRC-016 | ◈ | fam:D | PSRM-TARGETING-2019 | PSRM Missing the Target | 2019-03-01 | 2026-09-10T08:45:35Z | targeting accuracy validation | https://www.cambridge.org/core/journals/political-science-research-and-methods/article/missing-the-target-using-surveys-to-validate-social-media-ad-targeting/6D5793AD64168C6928F3B886F8A0C117

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.ftc.gov/news-events/news/press-releases/2019/07/ftc-sues-cambridge-analytica-settles-former-ceo-app-developer | A | 2014 | GSR workflow | FTC states Kogan, Cambridge Analytica and Nix developed, used and analysed GSRApp data, trained an algorithm generating personality scores, matched scores to US voter records, and used them for voter profiling and targeted-advertising services. | -
FCT-002 | FACT | ✧ | https://www.ftc.gov/news-events/news/press-releases/2019/07/ftc-sues-cambridge-analytica-settles-former-ceo-app-developer | A | 2014 | direct users and friends scale | FTC alleges 250,000-270,000 US app users plus 50-65 million friends were collected, including at least 30 million identifiable US consumers. | -
FCT-003 | FACT | ✧ | https://www.ftc.gov/news-events/news/press-releases/2019/07/ftc-sues-cambridge-analytica-settles-former-ceo-app-developer | A | 2014 | deceptive collection | FTC alleges app users were falsely told identifiable information would not be downloaded even though Facebook User IDs were collected. | -
FCT-004 | FACT | ✧ | https://www.ftc.gov/news-events/news/press-releases/2019/12/ftc-grants-final-approval-settlement-former-cambridge-analytica-ceo-app-developer-over-allegations | A | 2019-12-18 | final enforcement | FTC granted final approval to settlements with Kogan and Nix requiring deletion/destruction of GSRApp-derived personal information and restricting deceptive representations. | -
FCT-005 | FACT | ✧ | https://www.ftc.gov/business-guidance/blog/2019/07/ftc-sues-cambridge-analytica-deceptive-claims-about-consumers-personal-information | A | 2014 | profiling purpose | FTC describes the collaboration goal as using Facebook information to offer voter profiling, microtargeting and other services to US campaigns and clients. | -
FCT-006 | FACT | ✧ | https://ico.org.uk/media2/migrated/2260271/investigation-into-the-use-of-data-analytics-in-political-campaigns-final-20181105.pdf | A | 2018-11-06 | global and UK scale | ICO reports the app harvested data of up to 87 million Facebook users globally, including about one million in the UK, and that some data was used by Cambridge Analytica to target voters during the 2016 US presidential campaign process. | -
FCT-007 | FACT | ✧ | https://ico.org.uk/media2/migrated/2260271/investigation-into-the-use-of-data-analytics-in-political-campaigns-final-20181105.pdf | A | 2018-11-06 | political inference without awareness | ICO says users and friends were not made aware their data would be provided to Cambridge Analytica, used for political campaigning, or processed to infer political opinions, preferences and voting behaviour. | -
FCT-008 | FACT | ✧ | https://ico.org.uk/media2/migrated/2260271/investigation-into-the-use-of-data-analytics-in-political-campaigns-final-20181105.pdf | A | 2018-11-06 | commercialisation and control | ICO reports evidence that Cambridge Analytica sought Kogan expertise/access to research-basis Facebook data and was active in controlling the manner and frequency of harvesting. | -
FCT-009 | FACT | ✧ | https://ico.org.uk/media2/migrated/2260271/investigation-into-the-use-of-data-analytics-in-political-campaigns-final-20181105.pdf | A | 2018-11-06 | regulatory seriousness | ICO states it intended a substantial fine for serious unfair-processing breaches had the company still existed in original form. | -
FCT-010 | FACT | ✧ | https://www.electoralcommission.org.uk/cy/node/648 | A | 2018 | LeaveEU negative control | Electoral Commission found no evidence Cambridge Analytica had input into Leave.EU referendum campaigning; relationship did not progress beyond preliminary meetings/presentations and no contract was evidenced. | -
FCT-011 | FACT | ✧ | https://www.fec.gov/files/legal/murs/7351/7351_01.pdf | A | 2015-2016 | campaign payments | FEC record lists 2016-cycle disbursements of about $5.9125m by Donald J. Trump for President and about $5.8056m by Cruz for President to Cambridge Analytica. | -
FCT-012 | FACT | ✧ | https://committees.parliament.uk/oralevidence/7660/html/ | B | 2016 | Cruz psychographic method testimony | Alexander Nix testified that the Cruz approach combined behavioural communications/OCEAN psychological profiling, data analytics and ad placement. | -
FCT-013 | FACT | ✧ | https://committees.parliament.uk/oralevidence/7660/html/ | B | 2016 | Trump service scope testimony | Nix testified Cambridge Analytica pivoted technology from Cruz to Trump but focused on data/analytics, tech, digital and data-driven TV, claiming psychographics were not incorporated because of time/resources. | -
FCT-014 | FACT | ✧ | https://committees.parliament.uk/oralevidence/7660/html/ | B | 2016 | Trump survey scale testimony | Nix testified Cambridge Analytica helped run roughly 350,000-400,000 surveys per month for the Trump campaign over about five months. | -
FCT-015 | FACT | ✧ | https://committees.parliament.uk/oralevidence/7921/html/ | B | 2018 | Ripon OCEAN functionality | Chris Vickery testified that Ripon had the ability to search people using OCEAN psychographic scores. | -
FCT-016 | FACT | ✧ | https://committees.parliament.uk/oralevidence/7921/html/ | B | 2018 | Trump Ripon uncertainty | Vickery explicitly said he could not say Ripon was used in the Trump campaign and had not found material directly showing where it was used. | -
FCT-017 | FACT | ✧ | https://committees.parliament.uk/writtenevidence/89475/html/ | B | 2018 | whistleblower derivative claim | Christopher Wylie submitted that CA models had been trained using GSR Facebook-derived data and argued derivatives could persist even when original data were not directly used; this is witness evidence, not independent causal validation. | -
FCT-018 | FACT | ✧ | https://publications.parliament.uk/pa/cm201719/cmselect/cmcumeds/1791/179104.htm | B | 2019 | parliament inquiry boundary | The UK Parliament final report treated Cambridge Analytica/AggregateIQ data misuse and targeting as a central inquiry strand, but parliamentary findings do not themselves estimate Cambridge Analytica marginal vote effects. | -
FCT-019 | FACT | ✧ | https://about.fb.com/news/2018/04/restricting-data-access/ | C | 2018-04 | platform scale estimate | Facebook stated information of up to 87 million people, mostly in the US, may have been improperly shared with Cambridge Analytica. | -
FCT-020 | FACT | ✧ | https://about.fb.com/news/2018/04/restricting-data-access/ | C | 2018-04 | platform response | Facebook announced restrictions on data access and app controls in response to the incident, establishing a downstream governance effect distinct from electoral persuasion. | -
FCT-021 | FACT | ✧ | https://doi.org/10.1073/pnas.1218772110 | D | 2013 | digital footprint predictive signal | PNAS showed Facebook Likes can predict sensitive attributes including political views and personality; Democrat/Republican discrimination reached about 85% in that study sample. | -
FCT-022 | FACT | ✧ | https://pubmed.ncbi.nlm.nih.gov/25583507/ | D | 2015 | personality prediction validity | A PNAS study of 86,220 volunteers found computer personality judgments from Facebook Likes correlated r=0.56 with questionnaire scores and exceeded judgments by Facebook friends at r=0.49. | -
FCT-023 | FACT | ✧ | https://doi.org/10.1073/pnas.1710966114 | D | 2017 | psychological matching behavioural effect | Three field experiments reaching over 3.5 million people found psychologically matched advertising increased clicks and purchases, with reported increases up to 40% and 50%; outcomes were commercial behaviour, not votes. | -
FCT-024 | FACT | ✧ | https://www.cambridge.org/core/journals/experimental-results/article/evidence-of-psychological-targeting-but-not-psychological-tailoring-in-political-persuasion-around-brexit/55AFE19E5B1AC95BA4E02DC2DFDF25FC | D | 2020 | political tailoring weak evidence | Two Brexit-framed experiments found clear targeting differences but weak or no convincing evidence that psychological tailoring itself changed political decision-making. | -
FCT-025 | FACT | ✧ | https://www.cambridge.org/core/journals/political-science-research-and-methods/article/missing-the-target-using-surveys-to-validate-social-media-ad-targeting/6D5793AD64168C6928F3B886F8A0C117 | D | 2019 | target delivery imperfection | Validation across 20 social-media targeted ads found target-hit rates ranging from 24% to 99.8%, with lower success for statistically modelled and third-party targets than self-reported characteristics. | -
FCT-026 | FACT | ✧ | https://www.electoralcommission.org.uk/cy/node/648 | A | 2018 | claim execution distinction | Public claims that Cambridge Analytica had supercharged Leave.EU were contradicted by the Electoral Commission evidence record, which found no campaign input beyond scoping; vendor/public claims therefore cannot substitute for execution evidence. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-002
FCT-005 | SRC-003
FCT-006 | SRC-004
FCT-007 | SRC-004
FCT-008 | SRC-004
FCT-009 | SRC-004
FCT-010 | SRC-005
FCT-011 | SRC-006
FCT-012 | SRC-007
FCT-013 | SRC-007
FCT-014 | SRC-007
FCT-015 | SRC-008
FCT-016 | SRC-008
FCT-017 | SRC-009
FCT-018 | SRC-010
FCT-019 | SRC-011
FCT-020 | SRC-011
FCT-021 | SRC-012
FCT-022 | SRC-013
FCT-023 | SRC-014
FCT-024 | SRC-015
FCT-025 | SRC-016
FCT-026 | SRC-005

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

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:search
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:facts
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:causal
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:verify
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:accountability
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:finalize

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-10T08:55:10.599001+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":26,"eligible":26,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:26;attempted:0;success:0;failure:0;blocked:26} | WRITEBACK_EXECUTION_V1:[26 rows, see section]

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
