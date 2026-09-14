ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260913-1200-elnet-voyages-effet-causal | PARENT_RUN_ID:NONE | AS_OF:2026-09-13
INPUT_KIND:RUN_CARD | MISSION_MODE:DEEPEN | INPUT_REF:PATH:/mnt/data/inv161_work/runtime/investigations/2026-09/2026-09-13_elnet-voyages-effet-causal/2026-09-13_12-00_elnet-voyages-effet-causal_INPUT.md | SUBJECT_SLUG:elnet-voyages-effet-causal | SUBJECT_FP:sha256:eb01ba699fbdd2257fcb334c3c10722709913bfb83aade361303c66daa265319 | INPUT_SHA256:sha256:2ebfc74aaa565b18d861045c1322191a869bebfed95f3306be8a39cc6586a0bc
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France 2017-2026; ELNET-funded parliamentary travel, participants, declared invitations, public positions before/after, matched controls; separate exposure from persuasion and causal effect.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/NETWORK.md,clusters/TEMPORAL.md,clusters/ICEBERG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-161 — ELNET : voyages parlementaires et effet causal

## Objet

Tester si les voyages parlementaires financés ou organisés par ELNET en Israël produisent un effet politique mesurable en France, en séparant strictement financement, accès, exposition, réception, comportement parlementaire et résultat politique.

## Résultat central

**FACT.** Les voyages ELNET constituent un canal d'exposition parlementaire quantitativement important. Au 1er décembre 2025, sous la XVIIe législature, le rapport de la commission des affaires étrangères recense 82 déclarations d'invitations à voyager émanant de 47 députés, dont 38 financées par ELNET. Le même passage cite, à titre de comparaison, 6 déclarations financées par Taïwan et 4 par le Qatar (FCT-001). Le cadre déontologique impose la déclaration préalable des voyages financés par un tiers (FCT-002).

**FACT.** Le phénomène n'est pas nouveau. Des déclarations officielles identifient de nombreux participants à une mission ELNET de juillet 2021 et décrivent une délégation de 38 élus reçue par de hautes autorités israéliennes, avec comme objectif déclaré le renforcement de la relation stratégique France-Israël (FCT-003 à FCT-005).

**FACT.** En mars 2023, ELNET rapporte avoir conduit quinze députés Les Républicains en Israël. Le programme combinait diplomatie publique, sécurité/défense et transition écologique (FCT-006). Le compte rendu de l'organisateur documente trois objets particulièrement discriminants : proposition d'un groupe parlementaire français sur les Accords d'Abraham (FCT-007), engagement rapporté de vigilance sur les fonds européens destinés à l'Autorité palestinienne (FCT-008), et inspiration revendiquée en matière de sécurité (FCT-009).

**FACT.** Des productions parlementaires postérieures sont congruentes avec certains de ces thèmes. Annie Genevard défend en mai 2023 une lecture favorable d'Israël et souligne l'importance des Accords d'Abraham (FCT-010). Pierre-Henri Dumont et Annie Genevard figurent parmi les cosignataires d'une résolution du 13 octobre 2023 sur l'éducation palestinienne (FCT-012) ; Dumont intervient ensuite sur les aides aux Palestiniens en janvier 2024 (FCT-013).

**CONTROL.** Cette congruence ne ferme pas l'effet causal. Pierre-Henri Dumont avait déjà pris position sur le cadrage des débats liés à Israël en février 2019, plusieurs années avant la mission de mars 2023 (FCT-011). Annie Genevard indique elle-même en mai 2023 avoir déjà rencontré à deux reprises des acteurs israéliens et palestiniens (FCT-010). Les participants ne sont donc pas assimilables à un groupe traité aléatoirement.

**CONTROL.** Le 7 octobre 2023 constitue en outre un choc externe majeur. Les actes parlementaires d'octobre 2023 et 2024 ne permettent pas d'isoler un effet marginal du voyage de mars 2023 de l'effet du conflit, des positions partisanes ou des préférences antérieures.

**FACT.** La HATVP qualifie les activités d'ELNET France de représentation d'intérêts exercée en propre et mentionne explicitement ses délégations parlementaires ainsi que diverses méthodes d'influence politique (FCT-014, FCT-015). ELNET affirme de son côté que la participation à ses délégations est volontaire et qu'aucune contrepartie politique n'est attendue (FCT-016). Cette affirmation intéressée est un contre-claim, non une preuve d'absence d'influence.

## Plafond causal

Le run ferme solidement :

`ressources ELNET -> voyage organisé/financé -> rencontres et briefings ciblés -> exposition parlementaire` = **SUPPORTED**.

Il ferme partiellement :

`exposition -> prompts/engagements politiques identifiables -> productions parlementaires congruentes` = **PARTIAL**.

Il ne ferme pas :

`voyage ELNET -> changement d'attitude -> comportement parlementaire causé -> résultat politique contre-factuel` = **CAUSAL_DESIGN GAP**.

Le mécanisme le plus plausible à tester n'est donc pas un « achat de votes », mais un effet de sélection et de renforcement : ELNET offre un accès structuré à des élus souvent déjà intéressés ou alignés, fournit des cadres, interlocuteurs et thèmes, puis certains thèmes réapparaissent dans l'activité parlementaire. Le corpus inspecté ne permet pas encore de mesurer la part propre du voyage dans cette réapparition.

## Ce que le corpus réfute ou borne

- `voyage financé = capture` : non établi ;
- `exposition = persuasion` : non établi ;
- `position congruente après voyage = effet du voyage` : non établi ;
- `ELNET France = mandataire de l'État israélien` : non établi dans ce run ;
- `absence de causalité démontrée = absence d'influence` : faux raccourci ; le canal d'accès et d'exposition est matériellement établi.

## Upgrade probatoire nécessaire

Le prochain niveau exige un dataset longitudinal : univers complet des participants 2017-2026, date et financeur de chaque voyage, positions et productions avant/après, groupe/commission, appartenance au groupe d'amitié, et contrôles non exposés comparables. Les voyages préérieurs au 7 octobre 2023 doivent être privilégiés pour limiter le confondant de guerre. Les trois traces spécifiques de mars 2023 — caucus Accords d'Abraham, financement de l'Autorité palestinienne, sécurité — doivent être recherchées comme outputs versionnés et datés, non comme simples similitudes discursives.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:4|EDI_DECISIVE:3|SRC_COMPLETE:13/13

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **key_periods:**
  - July 2021 large ELNET mission
  - March 2023 LR delegation
  - 7 October 2023 common shock
  - 2024-2025 intensified trips
- **warning:** Post-7-Oct-2023 comparisons are strongly confounded.
- **window:** 2017-2026

### MANIPULATION_REPORT
- **assumptions:**
  - public declarations capture declared third-party travel but may not capture all informal exposure
  - ELNET pages are authoritative for ELNET self-description, not independent effect measurement
  - official parliamentary records are authoritative for dates and acts, not causal attribution
- **clusters:**
  - POWER
  - NETWORK
  - TEMPORAL
  - ICEBERG
- **complexity:**
  - **band:** HIGH
  - **score:** 9
- **implicit:**
  - **I01:** repeated exposure may reinforce rather than convert
  - **I02:** voluntary travel creates selection into treatment
  - **I03:** issue salience can create common-cause alignment
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - **P01:** funded travel -> curated exposure
  - **P02:** curated exposure -> stated participant commitment
  - **P03:** later congruent act -> attribution ambiguity
  - **P04:** pre-alignment + common shock -> reverse/omitted-variable risk
