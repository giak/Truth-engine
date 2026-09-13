ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260911-2109-dollar-clearing-extraterritorialite | PARENT_RUN_ID:NONE | AS_OF:2026-09-11
INPUT_KIND:RUN_CARD | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/audit121/INV152_TRANSACTION_2026-09-11/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-11_dollar-clearing-extraterritorialite/2026-09-11_21-09_dollar-clearing-extraterritorialite_INPUT.txt | SUBJECT_SLUG:dollar-clearing-extraterritorialite | SUBJECT_FP:sha256:1406365c6b614dfdc2f6fdd31544bc77ab486346b7ee7ca19e05e930fbadbf6a | INPUT_SHA256:sha256:7668f85cb2a67a4bec7a128297f58489be1fc0a8c94d91169edcea104f6b15c9
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/UE, 2014-2026; dollar clearing, correspondent/payable-through accounts, US secondary sanctions and European institutional/commercial responses. Exclude generic domestic debanking and cloud dependency already covered by INV-124/125.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-152 — Dollar, clearing, correspondent banking et extraterritorialité financière

## Verdict exécutif

INV-152 ferme un mécanisme distinct des sanctions génériques et du debanking domestique : **le contrôle d’une juridiction financière et de points d’accès au dollar/correspondent banking peut rendre une règle ou un risque d’enforcement matériellement contraignant pour des acteurs européens, puis propager cette contrainte par leurs propres décisions de compliance et de de-risking**. La chaîne observée est : `juridiction / rail financier -> accès au système ou compte correspondant -> règle/enforcement ou sanction secondaire -> risque économique -> adaptation de banque/entreprise -> contre-mesure éventuelle -> effet`.

Le premier discriminant est juridique. BNP Paribas constitue un cas d’enforcement massif mais pas le meilleur exemple d’extraterritorialité sans nexus : la banque a admis avoir fait transiter plus de 8,8 milliards de dollars par le système financier américain pour des entités sanctionnées. Le dossier ferme donc `transaction en dollars via système US -> compétence/enforcement -> pénalité/suspension de clearing`. Il ne justifie pas le raccourci `banque étrangère = compétence américaine universelle`.

Le cas Total/South Pars 11 ferme la branche plus forte. Le projet avait été signé en 2017 sous le cadre alors applicable. Après le retrait américain du JCPOA en mai 2018, Total a annoncé qu’il devrait se retirer avant novembre sans waiver américain protégeant le groupe des sanctions secondaires. L’entreprise a explicitement relié cette décision à ses dépendances au financement en dollars par des banques américaines, à son actionnariat américain et à ses opérations aux États-Unis. Ici, la contrainte ne vient pas d’un ordre individuel adressé par Washington à Total : **le risque crédible de perdre l’accès à des ressources financières et marchés reliés au système américain suffit à modifier une conduite commerciale européenne**.

Bank Melli Iran c. Telekom Deutschland confirme ce mécanisme de propagation privée. La Cour de justice de l’Union a jugé que l’interdiction européenne de se conformer aux sanctions secondaires américaines pouvait être invoquée même sans ordre ou instruction spécifique d’une autorité américaine. Elle a toutefois demandé de prendre en compte le risque de pertes économiques disproportionnées pour l’opérateur européen. Le point probatoire est essentiel : `enforcement public -> incitation privée -> de-risking` n’est pas identique à `État -> ordre direct -> entreprise`.

L’Union européenne n’est pas restée passive. Le Blocking Statute a été actualisé en 2018 pour couvrir les mesures américaines réimposées contre l’Iran, interdit en principe aux opérateurs européens de s’y conformer et prévoit des mécanismes de neutralisation/indemnisation, avec possibilité de dérogation si la non-conformité causerait de graves dommages. Les E3 ont ensuite créé puis opérationnalisé INSTEX ; une première transaction de biens médicaux vers l’Iran a été réalisée en mars 2020. Cela ferme une **contre-adaptation institutionnelle réelle**, mais pas l’efficacité générale d’INSTEX à neutraliser la puissance du dollar.

La dimension réseau dépasse les cas individuels. La BCE décrit le correspondent banking comme infrastructure centrale des paiements transfrontaliers et observe une contraction de 20 à 30 % du nombre de correspondants actifs sur une décennie. Les banques citent des facteurs de stratégie, de rentabilité, de conformité et de réputation ; la BCE relie aussi la contraction à plusieurs vagues de sanctions et à l’affaire BNP. Le réseau transmet donc les contraintes, mais **chaque fermeture de relation n’est pas une décision taskée par un État**.

Enfin, les autorités américaines disposent explicitement de leviers sur les comptes correspondants et payable-through accounts de banques étrangères. CISADA/IFSR permet d’imposer des conditions ou d’interdire ces accès ; FinCEN a encore proposé en février 2026 de couper une banque suisse de l’accès aux comptes correspondants américains. Cette proposition montre que le point de contrôle reste opérationnel, mais elle n’est pas traitée comme mesure finale.

## 1. Juridiction territoriale et extraterritorialité ne doivent pas être fusionnées

Le dossier BNP ferme un cas de compétence fondée sur le passage effectif par le système financier américain. C’est un exemple de puissance du rail, mais pas la preuve la plus forte d’une règle appliquée sans nexus territorial. À l’inverse, les sanctions secondaires visant des acteurs non américains et la réaction européenne au JCPOA isolent la dimension extraterritoriale au sens contesté par l’UE.

## 2. Le dollar agit par les dépendances qu’il agrège

Total expose le mécanisme : une entreprise européenne peut juger impossible de maintenir une activité licite en Europe si elle risque de perdre du financement en dollars, des actionnaires ou l’accès au marché américain. Le levier ne se réduit donc pas à un message SWIFT ou à une banque précise ; il agrège monnaie, banques correspondantes, financement, marché et juridiction.

## 3. Correspondent banking : propagation plutôt que commandement

