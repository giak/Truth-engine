ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260909-1331-generative-ai-deepfake-influence | PARENT_RUN_ID:NONE | AS_OF:2026-09-09
INPUT_KIND:RUN_CARD | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/inv092/runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-09_generative-ai-deepfake-influence/2026-09-09_13-31_generative-ai-deepfake-influence_INPUT.md | SUBJECT_SLUG:generative-ai-deepfake-influence | SUBJECT_FP:sha256:36885ad1614b4910133d6532a4ef7d51ca07b21ffc3560ded8894a3ea254a776 | INPUT_SHA256:sha256:13251f9f953557baeba51fd43c9ea2383e68c6231e3ba27b023773e0f099a11e
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France and European Union, mainly 2022-2026, with international comparators only where necessary; trace actor/operator -> model/tool -> synthetic/manipulated/automated content -> distribution/targeting -> exposure/reach -> detection/countermeasure -> persuasion/opinion/behavior/participation/vote -> democratic effect, separating technical capability, operational deployment, exposure, persuasion and electoral impact.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/NETWORK.md,clusters/POWER.md,clusters/CONFIRMATION.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Analyse technique

## Delta principal
Les sources attribuées convergent sur un changement opérationnel réel : les outils génératifs réduisent la friction de production, de traduction et de reformulation et permettent davantage de volume et de cadence. Cette capacité n'abolit pas le problème de distribution : plusieurs opérations observées restent sans audience authentique substantielle ou sans percée mesurable.

## Prévalence et exposition
Les incidents liés à l'IA sont désormais fréquents dans les corpus de menace, mais leur comptage ne fournit pas un dénominateur d'exposition. Les mesures disponibles sur plusieurs élections montrent que la part virale ou nuisible peut rester faible. Une opération détectée, un contenu synthétique ou une forte visibilité ponctuelle ne sont donc pas assimilés à une exposition populationnelle.

## Persuasion
Les expériences randomisées récentes établissent qu'une conversation politique interactive avec un système d'IA et des messages générés par LLM peuvent déplacer préférences déclarées, choix rapportés ou attitudes. Cette arête est causale dans le cadre expérimental. Les expériences sur deepfakes montrent parallèlement une détection imparfaite, sans avantage général de crédibilité par rapport aux autres formats de désinformation.

## Plafond causal
Le corpus inspecté ne fournit pas de design France/UE reliant une exposition identifiée à une opération générative ou automatisée à un vote réel puis à un résultat électoral avec contrefactuel crédible. Le modèle soutenu est donc : gain d'échelle et de productivité opérationnelle vérifié ; persuasion sous exposition contrôlée vérifiée ; effet électoral de terrain France/UE non identifié.

## Falsificateurs
Le modèle devrait être révisé si un jeu de données France/UE relie une opération attribuée, son exposition authentique, un changement comportemental et un résultat électoral ; ou si une nouvelle capacité établit un avantage de distribution/persuasion impossible à expliquer par les anciens playbooks accélérés.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:6|SRC_COMPLETE:16/16

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-09
- **notes:**
  - operational threat reporting current through September 2026
  - field election evidence concentrates on 2024-2025 elections
  - experimental persuasion evidence published 2025
  - future capability projections are not treated as observed effects
- **status:** CURRENT_WITH_2024_2025_ELECTION_COMPARATORS
- **window:** 2022-2026

### MANIPULATION_REPORT
- **assumptions:**
  - reported platform disruptions are bounded to their observed networks
  - experimental effects are not field-election estimates
  - cross-country observational denominators are not France/EU population estimates
- **clusters:**
  - **loaded:**
    - clusters/NETWORK.md
    - clusters/POWER.md
    - clusters/CONFIRMATION.md
- **complexity:**
  - **band:** HIGH
  - **score:** 9
- **implicit:**
  - automation value may lie in throughput rather than persuasion quality
  - distribution and authentic audience acquisition remain independent constraints
  - experimental persuasion may matter more for interactive targeting than static deepfakes
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - generative AI
  - deepfake
  - automated content
  - multilingual scaling
  - covert influence
  - distribution
  - exposure
  - persuasion
  - election effect
- **priorities:**
  - operational deployment
  - scale/productivity delta
  - exposure denominator
  - experimental persuasion
  - field electoral effect
- **query_guidance:** use attributed operational sources for deployment; measured datasets for prevalence/exposure; randomized evidence for persuasion; require field counterfactual for election effect.
- **rhetorical:**
  - **AUTH:** official/platform threat reports establish observed operations, not democratic effect
  - **BF:** headline incident counts require denominators
  - **DEM:** apply same causal standard to domestic and foreign AI use
  - **FAC:** separate production, distribution, exposure, persuasion, behavior and outcome
  - **NUM:** retain election, platform and denominator context
- **speaker:**
  - **goal:** forensic causal discrimination
  - **target:** tool -> content -> distribution -> exposure -> persuasion -> behavior -> electoral effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **Κ:** 4
  - **Λ:** 4
  - **Ξ:** 5
  - **Σ:** 4
  - **Φ:** 5
  - **Ψ:** 5
  - **Ω:** 4
  - **κ:** 4
  - **ρ:** 4
  - **€:** 4
  - **↕:** 5
  - **⏰:** 5
  - **⚔:** 5
  - **⫸:** 5
  - **🌐:** 5
- **threats:**
  - capability=deployment
  - incident=prevalence
  - detection=exposure
  - reach=persuasion
  - virality=behavior
  - experiment=field effect
  - attribution=effect
  - deepfake=unique persuasion

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - field exposure denominator
  - **input_ids:**
    - FCT-003
    - FCT-005
    - FCT-012
    - FCT-014
    - FCT-016
    - FCT-019
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no common distribution breakthrough established
  - **not_computable:**
    - cross-platform authentic audience denominator
  - **operations_applied:**
    - mapped operator/tool/content/distribution distinction
  - **reason:** separate content generation from channel distribution and authentic audience acquisition
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CAU-001
    - CAU-002
  - **status:** DONE
  - **trigger:** covert influence operations and distribution networks
- **item 2:**
  - **gaps:**
    - France/EU field causal design
  - **input_ids:**
    - FCT-004
    - FCT-007
    - FCT-022
    - FCT-023
    - FCT-024
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no France/EU election-result causal estimate found in inspected corpus
  - **not_computable:**
    - population vote effect without field exposure/outcome linkage
  - **operations_applied:**
    - separated experimental persuasion from field electoral impact
  - **reason:** bound operational capacity against measurable opinion/behavior/election effects
  - **result_ids:**
    - CLM-004
    - CLM-005
    - CLM-006
    - CAU-003
    - CAU-004
  - **status:** DONE
  - **trigger:** potential democratic effect from scalable persuasion
