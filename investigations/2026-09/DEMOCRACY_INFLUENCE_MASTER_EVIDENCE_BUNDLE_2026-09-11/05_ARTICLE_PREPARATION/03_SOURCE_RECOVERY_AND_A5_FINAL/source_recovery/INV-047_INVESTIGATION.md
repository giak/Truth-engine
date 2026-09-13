ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260910-1108-eu-sanctions-coercion | PARENT_RUN_ID:NONE | AS_OF:2026-09-10
INPUT_KIND:RUN_CARD | MISSION_MODE:DEEPEN | INPUT_REF:PATH:/mnt/data/inv047/runtime/investigations/2026-09/2026-09-10_eu-sanctions-coercion/2026-09-10_11-08_eu-sanctions-coercion_INPUT.md | SUBJECT_SLUG:eu-sanctions-coercion | SUBJECT_FP:sha256:1f7858b400a39c3749862243d75c58b997f83d09002f10f60bf5fe2634391d8e | INPUT_SHA256:sha256:cdeb848eddb9181a119c549255a30b564e40e8b6f9029ac93de850a63fd9480f
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:EU restrictive measures, mainly 2014-2026; bounded Russia, Belarus, RT/Sputnik and Iran-JCPOA cases; trace legal act -> implementation -> constraint/cost -> adaptation -> behavior/political effect.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/NETWORK.md,clusters/INFORMATION.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Analytic body

## Object
INV-047 tests EU sanctions as a coercive instrument through the chain authority -> legal act/listing/restriction -> implementing intermediary -> target -> cost or information constraint -> adaptation -> behavior -> political effect. The central discipline is to separate direct legal implementation and proximal measurable effects from terminal policy compliance.

## Legal mechanism
The Council explicitly defines sanctions as targeted CFSP instruments intended to change policy or conduct rather than punish. Legal acts bind EU operators. In the information domain, Regulation 2022/350 prohibited broadcasting or facilitating listed RT/Sputnik content and suspended licences and distribution arrangements [FCT-001,FCT-002,FCT-015,FCT-016]. RT France challenged the measure; the General Court rejected the annulment action after examining competence, defence rights, expression, proportionality and business freedom [FCT-017]. This closes legal constraint and judicial review, not audience persuasion.

## Russia: economic constraint and adaptation
The Russia regime produces large proximal effects. Council figures place embargoed trade at more than EUR48bn of exports and EUR91.2bn of imports relative to 2021; Russia's share of EU oil imports fell from 25.8% to 2.2% between 2021 and 2025; more than EUR210bn of Russian central-bank assets are immobilised in the EU [FCT-004,FCT-007,FCT-008]. ECB evidence shows bilateral trade fell sharply and euro-area exports to Russia halved within months [FCT-009,FCT-012].

Those effects do not close a sanctions-only causal story. Russia redirects trade to non-sanctioning partners, the EU substitutes energy suppliers, and the 2014-2019 gravity literature finds heterogeneous enforcement, substitution and relabelling [FCT-010,FCT-011,FCT-024,FCT-025,FCT-026]. The sanctions objective of ending the war remained unfulfilled in 2026, when measures were still being renewed and expanded [FCT-003]. Therefore cost/constraint is supported; sanctions -> Russian policy reversal is unresolved.

## Information restriction
The RT/Sputnik case demonstrates that sanctions can operate directly on information distribution: EU operators are legally forbidden to broadcast or facilitate listed content and licences/arrangements are suspended [FCT-015,FCT-016]. This is a direct restriction on lawful distribution inside the EU. No source in the inspected corpus identifies a causal estimate from that restriction to reduced propaganda exposure, changed beliefs or political behavior. Distribution effect and persuasion effect remain distinct.

## Belarus: mixed political outcome
The Belarus regime is explicitly intended to pressure authorities to end repression, release political prisoners and open dialogue [FCT-018,FCT-019]. In July 2026 the EU welcomed 28 releases but still reported at least 863 political prisoners, new arrests and continuing repression; the sanctions framework remained active and was extended [FCT-020,FCT-021]. This is a negative/mixed control against equating sanctions with terminal policy compliance. It does not prove sanctions had zero effect; it shows the terminal causal chain is not closed.

## JCPOA comparator
JCPOA provides the clearest conditionality sequence in this bounded corpus. IAEA verification that Iran had implemented specified nuclear measures was followed on 16 January 2016 by agreed lifting of EU nuclear-related economic and financial sanctions [FCT-022,FCT-023]. That sequence supports sanctions relief as one component of a negotiated incentive architecture. It does not isolate the EU sanction component from UN, US and E3+3 diplomacy.

## Result
EU sanctions are neither merely symbolic nor reliably policy-determining. Their strongest supported effects are legal implementation and proximal restriction: transaction denial, trade and energy reorientation, asset immobilisation, revenue pressure and media-distribution suspension. Political compliance is a separate layer whose attribution depends on coalition breadth, implementation, target adaptation, substitutes and concurrent military/diplomatic causes. Reopen only on sanction-specific target-behavior causal designs or provider/audience evidence closing the information-effect chain.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:7|SRC_COMPLETE:18/18

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-10
- **breaks:**
  - 2014 Russia sanctions
  - 2015-2016 JCPOA conditionality/relief
  - 2020 Belarus sanctions
  - 2022 Russia escalation and RT/Sputnik broadcast restriction
  - 2025-2026 expanded Russia/Belarus measures
- **status:** ONGOING_REGIMES_WITH_BOUNDED_HISTORICAL_COMPARATOR
- **window:** 2014-2026

### MANIPULATION_REPORT
- **assumptions:**
  - official statistics describe legal implementation and reported magnitudes
  - academic designs apply only within stated periods and outcomes
  - continued sanctions do not by themselves prove ineffectiveness or effectiveness
- **clusters:**
  - POWER
  - NETWORK
  - INFORMATION
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - sanctions can work at one layer and fail at another
  - target and sender both adapt
  - legal enforcement can be direct while political effect is indirect
  - multilateral bargaining can create conditional compliance without single-actor attribution
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - restrictive measure
  - asset immobilisation
  - trade embargo
  - energy decoupling
  - revenue pressure
  - broadcast suspension
  - judicial review
  - trade diversion
  - circumvention
  - conditional sanctions relief
- **priorities:**
  - close legal implementation
  - measure proximal economic constraints
  - test adaptation/circumvention
  - separate information restriction from persuasion
  - seek target behavior evidence
  - retain negative controls
