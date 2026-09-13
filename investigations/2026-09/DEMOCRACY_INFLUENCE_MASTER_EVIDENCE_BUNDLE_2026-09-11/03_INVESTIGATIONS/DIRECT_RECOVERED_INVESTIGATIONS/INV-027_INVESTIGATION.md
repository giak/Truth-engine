ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260910-1003-elnet-france-lobbying | PARENT_RUN_ID:NONE | AS_OF:2026-09-10
INPUT_KIND:RUN_CARD | MISSION_MODE:RECHECK_EXTEND | INPUT_REF:PATH:/mnt/data/inv027/runtime/investigations/2026-09/2026-09-10_elnet-france-lobbying/2026-09-10_10-03_elnet-france-lobbying_INPUT.md | SUBJECT_SLUG:elnet-france-lobbying | SUBJECT_FP:sha256:733225a1d99793a08fe7282e6209ec26d4ec787ee6fdc425076482f5559cbb7e | INPUT_SHA256:sha256:8a9938efdda3c53acc3c8cc70ebbabcd64f1f6c109628c197156f49221e08d82
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France 2017-2026; ELNET France resources -> trips/events/meetings -> public official access/exposure -> identifiable position/action -> decision/effect; separate funding, access, influence, tasking and capture.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/NETWORK.md,clusters/INFORMATION.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Analytic body

## Object
INV-027 tests ELNET France resources -> lobbying/trips/events -> public-official exposure -> position/action -> decision/effect, preserving funding != tasking, voyage != capture and access != influence.

## Declared capacity
HATVP identifies ELNET France as a registered interest-representation association with named representatives [FCT-001,FCT-002]. The declared expenditure band is EUR100,000-200,000 for each year 2021-2025, with three persons dedicated to interest representation [FCT-003,FCT-004]. HATVP says the represented interests are ELNET France's own account [FCT-005]. Activity sheets explicitly record policy objectives and techniques intended to influence public decisions [FCT-006,FCT-007,FCT-008,FCT-026].

## Trips and access
Official Assembly disclosures establish ELNET-supported travel by Sylvain Maillard and Aurore Berge in October 2024 [FCT-009,FCT-010] and multiple MPs in July 2021, including a declared 38-elected-official mission meeting senior Israeli authorities [FCT-011,FCT-012,FCT-013]. ELNET's own 2023 material says a delegation was organized around themes apt to inspire parliamentary action and records high-level political, diplomatic, military and civil-society meetings [FCT-014,FCT-015,FCT-016]. These first-party accounts prove intended exposure and agenda formation, not behavioral effect [FCT-017].

## Decision/effect ceiling
An ELNET-organized 2019 meeting records Sylvain Maillard presenting an already-existing resolution project. It proves contact around a legislative object, not ELNET causation [FCT-018]. A direct institutional request for sanctions is likewise an influence attempt, not proof of outcome [FCT-019]. The 2025 Assembly inquiry proposal is allegation/procedure, not a finding [FCT-020].

The most discriminating counterexample is the 2025 Palestine-recognition objective. ELNET France declared an objective to prevent French recognition, but France recognized the State of Palestine on 22 September 2025 [FCT-006,FCT-022]. Repeated access therefore does not imply reliable control of French foreign policy. This does not prove zero intermediate influence.

## Attribution and funding
HATVP's own-account declaration [FCT-005] and the absence of authenticated tasking in this run block a general Israeli-state proxy inference. Prior INV-026 established only a specific Israeli-MFA-funded ELNET Europe event, not general ELNET France control. US Friends of ELNET has material resources, but inspected filings do not establish a direct transfer to the French entity [FCT-023].

## Result
The strongest supported chain is resources/declaration -> trips/events/meetings -> repeated access/exposure and agenda opportunity. Stronger edges, ELNET input -> participant change -> exact vote/law/policy outcome and Israeli-state -> ELNET France tasking, remain unresolved. Reopen only for audited French funding, authenticated tasking/control, a versioned legislative footprint, or a credible participant/policy causal design.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:7|SRC_COMPLETE:16/16

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **anchors:**
  - 2021 mass ELNET parliamentary trip
  - 2023 repeated delegations
  - 2024 ELNET travel disclosures
  - 2025 declared lobbying objectives and Palestine-recognition outcome
- **as_of:** 2026-09-10
- **window:** 2017-2026

### MANIPULATION_REPORT
- **assumptions:**
  - official HATVP and Assembly disclosures accurately report declared activities/trips
  - ELNET first-party pages accurately describe their own intended programs but are not independent effect evidence
  - Elysée announcement accurately states final recognition decision
- **clusters:**
  - POWER
  - NETWORK
  - INFORMATION
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - professional lobbying can be influential without proving capture
  - funded travel can shape exposure without proving behavior change
  - own-account declaration does not prove absence of external relationships
  - failed lobbying objective does not prove zero intermediate influence
- **input_kind:** RUN_CARD
- **mission_mode:** RECHECK_EXTEND
- **patterns:**
  - declared lobbying
  - funded/invited travel
  - repeated delegations
  - high-level briefings
  - policy-objective declaration
  - drafting suggestions
  - open-letter pressure
  - negative policy outcome
- **priorities:**
  - map declared lobbying resources
  - verify travel/access independently
  - test legislative/policy effect
  - test Israeli-state tasking
  - use contrary outcome as control
