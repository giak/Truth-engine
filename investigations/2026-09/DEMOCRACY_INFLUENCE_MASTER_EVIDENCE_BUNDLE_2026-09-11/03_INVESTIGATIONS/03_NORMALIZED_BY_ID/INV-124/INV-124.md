ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260907-2126-debanking-coercion-europe | PARENT_RUN_ID:NONE | AS_OF:2026-09-07
INPUT_KIND:RUN_CARD | MISSION_MODE:DEEPEN | INPUT_REF:PATH:/mnt/data/inv124-exec/te/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-07_debanking-coercion-europe/2026-09-07_21-26_debanking-coercion-europe_INPUT.md | SUBJECT_SLUG:debanking-coercion-europe | SUBJECT_FP:sha256:4a684de1207aed9cc37605773eb2b5bd6b8f6c8476dc1929d1c6ab4b3a09a41a | INPUT_SHA256:sha256:bfd71896d80612d6fba908fcb6d170ecdc2f043cc8fed39ec799ae5d8b51f3cc
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/Europe 2015-2026; bank/payment access, account closure, AML de-risking and formal sanctions; trace trigger -> decision authority -> restriction -> notice/recourse -> economic/political effect; UK only as isomorphic comparator.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/MONEY.md,clusters/POWER.md,clusters/NETWORK.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-124 — Debanking, paiements, sanctions et accès financier comme infrastructure privée/publique de coercition

## Résultat central

Le corpus ferme trois mécanismes distincts qui sont souvent fusionnés. Premièrement, la France et le droit de l’Union organisent des droits d’accès et des garanties procédurales pour certaines catégories de comptes, avec des exceptions bornées notamment par la LCB-FT et la sécurité. Deuxièmement, l’EBA établit que le **de-risking** est un phénomène réel dans l’Union : il peut relever d’une gestion légitime du risque, mais le traitement global de catégories sans appréciation individuelle peut devenir injustifié et produire de l’exclusion financière. Troisièmement, les sanctions de l’Union fournissent un contrôle positif de coercition publique explicite : une inscription juridique peut imposer un gel des avoirs et interdire la mise à disposition de fonds.

Ces trois mécanismes ne sont pas isomorphes. Le premier encadre l’accès, le deuxième relève d’une décision privée sous contrainte réglementaire et le troisième procède d’un ordre juridique public. Les confondre ferait disparaître l’arête décisive : **qui ordonne réellement la restriction et sur quelle base ?**

## France et Union européenne : accès et recours

Le droit français au compte permet à des personnes physiques ou morales remplissant les conditions d’obtenir la désignation d’un établissement par la Banque de France après un refus. Pour le compte ouvert dans ce cadre, la clôture est enfermée dans des motifs déterminés, avec préavis, motivation sous réserve d’exceptions de sécurité et information de la Banque de France. Le droit général des conventions de compte prévoit aussi un préavis minimal pour la résiliation par l’établissement. La directive européenne sur les comptes de paiement borne également les motifs de refus ou de résiliation d’un compte de base et refuse que le seul coût ou la seule lourdeur du contrôle de conformité suffise. Ces règles prouvent que l’accès financier est un objet régulé ; elles ne prouvent pas qu’un refus ou une clôture ordinaire soit politiquement motivé.

## De-risking : mécanisme réel, motif politique non automatique

L’EBA a documenté le de-risking à travers l’Union et ses conséquences possibles d’exclusion économique et sociale. Son point central est discriminant : la sortie d’une relation peut être un outil légitime de gestion du risque, mais l’exclusion de catégories entières sans analyse individuelle peut signaler une mauvaise gestion du risque LCB-FT. Les lignes directrices ultérieures cherchent précisément à éviter l’usage de motifs AML/CFT non étayés comme justification automatique d’un refus de service.

Cela établit un mécanisme de **sur-conformité ou d’aversion au risque** capable de restreindre l’accès sans qu’un ordre politique explicite soit nécessaire. L’existence de ce mécanisme ne permet cependant pas d’inférer l’intention politique d’un établissement dans un dossier particulier.

## Sanctions : contrôle positif d’une coercition publique explicite

Les mesures restrictives de l’Union s’imposent aux personnes et activités relevant de sa juridiction. Les gels d’avoirs et interdictions de mettre des fonds ou ressources économiques à disposition sont des restrictions financières juridiquement commandées. Dans ce cas, l’arête `autorité publique -> obligation de l’intermédiaire financier -> restriction` est documentée. C’est précisément ce qui manque quand une banque agit sur la base d’un risque commercial, réputationnel ou LCB-FT autonome.

## Contrôle britannique : le « political debanking » ne supporte pas une généralisation simple

Le dossier britannique fournit un contrôle utile parce que la controverse a obligé régulateur et établissement à reconstruire les décisions. Dans le cas Farage, la revue Travers Smith a conclu à une décision de sortie légale et principalement commerciale ; les déclarations publiques et le risque réputationnel faisaient partie du dossier mais n’étaient pas déterminants. La même revue a identifié des défaillances distinctes de communication, traitement des plaintes et classification PEP. Le second examen, portant sur 84 clôtures, n’a pas trouvé de preuve de discrimination fondée sur les opinions ou affiliations politiques dans l’échantillon, tout en relevant des insuffisances de procédure.

Les travaux de la FCA vont dans le même sens avec prudence : les données initiales de 34 entreprises ne signalaient aucune clôture principalement motivée par les opinions politiques, mais le régulateur a explicitement poursuivi les vérifications en raison des limites de collecte et de l’usage variable du « reputational risk ». Le suivi de 2024 a trouvé des dossiers où les opinions étaient connues, sans que les éléments examinés établissent qu’elles aient constitué la raison de la fermeture.

Le résultat n’est donc ni « political debanking inexistant » ni « political debanking systémique ». Il est plus étroit : **la présence d’un contenu politique dans un dossier de risque ne suffit pas à prouver qu’il est le motif opératoire de la décision**.

## Chaîne causale et plafond

La chaîne soutenue est : `déclencheur juridique/compliance/commercial/réputationnel -> autorité décisionnaire -> restriction de compte/paiement -> friction ou exclusion financière -> conséquence économique/organisationnelle`. La chaîne devient incomplète lorsqu’on ajoute `-> modification du comportement politique -> persuasion -> résultat électoral`. Le corpus étudié ne fournit pas de design contrefactuel fermant ces dernières arêtes.

Plafond : I0-I4 sont vérifiables cas par cas pour l’autorité, la règle, la décision et la restriction ; I5 reste partiel pour l’intention/commandement dans les décisions privées ; I6-I7 ne sont pas établis.

## Conclusion pour INV-129

