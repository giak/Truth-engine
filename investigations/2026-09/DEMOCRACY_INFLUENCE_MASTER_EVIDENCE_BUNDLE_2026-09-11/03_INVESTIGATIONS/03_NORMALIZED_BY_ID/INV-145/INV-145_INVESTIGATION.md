ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260907-0538-inv145-recovery | PARENT_RUN_ID:NONE | AS_OF:2026-09-07
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/truth-engine/investigations/2026-09/2026-09-07_fara-france-ue-agent-etranger/2026-09-07_05-38_fara-france-ue-agent-etranger_INPUT.md | SUBJECT_SLUG:fara-france-ue-agent-etranger | SUBJECT_FP:sha256:3d098dd6a09c9a669b49c6d23f97075dae4d59529f58928976ac55369462ce88 | INPUT_SHA256:sha256:71922fc117f2e36bfe0ae71bc90f74050b5d1c011abef1eca1def5dae945f591
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:2018–2026; compare FARA (US), French HATVP foreign-influence register, and EU third-country interest-representation proposal on isomorphic behavior, definitions, exemptions, disclosure duties, sanctions and enforcement; distinguish textual scope from implementation.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/NETWORK.md,clusters/FRAMING.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-145 — Comparaison FARA / France / Union européenne

## Objet

Comparer, à comportement matériel aussi proche que possible, les régimes de transparence de l'influence étrangère aux États-Unis, en France et dans le projet européen, sans confondre différence de droit, différence d'enforcement et « double standard » normatif.

## Résultat central

**FACT.** Les trois cadres ne définissent pas le même objet juridique. Sous FARA, la catégorie de *foreign principal* inclut notamment des personnes et entités étrangères privées sans exigence générale de contrôle étatique (FCT-001, FCT-002). Le dispositif français vise un *mandant étranger* défini autour des puissances étrangères hors Union européenne, des partis hors UE et d'entités sous contrôle/direction ou financement majoritaire d'une puissance étrangère ; la simple propriété par une société étrangère ne suffit pas à elle seule (FCT-008, FCT-009, FCT-012). Le projet européen vise des activités de représentation d'intérêts menées pour un sponsor de pays tiers et la position du Parlement exclut explicitement le financement étranger sans lien avec cette activité (FCT-016, FCT-017, FCT-019).

**INFERENCE.** À conduite matérielle identique, l'obligation de transparence peut donc diverger selon la nature du principal, son lien avec une puissance publique, sa localisation UE/non-UE et le type exact de relation avec l'intermédiaire. Cette asymétrie de conception est documentée ; elle ne prouve pas par elle-même une application politiquement sélective (CLM-001, CLM-002, CLM-003, CLM-006).

## États-Unis — FARA

FARA fonctionne comme un régime de divulgation et non comme une interdiction générale de plaidoyer : le DOJ précise que le contenu de l'advocacy n'est pas interdit par l'enregistrement (FCT-020). Le déclencheur combine une relation avec un principal étranger et certaines activités politiques, de relations publiques, de conseil politique, de collecte ou de représentation (FCT-001). La notion de principal étranger est large et peut couvrir une entité privée organisée à l'étranger (FCT-002). Des exemptions commerciales, académiques, juridiques ou liées au Lobbying Disclosure Act existent sous conditions (FCT-003).

Les sanctions nominales peuvent être pénales et civiles (FCT-004). L'enforcement est observable sur une base mature : pour juillet-décembre 2024, le DOJ recensait 527 registrants actifs, 788 principals, 2 461 short-form registrations, six inspections, aucune action civile déposée et des poursuites FARA contre cinq personnes (FCT-005, FCT-006). En mai 2026, deux personnes ont été condamnées par jury pour des infractions FARA liées à un lobbying secret pour le gouvernement vénézuélien (FCT-007).

## France — registre de l'influence étrangère

Le périmètre français comporte une distinction géographique explicite : les puissances étrangères et partis politiques visés sont hors Union européenne ; certaines personnes morales ne deviennent pertinentes qu'en raison d'un contrôle, d'une direction ou d'un financement majoritaire par une puissance étrangère (FCT-008). L'acteur doit agir sur ordre, requête, direction ou contrôle du mandant, et les activités couvertes comprennent notamment certaines communications vers des responsables publics, communications au public et certains flux de fonds visant à influencer une décision ou politique publique (FCT-009, FCT-010).

Le régime prévoit des mécanismes de mise en conformité et des sanctions pénales pour les personnes physiques ainsi que des sanctions applicables aux personnes morales (FCT-011). Mais il est récent : le registre est entré en vigueur le 1er octobre 2025 et les premières déclarations d'activité datent de janvier 2026 (FCT-013). Le 7 septembre 2026, la liste publique observée comportait douze entités (FCT-014). Ce nombre est une observation de registre, pas un dénominateur d'enforcement.

La HATVP elle-même distingue influence étrangère légitime et ingérence ; le cadre de transparence ne permet donc pas de qualifier automatiquement toute activité enregistrable d'hostile ou d'illégale (FCT-021).

## Union européenne — cadre encore non final

Au 7 septembre 2026, la procédure législative 2023/0463/COD est toujours en cours après les amendements du Parlement du 27 novembre 2025 et le renvoi aux négociations interinstitutionnelles (FCT-015). Il n'existe donc pas encore de régime européen final, transposé et doté d'un historique d'enforcement comparable.

La proposition de la Commission porte sur la représentation d'intérêts menée pour le compte de pays tiers afin d'influencer l'élaboration ou la mise en œuvre de politiques, de législation ou de décisions publiques (FCT-016). La position du Parlement exclut le financement étranger qui n'est pas lié à une prestation de représentation d'intérêts et ajoute des garanties explicites contre la stigmatisation de type « foreign agent law » (FCT-017, FCT-018). Le sponsor de pays tiers et l'attribution de l'activité sont ainsi au centre du modèle, plutôt que l'origine étrangère du financement prise isolément (FCT-019).

## Contrôles de symétrie

**Contrôle 1 — entreprise privée étrangère.** Une société étrangère privée peut être un *foreign principal* sous FARA sans contrôle étatique, alors que le régime français exige, pour la catégorie pertinente examinée ici, le lien étatique/partisan prévu par le texte. C'est une différence de périmètre réelle (CTRL-001).

**Contrôle 2 — UE / hors UE.** La France exclut explicitement les États membres et partis de l'UE du *mandant étranger*. C'est une asymétrie géographique légale démontrée. Ce constat ne suffit pas à établir que des conduites isomorphes sont investiguées ou sanctionnées différemment selon qu'elles viennent d'un allié ou d'un adversaire (CTRL-002, CLM-003).

