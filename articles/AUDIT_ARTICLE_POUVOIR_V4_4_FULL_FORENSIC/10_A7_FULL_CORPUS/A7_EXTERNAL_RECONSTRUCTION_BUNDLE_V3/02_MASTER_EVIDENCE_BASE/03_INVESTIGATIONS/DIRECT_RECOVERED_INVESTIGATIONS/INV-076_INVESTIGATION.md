ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260910-0806-press-public-subsidies-pluralism | PARENT_RUN_ID:NONE | AS_OF:2026-09-10
INPUT_KIND:RUN_CARD | MISSION_MODE:RECHECK_EXTEND | INPUT_REF:PATH:/mnt/data/inv076/runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-10_press-public-subsidies-pluralism/2026-09-10_08-06_press-public-subsidies-pluralism_INPUT.md | SUBJECT_SLUG:press-public-subsidies-pluralism | SUBJECT_FP:sha256:9634b1632260640150e16513e55a4a9dfaaac11e9feafc063f2b814149f53bb8 | INPUT_SHA256:sha256:2e0ea42f47740ac06e380e62b50c2856d0fe5b5114d32e11dfc968e76d719b30
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France, mainly 2017-2026; trace press-support scheme/budget -> eligibility/formula -> beneficiary -> economic weight -> possible incentive/pressure -> editorial or market outcome -> pluralism.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/NETWORK.md,clusters/INFORMATION.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Analytic body

## Object

INV-076 tests French public support to the press as a chain: scheme/budget -> eligibility/formula -> award -> economic exposure -> possible leverage -> editorial/content or market effect -> pluralism. The run does not collapse subsidy into control, dependence into compliance, or a pluralism objective into a measured pluralism effect.

## Scale and architecture

The 2024 execution data establish a large, multi-channel architecture. The Ministry reports 175.2 million euros of direct aid, split into 23.4 million for pluralism, 130.1 million for transport/distribution and 21.7 million for modernization [FCT-001]. It also reports about 300 million euros of indirect support through the reduced VAT rate and postal tariff advantage [FCT-002]. In total, 527 titles received press aid in 2024 [FCT-003].

The system is not one discretionary grant. The Ministry separates aid categories [FCT-022], while the inspected decree uses IPG status, periodicity, price/circulation and low-advertising-resource thresholds, including an aid cap relative to prior-year revenue excluding subsidies [FCT-016, FCT-017, FCT-018]. Regional/local pluralism and national distribution schemes also use circulation/cost formulas [FCT-021, FCT-027]. The strongest generic administrative edge is therefore `status/economic criteria -> eligibility/formula -> aid amount`, not `political agreement -> subsidy`.

## Economic dependence and concentration

Public support is economically material. A Senate report places direct aid, excluding tax expenditure, above 20% of IPG press turnover in the cited period [FCT-009]. The 2021 Senate review similarly reported aid representing 21.4% of sector turnover before exceptional recovery-plan schemes [FCT-014]. Recipient tables show strong concentration among a limited set of titles receiving multi-million-euro amounts [FCT-010, FCT-012].

These facts justify treating dependence as a structural risk variable. They do not by themselves identify who controls editorial decisions. The Senate itself frames excessive dependence as a possible threat to independence [FCT-015], while article 2 bis of the 1881 press law gives journalists a right to refuse pressure and acts contrary to professional conviction [FCT-019]. That legal counter-control does not prove perfect enforcement; it prevents converting financial exposure into an automatic command chain.

## Pluralism rationale and coverage

Pluralism is an explicit policy objective. The Ministry states that aid to low-advertising-resource publications is intended to prevent advertising pressure from determining the ideas expressed [FCT-008]. In 2024, 375 titles shared 23.4 million euros of pluralism aid [FCT-004]; four national low-advertising-resource dailies shared 10.35 million [FCT-005], and 69 online titles received 4 million euros [FCT-006]. The Constitutional Council recognizes pluralism and independence of IPG dailies as constitutional-value objectives [FCT-020].

This establishes purpose, coverage and a plausible capacity-preservation mechanism. It does not identify the counterfactual number of titles or viewpoints that would disappear without aid. Government statements about sustaining local press and access remain policy rationale rather than causal estimates [FCT-023].

## Editorial-control test

The decisive stronger hypothesis is `aid dependence -> state leverage -> editorial instruction -> compliance`. The inspected allocation predicates are primarily formal/economic rather than agreement with a government editorial position [FCT-016, FCT-018]. The run also searched explicitly for authenticated subsidy-linked instructions, threats or quid-pro-quo exchanges and did not locate sufficient evidence. That negative search is not proof that informal pressure never occurs. It means the generic control edge remains unresolved without a named instruction, decision right, threat or compliance trace.

Concentration of public support therefore remains a relevant exposure/dependence indicator, not evidence of ideological favoritism or editorial capture.

## Causal ceiling on content and pluralism

Cross-year budget and beneficiary changes are observable [FCT-024, FCT-025, FCT-026], but they are not causal designs. The run did not identify a discontinuity, withdrawal shock, matched comparison or other credible design linking aid variation to a change in editorial line, political coverage, title survival or aggregate pluralism.

The supported causal registry therefore stops at rule/formula -> aid and, for distribution support, eligible-cost offset [CAU-001, CAU-002]. `Pluralism aid -> title/viewpoint preservation`, `dependence -> editorial compliance`, `aid change -> content change` and `support architecture -> overall pluralism` remain unresolved [CAU-003, CAU-004, CAU-005, CAU-006].

## Result

INV-076 closes the generic allocation and materiality mechanism: French press support is large, multi-channel, concentrated, economically material and substantially rule/formula based. Economic dependence is a legitimate structural independence risk, and pluralism is an explicit institutional objective. The inspected evidence does not establish generic state editorial tasking/control, a subsidy-linked quid pro quo, or a quantified marginal causal effect on editorial line, title survival or pluralism. High-value reopening requires either a title-specific authenticated pressure/control chain or a credible aid-shock/threshold design with content, survival or pluralism outcomes.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:6|SRC_COMPLETE:16/16

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-10
- **breaks:**
  - 2021 Senate dependence/reform review
  - 2022-2024 online/local pluralism expansion
  - 2023 distribution reform
  - 2024 execution data
  - 2025 continuing reform debate
- **status:** CURRENT_FOR_2024_EXECUTION_AND_CURRENT_RULES; BUDGET_PLANS_SEPARATE
- **window:** 2017-2026

### MANIPULATION_REPORT
- **assumptions:**
  - official execution data reliable for paid amounts
  - parliamentary ratios bounded to cited periods
  - formal independence rights do not prove perfect enforcement
