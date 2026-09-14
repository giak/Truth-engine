ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260910-0400-aipac-electoral-lobbying-france | PARENT_RUN_ID:NONE | AS_OF:2026-09-10
INPUT_KIND:RUN_CARD | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/inv028/runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-10_aipac-electoral-lobbying-france/2026-09-10_04-00_aipac-electoral-lobbying-france_INPUT.md | SUBJECT_SLUG:aipac-electoral-lobbying-france | SUBJECT_FP:sha256:e68064cc663609c998e0260cde7fed1c3a61f996ccedb69e45c5718e745d791c | INPUT_SHA256:sha256:591da7cd1092b6b1c87b79dec2187b6e601ebce289e0b85b9ce15675fe69318f
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:United States, mainly 2010-2026, with necessary antecedents and a France comparator limited to genuinely comparable mechanisms; trace resources -> lobbying/endorsement/electoral spending -> candidate/official -> position/vote/campaign behavior -> electoral or policy outcome.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/MONEY.md,clusters/POWER.md,clusters/NETWORK.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# AIPAC : mécanismes électoraux et lobbying, plafond causal, comparaison française

## Résultat central

Le corpus ferme trois mécanismes juridiquement distincts aux États-Unis : le lobbying fédéral direct d'AIPAC, les contributions via AIPAC PAC et les dépenses indépendantes via United Democracy Project. Les disclosures fédéraux documentent des flux financiers importants et, pour UDP, des dépenses explicites de soutien ou d'opposition envers des candidats identifiés. Les courses Bowman-Latimer et Bush-Bell montrent ainsi une intervention électorale financée suivie de la victoire du candidat soutenu, sans permettre d'identifier la contribution causale marginale de ces dépenses au résultat.

AIPAC PAC est enregistré comme PAC d'organisation de membres et PAC de lobbyiste/registrant. Sur la période 2025-2026 couverte par FEC, ses recettes et décaissements se comptent en dizaines de millions de dollars, avec l'essentiel du canal électoral observé sous forme de contributions à d'autres comités. UDP est un Super PAC indépendant et documente séparément des dizaines de millions de dollars de dépenses indépendantes. Ces deux véhicules ne doivent donc pas être confondus. [FCT-001, FCT-002, FCT-003, FCT-004, FCT-007, FCT-008, FCT-009, FCT-010]

## Cas électoraux et effet

Dans NY-16, les filings documentent des dépenses UDP en soutien à George Latimer et en opposition à Jamaal Bowman, avec un total annuel de dépenses indépendantes dépassant 14,5 millions de dollars à la fin du cycle observé. Latimer remporte ensuite la primaire. Le dossier contient toutefois plusieurs explications concurrentes propres au candidat et au district. Dans MO-01, UDP documente de même des dépenses de soutien à Wesley Bell et d'opposition à Cori Bush, puis Bell gagne la primaire officielle 51,1 % contre 45,6 %. [FCT-011, FCT-012, FCT-013, FCT-015, FCT-016, FCT-018, FCT-019, FCT-020, FCT-021]

Ces cas établissent une capacité d'intervention et une exposition achetée dans un environnement électoral. Ils n'établissent ni achat de vote, ni contrôle du candidat, ni persuasion mesurée, ni contrefactuel électoral. La littérature méthodologique retenue confirme qu'une inférence naïve dépenses-résultat est fortement exposée à l'endogénéité et à la sélection stratégique des courses. [FCT-022, FCT-029, FCT-030]

## Lobbying et politique publique

AIPAC est enregistré comme lobbyiste de sa propre organisation sur la politique étrangère américaine au Moyen-Orient et déclare des dépenses de lobbying. Cela établit un canal professionnel direct vers le processus fédéral. Le corpus courant ne ferme pas, pour autant, une chaîne `lobbying ou financement -> changement identifiable de position d'un élu -> vote ou décision -> résultat politique`. Cette arête reste ouverte faute de design ou de dossier décisionnel qui sépare sélection d'élus déjà alignés et modification induite de comportement. [FCT-023, FCT-024]

## Frontière avec la France

La comparaison française ne peut pas reprendre mécaniquement le modèle PAC/Super PAC. Les règles françaises de financement des campagnes interdisent aux personnes morales autres que partis ou groupements politiques de financer un candidat et imposent des restrictions spécifiques aux ressources provenant d'États ou de personnes morales étrangères. Le mécanisme financier américain est donc juridiquement non isomorphe. [FCT-025, FCT-026, FCT-027, FCT-028]

Une comparaison fonctionnelle reste pertinente pour le lobbying, l'accès, le plaidoyer et les réseaux. Elle doit cependant être testée sur des cas français propres, sans transformer l'existence d'un voyage, d'un contact, d'un financement ou d'une proximité en preuve de tasking, de capture ou d'effet politique. C'est précisément la frontière à tester dans le candidat adjacent ELNET France.

## Plafond causal

Le niveau le plus solide est : ressources vérifiées -> véhicule légal identifié -> lobbying, contribution ou dépense indépendante documentée -> intervention ou accès observable. Le niveau `intervention -> exposition` est solide pour les dépenses de communication. Le niveau `exposition -> persuasion -> comportement électoral -> résultat contrefactuel` n'est pas établi. Le niveau `ressource ou lobbying -> changement de position ou vote -> décision publique` n'est pas établi dans ce run.

Aucune preuve inspectée ne justifie une attribution automatique à un commandement étatique israélien, un contrôle des candidats ou un achat de votes. Toute montée à ces niveaux requerrait une preuve distincte de tasking, de comportement ou de causalité.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:7|SRC_COMPLETE:17/17

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-10
- **breaks:**
  - AIPAC PAC and UDP created in 2021-2022
  - 2024 high-spend primary cases
  - 2025-2026 current FEC financial cycle
  - French comparator current through 2026
- **status:** CURRENT_WITH_CAUSAL_CONTROLS
- **window:** 2010-2026 with 2015 lobbying-registration antecedent and 1994/2006 causal controls

### MANIPULATION_REPORT
- **assumptions:**
  - FEC filings establish reported financial actions, not persuasion
  - Schedule E independence certification is a legal assertion, not proof of all informal relationships
  - race outcomes do not identify marginal spending effect
- **clusters:**
  - MONEY
  - POWER
  - NETWORK
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - lobbying can be legal influence
  - electoral spending can alter information environment without buying a vote
  - institutional rules shape feasible influence channels
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - membership PAC contributions
  - independent-expenditure super PAC
  - direct lobbying
  - candidate support/opposition
  - primary spending
  - French legal comparator
- **priorities:**
  - separate AIPAC PAC and UDP legal channels
  - document spending at transaction level
  - test candidate/outcome association
  - retain causal endogeneity controls
  - test France non-isomorphism
- **query_guidance:** Prefer FEC/LDA/CNCCFP and official election results; use academic designs for causal ceiling; keep media only for contemporaneous race context and rival explanations.
- **rhetorical:**
  - **AUTH:** official filings prove bounded transactions and legal categories
  - **BF:** two salient races are not a prevalence denominator
  - **DEM:** retain failed/mixed causal literature and alternative explanations
  - **FAC:** separate spending, exposure, persuasion, candidate behavior and outcome
  - **NUM:** use transaction totals but never infer causal effect from amount alone
