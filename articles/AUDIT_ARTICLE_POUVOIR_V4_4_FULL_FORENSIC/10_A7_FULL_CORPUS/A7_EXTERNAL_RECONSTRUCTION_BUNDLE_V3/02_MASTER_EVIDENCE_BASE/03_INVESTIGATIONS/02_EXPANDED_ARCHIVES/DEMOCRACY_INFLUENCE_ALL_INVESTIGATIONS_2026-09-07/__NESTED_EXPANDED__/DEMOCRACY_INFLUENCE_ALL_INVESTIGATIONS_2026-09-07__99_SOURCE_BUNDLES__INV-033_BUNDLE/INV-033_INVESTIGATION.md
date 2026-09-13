ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260907-0711-emirats-influence-europe | PARENT_RUN_ID:NONE | AS_OF:2026-09-07
INPUT_KIND:RUN_CARD | MISSION_MODE:DEEPEN | INPUT_REF:PATH:/mnt/data/inv033-work/te/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-07_emirats-influence-europe/2026-09-07_07-11_emirats-influence-europe_INPUT.md | SUBJECT_SLUG:emirats-influence-europe | SUBJECT_FP:sha256:1d740cc267bab5f6d96c8a63ba61b1981ea2c2e7f45d3a69ca08522a8df1723b | INPUT_SHA256:sha256:c01967887a2e9736751781f80a0b40ca7f612669e5453fb0f68c4277d7a9171b
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/UE 2017-2026; UAE state/public entities, Emirati private clients, lobbying/PR, Alp Services/private intelligence, covert reputation operations, surveillance and comparable mechanisms; preserve client/state/tasking/effect boundaries.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/NETWORK.md,clusters/FRAMING.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-033 — Émirats arabes unis : influence clandestine et réputationnelle en Europe

## Question et règle de preuve

L'enquête teste un objet précis : quels mécanismes attribuables aux Émirats arabes unis ou à des commanditaires émiratis peuvent être documentés en France et en Europe, et jusqu'où la chaîne `commanditaire → prestataire → action → cible → exposition → effet` peut-elle être fermée sans convertir nationalité, proximité, financement ou accès en preuve de tasking étatique.

Le corpus est traité avec les séparations suivantes : `acteur émirati privé != État des EAU`, `financement != commandement`, `relation client != tasking étatique`, `cible listée != affiliation vraie`, `paiement d'un intermédiaire != connaissance du commanditaire final`, `opération existe != résultat changé`, `enquête judiciaire != culpabilité`, `classement procédural != exonération au fond`.

## 1. Chaîne client → Alp Services

Le résultat le plus robuste du run concerne le noyau Alp Services. Des documents internes rapportés par Mediapart/EIC décrivent un contact lié au renseignement d'Abou Dhabi utilisant Alp pendant plusieurs années, des commissions et contrats de montant substantiel, ainsi que des objectifs opérationnels visant des réseaux, lobbyistes, journalistes ou acteurs perçus comme favorables au Qatar. Les mêmes ensembles documentaires décrivent des propositions de contre-lobbying, de collecte d'informations compromettantes, de préparation de dossiers contentieux et d'actions réputationnelles. [FCT-001, FCT-002, FCT-003, FCT-009, FCT-013]

Ce faisceau permet de monter plus haut que dans de nombreux dossiers d'influence étrangère : l'identité du client, la relation avec le prestataire, les ressources et des objectifs opérationnels sont documentés. Pour le noyau client-Alp, I0 à I3 sont donc fortement soutenus. Cette conclusion ne vaut pas automatiquement pour tout acteur émirati, tout intermédiaire ou toute opération attribuée dans le corpus.

La qualification reste probatoire : l'attribution repose largement sur des documents internes divulgués et des investigations journalistiques croisées. Une enquête fédérale suisse a ensuite été ouverte sur des soupçons d'activités pour les EAU. Cette ouverture corrobore la matérialité judiciaire du dossier mais ne constitue pas une condamnation ni un jugement au fond de l'ensemble des allégations. [FCT-017]

## 2. Profilage européen et opérations réputationnelles

Le corpus documente une opération de grande échelle : plus d'un millier de personnes et plusieurs centaines d'organisations en Europe ont été recensées dans les données examinées par les journalistes, dont un volume important en France. Le mandat ne se limitait pas à cartographier : des documents décrivent également des stratégies de discrédit ou d'influence contre certaines cibles. [FCT-004, FCT-005]

Cette ampleur ne permet toutefois pas de traiter les assertions contenues dans les listes comme vraies. Le cas Zakia Khattabi fournit un contrôle direct : la ministre belge a réfuté publiquement plusieurs éléments factuels précis utilisés pour la caractériser, notamment des affiliations et caractéristiques religieuses erronées. Le bon objet probatoire est donc double : **le profilage et sa finalité sont documentés ; la véracité de chaque fiche ne l'est pas**. [FCT-010]

Même limite sur l'exécution : Operation Constellation documente une volonté de détecter, contrer et attaquer des réseaux attribués au Qatar dans l'environnement institutionnel européen, mais le reportage rapporte également des résultats maigres et des revendications de capacité ou d'accès politique exagérées. Un prestataire peut avoir un contrat réel, des moyens réels et néanmoins survendre sa performance. [FCT-006, FCT-007]

## 3. Intermédiaires, journalistes et connaissance du client

Des journalistes ou autres intermédiaires apparaissent dans des registres internes comme contributeurs, chercheurs ou sous-traitants rémunérés. Cette donnée peut établir une relation transactionnelle. Elle ne suffit pas à établir que chaque intermédiaire connaissait le commanditaire ultime, partageait l'objectif étatique ou agissait comme agent conscient des EAU. [FCT-008]

La chaîne correcte est donc : `paiement/mission documenté → rôle intermédiaire documenté`, puis un second test indépendant pour `connaissance du client final → instruction → coordination`. Aucun saut n'est autorisé entre ces niveaux.

## 4. Autriche et Operation Luxor : contrôle causal négatif

Le cas autrichien est particulièrement discriminant parce qu'il peut facilement être surinterprété. Profil documente un contrat avec Lorenzo Vidino pour fournir à Alp des informations, indications ou rumeurs sur des personnes et organisations liées au thème des Frères musulmans. Certaines personnes ou organisations étudiées apparaissent ensuite dans l'environnement d'Operation Luxor. [FCT-014]

Mais le même corpus fournit le contre-contrôle : Profil indique ne pas avoir trouvé de preuve définitive qu'un document précis de l'EICTP avait été transmis aux EAU, et les acteurs concernés contestent l'instrumentalisation. Surtout, le dossier autrichien comporte également des informations provenant d'autres services arabes. [FCT-015, FCT-016]

La conclusion admissible est donc une **voie d'information potentiellement contaminante et un chevauchement documenté**, pas la proposition plus forte `EAU → Alp/Vidino → police autrichienne → Operation Luxor`. Le dernier lien causal reste non établi.

## 5. Réactions institutionnelles et effets

Après les révélations, la Belgique a convoqué l'ambassadeur des EAU et demandé des explications. L'Union européenne a indiqué avoir pris note des révélations et suivre la question avec les États membres. Ces éléments établissent un effet institutionnel de la révélation du dossier, pas un effet politique causal de l'opération clandestine elle-même. [FCT-011, FCT-012]

Le cas Hazim Nada/Lord Energy documente une séquence beaucoup plus lourde au niveau individuel et économique : campagne réputationnelle, difficultés bancaires et effondrement de l'activité apparaissent dans la chronologie. Mais cette chronologie ne permet pas d'isoler la contribution contrefactuelle de chaque action d'influence par rapport aux décisions autonomes des banques, partenaires, autorités ou autres causes possibles. [FCT-021, FCT-022]

Ainsi I6 est **partiel** : des réactions diplomatiques et des conséquences économiques sont observables dans certains cas. I7 reste **non établi** : aucun design causal ne permet de dire ce qui se serait produit sans l'opération, ni de démontrer un changement électoral ou politique final imputable à elle seule.