- **clusters:**
  - POWER
  - NETWORK
  - INFORMATION
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - state aid can create leverage without proving use
  - market-pressure relief can preserve capacity without proving counterfactual survival
  - pluralism is both policy objective and empirical outcome
- **input_kind:** RUN_CARD
- **mission_mode:** RECHECK_EXTEND
- **patterns:**
  - rule-based subsidy
  - economic dependence
  - aid concentration
  - pluralism rationale
  - distribution cost offset
  - reform debate
- **priorities:**
  - map rules and payments
  - quantify dependence/concentration
  - seek quid-pro-quo/tasking
  - seek causal aid shock
  - separate title survival from pluralism
- **query_guidance:** prefer Ministry execution tables, statutes/decrees, parliamentary control reports and independence law; require authenticated pressure for control and counterfactual for effect
- **rhetorical:**
  - **AUTH:** official execution + law + parliamentary scrutiny
  - **BF:** no generic capture estimate
  - **DEM:** retain counter-controls
  - **FAC:** separate rule mechanics from interpretation
  - **NUM:** year-bounded amounts and counts
- **speaker:**
  - **goal:** forensic separation of subsidy, dependence, editorial leverage and pluralism effect
  - **target:** scheme -> aid -> dependence -> pressure/content -> pluralism
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** state aid
  - **S02:** scheme
  - **S03:** eligibility
  - **S04:** formula
  - **S05:** beneficiary
  - **S06:** revenue
  - **S07:** dependence
  - **S08:** leverage
  - **S09:** pressure
  - **S10:** editorial decision
  - **S11:** content
  - **S12:** distribution
  - **S13:** survival
  - **S14:** market structure
  - **S15:** pluralism
- **threats:**
  - subsidy=control
  - dependence=editorial compliance
  - recipient=government ally
  - pluralism objective=effect
  - budget=execution
  - concentration=favoritism

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - cross-year comparable denominator
  - **input_ids:**
    - FCT-001
    - FCT-002
    - FCT-003
    - FCT-016
    - FCT-017
    - FCT-018
    - FCT-021
    - FCT-022
    - FCT-027
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - eligibility not converted to viewpoint approval
    - budget authorization not converted to execution
  - **not_computable:**
    - harmonized all-in support denominator across years
  - **operations_applied:**
    - mapped aid scheme categories
    - reconstructed eligibility/formula pathways
    - separated direct and indirect resource flows
  - **reason:** separate institutional allocation pathways, beneficiary coverage and formulaic resource flows
  - **result_ids:**
    - CLM-001
    - CLM-003
    - CAU-001
    - CAU-002
  - **status:** DONE
  - **trigger:** aid scheme/administration/beneficiary network
- **item 2:**
  - **gaps:**
    - title-level denominator
    - named instruction/control/compliance trace
  - **input_ids:**
    - FCT-009
    - FCT-010
    - FCT-012
    - FCT-014
    - FCT-015
    - FCT-016
    - FCT-018
    - FCT-019
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no authenticated subsidy-linked instruction, threat or quid-pro-quo located
  - **not_computable:**
    - prevalence of informal pressure
    - current aid/revenue ratio for every beneficiary
  - **operations_applied:**
    - bounded sector dependence ratios
    - separated concentration from favoritism
    - tested leverage-to-tasking edge
    - retained legal independence counter-control
  - **reason:** test whether material public funding creates decision rights, pressure, tasking or compliance
  - **result_ids:**
    - CLM-002
    - CLM-005
    - CAU-004
  - **status:** DONE
  - **trigger:** economic dependence, leverage and possible editorial control
- **item 3:**
  - **gaps:**
    - aid-shock or eligibility-threshold causal design
  - **input_ids:**
    - FCT-003
    - FCT-004
    - FCT-006
    - FCT-008
    - FCT-020
    - FCT-023
    - FCT-024
    - FCT-025
    - FCT-026
  - **module:** clusters/INFORMATION.md
  - **negative_results:**
    - recipient counts not converted to pluralism effect
    - budget and beneficiary variation not treated as causal design
  - **not_computable:**
    - marginal content effect
    - counterfactual titles/viewpoints preserved
  - **operations_applied:**
    - separated policy objective from measured outcome
    - tested aid-change to content edge
    - tested survival/pluralism counterfactual
    - ran explicit negative causal-design searches
  - **reason:** separate pluralism rationale and distribution exposure from causal editorial or market effects
  - **result_ids:**
    - CLM-004
    - CLM-006
    - CAU-003
    - CAU-005
    - CAU-006
  - **status:** DONE
  - **trigger:** editorial content, survival and pluralism outcomes

### SCOPING_REPORT
- **exclusions:**
  - public-service audiovisual financing
  - generic ownership concentration except as context
  - assuming editorial capture from subsidy receipt
- **geo:** France
- **object_coverage:** HIGH_FOR_RULES_AMOUNTS_AND_CONCENTRATION; MODERATE_FOR_TITLE_DEPENDENCE; LOW_FOR_EDITORIAL_OR_PLURALISM_CAUSAL_EFFECT
- **object_question:** How are aid schemes allocated, how economically material are they, and what evidence links aid dependence to editorial or pluralism effects?
- **period:** mainly 2017-2026
- **subject:** French public support to press, economic dependence and possible effects on editorial independence/pluralism

### CREDO
- subsidy != control
- eligibility != tasking
- dependence != editorial effect
- coverage != quid pro quo
- pluralism objective != causal effect
- budget != execution
- concentration != favoritism
- absence of evidence != evidence of absence

### COGNITIVE_MAP
- **continuum:**
  - pluralism objective
  - aid scheme/budget
  - eligibility/status
  - formula/award
  - beneficiary
  - aid/revenue exposure
  - leverage
  - editorial decision
  - content
  - survival/market structure
  - pluralism outcome
- **core_model:** French press aid is a large, multi-channel and economically material support system whose allocation is mostly rule/formula based. It is concentrated for some titles and can create dependence risk. The inspected record does not close subsidy/dependence -> state editorial command, content change or marginal pluralism effect.
- **rival_models:**
  - public subsidy automatically controls editorial line
  - objective formulas eliminate all independence risk
  - aid concentration proves ideological favoritism
  - recipient diversity proves neutrality of every decision
  - pluralism objective proves causal effect

