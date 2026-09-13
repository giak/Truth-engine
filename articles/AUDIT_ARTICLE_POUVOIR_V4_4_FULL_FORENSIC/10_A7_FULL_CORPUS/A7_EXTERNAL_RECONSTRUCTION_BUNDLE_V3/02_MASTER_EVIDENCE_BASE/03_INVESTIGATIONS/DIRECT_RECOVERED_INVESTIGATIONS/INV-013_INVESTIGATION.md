ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260910-0157-active-measures-soviet-russian | PARENT_RUN_ID:NONE | AS_OF:2026-09-10
INPUT_KIND:RUN_CARD | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/inv013/runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-10_active-measures-soviet-russian/2026-09-10_01-57_active-measures-soviet-russian_INPUT.md | SUBJECT_SLUG:active-measures-soviet-russian | SUBJECT_FP:sha256:e6a0163324c00cad72fa47f7c51d1c242ce9f4d3e0a79fda77f73ac654c8a550 | INPUT_SHA256:sha256:88eb97222ac880501f414fffdc2b164ad742a7d42b7f5f0d49091234b784e207
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:URSS/Russie et cibles europeennes/occidentales, 1950-2026; cas documentables; autorite/operateur -> actif/front/media/faux document/canal -> message/action -> distribution -> exposition -> reaction/comportement -> effet; doctrine != operation; attribution != effet; diffusion != persuasion; repetition de tactique != commandement continu; activite != efficacite.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/NETWORK.md,clusters/FRAMING.md,clusters/POWER.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
## Question et résultat

L'enquête teste quatre objets séparés : le répertoire soviétique des « active measures », la continuité éventuelle de ces techniques dans les opérations russes contemporaines, la chaîne de commandement ou de tasking propre à chaque cas, et l'efficacité politique réellement mesurée. Le corpus ne soutient ni la thèse d'une rupture totale, ni celle d'un appareil unique demeuré institutionnellement inchangé depuis le KGB jusqu'aux opérations numériques actuelles.

## 1. Le répertoire soviétique est documenté, et déjà hétérogène

Les documents officiels des années 1980 décrivent un ensemble comprenant faux documents, désinformation, opérations politiques, groupes-fronts, agents d'influence et manipulation médiatique [FCT-001,FCT-003,FCT-005]. Ils fournissent également un contrôle décisif : les opérations n'atteignaient pas toujours leurs objectifs, certaines forgeries étant neutralisées par identification et exposition publiques [FCT-002,FCT-004]. « Active measures » décrit donc un portefeuille de techniques et d'organisations, pas une preuve automatique d'efficacité.

## 2. Continuité tactique, rupture organisationnelle à ne pas effacer

Les opérations russes contemporaines reprennent plusieurs structures fonctionnelles anciennes : dissimulation de la source, fausses identités, médias imités, contenus fabriqués, intermédiaires et amplification coordonnée [FCT-009,FCT-017,FCT-018,FCT-023,FCT-024,FCT-030]. Les technologies et supports changent : VPN, plateformes sociales, domaines cybersquattés, bots, vidéos mises en scène et contenu assisté par IA.

Cette ressemblance ferme une continuité de **répertoire**. Elle ne ferme pas une continuité de **commandement**. Le corpus passe du KGB/Service A aux structures IRA, SDA, Structura, ANO Dialog, administration présidentielle russe et autres opérateurs, sans pièce établissant une chaîne institutionnelle ininterrompue à travers 1991 [CLM-003]. La répétition d'une tactique n'est donc pas un substitut à la preuve de tasking.

## 3. Le tasking moderne peut cependant être très solide, cas par cas

Le dossier IRA ferme une infrastructure organisée : personnels, projet ciblant la population américaine, faux profils, infrastructure américaine et identités volées [FCT-007 à FCT-010]. Le dossier Doppelganger ferme une chaîne encore plus explicite dans les pièces américaines : administration présidentielle russe -> SDA/Structura/ANO Dialog -> domaines usurpant des médias, publicités, influenceurs et faux profils [FCT-017,FCT-018]. Treasury documente en outre la coordination d'ANO Dialog avec des responsables russes sur des comptes automatisés et la dissimulation de provenance autour de RRN [FCT-019,FCT-020].

La conclusion correcte est donc asymétrique : le grand récit de continuité institutionnelle reste partiel, mais plusieurs opérations modernes possèdent des chaînes de commandement ou de coordination suffisamment spécifiques pour dépasser la simple attribution géopolitique.

## 4. France et Europe : ciblage et distribution établis, résultat politique non mesuré

VIGINUM documente Portal Kombat comme un réseau de centaines de portails pro-russes, réorienté après l'invasion de l'Ukraine vers des pays occidentaux dont la France [FCT-021,FCT-022]. Matriochka emploie de faux contenus puis sollicite médias et fact-checkers afin qu'ils les vérifient, transformant potentiellement la procédure de vérification elle-même en vecteur de distribution [FCT-023,FCT-024]. Storm-1516 montre des reprises par RRN/Doppelganger, Portal Kombat, Mriya et des acteurs occidentaux pro-russes [FCT-025,FCT-026].

Ces éléments ferment `opération -> distribution/ciblage`. Ils ne ferment pas `distribution -> préférence -> comportement -> résultat politique français/européen`.

## 5. L'efficacité réelle est le maillon le plus faible

Deux contrôles quantitatifs empêchent l'inflation causale. Dans le témoignage Twitter de 2017, les comptes russes liés à l'élection représentent une fraction très faible de l'ensemble des comptes et des tweets électoraux vus dans la période étudiée [FCT-015,FCT-016]. L'étude longitudinale publiée en 2023 trouve une exposition fortement concentrée : 1 % des utilisateurs comptent pour 70 % des expositions, et elle ne détecte pas de relation significative substantielle avec les changements d'attitude, de polarisation ou de vote [FCT-027,FCT-028].

Cela ne prouve pas que toute opération russe est inefficace. Les campagnes contemporaines peuvent obtenir des millions de vues, tandis que d'autres contenus restent peu engagés [FCT-029]. Cela démontre surtout que **portée, persuasion et résultat sont trois objets distincts**.

## Conclusion

INV-013 ferme une thèse plus précise que « les active measures continuent » :

`répertoire soviétique documenté -> continuité tactique forte -> opérateurs modernes et tasking démontrables cas par cas -> distribution/exposition hétérogènes -> persuasion et résultat politique généralement non établis`.

La continuité la plus robuste est fonctionnelle et tactique, non la preuve d'un appareil de commandement institutionnel resté identique. Le corpus établit l'existence et parfois la sophistication des opérations russes ; il ne justifie pas de convertir leur existence en preuve générale qu'elles ont changé une élection, une opinion publique ou une politique. Pour la France et l'Union européenne, le gap prioritaire n'est plus « ces opérations existent-elles ? », mais `exposition attribuée -> réception -> comportement -> résultat`, avec dénominateurs et contrefactuel crédibles.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:7|SRC_COMPLETE:15/15

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-10
- **discontinuities:**
  - 1991 Soviet collapse breaks any presumption of organizational continuity
  - 2014-2016 IRA U.S. targeting
  - 2022-onward expansion of France/EU-facing Russian digital operations
  - 2024 U.S. disruption of Doppelganger infrastructure
