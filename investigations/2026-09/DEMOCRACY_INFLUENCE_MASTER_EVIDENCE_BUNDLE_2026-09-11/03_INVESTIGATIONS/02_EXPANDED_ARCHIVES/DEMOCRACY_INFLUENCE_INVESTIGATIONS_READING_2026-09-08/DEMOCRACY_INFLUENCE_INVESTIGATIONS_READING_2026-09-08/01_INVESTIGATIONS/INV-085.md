ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260908-0102-editorial-selection | PARENT_RUN_ID:NONE | AS_OF:2026-09-08
INPUT_KIND:RUN_CARD | MISSION_MODE:RECHECK_EXTEND | INPUT_REF:PATH:/mnt/data/inv085-work/exec/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-08_editorial-selection/2026-09-08_01-02_editorial-selection_INPUT.md | SUBJECT_SLUG:editorial-selection | SUBJECT_FP:sha256:ecd5afc8bf6363a2ee3de454176dbe4135311517dc29bef5a3c6960bde1eba77 | INPUT_SHA256:sha256:fe0b4e05962548b95a9eb19ffdcb4434ea37626fdfe74ab05e01bfb29e900d4b
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/Europe 2019-2026; selection of claims/topics before verdict; compare transparent selection criteria, internal editorial authority, platform signals, and evidence of systematic selection differences; platform and international comparators only when mechanism-isomorphic.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/FRAMING.md,clusters/POWER.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
## Question et résultat

INV-085 isole l’arête qui précède tout verdict : **qu’est-ce qui entre dans la file éditoriale, qui le choisit et selon quels signaux ?** Le résultat est net mais borné. Les organisations examinées ne prétendent pas vérifier un échantillon aléatoire de toutes les affirmations disponibles. Elles publient au contraire des critères de tri : intérêt public, actualité, portée ou viralité, dommage potentiel, répétition, vérifiabilité, disponibilité de preuves et parfois demandes du public [FCT-001,FCT-002,FCT-012,FCT-013,FCT-015,FCT-018,FCT-019,FCT-021,FCT-028].

La sélection constitue donc un **pouvoir éditorial amont**. Chez AFP, les journalistes discutent les claims proposés avec des éditeurs régionaux qui précisent les besoins de preuve et éditent avant publication [FCT-004]. Reuters situe sa cellule de fact-checking dans l’éditorial et attribue explicitement le contrôle de sortie à son responsable de vérification avec l’appui d’éditeurs seniors [FCT-022]. Les standards EFCSN exigent eux-mêmes que les membres rendent public qui exerce ce contrôle [FCT-010].

## Les signaux qui alimentent la sélection

La file de candidats n’est pas fermée sur la rédaction. AFP indique considérer des posts signalés sur Facebook et Instagram dans le cadre du programme Meta [FCT-005]. Full Fact cite parmi ses facteurs la viralité, les événements en cours, la nouveauté, les demandes des lecteurs, l’intérêt anticipé du public et la possibilité de traiter un claim dans son partenariat Meta [FCT-014]. CORRECTIV et Maldita utilisent également les signalements de communautés et lecteurs [FCT-016,FCT-020].

Ces interfaces ont une conséquence méthodologique importante : **candidate-pool influence != editorial command**. Elles peuvent modifier ce qui est vu et donc ce qui est susceptible d’être sélectionné, sans démontrer que l’acteur externe impose le sujet, le verdict ou la rédaction finale.

## Les règles de sélection sont normatives, pas purement mécaniques

AFP combine viralité, impact, dommage, intérêt public et faisabilité probatoire [FCT-001,FCT-002]. Full Fact privilégie notamment la portée du claim et le profil du locuteur, sa répétition et le dommage potentiel [FCT-012,FCT-013]. CORRECTIV retient actualité, portée et dommage [FCT-015]. Maldita retient viralité et dangerosité, y compris pour agir avant viralisation dans certains contextes sensibles [FCT-018,FCT-019]. Reuters retient valeur éditoriale, dommage, portée actuelle et potentielle et séparabilité du fait et de l’opinion [FCT-021]. Les Décodeurs indiquent pertinence dans l’actualité ou le débat public, vérifiabilité, puis pour les propositions de lecteurs provenance, viralité et importance du thème [FCT-028].

Ces critères sont raisonnables comme règles de rareté éditoriale, mais ils construisent nécessairement un agenda : deux claims également faux peuvent ne pas avoir la même probabilité d’être examinés si leur portée, thème, locuteur, disponibilité de preuve ou dangerosité diffèrent. C’est un mécanisme de sélection, pas une preuve de manipulation.

## Contrôle négatif : standards d’impartialité

IFCN exige que les signataires considèrent portée et importance, publient leur méthode de sélection et ne concentrent pas indûment leurs vérifications sur un camp [FCT-006,FCT-007]. EFCSN impose une contrainte comparable et exige transparence sur le contrôle éditorial et les mécanismes d’indépendance face aux financements potentiellement conflictuels [FCT-009,FCT-010,FCT-011]. AFP affirme appliquer les mêmes standards indépendamment de l’auteur du claim [FCT-003].

Ces règles ne prouvent pas une neutralité parfaite. Elles prouvent qu’une neutralité de sélection est un objectif explicite et auditable, ce qui permet de distinguer **écart observé** et **violation intentionnelle**.

## Le test empirique français : asymétrie de contenu, causalité ouverte

L’étude publiée en 2025 dans le *Journal of the European Economic Association* analyse 2 405 articles de six fact-checkers généralistes français jusqu’en juillet 2021 [FCT-024]. Son modèle pooled rapporte une association de -0,05 entre alignement idéologique du média affilié et part d’articles consacrée à l’orientation alignée [FCT-025]. L’auteur conclut à des différences de contenu compatibles avec une sélection moins fréquente d’entités idéologiquement alignées et, lorsqu’elles sont vérifiées, à une sélection plus fréquente d’énoncés ensuite jugés corrects [FCT-026].

Le plafond probatoire est explicitement posé par l’étude elle-même : elle n’observe pas la distribution réelle des affirmations fausses dans l’univers des claims candidats et ne peut donc pas conclure que tous les fact-checkers sont biaisés par rapport à une vérité de référence. Elle précise aussi que les différences de contenu peuvent survenir sans violation délibérée des principes [FCT-027].

