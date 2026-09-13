ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260909-1624-arcom-regulation-pluralism | PARENT_RUN_ID:NONE | AS_OF:2026-09-09
INPUT_KIND:RUN_CARD | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/inv074/runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-09_arcom-regulation-pluralism/2026-09-09_16-24_arcom-regulation-pluralism_INPUT.md | SUBJECT_SLUG:arcom-regulation-pluralism | SUBJECT_FP:sha256:639e8addf564655ecedfb06188b4c1ecf4b3881c6a9114684999372bae15b2a4 | INPUT_SHA256:sha256:3230d6d151d7248fdce76c10d871fcb35ae6834744c98fea46dbf18875bf031d
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France, mainly 2019-2026; trace ARCOM mandate/rule -> referral/monitoring -> procedure -> decision/sanction/convention/allocation -> media/platform -> adaptation -> content/access/pluralism -> effect, separating legal regulation, arbitration, editorial incentive, political bias and downstream democratic effect.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/NETWORK.md,clusters/POWER.md,clusters/CONFIRMATION.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Analyse technique

## Delta principal

L’ARCOM n’est pas une infrastructure purement procédurale : elle dispose de pouvoirs matériels de sanction, de contrôle du pluralisme, d’allocation de fréquences et de coordination DSA. Ces pouvoirs produisent des effets observables, notamment financiers pour un éditeur sanctionné et d’accès au marché pour les candidats TNT.

Le corpus ne permet toutefois pas de convertir cette puissance réglementaire en preuve de commandement politique. Les décisions sont encadrées par la loi, graduées, susceptibles de recours et effectivement corrigées ou validées par le Conseil d’État. Les nominations politiques d’une partie du collège sont un fait institutionnel, pas une chaîne de tasking.

## Pluralisme et autonomie éditoriale

La décision du Conseil d’État du 13 février 2024 a obligé l’ARCOM à réexaminer sa lecture du pluralisme concernant CNews. La délibération de juillet 2024 a élargi l’appréciation à l’ensemble des participants, des thèmes et des points de vue sur des fenêtres temporelles longues. Elle maintient néanmoins que les éditeurs choisissent leurs thèmes et intervenants et ne leur impose pas une classification idéologique exhaustive des personnes à l’antenne.

Le réexamen CNews a abouti à une mise en garde et à une demande de mesures de conformité, tandis que la demande portant sur l’indépendance de l’information a été rejetée. Cette gradation contredit l’équivalence automatique entre contrôle du pluralisme et ordre éditorial direct.

## Sanctions et contrôle juridictionnel

La sanction de 3,5 millions d’euros prononcée contre C8 constitue un effet coercitif direct. Le Conseil d’État l’a maintenue en 2024 après contrôle de la légalité et de la proportionnalité. Cette validation ferme le litige considéré, mais ne prouve pas la neutralité politique générale de toutes les décisions de l’ARCOM.

Des mises en demeure ont également visé France Télévisions et France Médias Monde pendant la campagne européenne 2024. Elles fournissent un contrôle négatif contre l’hypothèse d’une absence totale d’intervention envers l’audiovisuel public. Elles ne suffisent pas à établir une symétrie statistique entre secteurs, faute de dénominateurs comparables sur les saisines, les manquements, la gravité et les décisions.

## TNT et accès au marché

La procédure 2024-2025 a directement modifié l’accès à la TNT : C8 et NRJ12 n’ont pas été renouvelées, tandis que de nouveaux services ont obtenu des autorisations. Le Conseil d’État a jugé que les choix comparatifs n’étaient pas illégaux et que l’ARCOM pouvait tenir compte des manquements antérieurs d’un éditeur dans l’évaluation de sa capacité future à respecter ses obligations.

Le même arrêt a imposé une nouvelle étude d’impact et une consultation pour les fréquences devenues vacantes après le retrait tardif de Canal+, montrant que le juge ne valide pas mécaniquement l’ensemble de la procédure et peut imposer des obligations supplémentaires au régulateur.

## Plateformes et DSA

L’ARCOM est le coordinateur français pour les services numériques. Elle peut notamment certifier des signaleurs de confiance. Le mécanisme confère une priorité de traitement aux notifications, mais la décision de retirer ou non un contenu reste du ressort de la plateforme dans ce canal. Pour les obligations de diligence des très grandes plateformes et moteurs de recherche, la Commission européenne conserve une compétence exclusive.

## Plafond causal

Les arêtes suivantes sont supportées : mandat légal vers procédure réglementaire ; décision du Conseil d’État vers réexamen et nouveau cadre de pluralisme ; manquements C8 vers sanction financière confirmée ; procédure TNT vers perte ou gain d’accès hertzien ; certification DSA vers priorité de traitement des notifications.

Restent non établies : instruction politique authentifiée d’un décideur vers une décision ARCOM déterminée ; biais systémique après correction des dénominateurs ; capture éditoriale générale ; effet causal des interventions de l’ARCOM sur l’opinion, le vote ou un résultat électoral.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:6|SRC_COMPLETE:16/16

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-09
- **notes:**
  - ARCOM created 2022 from CSA/Hadopi merger
  - pluralism jurisprudence changed in 2024
  - TNT effects observable from 2025
  - DSA implementation ongoing through 2026
- **status:** CURRENT
- **window:** 2019-2026

### MANIPULATION_REPORT
- **assumptions:**
  - formal regulatory power can alter access without proving political tasking
  - judicial review can constrain but does not guarantee neutrality
  - cross-sector cases do not establish equal treatment rates
- **clusters:**
  - **loaded:**
    - clusters/NETWORK.md
    - clusters/POWER.md
    - clusters/CONFIRMATION.md
- **complexity:**
  - **band:** HIGH
  - **score:** 9
- **implicit:**
  - reviewable coercive power can exist without political tasking
  - procedural autonomy does not prove political neutrality
  - market-access decisions are direct effects even when opinion effects remain unknown
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - regulatory mandate
  - pluralism
  - sanction
  - frequency allocation
  - judicial review
  - platform coordination
  - political-control allegation
- **priorities:**
  - formal mandate
  - decision trace
  - judicial correction
  - market-access effect
  - symmetry denominator
  - downstream causal effect
- **query_guidance:** prioritize official decisions and court review; require denominators for bias and counterfactuals for editorial or democratic effects.
- **rhetorical:**
  - **AUTH:** official regulator and court sources are evidence, not automatic interpretive truth
  - **BF:** trace mandate-procedure-decision-review-effect
  - **DEM:** apply same standard to public and private broadcasters
  - **FAC:** separate legal effect, editorial effect and democratic effect
  - **NUM:** require denominators before symmetry claims
