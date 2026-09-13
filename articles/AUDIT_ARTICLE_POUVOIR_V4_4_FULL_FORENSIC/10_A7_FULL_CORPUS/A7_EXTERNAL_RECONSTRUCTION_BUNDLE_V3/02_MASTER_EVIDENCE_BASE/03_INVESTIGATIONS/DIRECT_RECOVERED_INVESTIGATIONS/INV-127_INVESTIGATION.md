ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260910-1143-soft-power-academic-cultural | PARENT_RUN_ID:NONE | AS_OF:2026-09-10
INPUT_KIND:RUN_CARD | MISSION_MODE:GREENFIELD | INPUT_REF:PATH:/mnt/data/inv127/runtime/investigations/2026-09/2026-09-10_soft-power-academic-cultural/2026-09-10_11-43_soft-power-academic-cultural_INPUT.md | SUBJECT_SLUG:soft-power-academic-cultural | SUBJECT_FP:sha256:0d2d50360a8fa5ac3857d48ed7f9fe8c1c65b3ac6574ca7ff053bc117c73d072 | INPUT_SHA256:sha256:69b80b0e5240c56543f2761e9d2e64c803f6bbe8673743db2ed3182ee54aea21
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France and European Union mainly 2010-2026; trace state/institution -> cultural or academic programme -> participant/public -> exposure/network/skill/attitude -> action or policy effect; bounded UK comparator only where it tests mechanism.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/NETWORK.md,clusters/INFORMATION.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Analytic body

## Object
INV-127 tests cultural and academic soft power through the chain state/institution -> budget/programme -> participant/public -> exposure, mobility or training -> network/skill/attitude -> political action -> specific decision. The central discipline is to stop at the strongest supported layer and not convert affinity, education or alumni status into tasking or capture.

## Deliberate influence infrastructure
France explicitly budgets and organises cultural and educational influence. Programme 185 reached EUR721.2m in 2024 [FCT-001]. The diplomatic cultural network is described by the MEAE as central to influence and spans services, institutes, Campus France branches and Alliances françaises [FCT-002]. Language and cultural exposure is large: French Institutes and Alliances together report well over one million language learners annually [FCT-003]. Institut français operational modes include mobility, residencies, professional networks, debates and cofunding [FCT-004]. This closes intent -> funded infrastructure -> exposure opportunity.

## Elite scholarships and alumni
France Excellence Eiffel is unusually explicit: it is designed to attract excellent international students and train future foreign public- and private-sector decision-makers [FCT-005]. Selection is institution-nominated and expert-jury based [FCT-006]. Campus France reported 347 laureates from 1,478 evaluated applications in 2021 and an institutional survey in which 84% of responding establishments treated the scheme as a major recruitment/cooperation instrument [FCT-007,FCT-008]. France Alumni then supplies durable relationship infrastructure at much larger scale: 687,000 current and former international students in more than 130 countries in July 2026, with events, information and professional networking explicitly intended to maintain links with France [FCT-009,FCT-010].

This is real elite formation and network maintenance. It is not evidence that France controls alumni. No source in the bounded corpus closes scholarship -> later French tasking -> specific foreign decision. The correct status is architecture supported, political decision causality unresolved.

## Erasmus: scale and exposure
Erasmus+ demonstrates the EU-scale version of the mechanism. In 2024 it had a EUR4.7bn budget, nearly 1.5m mobility participants, more than 34,400 projects and 85,600 organisations [FCT-011]. Since 1987 the programme reports more than 15m participants, with EUR26.2bn allocated for 2021-2027 [FCT-012]. EU material explicitly links the programme to objectives including European identity [FCT-013]. The 2019 higher-education impact study used almost 77,000 responses across a period with two million student/staff mobilities [FCT-014].

## Effects: skills and networks stronger than identity causality
The programme evaluation reports strong cross-cultural, career and internationalisation outcomes [FCT-015,FCT-016]. Independent evidence supports some effect classes: Mitchell's six-country panel found positive changes in European identification and linked them to transnational contact and European knowledge [FCT-017,FCT-018]. A propensity-score study across EU27 found a modest positive effect of international education mobility on environmental concern [FCT-022]. A UK alumni comparator likewise shows persistent social/professional ties years after study [FCT-023].

But the identity causal claim does not survive as a uniform result. Sigalas found no strengthening and possible adverse effects in a two-wave longitudinal design [FCT-019]. Kuhn attributes null results partly to selection and ceiling effects among students already likely to identify as European [FCT-020]. A 2024 pre-post study again found no substantial European-identity increase [FCT-021]. Therefore mobility -> contact/network/skills is substantially supported; mobility -> uniform European identity formation remains unresolved.

## From soft power to political action
The strongest general model is indirect: programmes change opportunity structures by creating exposure, skills, contacts, professional ties and sometimes attitudes. None of those is equivalent to a specific later policy decision. The bounded negative searches found no robust French participant-level chain identifying a scholarship or alumni relationship as the marginal cause of a later governmental decision. This is an absence of closure, not evidence of zero influence.

## Boundary with interference
EU governance sources provide a clean boundary. The European Parliament has documented concerns and specific cases involving foreign-state-linked cultural and academic entities, including Confucius Institutes [FCT-026,FCT-027]. The Commission's research-security framework defines foreign interference more narrowly: state-level activity must be coercive, covert, deceptive or corrupting and contrary to EU sovereignty, values or interests, while ordinary international academic cooperation remains legitimate and should be safeguarded through governance and due diligence [FCT-028,FCT-029]. Thus soft power is not interference by default; institution-specific control properties must be proven.

## Result
Cultural and academic soft power is materially real at the layers of policy intent, funded exposure, selective training, mobility, network formation and some bounded attitudinal effects. The evidence is much weaker when promoted to political alignment, tasking, capture or a specific decision. The robust model is exposure/relationship infrastructure with heterogeneous participant effects and substantial autonomy. Reopen only on named participant-to-decision footprints, stronger causal mobility designs, or authenticated institutional-control records where interference is alleged.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:7|SRC_COMPLETE:20/20

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-10
- **breaks:**
  - 2010-2015 competing Erasmus identity longitudinal evidence
  - 2019 Erasmus Higher Education Impact Study
  - 2022 EU foreign-interference research-security boundary
  - 2024-2026 scale-up and current French/EU network data
- **status:** CURRENT_PROGRAMMES_WITH_LONGITUDINAL_AND_POLICY_FOLLOWUP
- **window:** 2010-2026 with Erasmus historical scale since 1987

### MANIPULATION_REPORT
- **assumptions:**
  - official programme pages accurately state programme intent and scale
  - programme evaluations are evidence of reported outcomes but not automatically causal
  - peer-reviewed designs generalize only within their samples and outcomes
- **clusters:**
  - POWER
  - NETWORK
  - INFORMATION
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - soft power often works through exposure and relationships rather than commands
  - selection into elite/mobility programmes can mimic treatment effects
  - durable networks can exist without political alignment
  - academic openness and foreign-interference risk can coexist
- **input_kind:** RUN_CARD
- **mission_mode:** GREENFIELD
- **patterns:**
  - cultural diplomacy
  - elite scholarship
  - student mobility
  - language diffusion
  - alumni retention
  - professional networking
  - identity formation
  - attitude change
  - selection effect
  - academic interference boundary
- **priorities:**
  - map policy intent/resources
  - measure exposure/network scale
  - test longitudinal attitude effects
  - separate selection from treatment
  - seek participant-to-policy footprints
  - define interference boundary