- **priorities:**
  - measure scale
  - identify specific policy prompts
  - test pre-treatment alignment
  - bound causal effect
- **query_guidance:** prefer official travel declarations and parliamentary outputs; treat ELNET descriptions as self-report; use pre-7-Oct windows where possible
- **rhetorical:**
  - **R01:** travel equals capture
  - **R02:** organizer claim equals measured effect
  - **R03:** post-trip chronology equals causality
  - **R04:** actor identity equals state relation
- **speaker:**
  - **goal:** forensic measurement of travel exposure and causal effect
  - **target:** ELNET-funded parliamentary travel -> French parliamentary behavior
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** resource
  - **S02:** funding
  - **S03:** travel
  - **S04:** participant
  - **S05:** access
  - **S06:** briefing
  - **S07:** exposure
  - **S08:** reception
  - **S09:** policy_prompt
  - **S10:** public_act
  - **S11:** pre_alignment
  - **S12:** common_shock
  - **S13:** matched_control
  - **S14:** causality
  - **S15:** effect_gap
- **threats:**
  - travel=capture
  - organizer claim=measured persuasion
  - chronology=causality
  - Jewish/pro-Israel identity=Israeli state tasking
  - post-Oct7 output=trip effect

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - effect
  - **input_ids:**
    - FCT-001
    - FCT-004
    - FCT-006
    - FCT-014
  - **module:** clusters/POWER.md
  - **negative_results:**
    - capture/control not established
  - **not_computable:**
    - marginal persuasion
  - **operations_applied:**
    - typed exposure channel
    - bounded lobbying resource
  - **reason:** separate funded access from policy control
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CAU-001
  - **status:** DONE
  - **trigger:** resource/access
- **item 2:**
  - **gaps:**
    - complete participant network
  - **input_ids:**
    - FCT-010
    - FCT-011
    - FCT-014
    - FCT-016
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - state tasking not established
  - **not_computable:**
    - undisclosed relation universe
  - **operations_applied:**
    - preserved own-account status
    - tested pre-alignment
  - **reason:** test selection and relation edges
  - **result_ids:**
    - CLM-004
    - CLM-007
    - CTRL-002
    - CTRL-004
  - **status:** DONE
  - **trigger:** participant selection
- **item 3:**
  - **gaps:**
    - matched longitudinal panel
  - **input_ids:**
    - FCT-006
    - FCT-010
    - FCT-011
    - FCT-012
    - FCT-013
  - **module:** clusters/TEMPORAL.md
  - **negative_results:**
    - naive post-trip causality fails
  - **not_computable:**
    - representative treatment effect
  - **operations_applied:**
    - ordered pre/post events
    - identified Oct-7 confound
  - **reason:** avoid chronology fallacy and isolate common shock
  - **result_ids:**
    - CLM-004
    - CLM-005
    - CAU-002
    - CAU-003
  - **status:** DONE
  - **trigger:** before/after effect
- **item 4:**
  - **gaps:**
    - complete historical participant universe
  - **input_ids:**
    - FCT-001
    - FCT-002
    - FCT-003
    - FCT-004
    - FCT-005
  - **module:** clusters/ICEBERG.md
  - **negative_results:**
    - declaration count is not effect
  - **not_computable:**
    - long-run effect rate
  - **operations_applied:**
    - declaration denominator
    - shadow-participant warning
    - comparator caution
  - **reason:** test omitted participants and denominator
  - **result_ids:**
    - CLM-001
    - CLM-006
    - CTRL-001
  - **status:** DONE
  - **trigger:** denominator/selection

### SCOPING_REPORT
- **classification_dimensions:**
  - funding
  - travel
  - participant
  - programme
  - policy prompt
  - pre-position
  - post-output
  - counterfactual
- **exclusions:**
  - Jewish identity as relation proxy
  - general Israeli influence beyond ELNET travel
  - US AIPAC mechanism
  - unverified allegations from partisan inquiry proposals
- **scope:** France 2017-2026; ELNET-funded parliamentary travel, participant exposure and identifiable parliamentary outputs; causal effect tested against selection and common shocks.
- **status:** ACTIVE

### CREDO
- travel != capture
- funding != command
- access != adoption
- exposure != persuasion
- post-trip congruence != travel causation
- self-selection must be tested
- October 7 shock must be controlled
- own-account lobbying != foreign tasking

### COGNITIVE_MAP
- **chain:**
  - ELNET resource/funding
  - trip participation
  - curated meetings/briefings
  - exposure
  - participant reception
  - later parliamentary act
  - marginal causal effect
- **core_model:** ELNET-funded travel is a large, structured parliamentary exposure channel. Specific trips contain explicit policy-oriented prompts and organizer-reported commitments, but the inspectable corpus does not isolate a representative causal effect on parliamentary behavior because pre-treatment alignment, voluntary selection and the October 7 common shock are material rivals.
- **rival_models:**
  - self-selection of already aligned MPs
  - party ideology and specialization
  - normal parliamentary diplomacy
  - October 7 common shock
  - reinforcement rather than conversion

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** Official data prove funding/exposure, not purchase; participants can be pre-aligned and participation is voluntary.
  - **resolution:** Treat travel as a measurable exposure/treatment candidate; require pre/post matched evidence for effect.
  - **thesis:** ELNET trips buy parliamentary positions.
- **item 2:**
  - **antithesis:** Prompts are self-reported and later outputs face missing lineage or October 7 confounding.
  - **resolution:** Classify policy prompts as real; causal uptake remains partial/gap.
  - **thesis:** March 2023 commitments prove later policy capture.
- **item 3:**
  - **antithesis:** Scale, curated access and explicit influence-oriented programme make the mechanism materially testable.
  - **resolution:** Resource/action/exposure is supported; persuasion/behavior/outcome remains open.
  - **thesis:** No proven effect means trips are irrelevant.

### RESOURCE_FLOW_MAP
- **flows:**
  - ELNET resources -> travel/logistics -> MPs -> Israeli officials/security/civil-society briefings
  - Israeli MFA official -> Abraham Accords caucus suggestion -> French delegation
  - ELNET/briefers -> PA-funding narrative -> stated MP vigilance
- **limits:**
  - no command edge
  - no complete cost-per-trip dataset in run
  - no representative behavior effect estimate

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** ELNET France/network
  - **relation:** organizes/funds parliamentary delegations
  - **support:**
    - FCT-001
    - FCT-003
    - FCT-004
    - FCT-005
    - FCT-006
  - **to:** French MPs
- **item 2:**
  - **from:** Israeli MFA officials
  - **relation:** briefing/suggestion during delegation
  - **support:**
    - FCT-007
  - **to:** French MPs
- **item 3:**
  - **from:** French MPs
  - **relation:** later public acts on Israel/PA issues
  - **support:**
    - FCT-010
    - FCT-012
    - FCT-013
  - **to:** French Parliament/Government

### IMPACT_MAP
- **affected:**
  - participating MPs
  - parliamentary policy agenda
- **benefits:**
  - ELNET obtains repeated access and structured exposure to lawmakers
- **costs_harms:**
  - potential asymmetry of sponsored access and selection risk; causal harm not established
- **response_change:** Specific later acts are observable but causal treatment effect is not isolated.
- **status:** BOUNDED

### CONTRADICTION_LEDGER
- **item 1:**
  - **claim:** trip exposure caused later aligned acts
  - **counter:** pre-treatment alignment documented for named participant; October 7 is major common shock
  - **status:** UNRESOLVED
- **item 2:**
  - **claim:** March 2023 Abraham caucus prompt produced an official group
  - **counter:** bounded official searches located no material group trace
  - **status:** GAP_NOT_PROOF_OF_ABSENCE