Le delta robuste est donc : **un biais de sélection systématique est une hypothèse empiriquement soutenue pour certains écarts relatifs entre fact-checkers français ; son origine causale exacte reste ouverte**. Propriété, financement, affinité, environnement professionnel, croyances, disponibilité des claims et signaux d’audience restent des mécanismes concurrents tant que l’arête de contrôle n’est pas documentée.

## Plateformes et financement : influence de l’environnement, pas preuve de tasking

Reuters divulgue des financements de Facebook et TikTok contre des évaluations de contenu et des services de fact-checking à LinkedIn [FCT-023]. EFCSN exige précisément que les revenus de plateformes ou sources publiques soient déclarés et que les mécanismes d’indépendance éditoriale soient expliqués [FCT-011]. Cela établit une relation économique et fonctionnelle, mais pas une instruction générale sur les sujets à choisir.

CORRECTIV distingue également le fact-check lié à Meta de la suppression : ses vérifications peuvent être associées à des avertissements et à une réduction de portée, tandis que la suppression relève des règles de plateforme et non de sa décision de fact-check [FCT-017].

## Plafond probatoire

```text
I0 acteurs/relations                         = VERIFIED
I1 capacité d’accès aux claims/signaux        = VERIFIED
I2 sélection selon critères et arbitrage      = VERIFIED
I3 contrôle/tasking externe généralisé        = NOT_ESTABLISHED
I4 exposition des checks sélectionnés         = PARTIAL/CONTEXT_DEPENDENT
I5 persuasion                                = NOT_ESTABLISHED
I6 changement comportemental/institutionnel   = NOT_ESTABLISHED
I7 résultat politique/électoral contrefactuel = NOT_ESTABLISHED
```

Pour INV-082, la conséquence est décisive : la concentration économique ne peut pas être reliée à la concentration éditoriale par simple propriété. Il faut tester une chaîne plus précise : `propriétaire/financeur -> instruction ou incitation documentée -> sélection de sujets -> traitement -> distribution`. INV-085 ferme solidement l’existence et la matérialité du maillon **sélection**, mais laisse ouvert le maillon **contrôle causal externe**.

Pour INV-068, le même principe vaut : un apparent consensus médiatique peut être amplifié par des règles de sélection communes ou convergentes sans coordination centrale. Une architecture coordonnée exige une preuve supplémentaire de tasking ou de contrôle.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:2|EDI_DECISIVE:5|SRC_COMPLETE:10/10

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-08
- **notes:**
  - current selection methodologies for AFP, Reuters, Full Fact, CORRECTIV, Maldita, IFCN/EFCSN
  - Le Monde charter version modified 2021
  - JEEA study published 2025 on articles through July 2021
  - Meta 2025 retrospective treated as interested-party statement
- **status:** CURRENT_THROUGH_2026
- **window:** 2019-2026

### MANIPULATION_REPORT
- **assumptions:**
  - published methodologies accurately describe formal policy but not every informal decision
  - JEEA coding/model are treated as study evidence with stated limitations
  - absence of public tasking records is not proof none exist
- **clusters:**
  - **loaded:**
    - clusters/FRAMING.md
    - clusters/POWER.md
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - scarcity makes selection unavoidable
  - selection criteria shape observed agenda before verdict
  - external signals may affect candidate discovery without command
- **input_kind:** RUN_CARD
- **mission_mode:** RECHECK_EXTEND
- **patterns:**
  - selection gate
  - virality
  - harm
  - editorial hierarchy
  - platform input
  - political asymmetry
- **priorities:**
  - formal criteria
  - internal authority
  - external signals
  - empirical asymmetry
  - negative controls
- **query_guidance:** prefer current first-party methodologies; use peer-reviewed study for observed content differences; preserve causal limits
- **rhetorical:**
  - **AUTH:** method pages establish declared rules and roles, not perfect compliance
  - **BF:** N/A
  - **DEM:** selection differences do not by themselves prove suppression
  - **FAC:** separate candidate discovery, selection, verdict, moderation and effect
  - **NUM:** JEEA coefficient is association within its design, not universal bias rate
- **speaker:**
  - **goal:** forensic upstream-selection analysis
  - **target:** selection authority and causal boundaries
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **Κ:** 4
  - **Λ:** 4
  - **Ξ:** 4
  - **Σ:** 4
  - **Φ:** 4
  - **Ψ:** 3
  - **Ω:** 4
  - **κ:** 3
  - **ρ:** 4
  - **€:** 3
  - **↕:** 5
  - **⏰:** 4
  - **⚔:** 4
  - **⫸:** 4
  - **🌐:** 4
- **threats:**
  - selection=verdict
  - agenda=censorship
  - funding=command
  - correlation=causal control

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - unobserved rejected/never-seen candidate pool
  - **input_ids:**
    - FCT-001
    - FCT-012
    - FCT-015
    - FCT-018
    - FCT-021
    - FCT-028
  - **module:** clusters/FRAMING.md
  - **negative_results:**
    - no evidence that omission alone equals suppression
  - **not_computable:**
    - counterfactual universe of all equally checkable claims
  - **operations_applied:**
    - mapped selection criteria across outlets
    - separated candidate discovery from verdict
  - **reason:** topic selection determines which claims enter the verification frame before verdict
  - **result_ids:**
    - CLM-001
    - CLM-003
    - CLM-006
  - **status:** DONE
  - **trigger:** Φ
- **item 2:**
  - **gaps:**
    - contracts/instructions and internal deliberation records
  - **input_ids:**
    - FCT-004
    - FCT-010
    - FCT-022
    - FCT-023
    - FCT-025
    - FCT-027
  - **module:** clusters/POWER.md
  - **negative_results:**
    - general owner/funder/platform topic tasking not established
  - **not_computable:**
    - informal newsroom pressure without records
  - **operations_applied:**
    - located internal editorial authority
    - tested funding/platform inputs against topic-command inference
  - **reason:** selection requires authority over agenda and proposed checks
  - **result_ids:**
    - CLM-002
    - CLM-004
    - CLM-005
  - **status:** DONE
  - **trigger:** ↕

### SCOPING_REPORT
- **actors_institutions:**
  - AFP
  - Le Monde Les Décodeurs
  - Full Fact
  - CORRECTIV
  - Maldita
  - Reuters
  - IFCN
  - EFCSN
  - Meta
