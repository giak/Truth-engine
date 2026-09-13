ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260907-2247-efcsn-factcheck-access | PARENT_RUN_ID:NONE | AS_OF:2026-09-07
INPUT_KIND:RUN_CARD | MISSION_MODE:RECHECK_EXTEND | INPUT_REF:PATH:/mnt/data/inv045-exec/te/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-07_efcsn-factcheck-access/2026-09-07_22-47_efcsn-factcheck-access_INPUT.md | SUBJECT_SLUG:efcsn-factcheck-access | SUBJECT_FP:sha256:0d3e4cd412dc8e208507a8374cdecdea5e34491686ba12cec8a4b94a88b80b54 | INPUT_SHA256:sha256:3352149804cd10c0abdbdb46dae53fdeda1e1a8fe2b9c9c892373cbf4efd092b
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/EU 2019-2026; EFCSN central, IFCN comparator; trace standards/certification, governance, appeals, funding, platform/program access, subgrants and editorial-control boundaries.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/MONEY.md,clusters/POWER.md,clusters/NETWORK.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Investigation technique — certification fact-checking et infrastructure d'accès

## 1. Question et règle de preuve

L'objet n'est pas de décider si un label EFCSN ou IFCN garantit la vérité d'un contenu. Il s'agit de déterminer si ces dispositifs de certification créent des **droits d'accès ou avantages matériels documentables** — adhésion, subventions, bases de données, programmes de plateformes — et jusqu'où ces accès permettent d'inférer un pouvoir éditorial ou politique.

La chaîne testée est :

`standard -> certification -> éligibilité/accès -> ressource/capacité -> sélection éditoriale/publication -> exposition -> effet politique`.

Chaque arête reste indépendante. `certification != truth`, `funding != command`, `access != control` et `selection_effect != political_effect` sont des gardes de l'enquête.

## 2. EFCSN : certification organisationnelle et gouvernance

Le Code EFCSN impose une procédure formelle de conformité avant adhésion. Les critères portent notamment sur méthodologie, corrections, gouvernance, financement et transparence. Le Governance Body tranche les candidatures selon une majorité qualifiée ; EFCSN se décrit comme une association pilotée par ses membres, non comme une autorité publique. Des mécanismes de plainte et de conformité existent.

Cette architecture ferme un pouvoir réel : **admettre, refuser, renouveler ou sanctionner un statut de membre vérifié**. Elle ne transforme pas EFCSN en juge public de la vérité de chaque article.

## 3. Un gate d'accès explicite : FACTEUR Database Grants

Le cas le plus fort de l'enquête est le programme FACTEUR. La Commission a accordé 5 millions d'euros à un consortium mené par EFCSN, qui annonce redistribuer plus de 60 % de la subvention. Dans l'appel Database Grants de 2026, la certification EFCSN est une condition explicite d'éligibilité. L'appel dispose d'un budget de 860 000 euros, prévoit 40 à 60 subventions, et associe l'aide financière à l'accès au backoffice de la base de fact-checks et à un accord de licence de données.

Ici, `certification -> eligibility` est donc **VERIFIED**. C'est une infrastructure d'accès au sens matériel, pas seulement un badge symbolique.

Mais ce gate reste borné au programme : l'appel général de la Commission pour le réseau européen de fact-checkers et un appel séparé de visibilité utilisent des cadres d'éligibilité plus larges. Le corpus ne permet pas d'élever `EFCSN certification -> accès universel au financement européen` au rang de règle générale.

## 4. IFCN : condition d'accès à certains programmes de plateformes

IFCN fournit un comparateur externe. Son Code repose sur des critères publics, des évaluateurs externes et une revue par son advisory board. Il exige notamment une séparation nette lorsque des financements publics ou politiques existent.

Surtout, IFCN indique explicitement que Meta, Google et TikTok ont utilisé le statut de signataire vérifié comme condition d'accès à certains programmes ou politiques de fact-checking. IFCN précise aussi que ce statut est généralement **nécessaire mais non suffisant**, et qu'il ne négocie pas ces relations pour les signataires.

Ce résultat confirme qu'une certification privée peut devenir un **gate d'accès tiers** sans que le certificateur contrôle ensuite la décision de la plateforme ou l'activité éditoriale du partenaire.

## 5. EDMO : coordination financée, indépendance formelle

EDMO fournit une infrastructure distincte de collaboration : briefs, enquêtes coopératives, cartographie, repository et formations. Le call 2026 des hubs demande explicitement que leurs activités soient réalisées en pleine indépendance des tiers, y compris des autorités publiques, et exige la présence d'organisations de fact-checking dans les hubs. Les hubs doivent coopérer avec les repositories et initiatives européennes, dont le réseau européen de fact-checkers.

Le corpus établit donc une **interconnexion institutionnelle financée** entre certification, hubs, repositories et programmes européens, mais pas un commandement éditorial centralisé.

## 6. Pouvoir, ressources et limites

Trois pouvoirs distincts sont établis :

1. pouvoir associatif de certification/membership ;
2. pouvoir d'éligibilité et d'allocation dans certains programmes financés ;
3. rôle de vérification préalable ouvrant certains programmes de plateformes.

Ils ne doivent pas être fusionnés avec :

- autorité réglementaire de l'État ;
- contrôle de la ligne éditoriale ;
- décision de modération d'une plateforme ;
- preuve d'effet politique.

Les standards EFCSN/IFCN exigent d'ailleurs la transparence des financements et des mécanismes de séparation éditoriale. Ces garanties ne prouvent pas une neutralité parfaite ; elles empêchent seulement de transformer le financement en commandement sans preuve supplémentaire.

## 7. Modèles concurrents

### M1 — simple standard professionnel sans pouvoir matériel

**REFUTED / TOO WEAK.** Les conditions explicites d'accès aux Database Grants et à certains programmes de plateformes démontrent un pouvoir matériel borné.

### M2 — infrastructure distribuée de gatekeeping professionnel

**ESTABLISHED / BOUNDED.** Plusieurs programmes convertissent un statut de certification en condition d'accès, reconnaissance ou avantage. Le pouvoir est fragmenté entre certifier, financer et opérer les programmes.

### M3 — chaîne publique de commandement éditorial

**NOT_ESTABLISHED.** Le financement européen est matériel, mais aucun élément du corpus ne ferme `Commission/EFCSN/IFCN -> instruction sur le choix ou la conclusion d'un fact-check individuel`.

### M4 — gate universel de l'écosystème européen

**NOT_ESTABLISHED.** Des appels européens et les hubs EDMO utilisent des conditions plus larges ou distinctes ; les gates observés sont spécifiques à certains programmes.

