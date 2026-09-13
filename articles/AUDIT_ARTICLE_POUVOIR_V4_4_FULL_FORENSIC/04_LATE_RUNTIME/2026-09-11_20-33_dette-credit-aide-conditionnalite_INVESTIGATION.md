ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260911-2033-dette-credit-aide-conditionnalite | PARENT_RUN_ID:NONE | AS_OF:2026-09-11
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/audit121/INV153_TRANSACTION_2026-09-11/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-11_dette-credit-aide-conditionnalite/2026-09-11_20-33_dette-credit-aide-conditionnalite_INPUT.txt | SUBJECT_SLUG:dette-credit-aide-conditionnalite | SUBJECT_FP:sha256:cef8389cc45a91d429aa29acc70364b24b9eb25a91ef03d0407bd6809f6723b1 | INPUT_SHA256:sha256:a685e2eab1738af1a7e866d50e316405aae33086186ed26484ac423dee8865fa
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/UE and directly relevant European comparators, 2010-2026; sovereign/institutional loans, RRF grants, MFA and IMF conditionality. Trace financing need -> instrument -> explicit condition -> prior action/milestone -> compliance -> disbursement -> reform/adaptation -> effect.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-153 — Dette, crédit, garanties et aide conditionnelle : quand le financement devient un levier de décision

## Verdict exécutif

Le run établit que la **conditionnalité financière est un mécanisme autonome de pouvoir**. Aucun passage par l'exposition, la persuasion ou le changement de croyance n'est nécessaire : un financement peut être rendu disponible seulement si des actions, lois, jalons ou critères convenus sont satisfaits.

Le contrôle positif le plus dense est le programme grec du Mécanisme européen de stabilité. La chaîne publique est fermée sur plusieurs séquences : besoin de financement → programme et Memorandum of Understanding → prior actions ou jalons → adoption de textes/réformes → contrôle de conformité → décaissement. La Commission documente notamment des actes législatifs et réglementaires adoptés pour compléter des prior actions requises avant une tranche, ainsi que des décaissements déclenchés après franchissement de jalons et revues.

Cette fermeture ne permet toutefois pas le raccourci `conditionnalité = coercition`. Les évaluations du programme grec décrivent une efficacité partielle, des coûts d'ajustement et des problèmes d'appropriation, mais elles ne démontrent pas que chaque réforme aurait été imposée contre une préférence politique grecque clairement établie ni que le financement serait la cause marginale unique de chaque réforme. La condition financière et le mécanisme de conformité sont donc prouvés plus fortement que le contrefactuel politique.

La France fournit un contrôle négatif utile. La Facilité pour la reprise et la résilience est elle aussi explicitement fondée sur des paiements conditionnés à l'atteinte de jalons et cibles de réforme ou d'investissement. La France a reçu des versements après validation de tels jalons, notamment en matière de dépenses publiques et de services de l'emploi. Cela démontre la généralité du mécanisme `argent → condition → vérification → paiement`, mais pas une ingérence ou une coercition par simple existence de la condition.

Le FMI et l'assistance macrofinancière de l'Union européenne montrent enfin que cette architecture dépasse le seul ESM : paiements par tranches, prior actions, critères quantitatifs et conditions structurelles constituent des instruments institutionnalisés. A contrario, le Pandemic Crisis Support du MES montre qu'un financement d'urgence peut être assorti d'une condition étroite d'usage sanitaire sans programme macroéconomique général. `Financement conditionnel` ne désigne donc pas une intensité unique de contrainte.

## 1. Le mécanisme minimal

La chaîne probatoire est :

```text
BESOIN DE FINANCEMENT
→ CRÉANCIER / PROGRAMME
→ INSTRUMENT
→ CONDITION EXPLICITE
→ PRIOR ACTION / JALON / CRITÈRE
→ ÉVALUATION DE CONFORMITÉ
→ DÉCAISSEMENT / NON-DÉCAISSEMENT
→ RÉFORME OU ADAPTATION
→ EFFET AVAL
```

Le maillon décisif est la relation documentée entre **condition, conformité et disponibilité de la ressource financière**. Une simple corrélation entre programme et réforme ne suffit pas.

## 2. Grèce : la conditionnalité devient observable dans les actes

Le MES décrit lui-même certains programmes comme du « cash-for-reforms » : les prêts sont associés à des réformes consignées dans un Memorandum of Understanding. Le suivi est assuré avec la Commission, la BCE et, selon les programmes, le FMI ; les décaissements ultérieurs sont liés à une évaluation positive de la mise en œuvre.

Dans le cas grec, la documentation de 2017 indique que des lois et actes réglementaires ont été adoptés pour compléter les prior actions nécessaires à la troisième tranche. La chronologie 2015 et les revues ultérieures relient également l'atteinte de jalons ou l'achèvement de revues à des décaissements identifiables. Ici, le mécanisme ne repose donc pas sur une hypothèse d'influence : la condition est écrite, l'action est observable, la conformité est évaluée et le paiement est conditionné.

Cette densité ne ferme pourtant pas le contrefactuel maximal. Les évaluations du programme grec signalent une efficacité partielle, des effets sociaux importants, des problèmes de design et d'appropriation. L'OCDE décrit des rythmes et effets hétérogènes selon les domaines de réforme. Le corpus ne permet donc pas de transformer une chaîne de conditionnalité contractuelle documentée en proposition générale selon laquelle chaque réforme aurait été imposée contre une préférence souveraine autrement inchangée.

## 3. France : même mécanique, qualification différente

La RRF est une infrastructure de financement fondée sur la performance : les paiements interviennent lorsque les jalons et cibles convenus sont jugés satisfaits. En France, un versement de 10,3 milliards d'euros en 2023 a suivi la validation de 55 jalons et cibles ; un versement de 3,26 milliards en 2025 a suivi la validation de 7 jalons et 10 cibles.