- **query_guidance:** prefer Council/EUR-Lex/Curia/Commission/ECB/EEAS and peer-reviewed causal or counterfactual studies; require decision-specific evidence for terminal behavior change
- **rhetorical:**
  - **AUTH:** EU legal acts, Council, Court, Commission, ECB and peer-reviewed studies
  - **BF:** no sanctions-only counterfactual for Russia war or Belarus repression
  - **DEM:** retain war shocks, countersanctions, trade diversion and diplomacy
  - **FAC:** separate legal act, implementation, constraint, adaptation and outcome
  - **NUM:** trade shares, immobilised assets, revenue changes and sanctioned entities
- **speaker:**
  - **goal:** forensic separation of legal constraint, proximal effect and terminal political effect
  - **target:** authority -> act -> intermediary -> target -> cost/constraint -> adaptation -> behavior -> political effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** Council legal act
  - **S02:** listing
  - **S03:** asset freeze
  - **S04:** trade ban
  - **S05:** broadcast ban
  - **S06:** EU operator
  - **S07:** target
  - **S08:** economic cost
  - **S09:** distribution constraint
  - **S10:** adaptation
  - **S11:** circumvention
  - **S12:** behavior change
  - **S13:** political outcome
  - **S14:** coalition
  - **S15:** counterfactual
- **threats:**
  - listing=guilt
  - cost=compliance
  - trade fall=single cause
  - ban=persuasion
  - sanctions=war outcome
  - release=sanction causality
  - JCPOA=EU-only effect

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - counterfactual political designs
  - **input_ids:**
    - FCT-003
    - FCT-006
    - FCT-008
    - FCT-019
    - FCT-022
  - **module:** clusters/POWER.md
  - **negative_results:**
    - Russia war objective not closed
    - Belarus repression persists
  - **not_computable:**
    - sanctions-only political effect
  - **operations_applied:**
    - mapped constraint-to-behavior chain
    - tested terminal policy outcomes
  - **reason:** separate costs from political compliance
  - **result_ids:**
    - CLM-003
    - CLM-005
    - CLM-006
    - CAU-004
    - CAU-006
    - CAU-007
  - **status:** DONE
  - **trigger:** coercive policy-change claims
- **item 2:**
  - **gaps:**
    - firm-level enforcement/circumvention traces
  - **input_ids:**
    - FCT-002
    - FCT-010
    - FCT-014
    - FCT-025
    - FCT-026
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no frictionless implementation assumption
  - **not_computable:**
    - complete evasion denominator
  - **operations_applied:**
    - mapped intermediary enforcement
    - retained coalition breadth and trade diversion
  - **reason:** map Council -> operators -> targets and coalition/adaptation effects
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-007
    - CAU-001
    - CAU-002
  - **status:** DONE
  - **trigger:** multi-actor implementation and circumvention
- **item 3:**
  - **gaps:**
    - platform/audience causal design
  - **input_ids:**
    - FCT-015
    - FCT-016
    - FCT-017
  - **module:** clusters/INFORMATION.md
  - **negative_results:**
    - no causal audience belief effect identified
  - **not_computable:**
    - counterfactual exposure/persuasion effect
  - **operations_applied:**
    - mapped legal ban to distribution restriction
    - tested downstream audience-effect claim
  - **reason:** separate distribution control from persuasion effect
  - **result_ids:**
    - CLM-004
    - CAU-005
  - **status:** DONE
  - **trigger:** RT/Sputnik broadcast sanctions

### SCOPING_REPORT
- **exclusions:**
  - generic morality of sanctions
  - listing=guilt
  - cost=policy change
  - broadcast ban=measured persuasion
  - chronology=causality
- **geo:** European Union with bounded Russia, Belarus and Iran comparators
- **object_coverage:** HIGH_FOR_LEGAL_AND_PROXIMAL_EFFECTS; MODERATE_FOR_ADAPTATION; LOW_FOR_TERMINAL_POLITICAL_CAUSALITY
- **object_question:** Par quels mécanismes les sanctions européennes exercent-elles une contrainte politique, économique ou informationnelle, et quels effets mesurables peuvent être attribués à des mesures identifiées sans confondre décision juridique, mise en œuvre, coercition, signal politique et changement de comportement ?
- **period:** mainly 2014-2026
- **subject:** Sanctions européennes comme instrument de coercition politique et informationnelle

### CREDO
- sanction != guilt
- legal restriction != target compliance
- cost != policy change
- trade decline != sanctions-only causality
- broadcast restriction != persuasion effect
- coordination breadth matters
- JCPOA sequence != EU-only causal attribution
- absence of proof != proof of absence

### COGNITIVE_MAP
- **continuum:**
  - political objective
  - Council act
  - listing/restriction
  - operator implementation
  - target access/cost
  - adaptation/circumvention
  - behavior
  - political outcome
- **core_model:** EU sanctions reliably create legal and often measurable proximal economic or information constraints. Their translation into terminal political behavior is heterogeneous, mediated by coalition breadth, implementation, substitution, target adaptation and other concurrent causes.
- **rival_models:**
  - sanctions never have real effects
  - any economic cost proves political success
  - broadcast bans prove persuasion reduction
  - all sanctions are equivalent across regimes
  - target behavior observed during sanctions is automatically caused by sanctions

### DIALECTICAL_MAP
- **antithesis:** Targets adapt, enforcement is imperfect and large costs often do not identify terminal policy change.
- **synthesis:** Sanctions effectiveness must be evaluated by layer: implementation and proximal constraint can be supported while political compliance remains unresolved.
- **thesis:** EU sanctions impose real legal, economic and information constraints and can structure negotiated conditionality.

### RESOURCE_FLOW_MAP
- **flows:**
  - Council legal authority -> EU operators -> denied funds/trade/services/distribution
  - trade/energy restrictions -> reduced bilateral flows and revenue access
  - asset immobilisation -> constrained sovereign financial resources
  - sanctions relief promise -> negotiated compliance incentive
- **limits:**
  - trade diversion and substitution
  - sender adaptation costs
  - circumvention and uneven implementation
  - political outcomes are multicausal

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** Council of the EU
  - **relation:** adopts CFSP restrictive measures and regulations
  - **support:**
    - FCT-001
    - FCT-002
  - **to:** EU operators and listed targets
- **item 2:**
  - **from:** EU financial/commercial operators
  - **relation:** implement freezes, bans and transaction restrictions
  - **support:**
    - FCT-004
    - FCT-008
  - **to:** Russian targets/economic channels
- **item 3:**
  - **from:** EU media/distribution operators
  - **relation:** broadcast and distribution prohibition
  - **support:**
    - FCT-015
    - FCT-016
  - **to:** RT/Sputnik listed entities
- **item 4:**
  - **from:** Russia and third-country partners
  - **relation:** trade diversion/substitution/circumvention responses
  - **support:**
    - FCT-010
    - FCT-025
    - FCT-026
  - **to:** sanctions pressure effectiveness
