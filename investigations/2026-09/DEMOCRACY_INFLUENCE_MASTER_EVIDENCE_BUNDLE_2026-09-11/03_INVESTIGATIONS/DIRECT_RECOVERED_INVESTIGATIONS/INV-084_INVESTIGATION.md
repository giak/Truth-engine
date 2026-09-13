ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260910-0558-news-agencies-agenda-setting | PARENT_RUN_ID:NONE | AS_OF:2026-09-10
INPUT_KIND:RUN_CARD | MISSION_MODE:DEEPEN | INPUT_REF:PATH:/mnt/data/inv084/runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-10_news-agencies-agenda-setting/2026-09-10_05-58_news-agencies-agenda-setting_INPUT.md | SUBJECT_SLUG:news-agencies-agenda-setting | SUBJECT_FP:sha256:aa7cfa29975454b03e51573cce3bcb5c7cf932bd1478dcd028582940e0d88850 | INPUT_SHA256:sha256:5486d53b6956ef12c6a66a636445086fbcf5190346e37c3a328f6a9f346bd71b
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France and European information space, mainly 2019-2026; trace event/source -> agency selection/verification/framing -> wire -> syndication/reuse -> downstream agenda/framing -> any demonstrable effect.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/NETWORK.md,clusters/FRAMING.md,clusters/POWER.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Objet et résultat

L'objet est le pouvoir d'agenda exercé en amont par AFP, Reuters et AP, non une hypothèse de coordination politique entre ces agences. Le corpus ferme solidement la capacité de production, de sélection et de distribution, ainsi que la reprise aval de contenu d'agence. Il ne ferme pas un effet de persuasion ou un effet électoral/politique attribuable à cette origine éditoriale.

## Infrastructure de production et de distribution

Reuters décrit un réseau de 2 600 journalistes dans 165 pays et une production annuelle d'environ deux millions de sujets texte, 1,5 million d'images et 130 000 vidéos. Reuters Connect intègre flux, API, alertes, calendrier éditorial et plus de cent partenaires de contenu. Ces éléments établissent une capacité de mise à disposition rapide et industrialisée dans les workflows de clients [FCT-001; FCT-002; FCT-003].

AFP déclare un réseau couvrant 150 pays et 260 implantations, avec environ 2 300 dépêches texte, 3 000 photos et 300 vidéos par jour dans ses chiffres 2024. L'agence indique des milliers de clients médias, dont plusieurs grands médias européens. Cette combinaison capacité de collecte, production continue et clientèle étendue constitue une infrastructure de propagation potentielle [FCT-005; FCT-006; FCT-007].

AP déclare des clients dans 126 pays et estime que quatre milliards de personnes voient quotidiennement son contenu. Son rapport 2025 indique environ 5 000 éléments journalistiques par jour et un logiciel de workflow utilisé par plus de 65 000 professionnels dans plus de 800 rédactions. La puissance structurelle ne tient donc pas seulement au volume, mais aussi à l'intégration des contenus dans les chaînes de production aval [FCT-010; FCT-011].

## Le filtre éditorial existe avant la reprise

Les trois organisations publient des règles qui confirment que la dépêche n'est pas un flux brut. Reuters subordonne la vitesse à l'exactitude et à l'équilibre, prévoit la correction transparente et encadre le sourçage. AFP exige vérification, sourcing transparent, contestation active des sources et contrôle éditorial avant distribution. AP formalise l'exigence de rapidité, exactitude, honnêteté, équilibre et impartialité [FCT-004; FCT-008; FCT-012].

Pour AFP, ce dispositif éthique est complété par un statut légal qui interdit la prise en compte d'influences compromettant l'exactitude ou l'objectivité et le contrôle de droit ou de fait par un groupement idéologique, politique ou économique. Ce statut est un garde institutionnel. Il ne prouve pas l'absence absolue d'erreur ou de biais dans chaque production [FCT-009].

La sélection, la hiérarchisation, le choix des sources, la vérification et le cadrage sont donc des opérations éditoriales réelles. Elles constituent la première arête du mécanisme d'agenda, même lorsque les normes professionnelles visent l'impartialité.

## Reprise aval et dépendance

L'étude de Boumans et al. portant sur 119 452 éléments d'agence et 247 161 articles de grands médias néerlandais sur une année conclut que le contenu d'agence peut représenter jusqu'à 75 % des articles en ligne et qu'une part importante est reprise quasiment verbatim. Cela ferme l'arête dépêche vers article aval dans au moins un marché européen et montre que la sélection amont peut survivre avec peu de transformation [FCT-013].

Le pouvoir n'est cependant ni uniforme ni universel. Une étude récente du marché allemand trouve que 44,8 % des articles analysés utilisent du matériel d'agence, mais que dpa représente 83,8 % du contenu d'agence identifié, contre 5,0 % pour AFP et 1,8 % pour Reuters. Une grande capacité mondiale ne se transforme donc pas automatiquement en domination nationale des trois agences étudiées [FCT-014].

Un relevé courant, daté du 4 septembre 2026, observe que 57 % de 823 sources dont la provenance a pu être vérifiée reprennent le contenu d'un tiers et que 48 % de cette reprise provient de Reuters, AFP ou AP. Ce relevé est un signal de contemporanéité utile, mais son auteur précise explicitement que l'échantillon n'est pas aléatoire, qu'il porte sur des sujets internationaux contestés sélectionnés éditorialement et que 116 sources ont été exclues faute de provenance vérifiable. Il ne peut donc pas fournir un taux général pour l'ensemble de la presse [FCT-015; FCT-016].

## Boucle de demande et diversité des cadres

Des entretiens avec des responsables d'agences, dont AP et Reuters, indiquent que les métriques d'audience et les retours clients peuvent réallouer des ressources éditoriales vers des domaines à plus forte demande. Cela documente une boucle économique et éditoriale entre consommation aval et sélection amont. Le matériau ne quantifie toutefois pas un effet causal spécifique sur le choix des sujets politiques [FCT-017].

Une étude de rédactions sur l'imagerie étrangère décrit également Reuters et AP comme des filtres de confiance pour des contenus visuels amateurs, renforçant le rôle de gatekeeper sous contrainte de temps [FCT-018].

