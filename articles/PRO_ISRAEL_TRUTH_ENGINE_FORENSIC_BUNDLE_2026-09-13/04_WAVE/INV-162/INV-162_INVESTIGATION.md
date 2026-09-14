ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260913-1340-voices-israel-civil-society-funding | PARENT_RUN_ID:NONE | AS_OF:2026-09-13
INPUT_KIND:DOCUMENT | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/inv162_work/runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-13_voices-israel-civil-society-funding/2026-09-13_13-40_voices-israel-civil-society-funding_INPUT.md | SUBJECT_SLUG:voices-israel-civil-society-funding | SUBJECT_FP:sha256:e3dc95f69fcbc8fe3a4196165287d1d6c4855af48c3e8a96b3cd6921af005b7a | INPUT_SHA256:sha256:44d7bb9f3bbb230221b1fbdd86b0e7099ca24813edc1e4d47ec64cff2c8ad9cf
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:Israel 2022-2026 plus France/EU: Voices of Israel public-diplomacy funding architecture, named beneficiaries/programs, project deliverables, matching, milestones and downstream France/EU activities; do not infer state command from grant receipt or project selection.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/MONEY.md,clusters/NETWORK.md,clusters/POWER.md,clusters/ICEBERG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-162 — Voices of Israel : financements publics vers société civile

## Objet

Déterminer comment des fonds publics israéliens de diplomatie d'influence sont transformés en projets portés par des organisations de société civile, identifier les bénéficiaires ou projets France/UE publiquement traçables, et établir jusqu'où les conditions de financement ferment une relation de tasking sans confondre financement de projet, contrôle organisationnel, exposition de décideurs et effet politique.

## Résultat central

**FACT.** L'appel à projets inspecté de Voices of Israel décrit un mécanisme de cofinancement public-privé adossé à une joint-venture avec le ministère israélien chargé des affaires de diaspora. Il vise explicitement des projets renforçant le récit israélien, le soutien international à Israël et les capacités d'organisations pro-Israël (FCT-001 à FCT-003).

**FACT.** Le mécanisme n'est pas un grant général sans conditions. Le RFP impose un financement partagé à 50/50, des critères de sélection portant notamment sur le plan d'action, la capacité d'exécution et le ratio investissement/résultat attendu, ainsi que des jalons, justificatifs de dépenses et rapports de performance conditionnant le paiement (FCT-004 à FCT-006).

