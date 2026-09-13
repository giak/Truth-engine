ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260909-1037-dsa-information-governance | PARENT_RUN_ID:NONE | AS_OF:2026-09-09
INPUT_KIND:RUN_CARD | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/inv043/runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-09_dsa-information-governance/2026-09-09_10-37_dsa-information-governance_INPUT.md | SUBJECT_SLUG:dsa-information-governance | SUBJECT_FP:sha256:a23eeb3bfe718e6e5c113d1b955b4832d2c9cae6aca9f7382ca92660ddb806d5 | INPUT_SHA256:sha256:0e1977ef0bf71a60b7067158a5f0b8dd38b03248ef05c92361e5f71ad59f93bb
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:European Union, mainly 2022-2026; trace DSA rule/obligation -> platform or intermediary/authority -> moderation, recommendation or risk-mitigation action -> visibility/availability -> appeal/oversight -> measured behavioural or democratic effect, separating legal duty, execution, platform decision, state order, censorship and causal outcome.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/NETWORK.md,clusters/POWER.md,clusters/CONFIRMATION.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# DSA : gouvernance informationnelle, obligations réelles et plafond causal

## Résultat central

Le Digital Services Act ne constitue pas un mécanisme unique de retrait de contenus. Le corpus distingue au moins quatre chaînes juridiques et opérationnelles : les injonctions judiciaires ou administratives, le notice-and-action ordinaire, les signalements prioritaires des signaleurs de confiance, et la supervision systémique des très grandes plateformes. Ces chaînes ont des autorités, des seuils et des effets différents. [FCT-001][FCT-002][FCT-003][FCT-007][FCT-008][FCT-012]

Le point le plus discriminant concerne les signaleurs de confiance : leur notification bénéficie d'une priorité de traitement, mais elle ne vaut pas automatiquement ordre étatique de retrait. L'Arcom indique que la plateforme retire ou bloque si elle partage l'analyse d'illicéité ; elle peut contester le caractère manifestement illicite. `trusted flagger -> priority review` est donc vérifié, mais `trusted flagger -> automatic state removal` ne l'est pas. [FCT-007][FCT-008][FCT-009]

## Transparence et recours

Le DSA transforme fortement l'observabilité de la modération. Les décisions de retrait, rétrogradation, démonétisation, restriction de visibilité ou de compte doivent être motivées ; une base publique agrège les exposés des motifs, et des voies internes puis extrajudiciaires permettent de contester les décisions. [FCT-004][FCT-005][FCT-006][FCT-015]

Ces recours ne sont pas symboliques. Depuis 2024, plus de 165 millions de décisions de VLOP/VLOSE ont fait l'objet d'un recours interne dans l'UE et près de 30 % ont été renversées selon la Commission. Au premier semestre 2025, les organismes extrajudiciaires ont renversé 52 % des dossiers clos sur Facebook, Instagram et TikTok. L'Appeals Centre Europe rapporte lui aussi des renversements fréquents, tout en documentant des limites de coopération des plateformes. [FCT-017][FCT-018][FCT-019][FCT-020][FCT-021]

La conclusion probatoire est étroite : `moderation -> appeal -> reversal/restoration` est réel dans de nombreux cas ; cela ne démontre ni que toute décision initiale était illégale, ni que le système améliore globalement la liberté d'expression.

## Qui décide réellement de la majorité des modérations ?

Un contrôle négatif est déterminant. Pour le premier semestre 2025, la Commission indique que plus de neuf milliards de décisions de modération ont été déclarées et que 99 % étaient prises proactivement sur la base des propres conditions générales des plateformes ; seule une fraction marginale provenait de signalements de contenus illégaux. [FCT-016]

Cela n'exonère pas le DSA de toute influence : le règlement structure les procédures, la transparence, les recours, les systèmes de recommandation et les obligations de risque. Mais cela interdit d'attribuer mécaniquement la masse des retraits ou déclassements au régulateur européen.

## Risques systémiques, recommandation et enforcement

Pour les très grandes plateformes et moteurs, le DSA impose des évaluations et mesures de mitigation sur des risques incluant processus électoraux et discours civique, ainsi que de la transparence et du contrôle sur les systèmes de recommandation. La Commission a ouvert des procédures concernant Meta, TikTok, X et Shein, et elle a obtenu ou imposé des changements concrets dans certains dossiers. [FCT-010][FCT-011][FCT-012][FCT-013][FCT-022][FCT-023][FCT-024][FCT-025][FCT-026][FCT-027]

Il faut cependant préserver la hiérarchie des preuves : une demande d'information n'est pas une conclusion ; l'ouverture d'une procédure n'est pas une constatation d'infraction ; une obligation d'évaluer un risque n'est pas un ordre de supprimer un point de vue ; une mesure corrective de transparence n'est pas un retrait de contenu. [FCT-022][FCT-023][FCT-024][FCT-025][FCT-027]

## Ce que les données permettent de mesurer

La base DSA crée un niveau d'observabilité sans précédent, mais ses limites sont documentées. Une étude FAccT sur 131 millions d'exposés des motifs conclut à des gains de transparence tout en identifiant de fortes marges de discrétion et des problèmes de conformité/comparabilité. Une analyse de 439 millions d'enregistrements constate une modération très automatisée et des stratégies différentes selon les plateformes. [FCT-028][FCT-030]

Surtout, l'étude de 1,58 milliard d'actions autour des élections européennes de 2024 ne détecte pas de changement significatif des comportements d'enforcement autour du scrutin, tout en rappelant les limites de la base. Ce résultat ne prouve pas une absence d'effet du DSA ; il ferme seulement l'inférence simple `élection + DSA -> durcissement observable de la modération`. [FCT-029]

Les options de contrôle des recommandations offrent un autre séparateur : leur disponibilité ne garantit pas leur utilisation. Une étude expérimentale de 2026 constate que les utilisateurs utilisent peu les contrôles sans incitation, même si une conception transparente augmente le sentiment de contrôle. Aucun effet sur opinions ou résultats électoraux n'y est identifié. [FCT-031]

## Verdict forensique

1. `DSA -> procédures de notification, transparence, recours et supervision` : **VERIFIED**.
2. `trusted flagger -> traitement prioritaire` : **VERIFIED**.
3. `trusted flagger -> ordre automatique de retrait` : **NOT_ESTABLISHED** ; canal distinct des injonctions publiques.
4. `DSA -> modifications de systèmes/processus de plateforme` : **VERIFIED case-specific** via obligations, commitments, sanctions ou corrections.
5. `DSA -> décision de modération individuelle` : **PARTIAL / mechanism-dependent**, avec une grande majorité des décisions enregistrées provenant des règles propres des plateformes.
6. `DSA -> changement général des opinions, du débat ou d'un résultat électoral` : **NOT_IDENTIFIED by this corpus**.
7. `DSA = dispositif neutre sans effet` : **NOT_SUPPORTED** non plus : il change les règles de gouvernance, l'observabilité, les voies de recours et certaines architectures de plateforme.

La bonne qualification n'est donc ni « le DSA ne fait rien », ni « Bruxelles décide directement ce qui peut être dit ». Le mécanisme réel est une gouvernance multiniveau qui modifie les incitations, procédures, contrôles et obligations des plateformes ; l'attribution d'un effet de censure ou d'un effet démocratique exige ensuite une chaîne décisionnelle et causale spécifique.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:6|SRC_COMPLETE:20/20

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-09
- **notes:**
  - general DSA application from 17 February 2024
  - enforcement status is case-specific and current through September 2026
  - academic moderation studies use 2023-2025 database periods
- **status:** CURRENT_WITH_HISTORICAL_ANTECEDENTS
- **window:** 2022-2026

