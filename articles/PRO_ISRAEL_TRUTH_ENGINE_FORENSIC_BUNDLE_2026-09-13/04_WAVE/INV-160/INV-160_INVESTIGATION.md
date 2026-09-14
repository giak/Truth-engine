ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260913-1303-elnet-finance-topology | PARENT_RUN_ID:NONE | AS_OF:2026-09-13
INPUT_KIND:RUN_CARD | MISSION_MODE:DEEPEN | INPUT_REF:PATH:/mnt/data/inv160_work/runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-13_elnet-finance-topology/2026-09-13_13-03_elnet-finance-topology_INPUT.md | SUBJECT_SLUG:elnet-finance-topology | SUBJECT_FP:sha256:831e023544619f1876558d4003675cd219b1e350685c0f3e7caaa5ef20787c00 | INPUT_SHA256:sha256:854710940786dd89ef7c88c04ec261e6a0b6336287b1440f52234a39a298b758
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:US/Israel/France/EU financial topology of ELNET, mainly 2019-2026; trace donor/foundation -> Friends of ELNET -> foreign entity/program -> France/EU activity; include Israeli public procurement and French HATVP spend; separate general support, restricted grant, procurement/tasking and downstream lobbying effect.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/MONEY.md,clusters/NETWORK.md,clusters/POWER.md,clusters/ICEBERG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-160 — ELNET : topologie financière transnationale US–Israël–France/UE

## Objet

Reconstruire les flux financiers publiquement documentables autour du réseau ELNET et déterminer jusqu'où ces flux permettent d'établir ressource, restriction, allocation, tasking et effet dans les activités françaises ou européennes. Le run sépare systématiquement financement général, grant restreint, transfert entre entités, commande publique, lobbying déclaré et causalité politique.

## Résultat central

**FACT.** Friends of ELNET constitue un hub financier américain significatif. Son Form 990 2024 déclare 8,955 M$ de recettes, dont 8,680 M$ de contributions, et 5,926 M$ de grants versés à huit entités ELNET hors des États-Unis (FCT-005, FCT-006, FCT-008). La somme des huit lignes du Schedule F réconcilie exactement le total de 5,926 M$.

**FACT.** La plus grosse ligne du Schedule F est `ELNET, France` : 1,034 M$ en 2024 (FCT-007). Le Schedule O indique que les grants étrangers financent l'éducation de dirigeants européens, séminaires, débats publics, newsletters, conférences et colloques, ainsi que des visites et voyages d'étude en Israël et des échanges numériques (FCT-009).

**FACT.** ELNET France déclare parallèlement auprès de la HATVP une activité de représentation d'intérêts menée `en propre`, avec 100 000 à 200 000 euros de dépenses dédiées et trois ETP en 2023, 2024 et 2025 (FCT-001, FCT-002). Des fiches déclarent explicitement l'envoi de suggestions pour influencer la rédaction de décisions publiques et plusieurs objectifs législatifs, réglementaires et diplomatiques (FCT-003, FCT-016).

**INFERENCE BORNÉE.** Ces deux ensembles ferment `financement transnational -> capacité d'une entité française ayant une activité de lobbying`, mais ils ne ferment pas `dollar reçu -> action HATVP précise`. Le grant américain mesure un transfert organisationnel total, tandis que le montant HATVP mesure une catégorie réglementaire plus étroite de moyens consacrés à la représentation d'intérêts (FCT-004). Le différentiel ne peut donc pas être qualifié de lobbying dissimulé ou non déclaré sans comptabilité projet et règles d'affectation.

## Flux amont

**FACT.** Les financements amont ne sont pas tous nécessairement sans condition. Un Form 990-PF de la William Davidson Foundation précise pour Friends of ELNET un soutien au bureau de Bruxelles et à la création de programmes de haut niveau pour des délégations en Israël (FCT-015). Cette pièce ferme l'existence d'au moins un grant programmatique restreint dans l'histoire du financement.

**LIMIT.** Ce cas ne permet pas d'attribuer une instruction politique française au donateur. Le niveau de fermeture est `donor -> ressource/programme`, pas `donor -> position française nommée`.

## Flux vers les affiliés

Le Schedule F 2024 distribue les 5,926 M$ entre Bruxelles, France, Allemagne, Global, Israël, Italie, Pologne et Royaume-Uni (FCT-008). Le modèle empirique est donc celui d'un hub américain finançant plusieurs composantes internationales. Cette architecture est compatible avec une coordination de ressources et une mission commune, mais ne suffit pas à établir une chaîne de commandement unifiée.

Le Form 990 américain répond par ailleurs `No` à la question IRS sur les activités de lobbying de l'entité américaine (FCT-011). Ce point constitue un contrôle de catégorie : il concerne la qualification fiscale américaine de Friends of ELNET et ne contredit pas l'activité de lobbying légalement déclarée par ELNET France dans une autre juridiction.

## Arête étatique israélienne

**FACT.** Une relation financière étatique spécifique est directement documentée. Le ministère israélien des Affaires étrangères publie une exemption de fournisseur unique de 72 000 euros au bénéfice d'ELNET Europe-Israel, pour une opération liée à un événement au Sénat français le 10 novembre 2025 (FCT-013, FCT-014).

Cette transaction ferme `État israélien -> commande/financement spécifique -> entité ELNET -> événement institutionnel français`. Elle ne ferme ni `État israélien -> commandement général d'ELNET France`, ni `événement -> décision française causée`.

## Ce que le corpus ne permet pas d'établir

Le corpus public inspecté ne contient pas :

- le budget analytique d'ELNET France ventilant le grant américain par projet ;
- les conventions complètes de grant 2024 entre Friends of ELNET et ELNET France ;
- un ledger reliant le million de dollars reçu à une fiche HATVP nommée ;
- une instruction d'un donateur américain imposant une position politique française précise ;
- une instruction générale du gouvernement israélien contrôlant ELNET France ;
- un design causal reliant ces flux à une décision publique française contrefactuelle.

Ces absences sont des gaps de causalité/allocation. Elles ne valent ni preuve d'autonomie complète, ni preuve de tasking caché.

## Conclusion bornée

