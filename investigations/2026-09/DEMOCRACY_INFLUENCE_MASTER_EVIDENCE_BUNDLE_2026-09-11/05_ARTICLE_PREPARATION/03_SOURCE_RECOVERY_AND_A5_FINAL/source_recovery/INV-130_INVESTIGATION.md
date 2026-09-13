ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260910-1722-morocco-influence-france | PARENT_RUN_ID:NONE | AS_OF:2026-09-10
INPUT_KIND:RUN_CARD | MISSION_MODE:GREENFIELD | INPUT_REF:PATH:/mnt/data/inv130/runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-10_morocco-influence-france/2026-09-10_17-22_morocco-influence-france_INPUT.md | SUBJECT_SLUG:morocco-influence-france | SUBJECT_FP:sha256:512b1467792a36e57431a2dbf98bb060d19038b60c391665fe787b62c25ece04 | INPUT_SHA256:sha256:a4b4969c91c9b202701566c7b304f3cdca1d822a9337a9373e20481b84451cc3
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France, principalement 2010-2026; cas marocains séparés par mécanisme; influence déclarée, diplomatie parlementaire, culte/diaspora, surveillance et corruption présumée; effet politique uniquement si chaîne fermée.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/NETWORK.md,clusters/MONEY.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Corps analytique technique — INV-130

## Résultat central
Les mécanismes marocains observés en France ne forment pas une chaîne unique. Les arêtes les plus solides sont : influence institutionnelle sur certains éléments du culte musulman via recrutement, financement, formation ou désignation de personnels ; diplomatie parlementaire ouverte et répétée autour du Sahara occidental, suivie d’un alignement officiel français mais sans causalité marginale isolée ; ciblage Pegasus de responsables français avec attribution technique/investigative forte, sans effet politique aval démontré. Moroccogate fournit un comparateur corruption/tasking matériel mais sa responsabilité finale et son effet de décision restent non fermés dans le corpus inspecté.

## Plafond causal
Aucune chaîne générale ne permet de conclure `Maroc -> diaspora française -> comportement politique/électoral`, `advocacy -> décision présidentielle causée`, `Pegasus -> changement de politique`, ni `Moroccogate -> décision UE causée` à partir des pièces inspectées. Les voies ouvertes, transparentes ou coopératives doivent rester distinctes des opérations clandestines.

## Contrôle de symétrie
Le cas marocain est particulièrement utile pour INV-131 et INV-147 parce qu’il contient, sous un même pays émetteur, des mécanismes de nature différente : influence étrangère légale, coopération institutionnelle, advocacy parlementaire, influence diasporique/religieuse, surveillance clandestine et corruption alléguée. Le label doit suivre les propriétés de chaque mécanisme et son niveau de preuve, non la nationalité seule.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:6|SRC_COMPLETE:10/10

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-10
- **breaks:**
  - 2016 Senate/Interior worship-governance baseline
  - 2021 Pegasus public investigation
  - 2023-2024 parliamentary diplomacy and French Sahara shift
  - 2024 foreign-influence legal framework
  - 2026 strengthened Pegasus technical evidence
- **status:** CURRENT
- **window:** 2010-2026; older 2016 institutional material retained because it remains causal background for current religious-influence architecture

### MANIPULATION_REPORT
- **assumptions:**
  - official parliamentary records establish declared advocacy/institutional findings only
  - investigative journalism can strengthen attribution but not substitute for final judicial responsibility
- **clusters:**
  - POWER
  - NETWORK
  - MONEY
- **complexity:**
  - **band:** HIGH
  - **score:** 9
- **implicit:**
  - **I01:** foreign origin does not determine classification
  - **I02:** access does not determine adoption
  - **I03:** information acquisition does not determine political effect
- **input_kind:** RUN_CARD
- **mission_mode:** GREENFIELD
- **patterns:**
  - **P01:** open institutional influence
  - **P02:** resource/intermediary chain
  - **P03:** advocacy before policy alignment
  - **P04:** covert surveillance attribution
  - **P05:** alleged corruption/tasking with responsibility gap
- **priorities:**
  - separate mechanisms
  - trace state/intermediary/action/target/effect
  - test tasking and causal endpoints
  - preserve legal/normal-diplomacy controls
  - produce Algeria and ally/adversary symmetry value
- **query_guidance:** prefer official French records; use investigative reporting for covert operations with explicit attribution ceilings
- **rhetorical:**
  - **R01:** country bundle can create false single-system inference
  - **R02:** temporal sequence can be mistaken for causality
  - **R03:** diaspora language can imply proxy status without tasking
- **speaker:**
  - **goal:** bounded mechanism-first Morocco influence investigation
  - **target:** actor -> intermediary/resource/tasking -> action -> French target -> exposure/decision/effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** Moroccan state/public actor
  - **S02:** French intermediary
  - **S03:** diaspora/religious institution
  - **S04:** parliamentary friendship group
  - **S05:** executive
  - **S06:** resource/payment
  - **S07:** training/designation
  - **S08:** advocacy
  - **S09:** surveillance
  - **S10:** corruption allegation
  - **S11:** access/exposure
  - **S12:** information acquisition
  - **S13:** policy decision
  - **S14:** tasking/control
  - **S15:** political/electoral effect
- **threats:**
  - nationality=state link
  - cooperation=control
  - diaspora=relay
  - investment=influence
  - surveillance=policy effect
  - allegation=proved tasking
  - advocacy=causality

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - internal presidential decision footprint
  - **input_ids:**
    - FCT-011
    - FCT-012
    - FCT-013
    - FCT-014
    - FCT-015
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no marginal causal attribution to friendship group
  - **not_computable:**
    - counterfactual policy outcome without advocacy
  - **operations_applied:**
    - mapped friendship-group advocacy to policy endpoint
    - tested causal alternatives
  - **reason:** separate advocacy/access from adoption and causality
  - **result_ids:**
    - CLM-004
    - CLM-005
    - CAU-002
  - **status:** DONE
  - **trigger:** state, parliamentary and executive influence channels