- **query_guidance:** prefer HATVP, parliamentary travel records, official decision records and versioned legislative traces; require authenticated orders for tasking and counterfactual/versioned text evidence for policy causality
- **rhetorical:**
  - **AUTH:** HATVP, Assemblée nationale, Sénat, Élysée plus bounded ELNET first-party records
  - **BF:** no named policy-effect counterfactual or authenticated general tasking
  - **DEM:** retain lawful transparent lobbying/interference distinction
  - **FAC:** separate intent, access, behavior, decision and effect
  - **NUM:** annual HATVP spending band and recurring travel events
- **speaker:**
  - **goal:** forensic separation of ELNET resources, access, influence attempt, tasking and policy effect
  - **target:** resource -> ELNET activity -> public official -> action -> decision -> effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** ELNET France
  - **S02:** interest representation
  - **S03:** declared expenditure
  - **S04:** parliamentary trip
  - **S05:** event/meeting
  - **S06:** French decision-maker
  - **S07:** Israeli official
  - **S08:** access/exposure
  - **S09:** agenda opportunity
  - **S10:** position/action
  - **S11:** law/vote/policy
  - **S12:** funding
  - **S13:** tasking/control
  - **S14:** counterfactual effect
  - **S15:** capture
- **threats:**
  - funding=tasking
  - trip=capture
  - access=influence
  - alignment=causality
  - lobbying objective=success
  - parliamentary allegation=finding
  - US support organization=French financing
  - specific event funding=general state control

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - counterfactual behavior data
  - **input_ids:**
    - FCT-009
    - FCT-012
    - FCT-014
    - FCT-015
    - FCT-025
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no participant behavior chain
  - **not_computable:**
    - informal contact denominator
  - **operations_applied:**
    - mapped trips/events/targets
  - **reason:** map access without promoting contact to control
  - **result_ids:**
    - CLM-002
    - CAU-001
  - **status:** DONE
  - **trigger:** repeated political networks
- **item 2:**
  - **gaps:**
    - legislative footprint
  - **input_ids:**
    - FCT-003
    - FCT-006
    - FCT-007
    - FCT-019
    - FCT-022
  - **module:** clusters/POWER.md
  - **negative_results:**
    - reliable policy control not supported
  - **not_computable:**
    - marginal policy effect
  - **operations_applied:**
    - mapped declared actions
    - tested objective against outcome
  - **reason:** separate influence attempt from control
  - **result_ids:**
    - CLM-001
    - CLM-003
    - CLM-006
    - CAU-002
    - CAU-005
  - **status:** DONE
  - **trigger:** representation and policy objectives
- **item 3:**
  - **gaps:**
    - pre/post participant evidence
  - **input_ids:**
    - FCT-014
    - FCT-015
    - FCT-016
    - FCT-017
  - **module:** clusters/INFORMATION.md
  - **negative_results:**
    - no persuasion design
  - **not_computable:**
    - belief shift
  - **operations_applied:**
    - mapped exposure
    - bounded first-party claims
  - **reason:** separate exposure from persuasion
  - **result_ids:**
    - CLM-002
    - CLM-004
    - CAU-003
  - **status:** DONE
  - **trigger:** briefings/persuasive exposure

### SCOPING_REPORT
- **boundary:** funding != tasking; trip != capture; access != influence; alignment != causality; lobbying != demonstrated effect
- **mode:** RECHECK_EXTEND
- **scope:** France, mainly 2017-2026
- **subject:** ELNET France resources, trips, networks, HATVP declarations and demonstrable effects

### CREDO
- **rules:**
  - trace resource -> activity -> access -> action -> decision -> effect
  - prefer official declarations and travel records
  - treat first-party ELNET records as intent/access evidence only
  - require authenticated tasking for state-control claim
  - require counterfactual/versioned footprint for causal policy effect

### COGNITIVE_MAP
- **continuum:**
  - resources
  - lobbying
  - trip/event
  - access/exposure
  - position/action
  - decision
  - counterfactual effect
- **core_model:** ELNET France is a professional declared lobbying/access platform. Trips and events produce repeated access/exposure; causal conversion into French votes, laws or policy is not established.
- **rival_models:**
  - all activity is networking with no influence attempt
  - all ELNET activity is Israeli-state tasking
  - trip participation proves capture
  - declared objective proves success

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** HATVP records explicit influence attempts
  - **synthesis:** intent/access established; effect/capture separate
  - **thesis:** networking only
- **item 2:**
  - **antithesis:** official travel disclosures lack changed-vote evidence
  - **synthesis:** trips are a material access mechanism, not causal endpoint
  - **thesis:** funded trips prove capture
- **item 3:**
  - **antithesis:** France recognized Palestine against an explicit ELNET objective
  - **synthesis:** reliable-control model unsupported; issue-specific influence remains testable
  - **thesis:** repeated access means policy control

### RESOURCE_FLOW_MAP
- **item 1:**
  - **amount:** EUR100k-200k yearly band, 2021-2025
  - **flow:** ELNET France declared lobbying expenditure
  - **support:**
    - FCT-003
    - FCT-004
- **item 2:**
  - **amount:** in-kind/trip; aggregate unknown
  - **flow:** ELNET-supported/invited travel
  - **support:**
    - FCT-009
    - FCT-010
    - FCT-011
    - FCT-012
- **item 3:**
  - **amount:** UNKNOWN
  - **flow:** US Friends of ELNET -> ELNET France
  - **support:**
    - FCT-023

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** ELNET France
  - **relation:** declared lobbying, trips, events, correspondence
  - **support:**
    - FCT-001
    - FCT-006
    - FCT-007
    - FCT-009
    - FCT-012
    - FCT-014
    - FCT-025
  - **to:** French public decision-makers