- **speaker:**
  - **goal:** forensic causal discrimination
  - **target:** mandate -> procedure -> decision -> adaptation/access -> pluralism effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **§:** 5
  - **Κ:** 4
  - **Λ:** 4
  - **Ξ:** 5
  - **Σ:** 5
  - **Φ:** 5
  - **Ψ:** 5
  - **Ω:** 4
  - **κ:** 4
  - **ρ:** 4
  - **↕:** 5
  - **⏰:** 5
  - **⚔:** 5
  - **⫸:** 5
  - **🌐:** 5
- **threats:**
  - sanction=censorship
  - appointment=tasking
  - nonrenewal=political purge
  - warning=editorial capture
  - priority notice=removal order
  - case selection=systemic bias

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - downstream editorial effect
  - **input_ids:**
    - FCT-003
    - FCT-012
    - FCT-016
    - FCT-021
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no political tasking inferred
  - **not_computable:**
    - counterfactual pluralism outcome
  - **operations_applied:**
    - separated legal power, market-access effect and downstream democratic effect
  - **reason:** map formal authority and decision effects without motive inflation
  - **result_ids:**
    - CLM-001
    - CLM-005
    - CAU-001
    - CAU-004
  - **status:** DONE
  - **trigger:** ARCOM has sanctions and frequency-allocation powers
- **item 2:**
  - **gaps:**
    - authenticated instruction/tasking
  - **input_ids:**
    - FCT-001
    - FCT-005
    - FCT-023
    - FCT-024
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - appointment not treated as command
    - trusted flagger not treated as removal authority
  - **not_computable:**
    - informal political contacts
  - **operations_applied:**
    - mapped appointment, judicial and platform roles separately
  - **reason:** separate appointing network from case tasking and platform decision rights
  - **result_ids:**
    - CLM-006
    - CAU-005
  - **status:** DONE
  - **trigger:** appointments, courts, broadcasters and DSA actors form a multi-institution chain
- **item 3:**
  - **gaps:**
    - symmetry denominator
  - **input_ids:**
    - FCT-005
    - FCT-011
    - FCT-013
    - FCT-014
    - FCT-015
    - FCT-020
  - **module:** clusters/CONFIRMATION.md
  - **negative_results:**
    - no single-direction enforcement pattern established
  - **not_computable:**
    - population-level bias without denominator
  - **operations_applied:**
    - used judicial and cross-sector counter-cases
  - **reason:** test with judicial corrections, public-broadcaster enforcement and graded measures
  - **result_ids:**
    - CLM-003
    - CLM-004
    - CLM-006
  - **status:** DONE
  - **trigger:** political-arbiter/censorship framing

### SCOPING_REPORT
- **actors_institutions:**
  - ARCOM
  - Conseil d’État
  - private broadcasters
  - public broadcasters
  - TNT candidates
  - European Commission
  - trusted flaggers
  - online platforms
- **domains:**
  - audiovisual pluralism
  - sanctions
  - TNT market access
  - DSA coordination
- **evidence_limits:**
  - no complete intervention denominator by ideology/editor exposure
  - limited post-intervention editorial metrics
  - informal political contacts not observed
- **exclusions:**
  - political motive inferred from appointments
  - censorship inferred from any sanction
  - global neutrality inferred from one court ruling
- **geo:** France
- **period:** 2019-2026

### CREDO
- regulation != political control
- sanction != censorship by default
- appointment != tasking
- compliance != editorial capture
- asymmetry != intent
- decision != downstream democratic effect
- judicial validation != global neutrality
- trusted-flagger priority != removal order

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - mandate
  - pluralism
  - sanction
  - allocation
  - review
  - DSA
- **priorities:**
  - formal power
  - decision trace
  - judicial control
  - cross-sector counter-case
  - effect ceiling
- **query_guidance:** trace one institutional edge at a time; require denominators for bias and counterfactuals for effects.
- **speaker:**
  - **goal:** forensic discrimination
  - **target:** rule -> ARCOM procedure -> decision -> recipient adaptation/access -> pluralism effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **threats:**
  - motive inflation
  - case-selection bias
  - legal-effect/editorial-effect collapse

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** It can impose major sanctions, deny/allocate TNT frequencies and exercise DSA coordinator powers.
  - **support:**
    - FCT-012
    - FCT-021
    - FCT-024
  - **synthesis:** ARCOM has material coercive and allocative power; the remaining question is how that power is constrained and what downstream effects it causes.
  - **thesis:** ARCOM is only a procedural regulator with little material power.
- **item 2:**
  - **antithesis:** Its decisions are reviewable, courts can correct it, public broadcasters are also subject to formal measures, and editors retain topic/guest choice under the pluralism rule.
  - **support:**
    - FCT-005
    - FCT-009
    - FCT-014
    - FCT-015
    - FCT-020
  - **synthesis:** Political-control allegations require tasking or systematic asymmetry evidence beyond appointments and adverse decisions.
  - **thesis:** ARCOM is a political censorship arm.
- **item 3:**
  - **antithesis:** DSA requires priority handling, while providers retain responsibility for deciding notices and the Commission has exclusive VLOP due-diligence competence.
  - **support:**
    - FCT-023
    - FCT-024
  - **synthesis:** ARCOM has an upstream certification/coordinator role, not a general direct-removal power through the trusted-flagger mechanism.
  - **thesis:** Trusted flaggers let ARCOM order platforms to remove content.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **flow:** public spectrum -> call/audition/comparative criteria -> ARCOM authorisation -> terrestrial access/visibility
  - **resource:** TNT frequency
  - **support:**
    - FCT-016
    - FCT-017
    - FCT-019
    - FCT-021
- **item 2:**
  - **flow:** legal/conventional obligation -> ARCOM procedure -> pecuniary sanction -> judicial review
  - **resource:** regulatory sanction authority
  - **support:**
    - FCT-012
    - FCT-013
- **item 3:**
  - **flow:** ARCOM certification -> trusted flagger notice -> priority platform processing -> platform decision
  - **resource:** priority notice under DSA
  - **support:**
    - FCT-023
    - FCT-024

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** constitutional/political/judicial appointing authorities
  - **relation:** appoint ARCOM college members under Article 4
  - **support:**
    - FCT-001
    - FCT-002
  - **to:** ARCOM
- **item 2:**
  - **from:** Conseil d’État
  - **relation:** reviews/corrects ARCOM decisions
  - **support:**
    - FCT-005
    - FCT-013
    - FCT-017
    - FCT-020
  - **to:** ARCOM procedures and outcomes