- **query_guidance:** prefer official programme budgets/rules and independent longitudinal/quasi-experimental studies; require named participant-to-decision traces for political effects and coercive/covert/deceptive/corrupting evidence for interference
- **rhetorical:**
  - **AUTH:** MEAE/Campus France/European Commission/EEAS plus peer-reviewed longitudinal studies and EU governance sources
  - **BF:** no general participant-to-policy causal footprint
  - **DEM:** retain selection, self-report and rival-cause limits
  - **FAC:** separate infrastructure, treatment, attitudes and decisions
  - **NUM:** budgets, participant/network counts and study samples
- **speaker:**
  - **goal:** forensic separation of exposure, network, affinity, political action and tasking
  - **target:** institution -> programme -> participant -> exposure/network/attitude -> action/decision
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** state/institution
  - **S02:** budget
  - **S03:** programme
  - **S04:** selection
  - **S05:** participant/public
  - **S06:** exposure
  - **S07:** language/culture
  - **S08:** mobility
  - **S09:** network
  - **S10:** skill
  - **S11:** attitude
  - **S12:** affinity
  - **S13:** political action
  - **S14:** tasking/control
  - **S15:** counterfactual
- **threats:**
  - intent=effect
  - participation=alignment
  - network=coordination
  - affinity=tasking
  - education=indoctrination
  - identity=vote
  - alumni success=sponsor causality
  - state affiliation=interference

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - participant-level longitudinal decision footprints
  - **input_ids:**
    - FCT-009
    - FCT-010
    - FCT-011
    - FCT-022
    - FCT-023
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no generic network-to-policy causal trace
  - **not_computable:**
    - share of alumni later taking policy decisions because of programme
  - **operations_applied:**
    - mapped programme-to-network infrastructure
    - tested persistence versus political coordination
  - **reason:** separate durable ties from coordination
  - **result_ids:**
    - CLM-002
    - CLM-004
    - CAU-002
  - **status:** DONE
  - **trigger:** alumni, mobility and professional networks
- **item 2:**
  - **gaps:**
    - harmonised causal multi-country design
  - **input_ids:**
    - FCT-003
    - FCT-013
    - FCT-014
    - FCT-017
    - FCT-018
    - FCT-019
    - FCT-020
    - FCT-021
    - FCT-022
  - **module:** clusters/INFORMATION.md
  - **negative_results:**
    - no uniform Erasmus identity effect
  - **not_computable:**
    - general ideological treatment effect across participants
  - **operations_applied:**
    - compared longitudinal/pre-post findings
    - retained selection and ceiling effects
  - **reason:** separate exposure/contact from attitudinal and political effects
  - **result_ids:**
    - CLM-003
    - CLM-004
    - CAU-003
    - CAU-004
  - **status:** DONE
  - **trigger:** identity, language and attitude formation
- **item 3:**
  - **gaps:**
    - named decision footprints and authenticated control/tasking where alleged
  - **input_ids:**
    - FCT-005
    - FCT-006
    - FCT-009
    - FCT-010
    - FCT-025
    - FCT-026
    - FCT-028
    - FCT-029
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no generic scholarship/alumni-to-policy causality
    - state-linked culture alone insufficient for interference
  - **not_computable:**
    - marginal policy decisions caused by soft-power participation
  - **operations_applied:**
    - separated programme intent from decision effect
    - applied EU interference definition
  - **reason:** test influence architecture against tasking/capture
  - **result_ids:**
    - CLM-005
    - CLM-006
    - CLM-007
    - CAU-005
    - CAU-006
    - CAU-007
  - **status:** DONE
  - **trigger:** elite training, future decision-makers and interference claims

### SCOPING_REPORT
- **exclusions:**
  - participation=alignment
  - education=indoctrination
  - alumni network=coordination
  - attitude=policy action
  - state affiliation=interference
- **geo:** France and European Union mainly, bounded UK comparator
- **object_coverage:** HIGH_FOR_POLICY_INTENT_AND_EXPOSURE; HIGH_FOR_NETWORK_INFRASTRUCTURE; MODERATE_FOR_SKILL_AND_ATTITUDE_EFFECTS; LOW_FOR_POLICY_DECISION_CAUSALITY
- **object_question:** Par quels mécanismes universités, bourses, instituts culturels, échanges, langue et formation des élites produisent-ils du soft power, et quels effets durables sur réseaux, préférences ou décisions peuvent être démontrés sans confondre exposition culturelle, affinité, influence, recrutement et tasking ?
- **period:** mainly 2010-2026
- **subject:** Soft power culturel et académique : universités, bourses, instituts, échanges, langue, culture et formation des élites

### CREDO
- participation != alignment
- affinity != tasking
- education != indoctrination
- network != coordination
- attitude != policy action
- programme intent != measured effect
- selection != causality
- soft power != interference

### COGNITIVE_MAP
- **continuum:**
  - foreign-policy/identity objective
  - budget/institution
  - programme and selection
  - exposure/mobility
  - network/skill
  - attitude/affinity
  - political action
  - specific decision
  - tasking/control/interference
- **core_model:** Cultural and academic soft power is best evidenced as deliberately funded exposure, mobility, skill and relationship infrastructure. It can generate durable networks and some bounded attitudinal effects, but the promotion from exposure or affinity to political alignment, decision causality or tasking requires separate evidence and is usually unclosed.
- **rival_models:**
  - soft power is purely symbolic
  - any scholarship recipient becomes aligned with sponsor
  - Erasmus automatically creates European identity
  - all foreign cultural institutes are benign cooperation
  - all state-linked cultural institutes are interference

### DIALECTICAL_MAP
- **antithesis:** Participants self-select, retain autonomy, identity effects are inconsistent and later political decisions are multicausal; networks and affinity do not prove tasking.
- **synthesis:** Soft power is materially real at exposure/network/attitude layers, but policy capture or interference requires actor-specific control/causal evidence beyond programme participation.
- **thesis:** States and the EU deliberately invest in education, language, culture, mobility and alumni networks because these create influence-relevant exposure, skills, relationships and affinity.

### RESOURCE_FLOW_MAP
- **flows:**
  - French programme 185 funds cultural/influence infrastructure
  - MEAE/Campus France -> Eiffel scholarship selection/training
  - EU Erasmus+ budget -> organisations -> mobility cohorts
  - higher-education/cultural experience -> alumni and professional networks
- **limits:**
  - self-financing and institutional autonomy vary across networks
  - programme budget does not measure persuasion
  - alumni membership is self-selected
  - political effect lacks participant-level denominator/counterfactual

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** French MEAE / cultural network
  - **relation:** funds and coordinates influence, language, cultural and higher-education attraction tools
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
    - FCT-004
  - **to:** foreign publics, students and professionals
- **item 2:**
  - **from:** MEAE / Campus France
  - **relation:** selects/manages Eiffel scholarship and alumni relationship infrastructure
  - **support:**
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-009
    - FCT-010
  - **to:** international students and alumni
- **item 3:**
  - **from:** European Union / Erasmus+
  - **relation:** funds mobility and cross-border institutional network
  - **support:**
    - FCT-011
    - FCT-012
    - FCT-013
    - FCT-014
  - **to:** students, staff and organisations
- **item 4:**
  - **from:** participants/alumni
  - **relation:** form cross-border social/professional ties and potentially change skills/attitudes
  - **support:**
    - FCT-014
    - FCT-017
    - FCT-018
    - FCT-022
    - FCT-023
  - **to:** later personal/professional environments
- **item 5:**
  - **from:** foreign state-linked academic/cultural entities
  - **relation:** cooperation or, when coercive/covert/deceptive/corrupting control is evidenced, interference risk
  - **support:**
    - FCT-026
    - FCT-027
    - FCT-028
    - FCT-029
  - **to:** European higher-education institutions

