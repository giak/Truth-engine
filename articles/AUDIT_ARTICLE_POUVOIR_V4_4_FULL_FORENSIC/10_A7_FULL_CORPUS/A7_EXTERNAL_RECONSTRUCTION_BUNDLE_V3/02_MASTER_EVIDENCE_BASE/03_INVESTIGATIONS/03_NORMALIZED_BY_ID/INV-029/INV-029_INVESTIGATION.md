ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260911-0051-germany-eu-power | PARENT_RUN_ID:NONE | AS_OF:2026-09-11
INPUT_KIND:RUN_CARD | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/invchain/engine029/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-11_germany-eu-power/2026-09-11_00-51_germany-eu-power_INPUT.md | SUBJECT_SLUG:germany-eu-power | SUBJECT_FP:sha256:b2aafd57c57b72e4f25f8a6cbfabbf267631cb93bddc15c160d4d2f9e61b51ea | INPUT_SHA256:sha256:bb895ca7ed1503e067d8d03c404ed25bdc7b0e1a36188cf992bf27e639818609
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:Union européenne, principalement 2010-2026; trois cas décisionnels bornés: réforme des règles budgétaires 2023-2024, fonds de relance 2020, normes CO2 automobiles/e-fuels 2023. Tracer préférence allemande -> coalition/levier procédural -> décision UE -> delta identifiable, avec contrôles contre poids économique=contrôle.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/NETWORK.md,clusters/MONEY.md,clusters/TEMPORAL.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Corps analytique technique — INV-029

## Résultat central

L'enquête ne soutient pas une thèse de contrôle général de l'Union européenne par l'Allemagne. Elle établit trois mécanismes distincts permettant à Berlin de convertir certaines préférences nationales en résultats européens identifiables : coalition interétatique sur les règles budgétaires, agenda-setting conjoint franco-allemand sur le fonds de relance, et levier procédural de minorité de blocage sur le dossier automobile/e-fuels. Dans chacun des trois cas, le résultat final demeure un compromis institutionnel collectif et ne reproduit pas intégralement la préférence allemande initiale.

## Cas 1 — Règles budgétaires 2023-2024

L'Allemagne demande explicitement des minima numériques communs, dont une baisse annuelle minimale du ratio de dette. Onze ministres des finances cosignent une ligne proche. Le compromis du Conseil puis le texte adopté comportent deux safeguards quantitatifs de dette et de déficit. La correspondance temporelle et substantielle ferme une influence négociée réelle. Elle ne suffit pas à identifier l'Allemagne comme cause marginale unique, puisque les préférences de plusieurs États, la présidence du Conseil et le trilogue participent au résultat.

## Cas 2 — Fonds de relance 2020

Berlin et Paris proposent ensemble un fonds de 500 milliards d'euros. Angela Merkel indique ensuite que la Commission reprend de nombreux éléments de cette initiative. Le Conseil européen adopte finalement un dispositif de 750 milliards, structuré différemment et négocié à 27. Le mécanisme supporté est donc un agenda-setting franco-allemand puissant, non un commandement allemand unilatéral.

## Cas 3 — Normes CO2 automobiles et e-fuels, 2023

Le gouvernement allemand conditionne son soutien final à une voie permettant l'immatriculation après 2035 de véhicules fonctionnant exclusivement avec des carburants neutres en CO2. Le retrait tardif de son soutien, avec d'autres États, contribue à une minorité de blocage et au report du vote. Le texte finalement adopté maintient néanmoins l'objectif de réduction de 100 % des émissions de flotte en 2035 tout en ouvrant une voie réglementaire distincte pour les e-fuels. C'est le cas le plus net de levier procédural allemand produisant une concession bornée sans victoire totale.

## Modèle explicatif

Le meilleur modèle est : `ressources nationales -> préférence -> coalition ou levier procédural -> négociation institutionnelle -> delta de texte/décision`. Le poids économique augmente probablement la capacité de coalition, d'agenda et de crédibilité d'un veto, mais il n'est pas observé comme mécanisme causal autonome dans le corpus. Les catégories restent donc séparées : influence légitime et visible, pouvoir structurel, levier de blocage, coercion et contrôle ne sont pas synonymes.

## Plafond causal

Aucun des trois cas ne ferme `poids économique allemand -> décision européenne` indépendamment des règles de vote, coalitions, préférences alliées et compromis interinstitutionnels. La thèse forte d'une domination allemande systématique reste non établie. Pour la tester, il faudrait un corpus comparatif de dossiers avec préférences ex ante, position des États, règles de vote, concessions versionnées et contre-factuels de coalition.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:4|EDI_DECISIVE:4|SRC_COMPLETE:10/10

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-11
- **breaks:**
  - 2020 Franco-German recovery initiative and EUCO compromise
  - 2023 German fiscal coalition and e-fuels blocking episode
  - 2024 entry into force of reformed fiscal rules