INV-160 ferme une topologie financière plus précise que le corpus antérieur : `donateurs américains -> Friends of ELNET -> affiliés étrangers`, avec un transfert 2024 de 1,034 M$ à ELNET France et un usage programmatique déclaré centré notamment sur la formation, les événements et les voyages de dirigeants européens. Il ferme aussi une arête différente et plus forte de tasking : `MFA israélien -> 72 000 € -> ELNET Europe-Israel -> événement au Sénat`, mais uniquement pour cette transaction.

Le saut vers `financement -> commandement général -> politique française causée` reste non établi. Le prochain gain probatoire ne viendra pas d'une nouvelle liste de financeurs, mais des conventions de grants, comptes analytiques, livrables contractuels et empreintes de décision permettant de relier une ressource à une action puis à un effet.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:4|EDI_DECISIVE:3|SRC_COMPLETE:6/6

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **status:** BOUNDED
- **timeline:**
  - 2019 WDF restricted Friends grant for Brussels office/delegations
  - 2021-2025 HATVP French lobbying spend consistently EUR 100k-200k
  - 2024 Friends grant USD 1.034m to ELNET France and USD 5.926m to eight foreign ELNET entities
  - 2025 Israeli MFA EUR 72k ELNET Europe-Israel procurement for French Senate event
  - 2025 Friends donor financing remains large per FY2025 IRS-derived data

### MANIPULATION_REPORT
- **assumptions:**
  - IRS Schedule F recipient label ELNET, France identifies the French affiliate but does not expose internal project allocation
  - HATVP expenditure measures lobbying-specific means and is not total organization expenditure
  - procurement notice is authoritative for transaction fields but not downstream political effect
- **clusters:**
  - MONEY
  - NETWORK
  - POWER
  - ICEBERG
- **complexity:**
  - **band:** HIGH
  - **score:** 9
- **implicit:**
  - **I01:** large grant may fund mixed program/lobbying/non-lobbying activity
  - **I02:** program restriction may stop above downstream policy action
  - **I03:** federated affiliates can share mission without command
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - **P01:** donor -> US hub -> foreign affiliate
  - **P02:** affiliate resource -> access/program capacity
  - **P03:** state procurement -> specific task
  - **P04:** accounting-category mismatch -> false hidden-spend inference
- **priorities:**
  - close transnational money flow
  - separate general/restricted support
  - identify state-funded transaction
  - test France allocation/tasking
- **query_guidance:** prefer IRS primary schedules, official HATVP declarations and public procurement; do not infer tasking from mission alignment or grant receipt
- **rhetorical:**
  - **R01:** million-dollar grant equals million-dollar lobbying
  - **R02:** foreign grant equals foreign-agent relation
  - **R03:** specific state contract equals network control
  - **R04:** mission congruence equals causal policy effect
- **speaker:**
  - **goal:** forensic reconstruction of ELNET financial topology
  - **target:** donor -> hub -> affiliate -> France activity/tasking/effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** donor
  - **S02:** grant
  - **S03:** restriction
  - **S04:** US_hub
  - **S05:** affiliate
  - **S06:** France_grant
  - **S07:** lobbying_budget
  - **S08:** program_expense
  - **S09:** study_trip
  - **S10:** procurement
  - **S11:** state_funder
  - **S12:** tasking
  - **S13:** allocation_gap
  - **S14:** policy_footprint
  - **S15:** effect
- **threats:**
  - funding=command
  - grant=lobbying
  - network=coordination
  - foreign origin=state proxy
  - state procurement=general control
  - accounting mismatch=concealment

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - ALLOCATION
  - **input_ids:**
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-008
    - FCT-013
    - FCT-015
  - **module:** clusters/MONEY.md
  - **negative_results:**
    - no project-level France allocation ledger
  - **not_computable:**
    - share of USD 1.034m used for French lobbying
  - **operations_applied:**
    - resource-flow reconstruction
    - restriction versus general support
    - denominator/category check
  - **reason:** trace donor/grant/affiliate flows and category boundaries
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-006
    - CLM-007
    - CAU-001
    - CAU-003
  - **status:** DONE
  - **trigger:** €
- **item 2:**
  - **gaps:**
    - affiliate governance/agreements not inspected
  - **input_ids:**
    - FCT-007
    - FCT-008
    - FCT-001
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no general state-command edge
  - **not_computable:**
    - network-wide command probability
  - **operations_applied:**
    - entity separation
    - hub-to-affiliate map
  - **reason:** separate hub/affiliate relations from command
  - **result_ids:**
    - CLM-001
    - CLM-004
    - CAU-002
    - CTRL-001
  - **status:** DONE
  - **trigger:** 🌐
- **item 3:**
  - **gaps:**
    - CAUSALITY
  - **input_ids:**
    - FCT-003
    - FCT-009
    - FCT-013
    - FCT-014
    - FCT-016
  - **module:** clusters/POWER.md
  - **negative_results:**
    - policy causation not closed
  - **not_computable:**
    - marginal policy effect of foreign funding
  - **operations_applied:**
    - capacity/action/tasking separation
    - specific procurement edge
  - **reason:** test when resources become tasking/access/policy action
  - **result_ids:**
    - CLM-003
    - CLM-005
    - CLM-007
    - CAU-003
    - CAU-004
  - **status:** DONE
  - **trigger:** ↕
- **item 4:**
  - **gaps:**
    - French accounts/grant budget unavailable in inspected corpus
  - **input_ids:**
    - FCT-002
    - FCT-004
    - FCT-007
    - FCT-009
  - **module:** clusters/ICEBERG.md
  - **negative_results:**
    - grant-minus-lobbying residual cannot be labeled hidden lobbying
  - **not_computable:**
    - unreported lobbying amount
  - **operations_applied:**
    - category-trick test
    - denominator test
    - shadow-population search
  - **reason:** test hidden-spend inference, denominator manipulation and shadow allocation
  - **result_ids:**
    - CTRL-002
    - CLM-005
  - **status:** DONE
  - **trigger:** Ξ

### SCOPING_REPORT
- **classification_dimensions:**
  - legal entity
  - jurisdiction
  - source of funds
  - grant restriction
  - recipient
  - program purpose
  - French lobbying category
  - tasking
  - policy effect
