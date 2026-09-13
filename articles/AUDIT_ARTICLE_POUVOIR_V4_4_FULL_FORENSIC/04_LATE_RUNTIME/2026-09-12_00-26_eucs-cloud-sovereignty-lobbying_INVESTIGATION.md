ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260912-0026-eucs-cloud-sovereignty-lobbying | PARENT_RUN_ID:NONE | AS_OF:2026-09-12
INPUT_KIND:RUN_CARD | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/inv123_runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-12_eucs-cloud-sovereignty-lobbying/2026-09-12_00-26_eucs-cloud-sovereignty-lobbying_INPUT.md | SUBJECT_SLUG:eucs-cloud-sovereignty-lobbying | SUBJECT_FP:sha256:d88e2c9de018eecf47326818bcb8be04fa3b8a646ffac8ac370cb0e337654f88 | INPUT_SHA256:sha256:8e93611f0ef34d86af0718740bd882688f3f31e4540984d185bd04cf3e9831b7
COMPLEXITY:8→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:EU, Germany, France and transatlantic interface, 2021-2026. EUCS sovereignty criteria: documented lobbying requests -> decision channels -> draft changes -> market-access consequences. Controls: member-state preferences, cloud-customer positions, European industry opposition, later 2026 sovereignty procurement framework.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
## Résultat analytique technique

INV-123 ferme un cas précis d'influence normative : des fournisseurs et coalitions industrielles ayant un intérêt direct dans l'accès au marché européen du cloud ont **publiquement et explicitement demandé la suppression des exigences de souveraineté de l'EUCS**. Le cas AWS est particulièrement fort : son inscription au registre du Bundestag nomme littéralement comme objectif d'influence la suppression de ces exigences. Des coalitions industrielles ont parallèlement visé les États membres, les institutions européennes et ENISA, et ont mobilisé l'interface diplomatique EU-US/TTC.

Le résultat demandé a ensuite été observable dans la trajectoire du texte : le draft du 22 mars 2024 rapporté par Reuters ne contenait plus les exigences strictes antérieures de souveraineté, et les organisations industrielles ont publiquement salué ce changement. Cela ferme `intérêt -> action de lobbying -> cible normative -> delta de texte congruent`. Cela ne ferme pas `lobbying -> cause déterminante du delta`.

La contre-enquête empêche cette inflation causale. La France, l'Allemagne et l'Italie avaient officiellement défendu en octobre 2023 la protection des données sensibles contre les législations extraterritoriales ; la France maintenait encore cette ligne en avril 2024. Le compromis était contesté entre États et au sein de l'industrie européenne, et la réunion d'experts d'avril 2024 n'a pas abouti à un vote. Aucun document décisionnel inspecté ne permet donc d'allouer un effet marginal au lobbying AWS/BSA/CCIA par rapport aux préférences autonomes des États, aux utilisateurs du cloud, ou aux arguments techniques et commerciaux.

Enfin, le retrait de souveraineté dans l'EUCS 2024 ne constitue pas une capture permanente : en 2026 la Commission applique un Cloud Sovereignty Framework à la commande publique et propose une architecture législative incluant des niveaux de souveraineté tout en annonçant la reprise des travaux EUCS.

Conclusion : **`commercial interest -> explicit lobbying -> policy target -> aligned draft change` est SUPPORTÉ ; `Big Tech lobbying -> causal authorship of the change` reste NOT_ESTABLISHED ; `capture/corruption` est REFUTÉ dans le périmètre probatoire de ce run.**
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:0|EDI_DECISIVE:5|SRC_COMPLETE:16/16

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **item 1:**
  - **date:** 2021
  - **event:** ENISA candidate EUCS presented as voluntary harmonised cloud-security scheme
  - **support:**
    - FCT-010
- **item 2:**
  - **date:** 2023-05
  - **event:** industry coalitions publicly demand removal of sovereignty requirements and escalate through US TTC channel
  - **support:**
    - FCT-002
    - FCT-003
- **item 3:**
  - **date:** 2023-10-30
  - **event:** France/Germany/Italy state protection against extraterritorial law
  - **support:**
    - FCT-007
- **item 4:**
  - **date:** 2024-03-22
  - **event:** reported EUCS draft removes stringent sovereignty requirements
  - **support:**
    - FCT-005
- **item 5:**
  - **date:** 2024-04-11/16
  - **event:** BSA/GDA welcome removal; expert-group compromise remains contested and vote delayed
  - **support:**
    - FCT-004
    - FCT-006
- **item 6:**
  - **date:** 2024-06-28
  - **event:** AWS German lobby-register entry explicitly records deletion objective
  - **support:**
    - FCT-001
- **item 7:**
  - **date:** 2026-04/06
  - **event:** Commission applies and explains separate cloud-sovereignty procurement framework
  - **support:**
    - FCT-011
    - FCT-012
- **item 8:**
  - **date:** 2026
  - **event:** Commission proposal says work will resume on EUCS within broader cloud sovereignty architecture
  - **support:**
    - FCT-013

### MANIPULATION_REPORT
- **assumptions:**
  - sovereignty requirements have both security and industrial-policy dimensions
  - member states are autonomous actors, not passive lobby recipients
- **clusters:**
  - NONE
- **complexity:** COMPLEX/8
- **implicit:**
  - open lobbying can materially seek to shape security standards
  - policy outcomes can align with lobbying without causal closure
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - @PAT[MONEY]
  - @PAT[NET]
  - @PAT[TEMP]
- **priorities:**
  - explicit lobbying objective
  - coalition pressure
  - draft delta
  - counter-coalitions
  - causal attribution
  - 2026 persistence/reversal control
- **query_guidance:**
  - official lobby registers
  - public industry statements
  - official government positions
  - draft-change reporting
  - subsequent Commission architecture
- **rhetorical:**
  - NONE
- **speaker:** mechanism-first forensic contract
- **symbol_stage:** FINAL
- **symbols:**
  - **Κ:** LOW: institutional-facade claim is not established
  - **Λ:** STRONG: sovereignty-as-security versus sovereignty-as-protectionism frames diverge
  - **Ξ:** MATERIAL: draft/version provenance is decisive for exact policy delta
  - **Σ:** LOW: semiotic framing exists but is secondary to explicit lobbying
  - **Φ:** LOW: spectacle is not a causal core
  - **Ψ:** LOW: fear/sideration is not a material mechanism in this dossier
  - **Ω:** LOW: no inversion mechanism is needed for the causal core
  - **κ:** LOW: no nudge architecture in scope
  - **ρ:** MATERIAL: member-state and provider counter-coalitions constrain outcome
  - **€:** STRONG: commercial market-access stakes are central
  - **↕:** MATERIAL: hyperscaler resource/access asymmetry versus smaller providers
  - **⏰:** STRONG: lobbying precedes and accompanies the draft shift
  - **⚔:** LOW: no covert operation needed to explain documented influence attempt
  - **⫸:** MATERIAL: coalition aggregation of vendor/customer positions
  - **🌐:** STRONG: transatlantic and EU multi-level lobbying network