INV-124 établit que l’accès financier peut fonctionner comme un levier de coercition ou d’exclusion, mais sous au moins trois architectures : **ordre public explicite**, **gestion privée du risque sous cadre réglementaire**, et **décision commerciale/réputationnelle**. La qualification d’« instrument politique » exige de fermer une arête supplémentaire de motif, tasking, contrainte ou causalité. Pour la synthèse lawfare/coercition, il faut donc comparer les pouvoirs et standards de preuve plutôt que regrouper toutes les restrictions sous une même étiquette.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:5|SRC_COMPLETE:14/14

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-07
- **notes:**
  - France/EU current rules prioritized
  - UK 2023-2024 comparator retained because mechanism is isomorphic
  - no prediction beyond as-of
- **status:** CURRENT_WITH_HISTORICAL_CONTROLS
- **window:** 2015-2026

### MANIPULATION_REPORT
- **assumptions:**
  - official law establishes formal authority, not hidden motive
  - corporate independent review establishes its bounded findings
  - FCA aggregate data are retained with stated limitations
- **clusters:**
  - **loaded:**
    - clusters/MONEY.md
    - clusters/POWER.md
    - clusters/NETWORK.md
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - financial access is materially important but not equivalent to political control
  - state sanctions and private de-risking are non-isomorphic mechanisms
  - procedural failure does not prove political motive
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - right-to-account
  - account termination
  - AML de-risking
  - asset freeze
  - reputational-risk closure
  - PEP review
  - payment-service termination
- **priorities:**
  - formal authority and access rights
  - public versus private decision chain
  - AML de-risking boundary
  - political-motive evidence
  - recourse and process
  - causal effect ceiling
- **query_guidance:** trace trigger -> decision maker -> legal/contractual basis -> restriction -> notice/reason -> appeal/reinstatement -> economic consequence -> political effect; never infer motive from restriction alone
- **rhetorical:**
  - **AUTH:** official legal and regulatory sources establish bounded rules/findings only
  - **BF:** N/A
  - **DEM:** case-specific closure reviews cannot be generalized without denominator
  - **FAC:** separate trigger, decision authority, legal basis, motive and effect
  - **NUM:** counts and notice periods do not establish political motive
- **speaker:**
  - **goal:** forensic classification of financial-access coercion
  - **target:** trigger -> authority -> restriction -> recourse -> effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **Κ:** 3
  - **Λ:** 4
  - **Ξ:** 4
  - **Σ:** 3
  - **Φ:** 4
  - **Ψ:** 3
  - **Ω:** 4
  - **κ:** 3
  - **ρ:** 4
  - **€:** 5
  - **↕:** 5
  - **⏰:** 3
  - **⚔:** 3
  - **⫸:** 4
  - **🌐:** 4
- **threats:**
  - debanking=censorship
  - compliance=political motive
  - private decision=state command
  - sanction=guilt
  - restriction=political effect

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - political/electoral causal effect
  - **input_ids:**
    - FCT-001
    - FCT-009
    - FCT-017
    - FCT-019
    - FCT-023
  - **module:** clusters/MONEY.md
  - **negative_results:**
    - financial restriction does not itself prove political motive
  - **not_computable:**
    - complete economic loss across all affected customers
  - **operations_applied:**
    - distinguished access right, account closure, de-risking and asset freeze
    - separated economic consequence from political effect
  - **reason:** financial access, account and payment restrictions are the object
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-003
    - CTRL-001
    - CTRL-002
    - CTRL-003
  - **status:** DONE
  - **trigger:** €
- **item 2:**
  - **gaps:**
    - motive/tasking in individual opaque cases
  - **input_ids:**
    - FCT-015
    - FCT-017
    - FCT-019
    - FCT-022
    - FCT-023
    - FCT-025
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no general state-command edge in private closure corpus
  - **not_computable:**
    - informal political pressure without documentary trace
  - **operations_applied:**
    - positive control for explicit state command via sanctions
    - tested political-motive inference in private closures
  - **reason:** test public/private command and coercion
  - **result_ids:**
    - CLM-003
    - CLM-004
    - CLM-005
    - LED-001
    - CTRL-003
    - CTRL-004
    - CTRL-005
  - **status:** DONE
  - **trigger:** ↕
- **item 3:**
  - **gaps:**
    - case-level pressure channels where no primary record exists
  - **input_ids:**
    - FCT-002
    - FCT-013
    - FCT-016
    - FCT-018
    - FCT-027
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - network position does not establish command beyond explicit legal obligation
  - **not_computable:**
    - undocumented informal coordination
  - **operations_applied:**
    - mapped regulator/authority to financial intermediary to customer
    - separated legal obligation from autonomous commercial decision
  - **reason:** map regulator-bank-customer and sanctions-enforcement interfaces
  - **result_ids:**
    - CLM-001
    - CLM-003
    - CLM-005
    - CTRL-001
    - CTRL-003
  - **status:** DONE
  - **trigger:** 🌐

### SCOPING_REPORT
- **excluded:**
  - generic payment censorship anecdotes without primary decision record
  - cryptocurrency exchange access except as generic category
  - political motive inferred solely from ideology or association
- **guards:**
  - debanking != censorship
  - compliance != political_motive
  - private_decision != state_command
  - sanction != guilt
  - access_restriction != political_effect
  - complaint_or_association != proof
- **included:**
  - France right-to-account and closure rules
  - EU basic payment-account framework
  - EBA de-risking findings/guidelines
  - EU asset-freeze sanctions
  - UK FCA/NatWest comparator
- **route:** INV-129

### CREDO
- debanking != censorship
- compliance != political_motive
- private_decision != state_command
- sanction != guilt
- access_restriction != political_effect
- procedure_failure != political_motive
- financial_access != electoral_result

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - basic-account right
  - AML/CFT de-risking
  - asset freeze
  - reputational-risk closure
  - PEP handling
  - notice/reason safeguards
- **priorities:**
  - authority
  - decision-maker
  - legal/contractual basis
  - individualized risk assessment
  - motive evidence
  - appeal/recourse
  - effect
- **query_guidance:** edge-by-edge reconstruction
- **speaker:**
  - **goal:** classify financial coercion mechanisms
  - **target:** authority-restriction-effect chain
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **threats:**
  - motive inference
  - state/private conflation
  - sanction/guilt conflation

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** France/EU access rules, EBA de-risking guidance and FCA closure data show multiple legal, AML, commercial and procedural mechanisms.
  - **resolution:** Prove the specific decision basis and authority before assigning political motive.
  - **thesis:** Any debanking is political censorship.
- **item 2:**
  - **antithesis:** EBA explicitly recognizes unwarranted de-risking and rejects blanket category treatment.
  - **resolution:** Compliance is a possible lawful basis, not an automatic justification for category-wide exclusion.
  - **thesis:** AML compliance fully justifies any closure.
- **item 3:**
  - **antithesis:** EU sanctions provide a distinct positive control where legal command is explicit; private closures may be commercial or risk-based.
  - **resolution:** State command requires an identifiable legal or tasking edge.
  - **thesis:** Private banks act as state coercion whenever access is restricted.
