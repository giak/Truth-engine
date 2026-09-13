ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260906-1555-propriete-medias-francais | PARENT_RUN_ID:NONE | AS_OF:2026-09-06
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/truth-engine/investigations/2026-09/2026-09-06_propriete-medias-francais/2026-09-06_15-55_propriete-medias-francais_INPUT.md | SUBJECT_SLUG:propriete-medias-francais | SUBJECT_FP:sha256:6141501e9cca1cc33a9f24b5a5dfbae3d5ee0aef17ccc608cb76b6f635373be6 | INPUT_SHA256:sha256:aaf5026a47bda414d9f93edb98215c361a5c329671c7c543a26227f317ab7dbe
COMPLEXITY:8→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['Groupe Le Monde', 'Dassault Médias', 'LVMH/Groupe Les Echos-Le Parisien', 'Presse Indépendante/FDPI', 'SIPA Ouest-France', 'CMA Media', 'public service media', 'Arcom'], 'domains': ['print news', 'regional daily press', 'television', 'radio', 'digital news', 'media ownership/control', 'media pluralism regulation'], 'exclusions': ['automatic property-to-editorial-causality inference', 'single all-media percentage without common denominator', 'wealth status as a substitute for legal ownership/control'], 'geo': 'France', 'lead_question': 'test 9 billionaires / 80-90 percent claims by reconstructing denominator and current legal control', 'limits': ['each percentage requires an explicit universe/date/metric', 'ownership/control, financing, audience and editorial influence are separate objects', 'political/parliamentary concentration figures are claims until reproducible from a stated method', 'do not infer ownership -> editorial line'], 'object_question': "Quelle est la concentration réelle de la propriété et du contrôle des médias d'information français, selon des dénominateurs explicites et comparables (audience, diffusion, chiffre d'affaires, titres/chaînes/sites et contrôle capitalistique), et que permettent réellement de conclure ces mesures sur le pluralisme sans confondre propriété, audience et contrôle éditorial ?", 'period': '2010-2026; focus on current ownership and 2025-2026 measurement'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Résultat technique

`CLM-001` est le résultat central : la formule générique « 9/11 milliardaires possèdent 80-90 % des médias français » n'est pas une statistique universelle reproductible à partir des sources publiques examinées. Les chiffres retrouvés changent avec l'année, le secteur et la métrique. `FCT-001` borne explicitement le 91,4 % de 2021 à la **diffusion des quotidiens nationaux généralistes**. `FCT-002` et `FCT-003` montrent ensuite des formulations parlementaires différentes pour 2022 et 2026, mêlant propriété de quotidiens et parts d'audience radio/télévision. `CLM-005` conserve les chiffres 2026 comme claims publics, pas comme pourcentages indépendamment reproduits.

`CLM-002` interdit donc l'extension silencieuse du 91,4 % à « tous les médias ». Les classements ACPM renforcent cette garde : `FCT-004` décrit un univers PQN de 11 supports en 2025, tandis que `FCT-005` décrit séparément 63 supports de presse quotidienne régionale. `FCT-006` et `CTRL-002` établissent qu'un dénominateur PQN ne représente pas à lui seul la presse quotidienne française. Ouest-France, premier titre PQR à 581 505 exemplaires payés en 2025, est en outre rattaché à une structure associative sans but lucratif (`FCT-010`).

`CLM-003` montre qu'une carte historique des propriétaires ne peut pas être réutilisée comme état 2026. Le Groupe Le Monde indique désormais une structure capitalistique dominée par le Fonds pour l'indépendance de la presse et le Pôle d'indépendance, Xavier Niel ne conservant qu'une action (`FCT-007`, `CTRL-001`). À l'inverse, les disclosures actuels maintiennent Dassault Médias au-dessus de 95 % de la Société du Figaro (`FCT-008`) et LVMH comme maison mère du Groupe Les Echos-Le Parisien (`FCT-009`). Le nombre de « milliardaires propriétaires » dépend donc aussi de la définition juridique retenue et de la date de photographie.

Le rejet d'un slogan mal dénommé ne conduit pas à nier la concentration. `CLM-004` repose sur deux contrôles indépendants : la Commission européenne rapporte pour la France un risque de 71 % sur l'indicateur MPM2026 de pluralité du marché (`FCT-014`), et CMA CGM documente la poursuite de la consolidation cross-media avec Brut et Chérie 25 en 2025 (`FCT-013`). `CTRL-003` interdit cependant de transformer le 71 % de risque MPM en « 71 % des médias possédés » : ce sont deux objets numériques différents.

`CLM-008` montre pourquoi un unique pourcentage cross-media actuel n'est pas disponible dans l'infrastructure publique examinée. L'Arcom décrit encore sa base de transparence comme une préfiguration couvrant la télévision et la radio hertziennes, destinée à être étendue notamment à la presse et aux médias en ligne (`FCT-012`). Le droit anti-concentration décrit par l'Arcom utilise lui-même des critères sectoriels distincts pour télévision, radio et presse quotidienne nationale imprimée, dont un seuil de 20 % de la diffusion de cette dernière catégorie (`FCT-011`). Il n'existe donc pas, dans ces sources, un dénominateur officiel unique permettant d'additionner proprement titres, chaînes, radios, sites, diffusion et audience en un seul « X % des médias ».

`CLM-007` fixe enfin la frontière de causalité. Propriété juridique, financement, audience et influence éditoriale sont quatre objets différents. Le cas Libération l'illustre : `FCT-015` documente une structure de propriété séparée d'Altice, tandis que `FCT-016` documente en 2026 un prêt supplémentaire de 17 millions d'euros de Daniel Křetínský. Une relation de financement peut créer une dépendance matérielle, mais elle ne vaut ni propriété juridique, ni instruction éditoriale, ni effet démontré. `CAU-001` et `CAU-002` restent donc `UNRESOLVED` : la chaîne propriété/financement -> intervention éditoriale relève d'INV-082 et doit être documentée par des droits de gouvernance, des traces d'intervention ou d'autres preuves propres, pas par inférence.