- **item 2:**
  - **gaps:**
    - authenticated political instruction/action chain
  - **input_ids:**
    - FCT-003
    - FCT-004
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-008
    - FCT-010
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no general diaspora political tasking chain
  - **not_computable:**
    - general electoral effect on French Moroccan-origin population
  - **operations_applied:**
    - mapped personnel/training/governance levers
    - tested diaspora-proxy inference
  - **reason:** separate institutional linkage from political relay/tasking
  - **result_ids:**
    - CLM-002
    - CLM-003
    - CAU-001
  - **status:** DONE
  - **trigger:** diaspora/religious structures and intermediary relations
- **item 3:**
  - **gaps:**
    - final judicial/tasking/decision records
  - **input_ids:**
    - FCT-009
    - FCT-018
    - FCT-019
  - **module:** clusters/MONEY.md
  - **negative_results:**
    - no final public proof in inspected sources of complete DGED payment/tasking -> caused decision chain
  - **not_computable:**
    - policy effect attributable to alleged payment alone
  - **operations_applied:**
    - mapped alleged resource/intermediary chain
    - retained evidentiary caveat
  - **reason:** separate payment allegation, intermediary, tasking and policy effect
  - **result_ids:**
    - CLM-007
    - CAU-004
  - **status:** DONE
  - **trigger:** Moroccogate payment/corruption allegations

### SCOPING_REPORT
- **exclusions:**
  - nationality=state link
  - diaspora=relay
  - cooperation=control
  - advocacy=causal effect
  - investigative allegation=judicial finding
- **geo:** France; EU only as bounded Moroccogate comparator
- **object_coverage:** HIGH_FOR_WORSHIP_INSTITUTIONAL_CHANNELS_AND_PARLIAMENTARY_ADVOCACY; MODERATE_FOR_PEGASUS_ATTRIBUTION; PARTIAL_FOR_CORRUPTION_TASKING; LOW_FOR_DOWNSTREAM_CAUSAL_EFFECT
- **object_question:** Quels cas marocains en France ferment une chaîne acteur/intermédiaire/action/cible/effet, et lesquels relèvent de diplomatie, coopération, commerce ou diaspora ordinaires ?
- **period:** 2010-2026
- **subject:** Moroccan influence mechanisms in France

### CREDO
- nationality != state link
- cooperation != control
- diaspora != relay
- investment != influence
- intelligence activity != political effect
- proximity != tasking
- advocacy != causality
- allegation != proof
- foreign influence != interference by default

### COGNITIVE_MAP
- **continuum:**
  - foreign principal/resource
  - intermediary or institution
  - declared/open or covert action
  - French target/venue
  - access/exposure/information acquisition
  - institutional or policy response
  - behavior/decision
  - counterfactual effect
- **core_model:** Moroccan influence in France is not one mechanism. The strongest closed channels are exercised institutional influence over parts of religious organization and open parliamentary diplomacy/advocacy; Pegasus supplies a harder covert surveillance case with strong public technical attribution but no closed policy-effect edge. Moroccogate remains a bounded corruption/tasking comparator with unresolved final responsibility/causality.
- **rival_models:**
  - ordinary bilateral diplomacy/cooperation
  - diaspora governance without French political relay
  - pluralist parliamentary advocacy contributing alongside rival causes
  - covert intelligence gathering without demonstrated policy influence
  - state-directed corruption/tasking causing favorable decisions

### DIALECTICAL_MAP
- **antithesis:** Many observed relations are lawful diplomacy/cooperation or institutional links; national origin, access and temporal policy alignment do not prove tasking or causal control.
- **synthesis:** Mechanism-specific influence is established in several channels, but no evidence supports collapsing them into a single coordinated Moroccan command architecture or a general measurable electoral effect in France.
- **thesis:** Moroccan state-linked actors use several observable channels to seek or exercise influence touching French institutions, religious infrastructure and policy debates.

### RESOURCE_FLOW_MAP
- **flows:**
  - state/bilateral arrangements -> imam recruitment/training -> French religious infrastructure
  - Moroccan parliamentary counterpart/contact -> French friendship-group diplomacy -> public advocacy
  - Morocco-linked Pegasus infrastructure -> targeting of French officials -> potential information access
  - alleged Morocco-linked funds/intermediaries -> EU political actors (Moroccogate, unresolved final responsibility)
- **limits:**
  - religious influence != political proxy
  - parliamentary advocacy != causal adoption
  - surveillance != policy change
  - payment allegation != authenticated tasking

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** Moroccan state/bilateral structures
  - **relation:** recruitment, financing, training/designation channels
  - **support:**
    - FCT-003
    - FCT-004
    - FCT-006
    - FCT-010
  - **to:** parts of Muslim worship infrastructure in France
- **item 2:**
  - **from:** Moroccan parliamentary counterparts
  - **relation:** invitation/collaboration
  - **support:**
    - FCT-011
    - FCT-012
  - **to:** French Senate France-Morocco friendship group
- **item 3:**
  - **from:** French Senate friendship group / Senate president
  - **relation:** public advocacy
  - **support:**
    - FCT-012
    - FCT-013
  - **to:** French executive policy debate on Western Sahara
- **item 4:**
  - **from:** French executive
  - **relation:** adopted/implemented position
  - **support:**
    - FCT-014
    - FCT-015
  - **to:** Western Sahara policy
- **item 5:**
  - **from:** Morocco-linked Pegasus client
  - **relation:** technical targeting infrastructure
  - **support:**
    - FCT-016
    - FCT-017
  - **to:** French president/government officials
- **item 6:**
  - **from:** Atmoun / alleged DGED-linked network
  - **relation:** alleged payment/tasking intermediary
  - **support:**
    - FCT-018
    - FCT-019
  - **to:** Panzeri/Fight Impunity/EU actors

### IMPACT_MAP
- **established:**
  - foreign influence is legally separable from interference
  - Moroccan influence over parts of worship organization/personnel in France
  - open France-Morocco parliamentary advocacy before 2024 policy shift
  - French 2024 Western Sahara policy endpoint and implementation
  - strong public technical/investigative Pegasus targeting linkage