- **status:** CURRENT
- **window:** EU mainly 2010-2026; cases 2020 and 2023-2024

### MANIPULATION_REPORT
- **assumptions:**
  - official positions establish preferences, not causal effect by themselves
  - Council outcomes are collective unless a specific leverage chain is documented
  - economic size is background capacity, not tasking
- **clusters:**
  - POWER
  - NETWORK
  - MONEY
  - TEMPORAL
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - **I01:** power is converted through institutions rather than automatically
  - **I02:** blocking leverage can produce bounded concessions
  - **I03:** joint agenda-setting can matter without command
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - **P01:** coalition-building
  - **P02:** bilateral agenda-setting
  - **P03:** blocking-minority leverage
  - **P04:** structural-power overclaim
- **priorities:**
  - trace mechanism-specific deltas
  - preserve counterfactual limits
  - separate bilateral, coalition and veto channels
- **query_guidance:** prioritize official national and EU documents; use independent reporting only for the procedural blocking event
- **rhetorical:**
  - **R01:** actor-first attribution
  - **R02:** post-hoc policy similarity
  - **R03:** ignoring qualified-majority constraints
- **speaker:**
  - **goal:** distinguish normal influence, structural power and coercion
  - **target:** preference -> mechanism -> EU delta
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** preference
  - **S02:** resource
  - **S03:** coalition
  - **S04:** procedure
  - **S05:** veto
  - **S06:** agenda
  - **S07:** proposal
  - **S08:** text_delta
  - **S09:** decision
  - **S10:** implementation
  - **S11:** distribution
  - **S12:** constraint
  - **S13:** counterfactual
  - **S14:** causality
  - **S15:** symmetry
- **threats:**
  - economic weight=control
  - German position=EU decision
  - coalition=domination
  - joint initiative=German command
  - concession=total victory

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - cross-domain matched denominator
  - **input_ids:**
    - FCT-001
    - FCT-004
    - FCT-010
    - FCT-011
    - FCT-012
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no evidence of unilateral German command across cases
  - **not_computable:**
    - general probability Germany gets preferred EU outcome
  - **operations_applied:**
    - mapped formal decision constraints
    - distinguished bounded concession from control
  - **reason:** separate institutional leverage from domination
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-004
    - CLM-005
    - CAU-001
    - CAU-003
    - CAU-004
  - **status:** DONE
  - **trigger:** member-state influence on EU decisions
- **item 2:**
  - **gaps:**
    - internal bargaining records incomplete
  - **input_ids:**
    - FCT-003
    - FCT-006
    - FCT-007
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - coalition membership does not imply German control of partners
  - **not_computable:**
    - individual partner counterfactual preferences
  - **operations_applied:**
    - mapped 11-state fiscal coalition
    - separated Franco-German co-sponsorship from German-only action
  - **reason:** trace coalition formation and joint agenda-setting
  - **result_ids:**
    - CLM-001
    - CLM-003
    - CAU-001
    - CAU-002
  - **status:** DONE
  - **trigger:** coalition and bilateral alignment
- **item 3:**
  - **gaps:**
    - no causal design isolating contribution size
  - **input_ids:**
    - FCT-002
    - FCT-006
    - FCT-008
  - **module:** clusters/MONEY.md
  - **negative_results:**
    - no evidence that German budget contribution alone determined outcomes
  - **not_computable:**
    - marginal effect of German net contribution
  - **operations_applied:**
    - separated fiscal constraint design from direct transfers
    - tracked recovery borrowing scale change
  - **reason:** map resource and budget channels without treating money as command
  - **result_ids:**
    - CLM-001
    - CLM-003
    - CAU-001
    - CAU-002
  - **status:** DONE
  - **trigger:** fiscal rules and recovery financing
- **item 4:**
  - **gaps:**
    - private bargaining content
  - **input_ids:**
    - FCT-001
    - FCT-003
    - FCT-004
    - FCT-006
    - FCT-007
    - FCT-008
    - FCT-009
    - FCT-010
    - FCT-012
  - **module:** clusters/TEMPORAL.md
  - **negative_results:**
    - policy similarity alone not accepted as causation
  - **not_computable:**
    - unobserved negotiation counterfactuals
  - **operations_applied:**
    - ordered proposal, coalition, negotiation and final outcome
    - preserved late-veto sequence in e-fuels case
  - **reason:** avoid post-hoc attribution from final-text similarity
  - **result_ids:**
    - CLM-001
    - CLM-003
    - CLM-004
    - CAU-001
    - CAU-002
    - CAU-003
  - **status:** DONE
  - **trigger:** sequence from preference to decision

