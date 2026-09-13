ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260911-1742-trafic-influence-courtiers-acces | PARENT_RUN_ID:NONE | AS_OF:2026-09-11
INPUT_KIND:RUN_CARD | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/audit121/INV148_TRANSACTION_2026-09-11/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-11_trafic-influence-courtiers-acces/2026-09-11_17-42_trafic-influence-courtiers-acces_INPUT.txt | SUBJECT_SLUG:trafic-influence-courtiers-acces | SUBJECT_FP:sha256:79b1852f6ff574b080030a1e1542fc92530cf41e521f8f70fe9f370c5ca6786b | INPUT_SHA256:sha256:208ce16779a5b31bb68bc33b65d05960c1a1e1b369fd874597d9a6b6761a8b50
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/UE, principalement 2010-2026. Trafic d influence et courtiers d accès; tracer payeur/beneficiaire -> avantage -> intermediaire -> influence reelle ou supposee -> detenteur de decision -> intervention -> decision/avantage -> effet. Comparateurs etrangers isomorphes admis. Gardes: lobbying != trafic; intermediaire != trafic; corruption directe != trafic; origine etrangere != ingerence; accusation != condamnation; non trouve != inexistant.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-148 — Trafic d’influence et courtiers d’accès

## Objet

L’enquête cherche à isoler le mécanisme propre du trafic d’influence dans l’espace plus large de l’influence politique et économique. Le point discriminant n’est ni l’origine étrangère de l’acteur, ni la simple présence d’un intermédiaire, ni la rémunération d’un professionnel. Le mécanisme pertinent est triadique : un bénéficiaire ou payeur fournit ou promet un avantage à un intermédiaire afin que celui-ci abuse d’une influence réelle ou supposée auprès d’un tiers qui détient le pouvoir de décision recherché.

Cette structure est distincte de la corruption directe, dans laquelle l’avantage vise l’acte propre du décideur, et du lobbying ou de la représentation d’intérêts, dans lesquels un représentant peut être rémunéré pour présenter des arguments, organiser un accès ou défendre un intérêt sans échange indu portant sur une influence abusive. Cette séparation est soutenue par le droit pénal français, la doctrine publique de l’AFA et la directive européenne anticorruption de 2026 (FCT-001 à FCT-006 ; CLM-001 à CLM-003).

## Mécanisme établi

Le noyau probatoire est :

`bénéficiaire/payeur -> avantage indu -> intermédiaire -> influence réelle ou supposée -> détenteur de la décision -> intervention -> décision ou avantage recherché`.

Le droit français ferme explicitement les premiers maillons pour les situations domestiques et pour les décisions d’agents publics étrangers ou d’organisations internationales publiques (FCT-001 à FCT-003). La directive (UE) 2026/1021 renforce le discriminant : la qualification ne dépend pas du fait que l’influence soit effectivement exercée ni qu’elle obtienne le résultat recherché. L’infraction et l’effet politique final sont donc deux objets différents (FCT-004 ; CLM-003).

Ce résultat empêche deux confusions symétriques. Premièrement, une rémunération d’intermédiaire ne constitue pas automatiquement un trafic d’influence : agents commerciaux, avocats, consultants ou représentants d’intérêts peuvent être rémunérés légalement. Deuxièmement, l’absence de décision favorable finale ne suffit pas à exclure le mécanisme lorsque l’échange indu portant sur l’influence est établi. La directive de 2026 distingue d’ailleurs explicitement la représentation légitime d’intérêts de l’échange indu constitutif du trafic d’influence (FCT-005 ; CTRL-001).

## Contrôles positifs

Plusieurs dossiers montrent que le modèle n’est pas purement doctrinal. L’échantillon de décisions analysé par l’AFA décrit le mécanisme à trois acteurs et contient des condamnations pour trafic d’influence. Un cas de Montpellier constitue un contrôle positif particulièrement lisible : une personne proposait, contre paiement, son intermédiation auprès d’un service préfectoral en utilisant la position de sa mère afin d’accélérer la délivrance de certificats d’immatriculation (FCT-007 à FCT-009). Ce cas ferme l’existence pratique du courtage d’influence sans nécessiter de dimension étrangère.

L’affaire dite Bismuth fournit un autre contrôle positif domestique et définitif au niveau de la Cour de cassation. Le dossier associe information confidentielle, intermédiation et promesse d’un avantage professionnel ; il confirme que trafic d’influence et corruption peuvent coexister dans un même ensemble factuel tout en restant des qualifications distinctes (FCT-010).

Le dossier croate instruit par le Parquet européen constitue le contrôle transnational/institutionnel le plus utile de ce run. Dans une procédure d’achat de logiciel financée par des fonds européens, un ancien ministre a plaidé coupable et a été condamné pour abus de fonction et trafic d’influence ; le dossier décrit des interventions destinées à privilégier un intérêt commercial et une procédure ayant finalement conduit à un contrat. Un bénéficiaire économique du même dossier a ensuite plaidé coupable et restitué un gain indu (FCT-012 à FCT-014). Ces décisions ferment l’existence d’un mécanisme d’influence indue dans une chaîne économique et de commande publique, mais elles ne doivent pas être généralisées à l’ensemble des marchés publics.