- **item 3:**
  - **from:** ARCOM
  - **relation:** monitors/warns/sanctions/allocates
  - **support:**
    - FCT-010
    - FCT-012
    - FCT-021
  - **to:** broadcasters and TNT candidates
- **item 4:**
  - **from:** ARCOM as DSC
  - **relation:** certifies trusted flaggers / national coordination
  - **support:**
    - FCT-023
    - FCT-024
  - **to:** platform DSA ecosystem

### IMPACT_MAP
- **C8_sanction_to_financial_effect:** VERIFIED
- **TNT_selection_to_market_access:** VERIFIED
- **cross_sector_enforcement:** VERIFIED_CASE_EXISTENCE
- **democratic_pluralism_effect:** NOT_IDENTIFIED
- **editorial_orientation_effect:** NOT_IDENTIFIED
- **equal_treatment_rates:** NOT_IDENTIFIED
- **formal_regulatory_power:** VERIFIED
- **pluralism_judgment_to_regulatory_framework:** VERIFIED
- **political_tasking:** NOT_ESTABLISHED
- **support:**
  - FCT-005
  - FCT-012
  - FCT-013
  - FCT-014
  - FCT-015
  - FCT-021
  - FCT-023

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** multi-source appointments, non-renewable terms, judicial review and cross-sector enforcement
  - **issue:** regulator versus political arm
  - **pro:** appointments include political authorities and decisions materially affect broadcasters
  - **resolution:** power verified; political tasking not established
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-005
    - FCT-014
    - FCT-015
- **item 2:**
  - **contra:** deliberation explicitly leaves topic and guest choice to editors and avoids ideological classification
  - **issue:** pluralism control versus editorial autonomy
  - **pro:** ARCOM assesses themes, speakers and viewpoints over time
  - **resolution:** compliance constraint exists without direct editorial command established
  - **support:**
    - FCT-007
    - FCT-008
    - FCT-009
- **item 3:**
  - **contra:** court upheld comparative criteria and also constrained ARCOM on later vacancies
  - **issue:** TNT nonrenewal versus arbitrary exclusion
  - **pro:** C8/NRJ12 lost terrestrial access
  - **resolution:** material exclusion effect verified; arbitrariness/political motive not established by inspected record
  - **support:**
    - FCT-017
    - FCT-018
    - FCT-019
    - FCT-020
    - FCT-021

### VERIFICATION_REPORT
- **circular_families:**
  - statutory law family A
  - ARCOM regulatory family B
  - Conseil d’État judicial family C
  - European Commission DSA family D
  - Senate audit family E
- **contradiction_ids:**
  - regulator-vs-political-arm
  - pluralism-vs-editor-autonomy
  - TNT-exclusion-vs-arbitrariness
- **downgraded_ids:**
  - global neutrality from judicial validation
  - systemic bias from selected adverse cases
  - direct removal power from trusted-flagger status
- **none_found_claims:**
  - authenticated political instruction to decide a named ARCOM case
  - complete ideology-adjusted intervention-rate denominator
  - causal estimate of ARCOM intervention on voter opinion or election result
- **remaining_gaps:**
  - tasking evidence
  - symmetry denominator
  - post-intervention editorial effect design
- **verification:** Every material web fact is linked to a current FETCH source across five institutional provenance families.

### EDI_REPORT
- **corpus:**
  - **circularity:** regulator claims cross-checked against courts, law, EU and Senate
  - **coverage:** STRONG_FORMAL_POWER;STRONG_JUDICIAL_REVIEW;STRONG_C8_SANCTION;STRONG_TNT_ACCESS_EFFECT;STRONG_DSA_ROLE_BOUNDARY;WEAK_POLITICAL_TASKING_AND_DEMOCRATIC_EFFECT
  - **independence:** 5_PROVENANCE_FAMILIES
  - **limits:**
    - case records do not yield ideology-adjusted rates
    - editorial effects rarely measured
    - appointment structure not tasking evidence
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES_FORMAL_POWER
    - **gap_type:** NONE
    - **independent_families:** 4
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES_JUDGMENT_TO_REEXAMINATION
    - **gap_type:** NONE
    - **independent_families:** 2
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** YES_SANCTION_AND_REVIEW
    - **gap_type:** NONE
    - **independent_families:** 2
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** CROSS_SECTOR_CASES_ONLY
    - **gap_type:** MEASUREMENT
    - **independent_families:** 1
  - **item 5:**
    - **claim_id:** CLM-005
    - **direct_object:** YES_MARKET_ACCESS_EFFECT
    - **gap_type:** NONE
    - **independent_families:** 2
  - **item 6:**
    - **claim_id:** CLM-006
    - **direct_object:** MODEL_CEILING
    - **gap_type:** CAUSALITY
    - **independent_families:** 5
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** LAW+REGULATOR+COURT+EU_COMMISSION+PARLIAMENTARY_AUDIT
  - **perspective:** MANDATE+PROCEDURE+SANCTION+ALLOCATION+PLATFORM
  - **stratification:** AUDIOVISUAL+TNT+PLURALISM+DSA
  - **temporal:** 2022-2026
- **edi:**
  - **assessment:** MULTI_FAMILY_PROCEDURE_DECISION_REVIEW_CONTROL
  - **flags:**
    - POLITICAL_TASKING_GAP
    - SYMMETRY_DENOMINATOR_GAP
    - DOWNSTREAM_EFFECT_GAP
- **source_counts:**
  - **primary:** 16
  - **provenance_families:** 5
  - **secondary:** 0
  - **tertiary:** 0
  - **total:** 16

### RESPONSIBILITY_MAP
- **boundary:** Coercive regulatory power and discretionary comparative judgment are not equivalent to political command; downstream democratic effect is a separate causal edge.
- **not_established:**
  - appointing authorities task named case outcomes
  - ARCOM targets one political camp systematically after denominator controls
  - pluralism warnings cause a general editorial ideological shift
  - ARCOM directly orders trusted-flagger removals
  - ARCOM interventions change elections
- **verified:**
  - ARCOM makes reviewable regulatory decisions
  - Conseil d’État can annul/restrict/validate ARCOM decisions
  - ARCOM sanction directly affected C8 financially
  - TNT decisions directly changed terrestrial market access
  - ARCOM certifies DSA trusted flaggers in France

