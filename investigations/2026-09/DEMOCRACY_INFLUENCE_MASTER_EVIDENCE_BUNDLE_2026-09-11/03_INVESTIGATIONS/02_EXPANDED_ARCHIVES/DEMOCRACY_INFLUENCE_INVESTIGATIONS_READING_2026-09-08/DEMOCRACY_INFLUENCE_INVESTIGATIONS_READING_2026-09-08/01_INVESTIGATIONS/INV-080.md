ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260907-2217-sanctions-administratives | PARENT_RUN_ID:NONE | AS_OF:2026-09-07
INPUT_KIND:RUN_CARD | MISSION_MODE:RECHECK_EXTEND | INPUT_REF:PATH:/mnt/data/inv080-exec/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-07_sanctions-administratives/2026-09-07_22-17_sanctions-administratives_INPUT.md | SUBJECT_SLUG:sanctions-administratives | SUBJECT_FP:sha256:b1253f7ee96a17a445ccc278e4432970c229a34b2428c8fd9ab3daca4adf7780 | INPUT_SHA256:sha256:7ccd71bcdf45263c7885989fcddf53e4a42dd205d30e473b74ee60fdc701fe36
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/Europe 2015-2026; administrative asset freezes, expulsions, dissolutions and restrictive measures without criminal-conviction prerequisite; trace authority -> evidence -> measure -> review -> effect
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/MONEY.md,clusters/NETWORK.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-080 — Sanction administrative sans condamnation judiciaire

## 1. Question et règle de preuve
L'objet est de distinguer quatre niveaux souvent fusionnés : pouvoir administratif préventif, qualification pénale, contrôle juridictionnel et instrumentalisation politique. Une mesure sévère peut être légalement préventive sans constituer une condamnation pénale. Inversement, son existence ou sa validation ne suffit pas à démontrer légitimité politique, vérité générale des allégations ou effet électoral.

## 2. Pouvoir préventif administratif ≠ culpabilité pénale
Le corpus français établit plusieurs régimes où une autorité administrative peut imposer des restrictions matérielles sans condamnation pénale préalable : gels d'avoirs liés à l'ingérence étrangère, au terrorisme ou au narcotrafic, dissolutions administratives et expulsions. Ces pouvoirs ne sont pas juridiquement vides : ils reposent sur des critères propres et restent soumis à des voies de contrôle.

## 3. Gel préventif contre l'ingérence étrangère
Le code monétaire et financier définit l'ingérence étrangère par une relation directe ou indirecte avec une puissance étrangère et permet un gel préventif conjoint par les ministres compétents. Cette architecture ferme une arête publique explicite `autorité -> mesure financière`. Elle ne ferme pas pour autant `mesure -> culpabilité pénale`, ni `mesure -> instrumentalisation partisane`.

## 4. Comparateurs terrorisme et narcotrafic
Les régimes voisins confirment que le gel administratif préventif est une technique juridique distincte de la condamnation. Leur utilité ici est comparative : ils empêchent de traiter le seul mécanisme de gel comme une singularité propre à la lutte contre l'ingérence ou comme une preuve intrinsèque d'abus politique.

## 5. Dissolution : pouvoir sévère, contrôle substantiel
Le droit français permet la dissolution administrative d'organisations dans des hypothèses définies. Le Conseil d'État qualifie ce pouvoir de police administrative et non de peine pénale. Les contrôles sont discriminants : certaines dissolutions sont confirmées, tandis que celle des Soulèvements de la Terre a été annulée pour disproportion. Le corpus réfute donc à la fois `administration toujours déférée par le juge` et `annulation = preuve de mauvaise foi politique`.

## 6. Expulsion : examen motif par motif
Dans le dossier Iquioussen, le Conseil d'État a examiné séparément les motifs invoqués par l'administration, en rejetant certains comme insuffisants et en retenant d'autres. Ce contrôle montre que la chaîne n'est ni un simple blanc-seing administratif ni une requalification pénale globale. Le niveau soutenu reste : mesure administrative, dossier factuel, standard légal, contrôle juridictionnel.

## 7. Mesures restrictives de l'Union européenne
Le régime européen de gels d'avoirs fonctionne lui aussi par critères de listing et obligations financières contraignantes, sans exiger une condamnation pénale préalable. Les lignes directrices du Conseil imposent cependant des motifs défendables, une notification, des droits de la défense et une protection juridictionnelle effective.

## 8. Mazepin et Fridman : contrôles négatifs
Les annulations concernant Mazepin et Fridman montrent qu'une inscription sur une liste n'est ni une culpabilité pénale ni une présomption irréfragable. Dans Mazepin, le lien familial ne suffisait pas à maintenir la mesure selon le dossier examiné. Ces cas constituent des contrôles de correction : l'autorité de listing existe, mais ses critères restent justiciables.

## 9. Modèles concurrents
Trois modèles restent distincts. Le premier, **mesure préventive légale et proportionnée**, est établi dans plusieurs architectures. Le deuxième, **erreur ou disproportion administrative corrigée par le juge**, est également établi dans des cas précis. Le troisième, **instrumentalisation partisane systématique**, n'est pas établi transversalement par ce corpus. Une annulation, une mesure controversée ou un effet matériel ne suffisent pas à prouver l'intention politique cachée.

## 10. Plafond causal
`I0-I4` sont vérifiés de manière cas-spécifique pour l'autorité, la base juridique, la mesure, certains éléments d'attribution administrative, le contrôle et l'effet institutionnel ou matériel. `I5` reste non établi en général pour le motif partisan ou le tasking politique caché. `I6` et `I7` ne sont pas établis : aucune conception causale du corpus n'isole un changement de comportement politique ou un résultat électoral contrefactuel produit par ces mesures.

## 11. Résultat et routage
Le delta terminal est : **pouvoirs administratifs préventifs sévères sans condamnation pénale préalable établis et juridiquement bornés ; contrôle juridictionnel effectif avec validations et annulations établi ; instrumentalisation partisane générale et effet électoral causal non établis.** Ce résultat ferme le dernier constituant direct d'INV-129, qui peut désormais tester ce qui distingue influence juridique, coercition légale, erreur/disproportion et lawfare intentionnel.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:6|SRC_COMPLETE:14/14

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-07
- **notes:**
  - current French/EU rules prioritized
  - 2022-2024 adjudicated comparators retained
  - no prediction beyond as-of