- **item 3:**
  - **claim:** funded travel implies quid pro quo
  - **counter:** no instruction/exchange record inspected; HATVP says own-account; ELNET denies quid pro quo
  - **status:** NOT_ESTABLISHED

### VERIFICATION_REPORT
- **facts:** 16
- **fetches:** 13
- **interested_party_sources:**
  - ELNET
- **primary_or_official_sources:**
  - Assemblée nationale
  - HATVP
- **queries:** 39
- **sources:** 13
- **verification_rule:** Organizer claims used for programme/claimed commitments only; effect claims require independent parliamentary records.
- **web_discovery:** 26

### EDI_REPORT
- **corpus:** 13 accepted sources; 16 normalized facts; official Assembly/HATVP records plus ELNET organizer self-reports; 39 logged research/retrieval queries
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim:** CLM-001
    - **families:**
      - other:assembly_fr
  - **item 2:**
    - **claim:** CLM-004
    - **families:**
      - other:assembly_fr
      - other:elnet
  - **item 3:**
    - **claim:** CLM-006
    - **families:**
      - other:assembly_fr
      - other:elnet
      - other:hatvp
- **diagnostic_not_truth:** true
- **dimensions:**
  - scale
  - funding
  - participant exposure
  - policy prompt
  - pre-treatment alignment
  - post-output
  - causal attribution
- **edi:** OFFICIAL_TRAVEL_AND_PARLIAMENTARY_RECORDS_PLUS_ORGANIZER_PROGRAMME_SELF_REPORT_WITH_CAUSAL_DESIGN_GAP
- **source_counts:**
  - **other:assembly_fr:** 10
  - **other:elnet:** 2
  - **other:hatvp:** 1

### RESPONSIBILITY_MAP
- **ELNET:** responsible for documented trip organization/funding and self-described programme framing
- **French Assembly:** provides disclosure framework and parliamentary outputs
- **French MPs:** retain autonomous agency; participation and later acts cannot be attributed to sponsor without causal evidence
- **Israeli officials:** responsible for documented/sourced briefings and specific suggestion as reported by ELNET

### NEXT_QUERIES
- Build complete participant-level ELNET travel panel 2017-2026 from Assembly/Senate declarations
- Code pre-treatment Israel/PA positions for participants and matched non-participants
- Trace March 2023 Abraham-Accords caucus suggestion through bureau/group-study records
- Trace PA-funding commitment through participant-specific questions/amendments before 7 Oct where possible
- Acquire trip cost/in-kind data and Senate denominator for symmetry

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-002 | support:- | counter:- | results:FCT-001,FCT-002 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-003,QRY-004,QRY-005 | support:- | counter:- | results:FCT-003,FCT-004,FCT-005 | final:SATURATED | gap:NONE
LED-003 | attempts:QRY-006,QRY-007,QRY-008,QRY-009,QRY-010 | support:- | counter:- | results:FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-012,FCT-013 | final:SATURATED | gap:NONE
LED-004 | attempts:QRY-008,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-010,FCT-011,FCT-014,FCT-016 | final:SATURATED | gap:NONE
LED-005 | attempts:QRY-009,QRY-010 | support:- | counter:- | results:FCT-012,FCT-013 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-014,QRY-015,QRY-016 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-017,QRY-018,QRY-019,QRY-021,QRY-025,QRY-038,QRY-039 | support:- | counter:- | results:FCT-007,FCT-008,FCT-009,FCT-010,FCT-012,FCT-013 | final:GAP | gap:POLICY_FOOTPRINT
AXS-003 | attempts:QRY-008,QRY-011,QRY-013,QRY-031,QRY-032 | support:- | counter:- | results:FCT-010,FCT-011,FCT-016 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-001,QRY-003,QRY-004,QRY-005,QRY-006,QRY-008,QRY-009,QRY-010,QRY-011,QRY-014,QRY-015,QRY-016,QRY-018,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023,QRY-024,QRY-025,QRY-026,QRY-027,QRY-028,QRY-029,QRY-030,QRY-031,QRY-032,QRY-033,QRY-034,QRY-035,QRY-036,QRY-037,QRY-038,QRY-039 | support:- | counter:- | results:FCT-001,FCT-003,FCT-004,FCT-005,FCT-006,FCT-010,FCT-011,FCT-012,FCT-013 | final:GAP | gap:CAUSAL_DESIGN
CLM-001 | attempts:QRY-001,QRY-014 | support:FCT-001,FCT-002 | counter:The report gives declaration counts,not unique trips,persuasion or policy effect; Taiwan and Qatar are examples rather than a complete causal comparator design. | results:FCT-001,FCT-002 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-004,QRY-005,QRY-006,QRY-007,QRY-012 | support:FCT-004,FCT-006,FCT-007,FCT-008,FCT-009,FCT-014,FCT-015 | counter:Organizer descriptions establish programme and intended framing,not participant persuasion or behavioral change. | results:FCT-004,FCT-006,FCT-007,FCT-008,FCT-009,FCT-014,FCT-015 | final:PARTIAL | gap:EFFECT
CLM-003 | attempts:QRY-006,QRY-017,QRY-019,QRY-021,QRY-025,QRY-038,QRY-039 | support:FCT-007,FCT-008 | counter:These are ELNET self-reports of a suggestion and participant response; the bounded search did not locate a resulting official Abraham-Accords study group before the later geopolitical shock. | results:FCT-007,FCT-008,FCT-012,FCT-013 | final:PARTIAL | gap:POLICY_FOOTPRINT
CLM-004 | attempts:QRY-008,QRY-011,QRY-013,QRY-031,QRY-032 | support:FCT-010,FCT-011,FCT-016 | counter:A trip may still reinforce or sharpen existing positions; this corpus does not measure attitude intensity before and after. | results:FCT-010,FCT-011,FCT-016 | final:SUPPORTED | gap:CAUSAL_ATTRIBUTION
CLM-005 | attempts:QRY-009,QRY-010,QRY-019,QRY-025,QRY-027 | support:FCT-008,FCT-012,FCT-013 | counter:The same outputs can plausibly arise from the October 7 shock,party positions and pre-existing preferences; the resolution had many co-signatories. | results:FCT-008,FCT-012,FCT-013 | final:PARTIAL | gap:CAUSAL_ATTRIBUTION
CLM-006 | attempts:QRY-001,QRY-003,QRY-004,QRY-005,QRY-006,QRY-008,QRY-009,QRY-010,QRY-011,QRY-014,QRY-015,QRY-016,QRY-018,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023,QRY-024,QRY-025,QRY-026,QRY-027,QRY-028,QRY-029,QRY-030,QRY-031,QRY-032,QRY-033,QRY-034,QRY-035,QRY-036,QRY-037,QRY-038,QRY-039 | support:FCT-001,FCT-003,FCT-004,FCT-005,FCT-006,FCT-010,FCT-011,FCT-012,FCT-013 | counter:Scale and explicit policy-intent make an effect plausible and testable,but plausibility is not an effect estimate. | results:FCT-001,FCT-003,FCT-004,FCT-005,FCT-006,FCT-010,FCT-011,FCT-012,FCT-013 | final:GAP | gap:CAUSAL_DESIGN
CLM-007 | attempts:QRY-012,QRY-013 | support:FCT-014,FCT-016 | counter:Own-account declaration and ELNET denial do not prove absence of undisclosed influence; they bound what can be claimed from inspected evidence. | results:FCT-014,FCT-016 | final:SUPPORTED | gap:RELATION