- **domains:**
  - fact-checking
  - editorial governance
  - platform partnerships
  - media bias
- **evidence_limits:**
  - public methodologies omit some internal deliberations
  - JEEA candidate ground truth unobserved
  - platform/contract internals incomplete
- **exclusions:**
  - verdict accuracy as primary object
  - generic ownership->editorial inference
  - generic censorship claims
  - post-selection causal impact without design
- **geo:** France/Europe; comparators isomorphic only
- **lead_question:** Sélection des sujets avant traitement
- **object_coverage:** STRONG_FOR_FORMAL_SELECTION_RULES_AND_INTERNAL_AUTHORITY; MODERATE_FOR_SYSTEMATIC_DIFFERENCES; WEAK_FOR_EXTERNAL_TASKING_AND_CAUSAL_EFFECT
- **object_question:** Comment les rédactions/fact-checkers sélectionnent-ils les sujets avant toute conclusion et que peut-on inférer sur biais ou contrôle externe ?
- **period:** 2019-2026

### CREDO
- selection != verdict
- agenda != censorship
- ownership != editorial_command
- funding != topic_tasking
- omission != suppression
- correlation != causal_control

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** RECHECK_EXTEND
- **patterns:**
  - editorial gatekeeping
  - reach/virality prioritization
  - harm prioritization
  - community submissions
  - platform candidate signals
  - political-content asymmetry
- **priorities:**
  - selection criteria
  - decision authority
  - candidate-pool inputs
  - systematic differences
  - external-control boundary
  - causal ceiling
- **query_guidance:** separate public rules, observed content distributions, funding/interfaces and causal command; do not infer hidden tasking from correlation
- **speaker:**
  - **goal:** forensic assessment of upstream editorial selection
  - **target:** candidate universe -> selection -> treatment/verdict -> downstream effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **threats:**
  - selection=verdict
  - funding=tasking
  - association=control
  - omission=suppression

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** Selection is explicitly filtered by reach, harm, relevance, verifiability and editorial judgment, and JEEA finds cross-outlet political-content differences.
  - **resolution:** Published checks are not a random sample; selection effects are real, but the ground-truth candidate distribution is unobserved.
  - **thesis:** Published fact checks are a neutral sample of political falsehoods.
- **item 2:**
  - **antithesis:** Funding and platform candidate signals are documented, while standards and outlets describe internal editorial control and independence mechanisms.
  - **resolution:** Resource/input relationships are real; topic-specific command requires a separate evidenced edge.
  - **thesis:** Platform or public funding proves external editorial command.
- **item 3:**
  - **antithesis:** Scarcity and published prioritization rules necessarily exclude many claims; no general deletion/control chain follows from omission.
  - **resolution:** Omission may matter for agenda visibility but is not equivalent to suppression without additional action evidence.
  - **thesis:** Not checking a claim is censorship or suppression.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **boundary:** funding/service relation documented; topic tasking not established
  - **from:** Meta / TikTok
  - **support:**
    - FCT-023
  - **to:** Reuters Fact Check
  - **vehicle:** paid fact-checking partnership/services
- **item 2:**
  - **boundary:** candidate-pool input documented; final selection command not established
  - **from:** Meta candidate signals/flagged posts
  - **support:**
    - FCT-005
    - FCT-014
  - **to:** AFP / Full Fact candidate pool
  - **vehicle:** platform partnership input

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** fact-check journalists
  - **limits:**
    - internal authority != external command
  - **relation:** proposal discussion, evidence requirements, editing
  - **support:**
    - FCT-004
    - FCT-022
  - **to:** regional/senior editors
- **item 2:**
  - **from:** readers/communities
  - **limits:**
    - submission != selection
  - **relation:** tips/submissions feed candidate discovery
  - **support:**
    - FCT-016
    - FCT-020
    - FCT-028
  - **to:** fact-check teams
- **item 3:**
  - **from:** platforms
  - **limits:**
    - interface/funding != topic tasking
  - **relation:** flagged material and paid assessment partnerships
  - **support:**
    - FCT-005
    - FCT-014
    - FCT-023
  - **to:** fact-check units
- **item 4:**
  - **from:** IFCN/EFCSN
  - **limits:**
    - standard != proof of perfect compliance
  - **relation:** methodology, impartiality and transparency standards
  - **support:**
    - FCT-006
    - FCT-009
    - FCT-010
    - FCT-011
  - **to:** member fact-checkers

### IMPACT_MAP
- **agenda_visibility:** VERIFIED_BOUNDED: selection determines which claims receive verification attention
- **electoral_effect:** NOT_ESTABLISHED
- **platform_distribution:** PARTIAL: some partnerships attach warnings/reduced reach; deletion not controlled by CORRECTIV fact checks
- **political_behavior:** NOT_ESTABLISHED_BY_THIS_RUN
- **support:**
  - FCT-005
  - FCT-017
  - FCT-027
- **verdict_effect:** SEPARATE_EDGE

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** JEEA reports systematic cross-outlet political-content differences
  - **issue:** declared nonpartisanship versus observed selection differences
  - **pro:** IFCN/EFCSN and outlets state impartiality/non-concentration standards
  - **resolution:** formal standards and empirical selection asymmetry can coexist; causal origin remains open
  - **support:**
    - FCT-003
    - FCT-006
    - FCT-009
    - FCT-025
    - FCT-026
    - FCT-027
- **item 2:**
  - **contra:** internal editorial control and independence requirements are also documented
  - **issue:** platform/funder influence versus internal editorial control
  - **pro:** platform funding and candidate signals are documented
  - **resolution:** interface/resource influence is established; general topic command is not
  - **support:**
    - FCT-004
    - FCT-005
    - FCT-010
    - FCT-011
    - FCT-022
    - FCT-023

### VERIFICATION_REPORT
- **circular_families:**
  - NONE
- **contradiction_ids:**
  - selection-standards-vs-asymmetry
  - funding-vs-control
- **downgraded_ids:**
  - NONE
- **none_found_claims:**
  - general topic-tasking by owner/funder/state/platform
  - selection automatically causes political/electoral outcome
- **remaining_gaps:**
  - unobserved candidate pool and rejected claims
  - private contracts/instructions/internal deliberations
  - causal exposure-outcome designs