- **status:** CURRENT_WITH_HISTORICAL_CONTROLS
- **window:** 2015-2026

### MANIPULATION_REPORT
- **assumptions:**
  - official law establishes formal authority, not truth of every underlying allegation
  - judicial decisions establish bounded holdings, evidence assessment and proportionality review
  - absence of conviction prerequisite does not imply absence of legal standard
- **clusters:**
  - **loaded:**
    - clusters/POWER.md
    - clusters/MONEY.md
    - clusters/NETWORK.md
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - severe preventive measure is not criminal punishment
  - review can validate, narrow or reverse
  - anti-interference freeze requires a defined foreign-power request/on-behalf relationship
- **input_kind:** RUN_CARD
- **mission_mode:** RECHECK_EXTEND
- **patterns:**
  - asset freeze
  - listing
  - dissolution
  - expulsion
  - proportionality
  - error of assessment
  - delisting
- **priorities:**
  - legal basis
  - evidentiary threshold
  - reviewability
  - correction
  - motive boundary
  - causal ceiling
- **query_guidance:** separate authority/factual predicate/procedural safeguards/review/effect
- **rhetorical:**
  - **AUTH:** official sources establish formal rules/holdings only
  - **BF:** N/A
  - **DEM:** cases are controls, not prevalence estimates
  - **FAC:** separate measure, guilt, motive and effect
  - **NUM:** duration/count does not prove purpose
- **speaker:**
  - **goal:** forensic classification of preventive administrative coercion
  - **target:** authority -> evidence -> measure -> review -> effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **Κ:** 3
  - **Λ:** 4
  - **Ξ:** 4
  - **Σ:** 3
  - **Φ:** 4
  - **Ψ:** 3
  - **Ω:** 4
  - **κ:** 3
  - **ρ:** 4
  - **€:** 5
  - **↕:** 5
  - **⏰:** 3
  - **⚔:** 3
  - **⫸:** 4
  - **🌐:** 4
- **threats:**
  - administrative_measure=criminal_guilt
  - legality=legitimacy
  - annulment=bad_faith
  - upholding=truth_beyond_case
  - restriction=electoral_effect

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - motive/tasking
  - **input_ids:**
    - FCT-003
    - FCT-009
    - FCT-017
    - FCT-021
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no general partisan-command edge
  - **not_computable:**
    - informal partisan pressure without documentary trace
  - **operations_applied:**
    - separated authority from motive
    - mapped review/correction
  - **reason:** formal authority, discretion and review are central
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-003
    - CLM-004
  - **status:** DONE
  - **trigger:** administrative authority and coercive decision
- **item 2:**
  - **gaps:**
    - economic-to-political effect
  - **input_ids:**
    - FCT-003
    - FCT-005
    - FCT-007
    - FCT-021
  - **module:** clusters/MONEY.md
  - **negative_results:**
    - freeze does not prove guilt
  - **not_computable:**
    - aggregate political impact
  - **operations_applied:**
    - separated preventive freeze from criminal confiscation
    - mapped legal command
  - **reason:** financial coercion is a direct mechanism
  - **result_ids:**
    - CLM-001
    - CLM-004
  - **status:** DONE
  - **trigger:** asset freezes
- **item 3:**
  - **gaps:**
    - ultimate motive beyond legal record
  - **input_ids:**
    - FCT-001
    - FCT-004
    - FCT-022
    - FCT-026
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - association alone insufficient in Mazepin control
  - **not_computable:**
    - hidden tasking absent evidence
  - **operations_applied:**
    - bounded association inference
    - distinguished family/association from statutory criteria
  - **reason:** principal/intermediary relationships can matter to legal qualification
  - **result_ids:**
    - CLM-001
    - CLM-005
  - **status:** DONE
  - **trigger:** foreign-power tasking definition and association/listing criteria

### SCOPING_REPORT
- **excluded:**
  - criminal conviction as prerequisite unless legally relevant
  - generic allegations without primary legal/decision record
  - non-isomorphic non-European comparators
- **guards:**
  - administrative_measure != criminal_guilt
  - legality != legitimacy
  - allegation != proof
  - sanction != political_motive
  - institutional_effect != electoral_effect
  - judicial_review != proof_of_initial_bad_faith
- **included:**
  - France anti-interference/terror/narcotraffic asset freezes
  - France administrative dissolutions
  - France expulsion comparator
  - EU restrictive-measure asset freezes and judicial review
- **route:** INV-129

### CREDO
- administrative_measure != criminal_guilt
- legality != legitimacy
- allegation != proof
- sanction != political_motive
- institutional_effect != electoral_effect
- judicial_review != proof_of_initial_bad_faith
- annulment != partisan_instrumentalization

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** RECHECK_EXTEND
- **patterns:**
  - asset freeze
  - restrictive listing
  - administrative dissolution
  - expulsion
  - proportionality review
  - error of assessment
  - delisting
- **priorities:**
  - legal basis
  - factual threshold
  - decision-maker
  - contradictory process
  - judicial review
  - correction
  - political-motive evidence
  - causal effect
- **query_guidance:** separate authority, factual predicate, measure, review, motive and effect edge-by-edge
- **speaker:**
  - **goal:** classify preventive administrative coercion
  - **target:** authority-evidence-measure-review-effect chain
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **threats:**
  - administrative measure = criminal guilt
  - annulment = bad faith
  - upholding = truth beyond case
  - restriction = electoral effect

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** The examined statutes create preventive administrative powers with specific legal criteria and review.
  - **resolution:** Classify the legal basis and evidentiary threshold separately from criminal guilt.
  - **thesis:** A severe administrative measure without conviction is punishment without proof.
- **item 2:**
  - **antithesis:** Courts can annul for proportionality or error while upholding other measures on different records.
  - **resolution:** Annulment proves a legal defect in the adjudicated measure, not hidden motive absent additional evidence.
  - **thesis:** Judicial annulment proves political bad faith.
- **item 3:**
  - **antithesis:** Review is bounded by statutory criteria and the record before the court.
  - **resolution:** Retain only the holding and supported predicate.
  - **thesis:** An upheld measure proves the authority allegations true in every broader sense.
