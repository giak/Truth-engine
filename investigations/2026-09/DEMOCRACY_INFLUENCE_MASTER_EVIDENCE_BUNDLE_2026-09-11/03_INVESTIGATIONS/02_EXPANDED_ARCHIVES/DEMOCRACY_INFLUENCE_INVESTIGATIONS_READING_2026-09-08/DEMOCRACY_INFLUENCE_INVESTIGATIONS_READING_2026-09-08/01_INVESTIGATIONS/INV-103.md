ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260906-1451-defiance-institutionnelle-francaise | PARENT_RUN_ID:NONE | AS_OF:2026-09-06
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/truth-engine/investigations/2026-09/2026-09-06_defiance-institutionnelle-francaise/2026-09-06_14-51_defiance-institutionnelle-francaise_INPUT.md | SUBJECT_SLUG:defiance-institutionnelle-francaise | SUBJECT_FP:sha256:2704c43ef8b2f857e321368bc34ca012f78a77d9e0b4f416f262655ef7e4d760 | INPUT_SHA256:sha256:9b5bee0c0312885ec7574edc58274ef80c4362376620424e90aedd3045d6a7c7
COMPLEXITY:7→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['Presidency', 'Government', 'Assemblée nationale', 'parties', 'mayors/local authorities', 'media', 'justice', 'police', 'gendarmerie', 'army', 'hospitals', 'social security'], 'domains': ['national politics', 'local politics', 'democracy', 'media', 'justice', 'police/gendarmerie/army', 'health/social protection'], 'exclusions': ['generic anti-institutional aggregate without institution-level decomposition', 'causal claims unsupported by identification design'], 'geo': 'France; Germany/Italy/UK/OECD comparators where methodologically valid', 'lead_question': 'N/A(NO_INPUT_LEAD)', 'limits': ['public survey/analysis evidence', 'different survey question scales are not numerically interchangeable', 'observational regressions establish associations, not general causality'], 'object_question': 'Comment la confiance et la défiance se distribuent-elles réellement entre institutions en France, comment ont-elles évolué, et quelles causes sont soutenues par des preuves plutôt que par de simples corrélations ?', 'period': '2010-2026, focus 2020-2026'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Résultat technique

`CLM-001` est le résultat central : les données ne soutiennent pas un agrégat uniforme de « défiance envers les institutions ». `FCT-001`, `FCT-002` et `FCT-012` séparent nettement les institutions politiques nationales et les médias, situés au bas de l'échelle de confiance, des institutions de proximité, de soin et de protection, nettement plus hautes. `CTRL-001` montre que cette hiérarchie survit à un changement d'instrument entre CEVIPOF et OCDE, sans fusionner leurs pourcentages.

`CLM-002` et `CLM-003` bornent la lecture temporelle. `FCT-005` documente une dégradation longue de plusieurs acteurs politiques, tandis que `FCT-006` documente des trajectoires hétérogènes hors politique : police en hausse sur le long terme, justice approximativement stable, armée stable, médias bas mais non en effondrement continu, hôpitaux élevés malgré un recul historique. La formule correcte est donc une crise concentrée de représentation et de performance démocratique, pas un effondrement homogène de toute confiance institutionnelle.

`CLM-004` distingue le régime de sa performance. `FCT-003` établit la baisse de l'évaluation du fonctionnement démocratique jusqu'à 23 % en 2026, tandis que `FCT-015` maintient un attachement à la démocratie de 82 %. Le faible jugement de performance ne vaut pas rejet du principe démocratique.

`CLM-005` et `CLM-006` séparent deux institutions régaliennes souvent agrégées. `FCT-007` montre un écart police-justice particulièrement large en France. `FCT-008` montre aussi que la confiance policière a subi une baisse temporaire avant de remonter, ce qui contredit une causalité mécanique « controverse -> effondrement durable » au niveau agrégé. La justice reste durablement à un niveau intermédiaire-bas, sans rupture récente comparable à la politique nationale.

Les mécanismes restent volontairement bornés. `CLM-007` et `CAU-001..004` retiennent comme associations documentées la voix politique, la position sociale subjective, l'efficacité et les moyens perçus pour la justice, ainsi que l'honnêteté, l'efficacité et le respect perçus pour la police. Les régressions et écarts de groupes examinés ne fournissent pas de stratégie d'identification suffisante pour attribuer un effet causal général. Ces liens restent donc `UNRESOLVED` au titre `CAUSALITY` plutôt que promus par inférence narrative.

`CLM-008` confirme enfin une confiance médiatique basse. `FCT-001` et `FCT-014` convergent directionnellement à 29 %, mais `CTRL-001` impose la même garde méthodologique : identité numérique entre instruments ne signifie pas identité de mesure.

# Limites matérielles

La famille CEVIPOF domine la profondeur longitudinale française ; l'OCDE et le Reuters Institute servent de contrôles indépendants sur des objets partiellement comparables. Les pourcentages issus de questions/échelles différentes ne sont jamais fusionnés. Les gaps causaux `CAU-001..004` ne sont pas résolubles par accumulation de recherches descriptives supplémentaires : leur fermeture demanderait des données longitudinales ou des designs causaux adaptés.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:0|EDI_DECISIVE:3|SRC_COMPLETE:8/8

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-06
- **focus:** 2020-2026
- **latest_observations:** CEVIPOF field Jan 2026; OECD field Sep-Oct 2025 published Jun 2026; Reuters DNR Jun 2026
- **period:** 2010-2026
- **refresh_rule:** recheck next annual wave before reuse after 2026