### IMPACT_MAP
- **established:**
  - large-scale cultural/language/academic exposure infrastructure
  - selective elite scholarship architecture
  - large alumni and mobility networks
  - cross-cultural skill and career/network outcomes in programme evaluations
  - bounded attitudinal effects in some independent studies
  - institution-specific foreign-interference safeguards and concerns
- **not_established:**
  - generic scholarship/alumni -> specific sponsor-favourable policy decision
  - affinity -> recruitment/tasking
  - network -> coordination
  - general soft-power -> capture
  - all foreign cultural institutes -> interference
- **partial:**
  - European identity change from Erasmus
  - magnitude/durability of attitudinal effects across populations
  - independence of programme evaluation estimates from selection/self-report

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** Sigalas longitudinal, Kuhn selection/ceiling account and 2024 pre-post study find null/adverse or no substantial effect
  - **issue:** Erasmus identity effect
  - **pro:** Mitchell panel and Commission-commissioned evaluation report positive association/change
  - **resolution:** EXPOSURE_CONTACT_SUPPORTED_UNIFORM_IDENTITY_CAUSALITY_UNRESOLVED
  - **support:**
    - FCT-014
    - FCT-017
    - FCT-018
    - FCT-019
    - FCT-020
    - FCT-021
- **item 2:**
  - **contra:** no named later policy decision is causally linked to scholarship or French tasking in this run
  - **issue:** elite scholarship as influence
  - **pro:** Eiffel explicitly targets future foreign decision-makers and France maintains alumni infrastructure
  - **resolution:** ELITE_TRAINING_NETWORK_SUPPORTED_POLICY_CONTROL_UNRESOLVED
  - **support:**
    - FCT-005
    - FCT-006
    - FCT-009
    - FCT-010
- **item 3:**
  - **contra:** Commission definition requires coercive/covert/deceptive/corrupting state-level activity and safeguards ordinary international cooperation
  - **issue:** soft power versus interference
  - **pro:** EU Parliament documents concerns and institution-specific cases involving state-linked academic/cultural entities
  - **resolution:** CASE_SPECIFIC_INTERFERENCE_POSSIBLE_GENERIC_EQUIVALENCE_REFUTED
  - **support:**
    - FCT-026
    - FCT-027
    - FCT-028
    - FCT-029

### VERIFICATION_REPORT
- **downgraded:**
  - programme intent means measured influence
  - participation means alignment
  - alumni network means coordination
  - European identity association means indoctrination
  - future decision-maker training means tasking
  - state-linked cultural institute means interference
- **fact_count:** 29
- **negative_controls:**
  - conflicting Erasmus identity panel/pre-post evidence
  - selection/ceiling effect
  - no France scholarship/alumni-to-specific-policy causal footprint
  - foreign-interference definition excludes ordinary open cooperation
- **provenance_families:** 5
- **query_count:** 24
- **source_count:** 20
- **verification:** 29 bounded facts linked to 20 accepted sources across French official programme data, EU programme data, peer-reviewed longitudinal/quasi-experimental research, a UK comparator and EU foreign-interference governance sources, plus four explicit negative searches.

### EDI_REPORT
- **corpus:**
  - **limits:**
    - no participant-level French alumni policy-decision causal design
    - mixed Erasmus identity evidence
    - programme evaluations partly rely on self-report/selection
    - no generic denominator for foreign academic influence
  - **strength:** current French/EU official programme architecture plus multiple independent longitudinal/pre-post/quasi-experimental studies and governance boundary sources
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
  - **owner:** state/EU programme sponsor, host institution and participant depending stage
  - **perspective:** resources, exposure, networks, skills, attitudes, political action, control
  - **stratification:** institution -> programme -> participant -> exposure/network -> attitude -> action -> decision
  - **temporal:** 2010-2026 with Erasmus historical scale since 1987
- **edi:**
  - **coverage:** HIGH_FOR_POLICY_INTENT_AND_INFRASTRUCTURE; HIGH_FOR_EXPOSURE_AND_NETWORK_SCALE; MODERATE_FOR_ATTITUDE_EFFECTS; LOW_FOR_POLICY_DECISION_CAUSALITY
  - **independence:** STRONG_MIX_OF_OFFICIAL_PROGRAMME_DATA_AND_INDEPENDENT_ACADEMIC_COUNTEREVIDENCE
- **source_counts:**
  - **A:** 7
  - **B:** 4
  - **C:** 5
  - **D:** 2
  - **E:** 2
  - **total:** 20

### RESPONSIBILITY_MAP
- **Eiffel_selection:** MEAE-designed, institution-nominated and expert-jury scholarship for future foreign decision-makers
- **Erasmus:** EU-funded mobility/institutional programme with identity/cooperation objectives; participant attitude effect heterogeneous
- **France_Alumni:** Campus France relationship-maintenance infrastructure; political alignment not established
- **French_cultural_policy:** MEAE programme 185 and diplomatic/cultural network set explicit influence/attractiveness objectives
- **foreign_interference_boundary:** state linkage plus coercive/covert/deceptive/corrupting conduct or concrete institutional control required; ordinary cooperation excluded
- **participant_actions:** individual autonomy retained; later political decisions multicausal unless specific trace exists