- **item 5:**
  - **from:** EU/E3+3/UN/US package
  - **relation:** conditional sanctions relief after IAEA verification
  - **support:**
    - FCT-022
    - FCT-023
  - **to:** Iran JCPOA implementation

### IMPACT_MAP
- **established:**
  - direct legal restrictions on EU operators
  - large bilateral trade and energy reorientation
  - Russian sovereign asset immobilisation
  - RT/Sputnik legal distribution restriction
  - JCPOA verified conditional relief sequence
- **not_established:**
  - sanctions-only termination of Russia war
  - EU-sanctions-caused end of Belarus repression
  - causal audience belief/persuasion effect from broadcast restrictions
- **partial:**
  - attribution of exact Russia revenue losses to specific measures
  - degree of circumvention and substitution
  - relative EU contribution inside multilateral JCPOA

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** Russia targeted policy and war persisted through 2026
  - **issue:** economic pressure versus political success
  - **pro:** large trade, energy, revenue and asset constraints
  - **resolution:** PROXIMAL_EFFECT_SUPPORTED_TERMINAL_POLICY_EFFECT_UNRESOLVED
  - **support:**
    - FCT-003
    - FCT-006
    - FCT-007
    - FCT-008
    - FCT-009
- **item 2:**
  - **contra:** at least 863 remained and new arrests/repression continued
  - **issue:** Belarus releases versus repression
  - **pro:** 28 political prisoners released
  - **resolution:** MIXED_OUTCOME_CAUSAL_ATTRIBUTION_UNRESOLVED
  - **support:**
    - FCT-019
    - FCT-020
- **item 3:**
  - **contra:** no identified causal measurement of beliefs/persuasion
  - **issue:** broadcast restriction versus information effect
  - **pro:** binding distribution ban and licence suspension
  - **resolution:** DISTRIBUTION_CONSTRAINT_SUPPORTED_PERSUASION_EFFECT_UNRESOLVED
  - **support:**
    - FCT-015
    - FCT-016
    - FCT-017
- **item 4:**
  - **contra:** multilateral bargaining prevents EU-only causal attribution
  - **issue:** JCPOA as success case
  - **pro:** verified nuclear measures preceded conditional sanctions relief
  - **resolution:** NEGOTIATED_CONDITIONALITY_SUPPORTED_EU_ONLY_EFFECT_UNRESOLVED
  - **support:**
    - FCT-022
    - FCT-023

### VERIFICATION_REPORT
- **downgraded:**
  - listing means guilt
  - cost means policy change
  - trade decline is sanctions-only
  - broadcast ban means persuasion reduction
  - prisoner release means EU causal success
- **fact_count:** 27
- **negative_controls:**
  - Russia war/policy objective remains unclosed
  - Belarus repression continues despite releases
  - no RT/Sputnik audience persuasion causal design identified
  - JCPOA is multilateral rather than EU-only
- **provenance_families:** 4
- **query_count:** 22
- **source_count:** 18
- **verification:** 27 bounded facts linked to 18 sources across EU legal acts, Council/Commission/EEAS/ECB, judiciary and peer-reviewed research, plus four explicit negative searches.

### EDI_REPORT
- **corpus:**
  - **limits:**
    - no sanctions-only counterfactual for Russia terminal policy behavior
    - no causal audience-effect design for media ban
    - Belarus release causality not isolated
    - JCPOA is a multilateral package
  - **strength:** binding EU legal texts plus current Council/Commission/EEAS/ECB evidence and peer-reviewed counterfactual trade research
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
  - **owner:** Council/EU operators/target governments depending stage
  - **perspective:** legal implementation, economic constraint, informational restriction, adaptation, political behavior
  - **stratification:** authority -> act -> intermediary -> target -> cost -> adaptation -> behavior -> outcome
  - **temporal:** 2014-2026 with JCPOA 2015-2016 comparator
- **edi:**
  - **coverage:** HIGH_FOR_LEGAL_IMPLEMENTATION; HIGH_FOR_PROXIMAL_ECONOMIC_EFFECTS; MODERATE_FOR_ADAPTATION; LOW_FOR_TERMINAL_POLITICAL_CAUSALITY
  - **independence:** STRONG_OFFICIAL_PLUS_JUDICIAL_PLUS_ECONOMIC_RESEARCH_WITH_NEGATIVE_CONTROLS
- **source_counts:**
  - **A:** 5
  - **B:** 7
  - **C:** 3
  - **D:** 3
  - **total:** 18

### RESPONSIBILITY_MAP
- **Belarus_behavior:** target-government decisions; EU sanctions causal contribution unresolved
- **JCPOA_behavior:** Iranian implementation within multilateral negotiated package; EU-only marginal effect unresolved
- **RT_distribution:** Council legal restriction implemented by distribution operators; judicially reviewed
- **Russia_economic_effect:** joint product of sanctions, war shock, countersanctions, boycotts, substitution and enforcement
- **implementation:** EU/member-state financial, customs, commercial and media operators under applicable legal acts
- **sanctions_authority:** Council of the EU; unanimity for CFSP sanctions