- **item 2:**
  - **from:** ELNET-organized delegations
  - **relation:** meetings/briefings
  - **support:**
    - FCT-015
    - FCT-016
  - **to:** Israeli governmental/parliamentary/military/civil actors
- **item 3:**
  - **from:** US Friends of ELNET
  - **relation:** possible ecosystem resource only
  - **support:**
    - FCT-023
  - **to:** French transfer unresolved

### IMPACT_MAP
- **distal:** law/vote/foreign-policy marginal effect unresolved
- **intermediate:** participant positions/actions unresolved
- **negative_control:** 2025 French Palestine recognition contrary to declared ELNET objective
- **proximal:**
  - repeated access/exposure
  - agenda opportunity

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** Palestine-recognition objective failed
  - **issue:** access versus control
  - **pro:** repeated trips and senior contacts
  - **resolution:** ACCESS_SUPPORTED_CONTROL_NOT_ESTABLISHED
  - **support:**
    - FCT-009
    - FCT-014
    - FCT-022
- **item 2:**
  - **contra:** HATVP own-account activities
  - **issue:** state relationship
  - **pro:** prior INV-026 specific MFA funding to ELNET Europe event
  - **resolution:** SPECIFIC_RELATION_NOT_GENERAL_TASKING
  - **support:**
    - FCT-005
- **item 3:**
  - **contra:** no versioned causal footprint
  - **issue:** legislative effect
  - **pro:** explicit legislative objectives/drafting suggestions
  - **resolution:** INTENT_SUPPORTED_EFFECT_UNRESOLVED
  - **support:**
    - FCT-007
    - FCT-018

### VERIFICATION_REPORT
- **downgraded:**
  - trip means capture
  - lobbying objective means policy success
  - pro-Israel alignment means state tasking
  - contact means coordination
- **fact_count:** 26
- **negative_controls:**
  - own-account HATVP status
  - inquiry proposal not finding
  - 2019 reverse chronology
  - 2025 contrary policy outcome
  - US support scale not France transfer
- **provenance_families:** 4
- **query_count:** 19
- **source_count:** 16
- **verification:** 26 bounded facts linked to 16 sources across HATVP, official Assembly travel disclosures, ELNET first-party records, parliamentary oversight, presidential decision and financial context, plus three explicit negative searches.

### EDI_REPORT
- **corpus:**
  - **limits:**
    - no audited French donor-transfer chain obtained
    - no authenticated general Israeli-state tasking record
    - no versioned ELNET contribution-to-adopted-clause chain
    - no participant-level counterfactual behavior design
  - **strength:** official HATVP activity/spending data, official Assembly travel declarations, Elysée final policy decision, bounded first-party ELNET program records
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
  - **owner:** ELNET France and public decision-makers; state-tasking edge unresolved
  - **perspective:** resources, access, influence intent, behavior, decision, capture boundary
  - **stratification:** resource -> activity -> access/exposure -> position/action -> decision -> effect
  - **temporal:** 2017-2026 with 2021, 2023, 2024 and 2025 anchors
- **edi:**
  - **coverage:** HIGH_FOR_DECLARED_LOBBYING_AND_TRAVEL_ACCESS; MODERATE_FOR_NETWORK_REPEATABILITY; LOW_FOR_CAUSAL_POLICY_EFFECT_AND_TASKING
  - **independence:** STRONG_OFFICIAL_HATVP_ASSEMBLY_ELYSEE_WITH_FIRST_PARTY_PROGRAM_DETAIL
- **source_counts:**
  - **A:** 5
  - **B:** 7
  - **C:** 3
  - **D:** 1
  - **E:** 0
  - **total:** 16

### RESPONSIBILITY_MAP
- **ELNET_France_declared_interest:** own account per HATVP
- **Israeli_state_tasking_general:** UNRESOLVED
- **US_Friends_to_France_transfer:** UNRESOLVED
- **parliamentary_inquiry_allegations:** NOT_FINDINGS
- **specific_policy_effect:** UNRESOLVED