Les règles américaines peuvent atteindre une banque étrangère via son accès à un compte correspondant aux États-Unis. Mais la propagation en aval implique des décisions privées de conformité et de gestion du risque. La BCE montre précisément cette pluralité de causes. Une enquête qui coderait chaque fermeture comme `US tasking` fabriquerait de la causalité.

## 4. L’Union construit des contre-pouvoirs, avec un succès partiel

Blocking Statute, contentieux Bank Melli et INSTEX montrent que l’UE identifie le problème comme une atteinte à son autonomie normative et économique et tente d’y répondre. La première transaction INSTEX prouve que l’alternative a fonctionné au moins une fois ; elle ne prouve ni une substitution systémique au dollar ni la neutralisation générale des sanctions secondaires.

## Verdict causal

INV-152 ferme `rail/juridiction -> enforcement ou risque crédible -> adaptation commerciale` et `pression extraterritoriale -> contre-adaptation institutionnelle UE`. Elle ne ferme pas `levier financier -> concession politique souveraine européenne`, ni un taux de réussite représentatif. Le mécanisme relève donc du **pouvoir sur l’espace des choix économiques**, et peut contribuer à une coercition ou une ingérence selon l’intention, la demande politique et l’effet aval, qui doivent être prouvés séparément.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:0|EDI_DECISIVE:4|SRC_COMPLETE:14/14

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-11
- **breaks:**
  - 2014 BNP plea
  - 2018 US JCPOA withdrawal and secondary-sanctions reimposition
  - 2018 EU Blocking Statute update
  - 2019 INSTEX launch
  - 2020 first INSTEX transaction
  - 2021 Bank Melli judgment
  - 2025 ECB correspondent-banking review
  - 2026 MBaer proposed severance
- **status:** CURRENT
- **window:** France/UE 2014-2026; BNP enforcement, JCPOA withdrawal, blocking statute, INSTEX, Bank Melli, current correspondent controls

### MANIPULATION_REPORT
- **assumptions:**
  - public statements describe formal authorities and observed reactions but not every private compliance decision
- **clusters:**
  - POWER
  - MONEY
  - NETWORK
- **complexity:**
  - **band:** HIGH
  - **score:** 9
- **implicit:**
  - financial infrastructure can modify available choices without persuasion
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - dollar=extraterritoriality
  - sanctions=ingérence
  - de-risking=state command
  - commercial withdrawal=political capitulation
  - SWIFT=entire rail
- **priorities:**
  - legal nexus
  - correspondent-account authority
  - secondary-sanctions risk
  - EU company adaptation
  - EU countermeasures
  - political-effect ceiling
- **query_guidance:** separate territorial U.S. nexus, secondary sanctions, private compliance, institutional countermeasure and sovereign effect
- **rhetorical:**
  - NONE
- **speaker:** mechanism-first forensic investigation contract
- **symbol_stage:** FINAL
- **symbols:**
  - **ACCESS:** ability to use correspondent/dollar/U.S. financial infrastructure
  - **ACTOR:** state/regulator/financial institution or operator exercising or bearing rail power
  - **ADAPTATION:** commercial or institutional response to constraint
  - **CLEARING:** settlement/processing path for payment obligations
  - **COERCION:** pressure intended to alter a target decision through imposed cost or access loss
  - **CONCESSION:** specific sovereign policy change matching an external demand
  - **CORRESPONDENT:** bank providing account/payment services to another bank
  - **COUNTERMEASURE:** EU legal/institutional mitigation of foreign extraterritorial effects
  - **DE_RISKING:** private restriction/exit due legal/compliance/reputational/business risk
  - **EFFECT:** observable commercial, institutional or political downstream result
  - **ENFORCEMENT:** public legal action or credible sanction authority
  - **INGERENCE:** qualification requiring additional illegitimacy/autonomy-interference evidence, not a mechanism label
  - **RAIL:** currency/clearing/correspondent access infrastructure
  - **SECONDARY_SANCTION:** risk imposed on non-U.S. actor for covered foreign conduct
  - **TERRITORIAL_NEXUS:** transaction/entity touches U.S. system or territory
- **threats:**
  - legal-nexus collapse
  - attribution promotion
  - effect promotion
  - overlap regression with INV-124
  - single-case prevalence extrapolation

### MODULE_EXECUTION
NONE

### SCOPING_REPORT
- **chain:**
  - jurisdiction/monetary rail
  - transaction/correspondent access
  - rule/enforcement/secondary-sanctions risk
  - bank/company compliance or de-risking
  - access/commercial adaptation
  - EU countermeasure
  - sovereign effect
- **exclusions:**
  - generic domestic debanking
  - cloud/data extraterritoriality
  - sanctions catalogues without rail mechanism
- **object:** Dollar, clearing, correspondent banking and financial extraterritoriality
- **scope:** France/UE 2014-2026 with U.S. enforcement comparators

### CREDO
- territorial nexus != pure extraterritoriality
- secondary sanction != individual order
- enforcement risk != private state-tasking
- commercial adaptation != political concession
- correspondent banking != SWIFT
- legal reach != ingérence automatic
- countermeasure != full neutralisation

### COGNITIVE_MAP
- **causal_boundary:** close leverage at credible legal/rail control plus observed adaptation; close political coercion only with actor intent/demand and a causally linked sovereign concession
- **core_model:** financial-rail power is direct option-set power: access to a dominant currency/jurisdiction/correspondent network can make foreign legal risk economically binding on EU actors without persuasion
- **rival_models:**
  - ordinary territorial jurisdiction over transactions touching U.S. system
  - private profitability/reputation-driven de-risking
  - legitimate AML/sanctions compliance
  - EU resistance/adaptation rather than capitulation
  - market concentration without exercised exclusion
- **serial_edges:**
  - legal nexus
  - rail control
  - enforcement risk
  - private compliance
  - commercial adaptation
  - institutional countermeasure
  - sovereign policy effect

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** BNP admitted moving transactions through the U.S. financial system
  - **resolution:** treat BNP as exercised enforcement with direct U.S.-system nexus, not the strongest secondary-sanctions case
  - **thesis:** BNP proves U.S. extraterritoriality over any foreign dollar transaction
