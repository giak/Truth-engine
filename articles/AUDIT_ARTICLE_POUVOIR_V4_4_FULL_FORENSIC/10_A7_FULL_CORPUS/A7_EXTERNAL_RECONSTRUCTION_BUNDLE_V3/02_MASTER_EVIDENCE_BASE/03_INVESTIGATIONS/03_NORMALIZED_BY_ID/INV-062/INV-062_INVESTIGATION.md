ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260909-1657-mckinsey-state-consulting-influence | PARENT_RUN_ID:NONE | AS_OF:2026-09-09
INPUT_KIND:RUN_CARD | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/inv062/runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-09_mckinsey-state-consulting-influence/2026-09-09_16-57_mckinsey-state-consulting-influence_INPUT.md | SUBJECT_SLUG:mckinsey-state-consulting-influence | SUBJECT_FP:sha256:8cad9a39fb806bd59f1d62250d57f5f4b86e1b798927b6d436b012fab710b25e | INPUT_SHA256:sha256:17d7e793453f28d440930c92e6cd331317ac58442616bd727ed1cfe1a960790b
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France, mainly 2017-2026; trace administration/ministry -> contract -> consulting firm -> deliverable/recommendation -> adoption, modification or rejection -> public decision -> implementation/effect, separating external expertise, influence, cognitive dependence, delegation of decision and policy effect.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/NETWORK.md,clusters/POWER.md,clusters/CONFIRMATION.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-062 — McKinsey et cabinets de conseil dans l’État français

## Objet

L’enquête teste une chaîne bornée : **administration/ministère -> contrat -> cabinet -> livrable ou recommandation -> filtrage public -> décision ou mise en œuvre -> effet**. Elle distingue explicitement prestation, influence sur la préparation, dépendance opérationnelle, adoption, décision souveraine et effet de politique publique.

## Verdict

Le corpus établit une **pénétration matérielle et documentable des cabinets dans la préparation de certaines décisions et dans l’exécution de certaines politiques**. Le Sénat documente des missions de stratégie où les consultants prennent des positions de fond et présentent des scénarios orientés ou « clé en main », ainsi que leur intervention dans plusieurs réformes majeures. [FCT-001, FCT-006, FCT-007]

Ce constat ne ferme pas la chaîne jusqu’à une délégation générale de souveraineté. Les mêmes sources maintiennent la responsabilité des autorités publiques, montrent des filtres administratifs, des réécritures et des rejets de propositions, et fournissent des cas de transfert des activités vers les équipes internes. [FCT-004, FCT-005, FCT-010, FCT-016]

Le plafond probatoire est donc : **influence externe réelle et parfois importante sur la préparation ou l’implémentation ; dépendance ponctuelle documentée ; délégation généralisée de la décision politique non établie**.

## 1. Préparation de la décision : influence réelle, causalité finale non générale

Le rapport sénatorial distingue des missions sans suite tangible et d’autres ayant directement influencé des politiques publiques, notamment lorsque des cabinets structurent des scénarios de décision. Il relève également des différences fortes dans la capacité des ministères à piloter les consultants. [FCT-001, FCT-002]

La présence contractuelle ou le montant dépensé ne suffit donc pas. L’objet discriminant est l’existence d’un passage démontrable entre production du cabinet et préparation, adoption ou exécution publique.

## 2. Vaccination : contribution opérationnelle et dépendance réversible

McKinsey a reçu sept commandes liées à la vaccination pour 11,63 millions d’euros et est intervenu pendant plus d’un an. Olivier Véran a reconnu une contribution à la rédaction d’au moins un document ministériel tout en affirmant que les décisions restaient ministérielles et passaient par le filtre de la DGS. [FCT-005, FCT-009, FCT-011]

Le Sénat décrit une forme de dépendance organisationnelle, mais documente aussi le transfert des activités à la task force vaccinale, qui a ensuite fonctionné seule avant un rappel temporaire. La dépendance est donc établie **dans ce cas**, mais sa permanence et son extension à l’ensemble de l’État ne le sont pas. [FCT-010, FCT-012]

## 3. Télétravail : chaîne jusqu’à l’implémentation, auteurs multiples

Le guide public de télétravail ne mentionnait pas clairement le rôle des cabinets alors que McKinsey détenait le marché et qu’Alixio réalisait une partie du travail. Cependant, DITP et DGAFP fournissaient les matériaux, réécrivaient substantiellement les drafts et rejetaient certaines propositions. [FCT-015, FCT-016]

Une circulaire gouvernementale a ensuite renvoyé les managers vers le kit de bonnes pratiques. Ce cas ferme une chaîne **contribution de conseil -> production administrative partagée -> implémentation**, mais non une chaîne de contrôle autonome du cabinet. [FCT-017]

## 4. Contrôles négatifs : mission achetée ne signifie pas effet

La mission McKinsey sur le métier d’enseignant, proche de 500 000 euros, n’avait selon le Sénat ni besoin ni valeur ajoutée démontrés. Le ministère de l’Éducation n’a pas pu déterminer les conséquences directes de ses livrables, certains n’étant qu’une source parmi d’autres. [FCT-013, FCT-014]

Le cas CNAV fournit un autre contrôle : après une réflexion soutenue par du conseil, le programme Retraite 2025 a été lancé avec des compétences internes. [FCT-003]

Ces cas falsifient l’équivalence **contrat ou dépense = influence ou effet**.

## 5. Traçabilité, gouvernance et internalisation après 2022

Les rapports parlementaires et gouvernementaux postérieurs à 2022 documentent des contrôles renforcés : vérification préalable des compétences internes, supervision des engagements et identification des consultants. [FCT-020, FCT-021, FCT-022, FCT-023]

DITP indique une baisse des commandes externes de 271 millions d’euros en 2021 à 137 millions en 2022 puis 80 millions en 2023, et la création en 2024 d’une agence interne de conseil de l’État. [FCT-024, FCT-025]

La Cour des comptes ajoute un contrôle externe et publie les réponses des administrations, ce qui préserve la contradiction institutionnelle. [FCT-026, FCT-027]

La proposition sénatoriale de 2024 visant à identifier explicitement les consultants et leurs contributions dans les documents administratifs répond directement au problème de traçabilité observé dans plusieurs dossiers. [FCT-028]

## Conclusion forensique

1. **Expertise externalisée : établie à grande échelle dans les cas inspectés.**
2. **Influence sur la préparation : établie dans plusieurs missions.**
3. **Contribution à l’implémentation : établie dans certains cas, notamment vaccination et télétravail.**
4. **Dépendance : établie ponctuellement, avec contre-preuves de réversibilité et d’internalisation.**
5. **Délégation générale de souveraineté ou contrôle des décisions politiques par les cabinets : non établie.**
6. **Effet causal sur les politiques : à démontrer mission par mission ; ni contrat, ni montant, ni proximité chronologique ne suffisent.**
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:6|SRC_COMPLETE:16/16

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-09
- **notes:**
  - 2018-2021 cases document intensive external consulting on reforms and crisis operations
  - 2022 parliamentary controversy was followed by tighter governance/internal-capability rules
  - 2023-2024 audit, spending decline and internal State consulting capacity provide post-controversy controls