- **item 4:**
  - **antithesis:** The corpus establishes legal/material effects but no voter-behavior or electoral counterfactual design.
  - **resolution:** Stop causal inference at the highest supported edge.
  - **thesis:** Administrative restriction necessarily changes politics or elections.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **flow:** French ministers -> financial system -> targeted person/entity
  - **resource:** funds/economic resources
  - **restriction:** preventive freeze
  - **status:** BINDING_PUBLIC_LAW
  - **support:**
    - FCT-003
    - FCT-004
- **item 2:**
  - **flow:** French executive -> association/group
  - **resource:** legal organizational existence/activity
  - **restriction:** administrative dissolution
  - **status:** ADMINISTRATIVE_POLICE_REVIEWABLE
  - **support:**
    - FCT-009
    - FCT-011
    - FCT-013
- **item 3:**
  - **flow:** EU listing -> regulated actors -> listed person/entity
  - **resource:** funds/economic resources
  - **restriction:** asset freeze/prohibition to make available
  - **status:** BINDING_PUBLIC_LAW_WITH_JUDICIAL_REVIEW
  - **support:**
    - FCT-021
    - FCT-023
    - FCT-025
    - FCT-027

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** administrative authority
  - **limits:**
    - formal authority != partisan motive
  - **relation:** freeze/list/dissolve/expel under statutory criteria
  - **support:**
    - FCT-003
    - FCT-009
    - FCT-017
    - FCT-021
  - **to:** person/entity/group
- **item 2:**
  - **from:** court
  - **limits:**
    - review outcome != proof of initial bad faith
  - **relation:** legality/evidence/proportionality review
  - **support:**
    - FCT-011
    - FCT-012
    - FCT-017
    - FCT-025
    - FCT-027
  - **to:** administrative measure
- **item 3:**
  - **from:** EU listing authority
  - **limits:**
    - listing != criminal guilt
  - **relation:** binding asset freeze/prohibition
  - **support:**
    - FCT-021
    - FCT-022
    - FCT-023
  - **to:** regulated economic actors

### IMPACT_MAP
- **administrative_power:** VERIFIED
- **electoral_effect:** NOT_ESTABLISHED_COUNTERFACTUALLY
- **judicial_correction:** VERIFIED_CASE_SPECIFIC
- **material_restriction:** VERIFIED_CASE_SPECIFIC
- **political_behavior:** NOT_ESTABLISHED
- **political_motive:** NOT_ESTABLISHED_GENERALLY
- **support:**
  - FCT-003
  - FCT-012
  - FCT-017
  - FCT-025
  - FCT-027
  - FCT-028

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** statutes use distinct administrative criteria and review
  - **issue:** preventive authority versus criminal guilt
  - **pro:** severe measures operate before/no conviction prerequisite
  - **resolution:** DISTINCT_LEGAL_OBJECTS
- **item 2:**
  - **contra:** Soulèvements, Mazepin and Fridman controls show reversals/annulments
  - **issue:** judicial deference versus effective correction
  - **pro:** several measures upheld
  - **resolution:** CASE_SPECIFIC_REVIEW
- **item 3:**
  - **contra:** no general partisan tasking/motive evidence in examined cases
  - **issue:** foreign interference protection versus political weaponization
  - **pro:** French law expressly targets foreign-power-linked conduct
  - **resolution:** MOTIVE_EDGE_OPEN
- **item 4:**
  - **contra:** no causal behavior/electoral design
  - **issue:** material restriction versus political/electoral effect
  - **pro:** freezes/dissolutions/expulsions are consequential
  - **resolution:** I6_I7_NOT_ESTABLISHED

### VERIFICATION_REPORT
- **cross_checks:**
  - French statutory power versus Conseil d’État review
  - EU listing rules versus General Court annulments
  - positive preventive-power cases versus negative correction controls
- **facts:** 28
- **limitations:**
  - official/legal corpus captures formal/adjudicated mechanisms
  - no prevalence denominator
  - no causal electoral dataset
- **negative_controls:**
  - Soulèvements de la Terre annulment
  - Mazepin annulment
  - Fridman annulment
- **primary_or_official_dominant:** true
- **provenance_families:** 7
- **sources:** 14
- **verdict:** READY_FOR_PRE_GATE

### EDI_REPORT
- **corpus:**
  - **circularity:** LOW
  - **coverage:** STRONG_FOR_FORMAL_POWERS_AND_REVIEW_PARTIAL_FOR_MOTIVE_AND_EFFECT
  - **independence:** HIGH_ACROSS_FRENCH_STATUTE_FRENCH_COURTS_EU_LAW_COUNCIL_GUIDELINES_CURIA
  - **limits:**
    - official/legal corpus focused on formal/adjudicated mechanisms
    - no prevalence denominator
    - no causal electoral dataset
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **gap_type:** ATTRIBUTION
    - **independent_families:** 1
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES
    - **gap_type:** SCOPE
    - **independent_families:** 3
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** YES
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 2
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** YES
    - **gap_type:** EVIDENCE
    - **independent_families:** 3
  - **item 5:**
    - **claim_id:** CLM-005
    - **direct_object:** YES_WITH_BOUNDARIES
    - **gap_type:** SCOPE
    - **independent_families:** 2
  - **item 6:**
    - **claim_id:** CLM-006
    - **direct_object:** NO_CAUSAL_DESIGN
    - **gap_type:** CAUSALITY
    - **independent_families:** 4
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** 7_PROVENANCE_FAMILIES
  - **perspective:** FR_STATUTE+FR_COURTS+EU_LAW+COUNCIL+CURIA
  - **stratification:** FREEZE+DISSOLUTION+EXPULSION+LISTING+REVIEW
  - **temporal:** 2017-2026
- **edi:**
  - **assessment:** STRONG_MECHANISM_AND_REVIEW_COVERAGE_WITH_MOTIVE_AND_CAUSAL_GAPS
- **flags:**
  - OFFICIAL_PRIMARY_DOMINANT
  - POSITIVE_PREVENTIVE_POWER_CONTROLS
  - NEGATIVE_JUDICIAL_CORRECTION_CONTROLS
  - NO_CAUSAL_ELECTORAL_DESIGN
- **source_counts:**
  - **claim_source:** 0
  - **primary:** 14
  - **provenance_families:** 7
  - **secondary:** 0
  - **total:** 14