## 8. Plafond causal

`I0-I3` sont bien fermés pour les acteurs, règles, financements, procédures de certification et certains accès. `I4` est partiel : des ressources, backoffices et programmes peuvent augmenter la capacité et la distribution. `I5-I7` restent ouverts : la sélection éditoriale imposée, la persuasion et l'effet électoral ne sont pas établis.

Le delta terminal est :

**certification comme infrastructure d'accès bornée établie ; financement et pouvoir de gatekeeping réels ; autorité publique générale, commandement éditorial et effet politique causal non établis.**

## 9. Routing

Ce résultat alimente `INV-144` : il fournit une boucle économique concrète à tester dans la synthèse `standards/certification -> éligibilité -> subventions/plateformes/repository -> capacité`. Il ne démontre ni mauvaise foi ni « industrie » fabriquant la menace ; cette qualification reste à tester avec budgets, bénéficiaires, métriques et contrôles des autres dépendances.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:5|SRC_COMPLETE:14/14

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-07
- **notes:**
  - FACTEUR grant signed 2026-03-31
  - Database Grants published 2026-07-29
  - EDMO 2026 call dated 2025-10-09
- **status:** CURRENT_WITH_2026_PROGRAMS
- **window:** 2019-2026

### MANIPULATION_REPORT
- **assumptions:**
  - official program documents establish bounded eligibility/funding terms, not hidden motive
  - standards documents establish formal safeguards, not perfect neutrality
  - certifier statements about platform conditions are retained as first-party descriptions of their role
- **clusters:**
  - **loaded:**
    - clusters/MONEY.md
    - clusters/POWER.md
    - clusters/NETWORK.md
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - certification can create practical access advantages without controlling editorial conclusions
  - public funding can amplify capacity without proving tasking
  - a program-specific gate is not a universal ecosystem gate
- **input_kind:** RUN_CARD
- **mission_mode:** RECHECK_EXTEND
- **patterns:**
  - certification
  - membership
  - subgrant
  - repository
  - platform program
  - EDMO hub
  - complaints
- **priorities:**
  - formal gate evidence
  - resource allocation
  - governance
  - independence
  - negative controls
  - causal effect
- **query_guidance:** prove each gate from eligibility text; distinguish certifier decision from funder/platform decision and from editorial choice
- **rhetorical:**
  - **AUTH:** first-party organisational and EU documents establish their own rules only
  - **BF:** N/A
  - **DEM:** specific grant/program gates cannot be generalized to all fact-checking
  - **FAC:** separate certification, access, funding, editorial control and effect
  - **NUM:** budgets and member counts do not establish command
- **speaker:**
  - **goal:** forensic access-infrastructure assessment
  - **target:** standard -> status -> access -> resource -> control/effect
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
  - certification=truth
  - funding=command
  - access=control
  - membership=state authority
  - selection effect=political effect

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - downstream beneficiary outcomes beyond published calls
  - **input_ids:**
    - FCT-008
    - FCT-010
    - FCT-013
    - FCT-017
  - **module:** clusters/MONEY.md
  - **negative_results:**
    - no evidence that grant funding dictates article conclusions
  - **not_computable:**
    - complete ecosystem revenue share
  - **operations_applied:**
    - mapped Commission grant to consortium and downstream subgrants
    - separated funding from editorial tasking
  - **reason:** public grants, subgrants and access-linked financial benefits
  - **result_ids:**
    - CLM-003
    - CTRL-003
  - **status:** DONE
  - **trigger:** €
- **item 2:**
  - **gaps:**
    - private contract terms beyond published descriptions
  - **input_ids:**
    - FCT-001
    - FCT-002
    - FCT-012
    - FCT-025
    - FCT-026
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no public-regulator authority of EFCSN/IFCN
  - **not_computable:**
    - unobserved applicant chilling effect
  - **operations_applied:**
    - identified decision authority
    - tested bounded versus universal gatekeeping
  - **reason:** certification decisions and access gates
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-004
    - CTRL-001
    - CTRL-002
    - CTRL-004
  - **status:** DONE
  - **trigger:** ↕
- **item 3:**
  - **gaps:**
    - case-level platform selection decisions
  - **input_ids:**
    - FCT-009
    - FCT-018
    - FCT-020
    - FCT-021
    - FCT-025
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - network position does not establish editorial command
  - **not_computable:**
    - informal influence without records
  - **operations_applied:**
    - mapped institutional interfaces
    - separated coordination from command
  - **reason:** interfaces among Commission, EFCSN, EDMO, IFCN and platforms
  - **result_ids:**
    - CLM-003
    - CLM-004
    - CLM-006
    - LED-001
    - LED-002
  - **status:** DONE
  - **trigger:** 🌐

### SCOPING_REPORT
- **excluded:**
  - truthfulness of every individual fact-check
  - generic ideological criticism without access/control evidence
  - platform moderation outcomes not tied to documented certification program
- **guards:**
  - certification != truth
  - funding != command
  - access != control
  - membership != state_authority
  - grant != editorial_tasking
  - code_compliance != censorship
  - selection_effect != political_effect
- **included:**
  - EFCSN standards, governance, application, complaints and fees
  - EU grants/calls and FACTEUR subgrants
  - EDMO fact-checking/hub interfaces
  - IFCN verification and platform-program conditions
- **route:** INV-144

### CREDO
- certification != truth
- funding != command
- access != control
- membership != state_authority
- grant != editorial_tasking
- code_compliance != censorship
- selection_effect != political_effect

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** RECHECK_EXTEND
- **patterns:**
  - standards certification
  - membership gate
  - subgrant eligibility
  - platform-program condition
  - repository access
  - funding transparency
  - complaints/enforcement
- **priorities:**
  - who certifies
  - decision rule
  - access conditioned on status
  - resource flow
  - editorial independence
  - complaint/recourse
  - effect ceiling
- **query_guidance:** trace standard -> certification decision -> access condition -> grant/platform/repository -> editorial autonomy -> exposure/effect
- **speaker:**
  - **goal:** classify certification as bounded access infrastructure
  - **target:** certifier-access-resource-control-effect chain
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **threats:**
  - certification=truth
  - funding=command
  - membership=state authority
  - access=editorial control

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** FACTEUR Database Grants explicitly require EFCSN certification and IFCN status conditions some platform programs.
  - **resolution:** Certification is a real bounded access infrastructure in specific programs, not merely symbolic.
  - **thesis:** EFCSN certification is merely a voluntary badge with no material access consequences.
- **item 2:**
  - **antithesis:** EFCSN/IFCN standards require funding transparency/editorial separation and EDMO hub calls require independence from public authorities.
  - **resolution:** Funding/capacity is established; editorial tasking requires separate evidence.
  - **thesis:** EU funding of fact-checkers proves Commission editorial control.
