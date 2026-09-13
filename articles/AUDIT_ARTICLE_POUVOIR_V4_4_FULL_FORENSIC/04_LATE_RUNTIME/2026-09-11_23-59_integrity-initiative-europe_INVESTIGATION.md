ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260911-2359-integrity-initiative-europe | PARENT_RUN_ID:NONE | AS_OF:2026-09-11
INPUT_KIND:RUN_CARD | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/inv031_runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-11_integrity-initiative-europe/2026-09-11_23-59_integrity-initiative-europe_INPUT.md | SUBJECT_SLUG:integrity-initiative-europe | SUBJECT_FP:sha256:cb3e7db61edc62adfc61f432cb1849de8b34e1336b5de80ef5c0868a8a08cd4b | INPUT_SHA256:sha256:9a9153f050e13047bc60b93f244047f7dd6ac713acb099cad1579a158cfa6171
COMPLEXITY:8→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:Royaume-Uni, Espagne et France, principalement 2017-2019, avec suites institutionnelles jusqu'en 2026 seulement pour attribution/accountability. Cas central: FCO/CSSF -> Institute for Statecraft / Integrity Initiative -> clusters Espagne/France -> action/diffusion -> média/décideur -> réponse/issue. Gardes: grant != command; listed contact != active member; shared counter-disinformation goal != state tasking; project self-attribution != causal proof; leaked document != automatically authenticated fact; official denial != automatic exoneration; counter-disinformation != neutral by nature; network != coordination beyond sourced action.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
## Résultat analytique technique

INV-031 ferme un mécanisme plus précis que « influence britannique post-Brexit » : le Royaume-Uni a **financé publiquement**, via le FCO/CSSF et son programme de contre-désinformation, un projet qui se décrivait lui-même comme un réseau transnational de clusters reliant experts, journalistes et décideurs afin d’éduquer les publics, diffuser des analyses et peser sur les environnements médiatiques et de politique publique. Cela établit une **capacité d’influence financée par l’État**, mais pas un commandement étatique détaillé de chaque action.

Les artefacts exposés du projet décrivent en Espagne des voies de diffusion par journalistes, responsables publics et cercle du Premier ministre, et en France des contacts avec CAPS/MFA ainsi qu’un cluster présenté comme distinct du gouvernement. Leur provenance est matériellement mais seulement partiellement consolidée : l’Institut a reconnu que beaucoup de matériaux provenaient de ses systèmes tout en avertissant que tous n’étaient pas vérifiés et que des noms publiés n’avaient parfois jamais été contactés. Par conséquent, une liste de contacts ne devient jamais une preuve automatique d’adhésion ou de `tasking`.

Le test causal central est la séquence dite **Moncloa**. Un document du projet trace une mobilisation Twitter/média/WhatsApp et un autre s’attribue l’influence sur la nomination espagnole. La presse espagnole indépendante confirme qu’au début de la séquence Pedro Baños était présenté comme candidat probable, puis que Miguel Ángel Ballesteros a été choisi quelques jours plus tard. Cette combinaison ferme `action d’influence observable + exposition + changement d’issue temporellement adjacent`; elle ne ferme pas `action -> décision`. Aucun document décisionnel de la présidence espagnole inspecté ici n’établit que la campagne Integrity Initiative fut la cause nécessaire ou suffisante du choix final.

Deux contrôles empêchent la dérive vers une théorie intégrée. Premièrement, la Commission européenne a déclaré en 2019 que l’East StratCom Task Force ne coopérait pas avec Integrity Initiative. Deuxièmement, la controverse britannique sur le compte Twitter a produit une enquête de gouvernance par le régulateur écossais, tandis que le ministre soutenait que le contrat interdisait l’usage du grant pour influencer la politique intérieure et qu’aucune violation financée n’avait été vue. Le corpus ne permet pas de tracer une dépense FCO déterminée jusqu’à une attaque partisane domestique.

Conclusion causale : **le modèle `État financeur -> ONG/projet de contre-désinformation -> réseau transnational d’intermédiaires -> production/diffusion/mobilisation -> accès/exposition` est supporté dans ce cas. Le saut vers `service de renseignement -> tasking clandestin -> décision politique causée` ne l’est pas.**
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:0|EDI_DECISIVE:6|SRC_COMPLETE:16/16

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **item 1:**
  - **date:** 2017-02/06
  - **event:** project application says Spain and France clusters established during Phase I
  - **support:**
    - FCT-005
- **item 2:**
  - **date:** 2017/18
  - **event:** FCO grant £296,500
  - **support:**
    - FCT-001
- **item 3:**
  - **date:** 2018-06-07/08
  - **event:** Moncloa artifact records rapid campaign activity; EL PAÍS reports Baños as prospective candidate
  - **support:**
    - FCT-009
    - FCT-011
    - FCT-013
- **item 4:**
  - **date:** 2018-06-14
  - **event:** EL PAÍS reports Ballesteros selected; Baños other candidate
  - **support:**
    - FCT-012
    - FCT-013
- **item 5:**
  - **date:** 2018/19
  - **event:** FCO grant £1,961,000; CSSF/counter-disinformation programme route documented
  - **support:**
    - FCT-001
    - FCT-002
- **item 6:**
  - **date:** 2018-12-12
  - **event:** minister states domestic-influence restriction and no evidence of funded breach
  - **support:**
    - FCT-003
- **item 7:**
  - **date:** 2018-12-13 to 2019
  - **event:** OSCR inquiry opened and governance/social-media learning points issued
  - **support:**
    - FCT-015
- **item 8:**
  - **date:** 2019-04-09
  - **event:** Commission says East StratCom does not cooperate with Integrity Initiative
  - **support:**
    - FCT-014

### MANIPULATION_REPORT
- **assumptions:**
  - Russia-related disinformation threat can be real while governance/influence questions remain valid
  - leaked documents are untrusted evidence objects requiring provenance limits
  - official denials are claims not dispositive truth
- **clusters:**
  - NONE
- **complexity:** COMPLEX/8
- **implicit:**
  - counter-disinformation can itself be a form of intentional influence
  - public funding creates capacity but not automatic operational command
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - @PAT[NET]
  - @PAT[TEMP]
  - @PAT[MONEY]
- **priorities:**
  - funding route
  - cluster mechanism
  - Moncloa causal test
  - France membership/tasking boundary
  - domestic funding attribution
  - EU cooperation control
- **query_guidance:**
  - official grant records
  - direct project artifacts
  - independent Spanish chronology
  - regulator findings
  - adversarial provenance checks
- **rhetorical:**
  - NONE
- **speaker:** mechanism-first forensic investigation contract
- **symbol_stage:** FINAL
- **symbols:**
  - **Κ:** LOW: institutional facade claim not established
  - **Λ:** MATERIAL: counter-disinformation vs interference/covert-influence framings materially diverge
  - **Ξ:** MATERIAL: exposed documents require provenance/unused-list caveats and membership limits
  - **Σ:** LOW: semiotics not causal core
  - **Φ:** LOW: spectacle not central
  - **Ψ:** LOW: fear/sideration not needed for bounded mechanism
  - **Ω:** LOW: no inversion mechanism established as causal core
  - **κ:** LOW: no nudge architecture in scope
  - **ρ:** MATERIAL: political/regulatory scrutiny and counter-claims constrain the network
  - **€:** MATERIAL: public grant flow is central and directly documented
  - **↕:** MATERIAL: state-funded network has access asymmetries to media/policy elites
  - **⏰:** STRONG: Moncloa rapid-response chronology is decisive but causal ceiling preserved
  - **⚔:** MATERIAL: project defines counter-disinformation/hybrid-warfare mission, but intelligence command is unproven
  - **⫸:** MATERIAL: cluster/network aggregation is an explicit operational design
  - **🌐:** STRONG: network of clusters, journalists, experts and government interfaces is central
