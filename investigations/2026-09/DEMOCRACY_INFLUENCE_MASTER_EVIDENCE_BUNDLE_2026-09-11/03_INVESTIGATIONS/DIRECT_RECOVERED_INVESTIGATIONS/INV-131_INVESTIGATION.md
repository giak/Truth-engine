ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260910-1932-algerie-influence-france | PARENT_RUN_ID:NONE | AS_OF:2026-09-10
INPUT_KIND:RUN_CARD | MISSION_MODE:GREENFIELD | INPUT_REF:PATH:/tmp/inv131-te/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-10_algerie-influence-france/2026-09-10_19-32_algerie-influence-france_INPUT.md | SUBJECT_SLUG:algerie-influence-france | SUBJECT_FP:sha256:3c1a8713233b23b2670a87f98efe1f876fea38a26286dd5c5c61a55111a9bb65 | INPUT_SHA256:sha256:71d8ae12faabace44c91a15607212ea2d9a5c4ba9f00de2e9af7d089e716dec5
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France, principalement 2010-2026; cas algériens séparés par mécanisme; culte et institutions religieuses, leviers consulaires/diplomatiques, renseignement/intimidation clandestine; diaspora politique seulement sur preuve primaire; effet démocratique uniquement si chaîne fermée.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/NETWORK.md,clusters/MONEY.md,clusters/TEMPORAL.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Corps analytique technique — INV-131

## Résultat central
Les mécanismes algériens observés en France ne forment pas un système unique. Trois branches sont matériellement distinctes. Premièrement, une influence institutionnelle ouverte et ancienne sur une partie de l’organisation du culte musulman est documentée par des subventions, des imams détachés, la formation et les liens avec la Grande Mosquée de Paris. Deuxièmement, la relation consulaire et diplomatique crée des leviers réciproques : contrôle des laissez-passer, visas, coopération sécuritaire et dimensionnement des réseaux diplomatiques modifient des capacités administratives françaises, mais le cas des restrictions de visas fournit un contrôle négatif important puisque le levier tenté n’a pas produit l’effet recherché. Troisièmement, les dossiers Amir Boukhors et Bercy/OFII constituent une branche clandestine beaucoup plus dure : des actes judiciaires et des éléments d’enquête relient des personnes ayant des fonctions algériennes officielles ou alléguées de renseignement à l’enlèvement d’un opposant et à l’accès à des données sur des opposants en France. Le tasking étatique final et les responsabilités pénales définitives restent toutefois ouverts.

## Plafond causal
Le corpus ne ferme pas `Algérie -> diaspora -> vote`, `financement cultuel -> décision politique`, `statut diplomatique -> ordre étatique`, ni `opération clandestine -> effet électoral français`. L’allégation d’approches d’élus municipaux par des services/consulats algériens reste un lead non certifié : le corpus public inspecté contient des déclarations parlementaires citant une note de contre-espionnage, mais pas cette pièce primaire.

## Contrôle de symétrie avec INV-130
INV-130 et INV-131 sont comparables seulement mécanisme par mécanisme. Les deux dossiers documentent des influences cultuelles/institutionnelles de pays d’origine et des branches plus dures; mais leurs véhicules, preuves, temporalités et effets ne sont pas interchangeables. Le cas algérien ajoute surtout un test utile de coercition inefficace et une chaîne judiciaire d’intimidation/renseignement visant un opposant.

## Conséquence pour la synthèse
INV-038 peut désormais comparer au moins quatre dimensions homologues : influence cultuelle ouverte, diplomatie/cooperation ordinaire, levier coercitif exercé, et action clandestine. La comparaison doit conserver séparés financement, tasking, clandestinité, accès à l’information, comportement et effet politique.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:4|EDI_DECISIVE:4|SRC_COMPLETE:13/13

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-10
- **breaks:**
  - 2016 cult-financing baseline
  - 2020 announced end of detached-imam system
  - 2021 CRPR transparency controls
  - 2024 Amir Boukhors kidnapping
  - 2025 judicial escalation and diplomatic retaliation
  - 2026 renewed bilateral dialogue and current judicial status
- **status:** CURRENT
- **window:** 2010-2026; 2016/2020 institutional cult material retained as baseline because later 2023/2024 reports explicitly reuse it

### MANIPULATION_REPORT
- **assumptions:**
  - official parliamentary records establish their own findings/declarations, not every underlying causal inference
  - ongoing judicial cases establish procedural acts and evidence reported, not final guilt
- **clusters:**
  - POWER
  - NETWORK
  - MONEY
  - TEMPORAL
- **complexity:**
  - **band:** HIGH
  - **score:** 9
- **implicit:**
  - **I01:** foreign influence can be open and legal
  - **I02:** coercive capability may fail when exercised
  - **I03:** clandestinity raises seriousness but not causal effect automatically
- **input_kind:** RUN_CARD
- **mission_mode:** GREENFIELD
- **patterns:**
  - **P01:** open institutional influence
  - **P02:** resource/personnel channel
  - **P03:** reciprocal diplomatic coercion
  - **P04:** covert intimidation/intelligence
  - **P05:** diaspora-political allegation with access gap
- **priorities:**
  - separate cult, diplomatic, consular and covert mechanisms
  - test tasking and downstream effect
  - preserve normal bilateral cooperation controls
  - create matched comparison with INV-130
  - do not promote inaccessible intelligence note
- **query_guidance:** prefer Senate/Assemblée/MEAE primary records; use Le Monde/Reuters only for current judicial/covert developments with explicit responsibility ceiling
- **rhetorical:**
  - **R01:** bilateral conflict language can inflate mechanism classification
  - **R02:** diaspora framing can erase individual autonomy
  - **R03:** criminal suspicion can be promoted prematurely to state command
- **speaker:**
  - **goal:** bounded mechanism-first Algeria influence investigation
  - **target:** actor -> resource/tasking -> action -> French target -> access/exposure/decision/effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** Algerian state/public actor
  - **S02:** French institution
  - **S03:** Grande Mosquée de Paris
  - **S04:** religious network
  - **S05:** funding
  - **S06:** detached imam
  - **S07:** consular cooperation
  - **S08:** visa lever
  - **S09:** diplomatic retaliation
  - **S10:** opponent in exile
  - **S11:** consular/diplomatic official
  - **S12:** intelligence link
  - **S13:** data access
  - **S14:** tasking/command
  - **S15:** political/democratic effect
