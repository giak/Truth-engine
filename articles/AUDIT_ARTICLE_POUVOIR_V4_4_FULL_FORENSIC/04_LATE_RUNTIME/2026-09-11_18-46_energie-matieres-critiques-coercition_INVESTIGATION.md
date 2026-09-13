ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260911-1846-energie-matieres-critiques-coercition | PARENT_RUN_ID:NONE | AS_OF:2026-09-11
INPUT_KIND:RUN_CARD | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/audit121/INV151_TRANSACTION_2026-09-11/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-11_energie-matieres-critiques-coercition/2026-09-11_18-46_energie-matieres-critiques-coercition_INPUT.txt | SUBJECT_SLUG:energie-matieres-critiques-coercition | SUBJECT_FP:sha256:8e8b7a2215dab1b7c0d8a08ebe454548fc8407444400dace4c075d7fb5750c9d | INPUT_SHA256:sha256:462d5a5a75b5921c9b3acd9d471d9a19e795f2bd72d5edb0fb6c2a3121b58c91
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/UE 2006-2026; gaz, uranium, terres rares et matières critiques. Trace fournisseur/État -> dépendance -> point de contrôle -> restriction/menace/condition -> coût/rupture -> adaptation -> concession/décision éventuelle -> effet.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-151 — Énergie, matières critiques et dépendances d’approvisionnement comme leviers de coercition

## Verdict exécutif

Le run ferme un mécanisme plus exigeant que `dépendance = coercition`. Une dépendance économique devient un levier de coercition lorsque quatre objets peuvent être séparément établis : **un point de contrôle réel sur un flux difficilement substituable ; une restriction, condition, menace ou coupure imputable à l’acteur qui contrôle ce point ; un coût matériel pour la cible ; puis une adaptation ou décision observable de cette cible**. La concession politique terminale est un objet supplémentaire et ne doit pas être déduite de l’adaptation.

Le gaz russe en 2022 est le contrôle positif le plus net du corpus. L’Union dépendait de la Russie pour environ 45 % de ses importations de gaz en 2021. Après l’invasion de l’Ukraine et les sanctions européennes, la Russie a tenté d’imposer un paiement en roubles aux acheteurs européens ; Gazprom a interrompu les livraisons à la Pologne et à la Bulgarie après leur refus. La Commission et le Conseil ont ensuite qualifié la réduction graduelle des flux de **weaponisation** de l’énergie. Les volumes russes ont chuté, le prix de gros du gaz a dépassé 300 €/MWh à la fin août 2022 et les secteurs énergivores ont réduit leur demande. [FCT-001] [FCT-002] [FCT-003] [FCT-004]

La chaîne fermée est donc :

```text
DÉPENDANCE ÉLEVÉE
-> CONDITION DE PAIEMENT / RÉDUCTION DE FLUX / COUPURE
-> TENSION D'APPROVISIONNEMENT ET CHOC DE PRIX
-> STOCKAGE / DIVERSIFICATION / BAISSE DE DEMANDE / INFRASTRUCTURES
-> RÉDUCTION STRUCTURELLE DE LA DÉPENDANCE
```

Elle ne ferme pas `coupure -> concession politique à Moscou`. L’Union a au contraire renforcé le stockage, diversifié les importations, lancé REPowerEU, réduit la part russe puis adopté en 2026 une interdiction progressive des importations de gaz russe. [FCT-005] [FCT-006] [FCT-007]

## 1. Gaz russe : une coercition peut être réelle sans obtenir la concession recherchée

Le cas Pologne/Bulgarie ferme l’arête la plus difficile à distinguer d’un choc de marché : la coupure n’est pas une panne ni une hausse spontanée. L’agence exécutive européenne CINEA rapporte que Gazprom a interrompu l’approvisionnement après le refus des deux États de payer en roubles, sur décision du président russe. L’IEA décrit la tentative russe d’imposer un système de paiement en roubles comme une mesure ayant conduit à des coupures unilatérales et à des sanctions russes contre certains acheteurs. [FCT-002]

La Commission documente ensuite l’extension du mécanisme. Au troisième trimestre 2022, elle décrit la weaponisation des exportations de gaz russes comme le facteur dominant du marché, avec réduction progressive des volumes Nord Stream 1 ; les importations russes par gazoduc du trimestre ont diminué de 74 % sur un an et celles via Nord Stream 1 de 85 %. Le prix de gros a dépassé 300 €/MWh à la fin août et la contraction de la demande a été particulièrement forte dans l’industrie énergivore. [FCT-003] [FCT-004]

Ce résultat oblige à séparer **succès du levier** et **succès politique**. Le levier a réussi à imposer des coûts et à modifier l’architecture énergétique européenne. Mais le corpus ne montre pas que l’Union ait annulé ses sanctions, modifié sa politique ukrainienne ou accepté durablement la condition de paiement en échange du rétablissement des flux. `COERCION_EFFECTIVE_ON_COSTS != POLITICAL_CONCESSION_PROVEN`.

## 2. L’adaptation européenne est elle-même un effet politique mesurable

En juin 2022, le Conseil a adopté l’obligation de remplir les stockages avant l’hiver, avec un objectif d’au moins 80 % pour l’hiver 2022-2023 puis 90 % les hivers suivants. La Commission montre qu’entre 2021 et 2024 les importations de gaz russe sont passées de 150 à 52 milliards de mètres cubes et que leur part est passée de 45 % à 19 %. [FCT-005] [FCT-006]

Le processus ne s’est pas arrêté à une adaptation conjoncturelle. En janvier 2026, le Conseil a donné son feu vert définitif à l’interdiction progressive du gaz russe, avec extinction graduelle des contrats existants jusqu’en 2027. La page actuelle du Conseil indique que la part russe dans les importations de gaz de l’Union avait déjà chuté de 45 % en 2021 à 13 % en 2025. [FCT-007]

Il serait toutefois trop fort d’écrire `weaponisation russe -> règlement 2026` comme une causalité monocausale. La guerre, les sanctions, les objectifs climatiques, les stratégies d’autonomie et les choix nationaux contribuent aussi à cette trajectoire. La conclusion soutenue est plus bornée : **l’exercice du levier énergétique russe a rendu la dépendance matériellement coûteuse et a accéléré une architecture explicite de résilience et de sortie**.