# Conclusion technique

Le corpus doit remplacer toute formule globale « 80-90 % des médias » par une matrice explicite **métrique × univers × date × définition du contrôle**. La concentration de la propriété et des ressources médiatiques françaises est un objet réel et matériel, mais son ampleur ne peut être résumée honnêtement par un pourcentage unique sans définir le secteur et le dénominateur. Les anciennes cartes doivent en outre être revalidées avant réemploi, car l'actionnariat a changé matériellement au moins pour le Groupe Le Monde et le paysage continue de se consolider ailleurs.

# Limites matérielles

La méthode publique sous-jacente aux chiffres parlementaires 2026 de 93 % / ~60 % / 50 % n'a pas été reproduite dans ce run (`CLM-005`). La base Arcom n'offre pas encore le périmètre presse + en ligne nécessaire à une reconstruction cross-media officielle (`CLM-008`). Les effets de la propriété ou du financement sur les décisions éditoriales et sur les résultats démocratiques ne sont pas établis ici (`CAU-001..002`). Ces limites sont des frontières de mesure et de causalité ; les combler par davantage de cartes descriptives non dénommées serait du fishing.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:0|EDI_DECISIVE:4|SRC_COMPLETE:15/15

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-06
- **material_changes:**
  - Groupe Le Monde ownership transfer completed before 2026
  - CMA Media acquisitions in 2025
  - current Arcom transparency database still incomplete for print/online
- **measurement_focus:** ACPM 2025 circulation and 2026 ownership/regulatory state
- **period:** 2010-2026
- **refresh_rule:** recheck ownership map and Arcom/EMFA database after major transaction or database expansion

### MANIPULATION_REPORT
- **assumptions:**
  - ownership/control is not editorial influence
  - risk score is not ownership share
  - parliamentary claims require reproducible method before certification
- **clusters:**
  - NONE
- **complexity:**
  - **band:** COMPLEX
  - **score:** 8
- **implicit:**
  - do not turn billionaire status into proof of control
  - do not turn ownership into proof of editorial intervention
  - do not turn risk score into ownership percentage
- **input_kind:** TOPIC
- **mission_mode:** INVESTIGATION
- **patterns:**
  - denominator reconstruction
  - ownership/control recheck
  - cross-sector non-comparability
  - causal-boundary enforcement
- **priorities:**
  - trace slogan provenance
  - certified print denominators
  - current legal ownership
  - official regulatory scope
  - independent plurality-risk control
- **query_guidance:**
  - prefer certified circulation and legal/owner disclosures
  - recheck current 2026 ownership after historic transfer
  - separate sector denominators
  - use independent regulatory/pluralism evidence as control
- **rhetorical:**
  - NONE
- **speaker:** N/A(TOPIC)
- **symbol_stage:** FINAL
- **symbols:**
  - **M:** 0
  - **Κ:** 0
  - **Λ:** 4
  - **Ξ:** 2
  - **Σ:** 0
  - **Φ:** 0
  - **Ψ:** 0
  - **Ω:** 0
  - **κ:** 0
  - **ρ:** 1
  - **€:** 2
  - **↕:** 3
  - **⏰:** 4
  - **⚔:** 0
  - **⫸:** 3
- **threats:**
  - NONE

### MODULE_EXECUTION
NONE

### SCOPING_REPORT
- **geo:** France
- **measurement_contract:**
  - No percentage without universe, date and metric.
  - Keep legal ownership/control, financing, circulation/audience and editorial influence separate.
  - Treat prior corpus and parliamentary figures as leads until reproducible.
  - Do not infer ownership -> editorial line; that belongs to INV-082.
- **object:** Current ownership/control concentration of French news media, with explicit denominators and dates.
- **period:** 2010-2026; current measurement focused on 2025-2026.
- **priority_tests:**
  - Reconstruct provenance of 80-90% slogans.
  - Build current print circulation denominators from ACPM.
  - Recheck current legal ownership of key groups/titles.
  - Test whether a unified official cross-media denominator exists.
  - Use independent pluralism-risk evidence without confusing risk scores with ownership shares.

### CREDO
- No percentage without universe, date and metric.
- Legal ownership/control is distinct from financing.
- Circulation/audience is distinct from ownership.
- Ownership is not editorial tasking or effect.
- A risk indicator is not a market share.
- Current ownership must be rechecked before reuse of historical maps.

### COGNITIVE_MAP
- **causal_boundary:** ownership/control and financing establish structural capability/dependency context; editorial intervention and democratic effects require separate evidence
- **core_model:** media concentration must be represented as metric x universe x date x control-definition, not one denominator-free percentage
- **observed_structure:**
  - narrow historical PQN concentration claims
  - current legal ownership changes
  - large PQR universe including associative ownership
  - sector-specific regulation
  - ongoing cross-media consolidation
  - high independent plurality-risk indicator
- **rival_models:**
  - 80-90% is a universal all-French-media ownership share
  - wealth category alone proves legal control
  - ownership automatically proves editorial tasking
  - rejecting slogan arithmetic means concentration is not a real issue

### DIALECTICAL_MAP
- **item 1:**
  - **evidence:**
    - CLM-001
    - CLM-002
    - CLM-005
    - CLM-008
  - **hypothesis:** 80-90% is a universal all-media ownership share
  - **result:** NOT_REPRODUCIBLE
- **item 2:**
  - **evidence:**
    - CLM-003
    - CTRL-001
  - **hypothesis:** old billionaire ownership maps remain current in 2026
  - **result:** CONTRADICTED_IN_PART
- **item 3:**
  - **evidence:**
    - CLM-006
    - CTRL-002
  - **hypothesis:** broadening from PQN does not change the ownership object
  - **result:** CONTRADICTED
- **item 4:**
  - **evidence:**
    - CLM-004
    - CTRL-003
  - **hypothesis:** concentration concern disappears if slogan is rejected
  - **result:** NOT_SUPPORTED