### NEXT_QUERIES
- Acquire firm-level customs/financial enforcement data that separate legal sanction effects from voluntary exits and war shocks after 2022.
- Locate provider/audience data measuring the causal effect of RT/Sputnik EU distribution restrictions on actual exposure and beliefs.
- For Belarus, seek authenticated decision records or negotiation traces tying specific sanction changes to specific releases or repression decisions.
- For Russia, prioritize natural experiments or threshold designs that identify sanction-induced resource constraints and downstream military/policy behavior.

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-002,QRY-005,QRY-009,QRY-010,QRY-013 | support:FCT-001,FCT-002,FCT-003,FCT-004,FCT-008,FCT-015,FCT-016,FCT-017,FCT-021 | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-008,FCT-015,FCT-016,FCT-017,FCT-021 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-016,QRY-017,QRY-018,QRY-019 | support:FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-024,FCT-025,FCT-026 | counter:- | results:FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-024,FCT-025,FCT-026 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-009,QRY-010,QRY-020 | support:FCT-015,FCT-016,FCT-017 | counter:- | results:FCT-015,FCT-016,FCT-017 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-001,QRY-002,QRY-008,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-018,QRY-019,QRY-021,QRY-022 | support:FCT-003,FCT-013,FCT-018,FCT-019,FCT-020,FCT-021,FCT-022,FCT-023,FCT-027 | counter:- | results:FCT-003,FCT-013,FCT-018,FCT-019,FCT-020,FCT-021,FCT-022,FCT-023,FCT-027 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,QRY-009,SRC-001,SRC-009 | support:FCT-001,FCT-002,FCT-015,FCT-016 | counter:CTRL-001 | results:FCT-001,FCT-002,FCT-015,FCT-016,CTRL-001 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-016,SRC-002,SRC-003,SRC-004,SRC-005,SRC-006,SRC-007,SRC-016 | support:FCT-004,FCT-006,FCT-007,FCT-008,FCT-009,FCT-012,FCT-024 | counter:CTRL-002 | results:FCT-004,FCT-006,FCT-007,FCT-008,FCT-009,FCT-012,FCT-024,CTRL-002 | final:SUPPORTED | gap:CAUSALITY
CLM-003 | attempts:QRY-002,QRY-008,QRY-018,SRC-002,SRC-008,SRC-018 | support:FCT-003,FCT-013,FCT-027 | counter:CTRL-003 | results:FCT-003,FCT-013,FCT-027,CTRL-003 | final:PARTIAL | gap:CAUSALITY
CLM-004 | attempts:QRY-009,QRY-010,SRC-009,SRC-010 | support:FCT-015,FCT-016,FCT-017 | counter:CTRL-004 | results:FCT-015,FCT-016,FCT-017,CTRL-004 | final:SUPPORTED | gap:EFFECT
CLM-005 | attempts:QRY-011,QRY-012,QRY-013,SRC-011,SRC-012,SRC-013 | support:FCT-018,FCT-019,FCT-020,FCT-021 | counter:CTRL-005 | results:FCT-018,FCT-019,FCT-020,FCT-021,CTRL-005 | final:PARTIAL | gap:CAUSALITY
CLM-006 | attempts:QRY-014,QRY-015,SRC-014,SRC-015 | support:FCT-022,FCT-023 | counter:CTRL-006 | results:FCT-022,FCT-023,CTRL-006 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-007 | attempts:QRY-006,QRY-008,QRY-016,QRY-018,SRC-006,SRC-008,SRC-016,SRC-018 | support:FCT-010,FCT-013,FCT-014,FCT-025,FCT-026,FCT-027 | counter:CTRL-007 | results:FCT-010,FCT-013,FCT-014,FCT-025,FCT-026,FCT-027,CTRL-007 | final:SUPPORTED | gap:EXTERNAL_VALIDITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-002 | CLM | SUPPORTED | CAUSALITY | Some observed changes combine legal sanctions with war shocks, voluntary firm exits, Russian countersanctions and substitution.
CLM-003 | CLM | PARTIAL | CAUSALITY | The war and sanctions continued in 2026; no credible design isolates a sanctions-only terminal policy effect.
CLM-004 | CLM | SUPPORTED | EFFECT | Audience exposure and belief change caused by the restriction are not measured here.
CLM-005 | CLM | PARTIAL | CAUSALITY | Some releases occurred while at least 863 prisoners remained and repression/new arrests continued; causal attribution to EU sanctions is absent.
CLM-006 | CLM | SUPPORTED | RESPONSIBILITY | The sequence is multilateral and negotiated; EU sanctions alone cannot be isolated as the sole cause.
CLM-007 | CLM | SUPPORTED | EXTERNAL_VALIDITY | Cross-case generalisation remains design-dependent.
CAU-004 | CAU | UNRESOLVED | CAUSALITY | Need credible political-behavior counterfactual isolating sanctions from battlefield, diplomacy and domestic factors.
CAU-006 | CAU | UNRESOLVED | CAUSALITY | Need decision-specific evidence tying sanction pressure to Belarusian release/repression decisions against rival diplomatic causes.