Enfin, une analyse comparative de couvertures de la guerre Russie-Ukraine rapporte des stratégies de cadrage distinctes entre AFP, Reuters et AP. Cette source est secondaire et n'établit pas à elle seule la structure globale des cadres, mais elle suffit comme contre-épreuve à l'hypothèse simpliste d'un bloc éditorial homogène [FCT-019].

## Plafond causal

La chaîne la mieux établie est la suivante : événement ou source, sélection et vérification par l'agence, production d'une dépêche ou d'un élément visuel, distribution par flux ou outil intégré, reprise ou réécriture par une rédaction cliente. Cette chaîne donne aux agences un pouvoir d'agenda en amont parce qu'elles conditionnent une partie de ce qui est disponible rapidement pour les rédactions et parce qu'une partie de ce contenu est réutilisée avec peu de transformation.

La chaîne suivante n'est pas fermée : salience de l'agence vers salience d'un média client, puis exposition de l'audience, persuasion, comportement politique et résultat. La salience d'un événement, les choix propres des rédactions clientes, les autres agences, les correspondants internes, les plateformes et les préférences du public restent des causes concurrentes. Aucune source directe identifiée dans le périmètre ne ferme un effet AFP, Reuters ou AP sur un vote, une décision politique ou une préférence individuelle.

## Verdict

Le qualificatif le plus solide est pouvoir d'infrastructure et de gatekeeping avec capacité d'agenda intermédiatique. La dépendance aval est mesurable et parfois élevée, mais varie selon les marchés. La convergence de plusieurs médias peut résulter d'une source d'agence commune sans constituer plusieurs corroborations indépendantes. Elle ne prouve ni coordination entre agences, ni tasking politique, ni contrôle des rédactions clientes.

Le saut vers persuasion ou effet politique doit rester non établi tant qu'un design causal n'isole pas l'origine d'agence, la reprise aval, l'exposition et le comportement ou résultat final.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:7|SRC_COMPLETE:15/15

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-10
- **breaks:**
  - platformized newsroom delivery and APIs
  - growing visual/video output
  - audience analytics feedback
  - AI/content marketplace expansion
- **status:** CURRENT_FOR_SCALE_AND_DISTRIBUTION; CAUSAL_EFFECT_EVIDENCE_BOUNDED
- **window:** 2019-2026 with 2015/2018 mechanism controls

### MANIPULATION_REPORT
- **assumptions:**
  - official reach figures describe capacity not actual exposure of every item
  - copy reuse is evidence of transmission not persuasion
  - self-described ethics are governance controls not proof of perfect compliance
- **clusters:**
  - NETWORK
  - FRAMING
  - POWER
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - clients retain selection/editing autonomy
  - agency dependence varies by market
  - selection is unavoidable even under accuracy standards
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - wire syndication
  - ready-to-publish distribution
  - agency-copy dependence
  - visual gatekeeping
  - audience-demand feedback
- **priorities:**
  - measure agency scale
  - measure downstream reuse
  - retain national-market counterexample
  - separate propagation from political effect
- **query_guidance:** prefer agency official distribution data, peer-reviewed copy-tracing studies, independent counterexamples and explicit negative searches
- **rhetorical:**
  - **AUTH:** official standards are controls, not causal proof
  - **BF:** no global denominator for political influence
  - **DEM:** retain market heterogeneity
  - **FAC:** separate production, propagation and effect
  - **NUM:** use denominators and caveats
- **speaker:**
  - **goal:** forensic measurement of upstream news-agency agenda power
  - **target:** selection/distribution/reuse/effect chain
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** event
  - **S02:** source
  - **S03:** agency
  - **S04:** selection
  - **S05:** verification
  - **S06:** frame
  - **S07:** wire
  - **S08:** client
  - **S09:** reuse
  - **S10:** exposure
  - **S11:** agenda
  - **S12:** persuasion
  - **S13:** behavior
  - **S14:** policy
  - **S15:** outcome
- **threats:**
  - common sourcing=coordination
  - syndication=tasking
  - framing=falsehood
  - exposure=persuasion
  - agenda=vote effect

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - France-specific full denominator
  - **input_ids:**
    - FCT-001
    - FCT-003
    - FCT-007
    - FCT-010
    - FCT-011
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - global scale does not imply uniform market dominance
  - **not_computable:**
    - private client contracts and all downstream usage
  - **operations_applied:**
    - mapped agency scale
    - mapped feed/API/client distribution
  - **reason:** map upstream producers and downstream client channels
  - **result_ids:**
    - CLM-001
    - CLM-002
  - **status:** DONE
  - **trigger:** global agency-to-client distribution networks
- **item 2:**
  - **gaps:**
    - matched French wire-to-outlet content corpus
  - **input_ids:**
    - FCT-004
    - FCT-008
    - FCT-012
    - FCT-013
    - FCT-019
  - **module:** clusters/FRAMING.md
  - **negative_results:**
    - single coordinated frame not established
  - **not_computable:**
    - unpublished editorial deliberations
  - **operations_applied:**
    - tested standards
    - tested reuse
    - retained framing heterogeneity
  - **reason:** separate editorial gatekeeping from falsehood or coordination
  - **result_ids:**
    - CLM-003
    - CLM-004
    - CLM-005
  - **status:** DONE
  - **trigger:** selection/framing and downstream reuse
- **item 3:**
  - **gaps:**
    - public-agenda and political-outcome causal designs
  - **input_ids:**
    - FCT-013
    - FCT-014
    - FCT-015
    - FCT-017
    - FCT-018
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no direct causal political-effect source found
  - **not_computable:**
    - counterfactual public agenda absent agency copy
  - **operations_applied:**
    - mapped propagation edge
    - retained market heterogeneity
    - searched for causal political effect
  - **reason:** bound propagation versus persuasion/outcome
  - **result_ids:**
    - CLM-006
    - CLM-007
    - CAU-003
    - CAU-004
  - **status:** DONE
  - **trigger:** agenda-setting and possible political effect

### SCOPING_REPORT
- **exclusions:**
  - political coordination without tasking evidence
  - persuasion from exposure alone
  - vote effects from agenda salience alone