Ce contrôle interdit une erreur de catégorie. Si l'on qualifiait automatiquement toute relation `financement → jalons → paiement` de coercition ou d'ingérence, la même qualification devrait être appliquée sans distinction à des mécanismes budgétaires européens acceptés et co-gouvernés. La conditionnalité décrit ici une **architecture de décision et d'incitation** ; sa légitimité, son degré de contrainte et son éventuelle qualification d'ingérence requièrent d'autres preuves.

## 4. FMI et assistance macrofinancière : généralisation du mécanisme

Le FMI lie couramment les tranches de financement à des actions de politique publique, notamment des prior actions et des critères quantitatifs. L'assistance macrofinancière de l'Union européenne aux pays tiers ajoute des préconditions politiques et institutionnelles, puis attache les tranches à des conditions convenues pouvant viser finances publiques, commerce, restructuration d'entreprises, environnement des affaires ou secteur financier.

Le mécanisme de pouvoir est donc trans-institutionnel : la ressource financière est utilisée comme **variable conditionnelle**. Ce qui varie est la nature du contrat, le degré de besoin, la latitude de sortie, la légitimité du mandant, la symétrie de négociation, la portée des conditions et le coût du non-respect.

## 5. Ce que la conditionnalité n'établit pas seule

Le run conserve cinq séparations obligatoires :

```text
CONDITION != COERCITION
CONTRAT ACCEPTÉ != CONSENTEMENT SANS CONTRAINTE
RÉFORME RÉALISÉE != PRÉFÉRENCE TRANSFORMÉE
DÉCAISSEMENT != LÉGITIMITÉ
ASSOCIATION PROGRAMME/RÉFORME != CAUSALITÉ CONTREFACTUELLE
```

Pour passer de conditionnalité à coercition, il faut documenter au minimum une demande identifiable, des alternatives matériellement contraintes, une conséquence crédible du refus, l'exercice ou la menace crédible de cette conséquence et une adaptation reliée à cette contrainte. Pour passer ensuite à « ingérence », il faut encore établir la pertinence de l'origine, du mandat, de la relation de contrôle, de la légitimité de l'intervention et de la frontière institutionnelle affectée.

## 6. Gradient probatoire proposé

```text
FINANCEMENT NON CONDITIONNÉ
→ FINANCEMENT AFFECTÉ À UN USAGE
→ PAIEMENT CONDITIONNÉ À DES JALONS
→ CONDITIONNALITÉ DE RÉFORME
→ DÉPENDANCE FINANCIÈRE FORTE
→ MENACE / NON-DÉCAISSEMENT CRÉDIBLE
→ ADAPTATION SOUS CONTRAINTE
→ CONCESSION POLITIQUE CONTREFACTUELLEMENT IDENTIFIÉE
```

Les cas du run occupent plusieurs niveaux de ce gradient. Le Pandemic Crisis Support sert de contrôle à condition étroite ; la RRF ferme une conditionnalité de performance ; la Grèce ferme une conditionnalité macroéconomique forte avec prior actions et décaissements ; aucun de ces niveaux ne doit être automatiquement promu au dernier étage.

## 7. Gap terminal

Le run ne fournit pas de dénominateur représentatif permettant d'estimer, pour la France ou l'Union européenne, la fréquence à laquelle un financement conditionnel fait adopter une politique que le gouvernement cible n'aurait pas adoptée dans un scénario de préférence et de financement non contraints.

Ce manque n'annule pas le mécanisme documenté. Il borne sa généralisation : **la conditionnalité financière est prouvée comme levier de décision ; son degré de coercition et son effet politique contrefactuel restent dossier-spécifiques.**
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:0|EDI_DECISIVE:4|SRC_COMPLETE:14/14

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-11
- **breaks:**
  - 2015 Greek ESM programme
  - 2017 Greek second-review prior actions
  - 2021 RRF performance-based financing
  - 2023/2025 France RRF disbursements
  - 2026 RRF closure phase
- **status:** CURRENT
- **window:** 2010-2026; euro-area assistance, IMF conditionality, RRF, EU MFA

### MANIPULATION_REPORT
- **assumptions:**
  - qualification follows proved instrument/condition/action/compliance/disbursement/effect edges
- **clusters:**
  - POWER
  - MONEY
  - NETWORK
- **complexity:**
  - **band:** HIGH
  - **score:** 9
- **implicit:**
  - financial conditionality can change the option set directly without persuasion
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - conditionality=coercion
  - loan=command
  - reform=preference-change
  - disbursement=legitimacy
  - financial-need=loss-of-sovereignty
- **priorities:**
  - official programme documents
  - compliance/disbursement records
  - independent programme evaluation
  - negative controls
- **query_guidance:** separate financing need, explicit condition, policy action, compliance, payment, adaptation, coercion classification and counterfactual effect
- **rhetorical:**
  - NONE
- **speaker:** mechanism-first forensic investigation contract
- **symbol_stage:** FINAL
- **symbols:**
  - **ADAPTATION:** beneficiary response to financing conditions
  - **COERCION:** pressure that materially constrains alternatives to alter conduct
  - **COMPLIANCE:** institutional assessment that agreed conditions are met
  - **CONDITION:** explicit policy or use requirement attached to financing
  - **CONSENT:** formal acceptance distinct from unconstrained preference
  - **COUNTERFACTUAL:** what policy would have occurred absent the financing condition
  - **CREDITOR:** institution or programme controlling access to funds
  - **DISBURSEMENT:** release of a tranche or payment
  - **EFFECT:** downstream economic, institutional or political result
  - **FINANCING_NEED:** liquidity, balance-of-payments or recovery funding need
  - **INSTRUMENT:** loan, grant, guarantee or macro-financial assistance
  - **LEGITIMACY:** normative/legal evaluation distinct from causal leverage
  - **MILESTONE:** qualitative implementation step linked to payment
  - **PRIOR_ACTION:** action required before approval/review/disbursement
  - **REFORM:** legislative, administrative or economic policy change