### NEXT_QUERIES
- Acquire audited ELNET France accounts or transfer records to identify direct funders and separate ecosystem scale from French-entity resources.
- For one named legislative dossier, obtain ELNET position text plus successive draft/amendment/final versions to build a clause-level footprint.
- For a named trip participant, reconstruct pre-trip and post-trip positions/actions and compare against non-participants or prior trend.
- Seek authenticated Israeli-state instructions, contracts or control rights over ELNET France rather than inferring tasking from alignment or specific event funding.

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-002,QRY-003 | support:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-026 | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-026 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-002,QRY-003 | support:FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-024,FCT-025 | counter:- | results:FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-024,FCT-025 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-001,QRY-002,QRY-003 | support:FCT-017,FCT-018,FCT-019,FCT-022 | counter:- | results:FCT-017,FCT-018,FCT-019,FCT-022 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-001,QRY-002,QRY-003 | support:FCT-005,FCT-020,FCT-021,FCT-022,FCT-023 | counter:- | results:FCT-005,FCT-020,FCT-021,FCT-022,FCT-023 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,SRC-001 | support:FCT-001,FCT-003,FCT-004,FCT-006,FCT-007,FCT-026 | counter:- | results:FCT-001,FCT-003,FCT-004,FCT-006,FCT-007,FCT-026 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-015,SRC-002,SRC-003,SRC-004,SRC-005,SRC-006,SRC-015 | support:FCT-009,FCT-010,FCT-011,FCT-012,FCT-014,FCT-015,FCT-024 | counter:CTRL-001 | results:FCT-009,FCT-010,FCT-011,FCT-012,FCT-014,FCT-015,FCT-024,CTRL-001 | final:SUPPORTED | gap:CAUSALITY
CLM-003 | attempts:QRY-001,QRY-005,QRY-006,QRY-009,SRC-001,SRC-005,SRC-006,SRC-009 | support:FCT-006,FCT-007,FCT-014,FCT-016,FCT-019 | counter:CTRL-002 | results:FCT-006,FCT-007,FCT-014,FCT-016,FCT-019,CTRL-002 | final:SUPPORTED | gap:CAUSALITY
CLM-004 | attempts:QRY-006,QRY-008,SRC-006,SRC-008 | support:FCT-016,FCT-018 | counter:CTRL-003 | results:FCT-016,FCT-018,CTRL-003 | final:PARTIAL | gap:CAUSALITY
CLM-005 | attempts:QRY-001,SRC-001 | support:FCT-005 | counter:CTRL-004 | results:FCT-005,CTRL-004 | final:PARTIAL | gap:RESPONSIBILITY
CLM-006 | attempts:QRY-001,SRC-001 | support:FCT-006,FCT-026 | counter:CTRL-005 | results:FCT-006,FCT-026,CTRL-005 | final:PARTIAL | gap:CAUSALITY
CLM-007 | attempts:QRY-014,SRC-014 | support:FCT-023 | counter:CTRL-006 | results:FCT-023,CTRL-006 | final:PARTIAL | gap:RESOURCE_FLOW

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-002 | CLM | SUPPORTED | CAUSALITY | Access does not identify changed vote or decision.
CLM-003 | CLM | SUPPORTED | CAUSALITY | Intent does not establish success or control.
CLM-004 | CLM | PARTIAL | CAUSALITY | No versioned contribution-to-text trace or counterfactual isolates marginal effect.
CLM-005 | CLM | PARTIAL | RESPONSIBILITY | Own-account declaration and no authenticated general tasking record; prior INV-026 had only specific ELNET Europe transaction funding.
CLM-006 | CLM | PARTIAL | CAUSALITY | The 2025 Palestine-recognition objective failed at final policy outcome.
CLM-007 | CLM | PARTIAL | RESOURCE_FLOW | No direct transfer record to French entity obtained.
CAU-003 | CAU | UNRESOLVED | CAUSALITY | Need participant pre/post or versioned legislative footprint with counterfactual.
CAU-004 | CAU | UNRESOLVED | RESPONSIBILITY | Need authenticated orders/contracts/control rights.
CAU-005 | CAU | UNRESOLVED | CAUSALITY | Counterexample rejects reliable-control model; intermediate influence remains unknown.
CAU-006 | CAU | UNRESOLVED | RESOURCE_FLOW | Need audited French accounts or transfer records.