## 3. Matières critiques : de l’exposition au contrôle d’exportation exercé

Le précédent chinois sur les terres rares apporte un contrôle historique utile. En 2012, l’Union a contesté devant l’OMC des droits, quotas, licences et autres restrictions chinoises à l’exportation de terres rares, tungstène et molybdène. Le groupe spécial a conclu que certaines restrictions violaient les obligations de la Chine et que les quotas poursuivaient des objectifs de politique industrielle plutôt que le motif de conservation invoqué. En mai 2015, la Chine a indiqué avoir supprimé les droits, quotas et restrictions de droits commerciaux jugés incompatibles. [FCT-008] [FCT-009] [FCT-010]

Ce cas ferme donc `contrôle du flux -> restriction d’exportation -> contentieux institutionnel -> modification des mesures`. Il ne prouve pas que chaque restriction contemporaine sur un minerai critique soit une coercition politique dirigée contre l’Union.

Depuis 2023, le risque est redevenu concret. Un brief de la Commission recense des contrôles chinois sur le gallium, le germanium et le graphite et indique que les restrictions sur le gallium et le germanium apparaissent en partie comme des réactions aux restrictions néerlandaises sur les machines de lithographie. En avril 2025, la Chine a instauré de nouveaux contrôles sur sept terres rares lourdes et leurs aimants ; l’IEA constate que la baisse des exportations a forcé certains constructeurs automobiles en Europe et ailleurs à réduire leurs taux d’utilisation ou à suspendre temporairement leur production. [FCT-011] [FCT-012]

La chaîne économique est donc fermée jusqu’au coût industriel :

```text
CONCENTRATION D'APPROVISIONNEMENT
-> LICENCE / CONTRÔLE D'EXPORTATION
-> RETARD / BAISSE DE DISPONIBILITÉ
-> SURCOÛT / RÉDUCTION DE PRODUCTION
-> DIVERSIFICATION / POLITIQUE DE RÉSILIENCE
```

Mais le corpus ne ferme pas une concession politique européenne spécifique obtenue en contrepartie de ces restrictions. L’intention peut être géopolitique ou de politique industrielle ; elle doit rester qualifiée dossier par dossier.

## 4. Le Critical Raw Materials Act traite la dépendance comme un risque, pas comme une preuve d’ingérence

La dépendance européenne reste matérielle. Eurostat indique que 46,8 % des importations européennes de terres rares en 2025 provenaient de Chine ; pour les aimants permanents, la concentration industrielle mondiale est encore plus forte. [FCT-013]

Le Critical Raw Materials Act transforme ce risque en politiques de diversification : au moins 10 % d’extraction dans l’Union, 40 % de transformation, 25 % de recyclage et pas plus de 65 % de consommation annuelle d’une matière stratégique provenant d’un seul pays tiers à un stade pertinent de transformation. Il prévoit aussi suivi des chaînes, stress tests, coordination des stocks stratégiques et obligations de préparation pour certaines grandes entreprises. [FCT-014]

Ces dispositifs ferment `dépendance identifiée -> architecture de résilience`. Ils ne permettent pas de déduire rétrospectivement qu’une puissance étrangère a déjà exercé une coercition sur chaque matière concernée. C’est précisément la différence entre **vulnérabilité** et **levier exercé**.

## 5. Uranium russe : contrôle négatif d’une dépendance sans coupure démontrée

Le nucléaire fournit le meilleur contrôle négatif du run. En 2025, la Russie représente encore 15,98 % de l’uranium naturel livré aux électriciens européens et 22,55 % des services d’enrichissement. L’Agence d’approvisionnement d’Euratom indique que les électriciens européens ont constitué des stocks depuis le début de la guerre afin de réduire le risque de perturbation et que les réacteurs VVER restent particulièrement vulnérables à une dépendance fournisseur unique, malgré les efforts de diversification. [FCT-015] [FCT-016] [FCT-017]

Cette exposition est importante, mais le run n’identifie pas une coupure russe d’uranium ou d’enrichissement utilisée contre l’Union comme condition politique analogue au gaz de 2022. Il serait donc faux de transférer mécaniquement le statut `COERCION_EXERCISED` du gaz au nucléaire. `DEPENDENCY != EXERCISED_LEVERAGE` reste la garde centrale.

## 6. Modèle causal et borne finale

Le mécanisme général qui survit au corpus est :

```text
FOURNISSEUR / ÉTAT / ENTREPRISE
-> CONCENTRATION / DÉPENDANCE DE FLUX
-> POINT DE CONTRÔLE RÉEL
-> RESTRICTION / CONDITION / COUPURE / MENACE
-> COÛT / PÉNURIE / RISQUE DE CONTINUITÉ
-> ADAPTATION
-> CONCESSION OU DÉCISION ÉVENTUELLE
-> EFFET
```

Trois statuts doivent rester séparés :

- **EXPOSITION** : dépendance ou concentration, sans exercice du levier ;
- **COERCITION ÉCONOMIQUE EXERCÉE** : restriction/condition/coupure imputable produisant un coût ou une adaptation ;
- **COERCITION POLITIQUEMENT RÉUSSIE** : la cible adopte la concession recherchée, avec chaîne causale suffisamment fermée.

Le gaz russe ferme le deuxième statut et documente une adaptation européenne massive, mais ne ferme pas le troisième. Les terres rares chinoises ferment plusieurs restrictions et effets industriels ainsi que des réponses institutionnelles, mais la concession politique européenne reste ouverte. L’uranium russe ferme une vulnérabilité et des mesures préventives, pas un exercice de coercition dans le run borné.

## Bornes

- `dependency != coercion` ;
- `supply interruption != political intent` ;
- `price shock != coercion` ;
- `export control != political concession` ;
- `adaptation != concession` ;
- `strategic exposure != exercised leverage` ;
- `restriction effect != requested-policy effect` ;
- `absence of concession evidence != absence of coercive attempt`.