- **threats:**
  - @THR[POWER_PROX]: active; lobbying access is not capture
  - @THR[REG_CAPTURE]: active but not established
  - @THR[NARR_LAUNDER]: low; advocacy is overt, not covert laundering

### MODULE_EXECUTION
NONE

### SCOPING_REPORT
- **ACTORS_INSTITUTIONS:**
  - AWS
  - BSA
  - CCIA
  - US Chamber/USCIB
  - ENISA
  - ECCG/member states
  - France/Germany/Italy
  - European cloud providers
  - European Commission
- **DOMAINS:**
  - cloud certification
  - lobbying
  - digital sovereignty
  - market access
  - extraterritorial law
  - public procurement
- **EVIDENCE_LIMITS:**
  - key March 2024 draft change is documented through reputable reporting rather than a public final draft archive
  - private meetings and internal drafting rationale are incomplete
  - registered lobbying objective may postdate some draft changes and therefore proves intent/continuity, not initiation
- **EXCLUSIONS:**
  - general Big Tech power
  - content moderation
  - general cloud dependency already covered by INV-125
  - unrelated DSA/DMA lobbying
- **GEO:** EU, Germany, France, transatlantic interface
- **LEAD_QUESTION:** Did US Big Tech lobby the EU into dropping cloud-sovereignty requirements?
- **OBJECT_COVERAGE:** lobby target, advocacy channels, policy delta, counter-positions, causal gap, later sovereignty framework.
- **OBJECT_QUESTION:** What evidence links documented hyperscaler/industry lobbying against EUCS sovereignty criteria to the 2024 draft change, and how far can causation be separated from autonomous member-state, customer, technical and legal preferences?
- **PERIOD:** 2021-2026

### CREDO
- **rules:**
  - lobbying != causality
  - text change != single-author attribution
  - member-state preference != capture
  - commercial interest != state tasking
  - industry coalition != unanimity
  - draft != final law
  - policy relocation != permanent abandonment
- **truth_ceiling:** Explicit lobbying against sovereignty requirements and an aligned 2024 draft change are established; marginal causal responsibility of Big Tech for that change is not established.

### COGNITIVE_MAP
- **closed_level:** coordinated lobbying + specific target + aligned observable draft delta
- **continuum:**
  - legitimate policy advocacy
  - coordinated industry lobbying
  - access/agenda pressure
  - policy-delta congruence
  - demonstrated causal influence
  - capture
  - corruption
- **unclosed_levels:**
  - marginal causal effect
  - capture
  - corruption

### DIALECTICAL_MAP
- **perspectives:**
  - **item 1:**
    - **best_case:** EUCS should remain technical and non-discriminatory; sovereignty conditions distort cybersecurity certification and market choice.
    - **id:** P1
    - **position:** industry technical-security view
    - **support:**
      - FCT-002
      - FCT-003
      - FCT-004
  - **item 2:**
    - **best_case:** extra-EU legal control is itself a security/sovereignty risk for sensitive workloads, so nationality/control conditions are materially relevant.
    - **id:** P2
    - **position:** sovereignty/security view
    - **support:**
      - FCT-007
      - FCT-008
      - FCT-009
  - **item 3:**
    - **best_case:** industry pressure and target congruence are proven, but bargaining was multi-actor; causal capture cannot be inferred from congruence alone.
    - **id:** P3
    - **position:** forensic causal view
    - **support:**
      - FCT-005
      - FCT-006
      - FCT-014
      - FCT-015

### RESOURCE_FLOW_MAP
- **item 1:**
  - **case:** market-access stakes
  - **flow:** sovereignty conditions -> eligibility constraints for non-EU-controlled hyperscalers -> commercial incentive to lobby
  - **status:** SUPPORTED_AS_INCENTIVE
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
- **item 2:**
  - **case:** corruption/payment
  - **flow:** vendor money -> decision-maker -> draft change
  - **status:** NOT_ESTABLISHED
  - **support:**
    - NONE

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** AWS
  - **relation:** registered advocacy objective
  - **support:**
    - FCT-001
  - **to:** German/EU EUCS policy process
- **item 2:**
  - **from:** industry coalitions
  - **relation:** joint statements and US-government/TTC advocacy
  - **support:**
    - FCT-002
    - FCT-003
    - FCT-004
    - FCT-016
  - **to:** EU institutions/member states/ENISA
- **item 3:**
  - **from:** France/Germany/Italy
  - **relation:** government counter-position in 2023
  - **support:**
    - FCT-007
  - **to:** EUCS negotiation
- **item 4:**
  - **from:** European providers/customers
  - **relation:** split positions on compromise
  - **support:**
    - FCT-006
    - FCT-014
  - **to:** EUCS expert process

### IMPACT_MAP
- **actor_specific_causal_effect:** NOT_ESTABLISHED: no decision record allocates causal weight.
- **influence_attempt:** SUPPORTED: explicit, repeated and multi-channel advocacy against sovereignty criteria.
- **market_access_effect:** PLAUSIBLE_AND_DIRECT_BY_DESIGN: removing ownership/control constraints broadens eligibility, but final adoption remained unsettled.
- **permanent_capture:** REFUTED_BOUNDED: 2026 Commission procurement/legislative architecture reintroduced sovereignty metrics.
- **policy_alignment:** SUPPORTED: 2024 draft moved in requested direction.
- **support:**
  - FCT-001
  - FCT-002
  - FCT-003
  - FCT-004
  - FCT-005
  - FCT-006
  - FCT-011
  - FCT-012
  - FCT-013

### CONTRADICTION_LEDGER
- **item 1:**
  - **issue:** lobbying success vs causal proof
  - **resolution:** target congruence supported; causal attribution remains gap.
  - **side_a:** AWS/industry asked for deletion and draft deleted criteria.
  - **side_b:** member-state and customer positions were independently divided; expert compromise remained unsettled.
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-014
- **item 2:**
  - **issue:** technical security vs sovereignty security
  - **resolution:** normative conflict is real; Truth Engine does not treat either framing as self-validating.
  - **side_a:** industry frames sovereignty criteria as political/non-technical.
  - **side_b:** France/partners frame extraterritorial-law exposure as sensitive-data protection issue.
  - **support:**
    - FCT-002
    - FCT-003
    - FCT-007
    - FCT-008