### MANIPULATION_REPORT
- **assumptions:**
  - survey responses measure reported trust under each instrument definition
  - different question scales are not numerically interchangeable
- **clusters:**
  - NONE
- **complexity:**
  - **band:** COMPLEX
  - **score:** 7
- **implicit:**
  - avoid treating institution trust as one scalar
  - avoid causal upgrade from regression
- **input_kind:** TOPIC
- **mission_mode:** INVESTIGATION
- **patterns:**
  - aggregate-decomposition
  - longitudinal-comparison
  - cross-instrument-control
- **priorities:**
  - institution-level distribution
  - longitudinal direction
  - peer comparators
  - causal boundary
- **query_guidance:**
  - prefer primary survey series
  - seek independent instrument robustness
  - seek regression/model details for determinant claims
- **rhetorical:**
  - NONE
- **speaker:** N/A(TOPIC)
- **symbol_stage:** FINAL
- **symbols:**
  - **Κ:** 0
  - **Λ:** 3
  - **Ξ:** 3
  - **Σ:** 0
  - **Φ:** 0
  - **Ψ:** 0
  - **Ω:** 0
  - **κ:** 0
  - **ρ:** 1
  - **€:** 0
  - **↕:** 2
  - **⏰:** 4
  - **⚔:** 0
  - **⫸:** 2
  - **🌐:** 0
- **threats:**
  - NONE

### MODULE_EXECUTION
NONE

### SCOPING_REPORT
- **actor_network_applicable:** false
- **decomposed_domains:**
  - national politics
  - local politics
  - democratic performance
  - media/news
  - justice
  - police/gendarmerie/army
  - health/social protection
- **exclusions:**
  - no generic aggregate distrust score
  - no exact cross-instrument percentage merging
  - no causal attribution without identification design
- **geo:** France; selected peers only under comparable instruments
- **object_question:** Comment la confiance et la défiance se distribuent-elles réellement entre institutions en France, comment ont-elles évolué, et quelles causes sont soutenues par des preuves plutôt que par de simples corrélations ?
- **period:** 2010-2026; focus 2020-2026
- **resource_flows_applicable:** false
- **responsibility_attribution_applicable:** false

### CREDO
- Institution-specific before aggregate.
- Longitudinal before collapse language.
- Same-instrument comparisons before cross-instrument exact percentages.
- Association is not causality.
- Negative and stable trajectories are material evidence.

### COGNITIVE_MAP
- **causal_boundary:** reviewed surveys/regressions support association and temporal ordering, not general causal effect sizes
- **core_model:** institution domain + level of proximity/service/protection + political responsiveness/performance perceptions -> reported trust distribution; causal arrows remain bounded unless identified
- **observed_structure:**
  - national political representation low
  - local/proximity higher
  - care/protection high
  - justice mid-low and stable
  - media low
  - democratic attachment high while performance evaluation low
- **rival_models:**
  - generalized all-institution collapse
  - single anti-state latent factor
  - controversy mechanically causes durable police distrust
  - low democratic performance equals rejection of democracy

### DIALECTICAL_MAP
- **item 1:**
  - **evidence:**
    - CLM-001
    - CTRL-001
    - CTRL-003
  - **hypothesis:** generalized institutional distrust
  - **result:** CONTRADICTED_AS_AGGREGATE
- **item 2:**
  - **evidence:**
    - CLM-002
    - FCT-005
    - FCT-012
  - **hypothesis:** political-representation-specific distrust
  - **result:** SUPPORTED
- **item 3:**
  - **evidence:**
    - CLM-006
    - FCT-008
  - **hypothesis:** police legitimacy collapsed in aggregate
  - **result:** NOT_SUPPORTED
- **item 4:**
  - **evidence:**
    - CLM-004
    - FCT-015
  - **hypothesis:** democracy itself rejected
  - **result:** NOT_SUPPORTED
- **item 5:**
  - **evidence:**
    - CLM-007
    - CAU-001
    - CAU-002
    - CAU-003
  - **hypothesis:** measured associations are sufficient causal proof
  - **result:** REFUSED

### RESOURCE_FLOW_MAP
NONE

### ACTOR_NETWORK_MAP
NONE

### IMPACT_MAP
- **distributional_note:** the main empirical impact is a highly uneven trust map, not one aggregate institutional rejection
- **measured_outcomes:**
  - reported trust by institution
  - reported democratic functioning
  - reported news trust
- **not_established:**
  - behavioral withdrawal caused by distrust
  - vote choice caused by trust
  - institutional performance caused by trust
  - general causal effect of political voice/perceived qualities

### CONTRADICTION_LEDGER
- **item 1:**
  - **claim:** défiance envers les institutions is uniformly high
  - **counter:**
    - FCT-001
    - FCT-002
    - FCT-012
  - **resolution:** REJECT_UNIFORM_AGGREGATE
- **item 2:**
  - **claim:** police trust is in durable aggregate collapse
  - **counter:**
    - FCT-006
    - FCT-008
    - FCT-012
  - **resolution:** REJECT_DURABLE_COLLAPSE