**Contrôle 3 — financement seul.** La position du Parlement européen indique que le financement étranger sans rapport avec la prestation de représentation ne doit pas déclencher le dispositif. Le financement reste donc distinct du commandement, de l'agence et du tasking (CTRL-003).

**Contrôle 4 — maturité.** Comparer les centaines d'inscriptions FARA et ses poursuites à un registre français ouvert depuis moins d'un an produirait une fausse mesure. Les fenêtres, univers exposés et dénominateurs ne sont pas comparables (CTRL-004, CLM-005).

## Enforcement et limite causale

La comparaison établit des outils de contrôle et des actions d'enforcement américaines, ainsi que l'existence opérationnelle du registre français. Elle ne fournit pas de taux comparables d'infraction, de détection, de poursuite ou de sanction. Le cadre européen n'est pas encore final. Par conséquent, l'hypothèse d'un enforcement plus tolérant envers les alliés ou plus sévère envers les adversaires reste non établie dans cette investigation.

Le mécanisme causal minimal est : relation principal/sponsor + activité couverte → obligation de déclaration/transparence → pression de conformité et possibilité de sanction. Son effet dissuasif ou son impact sur les politiques publiques ne sont pas identifiés par un design causal comparable (CAU-001).

## Conclusion technique

Le résultat robuste n'est pas « les mêmes actes sont punis différemment » mais : **les systèmes ne construisent pas juridiquement le même objet de transparence étrangère**. FARA a un principal étranger plus large ; la France opère un filtrage explicite hors UE et lié à la puissance étrangère ; le projet européen vise une prestation attribuable à un sponsor de pays tiers et cherche explicitement à éviter qu'un financement étranger isolé ou l'enregistrement lui-même ne stigmatise l'acteur.

La différence de conception peut alimenter `INV-146` comme contrôle de symétrie. En revanche, une conclusion d'asymétrie d'enforcement exige des données françaises pluriannuelles, le texte européen final et des cas réellement isomorphes avec dénominateurs communs. Ces données n'existent pas encore dans une forme permettant ce test.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:6|SRC_COMPLETE:9/9

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **anchor_events:**
  - FARA enforcement snapshot Jul-Dec 2024
  - French foreign-influence register effective 1 Oct 2025
  - EU Parliament amendments 27 Nov 2025
  - French first activity declarations Jan 2026
  - DOJ Rivera/Nuhfer convictions 1 May 2026
  - EU procedure still ongoing 7 Sep 2026
- **as_of:** 2026-09-07
- **rules:**
  - legal text date != enforcement date != investigation date
  - mature-regime counts are not directly comparable to a sub-one-year regime
  - pending EU proposal is not treated as an operational enforcement regime
- **window:** 2018–2026

### MANIPULATION_REPORT
- **assumptions:**
  - public registers under-observe noncompliance
  - newer regimes have shorter enforcement histories
  - different constitutional/legal objectives may justify non-isomorphic design
- **clusters:**
  - **loaded:**
    - clusters/POWER.md
    - clusters/NETWORK.md
    - clusters/FRAMING.md
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - comparison must use isomorphic behavior
  - ally/adversary language must be separated from statutory scope
  - EU proposal status is time-sensitive
- **input_kind:** TOPIC
- **mission_mode:** INVESTIGATION
- **patterns:**
  - legal-design asymmetry
  - foreign-principal scope compression
  - funding-to-agency jump
  - sanction-to-enforcement jump
  - raw-count denominator error
- **priorities:**
  - authoritative statutory/regulatory text
  - current registry/enforcement data
  - same-behavior controls
  - explicit denominators and maturity limits
- **query_guidance:** compare principal/sponsor -> relation trigger -> covered activity -> exemption -> disclosure duty -> sanction -> observable enforcement; never infer selective enforcement from unmatched raw counts
- **rhetorical:**
  - **AUTH:** N/A
  - **BF:** N/A
  - **DEM:** N/A
  - **FAC:** N/A
  - **NUM:** N/A
- **speaker:**
  - **goal:** symmetrical legal comparison
  - **target:** classification and enforcement mechanics
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **Κ:** 3
  - **Λ:** 4
  - **Ξ:** 3
  - **Σ:** 3
  - **Φ:** 2
  - **Ψ:** 2
  - **Ω:** 3
  - **κ:** 2
  - **ρ:** 4
  - **€:** 3
  - **↕:** 6
  - **⏰:** 6
  - **⚔:** 2
  - **⫸:** 4
  - **🌐:** 5
- **threats:**
  - foreign=hostile agent
  - foreign funding=command
  - different law=illegitimate double standard
  - nominal sanction=actual enforcement
  - registry size=enforcement intensity

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - comparative policy justification deferred to synthesis
  - **input_ids:**
    - CLM-001
    - CLM-002
    - CLM-003
    - CLM-006
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no evidence that geographic statutory asymmetry equals selective enforcement by ally/adversary status
  - **not_computable:**
    - normative legitimacy of each jurisdictional choice
  - **operations_applied:**
    - separated statutory scope from enforcement
    - tested EU/non-EU and private/state-linked principal controls
  - **reason:** compare who is legally empowered to classify foreign influence and which foreign principals are in scope
  - **result_ids:**
    - CLM-002
    - CLM-003
    - CLM-006
    - CTRL-001
    - CTRL-002
  - **status:** DONE
  - **trigger:** ↕=6
- **item 2:**
  - **gaps:**
    - noncompliant actor denominator unavailable
  - **input_ids:**
    - FCT-001
    - FCT-002
    - FCT-008
    - FCT-009
    - FCT-012
    - FCT-019
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no basis to equate foreign funding alone with agency under the compared regimes
  - **not_computable:**
    - hidden non-registration universe
  - **operations_applied:**
    - typed principal-agent relation
    - separated mere foreign ownership/funding from order-request-direction-control
  - **reason:** map principal/agent/sponsor relations without collapsing ownership, funding and tasking
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CTRL-001
    - CTRL-003
  - **status:** DONE
  - **trigger:** 🌐=5
- **item 3:**
  - **gaps:**
    - normative/stigma effects not causally measured
  - **input_ids:**
    - FCT-018
    - FCT-020
    - FCT-021
    - CLM-006
  - **module:** clusters/FRAMING.md
  - **negative_results:**
    - registration itself does not prove hostile interference
  - **not_computable:**
    - cross-jurisdiction stigma effect
  - **operations_applied:**
    - separated disclosure label from illegality/hostility
    - retained anti-stigma safeguards
  - **reason:** foreign-agent terminology can imply hostility beyond the legal disclosure mechanics
  - **result_ids:**
    - CTRL-005
    - CLM-006
  - **status:** DONE
  - **trigger:** Λ=4

### SCOPING_REPORT
- **classification_dimensions:**
  - principal/sponsor definition
  - relation trigger
  - covered activity
  - exemptions
  - disclosure obligation
  - sanctions
  - enforcement maturity
  - geographic exclusions