- **status:** CURRENT
- **window:** 2017-2026

### MANIPULATION_REPORT
- **assumptions:**
  - public authority may retain formal responsibility while consultant input materially changes options
  - internal editing/rejection is evidence against autonomous consultant control
  - post-2022 internalisation is relevant counter-evidence to permanent-dependence claims
- **clusters:**
  - **loaded:**
    - clusters/NETWORK.md
    - clusters/POWER.md
    - clusters/CONFIRMATION.md
- **complexity:**
  - **band:** HIGH
  - **score:** 9
- **implicit:**
  - material influence can exist upstream without consultant control of final authority
  - dependence may be local and reversible
  - opaque attribution is a governance problem distinct from causal capture
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - external expertise
  - decision preparation
  - scenario design
  - operational support
  - shared authorship
  - dependence
  - internalisation
  - traceability
- **priorities:**
  - decision penetration
  - case-specific implementation edge
  - negative controls
  - dependence reversibility
  - traceability
  - causal ceiling
- **query_guidance:** prefer contract/audit/hearing/document chains; require explicit adoption or implementation evidence and preserve public-authority filtering.
- **rhetorical:**
  - **AUTH:** parliamentary, government and audit sources are evidence subject to contradiction
  - **BF:** trace contract-to-output-to-decision edge case by case
  - **DEM:** apply the same causal standard to influence and non-influence cases
  - **FAC:** separate preparation, adoption, implementation and downstream effect
  - **NUM:** use spending as scale context, not causal proof
- **speaker:**
  - **goal:** forensic causal discrimination
  - **target:** administration -> contract -> consultant output -> public filtering -> decision/implementation -> effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **§:** 5
  - **Κ:** 4
  - **Λ:** 5
  - **Ξ:** 5
  - **Σ:** 5
  - **Φ:** 5
  - **Ψ:** 5
  - **Ω:** 4
  - **κ:** 4
  - **ρ:** 4
  - **↕:** 5
  - **⏰:** 5
  - **⚔:** 5
  - **⫸:** 5
  - **🌐:** 4
- **threats:**
  - consulting=decision
  - spend=influence
  - recommendation=adoption
  - contribution=authorship
  - outsourcing=sovereignty loss
  - selected dependence=systemic dependence

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - decision-specific counterfactual causality
  - **input_ids:**
    - FCT-001
    - FCT-004
    - FCT-006
    - FCT-007
    - FCT-019
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no generalized consultant decision authority established
  - **not_computable:**
    - marginal contribution to many final reform choices
  - **operations_applied:**
    - mapped preparation, filtering, adoption and implementation as distinct edges
  - **reason:** separate material agenda/option-shaping power from final sovereign decision authority
  - **result_ids:**
    - CLM-001
    - CLM-006
    - CAU-001
    - CAU-005
  - **status:** DONE
  - **trigger:** consultants work on major reforms and can present oriented/turnkey scenarios
- **item 2:**
  - **gaps:**
    - authenticated tasking or dependence beyond formal contracts
  - **input_ids:**
    - FCT-002
    - FCT-009
    - FCT-010
    - FCT-016
    - FCT-022
    - FCT-025
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no single consultant command chain over ministries established
  - **not_computable:**
    - informal influence not documented in inspected records
  - **operations_applied:**
    - separated contracting, consultant contribution, administrative filtering, transfer-back and oversight roles
  - **reason:** map responsibility and transfer edges without inferring coordination or capture from recurring relationships
  - **result_ids:**
    - CLM-002
    - CLM-003
    - CLM-005
    - CAU-002
    - CAU-003
  - **status:** DONE
  - **trigger:** multiple ministries, DITP, consultants, audit and parliamentary controls form a recurring institutional network
- **item 3:**
  - **gaps:**
    - cross-ministry denominator and causal outcome designs
  - **input_ids:**
    - FCT-003
    - FCT-005
    - FCT-010
    - FCT-013
    - FCT-014
    - FCT-016
    - FCT-024
    - FCT-025
    - FCT-027
  - **module:** clusters/CONFIRMATION.md
  - **negative_results:**
    - spending and mission existence do not consistently predict policy effect
  - **not_computable:**
    - whole-of-state prevalence of cognitive dependence
  - **operations_applied:**
    - tested strong claims against no-follow-up, internal-editing, transfer-back and spending-decline controls
  - **reason:** use weak-effect, internal-control and reversibility cases as explicit falsifiers
  - **result_ids:**
    - CLM-004
    - CLM-005
    - CLM-006
    - CAU-004
    - CAU-005
  - **status:** DONE
  - **trigger:** sovereignty-loss and capture interpretations risk selecting only high-spend or controversial cases

### SCOPING_REPORT
- **actors_institutions:**
  - ministries and central administrations
  - DITP
  - DGAFP
  - McKinsey
  - other consulting firms
  - Parliament
  - Cour des comptes
- **domains:**
  - public consulting procurement
  - policy preparation
  - crisis operations
  - administrative transformation
  - internal capability
  - traceability
- **evidence_limits:**
  - no exhaustive mission-to-policy outcome denominator
  - precise consultant authorship often difficult to reconstruct
  - informal influence and internal deliberation not fully observable
  - spending data do not identify causal decision effects
- **exclusions:**
  - consulting treated as decision by default
  - contract value treated as influence
  - recommendation treated as adoption
  - outsourcing treated as sovereignty loss without displacement evidence
- **geo:** France
- **period:** 2017-2026

### CREDO
- consulting != decision
- recommendation != adoption
- contract value != influence
- similarity != authorship
- outsourcing != sovereignty loss by default
- chronology != causality
- case-specific dependence != systemic dependence

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - contract
  - scenario/recommendation
  - administrative filtering
  - shared drafting
  - implementation
  - dependence
  - transfer-back
  - internalisation
- **priorities:**
  - specific decision edge
  - public-authority filter
  - implementation trace
  - negative control
  - dependence ceiling
- **query_guidance:** trace one mission edge at a time and stop before causal claims unsupported by adoption or implementation evidence.
- **speaker:**
  - **goal:** forensic discrimination
  - **target:** contract -> consultant output -> administrative filter -> decision/implementation -> effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **threats:**
  - causal inflation
  - authorship inflation
  - spend proxy error
  - selection bias

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** The Senate documents substantive positions, oriented scenarios and involvement in major reforms, plus case-specific implementation edges.
  - **support:**
    - FCT-001
    - FCT-006
    - FCT-007
    - FCT-017
  - **synthesis:** Consultants can materially shape preparation and implementation; final political decision causality must be established separately.
  - **thesis:** Consultants are merely technical suppliers with no material effect on public policy.