- **reopened_ids:**
  - FCT-001
  - FCT-004
  - FCT-006
  - FCT-009
  - FCT-012
  - FCT-015
  - FCT-018
  - FCT-021
  - FCT-023
  - FCT-024
  - FCT-025
  - FCT-026
  - FCT-027
  - FCT-028
- **sources_reopened:** 10
- **upgraded_ids:**
  - NONE
- **verdict:** READY_FOR_PRE_GATE

### EDI_REPORT
- **corpus:**
  - **circularity:** LOW_TO_MODERATE; standards and member methods are related but not counted as independent proof of compliance
  - **coverage:** STRONG_FOR_DECLARED_SELECTION_RULES; MODERATE_FOR_EMPIRICAL_SELECTION_DIFFERENCES; WEAK_FOR_HIDDEN_TASKING_AND_CAUSAL_EFFECT
  - **independence:** MULTIPLE_FIRST_PARTY_OUTLETS_PLUS_STANDARDS_BODIES_PLUS_PEER_REVIEWED_STUDY
  - **limits:**
    - method pages are self-descriptions
    - JEEA ground truth candidate distribution unobserved
    - private tasking records unavailable
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **gap_type:** SCOPE
    - **independent_families:** 7
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 3
  - **item 3:**
    - **claim_id:** CLM-004
    - **direct_object:** YES_ASSOCIATIONAL
    - **gap_type:** CAUSALITY
    - **independent_families:** 1
  - **item 4:**
    - **claim_id:** CLM-005
    - **direct_object:** NEGATIVE_BOUNDARY
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 4
  - **item 5:**
    - **claim_id:** CLM-006
    - **direct_object:** CAUSAL_BOUNDARY
    - **gap_type:** CAUSALITY
    - **independent_families:** 3
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** 10_PROVENANCE_FAMILIES
  - **perspective:** FACTCHECKERS+STANDARDS_BODIES+PLATFORM+ACADEMIC
  - **stratification:** SELECTION_RULES+AUTHORITY+SIGNALS+FUNDING+EMPIRICAL_CONTENT
  - **temporal:** 2019-2026 with 2021 Le Monde methodology version and 2021-ending dataset
- **edi:**
  - **assessment:** STRONG_FORMAL_SELECTION_AND_AUTHORITY_COVERAGE_WITH_ONE_PEER_REVIEWED_SYSTEMATIC_ASYMMETRY_STUDY
  - **flags:**
    - MULTI_OUTLET_METHODS
    - EXPLICIT_SELECTION_CRITERIA
    - INTERNAL_EDITORIAL_AUTHORITY
    - PLATFORM_INPUTS
    - JEEA_ASSOCIATION_WITH_LIMITATIONS
- **source_counts:**
  - **claim_source:** 1
  - **primary:** 8
  - **provenance_families:** 10
  - **secondary:** 1
  - **total:** 10

### RESPONSIBILITY_MAP
- **boundary:** role, funding, affiliation or correlation do not establish topic-specific command or intent
- **not_established:**
  - general owner command over selected topics
  - general public-funder topic tasking
  - general platform command over final topic selection
  - intentional partisan manipulation by individual editors
  - causal electoral effect
- **verified:**
  - fact-check teams exercise selection under published criteria
  - editors exercise internal review/control in documented cases
  - platforms may supply signals/funding and apply downstream distribution mechanisms

### NEXT_QUERIES
- RECHECK if internal editorial calendars, rejected-candidate logs or assignment messages become accessible
- RECHECK if platform contracts specify claim/topic quotas or mandatory tasking
- RECHECK JEEA result if a later replication with observable candidate denominators appears
- DEFER political-effect claim pending exposure/outcome design

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-010 | support:- | counter:- | results:FCT-001,FCT-002,FCT-006,FCT-007,FCT-009,FCT-012,FCT-013,FCT-015,FCT-018,FCT-019,FCT-021,FCT-028 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-003,QRY-007 | support:- | counter:- | results:FCT-004,FCT-010,FCT-022 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-001,QRY-004,QRY-005,QRY-006,QRY-010 | support:- | counter:- | results:FCT-005,FCT-014,FCT-016,FCT-018,FCT-020,FCT-028 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-008 | support:- | counter:- | results:FCT-024,FCT-025,FCT-026,FCT-027 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-002,QRY-003,QRY-007,QRY-009 | support:- | counter:- | results:FCT-008,FCT-011,FCT-023,FCT-027 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-001,QRY-005,QRY-008,QRY-009 | support:- | counter:- | results:FCT-005,FCT-017,FCT-027 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,QRY-004,QRY-005,QRY-006,QRY-007,QRY-010,SRC-001,SRC-004,SRC-005,SRC-006,SRC-007,SRC-010 | support:FCT-001,FCT-002,FCT-012,FCT-013,FCT-015,FCT-018,FCT-019,FCT-021,FCT-028 | counter:CTRL-001 | results:FCT-001,FCT-002,FCT-012,FCT-013,FCT-015,FCT-018,FCT-019,FCT-021,FCT-028,CTRL-001 | final:SUPPORTED | gap:SCOPE
CLM-002 | attempts:QRY-001,QRY-003,QRY-007,SRC-001,SRC-003,SRC-007 | support:FCT-004,FCT-010,FCT-022 | counter:CTRL-003 | results:FCT-004,FCT-010,FCT-022,CTRL-003 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-003 | attempts:QRY-001,QRY-004,QRY-005,QRY-006,QRY-010,SRC-001,SRC-004,SRC-005,SRC-006,SRC-010 | support:FCT-005,FCT-014,FCT-016,FCT-018,FCT-020,FCT-028 | counter:CTRL-004 | results:FCT-005,FCT-014,FCT-016,FCT-018,FCT-020,FCT-028,CTRL-004 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-004 | attempts:QRY-008,SRC-008 | support:FCT-024,FCT-025,FCT-026 | counter:CTRL-006 | results:FCT-024,FCT-025,FCT-026,CTRL-006 | final:SUPPORTED | gap:CAUSALITY
CLM-005 | attempts:QRY-002,QRY-003,QRY-007,QRY-008,SRC-002,SRC-003,SRC-007,SRC-008 | support:FCT-008,FCT-011,FCT-023,FCT-027 | counter:CTRL-005 | results:FCT-008,FCT-011,FCT-023,FCT-027,CTRL-005 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-006 | attempts:QRY-001,QRY-005,QRY-008,SRC-001,SRC-005,SRC-008 | support:FCT-005,FCT-017,FCT-027 | counter:CTRL-004 | results:FCT-005,FCT-017,FCT-027,CTRL-004 | final:SUPPORTED | gap:CAUSALITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-001 | CLM | SUPPORTED | SCOPE | Les règles publiques ne capturent pas toutes les micro-décisions quotidiennes ni les sujets jamais considérés.
CLM-002 | CLM | SUPPORTED | RESPONSIBILITY | Les documents publics ne révèlent pas toutes les discussions internes, consignes informelles ou arbitrages de conférence de rédaction.
CLM-003 | CLM | SUPPORTED | RESPONSIBILITY | Candidate-pool influence does not establish external control over the final selection or verdict.
CLM-004 | CLM | SUPPORTED | CAUSALITY | L’étude identifie une association relative; elle ne connaît pas la distribution de vérité des déclarations candidates et ne ferme pas le mécanisme causal.
CLM-005 | CLM | SUPPORTED | RESPONSIBILITY | Des contrats, instructions internes ou échanges non publics pourraient modifier cette conclusion s’ils documentaient un topic tasking spécifique.
CLM-006 | CLM | SUPPORTED | CAUSALITY | Les effets de sélection sur exposition, confiance, comportement ou résultat politique exigent des designs causaux séparés.
CAU-001 | CAU | GAP | CAUSALITY | Need internal tasking records or quasi-experimental exposure/outcome evidence to close selection-control and political-effect links.