### NEXT_QUERIES
- For Eiffel/France Alumni, seek named alumni who later held public decision roles and reconstruct programme participation -> subsequent French institutional contact -> identifiable decision, retaining rival explanations.
- For Erasmus identity effects, prioritize recent multi-country panel, regression-discontinuity or eligibility-threshold designs with pre-treatment identity and non-mobile controls.
- For cultural institutes, obtain contracts/MOUs, curriculum-control clauses, funding rights and documented interventions before classifying influence as interference.
- Do not infer tasking or capture from alumni prominence, affinity, language competence or repeated network contact alone.

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009 | support:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013 | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-006,QRY-007,QRY-010,QRY-011,QRY-017,QRY-018 | support:FCT-008,FCT-009,FCT-010,FCT-014,FCT-015,FCT-016,FCT-022,FCT-023,FCT-024,FCT-025 | counter:- | results:FCT-008,FCT-009,FCT-010,FCT-014,FCT-015,FCT-016,FCT-022,FCT-023,FCT-024,FCT-025 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-023 | support:FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021,FCT-022 | counter:- | results:FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021,FCT-022 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-005,QRY-007,QRY-018,QRY-019,QRY-020,QRY-021,QRY-022,QRY-024 | support:FCT-005,FCT-006,FCT-009,FCT-010,FCT-023,FCT-024,FCT-025,FCT-026,FCT-027,FCT-028,FCT-029 | counter:- | results:FCT-005,FCT-006,FCT-009,FCT-010,FCT-023,FCT-024,FCT-025,FCT-026,FCT-027,FCT-028,FCT-029 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,QRY-002,QRY-004,QRY-005,QRY-008,QRY-009,QRY-018,SRC-001,SRC-002,SRC-004,SRC-005,SRC-008,SRC-009,SRC-018 | support:FCT-001,FCT-002,FCT-004,FCT-005,FCT-011,FCT-013,FCT-025 | counter:CTRL-001 | results:FCT-001,FCT-002,FCT-004,FCT-005,FCT-011,FCT-013,FCT-025,CTRL-001 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-002,QRY-003,QRY-007,QRY-008,QRY-009,QRY-016,SRC-002,SRC-003,SRC-007,SRC-008,SRC-009,SRC-016 | support:FCT-002,FCT-003,FCT-009,FCT-010,FCT-011,FCT-012,FCT-022 | counter:CTRL-002 | results:FCT-002,FCT-003,FCT-009,FCT-010,FCT-011,FCT-012,FCT-022,CTRL-002 | final:SUPPORTED | gap:EFFECT
CLM-003 | attempts:QRY-009,QRY-010,QRY-012,QRY-013,QRY-014,QRY-015,SRC-009,SRC-010,SRC-012,SRC-013,SRC-014,SRC-015 | support:FCT-013,FCT-014,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021 | counter:CTRL-003 | results:FCT-013,FCT-014,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021,CTRL-003 | final:PARTIAL | gap:CAUSALITY
CLM-004 | attempts:QRY-010,QRY-011,QRY-016,QRY-017,SRC-010,SRC-011,SRC-016,SRC-017 | support:FCT-014,FCT-015,FCT-016,FCT-022,FCT-023 | counter:CTRL-004 | results:FCT-014,FCT-015,FCT-016,FCT-022,FCT-023,CTRL-004 | final:SUPPORTED | gap:EXTERNAL_VALIDITY
CLM-005 | attempts:QRY-005,QRY-006,QRY-007,SRC-005,SRC-006,SRC-007 | support:FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010 | counter:CTRL-005 | results:FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,CTRL-005 | final:SUPPORTED | gap:CAUSALITY
CLM-006 | attempts:QRY-005,QRY-007,QRY-012,QRY-016,QRY-018,QRY-019,QRY-020,SRC-005,SRC-007,SRC-012,SRC-016,SRC-018,SRC-019,SRC-020 | support:FCT-005,FCT-010,FCT-017,FCT-022,FCT-025,FCT-026,FCT-028 | counter:CTRL-006 | results:FCT-005,FCT-010,FCT-017,FCT-022,FCT-025,FCT-026,FCT-028,CTRL-006 | final:PARTIAL | gap:RESPONSIBILITY
CLM-007 | attempts:QRY-019,QRY-020,SRC-019,SRC-020 | support:FCT-026,FCT-027,FCT-028,FCT-029 | counter:CTRL-007 | results:FCT-026,FCT-027,FCT-028,FCT-029,CTRL-007 | final:SUPPORTED | gap:SCOPE

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-002 | CLM | SUPPORTED | EFFECT | Network membership and exposure do not establish political alignment or action.
CLM-003 | CLM | PARTIAL | CAUSALITY | Longitudinal and recent pre-post studies conflict, and participant self-selection/ceiling effects are material.
CLM-004 | CLM | SUPPORTED | EXTERNAL_VALIDITY | Programme evaluations and alumni surveys have self-selection and self-report limits; effect magnitude is not uniform.
CLM-005 | CLM | SUPPORTED | CAUSALITY | No bounded evidence in this run links participation to a later specific foreign-policy decision or tasking by France.
CLM-006 | CLM | PARTIAL | RESPONSIBILITY | No authenticated order/control chain or participant-to-policy causal design supports a general promotion from affinity/network to tasking/capture.
CLM-007 | CLM | SUPPORTED | SCOPE | Institution-specific attribution remains necessary; policy concern is not proof for every programme.
CAU-003 | CAU | UNRESOLVED | CAUSALITY | Need harmonised multi-country longitudinal or quasi-experimental estimates with pre-treatment identity and non-mobile controls.
CAU-006 | CAU | UNRESOLVED | CAUSALITY | Need named participant, programme participation, later decision trace, sponsor interaction/tasking evidence where alleged, and rival-cause control.