- **exclusions:**
  - different statute=double standard by definition
  - foreign funding=agency
  - registration=hostility
  - raw prosecution count=comparable enforcement rate
- **scope:** 2018–2026; FARA, French HATVP foreign-influence regime, and pending EU third-country interest-representation framework
- **status:** ACTIVE

### CREDO
- foreign != hostile
- funding != command
- ownership != tasking
- registration != illegality
- nominal sanction != enforcement intensity
- legal-design asymmetry != selective enforcement
- raw counts require denominators
- pending proposal != operational regime
- transparency != prohibition
- different objective may justify different scope

### COGNITIVE_MAP
- **causal_boundary:** Legal triggers and observed enforcement acts are documented; deterrence, behavior change and comparative policy effects are not causally identified.
- **comparison_chain:**
  - principal/sponsor
  - agency/attribution relation
  - covered activity
  - exemption/safeguard
  - disclosure
  - sanction
  - observed enforcement
- **core_model:** The three regimes regulate different foreign-influence objects. FARA has the broadest foreign-principal concept; France narrows mandants to non-EU foreign powers/parties and specified state-linked entities; the pending EU framework targets attributable third-country interest-representation services and rejects funding-only triggers.
- **rival_models:**
  - neutral transparency regulation
  - national-security foreign-influence control
  - anti-stigma interest-representation transparency
  - selective ally/adversary enforcement
  - maturity-driven apparent enforcement differences

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** The statutes define principal, relation and activity differently.
  - **resolution:** Compare isomorphic behavior element by element before labeling asymmetry.
  - **thesis:** All foreign-connected political activity is equivalent across regimes.
- **item 2:**
  - **antithesis:** The French regime began in October 2025 while FARA has a mature multi-decade enforcement history.
  - **resolution:** No enforcement-rate conclusion without matched windows and denominators.
  - **thesis:** France enforces less because its public register is much smaller than FARA.
- **item 3:**
  - **antithesis:** The EU Parliament position explicitly rejects unrelated funding as a trigger and French law requires specified mandant/actor relations.
  - **resolution:** Funding is a resource fact, not agency/tasking by itself.
  - **thesis:** Foreign funding alone should trigger foreign-agent registration.
- **item 4:**
  - **antithesis:** It proves a textual geographic distinction, not selective investigation/sanction of isomorphic conduct.
  - **resolution:** Route legal-design asymmetry to INV-146; retain enforcement claim as unproven.
  - **thesis:** The French EU exclusion proves an ally double standard in practice.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **from:** foreign principal
  - **limits:**
    - FARA exemptions may apply
    - foreign principal status alone does not prove unlawful non-registration
  - **resource:** money, direction, political/PR activity
  - **support:**
    - FCT-001
    - FCT-002
  - **to:** US political/public sphere
  - **via:** agent/registrant
- **item 2:**
  - **from:** non-EU foreign power/party or qualifying state-linked entity
  - **limits:**
    - mere foreign-company ownership insufficient
  - **resource:** instructions, communications, certain fund flows
  - **support:**
    - FCT-008
    - FCT-009
    - FCT-010
  - **to:** French public decision/public communication sphere
  - **via:** actor under order/request/direction/control
- **item 3:**
  - **from:** third-country sponsor
  - **limits:**
    - proposal not final
    - unrelated foreign funding outside trigger per Parliament position
  - **resource:** remunerated/attributable representation activity
  - **support:**
    - FCT-016
    - FCT-017
    - FCT-019
  - **to:** EU policy/law/public decision sphere
  - **via:** interest-representation service provider

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** foreign principal
  - **limits:**
    - exemptions and fact-specific agency tests apply
  - **relation:** order/request/direction/control or covered agency relationship
  - **support:**
    - FCT-001
    - FCT-002
  - **to:** FARA agent
- **item 2:**
  - **from:** mandant étranger
  - **limits:**
    - EU states/parties excluded; corporate state-link tests apply
  - **relation:** order/request/direction/control
  - **support:**
    - FCT-008
    - FCT-009
  - **to:** French influence actor
- **item 3:**
  - **from:** third-country sponsor
  - **limits:**
    - legislative text still pending
  - **relation:** attributable interest-representation service
  - **support:**
    - FCT-016
    - FCT-019
  - **to:** EU interest representative
- **item 4:**
  - **from:** regulators/justice
  - **limits:**
    - maturity and denominator differ
  - **relation:** disclosure control and sanctions
  - **support:**
    - FCT-004
    - FCT-006
    - FCT-007
    - FCT-011
    - FCT-013
  - **to:** registrants/noncompliant actors

### IMPACT_MAP
- **I0_identity_relation:** HIGH for statutory principal/mandant/sponsor definitions and agency triggers
- **I1_resources_capability:** HIGH for legal disclosure/control powers and nominal sanctions
- **I2_documented_action:** HIGH for FARA inspections/charges/convictions and French live registration activity
- **I3_coordination_tasking:** DEFINED LEGALLY, case-specific factual proof remains necessary
- **I4_I6_effect:** NOT COMPARABLE across regimes from current public data
- **I7_counterfactual:** NOT ESTABLISHED
- **downstream:** Legal-design symmetry controls feed INV-146; enforcement asymmetry remains a future-data question.

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** foreign-agent terminology can imply hostility
  - **issue:** broad foreign-principal label vs hostile-agent connotation
  - **pro:** FARA covers foreign private persons/entities and is a disclosure statute
  - **resolution:** LEGAL_REGISTRATION_NOT_HOSTILITY
- **item 2:**
  - **contra:** no comparable enforcement sample proves ally/adversary selective application
  - **issue:** French EU/non-EU asymmetry
  - **pro:** mandant étranger definition expressly excludes EU Member States/parties
  - **resolution:** TEXTUAL_ASYMMETRY_VERIFIED_ENFORCEMENT_ASYMMETRY_OPEN
- **item 3:**
  - **contra:** regimes differ in scope and maturity; French regime began Oct 2025
  - **issue:** small French registry vs FARA scale
  - **pro:** 12 entities observed in HATVP live list versus hundreds of active FARA registrants in 2024
  - **resolution:** RAW_COUNTS_NOT_COMPARABLE_RATE
- **item 4:**
  - **contra:** EU Parliament expressly excludes unrelated funding; French/FARA require covered relations/activities
  - **issue:** foreign funding as trigger
  - **pro:** foreign funding can be relevant evidence/resource
  - **resolution:** FUNDING_ALONE_INSUFFICIENT

### VERIFICATION_REPORT
- **analytical_secondary_role:** 0
- **direct_primary_role:** 9
- **independence_limits:**
  - most legal-scope facts are necessarily regulator/statute self-description
  - French enforcement window is less than one year
  - EU proposal has no final enforcement data
