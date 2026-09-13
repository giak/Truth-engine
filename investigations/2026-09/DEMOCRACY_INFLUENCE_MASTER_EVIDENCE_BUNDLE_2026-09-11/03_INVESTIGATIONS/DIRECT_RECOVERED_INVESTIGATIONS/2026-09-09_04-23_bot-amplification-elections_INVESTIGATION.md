ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260909-0423-bot-amplification-elections | PARENT_RUN_ID:NONE | AS_OF:2026-09-09
INPUT_KIND:RUN_CARD | MISSION_MODE:RECHECK_EXTEND | INPUT_REF:PATH:/mnt/data/inv097/runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-09_bot-amplification-elections/2026-09-09_04-23_bot-amplification-elections_INPUT.md | SUBJECT_SLUG:bot-amplification-elections | SUBJECT_FP:sha256:fbfa3c15bd5647f06d2962c8f14ddd2a9b2fe3de07e0f753d913dd8c88ce53b0 | INPUT_SHA256:sha256:b14d5b0f137a2e57eb080125d952dfa90ec6b69c901de9b85859b9cd1380d806
COMPLEXITY:8→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/EU 2018-2026 with directly transposable comparators; operator/client/tasking -> account creation/control -> automation/coordination -> content -> incremental amplification -> exposure -> reception/behavior -> electoral effect. Preserve bot != fake account; network != coordination; coordination != tasking; detection != prevalence; reach != persuasion; amplification != vote change.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/NETWORK.md,clusters/FRAMING.md,clusters/TEMPORAL.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-097 — Bots, faux comptes, astroturfing et amplification artificielle pendant les élections

## Question

Dans quelle mesure les bots, faux comptes, réseaux coordonnés et techniques d’astroturfing augmentent-ils artificiellement l’exposition à des contenus politiques pendant les élections, qui les opère ou les commande, et jusqu’où la chaîne peut-elle être fermée vers la persuasion ou un effet électoral ? L’enquête sépare strictement type de compte, automatisation, identité trompeuse, coordination, opérateur, client/tasking, amplification incrémentale, exposition, réception et résultat électoral.

## Verdict

Le **mécanisme d’amplification artificielle est établi**, mais il n’est ni uniforme ni synonyme de changement électoral. Les cas RRN/Doppelganger, Portal Kombat et Matriochka documentent des infrastructures coordonnées combinant comptes inauthentiques, répétition automatisée, diffusion en réseau, faux contenus ou sites, réponses ciblées et optimisation de distribution. Le Sénat français corrobore spécifiquement l’usage de bots pour amplifier Portal Kombat, en partie via des comptes liés à RRN/Doppelganger. [SRC-001, SRC-002, SRC-003, SRC-004, SRC-010]

La Roumanie en 2024 fournit un cas électoral plus direct. TikTok a déclaré avoir identifié un réseau de 4 453 comptes inauthentiques visant le public roumain et cherchant à promouvoir AUR et, dans une moindre mesure, Calin Georgescu. La plateforme a également publié des volumes élevés de faux likes, fausses demandes de suivi et comptes spam bloqués. La Commission européenne a ensuite demandé des informations puis ouvert une procédure DSA portant notamment sur la manipulation inauthentique coordonnée et l’exploitation automatisée. Cette chaîne ferme activité inauthentique, cible politique et risque de distribution, mais **pas** le commanditaire ultime, la part incrémentale d’exposition humaine, la persuasion ni le résultat électoral contrefactuel. [SRC-005, SRC-006, SRC-007, SRC-008]

## Bots, faux comptes et coordination ne sont pas interchangeables

Les catégories opérationnelles doivent rester séparées. Un bot désigne une automatisation ; un faux compte implique une identité trompeuse ; un compte très actif ou un « amplificateur » peut être humain ; une coordination peut exister sans automatisation ; plusieurs comptes peuvent se ressembler sans partager un commandement unique. Meta et TikTok décrivent eux-mêmes leurs enquêtes d’opérations d’influence à partir de comportements coordonnés, identités trompeuses et liens techniques plutôt qu’à partir du seul contenu. Ces définitions servent à caractériser les mécaniques de plateforme, pas à prouver indépendamment un client ou un État commanditaire. [SRC-006, SRC-009]

Le cas Portal Kombat illustre la frontière opérateur/client. VIGINUM attribue un rôle majeur à TigerWeb dans la création et l’administration de l’infrastructure, mais indique que l’identité du donneur d’ordre ultime n’est pas établie à ce stade. De même, les liens russophones et les chaînes de diffusion observés autour de Matriochka ferment plusieurs arêtes opérationnelles sans produire à eux seuls un ordre authentifié d’un commanditaire politique ou étatique. [SRC-002, SRC-004]

## Amplification mesurée, puis exposition humaine

La littérature indépendante ferme une partie supplémentaire de la chaîne. Une analyse Nature Communications de quelque 14 millions de messages montre que les bots ont joué un rôle disproportionné dans les premiers moments de diffusion de contenus à faible crédibilité et ont ciblé des utilisateurs influents ; des humains ont ensuite repartagé du contenu initialement diffusé par ces bots. Cela ferme `bot -> amplification -> retransmission humaine` dans ce corpus, sans fermer `retransmission -> changement de vote`. [SRC-012]

L’étude de 2019 sur les élections européennes fournit un autre type de mesure : des « amplificateurs » apparaissent autour de partis de plusieurs orientations et, dans certains cas, au-delà des frontières nationales. Cette observation interdit de transformer le mécanisme en propriété d’un seul camp politique. Mais une classification réseau d’amplificateur ne prouve ni automatisation, ni fausse identité, ni tasking commun. [SRC-015]

## Deux contrôles négatifs importants

Premièrement, l’étude PLOS One sur les élections européennes de 2019, portant sur près de 400 000 tweets provenant de 863 comptes sélectionnés, n’a pas trouvé dans son corpus de réseau organisé destiné à diffuser de la désinformation ; les sources de désinformation y restaient périphériques. Cela montre que l’existence générale de bots ou de campagnes documentées ailleurs ne justifie pas d’en inférer une présence dominante dans chaque scrutin. [SRC-011]

Deuxièmement, l’étude longitudinale Nature Communications sur l’IRA en 2016 montre une exposition très concentrée, 1 % des utilisateurs représentant environ 70 % des expositions, et une exposition largement dépassée par celle aux médias et acteurs politiques domestiques. Elle ne détecte pas de relation significative avec les changements d’attitudes, la polarisation ou le comportement de vote. Le cas russe 2016, déjà traité par INV-018, reste donc un contrôle utile contre `volume d’activité -> effet électoral nécessaire`. [SRC-013]

Un troisième contrôle vient de l’expérience de bots neutres sur Twitter : les choix de connexions initiales modifient fortement la composition ultérieure de l’environnement informationnel et l’exposition à des comptes automatisés ou à faible crédibilité, sans preuve forte et cohérente d’un biais partisan du fil lui-même. L’environnement social peut donc produire des asymétries d’exposition sans que celles-ci prouvent un commandement politique de la plateforme. [SRC-014]

## Ce qui est établi

1. Des réseaux de comptes ou infrastructures coordonnés utilisent effectivement automatisation, fausses identités, répétition, faux engagement et autres techniques pour augmenter artificiellement la visibilité de contenus politiques ou géopolitiques.
2. Dans certains cas, l’opérateur technique, la structure de diffusion, la cible politique et l’amplification sont documentés séparément.
3. Une amplification par bots peut conduire à une retransmission humaine mesurable.
4. Les mécanismes sont transpartisans comme capacité : le simple fait d’amplifier ne permet pas d’inférer l’origine, l’idéologie, l’inauthenticité ou le tasking.
5. Les plateformes et régulateurs disposent de signaux importants de détection, mais leurs compteurs de suppressions ou de faux engagements ne constituent pas des dénominateurs d’exposition humaine ou d’effet électoral.

## Ce qui n’est pas établi

- une prévalence générale des bots ou faux comptes sur l’ensemble des élections France/UE ;
- un commanditaire unique déductible d’un réseau, d’une infrastructure ou d’une orientation de contenu ;
- que tout amplificateur est automatisé ou inauthentique ;
- que toute détection ou suppression correspond à une exposition humaine effective ;
- un effet uniforme de l’amplification artificielle sur les attitudes ;
- un effet causal démontré sur un résultat électoral en France ou dans l’Union européenne.

## Frontières forensiques