## Ce que l’intermédiaire ne prouve pas

L’OCDE montre que les intermédiaires sont fréquents dans les affaires de corruption transnationale de son corpus : ils interviennent dans une forte proportion des affaires conclues étudiées. Ce résultat établit leur importance opérationnelle, pas la qualification de trafic d’influence (FCT-011).

Le dossier Airbus sert ici de contrôle négatif. La convention judiciaire d’intérêt public documente l’usage d’intermédiaires commerciaux dans des mécanismes de corruption liés à des contrats internationaux. Pourtant, `intermédiaire + commission + corruption` ne suffit pas à prouver que l’objet de l’échange était l’influence de cet intermédiaire sur un tiers décideur, condition discriminante du trafic d’influence. Le rôle fonctionnel de l’intermédiaire doit donc être établi, et non déduit de son intitulé ou de sa rémunération (FCT-015 ; CLM-005 ; CAU-001).

## Frontière avec l’influence étrangère

Les articles 435-2 et 435-4 du Code pénal français montrent que le trafic d’influence peut viser un agent public étranger ou une organisation internationale publique (FCT-002, FCT-003). Cela ne signifie pas que tout trafic d’influence transnational est automatiquement une « ingérence étrangère », ni que toute activité d’influence d’un acteur étranger constitue un trafic d’influence. La qualification doit suivre le mécanisme prouvé : origine du principal, nature de l’avantage, fonction de l’intermédiaire, objet de l’influence, détenteur de la décision, transparence, légalité, puis effet éventuel (CTRL-002).

Cette distinction est centrale pour la nouvelle taxonomie mécanisme-first. Le trafic d’influence n’est pas un niveau supérieur du lobbying ni un sous-type automatique de l’ingérence. Il est une chaîne propre qui peut ensuite, selon l’origine, le contrôle, la cible et l’atteinte à l’autonomie décisionnelle, contribuer à une qualification d’ingérence.

## Limites et non-résultats

La recherche publique bornée n’a pas identifié un jugement français définitif récent, sous les articles 435-2 ou 435-4, fermant proprement la chaîne complète `principal étranger -> avantage -> intermédiaire rémunéré -> influence -> agent public étranger/organisation internationale -> décision`. Le droit applicable existe clairement et les comparateurs étrangers montrent que le mécanisme est opérationnel, mais le cas français final correspondant n’a pas été retrouvé dans le périmètre du run (CLM-008 ; AXS-004).

Ce non-résultat est un gap d’accès/retrieval, pas une preuve d’inexistence. Il ne doit pas être transformé en affirmation selon laquelle la France n’aurait jamais poursuivi ou condamné un tel schéma.

Les pourcentages de l’AFA ne fournissent pas non plus une prévalence nationale. Ils décrivent un échantillon borné de décisions de justice 2021-2022, avec un périmètre méthodologique propre ; ils ne mesurent ni l’ensemble des faits commis ni tous les signalements, enquêtes ou procédures (FCT-007, FCT-016 ; CLM-007).

Enfin, les dossiers Qatargate, Huawei et Azerbaïdjan/PACE examinés dans INV-136 ne doivent pas être requalifiés automatiquement en trafic d’influence. INV-136 ferme des chaînes de valeur, intermédiaires, responsables et actes à des degrés variables, mais chaque requalification exigerait de démontrer que l’avantage rémunère précisément l’abus d’une influence sur un tiers détenteur de décision, plutôt qu’un acte propre du bénéficiaire public ou une autre forme de corruption.

## Delta pour le programme

INV-148 ajoute un mécanisme qui manquait comme catégorie autonome : `BROKER_INFLUENCE / TRAFIC_INFLUENCE`. Il impose d’enregistrer séparément le payeur, l’intermédiaire, le détenteur de décision et l’objet de l’échange. Cela évite que les courtiers d’accès soient rangés indistinctement dans `LOBBYING`, `CORRUPTION` ou `OTHER`.

Le principal gap aval devient alors la provenance de l’argent et l’identité du principal lorsque le paiement traverse des sociétés écrans, prête-noms, bénéficiaires effectifs opaques, intermédiaires professionnels ou circuits de blanchiment. Le trafic d’influence est maintenant mieux défini ; la difficulté suivante consiste à relier proprement `fonds -> véritable principal -> intermédiaire -> accès/action`. Cela justifie la promotion d’INV-149, consacrée à la finance opaque et aux bénéficiaires effectifs, sans invalider les autres gaps économiques déjà identifiés.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:0|EDI_DECISIVE:6|SRC_COMPLETE:12/12

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-11
- **breaks:**
  - 2016 Sapin II foreign/public-international extension
  - 2024-12-18 Bismuth final Cour de cassation
  - 2025 Croatia plea convictions in EU-funded procurement
  - 2026-05-31 Directive (EU) 2026/1021 enters into force
- **status:** CURRENT
- **window:** France/UE principalement 2010-2026

### MANIPULATION_REPORT
- **assumptions:**
  - classification follows proved mechanism, not actor identity