- **item 3:**
  - **antithesis:** Commission calls and EDMO participation use broader eligibility frameworks; no universal certification rule is established.
  - **resolution:** Gatekeeping is program-specific.
  - **thesis:** Certification is a universal gateway to European fact-checking activity.
- **item 4:**
  - **antithesis:** Codes assess organisational methodology, transparency and governance and include complaint/correction mechanisms.
  - **resolution:** Certification is compliance verification, not article-by-article truth adjudication.
  - **thesis:** Verified status means the certifier guarantees factual correctness of all publications.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **boundary:** grant != command
  - **from:** European Commission
  - **support:**
    - FCT-008
    - FCT-009
  - **to:** FACTEUR consortium
  - **vehicle:** €5m grant
- **item 2:**
  - **boundary:** program eligibility and ranking are documented
  - **from:** FACTEUR
  - **support:**
    - FCT-010
    - FCT-013
    - FCT-014
  - **to:** European fact-checking organisations
  - **vehicle:** subgrants >60% of project / Database Grants €860k
- **item 3:**
  - **boundary:** status necessary not sufficient for some programs
  - **from:** IFCN verified status
  - **support:**
    - FCT-025
    - FCT-026
    - FCT-027
  - **to:** platform programs/tools
  - **vehicle:** program eligibility/benefits

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** European Commission/HaDEA
  - **limits:**
    - funding != editorial tasking
  - **relation:** grant/call framework
  - **support:**
    - FCT-008
    - FCT-009
    - FCT-019
    - FCT-020
  - **to:** EFCSN-led FACTEUR / EDMO hubs
- **item 2:**
  - **from:** EFCSN Governance Body / assessors
  - **limits:**
    - certification != truth
  - **relation:** assessment/certification
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
    - FCT-004
  - **to:** fact-checking organisations
- **item 3:**
  - **from:** IFCN verification
  - **limits:**
    - necessary != sufficient
    - IFCN does not negotiate platform relationship
  - **relation:** status condition
  - **support:**
    - FCT-022
    - FCT-025
    - FCT-026
  - **to:** some platform fact-checking programs

### IMPACT_MAP
- **certification_access:** VERIFIED_BOUNDED
- **editorial_command:** NOT_ESTABLISHED
- **electoral_effect:** NOT_ESTABLISHED_COUNTERFACTUALLY
- **funding_capacity:** VERIFIED
- **political_behavior:** NOT_ESTABLISHED
- **support:**
  - FCT-012
  - FCT-013
  - FCT-015
  - FCT-025
  - FCT-026
  - FCT-028

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** status is explicit eligibility for some grants/platform programs
  - **issue:** voluntary badge versus access gate
  - **pro:** membership/signatory status is voluntary
  - **resolution:** BOUNDED_GATEKEEPING
- **item 2:**
  - **contra:** formal independence and funding-separation rules exist
  - **issue:** public funding versus editorial independence
  - **pro:** EU grants materially fund the ecosystem
  - **resolution:** FUNDING_ESTABLISHED_COMMAND_NOT_ESTABLISHED
- **item 3:**
  - **contra:** EFCSN is member-driven and IFCN is a Poynter unit, not a regulator
  - **issue:** certifier authority versus public authority
  - **pro:** certifiers decide membership/signatory status
  - **resolution:** PRIVATE_ASSOCIATIONAL_AUTHORITY
- **item 4:**
  - **contra:** no causal voter/electoral design in corpus
  - **issue:** access advantage versus political effect
  - **pro:** grants/repositories/platform programs can expand capacity/reach
  - **resolution:** EFFECT_CEILING_I5_I7_OPEN

### VERIFICATION_REPORT
- **cross_checks:**
  - EFCSN certification rule versus broader Commission calls
  - EU funding versus formal editorial-independence clauses
  - IFCN platform condition versus necessary-not-sufficient caveat
- **facts:** 28
- **limitations:**
  - no direct platform contract text in corpus
  - no denominator for rejected applicants across all programs
  - no causal political-outcome dataset
- **negative_controls:**
  - Commission top-level call broader eligibility
  - EDMO public-authority independence requirement
  - IFCN necessary-not-sufficient platform condition
- **primary_or_official_dominant:** true
- **provenance_families:** 5
- **sources:** 14
- **verdict:** READY_FOR_PRE_GATE

### EDI_REPORT
- **corpus:**
  - **circularity:** MODERATE_WITHIN_SECTOR
  - **coverage:** STRONG_FOR_FORMAL_STANDARDS_FUNDING_AND_ACCESS_GATES_PARTIAL_FOR_EDITORIAL_EFFECT
  - **independence:** FIVE_PROVENANCE_FAMILIES_WITH_EFCSN_EC_EDMO_HADEA_IFCN
  - **limits:**
    - sector sources describe their own governance/programs
    - no platform contract text beyond IFCN first-party description
    - no causal political-outcome dataset
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **gap_type:** SCOPE
    - **independent_families:** 2
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES
    - **gap_type:** SCOPE
    - **independent_families:** 2
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** YES
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 2
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** YES_WITH_BOUNDARIES
    - **gap_type:** SCOPE
    - **independent_families:** 3
  - **item 5:**
    - **claim_id:** CLM-006
    - **direct_object:** NO_CAUSAL_DESIGN
    - **gap_type:** CAUSALITY
    - **independent_families:** 4
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** 5_PROVENANCE_FAMILIES
  - **perspective:** EFCSN+EU_COMMISSION+EDMO+HADEA+IFCN
  - **stratification:** STANDARDS+GOVERNANCE+GRANTS+SUBGRANTS+PLATFORM_ACCESS+REPOSITORIES
  - **temporal:** 2019-2026
- **edi:**
  - **assessment:** STRONG_FORMAL_GATE_AND_RESOURCE_COVERAGE_WITH_EDITORIAL_CAUSAL_GAPS
  - **flags:**
    - PRIMARY_FIRST_PARTY_DOMINANT
    - EXPLICIT_ACCESS_GATE_POSITIVE_CONTROL
    - NON_UNIVERSAL_GATE_NEGATIVE_CONTROL
    - NO_CAUSAL_ELECTORAL_DESIGN
- **source_counts:**
  - **claim_source:** 0
  - **primary:** 14
  - **provenance_families:** 5
  - **secondary:** 0
  - **total:** 14

### RESPONSIBILITY_MAP
- **boundary:** certification status can condition access and resource flows without establishing funder/certifier control over individual editorial conclusions
- **not_established:**
  - Commission tasking of individual fact-checks
  - EFCSN/IFCN command over individual conclusions
  - universal certification gate
  - causal political/electoral effect