- **threats:**
  - conditionality-to-coercion promotion
  - formal-consent-to-free-choice promotion
  - programme-reform causal overclaim
  - single-case prevalence extrapolation
  - not found=does not exist

### MODULE_EXECUTION
NONE

### SCOPING_REPORT
- **chain:**
  - financing need
  - instrument/creditor
  - explicit condition
  - prior action or milestone
  - compliance assessment
  - tranche/payment
  - reform/adaptation
  - effect
- **exclusions:**
  - ordinary market rates without conditions
  - generic debt burden without identifiable creditor condition
  - political disagreement unlinked to financing
- **object:** Debt, credit, guarantees and aid conditionality as decision levers
- **scope:** France/UE and European comparators 2010-2026

### CREDO
- condition != coercion
- contract accepted != unconstrained consent
- reform implemented != preference transformed
- disbursement != legitimacy
- programme association != counterfactual causality
- absence of coercion proof != absence of financial leverage

### COGNITIVE_MAP
- **causal_boundary:** financial leverage is closed at verified condition/action/payment linkage; coercion or ingérence requires separate evidence on autonomy, alternatives, mandate and political purpose
- **core_model:** conditional finance is a direct resource-to-policy mechanism: access to money may depend on specified actions and compliance, bypassing persuasion
- **rival_models:**
  - ordinary financing governance
  - jointly negotiated reform programme
  - domestically preferred reform financed by external funds
  - coercive leverage under acute liquidity constraints
  - creditor command without beneficiary agency
- **serial_effect:** INV-151 showed exercised resource coercion without closed concession; INV-153 tests formal finance where the requested actions are explicit.

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** transparent performance-based finance can condition payment without illegitimate coercion
  - **resolution:** separate condition/action/payment from coercion classification
  - **thesis:** conditional finance is coercion
- **item 2:**
  - **antithesis:** programme evaluation shows mixed ownership, partial effectiveness and heterogeneous reform effects
  - **resolution:** close prior-action -> law -> tranche; keep preference/counterfactual edge open
  - **thesis:** Greek reforms prove creditor command
- **item 3:**
  - **antithesis:** financing conditions can directly change available options and incentives
  - **resolution:** treat resource conditionality as an independent power branch
  - **thesis:** no persuasion means no influence

### RESOURCE_FLOW_MAP
- **item 1:**
  - **case:** Greece ESM 2015-2018
  - **flow:** acute financing need -> ESM programme/MoU -> prior actions and reforms -> compliance reviews -> tranches -> fiscal/structural adaptation
  - **status:** CONDITION_TO_ACTION_TO_DISBURSEMENT_SUPPORTED
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
    - FCT-004
    - FCT-005
    - FCT-006
    - FCT-016
- **item 2:**
  - **case:** France RRF
  - **flow:** EU grant envelope -> national plan milestones/targets -> Commission assessment -> payment -> reform/investment implementation
  - **status:** PERFORMANCE_BASED_CONDITIONALITY_WITHOUT_COERCION_PROOF
  - **support:**
    - FCT-011
    - FCT-012
    - FCT-013
- **item 3:**
  - **case:** EU MFA third countries
  - **flow:** balance-of-payments aid -> democratic/IMF preconditions + MoU conditions -> tranche release -> macro/structural reform
  - **status:** FORMAL_EXTERNAL_CONDITIONALITY
  - **support:**
    - FCT-014
    - FCT-015
- **item 4:**
  - **case:** ESM Pandemic Crisis Support
  - **flow:** credit line -> healthcare-use condition only
  - **status:** NARROW_CONDITION_NEGATIVE_CONTROL
  - **support:**
    - FCT-017

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** ESM/European institutions
  - **relation:** MoU conditionality, review and tranche decision
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
    - FCT-004
    - FCT-016
  - **to:** programme country
- **item 2:**
  - **from:** European Commission/RRF
  - **relation:** milestone/target assessment and payment
  - **support:**
    - FCT-011
    - FCT-012
    - FCT-013
  - **to:** France/member states
- **item 3:**
  - **from:** IMF
  - **relation:** prior actions/performance criteria and phased financing
  - **support:**
    - FCT-010
  - **to:** borrowing member
- **item 4:**
  - **from:** EU MFA
  - **relation:** democratic and macro/structural conditions
  - **support:**
    - FCT-014
    - FCT-015
  - **to:** partner countries

### IMPACT_MAP
- **downstream:** adds conditional finance as an independent branch of power over the policy choice set, distinct from persuasion, ownership and supply coercion
- **measured_objects:**
  - explicit loan/grant conditions
  - prior actions and legislation
  - milestone fulfilment
  - compliance assessment
  - tranche/payment release
  - programme economic/social outcomes
- **not_established:**
  - general creditor-command model
  - representative rate of coercive success
  - counterfactual preference change for each reform
  - automatic classification as ingérence

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** RRF and narrow-condition instruments show rule-based accepted conditionality
  - **issue:** conditionality=coercion
  - **pro:** funds can be withheld unless specified actions are completed
  - **resolution:** FINANCIAL_LEVERAGE_SUPPORTED; COERCION_SEPARATE
- **item 2:**
  - **contra:** evaluations show domestic agency, partial effectiveness, mixed ownership and heterogeneous effects
  - **issue:** Greece proves external command
  - **pro:** laws/prior actions were explicitly required for tranches
  - **resolution:** ACTION_AND_PAYMENT_EDGE_CLOSED; PREFERENCE_COUNTERFACTUAL_OPEN
- **item 3:**
  - **contra:** payment eligibility changes directly with compliance
  - **issue:** financial leverage needs persuasion
  - **pro:** policy changes can result from bargaining and beliefs
  - **resolution:** PERSUASION_NOT_REQUIRED_FOR_RESOURCE_CONDITIONALITY

