ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260911-2318-new-ip-itu-standardisation | PARENT_RUN_ID:NONE | AS_OF:2026-09-11
INPUT_KIND:RUN_CARD | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/inv024_runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-11_new-ip-itu-standardisation/2026-09-11_23-18_new-ip-itu-standardisation_INPUT.md | SUBJECT_SLUG:new-ip-itu-standardisation | SUBJECT_FP:sha256:cc4ea04901b609e3cb36a41957496c8a896733caf8b97072536adf01c5158151 | INPUT_SHA256:sha256:592cf583788e630b8d85f479389564f2019b70bc10762a386e956301d7943a4e
COMPLEXITY:8→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:UIT-T, principalement 2019-2021, avec suites jusqu'en 2022 pour l'issue WTSA. Cas New IP/Future Vertical Communication Networks; acteurs chinois co-proposants, IETF/ICANN/RIPE, France/Commission européenne/États UE et organisations sectorielles. Gardes : participation SDO != capture; co-signature Etat-entreprises != tasking individuel; proposition != adoption; opposition != preuve de malignité; standard technique != ingerence par nature; rejet != absence d'influence tentee.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
## Résultat analytique technique

Le cas New IP ferme un mécanisme plus précis que « influence chinoise » : une **coalition observable au niveau d’une contribution** associe le MIIT et plusieurs entreprises chinoises de télécommunications pour proposer une transformation stratégique du travail de l’UIT-T. Cette co-signature établit une action conjointe d’agenda-setting, pas le `tasking` de chaque entreprise.

La proposition est entrée dans le processus institutionnel : TSAG l’a discutée et l’a transmise à l’IETF/IAB; des contributions SG13 ont ensuite cherché à prolonger les travaux. En miroir, l’IETF a formulé une objection technique explicite, tandis qu’une coalition incluant la France, la Commission européenne, de nombreux États européens, GSMA/ETNO et RIPE NCC a déposé des contre-contributions visant à empêcher l’adoption des questions New IP/FVCN.

Le résultat aval est discriminant : les propositions New IP testées ici n’ont pas été acceptées au niveau des groupes d’étude et n’ont pas été adoptées à WTSA-20. La chaîne `proposition -> capture de l’UIT -> standard global imposé` est donc réfutée dans ce cas borné. En revanche, `proposition coordonnée -> mise à l’agenda -> mobilisation/contre-mobilisation institutionnelle` est supporté.

La dimension d’intention reste ouverte. Huawei décrit New IP comme un programme de recherche technique et récuse l’interprétation de contrôle centralisé; IETF et ICANN identifient des risques d’interopérabilité, d’architecture et de gouvernance. Le corpus permet d’établir cette divergence et les propriétés techniques contestées, pas de convertir ces risques en preuve d’une intention politique maligne.

Conclusion causale : **la standardisation technique est bien une arène d’influence institutionnelle où États, entreprises et communautés techniques tentent de fixer l’agenda et les règles; ce cas montre aussi un contre-pouvoir effectif, puisque la proposition contestée n’a pas franchi l’arête d’adoption.**
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:0|EDI_DECISIVE:5|SRC_COMPLETE:12/12

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **item 1:**
  - **date:** 2019-09-10
  - **event:** Contribution 83 New IP submitted by MIIT + China Mobile + China Unicom + Huawei
  - **support:**
    - FCT-001
- **item 2:**
  - **date:** 2019-09-23/30
  - **event:** TSAG considers New IP and sends liaison/material to IETF/IAB
  - **support:**
    - FCT-002
- **item 3:**
  - **date:** 2020-02-18
  - **event:** New IP potential standards in 2021 contribution appears in SG13
  - **support:**
    - FCT-005
- **item 4:**
  - **date:** 2020-03-30
  - **event:** IETF formal response rejects need for monolithic top-down New IP
  - **support:**
    - FCT-004
- **item 5:**
  - **date:** 2020-07-20
  - **event:** France/Commission/European coalition submits Next steps counter-contribution
  - **support:**
    - FCT-006
- **item 6:**
  - **date:** 2020-11-18
  - **event:** Broader coalition asks that New IP/FVCN questions not go forward for adoption
  - **support:**
    - FCT-007
    - FCT-008
- **item 7:**
  - **date:** 2020-12
  - **event:** New IP questions not accepted at ITU-T study-group level
  - **support:**
    - FCT-011
    - FCT-015
- **item 8:**
  - **date:** 2022
  - **event:** New IP not accepted at WTSA-20
  - **support:**
    - FCT-012

### MANIPULATION_REPORT
- **assumptions:**
  - standards participation can be legitimate
  - technical risk does not establish political intent
  - rejection is an observable outcome
- **clusters:**
  - NONE
- **complexity:** COMPLEX/8
- **implicit:**
  - standards can redistribute governance power
  - state-industry coalitions may coordinate agendas
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - @PAT[NET]
  - @PAT[TEMP]
- **priorities:**
  - formal proposal chain
  - counter-coalition
  - adoption outcome
  - tasking boundary
- **query_guidance:**
  - primary standards records
  - proponent rationale
  - counter-body response
  - final procedural outcome
- **rhetorical:**
  - NONE
- **speaker:** mechanism-first forensic investigation contract
- **symbol_stage:** FINAL
- **symbols:**
  - **Κ:** LOW: no cynical facade mechanism established
  - **Λ:** MATERIAL: competing technical/governance framings documented
  - **Ξ:** LOW: bounded omissions audited through explicit outcome/tasking gaps
  - **Σ:** LOW: no semiotic mechanism central to causal chain
  - **Φ:** LOW: no spectacle mechanism established
  - **Ψ:** LOW: no sideration mechanism in bounded standards case
  - **Ω:** LOW: no inversion mechanism established
  - **κ:** LOW: no nudge/choice-architecture mechanism in scope
  - **ρ:** MATERIAL: formal counter-mobilization and non-adoption documented
  - **€:** LOW: no material hidden financial-flow claim in scope
  - **↕:** MATERIAL: institutional asymmetry/state-industry participation is central
  - **⏰:** MATERIAL: 2019 proposal -> 2020 counter-contributions -> non-adoption chronology documented
  - **⚔:** LOW: no cognitive-warfare tasking established
  - **⫸:** MATERIAL: multi-actor coalition/counter-coalition convergence documented
  - **🌐:** MATERIAL: standards-body actor network and liaison edges documented