### MANIPULATION_REPORT
- **assumptions:**
  - Commission impact statistics are administrative reporting, not independent causal estimates
  - Transparency Database is not a complete causal denominator
  - proceedings carry weaker evidentiary status than findings/decisions
- **clusters:**
  - **loaded:**
    - clusters/NETWORK.md
    - clusters/POWER.md
    - clusters/CONFIRMATION.md
- **complexity:**
  - **band:** HIGH
  - **score:** 9
- **implicit:**
  - regulation can alter systems without directly selecting content
  - private platform rules and public regulation can act simultaneously
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - notice
  - priority
  - moderation
  - transparency
  - appeal
  - recommender
  - systemic risk
  - enforcement
- **priorities:**
  - legal decision rights
  - moderation denominator
  - remedy reversals
  - political-effect ceiling
- **query_guidance:** separate regulatory duty from platform execution and content-level effect.
- **rhetorical:**
  - **AUTH:** official enforcement claims are bounded by procedural status
  - **BF:** selected proceedings are not prevalence estimates
  - **DEM:** speech-restrictive and speech-restorative mechanisms receive same causal standard
  - **FAC:** separate order, notice, priority, review, action, appeal and outcome
  - **NUM:** counts retain source period and denominator
- **speaker:**
  - **goal:** forensic causal discrimination
  - **target:** rule -> intermediary/authority -> platform action -> remedy -> effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **Κ:** 4
  - **Λ:** 4
  - **Ξ:** 4
  - **Σ:** 4
  - **Φ:** 4
  - **Ψ:** 4
  - **Ω:** 4
  - **κ:** 4
  - **ρ:** 4
  - **€:** 4
  - **↕:** 5
  - **⏰:** 5
  - **⚔:** 5
  - **⫸:** 4
  - **🌐:** 5
- **threats:**
  - DSA=all moderation
  - flagger=state order
  - proceeding=finding
  - risk=censorship
  - reversal=illegality
  - chronology=causality

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - named decision-specific state-to-platform chains
  - **input_ids:**
    - FCT-002
    - FCT-007
    - FCT-008
    - FCT-012
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no general automatic removal authority found for trusted flaggers
  - **not_computable:**
    - complete EU-wide decision-level network of every notice, order and moderation action
  - **operations:**
    - map decision rights among authorities, flaggers and platforms
  - **operations_applied:**
    - mapped DSA rule -> notifier/authority -> platform review/action boundaries
  - **reason:** the question requires mapping legal authority, designated intermediaries and platform decision rights
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CAU-001
  - **status:** DONE
  - **trigger:** 🌐
- **item 2:**
  - **gaps:**
    - content-level causal attribution of enforcement interventions
  - **input_ids:**
    - FCT-012
    - FCT-022
    - FCT-023
    - FCT-024
    - FCT-025
    - FCT-026
    - FCT-027
  - **module:** clusters/POWER.md
  - **negative_results:**
    - proceeding alone not treated as infringement finding
  - **not_computable:**
    - general marginal effect of DSA enforcement on all platform content decisions
  - **operations:**
    - separate supervision powers, proceedings, findings and corrective outcomes
  - **operations_applied:**
    - separated supervision, proceedings, findings, commitments and platform system changes
  - **reason:** systemic-risk and recommender duties must be separated from case findings and downstream effects
  - **result_ids:**
    - CLM-004
    - CAU-004
  - **status:** DONE
  - **trigger:** ↕
- **item 3:**
  - **gaps:**
    - causal political-behaviour design
  - **input_ids:**
    - FCT-016
    - FCT-017
    - FCT-018
    - FCT-028
    - FCT-029
    - FCT-030
    - FCT-031
  - **module:** clusters/CONFIRMATION.md
  - **negative_results:**
    - most moderation not attributable to public notices
    - no general election effect identified
  - **not_computable:**
    - general causal effect of DSA on opinions, vote choice, turnout or election results
  - **operations:**
    - test censorship and democratic-effect hypotheses against denominator, remedies and independent data
  - **operations_applied:**
    - tested platform-terms denominator, appeal reversals, election-period moderation data and user-control limits
  - **reason:** censorship and democratic-effect claims require explicit negative controls and rival explanations
  - **result_ids:**
    - CLM-003
    - CLM-005
    - CLM-006
    - CAU-003
    - CAU-005
  - **status:** DONE
  - **trigger:** ⚔

### SCOPING_REPORT
- **actors_institutions:**
  - European Commission
  - Digital Services Coordinators
  - online platforms
  - trusted flaggers
  - out-of-court dispute bodies
  - researchers
  - users
- **domains:**
  - content moderation
  - recommender systems
  - systemic risk
  - elections and civic discourse
  - transparency
  - appeals
- **evidence_limits:**
  - DSA Transparency Database is platform-reported and incomplete for causal inference
  - enforcement cases are heterogeneous
  - downstream political-behaviour causal designs remain sparse
- **exclusions:**
  - treating every moderation decision as DSA-caused
  - equating trusted flagger with public removal order
  - equating proceeding with breach finding
  - inferring election effect from enforcement chronology
- **geo:** European Union
- **lead_question:** DSA as information-governance mechanism: obligations, intermediaries, effects and remedies
- **object_coverage:** STRONG_FOR_LEGAL_ARCHITECTURE_AND_REMEDIES;STRONG_FOR_CASE_SPECIFIC_ENFORCEMENT;STRONG_FOR_MODERATION_DENOMINATOR;NOT_IDENTIFIED_FOR_GENERAL_DEMOCRATIC_EFFECT
- **object_question:** Which DSA duties and intermediaries actually affect moderation, recommendation and systemic-risk governance, and what evidence separates legal obligation, platform execution, censorship claims and democratic effects?
- **period:** 2022-2026 with strictly necessary antecedents

### CREDO
- obligation != execution
- notice != removal
- trusted_flagger != state_order
- proceeding != finding
- risk_assessment != censorship
- platform_moderation != regulator_decision
- moderation != changed_opinion_or_election
- transparency != causality

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - notice-and-action
  - trusted flagger
  - statement of reasons
  - appeal
  - systemic risk
  - recommender system
  - enforcement
  - observability
- **priorities:**
  - decision-right boundaries
  - operational effects
  - negative controls
  - causal ceiling
- **query_guidance:** law and official enforcement first; independent empirical moderation evidence second; never substitute regulation for execution or execution for democratic effect.
- **speaker:**
  - **goal:** forensic causal discrimination
  - **target:** rule -> intermediary/authority -> platform action -> visibility -> remedy -> effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **threats:**
  - notice=removal
  - flagger=state_order
  - proceeding=finding
  - risk=censorship
  - moderation=election_effect

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** Most recorded moderation is platform-initiated under private terms.
  - **support:**
    - FCT-016
    - FCT-022
    - FCT-032
  - **synthesis:** DSA changes the governance envelope and specific intervention channels; attribution requires a decision-specific chain.
  - **thesis:** The DSA directly determines a broad share of online speech removals.
- **item 2:**
  - **antithesis:** They are designated priority notifiers and platforms retain a review step.
  - **support:**
    - FCT-002
    - FCT-007
    - FCT-008
  - **synthesis:** The mechanism increases agenda/processing priority but is not identical to an administrative or judicial order.
  - **thesis:** Trusted flaggers are de facto public censors.
- **item 3:**
  - **antithesis:** DSA is censorship.
  - **support:**
    - FCT-017
    - FCT-029
    - FCT-031
    - FCT-032
  - **synthesis:** Both global labels exceed the evidence; procedural, transparency and case-specific system effects are observable, democratic outcome effects are not generally identified.
  - **thesis:** DSA safeguards democracy.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **flow:** DSA or DSC designation -> notice/order/risk duty -> platform processing
  - **resource:** legal authority / procedural priority
  - **support:**
    - FCT-002
    - FCT-007
    - FCT-012