- **exclusions:**
  - Jewish identity/state proxy inference
  - grant=command
  - general support=specific instruction
  - total grant=lobbying spend
  - procurement=network control
  - mission alignment=causality
- **scope:** US/Israel/France/EU, mainly 2019-2026; financial topology and downstream France allocation/tasking only
- **status:** ACTIVE

### CREDO
- funding != command
- grant != tasking
- affiliate network != unified principal
- total grant != lobbying expenditure
- own-account declaration != proof of zero foreign support
- specific procurement != general state control
- resource/capacity != policy outcome
- currency/category mismatch must not be treated as discrepancy

### COGNITIVE_MAP
- **chain:**
  - upstream donor
  - US fundraising hub
  - foreign affiliate grant
  - program/resource allocation
  - France lobbying action
  - public-decision input
  - policy outcome
- **core_model:** ELNET has a traceable transnational financial architecture: a US donor-funded hub distributes multimillion-dollar grants to European/Israeli affiliates, including more than USD 1 million to ELNET France in 2024; ELNET France separately reports a substantial own-account lobbying operation. Public evidence does not allocate the France grant to named lobbying actions. A distinct Israeli MFA procurement closes state funding/tasking for one French-Senate-linked project only.
- **rival_models:**
  - federated nonprofit network with affiliate autonomy
  - general operating support without donor tasking
  - program-restricted philanthropy without policy command
  - specific state procurement without general organizational control
  - accounting-category mismatch rather than hidden lobbying

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** The US filing proves a USD 1.034m grant to ELNET France, while HATVP proves a narrower lobbying budget; project-level allocation is absent.
  - **resolution:** Resource support is established; named lobbying-dollar attribution is an ALLOCATION_GAP.
  - **thesis:** Friends of ELNET finances the French lobbying operation directly and comprehensively.
- **item 2:**
  - **antithesis:** A specific MFA procurement exists, but HATVP records ELNET France lobbying in own account and the public corpus lacks general tasking records.
  - **resolution:** State-tasking is supported only for the specific procured operation, not generalized.
  - **thesis:** ELNET is an Israeli-government proxy.
- **item 3:**
  - **antithesis:** A primary foundation filing specifies Brussels-office and delegation programming, and Friends Schedule O specifies leader-education/trip purposes.
  - **resolution:** Some program restrictions are real; donor-to-policy tasking remains unestablished.
  - **thesis:** Donors merely give unrestricted charity with no program direction.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **from:** Private foundations/donors
  - **limits:**
    - donor restrictions do not establish downstream policy tasking
  - **resource:** charitable grants, some general and some program-restricted
  - **support:**
    - FCT-015
    - FCT-005
    - FCT-006
    - FCT-008
  - **to:** ELNET foreign affiliates
  - **via:** Friends of ELNET US
- **item 2:**
  - **from:** Friends of ELNET US
  - **limits:**
    - specific internal allocation unavailable
  - **resource:** USD 1,034,210 cash grant in 2024
  - **support:**
    - FCT-007
    - FCT-009
  - **to:** France affiliate programs/capacity
  - **via:** ELNET France
- **item 3:**
  - **from:** ELNET France
  - **limits:**
    - foreign-grant share of lobbying spend unknown
  - **resource:** declared EUR 100k-200k lobbying means and 3 FTE
  - **support:**
    - FCT-002
    - FCT-003
    - FCT-016
  - **to:** French public authorities
  - **via:** meetings/events/suggestions/correspondence
- **item 4:**
  - **from:** Israeli Ministry of Foreign Affairs
  - **limits:**
    - transaction-specific; no generalization to ELNET France/network control
  - **resource:** EUR 72,000 procurement
  - **support:**
    - FCT-013
    - FCT-014
  - **to:** French Senate event 10 Nov 2025
  - **via:** ELNET Europe-Israel

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** Private US foundations/donors
  - **relation:** grants/general or program support
  - **support:**
    - FCT-015
  - **to:** Friends of ELNET US
- **item 2:**
  - **from:** Friends of ELNET US
  - **relation:** foreign cash grants
  - **support:**
    - FCT-006
    - FCT-007
    - FCT-008
  - **to:** ELNET France and seven other foreign ELNET entities
- **item 3:**
  - **from:** ELNET France
  - **relation:** declared own-account interest representation
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
    - FCT-016
  - **to:** French public authorities/parliament
- **item 4:**
  - **from:** Israeli Ministry of Foreign Affairs
  - **relation:** specific sole-supplier procurement
  - **support:**
    - FCT-013
    - FCT-014
  - **to:** ELNET Europe-Israel / French Senate event

### IMPACT_MAP
- **affected:**
  - ELNET France organizational capacity
  - European-leader programming
  - French public-authority access environment
- **benefits:**
  - substantial resources for European affiliate programs, events, trips and organizational activity
- **costs_harms:**
  - potential sponsored-access asymmetry is structurally plausible; corruption/capture/policy harm is not established by finance data
- **response_change:** Public records establish capacity and specific project funding; downstream decision effect remains unmeasured in this run.
- **status:** BOUNDED

### CONTRADICTION_LEDGER
- **item 1:**
  - **claim:** USD 1.034m France grant versus EUR 100k-200k HATVP spend proves undeclared lobbying
  - **counter:** Schedule F measures total grant; HATVP measures lobbying-specific expenditure under a different regulatory category. No common denominator.
  - **status:** REFUTED_AS_INFERENCE
- **item 2:**
  - **claim:** foreign funding proves ELNET France acts for a foreign principal
  - **counter:** HATVP declares activities in own account; direct project-level tasking must be shown separately.
  - **status:** NOT_ESTABLISHED_GENERAL
- **item 3:**
  - **claim:** Israeli MFA funding proves network-wide state control
  - **counter:** official evidence is transaction-specific to a EUR 72k ELNET Europe-Israel event.
  - **status:** NOT_ESTABLISHED_GENERAL
- **item 4:**
  - **claim:** US donor restrictions prove specific French policy tasking
  - **counter:** historical WDF restriction concerns Brussels office/delegations; no named French policy instruction.
  - **status:** NOT_ESTABLISHED

### VERIFICATION_REPORT
- **fact_count:** 16
- **limitations:**
  - no ELNET France detailed accounts/grant allocation
  - no complete current donor-purpose census
  - procurement attachments unavailable on portal
  - no decision-level causal design in this run