- **threats:**
  - @THR[REG_CAPTURE]: triaged; capture not established
  - @THR[POWER_PROX]: guarded; co-presence/co-signature not tasking

### MODULE_EXECUTION
NONE

### SCOPING_REPORT
- **ACTORS_INSTITUTIONS:**
  - MIIT
  - Huawei
  - China Mobile
  - China Unicom
  - China Telecom
  - ITU-T
  - IETF
  - ICANN
  - RIPE NCC
  - France
  - European Commission
  - EU member states
  - GSMA
  - ETNO
- **DOMAINS:**
  - technical standardization
  - Internet governance
  - state-industry coordination
  - institutional influence
- **EVIDENCE_LIMITS:**
  - ITU C83 and some coalition contributions were inspected through indexed exact-document extraction because direct fetch failed
  - no private communications proving tasking
  - no causal vote model for coalition marginal effect
- **EXCLUSIONS:**
  - general China influence
  - 5G vendor security
  - domestic Chinese Internet control not causally linked to ITU proposal
  - unrelated ITU work
- **GEO:** ITU-T global process with France/EU response
- **LEAD_QUESTION:** Did Chinese state/industry actors capture Internet standardization through New IP?
- **OBJECT_COVERAGE:** proposal authorship, formal routing, technical/proponent narratives, opposition coalition, study-group and WTSA outcome.
- **OBJECT_QUESTION:** In the New IP case, what evidence closes state/industry proposal -> ITU process -> counter-coalition -> adoption/rejection, and where does proof stop between normal standardization, strategic influence, capture and normative effect?
- **PERIOD:** 2019-2022; later sources only to verify historical outcome

### CREDO
- **rules:**
  - participation SDO != capture
  - joint contribution != individual tasking
  - proposal != adoption
  - technical risk != malign intent
  - rejection != no influence attempt
  - not found != does not exist
- **truth_ceiling:** The strongest closed result is attempted standards agenda-setting plus counter-mobilization and non-adoption; not capture or proven malign intent.

### COGNITIVE_MAP
- **closed_level:** joint agenda-setting + institutional influence attempt + organized counter-mobilization + non-adoption
- **continuum:**
  - normal standards participation
  - joint agenda-setting
  - institutional influence attempt
  - procedural coalition/counter-coalition
  - adoption/normative effect
  - capture
  - political-control intent
- **unclosed_levels:**
  - state tasking of each corporate co-proponent
  - capture of ITU
  - malign political-control intent
  - quantified causal weight of opposition

### DIALECTICAL_MAP
- **perspectives:**
  - **item 1:**
    - **best_case:** New IP responds to future industrial requirements through normal SDO consensus and is not a control architecture.
    - **id:** P1
    - **position:** proponent/technical innovation
    - **support:**
      - FCT-003
  - **item 2:**
    - **best_case:** IETF/ICANN identify duplication, interoperability and architectural risks; existing IP can evolve without top-down replacement.
    - **id:** P2
    - **position:** technical/interoperability critics
    - **support:**
      - FCT-004
      - FCT-009
      - FCT-010
  - **item 3:**
    - **best_case:** Joint state-industry proposals can be strategic agenda-setting in standards venues, but this case ended in counter-mobilization and non-adoption rather than capture.
    - **id:** P3
    - **position:** institutional/geopolitical mechanism
    - **support:**
      - FCT-001
      - FCT-006
      - FCT-007
      - FCT-011
      - FCT-012

### RESOURCE_FLOW_MAP
- **item 1:**
  - **case:** C83
  - **flow:** MIIT + Chinese telecom firms -> formal contribution -> TSAG consideration -> liaison/study-group discussion
  - **status:** AGENDA_SETTING_ATTEMPT_SUPPORTED
  - **support:**
    - FCT-001
    - FCT-002
- **item 2:**
  - **case:** European counter-coalition
  - **flow:** France + Commission + European states + industry/RIPE -> formal contributions -> request no adoption
  - **status:** COUNTER_MOBILIZATION_SUPPORTED
  - **support:**
    - FCT-006
    - FCT-007
    - FCT-008
- **item 3:**
  - **case:** Outcome
  - **flow:** contested work questions -> study-group non-acceptance -> no WTSA adoption
  - **status:** NON_ADOPTION_SUPPORTED
  - **support:**
    - FCT-011
    - FCT-012
    - FCT-015

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** MIIT + China Mobile + China Unicom + Huawei
  - **relation:** co-source formal contribution C83
  - **support:**
    - FCT-001
  - **to:** ITU-T TSAG
- **item 2:**
  - **from:** ITU-T TSAG
  - **relation:** liaison for review/comment
  - **support:**
    - FCT-002
  - **to:** IETF/IAB
- **item 3:**
  - **from:** IETF
  - **relation:** formal technical response
  - **support:**
    - FCT-004
  - **to:** ITU-T TSAG
- **item 4:**
  - **from:** France + European Commission + European states + GSMA/ETNO/RIPE
  - **relation:** formal counter-contributions
  - **support:**
    - FCT-006
    - FCT-007
    - FCT-008
  - **to:** ITU-T SG13/SG11/TSAG

### IMPACT_MAP
- **agenda_effect:** SUPPORTED: New IP entered formal ITU-T discussion and generated liaisons/work-question proposals.
- **capture_effect:** REFUTED_IN_BOUNDED_CASE: no captured/adopted global replacement standard.
- **counter_mobilization_effect:** SUPPORTED: IETF and European/industry/RIPE actors issued formal objections and anti-adoption contributions.
- **normative_effect:** PROPOSAL_NOT_ADOPTED: no tested New IP/FVCN work-question adoption at study-group/WTSA level.
- **political_intent:** UNKNOWN/GAP: architecture risks do not establish subjective intent.
- **support:**
  - FCT-002
  - FCT-004
  - FCT-006
  - FCT-007
  - FCT-011
  - FCT-012
  - FCT-015