- **item 3:**
  - **claim:** attachment to democracy is low because democratic performance is low
  - **counter:**
    - FCT-003
    - FCT-015
  - **resolution:** SEPARATE_REGIME_ATTACHMENT_FROM_PERFORMANCE
- **item 4:**
  - **claim:** same numerical percentage across surveys means same measurement
  - **counter:**
    - FCT-001
    - FCT-014
  - **resolution:** REJECT_SCALE_EQUIVALENCE

### VERIFICATION_REPORT
- **causal_assessment:** no reviewed source provides a design sufficient to identify the general causal effects claimed by CAU-001..004
- **cross_instrument_control:** OECD 2025 reproduces the political/local/police hierarchy without merging exact scales
- **exact_fetch_trace_for_all_web_sources:** true
- **facts:** 15
- **known_limit:** CEVIPOF dominates the longitudinal French evidence family
- **sources:** 8
- **tier_policy:** all concrete facts retained at probable tier; no confirmed tier forced from same-family repetition
- **upstream_families:**
  - other:cevipof
  - other:oecd
  - other:reuters-institute

### EDI_REPORT
- **corpus:**
  - **circularity:** CEVIPOF family supplies 6/8 accepted sources but distinct wave/analysis objects
  - **counters:** 3
  - **coverage:** 1.0
  - **direct_objects:** 4
  - **edi_star:** 0.725
  - **independence:** 0.375
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **credible_counter:** TESTED_OECD
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 2
  - **item 2:**
    - **claim_id:** CLM-004
    - **credible_counter:** NONE_FOUND
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 1
  - **item 3:**
    - **claim_id:** CLM-007
    - **credible_counter:** METHODOLOGICAL_LIMIT
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** CAUSALITY
    - **independent_families:** 2
- **diagnostic_not_truth:** true
- **dimensions:**
  - **geo:** 0.85
  - **lang:** 1.0
  - **owner:** 0.65
  - **persp:** N/A(methodological object; actor-position balance not a truth proxy here)
  - **strat:** 0.62
  - **temp:** 1.0
- **edi:**
  - **final:** 0.7
  - **flags:**
    - OWNERSHIP_CONCENTRATION:CEVIPOF_UPSTREAM_FAMILY
  - **penalties:** 0.1
  - **raw:** 0.8
- **source_counts:**
  - **other:** 0
  - **primary:** 4
  - **secondary:** 4
  - **total:** 8

### RESPONSIBILITY_MAP
NONE

### NEXT_QUERIES
- **item 1:**
  - **query:** recompute institution hierarchy and longitudinal deltas without merging instruments
  - **trigger:** new CEVIPOF/OECD wave or material methodology revision
- **item 2:**
  - **query:** require panel, experiment, natural experiment or other identified causal design before upgrading CAU-001..003
  - **trigger:** future source claims causal effect of voice/responsiveness or perceived institutional qualities
- **item 3:**
  - **query:** recheck current police series and subgroup heterogeneity rather than infer from salient controversies
  - **trigger:** future claim of aggregate police legitimacy collapse

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-002,QRY-008,QRY-009,QRY-010,QRY-014 | support:- | counter:- | results:FCT-001,FCT-002,FCT-005,FCT-006,FCT-012 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-004,QRY-005,QRY-006,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-013 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-002,QRY-009,QRY-010 | support:- | counter:- | results:FCT-002,FCT-003,FCT-005,FCT-006 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-008,QRY-009,QRY-014,QRY-015 | support:- | counter:- | results:FCT-001,FCT-002,FCT-012,FCT-014,FCT-015 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-006,QRY-014 | support:- | counter:- | results:FCT-012,FCT-013 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-004,QRY-011,QRY-012 | support:- | counter:- | results:FCT-007,FCT-009,FCT-010 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-003,QRY-005,QRY-011,QRY-013 | support:- | counter:- | results:FCT-007,FCT-008,FCT-011 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-006,QRY-010,QRY-014 | support:- | counter:- | results:FCT-006,FCT-012 | final:SATURATED | gap:NONE
AXS-007 | attempts:QRY-009,QRY-011 | support:- | counter:- | results:FCT-004,FCT-007 | final:SATURATED | gap:NONE
AXS-008 | attempts:QRY-012,QRY-013,QRY-014,QRY-015 | support:- | counter:- | results:FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-008,QRY-009,QRY-010,QRY-014,SRC-001,SRC-002,SRC-003,SRC-007 | support:FCT-001,FCT-002,FCT-006,FCT-012 | counter:- | results:FCT-001,FCT-002,FCT-006,FCT-012 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-009,QRY-010,SRC-002,SRC-003 | support:FCT-003,FCT-005,FCT-006 | counter:FCT-005(parties are a long-run exception) | results:FCT-003,FCT-005,FCT-006,FCT-005(parties are a long-run exception) | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-008,QRY-010,QRY-011,SRC-001,SRC-003,SRC-004 | support:FCT-001,FCT-006,FCT-008 | counter:FCT-006(hospitals declined from 83% to 75% by 2024) | results:FCT-001,FCT-006,FCT-008,FCT-006(hospitals declined from 83% to 75% by 2024) | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-008,QRY-009,SRC-001,SRC-002 | support:FCT-003,FCT-004,FCT-015 | counter:- | results:FCT-003,FCT-004,FCT-015 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-010,QRY-011,QRY-012,QRY-014,SRC-003,SRC-004,SRC-005,SRC-007 | support:FCT-006,FCT-007,FCT-009,FCT-010,FCT-012 | counter:- | results:FCT-006,FCT-007,FCT-009,FCT-010,FCT-012 | final:SUPPORTED | gap:NONE
CLM-006 | attempts:QRY-008,QRY-011,QRY-013,QRY-014,SRC-001,SRC-004,SRC-006,SRC-007 | support:FCT-001,FCT-007,FCT-008,FCT-011,FCT-012 | counter:FCT-008(temporary 2018-2020 decline) | results:FCT-001,FCT-007,FCT-008,FCT-011,FCT-012,FCT-008(temporary 2018-2020 decline) | final:SUPPORTED | gap:NONE
CLM-007 | attempts:QRY-012,QRY-013,QRY-014,SRC-005,SRC-006,SRC-007 | support:FCT-009,FCT-010,FCT-011,FCT-013 | counter:- | results:FCT-009,FCT-010,FCT-011,FCT-013 | final:PARTIAL | gap:CAUSALITY
CLM-008 | attempts:QRY-008,QRY-015,SRC-001,SRC-008 | support:FCT-001,FCT-014 | counter:- | results:FCT-001,FCT-014 | final:PARTIAL | gap:SCOPE

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-007 | CLM | PARTIAL | CAUSALITY | Cross-sectional and observational models remain vulnerable to reverse causality, common causes and conceptual overlap between evaluations and trust; stronger causal designs were not present in the reviewed sources.
CLM-008 | CLM | PARTIAL | SCOPE | CEVIPOF institution trust and Reuters Institute news trust use different questions/scales; only the low-trust direction is robust across instruments.
CAU-001 | CAU | UNRESOLVED | CAUSALITY | No reviewed design isolates the causal effect of political voice/responsiveness on trust.
CAU-002 | CAU | UNRESOLVED | CAUSALITY | No reviewed causal identification establishes direction or effect size.
CAU-003 | CAU | UNRESOLVED | CAUSALITY | No reviewed causal identification establishes direction or effect size.
CAU-004 | CAU | UNRESOLVED | CAUSALITY | Event-specific causal decomposition not established.