## STATUS_DELTA_V1
DELTA-001 | LED-001 | ACTIVE | SATURATED | fresh searches inspected and lead terminalized
DELTA-002 | LED-002 | ACTIVE | SATURATED | fresh searches inspected and lead terminalized
DELTA-003 | LED-003 | ACTIVE | SATURATED | fresh searches inspected and lead terminalized
DELTA-004 | LED-004 | ACTIVE | SATURATED | fresh searches inspected and lead terminalized
DELTA-005 | LED-005 | ACTIVE | SATURATED | fresh searches inspected and lead terminalized
DELTA-006 | AXS-001 | ACTIVE | SATURATED | axis terminalized after fresh retrieval and causal testing
DELTA-007 | AXS-002 | ACTIVE | GAP | axis terminalized after fresh retrieval and causal testing
DELTA-008 | AXS-003 | ACTIVE | SATURATED | axis terminalized after fresh retrieval and causal testing
DELTA-009 | AXS-004 | ACTIVE | GAP | axis terminalized after fresh retrieval and causal testing

## OPEN_GAPS_V1
AXS-002 | AXS | GAP | POLICY_FOOTPRINT | Specific prompts/commitments are documented, but bounded searches did not close a direct trip-to-output lineage; strongest later outputs are confounded by October 7.
AXS-004 | AXS | GAP | CAUSAL_DESIGN | No complete participant panel, baseline outcome coding and matched non-travel control design is available in the bounded run.
CLM-002 | CLM | PARTIAL | EFFECT | Reception and persuasion are not directly measured.
CLM-003 | CLM | PARTIAL | POLICY_FOOTPRINT | No closed adoption trace for the proposed caucus; PA-funding outputs later occur under heavy post-7-October confounding.
CLM-004 | CLM | SUPPORTED | CAUSAL_ATTRIBUTION | Need participant-level pre/post measures and matched non-travel controls.
CLM-005 | CLM | PARTIAL | CAUSAL_ATTRIBUTION | No design isolates the marginal travel effect from common shock and selection.
CLM-006 | CLM | GAP | CAUSAL_DESIGN | Need complete participant universe, pre-treatment outcomes, matched controls/event-study design and issue-specific outcome coding.
CLM-007 | CLM | SUPPORTED | RELATION | No inspected instruction, conditional benefit, vote exchange or command record connects travel to a specific parliamentary act.
CAU-002 | CAU | UNRESOLVED | CAUSAL_ATTRIBUTION | Need direct follow-up records or participant testimony/draft provenance plus pre/post controls.
CAU-003 | CAU | UNRESOLVED | CAUSAL_DESIGN | Need complete panel, baseline outcomes, matched non-travel MPs and coded issue outcomes.
CAU-004 | CAU | UNRESOLVED | RELATION | No instruction/condition/exchange evidence inspected.