- **geo:** France and European information space; global evidence only when it discriminates mechanism
- **object_coverage:** HIGH_FOR_DISTRIBUTION_AND_REUSE; MODERATE_FOR_SELECTION_AND_FRAMING; LOW_FOR_PUBLIC_OR_POLITICAL_CAUSAL_EFFECT
- **object_question:** How do agencies transform events/sources into widely reused wires, and what agenda effects are demonstrable without conflating centrality, coordination, framing, persuasion and political effect?
- **period:** mainly 2019-2026 with older causal/production studies as mechanism controls
- **subject:** AFP, Reuters and AP as upstream news agencies

### CREDO
- common sourcing != coordination
- syndication != tasking
- framing != falsehood
- exposure != persuasion
- agenda effect != vote effect
- distribution centrality != editorial control of clients

### COGNITIVE_MAP
- **continuum:**
  - event/source
  - agency selection
  - verification/framing
  - wire package
  - client selection/editing
  - syndication/reuse
  - audience exposure
  - public agenda
  - political behavior/outcome
- **core_model:** Agency power is upstream infrastructural gatekeeping: selection, verification, packaging and rapid distribution can propagate topic salience and framing into many downstream outlets; the strength of this mechanism depends on client reliance and national market structure.
- **rival_models:**
  - big three directly control downstream media
  - wire services are neutral pipes with no agenda power
  - all three agencies form one coordinated editorial bloc
  - centrality alone causes persuasion or votes

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** National markets and client newsrooms retain alternative sources and editing autonomy; Germany shows a domestic agency can dominate instead.
  - **support:**
    - FCT-013
    - FCT-014
    - FCT-019
  - **synthesis:** They possess strong upstream agenda capacity, not universal downstream control.
  - **thesis:** The big three control what the public sees.
- **item 2:**
  - **antithesis:** Selection, verification, packaging, alerts and ready distribution are editorial gates, and empirical studies show large downstream reuse.
  - **support:**
    - FCT-003
    - FCT-004
    - FCT-008
    - FCT-013
  - **synthesis:** Professional neutrality norms can coexist with structural gatekeeping power.
  - **thesis:** Wire agencies are neutral pipes and therefore have no agenda power.
- **item 3:**
  - **antithesis:** No common tasking source was found; agencies have separate governance/standards and comparative content work reports framing differences.
  - **support:**
    - FCT-004
    - FCT-008
    - FCT-009
    - FCT-012
    - FCT-019
  - **synthesis:** Common sourcing can generate convergence without proving coordination.
  - **thesis:** Shared Western wire dependence proves coordinated political framing.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **from:** Reuters
  - **resource:** high-volume text/photo/video plus API/feed distribution
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
  - **to:** media/technology/government/corporate customers
- **item 2:**
  - **from:** AFP
  - **resource:** daily text/photo/video feeds
  - **support:**
    - FCT-005
    - FCT-006
    - FCT-007
  - **to:** thousands of global media clients
- **item 3:**
  - **from:** AP
  - **resource:** daily multi-format journalism and newsroom workflow systems
  - **support:**
    - FCT-010
    - FCT-011
  - **to:** customers in 126 countries / 800+ workflow newsrooms

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** AFP/Reuters/AP newsrooms
  - **relation:** select, verify and package news
  - **support:**
    - FCT-004
    - FCT-008
    - FCT-012
  - **to:** wire products
- **item 2:**
  - **from:** wire products
  - **relation:** API/feed/marketplace/customer distribution
  - **support:**
    - FCT-003
    - FCT-007
    - FCT-010
    - FCT-011
  - **to:** client newsrooms/platforms
- **item 3:**
  - **from:** client newsrooms
  - **relation:** select/edit/reuse or publish agency material
  - **support:**
    - FCT-013
    - FCT-014
    - FCT-015
    - FCT-018
  - **to:** downstream public news agenda

### IMPACT_MAP
- **established:**
  - large upstream production/distribution capacity
  - substantial agency-copy reuse in empirical media samples
  - verbatim or lightly edited online reuse
  - upstream visual gatekeeping
  - market-specific agency concentration
- **not_established:**
  - common political tasking across AFP/Reuters/AP
  - uniform dominance across European national markets
  - persuasion attributable to wire exposure
  - electoral or policy outcome caused by agency agenda setting
- **partial:**
  - topic/framing propagation into downstream coverage
  - audience-demand feedback into resource allocation

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** German sample was dominated by dpa, with low Reuters/AFP shares
  - **issue:** global reach versus national dependence
  - **pro:** Reuters/AFP/AP each operate large global networks and customer infrastructures
  - **resolution:** GLOBAL_CAPACITY_VERIFIED; UNIFORM_NATIONAL_DOMINANCE_REFUTED
  - **support:**
    - FCT-001
    - FCT-005
    - FCT-010
    - FCT-014
- **item 2:**
  - **contra:** clients choose, edit and combine material; agencies have separate standards and heterogeneous frames
  - **issue:** reuse versus editorial control
  - **pro:** Dutch and current samples show extensive wire reuse
  - **resolution:** PROPAGATION_POWER_SUPPORTED; CLIENT_CONTROL_NOT_ESTABLISHED
  - **support:**
    - FCT-013
    - FCT-015
    - FCT-019
- **item 3:**
  - **contra:** no direct causal source found connecting AFP/Reuters/AP wire exposure to voting or policy outcomes
  - **issue:** agenda capacity versus political effect
  - **pro:** high-volume distribution and reuse can affect what enters downstream coverage
  - **resolution:** UPSTREAM_AGENDA_EDGE_SUPPORTED; POLITICAL_EFFECT_UNRESOLVED
  - **support:**
    - FCT-003
    - FCT-013
    - FCT-015

### VERIFICATION_REPORT
- **downgraded:**
  - global big-three dominance
  - coordination across AFP/Reuters/AP
  - persuasion/electoral effect from syndication
- **fact_count:** 19
- **negative_controls:**
  - German market dpa dominance
  - current non-random sample limitation
  - agency-specific framing heterogeneity
  - editorial independence/accuracy rules