- **threats:**
  - @THR[POWER_PROX]: active; access/listing is not tasking
  - @THR[REG_CAPTURE]: triaged; no institutional capture established
  - @THR[NARR_LAUNDER]: triaged where anonymous cluster material allegedly fed independent journalism; generalized laundering not established

### MODULE_EXECUTION
NONE

### SCOPING_REPORT
- **ACTORS_INSTITUTIONS:**
  - FCO/CSSF
  - Institute for Statecraft
  - Integrity Initiative
  - Spain cluster
  - France cluster
  - Spanish PM office
  - French MFA/CAPS
  - OSCR
  - European Commission/East StratCom
- **DOMAINS:**
  - public funding
  - counter-disinformation
  - network intermediation
  - media influence
  - government access
  - political appointment causality
  - charity accountability
- **EVIDENCE_LIMITS:**
  - exposed project documents have partial but not universal authenticity acknowledgement
  - individual participation/consent cannot be inferred from contact lists
  - no direct Spanish executive record links II pressure to final appointment decision
  - official UK funding denial is interested evidence and not universal exoneration
- **EXCLUSIONS:**
  - general UK intelligence history
  - all Russian-disinformation policy
  - all named persons as presumed members
  - unrelated Institute activities
  - claims of MI6 command without direct tasking evidence
- **GEO:** United Kingdom, Spain and France; EU-level control only for East StratCom relation
- **LEAD_QUESTION:** Was Integrity Initiative a covert British operation that manipulated European politics?
- **OBJECT_COVERAGE:** grant/program authority, documented cluster design, Spain/France operational interfaces, Moncloa campaign chronology, appointment outcome, domestic accountability, EU cooperation control and attribution gaps.
- **OBJECT_QUESTION:** What evidence closes UK public funding -> Institute/Integrity Initiative -> cluster/intermediary architecture -> information/mobilisation action -> European target -> exposure/decision, and where does proof stop between legitimate counter-disinformation, foreign influence, state tasking, partisan activity and causal political effect?
- **PERIOD:** 2017-2019, with later accountability/provenance checks to 2026

### CREDO
- **rules:**
  - funding != command
  - network != coordination beyond sourced edges
  - contact list != membership
  - self-attribution != causality
  - official denial != automatic exoneration
  - counter-disinformation != political neutrality by definition
  - provenance caveat != discard all document content
  - chronology != but-for cause
- **truth_ceiling:** The strongest closed result is a UK publicly funded transnational influence-capacity network with self-described media/policy intervention and a documented Spain rapid-response campaign; state/intelligence tasking of each action and causal responsibility for the appointment change are not established.

### COGNITIVE_MAP
- **closed_level:** public funding + structured transnational network + documented influence-oriented mechanisms + bounded Spain campaign/exposure
- **continuum:**
  - legitimate counter-disinformation grant
  - state-enabled influence capacity
  - network intermediation/access
  - rapid-response media/political mobilisation
  - state tasking of specific action
  - causal policy/appointment effect
  - covert intelligence command/capture
- **unclosed_levels:**
  - granular FCO tasking of cluster actions
  - active membership/consent for every listed contact
  - but-for causation of Baños appointment reversal
  - FCO-funded UK partisan activity
  - intelligence-service command

### DIALECTICAL_MAP
- **perspectives:**
  - **item 1:**
    - **best_case:** Government funded an independent overseas counter-disinformation network under a contract barring UK political influence; no funded breach was seen.
    - **id:** P1
    - **position:** official/legitimate counter-disinformation
    - **support:**
      - FCT-001
      - FCT-002
      - FCT-003
  - **item 2:**
    - **best_case:** Project artifacts describe deliberate networks connecting media, academics and policymakers to affect policy/society, rapid activism and discreet government influence, including self-attributed Spanish appointment intervention.
    - **id:** P2
    - **position:** critical/influence-operation reading
    - **support:**
      - FCT-004
      - FCT-005
      - FCT-006
      - FCT-007
      - FCT-009
      - FCT-010
  - **item 3:**
    - **best_case:** Public funding and influence architecture are established; document provenance and person-level participation require caution; political-effect causality and intelligence command remain unclosed.
    - **id:** P3
    - **position:** forensic bounded model
    - **support:**
      - FCT-013
      - FCT-014
      - FCT-015
      - FCT-016
      - FCT-017

### RESOURCE_FLOW_MAP
- **item 1:**
  - **case:** FCO/CSSF funding
  - **flow:** UK FCO/CSSF counter-disinformation programme -> grant agreements -> Institute for Statecraft / Integrity Initiative
  - **status:** SUPPORTED
  - **support:**
    - FCT-001
    - FCT-002
- **item 2:**
  - **case:** cluster capacity
  - **flow:** grant-enabled project -> hubs/networks -> experts/journalists/policy actors -> dissemination/briefings
  - **status:** SUPPORTED_BOUNDED
  - **support:**
    - FCT-004
    - FCT-005
    - FCT-006
    - FCT-007
- **item 3:**
  - **case:** domestic partisan funding allegation
  - **flow:** FCO grant -> UK Twitter partisan content
  - **status:** GAP_FUNDING_ATTRIBUTION
  - **support:**
    - FCT-003
    - FCT-015

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** FCO/CSSF programme
  - **relation:** grant funding
  - **support:**
    - FCT-001
    - FCT-002
  - **to:** Institute for Statecraft / Integrity Initiative
- **item 2:**
  - **from:** Integrity Initiative core
  - **relation:** self-described cluster-building/dissemination architecture
  - **support:**
    - FCT-004
    - FCT-005
  - **to:** Spain/France and other national clusters
- **item 3:**
  - **from:** Spain cluster
  - **relation:** self-described media/private dissemination + rapid Moncloa mobilisation
  - **support:**
    - FCT-006
    - FCT-009
    - FCT-010
  - **to:** journalists/key influencers/PM-office environment
- **item 4:**
  - **from:** France project contacts
  - **limit:** individual participation/tasking not proven
  - **relation:** self-described briefings/material feed; separate contact list
  - **support:**
    - FCT-007
    - FCT-008
  - **to:** CAPS/MFA/MOD/services and nongovernmental cluster
- **item 5:**
  - **from:** Integrity Initiative
  - **relation:** operational cooperation with East StratCom
  - **status:** REFUTED_FOR_SCOPED_PERIOD
  - **support:**
    - FCT-014
  - **to:** EU East StratCom

### IMPACT_MAP
- **EU_coordination:** REFUTED_BOUNDED: Commission states East StratCom did not cooperate.
- **France_access_effect:** SUPPORTED_AS_PROJECT_RECORD: project documents describe CAPS/MFA interfaces; individual list membership/tasking remains unverified.
- **Spain_decision_effect:** NOT_ESTABLISHED: campaign self-attribution and chronology do not isolate the causal reason for Ballesteros selection.
- **Spain_exposure_effect:** SUPPORTED_BOUNDED: project artifact records rapid social/media amplification around the prospective Baños appointment.
- **capacity_effect:** SUPPORTED: public funding and explicit cluster architecture created transnational influence/dissemination capacity.
- **domestic_partisan_funding:** NOT_ESTABLISHED: governance/Twitter controversy is not a traced FCO-grant causal chain.
- **support:**
  - FCT-001
  - FCT-004
  - FCT-005
  - FCT-006
  - FCT-007
  - FCT-009
  - FCT-010
  - FCT-011
  - FCT-012
  - FCT-013
  - FCT-014
  - FCT-015