- **item 5:**
  - **evidence:**
    - CLM-007
    - CAU-001
    - CAU-002
  - **hypothesis:** ownership or financing alone proves editorial control
  - **result:** REFUSED

### RESOURCE_FLOW_MAP
- **item 1:**
  - **classification:** FINANCING_NOT_OWNERSHIP
  - **date:** 2026-03
  - **flow:** 17m euro loan
  - **from:** Daniel Kretinsky
  - **support:**
    - FCT-016
  - **to:** Liberation
- **item 2:**
  - **classification:** CORPORATE_CONTROL_EXPANSION
  - **date:** 2025
  - **flow:** acquisitions
  - **from:** CMA CGM/CMA Media
  - **support:**
    - FCT-013
  - **to:** Brut and Cherie 25

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** Dassault Medias
  - **relation:** shareholder >95%
  - **support:**
    - FCT-008
  - **to:** Societe du Figaro
- **item 2:**
  - **from:** LVMH
  - **relation:** media subsidiary
  - **support:**
    - FCT-009
  - **to:** Groupe Les Echos-Le Parisien
- **item 3:**
  - **from:** ASPDH
  - **relation:** non-profit ownership structure
  - **support:**
    - FCT-010
  - **to:** SA Ouest-France
- **item 4:**
  - **from:** Fonds pour independance de la presse / Pole independance
  - **relation:** capital structure
  - **support:**
    - FCT-007
  - **to:** Groupe Le Monde

### IMPACT_MAP
- **downstream:** INV-082 may test ownership/control -> editorial selection; INV-095 may consume corrected ownership denominators when other dependencies close
- **measured_objects:**
  - paid print circulation by ACPM universe
  - legal ownership/control disclosures
  - regulatory thresholds and database scope
  - current acquisition events
  - plurality-risk indicator
- **not_established:**
  - one all-media ownership market share
  - general editorial control from ownership
  - persuasion caused by ownership
  - electoral or democratic outcome caused by concentration

### CONTRADICTION_LEDGER
- **item 1:**
  - **claim:** 91.4% or 80-90% describes all French media
  - **counter:**
    - FCT-001
    - FCT-006
    - FCT-011
    - FCT-012
  - **resolution:** REJECT_UNIVERSAL_DENOMINATOR
- **item 2:**
  - **claim:** Xavier Niel currently owns Groupe Le Monde in the old direct-capital sense
  - **counter:**
    - FCT-007
  - **resolution:** UPDATE_OWNERSHIP_MAP
- **item 3:**
  - **claim:** billionaire financing equals legal ownership
  - **counter:**
    - FCT-015
    - FCT-016
  - **resolution:** SEPARATE_FINANCING_FROM_OWNERSHIP
- **item 4:**
  - **claim:** 71% MPM risk equals 71% ownership share
  - **counter:**
    - FCT-014
  - **resolution:** REJECT_METRIC_EQUIVALENCE

### VERIFICATION_REPORT
- **causal_assessment:** ownership/financing -> editorial control or democratic effect remains unresolved
- **facts:** 16
- **key_controls:**
  - current legal ownership
  - denominator expansion
  - independent MPM risk
- **known_limit:** no official current unified all-media ownership denominator; parliamentary 93/60/50 figures not independently reconstructed
- **sources:** 15
- **tier_policy:** facts retained at probable tier; no confirmed tier manufactured from same-family repetition
- **upstream_families:**
  - other:politis
  - other:assemblee_nationale
  - other:acpm
  - other:groupe_lemonde
  - other:lefigaro_legal
  - other:lvmh
  - other:ouest_france
  - other:arcom
  - other:cma_cgm
  - other:eu_commission
  - other:lemonde_press
  - other:strategies

### EDI_REPORT
- **corpus:**
  - **circularity:** two parliamentary claims share one institutional family; ACPM PQN/PQR share one measurement family
  - **counters:** 3
  - **coverage:** 0.92
  - **direct_objects:** 7
  - **edi_star:** 0.82
  - **independence:** 0.8
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 4
  - **item 2:**
    - **claim_id:** CLM-003
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 3
  - **item 3:**
    - **claim_id:** CLM-005
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** METHOD
    - **independent_families:** 1
  - **item 4:**
    - **claim_id:** CLM-007
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** CAUSALITY
    - **independent_families:** 2
- **diagnostic_not_truth:** true
- **dimensions:**
  - **geo:** 1.0
  - **lang:** 0.95
  - **owner:** 0.85
  - **persp:** N/A(methodological ownership object)
  - **strat:** 0.8
  - **temp:** 1.0
- **edi:**
  - **final:** 0.82
  - **flags:**
    - PARLIAMENTARY_PERCENTAGES_NOT_REPRODUCED
    - NO_UNIFIED_CROSS_MEDIA_DENOMINATOR
  - **penalties:** 0.06
  - **raw:** 0.88
- **source_counts:**
  - **primary:** 10
  - **secondary:** 5
  - **total:** 15

### RESPONSIBILITY_MAP
NONE

### NEXT_QUERIES
- **item 1:**
  - **query:** recompute cross-sector ownership map from disclosed beneficial/control data
  - **trigger:** Arcom/EMFA ownership database extends to print and online
- **item 2:**
  - **query:** reproduce each percentage from explicit title/group universe and date
  - **trigger:** methodology for parliamentary 93/60/50 figures is published
- **item 3:**
  - **query:** refresh legal-control map before corpus reuse
  - **trigger:** major media ownership transaction