- **clusters:**
  - MONEY
  - NETWORK
  - POWER
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - outcome success distinct from offence completion
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - corruption/lobbying/traffic conflation
  - foreign-origin shortcut
  - intermediary-role inflation
  - procedural-status inflation
  - prevalence extrapolation
- **priorities:**
  - primary legal texts
  - final adjudications
  - negative controls
  - money/intermediary chain
- **query_guidance:** find adjudicated three-actor chains; preserve non-findings and legal/procedural status
- **rhetorical:**
  - NONE
- **speaker:** mechanism-first forensic investigation contract
- **symbol_stage:** FINAL
- **symbols:**
  - **ACCESS:** lawful or neutral contact channel unless other elements proved
  - **ACTOR:** person/entity acting
  - **ADVANTAGE:** undue payment/promise/benefit
  - **BENEFICIARY:** actor seeking favourable outcome
  - **CORRUPTION:** exchange tied to decision-holder own act
  - **DECISION:** public act/contract/employment/advantage sought
  - **DECISION_HOLDER:** third party with formal/public decision power
  - **EFFECT:** downstream outcome distinct from offence completion
  - **GAP:** typed unresolved evidence edge
  - **INFLUENCE:** real or supposed capacity to affect decision-holder
  - **INTERMEDIARY:** broker whose influence is the object of exchange
  - **LOBBYING:** declared/legitimate interest representation absent undue exchange
  - **PRINCIPAL:** beneficiary or instructing interest
  - **PROVENANCE:** source/status lineage
  - **TRAFIC_INFLUENCE:** undue exchange tied to intermediary influence over third-party decision-holder
- **threats:**
  - guilt by accusation
  - paid consultant = influence broker
  - intermediary = corrupt
  - foreign = interference
  - not found = does not exist

### MODULE_EXECUTION
NONE

### SCOPING_REPORT
- **chain:**
  - beneficiary/payer
  - undue advantage
  - intermediary
  - real/supposed influence
  - public decision-holder
  - intervention
  - decision/benefit
  - effect
- **exclusions:**
  - ordinary disclosed lobbying
  - direct bribery of decision-holder
  - fees without undue exchange
  - foreign origin alone
- **object:** Trafic d influence et courtiers d acces
- **scope:** France/UE 2010-2026; comparateurs étrangers isomorphes

### CREDO
- corruption directe != trafic influence
- lobbying rémunéré != trafic influence
- intermédiaire != preuve d échange indu
- foreign != ingérence
- influence réelle ou supposée peut suffire juridiquement si échange indu établi
- résultat favorable obtenu != élément nécessaire de infraction UE 2026
- non trouvé != inexistant

### COGNITIVE_MAP
- **causal_boundary:** the influence/undue-exchange edge is decisive; offence completion and downstream political effect are separate
- **core_model:** triadic paid influence brokerage
- **rival_models:**
  - lawful representation
  - direct bribery
  - consulting/access without undue exchange
  - mere claimed connections
  - bribe conduit without influence brokerage
- **serial_edges:**
  - advantage
  - intermediary
  - influence
  - decision-holder
  - decision

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** payment can purchase lawful professional representation or direct bribery instead
  - **resolution:** identify who is paid, what is exchanged, whose decision is targeted and whether influence over a third party is the bargained object
  - **thesis:** paid access broker = traffic automatically
- **item 2:**
  - **antithesis:** French/EU definitions cover real or supposed influence and EU law makes success irrelevant
  - **resolution:** separate offence completion from downstream effect
  - **thesis:** no final result means no trafficking

### RESOURCE_FLOW_MAP
- **item 1:**
  - **case:** Montpellier registration certificates
  - **flow:** garages -> payment -> intermediary -> family-position influence -> prefecture service -> faster certificates
  - **status:** ADJUDICATED_POSITIVE_CONTROL
  - **support:**
    - FCT-009
- **item 2:**
  - **case:** Croatia EU-funded software
  - **flow:** business interest -> privileged relationship/influence -> minister/procurement apparatus -> contract award -> monetary gain
  - **status:** PLEA_CONVICTIONS_WITH_REMAINING_DEFENDANTS
  - **support:**
    - FCT-012
    - FCT-013
    - FCT-014
- **item 3:**
  - **case:** Airbus
  - **flow:** company -> commercial intermediaries -> benefits/bribery in foreign contracts
  - **status:** NEGATIVE_CONTROL_FOR_CLASSIFICATION
  - **support:**
    - FCT-015

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** beneficiary/payor
  - **relation:** undue advantage
  - **support:**
    - FCT-001
    - FCT-008
  - **to:** intermediary
- **item 2:**
  - **from:** intermediary
  - **relation:** real or supposed influence
  - **support:**
    - FCT-001
    - FCT-004
    - FCT-008
  - **to:** public decision-holder
- **item 3:**
  - **from:** decision-holder
  - **relation:** favourable decision/act
  - **support:**
    - FCT-012
    - FCT-013
    - FCT-014
  - **to:** beneficiary

### IMPACT_MAP
- **downstream:** reclassifies economic influence ontology and raises finance-opacity/beneficial-ownership gap
- **measured_objects:**
  - legal classification boundary
  - adjudicated domestic positive controls
  - EU procurement positive control
  - intermediary prevalence in foreign bribery