`bot != faux compte` ; `faux compte != acteur étranger` ; `réseau != coordination` ; `coordination != tasking` ; `astroturfing != automatisation` ; `détection != prévalence` ; `suppression de comptes != effet` ; `impressions/reach != persuasion` ; `amplification != vote_change` ; `operation != electoral_effect`.

Le résultat central est donc borné : **l’amplification artificielle est un mécanisme réel et mesurable d’influence sur la visibilité, parfois jusqu’à la retransmission humaine ; la causalité électorale demeure une arête distincte et généralement non fermée**.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:4|EDI_DECISIVE:7|SRC_COMPLETE:15/15

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-09
- **freshness:** France/EU 2019-2024 election cases, 2024 Romanian enforcement and 2018-2024 peer-reviewed amplification/effect controls rechecked; INV-018 used only as comparator.
- **period:** 2018-2026

### MANIPULATION_REPORT
- **assumptions:**
  - artificial activity can change visible engagement without changing votes
  - platform takedown counters are not audience denominators
- **clusters:**
  - POWER
  - NETWORK
  - FRAMING
  - TEMPORAL
- **complexity:** APEX
- **implicit:**
  - network structure can produce amplification without a single command chain
  - human selection and domestic political content compete with covert exposure
- **input_kind:** RUN_CARD
- **mission_mode:** RECHECK_EXTEND
- **patterns:**
  - botting
  - fake persona
  - coordinated posting
  - retweet amplification
  - reply flooding
  - fake likes/follows
  - automation
  - SEO amplification
  - cross-account reuse
  - astroturfing
- **priorities:**
  - France/EU documented cases
  - operator/client/tasking edges
  - incremental amplification
  - human retransmission
  - negative controls
  - causal effect ceiling
- **query_guidance:** separate account type, coordination, operator/client/tasking, incremental amplification, human exposure, persuasion and electoral effect; prefer official/platform mechanics plus independent measurement controls
- **rhetorical:** bounded operation-amplification-effect chain
- **speaker:**
  - **goal:** test artificial-amplification mechanisms without collapsing account labels into command or reach into vote change
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** operator
  - **S02:** client
  - **S03:** account
  - **S04:** bot
  - **S05:** fake persona
  - **S06:** coordination
  - **S07:** tasking
  - **S08:** content
  - **S09:** retweet/reply
  - **S10:** fake engagement
  - **S11:** amplification
  - **S12:** organic baseline
  - **S13:** exposure
  - **S14:** persuasion
  - **S15:** electoral effect
- **threats:**
  - bot-label inflation
  - network-to-command inflation
  - platform-self-report circularity
  - takedown-to-prevalence inflation
  - reach-to-persuasion inflation
  - operation-to-vote-change inflation

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - tasking records
    - incremental organic baseline
    - France/EU causal outcome design
  - **input_ids:**
    - LED-001
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no universal bot prevalence
    - no automatic client/tasking inference
    - no generalized electoral causal closure
  - **not_computable:**
    - France/EU counterfactual vote effect absent causal design
    - ultimate client/tasking absent authenticated records in several cases
  - **operations_applied:**
    - bounded mechanism mapping
  - **reason:** relevant to operator/control, coordinated-network structure, deceptive presentation/amplification and election timing
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-003
    - CLM-004
    - CLM-005
    - CLM-006
    - CLM-007
  - **status:** DONE
  - **trigger:** symbol routing
- **item 2:**
  - **gaps:**
    - tasking records
    - incremental organic baseline
    - France/EU causal outcome design
  - **input_ids:**
    - LED-001
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no universal bot prevalence
    - no automatic client/tasking inference
    - no generalized electoral causal closure
  - **not_computable:**
    - France/EU counterfactual vote effect absent causal design
    - ultimate client/tasking absent authenticated records in several cases
  - **operations_applied:**
    - bounded mechanism mapping
  - **reason:** relevant to operator/control, coordinated-network structure, deceptive presentation/amplification and election timing
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-003
    - CLM-004
    - CLM-005
    - CLM-006
    - CLM-007
  - **status:** DONE
  - **trigger:** symbol routing
- **item 3:**
  - **gaps:**
    - tasking records
    - incremental organic baseline
    - France/EU causal outcome design
  - **input_ids:**
    - LED-001
  - **module:** clusters/FRAMING.md
  - **negative_results:**
    - no universal bot prevalence
    - no automatic client/tasking inference
    - no generalized electoral causal closure
  - **not_computable:**
    - France/EU counterfactual vote effect absent causal design
    - ultimate client/tasking absent authenticated records in several cases
  - **operations_applied:**
    - bounded mechanism mapping
  - **reason:** relevant to operator/control, coordinated-network structure, deceptive presentation/amplification and election timing
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-003
    - CLM-004
    - CLM-005
    - CLM-006
    - CLM-007
  - **status:** DONE
  - **trigger:** symbol routing
- **item 4:**
  - **gaps:**
    - tasking records
    - incremental organic baseline
    - France/EU causal outcome design
  - **input_ids:**
    - LED-001
  - **module:** clusters/TEMPORAL.md
  - **negative_results:**
    - no universal bot prevalence
    - no automatic client/tasking inference
    - no generalized electoral causal closure
  - **not_computable:**
    - France/EU counterfactual vote effect absent causal design
    - ultimate client/tasking absent authenticated records in several cases
  - **operations_applied:**
    - bounded mechanism mapping
  - **reason:** relevant to operator/control, coordinated-network structure, deceptive presentation/amplification and election timing
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-003
    - CLM-004
    - CLM-005
    - CLM-006
    - CLM-007
  - **status:** DONE
  - **trigger:** symbol routing

### SCOPING_REPORT
- **actors_institutions:**
  - VIGINUM
  - European Commission
  - TikTok
  - Meta
  - French Senate
  - platform users
  - independent researchers
- **domains:**
  - bots
  - fake accounts
  - coordinated inauthentic behavior
  - astroturfing
  - fake engagement
  - amplification
  - elections
  - exposure
  - persuasion
  - electoral effect
- **evidence_limits:**
  - platform enforcement counters are self-reported
  - several operator/client/tasking chains remain partial
  - France/EU incremental exposure denominators are sparse
  - no France/EU causal winner-change design
- **exclusions:**
  - bot as synonym for fake account
  - network as proof of coordination
  - coordination as proof of tasking
  - platform takedown as prevalence
  - amplification as persuasion
  - operation as electoral outcome
- **geo:** France/EU with directly transposable comparators
- **object_coverage:** Covers RRN/Doppelganger, Portal Kombat, Matriochka, Romania 2024, EU 2019 and peer-reviewed amplification/effect controls.
- **object_question:** When do bots, fake accounts, coordinated networks and astroturfing measurably create incremental political exposure, who operates or tasks them, and what evidence closes persuasion or electoral effect?
- **period:** 2018-2026

### CREDO
- **lead_question:** Does artificial account activity measurably amplify political content, and where does the causal chain stop?
- **object_question:** Trace operator/client/tasking -> accounts/automation/coordination -> content -> incremental amplification -> exposure -> reception/behavior -> electoral effect.
- **search_principle:** mechanism first; require behavioral/technical evidence for coordination, authenticated records for tasking, and causal designs for persuasion/electoral effect

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** RECHECK_EXTEND
- **patterns:**
  - operator->accounts
  - accounts->coordination
  - coordination->amplification
  - amplification->exposure
  - exposure->human reshare
  - reshare->persuasion
  - persuasion->vote/outcome
- **priorities:**
  - classification precision
  - tasking
  - incremental amplification
  - negative controls
  - causal effect
- **query_guidance:** direct operation evidence for mechanics; independent studies for reach and downstream effect
- **speaker:**
  - **goal:** bounded artificial-amplification mechanism test
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **threats:**
  - automation overclassification
  - attribution inflation
  - effect inflation

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** Platforms and research distinguish automation, deceptive identity, coordination and tasking; some operator/client links remain unresolved.
  - **resolution:** Require separate evidence for account type, coordination, operator, client and command.
  - **thesis:** Large numbers of bots or fake accounts prove a centrally commanded foreign operation.
- **item 2:**
  - **antithesis:** Human retransmission can occur, but exposure is concentrated and some election studies find limited reach or no meaningful voting relationship.
  - **resolution:** Close amplification separately from persuasion and electoral counterfactuals.
  - **thesis:** Artificial amplification necessarily persuades voters or changes election outcomes.