- **provenance_families:** 8
- **query_count:** 18
- **source_count:** 15
- **verification:** 19 bounded facts linked to 15 source records spanning official agency disclosures, French law, peer-reviewed/academic work and explicit current-sample limitations.

### EDI_REPORT
- **corpus:**
  - **limits:**
    - few France-specific full-denominator studies
    - current 2026 provenance sample is non-random
    - no causal public-agenda-to-vote design specific to AFP/Reuters/AP
  - **strength:** strong official scale/distribution records plus empirical copy-reuse studies
- **decisive_claim_coverage:**
  - CLM-001
  - CLM-002
  - CLM-003
  - CLM-004
  - CLM-005
  - CLM-006
  - CLM-007
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** official agency + French law + academic + independent current sample
  - **perspective:** Reuters/AFP/AP plus downstream market studies
  - **stratification:** production/distribution/reuse/framing/effect
  - **temporal:** 2015-2026
- **edi:**
  - **coverage:** HIGH_FOR_INFRASTRUCTURE_AND_REUSE; MODERATE_FOR_FRAMING; LOW_FOR_POLITICAL_CAUSALITY
  - **independence:** STRONG_FOR_MECHANISM; MIXED_FOR_CURRENT_SCALE_BECAUSE_AGENCY_SELF_REPORTS
- **source_counts:**
  - **A:** 3
  - **B:** 3
  - **C:** 2
  - **D:** 3
  - **E:** 1
  - **other:ijirss:** 1
  - **other:intelligence-bulletin:** 1
  - **other:risj:** 1
  - **total:** 15

### RESPONSIBILITY_MAP
- **boundary:** Agency selection and distribution create upstream agenda capacity; downstream client reuse, audience response and political effect are separate edges requiring separate evidence.
- **not_established:**
  - cross-agency command
  - client editorial control
  - public persuasion
  - vote/policy outcome causality
- **verified:**
  - global distribution infrastructure
  - editorial selection/verification
  - agency-copy reuse
  - market heterogeneity

### NEXT_QUERIES
- France-specific matched-wire corpus measuring AFP/Reuters/AP contribution to named outlets over a fixed denominator
- event-level time-series testing whether agency salience precedes downstream outlet salience after controlling for event importance
- client-editing comparison tracing one wire through multiple French/European outlets
- causal audience study separating exposure to agency-originated material from outlet brand and event salience

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-002,QRY-004,QRY-005,QRY-008 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-005,FCT-006,FCT-007,FCT-010,FCT-011 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-010,QRY-011,QRY-012 | support:- | counter:- | results:FCT-013,FCT-014,FCT-015,FCT-016 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-003,QRY-006,QRY-009,QRY-015 | support:- | counter:- | results:FCT-004,FCT-008,FCT-012,FCT-019 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-013,QRY-014,QRY-016,QRY-017,QRY-018 | support:- | counter:- | results:FCT-013,FCT-015,FCT-017,FCT-018 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,QRY-002,QRY-004,QRY-005,QRY-008,QRY-011,SRC-001,SRC-002,SRC-004,SRC-005,SRC-008,SRC-011 | support:FCT-001,FCT-002,FCT-003,FCT-005,FCT-006,FCT-007,FCT-010,FCT-011 | counter:FCT-014 | results:FCT-001,FCT-002,FCT-003,FCT-005,FCT-006,FCT-007,FCT-010,FCT-011,FCT-014 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-010,QRY-011,QRY-012,SRC-010,SRC-011,SRC-012 | support:FCT-013,FCT-015 | counter:FCT-014,FCT-016 | results:FCT-013,FCT-015,FCT-014,FCT-016 | final:PARTIAL | gap:GENERALIZATION
CLM-003 | attempts:QRY-003,QRY-006,QRY-009,QRY-014,SRC-003,SRC-006,SRC-009,SRC-014 | support:FCT-004,FCT-008,FCT-012,FCT-018 | counter:- | results:FCT-004,FCT-008,FCT-012,FCT-018 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-001,QRY-004,QRY-008,QRY-011,SRC-001,SRC-004,SRC-008,SRC-011 | support:FCT-014 | counter:FCT-001,FCT-005,FCT-010 | results:FCT-014,FCT-001,FCT-005,FCT-010 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-003,QRY-006,QRY-007,QRY-009,QRY-012,QRY-015,SRC-003,SRC-006,SRC-007,SRC-009,SRC-012,SRC-015 | support:FCT-004,FCT-008,FCT-009,FCT-012,FCT-019 | counter:FCT-015 | results:FCT-004,FCT-008,FCT-009,FCT-012,FCT-019,FCT-015 | final:PARTIAL | gap:TASKING
CLM-006 | attempts:QRY-003,QRY-006,QRY-009,QRY-013,SRC-003,SRC-006,SRC-009,SRC-013 | support:FCT-017 | counter:FCT-004,FCT-008,FCT-012 | results:FCT-017,FCT-004,FCT-008,FCT-012 | final:PARTIAL | gap:CAUSAL_ATTRIBUTION
CLM-007 | attempts:QRY-010,QRY-011,QRY-012,QRY-014,SRC-010,SRC-011,SRC-012,SRC-014 | support:FCT-013,FCT-015,FCT-018 | counter:FCT-014,FCT-016 | results:FCT-013,FCT-015,FCT-018,FCT-014,FCT-016 | final:PARTIAL | gap:COUNTERFACTUAL

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-002 | CLM | PARTIAL | GENERALIZATION | Available samples do not provide a representative France-wide 2019-2026 denominator specifically for AFP, Reuters and AP.
CLM-005 | CLM | PARTIAL | TASKING | No authenticated common editorial command/tasking record was found in the bounded search.
CLM-006 | CLM | PARTIAL | CAUSAL_ATTRIBUTION | Interview evidence does not quantify topic-level causal effects of metrics on political coverage.
CLM-007 | CLM | PARTIAL | COUNTERFACTUAL | No direct causal design was found linking exposure to agency-originated material through persuasion to a political behavior or outcome.
CAU-003 | CAU | UNRESOLVED | INTERMEDIA_CAUSALITY | Need event-level time-series or matched-content design isolating agency salience before downstream salience.
CAU-004 | CAU | UNRESOLVED | COUNTERFACTUAL | Need individual or aggregate causal exposure design linking agency-originated content to political behavior/outcome.