- **item 2:**
  - **flow:** platform -> statements/reports/data access -> public, researchers and supervisors
  - **resource:** moderation and system data
  - **support:**
    - FCT-014
    - FCT-015
    - FCT-028
    - FCT-030
- **item 3:**
  - **flow:** moderation decision -> internal/ODS challenge -> reversal or confirmation
  - **resource:** remedy rights
  - **support:**
    - FCT-005
    - FCT-006
    - FCT-017
    - FCT-018

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** EU legislature / DSA
  - **relation:** creates duties and supervision powers
  - **support:**
    - FCT-001
    - FCT-012
    - FCT-013
  - **to:** platforms, DSCs and Commission
- **item 2:**
  - **from:** trusted flaggers and users
  - **relation:** submit notices
  - **support:**
    - FCT-003
    - FCT-007
    - FCT-008
  - **to:** online platforms
- **item 3:**
  - **from:** Commission / DSCs
  - **relation:** supervise, investigate and enforce
  - **support:**
    - FCT-022
    - FCT-023
    - FCT-024
    - FCT-025
    - FCT-026
    - FCT-027
  - **to:** VLOPs/VLOSEs and intermediaries
- **item 4:**
  - **from:** users / dispute bodies / researchers
  - **relation:** appeal or scrutinise
  - **support:**
    - FCT-017
    - FCT-018
    - FCT-019
    - FCT-028
    - FCT-029
    - FCT-030
  - **to:** platform decisions and systems

### IMPACT_MAP
- **DSA_to_democratic_outcome:** NOT_IDENTIFIED
- **DSA_to_most_moderation_decisions:** NOT_IDENTIFIED
- **appeal_reversibility:** VERIFIED_OPERATIONAL
- **legal_architecture:** VERIFIED
- **support:**
  - FCT-007
  - FCT-008
  - FCT-016
  - FCT-017
  - FCT-022
  - FCT-029
- **systemic_risk_enforcement_to_platform_change:** VERIFIED_CASE_SPECIFIC
- **transparency_observability:** VERIFIED
- **trusted_flagger_auto_removal:** NOT_ESTABLISHED
- **trusted_flagger_priority:** VERIFIED

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** platform still evaluates illegality; separate public orders exist
  - **issue:** trusted flagger power
  - **pro:** notices receive priority and can lead to removal
  - **resolution:** priority review != automatic state removal
  - **support:**
    - FCT-002
    - FCT-007
    - FCT-008
- **item 2:**
  - **contra:** 99% of H1 2025 reported decisions were proactive platform terms enforcement
  - **issue:** DSA as cause of moderation
  - **pro:** DSA regulates moderation procedures and systemic risks
  - **resolution:** DSA shapes governance but does not identify most individual decisions as regulator-caused
  - **support:**
    - FCT-012
    - FCT-016
    - FCT-032
- **item 3:**
  - **contra:** large election-period database study found no significant enforcement adaptation
  - **issue:** election influence
  - **pro:** DSA regulates election/civic-discourse risks and triggered TikTok scrutiny
  - **resolution:** risk-governance activity != identified election effect
  - **support:**
    - FCT-012
    - FCT-025
    - FCT-029
- **item 4:**
  - **contra:** platform cooperation can constrain external review
  - **issue:** remedy effectiveness
  - **pro:** large reversal rates show meaningful correction
  - **resolution:** redress is operational but incomplete
  - **support:**
    - FCT-017
    - FCT-018
    - FCT-021

### VERIFICATION_REPORT
- **circular_families:**
  - EU law family A
  - Commission enforcement family B
  - French DSC family C
  - independent dispute family D
  - academic empirical family E
- **contradiction_ids:**
  - trusted-flagger-priority-vs-order
  - DSA-governance-vs-platform-terms-denominator
  - election-risk-enforcement-vs-observed-adaptation
  - appeal-effectiveness-vs-platform-cooperation
- **downgraded_ids:**
  - NONE
- **none_found_claims:**
  - general state command chain for most moderation decisions
  - general DSA causal effect on political opinions/election results
  - complete platform-independent moderation denominator
- **remaining_gaps:**
  - named content-level public-authority causal chain
  - DSA marginal effect on recommender exposure
  - political behaviour/election causal design
- **reopened_ids:**
  - FCT-001
  - FCT-002
  - FCT-003
  - FCT-004
  - FCT-005
  - FCT-006
  - FCT-007
  - FCT-008
  - FCT-009
  - FCT-010
  - FCT-011
  - FCT-012
  - FCT-013
  - FCT-014
  - FCT-015
  - FCT-016
  - FCT-017
  - FCT-018
  - FCT-019
  - FCT-020
  - FCT-021
  - FCT-022
  - FCT-023
  - FCT-024
  - FCT-025
  - FCT-026
  - FCT-027
  - FCT-028
  - FCT-029
  - FCT-030
  - FCT-031
  - FCT-032
- **sources_reopened:** 20
- **upgraded_ids:**
  - NONE
- **verdict:** READY_FOR_PRE_GATE

### EDI_REPORT
- **corpus:**
  - **circularity:** controlled by family accounting
  - **coverage:** STRONG_LEGAL_ARCHITECTURE;STRONG_OPERATIONAL_REMEDY;STRONG_CASE_ENFORCEMENT;MODERATE_EMPIRICAL_MODERATION;WEAK_GENERAL_DEMOCRATIC_CAUSALITY
  - **independence:** 5_UPSTREAM_FAMILIES
  - **limits:**
    - Commission impact page self-reports some outcomes
    - database fields reflect platform reporting
    - no general DSA political-treatment counterfactual
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **gap_type:** NONE
    - **independent_families:** 3
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES
    - **gap_type:** NONE
    - **independent_families:** 3
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** YES_OPERATIONAL
    - **gap_type:** NONE
    - **independent_families:** 3
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** YES_CASE
    - **gap_type:** CAUSALITY
    - **independent_families:** 2
  - **item 5:**
    - **claim_id:** CLM-005
    - **direct_object:** DENOMINATOR_CONTROL
    - **gap_type:** NONE
    - **independent_families:** 2
  - **item 6:**
    - **claim_id:** CLM-006
    - **direct_object:** BOUNDARY
    - **gap_type:** CAUSALITY
    - **independent_families:** 2
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** EU_LAW+COMMISSION+NATIONAL_DSC+DISPUTE_BODY+ACADEMIC
  - **perspective:** LAW+ENFORCEMENT+PLATFORM_MODERATION+REMEDY+EMPIRICAL_OBSERVABILITY
  - **stratification:** RULE+NOTICE/ORDER+PLATFORM_ACTION+REMEDY+OUTCOME
  - **temporal:** 2022-2026
- **edi:**
  - **assessment:** MULTI_FAMILY_LEGAL_ENFORCEMENT_REMEDY_EMPIRICAL_CORPUS
  - **flags:**
    - ADMINISTRATIVE_STATS_NOT_CAUSAL_ESTIMATES
    - PLATFORM_REPORTED_DATABASE
    - PROCEEDING_STATUS_HETEROGENEITY
    - POLITICAL_EFFECT_GAP
- **source_counts:**
  - **primary:** 14
  - **provenance_families:** 5
  - **secondary:** 6
  - **tertiary:** 0
  - **total:** 20

### RESPONSIBILITY_MAP
- **boundary:** public orders, platform notices, trusted-flagger notices, platform terms enforcement and systemic-risk supervision remain analytically separate.
- **not_established:**
  - general Commission command over individual political-content removals
  - trusted flaggers as automatic public removal authorities
  - general DSA causal effect on election outcomes