- **status:** CURRENT_WITH_HISTORICAL_LAYER
- **window:** 1950-2026

### MANIPULATION_REPORT
- **assumptions:**
  - historical official reports are evidence about documented cases, not universal Soviet success
  - modern official attributions remain claims bounded by disclosed evidence
  - effect requires measurement beyond operation existence
- **clusters:**
  - NETWORK
  - FRAMING
  - POWER
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - tactical continuity can coexist with organizational rupture
  - old techniques can be technologically adapted
  - countermeasures alter realized effect
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - forgery
  - front group
  - false persona
  - spoofed media
  - coordinated amplification
  - cross-network laundering
  - staged video
  - platform targeting
- **priorities:**
  - technique continuity
  - operator/tasking specificity
  - France/EU targeting
  - exposure denominators
  - effect ceiling
- **query_guidance:** Prefer declassified primary/official records, judicial or parliamentary attribution, VIGINUM technical findings and direct exposure/effect studies; require actor-specific bridges before continuity claims.
- **rhetorical:**
  - **AUTH:** official attribution is bounded to what each document establishes
  - **BF:** case series and impression totals do not establish prevalence or effect
  - **DEM:** retain failed/neutralized operations and null-effect evidence
  - **FAC:** separate command, action, exposure, persuasion and outcome
  - **NUM:** use denominators, not raw reach alone
- **speaker:**
  - **goal:** forensic continuity-and-effect mapping
  - **target:** authority/operator -> technique/action -> distribution -> exposure -> behavior/outcome
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** authority
  - **S02:** operator
  - **S03:** tasking
  - **S04:** front
  - **S05:** forgery
  - **S06:** spoof
  - **S07:** persona
  - **S08:** media
  - **S09:** distribution
  - **S10:** exposure
  - **S11:** reach
  - **S12:** reception
  - **S13:** behavior
  - **S14:** outcome
  - **S15:** countermeasure
- **threats:**
  - doctrine=operation
  - recurring tactic=continuous command
  - attribution=effect
  - reach=persuasion
  - activity=electoral outcome
  - targeting=France effect

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - organizational bridge across 1991
  - **input_ids:**
    - FCT-003
    - FCT-007
    - FCT-017
    - FCT-019
    - FCT-021
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no unbroken KGB-to-modern-operator command chain established
  - **not_computable:**
    - undisclosed current tasking outside public record
  - **operations_applied:**
    - mapped principal/operator/intermediary edges
    - separated actor attribution from downstream amplifiers
  - **reason:** map Soviet and modern operator-intermediary-action chains while separating tactical similarity from command continuity
  - **result_ids:**
    - CLM-003
    - CLM-004
    - CAU-002
    - CAU-003
    - CAU-004
  - **status:** DONE
  - **trigger:** operator/tasking networks
- **item 2:**
  - **gaps:**
    - message-level reception outside measured samples
  - **input_ids:**
    - FCT-001
    - FCT-003
    - FCT-009
    - FCT-018
    - FCT-023
    - FCT-030
  - **module:** clusters/FRAMING.md
  - **negative_results:**
    - same tactic does not prove same command
  - **not_computable:**
    - audience belief state for most cases
  - **operations_applied:**
    - typed deceptive presentation mechanisms
    - preserved technology change and attribution limits
  - **reason:** compare forgery, spoofing, false persona and staged-content mechanisms across eras
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CAU-001
  - **status:** DONE
  - **trigger:** deception and narrative distribution
- **item 3:**
  - **gaps:**
    - campaign-specific causal effect
  - **input_ids:**
    - FCT-015
    - FCT-016
    - FCT-027
    - FCT-028
    - FCT-029
  - **module:** clusters/POWER.md
  - **negative_results:**
    - general electoral effect not established
  - **not_computable:**
    - counterfactual France/EU outcome without exposure-linked design
  - **operations_applied:**
    - used exposure denominators
    - retained null/heterogeneous effect controls
    - separated targeting from result
  - **reason:** test whether documented operations close persuasion, behavior or outcome edges
  - **result_ids:**
    - CLM-005
    - CLM-006
    - CLM-007
    - CAU-005
  - **status:** DONE
  - **trigger:** exposure and political effect

### SCOPING_REPORT
- **exclusions:**
  - doctrine=operation
  - recurring tactic=continuous command
  - activity=effect
  - foreign case=France effect
- **geo:** USSR/Russia with Western/France/EU targets
- **object_coverage:** STRONG_FOR_REPERTOIRE_AND_CASE_TASKING; MODERATE_FOR_EXPOSURE; WEAK_FOR_GENERAL_POLITICAL_EFFECT
- **object_question:** Which documented techniques show continuity or rupture and what effects can be attributed without conflating doctrine, operation, exposure, persuasion and outcome?
- **period:** 1950-2026
- **subject:** Active Measures soviétiques puis russes

### CREDO
- doctrine != operation
- attribution != effect
- diffusion != persuasion
- repetition of tactic != continuous command
- activity != effectiveness
- targeting France/EU != measured France/EU effect

### COGNITIVE_MAP
- **continuum:**
  - documented repertoire
  - actor-specific tasking
  - action/infrastructure
  - distribution
  - exposure
  - reception
  - behavior
  - outcome
- **core_model:** continuity is strongest at the tactical repertoire level; modern tasking is case-specific; evidence decays from operation to outcome
- **rival_models:**
  - single uninterrupted active-measures apparatus
  - mostly unrelated modern digital propaganda
  - high-reach operations necessarily change elections

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** The inspected record shows different institutions and a major 1991 discontinuity.
  - **support:**
    - FCT-003
    - FCT-017
    - FCT-019
  - **synthesis:** Treat recurrent deceptive techniques as repertoire continuity and require direct evidence for organizational continuity.
  - **thesis:** Modern Russian influence is simply the unchanged Soviet active-measures system.
- **item 2:**
  - **antithesis:** Exposure is concentrated/heterogeneous and the 2016 longitudinal study finds no meaningful attitude or vote relationship.
  - **support:**
    - FCT-016
    - FCT-027
    - FCT-028
    - FCT-029
  - **synthesis:** Operation, exposure, persuasion and result require separate proof.
  - **thesis:** A large attributed operation proves electoral effectiveness.
- **item 3:**
  - **antithesis:** VIGINUM documents Portal Kombat and Matriochka infrastructures and targeting.
  - **support:**
    - FCT-021
    - FCT-023
    - FCT-024
  - **synthesis:** France/EU targeting and distribution are established case-specifically; downstream political effect remains open.
  - **thesis:** Russian information operations in France are merely allegations.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **from:** Soviet active-measures apparatus
  - **resource:** forged documents, front access, media manipulation
  - **support:**
    - FCT-001
    - FCT-003
    - FCT-005
  - **to:** foreign information environments
- **item 2:**
  - **from:** IRA
  - **resource:** staff, false personas, U.S. infrastructure, accounts
  - **support:**
    - FCT-007
    - FCT-008
    - FCT-009
  - **to:** U.S. political audiences
- **item 3:**
  - **from:** Russian Presidential Administration-linked operators
  - **resource:** domains, ads, influencers, bot accounts
  - **support:**
    - FCT-017
    - FCT-018
    - FCT-019
    - FCT-020
  - **to:** U.S./foreign audiences