- **speaker:**
  - **goal:** forensic mapping of lobbying/electoral-finance mechanisms and effect ceiling
  - **target:** resources -> lobbying/spending -> candidate/audience -> behavior/result
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** organization
  - **S02:** resources
  - **S03:** PAC
  - **S04:** superPAC
  - **S05:** lobbying
  - **S06:** endorsement
  - **S07:** contribution
  - **S08:** independent_spend
  - **S09:** candidate
  - **S10:** message
  - **S11:** exposure
  - **S12:** position
  - **S13:** vote
  - **S14:** result
  - **S15:** counterfactual
- **threats:**
  - donation=vote bought
  - endorsement=control
  - spending=electoral effect
  - lobbying=capture
  - association=tasking
  - US mechanism=France mechanism

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - beneficiary response and marginal electoral effect
  - **input_ids:**
    - FCT-001
    - FCT-004
    - FCT-007
    - FCT-010
    - FCT-011
    - FCT-020
  - **module:** clusters/MONEY.md
  - **negative_results:**
    - money alone does not establish control
  - **not_computable:**
    - unrecorded informal influence without evidence
  - **operations_applied:**
    - typed AIPAC PAC versus UDP flows
    - mapped transaction totals
  - **reason:** separate contribution and independent-expenditure architectures
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-003
  - **status:** DONE
  - **trigger:** PAC/Super-PAC resource flows
- **item 2:**
  - **gaps:**
    - race-specific marginal causal effect
  - **input_ids:**
    - FCT-015
    - FCT-016
    - FCT-021
    - FCT-022
    - FCT-029
    - FCT-030
  - **module:** clusters/POWER.md
  - **negative_results:**
    - spending-to-outcome causal shortcut rejected
  - **not_computable:**
    - counterfactual result from current records
  - **operations_applied:**
    - retained race outcomes
    - tested rival explanations/endogeneity
  - **reason:** test spending/action against outcomes and causal controls
  - **result_ids:**
    - CLM-004
    - CLM-005
    - CAU-003
  - **status:** DONE
  - **trigger:** electoral effect
- **item 3:**
  - **gaps:**
    - functional France lobbying comparison
  - **input_ids:**
    - FCT-001
    - FCT-007
    - FCT-023
    - FCT-025
    - FCT-028
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no direct France PAC/Super-PAC isomorphism
  - **not_computable:**
    - hidden tasking absent records
  - **operations_applied:**
    - separated legal entities/channels
    - tested US-France isomorphism
  - **reason:** separate AIPAC, AIPAC PAC, UDP and French legal comparator
  - **result_ids:**
    - CLM-006
    - CLM-007
  - **status:** DONE
  - **trigger:** organization/intermediary/legal channel

### SCOPING_REPORT
- **exclusions:**
  - donation=vote bought
  - spending=result cause
  - lobbying=capture
  - US architecture=France architecture
- **geo:** United States; France limited comparator
- **object_coverage:** STRONG_FOR_FINANCIAL_CHANNELS_AND_CASE_ACTIONS; MODERATE_FOR_ELECTORAL_ASSOCIATION; WEAK_FOR_MARGINAL_CAUSAL_EFFECT
- **object_question:** By what mechanisms do AIPAC-linked lobbying and electoral-finance structures act, what effects are demonstrable, and what prevents mechanical transposition to France?
- **period:** 2010-2026
- **subject:** AIPAC lobbying/electoral finance and France comparator

### CREDO
- donation != vote bought
- endorsement != control
- spending != electoral effect
- lobbying != capture
- association != tasking
- US mechanism != France mechanism

### COGNITIVE_MAP
- **continuum:**
  - resources
  - legal vehicle
  - lobbying/contribution/independent expenditure
  - candidate/audience exposure
  - candidate position or vote
  - electoral result
  - counterfactual effect
- **core_model:** AIPAC influence operates through legally distinct lobbying, PAC-contribution and super-PAC independent-expenditure channels; action and outcome can be documented, but marginal causal effect requires designs beyond spending/outcome coincidence.
- **rival_models:**
  - money mechanically buys votes
  - AIPAC has no material electoral mechanism
  - AIPAC US mechanism maps directly onto France

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** FEC filings prove contributions/independent expenditures, while causal literature and race-specific rivals break the spending-to-control inference.
  - **support:**
    - FCT-004
    - FCT-013
    - FCT-016
    - FCT-029
    - FCT-030
  - **synthesis:** Treat financial action as verified influence capacity/exposure and require separate evidence for tasking, persuasion, candidate behavior and result causality.
  - **thesis:** Large AIPAC-linked spending proves that supported candidates are controlled or that votes are bought.
- **item 2:**
  - **antithesis:** FEC filings show large candidate-specific support/opposition expenditures and PAC contributions.
  - **support:**
    - FCT-004
    - FCT-010
    - FCT-011
    - FCT-013
    - FCT-018
    - FCT-020
  - **synthesis:** The mechanism is real and measurable even when coordination/control and marginal electoral effect remain unproven.
  - **thesis:** AIPAC has no concrete electoral influence mechanism because spending is legally independent.
- **item 3:**
  - **antithesis:** French rules bar ordinary legal persons from financing candidate campaigns and impose foreign-source restrictions.
  - **support:**
    - FCT-025
    - FCT-027
    - FCT-028
  - **synthesis:** Compare functions such as lobbying/access/advocacy, not the U.S. PAC/Super-PAC financing architecture itself.
  - **thesis:** The U.S. AIPAC/UDP model can be copied directly to France.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **from:** AIPAC PAC donors/resources
  - **resource:** PAC contributions
  - **support:**
    - FCT-002
    - FCT-004
    - FCT-006
  - **to:** candidate/other political committees
- **item 2:**
  - **from:** UDP donors/resources
  - **resource:** independent expenditures
  - **support:**
    - FCT-008
    - FCT-010
    - FCT-011
    - FCT-013
    - FCT-018
    - FCT-020
  - **to:** candidate-specific media/direct mail support or opposition
- **item 3:**
  - **from:** AIPAC organization
  - **resource:** registered lobbying staff/expenditure
  - **support:**
    - FCT-023
    - FCT-024
  - **to:** U.S. federal policy process

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** AIPAC PAC
  - **relation:** contributions to candidates/committees
  - **support:**
    - FCT-004
    - FCT-006
  - **to:** federal electoral committees
- **item 2:**
  - **from:** United Democracy Project
  - **relation:** independent support/opposition expenditures
  - **support:**
    - FCT-011
    - FCT-012
    - FCT-013
    - FCT-018
    - FCT-019
    - FCT-020
  - **to:** NY-16 and MO-01 Democratic primary information environments
- **item 3:**
  - **from:** AIPAC
  - **relation:** registered lobbying
  - **support:**
    - FCT-023
    - FCT-024
  - **to:** U.S. federal decision process

### IMPACT_MAP
- **established:**
  - large PAC contribution flows
  - large candidate-specific independent expenditures
  - direct registered lobbying
  - case-specific electoral concurrence
- **not_established:**
  - vote buying
  - candidate control
  - marginal causal effect of UDP on Bowman or Bush defeats
  - general policy capture