- **verified:**
  - EFCSN membership decision structure
  - FACTEUR funding and regranting
  - EFCSN certification gate for Database Grants
  - IFCN condition for some platform programs
  - EDMO independence requirement

### NEXT_QUERIES
- RECHECK only if platform contract text shows stronger certification/control relation
- RECHECK only if EU/EFCSN subgrant decision records show editorial conditions
- DEFER causal political-effect study pending exposure/outcome design

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-006,QRY-007,QRY-008,QRY-010,QRY-012 | support:- | counter:- | results:FCT-012,FCT-016,FCT-017,FCT-019,FCT-020,FCT-025,FCT-026 | final:GAP | gap:SCOPE
LED-002 | attempts:QRY-001,QRY-004,QRY-010,QRY-011,QRY-015 | support:- | counter:- | results:FCT-005,FCT-008,FCT-019,FCT-023,FCT-024,FCT-028 | final:GAP | gap:RESPONSIBILITY
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-011,QRY-014 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-006,FCT-007,FCT-022,FCT-023 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-004,QRY-005,QRY-006,QRY-007,QRY-008 | support:- | counter:- | results:FCT-008,FCT-009,FCT-010,FCT-011,FCT-013,FCT-014,FCT-017 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-006,QRY-012,QRY-013 | support:- | counter:- | results:FCT-012,FCT-015,FCT-025,FCT-026,FCT-027 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-001,QRY-010,QRY-011,QRY-015 | support:- | counter:- | results:FCT-005,FCT-019,FCT-023,FCT-024,FCT-028 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-001,QRY-003,QRY-013,QRY-014 | support:- | counter:- | results:FCT-003,FCT-004,FCT-022 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-004,QRY-006,QRY-008,QRY-012,QRY-015 | support:- | counter:- | results:FCT-008,FCT-010,FCT-013,FCT-015,FCT-017,FCT-025,FCT-028 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-011,QRY-014,SRC-001,SRC-002,SRC-003,SRC-011,SRC-014 | support:FCT-001,FCT-002,FCT-003,FCT-022,FCT-023 | counter:CTRL-001 | results:FCT-001,FCT-002,FCT-003,FCT-022,FCT-023,CTRL-001 | final:SUPPORTED | gap:SCOPE
CLM-002 | attempts:QRY-006,QRY-012,SRC-006,SRC-012 | support:FCT-012,FCT-013,FCT-014,FCT-015,FCT-025,FCT-026 | counter:CTRL-002 | results:FCT-012,FCT-013,FCT-014,FCT-015,FCT-025,FCT-026,CTRL-002 | final:SUPPORTED | gap:SCOPE
CLM-003 | attempts:QRY-004,QRY-005,QRY-006,SRC-004,SRC-005,SRC-006 | support:FCT-008,FCT-009,FCT-010,FCT-011,FCT-013,FCT-014 | counter:CTRL-003 | results:FCT-008,FCT-009,FCT-010,FCT-011,FCT-013,FCT-014,CTRL-003 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-004 | attempts:QRY-007,QRY-008,QRY-009,QRY-010,SRC-007,SRC-008,SRC-009,SRC-010 | support:FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021 | counter:CTRL-004 | results:FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021,CTRL-004 | final:SUPPORTED | gap:SCOPE
CLM-005 | attempts:QRY-001,QRY-002,QRY-003,QRY-011,QRY-014,SRC-001,SRC-002,SRC-003,SRC-011,SRC-014 | support:FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-022 | counter:CTRL-005 | results:FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-022,CTRL-005 | final:SUPPORTED | gap:BIAS
CLM-006 | attempts:QRY-001,QRY-006,QRY-011,QRY-012,SRC-001,SRC-006,SRC-011,SRC-012 | support:FCT-023,FCT-024,FCT-026,FCT-028 | counter:CTRL-006 | results:FCT-023,FCT-024,FCT-026,FCT-028,CTRL-006 | final:SUPPORTED | gap:RESPONSIBILITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-001 | CLM | SUPPORTED | SCOPE | Certification evaluates organisational compliance, not the truth of every future article.
CLM-002 | CLM | SUPPORTED | SCOPE | These gates are program-specific and do not establish universal control of funding or platforms.
CLM-003 | CLM | SUPPORTED | RESPONSIBILITY | Funding and allocation authority do not establish editorial command over individual fact-checks.
CLM-004 | CLM | SUPPORTED | SCOPE | Program-specific eligibility documents may impose additional conditions not represented in every summary page.
CLM-005 | CLM | SUPPORTED | BIAS | Safeguards do not prove absence of bias or perfect consistency in selection decisions.
CLM-006 | CLM | SUPPORTED | RESPONSIBILITY | Case-specific contracts or private communications could alter the responsibility assessment if later produced.
CAU-001 | CAU | GAP | CAUSALITY | The chain is established through some access/capacity edges but not through editorial tasking, persuasion or political outcome.