**INFERENCE BORNÉE.** Cette architecture ferme une relation plus forte que `État -> ressource générale -> organisation`. Au niveau d'un projet sélectionné, elle soutient `ressource publique -> objectifs contractuels -> jalons/livrables -> contrôle de conformité avant paiement`. Elle ne permet toutefois pas de promouvoir automatiquement cette relation en `État -> commandement général de l'organisation` ni en `État -> position politique dictée` (CLM-001, CLM-002 ; CAU-001).

## Échelle et fonction du dispositif

**FACT.** Une source contemporaine indépendante décrit Voices of Israel comme un véhicule gouvernemental-philanthropique doté d'un modèle de matching public/privé et se présentant comme funder/accelerator d'organisations pro-Israël. La même source rapporte une volonté de coordination plus organisée entre l'appareil public et la société civile de plaidoyer (FCT-007 à FCT-009).

Cette pièce contextualise la fonction institutionnelle du dispositif mais ne remplace pas les contrats projet par projet. Le niveau probatoire retenu reste donc la relation documentée dans le RFP : sélection, cofinancement, objectifs, jalons et reporting.

## Arête ELNET / Europe

**FACT BORNÉ.** Une enquête journalistique fondée sur la documentation publique de Voices indique qu'ELNET figurait parmi les projets sélectionnés, pour des délégations et conférences destinées à des décideurs européens (FCT-010). La page primaire correspondante de Voices n'était plus inspectable directement lors du run ; le statut demeure donc borné par un gap de provenance primaire actuelle (CLM-003 ; CAU-002).

**FACT.** Les propres publications d'ELNET France et d'entités ELNET européennes documentent en parallèle des délégations visant explicitement des responsables politiques, journalistes, responsables de sécurité ou experts européens et français. Elles décrivent des rencontres avec des responsables israéliens, des briefings militaires ou sécuritaires et, dans certains cas, des demandes politiques adressées aux interlocuteurs français ou européens (FCT-013 à FCT-016).

Ces publications ferment `ELNET -> organisation de délégations -> exposition à des responsables/briefings/demandes`. Elles ne constituent pas une preuve indépendante que les interlocuteurs ont été persuadés, ont modifié leur comportement ou ont adopté une politique à cause de l'exposition (CLM-004, CLM-007 ; CAU-003).

## Ce que le corpus ne ferme pas

Le corpus inspecté ne permet pas d'établir :

- le montant exact de Voices of Israel affecté au projet ELNET mentionné ;
- un ledger complet des bénéficiaires France/UE de Voices entre 2023 et 2026 ;
- une convention de financement reliant un paiement Voices précis à une délégation française nommée ;
- un livrable contractuel démontrant qu'une position politique française précise devait être obtenue ;
- une chaîne `financement -> exposition -> persuasion -> comportement -> décision publique contrefactuelle` ;
- un commandement général d'ELNET ou d'autres organisations bénéficiaires par l'État israélien.

Ces limites sont des gaps d'allocation, de provenance, d'accès et de causalité (CLM-005 à CLM-007 ; CAU-002 à CAU-004). Elles ne constituent ni une preuve d'autonomie complète, ni une preuve d'un tasking caché.

## Contrôles négatifs

Le modèle est borné par plusieurs contrôles matériels :

- le cofinancement obligatoire signifie que le projet n'est pas nécessairement financé intégralement par l'État ;
- jalons et rapports démontrent un contrôle contractuel de projet, pas une gouvernance de toute l'organisation ;
- la mention d'ELNET comme projet sélectionné reste limitée tant que l'award ou la page primaire n'est pas réinspecté ;
- les pages ELNET sont de bonnes sources pour leurs propres activités et intentions, pas pour prouver leurs effets sur les cibles ;
- l'absence de montant ELNET publiquement inspectable interdit d'inventer une allocation ;
- financement public étranger et diplomatie d'influence ne sont pas automatiquement synonymes d'ingérence clandestine (CTRL-001 à CTRL-006).

## Conclusion bornée

INV-162 apporte un gain probatoire précis : **dans le dispositif Voices of Israel, le financement public peut prendre la forme d'un tasking contractuel au niveau du projet**, avec objectifs préalables, cofinancement, critères de sélection, jalons, justificatifs et rapports de performance. Le corpus relie en outre ELNET, de manière bornée, à un projet destiné aux décideurs européens et documente indépendamment l'existence de délégations France/Europe ciblant des responsables publics et acteurs d'opinion.

Le saut décisif reste ouvert : aucun élément inspecté ne permet d'affecter un paiement Voices déterminé à une délégation française précise puis à une décision publique causée. Le prochain gain ne viendra donc pas d'une accumulation de communications générales, mais d'awards, conventions, budgets projet, rapports d'exécution et empreintes décisionnelles permettant de fermer `project tasking -> action française nommée -> effet`.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:4|EDI_DECISIVE:3|SRC_COMPLETE:6/6

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **status:** BOUNDED
- **timeline:**
  - 2022 Voices rebrand/joint-venture funding model publicly described
  - Nov 2023 emergency RFP sets 50/50 matching, narrative/support objectives, milestones and performance reports
  - Jan-Mar 2024 ELNET France/Europe actor pages document targeted French/European missions and official briefings
  - Mar 2025 ELNET France documents multinational defence delegation
  - Nov 2025 taz reports Voices selected-project listing for ELNET but exact spending undisclosed

### MANIPULATION_REPORT
- **assumptions:**
  - Voices RFP applies to emergency projects under its stated terms, not every Voices project historically
  - taz accurately captured the then-visible Voices portfolio entry for ELNET, but direct current page is unavailable
  - ELNET actor pages reliably establish what ELNET organized and intended, not independent effect
- **clusters:**
  - MONEY
  - NETWORK
  - POWER
  - ICEBERG
- **complexity:**
  - **band:** HIGH
  - **score:** 9
- **implicit:**
  - **I01:** government cofunding can impose project deliverables without controlling recipient governance
  - **I02:** multiple funding streams may overlap in ELNET missions
  - **I03:** decision-makers may self-select into delegations
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - **P01:** ministry -> joint-venture fund -> cofunded project
  - **P02:** contract criteria -> milestone -> report -> reimbursement
  - **P03:** selected project -> decision-maker exposure
  - **P04:** exposure -> intended support -> unclosed policy effect
- **priorities:**
  - identify direct France/EU beneficiaries
  - retrieve award amounts/contracts
  - map deliverables
  - test tasking boundary
  - measure effect separately
- **query_guidance:** prioritize award lists, contracts, budgets, performance reports, archived portfolio pages and recipient accounts; do not infer organization-wide command from project funding
- **rhetorical:**
  - **R01:** state money means proxy
  - **R02:** selected project means every activity funded
  - **R03:** delegation means persuasion
  - **R04:** lack of public amount means secrecy proves wrongdoing
- **speaker:**
  - **goal:** forensic mapping of Voices of Israel civil-society funding into France/EU recipient and deliverable chains
  - **target:** state funding -> project tasking -> recipient -> France/EU activity -> effect ceiling
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** ministry
  - **S02:** Voices
  - **S03:** matching
  - **S04:** grant
  - **S05:** milestone
  - **S06:** report
  - **S07:** recipient
  - **S08:** ELNET
  - **S09:** delegation
  - **S10:** decision-maker
  - **S11:** France
  - **S12:** EU
  - **S13:** allocation_gap
  - **S14:** tasking
  - **S15:** effect
- **threats:**
  - funding=command
  - project=organization
  - selection=allocation
  - exposure=persuasion
  - support request=policy effect
  - foreign=interference

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - ALLOCATION
    - ACCESS
  - **input_ids:**
    - FCT-002
    - FCT-004
    - FCT-005
    - FCT-007
    - FCT-009
    - FCT-010
    - FCT-011
  - **module:** clusters/MONEY.md
  - **negative_results:**
    - no inspectable France/EU award ledger
  - **not_computable:**
    - Voices amount funding a named ELNET France mission
  - **operations_applied:**
    - funding-model reconstruction
    - matching test
    - allocation-gap test
  - **reason:** reconstruct government/private cofunding and recipient-award visibility
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-003
    - CLM-005
    - CAU-001
    - CAU-002
  - **status:** DONE
  - **trigger:** €
- **item 2:**
  - **gaps:**
    - award agreements outside RFP template
  - **input_ids:**
    - FCT-002
    - FCT-008
    - FCT-010
    - FCT-013
    - FCT-015
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no general command edge
  - **not_computable:**
    - network-wide state-control probability
  - **operations_applied:**
    - entity/relation separation
    - project-versus-organization boundary
  - **reason:** separate ministry/Voices/project/recipient relations from organization-wide control
  - **result_ids:**
    - CLM-002
    - CLM-003
    - CTRL-001
    - CTRL-002
  - **status:** DONE
  - **trigger:** 🌐
- **item 3:**
  - **gaps:**
    - CAUSALITY
  - **input_ids:**
    - FCT-003
    - FCT-013
    - FCT-014
    - FCT-015
    - FCT-016
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no causal policy outcome closed
  - **not_computable:**
    - marginal France/EU policy effect
  - **operations_applied:**
    - tasking/exposure/effect separation
    - policy-ask extraction
  - **reason:** test funded capacity -> targeted exposure -> policy outcome
  - **result_ids:**
    - CLM-004
    - CLM-007
    - CAU-003
    - CAU-004
  - **status:** DONE
  - **trigger:** ↕
- **item 4:**
  - **gaps:**
    - ACCESS
    - ALLOCATION
  - **input_ids:**
    - FCT-010
    - FCT-011
  - **module:** clusters/ICEBERG.md
  - **negative_results:**
    - no basis to infer hidden funding amount from missing public ledger
  - **not_computable:**
    - complete France/EU beneficiary universe
  - **operations_applied:**
    - omission test
    - shadow-recipient search
    - denominator/proxy test
  - **reason:** search for missing beneficiary lists, project amounts and shadow allocations
  - **result_ids:**
    - CLM-005
    - CLM-006
    - CTRL-003
    - CTRL-005
  - **status:** DONE
  - **trigger:** Ξ

### SCOPING_REPORT
- **classification_dimensions:**
  - funding source
  - public/private share
  - recipient
  - project purpose
  - milestones
  - reporting
  - France/EU target
  - tasking
  - policy effect
- **exclusions:**
  - Jewish identity=state proxy
  - civil-society grant=state command
  - selected project=specific French operation funding
  - delegation=persuasion
  - support objective=policy effect
- **scope:** Israel 2022-2026 plus France/EU recipient/deliverable edges; prior 2022 structure only where needed to understand 2023-2026 mechanism
- **status:** ACTIVE

### CREDO
- public funding != organization-wide command
- project tasking != general proxy status
- selected project != named France-operation financing
- delegation != persuasion
- exposure != behavior
- policy request != adoption
- foreign public diplomacy != clandestine interference by default
- actor self-description != independent effect proof
- missing ledger != proof of concealment

### COGNITIVE_MAP
- **chain:**
  - Israeli ministry public money
  - Voices of Israel joint venture
  - cofunded civil-society project
  - contractual objectives/milestones/reporting
  - recipient activity
  - France/EU exposure
  - reception
  - behavior/policy outcome
- **core_model:** Voices of Israel provides a documented project-level mechanism by which Israeli public money is combined with private matching funds and paid against specified public-diplomacy objectives, milestones, expenses and performance reports. ELNET is reported as a selected project for European decision-makers, and ELNET actor records document France/Europe-facing delegations. The inspected corpus does not expose the project-specific Voices award amount or contract for a named French operation, and downstream policy effect is not established.
- **rival_models:**
  - transparent public-diplomacy grantmaking rather than covert state control
  - mixed public/private cofunding with recipient autonomy outside funded project
  - ELNET activities financed from multiple sources with no one-to-one Voices allocation
  - self-selection of already supportive decision-makers
  - public diplomacy activity without measurable policy effect

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** The RFP specifies goals, selection criteria, 50/50 matching, milestones, documented expenses and performance-report approval.
  - **resolution:** Project-level tasking/monitoring is supported; unrestricted-grant model is false for this RFP.
  - **thesis:** Voices of Israel is merely an unrestricted grant pool.
- **item 2:**
  - **antithesis:** The inspected corpus lacks project-level award and allocation records for named French missions.
  - **resolution:** The program relationship is boundedly supported; operation-level funding attribution remains open.
  - **thesis:** Because ELNET is a Voices selected project, every ELNET France delegation is state-funded.
- **item 3:**
  - **antithesis:** ELNET materials document exposure and explicit requests but not independent before/after behavior change.
  - **resolution:** Close action/exposure; leave persuasion/policy effect as a causal gap.
  - **thesis:** Decision-maker delegations prove political effect.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **from:** Ministry of Diaspora Affairs and Combatting Antisemitism
  - **limits:**
    - 50% bidder matching; project-bounded
  - **resource:** public cofunding under joint venture
  - **support:**
    - FCT-002
    - FCT-004
    - FCT-005
  - **to:** approved public-diplomacy projects
  - **via:** Voices of Israel
- **item 2:**
  - **from:** Voices of Israel
  - **limits:**
    - recipient-level amounts incomplete in inspected corpus
  - **resource:** funding/acceleration plus project-selection and monitoring architecture
  - **support:**
    - FCT-003
    - FCT-005
    - FCT-006
    - FCT-008
  - **to:** pro-Israel civil-society organizations
  - **via:** selected projects
- **item 3:**
  - **from:** Voices selected-project portfolio
  - **limits:**
    - direct primary portfolio page unavailable; exact spending not disclosed
  - **resource:** reported selected project relationship
  - **support:**
    - FCT-010
    - FCT-011
  - **to:** European decision-maker delegations/conferences
  - **via:** ELNET
- **item 4:**
  - **from:** ELNET France/Europe
  - **limits:**
    - Voices-specific operation funding and downstream effect not closed
  - **resource:** delegations, meetings, briefings and access
  - **support:**
    - FCT-012
    - FCT-013
    - FCT-014
    - FCT-015
    - FCT-016
  - **to:** French/European political, media and security actors
  - **via:** Israel trips / France-Europe missions

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** Ministry of Diaspora Affairs and Combatting Antisemitism
  - **relation:** government joint-venture funding
  - **support:**
    - FCT-002
    - FCT-004
    - FCT-005
  - **to:** Voices of Israel / cofunded projects
- **item 2:**
  - **from:** Voices of Israel
  - **relation:** project selection, matching, milestone/report-controlled reimbursement
  - **support:**
    - FCT-003
    - FCT-004
    - FCT-005
    - FCT-006
  - **to:** civil-society/public-diplomacy projects
- **item 3:**
  - **from:** Voices of Israel selected-project portfolio
  - **relation:** reported selected project
  - **support:**
    - FCT-010
    - FCT-011
  - **to:** ELNET / European decision-maker delegations and conferences
- **item 4:**
  - **from:** ELNET France / Europe
  - **relation:** delegations, briefings, meetings and policy requests
  - **support:**
    - FCT-012
    - FCT-013
    - FCT-014
    - FCT-015
    - FCT-016
  - **to:** French/European political, media and security actors

### IMPACT_MAP
- **affected:**
  - civil-society public-diplomacy capacity
  - European decision-maker exposure environment
  - French political/media/security access to Israeli official framing
- **benefits:**
  - funded capacity, delegations, conferences, messaging and rapid public-diplomacy project execution
- **costs_harms:**
  - potential asymmetry of sponsored access and organized narrative exposure is real as a mechanism; manipulation, capture or policy harm is not established by the current evidence
- **response_change:** Evidence upgrades generic funding to contract-bounded project tasking but does not close France-specific award amounts or downstream decision effects.
- **status:** BOUNDED

### CONTRADICTION_LEDGER
- **item 1:**
  - **claim:** Voices funding makes recipient organizations government proxies
  - **counter:** The RFP closes project objectives and reporting but is 50/50 cofunded and does not establish organization-wide direction.
  - **status:** REFUTED_AS_AUTOMATIC_RULE
- **item 2:**
  - **claim:** ELNET France missions are proven to be financed by Voices of Israel
  - **counter:** ELNET is reported as a selected Voices project for European decision-makers, but no inspected award ledger maps a Voices amount to a named French mission.
  - **status:** PARTIAL / ALLOCATION_GAP
- **item 3:**
  - **claim:** French/European delegates changed policy because of funded trips
  - **counter:** Actor pages establish exposure and explicit asks, not persuasion or counterfactual behavior change.
  - **status:** NOT_ESTABLISHED
- **item 4:**
  - **claim:** No public recipient data exists at all
  - **counter:** Discovery surfaced aggregate government reporting and a selected-project relation, but a complete France/EU beneficiary/award ledger was not inspectable in this run.
  - **status:** TOO_STRONG

### VERIFICATION_REPORT
- **discovery_only_not_promoted:**
  - 2024 Ministry antisemitism report aggregate funding figures because direct PDF fetch returned 403 in this runtime
  - 2026 Knesset public-diplomacy budget page because opened content was not inspectable in current fetch
- **fact_count:** 16
- **limitations:**
  - no complete 2023-2026 recipient/payment ledger
  - no direct current Voices portfolio page
  - no ELNET award amount or grant contract from Voices
  - no participant-level causal effect design
- **primary_records:**
  - Voices of Israel emergency RFP
  - ELNET France January 2024 delegation page
  - ELNET Germany/France Tal Meron mission page
  - ELNET France 2025 defence delegation page
- **query_count:** 30
- **secondary_investigations:**
  - taz 2025 ELNET investigation
  - Jerusalem Post 2022 Voices structure/interviews
- **source_count:** 6
- **status:** PASS_BOUNDED

### EDI_REPORT
- **corpus:** 6 accepted inspected sources; 16 normalized facts; one direct Voices RFP, three ELNET actor pages, one investigative report, one background/interview report
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim:** CLM-001
    - **families:**
      - other:voices_israel
  - **item 2:**
    - **claim:** CLM-003
    - **families:**
      - other:taz
  - **item 3:**
    - **claim:** CLM-004
    - **families:**
      - other:elnet
- **diagnostic_not_truth:** true
- **dimensions:**
  - state funding architecture
  - matching
  - project selection
  - milestones/reporting
  - ELNET selected-project relation
  - France/EU exposure
  - allocation gap
  - policy-effect gap
- **edi:** PROJECT_LEVEL_TASKING_IS_DOCUMENTED_BUT_FRANCE_EU_AWARD_ALLOCATION_AND_POLICY_EFFECT_REMAIN_OPEN
- **source_counts:**
  - **other:elnet:** 3
  - **other:jpost:** 1
  - **other:taz:** 1
  - **other:voices_israel:** 1

### RESPONSIBILITY_MAP
- **item 1:**
  - **actor:** Ministry of Diaspora Affairs and Combatting Antisemitism
  - **responsibility:** government funding share for the Voices joint venture/project scheme
  - **status:** SUPPORTED
  - **support:**
    - FCT-002
    - FCT-004
- **item 2:**
  - **actor:** Voices of Israel
  - **responsibility:** project selection, cofunding, milestone/report review and reimbursement
  - **status:** SUPPORTED
  - **support:**
    - FCT-003
    - FCT-005
    - FCT-006
- **item 3:**
  - **actor:** ELNET France/Europe
  - **responsibility:** organizing documented France/Europe-facing decision-maker delegations and official briefings
  - **status:** SUPPORTED
  - **support:**
    - FCT-012
    - FCT-013
    - FCT-014
    - FCT-015
    - FCT-016
- **item 4:**
  - **actor:** Israeli state/Voices
  - **responsibility:** funding a named ELNET France mission in inspected corpus
  - **status:** NOT_ESTABLISHED_PROJECT_SPECIFIC
  - **support:**
    - CLM-005
    - CAU-002
- **item 5:**
  - **actor:** any funded recipient
  - **responsibility:** causing a French/EU policy outcome through the funding
  - **status:** NOT_ESTABLISHED
  - **support:**
    - CLM-007
    - CAU-003
    - CAU-004

### NEXT_QUERIES
- Retrieve archived Voices of Israel portfolio/award pages and exact ELNET grant award records.
- Obtain 2023-2026 Ministry/Voices beneficiary and payment lists with legal entity identifiers and project amounts.
- Match any ELNET/France/EU grant records to named delegations, conferences, invoices and performance reports.
- For each matched project, test downstream exposure, participant behavior and policy footprint separately.

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-025 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-011,QRY-012,QRY-013,QRY-027 | support:- | counter:- | results:FCT-010,FCT-011,FCT-012 | final:SATURATED | gap:NONE
LED-003 | attempts:QRY-021,QRY-024,QRY-028 | support:- | counter:- | results:FCT-013,FCT-014,FCT-015,FCT-016 | final:SATURATED | gap:NONE
LED-004 | attempts:QRY-005,QRY-006,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018,QRY-019,QRY-020 | support:- | counter:- | results:FCT-010,FCT-011 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-025 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-007,QRY-008,QRY-009,QRY-017,QRY-018,QRY-019,QRY-026 | support:- | counter:- | results:FCT-007,FCT-008,FCT-009 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-021,QRY-022,QRY-023,QRY-024,QRY-027,QRY-028,QRY-029,QRY-030 | support:- | counter:- | results:FCT-010,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-005,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-027 | support:- | counter:- | results:FCT-010,FCT-011,FCT-014 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-025 | support:FCT-002,FCT-003,FCT-004,FCT-005,FCT-006 | counter:The mechanism is project-specific and cofunded; it does not establish control over all activities of a recipient organization. | results:FCT-002,FCT-003,FCT-004,FCT-005,FCT-006 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-025 | support:FCT-003,FCT-004,FCT-005,FCT-006 | counter:Tasking applies to the funded project,not necessarily to the recipient organization beyond that project. | results:FCT-003,FCT-004,FCT-005,FCT-006 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-011,QRY-012,QRY-013,QRY-027 | support:FCT-010 | counter:The current Voices website is suspended and the direct portfolio page could not be freshly inspected; the relationship is therefore supported through an inspected secondary investigation,not a current primary portfolio page. | results:FCT-010 | final:PARTIAL | gap:PROVENANCE
CLM-004 | attempts:QRY-021,QRY-022,QRY-023,QRY-024,QRY-028,QRY-029,QRY-030 | support:FCT-012,FCT-013,FCT-014,FCT-015,FCT-016 | counter:These actor-published materials establish activity and intended exposure,not independent persuasion or policy causation. | results:FCT-012,FCT-013,FCT-014,FCT-015,FCT-016 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-005,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-027 | support:FCT-010,FCT-011,FCT-013,FCT-014 | counter:The broader funding architecture and ELNET selected-project relation make such funding plausible; absence of a public ledger is not evidence that no such allocation exists. | results:FCT-010,FCT-011,FCT-013,FCT-014 | final:GAP | gap:ALLOCATION
CLM-006 | attempts:QRY-001,QRY-002,QRY-006,QRY-007,QRY-008,QRY-009,QRY-017,QRY-018,QRY-019,QRY-020 | support:FCT-010,FCT-011 | counter:Discovery surfaced an official 2024 report describing large aggregate disbursement,but the direct PDF retrieval failed in this run and was not promoted to inspected evidence. | results:FCT-010,FCT-011 | final:GAP | gap:ACCESS
CLM-007 | attempts:QRY-021,QRY-022,QRY-023,QRY-024,QRY-028,QRY-029,QRY-030 | support:FCT-003,FCT-010,FCT-012,FCT-014,FCT-015,FCT-016 | counter:Project designs explicitly seek narrative/support outcomes,so downstream influence is an intended objective and must be tested rather than assumed absent. | results:FCT-012,FCT-013,FCT-014,FCT-015,FCT-016 | final:GAP | gap:CAUSALITY

## STATUS_DELTA_V1
DELTA-001 | CLM-002 | SUPPORTED_BOUNDED | SUPPORTED | Normalize bounded support to canonical terminal status; scope limit remains in counter/claim text.
DELTA-002 | CLM-003 | SUPPORTED_BOUNDED | PARTIAL | Normalize bounded secondary-source support to canonical PARTIAL while preserving PROVENANCE gap.
DELTA-003 | CAU-002 | PARTIAL | UNRESOLVED | Canonical terminalization: recipient/project relation has a material PROVENANCE gap despite bounded supporting evidence.
DELTA-004 | CAU-003 | PARTIAL | UNRESOLVED | Canonical terminalization: action/exposure is supported but downstream reception/effect remains a typed CAUSALITY gap.

## OPEN_GAPS_V1
CLM-003 | CLM | PARTIAL | PROVENANCE | Need an archived/direct Voices project page or grant award document identifying ELNET and the project amount.
CLM-005 | CLM | GAP | ALLOCATION | Need grant award, contract, budget, invoice or performance report mapping Voices funds to a named France/EU ELNET project.
CLM-006 | CLM | GAP | ACCESS | Need direct inspectable ministry award lists, grant register or archived Voices portfolio/award pages.
CLM-007 | CLM | GAP | CAUSALITY | Need recipient-specific outputs, exposure measures, before/after behavior and policy-footprint/counterfactual designs.
CAU-002 | CAU | UNRESOLVED | PROVENANCE | Need archived primary portfolio/grant document and project-specific amount.
CAU-003 | CAU | UNRESOLVED | CAUSALITY | Need participant-level before/after positions, outputs, votes or decisions and suitable controls.
CAU-004 | CAU | GAP | CAUSALITY | Need project agreements, instructions, deliverables and decision-level evidence.

SEMANTIC_COUNTS_V1:LED:4|CLM:7|AXS:4|CAU:4|CTRL:6|ACT:4

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-025"],"evidence_excerpt":"Government-funded 50/50 joint venture with milestone payment and performance reporting.","kind":"FUNDING_LEAD","lead":"Voices of Israel emergency public-diplomacy joint-venture funding architecture","linked_ids":["AXS-001","AXS-002"],"locator":"RFP pp1-3","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006"],"routes":["EXPAND","LINK"],"source_id":"SRC-001","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-011","QRY-012","QRY-013","QRY-027"],"evidence_excerpt":"ELNET listed for delegations and conferences for European decision-makers; exact fund spend not public.","kind":"RECIPIENT_LEAD","lead":"ELNET identified as a selected Voices of Israel project for European decision makers","linked_ids":["AXS-003","AXS-004"],"locator":"taz lines 159-161 citing Voices portfolio","materiality":"DECISIVE","result_ids":["FCT-010","FCT-011","FCT-012"],"routes":["EXPAND","LINK"],"source_id":"SRC-003","status":"SATURATED"}
LED-003 | {"attempt_ids":["QRY-021","QRY-024","QRY-028"],"evidence_excerpt":"French delegation meets Knesset, MFA, IDF/police; stated purpose includes reporting to peers and sustaining support.","kind":"FRANCE_LEAD","lead":"ELNET France missions target French parliamentarians, writers and policy actors with Israeli official briefings and explicit support requests","linked_ids":["AXS-003","AXS-004"],"locator":"January 2024 French delegation","materiality":"DECISIVE","result_ids":["FCT-013","FCT-014","FCT-015","FCT-016"],"routes":["EXPAND","LINK"],"source_id":"SRC-004","status":"SATURATED"}
LED-004 | {"attempt_ids":["QRY-005","QRY-006","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018","QRY-019","QRY-020"],"evidence_excerpt":"Publicly inspectable corpus does not expose a recipient-by-recipient France/UE grant ledger.","kind":"GAP_LEAD","lead":"Project-level Voices funding amounts and contracts for France/UE beneficiaries","linked_ids":["AXS-004"],"locator":"taz line 160; precise VoI spending described as undisclosed","materiality":"DECISIVE","result_ids":["FCT-010","FCT-011"],"routes":["EXPAND","LINK"],"source_id":"SRC-003","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"attempt_ids":["QRY-025"],"claim":"Voices of Israel operates a government-backed cofunding mechanism that conditions public-diplomacy project payments on approved objectives, milestones, documented expenses and performance reports.","claimant":"INV-162","counter":"The mechanism is project-specific and cofunded; it does not establish control over all activities of a recipient organization.","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","result_ids":["FCT-002","FCT-003","FCT-004","FCT-005","FCT-006"],"status":"SUPPORTED","support":"FCT-002,FCT-003,FCT-004,FCT-005,FCT-006"}
CLM-002 | {"attempt_ids":["QRY-025"],"claim":"The contractual architecture closes project-level tasking more strongly than a general unrestricted grant because eligibility, objectives, milestones and reporting are specified before payment.","claimant":"INV-162","counter":"Tasking applies to the funded project, not necessarily to the recipient organization beyond that project.","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","result_ids":["FCT-003","FCT-004","FCT-005","FCT-006"],"status":"SUPPORTED","support":"FCT-003,FCT-004,FCT-005,FCT-006"}
CLM-003 | {"attempt_ids":["QRY-011","QRY-012","QRY-013","QRY-027"],"claim":"ELNET appears in the inspected investigative corpus as a selected Voices of Israel project for delegations and conferences aimed at European decision-makers.","claimant":"INV-162","counter":"The current Voices website is suspended and the direct portfolio page could not be freshly inspected; the relationship is therefore supported through an inspected secondary investigation, not a current primary portfolio page.","gap":"Need an archived/direct Voices project page or grant award document identifying ELNET and the project amount.","gap_type":"PROVENANCE","materiality":"DECISIVE","result_ids":["FCT-010"],"status":"PARTIAL","support":"FCT-010"}
CLM-004 | {"attempt_ids":["QRY-021","QRY-022","QRY-023","QRY-024","QRY-028","QRY-029","QRY-030"],"claim":"ELNET France and related ELNET entities conduct France/Europe-facing delegations that expose French and European political, media and security actors to Israeli officials, military/security briefings and explicit policy requests.","claimant":"INV-162","counter":"These actor-published materials establish activity and intended exposure, not independent persuasion or policy causation.","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","result_ids":["FCT-012","FCT-013","FCT-014","FCT-015","FCT-016"],"status":"SUPPORTED","support":"FCT-012,FCT-013,FCT-014,FCT-015,FCT-016"}
CLM-005 | {"attempt_ids":["QRY-005","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-027"],"claim":"The inspected public corpus does not disclose a project-level ledger linking a specific Voices of Israel payment amount to a named French ELNET delegation or French policy intervention.","claimant":"INV-162","counter":"The broader funding architecture and ELNET selected-project relation make such funding plausible; absence of a public ledger is not evidence that no such allocation exists.","gap":"Need grant award, contract, budget, invoice or performance report mapping Voices funds to a named France/EU ELNET project.","gap_type":"ALLOCATION","materiality":"DECISIVE","result_ids":["FCT-010","FCT-011","FCT-013","FCT-014"],"status":"GAP","support":"FCT-010,FCT-011,FCT-013,FCT-014"}
CLM-006 | {"attempt_ids":["QRY-001","QRY-002","QRY-006","QRY-007","QRY-008","QRY-009","QRY-017","QRY-018","QRY-019","QRY-020"],"claim":"The inspected corpus does not identify the full set of 2023-2026 France/EU beneficiaries of Voices of Israel funding or their award amounts.","claimant":"INV-162","counter":"Discovery surfaced an official 2024 report describing large aggregate disbursement, but the direct PDF retrieval failed in this run and was not promoted to inspected evidence.","gap":"Need direct inspectable ministry award lists, grant register or archived Voices portfolio/award pages.","gap_type":"ACCESS","materiality":"IMPORTANT","result_ids":["FCT-010","FCT-011"],"status":"GAP","support":"FCT-010,FCT-011"}
CLM-007 | {"attempt_ids":["QRY-021","QRY-022","QRY-023","QRY-024","QRY-028","QRY-029","QRY-030"],"claim":"Voices funding and ELNET exposure activities do not by themselves establish persuasion, behavior change, capture or a French/European policy outcome.","claimant":"INV-162","counter":"Project designs explicitly seek narrative/support outcomes, so downstream influence is an intended objective and must be tested rather than assumed absent.","gap":"Need recipient-specific outputs, exposure measures, before/after behavior and policy-footprint/counterfactual designs.","gap_type":"CAUSALITY","materiality":"DECISIVE","result_ids":["FCT-012","FCT-013","FCT-014","FCT-015","FCT-016"],"status":"GAP","support":"FCT-003,FCT-010,FCT-012,FCT-014,FCT-015,FCT-016"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-025"],"axis":"FUNDING_MODEL","links":["CLM-001","CLM-002","CAU-001"],"question":"What contractual conditions transform public money into project-level deliverables?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006"],"sought_objects":["RFP","matching rules","milestones","performance reports","contract terms"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-001","QRY-007","QRY-008","QRY-009","QRY-017","QRY-018","QRY-019","QRY-026"],"axis":"PROGRAM_SCALE","links":["CLM-001","CLM-006","CAU-001"],"question":"What scale and institutional purpose does Voices of Israel claim for funding civil-society/public-diplomacy projects?","result_ids":["FCT-007","FCT-008","FCT-009"],"sought_objects":["budget statements","funding targets","government-philanthropic structure"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-021","QRY-022","QRY-023","QRY-024","QRY-027","QRY-028","QRY-029","QRY-030"],"axis":"FRANCE_EU_RECIPIENTS","links":["CLM-003","CLM-004","CAU-002","CAU-003"],"question":"Which France/EU programs or organizations are identifiable beneficiaries or selected projects?","result_ids":["FCT-010","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016"],"sought_objects":["ELNET","French delegations","European decision-maker conferences","France/EU activities"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-005","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-027"],"axis":"ALLOCATION_TASKING","links":["CLM-005","CLM-006","CLM-007","CAU-002","CAU-004"],"question":"Can specific Voices funding be linked to a named France/UE operation, contractual deliverable and downstream public decision?","result_ids":["FCT-010","FCT-011","FCT-014"],"sought_objects":["grant award amount","contract","recipient","deliverable","France/EU event","decision footprint"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"The RFP directly specifies state-backed 50/50 project financing, selection criteria, milestones, expense documentation and performance-report approval before payment.","counter":"The bidder contributes half of the project budget and retains organizational autonomy outside the funded project.","gap":"NONE","gap_type":"NONE","limit":"Closes contractual project tasking/monitoring, not organizational command.","mechanism":"Israeli ministry funding -> Voices of Israel cofunding -> selected civil-society project -> milestone/report-controlled payment","status":"SUPPORTED","support":"FCT-002,FCT-003,FCT-004,FCT-005,FCT-006"}
CAU-002 | {"causal_right":"An inspected investigation reports that the Voices portfolio listed ELNET under this project description, and independent ELNET actor pages document matching Europe-facing delegation activity.","counter":"The direct Voices portfolio page is currently unavailable and no inspected award amount/contract maps Voices money to a named ELNET operation.","gap":"Need archived primary portfolio/grant document and project-specific amount.","gap_type":"PROVENANCE","limit":"Recipient/project relationship is bounded; project-level financial allocation remains open.","mechanism":"Voices of Israel -> ELNET selected project -> delegations/conferences for European decision-makers","status":"UNRESOLVED","support":"FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016"}
CAU-003 | {"causal_right":"ELNET actor pages document targeted delegations, official briefings, meetings and explicit requests directed at French/European participants.","counter":"Actor-published accounts do not establish persuasion, later behavior or counterfactual policy change.","gap":"Need participant-level before/after positions, outputs, votes or decisions and suitable controls.","gap_type":"CAUSALITY","limit":"Closes action/exposure, not reception/effect.","mechanism":"ELNET France/Europe delegation -> exposure to Israeli official/security framing and policy requests -> French/European actor reception","status":"UNRESOLVED","support":"FCT-012,FCT-013,FCT-014,FCT-015,FCT-016"}
CAU-004 | {"causal_right":"State-backed project funding and policy-facing recipient activity coexist, but the intermediate organization-wide tasking and policy-effect edges are not established.","counter":"Funding is project-bounded and partly matched by recipients; exact France allocations and outcomes remain missing.","gap":"Need project agreements, instructions, deliverables and decision-level evidence.","gap_type":"CAUSALITY","limit":"Cannot promote project funding to proxy status, capture or policy causation.","mechanism":"Israeli public funding -> recipient organization -> generalized state command -> French/EU policy outcome","status":"GAP","support":"FCT-002,FCT-004,FCT-005,FCT-010,FCT-011,FCT-014"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"The RFP requires 50 percent bidder matching, so funded projects are mixed-resource joint ventures rather than automatically fully state-financed operations.","status":"PASS","support":"FCT-004"}
CTRL-002 | {"control":"Milestone/performance-report controls establish project accountability but do not establish state control of all recipient activities.","status":"PASS","support":"FCT-005,FCT-006"}
CTRL-003 | {"control":"The direct Voices portfolio page is currently unavailable; ELNET selection is therefore not upgraded beyond bounded support from the inspected secondary investigation.","status":"PASS","support":"FCT-010,FCT-011"}
CTRL-004 | {"control":"ELNET actor pages are primary for what ELNET says it organized and intended, but not independent proof of persuasion or policy effect.","status":"PASS","support":"FCT-013,FCT-014,FCT-015,FCT-016"}
CTRL-005 | {"control":"Exact Voices spending on ELNET was reported as undisclosed, blocking attribution of a named public amount to a named French delegation in this run.","status":"PASS","support":"FCT-011"}
CTRL-006 | {"control":"Foreign public-diplomacy funding is not automatically clandestine interference; classification depends on visibility, relation, tasking, legality and effect.","status":"PASS","support":"FCT-001,FCT-002,FCT-003,FCT-004"}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Offered 50/50 cofunding for public-diplomacy projects under a contract-like RFP with selection criteria, milestones, documented expenses and performance reports.","actor":"Ministry of Diaspora Affairs and Combating Antisemitism / Voices of Israel","intent":"PROVEN","status":"DONE","support":["FCT-002","FCT-003","FCT-004","FCT-005","FCT-006"]}
ACT-002 | {"action":"Operated as a funder/accelerator for pro-Israel nonprofits and sought greater coordination between government and civil-society advocacy ecosystems.","actor":"Voices of Israel","intent":"PROVEN","status":"DONE","support":["FCT-007","FCT-008","FCT-009"]}
ACT-003 | {"action":"Organized delegations, conferences and missions exposing French/European decision-makers and opinion actors to Israeli officials, security institutions and policy requests.","actor":"ELNET France / ELNET Europe ecosystem","intent":"PROVEN","status":"DONE","support":["FCT-010","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016"]}
ACT-004 | {"action":"Did not expose a France/EU recipient-by-recipient Voices award ledger or project contract tying a specific Voices payment to a named French policy intervention.","actor":"Publicly inspectable corpus","intent":"N/A","status":"DONE","support":["FCT-010","FCT-011"]}

SEARCH_ACTIVITY_V1:WEB:24|FETCH:6|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | UNAVAILABLE | MNEMO | MNEMO_UNAVAILABLE | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | DISCOVERY_RESULTS | - | - | site:gov.il Voices of Israel 45 million 56 organizations 2024 antisemitism report
QRY-002 | WEB | DISCOVERY_RESULTS | - | - | site:gov.il Voices of Israel nonprofit grants 2024 organizations Europe France
QRY-003 | WEB | DISCOVERY_RESULTS | - | - | site:knesset.gov.il public diplomacy budget 1.2 billion NIS 2026 civil society organizations
QRY-004 | WEB | DISCOVERY_RESULTS | - | - | site:gov.il Ministry Diaspora Affairs Voices of Israel Maccabi World Union 50 million 2025 ecosystem organizations diaspora
QRY-005 | WEB | DISCOVERY_RESULTS | - | - | site:mr.gov.il Voices of Israel France ELNET grant Israel Ministry 2024 2025
QRY-006 | WEB | DISCOVERY_RESULTS | - | - | site:gov.il "Voices of Israel" France Europe organizations grants
QRY-007 | WEB | DISCOVERY_RESULTS | - | - | "45 million" "Voices of Israel" 56 organizations
QRY-008 | WEB | DISCOVERY_RESULTS | - | - | "50 million" "Maccabi World Union" public diplomacy Israel 2025
QRY-009 | WEB | DISCOVERY_RESULTS | - | - | "Voices of Israel" "56" organizations
QRY-010 | WEB | DISCOVERY_RESULTS | - | - | "Voices of Israel" France Europe grant recipients
QRY-011 | WEB | DISCOVERY_RESULTS | - | - | "Voices of Israel" ELNET funding amount Europe
QRY-012 | WEB | DISCOVERY_RESULTS | - | - | "Voices of Israel" ELNET grant Europe decision makers
QRY-013 | WEB | DISCOVERY_RESULTS | - | - | "Voices of Israel" "ELNET" "France"
QRY-014 | WEB | DISCOVERY_RESULTS | - | - | "Voices of Israel" "European decision makers" ELNET
QRY-015 | WEB | DISCOVERY_RESULTS | - | - | site:voicesofisrael.org ELNET Europe decision makers
QRY-016 | WEB | DISCOVERY_RESULTS | - | - | site:gov.il ELNET Voices of Israel Europe 2024
QRY-017 | WEB | DISCOVERY_RESULTS | - | - | "45 million NIS" "56 organizations" site:gov.il OR site:knesset.gov.il
QRY-018 | WEB | DISCOVERY_RESULTS | - | - | "12 million NIS" "62 projects" site:gov.il OR site:knesset.gov.il
QRY-019 | WEB | DISCOVERY_RESULTS | - | - | "50,000,000 NIS" "Maccabi World Union" site:gov.il OR site:knesset.gov.il
QRY-020 | WEB | DISCOVERY_RESULTS | - | - | "Voices of Israel" site:main.knesset.gov.il
QRY-021 | WEB | DISCOVERY_RESULTS | - | - | "February 29 2024" ELNET delegation France Latvia Estonia Lithuania Knesset
QRY-022 | WEB | DISCOVERY_RESULTS | - | - | site:elnetwork.eu February 2024 delegation France ELNET Knesset
QRY-023 | WEB | DISCOVERY_RESULTS | - | - | site:elnetwork.eu France ELNET delegation Knesset 2024
QRY-024 | WEB | DISCOVERY_RESULTS | - | - | "ELNET" "France" "delegation" "Knesset" 2024
QRY-025 | FETCH | INSPECTED | SRC-001 | https://voicesofisrael.org/wp-content/uploads/2023/11/RFP-Swords-of-Iron-21.11.23-1.pdf | -
QRY-026 | FETCH | INSPECTED | SRC-002 | https://www.jpost.com/israel-news/article-713678 | -
QRY-027 | FETCH | INSPECTED | SRC-003 | https://taz.de/Lobbyorganisation-Elnet/!6130001/ | -
QRY-028 | FETCH | INSPECTED | SRC-004 | https://elnetwork.fr/delegation/delegation-de-22-senateurs-et-ecrivains-francais-en-israel-janvier-2024/amp/ | -
QRY-029 | FETCH | INSPECTED | SRC-005 | https://elnetwork.eu/country/israel/mk-shelly-tal-meron-visits-germany-and-france-meets-with-officials-to-discuss-october-7/ | -
QRY-030 | FETCH | INSPECTED | SRC-006 | https://elnetwork.fr/delegation/delegation-conjointe-dexperts-militaires-delnet-2025/ | -

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:other:voices_israel | voi:rfp:2023-11-21 | Voices of Israel — Emergency Fund Winning the War on Narrative RFP | 2023-11-21 | 2026-09-13 | pp1-3; joint venture, axes, 50/50 funding, milestones, performance reports | https://voicesofisrael.org/wp-content/uploads/2023/11/RFP-Swords-of-Iron-21.11.23-1.pdf
SRC-002 | ◉ | fam:other:jpost | jpost:713678 | Jerusalem Post — Israel Foreign Ministry launches re-branded hasbara org | 2022-08-01 | 2026-09-13 | VoI government-philanthropic structure, budget, funding/accelerator model, coordination intent | https://www.jpost.com/israel-news/article-713678
SRC-003 | ◉ | fam:other:taz | taz:6130001 | taz — Lobbyorganisation Elnet: Meinungsbildungsreisen nach Israel | 2025-11-29 | 2026-09-13 | lines 153-181; VoI lists ELNET as selected project for European decision makers; exact VoI expenditure undisclosed | https://taz.de/Lobbyorganisation-Elnet/!6130001/
SRC-004 | ◈ | fam:other:elnet | elnet-fr:delegation:2024-01 | ELNET France — délégation de 22 sénateurs et écrivains français, janvier 2024 | 2024-01-10 | 2026-09-13 | mission purpose, participants, briefings, explicit requests to French MPs and support objectives | https://elnetwork.fr/delegation/delegation-de-22-senateurs-et-ecrivains-francais-en-israel-janvier-2024/amp/
SRC-005 | ◈ | fam:other:elnet | elnet:tal-meron:2024-03 | ELNET — Shelly Tal Meron visits Germany and France | 2024-03-07 | 2026-09-13 | ELNET Germany/France-hosted mission; objective to raise awareness; meetings with public officials | https://elnetwork.eu/country/israel/mk-shelly-tal-meron-visits-germany-and-france-meets-with-officials-to-discuss-october-7/
SRC-006 | ◈ | fam:other:elnet | elnet-fr:defense-delegation:2025 | ELNET France — délégation conjointe d’experts militaires 2025 | 2025-03-31 | 2026-09-13 | 27 defence officials/experts including France; Israeli MFA/Knesset/security briefings | https://elnetwork.fr/delegation/delegation-conjointe-dexperts-militaires-delnet-2025/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://voicesofisrael.org/wp-content/uploads/2023/11/RFP-Swords-of-Iron-21.11.23-1.pdf | other:voices_israel | 2023-11-21 | Voices of Israel public benefit company purpose | The emergency RFP states that Voices of Israel is a Public Benefit Company whose goal is to strengthen Israel position internationally and fight delegitimization and antisemitism through public-diplomacy tools. | -
FCT-002 | FACT | ✧ | https://voicesofisrael.org/wp-content/uploads/2023/11/RFP-Swords-of-Iron-21.11.23-1.pdf | other:voices_israel | 2023-11-21 | Voices of Israel government joint venture funding source | The RFP states that Voices of Israel operates under a government decision establishing a joint venture and that its project-funding share is based on funding from the Ministry of Diaspora Affairs and Combatting Antisemitism. | -
FCT-003 | FACT | ✧ | https://voicesofisrael.org/wp-content/uploads/2023/11/RFP-Swords-of-Iron-21.11.23-1.pdf | other:voices_israel | 2023-11-21 | Voices of Israel emergency RFP action axes | The RFP solicits media, digital, public and other initiatives to strengthen the Israeli narrative and increase global support for and identification with Israel. | -
FCT-004 | FACT | ✧ | https://voicesofisrael.org/wp-content/uploads/2023/11/RFP-Swords-of-Iron-21.11.23-1.pdf | other:voices_israel | 2023-11-21 | Voices of Israel 50-50 project financing rule | The emergency RFP provides that the Ministry/VoI contribution is 50 percent and the bidder share 50 percent, with a minimum total proposed project budget of NIS 50,000. | -
FCT-005 | FACT | ✧ | https://voicesofisrael.org/wp-content/uploads/2023/11/RFP-Swords-of-Iron-21.11.23-1.pdf | other:voices_israel | 2023-11-21 | Voices of Israel milestone and performance-report payment rule | The RFP states that payments follow implemented project milestones, documented expenses, submission of performance reports, Voices approval and receipt of State funding. | -
FCT-006 | FACT | ✧ | https://voicesofisrael.org/wp-content/uploads/2023/11/RFP-Swords-of-Iron-21.11.23-1.pdf | other:voices_israel | 2023-11-21 | Voices of Israel project selection criteria | The RFP ranks proposals by alignment with action axes, bidder experience, plan quality, immediate execution, financial compliance and the ratio between financial investment and expected result. | -
FCT-007 | FACT | ✧ | https://www.jpost.com/israel-news/article-713678 | other:jpost | 2022-08-01 | Voices of Israel government-philanthropic budget model | Jerusalem Post reported that Voices of Israel was structured around NIS 100 million of public funding over four years with matching private funds potentially taking the envelope to NIS 200 million. | -
FCT-008 | FACT | ✧ | https://www.jpost.com/israel-news/article-713678 | other:jpost | 2022-08-01 | Voices of Israel funder and accelerator role | Voices leadership described the entity as a funder and accelerator intended to resource pro-Israel nonprofits and to make government/pro-Israel-world coordination more organized. | -
FCT-009 | FACT | ✧ | https://www.jpost.com/israel-news/article-713678 | other:jpost | 2022-08-01 | Voices of Israel annual funding ambition in 2022 | Voices chair Micah Avni stated in 2022 that the organization was looking to deploy NIS 30-40 million in funding that year. | -
FCT-010 | FACT | ✧ | https://taz.de/Lobbyorganisation-Elnet/!6130001/ | other:taz | 2025-11-29 | ELNET listed as selected Voices of Israel project | taz reports that the Voices of Israel website listed ELNET among selected projects under the description delegations and conferences for European decision-makers. | -
FCT-011 | FACT | ✧ | https://taz.de/Lobbyorganisation-Elnet/!6130001/ | other:taz | 2025-11-29 | Voices of Israel expenditure allocated to ELNET not disclosed | taz reports that exact Voices of Israel expenditures for the ELNET selected-project relationship were not publicly disclosed in the inspected corpus. | -
FCT-012 | FACT | ✧ | https://taz.de/Lobbyorganisation-Elnet/!6130001/ | other:taz | 2025-11-29 | ELNET European decision-maker travel scale | taz reports that ELNET Tel Aviv staff coordinate travel programs bringing up to roughly 300 European decision-makers to Israel annually and had reviewed ten itineraries from five years. | -
FCT-013 | FACT | ✧ | https://elnetwork.fr/delegation/delegation-de-22-senateurs-et-ecrivains-francais-en-israel-janvier-2024/amp/ | other:elnet | 2024-01-10 | ELNET France January 2024 solidarity delegation composition and purpose | ELNET France states that its January 2024 mission gathered 21 participants including senators, MPs, writers and novelists, with a stated aim of inviting influential writers and journalists to see the situation and report to peers. | -
FCT-014 | FACT | ✧ | https://elnetwork.fr/delegation/delegation-de-22-senateurs-et-ecrivains-francais-en-israel-janvier-2024/amp/ | other:elnet | 2024-01-10 | ELNET France delegation official briefings and policy asks | ELNET France describes briefings and meetings with Israeli police, IDF, Knesset members, MFA officials and the Knesset speaker, alongside explicit requests for French support in international institutions and on several policy questions. | -
FCT-015 | FACT | ✧ | https://elnetwork.eu/country/israel/mk-shelly-tal-meron-visits-germany-and-france-meets-with-officials-to-discuss-october-7/ | other:elnet | 2024-03-07 | ELNET Germany and France hosted Israeli MK awareness mission | ELNET states that its Germany and France branches hosted MK Shelly Tal Meron in February 2024 on a mission explicitly aimed at raising awareness about October 7 and gender-based crimes through high-level meetings. | -
FCT-016 | FACT | ✧ | https://elnetwork.fr/delegation/delegation-conjointe-dexperts-militaires-delnet-2025/ | other:elnet | 2025-03-31 | ELNET 2025 defence delegation involving France | ELNET France reports a 27-person delegation of senior defence officials, military strategists, security experts and advisers including participants from France and several European states, with briefings by Israeli officials and security actors. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-001
FCT-005 | SRC-001
FCT-006 | SRC-001
FCT-007 | SRC-002
FCT-008 | SRC-002
FCT-009 | SRC-002
FCT-010 | SRC-003
FCT-011 | SRC-003
FCT-012 | SRC-003
FCT-013 | SRC-004
FCT-014 | SRC-004
FCT-015 | SRC-005
FCT-016 | SRC-006

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
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:Lock funding/recipient/deliverable scope
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:Normalize inspected sources and facts
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:Normalize facts and test causal/tasking chains
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:Test public-funding-to-recipient-to-deliverable chains, France/EU allocation and tasking ceilings
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:Verify funding/tasking/recipient claims and causal ceiling
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:Build accountability, contradictions, impact and final narrative
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:Freeze technical narrative, normalize sections and run final gates

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-13T11:54:26.740450+00:00","fact_mem":{},"mnemo_row":"MNEMO_UNAVAILABLE — local memory service unavailable in this runtime; no memory ids fabricated.","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":16,"eligible":16,"failure":0,"success":0}}

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