- **not_established:**
  - general Moroccan political control of diaspora in France
  - general electoral effect
  - single coordinated Morocco influence architecture across channels
  - Pegasus-caused French policy change
  - final public proof in inspected corpus of Moroccogate DGED tasking causing a decision
- **partial:**
  - friendship-group advocacy contribution to policy decision
  - Moroccogate payment/tasking responsibility chain

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** HATVP explicitly recognizes legitimate foreign influence and separately frames interference risk
  - **issue:** foreign influence equals interference
  - **pro:** foreign principals can seek to influence French public policy
  - **resolution:** MECHANISM_PROPERTIES_REQUIRED
  - **support:**
    - FCT-001
    - FCT-002
- **item 2:**
  - **contra:** no general political tasking/electoral relay chain and Senate records explicit negative controls in adjacent campus case
  - **issue:** diaspora/religious influence equals political proxy
  - **pro:** state-linked levers over imams/training/governance are documented
  - **resolution:** RELIGIOUS_INSTITUTIONAL_INFLUENCE_SUPPORTED_POLITICAL_PROXY_NOT_ESTABLISHED
  - **support:**
    - FCT-003
    - FCT-004
    - FCT-005
    - FCT-008
- **item 3:**
  - **contra:** no internal decision footprint isolates marginal effect and other strategic/bilateral causes remain plausible
  - **issue:** advocacy caused French Sahara shift
  - **pro:** friendship group repeatedly requested same outcome before presidential adoption
  - **resolution:** SEQUENCE_SUPPORTED_CAUSAL_CONTRIBUTION_UNRESOLVED
  - **support:**
    - FCT-011
    - FCT-012
    - FCT-013
    - FCT-014
    - FCT-015
- **item 4:**
  - **contra:** information acquisition is not a demonstrated changed policy
  - **issue:** Pegasus proves policy influence
  - **pro:** technical/investigative targeting of French officials is strongly supported
  - **resolution:** SURVEILLANCE_SUPPORTED_DOWNSTREAM_EFFECT_UNRESOLVED
  - **support:**
    - FCT-016
    - FCT-017
    - FCT-020
- **item 5:**
  - **contra:** same public reporting says older records do not certify agent/payment status
  - **issue:** Moroccogate proves intelligence tasking
  - **pro:** investigator allegations describe money/intermediaries and DGED links
  - **resolution:** ALLEGATION_MATERIAL_FINAL_RESPONSIBILITY_UNRESOLVED
  - **support:**
    - FCT-009
    - FCT-018
    - FCT-019

### VERIFICATION_REPORT
- **downgraded:**
  - foreign relation -> interference
  - diaspora structure -> political proxy
  - advocacy -> caused policy
  - surveillance -> policy effect
  - allegation -> final intelligence tasking
- **fact_count:** 20
- **negative_controls:**
  - French law recognizes legitimate foreign influence
  - no campus-protest foreign-power link established in cited Senate report
  - no general diaspora political tasking chain found
  - no causal friendship-group -> presidential-decision isolation
  - 2021 French government did not prejudge Pegasus attribution while investigation ongoing
  - Moroccogate public reporting preserves payment/agent uncertainty
- **provenance_families:** 5
- **query_count:** 20
- **source_count:** 10
- **verification:** 20 bounded facts linked to 10 inspected sources; official French institutional sources dominate open/diaspora/legal channels, investigative reporting is used for covert-operation attribution with explicit responsibility ceilings.

### EDI_REPORT
- **corpus:**
  - **limits:**
    - no internal Moroccan tasking files for most open channels
    - no presidential decision causality file
    - no electoral-effect denominator
    - Moroccogate final judicial responsibility not closed in inspected sources
  - **strength:** multiple independent institutional records and explicit negative controls
- **decisive_claim_coverage:**
  - CLM-001
  - CLM-002
  - CLM-004
  - CLM-005
  - CLM-006
  - CLM-007
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** Moroccan public/para-public actors, French intermediaries/institutions, covert operators/alleged intermediaries
  - **perspective:** law, diplomacy, religion/diaspora, surveillance, corruption, policy effect
  - **stratification:** resource/relation -> action -> target -> access/exposure/information -> decision/effect
  - **temporal:** 2010-2026
- **edi:**
  - **coverage:** HIGH_MECHANISM_BREADTH_WITH_BOUNDED_CASES; LOW_GENERAL_EFFECT_DENOMINATORS
  - **independence:** OFFICIAL_FRENCH_RECORDS_PLUS_INDEPENDENT_INVESTIGATIVE_TECHNICAL_REPORTING
- **source_counts:**
  - **A:** 1
  - **B:** 5
  - **C:** 1
  - **D:** 2
  - **E:** 1
  - **total:** 10

### RESPONSIBILITY_MAP
- **French_executive:** owns final 2024 Western Sahara position; upstream marginal causal contribution unresolved
- **French_parliamentary_actors:** independently own their public advocacy; collaboration/invitation does not erase agency
- **Moroccan_state:** documented responsibility varies by mechanism: formal/bilateral religious channels supported; Pegasus strong public technical attribution; Moroccogate intelligence tasking not closed here
- **diaspora_and_religious_actors:** must not be treated as state proxies without case-specific instruction/control
- **investigative_sources:** support covert-attribution claims but do not substitute for final judicial findings