- **primary_records:**
  - HATVP ELNET France
  - HATVP lobbying methodology
  - Friends of ELNET Form 990/Schedules
  - Israeli MFA procurement
  - William Davidson Foundation 990-PF
- **query_count:** 15
- **secondary_index:**
  - ProPublica Nonprofit Explorer
- **source_count:** 6
- **status:** PASS_BOUNDED

### EDI_REPORT
- **corpus:** 6 accepted inspected sources; 16 normalized facts; IRS primary filings, French HATVP records, Israeli procurement notice, and one IRS-derived index
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim:** CLM-001
    - **families:**
      - other:irs
  - **item 2:**
    - **claim:** CLM-004
    - **families:**
      - other:hatvp
  - **item 3:**
    - **claim:** CLM-007
    - **families:**
      - other:israel_mfa
- **diagnostic_not_truth:** true
- **dimensions:**
  - upstream donor restrictions
  - US hub finances
  - affiliate transfers
  - France lobbying means
  - state procurement
  - allocation/tasking
  - policy effect
- **edi:** PRIMARY_FINANCIAL_RECORDS_CLOSE_RESOURCE_FLOWS_BUT_PROJECT_LEVEL_FRANCE_ALLOCATION_REMAINS_GAP
- **source_counts:**
  - **other:hatvp:** 2
  - **other:irs:** 2
  - **other:irs_foundation:** 1
  - **other:israel_mfa:** 1

### RESPONSIBILITY_MAP
- **item 1:**
  - **actor:** Friends of ELNET US
  - **responsibility:** fundraising and foreign affiliate grant distribution
  - **status:** SUPPORTED
  - **support:**
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-008
    - FCT-009
- **item 2:**
  - **actor:** ELNET France
  - **responsibility:** declared French lobbying activities in own account
  - **status:** SUPPORTED
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
    - FCT-016
- **item 3:**
  - **actor:** Israeli MFA
  - **responsibility:** specific EUR 72k ELNET Europe-Israel procurement
  - **status:** SUPPORTED_CASE_SPECIFIC
  - **support:**
    - FCT-013
    - FCT-014
- **item 4:**
  - **actor:** upstream private donors
  - **responsibility:** some general/program-restricted grants to US hub
  - **status:** SUPPORTED_BOUNDED
  - **support:**
    - FCT-015
- **item 5:**
  - **actor:** any funder
  - **responsibility:** tasking a named French lobbying position or policy outcome
  - **status:** NOT_ESTABLISHED
  - **support:**
    - CLM-005
    - CAU-004

### NEXT_QUERIES
- Obtain ELNET France statutory accounts and grant-restriction/budget documents for 2024.
- Inspect Friends of ELNET 2025 Schedule F when primary filing is available and compare affiliate distributions longitudinally.
- Retrieve additional donor 990-PF grant-purpose entries to classify general versus restricted funding.
- For the EUR 72k MFA procurement, retrieve committee protocol/contract deliverables if accessible and map outputs/participants.

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-012,QRY-013 | support:- | counter:- | results:FCT-005,FCT-006,FCT-007,FCT-008,FCT-009 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-010,QRY-011,QRY-012 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-007 | final:SATURATED | gap:NONE
LED-003 | attempts:QRY-014 | support:- | counter:- | results:FCT-012,FCT-013 | final:SATURATED | gap:NONE
LED-004 | attempts:QRY-001,QRY-002,QRY-006,QRY-007,QRY-008,QRY-015 | support:- | counter:- | results:FCT-014 | final:SATURATED | gap:NONE
LED-005 | attempts:QRY-010,QRY-011,QRY-012 | support:- | counter:- | results:FCT-007,FCT-009,FCT-001,FCT-003 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-015 | support:- | counter:- | results:FCT-014 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-012,QRY-013 | support:- | counter:- | results:FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-010,QRY-011,QRY-012 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-007,FCT-009 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-014 | support:- | counter:- | results:FCT-012,FCT-013 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-012,QRY-013 | support:FCT-005,FCT-006,FCT-008,FCT-010 | counter:The filing establishes transfers and stated program purpose,not control over every downstream action. | results:FCT-005,FCT-006,FCT-008,FCT-010 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-012 | support:FCT-007 | counter:The public Schedule F does not break this grant into French lobbying versus other programs,trips,events or overhead. | results:FCT-007 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-012 | support:FCT-009 | counter:A broad program-purpose statement does not identify which affiliate dollar financed which named event or policy intervention. | results:FCT-009 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-010,QRY-011 | support:FCT-001,FCT-002,FCT-003,FCT-016 | counter:Own-account registration under HATVP does not establish that no foreign grants support the organization; conversely foreign funding does not make every activity foreign-tasked. | results:FCT-001,FCT-002,FCT-003,FCT-016 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-010,QRY-011,QRY-012 | support:FCT-001,FCT-002,FCT-004,FCT-007,FCT-009 | counter:The broad grant purpose overlaps with some influence activities,so absence of allocation data is not proof of functional separation. | results:FCT-001,FCT-002,FCT-004,FCT-007,FCT-009 | final:GAP | gap:CAUSALITY
CLM-006 | attempts:QRY-001,QRY-002,QRY-006,QRY-007,QRY-008,QRY-015 | support:FCT-015 | counter:This 2019 William Davidson Foundation grant does not prove restrictions on all donors or downstream French policy tasking. | results:FCT-015 | final:SUPPORTED | gap:NONE
CLM-007 | attempts:QRY-014 | support:FCT-013,FCT-014 | counter:A specific public procurement closes state funding/tasking for that project only; it does not establish general Israeli-state command of ELNET France or the network. | results:FCT-013,FCT-014 | final:SUPPORTED | gap:NONE

## STATUS_DELTA_V1
DELTA-001 | CAU-002 | PARTIAL | GAP | Allocation edge remains causally unresolved; normalize terminal status/gap