- **verified:**
  - platforms remain operational decision-makers for ordinary moderation
  - DSCs designate trusted flaggers and supervise national obligations
  - Commission supervises VLOP/VLOSE systemic-risk obligations and can enforce
  - users and ODS bodies can reverse/contest decisions

### NEXT_QUERIES
- decision-specific chain from Commission/DSC communication to a named content restriction
- platform-level denominator separating DSA-triggered actions from private-terms actions over time
- causal design for DSA recommender controls on political exposure/behaviour
- court decisions testing DSA moderation/fundamental-rights boundaries

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-009,QRY-013,QRY-024,QRY-025 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-002,QRY-010,QRY-014,QRY-026,QRY-027 | support:- | counter:- | results:FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-003,QRY-006,QRY-007,QRY-008,QRY-018,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023 | support:- | counter:- | results:FCT-012,FCT-013,FCT-014,FCT-022,FCT-023,FCT-024,FCT-025,FCT-026,FCT-027,FCT-032 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-004,QRY-011,QRY-012,QRY-029,QRY-030,QRY-031,QRY-032 | support:- | counter:- | results:FCT-016,FCT-017,FCT-018,FCT-028,FCT-029,FCT-030,FCT-031,FCT-032 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-013,QRY-014,QRY-016,QRY-024,QRY-025,SRC-001,SRC-002,SRC-004,SRC-012,SRC-013 | support:FCT-001,FCT-002,FCT-003,FCT-007,FCT-008,FCT-012 | counter:FCT-002 | results:FCT-001,FCT-002,FCT-003,FCT-007,FCT-008,FCT-012,FCT-002 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-016,QRY-024,QRY-025,SRC-004,SRC-012,SRC-013 | support:FCT-007,FCT-008,FCT-009 | counter:FCT-002 | results:FCT-007,FCT-008,FCT-009,FCT-002 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-014,QRY-015,QRY-024,QRY-026,QRY-027,QRY-028,QRY-029,SRC-002,SRC-003,SRC-012,SRC-014,SRC-015,SRC-016,SRC-017 | support:FCT-004,FCT-005,FCT-006,FCT-015,FCT-017,FCT-018,FCT-019,FCT-020 | counter:FCT-021,FCT-028 | results:FCT-004,FCT-005,FCT-006,FCT-015,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021,FCT-028 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-014,QRY-015,QRY-018,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023,QRY-024,SRC-002,SRC-003,SRC-006,SRC-007,SRC-008,SRC-009,SRC-010,SRC-011,SRC-012 | support:FCT-010,FCT-011,FCT-012,FCT-013,FCT-022,FCT-023,FCT-024,FCT-025,FCT-026,FCT-027,FCT-032 | counter:FCT-024,FCT-025,FCT-027 | results:FCT-010,FCT-011,FCT-012,FCT-013,FCT-022,FCT-023,FCT-024,FCT-025,FCT-026,FCT-027,FCT-032,FCT-024,FCT-025,FCT-027 | final:PARTIAL | gap:CAUSALITY
CLM-005 | attempts:QRY-014,QRY-018,QRY-029,QRY-031,SRC-002,SRC-006,SRC-017,SRC-019 | support:FCT-016,FCT-028,FCT-030 | counter:FCT-012,FCT-022,FCT-032 | results:FCT-016,FCT-028,FCT-030,FCT-012,FCT-022,FCT-032 | final:SUPPORTED | gap:NONE
CLM-006 | attempts:QRY-014,QRY-021,QRY-030,QRY-031,QRY-032,SRC-002,SRC-009,SRC-018,SRC-019,SRC-020 | support:FCT-029,FCT-030,FCT-031 | counter:FCT-012,FCT-025,FCT-032 | results:FCT-029,FCT-030,FCT-031,FCT-012,FCT-025,FCT-032 | final:PARTIAL | gap:CAUSALITY

## STATUS_DELTA_V1
DELTA-001 | AXS-001 | OPEN | SATURATED | FACTS checkpoint evidence collected
DELTA-002 | AXS-002 | OPEN | SATURATED | FACTS checkpoint evidence collected
DELTA-003 | AXS-003 | OPEN | SATURATED | FACTS checkpoint evidence collected
DELTA-004 | AXS-004 | OPEN | SATURATED | FACTS checkpoint evidence collected

## OPEN_GAPS_V1
CLM-004 | CLM | PARTIAL | CAUSALITY | The inspected corpus does not provide a general decision-level counterfactual mapping each enforcement intervention to downstream content availability or political behaviour.
CLM-006 | CLM | PARTIAL | CAUSALITY | No credible cross-platform causal design in the inspected corpus isolates the DSA marginal effect on political beliefs, turnout, vote choice or election result.
CAU-005 | CAU | UNRESOLVED | CAUSALITY | No design in the inspected corpus isolates the DSA marginal effect on political opinions, vote choice, turnout or election result.