### DIALECTICAL_MAP
- **antithesis:** Inspected allocation rules are mainly status/economic/circulation formulas and journalist law preserves editorial refusal rights; funding does not establish instruction or compliance.
- **synthesis:** The generic mechanism closes at rule/formula -> aid -> economic exposure. Editorial control requires a named pressure/tasking chain, and pluralism effect requires a counterfactual design.
- **thesis:** French press support is large, multi-channel, concentrated and economically material, creating a plausible dependence/leverage variable.
- **unresolved:**
  - title-specific subsidy-linked instruction/threat/quid-pro-quo
  - marginal content effect of aid changes
  - counterfactual title survival and pluralism effect

### RESOURCE_FLOW_MAP
- **flows:**
  - state budget/tax-postal support -> aid scheme
  - eligibility/formula -> award -> press title
  - distribution aid -> eligible transport/distribution costs
  - pluralism aid -> low-ad-revenue/local/online press capacity
  - aid exposure -> possible economic dependence/leverage
- **limits:**
  - no authenticated state instruction -> editor flow established
  - no aid change -> editorial content causal flow established
  - no aid -> pluralism counterfactual effect quantified

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** Ministry/DGMIC and statutory aid schemes
  - **relation:** administer eligibility/formula and payments
  - **support:**
    - FCT-001
    - FCT-016
    - FCT-017
    - FCT-021
    - FCT-027
  - **to:** eligible press titles/distributors
- **item 2:**
  - **from:** Parliament/budget law
  - **relation:** authorizes envelopes and scrutinizes concentration/reform
  - **support:**
    - FCT-009
    - FCT-010
    - FCT-012
    - FCT-014
    - FCT-024
    - FCT-025
  - **to:** press-support architecture
- **item 3:**
  - **from:** press title/company
  - **relation:** receives aid while retaining editorial organization and journalist rights
  - **support:**
    - FCT-019
  - **to:** journalists/editorial decisions
- **item 4:**
  - **from:** advertising/distribution markets
  - **relation:** create revenue/cost pressures targeted by aid schemes
  - **support:**
    - FCT-007
    - FCT-008
    - FCT-016
    - FCT-020
    - FCT-023
  - **to:** press economics

### IMPACT_MAP
- **established:**
  - large multi-channel public support architecture
  - formula/status-based eligibility pathways
  - broad recipient coverage
  - sector-level economic materiality above 20% in cited Senate periods
  - concentration among multi-million-euro beneficiaries
  - explicit pluralism policy rationale
- **not_established:**
  - generic subsidy-linked editorial tasking/control
  - quid-pro-quo for favorable coverage
  - marginal aid effect on editorial line
  - marginal aid effect on title survival or overall pluralism
- **partial:**
  - dependence as structural independence risk
  - market-pressure relief as plausible preservation mechanism

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** Allocation rules are economic/formula based and journalist law preserves a right to refuse pressure.
  - **issue:** dependence versus control
  - **pro:** Aid is economically material and concentrated.
  - **resolution:** DEPENDENCE_RISK_SUPPORTED; GENERIC_EDITORIAL_CONTROL_NOT_ESTABLISHED
  - **support:**
    - FCT-009
    - FCT-010
    - FCT-014
    - FCT-016
    - FCT-019
- **item 2:**
  - **contra:** Recipient counts and purpose do not measure the counterfactual market/pluralism outcome.
  - **issue:** policy objective versus causal effect
  - **pro:** Pluralism aid is explicitly intended to preserve diverse viewpoints and local access.
  - **resolution:** PLURALISM_PURPOSE_SUPPORTED; MARGINAL_EFFECT_UNRESOLVED
  - **support:**
    - FCT-003
    - FCT-004
    - FCT-006
    - FCT-008
    - FCT-020
    - FCT-023
- **item 3:**
  - **contra:** Beneficiaries span multiple editorial positions and scheme types.
  - **issue:** concentration versus favoritism
  - **pro:** Large titles receive multi-million-euro support.
  - **resolution:** CONCENTRATION_SUPPORTED; IDEOLOGICAL_ALLOCATION_BIAS_NOT_ESTABLISHED
  - **support:**
    - FCT-005
    - FCT-010
    - FCT-012
    - FCT-016
    - FCT-021

### VERIFICATION_REPORT
- **downgraded:**
  - public aid generically controls editorial line
  - aid concentration proves ideological favoritism
  - economic dependence proves compliance
  - pluralism aid quantitatively preserves viewpoints
  - aid variation causes editorial content change
- **fact_count:** 27
- **negative_controls:**
  - subsidy separated from control
  - eligibility separated from tasking
  - dependence separated from editorial effect
  - favorable coverage separated from quid pro quo
  - pluralism objective separated from causal effect
  - budget authorization separated from execution
  - concentration separated from favoritism
  - absence search not converted to nonexistence
- **provenance_families:** 5
- **query_count:** 19
- **source_count:** 16
- **verification:** 27 bounded facts linked to 16 accepted source records and 19 requests across Ministry execution/rules, parliamentary scrutiny, legal/constitutional controls and public-policy materials, including three explicit negative WEB searches.

### EDI_REPORT
- **corpus:**
  - **limits:**
    - no current title-level aid/revenue denominator for all beneficiaries
    - no authenticated subsidy-linked editorial instruction located
    - no quasi-experimental aid-shock/content or survival design located
  - **strength:** official Ministry execution tables and aid rules, statutes/decrees, Constitutional Council and parliamentary scrutiny reports
- **decisive_claim_coverage:**
  - CLM-001
  - CLM-002
  - CLM-003
  - CLM-004
  - CLM-005
  - CLM-006
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** Ministry/DGMIC + Parliament + statutory/legal controls + beneficiaries
  - **perspective:** allocation, economic dependence, editorial independence/control, pluralism effect
  - **stratification:** scheme -> eligibility/formula -> award -> economic exposure -> possible leverage -> content/market -> pluralism
  - **temporal:** 2017-2026 with detailed 2021, 2023 and 2024 observations
- **edi:**
  - **coverage:** HIGH_FOR_ALLOCATION_AND_DEPENDENCE; MODERATE_FOR_INDEPENDENCE_RISK; LOW_FOR_EDITORIAL_AND_PLURALISM_CAUSAL_EFFECT
  - **independence:** STRONG_FOR_FORMAL_RULES_AND_EXECUTION; MODERATE_FOR_POLICY_RISK_INTERPRETATION
- **source_counts:**
  - **A:** 6
  - **B:** 6
  - **C:** 2
  - **D:** 1
  - **E:** 1
  - **total:** 16

### RESPONSIBILITY_MAP
- **aid_scheme_and_rules:** legislator/government/Ministry-DGMIC depending instrument
- **causal_editorial_or_pluralism_claim:** requires independent title-level pressure evidence or counterfactual empirical design
- **economic_dependency_measure:** requires beneficiary revenue denominator plus aid amounts
- **editorial_choice:** publication/editorial chain; journalist independence rights remain relevant
- **eligibility_and_payment:** competent public administration under scheme rules
- **pluralism_policy_objective:** public authority/constitutional framework