- **item 4:**
  - **antithesis:** The independent review found a predominantly commercial decision with political statements supporting but not determining it; FCA broader review did not find political views operative in sampled cases.
  - **resolution:** Farage demonstrates mixed-factor governance risk, not a general prevalence claim.
  - **thesis:** The Farage case proves systematic political debanking.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **flow:** customer/organization -> bank/payment provider
  - **resource:** account/payment access
  - **restriction:** refusal/closure/suspension
  - **status:** LEGALLY_AND_COMMERCIALLY_MULTI_CAUSAL
  - **support:**
    - FCT-001
    - FCT-009
    - FCT-019
- **item 2:**
  - **flow:** EU listing -> regulated financial institutions -> listed person/entity
  - **resource:** funds/economic resources
  - **restriction:** asset freeze + prohibition to make available
  - **status:** BINDING_PUBLIC_LAW
  - **support:**
    - FCT-015
    - FCT-017
- **item 3:**
  - **flow:** AML/CFT risk assessment -> customer category/individual
  - **resource:** financial service access
  - **restriction:** de-risking
  - **status:** LEGITIMATE_OR_UNWARRANTED_DEPENDING_ON_INDIVIDUALIZED_RISK_MANAGEMENT
  - **support:**
    - FCT-009
    - FCT-010
    - FCT-011
    - FCT-012

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** legislator/regulator
  - **limits:**
    - formal rule != case motive
  - **relation:** access rights, AML/CFT rules, sanctions obligations
  - **support:**
    - FCT-004
    - FCT-011
    - FCT-015
    - FCT-017
  - **to:** bank/payment provider
- **item 2:**
  - **from:** bank/payment provider
  - **limits:**
    - private decision != state command
  - **relation:** onboarding/closure/suspension/reputational-risk decision
  - **support:**
    - FCT-019
    - FCT-022
    - FCT-023
    - FCT-025
  - **to:** customer/organization
- **item 3:**
  - **from:** customer
  - **limits:**
    - recourse availability != successful restoration
  - **relation:** complaint/mediation/review
  - **support:**
    - FCT-003
    - FCT-005
    - FCT-024
    - FCT-027
  - **to:** bank/regulator/ombudsman channel

### IMPACT_MAP
- **economic_or_programmatic_effect:** SUPPORTED_GENERAL_RISK / CASE_SPECIFIC
- **electoral_effect:** NOT_ESTABLISHED_COUNTERFACTUALLY
- **financial_access:** VERIFIED_MECHANISM
- **political_behavior:** NOT_ESTABLISHED
- **political_motive:** NOT_ESTABLISHED_GENERALLY
- **support:**
  - FCT-009
  - FCT-013
  - FCT-017
  - FCT-024
  - FCT-028

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** EBA also identifies unwarranted blanket/category de-risking
  - **issue:** de-risking as legitimate risk tool versus unwarranted exclusion
  - **pro:** EBA recognizes legitimate risk management
  - **resolution:** INDIVIDUALIZED_RISK_AND_VALID_REASON_REQUIRED
- **item 2:**
  - **contra:** independent review found predominantly commercial exit and views not determining
  - **issue:** political views in closure record versus political motive
  - **pro:** Farage documents included public statements/reputational considerations
  - **resolution:** POLITICAL_CONTENT_PRESENT_MOTIVE_NOT_AUTOMATIC
- **item 3:**
  - **contra:** EU sanctions create explicit legal command; private closures may not
  - **issue:** private financial restriction versus public coercion
  - **pro:** both can remove access
  - **resolution:** AUTHORITY_EDGE_MUST_BE_PROVED
- **item 4:**
  - **contra:** no causal political/electoral design in corpus
  - **issue:** restriction versus political effect
  - **pro:** financial access is consequential
  - **resolution:** EFFECT_CEILING_I5_I7_OPEN

### VERIFICATION_REPORT
- **cross_checks:**
  - EBA de-risking versus access law
  - EU sanctions as positive state-command control
  - Farage case versus FCA aggregate
- **facts:** 28
- **limitations:**
  - FCA UK comparator not EU law
  - no prevalence census for France political actors
  - no causal political-outcome dataset
- **negative_controls:**
  - FCA aggregate/follow-up
  - Travers Smith Phase 2 sample
  - France/EU access safeguards
- **primary_or_official_dominant:** true
- **provenance_families:** 8
- **sources:** 14
- **verdict:** READY_FOR_PRE_GATE

### EDI_REPORT
- **corpus:**
  - **circularity:** LOW_TO_MODERATE
  - **coverage:** STRONG_FOR_FORMAL_MECHANISMS_PARTIAL_FOR_POLITICAL_MOTIVE
  - **independence:** HIGH_ACROSS_DISTINCT_INSTITUTIONAL_FAMILIES
  - **limits:**
    - NatWest publishes Travers Smith summaries of commissioned reviews
    - UK comparator is not France/EU legal regime
    - no political-effect counterfactual dataset
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **gap_type:** SCOPE
    - **independent_families:** 3
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 1
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** YES
    - **gap_type:** NONE
    - **independent_families:** 1
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** YES_WITH_BOUNDARIES
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 2
  - **item 5:**
    - **claim_id:** CLM-006
    - **direct_object:** NO_CAUSAL_DESIGN
    - **gap_type:** CAUSALITY
    - **independent_families:** 4
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** 8_PROVENANCE_FAMILIES
  - **perspective:** FR_ACCESS+EU_LAW+EBA+EU_SANCTIONS+UK_FCA+INDEPENDENT_CLOSURE_REVIEW
  - **stratification:** RIGHTS+AML_DERISKING+SANCTIONS+PRIVATE_CLOSURES+REMEDIES
  - **temporal:** 2014-2026
- **edi:**
  - **assessment:** STRONG_MECHANISM_AND_GOVERNANCE_COVERAGE_WITH_MOTIVE_AND_CAUSAL_GAPS
  - **flags:**
    - OFFICIAL_PRIMARY_DOMINANT
    - POSITIVE_STATE_COMMAND_CONTROL
    - NEGATIVE_POLITICAL_MOTIVE_CONTROLS
    - NO_CAUSAL_ELECTORAL_DESIGN
- **source_counts:**
  - **claim_source:** 0
  - **primary:** 14
  - **provenance_families:** 8
  - **secondary:** 0
  - **total:** 14

### RESPONSIBILITY_MAP
- **boundary:** restriction and access loss can be established without motive, state command or political effect
- **not_established:**
  - general political motive for private closures
  - general public tasking of private closures
  - political persuasion
  - electoral-result effect
- **verified:**
  - formal access-right and notice duties
  - EBA unwarranted-de-risking doctrine
  - EU sanctions legal command
  - case-specific commercial/reputational closure findings
  - procedural defects in reviewed Coutts cases