### VERIFICATION_REPORT
- **checks:**
  - ESM cash-for-reforms design sourced
  - Greek prior-action legislation linked to tranche sourced
  - France RRF milestone-to-payment negative control sourced
  - IMF conditionality general mechanism sourced
  - MFA democratic/structural conditions sourced
  - Pandemic support narrow-condition negative control retained
  - programme outcomes not promoted into creditor-command counterfactual
- **status:** PASS_WITH_EXPLICIT_CAUSAL_LIMITS

### EDI_REPORT
- **corpus:** 14 accepted sources; EU/ESM official dominant with IMF and OECD independent lineages; repeated institutional pages are not counted as independent prevalence evidence
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim:** ESM condition-action-disbursement
    - **families:**
      - A
  - **item 2:**
    - **claim:** programme outcomes/ownership limits
    - **families:**
      - A
      - C
  - **item 3:**
    - **claim:** IMF general conditionality
    - **families:**
      - B
  - **item 4:**
    - **claim:** RRF control
    - **families:**
      - A
- **diagnostic_not_truth:** true
- **dimensions:**
  - ESM condition design
  - Greek prior actions
  - Greek tranche release
  - programme evaluation
  - IMF conditionality
  - France RRF negative control
  - MFA external conditionality
  - narrow-condition negative control
- **edi:** OFFICIAL_EU_ESM_DOMINANT_WITH_IMF_AND_OECD_CORROBORATION
- **source_counts:**
  - **A:** 12
  - **B:** 1
  - **C:** 1

### RESPONSIBILITY_MAP
- **item 1:**
  - **claim:** ESM conditionality and Greek disbursement
  - **owner:** ESM/European Commission and Greek authorities
  - **status:** SUPPORTED
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
    - FCT-004
    - FCT-005
    - FCT-006
    - FCT-016
- **item 2:**
  - **claim:** Greek programme outcomes and ownership limits
  - **owner:** ESM independent evaluation/OECD contribution
  - **status:** SUPPORTED_WITH_LIMITS
  - **support:**
    - FCT-007
    - FCT-008
    - FCT-009
- **item 3:**
  - **claim:** France RRF payment conditions
  - **owner:** European Commission
  - **status:** SUPPORTED
  - **support:**
    - FCT-011
    - FCT-012
    - FCT-013
- **item 4:**
  - **claim:** conditionality automatically equals coercion/ingérence
  - **owner:** INV-153 synthesis
  - **status:** REFUTED_AS_AUTOMATIC_EQUIVALENCE
  - **support:**
    - FCT-011
    - FCT-012
    - FCT-013
    - FCT-017

### NEXT_QUERIES
- **item 1:**
  - **query:** informal economic retaliation with attributable political demand -> sector cost -> policy adaptation
  - **route:** CANDIDATE_INV-154
  - **trigger:** post-INV153 reclassification
- **item 2:**
  - **query:** dollar/clearing/correspondent banking control with explicit extraterritorial demand and EU target adaptation
  - **route:** CANDIDATE_INV-152
  - **trigger:** post-INV153 reclassification; overlap guard INV-124
- **item 3:**
  - **query:** conditional finance general prevalence or coercion-success denominator
  - **route:** RECHECK
  - **trigger:** dataset or causal-design evidence

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-004,FCT-005,FCT-006,FCT-011,FCT-012,FCT-013,FCT-015 | final:GAP | gap:DENOMINATOR
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-001,FCT-002,FCT-010,FCT-014,FCT-015,FCT-016,FCT-017 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-004,FCT-005,FCT-006,FCT-012,FCT-013 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-001,FCT-003,FCT-005,FCT-006,FCT-011,FCT-012,FCT-013,FCT-015 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-007,FCT-008,FCT-009,FCT-011,FCT-012,FCT-013,FCT-017 | final:GAP | gap:COUNTERFACTUAL
CLM-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-009,QRY-010,QRY-013,SRC-001,SRC-002,SRC-003,SRC-009,SRC-010,SRC-013 | support:FCT-001,FCT-002,FCT-003,FCT-010,FCT-011,FCT-014,FCT-015 | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-010,FCT-011,FCT-014,FCT-015 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-014,SRC-001,SRC-002,SRC-003,SRC-004,SRC-005,SRC-014 | support:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-016 | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-016 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-004,QRY-005,SRC-004,SRC-005 | support:FCT-004,FCT-005,FCT-006 | counter:- | results:FCT-004,FCT-005,FCT-006 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-006,QRY-007,QRY-008,SRC-006,SRC-007,SRC-008 | support:- | counter:FCT-007,FCT-008,FCT-009 | results:FCT-007,FCT-008,FCT-009 | final:REFUTED | gap:COUNTERFACTUAL
CLM-005 | attempts:QRY-010,QRY-011,QRY-012,SRC-010,SRC-011,SRC-012 | support:FCT-011,FCT-012,FCT-013 | counter:- | results:FCT-011,FCT-012,FCT-013 | final:SUPPORTED | gap:NONE
CLM-006 | attempts:QRY-009,SRC-009 | support:FCT-010 | counter:- | results:FCT-010 | final:SUPPORTED | gap:NONE
CLM-007 | attempts:QRY-013,SRC-013 | support:FCT-014,FCT-015 | counter:- | results:FCT-014,FCT-015 | final:SUPPORTED | gap:NONE
CLM-008 | attempts:QRY-002,SRC-002 | support:- | counter:FCT-017 | results:FCT-017 | final:REFUTED | gap:SCOPE
CLM-009 | attempts:QRY-002,QRY-010,QRY-011,QRY-012,SRC-002,SRC-010,SRC-011,SRC-012 | support:- | counter:FCT-011,FCT-012,FCT-013,FCT-017 | results:FCT-011,FCT-012,FCT-013,FCT-017 | final:REFUTED | gap:CLASSIFICATION
CLM-010 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:- | final:GAP | gap:DENOMINATOR

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
AXS-004 | AXS | GAP | COUNTERFACTUAL | No representative counterfactual separates financing-induced policy change from jointly negotiated or domestically preferred reform across the population of programmes.
CLM-004 | CLM | REFUTED | COUNTERFACTUAL | Programme evaluations show mixed effectiveness, domestic ownership problems and heterogeneous reform effects; they do not establish a clean counterfactual for each reform.
CLM-008 | CLM | REFUTED | SCOPE | The ESM Pandemic Crisis Support instrument used a narrow healthcare-use condition without broader macroeconomic conditions.
CLM-009 | CLM | REFUTED | CLASSIFICATION | Classification requires separate evidence on mandate, transparency, alternatives, bargaining asymmetry, threat/penalty, intent and target autonomy.
CLM-010 | CLM | GAP | DENOMINATOR | No representative denominator or causal design for general prevalence/success.
CAU-001 | CAU | SUPPORTED | CAUSALITY | No general counterfactual separates reforms caused by financing pressure from reforms consistent with domestic or jointly negotiated policy preferences.