- **item 3:**
  - **antithesis:** EU-election research identifies amplifiers across parties, and neutral-bot work shows ecosystem effects without strong feed-bias evidence.
  - **resolution:** Treat automation/amplification as a mechanism property, not an actor or ideology label.
  - **thesis:** Bot activity is exceptional and only associated with one political side or foreign actors.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **from:** operator/provider
  - **resource:** accounts, websites, automation tooling and content
  - **support:**
    - FCT-001
    - FCT-003
    - FCT-004
    - FCT-007
  - **to:** coordinated amplification infrastructure
- **item 2:**
  - **from:** inauthentic network
  - **resource:** posts, replies, retweets, likes, follows and repeated URLs
  - **support:**
    - FCT-002
    - FCT-009
    - FCT-010
    - FCT-019
    - FCT-023
    - FCT-029
  - **to:** platform visibility/engagement signals
- **item 3:**
  - **from:** platform visibility and network exposure
  - **resource:** attention and human retransmission opportunities
  - **support:**
    - FCT-024
    - FCT-025
    - FCT-027
  - **to:** users
- **item 4:**
  - **from:** users
  - **resource:** reshare, attention, belief and possible behavior
  - **support:**
    - FCT-024
    - FCT-026
    - FCT-028
  - **to:** political discourse/election

### ACTOR_NETWORK_MAP
- **item 1:**
  - **edge:** detects and attributes operation-level infrastructure/behavior
  - **from:** VIGINUM / regulators
  - **support:**
    - FCT-001
    - FCT-003
    - FCT-004
    - FCT-005
    - FCT-007
  - **to:** public evidence base
- **item 2:**
  - **edge:** detect and remove inauthentic networks / fake engagement
  - **from:** platforms
  - **support:**
    - FCT-009
    - FCT-010
    - FCT-011
    - FCT-017
    - FCT-018
  - **to:** accounts and distribution systems
- **item 3:**
  - **edge:** artificially repeat or boost content
  - **from:** coordinated/automated accounts
  - **support:**
    - FCT-007
    - FCT-019
    - FCT-023
    - FCT-029
  - **to:** audience-facing visibility
- **item 4:**
  - **edge:** may reshare or ignore exposed content
  - **from:** audience/users
  - **support:**
    - FCT-021
    - FCT-024
    - FCT-025
    - FCT-026
  - **to:** further diffusion / no effect

### IMPACT_MAP
- **case_specific:**
  - RRN/Doppelganger
  - Portal Kombat
  - Matriochka
  - Romania 2024
  - EU 2019 amplifier patterns
- **effect_limit:** Mechanism closes strongly through artificial amplification in several cases and to human retransmission in one peer-reviewed comparator; persuasion and electoral counterfactuals remain heterogeneous or unclosed.
- **not_established:**
  - general bot/fake-account prevalence across elections
  - common command from network structure alone
  - ultimate client/tasking for several operations
  - uniform persuasion effect
  - France/EU causal electoral outcome
- **verified:**
  - coordinated inauthentic networks and automated amplification exist in France/EU-adjacent cases
  - Portal Kombat bot amplification is corroborated by VIGINUM/Senate evidence
  - TikTok reported a named 4,453-account Romanian political-promotion network
  - peer-reviewed work shows bots can disproportionately amplify low-credibility content and induce human resharing

### CONTRADICTION_LEDGER
- **item 1:**
  - **ids:**
    - FCT-019
    - FCT-021
    - FCT-023
  - **resolution:** Artificial amplification is real in some operations but not ubiquitous or dominant in every election information environment.
  - **status:** RESOLVED_HETEROGENEOUS
  - **tension:** documented amplification versus limited reach
- **item 2:**
  - **ids:**
    - FCT-010
    - FCT-011
    - FCT-018
    - FCT-025
  - **resolution:** Enforcement volume measures detected/blocked activity, not unique human exposure or persuasion.
  - **status:** RESOLVED_STAGE_SEPARATION
  - **tension:** large platform takedown counters versus measured exposure
- **item 3:**
  - **ids:**
    - FCT-009
    - FCT-013
    - FCT-015
    - FCT-016
  - **resolution:** Named network activity and DSA scrutiny are established; causal winner-change and ultimate tasking remain separate unresolved edges.
  - **status:** RESOLVED_EVIDENCE_LEVEL
  - **tension:** Romania manipulation risk versus causal election claim

### VERIFICATION_REPORT
- **circular_families:**
  - Platform takedown and network counts are treated as platform self-reports; official VIGINUM/Commission material and independent peer-reviewed studies provide separate operational and effect controls.
- **downgraded_ids:**
  - NONE
- **none_found_claims:**
  - generalized France/EU bot prevalence denominator
  - authenticated client/tasking for several central networks
  - France/EU causal vote or winner effect from artificial amplification
- **remaining_gaps:**
  - operator/client/tasking records
  - incremental artificial-versus-organic exposure denominators
  - France/EU causal persuasion/voting designs
- **reopened_ids:**
  - FCT-001
  - FCT-002
  - FCT-003
  - FCT-004
  - FCT-005
  - FCT-006
  - FCT-007
  - FCT-008
  - FCT-009
  - FCT-010
  - FCT-011
  - FCT-012
  - FCT-013
  - FCT-014
  - FCT-015
  - FCT-016
  - FCT-017
  - FCT-018
  - FCT-019
  - FCT-020
  - FCT-021
  - FCT-022
  - FCT-023
  - FCT-024
  - FCT-025
  - FCT-026
  - FCT-027
  - FCT-028
  - FCT-029
  - FCT-030
- **sources_reopened:** 15
- **upgraded_ids:**
  - NONE
- **verdict:** READY_FOR_PRE_GATE

### EDI_REPORT
- **corpus:**
  - **coverage:** France/EU official operation reports, platform election-integrity records, EU regulatory proceedings, parliamentary corroboration and peer-reviewed amplification/effect studies
  - **independence:** official regulator/security, platform, parliamentary and academic families
  - **limits:**
    - platform self-report for enforcement counts
    - cross-case definitions differ
    - direct electoral-effect evidence sparse
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **gap_type:** GENERALIZATION
    - **independent_families:** 3
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES
    - **gap_type:** CLASSIFICATION
    - **independent_families:** 2
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** YES
    - **gap_type:** TASKING
    - **independent_families:** 2
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** YES
    - **gap_type:** EFFECT
    - **independent_families:** 3
  - **item 5:**
    - **claim_id:** CLM-005
    - **direct_object:** YES
    - **gap_type:** NONE
    - **independent_families:** 3
  - **item 6:**
    - **claim_id:** CLM-006
    - **direct_object:** YES
    - **gap_type:** EFFECT
    - **independent_families:** 2
  - **item 7:**
    - **claim_id:** CLM-007
    - **direct_object:** YES
    - **gap_type:** EFFECT
    - **independent_families:** 3
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** multi-operator/regulator/platform/research
  - **perspective:** operation+platform+network+effect-control
  - **stratification:** operator/tasking->accounts->coordination->amplification->exposure->persuasion->outcome
  - **temporal:** 2018-2026
- **edi:**
  - **assessment:** STRONG_FOR_OPERATION_AND_ARTIFICIAL_AMPLIFICATION; MODERATE_FOR_HUMAN_RETRANSMISSION; WEAK_FOR_TASKING_AND_ELECTORAL_OUTCOME
  - **flags:**
    - CIB_DOCUMENTED
    - BOT_AMPLIFICATION
    - FAKE_ENGAGEMENT
    - TASKING_GAP
    - PREVALENCE_GAP
    - HUMAN_RESHARE
    - NULL_EFFECT_CONTROL
    - ELECTORAL_EFFECT_GAP
- **source_counts:**
  - **primary_or_direct:** 10
  - **provenance_families:** 5
  - **secondary_or_peer_reviewed:** 5
  - **total:** 15

### RESPONSIBILITY_MAP
- **item 1:**
  - **actor:** RRN/Portal Kombat/Matriochka operators and identified service providers
  - **documented_action:** operate deceptive sites/accounts and coordinated amplification systems
  - **intent:** NARRATIVE_AMPLIFICATION
  - **scope:** ultimate client/state tasking not uniformly established
  - **support:**
    - FCT-001
    - FCT-003
    - FCT-004
    - FCT-005
    - FCT-007
    - FCT-019
- **item 2:**
  - **actor:** TikTok-reported Romanian inauthentic networks
  - **documented_action:** promote named political actors and generate inauthentic engagement
  - **intent:** POLITICAL_PROMOTION
  - **scope:** platform attribution; causal electoral effect and ultimate tasking not established
  - **support:**
    - FCT-009
    - FCT-010
    - FCT-011
    - FCT-012