- **item 2:**
  - **antithesis:** Decision responsibility, administrative filtering, transfer-back, falling orders and internal capability rebuilding are documented.
  - **support:**
    - FCT-004
    - FCT-005
    - FCT-010
    - FCT-012
    - FCT-016
    - FCT-024
    - FCT-025
  - **synthesis:** Case-specific dependence and opacity are real; generalized sovereign decision displacement is not established by the inspected corpus.
  - **thesis:** The consulting boom demonstrates a generalized delegation of state sovereignty.
- **item 3:**
  - **antithesis:** The teacher mission had no demonstrated need/value added and no determinable direct consequences.
  - **support:**
    - FCT-013
    - FCT-014
    - FCT-020
  - **synthesis:** Mission price and existence are scale indicators, not effect measures; outcome tracing is required.
  - **thesis:** High-value consulting missions necessarily produce corresponding policy value or effect.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **flow:** administration -> procurement/order -> consulting firm -> deliverable/service
  - **resource:** public consulting expenditure
  - **support:**
    - FCT-008
    - FCT-009
    - FCT-013
    - FCT-018
    - FCT-024
- **item 2:**
  - **flow:** ministry/administration -> consultant scenarios/expertise -> administrative/political filtering -> public decision preparation
  - **resource:** decision-preparation capacity
  - **support:**
    - FCT-001
    - FCT-004
    - FCT-006
    - FCT-019
- **item 3:**
  - **flow:** external support -> transfer-back/internalisation -> State task force or internal consulting agency
  - **resource:** internal capability
  - **support:**
    - FCT-003
    - FCT-010
    - FCT-023
    - FCT-025

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** ministries / administrations
  - **relation:** contract, steer, edit, accept or reject outputs
  - **support:**
    - FCT-002
    - FCT-016
    - FCT-022
  - **to:** consulting firms
- **item 2:**
  - **from:** consulting firms including McKinsey
  - **relation:** provide scenarios, operational support and draft contributions
  - **support:**
    - FCT-006
    - FCT-009
    - FCT-011
    - FCT-017
  - **to:** public decision-preparation and implementation chains
- **item 3:**
  - **from:** political/administrative authorities
  - **relation:** retain formal decision responsibility and filtering
  - **support:**
    - FCT-004
    - FCT-005
    - FCT-016
  - **to:** consultant-supported work
- **item 4:**
  - **from:** Parliament / Cour des comptes / DITP
  - **relation:** audit, regulate, reduce or internalise external consulting
  - **support:**
    - FCT-020
    - FCT-021
    - FCT-024
    - FCT-025
    - FCT-026
    - FCT-028
  - **to:** State consulting governance

### IMPACT_MAP
- **autonomous_consultant_decision_authority:** NOT_ESTABLISHED
- **general_sovereignty_delegation:** NOT_ESTABLISHED
- **material_decision_preparation_influence:** VERIFIED_CASE_SPECIFICALLY
- **opacity_of_contribution:** VERIFIED_CASE_SPECIFICALLY
- **operational_implementation_contribution:** VERIFIED_CASE_SPECIFICALLY
- **persistent_whole_state_dependence:** NOT_ESTABLISHED
- **post_2022_internalisation_and_spend_reduction:** VERIFIED
- **support:**
  - FCT-001
  - FCT-006
  - FCT-010
  - FCT-012
  - FCT-015
  - FCT-016
  - FCT-017
  - FCT-024
  - FCT-025
  - FCT-028

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** political authority remains responsible and administrative filters/editing are documented
  - **issue:** material influence versus retained public authority
  - **pro:** consultants can present substantive/oriented scenarios and work on major reforms
  - **resolution:** upstream influence is supported; generalized consultant decision authority is not
  - **support:**
    - FCT-004
    - FCT-005
    - FCT-006
    - FCT-016
- **item 2:**
  - **contra:** activities were transferred back and internal consulting capacity was later rebuilt while orders fell
  - **issue:** dependence versus reversibility/internal capability
  - **pro:** vaccination organisation shows a documented form of dependence
  - **resolution:** case-specific dependence supported; permanent systemic dependence not established
  - **support:**
    - FCT-010
    - FCT-012
    - FCT-024
    - FCT-025
- **item 3:**
  - **contra:** other missions had no demonstrable need/value added or determinable direct consequences
  - **issue:** consultant contribution versus policy effect
  - **pro:** some consultant-supported outputs reached implementation
  - **resolution:** effects are mission-specific and require direct tracing
  - **support:**
    - FCT-013
    - FCT-014
    - FCT-017

### VERIFICATION_REPORT
- **circular_families:**
  - Senate inquiry family A
  - government/administration family B
  - Cour des comptes family C
  - Assemblée nationale family D
  - DITP/Senate legislative family E
- **contradiction_ids:**
  - influence-vs-decision-authority
  - dependence-vs-reversibility
  - mission-spend-vs-effect
- **downgraded_ids:**
  - contract value as influence proxy
  - consultant contribution as autonomous authorship
  - case-specific dependence as generalized sovereignty loss
- **none_found_claims:**
  - general consultant control of sovereign political decisions
  - cross-ministry causal denominator for persistent cognitive dependence
  - general mission-price-to-policy-effect relationship
- **remaining_gaps:**
  - decision-specific marginal causality
  - whole-of-state prevalence denominator
  - versioned authorship/provenance for consultant-supported documents
- **verification:** All 28 material facts are linked to 16 current FETCH sources spanning five provenance families; causal conclusions remain bounded to inspected mission chains.

### EDI_REPORT
- **corpus:**
  - **circularity:** Senate findings cross-checked with administration, Assembly, DITP and Cour des comptes records
  - **coverage:** STRONG_FOR_SCALE_AND_GOVERNANCE;STRONG_FOR_SELECTED_CASE_PATHS;MODERATE_FOR_DEPENDENCE;WEAK_FOR_GENERAL_SOVEREIGNTY_DELEGATION
  - **independence:** 5_PROVENANCE_FAMILIES
  - **limits:**
    - parliamentary case selection is not a full denominator
    - administrative responses may contest audit interpretation
    - no general causal design on policy counterfactuals
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES_DECISION_PREPARATION
    - **gap_type:** NONE
    - **independent_families:** 2
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES_VACCINATION_OPERATION
    - **gap_type:** NONE
    - **independent_families:** 1
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** YES_OUTPUT_TO_IMPLEMENTATION
    - **gap_type:** NONE
    - **independent_families:** 1
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** NEGATIVE_CONTROL
    - **gap_type:** NONE
    - **independent_families:** 1
  - **item 5:**
    - **claim_id:** CLM-005
    - **direct_object:** CASE_PLUS_SYSTEM_COUNTEREVIDENCE
    - **gap_type:** GENERALIZATION
    - **independent_families:** 3
  - **item 6:**
    - **claim_id:** CLM-006
    - **direct_object:** MODEL_CEILING
    - **gap_type:** CAUSALITY
    - **independent_families:** 5
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** PARLIAMENT+ADMINISTRATION+AUDIT
  - **perspective:** PROCUREMENT+DECISION_PREPARATION+IMPLEMENTATION+OVERSIGHT
  - **stratification:** MISSION_CASES+SYSTEM_GOVERNANCE
  - **temporal:** 2017-2026