Le run ne fournit pas de dénominateur permettant d’estimer la fréquence générale de conversion des dépendances énergétiques ou minérales en coercition politique contre la France ou l’Union. Il ferme en revanche deux familles de **levier exercé** — gaz russe et contrôles d’exportation sur matières critiques — et démontre pourquoi le résultat terminal doit rester séparé du coût imposé et de l’adaptation de la cible.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:0|EDI_DECISIVE:4|SRC_COMPLETE:13/13

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-11
- **breaks:**
  - 2012-2015 EU/WTO rare-earth dispute
  - 2022 Russian gas payment/cutoff crisis
  - 2024 CRMA enters into force
  - 2025 Chinese heavy rare-earth export controls
  - 2026 EU stepwise Russian-gas prohibition
- **status:** CURRENT
- **window:** France/UE 2006-2026; gaz, uranium, terres rares et matières critiques

### MANIPULATION_REPORT
- **assumptions:**
  - qualification follows proved dependency/control/action/cost/adaptation/concession edges
- **clusters:**
  - POWER
  - MONEY
  - NETWORK
- **complexity:**
  - **band:** HIGH
  - **score:** 9
- **implicit:**
  - persuasion is not required for economic coercion; the state of available options can change directly
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - dependency=coercion
  - price=political pressure
  - cutoff=concession
  - export-control=ingérence
  - diversification=proof-of-threat
- **priorities:**
  - official market data
  - legal/contractual control point
  - independent energy-market corroboration
  - negative controls
- **query_guidance:** separate vulnerability, exercised leverage, material impact, adaptation and political concession
- **rhetorical:**
  - NONE
- **speaker:** mechanism-first forensic investigation contract
- **symbol_stage:** FINAL
- **symbols:**
  - **ACTOR:** state/supplier/controller exercising or holding leverage
  - **ADAPTATION:** target mitigation/diversification/regulatory response
  - **COERCION:** deliberate exercise or credible threat of control to alter target conduct
  - **CONCESSION:** requested political decision by target
  - **CONTROL_POINT:** actor-controlled bottleneck or contractual/export gate
  - **COST:** price/shortage/production/continuity effect
  - **DEPENDENCY:** concentrated reliance on external flow
  - **EFFECT:** downstream material or political result
  - **INTENT:** purpose or requested policy outcome requiring separate evidence
  - **LEVERAGE:** actionable ability to alter a hard-to-substitute flow
  - **MARKET_SHOCK:** price/supply movement without proven deliberate coercive act
  - **RESTRICTION:** cutoff/export control/condition/limitation
  - **SUPPLIER:** actor controlling relevant flow or licence gate
  - **TARGET:** state, buyer, industry or institution bearing the constraint
  - **VULNERABILITY:** dependency that may exist without exercised leverage
- **threats:**
  - market-shock attribution error
  - intent promotion
  - adaptation-to-concession promotion
  - single-case prevalence extrapolation
  - not found=does not exist

### MODULE_EXECUTION
NONE

### SCOPING_REPORT
- **chain:**
  - supplier/state
  - dependency
  - control point
  - restriction/condition/cutoff
  - cost/disruption
  - adaptation
  - concession/decision
  - effect
- **exclusions:**
  - generic commodity price movements
  - supply shocks without attributable action
  - foreign origin alone
- **object:** Energy and critical-material dependencies as coercive leverage
- **scope:** France/UE 2006-2026

### CREDO
- dependency != coercion
- market shock != deliberate action
- restriction != political concession
- adaptation != concession
- exposure != exercised leverage
- absence of terminal effect evidence != absence of operation

### COGNITIVE_MAP
- **causal_boundary:** political success exists only when a specific requested decision is causally linked to the exercised lever
- **core_model:** economic coercion is a branch where control over a hard-to-substitute flow modifies costs/options directly, without persuasion
- **rival_models:**
  - ordinary market shock
  - contract dispute without political purpose
  - security/export-control policy without EU-targeted concession
  - precaution against vulnerability without exercised coercion
- **serial_edges:**
  - dependency
  - control point
  - deliberate restriction/condition
  - material cost
  - target adaptation
  - requested concession
  - terminal effect

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** many dependencies remain unexercised and are managed by contracts/markets
  - **resolution:** require actor-controlled restriction/condition plus material effect
  - **thesis:** dependency itself is coercion
- **item 2:**
  - **antithesis:** cuts imposed large costs and forced structural adaptation
  - **resolution:** separate coercive exercise/material effect from political success
  - **thesis:** Russia failed because EU did not concede
- **item 3:**
  - **antithesis:** controls can serve security/industrial-policy aims and target broader trade systems
  - **resolution:** close restriction and industrial effect; keep EU political-concession intent case-specific
  - **thesis:** all Chinese critical-material controls are anti-EU coercion

### RESOURCE_FLOW_MAP
- **item 1:**
  - **case:** Russia gas 2022
  - **flow:** high dependency -> ruble payment condition/cutoffs/flow reductions -> price/supply shock -> storage/LNG/diversification -> phaseout
  - **status:** EXERCISED_COERCION_WITHOUT_CLOSED_CONCESSION
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
    - FCT-004
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-008
    - FCT-019
- **item 2:**
  - **case:** China rare-earth restrictions
  - **flow:** supply concentration -> export duties/quotas/licensing or 2025 controls -> availability/production effects -> legal/policy diversification response
  - **status:** EXERCISED_EXPORT_CONTROL_WITH_POLITICAL_EFFECT_GAP
  - **support:**
    - FCT-009
    - FCT-010
    - FCT-011
    - FCT-012
    - FCT-013
    - FCT-014
    - FCT-015
- **item 3:**
  - **case:** Russian nuclear fuel
  - **flow:** material supplier exposure -> stockpiling/diversification -> no scoped Russian cutoff established
  - **status:** VULNERABILITY_NEGATIVE_CONTROL
  - **support:**
    - FCT-016
    - FCT-017
    - FCT-018

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** Russian state/Gazprom
  - **relation:** payment condition and gas-supply control
  - **support:**
    - FCT-002
    - FCT-003
    - FCT-019
  - **to:** EU buyers/member states
- **item 2:**
  - **from:** Chinese export-control authorities
  - **relation:** licensing/export restrictions
  - **support:**
    - FCT-009
    - FCT-012
    - FCT-013
  - **to:** global/EU-dependent rare-earth supply chains