- **not_established:**
  - national prevalence
  - automatic requalification of INV-136 cases as trading in influence
  - clean final French 435-2/435-4 transnational case
  - general democratic outcome effect

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** OECD/Airbus show intermediaries also channel ordinary bribery or lawful commercial roles
  - **issue:** intermediary = traffic
  - **pro:** triadic mechanism requires intermediary
  - **resolution:** INTERMEDIARY_NECESSARY_IN_MODEL_NOT_SUFFICIENT_FOR_CLASSIFICATION
- **item 2:**
  - **contra:** Directive 2026 distinguishes legitimate interest representation absent undue exchange
  - **issue:** lobbying = traffic
  - **pro:** both seek public decisions
  - **resolution:** UNDUE_EXCHANGE_AND_IMPROPER_INFLUENCE_DISCRIMINATE

### VERIFICATION_REPORT
- **checks:**
  - legal definitions current as of 2026
  - Bismuth finality checked
  - Croatia procedural endpoints checked
  - AFA denominator bounded
  - OECD intermediary statistic not converted into traffic prevalence
  - Airbus retained as negative comparator
  - no French foreign-case absence claim promoted to non-existence
- **status:** PASS_WITH_EXPLICIT_GAP

### EDI_REPORT
- **corpus:** 12 accepted sources across 3 provenance families; EPPO releases form one case lineage and French institutional sources are not independent of the same legal system
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim:** CLM-001
    - **families:**
      - A
  - **item 2:**
    - **claim:** CLM-002
    - **families:**
      - A
      - B
  - **item 3:**
    - **claim:** CLM-003
    - **families:**
      - A
      - B
  - **item 4:**
    - **claim:** CLM-004
    - **families:**
      - A
      - B
  - **item 5:**
    - **claim:** CLM-005
    - **families:**
      - A
      - C
  - **item 6:**
    - **claim:** CLM-006
    - **families:**
      - A
- **diagnostic_not_truth:** true
- **dimensions:**
  - French criminal law
  - EU harmonised law
  - French final jurisprudence
  - AFA decision sample
  - EPPO procurement adjudication
  - OECD transnational bribery dataset
  - CJIP negative comparator
- **edi:** PRIMARY_OFFICIAL_DOMINANT_WITH_ONE_OECD_DATASET_AND_CASE_LINEAGE_DEPENDENCE
- **source_counts:**
  - **A:** 6
  - **B:** 5
  - **C:** 1

### RESPONSIBILITY_MAP
- **item 1:**
  - **claim:** French offence definition
  - **owner:** French legislature/courts
  - **status:** ESTABLISHED
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
- **item 2:**
  - **claim:** Bismuth guilt
  - **owner:** Cour de cassation
  - **status:** FINAL
  - **support:**
    - FCT-010
- **item 3:**
  - **claim:** Croatia minister/business owner guilt
  - **owner:** Croatian court / EPPO reporting
  - **status:** PLEA_CONVICTIONS
  - **support:**
    - FCT-012
    - FCT-014
- **item 4:**
  - **claim:** foreign-bribery intermediary frequency
  - **owner:** OECD dataset
  - **status:** BOUNDED_DATASET
  - **support:**
    - FCT-011

### NEXT_QUERIES
- **item 1:**
  - **query:** French final judgments applying 435-2/435-4 to a fully documented foreign/public-international decision chain
  - **route:** RECHECK
  - **trigger:** new indexed jurisprudence or court database access
- **item 2:**
  - **query:** shell companies / beneficial owners / laundering around paid intermediaries and corrupt influence
  - **route:** NEW_INVESTIGATION
  - **trigger:** INV-149
- **item 3:**
  - **query:** more lobbying examples without undue exchange
  - **route:** DROP
  - **trigger:** mechanism already bounded

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-002,QRY-003,QRY-005,QRY-008,QRY-009 | support:- | counter:- | results:FCT-002,FCT-003,FCT-004,FCT-011 | final:GAP | gap:ACCESS
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-008 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-006,QRY-007,QRY-010,QRY-011 | support:- | counter:- | results:FCT-009,FCT-010,FCT-012,FCT-013,FCT-014 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-008,QRY-012 | support:- | counter:- | results:FCT-011,FCT-015 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-002,QRY-003,QRY-005,QRY-008,QRY-009 | support:- | counter:- | results:FCT-002,FCT-003,FCT-004,FCT-011 | final:GAP | gap:ACCESS
CLM-001 | attempts:QRY-001,QRY-004,QRY-007,SRC-001,SRC-004,SRC-007 | support:FCT-001,FCT-006,FCT-008 | counter:- | results:FCT-001,FCT-006,FCT-008 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-004,QRY-005,SRC-004,SRC-005 | support:FCT-005,FCT-006 | counter:- | results:FCT-005,FCT-006 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-001,QRY-005,SRC-001,SRC-005 | support:FCT-001,FCT-004 | counter:- | results:FCT-001,FCT-004 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-006,QRY-007,QRY-010,QRY-011,SRC-006,SRC-007,SRC-010,SRC-011 | support:FCT-007,FCT-009,FCT-010,FCT-012,FCT-014 | counter:- | results:FCT-007,FCT-009,FCT-010,FCT-012,FCT-014 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-008,QRY-012,SRC-008,SRC-012 | support:FCT-011,FCT-015 | counter:- | results:FCT-011,FCT-015 | final:SUPPORTED | gap:NONE
CLM-006 | attempts:QRY-002,QRY-003,SRC-002,SRC-003 | support:FCT-002,FCT-003 | counter:- | results:FCT-002,FCT-003 | final:SUPPORTED | gap:NONE
CLM-007 | attempts:QRY-007,SRC-007 | support:FCT-007,FCT-016 | counter:- | results:FCT-007,FCT-016 | final:SUPPORTED | gap:NONE
CLM-008 | attempts:QRY-002,QRY-003,SRC-002,SRC-003 | support:- | counter:FCT-002,FCT-003 | results:FCT-002,FCT-003 | final:GAP | gap:ACCESS

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
AXS-004 | AXS | GAP | ACCESS | Legal coverage is explicit; a clean final French merits example under 435-2/435-4 was not identified in this bounded run.
CLM-008 | CLM | GAP | ACCESS | No clean final French case matching the full transnational chain was identified in the bounded public-source run. This is NOT_FOUND, not NON_EXISTENCE.
CAU-001 | CAU | UNRESOLVED | CAUSALITY | The payment-to-influence edge must be evidenced case by case; role labels or fees are insufficient.