- **item 2:**
  - **antithesis:** Total explicitly tied unwind to U.S. secondary-sanctions risk and dollar/U.S. exposure
  - **resolution:** commercial adaptation caused by secondary-sanctions risk is supported; political capitulation is not
  - **thesis:** Total withdrawal was ordinary business choice
- **item 3:**
  - **antithesis:** Bank Melli and ECB show firms can act without an individual order and for mixed risk/business reasons
  - **resolution:** public enforcement risk can propagate through private incentives without converting each exit into state tasking
  - **thesis:** private de-risking equals U.S. command
- **item 4:**
  - **antithesis:** EU maintained JCPOA commitment, updated blocking statute and operationalised INSTEX
  - **resolution:** commercial reach and EU counter-adaptation are supported; sovereign policy concession is not closed
  - **thesis:** EU surrendered to financial leverage

### RESOURCE_FLOW_MAP
- **item 1:**
  - **case:** BNP Paribas 2014
  - **flow:** dollar transactions -> U.S. financial system -> criminal/regulatory enforcement -> penalty + temporary clearing suspension -> compliance change
  - **status:** EXERCISED_WITH_DIRECT_US_NEXUS
  - **support:**
    - FCT-001
    - FCT-002
- **item 2:**
  - **case:** Total SP11 2018
  - **flow:** lawful EU/Iran project -> U.S. secondary-sanctions reimposition -> financing/shareholder/US-operations exposure -> project unwind absent waiver
  - **status:** SECONDARY_SANCTIONS_TO_COMMERCIAL_ADAPTATION_SUPPORTED
  - **support:**
    - FCT-005
    - FCT-006
    - FCT-007
- **item 3:**
  - **case:** Bank Melli/Telekom
  - **flow:** U.S. secondary sanctions -> EU telecom termination risk -> EU Blocking Statute litigation -> balancing of economic loss and EU prohibition
  - **status:** PRIVATE_PROPAGATION_WITHOUT_INDIVIDUAL_US_ORDER
  - **support:**
    - FCT-009
    - FCT-010
    - FCT-011
- **item 4:**
  - **case:** EU institutional response
  - **flow:** reimposed U.S. sanctions -> blocking statute + preservation of financial channels -> INSTEX -> first transaction
  - **status:** COUNTERMEASURE_USED_BUT_BOUNDED
  - **support:**
    - FCT-008
    - FCT-009
    - FCT-012
    - FCT-013
- **item 5:**
  - **case:** correspondent network
  - **flow:** correspondent-account authority + sanctions/compliance risk -> relationship retreat/exclusion -> under-served corridors
  - **status:** SYSTEMIC_PROPAGATION_SUPPORTED_WITH_MIXED_DRIVERS
  - **support:**
    - FCT-003
    - FCT-004
    - FCT-014
    - FCT-015
    - FCT-016
    - FCT-017

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** U.S. DOJ/Treasury/FinCEN
  - **relation:** enforcement and correspondent-account access conditions/prohibitions
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
    - FCT-004
    - FCT-016
    - FCT-017
  - **to:** foreign banks
- **item 2:**
  - **from:** U.S. secondary-sanctions regime
  - **relation:** credible loss of U.S./dollar access and sanctions exposure influencing commercial choice
  - **support:**
    - FCT-006
    - FCT-007
    - FCT-010
    - FCT-011
  - **to:** Total/Telekom and other EU operators
- **item 3:**
  - **from:** EU/Member States
  - **relation:** Blocking Statute and INSTEX mitigation/countermeasure
  - **support:**
    - FCT-008
    - FCT-009
    - FCT-012
    - FCT-013
  - **to:** EU operators/Iran trade
- **item 4:**
  - **from:** correspondent-banking network
  - **relation:** private network retrenchment under business/compliance/reputational pressures
  - **support:**
    - FCT-014
    - FCT-015
  - **to:** cross-border payment corridors

### IMPACT_MAP
- **downstream:** adds financial-jurisdiction/rail control as a distinct economic-power mechanism while preserving attribution and political-effect ceilings
- **measured_objects:**
  - enforcement penalties
  - dollar-clearing suspension
  - project withdrawal
  - contract termination risk
  - blocking-statute litigation
  - INSTEX transaction
  - correspondent relationship retreat
  - proposed severance of correspondent access
- **not_established:**
  - general EU sovereign policy concession
  - all private de-risking as U.S. tasking
  - representative prevalence/success rate
  - full neutralisation by Blocking Statute/INSTEX

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** transactions were routed through U.S. financial system and New York clearing
  - **issue:** BNP = pure extraterritoriality
  - **pro:** French bank faced massive U.S. penalties
  - **resolution:** EXERCISED_ENFORCEMENT_WITH_TERRITORIAL_SYSTEM_NEXUS
- **item 2:**
  - **contra:** company explicitly identified U.S. secondary sanctions and dollar/U.S. exposure as decisive constraints
  - **issue:** Total exit = voluntary business decision only
  - **pro:** company chose to exit project
  - **resolution:** SECONDARY_SANCTIONS_CAUSAL_COMMERCIAL_ADAPTATION_SUPPORTED
- **item 3:**
  - **contra:** CJEU/ECB evidence shows decisions can occur without specific orders and have multiple private drivers
  - **issue:** de-risking = direct state command
  - **pro:** sanctions/enforcement create incentives
  - **resolution:** PUBLIC_RISK_PRIVATE_MEDIATION
- **item 4:**
  - **contra:** EU maintained JCPOA commitment and no specific sovereign concession is isolated
  - **issue:** financial leverage = successful political coercion
  - **pro:** EU firms changed conduct and EU built countermeasures
  - **resolution:** COMMERCIAL_EFFECT_CLOSED_POLITICAL_SUCCESS_OPEN