SEMANTIC_COUNTS_V1:LED:0|CLM:7|AXS:4|CAU:5|CTRL:8|ACT:4

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"AFP, Reuters and AP possess substantial upstream agenda capacity because each combines large newsgathering networks with high-volume, rapid distribution into customer newsroom workflows.","claimant":"INV-084 synthesis","counter":["FCT-014"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-005","FCT-006","FCT-007","FCT-010","FCT-011"]}
CLM-002 | {"claim":"Agency content can propagate directly into downstream news agendas: empirical copy-tracing finds substantial agency dependence and frequent verbatim or lightly edited reuse in online news.","claimant":"INV-084 synthesis","counter":["FCT-014","FCT-016"],"gap":"Available samples do not provide a representative France-wide 2019-2026 denominator specifically for AFP, Reuters and AP.","gap_type":"GENERALIZATION","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-013","FCT-015"]}
CLM-003 | {"claim":"News agencies are editorial gatekeepers rather than neutral pipes: their own standards describe selection, sourcing, verification, editor review and correction before distribution.","claimant":"INV-084 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-004","FCT-008","FCT-012","FCT-018"]}
CLM-004 | {"claim":"Global agency centrality does not equal uniform national-market dominance: the German sample is heavily dominated by dpa, with much smaller AFP and Reuters shares.","claimant":"INV-084 synthesis","counter":["FCT-001","FCT-005","FCT-010"],"gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-014"]}
CLM-005 | {"claim":"Common sourcing and similar downstream coverage do not establish coordination or tasking among AFP, Reuters and AP; the inspected corpus contains separate governance/standards and evidence of agency-specific framing differences.","claimant":"INV-084 synthesis","counter":["FCT-015"],"gap":"No authenticated common editorial command/tasking record was found in the bounded search.","gap_type":"TASKING","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-004","FCT-008","FCT-009","FCT-012","FCT-019"]}
CLM-006 | {"claim":"Audience and customer demand can feed back into agency resource allocation, creating an economic/editorial selection feedback loop without by itself proving political manipulation.","claimant":"INV-084 synthesis","counter":["FCT-004","FCT-008","FCT-012"],"gap":"Interview evidence does not quantify topic-level causal effects of metrics on political coverage.","gap_type":"CAUSAL_ATTRIBUTION","materiality":"MEDIUM","status":"PARTIAL","support":["FCT-017"]}
CLM-007 | {"claim":"The highest supported effect is upstream agenda propagation into downstream coverage; persuasion, voting effects and policy outcomes attributable to AFP/Reuters/AP agenda setting remain not established.","claimant":"INV-084 synthesis","counter":["FCT-014","FCT-016"],"gap":"No direct causal design was found linking exposure to agency-originated material through persuasion to a political behavior or outcome.","gap_type":"COUNTERFACTUAL","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-013","FCT-015","FCT-018"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-004","QRY-005","QRY-008"],"axis":"agency_scale_and_distribution","links":["INV-084"],"question":"What upstream production and delivery capacity do AFP, Reuters and AP document?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-005","FCT-006","FCT-007","FCT-010","FCT-011"],"sought_objects":["journalists","countries","output","clients","delivery infrastructure"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-010","QRY-011","QRY-012"],"axis":"downstream_reuse_and_dependence","links":["INV-084"],"question":"How much agency material is reused downstream, and with how much editing?","result_ids":["FCT-013","FCT-014","FCT-015","FCT-016"],"sought_objects":["agency-copy share","verbatim reuse","provider concentration"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-003","QRY-006","QRY-009","QRY-015"],"axis":"selection_verification_and_framing","links":["INV-084"],"question":"What editorial gates operate before distribution and do the agencies behave as one frame?","result_ids":["FCT-004","FCT-008","FCT-012","FCT-019"],"sought_objects":["standards","source challenge","editing","framing differences"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-013","QRY-014","QRY-016","QRY-017","QRY-018"],"axis":"agenda_to_effect_ceiling","links":["INV-084"],"question":"What can be established from wire propagation to agenda, persuasion or political effect?","result_ids":["FCT-013","FCT-015","FCT-017","FCT-018"],"sought_objects":["propagation","audience feedback","agenda effect","vote/policy effect"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"Upstream editorial gatekeeping is directly documented.","counter":"NONE_FOUND","limit":"Editorial standards document the gate and its controls but do not enumerate every unpublished selection decision.","mechanism":"event/source -> agency selection and verification -> packaged wire output","status":"SUPPORTED","support":["FCT-004","FCT-008","FCT-012"]}
CAU-002 | {"causal_right":"Distribution and reuse transmission edge is empirically supported.","counter":["FCT-014","FCT-016"],"limit":"Magnitude varies across markets; no France-wide full denominator specific to the big three is available in this run.","mechanism":"agency wire -> feed/API/client workflow -> downstream article reuse","status":"SUPPORTED","support":["FCT-003","FCT-007","FCT-011","FCT-013","FCT-015"]}
CAU-003 | {"counter":["FCT-014"],"gap":"Need event-level time-series or matched-content design isolating agency salience before downstream salience.","gap_type":"INTERMEDIA_CAUSALITY","limit":"Copy reuse and upstream filtering support propagation capacity, but event importance and client editing confound exact marginal agenda contribution.","mechanism":"agency topic salience/framing -> downstream media agenda salience/framing","status":"UNRESOLVED","support":["FCT-013","FCT-018","FCT-019"]}
CAU-004 | {"counter":["FCT-014","FCT-016"],"gap":"Need individual or aggregate causal exposure design linking agency-originated content to political behavior/outcome.","gap_type":"COUNTERFACTUAL","limit":"No direct causal design specific to AFP/Reuters/AP wire exposure was found; exposure and agenda salience are not persuasion or vote effects.","mechanism":"agency-originated downstream exposure -> audience persuasion -> vote or policy outcome","status":"UNRESOLVED","support":["FCT-015"]}
CAU-005 | {"causal_right":"Coordination inference is not supported by common sourcing alone.","counter":["FCT-004","FCT-008","FCT-009","FCT-012","FCT-019"],"limit":"Shared professional routines or common event salience can generate convergence without tasking.","mechanism":"shared AFP/Reuters/AP sourcing -> coordinated common political agenda command","status":"REFUTED","support":["FCT-015"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Global reach or production volume is capacity evidence, not proof that every item reaches or influences a given audience.","status":"DONE","support":["FCT-001","FCT-005","FCT-010"]}
CTRL-002 | {"control":"Syndication or verbatim reuse establishes content transmission, not client tasking or political coordination.","status":"DONE","support":["FCT-013","FCT-015"]}
CTRL-003 | {"control":"National agency dependence varies materially; German dpa dominance blocks a universal big-three market-share claim.","status":"DONE","support":["FCT-014"]}
CTRL-004 | {"control":"The current 2026 provenance snapshot is explicitly non-random and cannot be generalized to all journalism.","status":"DONE","support":["FCT-016"]}
CTRL-005 | {"control":"Agency editorial standards and statutory safeguards are governance controls, not evidence that errors or bias never occur.","status":"DONE","support":["FCT-004","FCT-008","FCT-009","FCT-012"]}
CTRL-006 | {"control":"Framing differences are compatible with professional selection and do not by themselves establish falsehood or manipulation.","status":"DONE","support":["FCT-019"]}
CTRL-007 | {"control":"Audience metrics can influence resource allocation without proving politically motivated topic selection.","status":"DONE","support":["FCT-017"]}
CTRL-008 | {"control":"Agenda propagation must remain separate from persuasion, vote choice and policy outcome.","status":"DONE","support":["FCT-013","FCT-015","FCT-018"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"RECHECK with a fixed-denominator French corpus matching agency wires to named downstream outlets.","actor":"future INV-084 update","intent":"quantify France-specific dependence and reuse","status":"DEFERRED","support":["FCT-013","FCT-014"]}
ACT-002 | {"action":"RECHECK with event-level temporal designs testing agency salience before downstream salience while controlling event importance.","actor":"future adjacent research","intent":"close intermedia agenda causal edge","status":"DEFERRED","support":["FCT-013","FCT-018"]}
ACT-003 | {"action":"Do not infer cross-agency coordination without authenticated tasking or common-command evidence.","actor":"routing/control plane","intent":"prevent common-sourcing-to-coordination error","status":"DONE","support":["FCT-004","FCT-008","FCT-012","FCT-019"]}
ACT-004 | {"action":"Do not claim persuasion or electoral/policy effect absent a causal exposure design.","actor":"routing/control plane","intent":"preserve causal ceiling","status":"DONE","support":["FCT-013","FCT-015","FCT-016"]}

SEARCH_ACTIVITY_V1:WEB:3|FETCH:15|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL | mnemo | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://reutersagency.com/about/ | FETCH REUTERS-ABOUT-CURRENT
QRY-002 | FETCH | FOUND | SRC-002 | https://reutersagency.com/content-delivery-platforms/reuters-connect/ | FETCH REUTERS-CONNECT-CURRENT
QRY-003 | FETCH | FOUND | SRC-003 | https://reutersagency.com/about/standards-values/ | FETCH REUTERS-STANDARDS-CURRENT
QRY-004 | FETCH | FOUND | SRC-004 | https://www.afp.com/sites/default/files/2025-09/AFP-annual-report-2024-EN.pdf | FETCH AFP-ANNUAL-2024-EN
QRY-005 | FETCH | FOUND | SRC-005 | https://factuel.afp.com/propos | FETCH AFP-FACTUEL-ABOUT-CURRENT
QRY-006 | FETCH | FOUND | SRC-006 | https://www.afp.com/sites/default/files/afp_ethic_march_2024.pdf | FETCH AFP-ETHICS-2024
QRY-007 | FETCH | FOUND | SRC-007 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006451182 | FETCH LEGIFRANCE-AFP-ART2
QRY-008 | FETCH | FOUND | SRC-008 | https://www.ap.org/about/annual-report/2025-letter-from-the-chair-and-ceo/2025-ap-by-the-numbers/ | FETCH AP-ANNUAL-2025-NUMBERS
QRY-009 | FETCH | FOUND | SRC-009 | https://www.ap.org/about/news-values-and-principles/news-values-introduction/ | FETCH AP-NEWS-VALUES-CURRENT
QRY-010 | FETCH | FOUND | SRC-010 | https://research.wur.nl/en/publications/the-agency-makes-the-online-news-world-go-round-the-impact-of-new/ | FETCH BOUMANS-IJOC-2018
QRY-011 | FETCH | FOUND | SRC-011 | https://www.tandfonline.com/doi/abs/10.1080/17512786.2024.2415541 | FETCH ELEPHANTS-NEWSROOM-2024
QRY-012 | FETCH | FOUND | SRC-012 | https://theintelligencebulletin.com/research/who-writes-the-news/ | FETCH TIB-WIRE-COPY-2026-09-04
QRY-013 | FETCH | FOUND | SRC-013 | https://reutersinstitute.politics.ox.ac.uk/our-research/speed-not-everything-how-news-agencies-use-audience-metrics | FETCH RISJ-AGENCY-METRICS
QRY-014 | FETCH | FOUND | SRC-014 | https://www.tandfonline.com/doi/full/10.1080/21670811.2015.1034518 | FETCH PHOTO-TRUTH-2015
QRY-015 | FETCH | FOUND | SRC-015 | https://www.ijirss.com/index.php/ijirss/article/view/7165 | FETCH IJIRSS-AFP-REUTERS-AP-2025
QRY-016 | WEB | NO_DIRECT_SOURCE | - | - | REFUTATION AFP Reuters AP coordinated political agenda common editorial command 2019 2026 France Europe
QRY-017 | WEB | NO_DIRECT_SOURCE | - | - | REFUTATION AFP Reuters AP wire exposure causes voting behavior election result causal study 2019 2026
QRY-018 | WEB | NO_DIRECT_SOURCE | - | - | REFUTATION France 2019 2026 exact share downstream news articles attributable specifically to AFP Reuters AP full denominator

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | REUTERS-ABOUT-CURRENT | Reuters — About Us | CURRENT_UNDATED | 2026-09-10T04:01:00Z | 2,600 journalists; 165 countries; 12 languages; annual output metrics | https://reutersagency.com/about/
SRC-002 | ◈ | fam:A | REUTERS-CONNECT-CURRENT | Reuters Connect — content marketplace | CURRENT_UNDATED | 2026-09-10T04:01:00Z | Reuters plus 100+ partners; API/search; alerts; editorial calendar; usage reports | https://reutersagency.com/content-delivery-platforms/reuters-connect/
SRC-003 | ◈ | fam:A | REUTERS-STANDARDS-CURRENT | Reuters Journalistic Standards and Values | CURRENT_UNDATED | 2026-09-10T04:01:00Z | accuracy over speed; corrections; sourcing; balance; fact/opinion separation | https://reutersagency.com/about/standards-values/
SRC-004 | ◈ | fam:B | AFP-ANNUAL-2024-EN | AFP Annual Report 2024 | 2025-09 | 2026-09-10T04:01:00Z | AFP in figures: journalists, countries, locations, daily output | https://www.afp.com/sites/default/files/2025-09/AFP-annual-report-2024-EN.pdf
SRC-005 | ◈ | fam:B | AFP-FACTUEL-ABOUT-CURRENT | AFP Factuel — About AFP and funding | CURRENT_UNDATED | 2026-09-10T04:01:00Z | 2025 revenue; thousands of media clients; examples of European clients; funding structure | https://factuel.afp.com/propos
SRC-006 | ◈ | fam:B | AFP-ETHICS-2024 | AFP Editorial Standards and Best Practices | 2024-03 | 2026-09-10T04:01:00Z | verification, sourcing, editor check, corrections, independence principles | https://www.afp.com/sites/default/files/afp_ethic_march_2024.pdf
SRC-007 | ◈ | fam:E | LEGIFRANCE-AFP-ART2 | Légifrance — AFP statute Article 2 | 1957-01-10 | 2026-09-10T04:01:00Z | statutory accuracy/objectivity and no political/economic/ideological control obligations | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006451182
SRC-008 | ◈ | fam:C | AP-ANNUAL-2025-NUMBERS | Associated Press — 2025 AP by the Numbers | 2026 | 2026-09-10T04:01:00Z | 220 locations, 90 countries, customers in 126 countries, 4bn daily reach, 5,000 pieces/day | https://www.ap.org/about/annual-report/2025-letter-from-the-chair-and-ceo/2025-ap-by-the-numbers/
SRC-009 | ◈ | fam:C | AP-NEWS-VALUES-CURRENT | Associated Press — News Values Introduction | CURRENT_UNDATED | 2026-09-10T04:01:00Z | accuracy, impartiality, balanced reporting, corrections and standards | https://www.ap.org/about/news-values-and-principles/news-values-introduction/
SRC-010 | ◈ | fam:D | BOUMANS-IJOC-2018 | Boumans et al. — The Agency Makes the (Online) News World Go Round | 2018 | 2026-09-10T04:01:00Z | Dutch study n=119,452 agency copy / n=247,161 media articles; up to 75% online agency content; verbatim reuse | https://research.wur.nl/en/publications/the-agency-makes-the-online-news-world-go-round-the-impact-of-new/
SRC-011 | ◈ | fam:D | ELEPHANTS-NEWSROOM-2024 | The Elephant(s) in the Newsroom — mixed methods agency material study | 2024 | 2026-09-10T04:01:00Z | German sample: agency-material share and provider concentration; dpa/AFP/Reuters shares | https://www.tandfonline.com/doi/abs/10.1080/17512786.2024.2415541
SRC-012 | ◈ | fam:other:intelligence-bulletin | TIB-WIRE-COPY-2026-09-04 | The Intelligence Bulletin — Who actually writes the world’s news? | 2026-09-04 | 2026-09-10T04:01:00Z | 939 sources / 823 verifiable; external-copy and big-three shares; explicit non-random limitation | https://theintelligencebulletin.com/research/who-writes-the-news/
SRC-013 | ◈ | fam:other:risj | RISJ-AGENCY-METRICS | Reuters Institute — Speed is not everything | CURRENT_ARCHIVE | 2026-09-10T04:01:00Z | interviews with agency editors incl. AP and Reuters; metrics/customer feedback can shift editorial resources | https://reutersinstitute.politics.ox.ac.uk/our-research/speed-not-everything-how-news-agencies-use-audience-metrics
SRC-014 | ◈ | fam:D | PHOTO-TRUTH-2015 | The Fragility of Photo-Truth | 2015 | 2026-09-10T04:01:00Z | newsrooms rely on international agencies as upstream filters for foreign visual material | https://www.tandfonline.com/doi/full/10.1080/21670811.2015.1034518
SRC-015 | ◈ | fam:other:ijirss | IJIRSS-AFP-REUTERS-AP-2025 | Framing war in the age of algorithmic mediation | 2025 | 2026-09-10T04:01:00Z | comparative content analysis of AFP, Reuters, AP Ukraine coverage; distinct framing strategies | https://www.ijirss.com/index.php/ijirss/article/view/7165

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://reutersagency.com/about/ | A | 2026-09-10 | Reuters global footprint | Reuters states that it has 2,600 journalists in 165 countries and publishes in 12 languages. | -
FCT-002 | FACT | ✧ | https://reutersagency.com/about/ | A | 2026-09-10 | Reuters annual production scale | Reuters states that it delivers about 2 million unique news stories, 1.5 million pictures and 130,000 video stories per year. | -
FCT-003 | FACT | ✧ | https://reutersagency.com/content-delivery-platforms/reuters-connect/ | A | 2026-09-10 | Reuters distribution infrastructure | Reuters Connect provides Reuters content plus content from more than 100 partners, with fast search, API delivery, alerts, editorial calendar and usage reporting for newsroom customers. | -
FCT-004 | FACT | ✧ | https://reutersagency.com/about/standards-values/ | A | 2026-09-10 | Reuters editorial control | Reuters standards state that accuracy and balance take precedence over speed, errors are corrected transparently, named sources are generally preferred, and fact-based news is separated from labeled opinion. | -
FCT-005 | FACT | ✧ | https://www.afp.com/sites/default/files/2025-09/AFP-annual-report-2024-EN.pdf | B | 2024 | AFP global footprint | AFP reported for 2024 about 1,700 journalists, 150 countries and 260 locations, with 24/7 coverage in six languages. | -
FCT-006 | FACT | ✧ | https://www.afp.com/sites/default/files/2025-09/AFP-annual-report-2024-EN.pdf | B | 2024 | AFP production scale | AFP reported approximately 2,300 text stories, 3,000 photos and 300 videos per day in its 2024 figures. | -
FCT-007 | FACT | ✧ | https://factuel.afp.com/propos | B | 2025 | AFP customer network | AFP states that thousands of media clients worldwide subscribe to its text, multimedia, photo, video and graphics feeds; named European clients include BBC, Deutsche Welle, France Télévisions, Le Monde, Rai and The Times. | -
FCT-008 | FACT | ✧ | https://www.afp.com/sites/default/files/afp_ethic_march_2024.pdf | B | 2024-03 | AFP editorial process | AFP standards require accurate, impartial and balanced coverage, transparent sourcing, active challenge of sources, rapid transparent corrections, and editor checking before client distribution or online publication. | -
FCT-009 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006451182 | E | 1957-01-10 | AFP statutory independence | French law requires AFP not to take account of influences compromising accuracy or objectivity and not to come under de jure or de facto control of an ideological, political or economic group. | -
FCT-010 | FACT | ✧ | https://www.ap.org/about/annual-report/2025-letter-from-the-chair-and-ceo/2025-ap-by-the-numbers/ | C | 2025 | AP global distribution scale | AP reported 220 locations in 90 countries, customers in 126 countries and estimated that four billion people see AP news each day. | -
FCT-011 | FACT | ✧ | https://www.ap.org/about/annual-report/2025-letter-from-the-chair-and-ceo/2025-ap-by-the-numbers/ | C | 2025 | AP production and workflow scale | AP reported about 5,000 individual pieces of journalism per day; AP workflow software was used by over 65,000 news professionals in more than 800 newsrooms across more than 50 countries. | -
FCT-012 | FACT | ✧ | https://www.ap.org/about/news-values-and-principles/news-values-introduction/ | C | 2026-09-10 | AP editorial standards | AP says its reporting must be fast, accurate, honest, balanced and impartial; its published news-values framework makes standards and corrections part of newsroom accountability. | -
FCT-013 | FACT | ✧ | https://research.wur.nl/en/publications/the-agency-makes-the-online-news-world-go-round-the-impact-of-new/ | D | 2018 | Dutch agency-copy dependence | Boumans et al. traced 119,452 agency-copy items across 247,161 major Dutch print and online news articles for a year and found agency content responsible for up to 75% of online articles, with a large share reproduced verbatim or with little editing. | -
FCT-014 | FACT | ✧ | https://www.tandfonline.com/doi/abs/10.1080/17512786.2024.2415541 | D | 2024 | German market counterexample | A recent German mixed-methods study reported that 44.8% of analyzed articles used agency material; within identified agency content dpa accounted for 83.8%, AFP 5.0% and Reuters 1.8%, showing strong national-market variation rather than uniform big-three dominance. | -
FCT-015 | FACT | ✧ | https://theintelligencebulletin.com/research/who-writes-the-news/ | other:intelligence-bulletin | 2026-09-04 | Current contested-story wire-copy snapshot | In a non-random 2026-08-01 to 2026-09-04 sample, The Intelligence Bulletin verified provenance for 823 of 939 sources: 57% carried someone else’s copy and 48% of that external copy came from Reuters, AFP or AP. | -
FCT-016 | FACT | ✧ | https://theintelligencebulletin.com/research/who-writes-the-news/ | other:intelligence-bulletin | 2026-09-04 | Current sample limitation | The same study explicitly states that its sample is not random, excludes 116 sources whose provenance could not be established, and describes contested international stories selected by its editorial process rather than journalism as a whole. | -
FCT-017 | FACT | ✧ | https://reutersinstitute.politics.ox.ac.uk/our-research/speed-not-everything-how-news-agencies-use-audience-metrics | other:risj | 2026-09-10 | Audience-demand feedback into agency selection | A Reuters Institute fellows paper based on interviews with editors including AP and Reuters reports that audience metrics and qualitative customer feedback can shift newsroom resources toward areas of higher demand or interest. | -
FCT-018 | FACT | ✧ | https://www.tandfonline.com/doi/full/10.1080/21670811.2015.1034518 | D | 2015 | Visual gatekeeping role | A newsroom study found substantial reliance on international agencies, including Reuters and AP, as upstream filters for foreign amateur images; journalists described trust in agency verification and gatekeeping under time pressure. | -
FCT-019 | FACT | ✧ | https://www.ijirss.com/index.php/ijirss/article/view/7165 | other:ijirss | 2025 | Agency framing heterogeneity | A 2025 comparative study of AFP, Reuters and AP coverage of the Russia-Ukraine war reported distinct framing strategies across the three agencies, which is evidence against treating their output as a single homogeneous editorial frame. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-002
FCT-004 | SRC-003
FCT-005 | SRC-004
FCT-006 | SRC-004
FCT-007 | SRC-005
FCT-008 | SRC-006
FCT-009 | SRC-007
FCT-010 | SRC-008
FCT-011 | SRC-008
FCT-012 | SRC-009
FCT-013 | SRC-010
FCT-014 | SRC-011
FCT-015 | SRC-012
FCT-016 | SRC-012
FCT-017 | SRC-013
FCT-018 | SRC-014
FCT-019 | SRC-015

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
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:search
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:facts
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:causal
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:verify
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:accountability
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:finalize

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-10T04:04:50.282193+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":19,"eligible":19,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:19;attempted:0;success:0;failure:0;blocked:19} | WRITEBACK_EXECUTION_V1:[19 rows, see section]

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