SEMANTIC_COUNTS_V1:LED:0|CLM:6|AXS:6|CAU:1|CTRL:6|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"La sélection en amont est un pouvoir éditorial réel et documenté : les rédactions filtrent un univers de claims selon intérêt public, portée, dommage potentiel, actualité, vérifiabilité et ressources.","claimant":"INV-085 synthesis","counter":"CTRL-001","gap":"Les règles publiques ne capturent pas toutes les micro-décisions quotidiennes ni les sujets jamais considérés.","gap_type":"SCOPE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-012","FCT-013","FCT-015","FCT-018","FCT-019","FCT-021","FCT-028"]}
CLM-002 | {"claim":"La décision de sélectionner et valider un sujet est principalement située dans la chaîne éditoriale interne documentée, non dans le verdict final lui-même.","claimant":"INV-085 synthesis","counter":"CTRL-003","gap":"Les documents publics ne révèlent pas toutes les discussions internes, consignes informelles ou arbitrages de conférence de rédaction.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-004","FCT-010","FCT-022"]}
CLM-003 | {"claim":"Des signaux externes peuvent modifier la file de candidats : virality metrics, reader/community reports and platform-flagged material are explicitly used by multiple fact-checkers.","claimant":"INV-085 synthesis","counter":"CTRL-004","gap":"Candidate-pool influence does not establish external control over the final selection or verdict.","gap_type":"RESPONSIBILITY","materiality":"HIGH","status":"SUPPORTED","support":["FCT-005","FCT-014","FCT-016","FCT-018","FCT-020","FCT-028"]}
CLM-004 | {"claim":"Une étude statistique publiée en 2025 trouve des différences systématiques entre six fact-checkers français compatibles avec un biais de sélection lié à l’orientation du média affilié.","claimant":"INV-085 synthesis","counter":"CTRL-006","gap":"L’étude identifie une association relative; elle ne connaît pas la distribution de vérité des déclarations candidates et ne ferme pas le mécanisme causal.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-024","FCT-025","FCT-026"]}
CLM-005 | {"claim":"Le corpus n’établit pas qu’un propriétaire, financeur, État ou plateforme commande de manière générale quels sujets les fact-checkers doivent traiter.","claimant":"INV-085 synthesis","counter":"CTRL-005","gap":"Des contrats, instructions internes ou échanges non publics pourraient modifier cette conclusion s’ils documentaient un topic tasking spécifique.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-008","FCT-011","FCT-023","FCT-027"]}
CLM-006 | {"claim":"Sélection du sujet, verdict, modération/suppression et effet politique sont des arêtes distinctes; aucune transition automatique entre elles n’est démontrée par ce corpus.","claimant":"INV-085 synthesis","counter":"CTRL-004","gap":"Les effets de sélection sur exposition, confiance, comportement ou résultat politique exigent des designs causaux séparés.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-005","FCT-017","FCT-027"]}