- **item 3:**
  - **issue:** permanent policy capture
  - **resolution:** policy venue shifted/returned; no permanent abandonment.
  - **side_a:** 2024 draft removal weakens sovereignty inside EUCS.
  - **side_b:** 2026 Commission creates separate measurable sovereignty procurement framework.
  - **support:**
    - FCT-005
    - FCT-011
    - FCT-012
    - FCT-013

### VERIFICATION_REPORT
- **contradictions_material:** 3
- **critical_result:** Explicit commercial lobbying against EUCS sovereignty requirements and an aligned 2024 draft change are supported; Big Tech causal responsibility for the change is not established; corruption/capture are not established.
- **domains:**
  - **CONTROLS:** 2
  - **LOBBYING:** 5
  - **POLICY_DELTA:** 3
  - **POLICY_PERSISTENCE:** 3
  - **STATE_POSITIONS:** 3
- **primary_or_direct_source_facts:** 13
- **retrieval_limits:**
  - March 2024 EUCS draft itself was not available as a stable official public text in the inspected corpus; Reuters reporting is used for version delta
  - private ECCG/member-state deliberations and internal drafting rationale were not obtained
  - German AWS register entry dated June 2024 proves a continuing explicit lobbying objective but does not by itself prove pre-March initiation
- **status:** PASS_WITH_CAUSALITY_GAP
- **verified_facts:** 16

### EDI_REPORT
- **corpus:**
  - **families:** 10
  - **notes:** official German/French/Italian/EU sources, vendor/industry advocacy, European industry control and Reuters version reporting.
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim:** AWS lobbying objective
    - **facts:**
      - FCT-001
    - **status:** COVERED
  - **item 2:**
    - **claim:** multi-channel industry pressure
    - **facts:**
      - FCT-002
      - FCT-003
      - FCT-004
      - FCT-016
    - **status:** COVERED
  - **item 3:**
    - **claim:** 2024 draft removal
    - **facts:**
      - FCT-005
      - FCT-006
    - **status:** COVERED_BY_REPUTABLE_VERSION_REPORT
  - **item 4:**
    - **claim:** Big Tech caused removal
    - **facts:**
      - FCT-015
    - **status:** GAP_CAUSALITY
  - **item 5:**
    - **claim:** permanent sovereignty abandonment
    - **facts:**
      - FCT-011
      - FCT-012
      - FCT-013
    - **status:** REFUTED_BOUNDED
- **diagnostic_not_truth:** true
- **dimensions:**
  - **geo:** 0.84
  - **lang:** 0.78
  - **owner:** 0.76
  - **persp:** 0.85
  - **strat:** 0.82
  - **temp:** 0.88
- **edi:**
  - **band:** BROAD
  - **score:** 0.74
- **source_counts:**
  - **◈:** 8
  - **◉:** 8
  - **○:** 0

### RESPONSIBILITY_MAP
- **item 1:**
  - **actor:** AWS
  - **evidence:**
    - FCT-001
  - **limit:** objective != demonstrated effectiveness
  - **responsibility:** explicit registered objective to remove sovereignty requirements
- **item 2:**
  - **actor:** industry coalitions
  - **evidence:**
    - FCT-002
    - FCT-003
    - FCT-004
    - FCT-016
  - **limit:** coalition advocacy != single principal/tasking
  - **responsibility:** sustained public advocacy and transatlantic escalation
- **item 3:**
  - **actor:** EU/member states
  - **evidence:**
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-008
  - **limit:** internal causal weighting unavailable
  - **responsibility:** draft negotiation and compromise
- **item 4:**
  - **actor:** European Commission 2026
  - **evidence:**
    - FCT-011
    - FCT-012
    - FCT-013
  - **limit:** later policy does not negate earlier influence attempt
  - **responsibility:** separate sovereignty procurement framework / renewed legislative architecture

### NEXT_QUERIES
- **item 1:**
  - **query:** ECCG/member-state minutes, position papers or voting records tied to March-April 2024 EUCS compromise
  - **route:** RECHECK
  - **trigger:** public/declassified records become available
- **item 2:**
  - **query:** Commission/ENISA internal drafting rationale identifying which submissions changed sovereignty clauses
  - **route:** RECHECK
  - **trigger:** FOI/document release