## 6. Statut judiciaire : ni blanchiment ni condamnation globale

Le volet judiciaire impose une chronologie stricte. La Suisse a ouvert une enquête fédérale sur des soupçons d'espionnage politique ou d'actes pour un État étranger. [FCT-017]

En France, une enquête préliminaire a été classée sans poursuites en 2024 dans un contexte où les enquêteurs n'avaient pas obtenu certains éléments ou auditions et où le dossier avait été transmis aux autorités suisses. Le classement rapporté est procédural et probatoire ; il n'établit pas que les opérations alléguées n'ont pas existé. [FCT-018, FCT-019]

En 2025, une information judiciaire distincte a été ouverte à la suite de la plainte de Sihem Souid pour plusieurs faits allégués touchant notamment le domicile, la vie privée et les correspondances. Cette procédure est elle aussi non terminale. [FCT-020]

Le statut global est donc : **dossier juridiquement actif/non terminal dans certaines branches, sans jugement définitif disponible dans le corpus fermant la responsabilité pénale de l'ensemble de la chaîne**.

## 7. Évaluation I0 → I7

- **I0 identité/relation : STRONG** pour le noyau client lié au renseignement émirati et Alp ; variable pour les intermédiaires.
- **I1 ressources/capacité : VERIFIED** pour contrats, commissions, paiements et capacités proposées/documentées.
- **I2 action documentée : VERIFIED/PARTIAL** : profilage, contre-lobbying et opérations réputationnelles sont documentés comme familles ; toutes les propositions ne sont pas prouvées comme exécutées.
- **I3 coordination/tasking : STRONG pour le noyau client-Alp**, mais non transférable à chaque journaliste, chercheur, cible ou institution downstream.
- **I4 exposition/reach : PARTIAL**, très dépendant des sous-opérations.
- **I5 réception/persuasion : NOT_ESTABLISHED systématiquement**.
- **I6 changement comportemental/institutionnel/économique : PARTIAL** pour certains effets ou réactions observables.
- **I7 résultat contrefactuel : NOT_ESTABLISHED**.

## 8. Contrôle de symétrie pour INV-146

INV-033 apporte un cas matériel à la future synthèse alliés/adversaires. Les EAU sont un partenaire proche de plusieurs États européens ; pourtant le corpus soutient, pour un noyau d'opérations, une chaîne de covert influence-for-hire allant beaucoup plus loin que la simple diplomatie, le lobbying déclaré ou le financement d'acteurs autonomes : client lié au renseignement, ressources, prestataire, objectifs et opérations sont documentés.

Cette propriété rend le cas comparable à des opérations attribuées à des puissances adversaires, **à condition de comparer des mécanismes isomorphes**. Le cas ne permet pas encore de conclure que les autorités ou médias utilisent effectivement des standards asymétriques : ce test appartient à INV-146. Il fournit seulement le contrôle nécessaire pour le faire.

## 9. Verdict et gaps

**Verdict technique :** l'existence d'un dispositif UAE-linked de renseignement privé et d'influence réputationnelle en Europe est fortement documentée pour le noyau Alp Services. La chaîne client → paiement/tasking → prestataire → opérations/cibles atteint I3 avec un niveau de support élevé. Elle ne doit pas être étendue par association à tous les acteurs émiratis, journalistes, chercheurs ou institutions cités.

Trois plafonds restent matériels :

1. **RESPONSIBILITY / JUDICIAL FINALITY** — absence de jugement définitif fermant toutes les responsabilités alléguées.
2. **EDGE SPECIFICITY** — connaissance/tasking des intermédiaires et exécution de chaque opération restent cas par cas ; le cas autrichien ne ferme pas la causalité UAE → Luxor.
3. **CAUSALITY** — I5-I7 ne sont pas fermés ; aucun résultat électoral/politique contrefactuel n'est démontré.

Ces gaps ne sont pas réparables par une recherche générique supplémentaire. Ils nécessitent de futurs actes judiciaires, des documents authentifiés supplémentaires ou des designs causaux identifiés. La collecte large est donc gelée.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:4|SRC_COMPLETE:13/13

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **anchor_events:**
  - 2017: reported client relationship begins
  - 2018: commissions/contracts documented
  - 2023: Abu Dhabi Secrets publications and diplomatic reaction
  - 2023-2025: Swiss/French legal proceedings
- **as_of:** 2026-09-07
- **rules:**
  - event date != publication date != investigation date
  - investigative attribution != judicial finding
- **window:** 2017-2026

### MANIPULATION_REPORT
- **assumptions:**
  - private actors independent unless relation evidence says otherwise
  - specific erroneous target data can invalidate target-level claims without erasing operation existence
  - commercial capability statements require execution controls
- **clusters:**
  - **loaded:**
    - clusters/POWER.md
    - clusters/NETWORK.md
    - clusters/FRAMING.md
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - state relation is case-specific
  - intermediary knowledge cannot be inferred from payment
  - institutional reaction is not counterfactual policy effect
- **input_kind:** TOPIC
- **mission_mode:** INVESTIGATION
- **patterns:**
  - private intelligence for hire
  - covert reputation operation
  - target mapping
  - counter-lobbying
  - paid intermediaries
  - institutional contamination pathway
- **priorities:**
  - client/state attribution
  - payment/tasking
  - executed operations
  - negative controls
  - effect ceilings
- **query_guidance:** trace client -> state relation -> payment -> tasking -> operation -> target/intermediary -> exposure -> reception -> effect -> counterfactual
- **rhetorical:**
  - **AUTH:** authority statements bounded to their evidentiary role
  - **BF:** N/A
  - **DEM:** N/A
  - **FAC:** avoid actor-to-network generalization
  - **NUM:** counts do not establish truth or causal effect
- **speaker:**
  - **goal:** forensic classification of UAE-linked influence mechanisms
  - **target:** France/EU client-tasking-action-effect chains
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **Κ:** 3
  - **Λ:** 5
  - **Ξ:** 4
  - **Σ:** 4
  - **Φ:** 3
  - **Ψ:** 3
  - **Ω:** 4
  - **κ:** 3
  - **ρ:** 5
  - **€:** 4
  - **↕:** 6
  - **⏰:** 4
  - **⚔:** 3
  - **⫸:** 5
  - **🌐:** 6
- **threats:**
  - Emirati actor=state
  - target list=fact
  - payment=knowing agency
  - operation=effect
  - investigation=guilt

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - judicial finality
  - **input_ids:**
    - FCT-001
    - FCT-002
    - FCT-009
    - FCT-013
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no final merits judgment
  - **not_computable:**
    - full hidden client universe
  - **operations_applied:**
    - typed client/state relation
    - separated payment from final liability
  - **reason:** separate state/intelligence client resources from private actors and downstream institutions
  - **result_ids:**
    - CLM-001
    - CTRL-001
  - **status:** DONE
  - **trigger:** ↕
- **item 2:**
  - **gaps:**
    - intermediary knowledge
    - downstream causal edges
  - **input_ids:**
    - FCT-004
    - FCT-006
    - FCT-008
    - FCT-014
    - FCT-016
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no basis to treat every target allegation as true
    - no UAE causation of Luxor established
  - **not_computable:**
    - unobserved operations
  - **operations_applied:**
    - typed target and intermediary edges
    - retained missing knowledge/tasking links
  - **reason:** map client -> provider -> intermediary -> target edges without association fallacies
  - **result_ids:**
    - CLM-002
    - CLM-003
    - CLM-004
    - CTRL-003
    - CTRL-004
    - CTRL-005
  - **status:** DONE
  - **trigger:** 🌐