- **item 3:**
  - **from:** EU institutions
  - **relation:** storage/diversification/CRMA resilience rules
  - **support:**
    - FCT-006
    - FCT-007
    - FCT-008
    - FCT-015
  - **to:** member states/industry
- **item 4:**
  - **from:** Russian nuclear-fuel suppliers
  - **relation:** continuing supply exposure
  - **support:**
    - FCT-016
    - FCT-018
  - **to:** EU utilities/VVER operators

### IMPACT_MAP
- **downstream:** supports economic coercion as independent branch of democratic/state influence without persuasion
- **measured_objects:**
  - gas cutoff/flow reduction
  - gas wholesale price shock
  - storage/diversification policy
  - Russian gas phaseout
  - rare-earth export controls
  - European industrial disruption
  - CRMA resilience architecture
  - uranium/enrichment exposure
- **not_established:**
  - specific EU concession to Russian gas coercion
  - specific EU political concession to Chinese material controls
  - general prevalence/success rate of economic coercion

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** uranium exposure and other dependencies can persist without exercised cutoff
  - **issue:** dependency=coercion
  - **pro:** concentration creates a potential leverage point
  - **resolution:** DEPENDENCY_IS_CAPABILITY_NOT_ACTION
- **item 2:**
  - **contra:** cuts clearly imposed costs and triggered adaptation
  - **issue:** gas coercion failed because no concession
  - **pro:** no requested EU concession is closed
  - **resolution:** COERCION_EXERCISE_AND_POLITICAL_SUCCESS_SEPARATE
- **item 3:**
  - **contra:** official sources also describe industrial/security aims and only partial evidence of retaliatory motive
  - **issue:** China controls=anti-EU political coercion
  - **pro:** controls hit EU-relevant materials and industry
  - **resolution:** RESTRICTION_AND_COST_CLOSED_POLITICAL_CONCESSION_OPEN

### VERIFICATION_REPORT
- **checks:**
  - Russian ruble-payment cutoff corroborated by EU and IEA sources
  - market shock separated from attributable supply action
  - gas cost and adaptation separately evidenced
  - political concession not inferred from adaptation
  - WTO rare-earth restrictions and removal traced
  - 2025 rare-earth industrial effects independently sourced
  - CRMA treated as resilience architecture not proof of prior coercion
  - uranium dependency retained as negative control
- **status:** PASS_WITH_EXPLICIT_GAPS

### EDI_REPORT
- **corpus:** 13 accepted sources across EU institutions, WTO and independent/specialised energy-statistical lineages; related EU pages are not counted as independent prevalence evidence
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim:** gas exercised leverage
    - **families:**
      - A
      - C
  - **item 2:**
    - **claim:** rare-earth restrictions
    - **families:**
      - A
      - B
      - C
  - **item 3:**
    - **claim:** EU adaptation
    - **families:**
      - A
  - **item 4:**
    - **claim:** nuclear negative control
    - **families:**
      - C
- **diagnostic_not_truth:** true
- **dimensions:**
  - gas dependency/control/action
  - market impact
  - EU adaptation
  - rare-earth export controls
  - industrial impact
  - CRMA resilience
  - nuclear negative control
- **edi:** OFFICIAL_EU_DOMINANT_WITH_WTO_AND_IEA_EURATOM_CORROBORATION
- **source_counts:**
  - **A:** 8
  - **B:** 1
  - **C:** 4

### RESPONSIBILITY_MAP
- **item 1:**
  - **claim:** Russia gas cutoff/payment condition
  - **owner:** Russian state/Gazprom as documented by EU/IEA
  - **status:** SUPPORTED
  - **support:**
    - FCT-002
    - FCT-003
    - FCT-019
- **item 2:**
  - **claim:** EU gas-market costs/adaptation
  - **owner:** EU institutions/market data
  - **status:** SUPPORTED
  - **support:**
    - FCT-004
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-008
- **item 3:**
  - **claim:** China rare-earth export restrictions
  - **owner:** Chinese export-control policy as documented by WTO/Commission/IEA
  - **status:** SUPPORTED
  - **support:**
    - FCT-009
    - FCT-010
    - FCT-012
    - FCT-013
- **item 4:**
  - **claim:** EU political concession caused by material coercion
  - **owner:** INV-151 synthesis
  - **status:** NOT_ESTABLISHED
  - **support:**
    - NONE
- **item 5:**
  - **claim:** Russian nuclear cutoff against EU
  - **owner:** INV-151 synthesis
  - **status:** NOT_ESTABLISHED
  - **support:**
    - FCT-016
    - FCT-017
    - FCT-018

### NEXT_QUERIES
- **item 1:**
  - **query:** economic coercion through dollar/clearing/correspondent banking with explicit condition and target adaptation in EU
  - **route:** CANDIDATE_INV-152
  - **trigger:** post-INV151 reclassification only
- **item 2:**
  - **query:** sovereign debt/credit/aid condition -> concession in France/EU-relevant comparators
  - **route:** CANDIDATE_INV-153
  - **trigger:** post-INV151 reclassification only