### NEXT_QUERIES
- Named title: authenticated correspondence linking public aid grant, threat or withdrawal to a specific editorial request or compliance act.
- Title-level panel: aid/revenue ratios over time matched to ownership, survival and coded political/editorial content.
- Quasi-experimental discontinuity: eligibility threshold or rule change producing exogenous aid variation with comparator titles.
- Pluralism outcome: consistent market/viewpoint diversity metric before and after identifiable aid shocks.

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-002,QRY-007,QRY-010,QRY-011,QRY-013,QRY-014,QRY-015,QRY-016 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-016,FCT-017,FCT-018,FCT-021,FCT-022,FCT-024,FCT-025,FCT-026,FCT-027 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-003,QRY-004,QRY-005,QRY-006 | support:- | counter:- | results:FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-007,QRY-008,QRY-017 | support:- | counter:- | results:FCT-013,FCT-015,FCT-016,FCT-017,FCT-018,FCT-019 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-001,QRY-002,QRY-009,QRY-012,QRY-018,QRY-019 | support:- | counter:- | results:FCT-003,FCT-004,FCT-006,FCT-008,FCT-020,FCT-023,FCT-026 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,QRY-007,QRY-010,QRY-011,QRY-016,SRC-001,SRC-007,SRC-010,SRC-011,SRC-016 | support:FCT-001,FCT-002,FCT-007,FCT-016,FCT-017,FCT-021,FCT-022,FCT-027 | counter:- | results:FCT-001,FCT-002,FCT-007,FCT-016,FCT-017,FCT-021,FCT-022,FCT-027 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-003,QRY-004,QRY-005,SRC-003,SRC-004,SRC-005 | support:FCT-009,FCT-010,FCT-011,FCT-012,FCT-014 | counter:- | results:FCT-009,FCT-010,FCT-011,FCT-012,FCT-014 | final:SUPPORTED | gap:TITLE_DENOMINATOR
CLM-003 | attempts:QRY-007,QRY-010,QRY-016,SRC-007,SRC-010,SRC-016 | support:FCT-016,FCT-017,FCT-018,FCT-021,FCT-027 | counter:- | results:FCT-016,FCT-017,FCT-018,FCT-021,FCT-027 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-001,QRY-002,QRY-009,QRY-012,SRC-001,SRC-002,SRC-009,SRC-012 | support:FCT-003,FCT-004,FCT-006,FCT-008,FCT-020,FCT-023 | counter:- | results:FCT-003,FCT-004,FCT-006,FCT-008,FCT-020,FCT-023 | final:PARTIAL | gap:CAUSAL_ATTRIBUTION
CLM-005 | attempts:QRY-003,QRY-005,QRY-006,QRY-007,QRY-008,SRC-003,SRC-005,SRC-006,SRC-007,SRC-008 | support:FCT-009,FCT-014,FCT-015,FCT-019 | counter:FCT-016,FCT-018,FCT-019 | results:FCT-009,FCT-014,FCT-015,FCT-019,FCT-016,FCT-018,FCT-019 | final:PARTIAL | gap:TASKING
CLM-006 | attempts:QRY-001,QRY-005,QRY-012,SRC-001,SRC-005,SRC-012 | support:FCT-003,FCT-014,FCT-023 | counter:- | results:FCT-003,FCT-014,FCT-023 | final:PARTIAL | gap:CAUSAL_ATTRIBUTION

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-002 | CLM | SUPPORTED | TITLE_DENOMINATOR | Sector ratios and gross awards do not provide a current aid/revenue ratio for each beneficiary.
CLM-004 | CLM | PARTIAL | CAUSAL_ATTRIBUTION | Policy objective and coverage do not identify the counterfactual number of titles/viewpoints that would disappear without aid.
CLM-005 | CLM | PARTIAL | TASKING | Need authenticated instruction, threat, quid-pro-quo or decision-right evidence tied to a named title and editorial act.
CLM-006 | CLM | PARTIAL | CAUSAL_ATTRIBUTION | Need title-level aid shocks or rule discontinuities linked to content/survival/pluralism outcomes with a credible counterfactual.
CAU-003 | CAU | UNRESOLVED | CAUSAL_ATTRIBUTION | Need title-level counterfactual showing survival/viewpoint loss absent aid.
CAU-004 | CAU | UNRESOLVED | TASKING | Need named pressure/threat/instruction plus editorial compliance trace.
CAU-005 | CAU | UNRESOLVED | CAUSAL_ATTRIBUTION | Need discontinuity/shock analysis with content coding and comparator titles.
CAU-006 | CAU | UNRESOLVED | GENERALIZATION | Need consistent pluralism metric and counterfactual market structure.