### CONTRADICTION_LEDGER
- **item 1:**
  - **issue:** Purpose of New IP
  - **resolution:** Technical proposal and risks are established; political-control intent is not.
  - **side_a:** Huawei: future technical research, normal SDO consensus, no centralized-control mechanism.
  - **side_b:** IETF/ICANN: top-down/compatibility/governance risks and no demonstrated need for wholesale replacement.
  - **support:**
    - FCT-003
    - FCT-004
    - FCT-009
    - FCT-010
    - FCT-014
- **item 2:**
  - **issue:** State-industry relation
  - **resolution:** Coalition at proposal level supported; command relation remains a gap.
  - **side_a:** MIIT and firms co-signed C83.
  - **side_b:** Co-signature alone does not establish state tasking of each firm.
  - **support:**
    - FCT-001
    - FCT-003
- **item 3:**
  - **issue:** Influence vs capture
  - **resolution:** Influence attempt/agenda-setting supported; capture/adoption refuted in bounded case.
  - **side_a:** Proposal entered ITU process and triggered international response.
  - **side_b:** Proposal was not accepted/adopted.
  - **support:**
    - FCT-002
    - FCT-011
    - FCT-012
    - FCT-015

### VERIFICATION_REPORT
- **contradictions_material:** 3
- **critical_result:** New IP is a documented standards agenda-setting attempt with state-industry co-sponsorship and international counter-mobilization; the tested proposal was not adopted, and tasking/capture/malign-intent claims remain unclosed.
- **domains:**
  - **GOVERNANCE:** 3
  - **STANDARDIZATION:** 9
  - **TECHNICAL:** 4
- **pdf_visual_check:** ICANN OCTO-017 executive-summary page was visually inspected; RIPE-hosted formal-contribution PDFs were available through exact indexed text but direct screenshot fetch failed.
- **primary_or_direct_source_facts:** 13
- **retrieval_limits:**
  - some ITU/RIPE-hosted formal contributions inspected from indexed exact-document extraction after direct fetch/cache failures
- **status:** PASS_WITH_ATTRIBUTION_AND_INTENT_GAPS
- **verified_facts:** 16

### EDI_REPORT
- **corpus:**
  - **families:** 6
  - **notes:** ITU/proponent, Huawei, IETF, European coalition, RIPE and ICANN perspectives; direct formal records prioritized.
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim:** state-industry co-sponsorship
    - **facts:**
      - FCT-001
      - FCT-002
    - **status:** COVERED_BOUNDED
  - **item 2:**
    - **claim:** tasking of each firm
    - **facts:**
      - NONE
    - **status:** GAP_ATTRIBUTION
  - **item 3:**
    - **claim:** counter-mobilization
    - **facts:**
      - FCT-004
      - FCT-006
      - FCT-007
      - FCT-008
    - **status:** COVERED
  - **item 4:**
    - **claim:** adoption/capture
    - **facts:**
      - FCT-011
      - FCT-012
      - FCT-015
    - **status:** REFUTED_BOUNDED
  - **item 5:**
    - **claim:** malign political-control intent
    - **facts:**
      - FCT-003
      - FCT-010
      - FCT-014
    - **status:** GAP_INTENT
- **diagnostic_not_truth:** true
- **dimensions:**
  - **geo:** 0.85
  - **lang:** 0.55
  - **owner:** 0.75
  - **persp:** 0.8
  - **strat:** 0.9
  - **temp:** 0.8
- **edi:**
  - **band:** BROAD
  - **score:** 0.72
- **source_counts:**
  - **◈:** 8
  - **◉:** 4
  - **○:** 0

### RESPONSIBILITY_MAP
- **item 1:**
  - **actor:** MIIT / corporate co-proponents
  - **evidence:**
    - FCT-001
    - FCT-005
  - **limit:** joint authorship does not prove command relationship among co-sponsors
  - **responsibility:** authorship/co-sponsorship of formal standards proposal
- **item 2:**
  - **actor:** ITU-T
  - **evidence:**
    - FCT-002
    - FCT-011
    - FCT-012
  - **limit:** venue participation does not imply capture
  - **responsibility:** procedural venue for consideration and study-question decisions
- **item 3:**
  - **actor:** IETF/ICANN
  - **evidence:**
    - FCT-004
    - FCT-009
    - FCT-010
  - **limit:** technical criticism does not establish proponent intent
  - **responsibility:** technical assessment/counter-position
- **item 4:**
  - **actor:** France/EU/European and sector coalition
  - **evidence:**
    - FCT-006
    - FCT-007
    - FCT-008
  - **limit:** exact marginal causal weight on final outcome not measured
  - **responsibility:** formal opposition and anti-adoption contributions

### NEXT_QUERIES
- **item 1:**
  - **query:** primary Chinese ministry/corporate communications proving instruction or tasking for New IP contributions
  - **route:** RECHECK
  - **trigger:** new archival/leak/judicial evidence
- **item 2:**
  - **query:** ITU consensus minutes or chair reports identifying exact reasons and actors decisive for SG13 New IP question non-adoption
  - **route:** RECHECK
  - **trigger:** accessible primary meeting records