- **negative_checks:**
  - no matched France-US enforcement denominator
  - no EU final directive/transposition/enforcement
  - no causal deterrence design
  - no proof of ally/adversary selective enforcement from statutory scope alone
- **source_families:** 5
- **source_records_complete:** 9/9
- **status:** PASS_WITH_EXPLICIT_GAPS
- **web_fact_trace:** 21/21 facts mapped to accepted FETCH-backed sources

### EDI_REPORT
- **corpus:**
  - **circularity:** LOW_ACROSS_JURISDICTIONS
  - **coverage:** CENTRAL_LEGAL_MECHANISMS_COVERED
  - **independence:** INSTITUTIONALLY_DIVERSE
  - **limits:**
    - short French enforcement history
    - EU proposal pending
    - noncompliance denominator unknown
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
    - **independent_families:** 2
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** YES_TEXT_PARTIAL_ENFORCEMENT
    - **gap_type:** BASELINE
    - **independent_families:** 1
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** YES
    - **gap_type:** TEMPORAL
    - **independent_families:** 1
  - **item 5:**
    - **claim_id:** CLM-005
    - **direct_object:** PARTIAL
    - **gap_type:** BASELINE
    - **independent_families:** 2
  - **item 6:**
    - **claim_id:** CLM-006
    - **direct_object:** YES_MECHANICS
    - **gap_type:** NORMATIVE
    - **independent_families:** 3
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** 5_PROVENANCE_FAMILIES
  - **perspective:** US_DOJ+FR_HATVP+EU_LEGISLATIVE_SOURCES
  - **stratification:** LEGAL_TEXT+LIVE_REGISTRY+ENFORCEMENT_REPORT
  - **temporal:** 2018-2026
- **edi:**
  - **assessment:** HIGH_AUTHORITY_LOW_ENFORCEMENT_COMPARABILITY
  - **flags:**
    - REGULATOR_SELF_DESCRIPTION
    - MATURITY_MISMATCH
    - PENDING_EU_LEGISLATION
    - NO_CAUSAL_ENFORCEMENT_DESIGN
- **source_counts:**
  - **primary:** 9
  - **provenance_families:** 5
  - **secondary:** 0
  - **total:** 9

### RESPONSIBILITY_MAP
- **item 1:**
  - **highest_supported:** DOJ statutory/administrative definition and documented enforcement actions
  - **not_supported:** that every foreign principal engages in hostile or unlawful influence
  - **object:** FARA classification
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-004
    - FCT-006
    - FCT-007
- **item 2:**
  - **highest_supported:** HATVP statutory scope including non-EU/state-link tests and live register
  - **not_supported:** selective enforcement against adversaries rather than allies
  - **object:** French foreign-influence classification
  - **support:**
    - FCT-008
    - FCT-009
    - FCT-013
    - FCT-014
- **item 3:**
  - **highest_supported:** Commission proposal and Parliament position define intended third-country interest-representation transparency model
  - **not_supported:** final EU law, transposition or enforcement
  - **object:** EU framework
  - **support:**
    - FCT-015
    - FCT-016
    - FCT-017
    - FCT-018
    - FCT-019

### NEXT_QUERIES
- **item 1:**
  - **query:** multi-year HATVP enforcement totals and case-level sanctions after sufficient operational history
  - **route:** RECHECK
  - **trigger:** future annual reports / sanctions
- **item 2:**
  - **query:** final EU directive text, adoption, transposition and first enforcement data
  - **route:** RECHECK
  - **trigger:** procedure 2023/0463/COD final adoption
- **item 3:**
  - **query:** matched US-France isomorphic case sample with common denominator
  - **route:** DEFER
  - **trigger:** sufficient French case history
- **item 4:**
  - **query:** ally/adversary legal-design and vocabulary synthesis
  - **route:** MERGE
  - **trigger:** INV-146 after dependencies close

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-004,QRY-007,QRY-008,QRY-009 | support:- | counter:- | results:FCT-001,FCT-002,FCT-008,FCT-015,FCT-016,FCT-017,FCT-019 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-002,QRY-003,QRY-005,QRY-006,QRY-007 | support:- | counter:- | results:FCT-005,FCT-006,FCT-007,FCT-011,FCT-013,FCT-014,FCT-015 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-001,QRY-004,QRY-008,QRY-009 | support:- | counter:- | results:FCT-002,FCT-008,FCT-012,FCT-019 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-004,QRY-008 | support:- | counter:- | results:FCT-001,FCT-009,FCT-019 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-001,QRY-004,QRY-006,QRY-009 | support:- | counter:- | results:FCT-001,FCT-010,FCT-016,FCT-020 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-001,QRY-008 | support:- | counter:- | results:FCT-003,FCT-017,FCT-018,FCT-021 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-001,QRY-006 | support:- | counter:- | results:FCT-004,FCT-011 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-002,QRY-003,QRY-005 | support:- | counter:- | results:FCT-005,FCT-006,FCT-007,FCT-014 | final:GAP | gap:BASELINE
AXS-007 | attempts:QRY-007,QRY-008,QRY-009 | support:- | counter:- | results:FCT-015,FCT-016,FCT-017,FCT-018,FCT-019 | final:SATURATED | gap:NONE
AXS-008 | attempts:QRY-001,QRY-004,QRY-008,QRY-009 | support:- | counter:- | results:FCT-002,FCT-008,FCT-012,FCT-017,FCT-019 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,QRY-004,QRY-008,QRY-009,SRC-001,SRC-004,SRC-008,SRC-009 | support:FCT-002,FCT-008,FCT-012,FCT-016,FCT-017,FCT-019 | counter:CTRL-001;CTRL-003 | results:FCT-002,FCT-008,FCT-012,FCT-016,FCT-017,FCT-019,CTRL-001;CTRL-003 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-001,QRY-004,SRC-001,SRC-004 | support:FCT-002,FCT-003,FCT-008,FCT-009,FCT-012 | counter:FARA exemptions and French activity/agency triggers still apply before registration duties arise. | results:FCT-002,FCT-003,FCT-008,FCT-009,FCT-012,FARA exemptions and French activity/agency triggers still apply before registration duties arise. | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-004,QRY-005,QRY-006,SRC-004,SRC-005,SRC-006 | support:FCT-008,FCT-013,FCT-014 | counter:CTRL-004 | results:FCT-008,FCT-013,FCT-014,CTRL-004 | final:PARTIAL | gap:BASELINE
CLM-004 | attempts:QRY-007,SRC-007 | support:FCT-015 | counter:- | results:FCT-015 | final:SUPPORTED | gap:TEMPORAL
CLM-005 | attempts:QRY-001,QRY-002,QRY-003,QRY-005,QRY-006,SRC-001,SRC-002,SRC-003,SRC-005,SRC-006 | support:FCT-004,FCT-005,FCT-006,FCT-007,FCT-011,FCT-013,FCT-014 | counter:FARA has observable inspections,charges and a 2026 conviction; France has a live register and formal control powers. | results:FCT-004,FCT-005,FCT-006,FCT-007,FCT-011,FCT-013,FCT-014,FARA has observable inspections,charges and a 2026 conviction; France has a live register and formal control powers. | final:PARTIAL | gap:BASELINE
CLM-006 | attempts:QRY-001,QRY-004,QRY-008,QRY-009,SRC-001,SRC-004,SRC-008,SRC-009 | support:FCT-002,FCT-008,FCT-012,FCT-016,FCT-017,FCT-019 | counter:Different legal objectives and constitutional contexts may justify some non-isomorphic design choices. | results:FCT-002,FCT-008,FCT-012,FCT-016,FCT-017,FCT-019,Different legal objectives and constitutional contexts may justify some non-isomorphic design choices. | final:SUPPORTED | gap:NORMATIVE