- **item 3:**
  - **gaps:**
    - effect attribution
  - **input_ids:**
    - FCT-007
    - FCT-010
    - FCT-018
    - FCT-019
  - **module:** clusters/FRAMING.md
  - **negative_results:**
    - no general UAE control claim beyond documented client edges
  - **not_computable:**
    - normative legitimacy
  - **operations_applied:**
    - retained rebuttals and procedural limits
    - separated operation from effect
  - **reason:** prevent covert-operation evidence from becoming nationality-based or totalizing labels
  - **result_ids:**
    - CTRL-002
    - CTRL-003
    - CTRL-006
    - CTRL-007
  - **status:** DONE
  - **trigger:** Λ

### SCOPING_REPORT
- **classification_dimensions:**
  - origin
  - visibility
  - client identity
  - state relation
  - payment
  - tasking
  - action
  - target
  - exposure
  - effect
- **exclusions:**
  - Emirati actor=UAE state
  - funding=command
  - client relation=state tasking
  - target list=truth
  - operation=result changed
- **scope:** France/UE 2017-2026; distinguish UAE state/intelligence, Emirati private clients, providers, intermediaries and targets.
- **status:** ACTIVE

### CREDO
- Emirati/private actor != UAE state
- funding != command
- client relationship != state tasking
- target list != factual affiliation
- paid intermediary != knowing state agent
- operation exists != result changed
- investigation != guilt
- procedural closure != exoneration

### COGNITIVE_MAP
- **causal_boundary:** I0-I3 strong for the core Alp/UAE client chain; I4-I6 heterogeneous; I7 not established.
- **core_model:** Strong reported UAE-intelligence/client -> Alp Services payment/tasking chain for covert reputation and influence operations; execution, intermediary knowledge and effect remain operation-specific.
- **relation_chain:**
  - client identity
  - state relation
  - payment
  - tasking
  - operation
  - target/intermediary
  - exposure
  - reception
  - effect
  - counterfactual
- **rival_models:**
  - state-directed covert influence-for-hire
  - private commercial work without state tasking
  - mixed ecosystem
  - inflated vendor claims with limited effect

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** The core client-Alp edge is strong, but target accuracy, intermediary knowledge, execution and downstream causality vary materially.
  - **resolution:** Keep UAE client/tasking finding for the core operation; classify every downstream edge separately.
  - **thesis:** Abu Dhabi Secrets proves a unified UAE-controlled European influence network with demonstrated effects.
- **item 2:**
  - **antithesis:** Reported closure grounds were evidentiary/procedural and Swiss/later French proceedings continued on related allegations.
  - **resolution:** Closure != exoneration; investigation != guilt.
  - **thesis:** A French procedural closure disproves the allegations.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **from:** UAE intelligence-linked client
  - **limits:**
    - commercial record != final criminal finding
  - **resource:** commissions/contracts/payments
  - **support:**
    - FCT-002
    - FCT-013
  - **to:** covert influence/reputation work
  - **via:** Alp Services
- **item 2:**
  - **from:** Alp Services
  - **limits:**
    - proposal != execution; execution != effect
  - **resource:** profiling, compromising information, counter-lobbying and reputation capability
  - **support:**
    - FCT-003
    - FCT-005
    - FCT-006
    - FCT-008
  - **to:** European political/media/reputation environment
  - **via:** staff and intermediaries

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** UAE intelligence-linked client
  - **limits:**
    - reported internal records; final judicial liability unresolved
  - **relation:** reported client/tasking/payment chain
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-009
    - FCT-013
  - **to:** Alp Services
- **item 2:**
  - **from:** Alp Services
  - **limits:**
    - execution/effect varies; some capability overclaim
  - **relation:** profiling/reputation/counter-lobbying operations
  - **support:**
    - FCT-003
    - FCT-004
    - FCT-005
    - FCT-006
  - **to:** European targets including France
- **item 3:**
  - **from:** Alp Services
  - **limits:**
    - ultimate-client knowledge and tasking case-specific
  - **relation:** research/payment/subcontracting records
  - **support:**
    - FCT-008
    - FCT-014
  - **to:** journalists/research intermediaries
- **item 4:**
  - **from:** Alp-linked information ecosystem
  - **limits:**
    - UAE causal edge to Operation Luxor not established
  - **relation:** possible information pathway
  - **support:**
    - FCT-014
    - FCT-016
  - **to:** Austrian institutional environment

### IMPACT_MAP
- **I0_identity_relation:** STRONG for core Alp/UAE client chain; case-specific elsewhere
- **I1_resources_capability:** VERIFIED for payments/contracts and Alp capabilities
- **I2_documented_action:** VERIFIED for profiling/reputation/counter-lobbying families, not every proposal
- **I3_coordination_tasking:** STRONG for core client-Alp edge; not transferable to every intermediary
- **I4_exposure_reach:** PARTIAL and case-specific
- **I5_reception_persuasion:** NOT_ESTABLISHED systematically
- **I6_behavior_institutional_economic_change:** PARTIAL for Belgian diplomatic response and selected economic sequence
- **I7_counterfactual_outcome:** NOT_ESTABLISHED
- **downstream:** Feeds INV-146 as allied-state covert influence-for-hire symmetry control.

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** Khattabi identifies concrete false affiliations
  - **issue:** target-list reliability
  - **pro:** large UAE-linked profiling operation documented
  - **resolution:** OPERATION_VERIFIED_TARGET_ASSERTIONS_NOT_AUTOMATICALLY_TRUE
- **item 2:**
  - **contra:** Constellation documents limited output and overclaiming
  - **issue:** Alp capability
  - **pro:** contracts/proposals describe extensive services
  - **resolution:** CAPABILITY_AND_SOME_EXECUTION_VERIFIED_GENERAL_EFFECT_NOT
- **item 3:**
  - **contra:** missing key transmission proof and other intelligence inputs
  - **issue:** Austria causality
  - **pro:** Vidino/Alp information overlaps later Luxor targets
  - **resolution:** PATHWAY_PARTIAL_UAE_CAUSATION_NOT_ESTABLISHED
- **item 4:**
  - **contra:** no final merits judgment; one French preliminary case procedurally closed
  - **issue:** judicial status
  - **pro:** Swiss and later French investigations opened
  - **resolution:** ALLEGATIONS_SERIOUS_AND_NONTERMINAL

### VERIFICATION_REPORT
- **independence_limits:**
  - five Mediapart records share one outlet family
  - leaked-record claims lack final merits adjudication
  - causal effect data sparse
- **negative_checks:**
  - Khattabi rebuttal retained
  - vendor overclaim retained
  - Austria causal edge not promoted
  - procedural closure not exoneration
  - no I7 claim
- **source_families:** 9
- **source_records_complete:** 13/13
- **status:** PASS_WITH_EXPLICIT_GAPS
- **web_fact_trace:** 22/22 facts mapped to accepted FETCH-backed sources

### EDI_REPORT
- **corpus:**
  - **circularity:** LOW_TO_MODERATE
  - **coverage:** CORE_CHAIN_COVERED
  - **independence:** DIVERSE_WITH_MEDIAPART_CONCENTRATION
  - **limits:**
    - five Mediapart records share one outlet family
    - no final merits adjudication
    - causal effect data sparse
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 4
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES_PARTIAL_EXECUTION
    - **gap_type:** CAUSALITY
    - **independent_families:** 3
  - **item 3:**
    - **claim_id:** CLM-005
    - **direct_object:** PARTIAL_EFFECT
    - **gap_type:** CAUSALITY
    - **independent_families:** 3
  - **item 4:**
    - **claim_id:** CLM-007
    - **direct_object:** YES_SYMMETRY_CONTROL
    - **gap_type:** COMPARABILITY
    - **independent_families:** 4
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** 9_PROVENANCE_FAMILIES
  - **perspective:** LEAK_INVESTIGATIONS+BELGIAN_GOVERNMENT+EU+SWISS_FRENCH_JUDICIAL_REPORTING
  - **stratification:** CLIENT_RECORDS+TARGET_REBUTTAL+INSTITUTIONAL_RESPONSE+JUDICIAL_STATUS
  - **temporal:** 2017-2025