### VERIFICATION_REPORT
- **checks:**
  - BNP nexus separated from pure secondary sanctions
  - Total before/after project state checked
  - secondary-sanctions financial exposure tied to company statement
  - Blocking Statute purpose and compliance rule checked
  - Bank Melli preserved no-specific-order distinction
  - INSTEX actual first transaction checked
  - correspondent retreat treated as mixed-driver system effect
  - political concession not inferred from commercial adaptation
- **status:** PASS_WITH_EXPLICIT_GAPS

### EDI_REPORT
- **corpus:** 14 inspected sources across U.S. enforcement/regulatory, EU institutional/judicial, company and central-bank lineages; related pages are not counted as prevalence evidence
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim:** BNP exercised enforcement
    - **families:**
      - A
  - **item 2:**
    - **claim:** Total commercial adaptation
    - **families:**
      - C
  - **item 3:**
    - **claim:** EU countermeasures
    - **families:**
      - B
      - E
  - **item 4:**
    - **claim:** correspondent network propagation
    - **families:**
      - A
      - D
- **diagnostic_not_truth:** true
- **dimensions:**
  - territorial nexus
  - secondary sanctions
  - correspondent-account authority
  - EU company adaptation
  - EU legal countermeasure
  - actual alternative-rail use
  - private de-risking
  - sovereign-effect ceiling
- **edi:** MULTI_LINEAGE_OFFICIAL_DOMINANT_WITH_COMPANY_AND_CENTRAL_BANK_CONTROLS
- **source_counts:**
  - **A:** 6
  - **B:** 4
  - **C:** 2
  - **D:** 1
  - **E:** 1

### RESPONSIBILITY_MAP
- **item 1:**
  - **claim:** BNP enforcement nexus
  - **owner:** US DOJ/regulators + BNPP admissions
  - **status:** SUPPORTED
  - **support:**
    - FCT-001
    - FCT-002
- **item 2:**
  - **claim:** Total secondary-sanctions-driven unwind
  - **owner:** Total corporate statement
  - **status:** SUPPORTED
  - **support:**
    - FCT-005
    - FCT-006
    - FCT-007
- **item 3:**
  - **claim:** EU extraterritoriality objection/countermeasure
  - **owner:** European Commission/CJEU/E3
  - **status:** SUPPORTED
  - **support:**
    - FCT-008
    - FCT-009
    - FCT-010
    - FCT-011
    - FCT-012
    - FCT-013
- **item 4:**
  - **claim:** private correspondent retreat
  - **owner:** ECB synthesis of network/survey evidence
  - **status:** SUPPORTED_WITH_MIXED_DRIVERS
  - **support:**
    - FCT-014
    - FCT-015
- **item 5:**
  - **claim:** general sovereign EU concession
  - **owner:** INV-152 synthesis
  - **status:** NOT_ESTABLISHED
  - **support:**
    - NONE
- **item 6:**
  - **claim:** representative denominator
  - **owner:** INV-152 synthesis
  - **status:** NOT_ESTABLISHED
  - **support:**
    - FCT-001
    - FCT-003
    - FCT-006
    - FCT-010
    - FCT-012
    - FCT-013
    - FCT-015

### NEXT_QUERIES
- **item 1:**
  - **query:** investor-state arbitration threat/claim -> regulatory chilling/adaptation -> policy effect
  - **route:** RECLASS_CANDIDATE
  - **trigger:** post-INV152 reclassification
- **item 2:**
  - **query:** procurement/offset/agent/commission -> intermediary/official -> award/policy decision
  - **route:** RECLASS_CANDIDATE
  - **trigger:** post-INV152 reclassification
- **item 3:**
  - **query:** financial-rail coercion representative denominator and sovereign-policy success rate
  - **route:** RECHECK
  - **trigger:** comparative dataset or causal-design evidence

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-001,FCT-003,FCT-006,FCT-010,FCT-012,FCT-013,FCT-015 | final:GAP | gap:DENOMINATOR
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-001,FCT-002,FCT-006 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-003,FCT-004,FCT-016,FCT-017 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-006,FCT-007,FCT-010,FCT-011,FCT-015 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-008,FCT-009,FCT-012,FCT-013 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-012,FCT-013 | final:GAP | gap:CAUSALITY
AXS-006 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-001,FCT-003,FCT-006,FCT-010,FCT-012,FCT-013,FCT-015 | final:GAP | gap:DENOMINATOR
CLM-001 | attempts:QRY-001,SRC-001 | support:FCT-001,FCT-002 | counter:- | results:FCT-001,FCT-002 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-001,SRC-001 | support:FCT-001,FCT-002 | counter:- | results:FCT-001,FCT-002 | final:REFUTED | gap:LEGAL_NEXUS
CLM-003 | attempts:QRY-007,QRY-008,QRY-009,QRY-011,SRC-007,SRC-008,SRC-009,SRC-011 | support:FCT-003,FCT-004,FCT-016,FCT-017 | counter:- | results:FCT-003,FCT-004,FCT-016,FCT-017 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-002,QRY-013,SRC-002,SRC-013 | support:FCT-005,FCT-006,FCT-007 | counter:- | results:FCT-005,FCT-006,FCT-007 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-006,QRY-010,SRC-006,SRC-010 | support:FCT-010,FCT-011,FCT-015 | counter:- | results:FCT-010,FCT-011,FCT-015 | final:SUPPORTED | gap:NONE
CLM-006 | attempts:QRY-003,QRY-004,QRY-005,QRY-012,QRY-014,SRC-003,SRC-004,SRC-005,SRC-012,SRC-014 | support:FCT-008,FCT-009,FCT-012,FCT-013 | counter:- | results:FCT-008,FCT-009,FCT-012,FCT-013 | final:SUPPORTED | gap:NONE
CLM-007 | attempts:QRY-006,SRC-006 | support:FCT-015 | counter:- | results:FCT-015 | final:REFUTED | gap:GENERALIZATION
CLM-008 | attempts:QRY-006,QRY-010,SRC-006,SRC-010 | support:FCT-011,FCT-015 | counter:- | results:FCT-011,FCT-015 | final:REFUTED | gap:ATTRIBUTION
CLM-009 | attempts:QRY-001,QRY-003,QRY-007,QRY-008,QRY-012,SRC-001,SRC-003,SRC-007,SRC-008,SRC-012 | support:FCT-001,FCT-003,FCT-004,FCT-008,FCT-009 | counter:- | results:FCT-001,FCT-003,FCT-004,FCT-008,FCT-009 | final:REFUTED | gap:QUALIFICATION
CLM-010 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:- | final:GAP | gap:CAUSALITY
CLM-011 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:- | final:GAP | gap:DENOMINATOR

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
AXS-005 | AXS | GAP | CAUSALITY | No specific sovereign EU policy concession is causally closed.
AXS-006 | AXS | GAP | DENOMINATOR | No representative France/EU denominator or success-rate dataset in the bounded run.
CLM-002 | CLM | REFUTED | LEGAL_NEXUS | The admitted conduct used the U.S. financial system.
CLM-007 | CLM | REFUTED | GENERALIZATION | ECB identifies business strategy, profitability and compliance/reputational risk as distinct drivers.
CLM-008 | CLM | REFUTED | ATTRIBUTION | Private risk calculations can mediate or amplify public enforcement risk.
CLM-009 | CLM | REFUTED | QUALIFICATION | Jurisdiction/enforcement, commercial adaptation and political coercion require separate qualification.
CLM-010 | CLM | GAP | CAUSALITY | Commercial and institutional adaptations are established; a specific sovereign concession causally attributable to the lever is not closed.
CLM-011 | CLM | GAP | DENOMINATOR | No representative denominator found in the 14 inspected sources.
CAU-001 | CAU | SUPPORTED | CAUSALITY | No specific sovereign EU policy concession or representative success-rate denominator is causally closed.