### NEXT_QUERIES
- INV-131: apply the same mechanism grid to Algeria in France, especially religious institutional channels, political/diplomatic advocacy, intelligence/security and diaspora controls.
- INV-147: pair Morocco cases with ally/adversary/domestic isomorphs at matched evidence levels to test label and consequence asymmetry.
- If a future authenticated French executive decision record exposes inputs to the 2024 Western Sahara shift, reopen only the advocacy -> policy causal edge.
- If final public judicial records close Moroccogate Morocco/DGED tasking and specific favorable decisions, update responsibility/causal classification rather than rerun generic Morocco coverage.

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-011 | support:FCT-001,FCT-002 | counter:- | results:FCT-001,FCT-002 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-002,QRY-003,QRY-004,QRY-012,QRY-017 | support:FCT-003,FCT-004,FCT-006,FCT-008,FCT-010 | counter:- | results:FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-010 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-005,QRY-006,QRY-007,QRY-013,QRY-016 | support:FCT-011,FCT-012,FCT-013,FCT-014,FCT-015 | counter:- | results:FCT-011,FCT-012,FCT-013,FCT-014,FCT-015 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-008,QRY-015 | support:FCT-016,FCT-017,FCT-020 | counter:- | results:FCT-016,FCT-017,FCT-020 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-009,QRY-014 | support:FCT-009,FCT-018,FCT-019 | counter:- | results:FCT-009,FCT-018,FCT-019 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,SRC-001 | support:FCT-001,FCT-002 | counter:CTRL-001 | results:FCT-001,FCT-002,CTRL-001 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-002,QRY-003,SRC-002,SRC-003 | support:FCT-003,FCT-004,FCT-006,FCT-007 | counter:CTRL-002 | results:FCT-003,FCT-004,FCT-006,FCT-007,CTRL-002 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-002,QRY-003,SRC-002,SRC-003 | support:FCT-005,FCT-008 | counter:- | results:FCT-005,FCT-008 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-004 | attempts:QRY-005,QRY-006,QRY-007,SRC-005,SRC-006,SRC-007 | support:FCT-011,FCT-012,FCT-013,FCT-014,FCT-015 | counter:CTRL-003 | results:FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,CTRL-003 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-005,QRY-006,QRY-007,SRC-005,SRC-006,SRC-007 | support:FCT-011,FCT-012,FCT-013,FCT-014,FCT-015 | counter:CTRL-003 | results:FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,CTRL-003 | final:PARTIAL | gap:CAUSALITY
CLM-006 | attempts:QRY-008,QRY-010,SRC-008,SRC-010 | support:FCT-016,FCT-017,FCT-020 | counter:CTRL-004 | results:FCT-016,FCT-017,FCT-020,CTRL-004 | final:SUPPORTED | gap:CAUSALITY
CLM-007 | attempts:QRY-003,QRY-009,SRC-003,SRC-009 | support:FCT-009,FCT-018,FCT-019 | counter:CTRL-005 | results:FCT-009,FCT-018,FCT-019,CTRL-005 | final:PARTIAL | gap:RESPONSIBILITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-003 | CLM | SUPPORTED | RESPONSIBILITY | No authenticated Morocco-state -> French diaspora organization -> political instruction/action chain was identified in the bounded searches.
CLM-005 | CLM | PARTIAL | CAUSALITY | Temporal sequence and policy alignment are documented, but the inspected corpus does not isolate the friendship group from executive, strategic, commercial, regional-security and bilateral-normalization causes.
CLM-006 | CLM | SUPPORTED | CAUSALITY | Information acquisition/targeting is documented at a stronger level than any downstream French decision caused by it.
CLM-007 | CLM | PARTIAL | RESPONSIBILITY | Investigators’ allegations and relationships are public, but the inspected sources explicitly preserve uncertainty on intelligence payment/agent status and do not close a final causal EU policy effect.
CAU-002 | CAU | UNRESOLVED | CAUSALITY | No internal decision record or counterfactual isolates friendship-group advocacy from rival causes.
CAU-003 | CAU | UNRESOLVED | CAUSALITY | No inspected footprint links acquired information to a changed French policy or behavior.
CAU-004 | CAU | UNRESOLVED | RESPONSIBILITY | No final public source inspected here closes both authenticated DGED tasking/payment and a caused policy decision.