### SCOPING_REPORT
- **excluded:**
  - generic Germany economic-size rankings
  - broad historical claims about German domination
  - energy-policy narratives without a bounded decision chain
- **included:**
  - EU fiscal-rules reform 2023-2024
  - Next Generation EU recovery-fund formation 2020
  - 2035 car CO2/e-fuels adoption 2023
- **reason:** three cases provide distinct observable institutional conversion mechanisms

### CREDO
- **forbidden_shortcuts:**
  - economic_weight=control
  - position=decision
  - coalition=domination
  - gain=capture
  - correlation=causality
- **rule:** trace preference -> coalition/procedure -> text or decision -> bounded effect; never infer control from size or outcome similarity

### COGNITIVE_MAP
- **chain:**
  - national preference
  - coalition/resource
  - EU procedure
  - text/decision delta
  - bounded effect
  - counterfactual gap
- **rival_models:**
  - normal negotiated influence
  - structural bargaining power
  - procedural blocking leverage
  - unilateral domination

### DIALECTICAL_MAP
- **antithesis:** EU institutions, coalitions and qualified-majority rules constrain Germany and produce collective compromises.
- **synthesis:** German influence is materially observable but mechanism-specific: coalition-building, joint agenda-setting and blocking-minority leverage. These channels can produce identifiable deltas without establishing general German control of the EU.
- **thesis:** Germany can convert national preferences into EU outcomes through superior structural power.

### RESOURCE_FLOW_MAP
- **flows:**
  - fiscal-rule preference -> 11-state coalition -> Council safeguards
  - Franco-German 500bn initiative -> Commission uptake -> 750bn EUCO compromise
  - German e-fuels demand -> withheld support/blocking minority -> postponement -> e-fuels pathway reference
- **limits:**
  - money != command
  - agenda-setting != adoption
  - blocking leverage != full policy victory

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** German Finance Ministry
  - **relation:** advocacy plus coalition-building
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
  - **to:** 11-state fiscal coalition / ECOFIN
- **item 2:**
  - **from:** Germany + France
  - **relation:** joint recovery initiative
  - **support:**
    - FCT-006
    - FCT-007
    - FCT-008
  - **to:** European Commission / European Council agenda
- **item 3:**
  - **from:** German federal government
  - **relation:** withheld support with other states
  - **support:**
    - FCT-009
    - FCT-010
    - FCT-011
    - FCT-012
  - **to:** Council final adoption / Commission e-fuels pathway

### IMPACT_MAP
- **established:**
  - case-specific German negotiated influence
  - fiscal coalition-building
  - joint Franco-German agenda-setting
  - procedural blocking leverage producing bounded e-fuels accommodation
- **not_established:**
  - general German control of EU institutions
  - economic weight as sufficient causal mechanism
  - coercion of other member states across cases
- **partial:**
  - German marginal authorship of fiscal safeguards

### CONTRADICTION_LEDGER
- **item 1:**
  - **issue:** German fiscal demands resemble final safeguards
  - **resolution:** retain influence signal but cap at partial unique authorship because final text is collective and German attribution is partly self-reported
- **item 2:**
  - **issue:** Franco-German initiative preceded NGEU
  - **resolution:** classify as joint agenda-setting because final package expanded and changed through Commission and European Council compromise
- **item 3:**
  - **issue:** Germany delayed 2035 car law
  - **resolution:** classify as strong procedural leverage, not total victory, because core 100 percent target remained

### VERIFICATION_REPORT
- **facts:** 12
- **method:** exact FETCH for every high-tier fact; mechanism-specific temporal chains and negative controls
- **negative_checks:**
  - final collective Council texts
  - modified recovery package
  - 2035 core target retained despite e-fuels concession
- **research_queries:** 10
- **sources_fetched:** 10
- **verdict:** sufficient to establish several bounded German influence mechanisms; insufficient to establish general German domination or economic-weight causality

### EDI_REPORT
- **corpus:** 10 accepted sources across 4 provenance families
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim:** CLM-001
    - **families:**
      - A
      - B
  - **item 2:**
    - **claim:** CLM-003
    - **families:**
      - B
      - C
  - **item 3:**
    - **claim:** CLM-004
    - **families:**
      - B
      - C
      - D
  - **item 4:**
    - **claim:** CLM-005
    - **families:**
      - A
      - B
      - C
      - D