## STATUS_DELTA_V1
DELTA-001 | AXS-006 | PARTIAL | GAP | Terminalize inaccessible same-window enforcement baseline as typed gap

## OPEN_GAPS_V1
AXS-006 | AXS | GAP | BASELINE | No comparable multi-year French enforcement denominator exists yet; the EU framework is not final.
CLM-003 | CLM | PARTIAL | BASELINE | No comparable case-level enforcement sample across EU and non-EU principals is yet available.
CLM-004 | CLM | SUPPORTED | TEMPORAL | Final text, transposition and enforcement do not yet exist.
CLM-005 | CLM | PARTIAL | BASELINE | Comparable multi-year French enforcement data are not yet available.
CLM-006 | CLM | SUPPORTED | NORMATIVE | Normative legitimacy requires a separate legal/policy judgment; this run establishes comparative mechanics.
CAU-001 | CAU | UNRESOLVED | CAUSALITY | No cross-regime causal design measures transparency or deterrence effects.

SEMANTIC_COUNTS_V1:LED:2|CLM:6|AXS:8|CAU:1|CTRL:5|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-004","QRY-007","QRY-008","QRY-009"],"evidence_excerpt":"Authoritative US, French and EU texts establish different principal/sponsor definitions and coverage triggers.","kind":"HYPOTHESIS","lead":"FARA, the French HATVP regime and the pending EU framework may classify materially similar foreign-influence activity differently because they use different principal/sponsor definitions and scope triggers.","linked_ids":["CLM-001","CLM-002","CLM-003","CLM-006"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-008","FCT-015","FCT-016","FCT-017","FCT-019"],"routes":["LEGAL_SCOPE","SYMMETRY_CONTROL"],"source_id":"INV-145_RUN_CARD","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-002","QRY-003","QRY-005","QRY-006","QRY-007"],"evidence_excerpt":"FARA has mature registry/enforcement observations while the French register began in October 2025 and the EU framework remains pending.","kind":"METHOD_CONSTRAINT","lead":"Textual scope, nominal sanctions and observed enforcement must be compared separately; a newer regime with a small observable registry cannot be treated as under-enforced merely because it lacks a mature prosecution history.","linked_ids":["CLM-003","CLM-005","CTRL-004"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-005","FCT-006","FCT-007","FCT-011","FCT-013","FCT-014","FCT-015"],"routes":["ENFORCEMENT","COUNTER_HYPOTHESES"],"source_id":"INV-145_RUN_CARD","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"The three frameworks are not legally isomorphic: FARA uses a broader foreign-principal concept, the French regime centers non-EU foreign powers and state-linked entities, and the pending EU text targets attributable third-country interest representation rather than foreign funding as such.","claimant":"INV-145 synthesis","counter":"CTRL-001;CTRL-003","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-002","FCT-008","FCT-012","FCT-016","FCT-017","FCT-019"]}
CLM-002 | {"claim":"A private foreign company can qualify as a foreign principal under FARA without state control, whereas comparable status under the French foreign-influence register generally requires the foreign-power/party linkage specified by the French statute; this is a material scope difference.","claimant":"INV-145 synthesis","counter":"FARA exemptions and French activity/agency triggers still apply before registration duties arise.","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-002","FCT-003","FCT-008","FCT-009","FCT-012"]}
CLM-003 | {"claim":"France contains an explicit EU/non-EU asymmetry in the statutory definition of mandant étranger; the evidence establishes the textual distinction but does not establish that comparable conduct is selectively investigated or sanctioned according to ally/adversary status.","claimant":"INV-145 synthesis","counter":"CTRL-004","gap":"No comparable case-level enforcement sample across EU and non-EU principals is yet available.","gap_type":"BASELINE","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-008","FCT-013","FCT-014"]}
CLM-004 | {"claim":"The EU framework cannot yet be treated as an operational enforcement regime as of 7 September 2026 because procedure 2023/0463/COD remains ongoing after Parliament amendments and referral to interinstitutional negotiations.","claimant":"INV-145 synthesis","counter":"NONE_FOUND","gap":"Final text, transposition and enforcement do not yet exist.","gap_type":"TEMPORAL","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-015"]}
CLM-005 | {"claim":"Nominal sanctions under FARA and the French regime are both substantial, but enforcement intensity cannot be compared from raw prosecution counts because FARA is mature while the French regime is less than one year old and lacks an equivalent denominator/history.","claimant":"INV-145 synthesis","counter":"FARA has observable inspections, charges and a 2026 conviction; France has a live register and formal control powers.","gap":"Comparable multi-year French enforcement data are not yet available.","gap_type":"BASELINE","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-004","FCT-005","FCT-006","FCT-007","FCT-011","FCT-013","FCT-014"]}
CLM-006 | {"claim":"The strongest supported double-standard finding is therefore legal-design asymmetry, not demonstrated enforcement asymmetry: identical foreign provenance can receive different treatment depending on whether the principal is a private foreign company, an EU actor, a non-EU state-linked entity, or a third-country sponsor tied to an interest-representation service.","claimant":"INV-145 synthesis","counter":"Different legal objectives and constitutional contexts may justify some non-isomorphic design choices.","gap":"Normative legitimacy requires a separate legal/policy judgment; this run establishes comparative mechanics.","gap_type":"NORMATIVE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-002","FCT-008","FCT-012","FCT-016","FCT-017","FCT-019"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-004","QRY-008","QRY-009"],"axis":"PRINCIPAL_SCOPE","links":["CLM-001","CLM-002","CTRL-001"],"question":"Who counts as the relevant foreign principal/mandant/sponsor in each regime?","result_ids":["FCT-002","FCT-008","FCT-012","FCT-019"],"sought_objects":["FOREIGN_PRINCIPAL","MANDANT_ETRANGER","THIRD_COUNTRY_SPONSOR"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-001","QRY-004","QRY-008"],"axis":"RELATION_TRIGGER","links":["CLM-001","CLM-002"],"question":"What relationship between actor and foreign principal is required?","result_ids":["FCT-001","FCT-009","FCT-019"],"sought_objects":["ORDER","REQUEST","DIRECTION","CONTROL","ATTRIBUTION"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-001","QRY-004","QRY-006","QRY-009"],"axis":"ACTIVITY_SCOPE","links":["CLM-001","CTRL-005"],"question":"Which political, lobbying, communication or funding activities trigger disclosure?","result_ids":["FCT-001","FCT-010","FCT-016","FCT-020"],"sought_objects":["POLITICAL_ACTIVITY","PUBLIC_COMMUNICATION","LOBBYING","FUNDS"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-001","QRY-008"],"axis":"EXEMPTIONS_SAFEGUARDS","links":["CLM-001","CTRL-003","CTRL-005"],"question":"Which exemptions or safeguards prevent overbroad foreign-agent classification?","result_ids":["FCT-003","FCT-017","FCT-018","FCT-021"],"sought_objects":["COMMERCIAL","ACADEMIC","LEGAL","LDA","FUNDING_ONLY","ANTI_STIGMA"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-001","QRY-006"],"axis":"SANCTIONS","links":["CLM-005"],"question":"What sanctions can follow non-compliance?","result_ids":["FCT-004","FCT-011"],"sought_objects":["CRIMINAL","CIVIL","ADMINISTRATIVE"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-002","QRY-003","QRY-005"],"axis":"ENFORCEMENT","gap":"No comparable multi-year French enforcement denominator exists yet; the EU framework is not final.","gap_type":"BASELINE","linked_ids":["CLM-003","CLM-005","CTRL-004"],"links":["CLM-003","CLM-005","CTRL-004"],"question":"What observable implementation/enforcement exists under comparable time windows?","reason":"Time-comparable enforcement intensity cannot be established as of 2026-09-07.","result_ids":["FCT-005","FCT-006","FCT-007","FCT-014"],"sought_objects":["REGISTRATIONS","INSPECTIONS","CHARGES","CONVICTIONS","HATVP_REGISTER"],"status":"GAP"}
AXS-007 | {"attempt_ids":["QRY-007","QRY-008","QRY-009"],"axis":"EU_STATUS","links":["CLM-004","CTRL-003"],"question":"Is the EU framework final and enforceable as of the investigation date?","result_ids":["FCT-015","FCT-016","FCT-017","FCT-018","FCT-019"],"sought_objects":["LEGISLATIVE_STATUS","PARLIAMENT_POSITION","FINAL_DIRECTIVE"],"status":"SATURATED"}
AXS-008 | {"attempt_ids":["QRY-001","QRY-004","QRY-008","QRY-009"],"axis":"SYMMETRY","links":["CLM-003","CLM-006","CTRL-001","CTRL-002"],"question":"Would isomorphic conduct be classified the same under each regime?","result_ids":["FCT-002","FCT-008","FCT-012","FCT-017","FCT-019"],"sought_objects":["PRIVATE_FOREIGN_COMPANY","EU_STATE","NON_EU_STATE","FUNDING_ONLY","TASKED_REPRESENTATION"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"Registration regimes may improve disclosure without measurably changing influence behavior; observed prosecutions do not identify deterrent effect.","gap":"No cross-regime causal design measures transparency or deterrence effects.","gap_type":"CAUSALITY","limit":"The legal trigger and enforcement tools are documented; downstream deterrence, public-opinion change and policy outcomes are not causally identified.","mechanism":"foreign-principal/sponsor relationship + covered influence activity -> registration/disclosure obligation -> public transparency and compliance/enforcement pressure","status":"UNRESOLVED","support":["FCT-001","FCT-004","FCT-009","FCT-010","FCT-011","FCT-016"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Private-foreign-company control: FARA can treat any foreign-organized or foreign-based entity as a foreign principal, while the French foreign-influence regime does not treat mere foreign corporate ownership as sufficient and instead requires the relevant state/party/control/majority-funding relationship.","status":"SUPPORTED","support":["FCT-002","FCT-008","FCT-012"]}
CTRL-002 | {"control":"EU-geography control: the French text explicitly excludes EU Member States and EU political parties from the mandant-étranger category. This proves a geographic legal asymmetry, but not selective enforcement or illegitimacy by itself.","status":"SUPPORTED","support":["FCT-008"]}
CTRL-003 | {"control":"Funding-only control: the Parliament position on the EU proposal says foreign funding unrelated to a third-country interest-representation activity should not trigger the regime, preventing funding alone from becoming command or agency.","status":"SUPPORTED","support":["FCT-017","FCT-018"]}
CTRL-004 | {"control":"Maturity control: FARA had 527 active registrants and documented inspections/charges in 2024 and a conviction in 2026; the French register began only on 1 October 2025 and showed twelve entities on 7 September 2026. Those observations do not provide comparable enforcement denominators.","status":"SUPPORTED","support":["FCT-005","FCT-006","FCT-007","FCT-013","FCT-014"]}
CTRL-005 | {"control":"Transparency-not-prohibition control: DOJ says FARA disclosure does not restrict advocacy content, while HATVP itself distinguishes legitimate foreign influence from interference; foreign-agent-style transparency should not be equated automatically with illegality or hostile interference.","status":"SUPPORTED","support":["FCT-020","FCT-021"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:9|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FAIL:MNEMO_UNAVAILABLE | MnemoLite | - | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | ACCEPT | SRC-001 | https://www.justice.gov/nsd-fara/frequently-asked-questions | FARA scope foreign principal exemptions obligations penalties
QRY-002 | FETCH | ACCEPT | SRC-002 | https://www.justice.gov/nsd/media/1406631/dl?inline= | FARA 2024 second semiannual report registrants enforcement inspections charges
QRY-003 | FETCH | ACCEPT | SRC-003 | https://www.justice.gov/usao-sdfl/pr/former-us-congressman-and-lobbyist-convicted-acting-unregistered-agents-venezuela | FARA conviction May 2026 Rivera Nuhfer Venezuela
QRY-004 | FETCH | ACCEPT | SRC-004 | https://www.hatvp.fr/espacedeclarant/influence-etrangere/quest-ce-que-linfluence-etrangere/ | HATVP definition mandant étranger EU exclusion actions sanctions
QRY-005 | FETCH | ACCEPT | SRC-005 | https://www.hatvp.fr/repertoire-de-linfluence-etrangere/liste-des-entites-influence-enregistrees/ | HATVP registered foreign influence entities 2026
QRY-006 | FETCH | ACCEPT | SRC-006 | https://www.hatvp.fr/la-haute-autorite/lencadrement-de-linfluence-etrangere/le-repertoire-de-linfluence-etrangere/ | HATVP foreign influence register scope control sanctions 2026
QRY-007 | FETCH | ACCEPT | SRC-007 | https://eur-lex.europa.eu/procedure/EN/2023_463 | EU 2023/0463 status September 2026 third country interest representation
QRY-008 | FETCH | ACCEPT | SRC-008 | https://www.europarl.europa.eu/doceo/document/TA-10-2025-0306_EN.html | European Parliament amendments third-country interest representation foreign funding safeguards 27 Nov 2025
QRY-009 | FETCH | ACCEPT | SRC-009 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=COM:2023:637:FIN | Commission proposal transparency interest representation third countries 2023

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:other:us-doj | DOJ-FARA-FAQ | DOJ FARA Frequently Asked Questions | 2026-07-18 | 2026-09-07T03:43:00+00:00 | FAQ definitions/exemptions/registration/penalties | https://www.justice.gov/nsd-fara/frequently-asked-questions
SRC-002 | ◈ | fam:other:us-doj | DOJ-FARA-REPORT-2024-H2 | FARA Second Semi-Annual Report 2024 | 2024-12-31 | 2026-09-07T03:43:00+00:00 | pp. 9-11 statistical summary and enforcement; period ending 2024-12-31 | https://www.justice.gov/nsd/media/1406631/dl?inline=
SRC-003 | ◈ | fam:other:us-doj | DOJ-SDFL-RIVERA-2026 | Former U.S. Congressman and Lobbyist Convicted of Acting as Unregistered Agents of Venezuela | 2026-05-01 | 2026-09-07T03:43:00+00:00 | press release conviction | https://www.justice.gov/usao-sdfl/pr/former-us-congressman-and-lobbyist-convicted-acting-unregistered-agents-venezuela
SRC-004 | ◈ | fam:other:hatvp | HATVP-INFLUENCE-FAQ | HATVP - Qu’est-ce que l’influence étrangère ? | 2026-09-07 | 2026-09-07T03:43:00+00:00 | dynamic current page; definitions, obligations, sanctions | https://www.hatvp.fr/espacedeclarant/influence-etrangere/quest-ce-que-linfluence-etrangere/
SRC-005 | ◈ | fam:other:hatvp | HATVP-INFLUENCE-REGISTER-LIST | Liste des entités influence enregistrées | 2026-09-07 | 2026-09-07T03:43:00+00:00 | dynamic live register list as checked 2026-09-07 | https://www.hatvp.fr/repertoire-de-linfluence-etrangere/liste-des-entites-influence-enregistrees/
SRC-006 | ◈ | fam:other:hatvp | HATVP-INFLUENCE-REGISTER-OVERVIEW | Le répertoire de l’influence étrangère | 2026-09-07 | 2026-09-07T03:43:00+00:00 | dynamic current page; scope, controls, sanctions | https://www.hatvp.fr/la-haute-autorite/lencadrement-de-linfluence-etrangere/le-repertoire-de-linfluence-etrangere/
SRC-007 | ◈ | fam:other:eu-legislative | EURLEX-2023-0463-COD | EUR-Lex procedure 2023/0463/COD | 2023-12-13 | 2026-09-07T03:43:00+00:00 | procedure status ongoing as checked 2026-09-07 | https://eur-lex.europa.eu/procedure/EN/2023_463
SRC-008 | ◈ | fam:other:eu-parliament | EP-P10-TA-2025-0306 | European Parliament amendments P10_TA(2025)0306 | 2025-11-27 | 2026-09-07T03:43:00+00:00 | amendments 12-16, 29, 64+ | https://www.europarl.europa.eu/doceo/document/TA-10-2025-0306_EN.html
SRC-009 | ◈ | fam:other:eu-commission | COM-2023-637-FINAL | COM(2023) 637 final | 2023-12-12 | 2026-09-07T03:43:00+00:00 | proposal scope and rationale | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=COM:2023:637:FIN

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.justice.gov/nsd-fara/frequently-asked-questions | other:us-doj | 2026-07-18 | FARA agent trigger | FARA requires registration and disclosure when a person acts at the order, request, direction or control of a foreign principal and performs covered activities such as political activity, public relations, political consulting, fundraising or representation before U.S. government officials. | -
FCT-002 | FACT | ✧ | https://www.justice.gov/nsd-fara/frequently-asked-questions | other:us-doj | 2026-07-18 | FARA foreign principal breadth | Under FARA, a foreign principal can be a foreign government or political party, but also any non-U.S.-domiciled person and any entity organized under foreign law or principally based abroad; state control is not required for foreign-principal status. | -
FCT-003 | FACT | ✧ | https://www.justice.gov/nsd-fara/frequently-asked-questions | other:us-doj | 2026-07-18 | FARA exemptions | FARA provides exemptions including diplomatic, bona fide commercial, humanitarian, religious/scholastic/academic/scientific/fine-arts, legal-representation, and certain Lobbying Disclosure Act activities; the LDA exemption does not apply when a foreign government or foreign political party is the principal beneficiary. | -
FCT-004 | FACT | ✧ | https://www.justice.gov/nsd-fara/frequently-asked-questions | other:us-doj | 2026-07-18 | FARA penalties and enforcement powers | The DOJ states that a willful FARA violation can carry up to five years imprisonment and a fine up to 250,000 dollars, with civil enforcement allowing injunctions requiring registration or correction of deficient filings. | -
FCT-005 | FACT | ✧ | https://www.justice.gov/nsd/media/1406631/dl?inline= | other:us-doj | 2024-12-31 | FARA 2024 H2 registry scale | For July through December 2024, DOJ reported 66 new registration statements, 22 terminations, 527 active registrants representing 788 foreign principals, and 2,461 short-form registrations. | -
FCT-006 | FACT | ✧ | https://www.justice.gov/nsd/media/1406631/dl?inline= | other:us-doj | 2024-12-31 | FARA 2024 H2 enforcement | For July through December 2024, the FARA Unit reported six books-and-records inspections, no civil FARA causes of action filed, and criminal charges under FARA against five individuals. | -
FCT-007 | FACT | ✧ | https://www.justice.gov/usao-sdfl/pr/former-us-congressman-and-lobbyist-convicted-acting-unregistered-agents-venezuela | other:us-doj | 2026-05-01 | FARA criminal enforcement 2026 | On 1 May 2026, DOJ reported jury convictions of David Rivera and Esther Nuhfer for FARA offenses tied to secretly lobbying on behalf of the Venezuelan government, demonstrating continued criminal enforcement beyond the 2024 reporting period. | -
FCT-008 | FACT | ✧ | https://www.hatvp.fr/espacedeclarant/influence-etrangere/quest-ce-que-linfluence-etrangere/ | other:hatvp | 2026-09-07 | French mandant foreign definition | The French HATVP regime defines a mandant étranger as a foreign power outside the European Union, a legal entity directly or indirectly directed, controlled or financed more than 50 percent by a foreign power, or a foreign political party except parties from EU Member States. | -
FCT-009 | FACT | ✧ | https://www.hatvp.fr/espacedeclarant/influence-etrangere/quest-ce-que-linfluence-etrangere/ | other:hatvp | 2026-09-07 | French agency relation trigger | A person is treated as acting for a foreign mandant when the person carries out influence actions on the order, at the request, or under the direction or control of that foreign mandant. | -
FCT-010 | FACT | ✧ | https://www.hatvp.fr/espacedeclarant/influence-etrangere/quest-ce-que-linfluence-etrangere/ | other:hatvp | 2026-09-07 | French covered influence actions | The French regime covers, when conducted for a foreign mandant, communications with public officials, communications to the public, and certain collection or transfer of funds without consideration aimed at influencing public decisions or public policy. | -
FCT-011 | FACT | ✧ | https://www.hatvp.fr/la-haute-autorite/lencadrement-de-linfluence-etrangere/le-repertoire-de-linfluence-etrangere/ | other:hatvp | 2026-09-07 | French sanctions | HATVP states that non-compliance can lead after notice to a financial penalty of up to 1,000 euros per day; individuals can face up to three years imprisonment and a 45,000-euro fine, while legal persons can face a 225,000-euro fine and additional penalties. | -
FCT-012 | FACT | ✧ | https://www.hatvp.fr/espacedeclarant/influence-etrangere/quest-ce-que-linfluence-etrangere/ | other:hatvp | 2026-09-07 | French ownership is not sufficient alone | HATVP expressly states that mere ownership of a legal entity by a foreign company does not by itself make the entity an actor of foreign influence; the relevant relationship to a foreign power, political party, or state-controlled or state-majority-funded entity must be established. | -
FCT-013 | FACT | ✧ | https://www.hatvp.fr/la-haute-autorite/lencadrement-de-linfluence-etrangere/le-repertoire-de-linfluence-etrangere/ | other:hatvp | 2025-10-01 | French register implementation date | The French foreign-influence register entered into operation on 1 October 2025, with the first activity declarations opening in January 2026. | -
FCT-014 | FACT | ✧ | https://www.hatvp.fr/repertoire-de-linfluence-etrangere/liste-des-entites-influence-enregistrees/ | other:hatvp | 2026-09-07 | French register observed population | As checked on 7 September 2026, the HATVP public list displayed twelve registered foreign-influence entities, including consultancies and companies linked on the register to foreign powers such as China, Morocco, Norway, Qatar and Togo; this is an observed registry count, not an enforcement denominator. | -
FCT-015 | FACT | ✧ | https://eur-lex.europa.eu/procedure/EN/2023_463 | other:eu-legislative | 2026-09-07 | EU proposal legislative status | EUR-Lex lists procedure 2023/0463/COD on transparency of third-country interest representation as ongoing as of 7 September 2026; the European Parliament adopted amendments on 27 November 2025 and referred the matter back for interinstitutional negotiations. | -
FCT-016 | FACT | ✧ | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=COM:2023:637:FIN | other:eu-commission | 2023-12-12 | EU proposal object | The Commission proposal targets interest-representation activities carried out on behalf of third countries with the objective of influencing policy, legislation or public decision-making in the Union; its legal object is the representation service or attributable activity, not foreign funding in the abstract. | -
FCT-017 | FACT | ✧ | https://www.europarl.europa.eu/doceo/document/TA-10-2025-0306_EN.html | other:eu-parliament | 2025-11-27 | EU Parliament foreign-funding safeguard | The Parliament amendments state that entities should not become subject merely because they receive funding from abroad and that funding unrelated to third-country interest representation should remain outside the directive. | -
FCT-018 | FACT | ✧ | https://www.europarl.europa.eu/doceo/document/TA-10-2025-0306_EN.html | other:eu-parliament | 2025-11-27 | EU Parliament anti-stigma safeguard | The Parliament amendments expressly contrast the proposal with stigmatizing foreign-agent laws and require factual, neutral presentation so registration itself does not produce adverse consequences such as stigmatization. | -
FCT-019 | FACT | ✧ | https://www.europarl.europa.eu/doceo/document/TA-10-2025-0306_EN.html | other:eu-parliament | 2025-11-27 | EU third-country sponsor attribution | The Parliament text defines the relevant sponsor around a third country and attributable public or private entities, including circumstances such as decisive influence or ultimate control, rather than treating every foreign private company as equivalent to a state-linked sponsor. | -
FCT-020 | FACT | ✧ | https://www.justice.gov/nsd-fara/frequently-asked-questions | other:us-doj | 2026-07-18 | FARA disclosure not prohibition | DOJ describes FARA as a transparency regime: registration does not limit the content of political advocacy or informational materials, though disclosure and labeling duties apply. | -
FCT-021 | FACT | ✧ | https://www.hatvp.fr/la-haute-autorite/lencadrement-de-linfluence-etrangere/le-repertoire-de-linfluence-etrangere/ | other:hatvp | 2026-09-07 | HATVP influence versus interference distinction | HATVP states that foreign influence strategies are a legitimate component of international relations and distinguishes them from foreign interference aimed at destabilizing institutions and harming national interests. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-001
FCT-005 | SRC-002
FCT-006 | SRC-002
FCT-007 | SRC-003
FCT-008 | SRC-004
FCT-009 | SRC-004
FCT-010 | SRC-004
FCT-011 | SRC-006
FCT-012 | SRC-004
FCT-013 | SRC-006
FCT-014 | SRC-005
FCT-015 | SRC-007
FCT-016 | SRC-009
FCT-017 | SRC-008
FCT-018 | SRC-008
FCT-019 | SRC-008
FCT-020 | SRC-001
FCT-021 | SRC-006

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

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:Freeze comparative scope and symmetry controls.
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:Collect and reconcile authoritative legal and enforcement sources.
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:Consolidate source-backed facts and enforcement baselines.
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:Freeze causal limits and test whether any causal comparison is computable.
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 | NEXT_ACTION:Verify comparative claims, typed gaps and symmetry controls.
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:Close investigation accountability and prepare technical narrative.
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:Write frozen technical narrative and execute PRE gate.

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-07T03:53:11.981293+00:00","fact_mem":{},"mnemo_row":"BLOCKED:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":21,"eligible":21,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:BLOCKED:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:21;attempted:0;success:0;failure:0;blocked:21} | WRITEBACK_EXECUTION_V1:[21 rows, see section]

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