- **item 4:**
  - **query:** seek governance rights, intervention traces and causal evidence rather than infer editorial control from ownership
  - **trigger:** INV-082 execution

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-001,QRY-002,QRY-003 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-004,QRY-005 | support:- | counter:- | results:FCT-004,FCT-005,FCT-006 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-006,QRY-007,QRY-008,QRY-009 | support:- | counter:- | results:FCT-007,FCT-008,FCT-009,FCT-010 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-010,QRY-011 | support:- | counter:- | results:FCT-011,FCT-012 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-012 | support:- | counter:- | results:FCT-013 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-013 | support:- | counter:- | results:FCT-014 | final:SATURATED | gap:NONE
AXS-007 | attempts:QRY-014,QRY-015 | support:- | counter:- | results:FCT-015,FCT-016 | final:SATURATED | gap:NONE
AXS-008 | attempts:QRY-006,QRY-008,QRY-014 | support:- | counter:- | results:FCT-007,FCT-008,FCT-015,FCT-016 | final:GAP | gap:CAUSALITY
CLM-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-010,QRY-011,SRC-001,SRC-002,SRC-003,SRC-010,SRC-011 | support:FCT-001,FCT-002,FCT-003,FCT-011,FCT-012 | counter:FCT-014(concentration risk remains high) | results:FCT-001,FCT-002,FCT-003,FCT-011,FCT-012,FCT-014(concentration risk remains high) | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-001,SRC-001 | support:FCT-001 | counter:- | results:FCT-001 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-006,QRY-007,QRY-008,SRC-006,SRC-007,SRC-008 | support:FCT-007,FCT-008,FCT-009 | counter:- | results:FCT-007,FCT-008,FCT-009 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-012,QRY-013,SRC-012,SRC-013 | support:FCT-013,FCT-014 | counter:- | results:FCT-013,FCT-014 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-003,SRC-003 | support:FCT-003 | counter:FCT-002(different 2022 actor counts and percentages) | results:FCT-003,FCT-002(different 2022 actor counts and percentages) | final:PARTIAL | gap:METHOD
CLM-006 | attempts:QRY-004,QRY-005,QRY-009,SRC-004,SRC-005,SRC-009 | support:FCT-004,FCT-005,FCT-006,FCT-010 | counter:- | results:FCT-004,FCT-005,FCT-006,FCT-010 | final:SUPPORTED | gap:NONE
CLM-007 | attempts:QRY-014,QRY-015,SRC-014,SRC-015 | support:FCT-015,FCT-016 | counter:- | results:FCT-015,FCT-016 | final:SUPPORTED | gap:NONE
CLM-008 | attempts:QRY-010,QRY-011,SRC-010,SRC-011 | support:FCT-011,FCT-012 | counter:- | results:FCT-011,FCT-012 | final:SUPPORTED | gap:NONE

## STATUS_DELTA_V1
DELTA-001 | AXS-008 | OPEN_GAP | GAP | terminalize scoped causal boundary

## OPEN_GAPS_V1
AXS-008 | AXS | GAP | CAUSALITY | No scoped evidence identifies a general causal path from ownership/financing to editorial intervention or democratic outcome; INV-082 is the proper downstream object.
CLM-005 | CLM | PARTIAL | METHOD | Underlying title/group mapping, date cut and denominator calculation are not exposed in the reviewed record.
CAU-001 | CAU | UNRESOLVED | CAUSALITY | The scoped evidence establishes legal ownership/control structures but does not identify a general causal effect on editorial choices.
CAU-002 | CAU | UNRESOLVED | CAUSALITY | No reviewed evidence isolates control rights, editorial intervention or causal effect from the financing relation alone.