SEMANTIC_COUNTS_V1:LED:5|CLM:7|AXS:4|CAU:4|CTRL:6|ACT:4

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-002"],"evidence_excerpt":"Need current-legislature denominator and historical trip records.","kind":"DATA_LEAD","lead":"Scale and denominator of ELNET-funded parliamentary travel under French disclosure rules","linked_ids":["AXS-001"],"locator":"Assemblée travel declarations + 2026 parliamentary diplomacy report","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002"],"routes":["EXPAND","LINK"],"source_id":"SRC-001","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-003","QRY-004","QRY-005"],"evidence_excerpt":"Official declarations provide financeur, dates, purpose and named participants.","kind":"EVENT_LEAD","lead":"July 2021 ELNET mission and named French MPs","linked_ids":["AXS-001","AXS-003"],"locator":"Assemblée travel declarations 15th legislature","materiality":"IMPORTANT","result_ids":["FCT-003","FCT-004","FCT-005"],"routes":["EXPAND","LINK"],"source_id":"SRC-003","status":"SATURATED"}
LED-003 | {"attempt_ids":["QRY-006","QRY-007","QRY-008","QRY-009","QRY-010"],"evidence_excerpt":"ELNET describes security inspiration, Abraham Accords caucus suggestion and vigilance on Palestinian-authority funding.","kind":"MECHANISM_LEAD","lead":"March 2023 LR delegation contains explicit policy-intent and participant commitments","linked_ids":["AXS-002","AXS-004"],"locator":"ELNET delegation report March 2023","materiality":"DECISIVE","result_ids":["FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-012","FCT-013"],"routes":["EXPAND","LINK"],"source_id":"SRC-006","status":"SATURATED"}
LED-004 | {"attempt_ids":["QRY-008","QRY-011","QRY-012","QRY-013"],"evidence_excerpt":"Need pre-trip positions and group roles for exposed MPs.","kind":"RIVAL_LEAD","lead":"Self-selection and pre-treatment alignment may explain post-trip positions","linked_ids":["AXS-003","AXS-004"],"locator":"pre-trip parliamentary records + voluntary participation","materiality":"DECISIVE","result_ids":["FCT-010","FCT-011","FCT-014","FCT-016"],"routes":["EXPAND","LINK"],"source_id":"SRC-011","status":"SATURATED"}
LED-005 | {"attempt_ids":["QRY-009","QRY-010"],"evidence_excerpt":"Prefer pre-Oct-7 trips for causal discrimination.","kind":"CAUSAL_DESIGN_LEAD","lead":"October 7 2023 is a major common shock confounding recent before/after comparisons","linked_ids":["AXS-004"],"locator":"trip dates and parliamentary outputs","materiality":"IMPORTANT","result_ids":["FCT-012","FCT-013"],"routes":["CONTEXT","LINK"],"source_id":"SRC-009","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"attempt_ids":["QRY-001","QRY-014"],"claim":"ELNET-funded parliamentary travel is a quantitatively large exposure channel in the current legislature: 38 of 82 declared travel invitations were ELNET-funded as of 1 December 2025.","claimant":"INV-161","counter":"The report gives declaration counts, not unique trips, persuasion or policy effect; Taiwan and Qatar are examples rather than a complete causal comparator design.","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002"],"status":"SUPPORTED","support":"FCT-001,FCT-002"}
CLM-002 | {"attempt_ids":["QRY-004","QRY-005","QRY-006","QRY-007","QRY-012"],"claim":"ELNET designs parliamentary delegations as structured exposure to Israeli political, military, diplomatic and policy frames, and its declared French lobbying activity includes parliamentary delegations and influence-oriented contacts.","claimant":"INV-161","counter":"Organizer descriptions establish programme and intended framing, not participant persuasion or behavioral change.","gap":"Reception and persuasion are not directly measured.","gap_type":"EFFECT","materiality":"DECISIVE","result_ids":["FCT-004","FCT-006","FCT-007","FCT-008","FCT-009","FCT-014","FCT-015"],"status":"PARTIAL","support":"FCT-004,FCT-006,FCT-007,FCT-008,FCT-009,FCT-014,FCT-015"}
CLM-003 | {"attempt_ids":["QRY-006","QRY-017","QRY-019","QRY-021","QRY-025","QRY-038","QRY-039"],"claim":"The March 2023 LR mission generated identifiable policy-oriented prompts and stated commitments, including a proposed French Abraham Accords study group and vigilance over Palestinian-Authority funding.","claimant":"INV-161","counter":"These are ELNET self-reports of a suggestion and participant response; the bounded search did not locate a resulting official Abraham-Accords study group before the later geopolitical shock.","gap":"No closed adoption trace for the proposed caucus; PA-funding outputs later occur under heavy post-7-October confounding.","gap_type":"POLICY_FOOTPRINT","materiality":"IMPORTANT","result_ids":["FCT-007","FCT-008","FCT-012","FCT-013"],"status":"PARTIAL","support":"FCT-007,FCT-008"}
CLM-004 | {"attempt_ids":["QRY-008","QRY-011","QRY-013","QRY-031","QRY-032"],"claim":"Post-trip pro-Israel or PA-funding positions by exposed MPs cannot be attributed to ELNET travel from chronology alone because pre-treatment alignment and prior Israel engagement are observable.","claimant":"INV-161","counter":"A trip may still reinforce or sharpen existing positions; this corpus does not measure attitude intensity before and after.","gap":"Need participant-level pre/post measures and matched non-travel controls.","gap_type":"CAUSAL_ATTRIBUTION","materiality":"DECISIVE","result_ids":["FCT-010","FCT-011","FCT-016"],"status":"SUPPORTED","support":"FCT-010,FCT-011,FCT-016"}
CLM-005 | {"attempt_ids":["QRY-009","QRY-010","QRY-019","QRY-025","QRY-027"],"claim":"Several later parliamentary acts are congruent with themes presented during ELNET travel, but the strongest examples after October 2023 are confounded by the 7 October attack and broad party/parliamentary dynamics.","claimant":"INV-161","counter":"The same outputs can plausibly arise from the October 7 shock, party positions and pre-existing preferences; the resolution had many co-signatories.","gap":"No design isolates the marginal travel effect from common shock and selection.","gap_type":"CAUSAL_ATTRIBUTION","materiality":"DECISIVE","result_ids":["FCT-008","FCT-012","FCT-013"],"status":"PARTIAL","support":"FCT-008,FCT-012,FCT-013"}
CLM-006 | {"attempt_ids":["QRY-001","QRY-003","QRY-004","QRY-005","QRY-006","QRY-008","QRY-009","QRY-010","QRY-011","QRY-014","QRY-015","QRY-016","QRY-018","QRY-019","QRY-020","QRY-021","QRY-022","QRY-023","QRY-024","QRY-025","QRY-026","QRY-027","QRY-028","QRY-029","QRY-030","QRY-031","QRY-032","QRY-033","QRY-034","QRY-035","QRY-036","QRY-037","QRY-038","QRY-039"],"claim":"A representative causal effect of ELNET-funded trips on parliamentary votes, questions, amendments or public positions is not established by the currently inspectable corpus.","claimant":"INV-161","counter":"Scale and explicit policy-intent make an effect plausible and testable, but plausibility is not an effect estimate.","gap":"Need complete participant universe, pre-treatment outcomes, matched controls/event-study design and issue-specific outcome coding.","gap_type":"CAUSAL_DESIGN","materiality":"DECISIVE","result_ids":["FCT-001","FCT-003","FCT-004","FCT-005","FCT-006","FCT-010","FCT-011","FCT-012","FCT-013"],"status":"GAP","support":"FCT-001,FCT-003,FCT-004,FCT-005,FCT-006,FCT-010,FCT-011,FCT-012,FCT-013"}
CLM-007 | {"attempt_ids":["QRY-012","QRY-013"],"claim":"The inspected evidence does not establish quid pro quo, capture or Israeli-state command of MPs through ELNET travel.","claimant":"INV-161","counter":"Own-account declaration and ELNET denial do not prove absence of undisclosed influence; they bound what can be claimed from inspected evidence.","gap":"No inspected instruction, conditional benefit, vote exchange or command record connects travel to a specific parliamentary act.","gap_type":"RELATION","materiality":"IMPORTANT","result_ids":["FCT-014","FCT-016"],"status":"SUPPORTED","support":"FCT-014,FCT-016"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-014","QRY-015","QRY-016"],"axis":"EXPOSURE_SCALE","links":["CLM-001","CLM-002","CAU-001"],"question":"How frequent and concentrated are ELNET-funded parliamentary trips relative to all declared trips and selected foreign comparators?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006"],"sought_objects":["official travel declarations","current-legislature denominator","named participants","financeur"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-017","QRY-018","QRY-019","QRY-021","QRY-025","QRY-038","QRY-039"],"axis":"POLICY_FOOTPRINT_AFTER_TRIP","gap":"Specific prompts/commitments are documented, but bounded searches did not close a direct trip-to-output lineage; strongest later outputs are confounded by October 7.","gap_type":"POLICY_FOOTPRINT","links":["CLM-003","CLM-005","CAU-002"],"question":"Do explicit themes or commitments from ELNET trips recur in later parliamentary acts by participants?","result_ids":["FCT-007","FCT-008","FCT-009","FCT-010","FCT-012","FCT-013"],"sought_objects":["questions","resolutions","amendments","study groups","speeches"],"status":"GAP"}
AXS-003 | {"attempt_ids":["QRY-008","QRY-011","QRY-013","QRY-031","QRY-032"],"axis":"SELF_SELECTION","links":["CLM-004","CAU-003","CTRL-002"],"question":"Were exposed MPs already aligned or active on Israel-related issues before travel?","result_ids":["FCT-010","FCT-011","FCT-016"],"sought_objects":["pre-trip speeches","prior Israel travel","group membership","prior questions"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-001","QRY-003","QRY-004","QRY-005","QRY-006","QRY-008","QRY-009","QRY-010","QRY-011","QRY-014","QRY-015","QRY-016","QRY-018","QRY-019","QRY-020","QRY-021","QRY-022","QRY-023","QRY-024","QRY-025","QRY-026","QRY-027","QRY-028","QRY-029","QRY-030","QRY-031","QRY-032","QRY-033","QRY-034","QRY-035","QRY-036","QRY-037","QRY-038","QRY-039"],"axis":"CAUSAL_EFFECT","gap":"No complete participant panel, baseline outcome coding and matched non-travel control design is available in the bounded run.","gap_type":"CAUSAL_DESIGN","links":["CLM-004","CLM-005","CLM-006","CAU-003"],"question":"Can any observed post-trip behavior be attributed to travel rather than prior preferences, party position or common shocks?","result_ids":["FCT-001","FCT-003","FCT-004","FCT-005","FCT-006","FCT-010","FCT-011","FCT-012","FCT-013"],"sought_objects":["within-person pre/post","matched controls","pre-Oct-7 windows","negative outcomes"],"status":"GAP"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"Official declarations and organizer records directly establish funding/organization, participation, meetings and briefings; this closes the resource/action/exposure edge without implying persuasion.","counter":"Exposure is documented but reception/persuasion is not measured.","gap":"NONE","gap_type":"NONE","limit":"Closes I1-I4 (resource/action/exposure), not I5-I7.","mechanism":"ELNET funding/organization -> parliamentary trip -> curated meetings/briefings -> exposure to Israel-related frames","status":"SUPPORTED","support":"FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-014"}
CAU-002 | {"counter":"No official Abraham-Accords study group was located in bounded searches; later PA-related acts are confounded by October 7 and pre-existing positions.","gap":"Need direct follow-up records or participant testimony/draft provenance plus pre/post controls.","gap_type":"CAUSAL_ATTRIBUTION","limit":"Policy-congruent outputs exist but marginal travel contribution is not isolated.","mechanism":"March 2023 ELNET/Israeli-official input -> participant stated commitment -> later parliamentary policy output","status":"UNRESOLVED","support":"FCT-007,FCT-008,FCT-010,FCT-012,FCT-013"}
CAU-003 | {"counter":"FCT-011 shows prior Israel-related framing by Dumont; FCT-010 indicates Genevard had prior Israel/Palestinian encounters; October 7 is a large common shock.","gap":"Need complete panel, baseline outcomes, matched non-travel MPs and coded issue outcomes.","gap_type":"CAUSAL_DESIGN","limit":"No representative causal estimate.","mechanism":"ELNET trip -> changed participant attitude/behavior -> changed parliamentary outcome","status":"UNRESOLVED","support":"FCT-001,FCT-006,FCT-010,FCT-012,FCT-013"}
CAU-004 | {"counter":"HATVP records own-account lobbying; no inspected command/conditional exchange record; ELNET denies quid pro quo.","gap":"No instruction/condition/exchange evidence inspected.","gap_type":"RELATION","limit":"Not established from current evidence.","mechanism":"ELNET-funded travel -> quid pro quo/state tasking -> specific vote or decision","status":"UNRESOLVED","support":"FCT-014,FCT-016"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Declared trip scale is exposure, not persuasion or effect.","status":"PASS","support":"FCT-001,FCT-002"}
CTRL-002 | {"control":"Pre-treatment alignment/self-selection must be preserved.","status":"PASS","support":"FCT-011 and FCT-010 show relevant prior positioning/experience."}
CTRL-003 | {"control":"October 7 2023 is a material common shock for post-2023 outputs.","status":"PASS","support":"FCT-012 and FCT-013 occur after the shock and cannot isolate travel effect."}
CTRL-004 | {"control":"Own-account lobbying does not establish Israeli-state tasking.","status":"PASS","support":"FCT-014."}
CTRL-005 | {"control":"Organizer self-report of inspiration/commitment is not independent behavioral measurement.","status":"PASS","support":"FCT-007,FCT-008,FCT-009."}
CTRL-006 | {"control":"Failure to locate a proposed study group in bounded searches is a gap/negative result, not proof it never existed.","status":"PASS","support":"QRY-017,QRY-021,QRY-038,QRY-039 returned no material official study-group trace."}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Funded or organized repeated parliamentary trips to Israel and structured meetings/briefings around bilateral, security and policy themes.","actor":"ELNET France / ELNET network","intent":"PROVEN","status":"DONE","support":["FCT-001","FCT-003","FCT-004","FCT-005","FCT-006","FCT-014"]}
ACT-002 | {"action":"Proposed a French parliamentary study group on the Abraham Accords; delegation reportedly welcomed and agreed to study modalities.","actor":"Israeli Foreign Ministry officials during March 2023 delegation","intent":"PROVEN_AS_REPORTED_BY_ORGANIZER","status":"DONE","support":["FCT-007"]}
ACT-003 | {"action":"According to organizer report, expressed commitment to vigilance regarding European funds to the Palestinian Authority.","actor":"French MPs in March 2023 delegation","intent":"REPORTED","status":"DONE","support":["FCT-008"]}
ACT-004 | {"action":"Requires declaration of third-party travel and publishes accepted invitations, enabling exposure measurement.","actor":"French National Assembly / ethics framework","intent":"PROVEN","status":"DONE","support":["FCT-001","FCT-002"]}

SEARCH_ACTIVITY_V1:WEB:26|FETCH:13|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | UNAVAILABLE | MNEMO | MNEMO_UNAVAILABLE | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | PASS | SRC-001 | https://www.assemblee-nationale.fr/dyn/opendata/RINFANR5L17B2466.html | FETCH official parliamentary diplomacy report ELNET travel denominator
QRY-002 | FETCH | PASS | SRC-002 | https://www.assemblee-nationale.fr/dyn/deontologie/declarations | FETCH Assembly rules third-party parliamentary travel disclosure
QRY-003 | FETCH | PASS | SRC-003 | https://www.assemblee-nationale.fr/dyn/15/donsetvoyages/voyages?limit=5&page=5 | FETCH 2021 ELNET travel declarations page 5
QRY-004 | FETCH | PASS | SRC-004 | https://www.assemblee-nationale.fr/dyn/15/donsetvoyages/voyages?limit=5&page=6 | FETCH 2021 ELNET travel declarations page 6
QRY-005 | FETCH | PASS | SRC-005 | https://www.assemblee-nationale.fr/dyn/15/donsetvoyages/voyages?limit=5&page=7 | FETCH 2021 ELNET travel declarations page 7
QRY-006 | FETCH | PASS | SRC-006 | https://elnetwork.fr/delegation/delegation-parlementaire-les-republicains-en-israel-mars-2023/ | FETCH ELNET March 2023 LR delegation report
QRY-007 | FETCH | PASS | SRC-007 | https://elnetwork.fr/vie-parlementaire-et-politique/place-du-palais-bourbon-semaine-du-13-au-17-mars-2023/ | FETCH ELNET weekly account March 2023 delegation
QRY-008 | FETCH | PASS | SRC-008 | https://www.assemblee-nationale.fr/dyn/16/comptes-rendus/seance/session-ordinaire-de-2022-2023/premiere-seance-du-jeudi-04-mai-2023 | FETCH Assembly 4 May 2023 Annie Genevard Israel debate
QRY-009 | FETCH | PASS | SRC-009 | https://www.assemblee-nationale.fr/dyn/docs/PNREANR5L16B1744.raw | FETCH Assembly resolution 1744 Palestinian education 13 Oct 2023
QRY-010 | FETCH | PASS | SRC-010 | https://www.assemblee-nationale.fr/dyn/16/comptes-rendus/seance/session-ordinaire-de-2023-2024/premiere-seance-du-mardi-16-janvier-2024 | FETCH Assembly 16 Jan 2024 Pierre-Henri Dumont Palestinian aid
QRY-011 | FETCH | PASS | SRC-011 | https://www.assemblee-nationale.fr/dyn/15/comptes-rendus/seance/session-ordinaire-de-2018-2019/premiere-seance-du-jeudi-14-fevrier-2019.pdf | FETCH+SCREEN Assembly 14 Feb 2019 Pierre-Henri Dumont Israel convention
QRY-012 | FETCH | PASS | SRC-012 | https://www.hatvp.fr/fiche-organisation/?organisation=531006237 | FETCH HATVP ELNET France interest representation record
QRY-013 | FETCH | PASS | SRC-013 | https://elnetwork.fr/communique/droit-de-reponse-delnet-a-mediapart/ | FETCH ELNET right of reply parliamentary delegations voluntary
QRY-014 | WEB | PASS | - | - | site:assemblee-nationale.fr ELNET voyage parlementaire 38 déclarations 1 décembre 2025
QRY-015 | WEB | PASS | - | - | site:assemblee-nationale.fr ELNET mars 2023 député voyage Israël
QRY-016 | WEB | PASS | - | - | site:assemblee-nationale.fr ELNET 2021 voyage Israël député
QRY-017 | WEB | NO_RESULT | - | - | site:assemblee-nationale.fr accords d Abraham député 2023 Israël groupe études
QRY-018 | WEB | NO_RESULT | - | - | site:assemblee-nationale.fr reconnaissance faciale Paris 2024 député LR mars 2023 Israël ELNET
QRY-019 | WEB | PASS | - | - | site:assemblee-nationale.fr financement Autorité palestinienne député LR 2023 question
QRY-020 | WEB | PASS | - | - | site:elnetwork.fr délégation parlementaire Les Républicains Israël mars 2023 Pierre-Henri Dumont Annie Genevard
QRY-021 | WEB | NO_RESULT | - | - | site:assemblee-nationale.fr accords d Abraham Pierre-Henri Dumont
QRY-022 | WEB | PASS | - | - | site:assemblee-nationale.fr accords d Abraham Annie Genevard
QRY-023 | WEB | NO_RESULT | - | - | site:assemblee-nationale.fr reconnaissance faciale Pierre-Henri Dumont 2023
QRY-024 | WEB | NO_RESULT | - | - | site:assemblee-nationale.fr reconnaissance faciale Annie Genevard 2023
QRY-025 | WEB | PASS | - | - | site:assemblee-nationale.fr Autorité palestinienne Pierre-Henri Dumont 2023 2024
QRY-026 | WEB | NO_RESULT | - | - | site:assemblee-nationale.fr Autorité palestinienne Annie Genevard 2023 2024
QRY-027 | WEB | NO_RESULT | - | - | site:assemblee-nationale.fr Pierre-Henri Dumont Autorité palestinienne before 2023-10-07 after 2023-03-14
QRY-028 | WEB | NO_RESULT | - | - | site:assemblee-nationale.fr Annie Genevard Autorité palestinienne before 2023-10-07 after 2023-03-14
QRY-029 | WEB | NO_RESULT | - | - | site:assemblee-nationale.fr Pierre-Henri Dumont Accords d Abraham before 2023-10-07 after 2023-03-14
QRY-030 | WEB | PASS | - | - | site:assemblee-nationale.fr Annie Genevard Accords d Abraham before 2023-10-07 after 2023-03-14
QRY-031 | WEB | PASS | - | - | site:assemblee-nationale.fr Pierre-Henri Dumont Israël before 2023-03-11
QRY-032 | WEB | PASS | - | - | site:assemblee-nationale.fr Annie Genevard Israël before 2023-03-11
QRY-033 | WEB | NO_RESULT | - | - | site:assemblee-nationale.fr/dyn/16/donsetvoyages/voyages ELNET mars 2023 Israël
QRY-034 | WEB | NO_RESULT | - | - | site:assemblee-nationale.fr/dyn/16/donsetvoyages/voyages ELNET 11 mars 2023
QRY-035 | WEB | NO_RESULT | - | - | site:assemblee-nationale.fr/dyn/16/donsetvoyages/voyages ELNET 14 mars 2023
QRY-036 | WEB | NO_RESULT | - | - | site:assemblee-nationale.fr/dyn/16/donsetvoyages/voyages Annie Genevard Israel ELNET
QRY-037 | WEB | NO_RESULT | - | - | site:assemblee-nationale.fr/dyn/16/donsetvoyages/voyages Pierre-Henri Dumont Israel ELNET
QRY-038 | WEB | NO_RESULT | - | - | site:assemblee-nationale.fr groupe études Accords d Abraham
QRY-039 | WEB | NO_RESULT | - | - | site:assemblee-nationale.fr Accords d Abraham groupe amitié 2023 2024

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:other:assembly_fr | AN-RINF-2466-2026 | Rapport d’information n°2466 — doctrine française de diplomatie parlementaire | 2026-02-11 | 2026-09-13T12:10:00+02:00 | Travel declarations: 47 MPs, 82 invitations, 38 ELNET as of 1 Dec 2025 | https://www.assemblee-nationale.fr/dyn/opendata/RINFANR5L17B2466.html
SRC-002 | ◈ | fam:other:assembly_fr | AN-DEONTO-TRAVEL | Assemblée nationale — déclarations dons et voyages | 2019-06-04 | 2026-09-13T12:10:00+02:00 | Article 80-1-2: third-party trip invitation declared before travel with programme/modalities | https://www.assemblee-nationale.fr/dyn/deontologie/declarations
SRC-003 | ◈ | fam:other:assembly_fr | AN-TRAVEL-15-P5 | Assemblée — invitations voyages, 15e législature page 5 | 2021-09-01 | 2026-09-13T12:10:00+02:00 | David Corceiro ELNET Israel trip 18-21 Jul 2021 | https://www.assemblee-nationale.fr/dyn/15/donsetvoyages/voyages?limit=5&page=5
SRC-004 | ◈ | fam:other:assembly_fr | AN-TRAVEL-15-P6 | Assemblée — invitations voyages, 15e législature page 6 | 2021-07-08 | 2026-09-13T12:10:00+02:00 | Pupponi, Marleix, Goulet, Quentin, Bonnivard ELNET trip declarations | https://www.assemblee-nationale.fr/dyn/15/donsetvoyages/voyages?limit=5&page=6
SRC-005 | ◈ | fam:other:assembly_fr | AN-TRAVEL-15-P7 | Assemblée — invitations voyages, 15e législature page 7 | 2021-07-01 | 2026-09-13T12:10:00+02:00 | Trastour-Isnart, Le Grip, Lagleize ELNET trip declarations | https://www.assemblee-nationale.fr/dyn/15/donsetvoyages/voyages?limit=5&page=7
SRC-006 | ◈ | fam:other:elnet | ELNET-LR-MAR2023 | ELNET — délégation parlementaire Les Républicains en Israël, mars 2023 | 2023-03-18 | 2026-09-13T12:10:00+02:00 | 15 LR MPs; program, stated inspiration, Abraham Accords suggestion, PA-funding vigilance | https://elnetwork.fr/delegation/delegation-parlementaire-les-republicains-en-israel-mars-2023/
SRC-007 | ◈ | fam:other:elnet | ELNET-PB-2023-03-17 | ELNET — Place du Palais Bourbon, 13–17 mars 2023 | 2023-03-17 | 2026-09-13T12:10:00+02:00 | ELNET self-report on effects/learning of LR trip | https://elnetwork.fr/vie-parlementaire-et-politique/place-du-palais-bourbon-semaine-du-13-au-17-mars-2023/
SRC-008 | ◈ | fam:other:assembly_fr | AN-CR-2023-05-04 | Assemblée — séance 4 mai 2023 | 2023-05-04 | 2026-09-13T12:10:00+02:00 | Genevard argues against apartheid resolution; cites two visits and Abraham Accords | https://www.assemblee-nationale.fr/dyn/16/comptes-rendus/seance/session-ordinaire-de-2022-2023/premiere-seance-du-jeudi-04-mai-2023
SRC-009 | ◈ | fam:other:assembly_fr | AN-PNR-1744 | Assemblée — proposition de résolution n°1744 | 2023-10-13 | 2026-09-13T12:10:00+02:00 | Resolution on Palestinian education; signatories include Dumont and Genevard | https://www.assemblee-nationale.fr/dyn/docs/PNREANR5L16B1744.raw
SRC-010 | ◈ | fam:other:assembly_fr | AN-CR-2024-01-16 | Assemblée — séance 16 janvier 2024 | 2024-01-16 | 2026-09-13T12:10:00+02:00 | Dumont challenges Palestinian aid after Oct 7 | https://www.assemblee-nationale.fr/dyn/16/comptes-rendus/seance/session-ordinaire-de-2023-2024/premiere-seance-du-mardi-16-janvier-2024
SRC-011 | ◈ | fam:other:assembly_fr | AN-CR-2019-02-14 | Assemblée — séance 14 février 2019 | 2019-02-14 | 2026-09-13T12:10:00+02:00 | Screenshot p.1248: Dumont objects to automatic Palestine-prisoner debate when Israel convention examined | https://www.assemblee-nationale.fr/dyn/15/comptes-rendus/seance/session-ordinaire-de-2018-2019/premiere-seance-du-jeudi-14-fevrier-2019.pdf
SRC-012 | ◈ | fam:other:hatvp | HATVP-ELNET-531006237 | HATVP — ELNET France | 2026-03-31 | 2026-09-13T12:10:00+02:00 | Own-account lobbying; annual objectives; 2023 parliamentary delegations; policy-influence methods | https://www.hatvp.fr/fiche-organisation/?organisation=531006237
SRC-013 | ◈ | fam:other:elnet | ELNET-DROIT-REPONSE | ELNET — droit de réponse à Mediapart | 2025-12-01 | 2026-09-13T12:10:00+02:00 | ELNET counter-claim: delegations voluntary/no quid pro quo expected | https://elnetwork.fr/communique/droit-de-reponse-delnet-a-mediapart/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/opendata/RINFANR5L17B2466.html | other:assembly_fr | 2026-02-11 | ELNET travel scale XVII legislature | At 1 December 2025, 47 distinct MPs had declared 82 travel invitations since the start of the XVII legislature; 38 declarations were ELNET-funded, compared with 6 Taiwan-funded and 4 Qatar-funded. | -
FCT-002 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/deontologie/declarations | other:assembly_fr | 2019-06-04 | French MP travel disclosure rule | Assembly rules require MPs to declare before travel any accepted invitation to a trip from a third party, with information on programme and modalities. | -
FCT-003 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/15/donsetvoyages/voyages?limit=5&page=5 | other:assembly_fr | 2021-09-01 | David Corceiro ELNET July 2021 trip | David Corceiro declared an ELNET-organized trip to Israel from 18 to 21 July 2021. | -
FCT-004 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/15/donsetvoyages/voyages?limit=5&page=6 | other:assembly_fr | 2021-07-08 | July 2021 ELNET delegation participants and purpose | Official declarations identify François Pupponi, Olivier Marleix, Perrine Goulet, Didier Quentin and Émilie Bonnivard among ELNET-funded participants; declarations describe a 38-elected-official information/friendship mission aimed at promoting the France-Israel strategic bilateral relationship and meetings with high Israeli authorities. | -
FCT-005 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/15/donsetvoyages/voyages?limit=5&page=7 | other:assembly_fr | 2021-07-01 | Additional July 2021 ELNET participants | Official declarations additionally identify Laurence Trastour-Isnart, Constance Le Grip and Jean-Luc Lagleize on the ELNET-funded 18-21 July 2021 Israel trip. | -
FCT-006 | FACT | ✧ | https://elnetwork.fr/delegation/delegation-parlementaire-les-republicains-en-israel-mars-2023/ | other:elnet | 2023-03-18 | March 2023 LR delegation scale | ELNET reports organizing a March 2023 delegation of 15 French Les Républicains MPs to Israel around public diplomacy, security/defense and ecological transition. | -
FCT-007 | FACT | ✧ | https://elnetwork.fr/delegation/delegation-parlementaire-les-republicains-en-israel-mars-2023/ | other:elnet | 2023-03-18 | Abraham Accords caucus suggestion | ELNET reports that an Israeli Foreign Ministry official suggested creation of a French parliamentary study group on the Abraham Accords and that the delegation welcomed the suggestion and agreed to study modalities. | -
FCT-008 | FACT | ✧ | https://elnetwork.fr/delegation/delegation-parlementaire-les-republicains-en-israel-mars-2023/ | other:elnet | 2023-03-18 | Palestinian Authority funding vigilance commitment | ELNET reports that after briefings on Palestinian media and financing, the French MPs committed to exercise strong vigilance over European funds allocated to the Palestinian Authority. | -
FCT-009 | FACT | ✧ | https://elnetwork.fr/delegation/delegation-parlementaire-les-republicains-en-israel-mars-2023/ | other:elnet | 2023-03-18 | Security-technology inspiration claim | ELNET states that exposure to Israeli security arrangements inspired participating MPs regarding security in their constituencies and France; this is an organizer self-report, not an independently measured behavioral effect. | -
FCT-010 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/16/comptes-rendus/seance/session-ordinaire-de-2022-2023/premiere-seance-du-jeudi-04-mai-2023 | other:assembly_fr | 2023-05-04 | Annie Genevard post-trip Israel position | On 4 May 2023 Annie Genevard argued against a resolution characterizing Israel as apartheid, referred to having met Israeli and Palestinian protagonists on two occasions, and highlighted the Abraham Accords as a major regional development. | -
FCT-011 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/15/comptes-rendus/seance/session-ordinaire-de-2018-2019/premiere-seance-du-jeudi-14-fevrier-2019.pdf | other:assembly_fr | 2019-02-14 | Pierre-Henri Dumont pre-trip Israel position | In February 2019, years before the March 2023 ELNET delegation, Pierre-Henri Dumont objected that debate on a convention with Israel automatically triggered extended discussion of Palestinian prisoners, demonstrating prior parliamentary positioning on Israel-related framing. | -
FCT-012 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/docs/PNREANR5L16B1744.raw | other:assembly_fr | 2023-10-13 | Post-7-Oct resolution signatories | A 13 October 2023 resolution proposal condemning education to hatred of Palestinian children listed Pierre-Henri Dumont and Annie Genevard among many co-signatories. | -
FCT-013 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/16/comptes-rendus/seance/session-ordinaire-de-2023-2024/premiere-seance-du-mardi-16-janvier-2024 | other:assembly_fr | 2024-01-16 | Pierre-Henri Dumont Palestinian-aid intervention | On 16 January 2024 Pierre-Henri Dumont challenged French/Western development aid to Palestinians and alleged diversion to Islamist terrorism after the 7 October attacks. | -
FCT-014 | FACT | ✧ | https://www.hatvp.fr/fiche-organisation/?organisation=531006237 | other:hatvp | 2026-03-31 | ELNET France lobbying status and travel activity | HATVP records ELNET France interest representation as conducted on its own account; its 2023 activity explicitly reports Renaissance then LR parliamentary delegations to Israel and high-level political meetings. | -
FCT-015 | FACT | ✧ | https://www.hatvp.fr/fiche-organisation/?organisation=531006237 | other:hatvp | 2026-03-31 | ELNET declared influence methods | ELNET France declares activities including meetings, events, correspondence and, in some periods, transmission of suggestions intended to influence the drafting of public decisions. | -
FCT-016 | FACT | ✧ | https://elnetwork.fr/communique/droit-de-reponse-delnet-a-mediapart/ | other:elnet | 2025-12-01 | ELNET voluntary-participation counterclaim | ELNET states in a right of reply that parliamentary delegations are voluntary and that no quid pro quo or political support is expected; this is an interested-party counterclaim, not independent proof of absence of influence. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-003
FCT-004 | SRC-004
FCT-005 | SRC-005
FCT-006 | SRC-006
FCT-007 | SRC-006
FCT-008 | SRC-006
FCT-009 | SRC-006
FCT-010 | SRC-008
FCT-011 | SRC-011
FCT-012 | SRC-009
FCT-013 | SRC-010
FCT-014 | SRC-012
FCT-015 | SRC-012
FCT-016 | SRC-013

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
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:Lock scope and execute fresh source retrieval
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:Search exposure, policy-footprint, self-selection and causal-effect axes
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:Normalize facts and build causal/effect claims
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:Test travel exposure, self-selection, policy-footprint and causal effect
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:Verify claims, controls and effect ceiling
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:Build accountability, impact, contradictions and final narrative
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:Freeze technical narrative and run final gates

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-13T10:24:58.684320+00:00","fact_mem":{},"mnemo_row":"MNEMO_UNAVAILABLE — local memory service unavailable in this runtime; no memory ids fabricated.","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":16,"eligible":16,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_UNAVAILABLE — local memory service unavailable in this runtime; no memory ids fabricated. | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:16;attempted:0;success:0;failure:0;blocked:16} | WRITEBACK_EXECUTION_V1:[16 rows, see section]

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