- **item 3:**
  - **query:** post-2022 New IP/FVCN building-block proposals with direct adoption and measurable governance effect
  - **route:** NEW_CANDIDATE
  - **trigger:** specific adopted standard/work item with causal continuity

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-007,QRY-008 | support:- | counter:- | results:FCT-001,FCT-002 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-009 | support:- | counter:- | results:FCT-003,FCT-014 | final:SATURATED | gap:NONE
LED-003 | attempts:QRY-010 | support:- | counter:- | results:FCT-004,FCT-013 | final:SATURATED | gap:NONE
LED-004 | attempts:QRY-013 | support:- | counter:- | results:FCT-006,FCT-007,FCT-015 | final:SATURATED | gap:NONE
LED-005 | attempts:QRY-017 | support:- | counter:- | results:FCT-011,FCT-012,FCT-015 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-007,QRY-008 | support:- | counter:- | results:FCT-001,FCT-002,CAU-001 | final:GAP | gap:ATTRIBUTION
AXS-002 | attempts:QRY-009,QRY-010,QRY-016 | support:- | counter:- | results:FCT-003,FCT-004,FCT-009,FCT-010,FCT-014 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-008,QRY-010,QRY-012,QRY-013,QRY-014,QRY-015 | support:- | counter:- | results:FCT-002,FCT-004,FCT-006,FCT-007,FCT-008,FCT-013,FCT-016 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-017 | support:- | counter:- | results:FCT-011,FCT-012,FCT-015,CAU-004 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-009,QRY-010,QRY-013,QRY-017 | support:- | counter:- | results:FCT-003,FCT-013,FCT-014,FCT-015 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-007,QRY-008,SRC-001,SRC-002 | support:FCT-001,FCT-002 | counter:- | results:FCT-001,FCT-002 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-009,SRC-003 | support:- | counter:FCT-003 | results:FCT-003 | final:GAP | gap:ATTRIBUTION
CLM-003 | attempts:QRY-009,QRY-010,QRY-012,QRY-013,QRY-016,SRC-003,SRC-004,SRC-006,SRC-007,SRC-010 | support:FCT-003 | counter:FCT-004,FCT-009,FCT-010,FCT-013 | results:FCT-003,FCT-004,FCT-009,FCT-010,FCT-013 | final:PARTIAL | gap:NONE
CLM-004 | attempts:QRY-013,QRY-017,SRC-007,SRC-011 | support:- | counter:FCT-011,FCT-012,FCT-015 | results:FCT-011,FCT-012,FCT-015 | final:REFUTED | gap:NONE
CLM-005 | attempts:QRY-007,QRY-008,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-017,QRY-018,SRC-001,SRC-002,SRC-005,SRC-006,SRC-007,SRC-008,SRC-009,SRC-011,SRC-012 | support:FCT-002,FCT-005,FCT-006,FCT-007,FCT-008,FCT-016 | counter:FCT-015 | results:FCT-002,FCT-005,FCT-006,FCT-007,FCT-008,FCT-016,FCT-015 | final:SUPPORTED | gap:NONE
CLM-006 | attempts:QRY-010,QRY-012,QRY-013,QRY-016,SRC-004,SRC-006,SRC-007,SRC-010 | support:- | counter:FCT-004,FCT-006,FCT-007,FCT-009,FCT-013 | results:FCT-004,FCT-006,FCT-007,FCT-009,FCT-013 | final:REFUTED | gap:NONE
CLM-007 | attempts:QRY-009,QRY-010,QRY-016,SRC-003,SRC-004,SRC-010 | support:FCT-010 | counter:FCT-003,FCT-014 | results:FCT-010,FCT-003,FCT-014 | final:GAP | gap:INTENT

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
AXS-001 | AXS | GAP | ATTRIBUTION | Joint sponsorship is observable; separate evidence of MIIT tasking each corporate co-sponsor was not found in the bounded run.
CLM-002 | CLM | GAP | ATTRIBUTION | Joint sponsorship/coordination is established at contribution level; tasking relationship for each firm is not established.
CLM-007 | CLM | GAP | INTENT | Technical/governance risk is documented; proponent intent to enable political control is not proven by the inspected corpus.
CAU-005 | CAU | GAP | INTENT | Risk properties and political context do not prove subjective intent.