- **item 3:**
  - **actor:** Platforms
  - **documented_action:** detect and remove CIB/covert influence, spam and fake engagement
  - **intent:** PLATFORM_INTEGRITY
  - **scope:** takedown count is not prevalence/effect denominator
  - **support:**
    - FCT-010
    - FCT-011
    - FCT-017
    - FCT-018
- **item 4:**
  - **actor:** European Commission / VIGINUM / French Senate
  - **documented_action:** investigate, characterize and regulate information-manipulation/election risks
  - **intent:** PUBLIC_OVERSIGHT
  - **scope:** investigation or risk finding is not causal election proof
  - **support:**
    - FCT-001
    - FCT-013
    - FCT-014
    - FCT-015
    - FCT-016
    - FCT-019
    - FCT-020
- **item 5:**
  - **actor:** Independent researchers
  - **documented_action:** measure network amplification, exposure concentration, human retransmission and downstream null/limited effects
  - **intent:** MEASUREMENT
  - **scope:** external validity to all France/EU elections remains bounded
  - **support:**
    - FCT-021
    - FCT-023
    - FCT-024
    - FCT-025
    - FCT-026
    - FCT-027
    - FCT-028
    - FCT-029
    - FCT-030

### NEXT_QUERIES
- Reopen tasking only with authenticated operator-client instructions, payment/contract records or technical evidence tying a named network to a principal.
- Reopen prevalence/amplification only with reproducible platform-scale denominators separating automated/inauthentic activity from organic baseline exposure.
- Reopen electoral-effect closure on a France/EU experiment or credible quasi-experimental design linking incremental artificial exposure to persuasion, turnout, vote choice or outcome.

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-003,QRY-005,QRY-007,QRY-009,QRY-011,QRY-013,QRY-015,QRY-017,QRY-019,QRY-021,QRY-023,QRY-025,QRY-027,QRY-029 | support:- | counter:- | results:FCT-003,FCT-004,FCT-007,FCT-009,FCT-019,FCT-021,FCT-023,FCT-025,FCT-026,FCT-029 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-011,QRY-017,QRY-023,QRY-029 | support:- | counter:- | results:FCT-011,FCT-012,FCT-017,FCT-023,FCT-029,FCT-030 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-003,QRY-007,QRY-011,QRY-015 | support:- | counter:- | results:FCT-004,FCT-008,FCT-012,FCT-016 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-001,QRY-005,QRY-007,QRY-009,QRY-013,QRY-015,QRY-019,QRY-021,QRY-029 | support:- | counter:- | results:FCT-001,FCT-005,FCT-007,FCT-009,FCT-013,FCT-015,FCT-019,FCT-021,FCT-029 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-003,QRY-007,QRY-009,QRY-019,QRY-023,QRY-029 | support:- | counter:- | results:FCT-003,FCT-007,FCT-010,FCT-019,FCT-023,FCT-024,FCT-029 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-023,QRY-025,QRY-027 | support:- | counter:- | results:FCT-024,FCT-025,FCT-026,FCT-027,FCT-028 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-021,QRY-025,QRY-027,QRY-029 | support:- | counter:- | results:FCT-021,FCT-022,FCT-025,FCT-026,FCT-028,FCT-030 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-004,QRY-008,QRY-010,QRY-020,QRY-022,QRY-024,QRY-026,SRC-002,SRC-004,SRC-005,SRC-010,SRC-011,SRC-012,SRC-013 | support:FCT-003,FCT-007,FCT-009,FCT-019,FCT-023,FCT-024 | counter:FCT-021,FCT-025 | results:FCT-003,FCT-007,FCT-009,FCT-019,FCT-023,FCT-024,FCT-021,FCT-025 | final:SUPPORTED | gap:GENERALIZATION
CLM-002 | attempts:QRY-004,QRY-012,QRY-018,QRY-030,SRC-002,SRC-006,SRC-009,SRC-015 | support:FCT-011,FCT-017,FCT-029 | counter:FCT-004,FCT-012,FCT-030 | results:FCT-011,FCT-017,FCT-029,FCT-004,FCT-012,FCT-030 | final:PARTIAL | gap:CLASSIFICATION
CLM-003 | attempts:QRY-004,QRY-008,QRY-012,QRY-016,SRC-002,SRC-004,SRC-006,SRC-008 | support:FCT-004,FCT-008,FCT-012,FCT-016 | counter:- | results:FCT-004,FCT-008,FCT-012,FCT-016 | final:SUPPORTED | gap:TASKING
CLM-004 | attempts:QRY-004,QRY-020,QRY-024,QRY-026,SRC-002,SRC-010,SRC-012,SRC-013 | support:FCT-019,FCT-023,FCT-024,FCT-025 | counter:FCT-026 | results:FCT-019,FCT-023,FCT-024,FCT-025,FCT-026 | final:SUPPORTED | gap:EFFECT
CLM-005 | attempts:QRY-004,QRY-006,QRY-020,QRY-022,QRY-030,SRC-002,SRC-003,SRC-010,SRC-011,SRC-015 | support:FCT-005,FCT-019,FCT-021,FCT-029 | counter:- | results:FCT-005,FCT-019,FCT-021,FCT-029 | final:SUPPORTED | gap:NONE
CLM-006 | attempts:QRY-010,QRY-014,QRY-016,SRC-005,SRC-007,SRC-008 | support:FCT-009,FCT-013,FCT-015 | counter:FCT-010,FCT-014,FCT-016 | results:FCT-009,FCT-013,FCT-015,FCT-010,FCT-014,FCT-016 | final:PARTIAL | gap:EFFECT
CLM-007 | attempts:QRY-004,QRY-020,QRY-022,QRY-026,QRY-028,QRY-030,SRC-002,SRC-010,SRC-011,SRC-013,SRC-014,SRC-015 | support:FCT-019,FCT-029 | counter:FCT-020,FCT-021,FCT-022,FCT-025,FCT-026,FCT-028,FCT-030 | results:FCT-019,FCT-029,FCT-020,FCT-021,FCT-022,FCT-025,FCT-026,FCT-028,FCT-030 | final:PARTIAL | gap:EFFECT

## STATUS_DELTA_V1
DELTA-001 | FCT-019 | FACT|✦ | FACT|✧ | single independent corroborated claim does not need strong tier for this run

## OPEN_GAPS_V1
CLM-001 | CLM | SUPPORTED | GENERALIZATION | Amplification is case-specific and heterogeneous; no universal prevalence or effect denominator exists across elections.
CLM-002 | CLM | PARTIAL | CLASSIFICATION | Automation, identity deception, coordination and tasking are distinct properties and require separate evidence.
CLM-003 | CLM | SUPPORTED | TASKING | Authenticated client/tasking records are absent for several central France/EU cases.
CLM-004 | CLM | SUPPORTED | EFFECT | The reviewed evidence does not close a general amplification -> persuasion -> vote-change chain.
CLM-006 | CLM | PARTIAL | EFFECT | Platform and regulatory records establish network activity and risk scrutiny, not a causal vote or winner counterfactual.
CLM-007 | CLM | PARTIAL | EFFECT | No France/EU causal design closes incremental artificial amplification -> persuasion/behavior -> changed electoral outcome.