- **item 3:**
  - **gaps:**
    - comparable denominators
  - **input_ids:**
    - FCT-001
    - FCT-006
    - FCT-010
    - FCT-018
    - FCT-026
    - FCT-027
    - FCT-028
  - **module:** clusters/CONFIRMATION.md
  - **negative_results:**
    - deepfakes not uniquely credible relative to other misinformation
    - several measured election samples show low harmful/viral share
  - **not_computable:**
    - uniform global prevalence because detection/reporting regimes differ
  - **operations_applied:**
    - compared high incident counts with measured prevalence/reach and credibility controls
  - **reason:** test whether incident visibility or novelty is being mistaken for prevalence and effect
  - **result_ids:**
    - CLM-003
    - CLM-004
    - CAU-005
  - **status:** DONE
  - **trigger:** high-salience deepfake and AI-election narratives

### SCOPING_REPORT
- **actors_institutions:**
  - EEAS
  - VIGINUM
  - platform threat-intelligence teams
  - election monitors
  - influence operators
  - voters/users
  - research institutions
- **domains:**
  - generative AI
  - deepfakes
  - automated influence
  - election integrity
  - political persuasion
- **evidence_limits:**
  - cross-platform exposure denominator incomplete
  - platform reports cover observed/disrupted networks not full universe
  - field causal election evidence sparse
- **exclusions:**
  - future capability treated as present deployment
  - incident counts treated as effect
  - experimental persuasion treated as election outcome
  - foreign observations extrapolated to France/EU
- **geo:** France and European Union with bounded international comparators
- **period:** 2022-2026

### CREDO
- capability != deployment
- synthetic != deceptive
- detection != exposure
- reach != persuasion
- virality != behavior
- automation != coordination
- attribution != effect
- incident != prevalence
- experiment != field election effect
- foreign comparator != France/EU effect

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - deployment
  - production scale
  - distribution
  - exposure
  - persuasion
  - behavior
  - electoral effect
- **priorities:**
  - operational evidence
  - denominators
  - causal persuasion
  - field effect
- **query_guidance:** move one edge at a time; reject novelty as a proxy for effect.
- **speaker:**
  - **goal:** forensic causal discrimination
  - **target:** AI capability -> operation -> exposure -> persuasion -> effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **threats:**
  - novelty bias
  - availability bias
  - incident denominator neglect
  - experimental external-validity overreach

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** Operational reports mostly show workflow acceleration and old playbooks, with limited measured audience breakout.
  - **support:**
    - FCT-002
    - FCT-012
    - FCT-015
    - FCT-017
  - **synthesis:** A real scale/productivity delta is established; a qualitatively new field electoral effect is not.
  - **thesis:** Generative AI creates a qualitatively new election-manipulation regime.
- **item 2:**
  - **antithesis:** Experiments show imperfect detection but credibility roughly comparable to other misinformation.
  - **support:**
    - FCT-025
    - FCT-026
  - **synthesis:** Realism can impair discernment without proving a unique persuasion or behavior advantage.
  - **thesis:** Deepfakes are uniquely persuasive because they look real.
- **item 3:**
  - **antithesis:** Randomized interactive-AI studies produce measurable political preference and reported vote-choice shifts.
  - **support:**
    - FCT-007
    - FCT-022
    - FCT-023
    - FCT-024
  - **synthesis:** Current field effect is unproven while persuasion capacity under controlled exposure is real and materially relevant.
  - **thesis:** Low 2024 field impact means AI persuasion is negligible.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **flow:** operator -> model/tool -> generated/reformulated multilingual content
  - **resource:** model inference / automation capacity
  - **support:**
    - FCT-002
    - FCT-005
    - FCT-013
    - FCT-015
- **item 2:**
  - **flow:** generated content -> social/media channels -> potential audience exposure
  - **resource:** distribution infrastructure
  - **support:**
    - FCT-012
    - FCT-014
    - FCT-016
- **item 3:**
  - **flow:** interactive AI exposure -> participant conversation -> attitude/preference response
  - **resource:** attention/persuasion opportunity
  - **support:**
    - FCT-022
    - FCT-023
    - FCT-024

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** attributed influence operators
  - **relation:** use AI for generation/reformulation/translation and workflow support
  - **support:**
    - FCT-003
    - FCT-005
    - FCT-013
    - FCT-015
    - FCT-016
  - **to:** synthetic or AI-assisted content
- **item 2:**
  - **from:** platform/distribution accounts
  - **relation:** mediate reach independently of content-generation capacity
  - **support:**
    - FCT-012
    - FCT-014
    - FCT-019
  - **to:** authentic audiences
- **item 3:**
  - **from:** interactive AI systems
  - **relation:** deliver tailored political dialogue under experimental treatment
  - **support:**
    - FCT-022
    - FCT-023
  - **to:** participants/voters
- **item 4:**
  - **from:** platforms/regulators/researchers
  - **relation:** detect, disrupt, label or measure synthetic content
  - **support:**
    - FCT-018
    - FCT-020
    - FCT-027
    - FCT-028
  - **to:** deployment/exposure evidence

### IMPACT_MAP
- **AI_content_to_measured_exposure:** PARTIAL_CONTEXT_SPECIFIC
- **AI_to_distribution_breakthrough:** NOT_ESTABLISHED_GENERAL
- **AI_to_operational_productivity:** VERIFIED
- **France_EU_AI_to_election_result:** NOT_IDENTIFIED
- **deepfake_to_unique_credibility_advantage:** NOT_SUPPORTED
- **interactive_AI_to_political_persuasion:** SUPPORTED_EXPERIMENTAL
- **support:**
  - FCT-002
  - FCT-007
  - FCT-012
  - FCT-022
  - FCT-024
  - FCT-026
  - FCT-027

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** platform/election monitors often found limited authentic reach or election impact
  - **issue:** operational growth versus effect
  - **pro:** AI-related incidents and operational use rose sharply
  - **resolution:** deployment/scale is supported; effect remains a separate edge
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-007
    - FCT-012
    - FCT-014
- **item 2:**
  - **contra:** measured viral/harmful shares in several samples were low
  - **issue:** widespread incidents versus prevalence
  - **pro:** GenAI incidents appeared across many 2024 election countries
  - **resolution:** incident prevalence requires platform/population denominators
  - **support:**
    - FCT-010
    - FCT-018
    - FCT-027
    - FCT-028
- **item 3:**
  - **contra:** deepfakes are not more credible than other misinformation formats
  - **issue:** deepfake realism versus persuasion uniqueness
  - **pro:** human discernment is imperfect
  - **resolution:** detection difficulty does not establish unique persuasion
  - **support:**
    - FCT-025
    - FCT-026