SEMANTIC_COUNTS_V1:LED:0|CLM:6|AXS:4|CAU:6|CTRL:8|ACT:4

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"French press support is a multi-channel, rule-based system combining pluralism, distribution, modernization and indirect fiscal/postal support.","claimant":"INV-076 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-007","FCT-016","FCT-017","FCT-021","FCT-022","FCT-027"]}
CLM-002 | {"claim":"Public aid is economically material and concentrated: Senate reports place direct support above 20% of IPG turnover at sector level and identify a small group of multi-million-euro beneficiaries.","claimant":"INV-076 synthesis","counter":"NONE_FOUND","gap":"Sector ratios and gross awards do not provide a current aid/revenue ratio for each beneficiary.","gap_type":"TITLE_DENOMINATOR","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-014"]}
CLM-003 | {"claim":"The allocation rules inspected are predominantly status/economic/circulation formulas, with an IPG content category, and do not condition aid on agreement with a government editorial position.","claimant":"INV-076 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-016","FCT-017","FCT-018","FCT-021","FCT-027"]}
CLM-004 | {"claim":"The policy rationale is explicitly pluralist: aid seeks to cushion low advertising revenue and distribution costs so market pressure does not eliminate viewpoints or local access.","claimant":"INV-076 synthesis","counter":"NONE_FOUND","gap":"Policy objective and coverage do not identify the counterfactual number of titles/viewpoints that would disappear without aid.","gap_type":"CAUSAL_ATTRIBUTION","materiality":"HIGH","status":"PARTIAL","support":["FCT-003","FCT-004","FCT-006","FCT-008","FCT-020","FCT-023"]}
CLM-005 | {"claim":"Economic dependence creates a plausible structural risk to independence, but the inspected corpus does not establish a generic subsidy -> state instruction -> editorial compliance chain.","claimant":"INV-076 synthesis","counter":["FCT-016","FCT-018","FCT-019"],"gap":"Need authenticated instruction, threat, quid-pro-quo or decision-right evidence tied to a named title and editorial act.","gap_type":"TASKING","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-009","FCT-014","FCT-015","FCT-019"]}
CLM-006 | {"claim":"The inspected corpus does not establish the marginal causal effect of press subsidies on editorial line, political coverage or pluralism outcomes.","claimant":"INV-076 synthesis","counter":"NONE_FOUND","gap":"Need title-level aid shocks or rule discontinuities linked to content/survival/pluralism outcomes with a credible counterfactual.","gap_type":"CAUSAL_ATTRIBUTION","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-003","FCT-014","FCT-023"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-007","QRY-010","QRY-011","QRY-013","QRY-014","QRY-015","QRY-016"],"axis":"allocation_rules_and_amounts","inv_id":"INV-076","links":["INV-076"],"question":"How are press aids allocated and how large are they?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-016","FCT-017","FCT-018","FCT-021","FCT-022","FCT-024","FCT-025","FCT-026","FCT-027"],"sought_objects":["scheme categories","eligibility rules","award formulas","beneficiary counts","amounts"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-003","QRY-004","QRY-005","QRY-006"],"axis":"economic_dependence","inv_id":"INV-076","links":["INV-076"],"question":"What evidence shows material economic dependence on public support?","result_ids":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015"],"sought_objects":["sector aid/revenue ratio","title concentration","historical dependence indicators"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-007","QRY-008","QRY-017"],"axis":"editorial_pressure_control","inv_id":"INV-076","links":["INV-076"],"question":"What evidence links aid dependence to state editorial pressure or tasking?","result_ids":["FCT-013","FCT-015","FCT-016","FCT-017","FCT-018","FCT-019"],"sought_objects":["quid pro quo","instruction","withdrawal threat","editorial compliance","formal independence controls"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-001","QRY-002","QRY-009","QRY-012","QRY-018","QRY-019"],"axis":"pluralism_effect","inv_id":"INV-076","links":["INV-076"],"question":"What evidence links aid to pluralism, survival, market structure or editorial outcomes?","result_ids":["FCT-003","FCT-004","FCT-006","FCT-008","FCT-020","FCT-023","FCT-026"],"sought_objects":["survival counterfactual","pluralism measure","market structure","content effect","aid change design"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"Rules directly define the eligibility and calculation pathway.","counter":"NONE_FOUND","limit":"Formal eligibility does not imply editorial approval or tasking.","mechanism":"IPG status + low advertising/circulation/economic criteria -> eligibility/formula -> public aid amount","status":"SUPPORTED","support":["FCT-016","FCT-017","FCT-018","FCT-021","FCT-027"]}
CAU-002 | {"causal_right":"The subsidy mechanism directly offsets defined distribution costs.","counter":"NONE_FOUND","limit":"The run does not estimate the marginal readership or survival effect.","mechanism":"distribution subsidy -> lower eligible distribution burden -> wider/cheaper physical access","status":"SUPPORTED","support":["FCT-007","FCT-027"]}
CAU-003 | {"counter":"NONE_FOUND","gap":"Need title-level counterfactual showing survival/viewpoint loss absent aid.","gap_type":"CAUSAL_ATTRIBUTION","limit":"Rationale is explicit, but a counterfactual survival/pluralism effect is not measured.","mechanism":"pluralism aid -> weaker advertising-market pressure -> preservation of title/viewpoint","status":"UNRESOLVED","support":["FCT-004","FCT-008","FCT-020","FCT-023"]}
CAU-004 | {"counter":["FCT-016","FCT-018","FCT-019"],"gap":"Need named pressure/threat/instruction plus editorial compliance trace.","gap_type":"TASKING","limit":"Material dependence is not an authenticated command chain.","mechanism":"high public-aid dependence -> state leverage -> editorial instruction/compliance","status":"UNRESOLVED","support":["FCT-009","FCT-014","FCT-015"]}
CAU-005 | {"counter":"NONE_FOUND","gap":"Need discontinuity/shock analysis with content coding and comparator titles.","gap_type":"CAUSAL_ATTRIBUTION","limit":"Temporal budget variation and beneficiary turnover are not content-effect designs.","mechanism":"change in aid amount/rules -> change in editorial line/content","status":"UNRESOLVED","support":["FCT-024","FCT-025","FCT-026"]}
CAU-006 | {"counter":"NONE_FOUND","gap":"Need consistent pluralism metric and counterfactual market structure.","gap_type":"GENERALIZATION","limit":"Broad beneficiary counts show coverage, not marginal pluralism effect.","mechanism":"public support architecture -> overall media pluralism","status":"UNRESOLVED","support":["FCT-003","FCT-004","FCT-006","FCT-008","FCT-020","FCT-023"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Subsidy != control: public financing must be separated from authority over editorial decisions.","status":"DONE","support":["FCT-016","FCT-018","FCT-019"]}
CTRL-002 | {"control":"Eligibility != tasking: IPG/economic criteria do not prove message instruction.","status":"DONE","support":["FCT-016","FCT-018","FCT-021"]}
CTRL-003 | {"control":"Dependence != editorial effect: aid/revenue exposure is a risk indicator, not evidence of content change.","status":"DONE","support":["FCT-009","FCT-014","FCT-015"]}
CTRL-004 | {"control":"Favorable or unfavorable coverage != quid pro quo absent authenticated exchange or threat.","status":"DONE","support":["FCT-019"]}
CTRL-005 | {"control":"Pluralism objective != pluralism causal effect: policy purpose and recipient counts do not identify the counterfactual.","status":"DONE","support":["FCT-003","FCT-004","FCT-020","FCT-023"]}
CTRL-006 | {"control":"Budget authorization != execution.","status":"DONE","support":["FCT-001","FCT-024","FCT-025"]}
CTRL-007 | {"control":"Concentration of aid != ideological favoritism without an allocation-bias or instruction test.","status":"DONE","support":["FCT-010","FCT-012","FCT-016"]}
CTRL-008 | {"control":"Absence of a located quid-pro-quo or causal study is not proof that none exists.","status":"DONE","support":["FCT-013","FCT-015"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Preserve separate nodes for eligibility/formula, economic dependence, editorial authority and downstream pluralism effect.","actor":"routing/control plane","intent":"avoid subsidy=control shortcut","status":"DONE","support":["FCT-016","FCT-017","FCT-019","FCT-021"]}
ACT-002 | {"action":"Treat Senate aid/turnover ratios and top-beneficiary tables as dependence/concentration evidence only.","actor":"routing/control plane","intent":"preserve causal ceiling","status":"DONE","support":["FCT-009","FCT-010","FCT-012","FCT-014"]}
ACT-003 | {"action":"Reopen editorial-control claim only with title-specific authenticated pressure, grant conditionality or compliance evidence.","actor":"future INV-076 update","intent":"close leverage -> editorial effect edge","status":"DEFERRED","support":["FCT-015","FCT-019"]}
ACT-004 | {"action":"Reopen pluralism-effect claim only with aid-rule shocks or title-level counterfactual survival/content designs.","actor":"future INV-076 update","intent":"close subsidy -> pluralism edge","status":"DEFERRED","support":["FCT-003","FCT-023","FCT-026"]}

SEARCH_ACTIVITY_V1:WEB:3|FETCH:16|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL | mnemo | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.culture.gouv.fr/thematiques/presse-ecrite/tableaux-des-titres-de-presse-aides3 | FETCH CULTURE-AIDES-2024
QRY-002 | FETCH | FOUND | SRC-002 | https://www.culture.gouv.fr/thematiques/presse-ecrite/soutien-public-a-la-presse | FETCH CULTURE-SOUTIEN-PRESSE
QRY-003 | FETCH | FOUND | SRC-003 | https://www.senat.fr/rap/a23-133-42/a23-133-42_mono.html | FETCH SENAT-PRESSE-PLF2024
QRY-004 | FETCH | FOUND | SRC-004 | https://www.senat.fr/rap/a24-149-42/a24-149-42_mono.html | FETCH SENAT-PRESSE-PLF2025
QRY-005 | FETCH | FOUND | SRC-005 | https://www.senat.fr/rap/r20-692/r20-692.html | FETCH SENAT-AIDES-PRESSE-2021
QRY-006 | FETCH | FOUND | SRC-006 | https://www.senat.fr/salle-de-presse/communiques-de-presse/presse/cp20210617.html | FETCH SENAT-AIDES-SYNTHESE-2021
QRY-007 | FETCH | FOUND | SRC-007 | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000332947 | FETCH LEGIFRANCE-86-616
QRY-008 | FETCH | FOUND | SRC-008 | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000033386692 | FETCH LEGIFRANCE-1881-2BIS
QRY-009 | FETCH | FOUND | SRC-009 | https://qpc360.conseil-constitutionnel.fr/2016-01-07/decision-2015-511-qpc-7-janvier-2016 | FETCH CC-2015-511-QPC
QRY-010 | FETCH | FOUND | SRC-010 | https://www.culture.gouv.fr/thematiques/presse-ecrite/liste-des-aides-a-la-presse-et-des-appels-a-projets/l-aide-au-pluralisme-de-la-presse-periodique-regionale-et-locale | FETCH CULTURE-PPR-AIDE
QRY-011 | FETCH | FOUND | SRC-011 | https://www.culture.gouv.fr/thematiques/presse-ecrite/liste-des-aides-a-la-presse-et-des-appels-a-projets | FETCH CULTURE-AIDES-LISTE
QRY-012 | FETCH | FOUND | SRC-012 | https://questions.assemblee-nationale.fr/q17/17-1312QE.htm | FETCH AN-QE-1312-2025
QRY-013 | FETCH | FOUND | SRC-013 | https://www.senat.fr/rap/l23-128-319/l23-128-319_mono.html | FETCH SENAT-MLIC-PLF2024
QRY-014 | FETCH | FOUND | SRC-014 | https://www.senat.fr/rap/l24-144-319/l24-144-3191.html | FETCH SENAT-MLIC-PLF2025
QRY-015 | FETCH | FOUND | SRC-015 | https://www.culture.gouv.fr/thematiques/presse-ecrite/tableaux-des-titres-de-presse-aides2?switchTo=fre-FR | FETCH CULTURE-AIDES-2023
QRY-016 | FETCH | FOUND | SRC-016 | https://www.culture.gouv.fr/catalogue-des-demarches-et-subventions/subvention/aide-a-la-distribution-de-la-presse-nationale-au-numero | FETCH CULTURE-DISTRIBUTION-AIDE
QRY-017 | WEB | NON_TROUVE | - | - | France authenticated public press subsidy editorial instruction coverage quid pro quo correspondence
QRY-018 | WEB | NON_TROUVE | - | - | France causal study press subsidy change editorial line content counterfactual
QRY-019 | WEB | NON_TROUVE | - | - | France public press aid withdrawal causal effect title survival pluralism independent design

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | CULTURE-AIDES-2024 | Ministère Culture — tableaux titres aidés 2024 | 2025-08-06 | 2026-09-10T06:32:32Z | 2024 direct/indirect totals, beneficiary counts, pluralism/distribution breakdown | https://www.culture.gouv.fr/thematiques/presse-ecrite/tableaux-des-titres-de-presse-aides3
SRC-002 | ◈ | fam:A | CULTURE-SOUTIEN-PRESSE | Ministère Culture — soutien public à la presse | 2026-07-01 | 2026-09-10T06:32:32Z | Current pluralism rationale and 2024 figures | https://www.culture.gouv.fr/thematiques/presse-ecrite/soutien-public-a-la-presse
SRC-003 | ◈ | fam:B | SENAT-PRESSE-PLF2024 | Sénat — PLF 2024 Presse | 2023-11-23 | 2026-09-10T06:32:32Z | Concentration, top aided dailies, direct aid share of IPG turnover | https://www.senat.fr/rap/a23-133-42/a23-133-42_mono.html
SRC-004 | ◈ | fam:B | SENAT-PRESSE-PLF2025 | Sénat — PLF 2025 Presse | 2024-11-21 | 2026-09-10T06:32:32Z | 2023 top aid recipients and reform critique | https://www.senat.fr/rap/a24-149-42/a24-149-42_mono.html
SRC-005 | ◈ | fam:B | SENAT-AIDES-PRESSE-2021 | Sénat — rapport aides presse 2021 | 2021-06-16 | 2026-09-10T06:32:32Z | About 400m public support; 21.4% turnover excluding tax expenditure | https://www.senat.fr/rap/r20-692/r20-692.html
SRC-006 | ◈ | fam:B | SENAT-AIDES-SYNTHESE-2021 | Sénat — synthèse Vitamine ou morphine | 2021-06-17 | 2026-09-10T06:32:32Z | Dependence risk and reform recommendation | https://www.senat.fr/salle-de-presse/communiques-de-presse/presse/cp20210617.html
SRC-007 | ◈ | fam:C | LEGIFRANCE-86-616 | Légifrance — décret 86-616 | 2026-09-03 | 2026-09-10T06:32:32Z | IPG/economic eligibility and aid cap | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000332947
SRC-008 | ◈ | fam:C | LEGIFRANCE-1881-2BIS | Légifrance — loi presse article 2 bis | 2026-06-27 | 2026-09-10T06:32:32Z | Journalist right to refuse pressure | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000033386692
SRC-009 | ◈ | fam:D | CC-2015-511-QPC | Conseil constitutionnel — 2015-511 QPC | 2016-01-07 | 2026-09-10T06:32:32Z | Pluralism and independence as constitutional objectives | https://qpc360.conseil-constitutionnel.fr/2016-01-07/decision-2015-511-qpc-7-janvier-2016
SRC-010 | ◈ | fam:A | CULTURE-PPR-AIDE | Ministère Culture — aide pluralisme presse régionale/locale | 2026 | 2026-09-10T06:32:32Z | Paid-copy formulas and bounds | https://www.culture.gouv.fr/thematiques/presse-ecrite/liste-des-aides-a-la-presse-et-des-appels-a-projets/l-aide-au-pluralisme-de-la-presse-periodique-regionale-et-locale
SRC-011 | ◈ | fam:A | CULTURE-AIDES-LISTE | Ministère Culture — liste aides presse | 2026 | 2026-09-10T06:32:32Z | Aid architecture by channel | https://www.culture.gouv.fr/thematiques/presse-ecrite/liste-des-aides-a-la-presse-et-des-appels-a-projets
SRC-012 | ◈ | fam:E | AN-QE-1312-2025 | Assemblée nationale — réponse presse locale | 2025-03-04 | 2026-09-10T06:32:32Z | Market weakness and pluralism rationale | https://questions.assemblee-nationale.fr/q17/17-1312QE.htm
SRC-013 | ◈ | fam:B | SENAT-MLIC-PLF2024 | Sénat — PLF 2024 Médias | 2023-11-23 | 2026-09-10T06:32:32Z | 2024 budget envelope and pluralism credits | https://www.senat.fr/rap/l23-128-319/l23-128-319_mono.html
SRC-014 | ◈ | fam:B | SENAT-MLIC-PLF2025 | Sénat — PLF 2025 Médias | 2024-11-21 | 2026-09-10T06:32:32Z | 2025 aid envelope | https://www.senat.fr/rap/l24-144-319/l24-144-3191.html
SRC-015 | ◈ | fam:A | CULTURE-AIDES-2023 | Ministère Culture — tableaux titres aidés 2023 | 2024-06-21 | 2026-09-10T06:34:05Z | 2023 QFRP beneficiary set | https://www.culture.gouv.fr/thematiques/presse-ecrite/tableaux-des-titres-de-presse-aides2?switchTo=fre-FR
SRC-016 | ◈ | fam:A | CULTURE-DISTRIBUTION-AIDE | Ministère Culture — aide distribution presse nationale | 2026 | 2026-09-10T06:34:05Z | Distribution formula from eligible costs | https://www.culture.gouv.fr/catalogue-des-demarches-et-subventions/subvention/aide-a-la-distribution-de-la-presse-nationale-au-numero

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.culture.gouv.fr/thematiques/presse-ecrite/tableaux-des-titres-de-presse-aides3 | A | 2024 | 2024 direct press aid execution | The Ministry reports 175.2 million euros of direct press aid in 2024: 23.4m pluralism, 130.1m transport/distribution and 21.7m modernization. | -
FCT-002 | FACT | ✧ | https://www.culture.gouv.fr/thematiques/presse-ecrite/tableaux-des-titres-de-presse-aides3 | A | 2024 | 2024 indirect aid estimate | The Ministry reports about 300 million euros of indirect support in 2024: 119m estimated tax expenditure from the 2.1% VAT rate and 181m estimated postal tariff advantage. | -
FCT-003 | FACT | ✧ | https://www.culture.gouv.fr/thematiques/presse-ecrite/tableaux-des-titres-de-presse-aides3 | A | 2024 | Broad beneficiary coverage | The Ministry states that 527 press titles benefited from press aid in 2024. | -
FCT-004 | FACT | ✧ | https://www.culture.gouv.fr/thematiques/presse-ecrite/tableaux-des-titres-de-presse-aides3 | A | 2024 | Pluralism aid coverage | In 2024, 23.4m euros of pluralism aid went to 375 titles. | -
FCT-005 | FACT | ✧ | https://www.culture.gouv.fr/thematiques/presse-ecrite/tableaux-des-titres-de-presse-aides3 | A | 2024 | National low-ad-revenue pluralism aid concentration | Four national IPG dailies — La Croix, L’Humanité, Libération and L’Opinion — shared 10.35m euros under the low-advertising-resource daily aid in 2024. | -
FCT-006 | FACT | ✧ | https://www.culture.gouv.fr/thematiques/presse-ecrite/tableaux-des-titres-de-presse-aides3 | A | 2024 | Online pluralism aid | The dedicated online press pluralism aid supported 69 titles for 4m euros in 2024. | -
FCT-007 | FACT | ✧ | https://www.culture.gouv.fr/thematiques/presse-ecrite/tableaux-des-titres-de-presse-aides3 | A | 2024 | Distribution aid is a major component | The Ministry reports 130.1m euros of transport/distribution aid in 2024, including 27m for distribution of 10 national IPG dailies, 69.2m for posted copies and 33.9m for delivered copies. | -
FCT-008 | FACT | ✧ | https://www.culture.gouv.fr/thematiques/presse-ecrite/soutien-public-a-la-presse | A | 2024 | Pluralism rationale and advertising pressure | The Ministry describes pluralism aid as supplementing resources of titles with insufficient advertising revenue so advertising pressure does not determine which ideas can be expressed. | -
FCT-009 | FACT | ✧ | https://www.senat.fr/rap/a23-133-42/a23-133-42_mono.html | B | 2024-budget-report | Direct aid is economically material at sector level | The Senate culture report states that direct press aid, excluding tax expenditure, represents more than 20% of the turnover of the IPG press. | -
FCT-010 | FACT | ✧ | https://www.senat.fr/rap/a23-133-42/a23-133-42_mono.html | B | 2024-budget-report | Aid concentration among large beneficiaries | The Senate report lists six heavily aided dailies, with total support in the cited table ranging from about 3.9m euros for L’Humanité to 12.2m euros for Aujourd’hui en France. | -
FCT-011 | FACT | ✧ | https://www.senat.fr/rap/a23-133-42/a23-133-42_mono.html | B | 2024-budget-report | Pluralism-aid concentration is explicit | The Senate report describes pluralism aid as extremely concentrated, noting that a small number of national titles share a large part of the relevant envelopes. | -
FCT-012 | FACT | ✧ | https://www.senat.fr/rap/a24-149-42/a24-149-42_mono.html | B | 2023 | 2023 top beneficiaries remain concentrated | For 2023, the Senate lists Le Parisien at 12.685m euros, Le Monde 5.744m, Le Figaro 5.668m, Ouest-France 5.455m, Libération 5.200m and L’Humanité 3.970m among the largest aided entities. | -
FCT-013 | FACT | ✧ | https://www.senat.fr/rap/a24-149-42/a24-149-42_mono.html | B | 2024 | Parliamentary critique targets opacity/complexity, not proven editorial quid pro quo | The Senate rapporteur calls direct aids frozen, opaque and complex and argues for reform, but the cited report does not document a state instruction to alter a named editorial line in exchange for aid. | -
FCT-014 | FACT | ✧ | https://www.senat.fr/rap/r20-692/r20-692.html | B | 2021 | Historical public-aid dependence indicator | A 2021 Senate report estimated public support to written press at about 400m euros per year and, excluding tax expenditure, 21.4% of sector turnover before additional recovery-plan schemes. | -
FCT-015 | FACT | ✧ | https://www.senat.fr/salle-de-presse/communiques-de-presse/presse/cp20210617.html | B | 2021 | Dependence risk is a policy concern, not a demonstrated control chain | The Senate synthesis explicitly raises the risk that excessive dependence on public funds could threaten press independence and recommends reform; it frames a risk rather than demonstrating editorial command. | -
FCT-016 | FACT | ✧ | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000332947 | C | current-law | QFRP eligibility is rule-based and economic | Decree 86-616 ties eligibility to IPG status, periodicity, price/circulation conditions and low advertising-resource thresholds; for several sections advertising must be below 25% of total revenues. | -
FCT-017 | FACT | ✧ | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000332947 | C | current-law | Per-title pluralism aid has an explicit economic cap | Under decree 86-616, aid to a publication cannot exceed 25% of its prior-year total revenues excluding public subsidies. | -
FCT-018 | FACT | ✧ | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000332947 | C | current-law | Eligibility includes IPG content category but not government approval of editorial viewpoint | The decree requires qualifying publications to provide political/general information and commentary tending to enlighten citizens, while award mechanics rely on economic and circulation criteria rather than agreement with a government editorial position. | -
FCT-019 | FACT | ✧ | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000033386692 | C | current-law | Journalists have a statutory right to refuse pressure | Article 2 bis of the 1881 press law gives journalists the right to refuse pressure and acts contrary to professional conviction, within the company ethical-charter framework. | -
FCT-020 | FACT | ✧ | https://qpc360.conseil-constitutionnel.fr/2016-01-07/decision-2015-511-qpc-7-janvier-2016 | D | 2016 | Pluralism and independence are constitutional-value objectives | The Constitutional Council states that pluralism and independence of IPG dailies are objectives of constitutional value tied to effective freedom of communication. | -
FCT-021 | FACT | ✧ | https://www.culture.gouv.fr/thematiques/presse-ecrite/liste-des-aides-a-la-presse-et-des-appels-a-projets/l-aide-au-pluralisme-de-la-presse-periodique-regionale-et-locale | A | current | Regional/local pluralism aid uses bounded distribution formulas | The regional/local periodic press aid calculates grants from paid-copy counts with floor and ceiling diffusion references and section-specific eligibility conditions. | -
FCT-022 | FACT | ✧ | https://www.culture.gouv.fr/thematiques/presse-ecrite/liste-des-aides-a-la-presse-et-des-appels-a-projets | A | current | Aid architecture separates objectives and channels | The Ministry catalog separates direct pluralism aid, distribution aid, modernization and innovation mechanisms rather than a single discretionary grant. | -
FCT-023 | FACT | ✧ | https://questions.assemblee-nationale.fr/q17/17-1312QE.htm | E | 2025 | Government links local aid to market weakness and pluralism | In a March 2025 parliamentary answer, the government cites declining advertising and readership and justifies distribution and modernization support as helping maintain local pluralism and access. | -
FCT-024 | FACT | ✧ | https://www.senat.fr/rap/l23-128-319/l23-128-319_mono.html | B | 2024-budget | Budget authorization differs from executed aid totals | The 2024 Senate budget report put program-180 press-aid credits near 195.8m euros, including 25.925m for pluralism; later Ministry execution figures differ, so authorization and actual payments must not be conflated. | -
FCT-025 | FACT | ✧ | https://www.senat.fr/rap/l24-144-319/l24-144-3191.html | B | 2025-budget | 2025 planned aid envelope remained near 194m euros | The Senate 2025 budget report projected about 193.8m euros in payment credits for press aid, broadly stable year on year. | -
FCT-026 | FACT | ✧ | https://www.culture.gouv.fr/thematiques/presse-ecrite/tableaux-des-titres-de-presse-aides2?switchTo=fre-FR | A | 2023 | Pluralism-aid beneficiary set changes over time | For 2023 the Ministry reported seven national low-ad-revenue daily beneficiaries sharing about 10.4m euros, compared with four such dailies in 2024. | -
FCT-027 | FACT | ✧ | https://www.culture.gouv.fr/catalogue-des-demarches-et-subventions/subvention/aide-a-la-distribution-de-la-presse-nationale-au-numero | A | current | Distribution support is formulaic | The national distribution aid is calculated as a percentage of eligible prior-year distribution costs, with different rates for QFRP and other eligible IPG publications. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-001
FCT-005 | SRC-001
FCT-006 | SRC-001
FCT-007 | SRC-001
FCT-008 | SRC-002
FCT-009 | SRC-003
FCT-010 | SRC-003
FCT-011 | SRC-003
FCT-012 | SRC-004
FCT-013 | SRC-004
FCT-014 | SRC-005
FCT-015 | SRC-006
FCT-016 | SRC-007
FCT-017 | SRC-007
FCT-018 | SRC-007
FCT-019 | SRC-008
FCT-020 | SRC-009
FCT-021 | SRC-010
FCT-022 | SRC-011
FCT-023 | SRC-012
FCT-024 | SRC-013
FCT-025 | SRC-014
FCT-026 | SRC-015
FCT-027 | SRC-016

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
ATTEMPT-001 | {"created_at":"2026-09-10T06:41:47.686949+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":27,"eligible":27,"failure":0,"success":0}}

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