- **item 3:**
  - **query:** EU Transparency Register meeting logs for AWS/BSA/CCIA on EUCS with Commission/ENISA/member-state officials
  - **route:** RECHECK
  - **trigger:** actor-specific access reconstruction needed

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-009 | support:- | counter:- | results:FCT-001,FCT-015 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-010,QRY-011 | support:- | counter:- | results:FCT-002,FCT-003,FCT-016 | final:SATURATED | gap:NONE
LED-003 | attempts:QRY-013 | support:- | counter:- | results:FCT-005,FCT-015 | final:SATURATED | gap:NONE
LED-004 | attempts:QRY-014 | support:- | counter:- | results:FCT-007,FCT-008 | final:SATURATED | gap:NONE
LED-005 | attempts:QRY-014 | support:- | counter:- | results:FCT-006 | final:SATURATED | gap:NONE
LED-006 | attempts:QRY-016 | support:- | counter:- | results:FCT-011,FCT-012,FCT-013 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-009,QRY-010,QRY-011,QRY-012 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-016 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-009,QRY-010 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-013,QRY-014 | support:- | counter:- | results:FCT-005,FCT-006,FCT-015 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-014,QRY-015 | support:- | counter:- | results:FCT-006,FCT-007,FCT-008,FCT-014 | final:GAP | gap:CAUSALITY
AXS-005 | attempts:QRY-016 | support:- | counter:- | results:FCT-011,FCT-012,FCT-013 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-009 | support:- | counter:- | results:FCT-001 | final:GAP | gap:RESOURCE_ATTRIBUTION
CLM-001 | attempts:QRY-009,SRC-001 | support:FCT-001 | counter:- | results:FCT-001 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-010,QRY-011,QRY-012,QRY-013,SRC-002,SRC-003,SRC-004,SRC-005 | support:FCT-002,FCT-003,FCT-004,FCT-016 | counter:- | results:FCT-002,FCT-003,FCT-004,FCT-016 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-009,QRY-014,QRY-015,SRC-001,SRC-006,SRC-007 | support:FCT-005,FCT-006,FCT-015 | counter:- | results:FCT-005,FCT-006,FCT-015 | final:SUPPORTED | gap:OUTCOME_STATUS
CLM-004 | attempts:QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018,QRY-024,SRC-001,SRC-002,SRC-003,SRC-004,SRC-005,SRC-006,SRC-007,SRC-008,SRC-009,SRC-010,SRC-016 | support:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-015,FCT-016 | counter:FCT-006,FCT-007,FCT-008,FCT-014 | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-015,FCT-016,FCT-006,FCT-007,FCT-008,FCT-014 | final:PARTIAL | gap:CAUSALITY
CLM-005 | attempts:QRY-016,QRY-017,QRY-018,SRC-008,SRC-009,SRC-010 | support:- | counter:FCT-007,FCT-008 | results:FCT-007,FCT-008 | final:REFUTED | gap:NONE
CLM-006 | attempts:QRY-015,QRY-024,SRC-007,SRC-016 | support:- | counter:FCT-006,FCT-014 | results:FCT-006,FCT-014 | final:REFUTED | gap:NONE
CLM-007 | attempts:QRY-021,QRY-022,QRY-023,SRC-013,SRC-014,SRC-015 | support:- | counter:FCT-011,FCT-012,FCT-013 | results:FCT-011,FCT-012,FCT-013 | final:REFUTED | gap:NONE
CLM-008 | attempts:QRY-009,QRY-010,QRY-014,SRC-001,SRC-002,SRC-006 | support:- | counter:FCT-001,FCT-002,FCT-005 | results:FCT-001,FCT-002,FCT-005 | final:REFUTED | gap:CORRUPTION

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
AXS-004 | AXS | GAP | CAUSALITY | The inspected corpus shows multiple autonomous political and market positions but no decision record assigning marginal causal weight to each.
AXS-006 | AXS | GAP | RESOURCE_ATTRIBUTION | Objective and advocacy are documented; this run does not establish a payment-to-decision or corruption chain.
CLM-003 | CLM | SUPPORTED | OUTCOME_STATUS | Draft process was not final adoption.
CLM-004 | CLM | PARTIAL | CAUSALITY | No inspected decision-maker record or causal design isolates lobbying from member-state bargaining, customer preferences and legal/technical arguments.
CLM-008 | CLM | REFUTED | CORRUPTION | No quid pro quo, payment-to-decision, unlawful act or hidden command is established.
CAU-003 | CAU | GAP | CAUSALITY | No marginal causal attribution can be made from the inspected decision record.