SEMANTIC_COUNTS_V1:LED:5|CLM:7|AXS:5|CAU:5|CTRL:5|ACT:3

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-007","QRY-008"],"evidence_excerpt":"MIIT + China Mobile + China Unicom + Huawei are listed as sources of Contribution 83.","kind":"MECHANISM","lead":"New IP was formally co-sponsored by a Chinese ministry and telecom firms in an ITU-T contribution, making state-industry coalition observable at the proposal level.","linked_ids":["AXS-001","CLM-001","CAU-001"],"locator":"title/date/source metadata","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002"],"routes":["EXPAND","LINK"],"source_id":"SRC-001","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-009"],"evidence_excerpt":"future industrial requirements; research initiative; no control mechanisms; consensus process.","kind":"CLAIM","lead":"The proponent narrative supplies a legitimate technical rationale and explicitly denies centralized-control intent; this is a required symmetry control.","linked_ids":["AXS-002","CLM-002","CTRL-002"],"locator":"New IP initiative sections Why/What/What it is not","materiality":"DECISIVE","result_ids":["FCT-003","FCT-014"],"routes":["AUDIT","LINK"],"source_id":"SRC-003","status":"SATURATED"}
LED-003 | {"attempt_ids":["QRY-010"],"evidence_excerpt":"no evidence for monolithic New IP; top-down replacement would harm interoperability.","kind":"MECHANISM","lead":"IETF formally contested the need and architecture, creating a standards-body counter-case rather than a geopolitical allegation alone.","linked_ids":["AXS-002","CLM-003","CAU-002"],"locator":"liaison body","materiality":"IMPORTANT","result_ids":["FCT-004","FCT-013"],"routes":["EXPAND","LINK"],"source_id":"SRC-004","status":"SATURATED"}
LED-004 | {"attempt_ids":["QRY-013"],"evidence_excerpt":"case not made; significant concerns; questions should not go forward for adoption.","kind":"EVENT","lead":"France/EU/industry/RIPE jointly sought non-adoption of the proposed New IP/FVCN questions.","linked_ids":["AXS-003","CLM-004","CAU-003"],"locator":"abstract + source list","materiality":"DECISIVE","result_ids":["FCT-006","FCT-007","FCT-015"],"routes":["EXPAND","LINK"],"source_id":"SRC-007","status":"SATURATED"}
LED-005 | {"attempt_ids":["QRY-017"],"evidence_excerpt":"New IP proposals were not accepted at ITU-T study group level in 2020, and thus were not accepted at WTSA-20.","kind":"EVENT","lead":"The tested proposal failed to cross the adoption edge: not accepted at study-group level and therefore not at WTSA-20.","linked_ids":["AXS-004","CLM-005","CAU-004"],"locator":"ITU 2022 overview outcome","materiality":"DECISIVE","result_ids":["FCT-011","FCT-012","FCT-015"],"routes":["AUDIT","LINK"],"source_id":"SRC-011","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"New IP was a formally visible state-industry standards proposal involving MIIT and Chinese telecom firms.","claimant":"INV-024 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002"]}
CLM-002 | {"claim":"The MIIT/firm co-signature proves that the Chinese state tasked or controlled every corporate co-proponent.","claimant":"automatic tasking inference","counter":["FCT-003"],"gap":"Joint sponsorship/coordination is established at contribution level; tasking relationship for each firm is not established.","gap_type":"ATTRIBUTION","materiality":"DECISIVE","status":"GAP","support":"NONE_FOUND"}
CLM-003 | {"claim":"New IP was merely a technical research initiative with no material governance implications.","claimant":"strong proponent reading","counter":["FCT-004","FCT-009","FCT-010","FCT-013"],"gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"PARTIAL","support":["FCT-003"]}
CLM-004 | {"claim":"New IP was an adopted ITU replacement for TCP/IP or a captured global standard.","claimant":"strong capture/adoption hypothesis","counter":["FCT-011","FCT-012","FCT-015"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"REFUTED","support":"NONE_FOUND"}
CLM-005 | {"claim":"Formal standards participation can function as institutional influence/agenda-setting even when the proposal is rejected.","claimant":"INV-024 mechanism","counter":["FCT-015"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-002","FCT-005","FCT-006","FCT-007","FCT-008","FCT-016"]}
CLM-006 | {"claim":"Opposition to New IP was simply geopolitical resistance with no technical basis.","claimant":"symmetry counter-hypothesis","counter":["FCT-004","FCT-006","FCT-007","FCT-009","FCT-013"],"gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"REFUTED","support":"NONE_FOUND"}
CLM-007 | {"claim":"New IP proponents had a proven malign political intent to centralize surveillance/control.","claimant":"strong intent hypothesis","counter":["FCT-003","FCT-014"],"gap":"Technical/governance risk is documented; proponent intent to enable political control is not proven by the inspected corpus.","gap_type":"INTENT","materiality":"DECISIVE","status":"GAP","support":["FCT-010"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-007","QRY-008"],"axis":"ACTORS_RELATIONS","gap":"Joint sponsorship is observable; separate evidence of MIIT tasking each corporate co-sponsor was not found in the bounded run.","gap_type":"ATTRIBUTION","links":["LED-001"],"question":"Is state-industry joint sponsorship directly observable, and does it prove tasking/control?","result_ids":["FCT-001","FCT-002","CAU-001"],"sought_objects":["formal source lists","proposal authorship","instruction/tasking evidence"],"status":"GAP"}
AXS-002 | {"attempt_ids":["QRY-009","QRY-010","QRY-016"],"axis":"COUNTER_HYPOTHESES","links":["LED-002","LED-003"],"question":"Can New IP be explained as a bona fide technical research agenda rather than a control project?","result_ids":["FCT-003","FCT-004","FCT-009","FCT-010","FCT-014"],"sought_objects":["proponent rationale","technical critiques","alternative standards work"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-008","QRY-010","QRY-012","QRY-013","QRY-014","QRY-015"],"axis":"MECHANISMS","links":["LED-001","LED-003","LED-004"],"question":"Did the proposal move through an institutional standards process and trigger organized counter-mobilization?","result_ids":["FCT-002","FCT-004","FCT-006","FCT-007","FCT-008","FCT-013","FCT-016"],"sought_objects":["liaisons","study questions","formal counter-contributions","coalition membership"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-017"],"axis":"IMPACT_RESPONSIBILITY","links":["LED-005"],"question":"Was New IP/FVCN adopted as ITU-T work/standard in the bounded period?","result_ids":["FCT-011","FCT-012","FCT-015","CAU-004"],"sought_objects":["study-group outcome","WTSA outcome"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-009","QRY-010","QRY-013","QRY-017"],"axis":"RULES_CONTROLS","links":["LED-002","LED-004","LED-005"],"question":"Does participation in ITU standardization itself establish capture, ingérence or malign intent?","result_ids":["FCT-003","FCT-013","FCT-014","FCT-015"],"sought_objects":["normal process evidence","proponent position","opposition process","outcome"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"Formal submission and institutional routing establish agenda-setting attempt, not capture.","counter":"NONE_FOUND","limit":"No evidence that every co-sponsor was state-tasked.","mechanism":"state ministry + firms co-sponsor proposal -> ITU-T consideration/liaison -> study-group work agenda","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-005"],"type":"INSTITUTIONAL_INFLUENCE"}
CAU-002 | {"causal_right":"Chronology and explicit response documents close proposal -> opposition response.","counter":"NONE_FOUND","limit":"Does not by itself identify each actor marginal causal weight.","mechanism":"New IP/FVCN proposals -> IETF/France/EU/industry/RIPE objections -> coordinated counter-contributions","status":"SUPPORTED","support":["FCT-004","FCT-006","FCT-007","FCT-008","FCT-016"],"type":"COUNTER_MOBILIZATION"}
CAU-003 | {"causal_right":"Outcome record plus anti-adoption contribution supports non-adoption; exact but-for weight of the coalition remains unmeasured.","counter":"NONE_FOUND","limit":"No counterfactual vote/consensus model quantifies which objections were decisive.","mechanism":"proposal + opposition -> proposed study questions not accepted -> no WTSA adoption","status":"SUPPORTED","support":["FCT-007","FCT-011","FCT-012","FCT-015"],"type":"NORMATIVE_EFFECT"}
CAU-004 | {"causal_right":"The tested New IP/FVCN proposal did not cross the study-group/WTSA adoption edge; this refutes capture in the bounded case.","counter":["FCT-011","FCT-012","FCT-015"],"gap":"The tested proposal was not adopted.","limit":"Refutation is bounded to the tested proposal and period; it does not prove absence of influence attempts or future successor work.","mechanism":"state-industry proposal -> capture of ITU -> replacement global Internet standard","status":"REFUTED","support":"NONE_FOUND","type":"CAPTURE"}
CAU-005 | {"counter":["FCT-003","FCT-014"],"gap":"Risk properties and political context do not prove subjective intent.","gap_type":"INTENT","limit":"No inspected primary communication establishes a malign political-control intent behind the proposal.","mechanism":"technical design concerns -> malign political-control intent","status":"GAP","support":"NONE_FOUND","type":"INTENT"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"participation in standards body != capture","status":"DONE","support":["FCT-011","FCT-012","FCT-015"]}
CTRL-002 | {"control":"joint state-industry contribution != tasking of each firm","status":"DONE","support":["FCT-001","FCT-003"]}
CTRL-003 | {"control":"proposal != adoption","status":"DONE","support":["FCT-002","FCT-011","FCT-012"]}
CTRL-004 | {"control":"technical/governance risk != malign intent","status":"DONE","support":["FCT-003","FCT-009","FCT-010","FCT-014"]}
CTRL-005 | {"control":"rejection != absence of attempted institutional influence","status":"DONE","support":["FCT-002","FCT-005","FCT-006","FCT-007"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Represent New IP as a failed but observable standards agenda-setting attempt, not as a captured/adopted global standard.","actor":"future synthesis/article protocol","intent":"prevent adoption/capture inflation","status":"DONE","support":["FCT-001","FCT-002","FCT-011","FCT-012","FCT-015"]}
ACT-002 | {"action":"Reopen state tasking only on direct instruction/governance/communications linking MIIT to specific corporate contribution decisions.","actor":"future investigation","intent":"close attribution gap","status":"DEFERRED","support":["FCT-001"]}
ACT-003 | {"action":"Preserve Huawei technical rationale and IETF/ICANN objections side-by-side; do not infer political intent from architecture alone.","actor":"future synthesis/article protocol","intent":"symmetry","status":"DONE","support":["FCT-003","FCT-004","FCT-009","FCT-010","FCT-014"]}

SEARCH_ACTIVITY_V1:WEB:6|FETCH:15|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"EMPTY","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL | mnemo | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | https://www.itu.int/md/T17-TSAG-C-0083/en | New IP ITU MIIT Huawei China Mobile China Unicom contribution 83
QRY-002 | WEB | FOUND | - | https://datatracker.ietf.org/liaison/1677/ | IETF response New IP ITU liaison 2020
QRY-003 | WEB | FOUND | - | https://www.ripe.net/documents/1363/T17-SG13-C-1069R1MSW-E.pdf | France European Commission New IP ITU contribution
QRY-004 | WEB | FOUND | - | https://www.huawei.com/de/deu/magazin/aktuelles/new-ip | Huawei New IP initiative technical rationale
QRY-005 | WEB | FOUND | - | https://www.icann.org/en/system/files/files/octo-017-27oct20-en.pdf | ICANN OCTO New IP technical analysis
QRY-006 | WEB | FOUND | - | https://itp.cdn.icann.org/en/files/government-engagement-ge/ge-013-12-07-2023-en.pdf | New IP outcome SG13 WTSA not accepted
QRY-007 | FETCH | FOUND | SRC-001 | https://www.itu.int/md/T17-TSAG-C-0083/en | ITU contribution 83 exact catalog metadata inspected via indexed page; direct page open failed decoding
QRY-008 | FETCH | FOUND | SRC-002 | https://datatracker.ietf.org/liaison/1653/ | IETF Datatracker incoming ITU-T TSAG liaison inspected
QRY-009 | FETCH | FOUND | SRC-003 | https://www.huawei.com/de/deu/magazin/aktuelles/new-ip | Huawei official New IP initiative page inspected
QRY-010 | FETCH | FOUND | SRC-004 | https://datatracker.ietf.org/liaison/1677/ | IETF response liaison inspected
QRY-011 | FETCH | FOUND | SRC-005 | https://www.itu.int/md/meetingdoc.asp?parent=T17-SG13-200313-C&source=China+Telecom | ITU SG13 contribution listings inspected via indexed exact meeting pages
QRY-012 | FETCH | FOUND | SRC-006 | https://www.ripe.net/media/documents/T17-SG13-C-0971R2MSW-E.pdf | formal ITU contribution text inspected via indexed PDF extraction
QRY-013 | FETCH | FOUND | SRC-007 | https://www.ripe.net/documents/1363/T17-SG13-C-1069R1MSW-E.pdf | formal ITU contribution text inspected via indexed PDF extraction
QRY-014 | FETCH | FOUND | SRC-008 | https://labs.ripe.net/author/marco_hogewoning/update-on-wtsa-20-preparations-and-new-ip/ | RIPE NCC WTSA/New IP update inspected
QRY-015 | FETCH | FOUND | SRC-009 | https://www.ripe.net/community/internet-governance/multi-stakeholder-engagement/ripe-ncc-contributions-to-external-consultations/ | RIPE NCC contributions register inspected
QRY-016 | FETCH | FOUND | SRC-010 | https://www.icann.org/en/system/files/files/octo-017-27oct20-en.pdf | ICANN OCTO-017 PDF opened and page 3 visually inspected
QRY-017 | FETCH | FOUND | SRC-011 | https://itp.cdn.icann.org/en/files/government-engagement-ge/ge-013-12-07-2023-en.pdf | ICANN government-engagement report text inspected via indexed PDF extraction
QRY-018 | FETCH | FOUND | SRC-012 | https://www.ripe.net/community/wg/active-wg/coop/minutes/cooperation-working-group-minutes-ripe-80/ | RIPE Cooperation WG minutes inspected
QRY-019 | FETCH | FOUND | - | https://www.huawei.com/de/deu/magazin/aktuelles/new-ip | REFUTATION Opposition technical governance: inspect proponent rationale for evidence that objections were purely geopolitical and lacked technical basis
QRY-020 | FETCH | FOUND | - | https://www.huawei.com/de/deu/magazin/aktuelles/new-ip | REFUTATION Material narrative divergence: inspect proponent and critic positions for convergence that would eliminate the documented disagreement
QRY-021 | FETCH | FOUND | - | https://itp.cdn.icann.org/en/files/government-engagement-ge/ge-013-12-07-2023-en.pdf | REFUTATION Proposal did not become proposed ITU work program: inspect later ITU outcome reporting for evidence of study-group or WTSA acceptance of New IP

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | ITU-T-TSAG-C83 | ITU-T TSAG Contribution 83 — New IP, Shaping Future Network | 2019-09-10 | 2026-09-11T21:18:00Z | title/date/source fields: China Mobile, China Unicom, Huawei, MIIT; proposal to initiate strategy transformation | https://www.itu.int/md/T17-TSAG-C-0083/en
SRC-002 | ◈ | fam:A | IETF-LIAISON-1653 | ITU-T TSAG liaison — LS on New IP, Shaping Future Network | 2019-09-30 | 2026-09-11T21:18:00Z | lines 100-132; TSAG considered New IP and sent contribution/tutorial to IETF/IAB for comment ahead WTSA | https://datatracker.ietf.org/liaison/1653/
SRC-003 | ◈ | fam:B | HUAWEI-NEW-IP | Huawei — New IP Initiative | UNKNOWN | 2026-09-11T21:18:00Z | lines 149-185; motivation, research fields, denial of central-control interpretation, SDO consensus claim | https://www.huawei.com/de/deu/magazin/aktuelles/new-ip
SRC-004 | ◈ | fam:C | IETF-LIAISON-1677 | IETF — Response to LS on New IP | 2020-03-30 | 2026-09-11T21:18:00Z | lines 100-255; no evidence of need for monolithic top-down New IP; interoperability/duplication concerns | https://datatracker.ietf.org/liaison/1677/
SRC-005 | ◈ | fam:A | ITU-SG13-C871 | ITU-T SG13 — New IP potential standards in 2021 | 2020-02-18 | 2026-09-11T21:18:00Z | catalog listing; China Mobile, China Telecom, Huawei; QALL/13 | https://www.itu.int/md/meetingdoc.asp?parent=T17-SG13-200313-C&source=China+Telecom
SRC-006 | ◈ | fam:D | ITU-SG13-C971-R2 | ITU-T SG13 C971-R2 — Next steps for proposed work on New IP | 2020-07-20 | 2026-09-11T21:18:00Z | France/European Commission/European states/GSMA/RIPE coalition; no decisions on New IP before analysis; IETF should lead Internet architecture | https://www.ripe.net/media/documents/T17-SG13-C-0971R2MSW-E.pdf
SRC-007 | ◈ | fam:D | ITU-SG13-C1069-R1 | ITU-T SG13 C1069-R1 — New IP/FVCN or similar proposals | 2020-11-18 | 2026-09-11T21:18:00Z | France/EU/European states/ETNO/GSMA/RIPE coalition; recommends proposed questions not go forward for adoption | https://www.ripe.net/documents/1363/T17-SG13-C-1069R1MSW-E.pdf
SRC-008 | ◉ | fam:E | RIPE-NEWIP-UPDATE | RIPE NCC — Update on WTSA-20 preparations and New IP | 2020-11-10 | 2026-09-11T21:18:00Z | RIPE participant account: contested questions, name change FVCN, objections and compromise discussions | https://labs.ripe.net/author/marco_hogewoning/update-on-wtsa-20-preparations-and-new-ip/
SRC-009 | ◈ | fam:E | RIPE-ITU-CONTRIB-LIST | RIPE NCC — ITU contributions register | UNKNOWN | 2026-09-11T21:18:00Z | lists Jan/Jul/Sep/Nov 2020 New IP submissions across TSAG, SG11, SG13 | https://www.ripe.net/community/internet-governance/multi-stakeholder-engagement/ripe-ncc-contributions-to-external-consultations/
SRC-010 | ◉ | fam:other:icann | ICANN-OCTO-017 | ICANN OCTO — New IP | 2020-10-27 | 2026-09-11T21:18:00Z | executive summary pp.3-4; work-in-progress status, architecture elements, compatibility and governance/security implications | https://www.icann.org/en/system/files/files/octo-017-27oct20-en.pdf
SRC-011 | ◉ | fam:other:icann | ICANN-GE-013 | ICANN — ITU 2022 Overview | 2023-07-12 | 2026-09-11T21:18:00Z | reports New IP proposals not accepted at ITU-T study-group level in 2020 and therefore not accepted at WTSA-20 | https://itp.cdn.icann.org/en/files/government-engagement-ge/ge-013-12-07-2023-en.pdf
SRC-012 | ◉ | fam:E | RIPE80-COOP-MINUTES | RIPE 80 Cooperation WG minutes — New IP | 2020-05-13 | 2026-09-11T21:18:00Z | records government/RIPE discussion and German support for bottom-up multistakeholder Internet architecture | https://www.ripe.net/community/wg/active-wg/coop/minutes/cooperation-working-group-minutes-ripe-80/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.itu.int/md/T17-TSAG-C-0083/en | A | 2019-09-10 | New IP C83 co-proponents | ITU-T catalog metadata lists Contribution 83, New IP, Shaping Future Network, with China Mobile, China Unicom, Huawei Technologies and China Ministry of Industry and Information Technology (MIIT) as sources. | -
FCT-002 | FACT | ✧ | https://datatracker.ietf.org/liaison/1653/ | A | 2019-09-23/30 | New IP entered formal ITU-T process | TSAG considered a New IP tutorial and contribution proposing analysis of current challenges and a future-network development path; ITU-T then transmitted the material to IETF/IAB for comment ahead of WTSA. | -
FCT-003 | FACT | ✧ | https://www.huawei.com/de/deu/magazin/aktuelles/new-ip | B | UNKNOWN | Huawei stated rationale | Huawei describes New IP as a technology-research initiative for future industrial/social network requirements and states that it does not define control mechanisms or centralized top-down Internet control. | -
FCT-004 | FACT | ✧ | https://datatracker.ietf.org/liaison/1677/ | C | 2020-03-30 | IETF technical opposition | The IETF said it had seen no evidence for a monolithic top-down New IP, identified unsupported/incorrect premises, and argued that replacing the existing IP stack wholesale would harm interoperability and create network islands. | -
FCT-005 | FACT | ✧ | https://www.itu.int/md/meetingdoc.asp?parent=T17-SG13-200313-C&source=China+Telecom | A | 2020-02-18 | Continued New IP standardization proposals | ITU-T SG13 catalog records a contribution titled New IP potential standards in 2021 from China Mobile, China Telecom and Huawei, showing continued effort beyond the September 2019 TSAG proposal. | -
FCT-006 | FACT | ✧ | https://www.ripe.net/media/documents/T17-SG13-C-0971R2MSW-E.pdf | D | 2020-07-20 | France/EU formal counter-contribution | A formal SG13 contribution co-sponsored by France, the European Commission, multiple European states, GSMA and RIPE NCC urged that no New IP-related work-item/question decisions be taken before analysis and argued that IETF should lead Internet-architecture development. | -
FCT-007 | FACT | ✧ | https://www.ripe.net/documents/1363/T17-SG13-C-1069R1MSW-E.pdf | D | 2020-11-18 | Broad coalition sought non-adoption | A later SG13 contribution co-sponsored by France, EU actors, European states, ETNO, GSMA and RIPE NCC said the case for New IP/FVCN questions had not been made and proposed that the proposed questions not go forward for adoption. | -
FCT-008 | FACT | ✧ | https://www.ripe.net/community/internet-governance/multi-stakeholder-engagement/ripe-ncc-contributions-to-external-consultations/ | E | 2020 | Sustained counter-mobilization | RIPE NCC documents a sequence of New IP responses in TSAG, SG11 and SG13 during 2020, while its contemporaneous update describes the questions as contested and the label shifting toward Future Vertical Communication Networks. | -
FCT-009 | FACT | ✧ | https://www.icann.org/en/system/files/files/octo-017-27oct20-en.pdf | other:icann | 2020-10-27 | ICANN technical assessment | ICANN OCTO described New IP as incomplete work in progress, analyzed variable-length addressing, ManyNets and other elements, and assessed incompatibility risks with the deployed IPv4/IPv6 Internet. | -
FCT-010 | FACT | ✧ | https://www.icann.org/en/system/files/files/octo-017-27oct20-en.pdf | other:icann | 2020-10-27 | ICANN governance/security concern | ICANN OCTO assessed that proposed strong regulatory binding between IP address and user could make pervasive monitoring easier; this is an ICANN technical-risk assessment, not proof of the proponents political intent. | -
FCT-011 | FACT | ✧ | https://itp.cdn.icann.org/en/files/government-engagement-ge/ge-013-12-07-2023-en.pdf | other:icann | 2020/2022 | New IP study-group outcome | ICANN government-engagement reporting states that New IP proposals were not accepted at ITU-T study-group level in 2020. | -
FCT-012 | FACT | ✧ | https://itp.cdn.icann.org/en/files/government-engagement-ge/ge-013-12-07-2023-en.pdf | other:icann | 2022 | WTSA outcome | The same ICANN report states that because New IP proposals were not accepted at study-group level, they were not accepted at WTSA-20. | -
FCT-013 | FACT | ✦ | https://datatracker.ietf.org/liaison/1677/ | C,D | 2020 | Opposition was technical and governance-oriented | Independent IETF and European/sector-member contributions objected on interoperability, duplication, technical-merit, multistakeholder-process and economic-risk grounds; opposition was not merely geopolitical labeling. | -
FCT-014 | FACT | ✦ | https://www.huawei.com/de/deu/magazin/aktuelles/new-ip | B,C,other:icann | 2020 | Material narrative divergence | Huawei framed New IP as open technical research under normal consensus processes and rejected centralized-control interpretations, while IETF and ICANN documented substantial architectural/interoperability/governance concerns. The disagreement itself is established; malign intent is not. | -
FCT-015 | FACT | ✦ | https://itp.cdn.icann.org/en/files/government-engagement-ge/ge-013-12-07-2023-en.pdf | D,other:icann | 2020-2022 | Proposal did not become the proposed ITU work program | The bounded New IP/FVCN proposal encountered organized opposition and was not accepted into the next ITU-T study-period/WTSA outcome in the form tested here. | -
FCT-016 | FACT | ✧ | https://www.ripe.net/community/wg/active-wg/coop/minutes/cooperation-working-group-minutes-ripe-80/ | E | 2020-05-13 | European government coordination around standards response | RIPE 80 minutes record German government support for bottom-up multistakeholder Internet development and coordination with German ITU representatives and others, illustrating that the counter-response itself also involved state coordination. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001,SRC-002
FCT-003 | SRC-003
FCT-004 | SRC-004
FCT-005 | SRC-005
FCT-006 | SRC-006
FCT-007 | SRC-007
FCT-008 | SRC-008,SRC-009
FCT-009 | SRC-010
FCT-010 | SRC-010
FCT-011 | SRC-011
FCT-012 | SRC-011
FCT-013 | SRC-004,SRC-006,SRC-007
FCT-014 | SRC-003,SRC-004,SRC-010
FCT-015 | SRC-007,SRC-011
FCT-016 | SRC-012

## REFUTATION_REGISTRY_V1
FCT-013 | QRY-019 | NONE
FCT-014 | QRY-020 | NONE
FCT-015 | QRY-021 | NONE

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
FCT-013 | ELIGIBLE:CONFIRME
FCT-014 | ELIGIBLE:CONFIRME
FCT-015 | ELIGIBLE:CONFIRME
FCT-016 | ELIGIBLE:VERIFIE

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

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:CAUSAL
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:FINALIZE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-11T21:33:07.163136+00:00","fact_mem":{},"mnemo_row":"BLOCKED:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:CONFIRME","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:CONFIRME","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:CONFIRME","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":16,"eligible":16,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:BLOCKED:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:16;attempted:0;success:0;failure:0;blocked:16} | WRITEBACK_EXECUTION_V1:[16 rows, see section]

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
FCT-013 | ELIGIBLE:CONFIRME | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-014 | ELIGIBLE:CONFIRME | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-015 | ELIGIBLE:CONFIRME | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-016 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