- **edi:**
  - **assessment:** MULTI_FAMILY_CASE_SPECIFIC_DECISION_AND_IMPLEMENTATION_CONTROL
  - **flags:**
    - MARGINAL_CAUSALITY_GAP
    - SYSTEMIC_DEPENDENCE_DENOMINATOR_GAP
    - AUTHORSHIP_TRACE_GAP
- **source_counts:**
  - **primary:** 16
  - **provenance_families:** 5
  - **secondary:** 0
  - **tertiary:** 0
  - **total:** 16

### RESPONSIBILITY_MAP
- **boundary:** Consultant influence on preparation or implementation is not equivalent to formal or causal displacement of responsible public authorities.
- **not_established:**
  - consultants generally make sovereign political decisions
  - McKinsey made vaccination policy decisions
  - contract value predicts influence or public value
  - persistent whole-of-state cognitive dependence
  - generalized sovereignty loss caused by consulting
- **verified:**
  - consultants can materially contribute to decision preparation
  - consultants contributed operationally to vaccination and telework cases
  - administrations can edit/reject consultant proposals
  - post-2022 governance and internalisation measures were implemented

### NEXT_QUERIES
- versioned before/after records linking consultant recommendations to named policy choices
- mission-level outcome evaluations with rejected/unused deliverables as controls
- cross-ministry denominator of consulting use, internal capability and transfer-back
- authenticated records of consultant tasking or decision-maker dependence where sovereignty delegation is alleged

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023,QRY-024,QRY-025,QRY-026,QRY-027 | support:- | counter:- | results:FCT-001,FCT-002,FCT-020,FCT-021,FCT-022,FCT-023,FCT-024,FCT-025,FCT-026,FCT-027,FCT-028 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023,QRY-024,QRY-025,QRY-026,QRY-027 | support:- | counter:- | results:FCT-003,FCT-004,FCT-005,FCT-006,FCT-019,FCT-020 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023,QRY-024,QRY-025,QRY-026,QRY-027 | support:- | counter:- | results:FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,FCT-019 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023,QRY-024,QRY-025,QRY-026,QRY-027 | support:- | counter:- | results:FCT-002,FCT-003,FCT-010,FCT-012,FCT-013,FCT-014,FCT-016,FCT-019,FCT-022,FCT-023,FCT-024,FCT-025,FCT-028 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-012,QRY-014,QRY-015,QRY-019,SRC-001,SRC-003,SRC-004,SRC-008 | support:FCT-001,FCT-006,FCT-007,FCT-008,FCT-018 | counter:FCT-002,FCT-004 | results:FCT-001,FCT-006,FCT-007,FCT-008,FCT-018,FCT-002,FCT-004 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-014,QRY-016,SRC-003,SRC-005 | support:FCT-005,FCT-009,FCT-010,FCT-011,FCT-012 | counter:FCT-004 | results:FCT-005,FCT-009,FCT-010,FCT-011,FCT-012,FCT-004 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-018,SRC-007 | support:FCT-015,FCT-016,FCT-017 | counter:- | results:FCT-015,FCT-016,FCT-017 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-012,QRY-017,QRY-018,SRC-001,SRC-006,SRC-007 | support:FCT-013,FCT-014 | counter:FCT-001,FCT-017 | results:FCT-013,FCT-014,FCT-001,FCT-017 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-012,QRY-016,QRY-023,QRY-024,SRC-001,SRC-005,SRC-012,SRC-013 | support:FCT-012,FCT-023,FCT-024,FCT-025 | counter:FCT-002,FCT-010 | results:FCT-012,FCT-023,FCT-024,FCT-025,FCT-002,FCT-010 | final:PARTIAL | gap:GENERALIZATION
CLM-006 | attempts:QRY-012,QRY-013,QRY-014,QRY-016,QRY-018,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023,QRY-024,QRY-025,QRY-027,SRC-001,SRC-002,SRC-003,SRC-005,SRC-007,SRC-008,SRC-009,SRC-010,SRC-011,SRC-012,SRC-013,SRC-014,SRC-016 | support:FCT-003,FCT-004,FCT-005,FCT-010,FCT-016,FCT-020,FCT-021,FCT-022,FCT-023,FCT-025,FCT-026,FCT-028 | counter:FCT-001,FCT-006,FCT-012,FCT-019 | results:FCT-003,FCT-004,FCT-005,FCT-010,FCT-016,FCT-020,FCT-021,FCT-022,FCT-023,FCT-025,FCT-026,FCT-028,FCT-001,FCT-006,FCT-012,FCT-019 | final:PARTIAL | gap:CAUSALITY

## STATUS_DELTA_V1
DELTA-001 | AXS-001 | OPEN | SATURATED | axis saturated by current multi-case corpus
DELTA-002 | AXS-002 | OPEN | SATURATED | axis saturated by current multi-case corpus
DELTA-003 | AXS-003 | OPEN | SATURATED | axis saturated by current multi-case corpus
DELTA-004 | AXS-004 | OPEN | SATURATED | axis saturated by current multi-case corpus

## OPEN_GAPS_V1
CLM-005 | CLM | PARTIAL | GENERALIZATION | The inspected record does not provide a denominator or causal design establishing persistent whole-of-state cognitive dependence across ministries and policy domains.
CLM-006 | CLM | PARTIAL | CAUSALITY | A sovereignty-delegation claim would require decision-specific evidence that consultant recommendations displaced or controlled the responsible public authority, plus a counterfactual showing the public decision depended on that displacement.
CAU-004 | CAU | UNRESOLVED | CAUSALITY | Direct consequences could not be determined and the deliverables were only one source among others.
CAU-005 | CAU | UNRESOLVED | CAUSALITY | No inspected cross-ministry causal design establishes consultant control as the marginal cause of sovereign policy choices.