- **partial:**
  - exposure via purchased media/direct mail
  - candidate-response/incentive effects

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** race-specific rival factors and spending endogeneity; no counterfactual design
  - **issue:** spending versus result
  - **pro:** UDP spent heavily in races where Latimer and Bell won
  - **resolution:** ACTION_AND_OUTCOME_VERIFIED; MARGINAL_CAUSAL_EFFECT_NOT_ESTABLISHED
  - **support:**
    - FCT-015
    - FCT-016
    - FCT-021
    - FCT-022
    - FCT-029
    - FCT-030
- **item 2:**
  - **contra:** Schedule E certifies no coordination; no direct tasking evidence inspected
  - **issue:** independent expenditure versus control
  - **pro:** candidate-specific support/opposition spending is explicit
  - **resolution:** ELECTORAL_INTERVENTION_VERIFIED; CANDIDATE_CONTROL_NOT_ESTABLISHED
  - **support:**
    - FCT-013
    - FCT-014
- **item 3:**
  - **contra:** candidate-finance legal-person and foreign-source rules materially differ
  - **issue:** US-France analogy
  - **pro:** both systems permit political advocacy/lobbying
  - **resolution:** FUNCTIONAL_COMPARISON_ONLY; FINANCIAL_ARCHITECTURE_NON_ISOMORPHIC
  - **support:**
    - FCT-025
    - FCT-026
    - FCT-027
    - FCT-028

### VERIFICATION_REPORT
- **downgraded:**
  - spending proves bought vote
  - race victory proves UDP caused outcome
  - U.S. PAC architecture directly maps to France
- **fact_count:** 30
- **negative_controls:**
  - Schedule E non-coordination certification
  - NY-16 rival explanations
  - campaign-spending endogeneity literature
  - French non-isomorphic finance rules
- **provenance_families:** 6
- **query_count:** 20
- **source_count:** 17
- **verification:** 30 material facts map to FEC, election authorities, CNCCFP, LDA, academic and bounded contemporaneous reporting.

### EDI_REPORT
- **corpus:**
  - **limits:**
    - FEC does not measure persuasion
    - two races do not establish prevalence
    - no randomized or natural-experiment estimate specific to UDP cases
  - **strength:** strong financial/action records plus explicit causal controls
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
  - **owner:** 6 provenance families
  - **perspective:** federal filings + state election authorities + French regulator + lobbying disclosures + academic causal literature + bounded media context
  - **stratification:** money/legal vehicle/action/exposure/result/counterfactual
  - **temporal:** 2010-2026 with causal antecedents
- **edi:**
  - **coverage:** HIGH_FOR_MECHANISM_MODERATE_FOR_ASSOCIATION_LOW_FOR_COUNTERFACTUAL_EFFECT
  - **independence:** STRONG_FOR_TRANSACTION_AND_LEGAL_CONTROLS
- **source_counts:**
  - **A:** 8
  - **B:** 2
  - **C:** 2
  - **D:** 2
  - **E:** 2
  - **other:rollcall:** 1
  - **total:** 17

### RESPONSIBILITY_MAP
- **boundary:** Funding, lobbying, independent expenditure, coordination, persuasion, candidate behavior and electoral outcome are distinct claims.
- **not_established:**
  - AIPAC/UDP candidate control
  - vote buying
  - foreign-state tasking of AIPAC in inspected evidence
  - marginal causal share of election outcomes
- **verified:**
  - AIPAC PAC contribution channel
  - UDP independent-expenditure channel
  - AIPAC registered lobbying
  - Latimer/Bell race outcomes

### NEXT_QUERIES
- Candidate/office-level decision records testing whether AIPAC/UDP spending changes policy positions rather than selecting aligned candidates
- Quasi-experimental designs around close AIPAC-targeted primaries
- Comparable France lobbying/access cases without importing U.S. campaign-finance categories
- Authenticated principal/tasking evidence before any foreign-state agency claim

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-002,QRY-014,QRY-015 | support:- | counter:- | results:FCT-001,FCT-004,FCT-007,FCT-023,FCT-024 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-005,QRY-006,QRY-007,QRY-008 | support:- | counter:- | results:FCT-011,FCT-012,FCT-013,FCT-018,FCT-019,FCT-020 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-009,QRY-010,QRY-011,QRY-016,QRY-017 | support:- | counter:- | results:FCT-015,FCT-016,FCT-021,FCT-022,FCT-029,FCT-030 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-012,QRY-013,QRY-020 | support:- | counter:- | results:FCT-025,FCT-026,FCT-027,FCT-028 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-021,QRY-022,QRY-025,QRY-034,QRY-035,SRC-001,SRC-002,SRC-005,SRC-014,SRC-015 | support:FCT-001,FCT-004,FCT-007,FCT-010,FCT-023,FCT-024 | counter:FCT-014 | results:FCT-001,FCT-004,FCT-007,FCT-010,FCT-023,FCT-024,FCT-014 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-021,QRY-022,QRY-023,QRY-024,SRC-001,SRC-002,SRC-003,SRC-004 | support:FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-008,FCT-009,FCT-010 | counter:- | results:FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-008,FCT-009,FCT-010 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-025,QRY-026,QRY-027,QRY-028,QRY-030,QRY-031,QRY-036,QRY-037,SRC-005,SRC-006,SRC-007,SRC-008,SRC-010,SRC-011,SRC-016,SRC-017 | support:FCT-011,FCT-012,FCT-013,FCT-015,FCT-018,FCT-019,FCT-020,FCT-021,FCT-022 | counter:FCT-016,FCT-029,FCT-030 | results:FCT-011,FCT-012,FCT-013,FCT-015,FCT-018,FCT-019,FCT-020,FCT-021,FCT-022,FCT-016,FCT-029,FCT-030 | final:PARTIAL | gap:COUNTERFACTUAL
CLM-004 | attempts:QRY-027,QRY-028,QRY-030,QRY-031,QRY-036,QRY-037,SRC-007,SRC-008,SRC-010,SRC-011,SRC-016,SRC-017 | support:FCT-029,FCT-030,FCT-016,FCT-022 | counter:FCT-015,FCT-021 | results:FCT-029,FCT-030,FCT-016,FCT-022,FCT-015,FCT-021 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-021,QRY-022,QRY-032,QRY-033,SRC-001,SRC-002,SRC-012,SRC-013 | support:FCT-025,FCT-026,FCT-027,FCT-028 | counter:- | results:FCT-025,FCT-026,FCT-027,FCT-028 | final:SUPPORTED | gap:NONE
CLM-006 | attempts:QRY-021,QRY-022,QRY-032,QRY-033,QRY-034,QRY-035,SRC-001,SRC-002,SRC-012,SRC-013,SRC-014,SRC-015 | support:FCT-023,FCT-024,FCT-025,FCT-028 | counter:- | results:FCT-023,FCT-024,FCT-025,FCT-028 | final:PARTIAL | gap:FRANCE_CASE_EVIDENCE
CLM-007 | attempts:QRY-021,QRY-022,QRY-025,QRY-028,QRY-032,QRY-033,QRY-034,QRY-035,SRC-001,SRC-002,SRC-005,SRC-008,SRC-012,SRC-013,SRC-014,SRC-015 | support:FCT-014,FCT-023,FCT-024,FCT-028 | counter:FCT-010,FCT-013,FCT-020 | results:FCT-014,FCT-023,FCT-024,FCT-028,FCT-010,FCT-013,FCT-020 | final:PARTIAL | gap:TASKING_AND_BEHAVIOR

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-003 | CLM | PARTIAL | COUNTERFACTUAL | No race-specific counterfactual or quasi-experimental design isolates the marginal effect of UDP spending from candidate, district, timing and strategic-spending confounders.
CLM-006 | CLM | PARTIAL | FRANCE_CASE_EVIDENCE | This run does not establish a matched French actor-level case measuring access, policy-position change or decision effect under the French lobbying regime.
CLM-007 | CLM | PARTIAL | TASKING_AND_BEHAVIOR | Authenticated principal-tasking records or candidate/office-level response evidence would be required to upgrade agency, control or capture claims.
CAU-003 | CAU | UNRESOLVED | COUNTERFACTUAL | No causal design specific to these races isolates spending -> voter behavior -> result.
CAU-004 | CAU | UNRESOLVED | BEHAVIORAL_RESPONSE | Need candidate/office-level decision records or a design separating selection of already-aligned candidates from induced position change.