SEMANTIC_COUNTS_V1:LED:2|CLM:6|AXS:6|CAU:1|CTRL:6|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-006","QRY-007","QRY-008","QRY-010","QRY-012"],"evidence_excerpt":"Explicit gates exist for FACTEUR Database Grants and some IFCN-linked platform programs, while other EU calls use broader eligibility conditions.","gap":"No universal certification prerequisite is established across the whole EU fact-checking ecosystem.","gap_type":"SCOPE","kind":"SCOPE_GAP","lead":"Certification gate is real but program-specific, not universal","linked_ids":["CLM-002","CLM-004","CTRL-002","CTRL-004"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-012","FCT-016","FCT-017","FCT-019","FCT-020","FCT-025","FCT-026"],"routes":["INV-144"],"source_id":"INV-045_RUN_CARD","status":"GAP"}
LED-002 | {"attempt_ids":["QRY-001","QRY-004","QRY-010","QRY-011","QRY-015"],"evidence_excerpt":"Funding, certification and access effects are documented, but standards require editorial separation and no source closes individual tasking or political outcome.","gap":"Direct editorial tasking, selection manipulation and causal political effect remain unclosed.","gap_type":"RESPONSIBILITY","kind":"CAUSAL_GAP","lead":"Certification/funding to editorial command or political effect","linked_ids":["CLM-003","CLM-006","CAU-001","CTRL-003","CTRL-006"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-005","FCT-008","FCT-019","FCT-023","FCT-024","FCT-028"],"routes":["INV-144","INV-133"],"source_id":"INV-045_RUN_CARD","status":"GAP"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"EFCSN and IFCN operate standards-based certification systems that confer verified membership/signatory status through formal assessment, rather than exercising public-law truth adjudication.","claimant":"INV-045 synthesis","counter":"CTRL-001","gap":"Certification evaluates organisational compliance, not the truth of every future article.","gap_type":"SCOPE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-022","FCT-023"]}
CLM-002 | {"claim":"Certification can function as access infrastructure in bounded contexts: EFCSN certification is an explicit eligibility condition for FACTEUR Database Grants, and IFCN verified status is a condition for some platform fact-checking programs.","claimant":"INV-045 synthesis","counter":"CTRL-002","gap":"These gates are program-specific and do not establish universal control of funding or platforms.","gap_type":"SCOPE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-012","FCT-013","FCT-014","FCT-015","FCT-025","FCT-026"]}
CLM-003 | {"claim":"EU public funding materially strengthens fact-checking capacity and places subgrant/database-allocation functions inside an EFCSN-led consortium.","claimant":"INV-045 synthesis","counter":"CTRL-003","gap":"Funding and allocation authority do not establish editorial command over individual fact-checks.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-008","FCT-009","FCT-010","FCT-011","FCT-013","FCT-014"]}
CLM-004 | {"claim":"EFCSN/IFCN certification is not shown to be a universal prerequisite for all EU fact-checking funding, EDMO participation, or fact-checking activity.","claimant":"INV-045 synthesis","counter":"CTRL-004","gap":"Program-specific eligibility documents may impose additional conditions not represented in every summary page.","gap_type":"SCOPE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021"]}
CLM-005 | {"claim":"The certification systems include governance and accountability safeguards, including member governance, external assessment, disclosure requirements and complaint/review mechanisms.","claimant":"INV-045 synthesis","counter":"CTRL-005","gap":"Safeguards do not prove absence of bias or perfect consistency in selection decisions.","gap_type":"BIAS","materiality":"HIGH","status":"SUPPORTED","support":["FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-022"]}
CLM-006 | {"claim":"The examined corpus does not establish that EFCSN, IFCN or EU funders dictate individual editorial conclusions or that certification status has a demonstrated causal political/electoral effect.","claimant":"INV-045 synthesis","counter":"CTRL-006","gap":"Case-specific contracts or private communications could alter the responsibility assessment if later produced.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-023","FCT-024","FCT-026","FCT-028"]}