### RESPONSIBILITY_MAP
- **boundary:** administrative coercion and legal defect can be established without inferring criminal guilt, partisan motive or electoral effect
- **not_established:**
  - general partisan motive
  - general misuse by political authorities
  - political persuasion
  - electoral-result effect
- **verified:**
  - formal preventive powers
  - case-specific administrative decisions
  - effective judicial review and corrections
  - EU listing due-process requirements

### NEXT_QUERIES
- **item 1:**
  - **need:** synthesize litigation, administrative coercion, electoral annulment and financial restriction under a common lawfare standard
  - **route:** INV-129
- **item 2:**
  - **need:** comparative denominator for politically salient preventive measures if new structured data appears
  - **route:** INV-129
- **item 3:**
  - **condition:** new primary evidence of partisan tasking, discriminatory instruction or causal political outcome
  - **reopen:** INV-080

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-002,QRY-006,QRY-009,QRY-013,QRY-014 | support:- | counter:- | results:FCT-003,FCT-012,FCT-017,FCT-025,FCT-027,FCT-028 | final:GAP | gap:RESPONSIBILITY
LED-002 | attempts:QRY-006,QRY-009,QRY-013,QRY-014,QRY-015 | support:- | counter:- | results:FCT-012,FCT-017,FCT-025,FCT-027,FCT-028 | final:GAP | gap:CAUSALITY
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-010,QRY-011 | support:- | counter:- | results:FCT-001,FCT-003,FCT-005,FCT-007,FCT-009,FCT-019,FCT-021 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-004,QRY-005,QRY-009,QRY-011,QRY-012 | support:- | counter:- | results:FCT-001,FCT-007,FCT-009,FCT-018,FCT-022,FCT-024 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-006,QRY-007,QRY-008,QRY-009,QRY-013,QRY-014 | support:- | counter:- | results:FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,FCT-025,FCT-026,FCT-027 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-001,QRY-002 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-021,FCT-022,FCT-023,FCT-024,FCT-025,FCT-026,FCT-027 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-006,QRY-009,QRY-013,QRY-014,QRY-015 | support:- | counter:- | results:FCT-012,FCT-018,FCT-025,FCT-027,FCT-028 | final:GAP | gap:CAUSALITY
CLM-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,SRC-001,SRC-002,SRC-003,SRC-004 | support:FCT-001,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008 | counter:CTRL-001 | results:FCT-001,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,CTRL-001 | final:SUPPORTED | gap:ATTRIBUTION
CLM-002 | attempts:QRY-005,QRY-007,QRY-009,QRY-010,SRC-005,SRC-007,SRC-009,SRC-010 | support:FCT-009,FCT-010,FCT-013,FCT-017,FCT-019,FCT-020 | counter:CTRL-003;CTRL-004 | results:FCT-009,FCT-010,FCT-013,FCT-017,FCT-019,FCT-020,CTRL-003;CTRL-004 | final:SUPPORTED | gap:SCOPE
CLM-003 | attempts:QRY-006,QRY-007,QRY-008,QRY-009,SRC-006,SRC-007,SRC-008,SRC-009 | support:FCT-011,FCT-012,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018 | counter:CTRL-002 | results:FCT-011,FCT-012,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,CTRL-002 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-004 | attempts:QRY-011,QRY-012,SRC-011,SRC-012 | support:FCT-021,FCT-022,FCT-023,FCT-024 | counter:CTRL-005 | results:FCT-021,FCT-022,FCT-023,FCT-024,CTRL-005 | final:SUPPORTED | gap:EVIDENCE
CLM-005 | attempts:QRY-013,QRY-014,SRC-013,SRC-014 | support:FCT-025,FCT-026,FCT-027 | counter:CTRL-005 | results:FCT-025,FCT-026,FCT-027,CTRL-005 | final:SUPPORTED | gap:SCOPE
CLM-006 | attempts:QRY-006,QRY-009,QRY-011,QRY-013,QRY-014,SRC-006,SRC-009,SRC-011,SRC-013,SRC-014 | support:FCT-028,FCT-012,FCT-018,FCT-025,FCT-027 | counter:CTRL-006 | results:FCT-028,FCT-012,FCT-018,FCT-025,FCT-027,CTRL-006 | final:SUPPORTED | gap:CAUSALITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
AXS-006 | AXS | GAP | CAUSALITY | No prevalence, motive-command or electoral counterfactual design.
CLM-001 | CLM | SUPPORTED | ATTRIBUTION | The legal power does not by itself prove that any specific person satisfies the criteria.
CLM-002 | CLM | SUPPORTED | SCOPE | Different mechanisms are not legally identical and should not be collapsed into one sanction category.
CLM-003 | CLM | SUPPORTED | RESPONSIBILITY | Judicial correction does not establish bad faith in the initial decision.
CLM-004 | CLM | SUPPORTED | EVIDENCE | Compliance with formal due process must still be tested in each listing.
CLM-005 | CLM | SUPPORTED | SCOPE | Annulment of one listing period does not prove the target was factually innocent of every alleged conduct or that all sanctions are defective.
CLM-006 | CLM | SUPPORTED | CAUSALITY | No comparative prevalence or causal electoral design is present.
CAU-001 | CAU | GAP | CAUSALITY | Political-motive and high-causal-effect edges remain open.