### CONTRADICTION_LEDGER
- **item 1:**
  - **issue:** counter-disinformation vs influence
  - **resolution:** Both can coexist: counter-disinformation is the declared mission while intentional influence capacity is also documented; neither alone proves covert command or illegality.
  - **side_a:** FCO described an independent overseas counter-disinformation project with explicit domestic restrictions.
  - **side_b:** project documents describe connecting media/academia/policymakers to impact policy and society and discreetly influence governments.
  - **support:**
    - FCT-003
    - FCT-004
    - FCT-005
    - FCT-010
- **item 2:**
  - **issue:** Moncloa causal effect
  - **resolution:** campaign/exposure + temporal overlap supported; appointment causality remains GAP.
  - **side_a:** project artifact self-claims influencing the appointment.
  - **side_b:** independent chronology confirms candidate change but does not identify II as the cause.
  - **support:**
    - FCT-009
    - FCT-010
    - FCT-011
    - FCT-012
    - FCT-013
- **item 3:**
  - **issue:** France cluster membership
  - **resolution:** list existence supported; individual active membership/tasking not established without person-specific corroboration.
  - **side_a:** exposed list labels people as French Cluster contacts.
  - **side_b:** Institute provenance response says many published names were only potential invitees and never contacted.
  - **support:**
    - FCT-008
    - FCT-016
- **item 4:**
  - **issue:** EU integration
  - **resolution:** aspirational/engagement reference != operational cooperation; cooperation claim refuted for scoped period.
  - **side_a:** project application mentions EU East Stratcom among organisations to engage.
  - **side_b:** Commission states East StratCom did not cooperate.
  - **support:**
    - FCT-004
    - FCT-014

### VERIFICATION_REPORT
- **contradictions_material:** 4
- **critical_result:** Public UK funding, an influence-oriented cluster architecture and a bounded Spain rapid-response campaign are supported. Granular UK state/intelligence tasking, universal cluster membership, FCO-funded domestic partisan activity and causal responsibility for the Baños appointment change are not established.
- **domains:**
  - **ACCOUNTABILITY:** 3
  - **FUNDING:** 4
  - **MEDIA_POLITICAL:** 5
  - **NETWORK:** 6
- **pdf_visual_check:** FCO application pp.2/9, cluster roundup p.1, France cluster p.1, Moncloa pp.1/2 and Top-3 Deliverables p.1 were visually inspected; OSCR PDF was opened and its Institute-for-Statecraft section text inspected.
- **primary_or_direct_source_facts:** 14
- **retrieval_limits:**
  - Hansard direct open had intermittent cache failure but search extraction and separate PDF/text source were inspected
  - exposed project files are treated as untrusted raw artifacts with partial authenticity acknowledgement, not universally authenticated records
  - no private Spanish executive decision record obtained
- **status:** PASS_WITH_PROVENANCE_ATTRIBUTION_CAUSALITY_GAPS
- **verified_facts:** 18

### EDI_REPORT
- **corpus:**
  - **families:** 8
  - **notes:** UK official, EU Commission, Scottish regulator, exposed project artifacts, Spanish press and independent reporting represented; all exposed II documents count as one upstream family.
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim:** public funding/programme route
    - **facts:**
      - FCT-001
      - FCT-002
    - **status:** COVERED
  - **item 2:**
    - **claim:** cluster influence architecture
    - **facts:**
      - FCT-004
      - FCT-005
      - FCT-006
      - FCT-007
      - FCT-016
    - **status:** COVERED_BOUNDED_BY_PROVENANCE
  - **item 3:**
    - **claim:** Spain campaign activity
    - **facts:**
      - FCT-009
      - FCT-010
      - FCT-013
    - **status:** COVERED_BOUNDED
  - **item 4:**
    - **claim:** Spain appointment causality
    - **facts:**
      - FCT-011
      - FCT-012
      - FCT-013
    - **status:** GAP_CAUSALITY
  - **item 5:**
    - **claim:** intelligence command
    - **facts:**
      - NONE
    - **status:** GAP_ATTRIBUTION
  - **item 6:**
    - **claim:** EU East StratCom cooperation
    - **facts:**
      - FCT-014
    - **status:** REFUTED_BOUNDED
- **diagnostic_not_truth:** true
- **dimensions:**
  - **geo:** 0.82
  - **lang:** 0.72
  - **owner:** 0.72
  - **persp:** 0.78
  - **strat:** 0.86
  - **temp:** 0.75
- **edi:**
  - **band:** BROAD
  - **score:** 0.69
- **source_counts:**
  - **◈:** 13
  - **◉:** 3
  - **○:** 0

### RESPONSIBILITY_MAP
- **item 1:**
  - **actor:** UK FCO/CSSF
  - **evidence:**
    - FCT-001
    - FCT-002
    - FCT-003
  - **limit:** funding does not prove detailed operational tasking
  - **responsibility:** public funding/programme sponsorship
- **item 2:**
  - **actor:** Institute for Statecraft / Integrity Initiative
  - **evidence:**
    - FCT-004
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-009
    - FCT-010
  - **limit:** exposed-document provenance caveat and self-attribution limits apply
  - **responsibility:** project design and self-described cluster/dissemination/rapid-response activities
- **item 3:**
  - **actor:** Spanish executive
  - **evidence:**
    - FCT-011
    - FCT-012
  - **limit:** reason for choosing Ballesteros over Baños not causally attributed to II by inspected decision record
  - **responsibility:** final National Security Director appointment
- **item 4:**
  - **actor:** OSCR
  - **evidence:**
    - FCT-015
  - **limit:** regulatory governance findings do not trace FCO money to partisan activity
  - **responsibility:** charity governance inquiry/accountability
- **item 5:**
  - **actor:** European Commission
  - **evidence:**
    - FCT-014
  - **limit:** does not speak for every EU actor/contact
  - **responsibility:** scoped statement on East StratCom relationship

### NEXT_QUERIES
- **item 1:**
  - **query:** Spanish PM office/cabinet records, emails or testimony contemporaneous to Baños/Ballesteros decision explaining the change
  - **route:** RECHECK
  - **trigger:** primary decision-maker evidence becomes available
- **item 2:**
  - **query:** FCO grant monitoring/audit records connecting specific Integrity Initiative cluster operations to requested or approved deliverables
  - **route:** RECHECK
  - **trigger:** declassified/released grant oversight material
- **item 3:**
  - **query:** person-specific confirmation or denial for France cluster listed contacts, without bulk guilt-by-association
  - **route:** RECHECK
  - **trigger:** material actor-specific claim requires membership/tasking closure