- **diagnostic_not_truth:** true
- **dimensions:**
  - German national preferences
  - cross-state coalition
  - Council outcome
  - bilateral initiative
  - procedural blocking
  - final legal accommodation
- **edi:** MULTI_INSTITUTIONAL_WITH_NATIONAL_SELF_ATTRIBUTION_AND_ONE_INDEPENDENT_PROCEDURAL_SOURCE
- **source_counts:**
  - **A:** 3
  - **B:** 3
  - **C:** 3
  - **D:** 1

### RESPONSIBILITY_MAP
- **item 1:**
  - **actor:** German Federal Ministry of Finance
  - **documented_action:** proposed quantitative fiscal safeguards and coalitioned with other finance ministers
  - **intent:** PROVEN
  - **scope:** fiscal governance influence; unique authorship not isolated
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
    - FCT-005
- **item 2:**
  - **actor:** German and French governments
  - **documented_action:** jointly proposed European recovery fund
  - **intent:** PROVEN
  - **scope:** agenda-setting; final EUCO compromise collective
  - **support:**
    - FCT-006
    - FCT-007
    - FCT-008
- **item 3:**
  - **actor:** German federal government / transport minister
  - **documented_action:** conditioned final support on e-fuels pathway
  - **intent:** PROVEN
  - **scope:** procedural leverage and bounded concession
  - **support:**
    - FCT-009
    - FCT-010
    - FCT-011
    - FCT-012

### NEXT_QUERIES
- Do not reopen generic Germany-power collection without a new bounded decision and observable preference-to-delta chain.
- For stronger causal attribution, seek presidency negotiation notes, member-state position matrices or versioned text deltas that identify the marginal concession.
- Use INV-029 as a symmetry control: intra-EU influence can be strong and consequential without satisfying coercion or clandestine-ingérence criteria.

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-005,QRY-006,QRY-010 | support:- | counter:- | results:FCT-006,FCT-007,FCT-008 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-007,QRY-008,QRY-009 | support:- | counter:- | results:FCT-009,FCT-010,FCT-011,FCT-012 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,SRC-001,SRC-002,SRC-003,SRC-004 | support:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005 | counter:Final text was a Council/Parliament compromise and German post-hoc attribution does not isolate unique marginal authorship. | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,Final text was a Council/Parliament compromise and German post-hoc attribution does not isolate unique marginal authorship. | final:PARTIAL | gap:CAUSALITY
CLM-002 | attempts:QRY-002,QRY-006,QRY-009,SRC-002,SRC-006,SRC-009 | support:- | counter:FCT-003,FCT-008,FCT-011,FCT-012 | results:FCT-003,FCT-008,FCT-011,FCT-012 | final:REFUTED | gap:NONE
CLM-003 | attempts:QRY-005,QRY-006,QRY-010,SRC-005,SRC-006,SRC-010 | support:FCT-006,FCT-007,FCT-008 | counter:- | results:FCT-006,FCT-007,FCT-008 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-007,QRY-008,QRY-009,SRC-007,SRC-008,SRC-009 | support:FCT-009,FCT-010,FCT-011,FCT-012 | counter:The final e-fuels route remained subject to later Commission proposal,EU law and climate-neutrality conditions. | results:FCT-009,FCT-010,FCT-011,FCT-012,The final e-fuels route remained subject to later Commission proposal,EU law and climate-neutrality conditions. | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-002,QRY-005,QRY-006,QRY-008,QRY-009,SRC-002,SRC-005,SRC-006,SRC-008,SRC-009 | support:FCT-003,FCT-006,FCT-008,FCT-010,FCT-012 | counter:- | results:FCT-003,FCT-006,FCT-008,FCT-010,FCT-012 | final:SUPPORTED | gap:NONE

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-001 | CLM | PARTIAL | CAUSALITY | Unique German marginal effect versus aligned states and presidency compromise is not separately identified.
CAU-004 | CAU | UNRESOLVED | CAUSALITY | No comparative design isolates economic weight itself from coalition, presidency, institutional rules, domestic bargaining and other member-state preferences.