SEMANTIC_COUNTS_V1:LED:2|CLM:6|AXS:6|CAU:1|CTRL:6|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-002","QRY-006","QRY-009","QRY-013","QRY-014"],"evidence_excerpt":"French and EU law permits freezes, dissolutions and expulsions without criminal conviction prerequisites; courts both uphold and annul individual measures.","gap":"The corpus proves broad preventive administrative powers and case-specific review but not a general edge from authority motive to partisan suppression.","gap_type":"RESPONSIBILITY","kind":"EVIDENCE_GAP","lead":"Administrative preventive measure to partisan instrumentalization","linked_ids":["CLM-006","CAU-001","CTRL-002","CTRL-005"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-003","FCT-012","FCT-017","FCT-025","FCT-027","FCT-028"],"routes":["INV-129"],"source_id":"INV-080_RUN_CARD","status":"GAP"}
LED-002 | {"attempt_ids":["QRY-006","QRY-009","QRY-013","QRY-014","QRY-015"],"evidence_excerpt":"The corpus reaches legal basis, measure, review and some material consequences but not high causal political effects.","gap":"No examined primary source supplies a design identifying voter persuasion, participation change or a counterfactual electoral result caused by the administrative measures.","gap_type":"CAUSALITY","kind":"CAUSAL_GAP","lead":"Administrative restriction to political behavior or electoral result","linked_ids":["CLM-006","CAU-001","CTRL-006"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-012","FCT-017","FCT-025","FCT-027","FCT-028"],"routes":["INV-129","INV-133"],"source_id":"INV-080_RUN_CARD","status":"GAP"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"French law expressly authorizes preventive asset freezes for acts of foreign interference, terrorism and serious narcotrafficking on administrative criteria without making a prior criminal conviction a textual prerequisite.","claimant":"INV-080 synthesis","counter":"CTRL-001","gap":"The legal power does not by itself prove that any specific person satisfies the criteria.","gap_type":"ATTRIBUTION","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008"]}
CLM-002 | {"claim":"French dissolution and expulsion mechanisms can impose severe restrictions through administrative action without a prior criminal judgment, but they remain subject to legality, evidence and proportionality review.","claimant":"INV-080 synthesis","counter":"CTRL-003;CTRL-004","gap":"Different mechanisms are not legally identical and should not be collapsed into one sanction category.","gap_type":"SCOPE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-009","FCT-010","FCT-013","FCT-017","FCT-019","FCT-020"]}
CLM-003 | {"claim":"Judicial review is substantively capable of both validating and reversing preventive administrative measures: the examined French cases include upheld dissolutions/expulsion and the annulled Soulèvements de la Terre dissolution.","claimant":"INV-080 synthesis","counter":"CTRL-002","gap":"Judicial correction does not establish bad faith in the initial decision.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-011","FCT-012","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018"]}
CLM-004 | {"claim":"EU restrictive measures freeze assets on defined listing criteria rather than criminal conviction, while the Council framework requires reasons, defence rights and effective judicial protection.","claimant":"INV-080 synthesis","counter":"CTRL-005","gap":"Compliance with formal due process must still be tested in each listing.","gap_type":"EVIDENCE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-021","FCT-022","FCT-023","FCT-024"]}
CLM-005 | {"claim":"The Mazepin and Fridman cases demonstrate that EU listings can fail judicial scrutiny where association or supporting evidence does not satisfy the applicable criteria; a listing therefore is not equivalent to criminal guilt or irrebuttable proof.","claimant":"INV-080 synthesis","counter":"CTRL-005","gap":"Annulment of one listing period does not prove the target was factually innocent of every alleged conduct or that all sanctions are defective.","gap_type":"SCOPE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-025","FCT-026","FCT-027"]}
CLM-006 | {"claim":"The examined corpus does not establish a general system in which preventive administrative measures are intentionally weaponized for partisan suppression or causally alter electoral outcomes.","claimant":"INV-080 synthesis","counter":"CTRL-006","gap":"No comparative prevalence or causal electoral design is present.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-028","FCT-012","FCT-018","FCT-025","FCT-027"]}