- **threats:**
  - nationality=state link
  - cult influence=political proxy
  - diplomacy=coercion success
  - charge=conviction
  - official status=state tasking
  - allegation=proof
  - country bundle=single system

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - full bilateral decision counterfactual
  - **input_ids:**
    - FCT-009
    - FCT-010
    - FCT-011
    - FCT-012
    - FCT-018
  - **module:** clusters/POWER.md
  - **negative_results:**
    - visa pressure did not automatically improve laissez-passer/expulsion outcomes
  - **not_computable:**
    - counterfactual bilateral policy absent each lever
  - **operations_applied:**
    - mapped reciprocal leverage
    - tested effect failure and adaptation
  - **reason:** separate capacity, exercised pressure and effect
  - **result_ids:**
    - CLM-003
    - CAU-002
  - **status:** DONE
  - **trigger:** diplomatic, consular and institutional leverage
- **item 2:**
  - **gaps:**
    - underlying counter-intelligence note cited in parliamentary debate
  - **input_ids:**
    - FCT-001
    - FCT-002
    - FCT-004
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-019
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no public primary chain from Algerian service/consulate to municipal decision in inspected corpus
  - **not_computable:**
    - general political behavior of Algerian-origin population
  - **operations_applied:**
    - mapped funding/personnel/governance chain
    - tested diaspora-proxy inference
  - **reason:** separate institutional relation from political proxy/tasking
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-006
    - CAU-001
    - CAU-004
  - **status:** DONE
  - **trigger:** religious/diaspora institutions and official intermediaries
- **item 3:**
  - **gaps:**
    - current full funding denominator across affiliated mosques
  - **input_ids:**
    - FCT-001
    - FCT-003
    - FCT-004
    - FCT-007
  - **module:** clusters/MONEY.md
  - **negative_results:**
    - funding does not close political tasking
  - **not_computable:**
    - marginal effect of subsidy on political outcomes
  - **operations_applied:**
    - mapped declared subsidy
    - retained post-2021 control/decline evidence
  - **reason:** distinguish transparent financing from command/capture
  - **result_ids:**
    - CLM-001
    - CTRL-001
  - **status:** DONE
  - **trigger:** state funding and resource channels
- **item 4:**
  - **gaps:**
    - current comparable denominators for cult funding/personnel after reforms
  - **input_ids:**
    - FCT-004
    - FCT-005
    - FCT-007
    - FCT-008
    - FCT-013
    - FCT-015
    - FCT-017
  - **module:** clusters/TEMPORAL.md
  - **negative_results:**
    - 2016 architecture does not prove unchanged 2026 intensity
  - **not_computable:**
    - continuous yearly influence intensity series
  - **operations_applied:**
    - separated historical cult architecture from current covert case
    - tracked post-2021 control change
  - **reason:** prevent static inference across changing legal and bilateral conditions
  - **result_ids:**
    - CLM-001
    - CLM-004
    - CAU-003
  - **status:** DONE
  - **trigger:** 2016 baseline -> 2021 controls -> 2024-2026 covert/diplomatic developments

### SCOPING_REPORT
- **exclusions:**
  - nationality as state-link proxy
  - generic historical grievance
  - diaspora politics without primary chain
  - criminal allegation as final state attribution
- **geo:** France; Algeria only where directly causal to France-side mechanism
- **object_coverage:** HIGH for cult institutional channels; HIGH for observed bilateral leverage; MODERATE-HIGH for Amir/Bercy procedural chain; LOW for diaspora municipal tasking and downstream electoral effects
- **object_question:** Quels cas algériens en France ferment une chaîne acteur/intermédiaire/action/cible/effet et lesquels relèvent de diplomatie, coopération, culte ou diaspora ordinaires ?
- **period:** 2010-2026
- **subject:** Algerian influence mechanisms in France

### CREDO
- nationality != state link
- cooperation != control
- diaspora != relay
- funding != command
- official role != tasking
- criminal charge != conviction
- diplomatic pressure != successful coercion
- operation != electoral effect
- Algeria != Morocco

### COGNITIVE_MAP
- **continuum:**
  - resource/status
  - institution/intermediary
  - open or covert action
  - French target
  - access/data/exposure
  - institutional response
  - behavior/decision
  - counterfactual democratic effect
- **core_model:** Algerian influence in France is multi-mechanism, not a single system. The most established open channel is institutional religious influence through funding/personnel/governance; bilateral consular and diplomatic decisions create reciprocal leverage with measurable but non-monotonic effects; the Amir Boukhors/Bercy cases create a materially harder clandestine-intelligence branch with substantial procedural evidence but unresolved final state tasking.
- **rival_models:**
  - ordinary bilateral cooperation
  - institutional religious influence without political proxy
  - reciprocal bargaining/interdependence
  - localized covert operation without proven central command
  - systematic state-directed political network in diaspora

### DIALECTICAL_MAP
- **antithesis:** Many channels are transparent bilateral arrangements or reciprocal diplomacy; cult linkage, nationality, official status and political allegations do not prove tasking, coordination or electoral effect.
- **synthesis:** Influence and some coercive/clandestine mechanisms are documentable case by case, but a unitary Algerian command architecture over French diaspora/politics is not established.
- **thesis:** Algerian public or state-linked actors possess and sometimes exercise multiple channels capable of affecting French institutions, administrative options, religious organization and opponents in exile.

### RESOURCE_FLOW_MAP
- **flows:**
  - Algerian public subsidy -> Grande Mosquée de Paris -> institutional/religious capacity
  - Algerian state payroll/personnel -> detached imams -> French mosques
  - consular cooperation/withholding -> French removals/visa policy bargaining
  - diplomatic staffing decisions -> French consular capacity
  - alleged official/intelligence links -> surveillance/data/abduction chain targeting opponents
- **limits:**
  - funding != command
  - religious capacity != political proxy
  - leverage != effective coercion
  - judicial suspicion != final state responsibility

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** Algerian state/embassy
  - **relation:** funding/personnel
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-004
    - FCT-005
  - **to:** Grande Mosquée de Paris and affiliated religious structures
- **item 2:**
  - **from:** Algerian authorities
  - **relation:** consular/diplomatic decisions
  - **support:**
    - FCT-009
    - FCT-010
    - FCT-012
    - FCT-018
  - **to:** French migration/diplomatic capacity