- **item 3:**
  - **query:** informal trade retaliation -> attributed political demand -> company/state adaptation
  - **route:** CANDIDATE_INV-154
  - **trigger:** post-INV151 reclassification only

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,FCT-019 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-012,FCT-013,FCT-016,FCT-017,FCT-018 | final:GAP | gap:DENOMINATOR
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-001,FCT-014,FCT-016,FCT-018 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-002,FCT-003,FCT-009,FCT-010,FCT-012,FCT-013,FCT-019 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-004,FCT-005,FCT-013 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-006,FCT-007,FCT-008,FCT-011,FCT-015,FCT-017,FCT-018 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-002,FCT-003,FCT-006,FCT-007,FCT-008,FCT-012,FCT-013 | final:GAP | gap:CAUSALITY
CLM-001 | attempts:QRY-001,QRY-011,QRY-012,SRC-001,SRC-011,SRC-012 | support:FCT-001,FCT-014,FCT-016,FCT-018 | counter:- | results:FCT-001,FCT-014,FCT-016,FCT-018 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-002,QRY-003,QRY-013,SRC-002,SRC-003,SRC-013 | support:FCT-002,FCT-003,FCT-019 | counter:- | results:FCT-002,FCT-003,FCT-019 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-003,SRC-003 | support:FCT-004,FCT-005 | counter:- | results:FCT-004,FCT-005 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-004,QRY-005,QRY-006,SRC-004,SRC-005,SRC-006 | support:FCT-006,FCT-007,FCT-008 | counter:- | results:FCT-006,FCT-007,FCT-008 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-004,QRY-005,QRY-006,SRC-004,SRC-005,SRC-006 | support:- | counter:FCT-006,FCT-007,FCT-008 | results:FCT-006,FCT-007,FCT-008 | final:GAP | gap:CAUSALITY
CLM-006 | attempts:QRY-007,QRY-008,QRY-009,SRC-007,SRC-008,SRC-009 | support:FCT-009,FCT-010,FCT-011,FCT-012,FCT-013 | counter:- | results:FCT-009,FCT-010,FCT-011,FCT-012,FCT-013 | final:PARTIAL | gap:CAUSALITY
CLM-007 | attempts:QRY-010,QRY-012,SRC-010,SRC-012 | support:FCT-014,FCT-015 | counter:- | results:FCT-014,FCT-015 | final:SUPPORTED | gap:NONE
CLM-008 | attempts:QRY-011,SRC-011 | support:FCT-016,FCT-017,FCT-018 | counter:FCT-016,FCT-017,FCT-018 | results:FCT-016,FCT-017,FCT-018,FCT-016,FCT-017,FCT-018 | final:REFUTED | gap:NONE
CLM-009 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:- | final:GAP | gap:DENOMINATOR

## STATUS_DELTA_V1
DELTA-001 | CLM-006 | SUPPORTED_WITH_LIMIT | PARTIAL | normalize terminal status; substantive limit retained in gap field

## OPEN_GAPS_V1
AXS-005 | AXS | GAP | CAUSALITY | The run closes costs and adaptation but not a specific EU political concession attributable to the exercised gas or critical-material leverage.
CLM-005 | CLM | GAP | CAUSALITY | No specific requested EU political concession is causally closed in the bounded run.
CLM-006 | CLM | PARTIAL | CAUSALITY | Intent and political concession remain episode-specific.
CLM-009 | CLM | GAP | DENOMINATOR | No representative denominator/success-rate design.
CAU-001 | CAU | SUPPORTED | CAUSALITY | No general France/EU coercion-success denominator; no specific political concession closed for the strongest gas/critical-material cases.