SEMANTIC_COUNTS_V1:LED:0|CLM:5|AXS:3|CAU:4|CTRL:5|ACT:3

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Germany converted a specific preference for quantitative fiscal safeguards into a Council framework containing materially similar safeguards through coalition and negotiation.","claimant":"INV-029","counter":"Final text was a Council/Parliament compromise and German post-hoc attribution does not isolate unique marginal authorship.","gap":"Unique German marginal effect versus aligned states and presidency compromise is not separately identified.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005"]}
CLM-002 | {"claim":"Germany generally controls EU decisions because of its economic weight.","claimant":"strong structural-power hypothesis","counter":["FCT-003","FCT-008","FCT-011","FCT-012"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"REFUTED","support":"NONE_FOUND"}
CLM-003 | {"claim":"The 2020 recovery fund shows joint Franco-German agenda-setting followed by Commission uptake and a materially modified 27-state compromise, not unilateral German command.","claimant":"INV-029","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-006","FCT-007","FCT-008"]}
CLM-004 | {"claim":"In the 2035 car file, Germany used late procedural leverage with other states to delay adoption and obtain an e-fuels pathway while the 100 percent fleet CO2 target remained intact.","claimant":"INV-029","counter":"The final e-fuels route remained subject to later Commission proposal, EU law and climate-neutrality conditions.","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-009","FCT-010","FCT-011","FCT-012"]}
CLM-005 | {"claim":"The observed German influence mechanisms are heterogeneous and case-specific: coalition-building, bilateral agenda-setting and blocking-minority leverage cannot be collapsed into one domination mechanism.","claimant":"INV-029","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-003","FCT-006","FCT-008","FCT-010","FCT-012"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004"],"axis":"FISCAL_RULES","links":["CLM-001","CLM-002","CAU-001"],"question":"Germany numerical fiscal-rule preferences -> coalition -> Council safeguards?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005"],"sought_objects":["GERMAN_POSITION","COALITION","SAFEGUARDS","FINAL_RULE"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-005","QRY-006","QRY-010"],"axis":"RECOVERY_FUND","links":["CLM-003","CLM-002","CAU-002"],"question":"Franco-German initiative -> Commission uptake -> European Council compromise?","result_ids":["FCT-006","FCT-007","FCT-008"],"sought_objects":["JOINT_INITIATIVE","COMMISSION_UPTAKE","EUCO_COMPROMISE"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-007","QRY-008","QRY-009"],"axis":"EFUELS_BLOCKING","links":["CLM-004","CLM-002","CAU-003"],"question":"German withholding of support -> delayed adoption -> e-fuels accommodation while core target survives?","result_ids":["FCT-009","FCT-010","FCT-011","FCT-012"],"sought_objects":["GERMAN_POSITION","BLOCKING_MINORITY","DELAY","CONCESSION","FINAL_TARGET"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"documented preference plus coalition plus matched negotiated outcome -> safeguards adopted","counter":"The outcome was negotiated by all member states and Parliament; German sources self-attribute influence.","limit":"Specific negotiated influence is supported; unique marginal German authorship is not isolated.","mechanism":"German quantitative fiscal-rule preferences -> coalition support -> Council negotiation -> debt/deficit safeguards","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005"]}
CAU-002 | {"causal_right":"joint bilateral initiative -> supranational proposal uptake -> 27-state negotiated outcome","counter":"The final 750 billion package differed materially from the 500 billion bilateral initiative and required European Council agreement.","limit":"Joint agenda-setting and proposal influence supported; unilateral German control refuted.","mechanism":"Franco-German recovery initiative -> Commission uptake -> European Council recovery compromise","status":"SUPPORTED","support":["FCT-006","FCT-007","FCT-008"]}
CAU-003 | {"causal_right":"credible withholding of qualified-majority support -> delay -> negotiated concession while core rule survives","counter":"Germany did not remove the 2035 100 percent CO2 fleet target and the e-fuels route remained conditional on later legal implementation.","limit":"Procedural leverage and bounded concession supported; complete policy control not supported.","mechanism":"German withholding of support -> blocking minority/postponement -> e-fuels accommodation -> final adoption","status":"SUPPORTED","support":["FCT-009","FCT-010","FCT-011","FCT-012"]}
CAU-004 | {"counter":["FCT-003","FCT-008","FCT-011","FCT-012"],"gap":"No comparative design isolates economic weight itself from coalition, presidency, institutional rules, domestic bargaining and other member-state preferences.","gap_type":"CAUSALITY","limit":"Three cases show different institutional mechanisms and significant constraints; no cross-domain marginal-effect denominator.","mechanism":"German economic weight -> systematic control of EU outcomes across policy domains","status":"UNRESOLVED","support":"NONE_FOUND"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"economic weight != control","status":"PASS","support":["FCT-008","FCT-011"]}
CTRL-002 | {"control":"German position != EU decision","status":"PASS","support":["FCT-001","FCT-004","FCT-009","FCT-011"]}
CTRL-003 | {"control":"coalition != domination","status":"PASS","support":["FCT-003","FCT-004"]}
CTRL-004 | {"control":"joint agenda-setting != unilateral command","status":"PASS","support":["FCT-006","FCT-007","FCT-008"]}
CTRL-005 | {"control":"procedural veto leverage != complete policy victory","status":"PASS","support":["FCT-010","FCT-011","FCT-012"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Advocated numerical minimum fiscal safeguards and built a coalition of like-minded finance ministers.","actor":"German federal finance ministry and allied EU finance ministers","intent":"PROVEN","status":"DONE","support":["FCT-001","FCT-002","FCT-003"]}
ACT-002 | {"action":"Co-launched a 500 billion euro recovery-fund initiative with France.","actor":"German and French governments","intent":"PROVEN","status":"DONE","support":["FCT-006","FCT-007"]}
ACT-003 | {"action":"Withheld support for final 2035 car-law approval pending an e-fuels route, contributing to postponement and later accommodation.","actor":"German federal government with other blocking states","intent":"PROVEN","status":"DONE","support":["FCT-009","FCT-010","FCT-012"]}

SEARCH_ACTIVITY_V1:WEB:0|FETCH:10|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | MNEMO_UNAVAILABLE | mnemo | NONE | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.bundesfinanzministerium.de/Monatsberichte/2023/06/Inhalte/Kapitel-2a-Schlaglicht/funktionierende-fiskalregeln.html | German position EU fiscal rules June 2023
QRY-002 | FETCH | FOUND | SRC-002 | https://www.bundesfinanzministerium.de/Monatsberichte/2023/06/Inhalte/Kapitel-2a-Schlaglicht/gastbeitrag-finanzminister-reform-eu-fiskalregeln.html | 11 finance ministers fiscal rules
QRY-003 | FETCH | FOUND | SRC-003 | https://www.consilium.europa.eu/en/press/press-releases/2023/12/21/economic-governance-review-council-agrees-on-reform-of-fiscal-rules/ | Council agrees fiscal rules safeguards
QRY-004 | FETCH | FOUND | SRC-004 | https://www.bundesfinanzministerium.de/Monatsberichte/Ausgabe/2024/05/Inhalte/Kapitel-2-Fokus/reform-stabilitaets-und-wachstumspakt.html | BMF outcome fiscal rules 2024 safeguards
QRY-005 | FETCH | FOUND | SRC-005 | https://www.bundesregierung.de/breg-en/news/dt-franz-initiative-1753890 | Franco German recovery initiative 500 billion
QRY-006 | FETCH | FOUND | SRC-006 | https://www.consilium.europa.eu/en/press/press-releases/2020/07/21/european-council-conclusions-17-21-july-2020/ | European Council recovery fund July 2020
QRY-007 | FETCH | FOUND | SRC-007 | https://www.bundesregierung.de/breg-de/service/newsletter-und-abos/bulletin/rede-des-bundesministers-fuer-digitales-und-verkehr-dr-volker-wissing--2169724 | Wissing e-fuels EU March 2023 conflict
QRY-008 | FETCH | FOUND | SRC-008 | https://euractiv.com/fr/news/fin-des-moteurs-a-combustion-en-2035-les-diplomates-europeens-vent-debout-contre-le-blocage-de-berlin/ | Germany block final 2035 cars vote March 2023
QRY-009 | FETCH | FOUND | SRC-009 | https://www.consilium.europa.eu/en/press/press-releases/2023/03/28/fit-for-55-council-adopts-regulation-on-co2-emissions-for-new-cars-and-vans/ | Council adopts 2035 cars e-fuels reference
QRY-010 | FETCH | FOUND | SRC-010 | https://www.bundesregierung.de/breg-en/service/archive/speech-by-federal-chancellor-angela-merkel-on-the-german-presidency-of-the-council-of-the-eu-2020-to-the-european-parliament-in-brussels-on-8-july-2020-1768008 | Merkel Commission incorporated Franco-German recovery initiative

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | BMF-2023-06-FISKALREGELN | Funktionierende Fiskalregeln sind das Fundament für den Erfolg Europas | 2023-06-16 | 2026-09-11 | web | https://www.bundesfinanzministerium.de/Monatsberichte/2023/06/Inhalte/Kapitel-2a-Schlaglicht/funktionierende-fiskalregeln.html
SRC-002 | ◈ | fam:A | BMF-2023-06-11MINISTERS | Klare und verständliche Regeln für tragfähige öffentliche Finanzen und Handlungsspielraum | 2023-06-15 | 2026-09-11 | web | https://www.bundesfinanzministerium.de/Monatsberichte/2023/06/Inhalte/Kapitel-2a-Schlaglicht/gastbeitrag-finanzminister-reform-eu-fiskalregeln.html
SRC-003 | ◈ | fam:B | COUNCIL-2023-12-FISCAL | Economic governance review: Council agrees on reform of fiscal rules | 2023-12-21 | 2026-09-11 | web | https://www.consilium.europa.eu/en/press/press-releases/2023/12/21/economic-governance-review-council-agrees-on-reform-of-fiscal-rules/
SRC-004 | ◈ | fam:A | BMF-2024-05-FISCAL | Reform des Europäischen Stabilitäts- und Wachstumspakts | 2024-05-24 | 2026-09-11 | web | https://www.bundesfinanzministerium.de/Monatsberichte/Ausgabe/2024/05/Inhalte/Kapitel-2-Fokus/reform-stabilitaets-und-wachstumspakt.html
SRC-005 | ◈ | fam:C | BREG-2020-05-RECOVERY | Emerging stronger from the crisis | 2020-05-18 | 2026-09-11 | web | https://www.bundesregierung.de/breg-en/news/dt-franz-initiative-1753890
SRC-006 | ◈ | fam:B | EUCO-2020-07-RECOVERY | European Council conclusions, 17-21 July 2020 | 2020-07-21 | 2026-09-11 | web | https://www.consilium.europa.eu/en/press/press-releases/2020/07/21/european-council-conclusions-17-21-july-2020/
SRC-007 | ◈ | fam:C | BREG-2023-03-EFUELS | Rede des Bundesministers für Digitales und Verkehr Dr. Volker Wissing | 2023-03-03 | 2026-09-11 | web | https://www.bundesregierung.de/breg-de/service/newsletter-und-abos/bulletin/rede-des-bundesministers-fuer-digitales-und-verkehr-dr-volker-wissing--2169724
SRC-008 | ○ | fam:D | EURACTIV-2023-03-BLOCK | Fin des moteurs à combustion en 2035 : les diplomates européens vent debout contre le blocage de Berlin | 2023-03-06 | 2026-09-11 | web | https://euractiv.com/fr/news/fin-des-moteurs-a-combustion-en-2035-les-diplomates-europeens-vent-debout-contre-le-blocage-de-berlin/
SRC-009 | ◈ | fam:B | COUNCIL-2023-03-CARS | Fit for 55: Council adopts regulation on CO2 emissions for new cars and vans | 2023-03-28 | 2026-09-11 | web | https://www.consilium.europa.eu/en/press/press-releases/2023/03/28/fit-for-55-council-adopts-regulation-on-co2-emissions-for-new-cars-and-vans/
SRC-010 | ◈ | fam:C | BREG-2020-07-MERKEL-EP | Speech by Federal Chancellor Angela Merkel on the German Presidency of the Council of the EU 2020 | 2020-07-08 | 2026-09-11 | web | https://www.bundesregierung.de/breg-en/service/archive/speech-by-federal-chancellor-angela-merkel-on-the-german-presidency-of-the-council-of-the-eu-2020-to-the-european-parliament-in-brussels-on-8-july-2020-1768008

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.bundesfinanzministerium.de/Monatsberichte/2023/06/Inhalte/Kapitel-2a-Schlaglicht/funktionierende-fiskalregeln.html | A | 2023-06-16 | DE_FISCAL_POSITION | Germany considered the Commission April 2023 fiscal-rule proposal insufficient and demanded clear, uniform numerical minimum requirements. | -
FCT-002 | FACT | ✧ | https://www.bundesfinanzministerium.de/Monatsberichte/2023/06/Inhalte/Kapitel-2a-Schlaglicht/funktionierende-fiskalregeln.html | A | 2023-06-16 | DE_DEBT_SAFEGUARD_PROPOSAL | Germany proposed an independent common safeguard requiring annual debt-ratio reduction of at least 1 percentage point for high-debt states and 0.5 percentage point for medium-debt states above 60 percent. | -
FCT-003 | FACT | ✧ | https://www.bundesfinanzministerium.de/Monatsberichte/2023/06/Inhalte/Kapitel-2a-Schlaglicht/gastbeitrag-finanzminister-reform-eu-fiskalregeln.html | A | 2023-06-15 | FISCAL_COALITION_11 | Finance ministers from 11 of 27 EU member states jointly endorsed clear and simple expenditure rules applicable across countries. | -
FCT-004 | FACT | ✧ | https://www.consilium.europa.eu/en/press/press-releases/2023/12/21/economic-governance-review-council-agrees-on-reform-of-fiscal-rules/ | B | 2023-12-21 | COUNCIL_FISCAL_SAFEGUARDS | The Council agreement required both a debt sustainability safeguard and a deficit resilience safeguard in the technical trajectory. | -
FCT-005 | FACT | ✧ | https://www.bundesfinanzministerium.de/Monatsberichte/Ausgabe/2024/05/Inhalte/Kapitel-2-Fokus/reform-stabilitaets-und-wachstumspakt.html | A | 2024-05-24 | DE_OUTCOME_ATTRIBUTION | The German Finance Ministry stated after adoption that the debt-sustainability and deficit-resilience safeguards originated from Germany demand for quantitative minimum requirements. | -
FCT-006 | FACT | ✧ | https://www.bundesregierung.de/breg-en/news/dt-franz-initiative-1753890 | C | 2020-05-18 | FR_DE_RECOVERY_INITIATIVE | Germany and France jointly proposed a 500 billion euro European recovery fund aimed at the sectors and regions hardest hit by the pandemic. | -
FCT-007 | FACT | ✧ | https://www.bundesregierung.de/breg-en/service/archive/speech-by-federal-chancellor-angela-merkel-on-the-german-presidency-of-the-council-of-the-eu-2020-to-the-european-parliament-in-brussels-on-8-july-2020-1768008 | C | 2020-07-08 | COMMISSION_TAKES_FRDE_ELEMENTS | Merkel stated that the Commission had incorporated many aspects of the Franco-German initiative into its MFF and recovery-programme proposal. | -
FCT-008 | FACT | ✧ | https://www.consilium.europa.eu/en/press/press-releases/2020/07/21/european-council-conclusions-17-21-july-2020/ | B | 2020-07-21 | EUCO_RECOVERY_COMPROMISE | The European Council final compromise authorised up to 750 billion euro of EU borrowing for Next Generation EU, combining loans and expenditure rather than reproducing the Franco-German proposal unchanged. | -
FCT-009 | FACT | ✧ | https://www.bundesregierung.de/breg-de/service/newsletter-und-abos/bulletin/rede-des-bundesministers-fuer-digitales-und-verkehr-dr-volker-wissing--2169724 | C | 2023-03-03 | DE_EFUELS_POSITION | German transport minister Volker Wissing publicly insisted that the Commission deliver a route for registering new combustion-engine vehicles after 2035 when operated with synthetic fuels. | -
FCT-010 | FACT | ✧ | https://euractiv.com/fr/news/fin-des-moteurs-a-combustion-en-2035-les-diplomates-europeens-vent-debout-contre-le-blocage-de-berlin/ | D | 2023-03-06 | DE_EFUELS_BLOCKING_EFFECT | Germany last-minute refusal to support the already-negotiated 2035 car measure contributed to postponement of the formal approval vote and, with other states, created a blocking minority. | -
FCT-011 | FACT | ✧ | https://www.consilium.europa.eu/en/press/press-releases/2023/03/28/fit-for-55-council-adopts-regulation-on-co2-emissions-for-new-cars-and-vans/ | B | 2023-03-28 | FINAL_CARS_2035 | The Council ultimately adopted the 100 percent CO2 reduction target for new cars and vans from 2035. | -
FCT-012 | FACT | ✧ | https://www.consilium.europa.eu/en/press/press-releases/2023/03/28/fit-for-55-council-adopts-regulation-on-co2-emissions-for-new-cars-and-vans/ | B | 2023-03-28 | FINAL_EFUELS_REFERENCE | The adopted framework included a reference under which the Commission would propose a route for registering vehicles running exclusively on CO2-neutral fuels after 2035, outside fleet standards and subject to EU law and climate-neutrality objectives. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-002
FCT-004 | SRC-003
FCT-005 | SRC-004
FCT-006 | SRC-005
FCT-007 | SRC-010
FCT-008 | SRC-006
FCT-009 | SRC-007
FCT-010 | SRC-008
FCT-011 | SRC-009
FCT-012 | SRC-009

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

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:SEARCH
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:FACTS
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:CAUSAL
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:VERIFY
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:INVESTIGATION_ACCOUNTABILITY
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:FINALIZE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-10T23:01:43.507585+00:00","fact_mem":{},"mnemo_row":"MNEMO_UNAVAILABLE — local memory service not available; no memory ids fabricated.","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":12,"eligible":12,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_UNAVAILABLE — local memory service not available; no memory ids fabricated. | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:12;attempted:0;success:0;failure:0;blocked:12} | WRITEBACK_EXECUTION_V1:[12 rows, see section]

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