- **item 3:**
  - **from:** persons under judicial investigation with Algerian official links
  - **relation:** alleged intelligence/intimidation operation
  - **support:**
    - FCT-013
    - FCT-014
    - FCT-015
    - FCT-016
    - FCT-017
  - **to:** Amir Boukhors / opponents in France

### IMPACT_MAP
- **established:**
  - institutional influence on parts of worship organisation
  - observable bilateral administrative/diplomatic constraint
- **not_established:**
  - general diaspora political tasking
  - persuasion of French electorate
  - causal change of French election or broad public policy
  - single coordinated Algerian influence architecture
- **partial:**
  - clandestine intimidation/intelligence chain involving official-linked suspects

### CONTRADICTION_LEDGER
- **item 1:**
  - **issue:** cult funding can be described as foreign influence while also being transparent bilateral cooperation
  - **resolution:** classify mechanism as open institutional influence; do not promote to covert interference without tasking/coercion
- **item 2:**
  - **issue:** visa restriction intended as leverage produced weaker laissez-passer/expulsion outcomes
  - **resolution:** retain as negative causal control: attempted coercion != effective coercion
- **item 3:**
  - **issue:** Amir case contains strong procedural links but no final judgment of state command
  - **resolution:** retain operation/linkage as partial and responsibility gap as unresolved
- **item 4:**
  - **issue:** parliamentary claims cite counter-intelligence note on elected officials
  - **resolution:** retain as evidence lead only because primary note is not public

### VERIFICATION_REPORT
- **facts:** 19
- **method:** fresh web fetch for every material URL; official-source priority; current judicial reporting cross-checked where possible
- **negative_checks:**
  - no public primary note for municipal-elected-official network
  - no causal electoral-effect design
  - no final judicial attribution of Algerian state command in Amir case
- **research_queries:** 9
- **sources_fetched:** 13
- **verdict:** bounded evidence sufficient for mechanism-level conclusions; causal ceiling retained

### EDI_REPORT
- **corpus:** 13 accepted sources across 5 provenance families
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim:** CLM-001
    - **families:**
      - A
  - **item 2:**
    - **claim:** CLM-003
    - **families:**
      - B
      - C
      - E
  - **item 3:**
    - **claim:** CLM-004
    - **families:**
      - D
  - **item 4:**
    - **claim:** CLM-006
    - **families:**
      - C
    - **limitation:** underlying note inaccessible
- **diagnostic_not_truth:** true
- **dimensions:**
  - official parliamentary
  - executive/diplomatic
  - legislative debate
  - judicial investigative reporting
  - international wire corroboration
- **edi:** DIVERSE_ENOUGH_FOR_MECHANISM_MAPPING_NOT_FOR_POPULATION_CAUSALITY
- **source_counts:**
  - **A:** 5
  - **B:** 2
  - **C:** 2
  - **D:** 3
  - **E:** 1

### RESPONSIBILITY_MAP
- **item 1:**
  - **actor:** Algerian state/embassy
  - **documented_action:** funding/personnel support to GMP/imams
  - **intent:** CLAIMED
  - **scope:** institutional religious influence, not political command
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
    - FCT-004
    - FCT-005
- **item 2:**
  - **actor:** Algerian authorities
  - **documented_action:** diplomatic/consular restrictions and bargaining
  - **intent:** PROVEN
  - **scope:** bilateral leverage; democratic effect not established
  - **support:**
    - FCT-012
    - FCT-018
- **item 3:**
  - **actor:** persons with Algerian consular/diplomatic/intelligence links under investigation
  - **documented_action:** alleged involvement in intimidation/intelligence operations
  - **intent:** UNKNOWN
  - **scope:** individual/criminal responsibility pending; state tasking unresolved
  - **support:**
    - FCT-013
    - FCT-014
    - FCT-015
    - FCT-016
    - FCT-017

### NEXT_QUERIES
- Obtenir, si déclassifiée/publiée, la note primaire sur approches d’élus locaux afin de tester tasking -> action -> décision.
- Suivre l’issue judiciaire définitive Amir Boukhors/Selloum/agent consulaire et le dossier Bercy-OFII.
- Construire dans INV-038 la comparaison strictement homologue Algérie/Maroc sur culte, diplomatie, coercition et clandestinité.
- Alimenter INV-147 uniquement avec des cas appariés où mécanisme, preuve, label et conséquence institutionnelle sont comparables.

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-014,QRY-015,QRY-016,QRY-017 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-006,QRY-007,QRY-008,QRY-018,QRY-019 | support:- | counter:- | results:FCT-009,FCT-010,FCT-011,FCT-012,FCT-018 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-010,QRY-011,QRY-012,QRY-013,QRY-020,QRY-021 | support:- | counter:- | results:FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-009,QRY-022 | support:- | counter:- | results:FCT-019 | final:GAP | gap:ACCESS
AXS-005 | attempts:QRY-001,QRY-005,QRY-010,QRY-011,QRY-017,QRY-020 | support:- | counter:- | results:FCT-004,FCT-006,FCT-007,FCT-013,FCT-015,FCT-017 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,SRC-001,SRC-002,SRC-003,SRC-004,SRC-005 | support:FCT-001,FCT-002,FCT-004,FCT-005,FCT-006,FCT-007 | counter:FCT-003,FCT-008 | results:FCT-001,FCT-002,FCT-004,FCT-005,FCT-006,FCT-007,FCT-003,FCT-008 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-001,QRY-005,QRY-009,SRC-001,SRC-005,SRC-009 | support:- | counter:FCT-003,FCT-008,FCT-019 | results:FCT-003,FCT-008,FCT-019 | final:REFUTED | gap:ACCESS
CLM-003 | attempts:QRY-006,QRY-007,QRY-008,QRY-013,SRC-006,SRC-007,SRC-008,SRC-013 | support:FCT-009,FCT-010,FCT-011,FCT-012,FCT-018 | counter:- | results:FCT-009,FCT-010,FCT-011,FCT-012,FCT-018 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-010,QRY-011,QRY-012,SRC-010,SRC-011,SRC-012 | support:FCT-013,FCT-015,FCT-016,FCT-017 | counter:- | results:FCT-013,FCT-015,FCT-016,FCT-017 | final:PARTIAL | gap:RESPONSIBILITY
CLM-005 | attempts:QRY-010,SRC-010 | support:FCT-014 | counter:- | results:FCT-014 | final:PARTIAL | gap:RESPONSIBILITY
CLM-006 | attempts:QRY-009,SRC-009 | support:FCT-019 | counter:- | results:FCT-019 | final:GAP | gap:ACCESS
CLM-007 | attempts:QRY-002,QRY-005,QRY-006,QRY-009,QRY-010,QRY-011,SRC-002,SRC-005,SRC-006,SRC-009,SRC-010,SRC-011 | support:FCT-004,FCT-006,FCT-013 | counter:FCT-009,FCT-010,FCT-015,FCT-019 | results:FCT-004,FCT-006,FCT-013,FCT-009,FCT-010,FCT-015,FCT-019 | final:REFUTED | gap:NONE

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
AXS-004 | AXS | GAP | ACCESS | La note de contre-espionnage citée publiquement n’est pas accessible dans le corpus; les déclarations parlementaires sont des claims secondaires.
CLM-002 | CLM | REFUTED | ACCESS | Aucune chaîne primaire publique tasking -> élu/association -> comportement politique/électoral n’est fermée dans le corpus inspecté.
CLM-004 | CLM | PARTIAL | RESPONSIBILITY | L’attribution au commandement de l’État algérien et la responsabilité pénale définitive restent non jugées.
CLM-005 | CLM | PARTIAL | RESPONSIBILITY | Le résultat judiciaire définitif et l’étendue du tasking restent ouverts.
CLM-006 | CLM | GAP | ACCESS | La note primaire citée n’est pas publique et aucune chaîne individuelle tasking -> action -> décision n’est accessible dans le corpus inspecté.
CAU-003 | CAU | UNRESOLVED | RESPONSIBILITY | Jugement définitif et preuve publique de tasking/commandement étatique requis.
CAU-004 | CAU | UNRESOLVED | ACCESS | Accès à la note primaire, cas individuels, instructions et décisions attribuables manquants.