- **item 4:**
  - **query:** direct British intelligence tasking document or authoritative inquiry finding
  - **route:** RECHECK
  - **trigger:** new declassified/judicial/parliamentary evidence

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-009,QRY-011,QRY-012 | support:- | counter:- | results:FCT-001,FCT-002 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-013 | support:- | counter:- | results:FCT-004,FCT-005 | final:SATURATED | gap:NONE
LED-003 | attempts:QRY-014,QRY-015 | support:- | counter:- | results:FCT-006,FCT-007,FCT-008 | final:SATURATED | gap:NONE
LED-004 | attempts:QRY-016,QRY-017,QRY-018,QRY-019 | support:- | counter:- | results:FCT-009,FCT-010,FCT-011,FCT-012,FCT-013 | final:SATURATED | gap:NONE
LED-005 | attempts:QRY-020 | support:- | counter:- | results:FCT-014 | final:SATURATED | gap:NONE
LED-006 | attempts:QRY-010,QRY-021,QRY-022 | support:- | counter:- | results:FCT-003,FCT-015,FCT-016,FCT-017 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-009,QRY-011,QRY-012 | support:- | counter:- | results:FCT-001,FCT-002,CAU-001 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-013 | support:- | counter:- | results:FCT-004,FCT-005,CAU-001 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-014,QRY-015 | support:- | counter:- | results:FCT-006,FCT-007,FCT-008,CAU-002 | final:GAP | gap:ATTRIBUTION
AXS-004 | attempts:QRY-016,QRY-017,QRY-018,QRY-019 | support:- | counter:- | results:FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,CAU-003 | final:GAP | gap:CAUSALITY
AXS-005 | attempts:QRY-020 | support:- | counter:- | results:FCT-014,CTRL-004 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-010,QRY-021,QRY-022,QRY-023,QRY-024 | support:- | counter:- | results:FCT-003,FCT-015,FCT-016,FCT-017,FCT-018,CTRL-001,CTRL-002,CTRL-003 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-009,QRY-011,QRY-012,SRC-001,SRC-003,SRC-004 | support:FCT-001,FCT-002 | counter:- | results:FCT-001,FCT-002 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-013,QRY-014,QRY-017,QRY-022,SRC-005,SRC-006,SRC-009,SRC-014 | support:FCT-004,FCT-005,FCT-006,FCT-007,FCT-010 | counter:FCT-016 | results:FCT-004,FCT-005,FCT-006,FCT-007,FCT-010,FCT-016 | final:PARTIAL | gap:PROVENANCE
CLM-003 | attempts:QRY-015,QRY-022,SRC-007,SRC-014 | support:- | counter:FCT-008,FCT-016 | results:FCT-008,FCT-016 | final:REFUTED | gap:ATTRIBUTION
CLM-004 | attempts:QRY-016,QRY-017,QRY-018,QRY-019,SRC-008,SRC-009,SRC-010,SRC-011 | support:FCT-009,FCT-010,FCT-013 | counter:FCT-011,FCT-012 | results:FCT-009,FCT-010,FCT-013,FCT-011,FCT-012 | final:PARTIAL | gap:CAUSALITY
CLM-005 | attempts:QRY-016,QRY-017,QRY-018,QRY-019,SRC-008,SRC-009,SRC-010,SRC-011 | support:FCT-009,FCT-010,FCT-011,FCT-012,FCT-013 | counter:- | results:FCT-009,FCT-010,FCT-011,FCT-012,FCT-013 | final:SUPPORTED | gap:CAUSALITY
CLM-006 | attempts:QRY-020,SRC-012 | support:- | counter:FCT-014 | results:FCT-014 | final:REFUTED | gap:NONE
CLM-007 | attempts:QRY-010,QRY-021,SRC-002,SRC-013 | support:- | counter:FCT-003,FCT-015 | results:FCT-003,FCT-015 | final:PARTIAL | gap:FUNDING_ATTRIBUTION
CLM-008 | attempts:QRY-009,QRY-010,QRY-011,QRY-012,QRY-023,SRC-001,SRC-002,SRC-003,SRC-004,SRC-015 | support:- | counter:FCT-001,FCT-002,FCT-003,FCT-017 | results:FCT-001,FCT-002,FCT-003,FCT-017 | final:PARTIAL | gap:ATTRIBUTION

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
AXS-003 | AXS | GAP | ATTRIBUTION | Project artifacts describe interfaces and list contacts, but active membership/consent/tasking for every listed person is not established.
AXS-004 | AXS | GAP | CAUSALITY | Campaign activity and self-attribution overlap the candidate change, but no inspected decision-maker record establishes the campaign as the but-for cause.
CLM-002 | CLM | PARTIAL | PROVENANCE | Document provenance is partially acknowledged but not universally authenticated; claims are bounded to what inspected artifacts state.
CLM-003 | CLM | REFUTED | ATTRIBUTION | A list is not proof of contact, consent, active participation or tasking.
CLM-004 | CLM | PARTIAL | CAUSALITY | No inspected decision-maker communication or causal design establishes the project campaign as the but-for cause; multiple domestic actors/media also opposed the candidate.
CLM-005 | CLM | SUPPORTED | CAUSALITY | Effect on the final appointment decision is not causally closed.
CLM-007 | CLM | PARTIAL | FUNDING_ATTRIBUTION | OSCR governance/Twitter concerns do not trace the partisan content to the FCO grant; the government statement is not conclusive exoneration of all conduct.
CLM-008 | CLM | PARTIAL | ATTRIBUTION | Public funding, military links or separate training payments do not establish intelligence-service tasking; no direct command document was inspected.
CAU-003 | CAU | GAP | CAUSALITY | Temporal sequence and self-attribution are insufficient to establish decision causation.
CAU-005 | CAU | GAP | FUNDING_ATTRIBUTION | Controversial social-media conduct/governance concerns are documented, but grant-funded causal routing to UK partisan content is not.