## OPEN_GAPS_V1
CLM-005 | CLM | GAP | CAUSALITY | Need ELNET France accounts, grant agreement/budget, restricted-fund ledger or project-level expenditure mapping to connect foreign grant dollars to named HATVP actions.
CAU-002 | CAU | GAP | CAUSALITY | Need restricted-fund terms, French accounts and project-level cost allocation to attribute Friends of ELNET grant dollars to named ELNET France lobbying actions.
CAU-004 | CAU | GAP | CAUSALITY | Grant agreements/ledgers/instructions and policy-footprint evidence required.

SEMANTIC_COUNTS_V1:LED:5|CLM:7|AXS:4|CAU:4|CTRL:6|ACT:4

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-012","QRY-013"],"evidence_excerpt":"Need donor -> US hub -> affiliate amounts and stated grant purposes.","kind":"DATA_LEAD","lead":"Friends of ELNET upstream revenue and foreign grant distribution","linked_ids":["AXS-001","AXS-002"],"locator":"2024 Form 990 + Schedule F/O","materiality":"DECISIVE","result_ids":["FCT-005","FCT-006","FCT-007","FCT-008","FCT-009"],"routes":["EXPAND","LINK"],"source_id":"SRC-003","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-010","QRY-011","QRY-012"],"evidence_excerpt":"Test category/denominator mismatch without treating the residual as hidden lobbying.","kind":"DATA_LEAD","lead":"ELNET France declared lobbying means versus total foreign grant received","linked_ids":["AXS-002","AXS-003"],"locator":"HATVP means/actions","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-007"],"routes":["EXPAND","LINK"],"source_id":"SRC-001","status":"SATURATED"}
LED-003 | {"attempt_ids":["QRY-014"],"evidence_excerpt":"Specific state-funded project can close tasking for one operation but not general organization control.","kind":"RELATION_LEAD","lead":"Israeli state procurement to ELNET Europe-Israel for a French Senate event","linked_ids":["AXS-004"],"locator":"Procurement notice 4000606739","materiality":"DECISIVE","result_ids":["FCT-012","FCT-013"],"routes":["EXPAND","LINK"],"source_id":"SRC-005","status":"SATURATED"}
LED-004 | {"attempt_ids":["QRY-001","QRY-002","QRY-006","QRY-007","QRY-008","QRY-015"],"evidence_excerpt":"At least one primary donor filing specifies Brussels-office and Israel-delegation programming.","kind":"FUNDING_LEAD","lead":"Private-foundation restrictions upstream of Friends of ELNET","linked_ids":["AXS-001"],"locator":"William Davidson Foundation 990-PF Part XV p31","materiality":"IMPORTANT","result_ids":["FCT-014"],"routes":["EXPAND","CONTEXT"],"source_id":"SRC-006","status":"SATURATED"}
LED-005 | {"attempt_ids":["QRY-010","QRY-011","QRY-012"],"evidence_excerpt":"Public sources do not expose a ledger mapping each dollar/euro to a specific HATVP action or decision.","kind":"GAP_LEAD","lead":"Allocation from foreign grants to named French lobbying actions or policy outputs","linked_ids":["AXS-003","AXS-004"],"locator":"Schedule F/O versus HATVP activity sheets","materiality":"DECISIVE","result_ids":["FCT-007","FCT-009","FCT-001","FCT-003"],"routes":["EXPAND","LINK"],"source_id":"SRC-003","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"attempt_ids":["QRY-012","QRY-013"],"claim":"Friends of ELNET functions as a US fundraising/grantmaking hub that transferred USD 5.926 million in 2024 to eight foreign ELNET entities.","claimant":"INV-160","counter":"The filing establishes transfers and stated program purpose, not control over every downstream action.","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","result_ids":["FCT-005","FCT-006","FCT-008","FCT-010"],"status":"SUPPORTED","support":"FCT-005,FCT-006,FCT-008,FCT-010"}
CLM-002 | {"attempt_ids":["QRY-012"],"claim":"ELNET France received USD 1,034,210 from Friends of ELNET in 2024.","claimant":"INV-160","counter":"The public Schedule F does not break this grant into French lobbying versus other programs, trips, events or overhead.","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","result_ids":["FCT-007"],"status":"SUPPORTED","support":"FCT-007"}
CLM-003 | {"attempt_ids":["QRY-012"],"claim":"Friends of ELNET foreign grants are explicitly described as supporting European-leader education, seminars/debates/colloquia, Israel visits/study trips and digital exchange.","claimant":"INV-160","counter":"A broad program-purpose statement does not identify which affiliate dollar financed which named event or policy intervention.","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","result_ids":["FCT-009"],"status":"SUPPORTED","support":"FCT-009"}
CLM-004 | {"attempt_ids":["QRY-010","QRY-011"],"claim":"ELNET France has a declared French lobbying operation with EUR 100k-200k annual interest-representation expenditure and 3 FTE in 2023-2025, and declares activity for its own account.","claimant":"INV-160","counter":"Own-account registration under HATVP does not establish that no foreign grants support the organization; conversely foreign funding does not make every activity foreign-tasked.","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-016"],"status":"SUPPORTED","support":"FCT-001,FCT-002,FCT-003,FCT-016"}
CLM-005 | {"attempt_ids":["QRY-010","QRY-011","QRY-012"],"claim":"The public corpus does not establish a dollar/euro-level allocation from the USD 1.034m Friends of ELNET grant to named HATVP lobbying actions, nor donor tasking of a specific French policy position.","claimant":"INV-160","counter":"The broad grant purpose overlaps with some influence activities, so absence of allocation data is not proof of functional separation.","gap":"Need ELNET France accounts, grant agreement/budget, restricted-fund ledger or project-level expenditure mapping to connect foreign grant dollars to named HATVP actions.","gap_type":"CAUSALITY","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-004","FCT-007","FCT-009"],"status":"GAP","support":"FCT-001,FCT-002,FCT-004,FCT-007,FCT-009"}
CLM-006 | {"attempt_ids":["QRY-001","QRY-002","QRY-006","QRY-007","QRY-008","QRY-015"],"claim":"At least one upstream private-foundation grant to Friends of ELNET carried an explicit program restriction tied to the Brussels office and high-level Israel-delegation programming.","claimant":"INV-160","counter":"This 2019 William Davidson Foundation grant does not prove restrictions on all donors or downstream French policy tasking.","gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","result_ids":["FCT-015"],"status":"SUPPORTED","support":"FCT-015"}
CLM-007 | {"attempt_ids":["QRY-014"],"claim":"The Israeli Ministry of Foreign Affairs directly funded a specific ELNET Europe-Israel operation connected to a French Senate event through a EUR 72,000 sole-supplier procurement.","claimant":"INV-160","counter":"A specific public procurement closes state funding/tasking for that project only; it does not establish general Israeli-state command of ELNET France or the network.","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","result_ids":["FCT-013","FCT-014"],"status":"SUPPORTED","support":"FCT-013,FCT-014"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-015"],"axis":"UPSTREAM_DONORS","links":["CLM-006","CAU-001"],"question":"What upstream grants to Friends of ELNET are general versus program-restricted?","result_ids":["FCT-014"],"sought_objects":["private-foundation 990-PF grants","grant purpose restrictions","donor advised fund entries"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-012","QRY-013"],"axis":"US_HUB_TO_AFFILIATES","links":["CLM-001","CLM-002","CLM-003","CAU-001","CAU-002"],"question":"How much did Friends of ELNET transfer to each foreign ELNET entity and for what program purpose?","result_ids":["FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010"],"sought_objects":["Form 990","Schedule F","Schedule O"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-010","QRY-011","QRY-012"],"axis":"FRANCE_ALLOCATION","links":["CLM-004","CLM-005","CAU-002","CAU-004"],"question":"Can the ELNET France foreign grant be allocated to declared French lobbying expenditure and named influence actions?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-007","FCT-009"],"sought_objects":["HATVP spend","HATVP activity sheets","French entity accounts","grant allocation schedules"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-014"],"axis":"STATE_PROCUREMENT","links":["CLM-007","CAU-003"],"question":"Is there a specific Israeli-state funding/tasking edge to an ELNET entity tied to a French institutional event?","result_ids":["FCT-012","FCT-013"],"sought_objects":["Israeli procurement notice","supplier","amount","project date/object"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"US tax filings directly document donor grants to the US hub and Schedule F cash grants to named foreign affiliates.","counter":"Many donor grants are general support; donor intent/tasking does not automatically propagate downstream.","gap":"NONE","gap_type":"NONE","limit":"Closes resource-flow topology, not downstream political causality.","mechanism":"private foundations/donors -> Friends of ELNET US -> foreign ELNET affiliates","status":"SUPPORTED","support":"FCT-005,FCT-006,FCT-007,FCT-008,FCT-015"}
CAU-002 | {"causal_right":"The US grant to ELNET France and the existence of a substantial declared French lobbying operation are both established; Schedule O describes leader-education/trip/event purposes overlapping with advocacy capacity.","counter":"No inspected allocation ledger maps the USD 1.034m grant to the EUR 100k-200k HATVP lobbying category or to a named action.","gap":"Need restricted-fund terms, French accounts and project-level cost allocation to attribute Friends of ELNET grant dollars to named ELNET France lobbying actions.","gap_type":"CAUSALITY","limit":"Resource/capacity link is plausible and partially supported; action-level funding attribution remains open.","mechanism":"Friends of ELNET US grant -> ELNET France resources/program capacity -> French lobbying operation","status":"GAP","support":"FCT-001,FCT-002,FCT-004,FCT-007,FCT-009"}
CAU-003 | {"causal_right":"The official procurement notice names the ministry, supplier, amount, sole-supplier basis and one-day engagement tied to the French Senate event.","counter":"The notice does not establish control over ELNET France generally or causal effect on a French decision.","gap":"NONE","gap_type":"NONE","limit":"Specific I1-I3 funding/tasking edge only.","mechanism":"Israeli MFA -> EUR 72k sole-supplier procurement -> ELNET Europe-Israel -> French Senate event","status":"SUPPORTED","support":"FCT-013,FCT-014"}
CAU-004 | {"causal_right":"Funding and lobbying actions exist in the same organizational ecosystem, but the public corpus lacks the intermediate allocation/tasking records and counterfactual outcome design.","counter":"HATVP records French actions as own-account; some upstream grants are general support; France-level lobbying spend is a narrower accounting category than total grant receipts.","gap":"Grant agreements/ledgers/instructions and policy-footprint evidence required.","gap_type":"CAUSALITY","limit":"Cannot promote funding to command, capture or policy causation.","mechanism":"foreign/private funding -> tasking of ELNET France -> named lobbying action -> French policy outcome","status":"GAP","support":"FCT-001,FCT-002,FCT-003,FCT-004,FCT-007,FCT-009,FCT-011,FCT-016"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"HATVP records ELNET France interest-representation activities as undertaken for its own account; this blocks automatic reclassification as acting for a foreign client.","status":"PASS","support":"FCT-001,FCT-003"}
CTRL-002 | {"control":"HATVP lobbying expenditure is a bounded regulatory category and cannot be directly compared with total organizational grants as if they measured the same thing.","status":"PASS","support":"FCT-002,FCT-004,FCT-007"}
CTRL-003 | {"control":"Friends of ELNET reports no US lobbying under the IRS Form 990 lobbying question; this is jurisdiction/category-specific and does not negate French affiliate lobbying.","status":"PASS","support":"FCT-011"}
CTRL-004 | {"control":"William Davidson Foundation evidence shows at least one program-restricted upstream grant, but a single restricted donor cannot be generalized to all funders.","status":"PASS","support":"FCT-015"}
CTRL-005 | {"control":"Israeli MFA procurement proves a specific state-funded task but cannot be extrapolated into general state command of ELNET France/network.","status":"PASS","support":"FCT-013,FCT-014"}
CTRL-006 | {"control":"Large foreign grant receipts plus French policy advocacy do not establish downstream policy effect without an allocation/tasking and decision-footprint chain.","status":"PASS","support":"FCT-003,FCT-007,FCT-009,FCT-016"}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Raised donor funds and distributed USD 5.926m in 2024 cash grants to eight foreign ELNET entities, including USD 1.034m to ELNET France.","actor":"Friends of ELNET US","intent":"PROVEN","status":"DONE","support":["FCT-005","FCT-006","FCT-007","FCT-008"]}
ACT-002 | {"action":"Used grant programs described as educating European leaders through seminars, debates, colloquia, Israel visits/study trips and digital exchange.","actor":"Friends of ELNET / foreign affiliates","intent":"PROVEN","status":"DONE","support":["FCT-009"]}
ACT-003 | {"action":"Conducted declared French interest-representation activities targeting laws, public decisions, government and parliament with EUR 100k-200k annual declared lobbying expenditure.","actor":"ELNET France","intent":"PROVEN","status":"DONE","support":["FCT-001","FCT-002","FCT-003","FCT-016"]}
ACT-004 | {"action":"Issued a EUR 72,000 sole-supplier engagement to ELNET Europe-Israel for an event at the French Senate on 10 November 2025.","actor":"Israeli Ministry of Foreign Affairs","intent":"PROVEN","status":"DONE","support":["FCT-013","FCT-014"]}