SEMANTIC_COUNTS_V1:LED:2|CLM:8|AXS:4|CAU:1|CTRL:4|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012"],"evidence_excerpt":"Distinguish lobbying, direct corruption and trading in influence.","kind":"HYPOTHESIS","lead":"Trading in influence is a distinct triadic mechanism: beneficiary/payer -> rewarded intermediary -> real or supposed influence -> decision-holder; foreign origin is neither necessary nor sufficient.","linked_ids":["AXS-001","CLM-001"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016"],"routes":["OBJECT_INVESTIGATION","MECHANISMS","COUNTER_HYPOTHESES"],"source_id":"INV-148_RUN_CARD","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-002","QRY-003","QRY-005","QRY-008","QRY-009"],"evidence_excerpt":"Bounded search found explicit legal coverage but no clean final French merits case matching the full transnational chain.","gap":"No qualifying final French 435-2/435-4 conviction identified in the bounded public search; absence of finding is not proof of non-existence.","gap_type":"ACCESS","kind":"GAP","lead":"Clean French 2016-2026 final case under articles 435-2/435-4 closing a foreign principal -> paid intermediary -> foreign/international public decision chain.","linked_ids":["AXS-004","CLM-008"],"locator":"GAP-1","materiality":"IMPORTANT","result_ids":["FCT-002","FCT-003","FCT-004","FCT-011"],"routes":["RECHECK"],"source_id":"INV-148_RUN_CARD","status":"GAP"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Trading in influence is structurally triadic: beneficiary/payer -> intermediary -> decision-holder; direct corruption instead targets the decision-holder own act.","claimant":"INV-148 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-006","FCT-008"]}
CLM-002 | {"claim":"Lawful lobbying or interest representation is not trading in influence merely because it seeks to affect a public decision; an undue advantage and improper influence exchange are material discriminants.","claimant":"INV-148 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-005","FCT-006"]}
CLM-003 | {"claim":"The influence may be real or supposed, and under Directive (EU) 2026/1021 the offence does not depend on the influence actually being exerted or succeeding.","claimant":"INV-148 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-004"]}
CLM-004 | {"claim":"Trading in influence is an empirically observed offence, not a purely doctrinal category: AFA decisions, the final Bismuth judgment and Croatian EPPO convictions provide positive controls.","claimant":"INV-148 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-007","FCT-009","FCT-010","FCT-012","FCT-014"]}
CLM-005 | {"claim":"Intermediaries are operationally central in transnational corruption ecosystems, but intermediary involvement or commission payments alone do not establish trading in influence.","claimant":"INV-148 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-011","FCT-015"]}
CLM-006 | {"claim":"French law expressly covers trading in influence aimed at foreign public officials and public international organisations.","claimant":"INV-148 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-002","FCT-003"]}
CLM-007 | {"claim":"The AFA 5.8% case share cannot be used as a national prevalence estimate for trading in influence.","claimant":"INV-148 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-007","FCT-016"]}
CLM-008 | {"claim":"A clean final French 435-2/435-4 merits case was identified that closes foreign principal -> paid intermediary -> foreign/international decision.","claimant":"INV-148 bounded search target","counter":["FCT-002","FCT-003"],"gap":"No clean final French case matching the full transnational chain was identified in the bounded public-source run. This is NOT_FOUND, not NON_EXISTENCE.","gap_type":"ACCESS","materiality":"HIGH","status":"GAP","support":"NONE_FOUND"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005"],"axis":"LEGAL_MECHANISM","links":["CLM-001","CLM-002","CLM-003"],"question":"What distinguishes trading in influence from direct corruption and lawful lobbying?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-008"],"sought_objects":["LEGAL_ELEMENTS","BOUNDARIES"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-006","QRY-007","QRY-010","QRY-011"],"axis":"POSITIVE_CONTROLS","links":["CLM-004"],"question":"Are there adjudicated cases where the intermediary/influence mechanism is operational rather than merely theoretical?","result_ids":["FCT-009","FCT-010","FCT-012","FCT-013","FCT-014"],"sought_objects":["CASE_CHAIN"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-008","QRY-012"],"axis":"INTERMEDIARY_ECOLOGY","links":["CLM-005"],"question":"How central are intermediaries in adjacent corruption mechanisms and what must not be conflated?","result_ids":["FCT-011","FCT-015"],"sought_objects":["INTERMEDIARIES","NEGATIVE_CONTROL"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-002","QRY-003","QRY-005","QRY-008","QRY-009"],"axis":"FOREIGN_APPLICATION","gap":"Legal coverage is explicit; a clean final French merits example under 435-2/435-4 was not identified in this bounded run.","gap_type":"ACCESS","links":["CLM-006","CLM-008"],"question":"Does French/EU law and evidence close a foreign-principal trading-in-influence chain in a final French merits case?","result_ids":["FCT-002","FCT-003","FCT-004","FCT-011"],"sought_objects":["TRANSNATIONAL_CASE"],"status":"GAP"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"Airbus shows intermediaries can channel bribery without proving the distinct trading-in-influence mechanism; lawful representation can also be paid.","gap":"The payment-to-influence edge must be evidenced case by case; role labels or fees are insufficient.","gap_type":"CAUSALITY","limit":"Need evidence of the undue exchange specifically for influence over a third-party decision-holder.","mechanism":"advantage/payment -> intermediary -> claimed/real influence -> public decision-holder -> intervention -> favourable decision","status":"UNRESOLVED","support":["FCT-001","FCT-008","FCT-009","FCT-012","FCT-014"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"intermediary involvement != trading in influence; an intermediary can be a lawful lobbyist, consultant, bribery conduit or influence broker depending on the exchange and target.","status":"PASS","support":["FCT-005","FCT-011","FCT-015"]}
CTRL-002 | {"control":"foreign origin != ingérence and != trading in influence; classify the mechanism first.","status":"PASS","support":["FCT-002","FCT-003","FCT-006"]}
CTRL-003 | {"control":"charge/indictment != conviction; preserve procedural status.","status":"PASS","support":["FCT-010","FCT-012","FCT-014"]}
CTRL-004 | {"control":"bounded search non-finding != proof of non-existence.","status":"PASS","support":["FCT-002","FCT-003","FCT-004"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:12|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"EMPTY","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | MNEMO_UNAVAILABLE | mnemo | NONE | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000028311912/2026-05-10 | -
QRY-002 | FETCH | FOUND | SRC-002 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033611474 | -
QRY-003 | FETCH | FOUND | SRC-003 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033611468/2026-05-05 | -
QRY-004 | FETCH | FOUND | SRC-004 | https://www.agence-francaise-anticorruption.gouv.fr/fr/lexique | -
QRY-005 | FETCH | FOUND | SRC-005 | https://eur-lex.europa.eu/eli/dir/2026/1021/oj | -
QRY-006 | FETCH | FOUND | SRC-006 | https://www.courdecassation.fr/toutes-les-actualites/2024/12/18/communique-affaire-de-corruption-trafic-dinfluence-et-violation-du | -
QRY-007 | FETCH | FOUND | SRC-007 | https://www.agence-francaise-anticorruption.gouv.fr/files/files/Note_Analyse_Decisionsdejustice_ObservatoireAFA_09122024.pdf | -
QRY-008 | FETCH | FOUND | SRC-008 | https://www.oecd.org/content/dam/oecd/en/publications/reports/2014/12/oecd-foreign-bribery-report_g1g4d808/9789264226616-en.pdf | -
QRY-009 | FETCH | FOUND | SRC-009 | https://www.eppo.europa.eu/media/news/former-minister-and-three-suspects-indicted-croatia-abuse-office-and-authority-and-trading-influence-2022-12-29_en | -
QRY-010 | FETCH | FOUND | SRC-010 | https://www.eppo.europa.eu/media/news/croatia-former-minister-sentenced-two-years-imprisonment-abuse-office-and-authority-2025-06-12_en | -
QRY-011 | FETCH | FOUND | SRC-011 | https://www.eppo.europa.eu/media/news/croatia-additional-conviction-investigation-software-purchase-ministry-regional-development-and-eu-2025-09-12_en | -
QRY-012 | FETCH | FOUND | SRC-012 | https://www.tribunal-de-paris.justice.fr/sites/default/files/2020-02/CJIP%20AIRBUS_English%20version.pdf | -

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | FR-CP-433-2 | Code penal — article 433-2 | 2013-12-08 | 2026-09-11T15:45:00Z | definition domestique du trafic d influence | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000028311912/2026-05-10
SRC-002 | ◈ | fam:A | FR-CP-435-2 | Code penal — article 435-2 | 2016-12-11 | 2026-09-11T15:45:00Z | trafic d influence passif visant agent public etranger ou organisation internationale | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033611474
SRC-003 | ◈ | fam:A | FR-CP-435-4 | Code penal — article 435-4 | 2016-12-11 | 2026-09-11T15:45:00Z | trafic d influence actif visant agent public etranger ou organisation internationale | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033611468/2026-05-05
SRC-004 | ◈ | fam:A | AFA-LEX-TI | AFA — Lexique : Trafic d influence | 2026-09-11 | 2026-09-11T15:45:00Z | definition et distinction corruption / trafic d influence | https://www.agence-francaise-anticorruption.gouv.fr/fr/lexique
SRC-005 | ◈ | fam:B | EU-DIR-2026-1021 | Directive (UE) 2026/1021 — lutte contre la corruption | 2026-05-11 | 2026-09-11T15:45:00Z | considerant 16 et article 6 — trading in influence | https://eur-lex.europa.eu/eli/dir/2026/1021/oj
SRC-006 | ◈ | fam:A | CASS-2024-23-83178 | Cour de cassation — corruption, trafic d influence et violation du secret professionnel | 2024-12-18 | 2026-09-11T15:45:00Z | condamnations definitives et mecanisme Bismuth | https://www.courdecassation.fr/toutes-les-actualites/2024/12/18/communique-affaire-de-corruption-trafic-dinfluence-et-violation-du
SRC-007 | ◈ | fam:A | AFA-DJ-2024 | AFA — Note analyse 2024 des decisions de justice | 2024-12-09 | 2026-09-11T15:45:00Z | trafic d influence, echantillon 2021-2022, infractions connexes | https://www.agence-francaise-anticorruption.gouv.fr/files/files/Note_Analyse_Decisionsdejustice_ObservatoireAFA_09122024.pdf
SRC-008 | ◈ | fam:C | OECD-FBR-2014 | OECD Foreign Bribery Report | 2014-12-02 | 2026-09-11T15:45:00Z | Figure 16 — intermediaries in foreign bribery cases | https://www.oecd.org/content/dam/oecd/en/publications/reports/2014/12/oecd-foreign-bribery-report_g1g4d808/9789264226616-en.pdf
SRC-009 | ◈ | fam:B | EPPO-HR-2022-TI | EPPO — Croatia indictment for trading in influence | 2022-12-29 | 2026-09-11T15:45:00Z | indictment, procurement mechanism, estimated damage | https://www.eppo.europa.eu/media/news/former-minister-and-three-suspects-indicted-croatia-abuse-office-and-authority-and-trading-influence-2022-12-29_en
SRC-010 | ◈ | fam:B | EPPO-HR-2025-MIN | EPPO — former Croatian minister convicted for trading in influence | 2025-06-12 | 2026-09-11T15:45:00Z | conviction, plea, procurement actions and damage | https://www.eppo.europa.eu/media/news/croatia-former-minister-sentenced-two-years-imprisonment-abuse-office-and-authority-2025-06-12_en
SRC-011 | ◈ | fam:B | EPPO-HR-2025-OWNER | EPPO — additional Croatia conviction in software procurement case | 2025-09-12 | 2026-09-11T15:45:00Z | business owner conviction, benefit and contract award | https://www.eppo.europa.eu/media/news/croatia-additional-conviction-investigation-software-purchase-ministry-regional-development-and-eu-2025-09-12_en
SRC-012 | ◈ | fam:A | PNF-AIRBUS-2020 | PNF / Tribunal de Paris — Airbus CJIP | 2020-01-31 | 2026-09-11T15:45:00Z | foreign bribery and commercial intermediaries; negative comparator | https://www.tribunal-de-paris.justice.fr/sites/default/files/2020-02/CJIP%20AIRBUS_English%20version.pdf

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000028311912/2026-05-10 | A | 2013-12-08 | French domestic legal definition | Article 433-2 criminalises giving or receiving an undue advantage so an intermediary abuses real or supposed influence to obtain a favourable decision from a public authority or administration. | -
FCT-002 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033611474 | A | 2016-12-11 | Foreign/international passive trading in influence | Article 435-2 covers solicitation or receipt of an advantage to abuse real or supposed influence over a foreign public official or public international organisation decision. | -
FCT-003 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033611468/2026-05-05 | A | 2016-12-11 | Foreign/international active trading in influence | Article 435-4 covers offering or giving an advantage to an intermediary to abuse real or supposed influence over a foreign public official or public international organisation decision. | -
FCT-004 | FACT | ✧ | https://eur-lex.europa.eu/eli/dir/2026/1021/oj | B | 2026-05-11 | EU harmonised offence | Directive (EU) 2026/1021 Article 6 requires Member States to criminalise intentional trading in influence; whether influence is actually exerted or achieves the intended result is irrelevant to the offence. | -
FCT-005 | FACT | ✧ | https://eur-lex.europa.eu/eli/dir/2026/1021/oj | B | 2026-05-11 | Legitimate representation boundary | Directive recital 16 distinguishes legitimate interest/legal representation from trading in influence where the undue exchange and other offence elements are absent. | -
FCT-006 | FACT | ✧ | https://www.agence-francaise-anticorruption.gouv.fr/fr/lexique | A | 2026-09-11 | AFA conceptual distinction | AFA distinguishes corruption, where the corrupted person acts within own functions, from trading in influence, where the intermediary uses influence over the actual decision-holder. | -
FCT-007 | FACT | ✧ | https://www.agence-francaise-anticorruption.gouv.fr/files/files/Note_Analyse_Decisionsdejustice_ObservatoireAFA_09122024.pdf | A | 2024-12-09 | AFA sample frequency bounded | In the AFA 2021-2022 decision sample, trading in influence represents 8.4% of offences and concerns 5.8% of 489 cases; this is a bounded court-decision sample, not a national prevalence estimate. | -
FCT-008 | FACT | ✧ | https://www.agence-francaise-anticorruption.gouv.fr/files/files/Note_Analyse_Decisionsdejustice_ObservatoireAFA_09122024.pdf | A | 2024-12-09 | Triadic actor model | AFA describes three roles: beneficiary, intermediary using real or attributed credit, and the target who holds decision power. | -
FCT-009 | FACT | ✧ | https://www.agence-francaise-anticorruption.gouv.fr/files/files/Note_Analyse_Decisionsdejustice_ObservatoireAFA_09122024.pdf | A | 2021-06-21 | Montpellier positive control | A Montpellier case convicted a person for passive trading in influence after offering, for payment, to act as intermediary for garages seeking faster vehicle-registration certificates using his mother position in the prefecture service. | -
FCT-010 | FACT | ✧ | https://www.courdecassation.fr/toutes-les-actualites/2024/12/18/communique-affaire-de-corruption-trafic-dinfluence-et-violation-du | A | 2024-12-18 | Bismuth final conviction | The Cour de cassation confirmed final convictions of a political figure, lawyer and magistrate for corruption/trading in influence/secret violations in a scheme involving confidential procedural information and a promised professional favour. | -
FCT-011 | FACT | ✧ | https://www.oecd.org/content/dam/oecd/en/publications/reports/2014/12/oecd-foreign-bribery-report_g1g4d808/9789264226616-en.pdf | C | 2014-12-02 | Intermediaries in foreign bribery | OECD found intermediaries involved in 71% of concluded foreign-bribery cases in its dataset; agents accounted for the largest category. This does not make those cases trading in influence. | -
FCT-012 | FACT | ✧ | https://www.eppo.europa.eu/media/news/croatia-former-minister-sentenced-two-years-imprisonment-abuse-office-and-authority-2025-06-12_en | B | 2025-06-12 | Croatia minister conviction | A former Croatian minister pleaded guilty and was sentenced to two years for abuse of office and trading in influence in an EU-funded software procurement case. | -
FCT-013 | FACT | ✧ | https://www.eppo.europa.eu/media/news/croatia-former-minister-sentenced-two-years-imprisonment-abuse-office-and-authority-2025-06-12_en | B | 2025-06-12 | Croatia procurement mechanism | The minister took actions to privilege a business owner, including inflating estimated value and using a negotiated procedure; after annulment the actors continued seeking award, and a EUR 1.73m contract was eventually concluded. | -
FCT-014 | FACT | ✧ | https://www.eppo.europa.eu/media/news/croatia-additional-conviction-investigation-software-purchase-ministry-regional-development-and-eu-2025-09-12_en | B | 2025-09-12 | Croatia beneficiary-side conviction | A business owner in the same procurement case pleaded guilty, received an 11-month sentence converted to community service, repaid about EUR 272k of undue gain, and had acted with the former minister and another owner to secure the award. | -
FCT-015 | FACT | ✧ | https://www.tribunal-de-paris.justice.fr/sites/default/files/2020-02/CJIP%20AIRBUS_English%20version.pdf | A | 2020-01-31 | Airbus negative comparator | Airbus CJIP documents foreign bribery involving commercial intermediaries in international contracts; use of an intermediary to channel bribery is operationally important but does not by itself establish the distinct offence of trading in influence. | -
FCT-016 | FACT | ✧ | https://www.agence-francaise-anticorruption.gouv.fr/files/files/Note_Analyse_Decisionsdejustice_ObservatoireAFA_09122024.pdf | A | 2024-12-09 | AFA denominator limitation | The AFA 2024 note analyses judicial decisions rendered in 2021-2022 and excludes CJIP homologation orders; its percentages cannot be extrapolated to all corruption or influence activity. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-003
FCT-004 | SRC-005
FCT-005 | SRC-005
FCT-006 | SRC-004
FCT-007 | SRC-007
FCT-008 | SRC-007
FCT-009 | SRC-007
FCT-010 | SRC-006
FCT-011 | SRC-008
FCT-012 | SRC-010
FCT-013 | SRC-010
FCT-014 | SRC-011
FCT-015 | SRC-012
FCT-016 | SRC-007

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
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:SEARCH
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:FACTS
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:CAUSAL
CP-004 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 | NEXT_ACTION:VERIFY
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:INVESTIGATION_ACCOUNTABILITY
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:FINALIZE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-11T15:58:17.162306+00:00","fact_mem":{},"mnemo_row":"MNEMO_UNAVAILABLE — local memory service not available; no memory ids fabricated.","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":16,"eligible":16,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_UNAVAILABLE — local memory service not available; no memory ids fabricated. | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:16;attempted:0;success:0;failure:0;blocked:16} | WRITEBACK_EXECUTION_V1:[16 rows, see section]

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