SEMANTIC_COUNTS_V1:LED:0|CLM:7|AXS:5|CAU:5|CTRL:7|ACT:7

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"L’État algérien a exercé en France une influence institutionnelle explicite sur une partie de l’organisation du culte musulman par financement, imams détachés et relations avec la Grande Mosquée de Paris.","claimant":"INV-131","counter":["FCT-003","FCT-008"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-004","FCT-005","FCT-006","FCT-007"]}
CLM-002 | {"claim":"Cette influence cultuelle documentée suffit à établir un relais politique ou électoral de la diaspora algérienne en France.","claimant":"hypothèse forte","counter":["FCT-003","FCT-008","FCT-019"],"gap":"Aucune chaîne primaire publique tasking -> élu/association -> comportement politique/électoral n’est fermée dans le corpus inspecté.","gap_type":"ACCESS","materiality":"DECISIVE","status":"REFUTED","support":"NONE_FOUND"}
CLM-003 | {"claim":"Les instruments consulaires et diplomatiques franco-algériens constituent des leviers réciproques de contrainte, mais leur efficacité n’est pas automatique.","claimant":"INV-131","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-018"]}
CLM-004 | {"claim":"L’affaire Amir Boukhors documente une opération clandestine violente sur le sol français avec implication présumée de personnels algériens officiels ou liés aux services.","claimant":"procédure judiciaire et enquête","counter":"NONE_FOUND","gap":"L’attribution au commandement de l’État algérien et la responsabilité pénale définitive restent non jugées.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-013","FCT-015","FCT-016","FCT-017"]}
CLM-005 | {"claim":"L’affaire connexe Bercy/OFII ferme une chaîne d’accès à des données françaises sur des opposants au profit des autorités algériennes.","claimant":"enquête judiciaire rapportée","counter":"NONE_FOUND","gap":"Le résultat judiciaire définitif et l’étendue du tasking restent ouverts.","gap_type":"RESPONSIBILITY","materiality":"IMPORTANT","status":"PARTIAL","support":["FCT-014"]}
CLM-006 | {"claim":"Les services algériens ont orchestré de manière établie un réseau d’élus municipaux d’origine algérienne en France.","claimant":"allégations publiques 2026","counter":"NONE_FOUND","gap":"La note primaire citée n’est pas publique et aucune chaîne individuelle tasking -> action -> décision n’est accessible dans le corpus inspecté.","gap_type":"ACCESS","materiality":"IMPORTANT","status":"GAP","support":["FCT-019"]}
CLM-007 | {"claim":"Le cas algérien est isomorphe au cas marocain dans son ensemble.","claimant":"hypothèse de symétrie forte","counter":["FCT-009","FCT-010","FCT-015","FCT-019"],"gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"REFUTED","support":["FCT-004","FCT-006","FCT-013"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-014","QRY-015","QRY-016","QRY-017"],"axis":"RELIGIOUS_INSTITUTIONAL","links":["CLM-001","CLM-002"],"question":"Quels flux et dispositifs algériens structurent-ils réellement des institutions cultuelles françaises ?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008"],"sought_objects":["FUNDING","PERSONNEL","GOVERNANCE","TRAINING"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-006","QRY-007","QRY-008","QRY-018","QRY-019"],"axis":"CONSULAR_DIPLOMATIC_LEVERAGE","links":["CLM-003","CAU-002"],"question":"Quels leviers consulaires ou diplomatiques modifient matériellement les options françaises et avec quelle efficacité ?","result_ids":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-018"],"sought_objects":["VISA","LAISSEZ_PASSER","EXPULSION","DIPLOMATIC_STAFF"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-010","QRY-011","QRY-012","QRY-013","QRY-020","QRY-021"],"axis":"COVERT_INTIMIDATION_INTELLIGENCE","links":["CLM-004","CLM-005","CAU-003"],"question":"Quelles actions clandestines visant des opposants en France sont juridiquement et factuellement documentées, et jusqu’où remonte l’attribution ?","result_ids":["FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018"],"sought_objects":["KIDNAPPING","INTELLIGENCE","CONSULAR_AGENT","DIPLOMAT","TASKING"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-009","QRY-022"],"axis":"DIASPORA_POLITICAL_RELAY","gap":"La note de contre-espionnage citée publiquement n’est pas accessible dans le corpus; les déclarations parlementaires sont des claims secondaires.","gap_type":"ACCESS","links":["CLM-006","CAU-004"],"question":"Existe-t-il une chaîne publique primaire reliant des services/consulats algériens à des élus locaux ou à un comportement politique de diaspora en France ?","result_ids":["FCT-019"],"sought_objects":["LOCAL_ELECTED_OFFICIAL","CONSULATE","TASKING","POLITICAL_BEHAVIOR"],"status":"GAP"}
AXS-005 | {"attempt_ids":["QRY-001","QRY-005","QRY-010","QRY-011","QRY-017","QRY-020"],"axis":"SYMMETRY_WITH_MOROCCO","links":["CLM-007","CAU-005"],"question":"Quelles chaînes sont suffisamment homologues à INV-130 pour permettre une comparaison sans fusionner pays, mécanismes ou niveaux de preuve ?","result_ids":["FCT-004","FCT-006","FCT-007","FCT-013","FCT-015","FCT-017"],"sought_objects":["RELIGIOUS_CHANNEL","DIPLOMATIC_LEVERAGE","COVERT_ACTION","EFFECT"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"ressources/personnel publics algériens -> capacité institutionnelle et influence sur certains dispositifs cultuels français","counter":["FCT-003","FCT-008"],"limit":"Ferme une influence institutionnelle sur une partie du champ cultuel; ne ferme ni proxy politique, ni persuasion, ni vote, ni contrôle général des musulmans de France.","mechanism":"État algérien -> subvention/personnel/accords -> Grande Mosquée de Paris et réseau -> gouvernance/formation/désignation cultuelles en France","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-004","FCT-005","FCT-006","FCT-007"]}
CAU-002 | {"causal_right":"décisions consulaires/diplomatiques -> modification observable de capacités administratives et de coopération","counter":"La France garde ses propres choix et peut appliquer des mesures de rétorsion; certains leviers ont eu des effets contraires à ceux recherchés.","limit":"Démontre levier et interdépendance, pas une coercition unilatérale efficace ni un effet démocratique direct.","mechanism":"contrôle/coopération consulaire et présence diplomatique -> capacité administrative française -> visas/éloignements/dialogue -> politique bilatérale","status":"SUPPORTED","support":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-018"]}
CAU-003 | {"counter":"Procédures pénales non définitivement jugées; présence ou statut officiel ne prouve pas à lui seul un ordre étatique central.","gap":"Jugement définitif et preuve publique de tasking/commandement étatique requis.","gap_type":"RESPONSIBILITY","limit":"L’opération et plusieurs liens officiels présumés sont fortement documentés; le tasking étatique final, la chaîne de commandement et l’effet comportemental sur la cible ou le débat français restent ouverts.","mechanism":"acteur lié à des structures algériennes -> repérage/intermédiaires -> enlèvement/intimidation d’un opposant en France -> effet sur expression/comportement politique","status":"UNRESOLVED","support":["FCT-013","FCT-014","FCT-015","FCT-016","FCT-017"]}
CAU-004 | {"counter":"Le seul élément public inspecté est une déclaration parlementaire relayant une note non publiée.","gap":"Accès à la note primaire, cas individuels, instructions et décisions attribuables manquants.","gap_type":"ACCESS","limit":"Aucune causalité ou chaîne individuelle ne peut être certifiée depuis le corpus public inspecté.","mechanism":"services/consulats algériens -> élus locaux d’origine algérienne -> pression/tasking -> décision municipale ou comportement électoral","status":"UNRESOLVED","support":["FCT-019"]}
CAU-005 | {"causal_right":"propriétés du mécanisme et niveau de preuve -> comparabilité analytique, non nationalité seule","counter":"Les instruments et intensités ne sont pas uniformes; certains canaux sont ouverts/bilatéraux, d’autres clandestins ou judiciaires.","limit":"La comparaison est valide seulement mécanisme par mécanisme, pas pays contre pays en bloc.","mechanism":"comparaison Algérie/Maroc -> mêmes catégories de mécanismes -> labels/niveaux de preuve -> qualification influence/ingérence","status":"SUPPORTED","support":["FCT-004","FCT-006","FCT-013","FCT-015"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"financement cultuel transparent != tasking politique","status":"PASS","support":["FCT-003","FCT-004"]}
CTRL-002 | {"control":"imams détachés/formation != relais électoral de diaspora","status":"PASS","support":["FCT-005","FCT-008","FCT-019"]}
CTRL-003 | {"control":"levier diplomatique/visa != effet coercitif réussi","status":"PASS","support":["FCT-009","FCT-010"]}
CTRL-004 | {"control":"mise en examen/mandat != condamnation définitive ni ordre étatique prouvé","status":"PASS","support":["FCT-013","FCT-015","FCT-016","FCT-017"]}
CTRL-005 | {"control":"représailles diplomatiques != preuve de culpabilité dans le dossier pénal","status":"PASS","support":["FCT-018"]}
CTRL-006 | {"control":"déclaration parlementaire citant une note non publique != pièce primaire vérifiée","status":"PASS","support":["FCT-019"]}
CTRL-007 | {"control":"Algérie != Maroc; seuls les mécanismes homologues peuvent être comparés","status":"PASS","support":["FCT-006","FCT-007","FCT-013","FCT-015"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Financement déclaré de la Grande Mosquée de Paris","actor":"État/ambassade d’Algérie","intent":"CLAIMED","status":"DONE","support":["FCT-001","FCT-003","FCT-004"]}
ACT-002 | {"action":"Détachement et rémunération d’imams en France","actor":"État algérien / Grande Mosquée de Paris","intent":"PROVEN","status":"DONE","support":["FCT-002","FCT-005"]}
ACT-003 | {"action":"Mesures d’entrave sur financements/activité liés à la Grande Mosquée de Paris","actor":"Tracfin / autorités françaises","intent":"PROVEN","status":"DONE","support":["FCT-007"]}
ACT-004 | {"action":"Usage français du levier visas en réaction à la coopération consulaire","actor":"État français","intent":"PROVEN","status":"DONE","support":["FCT-009","FCT-010"]}
ACT-005 | {"action":"Restriction algérienne du dispositif diplomatique français avec effet sur capacité visa","actor":"Autorités algériennes","intent":"PROVEN","status":"DONE","support":["FCT-012","FCT-018"]}
ACT-006 | {"action":"Enlèvement et séquestration d’Amir Boukhors","actor":"auteurs mis en cause; liens algériens sous enquête","intent":"UNKNOWN","status":"DONE","support":["FCT-013","FCT-015","FCT-016","FCT-017"]}
ACT-007 | {"action":"Transmission présumée de données sur opposants","actor":"fonctionnaire de Bercy / destinataire algérien sous enquête","intent":"UNKNOWN","status":"DONE","support":["FCT-014"]}

SEARCH_ACTIVITY_V1:WEB:9|FETCH:13|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | UNAVAILABLE | mnemolite | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.senat.fr/compte-rendu-commissions/20160530/mi_islam.html | fresh fetch for material source
QRY-002 | FETCH | FOUND | SRC-002 | https://www.senat.fr/rap/r15-757/r15-7579.html | fresh fetch for material source
QRY-003 | FETCH | FOUND | SRC-003 | https://www.senat.fr/rap/r19-595-1/r19-595-19.html | fresh fetch for material source
QRY-004 | FETCH | FOUND | SRC-004 | https://www.senat.fr/rap/r22-810/r22-810_mono.html | fresh fetch for material source
QRY-005 | FETCH | FOUND | SRC-005 | https://www.senat.fr/rap/r23-739-1/r23-739-18.html | fresh fetch for material source
QRY-006 | FETCH | FOUND | SRC-006 | https://www.diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/audition-de-jean-noel-barrot-devant-la-commission-des-affaires-etrangeres-de-l-assemblee-nationale | fresh fetch for material source
QRY-007 | FETCH | FOUND | SRC-007 | https://www.diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/relations-avec-l-algerie-reponse-de-jean-noel-barrot-ministre-de-l-europe-et-des-affaires-etrangeres | fresh fetch for material source
QRY-008 | FETCH | FOUND | SRC-008 | https://questions.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-extraordinaire-de-2025-2026/premiere-seance-du-mardi-21-juillet-2026 | fresh fetch for material source
QRY-009 | FETCH | FOUND | SRC-009 | https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2025-2026/troisieme-seance-du-mardi-24-mars-2026 | fresh fetch for material source
QRY-010 | FETCH | FOUND | SRC-010 | https://www.lemonde.fr/societe/article/2025/04/12/apres-l-enlevement-de-l-opposant-algerien-amir-boukhors-en-france-une-information-judiciaire-ouverte_6594611_3224.html | fresh fetch for material source
QRY-011 | FETCH | FOUND | SRC-011 | https://www.lemonde.fr/afrique/article/2025/08/09/la-justice-francaise-emet-un-mandat-d-arret-international-contre-un-diplomate-algerien_6627604_3212.html | fresh fetch for material source
QRY-012 | FETCH | FOUND | SRC-012 | https://www.lemonde.fr/afrique/article/2026/07/09/la-justice-confirme-le-maintien-en-detention-d-un-agent-consulaire-algerien-soupconne-d-etre-implique-dans-l-enlevement-de-l-influenceur-amir-dz_6722134_3212.html | fresh fetch for material source
QRY-013 | FETCH | FOUND | SRC-013 | https://www.reuters.com/world/france-says-algeria-threatening-expel-diplomatic-staff-2025-04-14/ | fresh fetch for material source
QRY-014 | WEB | FOUND | - | - | Algérie Grande Mosquée de Paris financement imams détachés influence France
QRY-015 | WEB | FOUND | - | - | Algérie imams France accord bilatéral 120 Sénat
QRY-016 | WEB | FOUND | - | - | DPR 2023 activité algérienne Grande Mosquée de Paris Tracfin
QRY-017 | WEB | FOUND | - | - | Sénat 2024 influences étrangères Algérie diaspora culte
QRY-018 | WEB | FOUND | - | - | Algérie visas laissez-passer 2021 effet expulsions France 2026
QRY-019 | WEB | FOUND | - | - | Algérie coopération sécuritaire migratoire France 2026 résultats
QRY-020 | WEB | FOUND | - | - | Amir Boukhors enlèvement France agent consulaire algérien PNAT
QRY-021 | WEB | FOUND | - | - | mandat arrêt diplomate algérien Amir DZ DGSI 2025
QRY-022 | WEB | FOUND | - | - | Algérie élus municipaux diaspora note contre espionnage France 2026

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | SENAT-MI-ISLAM-2016-05-30 | MI organisation, place et financement de l'Islam en France - audition de l'ambassadeur d'Algérie | 2016-05-30 | 2026-09-10T17:32:00+00:00 | Audition Amar Bendjama; financement GMP et imams | https://www.senat.fr/compte-rendu-commissions/20160530/mi_islam.html
SRC-002 | ◈ | fam:A | SENAT-R15-757 | De l'Islam en France à un Islam de France - financement par l'Algérie | 2016-07-05 | 2026-09-10T17:32:00+00:00 | Rapport 757; financement algérien et Grande Mosquée de Paris | https://www.senat.fr/rap/r15-757/r15-7579.html
SRC-003 | ◈ | fam:A | SENAT-R19-595 | Radicalisation islamiste : faire face et lutter ensemble - imams détachés | 2020-07-07 | 2026-09-10T17:32:00+00:00 | Rapport 595; 120 imams algériens détachés et accords bilatéraux | https://www.senat.fr/rap/r19-595-1/r19-595-19.html
SRC-004 | ◈ | fam:A | SENAT-DPR-2023 | Rapport de la délégation parlementaire au renseignement 2022-2023 | 2023-06-29 | 2026-09-10T17:32:00+00:00 | DPR; Tracfin et activité algérienne/marocaine liée à la GMP | https://www.senat.fr/rap/r22-810/r22-810_mono.html
SRC-005 | ◈ | fam:A | SENAT-R23-739 | Lutte contre les influences étrangères malveillantes - rapport 739 | 2024-07-23 | 2026-09-10T17:32:00+00:00 | Commission enquête; leviers cultuels et absence de nouveaux éléments | https://www.senat.fr/rap/r23-739-1/r23-739-18.html
SRC-006 | ◈ | fam:B | MEAE-BARROT-2026-06-04 | Audition de Jean-Noël Barrot devant la commission des Affaires étrangères | 2026-06-04 | 2026-09-10T17:32:00+00:00 | Visas, laissez-passer, coopération franco-algérienne | https://www.diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/audition-de-jean-noel-barrot-devant-la-commission-des-affaires-etrangeres-de-l-assemblee-nationale
SRC-007 | ◈ | fam:B | MEAE-ALGERIE-2026-04-28 | Relations avec l’Algérie - réponse de Jean-Noël Barrot | 2026-04-28 | 2026-09-10T17:32:00+00:00 | Reprise coopération migratoire et sécuritaire | https://www.diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/relations-avec-l-algerie-reponse-de-jean-noel-barrot-ministre-de-l-europe-et-des-affaires-etrangeres
SRC-008 | ◈ | fam:C | AN-2026-07-21 | Première séance du mardi 21 juillet 2026 - visas algériens | 2026-07-21 | 2026-09-10T17:32:00+00:00 | Question au gouvernement; visas et réseau diplomatique | https://questions.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-extraordinaire-de-2025-2026/premiere-seance-du-mardi-21-juillet-2026
SRC-009 | ◈ | fam:C | AN-2026-03-24 | Débat sur les ingérences étrangères du 24 mars 2026 | 2026-03-24 | 2026-09-10T17:32:00+00:00 | Débat parlementaire; allégation sur élus d’origine algérienne et note non publique | https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2025-2026/troisieme-seance-du-mardi-24-mars-2026
SRC-010 | ◉ | fam:D | LEMONDE-AMIR-2025-04-12 | Après l’enlèvement d’Amir Boukhors, information judiciaire et mises en examen | 2025-04-12 | 2026-09-10T17:32:00+00:00 | Enlèvement, mises en examen, Bercy/OFII, consulat | https://www.lemonde.fr/societe/article/2025/04/12/apres-l-enlevement-de-l-opposant-algerien-amir-boukhors-en-france-une-information-judiciaire-ouverte_6594611_3224.html
SRC-011 | ◉ | fam:D | LEMONDE-AMIR-2025-08-09 | Mandat d’arrêt international contre un ancien diplomate algérien | 2025-08-09 | 2026-09-10T17:32:00+00:00 | Mandat contre Salaheddine Selloum; présomptions et éléments DGSI | https://www.lemonde.fr/afrique/article/2025/08/09/la-justice-francaise-emet-un-mandat-d-arret-international-contre-un-diplomate-algerien_6627604_3212.html
SRC-012 | ◉ | fam:D | LEMONDE-AMIR-2026-07-09 | Maintien en détention d’un agent consulaire algérien dans l’affaire Amir DZ | 2026-07-09 | 2026-09-10T17:32:00+00:00 | Cour d’appel; agent consulaire suspecté | https://www.lemonde.fr/afrique/article/2026/07/09/la-justice-confirme-le-maintien-en-detention-d-un-agent-consulaire-algerien-soupconne-d-etre-implique-dans-l-enlevement-de-l-influenceur-amir-dz_6722134_3212.html
SRC-013 | ◉ | fam:E | REUTERS-2025-04-14-ALG | France says Algeria threatening to expel diplomatic staff | 2025-04-14 | 2026-09-10T17:32:00+00:00 | Réaction diplomatique après détention agent consulaire | https://www.reuters.com/world/france-says-algeria-threatening-expel-diplomatic-staff-2025-04-14/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.senat.fr/compte-rendu-commissions/20160530/mi_islam.html | A | 2016-05-30 | ALG_GMP_ANNUAL_SUBSIDY | L’ambassadeur d’Algérie a déclaré au Sénat une subvention annuelle à la Grande Mosquée de Paris d’environ 2 millions d’euros depuis plusieurs années. | -
FCT-002 | FACT | ✧ | https://www.senat.fr/compte-rendu-commissions/20160530/mi_islam.html | A | 2016-05-30 | ALG_IMAMS_EMBASSY_PAY | L’ambassadeur d’Algérie a déclaré que les imams fonctionnaires algériens affectés en France étaient répartis par la Grande Mosquée de Paris et rémunérés par l’ambassade. | -
FCT-003 | FACT | ✧ | https://www.senat.fr/compte-rendu-commissions/20160530/mi_islam.html | A | 2016-05-30 | ALG_FINANCING_TRANSPARENT_BILATERAL | Le financement déclaré de l’Algérie vers la Grande Mosquée et des lieux de culte passait, selon l’ambassadeur, par des circuits bancaires classiques et un cadre coordonné avec les autorités françaises. | -
FCT-004 | FACT | ✧ | https://www.senat.fr/rap/r15-757/r15-7579.html | A | 2016-07-05 | ALG_GMP_NETWORK_FINANCING | Le rapport sénatorial de 2016 décrit un financement algérien indirect des associations et lieux de culte via une subvention globale à la Grande Mosquée de Paris, qui en redistribue une partie à son réseau affilié. | -
FCT-005 | FACT | ✧ | https://www.senat.fr/rap/r19-595-1/r19-595-19.html | A | 2020-07-07 | ALG_DETACHED_IMAMS_2020 | Le Sénat recensait en 2020 120 imams détachés par l’Algérie en France parmi 290 imams détachés, dans le cadre d’accords bilatéraux. | -
FCT-006 | FACT | ✧ | https://www.senat.fr/rap/r23-739-1/r23-739-18.html | A | 2024-07-23 | ALG_CULT_INFLUENCE_LEVERS | Le rapport sénatorial de 2024 reprend six leviers d’influence des pays d’origine, dont l’Algérie, sur l’organisation du culte musulman en France : mosquées, fédérations, gouvernance, halal, formation et désignation des imams. | -
FCT-007 | FACT | ✧ | https://www.senat.fr/rap/r22-810/r22-810_mono.html | A | 2023-06-29 | TRACFIN_ALG_GMP_HINDRANCE | La DPR 2022-2023 indique que Tracfin a pris des mesures d’entrave de l’activité marocaine et algérienne en lien avec la Grande Mosquée de Paris et observe un recul des financements cultuels étrangers depuis la loi de 2021. | -
FCT-008 | FACT | ✧ | https://www.senat.fr/rap/r23-739-1/r23-739-18.html | A | 2024-07-23 | ALG_2024_NO_NEW_ELEMENTS | La commission d’enquête sénatoriale de 2024 indique que ses auditions n’ont pas identifié d’éléments nouveaux sur ce volet au-delà des travaux antérieurs, tout en maintenant une vigilance sur l’instrumentalisation des communautés religieuses. | -
FCT-009 | FACT | ✧ | https://www.diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/audition-de-jean-noel-barrot-devant-la-commission-des-affaires-etrangeres-de-l-assemblee-nationale | B | 2026-06-04 | FR_VISA_LEVER_BACKFIRE | Jean-Noël Barrot a déclaré en juin 2026 que la précédente restriction générale des visas aux Algériens avait été suivie d’une baisse des laissez-passer consulaires et des expulsions, et n’avait pas produit les effets escomptés. | -
FCT-010 | FACT | ✧ | https://www.diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/audition-de-jean-noel-barrot-devant-la-commission-des-affaires-etrangeres-de-l-assemblee-nationale | B | 2026-06-04 | FR_VISA_EU_COORDINATION | Jean-Noël Barrot a déclaré qu’une politique de visas destinée à infléchir la politique algérienne devait être coordonnée à l’échelle européenne, faute de quoi des voies de contournement réduisent son effet. | -
FCT-011 | FACT | ✧ | https://www.diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/relations-avec-l-algerie-reponse-de-jean-noel-barrot-ministre-de-l-europe-et-des-affaires-etrangeres | B | 2026-04-28 | FR_ALG_SECURITY_DIALOGUE_RESUMED | Le ministre français des Affaires étrangères a indiqué en avril 2026 que la coopération migratoire et sécuritaire avec l’Algérie avait repris après environ un an de blocage et produisait de premiers résultats. | -
FCT-012 | FACT | ✧ | https://questions.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-extraordinaire-de-2025-2026/premiere-seance-du-mardi-21-juillet-2026 | C | 2026-07-21 | ALG_DIPLOMATIC_STAFF_EFFECT_ON_VISAS | En juillet 2026, Jean-Noël Barrot a indiqué que le nombre de visas délivrés aux Algériens avait baissé de 20 % en 2025, principalement en raison des restrictions imposées par Alger au réseau diplomatique français. | -
FCT-013 | FACT | ✧ | https://www.lemonde.fr/societe/article/2025/04/12/apres-l-enlevement-de-l-opposant-algerien-amir-boukhors-en-france-une-information-judiciaire-ouverte_6594611_3224.html | D | 2025-04-12 | AMIR_KIDNAPPING_JUDICIAL_CASE | Amir Boukhors, réfugié politique algérien en France, a été enlevé et séquestré pendant environ vingt-sept heures en avril 2024; une information judiciaire antiterroriste a conduit en avril 2025 à la mise en examen et détention provisoire de trois suspects. | -
FCT-014 | FACT | ✧ | https://www.lemonde.fr/societe/article/2025/04/12/apres-l-enlevement-de-l-opposant-algerien-amir-boukhors-en-france-une-information-judiciaire-ouverte_6594611_3224.html | D | 2025-04-12 | BERCY_FOREIGN_POWER_CHARGE | Dans une enquête connexe, un fonctionnaire de Bercy a été mis en examen pour intelligence avec une puissance étrangère après des soupçons de transmission d’informations sur des opposants aux autorités algériennes; une agente de l’OFII a été mise en examen pour violation du secret professionnel. | -
FCT-015 | FACT | ✧ | https://www.lemonde.fr/afrique/article/2025/08/09/la-justice-francaise-emet-un-mandat-d-arret-international-contre-un-diplomate-algerien_6627604_3212.html | D | 2025-08-09 | AMIR_DIPLOMAT_WARRANT | Un juge français a délivré le 25 juillet 2025 un mandat d’arrêt international contre l’ancien premier secrétaire de l’ambassade d’Algérie Salaheddine Selloum pour sa participation présumée à l’enlèvement d’Amir Boukhors. | -
FCT-016 | EVIDENCE | ❧ | https://www.lemonde.fr/afrique/article/2025/08/09/la-justice-francaise-emet-un-mandat-d-arret-international-contre-un-diplomate-algerien_6627604_3212.html | D | 2025-08-09 | AMIR_DGSI_ATTRIBUTION_ELEMENTS | Le Monde rapporte que, selon les investigations de la DGSI, Selloum aurait été un membre des services extérieurs algériens et que des bornages et contacts le reliaient à des phases de repérage et à des personnes associées à l’opération; ces éléments restent ceux d’une procédure non jugée définitivement. | -
FCT-017 | FACT | ✧ | https://www.lemonde.fr/afrique/article/2026/07/09/la-justice-confirme-le-maintien-en-detention-d-un-agent-consulaire-algerien-soupconne-d-etre-implique-dans-l-enlevement-de-l-influenceur-amir-dz_6722134_3212.html | D | 2026-07-09 | AMIR_CONSULAR_AGENT_DETENTION_2026 | La cour d’appel de Paris a confirmé en juillet 2026 le maintien en détention d’un agent consulaire algérien soupçonné d’implication dans l’enlèvement d’Amir Boukhors. | -
FCT-018 | FACT | ✧ | https://www.reuters.com/world/france-says-algeria-threatening-expel-diplomatic-staff-2025-04-14/ | E | 2025-04-14 | ALG_DIPLOMATIC_RETALIATION_2025 | Reuters a rapporté qu’Alger avait demandé le départ de douze agents diplomatiques français après la détention d’un agent consulaire algérien soupçonné dans l’affaire Boukhors, et que Paris avait annoncé une riposte. | -
FCT-019 | EVIDENCE | ❧ | https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2025-2026/troisieme-seance-du-mardi-24-mars-2026 | C | 2026-03-24 | ALG_LOCAL_ELECTED_OFFICIALS_ALLEGATION | Un débat parlementaire de mars 2026 relaie l’existence alléguée d’une note du contre-espionnage sur des opérations algériennes auprès d’élus municipaux d’origine algérienne; la note primaire n’est pas publique dans le corpus inspecté et cette affirmation n’est donc pas promue en fait établi. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-002
FCT-005 | SRC-003
FCT-006 | SRC-005
FCT-007 | SRC-004
FCT-008 | SRC-005
FCT-009 | SRC-006
FCT-010 | SRC-006
FCT-011 | SRC-007
FCT-012 | SRC-008
FCT-013 | SRC-010
FCT-014 | SRC-010
FCT-015 | SRC-011
FCT-016 | SRC-011
FCT-017 | SRC-012
FCT-018 | SRC-013
FCT-019 | SRC-009

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
FCT-016 | SKIP:NOT_ELIGIBLE
FCT-017 | ELIGIBLE:VERIFIE
FCT-018 | ELIGIBLE:VERIFIE
FCT-019 | SKIP:NOT_ELIGIBLE

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
FCT-017 | WRITE | -
FCT-018 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:SEARCH
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:FACTS
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:CAUSAL
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:VERIFY
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:INVESTIGATION_ACCOUNTABILITY
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-10T17:46:55.556591+00:00","fact_mem":{},"mnemo_row":"MNEMO_UNAVAILABLE — local memory service not available; no memory ids fabricated.","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":17,"eligible":17,"failure":0,"success":0}}

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
FCT-017 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-018 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