### NEXT_QUERIES
- full intervention denominator by editor/category/referral source and outcome
- pre/post content designs around pluralism warnings and sanctions
- authenticated contacts/instructions if political tasking is alleged
- TNT scoring records and comparative candidate matrices where accessible
- trusted-flagger annual reports linking notices to platform actions without treating action as ARCOM order

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-012,QRY-013 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-022 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018,QRY-019 | support:- | counter:- | results:FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-027,FCT-028 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-007,QRY-008,QRY-020,QRY-021,QRY-022,QRY-023,QRY-024 | support:- | counter:- | results:FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021,FCT-022 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-009,QRY-010,QRY-011,QRY-025,QRY-026,QRY-027 | support:- | counter:- | results:FCT-023,FCT-024,FCT-025,FCT-026 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-013,QRY-014,QRY-017,QRY-021,QRY-022,QRY-025,QRY-026,SRC-002,SRC-003,SRC-006,SRC-010,SRC-011,SRC-014,SRC-015 | support:FCT-003,FCT-004,FCT-012,FCT-016,FCT-019,FCT-023,FCT-024 | counter:FCT-006,FCT-020 | results:FCT-003,FCT-004,FCT-012,FCT-016,FCT-019,FCT-023,FCT-024,FCT-006,FCT-020 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-014,QRY-015,QRY-016,SRC-003,SRC-004,SRC-005 | support:FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-027 | counter:FCT-011 | results:FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-027,FCT-011 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-017,QRY-018,SRC-006,SRC-007 | support:FCT-012,FCT-013,FCT-028 | counter:FCT-028 | results:FCT-012,FCT-013,FCT-028,FCT-028 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-017,QRY-019,QRY-020,SRC-006,SRC-008,SRC-009 | support:FCT-014,FCT-015 | counter:FCT-012 | results:FCT-014,FCT-015,FCT-012 | final:PARTIAL | gap:MEASUREMENT
CLM-005 | attempts:QRY-021,QRY-022,QRY-023,QRY-024,SRC-010,SRC-011,SRC-012,SRC-013 | support:FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021,FCT-022 | counter:FCT-020 | results:FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021,FCT-022,FCT-020 | final:SUPPORTED | gap:NONE
CLM-006 | attempts:QRY-012,QRY-014,QRY-016,QRY-017,QRY-018,QRY-022,QRY-023,QRY-027,SRC-001,SRC-003,SRC-005,SRC-006,SRC-007,SRC-011,SRC-012,SRC-016 | support:FCT-001,FCT-002,FCT-005,FCT-006,FCT-020,FCT-025,FCT-026,FCT-028 | counter:FCT-010,FCT-012,FCT-021 | results:FCT-001,FCT-002,FCT-005,FCT-006,FCT-020,FCT-025,FCT-026,FCT-028,FCT-010,FCT-012,FCT-021 | final:PARTIAL | gap:CAUSALITY

## STATUS_DELTA_V1
DELTA-001 | AXS-001 | OPEN | SATURATED | material mandate/procedure/decision/review evidence acquired
DELTA-002 | AXS-002 | OPEN | SATURATED | material mandate/procedure/decision/review evidence acquired
DELTA-003 | AXS-003 | OPEN | SATURATED | material mandate/procedure/decision/review evidence acquired
DELTA-004 | AXS-004 | OPEN | SATURATED | material mandate/procedure/decision/review evidence acquired

## OPEN_GAPS_V1
CLM-004 | CLM | PARTIAL | MEASUREMENT | Case existence proves cross-sector enforcement, not symmetry of rates, severity, issue mix or exposure to complaints across all editors.
CLM-006 | CLM | PARTIAL | CAUSALITY | A political-control claim requires authenticated instruction, dependence or decision-specific tasking; a downstream pluralism claim requires measured editorial/exposure effects with a credible counterfactual.