SEMANTIC_COUNTS_V1:LED:6|CLM:8|AXS:6|CAU:5|CTRL:5|ACT:3

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-009","QRY-011","QRY-012"],"evidence_excerpt":"£296,500 in 2017/18 and £1,961,000 in 2018/19, both through grant agreements.","kind":"FLOW","lead":"Substantial FCO public funding to Integrity Initiative is directly documented.","linked_ids":["AXS-001","CLM-001","CAU-001"],"locator":"UK Parliament answer 196177","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002"],"routes":["EXPAND","LINK"],"source_id":"SRC-001","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-013"],"evidence_excerpt":"network of experts, opinion formers and policy makers; cement UK influence post-Brexit; cluster dissemination to 100+ key individuals/institutions.","kind":"MECHANISM","lead":"Project documents describe a cross-border cluster network explicitly intended to shape awareness, policy/society and UK influence.","linked_ids":["AXS-002","CLM-002","CAU-001"],"locator":"Phase II application pp.2,9","materiality":"DECISIVE","result_ids":["FCT-004","FCT-005"],"routes":["AUDIT","EXPAND","LINK"],"source_id":"SRC-005","status":"SATURATED"}
LED-003 | {"attempt_ids":["QRY-014","QRY-015"],"evidence_excerpt":"Spain: anonymous cluster material to independent journalists and PM office; France: CAPS/MFA contacts and informal material feed.","kind":"MECHANISM","lead":"Spain and France cluster documents describe concrete media and government-interface routes.","linked_ids":["AXS-003","CLM-003","CAU-002"],"locator":"Cluster Roundup p.1","materiality":"DECISIVE","result_ids":["FCT-006","FCT-007","FCT-008"],"routes":["EXPAND","LINK"],"source_id":"SRC-006","status":"SATURATED"}
LED-004 | {"attempt_ids":["QRY-016","QRY-017","QRY-018","QRY-019"],"evidence_excerpt":"initial Twitter campaign; media impact; WhatsApp example; Top 3 Deliverables says recent Spain example of influencing the appointment.","kind":"EVENT","lead":"The exposed Moncloa material records coordinated amplification and the project self-claims influence over the Baños appointment.","linked_ids":["AXS-004","CLM-004","CAU-003"],"locator":"Moncloa pp.1-2 + Top 3 Deliverables p.1","materiality":"DECISIVE","result_ids":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-013"],"routes":["AUDIT","EXPAND","LINK"],"source_id":"SRC-008","status":"SATURATED"}
LED-005 | {"attempt_ids":["QRY-020"],"evidence_excerpt":"East Stratcom Task Force does not cooperate with the Integrity Initiative.","kind":"RELATION","lead":"EU-level operational cooperation with East StratCom is directly denied by the Commission for the period.","linked_ids":["AXS-005","CLM-006","CTRL-004"],"locator":"Commission answer E-000092/2019","materiality":"IMPORTANT","result_ids":["FCT-014"],"routes":["AUDIT","LINK"],"source_id":"SRC-012","status":"SATURATED"}
LED-006 | {"attempt_ids":["QRY-010","QRY-021","QRY-022"],"evidence_excerpt":"inquiry opened after data-breach information and concerns about Twitter; trustee governance/social-media learning points.","kind":"CONTROL","lead":"A domestic accountability controversy existed, but regulator findings concern charity governance/social media rather than proof that FCO grant funded partisan tasking.","linked_ids":["AXS-006","CLM-007","CTRL-003"],"locator":"OSCR Reporter p.4","materiality":"IMPORTANT","result_ids":["FCT-003","FCT-015","FCT-016","FCT-017"],"routes":["AUDIT","LINK"],"source_id":"SRC-013","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"The Integrity Initiative was materially funded by the UK FCO/CSSF counter-disinformation programme.","claimant":"official records + INV-031 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002"]}
CLM-002 | {"claim":"Integrity Initiative documents describe an intentional transnational network designed to disseminate material through experts, journalists and policy actors and to affect policy/society.","claimant":"project exposed documents","counter":["FCT-016"],"gap":"Document provenance is partially acknowledged but not universally authenticated; claims are bounded to what inspected artifacts state.","gap_type":"PROVENANCE","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-004","FCT-005","FCT-006","FCT-007","FCT-010"]}
CLM-003 | {"claim":"Every person listed in the France Cluster artifact was an active, consenting Integrity Initiative member or UK-tasked intermediary.","claimant":"strong network inference","counter":["FCT-008","FCT-016"],"gap":"A list is not proof of contact, consent, active participation or tasking.","gap_type":"ATTRIBUTION","materiality":"IMPORTANT","status":"REFUTED","support":"NONE_FOUND"}
CLM-004 | {"claim":"Integrity Initiative activity caused Pedro Baños to lose the National Security Director appointment.","claimant":"project self-attribution / external allegations","counter":["FCT-011","FCT-012"],"gap":"No inspected decision-maker communication or causal design establishes the project campaign as the but-for cause; multiple domestic actors/media also opposed the candidate.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-009","FCT-010","FCT-013"]}
CLM-005 | {"claim":"The project exercised a bounded transnational influence attempt in Spain through rapid media/social mobilisation around an identifiable appointment.","claimant":"INV-031 synthesis","counter":"NONE_FOUND","gap":"Effect on the final appointment decision is not causally closed.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-013"]}
CLM-006 | {"claim":"EU East StratCom Task Force cooperated operationally with Integrity Initiative in the scoped period.","claimant":"network-expansion inference","counter":["FCT-014"],"gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"REFUTED","support":"NONE_FOUND"}
CLM-007 | {"claim":"FCO grant money was proven to have funded UK party-political attacks.","claimant":"domestic controversy allegation","counter":["FCT-003","FCT-015"],"gap":"OSCR governance/Twitter concerns do not trace the partisan content to the FCO grant; the government statement is not conclusive exoneration of all conduct.","gap_type":"FUNDING_ATTRIBUTION","materiality":"IMPORTANT","status":"PARTIAL","support":"NONE_FOUND"}
CLM-008 | {"claim":"Integrity Initiative was proven to be under direct British intelligence-service command.","claimant":"strong covert-operation allegation","counter":["FCT-001","FCT-002","FCT-003","FCT-017"],"gap":"Public funding, military links or separate training payments do not establish intelligence-service tasking; no direct command document was inspected.","gap_type":"ATTRIBUTION","materiality":"DECISIVE","status":"PARTIAL","support":"NONE_FOUND"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-009","QRY-011","QRY-012"],"axis":"RESOURCES_FLOWS","links":["LED-001"],"question":"What public funding and programme authority are directly documented?","result_ids":["FCT-001","FCT-002","CAU-001"],"sought_objects":["grant amounts","funding programme","CSSF source"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-013"],"axis":"MECHANISMS","links":["LED-002"],"question":"What operating architecture did the project itself describe?","result_ids":["FCT-004","FCT-005","CAU-001"],"sought_objects":["cluster design","target audiences","policy/media interfaces"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-014","QRY-015"],"axis":"ACTORS_RELATIONS","gap":"Project artifacts describe interfaces and list contacts, but active membership/consent/tasking for every listed person is not established.","gap_type":"ATTRIBUTION","links":["LED-003"],"question":"Which Spain/France interfaces are documented and where does membership/tasking proof stop?","result_ids":["FCT-006","FCT-007","FCT-008","CAU-002"],"sought_objects":["cluster activity","government contacts","member consent/tasking"],"status":"GAP"}
AXS-004 | {"attempt_ids":["QRY-016","QRY-017","QRY-018","QRY-019"],"axis":"IMPACT_RESPONSIBILITY","gap":"Campaign activity and self-attribution overlap the candidate change, but no inspected decision-maker record establishes the campaign as the but-for cause.","gap_type":"CAUSALITY","links":["LED-004"],"question":"Did Moncloa activity causally change the Spanish appointment?","result_ids":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","CAU-003"],"sought_objects":["campaign trace","appointment chronology","decision-maker evidence","counterfactual"],"status":"GAP"}
AXS-005 | {"attempt_ids":["QRY-020"],"axis":"RULES_CONTROLS","links":["LED-005"],"question":"Was Integrity Initiative operationally integrated with EU East StratCom?","result_ids":["FCT-014","CTRL-004"],"sought_objects":["Commission cooperation record"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-010","QRY-021","QRY-022","QRY-023","QRY-024"],"axis":"COUNTER_HYPOTHESES","links":["LED-006"],"question":"Can the strongest covert-state/partisan reading be distinguished from funded counter-disinformation plus governance failures?","result_ids":["FCT-003","FCT-015","FCT-016","FCT-017","FCT-018","CTRL-001","CTRL-002","CTRL-003"],"sought_objects":["grant restrictions","regulator findings","provenance caveat","separate MOD payment"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"Funding and project design establish resource-to-capacity enablement; they do not establish detailed state command of every cluster action.","counter":"NONE_FOUND","limit":"Grant conditions/tasking granularity beyond public records is incomplete.","mechanism":"UK public grant/programme -> Institute/Integrity Initiative -> cluster network and dissemination capacity","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-004","FCT-005"],"type":"INSTITUTIONAL_INFLUENCE"}
CAU-002 | {"causal_right":"Project documents directly describe this operational route; person-level participation remains bounded by provenance/consent gaps.","counter":["FCT-008","FCT-016"],"limit":"No generalized denominator for how many listed contacts were active or effective.","mechanism":"cluster hub/network -> journalists/academics/government contacts -> articles, briefings, private dissemination","status":"SUPPORTED","support":["FCT-005","FCT-006","FCT-007"],"type":"NETWORK_INTERMEDIATION"}
CAU-003 | {"counter":["FCT-011","FCT-012"],"gap":"Temporal sequence and self-attribution are insufficient to establish decision causation.","gap_type":"CAUSALITY","limit":"No decision-maker record or counterfactual isolates the project contribution from domestic party, media and executive considerations.","mechanism":"Moncloa mobilisation -> media/political pressure -> appointment decision changes from Baños to Ballesteros","status":"GAP","support":["FCT-009","FCT-010","FCT-013"],"type":"POLITICAL_APPOINTMENT_EFFECT"}
CAU-004 | {"causal_right":"Commission directly denied cooperation in the scoped period.","counter":["FCT-014"],"limit":"Bounded to East StratCom and the 2019 Commission answer; does not exclude unrelated contacts with other EU actors.","mechanism":"Integrity Initiative -> EU East StratCom operational cooperation","status":"REFUTED","support":"NONE_FOUND","type":"EU_COORDINATION"}
CAU-005 | {"counter":["FCT-003","FCT-015"],"gap":"Controversial social-media conduct/governance concerns are documented, but grant-funded causal routing to UK partisan content is not.","gap_type":"FUNDING_ATTRIBUTION","limit":"Official denial is interested evidence and not a universal exoneration; OSCR finding does not trace funding source.","mechanism":"FCO grant -> Integrity Initiative UK social-media activity -> partisan attack","status":"GAP","support":"NONE_FOUND","type":"DOMESTIC_PARTISAN_USE"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"grant != detailed state command","status":"DONE","support":["FCT-001","FCT-002","FCT-004"]}
CTRL-002 | {"control":"listed contact != active member/tasked intermediary","status":"DONE","support":["FCT-008","FCT-016"]}
CTRL-003 | {"control":"project self-attribution + chronology != causal proof","status":"DONE","support":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-013"]}
CTRL-004 | {"control":"shared counter-disinformation mission != EU operational cooperation","status":"DONE","support":["FCT-014"]}
CTRL-005 | {"control":"payment to Institute != payment to Integrity Initiative","status":"DONE","support":["FCT-017"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Represent Integrity Initiative as a publicly funded transnational counter-disinformation influence network with documented cluster/dissemination architecture, not as a proven intelligence-command system.","actor":"future synthesis/article protocol","intent":"preserve mechanism while preventing attribution inflation","status":"DONE","support":["FCT-001","FCT-002","FCT-004","FCT-005","FCT-006","FCT-007"]}
ACT-002 | {"action":"Reopen Moncloa causality only on direct Spanish decision-maker evidence, internal government chronology or a defensible causal design linking campaign pressure to the appointment switch.","actor":"future investigation","intent":"close appointment-effect gap","status":"DEFERRED","support":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-013"]}
ACT-003 | {"action":"Treat exposed cluster lists as leads/documents, never as proof that every named person consented or was tasked.","actor":"future synthesis/article protocol","intent":"avoid network guilt by association","status":"DONE","support":["FCT-008","FCT-016"]}

SEARCH_ACTIVITY_V1:WEB:8|FETCH:16|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"EMPTY","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL | mnemo | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | https://questions-statements.parliament.uk/written-questions/detail/2018-11-27/196177 | Integrity Initiative FCO funding 2017 2018 Parliament
QRY-002 | WEB | FOUND | - | https://hansard.parliament.uk/commons/2018-12-12/debates/298F9A3C-307A-40ED-9CB1-3B2A98F14165/InstituteForStatecraftIntegrityInitiative | Integrity Initiative grant domestic political influence clause Hansard
QRY-003 | WEB | FOUND | - | https://questions-statements.parliament.uk/written-questions/detail/2018-12-04/198811 | Integrity Initiative Counter Disinformation Media Development Programme CSSF
QRY-004 | WEB | FOUND | - | https://fdik.org/Integrity_Initiative/ | Integrity Initiative exposed FCO application cluster roundup Moncloa
QRY-005 | WEB | FOUND | - | https://elpais.com/politica/2018/06/14/actualidad/1528987717_390585.html | Pedro Banos Ballesteros director Seguridad Nacional June 2018
QRY-006 | WEB | FOUND | - | https://www.europarl.europa.eu/RegData/questions/reponses_qe/2019/000092/P8_RE%282019%29000092_EN.pdf | Integrity Initiative East Stratcom cooperation European Commission 2019
QRY-007 | WEB | FOUND | - | https://www.oscr.org.uk/media/3803/2019-12-02-oscr-reporter-december-2019.pdf | OSCR Institute for Statecraft inquiry Twitter 2019
QRY-008 | WEB | FOUND | - | https://www.theferret.scot/scottish-charity-propaganda-regulator/ | Integrity Initiative exposed document authenticity acknowledgement
QRY-009 | FETCH | FOUND | SRC-001 | https://questions-statements.parliament.uk/written-questions/detail/2018-11-27/196177 | UK Parliament answer on FCO Integrity Initiative grants inspected
QRY-010 | FETCH | FOUND | SRC-002 | https://hansard.parliament.uk/commons/2018-12-12/debates/298F9A3C-307A-40ED-9CB1-3B2A98F14165/InstituteForStatecraftIntegrityInitiative | Hansard Integrity Initiative urgent question inspected
QRY-011 | FETCH | FOUND | SRC-003 | https://questions-statements.parliament.uk/written-questions/detail/2018-12-04/198811 | UK Parliament answer on programme inspected
QRY-012 | FETCH | FOUND | SRC-004 | https://questions-statements.parliament.uk/written-questions/detail/2018-12-10/200677/ | UK Parliament answer on CSSF inspected
QRY-013 | FETCH | FOUND | SRC-005 | https://fdik.org/Integrity_Initiative/392195390-FCO-Application-Form-2018-v2.pdf | exposed FCO application PDF inspected and visually checked
QRY-014 | FETCH | FOUND | SRC-006 | https://fdik.org/Integrity_Initiative/392195321-Cluster-Roundup-Jul18.pdf | exposed cluster roundup PDF inspected and visually checked
QRY-015 | FETCH | FOUND | SRC-007 | https://fdik.org/Integrity_Initiative/392195457-France-Cluster.pdf | exposed France Cluster PDF inspected and visually checked
QRY-016 | FETCH | FOUND | SRC-008 | https://fdik.org/Integrity_Initiative/392195691-Moncloa-Campaign-6-AttTwitter-08-06-18.pdf | exposed Moncloa campaign PDF inspected and visually checked
QRY-017 | FETCH | FOUND | SRC-009 | https://fdik.org/Integrity_Initiative/392195825-Top-3-Deliverables-for-FCO.pdf | exposed Top 3 Deliverables PDF inspected and visually checked
QRY-018 | FETCH | FOUND | SRC-010 | https://elpais.com/politica/2018/06/07/actualidad/1528372493_075633.html?id_externo_rsoc=whatsapp | El Pais contemporaneous Baños candidate article inspected
QRY-019 | FETCH | FOUND | SRC-011 | https://elpais.com/politica/2018/06/14/actualidad/1528987717_390585.html | El Pais Ballesteros appointment article inspected
QRY-020 | FETCH | FOUND | SRC-012 | https://www.europarl.europa.eu/RegData/questions/reponses_qe/2019/000092/P8_RE%282019%29000092_EN.pdf | European Commission answer on East StratCom inspected
QRY-021 | FETCH | FOUND | SRC-013 | https://www.oscr.org.uk/media/3803/2019-12-02-oscr-reporter-december-2019.pdf | OSCR reporter inquiry entry inspected and PDF opened
QRY-022 | FETCH | FOUND | SRC-014 | https://www.theferret.scot/scottish-charity-propaganda-regulator/ | The Ferret report with Institute provenance response inspected
QRY-023 | FETCH | FOUND | SRC-015 | https://questions-statements.parliament.uk/written-questions/detail/2018-12-18/203331/ | UK Parliament MOD payment clarification inspected
QRY-024 | FETCH | FOUND | SRC-016 | https://www.oscr.org.uk/about-charities/search-the-register/charity-details?number=SC040870 | OSCR current charity register inspected

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:other:uk-fco | UKPQ-196177 | UK Parliament — FCO Integrity Initiative funding answer | 2018-12-03 | 2026-09-11T21:59:00Z | lines 14-24; £296,500 FY2017/18 and £1,961,000 FY2018/19 via grants | https://questions-statements.parliament.uk/written-questions/detail/2018-11-27/196177
SRC-002 | ◈ | fam:other:uk-parliament | HANSARD-II-20181212 | Hansard — Institute for Statecraft: Integrity Initiative | 2018-12-12 | 2026-09-11T21:59:00Z | minister: overseas counter-disinformation; grant restriction against influencing UK Parliament/Government/parties; government said no evidence of funded breach | https://hansard.parliament.uk/commons/2018-12-12/debates/298F9A3C-307A-40ED-9CB1-3B2A98F14165/InstituteForStatecraftIntegrityInitiative
SRC-003 | ◈ | fam:other:uk-fco | UKPQ-198811 | UK Parliament — Counter Disinformation and Media Development Programme | 2018-12-10 | 2026-09-11T21:59:00Z | lines 14-19; Institute funding came from NSC-authorised Counter Disinformation and Media Development Programme | https://questions-statements.parliament.uk/written-questions/detail/2018-12-04/198811
SRC-004 | ◈ | fam:other:uk-fco | UKPQ-200677 | UK Parliament — CSSF funding answer | 2018-12-13 | 2026-09-11T21:59:00Z | lines 19-37; support CSSF-funded, no ODA money | https://questions-statements.parliament.uk/written-questions/detail/2018-12-10/200677/
SRC-005 | ◈ | fam:other:ii-exposed | II-FCO-APP-2018-V2 | Integrity Initiative Phase II — exposed FCO application form | 2018 | 2026-09-11T21:59:00Z | pp.2,9; network of experts/opinion formers/policy makers; post-Brexit UK influence; cluster structure and target dissemination. Provenance caveat applies. | https://fdik.org/Integrity_Initiative/392195390-FCO-Application-Form-2018-v2.pdf
SRC-006 | ◈ | fam:other:ii-exposed | II-CLUSTER-ROUNDUP-JUL18 | Integrity Initiative — Progress report on establishing national clusters | 2018-07 | 2026-09-11T21:59:00Z | p.1 lines 6-34; Spain influence/dissemination and France CAPS/MFA contacts; direct artifact content, provenance caveat applies | https://fdik.org/Integrity_Initiative/392195321-Cluster-Roundup-Jul18.pdf
SRC-007 | ◈ | fam:other:ii-exposed | II-FRANCE-CLUSTER | Integrity Initiative — French Cluster list | 2018 | 2026-09-11T21:59:00Z | p.1; names/emails including government domains; list does not prove active membership/consent | https://fdik.org/Integrity_Initiative/392195457-France-Cluster.pdf
SRC-008 | ◈ | fam:other:ii-exposed | II-MONCLOA-20180607 | Integrity Initiative — Moncloa campaign | 2018-06-07 | 2026-09-11T21:59:00Z | pp.1-2; initial Twitter campaign, media impact links and WhatsApp example; direct artifact content, provenance caveat applies | https://fdik.org/Integrity_Initiative/392195691-Moncloa-Campaign-6-AttTwitter-08-06-18.pdf
SRC-009 | ◈ | fam:other:ii-exposed | II-TOP3-FCO | Integrity Initiative — Top 3 deliverables/achievements | 2018-06 | 2026-09-11T21:59:00Z | p.1 lines 1-30; cluster concept, impact on policy/society, distribution to 350 key people, golden minute, self-attribution re Spain appointment | https://fdik.org/Integrity_Initiative/392195825-Top-3-Deliverables-for-FCO.pdf
SRC-010 | ◉ | fam:other:elpais | ELPAIS-BANOS-20180608 | EL PAÍS — Pedro Baños prospective national-security director | 2018-06-08 | 2026-09-11T21:59:00Z | contemporaneous report: Baños previsibly/prospectively to be Director de Seguridad Nacional | https://elpais.com/politica/2018/06/07/actualidad/1528372493_075633.html?id_externo_rsoc=whatsapp
SRC-011 | ◉ | fam:other:elpais | ELPAIS-BALLESTEROS-20180614 | EL PAÍS — Ballesteros to be director general of National Security | 2018-06-14 | 2026-09-11T21:59:00Z | lines 19-67; Ballesteros selected; Baños described as other candidate | https://elpais.com/politica/2018/06/14/actualidad/1528987717_390585.html
SRC-012 | ◈ | fam:other:eu-commission | EC-E000092-2019 | European Commission answer E-000092/2019 | 2019-04-09 | 2026-09-11T21:59:00Z | answer: Member State initiative not raised at EU level; East StratCom Task Force does not cooperate with Integrity Initiative | https://www.europarl.europa.eu/RegData/questions/reponses_qe/2019/000092/P8_RE%282019%29000092_EN.pdf
SRC-013 | ◈ | fam:other:oscr | OSCR-REPORTER-201912 | OSCR Reporter — Inquiry Report: The Institute for Statecraft | 2019-12 | 2026-09-11T21:59:00Z | p.4 lines 179-203; inquiry opened 13 Dec 2018 re data breaches/Twitter; trustee governance/social-media learning points | https://www.oscr.org.uk/media/3803/2019-12-02-oscr-reporter-december-2019.pdf
SRC-014 | ◉ | fam:other:ferret | FERRET-II-201812 | The Ferret — Scottish charity at centre of propaganda row probed | 2018-12 | 2026-09-11T21:59:00Z | reports Institute site acknowledged much exposed material was on II/Institute systems while not verifying every document; many listed names were only potential invitees | https://www.theferret.scot/scottish-charity-propaganda-regulator/
SRC-015 | ◈ | fam:other:uk-mod | UKPQ-203331 | UK Parliament — MOD payment to Institute for Statecraft | 2019-01-07 | 2026-09-11T21:59:00Z | payment £6,788.52 made 29 Nov 2017 for specialist Army training; identified as Institute payment rather than Integrity Initiative programme | https://questions-statements.parliament.uk/written-questions/detail/2018-12-18/203331/
SRC-016 | ◈ | fam:other:oscr | OSCR-SC040870 | OSCR charity register — Institute for Statecraft | 2026-09-11 | 2026-09-11T21:59:00Z | register shows charity ceased 16 Oct 2023 and wound up/dissolved; not a causal finding for 2018 | https://www.oscr.org.uk/about-charities/search-the-register/charity-details?number=SC040870

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://questions-statements.parliament.uk/written-questions/detail/2018-11-27/196177 | other:uk-fco | 2017/18-2018/19 | FCO grant amounts | UK Parliament records FCO grants of £296,500 in FY2017/18 and £1,961,000 in FY2018/19 to the Institute for Statecraft Integrity Initiative. | -
FCT-002 | FACT | ✧ | https://questions-statements.parliament.uk/written-questions/detail/2018-12-04/198811 | other:uk-fco | 2016-2018 | Counter-disinformation programme funding route | FCO answers state that the Institute funding came through the NSC-authorised Counter Disinformation and Media Development Programme and that the support was CSSF-funded, with no ODA money used. | -
FCT-003 | FACT | ✧ | https://hansard.parliament.uk/commons/2018-12-12/debates/298F9A3C-307A-40ED-9CB1-3B2A98F14165/InstituteForStatecraftIntegrityInitiative | other:uk-parliament | 2018-12-12 | Domestic influence restriction in grant | The responsible UK minister told Parliament that the grant contract prohibited use to influence or attempt to influence the UK Parliament, Government or political parties, and said the Government had not seen evidence that the Integrity Initiative breached that funded obligation. | -
FCT-004 | FACT | ✧ | https://fdik.org/Integrity_Initiative/392195390-FCO-Application-Form-2018-v2.pdf | other:ii-exposed | 2018 | Project stated network-and-influence purpose | The exposed Phase II application describes a network of experts, opinion formers and policy makers to educate national audiences and build counter-disinformation capacity, and states that expansion would cement UK influence in North America and Europe post-Brexit. This is evidence of the document stated purpose, not independent proof of every activity claimed in it. | -
FCT-005 | FACT | ✧ | https://fdik.org/Integrity_Initiative/392195390-FCO-Application-Form-2018-v2.pdf | other:ii-exposed | 2018 | Cluster dissemination design | The exposed application describes each cluster as a 1-3 person hub plus 10-20 active members disseminating material to 100+ key individuals and institutions, with Spain and France among Phase I clusters. | -
FCT-006 | FACT | ✧ | https://fdik.org/Integrity_Initiative/392195321-Cluster-Roundup-Jul18.pdf | other:ii-exposed | 2018-07 | Spain cluster self-described influence methods | The exposed cluster roundup says the Spain cluster drew from academia, media, civil servants, military and several parties; it describes articles by independent journalists based on anonymously supplied cluster material and private circulation to key influencers including the PM office. | -
FCT-007 | FACT | ✧ | https://fdik.org/Integrity_Initiative/392195321-Cluster-Roundup-Jul18.pdf | other:ii-exposed | 2018-07 | France cluster self-described government interface | The exposed cluster roundup says Integrity Initiative staff had contacts with French MFA CAPS, briefed MOD/MFA/services officers, continued to feed material informally into CAPS, and separately established a nongovernmental cluster using selected journalists and academics. | -
FCT-008 | FACT | ✧ | https://fdik.org/Integrity_Initiative/392195457-France-Cluster.pdf | other:ii-exposed | 2018 | France contact list provenance limit | An exposed one-page French Cluster artifact lists named contacts, many with French government email domains. The artifact establishes that such a list existed in the exposed corpus; it does not by itself establish that every listed person consented, was contacted, or actively participated. | -
FCT-009 | FACT | ✧ | https://fdik.org/Integrity_Initiative/392195691-Moncloa-Campaign-6-AttTwitter-08-06-18.pdf | other:ii-exposed | 2018-06-07 | Moncloa campaign artifact activity | The exposed Moncloa artifact records an initial Twitter campaign, subsequent amplification, links to first media impact and a WhatsApp-group example around the proposed Pedro Baños appointment. | -
FCT-010 | FACT | ✧ | https://fdik.org/Integrity_Initiative/392195825-Top-3-Deliverables-for-FCO.pdf | other:ii-exposed | 2018-06 | Project self-attribution of Spain appointment influence | An exposed Top 3 Deliverables artifact describes connecting media, academia and policy makers to impact policy/society, a proactive distribution system to 350 key people, network activism in a golden minute, and self-attributes influence over the Spanish appointment within hours of announcement. | -
FCT-011 | FACT | ✧ | https://elpais.com/politica/2018/06/07/actualidad/1528372493_075633.html?id_externo_rsoc=whatsapp | other:elpais | 2018-06-08 | Baños was a prospective candidate | Contemporaneous EL PAÍS reporting described Pedro Baños as the prospective/expected Director de Seguridad Nacional in the new Sánchez government. | -
FCT-012 | FACT | ✧ | https://elpais.com/politica/2018/06/14/actualidad/1528987717_390585.html | other:elpais | 2018-06-14 | Ballesteros selected and Baños identified as other candidate | On 14 June EL PAÍS reported that Miguel Ángel Ballesteros would be appointed Director General de Seguridad Nacional and identified Pedro Baños as the other candidate. | -
FCT-013 | FACT | ✧ | https://fdik.org/Integrity_Initiative/392195691-Moncloa-Campaign-6-AttTwitter-08-06-18.pdf | other:elpais,other:ii-exposed | 2018-06-07/14 | Moncloa temporal overlap without causal closure | The exposed campaign artifact is dated to the same period in which Baños was publicly reported as the prospective candidate and Ballesteros was selected days later. This closes temporal overlap and campaign self-attribution, not the but-for cause of the appointment decision. | -
FCT-014 | FACT | ✧ | https://www.europarl.europa.eu/RegData/questions/reponses_qe/2019/000092/P8_RE%282019%29000092_EN.pdf | other:eu-commission | 2019-04-09 | EU East StratCom non-cooperation | The European Commission stated that Integrity Initiative was a Member State initiative not raised at EU level and that the East StratCom Task Force did not cooperate with it. | -
FCT-015 | FACT | ✧ | https://www.oscr.org.uk/media/3803/2019-12-02-oscr-reporter-december-2019.pdf | other:oscr | 2018-2019 | OSCR governance inquiry | OSCR says it opened an inquiry on 13 December 2018 after information about data breaches and concerns over the charity Twitter feed, and later highlighted trustee decision-making, recordkeeping and social-media care as learning points. | -
FCT-016 | FACT | ✧ | https://www.theferret.scot/scottish-charity-propaganda-regulator/ | other:ferret | 2018 | Exposed-document authenticity is partial not universal | The Ferret reported the Institute position that much exposed material was indeed on Integrity Initiative or Institute systems but it could not verify that all documents were genuine; it also said many published names were merely considered as possible future invitees and were never contacted. | -
FCT-017 | FACT | ✧ | https://questions-statements.parliament.uk/written-questions/detail/2018-12-18/203331/ | other:uk-mod | 2017-11-29 | MOD payment control | The Ministry of Defence said a £6,788.52 payment on 29 November 2017 was to the Institute for Statecraft for specialist Army training and was not identified in its search as an Integrity Initiative programme payment. This is a control against conflating every Institute payment with the project. | -
FCT-018 | FACT | ✧ | https://www.oscr.org.uk/about-charities/search-the-register/charity-details?number=SC040870 | other:oscr | 2023 | Institute charity ceased | OSCR current register records the Institute for Statecraft charity as ceased on 16 October 2023 and wound up/dissolved. This later status does not establish any causal fact about 2018 influence operations. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-003,SRC-004
FCT-003 | SRC-002
FCT-004 | SRC-005
FCT-005 | SRC-005
FCT-006 | SRC-006
FCT-007 | SRC-006
FCT-008 | SRC-007
FCT-009 | SRC-008
FCT-010 | SRC-009
FCT-011 | SRC-010
FCT-012 | SRC-011
FCT-013 | SRC-008,SRC-010,SRC-011
FCT-014 | SRC-012
FCT-015 | SRC-013
FCT-016 | SRC-014
FCT-017 | SRC-015
FCT-018 | SRC-016

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

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:CAUSAL
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:FINALIZE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-11T22:13:25.774100+00:00","fact_mem":{},"mnemo_row":"BLOCKED:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":18,"eligible":18,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:BLOCKED:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:18;attempted:0;success:0;failure:0;blocked:18} | WRITEBACK_EXECUTION_V1:[18 rows, see section]

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