### NEXT_QUERIES
- **item 1:**
  - **need:** administrative sanctions without conviction, evidentiary threshold and due process
  - **route:** INV-080
- **item 2:**
  - **need:** synthesize lawfare/coercion across litigation, administrative and financial mechanisms
  - **route:** INV-129
- **item 3:**
  - **condition:** new primary case showing explicit political tasking, formal public instruction to a provider, or causal political-outcome evidence
  - **reopen:** INV-124

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-019,FCT-021,FCT-022,FCT-023,FCT-024,FCT-025,FCT-026 | final:GAP | gap:RESPONSIBILITY
LED-002 | attempts:QRY-005,QRY-006,QRY-007,QRY-010,QRY-011,QRY-013 | support:- | counter:- | results:FCT-009,FCT-013,FCT-019,FCT-022,FCT-025,FCT-028 | final:GAP | gap:CAUSALITY
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-005,QRY-006,QRY-007 | support:- | counter:- | results:FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-008,QRY-009 | support:- | counter:- | results:FCT-015,FCT-016,FCT-017,FCT-018 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-019,FCT-020,FCT-021,FCT-022,FCT-023,FCT-024,FCT-025,FCT-026 | final:GAP | gap:RESPONSIBILITY
AXS-005 | attempts:QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-024,FCT-026,FCT-027 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-005,QRY-006,QRY-007,QRY-010,QRY-011,QRY-013 | support:- | counter:- | results:FCT-009,FCT-013,FCT-019,FCT-022,FCT-025,FCT-028 | final:GAP | gap:CAUSALITY
CLM-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,SRC-001,SRC-002,SRC-003,SRC-004 | support:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008 | counter:CTRL-001 | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,CTRL-001 | final:SUPPORTED | gap:SCOPE
CLM-002 | attempts:QRY-005,QRY-006,QRY-007,SRC-005,SRC-006,SRC-007 | support:FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014 | counter:CTRL-002 | results:FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,CTRL-002 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-003 | attempts:QRY-008,QRY-009,SRC-008,SRC-009 | support:FCT-015,FCT-016,FCT-017,FCT-018 | counter:CTRL-003 | results:FCT-015,FCT-016,FCT-017,FCT-018,CTRL-003 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-010,QRY-011,QRY-012,QRY-013,SRC-010,SRC-011,SRC-012,SRC-013 | support:FCT-019,FCT-020,FCT-021,FCT-022,FCT-023,FCT-025 | counter:CTRL-004;CTRL-005 | results:FCT-019,FCT-020,FCT-021,FCT-022,FCT-023,FCT-025,CTRL-004;CTRL-005 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-005 | attempts:QRY-012,QRY-013,QRY-014,SRC-012,SRC-013,SRC-014 | support:FCT-024,FCT-026,FCT-027 | counter:CTRL-004 | results:FCT-024,FCT-026,FCT-027,CTRL-004 | final:SUPPORTED | gap:NONE
CLM-006 | attempts:QRY-005,QRY-007,QRY-009,QRY-010,QRY-011,QRY-013,SRC-005,SRC-007,SRC-009,SRC-010,SRC-011,SRC-013 | support:FCT-028,FCT-009,FCT-017,FCT-019,FCT-025 | counter:CTRL-006 | results:FCT-028,FCT-009,FCT-017,FCT-019,FCT-025,CTRL-006 | final:SUPPORTED | gap:CAUSALITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
AXS-004 | AXS | GAP | RESPONSIBILITY | Political awareness and reputational review are observable in some cases, but a general political-motive or state-command edge is not established.
AXS-006 | AXS | GAP | CAUSALITY | No causal design connects the observed restrictions to changed political behavior or electoral results.
CLM-001 | CLM | SUPPORTED | SCOPE | These protections are not identical across account types, organizations or ordinary commercial accounts.
CLM-002 | CLM | SUPPORTED | RESPONSIBILITY | A finding of de-risking does not establish political motive or state command.
CLM-004 | CLM | SUPPORTED | RESPONSIBILITY | Aggregate FCA data were initially gathered rapidly, and case-specific mixed factors require individual reconstruction rather than a universal motive conclusion.
CLM-006 | CLM | SUPPORTED | CAUSALITY | No exposure/persuasion/behavioral counterfactual design is present.
CAU-001 | CAU | GAP | CAUSALITY | The political-behavior and electoral-result edges remain unclosed.

SEMANTIC_COUNTS_V1:LED:2|CLM:6|AXS:6|CAU:1|CTRL:6|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-010","QRY-011","QRY-012","QRY-013"],"evidence_excerpt":"Political views can appear in customer-risk records, but the FCA follow-up and Travers Smith reviews preserve commercial, financial-crime and process explanations and do not establish general political command.","gap":"The examined aggregate and case-specific records do not establish a general edge from account restriction or reputational-risk review to political motive or public tasking.","gap_type":"RESPONSIBILITY","kind":"EVIDENCE_GAP","lead":"Private financial restriction to political motive or state command","linked_ids":["CLM-004","CAU-001","CTRL-004","CTRL-005"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-019","FCT-021","FCT-022","FCT-023","FCT-024","FCT-025","FCT-026"],"routes":["INV-129"],"source_id":"INV-124_RUN_CARD","status":"GAP"}
LED-002 | {"attempt_ids":["QRY-005","QRY-006","QRY-007","QRY-010","QRY-011","QRY-013"],"evidence_excerpt":"The corpus establishes access, closures, sanctions and process consequences but not a counterfactual political outcome.","gap":"No examined source identifies a causal change in political behavior, voter persuasion or electoral result attributable to the financial restriction.","gap_type":"CAUSALITY","kind":"CAUSAL_GAP","lead":"Financial restriction to political behavior or electoral-result effect","linked_ids":["CLM-006","CAU-001","CTRL-006"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-009","FCT-013","FCT-019","FCT-022","FCT-025","FCT-028"],"routes":["INV-129","INV-133"],"source_id":"INV-124_RUN_CARD","status":"GAP"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"French and EU law create bounded rights and procedural safeguards for access to basic payment accounts while retaining AML/CFT, security and other specified exceptions.","claimant":"INV-124 synthesis","counter":"CTRL-001","gap":"These protections are not identical across account types, organizations or ordinary commercial accounts.","gap_type":"SCOPE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008"]}
CLM-002 | {"claim":"De-risking is a real EU-wide financial-access mechanism that can be legitimate risk management or unwarranted exclusion; category-wide refusal without individual risk assessment can be inconsistent with effective risk-based AML/CFT management.","claimant":"INV-124 synthesis","counter":"CTRL-002","gap":"A finding of de-risking does not establish political motive or state command.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014"]}
CLM-003 | {"claim":"Formal EU sanctions constitute a direct public-law financial coercion mechanism: listed persons can face asset freezes and prohibitions on making funds or economic resources available, with Member States responsible for enforcement.","claimant":"INV-124 synthesis","counter":"CTRL-003","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-015","FCT-016","FCT-017","FCT-018"]}
CLM-004 | {"claim":"The examined UK political-debanking evidence does not support a general rule that banks close accounts because of lawful political views: the Farage review found a predominantly commercial exit with political statements supporting but not determining it, while FCA aggregate and follow-up work did not establish political views as the operative reason in reviewed cases.","claimant":"INV-124 synthesis","counter":"CTRL-004;CTRL-005","gap":"Aggregate FCA data were initially gathered rapidly, and case-specific mixed factors require individual reconstruction rather than a universal motive conclusion.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-019","FCT-020","FCT-021","FCT-022","FCT-023","FCT-025"]}
CLM-005 | {"claim":"A financial-access decision can be lawful or commercially grounded while still containing procedural, communication, complaints, PEP-classification or data-governance defects.","claimant":"INV-124 synthesis","counter":"CTRL-004","gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-024","FCT-026","FCT-027"]}
CLM-006 | {"claim":"The corpus does not establish that debanking, de-risking or financial sanctions by themselves changed political preferences, participation or an election result.","claimant":"INV-124 synthesis","counter":"CTRL-006","gap":"No exposure/persuasion/behavioral counterfactual design is present.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-028","FCT-009","FCT-017","FCT-019","FCT-025"]}