SEMANTIC_COUNTS_V1:LED:0|CLM:6|AXS:4|CAU:5|CTRL:9|ACT:4

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"The DSA creates a multi-layer governance architecture for content and recommender systems, but ordinary notices, trusted-flagger notices, platform moderation and judicial/administrative orders are distinct mechanisms with different decision rights.","claimant":"INV-043 synthesis","counter":["FCT-002"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-007","FCT-008","FCT-012"]}
CLM-002 | {"claim":"Trusted flaggers obtain priority handling for notices within their expertise, but the inspected rules do not make the flagger itself the final public authority deciding every removal; platform review remains a distinct step unless a separate legal order applies.","claimant":"INV-043 synthesis","counter":["FCT-002"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-007","FCT-008","FCT-009"]}
CLM-003 | {"claim":"The DSA materially increases moderation observability and reversibility through statements of reasons, a public database, internal appeals and certified out-of-court disputes; reversal rates show substantial contestability of platform decisions.","claimant":"INV-043 synthesis","counter":["FCT-021","FCT-028"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-004","FCT-005","FCT-006","FCT-015","FCT-017","FCT-018","FCT-019","FCT-020"]}
CLM-004 | {"claim":"DSA systemic-risk, recommender and transparency obligations can change platform procedures and systems through supervision, commitments, fines or corrective plans, but enforcement stages must be distinguished from findings and from content-specific removal orders.","claimant":"INV-043 synthesis","counter":["FCT-024","FCT-025","FCT-027"],"gap":"The inspected corpus does not provide a general decision-level counterfactual mapping each enforcement intervention to downstream content availability or political behaviour.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-010","FCT-011","FCT-012","FCT-013","FCT-022","FCT-023","FCT-024","FCT-025","FCT-026","FCT-027","FCT-032"]}
CLM-005 | {"claim":"The recorded moderation denominator is inconsistent with a simple model in which the DSA or public notices directly cause most content moderation: Commission data for H1 2025 attribute 99% of more than 9 billion reported decisions to proactive platform terms-of-service enforcement.","claimant":"INV-043 synthesis","counter":["FCT-012","FCT-022","FCT-032"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-016","FCT-028","FCT-030"]}
CLM-006 | {"claim":"The inspected evidence does not identify a general causal effect of the DSA on opinions, civic discourse quality or election outcomes; empirical work improves observability but currently supports narrower claims about moderation patterns, transparency and user control.","claimant":"INV-043 synthesis","counter":["FCT-012","FCT-025","FCT-032"],"gap":"No credible cross-platform causal design in the inspected corpus isolates the DSA marginal effect on political beliefs, turnout, vote choice or election result.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-029","FCT-030","FCT-031"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-009","QRY-013","QRY-024","QRY-025"],"axis":"legal architecture/intermediaries","links":["OBJECT_QUESTION"],"question":"Which DSA actors and legal instruments can trigger, prioritise, review or compel action on content or recommender systems?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015"],"sought_objects":["articles 9/10 orders","article 16 notices","trusted flaggers","DSCs/Commission","platform decision boundary"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-002","QRY-010","QRY-014","QRY-026","QRY-027"],"axis":"moderation, transparency and redress","links":["OBJECT_QUESTION"],"question":"What operational changes to moderation transparency and user redress are observable under the DSA?","result_ids":["FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021"],"sought_objects":["statements of reasons","transparency database","internal appeals","out-of-court disputes","reversal rates"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-003","QRY-006","QRY-007","QRY-008","QRY-018","QRY-019","QRY-020","QRY-021","QRY-022","QRY-023"],"axis":"systemic-risk enforcement","links":["OBJECT_QUESTION"],"question":"How do systemic-risk and recommender obligations translate into Commission/DSC investigations, commitments or platform changes?","result_ids":["FCT-012","FCT-013","FCT-014","FCT-022","FCT-023","FCT-024","FCT-025","FCT-026","FCT-027","FCT-032"],"sought_objects":["risk assessments","election/civic discourse","recommender systems","proceedings","commitments/fines"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-004","QRY-011","QRY-012","QRY-029","QRY-030","QRY-031","QRY-032"],"axis":"causal democratic effect","links":["OBJECT_QUESTION"],"question":"What evidence identifies the DSA itself as causing changes in content availability, user behaviour, opinions or election outcomes?","result_ids":["FCT-016","FCT-017","FCT-018","FCT-028","FCT-029","FCT-030","FCT-031","FCT-032"],"sought_objects":["empirical moderation data","election comparison","automation","user control","negative controls"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"The legal processing sequence and platform decision boundary are directly documented.","counter":["FCT-002"],"limit":"A notice is not itself a public removal order and does not prove a particular content decision.","mechanism":"DSA notice or trusted-flagger notice -> prioritised/ordinary platform review -> platform decision -> restriction or no restriction","status":"SUPPORTED","support":["FCT-003","FCT-007","FCT-008","FCT-009"]}
CAU-002 | {"causal_right":"The publication mechanism and downstream empirical use of the database are directly observed.","counter":["FCT-028"],"limit":"Observability is not the same as accuracy, completeness or causal identification.","mechanism":"DSA transparency duties -> statement of reasons -> public database -> external observability and research","status":"SUPPORTED","support":["FCT-004","FCT-015","FCT-028","FCT-030"]}
CAU-003 | {"causal_right":"Large reversal counts and external dispute decisions establish an operational correction channel.","counter":["FCT-021"],"limit":"Reversal does not by itself prove the original decision was unlawful or measure net speech effects.","mechanism":"platform moderation -> internal/out-of-court appeal -> reversal/restoration","status":"SUPPORTED","support":["FCT-005","FCT-006","FCT-017","FCT-018","FCT-019","FCT-020"]}
CAU-004 | {"causal_right":"Case records show concrete procedural, transparency and system changes following DSA enforcement.","counter":["FCT-024","FCT-025"],"limit":"Case-specific system change does not establish viewpoint-specific censorship or downstream democratic effect.","mechanism":"DSA systemic-risk/recommender obligation -> Commission/DSC supervision -> commitment/fine/corrective plan -> platform system or process change","status":"SUPPORTED","support":["FCT-012","FCT-013","FCT-022","FCT-023","FCT-026","FCT-027","FCT-032"]}
CAU-005 | {"counter":["FCT-016","FCT-029","FCT-030"],"gap":"No design in the inspected corpus isolates the DSA marginal effect on political opinions, vote choice, turnout or election result.","gap_type":"CAUSALITY","limit":"chronology != causality; moderation != changed belief/election.","mechanism":"DSA governance -> aggregate moderation pattern -> political opinion/behaviour/election outcome","status":"UNRESOLVED","support":["FCT-029","FCT-031","FCT-032"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"notice != removal","status":"DONE","support":["FCT-003","FCT-008"]}
CTRL-002 | {"control":"trusted_flagger != state_order","status":"DONE","support":["FCT-002","FCT-007","FCT-008"]}
CTRL-003 | {"control":"proceeding != finding","status":"DONE","support":["FCT-024","FCT-025","FCT-027"]}
CTRL-004 | {"control":"risk_assessment != censorship","status":"DONE","support":["FCT-012","FCT-013"]}
CTRL-005 | {"control":"platform_moderation != regulator_decision","status":"DONE","support":["FCT-016","FCT-030"]}
CTRL-006 | {"control":"appeal_reversal != proof_original_illegality","status":"DONE","support":["FCT-017","FCT-018","FCT-020"]}
CTRL-007 | {"control":"transparency != causal_effect","status":"DONE","support":["FCT-015","FCT-028"]}
CTRL-008 | {"control":"moderation != changed_opinion_or_election","status":"DONE","support":["FCT-029","FCT-031"]}
CTRL-009 | {"control":"platform_terms_action != DSA_causation","status":"DONE","support":["FCT-016"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"implement notice handling, moderation explanations, complaint systems and recommender transparency/control","actor":"online platforms","intent":"comply with DSA duties while retaining platform-level moderation operations","status":"DONE","support":["FCT-003","FCT-004","FCT-005","FCT-010","FCT-011","FCT-015"]}
ACT-002 | {"action":"submit notices or challenges into DSA procedural channels","actor":"trusted flaggers and users","intent":"trigger priority review or contest moderation decisions","status":"DONE","support":["FCT-007","FCT-008","FCT-017","FCT-018","FCT-019"]}
ACT-003 | {"action":"designate, supervise, investigate, request information, sanction or accept commitments","actor":"Digital Services Coordinators and European Commission","intent":"enforce DSA obligations and systemic-risk governance","status":"DONE","support":["FCT-007","FCT-012","FCT-022","FCT-023","FCT-024","FCT-025","FCT-026","FCT-027"]}
ACT-004 | {"action":"scrutinise moderation data and independently review contested decisions","actor":"researchers and out-of-court dispute bodies","intent":"increase accountability, observability and redress","status":"DONE","support":["FCT-014","FCT-018","FCT-019","FCT-020","FCT-028","FCT-029","FCT-030"]}

SEARCH_ACTIVITY_V1:WEB:12|FETCH:20|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FAIL | MNEMO | MNEMO_UNAVAILABLE | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | PASS | - | - | Digital Services Act article 16 notice action article 22 trusted flagger platform decision
QRY-002 | WEB | PASS | - | - | DSA statements reasons transparency database internal complaints out of court dispute reversal rates
QRY-003 | WEB | PASS | - | - | DSA systemic risk elections civic discourse recommender systems Commission enforcement
QRY-004 | WEB | PASS | - | - | DSA empirical effect moderation political speech elections transparency database study
QRY-005 | WEB | PASS | - | - | DSA researcher data access audits risk assessment 2026
QRY-006 | WEB | PASS | - | - | DSA X fine transparency corrective measures 2025 2026
QRY-007 | WEB | PASS | - | - | DSA Meta political content CrowdTangle proceedings
QRY-008 | WEB | PASS | - | - | DSA TikTok Romania election proceedings recommender risks
QRY-009 | WEB | PASS | - | - | DSA trusted flaggers France Arcom platform removal decision
QRY-010 | WEB | PASS | - | - | DSA appeals centre transparency report overturn platform decisions
QRY-011 | WEB | PASS | - | - | DSA recommender non profiling option user control empirical
QRY-012 | WEB | PASS | - | - | DSA automated moderation statements reasons database observability 2025
QRY-013 | FETCH | PASS | SRC-001 | https://eur-lex.europa.eu/legal-content/EN-FR/TXT/?uri=CELEX%3A32022R2065 | -
QRY-014 | FETCH | PASS | SRC-002 | https://digital-strategy.ec.europa.eu/en/policies/dsa-impact-platforms | -
QRY-015 | FETCH | PASS | SRC-003 | https://digital-strategy.ec.europa.eu/en/policies/dsa-brings-transparency | -
QRY-016 | FETCH | PASS | SRC-004 | https://digital-strategy.ec.europa.eu/en/policies/trusted-flaggers-under-dsa | -
QRY-017 | FETCH | PASS | SRC-005 | https://digital-strategy.ec.europa.eu/en/news/commission-holds-roundtable-data-access-vetted-researchers | -
QRY-018 | FETCH | PASS | SRC-006 | https://digital-strategy.ec.europa.eu/en/news/commission-fines-x-eu120-million-under-digital-services-act | -
QRY-019 | FETCH | PASS | SRC-007 | https://digital-strategy.ec.europa.eu/en/news/commission-accepts-xs-corrective-measures-terminate-breaches-dsa | -
QRY-020 | FETCH | PASS | SRC-008 | https://digital-strategy.ec.europa.eu/en/news/commission-opens-formal-proceedings-against-facebook-and-instagram-under-digital-services-act | -
QRY-021 | FETCH | PASS | SRC-009 | https://digital-strategy.ec.europa.eu/en/news/commission-opens-formal-proceedings-against-tiktok-election-risks-under-digital-services-act | -
QRY-022 | FETCH | PASS | SRC-010 | https://digital-strategy.ec.europa.eu/en/news/commission-launches-investigation-shein-under-digital-services-act | -
QRY-023 | FETCH | PASS | SRC-011 | https://digital-strategy.ec.europa.eu/en/policies/list-designated-vlops-and-vloses | -
QRY-024 | FETCH | PASS | SRC-012 | https://www.arcom.fr/espace-professionnel/reglement-sur-les-services-numeriques-ou-dsa-obligations-et-services-concernes | -
QRY-025 | FETCH | PASS | SRC-013 | https://www.arcom.fr/nous-connaitre-nos-missions/superviser-les-plateformes-en-ligne-et-les-reseaux-sociaux/reglement-sur-les-services-numeriques-dsa-liste-des-signaleurs-de-confiance-designes-par-larcom | -
QRY-026 | FETCH | PASS | SRC-014 | https://www.arcom.fr/espace-professionnel/reglement-sur-les-services-numeriques-ou-dsa-enregistrement-dune-plateforme-en-ligne-sur-la-base-de-donnees-de-transparence-art-245 | -
QRY-027 | FETCH | PASS | SRC-015 | https://www.appealscentre.eu/appeals-centre-publishes-first-transparency-report/ | -
QRY-028 | FETCH | PASS | SRC-016 | https://www.appealscentre.eu/users-make-voices-heard-as-appeals-centres-first-decisions-overturn-platforms/ | -
QRY-029 | FETCH | PASS | SRC-017 | https://cris.maastrichtuniversity.nl/en/publications/automated-transparency-a-legal-and-empirical-analysis-of-the-digi/ | -
QRY-030 | FETCH | PASS | SRC-018 | https://arxiv.org/abs/2504.06976 | -
QRY-031 | FETCH | PASS | SRC-019 | https://policyreview.info/articles/analysis/platform-observability-and-content-governance | -
QRY-032 | FETCH | PASS | SRC-020 | https://www.sciencedirect.com/science/article/pii/S1071581926000868 | -

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | EURLEX-DSA | Regulation (EU) 2022/2065 - Digital Services Act | 2022-10-27 | 2026-09-09 | legal duties, notices, trusted flaggers, recommender transparency, systemic risk, redress | https://eur-lex.europa.eu/legal-content/EN-FR/TXT/?uri=CELEX%3A32022R2065
SRC-002 | ◈ | fam:B | EC-DSA-IMPACT-2026 | The impact of the Digital Services Act on digital platforms | 2026-05-19 | 2026-09-09 | moderation volumes, appeals, recommender choices, election guidance and enforcement outcomes | https://digital-strategy.ec.europa.eu/en/policies/dsa-impact-platforms
SRC-003 | ◈ | fam:B | EC-DSA-TRANSPARENCY | How the Digital Services Act enhances transparency online | 2026-09-08 | 2026-09-09 | reports, statements of reasons database, researcher access, risk and audit reports | https://digital-strategy.ec.europa.eu/en/policies/dsa-brings-transparency
SRC-004 | ◈ | fam:B | EC-TRUSTED-FLAGGERS | Trusted flaggers under the Digital Services Act | 2026-06-12 | 2026-09-09 | criteria, priority mechanism, annual reports and safeguards | https://digital-strategy.ec.europa.eu/en/policies/trusted-flaggers-under-dsa
SRC-005 | ◈ | fam:B | EC-RESEARCHER-ACCESS-2026 | Commission roundtable on data access for vetted researchers | 2026-05-20 | 2026-09-09 | launch of first vetted-researcher data access requests | https://digital-strategy.ec.europa.eu/en/news/commission-holds-roundtable-data-access-vetted-researchers
SRC-006 | ◈ | fam:B | EC-X-FINE-2025 | Commission fines X EUR 120 million under the DSA | 2025-12-05 | 2026-09-09 | deceptive design, ad repository and researcher public-data access breaches | https://digital-strategy.ec.europa.eu/en/news/commission-fines-x-eu120-million-under-digital-services-act
SRC-007 | ◈ | fam:B | EC-X-CORRECTIVE-2026 | Commission accepts X corrective measures to terminate DSA breaches | 2026-07-15 | 2026-09-09 | transparency and researcher data-access corrective action plan | https://digital-strategy.ec.europa.eu/en/news/commission-accepts-xs-corrective-measures-terminate-breaches-dsa
SRC-008 | ◈ | fam:B | EC-META-PROCEEDINGS-2024 | Commission opens formal proceedings against Facebook and Instagram under DSA | 2024-04-30 | 2026-09-09 | suspected political/deceptive advertising and CrowdTangle civic monitoring issues | https://digital-strategy.ec.europa.eu/en/news/commission-opens-formal-proceedings-against-facebook-and-instagram-under-digital-services-act
SRC-009 | ◈ | fam:B | EC-TIKTOK-ELECTION-2024 | Commission opens formal proceedings against TikTok on election risks | 2024-12-17 | 2026-09-09 | suspected election-risk assessment and mitigation failures in Romania | https://digital-strategy.ec.europa.eu/en/news/commission-opens-formal-proceedings-against-tiktok-election-risks-under-digital-services-act
SRC-010 | ◈ | fam:B | EC-SHEIN-2026 | Commission launches investigation into Shein under DSA | 2026-02-17 | 2026-09-09 | recommender transparency, addictive design and illegal products investigation | https://digital-strategy.ec.europa.eu/en/news/commission-launches-investigation-shein-under-digital-services-act
SRC-011 | ◈ | fam:B | EC-VLOP-SUPERVISION-2026 | Supervision of designated VLOPs and VLOSEs under DSA | 2026-09-07 | 2026-09-09 | current designations and enforcement chronology | https://digital-strategy.ec.europa.eu/en/policies/list-designated-vlops-and-vloses
SRC-012 | ◈ | fam:C | ARCOM-DSA-OBLIGATIONS | DSA obligations and services concerned - Arcom | 2026-02-06 | 2026-09-09 | French DSC role, obligations by article, complaints and certified dispute bodies | https://www.arcom.fr/espace-professionnel/reglement-sur-les-services-numeriques-ou-dsa-obligations-et-services-concernes
SRC-013 | ◈ | fam:C | ARCOM-TRUSTED-FLAGGERS | DSA trusted flaggers designated by Arcom | 2025-08-18 | 2026-09-09 | French trusted-flagger list, priority and platform review boundary | https://www.arcom.fr/nous-connaitre-nos-missions/superviser-les-plateformes-en-ligne-et-les-reseaux-sociaux/reglement-sur-les-services-numeriques-dsa-liste-des-signaleurs-de-confiance-designes-par-larcom
SRC-014 | ◈ | fam:C | ARCOM-DSA-DATABASE | DSA transparency database registration - Arcom | 2026-01-01 | 2026-09-09 | moderation definition, statements of reasons and public database submission | https://www.arcom.fr/espace-professionnel/reglement-sur-les-services-numeriques-ou-dsa-enregistrement-dune-plateforme-en-ligne-sur-la-base-de-donnees-de-transparence-art-245
SRC-015 | ◉ | fam:D | APPEALS-CENTRE-REPORT-2025 | Appeals Centre Europe first transparency report | 2025-10-01 | 2026-09-09 | nearly 10,000 disputes, scope and platform cooperation | https://www.appealscentre.eu/appeals-centre-publishes-first-transparency-report/
SRC-016 | ◉ | fam:D | APPEALS-CENTRE-FIRST-2025 | Appeals Centre first decisions overturn platforms | 2025-03-10 | 2026-09-09 | initial dispute outcomes and reversals | https://www.appealscentre.eu/users-make-voices-heard-as-appeals-centres-first-decisions-overturn-platforms/
SRC-017 | ◉ | fam:E | KAUSHAL-FACTT-2024 | Automated Transparency: Legal and Empirical Analysis of DSA Transparency Database | 2024-06-03 | 2026-09-09 | 131m statements of reasons; transparency gains and compliance limitations | https://cris.maastrichtuniversity.nl/en/publications/automated-transparency-a-legal-and-empirical-analysis-of-the-digi/
SRC-018 | ◉ | fam:E | SHAHI-DSA-ELECTION-2025 | A Year of the DSA Transparency Database: 2024 European Parliament Election | 2025-04-09 | 2026-09-09 | 1.58bn moderation actions around election and no significant adaptation finding | https://arxiv.org/abs/2504.06976
SRC-019 | ◉ | fam:E | PAPAEVANGELOU-VOTTA-2025 | Trading nuance for scale? Platform observability under the DSA | 2025-09-17 | 2026-09-09 | 439m statements of reasons; automation and cross-platform moderation differences | https://policyreview.info/articles/analysis/platform-observability-and-content-governance
SRC-020 | ◉ | fam:E | RS-CONTROL-2026 | Feeding the short-video feed: user control under DSA recommender rules | 2026-01-01 | 2026-09-09 | experimental user-control preferences and usage under transparent recommender controls | https://www.sciencedirect.com/science/article/pii/S1071581926000868

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://eur-lex.europa.eu/legal-content/EN-FR/TXT/?uri=CELEX%3A32022R2065 | A | 2026-09-09 | DSA application and layered obligations | The DSA applies a layered regime to intermediary services; VLOP/VLOSE obligations began earlier and the general regime applies broadly from 17 February 2024, with different duties depending on service type and size. | -
FCT-002 | FACT | ✧ | https://www.arcom.fr/espace-professionnel/reglement-sur-les-services-numeriques-ou-dsa-obligations-et-services-concernes | C | 2026-09-09 | Orders differ from platform notice-and-action | Arcom distinguishes judicial or administrative orders under DSA Articles 9 and 10 from platform notice-and-action under Article 16; these are separate legal channels and should not be collapsed into one state-removal mechanism. | -
FCT-003 | FACT | ✧ | https://www.arcom.fr/espace-professionnel/reglement-sur-les-services-numeriques-ou-dsa-obligations-et-services-concernes | C | 2026-09-09 | Article 16 notice-and-action mechanism | Hosting providers must provide mechanisms for notifying alleged illegal content; a notice initiates processing but does not itself establish that the content is illegal. | -
FCT-004 | FACT | ✧ | https://www.arcom.fr/espace-professionnel/reglement-sur-les-services-numeriques-ou-dsa-enregistrement-dune-plateforme-en-ligne-sur-la-base-de-donnees-de-transparence-art-245 | C | 2026-09-09 | Statement of reasons covers visibility restrictions | A DSA moderation decision includes removal as well as demotion, demonetisation, visibility/access restrictions and account restrictions; affected users must receive reasons and information about avenues of redress. | -
FCT-005 | FACT | ✧ | https://www.arcom.fr/espace-professionnel/reglement-sur-les-services-numeriques-ou-dsa-obligations-et-services-concernes | C | 2026-09-09 | Internal complaint right | Online platforms must provide an internal complaint-handling system for specified moderation decisions under Article 20. | -
FCT-006 | FACT | ✧ | https://www.arcom.fr/espace-professionnel/reglement-sur-les-services-numeriques-ou-dsa-obligations-et-services-concernes | C | 2026-09-09 | Out-of-court dispute right | Users must be informed about certified out-of-court dispute settlement under Article 21 as an additional route to challenge moderation decisions. | -
FCT-007 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/trusted-flaggers-under-dsa | B | 2026-09-09 | Trusted flagger notices receive priority | Trusted flagger status is awarded by the national Digital Services Coordinator to qualifying independent and competent entities; their notices within the designated expertise area receive priority and must be processed without undue delay. | -
FCT-008 | FACT | ✧ | https://www.arcom.fr/nous-connaitre-nos-missions/superviser-les-plateformes-en-ligne-et-les-reseaux-sociaux/reglement-sur-les-services-numeriques-dsa-liste-des-signaleurs-de-confiance-designes-par-larcom | C | 2026-09-09 | Trusted flagger is not an automatic removal order | Arcom states that a platform removes or blocks content when it shares the trusted flagger assessment; the platform may contest the manifestly illegal character, so trusted-flagger notice priority is not equivalent to a state order to remove. | -
FCT-009 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/trusted-flaggers-under-dsa | B | 2026-09-09 | Trusted flagger safeguards and reporting | Trusted flaggers must meet diligence, accuracy/objectivity and independence criteria and publish annual activity reports; status can be subject to supervision and safeguards. | -
FCT-010 | FACT | ✧ | https://www.arcom.fr/espace-professionnel/reglement-sur-les-services-numeriques-ou-dsa-obligations-et-services-concernes | C | 2026-09-09 | Recommender-system transparency obligation | Online platforms must explain the main parameters used by recommender systems; the DSA creates transparency obligations over how content is ranked. | -
FCT-011 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/dsa-impact-platforms | B | 2026-09-09 | VLOPs provide a non-personalised recommendation option | The Commission reports that VLOPs must offer at least one option not based on profiling and identifies major platforms that provide ways to disable personalised feeds. | -
FCT-012 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/dsa-impact-platforms | B | 2026-09-09 | Election and civic-discourse systemic risks are regulated | VLOPs and VLOSEs must assess and mitigate systemic risks related to electoral processes and civic discourse while protecting freedom of expression. | -
FCT-013 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/dsa-brings-transparency | B | 2026-09-09 | Risk assessments and independent audits | VLOPs/VLOSEs must perform recurring systemic-risk assessments and publish risk, mitigation and independent audit material, creating a formal oversight chain without itself proving that a specific moderation outcome was caused by the regulator. | -
FCT-014 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/dsa-brings-transparency | B | 2026-09-09 | Researcher data-access channel | The DSA creates routes for qualified researchers to access public and, through vetted procedures, internal platform data for research into systemic risks and mitigation effectiveness. | -
FCT-015 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/dsa-brings-transparency | B | 2026-09-09 | Transparency database creates near-real-time observability | The DSA Transparency Database publishes anonymised statements of reasons for content moderation decisions and, from 2025, uses more harmonised categories to improve comparison. | -
FCT-016 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/dsa-impact-platforms | B | 2026-09-09 | Most reported moderation is platform-initiated | For the first half of 2025 the Commission reports more than 9 billion moderation decisions, 99% taken proactively under platforms own terms and conditions, with only a marginal fraction linked to reports of illegal content. | -
FCT-017 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/dsa-impact-platforms | B | 2026-09-09 | Internal appeals reverse a material share of decisions | Since 2024 EU users appealed more than 165 million VLOP/VLOSE moderation decisions through internal mechanisms and almost 30% were reversed, showing that initial moderation decisions are materially contestable. | -
FCT-018 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/dsa-impact-platforms | B | 2026-09-09 | Out-of-court disputes also reverse decisions | In the first half of 2025 certified out-of-court bodies reviewed more than 1,800 Facebook, Instagram and TikTok disputes and reversed 52% of closed cases according to the Commission. | -
FCT-019 | FACT | ✧ | https://www.appealscentre.eu/appeals-centre-publishes-first-transparency-report/ | D | 2026-09-09 | Independent dispute route has non-trivial demand | Appeals Centre Europe reported nearly 10,000 disputes from November 2024 to August 2025, of which more than 3,300 were within scope, demonstrating actual use of the DSA-created independent dispute route. | -
FCT-020 | FACT | ✧ | https://www.appealscentre.eu/users-make-voices-heard-as-appeals-centres-first-decisions-overturn-platforms/ | D | 2026-09-09 | Early external appeals frequently overturned Facebook decisions | In its first published batch, Appeals Centre Europe reported more than 150 decisions and said more than half of 141 Facebook decisions were overturned. | -
FCT-021 | FACT | ✧ | https://www.appealscentre.eu/appeals-centre-publishes-first-transparency-report/ | D | 2026-09-09 | Dispute remedy can be limited by platform cooperation | Appeals Centre Europe later reported that although it received thousands of eligible Meta account-suspension disputes, it received the necessary content in fewer than 100 cases, limiting independent review in that class. | -
FCT-022 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/news/commission-fines-x-eu120-million-under-digital-services-act | B | 2026-09-09 | X fine targeted transparency and interface obligations | The Commission fined X EUR 120 million in December 2025 for DSA breaches including deceptive blue-check design, an inadequate advertising repository and failure to provide researcher access to public data; the decision was not a general order to remove political viewpoints. | -
FCT-023 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/news/commission-accepts-xs-corrective-measures-terminate-breaches-dsa | B | 2026-09-09 | X corrective measures targeted observability | In July 2026 the Commission accepted an X action plan focused on advertising-repository functionality and researcher access, subject to audit and enhanced supervision. | -
FCT-024 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/news/commission-opens-formal-proceedings-against-facebook-and-instagram-under-digital-services-act | B | 2026-09-09 | Meta political-content proceeding is an investigation, not a finding | The April 2024 Meta proceedings concerned suspected deceptive advertising/political-content practices and the loss of an effective third-party civic/election monitoring tool; opening proceedings did not itself establish a breach or a content-removal command. | -
FCT-025 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/news/commission-opens-formal-proceedings-against-tiktok-election-risks-under-digital-services-act | B | 2026-09-09 | TikTok Romania proceeding tests risk management | The December 2024 TikTok proceeding tests whether the platform adequately assessed and mitigated election risks, including recommender-system manipulation; the proceeding is not proof that foreign interference occurred or that the DSA changed the election result. | -
FCT-026 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/news/commission-launches-investigation-shein-under-digital-services-act | B | 2026-09-09 | Shein proceeding shows recommender-risk supervision beyond political content | The 2026 Shein investigation covers recommender transparency, addictive design and illegal products, illustrating that the DSA systemic-risk framework is broader than political speech governance. | -
FCT-027 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/list-designated-vlops-and-vloses | B | 2026-09-09 | DSA enforcement is case-specific and procedural | The Commission supervision register records designations, information requests, proceedings, preliminary findings, commitments, fines and corrective plans across services; these stages have different evidentiary meanings and should not be treated as equivalent findings. | -
FCT-028 | FACT | ✧ | https://cris.maastrichtuniversity.nl/en/publications/automated-transparency-a-legal-and-empirical-analysis-of-the-digi/ | E | 2026-09-09 | Transparency database has empirical value but compliance discretion | A 2024 FAccT study analysing a representative sample of 131 million statements of reasons found real transparency gains but continuing compliance and comparability problems due to platform discretion in reporting practices. | -
FCT-029 | FACT | ✧ | https://arxiv.org/abs/2504.06976 | E | 2026-09-09 | No clear election-period moderation adaptation in database study | A 2025 study of 1.58 billion self-reported moderation actions across eight large platforms around the 2024 European Parliament election found no significant change in enforcement behaviour around the election, while noting database limitations. | -
FCT-030 | FACT | ✧ | https://policyreview.info/articles/analysis/platform-observability-and-content-governance | E | 2026-09-09 | Moderation is heavily automated and platform-specific | A 2025 analysis of 439 million statements of reasons found most recorded moderation decisions were automated and applied broadly across the EU/EEA, with substantial differences among platform moderation strategies. | -
FCT-031 | FACT | ✧ | https://www.sciencedirect.com/science/article/pii/S1071581926000868 | E | 2026-09-09 | User control availability does not guarantee use | A 2026 recommender-control study found users tended not to use control features without prompting, while transparent and usable controls increased perceived control; it does not establish an effect on political beliefs or elections. | -
FCT-032 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/dsa-impact-platforms | B | 2026-09-09 | Commission attributes some platform changes to DSA guidance | The Commission reports examples of platforms changing AI/deepfake or recommender-related practices following DSA guidance and proceedings, but this administrative account does not isolate the DSA marginal causal effect on downstream democratic outcomes. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-012
FCT-003 | SRC-012
FCT-004 | SRC-014
FCT-005 | SRC-012
FCT-006 | SRC-012
FCT-007 | SRC-004
FCT-008 | SRC-013
FCT-009 | SRC-004
FCT-010 | SRC-012
FCT-011 | SRC-002
FCT-012 | SRC-002
FCT-013 | SRC-003
FCT-014 | SRC-003
FCT-015 | SRC-003
FCT-016 | SRC-002
FCT-017 | SRC-002
FCT-018 | SRC-002
FCT-019 | SRC-015
FCT-020 | SRC-016
FCT-021 | SRC-015
FCT-022 | SRC-006
FCT-023 | SRC-007
FCT-024 | SRC-008
FCT-025 | SRC-009
FCT-026 | SRC-010
FCT-027 | SRC-011
FCT-028 | SRC-017
FCT-029 | SRC-018
FCT-030 | SRC-019
FCT-031 | SRC-020
FCT-032 | SRC-002

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
FCT-031 | ELIGIBLE:VERIFIE
FCT-032 | ELIGIBLE:VERIFIE

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
FCT-031 | WRITE | -
FCT-032 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:search
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:facts
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:causal
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:verify
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:accountability
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:narrative

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-09T08:52:10.774326+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-029","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-030","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-031","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-032","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":32,"eligible":32,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:32;attempted:0;success:0;failure:0;blocked:32} | WRITEBACK_EXECUTION_V1:[32 rows, see section]

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
FCT-031 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-032 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