SEMANTIC_COUNTS_V1:LED:2|CLM:8|AXS:8|CAU:2|CTRL:3|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009"],"evidence_excerpt":"sans reprendre 9 milliardaires/80-90 % sans dénominateur","kind":"HYPOTHESIS","lead":"The recurring 80-90% / 9-billionaires formulation may collapse multiple dates, media universes and metrics into a denominator-free all-media claim.","linked_ids":["AXS-001","AXS-002","AXS-004","CLM-001","CLM-002","CLM-005"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008"],"routes":["OBJECT_INVESTIGATION","SCOPE_HISTORY","RULES_CONTROLS"],"source_id":"INV-081_RUN_CARD","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"evidence_excerpt":"ne pas confondre propriété, audience et contrôle éditorial","kind":"METHOD_CONSTRAINT","lead":"Legal ownership/control, financing, audience/circulation and editorial influence must be measured separately; ownership alone cannot establish editorial control or effect.","linked_ids":["AXS-003","AXS-005","AXS-006","AXS-007","AXS-008","CLM-003","CLM-004","CLM-006","CLM-007","CLM-008","CAU-001","CAU-002"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016"],"routes":["MECHANISMS","COUNTER_HYPOTHESES","RULES_CONTROLS"],"source_id":"INV-081_RUN_CARD","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"The denominator-free formulation that 80-90% of French media are owned by a small number of billionaires is not a reproducible universal statistic in the reviewed evidence: the documented figures refer to different sectors, dates and metrics.","claimant":"INV-081 synthesis","counter":"FCT-014(concentration risk remains high)","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-011","FCT-012"]}
CLM-002 | {"claim":"The traceable 91.4% figure is specifically a 2021 claim about circulation of national general-interest daily newspapers, not all French media.","claimant":"INV-081 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001"]}
CLM-003 | {"claim":"The current 2026 ownership map materially differs from older billionaire-owner maps: Groupe Le Monde reports a fund/independence-pole capital structure with Xavier Niel retaining one share, while Le Figaro and Groupe Les Echos-Le Parisien remain linked to Dassault Medias and LVMH respectively.","claimant":"INV-081 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-007","FCT-008","FCT-009"]}
CLM-004 | {"claim":"Media concentration remains a real structural pluralism issue even after rejecting slogan arithmetic: MPM2026 reports high market-plurality risk and CMA Media continued cross-media consolidation in 2025.","claimant":"INV-081 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-013","FCT-014"]}
CLM-005 | {"claim":"The 2026 parliamentary figures of 93% of national dailies, about 60% of television audience and 50% of radio audience are public claims but were not independently reproduced from a disclosed calculation in the reviewed public record.","claimant":"INV-081 synthesis","counter":"FCT-002(different 2022 actor counts and percentages)","gap":"Underlying title/group mapping, date cut and denominator calculation are not exposed in the reviewed record.","gap_type":"METHOD","materiality":"IMPORTANT","status":"PARTIAL","support":["FCT-003"]}
CLM-006 | {"claim":"Broader print denominators materially change the object: ACPM treats national and regional dailies separately, and Ouest-France alone has 581,505 paid copies in the 2025 PQR ranking under an associative ownership structure.","claimant":"INV-081 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-004","FCT-005","FCT-006","FCT-010"]}
CLM-007 | {"claim":"Legal ownership/control, financing, audience/circulation and editorial influence are distinct evidentiary objects and cannot be substituted for one another; Liberation provides a concrete ownership-versus-financing example.","claimant":"INV-081 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-015","FCT-016"]}
CLM-008 | {"claim":"A current unified official cross-media ownership concentration share cannot be computed from the present Arcom transparency database because its prefiguration does not yet cover print and online media; current French anti-concentration law itself uses sector-specific criteria.","claimant":"INV-081 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-011","FCT-012"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003"],"axis":"SLOGAN_PROVENANCE","links":["CLM-001","CLM-002","CLM-005"],"question":"What exact universe/date/metric supports recurring 80-90% or 9/11-billionaires claims?","result_ids":["FCT-001","FCT-002","FCT-003"],"sought_objects":["original 91.4% formulation","2022 parliamentary formulation","2026 parliamentary formulation"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-004","QRY-005"],"axis":"PRINT_DENOMINATORS","links":["CLM-002","CLM-006","CTRL-002"],"question":"What do current certified circulation data show for national and regional daily press when the denominator is explicit?","result_ids":["FCT-004","FCT-005","FCT-006"],"sought_objects":["ACPM PQN 2025","ACPM PQR 2025"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-006","QRY-007","QRY-008","QRY-009"],"axis":"CURRENT_LEGAL_OWNERSHIP","links":["CLM-003","CLM-006","CTRL-001"],"question":"What is the current 2026 legal ownership/control of key high-circulation news groups and titles?","result_ids":["FCT-007","FCT-008","FCT-009","FCT-010"],"sought_objects":["Groupe Le Monde","Dassault Médias/Le Figaro","LVMH/Groupe Les Echos-Le Parisien","Ouest-France"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-010","QRY-011"],"axis":"REGULATORY_DENOMINATORS","links":["CLM-001","CLM-008","CTRL-003"],"question":"Does French regulation use one unified all-media concentration measure or sector-specific thresholds?","result_ids":["FCT-011","FCT-012"],"sought_objects":["Arcom anti-concentration rule","current transparency database scope"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-012"],"axis":"CROSS_MEDIA_CONSOLIDATION","links":["CLM-004"],"question":"Is there current evidence of continuing cross-media consolidation independent of slogan arithmetic?","result_ids":["FCT-013"],"sought_objects":["CMA Media acquisitions","current media portfolio expansion"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-013"],"axis":"PLURALISM_RISK","links":["CLM-004","CTRL-003"],"question":"What independent current evidence assesses market plurality risk without presenting it as an ownership share?","result_ids":["FCT-014"],"sought_objects":["European Commission Rule of Law 2026","MPM2026 France risk indicator"],"status":"SATURATED"}
AXS-007 | {"attempt_ids":["QRY-014","QRY-015"],"axis":"OWNERSHIP_VS_FINANCING","links":["CLM-007","CAU-002"],"question":"Can legal ownership be separated from billionaire financing/dependency in concrete cases?","result_ids":["FCT-015","FCT-016"],"sought_objects":["Libération transfer/control","2026 external financing"],"status":"SATURATED"}
AXS-008 | {"attempt_ids":["QRY-006","QRY-008","QRY-014"],"axis":"CAUSAL_BOUNDARY","gap":"No scoped evidence identifies a general causal path from ownership/financing to editorial intervention or democratic outcome; INV-082 is the proper downstream object.","gap_type":"CAUSALITY","links":["CLM-007","CAU-001","CAU-002"],"question":"What can ownership concentration establish about editorial control, persuasion or democratic effects?","result_ids":["FCT-007","FCT-008","FCT-015","FCT-016"],"sought_objects":["documented governance/control rights","intervention traces","identified causal evidence"],"status":"GAP"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"NONE_FOUND","gap":"The scoped evidence establishes legal ownership/control structures but does not identify a general causal effect on editorial choices.","gap_type":"CAUSALITY","limit":"Ownership is capability/governance context, not evidence of specific editorial tasking or effect; this belongs to INV-082.","mechanism":"Ownership concentration -> editorial concentration or intervention","status":"UNRESOLVED","support":["FCT-007","FCT-008","FCT-009","FCT-010"]}
CAU-002 | {"counter":"NONE_FOUND","gap":"No reviewed evidence isolates control rights, editorial intervention or causal effect from the financing relation alone.","gap_type":"CAUSALITY","limit":"Debt/financing can create dependency but is not equivalent to legal ownership, tasking or demonstrated editorial control.","mechanism":"External billionaire financing -> editorial control","status":"UNRESOLVED","support":["FCT-015","FCT-016"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Current legal-ownership control: the 2026 Groupe Le Monde capital structure falsifies a stale simplification that Xavier Niel currently owns Le Monde in the same sense as before the transfer to the independence fund.","status":"SUPPORTED","support":["FCT-007"]}
CTRL-002 | {"control":"Denominator control: ACPM separates PQN and PQR, and the largest PQR title Ouest-France exceeds any single listed PQN title in paid circulation, so a narrow PQN denominator cannot stand for all French daily press.","status":"SUPPORTED","support":["FCT-004","FCT-005","FCT-006"]}
CTRL-003 | {"control":"Independent structural-risk control: the 71% MPM2026 market-plurality risk score and recent CMA Media acquisitions support a real concentration concern while remaining numerically incommensurable with an ownership market share.","status":"SUPPORTED","support":["FCT-013","FCT-014"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:15|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"EMPTY","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"EMPTY","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | subject-fp lookup | MNEMO_Q
SYS-003 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-004 | SYS | OK | web | INV-081 | WEB_RESEARCH
SYS-005 | SYS | FAIL:MNEMO_UNAVAILABLE | mnemo | INV-081 | MNEMO_S
SYS-006 | SYS | PARTIAL | runtime | ATTEMPT-001 | PERSIST_REBIND
SYS-007 | SYS | PASS | runtime | ATTEMPT-002 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.politis.fr/articles/2021/12/menace-sur-le-pluralisme-une-concentration-dans-les-medias-toujours-plus-forte-43905/ | trace original 91.4 percent national generalist daily circulation claim
QRY-002 | FETCH | FOUND | SRC-002 | https://questions.assemblee-nationale.fr/dyn/docs/CRCANR5L17S2026PO419604N039.raw | trace 2022 parliamentary 11 billionaires 80% national dailies claim
QRY-003 | FETCH | FOUND | SRC-003 | https://questions.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2025-2026/deuxieme-seance-du-jeudi-12-fevrier-2026 | trace 2026 parliamentary 5 billionaires 93% national dailies claim
QRY-004 | FETCH | FOUND | SRC-004 | https://www.acpm.fr/classements/pqn?thematic=5 | ACPM 2025 paid circulation national daily press
QRY-005 | FETCH | FOUND | SRC-005 | https://www.acpm.fr/classements/pqr | ACPM 2025 paid circulation regional daily press
QRY-006 | FETCH | FOUND | SRC-006 | https://www.lemonde.fr/actualite-medias/article/2026/06/10/l-actionnariat-du-groupe-le-monde-en-2026_6700443_3236.html | current 2026 Groupe Le Monde ownership structure
QRY-007 | FETCH | FOUND | SRC-007 | https://mentions-legales.lefigaro.fr/le-figaro/mentions-legales-figaro | current Le Figaro legal ownership shareholder over 95 percent
QRY-008 | FETCH | FOUND | SRC-008 | https://www.lvmh.com/join-us/our-maisons/other-activities/groupe-les-echos-le-parisien | current LVMH Groupe Les Echos Le Parisien media subsidiary portfolio
QRY-009 | FETCH | FOUND | SRC-009 | https://www.ouest-france.fr/qui-sommes-nous/ | current Ouest-France ownership association non-profit ASPDH
QRY-010 | FETCH | FOUND | SRC-010 | https://www.arcom.fr/nous-connaitre/nos-missions/garantir-le-pluralisme-et-la-cohesion-sociale/le-dispositif-anti-concentration-un-outil-visant-garantir-le-pluralisme | Arcom national anti-concentration thresholds printed daily press
QRY-011 | FETCH | FOUND | SRC-011 | https://www.arcom.fr/nous-connaitre-notre-institution/regulation-europeenne-et-internationale/base-de-donnees-sur-la-transparence-des-medias | Arcom media ownership transparency database current scope print online absent
QRY-012 | FETCH | FOUND | SRC-012 | https://www.cmacgm-group.com/fr/actualites-media/resultats-financiers-annuels-2025 | CMA Media acquisitions 2025 Brut Cherie 25 cross-media portfolio
QRY-013 | FETCH | FOUND | SRC-013 | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52026SC0910 | EU Commission 2026 France media market plurality risk MPM 71 percent
QRY-014 | FETCH | FOUND | SRC-014 | https://www.lemonde.fr/economie/article/2022/02/14/patrick-drahi-vole-au-secours-de-liberation_6113628_3234.html | Libération legal control transfer from Altice to FDPI / Presse Independante
QRY-015 | FETCH | FOUND | SRC-015 | https://www.strategies.fr/actualites/medias/LQ5508814C/liberation-daniel-kretinsky-apporte-17-millions-deuros-supplementaires.html | Libération 2026 external financing loan Kretinsky 17 million

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:other:politis | POLITIS-CONCENTRATION-2021 | Menace sur le pluralisme : une concentration dans les médias toujours plus forte | 2021-12-15 | 2026-09-06T14:01:33Z | explicit 91.4% formulation and denominator | https://www.politis.fr/articles/2021/12/menace-sur-le-pluralisme-une-concentration-dans-les-medias-toujours-plus-forte-43905/
SRC-002 | ◈ | fam:other:assemblee_nationale | AN-COMMISSION-MEDIA-CONCENTRATION-2026-039 | Commission des affaires culturelles et de l education - audition concentration des medias | 2026 | 2026-09-06T14:01:33Z | speaker cites 2022 figures: 11 billionaires/80% dailies/95% weeklies/47% radio/57% TV | https://questions.assemblee-nationale.fr/dyn/docs/CRCANR5L17S2026PO419604N039.raw
SRC-003 | ◈ | fam:other:assemblee_nationale | AN-SEANCE-2026-02-12 | Deuxieme seance du jeudi 12 fevrier 2026 | 2026-02-12 | 2026-09-06T14:01:33Z | speaker claim: 5 billionaires/93% national dailies; TV/radio audience claims | https://questions.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2025-2026/deuxieme-seance-du-jeudi-12-fevrier-2026
SRC-004 | ◈ | fam:other:acpm | ACPM-PQN-2025 | Presse Quotidienne Nationale - Classement 2025 | 2025 | 2026-09-06T14:01:33Z | 11 supports; diffusion France payee par titre | https://www.acpm.fr/classements/pqn?thematic=5
SRC-005 | ◈ | fam:other:acpm | ACPM-PQR-2025 | Presse Quotidienne Regionale - Classement 2025 | 2025 | 2026-09-06T14:01:33Z | 63 supports; diffusion France payee par titre | https://www.acpm.fr/classements/pqr
SRC-006 | ◈ | fam:other:groupe_lemonde | GROUPE-LEMONDE-OWNERSHIP-2026 | L actionnariat du Groupe Le Monde en 2026 | 2026-06-10 | 2026-09-06T14:01:33Z | 72.5% via Fonds pour independance de la presse; 25.4% pole independance; Niel one share | https://www.lemonde.fr/actualite-medias/article/2026/06/10/l-actionnariat-du-groupe-le-monde-en-2026_6700443_3236.html
SRC-007 | ◈ | fam:other:lefigaro_legal | LEFIGARO-LEGAL-2026 | Mentions legales Le Figaro | 2026 | 2026-09-06T14:01:33Z | Societe du Figaro; shareholder >95% Dassault Medias | https://mentions-legales.lefigaro.fr/le-figaro/mentions-legales-figaro
SRC-008 | ◈ | fam:other:lvmh | LVMH-GLELP-2026 | Groupe Les Echos-Le Parisien - LVMH | 2026 | 2026-09-06T14:01:33Z | LVMH media subsidiary; Les Echos, Le Parisien-Aujourd hui en France and other media | https://www.lvmh.com/join-us/our-maisons/other-activities/groupe-les-echos-le-parisien
SRC-009 | ◈ | fam:other:ouest_france | OUESTFRANCE-OWNERSHIP-2026 | Qui sommes-nous - Ouest-France | 2026 | 2026-09-06T14:01:33Z | SA Ouest-France depends since 1990 on non-profit ASPDH | https://www.ouest-france.fr/qui-sommes-nous/
SRC-010 | ◈ | fam:other:arcom | ARCOM-ANTI-CONCENTRATION-2026 | Le dispositif anti-concentration : un outil visant a garantir le pluralisme | 2026 | 2026-09-06T14:01:33Z | national multimedia rule uses sector-specific TV/radio/printed daily thresholds; print threshold >20% category diffusion | https://www.arcom.fr/nous-connaitre/nos-missions/garantir-le-pluralisme-et-la-cohesion-sociale/le-dispositif-anti-concentration-un-outil-visant-garantir-le-pluralisme
SRC-011 | ◈ | fam:other:arcom | ARCOM-TRANSPARENCY-DB-2026 | Base de donnees sur la transparence des medias | 2026 | 2026-09-06T14:01:33Z | prefiguration EMFA; current scope terrestrial TV/radio; print/online to be extended | https://www.arcom.fr/nous-connaitre-notre-institution/regulation-europeenne-et-internationale/base-de-donnees-sur-la-transparence-des-medias
SRC-012 | ◈ | fam:other:cma_cgm | CMA-CGM-RESULTS-2025 | Resultats financiers annuels 2025 - CMA CGM | 2026 | 2026-09-06T14:01:33Z | Brut acquisition finalized Sep 2025; Cherie 25 Oct 2025; CMA Media cross-media expansion | https://www.cmacgm-group.com/fr/actualites-media/resultats-financiers-annuels-2025
SRC-013 | ◈ | fam:other:eu_commission | EU-ROL-FRANCE-2026 | 2026 Rule of Law Report - France country chapter | 2026 | 2026-09-06T14:01:33Z | media pluralism section; current audiovisual-only ownership database; MPM2026 market plurality risk 71% | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52026SC0910
SRC-014 | ◈ | fam:other:lemonde_press | LEMONDE-LIBERATION-2022 | Patrick Drahi vole au secours de Liberation | 2022-02-14 | 2026-09-06T14:01:33Z | reports Libération no longer owned by Altice; FDPI structure | https://www.lemonde.fr/economie/article/2022/02/14/patrick-drahi-vole-au-secours-de-liberation_6113628_3234.html
SRC-015 | ◈ | fam:other:strategies | STRATEGIES-LIBERATION-2026 | Liberation : Daniel Kretinsky apporte 17 millions d euros supplementaires | 2026-03-09 | 2026-09-06T14:01:33Z | new 17m euro loan; fourth since 2022 | https://www.strategies.fr/actualites/medias/LQ5508814C/liberation-daniel-kretinsky-apporte-17-millions-deuros-supplementaires.html

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.politis.fr/articles/2021/12/menace-sur-le-pluralisme-une-concentration-dans-les-medias-toujours-plus-forte-43905/ | other:politis | 2021-12-15 | Original 91.4 percent formulation | Politis states that 91.4% of the circulation of national general-interest daily newspapers in France belonged to six billionaires; the stated universe is national generalist dailies and the metric is circulation, not all French media. | -
FCT-002 | FACT | ✧ | https://questions.assemblee-nationale.fr/dyn/docs/CRCANR5L17S2026PO419604N039.raw | other:assemblee_nationale | 2026 | Parliamentary citation of 2022 concentration figures | A 2026 National Assembly committee record cites 2022 figures: eleven billionaires held 80% of national dailies and 95% of generalist weeklies, with 47% of radio audience and 57% of television audience; these are speaker-cited figures and not independently reproduced by this run. | -
FCT-003 | FACT | ✧ | https://questions.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2025-2026/deuxieme-seance-du-jeudi-12-fevrier-2026 | other:assemblee_nationale | 2026-02-12 | Parliamentary 2026 concentration claims | A National Assembly speaker stated that five billionaires own 93% of national dailies, four hold about 60% of television audience, and four 50% of radio audience; the public record reviewed does not expose a common denominator or reproducible calculation for these percentages. | -
FCT-004 | FACT | ✧ | https://www.acpm.fr/classements/pqn?thematic=5 | other:acpm | 2025 | ACPM national daily paid circulation universe | ACPM 2025 lists 11 supports in its national daily press paid-circulation ranking, including Le Monde 559,250; Le Figaro 386,769; L Equipe 237,817; Les Echos 141,021; Liberation 117,465; La Croix 75,902; L Humanite 39,807; and the Le Parisien + Aujourd hui en France coupling 260,849. | -
FCT-005 | FACT | ✧ | https://www.acpm.fr/classements/pqr | other:acpm | 2025 | ACPM regional daily paid circulation universe | ACPM 2025 lists 63 regional daily press supports; Ouest-France is first at 581,505 paid copies, followed by Le Parisien 192,505 and Sud Ouest 164,510 among the leading titles. | -
FCT-006 | FACT | ✧ | https://www.acpm.fr/classements/pqr | other:acpm | 2025 | National daily and regional daily are distinct measurable universes | ACPM publishes national daily press and regional daily press as separate certified ranking universes; a percentage calculated on PQN does not by itself describe the broader French daily press universe. | -
FCT-007 | FACT | ✧ | https://www.lemonde.fr/actualite-medias/article/2026/06/10/l-actionnariat-du-groupe-le-monde-en-2026_6700443_3236.html | other:groupe_lemonde | 2026-06-10 | Groupe Le Monde ownership 2026 | Groupe Le Monde reports that 72.5% is held via Le Monde Libre by the Fonds pour l independance de la presse and 25.4% by the Pole d independance; Xavier Niel retains one share after transfer of his balance to the fund. | -
FCT-008 | FACT | ✧ | https://mentions-legales.lefigaro.fr/le-figaro/mentions-legales-figaro | other:lefigaro_legal | 2026 | Le Figaro legal ownership 2026 | Le Figaro legal notices identify Societe du Figaro and state that Dassault Medias is a shareholder above 95%. | -
FCT-009 | FACT | ✧ | https://www.lvmh.com/join-us/our-maisons/other-activities/groupe-les-echos-le-parisien | other:lvmh | 2026 | LVMH media subsidiary portfolio | LVMH presents Groupe Les Echos-Le Parisien as its media subsidiary and lists Les Echos and Le Parisien-Aujourd hui en France among its media assets. | -
FCT-010 | FACT | ✧ | https://www.ouest-france.fr/qui-sommes-nous/ | other:ouest_france | 2026 | Ouest-France ownership structure | Ouest-France states that since 1990 SA Ouest-France depends on the non-profit Association pour le soutien des principes de la democratie humaniste (ASPDH), providing a large-circulation ownership model outside the common billionaire-owner category. | -
FCT-011 | FACT | ✧ | https://www.arcom.fr/nous-connaitre/nos-missions/garantir-le-pluralisme-et-la-cohesion-sociale/le-dispositif-anti-concentration-un-outil-visant-garantir-le-pluralisme | other:arcom | 2026 | French anti-concentration rule uses sector-specific thresholds | Arcom describes the national multimedia anti-concentration rule through separate television, radio and printed national daily criteria; for printed national daily IPG press the criterion is control above 20% of total diffusion in that category over the previous twelve months. | -
FCT-012 | FACT | ✧ | https://www.arcom.fr/nous-connaitre-notre-institution/regulation-europeenne-et-internationale/base-de-donnees-sur-la-transparence-des-medias | other:arcom | 2026 | Arcom media transparency database current scope | Arcom states that the current prefiguration of its media-transparency database covers terrestrial television and radio and must be extended to other media, including print and online, to meet the European Media Freedom Act information scope. | -
FCT-013 | FACT | ✧ | https://www.cmacgm-group.com/fr/actualites-media/resultats-financiers-annuels-2025 | other:cma_cgm | 2026 | CMA Media cross-media consolidation 2025-2026 | CMA CGM reports completion of the Brut acquisition in September 2025 and Cherie 25 in October 2025; CMA Media spans regional/national press, television, radio and digital/social media. | -
FCT-014 | FACT | ✧ | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52026SC0910 | other:eu_commission | 2026 | France market plurality risk indicator | The European Commission 2026 France Rule of Law chapter, citing MPM2026, reports a 71% risk score for market plurality in France and notes concerns about concentration; 71% is a risk indicator, not a media-ownership market share. | -
FCT-015 | FACT | ✧ | https://www.lemonde.fr/economie/article/2022/02/14/patrick-drahi-vole-au-secours-de-liberation_6113628_3234.html | other:lemonde_press | 2022-02-14 | Liberation legal ownership separated from Altice | Le Monde reported that Liberation was no longer owned by Altice and was housed in the Presse Independante/FDPI structure; this distinguishes legal ownership from later external financing. | -
FCT-016 | FACT | ✧ | https://www.strategies.fr/actualites/medias/LQ5508814C/liberation-daniel-kretinsky-apporte-17-millions-deuros-supplementaires.html | other:strategies | 2026-03-09 | Liberation external financing 2026 | Strategies reported a new 17 million euro loan from Daniel Kretinsky to Liberation in March 2026, described as the fourth such loan since 2022; a loan is a financing relation and is not by itself proof of legal ownership or editorial tasking. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-003
FCT-004 | SRC-004
FCT-005 | SRC-005
FCT-006 | SRC-004,SRC-005
FCT-007 | SRC-006
FCT-008 | SRC-007
FCT-009 | SRC-008
FCT-010 | SRC-009
FCT-011 | SRC-010
FCT-012 | SRC-011
FCT-013 | SRC-012
FCT-014 | SRC-013
FCT-015 | SRC-014
FCT-016 | SRC-015

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
CP-001 | LEADS | PASS | LAST_COMPLETED:5 LEADS | NEXT_ACTION:7 SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 SCOPE | NEXT_ACTION:9 SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 SEARCH | NEXT_ACTION:10 FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10 FACTS | NEXT_ACTION:11 CAUSAL
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 CAUSAL_GAP | NEXT_ACTION:13 VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 VERIFY | NEXT_ACTION:17 INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:18 FINALIZATION

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-06T14:08:19.073812+00:00","fact_mem":{},"mnemo_row":"BLOCKED:MNEMO_UNAVAILABLE","result":"PARTIAL","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":16,"eligible":16,"failure":0,"success":0}}
ATTEMPT-002 | {"created_at":"2026-09-06T14:09:32.455072+00:00","fact_mem":{},"mnemo_row":"BLOCKED:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":16,"eligible":16,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:BLOCKED:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:16;attempted:0;success:0;failure:0;blocked:16} | WRITEBACK_EXECUTION_V1:[16 rows, see section]

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