SEMANTIC_COUNTS_V1:LED:2|CLM:10|AXS:4|CAU:1|CTRL:5|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"evidence_excerpt":"Trace financing need -> instrument -> conditions -> prior actions/milestones -> compliance -> tranche -> reform/adaptation -> effect.","kind":"HYPOTHESIS","lead":"Conditional finance becomes a decision lever when access to funds is explicitly tied to policy actions, compliance is assessed, and disbursement depends on completion; coercion or interference requires additional evidence about mandate, alternatives, bargaining asymmetry and political purpose.","linked_ids":["CLM-001","CLM-002","CLM-003","CLM-004","CLM-005","CLM-006","CLM-007","CLM-008","CLM-009"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017"],"routes":["POWER","MONEY","NETWORK"],"source_id":"INV-153-RUN_CARD","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"evidence_excerpt":"Case evidence closes contractual conditionality and implementation more strongly than preference transformation or coercive success.","gap":"No representative denominator or general coercion-success rate in the bounded run.","gap_type":"DENOMINATOR","kind":"GAP","lead":"Representative denominator for conditional financing that materially changes policy against the target government’s unconstrained preference.","linked_ids":["CLM-010"],"locator":"GAP","materiality":"HIGH","result_ids":["FCT-004","FCT-005","FCT-006","FCT-011","FCT-012","FCT-013","FCT-015"],"routes":["RECHECK"],"source_id":"INV-153-RUN_CARD","status":"GAP"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Conditional financing is an autonomous mechanism of power because money can be made contingent on specified actions without any persuasion step.","claimant":"INV-153 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-010","FCT-011","FCT-014","FCT-015"]}
CLM-002 | {"claim":"ESM macroeconomic assistance closes a contractual chain condition -> prior action/reform -> compliance assessment -> tranche.","claimant":"INV-153 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-016"]}
CLM-003 | {"claim":"In Greece, specific legislative and administrative actions were adopted to complete prior actions required for ESM disbursement.","claimant":"INV-153 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-004","FCT-005","FCT-006"]}
CLM-004 | {"claim":"The Greek programmes prove that each reform was caused solely by external creditor pressure and was contrary to Greek policy preferences.","claimant":"strongest overclaim","counter":["FCT-007","FCT-008","FCT-009"],"gap":"Programme evaluations show mixed effectiveness, domestic ownership problems and heterogeneous reform effects; they do not establish a clean counterfactual for each reform.","gap_type":"COUNTERFACTUAL","materiality":"DECISIVE","status":"REFUTED","support":"NONE_FOUND"}
CLM-005 | {"claim":"France RRF payments demonstrate money-to-milestone/reform conditionality inside an accepted EU performance-based framework, but do not by themselves establish coercion or ingérence.","claimant":"INV-153 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-011","FCT-012","FCT-013"]}
CLM-006 | {"claim":"IMF lending institutionalises similar policy-action conditionality through prior actions, quantitative criteria and phased disbursement.","claimant":"INV-153 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-010"]}
CLM-007 | {"claim":"EU Macro-Financial Assistance to third countries can condition tranches on democratic preconditions and macroeconomic or structural reforms.","claimant":"INV-153 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-014","FCT-015"]}
CLM-008 | {"claim":"Every emergency credit instrument necessarily imposes broad policy conditionality.","claimant":"strongest overclaim","counter":["FCT-017"],"gap":"The ESM Pandemic Crisis Support instrument used a narrow healthcare-use condition without broader macroeconomic conditions.","gap_type":"SCOPE","materiality":"HIGH","status":"REFUTED","support":"NONE_FOUND"}
CLM-009 | {"claim":"Conditionality is automatically equivalent to coercion, corruption, capture or foreign interference.","claimant":"strongest overclaim","counter":["FCT-011","FCT-012","FCT-013","FCT-017"],"gap":"Classification requires separate evidence on mandate, transparency, alternatives, bargaining asymmetry, threat/penalty, intent and target autonomy.","gap_type":"CLASSIFICATION","materiality":"DECISIVE","status":"REFUTED","support":"NONE_FOUND"}
CLM-010 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"claim":"The corpus provides a representative France/EU rate at which conditional finance changes policy against the target government’s unconstrained preference.","claimant":"INV-153 denominator test","counter":"NONE_FOUND","gap":"No representative denominator or causal design for general prevalence/success.","gap_type":"DENOMINATOR","materiality":"HIGH","status":"GAP","support":"NONE_FOUND"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"axis":"CONDITION_SPECIFICITY","links":["CLM-001","CLM-002","CLM-006","CLM-007","CLM-008"],"question":"Are financing conditions explicit and linked to an identified instrument?","result_ids":["FCT-001","FCT-002","FCT-010","FCT-014","FCT-015","FCT-016","FCT-017"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"axis":"POLICY_ACTION","links":["CLM-002","CLM-003","CLM-005"],"question":"Did the beneficiary actually adopt prior actions, laws, milestones or reforms required by the instrument?","result_ids":["FCT-004","FCT-005","FCT-006","FCT-012","FCT-013"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"axis":"DISBURSEMENT_LINK","links":["CLM-002","CLM-005","CLM-006","CLM-007"],"question":"Was payment or tranche release dependent on verified completion?","result_ids":["FCT-001","FCT-003","FCT-005","FCT-006","FCT-011","FCT-012","FCT-013","FCT-015"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"axis":"COERCION_COUNTERFACTUAL","gap":"No representative counterfactual separates financing-induced policy change from jointly negotiated or domestically preferred reform across the population of programmes.","gap_type":"COUNTERFACTUAL","links":["CLM-004","CLM-005","CLM-008","CLM-009","CLM-010"],"question":"Does conditionality establish coercion, preference change or interference rather than negotiated/performance-based finance?","result_ids":["FCT-007","FCT-008","FCT-009","FCT-011","FCT-012","FCT-013","FCT-017"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"GAP"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"CONDITION_PLUS_COMPLIANCE_PLUS_DISBURSEMENT closes financial leverage; COERCION/INGERENCE is a separate qualification.","counter":"RRF France and narrow-condition Pandemic Crisis Support show that conditionality can be transparent, rule-based and accepted without proving coercion; Greece evaluations show mixed ownership/effects rather than a single creditor-command model.","gap":"No general counterfactual separates reforms caused by financing pressure from reforms consistent with domestic or jointly negotiated policy preferences.","gap_type":"CAUSALITY","limit":"Coercion or ingérence requires evidence beyond the payment condition itself: constrained alternatives, attributable demand, material penalty/non-payment and a policy change causally tied to that pressure.","mechanism":"financing need -> creditor/programme -> explicit conditions -> prior actions/milestones -> compliance assessment -> tranche/release -> reform/adaptation -> downstream effect","question":"When does debt, credit, aid or guarantee conditionality become a material decision lever rather than ordinary financing governance?","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"condition != coercion","status":"PASS","support":["FCT-011","FCT-012","FCT-013","FCT-017"]}
CTRL-002 | {"control":"contract accepted != unconstrained consent","status":"PASS","support":["FCT-001","FCT-002","FCT-016"]}
CTRL-003 | {"control":"reform implemented != preference transformed","status":"PASS","support":["FCT-004","FCT-008","FCT-009"]}
CTRL-004 | {"control":"disbursement != legitimacy","status":"PASS","support":["FCT-003","FCT-005","FCT-011"]}
CTRL-005 | {"control":"programme association != counterfactual causality","status":"PASS","support":["FCT-007","FCT-008","FCT-009"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:14|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"EMPTY","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | MNEMO_UNAVAILABLE | mnemo | NONE | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.esm.europa.eu/financial-assistance/programme-database/conditionality | -
QRY-002 | FETCH | FOUND | SRC-002 | https://www.esm.europa.eu/financial-assistance/lending-toolkit | -
QRY-003 | FETCH | FOUND | SRC-003 | https://www.esm.europa.eu/content/how-conditionality-monitored-during-esm-programme | -
QRY-004 | FETCH | FOUND | SRC-004 | https://economy-finance.ec.europa.eu/document/download/a632c4c1-5f68-465a-9f8e-4b56708b49e3_en?filename=compliance_report-to_ewg_2017_06_21.pdf | -
QRY-005 | FETCH | FOUND | SRC-005 | https://economy-finance.ec.europa.eu/eu-financial-assistance/euro-area-countries/financial-assistance-greece_en | -
QRY-006 | FETCH | FOUND | SRC-006 | https://www.esm.europa.eu/press-releases/programme-evaluation-greece-published-today | -
QRY-007 | FETCH | FOUND | SRC-007 | https://www.esm.europa.eu/news/explainer-evaluation-financial-assistance-greece | -
QRY-008 | FETCH | FOUND | SRC-008 | https://www.esm.europa.eu/publications/oecd-contribution-evaluation-esm-financial-assistance-programme-greece | -
QRY-009 | FETCH | FOUND | SRC-009 | https://www.imf.org/en/about/factsheets/sheets/2023/imf-conditionality | -
QRY-010 | FETCH | FOUND | SRC-010 | https://reforms-investments.ec.europa.eu/recovery-and-resilience-facility-1/rrf-how-it-works_en | -
QRY-011 | FETCH | FOUND | SRC-011 | https://france.representation.ec.europa.eu/informations-et-evenements/informations/la-france-et-la-belgique-recoivent-de-nouveaux-paiements-au-titre-de-la-facilite-de-lue-pour-la-2025-05-27_fr | -
QRY-012 | FETCH | FOUND | SRC-012 | https://france.representation.ec.europa.eu/informations-et-evenements/informations/la-commission-verse-un-deuxieme-versement-de-103-milliards-deuros-la-france-au-titre-de-la-facilite-2023-12-22_fr | -
QRY-013 | FETCH | FOUND | SRC-013 | https://economy-finance.ec.europa.eu/eu-financial-assistance/macro-financial-assistance-mfa_en | -
QRY-014 | FETCH | FOUND | SRC-014 | https://www.esm.europa.eu/press-releases/esm-board-governors-approves-decision-grant-principle-stability-support-greece | -

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | ESM-CONDITIONALITY-DASHBOARD | ESM — Conditionality dashboard | 2026-09-11 | 2026-09-11T18:33:00Z | MoU conditions; reviews; further disbursements only after positive compliance assessment | https://www.esm.europa.eu/financial-assistance/programme-database/conditionality
SRC-002 | ◈ | fam:A | ESM-LENDING-TOOLKIT | ESM — Financial assistance instruments / lending toolkit | 2026-09-11 | 2026-09-11T18:33:00Z | cash-for-reforms; loan instruments; disbursement linked to reforms | https://www.esm.europa.eu/financial-assistance/lending-toolkit
SRC-003 | ◈ | fam:A | ESM-CONDITIONALITY-MONITORING | ESM — How conditionality is monitored | 2026-09-11 | 2026-09-11T18:33:00Z | reviews by institutions; disbursement only after positive reform assessment | https://www.esm.europa.eu/content/how-conditionality-monitored-during-esm-programme
SRC-004 | ◈ | fam:A | EC-GREECE-COMPLIANCE-2017-06-21 | European Commission — Greece compliance report, second review | 2017-06-21 | 2026-09-11T18:33:00Z | Greek legislative prior actions tied to third tranche | https://economy-finance.ec.europa.eu/document/download/a632c4c1-5f68-465a-9f8e-4b56708b49e3_en?filename=compliance_report-to_ewg_2017_06_21.pdf
SRC-005 | ◈ | fam:A | EC-GREECE-FINANCIAL-ASSISTANCE | European Commission — Financial assistance to Greece | 2026-09-11 | 2026-09-11T18:33:00Z | milestones, prior actions and disbursement chronology 2015-2018 | https://economy-finance.ec.europa.eu/eu-financial-assistance/euro-area-countries/financial-assistance-greece_en
SRC-006 | ◈ | fam:A | ESM-GREECE-EVAL-PRESS | ESM — Programme evaluation on Greece published | 2020-06-11 | 2026-09-11T18:33:00Z | 203.8bn ESM/EFSF loans; stabilisation and adjustment costs | https://www.esm.europa.eu/press-releases/programme-evaluation-greece-published-today
SRC-007 | ◈ | fam:A | ESM-GREECE-EVAL-EXPLAINER | ESM — Explainer: Evaluation of Financial Assistance to Greece | 2020-06-11 | 2026-09-11T18:33:00Z | partial effectiveness, unintended consequences, reform ownership limits | https://www.esm.europa.eu/news/explainer-evaluation-financial-assistance-greece
SRC-008 | ◈ | fam:C | OECD-GREECE-REFORMS | OECD contribution to ESM Greece evaluation | 2020-06-11 | 2026-09-11T18:33:00Z | empirical assessment of labour/product/public-sector reforms and effects | https://www.esm.europa.eu/publications/oecd-contribution-evaluation-esm-financial-assistance-programme-greece
SRC-009 | ◈ | fam:B | IMF-CONDITIONALITY | IMF — Conditionality factsheet | 2026-09-11 | 2026-09-11T18:33:00Z | instalments linked to policy actions; prior actions and quantitative criteria | https://www.imf.org/en/about/factsheets/sheets/2023/imf-conditionality
SRC-010 | ◈ | fam:A | EC-RRF-HOW-IT-WORKS | European Commission — RRF: How it works | 2026-09-11 | 2026-09-11T18:33:00Z | performance-based payments after milestones and targets | https://reforms-investments.ec.europa.eu/recovery-and-resilience-facility-1/rrf-how-it-works_en
SRC-011 | ◈ | fam:A | EC-FR-RRF-2025-05-27 | European Commission Representation France — France fourth RRF payment | 2025-05-27 | 2026-09-11T18:33:00Z | 3.26bn payment after 7 milestones and 10 targets | https://france.representation.ec.europa.eu/informations-et-evenements/informations/la-france-et-la-belgique-recoivent-de-nouveaux-paiements-au-titre-de-la-facilite-de-lue-pour-la-2025-05-27_fr
SRC-012 | ◈ | fam:A | EC-FR-RRF-2023-12-22 | European Commission Representation France — France second RRF payment | 2023-12-22 | 2026-09-11T18:33:00Z | 10.3bn payment after 55 milestones and targets | https://france.representation.ec.europa.eu/informations-et-evenements/informations/la-commission-verse-un-deuxieme-versement-de-103-milliards-deuros-la-france-au-titre-de-la-facilite-2023-12-22_fr
SRC-013 | ◈ | fam:A | EC-MFA | European Commission — Macro-Financial Assistance | 2026-09-11 | 2026-09-11T18:33:00Z | MFA preconditions; IMF link; tranches tied to macro/structural conditions | https://economy-finance.ec.europa.eu/eu-financial-assistance/macro-financial-assistance-mfa_en
SRC-014 | ◈ | fam:A | ESM-GREECE-2015-07-17 | ESM — Greece stability support approved in principle | 2015-07-17 | 2026-09-11T18:33:00Z | loan support subject to negotiated MoU policy conditionality | https://www.esm.europa.eu/press-releases/esm-board-governors-approves-decision-grant-principle-stability-support-greece

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.esm.europa.eu/financial-assistance/programme-database/conditionality | A | 2026-09-11 | Conditionality and disbursement | The ESM provides assistance on condition that beneficiary countries adjust policies; further disbursements are made only after positive assessment of reform implementation. | -
FCT-002 | FACT | ✧ | https://www.esm.europa.eu/financial-assistance/lending-toolkit | A | 2026-09-11 | Cash-for-reforms design | The ESM describes macroeconomic-adjustment lending as cash-for-reforms: members receive loans in exchange for reforms detailed in a Memorandum of Understanding. | -
FCT-003 | FACT | ✧ | https://www.esm.europa.eu/content/how-conditionality-monitored-during-esm-programme | A | 2026-09-11 | Conditionality monitoring | ESM, Commission and ECB, with IMF where applicable, monitor agreed reforms; disbursement can occur only after a positive reform-performance assessment. | -
FCT-004 | FACT | ✧ | https://economy-finance.ec.europa.eu/document/download/a632c4c1-5f68-465a-9f8e-4b56708b49e3_en?filename=compliance_report-to_ewg_2017_06_21.pdf | A | 2017-06-21 | Greek legislative prior actions | The Commission reported that Greek authorities adopted laws and secondary legislation to complete prior actions required for the third tranche of the ESM programme. | -
FCT-005 | FACT | ✧ | https://economy-finance.ec.europa.eu/eu-financial-assistance/euro-area-countries/financial-assistance-greece_en | A | 2015-12-01 | Greek milestone-linked disbursements | The Commission records that achievement of milestone sets in October and December 2015 led respectively to further ESM disbursements of EUR 2 billion and EUR 1 billion. | -
FCT-006 | FACT | ✧ | https://economy-finance.ec.europa.eu/eu-financial-assistance/euro-area-countries/financial-assistance-greece_en | A | 2018-08-20 | Greek later-review disbursements | Completion of the third and fourth reviews unlocked EUR 21.7 billion of ESM financing between March and August 2018. | -
FCT-007 | FACT | ✧ | https://www.esm.europa.eu/press-releases/programme-evaluation-greece-published-today | A | 2020-06-11 | Scale and stabilisation of Greek assistance | The ESM evaluation states that ESM/EFSF disbursed EUR 203.8 billion in loans to Greece and that support helped keep Greece in the euro area and supported stabilisation and growth, while adjustment imposed substantial costs. | -
FCT-008 | FACT | ✧ | https://www.esm.europa.eu/news/explainer-evaluation-financial-assistance-greece | A | 2020-06-11 | Partial effectiveness and side effects | The ESM evaluation explainer describes the Greek programmes as partially effective, notes unintended consequences including unemployment and brain drain, and records weaknesses in reform ownership and programme design. | -
FCT-009 | FACT | ✧ | https://www.esm.europa.eu/publications/oecd-contribution-evaluation-esm-financial-assistance-programme-greece | C | 2020-06-11 | Reform effects were heterogeneous | The OECD contribution found product-market reforms slow and piecemeal relative to labour-market restructuring and identified mixed economic and social effects across reform domains. | -
FCT-010 | FACT | ✧ | https://www.imf.org/en/about/factsheets/sheets/2023/imf-conditionality | B | 2026-09-11 | IMF conditionality mechanics | The IMF states that most financing is paid in instalments linked to demonstrable policy actions, including prior actions and quantitative performance criteria. | -
FCT-011 | FACT | ✧ | https://reforms-investments.ec.europa.eu/recovery-and-resilience-facility-1/rrf-how-it-works_en | A | 2026-09-11 | RRF performance-based mechanism | The Recovery and Resilience Facility pays Member States when agreed milestones and targets for reforms and investments are satisfactorily fulfilled. | -
FCT-012 | FACT | ✧ | https://france.representation.ec.europa.eu/informations-et-evenements/informations/la-france-et-la-belgique-recoivent-de-nouveaux-paiements-au-titre-de-la-facilite-de-lue-pour-la-2025-05-27_fr | A | 2025-05-27 | France fourth RRF payment | France received EUR 3.26 billion in grants after positive assessment of 7 milestones and 10 targets covering investments and reforms, including quality of public spending. | -
FCT-013 | FACT | ✧ | https://france.representation.ec.europa.eu/informations-et-evenements/informations/la-commission-verse-un-deuxieme-versement-de-103-milliards-deuros-la-france-au-titre-de-la-facilite-2023-12-22_fr | A | 2023-12-22 | France second RRF payment | France received EUR 10.3 billion after fulfilling 55 milestones and targets linked to reforms and investments including public finances and employment services. | -
FCT-014 | FACT | ✧ | https://economy-finance.ec.europa.eu/eu-financial-assistance/macro-financial-assistance-mfa_en | A | 2026-09-11 | MFA entry preconditions | EU Macro-Financial Assistance requires respect for democratic mechanisms and rule of law, an IMF credit arrangement and a satisfactory track record of IMF-programme reforms. | -
FCT-015 | FACT | ✧ | https://economy-finance.ec.europa.eu/eu-financial-assistance/macro-financial-assistance-mfa_en | A | 2026-09-11 | MFA tranche conditionality | MFA tranches are strictly tied to conditions in an EU-beneficiary Memorandum of Understanding and may cover public finance, trade, enterprise restructuring, business environment and financial-sector reform. | -
FCT-016 | FACT | ✧ | https://www.esm.europa.eu/press-releases/esm-board-governors-approves-decision-grant-principle-stability-support-greece | A | 2015-07-17 | Greece 2015 support and MoU | The ESM Board approved stability support to Greece in principle and stated that the next step was negotiation of a MoU detailing policy conditionality linked to the financial assistance facility. | -
FCT-017 | FACT | ✧ | https://www.esm.europa.eu/financial-assistance/lending-toolkit | A | 2026-09-11 | Narrow-condition negative control | The ESM Pandemic Crisis Support instrument required healthcare-related use of funds but no additional macroeconomic policy conditions, showing that financing instruments can carry narrow rather than broad conditionality. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-003
FCT-004 | SRC-004
FCT-005 | SRC-005
FCT-006 | SRC-005
FCT-007 | SRC-006
FCT-008 | SRC-007
FCT-009 | SRC-008
FCT-010 | SRC-009
FCT-011 | SRC-010
FCT-012 | SRC-011
FCT-013 | SRC-012
FCT-014 | SRC-013
FCT-015 | SRC-013
FCT-016 | SRC-014
FCT-017 | SRC-002

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
ATTEMPT-001 | {"created_at":"2026-09-11T18:48:41.015137+00:00","fact_mem":{},"mnemo_row":"MNEMO_UNAVAILABLE — local memory service not available; no memory ids fabricated.","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":17,"eligible":17,"failure":0,"success":0}}

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