- **item 4:**
  - **contra:** randomized AI dialogue and message studies shift preferences/attitudes
  - **issue:** field null/limited effects versus experimental persuasion
  - **pro:** 2024 field evidence found no meaningful election-result effect
  - **resolution:** persuasion capacity is causal under exposure; field-scale external validity remains unresolved
  - **support:**
    - FCT-007
    - FCT-022
    - FCT-023
    - FCT-024

### VERIFICATION_REPORT
- **circular_families:**
  - official EU/France family A
  - platform/threat-intelligence family B
  - election-monitoring family C
  - peer-reviewed experimental family D
  - observational dataset family E
- **contradiction_ids:**
  - deployment-vs-effect
  - incident-vs-prevalence
  - deepfake-detection-vs-persuasion
  - experimental-vs-field-effect
- **downgraded_ids:**
  - NONE
- **none_found_claims:**
  - France/EU causal election-result effect of GenAI
  - general AI-driven audience breakout
  - unique deepfake persuasion advantage
- **remaining_gaps:**
  - cross-platform exposure denominator
  - France/EU field exposure-to-vote design
  - real-world external validity of interactive AI persuasion
- **verification:** Every material web fact is linked to a fresh FETCH and current SRC/FCT; prior corpus used only as lead.

### EDI_REPORT
- **corpus:**
  - **circularity:** controlled by family accounting
  - **coverage:** STRONG_OPERATIONAL_DEPLOYMENT;STRONG_PRODUCTIVITY_DELTA;MIXED_PREVALENCE;STRONG_EXPERIMENTAL_PERSUASION;WEAK_FIELD_ELECTORAL_EFFECT
  - **independence:** 5_UPSTREAM_FAMILIES
  - **limits:**
    - platform visibility is incomplete
    - country/platform denominators differ
    - experimental persuasion is not field election effect
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES_OPERATIONAL
    - **gap_type:** NONE
    - **independent_families:** 3
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES_DISTRIBUTION_CONTROL
    - **gap_type:** NONE
    - **independent_families:** 3
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** MIXED_DENOMINATORS
    - **gap_type:** MEASUREMENT
    - **independent_families:** 3
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** RANDOMIZED_EXPERIMENTS
    - **gap_type:** NONE
    - **independent_families:** 2
  - **item 5:**
    - **claim_id:** CLM-005
    - **direct_object:** FIELD_BOUNDARY
    - **gap_type:** CAUSALITY
    - **independent_families:** 3
  - **item 6:**
    - **claim_id:** CLM-006
    - **direct_object:** MODEL_SYNTHESIS
    - **gap_type:** CAUSALITY
    - **independent_families:** 4
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** EU_FR_OFFICIAL+PLATFORMS+ELECTION_MONITORS+ACADEMIC
  - **perspective:** OPERATIONS+PREVALENCE+PERSUASION+FIELD_EFFECT
  - **stratification:** CAPABILITY+DEPLOYMENT+CONTENT+DISTRIBUTION+EXPOSURE+PERSUASION+BEHAVIOR+OUTCOME
  - **temporal:** 2022-2026
- **edi:**
  - **assessment:** MULTI_FAMILY_OPERATIONAL_PREVALENCE_EXPERIMENTAL_FIELD_CONTROL
  - **flags:**
    - EXPOSURE_DENOMINATOR_GAP
    - PLATFORM_OBSERVABILITY_BOUNDARY
    - EXPERIMENTAL_EXTERNAL_VALIDITY_GAP
    - FIELD_ELECTORAL_EFFECT_GAP
- **source_counts:**
  - **primary:** 9
  - **provenance_families:** 5
  - **secondary:** 7
  - **tertiary:** 0
  - **total:** 16

### RESPONSIBILITY_MAP
- **boundary:** Responsibility for producing or deploying synthetic content is distinct from causal responsibility for downstream electoral outcomes.
- **not_established:**
  - general AI control over political audiences
  - France/EU election outcome caused by GenAI
  - unique deepfake persuasion capability
- **verified:**
  - operators choose to deploy AI in attributed influence workflows
  - platform/distribution systems mediate audience acquisition
  - interactive systems can produce persuasive treatment effects under experimental exposure

### NEXT_QUERIES
- France/EU linked panel of identified AI-content exposure and validated political behavior
- cross-platform authentic-reach denominator for election synthetic content
- field experiment comparing interactive AI persuasion with static misinformation and human canvassing
- operator cost/time/volume measurements before versus after GenAI adoption
- post-election audits tying attributed AI operations to turnout or vote-choice data

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-002,QRY-005,QRY-006,QRY-007,QRY-008,QRY-012,QRY-013,QRY-016,QRY-017,QRY-018,QRY-019,QRY-021 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-005,FCT-010,FCT-012,FCT-013,FCT-015,FCT-016,FCT-017,FCT-019,FCT-020,FCT-021 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-003,QRY-004,QRY-005,QRY-007,QRY-011,QRY-014,QRY-015,QRY-016,QRY-020,QRY-023,QRY-026,QRY-027 | support:- | counter:- | results:FCT-004,FCT-006,FCT-007,FCT-010,FCT-011,FCT-012,FCT-014,FCT-016,FCT-018,FCT-019,FCT-027,FCT-028 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-009,QRY-010,QRY-011,QRY-022,QRY-023,QRY-024,QRY-025 | support:- | counter:- | results:FCT-022,FCT-023,FCT-024,FCT-025,FCT-026 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-003,QRY-004,QRY-005,QRY-007,QRY-009,QRY-011,QRY-014,QRY-015,QRY-020,QRY-022,QRY-026,QRY-027 | support:- | counter:- | results:FCT-004,FCT-007,FCT-008,FCT-009,FCT-011,FCT-012,FCT-014,FCT-016,FCT-018,FCT-020,FCT-021,FCT-023,FCT-027,FCT-028 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-012,QRY-013,QRY-016,QRY-017,QRY-018,QRY-019,QRY-020,SRC-001,SRC-002,SRC-005,SRC-006,SRC-007,SRC-008,SRC-009 | support:FCT-001,FCT-002,FCT-005,FCT-013,FCT-015,FCT-017,FCT-019 | counter:FCT-012,FCT-014,FCT-016 | results:FCT-001,FCT-002,FCT-005,FCT-013,FCT-015,FCT-017,FCT-019,FCT-012,FCT-014,FCT-016 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-014,QRY-015,QRY-016,QRY-018,QRY-020,QRY-026,QRY-027,SRC-003,SRC-004,SRC-005,SRC-007,SRC-009,SRC-015,SRC-016 | support:FCT-007,FCT-008,FCT-012,FCT-014,FCT-016,FCT-018,FCT-027,FCT-028 | counter:FCT-010 | results:FCT-007,FCT-008,FCT-012,FCT-014,FCT-016,FCT-018,FCT-027,FCT-028,FCT-010 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-012,QRY-014,QRY-015,QRY-020,QRY-026,QRY-027,SRC-001,SRC-003,SRC-004,SRC-009,SRC-015,SRC-016 | support:FCT-006,FCT-010,FCT-011,FCT-018,FCT-027,FCT-028 | counter:FCT-001 | results:FCT-006,FCT-010,FCT-011,FCT-018,FCT-027,FCT-028,FCT-001 | final:PARTIAL | gap:MEASUREMENT
CLM-004 | attempts:QRY-014,QRY-022,QRY-023,QRY-024,QRY-025,SRC-003,SRC-011,SRC-012,SRC-013,SRC-014 | support:FCT-022,FCT-023,FCT-024,FCT-025,FCT-026 | counter:FCT-007 | results:FCT-022,FCT-023,FCT-024,FCT-025,FCT-026,FCT-007 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-013,QRY-014,QRY-020,QRY-022,QRY-026,QRY-027,SRC-002,SRC-003,SRC-009,SRC-011,SRC-015,SRC-016 | support:FCT-004,FCT-006,FCT-007,FCT-008,FCT-018,FCT-027,FCT-028 | counter:FCT-022,FCT-023 | results:FCT-004,FCT-006,FCT-007,FCT-008,FCT-018,FCT-027,FCT-028,FCT-022,FCT-023 | final:PARTIAL | gap:CAUSALITY
CLM-006 | attempts:QRY-012,QRY-014,QRY-017,QRY-019,QRY-020,QRY-022,QRY-023,QRY-026,QRY-027,SRC-001,SRC-003,SRC-006,SRC-008,SRC-009,SRC-011,SRC-012,SRC-015,SRC-016 | support:FCT-002,FCT-008,FCT-015,FCT-017,FCT-022,FCT-023,FCT-024 | counter:FCT-007,FCT-018,FCT-027,FCT-028 | results:FCT-002,FCT-008,FCT-015,FCT-017,FCT-022,FCT-023,FCT-024,FCT-007,FCT-018,FCT-027,FCT-028 | final:PARTIAL | gap:CAUSALITY