### AXIS_REGISTRY_V1
AXS-001 | {"assessment":"VERIFIED_BOUNDED","attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004"],"axis":"formal_access_and_remedies","links":["CLM-001","CTRL-001"],"question":"What legal rights, notice duties and remedies constrain account refusal or closure?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008"],"sought_objects":["RIGHT_TO_ACCOUNT","BASIC_ACCOUNT","NOTICE","REASONS","MEDIATION"],"status":"SATURATED"}
AXS-002 | {"assessment":"VERIFIED","attempt_ids":["QRY-005","QRY-006","QRY-007"],"axis":"aml_derisking","links":["CLM-002","CTRL-002"],"question":"When does compliance-driven refusal or closure become unwarranted de-risking?","result_ids":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014"],"sought_objects":["AML_CFT","RISK_BASED","CATEGORY_DERISKING","FINANCIAL_EXCLUSION"],"status":"SATURATED"}
AXS-003 | {"assessment":"VERIFIED","attempt_ids":["QRY-008","QRY-009"],"axis":"formal_state_financial_coercion","links":["CLM-003","CTRL-003"],"question":"What distinguishes explicit public-law financial coercion from private account-risk decisions?","result_ids":["FCT-015","FCT-016","FCT-017","FCT-018"],"sought_objects":["EU_SANCTION","ASSET_FREEZE","PROHIBITION_TO_PROVIDE_FUNDS","NATIONAL_ENFORCEMENT"],"status":"SATURATED"}
AXS-004 | {"assessment":"PARTIAL_NOT_GENERALIZABLE","attempt_ids":["QRY-010","QRY-011","QRY-012","QRY-013"],"axis":"political_motive_and_command","gap":"Political awareness and reputational review are observable in some cases, but a general political-motive or state-command edge is not established.","gap_type":"RESPONSIBILITY","links":["CLM-004","LED-001","CTRL-004","CTRL-005"],"question":"Do account closures or reputational-risk decisions establish political motive or public/private political command?","result_ids":["FCT-019","FCT-020","FCT-021","FCT-022","FCT-023","FCT-024","FCT-025","FCT-026"],"sought_objects":["POLITICAL_VIEW","REPUTATIONAL_RISK","COMMERCIAL_REASON","STATE_TASKING"],"status":"GAP"}
AXS-005 | {"assessment":"VERIFIED_CASE_SPECIFIC","attempt_ids":["QRY-012","QRY-013","QRY-014"],"axis":"procedural_governance","links":["CLM-005","CTRL-004"],"question":"Can a lawful or commercial exit still contain material governance defects?","result_ids":["FCT-024","FCT-026","FCT-027"],"sought_objects":["NOTICE","REASONS","COMPLAINT","PEP_CLASSIFICATION","DATA_PROCESSING"],"status":"SATURATED"}
AXS-006 | {"assessment":"NOT_ESTABLISHED","attempt_ids":["QRY-005","QRY-006","QRY-007","QRY-010","QRY-011","QRY-013"],"axis":"political_effect","gap":"No causal design connects the observed restrictions to changed political behavior or electoral results.","gap_type":"CAUSALITY","links":["CLM-006","LED-002","CTRL-006"],"question":"What political or electoral effect is causally attributable to financial restriction?","result_ids":["FCT-009","FCT-013","FCT-019","FCT-022","FCT-025","FCT-028"],"sought_objects":["ECONOMIC_ACCESS","POLITICAL_BEHAVIOR","PERSUASION","ELECTORAL_RESULT"],"status":"GAP"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"CTRL-001;CTRL-002;CTRL-004;CTRL-005;CTRL-006","gap":"The political-behavior and electoral-result edges remain unclosed.","gap_type":"CAUSALITY","limit":"The chain is well supported through restriction and some procedural/economic consequences, but motive and political outcome are not generally identified.","mechanism":"trigger (law/compliance/commercial/reputational) -> decision authority -> account/payment restriction -> loss or friction of financial access -> economic/organizational consequence -> possible political behavior/effect","status":"GAP","support":["FCT-003","FCT-009","FCT-017","FCT-023","FCT-024","FCT-026","FCT-027"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"France/EU access rights show that financial institutions are not unconstrained and that formal recourse exists in bounded account categories.","status":"VERIFIED","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008"]}
CTRL-002 | {"control":"EBA guidance explicitly distinguishes legitimate risk management from unwarranted de-risking and rejects blanket category treatment as a substitute for individual risk assessment.","status":"VERIFIED","support":["FCT-009","FCT-010","FCT-011","FCT-012"]}
CTRL-003 | {"control":"EU sanctions provide a positive control for actual public command: a legal listing produces binding asset-freeze/prohibition obligations.","status":"VERIFIED","support":["FCT-015","FCT-016","FCT-017","FCT-018"]}
CTRL-004 | {"control":"Farage is a mixed case rather than a clean political-motive example: political statements entered the record, but the independent review found the exit lawful and predominantly commercial and identified separate process failures.","status":"VERIFIED_CASE_SPECIFIC","support":["FCT-023","FCT-024"]}
CTRL-005 | {"control":"FCA aggregate and follow-up work did not identify political views as the primary/operative reason in the reviewed closure data, while acknowledging data and reputational-risk issues requiring follow-up.","status":"VERIFIED_NEGATIVE_CONTROL","support":["FCT-019","FCT-020","FCT-021","FCT-022"]}
CTRL-006 | {"control":"None of the examined authorities supplies a design identifying political persuasion or an electoral counterfactual caused by financial restriction.","status":"NEGATIVE_CONTROL","support":["FCT-028"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:1|FETCH:14|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | MNEMO_UNAVAILABLE degraded; exact snapshot search unavailable in this environment | MnemoLite | NONE | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | PASS | SRC-001 | https://www.banque-france.fr/fr/a-votre-service/particuliers/droit-au-compte-bancaire | FETCH exact source for INV-124: Banque de France — droit au compte bancaire
QRY-002 | FETCH | PASS | SRC-002 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044605348/2026-04-09 | FETCH exact source for INV-124: Code monétaire et financier — article L312-1
QRY-003 | FETCH | PASS | SRC-003 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038614561/2026-05-20 | FETCH exact source for INV-124: Code monétaire et financier — article L312-1-1
QRY-004 | FETCH | PASS | SRC-004 | https://eur-lex.europa.eu/legal-content/FR-EN/TXT/?uri=CELEX%3A32014L0092 | FETCH exact source for INV-124: Directive 2014/92/EU — payment accounts
QRY-005 | FETCH | PASS | SRC-005 | https://www.eba.europa.eu/publications-and-media/press-releases/eba-alerts-detrimental-impact-unwarranted-de-risking-and | FETCH exact source for INV-124: EBA — detrimental impact of unwarranted de-risking
QRY-006 | FETCH | PASS | SRC-006 | https://eba.europa.eu/publications-and-media/press-releases/eba-issues-guidelines-challenge-unwarranted-de-risking-and | FETCH exact source for INV-124: EBA — Guidelines to challenge unwarranted de-risking
QRY-007 | FETCH | PASS | SRC-007 | https://www.eba.europa.eu/sites/default/files/2025-03/514b651f-091b-42d3-b738-1fae79264044/Consumer%20Trends%20Report%202024-2025.pdf | FETCH exact source for INV-124: EBA Consumer Trends Report 2024/25
QRY-008 | FETCH | PASS | SRC-008 | https://finance.ec.europa.eu/eu-and-world/sanctions-restrictive-measures/overview-sanctions-and-related-resources_en | FETCH exact source for INV-124: European Commission — overview of EU sanctions
QRY-009 | FETCH | PASS | SRC-009 | https://finance.ec.europa.eu/publications/asset-freeze-and-prohibition-provide-funds-or-economic-resources_en | FETCH exact source for INV-124: European Commission — asset freeze and prohibition to provide funds/economic resources
QRY-010 | FETCH | PASS | SRC-010 | https://www.fca.org.uk/news/press-releases/fca-sets-out-initial-findings-bank-account-access-and-closures | FETCH exact source for INV-124: FCA — initial findings on bank account access and closures
QRY-011 | FETCH | PASS | SRC-011 | https://www.fca.org.uk/publications/corporate-documents/uk-payment-accounts-access-and-closures-update | FETCH exact source for INV-124: FCA — UK payment accounts access and closures update
QRY-012 | FETCH | PASS | SRC-012 | https://www.natwestgroup.com/news-and-insights/news-room/press-releases/our-updates/2023/oct/key-findings-from-phase-1-of-travers-smith-review.html | FETCH exact source for INV-124: NatWest/Travers Smith — Phase 1 Farage closure review
QRY-013 | FETCH | PASS | SRC-013 | https://www.natwestgroup.com/news-and-insights/news-room/press-releases/our-updates/2023/dec/key-findings-from-phase-2-of-travers-smith-review.html | FETCH exact source for INV-124: NatWest/Travers Smith — Phase 2 Coutts closure review
QRY-014 | FETCH | PASS | SRC-014 | https://www.gov.uk/government/publications/payment-service-contract-termination-rule-changes-draft-si-and-policy-note | FETCH exact source for INV-124: HM Treasury — payment service contract termination rule changes
QRY-015 | WEB | PASS | - | - | REFUTATION Causal political effect of financial restriction: search for evidence that bank/payment access restrictions, AML de-risking or financial sanctions caused voter persuasion, political behavior change, or a counterfactual electoral result.

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | BDF-DAC | Banque de France — droit au compte bancaire | n.d. | 2026-09-07T21:27:00+02:00 | eligibility, designation, refusal and closure exceptions | https://www.banque-france.fr/fr/a-votre-service/particuliers/droit-au-compte-bancaire
SRC-002 | ◈ | fam:B | LEGIARTI000044605348 | Code monétaire et financier — article L312-1 | 2021-12-27 | 2026-09-07T21:27:00+02:00 | right to account; motivated termination; Banque de France notice; mediation | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044605348/2026-04-09
SRC-003 | ◈ | fam:B | LEGIARTI000038614561 | Code monétaire et financier — article L312-1-1 | 2019-05-24 | 2026-09-07T21:27:00+02:00 | general deposit-account contract termination; minimum two-month notice | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038614561/2026-05-20
SRC-004 | ◈ | fam:C | CELEX-32014L0092 | Directive 2014/92/EU — payment accounts | 2014-08-28 | 2026-09-07T21:27:00+02:00 | basic payment account access and limited refusal/termination grounds | https://eur-lex.europa.eu/legal-content/FR-EN/TXT/?uri=CELEX%3A32014L0092
SRC-005 | ◈ | fam:D | EBA-OP-2022-01-PR | EBA — detrimental impact of unwarranted de-risking | 2022-01-05 | 2026-09-07T21:27:00+02:00 | scale, drivers and effects of de-risking in the EU | https://www.eba.europa.eu/publications-and-media/press-releases/eba-alerts-detrimental-impact-unwarranted-de-risking-and
SRC-006 | ◈ | fam:D | EBA-GL-2023-04-PR | EBA — Guidelines to challenge unwarranted de-risking | 2023-03-31 | 2026-09-07T21:27:00+02:00 | risk-based access to financial services; category-wide de-risking | https://eba.europa.eu/publications-and-media/press-releases/eba-issues-guidelines-challenge-unwarranted-de-risking-and
SRC-007 | ◈ | fam:D | EBA-CTR-2024-25 | EBA Consumer Trends Report 2024/25 | 2025-03-01 | 2026-09-07T21:27:00+02:00 | NCA measures and supervision on de-risking and financial inclusion | https://www.eba.europa.eu/sites/default/files/2025-03/514b651f-091b-42d3-b738-1fae79264044/Consumer%20Trends%20Report%202024-2025.pdf
SRC-008 | ◈ | fam:E | EC-FISMA-SANCTIONS-OVERVIEW | European Commission — overview of EU sanctions | 2025-12-01 | 2026-09-07T21:27:00+02:00 | jurisdiction, measures, enforcement roles | https://finance.ec.europa.eu/eu-and-world/sanctions-restrictive-measures/overview-sanctions-and-related-resources_en
SRC-009 | ◈ | fam:E | EC-FISMA-ASSET-FREEZE-2026 | European Commission — asset freeze and prohibition to provide funds/economic resources | 2026-05-06 | 2026-09-07T21:27:00+02:00 | Regulation 269/2014 asset-freeze guidance | https://finance.ec.europa.eu/publications/asset-freeze-and-prohibition-provide-funds-or-economic-resources_en
SRC-010 | ◈ | fam:other:fca | FCA-2023-ACCOUNT-CLOSURES | FCA — initial findings on bank account access and closures | 2023-09-19 | 2026-09-07T21:27:00+02:00 | 34-firm data exercise; political views and closure reasons | https://www.fca.org.uk/news/press-releases/fca-sets-out-initial-findings-bank-account-access-and-closures
SRC-011 | ◈ | fam:other:fca | FCA-2024-ACCOUNT-CLOSURES | FCA — UK payment accounts access and closures update | 2024-09-04 | 2026-09-07T21:27:00+02:00 | follow-up work on political views, reputational risk and controls | https://www.fca.org.uk/publications/corporate-documents/uk-payment-accounts-access-and-closures-update
SRC-012 | ◈ | fam:other:natwest | NWG-TS-PHASE1 | NatWest/Travers Smith — Phase 1 Farage closure review | 2023-10-27 | 2026-09-07T21:27:00+02:00 | independent review key findings on Farage closure | https://www.natwestgroup.com/news-and-insights/news-room/press-releases/our-updates/2023/oct/key-findings-from-phase-1-of-travers-smith-review.html
SRC-013 | ◈ | fam:other:natwest | NWG-TS-PHASE2 | NatWest/Travers Smith — Phase 2 Coutts closure review | 2023-12-15 | 2026-09-07T21:27:00+02:00 | 84-closure sample; standards, discrimination and process | https://www.natwestgroup.com/news-and-insights/news-room/press-releases/our-updates/2023/dec/key-findings-from-phase-2-of-travers-smith-review.html
SRC-014 | ◈ | fam:other:hmt | HMT-2024-TERMINATIONS | HM Treasury — payment service contract termination rule changes | 2024-03-14 | 2026-09-07T21:27:00+02:00 | proposed 90-day notice and detailed reasons for provider-initiated termination | https://www.gov.uk/government/publications/payment-service-contract-termination-rule-changes-draft-si-and-policy-note

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.banque-france.fr/fr/a-votre-service/particuliers/droit-au-compte-bancaire | A | 2026-09-07 | Right to a bank account in France | A person or legal entity domiciled in France and lacking a deposit account can use the French right-to-account procedure after a refusal to open an account. | -
FCT-002 | FACT | ✧ | https://www.banque-france.fr/fr/a-votre-service/particuliers/droit-au-compte-bancaire | A | 2026-09-07 | Bank designated under French right-to-account | A bank designated by Banque de France must open the account except bounded cases such as an existing deposit account or failure to provide AML/CFT documentation. | -
FCT-003 | FACT | ✧ | https://www.banque-france.fr/fr/a-votre-service/particuliers/droit-au-compte-bancaire | A | 2026-09-07 | Closure of designated French right-to-account account | For an account opened under the right-to-account procedure, closure is limited to specified grounds and generally requires a two-month notice, a reasoned decision and information to Banque de France. | -
FCT-004 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044605348/2026-04-09 | B | 2021-12-27 | French statutory right to account | Article L312-1 recognizes a right to a deposit account for qualifying persons and legal entities lacking such an account in France. | -
FCT-005 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044605348/2026-04-09 | B | 2021-12-27 | French termination notice and reasons under right-to-account | Article L312-1 requires a reasoned termination decision for a designated account except where reasons conflict with national security or public-order objectives, with Banque de France informed and mediation indicated. | -
FCT-006 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038614561/2026-05-20 | B | 2019-05-24 | General French deposit-account termination notice | For an indefinite-term deposit-account agreement, a French credit institution generally terminates with at least two months notice. | -
FCT-007 | FACT | ✧ | https://eur-lex.europa.eu/legal-content/FR-EN/TXT/?uri=CELEX%3A32014L0092 | C | 2014-08-28 | EU basic payment account refusal and termination grounds | Directive 2014/92/EU frames refusal or termination of a basic payment account as limited to specific circumstances, including AML/CFT or crime-related grounds defined by law. | -
FCT-008 | FACT | ✧ | https://eur-lex.europa.eu/legal-content/FR-EN/TXT/?uri=CELEX%3A32014L0092 | C | 2014-08-28 | Compliance burden not sufficient for basic account refusal | The Payment Accounts Directive states that refusal should not be justified merely because compliance checking is burdensome or costly. | -
FCT-009 | FACT | ✧ | https://www.eba.europa.eu/publications-and-media/press-releases/eba-alerts-detrimental-impact-unwarranted-de-risking-and | D | 2022-01-05 | De-risking occurs across the EU | The EBA found de-risking across the EU affecting multiple customer categories and capable of producing adverse economic outcomes or financial exclusion. | -
FCT-010 | FACT | ✧ | https://www.eba.europa.eu/publications-and-media/press-releases/eba-alerts-detrimental-impact-unwarranted-de-risking-and | D | 2022-01-05 | De-risking can be legitimate or unwarranted | The EBA states that de-risking can be a legitimate risk-management tool but can also indicate ineffective ML/TF risk management and have severe consequences. | -
FCT-011 | FACT | ✧ | https://eba.europa.eu/publications-and-media/press-releases/eba-issues-guidelines-challenge-unwarranted-de-risking-and | D | 2023-03-31 | EBA access-to-services guidelines | The EBA issued Guidelines intended to prevent denial of financial services on unsubstantiated AML/CFT grounds or without valid reason. | -
FCT-012 | FACT | ✧ | https://eba.europa.eu/publications-and-media/press-releases/eba-issues-guidelines-challenge-unwarranted-de-risking-and | D | 2023-03-31 | Category-wide de-risking | The EBA states that de-risking entire customer categories without considering individual risk profiles may be unwarranted and a sign of ineffective ML/TF risk management. | -
FCT-013 | FACT | ✧ | https://www.eba.europa.eu/sites/default/files/2025-03/514b651f-091b-42d3-b738-1fae79264044/Consumer%20Trends%20Report%202024-2025.pdf | D | 2025-03-01 | National supervisory responses to de-risking | EBA Consumer Trends reporting describes national measures including rules against category-wide de-risking, inspections and guidance on blocking or terminating customer relationships. | -
FCT-014 | FACT | ✧ | https://www.eba.europa.eu/sites/default/files/2025-03/514b651f-091b-42d3-b738-1fae79264044/Consumer%20Trends%20Report%202024-2025.pdf | D | 2025-03-01 | NGO relationship supervision | The EBA reports that some national authorities inspect how banks enter into and maintain relationships with NGOs while complying with AML/CFT duties. | -
FCT-015 | FACT | ✧ | https://finance.ec.europa.eu/eu-and-world/sanctions-restrictive-measures/overview-sanctions-and-related-resources_en | E | 2025-12-01 | EU sanctions bind actors within EU jurisdiction | EU restrictive measures are binding on EU nationals, persons located in the EU and persons doing business within EU jurisdiction. | -
FCT-016 | FACT | ✧ | https://finance.ec.europa.eu/eu-and-world/sanctions-restrictive-measures/overview-sanctions-and-related-resources_en | E | 2025-12-01 | Member-state enforcement of EU sanctions | Investigations of potential sanctions non-compliance and effective proportionate dissuasive penalties are responsibilities of Member States and national competent authorities. | -
FCT-017 | FACT | ✧ | https://finance.ec.europa.eu/publications/asset-freeze-and-prohibition-provide-funds-or-economic-resources_en | E | 2026-05-06 | Asset freeze as direct legal financial restriction | EU individual sanctions can impose asset freezes and prohibit making funds or economic resources available to listed persons or entities. | -
FCT-018 | FACT | ✧ | https://finance.ec.europa.eu/publications/asset-freeze-and-prohibition-provide-funds-or-economic-resources_en | E | 2026-05-06 | Sanctions distinguish state command from private risk choice | Where an EU asset-freeze rule applies, financial restrictions follow a binding legal measure rather than an autonomous reputational-risk decision by a bank. | -
FCT-019 | FACT | ✧ | https://www.fca.org.uk/news/press-releases/fca-sets-out-initial-findings-bank-account-access-and-closures | other:fca | 2023-09-19 | FCA 34-firm political-closure data exercise | The FCA collected data from 34 firms; firms reported no account closure between July 2022 and June 2023 primarily because of a customer political views, while the FCA said further verification was needed. | -
FCT-020 | FACT | ✧ | https://www.fca.org.uk/news/press-releases/fca-sets-out-initial-findings-bank-account-access-and-closures | other:fca | 2023-09-19 | Common reported closure reasons in FCA exercise | The most common reported reasons for closing, suspending or declining accounts were dormancy/inactivity or financial-crime concerns. | -
FCT-021 | FACT | ✧ | https://www.fca.org.uk/news/press-releases/fca-sets-out-initial-findings-bank-account-access-and-closures | other:fca | 2023-09-19 | UK protections not universal across organizations | The FCA noted that some Payment Accounts Regulations protections do not apply to businesses, charities, political parties and civil-society organisations. | -
FCT-022 | FACT | ✧ | https://www.fca.org.uk/publications/corporate-documents/uk-payment-accounts-access-and-closures-update | other:fca | 2024-09-04 | FCA follow-up on reputational-risk closures | In a sample of reputational-risk cases, FCA records sometimes showed awareness of political views, but the reviewed records supported firms explanations that those views were not the reason for denial or termination. | -
FCT-023 | FACT | ✧ | https://www.natwestgroup.com/news-and-insights/news-room/press-releases/our-updates/2023/oct/key-findings-from-phase-1-of-travers-smith-review.html | other:natwest | 2023-10-27 | Farage closure predominant rationale | Travers Smith Phase 1 concluded the Farage exit decision was lawful and predominantly commercial, while reputational risk and public statements were considered but were not determining factors. | -
FCT-024 | FACT | ✧ | https://www.natwestgroup.com/news-and-insights/news-room/press-releases/our-updates/2023/oct/key-findings-from-phase-1-of-travers-smith-review.html | other:natwest | 2023-10-27 | Farage process shortcomings | The same review found shortcomings in communication, complaints handling and the PEP classification, showing that a lawful closure can still contain procedural or governance defects. | -
FCT-025 | FACT | ✧ | https://www.natwestgroup.com/news-and-insights/news-room/press-releases/our-updates/2023/dec/key-findings-from-phase-2-of-travers-smith-review.html | other:natwest | 2023-12-15 | Coutts closure sample political-discrimination control | Travers Smith Phase 2 reviewed 84 closures, including relevant PEP cases, and reported no evidence of discrimination due to political views or affiliations in that sample. | -
FCT-026 | FACT | ✧ | https://www.natwestgroup.com/news-and-insights/news-room/press-releases/our-updates/2023/dec/key-findings-from-phase-2-of-travers-smith-review.html | other:natwest | 2023-12-15 | Coutts closure-process deficiencies | Phase 2 identified potential failures around notice, reasons, customer treatment and data processing in some cases despite finding decision-making generally consistent with relevant standards. | -
FCT-027 | FACT | ✧ | https://www.gov.uk/government/publications/payment-service-contract-termination-rule-changes-draft-si-and-policy-note | other:hmt | 2024-03-14 | UK proposed stronger account-termination procedure | HM Treasury published draft reforms requiring at least 90 days notice and a sufficiently detailed and specific explanation for provider-initiated payment-service termination, subject to exceptions such as unlawfulness. | -
FCT-028 | FACT | ✦ | https://www.eba.europa.eu/sites/default/files/2025-03/514b651f-091b-42d3-b738-1fae79264044/Consumer%20Trends%20Report%202024-2025.pdf | D,other:fca,other:natwest | 2026-09-07 | Causal political effect of financial restriction | The examined legal, supervisory and closure-review corpus establishes access restrictions, procedural safeguards and some economic or institutional consequences, but does not identify voter persuasion or a counterfactual political/electoral result caused by those restrictions. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-002
FCT-005 | SRC-002
FCT-006 | SRC-003
FCT-007 | SRC-004
FCT-008 | SRC-004
FCT-009 | SRC-005
FCT-010 | SRC-005
FCT-011 | SRC-006
FCT-012 | SRC-006
FCT-013 | SRC-007
FCT-014 | SRC-007
FCT-015 | SRC-008
FCT-016 | SRC-008
FCT-017 | SRC-009
FCT-018 | SRC-009
FCT-019 | SRC-010
FCT-020 | SRC-010
FCT-021 | SRC-010
FCT-022 | SRC-011
FCT-023 | SRC-012
FCT-024 | SRC-012
FCT-025 | SRC-013
FCT-026 | SRC-013
FCT-027 | SRC-014
FCT-028 | SRC-007,SRC-010,SRC-011,SRC-013

## REFUTATION_REGISTRY_V1
FCT-028 | QRY-015 | NONE

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
FCT-028 | ELIGIBLE:CONFIRME

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
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8
CP-002 | SEARCH | PASS | LAST_COMPLETED:9:ECOSYSTEM | NEXT_ACTION:10
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11:CAU-001 | NEXT_ACTION:12
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-07T19:44:24.583050+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:CONFIRME","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":28,"eligible":28,"failure":0,"success":0}}

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
FCT-028 | ELIGIBLE:CONFIRME | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