### AXIS_REGISTRY_V1
AXS-001 | {"assessment":"VERIFIED_MULTI_OUTLET","attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-010"],"axis":"selection_rules","links":["CLM-001"],"question":"Quels critères explicites gouvernent la sélection avant traitement ?","result_ids":["FCT-001","FCT-002","FCT-006","FCT-007","FCT-009","FCT-012","FCT-013","FCT-015","FCT-018","FCT-019","FCT-021","FCT-028"],"sought_objects":["PUBLIC_INTEREST","REACH","HARM","CURRENT_RELEVANCE","VERIFIABILITY"],"status":"SATURATED"}
AXS-002 | {"assessment":"INTERNAL_EDITORIAL_AUTHORITY_DOCUMENTED","attempt_ids":["QRY-001","QRY-003","QRY-007"],"axis":"editorial_authority","links":["CLM-002"],"question":"Qui exerce concrètement le pouvoir de choisir/valider un sujet ?","result_ids":["FCT-004","FCT-010","FCT-022"],"sought_objects":["EDITOR","TEAM","NEWSROOM","EDITORIAL_CONTROL"],"status":"SATURATED"}
AXS-003 | {"assessment":"MULTIPLE_EXTERNAL_INPUTS_DOCUMENTED","attempt_ids":["QRY-001","QRY-004","QRY-005","QRY-006","QRY-010"],"axis":"signals_and_candidate_pool","links":["CLM-001","CLM-003"],"question":"Quels signaux externes alimentent la file de sujets ?","result_ids":["FCT-005","FCT-014","FCT-016","FCT-018","FCT-020","FCT-028"],"sought_objects":["PLATFORM_FLAGS","VIRALITY","COMMUNITY_REPORTS","AUDIENCE_INTEREST"],"status":"SATURATED"}
AXS-004 | {"assessment":"ASSOCIATION_SUPPORTED_CAUSALITY_LIMITED","attempt_ids":["QRY-008"],"axis":"systematic_selection_difference","links":["CLM-004","CLM-005"],"question":"Existe-t-il une différence systématique documentée de sélection politique ?","result_ids":["FCT-024","FCT-025","FCT-026","FCT-027"],"sought_objects":["ARTICLE_DISTRIBUTION","POLITICAL_ALIGNMENT","SELECTION_ASYMMETRY"],"status":"SATURATED"}
AXS-005 | {"assessment":"FUNDING/INTERFACES_DOCUMENTED_TOPIC_TASKING_NOT_ESTABLISHED","attempt_ids":["QRY-002","QRY-003","QRY-007","QRY-009"],"axis":"funding_and_external_control","links":["CLM-003","CLM-005"],"question":"Les financeurs ou plateformes commandent-ils les sujets sélectionnés ?","result_ids":["FCT-008","FCT-011","FCT-023","FCT-027"],"sought_objects":["FUNDING","TASKING","TOPIC_COMMAND","EDITORIAL_INDEPENDENCE"],"status":"SATURATED"}
AXS-006 | {"assessment":"SELECTION_DISTINCT_FROM_VERDICT/DELETION/CAUSAL_EFFECT","attempt_ids":["QRY-001","QRY-005","QRY-008","QRY-009"],"axis":"downstream_effect","links":["CLM-006"],"question":"La sélection entraîne-t-elle automatiquement verdict, suppression ou effet politique ?","result_ids":["FCT-005","FCT-017","FCT-027"],"sought_objects":["VERDICT","DISTRIBUTION","DELETION","POLITICAL_EFFECT"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"CTRL-004;CTRL-005;CTRL-006","gap":"Need internal tasking records or quasi-experimental exposure/outcome evidence to close selection-control and political-effect links.","gap_type":"CAUSALITY","limit":"The chain is evidenced through candidate discovery and editorial selection, and partly through platform-linked downstream consequences; external command and political causal effect are not established.","mechanism":"universe of candidate claims -> monitoring/community/platform signals -> editorial selection criteria and judgement -> selected claim -> verification/verdict -> possible distribution/intervention consequences -> possible political effect","status":"GAP","support":["FCT-001","FCT-004","FCT-005","FCT-012","FCT-014","FCT-018","FCT-021","FCT-028"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Les standards IFCN/EFCSN exigent transparence de sélection et non-concentration indue sur un camp.","status":"VERIFIED","support":["FCT-006","FCT-007","FCT-009"]}
CTRL-002 | {"control":"Plusieurs rédactions publient des critères de sélection explicites et non identiques, ce qui rend la sélection observable mais non aléatoire.","status":"VERIFIED","support":["FCT-001","FCT-012","FCT-015","FCT-018","FCT-021","FCT-028"]}
CTRL-003 | {"control":"L’autorité éditoriale interne est explicitement documentée chez AFP, Reuters et par les exigences EFCSN.","status":"VERIFIED","support":["FCT-004","FCT-010","FCT-022"]}
CTRL-004 | {"control":"Les plateformes et communautés peuvent alimenter la file de candidats sans que cela établisse à lui seul un commandement éditorial externe.","status":"VERIFIED_BOUNDED","support":["FCT-005","FCT-014","FCT-016","FCT-020"]}
CTRL-005 | {"control":"Des relations financières avec des plateformes existent et doivent être séparées de la preuve de tasking sur les sujets.","status":"VERIFIED_BOUNDED","support":["FCT-011","FCT-023"]}
CTRL-006 | {"control":"L’étude JEEA mesure des différences relatives de contenu mais ne dispose pas de la distribution vraie des fausses déclarations et ne prouve pas un contrôle causal par propriétaire, financeur ou État.","status":"VERIFIED_LIMITATION","support":["FCT-024","FCT-025","FCT-026","FCT-027"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:10|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL:MNEMO_UNAVAILABLE | mnemo | NONE | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | NONE | runtime | NONE | MEMORY_PROBE
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | PASS | SRC-001 | https://factcheck.afp.com/How-we-work | FETCH AFP How we work selection criteria editorial process Meta partnership
QRY-002 | FETCH | PASS | SRC-002 | https://ifcncodeofprinciples.poynter.org/the-commitments | FETCH IFCN Code commitments selection reach importance editorial independence
QRY-003 | FETCH | PASS | SRC-003 | https://efcsn.com/code-of-standards/ | FETCH EFCSN Code standards methodology impartiality editorial control funding transparency
QRY-004 | FETCH | PASS | SRC-004 | https://fullfact.org/blog/2025/apr/how-does-the-full-fact-team-choose-what-to-fact-check/ | FETCH Full Fact 2025 how choose claims prominence repetition harm Meta partnership audience
QRY-005 | FETCH | PASS | SRC-005 | https://correctiv.org/faktencheck/faq-haeufig-gestellte-fragen-an-das-faktencheck-team/ | FETCH CORRECTIV Faktencheck FAQ selection relevance reach harm submissions Meta
QRY-006 | FETCH | PASS | SRC-006 | https://maldita.es/metodologia-maldita/ | FETCH Maldita methodology selection virality dangerousness community
QRY-007 | FETCH | PASS | SRC-007 | https://www.reuters.com/fact-check/about/ | FETCH Reuters Fact Check about methodology editorial criteria reach harm funding partnerships
QRY-008 | FETCH | PASS | SRC-008 | https://academic.oup.com/jeea/article/23/6/2137/8087339 | FETCH JEEA 2025 Both Judge and Party French fact-checkers selection slant limitations
QRY-009 | FETCH | PASS | SRC-009 | https://about.fb.com/news/2025/01/meta-more-speech-fewer-mistakes/ | FETCH Meta January 2025 ending third party fact checking stated rationale choices what to fact check
QRY-010 | FETCH | PASS | SRC-010 | https://www.lemonde.fr/les-decodeurs/article/2014/03/10/la-charte-des-decodeurs_4365106_4355770.html | FETCH Le Monde Decodeurs charter modified 2021 selection criteria reader proposals Facebook partnership

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | AFP-HOW-WE-WORK | AFP Fact Check — How we work | 2026-09-08 | 2026-09-08T16:30:00+02:00 | selection lines 18-24; editors 93-96; platform partnership 115-120 | https://factcheck.afp.com/How-we-work
SRC-002 | ◈ | fam:B | IFCN-CODE-COMMITMENTS | IFCN — Code of Principles commitments | 2026-09-08 | 2026-09-08T16:30:00+02:00 | eligibility and principles 1/4; selection methodology criteria | https://ifcncodeofprinciples.poynter.org/the-commitments
SRC-003 | ◈ | fam:C | EFCSN-CODE-STANDARDS | EFCSN — Code of Standards | 2026-09-08 | 2026-09-08T16:30:00+02:00 | Article 2 methodology; Article 3.1; Article 4.1-4.2 | https://efcsn.com/code-of-standards/
SRC-004 | ◈ | fam:D | FULLFACT-SELECTION-2025 | Full Fact — How does the team choose what to fact check? | 2025-04-03 | 2026-09-08T16:30:00+02:00 | Choosing what to check, lines 37-45 | https://fullfact.org/blog/2025/apr/how-does-the-full-fact-team-choose-what-to-fact-check/
SRC-005 | ◈ | fam:E | CORRECTIV-FACTCHECK-FAQ | CORRECTIV.Faktencheck — FAQ | 2026-09-08 | 2026-09-08T16:30:00+02:00 | topic selection criteria; reader submissions; Meta cooperation | https://correctiv.org/faktencheck/faq-haeufig-gestellte-fragen-an-das-faktencheck-team/
SRC-006 | ◈ | fam:other:maldita | MALDITA-METHODOLOGY | Maldita.es — Metodología | 2025-06-13 | 2026-09-08T16:30:00+02:00 | selection section, virality/dangerousness and community inputs | https://maldita.es/metodologia-maldita/
SRC-007 | ◈ | fam:other:reuters | REUTERS-FACTCHECK-ABOUT | Reuters Fact Check — About | 2026-09-08 | 2026-09-08T16:30:00+02:00 | methodology lines 166-181; editorial control line 220; funding lines 316-324 | https://www.reuters.com/fact-check/about/
SRC-008 | ◉ | fam:other:jeea | DOI:10.1093/jeea/jvaf011 | Journal of the European Economic Association — Both Judge and Party? | 2025-03-19 | 2026-09-08T16:30:00+02:00 | abstract; Table 3 aligned coefficient; limitations; conclusion | https://academic.oup.com/jeea/article/23/6/2137/8087339
SRC-009 | ○ | fam:other:meta | META-2025-TPFC-END | Meta — More Speech and Fewer Mistakes | 2025-01-07 | 2026-09-08T16:30:00+02:00 | Ending Third Party Fact Checking Program; stated rationale on selection choices | https://about.fb.com/news/2025/01/meta-more-speech-fewer-mistakes/
SRC-010 | ◈ | fam:other:lemonde | LEMONDE-DECODEURS-CHARTER | Le Monde — Charte des Décodeurs | 2021-11-03 | 2026-09-08T16:30:00+02:00 | selection and suggestion criteria lines 396-424; page modified 2021-11-03 | https://www.lemonde.fr/les-decodeurs/article/2014/03/10/la-charte-des-decodeurs_4365106_4355770.html

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://factcheck.afp.com/How-we-work | A | 2026-09-08 | AFP selection: virality impact harm | AFP states that its fact-checkers prioritize dubious online claims that are viral, impactful and potentially harmful to the public. | -
FCT-002 | FACT | ✧ | https://factcheck.afp.com/How-we-work | A | 2026-09-08 | AFP selection: public interest and evidentiary feasibility | AFP says it selects claims by assessing public interest and whether clear, sufficient evidence can be gathered; it does not publish a fact-check if strong cross-checked evidence cannot be established. | -
FCT-003 | FACT | ✧ | https://factcheck.afp.com/How-we-work | A | 2026-09-08 | AFP selection: political neutrality rule | AFP states it applies the same investigative approach regardless of claimant and does not focus on one candidate, party or website, while allowing more checks of consistent spreaders of potentially harmful misinformation. | -
FCT-004 | FACT | ✧ | https://factcheck.afp.com/How-we-work | A | 2026-09-08 | AFP editorial authority over proposed checks | AFP states that journalists liaise with regional editors, who discuss claims and proposed fact-checks, assess evidence needs and edit articles before publication. | -
FCT-005 | FACT | ✧ | https://factcheck.afp.com/How-we-work | A | 2026-09-08 | AFP Meta candidate-pool input | AFP states that posts flagged on Facebook and Instagram under Meta third-party fact checking are considered among the material it investigates. | -
FCT-006 | FACT | ✧ | https://ifcncodeofprinciples.poynter.org/the-commitments | B | 2026-09-08 | IFCN selection standard | IFCN requires signatories to consider reach and importance when selecting claims and to publish how they select claims. | -
FCT-007 | FACT | ✧ | https://ifcncodeofprinciples.poynter.org/the-commitments | B | 2026-09-08 | IFCN methodology standard | IFCN requires a public methodology covering selection, research, writing and publication, and says claims should be selected primarily on reach and importance. | -
FCT-008 | FACT | ✧ | https://ifcncodeofprinciples.poynter.org/the-commitments | B | 2026-09-08 | IFCN state/political editorial-control boundary | IFCN excludes organizations whose editorial work is controlled by a state, political party or politician, while allowing public-service funding when editorial control is clearly separated. | -
FCT-009 | FACT | ✧ | https://efcsn.com/code-of-standards/ | C | 2026-09-08 | EFCSN impartiality selection constraint | EFCSN requires verified members not to focus investigations unduly on one political party or side of the political spectrum. | -
FCT-010 | FACT | ✧ | https://efcsn.com/code-of-standards/ | C | 2026-09-08 | EFCSN editorial-control transparency | EFCSN requires members to make clear how and by whom editorial control is exercised and to identify editors or decision makers. | -
FCT-011 | FACT | ✧ | https://efcsn.com/code-of-standards/ | C | 2026-09-08 | EFCSN funding and independence transparency | EFCSN requires disclosure of platform/public income sources and an explanation of mechanisms ensuring editorial independence and the work funded by potentially conflicting sources. | -
FCT-012 | FACT | ✧ | https://fullfact.org/blog/2025/apr/how-does-the-full-fact-team-choose-what-to-fact-check/ | D | 2025-04-03 | Full Fact prioritizes prominence and reach | Full Fact says a higher-profile claimant and wider reach can cause one claim to be selected over another. | -
FCT-013 | FACT | ✧ | https://fullfact.org/blog/2025/apr/how-does-the-full-fact-team-choose-what-to-fact-check/ | D | 2025-04-03 | Full Fact prioritizes repetition and harm | Full Fact says repeated claims and claims with potential harm to people, institutions, groups or democratic processes receive greater priority. | -
FCT-014 | FACT | ✧ | https://fullfact.org/blog/2025/apr/how-does-the-full-fact-team-choose-what-to-fact-check/ | D | 2025-04-03 | Full Fact uses multiple secondary selection signals | Full Fact lists Meta-partnership eligibility, virality, breaking-news relevance, novelty, reader requests and expected audience interest among additional considerations. | -
FCT-015 | FACT | ✧ | https://correctiv.org/faktencheck/faq-haeufig-gestellte-fragen-an-das-faktencheck-team/ | E | 2026-09-08 | CORRECTIV selection criteria | CORRECTIV says selection is necessary because not all online misinformation can be checked and lists current relevance, reach/virality and potential harm as key criteria. | -
FCT-016 | FACT | ✧ | https://correctiv.org/faktencheck/faq-haeufig-gestellte-fragen-an-das-faktencheck-team/ | E | 2026-09-08 | CORRECTIV community input | CORRECTIV says it searches proactively and also takes reader/community submissions through WhatsApp and its Faktenforum. | -
FCT-017 | FACT | ✧ | https://correctiv.org/faktencheck/faq-haeufig-gestellte-fragen-an-das-faktencheck-team/ | E | 2026-09-08 | CORRECTIV Meta effect boundary | CORRECTIV states its Meta-linked fact checks can trigger warnings and reduced reach, but that its fact-checking work does not control deletion decisions. | -
FCT-018 | FACT | ✧ | https://maldita.es/metodologia-maldita/ | other:maldita | 2025-06-13 | Maldita selection: virality | Maldita says it prioritizes viral content using repeated reports, social diffusion, prominence of the sharer and circulation across formats. | -
FCT-019 | FACT | ✧ | https://maldita.es/metodologia-maldita/ | other:maldita | 2025-06-13 | Maldita selection: dangerousness | Maldita says potentially harmful misinformation can be prioritized before it becomes viral, especially in health, emergencies, attacks, disasters or threats to social coexistence. | -
FCT-020 | FACT | ✧ | https://maldita.es/metodologia-maldita/ | other:maldita | 2025-06-13 | Maldita community shapes candidate discovery | Maldita describes community reporting and collaborative platforms as inputs that help identify circulating misinformation and support investigations. | -
FCT-021 | FACT | ✧ | https://www.reuters.com/fact-check/about/ | other:reuters | 2026-09-08 | Reuters selection criteria | Reuters Fact Check says material is selected using editorial value, potential real-world harm, actual reach, potential reach and separability of fact from opinion. | -
FCT-022 | FACT | ✧ | https://www.reuters.com/fact-check/about/ | other:reuters | 2026-09-08 | Reuters internal editorial control | Reuters states its fact-check unit is within editorial and that its digital verification editor has editorial control of output with support from senior editors. | -
FCT-023 | FACT | ✧ | https://www.reuters.com/fact-check/about/ | other:reuters | 2026-09-08 | Reuters platform funding relationships | Reuters discloses that Facebook and TikTok fund its fact-checking unit in exchange for content-authenticity or misinformation assessments, and that it provides fact-checking services to LinkedIn. | -
FCT-024 | FACT | ✧ | https://academic.oup.com/jeea/article/23/6/2137/8087339 | other:jeea | 2025-03-19 | JEEA French fact-check dataset | The 2025 JEEA study analyzes 2,405 articles from six main general-interest French fact-checkers through July 2021. | -
FCT-025 | FACT | ✧ | https://academic.oup.com/jeea/article/23/6/2137/8087339 | other:jeea | 2025-03-19 | JEEA pooled alignment association | In the study pooled specification, alignment between a fact-checker affiliated outlet and political orientation is associated with a 0.05 lower share of articles on that orientation, reported as statistically significant in the study. | -
FCT-026 | FACT | ✧ | https://academic.oup.com/jeea/article/23/6/2137/8087339 | other:jeea | 2025-03-19 | JEEA selection asymmetry conclusion | The study concludes that fact-checkers are relatively less likely to check ideologically aligned entities and, when they do, more likely to select statements they assess as correct. | -
FCT-027 | FACT | ✧ | https://academic.oup.com/jeea/article/23/6/2137/8087339 | other:jeea | 2025-03-19 | JEEA causal and ground-truth limitation | The study explicitly states that the underlying distribution of incorrect statements is unobserved, so the results cannot establish that all fact-checkers are biased from ground truth; content differences may also arise without deliberate rule violations. | -
FCT-028 | FACT | ✧ | https://www.lemonde.fr/les-decodeurs/article/2014/03/10/la-charte-des-decodeurs_4365106_4355770.html | other:lemonde | 2021-11-03 | Le Monde Décodeurs selection criteria | Les Décodeurs state that claim selection depends on relevance to current events/public debate and factual verifiability; reader suggestions are further evaluated by source provenance, apparent veracity, virality and public importance. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-001
FCT-005 | SRC-001
FCT-006 | SRC-002
FCT-007 | SRC-002
FCT-008 | SRC-002
FCT-009 | SRC-003
FCT-010 | SRC-003
FCT-011 | SRC-003
FCT-012 | SRC-004
FCT-013 | SRC-004
FCT-014 | SRC-004
FCT-015 | SRC-005
FCT-016 | SRC-005
FCT-017 | SRC-005
FCT-018 | SRC-006
FCT-019 | SRC-006
FCT-020 | SRC-006
FCT-021 | SRC-007
FCT-022 | SRC-007
FCT-023 | SRC-007
FCT-024 | SRC-008
FCT-025 | SRC-008
FCT-026 | SRC-008
FCT-027 | SRC-008
FCT-028 | SRC-010

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
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8
CP-002 | SEARCH | PASS | LAST_COMPLETED:9:ECOSYSTEM | NEXT_ACTION:10
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-004 | CAUSAL_GAP | PASS | LAST_COMPLETED:11:CAU-001 | NEXT_ACTION:12
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-07T23:04:04.575760+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":28,"eligible":28,"failure":0,"success":0}}

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