- **item 4:**
  - **from:** Portal Kombat/Matriochka/Storm-1516 ecosystem
  - **resource:** sites, fake content, coordinated amplification
  - **support:**
    - FCT-021
    - FCT-023
    - FCT-025
  - **to:** France/EU/international audiences

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** KGB Service A / Soviet active-measures apparatus
  - **relation:** forgery/disinformation/front/media techniques
  - **support:**
    - FCT-003
    - FCT-005
  - **to:** foreign targets
- **item 2:**
  - **from:** Internet Research Agency
  - **relation:** organized covert social-media operation
  - **support:**
    - FCT-007
    - FCT-009
    - FCT-010
  - **to:** U.S. audiences
- **item 3:**
  - **from:** Russian Presidential Administration
  - **relation:** direction/control alleged in official action
  - **support:**
    - FCT-017
    - FCT-019
  - **to:** SDA/Structura/ANO Dialog
- **item 4:**
  - **from:** Russia-linked digital operations
  - **relation:** cross-amplification and targeting
  - **support:**
    - FCT-021
    - FCT-023
    - FCT-025
  - **to:** France/EU audiences

### IMPACT_MAP
- **established:**
  - historical operational repertoire
  - case-specific modern tasking
  - deceptive distribution infrastructure
  - France/EU targeting
  - heterogeneous reach
- **not_established:**
  - general persuasion effect
  - general electoral-result effect
  - measured France/EU political outcome caused by inspected campaigns
- **partial:**
  - organizational continuity across Soviet/Russian eras
  - representative exposure

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** different institutions and 1991 discontinuity; no archival command bridge
  - **issue:** continuity
  - **pro:** recurrent forgery/spoofing/front/persona techniques
  - **resolution:** TACTICAL_CONTINUITY_SUPPORTED; ORGANIZATIONAL_CONTINUITY_PARTIAL
  - **support:**
    - FCT-003
    - FCT-017
    - FCT-030
- **item 2:**
  - **contra:** exposure concentration, small platform shares in some periods, null relationship in 2016 study
  - **issue:** effectiveness
  - **pro:** some modern content obtains millions of views
  - **resolution:** REACH_HETEROGENEOUS; GENERAL_POLITICAL_EFFECT_NOT_ESTABLISHED
  - **support:**
    - FCT-016
    - FCT-027
    - FCT-028
    - FCT-029
- **item 3:**
  - **contra:** no inspected counterfactual attitude/vote/policy design
  - **issue:** France/EU relevance
  - **pro:** VIGINUM documents direct targeting and coordinated campaigns
  - **resolution:** TARGETING_SUPPORTED; POLITICAL_EFFECT_OPEN
  - **support:**
    - FCT-021
    - FCT-023
    - FCT-024

### VERIFICATION_REPORT
- **downgraded:**
  - unbroken Soviet-to-Russian command continuity
  - operation as proof of election change
  - France targeting as France political effect
- **fact_count:** 30
- **negative_controls:**
  - historical failed/neutralized active measures
  - Twitter relative-exposure denominator
  - Nature 2016 null relationship
  - heterogeneous 2024 engagement
- **provenance_families:** 5
- **query_count:** 20
- **source_count:** 15
- **verification:** All 30 material facts map to 15 current FETCH traces across five provenance families.

### EDI_REPORT
- **corpus:**
  - **limits:**
    - historical official adversarial reporting requires claim-bounding
    - single academic effect design cannot generalize all campaigns
    - platform/vendor reach observations are not independent causal outcome studies
  - **strength:** strong actor/action evidence with explicit downstream ceilings
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
  - **owner:** 5 provenance families
  - **perspective:** historical official + contemporary judicial/parliamentary + French technical + academic + vendor
  - **stratification:** repertoire/tasking/action/exposure/effect
  - **temporal:** 1950-2026 with explicit 1991 discontinuity
- **edi:**
  - **circularity:** CONTROLLED
  - **coverage:** HIGH_FOR_REPERTOIRE_AND_ATTRIBUTION_MODERATE_FOR_EFFECT
  - **independence:** MIXED_STRONG
- **source_counts:**
  - **A:** 3
  - **B:** 7
  - **C:** 3
  - **D:** 1
  - **E:** 1
  - **total:** 15

### RESPONSIBILITY_MAP
- **boundary:** Technique, actor, tasking, action, exposure, persuasion and outcome are distinct claims.
- **not_established:**
  - unbroken KGB-to-current command chain
  - every pro-Russian amplifier is tasked
  - general voter persuasion
  - changed French/EU election or policy result
- **verified:**
  - Soviet active-measures repertoire
  - IRA organized covert activity
  - Doppelganger actor-specific direction allegations with disclosed infrastructure
  - France/EU-facing Portal Kombat and Matriochka campaigns

### NEXT_QUERIES
- Archival bridge evidence on post-1991 transfer of active-measures personnel/doctrine into specific Russian institutions
- France/EU operation-specific reach and audience denominators tied to attributed campaigns
- Causal designs linking exposure to Matriochka/Portal Kombat/Doppelganger/Storm-1516 to attitudes, participation, vote or policy
- Decision-level records of modern Russian tasking for downstream Western amplifiers; do not infer from narrative alignment alone

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-006,QRY-007,QRY-008 | support:- | counter:- | results:FCT-001,FCT-003,FCT-005,FCT-030 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-002,QRY-009,QRY-010,QRY-014,QRY-015 | support:- | counter:- | results:FCT-007,FCT-009,FCT-017,FCT-019 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-003,QRY-013,QRY-020 | support:- | counter:- | results:FCT-015,FCT-016,FCT-021,FCT-029 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-004,QRY-019,QRY-020 | support:- | counter:- | results:FCT-002,FCT-004,FCT-028,FCT-029 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-006,QRY-007,QRY-008,SRC-001,SRC-002,SRC-003 | support:FCT-001,FCT-003,FCT-005 | counter:FCT-002,FCT-004 | results:FCT-001,FCT-003,FCT-005,FCT-002,FCT-004 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-010,QRY-014,QRY-017,QRY-020,SRC-005,SRC-009,SRC-012,SRC-015 | support:FCT-009,FCT-017,FCT-018,FCT-023,FCT-024,FCT-030 | counter:FCT-029 | results:FCT-009,FCT-017,FCT-018,FCT-023,FCT-024,FCT-030,FCT-029 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-007,QRY-008,QRY-009,QRY-014,QRY-015,QRY-016,SRC-002,SRC-003,SRC-004,SRC-009,SRC-010,SRC-011 | support:FCT-003,FCT-005,FCT-007,FCT-017,FCT-019,FCT-021 | counter:- | results:FCT-003,FCT-005,FCT-007,FCT-017,FCT-019,FCT-021 | final:PARTIAL | gap:TEMPORAL
CLM-004 | attempts:QRY-009,QRY-010,QRY-014,QRY-015,SRC-004,SRC-005,SRC-009,SRC-010 | support:FCT-007,FCT-008,FCT-009,FCT-010,FCT-017,FCT-019,FCT-020 | counter:- | results:FCT-007,FCT-008,FCT-009,FCT-010,FCT-017,FCT-019,FCT-020 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-016,QRY-017,QRY-018,SRC-011,SRC-012,SRC-013 | support:FCT-021,FCT-022,FCT-023,FCT-024,FCT-025,FCT-026 | counter:- | results:FCT-021,FCT-022,FCT-023,FCT-024,FCT-025,FCT-026 | final:PARTIAL | gap:CAUSALITY
CLM-006 | attempts:QRY-013,QRY-014,QRY-019,QRY-020,SRC-008,SRC-009,SRC-014,SRC-015 | support:FCT-015,FCT-016,FCT-027,FCT-029 | counter:FCT-018,FCT-030 | results:FCT-015,FCT-016,FCT-027,FCT-029,FCT-018,FCT-030 | final:SUPPORTED | gap:NONE
CLM-007 | attempts:QRY-014,QRY-019,QRY-020,SRC-009,SRC-014,SRC-015 | support:FCT-027,FCT-028,FCT-029 | counter:FCT-018 | results:FCT-027,FCT-028,FCT-029,FCT-018 | final:PARTIAL | gap:CAUSALITY
CLM-008 | attempts:QRY-006,QRY-007,QRY-014,QRY-020,SRC-001,SRC-002,SRC-009,SRC-015 | support:FCT-002,FCT-004,FCT-017,FCT-018 | counter:FCT-029 | results:FCT-002,FCT-004,FCT-017,FCT-018,FCT-029 | final:SUPPORTED | gap:NONE