SEMANTIC_COUNTS_V1:LED:0|CLM:6|AXS:4|CAU:5|CTRL:8|ACT:4

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"External consulting materially entered preparation of major French public reforms and could shape decision scenarios, but contract existence alone does not establish influence on the final decision.","claimant":"INV-062 synthesis","counter":["FCT-002","FCT-004"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-006","FCT-007","FCT-008","FCT-018"]}
CLM-002 | {"claim":"In the inspected vaccination case, McKinsey had a sustained operational role and contributed to at least one ministry document, while ministerial/DGS authority and later transfer back to the state task force remained documented.","claimant":"INV-062 synthesis","counter":["FCT-004"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-005","FCT-009","FCT-010","FCT-011","FCT-012"]}
CLM-003 | {"claim":"The telework case closes a consultant-supported output-to-implementation edge, but also shows administration editing, rejection of proposals and opaque attribution rather than autonomous consultant control.","claimant":"INV-062 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-015","FCT-016","FCT-017"]}
CLM-004 | {"claim":"Consulting mission value and spending do not reliably predict policy effect: the teacher-profession mission had no demonstrated need/value added and its direct consequences could not be determined.","claimant":"INV-062 synthesis","counter":["FCT-001","FCT-017"],"gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-013","FCT-014"]}
CLM-005 | {"claim":"A case-specific dependence risk is documented in vaccination organisation, but the corpus also documents reversibility, declining external orders and deliberate rebuilding of internal consulting capability after 2022.","claimant":"INV-062 synthesis","counter":["FCT-002","FCT-010"],"gap":"The inspected record does not provide a denominator or causal design establishing persistent whole-of-state cognitive dependence across ministries and policy domains.","gap_type":"GENERALIZATION","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-012","FCT-023","FCT-024","FCT-025"]}
CLM-006 | {"claim":"The strongest supported ceiling is material external influence on preparation and implementation in some missions, not a demonstrated generalized delegation of sovereign political decision-making to consulting firms.","claimant":"INV-062 synthesis","counter":["FCT-001","FCT-006","FCT-012","FCT-019"],"gap":"A sovereignty-delegation claim would require decision-specific evidence that consultant recommendations displaced or controlled the responsible public authority, plus a counterfactual showing the public decision depended on that displacement.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-003","FCT-004","FCT-005","FCT-010","FCT-016","FCT-020","FCT-021","FCT-022","FCT-023","FCT-025","FCT-026","FCT-028"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018","QRY-019","QRY-020","QRY-021","QRY-022","QRY-023","QRY-024","QRY-025","QRY-026","QRY-027"],"axis":"scale and governance","links":["OBJECT_QUESTION"],"question":"What scale, procurement and governance mechanisms of external consulting are documented, and what changed after 2022?","result_ids":["FCT-001","FCT-002","FCT-020","FCT-021","FCT-022","FCT-023","FCT-024","FCT-025","FCT-026","FCT-027","FCT-028"],"sought_objects":["spending","procurement","controls","internalisation"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018","QRY-019","QRY-020","QRY-021","QRY-022","QRY-023","QRY-024","QRY-025","QRY-026","QRY-027"],"axis":"decision penetration","links":["OBJECT_QUESTION"],"question":"Where do consultants enter decision preparation, and which evidence separates recommendation from political decision?","result_ids":["FCT-003","FCT-004","FCT-005","FCT-006","FCT-019","FCT-020"],"sought_objects":["scenario design","filtering","ministerial responsibility","major reforms"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018","QRY-019","QRY-020","QRY-021","QRY-022","QRY-023","QRY-024","QRY-025","QRY-026","QRY-027"],"axis":"case-specific effects","links":["OBJECT_QUESTION"],"question":"Which missions show identifiable contribution to implementation or public outputs, and which show weak/no follow-up?","result_ids":["FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018","FCT-019"],"sought_objects":["APL","vaccination","telework","central administration","teacher","CNAV"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018","QRY-019","QRY-020","QRY-021","QRY-022","QRY-023","QRY-024","QRY-025","QRY-026","QRY-027"],"axis":"dependence and sovereignty","links":["OBJECT_QUESTION"],"question":"What evidence supports or falsifies recurring dependence, opacity or loss of internal capability?","result_ids":["FCT-002","FCT-003","FCT-010","FCT-012","FCT-013","FCT-014","FCT-016","FCT-019","FCT-022","FCT-023","FCT-024","FCT-025","FCT-028"],"sought_objects":["transfer of activities","internal skills","traceability","counterfactual capability"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"The Senate directly documents substantive positions, oriented/turnkey scenarios and involvement in major reforms.","counter":["FCT-002","FCT-004"],"limit":"Decision preparation is established; marginal causal contribution to the final political choice is not generally isolated.","mechanism":"strategy consulting mission -> substantive scenarios/recommendations -> public decision preparation","status":"SUPPORTED","support":["FCT-001","FCT-006","FCT-007"]}
CAU-002 | {"causal_right":"Mission duration/orders, document contribution and transfer of activities to the task force directly connect consulting work to campaign operations.","counter":["FCT-005"],"limit":"Operational contribution and temporary dependence do not establish that McKinsey made health-policy or vaccination decisions.","mechanism":"McKinsey vaccination support -> operational organisation/document contribution -> state vaccination campaign execution","status":"SUPPORTED","support":["FCT-009","FCT-010","FCT-011","FCT-012"]}
CAU-003 | {"causal_right":"The administration documented consultant work, substantial internal editing and subsequent official referral to the resulting kit.","counter":"NONE_FOUND","limit":"The edge reaches implementation of a shared output; consultant marginal authorship and independent control are not established.","mechanism":"consulting-supported telework drafting -> administration editing/rejection -> published guide -> circular referral -> administrative implementation","status":"SUPPORTED","support":["FCT-015","FCT-016","FCT-017"]}
CAU-004 | {"counter":"NONE_FOUND","gap":"Direct consequences could not be determined and the deliverables were only one source among others.","gap_type":"CAUSALITY","limit":"No inspected evidence identifies a direct policy consequence attributable to the mission.","mechanism":"teacher-profession consulting mission -> deliverables -> identifiable education-policy change","status":"UNRESOLVED","support":["FCT-013","FCT-014"]}
CAU-005 | {"counter":["FCT-003","FCT-010","FCT-016","FCT-021","FCT-023","FCT-024","FCT-025"],"gap":"No inspected cross-ministry causal design establishes consultant control as the marginal cause of sovereign policy choices.","gap_type":"CAUSALITY","limit":"Dependence indicators exist case-specifically; generalized decision displacement is not demonstrated and post-2022 controls/internalisation provide counter-evidence.","mechanism":"external consulting at scale -> loss of internal capability/dependence -> consultant control of sovereign policy decision","status":"UNRESOLVED","support":["FCT-002","FCT-012","FCT-019"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"consulting != decision","status":"DONE","support":["FCT-004","FCT-005"]}
CTRL-002 | {"control":"recommendation != adoption","status":"DONE","support":["FCT-001","FCT-014","FCT-019"]}
CTRL-003 | {"control":"contract value != influence","status":"DONE","support":["FCT-002","FCT-013","FCT-014"]}
CTRL-004 | {"control":"similarity or contribution != autonomous authorship","status":"DONE","support":["FCT-011","FCT-015","FCT-016","FCT-019"]}
CTRL-005 | {"control":"outsourcing != sovereignty loss by default","status":"DONE","support":["FCT-003","FCT-010","FCT-020","FCT-023","FCT-025"]}
CTRL-006 | {"control":"chronology != causality","status":"DONE","support":["FCT-014","FCT-019"]}
CTRL-007 | {"control":"case-specific dependence != permanent systemic dependence","status":"DONE","support":["FCT-012","FCT-024","FCT-025"]}
CTRL-008 | {"control":"audit criticism != uncontested truth","status":"DONE","support":["FCT-026","FCT-027"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"require attributable versioning of consultant contributions in material administrative documents and reform deliverables","actor":"administrations / contracting authorities","intent":"make consultant contribution, internal edits and final public authorship reconstructable","status":"OPEN","support":["FCT-015","FCT-016","FCT-019","FCT-028"]}
ACT-002 | {"action":"evaluate major consulting missions against predefined need, internal-capability, deliverable-use and outcome criteria","actor":"ministries / procurement control / audit bodies","intent":"separate purchased activity from demonstrable public value and policy effect","status":"OPEN","support":["FCT-013","FCT-014","FCT-020","FCT-022","FCT-023"]}
ACT-003 | {"action":"maintain longitudinal measures of external spend, internal consulting capacity and transfer-back of mission functions","actor":"DITP / ministries / Cour des comptes / Parliament","intent":"test persistent dependence rather than infer it from selected contracts","status":"OPEN","support":["FCT-010","FCT-012","FCT-024","FCT-025","FCT-026"]}
ACT-004 | {"action":"reopen generalized sovereignty-delegation claim only on decision-specific tasking/control evidence or a credible causal design showing consultant displacement of public authority","actor":"future investigation","intent":"preserve the causal ceiling and avoid converting influence evidence into sovereignty-loss proof","status":"OPEN","support":["FCT-004","FCT-005","FCT-006","FCT-019"]}

SEARCH_ACTIVITY_V1:WEB:11|FETCH:16|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL | MNEMO | MNEMO_UNAVAILABLE | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | PASS | - | - | French Senate consulting firms public policy influence 2022 report outcomes
QRY-002 | WEB | PASS | - | - | McKinsey vaccination France Senate 11.63 million transfer task force
QRY-003 | WEB | PASS | - | - | McKinsey APL reform France 3.88 million Senate technical defect
QRY-004 | WEB | PASS | - | - | McKinsey teacher profession 500000 no demonstrated value Senate
QRY-005 | WEB | PASS | - | - | McKinsey telework guide Alixio DITP Senate
QRY-006 | WEB | PASS | - | - | McKinsey Accenture central administration reorganisation 617388 Senate
QRY-007 | WEB | PASS | - | - | Cour des comptes State intellectual consulting 2023 dependence internal skills
QRY-008 | WEB | PASS | - | - | Assemblée nationale outsourcing cabinets conseil autonomy 2022
QRY-009 | WEB | PASS | - | - | France government internal consulting agency 2024 expenditure 271 80 million
QRY-010 | WEB | PASS | - | - | French law proposal consulting transparency contributions documents 2024
QRY-011 | WEB | PASS | - | - | French consulting public contracts 500000 committee approval 2024
QRY-012 | FETCH | PASS | SRC-001 | https://www.senat.fr/rap/r21-578-1/r21-578-111.html | -
QRY-013 | FETCH | PASS | SRC-002 | https://www.senat.fr/rap/r21-578-1/r21-578-112.html | -
QRY-014 | FETCH | PASS | SRC-003 | https://www.senat.fr/rap/r21-578-1/r21-578-114.html | -
QRY-015 | FETCH | PASS | SRC-004 | https://www.senat.fr/rap/r21-578-1/r21-578-115.html | -
QRY-016 | FETCH | PASS | SRC-005 | https://www.senat.fr/rap/r21-578-1/r21-578-124.html | -
QRY-017 | FETCH | PASS | SRC-006 | https://www.senat.fr/rap/r21-578-1/r21-578-125.html | -
QRY-018 | FETCH | PASS | SRC-007 | https://www.senat.fr/rap/r21-578-1/r21-578-126.html | -
QRY-019 | FETCH | PASS | SRC-008 | https://www.senat.fr/rap/r21-578-1/r21-578-128.html | -
QRY-020 | FETCH | PASS | SRC-009 | https://www.assemblee-nationale.fr/dyn/opendata/RINFANR5L15B4928.html | -
QRY-021 | FETCH | PASS | SRC-010 | https://www.assemblee-nationale.fr/dyn/opendata/RAPPANR5L16B2112.html | -
QRY-022 | FETCH | PASS | SRC-011 | https://questions.assemblee-nationale.fr/q16/16-11307QE.htm | -
QRY-023 | FETCH | PASS | SRC-012 | https://questions.assemblee-nationale.fr/q16/16-10031QE.htm | -
QRY-024 | FETCH | PASS | SRC-013 | https://www.transformation.gouv.fr/files/presse/cp-renfort-competences-agence-conseil-interne.pdf | -
QRY-025 | FETCH | PASS | SRC-014 | https://www.ccomptes.fr/fr/publications/le-recours-par-letat-aux-prestations-intellectuelles-de-cabinets-de-conseil | -
QRY-026 | FETCH | PASS | SRC-015 | https://www.ccomptes.fr/system/files/2023-07/20230710-reponses-Recours-par-Etat-aux-prestations-intellectuelles-cabinets-conseil.pdf | -
QRY-027 | FETCH | PASS | SRC-016 | https://www.senat.fr/rap/l23-615/l23-6157.html | -

## EVIDENCE_REGISTRY
SRC-001 | ◉ | fam:A | SENAT-R578-P111 | Sénat inquiry - heterogeneous outcomes | 2022-03-16 | 2026-09-09 | report p111 outcomes and influence | https://www.senat.fr/rap/r21-578-1/r21-578-111.html
SRC-002 | ◉ | fam:A | SENAT-R578-P112 | Sénat inquiry - CNAV internal follow-up | 2022-03-16 | 2026-09-09 | report p112 CNAV and internal skills | https://www.senat.fr/rap/r21-578-1/r21-578-112.html
SRC-003 | ◉ | fam:A | SENAT-R578-P114 | Sénat inquiry - consultants and public decision | 2022-03-16 | 2026-09-09 | report p114 decision boundary | https://www.senat.fr/rap/r21-578-1/r21-578-114.html
SRC-004 | ◉ | fam:A | SENAT-R578-P115 | Sénat inquiry - major reforms and consulting | 2022-03-16 | 2026-09-09 | report p115 major reforms | https://www.senat.fr/rap/r21-578-1/r21-578-115.html
SRC-005 | ◉ | fam:A | SENAT-R578-P124 | Sénat inquiry - vaccination case | 2022-03-16 | 2026-09-09 | report p124 vaccination | https://www.senat.fr/rap/r21-578-1/r21-578-124.html
SRC-006 | ◉ | fam:A | SENAT-R578-P125 | Sénat inquiry - teacher profession case | 2022-03-16 | 2026-09-09 | report p125 teacher mission | https://www.senat.fr/rap/r21-578-1/r21-578-125.html
SRC-007 | ◉ | fam:A | SENAT-R578-P126 | Sénat inquiry - telework guide case | 2022-03-16 | 2026-09-09 | report p126 telework guide | https://www.senat.fr/rap/r21-578-1/r21-578-126.html
SRC-008 | ◉ | fam:A | SENAT-R578-P128 | Sénat inquiry - central administration reorganisation | 2022-03-16 | 2026-09-09 | report p128 central administration | https://www.senat.fr/rap/r21-578-1/r21-578-128.html
SRC-009 | ◈ | fam:D | AN-RINF-4928 | Assemblée nationale outsourcing report 4928 | 2022-01-19 | 2026-09-09 | outsourcing doctrine and autonomy | https://www.assemblee-nationale.fr/dyn/opendata/RINFANR5L15B4928.html
SRC-010 | ◈ | fam:D | AN-RAPP-2112 | Assemblée nationale consulting regulation report 2112 | 2024-01-24 | 2026-09-09 | post-inquiry controls and transparency | https://www.assemblee-nationale.fr/dyn/opendata/RAPPANR5L16B2112.html
SRC-011 | ◈ | fam:B | AN-QE-11307 | Government answer on consulting controls | 2024-01-02 | 2026-09-09 | government control and internalisation measures | https://questions.assemblee-nationale.fr/q16/16-11307QE.htm
SRC-012 | ◈ | fam:B | AN-QE-10031 | Government answer on internalisation priority | 2024-01-02 | 2026-09-09 | last-resort doctrine and internalisation | https://questions.assemblee-nationale.fr/q16/16-10031QE.htm
SRC-013 | ◈ | fam:E | DITP-ACI-2024 | DITP - internal consulting agency launch | 2024-03-26 | 2026-09-09 | internal consulting agency and expenditure reduction | https://www.transformation.gouv.fr/files/presse/cp-renfort-competences-agence-conseil-interne.pdf
SRC-014 | ◈ | fam:C | CDC-CONSEIL-2023 | Cour des comptes - State consulting services | 2023-07-10 | 2026-09-09 | state consulting control report | https://www.ccomptes.fr/fr/publications/le-recours-par-letat-aux-prestations-intellectuelles-de-cabinets-de-conseil
SRC-015 | ◈ | fam:C | CDC-CONSEIL-RESP-2023 | Cour des comptes - administration responses | 2023-07-10 | 2026-09-09 | administration responses to Cour report | https://www.ccomptes.fr/system/files/2023-07/20230710-reponses-Recours-par-Etat-aux-prestations-intellectuelles-cabinets-conseil.pdf
SRC-016 | ◈ | fam:E | SENAT-L23-615-P7 | Sénat 2024 consulting transparency provisions | 2024-05-22 | 2026-09-09 | traceability of consultant contributions | https://www.senat.fr/rap/l23-615/l23-6157.html

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.senat.fr/rap/r21-578-1/r21-578-111.html | A | 2026-09-09 | Consulting outcomes are heterogeneous | The Senate inquiry states that some consulting missions produced no tangible follow-up while others directly influenced public policies, especially strategy missions presenting decision scenarios. | -
FCT-002 | FACT | ✧ | https://www.senat.fr/rap/r21-578-1/r21-578-111.html | A | 2026-09-09 | Administrative steering capacity is itself a control variable | The Senate inquiry found large differences in ministries ability to steer consultants and noted a shortage of project managers, making contract existence insufficient to infer influence. | -
FCT-003 | FACT | ✧ | https://www.senat.fr/rap/r21-578-1/r21-578-112.html | A | 2026-09-09 | CNAV provides a negative control on durable consulting effect | After a consulting-supported transformation reflection, CNAV launched Retraite 2025 in 2021 using internal competences rather than consulting firms. | -
FCT-004 | FACT | ✧ | https://www.senat.fr/rap/r21-578-1/r21-578-114.html | A | 2026-09-09 | Government and senior officials explicitly retain political decision responsibility | Audition evidence compiled by the Senate consistently states that political authority remains responsible for decisions and consultants operate upstream or downstream. | -
FCT-005 | FACT | ✧ | https://www.senat.fr/rap/r21-578-1/r21-578-114.html | A | 2026-09-09 | Olivier Véran denied direct McKinsey decision-taking | Véran told the inquiry that McKinsey never made him take a decision on the health crisis or vaccination and that work passed through the DGS filter. | -
FCT-006 | FACT | ✧ | https://www.senat.fr/rap/r21-578-1/r21-578-114.html | A | 2026-09-09 | Senate inquiry identifies a blurrier practical boundary | The Senate report concludes that in practice strategy consultants can take substantive positions, work on major reforms and present turnkey or oriented scenarios. | -
FCT-007 | FACT | ✧ | https://www.senat.fr/rap/r21-578-1/r21-578-115.html | A | 2026-09-09 | Consultants intervened on several major reforms | The Senate lists legal aid, unemployment bonus-malus, disability rights, vocational training and the APL reform among major reforms involving consulting firms. | -
FCT-008 | FACT | ✧ | https://www.senat.fr/rap/r21-578-1/r21-578-115.html | A | 2026-09-09 | APL consulting spend was material | The Senate identifies McKinsey work on the APL reform from 2018-2020 for EUR 3.88 million. | -
FCT-009 | FACT | ✧ | https://www.senat.fr/rap/r21-578-1/r21-578-124.html | A | 2026-09-09 | Vaccination mission became long and repeated | The Senate reports seven McKinsey vaccination orders totaling EUR 11.63 million and a mission lasting more than a year. | -
FCT-010 | FACT | ✧ | https://www.senat.fr/rap/r21-578-1/r21-578-124.html | A | 2026-09-09 | Vaccination activities were transferred back to the state task force | The Senate documents a summer-2021 transition transferring McKinsey activities to the vaccine task force, which then managed the campaign alone until a later temporary recall. | -
FCT-011 | FACT | ✧ | https://www.senat.fr/rap/r21-578-1/r21-578-124.html | A | 2026-09-09 | McKinsey contributed to ministry vaccination documents | Olivier Véran acknowledged during Senate hearings that McKinsey contributed to drafting at least one ministry document while maintaining that the document and decision remained ministerial. | -
FCT-012 | FACT | ✧ | https://www.senat.fr/rap/r21-578-1/r21-578-124.html | A | 2026-09-09 | Vaccination dependence claim is case-specific rather than universal | The Senate characterises a form of dependence in the vaccination organisation, but the documented transfer back to the task force shows reversibility and continued state supervision. | -
FCT-013 | FACT | ✧ | https://www.senat.fr/rap/r21-578-1/r21-578-125.html | A | 2026-09-09 | Teacher-profession mission is a strong negative control | The Senate found the nearly EUR 500,000 McKinsey teacher-profession mission had no demonstrated need and no demonstrated value added. | -
FCT-014 | FACT | ✧ | https://www.senat.fr/rap/r21-578-1/r21-578-125.html | A | 2026-09-09 | Teacher deliverables had no identifiable direct policy consequence | The Education Ministry said the direct consequences of the teacher mission deliverables could not be determined; some were only one source among others. | -
FCT-015 | FACT | ✧ | https://www.senat.fr/rap/r21-578-1/r21-578-126.html | A | 2026-09-09 | Telework guide had an undisclosed consulting contribution | The public telework guide did not mention the role of consulting firms although McKinsey held the contract and Alixio performed the work. | -
FCT-016 | FACT | ✧ | https://www.senat.fr/rap/r21-578-1/r21-578-126.html | A | 2026-09-09 | Telework guide shows administrative editing and rejection | DITP and DGAFP supplied source material, substantially edited drafts and rejected some consultant proposals, demonstrating contribution without autonomous control. | -
FCT-017 | FACT | ✧ | https://www.senat.fr/rap/r21-578-1/r21-578-126.html | A | 2026-09-09 | Telework output entered an official implementation chain | A government circular referred managers to the telework good-practice kit, creating a traceable consultant-supported output to administrative implementation edge. | -
FCT-018 | FACT | ✧ | https://www.senat.fr/rap/r21-578-1/r21-578-128.html | A | 2026-09-09 | Central-administration reorganisation involved McKinsey and Accenture | DITP hired McKinsey and Accenture for EUR 617,388 to support the 2018 central-administration reorganisation process. | -
FCT-019 | FACT | ✧ | https://www.senat.fr/rap/r21-578-1/r21-578-128.html | A | 2026-09-09 | Central-administration case shows deep process involvement with attribution uncertainty | The Senate found consultants involved in guidance and counter-expertise but said their precise role was difficult to reconstruct, preventing confident marginal authorship of later reforms. | -
FCT-020 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/opendata/RINFANR5L15B4928.html | D | 2026-09-09 | Assemblée nationale treats outsourcing as neither inherently good nor bad | The 2022 Assembly report frames utility, governance, monitoring and evaluation as the relevant criteria rather than treating externalisation itself as proof of capture. | -
FCT-021 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/opendata/RAPPANR5L16B2112.html | D | 2026-09-09 | Post-2022 controls formalised a last-resort and traceability doctrine | The 2024 Assembly legislative report records the 2022 circular, ministry engagement controls, internalisation measures and rules identifying consultants as external providers. | -
FCT-022 | FACT | ✧ | https://questions.assemblee-nationale.fr/q16/16-11307QE.htm | B | 2026-09-09 | Government describes a three-level internal control system | The January 2024 government answer describes administration-level compliance, secretary-general control and central spending oversight, with additional approval for large orders. | -
FCT-023 | FACT | ✧ | https://questions.assemblee-nationale.fr/q16/16-10031QE.htm | B | 2026-09-09 | External consulting is formally a last-resort option | The government states that the 2022 circular requires checking whether internal competences can satisfy the need before using external consulting. | -
FCT-024 | FACT | ✧ | https://www.transformation.gouv.fr/files/presse/cp-renfort-competences-agence-conseil-interne.pdf | E | 2026-09-09 | External strategy/organisation consulting orders fell after 2021 | DITP stated in March 2024 that external consulting orders fell from EUR 271 million in 2021 to EUR 137 million in 2022 and EUR 80 million in 2023. | -
FCT-025 | FACT | ✧ | https://www.transformation.gouv.fr/files/presse/cp-renfort-competences-agence-conseil-interne.pdf | E | 2026-09-09 | The State created an internal consulting agency | DITP launched an internal State consulting agency in March 2024, with 53 agents then and a target of 75 by end-2024, explicitly to internalise capabilities. | -
FCT-026 | FACT | ✧ | https://www.ccomptes.fr/fr/publications/le-recours-par-letat-aux-prestations-intellectuelles-de-cabinets-de-conseil | C | 2026-09-09 | Cour des comptes created an independent control layer on consulting | The Cour des comptes published a dedicated 2023 control on State use of intellectual consulting services, adding an external audit perspective to parliamentary and government accounts. | -
FCT-027 | FACT | ✧ | https://www.ccomptes.fr/system/files/2023-07/20230710-reponses-Recours-par-Etat-aux-prestations-intellectuelles-cabinets-conseil.pdf | C | 2026-09-09 | Administrations formally responded to the Cour des comptes findings | The Cour published administration responses alongside its 2023 consulting report, preserving institutional contradiction rather than treating the audit report as uncontested truth. | -
FCT-028 | FACT | ✧ | https://www.senat.fr/rap/l23-615/l23-6157.html | E | 2026-09-09 | Legislative follow-up targets attribution opacity | The 2024 Senate legislative report proposes explicit identification of consultants and their contributions in documents produced for administrations, directly addressing invisible authorship risk. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-002
FCT-004 | SRC-003
FCT-005 | SRC-003
FCT-006 | SRC-003
FCT-007 | SRC-004
FCT-008 | SRC-004
FCT-009 | SRC-005
FCT-010 | SRC-005
FCT-011 | SRC-005
FCT-012 | SRC-005
FCT-013 | SRC-006
FCT-014 | SRC-006
FCT-015 | SRC-007
FCT-016 | SRC-007
FCT-017 | SRC-007
FCT-018 | SRC-008
FCT-019 | SRC-008
FCT-020 | SRC-009
FCT-021 | SRC-010
FCT-022 | SRC-011
FCT-023 | SRC-012
FCT-024 | SRC-013
FCT-025 | SRC-013
FCT-026 | SRC-014
FCT-027 | SRC-015
FCT-028 | SRC-016

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

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:search
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:facts
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:causal
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:verify
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:accountability
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:narrative

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-09T15:25:57.199226+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":28,"eligible":28,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:28;attempted:0;success:0;failure:0;blocked:28} | WRITEBACK_EXECUTION_V1:[28 rows, see section]

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