SEMANTIC_COUNTS_V1:LED:1|CLM:7|AXS:6|CAU:1|CTRL:9|ACT:5

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-003","QRY-005","QRY-007","QRY-009","QRY-011","QRY-013","QRY-015","QRY-017","QRY-019","QRY-021","QRY-023","QRY-025","QRY-027","QRY-029"],"evidence_excerpt":"documented automated/coordinated amplification exists case-specifically; client/tasking and downstream electoral effect frequently remain unclosed; EU cases include both positive and negative controls","kind":"DECISIVE","lead":"When do bots, fake accounts, coordinated networks and astroturfing measurably create incremental political exposure, and when do operator/tasking/persuasion/electoral-effect claims remain unclosed?","linked_ids":["AXS-001","AXS-002","AXS-003","AXS-004","AXS-005","AXS-006"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-003","FCT-004","FCT-007","FCT-009","FCT-019","FCT-021","FCT-023","FCT-025","FCT-026","FCT-029"],"routes":["POWER","NETWORK","FRAMING","TEMPORAL"],"source_id":"RUN_CARD","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Bots, inauthentic accounts and coordinated networks can materially amplify political or low-credibility content in documented cases.","claimant":"INV-097","counter":["FCT-021","FCT-025"],"gap":"Amplification is case-specific and heterogeneous; no universal prevalence or effect denominator exists across elections.","gap_type":"GENERALIZATION","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-003","FCT-007","FCT-009","FCT-019","FCT-023","FCT-024"]}
CLM-002 | {"claim":"A bot, fake account, amplifier or coordinated network label is sufficient to establish a single operator or common command.","claimant":"INV-097","counter":["FCT-004","FCT-012","FCT-030"],"gap":"Automation, identity deception, coordination and tasking are distinct properties and require separate evidence.","gap_type":"CLASSIFICATION","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-011","FCT-017","FCT-029"]}
CLM-003 | {"claim":"Public evidence frequently closes the operation or service-provider layer before it closes the ultimate client or tasking chain.","claimant":"INV-097","counter":"NONE_FOUND","gap":"Authenticated client/tasking records are absent for several central France/EU cases.","gap_type":"TASKING","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-004","FCT-008","FCT-012","FCT-016"]}
CLM-004 | {"claim":"Artificial amplification can increase exposure or human retransmission without establishing persuasion or electoral outcome.","claimant":"INV-097","counter":["FCT-026"],"gap":"The reviewed evidence does not close a general amplification -> persuasion -> vote-change chain.","gap_type":"EFFECT","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-019","FCT-023","FCT-024","FCT-025"]}
CLM-005 | {"claim":"France/EU election contexts contain both documented coordinated amplification and credible negative controls where organized disinformation reach was limited or not detected.","claimant":"INV-097","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-005","FCT-019","FCT-021","FCT-029"]}
CLM-006 | {"claim":"The Romanian 2024 case proves that a 4,453-account inauthentic network caused the presidential election result.","claimant":"INV-097","counter":["FCT-010","FCT-014","FCT-016"],"gap":"Platform and regulatory records establish network activity and risk scrutiny, not a causal vote or winner counterfactual.","gap_type":"EFFECT","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-009","FCT-013","FCT-015"]}
CLM-007 | {"claim":"The reviewed corpus establishes a generalized causal electoral effect from bots, fake accounts or artificial amplification in France/EU elections.","claimant":"INV-097","counter":["FCT-020","FCT-021","FCT-022","FCT-025","FCT-026","FCT-028","FCT-030"],"gap":"No France/EU causal design closes incremental artificial amplification -> persuasion/behavior -> changed electoral outcome.","gap_type":"EFFECT","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-019","FCT-029"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-011","QRY-017","QRY-023","QRY-029"],"axis":"definitions_and_account_taxonomy","links":["LED-001"],"question":"What distinguishes bots, fake accounts, amplifiers, coordinated inauthentic behavior and astroturfing?","result_ids":["FCT-011","FCT-012","FCT-017","FCT-023","FCT-029","FCT-030"],"sought_objects":["automation","deceptive identity","coordination","amplifier classification"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-001","QRY-003","QRY-007","QRY-011","QRY-015"],"axis":"operator_client_tasking","links":["LED-001"],"question":"Which cases close operator or service-provider identity, and which close client or command/tasking?","result_ids":["FCT-004","FCT-008","FCT-012","FCT-016"],"sought_objects":["operator","provider","client","state command","tasking records"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-001","QRY-005","QRY-007","QRY-009","QRY-013","QRY-015","QRY-019","QRY-021","QRY-029"],"axis":"france_eu_election_cases","links":["LED-001"],"question":"Which France/EU election-adjacent cases document inauthentic networks or artificial amplification?","result_ids":["FCT-001","FCT-005","FCT-007","FCT-009","FCT-013","FCT-015","FCT-019","FCT-021","FCT-029"],"sought_objects":["Portal Kombat","RRN","Matriochka","Romania 2024","EU 2019"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-003","QRY-007","QRY-009","QRY-019","QRY-023","QRY-029"],"axis":"incremental_amplification","links":["LED-001"],"question":"What evidence shows artificial amplification rather than mere presence of accounts or content?","result_ids":["FCT-003","FCT-007","FCT-010","FCT-019","FCT-023","FCT-024","FCT-029"],"sought_objects":["fake engagement","automated reposting","bot early diffusion","retweet amplification","baseline organic reach"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-023","QRY-025","QRY-027"],"axis":"exposure_reception","links":["LED-001"],"question":"When does artificial amplification reach humans, and what evidence exists for reception or behavior?","result_ids":["FCT-024","FCT-025","FCT-026","FCT-027","FCT-028"],"sought_objects":["human reshare","exposure concentration","attitude change","voting behavior"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-021","QRY-025","QRY-027","QRY-029"],"axis":"prevalence_effect_controls","links":["LED-001"],"question":"What negative controls prevent detection or amplification from becoming prevalence, persuasion or vote-change claims?","result_ids":["FCT-021","FCT-022","FCT-025","FCT-026","FCT-028","FCT-030"],"sought_objects":["negative network finding","relative exposure denominator","null voting relationship","classification limits"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"PARTIAL","counter":["FCT-021","FCT-025","FCT-026","FCT-028","FCT-030"],"limit":"The chain is strongly supported through operation and amplification in several cases and reaches human retransmission in a peer-reviewed comparator, but client/tasking, persuasion and electoral outcome remain unclosed or heterogeneous.","mechanism":"operator/client/tasking -> automated or inauthentic account network -> coordinated posting/retweet/reply/fake engagement -> incremental amplification -> human exposure/retransmission -> possible persuasion/behavior -> possible electoral effect","status":"SUPPORTED","support":["FCT-003","FCT-007","FCT-009","FCT-019","FCT-023","FCT-024","FCT-029"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"bot != fake account","status":"PASS","support":["FCT-011","FCT-012","FCT-030"]}
CTRL-002 | {"control":"fake account != foreign actor","status":"PASS","support":["FCT-009","FCT-012","FCT-016"]}
CTRL-003 | {"control":"network != coordination","status":"PASS","support":["FCT-021","FCT-030"]}
CTRL-004 | {"control":"coordination != tasking","status":"PASS","support":["FCT-004","FCT-008","FCT-012"]}
CTRL-005 | {"control":"astroturfing != automation","status":"PASS","support":["FCT-017","FCT-029","FCT-030"]}
CTRL-006 | {"control":"detection != prevalence","status":"PASS","support":["FCT-018","FCT-021","FCT-025"]}
CTRL-007 | {"control":"suppression or enforcement count != effect","status":"PASS","support":["FCT-010","FCT-014","FCT-016","FCT-018"]}
CTRL-008 | {"control":"reach or amplification != persuasion","status":"PASS","support":["FCT-019","FCT-023","FCT-024","FCT-025","FCT-026"]}
CTRL-009 | {"control":"operation != electoral effect","status":"PASS","support":["FCT-020","FCT-026","FCT-028","FCT-030"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"creates and/or operates coordinated websites and amplification infrastructure","actor":"Documented influence-operation operators/providers","intent":"AMPLIFY_NARRATIVES","status":"DONE","support":["FCT-001","FCT-003","FCT-004","FCT-005","FCT-007"]}
ACT-002 | {"action":"uses inauthentic accounts, fake engagement or coordinated posting to alter apparent activity and visibility","actor":"Inauthentic account networks","intent":"ARTIFICIAL_AMPLIFICATION","status":"DONE","support":["FCT-002","FCT-007","FCT-009","FCT-010","FCT-019"]}
ACT-003 | {"action":"detects, labels or removes covert influence and deceptive-account networks","actor":"Platforms","intent":"INTEGRITY_ENFORCEMENT","status":"DONE","support":["FCT-009","FCT-010","FCT-011","FCT-017","FCT-018"]}
ACT-004 | {"action":"investigates automated exploitation and coordinated inauthentic manipulation as election-integrity risks","actor":"European Commission / regulators","intent":"DSA_OVERSIGHT","status":"DONE","support":["FCT-013","FCT-014","FCT-015","FCT-016"]}
ACT-005 | {"action":"measures amplification, exposure concentration, human retransmission and null/limited downstream effects","actor":"Independent researchers","intent":"MEASUREMENT","status":"DONE","support":["FCT-021","FCT-023","FCT-024","FCT-025","FCT-026","FCT-027","FCT-028","FCT-029","FCT-030"]}

SEARCH_ACTIVITY_V1:WEB:15|FETCH:15|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | FCT-019 | REPAIR_FACT
SYS-004 | SYS | MNEMO_UNAVAILABLE | MnemoLite | - | MNEMO_Q
SYS-005 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | VIGINUM RRN Doppelganger inauthentic social accounts France Europe 2023
QRY-002 | FETCH | FOUND | SRC-001 | https://www.sgdsn.gouv.fr/viginum/publications/rrn-une-campagne-numerique-de-manipulation-de-linformation-complexe-et | VIGINUM RRN Doppelganger inauthentic social accounts France Europe 2023
QRY-003 | WEB | FOUND | - | - | VIGINUM Portal Kombat TigerWeb automation SEO bots February 2024
QRY-004 | FETCH | FOUND | SRC-002 | https://www.sgdsn.gouv.fr/viginum/publications/portal-kombat-suite-des-investigations-sur-le-reseau-structure-et-coordonne-de | VIGINUM Portal Kombat TigerWeb automation SEO bots February 2024
QRY-005 | WEB | FOUND | - | - | VIGINUM Portal Kombat extension European elections April 2024 224 portals
QRY-006 | FETCH | FOUND | SRC-003 | https://www.sgdsn.gouv.fr/viginum/publications/portal-kombat-extension-du-reseau-de-propagande-russe | VIGINUM Portal Kombat extension European elections April 2024 224 portals
QRY-007 | WEB | FOUND | - | - | VIGINUM Matriochka coordinated seeder quoter accounts media fact checkers June 2024
QRY-008 | FETCH | FOUND | SRC-004 | https://www.sgdsn.gouv.fr/viginum/publications/matriochka-une-campagne-prorusse-ciblant-les-medias-et-la-communaute-des-fact | VIGINUM Matriochka coordinated seeder quoter accounts media fact checkers June 2024
QRY-009 | WEB | FOUND | - | - | TikTok Romanian elections 4453 inauthentic accounts fake likes followers December 2024
QRY-010 | FETCH | FOUND | SRC-005 | https://newsroom.tiktok.com/continuing-to-protect-the-integrity-of-tiktok-during-romanian-elections?from_seo_redirect=1&lang=en-150 | TikTok Romanian elections 4453 inauthentic accounts fake likes followers December 2024
QRY-011 | WEB | FOUND | - | - | TikTok how counters deceptive behaviour covert influence networks 2024 Romania 70000 accounts
QRY-012 | FETCH | FOUND | SRC-006 | https://newsroom.tiktok.com/how-tiktok-counters-deceptive-behaviour?lang=en-150&trk=article-ssr-frontend-pulse_little-text-block | TikTok how counters deceptive behaviour covert influence networks 2024 Romania 70000 accounts
QRY-013 | WEB | FOUND | - | - | European Commission request information TikTok Romania automated inauthentic exploitation November 2024
QRY-014 | FETCH | FOUND | SRC-007 | https://digital-strategy.ec.europa.eu/en/news/commission-sends-additional-request-information-tiktok-under-digital-services-act | European Commission request information TikTok Romania automated inauthentic exploitation November 2024
QRY-015 | WEB | FOUND | - | - | European Commission formal proceedings TikTok Romanian election coordinated inauthentic manipulation December 2024
QRY-016 | FETCH | FOUND | SRC-008 | https://digital-strategy.ec.europa.eu/en/news/commission-opens-formal-proceedings-against-tiktok-election-risks-under-digital-services-act | European Commission formal proceedings TikTok Romanian election coordinated inauthentic manipulation December 2024
QRY-017 | WEB | FOUND | - | - | Meta EU 2024 elections coordinated inauthentic behavior fake identities 200 adversarial networks since 2017
QRY-018 | FETCH | FOUND | SRC-009 | https://about.fb.com/news/2024/02/how-meta-is-preparing-for-the-eus-2024-parliament-elections/ | Meta EU 2024 elections coordinated inauthentic behavior fake identities 200 adversarial networks since 2017
QRY-019 | WEB | FOUND | - | - | French Senate 2024 foreign influence Portal Kombat bots artificial amplification RRN
QRY-020 | FETCH | FOUND | SRC-010 | https://www.senat.fr/rap/r23-739-1/r23-739-111.html | French Senate 2024 foreign influence Portal Kombat bots artificial amplification RRN
QRY-021 | WEB | FOUND | - | - | 2019 European elections Twitter fake news limited reach organized network disinformation PLOS
QRY-022 | FETCH | FOUND | SRC-011 | https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0234689 | 2019 European elections Twitter fake news limited reach organized network disinformation PLOS
QRY-023 | WEB | FOUND | - | - | Nature social bots low credibility content early amplification 14 million messages 2018
QRY-024 | FETCH | FOUND | SRC-012 | https://www.nature.com/articles/s41467-018-06930-7 | Nature social bots low credibility content early amplification 14 million messages 2018
QRY-025 | WEB | FOUND | - | - | Nature IRA Twitter 2016 exposure 1 percent 70 percent no voting behavior relationship 2023
QRY-026 | FETCH | FOUND | SRC-013 | https://www.nature.com/articles/s41467-022-35576-9 | Nature IRA Twitter 2016 exposure 1 percent 70 percent no voting behavior relationship 2023
QRY-027 | WEB | FOUND | - | - | Nature neutral bots political bias social media 2021 bot exposure low credibility content
QRY-028 | FETCH | FOUND | SRC-014 | https://www.nature.com/articles/s41467-021-25738-6 | Nature neutral bots political bias social media 2021 bot exposure low credibility content
QRY-029 | WEB | FOUND | - | - | 2019 European elections Twitter amplifiers France Germany Italy Greece 2024 study
QRY-030 | FETCH | FOUND | SRC-015 | https://www.mdpi.com/2673-5172/5/3/60 | 2019 European elections Twitter amplifiers France Germany Italy Greece 2024 study

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | VIGINUM-RRN-2023 | VIGINUM — RRN : une campagne numérique de manipulation de l’information complexe et persistante | 2023-06-13 | 2026-09-09 | Synthèse + rapport technique; composantes et comptes inauthentiques | https://www.sgdsn.gouv.fr/viginum/publications/rrn-une-campagne-numerique-de-manipulation-de-linformation-complexe-et
SRC-002 | ◈ | fam:A | VIGINUM-PORTAL-KOMBAT-2-2024 | VIGINUM — Portal Kombat : suite des investigations sur le réseau structuré et coordonné | 2024-02-14 | 2026-09-09 | Réseau 193 portails; automatisation; rôle TigerWeb | https://www.sgdsn.gouv.fr/viginum/publications/portal-kombat-suite-des-investigations-sur-le-reseau-structure-et-coordonne-de
SRC-003 | ◈ | fam:A | VIGINUM-PORTAL-KOMBAT-3-2024 | VIGINUM — Portal Kombat : extension du réseau de propagande russe | 2024-04-29 | 2026-09-09 | Extension 224 portails; ciblage UE avant élections | https://www.sgdsn.gouv.fr/viginum/publications/portal-kombat-extension-du-reseau-de-propagande-russe
SRC-004 | ◈ | fam:A | VIGINUM-MATRIOCHKA-2024 | VIGINUM — Matriochka : campagne prorusse ciblant médias et fact-checkers | 2024-06-10 | 2026-09-09 | Mode opératoire seeders/quoters; plus de 60 pays | https://www.sgdsn.gouv.fr/viginum/publications/matriochka-une-campagne-prorusse-ciblant-les-medias-et-la-communaute-des-fact
SRC-005 | ◉ | fam:B | TIKTOK-ROMANIA-ELECTIONS-2024 | TikTok — Continuing to protect the integrity of TikTok during Romanian elections | 2024-12-07 | 2026-09-09 | Updates Dec 2024-Jan 2025; inauthentic network and fake engagement | https://newsroom.tiktok.com/continuing-to-protect-the-integrity-of-tiktok-during-romanian-elections?from_seo_redirect=1&lang=en-150
SRC-006 | ◉ | fam:B | TIKTOK-DECEPTIVE-BEHAVIOUR-2024 | TikTok — How TikTok counters deceptive behaviour | 2024-12-09 | 2026-09-09 | Covert influence definitions; 40 networks and 70k accounts | https://newsroom.tiktok.com/how-tiktok-counters-deceptive-behaviour?lang=en-150&trk=article-ssr-frontend-pulse_little-text-block
SRC-007 | ◈ | fam:A | EC-TIKTOK-RFI-2024-11-29 | European Commission — Additional request for information to TikTok under DSA | 2024-11-29 | 2026-09-09 | Romanian elections; inauthentic or automated exploitation and recommender risks | https://digital-strategy.ec.europa.eu/en/news/commission-sends-additional-request-information-tiktok-under-digital-services-act
SRC-008 | ◈ | fam:A | EC-TIKTOK-PROCEEDINGS-2024-12-17 | European Commission — Formal proceedings against TikTok on election risks | 2024-12-17 | 2026-09-09 | Suspected DSA breach; coordinated inauthentic manipulation and automated exploitation | https://digital-strategy.ec.europa.eu/en/news/commission-opens-formal-proceedings-against-tiktok-election-risks-under-digital-services-act
SRC-009 | ◉ | fam:B | META-EU-ELECTIONS-2024 | Meta — How Meta Is Preparing for the EU’s 2024 Parliament Elections | 2024-02-25 | 2026-09-09 | Influence operations and CIB definition; >200 networks | https://about.fb.com/news/2024/02/how-meta-is-preparing-for-the-eus-2024-parliament-elections/
SRC-010 | ◈ | fam:C | SENAT-R23-739-1-PORTAL-KOMBAT | Sénat — Lutte contre les influences étrangères malveillantes : Portal Kombat | 2024-07-25 | 2026-09-09 | Portal Kombat; bot amplification and links to RRN/Doppelganger | https://www.senat.fr/rap/r23-739-1/r23-739-111.html
SRC-011 | ◉ | fam:D | PLOS-EU-ELECTIONS-2020-E0234689 | PLOS One — The limited reach of fake news on Twitter during 2019 European elections | 2020-06-18 | 2026-09-09 | Abstract/results; ~400k tweets, 863 accounts; no organized network found | https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0234689
SRC-012 | ◉ | fam:D | NATCOMMS-2018-4787 | Nature Communications — The spread of low-credibility content by social bots | 2018-11-20 | 2026-09-09 | Abstract/results; 14m messages; early amplification and human reshares | https://www.nature.com/articles/s41467-018-06930-7
SRC-013 | ◉ | fam:D | NATCOMMS-2023-62 | Nature Communications — Exposure to the Russian Internet Research Agency foreign influence campaign | 2023-01-09 | 2026-09-09 | Abstract/results; concentrated exposure and no meaningful attitude/vote relationship | https://www.nature.com/articles/s41467-022-35576-9
SRC-014 | ◉ | fam:D | NATCOMMS-2021-5580 | Nature Communications — Neutral bots probe political bias on social media | 2021-09-22 | 2026-09-09 | Experiment; early connections, bot-like exposure, no strong feed-bias evidence | https://www.nature.com/articles/s41467-021-25738-6
SRC-015 | ◉ | fam:E | JOURNALMEDIA-2024-5-3-60 | Journalism and Media — The Usage of Twitter (Now X) Amplifiers in the European Elections of 2019 | 2024-07-12 | 2026-09-09 | Dataset 88 political accounts, 44,651 retweeters, 237,813 tweets; amplifier analysis | https://www.mdpi.com/2673-5172/5/3/60

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.sgdsn.gouv.fr/viginum/publications/rrn-une-campagne-numerique-de-manipulation-de-linformation-complexe-et | A | 2023-06-13 | RRN campaign scope | VIGINUM identified the RRN/Doppelganger manipulation campaign as targeting several European states including France from September 2022, using pro-Russian content and impersonation infrastructure. | -
FCT-002 | FACT | ✧ | https://www.sgdsn.gouv.fr/viginum/publications/rrn-une-campagne-numerique-de-manipulation-de-linformation-complexe-et | A | 2023-06-13 | RRN inauthentic account layer | VIGINUM documented social-media amplification through inauthentic accounts, including around 200 single-use Facebook accounts in the detailed RRN reporting, with sponsored links to campaign content. | -
FCT-003 | FACT | ✧ | https://www.sgdsn.gouv.fr/viginum/publications/portal-kombat-suite-des-investigations-sur-le-reseau-structure-et-coordonne-de | A | 2024-02-14 | Portal Kombat automation | VIGINUM documented a network of 193 portals that largely republished Russian or pro-Russian sources and used massive automation and search-engine optimization to expand distribution. | -
FCT-004 | FACT | ✧ | https://www.sgdsn.gouv.fr/viginum/publications/portal-kombat-suite-des-investigations-sur-le-reseau-structure-et-coordonne-de | A | 2024-02-14 | Portal Kombat service provider | VIGINUM identified the Crimea-based company TigerWeb as playing a major role in creating and administering Portal Kombat sites while stating that the identity of the ultimate operator/client was not established at that stage. | -
FCT-005 | FACT | ✧ | https://www.sgdsn.gouv.fr/viginum/publications/portal-kombat-extension-du-reseau-de-propagande-russe | A | 2024-04-29 | Portal Kombat expansion before EU elections | VIGINUM expanded the Portal Kombat inventory to 224 portals, including domains targeting 19 EU member states, shortly before the June 2024 European Parliament elections. | -
FCT-006 | EVIDENCE | ✧ | https://www.sgdsn.gouv.fr/viginum/publications/portal-kombat-extension-du-reseau-de-propagande-russe | A | 2024-04-29 | Portal count is not electoral effect | The geographic and infrastructure expansion establishes targeting capacity and scale but does not by itself measure incremental audience exposure, persuasion, turnout, vote choice or seat outcomes. | -
FCT-007 | FACT | ✧ | https://www.sgdsn.gouv.fr/viginum/publications/matriochka-une-campagne-prorusse-ciblant-les-medias-et-la-communaute-des-fact | A | 2024-06-10 | Matriochka coordinated diffusion | VIGINUM documented Matriochka as a coordinated two-stage diffusion system in which seeder accounts posted fabricated media-like content and quoter accounts injected it into replies to media, public figures and fact-checkers across more than sixty countries. | -
FCT-008 | EVIDENCE | ✧ | https://www.sgdsn.gouv.fr/viginum/publications/matriochka-une-campagne-prorusse-ciblant-les-medias-et-la-communaute-des-fact | A | 2024-06-10 | Matriochka attribution ceiling | Russian-speaking Telegram channels and coordinated account behavior support an operational linkage, but the public report does not by itself close an authenticated state-command or electoral-effect chain. | -
FCT-009 | FACT | ✧ | https://newsroom.tiktok.com/continuing-to-protect-the-integrity-of-tiktok-during-romanian-elections?from_seo_redirect=1&lang=en-150 | B | 2024-12-17 | Romania 4453-account network | TikTok reported a network of 4,453 inauthentic accounts targeting Romanian audiences that attempted to promote the AUR party and, to a lesser extent, independent candidate Calin Georgescu. | -
FCT-010 | EVIDENCE | ✧ | https://newsroom.tiktok.com/continuing-to-protect-the-integrity-of-tiktok-during-romanian-elections?from_seo_redirect=1&lang=en-150 | B | 2024-12-07 | Romania fake-engagement counters | TikTok reported preventing tens of millions of fake likes and follow requests and blocking hundreds of thousands of spam-account creations in Romania; these are platform enforcement counters, not measured human exposure or persuasion. | -
FCT-011 | FACT | ✧ | https://newsroom.tiktok.com/how-tiktok-counters-deceptive-behaviour?lang=en-150&trk=article-ssr-frontend-pulse_little-text-block | B | 2024-12-09 | TikTok covert influence enforcement 2024 | TikTok reported disrupting more than 40 covert influence networks in 2024, including three in Romania, and removing more than 70,000 accounts under its covert-influence policies. | -
FCT-012 | EVIDENCE | ✧ | https://newsroom.tiktok.com/how-tiktok-counters-deceptive-behaviour?lang=en-150&trk=article-ssr-frontend-pulse_little-text-block | B | 2024-12-09 | Platform CIB definition is not independent attribution | TikTok detects covert influence through coordination, deceptive identity/location or technical linkages and attempted manipulation; this platform classification is operational evidence but not independent proof of a client, state tasking or electoral effect. | -
FCT-013 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/news/commission-sends-additional-request-information-tiktok-under-digital-services-act | A | 2024-11-29 | Commission Romania automated-exploitation inquiry | During the Romanian elections, the European Commission requested TikTok information on risks from inauthentic or automated exploitation of the service and from recommender systems. | -
FCT-014 | EVIDENCE | ✧ | https://digital-strategy.ec.europa.eu/en/news/commission-sends-additional-request-information-tiktok-under-digital-services-act | A | 2024-11-29 | RFI is investigatory | A Commission request for information establishes regulatory scrutiny and specified risk hypotheses; it is not a final finding that manipulation occurred or changed an election. | -
FCT-015 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/news/commission-opens-formal-proceedings-against-tiktok-election-risks-under-digital-services-act | A | 2024-12-17 | Commission TikTok election-risk proceedings | The Commission opened formal DSA proceedings focused in part on risks from coordinated inauthentic manipulation or automated exploitation of TikTok in the Romanian presidential-election context. | -
FCT-016 | EVIDENCE | ✧ | https://digital-strategy.ec.europa.eu/en/news/commission-opens-formal-proceedings-against-tiktok-election-risks-under-digital-services-act | A | 2024-12-17 | Proceeding is not adjudication or attribution | The formal proceeding concerns suspected compliance failures and systemic risks; it does not itself adjudicate a DSA violation, identify the ultimate operator of every network, or prove a causal electoral outcome. | -
FCT-017 | FACT | ✧ | https://about.fb.com/news/2024/02/how-meta-is-preparing-for-the-eus-2024-parliament-elections/ | B | 2024-02-25 | Meta CIB operational definition | Meta defines covert influence operations as coordinated efforts to manipulate public debate that can rely on fake identities, which it classifies as coordinated inauthentic behaviour. | -
FCT-018 | FACT | ✧ | https://about.fb.com/news/2024/02/how-meta-is-preparing-for-the-eus-2024-parliament-elections/ | B | 2024-02-25 | Meta network takedown volume | Meta reported investigating and taking down more than 200 adversarial coordinated-inauthentic-behaviour networks since 2017. | -
FCT-019 | FACT | ✧ | https://www.senat.fr/rap/r23-739-1/r23-739-111.html | A,C | 2024-07-25 | Portal Kombat bot amplification corroboration | The French Senate reported that Portal Kombat distribution was massively amplified by bots and that part of this artificial amplification used accounts linked to RRN/Doppelganger. | -
FCT-020 | EVIDENCE | ✧ | https://www.senat.fr/rap/r23-739-1/r23-739-111.html | C | 2024-07-25 | Senate amplification assessment has no vote denominator | The parliamentary assessment supports the existence of bot amplification but does not supply a counterfactual denominator for incremental voter exposure, persuasion or electoral result change. | -
FCT-021 | FACT | ✧ | https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0234689 | D | 2020-06-18 | EU 2019 limited fake-news reach | A PLOS One study of nearly 400,000 tweets from 863 selected accounts around the 2019 European elections found disinformation outlets peripheral and found no evidence in its dataset of an organized network of accounts aimed at spreading disinformation. | -
FCT-022 | EVIDENCE | ✧ | https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0234689 | D | 2020-06-18 | EU 2019 negative control | The 2019 European-election study provides a negative control: the presence of disinformation sources and automation concerns does not imply that an organized amplification network is detectable or influential in every election dataset. | -
FCT-023 | FACT | ✧ | https://www.nature.com/articles/s41467-018-06930-7 | D | 2018-11-20 | Social bots early low-credibility amplification | A Nature Communications analysis of roughly 14 million Twitter messages found social bots played a disproportionate role in early diffusion of low-credibility content and targeted influential users through replies and mentions. | -
FCT-024 | FACT | ✧ | https://www.nature.com/articles/s41467-018-06930-7 | D | 2018-11-20 | Humans reshare bot-seeded low-credibility content | The same study found human users reshared low-credibility content posted by bots, closing a bot-to-human retransmission edge while not measuring electoral vote change. | -
FCT-025 | FACT | ✧ | https://www.nature.com/articles/s41467-022-35576-9 | D | 2023-01-09 | IRA exposure concentration | The Nature Communications linked-survey study found exposure to IRA accounts highly concentrated: one percent of users accounted for about seventy percent of exposures, and domestic media/politicians dwarfed IRA exposure. | -
FCT-026 | FACT | ✧ | https://www.nature.com/articles/s41467-022-35576-9 | D | 2023-01-09 | IRA no meaningful attitude or voting relationship | Across measured outcomes, the study found no evidence of a meaningful relationship between IRA exposure and changes in attitudes, polarization or voting behavior in the 2016 election. | -
FCT-027 | FACT | ✧ | https://www.nature.com/articles/s41467-021-25738-6 | D | 2021-09-22 | Neutral-bot exposure depends on initial network | A controlled social-bot experiment found that early follow choices strongly shaped later political information exposure, network structure and exposure to bot-like or low-credibility accounts. | -
FCT-028 | EVIDENCE | ✧ | https://www.nature.com/articles/s41467-021-25738-6 | D | 2021-09-22 | Neutral-bot study does not establish platform partisan command | The neutral-bot experiment found no strong or consistent evidence of political bias in the Twitter news feed and could not measure real-world political actions, separating ecosystem effects from intentional platform or operator tasking. | -
FCT-029 | FACT | ✧ | https://www.mdpi.com/2673-5172/5/3/60 | E | 2024-07-12 | EU 2019 amplifier prevalence across parties | A 2024 study of the 2019 European elections analyzed 88 party leaders/MEP candidates, 44,651 retweeter accounts and 237,813 election-related tweets, concluding that amplifiers were used across political parties and sometimes shared across countries. | -
FCT-030 | EVIDENCE | ✧ | https://www.mdpi.com/2673-5172/5/3/60 | E | 2024-07-12 | Amplifier label is not tasking or vote effect | Network-level classification as an amplifier or highly active retweeter does not by itself establish automation, deceptive identity, common command, client tasking, persuasion or a changed vote. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-002
FCT-004 | SRC-002
FCT-005 | SRC-003
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
FCT-019 | SRC-002,SRC-010
FCT-020 | SRC-010
FCT-021 | SRC-011
FCT-022 | SRC-011
FCT-023 | SRC-012
FCT-024 | SRC-012
FCT-025 | SRC-013
FCT-026 | SRC-013
FCT-027 | SRC-014
FCT-028 | SRC-014
FCT-029 | SRC-015
FCT-030 | SRC-015

## REFUTATION_REGISTRY_V1

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | SKIP:NOT_ELIGIBLE
FCT-007 | ELIGIBLE:VERIFIE
FCT-008 | SKIP:NOT_ELIGIBLE
FCT-009 | ELIGIBLE:VERIFIE
FCT-010 | SKIP:NOT_ELIGIBLE
FCT-011 | ELIGIBLE:VERIFIE
FCT-012 | SKIP:NOT_ELIGIBLE
FCT-013 | ELIGIBLE:VERIFIE
FCT-014 | SKIP:NOT_ELIGIBLE
FCT-015 | ELIGIBLE:VERIFIE
FCT-016 | SKIP:NOT_ELIGIBLE
FCT-017 | ELIGIBLE:VERIFIE
FCT-018 | ELIGIBLE:VERIFIE
FCT-019 | ELIGIBLE:VERIFIE
FCT-020 | SKIP:NOT_ELIGIBLE
FCT-021 | ELIGIBLE:VERIFIE
FCT-022 | SKIP:NOT_ELIGIBLE
FCT-023 | ELIGIBLE:VERIFIE
FCT-024 | ELIGIBLE:VERIFIE
FCT-025 | ELIGIBLE:VERIFIE
FCT-026 | ELIGIBLE:VERIFIE
FCT-027 | ELIGIBLE:VERIFIE
FCT-028 | SKIP:NOT_ELIGIBLE
FCT-029 | ELIGIBLE:VERIFIE
FCT-030 | SKIP:NOT_ELIGIBLE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-007 | WRITE | -
FCT-009 | WRITE | -
FCT-011 | WRITE | -
FCT-013 | WRITE | -
FCT-015 | WRITE | -
FCT-017 | WRITE | -
FCT-018 | WRITE | -
FCT-019 | WRITE | -
FCT-021 | WRITE | -
FCT-023 | WRITE | -
FCT-024 | WRITE | -
FCT-025 | WRITE | -
FCT-026 | WRITE | -
FCT-027 | WRITE | -
FCT-029 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:CAUSAL
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:FINALIZE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-09T02:36:46.260298+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-029","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":20,"eligible":20,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:20;attempted:0;success:0;failure:0;blocked:20} | WRITEBACK_EXECUTION_V1:[20 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-002 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-003 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-004 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-005 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-007 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-009 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-011 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-013 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-015 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-017 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-018 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-019 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-021 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-023 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-024 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-025 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-026 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-027 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-029 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