## STATUS_DELTA_V1
DELTA-001 | AXS-001 | OPEN | SATURATED | axis closed after FACTS with explicit result IDs
DELTA-002 | AXS-002 | OPEN | SATURATED | axis closed after FACTS with explicit result IDs
DELTA-003 | AXS-003 | OPEN | SATURATED | axis closed after FACTS with explicit result IDs
DELTA-004 | AXS-004 | OPEN | SATURATED | axis closed after FACTS with explicit result IDs

## OPEN_GAPS_V1
CLM-003 | CLM | PARTIAL | TEMPORAL | A direct archival command/organizational bridge across the Soviet collapse and later Russian operator ecosystem is not established in the inspected record.
CLM-005 | CLM | PARTIAL | CAUSALITY | No inspected France/EU design isolates marginal effects on political attitudes, voting or a named public decision.
CLM-007 | CLM | PARTIAL | CAUSALITY | Case-specific effects outside the measured Twitter sample and later campaigns remain possible and require their own exposure-to-outcome designs.
CAU-005 | CAU | UNRESOLVED | CAUSALITY | Requires campaign-specific exposure, reception and counterfactual outcome designs, especially for France/EU and post-2022 operations.

SEMANTIC_COUNTS_V1:LED:0|CLM:8|AXS:4|CAU:5|CTRL:10|ACT:4

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Soviet active measures were a heterogeneous toolkit including forgery, disinformation, front organizations, influence agents and media manipulation; reducing them to a single propaganda program is not supported.","claimant":"INV-013 synthesis","counter":["FCT-002","FCT-004"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-003","FCT-005"]}
CLM-002 | {"claim":"Modern Russian influence operations show tactical continuity with older active-measures techniques in source concealment, false identities, spoofed media, front-like intermediaries and coordinated amplification, while adding digital infrastructure, social platforms and AI-enhanced content.","claimant":"INV-013 synthesis","counter":["FCT-029"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-009","FCT-017","FCT-018","FCT-023","FCT-024","FCT-030"]}
CLM-003 | {"claim":"The inspected corpus does not establish an unbroken institutional command chain from Soviet KGB Service A to current Russian Presidential Administration, IRA, ANO Dialog, SDA, TigerWeb or other modern operators; continuity is strongest at the repertoire level.","claimant":"INV-013 synthesis","counter":"NONE_FOUND","gap":"A direct archival command/organizational bridge across the Soviet collapse and later Russian operator ecosystem is not established in the inspected record.","gap_type":"TEMPORAL","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-003","FCT-005","FCT-007","FCT-017","FCT-019","FCT-021"]}
CLM-004 | {"claim":"Case-specific modern tasking and control can be strongly established: the IRA indictment documents organized U.S.-targeted activity, and the 2024 Doppelganger record attributes SDA/Structura/ANO Dialog activity to Russian Presidential Administration direction.","claimant":"INV-013 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-007","FCT-008","FCT-009","FCT-010","FCT-017","FCT-019","FCT-020"]}
CLM-005 | {"claim":"France and wider Europe were demonstrably targeted by contemporary pro-Russian information infrastructures including Portal Kombat and Matriochka, but target selection and content distribution do not by themselves establish changed French or European political preferences or outcomes.","claimant":"INV-013 synthesis","counter":"NONE_FOUND","gap":"No inspected France/EU design isolates marginal effects on political attitudes, voting or a named public decision.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-021","FCT-022","FCT-023","FCT-024","FCT-025","FCT-026"]}
CLM-006 | {"claim":"Reach and exposure are highly heterogeneous: modern operations can generate millions of views, yet platform denominators and the 2016 linked-survey study show concentration and sometimes small relative exposure compared with domestic political information.","claimant":"INV-013 synthesis","counter":["FCT-018","FCT-030"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-015","FCT-016","FCT-027","FCT-029"]}
CLM-007 | {"claim":"The strongest inspected evidence does not establish a general chain from Russian information-operation exposure to persuasion, vote change or electoral-result change; the 2023 longitudinal Twitter study found no meaningful relationship with attitudes, polarization or voting behavior in its sample.","claimant":"INV-013 synthesis","counter":["FCT-018"],"gap":"Case-specific effects outside the measured Twitter sample and later campaigns remain possible and require their own exposure-to-outcome designs.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-027","FCT-028","FCT-029"]}
CLM-008 | {"claim":"Countermeasures matter to effectiveness: Soviet forgeries were sometimes neutralized by exposure, while contemporary campaigns face domain seizure, platform disruption and public attribution; operation capability therefore cannot be treated as fixed realized influence.","claimant":"INV-013 synthesis","counter":["FCT-029"],"gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-002","FCT-004","FCT-017","FCT-018"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-006","QRY-007","QRY-008"],"axis":"soviet_doctrine_and_techniques","links":["INV-013"],"question":"Quelles techniques d active measures sont directement documentees dans les archives officielles soviet-era et lesquelles peuvent etre comparees a des operations russes contemporaines?","result_ids":["FCT-001","FCT-003","FCT-005","FCT-030"],"sought_objects":["forgery","front groups","media manipulation","covert placement","false personas"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-002","QRY-009","QRY-010","QRY-014","QRY-015"],"axis":"operator_tasking_attribution","links":["INV-013"],"question":"Quelles operations contemporaines ferment une chaine operateur -> commandement/tasking -> infrastructure/action plutot qu une simple attribution geopolitique?","result_ids":["FCT-007","FCT-009","FCT-017","FCT-019"],"sought_objects":["operator","principal","tasking","infrastructure","action"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-003","QRY-013","QRY-020"],"axis":"exposure_and_reach","links":["INV-013"],"question":"Quels denominators ou mesures permettent de distinguer presence d une operation, diffusion, exposition et portee reelle?","result_ids":["FCT-015","FCT-016","FCT-021","FCT-029"],"sought_objects":["reach","impressions","share of exposure","audience concentration"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-004","QRY-019","QRY-020"],"axis":"persuasion_behavior_outcome","links":["INV-013"],"question":"Quels designs mesurent reception, persuasion, comportement ou resultat politique et ou s arrete la causalite?","result_ids":["FCT-002","FCT-004","FCT-028","FCT-029"],"sought_objects":["attitude change","polarization","vote choice","counterfactual outcome"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"Documented operational repertoire and distribution capacity","counter":["FCT-002","FCT-004"],"limit":"Technique execution and institutional use are established; generalized persuasion or policy change is not.","mechanism":"Soviet authority/KGB active-measures apparatus -> forged documents/fronts/media manipulation -> foreign distribution environments","status":"SUPPORTED","support":["FCT-001","FCT-003","FCT-005","FCT-006"]}
CAU-002 | {"causal_right":"Organized covert action and audience exposure","counter":["FCT-015","FCT-016","FCT-028"],"limit":"Tasking/action are strong; measured marginal persuasion and result change remain unclosed.","mechanism":"IRA organization -> false personas/US infrastructure -> interaction with U.S. audiences -> election-related activity","status":"SUPPORTED","support":["FCT-007","FCT-008","FCT-009","FCT-010","FCT-011"]}
CAU-003 | {"causal_right":"Actor-specific command-to-operation chain","counter":"NONE_FOUND","limit":"Direct campaign command is alleged/documented by official U.S. action; downstream voter or policy effect is not established.","mechanism":"Russian Presidential Administration -> SDA/Structura/ANO Dialog -> spoofed domains/influencers/bots -> foreign audience targeting","status":"SUPPORTED","support":["FCT-017","FCT-018","FCT-019","FCT-020"]}
CAU-004 | {"causal_right":"Case-specific coordinated distribution and targeting","counter":"NONE_FOUND","limit":"Distribution and targeting are established; common tasking for every downstream amplifier and political effect are not.","mechanism":"Russia-linked operator ecosystem -> Portal Kombat/Matriochka/Storm-1516 cross-amplification -> France/EU information exposure","status":"SUPPORTED","support":["FCT-021","FCT-022","FCT-023","FCT-024","FCT-025","FCT-026"]}
CAU-005 | {"counter":["FCT-015","FCT-016","FCT-027","FCT-028"],"gap":"Requires campaign-specific exposure, reception and counterfactual outcome designs, especially for France/EU and post-2022 operations.","gap_type":"CAUSALITY","limit":"No general causal closure; the strongest inspected individual-level study finds no meaningful relationship in the 2016 Twitter sample.","mechanism":"Russian influence-operation exposure -> attitude/polarization/vote change -> electoral or policy outcome","status":"UNRESOLVED","support":["FCT-018","FCT-029"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Doctrine is not an operation: Soviet descriptions of an active-measures repertoire cannot prove that every listed technique was used in a given case.","status":"DONE","support":["FCT-001","FCT-005"]}
CTRL-002 | {"control":"Technique recurrence is not organizational continuity: false documents or spoofed media in different eras do not prove one uninterrupted command structure.","status":"DONE","support":["FCT-003","FCT-017","FCT-030"]}
CTRL-003 | {"control":"Attribution is not effect: identifying IRA, ANO Dialog, SDA or other operators does not establish persuasion or changed electoral outcomes.","status":"DONE","support":["FCT-007","FCT-017","FCT-028"]}
CTRL-004 | {"control":"Raw reach is not representative exposure: millions of impressions can coexist with highly concentrated exposure among a small user subset.","status":"DONE","support":["FCT-027","FCT-029"]}
CTRL-005 | {"control":"Platform share denominator matters: Twitter s 2017 testimony placed Russian-linked automated election exposure at a small share of overall election-related tweets seen in its studied period.","status":"DONE","support":["FCT-015","FCT-016"]}
CTRL-006 | {"control":"Historical countermeasure control: official exposure and debunking sometimes neutralized Soviet forgery effects.","status":"DONE","support":["FCT-004"]}
CTRL-007 | {"control":"Modern countermeasure control: domain seizure and attribution can disrupt infrastructure without proving the campaign previously changed voter behavior.","status":"DONE","support":["FCT-017","FCT-018"]}
CTRL-008 | {"control":"Downstream amplifier is not automatically a tasked asset: VIGINUM notes Western pro-Russian actors amplifying Storm-1516 narratives without establishing common command for every amplifier.","status":"DONE","support":["FCT-025","FCT-026"]}
CTRL-009 | {"control":"France/EU target selection is not France/EU political effect: Portal Kombat and Matriochka presence closes targeting/distribution, not preference or election change.","status":"DONE","support":["FCT-021","FCT-023","FCT-024"]}
CTRL-010 | {"control":"A null or weak measured effect in one 2016 Twitter design does not prove all Russian influence operations are ineffective across channels, populations and periods.","status":"DONE","support":["FCT-028","FCT-029"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Require actor-specific tasking/command evidence before upgrading tactical continuity into institutional continuity.","actor":"future investigator","intent":"prevent continuity inflation","status":"DONE","support":["FCT-003","FCT-017","FCT-019"]}
ACT-002 | {"action":"For every influence operation, preserve separate denominators for content produced, distribution, potential exposure, verified exposure, reception and behavioral outcome.","actor":"future investigator","intent":"prevent operation-to-effect inflation","status":"DONE","support":["FCT-015","FCT-016","FCT-027","FCT-029"]}
ACT-003 | {"action":"Prioritize France/EU campaign-specific studies that link attributed operation exposure to measured attitudes, participation, vote or policy effects with a credible counterfactual.","actor":"program","intent":"close the principal causal gap","status":"DONE","support":["FCT-021","FCT-023","FCT-028"]}
ACT-004 | {"action":"Use same mechanism-first standard for Russian, allied and domestic operations; classify concealment, tasking, coercion, reach and effect separately.","actor":"program","intent":"preserve symmetry","status":"DONE","support":["FCT-001","FCT-007","FCT-017","FCT-028"]}

SEARCH_ACTIVITY_V1:WEB:5|FETCH:15|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL | mnemo | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | Soviet active measures report forgery disinformation front groups Service A
QRY-002 | WEB | FOUND | - | - | Russian active measures 2016 Senate social media IRA
QRY-003 | WEB | FOUND | - | - | Doppelganger Russian Presidential Administration SDA Structura ANO Dialog
QRY-004 | WEB | FOUND | - | - | VIGINUM Portal Kombat Matriochka Storm-1516 France
QRY-005 | WEB | FOUND | - | - | Russian IRA exposure attitudes voting behavior 2016 Nature Communications
QRY-006 | FETCH | FOUND | SRC-001 | https://www.cia.gov/readingroom/docs/CIA-RDP84B00274R000100040004-8.pdf | https://www.cia.gov/readingroom/docs/CIA-RDP84B00274R000100040004-8.pdf
QRY-007 | FETCH | FOUND | SRC-002 | https://www.cia.gov/readingroom/docs/CIA-RDP90-00806R000200720008-2.pdf | https://www.cia.gov/readingroom/docs/CIA-RDP90-00806R000200720008-2.pdf
QRY-008 | FETCH | FOUND | SRC-003 | https://www.cia.gov/readingroom/docs/CIA-RDP88G01116R000400410020-1.pdf | https://www.cia.gov/readingroom/docs/CIA-RDP88G01116R000400410020-1.pdf
QRY-009 | FETCH | FOUND | SRC-004 | https://www.justice.gov/archives/opa/pr/grand-jury-indicts-thirteen-russian-individuals-and-three-russian-companies-scheme-interfere | https://www.justice.gov/archives/opa/pr/grand-jury-indicts-thirteen-russian-individuals-and-three-russian-companies-scheme-interfere
QRY-010 | FETCH | FOUND | SRC-005 | https://www.justice.gov/archives/sco/file/1035477/dl?inline= | https://www.justice.gov/archives/sco/file/1035477/dl?inline=
QRY-011 | FETCH | FOUND | SRC-006 | https://www.intelligence.senate.gov/2019/10/08/press-senate-intel-committee-releases-bipartisan-report-russia-e2-80-99s-use-social-media/ | https://www.intelligence.senate.gov/2019/10/08/press-senate-intel-committee-releases-bipartisan-report-russia-e2-80-99s-use-social-media/
QRY-012 | FETCH | FOUND | SRC-007 | https://www.intelligence.senate.gov/2020/08/18/publications-report-select-committee-intelligence-united-states-senate-russian-active-measures/ | https://www.intelligence.senate.gov/2020/08/18/publications-report-select-committee-intelligence-united-states-senate-russian-active-measures/
QRY-013 | FETCH | FOUND | SRC-008 | https://www.intelligence.senate.gov/2017/10/26/hearings-open-hearing-social-media-influence-2016-us-elections/ | https://www.intelligence.senate.gov/2017/10/26/hearings-open-hearing-social-media-influence-2016-us-elections/
QRY-014 | FETCH | FOUND | SRC-009 | https://www.justice.gov/usao-edpa/pr/justice-department-disrupts-covert-russian-government-sponsored-foreign-malign | https://www.justice.gov/usao-edpa/pr/justice-department-disrupts-covert-russian-government-sponsored-foreign-malign
QRY-015 | FETCH | FOUND | SRC-010 | https://home.treasury.gov/news/press-releases/jy2559 | https://home.treasury.gov/news/press-releases/jy2559
QRY-016 | FETCH | FOUND | SRC-011 | https://www.sgdsn.gouv.fr/publications/portal-kombat-un-reseau-structure-et-coordonne-de-propagande-prorusse | https://www.sgdsn.gouv.fr/publications/portal-kombat-un-reseau-structure-et-coordonne-de-propagande-prorusse
QRY-017 | FETCH | FOUND | SRC-012 | https://www.sgdsn.gouv.fr/viginum/publications/matriochka-une-campagne-prorusse-ciblant-les-medias-et-la-communaute-des-fact | https://www.sgdsn.gouv.fr/viginum/publications/matriochka-une-campagne-prorusse-ciblant-les-medias-et-la-communaute-des-fact
QRY-018 | FETCH | FOUND | SRC-013 | https://www.sgdsn.gouv.fr/files/2025-05/20250507_TLP-CLEAR_NP_SGDSN_VIGINUM_Rapport%20technique_Storm-1516.pdf | https://www.sgdsn.gouv.fr/files/2025-05/20250507_TLP-CLEAR_NP_SGDSN_VIGINUM_Rapport%20technique_Storm-1516.pdf
QRY-019 | FETCH | FOUND | SRC-014 | https://www.nature.com/articles/s41467-022-35576-9 | https://www.nature.com/articles/s41467-022-35576-9
QRY-020 | FETCH | FOUND | SRC-015 | https://blogs.microsoft.com/on-the-issues/2024/10/23/as-the-u-s-election-nears-russia-iran-and-china-step-up-influence-efforts/ | https://blogs.microsoft.com/on-the-issues/2024/10/23/as-the-u-s-election-nears-russia-iran-and-china-step-up-influence-efforts/

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | STATE-SR88-1981 | Soviet Active Measures Special Report No. 88 | 1981-10-01 | 2026-09-10T00:00:00Z | Forgery, Disinformation, Political Operations | https://www.cia.gov/readingroom/docs/CIA-RDP84B00274R000100040004-8.pdf
SRC-002 | ◈ | fam:A | CIA-ACTIVE-MEASURES-FORGERY | Active Measures - Forgery | 1986-01-01 | 2026-09-10T00:00:00Z | Service A forgery operations and countering | https://www.cia.gov/readingroom/docs/CIA-RDP90-00806R000200720008-2.pdf
SRC-003 | ◈ | fam:A | DCI-ICS-86-0856 | DCI Intelligence Community Staff memorandum on Soviet activities | 1986-01-01 | 2026-09-10T00:00:00Z | Active Measures section | https://www.cia.gov/readingroom/docs/CIA-RDP88G01116R000400410020-1.pdf
SRC-004 | ◈ | fam:B | DOJ-IRA-2018-PR | Grand Jury Indicts Thirteen Russian Individuals and Three Russian Companies | 2018-02-16 | 2026-09-10T00:00:00Z | IRA organization and translator project | https://www.justice.gov/archives/opa/pr/grand-jury-indicts-thirteen-russian-individuals-and-three-russian-companies-scheme-interfere
SRC-005 | ◈ | fam:B | DOJ-IRA-INDICTMENT | Internet Research Agency Indictment | 2018-02-16 | 2026-09-10T00:00:00Z | False personas, identities and election targeting | https://www.justice.gov/archives/sco/file/1035477/dl?inline=
SRC-006 | ◈ | fam:B | SSCI-RUSSIA-SOCIAL-MEDIA-V2 | Senate report - Russia s Use of Social Media | 2019-10-08 | 2026-09-10T00:00:00Z | Volume 2 overview | https://www.intelligence.senate.gov/2019/10/08/press-senate-intel-committee-releases-bipartisan-report-russia-e2-80-99s-use-social-media/
SRC-007 | ◈ | fam:B | SSCI-RUSSIAN-ACTIVE-MEASURES-2020 | Russian Active Measures Campaigns and Interference in the 2016 U.S. Election | 2020-08-18 | 2026-09-10T00:00:00Z | Volumes I-V publication | https://www.intelligence.senate.gov/2020/08/18/publications-report-select-committee-intelligence-united-states-senate-russian-active-measures/
SRC-008 | ◈ | fam:B | SSCI-SOCIAL-MEDIA-HEARING-2017 | Open Hearing - Social Media Influence in the 2016 U.S. Elections | 2017-10-26 | 2026-09-10T00:00:00Z | Twitter testimony exposure denominators | https://www.intelligence.senate.gov/2017/10/26/hearings-open-hearing-social-media-influence-2016-us-elections/
SRC-009 | ◈ | fam:B | DOJ-DOPPELGANGER-2024 | Justice Department Disrupts Covert Russian Government-Sponsored Foreign Malign Influence Operation | 2024-09-04 | 2026-09-10T00:00:00Z | 32 domains and Presidential Administration direction | https://www.justice.gov/usao-edpa/pr/justice-department-disrupts-covert-russian-government-sponsored-foreign-malign
SRC-010 | ◈ | fam:B | TREASURY-RUSSIA-FMI-2024 | Treasury Takes Action on Russia Foreign Malign Influence Operations | 2024-09-04 | 2026-09-10T00:00:00Z | ANO Dialog, RRN and bot coordination | https://home.treasury.gov/news/press-releases/jy2559
SRC-011 | ◈ | fam:C | VIGINUM-PORTAL-KOMBAT-2024 | Portal Kombat - un reseau structure et coordonne de propagande prorusse | 2024-02-12 | 2026-09-10T00:00:00Z | 193-site network and France targeting | https://www.sgdsn.gouv.fr/publications/portal-kombat-un-reseau-structure-et-coordonne-de-propagande-prorusse
SRC-012 | ◈ | fam:C | VIGINUM-MATRIOCHKA-2024 | Matriochka - une campagne prorusse ciblant les medias et fact-checkers | 2024-06-10 | 2026-09-10T00:00:00Z | Fake content and coordinated targeting | https://www.sgdsn.gouv.fr/viginum/publications/matriochka-une-campagne-prorusse-ciblant-les-medias-et-la-communaute-des-fact
SRC-013 | ◈ | fam:C | VIGINUM-STORM1516-2025 | Rapport technique Storm-1516 | 2025-05-07 | 2026-09-10T00:00:00Z | Cross-amplification by RRN Portal Kombat Mriya | https://www.sgdsn.gouv.fr/files/2025-05/20250507_TLP-CLEAR_NP_SGDSN_VIGINUM_Rapport%20technique_Storm-1516.pdf
SRC-014 | ◈ | fam:D | NATURE-EADY-2023 | Exposure to the Russian Internet Research Agency foreign influence campaign on Twitter | 2023-01-09 | 2026-09-10T00:00:00Z | Exposure concentration and attitudes/vote analysis | https://www.nature.com/articles/s41467-022-35576-9
SRC-015 | ◈ | fam:E | MSFT-MTAC-2024-10 | As the U.S. election nears Russia Iran and China step up influence efforts | 2024-10-23 | 2026-09-10T00:00:00Z | Russian staged and AI-enhanced video reach | https://blogs.microsoft.com/on-the-issues/2024/10/23/as-the-u-s-election-nears-russia-iran-and-china-step-up-influence-efforts/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.cia.gov/readingroom/docs/CIA-RDP84B00274R000100040004-8.pdf | A | 1981-10-01 | 1981 active-measures scope | The State Department special report describes Soviet active measures as including forgery, disinformation and political operations rather than a single propaganda technique. | -
FCT-002 | FACT | ✧ | https://www.cia.gov/readingroom/docs/CIA-RDP84B00274R000100040004-8.pdf | A | 1981-10-01 | 1981 effectiveness control | The same report explicitly states that Soviet active measures did not always achieve Moscow s objectives and sometimes failed because of ineptitude or effective target response. | -
FCT-003 | FACT | ✧ | https://www.cia.gov/readingroom/docs/CIA-RDP90-00806R000200720008-2.pdf | A | 1986-01-01 | Service A forgery role | The declassified active-measures document attributes KGB forgery operations to Service A of the First Chief Directorate and describes forged or fabricated U.S.-appearing documents as a clandestine political-warfare technique. | -
FCT-004 | FACT | ✧ | https://www.cia.gov/readingroom/docs/CIA-RDP90-00806R000200720008-2.pdf | A | 1986-01-01 | Forgery countermeasure effect | The document states that rapid CIA/FBI exposure of errors and motivation neutralized much of the effect of many Soviet forgeries, providing a direct negative control on assumed effectiveness. | -
FCT-005 | FACT | ✧ | https://www.cia.gov/readingroom/docs/CIA-RDP88G01116R000400410020-1.pdf | A | 1986-01-01 | 1986 active-measures architecture | A declassified Intelligence Community memorandum describes active measures as covert action used to implement Soviet policy goals and identifies front groups, influence agents and media manipulation as continuing techniques. | -
FCT-006 | FACT | ✧ | https://www.cia.gov/readingroom/docs/CIA-RDP88G01116R000400410020-1.pdf | A | 1986-01-01 | Los Angeles Olympics forgery case | The memorandum describes a 1984 campaign using forged threat letters to discredit the Los Angeles Olympics and records U.S. attribution of the letters to a Soviet active-measures pattern. | -
FCT-007 | FACT | ✧ | https://www.justice.gov/archives/opa/pr/grand-jury-indicts-thirteen-russian-individuals-and-three-russian-companies-scheme-interfere | B | 2018-02-16 | IRA organizational capacity | The 2018 DOJ release alleges that the Internet Research Agency operated as a structured organization with hundreds of personnel and an annual budget of millions of dollars for online operations. | -
FCT-008 | FACT | ✧ | https://www.justice.gov/archives/opa/pr/grand-jury-indicts-thirteen-russian-individuals-and-three-russian-companies-scheme-interfere | B | 2018-02-16 | IRA Translator Project staffing | DOJ states that the IRA created a Translator Project focused on the U.S. population and that more than 80 employees were assigned to it by July 2016. | -
FCT-009 | FACT | ✧ | https://www.justice.gov/archives/sco/file/1035477/dl?inline= | B | 2018-02-16 | IRA false-persona infrastructure | The IRA indictment alleges use of U.S.-based infrastructure, false U.S. personas, hundreds of accounts and stolen identities to mask Russian origin and interact with real U.S. persons. | -
FCT-010 | FACT | ✧ | https://www.justice.gov/archives/sco/file/1035477/dl?inline= | B | 2018-02-16 | IRA election intent timing | The indictment alleges that by approximately May 2014 the defendants were discussing efforts to interfere in the 2016 U.S. presidential election and later targeted election-related audiences. | -
FCT-011 | FACT | ✧ | https://www.intelligence.senate.gov/2019/10/08/press-senate-intel-committee-releases-bipartisan-report-russia-e2-80-99s-use-social-media/ | B | 2019-10-08 | Senate social-media attribution | The Senate Intelligence Committee describes the 2016 social-media campaign as led by the Kremlin-backed Internet Research Agency and intended to sow societal discord and influence the election environment. | -
FCT-012 | FACT | ✧ | https://www.intelligence.senate.gov/2019/10/08/press-senate-intel-committee-releases-bipartisan-report-russia-e2-80-99s-use-social-media/ | B | 2019-10-08 | Senate evidence basis | The Senate report states that its social-media analysis drew on platform-provided data and a technical advisory group, separating campaign attribution evidence from downstream persuasion claims. | -
FCT-013 | FACT | ✧ | https://www.intelligence.senate.gov/2020/08/18/publications-report-select-committee-intelligence-united-states-senate-russian-active-measures/ | B | 2020-08-18 | Senate active-measures framing | The Senate Select Committee published a bipartisan multi-volume report explicitly titled Russian Active Measures Campaigns and Interference in the 2016 U.S. Election. | -
FCT-014 | FACT | ✧ | https://www.intelligence.senate.gov/2020/08/18/publications-report-select-committee-intelligence-united-states-senate-russian-active-measures/ | B | 2020-08-18 | Senate multi-volume scope | The 2020 publication consolidates Volumes I-V of the committee investigation, showing that cyber, social-media, intelligence and political-contact questions were treated as distinct evidentiary components rather than one undifferentiated operation. | -
FCT-015 | FACT | ✧ | https://www.intelligence.senate.gov/2017/10/26/hearings-open-hearing-social-media-influence-2016-us-elections/ | B | 2017-10-26 | Twitter linked-account denominator | In 2017 Senate testimony, Twitter said accounts it could link to Russia that tweeted election-related content represented about one one-hundredth of one percent of total Twitter accounts in the studied period. | -
FCT-016 | FACT | ✧ | https://www.intelligence.senate.gov/2017/10/26/hearings-open-hearing-social-media-influence-2016-us-elections/ | B | 2017-10-26 | Twitter exposure-share denominator | The same testimony said about one-third of one percent of election-related tweets people saw came from Russian-linked automated accounts, a material denominator against raw account or impression totals. | -
FCT-017 | FACT | ✧ | https://www.justice.gov/usao-edpa/pr/justice-department-disrupts-covert-russian-government-sponsored-foreign-malign | B | 2024-09-04 | Doppelganger command chain | A 2024 DOJ action alleges that SDA, Structura and ANO Dialog operated under the direction and control of the Russian Presidential Administration, including Sergei Kiriyenko, in the Doppelganger campaign. | -
FCT-018 | FACT | ✧ | https://www.justice.gov/usao-edpa/pr/justice-department-disrupts-covert-russian-government-sponsored-foreign-malign | B | 2024-09-04 | Doppelganger deception infrastructure | DOJ describes 32 seized domains, cybersquatted news sites, paid ads, influencers and social profiles posing as non-Russian citizens to obscure source identity and drive audiences to Russian-government messaging. | -
FCT-019 | FACT | ✧ | https://home.treasury.gov/news/press-releases/jy2559 | B | 2024-09-04 | RRN provenance concealment | Treasury reports that an ANO Dialog adviser purchased the rrn.world domain to avoid retaining an obvious connection to Russia and coordinated services for an RRN-affiliate translator. | -
FCT-020 | FACT | ✧ | https://home.treasury.gov/news/press-releases/jy2559 | B | 2024-09-04 | Voting-location bot coordination | Treasury states that in May 2024 ANO Dialog and Dialog Regions personnel coordinated with Russian government officials on creation of bot accounts for a misinformation campaign concerning U.S. voting locations. | -
FCT-021 | FACT | ✧ | https://www.sgdsn.gouv.fr/publications/portal-kombat-un-reseau-structure-et-coordonne-de-propagande-prorusse | C | 2024-02-12 | Portal Kombat network scale | VIGINUM identified at least 193 similar pro-Russian information portals in Portal Kombat during its initial investigation. | -
FCT-022 | FACT | ✧ | https://www.sgdsn.gouv.fr/publications/portal-kombat-un-reseau-structure-et-coordonne-de-propagande-prorusse | C | 2024-02-12 | Portal Kombat retargeting | VIGINUM found that the network shifted after Russia s invasion of Ukraine toward occupied territories and then Western countries supporting Ukraine, including France. | -
FCT-023 | FACT | ✧ | https://www.sgdsn.gouv.fr/viginum/publications/matriochka-une-campagne-prorusse-ciblant-les-medias-et-la-communaute-des-fact | C | 2024-06-10 | Matriochka fake-content mechanism | VIGINUM documents Matriochka as active since at least September 2023 and based on fabricated reports, graffiti, memes and other false content. | -
FCT-024 | FACT | ✧ | https://www.sgdsn.gouv.fr/viginum/publications/matriochka-une-campagne-prorusse-ciblant-les-medias-et-la-communaute-des-fact | C | 2024-06-10 | Matriochka target-laundering mechanism | VIGINUM describes coordinated replies and emails that directly ask media and fact-checkers in more than sixty countries to investigate the fabricated content, using the target s own verification process as an amplification vector. | -
FCT-025 | FACT | ✧ | https://www.sgdsn.gouv.fr/files/2025-05/20250507_TLP-CLEAR_NP_SGDSN_VIGINUM_Rapport%20technique_Storm-1516.pdf | C | 2025-05-07 | Storm1516 cross-network amplification | VIGINUM reports that narratives attributed to Storm-1516 were amplified by other Russia-linked information operations including RRN/Doppelganger, Portal Kombat and Mriya. | -
FCT-026 | FACT | ✧ | https://www.sgdsn.gouv.fr/files/2025-05/20250507_TLP-CLEAR_NP_SGDSN_VIGINUM_Rapport%20technique_Storm-1516.pdf | C | 2025-05-07 | Storm1516 intermediary amplification | The report also notes repeated amplification by Western pro-Russian media and actors, demonstrating a distribution layer that is not equivalent to proving common tasking for every downstream amplifier. | -
FCT-027 | FACT | ✧ | https://www.nature.com/articles/s41467-022-35576-9 | D | 2023-01-09 | IRA exposure concentration | The 2023 Nature Communications study found that only 1 percent of users accounted for 70 percent of exposures to Russian foreign-influence accounts in its linked Twitter-survey sample. | -
FCT-028 | FACT | ✧ | https://www.nature.com/articles/s41467-022-35576-9 | D | 2023-01-09 | IRA measured-effect ceiling | Across its longitudinal outcomes, the study found no evidence of a meaningful relationship between exposure to Russian influence accounts and changes in attitudes, polarization or voting behavior; the authors also stress the observational design is not definitive causal proof. | -
FCT-029 | FACT | ✧ | https://blogs.microsoft.com/on-the-issues/2024/10/23/as-the-u-s-election-nears-russia-iran-and-china-step-up-influence-efforts/ | E | 2024-10-23 | 2024 Russian video reach heterogeneity | Microsoft reported that some Russian influence videos in the 2024 U.S. cycle received minimal engagement while other staged or false videos obtained millions of views, showing substantial reach heterogeneity across operations. | -
FCT-030 | FACT | ✧ | https://blogs.microsoft.com/on-the-issues/2024/10/23/as-the-u-s-election-nears-russia-iran-and-china-step-up-influence-efforts/ | E | 2024-10-23 | Traditional-technique continuity | Microsoft assessed that Kremlin-backed campaigns continued to rely heavily on longstanding techniques such as staged videos, deceptive editing and spoofed media alongside newer AI-enhanced content, supporting tactical continuity with technological adaptation rather than identity of command structures across eras. | -
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
FCT-019 | SRC-010
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
FCT-023 | ELIGIBLE:VERIFIE
FCT-024 | ELIGIBLE:VERIFIE
FCT-025 | ELIGIBLE:VERIFIE
FCT-026 | ELIGIBLE:VERIFIE
FCT-027 | ELIGIBLE:VERIFIE
FCT-028 | ELIGIBLE:VERIFIE
FCT-029 | ELIGIBLE:VERIFIE
FCT-030 | ELIGIBLE:VERIFIE

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
FCT-023 | WRITE | -
FCT-024 | WRITE | -
FCT-025 | WRITE | -
FCT-026 | WRITE | -
FCT-027 | WRITE | -
FCT-028 | WRITE | -
FCT-029 | WRITE | -
FCT-030 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:search
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:facts
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:causal
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:verify
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:accountability
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:finalize

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-10T00:10:26.361804+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-029","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-030","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":30,"eligible":30,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:30;attempted:0;success:0;failure:0;blocked:30} | WRITEBACK_EXECUTION_V1:[30 rows, see section]

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
FCT-023 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-024 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-025 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-026 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-027 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-028 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-029 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-030 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