- **edi:**
  - **assessment:** HIGH_CORE_CHAIN_COVERAGE_WITH_CAUSAL_AND_JUDICIAL_LIMITS
  - **flags:**
    - LEAKED_RECORD_DEPENDENCE
    - OUTLET_FAMILY_CONCENTRATION
    - TARGET_DATA_ERRORS
    - VENDOR_OVERCLAIM
    - NO_FINAL_JUDGMENT
    - NO_COUNTERFACTUAL_EFFECT
- **source_counts:**
  - **claim_source:** 0
  - **primary:** 10
  - **provenance_families:** 9
  - **secondary:** 3
  - **total:** 13

### RESPONSIBILITY_MAP
- **item 1:**
  - **highest_supported:** reported UAE intelligence-linked client, payments/tasking and operational objectives
  - **not_supported:** final judicial liability for every alleged act
  - **object:** core Alp client chain
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-009
    - FCT-013
    - FCT-017
- **item 2:**
  - **highest_supported:** large-scale lists and operational records
  - **not_supported:** truth of every affiliation or knowing state-agent status of every intermediary
  - **object:** target/intermediary universe
  - **support:**
    - FCT-004
    - FCT-008
    - FCT-010
- **item 3:**
  - **highest_supported:** partial information/research pathway and overlap
  - **not_supported:** UAE causation of police operation
  - **object:** Austria/Operation Luxor
  - **support:**
    - FCT-014
    - FCT-015
    - FCT-016

### NEXT_QUERIES
- **item 1:**
  - **query:** final Swiss/French judicial findings or authenticated tasking/contracts resolving UAE responsibility edges
  - **route:** RECHECK
  - **trigger:** new judicial/primary evidence
- **item 2:**
  - **query:** case-level causal studies of exposure, persuasion or institutional/economic outcome from Alp operations
  - **route:** DEFER
  - **trigger:** identified independent causal design
- **item 3:**
  - **query:** ally/adversary isomorphic comparison using INV-033 with INV-128/134/140/145 and adversary operations
  - **route:** MERGE
  - **trigger:** INV-146 dependency gate pass

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-003,QRY-004,QRY-006,QRY-010,QRY-011 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-006,FCT-009,FCT-013,FCT-017 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-004,QRY-005,QRY-007,QRY-010,QRY-012,QRY-013 | support:- | counter:- | results:FCT-007,FCT-008,FCT-010,FCT-015,FCT-016,FCT-018,FCT-019,FCT-022 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-001,QRY-006,QRY-010,QRY-011 | support:- | counter:- | results:FCT-001,FCT-002,FCT-009,FCT-013,FCT-017 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-010 | support:- | counter:- | results:FCT-002,FCT-013 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-001,QRY-003,QRY-004 | support:- | counter:- | results:FCT-003,FCT-004,FCT-005,FCT-006,FCT-007 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-005 | support:- | counter:- | results:FCT-008 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-002,QRY-012,QRY-013 | support:- | counter:- | results:FCT-018,FCT-019,FCT-020,FCT-021,FCT-022 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-008,QRY-009 | support:- | counter:- | results:FCT-011,FCT-012 | final:SATURATED | gap:NONE
AXS-007 | attempts:QRY-010 | support:- | counter:- | results:FCT-014,FCT-015,FCT-016 | final:SATURATED | gap:NONE
AXS-008 | attempts:QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-017,FCT-018,FCT-019,FCT-020 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,QRY-006,QRY-010,QRY-011,SRC-001,SRC-006,SRC-010,SRC-011 | support:FCT-001,FCT-002,FCT-003,FCT-009,FCT-013,FCT-017 | counter:CTRL-001 | results:FCT-001,FCT-002,FCT-003,FCT-009,FCT-013,FCT-017,CTRL-001 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-002 | attempts:QRY-003,QRY-004,QRY-007,SRC-003,SRC-004,SRC-007 | support:FCT-004,FCT-005,FCT-006,FCT-007,FCT-010 | counter:CTRL-002;CTRL-003 | results:FCT-004,FCT-005,FCT-006,FCT-007,FCT-010,CTRL-002;CTRL-003 | final:SUPPORTED | gap:CAUSALITY
CLM-003 | attempts:QRY-005,SRC-005 | support:FCT-008 | counter:CTRL-004 | results:FCT-008,CTRL-004 | final:PARTIAL | gap:RESPONSIBILITY
CLM-004 | attempts:QRY-010,SRC-010 | support:FCT-014,FCT-015,FCT-016 | counter:CTRL-005 | results:FCT-014,FCT-015,FCT-016,CTRL-005 | final:PARTIAL | gap:CAUSALITY
CLM-005 | attempts:QRY-002,QRY-008,SRC-002,SRC-008 | support:FCT-011,FCT-021,FCT-022 | counter:CTRL-007 | results:FCT-011,FCT-021,FCT-022,CTRL-007 | final:PARTIAL | gap:CAUSALITY
CLM-006 | attempts:QRY-011,QRY-012,QRY-013,SRC-011,SRC-012,SRC-013 | support:FCT-017,FCT-018,FCT-019,FCT-020 | counter:CTRL-006 | results:FCT-017,FCT-018,FCT-019,FCT-020,CTRL-006 | final:SUPPORTED | gap:TEMPORAL
CLM-007 | attempts:QRY-001,QRY-002,QRY-004,QRY-008,QRY-011,SRC-001,SRC-002,SRC-004,SRC-008,SRC-011 | support:FCT-001,FCT-002,FCT-006,FCT-011,FCT-017,FCT-022 | counter:CTRL-001;CTRL-007 | results:FCT-001,FCT-002,FCT-006,FCT-011,FCT-017,FCT-022,CTRL-001;CTRL-007 | final:SUPPORTED | gap:COMPARABILITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-001 | CLM | SUPPORTED | RESPONSIBILITY | No final judicial merits judgment in the examined sources establishes criminal liability for the full chain.
CLM-002 | CLM | SUPPORTED | CAUSALITY | Execution and effect are not established for every mapped target or proposed action.
CLM-003 | CLM | PARTIAL | RESPONSIBILITY | Individual knowledge, intent and tasking remain case-specific.
CLM-004 | CLM | PARTIAL | CAUSALITY | The decisive UAE-to-Austrian-decision causal edge is not proven and other intelligence inputs are documented.
CLM-005 | CLM | PARTIAL | CAUSALITY | No independent causal design isolates campaign contribution to policy, voting or final economic outcome.
CLM-006 | CLM | SUPPORTED | TEMPORAL | No final conviction/acquittal resolving the core state-tasking allegations is available in the examined record.
CLM-007 | CLM | SUPPORTED | COMPARABILITY | Symmetry of public labeling or enforcement is a separate comparative question for INV-146.
CAU-001 | CAU | UNRESOLVED | CAUSALITY | I0-I3 are strong for the core Alp/UAE client chain; I4 is case-specific; I5 persuasion is not measured; I6 is partial for selected diplomatic/economic consequences; I7 counterfactual political/electoral outcome is not established.