SEMANTIC_COUNTS_V1:LED:0|CLM:6|AXS:4|CAU:5|CTRL:10|ACT:4

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"ARCOM possesses material regulatory powers over audiovisual market access, pluralism compliance, sanctions and parts of platform enforcement, but these powers are exercised under statutory criteria and reviewable procedures.","claimant":"INV-074 synthesis","counter":["FCT-006","FCT-020"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-003","FCT-004","FCT-012","FCT-016","FCT-019","FCT-023","FCT-024"]}
CLM-002 | {"claim":"The 2024 CNews sequence shows that judicial review can force ARCOM to reconsider its pluralism analysis, after which ARCOM adopted a broader pluralism framework and issued a warning without granting all requested measures.","claimant":"INV-074 synthesis","counter":["FCT-011"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-027"]}
CLM-003 | {"claim":"The C8 case establishes a coercive sanction pathway that survived judicial review, but legality and proportionality of that case do not establish political neutrality of all ARCOM decisions.","claimant":"INV-074 synthesis","counter":["FCT-028"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-012","FCT-013","FCT-028"]}
CLM-004 | {"claim":"ARCOM enforcement is not confined to private or opposition-coded broadcasters: France Télévisions and France Médias Monde were also formally put on notice during the 2024 European election period; however equal intervention frequency or intensity is not established by these cases alone.","claimant":"INV-074 synthesis","counter":["FCT-012"],"gap":"Case existence proves cross-sector enforcement, not symmetry of rates, severity, issue mix or exposure to complaints across all editors.","gap_type":"MEASUREMENT","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-014","FCT-015"]}
CLM-005 | {"claim":"The 2024-2025 TNT procedure had a direct access effect: C8 and NRJ12 were not renewed while new services entered; the Conseil d’État upheld the comparative choices and allowed prior breaches to be considered, while also imposing a further impact-study obligation on newly vacant frequencies.","claimant":"INV-074 synthesis","counter":["FCT-020"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021","FCT-022"]}
CLM-006 | {"claim":"The inspected corpus does not establish a political tasking chain from appointing authorities or government preferences to ARCOM case outcomes, nor a general causal effect of ARCOM interventions on editorial orientation, public opinion or democratic pluralism.","claimant":"INV-074 synthesis","counter":["FCT-010","FCT-012","FCT-021"],"gap":"A political-control claim requires authenticated instruction, dependence or decision-specific tasking; a downstream pluralism claim requires measured editorial/exposure effects with a credible counterfactual.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-001","FCT-002","FCT-005","FCT-006","FCT-020","FCT-025","FCT-026","FCT-028"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-012","QRY-013"],"axis":"mandate governance and safeguards","links":["OBJECT_QUESTION"],"question":"What formal powers, appointment rules and institutional safeguards structure ARCOM action?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-022"],"sought_objects":["law mandate","college composition","freedom of communication","judicial review"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018","QRY-019"],"axis":"pluralism sanctions and review","links":["OBJECT_QUESTION"],"question":"How are pluralism, independence and broadcast obligations monitored, sanctioned and corrected on appeal?","result_ids":["FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-027","FCT-028"],"sought_objects":["pluralism rule","CNews reexamination","C8 sanction","public broadcaster controls"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-007","QRY-008","QRY-020","QRY-021","QRY-022","QRY-023","QRY-024"],"axis":"TNT allocation and market access","links":["OBJECT_QUESTION"],"question":"How did the 2024-2025 TNT procedure change access and how was that choice judicially reviewed?","result_ids":["FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021","FCT-022"],"sought_objects":["candidate procedure","C8 NRJ12 nonrenewal","new entrants","judicial validation","numbering"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-009","QRY-010","QRY-011","QRY-025","QRY-026","QRY-027"],"axis":"platform powers and downstream effect","links":["OBJECT_QUESTION"],"question":"What DSA powers does ARCOM have and what evidence closes or fails to close editorial/pluralism effects?","result_ids":["FCT-023","FCT-024","FCT-025","FCT-026"],"sought_objects":["DSC powers","trusted flaggers","platform decision autonomy","formal intervention rates","effect gap"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"Law, deliberations and decisions explicitly connect mandate to procedure and intervention.","counter":["FCT-027"],"limit":"The legal chain establishes regulatory authority, not political motive.","mechanism":"statutory mandate -> monitoring/referral -> ARCOM procedure -> graded decision or sanction","status":"SUPPORTED","support":["FCT-003","FCT-004","FCT-007","FCT-012"]}
CAU-002 | {"causal_right":"Chronology and explicit references in ARCOM decisions close the institutional chain.","counter":["FCT-011"],"limit":"Judicially induced regulatory change is supported; downstream editorial change is not measured here.","mechanism":"Conseil d’État 13 Feb 2024 judgment -> mandatory reexamination -> broadened pluralism framework -> CNews warning/request for compliance measures","status":"SUPPORTED","support":["FCT-005","FCT-006","FCT-007","FCT-008","FCT-010","FCT-011"]}
CAU-003 | {"causal_right":"The sanction decision and Conseil d’État judgment directly establish the chain.","counter":["FCT-028"],"limit":"Case-specific enforcement legality/proportionality; no inference to all ARCOM cases.","mechanism":"repeated C8 contractual/legal breaches -> ARCOM financial sanction -> judicial review -> sanction maintained","status":"SUPPORTED","support":["FCT-012","FCT-013"]}
CAU-004 | {"causal_right":"The regulator and court records directly connect the selection process to authorisation outcomes.","counter":["FCT-020"],"limit":"Direct access effect is established; political intent or democratic downstream effect is separate.","mechanism":"TNT call + statutory comparative criteria -> rejection/non-renewal of C8 and NRJ12 -> new service authorisations / loss of terrestrial market access","status":"SUPPORTED","support":["FCT-016","FCT-017","FCT-018","FCT-019","FCT-021","FCT-022"]}
CAU-005 | {"causal_right":"Commission DSA guidance explicitly defines coordinator, trusted-flagger and platform roles.","counter":["FCT-023","FCT-024"],"limit":"Priority processing is mandatory, but providers retain decision responsibility and the Commission has exclusive VLOP due-diligence competence.","mechanism":"ARCOM as French DSA coordinator -> designation of trusted flaggers -> priority platform review -> platform content decision","status":"SUPPORTED","support":["FCT-023","FCT-024"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"regulation != political control","status":"DONE","support":["FCT-003","FCT-005","FCT-020"]}
CTRL-002 | {"control":"sanction != censorship by default","status":"DONE","support":["FCT-012","FCT-013"]}
CTRL-003 | {"control":"appointment != tasking","status":"DONE","support":["FCT-001","FCT-002"]}
CTRL-004 | {"control":"compliance != editorial capture","status":"DONE","support":["FCT-010","FCT-027"]}
CTRL-005 | {"control":"asymmetry != intent","status":"DONE","support":["FCT-014","FCT-015","FCT-028"]}
CTRL-006 | {"control":"decision != downstream democratic effect","status":"DONE","support":["FCT-021","FCT-022"]}
CTRL-007 | {"control":"judicial validation != global neutrality","status":"DONE","support":["FCT-013","FCT-028"]}
CTRL-008 | {"control":"warning != licence withdrawal","status":"DONE","support":["FCT-010","FCT-011","FCT-021"]}
CTRL-009 | {"control":"trusted-flagger priority != removal order","status":"DONE","support":["FCT-023","FCT-024"]}
CTRL-010 | {"control":"pluralism mandate != ideological classification of speakers","status":"DONE","support":["FCT-007","FCT-008","FCT-009"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"publish structured annual denominators by editor type, issue, referral source, intervention level, sanction amount and judicial outcome","actor":"ARCOM","intent":"permit symmetry testing without inferring bias from selected cases","status":"OPEN","support":["FCT-014","FCT-015","FCT-026"]}
ACT-002 | {"action":"link major pluralism warnings and sanctions to pre/post programme-level indicators while preserving editor autonomy and confounders","actor":"ARCOM / researchers / broadcasters","intent":"measure whether regulatory intervention changes editorial output rather than only legal compliance records","status":"OPEN","support":["FCT-007","FCT-010"]}
ACT-003 | {"action":"for frequency allocations, preserve scoring/criteria traces sufficient to compare accepted and rejected candidacies and later judicial outcomes","actor":"ARCOM / courts","intent":"separate lawful comparative discretion from alleged political selection","status":"OPEN","support":["FCT-016","FCT-017","FCT-018","FCT-019"]}
ACT-004 | {"action":"reopen political-control claim only on authenticated instruction/tasking, demonstrable decision-maker dependence, unexplained systematic asymmetry after denominator controls, or credible causal evidence of editorial/pluralism effects","actor":"future investigation","intent":"avoid cumulative case counting and target decisive edges","status":"OPEN","support":["FCT-001","FCT-020","FCT-026","FCT-028"]}

SEARCH_ACTIVITY_V1:WEB:11|FETCH:16|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FAIL | MNEMO | MNEMO_UNAVAILABLE | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | PASS | - | - | ARCOM law composition powers freedom communication France
QRY-002 | WEB | PASS | - | - | Conseil Etat RSF CNews ARCOM pluralism 13 February 2024
QRY-003 | WEB | PASS | - | - | ARCOM deliberation pluralism 17 July 2024 all participants
QRY-004 | WEB | PASS | - | - | ARCOM CNews reexamination RSF July 2024 pluralism independence
QRY-005 | WEB | PASS | - | - | ARCOM C8 3.5 million sanction Council State upheld 2024
QRY-006 | WEB | PASS | - | - | ARCOM France Televisions France Medias Monde European election notices 2024
QRY-007 | WEB | PASS | - | - | ARCOM TNT 2024 C8 NRJ12 T18 OFTV Conseil Etat 2025
QRY-008 | WEB | PASS | - | - | ARCOM TNT numbering 2025 Conseil Etat 2026
QRY-009 | WEB | PASS | - | - | ARCOM DSA digital services coordinator trusted flaggers platform decision
QRY-010 | WEB | PASS | - | - | ARCOM interventions public private 2023 2025 formal rates
QRY-011 | WEB | PASS | - | - | Senate ARCOM 2025 report pluralism platforms resource constraints
QRY-012 | FETCH | PASS | SRC-001 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044259313 | -
QRY-013 | FETCH | PASS | SRC-002 | https://www.arcom.fr/nos-missions | -
QRY-014 | FETCH | PASS | SRC-003 | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2024-02-13/463162 | -
QRY-015 | FETCH | PASS | SRC-004 | https://www.arcom.fr/se-documenter/espace-juridique/textes-juridiques/deliberation-ndeg-2024-15-du-17-juillet-2024-relative-au-respect-du-principe-de-pluralisme-des-courants-de-pensee-et-dopinion-par-les-editeurs-de-services | -
QRY-016 | FETCH | PASS | SRC-005 | https://www.arcom.fr/se-documenter/espace-juridique/decisions/reexamen-de-la-saisine-de-lassociation-reporters-sans-frontieres-rsf | -
QRY-017 | FETCH | PASS | SRC-006 | https://www.arcom.fr/se-documenter/espace-juridique/decisions/decision-du-9-fevrier-2023-portant-sanction-pecuniaire-lencontre-de-la-societe-c8 | -
QRY-018 | FETCH | PASS | SRC-007 | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2024-07-10/472887 | -
QRY-019 | FETCH | PASS | SRC-008 | https://www.arcom.fr/se-documenter/espace-juridique/decisions/decision-du-30-mai-2024-mettant-en-demeure-la-societe-france-televisions | -
QRY-020 | FETCH | PASS | SRC-009 | https://www.arcom.fr/se-documenter/espace-juridique/decisions/decision-du-30-mai-2024-mettant-en-demeure-la-societe-france-medias-monde | -
QRY-021 | FETCH | PASS | SRC-010 | https://www.arcom.fr/presse/appel-aux-candidatures-pour-15-services-de-la-tnt-preselection-des-candidats | -
QRY-022 | FETCH | PASS | SRC-011 | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2025-02-19/499823 | -
QRY-023 | FETCH | PASS | SRC-012 | https://www.arcom.fr/presse/presentation-du-rapport-dactivite-2024-de-larcom-audition-de-martin-ajdari-president-de-larcom-devant-la-commission-des-affaires-culturelles-et-de-leducation-de-lassemblee-nationale | -
QRY-024 | FETCH | PASS | SRC-013 | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2026-02-25/502416 | -
QRY-025 | FETCH | PASS | SRC-014 | https://digital-strategy.ec.europa.eu/en/policies/trusted-flaggers-under-dsa | -
QRY-026 | FETCH | PASS | SRC-015 | https://digital-strategy.ec.europa.eu/en/policies/dsa-dscs | -
QRY-027 | FETCH | PASS | SRC-016 | https://www.senat.fr/notice-rapport/2025/r25-068-notice.html | -

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | LEGIFRANCE-1986-ART4 | Légifrance - loi 1986 article 4 composition Arcom | 2022-01-01 | 2026-09-09 | Composition, nomination and mandate of ARCOM college | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044259313
SRC-002 | ◈ | fam:B | ARCOM-MISSIONS | Arcom - Nos missions | 2026-09-09 | 2026-09-09 | ARCOM official statement of missions and freedom of communication | https://www.arcom.fr/nos-missions
SRC-003 | ◈ | fam:C | CE-463162 | Conseil d’État - décision 463162 RSF/CNews | 2024-02-13 | 2026-09-09 | Judicial review requiring ARCOM reexamination | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2024-02-13/463162
SRC-004 | ◈ | fam:B | ARCOM-2024-15 | Arcom - délibération pluralisme 2024-15 | 2024-07-18 | 2026-09-09 | Pluralism assessment criteria and editor autonomy | https://www.arcom.fr/se-documenter/espace-juridique/textes-juridiques/deliberation-ndeg-2024-15-du-17-juillet-2024-relative-au-respect-du-principe-de-pluralisme-des-courants-de-pensee-et-dopinion-par-les-editeurs-de-services
SRC-005 | ◈ | fam:B | ARCOM-RSF-2024 | Arcom - réexamen saisine RSF/CNews | 2024-07-31 | 2026-09-09 | ARCOM warning after Council of State reexamination | https://www.arcom.fr/se-documenter/espace-juridique/decisions/reexamen-de-la-saisine-de-lassociation-reporters-sans-frontieres-rsf
SRC-006 | ◈ | fam:B | ARCOM-C8-2023-63 | Arcom - sanction C8 3.5m | 2023-02-09 | 2026-09-09 | Financial sanction for rights/mastery-of-air breaches | https://www.arcom.fr/se-documenter/espace-juridique/decisions/decision-du-9-fevrier-2023-portant-sanction-pecuniaire-lencontre-de-la-societe-c8
SRC-007 | ◈ | fam:C | CE-472887 | Conseil d’État - C8 sanction 3.5m upheld | 2024-07-10 | 2026-09-09 | Judicial review of ARCOM sanction | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2024-07-10/472887
SRC-008 | ◈ | fam:B | ARCOM-FTV-2024 | Arcom - mise en demeure France Télévisions élections européennes | 2024-05-31 | 2026-09-09 | Election-period pluralism enforcement against public broadcaster | https://www.arcom.fr/se-documenter/espace-juridique/decisions/decision-du-30-mai-2024-mettant-en-demeure-la-societe-france-televisions
SRC-009 | ◈ | fam:B | ARCOM-FMM-2024 | Arcom - mise en demeure France Médias Monde élections européennes | 2024-05-31 | 2026-09-09 | Election-period pluralism enforcement against public broadcaster | https://www.arcom.fr/se-documenter/espace-juridique/decisions/decision-du-30-mai-2024-mettant-en-demeure-la-societe-france-medias-monde
SRC-010 | ◈ | fam:B | ARCOM-TNT-PRESEL-2024 | Arcom - présélection TNT 2024 | 2024-07-24 | 2026-09-09 | TNT candidate selection procedure | https://www.arcom.fr/presse/appel-aux-candidatures-pour-15-services-de-la-tnt-preselection-des-candidats
SRC-011 | ◈ | fam:C | CE-499823 | Conseil d’État - TNT C8 NRJ12 | 2025-02-19 | 2026-09-09 | Judicial review of TNT non-renewals and selection criteria | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2025-02-19/499823
SRC-012 | ◈ | fam:B | ARCOM-RA2024-AUDITION | Arcom - présentation rapport activité 2024 | 2025-10-01 | 2026-09-09 | TNT outcome and stated selection considerations | https://www.arcom.fr/presse/presentation-du-rapport-dactivite-2024-de-larcom-audition-de-martin-ajdari-president-de-larcom-devant-la-commission-des-affaires-culturelles-et-de-leducation-de-lassemblee-nationale
SRC-013 | ◈ | fam:C | CE-502416 | Conseil d’État - numérotation TNT 2026 | 2026-02-25 | 2026-09-09 | Judicial review of ARCOM numbering choices | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2026-02-25/502416
SRC-014 | ◈ | fam:D | EC-DSA-TRUSTED-FLAGGERS | European Commission - trusted flaggers DSA | 2026-06-12 | 2026-09-09 | Trusted flagger priority and platform decision responsibility | https://digital-strategy.ec.europa.eu/en/policies/trusted-flaggers-under-dsa
SRC-015 | ◈ | fam:D | EC-DSA-DSC | European Commission - Digital Services Coordinators | 2026-06-12 | 2026-09-09 | National DSC powers and Commission exclusive VLOP competence | https://digital-strategy.ec.europa.eu/en/policies/dsa-dscs
SRC-016 | ◈ | fam:E | SENAT-R25-068 | Sénat - rapport Arcom 2025 | 2026-04-24 | 2026-09-09 | Independent institutional audit of expanding missions and constraints | https://www.senat.fr/notice-rapport/2025/r25-068-notice.html

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044259313 | A | 2026-09-09 | ARCOM college has nine members from multiple appointing authorities | Article 4 provides for nine members: the president appointed by the President of the Republic, three designated by the President of the National Assembly, three by the President of the Senate, one member of the Conseil d’État and one of the Cour de cassation. | -
FCT-002 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044259313 | A | 2026-09-09 | ARCOM member mandates are six years and non-renewable | Article 4 sets six-year non-renewable mandates, a structural safeguard against immediate reappointment incentives. | -
FCT-003 | FACT | ✧ | https://www.arcom.fr/nos-missions | B | 2026-09-09 | ARCOM mission includes protection of freedom of expression and communication | ARCOM states that its first mission is to guarantee freedom of expression and audiovisual communication while regulating in the public interest. | -
FCT-004 | FACT | ✧ | https://www.arcom.fr/nos-missions | B | 2026-09-09 | ARCOM powers cover pluralism, market access and platforms | ARCOM describes missions spanning audiovisual pluralism, frequency attribution and economic regulation, and supervision of online-platform compliance. | -
FCT-005 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2024-02-13/463162 | C | 2026-09-09 | Conseil d’État annulled ARCOM refusal to act on parts of RSF CNews complaint | On 13 February 2024 the Conseil d’État annulled ARCOM’s 2022 refusal insofar as it rejected requests concerning pluralism and independence of CNews information and ordered reexamination within six months. | -
FCT-006 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2024-02-13/463162 | C | 2026-09-09 | Judicial review can constrain ARCOM interpretation without ordering a predetermined sanction | The Conseil d’État ordered reexamination rather than directly imposing the requested CNews formal notice, showing a judicial correction of regulatory analysis without substituting the regulator on the final measure. | -
FCT-007 | FACT | ✧ | https://www.arcom.fr/se-documenter/espace-juridique/textes-juridiques/deliberation-ndeg-2024-15-du-17-juillet-2024-relative-au-respect-du-principe-de-pluralisme-des-courants-de-pensee-et-dopinion-par-les-editeurs-de-services | B | 2026-09-09 | 2024 pluralism rule extends assessment to all programme participants | ARCOM’s 17 July 2024 deliberation requires consideration of all participants and assesses manifest and durable imbalance using subject variety, diversity of speakers and plurality of viewpoints. | -
FCT-008 | FACT | ✧ | https://www.arcom.fr/se-documenter/espace-juridique/textes-juridiques/deliberation-ndeg-2024-15-du-17-juillet-2024-relative-au-respect-du-principe-de-pluralisme-des-courants-de-pensee-et-dopinion-par-les-editeurs-de-services | B | 2026-09-09 | Pluralism review uses time windows rather than per-segment ideological quotas | The deliberation generally assesses at least three months for services and one month for continuous news channels, rather than classifying every speaker by ideology. | -
FCT-009 | FACT | ✧ | https://www.arcom.fr/se-documenter/espace-juridique/textes-juridiques/deliberation-ndeg-2024-15-du-17-juillet-2024-relative-au-respect-du-principe-de-pluralisme-des-courants-de-pensee-et-dopinion-par-les-editeurs-de-services | B | 2026-09-09 | Editors retain responsibility for themes and guests under the pluralism rule | ARCOM explicitly states that editors remain solely responsible for choosing topics and participants, within applicable legal and contractual obligations. | -
FCT-010 | FACT | ✧ | https://www.arcom.fr/se-documenter/espace-juridique/decisions/reexamen-de-la-saisine-de-lassociation-reporters-sans-frontieres-rsf | B | 2026-09-09 | ARCOM found CNews May 2021 treatment of several subjects univocal | On reexamination ARCOM found several subjects were treated univocally with divergent viewpoints remaining very occasional, despite variety of topics and speakers. | -
FCT-011 | FACT | ✧ | https://www.arcom.fr/se-documenter/espace-juridique/decisions/reexamen-de-la-saisine-de-lassociation-reporters-sans-frontieres-rsf | B | 2026-09-09 | ARCOM issued a warning on pluralism but rejected the requested independence notice | ARCOM warned CNews and requested future compliance measures on pluralism while rejecting RSF’s request for a formal notice on independence of information. | -
FCT-012 | FACT | ✧ | https://www.arcom.fr/se-documenter/espace-juridique/decisions/decision-du-9-fevrier-2023-portant-sanction-pecuniaire-lencontre-de-la-societe-c8 | B | 2026-09-09 | ARCOM imposed a 3.5 million euro sanction on C8 | The 9 February 2023 decision imposed EUR 3.5 million for breaches concerning rights of a person and mastery of the air, taking account of prior sanctions. | -
FCT-013 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2024-07-10/472887 | C | 2026-09-09 | Conseil d’État upheld the C8 3.5 million euro sanction | On 10 July 2024 the Conseil d’État rejected C8’s annulment request and held that the sanction was not excessive in light of the gravity and repeated breaches. | -
FCT-014 | FACT | ✧ | https://www.arcom.fr/se-documenter/espace-juridique/decisions/decision-du-30-mai-2024-mettant-en-demeure-la-societe-france-televisions | B | 2026-09-09 | ARCOM also formally enforced election-period rules against France Télévisions | On 30 May 2024 ARCOM put France Télévisions on formal notice under European-election pluralism rules. | -
FCT-015 | FACT | ✧ | https://www.arcom.fr/se-documenter/espace-juridique/decisions/decision-du-30-mai-2024-mettant-en-demeure-la-societe-france-medias-monde | B | 2026-09-09 | ARCOM also formally enforced election-period rules against France Médias Monde | On 30 May 2024 ARCOM put France Médias Monde on formal notice under European-election pluralism rules. | -
FCT-016 | FACT | ✧ | https://www.arcom.fr/presse/appel-aux-candidatures-pour-15-services-de-la-tnt-preselection-des-candidats | B | 2026-09-09 | 2024 TNT allocation used an open call with more candidates than frequencies | ARCOM launched a call for fifteen national TNT services, declared twenty-five candidacies admissible and held public auditions before preselction. | -
FCT-017 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2025-02-19/499823 | C | 2026-09-09 | Conseil d’État upheld ARCOM non-renewal of C8 and NRJ12 | On 19 February 2025 the Conseil d’État rejected C8 and NRJ12 challenges and found no illegality in ARCOM’s comparative assessment. | -
FCT-018 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2025-02-19/499823 | C | 2026-09-09 | Past regulatory breaches could legally be considered in TNT renewal | The Conseil d’État held that ARCOM could take into account breaches committed by an incumbent editor when assessing its capacity to comply with future obligations. | -
FCT-019 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2025-02-19/499823 | C | 2026-09-09 | TNT selection criteria include pluralism, public interest and comparative merits | The Conseil d’État described ARCOM’s task as comparing candidacies under statutory criteria including pluralism, diversity, public interest, competition, financing and compliance capacity. | -
FCT-020 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2025-02-19/499823 | C | 2026-09-09 | Conseil d’État also constrained ARCOM after late Canal Plus withdrawals | Although it upheld the C8/NRJ12 choices, the Conseil d’État required a new impact-study and consultation process to assess whether four newly vacant frequencies should be reallocated. | -
FCT-021 | FACT | ✧ | https://www.arcom.fr/presse/presentation-du-rapport-dactivite-2024-de-larcom-audition-de-martin-ajdari-president-de-larcom-devant-la-commission-des-affaires-culturelles-et-de-leducation-de-lassemblee-nationale | B | 2026-09-09 | TNT outcome replaced C8 and NRJ12 with two new services | ARCOM’s 2024 activity presentation states that T18 and Novo19 were authorised while C8 and NRJ12 were not renewed, based on comparative merits, past experience and breaches, and interest of new projects. | -
FCT-022 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2026-02-25/502416 | C | 2026-09-09 | ARCOM numbering choices were subject to later judicial review | The Conseil d’État’s 25 February 2026 decision records ARCOM’s regrouping of news channels and reallocation of vacated numbers, demonstrating reviewable procedural/economic power over visibility. | -
FCT-023 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/trusted-flaggers-under-dsa | D | 2026-09-09 | DSA trusted flaggers receive priority review but do not decide removal | The European Commission states that trusted-flagger notices must be prioritised, while platform providers retain sole responsibility to decide on notices and remove content where justified. | -
FCT-024 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/dsa-dscs | D | 2026-09-09 | ARCOM is France Digital Services Coordinator but Commission has exclusive VLOP due-diligence competence | The Commission lists ARCOM as France’s DSC with investigation and enforcement powers for intermediary services, while the Commission has exclusive competence for monitoring due-diligence obligations of very large platforms and search engines. | -
FCT-025 | FACT | ✧ | https://www.senat.fr/notice-rapport/2025/r25-068-notice.html | E | 2026-09-09 | Senate audit identifies expanding ARCOM missions and implementation constraints | The Senate report notes rapid expansion of ARCOM responsibilities and specific difficulties in pluralism control and regulation of international digital platforms. | -
FCT-026 | FACT | ✧ | https://www.senat.fr/notice-rapport/2025/r25-068-notice.html | E | 2026-09-09 | Institutional audit warns of resource dispersion rather than documenting political tasking | The Senate report flags risk that multiplying missions disperses ARCOM resources; it does not establish a political command chain over case decisions. | -
FCT-027 | FACT | ✧ | https://www.arcom.fr/se-documenter/espace-juridique/decisions/reexamen-de-la-saisine-de-lassociation-reporters-sans-frontieres-rsf | B | 2026-09-09 | CNews reexamination shows an intermediate enforcement instrument | The July 2024 outcome was a warning and request for compliance information, not a sanction or licence withdrawal, illustrating graded intervention. | -
FCT-028 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2024-07-10/472887 | C | 2026-09-09 | Judicial validation of one sanction does not prove political neutrality of all decisions | The C8 judgment closes legality and proportionality for that sanction only; it does not establish absence of bias across ARCOM’s entire caseload. | -
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
FCT-009 | SRC-004
FCT-010 | SRC-005
FCT-011 | SRC-005
FCT-012 | SRC-006
FCT-013 | SRC-007
FCT-014 | SRC-008
FCT-015 | SRC-009
FCT-016 | SRC-010
FCT-017 | SRC-011
FCT-018 | SRC-011
FCT-019 | SRC-011
FCT-020 | SRC-011
FCT-021 | SRC-012
FCT-022 | SRC-013
FCT-023 | SRC-014
FCT-024 | SRC-015
FCT-025 | SRC-016
FCT-026 | SRC-016
FCT-027 | SRC-005
FCT-028 | SRC-007

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

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:search
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:facts
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:causal
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:verify
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:accountability
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:narrative

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-09T14:38:34.884563+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":28,"eligible":28,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:28;attempted:0;success:0;failure:0;blocked:28} | WRITEBACK_EXECUTION_V1:[28 rows, see section]

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