SEMANTIC_COUNTS_V1:LED:2|CLM:11|AXS:6|CAU:1|CTRL:6|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"evidence_excerpt":"BNP territorial nexus; Total secondary-sanctions withdrawal; Bank Melli private response; EU Blocking Statute and INSTEX countermeasures.","kind":"HYPOTHESIS","lead":"Financial rails create leverage when legal jurisdiction or correspondent-account access can impose credible enforcement risk that changes EU bank/company conduct.","linked_ids":["CLM-001","CLM-002","CLM-003","CLM-004","CLM-005","CLM-006","CLM-007","CLM-008","CLM-009","CLM-010"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017"],"routes":["POWER","MONEY","NETWORK"],"source_id":"INV-152-RUN_CARD","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"evidence_excerpt":"Run closes commercial/institutional adaptation, not prevalence or general political success.","gap":"No representative denominator and no closed sovereign concession.","gap_type":"DENOMINATOR","kind":"GAP","lead":"Representative denominator and sovereign-policy success rate of extraterritorial financial leverage against France/EU.","linked_ids":["CLM-010","CLM-011"],"locator":"GAP","materiality":"HIGH","result_ids":["FCT-001","FCT-003","FCT-006","FCT-010","FCT-012","FCT-013","FCT-015"],"routes":["RECHECK"],"source_id":"INV-152-RUN_CARD","status":"GAP"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"BNP Paribas demonstrates exercised U.S. enforcement where dollar transactions traversed the U.S. financial system.","claimant":"INV-152 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002"]}
CLM-002 | {"claim":"BNP Paribas alone proves a purely extraterritorial no-U.S.-nexus sanctions theory.","claimant":"INV-152 synthesis","counter":"NONE_FOUND","gap":"The admitted conduct used the U.S. financial system.","gap_type":"LEGAL_NEXUS","materiality":"DECISIVE","status":"REFUTED","support":["FCT-001","FCT-002"]}
CLM-003 | {"claim":"U.S. law can use correspondent/payable-through account access as leverage on foreign financial institutions.","claimant":"INV-152 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-003","FCT-004","FCT-016","FCT-017"]}
CLM-004 | {"claim":"Total SP11 closes a secondary-sanctions threat -> EU company commercial withdrawal/adaptation edge.","claimant":"INV-152 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-005","FCT-006","FCT-007"]}
CLM-005 | {"claim":"Secondary-sanctions effects can propagate through private risk management without an individual U.S. order to the EU firm.","claimant":"INV-152 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-010","FCT-011","FCT-015"]}
CLM-006 | {"claim":"EU institutions treated U.S. Iran sanctions as an extraterritoriality problem and adopted/used countermeasures.","claimant":"INV-152 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-008","FCT-009","FCT-012","FCT-013"]}
CLM-007 | {"claim":"Correspondent-banking retreat can be explained entirely by direct state orders.","claimant":"INV-152 synthesis","counter":"NONE_FOUND","gap":"ECB identifies business strategy, profitability and compliance/reputational risk as distinct drivers.","gap_type":"GENERALIZATION","materiality":"HIGH","status":"REFUTED","support":["FCT-015"]}
CLM-008 | {"claim":"Private de-risking decisions are automatically attributable as state command.","claimant":"INV-152 synthesis","counter":"NONE_FOUND","gap":"Private risk calculations can mediate or amplify public enforcement risk.","gap_type":"ATTRIBUTION","materiality":"DECISIVE","status":"REFUTED","support":["FCT-011","FCT-015"]}
CLM-009 | {"claim":"Financial-rail leverage automatically constitutes political ingérence.","claimant":"INV-152 synthesis","counter":"NONE_FOUND","gap":"Jurisdiction/enforcement, commercial adaptation and political coercion require separate qualification.","gap_type":"QUALIFICATION","materiality":"DECISIVE","status":"REFUTED","support":["FCT-001","FCT-003","FCT-004","FCT-008","FCT-009"]}
CLM-010 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"claim":"The bounded run establishes that financial-rail leverage caused a specific sovereign EU policy concession to the United States.","claimant":"INV-152 synthesis","counter":"NONE_FOUND","gap":"Commercial and institutional adaptations are established; a specific sovereign concession causally attributable to the lever is not closed.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"GAP","support":"NONE_FOUND"}
CLM-011 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"claim":"A representative France/EU success-rate denominator for financial-rail coercion is available.","claimant":"INV-152 synthesis","counter":"NONE_FOUND","gap":"No representative denominator found in the 14 inspected sources.","gap_type":"DENOMINATOR","materiality":"HIGH","status":"GAP","support":"NONE_FOUND"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"axis":"LEGAL_NEXUS","links":["CLM-001","CLM-002"],"question":"Does the transaction actually touch U.S. territory/system or rely only on secondary sanctions?","result_ids":["FCT-001","FCT-002","FCT-006"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"axis":"RAIL_CONTROL","links":["CLM-003"],"question":"Can correspondent/dollar access be conditioned or severed?","result_ids":["FCT-003","FCT-004","FCT-016","FCT-017"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"axis":"PRIVATE_ADAPTATION","links":["CLM-004","CLM-005","CLM-008"],"question":"Does enforcement risk change conduct of EU firms/banks?","result_ids":["FCT-006","FCT-007","FCT-010","FCT-011","FCT-015"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"axis":"EU_COUNTERMEASURES","links":["CLM-006"],"question":"Did EU institutions build and use countermeasures?","result_ids":["FCT-008","FCT-009","FCT-012","FCT-013"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"axis":"POLITICAL_EFFECT","gap":"No specific sovereign EU policy concession is causally closed.","gap_type":"CAUSALITY","links":["CLM-009","CLM-010"],"question":"Is a sovereign EU policy concession causally closed?","result_ids":["FCT-012","FCT-013"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"GAP"}
AXS-006 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"axis":"DENOMINATOR","gap":"No representative France/EU denominator or success-rate dataset in the bounded run.","gap_type":"DENOMINATOR","links":["CLM-011"],"question":"Is there a representative success-rate denominator?","result_ids":["FCT-001","FCT-003","FCT-006","FCT-010","FCT-012","FCT-013","FCT-015"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"GAP"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"FINANCIAL_RAIL_CONTROL_CAN_MODIFY_OPTIONS_DIRECTLY; POLITICAL_INGERENCE_REQUIRES_ADDITIONAL_INTENT_AND_EFFECT_EVIDENCE","counter":"BNP has a direct U.S.-system nexus; EU maintained JCPOA commitment and created countermeasures rather than simply conceding policy; private de-risking has business/compliance drivers.","gap":"No specific sovereign EU policy concession or representative success-rate denominator is causally closed.","gap_type":"CAUSALITY","limit":"Close legal reach, rail control and commercial adaptation separately from political coercion/success.","mechanism":"jurisdiction/monetary rail -> transaction or correspondent access -> rule/enforcement/secondary-sanctions risk -> bank/company compliance or de-risking -> access loss/commercial adaptation -> institutional countermeasure or policy effect","question":"When does control of dollar/correspondent rails become transnational leverage rather than ordinary territorial jurisdiction?","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"US-system nexus != pure extraterritoriality","status":"PASS","support":["FCT-001","FCT-002"]}
CTRL-002 | {"control":"secondary sanctions != individual enforcement order","status":"PASS","support":["FCT-006","FCT-010"]}
CTRL-003 | {"control":"enforcement risk != state command of each private exit","status":"PASS","support":["FCT-011","FCT-015"]}
CTRL-004 | {"control":"commercial withdrawal != sovereign policy concession","status":"PASS","support":["FCT-006","FCT-012","FCT-013"]}
CTRL-005 | {"control":"correspondent access != SWIFT monopoly","status":"PASS","support":["FCT-003","FCT-014","FCT-016"]}
CTRL-006 | {"control":"blocking statute != immunity from economic loss","status":"PASS","support":["FCT-009","FCT-011"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:14|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"EMPTY","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | MNEMO_UNAVAILABLE | mnemo | NONE | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.justice.gov/archives/opa/pr/bnp-paribas-agrees-plead-guilty-and-pay-89-billion-illegally-processing-financial | -
QRY-002 | FETCH | FOUND | SRC-002 | https://totalenergies.com/newsroom/us-withdrawal-jcpoa-totals-position-related-south-pars-11-project-iran/?lang=eng | -
QRY-003 | FETCH | FOUND | SRC-003 | https://finance.ec.europa.eu/eu-and-world/open-strategic-autonomy/extraterritoriality-blocking-statute_en | -
QRY-004 | FETCH | FOUND | SRC-004 | https://www.gov.uk/government/news/instex-successfully-concludes-first-transaction | -
QRY-005 | FETCH | FOUND | SRC-005 | https://www.eeas.europa.eu/node/61840_en | -
QRY-006 | FETCH | FOUND | SRC-006 | https://www.ecb.europa.eu/press/other-publications/ire/html/ecb.ire202506.en.html | -
QRY-007 | FETCH | FOUND | SRC-007 | https://home.treasury.gov/news/press-releases/tg829 | -
QRY-008 | FETCH | FOUND | SRC-008 | https://home.treasury.gov/news/press-releases/sm541 | -
QRY-009 | FETCH | FOUND | SRC-009 | https://home.treasury.gov/news/press-releases/sm804 | -
QRY-010 | FETCH | FOUND | SRC-010 | https://curia.europa.eu/panorama/2021/en/judicial-activity.html | -
QRY-011 | FETCH | FOUND | SRC-011 | https://home.treasury.gov/news/press-releases/sb0408 | -
QRY-012 | FETCH | FOUND | SRC-012 | https://www.europarl.europa.eu/doceo/document/E-8-2018-004184-ASW_EN.html | -
QRY-013 | FETCH | FOUND | SRC-013 | https://totalenergies.com/newsroom/iran-total-and-nioc-sign-contract-development-phase-11-giant-south-pars-gas-field/?lang=eng | -
QRY-014 | FETCH | FOUND | SRC-014 | https://www.eeas.europa.eu/node/62093_en | -

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | US-DOJ-BNP-2014 | US DOJ — BNP Paribas sanctions plea | 2014-06-30 | 2026-09-11T19:18:00Z | US-system nexus, dollar clearing, plea, penalties and one-year clearing suspension | https://www.justice.gov/archives/opa/pr/bnp-paribas-agrees-plead-guilty-and-pay-89-billion-illegally-processing-financial
SRC-002 | ◈ | fam:C | TOTAL-SP11-2018 | Total — US withdrawal from JCPOA and South Pars 11 | 2018-05-16 | 2026-09-11T19:18:00Z | secondary-sanctions exposure and project unwind | https://totalenergies.com/newsroom/us-withdrawal-jcpoa-totals-position-related-south-pars-11-project-iran/?lang=eng
SRC-003 | ◈ | fam:B | EC-BLOCKING-STATUTE | European Commission — Extraterritoriality / Blocking Statute | 2021-12-17 | 2026-09-11T19:18:00Z | EU rejection/mitigation of listed extraterritorial third-country laws | https://finance.ec.europa.eu/eu-and-world/open-strategic-autonomy/extraterritoriality-blocking-statute_en
SRC-004 | ◈ | fam:A | UK-INSTEX-FIRST | UK FCO — INSTEX successfully concludes first transaction | 2020-03-31 | 2026-09-11T19:18:00Z | first INSTEX transaction for medical goods | https://www.gov.uk/government/news/instex-successfully-concludes-first-transaction
SRC-005 | ◈ | fam:B | EEAS-JCPOA-2019 | EEAS/E3 — JCPOA statement and financial channels | 2019-05-04 | 2026-09-11T19:18:00Z | EU/E3 commitment to preserve financial channels and operationalise INSTEX | https://www.eeas.europa.eu/node/61840_en
SRC-006 | ◈ | fam:D | ECB-IRE-2025 | ECB — International role of the euro 2025 | 2025-06-01 | 2026-09-11T19:18:00Z | correspondent-banking retreat, compliance/reputational risk and sanctions | https://www.ecb.europa.eu/press/other-publications/ire/html/ecb.ire202506.en.html
SRC-007 | ◈ | fam:A | UST-CISADA-IFSR | US Treasury — Iranian Financial Sanctions Regulations fact sheet | 2010-08-16 | 2026-09-11T19:18:00Z | correspondent/payable-through account restrictions on foreign financial institutions | https://home.treasury.gov/news/press-releases/tg829
SRC-008 | ◈ | fam:A | UST-IRAN-2018 | US Treasury — full reimposition of Iran sanctions | 2018-11-05 | 2026-09-11T19:18:00Z | secondary exposure and correspondent-account sanctions | https://home.treasury.gov/news/press-releases/sm541
SRC-009 | ◈ | fam:A | UST-SECTION311-2019 | US Treasury — humanitarian mechanism / Section 311 Iran | 2019-10-25 | 2026-09-11T19:18:00Z | correspondent-account prohibition involving Iranian financial institutions | https://home.treasury.gov/news/press-releases/sm804
SRC-010 | ◈ | fam:E | CJEU-BANK-MELLI | CJEU — Bank Melli Iran v Telekom Deutschland C-124/20 | 2021-12-21 | 2026-09-11T19:18:00Z | EU Blocking Statute applies to US secondary sanctions even absent individual US instruction | https://curia.europa.eu/panorama/2021/en/judicial-activity.html
SRC-011 | ◈ | fam:A | FINCEN-MBAER-2026 | US Treasury/FinCEN — proposed severance of MBaer access | 2026-02-26 | 2026-09-11T19:18:00Z | current control point: correspondent-account access can be severed | https://home.treasury.gov/news/press-releases/sb0408
SRC-012 | ◈ | fam:B | EU-PARL-BLOCKING-ANSWER | European Parliament — Commission answer on Blocking Statute and Iran | 2018-11-06 | 2026-09-11T19:18:00Z | blocking-statute effects, EIB/financial-channel mitigation | https://www.europarl.europa.eu/doceo/document/E-8-2018-004184-ASW_EN.html
SRC-013 | ◈ | fam:C | TOTAL-SP11-2017 | Total — South Pars 11 contract with NIOC | 2017-07-03 | 2026-09-11T19:18:00Z | pre-sanctions baseline: project signed under then-applicable law | https://totalenergies.com/newsroom/iran-total-and-nioc-sign-contract-development-phase-11-giant-south-pars-gas-field/?lang=eng
SRC-014 | ◈ | fam:B | EEAS-JCPOA-2019-MAY | EEAS/E3 — joint statement on JCPOA and INSTEX | 2019-05-09 | 2026-09-11T19:18:00Z | continued European commitment despite US sanctions | https://www.eeas.europa.eu/node/62093_en

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.justice.gov/archives/opa/pr/bnp-paribas-agrees-plead-guilty-and-pay-89-billion-illegally-processing-financial | A | 2014-06-30 | BNP used US financial system | BNP Paribas admitted knowingly moving more than USD 8.8bn through the U.S. financial system on behalf of sanctioned entities; this closes a territorial/system nexus rather than a pure no-nexus extraterritorial case. | -
FCT-002 | FACT | ✧ | https://www.justice.gov/archives/opa/pr/bnp-paribas-agrees-plead-guilty-and-pay-89-billion-illegally-processing-financial | A | 2014-06-30 | BNP penalties and clearing suspension | The resolution provided about USD 8.97bn in penalties and a one-year suspension of certain U.S.-dollar clearing operations through the New York branch/affiliates for affected business lines. | -
FCT-003 | FACT | ✧ | https://home.treasury.gov/news/press-releases/tg829 | A | 2010-08-16 | Correspondent-account sanctions authority | CISADA/IFSR authorises strict conditions or prohibition on opening/maintaining U.S. correspondent or payable-through accounts for qualifying foreign financial institutions. | -
FCT-004 | FACT | ✧ | https://home.treasury.gov/news/press-releases/sm541 | A | 2018-11-05 | Secondary sanctions propagation | On reimposition of Iran sanctions, U.S. Treasury stated that foreign financial institutions facilitating significant transactions for covered Iranian persons could face U.S. correspondent/payable-through account sanctions. | -
FCT-005 | FACT | ✧ | https://totalenergies.com/newsroom/iran-total-and-nioc-sign-contract-development-phase-11-giant-south-pars-gas-field/?lang=eng | C | 2017-07-03 | Total pre-sanctions baseline | Total signed SP11 while stating compliance with applicable national and international law, establishing a before-state in which the project was pursued lawfully under the then-current framework. | -
FCT-006 | FACT | ✧ | https://totalenergies.com/newsroom/us-withdrawal-jcpoa-totals-position-related-south-pars-11-project-iran/?lang=eng | C | 2018-05-16 | Total unwind due secondary-sanctions risk | After the U.S. JCPOA withdrawal, Total stated it would unwind SP11 absent a U.S. waiver protecting it from secondary sanctions. | -
FCT-007 | FACT | ✧ | https://totalenergies.com/newsroom/us-withdrawal-jcpoa-totals-position-related-south-pars-11-project-iran/?lang=eng | C | 2018-05-16 | Total dollar-finance exposure | Total said more than 90% of its financing operations involved U.S. banks and identified loss of dollar financing, U.S. shareholders or U.S. operations as possible secondary-sanctions consequences. | -
FCT-008 | FACT | ✧ | https://finance.ec.europa.eu/eu-and-world/open-strategic-autonomy/extraterritoriality-blocking-statute_en | B | 2018-08-07 | EU Blocking Statute updated for Iran | The EU updated the Blocking Statute in 2018 to cover reimposed U.S. Iran measures it characterises as extraterritorial and to mitigate their effects on lawful EU trade. | -
FCT-009 | FACT | ✧ | https://finance.ec.europa.eu/eu-and-world/open-strategic-autonomy/extraterritoriality-blocking-statute_en | B | 2021-12-17 | Blocking Statute compliance prohibition | The Blocking Statute prohibits EU operators from complying with listed foreign requirements/prohibitions absent an authorised derogation and allows damage recovery/nullification mechanisms. | -
FCT-010 | FACT | ✧ | https://curia.europa.eu/panorama/2021/en/judicial-activity.html | E | 2021-12-21 | Bank Melli secondary-sanctions effect without individual order | The CJEU held that the EU prohibition on complying with U.S. secondary sanctions can be invoked even without a specific U.S. administrative or judicial instruction; Telekom had terminated services to Bank Melli. | -
FCT-011 | FACT | ✧ | https://curia.europa.eu/panorama/2021/en/judicial-activity.html | E | 2021-12-21 | Private risk calculus preserved | The CJEU required national courts to balance the Blocking Statute objective against the probability and extent of economic losses an EU operator could face if it could not terminate the relationship. | -
FCT-012 | FACT | ✧ | https://www.eeas.europa.eu/node/61840_en | B | 2019-05-04 | EU preservation of financial channels | EU/E3 statements committed to preserve financial channels and legitimate trade with Iran despite U.S. withdrawal and reimposed sanctions, including through INSTEX. | -
FCT-013 | FACT | ✧ | https://www.gov.uk/government/news/instex-successfully-concludes-first-transaction | A | 2020-03-31 | INSTEX first transaction | INSTEX completed its first transaction, facilitating European medical-goods exports to Iran; this proves an institutional workaround was actually used, though at bounded scale. | -
FCT-014 | FACT | ✧ | https://www.ecb.europa.eu/press/other-publications/ire/html/ecb.ire202506.en.html | D | 2025-06-01 | Correspondent banking is central infrastructure | ECB describes correspondent banking as central to cross-border payments; in 2022 there were about 90,000 active correspondents over 9,000 corridors, 20-30% fewer than a decade earlier. | -
FCT-015 | FACT | ✧ | https://www.ecb.europa.eu/press/other-publications/ire/html/ecb.ire202506.en.html | D | 2025-06-01 | Compliance/reputation contributes to correspondent retreat | ECB reports that one-fifth of surveyed banks cited higher compliance and reputational risks in terminating correspondent relationships and notes retrenchment after sanctions/enforcement episodes. | -
FCT-016 | FACT | ✧ | https://home.treasury.gov/news/press-releases/sm804 | A | 2019-10-25 | Section 311 correspondent-account prohibition | FinCEN prohibited opening or maintaining U.S. correspondent accounts for or on behalf of Iranian financial institutions and barred use of foreign-bank correspondent accounts to process such transactions. | -
FCT-017 | FACT | ✧ | https://home.treasury.gov/news/press-releases/sb0408 | A | 2026-02-26 | Current proposed severance control point | FinCEN proposed severing Swiss MBaer Merchant Bank from U.S. correspondent-account access, showing the control point remains operational in current policy; the cited action was proposed, not final. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-007
FCT-004 | SRC-008
FCT-005 | SRC-013
FCT-006 | SRC-002
FCT-007 | SRC-002
FCT-008 | SRC-003,SRC-012
FCT-009 | SRC-003
FCT-010 | SRC-010
FCT-011 | SRC-010
FCT-012 | SRC-005,SRC-014
FCT-013 | SRC-004
FCT-014 | SRC-006
FCT-015 | SRC-006
FCT-016 | SRC-009
FCT-017 | SRC-011

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

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:SEARCH
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:FACTS
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:CAUSAL_GAP
CP-004 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 | NEXT_ACTION:VERIFY
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:INVESTIGATION_ACCOUNTABILITY
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:FINALIZE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-11T19:17:13.204675+00:00","fact_mem":{},"mnemo_row":"MNEMO_UNAVAILABLE — local memory service not available; no memory ids fabricated.","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":17,"eligible":17,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_UNAVAILABLE — local memory service not available; no memory ids fabricated. | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:17;attempted:0;success:0;failure:0;blocked:17} | WRITEBACK_EXECUTION_V1:[17 rows, see section]

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