SEARCH_ACTIVITY_V1:WEB:9|FETCH:6|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | UNAVAILABLE | MNEMO | MNEMO_UNAVAILABLE | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | DISCOVERY_RESULTS | - | - | "William Davidson Foundation" "Friends of ELNET" 450000 2024
QRY-002 | WEB | DISCOVERY_RESULTS | - | - | "Friends of ELNET" "William Davidson Foundation" 990 PF
QRY-003 | WEB | DISCOVERY_RESULTS | - | - | "Rosenberg Family Foundation" "Friends of ELNET" 2024
QRY-004 | WEB | DISCOVERY_RESULTS | - | - | "Newton and Rochelle Becker" "Friends of ELNET" 2024
QRY-005 | WEB | DISCOVERY_RESULTS | - | - | "Friends of ELNET" "delegations to Israel" 450000
QRY-006 | WEB | DISCOVERY_RESULTS | - | - | "WILLIAM DAVIDSON FOUNDATION" "FRIENDS OF ELNET" "450,000" pdf 2024
QRY-007 | WEB | DISCOVERY_RESULTS | - | - | "FRIENDS OF ELNET" "GENERAL OPERATING SUPPORT AND DELEGATIONS TO ISRAEL" pdf
QRY-008 | WEB | DISCOVERY_RESULTS | - | - | "203899187" "FRIENDS OF ELNET" 2024 pdf
QRY-009 | WEB | DISCOVERY_RESULTS | - | - | "Newton & Rochelle Becker Charitable Trust" "FRIENDS OF ELNET" pdf 2024
QRY-010 | FETCH | INSPECTED | SRC-001 | https://www.hatvp.fr/fiche-organisation/?organisation=531006237 | -
QRY-011 | FETCH | INSPECTED | SRC-002 | https://www.hatvp.fr/espacedeclarant/representant-dinterets/ressources/ | -
QRY-012 | FETCH | INSPECTED | SRC-003 | https://docs.candid.org/990/452/452212393/452212393_2024_202512789349300106_990.pdf | -
QRY-013 | FETCH | INSPECTED | SRC-004 | https://projects.propublica.org/nonprofits/organizations/452212393 | -
QRY-014 | FETCH | INSPECTED | SRC-005 | https://mr.gov.il/ilgstorefront/en/p/4000606739 | -
QRY-015 | FETCH | INSPECTED | SRC-006 | https://filing-service.s3-us-west-2.amazonaws.com/scanned-pdfs/201912/203899187/23142111/203899187_201912_990PF_2022013119582662.pdf | -

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:other:hatvp | hatvp:531006237 | HATVP — Fiche ELNET France | 2026-03-31 | 2026-09-13 | ELNET France identity/actions/means; 2025 activity sheets and expenditure section | https://www.hatvp.fr/fiche-organisation/?organisation=531006237
SRC-002 | ◈ | fam:other:hatvp | hatvp:lobbying-resources | HATVP — Ressources représentants d’intérêts | undated | 2026-09-13 | Official scope/method for declaring lobbying resources and expenses | https://www.hatvp.fr/espacedeclarant/representant-dinterets/ressources/
SRC-003 | ◈ | fam:other:irs | irs:45-2212393:2024 | Friends of ELNET — Form 990 2024 | 2025-10-05 | 2026-09-13 | Form 990; Schedule F p2; Schedule O; screenshot-inspected recipient and purpose pages | https://docs.candid.org/990/452/452212393/452212393_2024_202512789349300106_990.pdf
SRC-004 | ◉ | fam:other:irs | propublica:45-2212393 | ProPublica Nonprofit Explorer — Friends of ELNET | 2026-06-26 | 2026-09-13 | Extracted FY2025/FY2024 IRS data and filing links | https://projects.propublica.org/nonprofits/organizations/452212393
SRC-005 | ◈ | fam:other:israel_mfa | mr.gov.il:4000606739 | Israeli MFA procurement/exemption notice 4000606739 | 2025-09-08 | 2026-09-13 | Publisher, sole-supplier exemption, amount, supplier, engagement date | https://mr.gov.il/ilgstorefront/en/p/4000606739
SRC-006 | ◈ | fam:other:irs_foundation | irs:20-3899187:2019 | William Davidson Foundation — Form 990-PF 2019 | 2022-01-31 | 2026-09-13 | Part XV p31; screenshot-inspected Friends of ELNET grant purpose | https://filing-service.s3-us-west-2.amazonaws.com/scanned-pdfs/201912/203899187/23142111/203899187_201912_990PF_2022013119582662.pdf

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.hatvp.fr/fiche-organisation/?organisation=531006237 | other:hatvp | 2026-03-31 | ELNET France HATVP representation status | ELNET France is registered as an interest representative; its 2025 activity sheets state that the represented interest is ELNET France itself (en propre). | -
FCT-002 | FACT | ✧ | https://www.hatvp.fr/fiche-organisation/?organisation=531006237 | other:hatvp | 2026-03-31 | ELNET France declared lobbying expenditure 2025 | For 2025 ELNET France declared between EUR 100,000 and EUR 200,000 of expenditure devoted to interest-representation actions and 3 FTE staff; the same expenditure bracket and 3 FTE are shown for 2023 and 2024. | -
FCT-003 | FACT | ✧ | https://www.hatvp.fr/fiche-organisation/?organisation=531006237 | other:hatvp | 2026-03-31 | ELNET France declared policy-influence methods | A 2025 ELNET France activity sheet on strengthening legislation/regulation against Islamism declares methods including transmitting suggestions to influence drafting of a public decision, online influence strategies, correspondence, events and meetings. | -
FCT-004 | FACT | ✧ | https://www.hatvp.fr/espacedeclarant/representant-dinterets/ressources/ | other:hatvp | 2026-09-13 | HATVP lobbying resource perimeter | HATVP rules define declared interest-representation resources as a bounded category of means devoted to lobbying activities; this category is not the same as an organization’s total operating budget or all program expenditure. | -
FCT-005 | FACT | ✧ | https://docs.candid.org/990/452/452212393/452212393_2024_202512789349300106_990.pdf | other:irs | 2025-10-05 | Friends of ELNET 2024 revenue and contributions | Friends of ELNET reported USD 8,955,347 total revenue in 2024, including USD 8,679,742 in contributions and grants. | -
FCT-006 | FACT | ✧ | https://docs.candid.org/990/452/452212393/452212393_2024_202512789349300106_990.pdf | other:irs | 2025-10-05 | Friends of ELNET 2024 foreign grants total | Friends of ELNET reported USD 5,926,477 in grants and similar amounts paid; Schedule F lists eight foreign ELNET recipient entities whose cash grants sum exactly to USD 5,926,477. | -
FCT-007 | FACT | ✧ | https://docs.candid.org/990/452/452212393/452212393_2024_202512789349300106_990.pdf | other:irs | 2025-10-05 | Friends of ELNET grant to ELNET France | Schedule F lists a USD 1,034,210 electronic cash grant to ELNET, France in 2024. | -
FCT-008 | FACT | ✧ | https://docs.candid.org/990/452/452212393/452212393_2024_202512789349300106_990.pdf | other:irs | 2025-10-05 | Friends of ELNET 2024 affiliate grant distribution | Schedule F lists 2024 grants to ELNET Brussels USD 685,202; France USD 1,034,210; Germany USD 904,528; Global USD 929,486; Israel USD 880,438; Italy USD 415,522; Poland USD 496,500; UK USD 580,591. | -
FCT-009 | FACT | ✧ | https://docs.candid.org/990/452/452212393/452212393_2024_202512789349300106_990.pdf | other:irs | 2025-10-05 | Friends of ELNET stated foreign-grant program purpose | Schedule O states that foreign grants support education of European leaders, seminars, public debates, newsletters, lectures and colloquia, visits and study trips to Israel, and internet/new-technology exchange of ideas. | -
FCT-010 | FACT | ✧ | https://docs.candid.org/990/452/452212393/452212393_2024_202512789349300106_990.pdf | other:irs | 2025-10-05 | Friends of ELNET 2024 program service expense | Friends of ELNET reported USD 7,029,701 in program-service expenses in 2024, including USD 5,926,477 of grants. | -
FCT-011 | FACT | ✧ | https://docs.candid.org/990/452/452212393/452212393_2024_202512789349300106_990.pdf | other:irs | 2025-10-05 | Friends of ELNET US lobbying checkbox | On its 2024 US Form 990, Friends of ELNET answered No to the IRS question asking whether the US 501(c)(3) engaged in lobbying activities; this is a US tax-form classification and does not classify foreign affiliates under French law. | -
FCT-012 | FACT | ✧ | https://projects.propublica.org/nonprofits/organizations/452212393 | other:irs | 2026-06-26 | Friends of ELNET FY2025 growth | ProPublica’s IRS-derived data for FY2025 reports USD 10,705,776 revenue and USD 10,307,022 contributions, showing continued large-scale donor financing after 2024. | -
FCT-013 | FACT | ✧ | https://mr.gov.il/ilgstorefront/en/p/4000606739 | other:israel_mfa | 2025-09-08 | Israeli MFA ELNET Europe-Israel procurement amount | Israeli Ministry of Foreign Affairs exemption notice 4000606739 records a EUR 72,000 sole-supplier engagement with ELNET Europe-Israel. | -
FCT-014 | FACT | ✧ | https://mr.gov.il/ilgstorefront/en/p/4000606739 | other:israel_mfa | 2025-09-08 | Israeli MFA ELNET procurement French Senate event | The procurement notice concerns an ELNET Europe event at the French Senate, with engagement start and end on 10 November 2025; the supplier tax number is 580535672. | -
FCT-015 | FACT | ✧ | https://filing-service.s3-us-west-2.amazonaws.com/scanned-pdfs/201912/203899187/23142111/203899187_201912_990PF_2022013119582662.pdf | other:irs_foundation | 2022-01-31 | William Davidson Foundation restricted-purpose grant to Friends of ELNET | The William Davidson Foundation 2019 Form 990-PF specifies a Friends of ELNET grant purpose: support the Brussels office and creation of high-level programming for Israel delegations. | -
FCT-016 | FACT | ✧ | https://www.hatvp.fr/fiche-organisation/?organisation=531006237 | other:hatvp | 2026-03-31 | ELNET France 2025 declared policy objectives | ELNET France declared 2025 objectives including opposing French recognition of a Palestinian state, strengthening legislation/regulation on Islamism and anti-Jewish hatred, and strengthening France-Europe-Israel/Abraham Accords diplomatic relations. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-002
FCT-005 | SRC-003
FCT-006 | SRC-003
FCT-007 | SRC-003
FCT-008 | SRC-003
FCT-009 | SRC-003
FCT-010 | SRC-003
FCT-011 | SRC-003
FCT-012 | SRC-004
FCT-013 | SRC-005
FCT-014 | SRC-005
FCT-015 | SRC-006
FCT-016 | SRC-001

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
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:Lock financial topology scope and inspect primary funding records
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:Retrieve IRS/HATVP/procurement records and test allocation/tasking
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:Normalize financial and lobbying facts
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:Test donor-to-hub-to-affiliate allocation, specific procurement tasking and downstream policy-effect ceiling
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:Verify finance/tasking claims and causal ceiling
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:Build accountability, contradictions, impact and final technical narrative
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:Freeze technical narrative and run final gates

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-13T11:20:39.700801+00:00","fact_mem":{},"mnemo_row":"MNEMO_UNAVAILABLE — local memory service unavailable in this runtime; no memory ids fabricated.","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":16,"eligible":16,"failure":0,"success":0}}

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