SEMANTIC_COUNTS_V1:LED:0|CLM:7|AXS:4|CAU:7|CTRL:8|ACT:4

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"EU sanctions are designed as targeted restrictive measures intended to change policy or conduct and are implemented through legal obligations on EU operators.","claimant":"INV-047 synthesis","counter":"CTRL-001","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-015","FCT-016"]}
CLM-002 | {"claim":"Russia-related sanctions have produced large measurable proximal economic effects in EU-Russia trade, energy dependence, asset immobilisation and targeted revenue channels.","claimant":"INV-047 synthesis","counter":"CTRL-002","gap":"Some observed changes combine legal sanctions with war shocks, voluntary firm exits, Russian countersanctions and substitution.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-004","FCT-006","FCT-007","FCT-008","FCT-009","FCT-012","FCT-024"]}
CLM-003 | {"claim":"Observed economic costs from EU sanctions can be promoted into proof that sanctions caused Russia to terminate the war or reverse the targeted policy.","claimant":"INV-047 synthesis","counter":"CTRL-003","gap":"The war and sanctions continued in 2026; no credible design isolates a sanctions-only terminal policy effect.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-003","FCT-013","FCT-027"]}
CLM-004 | {"claim":"The RT/Sputnik measures directly constrained distribution in the EU through broadcast prohibitions and licence/arrangement suspensions, subject to judicial review.","claimant":"INV-047 synthesis","counter":"CTRL-004","gap":"Audience exposure and belief change caused by the restriction are not measured here.","gap_type":"EFFECT","materiality":"HIGH","status":"SUPPORTED","support":["FCT-015","FCT-016","FCT-017"]}
CLM-005 | {"claim":"EU Belarus sanctions demonstrably caused the release of political prisoners and ended repression.","claimant":"INV-047 synthesis","counter":"CTRL-005","gap":"Some releases occurred while at least 863 prisoners remained and repression/new arrests continued; causal attribution to EU sanctions is absent.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-018","FCT-019","FCT-020","FCT-021"]}
CLM-006 | {"claim":"The JCPOA provides a documented conditionality sequence in which verified Iranian nuclear measures triggered coordinated sanctions relief.","claimant":"INV-047 synthesis","counter":"CTRL-006","gap":"The sequence is multilateral and negotiated; EU sanctions alone cannot be isolated as the sole cause.","gap_type":"RESPONSIBILITY","materiality":"HIGH","status":"SUPPORTED","support":["FCT-022","FCT-023"]}
CLM-007 | {"claim":"Sanctions effectiveness is heterogeneous: legal and economic constraints are easier to identify than downstream political behavior change, and circumvention/coordination materially affect results.","claimant":"INV-047 synthesis","counter":"CTRL-007","gap":"Cross-case generalisation remains design-dependent.","gap_type":"EXTERNAL_VALIDITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-010","FCT-013","FCT-014","FCT-025","FCT-026","FCT-027"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-005","QRY-009","QRY-010","QRY-013"],"axis":"legal_instrument_and_implementation","inv_id":"INV-047","links":["INV-047"],"question":"How do EU legal acts become enforceable restrictions through financial, commercial and media intermediaries?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-008","FCT-015","FCT-016","FCT-017","FCT-021"],"sought_objects":["Council decision/regulation","listing","asset freeze","trade ban","broadcast suspension","judicial review"],"status":"SATURATED","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-008","FCT-015","FCT-016","FCT-017","FCT-021"]}
AXS-002 | {"attempt_ids":["QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-016","QRY-017","QRY-018","QRY-019"],"axis":"economic_constraint_and_adaptation","inv_id":"INV-047","links":["INV-047"],"question":"What measurable economic constraints follow sanctions and how much is offset by adaptation or diversion?","result_ids":["FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-024","FCT-025","FCT-026"],"sought_objects":["trade reduction","energy displacement","asset immobilisation","revenue loss","trade diversion","sender cost"],"status":"SATURATED","support":["FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-024","FCT-025","FCT-026"]}
AXS-003 | {"attempt_ids":["QRY-009","QRY-010","QRY-020"],"axis":"informational_restriction","inv_id":"INV-047","links":["INV-047"],"question":"What is directly established by EU broadcasting sanctions and what downstream information effects remain unmeasured?","result_ids":["FCT-015","FCT-016","FCT-017"],"sought_objects":["broadcast ban","licence suspension","distribution","judicial proportionality","audience exposure","persuasion"],"status":"SATURATED","support":["FCT-015","FCT-016","FCT-017"]}
AXS-004 | {"attempt_ids":["QRY-001","QRY-002","QRY-008","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-018","QRY-019","QRY-021","QRY-022"],"axis":"political_behavior_and_effect","inv_id":"INV-047","links":["INV-047"],"question":"When do sanctions or sanctions relief map to target behavior, and when does attribution remain unresolved?","result_ids":["FCT-003","FCT-013","FCT-018","FCT-019","FCT-020","FCT-021","FCT-022","FCT-023","FCT-027"],"sought_objects":["war termination","repression","prisoner release","JCPOA compliance","counterfactual political change"],"status":"SATURATED","support":["FCT-003","FCT-013","FCT-018","FCT-019","FCT-020","FCT-021","FCT-022","FCT-023","FCT-027"]}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"direct compliance constraint","counter":"CTRL-001","limit":"Legal prohibition establishes constraint, not target political compliance.","mechanism":"EU legal act/listing/restriction -> obligation on EU financial, commercial or media operator -> denied transaction/access/distribution","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-015","FCT-016"]}
CAU-002 | {"causal_right":"proximal economic/trade effect","counter":"CTRL-002","limit":"War, boycotts, countersanctions and energy diversification co-determine magnitudes.","mechanism":"Russia trade/energy restrictions -> lower sanctioned bilateral trade and EU Russian-oil dependence","status":"SUPPORTED","support":["FCT-004","FCT-007","FCT-009","FCT-012","FCT-024"]}
CAU-003 | {"causal_right":"proximal financial constraint","counter":"CTRL-002","limit":"Cost is not equivalent to changed Kremlin policy.","mechanism":"asset freezes + revenue/financial restrictions -> financial cost and reduced resource access","status":"SUPPORTED","support":["FCT-006","FCT-008"]}
CAU-004 | {"counter":"CTRL-003","gap":"Need credible political-behavior counterfactual isolating sanctions from battlefield, diplomacy and domestic factors.","gap_type":"CAUSALITY","limit":"No sanctions-only counterfactual; targeted policy persisted through 2026.","mechanism":"economic cost/constraint -> Russian policy reversal or termination of war","status":"UNRESOLVED","support":["FCT-003","FCT-013","FCT-027"]}
CAU-005 | {"causal_right":"distribution constraint","counter":"CTRL-004","limit":"Does not establish audience belief or persuasion effect.","mechanism":"RT/Sputnik broadcast restriction -> lower legal distribution availability in EU","status":"SUPPORTED","support":["FCT-015","FCT-016","FCT-017"]}
CAU-006 | {"counter":"CTRL-005","gap":"Need decision-specific evidence tying sanction pressure to Belarusian release/repression decisions against rival diplomatic causes.","gap_type":"CAUSALITY","limit":"Outcome remains mixed and attribution unclosed.","mechanism":"EU Belarus sanctions -> prisoner release / end of repression","status":"UNRESOLVED","support":["FCT-018","FCT-019","FCT-020","FCT-021"]}
CAU-007 | {"causal_right":"negotiated conditional compliance sequence","counter":"CTRL-006","limit":"EU-only marginal causal contribution cannot be separated from UN/US/E3+3 bargaining.","mechanism":"multilateral sanctions pressure/relief bargain -> JCPOA commitments -> IAEA-verified nuclear measures -> sanctions relief","status":"SUPPORTED","support":["FCT-022","FCT-023"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Sanction/listing is a legal restriction, not proof of guilt beyond the legal basis or proof of later political compliance.","status":"DONE","support":["FCT-001","FCT-015","FCT-017"]}
CTRL-002 | {"control":"Trade, revenue or asset effects establish cost/constraint, not policy change.","status":"DONE","support":["FCT-006","FCT-008","FCT-009","FCT-024"]}
CTRL-003 | {"control":"War shock, voluntary boycotts, countersanctions, substitution and diversion are rival causes for observed economic changes.","status":"DONE","support":["FCT-009","FCT-010","FCT-011","FCT-025","FCT-026"]}
CTRL-004 | {"control":"Broadcast restriction is an information-distribution constraint; sanction != generic censorship and restriction != measured persuasion effect.","status":"DONE","support":["FCT-015","FCT-016","FCT-017"]}
CTRL-005 | {"control":"Belarus prisoner releases during sanctions do not identify EU sanctions as their cause while repression continues.","status":"DONE","support":["FCT-018","FCT-019","FCT-020","FCT-021"]}
CTRL-006 | {"control":"JCPOA conditionality is multilateral; verified reciprocal sequencing does not isolate an EU-only causal coefficient.","status":"DONE","support":["FCT-022","FCT-023"]}
CTRL-007 | {"control":"Implementation quality and coalition breadth are causal moderators, not background noise.","status":"DONE","support":["FCT-013","FCT-014","FCT-025","FCT-026"]}
CTRL-008 | {"control":"Absence of terminal political success is not evidence that sanctions had no effects; proximal constraint and strategic signaling are separate outcomes.","status":"DONE","support":["FCT-003","FCT-006","FCT-008","FCT-013"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Separate legal implementation, proximal economic/information constraint and terminal political behavior in every sanctions claim.","actor":"routing/control plane","intent":"prevent causal inflation","status":"DONE","support":["FCT-001","FCT-004","FCT-015","FCT-019"]}
ACT-002 | {"action":"Treat Russia trade/asset/revenue effects as supported proximal outcomes while leaving war-termination causality unresolved.","actor":"routing/control plane","intent":"effect-layer discipline","status":"DONE","support":["FCT-006","FCT-007","FCT-008","FCT-009","FCT-024"]}
ACT-003 | {"action":"Treat RT/Sputnik restrictions as direct distribution constraints, not evidence of audience persuasion or belief change.","actor":"routing/control plane","intent":"information-effect discipline","status":"DONE","support":["FCT-015","FCT-016","FCT-017"]}
ACT-004 | {"action":"Use Belarus as a negative/mixed political-effect control and JCPOA as a negotiated conditionality comparator without assigning EU-only causality.","actor":"routing/control plane","intent":"comparative causal discipline","status":"DONE","support":["FCT-018","FCT-020","FCT-022","FCT-023"]}

SEARCH_ACTIVITY_V1:WEB:4|FETCH:18|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL | mnemo | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.consilium.europa.eu/en/policies/why-sanctions/ | FETCH CONSILIUM-WHY-SANCTIONS
QRY-002 | FETCH | FOUND | SRC-002 | https://www.consilium.europa.eu/en/policies/sanctions-against-russia-explained/ | FETCH CONSILIUM-RUSSIA-QA-2026
QRY-003 | FETCH | FOUND | SRC-003 | https://www.consilium.europa.eu/fr/press/press-releases/2025/05/20/russia-s-war-of-aggression-against-ukraine-eu-agrees-17th-package-of-sanctions/ | FETCH CONSILIUM-RUSSIA-17TH
QRY-004 | FETCH | FOUND | SRC-004 | https://skribi.consilium.europa.eu/en/infographics/where-does-the-eu-get-its-oil-from/ | FETCH CONSILIUM-OIL-2026
QRY-005 | FETCH | FOUND | SRC-005 | https://commission.europa.eu/topics/eu-solidarity-ukraine/holding-russia-accountable_en | FETCH COMMISSION-FROZEN-ASSETS
QRY-006 | FETCH | FOUND | SRC-006 | https://www.ecb.europa.eu/press/blog/date/2023/html/ecb.blog.230412~1d6e657dd5.mt.html | FETCH ECB-TRADE-DIVERSION-2023
QRY-007 | FETCH | FOUND | SRC-007 | https://www.ecb.europa.eu/press/economic-bulletin/articles/2024/html/ecb.ebart202406_01~3639959dc2.en.html | FETCH ECB-EXPORTS-RUSSIA-2024
QRY-008 | FETCH | FOUND | SRC-008 | https://www.europarl.europa.eu/thinktank/en/document/EPRS_BRI(2024)760416 | FETCH EP-SANCTIONS-EFFECTIVENESS-2024
QRY-009 | FETCH | FOUND | SRC-009 | https://eur-lex.europa.eu/eli/reg/2022/350/oj/eng | FETCH EURLEX-2022-350
QRY-010 | FETCH | FOUND | SRC-010 | https://infocuria.curia.europa.eu/tabs/redirect/juris/liste.jsf?language=en&num=T-125/22 | FETCH CURIA-RTFRANCE-2022
QRY-011 | FETCH | FOUND | SRC-011 | https://www.consilium.europa.eu/fr/policies/sanctions-against-belarus/ | FETCH CONSILIUM-BELARUS-2026
QRY-012 | FETCH | FOUND | SRC-012 | https://www.eeas.europa.eu/delegations/council-europe/eu-statement-recent-release-political-prisoners-belarus_en | FETCH EEAS-BELARUS-PRISONERS-2026
QRY-013 | FETCH | FOUND | SRC-013 | https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32026R1846 | FETCH EURLEX-BELARUS-2026
QRY-014 | FETCH | FOUND | SRC-014 | https://www.consilium.europa.eu/en/policies/jcpoa-iran-restrictive-measures/ | FETCH CONSILIUM-JCPOA
QRY-015 | FETCH | FOUND | SRC-015 | https://www.eeas.europa.eu/node/3702_en | FETCH EEAS-JCPOA-2016
QRY-016 | FETCH | FOUND | SRC-016 | https://onlinelibrary.wiley.com/doi/10.1111/roie.12707 | FETCH WILEY-FLACH-2024
QRY-017 | FETCH | FOUND | SRC-017 | https://www.sciencedirect.com/science/article/pii/S0313592621000692 | FETCH SCIENCEDIRECT-RUSSIA-TRADE-2021
QRY-018 | FETCH | FOUND | SRC-018 | https://www.sciencedirect.com/science/article/pii/S0167268126001915 | FETCH JEBO-SANCTIONS-2026
QRY-019 | WEB | NON_TROUVE | - | - | EU sanctions Russia independent causal estimate sanctions alone ended war changed Kremlin policy counterfactual
QRY-020 | WEB | NON_TROUVE | - | - | EU RT Sputnik broadcasting ban measured exposure persuasion belief effect causal study
QRY-021 | WEB | NON_TROUVE | - | - | EU Belarus sanctions caused prisoner releases or ended repression causal attribution
QRY-022 | WEB | NON_TROUVE | - | - | EU sanctions Iran JCPOA EU-only marginal causal effect separate from US UN negotiation

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | CONSILIUM-WHY-SANCTIONS | Why the EU adopts sanctions | 2024-04-01 | 2026-09-10T09:15:59Z | sanctions aim policy or conduct change; unanimity and targeting | https://www.consilium.europa.eu/en/policies/why-sanctions/
SRC-002 | ◈ | fam:B | CONSILIUM-RUSSIA-QA-2026 | EU sanctions against Russia: questions and answers | 2026-09-03 | 2026-09-10T09:15:59Z | current scope, objectives and embargo values | https://www.consilium.europa.eu/en/policies/sanctions-against-russia-explained/
SRC-003 | ◈ | fam:B | CONSILIUM-RUSSIA-17TH | EU 17th package sanctions Russia | 2025-05-20 | 2026-09-10T09:15:59Z | shadow fleet and oil revenue figures | https://www.consilium.europa.eu/fr/press/press-releases/2025/05/20/russia-s-war-of-aggression-against-ukraine-eu-agrees-17th-package-of-sanctions/
SRC-004 | ◈ | fam:B | CONSILIUM-OIL-2026 | Where does the EU get its oil from | 2026-05-01 | 2026-09-10T09:15:59Z | Russian oil import share and tonnes 2021-2025 | https://skribi.consilium.europa.eu/en/infographics/where-does-the-eu-get-its-oil-from/
SRC-005 | ◈ | fam:B | COMMISSION-FROZEN-ASSETS | Holding Russia accountable | 2026-08-21 | 2026-09-10T09:15:59Z | over EUR210bn Russian central-bank assets immobilised in EU | https://commission.europa.eu/topics/eu-solidarity-ukraine/holding-russia-accountable_en
SRC-006 | ◈ | fam:C | ECB-TRADE-DIVERSION-2023 | International trade diversion after war sanctions boycotts | 2023-04-12 | 2026-09-10T09:15:59Z | bilateral trade plunge, diversion and substitution | https://www.ecb.europa.eu/press/blog/date/2023/html/ecb.blog.230412~1d6e657dd5.mt.html
SRC-007 | ◈ | fam:C | ECB-EXPORTS-RUSSIA-2024 | External competitiveness of euro area | 2024-09-01 | 2026-09-10T09:15:59Z | euro area exports to Russia halved within months | https://www.ecb.europa.eu/press/economic-bulletin/articles/2024/html/ecb.ebart202406_01~3639959dc2.en.html
SRC-008 | ◈ | fam:C | EP-SANCTIONS-EFFECTIVENESS-2024 | EU sanctions: key foreign and security policy instrument | 2024-07-01 | 2026-09-10T09:15:59Z | effectiveness measurement and implementation limits | https://www.europarl.europa.eu/thinktank/en/document/EPRS_BRI(2024)760416
SRC-009 | ◈ | fam:A | EURLEX-2022-350 | Regulation EU 2022/350 RT Sputnik broadcasting | 2022-03-01 | 2026-09-10T09:15:59Z | broadcast prohibition and licence suspension | https://eur-lex.europa.eu/eli/reg/2022/350/oj/eng
SRC-010 | ◈ | fam:A | CURIA-RTFRANCE-2022 | RT France v Council T-125/22 | 2022-07-27 | 2026-09-10T09:15:59Z | General Court judgment upholding broadcast restriction | https://infocuria.curia.europa.eu/tabs/redirect/juris/liste.jsf?language=en&num=T-125/22
SRC-011 | ◈ | fam:B | CONSILIUM-BELARUS-2026 | EU sanctions against Belarus | 2026-08-01 | 2026-09-10T09:15:59Z | 310 persons 46 entities; objective and extension to Feb 2027 | https://www.consilium.europa.eu/fr/policies/sanctions-against-belarus/
SRC-012 | ◈ | fam:B | EEAS-BELARUS-PRISONERS-2026 | EU statement political prisoners Belarus | 2026-07-08 | 2026-09-10T09:15:59Z | 28 released but at least 863 remain and repression continues | https://www.eeas.europa.eu/delegations/council-europe/eu-statement-recent-release-political-prisoners-belarus_en
SRC-013 | ◈ | fam:A | EURLEX-BELARUS-2026 | Council Regulation EU 2026/1846 Belarus | 2026-07-23 | 2026-09-10T09:15:59Z | current Belarus restrictive-measures amendment in force | https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32026R1846
SRC-014 | ◈ | fam:B | CONSILIUM-JCPOA | Iran nuclear agreement and EU sanctions | 2026-08-01 | 2026-09-10T09:15:59Z | Implementation Day conditional sanctions lifting | https://www.consilium.europa.eu/en/policies/jcpoa-iran-restrictive-measures/
SRC-015 | ◈ | fam:A | EEAS-JCPOA-2016 | JCPOA Implementation Day reached | 2016-01-16 | 2026-09-10T09:15:59Z | IAEA verified commitments and sanctions relief followed | https://www.eeas.europa.eu/node/3702_en
SRC-016 | ◈ | fam:D | WILEY-FLACH-2024 | Quantifying sanctions effects on Russia | 2023-09-22 | 2026-09-10T09:15:59Z | gravity and general-equilibrium estimates 2014-2019 | https://onlinelibrary.wiley.com/doi/10.1111/roie.12707
SRC-017 | ◈ | fam:D | SCIENCEDIRECT-RUSSIA-TRADE-2021 | Impact of sanctions and counter-sanctions on Russian trade | 2021-10-01 | 2026-09-10T09:15:59Z | counterfactual gravity analysis of targeted trade | https://www.sciencedirect.com/science/article/pii/S0313592621000692
SRC-018 | ◈ | fam:D | JEBO-SANCTIONS-2026 | Sanctions without sanctimony | 2026-08-01 | 2026-09-10T09:15:59Z | broad empirical null/negative effects against stated goals | https://www.sciencedirect.com/science/article/pii/S0167268126001915

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.consilium.europa.eu/en/policies/why-sanctions/ | A | 2026 | formal objective | The Council states EU sanctions are targeted foreign-policy measures intended to bring about a change in policy or conduct, not punishment as such. | -
FCT-002 | FACT | ✧ | https://www.consilium.europa.eu/en/policies/why-sanctions/ | A | 2026 | decision rule | Autonomous EU sanctions are adopted by the Council by unanimity, making the legal act a collective political decision rather than an administrative platform action. | -
FCT-003 | FACT | ✧ | https://www.consilium.europa.eu/en/policies/sanctions-against-russia-explained/ | B | 2026 | Russia policy objective | The Council describes the objective of Russia sanctions as ending the war of aggression by maximising pressure and diminishing Russia ability to wage war. | -
FCT-004 | FACT | ✧ | https://www.consilium.europa.eu/en/policies/sanctions-against-russia-explained/ | B | 2026 | trade embargo scale | The Council reports EU bans covering goods and technology worth more than EUR48bn of exports and EUR91.2bn of imports relative to 2021 volumes, about 54% and 58% respectively. | -
FCT-005 | FACT | ✧ | https://www.consilium.europa.eu/fr/press/press-releases/2025/05/20/russia-s-war-of-aggression-against-ukraine-eu-agrees-17th-package-of-sanctions/ | B | 2025-05-20 | shadow fleet enforcement | The 17th package added 189 shadow-fleet vessels, bringing the designated vessel total to 342 at that date, with port-access and service restrictions. | -
FCT-006 | FACT | ✧ | https://www.consilium.europa.eu/fr/press/press-releases/2025/05/20/russia-s-war-of-aggression-against-ukraine-eu-agrees-17th-package-of-sanctions/ | B | 2025-05-20 | oil revenue proxy | The Council reported targeted Russian revenues had fallen by EUR38bn since introduction of the oil price cap and shadow-fleet sanctions; March 2025 revenues were 20.3% below March 2022. | -
FCT-007 | FACT | ✧ | https://skribi.consilium.europa.eu/en/infographics/where-does-the-eu-get-its-oil-from/ | B | 2021-2025 | oil import displacement | Russia share of EU oil imports fell from 25.8% in 2021 to 2.2% in 2025; volumes fell from 114.4 Mt to 9.7 Mt. | -
FCT-008 | FACT | ✧ | https://commission.europa.eu/topics/eu-solidarity-ukraine/holding-russia-accountable_en | B | 2026 | asset immobilisation | More than EUR210bn of Central Bank of Russia assets are immobilised in the EU, a direct financial constraint distinct from evidence of policy change. | -
FCT-009 | FACT | ✧ | https://www.ecb.europa.eu/press/blog/date/2023/html/ecb.blog.230412~1d6e657dd5.mt.html | C | 2022-2023 | bilateral trade collapse | ECB analysis reports euro-area/Russia trade at roughly half pre-war levels by 2023, with sanctioned export categories remaining low. | -
FCT-010 | FACT | ✧ | https://www.ecb.europa.eu/press/blog/date/2023/html/ecb.blog.230412~1d6e657dd5.mt.html | C | 2022-2023 | trade diversion | ECB notes Russia redirected trade toward non-sanctioning partners and had to offer discounts on commodity exports; circumvention and substitution reduce coercive closure. | -
FCT-011 | FACT | ✧ | https://www.ecb.europa.eu/press/blog/date/2023/html/ecb.blog.230412~1d6e657dd5.mt.html | C | 2023 | EU adaptation | The EU also diverted energy trade away from Russia toward Norway, Algeria, Azerbaijan and LNG suppliers, showing sender-side adaptation and cost. | -
FCT-012 | FACT | ✧ | https://www.ecb.europa.eu/press/economic-bulletin/articles/2024/html/ecb.ebart202406_01~3639959dc2.en.html | C | 2022-2024 | exports to Russia | ECB reports euro-area exports to Russia halved within months after invasion and sanctions and continued to decline. | -
FCT-013 | FACT | ✧ | https://www.europarl.europa.eu/thinktank/en/document/EPRS_BRI(2024)760416 | C | 2024 | effectiveness measurement | European Parliament research service states sanctions effectiveness is difficult to measure because sanctions rarely achieve all aims alone and changes have multiple causes. | -
FCT-014 | FACT | ✧ | https://www.europarl.europa.eu/thinktank/en/document/EPRS_BRI(2024)760416 | C | 2024 | implementation weakness | The same briefing identifies inconsistent implementation and coordination across stakeholders as factors that can undermine sanctions effectiveness. | -
FCT-015 | FACT | ✧ | https://eur-lex.europa.eu/eli/reg/2022/350/oj/eng | A | 2022-03-01 | broadcast prohibition | Regulation 2022/350 prohibited operators from broadcasting or facilitating content from listed RT/Sputnik entities across cable, satellite, IPTV, internet providers, video-sharing platforms and apps. | -
FCT-016 | FACT | ✧ | https://eur-lex.europa.eu/eli/reg/2022/350/oj/eng | A | 2022-03-01 | licence suspension | The Regulation required suspension of broadcasting licences, authorisations, transmission and distribution arrangements for listed entities. | -
FCT-017 | FACT | ✧ | https://infocuria.curia.europa.eu/tabs/redirect/juris/liste.jsf?language=en&num=T-125/22 | A | 2022-07-27 | judicial control | The General Court rejected RT France request to annul the Council measures; the case expressly examined Council powers, rights of defence, freedom of expression, proportionality and business freedom. | -
FCT-018 | FACT | ✧ | https://www.consilium.europa.eu/fr/policies/sanctions-against-belarus/ | B | 2026 | Belarus scope | Current Council material reports 310 persons and 46 entities sanctioned under the Belarus regime and extension of relevant measures until 28 February 2027. | -
FCT-019 | FACT | ✧ | https://www.consilium.europa.eu/fr/policies/sanctions-against-belarus/ | B | 2026 | Belarus stated objective | The stated objective is to pressure Belarusian leadership to prevent repression, release political prisoners and begin inclusive national dialogue. | -
FCT-020 | FACT | ✧ | https://www.eeas.europa.eu/delegations/council-europe/eu-statement-recent-release-political-prisoners-belarus_en | B | 2026-07-08 | Belarus negative outcome control | The EU welcomed release of 28 political prisoners but reported at least 863 still detained, new arrests/re-arrests and continuing repression. | -
FCT-021 | FACT | ✧ | https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32026R1846 | A | 2026-07-23 | Belarus legal persistence | Council Regulation 2026/1846 amended the Belarus restrictive-measures framework and remained in force, confirming continued legal coercion rather than completed policy reversal. | -
FCT-022 | FACT | ✧ | https://www.consilium.europa.eu/en/policies/jcpoa-iran-restrictive-measures/ | B | 2016-01-16 | JCPOA conditionality | On Implementation Day, after IAEA verification of Iran nuclear-related measures, the EU lifted all nuclear-related economic and financial sanctions. | -
FCT-023 | FACT | ✧ | https://www.eeas.europa.eu/node/3702_en | A | 2016-01-16 | verified reciprocal sequence | EEAS described IAEA-verified Iranian implementation and simultaneous UN/EU/US sanctions relief as the agreed reciprocal sequence under the JCPOA. | -
FCT-024 | FACT | ✧ | https://onlinelibrary.wiley.com/doi/10.1111/roie.12707 | D | 2014-2019 | estimated Russia trade effect | Flach et al. estimate 2014 sanctions reduced Russian real income by about 0.3%; EU manufacturing exports to Russia fell about 12%, while Russian countersanctions cut agricultural imports from G7plus by about 70%. | -
FCT-025 | FACT | ✧ | https://onlinelibrary.wiley.com/doi/10.1111/roie.12707 | D | 2014-2019 | coordination and substitution | The study finds coordinated sanctions impose a larger burden than EU-only sanctions, while Russia can redirect exports to third countries and substitute imports only partially. | -
FCT-026 | FACT | ✧ | https://onlinelibrary.wiley.com/doi/10.1111/roie.12707 | D | 2014-2019 | imperfect enforcement | The study finds codified restrictions explain much of observed effects but differences are consistent with imperfect enforcement, substitution or relabelling. | -
FCT-027 | FACT | ✧ | https://www.sciencedirect.com/science/article/pii/S0167268126001915 | D | 2026 | broad political-effect benchmark | A 2026 cross-case study reports null or negative effects across tested outcomes relative to stated sanction goals; this is a broad benchmark, not a case-specific EU verdict. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-002
FCT-004 | SRC-002
FCT-005 | SRC-003
FCT-006 | SRC-003
FCT-007 | SRC-004
FCT-008 | SRC-005
FCT-009 | SRC-006
FCT-010 | SRC-006
FCT-011 | SRC-006
FCT-012 | SRC-007
FCT-013 | SRC-008
FCT-014 | SRC-008
FCT-015 | SRC-009
FCT-016 | SRC-009
FCT-017 | SRC-010
FCT-018 | SRC-011
FCT-019 | SRC-011
FCT-020 | SRC-012
FCT-021 | SRC-013
FCT-022 | SRC-014
FCT-023 | SRC-015
FCT-024 | SRC-016
FCT-025 | SRC-016
FCT-026 | SRC-016
FCT-027 | SRC-018

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

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:search
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:facts
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:causal
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:verify
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:accountability
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:finalize

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-10T09:21:15.744771+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":27,"eligible":27,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:27;attempted:0;success:0;failure:0;blocked:27} | WRITEBACK_EXECUTION_V1:[27 rows, see section]

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