SEMANTIC_COUNTS_V1:LED:2|CLM:7|AXS:8|CAU:1|CTRL:7|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-003","QRY-004","QRY-006","QRY-010","QRY-011"],"evidence_excerpt":"Internal-record reporting supports client, payment, tasking and operation edges; judicial sources preserve the distinction between reported evidence and final liability.","kind":"HYPOTHESIS","lead":"A documented UAE-state/intelligence client chain exists for covert reputation and influence-for-hire operations in Europe, but execution and effect vary by sub-operation and cannot be generalized to every Emirati interest or aligned actor.","linked_ids":["CLM-001","CLM-002","CLM-006","CLM-007"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-006","FCT-009","FCT-013","FCT-017"],"routes":["CLIENT_CHAIN","SYMMETRY_CONTROL"],"source_id":"INV-033_RUN_CARD","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-004","QRY-005","QRY-007","QRY-010","QRY-012","QRY-013"],"evidence_excerpt":"The counter-evidence directly shows false target data, overclaimed capability, missing transmission edges, procedural legal limits and unresolved outcome causality.","kind":"METHOD_CONSTRAINT","lead":"State/client identity, payment, tasking, operations, intermediaries, exposure and effect are separate edges; private Emirati origin, shared anti-Brotherhood framing, access or commercial relationship do not substitute for UAE-state tasking or causal effect.","linked_ids":["CLM-002","CLM-003","CLM-004","CLM-005","CTRL-002","CTRL-003","CTRL-004","CTRL-005","CTRL-006","CTRL-007"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-007","FCT-008","FCT-010","FCT-015","FCT-016","FCT-018","FCT-019","FCT-022"],"routes":["ATTRIBUTION","CONTROL","CAUSALITY"],"source_id":"INV-033_RUN_CARD","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"A materially documented UAE intelligence/client-to-Alp chain existed for covert reputation and influence operations in Europe, supported by internal records reporting payments, commissions, communications and operational objectives.","claimant":"INV-033 synthesis","counter":"CTRL-001","gap":"No final judicial merits judgment in the examined sources establishes criminal liability for the full chain.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-009","FCT-013","FCT-017"]}
CLM-002 | {"claim":"Alp performed large-scale profiling and targeted reputation/influence work across Europe, including France, but target lists and proposals vary in reliability and cannot all be promoted to executed or successful operations.","claimant":"INV-033 synthesis","counter":"CTRL-002;CTRL-003","gap":"Execution and effect are not established for every mapped target or proposed action.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-004","FCT-005","FCT-006","FCT-007","FCT-010"]}
CLM-003 | {"claim":"Journalists and other intermediaries appear in Alp operational/payment records as dissemination or research channels, but the evidence does not support generalizing ultimate-client knowledge or UAE-state tasking to each intermediary.","claimant":"INV-033 synthesis","counter":"CTRL-004","gap":"Individual knowledge, intent and tasking remain case-specific.","gap_type":"RESPONSIBILITY","materiality":"HIGH","status":"PARTIAL","support":["FCT-008"]}
CLM-004 | {"claim":"The Austria/Operation Luxor material demonstrates a plausible pathway by which private intelligence/research can enter institutional decision environments, but does not establish that the UAE caused Operation Luxor.","claimant":"INV-033 synthesis","counter":"CTRL-005","gap":"The decisive UAE-to-Austrian-decision causal edge is not proven and other intelligence inputs are documented.","gap_type":"CAUSALITY","materiality":"HIGH","status":"PARTIAL","support":["FCT-014","FCT-015","FCT-016"]}
CLM-005 | {"claim":"The affair produced documented institutional and economic downstream consequences in selected cases, including a Belgian diplomatic response and severe consequences around Lord Energy, while persuasion and counterfactual political/electoral effect remain unestablished.","claimant":"INV-033 synthesis","counter":"CTRL-007","gap":"No independent causal design isolates campaign contribution to policy, voting or final economic outcome.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-011","FCT-021","FCT-022"]}
CLM-006 | {"claim":"Judicial treatment remains non-terminal: Switzerland opened a federal investigation, a French preliminary case was procedurally closed without a merits exoneration, and a later French judicial investigation was opened on a separate complaint.","claimant":"INV-033 synthesis","counter":"CTRL-006","gap":"No final conviction/acquittal resolving the core state-tasking allegations is available in the examined record.","gap_type":"TEMPORAL","materiality":"HIGH","status":"SUPPORTED","support":["FCT-017","FCT-018","FCT-019","FCT-020"]}
CLM-007 | {"claim":"INV-033 is a material ally/adversary symmetry control for INV-146 because a covert influence-for-hire chain linked by reported internal records to an allied/partner-state intelligence client is documentable, while the same evidentiary ceilings on tasking, execution and effect must apply as in adversary cases.","claimant":"INV-033 synthesis","counter":"CTRL-001;CTRL-007","gap":"Symmetry of public labeling or enforcement is a separate comparative question for INV-146.","gap_type":"COMPARABILITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-006","FCT-011","FCT-017","FCT-022"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-006","QRY-010","QRY-011"],"axis":"CLIENT_ATTRIBUTION","links":["CLM-001","CTRL-001"],"question":"Can the Emirati client be tied to state/intelligence structures rather than inferred from nationality or interest?","result_ids":["FCT-001","FCT-002","FCT-009","FCT-013","FCT-017"],"sought_objects":["CLIENT","STATE_RELATION","TASKING"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-001","QRY-010"],"axis":"CONTRACT_PAYMENT","links":["CLM-001"],"question":"Are payments, commissions or contracts documented between the client and Alp?","result_ids":["FCT-002","FCT-013"],"sought_objects":["PAYMENT","CONTRACT","COMMISSION"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-001","QRY-003","QRY-004"],"axis":"OPERATIONS_TARGETS","links":["CLM-002","CTRL-002","CTRL-003"],"question":"Which profiling, reputation, counter-lobbying or covert operations were proposed or executed and against whom?","result_ids":["FCT-003","FCT-004","FCT-005","FCT-006","FCT-007"],"sought_objects":["TARGET","OPERATION","DELIVERABLE"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-005"],"axis":"MEDIA_INTERMEDIARIES","links":["CLM-003","CTRL-004"],"question":"What role did journalists or other intermediaries play, and what is proven about their knowledge or tasking?","result_ids":["FCT-008"],"sought_objects":["INTERMEDIARY","PAYMENT","KNOWLEDGE"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-002","QRY-012","QRY-013"],"axis":"FRANCE_EFFECT","links":["CLM-005","CLM-006","CTRL-006","CTRL-007"],"question":"What downstream consequences in France can be documented without overstating causality?","result_ids":["FCT-018","FCT-019","FCT-020","FCT-021","FCT-022"],"sought_objects":["REPUTATION","ECONOMIC_EFFECT","JUDICIAL_RESPONSE"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-008","QRY-009"],"axis":"EU_INSTITUTIONAL_RESPONSE","links":["CLM-005","CTRL-007"],"question":"What institutional or diplomatic responses followed the revelations?","result_ids":["FCT-011","FCT-012"],"sought_objects":["DIPLOMATIC_RESPONSE","EU_RESPONSE"],"status":"SATURATED"}
AXS-007 | {"attempt_ids":["QRY-010"],"axis":"AUSTRIA_CAUSAL_CONTROL","links":["CLM-004","CTRL-005"],"question":"Does the Austrian material prove UAE causation of Operation Luxor or only a partial information pathway?","result_ids":["FCT-014","FCT-015","FCT-016"],"sought_objects":["INFORMATION_FLOW","INSTITUTIONAL_ACTION","CAUSAL_EDGE"],"status":"SATURATED"}
AXS-008 | {"attempt_ids":["QRY-011","QRY-012","QRY-013"],"axis":"JUDICIAL_STATUS","links":["CLM-006","CTRL-006"],"question":"What has judicial or prosecutorial action established, and what remains allegation?","result_ids":["FCT-017","FCT-018","FCT-019","FCT-020"],"sought_objects":["INVESTIGATION","CLOSURE","JUDICIAL_FINDING"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"Bad source data, Alp capability overclaim, intermediary autonomy, other intelligence inputs, editorial/institutional agency and ordinary market/legal causes can break or confound downstream links.","gap":"I0-I3 are strong for the core Alp/UAE client chain; I4 is case-specific; I5 persuasion is not measured; I6 is partial for selected diplomatic/economic consequences; I7 counterfactual political/electoral outcome is not established.","gap_type":"CAUSALITY","limit":"Operation existence and even documented downstream reaction do not identify the counterfactual share of the covert campaign in policy, voting or final institutional/economic outcomes.","mechanism":"UAE intelligence/client -> payment/tasking of Alp -> profiling/reputation or counter-lobbying operations -> intermediaries/platforms/institutions -> exposure -> reception -> economic/institutional/political effect -> counterfactual outcome","status":"UNRESOLVED","support":["FCT-001","FCT-002","FCT-003","FCT-006","FCT-008","FCT-011","FCT-013","FCT-021"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Attribution control: leaked internal records and cross-outlet reporting can establish a strong client/tasking chain, but they do not equal a final judicial conviction of UAE officials or Alp principals.","status":"DONE","support":["FCT-001","FCT-002","FCT-009","FCT-013","FCT-017"]}
CTRL-002 | {"control":"Capability control: Alp proposals, commercial claims and claimed political access do not prove that every proposed operation was executed or effective; Operation Constellation includes documented overclaiming.","status":"DONE","support":["FCT-006","FCT-007"]}
CTRL-003 | {"control":"Data-quality control: Zakia Khattabi's official rebuttal identifies specific factual errors in the profiling material, so inclusion in an Alp/UAE map cannot be treated as proof of the alleged affiliation.","status":"DONE","support":["FCT-004","FCT-010"]}
CTRL-004 | {"control":"Intermediary-intent control: an Alp payment or subcontracting record can document a transaction, but does not by itself prove that a journalist or intermediary knew the ultimate UAE client, shared its purpose, or acted under state tasking.","status":"DONE","support":["FCT-008"]}
CTRL-005 | {"control":"Austria causal control: Vidino/Alp information flows and overlap with later Operation Luxor targets do not establish that UAE tasking caused the Austrian police operation; Profil explicitly records missing proof for one transmission edge and other intelligence inputs.","status":"DONE","support":["FCT-014","FCT-015","FCT-016"]}
CTRL-006 | {"control":"Judicial-status control: Swiss and French proceedings show serious allegations under investigation, but investigation != guilt and a procedural closure != merits exoneration.","status":"DONE","support":["FCT-017","FCT-018","FCT-019","FCT-020"]}
CTRL-007 | {"control":"Effect control: Belgium's diplomatic summons and the Nada/Lord Energy sequence are documented downstream consequences or reactions, but they do not establish a counterfactual electoral or policy outcome caused solely by the UAE-linked campaign.","status":"DONE","support":["FCT-011","FCT-021","FCT-022"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:13|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | MNEMO_Q | MNEMO_Q subject_fingerprint
SYS-003 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | MNEMO_Q | MNEMO_Q
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | PASS | SRC-001 | https://www.mediapart.fr/en/journal/france/040323/leaked-data-shows-extent-uaes-meddling-france | Mediapart leaked data UAE meddling France Alp Services
QRY-002 | FETCH | PASS | SRC-002 | https://www.newyorker.com/magazine/2023/04/03/the-dirty-secrets-of-a-smear-campaign | New Yorker dirty secrets smear campaign Alp Services UAE
QRY-003 | FETCH | PASS | SRC-003 | https://www.mediapart.fr/journal/international/070723/plus-de-200-francais-ont-ete-fiches-pour-le-compte-des-services-secrets-des-emirats-arabes-unis/prolonger | Mediapart 200 French people profiled UAE intelligence Alp Services
QRY-004 | FETCH | PASS | SRC-004 | https://www.mediapart.fr/journal/international/090723/operation-constellation-les-pieds-nickeles-d-abou-dhabi-bruxelles | Mediapart Operation Constellation UAE Brussels counter lobbying
QRY-005 | FETCH | PASS | SRC-005 | https://www.mediapart.fr/journal/france/100723/un-pilier-d-europe-1-ex-de-valeurs-actuelles-dans-la-main-des-barbouzes-des-emirats | Mediapart paid journalists Alp Services UAE
QRY-006 | FETCH | PASS | SRC-006 | https://www.mediapart.fr/journal/international/130723/onu-qatar-macron-les-operations-secretes-du-sheikh-matar-agent-des-emirats | Mediapart Sheikh Matar UAE operations Europe
QRY-007 | FETCH | PASS | SRC-007 | https://news.belgium.be/fr/les-secrets-dabou-dhabi-zakia-khattabi-denonce-une-enquete-fantaisiste-et-refute-tout-lien-avec-le | Belgian government Khattabi Abu Dhabi Secrets response
QRY-008 | FETCH | PASS | SRC-008 | https://www.standaard.be/binnenland/belgie-roept-emiraten-op-het-matje-over-abu-dhabi-secrets/40689421.html | Belgium summons UAE ambassador Abu Dhabi Secrets
QRY-009 | FETCH | PASS | SRC-009 | https://www.europarl.europa.eu/doceo/document/P-9-2023-002379-ASW_EN.html | European Commission answer Abu Dhabi Secrets FIMI
QRY-010 | FETCH | PASS | SRC-010 | https://www.profil.at/investigativ/inside-the-united-arab-emirates-spy-campaign-in-europe/402598541 | Profil UAE spy campaign Austria Alp Services
QRY-011 | FETCH | PASS | SRC-011 | https://www.rsi.ch/info/ticino-grigioni-e-insubria/Abu-Dhabi-Secrets-aperta-inchiesta-per-spionaggio--2123236.html | RSI Swiss federal investigation Alp Services UAE
QRY-012 | FETCH | PASS | SRC-012 | https://www.leparisien.fr/faits-divers/agence-suisse-accusee-despionnage-pour-les-emirats-lenquete-classee-par-la-justice-francaise-21-06-2024-CSUQERHPSBAJVL65XYNIVI3GR4.php | Paris prosecutor Alp Services case closed procedural 2024
QRY-013 | FETCH | PASS | SRC-013 | https://www.lemonde.fr/societe/article/2025/08/22/accusations-d-espionnage-d-une-communicante-du-qatar-en-france-une-information-judiciaire-ouverte_6633518_3224.html | Sihem Souid judicial investigation Alp Services UAE 2025

## EVIDENCE_REGISTRY
SRC-001 | ◉ | fam:other:media-mediapart | https://www.mediapart.fr/en/journal/france/040323/leaked-data-shows-extent-uaes-meddling-france | Leaked data shows extent of UAE meddling in France | 2023-03-04 | 2026-09-07T05:20:00+00:00 | contracts/client/targets sections | https://www.mediapart.fr/en/journal/france/040323/leaked-data-shows-extent-uaes-meddling-france
SRC-002 | ◉ | fam:other:media-newyorker | https://www.newyorker.com/magazine/2023/04/03/the-dirty-secrets-of-a-smear-campaign | The Dirty Secrets of a Smear Campaign | 2023-03-27 | 2026-09-07T05:20:00+00:00 | Nada/Lord Energy investigation | https://www.newyorker.com/magazine/2023/04/03/the-dirty-secrets-of-a-smear-campaign
SRC-003 | ◉ | fam:other:media-mediapart | https://www.mediapart.fr/journal/international/070723/plus-de-200-francais-ont-ete-fiches-pour-le-compte-des-services-secrets-des-emirats-arabes-unis/prolonger | Plus de 200 Français ont été fichés pour le compte des services secrets des Émirats arabes unis | 2023-07-07 | 2026-09-07T05:20:00+00:00 | profiling/list operation | https://www.mediapart.fr/journal/international/070723/plus-de-200-francais-ont-ete-fiches-pour-le-compte-des-services-secrets-des-emirats-arabes-unis/prolonger
SRC-004 | ◉ | fam:other:media-mediapart | https://www.mediapart.fr/journal/international/090723/operation-constellation-les-pieds-nickeles-d-abou-dhabi-bruxelles | Opération Constellation : les pieds nickelés d’Abou Dhabi à Bruxelles | 2023-07-09 | 2026-09-07T05:20:00+00:00 | Constellation objectives/results | https://www.mediapart.fr/journal/international/090723/operation-constellation-les-pieds-nickeles-d-abou-dhabi-bruxelles
SRC-005 | ◉ | fam:other:media-mediapart | https://www.mediapart.fr/journal/france/100723/un-pilier-d-europe-1-ex-de-valeurs-actuelles-dans-la-main-des-barbouzes-des-emirats | Un pilier d’Europe 1, ex de Valeurs actuelles, dans la main des barbouzes des Émirats | 2023-07-10 | 2026-09-07T05:20:00+00:00 | journalist subcontractor allegations/denials | https://www.mediapart.fr/journal/france/100723/un-pilier-d-europe-1-ex-de-valeurs-actuelles-dans-la-main-des-barbouzes-des-emirats
SRC-006 | ◉ | fam:other:media-mediapart | https://www.mediapart.fr/journal/international/130723/onu-qatar-macron-les-operations-secretes-du-sheikh-matar-agent-des-emirats | ONU, Qatar, Macron : les opérations secrètes du Sheikh Matar, agent des Émirats | 2023-07-13 | 2026-09-07T05:20:00+00:00 | agent/tasking operations | https://www.mediapart.fr/journal/international/130723/onu-qatar-macron-les-operations-secretes-du-sheikh-matar-agent-des-emirats
SRC-007 | ◈ | fam:other:belgium-government | https://news.belgium.be/fr/les-secrets-dabou-dhabi-zakia-khattabi-denonce-une-enquete-fantaisiste-et-refute-tout-lien-avec-le | Les secrets d’Abou Dhabi : Zakia Khattabi dénonce une enquête fantaisiste | 2023-07-07 | 2026-09-07T05:20:00+00:00 | minister response | https://news.belgium.be/fr/les-secrets-dabou-dhabi-zakia-khattabi-denonce-une-enquete-fantaisiste-et-refute-tout-lien-avec-le
SRC-008 | ◉ | fam:other:media-destandaard | https://www.standaard.be/binnenland/belgie-roept-emiraten-op-het-matje-over-abu-dhabi-secrets/40689421.html | België roept Emiraten op het matje over Abu Dhabi Secrets | 2023-07-11 | 2026-09-07T05:20:00+00:00 | foreign ministry summons/official quote | https://www.standaard.be/binnenland/belgie-roept-emiraten-op-het-matje-over-abu-dhabi-secrets/40689421.html
SRC-009 | ◈ | fam:other:eu-parliament-commission | https://www.europarl.europa.eu/doceo/document/P-9-2023-002379-ASW_EN.html | Answer for question P-002379/2023 on Abu Dhabi Secrets | 2023-08-28 | 2026-09-07T05:20:00+00:00 | Commission/HR answer | https://www.europarl.europa.eu/doceo/document/P-9-2023-002379-ASW_EN.html
SRC-010 | ◉ | fam:other:media-profil | https://www.profil.at/investigativ/inside-the-united-arab-emirates-spy-campaign-in-europe/402598541 | Inside the United Arab Emirate’s spy campaign in Europe | 2023-09-19 | 2026-09-07T05:20:00+00:00 | lines 60-200, 244-322 | https://www.profil.at/investigativ/inside-the-united-arab-emirates-spy-campaign-in-europe/402598541
SRC-011 | ◈ | fam:other:swiss-public-broadcaster-judicial | https://www.rsi.ch/info/ticino-grigioni-e-insubria/Abu-Dhabi-Secrets-aperta-inchiesta-per-spionaggio--2123236.html | Abu Dhabi Secrets, aperta inchiesta per spionaggio | 2024-04-15 | 2026-09-07T05:20:00+00:00 | Swiss federal investigation | https://www.rsi.ch/info/ticino-grigioni-e-insubria/Abu-Dhabi-Secrets-aperta-inchiesta-per-spionaggio--2123236.html
SRC-012 | ◉ | fam:other:media-afp-leparisien | https://www.leparisien.fr/faits-divers/agence-suisse-accusee-despionnage-pour-les-emirats-lenquete-classee-par-la-justice-francaise-21-06-2024-CSUQERHPSBAJVL65XYNIVI3GR4.php | Agence suisse accusée d’espionnage pour les Émirats : l’enquête classée par la justice française | 2024-06-21 | 2026-09-07T05:20:00+00:00 | Paris prosecutor closure reasons | https://www.leparisien.fr/faits-divers/agence-suisse-accusee-despionnage-pour-les-emirats-lenquete-classee-par-la-justice-francaise-21-06-2024-CSUQERHPSBAJVL65XYNIVI3GR4.php
SRC-013 | ◉ | fam:other:media-lemonde | https://www.lemonde.fr/societe/article/2025/08/22/accusations-d-espionnage-d-une-communicante-du-qatar-en-france-une-information-judiciaire-ouverte_6633518_3224.html | Accusations d’espionnage d’une communicante du Qatar en France : une information judiciaire ouverte | 2025-08-22 | 2026-09-07T05:20:00+00:00 | Créteil judicial investigation | https://www.lemonde.fr/societe/article/2025/08/22/accusations-d-espionnage-d-une-communicante-du-qatar-en-france-une-information-judiciaire-ouverte_6633518_3224.html

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.mediapart.fr/en/journal/france/040323/leaked-data-shows-extent-uaes-meddling-france | other:media-mediapart | 2023-03-04 | Alp Services Emirati intelligence client | Mediapart reports from leaked internal Alp records that a senior Abu Dhabi intelligence officer used Alp Services for at least four years, with meetings and encrypted communications between the firm and Emirati intelligence contacts. | -
FCT-002 | FACT | ✧ | https://www.mediapart.fr/en/journal/france/040323/leaked-data-shows-extent-uaes-meddling-france | other:media-mediapart | 2018-11 | Alp commissions and contract scale | An internal message cited by Mediapart states that an Emirati contact entrusted Alp with three commissions totaling EUR 1 million in November 2018; Mediapart also reports a later contract worth CHF 1.2 million every six months. | -
FCT-003 | FACT | ✧ | https://www.mediapart.fr/en/journal/france/040323/leaked-data-shows-extent-uaes-meddling-france | other:media-mediapart | 2023-03-04 | Anti-Qatar EU influence proposal | Documents reviewed by Mediapart describe a mandate to investigate Qatar-linked lobbyists, influencers and journalists in the EU and Alp proposals to counter Qatar lobbying by feeding information to friendly politicians and preparing litigation files. | -
FCT-004 | FACT | ✧ | https://www.mediapart.fr/journal/international/070723/plus-de-200-francais-ont-ete-fiches-pour-le-compte-des-services-secrets-des-emirats-arabes-unis/prolonger | other:media-mediapart | 2023-07-07 | European profiling scale | Mediapart/EIC report that Alp Services supplied UAE intelligence with files covering more than 1,000 individuals and more than 400 organisations across 18 European countries, including more than 200 individuals and about 120 organisations in France. | -
FCT-005 | FACT | ✧ | https://www.mediapart.fr/journal/international/070723/plus-de-200-francais-ont-ete-fiches-pour-le-compte-des-services-secrets-des-emirats-arabes-unis/prolonger | other:media-mediapart | 2023-07-07 | Profiling and discredit strategy | Mediapart/EIC report that the Alp mandate combined mapping of supposed Muslim Brotherhood-linked people and organisations with a strategy to discredit selected targets through compromising information and influence actions. | -
FCT-006 | FACT | ✧ | https://www.mediapart.fr/journal/international/090723/operation-constellation-les-pieds-nickeles-d-abou-dhabi-bruxelles | other:media-mediapart | 2023-07-09 | Operation Constellation objective | Mediapart describes Operation Constellation as a covert counter-lobbying effort commissioned after an Abu Dhabi meeting to identify, hinder and attack networks perceived as serving Qatari interests around EU institutions. | -
FCT-007 | FACT | ✧ | https://www.mediapart.fr/journal/international/090723/operation-constellation-les-pieds-nickeles-d-abou-dhabi-bruxelles | other:media-mediapart | 2023-07-09 | Alp capability overclaim control | The same Constellation reporting says Alp found little beyond the Avisa case and at times presented supposed political influence or operational success that the investigation characterized as exaggerated or imaginary. | -
FCT-008 | FACT | ✧ | https://www.mediapart.fr/journal/france/100723/un-pilier-d-europe-1-ex-de-valeurs-actuelles-dans-la-main-des-barbouzes-des-emirats | other:media-mediapart | 2023-07-10 | Journalists in Alp records | Mediapart reports that several journalists appeared in Alp internal records as paid contributors or subcontractors on UAE-linked missions; the records alone do not establish each individual’s knowledge of the ultimate client or state purpose. | -
FCT-009 | FACT | ✧ | https://www.mediapart.fr/journal/international/130723/onu-qatar-macron-les-operations-secretes-du-sheikh-matar-agent-des-emirats | other:media-mediapart | 2023-07-13 | Sheikh Matar investigative attribution | Mediapart/EIC identify the figure called Sheikh Matar in Alp records as an Emirati intelligence officer coordinating operations in Europe; this is an investigative attribution based on leaked records and sources, not a final judicial finding. | -
FCT-010 | FACT | ✧ | https://news.belgium.be/fr/les-secrets-dabou-dhabi-zakia-khattabi-denonce-une-enquete-fantaisiste-et-refute-tout-lien-avec-le | other:belgium-government | 2023-07-07 | Khattabi factual rebuttal | Belgian federal minister Zakia Khattabi publicly rebutted Alp-linked claims about her, stating among other points that she was neither vice-president of the Executive of Muslims of Belgium nor Shia. | -
FCT-011 | FACT | ✧ | https://www.standaard.be/binnenland/belgie-roept-emiraten-op-het-matje-over-abu-dhabi-secrets/40689421.html | other:media-destandaard | 2023-07-11 | Belgium summons UAE ambassador | Belgian Foreign Affairs summoned the UAE ambassador and requested explanations after the Abu Dhabi Secrets revelations, creating a documented diplomatic institutional response. | -
FCT-012 | FACT | ✧ | https://www.europarl.europa.eu/doceo/document/P-9-2023-002379-ASW_EN.html | other:eu-parliament-commission | 2023-08-28 | EU institutional acknowledgement | The EU High Representative/Commission stated that it had taken note of the Abu Dhabi Secrets findings and was following the matter with Member States, while leaving investigation and enforcement to competent authorities. | -
FCT-013 | FACT | ✧ | https://www.profil.at/investigativ/inside-the-united-arab-emirates-spy-campaign-in-europe/402598541 | other:media-profil | 2023-09-19 | Profil leaked-record payment chain | Profil reports that leaked Alp files contain payment records and communications linking the firm to an Emirati official from 2017 and describe services including reputational operations, surveillance and offensive viral communications. | -
FCT-014 | FACT | ✧ | https://www.profil.at/investigativ/inside-the-united-arab-emirates-spy-campaign-in-europe/402598541 | other:media-profil | 2023-09-19 | Vidino information contract | Profil reports that Lorenzo Vidino had a contract with Alp from 2018 to provide confidential indications, rumours and information about organisations, individuals and funding relevant to Muslim Brotherhood mapping. | -
FCT-015 | FACT | ✧ | https://www.profil.at/investigativ/inside-the-united-arab-emirates-spy-campaign-in-europe/402598541 | other:media-profil | 2023-09-19 | EICTP transmission negative control | Profil explicitly states that it found no definitive proof that an EICTP actor-analysis document was transmitted to the UAE, and the Austrian actors concerned denied instrumentalisation or lobbying. | -
FCT-016 | FACT | ✧ | https://www.profil.at/investigativ/inside-the-united-arab-emirates-spy-campaign-in-europe/402598541 | other:media-profil | 2023-09-19 | Operation Luxor causal boundary | Profil found overlap between people appearing in anti-Muslim-Brotherhood research and later Operation Luxor suspects, but did not establish that UAE tasking caused the Austrian police operation; its reporting also notes information from other Arab intelligence services in the Luxor file. | -
FCT-017 | FACT | ✧ | https://www.rsi.ch/info/ticino-grigioni-e-insubria/Abu-Dhabi-Secrets-aperta-inchiesta-per-spionaggio--2123236.html | other:swiss-public-broadcaster-judicial | 2024-04-15 | Swiss federal investigation | Swiss federal prosecutors opened an investigation into the Geneva private-intelligence company and principals suspected of conducting activities for the UAE, including possible political espionage and acts for a foreign state; suspicion is not conviction. | -
FCT-018 | FACT | ✧ | https://www.leparisien.fr/faits-divers/agence-suisse-accusee-despionnage-pour-les-emirats-lenquete-classee-par-la-justice-francaise-21-06-2024-CSUQERHPSBAJVL65XYNIVI3GR4.php | other:media-afp-leparisien | 2024-06-21 | French preliminary case procedural closure | A Paris preliminary investigation triggered by complaints linked to the Alp affair was closed without prosecution after investigators failed to obtain additional material and could not effectively hear Brero/Alp; French authorities referred elements to Switzerland. | -
FCT-019 | FACT | ✧ | https://www.leparisien.fr/faits-divers/agence-suisse-accusee-despionnage-pour-les-emirats-lenquete-classee-par-la-justice-francaise-21-06-2024-CSUQERHPSBAJVL65XYNIVI3GR4.php | other:media-afp-leparisien | 2024-06-21 | Procedural closure is not merits exoneration | The reported reason for the French closure was evidentiary/procedural difficulty rather than a judicial finding that the alleged operations had not occurred. | -
FCT-020 | FACT | ✧ | https://www.lemonde.fr/societe/article/2025/08/22/accusations-d-espionnage-d-une-communicante-du-qatar-en-france-une-information-judiciaire-ouverte_6633518_3224.html | other:media-lemonde | 2025-08-22 | Souid judicial investigation | Le Monde reports that a French judicial investigation was opened in 2025 following Sihem Souid’s complaint concerning alleged burglary, invasion of home/privacy and correspondence offences connected to the wider affair; the allegations remain subject to judicial determination. | -
FCT-021 | FACT | ✧ | https://www.newyorker.com/magazine/2023/04/03/the-dirty-secrets-of-a-smear-campaign | other:media-newyorker | 2023-03-27 | Hazim Nada and Lord Energy sequence | The New Yorker documents a smear campaign targeting Hazim Nada and Lord Energy and a subsequent sequence involving reputational damage, banking restrictions and collapse of the business; the chronology does not by itself identify the counterfactual contribution of each influence action. | -
FCT-022 | FACT | ✧ | https://www.newyorker.com/magazine/2023/04/03/the-dirty-secrets-of-a-smear-campaign | other:media-newyorker | 2023-03-27 | Outcome causality limit | The available reporting supports exposure and serious downstream consequences in selected cases, but does not provide a causal design proving that the covert campaign alone produced the economic, institutional or political outcomes. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-003
FCT-005 | SRC-003
FCT-006 | SRC-004
FCT-007 | SRC-004
FCT-008 | SRC-005
FCT-009 | SRC-006
FCT-010 | SRC-007
FCT-011 | SRC-008
FCT-012 | SRC-009
FCT-013 | SRC-010
FCT-014 | SRC-010
FCT-015 | SRC-010
FCT-016 | SRC-010
FCT-017 | SRC-011
FCT-018 | SRC-012
FCT-019 | SRC-012
FCT-020 | SRC-013
FCT-021 | SRC-002
FCT-022 | SRC-002

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

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:Scope and evidence axes
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:Search and source acceptance
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:Freeze source-backed facts and provenance independence
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:Formalize causal boundary and effect ceiling
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 | NEXT_ACTION:Verify attribution, relation and symmetry controls
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:Close accountability and technical narrative
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:Write frozen technical narrative and execute PRE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-07T05:30:39.449255+00:00","fact_mem":{},"mnemo_row":"BLOCKED:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":22,"eligible":22,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:BLOCKED:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:22;attempted:0;success:0;failure:0;blocked:22} | WRITEBACK_EXECUTION_V1:[22 rows, see section]

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