SEMANTIC_COUNTS_V1:LED:2|CLM:8|AXS:8|CAU:4|CTRL:3|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-008","QRY-009","QRY-010","QRY-014"],"evidence_excerpt":"éviter l’agrégat vague defiance envers les institutions","kind":"HYPOTHESIS","lead":"The vague aggregate distrust of institutions may conceal materially different trust regimes by institution.","linked_ids":["AXS-001","AXS-002","AXS-006","CLM-001"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-005","FCT-006","FCT-012"],"routes":["OBJECT_INVESTIGATION","SCOPE_HISTORY","COUNTER_HYPOTHESES"],"source_id":"INV-103_RUN_CARD","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-004","QRY-005","QRY-006","QRY-011","QRY-012","QRY-013","QRY-014"],"evidence_excerpt":"quelles causes sont soutenues par des preuves plutôt que par de simples corrélations","kind":"METHOD_CONSTRAINT","lead":"Candidate explanations for distrust must be separated into supported associations versus identified causal effects.","linked_ids":["AXS-003","AXS-004","AXS-005","AXS-008","CLM-007"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-013"],"routes":["MECHANISMS","COUNTER_HYPOTHESES","RULES_CONTROLS"],"source_id":"INV-103_RUN_CARD","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"French institutional distrust is not a uniform aggregate: national political institutions and media are low-trust while proximity, care and protection institutions retain substantially higher trust.","claimant":"INV-103 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-006","FCT-012"]}
CLM-002 | {"claim":"The long-run decline is concentrated in national/political representation rather than across all institutions.","claimant":"INV-103 synthesis","counter":"FCT-005(parties are a long-run exception)","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-003","FCT-005","FCT-006"]}
CLM-003 | {"claim":"Protection and care institutions remain high-trust, with police and army stable or resilient over the long run while hospitals remain high despite some decline from the 2009 baseline.","claimant":"INV-103 synthesis","counter":"FCT-006(hospitals declined from 83% to 75% by 2024)","gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-001","FCT-006","FCT-008"]}
CLM-004 | {"claim":"Attachment to democracy and evaluation of democratic performance diverge sharply: attachment remains high while the share saying democracy works well fell to 23% in 2026.","claimant":"INV-103 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-003","FCT-004","FCT-015"]}
CLM-005 | {"claim":"Justice trust is durably low-to-middling rather than a newly collapsing series; France also shows a much larger police-justice trust gap than selected peers.","claimant":"INV-103 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-006","FCT-007","FCT-009","FCT-010","FCT-012"]}
CLM-006 | {"claim":"Aggregate trust in police is high and resilient; therefore a claim of generalized aggregate police-legitimacy collapse is not supported by the trust series.","claimant":"INV-103 synthesis","counter":"FCT-008(temporary 2018-2020 decline)","gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-001","FCT-007","FCT-008","FCT-011","FCT-012"]}
CLM-007 | {"claim":"Political voice/responsiveness, subjective social position, perceived effectiveness/means, honesty and respect are strongly associated with institution-specific trust, but the reviewed evidence does not identify their general causal effect.","claimant":"INV-103 synthesis","counter":"NONE_FOUND","gap":"Cross-sectional and observational models remain vulnerable to reverse causality, common causes and conceptual overlap between evaluations and trust; stronger causal designs were not present in the reviewed sources.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-009","FCT-010","FCT-011","FCT-013"]}
CLM-008 | {"claim":"Media/news trust is genuinely low in 2026, and two differently worded instruments both report 29%; the identical percentage must not be treated as measurement identity.","claimant":"INV-103 synthesis","counter":"NONE_FOUND","gap":"CEVIPOF institution trust and Reuters Institute news trust use different questions/scales; only the low-trust direction is robust across instruments.","gap_type":"SCOPE","materiality":"IMPORTANT","status":"PARTIAL","support":["FCT-001","FCT-014"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-002","QRY-009","QRY-010"],"axis":"SCOPE_HISTORY","links":["CLM-001","CLM-002","CLM-003"],"question":"How did institution-specific trust evolve from the 2009/2010 baseline to 2026?","result_ids":["FCT-002","FCT-003","FCT-005","FCT-006"],"sought_objects":["longitudinal CEVIPOF series","current 2026 wave"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-008","QRY-009","QRY-014","QRY-015"],"axis":"EVIDENCE_CASES","links":["CLM-001","CLM-008"],"question":"What is the current 2025-2026 trust distribution across political, local, media, justice, security and care institutions?","result_ids":["FCT-001","FCT-002","FCT-012","FCT-014","FCT-015"],"sought_objects":["CEVIPOF wave 17","OECD Trust Survey France 2025","Reuters Institute France 2026"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-006","QRY-014"],"axis":"MECHANISMS_POLITICAL","links":["CLM-007","CAU-001"],"question":"Which measured factors are associated with low national-political trust?","result_ids":["FCT-012","FCT-013"],"sought_objects":["political voice trust gaps","responsiveness/performance indicators"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-004","QRY-011","QRY-012"],"axis":"MECHANISMS_JUSTICE","links":["CLM-005","CAU-002"],"question":"Which measured factors are associated with trust in justice?","result_ids":["FCT-007","FCT-009","FCT-010"],"sought_objects":["justice-trust regression","perceived institutional qualities"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-003","QRY-005","QRY-011","QRY-013"],"axis":"MECHANISMS_POLICE","links":["CLM-006","CAU-003","CAU-004"],"question":"Which measured factors are associated with trust in police, and is controversy followed by durable collapse?","result_ids":["FCT-007","FCT-008","FCT-011"],"sought_objects":["police-trust regression","longitudinal police series"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-006","QRY-010","QRY-014"],"axis":"COUNTER_HYPOTHESES","links":["CLM-001","CTRL-001","CTRL-003"],"question":"Does an independent survey instrument reproduce the generalized-distrust hypothesis or the differentiated hierarchy?","result_ids":["FCT-006","FCT-012"],"sought_objects":["OECD cross-institution hierarchy","historical counterexamples"],"status":"SATURATED"}
AXS-007 | {"attempt_ids":["QRY-009","QRY-011"],"axis":"COMPARATORS","links":["CLM-004","CLM-005","CTRL-002"],"question":"How does France compare with peer countries where the same instrument permits comparison?","result_ids":["FCT-004","FCT-007"],"sought_objects":["democracy functioning comparators","police-justice gap comparators"],"status":"SATURATED"}
AXS-008 | {"attempt_ids":["QRY-012","QRY-013","QRY-014","QRY-015"],"axis":"RULES_CONTROLS","links":["CLM-007","CLM-008","CTRL-001"],"question":"Which methodological boundaries prevent false exact comparisons or causal overclaiming?","result_ids":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014"],"sought_objects":["survey wording/scales","observational regression limits","cross-source media check"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"NONE_FOUND","gap":"No reviewed design isolates the causal effect of political voice/responsiveness on trust.","gap_type":"CAUSALITY","limit":"Observed trust gap is cross-sectional/associational; political trust can also shape perceived voice.","mechanism":"Perceived lack of political voice/responsiveness -> lower national-government trust","status":"UNRESOLVED","support":["FCT-013"]}
CAU-002 | {"counter":"NONE_FOUND","gap":"No reviewed causal identification establishes direction or effect size.","gap_type":"CAUSALITY","limit":"Regression identifies association, not exogenous treatment; perceptions may be partly downstream of trust.","mechanism":"Subjective social position and perceived justice effectiveness/means -> justice trust","status":"UNRESOLVED","support":["FCT-009","FCT-010"]}
CAU-003 | {"counter":"NONE_FOUND","gap":"No reviewed causal identification establishes direction or effect size.","gap_type":"CAUSALITY","limit":"Predictors and trust are measured observationally and may share latent evaluations.","mechanism":"Perceived police honesty/effectiveness/respect -> police trust","status":"UNRESOLVED","support":["FCT-011"]}
CAU-004 | {"counter":["FCT-008"],"gap":"Event-specific causal decomposition not established.","gap_type":"CAUSALITY","limit":"A temporary fall followed by recovery rejects a simple mechanical durable-collapse story but does not identify the causal contribution of each event.","mechanism":"Major police controversies -> durable aggregate police distrust","status":"UNRESOLVED","support":["FCT-008"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Cross-instrument hierarchy control: OECD 2025 and CEVIPOF 2026 use different scales but both place police/local administration well above national government/parties.","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-012"]}
CTRL-002 | {"control":"Same-instrument peer control: CEVIPOF shows France markedly lower on democratic functioning and a much larger police-justice gap than Germany/UK within the compared questions.","status":"SUPPORTED","support":["FCT-004","FCT-007"]}
CTRL-003 | {"control":"Longitudinal counter-control: police rises and justice is roughly stable across long windows, falsifying a blanket all-institutions collapse narrative.","status":"SUPPORTED","support":["FCT-006","FCT-008"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:7|FETCH:8|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"EMPTY","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"EMPTY","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"EMPTY","RESPONSIBILITY_MAP":"EMPTY","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | subject-fp lookup | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | investigation-summary | MNEMO_S
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
SYS-005 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | snapshot:v1 | SNAPSHOT_MEMORY_WRITE
QRY-001 | WEB | FOUND | - | - | CEVIPOF 2026 confiance institutions France
QRY-002 | WEB | FOUND | - | - | CEVIPOF 2009 2024 confiance acteurs institutions
QRY-003 | WEB | FOUND | - | - | CEVIPOF confiance police justice 2026 France
QRY-004 | WEB | FOUND | - | - | CEVIPOF confiance justice 2023 régression
QRY-005 | WEB | FOUND | - | - | CEVIPOF confiance police 2022 régression
QRY-006 | WEB | FOUND | - | - | OECD France trust public institutions 2026 political voice
QRY-007 | WEB | FOUND | - | - | Reuters Institute Digital News Report 2026 France trust news 29 percent
QRY-008 | FETCH | FOUND | SRC-001 | https://www.sciencespo.fr/cevipof/fr/actualites/barometre-de-la-confiance-politique-cevipof-2026-la-confiance-s-effondre-en-politique-la-proximite-fait-figure-de-refuge/ | FETCH CEVIPOF Baromètre confiance politique vague 17 actualité 9 février 2026
QRY-009 | FETCH | FOUND | SRC-002 | https://www.sciencespo.fr/cevipof/sites/sciencespo.fr.cevipof/files/Barometre_confiance_CEVIPOFVague17_fev2026_vd1.pdf | FETCH CEVIPOF Baromètre confiance politique vague 17 résultats complets
QRY-010 | FETCH | FOUND | SRC-003 | https://www.sciencespo.fr/cevipof/sites/sciencespo.fr.cevipof/files/Bilan%2015ans%20Baro_FC_BD.pdf | FETCH CEVIPOF bilan 15 ans baromètre confiance politique
QRY-011 | FETCH | FOUND | SRC-004 | https://www.sciencespo.fr/cevipof/fr/actualites/pourquoi-les-francais-font-ils-davantage-confiance-a-la-police-qu-a-la-justice/ | FETCH CEVIPOF police justice 27 août 2026
QRY-012 | FETCH | FOUND | SRC-005 | https://www.sciencespo.fr/cevipof/sites/sciencespo.fr.cevipof/files/NoteBaroV14_LR_confiancedanslajustice_mai2023_VF-1.pdf | FETCH CEVIPOF confiance dans la justice mai 2023
QRY-013 | FETCH | FOUND | SRC-006 | https://www.sciencespo.fr/cevipof/sites/sciencespo.fr.cevipof/files/NoteBaroV13_LR_confiancepolice_juin2022_VF.pdf | FETCH CEVIPOF confiance dans la police juin 2022
QRY-014 | FETCH | FOUND | SRC-007 | https://www.oecd.org/fr/publications/2026/06/oecd-survey-on-drivers-of-trust-in-public-institutions-2026-results-country-notes_6dae3a76/france_8cc554a8.html | FETCH OECD résultats 2026 confiance institutions France
QRY-015 | FETCH | FOUND | SRC-008 | https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026/france | FETCH Reuters Institute Digital News Report 2026 France

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:other:cevipof | CEVIPOF-BCP-W17-NEWS-2026 | Baromètre de la confiance politique CEVIPOF 2026 : la confiance s’effondre en politique, la proximité fait figure de refuge | 2026-02-09 | 2026-09-06T13:02:57Z | article; headline metrics and democracy attachment | https://www.sciencespo.fr/cevipof/fr/actualites/barometre-de-la-confiance-politique-cevipof-2026-la-confiance-s-effondre-en-politique-la-proximite-fait-figure-de-refuge/
SRC-002 | ◈ | fam:other:cevipof | CEVIPOF-BCP-W17-RESULTS-2026 | Baromètre de la confiance politique - Vague 17 - Résultats | 2026-02-09 | 2026-09-06T13:02:57Z | pp.29,36,40,43; longitudinal and institution charts | https://www.sciencespo.fr/cevipof/sites/sciencespo.fr.cevipof/files/Barometre_confiance_CEVIPOFVague17_fev2026_vd1.pdf
SRC-003 | ◈ | fam:other:cevipof | CEVIPOF-BCP-RETRO-2009-2024 | 15 ans de confiance politique : bilan du Baromètre | 2024 (exact day not stated in retrieved PDF) | 2026-09-06T13:02:57Z | pp.5-7; actor and institution long-run comparisons | https://www.sciencespo.fr/cevipof/sites/sciencespo.fr.cevipof/files/Bilan%2015ans%20Baro_FC_BD.pdf
SRC-004 | ◉ | fam:other:cevipof | CEVIPOF-FARDE-POLICE-JUSTICE-2026 | Pourquoi les Français font-ils davantage confiance à la police qu’à la justice ? | 2026-08-27 | 2026-09-06T13:02:57Z | article; 2026 police/justice gap and longitudinal interpretation | https://www.sciencespo.fr/cevipof/fr/actualites/pourquoi-les-francais-font-ils-davantage-confiance-a-la-police-qu-a-la-justice/
SRC-005 | ◉ | fam:other:cevipof | CEVIPOF-BCP-W14-JUSTICE-2023 | La confiance dans la justice comme test démocratique | 2023-05 | 2026-09-06T13:02:57Z | pp.1-6; regressions and perceived qualities | https://www.sciencespo.fr/cevipof/sites/sciencespo.fr.cevipof/files/NoteBaroV14_LR_confiancedanslajustice_mai2023_VF-1.pdf
SRC-006 | ◉ | fam:other:cevipof | CEVIPOF-BCP-W13-POLICE-2022 | Méfiance et confiance dans la police : une analyse sociologique | 2022-06 | 2026-09-06T13:02:57Z | pp.10-11; logistic regressions and endogenous evaluations | https://www.sciencespo.fr/cevipof/sites/sciencespo.fr.cevipof/files/NoteBaroV13_LR_confiancepolice_juin2022_VF.pdf
SRC-007 | ◈ | fam:other:oecd | OECD-TRUST-2026-FRANCE | Résultats 2026 de l’enquête de l’OCDE sur les déterminants de la confiance dans les institutions publiques : France | 2026-06-29 | 2026-09-06T13:02:57Z | Trust in public institutions; trust gaps; 2025 field results | https://www.oecd.org/fr/publications/2026/06/oecd-survey-on-drivers-of-trust-in-public-institutions-2026-results-country-notes_6dae3a76/france_8cc554a8.html
SRC-008 | ◉ | fam:other:reuters-institute | RISJ-DNR-2026-FRANCE | Digital News Report 2026 - France | 2026-06-16 | 2026-09-06T13:02:57Z | France country page; overall news trust and methodology | https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026/france

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.sciencespo.fr/cevipof/fr/actualites/barometre-de-la-confiance-politique-cevipof-2026-la-confiance-s-effondre-en-politique-la-proximite-fait-figure-de-refuge/ | other:cevipof | 2026-02-09 | France 2026 headline trust split | CEVIPOF wave 17 reports trust in politics at 22%; hospitals 79%, gendarmerie 77%, army 75%, police 73%, social security 68%, media 29%; attachment to democracy 82%. | -
FCT-002 | FACT | ✧ | https://www.sciencespo.fr/cevipof/sites/sciencespo.fr.cevipof/files/Barometre_confiance_CEVIPOFVague17_fev2026_vd1.pdf | other:cevipof | 2026-01 | France 2026 political institution hierarchy | Wave 17 chart: municipal council 58%, departmental council 49%, regional council 46%, Court of Audit 44%, Constitutional Council 36%, CESE 33%, EU 29%, Senate 26%, European Parliament 25%, Presidency 22%, National Assembly 20%, Government 17%. | -
FCT-003 | FACT | ✧ | https://www.sciencespo.fr/cevipof/sites/sciencespo.fr.cevipof/files/Barometre_confiance_CEVIPOFVague17_fev2026_vd1.pdf | other:cevipof | 2026-01 | Democracy functioning trend France 2020-2026 | Share saying democracy functions well in France: 35% Feb 2020, 42% Feb 2021, 35% Feb 2023, 31% Jan 2024, 28% Jan 2025, 23% Jan 2026. | -
FCT-004 | FACT | ✧ | https://www.sciencespo.fr/cevipof/sites/sciencespo.fr.cevipof/files/Barometre_confiance_CEVIPOFVague17_fev2026_vd1.pdf | other:cevipof | 2026-01 | Democracy functioning comparators 2026 | Wave 17 chart reports democracy functioning well at 23% France versus 52% Germany, 40% Italy and 54% United Kingdom; exact cross-country percentages are used only within this common instrument. | -
FCT-005 | FACT | ✧ | https://www.sciencespo.fr/cevipof/sites/sciencespo.fr.cevipof/files/Bilan%2015ans%20Baro_FC_BD.pdf | other:cevipof | 2024 | Long-run trust in political actors 2009-2024 | CEVIPOF retrospective reports mayor 65% to 60%, département 54% to 47%, région 53% to 45%, député 47% to 39%, Prime Minister 38% to 35%, President 32% to 29%; parties are an exception, 14% to 20%. | -
FCT-006 | FACT | ✧ | https://www.sciencespo.fr/cevipof/sites/sciencespo.fr.cevipof/files/Bilan%2015ans%20Baro_FC_BD.pdf | other:cevipof | 2024 | Long-run trust in non-political institutions | CEVIPOF retrospective shows heterogeneous long-run paths: police 63% in 2009 to 70% in 2024; justice 45% in 2012 and 45% in 2024; army about 73% in 2012 and 2024; hospitals 83% in 2009 to 75% in 2024; media 24% in 2009 to 28% in 2024. | -
FCT-007 | FACT | ✧ | https://www.sciencespo.fr/cevipof/fr/actualites/pourquoi-les-francais-font-ils-davantage-confiance-a-la-police-qu-a-la-justice/ | other:cevipof | 2026-08-27 | Police versus justice trust gap 2026 | CEVIPOF reports France 2026 police trust at 73% versus justice 45%; Germany 72% versus 63% and United Kingdom 61% versus 60%, making the French police-justice gap unusually large in these comparators. | -
FCT-008 | FACT | ✧ | https://www.sciencespo.fr/cevipof/fr/actualites/pourquoi-les-francais-font-ils-davantage-confiance-a-la-police-qu-a-la-justice/ | other:cevipof | 2026-08-27 | Police trust rebound after 2018-2020 decline | Police trust fell from 74% in December 2018 to 66% in February 2020, then recovered to 73% in 2026; controversy does not map mechanically to a durable aggregate collapse. | -
FCT-009 | FACT | ✧ | https://www.sciencespo.fr/cevipof/sites/sciencespo.fr.cevipof/files/NoteBaroV14_LR_confiancedanslajustice_mai2023_VF-1.pdf | other:cevipof | 2023-05 | Justice trust social-position association | CEVIPOF wave 14 logistic analysis reports subjective social position as the strongest exogenous correlate of justice trust; objective occupational category, diploma and generation are not significant in the same way, and recent personal justice experience has no detected effect in that model. | -
FCT-010 | FACT | ✧ | https://www.sciencespo.fr/cevipof/sites/sciencespo.fr.cevipof/files/NoteBaroV14_LR_confiancedanslajustice_mai2023_VF-1.pdf | other:cevipof | 2023-05 | Justice trust perceived-quality associations | In the French justice-trust regression using perceived institutional qualities, effectiveness and adequacy of means are the strongest reported associations; the analysis is observational and does not identify a general causal effect. | -
FCT-011 | FACT | ✧ | https://www.sciencespo.fr/cevipof/sites/sciencespo.fr.cevipof/files/NoteBaroV13_LR_confiancepolice_juin2022_VF.pdf | other:cevipof | 2022-06 | Police trust perceived-quality associations | CEVIPOF wave 13 logistic analysis reports perceived honesty first, followed by effectiveness and respect, among the strongest endogenous associations with police trust; this is observational association, not identified causality. | -
FCT-012 | FACT | ✧ | https://www.oecd.org/fr/publications/2026/06/oecd-survey-on-drivers-of-trust-in-public-institutions-2026-results-country-notes_6dae3a76/france_8cc554a8.html | other:oecd | 2026-06-29 | OECD France institution trust 2025 | OECD 2025 France results: national government 22%, police 65%, local administration 52%, courts 45%, civil service 51%, political parties 15%; its 0-10 scale differs from CEVIPOF, so exact percentages are not merged across instruments. | -
FCT-013 | FACT | ✧ | https://www.oecd.org/fr/publications/2026/06/oecd-survey-on-drivers-of-trust-in-public-institutions-2026-results-country-notes_6dae3a76/france_8cc554a8.html | other:oecd | 2026-06-29 | OECD political voice trust gap France 2025 | OECD reports a 42 percentage-point national-government trust gap associated with perceived political voice in France; only 23% report that people like them have a say. The report describes these as trust gaps/associations, not causal identification. | -
FCT-014 | FACT | ✧ | https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026/france | other:reuters-institute | 2026-06-16 | France news trust 2026 | Reuters Institute Digital News Report 2026 reports overall trust in news in France at 29%, unchanged year-on-year, versus a 37% global average; its media-trust measure is not numerically interchangeable with institution-trust questions. | -
FCT-015 | FACT | ✧ | https://www.sciencespo.fr/cevipof/fr/actualites/barometre-de-la-confiance-politique-cevipof-2026-la-confiance-s-effondre-en-politique-la-proximite-fait-figure-de-refuge/ | other:cevipof | 2026-02-09 | Democratic attachment versus performance evaluation | CEVIPOF 2026 reports 82% attachment to democracy while the full wave-17 results show only 23% saying democracy functions well in France, separating regime attachment from performance evaluation. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-002
FCT-004 | SRC-002
FCT-005 | SRC-003
FCT-006 | SRC-003
FCT-007 | SRC-004
FCT-008 | SRC-004
FCT-009 | SRC-005
FCT-010 | SRC-005
FCT-011 | SRC-006
FCT-012 | SRC-007
FCT-013 | SRC-007
FCT-014 | SRC-008
FCT-015 | SRC-001

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

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 LEADS | NEXT_ACTION:7 SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 SCOPE | NEXT_ACTION:9 SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 SEARCH | NEXT_ACTION:10 FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10 FACTS | NEXT_ACTION:11 CAUSAL
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 CAUSAL_GAP | NEXT_ACTION:13 VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 VERIFY | NEXT_ACTION:17 INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:18 FINALIZATION

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-06T13:08:57.034041+00:00","fact_mem":{},"mnemo_row":"BLOCKED:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":15,"eligible":15,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:BLOCKED:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:15;attempted:0;success:0;failure:0;blocked:15} | WRITEBACK_EXECUTION_V1:[15 rows, see section]

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