SEMANTIC_COUNTS_V1:LED:0|CLM:7|AXS:5|CAU:4|CTRL:5|ACT:2

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"French law explicitly distinguishes legitimate foreign influence from foreign interference and regulates specified influence activities through transparency rather than treating foreign origin itself as interference.","claimant":"INV-130","counter":"CTRL-001","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002"]}
CLM-002 | {"claim":"Moroccan state-linked influence over parts of Muslim-worship organization in France is documented through personnel, training and institutional channels.","claimant":"INV-130","counter":"CTRL-002","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-003","FCT-004","FCT-006","FCT-007"]}
CLM-003 | {"claim":"The inspected evidence does not establish that French citizens of Moroccan origin or French Muslim organizations generally act as Moroccan political relays or follow Moroccan electoral tasking.","claimant":"INV-130","counter":"NONE_FOUND","gap":"No authenticated Morocco-state -> French diaspora organization -> political instruction/action chain was identified in the bounded searches.","gap_type":"RESPONSIBILITY","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-005","FCT-008"]}
CLM-004 | {"claim":"France-Morocco parliamentary friendship structures openly advocated a stronger French Western Sahara position before France adopted and implemented that position.","claimant":"INV-130","counter":"CTRL-003","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-011","FCT-012","FCT-013","FCT-014","FCT-015"]}
CLM-005 | {"claim":"The friendship-group advocacy is a proven marginal cause of the French 2024 Western Sahara policy shift.","claimant":"INV-130","counter":"CTRL-003","gap":"Temporal sequence and policy alignment are documented, but the inspected corpus does not isolate the friendship group from executive, strategic, commercial, regional-security and bilateral-normalization causes.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-011","FCT-012","FCT-013","FCT-014","FCT-015"]}
CLM-006 | {"claim":"Pegasus provides strong public technical/investigative evidence of a Morocco-linked covert surveillance operation against French officials, but the inspected material does not close a downstream policy or electoral effect.","claimant":"INV-130","counter":"CTRL-004","gap":"Information acquisition/targeting is documented at a stronger level than any downstream French decision caused by it.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-016","FCT-017","FCT-020"]}
CLM-007 | {"claim":"Moroccogate closes a final proven Morocco-DGED payment/tasking chain causing favorable EU decisions.","claimant":"INV-130","counter":"CTRL-005","gap":"Investigators’ allegations and relationships are public, but the inspected sources explicitly preserve uncertainty on intelligence payment/agent status and do not close a final causal EU policy effect.","gap_type":"RESPONSIBILITY","materiality":"IMPORTANT","status":"PARTIAL","support":["FCT-009","FCT-018","FCT-019"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-011"],"axis":"Legal/transparent foreign influence boundary","links":["INV-130","INV-147"],"question":"How does French law separate declared foreign influence from interference, and what does that imply for Moroccan activity?","result_ids":["FCT-001","FCT-002"],"sought_objects":["legal definition","disclosure duties","covered activities","interference boundary"],"status":"SATURATED","support":["FCT-001","FCT-002"]}
AXS-002 | {"attempt_ids":["QRY-002","QRY-003","QRY-004","QRY-012","QRY-017"],"axis":"Religious/diaspora institutional influence","links":["INV-130","INV-131","INV-038"],"question":"Which Moroccan state-linked levers over worship organization and religious personnel in France are documented, and do they close political tasking or electoral effects?","result_ids":["FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-010"],"sought_objects":["imam financing/designation","training","worship governance","political relay evidence"],"status":"SATURATED","support":["FCT-003","FCT-004","FCT-006","FCT-008","FCT-010"]}
AXS-003 | {"attempt_ids":["QRY-005","QRY-006","QRY-007","QRY-013","QRY-016"],"axis":"Parliamentary diplomacy and Western Sahara policy","links":["INV-130","INV-147"],"question":"Can Moroccan-linked parliamentary diplomacy be traced to an identifiable French policy shift, and is its causal contribution isolable?","result_ids":["FCT-011","FCT-012","FCT-013","FCT-014","FCT-015"],"sought_objects":["invitation/contact","advocacy","policy endpoint","rival causes","decision footprint"],"status":"SATURATED","support":["FCT-011","FCT-012","FCT-013","FCT-014","FCT-015"]}
AXS-004 | {"attempt_ids":["QRY-008","QRY-015"],"axis":"Covert surveillance / intelligence operation","links":["INV-130","INV-147"],"question":"What can be attributed in the Pegasus targeting of French officials, and what downstream political influence effect is demonstrated?","result_ids":["FCT-016","FCT-017","FCT-020"],"sought_objects":["technical attribution","state responsibility","targets","information access","policy effect"],"status":"SATURATED","support":["FCT-016","FCT-017","FCT-020"]}
AXS-005 | {"attempt_ids":["QRY-009","QRY-014"],"axis":"Corruption/tasking comparator","links":["INV-130","INV-038","INV-147"],"question":"Does Moroccogate close a Morocco -> intermediary -> payment/tasking -> favorable-position chain, and which links remain allegations?","result_ids":["FCT-009","FCT-018","FCT-019"],"sought_objects":["payment","intermediary","intelligence tasking","favorable action","judicial outcome"],"status":"SATURATED","support":["FCT-009","FCT-018","FCT-019"]}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"Personnel/training/governance levers materially alter who supplies and forms religious personnel and therefore constitute an exercised institutional influence channel.","counter":"CTRL-002","limit":"Closes influence over parts of religious infrastructure; does not close political/electoral tasking of diaspora.","mechanism":"Moroccan state/agreements -> imam recruitment, financing or training -> religious personnel/institutional presence in France","status":"SUPPORTED","support":["FCT-003","FCT-004","FCT-006","FCT-010"]}
CAU-002 | {"counter":"CTRL-003","gap":"No internal decision record or counterfactual isolates friendship-group advocacy from rival causes.","gap_type":"CAUSALITY","limit":"Sequence and alignment are supported; marginal causal contribution to presidential decision remains unresolved.","mechanism":"Moroccan parliamentary counterpart/contact -> France-Morocco friendship-group diplomacy -> repeated advocacy -> French Western Sahara policy alignment/implementation","status":"UNRESOLVED","support":["FCT-011","FCT-012","FCT-013","FCT-014","FCT-015"]}
CAU-003 | {"counter":"CTRL-004","gap":"No inspected footprint links acquired information to a changed French policy or behavior.","gap_type":"CAUSALITY","limit":"Targeting/technical linkage is stronger than demonstrated downstream leverage or decision change.","mechanism":"Morocco-linked Pegasus client -> targeting/infection infrastructure -> French officials -> potential intelligence access -> political leverage/effect","status":"UNRESOLVED","support":["FCT-016","FCT-017","FCT-020"]}
CAU-004 | {"counter":"CTRL-005","gap":"No final public source inspected here closes both authenticated DGED tasking/payment and a caused policy decision.","gap_type":"RESPONSIBILITY","limit":"Public allegations and contact/payment pathway are incomplete for final responsibility and policy causality.","mechanism":"Moroccan state/intelligence-linked actors -> intermediary/payment/tasking -> EU political actor -> favorable position/decision","status":"UNRESOLVED","support":["FCT-009","FCT-018","FCT-019"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Foreign origin or representation of a foreign principal is not itself interference; French law explicitly recognizes legitimate foreign influence and regulates transparency.","status":"DONE","support":["FCT-001","FCT-002"]}
CTRL-002 | {"control":"Influence over worship organization or imam training does not establish that diaspora members are political proxies, coordinated voters or state-tasked relays.","status":"DONE","support":["FCT-005","FCT-008"]}
CTRL-003 | {"control":"Repeated advocacy followed by a matching policy endpoint does not prove that the advocacy caused the decision; rival executive, strategic and bilateral explanations remain live.","status":"DONE","support":["FCT-011","FCT-012","FCT-013","FCT-014","FCT-015"]}
CTRL-004 | {"control":"Pegasus targeting/technical attribution establishes a covert surveillance channel more strongly than downstream political influence; espionage != changed policy.","status":"DONE","support":["FCT-016","FCT-017","FCT-020"]}
CTRL-005 | {"control":"Moroccogate allegations are material but allegations/investigative suspicions != final proof of DGED tasking, agent status or caused EU decision.","status":"DONE","support":["FCT-009","FCT-018","FCT-019"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Route Morocco as an actor-specific symmetry case with separate transparent, institutional, covert-surveillance and alleged-corruption mechanisms; do not collapse them into one national influence system.","actor":"INV-130 control plane","intent":"Preserve mechanism-first classification and avoid country-level guilt by association.","status":"DONE","support":["CLM-001","CLM-002","CLM-004","CLM-006","CLM-007"]}
ACT-002 | {"action":"Send bounded Morocco edges to INV-038 and symmetry/qualification controls to INV-147; prioritize INV-131 as the paired Algeria case only if reclassification ranking selects it.","actor":"INV-130 control plane","intent":"Use the result as a discriminating comparator rather than force dependency closure.","status":"DONE","support":["CLM-002","CLM-003","CLM-004","CLM-005","CAU-001","CAU-002"]}

SEARCH_ACTIVITY_V1:WEB:10|FETCH:10|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | MNEMO_UNAVAILABLE | mnemolite | NONE | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.hatvp.fr/la-haute-autorite/lencadrement-de-linfluence-etrangere/le-repertoire-de-linfluence-etrangere/ | FETCH HATVP-FOREIGN-INFLUENCE-2026
QRY-002 | FETCH | FOUND | SRC-002 | https://www.senat.fr/rap/r15-757/r15-7575.html | FETCH SENAT-ISLAM-FRANCE-2016
QRY-003 | FETCH | FOUND | SRC-003 | https://www.senat.fr/rap/r23-739-1/r23-739-1_mono.html | FETCH SENAT-INFLUENCES-2024
QRY-004 | FETCH | FOUND | SRC-004 | https://www.interieur.gouv.fr/fr/Archives/Archives-ministres-de-l-Interieur/Archives-Bernard-Cazeneuve-avril-2014-decembre-2016/Interventions-du-ministre/Journee-de-travaux-et-d-echanges-autour-de-l-Islam-de-France | FETCH INTERIEUR-ISLAM-FRANCE-2016
QRY-005 | FETCH | FOUND | SRC-005 | https://www.senat.fr/salle-de-presse/communiques-de-presse/presse/31-05-2023/senateurs-francais-et-marocains-reunis-pour-lancer-un-appel-au-rechauffement-des-relations-entre-rabat-et-paris.html | FETCH SENAT-FR-MA-2023
QRY-006 | FETCH | FOUND | SRC-006 | https://www.senat.fr/salle-de-presse/communiques-de-presse/presse/30-07-2024/sahara-occidental-le-groupe-damitie-france-maroc-du-senat-se-rejouit-du-soutien-de-la-france-au-plan-marocain-dautonomie.html | FETCH SENAT-SAHARA-2024
QRY-007 | FETCH | FOUND | SRC-007 | https://www.elysee.fr/emmanuel-macron/2024/10/29/visite-detat-au-maroc-deuxieme-journee | FETCH ELYSEE-MAROC-2024
QRY-008 | FETCH | FOUND | SRC-008 | https://www.lemonde.fr/pixels/article/2026/07/16/de-nouvelles-preuves-demontrent-que-le-maroc-a-utilise-le-logiciel-espion-pegasus_6723736_4408996.html | FETCH LEMONDE-PEGASUS-MOROCCO-2026
QRY-009 | FETCH | FOUND | SRC-009 | https://www.lemonde.fr/international/article/2022/12/17/corruption-au-parlement-europeen-un-mysterieux-espion-marocain-au-c-ur-de-l-enquete_6154798_3210.html | FETCH LEMONDE-MOROCCOGATE-2022
QRY-010 | FETCH | FOUND | SRC-010 | https://www.senat.fr/questions/base/2021/qSEQ210723934.html | FETCH SENAT-PEGASUS-RESPONSE-2021
QRY-011 | WEB | FOUND | - | - | Morocco influence France HATVP foreign influence registry
QRY-012 | WEB | FOUND | - | - | Morocco France Senate diaspora imams influence report
QRY-013 | WEB | FOUND | - | - | Morocco France parliamentary friendship Sahara autonomy lobbying policy shift
QRY-014 | WEB | FOUND | - | - | Morocco Pegasus Macron France ANSSI attribution
QRY-015 | WEB | FOUND | - | - | Moroccogate Morocco DGED Panzeri evidence tasking
QRY-016 | WEB | FOUND | - | - | Morocco France policy shift Western Sahara alternative causes strategic business Sahel
QRY-017 | WEB | NO_DECISIVE_CHAIN | - | - | Moroccan diaspora France electoral political mobilization state tasking evidence
QRY-018 | WEB | NO_DECISIVE_CHAIN | - | - | Morocco investment France specific policy decision causal influence
QRY-019 | WEB | NO_DECISIVE_CHAIN | - | - | Morocco security cooperation France tasking political influence evidence
QRY-020 | WEB | NO_DECISIVE_EFFECT | - | - | Morocco France influence causal electoral effect evidence

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | HATVP-FOREIGN-INFLUENCE-2026 | Le répertoire de l’influence étrangère | 2026-09-10 | 2026-09-10T15:25:00Z | lines 96-146: legal distinction influence/ingérence, covered actors/activities, disclosure/control | https://www.hatvp.fr/la-haute-autorite/lencadrement-de-linfluence-etrangere/le-repertoire-de-linfluence-etrangere/
SRC-002 | ◈ | fam:B | SENAT-ISLAM-FRANCE-2016 | De l Islam en France à un Islam de France | 2016-07-05 | 2026-09-10T15:25:00Z | lines 318-329: six levers of Algeria/Morocco/Turkey influence on worship; imam recruitment/training | https://www.senat.fr/rap/r15-757/r15-7575.html
SRC-003 | ◈ | fam:B | SENAT-INFLUENCES-2024 | Lutte contre les influences étrangères malveillantes | 2024-07-23 | 2026-09-10T15:25:00Z | lines 1242,1262-1278,2324-2328,2645: Morocco cases, controls and limits | https://www.senat.fr/rap/r23-739-1/r23-739-1_mono.html
SRC-004 | ◈ | fam:E | INTERIEUR-ISLAM-FRANCE-2016 | Journée de travaux et d échanges autour de l Islam de France | 2016-08-29 | 2026-09-10T15:25:00Z | lines 91-120: French institutional governance and training response | https://www.interieur.gouv.fr/fr/Archives/Archives-ministres-de-l-Interieur/Archives-Bernard-Cazeneuve-avril-2014-decembre-2016/Interventions-du-ministre/Journee-de-travaux-et-d-echanges-autour-de-l-Islam-de-France
SRC-005 | ◈ | fam:B | SENAT-FR-MA-2023 | Sénateurs français et marocains réunis pour relancer les relations | 2023-05-31 | 2026-09-10T15:25:00Z | friendship group invited to Morocco; explicit support request for autonomy plan | https://www.senat.fr/salle-de-presse/communiques-de-presse/presse/31-05-2023/senateurs-francais-et-marocains-reunis-pour-lancer-un-appel-au-rechauffement-des-relations-entre-rabat-et-paris.html
SRC-006 | ◈ | fam:B | SENAT-SAHARA-2024 | Groupe d amitié France-Maroc et soutien au plan marocain | 2024-07-30 | 2026-09-10T15:25:00Z | lines 84-104: repeated advocacy, cooperation with Moroccan friendship group, subsequent presidential position | https://www.senat.fr/salle-de-presse/communiques-de-presse/presse/30-07-2024/sahara-occidental-le-groupe-damitie-france-maroc-du-senat-se-rejouit-du-soutien-de-la-france-au-plan-marocain-dautonomie.html
SRC-007 | ◈ | fam:C | ELYSEE-MAROC-2024 | Visite d État au Maroc : deuxième journée | 2024-10-29 | 2026-09-10T15:25:00Z | lines 92-94 and 198-200: final French position on Western Sahara and implementation | https://www.elysee.fr/emmanuel-macron/2024/10/29/visite-detat-au-maroc-deuxieme-journee
SRC-008 | ◈ | fam:D | LEMONDE-PEGASUS-MOROCCO-2026 | De nouvelles preuves démontrent que le Maroc a utilisé Pegasus | 2026-07-16 | 2026-09-10T15:25:00Z | lines 337-357: French officials targeted, ANSSI technical linkage, Morocco denial, NSO litigation material | https://www.lemonde.fr/pixels/article/2026/07/16/de-nouvelles-preuves-demontrent-que-le-maroc-a-utilise-le-logiciel-espion-pegasus_6723736_4408996.html
SRC-009 | ◈ | fam:D | LEMONDE-MOROCCOGATE-2022 | Corruption au Parlement européen : piste marocaine | 2022-12-17 | 2026-09-10T15:25:00Z | lines 398-407: investigators allegations, Atmoun/DGED links, explicit evidentiary caveat | https://www.lemonde.fr/international/article/2022/12/17/corruption-au-parlement-europeen-un-mysterieux-espion-marocain-au-c-ur-de-l-enquete_6154798_3210.html
SRC-010 | ◈ | fam:B | SENAT-PEGASUS-RESPONSE-2021 | Relations franco-marocaine - réponse MEAE sur Pegasus | 2021-09-16 | 2026-09-10T15:25:00Z | lines 303-317: reported targeting allegations; government says facts under investigation and if proven extremely serious | https://www.senat.fr/questions/base/2021/qSEQ210723934.html

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.hatvp.fr/la-haute-autorite/lencadrement-de-linfluence-etrangere/le-repertoire-de-linfluence-etrangere/ | A | 2024-07-25 | French legal distinction | French law/HATVP treats foreign influence as a potentially legitimate component of international relations and distinguishes it from foreign interference risk. | -
FCT-002 | FACT | ✧ | https://www.hatvp.fr/la-haute-autorite/lencadrement-de-linfluence-etrangere/le-repertoire-de-linfluence-etrangere/ | A | 2025-10-01 | Foreign influence disclosure threshold | From 1 October 2025, persons acting for a non-EU foreign principal to influence French public policy must register; covered activities include contacts with officials, public communication and certain fund transfers. | -
FCT-003 | FACT | ✧ | https://www.senat.fr/rap/r15-757/r15-7575.html | B | 2016-07-05 | Origin-state influence on worship | The 2016 Senate mission identified Algeria, Morocco and Turkey as exercising influence over organization of Muslim worship in France through six principal levers. | -
FCT-004 | FACT | ✧ | https://www.senat.fr/rap/r15-757/r15-7575.html | B | 2016-07-05 | Moroccan imam channel | The Senate reported that Morocco participates in recruitment/financial support arrangements for foreign imams and in training future French imams at the Mohammed VI Institute in Rabat. | -
FCT-005 | FACT | ✧ | https://www.senat.fr/rap/r15-757/r15-7575.html | B | 2016-07-05 | Religious governance effect boundary | The Senate described Moroccan-current representation in governance/halal/mosque structures, but did not thereby establish a political or electoral relay by French Muslims of Moroccan origin. | -
FCT-006 | FACT | ✧ | https://www.senat.fr/rap/r23-739-1/r23-739-1_mono.html | B | 2024-07-23 | Persistence of Moroccan diaspora influence | The 2024 Senate inquiry states that Moroccan and Turkish strategies are more oriented toward control of diasporas and repeats Moroccan influence through worship organization, training and imam designation. | -
FCT-007 | FACT | ✧ | https://www.senat.fr/rap/r23-739-1/r23-739-1_mono.html | B | 2024-07-23 | DPR persistence report | The 2024 Senate report says the 2022-23 parliamentary intelligence delegation noted persistence of Moroccan activity concerning foreign influence around religious organization. | -
FCT-008 | FACT | ✧ | https://www.senat.fr/rap/r23-739-1/r23-739-1_mono.html | B | 2024-07-23 | University protest negative control | The same Senate inquiry records that no link had been established between recent pro-Palestinian campus movements and identified foreign powers. | -
FCT-009 | FACT | ✧ | https://www.senat.fr/rap/r23-739-1/r23-739-1_mono.html | B | 2024-07-23 | Moroccogate Senate qualification | The Senate describes suspicions that Qatar and Morocco paid actors around the European Parliament for favorable positions, using conditional language rather than a final finding. | -
FCT-010 | FACT | ✧ | https://www.interieur.gouv.fr/fr/Archives/Archives-ministres-de-l-Interieur/Archives-Bernard-Cazeneuve-avril-2014-decembre-2016/Interventions-du-ministre/Journee-de-travaux-et-d-echanges-autour-de-l-Islam-de-France | E | 2016-08-29 | French institutional counter-control | The French Interior Ministry described bilateral arrangements and domestic training/governance reforms intended to reduce dependence on foreign-detached imams and strengthen a France-based framework. | -
FCT-011 | FACT | ✧ | https://www.senat.fr/salle-de-presse/communiques-de-presse/presse/31-05-2023/senateurs-francais-et-marocains-reunis-pour-lancer-un-appel-au-rechauffement-des-relations-entre-rabat-et-paris.html | B | 2023-05-31 | Parliamentary diplomacy request | A French Senate friendship-group delegation, invited by its Moroccan counterpart, publicly called for warmer bilateral relations and for France to go further in supporting Morocco’s Western Sahara autonomy plan. | -
FCT-012 | FACT | ✧ | https://www.senat.fr/salle-de-presse/communiques-de-presse/presse/30-07-2024/sahara-occidental-le-groupe-damitie-france-maroc-du-senat-se-rejouit-du-soutien-de-la-france-au-plan-marocain-dautonomie.html | B | 2024-07-30 | Repeated friendship-group advocacy | After Macron’s July 2024 shift, the Senate France-Morocco friendship group said it had repeatedly requested that position and had long worked through parliamentary diplomacy in close collaboration with the Moroccan counterpart group. | -
FCT-013 | FACT | ✧ | https://www.senat.fr/salle-de-presse/communiques-de-presse/presse/30-07-2024/sahara-occidental-le-groupe-damitie-france-maroc-du-senat-se-rejouit-du-soutien-de-la-france-au-plan-marocain-dautonomie.html | B | 2024-07-30 | Senate-president advocacy | The same Senate communiqué states that Senate President Gérard Larcher had written to the French president in March 2024 advocating a diplomatic initiative in that direction. | -
FCT-014 | FACT | ✧ | https://www.elysee.fr/emmanuel-macron/2024/10/29/visite-detat-au-maroc-deuxieme-journee | C | 2024-10-29 | French Western Sahara position | President Macron publicly stated that for France the present and future of Western Sahara lie within Moroccan sovereignty and that the 2007 autonomy plan is the sole basis for a political solution. | -
FCT-015 | FACT | ✧ | https://www.elysee.fr/emmanuel-macron/2024/10/29/visite-detat-au-maroc-deuxieme-journee | C | 2024-10-29 | Implementation commitment | Macron stated France would implement this position in international institutions, closing a French policy-action endpoint but not the marginal cause of the decision. | -
FCT-016 | FACT | ✧ | https://www.lemonde.fr/pixels/article/2026/07/16/de-nouvelles-preuves-demontrent-que-le-maroc-a-utilise-le-logiciel-espion-pegasus_6723736_4408996.html | D | 2026-07-16 | Pegasus targeting of French officials | Le Monde/Forbidden Stories reported that Pegasus was used to target Emmanuel Macron and members of the French government and that ANSSI analyses linked the same Pegasus client to Moroccan-interest targets. | -
FCT-017 | FACT | ✧ | https://www.lemonde.fr/pixels/article/2026/07/16/de-nouvelles-preuves-demontrent-que-le-maroc-a-utilise-le-logiciel-espion-pegasus_6723736_4408996.html | D | 2026-07-16 | Pegasus attribution ceiling | The 2026 report adds NSO litigation material and technical linkage while recording Morocco’s categorical denial; the inspected public material is strong technical/investigative attribution, not a final French judicial finding of state responsibility. | -
FCT-018 | FACT | ✧ | https://www.lemonde.fr/international/article/2022/12/17/corruption-au-parlement-europeen-un-mysterieux-espion-marocain-au-c-ur-de-l-enquete_6154798_3210.html | D | 2022-12-17 | Moroccogate alleged payment/tasking chain | Le Monde reported Belgian investigators’ allegation that Panzeri/Fight Impunity received Moroccan money through diplomat Abderrahim Atmoun and had links to Morocco’s DGED. | -
FCT-019 | FACT | ✧ | https://www.lemonde.fr/international/article/2022/12/17/corruption-au-parlement-europeen-un-mysterieux-espion-marocain-au-c-ur-de-l-enquete_6154798_3210.html | D | 2022-12-17 | Moroccogate evidentiary caveat | The same report says older confidential Moroccan diplomatic documents do not certify that Panzeri was paid by Moroccan intelligence or was its agent, preserving a responsibility gap. | -
FCT-020 | FACT | ✧ | https://www.senat.fr/questions/base/2021/qSEQ210723934.html | B | 2021-09-16 | French official Pegasus control | In September 2021 the French foreign ministry said reported Pegasus facts would be extremely serious if established, had ordered investigations, and would not prejudge them while ongoing. | -
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
FCT-011 | SRC-005
FCT-012 | SRC-006
FCT-013 | SRC-006
FCT-014 | SRC-007
FCT-015 | SRC-007
FCT-016 | SRC-008
FCT-017 | SRC-008
FCT-018 | SRC-009
FCT-019 | SRC-009
FCT-020 | SRC-010

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

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-10T15:32:28.662864+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":20,"eligible":20,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:20;attempted:0;success:0;failure:0;blocked:20} | WRITEBACK_EXECUTION_V1:[20 rows, see section]

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