## STATUS_DELTA_V1
DELTA-001 | AXS-001 | OPEN | SATURATED | FACTS checkpoint evidence collected
DELTA-002 | AXS-002 | OPEN | SATURATED | FACTS checkpoint evidence collected
DELTA-003 | AXS-003 | OPEN | SATURATED | FACTS checkpoint evidence collected
DELTA-004 | AXS-004 | OPEN | SATURATED | FACTS checkpoint evidence collected

## OPEN_GAPS_V1
CLM-003 | CLM | PARTIAL | MEASUREMENT | Cross-platform population exposure and comparable denominator data are missing for France/EU; reporting intensity and detection differ by platform and election.
CLM-005 | CLM | PARTIAL | CAUSALITY | No France/EU field design in the inspected corpus links identified AI-mediated exposure to individual behavior and aggregate electoral outcomes with a credible counterfactual.
CLM-006 | CLM | PARTIAL | CAUSALITY | External validity, real-world repeated exposure, targeting quality, platform distribution and conversion from expressed preference to actual vote remain unresolved.
CAU-002 | CAU | UNRESOLVED | MEASUREMENT | Cross-platform authentic reach and user-level exposure are not consistently observed; distribution remains an independent bottleneck.
CAU-004 | CAU | UNRESOLVED | CAUSALITY | No inspected France/EU design observes identified AI exposure and actual voting outcomes with a credible counterfactual.