SEMANTIC_COUNTS_V1:LED:2|CLM:9|AXS:5|CAU:1|CTRL:8|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013"],"evidence_excerpt":"Trace supplier/state -> dependency -> control point -> restriction/threat/price/condition -> cost/disruption -> adaptation -> political effect.","kind":"HYPOTHESIS","lead":"Economic dependency becomes coercive leverage only when a supplier/controller deliberately restricts, conditions, threatens or interrupts a hard-to-substitute flow and the target bears measurable cost or adapts; political concession is a further edge.","linked_ids":["CLM-001","CLM-002","CLM-003","CLM-004","CLM-005","CLM-006","CLM-007","CLM-008"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018","FCT-019"],"routes":["POWER","MONEY","NETWORK"],"source_id":"INV-151-RUN_CARD","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013"],"evidence_excerpt":"Positive cases close exercised leverage and adaptation more often than a requested political concession.","gap":"No representative denominator and no general estimate of coercion-to-concession success rate.","gap_type":"DENOMINATOR","kind":"GAP","lead":"Representative denominator for energy/critical-material dependencies converted into successful political coercion against France/EU.","linked_ids":["CLM-009"],"locator":"GAP","materiality":"HIGH","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-012","FCT-013","FCT-016","FCT-017","FCT-018"],"routes":["RECHECK"],"source_id":"INV-151-RUN_CARD","status":"GAP"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Dependency or supply concentration alone is not economic coercion.","claimant":"INV-151 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-014","FCT-016","FCT-018"]}
CLM-002 | {"claim":"Russia exercised a coercive gas lever against EU member states in 2022 through the ruble-payment condition and supply cutoffs/reductions.","claimant":"INV-151 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-002","FCT-003","FCT-019"]}
CLM-003 | {"claim":"The 2022 Russian gas reductions imposed large material costs on the EU gas/electricity system and energy-intensive industry.","claimant":"INV-151 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-004","FCT-005"]}
CLM-004 | {"claim":"The EU materially adapted through storage rules, diversification, demand reduction and progressive phaseout of Russian gas.","claimant":"INV-151 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-006","FCT-007","FCT-008"]}
CLM-005 | {"claim":"The Russian gas coercion caused the EU to make the requested political concession to Moscow.","claimant":"INV-151 synthesis","counter":["FCT-006","FCT-007","FCT-008"],"gap":"No specific requested EU political concession is causally closed in the bounded run.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"GAP","support":"NONE_FOUND"}
CLM-006 | {"claim":"Chinese rare-earth/export restrictions are real control points capable of generating industrial disruption, but each episode requires separate intent and political-effect analysis.","claimant":"INV-151 synthesis","counter":"NONE_FOUND","gap":"Intent and political concession remain episode-specific.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-013"]}
CLM-007 | {"claim":"The EU Critical Raw Materials Act is a resilience response to concentrated strategic dependencies, not proof that every dependency has already been weaponised.","claimant":"INV-151 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-014","FCT-015"]}
CLM-008 | {"claim":"Russian nuclear-fuel exposure in 2025 proves that Russia exercised an uranium/enrichment cutoff against the EU in the scoped run.","claimant":"INV-151 synthesis","counter":["FCT-016","FCT-017","FCT-018"],"gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"REFUTED","support":["FCT-016","FCT-017","FCT-018"]}
CLM-009 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013"],"claim":"This run establishes a general prevalence or success rate of economic coercion against France/EU.","claimant":"INV-151 synthesis","counter":"NONE_FOUND","gap":"No representative denominator/success-rate design.","gap_type":"DENOMINATOR","materiality":"HIGH","status":"GAP","support":"NONE_FOUND"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013"],"axis":"DEPENDENCY","links":["CLM-001"],"question":"Is a concentrated/hard-to-substitute dependency established?","result_ids":["FCT-001","FCT-014","FCT-016","FCT-018"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013"],"axis":"EXERCISED_CONTROL","links":["CLM-002","CLM-006"],"question":"Was a restriction/condition/cutoff/export control actually exercised?","result_ids":["FCT-002","FCT-003","FCT-009","FCT-010","FCT-012","FCT-013","FCT-019"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013"],"axis":"MATERIAL_COST","links":["CLM-003"],"question":"Did the action produce a measurable cost/shortage/industrial disruption?","result_ids":["FCT-004","FCT-005","FCT-013"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013"],"axis":"TARGET_ADAPTATION","links":["CLM-004","CLM-007","CLM-008"],"question":"Did EU/public/industrial actors materially adapt?","result_ids":["FCT-006","FCT-007","FCT-008","FCT-011","FCT-015","FCT-017","FCT-018"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013"],"axis":"POLITICAL_CONCESSION","gap":"The run closes costs and adaptation but not a specific EU political concession attributable to the exercised gas or critical-material leverage.","gap_type":"CAUSALITY","links":["CLM-005","CLM-009"],"question":"Did the coercer obtain a specific requested EU political concession?","result_ids":["FCT-002","FCT-003","FCT-006","FCT-007","FCT-008","FCT-012","FCT-013"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"GAP"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"EXERCISED_CONTROL_PLUS_COST_OR_ADAPTATION_REQUIRED; POLITICAL_CONCESSION_SEPARATE","counter":"Uranium/VVER exposure demonstrates strategic vulnerability and precaution without an exercised Russian cutoff in this run; adaptation can occur without concession.","gap":"No general France/EU coercion-success denominator; no specific political concession closed for the strongest gas/critical-material cases.","gap_type":"CAUSALITY","limit":"Political success requires evidence that the target adopted the requested policy because of the coercive action; cost and adaptation are insufficient.","mechanism":"supplier/state -> concentrated dependency -> real control point -> deliberate restriction/condition/cutoff -> cost/disruption -> target adaptation -> requested concession or downstream effect","question":"When does energy or critical-material dependency become coercive leverage rather than mere vulnerability?","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-012","FCT-013","FCT-014","FCT-015"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"dependency != coercion","status":"PASS","support":["FCT-001","FCT-016","FCT-018"]}
CTRL-002 | {"control":"supply interruption != political intent","status":"PASS","support":["FCT-003","FCT-005"]}
CTRL-003 | {"control":"price shock != coercion","status":"PASS","support":["FCT-004"]}
CTRL-004 | {"control":"export control != political concession","status":"PASS","support":["FCT-009","FCT-012","FCT-013"]}
CTRL-005 | {"control":"adaptation != concession","status":"PASS","support":["FCT-006","FCT-007","FCT-008"]}
CTRL-006 | {"control":"strategic exposure != exercised leverage","status":"PASS","support":["FCT-014","FCT-016","FCT-018"]}
CTRL-007 | {"control":"restriction effect != requested-policy effect","status":"PASS","support":["FCT-004","FCT-013"]}
CTRL-008 | {"control":"absence of concession evidence != absence of coercive attempt","status":"PASS","support":["FCT-002","FCT-003","FCT-019"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:13|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"EMPTY","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | MNEMO_UNAVAILABLE | mnemo | NONE | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://energy.ec.europa.eu/topics/energy-security/security-gas-supply_en | -
QRY-002 | FETCH | FOUND | SRC-002 | https://cinea.ec.europa.eu/news-events/news/cef-energy-eu-funded-energy-projects-more-crucial-ever-after-russia-cuts-gas-supply-poland-and-2022-04-27_en | -
QRY-003 | FETCH | FOUND | SRC-003 | https://energy.ec.europa.eu/news/new-reports-highlight-3rd-quarter-impact-gas-supply-cuts-2023-01-13_en | -
QRY-004 | FETCH | FOUND | SRC-004 | https://www.consilium.europa.eu/en/press/press-releases/2022/06/27/council-adopts-regulation-gas-storage/ | -
QRY-005 | FETCH | FOUND | SRC-005 | https://energy.ec.europa.eu/news/repowereu-3-years-commission-takes-stock-progress-phase-out-russian-fossil-fuels-2025-05-16_en | -
QRY-006 | FETCH | FOUND | SRC-006 | https://www.consilium.europa.eu/en/policies/ending-russian-energy-imports/ | -
QRY-007 | FETCH | FOUND | SRC-007 | https://www.wto.org/english/tratop_e/dispu_e/cases_e/ds432_e.htm | -
QRY-008 | FETCH | FOUND | SRC-008 | https://single-market-economy.ec.europa.eu/system/files/2024-01/EconomicBrief_4_ETBD_23_004ENN_V2.pdf | -
QRY-009 | FETCH | FOUND | SRC-009 | https://www.iea.org/commentaries/with-new-export-controls-on-critical-minerals-supply-concentration-risks-become-reality | -
QRY-010 | FETCH | FOUND | SRC-010 | https://single-market-economy.ec.europa.eu/sectors/raw-materials/areas-specific-interest/critical-raw-materials/critical-raw-materials-act_en | -
QRY-011 | FETCH | FOUND | SRC-011 | https://euratom-supply.ec.europa.eu/activities/market-observatory_en | -
QRY-012 | FETCH | FOUND | SRC-012 | https://ec.europa.eu/eurostat/en/web/products-eurostat-news/w/ddn-20260629-1 | -
QRY-013 | FETCH | FOUND | SRC-013 | https://www.iea.org/reports/gas-market-lessons-from-the-2022-2023-energy-crisis/anatomy-of-a-natural-gas-crisis | -

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | EC-GAS-SECURITY | European Commission — Security of gas supply | 2026-09-11 | 2026-09-11T16:46:00Z | Russian attempted weaponisation; over-dependence on one supplier; EU response | https://energy.ec.europa.eu/topics/energy-security/security-gas-supply_en
SRC-002 | ◈ | fam:A | CINEA-GAS-CUTOFFS-2022 | CINEA — Russia cuts gas supply to Poland and Bulgaria | 2022-04-27 | 2026-09-11T16:46:00Z | Gazprom cutoff after refusal to pay in rubles, decision by Russian president | https://cinea.ec.europa.eu/news-events/news/cef-energy-eu-funded-energy-projects-more-crucial-ever-after-russia-cuts-gas-supply-poland-and-2022-04-27_en
SRC-003 | ◈ | fam:A | EC-GAS-Q3-2022 | European Commission — Q3 2022 gas market impact report | 2023-01-13 | 2026-09-11T16:46:00Z | weaponisation, Nord Stream reductions, prices, LNG substitution, demand contraction | https://energy.ec.europa.eu/news/new-reports-highlight-3rd-quarter-impact-gas-supply-cuts-2023-01-13_en
SRC-004 | ◈ | fam:A | COUNCIL-GAS-STORAGE-2022 | Council — regulation on gas storage | 2022-06-27 | 2026-09-11T16:46:00Z | 80% storage 2022/23 and 90% subsequent winters | https://www.consilium.europa.eu/en/press/press-releases/2022/06/27/council-adopts-regulation-gas-storage/
SRC-005 | ◈ | fam:A | EC-REPOWEREU-2025 | European Commission — REPowerEU three years on | 2025-05-16 | 2026-09-11T16:46:00Z | Russian gas imports 150 bcm 2021 to 52 bcm 2024; share 45% to 19% | https://energy.ec.europa.eu/news/repowereu-3-years-commission-takes-stock-progress-phase-out-russian-fossil-fuels-2025-05-16_en
SRC-006 | ◈ | fam:A | COUNCIL-END-RUSSIAN-GAS-2026 | Council — Ending Russian energy imports | 2026-01-26 | 2026-09-11T16:46:00Z | systematic weaponisation; 2026 regulation for stepwise gas import prohibition; share 45% to 13% by 2025 | https://www.consilium.europa.eu/en/policies/ending-russian-energy-imports/
SRC-007 | ◈ | fam:B | WTO-DS432 | WTO DS432 — China export restrictions on rare earths, tungsten and molybdenum | 2015-05-20 | 2026-09-11T16:46:00Z | EU complaint; export duties/quotas/licensing; findings and implementation/removal | https://www.wto.org/english/tratop_e/dispu_e/cases_e/ds432_e.htm
SRC-008 | ◈ | fam:A | EC-CHINA-EXPOSURE-2024 | European Commission Economic Brief — EU economic exposure to China | 2024-01-01 | 2026-09-11T16:46:00Z | 2023 controls on gallium/germanium/graphite; reactions to Dutch lithography restrictions described cautiously | https://single-market-economy.ec.europa.eu/system/files/2024-01/EconomicBrief_4_ETBD_23_004ENN_V2.pdf
SRC-009 | ◈ | fam:C | IEA-REE-CONTROLS-2025 | IEA — New export controls on critical minerals | 2025-10-23 | 2026-09-11T16:46:00Z | April 2025 heavy rare earth controls, European automaker production effects, concentration and later expansion | https://www.iea.org/commentaries/with-new-export-controls-on-critical-minerals-supply-concentration-risks-become-reality
SRC-010 | ◈ | fam:A | EU-CRMA | European Commission — Critical Raw Materials Act | 2024-05-23 | 2026-09-11T16:46:00Z | 2030 diversification benchmarks; monitoring, stress testing, strategic stocks, preparedness | https://single-market-economy.ec.europa.eu/sectors/raw-materials/areas-specific-interest/critical-raw-materials/critical-raw-materials-act_en
SRC-011 | ◈ | fam:C | EURATOM-2025 | Euratom Supply Agency — EU nuclear fuel market 2025 | 2026-09-11 | 2026-09-11T16:46:00Z | Russian shares in uranium/enrichment, stockpiling, VVER single-supplier vulnerability | https://euratom-supply.ec.europa.eu/activities/market-observatory_en
SRC-012 | ◈ | fam:C | EUROSTAT-REE-2025 | Eurostat — EU trade in rare earth elements in 2025 | 2026-06-29 | 2026-09-11T16:46:00Z | China 46.8% of EU rare-earth imports by weight in 2025 | https://ec.europa.eu/eurostat/en/web/products-eurostat-news/w/ddn-20260629-1
SRC-013 | ◈ | fam:C | IEA-GAS-LESSONS-2025 | IEA — Anatomy of a natural gas crisis | 2025-01-01 | 2026-09-11T16:46:00Z | ruble payment attempt, unilateral cuts, concentration and LNG adaptation | https://www.iea.org/reports/gas-market-lessons-from-the-2022-2023-energy-crisis/anatomy-of-a-natural-gas-crisis

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://energy.ec.europa.eu/topics/energy-security/security-gas-supply_en | A | 2026-09-11 | Russian gas dependency and weaponisation | The Commission states that Russia attempted to weaponise Europe’s security of energy supply and that the EU had been over-dependent on one supplier for almost half of its gas imports. | -
FCT-002 | FACT | ✧ | https://cinea.ec.europa.eu/news-events/news/cef-energy-eu-funded-energy-projects-more-crucial-ever-after-russia-cuts-gas-supply-poland-and-2022-04-27_en | A | 2022-04-27 | Ruble-payment cutoff control | Gazprom halted gas supplies to Poland and Bulgaria after they refused to pay in rubles, following a decision by the Russian President. | -
FCT-003 | FACT | ✧ | https://energy.ec.europa.eu/news/new-reports-highlight-3rd-quarter-impact-gas-supply-cuts-2023-01-13_en | A | 2023-01-13 | Gas weaponisation and Nord Stream reductions | The Commission described Russia’s weaponisation of gas exports as the dominant Q3 2022 market factor and reported progressive reductions in Nord Stream 1 flows. | -
FCT-004 | FACT | ✧ | https://energy.ec.europa.eu/news/new-reports-highlight-3rd-quarter-impact-gas-supply-cuts-2023-01-13_en | A | 2023-01-13 | Gas price and industrial impact | Wholesale gas prices exceeded EUR 300/MWh by end-August 2022; high prices contributed to a collapse in demand in some energy-intensive industries and to unprecedented electricity prices. | -
FCT-005 | FACT | ✧ | https://energy.ec.europa.eu/news/new-reports-highlight-3rd-quarter-impact-gas-supply-cuts-2023-01-13_en | A | 2023-01-13 | Flow and LNG substitution | Russian pipeline gas imports in Q3 2022 were down 74% year-on-year, Nord Stream 1 imports down 85%, while EU LNG imports rose 89%. | -
FCT-006 | FACT | ✧ | https://www.consilium.europa.eu/en/press/press-releases/2022/06/27/council-adopts-regulation-gas-storage/ | A | 2022-06-27 | Storage regulation adaptation | The Council adopted rules requiring gas storage before winter, with an 80% target for 2022/23 and 90% for subsequent winters. | -
FCT-007 | FACT | ✧ | https://energy.ec.europa.eu/news/repowereu-3-years-commission-takes-stock-progress-phase-out-russian-fossil-fuels-2025-05-16_en | A | 2025-05-16 | Russian gas dependency reduced | The Commission reports Russian gas imports falling from 150 bcm in 2021 to 52 bcm in 2024, with the Russian share dropping from 45% to 19%. | -
FCT-008 | FACT | ✧ | https://www.consilium.europa.eu/en/policies/ending-russian-energy-imports/ | A | 2026-01-26 | Stepwise Russian gas phaseout | The Council records a 2026 regulation for a stepwise prohibition of Russian gas imports and reports the Russian gas share declining from 45% in 2021 to 13% in 2025. | -
FCT-009 | FACT | ✧ | https://www.wto.org/english/tratop_e/dispu_e/cases_e/ds432_e.htm | B | 2012-03-13 | EU rare-earth dispute initiation | The EU challenged Chinese export duties, quotas, licensing and related restrictions affecting rare earths, tungsten and molybdenum. | -
FCT-010 | FACT | ✧ | https://www.wto.org/english/tratop_e/dispu_e/cases_e/ds432_e.htm | B | 2014-03-26 | WTO rare-earth findings | The WTO panel found challenged Chinese export restrictions inconsistent with obligations and found the export quotas served industrial-policy goals rather than the conservation justification advanced. | -
FCT-011 | FACT | ✧ | https://www.wto.org/english/tratop_e/dispu_e/cases_e/ds432_e.htm | B | 2015-05-20 | Removal after WTO ruling | China informed the WTO that export duties, quotas and trading-right restrictions found inconsistent had been removed. | -
FCT-012 | FACT | ✧ | https://single-market-economy.ec.europa.eu/system/files/2024-01/EconomicBrief_4_ETBD_23_004ENN_V2.pdf | A | 2024-01-01 | China 2023 critical-material export controls | A Commission economic brief records 2023 Chinese export controls on gallium, germanium and graphite and says the gallium/germanium restrictions appear in part to react to Dutch lithography export restrictions. | -
FCT-013 | FACT | ✧ | https://www.iea.org/commentaries/with-new-export-controls-on-critical-minerals-supply-concentration-risks-become-reality | C | 2025-10-23 | 2025 rare-earth controls hit industry | The IEA reports that China’s April 2025 controls on seven heavy rare earth elements sharply reduced export volumes, forcing some automakers in Europe and elsewhere to cut utilisation or temporarily halt production. | -
FCT-014 | FACT | ✧ | https://ec.europa.eu/eurostat/en/web/products-eurostat-news/w/ddn-20260629-1 | C | 2026-06-29 | EU rare-earth import concentration | Eurostat reports that China supplied 46.8% of the EU’s rare-earth imports by weight in 2025. | -
FCT-015 | FACT | ✧ | https://single-market-economy.ec.europa.eu/sectors/raw-materials/areas-specific-interest/critical-raw-materials/critical-raw-materials-act_en | A | 2024-05-23 | CRMA diversification architecture | The Critical Raw Materials Act sets 2030 benchmarks of 10% EU extraction, 40% processing, 25% recycling and no more than 65% dependence on one third country, with monitoring, stress tests and strategic-stock coordination. | -
FCT-016 | FACT | ✧ | https://euratom-supply.ec.europa.eu/activities/market-observatory_en | C | 2026-09-11 | Russian uranium exposure | In 2025 Russia supplied 15.98% of natural uranium delivered to EU utilities and 22.55% of enrichment services. | -
FCT-017 | FACT | ✧ | https://euratom-supply.ec.europa.eu/activities/market-observatory_en | C | 2026-09-11 | Nuclear stockpiling response | Euratom reports that EU utilities have stockpiled nuclear materials and fuel since Russia’s invasion to mitigate supply-disruption risk. | -
FCT-018 | FACT | ✧ | https://euratom-supply.ec.europa.eu/activities/market-observatory_en | C | 2026-09-11 | VVER single-supplier vulnerability | Euratom identifies dependence on a single fuel design/supplier for VVER reactors as a significant security-of-supply vulnerability and records diversification efforts. | -
FCT-019 | FACT | ✧ | https://www.iea.org/reports/gas-market-lessons-from-the-2022-2023-energy-crisis/anatomy-of-a-natural-gas-crisis | C | 2025-01-01 | Independent gas coercion corroboration | The IEA reports that Russia attempted to impose a ruble payment system on EU buyers, leading to unilateral cuts and sanctions against certain buyers, with Russian piped exports to OECD Europe falling roughly 50% in 2022. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-003
FCT-004 | SRC-003
FCT-005 | SRC-003
FCT-006 | SRC-004
FCT-007 | SRC-005
FCT-008 | SRC-006
FCT-009 | SRC-007
FCT-010 | SRC-007
FCT-011 | SRC-007
FCT-012 | SRC-008
FCT-013 | SRC-009
FCT-014 | SRC-012
FCT-015 | SRC-010
FCT-016 | SRC-011
FCT-017 | SRC-011
FCT-018 | SRC-011
FCT-019 | SRC-013

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

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:SEARCH
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:FACTS
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:CAUSAL_GAP
CP-004 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 | NEXT_ACTION:VERIFY
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:INVESTIGATION_ACCOUNTABILITY
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:FINALIZE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-11T16:59:17.875911+00:00","fact_mem":{},"mnemo_row":"MNEMO_UNAVAILABLE — local memory service not available; no memory ids fabricated.","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":19,"eligible":19,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_UNAVAILABLE — local memory service not available; no memory ids fabricated. | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:19;attempted:0;success:0;failure:0;blocked:19} | WRITEBACK_EXECUTION_V1:[19 rows, see section]

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