SEMANTIC_COUNTS_V1:LED:0|CLM:7|AXS:4|CAU:5|CTRL:8|ACT:4

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"AIPAC-linked influence capacity operates through legally distinct channels: direct federal lobbying by AIPAC, contributions through AIPAC PAC, and independent expenditures through United Democracy Project.","claimant":"INV-028 synthesis","counter":["FCT-014"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-004","FCT-007","FCT-010","FCT-023","FCT-024"]}
CLM-002 | {"claim":"AIPAC PAC and UDP mobilize large, disclosed financial resources, including tens of millions of dollars in contributions and independent expenditures in the 2024 and 2025-2026 cycles.","claimant":"INV-028 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-008","FCT-009","FCT-010"]}
CLM-003 | {"claim":"UDP made candidate-specific support and opposition expenditures in the Bowman-Latimer and Bush-Bell primaries, and the supported candidates won; these observations establish intervention plus outcome concurrence but not UDP's marginal causal contribution to the results.","claimant":"INV-028 synthesis","counter":["FCT-016","FCT-029","FCT-030"],"gap":"No race-specific counterfactual or quasi-experimental design isolates the marginal effect of UDP spending from candidate, district, timing and strategic-spending confounders.","gap_type":"COUNTERFACTUAL","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-011","FCT-012","FCT-013","FCT-015","FCT-018","FCT-019","FCT-020","FCT-021","FCT-022"]}
CLM-004 | {"claim":"Campaign-spending totals and election outcomes cannot by themselves identify electoral causality because strategic spending and candidate/district differences create substantial endogeneity.","claimant":"INV-028 synthesis","counter":["FCT-015","FCT-021"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-029","FCT-030","FCT-016","FCT-022"]}
CLM-005 | {"claim":"The U.S. PAC/Super-PAC campaign-finance architecture is not mechanically transposable to France because French candidate-finance rules prohibit ordinary legal-person campaign financing and restrict foreign-state or foreign-legal-person assistance.","claimant":"INV-028 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-025","FCT-026","FCT-027","FCT-028"]}
CLM-006 | {"claim":"A functional comparison with France remains possible for lobbying, advocacy, access and network mechanisms, but not by importing the U.S. PAC/Super-PAC financing architecture as an isomorphic model.","claimant":"INV-028 synthesis","counter":"NONE_FOUND","gap":"This run does not establish a matched French actor-level case measuring access, policy-position change or decision effect under the French lobbying regime.","gap_type":"FRANCE_CASE_EVIDENCE","materiality":"HIGH","status":"PARTIAL","support":["FCT-023","FCT-024","FCT-025","FCT-028"]}
CLM-007 | {"claim":"The inspected corpus does not establish vote buying, candidate control, or direct Israeli-state tasking of AIPAC/UDP; financial action, lobbying and political alignment must therefore remain separate from agency or capture claims.","claimant":"INV-028 synthesis","counter":["FCT-010","FCT-013","FCT-020"],"gap":"Authenticated principal-tasking records or candidate/office-level response evidence would be required to upgrade agency, control or capture claims.","gap_type":"TASKING_AND_BEHAVIOR","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-014","FCT-023","FCT-024","FCT-028"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-014","QRY-015"],"axis":"lobbying_and_pac_architecture","links":["INV-028"],"question":"Quels canaux AIPAC sont directement documentés et juridiquement distincts?","result_ids":["FCT-001","FCT-004","FCT-007","FCT-023","FCT-024"],"sought_objects":["registered lobbying","membership PAC","contributions","super PAC"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-005","QRY-006","QRY-007","QRY-008"],"axis":"candidate_specific_electoral_spending","links":["INV-028"],"question":"Quelles dépenses UDP support/opposition sont documentées transactionnellement?","result_ids":["FCT-011","FCT-012","FCT-013","FCT-018","FCT-019","FCT-020"],"sought_objects":["support","opposition","media placement","direct mail"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-009","QRY-010","QRY-011","QRY-016","QRY-017"],"axis":"electoral_effect_closure","links":["INV-028"],"question":"Les cas Bowman et Bush ferment-ils un effet causal du spending sur le résultat?","result_ids":["FCT-015","FCT-016","FCT-021","FCT-022","FCT-029","FCT-030"],"sought_objects":["outcome","rival explanation","endogeneity","counterfactual"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-012","QRY-013","QRY-020"],"axis":"france_comparability","links":["INV-028"],"question":"Quelles arêtes sont comparables avec la France et lesquelles sont juridiquement non isomorphes?","result_ids":["FCT-025","FCT-026","FCT-027","FCT-028"],"sought_objects":["legal-person finance","foreign source","individual donations","lobbying functional comparator"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"Documented direct lobbying mechanism and disclosed lobbying expenditure","counter":"NONE_FOUND","limit":"Registered lobbying and disclosed expenditure establish an influence channel and access-seeking activity, not policy capture or a specific decision effect.","mechanism":"AIPAC organizational resources -> registered federal lobbying -> access to and activity within the U.S. federal policy process","status":"SUPPORTED","support":["FCT-023","FCT-024"]}
CAU-002 | {"causal_right":"Documented candidate-specific electoral intervention and paid communication exposure","counter":["FCT-014"],"limit":"The expenditure-to-exposure edge is supported by transaction records; persuasion and candidate control are not established by those records.","mechanism":"UDP resources -> candidate-specific independent expenditures -> purchased media/direct-mail support or opposition -> campaign information exposure","status":"SUPPORTED","support":["FCT-010","FCT-011","FCT-012","FCT-013","FCT-018","FCT-019","FCT-020"]}
CAU-003 | {"counter":["FCT-016","FCT-022","FCT-029","FCT-030"],"gap":"No causal design specific to these races isolates spending -> voter behavior -> result.","gap_type":"COUNTERFACTUAL","limit":"Large spending and subsequent defeat coexist, but strategic selection, candidate quality, district factors and other campaign shocks prevent identification of the marginal spending effect.","mechanism":"UDP candidate-specific spending -> voter persuasion/turnout -> Bowman or Bush defeat","status":"UNRESOLVED","support":["FCT-015","FCT-021"]}
CAU-004 | {"counter":"NONE_FOUND","gap":"Need candidate/office-level decision records or a design separating selection of already-aligned candidates from induced position change.","gap_type":"BEHAVIORAL_RESPONSE","limit":"Resource and access channels are documented, but this run lacks matched before/after or counterfactual evidence on candidate or office behavior attributable to the intervention.","mechanism":"AIPAC/UDP lobbying, contributions or spending -> candidate/office policy-position change or vote -> policy outcome","status":"UNRESOLVED","support":["FCT-004","FCT-010","FCT-023","FCT-024"]}
CAU-005 | {"causal_right":"Direct campaign-finance isomorphism with France is rejected by current legal rules","counter":"NONE_FOUND","limit":"Functional lobbying/advocacy comparison remains possible, but the campaign-finance vehicles are legally non-isomorphic.","mechanism":"U.S. PAC/Super-PAC financing architecture -> direct legal analogue in French candidate financing","status":"REFUTED","support":["FCT-025","FCT-026","FCT-027","FCT-028"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Donation or contribution is not evidence that a vote or policy position was bought.","status":"DONE","support":["FCT-004","FCT-006","FCT-029","FCT-030"]}
CTRL-002 | {"control":"Independent-expenditure spending plus an electoral victory does not identify the spending's marginal causal effect.","status":"DONE","support":["FCT-015","FCT-016","FCT-021","FCT-022","FCT-029","FCT-030"]}
CTRL-003 | {"control":"A Schedule E non-coordination certification is a legal reporting assertion and does not prove absence of every informal relationship beyond the filing.","status":"DONE","support":["FCT-014"]}
CTRL-004 | {"control":"Race-specific rival explanations must remain live rather than attributing an outcome to the largest disclosed spender.","status":"DONE","support":["FCT-016","FCT-029","FCT-030"]}
CTRL-005 | {"control":"Registered lobbying establishes lobbying activity, not capture or a specific policy effect.","status":"DONE","support":["FCT-023","FCT-024"]}
CTRL-006 | {"control":"AIPAC, AIPAC PAC and United Democracy Project are distinct legal/operational channels and must not be collapsed into one undifferentiated entity.","status":"DONE","support":["FCT-001","FCT-007","FCT-023"]}
CTRL-007 | {"control":"The U.S. PAC/Super-PAC architecture is not a direct French analogue because candidate-finance rules differ materially.","status":"DONE","support":["FCT-025","FCT-026","FCT-027","FCT-028"]}
CTRL-008 | {"control":"Absence of direct tasking evidence in the inspected corpus blocks an inference of foreign-state agency or command.","status":"DONE","support":["FCT-014","FCT-023","FCT-028"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"RECHECK only if a quasi-experimental or otherwise credible race-specific design isolates UDP/AIPAC-linked spending from candidate and district confounders.","actor":"future INV-028 update","intent":"close marginal electoral-effect uncertainty","status":"DEFERRED","support":["FCT-022","FCT-029","FCT-030"]}
ACT-002 | {"action":"RECHECK matched candidate/office decision records that can distinguish support for already-aligned candidates from induced policy-position change.","actor":"future adjacent investigation","intent":"test behavior rather than resource flow alone","status":"DEFERRED","support":["FCT-004","FCT-010","FCT-023"]}
ACT-003 | {"action":"Use France only as a functional lobbying/access comparator unless a legally comparable campaign-finance mechanism is identified.","actor":"routing/control plane","intent":"prevent false U.S.-France isomorphism","status":"DONE","support":["FCT-025","FCT-026","FCT-027","FCT-028"]}
ACT-004 | {"action":"Require authenticated principal/tasking evidence before any foreign-state agency or command claim.","actor":"future adjacent investigation","intent":"separate lobbying/affinity from state tasking","status":"DONE","support":["FCT-014","FCT-023","FCT-028"]}

SEARCH_ACTIVITY_V1:WEB:20|FETCH:17|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL | mnemo | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | https://www.fec.gov/data/committee/C00797670/ | AIPAC PAC FEC committee current financial summary
QRY-002 | WEB | FOUND | - | https://www.fec.gov/data/committee/C00799031/ | United Democracy Project FEC committee current financial summary
QRY-003 | WEB | FOUND | - | https://www.fec.gov/resources/campaign-finance-statistics/2024/tables/pac/PAC9a_2024_24m.pdf | FEC 2024 top membership PACs AIPAC receipts
QRY-004 | WEB | FOUND | - | https://www.fec.gov/resources/campaign-finance-statistics/2024/tables/pac/PAC4c_2024_18m.pdf | FEC 2024 PAC contributions candidates other committees AIPAC
QRY-005 | WEB | FOUND | - | https://docquery.fec.gov/pdf/814/202406209652023814/202406209652023814_000001.pdf | UDP Bowman June 19 2024 independent expenditure Schedule E
QRY-006 | WEB | FOUND | - | https://docquery.fec.gov/pdf/708/202405229648717708/202405229648717708.pdf | UDP Latimer Bowman May 21 2024 Schedule E
QRY-007 | WEB | FOUND | - | https://docquery.fec.gov/pdf/215/202407039652564215/202407039652564215.pdf | UDP Cori Bush Wesley Bell July 2 2024 Schedule E
QRY-008 | WEB | FOUND | - | https://docquery.fec.gov/pdf/195/202407249665725195/202407249665725195_000001.pdf | UDP Wesley Bell Cori Bush July 23 2024 Schedule E
QRY-009 | WEB | FOUND | - | https://results.elections.ny.gov/contest/5580 | New York Board Elections 2024 Democratic primary congressional district 16 Latimer Bowman
QRY-010 | WEB | FOUND | - | https://www.sos.mo.gov/CMSImages/ElectionResultsStatistics/2024PrimaryElection.pdf | Missouri Secretary State 2024 primary District 1 Bush Bell results
QRY-011 | WEB | FOUND | - | https://rollcall.com/2024/06/25/bowman-ousted-in-new-york-primary-that-drew-millions-in-spending/ | Bowman Latimer 2024 primary UDP spending 14.5 million outcome factors
QRY-012 | WEB | FOUND | - | https://cnccfp.fr/faq/comment-le-candidat-peut-il-financer-sa-campagne/ | CNCCFP how candidate can finance campaign legal persons
QRY-013 | WEB | FOUND | - | https://cnccfp.fr/faq/le-mandataire-peut-il-accepter-un-don-en-provenance-de-letranger-existe-t-il-des-precautions-particulieres-dans-ce-cas/ | CNCCFP foreign donation candidate campaign France
QRY-014 | WEB | FOUND | - | https://lda.gov/filings/public/filing/622ade04-65ca-4364-b78d-49e0dde1d4a5/print/ | AIPAC Lobbying Disclosure Act registration LD-1
QRY-015 | WEB | FOUND | - | https://lda.gov/filings/public/filing/62a5b5e7-b60d-4dc7-a525-b0b2aa99d57f/print/ | AIPAC Lobbying Disclosure Act 2025 Q4 LD-2
QRY-016 | WEB | FOUND | - | https://www.journals.uchicago.edu/doi/10.1086/261954 | Levitt repeat challengers campaign spending election outcomes 1994
QRY-017 | WEB | FOUND | - | https://www.sciencedirect.com/science/article/pii/S0261379405000569 | Jacobson campaign spending effects Senate elections 2006
QRY-018 | WEB | NO_DIRECT_SOURCE | - | - | AIPAC spending proves congressional vote bought causal study
QRY-019 | WEB | NO_DIRECT_SOURCE | - | - | AIPAC FARA foreign principal registration evidence direct Israeli state command
QRY-020 | WEB | NO_DIRECT_SOURCE | - | - | France super PAC unlimited independent expenditure exact analogue candidate campaign
QRY-021 | FETCH | FOUND | SRC-001 | https://www.fec.gov/data/committee/C00797670/ | FETCH FEC-C00797670-CURRENT
QRY-022 | FETCH | FOUND | SRC-002 | https://www.fec.gov/data/committee/C00799031/ | FETCH FEC-C00799031-CURRENT
QRY-023 | FETCH | FOUND | SRC-003 | https://www.fec.gov/resources/campaign-finance-statistics/2024/tables/pac/PAC9a_2024_24m.pdf | FETCH FEC-PAC9A-2024-24M
QRY-024 | FETCH | FOUND | SRC-004 | https://www.fec.gov/resources/campaign-finance-statistics/2024/tables/pac/PAC4c_2024_18m.pdf | FETCH FEC-PAC4C-2024-18M
QRY-025 | FETCH | FOUND | SRC-005 | https://docquery.fec.gov/pdf/814/202406209652023814/202406209652023814_000001.pdf | FETCH FEC-UDP-E231AAB5124DC488CAFE
QRY-026 | FETCH | FOUND | SRC-006 | https://docquery.fec.gov/pdf/708/202405229648717708/202405229648717708.pdf | FETCH FEC-UDP-NY16-20240522
QRY-027 | FETCH | FOUND | SRC-007 | https://docquery.fec.gov/pdf/215/202407039652564215/202407039652564215.pdf | FETCH FEC-UDP-MO01-20240703
QRY-028 | FETCH | FOUND | SRC-008 | https://docquery.fec.gov/pdf/195/202407249665725195/202407249665725195_000001.pdf | FETCH FEC-UDP-MO01-20240724
QRY-029 | FETCH | FOUND | SRC-009 | https://results.elections.ny.gov/contest/5580 | FETCH NYSE-2024-PRIMARY-CD16
QRY-030 | FETCH | FOUND | SRC-010 | https://www.sos.mo.gov/CMSImages/ElectionResultsStatistics/2024PrimaryElection.pdf | FETCH MOSOS-2024-PRIMARY
QRY-031 | FETCH | FOUND | SRC-011 | https://rollcall.com/2024/06/25/bowman-ousted-in-new-york-primary-that-drew-millions-in-spending/ | FETCH ROLLCALL-2024-06-25-BOWMAN
QRY-032 | FETCH | FOUND | SRC-012 | https://cnccfp.fr/faq/comment-le-candidat-peut-il-financer-sa-campagne/ | FETCH CNCCFP-CANDIDATE-FINANCING-2026
QRY-033 | FETCH | FOUND | SRC-013 | https://cnccfp.fr/faq/le-mandataire-peut-il-accepter-un-don-en-provenance-de-letranger-existe-t-il-des-precautions-particulieres-dans-ce-cas/ | FETCH CNCCFP-FOREIGN-DONATION-2026
QRY-034 | FETCH | FOUND | SRC-014 | https://lda.gov/filings/public/filing/622ade04-65ca-4364-b78d-49e0dde1d4a5/print/ | FETCH LDA-AIPAC-LD1-2015
QRY-035 | FETCH | FOUND | SRC-015 | https://lda.gov/filings/public/filing/62a5b5e7-b60d-4dc7-a525-b0b2aa99d57f/print/ | FETCH LDA-AIPAC-2025Q4
QRY-036 | FETCH | FOUND | SRC-016 | https://www.journals.uchicago.edu/doi/10.1086/261954 | FETCH LEVITT-JPE-1994
QRY-037 | FETCH | FOUND | SRC-017 | https://www.sciencedirect.com/science/article/pii/S0261379405000569 | FETCH JACOBSON-ES-2006

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | FEC-C00797670-CURRENT | FEC — AIPAC PAC committee overview | 2026-07-31 | 2026-09-10T03:19:47Z | committee type; 2025-2026 receipts/disbursements | https://www.fec.gov/data/committee/C00797670/
SRC-002 | ◈ | fam:A | FEC-C00799031-CURRENT | FEC — United Democracy Project committee overview | 2026-07-31 | 2026-09-10T03:19:47Z | super PAC type; 2025-2026 receipts/disbursements/IE | https://www.fec.gov/data/committee/C00799031/
SRC-003 | ◈ | fam:A | FEC-PAC9A-2024-24M | FEC PAC Table 9a — Top Membership PACs by Receipts | 2025-03-14 | 2026-09-10T03:19:47Z | rank 1 AIPAC PAC $57,871,196 | https://www.fec.gov/resources/campaign-finance-statistics/2024/tables/pac/PAC9a_2024_24m.pdf
SRC-004 | ◈ | fam:A | FEC-PAC4C-2024-18M | FEC PAC Table 4c — Contributions to Candidates and Other Committees | 2024-08-30 | 2026-09-10T03:19:47Z | rank 1 AIPAC PAC $39,745,931 through 2024-06-30 | https://www.fec.gov/resources/campaign-finance-statistics/2024/tables/pac/PAC4c_2024_18m.pdf
SRC-005 | ◈ | fam:A | FEC-UDP-E231AAB5124DC488CAFE | FEC Schedule E — UDP oppose Jamaal Bowman 2024-06-19 | 2024-06-20 | 2026-09-10T03:19:47Z | Bowman oppose; $47,105.47; CYTD $14,590,266.89 | https://docquery.fec.gov/pdf/814/202406209652023814/202406209652023814_000001.pdf
SRC-006 | ◈ | fam:A | FEC-UDP-NY16-20240522 | FEC Schedule E — UDP NY-16 2024-05-21 | 2024-05-22 | 2026-09-10T03:19:47Z | Latimer support / Bowman opposition media expenditures | https://docquery.fec.gov/pdf/708/202405229648717708/202405229648717708.pdf
SRC-007 | ◈ | fam:A | FEC-UDP-MO01-20240703 | FEC Schedule E — UDP MO-01 2024-07-02 | 2024-07-03 | 2026-09-10T03:19:47Z | Bush oppose / Bell support; CYTD $3,545,608.13 | https://docquery.fec.gov/pdf/215/202407039652564215/202407039652564215.pdf
SRC-008 | ◈ | fam:A | FEC-UDP-MO01-20240724 | FEC Schedule E — UDP MO-01 2024-07-23 | 2024-07-24 | 2026-09-10T03:19:47Z | Bell support $300,000; Bush oppose $700,000; CYTD $7,057,528.36 | https://docquery.fec.gov/pdf/195/202407249665725195/202407249665725195_000001.pdf
SRC-009 | ◈ | fam:B | NYSE-2024-PRIMARY-CD16 | New York State Board of Elections — NY-16 Democratic primary | 2024-06-25 | 2026-09-10T03:19:47Z | official contest; Latimer and Bowman candidates | https://results.elections.ny.gov/contest/5580
SRC-010 | ◈ | fam:B | MOSOS-2024-PRIMARY | Missouri Secretary of State — 2024 Primary Election | 2024-08-06 | 2026-09-10T03:19:47Z | MO-01 Democratic totals Bush/Bell | https://www.sos.mo.gov/CMSImages/ElectionResultsStatistics/2024PrimaryElection.pdf
SRC-011 | ◈ | fam:other:rollcall | ROLLCALL-2024-06-25-BOWMAN | Roll Call — Bowman ousted in New York primary | 2024-06-25 | 2026-09-10T03:19:47Z | Latimer result; UDP $14.5m; alternative factors | https://rollcall.com/2024/06/25/bowman-ousted-in-new-york-primary-that-drew-millions-in-spending/
SRC-012 | ◈ | fam:C | CNCCFP-CANDIDATE-FINANCING-2026 | CNCCFP — Comment le candidat peut-il financer sa campagne ? | 2026-03-18 | 2026-09-10T03:19:47Z | legal persons other than parties cannot finance candidate campaign | https://cnccfp.fr/faq/comment-le-candidat-peut-il-financer-sa-campagne/
SRC-013 | ◈ | fam:C | CNCCFP-FOREIGN-DONATION-2026 | CNCCFP — Don en provenance de l’étranger | 2026-03-18 | 2026-09-10T03:19:47Z | foreign-state/legal-person aid restrictions; individual eligibility | https://cnccfp.fr/faq/le-mandataire-peut-il-accepter-un-don-en-provenance-de-letranger-existe-t-il-des-precautions-particulieres-dans-ce-cas/
SRC-014 | ◈ | fam:D | LDA-AIPAC-LD1-2015 | LDA LD-1 — American Israel Public Affairs Committee | 2015-10-01 | 2026-09-10T03:19:47Z | self-client; U.S. Middle East foreign policy lobbying | https://lda.gov/filings/public/filing/622ade04-65ca-4364-b78d-49e0dde1d4a5/print/
SRC-015 | ◈ | fam:D | LDA-AIPAC-2025Q4 | LDA LD-2 — AIPAC 2025 Q4 | 2026-01-15 | 2026-09-10T03:19:47Z | reported lobbying income/expenditure $973,910 | https://lda.gov/filings/public/filing/62a5b5e7-b60d-4dc7-a525-b0b2aa99d57f/print/
SRC-016 | ◈ | fam:E | LEVITT-JPE-1994 | Levitt 1994 — Using Repeat Challengers to Estimate Campaign Spending Effects | 1994-08-01 | 2026-09-10T03:19:47Z | repeat-challenger design; much smaller causal estimates than naive correlations | https://www.journals.uchicago.edu/doi/10.1086/261954
SRC-017 | ◈ | fam:E | JACOBSON-ES-2006 | Jacobson 2006 — Campaign spending effects in U.S. Senate elections | 2006-06-01 | 2026-09-10T03:19:47Z | challenger spending efficacy; strategic endogeneity caveat | https://www.sciencedirect.com/science/article/pii/S0261379405000569

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.fec.gov/data/committee/C00797670/ | A | 2021-12-15 | AIPAC PAC legal form | The FEC lists the American Israel Public Affairs Committee Political Action Committee as an active qualified membership-organization PAC and Lobbyist/Registrant PAC, registered 15 December 2021. | -
FCT-002 | FACT | ✧ | https://www.fec.gov/data/committee/C00797670/ | A | 2026-07-31 | AIPAC PAC current receipts | For 1 January 2025 through 31 July 2026, AIPAC PAC reported $50,061,505.47 in total receipts. | -
FCT-003 | FACT | ✧ | https://www.fec.gov/data/committee/C00797670/ | A | 2026-07-31 | AIPAC PAC current disbursements | For the same period AIPAC PAC reported $48,460,201.45 in total disbursements. | -
FCT-004 | FACT | ✧ | https://www.fec.gov/data/committee/C00797670/ | A | 2026-07-31 | AIPAC PAC transfer channel | AIPAC PAC reported $45,895,280 in contributions to other committees and $0 in independent expenditures for the 2025-2026 coverage period, showing a contribution channel distinct from UDP independent expenditures. | -
FCT-005 | FACT | ✧ | https://www.fec.gov/resources/campaign-finance-statistics/2024/tables/pac/PAC9a_2024_24m.pdf | A | 2025-03-14 | AIPAC PAC 2024 receipt rank | The FEC ranked AIPAC PAC first among membership PACs by receipts for 1 January 2023 through 31 December 2024, at $57,871,196. | -
FCT-006 | FACT | ✧ | https://www.fec.gov/resources/campaign-finance-statistics/2024/tables/pac/PAC4c_2024_18m.pdf | A | 2024-08-30 | AIPAC PAC 2024 contribution rank | The FEC ranked AIPAC PAC first among PACs by contributions to candidates and other committees for 1 January 2023 through 30 June 2024, at $39,745,931. | -
FCT-007 | FACT | ✧ | https://www.fec.gov/data/committee/C00799031/ | A | 2022-01-03 | UDP legal form | The FEC lists United Democracy Project as an active unauthorized independent-expenditure-only Super PAC, registered 3 January 2022. | -
FCT-008 | FACT | ✧ | https://www.fec.gov/data/committee/C00799031/ | A | 2026-07-31 | UDP current receipts | For 1 January 2025 through 31 July 2026 UDP reported $107,542,702.64 in total receipts. | -
FCT-009 | FACT | ✧ | https://www.fec.gov/data/committee/C00799031/ | A | 2026-07-31 | UDP current disbursements | For the same period UDP reported $77,208,509.82 in total disbursements. | -
FCT-010 | FACT | ✧ | https://www.fec.gov/data/committee/C00799031/ | A | 2026-07-31 | UDP independent expenditures | UDP reported $50,927,163.82 in independent expenditures and $9,931,200 in contributions to other committees for the current 2025-2026 coverage period. | -
FCT-011 | FACT | ✧ | https://docquery.fec.gov/pdf/708/202405229648717708/202405229648717708.pdf | A | 2024-05-21 | UDP Latimer support | A UDP Schedule E filing reports $105,194.72 for media production and $1,176,637 for media placement supporting George Latimer in the NY-16 Democratic primary on 21 May 2024. | -
FCT-012 | FACT | ✧ | https://docquery.fec.gov/pdf/708/202405229648717708/202405229648717708.pdf | A | 2024-05-21 | UDP Bowman opposition | The same UDP filing reports opposition spending against Jamaal Bowman, including a $1,176,637 media-placement entry, within a NY-16 calendar-year-to-date independent-expenditure total of $4,813,616.55 at that filing stage. | -
FCT-013 | FACT | ✧ | https://docquery.fec.gov/pdf/814/202406209652023814/202406209652023814_000001.pdf | A | 2024-06-19 | UDP Bowman late-cycle opposition | A 20 June FEC Schedule E reports $47,105.47 in direct-mail spending opposing Jamaal Bowman, with NY-16 calendar-year-to-date independent expenditures of $14,590,266.89. | -
FCT-014 | FACT | ✧ | https://docquery.fec.gov/pdf/814/202406209652023814/202406209652023814_000001.pdf | A | 2024-06-20 | UDP independence certification | The Bowman Schedule E certifies under penalty of perjury that the reported independent expenditures were not made in cooperation, consultation, concert, request or suggestion with the candidate or political party; this is a legal reporting assertion, not proof of every informal relationship beyond the filing. | -
FCT-015 | FACT | ✧ | https://rollcall.com/2024/06/25/bowman-ousted-in-new-york-primary-that-drew-millions-in-spending/ | other:rollcall | 2024-06-25 | NY16 election outcome | George Latimer defeated Jamaal Bowman in the NY-16 Democratic primary; Roll Call reported Latimer at about 58 percent and UDP spending $14.5 million in the race. | -
FCT-016 | FACT | ✧ | https://rollcall.com/2024/06/25/bowman-ousted-in-new-york-primary-that-drew-millions-in-spending/ | other:rollcall | 2024-06-25 | NY16 alternative explanations | The same contemporaneous account documents material rival explanations for the NY-16 outcome, including Latimer s long local incumbency and district roots, Bowman s censure/fire-alarm episode, his infrastructure-bill vote and district composition; the race therefore does not isolate UDP spending as the sole or marginal cause. | -
FCT-017 | FACT | ✧ | https://results.elections.ny.gov/contest/5580 | B | 2024-06-25 | NY16 official contestant control | The New York State Board of Elections official contest record identifies George S. Latimer and Jamaal A. Bowman as the Democratic candidates in Congressional District 16. | -
FCT-018 | FACT | ✧ | https://docquery.fec.gov/pdf/215/202407039652564215/202407039652564215.pdf | A | 2024-07-02 | UDP Bush opposition | A UDP Schedule E filing reports $49,900.63 in direct-mail spending opposing Cori Bush in Missouri District 1 on 2 July 2024. | -
FCT-019 | FACT | ✧ | https://docquery.fec.gov/pdf/215/202407039652564215/202407039652564215.pdf | A | 2024-07-02 | UDP Bell support | The same filing reports $165,914.10 in media-placement spending supporting Wesley Bell and a Missouri-01 calendar-year-to-date independent-expenditure total of $3,545,608.13. | -
FCT-020 | FACT | ✧ | https://docquery.fec.gov/pdf/195/202407249665725195/202407249665725195_000001.pdf | A | 2024-07-23 | UDP Missouri late-cycle spending | A 24 July Schedule E reports $300,000 supporting Wesley Bell and $700,000 opposing Cori Bush, with Missouri-01 calendar-year-to-date independent expenditures of $7,057,528.36. | -
FCT-021 | FACT | ✧ | https://www.sos.mo.gov/CMSImages/ElectionResultsStatistics/2024PrimaryElection.pdf | B | 2024-08-06 | Missouri primary result | Official Missouri results record Wesley Bell at 63,521 votes (51.1%) and Cori Bush at 56,723 (45.6%) in the Democratic primary for U.S. House District 1. | -
FCT-022 | FACT | ✧ | https://www.sos.mo.gov/CMSImages/ElectionResultsStatistics/2024PrimaryElection.pdf | A,B | 2024-08-06 | Missouri causal ceiling | The coexistence of large UDP expenditures and Bell s victory establishes exposure to a financed campaign intervention plus an electoral outcome, but the official result alone contains no counterfactual design isolating UDP s marginal causal contribution. | -
FCT-023 | FACT | ✧ | https://lda.gov/filings/public/filing/622ade04-65ca-4364-b78d-49e0dde1d4a5/print/ | D | 2015-10-01 | AIPAC lobbying registration | AIPAC registered under the Lobbying Disclosure Act as both registrant and client, describing its lobbying as focused on U.S. Middle East foreign policy. | -
FCT-024 | FACT | ✧ | https://lda.gov/filings/public/filing/62a5b5e7-b60d-4dc7-a525-b0b2aa99d57f/print/ | D | 2026-01-15 | AIPAC lobbying expenditure disclosure | AIPAC s 2025 fourth-quarter LD-2 filing reports $973,910 for its self-lobbying activity, documenting a professional direct-lobbying channel distinct from PAC and super-PAC election spending. | -
FCT-025 | FACT | ✧ | https://cnccfp.fr/faq/comment-le-candidat-peut-il-financer-sa-campagne/ | C | 2026-03-18 | France legal-person financing control | CNCCFP states that legal persons other than political parties or political groups may not finance a candidate s French election campaign or provide goods/services below customary prices. | -
FCT-026 | FACT | ✧ | https://cnccfp.fr/faq/comment-le-candidat-peut-il-financer-sa-campagne/ | C | 2026-03-18 | France individual-donation channel | CNCCFP identifies natural-person donations as an authorized campaign-finance source subject to French eligibility and limits; this is materially different from the U.S. PAC/Super-PAC architecture. | -
FCT-027 | FACT | ✧ | https://cnccfp.fr/faq/le-mandataire-peut-il-accepter-un-don-en-provenance-de-letranger-existe-t-il-des-precautions-particulieres-dans-ce-cas/ | C | 2026-03-18 | France foreign-source restriction | CNCCFP states that a foreign State or foreign legal person cannot directly or indirectly provide contributions or material assistance to a candidate campaign, while individual-donor eligibility turns on French nationality or residence rules. | -
FCT-028 | FACT | ✧ | https://cnccfp.fr/faq/comment-le-candidat-peut-il-financer-sa-campagne/ | A,C | 2026-03-18 | US-France structural non-isomorphism | French candidate-finance rules prohibit the legal-person financing channel used by U.S. PAC structures; therefore AIPAC/UDP is not mechanically transposable to France even though lobbying, advocacy and access can be compared functionally. | -
FCT-029 | FACT | ✧ | https://www.journals.uchicago.edu/doi/10.1086/261954 | E | 1994-08-01 | Campaign-spending identification control | Levitt s repeat-challenger design reports campaign-spending effects far smaller than ordinary cross-sectional estimates once fixed candidate and district factors are controlled, demonstrating severe endogeneity in naive spending-to-result inference. | -
FCT-030 | FACT | ✧ | https://www.sciencedirect.com/science/article/pii/S0261379405000569 | E | 2006-06-01 | Campaign-spending positive-effect control | Jacobson s panel analysis finds challenger expenditures can increase candidate knowledge/evaluations and support, while also emphasizing strategic spending and contributor endogeneity; spending can matter without making any single race result causally attributable from expenditure totals alone. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-001
FCT-005 | SRC-003
FCT-006 | SRC-004
FCT-007 | SRC-002
FCT-008 | SRC-002
FCT-009 | SRC-002
FCT-010 | SRC-002
FCT-011 | SRC-006
FCT-012 | SRC-006
FCT-013 | SRC-005
FCT-014 | SRC-005
FCT-015 | SRC-011
FCT-016 | SRC-011
FCT-017 | SRC-009
FCT-018 | SRC-007
FCT-019 | SRC-007
FCT-020 | SRC-008
FCT-021 | SRC-010
FCT-022 | SRC-007,SRC-008,SRC-010
FCT-023 | SRC-014
FCT-024 | SRC-015
FCT-025 | SRC-012
FCT-026 | SRC-012
FCT-027 | SRC-013
FCT-028 | SRC-001,SRC-002,SRC-012,SRC-013
FCT-029 | SRC-016
FCT-030 | SRC-017

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
FCT-029 | ELIGIBLE:VERIFIE
FCT-030 | ELIGIBLE:VERIFIE

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
FCT-029 | WRITE | -
FCT-030 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:search
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:facts
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:causal
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:verify
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:accountability
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:finalize

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-10T03:23:10.131838+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-029","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-030","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":30,"eligible":30,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:30;attempted:0;success:0;failure:0;blocked:30} | WRITEBACK_EXECUTION_V1:[30 rows, see section]

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
FCT-029 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-030 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