SEMANTIC_COUNTS_V1:LED:0|CLM:6|AXS:4|CAU:5|CTRL:10|ACT:4

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Generative AI is now operationally deployed in attributed influence workflows and materially increases production speed, volume, multilingual adaptation and workflow efficiency, but the inspected evidence does not show a commensurate breakthrough in audience acquisition or novel offensive capability.","claimant":"INV-092 synthesis","counter":["FCT-012","FCT-014","FCT-016"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-005","FCT-013","FCT-015","FCT-017","FCT-019"]}
CLM-002 | {"claim":"Distribution and authentic audience acquisition remain separate bottlenecks: several platform and election-monitoring datasets show that higher AI-assisted production does not automatically translate into virality, authentic reach or breakout.","claimant":"INV-092 synthesis","counter":["FCT-010"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-007","FCT-008","FCT-012","FCT-014","FCT-016","FCT-018","FCT-027","FCT-028"]}
CLM-003 | {"claim":"GenAI election incidents are geographically widespread, but incident counts and detected synthetic content do not provide a population denominator for prevalence or democratic impact; measured viral/harmful shares in several observed election contexts were much smaller than headline incident counts imply.","claimant":"INV-092 synthesis","counter":["FCT-001"],"gap":"Cross-platform population exposure and comparable denominator data are missing for France/EU; reporting intensity and detection differ by platform and election.","gap_type":"MEASUREMENT","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-006","FCT-010","FCT-011","FCT-018","FCT-027","FCT-028"]}
CLM-004 | {"claim":"Controlled experiments establish that interactive AI dialogue and LLM-generated political messages can causally shift candidate preferences, reported vote choice or policy attitudes under exposure, while political deepfakes are not uniquely credible or persuasive relative to other misinformation formats.","claimant":"INV-092 synthesis","counter":["FCT-007"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-022","FCT-023","FCT-024","FCT-025","FCT-026"]}
CLM-005 | {"claim":"The inspected field evidence does not identify a causal effect of generative AI, deepfakes or automation on actual France/EU election results in 2024–2026; detection, exposure and experimental persuasion cannot by themselves establish changed turnout, vote totals or winners.","claimant":"INV-092 synthesis","counter":["FCT-022","FCT-023"],"gap":"No France/EU field design in the inspected corpus links identified AI-mediated exposure to individual behavior and aggregate electoral outcomes with a credible counterfactual.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-004","FCT-006","FCT-007","FCT-008","FCT-018","FCT-027","FCT-028"]}
CLM-006 | {"claim":"The strongest current model is a scale/productivity delta rather than a proven qualitatively new electoral-effect regime; however, interactive personalized persuasion remains a material forward risk because experiments close a persuasion edge that field election studies have not yet measured at scale.","claimant":"INV-092 synthesis","counter":["FCT-007","FCT-018","FCT-027","FCT-028"],"gap":"External validity, real-world repeated exposure, targeting quality, platform distribution and conversion from expressed preference to actual vote remain unresolved.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-002","FCT-008","FCT-015","FCT-017","FCT-022","FCT-023","FCT-024"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-005","QRY-006","QRY-007","QRY-008","QRY-012","QRY-013","QRY-016","QRY-017","QRY-018","QRY-019","QRY-021"],"axis":"operational deployment and scale","links":["OBJECT_QUESTION"],"question":"Where is generative AI actually used by influence operators, and what changes in cost, speed, volume, multilingual reach or workflow are documented?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-005","FCT-010","FCT-012","FCT-013","FCT-015","FCT-016","FCT-017","FCT-019","FCT-020","FCT-021"],"sought_objects":["deployment","workflow","cost","speed","volume","translation","synthetic media"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-003","QRY-004","QRY-005","QRY-007","QRY-011","QRY-014","QRY-015","QRY-016","QRY-020","QRY-023","QRY-026","QRY-027"],"axis":"prevalence and exposure","links":["OBJECT_QUESTION"],"question":"How prevalent is AI-enabled political content in real election environments, how much authentic reach does it obtain, and through which distribution channels?","result_ids":["FCT-004","FCT-006","FCT-007","FCT-010","FCT-011","FCT-012","FCT-014","FCT-016","FCT-018","FCT-019","FCT-027","FCT-028"],"sought_objects":["incident prevalence","viral cases","audience reach","engagement","distribution"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-009","QRY-010","QRY-011","QRY-022","QRY-023","QRY-024","QRY-025"],"axis":"persuasion and behavior","links":["OBJECT_QUESTION"],"question":"What experimental or observational evidence shows that AI-generated political content or dialogue changes beliefs, candidate preference, voting intention or behavior?","result_ids":["FCT-022","FCT-023","FCT-024","FCT-025","FCT-026"],"sought_objects":["persuasion experiments","deepfake credibility","discernment","vote choice"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-003","QRY-004","QRY-005","QRY-007","QRY-009","QRY-011","QRY-014","QRY-015","QRY-020","QRY-022","QRY-026","QRY-027"],"axis":"electoral effect and controls","links":["OBJECT_QUESTION"],"question":"What evidence distinguishes technical capability and exposure from meaningful democratic or electoral effects, and what negative controls bound the threat?","result_ids":["FCT-004","FCT-007","FCT-008","FCT-009","FCT-011","FCT-012","FCT-014","FCT-016","FCT-018","FCT-020","FCT-021","FCT-023","FCT-027","FCT-028"],"sought_objects":["field election outcomes","counterfactuals","traditional tactics","defensive friction","negative controls"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"Repeated attributed operational observations across official/platform families directly document AI use for content and workflow acceleration.","counter":["FCT-012"],"limit":"Productivity gain does not itself establish distribution, audience acquisition or persuasion.","mechanism":"model/tool access -> automated generation/translation/reformulation -> lower linguistic friction and higher content volume/speed","status":"SUPPORTED","support":["FCT-002","FCT-005","FCT-013","FCT-015","FCT-017"]}
CAU-002 | {"counter":["FCT-010"],"gap":"Cross-platform authentic reach and user-level exposure are not consistently observed; distribution remains an independent bottleneck.","gap_type":"MEASUREMENT","limit":"Incident detection and synthetic-content presence do not identify a common exposure denominator or virality mechanism.","mechanism":"AI-assisted content production -> distribution through existing channels -> authentic audience exposure","status":"UNRESOLVED","support":["FCT-008","FCT-012","FCT-014","FCT-016","FCT-018","FCT-027","FCT-028"]}
CAU-003 | {"causal_right":"Preregistered randomized experiments isolate the treatment effect of AI dialogue/messages on reported political attitudes and choices.","counter":["FCT-007"],"limit":"Experimental treatment effects establish persuasion under controlled exposure, not population-scale field election effects.","mechanism":"interactive LLM political conversation or generated persuasive message -> exposed participant -> changed candidate preference/reported vote choice/policy attitude","status":"SUPPORTED","support":["FCT-022","FCT-023","FCT-024"]}
CAU-004 | {"counter":["FCT-022","FCT-023"],"gap":"No inspected France/EU design observes identified AI exposure and actual voting outcomes with a credible counterfactual.","gap_type":"CAUSALITY","limit":"Experimental susceptibility and incident visibility are upstream of actual field behavior and election outcomes.","mechanism":"AI/deepfake/automation deployment in France/EU election environment -> population exposure -> changed turnout/vote/election result","status":"UNRESOLVED","support":["FCT-004","FCT-006","FCT-007","FCT-018"]}
CAU-005 | {"causal_right":"Experiments show harder discernment for some synthetic formats while separate experiments show deepfakes are not uniquely credible versus text/audio misinformation.","counter":["FCT-026"],"limit":"Imperfect detection does not imply unique credibility, persuasion, virality or behavioral effect.","mechanism":"higher synthetic-media realism -> reduced human discernment -> potential deception advantage","status":"SUPPORTED","support":["FCT-025","FCT-026"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"capability != deployment","status":"DONE","support":["FCT-020","FCT-005"]}
CTRL-002 | {"control":"synthetic != deceptive","status":"DONE","support":["FCT-025","FCT-026"]}
CTRL-003 | {"control":"detection != exposure","status":"DONE","support":["FCT-001","FCT-010"]}
CTRL-004 | {"control":"reach != persuasion","status":"DONE","support":["FCT-012","FCT-014"]}
CTRL-005 | {"control":"virality != behavior","status":"DONE","support":["FCT-006","FCT-007"]}
CTRL-006 | {"control":"automation != coordination","status":"DONE","support":["FCT-013","FCT-019"]}
CTRL-007 | {"control":"attribution != effect","status":"DONE","support":["FCT-003","FCT-004"]}
CTRL-008 | {"control":"incident != prevalence","status":"DONE","support":["FCT-010","FCT-027","FCT-028"]}
CTRL-009 | {"control":"foreign comparator != France/EU effect","status":"DONE","support":["FCT-022","FCT-023"]}
CTRL-010 | {"control":"platform/threat report != population denominator","status":"DONE","support":["FCT-012","FCT-018"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"publish interoperable cross-platform exposure denominators for election-related synthetic/manipulated content, with bot/authentic-audience separation","actor":"platforms / regulators / researchers","intent":"separate detected incidents and production volume from actual audience exposure","status":"OPEN","support":["FCT-010","FCT-014","FCT-018","FCT-027"]}
ACT-002 | {"action":"link identified AI-mediated exposure to panel behavior or validated vote outcomes using preregistered field or quasi-experimental designs","actor":"researchers / election-integrity bodies","intent":"test exposure -> persuasion -> behavior -> democratic effect rather than infer it","status":"OPEN","support":["FCT-007","FCT-022","FCT-023"]}
ACT-003 | {"action":"track operator productivity, cost, multilingual throughput and distribution performance separately","actor":"threat intelligence / platforms","intent":"measure the scale delta without conflating production capability with audience impact","status":"OPEN","support":["FCT-002","FCT-013","FCT-015","FCT-017"]}
ACT-004 | {"action":"reopen only on France/EU field evidence linking authenticated AI-enabled operation, measured exposure and behavioral/electoral outcome, or on robust evidence of a new capability beyond workflow acceleration","actor":"future investigation","intent":"upgrade the unresolved field-effect edge without cumulative incident collection","status":"OPEN","support":["FCT-004","FCT-007","FCT-015","FCT-022"]}

SEARCH_ACTIVITY_V1:WEB:11|FETCH:16|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FAIL | MNEMO | MNEMO_UNAVAILABLE | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | PASS | - | - | EEAS 2026 FIMI AI enhanced activities generative AI 147 incidents 27 percent
QRY-002 | WEB | PASS | - | - | VIGINUM Storm-1516 AI CopyCop 77 operations elections France 2025
QRY-003 | WEB | PASS | - | - | CETaS AI-enabled influence 2024 French EU elections deepfakes impact
QRY-004 | WEB | PASS | - | - | IPIE generative AI 2024 elections worldwide 215 incidents
QRY-005 | WEB | PASS | - | - | OpenAI covert influence operations AI engagement productivity 2024 2025 2026
QRY-006 | WEB | PASS | - | - | Google threat intelligence generative AI influence operations productivity breakthrough capabilities
QRY-007 | WEB | PASS | - | - | Meta 2024 global elections generative AI misinformation prevalence
QRY-008 | WEB | PASS | - | - | Microsoft 2024 election influence AI deepfakes shallow fakes
QRY-009 | WEB | PASS | - | - | political AI dialogue voter persuasion experiment 2025 Nature
QRY-010 | WEB | PASS | - | - | LLM generated political messages persuasion policy experiment Nature Communications 2025
QRY-011 | WEB | PASS | - | - | political deepfake prevalence credibility detection elections 2024 2025 studies
QRY-012 | FETCH | PASS | SRC-001 | https://www.eeas.europa.eu/sites/default/files/2026/documents/EEAS%204th%20Threat%20Report_web.pdf | -
QRY-013 | FETCH | PASS | SRC-002 | https://www.sgdsn.gouv.fr/publications/analyse-du-mode-operatoire-informationnel-russe-storm-1516 | -
QRY-014 | FETCH | PASS | SRC-003 | https://cetas.turing.ac.uk/publications/ai-enabled-influence-operations-threat-analysis-2024-uk-and-european-elections | -
QRY-015 | FETCH | PASS | SRC-004 | https://www.ipie.info/research/tp2025-2 | -
QRY-016 | FETCH | PASS | SRC-005 | https://openai.com/index/disrupting-deceptive-uses-of-ai-by-covert-influence-operations/ | -
QRY-017 | FETCH | PASS | SRC-006 | https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-october-2025/ | -
QRY-018 | FETCH | PASS | SRC-007 | https://openai.com/index/disrupting-malicious-uses-of-ai-influence-campaign-russia/ | -
QRY-019 | FETCH | PASS | SRC-008 | https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai | -
QRY-020 | FETCH | PASS | SRC-009 | https://about.fb.com/news/2024/12/2024-global-elections-meta-platforms/ | -
QRY-021 | FETCH | PASS | SRC-010 | https://blogs.microsoft.com/on-the-issues/2024/04/17/russia-us-election-interference-deepfakes-ai/ | -
QRY-022 | FETCH | PASS | SRC-011 | https://www.nature.com/articles/s41586-025-09771-9 | -
QRY-023 | FETCH | PASS | SRC-012 | https://www.nature.com/articles/s41467-025-61345-5 | -
QRY-024 | FETCH | PASS | SRC-013 | https://www.nature.com/articles/s41467-024-51998-z | -
QRY-025 | FETCH | PASS | SRC-014 | https://doi.org/10.1086/732990 | -
QRY-026 | FETCH | PASS | SRC-015 | https://arxiv.org/abs/2512.13915 | -
QRY-027 | FETCH | PASS | SRC-016 | https://www.nature.com/articles/d41586-024-01588-2 | -

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | EEAS-FIMI-2026 | EEAS 4th Report on FIMI Threats | 2026-03-01 | 2026-09-09 | AI-enhanced FIMI: 2025 incident count, scaling, multilingual production | https://www.eeas.europa.eu/sites/default/files/2026/documents/EEAS%204th%20Threat%20Report_web.pdf
SRC-002 | ◈ | fam:A | VIGINUM-STORM1516-2025 | VIGINUM - Analyse du mode opératoire informationnel russe Storm-1516 | 2025-05-06 | 2026-09-09 | 77 operations, election targeting, CopyCop/AI workflow, impact caveat | https://www.sgdsn.gouv.fr/publications/analyse-du-mode-operatoire-informationnel-russe-storm-1516
SRC-003 | ◉ | fam:C | CETAS-AI-ELECTIONS-2024 | CETaS - AI-Enabled Influence Operations: 2024 UK and European Elections | 2024-09-19 | 2026-09-09 | viral case counts, exposure and election-impact assessment | https://cetas.turing.ac.uk/publications/ai-enabled-influence-operations-threat-analysis-2024-uk-and-european-elections
SRC-004 | ◉ | fam:C | IPIE-TP2025-2 | IPIE - The Role of Generative AI Use in 2024 Elections Worldwide | 2025-05-27 | 2026-09-09 | 215 incidents across 50 competitive elections; source and use categories | https://www.ipie.info/research/tp2025-2
SRC-005 | ◈ | fam:B | OPENAI-IO-2024-05 | OpenAI - Disrupting deceptive uses of AI by covert influence operations | 2024-05-30 | 2026-09-09 | five covert IOs; volume/productivity and audience-engagement assessment | https://openai.com/index/disrupting-deceptive-uses-of-ai-by-covert-influence-operations/
SRC-006 | ◈ | fam:B | OPENAI-THREAT-2025-10 | OpenAI - Disrupting malicious uses of AI: October 2025 | 2025-10-07 | 2026-09-09 | 40+ disrupted networks; old playbooks faster rather than novel capability | https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-october-2025/
SRC-007 | ◈ | fam:B | OPENAI-RUSSIA-IBI-2026 | OpenAI - Disrupting a new covert influence campaign from Russia | 2026-08-25 | 2026-09-09 | AI-generated social posts and small-audience influence operation | https://openai.com/index/disrupting-malicious-uses-of-ai-influence-campaign-russia/
SRC-008 | ◈ | fam:B | GOOGLE-GTIG-AI-2026 | Google Threat Intelligence - From Prompting to Autonomy | 2026-09-08 | 2026-09-09 | IO productivity gains, synthetic media, no breakthrough capabilities | https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai
SRC-009 | ◈ | fam:B | META-ELECTIONS-2024 | Meta - What We Saw on Our Platforms During 2024’s Global Elections | 2024-12-03 | 2026-09-09 | AI misinformation volume and CIB productivity observations | https://about.fb.com/news/2024/12/2024-global-elections-meta-platforms/
SRC-010 | ◈ | fam:B | MSFT-MTAC-2024-04 | Microsoft MTAC - Russian US election interference and AI/deepfakes | 2024-04-17 | 2026-09-09 | nation-state genAI usage and shallow-vs-deepfake threat assessment | https://blogs.microsoft.com/on-the-issues/2024/04/17/russia-us-election-interference-deepfakes-ai/
SRC-011 | ◉ | fam:D | NATURE-AI-VOTERS-2025 | Persuading voters using human–artificial intelligence dialogues | 2025-12-04 | 2026-09-09 | preregistered candidate-preference and voting-intention experiments | https://www.nature.com/articles/s41586-025-09771-9
SRC-012 | ◉ | fam:D | NATCOMM-LLM-PERSUASION-2025 | LLM-generated messages can persuade humans on policy issues | 2025-07-01 | 2026-09-09 | three preregistered experiments; policy-attitude effect sizes | https://www.nature.com/articles/s41467-025-61345-5
SRC-013 | ◉ | fam:D | NATCOMM-DEEPFAKE-DETECTION-2024 | Human detection of political speech deepfakes across transcripts, audio, and video | 2024-09-01 | 2026-09-09 | five preregistered experiments, N=2215, discernment by modality | https://www.nature.com/articles/s41467-024-51998-z
SRC-014 | ◉ | fam:D | JOP-DEEPFAKE-CREDIBILITY-2025 | Political Deepfakes Are as Credible as Other Fake Media and (Sometimes) Real Media | 2025-03-13 | 2026-09-09 | experimental comparison of deepfake credibility with text/audio misinformation | https://doi.org/10.1086/732990
SRC-015 | ◉ | fam:E | ARXIV-CANADA-DEEPFAKES-2025 | Deepfakes in the 2025 Canadian Election: Prevalence, Partisanship, and Platform Dynamics | 2025-12-15 | 2026-09-09 | 187,778 posts; prevalence and view-share estimates | https://arxiv.org/abs/2512.13915
SRC-016 | ◉ | fam:E | NATURE-INDIA-AI-2024 | How prevalent is AI misinformation? What our studies in India show so far | 2024-06-05 | 2026-09-09 | roughly two million WhatsApp messages; viral GenAI prevalence estimate | https://www.nature.com/articles/d41586-024-01588-2

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.eeas.europa.eu/sites/default/files/2026/documents/EEAS%204th%20Threat%20Report_web.pdf | A | 2026-09-09 | AI-related FIMI incidence in 2025 | The EEAS 4th threat report says 27% of incidents detected in 2025 involved AI-related TTPs, rising from 41 cases in 2024 to 147 in 2025, about a 259% increase. | -
FCT-002 | FACT | ✧ | https://www.eeas.europa.eu/sites/default/files/2026/documents/EEAS%204th%20Threat%20Report_web.pdf | A | 2026-09-09 | AI changes production scale more clearly than precision | The EEAS reports Russian and Chinese FIMI actors embedding AI to accelerate content production, scale activity with fewer resources and sustain a constant stream of multilingual content; the described objective is often presence rather than precision. | -
FCT-003 | FACT | ✧ | https://www.sgdsn.gouv.fr/publications/analyse-du-mode-operatoire-informationnel-russe-storm-1516 | A | 2026-09-09 | Storm-1516 operational denominator | VIGINUM analysed 77 Storm-1516 information operations conducted from the mode’s emergence through 5 March 2025, including campaigns targeting Western and French audiences. | -
FCT-004 | FACT | ✧ | https://www.sgdsn.gouv.fr/publications/analyse-du-mode-operatoire-informationnel-russe-storm-1516 | A | 2026-09-09 | Storm-1516 electoral targeting and impact ceiling | VIGINUM documents Storm-1516 targeting election processes and reports that some narratives reached high online visibility, while explicitly stating that the real impact on digital public debate remains difficult to estimate. | -
FCT-005 | FACT | ✧ | https://www.sgdsn.gouv.fr/publications/analyse-du-mode-operatoire-informationnel-russe-storm-1516 | A | 2026-09-09 | CopyCop AI integration | VIGINUM documents CopyCop as part of the Storm-1516 ecosystem and reports use of AI tools to generate or reformulate articles, supporting operational deployment of AI in the content-production workflow. | -
FCT-006 | FACT | ✧ | https://cetas.turing.ac.uk/publications/ai-enabled-influence-operations-threat-analysis-2024-uk-and-european-elections | C | 2026-09-09 | Low viral case count in 2024 EU and French elections | CETaS identified 11 confirmed viral cases of AI-enabled disinformation or deepfakes across the EU and French elections it studied, far below pre-election fears. | -
FCT-007 | FACT | ✧ | https://cetas.turing.ac.uk/publications/ai-enabled-influence-operations-threat-analysis-2024-uk-and-european-elections | C | 2026-09-09 | No demonstrated 2024 UK/EU/French election-result effect | CETaS found no evidence that AI-enabled disinformation or deepfakes meaningfully affected UK or European election results; observed exposure was concentrated among users already aligned with the narratives. | -
FCT-008 | FACT | ✧ | https://cetas.turing.ac.uk/publications/ai-enabled-influence-operations-threat-analysis-2024-uk-and-european-elections | C | 2026-09-09 | Traditional distribution tactics remained more influential | CETaS found generative AI played less of a role in boosting virality than traditional interference tactics and human influencers; where used, it mainly rewrote news or scaled online activity. | -
FCT-009 | FACT | ✧ | https://cetas.turing.ac.uk/publications/ai-enabled-influence-operations-threat-analysis-2024-uk-and-european-elections | C | 2026-09-09 | Non-electoral harms can occur without vote switching | CETaS documented confusion about authenticity, harassment and hate around deepfakes, showing democratic-system or personal harms can occur even when election-result effects are not identified. | -
FCT-010 | FACT | ✧ | https://www.ipie.info/research/tp2025-2 | C | 2026-09-09 | Global 2024 election incident prevalence | IPIE’s database contains 215 reported GenAI election incidents across all 50 countries holding competitive national elections in 2024; 80% of those countries had at least one incident and 90% of incidents involved content creation. | -
FCT-011 | FACT | ✧ | https://www.ipie.info/research/tp2025-2 | C | 2026-09-09 | Incident source categories do not equal effect | IPIE reports 20% of the 215 incidents were attributed to foreign actors and 69% were described as harmful; these are incident classifications rather than estimates of changed votes or election outcomes. | -
FCT-012 | FACT | ✧ | https://openai.com/index/disrupting-deceptive-uses-of-ai-by-covert-influence-operations/ | B | 2026-09-09 | Five covert IOs showed no AI-driven audience breakout | OpenAI reported disrupting five covert influence operations in early 2024 and found no meaningful increase in audience engagement or reach attributable to its services; none scored above 2 on the cited Breakout Scale. | -
FCT-013 | FACT | ✧ | https://openai.com/index/disrupting-deceptive-uses-of-ai-by-covert-influence-operations/ | B | 2026-09-09 | Volume and language quality productivity gain | OpenAI observed threat actors using AI to generate greater volumes of text with fewer language errors, translate/edit content, debug code and fabricate engagement, while distinguishing inauthentic self-replies from authentic audience engagement. | -
FCT-014 | FACT | ✧ | https://openai.com/index/disrupting-deceptive-uses-of-ai-by-covert-influence-operations/ | B | 2026-09-09 | Distribution remains a separate bottleneck | OpenAI states that AI-generated material still requires distribution to reach an audience and that the 2024 covert networks it studied did not engage a substantial authentic audience. | -
FCT-015 | FACT | ✧ | https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-october-2025/ | B | 2026-09-09 | Old playbooks accelerated rather than replaced | In October 2025 OpenAI reported more than 40 disrupted abusive networks since February 2024 and said threat actors were bolting AI onto old playbooks to move faster rather than obtaining novel offensive capability from the models. | -
FCT-016 | FACT | ✧ | https://openai.com/index/disrupting-malicious-uses-of-ai-influence-campaign-russia/ | B | 2026-09-09 | Elaborate 2026 Russian-linked operation still had small reach | OpenAI’s August 2026 report describes a likely Russia-origin cluster using ChatGPT to generate social-media comments and conceal linguistic clues, but says the campaign appeared to reach relatively small audiences. | -
FCT-017 | FACT | ✧ | https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai | B | 2026-09-09 | Google IO observation: productivity without breakthrough | Google Threat Intelligence reported continuing use of generative AI for productivity gains, operational workflow optimisation, content generation and synthetic media in influence operations, while observing no breakthrough IO capabilities from those tactics. | -
FCT-018 | FACT | ✧ | https://about.fb.com/news/2024/12/2024-global-elections-meta-platforms/ | B | 2026-09-09 | Meta observed low AI misinformation volume in 2024 elections | Meta reported that election-, politics- and social-topic AI content rated by fact-checkers represented less than 1% of all fact-checked misinformation during the major 2024 elections it monitored. | -
FCT-019 | FACT | ✧ | https://about.fb.com/news/2024/12/2024-global-elections-meta-platforms/ | B | 2026-09-09 | Meta observed incremental CIB gains | Meta reported that coordinated inauthentic networks achieved only incremental productivity and content-generation gains from generative AI during 2024, and said this did not prevent behavioral detection and disruption. | -
FCT-020 | FACT | ✧ | https://about.fb.com/news/2024/12/2024-global-elections-meta-platforms/ | B | 2026-09-09 | Defensive friction blocks capability from becoming deployment | Meta reported rejecting about 590,000 requests to generate images of leading US candidates and officeholders in the month before the 2024 US election, illustrating a gap between technical capability and allowed platform deployment. | -
FCT-021 | FACT | ✧ | https://blogs.microsoft.com/on-the-issues/2024/04/17/russia-us-election-interference-deepfakes-ai/ | B | 2026-09-09 | Nation-state adoption did not make sophisticated deepfakes dominant | Microsoft MTAC reported in April 2024 that Russia, Iran and China had each used some form of generative AI, while assessing that simple or shallow manipulations were more likely to have impact than the most sophisticated deepfakes. | -
FCT-022 | FACT | ✧ | https://www.nature.com/articles/s41586-025-09771-9 | D | 2026-09-09 | Interactive AI can causally shift candidate preference in experiments | A 2025 Nature study using preregistered experiments in the 2024 US, 2025 Canadian and 2025 Polish elections found significant AI-dialogue treatment effects on candidate preference, larger than typical effects from traditional video advertisements. | -
FCT-023 | FACT | ✧ | https://www.nature.com/articles/s41586-025-09771-9 | D | 2026-09-09 | AI dialogue changed reported vote choice and intention under experimental exposure | The Nature experiments report pro-candidate AI conversations increasing reported vote choice toward the advocated candidate and increasing voting intention for some participants; this establishes experimental persuasion, not field election outcomes. | -
FCT-024 | FACT | ✧ | https://www.nature.com/articles/s41467-025-61345-5 | D | 2026-09-09 | LLM persuasive messages produce small but measurable attitude shifts | Across three preregistered experiments with 4,829 participants, LLM-generated policy messages shifted support by roughly 2 to 4 points on 101-point scales and were similarly persuasive to messages written by lay humans. | -
FCT-025 | FACT | ✧ | https://www.nature.com/articles/s41467-024-51998-z | D | 2026-09-09 | Deepfake discernment is imperfect rather than impossible | Five preregistered experiments with 2,215 participants found people were better than random at distinguishing real from fabricated political speeches but far from perfect; synthetic text-to-speech audio made deepfakes harder to discern than voice-actor audio. | -
FCT-026 | FACT | ✧ | https://doi.org/10.1086/732990 | D | 2026-09-09 | Deepfakes are not uniquely credible versus other misinformation | A 2025 Journal of Politics experiment found political deepfakes were approximately as credible as misinformation conveyed through text or audio, and sometimes as credible as authentic video, undermining a simple deepfake-equals-uniquely-persuasive assumption. | -
FCT-027 | FACT | ✧ | https://arxiv.org/abs/2512.13915 | E | 2026-09-09 | Canadian 2025 harmful deepfake reach was small in measured X views | A study of 187,778 election-related posts in the 2025 Canadian election estimated 5.86% of election-related images as deepfakes, but harmful deepfakes accounted for only 0.12% of all measured views on X. | -
FCT-028 | FACT | ✧ | https://www.nature.com/articles/d41586-024-01588-2 | E | 2026-09-09 | India WhatsApp sample found low GenAI prevalence | In a study sampling roughly two million WhatsApp messages around India’s 2024 election, fewer than two dozen of 1,858 viral messages contained identified GenAI-created content, around 1%, with no detected election-period spike in the monitored sample. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-002
FCT-004 | SRC-002
FCT-005 | SRC-002
FCT-006 | SRC-003
FCT-007 | SRC-003
FCT-008 | SRC-003
FCT-009 | SRC-003
FCT-010 | SRC-004
FCT-011 | SRC-004
FCT-012 | SRC-005
FCT-013 | SRC-005
FCT-014 | SRC-005
FCT-015 | SRC-006
FCT-016 | SRC-007
FCT-017 | SRC-008
FCT-018 | SRC-009
FCT-019 | SRC-009
FCT-020 | SRC-009
FCT-021 | SRC-010
FCT-022 | SRC-011
FCT-023 | SRC-011
FCT-024 | SRC-012
FCT-025 | SRC-013
FCT-026 | SRC-014
FCT-027 | SRC-015
FCT-028 | SRC-016

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
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:narrative

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-09T11:49:17.017078+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":28,"eligible":28,"failure":0,"success":0}}

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