### AXIS_REGISTRY_V1
AXS-001 | {"assessment":"VERIFIED","attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-010","QRY-011"],"axis":"formal_preventive_powers","links":["CLM-001","CLM-002","CLM-004","CTRL-001"],"question":"What administrative measures can be imposed without a prior criminal conviction?","result_ids":["FCT-001","FCT-003","FCT-005","FCT-007","FCT-009","FCT-019","FCT-021"],"sought_objects":["ASSET_FREEZE","DISSOLUTION","EXPULSION","EU_LISTING"],"status":"SATURATED"}
AXS-002 | {"assessment":"VERIFIED_BOUNDED","attempt_ids":["QRY-001","QRY-004","QRY-005","QRY-009","QRY-011","QRY-012"],"axis":"evidentiary_threshold","links":["CLM-001","CLM-002","CLM-004","CTRL-001","CTRL-005"],"question":"What factual/legal thresholds replace criminal conviction in preventive administrative action?","result_ids":["FCT-001","FCT-007","FCT-009","FCT-018","FCT-022","FCT-024"],"sought_objects":["CONDUCT","THREAT","ASSOCIATION","SUPPORT","PROPORTIONALITY"],"status":"SATURATED"}
AXS-003 | {"assessment":"VERIFIED_CASE_SPECIFIC","attempt_ids":["QRY-006","QRY-007","QRY-008","QRY-009","QRY-013","QRY-014"],"axis":"judicial_review_and_correction","links":["CLM-003","CLM-005","CTRL-002","CTRL-004","CTRL-005"],"question":"Can courts meaningfully reverse or narrow administrative measures?","result_ids":["FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018","FCT-025","FCT-026","FCT-027"],"sought_objects":["ANNULMENT","UPHOLDING","PROPORTIONALITY","ERROR_OF_ASSESSMENT"],"status":"SATURATED"}
AXS-004 | {"assessment":"VERIFIED_TEXTUAL","attempt_ids":["QRY-001","QRY-002"],"axis":"foreign_interference_freeze","links":["CLM-001","CTRL-001"],"question":"Does French law now provide a direct preventive financial measure for foreign interference?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004"],"sought_objects":["FOREIGN_POWER","REQUEST_OR_BEHALF","ASSET_FREEZE","CONTROL_OR_INSTRUCTIONS"],"status":"SATURATED"}
AXS-005 | {"assessment":"VERIFIED","attempt_ids":["QRY-011","QRY-012","QRY-013","QRY-014"],"axis":"eu_restrictive_measures_due_process","links":["CLM-004","CLM-005","CTRL-005"],"question":"How are EU asset-freeze listings bounded by reasons and judicial protection?","result_ids":["FCT-021","FCT-022","FCT-023","FCT-024","FCT-025","FCT-026","FCT-027"],"sought_objects":["LISTING_CRITERIA","REASONS","RIGHTS_OF_DEFENCE","DELISTING"],"status":"SATURATED"}
AXS-006 | {"assessment":"NOT_ESTABLISHED","attempt_ids":["QRY-006","QRY-009","QRY-013","QRY-014","QRY-015"],"axis":"political_motive_and_effect","gap":"No prevalence, motive-command or electoral counterfactual design.","gap_type":"CAUSALITY","links":["CLM-006","LED-001","LED-002","CTRL-006"],"question":"Do the examined measures establish partisan motive or causal electoral effect?","result_ids":["FCT-012","FCT-018","FCT-025","FCT-027","FCT-028"],"sought_objects":["PARTISAN_MOTIVE","TASKING","PERSUASION","ELECTORAL_RESULT"],"status":"GAP"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"CTRL-002;CTRL-004;CTRL-005;CTRL-006","gap":"Political-motive and high-causal-effect edges remain open.","gap_type":"CAUSALITY","limit":"The chain is strongly supported through measure and judicial review, but partisan motive, persuasion and electoral-result edges are not established.","mechanism":"authority/legal basis -> administrative assessment of conduct/threat/association -> preventive measure or listing -> material restriction -> notice/review/litigation -> confirmation, narrowing or annulment -> possible political effect","status":"GAP","support":["FCT-003","FCT-009","FCT-012","FCT-017","FCT-021","FCT-025","FCT-027"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"The French interference-freeze statute is a positive control for explicit administrative power: it defines foreign-power tasking and authorizes a preventive asset freeze without a conviction prerequisite.","status":"VERIFIED","support":["FCT-001","FCT-003","FCT-004"]}
CTRL-002 | {"control":"The Soulèvements de la Terre annulment demonstrates that judicial review can invalidate a severe administrative measure for disproportionality even where some underlying conduct is established.","status":"VERIFIED_NEGATIVE_CONTROL","support":["FCT-011","FCT-012"]}
CTRL-003 | {"control":"Conseil d’État case law distinguishes dissolution as administrative police rather than criminal punishment, preventing automatic sanction/guilt conflation.","status":"VERIFIED","support":["FCT-013","FCT-014"]}
CTRL-004 | {"control":"The Iquioussen decision disaggregated government grounds, rejecting some as insufficient while accepting others; review is not reducible to wholesale deference or wholesale rejection.","status":"VERIFIED_CASE_SPECIFIC","support":["FCT-017","FCT-018"]}
CTRL-005 | {"control":"EU sanctions guidelines and General Court annulments provide a positive control for effective due-process/evidence constraints on listings.","status":"VERIFIED","support":["FCT-023","FCT-024","FCT-025","FCT-026","FCT-027"]}
CTRL-006 | {"control":"No examined source establishes a causal electoral result or general partisan instrumentalization from preventive administrative measures.","status":"NEGATIVE_CONTROL","support":["FCT-028"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:1|FETCH:14|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | MNEMO_UNAVAILABLE degraded; exact snapshot search unavailable in this environment | MnemoLite | NONE | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | PASS | SRC-001 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000050053961/2025-05-20 | FETCH exact primary source for INV-080: Code monétaire et financier — article L562-1
QRY-002 | FETCH | PASS | SRC-002 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000050053951 | FETCH exact primary source for INV-080: Code monétaire et financier — article L562-2-1
QRY-003 | FETCH | PASS | SRC-003 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033475988/2026-05-17 | FETCH exact primary source for INV-080: Code monétaire et financier — article L562-2
QRY-004 | FETCH | PASS | SRC-004 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051739332/2026-05-07 | FETCH exact primary source for INV-080: Code monétaire et financier — article L562-2-2
QRY-005 | FETCH | PASS | SRC-005 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043982161/2026-01-28 | FETCH exact primary source for INV-080: Code de la sécurité intérieure — article L212-1
QRY-006 | FETCH | PASS | SRC-006 | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2023-11-09/476384 | FETCH exact primary source for INV-080: Conseil d’État n°476384 — Les Soulèvements de la Terre
QRY-007 | FETCH | PASS | SRC-007 | https://www.conseil-etat.fr/fr/arianeweb/CE/analyse/2023-11-09/460457 | FETCH exact primary source for INV-080: Conseil d’État n°460457 — dissolution groupement extrême droite
QRY-008 | FETCH | PASS | SRC-008 | https://www.conseil-etat.fr/fr/arianeweb/CE/analyse/2023-11-09/464412 | FETCH exact primary source for INV-080: Conseil d’État n°464412 — dissolution GALE
QRY-009 | FETCH | PASS | SRC-009 | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2022-08-30/466554 | FETCH exact primary source for INV-080: Conseil d’État n°466554 — expulsion Hassan Iquioussen
QRY-010 | FETCH | PASS | SRC-010 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049050672/2026-05-01 | FETCH exact primary source for INV-080: CESEDA — article L631-3
QRY-011 | FETCH | PASS | SRC-011 | https://eur-lex.europa.eu/eli/reg/2014/269/2024-01-03/eng | FETCH exact primary source for INV-080: Règlement (UE) n°269/2014 — mesures restrictives Ukraine
QRY-012 | FETCH | PASS | SRC-012 | https://data.consilium.europa.eu/doc/document/ST-11618-2024-INIT/en/pdf | FETCH exact primary source for INV-080: Council of the EU — Guidelines on implementation and evaluation of restrictive measures
QRY-013 | FETCH | PASS | SRC-013 | https://curia.europa.eu/jcms/upload/docs/application/pdf/2024-03/cp240049en.pdf | FETCH exact primary source for INV-080: General Court — Mazepin v Council T-743/22
QRY-014 | FETCH | PASS | SRC-014 | https://infocuria.curia.europa.eu/tabs/redirect/juris/liste.jsf?num=T-304%2F22 | FETCH exact primary source for INV-080: General Court — Fridman v Council T-304/22
QRY-015 | WEB | PASS | - | - | REFUTATION INV-080: search examined primary corpus for proof that preventive administrative measures/listings were intentionally weaponized for partisan suppression and causally changed an electoral result.

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | LEGIARTI000050053961 | Code monétaire et financier — article L562-1 | 2024-07-25 | 2026-09-07T22:20:00+02:00 | definition acte ingérence; commande étrangère; atteinte institutions | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000050053961/2025-05-20
SRC-002 | ◈ | fam:A | LEGIARTI000050053951 | Code monétaire et financier — article L562-2-1 | 2024-07-25 | 2026-09-07T22:20:00+02:00 | gel préventif pour actes ingérence; ministres; six mois renouvelable | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000050053951
SRC-003 | ◈ | fam:A | LEGIARTI000033475988 | Code monétaire et financier — article L562-2 | 2016-11-24 | 2026-09-07T22:20:00+02:00 | gel terrorisme; personnes et entités contrôlées/instructions | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033475988/2026-05-17
SRC-004 | ◈ | fam:A | LEGIARTI000051739332 | Code monétaire et financier — article L562-2-2 | 2025-06-13 | 2026-09-07T22:20:00+02:00 | gel narcotrafic; menace grave; durée et renouvellement | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051739332/2026-05-07
SRC-005 | ◈ | fam:B | LEGIARTI000043982161 | Code de la sécurité intérieure — article L212-1 | 2021-08-24 | 2026-09-07T22:20:00+02:00 | dissolution administrative; motifs; décret conseil ministres | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043982161/2026-01-28
SRC-006 | ◈ | fam:C | CE-476384 | Conseil d’État n°476384 — Les Soulèvements de la Terre | 2023-11-09 | 2026-09-07T22:20:00+02:00 | annulation dissolution; nécessité et proportionnalité; contrôle excès de pouvoir | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2023-11-09/476384
SRC-007 | ◈ | fam:C | CE-460457 | Conseil d’État n°460457 — dissolution groupement extrême droite | 2023-11-09 | 2026-09-07T22:20:00+02:00 | dissolution = mesure police administrative; faits justifiant dissolution | https://www.conseil-etat.fr/fr/arianeweb/CE/analyse/2023-11-09/460457
SRC-008 | ◈ | fam:C | CE-464412 | Conseil d’État n°464412 — dissolution GALE | 2023-11-09 | 2026-09-07T22:20:00+02:00 | dissolution; propos haineux; contrôle CEDH | https://www.conseil-etat.fr/fr/arianeweb/CE/analyse/2023-11-09/464412
SRC-009 | ◈ | fam:D | CE-466554 | Conseil d’État n°466554 — expulsion Hassan Iquioussen | 2022-08-30 | 2026-09-07T22:20:00+02:00 | expulsion administrative; motifs retenus/non retenus; référé | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2022-08-30/466554
SRC-010 | ◈ | fam:D | LEGIARTI000049050672 | CESEDA — article L631-3 | 2024-01-26 | 2026-09-07T22:20:00+02:00 | expulsion protégés; comportements graves; exceptions condamnations | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049050672/2026-05-01
SRC-011 | ◈ | fam:E | CELEX-02014R0269-20240103 | Règlement (UE) n°269/2014 — mesures restrictives Ukraine | 2014-03-17 | 2026-09-07T22:20:00+02:00 | gel fonds ressources; critères inscription; motifs liste | https://eur-lex.europa.eu/eli/reg/2014/269/2024-01-03/eng
SRC-012 | ◈ | fam:other:consilium | ST-11618-2024-INIT | Council of the EU — Guidelines on implementation and evaluation of restrictive measures | 2024-07-02 | 2026-09-07T22:20:00+02:00 | due process; clear criteria; defendable reasons; notification and delisting | https://data.consilium.europa.eu/doc/document/ST-11618-2024-INIT/en/pdf
SRC-013 | ◈ | fam:other:curia | T-743/22 | General Court — Mazepin v Council T-743/22 | 2024-03-20 | 2026-09-07T22:20:00+02:00 | annulment of maintenance; family link insufficient | https://curia.europa.eu/jcms/upload/docs/application/pdf/2024-03/cp240049en.pdf
SRC-014 | ◈ | fam:other:curia | T-304/22 | General Court — Fridman v Council T-304/22 | 2024-04-10 | 2026-09-07T22:20:00+02:00 | annulment action granted; error of assessment; asset freeze | https://infocuria.curia.europa.eu/tabs/redirect/juris/liste.jsf?num=T-304%2F22

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000050053961/2025-05-20 | A | 2026-09-07 | Administrative definition of foreign interference | French law defines an act of interference as conduct committed directly or indirectly at the request of or on behalf of a foreign power and aimed at or having the effect of harming fundamental national interests, essential infrastructure integrity, or regular functioning of democratic institutions. | -
FCT-002 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000050053961/2025-05-20 | A | 2026-09-07 | Means of interference | The statutory definition expressly includes false or inaccurate information as a possible means, while the decisive element remains the foreign-power request/on-behalf edge plus the protected-interest harm object or effect. | -
FCT-003 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000050053951 | A | 2026-09-07 | Preventive freeze for interference | Since July 2024, the French economy and interior ministers may jointly freeze funds and economic resources for six renewable months for the sole purpose of preventing acts of interference. | -
FCT-004 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000050053951 | A | 2026-09-07 | Interference-freeze reach | The interference-freeze power reaches assets of persons or entities committing, attempting, facilitating or financing interference and entities controlled by or knowingly acting for them or on their instructions. | -
FCT-005 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033475988/2026-05-17 | A | 2026-09-07 | Terrorism freeze comparator | French law separately authorizes the economy and interior ministers to freeze assets linked to persons or entities committing, attempting, facilitating or financing terrorist acts for renewable six-month periods. | -
FCT-006 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033475988/2026-05-17 | A | 2026-09-07 | Administrative freeze not conviction prerequisite | Article L562-2 formulates the terrorism freeze around administrative findings about conduct/control/instructions and does not make a prior criminal conviction a textual prerequisite to the freeze. | -
FCT-007 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051739332/2026-05-07 | A | 2026-09-07 | Narcotraffic freeze comparator | Since June 2025, French ministers may freeze assets linked to serious narcotrafficking threats for six months renewable up to seven times after informing the specialized prosecutor. | -
FCT-008 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051739332/2026-05-07 | A | 2026-09-07 | Preventive architecture across risks | The narcotrafficking provision confirms a preventive administrative architecture distinct from criminal adjudication, while adding a particular-gravity public-order threshold and prosecutor information. | -
FCT-009 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043982161/2026-01-28 | B | 2026-09-07 | Administrative dissolution grounds | Article L212-1 of the Internal Security Code authorizes dissolution by decree in Council of Ministers on enumerated public-order, violence, discrimination/hate and terrorism grounds. | -
FCT-010 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043982161/2026-01-28 | B | 2026-09-07 | Dissolution not conditioned on criminal conviction | The statutory dissolution mechanism is framed as an administrative decree based on organizational conduct; the text does not require a prior criminal conviction of the association or group as a condition. | -
FCT-011 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2023-11-09/476384 | C | 2026-09-07 | Proportionality control of dissolution | The Conseil d’État requires a dissolution under L212-1 to be adapted, necessary and proportionate to the gravity of the public-order disturbances attributable to the organization. | -
FCT-012 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2023-11-09/476384 | C | 2026-09-07 | Soulèvements dissolution annulled | The Conseil d’État annulled the 2023 dissolution of Les Soulèvements de la Terre even though it accepted that some provocations to violence against property were attributable, because dissolution was not proportionate to the gravity and real effects at the date of the decree. | -
FCT-013 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/analyse/2023-11-09/460457 | C | 2026-09-07 | Dissolution classified as police measure | In decision 460457, the Conseil d’État expressly classified a dissolution under L212-1 as a measure of administrative police rather than a sanction. | -
FCT-014 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/analyse/2023-11-09/460457 | C | 2026-09-07 | Dissolution may nevertheless be upheld | The same decision upheld dissolution of an extreme-right group on facts found sufficient under the statutory discrimination, hate or violence ground, showing that judicial review can validate the measure case-specifically. | -
FCT-015 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/analyse/2023-11-09/464412 | C | 2026-09-07 | GALE dissolution upheld | In decision 464412, the Conseil d’État upheld dissolution of the Groupe Antifasciste Lyon et Environs based on recurrent hateful statements and conduct assessed under L212-1. | -
FCT-016 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/analyse/2023-11-09/464412 | C | 2026-09-07 | Rights review does not imply automatic invalidity | The Conseil d’État assessed the dissolution against Articles 10 and 11 ECHR and did not find a violation in that case, showing that severe administrative measures can survive rights review when the factual and proportionality thresholds are met. | -
FCT-017 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2022-08-30/466554 | D | 2026-09-07 | Iquioussen expulsion administrative decision | The French interior minister ordered Hassan Iquioussen’s expulsion and withdrawal of residence status in July 2022; the Conseil d’État ultimately refused to suspend the measure under the applicable expulsion framework. | -
FCT-018 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2022-08-30/466554 | D | 2026-09-07 | Judicial disaggregation of government grounds | In the Iquioussen litigation, the Conseil d’État rejected some asserted grounds as insufficient in the record but found other repeated statements sufficient to justify expulsion, demonstrating ground-by-ground judicial review rather than automatic deference. | -
FCT-019 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049050672/2026-05-01 | D | 2026-09-07 | Current protected-person expulsion threshold | Article L631-3 currently permits expulsion of otherwise protected foreigners in specified cases involving threats to fundamental state interests, particularly grave violations of republican principles, terrorism-related activity, or explicit deliberate incitement to discrimination, hatred or violence. | -
FCT-020 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049050672/2026-05-01 | D | 2026-09-07 | Conviction and behavior are distinct legal routes | The current provision separately contains conviction-based derogations, confirming that a final criminal conviction is one route among others and not synonymous with the behavioral grounds supporting administrative expulsion. | -
FCT-021 | FACT | ✧ | https://eur-lex.europa.eu/eli/reg/2014/269/2024-01-03/eng | E | 2026-09-07 | EU restrictive-measure freeze | Regulation 269/2014 requires freezing all funds and economic resources of listed persons/entities and prohibits making funds or resources available to them. | -
FCT-022 | FACT | ✧ | https://eur-lex.europa.eu/eli/reg/2014/269/2024-01-03/eng | E | 2026-09-07 | EU listing based on defined criteria and reasons | The regulation ties listing to specified policy/support/association criteria and requires grounds for listing and identifying information; the mechanism is not textually conditioned on a criminal conviction. | -
FCT-023 | FACT | ✧ | https://data.consilium.europa.eu/doc/document/ST-11618-2024-INIT/en/pdf | other:consilium | 2026-09-07 | EU sanctions due-process requirements | Council sanctions guidelines state that targeted listings must respect fundamental rights, including rights of defence and effective judicial protection. | -
FCT-024 | FACT | ✧ | https://data.consilium.europa.eu/doc/document/ST-11618-2024-INIT/en/pdf | other:consilium | 2026-09-07 | EU listing reasons must be defendable | The Council guidelines require clear case-specific listing criteria and accurate, up-to-date and defendable statements of reasons, with notification and opportunities to make views known and seek delisting. | -
FCT-025 | FACT | ✧ | https://curia.europa.eu/jcms/upload/docs/application/pdf/2024-03/cp240049en.pdf | other:curia | 2026-09-07 | Mazepin retention annulled | The General Court annulled acts maintaining Nikita Mazepin on EU sanctions lists because the asserted association/common-interest link with his father was not sufficiently established. | -
FCT-026 | FACT | ✧ | https://curia.europa.eu/jcms/upload/docs/application/pdf/2024-03/cp240049en.pdf | other:curia | 2026-09-07 | Family relationship insufficient for continued sanctions | The General Court stated that family relationship alone was insufficient to establish common interests justifying continued restrictive measures against Nikita Mazepin. | -
FCT-027 | FACT | ✧ | https://infocuria.curia.europa.eu/tabs/redirect/juris/liste.jsf?num=T-304%2F22 | other:curia | 2026-09-07 | Fridman inclusion annulled for error of assessment | In T-304/22 the General Court granted Mikhail Fridman’s annulment action concerning his inclusion/maintenance on EU restrictive-measure lists for the February 2022 to March 2023 period, on error-of-assessment grounds. | -
FCT-028 | FACT | ✦ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2023-11-09/476384 | C,D,E,other:curia | 2026-09-07 | Causal and motive ceiling of preventive administrative measures | The examined primary corpus establishes powerful preventive measures, case-specific judicial validation and reversals, but does not establish a general chain from administrative measure to partisan motive, voter persuasion, or a counterfactual electoral result. | -
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
FCT-028 | SRC-006,SRC-009,SRC-011,SRC-013,SRC-014

## REFUTATION_REGISTRY_V1
FCT-028 | QRY-015 | NONE

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
FCT-028 | ELIGIBLE:CONFIRME

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
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8
CP-002 | SEARCH | PASS | LAST_COMPLETED:9:CORPUS | NEXT_ACTION:10
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11:CAU-001 | NEXT_ACTION:12
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-07T20:34:07.679674+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:CONFIRME","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":28,"eligible":28,"failure":0,"success":0}}

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
FCT-028 | ELIGIBLE:CONFIRME | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