SEMANTIC_COUNTS_V1:LED:6|CLM:8|AXS:6|CAU:5|CTRL:5|ACT:3

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-009"],"evidence_excerpt":"Objective explicitly states deletion of sovereignty requirements.","kind":"MECHANISM","lead":"AWS registered a precise influence objective: remove EUCS sovereignty requirements.","linked_ids":["AXS-001","CLM-001","CAU-001"],"locator":"Bundestag Lobbyregister RV0008557","materiality":"DECISIVE","result_ids":["FCT-001","FCT-015"],"routes":["LINK","EXPAND"],"source_id":"SRC-001","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-010","QRY-011"],"evidence_excerpt":"Repeated coordinated public advocacy before draft change.","kind":"MECHANISM","lead":"Industry coalition publicly targeted EU member states, institutions and ENISA to reject sovereignty criteria.","linked_ids":["AXS-002","CLM-002","CAU-001"],"locator":"May 2023 joint industry statement","materiality":"DECISIVE","result_ids":["FCT-002","FCT-003","FCT-016"],"routes":["LINK","EXPAND"],"source_id":"SRC-002","status":"SATURATED"}
LED-003 | {"attempt_ids":["QRY-013"],"evidence_excerpt":"Draft moved toward technical/transparency criteria rather than nationality/control conditions.","kind":"EVENT","lead":"Observable normative delta: sovereignty requirements removed from 2024 draft.","linked_ids":["AXS-003","CLM-003","CAU-002"],"locator":"Reuters March 22 draft","materiality":"DECISIVE","result_ids":["FCT-005","FCT-015"],"routes":["LINK","AUDIT"],"source_id":"SRC-006","status":"SATURATED"}
LED-004 | {"attempt_ids":["QRY-014"],"evidence_excerpt":"Three ministers jointly called for sensitive-data protection including extraterritorial-law protection.","kind":"CONTROL","lead":"Counter-position existed among major member states: protection against extraterritorial law.","linked_ids":["AXS-004","CTRL-001","CAU-003"],"locator":"France/Germany/Italy 30 Oct 2023 communiqué","materiality":"DECISIVE","result_ids":["FCT-007","FCT-008"],"routes":["AUDIT","LINK"],"source_id":"SRC-008","status":"SATURATED"}
LED-005 | {"attempt_ids":["QRY-014"],"evidence_excerpt":"Big Tech welcomed, European providers opposed, vote delayed.","kind":"CONTROL","lead":"Outcome was a negotiated compromise with unresolved member-state and industry disagreement, not a transparent single-actor decision.","linked_ids":["AXS-005","CLM-005","CAU-003"],"locator":"Reuters Apr 16 expert-group report","materiality":"DECISIVE","result_ids":["FCT-006"],"routes":["AUDIT","LINK"],"source_id":"SRC-007","status":"SATURATED"}
LED-006 | {"attempt_ids":["QRY-016"],"evidence_excerpt":"Commission created explicit sovereignty assurance levels and scoring criteria.","kind":"CONTROL","lead":"Sovereignty returned via procurement framework, limiting any thesis of permanent Big-Tech policy capture.","linked_ids":["AXS-006","CTRL-004","CAU-004"],"locator":"Commission 2026 framework","materiality":"IMPORTANT","result_ids":["FCT-011","FCT-012","FCT-013"],"routes":["AUDIT","LINK"],"source_id":"SRC-013","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"AWS explicitly lobbied for removal of EUCS sovereignty requirements.","claimant":"registry evidence","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001"]}
CLM-002 | {"claim":"A broad industry campaign repeatedly opposed EUCS sovereignty requirements before the 2024 draft change.","claimant":"public industry records","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-002","FCT-003","FCT-004","FCT-016"]}
CLM-003 | {"claim":"The 2024 EUCS draft moved in the direction requested by these lobby actors by removing sovereignty requirements.","claimant":"draft-change observation","counter":"NONE_FOUND","gap":"Draft process was not final adoption.","gap_type":"OUTCOME_STATUS","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-005","FCT-006","FCT-015"]}
CLM-004 | {"claim":"Big Tech lobbying caused the removal of sovereignty requirements.","claimant":"strong capture/influence inference","counter":["FCT-006","FCT-007","FCT-008","FCT-014"],"gap":"No inspected decision-maker record or causal design isolates lobbying from member-state bargaining, customer preferences and legal/technical arguments.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-015","FCT-016"]}
CLM-005 | {"claim":"EU states unanimously opposed sovereignty requirements.","claimant":"simplified explanation","counter":["FCT-007","FCT-008"],"gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"REFUTED","support":"NONE_FOUND"}
CLM-006 | {"claim":"European cloud industry uniformly demanded strict sovereignty requirements.","claimant":"binary industry narrative","counter":["FCT-006","FCT-014"],"gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"REFUTED","support":"NONE_FOUND"}
CLM-007 | {"claim":"Removal from EUCS meant the EU permanently abandoned cloud-sovereignty policy.","claimant":"strong policy-capture narrative","counter":["FCT-011","FCT-012","FCT-013"],"gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"REFUTED","support":"NONE_FOUND"}
CLM-008 | {"claim":"The case proves corruption or unlawful capture.","claimant":"strong corruption inference","counter":["FCT-001","FCT-002","FCT-005"],"gap":"No quid pro quo, payment-to-decision, unlawful act or hidden command is established.","gap_type":"CORRUPTION","materiality":"DECISIVE","status":"REFUTED","support":"NONE_FOUND"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-009","QRY-010","QRY-011","QRY-012"],"axis":"ACTORS_RELATIONS","links":["LED-001","LED-002"],"question":"Who explicitly sought removal of sovereignty criteria and through which channels?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-016"],"sought_objects":["registered lobbying objective","industry statements","TTC escalation"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-009","QRY-010"],"axis":"MECHANISMS","links":["LED-001","LED-002"],"question":"What exact policy target was sought?","result_ids":["FCT-001","FCT-002","FCT-003"],"sought_objects":["ownership/control requirements","extraterritorial-law immunity","data localisation"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-013","QRY-014"],"axis":"IMPACT_RESPONSIBILITY","links":["LED-003"],"question":"Did EUCS text move in the requested direction?","result_ids":["FCT-005","FCT-006","FCT-015"],"sought_objects":["draft delta","assurance requirements"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-014","QRY-015"],"axis":"COUNTER_HYPOTHESES","gap":"The inspected corpus shows multiple autonomous political and market positions but no decision record assigning marginal causal weight to each.","gap_type":"CAUSALITY","links":["LED-004","LED-005"],"question":"Can the text change be attributed to Big Tech rather than member-state/customer/legal preferences?","result_ids":["FCT-006","FCT-007","FCT-008","FCT-014"],"sought_objects":["opposing state positions","industry split","decision record"],"status":"GAP"}
AXS-005 | {"attempt_ids":["QRY-016"],"axis":"RULES_CONTROLS","links":["LED-006"],"question":"Was the 2024 removal permanent abandonment of cloud sovereignty?","result_ids":["FCT-011","FCT-012","FCT-013"],"sought_objects":["2026 framework","procurement criteria","resumed EUCS work"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-009"],"axis":"RESOURCE_FLOWS","gap":"Objective and advocacy are documented; this run does not establish a payment-to-decision or corruption chain.","gap_type":"RESOURCE_ATTRIBUTION","links":["LED-001"],"question":"Do inspected sources close lobbying expenditure or direct financial inducement?","result_ids":["FCT-001"],"sought_objects":["spend","contracts","payments"],"status":"GAP"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"Intentional influence attempt on a specific normative target is directly documented.","counter":"NONE_FOUND","limit":"Access intensity and private meeting content are incomplete.","mechanism":"AWS/industry interests -> public/register advocacy -> EU/member-state decision venues","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-016"],"type":"LOBBYING_ATTEMPT"}
CAU-002 | {"causal_right":"Text trajectory and target congruence are observable.","counter":"NONE_FOUND","limit":"This establishes outcome congruence, not actor-specific causation.","mechanism":"draft with sovereignty conditions -> negotiated revision -> March 2024 draft without them","status":"SUPPORTED","support":["FCT-005","FCT-006","FCT-015"],"type":"POLICY_DELTA"}
CAU-003 | {"counter":["FCT-006","FCT-007","FCT-008","FCT-014"],"gap":"No marginal causal attribution can be made from the inspected decision record.","gap_type":"CAUSALITY","limit":"Multiple member states, user groups and industries had independent preferences.","mechanism":"industry lobbying -> removal of sovereignty requirements","status":"GAP","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-016"],"type":"LOBBYING_TO_POLICY_CAUSATION"}
CAU-004 | {"causal_right":"2026 procurement and legislative architecture explicitly reintroduce sovereignty metrics.","counter":["FCT-011","FCT-012","FCT-013"],"limit":"EUCS itself remained unresolved/resumed separately.","mechanism":"2024 removal -> enduring exclusion of sovereignty criteria from EU cloud policy","status":"REFUTED","support":"NONE_FOUND","type":"PERMANENT_CAPTURE"}
CAU-005 | {"causal_right":"Documented conduct is lobbying/advocacy, not a proven corrupt transaction.","counter":["FCT-001","FCT-002","FCT-005"],"limit":"Absence in this corpus is not proof no misconduct existed elsewhere.","mechanism":"commercial interest -> payment/quid pro quo -> policy change","status":"REFUTED","support":"NONE_FOUND","type":"CORRUPTION"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"lobbying objective != policy causation","status":"DONE","support":["FCT-001","FCT-005","FCT-006"]}
CTRL-002 | {"control":"member-state disagreement != Big Tech capture","status":"DONE","support":["FCT-006","FCT-007","FCT-008"]}
CTRL-003 | {"control":"European industry != single sovereignty position","status":"DONE","support":["FCT-006","FCT-014"]}
CTRL-004 | {"control":"2024 EUCS removal != permanent sovereignty abandonment","status":"DONE","support":["FCT-011","FCT-012","FCT-013"]}
CTRL-005 | {"control":"commercial lobbying != corruption","status":"DONE","support":["FCT-001","FCT-002"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Use EUCS as a positive case of explicit commercial lobbying aligned with an observable policy delta, while keeping actor-specific policy causation unclosed.","actor":"future synthesis/article protocol","intent":"preserve influence evidence without capture inflation","status":"DONE","support":["FCT-001","FCT-002","FCT-005","FCT-015"]}
ACT-002 | {"action":"Reopen causal attribution only on meeting minutes, internal drafting rationale, member-state voting/position records or other evidence assigning weight to lobby arguments.","actor":"future investigation","intent":"close causal gap","status":"DEFERRED","support":["FCT-006","FCT-007","FCT-008"]}
ACT-003 | {"action":"Represent 2026 sovereignty procurement as policy relocation/return, not proof that the 2024 lobbying had no effect.","actor":"future synthesis/article protocol","intent":"avoid false all-or-nothing policy model","status":"DONE","support":["FCT-011","FCT-012","FCT-013"]}

SEARCH_ACTIVITY_V1:WEB:8|FETCH:16|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"EMPTY","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL | mnemo | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | https://www.lobbyregister.bundestag.de/inhalte-der-interessenvertretung/regelungsvorhabensuche/RV0008557/8286 | AWS EUCS deletion sovereignty requirements lobbying register
QRY-002 | WEB | FOUND | - | https://www.uschamber.com/security/cybersecurity/joint-industry-statement-on-the-need-for-a-swift-adoption-of-the-eu-cybersecurity-certification-scheme-for-cloud-services-without-sovereignty-requirements | joint industry EUCS without sovereignty requirements May 2023
QRY-003 | WEB | FOUND | - | https://ccianet.org/news/2023/05/u-s-industry-raises-concerns-on-european-cloud-services-scheme-ahead-of-eu-u-s-ttc-meetings/ | CCIA EUCS ownership restrictions TTC May 2023
QRY-004 | WEB | FOUND | - | https://www.bsa.org/news-events/media/bsa-welcomes-latest-draft-of-eucs | BSA latest draft EUCS April 2024 sovereignty removed
QRY-005 | WEB | FOUND | - | https://www.reuters.com/technology/eu-drops-sovereignty-requirements-cybersecurity-certification-scheme-document-2024-04-03/ | EUCS sovereignty requirements removed March 2024 draft Reuters
QRY-006 | WEB | FOUND | - | https://presse.economie.gouv.fr/30102023-litalie-lallemagne-et-la-france-decident-de-renforcer-leur-cooperation-dans-le-domaine-de-lintelligence-artificielle/ | France Germany Italy EUCS extraterritorial laws October 2023
QRY-007 | WEB | FOUND | - | https://questions.assemblee-nationale.fr/q16/16-12713QE.htm | France answer EUCS SecNumCloud April 2024
QRY-008 | WEB | FOUND | - | https://commission.europa.eu/news-and-media/news/sovereign-cloud-framework-explained-2026-06-01_en | Commission cloud sovereignty framework 2026
QRY-009 | FETCH | FOUND | SRC-001 | https://www.lobbyregister.bundestag.de/inhalte-der-interessenvertretung/regelungsvorhabensuche/RV0008557/8286 | AWS German lobbying-register filing inspected
QRY-010 | FETCH | FOUND | SRC-002 | https://www.uschamber.com/security/cybersecurity/joint-industry-statement-on-the-need-for-a-swift-adoption-of-the-eu-cybersecurity-certification-scheme-for-cloud-services-without-sovereignty-requirements | 2023 joint industry statement inspected
QRY-011 | FETCH | FOUND | SRC-003 | https://ccianet.org/news/2023/05/u-s-industry-raises-concerns-on-european-cloud-services-scheme-ahead-of-eu-u-s-ttc-meetings/ | CCIA 2023 TTC lobbying statement inspected
QRY-012 | FETCH | FOUND | SRC-004 | https://www.bsa.org/news-events/media/bsa-welcomes-latest-draft-of-eucs | BSA April 2024 latest-draft statement inspected
QRY-013 | FETCH | FOUND | SRC-005 | https://www.bsa.org/news-events/media/gda-and-bsa-support-new-version-of-eucs | BSA/GDA support statement inspected
QRY-014 | FETCH | FOUND | SRC-006 | https://www.reuters.com/technology/eu-drops-sovereignty-requirements-cybersecurity-certification-scheme-document-2024-04-03/ | Reuters March 2024 draft-change report inspected
QRY-015 | FETCH | FOUND | SRC-007 | https://www.reuters.com/technology/cybersecurity/vote-eu-cybersecurity-label-delayed-may-sources-say-2024-04-16/ | Reuters April 2024 expert-group report inspected
QRY-016 | FETCH | FOUND | SRC-008 | https://presse.economie.gouv.fr/30102023-litalie-lallemagne-et-la-france-decident-de-renforcer-leur-cooperation-dans-le-domaine-de-lintelligence-artificielle/ | France/Germany/Italy official trilateral statement inspected
QRY-017 | FETCH | FOUND | SRC-009 | https://www.mimit.gov.it/en/media-tools/news/italy-germany-and-france-agree-on-strengthening-their-cooperation-on-artificial-intelligence | Italian official version of trilateral statement inspected
QRY-018 | FETCH | FOUND | SRC-010 | https://questions.assemblee-nationale.fr/q16/16-12713QE.htm | French parliamentary answer on sovereign cloud/EUCS inspected
QRY-019 | FETCH | FOUND | SRC-011 | https://www.senat.fr/questions/base/2023/qSEQ231108911.html | French Senate answer on AWS sovereign cloud inspected
QRY-020 | FETCH | FOUND | SRC-012 | https://www.enisa.europa.eu/topics/consultation-on-the-draft-of-the-candidate-certification-scheme-on-cloud-services-eucs-closed | ENISA EUCS candidate consultation page inspected
QRY-021 | FETCH | FOUND | SRC-013 | https://commission.europa.eu/news-and-media/news/sovereign-cloud-framework-explained-2026-06-01_en | Commission 2026 sovereign-cloud framework page inspected
QRY-022 | FETCH | FOUND | SRC-014 | https://commission.europa.eu/news-and-media/news/commission-advances-cloud-sovereignty-through-strategic-procurement-2026-04-17_en | Commission 2026 sovereign procurement result inspected
QRY-023 | FETCH | FOUND | SRC-015 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A52026PC0502 | 2026 EU cloud/AI proposal inspected
QRY-024 | FETCH | FOUND | SRC-016 | https://www.cispe.cloud/cispe-statement-on-current-eucs-compromise-draft/ | CISPE April 2024 compromise statement inspected

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:other:bundestag | BUNDESTAG-AWS-EUCS-RV0008557 | Bundestag Lobbyregister — AWS EUCS sovereignty requirements | 2024-06-28 | 2026-09-11T22:26:00Z | explicit objective: deletion of sovereignty requirements | https://www.lobbyregister.bundestag.de/inhalte-der-interessenvertretung/regelungsvorhabensuche/RV0008557/8286
SRC-002 | ◉ | fam:other:uschamber | USCHAMBER-EUCS-20230523 | Joint industry statement — EUCS without sovereignty requirements | 2023-05-23 | 2026-09-11T22:26:00Z | calls EU/MS/ENISA to reject sovereignty requirements; says multiple industry actors and member states had opposed them | https://www.uschamber.com/security/cybersecurity/joint-industry-statement-on-the-need-for-a-swift-adoption-of-the-eu-cybersecurity-certification-scheme-for-cloud-services-without-sovereignty-requirements
SRC-003 | ◉ | fam:other:ccia | CCIA-EUCS-20230525 | CCIA — EUCS concerns ahead of TTC | 2023-05-25 | 2026-09-11T22:26:00Z | letter to US administration; asks removal of nationality-based ownership restrictions | https://ccianet.org/news/2023/05/u-s-industry-raises-concerns-on-european-cloud-services-scheme-ahead-of-eu-u-s-ttc-meetings/
SRC-004 | ◉ | fam:other:bsa | BSA-EUCS-20240411 | BSA welcomes latest EUCS draft | 2024-04-11 | 2026-09-11T22:26:00Z | welcomes latest draft and asks implementing regulation without sovereignty requirements | https://www.bsa.org/news-events/media/bsa-welcomes-latest-draft-of-eucs
SRC-005 | ◉ | fam:other:bsa | BSA-GDA-EUCS-20240411 | GDA and BSA support new EUCS version | 2024-04-11 | 2026-09-11T22:26:00Z | supports version understood to remove sovereignty requirements | https://www.bsa.org/news-events/media/gda-and-bsa-support-new-version-of-eucs
SRC-006 | ◉ | fam:other:reuters | REUTERS-EUCS-20240403 | Reuters — EU drops sovereignty requirements in draft | 2024-04-03 | 2026-09-11T22:26:00Z | March 22 draft removed prior stringent sovereignty conditions; only transparency requirements described | https://www.reuters.com/technology/eu-drops-sovereignty-requirements-cybersecurity-certification-scheme-document-2024-04-03/
SRC-007 | ◉ | fam:other:reuters | REUTERS-EUCS-20240416 | Reuters — EUCS vote delayed | 2024-04-16 | 2026-09-11T22:26:00Z | Belgian compromise removed prior sovereignty requirements; welcomed by Big Tech; opposed by European providers; no vote | https://www.reuters.com/technology/cybersecurity/vote-eu-cybersecurity-label-delayed-may-sources-say-2024-04-16/
SRC-008 | ◈ | fam:other:fr-gov | FR-DE-IT-EUCS-20231030 | France/Germany/Italy trilateral communiqué | 2023-10-30 | 2026-09-11T22:26:00Z | three ministers call for protection of sensitive data including against extraterritorial laws | https://presse.economie.gouv.fr/30102023-litalie-lallemagne-et-la-france-decident-de-renforcer-leur-cooperation-dans-le-domaine-de-lintelligence-artificielle/
SRC-009 | ◈ | fam:other:it-gov | IT-DE-FR-EUCS-20231030 | Italy/Germany/France official statement | 2023-10-30 | 2026-09-11T22:26:00Z | same EUCS protection objective; independent government publication but same political event | https://www.mimit.gov.it/en/media-tools/news/italy-germany-and-france-agree-on-strengthening-their-cooperation-on-artificial-intelligence
SRC-010 | ◈ | fam:other:fr-parliament | AN-Q12713-EUCS | French government answer — AWS sovereign cloud/EUCS | 2024-04-16 | 2026-09-11T22:26:00Z | France says it consistently defends robust EUCS protection against extraterritorial laws | https://questions.assemblee-nationale.fr/q16/16-12713QE.htm
SRC-011 | ◈ | fam:other:fr-parliament | SENAT-Q08911-AWS | French government answer — AWS European Sovereign Cloud | 2024-04-18 | 2026-09-11T22:26:00Z | SecNumCloud protection against extraterritorial law remains French trusted-cloud criterion | https://www.senat.fr/questions/base/2023/qSEQ231108911.html
SRC-012 | ◈ | fam:other:enisa | ENISA-EUCS-CANDIDATE | ENISA candidate EUCS overview | 2021 | 2026-09-11T22:26:00Z | voluntary EU-wide cloud certification, three assurance levels; baseline institutional scope | https://www.enisa.europa.eu/topics/consultation-on-the-draft-of-the-candidate-certification-scheme-on-cloud-services-eucs-closed
SRC-013 | ◈ | fam:other:eu-commission | EC-CLOUD-SOV-FRAMEWORK-20260601 | Commission — Sovereign Cloud Framework explained | 2026-06-01 | 2026-09-11T22:26:00Z | Commission uses sovereignty scores/criteria in procurement and presents them as digital-sovereignty benchmark | https://commission.europa.eu/news-and-media/news/sovereign-cloud-framework-explained-2026-06-01_en
SRC-014 | ◈ | fam:other:eu-commission | EC-CLOUD-PROC-20260417 | Commission advances cloud sovereignty through procurement | 2026-04-17 | 2026-09-11T22:26:00Z | €180m sovereign-cloud procurement; measurable sovereignty criteria and SEAL levels | https://commission.europa.eu/news-and-media/news/commission-advances-cloud-sovereignty-through-strategic-procurement-2026-04-17_en
SRC-015 | ◈ | fam:other:eurlex | EURLEX-CADA-2026 | EU proposal — cloud sovereignty framework and EUCS resumption | 2026 | 2026-09-11T22:26:00Z | proposal establishes cloud sovereignty framework and says work will resume on EUCS | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A52026PC0502
SRC-016 | ◉ | fam:other:cispe | CISPE-EUCS-20240412 | CISPE statement on EUCS compromise | 2024-04-12 | 2026-09-11T22:26:00Z | supports agreement but emphasizes customer choice and sovereignty needs; control against binary US-vs-EU industry model | https://www.cispe.cloud/cispe-statement-on-current-eucs-compromise-draft/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.lobbyregister.bundestag.de/inhalte-der-interessenvertretung/regelungsvorhabensuche/RV0008557/8286 | other:bundestag | 2024-06-28 | AWS registered lobbying objective | Bundestag lobbying register records AWS EMEA objective on EUCS as deletion of sovereignty requirements, because AWS argued they did not strengthen cybersecurity. | -
FCT-002 | FACT | ✧ | https://www.uschamber.com/security/cybersecurity/joint-industry-statement-on-the-need-for-a-swift-adoption-of-the-eu-cybersecurity-certification-scheme-for-cloud-services-without-sovereignty-requirements | other:uschamber | 2023-05-23 | Cross-industry demand to reject sovereignty criteria | A broad industry statement called on EU member states, EU institutions and ENISA to reject EUCS sovereignty requirements and described them as politically motivated. | -
FCT-003 | FACT | ✧ | https://ccianet.org/news/2023/05/u-s-industry-raises-concerns-on-european-cloud-services-scheme-ahead-of-eu-u-s-ttc-meetings/ | other:ccia | 2023-05-25 | US industry escalation through TTC channel | CCIA and other US groups sent concerns to the US administration ahead of the EU-US TTC and advocated removal of nationality-based ownership restrictions. | -
FCT-004 | FACT | ✧ | https://www.bsa.org/news-events/media/bsa-welcomes-latest-draft-of-eucs | other:bsa | 2024-04-11 | Industry support after draft changed | BSA/GDA publicly welcomed the new draft specifically because sovereignty requirements had been removed and urged EU institutions to proceed without reintroducing them. | -
FCT-005 | FACT | ✧ | https://www.reuters.com/technology/eu-drops-sovereignty-requirements-cybersecurity-certification-scheme-document-2024-04-03/ | other:reuters | 2024-03-22 | Draft policy delta | Reuters reported that the March 22 2024 EUCS draft removed prior stringent sovereignty requirements and retained transparency about data location, processing and applicable laws. | -
FCT-006 | FACT | ✧ | https://www.reuters.com/technology/cybersecurity/vote-eu-cybersecurity-label-delayed-may-sources-say-2024-04-16/ | other:reuters | 2024-04-15/16 | Compromise contested by opposing industries | Reuters reported the Belgian compromise removed prior sovereignty requirements, was welcomed by Big Tech, opposed by European providers, and failed to reach a vote at that meeting. | -
FCT-007 | FACT | ✧ | https://presse.economie.gouv.fr/30102023-litalie-lallemagne-et-la-france-decident-de-renforcer-leur-cooperation-dans-le-domaine-de-lintelligence-artificielle/ | other:fr-gov,other:it-gov | 2023-10-30 | Government counter-position | France, Germany and Italy jointly called for EU cloud certification protecting sensitive data, including against extraterritorial laws. | -
FCT-008 | FACT | ✧ | https://questions.assemblee-nationale.fr/q16/16-12713QE.htm | other:fr-parliament | 2024-04-16 | French position persisted through change period | French government said it continued to defend EUCS protection for sensitive data against extraterritorial legislation. | -
FCT-009 | FACT | ✧ | https://www.senat.fr/questions/base/2023/qSEQ231108911.html | other:fr-parliament | 2024-04-18 | French national certification control | France stated that AWS or any provider must meet SecNumCloud 3.2, including protection against extra-European law, to obtain trusted-cloud qualification in France. | -
FCT-010 | FACT | ✧ | https://www.enisa.europa.eu/topics/consultation-on-the-draft-of-the-candidate-certification-scheme-on-cloud-services-eucs-closed | other:enisa | 2021 | EUCS institutional baseline | ENISA describes EUCS as voluntary EU-wide cloud certification with basic, substantial and high assurance levels and technical-security harmonisation goals. | -
FCT-011 | FACT | ✧ | https://commission.europa.eu/news-and-media/news/sovereign-cloud-framework-explained-2026-06-01_en | other:eu-commission | 2026-06-01 | Sovereignty later reintroduced through procurement framework | Commission states its Cloud Sovereignty Framework uses explicit sovereignty/resilience assurance levels and 48 criteria and is intended as a public-sector benchmark. | -
FCT-012 | FACT | ✧ | https://commission.europa.eu/news-and-media/news/commission-advances-cloud-sovereignty-through-strategic-procurement-2026-04-17_en | other:eu-commission | 2026-04-17 | Commission applied sovereignty criteria in procurement | Commission used its sovereignty framework in a €180m procurement and required at least a data-sovereignty assurance level for eligibility. | -
FCT-013 | FACT | ✧ | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A52026PC0502 | other:eurlex | 2026 | EU architecture shifted rather than sovereignty disappearing | A 2026 Commission proposal establishes a cloud sovereignty framework and states that work will resume on EUCS, showing the 2024 EUCS removal did not amount to permanent abandonment of sovereignty policy. | -
FCT-014 | FACT | ✧ | https://www.cispe.cloud/cispe-statement-on-current-eucs-compromise-draft/ | other:cispe | 2024-04-12 | European cloud-provider position was not monolithic | CISPE backed reaching an EUCS compromise while preserving customer sovereignty choice and special high-sovereignty use cases, complicating a simple Big-Tech-versus-Europe model. | -
FCT-015 | FACT | ✧ | https://www.lobbyregister.bundestag.de/inhalte-der-interessenvertretung/regelungsvorhabensuche/RV0008557/8286 | other:bundestag,other:reuters | 2024 | Lobbying-target / policy-delta congruence | AWS had an explicit registered objective to delete sovereignty requirements; the March 2024 draft had already removed them. Congruence and chronology are supported; causal attribution is not closed by those facts alone. | -
FCT-016 | FACT | ✧ | https://www.uschamber.com/security/cybersecurity/joint-industry-statement-on-the-need-for-a-swift-adoption-of-the-eu-cybersecurity-certification-scheme-for-cloud-services-without-sovereignty-requirements | other:bsa,other:ccia,other:uschamber | 2023-2024 | Sustained multi-channel industry pressure | Industry pressure against sovereignty criteria was repeated across joint statements, direct advocacy to EU actors, and escalation through US-government/TTC channels before and during the draft change. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-003
FCT-004 | SRC-004,SRC-005
FCT-005 | SRC-006
FCT-006 | SRC-007
FCT-007 | SRC-008,SRC-009
FCT-008 | SRC-010
FCT-009 | SRC-011
FCT-010 | SRC-012
FCT-011 | SRC-013
FCT-012 | SRC-014
FCT-013 | SRC-015
FCT-014 | SRC-016
FCT-015 | SRC-001,SRC-006
FCT-016 | SRC-002,SRC-003,SRC-004,SRC-005

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
ATTEMPT-001 | {"created_at":"2026-09-11T22:30:28.252162+00:00","fact_mem":{},"mnemo_row":"BLOCKED:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":16,"eligible":16,"failure":0,"success":0}}

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
FCT-013 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-014 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-015 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-016 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