### AXIS_REGISTRY_V1
AXS-001 | {"assessment":"VERIFIED","attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-011","QRY-014"],"axis":"standards_and_certification","links":["CLM-001","CLM-005"],"question":"What is certified, by whom, under which criteria and final decision rule?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-006","FCT-007","FCT-022","FCT-023"],"sought_objects":["CODE","ASSESSMENT","MEMBERSHIP","BADGE"],"status":"SATURATED"}
AXS-002 | {"assessment":"VERIFIED","attempt_ids":["QRY-004","QRY-005","QRY-006","QRY-007","QRY-008"],"axis":"funding_and_resource_flow","links":["CLM-003","CTRL-003"],"question":"What public/private resources flow through the certification ecosystem and who allocates them?","result_ids":["FCT-008","FCT-009","FCT-010","FCT-011","FCT-013","FCT-014","FCT-017"],"sought_objects":["EU_GRANT","SUBGRANT","BUDGET","CONSORTIUM"],"status":"SATURATED"}
AXS-003 | {"assessment":"VERIFIED_BOUNDED","attempt_ids":["QRY-006","QRY-012","QRY-013"],"axis":"access_gatekeeping","links":["CLM-002","CTRL-002"],"question":"Which grants, repositories or platform programs explicitly condition access on certification?","result_ids":["FCT-012","FCT-015","FCT-025","FCT-026","FCT-027"],"sought_objects":["ELIGIBILITY","PLATFORM_PROGRAM","REPOSITORY","BACKOFFICE"],"status":"SATURATED"}
AXS-004 | {"assessment":"NOT_ESTABLISHED_FOR_COMMAND","attempt_ids":["QRY-001","QRY-010","QRY-011","QRY-015"],"axis":"independence_and_editorial_control","links":["CLM-003","CLM-006","CTRL-003","CTRL-006"],"question":"Do funders, public authorities or certifiers control editorial selections or conclusions?","result_ids":["FCT-005","FCT-019","FCT-023","FCT-024","FCT-028"],"sought_objects":["EDITORIAL_CONTROL","FUNDING_SEPARATION","PUBLIC_AUTHORITY_INDEPENDENCE"],"status":"SATURATED"}
AXS-005 | {"assessment":"VERIFIED_BOUNDED","attempt_ids":["QRY-001","QRY-003","QRY-013","QRY-014"],"axis":"complaints_and_recourse","links":["CLM-005","CTRL-005"],"question":"What review, complaint, renewal or sanction mechanisms constrain certification decisions?","result_ids":["FCT-003","FCT-004","FCT-022"],"sought_objects":["COMPLAINT","RENEWAL","SANCTION","EXTERNAL_ASSESSOR"],"status":"SATURATED"}
AXS-006 | {"assessment":"I0_I4_PARTIAL_I5_I7_OPEN","attempt_ids":["QRY-004","QRY-006","QRY-008","QRY-012","QRY-015"],"axis":"effect_and_causality","links":["CLM-002","CLM-003","CLM-006","CTRL-006"],"question":"What effects are established from certification to capacity, editorial output, exposure and political outcome?","result_ids":["FCT-008","FCT-010","FCT-013","FCT-015","FCT-017","FCT-025","FCT-028"],"sought_objects":["CAPACITY","REACH","EDITORIAL_OUTPUT","POLITICAL_EFFECT"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"CTRL-003;CTRL-004;CTRL-006","gap":"The chain is established through some access/capacity edges but not through editorial tasking, persuasion or political outcome.","gap_type":"CAUSALITY","limit":"Certification can alter access opportunities without demonstrating control over conclusions or electoral effects.","mechanism":"professional standards -> certification decision -> eligibility/recognition -> grant/platform/repository access -> organisational capacity/reach -> editorial selection/publication -> audience exposure -> possible political effect","status":"GAP","support":["FCT-001","FCT-012","FCT-013","FCT-015","FCT-025","FCT-026"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"EFCSN and IFCN define certification as compliance with professional standards, not as a public-law declaration that every publication is true.","status":"VERIFIED","support":["FCT-001","FCT-003","FCT-022","FCT-023"]}
CTRL-002 | {"control":"Certification creates real but bounded access gates: EFCSN certification is required for FACTEUR Database Grants; IFCN status is required for some platform programs but is explicitly not sufficient.","status":"VERIFIED","support":["FCT-012","FCT-013","FCT-014","FCT-015","FCT-025","FCT-026"]}
CTRL-003 | {"control":"EU funding and regranting capacity are material, while EFCSN/IFCN standards explicitly require funding transparency and editorial-independence safeguards; funding alone does not prove editorial tasking.","status":"VERIFIED","support":["FCT-005","FCT-008","FCT-009","FCT-010","FCT-011","FCT-024"]}
CTRL-004 | {"control":"Certification is not a universal EU fact-check funding gate in the examined corpus: Commission calls describe broader eligible stakeholders and EDMO hubs have separate consortium conditions and independence duties.","status":"VERIFIED","support":["FCT-016","FCT-017","FCT-019","FCT-020","FCT-021"]}
CTRL-005 | {"control":"EFCSN/IFCN include governance, external assessment, complaints or review mechanisms, so access decisions are not unbounded individual discretion.","status":"VERIFIED","support":["FCT-002","FCT-003","FCT-004","FCT-006","FCT-022"]}
CTRL-006 | {"control":"No examined source closes a causal chain from certification status or grant access to dictated individual conclusions, voter persuasion, or a counterfactual political result.","status":"VERIFIED_NEGATIVE","support":["FCT-028"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:17|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | MNEMO_UNAVAILABLE degraded; exact snapshot search unavailable in this environment | MnemoLite | NONE | MNEMO_Q
SYS-003 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | PASS | SRC-001 | https://efcsn.com/code-of-standards/ | FETCH exact source for INV-045: EFCSN — European Code of Standards
QRY-002 | FETCH | PASS | SRC-002 | https://efcsn.com/governance/ | FETCH exact source for INV-045: EFCSN — Governance
QRY-003 | FETCH | PASS | SRC-003 | https://efcsn.com/application/ | FETCH exact source for INV-045: EFCSN — Application process and fees
QRY-004 | FETCH | PASS | SRC-004 | https://digital-strategy.ec.europa.eu/en/news/commission-boosts-independent-fact-checking-eu5-million-grant-under-european-democracy-shield | FETCH exact source for INV-045: European Commission — €5m grant under European Democracy Shield
QRY-005 | FETCH | PASS | SRC-005 | https://efcsn.com/funding-opportunities/efcsn-eu-grant-facteur/ | FETCH exact source for INV-045: EFCSN — FACTEUR €5m grant
QRY-006 | FETCH | PASS | SRC-006 | https://efcsn.com/funding-opportunities/efcsn-database-grants/ | FETCH exact source for INV-045: EFCSN — Database Grants
QRY-007 | FETCH | PASS | SRC-007 | https://digital-strategy.ec.europa.eu/en/news/commission-launches-eu5-million-call-strengthen-european-fact-checking-network | FETCH exact source for INV-045: European Commission — €5m call European Network of Fact-Checkers
QRY-008 | FETCH | PASS | SRC-008 | https://digital-strategy.ec.europa.eu/en/funding/boosting-visibility-fact-checking-content-europe | FETCH exact source for INV-045: European Commission — €1.6m visibility call
QRY-009 | FETCH | PASS | SRC-009 | https://edmo.eu/areas-of-activities/fact-checking/ | FETCH exact source for INV-045: EDMO — Fact-checking activities
QRY-010 | FETCH | PASS | SRC-010 | https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/digital/wp-call/2026/call-fiche_digital-2026-bestuse-tech-edmo-09_en.pdf | FETCH exact source for INV-045: HaDEA — DIGITAL-2026 EDMO hubs call
QRY-011 | FETCH | PASS | SRC-011 | https://ifcncodeofprinciples.poynter.org/the-commitments | FETCH exact source for INV-045: IFCN — Code commitments
QRY-012 | FETCH | PASS | SRC-012 | https://www.ifcncodeofprinciples.poynter.org/signatory-benefits | FETCH exact source for INV-045: IFCN — Signatory benefits
QRY-013 | FETCH | PASS | SRC-013 | https://ifcncodeofprinciples.poynter.org/application-process | FETCH exact source for INV-045: IFCN — Application and complaints process
QRY-014 | FETCH | PASS | SRC-014 | https://ifcncodeofprinciples.poynter.org/assessors | FETCH exact source for INV-045: IFCN — External assessors
QRY-015 | FETCH | PASS | - | https://digital-strategy.ec.europa.eu/en/funding/boosting-visibility-fact-checking-content-europe | REFUTATION: evidence that certification or EU funding directly dictates individual fact-check selections, conclusions, or political outcomes
QRY-016 | FETCH | NONE | - | https://digital-strategy.ec.europa.eu/en/news/commission-boosts-independent-fact-checking-eu5-million-grant-under-european-democracy-shield | REFUTATION: seek primary evidence contradicting that FACTEUR is led by EFCSN with seven partners.
QRY-017 | FETCH | NONE | - | https://digital-strategy.ec.europa.eu/en/news/commission-boosts-independent-fact-checking-eu5-million-grant-under-european-democracy-shield | REFUTATION: seek primary evidence contradicting FACTEUR protection, crisis cooperation, repository/database and sustainability-fund functions.

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | EFCSN-CODE | EFCSN — European Code of Standards | 2026-09-07 | 2026-09-07T22:55:00+02:00 | membership/compliance/methodology/transparency/access/enforcement | https://efcsn.com/code-of-standards/
SRC-002 | ◈ | fam:A | EFCSN-GOV | EFCSN — Governance | 2026-09-07 | 2026-09-07T22:55:00+02:00 | member-driven assembly and governance body | https://efcsn.com/governance/
SRC-003 | ◈ | fam:A | EFCSN-APPLICATION | EFCSN — Application process and fees | 2026-09-07 | 2026-09-07T22:55:00+02:00 | assessment decisions, badge, fees | https://efcsn.com/application/
SRC-004 | ◈ | fam:B | EC-FACTCHECK-GRANT-2026 | European Commission — €5m grant under European Democracy Shield | 2026-03-31 | 2026-09-07T22:55:00+02:00 | grant agreement, coverage, protection, repository | https://digital-strategy.ec.europa.eu/en/news/commission-boosts-independent-fact-checking-eu5-million-grant-under-european-democracy-shield
SRC-005 | ◈ | fam:A | EFCSN-FACTEUR-2026 | EFCSN — FACTEUR €5m grant | 2026-03-31 | 2026-09-07T22:55:00+02:00 | consortium, actions, >60% redistribution | https://efcsn.com/funding-opportunities/efcsn-eu-grant-facteur/
SRC-006 | ◈ | fam:A | EFCSN-DATABASE-GRANTS-2026 | EFCSN — Database Grants | 2026-07-29 | 2026-09-07T22:55:00+02:00 | certification eligibility, €860k subgrants, selection, licensing/backoffice | https://efcsn.com/funding-opportunities/efcsn-database-grants/
SRC-007 | ◈ | fam:B | EC-FACTCHECK-CALL-2025 | European Commission — €5m call European Network of Fact-Checkers | 2025-04-01 | 2026-09-07T22:55:00+02:00 | scope, actions, open geography, relation to EDMO/EFCSN | https://digital-strategy.ec.europa.eu/en/news/commission-launches-eu5-million-call-strengthen-european-fact-checking-network
SRC-008 | ◈ | fam:B | EC-FACTCHECK-VISIBILITY-2025 | European Commission — €1.6m visibility call | 2025-04-30 | 2026-09-07T22:55:00+02:00 | independent fact-checkers, reach/impact collaborations | https://digital-strategy.ec.europa.eu/en/funding/boosting-visibility-fact-checking-content-europe
SRC-009 | ◈ | fam:C | EDMO-FACTCHECKING | EDMO — Fact-checking activities | 2026-09-07 | 2026-09-07T22:55:00+02:00 | network, briefs, investigations, map, repository, training | https://edmo.eu/areas-of-activities/fact-checking/
SRC-010 | ◈ | fam:D | HADEA-EDMO-2026-CALL | HaDEA — DIGITAL-2026 EDMO hubs call | 2025-10-09 | 2026-09-07T22:55:00+02:00 | hub independence, fact-checker participation, ENFC repository/interface | https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/digital/wp-call/2026/call-fiche_digital-2026-bestuse-tech-edmo-09_en.pdf
SRC-011 | ◈ | fam:E | IFCN-COMMITMENTS | IFCN — Code commitments | 2026-09-07 | 2026-09-07T22:55:00+02:00 | eligibility, 31 criteria, funding/editorial independence, methodology | https://ifcncodeofprinciples.poynter.org/the-commitments
SRC-012 | ◈ | fam:E | IFCN-BENEFITS | IFCN — Signatory benefits | 2026-09-07 | 2026-09-07T22:55:00+02:00 | platform-program conditions, tools, badge | https://www.ifcncodeofprinciples.poynter.org/signatory-benefits
SRC-013 | ◈ | fam:E | IFCN-APPLICATION | IFCN — Application and complaints process | 2026-09-07 | 2026-09-07T22:55:00+02:00 | external assessment, complaints, renewal/removal | https://ifcncodeofprinciples.poynter.org/application-process
SRC-014 | ◈ | fam:E | IFCN-ASSESSORS | IFCN — External assessors | 2026-09-07 | 2026-09-07T22:55:00+02:00 | independent assessor role and expertise | https://ifcncodeofprinciples.poynter.org/assessors

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://efcsn.com/code-of-standards/ | A | 2026-09-07 | EFCSN membership requires Code compliance | An operation becomes a verified EFCSN member only after assessment for compliance with the European Code of Standards. | -
FCT-002 | FACT | ✧ | https://efcsn.com/code-of-standards/ | A | 2026-09-07 | EFCSN governance body controls admission | The EFCSN Governance Body has the final word on membership applications and requires a two-thirds qualified majority with quorum for a valid decision. | -
FCT-003 | FACT | ✧ | https://efcsn.com/code-of-standards/ | A | 2026-09-07 | EFCSN external assessment and public outcome | EFCSN applications are assessed and can end in approval, pending decision or rejection, with the final outcome explained and publicly available. | -
FCT-004 | FACT | ✧ | https://efcsn.com/code-of-standards/ | A | 2026-09-07 | EFCSN complaints and compliance enforcement | After an unsatisfied complaint to a member, a complaint can be submitted to EFCSN; significant Code breaches can be reviewed with a right of reply and can lead to sanctions under the compliance procedure. | -
FCT-005 | FACT | ✧ | https://efcsn.com/code-of-standards/ | A | 2026-09-07 | EFCSN financial-transparency standard | EFCSN members must disclose major funding sources and explain mechanisms protecting editorial independence, including the nature of work funded by platforms or public sources. | -
FCT-006 | FACT | ✧ | https://efcsn.com/governance/ | A | 2026-09-07 | EFCSN is member-driven rather than a public authority | EFCSN describes itself as a member-driven association whose Assembly gives each member organisation one vote and elects the Governance Body. | -
FCT-007 | FACT | ✧ | https://efcsn.com/application/ | A | 2026-09-07 | EFCSN application and membership fees | EFCSN charges an application fee scaled by turnover and annual membership fees scaled by organisational turnover, with waivers or reductions possible by reasoned decision. | -
FCT-008 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/news/commission-boosts-independent-fact-checking-eu5-million-grant-under-european-democracy-shield | B | 2026-03-31 | European Commission signed €5m fact-checking grant | The European Commission signed a €5 million grant agreement to support independent fact-checkers across the EU and beyond under the European Democracy Shield agenda. | -
FCT-009 | FACT | ✦ | https://digital-strategy.ec.europa.eu/en/news/commission-boosts-independent-fact-checking-eu5-million-grant-under-european-democracy-shield | A,B | 2026-03-31 | FACTEUR is led by EFCSN with seven partners | The €5 million FACTEUR project is led by EFCSN with seven partner organisations and is planned for 30 months. | -
FCT-010 | FACT | ✧ | https://efcsn.com/funding-opportunities/efcsn-eu-grant-facteur/ | A | 2026-03-31 | FACTEUR redistributes most grant funding | EFCSN states that more than 60% of the FACTEUR grant will be distributed to fact-checking organisations across Europe. | -
FCT-011 | FACT | ✦ | https://digital-strategy.ec.europa.eu/en/news/commission-boosts-independent-fact-checking-eu5-million-grant-under-european-democracy-shield | A,B | 2026-03-31 | FACTEUR builds protection, crisis and repository capacity | FACTEUR includes a protection scheme, crisis cooperation, a repository/database and a dedicated sustainability fund for fact-checking organisations. | -
FCT-012 | FACT | ✧ | https://efcsn.com/funding-opportunities/efcsn-database-grants/ | A | 2026-07-29 | EFCSN certification is an explicit Database Grant eligibility gate | The FACTEUR Database Grants require applicants to be EFCSN-certified fact-checking organisations. | -
FCT-013 | FACT | ✧ | https://efcsn.com/funding-opportunities/efcsn-database-grants/ | A | 2026-07-29 | Database Grants allocate €860k through EFCSN-led process | The Database Grants have a total budget of €860,000, a maximum grant of €70,000 per project and anticipate 40–60 grants at a 50% funding rate. | -
FCT-014 | FACT | ✧ | https://efcsn.com/funding-opportunities/efcsn-database-grants/ | A | 2026-07-29 | Database Grant selection is multi-stage | The EFCSN team performs eligibility and review/ranking, while the FACTEUR consortium performs final evaluation of the ranking. | -
FCT-015 | FACT | ✧ | https://efcsn.com/funding-opportunities/efcsn-database-grants/ | A | 2026-07-29 | Database Grant access includes data-platform privileges and obligations | Successful Database Grant applicants sign grant and data-licensing agreements and gain backoffice access to the shared fact-check database. | -
FCT-016 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/news/commission-launches-eu5-million-call-strengthen-european-fact-checking-network | B | 2025-04-01 | Commission top-level €5m call did not make EFCSN membership the stated universal eligibility rule | The Commission call was open to stakeholders across eligible EU, candidate, accession and associated neighbouring countries and described EFCSN as an effort to build on and complement, not as the stated universal applicant-certification gate. | -
FCT-017 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/funding/boosting-visibility-fact-checking-content-europe | B | 2025-04-30 | Separate EU visibility funding targets independent fact-checkers and distribution partnerships | A separate approximately €1.6 million EU call funds projects to increase reach and impact of independent fact-checking content through collaborations with media, creators, influencers and podcasters. | -
FCT-018 | FACT | ✧ | https://edmo.eu/areas-of-activities/fact-checking/ | C | 2026-09-07 | EDMO maintains a fact-checking collaboration infrastructure | EDMO operates fact-checking briefs, cooperative investigations, a map of organisations, a searchable repository and training/events for fact-checkers. | -
FCT-019 | FACT | ✧ | https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/digital/wp-call/2026/call-fiche_digital-2026-bestuse-tech-edmo-09_en.pdf | D | 2025-10-09 | EDMO hubs are required to operate independently from public authorities | The 2026 EDMO hubs call states that hub activities are carried out in full independence from third-party entities including public authorities. | -
FCT-020 | FACT | ✧ | https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/digital/wp-call/2026/call-fiche_digital-2026-bestuse-tech-edmo-09_en.pdf | D | 2025-10-09 | EDMO hubs must include fact-checking organisations | The 2026 EDMO hubs call requires a hub to include one or more fact-checking organisations that together cover its geographical area. | -
FCT-021 | FACT | ✧ | https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/digital/wp-call/2026/call-fiche_digital-2026-bestuse-tech-edmo-09_en.pdf | D | 2025-10-09 | EDMO hubs interface with the European fact-check repository | The 2026 EDMO hubs call expects hubs to publish fact-checks into relevant repositories, including the repository established by the European Network of Fact-Checkers, and seek synergies with that network. | -
FCT-022 | FACT | ✧ | https://ifcncodeofprinciples.poynter.org/the-commitments | E | 2026-09-07 | IFCN verification uses public criteria and independent assessment | IFCN signatory applications are assessed against 31 criteria by independent assessors and reviewed by the IFCN advisory board. | -
FCT-023 | FACT | ✧ | https://ifcncodeofprinciples.poynter.org/the-commitments | E | 2026-09-07 | IFCN excludes state-controlled editorial output but permits some state funding with separation | IFCN does not grant signatory status to organisations whose editorial work is controlled by a state, party or politician, while state-funded public-service journalism can qualify if clear editorial separation is established. | -
FCT-024 | FACT | ✧ | https://ifcncodeofprinciples.poynter.org/the-commitments | E | 2026-09-07 | IFCN requires funding transparency and funder non-influence | IFCN standards require funding transparency and state that outside funders must not influence the conclusions fact-checkers reach. | -
FCT-025 | FACT | ✧ | https://www.ifcncodeofprinciples.poynter.org/signatory-benefits | E | 2026-09-07 | IFCN status is an access condition for some platform programs | IFCN states that Meta, Google and TikTok have made verified signatory status a condition for participation in some fact-checking programs and policies. | -
FCT-026 | FACT | ✧ | https://www.ifcncodeofprinciples.poynter.org/signatory-benefits | E | 2026-09-07 | IFCN certification is necessary but not sufficient for those platform programs | IFCN states that signatory status is typically necessary but not sufficient for access to such platform programs and that IFCN does not negotiate those relationships. | -
FCT-027 | FACT | ✧ | https://www.ifcncodeofprinciples.poynter.org/signatory-benefits | E | 2026-09-07 | IFCN signatory status provides additional non-editorial privileges | Verified IFCN signatories receive a badge and access to tool discounts, illustrating that certification can confer practical benefits without determining editorial conclusions. | -
FCT-028 | FACT | ✦ | https://efcsn.com/code-of-standards/ | A,E | 2026-09-07 | Certification has bounded access effects but editorial and political causality remain unproven | The corpus establishes that certification can gate some grants, repositories and platform programs, but it does not establish that EFCSN, IFCN or EU funders dictate individual fact-check selections or conclusions, nor a causal political/electoral effect from certification. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001,SRC-002
FCT-003 | SRC-001,SRC-003
FCT-004 | SRC-001
FCT-005 | SRC-001
FCT-006 | SRC-002
FCT-007 | SRC-003
FCT-008 | SRC-004
FCT-009 | SRC-004,SRC-005
FCT-010 | SRC-005
FCT-011 | SRC-004,SRC-005
FCT-012 | SRC-006
FCT-013 | SRC-006
FCT-014 | SRC-006
FCT-015 | SRC-006
FCT-016 | SRC-007
FCT-017 | SRC-008
FCT-018 | SRC-009
FCT-019 | SRC-010
FCT-020 | SRC-010
FCT-021 | SRC-010
FCT-022 | SRC-011,SRC-014
FCT-023 | SRC-011
FCT-024 | SRC-011
FCT-025 | SRC-012
FCT-026 | SRC-012
FCT-027 | SRC-012
FCT-028 | SRC-001,SRC-006,SRC-011,SRC-012

## REFUTATION_REGISTRY_V1
FCT-009 | QRY-016 | NONE
FCT-011 | QRY-017 | NONE
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
FCT-009 | ELIGIBLE:CONFIRME
FCT-010 | ELIGIBLE:VERIFIE
FCT-011 | ELIGIBLE:CONFIRME
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
ATTEMPT-001 | {"created_at":"2026-09-07T21:26:47.522612+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:CONFIRME","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:CONFIRME","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:CONFIRME","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":28,"eligible":28,"failure":0,"success":0}}

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
FCT-009 | ELIGIBLE:CONFIRME | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-010 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-011 | ELIGIBLE:CONFIRME | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
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