SEMANTIC_COUNTS_V1:LED:0|CLM:7|AXS:4|CAU:7|CTRL:8|ACT:4

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"France and the EU deliberately fund cultural, language, scholarship and mobility infrastructures as instruments of influence, attractiveness, cooperation or European identity formation.","claimant":"INV-127 synthesis","counter":"CTRL-001","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-004","FCT-005","FCT-011","FCT-013","FCT-025"]}
CLM-002 | {"claim":"These programmes reliably create large-scale exposure and durable network infrastructure through institutes, mobility cohorts and alumni platforms.","claimant":"INV-127 synthesis","counter":"CTRL-002","gap":"Network membership and exposure do not establish political alignment or action.","gap_type":"EFFECT","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-002","FCT-003","FCT-009","FCT-010","FCT-011","FCT-012","FCT-022"]}
CLM-003 | {"claim":"Erasmus participation reliably and uniformly increases European identity across participants.","claimant":"INV-127 synthesis","counter":"CTRL-003","gap":"Longitudinal and recent pre-post studies conflict, and participant self-selection/ceiling effects are material.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-013","FCT-014","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021"]}
CLM-004 | {"claim":"International academic mobility can produce durable skills, career internationalisation and persistent social/professional ties.","claimant":"INV-127 synthesis","counter":"CTRL-004","gap":"Programme evaluations and alumni surveys have self-selection and self-report limits; effect magnitude is not uniform.","gap_type":"EXTERNAL_VALIDITY","materiality":"HIGH","status":"SUPPORTED","support":["FCT-014","FCT-015","FCT-016","FCT-022","FCT-023"]}
CLM-005 | {"claim":"France Excellence Eiffel and France Alumni form a deliberate elite-training and relationship-maintenance architecture aimed at future foreign decision-makers.","claimant":"INV-127 synthesis","counter":"CTRL-005","gap":"No bounded evidence in this run links participation to a later specific foreign-policy decision or tasking by France.","gap_type":"CAUSALITY","materiality":"HIGH","status":"SUPPORTED","support":["FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010"]}
CLM-006 | {"claim":"Soft-power participation or affinity can be promoted directly into evidence of recruitment, coordination, tasking or policy capture.","claimant":"INV-127 synthesis","counter":"CTRL-006","gap":"No authenticated order/control chain or participant-to-policy causal design supports a general promotion from affinity/network to tasking/capture.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-005","FCT-010","FCT-017","FCT-022","FCT-025","FCT-026","FCT-028"]}
CLM-007 | {"claim":"Academic and cultural cooperation crosses from soft power into foreign interference only when additional properties such as state linkage plus coercive, covert, deceptive or corrupting control are established; ordinary cooperation is not interference by definition.","claimant":"INV-127 synthesis","counter":"CTRL-007","gap":"Institution-specific attribution remains necessary; policy concern is not proof for every programme.","gap_type":"SCOPE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-026","FCT-027","FCT-028","FCT-029"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009"],"axis":"policy_resources_and_exposure","inv_id":"INV-127","links":["INV-127"],"question":"How do states/EU convert budgets, cultural networks, scholarships and mobility programmes into exposure and durable network infrastructure?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013"],"sought_objects":["budget","institutes","language learners","scholarships","mobility","alumni networks"],"status":"SATURATED","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013"]}
AXS-002 | {"attempt_ids":["QRY-006","QRY-007","QRY-010","QRY-011","QRY-017","QRY-018"],"axis":"participant_network_skill_effects","inv_id":"INV-127","links":["INV-127"],"question":"What durable network, skill or career effects are observed after academic/cultural mobility?","result_ids":["FCT-008","FCT-009","FCT-010","FCT-014","FCT-015","FCT-016","FCT-022","FCT-023","FCT-024","FCT-025"],"sought_objects":["cross-cultural skill","career","international network","alumni retention","language competence"],"status":"SATURATED","support":["FCT-008","FCT-009","FCT-010","FCT-014","FCT-015","FCT-016","FCT-022","FCT-023","FCT-024","FCT-025"]}
AXS-003 | {"attempt_ids":["QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-023"],"axis":"attitudes_identity_causality","inv_id":"INV-127","links":["INV-127"],"question":"Does mobility causally alter European identity or other attitudes, and how stable is the result across designs?","result_ids":["FCT-014","FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021","FCT-022"],"sought_objects":["panel","pre-post","selection bias","propensity score","identity","attitude"],"status":"SATURATED","support":["FCT-014","FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021","FCT-022"]}
AXS-004 | {"attempt_ids":["QRY-005","QRY-007","QRY-018","QRY-019","QRY-020","QRY-021","QRY-022","QRY-024"],"axis":"soft_power_to_policy_and_interference_boundary","inv_id":"INV-127","links":["INV-127"],"question":"When can soft-power exposure be linked to political action, tasking or interference rather than affinity or network formation?","result_ids":["FCT-005","FCT-006","FCT-009","FCT-010","FCT-023","FCT-024","FCT-025","FCT-026","FCT-027","FCT-028","FCT-029"],"sought_objects":["future decision-makers","policy action","tasking","academic freedom","coercion","covert control"],"status":"SATURATED","support":["FCT-005","FCT-006","FCT-009","FCT-010","FCT-023","FCT-024","FCT-025","FCT-026","FCT-027","FCT-028","FCT-029"]}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"direct programme-delivery chain","counter":"CTRL-001","limit":"Exposure is not alignment.","mechanism":"public budget/institutional mandate -> scholarship, institute, exchange or language programme -> participant/public exposure","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-011"]}
CAU-002 | {"causal_right":"proximal human-capital/network effect","counter":"CTRL-002","limit":"Persistent ties vary and can reflect selection into mobility/alumni networks.","mechanism":"academic/cultural programme -> repeated contact, skills and alumni/professional network formation","status":"SUPPORTED","support":["FCT-009","FCT-010","FCT-014","FCT-015","FCT-016","FCT-022"]}
CAU-003 | {"counter":"CTRL-003","gap":"Need harmonised multi-country longitudinal or quasi-experimental estimates with pre-treatment identity and non-mobile controls.","gap_type":"CAUSALITY","limit":"Conflicting panel/pre-post evidence and ceiling/selection effects prevent a uniform causal conclusion.","mechanism":"Erasmus mobility -> stronger European identity","status":"UNRESOLVED","support":["FCT-013","FCT-014","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021"]}
CAU-004 | {"causal_right":"bounded attitudinal effect under propensity-score design","counter":"CTRL-004","limit":"One attitude domain and observational matching do not establish broad ideological or policy alignment.","mechanism":"international education mobility -> modest increase in environmental concern","status":"SUPPORTED","support":["FCT-022"]}
CAU-005 | {"causal_right":"selection/training/network architecture","counter":"CTRL-005","limit":"Architecture and intent do not establish later decision causality.","mechanism":"Eiffel elite scholarship -> future decision-maker training + France Alumni retention infrastructure","status":"SUPPORTED","support":["FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010"]}
CAU-006 | {"counter":"CTRL-006","gap":"Need named participant, programme participation, later decision trace, sponsor interaction/tasking evidence where alleged, and rival-cause control.","gap_type":"CAUSALITY","limit":"No participant-level policy footprint or counterfactual decision effect identified.","mechanism":"scholarship/cultural exposure or alumni affinity -> specific later policy decision favorable to sponsor state","status":"UNRESOLVED","support":["FCT-005","FCT-009","FCT-010","FCT-023","FCT-024"]}
CAU-007 | {"causal_right":"definition and institution-specific governance boundary","counter":"CTRL-007","limit":"State affiliation or cultural promotion alone does not satisfy the interference definition.","mechanism":"state-linked academic/cultural presence + coercive/covert/deceptive/corrupting control -> foreign interference risk/action","status":"SUPPORTED","support":["FCT-026","FCT-027","FCT-028","FCT-029"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Participation or exposure does not equal political alignment, and affinity does not equal tasking.","status":"DONE","support":["FCT-010","FCT-017","FCT-020","FCT-022"]}
CTRL-002 | {"control":"Network persistence establishes relationship infrastructure, not coordination or policy influence.","status":"DONE","support":["FCT-009","FCT-010","FCT-022","FCT-023"]}
CTRL-003 | {"control":"Erasmus identity evidence is mixed across longitudinal/pre-post designs; Commission programme evaluations cannot be treated as causal consensus.","status":"DONE","support":["FCT-014","FCT-017","FCT-019","FCT-020","FCT-021"]}
CTRL-004 | {"control":"Selection into mobility and already-European attitudes can inflate apparent programme effects.","status":"DONE","support":["FCT-019","FCT-020"]}
CTRL-005 | {"control":"Eiffel objective to train future decision-makers is programme intent and selection architecture, not proof of later French control over alumni decisions.","status":"DONE","support":["FCT-005","FCT-006","FCT-007","FCT-008"]}
CTRL-006 | {"control":"Education and language learning are not indoctrination by default; skill, identity and policy action are separate outcomes.","status":"DONE","support":["FCT-003","FCT-014","FCT-021","FCT-022"]}
CTRL-007 | {"control":"Foreign interference requires additional coercive/covert/deceptive/corrupting properties; state linkage or cultural presence alone is insufficient.","status":"DONE","support":["FCT-026","FCT-028","FCT-029"]}
CTRL-008 | {"control":"Institution-specific academic-freedom concerns around Confucius Institutes cannot be generalized to all foreign cultural institutes or all participants.","status":"DONE","support":["FCT-026","FCT-027","FCT-028"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Separate programme intent, exposure, network formation, attitude change, political action and tasking into distinct evidentiary layers.","actor":"routing/control plane","intent":"prevent soft-power causal inflation","status":"DONE","support":["FCT-001","FCT-010","FCT-013","FCT-026"]}
ACT-002 | {"action":"Treat French cultural/Eiffel/France Alumni infrastructure as a deliberate influence and relationship architecture while leaving participant-to-policy causality unresolved.","actor":"routing/control plane","intent":"preserve intent/effect boundary","status":"DONE","support":["FCT-001","FCT-005","FCT-009","FCT-010"]}
ACT-003 | {"action":"Use conflicting Erasmus longitudinal/pre-post evidence as a mandatory control against claims of automatic identity formation.","actor":"routing/control plane","intent":"causal discipline","status":"DONE","support":["FCT-017","FCT-019","FCT-020","FCT-021"]}
ACT-004 | {"action":"Classify academic/cultural activity as interference only with institution-specific evidence meeting coercive/covert/deceptive/corrupting criteria or concrete academic-control evidence.","actor":"routing/control plane","intent":"soft-power/interference boundary","status":"DONE","support":["FCT-026","FCT-027","FCT-028","FCT-029"]}

SEARCH_ACTIVITY_V1:WEB:4|FETCH:20|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL | mnemo | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/le-budget-2024-du-ministere-de-l-europe-et-des-affaires-etrangeres-un-budget-en-hausse-de-plus-de-6 | FETCH FR-MEAE-BUDGET-2024
QRY-002 | FETCH | FOUND | SRC-002 | https://www.diplomatie.gouv.fr/fr/le-ministere-et-son-reseau/les-metiers-de-la-diplomatie/un-reseau-diplomatique-essentiel-a-la-politique-etrangere-de-la-france/le-reseau-de-cooperation-et-d-action-culturelle-et-ses-metiers/article/qui-sont-les-conseillers-et-conseilleres-de-cooperation-et-d-action-culturelle | FETCH FR-MEAE-NETWORK-2026
QRY-003 | FETCH | FOUND | SRC-003 | https://www.diplomatie.gouv.fr/fr/le-ministere-en-action/assurer-la-presence-de-la-culture-francaise/defendre-la-francophonie-et-la-langue-francaise/engagement-de-la-france-pour-la-diversite-linguistique-et-la-langue-francaise/enseigner-et-apprendre-le-francais | FETCH FR-MEAE-LANGUAGE-NETWORK
QRY-004 | FETCH | FOUND | SRC-004 | https://www.institutfrancais.com/fr | FETCH INSTITUT-FRANCAIS-ACTIONS
QRY-005 | FETCH | FOUND | SRC-005 | https://www.campusfrance.org/fr/le-programme-de-bourses-france-excellence-eiffel | FETCH CAMPUSFRANCE-EIFFEL-2026
QRY-006 | FETCH | FOUND | SRC-006 | https://rapportactivite2021.campusfrance.org/ | FETCH CAMPUSFRANCE-RA2021
QRY-007 | FETCH | FOUND | SRC-007 | https://www.campusfrance.org/fr/reseau-France-Alumni | FETCH FRANCE-ALUMNI-2026
QRY-008 | FETCH | FOUND | SRC-008 | https://erasmus-plus.ec.europa.eu/nl/news/almost-15-million-people-went-on-an-erasmus-mobility-in-2024-according-to-latest-report | FETCH ERASMUS-2024-FIGURES
QRY-009 | FETCH | FOUND | SRC-009 | https://erasmus-plus.ec.europa.eu/whats-new/news/marking-37-years-of-erasmus-key-numbers-and-achievements | FETCH ERASMUS-37-YEARS
QRY-010 | FETCH | FOUND | SRC-010 | https://op.europa.eu/en/publication-detail/-/publication/94d97f5c-7ae2-11e9-9f05-01aa75ed71a1/language-en | FETCH EU-ERASMUS-IMPACT-2019
QRY-011 | FETCH | FOUND | SRC-011 | https://www.eeas.europa.eu/node/63171_en | FETCH EEAS-ERASMUS-IMPACT-2019
QRY-012 | FETCH | FOUND | SRC-012 | https://onlinelibrary.wiley.com/doi/10.1111/jcms.12152 | FETCH MITCHELL-ERASMUS-2015
QRY-013 | FETCH | FOUND | SRC-013 | https://journals.sagepub.com/doi/10.1177/1465116510363656 | FETCH SIGALAS-ERASMUS-2010
QRY-014 | FETCH | FOUND | SRC-014 | https://onlinelibrary.wiley.com/doi/10.1111/j.1468-5965.2012.02286.x | FETCH KUHN-ERASMUS-2012
QRY-015 | FETCH | FOUND | SRC-015 | https://www.tandfonline.com/doi/full/10.1080/01434632.2024.2357716 | FETCH MOCANU-LLURDA-2024
QRY-016 | FETCH | FOUND | SRC-016 | https://doi.org/10.1177/10283153241235698 | FETCH DIPIETRO-MOBILITY-2024
QRY-017 | FETCH | FOUND | SRC-017 | https://www.britishcouncil.org/research-insight/alumni-voices-2025-uk-graduates-global-influence | FETCH BC-ALUMNI-2025
QRY-018 | FETCH | FOUND | SRC-018 | https://www.britishcouncil.org/research-insight/soft-power-cultural-relations-comparative-analysis-2024 | FETCH BC-SOFTPOWER-2024
QRY-019 | FETCH | FOUND | SRC-019 | https://www.europarl.europa.eu/doceo/document/A-9-2022-0022_EN.html | FETCH EP-FOREIGN-INTERFERENCE-2022
QRY-020 | FETCH | FOUND | SRC-020 | https://research-and-innovation.ec.europa.eu/news/all-research-and-innovation-news/commission-publishes-toolkit-help-mitigate-foreign-interference-research-and-innovation-2022-01-18_en | FETCH EC-RI-INTERFERENCE-TOOLKIT-2022
QRY-021 | WEB | NON_TROUVE | - | - | France Eiffel scholarship alumni specific later minister vote policy decision caused by scholarship causal evidence
QRY-022 | WEB | NON_TROUVE | - | - | France Alumni network causal effect on foreign government policy decision longitudinal counterfactual
QRY-023 | WEB | NON_TROUVE | - | - | Erasmus exchange automatic indoctrination European identity robust causal consensus longitudinal null study
QRY-024 | WEB | NON_TROUVE | - | - | cultural institute participation France EU recruitment tasking participants by sponsor state authenticated evidence general model

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | FR-MEAE-BUDGET-2024 | Budget 2024 du MEAE | 2023-10-01 | 2026-09-10T09:46:17Z | programme 185 diplomatie culturelle et influence, EUR721.2m | https://www.diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/le-budget-2024-du-ministere-de-l-europe-et-des-affaires-etrangeres-un-budget-en-hausse-de-plus-de-6
SRC-002 | ◈ | fam:A | FR-MEAE-NETWORK-2026 | Réseau de coopération et action culturelle | 2026-04-28 | 2026-09-10T09:46:17Z | network explicitly at heart of influence; SCAC, institutes, Campus France, Alliances | https://www.diplomatie.gouv.fr/fr/le-ministere-et-son-reseau/les-metiers-de-la-diplomatie/un-reseau-diplomatique-essentiel-a-la-politique-etrangere-de-la-france/le-reseau-de-cooperation-et-d-action-culturelle-et-ses-metiers/article/qui-sont-les-conseillers-et-conseilleres-de-cooperation-et-d-action-culturelle
SRC-003 | ◈ | fam:A | FR-MEAE-LANGUAGE-NETWORK | Enseigner et apprendre le français | 2025-01-01 | 2026-09-10T09:46:17Z | language-learning reach of institutes and Alliances | https://www.diplomatie.gouv.fr/fr/le-ministere-en-action/assurer-la-presence-de-la-culture-francaise/defendre-la-francophonie-et-la-langue-francaise/engagement-de-la-france-pour-la-diversite-linguistique-et-la-langue-francaise/enseigner-et-apprendre-le-francais
SRC-004 | ◈ | fam:A | INSTITUT-FRANCAIS-ACTIONS | Institut français - modalités action | 2026-09-10 | 2026-09-10T09:46:17Z | mobility, residencies, professional networks, debates and cofunding | https://www.institutfrancais.com/fr
SRC-005 | ◈ | fam:A | CAMPUSFRANCE-EIFFEL-2026 | Programme France Excellence Eiffel | 2025-09-30 | 2026-09-10T09:46:17Z | attract top students and train future foreign decision-makers | https://www.campusfrance.org/fr/le-programme-de-bourses-france-excellence-eiffel
SRC-006 | ◈ | fam:A | CAMPUSFRANCE-RA2021 | Campus France rapport activité 2021 | 2022-01-01 | 2026-09-10T09:46:17Z | Eiffel selection and institutional impact study | https://rapportactivite2021.campusfrance.org/
SRC-007 | ◈ | fam:A | FRANCE-ALUMNI-2026 | Réseau France Alumni | 2026-07-31 | 2026-09-10T09:46:17Z | 687k current/former international students in >130 countries; maintain ties and networks | https://www.campusfrance.org/fr/reseau-France-Alumni
SRC-008 | ◈ | fam:B | ERASMUS-2024-FIGURES | Erasmus+ 2024 headline figures | 2025-11-14 | 2026-09-10T09:46:17Z | EUR4.7bn; 1.5m mobility; 34,400 projects; 85,600 organisations | https://erasmus-plus.ec.europa.eu/nl/news/almost-15-million-people-went-on-an-erasmus-mobility-in-2024-according-to-latest-report
SRC-009 | ◈ | fam:B | ERASMUS-37-YEARS | 37 years Erasmus+ key numbers | 2024-06-17 | 2026-09-10T09:46:17Z | >15m participants; EUR26.2bn 2021-27; European identity objective | https://erasmus-plus.ec.europa.eu/whats-new/news/marking-37-years-of-erasmus-key-numbers-and-achievements
SRC-010 | ◈ | fam:B | EU-ERASMUS-IMPACT-2019 | Erasmus+ Higher Education Impact Study | 2019-05-17 | 2026-09-10T09:46:17Z | ~77k responses; 2m students/staff mobility 2014-2018 | https://op.europa.eu/en/publication-detail/-/publication/94d97f5c-7ae2-11e9-9f05-01aa75ed71a1/language-en
SRC-011 | ◈ | fam:B | EEAS-ERASMUS-IMPACT-2019 | EEAS summary of Erasmus+ impact studies | 2019-05-26 | 2026-09-10T09:46:17Z | career, cross-cultural and European-identity survey results | https://www.eeas.europa.eu/node/63171_en
SRC-012 | ◈ | fam:C | MITCHELL-ERASMUS-2015 | Rethinking the Erasmus Effect on European Identity | 2014-04-11 | 2026-09-10T09:46:17Z | panel 1,729 students, 28 universities, six countries; positive identity change association | https://onlinelibrary.wiley.com/doi/10.1111/jcms.12152
SRC-013 | ◈ | fam:C | SIGALAS-ERASMUS-2010 | Cross-border mobility and European identity | 2010-06-04 | 2026-09-10T09:46:17Z | two-wave longitudinal study; no strengthening and possible adverse identity effect | https://journals.sagepub.com/doi/10.1177/1465116510363656
SRC-014 | ◈ | fam:C | KUHN-ERASMUS-2012 | Why Educational Exchange Programmes Miss Their Mark | 2012-10-17 | 2026-09-10T09:46:17Z | no Erasmus identity gain; selection/ceiling explanation | https://onlinelibrary.wiley.com/doi/10.1111/j.1468-5965.2012.02286.x
SRC-015 | ◈ | fam:C | MOCANU-LLURDA-2024 | Multilingual ELF and European identity through Erasmus | 2024-05-27 | 2026-09-10T09:46:17Z | pre-post N155; no substantial European identity impact | https://www.tandfonline.com/doi/full/10.1080/01434632.2024.2357716
SRC-016 | ◈ | fam:C | DIPIETRO-MOBILITY-2024 | International Education Mobility and Environmental Concerns | 2024-04-15 | 2026-09-10T09:46:17Z | propensity-score matching, EU27; modest positive effect on environmental concern | https://doi.org/10.1177/10283153241235698
SRC-017 | ◈ | fam:D | BC-ALUMNI-2025 | Alumni Voices 2025 | 2025-08-01 | 2026-09-10T09:46:17Z | 3,094 alumni survey; persistent contacts; soft-power framing | https://www.britishcouncil.org/research-insight/alumni-voices-2025-uk-graduates-global-influence
SRC-018 | ◈ | fam:D | BC-SOFTPOWER-2024 | Soft power at a turning point | 2024-07-01 | 2026-09-10T09:46:17Z | comparative policies include France/EU; education most common activity; stronger alignment with national interests | https://www.britishcouncil.org/research-insight/soft-power-cultural-relations-comparative-analysis-2024
SRC-019 | ◈ | fam:E | EP-FOREIGN-INTERFERENCE-2022 | European Parliament report on foreign interference | 2022-03-09 | 2026-09-10T09:46:17Z | educational/cultural institutes and Confucius Institute concerns; academic-freedom boundary | https://www.europarl.europa.eu/doceo/document/A-9-2022-0022_EN.html
SRC-020 | ◈ | fam:E | EC-RI-INTERFERENCE-TOOLKIT-2022 | Commission toolkit on foreign interference in research | 2022-01-18 | 2026-09-10T09:46:17Z | defines foreign interference and safeguards cooperation | https://research-and-innovation.ec.europa.eu/news/all-research-and-innovation-news/commission-publishes-toolkit-help-mitigate-foreign-interference-research-and-innovation-2022-01-18_en

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/le-budget-2024-du-ministere-de-l-europe-et-des-affaires-etrangeres-un-budget-en-hausse-de-plus-de-6 | A | 2024 | French influence budget | France budgeted EUR721.2m for programme 185 Diplomatie culturelle et influence in 2024, EUR50m above 2023, explicitly presenting influence as a policy priority. | -
FCT-002 | FACT | ✧ | https://www.diplomatie.gouv.fr/fr/le-ministere-et-son-reseau/les-metiers-de-la-diplomatie/un-reseau-diplomatique-essentiel-a-la-politique-etrangere-de-la-france/le-reseau-de-cooperation-et-d-action-culturelle-et-ses-metiers/article/qui-sont-les-conseillers-et-conseilleres-de-cooperation-et-d-action-culturelle | A | 2026 | French cultural-diplomatic network | The MEAE describes its cooperation and cultural-action network as central to influence and reports 131 cooperation/cultural services, 125 institutes including 98 local Instituts français, 310 Campus France spaces/branches in 134 countries and more than 380 conventioned Alliances among 832 worldwide. | -
FCT-003 | FACT | ✧ | https://www.diplomatie.gouv.fr/fr/le-ministere-en-action/assurer-la-presence-de-la-culture-francaise/defendre-la-francophonie-et-la-langue-francaise/engagement-de-la-france-pour-la-diversite-linguistique-et-la-langue-francaise/enseigner-et-apprendre-le-francais | A | 2025 | language exposure scale | French Institutes receive more than 600,000 French-language learners per year and 832 Alliances françaises receive nearly 500,000 learners per year. | -
FCT-004 | FACT | ✧ | https://www.institutfrancais.com/fr | A | 2026 | programme mechanisms | Institut français lists mobility and residency programmes, professional network-building, debates and ideas, expertise/training and project cofunding among its action modes. | -
FCT-005 | FACT | ✧ | https://www.campusfrance.org/fr/le-programme-de-bourses-france-excellence-eiffel | A | 2026 | Eiffel explicit objective | France Excellence Eiffel is explicitly designed by the foreign ministry both to attract high-performing foreign students and to train future foreign public- and private-sector decision-makers in priority fields. | -
FCT-006 | FACT | ✧ | https://www.campusfrance.org/fr/le-programme-de-bourses-france-excellence-eiffel | A | 2026 | Eiffel selection architecture | Only French higher-education institutions submit Eiffel candidates and expert juries selected by the ministry assess applications, which establishes selective elite formation but not later political tasking. | -
FCT-007 | FACT | ✧ | https://rapportactivite2021.campusfrance.org/ | A | 2021 | Eiffel programme scale | Campus France reported 347 Eiffel laureates selected from 1,478 applications in 2021 and presented an impact study of the programme. | -
FCT-008 | FACT | ✧ | https://rapportactivite2021.campusfrance.org/ | A | 2021 | institutional cooperation effect | In Campus France reporting, 84% of responding institutions considered Eiffel a major tool for recruiting excellent students and developing international cooperation strategy; this is institutional self-report rather than causal policy-outcome evidence. | -
FCT-009 | FACT | ✧ | https://www.campusfrance.org/fr/reseau-France-Alumni | A | 2026-07-31 | France Alumni network scale | France Alumni reports 687,000 current and former international students from French higher education across more than 130 countries. | -
FCT-010 | FACT | ✧ | https://www.campusfrance.org/fr/reseau-France-Alumni | A | 2026 | alumni retention mechanism | France Alumni is explicitly designed to maintain links with France through events, information, thematic groups and professional networking; network existence does not identify political alignment or tasking. | -
FCT-011 | FACT | ✧ | https://erasmus-plus.ec.europa.eu/nl/news/almost-15-million-people-went-on-an-erasmus-mobility-in-2024-according-to-latest-report | B | 2024 | Erasmus annual scale | Erasmus+ operated with a EUR4.7bn annual budget in 2024, supported more than 34,400 projects and 85,600 organisations, and provided mobility opportunities to almost 1.5m people. | -
FCT-012 | FACT | ✧ | https://erasmus-plus.ec.europa.eu/whats-new/news/marking-37-years-of-erasmus-key-numbers-and-achievements | B | 1987-2024 | Erasmus accumulated scale | Erasmus+ reports more than 15m participants since 1987 and EUR26.2bn allocated for 2021-2027. | -
FCT-013 | FACT | ✧ | https://erasmus-plus.ec.europa.eu/whats-new/news/marking-37-years-of-erasmus-key-numbers-and-achievements | B | 2024 | European identity policy intent | EU programme material explicitly links Erasmus investment to political objectives including a European Education Area, youth empowerment and promotion of European identity through education and culture. | -
FCT-014 | FACT | ✧ | https://op.europa.eu/en/publication-detail/-/publication/94d97f5c-7ae2-11e9-9f05-01aa75ed71a1/language-en | B | 2014-2018 | impact study design | The 2019 Erasmus+ Higher Education Impact Study covered two million student/staff mobilities in 2014-2018 and used almost 77,000 survey responses. | -
FCT-015 | FACT | ✧ | https://www.eeas.europa.eu/node/63171_en | B | 2019 | Commission-commissioned impact findings | The EEAS summary of the Commission-commissioned study reports more than 90% of Erasmus students improved cross-cultural collaboration ability and felt they had a European identity, with larger reported impact among students initially less convinced about the EU. | -
FCT-016 | FACT | ✧ | https://www.eeas.europa.eu/node/63171_en | B | 2019 | career and mobility outcomes | The same study reports 80% employed within three months of graduation, 72% saying Erasmus helped with the first job, and more internationally oriented careers; these are programme-evaluation associations/self-reports, not randomized causal effects. | -
FCT-017 | FACT | ✧ | https://onlinelibrary.wiley.com/doi/10.1111/jcms.12152 | C | 2015 | positive identity panel | Mitchell analysed a panel of 1,729 students at 28 universities in six countries and found Erasmus participation significantly and positively related to changes in identification as European and identification with Europe. | -
FCT-018 | FACT | ✧ | https://onlinelibrary.wiley.com/doi/10.1111/jcms.12152 | C | 2015 | contact mechanism | Mitchell found transnational contact during exchange, increased knowledge of Europe and attention to European news associated with stronger European identification, supporting an exposure/contact mechanism. | -
FCT-019 | FACT | ✧ | https://journals.sagepub.com/doi/10.1177/1465116510363656 | C | 2010 | negative longitudinal control | Sigalas two-wave longitudinal study found Erasmus study abroad did not strengthen European identity and could have an adverse effect despite increased socialising with other Europeans. | -
FCT-020 | FACT | ✧ | https://onlinelibrary.wiley.com/doi/10.1111/j.1468-5965.2012.02286.x | C | 2012 | selection ceiling control | Kuhn argued Erasmus often misses the identity target because participants are already unusually likely to feel European, creating a selection/ceiling problem. | -
FCT-021 | FACT | ✧ | https://www.tandfonline.com/doi/full/10.1080/01434632.2024.2357716 | C | 2024 | recent pre-post null | A 2024 pre-post study of 155 Erasmus students across three European contexts found no substantial effect on European identity, while participants strongly valued English as a shared language. | -
FCT-022 | FACT | ✧ | https://doi.org/10.1177/10283153241235698 | C | 2024 | attitude effect outside identity | Using propensity-score matching on EU27 Eurobarometer data, Di Pietro estimated a modest but statistically significant positive effect of education mobility abroad on environmental concern. | -
FCT-023 | FACT | ✧ | https://www.britishcouncil.org/research-insight/alumni-voices-2025-uk-graduates-global-influence | D | 2025 | alumni network comparator | British Council Alumni Voices surveyed 3,094 UK-education alumni from 123 countries; more than 75% had contacted or met someone from their UK study experience in the prior year, evidence of persistent network ties in a comparator programme. | -
FCT-024 | FACT | ✧ | https://www.britishcouncil.org/research-insight/alumni-voices-2025-uk-graduates-global-influence | D | 2025 | self-selection limit | The British Council frames international alumni as soft-power assets, but the survey is drawn from Alumni UK members and cannot by itself identify a causal effect on foreign policy decisions. | -
FCT-025 | FACT | ✧ | https://www.britishcouncil.org/research-insight/soft-power-cultural-relations-comparative-analysis-2024 | D | 2024 | comparative policy orientation | British Council comparative research including France and the EU reports education as the most common soft-power activity and finds soft-power policies increasingly tied to national foreign-policy and economic priorities. | -
FCT-026 | FACT | ✧ | https://www.europarl.europa.eu/doceo/document/A-9-2022-0022_EN.html | E | 2022 | academic sharp-power boundary | The European Parliament report identifies foreign-state use of cultural and educational institutes as a potential interference channel and raises specific academic-freedom concerns around Confucius Institutes and foreign university funding in Europe. | -
FCT-027 | FACT | ✧ | https://www.europarl.europa.eu/doceo/document/A-9-2022-0022_EN.html | E | 2022 | case heterogeneity | The Parliament report notes university closures or severed ties with Confucius Institutes in several EU states, while also treating the issue as institution- and evidence-specific rather than proof that all cultural institutes are interference. | -
FCT-028 | FACT | ✧ | https://research-and-innovation.ec.europa.eu/news/all-research-and-innovation-news/commission-publishes-toolkit-help-mitigate-foreign-interference-research-and-innovation-2022-01-18_en | E | 2022 | foreign interference definition | The Commission research-security toolkit defines foreign interference as activity by or on behalf of a foreign state-level actor that is coercive, covert, deceptive or corrupting and contrary to EU sovereignty, values and interests. | -
FCT-029 | FACT | ✧ | https://research-and-innovation.ec.europa.eu/news/all-research-and-innovation-news/commission-publishes-toolkit-help-mitigate-foreign-interference-research-and-innovation-2022-01-18_en | E | 2022 | cooperation versus interference safeguards | The same Commission guidance explicitly preserves international academic cooperation while recommending safeguards in values, governance, partnerships and cybersecurity, separating openness from covert/coercive control. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-003
FCT-004 | SRC-004
FCT-005 | SRC-005
FCT-006 | SRC-005
FCT-007 | SRC-006
FCT-008 | SRC-006
FCT-009 | SRC-007
FCT-010 | SRC-007
FCT-011 | SRC-008
FCT-012 | SRC-009
FCT-013 | SRC-009
FCT-014 | SRC-010
FCT-015 | SRC-011
FCT-016 | SRC-011
FCT-017 | SRC-012
FCT-018 | SRC-012
FCT-019 | SRC-013
FCT-020 | SRC-014
FCT-021 | SRC-015
FCT-022 | SRC-016
FCT-023 | SRC-017
FCT-024 | SRC-017
FCT-025 | SRC-018
FCT-026 | SRC-019
FCT-027 | SRC-019
FCT-028 | SRC-020
FCT-029 | SRC-020

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

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:search
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:facts
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:causal
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:verify
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:accountability
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:finalize

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-10T09:50:58.316961+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-029","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":29,"eligible":29,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:29;attempted:0;success:0;failure:0;blocked:29} | WRITEBACK_EXECUTION_V1:[29 rows, see section]

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