SEMANTIC_COUNTS_V1:LED:0|CLM:7|AXS:4|CAU:6|CTRL:6|ACT:4

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"ELNET France is a declared professional interest-representation organization with stable six-figure annual lobbying expenditure and explicit policy objectives.","claimant":"INV-027 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-003","FCT-004","FCT-006","FCT-007","FCT-026"]}
CLM-002 | {"claim":"ELNET-funded or organized parliamentary trips create repeated access/exposure to Israeli political, diplomatic, military and civil-society actors.","claimant":"INV-027 synthesis","counter":"CTRL-001","gap":"Access does not identify changed vote or decision.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-014","FCT-015","FCT-024"]}
CLM-003 | {"claim":"ELNET deliberately seeks to shape parliamentary agendas and public decisions.","claimant":"INV-027 synthesis","counter":"CTRL-002","gap":"Intent does not establish success or control.","gap_type":"CAUSALITY","materiality":"HIGH","status":"SUPPORTED","support":["FCT-006","FCT-007","FCT-014","FCT-016","FCT-019"]}
CLM-004 | {"claim":"A specific ELNET proposal or trip caused an adopted French law, amendment, vote or foreign-policy decision.","claimant":"INV-027 synthesis","counter":"CTRL-003","gap":"No versioned contribution-to-text trace or counterfactual isolates marginal effect.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-016","FCT-018"]}
CLM-005 | {"claim":"ELNET France is generally tasked or controlled by the Israeli state.","claimant":"INV-027 synthesis","counter":"CTRL-004","gap":"Own-account declaration and no authenticated general tasking record; prior INV-026 had only specific ELNET Europe transaction funding.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-005"]}
CLM-006 | {"claim":"ELNET access amounts to reliable control of French policy.","claimant":"INV-027 synthesis","counter":"CTRL-005","gap":"The 2025 Palestine-recognition objective failed at final policy outcome.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-006","FCT-026"]}
CLM-007 | {"claim":"US Friends of ELNET funding directly financed ELNET France in the inspected period.","claimant":"INV-027 synthesis","counter":"CTRL-006","gap":"No direct transfer record to French entity obtained.","gap_type":"RESOURCE_FLOW","materiality":"IMPORTANT","status":"PARTIAL","support":["FCT-023"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003"],"axis":"resources_and_declared_lobbying","inv_id":"INV-027","links":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-026"],"question":"What resources and declared representation activities are documented?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-026"],"sought_objects":["spending","staff","objectives","own-account"],"status":"SATURATED","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-026"]}
AXS-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003"],"axis":"trips_events_access","inv_id":"INV-027","links":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-024","FCT-025"],"question":"Do funded trips/events create repeated access?","result_ids":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-024","FCT-025"],"sought_objects":["travel","delegations","meetings"],"status":"SATURATED","support":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-024","FCT-025"]}
AXS-003 | {"attempt_ids":["QRY-001","QRY-002","QRY-003"],"axis":"position_decision_effect","inv_id":"INV-027","links":["FCT-017","FCT-018","FCT-019","FCT-022"],"question":"Can activity be tied causally to a decision?","result_ids":["FCT-017","FCT-018","FCT-019","FCT-022"],"sought_objects":["footprint","chronology","policy outcome"],"status":"SATURATED","support":["FCT-017","FCT-018","FCT-019","FCT-022"]}
AXS-004 | {"attempt_ids":["QRY-001","QRY-002","QRY-003"],"axis":"tasking_capture_boundary","inv_id":"INV-027","links":["FCT-005","FCT-020","FCT-021","FCT-022","FCT-023"],"question":"Does funding/access establish state tasking or capture?","result_ids":["FCT-005","FCT-020","FCT-021","FCT-022","FCT-023"],"sought_objects":["tasking records","own-account","findings"],"status":"SATURATED","support":["FCT-005","FCT-020","FCT-021","FCT-022","FCT-023"]}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"access/exposure","counter":"CTRL-001","limit":"Access/exposure only, not behavior change.","mechanism":"ELNET resources/lobbying -> trips/events/meetings -> repeated parliamentary access/exposure","status":"SUPPORTED","support":["FCT-003","FCT-004","FCT-009","FCT-011","FCT-012","FCT-014","FCT-015","FCT-024","FCT-025"]}
CAU-002 | {"causal_right":"agenda opportunity","counter":"CTRL-002","limit":"Intent/opportunity are not adoption.","mechanism":"declared objective + suggestions/correspondence/events -> opportunity to shape policy agenda","status":"SUPPORTED","support":["FCT-006","FCT-007","FCT-016","FCT-019","FCT-026"]}
CAU-003 | {"counter":"CTRL-003","gap":"Need participant pre/post or versioned legislative footprint with counterfactual.","gap_type":"CAUSALITY","limit":"No causal identification.","mechanism":"ELNET trip/contact -> participant position/vote -> adopted decision","status":"UNRESOLVED","support":["FCT-016","FCT-018"]}
CAU-004 | {"counter":"CTRL-004","gap":"Need authenticated orders/contracts/control rights.","gap_type":"RESPONSIBILITY","limit":"Specific prior event funding cannot generalize.","mechanism":"Israeli-state tasking -> ELNET France general program -> French political action","status":"UNRESOLVED","support":["FCT-005"]}
CAU-005 | {"counter":"CTRL-005","gap":"Counterexample rejects reliable-control model; intermediate influence remains unknown.","gap_type":"CAUSALITY","limit":"Observed outcome opposed declared objective.","mechanism":"ELNET anti-recognition lobbying -> French Palestine-recognition decision","status":"UNRESOLVED","support":["FCT-006","FCT-022"]}
CAU-006 | {"counter":"CTRL-006","gap":"Need audited French accounts or transfer records.","gap_type":"RESOURCE_FLOW","limit":"US scale does not identify French transfers.","mechanism":"US Friends resources -> direct ELNET France financing -> lobbying capacity","status":"UNRESOLVED","support":["FCT-023"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Funding/trip/access is not influence, tasking or capture without downstream evidence.","status":"DONE","support":["FCT-009","FCT-010","FCT-011","FCT-012"]}
CTRL-002 | {"control":"First-party inspiration/commitment claims are intent/self-report, not independent effect evidence.","status":"DONE","support":["FCT-014","FCT-016","FCT-017"]}
CTRL-003 | {"control":"Existing-proposal chronology blocks reverse attribution for Maillard 2019.","status":"DONE","support":["FCT-018"]}
CTRL-004 | {"control":"Own-account declaration and prior specific funding cannot establish general state tasking.","status":"DONE","support":["FCT-005"]}
CTRL-005 | {"control":"Palestine recognition is negative control against reliable policy control, not proof of zero influence.","status":"DONE","support":["FCT-006","FCT-022"]}
CTRL-006 | {"control":"Inquiry proposal is allegation/procedure, not factual finding.","status":"DONE","support":["FCT-020"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Keep access/exposure as highest generally closed edge.","actor":"routing/control plane","intent":"prevent causal inflation","status":"DONE","support":["FCT-009","FCT-012","FCT-014","FCT-015"]}
ACT-002 | {"action":"Require versioned legislative footprint for policy-effect upgrade.","actor":"routing/control plane","intent":"causal closure","status":"DONE","support":["FCT-018","FCT-022"]}
ACT-003 | {"action":"Keep Israeli-state tasking separate from pro-Israel lobbying identity.","actor":"routing/control plane","intent":"attribution discipline","status":"DONE","support":["FCT-005","FCT-021"]}
ACT-004 | {"action":"Do not infer French funding from US support-organization scale.","actor":"routing/control plane","intent":"resource-flow discipline","status":"DONE","support":["FCT-023"]}

SEARCH_ACTIVITY_V1:WEB:3|FETCH:16|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL | mnemo | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.hatvp.fr/fiche-organisation/?organisation=531006237 | FETCH HATVP-ELNET
QRY-002 | FETCH | FOUND | SRC-002 | https://www.assemblee-nationale.fr/dyn/donsetvoyages/voyages?limit=5&page=12 | FETCH AN-TRAVEL-17
QRY-003 | FETCH | FOUND | SRC-003 | https://www.assemblee-nationale.fr/dyn/15/donsetvoyages/voyages?limit=5&page=5 | FETCH AN-TRAVEL-15-P5
QRY-004 | FETCH | FOUND | SRC-004 | https://www.assemblee-nationale.fr/dyn/15/donsetvoyages/voyages?limit=5&page=6 | FETCH AN-TRAVEL-15-P6
QRY-005 | FETCH | FOUND | SRC-005 | https://elnetwork.fr/chronique/delegation-parlementaire-en-israel-quelle-mission-pour-elnet-france/ | FETCH ELNET-MISSION-2023
QRY-006 | FETCH | FOUND | SRC-006 | https://elnetwork.fr/delegation/delegation-parlementaire-les-republicains-en-israel-mars-2023/ | FETCH ELNET-LR-2023
QRY-007 | FETCH | FOUND | SRC-007 | https://elnetwork.fr/vie-parlementaire-et-politique/place-du-palais-bourbon-semaine-du-13-au-17-mars-2023/ | FETCH ELNET-PB-2023
QRY-008 | FETCH | FOUND | SRC-008 | https://elnetwork.fr/delegation/evenement-compte-rendu-de-delegation-conseil-regional-de-samarie-a-paris-28-29-mai-2019/ | FETCH ELNET-SAMARIA-2019
QRY-009 | FETCH | FOUND | SRC-009 | https://elnetwork.fr/communique/lettre-ouverte-a-la-presidente-de-lassemblee-nationale/ | FETCH ELNET-CARON-LETTER
QRY-010 | FETCH | FOUND | SRC-010 | https://www.assemblee-nationale.fr/dyn/17/dossiers/ingerences_politiques_elnet_france_influence_gouvernement | FETCH AN-RES-1000
QRY-011 | FETCH | FOUND | SRC-011 | https://www.assemblee-nationale.fr/dyn/docs/PNREANR5L17B1000.raw | FETCH AN-RES-1000-RAW
QRY-012 | FETCH | FOUND | SRC-012 | https://www.senat.fr/rap/r23-739-2/r23-739-21.html | FETCH SENAT-FOREIGN-INFLUENCE
QRY-013 | FETCH | FOUND | SRC-013 | https://www.elysee.fr/emmanuel-macron/2025/09/22/80e-session-de-lassemblee-generale-des-nations-unies-a-new-york-premiere-journee | FETCH ELYSEE-PALESTINE-2025
QRY-014 | FETCH | FOUND | SRC-014 | https://projects.propublica.org/nonprofits/organizations/452212393 | FETCH PROPUBLICA-FOELNET
QRY-015 | FETCH | FOUND | SRC-015 | https://elnetwork.fr/delegations/ | FETCH ELNET-DELEGATIONS
QRY-016 | FETCH | FOUND | SRC-016 | https://elnetwork.fr/vie-parlementaire-et-politique/place-du-palais-bourbon-semaine-du-19-au-23-juin-2023/ | FETCH ELNET-FORUM-2023
QRY-017 | WEB | NON_TROUVE | - | - | ELNET France authenticated Israeli state tasking general lobbying program order instruction contract
QRY-018 | WEB | NON_TROUVE | - | - | ELNET France causal evidence parliamentary trip changed vote law policy counterfactual
QRY-019 | WEB | NON_TROUVE | - | - | ELNET France donor transfer Friends of ELNET France audited accounts direct grant

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | HATVP-ELNET | HATVP fiche ELNET France | 2026-03-31 | 2026-09-10T08:13:16Z | identity activities spending own-account | https://www.hatvp.fr/fiche-organisation/?organisation=531006237
SRC-002 | ◈ | fam:A | AN-TRAVEL-17 | Assemblée nationale déplacements 17e | 2024-11-26 | 2026-09-10T08:13:16Z | Maillard Bergé ELNET trips 2024 | https://www.assemblee-nationale.fr/dyn/donsetvoyages/voyages?limit=5&page=12
SRC-003 | ◈ | fam:A | AN-TRAVEL-15-P5 | Assemblée nationale déplacements 15e p5 | 2021-09-01 | 2026-09-10T08:13:16Z | Corceiro Belhaddad Mis trip | https://www.assemblee-nationale.fr/dyn/15/donsetvoyages/voyages?limit=5&page=5
SRC-004 | ◈ | fam:A | AN-TRAVEL-15-P6 | Assemblée nationale déplacements 15e p6 | 2021-07-12 | 2026-09-10T08:13:16Z | Pupponi Marleix delegation | https://www.assemblee-nationale.fr/dyn/15/donsetvoyages/voyages?limit=5&page=6
SRC-005 | ◈ | fam:B | ELNET-MISSION-2023 | ELNET mission delegation 2023 | 2023-03-16 | 2026-09-10T08:13:16Z | inspire parliamentary action | https://elnetwork.fr/chronique/delegation-parlementaire-en-israel-quelle-mission-pour-elnet-france/
SRC-006 | ◈ | fam:B | ELNET-LR-2023 | ELNET délégation LR 2023 | 2023-03-18 | 2026-09-10T08:13:16Z | 15 MPs high-level meetings | https://elnetwork.fr/delegation/delegation-parlementaire-les-republicains-en-israel-mars-2023/
SRC-007 | ◈ | fam:B | ELNET-PB-2023 | ELNET Palais Bourbon mars 2023 | 2023-03-17 | 2026-09-10T08:13:16Z | delegation framing | https://elnetwork.fr/vie-parlementaire-et-politique/place-du-palais-bourbon-semaine-du-13-au-17-mars-2023/
SRC-008 | ◈ | fam:B | ELNET-SAMARIA-2019 | ELNET Samarie Paris 2019 | 2019-05-29 | 2026-09-10T08:13:16Z | Maillard resolution discussion | https://elnetwork.fr/delegation/evenement-compte-rendu-de-delegation-conseil-regional-de-samarie-a-paris-28-29-mai-2019/
SRC-009 | ◈ | fam:B | ELNET-CARON-LETTER | ELNET lettre ouverte AN | 2024-01-01 | 2026-09-10T08:13:16Z | disciplinary request | https://elnetwork.fr/communique/lettre-ouverte-a-la-presidente-de-lassemblee-nationale/
SRC-010 | ◈ | fam:C | AN-RES-1000 | Assemblée nationale résolution enquête ELNET | 2025-02-19 | 2026-09-10T08:13:16Z | proposal not finding | https://www.assemblee-nationale.fr/dyn/17/dossiers/ingerences_politiques_elnet_france_influence_gouvernement
SRC-011 | ◈ | fam:C | AN-RES-1000-RAW | Assemblée nationale résolution 1000 texte | 2025-02-19 | 2026-09-10T08:13:16Z | authors allegations | https://www.assemblee-nationale.fr/dyn/docs/PNREANR5L17B1000.raw
SRC-012 | ◈ | fam:C | SENAT-FOREIGN-INFLUENCE | Sénat influence étrangère | 2024-07-01 | 2026-09-10T08:13:16Z | transparent influence vs interference | https://www.senat.fr/rap/r23-739-2/r23-739-21.html
SRC-013 | ◈ | fam:A | ELYSEE-PALESTINE-2025 | Élysée reconnaissance Palestine | 2025-09-22 | 2026-09-10T08:13:16Z | France recognizes Palestine | https://www.elysee.fr/emmanuel-macron/2025/09/22/80e-session-de-lassemblee-generale-des-nations-unies-a-new-york-premiere-journee
SRC-014 | ◈ | fam:D | PROPUBLICA-FOELNET | ProPublica Friends of ELNET | 2026-09-10 | 2026-09-10T08:13:16Z | US support organization scale | https://projects.propublica.org/nonprofits/organizations/452212393
SRC-015 | ◈ | fam:B | ELNET-DELEGATIONS | ELNET délégations index | 2026-09-10 | 2026-09-10T08:13:16Z | repeated delegations | https://elnetwork.fr/delegations/
SRC-016 | ◈ | fam:B | ELNET-FORUM-2023 | ELNET forum juin 2023 | 2023-06-23 | 2026-09-10T08:13:16Z | parliamentary forum | https://elnetwork.fr/vie-parlementaire-et-politique/place-du-palais-bourbon-semaine-du-19-au-23-juin-2023/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.hatvp.fr/fiche-organisation/?organisation=531006237 | A | 2026-03-31 | registered representative | HATVP identifies ELNET France as an association intervening at local and national levels in international cooperation and public institutions. | -
FCT-002 | FACT | ✧ | https://www.hatvp.fr/fiche-organisation/?organisation=531006237 | A | 2026-03-31 | named representatives | HATVP lists Ariel Bellaiche, Charlotte Gribe and Arie Bensemhoun as persons responsible for interest representation. | -
FCT-003 | FACT | ✧ | https://www.hatvp.fr/fiche-organisation/?organisation=531006237 | A | 2021-2025 | spending band | HATVP shows declared representation spending at at least EUR100,000 and below EUR200,000 for each year 2021 through 2025. | -
FCT-004 | FACT | ✧ | https://www.hatvp.fr/fiche-organisation/?organisation=531006237 | A | 2021-2025 | representation staffing | HATVP records three persons devoted to interest representation and notes spending includes salaries and events with public decision-makers. | -
FCT-005 | FACT | ✧ | https://www.hatvp.fr/fiche-organisation/?organisation=531006237 | A | 2025 | own-account representation | HATVP activity sheets state ELNET France performed declared representation activities for its own account. | -
FCT-006 | FACT | ✧ | https://www.hatvp.fr/fiche-organisation/?organisation=531006237 | A | 2025 | anti-recognition objective | A 2025 HATVP activity objective is to oppose recognition of the State of Palestine by France, targeting presidential, parliamentary and foreign-affairs actors. | -
FCT-007 | FACT | ✧ | https://www.hatvp.fr/fiche-organisation/?organisation=531006237 | A | 2025 | declared influence techniques | HATVP records actions including transmitting suggestions to influence drafting of public decisions, correspondence, debates and events. | -
FCT-008 | FACT | ✧ | https://www.hatvp.fr/fiche-organisation/?organisation=531006237 | A | 2021 | historical policy objectives | Historical HATVP sheets include strengthening parliamentary/legal action against anti-Jewish hatred and inspiring French political actors on vaccination policy. | -
FCT-009 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/donsetvoyages/voyages?limit=5&page=12 | A | 2024-10-06 | Maillard trip | Assembly travel disclosure records Sylvain Maillard in Israel 6-9 October 2024 with ELNET as third-party funder. | -
FCT-010 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/donsetvoyages/voyages?limit=5&page=12 | A | 2024-10-06 | Berge trip | Assembly travel disclosure records Aurore Berge in Israel 6-8 October 2024 invited by ELNET. | -
FCT-011 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/15/donsetvoyages/voyages?limit=5&page=5 | A | 2021-07-18 | multiple MPs 2021 trip | Assembly disclosures identify David Corceiro, Belkhir Belhaddad and Jean-Michel Mis among MPs travelling to Israel with ELNET as organizer/funder. | -
FCT-012 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/15/donsetvoyages/voyages?limit=5&page=6 | A | 2021-07-18 | 38 elected officials mission | François Pupponi declared an ELNET France mission involving 38 elected officials and meetings with high Israeli authorities. | -
FCT-013 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/15/donsetvoyages/voyages?limit=5&page=6 | A | 2021-07-18 | strategic framing | The 2021 disclosure frames the mission as promoting France-Israel strategic relations and covering security, Covid, Abraham Accords and regional conflict. | -
FCT-014 | FACT | ✧ | https://elnetwork.fr/chronique/delegation-parlementaire-en-israel-quelle-mission-pour-elnet-france/ | B | 2023-03-16 | inspire parliamentary action | ELNET France stated the March 2023 delegation was designed around themes apt to inspire MPs parliamentary action on return to France. | -
FCT-015 | FACT | ✧ | https://elnetwork.fr/delegation/delegation-parlementaire-les-republicains-en-israel-mars-2023/ | B | 2023-03-18 | 15 LR MPs high-level access | ELNET reports organizing a 15-LR-MP delegation with meetings involving Israeli foreign-affairs, Knesset, military and civil-society actors. | -
FCT-016 | FACT | ✧ | https://elnetwork.fr/delegation/delegation-parlementaire-les-republicains-en-israel-mars-2023/ | B | 2023-03-18 | caucus suggestion | ELNET reports an Israeli Foreign Ministry official suggested creating a French parliamentary study group on the Abraham Accords and the delegation agreed to study modalities. | -
FCT-017 | FACT | ✧ | https://elnetwork.fr/delegation/delegation-parlementaire-les-republicains-en-israel-mars-2023/ | B | 2023-03-18 | first-party downstream claims | ELNET self-reports delegation commitments and lessons; these statements are first-party reporting, not independent causal measurement. | -
FCT-018 | FACT | ✧ | https://elnetwork.fr/delegation/evenement-compte-rendu-de-delegation-conseil-regional-de-samarie-a-paris-28-29-mai-2019/ | B | 2019-05-29 | resolution chronology | At an ELNET-organized 2019 meeting, Sylvain Maillard presented his existing resolution project; contact is proven, ELNET causation is not. | -
FCT-019 | FACT | ✧ | https://elnetwork.fr/communique/lettre-ouverte-a-la-presidente-de-lassemblee-nationale/ | B | 2024-01-01 | disciplinary request | An ELNET France open letter asked the President of the National Assembly for disciplinary sanctions against MP Aymeric Caron; request does not prove outcome. | -
FCT-020 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/17/dossiers/ingerences_politiques_elnet_france_influence_gouvernement | C | 2025-02-19 | inquiry proposal not finding | Assembly dossier confirms resolution proposal no.1000 seeking an inquiry was deposited and referred to the Laws Committee; this is allegation/procedure, not an established finding. | -
FCT-021 | FACT | ✧ | https://www.senat.fr/rap/r23-739-2/r23-739-21.html | C | 2024-07-01 | transparent influence boundary | Senate work distinguishes transparent lawful influence from covert/deceptive interference; invitation/contact alone is insufficient for an interference finding. | -
FCT-022 | FACT | ✧ | https://www.elysee.fr/emmanuel-macron/2025/09/22/80e-session-de-lassemblee-generale-des-nations-unies-a-new-york-premiere-journee | A | 2025-09-22 | Palestine recognition negative control | President Macron declared that France recognized the State of Palestine, contrary to ELNET Frances declared 2025 objective to prevent recognition. | -
FCT-023 | FACT | ✧ | https://projects.propublica.org/nonprofits/organizations/452212393 | D | 2024 | US support organization scale | US Friends of ELNET filings show multimillion-dollar annual contributions/revenue; this does not establish a direct transfer to ELNET France. | -
FCT-024 | FACT | ✧ | https://elnetwork.fr/delegations/ | B | 2026-09-10 | repeated delegation model | ELNETs delegation index documents repeated parliamentary/political delegations across years. | -
FCT-025 | FACT | ✧ | https://elnetwork.fr/vie-parlementaire-et-politique/place-du-palais-bourbon-semaine-du-19-au-23-juin-2023/ | B | 2023-06-23 | parliamentary forum access | ELNET reports a France-Germany-Israel parliamentary forum in the National Assembly with MPs and experts. | -
FCT-026 | FACT | ✧ | https://www.hatvp.fr/fiche-organisation/?organisation=531006237 | A | 2025 | senior target categories | HATVP sheets identify target categories including presidential collaborators, MPs/senators, government/cabinet members and foreign-affairs officials. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-001
FCT-005 | SRC-001
FCT-006 | SRC-001
FCT-007 | SRC-001
FCT-008 | SRC-001
FCT-009 | SRC-002
FCT-010 | SRC-002
FCT-011 | SRC-003
FCT-012 | SRC-004
FCT-013 | SRC-004
FCT-014 | SRC-005
FCT-015 | SRC-006
FCT-016 | SRC-006
FCT-017 | SRC-006
FCT-018 | SRC-008
FCT-019 | SRC-009
FCT-020 | SRC-010
FCT-021 | SRC-012
FCT-022 | SRC-013
FCT-023 | SRC-014
FCT-024 | SRC-015
FCT-025 | SRC-016
FCT-026 | SRC-001

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
ATTEMPT-001 | {"created_at":"2026-09-10T08:19:12.402090+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":26,"eligible":26,"failure":0,"success":0}}

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
