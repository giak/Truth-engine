ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260908-0942-platform-visibility-friction | PARENT_RUN_ID:NONE | AS_OF:2026-09-08
INPUT_KIND:RUN_CARD | MISSION_MODE:DEEPEN | INPUT_REF:PATH:/mnt/data/inv090-runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-08_platform-visibility-friction/2026-09-08_09-42_platform-visibility-friction_INPUT.md | SUBJECT_SLUG:platform-visibility-friction | SUBJECT_FP:sha256:1659f843335bfe4f416093054fa672cd44fda1331bd98475c005ca8ac5e8b1cc | INPUT_SHA256:sha256:9ea6b962289e773301daa757d0abc35462c9e5c816fb00d045afd2f93267ded1
COMPLEXITY:8→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/UE 2018-2026; platform rule/signal or external request -> ranking/demotion/demonetization/recommendation restriction -> exposure change -> notice/appeal/correction -> downstream effect. Foreign comparators only for isomorphic visibility mechanisms.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/FRAMING.md,clusters/NETWORK.md | degraded:MNEMO_UNAVAILABLE,LOCAL_CORPUS_PATH_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-090 — Shadow banning, démonétisation, déréférencement et friction algorithmique

## Résultat central

Les restrictions de visibilité sans suppression totale sont réelles et documentées. Elles ne nécessitent pas le mot imprécis « shadow ban » pour être établies : Meta a explicitement modifié le ranking du contenu politique, Instagram/Threads ont limité les recommandations politiques de comptes non suivis, X publie des données de « restricted reach labels », TikTok distingue contenu supprimé et contenu inéligible au For You Feed, et TikTok applique aussi des restrictions catégorielles de monétisation aux comptes politiques (FCT-001, FCT-005, FCT-011, FCT-031 à FCT-035).

La frontière centrale est toutefois stricte : **baisse de portée != shadowban politique != intention partisane != tasking étatique != persuasion != effet électoral**. Le corpus établit fortement les mécanismes en amont, partiellement leurs volumes et erreurs, mais ne ferme pas généralement les arêtes d’intention ni d’effet démocratique aval.

## Les plateformes modifient réellement la visibilité politique

Meta fournit le cas le plus clair de politique explicite. Dès 2021, la plateforme teste une réduction de distribution du contenu politique ; en 2022, elle dit avoir globalement implémenté un ranking donnant moins de poids à certains signaux pour réduire la quantité de politique vue (FCT-001/FCT-002). En 2024, Instagram et Threads annoncent qu’ils ne recommanderont plus proactivement le contenu politique de comptes non suivis sur Explore, Reels, recommandations de Feed et comptes suggérés (FCT-005/FCT-006). Cela établit une friction politique réelle et intentionnelle au niveau de la catégorie de contenu.

Mais ce mécanisme n’est ni caché ni stable : Meta annonce en janvier 2025 une réintroduction plus personnalisée du contenu civique/politique (FCT-008/FCT-009). Une baisse de reach observée en 2024 ne peut donc pas être projetée mécaniquement sur 2025-2026 sans identifier l’état de politique correspondant.

## France/UE : reach restrictions et corrections sont quantifiables

Le rapport DSA de X est un contrôle opérationnel précieux. Il nomme explicitement des Restricted Reach Labels et, pour la France entre avril et septembre 2024, rapporte 39 454 labels automatisés pour Hateful Conduct ; l’addition des lignes affichées de reach restriction pour Hateful Conduct, Abuse & Harassment et Violent Speech atteint 61 550 actions dans le rapport (FCT-011 à FCT-013). Ce nombre n’est pas un dénominateur politique : il prouve l’échelle d’une technique de limitation de portée, pas une prévalence de shadowban idéologique.

Les recours montrent en parallèle que l’action initiale n’est pas une vérité finale. X rapporte 46 222 plaintes françaises contre des suspensions, dont 12 047 renversées, et 6 772 plaintes contre des actions de contenu, dont 793 renversées (FCT-016/FCT-017). À l’échelle UE, la Commission indique que près de 30 % des 165 millions de décisions contestées via les mécanismes internes ont été inversées, tandis que les organismes extrajudiciaires ont renversé 52 % des affaires clôturées étudiées au premier semestre 2025 (FCT-018/FCT-020). L’erreur et la correction sont donc des composantes matérielles du système.

## L’État n’explique pas automatiquement la modération

Le corpus ne justifie pas de convertir la régulation ou l’existence de demandes publiques en commande générale de la visibilité. Dans le rapport X étudié, la France apparaît avec cinq information requests sous « negative effects on civic discourse or elections », mais aucun ordre de retrait français dans cette catégorie ; les huit ordres de retrait français listés concernent les produits dangereux ou illégaux (FCT-014/FCT-015).

Plus largement, la Commission indique qu’au premier semestre 2025, 99 % des plus de neuf milliards de décisions de modération déclarées relevaient des propres conditions générales des plateformes plutôt que de signalements de contenu illégal (FCT-019). Cela n’exclut pas des cas de tasking public. Cela interdit seulement d’attribuer l’agrégat au pouvoir public sans chaîne décisionnelle précise.

## « Shadowban politique » : les audits imposent une forte discipline

L’audit Journal of Communication d’environ 25 000 comptes Twitter conclut que les shadowbans étaient rares. Les comptes de type bot étaient plus touchés ; les réponses politiques étaient davantage downtiered, mais à gauche comme à droite (FCT-022 à FCT-024).

Une autre expérience de grande échelle, publiée dans PNAS, montre qu’un ranking algorithmique peut produire une asymétrie politique : sur sept pays, la droite bénéficiait en moyenne d’une amplification supérieure à la gauche (FCT-025/FCT-026). C’est une différence d’exposition réelle, pas une preuve autonome d’intention partisane (FCT-027).

Le contrôle TikTok 2026 est encore plus important méthodologiquement : un écart apparemment massif dans des centaines de milliers d’observations horaires disparaît quand l’unité indépendante devient le compte. Les auteurs ne détectent alors pas de suppression de portée modérée à forte sur les trois sujets testés et attribuent le faux signal à la pseudoréplication/confusion (FCT-028 à FCT-030). Un gros volume de mesures corrélées n’est pas un gros faisceau indépendant.

## Démonétisation et curation politique

TikTok fournit un exemple de démonétisation politique réellement établie mais non clandestine : les comptes de politiciens et partis ont accès aux fonctions publicitaires automatiquement coupé et sont exclus de plusieurs outils de monétisation (FCT-031/FCT-032). Cela est une restriction économique catégorielle déclarée ; démonétisation != censure idéologique (FCT-033).

TikTok peut également rendre certains contenus électoraux inéligibles au For You Feed sans les supprimer, ce qui matérialise une restriction de recommandation (FCT-034/FCT-035). YouTube adopte une autre forme de curation en mettant en avant des sources dites autoritatives dans recherche et recommandations électorales (FCT-036/FCT-037). Dans les deux cas, la structure d’exposition est modifiée, mais l’effet électoral aval reste une question distincte.

## Plafond I0–I7

- I0 VERIFIED : plateformes, règles et types d’intervention identifiés.
- I1 VERIFIED : capacité de réduire/amplifier visibilité ou monétisation établie.
- I2 VERIFIED : interventions réelles documentées, y compris en France/UE.
- I3 VERIFIED/PARTIAL : règles et certains déclencheurs connus ; décision-level classifier/tasking souvent inaccessible.
- I4 VERIFIED case-specifically : changements d’exposition et asymétries mesurables dans plusieurs audits/rapports.
- I5 NOT_ESTABLISHED generally : motif politique/partisan non déductible de la seule asymétrie ou action.
- I6 NOT_ESTABLISHED generally : persuasion/comportement non fermés par les sources de visibilité ici.
- I7 NOT_ESTABLISHED : aucun effet causal général sur un résultat électoral n’est établi.

## Résidu matériel

Un nouvel effort ne changerait le modèle que s’il apporte un dataset France/UE à dénominateur politique comparatif reliant classification ou demande précise à l’action de reach, des logs d’appel/correction par orientation ou type de contenu, des documents de tasking public ou interne, ou un design causal reliant restriction de visibilité, exposition réelle, persuasion et vote. Des plaintes isolées de « shadowban » sans trace d’action ni dénominateur sont cumulatives, pas décisives.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:6|SRC_COMPLETE:12/12

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-08
- **notes:**
  - Meta political ranking reductions 2021-2024
  - Meta political-content approach materially changes in 2025
  - X DSA report covers Apr-Sep 2024
  - DSA appeals/reversals aggregate through H1 2025 / reported 2026
  - TikTok audit published July 2026
- **status:** CURRENT_THROUGH_2026
- **window:** 2018-2026

### MANIPULATION_REPORT
- **assumptions:**
  - lower reach proves shadowban
  - political asymmetry proves partisan intent
  - platform moderation is state command
  - appeal equals exoneration
  - exposure change implies vote change
- **clusters:**
  - **loaded:**
    - clusters/POWER.md
    - clusters/FRAMING.md
    - clusters/NETWORK.md
- **complexity:**
  - **band:** APEX
  - **score:** 8
- **implicit:**
  - electoral systems can contain both real fraud cases and non-fraud errors
  - correction mechanisms can operate without implying systemic failure
  - rumor ecosystems may exploit anomalies or impossible mechanisms
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - explicit political ranking rules
  - recommendation eligibility
  - restricted reach labels
  - appeals/reversals
  - algorithmic amplification audits
  - state-vs-platform action boundary
- **priorities:**
  - action trace
  - visibility delta
  - political comparator
  - appeal/correction
  - state/platform attribution
  - downstream effect
- **query_guidance:** prefer platform transparency, DSA/regulators and independent audits; preserve rule/action/motive/effect boundaries.
- **rhetorical:**
  - **AUTH:** authority supplies adjudicated/administrative records but remains claim-bound
  - **BF:** selected cases are not a national base rate
  - **DEM:** German comparator is procedural, not prevalence evidence
  - **FAC:** separate fraud, error, accusation, detection and effect
  - **NUM:** all counts retain their denominator and case scope
- **speaker:**
  - **goal:** forensic decomposition of platform visibility restrictions
  - **target:** rule/signal/request->action->exposure->appeal/effect chain
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **Κ:** 4
  - **Λ:** 4
  - **Ξ:** 4
  - **Σ:** 4
  - **Φ:** 5
  - **Ψ:** 3
  - **Ω:** 4
  - **κ:** 4
  - **ρ:** 5
  - **€:** 2
  - **↕:** 4
  - **⏰:** 3
  - **⚔:** 4
  - **⫸:** 4
  - **🌐:** 4
- **threats:**
  - reduced_reach=shadowban
  - moderation=political_motive
  - ranking_bias=intentional_suppression
  - complaint=proof
  - platform_action=state_tasking
  - exposure=electoral_effect

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - case-level public-request-to-visibility-action linkage
  - **input_ids:**
    - FCT-011
    - FCT-014
    - FCT-015
    - FCT-019
    - FCT-031
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no generalized state tasking chain established
  - **not_computable:**
    - undisclosed internal or public communications
  - **operations_applied:**
    - mapped platform/public authority edges
    - separated information requests from removal orders and platform-own terms
  - **reason:** separate platform rule authority, regulator/public requests and account-level enforcement
  - **result_ids:**
    - CLM-001
    - CLM-004
    - CTRL-004
  - **status:** DONE
  - **trigger:** ↕
- **item 2:**
  - **gaps:**
    - France/UE party-balanced repeated audit under known policy states
  - **input_ids:**
    - FCT-022
    - FCT-024
    - FCT-025
    - FCT-026
    - FCT-029
    - FCT-030
  - **module:** clusters/FRAMING.md
  - **negative_results:**
    - no general one-direction political suppression effect
  - **not_computable:**
    - intent without internal tasking evidence
  - **operations_applied:**
    - compared positive, mixed and null visibility audits
    - separated exposure asymmetry from motive
  - **reason:** test shadowban and political-bias claims against alternative ranking explanations and audits
  - **result_ids:**
    - CLM-002
    - CLM-003
    - CLM-006
    - CTRL-001
    - CTRL-002
    - CTRL-003
    - CAU-001
  - **status:** DONE
  - **trigger:** Φ
- **item 3:**
  - **gaps:**
    - decision-level trace from trigger to ranking action
  - **input_ids:**
    - FCT-005
    - FCT-007
    - FCT-011
    - FCT-016
    - FCT-017
    - FCT-020
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no stable hidden blacklist architecture established from aggregate data
  - **not_computable:**
    - private classifier features and thresholds
  - **operations_applied:**
    - mapped enforcement and appeal interfaces
    - preserved platform policy changes over time
  - **reason:** map platform->moderator/algorithm->content/account->user exposure and appeal loops
  - **result_ids:**
    - CLM-001
    - CLM-005
    - CTRL-005
  - **status:** DONE
  - **trigger:** 🌐

### SCOPING_REPORT
- **actors_institutions:**
  - Meta
  - X
  - TikTok
  - YouTube
  - European Commission
  - research teams
  - public authorities
- **domains:**
  - content moderation
  - recommendation/ranking
  - demonetization
  - political communication
  - DSA appeals
  - algorithmic auditing
- **evidence_limits:**
  - no exhaustive France political-only restriction denominator
  - platform rules change over time
  - most audits cannot observe internal motive/tasking
  - no person-level visibility-to-vote causal design
- **exclusions:**
  - reduced reach=shadowban
  - moderation=political motive
  - demonetization=censorship
  - ranking change=targeted suppression
  - complaint=proof
  - platform action=state tasking
  - exposure change=electoral effect
- **geo:** France/UE; foreign isomorphic comparators
- **lead_question:** Shadow banning, démonétisation, déréférencement et friction algorithmique
- **object_coverage:** STRONG_FOR_EXISTENCE_AND_RECOURSE; MODERATE_FOR_POLITICAL_DIFFERENTIAL; WEAK_FOR_MOTIVE_AND_ELECTORAL_EFFECT
- **object_question:** Quand une baisse de visibilité politique peut-elle être attribuée à une action de plateforme identifiable plutôt qu’à un changement de ranking, une règle générale, le comportement du compte ou un artefact de mesure?
- **period:** 2018-2026

### CREDO
- reduced_reach != shadowban
- moderation != political_motive
- demonetization != censorship
- ranking_change != targeted_suppression
- complaint != proof
- detected_case != prevalence
- platform_action != state_tasking
- exposure_change != persuasion
- exposure_change != electoral_effect

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - explicit rank reduction
  - recommendation ineligibility
  - restricted reach
  - monetization restriction
  - appeal reversal
  - algorithmic exposure audit
- **priorities:**
  - rule/signal
  - action
  - target
  - exposure delta
  - notice/appeal
  - motive
  - downstream effect
- **query_guidance:** prefer direct platform/DSA records plus independent audits; require temporal policy state and unit-of-analysis discipline.
- **speaker:**
  - **goal:** forensic visibility attribution
  - **target:** platform action->exposure->effect chain
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **threats:**
  - complaint laundering
  - policy temporal drift
  - pseudoreplication
  - state/platform conflation
  - exposure/effect conflation

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** Meta, X and TikTok publicly document reach/recommendation restrictions that can lower visibility without deletion.
  - **resolution:** Visibility restriction exists; label each mechanism precisely instead of making the term shadowban do all causal work.
  - **thesis:** Le shadow banning politique est imaginaire parce que les plateformes nient le terme.
- **item 2:**
  - **antithesis:** Independent audits show rare shadowbans, cross-ideological downtiering, right amplification on Twitter and a TikTok null after correcting pseudoreplication.
  - **resolution:** Require comparable denominators and action traces; political asymmetry is evidence of exposure difference, not motive by itself.
  - **thesis:** Une baisse de portée politique prouve un ciblage partisan.
- **item 3:**
  - **antithesis:** DSA aggregate data report 99% of H1-2025 moderation decisions under platforms own terms; X France shows requests but not corresponding election-category removal orders in the sampled report.
  - **resolution:** State tasking must be proven decision by decision; aggregate moderation cannot be attributed to government.
  - **thesis:** Les autorités publiques pilotent l’essentiel de la modération UE.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **boundary:** ranking action != political motive
  - **from:** platform rule/signal
  - **support:**
    - FCT-001
    - FCT-005
    - FCT-011
    - FCT-034
  - **to:** restricted or amplified exposure
  - **vehicle:** ranking/recommendation/moderation system
- **item 2:**
  - **boundary:** request != action; order category must match
  - **from:** public request/order
  - **support:**
    - FCT-014
    - FCT-015
  - **to:** potential platform action
  - **vehicle:** legal/moderation intake
- **item 3:**
  - **boundary:** initial decision != final adjudication
  - **from:** restriction decision
  - **support:**
    - FCT-016
    - FCT-017
    - FCT-018
    - FCT-020
  - **to:** upheld or reversed action
  - **vehicle:** appeal/review
- **item 4:**
  - **boundary:** exposure change != persuasion/electoral effect
  - **from:** exposure delta
  - **support:**
    - FCT-025
    - FCT-026
    - FCT-036
  - **to:** behavior/vote
  - **vehicle:** attention/persuasion pathway

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** platform policy/product teams
  - **limits:**
    - policy rule != ideological targeting
  - **relation:** define ranking/recommendation/monetization rules
  - **support:**
    - FCT-001
    - FCT-005
    - FCT-008
    - FCT-031
    - FCT-034
  - **to:** content/accounts
- **item 2:**
  - **from:** automated/human moderation
  - **limits:**
    - aggregate action != political prevalence
  - **relation:** apply restricted reach or account/content actions
  - **support:**
    - FCT-011
    - FCT-012
    - FCT-013
  - **to:** users/content
- **item 3:**
  - **from:** public authorities
  - **limits:**
    - request != action; information request != removal order
  - **relation:** information requests / legal orders
  - **support:**
    - FCT-014
    - FCT-015
  - **to:** platforms
- **item 4:**
  - **from:** users/settlement bodies
  - **limits:**
    - reversal proves error/correction, not political motive
  - **relation:** appeal/review/correction
  - **support:**
    - FCT-016
    - FCT-017
    - FCT-018
    - FCT-020
  - **to:** platform decisions
- **item 5:**
  - **from:** ranking algorithms
  - **limits:**
    - exposure asymmetry != persuasion or vote effect
  - **relation:** amplify/reduce visibility
  - **support:**
    - FCT-025
    - FCT-026
    - FCT-036
  - **to:** political exposure

### IMPACT_MAP
- **France_EU_scale:** VERIFIED/PARTIAL
- **appeal_error_correction:** VERIFIED MATERIAL
- **demonetization_by_rule:** VERIFIED case-specific
- **electoral_effect:** NOT_ESTABLISHED
- **exposure_change:** VERIFIED case-specific
- **persuasion:** NOT_ESTABLISHED by this run
- **political_direction:** MIXED/PLATFORM-SPECIFIC
- **state_tasking:** NOT_ESTABLISHED generally
- **support:**
  - FCT-011
  - FCT-013
  - FCT-018
  - FCT-020
  - FCT-025
  - FCT-029
  - FCT-031
  - FCT-034
- **visibility_restriction_mechanisms:** VERIFIED

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** term shadowban often used for any reach decline; JOC audit finds formal shadowbans rare
  - **issue:** existence of shadow-style visibility restrictions
  - **pro:** Meta/X/TikTok explicitly document ranking, recommendation or restricted-reach interventions
  - **resolution:** MECHANISM VERIFIED; generic allegation not verified
  - **support:**
    - FCT-001
    - FCT-011
    - FCT-022
    - FCT-034
    - FCT-035
- **item 2:**
  - **contra:** JOC effect spans left and right; TikTok 2026 account-level audit finds no moderate-large suppression
  - **issue:** partisan direction
  - **pro:** PNAS finds higher right amplification on Twitter; JOC sees political replies more often downtiered
  - **resolution:** POLITICAL_DIFFERENTIAL MIXED/PLATFORM-DESIGN-SPECIFIC
  - **support:**
    - FCT-024
    - FCT-025
    - FCT-026
    - FCT-029
    - FCT-030
- **item 3:**
  - **contra:** 99% of reported H1-2025 moderation decisions were under platform T&C; X France election-category entries were information requests not removal orders
  - **issue:** moderation authority
  - **pro:** public authorities can send requests/orders and DSA regulates platform behavior
  - **resolution:** GENERAL STATE TASKING NOT_ESTABLISHED
  - **support:**
    - FCT-014
    - FCT-015
    - FCT-019

### VERIFICATION_REPORT
- **circular_families:**
  - Meta pages one platform family; TikTok policy pages one platform family; platform self-reports kept separate from independent academic/DSA evidence
- **contradiction_ids:**
  - visibility-exists-vs-shadowban-term
  - partisan-direction-mixed
  - state-vs-platform-authority
  - appeal-error-material
- **downgraded_ids:**
  - NONE
- **none_found_claims:**
  - general covert partisan shadowban architecture France/UE
  - general government tasking of reach restrictions
  - stable one-direction ideological suppression
  - general electoral effect from exposure restriction
- **remaining_gaps:**
  - political-only France restriction denominator
  - decision-level trigger->action logs
  - party-balanced longitudinal audits under stable policy
  - visibility-to-vote causal design
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
  - FCT-031
  - FCT-032
  - FCT-033
  - FCT-034
  - FCT-035
  - FCT-036
  - FCT-037
  - FCT-038
  - FCT-039
  - FCT-040
- **sources_reopened:** 12
- **upgraded_ids:**
  - NONE
- **verdict:** READY_FOR_PRE_GATE

### EDI_REPORT
- **corpus:**
  - **circularity:** Meta and TikTok self-statements grouped by platform family; independent audits used for bias/effect tests
  - **coverage:** STRONG_FOR_MECHANISM_EXISTENCE_AND_APPEALS; MODERATE_FOR_POLITICAL_DIFFERENTIAL; WEAK_FOR_MOTIVE_AND_ELECTORAL_EFFECT
  - **independence:** PLATFORMS+EU_REGULATOR+ACADEMIC_AUDITS
  - **limits:**
    - no exhaustive France political-only restriction denominator
    - platform policies change over time
    - internal classifier/tasking evidence absent
    - no visibility-to-vote causal design
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **gap_type:** NONE
    - **independent_families:** 4
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** REFUTATION_CONTROLS
    - **gap_type:** ATTRIBUTION
    - **independent_families:** 4
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** TEMPORAL_POLICY_CHANGE
    - **gap_type:** TEMPORAL
    - **independent_families:** 1
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** AGGREGATE_BOUNDARY
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 2
  - **item 5:**
    - **claim_id:** CLM-005
    - **direct_object:** APPEAL_REVERSALS
    - **gap_type:** EVIDENCE
    - **independent_families:** 2
  - **item 6:**
    - **claim_id:** CLM-006
    - **direct_object:** EXPOSURE_ONLY
    - **gap_type:** CAUSALITY
    - **independent_families:** 4
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** 9_PROVENANCE_FAMILIES
  - **perspective:** PLATFORM+EU_REGULATOR+INDEPENDENT_AUDITS
  - **stratification:** RULE+ACTION+EXPOSURE+APPEAL+MOTIVE+EFFECT
  - **temporal:** 2018-2026 with explicit policy-state changes
- **edi:**
  - **assessment:** STRONG_MECHANISM_DISCRIMINATION; MOTIVE_AND_DOWNSTREAM_EFFECT_UNRESOLVED
  - **flags:**
    - REAL_VISIBILITY_RESTRICTIONS
    - MATERIAL_APPEAL_REVERSALS
    - MIXED_POLITICAL_DIFFERENTIAL
    - TEMPORAL_POLICY_DRIFT
    - STATE_TASKING_NOT_GENERALIZED
- **source_counts:**
  - **primary:** 7
  - **provenance_families:** 9
  - **secondary:** 5
  - **tertiary:** 0
  - **total:** 12

### RESPONSIBILITY_MAP
- **boundary:** Visibility control is an influence/distribution mechanism; censorship, political motive, state tasking and electoral effect require separate evidence.
- **not_established:**
  - general covert partisan shadowban architecture in France/UE
  - general government command of platform reach restrictions
  - stable one-direction ideological suppression across platforms/time
  - general persuasion or electoral-result effect from visibility changes
- **verified:**
  - platforms can intentionally alter visibility via ranking/recommendation/reach restrictions
  - TikTok categorically restricts monetization/advertising for political accounts
  - appeal systems reverse substantial numbers of moderation decisions
  - public authorities can submit requests/orders
  - algorithmic ranking can produce political exposure asymmetries

### NEXT_QUERIES
- RECHECK France/UE decision-level datasets linking political content classification to demotion and pre/post reach
- RECHECK platform transparency/API data with party-balanced denominators and appeal outcomes
- RECHECK legally compelled public-request datasets that link a named request to a visibility action
- RECHECK causal designs connecting restriction-induced exposure change to persuasion/vote
- DEFER generic shadowban complaints without action trace or denominator

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-002,QRY-003 | support:- | counter:- | results:FCT-001,FCT-002,FCT-005,FCT-008,FCT-009 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-004 | support:- | counter:- | results:FCT-011,FCT-012,FCT-013,FCT-016,FCT-017 | final:SATURATED | gap:NONE
LED-003 | attempts:QRY-006,QRY-007,QRY-008 | support:- | counter:- | results:FCT-022,FCT-024,FCT-025,FCT-026,FCT-029,FCT-030 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-009,QRY-010,QRY-011 | support:- | counter:- | results:FCT-001,FCT-002,FCT-005,FCT-010,FCT-011,FCT-031,FCT-032,FCT-034,FCT-035,FCT-036 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-004,QRY-005 | support:- | counter:- | results:FCT-012,FCT-013,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-006,QRY-007,QRY-008 | support:- | counter:- | results:FCT-022,FCT-023,FCT-024,FCT-025,FCT-026,FCT-027,FCT-028,FCT-029,FCT-030 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-004,QRY-005 | support:- | counter:- | results:FCT-014,FCT-015,FCT-019 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-002,QRY-004,QRY-005 | support:- | counter:- | results:FCT-007,FCT-016,FCT-017,FCT-018,FCT-020,FCT-021 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-006,QRY-007,QRY-011,QRY-012 | support:- | counter:- | results:FCT-025,FCT-026,FCT-027,FCT-036,FCT-037,FCT-040 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,QRY-002,QRY-004,QRY-010,SRC-001,SRC-002,SRC-004,SRC-010 | support:FCT-001,FCT-005,FCT-011,FCT-034,FCT-035 | counter:- | results:FCT-001,FCT-005,FCT-011,FCT-034,FCT-035 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-006,QRY-008,QRY-012,SRC-006,SRC-008,SRC-012 | support:- | counter:FCT-022,FCT-023,FCT-024,FCT-029,FCT-030,FCT-040 | results:FCT-022,FCT-023,FCT-024,FCT-029,FCT-030,FCT-040 | final:REFUTED | gap:ATTRIBUTION
CLM-003 | attempts:QRY-001,QRY-002,QRY-003,SRC-001,SRC-002,SRC-003 | support:- | counter:FCT-001,FCT-005,FCT-008,FCT-009 | results:FCT-001,FCT-005,FCT-008,FCT-009 | final:REFUTED | gap:TEMPORAL
CLM-004 | attempts:QRY-004,QRY-005,SRC-004,SRC-005 | support:FCT-014 | counter:FCT-015,FCT-019 | results:FCT-014,FCT-015,FCT-019 | final:PARTIAL | gap:RESPONSIBILITY
CLM-005 | attempts:QRY-004,QRY-005,SRC-004,SRC-005 | support:- | counter:FCT-016,FCT-017,FCT-018,FCT-020 | results:FCT-016,FCT-017,FCT-018,FCT-020 | final:REFUTED | gap:EVIDENCE
CLM-006 | attempts:QRY-007,QRY-011,SRC-007,SRC-011 | support:- | counter:FCT-025,FCT-026,FCT-027,FCT-036,FCT-037 | results:FCT-025,FCT-026,FCT-027,FCT-036,FCT-037 | final:REFUTED | gap:CAUSALITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-002 | CLM | REFUTED | ATTRIBUTION | Need platform/action trace and comparable denominator; apparent reach gaps can be caused by policy, ranking, behavior, confounding or measurement error.
CLM-003 | CLM | REFUTED | TEMPORAL | Meta materially changed its political recommendation/ranking approach between 2021-2025.
CLM-004 | CLM | PARTIAL | RESPONSIBILITY | Specific public orders/requests exist, but aggregate DSA data show platform own terms dominate; state tasking must be proven action by action.
CLM-005 | CLM | REFUTED | EVIDENCE | Substantial appeal reversal rates show material error/correction; complaint != proof and initial action != final truth.
CLM-006 | CLM | REFUTED | CAUSALITY | Exposure shifts are real and sometimes asymmetric, but downstream persuasion/vote/outcome is not identified by these visibility studies.
CAU-001 | CAU | GAP | CAUSALITY | No current France/UE design closes a specific visibility restriction -> person-level exposure delta -> persuasion/vote -> changed electoral result chain.

SEMANTIC_COUNTS_V1:LED:3|CLM:6|AXS:6|CAU:1|CTRL:6|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003"],"evidence_excerpt":"Meta explicitly reduced political distribution/recommendation and later phased political content back in with personalization.","kind":"MECHANISM_LEAD","lead":"Meta fournit un contrôle positif fort: la visibilité politique a été explicitement modifiée par le ranking, puis la politique a été matériellement révisée. Il s’agit d’une intervention réelle mais pas nécessairement clandestine ni idéologiquement ciblée.","linked_ids":["FCT-001","FCT-002","FCT-005","FCT-008","FCT-009"],"locator":"Meta 2021-2025 political ranking policy sequence","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-005","FCT-008","FCT-009"],"routes":["VERIFY","FRAMING"],"source_id":"SRC-001","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-004"],"evidence_excerpt":"Restricted reach labels are an explicit enforcement type; French counts and appeal reversals are reported under the DSA.","kind":"MECHANISM_LEAD","lead":"Le rapport DSA de X rend observable une intervention de reach restriction à grande échelle en France et montre simultanément que des milliers de décisions sont contestées et certaines renversées.","linked_ids":["FCT-011","FCT-012","FCT-013","FCT-016","FCT-017"],"locator":"X DSA restricted reach + France appeals","materiality":"DECISIVE","result_ids":["FCT-011","FCT-012","FCT-013","FCT-016","FCT-017"],"routes":["VERIFY","POWER"],"source_id":"SRC-004","status":"SATURATED"}
LED-003 | {"attempt_ids":["QRY-006","QRY-007","QRY-008"],"evidence_excerpt":"Independent audits find rare shadowbans, cross-ideological downtiering, unequal amplification, and a TikTok null after account-level correction.","kind":"DISCRIMINATION_LEAD","lead":"Les audits indépendants interdisent de convertir une baisse de visibilité observée en preuve automatique de biais partisan: shadowbans rares dans un audit Twitter, effets politiques des deux côtés, amplification asymétrique dans une autre expérience et null TikTok après correction du design.","linked_ids":["FCT-022","FCT-024","FCT-025","FCT-026","FCT-029","FCT-030"],"locator":"independent audits mixed/null","materiality":"DECISIVE","result_ids":["FCT-022","FCT-024","FCT-025","FCT-026","FCT-029","FCT-030"],"routes":["VERIFY","CAUSALITY"],"source_id":"SRC-006","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Les plateformes appliquent réellement des restrictions de visibilité/ranking distinctes de la suppression complète.","claimant":"INV-090","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-005","FCT-011","FCT-034","FCT-035"]}
CLM-002 | {"claim":"Une baisse de portée observée suffit à prouver un shadowban politique ciblé.","claimant":"HYPOTHESIS_TEST","counter":["FCT-022","FCT-023","FCT-024","FCT-029","FCT-030","FCT-040"],"gap":"Need platform/action trace and comparable denominator; apparent reach gaps can be caused by policy, ranking, behavior, confounding or measurement error.","gap_type":"ATTRIBUTION","materiality":"DECISIVE","status":"REFUTED","support":"NONE_FOUND"}
CLM-003 | {"claim":"Les politiques de visibilité politique sont stables dans le temps et peuvent être extrapolées d’une année à l’autre.","claimant":"HYPOTHESIS_TEST","counter":["FCT-001","FCT-005","FCT-008","FCT-009"],"gap":"Meta materially changed its political recommendation/ranking approach between 2021-2025.","gap_type":"TEMPORAL","materiality":"IMPORTANT","status":"REFUTED","support":"NONE_FOUND"}
CLM-004 | {"claim":"Les restrictions de visibilité en UE sont principalement commandées par les autorités publiques.","claimant":"HYPOTHESIS_TEST","counter":["FCT-015","FCT-019"],"gap":"Specific public orders/requests exist, but aggregate DSA data show platform own terms dominate; state tasking must be proven action by action.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-014"]}
CLM-005 | {"claim":"Les décisions de modération/restriction sont suffisamment fiables pour qu’une plainte ou une décision initiale vaille preuve définitive.","claimant":"HYPOTHESIS_TEST","counter":["FCT-016","FCT-017","FCT-018","FCT-020"],"gap":"Substantial appeal reversal rates show material error/correction; complaint != proof and initial action != final truth.","gap_type":"EVIDENCE","materiality":"DECISIVE","status":"REFUTED","support":"NONE_FOUND"}
CLM-006 | {"claim":"Une modification d’exposition par ranking ou restriction établit à elle seule persuasion, changement de vote ou effet électoral.","claimant":"HYPOTHESIS_TEST","counter":["FCT-025","FCT-026","FCT-027","FCT-036","FCT-037"],"gap":"Exposure shifts are real and sometimes asymmetric, but downstream persuasion/vote/outcome is not identified by these visibility studies.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"REFUTED","support":"NONE_FOUND"}

### AXIS_REGISTRY_V1
AXS-001 | {"assessment":"VERIFIED: ranking, recommendation restriction, restricted reach and political-account monetization limits exist as distinct mechanisms.","attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-009","QRY-010","QRY-011"],"axis":"PLATFORM_RULES","links":["FCT-001","FCT-002","FCT-005","FCT-010","FCT-011","FCT-031","FCT-032","FCT-034","FCT-035","FCT-036"],"question":"Quelles restrictions de visibilité ou monétisation sont explicitement prévues par les plateformes?","result_ids":["FCT-001","FCT-002","FCT-005","FCT-010","FCT-011","FCT-031","FCT-032","FCT-034","FCT-035","FCT-036"],"sought_objects":["mechanism","evidence","effect"],"status":"SATURATED"}
AXS-002 | {"assessment":"PARTIAL but material: large moderation/reach volumes and substantial reversals are observable; no political-only denominator for all restrictions.","attempt_ids":["QRY-004","QRY-005"],"axis":"FRANCE_EU_SCALE","links":["FCT-012","FCT-013","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021"],"question":"Quelle fréquence et quels recours sont observables en France/UE?","result_ids":["FCT-012","FCT-013","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021"],"sought_objects":["mechanism","evidence","effect"],"status":"SATURATED"}
AXS-003 | {"assessment":"NOT_GENERALIZABLE: audits show rare shadowbans, both-side downtiering, right amplification on Twitter, and a TikTok null after proper unit-of-analysis correction.","attempt_ids":["QRY-006","QRY-007","QRY-008"],"axis":"POLITICAL_DIFFERENTIAL","links":["FCT-022","FCT-023","FCT-024","FCT-025","FCT-026","FCT-027","FCT-028","FCT-029","FCT-030"],"question":"Les restrictions ou classements favorisent-ils systématiquement un camp politique?","result_ids":["FCT-022","FCT-023","FCT-024","FCT-025","FCT-026","FCT-027","FCT-028","FCT-029","FCT-030"],"sought_objects":["mechanism","evidence","effect"],"status":"SATURATED"}
AXS-004 | {"assessment":"LOW/BOUNDED: 99% of reported H1-2025 EU moderation decisions were platform-T&C based; X France shows information requests about civic/elections but no removal order in that category during the report period.","attempt_ids":["QRY-004","QRY-005"],"axis":"STATE_TASKING","links":["FCT-014","FCT-015","FCT-019"],"question":"Quelle part des actions peut être reliée à une demande/ordre public plutôt qu’aux règles propres des plateformes?","result_ids":["FCT-014","FCT-015","FCT-019"],"sought_objects":["mechanism","evidence","effect"],"status":"SATURATED"}
AXS-005 | {"assessment":"VERIFIED: review/appeal mechanisms exist and non-trivial reversal rates prove error/correction is material.","attempt_ids":["QRY-002","QRY-004","QRY-005"],"axis":"APPEALS_AND_ERROR","links":["FCT-007","FCT-016","FCT-017","FCT-018","FCT-020","FCT-021"],"question":"Les décisions de restriction sont-elles fiables/finales ou souvent corrigées?","result_ids":["FCT-007","FCT-016","FCT-017","FCT-018","FCT-020","FCT-021"],"sought_objects":["mechanism","evidence","effect"],"status":"SATURATED"}
AXS-006 | {"assessment":"GAP: exposure structure is measurable, but no France/UE causal chain from a specific restriction to persuasion, vote change or election result is closed here.","attempt_ids":["QRY-006","QRY-007","QRY-011","QRY-012"],"axis":"DOWNSTREAM_EFFECT","links":["FCT-025","FCT-026","FCT-027","FCT-036","FCT-037","FCT-040"],"question":"Une variation de visibilité établit-elle persuasion ou effet électoral?","result_ids":["FCT-025","FCT-026","FCT-027","FCT-036","FCT-037","FCT-040"],"sought_objects":["mechanism","evidence","effect"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":["FCT-008","FCT-018","FCT-019","FCT-022","FCT-029","FCT-040"],"gap":"No current France/UE design closes a specific visibility restriction -> person-level exposure delta -> persuasion/vote -> changed electoral result chain.","gap_type":"CAUSALITY","limit":"Visibility interventions and exposure asymmetries are established case-specifically; political motive, prevalence by ideology and downstream electoral effects are not generally identified.","mechanism":"platform rule/signal or external request -> ranking/recommendation/demotion/demonetization action -> exposure change -> possible persuasion/behavior/electoral effect","status":"GAP","support":["FCT-001","FCT-005","FCT-011","FCT-025","FCT-034","FCT-036"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"reduced_reach != shadowban","status":"VERIFIED","support":["FCT-001","FCT-011","FCT-022"]}
CTRL-002 | {"control":"moderation != political_motive","status":"VERIFIED","support":["FCT-023","FCT-024","FCT-039","FCT-040"]}
CTRL-003 | {"control":"ranking_change != targeted_suppression","status":"VERIFIED","support":["FCT-025","FCT-026","FCT-027","FCT-029"]}
CTRL-004 | {"control":"platform_action != state_tasking","status":"VERIFIED","support":["FCT-014","FCT-015","FCT-019"]}
CTRL-005 | {"control":"complaint_or_initial_action != proof","status":"VERIFIED","support":["FCT-016","FCT-017","FCT-018","FCT-020"]}
CTRL-006 | {"control":"exposure_change != electoral_effect","status":"VERIFIED","support":["FCT-025","FCT-026","FCT-036","FCT-037"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:12|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL:MNEMO_UNAVAILABLE | mnemo | NONE | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | FAIL:LOCAL_CORPUS_PATH_UNAVAILABLE | filesystem | /home/giak/projects/truth-engine/substack-online/index.md | READ_CORPUS
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | OK | SRC-001 | https://about.fb.com/news/2021/02/reducing-political-content-in-news-feed/ | FETCH Meta political content feed ranking reductions and updates
QRY-002 | FETCH | OK | SRC-002 | https://about.fb.com/ltam/news/2024/02/actualizacion-sobre-nuestro-abordaje-al-contenido-politico-en-instagram-y-threads/ | FETCH Meta Instagram Threads political recommendation restriction 2024
QRY-003 | FETCH | OK | SRC-003 | https://about.fb.com/news/2025/01/meta-more-speech-fewer-mistakes/ | FETCH Meta January 2025 more speech political content personalized reintroduction
QRY-004 | FETCH | OK | SRC-004 | https://transparency.x.com/dsa-transparency-report.html | FETCH X DSA transparency restricted reach France appeals 2024
QRY-005 | FETCH | OK | SRC-005 | https://digital-strategy.ec.europa.eu/en/policies/dsa-impact-platforms | FETCH European Commission DSA moderation reversals shadow ban appeals 2026
QRY-006 | FETCH | OK | SRC-006 | https://academic.oup.com/joc/article-pdf/73/2/163/49678253/jqac050.pdf | FETCH Journal Communication shadowban audit Twitter 25000 accounts 2023
QRY-007 | FETCH | OK | SRC-007 | https://doi.org/10.1073/pnas.2025334119 | FETCH PNAS algorithmic amplification politics Twitter randomized experiment
QRY-008 | FETCH | OK | SRC-008 | https://arxiv.org/abs/2607.17356 | FETCH TikTok political shadowban audit 2026 differential visibility
QRY-009 | FETCH | OK | SRC-009 | https://newsroom.tiktok.com/updating-our-policies-for-political-accounts?lang=en | FETCH TikTok political accounts monetization restrictions 2022
QRY-010 | FETCH | OK | SRC-010 | https://www.tiktok.com/community-guidelines/en/integrity-authenticity/ | FETCH TikTok civic election integrity For You feed ineligibility 2024
QRY-011 | FETCH | OK | SRC-011 | https://blog.youtube/inside-youtube/us-election-misinformation-update-2023/ | FETCH YouTube authoritative election sources search recommendations 2023
QRY-012 | FETCH | OK | SRC-012 | https://link.springer.com/article/10.1140/epjds/s13688-023-00420-7 | FETCH EPJ Data Science Twitter suspension French election 2022

## EVIDENCE_REGISTRY
SRC-001 | ○ | fam:other:meta | META-POLITICAL-FEEDS | Meta — Political Content in Feeds | 2025-05-28 | 2026-09-08T09:50:00+02:00 | 2021-2025 ranking changes, global rollout, political-content controls | https://about.fb.com/news/2021/02/reducing-political-content-in-news-feed/
SRC-002 | ○ | fam:other:meta | META-IG-THREADS-POL-2024 | Meta — Political content recommendations on Instagram and Threads | 2024-02-09 | 2026-09-08T09:50:00+02:00 | no proactive political recommendations from unfollowed accounts; account-status review | https://about.fb.com/ltam/news/2024/02/actualizacion-sobre-nuestro-abordaje-al-contenido-politico-en-instagram-y-threads/
SRC-003 | ○ | fam:other:meta | META-MORE-SPEECH-2025 | Meta — More Speech and Fewer Mistakes | 2025-01-07 | 2026-09-08T09:50:00+02:00 | phase political content back into feeds; stop demoting fact-checked content in US transition | https://about.fb.com/news/2025/01/meta-more-speech-fewer-mistakes/
SRC-004 | ○ | fam:other:x | X-DSA-2024-10 | X — DSA Transparency Report October 2024 | 2024-10 | 2026-09-08T09:50:00+02:00 | restricted reach labels, French counts, requests, appeals and reversals | https://transparency.x.com/dsa-transparency-report.html
SRC-005 | ◈ | fam:A | EC-DSA-IMPACT-2026 | European Commission — Impact of the DSA on digital platforms | 2026-06-01 | 2026-09-08T09:50:00+02:00 | 9bn decisions H1 2025; 99% own T&C; 165m appeals; ~30% reversals; 52% OOC reversals | https://digital-strategy.ec.europa.eu/en/policies/dsa-impact-platforms
SRC-006 | ◈ | fam:D | JOC-SHADOWBAN-2023 | Journal of Communication — Silenced on social media | 2023-01-02 | 2026-09-08T09:50:00+02:00 | n≈25,000 audit; shadowbans rare; politics both left/right more likely downtiered | https://academic.oup.com/joc/article-pdf/73/2/163/49678253/jqac050.pdf
SRC-007 | ◈ | fam:E | PNAS-TWITTER-AMPLIFICATION | PNAS — Algorithmic amplification of politics on Twitter | 2021-12-21 | 2026-09-08T09:50:00+02:00 | nearly 2m control accounts; 7 countries; political right higher amplification | https://doi.org/10.1073/pnas.2025334119
SRC-008 | ◈ | fam:other:tiktok-audit | ARXIV-2607.17356 | Ibrahim & Girmay — Auditing Differential Visibility of Political Content on TikTok | 2026-07-19 | 2026-09-08T09:50:00+02:00 | 556,946 hourly observations; 2,753 videos/67 accounts; account-level null | https://arxiv.org/abs/2607.17356
SRC-009 | ○ | fam:other:tiktok | TIKTOK-POL-ACCOUNTS-2022 | TikTok — Updating our policies for political accounts | 2022-09-21 | 2026-09-08T09:50:00+02:00 | political accounts advertising off; monetization features unavailable | https://newsroom.tiktok.com/updating-our-policies-for-political-accounts?lang=en
SRC-010 | ○ | fam:other:tiktok | TIKTOK-GUIDELINES-2024 | TikTok — Community Guidelines: Integrity and Authenticity | 2024-04-17 | 2026-09-08T09:50:00+02:00 | unverified election claims and some misinformation FYF-ineligible; paid political promotion prohibited | https://www.tiktok.com/community-guidelines/en/integrity-authenticity/
SRC-011 | ○ | fam:other:youtube | YOUTUBE-ELECTION-2023 | YouTube — US election misinformation update | 2023-06-02 | 2026-09-08T09:50:00+02:00 | authoritative election sources prominent in search/recommendations | https://blog.youtube/inside-youtube/us-election-misinformation-update-2023/
SRC-012 | ◈ | fam:other:epj | EPJ-TWITTER-MOD-2023 | EPJ Data Science — Twitter account moderation during major events | 2023-10-04 | 2026-09-08T09:50:00+02:00 | 270M tweets/16M users; 2022 French election; suspended accounts behavior | https://link.springer.com/article/10.1140/epjds/s13688-023-00420-7

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://about.fb.com/news/2021/02/reducing-political-content-in-news-feed/ | other:meta | 2026-09-08 | Meta a explicitement réduit la distribution politique | Meta indique avoir testé dès 2021 une réduction temporaire de la distribution de contenu politique dans le News Feed, puis modifié les signaux de ranking utilisés pour ce contenu. | -
FCT-002 | FACT | ✧ | https://about.fb.com/news/2021/02/reducing-political-content-in-news-feed/ | other:meta | 2026-09-08 | Réduction politique globale via poids des signaux | Meta indique qu’en juillet 2022 la baisse du poids des partages et commentaires pour le contenu politique avait réduit la quantité de contenu politique vue et que ces changements avaient été implémentés globalement. | -
FCT-003 | FACT | ✧ | https://about.fb.com/news/2021/02/reducing-political-content-in-news-feed/ | other:meta | 2026-09-08 | Impact trafic reconnu par Meta | Meta indiquait que ses changements de ranking politique pouvaient affecter plus largement les contenus d’affaires publiques et le trafic des éditeurs. | -
FCT-004 | FACT | ✧ | https://about.fb.com/news/2021/02/reducing-political-content-in-news-feed/ | other:meta | 2026-09-08 | Exemption initiale des agences gouvernementales | Dans les tests initiaux 2021 de réduction de distribution politique, Meta exemptait le contenu des agences et services gouvernementaux officiels. | -
FCT-005 | FACT | ✧ | https://about.fb.com/ltam/news/2024/02/actualizacion-sobre-nuestro-abordaje-al-contenido-politico-en-instagram-y-threads/ | other:meta | 2026-09-08 | Instagram/Threads 2024 limitaient les recommandations politiques | En février 2024, Meta annonçait ne pas recommander proactivement du contenu politique de comptes non suivis dans les surfaces de recommandation Instagram et Threads. | -
FCT-006 | FACT | ✧ | https://about.fb.com/ltam/news/2024/02/actualizacion-sobre-nuestro-abordaje-al-contenido-politico-en-instagram-y-threads/ | other:meta | 2026-09-08 | Restriction 2024 portait sur recommandations, pas abonnements | La politique 2024 s’appliquait à Explore, Reels, recommandations de Feed et utilisateurs suggérés, sans changer l’affichage du contenu des comptes déjà suivis. | -
FCT-007 | FACT | ✧ | https://about.fb.com/ltam/news/2024/02/actualizacion-sobre-nuestro-abordaje-al-contenido-politico-en-instagram-y-threads/ | other:meta | 2026-09-08 | Recours de recommandation prévu pour comptes professionnels | Meta indiquait que les comptes professionnels pouvaient consulter leur éligibilité à la recommandation, modifier ou supprimer des publications politiques récentes et demander une révision. | -
FCT-008 | FACT | ✧ | https://about.fb.com/news/2025/01/meta-more-speech-fewer-mistakes/ | other:meta | 2026-09-08 | Meta réintroduit davantage de contenu politique en 2025 | En janvier 2025, Meta annonçait qu’il allait réintroduire progressivement davantage de contenu civique/politique dans Facebook, Instagram et Threads avec une approche plus personnalisée. | -
FCT-009 | FACT | ✧ | https://about.fb.com/news/2025/01/meta-more-speech-fewer-mistakes/ | other:meta | 2026-09-08 | Politique Meta de visibilité politique n’est pas temporellement stable | Le changement 2025 montre que la politique explicite de recommandation politique de Meta a évolué matériellement après les restrictions 2021-2024. | -
FCT-010 | FACT | ✧ | https://about.fb.com/news/2025/01/meta-more-speech-fewer-mistakes/ | other:meta | 2026-09-08 | Meta annonce arrêt de la démotion fact-check US | Dans la transition américaine vers Community Notes, Meta annonçait qu’il arrêterait de démoter le contenu fact-checké, montrant qu’une démotion liée à fact-checking était bien une intervention de visibilité distincte de la suppression. | -
FCT-011 | FACT | ✧ | https://transparency.x.com/dsa-transparency-report.html | other:x | 2026-09-08 | X utilise officiellement des restricted reach labels | Le rapport DSA de X distingue explicitement des Restricted Reach Labels comme type d’intervention de modération, avec détection automatisée et revue manuelle. | -
FCT-012 | FACT | ✧ | https://transparency.x.com/dsa-transparency-report.html | other:x | 2026-09-08 | X France: 39 454 labels automatisés hateful conduct | Du 1er avril au 30 septembre 2024, X rapporte 39 454 restricted reach labels en France pour Hateful Conduct détecté par moyens automatisés à l’initiative de la plateforme. | -
FCT-013 | FACT | ✧ | https://transparency.x.com/dsa-transparency-report.html | other:x | 2026-09-08 | X France: volume additionnel de restrictions manuelles | Sur la même période, les catégories affichées par X totalisent 61 550 restricted reach labels en France si l’on additionne les lignes Hateful Conduct, Abuse & Harassment et Violent Speech en automatisé/revue manuelle listées dans le rapport. | -
FCT-014 | FACT | ✧ | https://transparency.x.com/dsa-transparency-report.html | other:x | 2026-09-08 | X France: requêtes élections != ordres de retrait | X rapporte cinq information requests provenant de France classées sous effets négatifs sur le discours civique ou les élections, mais aucun ordre de retrait français dans cette catégorie sur la période. | -
FCT-015 | FACT | ✧ | https://transparency.x.com/dsa-transparency-report.html | other:x | 2026-09-08 | X France: ordres de retrait observés dans autre catégorie | Les huit ordres de retrait français rapportés par X sur la période concernent la catégorie produits dangereux ou illégaux, pas le discours civique ou les élections. | -
FCT-016 | FACT | ✧ | https://transparency.x.com/dsa-transparency-report.html | other:x | 2026-09-08 | X France: appels suspension et renversements | Pour les violations des règles/TOS, X rapporte en France 46 222 plaintes contre suspension de compte et 12 047 décisions renversées sur la période. | -
FCT-017 | FACT | ✧ | https://transparency.x.com/dsa-transparency-report.html | other:x | 2026-09-08 | X France: appels actions contenu et renversements | X rapporte en France 6 772 plaintes contre des actions sur contenu et 793 décisions renversées sur la même période. | -
FCT-018 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/dsa-impact-platforms | A | 2026-09-08 | DSA: près de 30% des appels internes renversés | Depuis 2024, plus de 165 millions de décisions de modération de VLOP/VLOSE ont été contestées via les mécanismes internes en UE, avec près de 30% de décisions inversées selon la Commission. | -
FCT-019 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/dsa-impact-platforms | A | 2026-09-08 | DSA: 99% des décisions H1 2025 relevaient des propres règles plateformes | La Commission indique qu’au premier semestre 2025, 99% des plus de 9 milliards de décisions de modération reportées relevaient des conditions générales propres aux plateformes plutôt que de contenus signalés comme illégaux. | -
FCT-020 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/dsa-impact-platforms | A | 2026-09-08 | DSA: règlement extrajudiciaire inverse 52% des cas clôturés étudiés | Au premier semestre 2025, des organismes de règlement extrajudiciaire ont examiné plus de 1 800 litiges Facebook/Instagram/TikTok en UE et inversé la décision de plateforme dans 52% des affaires clôturées. | -
FCT-021 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/dsa-impact-platforms | A | 2026-09-08 | DSA rend la limitation de visibilité contestable | La Commission présente le DSA comme donnant aux utilisateurs des recours contre les décisions affectant, suspendant, supprimant ou shadow-bannant contenu ou comptes. | -
FCT-022 | FACT | ✧ | https://academic.oup.com/joc/article-pdf/73/2/163/49678253/jqac050.pdf | D | 2026-09-08 | Audit 25k: shadowbans Twitter rares | L’étude Journal of Communication auditant environ 25 000 comptes Twitter conclut que les shadowbans étaient rares dans son échantillon. | -
FCT-023 | FACT | ✧ | https://academic.oup.com/joc/article-pdf/73/2/163/49678253/jqac050.pdf | D | 2026-09-08 | Comportement bot associé au shadowban | Dans cet audit, les comptes au comportement de type bot étaient plus susceptibles d’être shadowbannés et les comptes vérifiés moins susceptibles de l’être. | -
FCT-024 | FACT | ✧ | https://academic.oup.com/joc/article-pdf/73/2/163/49678253/jqac050.pdf | D | 2026-09-08 | Politique gauche et droite: réponses plus souvent downtiered | L’audit trouve que les réponses de comptes publiant des tweets politiques, à gauche comme à droite, étaient plus susceptibles d’être rétrogradées, ainsi que celles associées à des tweets offensants. | -
FCT-025 | FACT | ✧ | https://doi.org/10.1073/pnas.2025334119 | E | 2026-09-08 | Expérience massive Twitter: ranking change réellement l’exposition politique | L’étude PNAS s’appuie sur une expérience randomisée de grande échelle, incluant près de deux millions de comptes actifs quotidiens dans un contrôle chronologique, pour mesurer l’amplification algorithmique politique. | -
FCT-026 | FACT | ✧ | https://doi.org/10.1073/pnas.2025334119 | E | 2026-09-08 | Twitter: droite davantage amplifiée dans 7 pays | L’étude PNAS rapporte que, dans sept pays étudiés, la droite politique bénéficiait en moyenne d’une amplification algorithmique plus élevée que la gauche. | -
FCT-027 | FACT | ✧ | https://doi.org/10.1073/pnas.2025334119 | E | 2026-09-08 | Amplification asymétrique != preuve d’intention de suppression | L’étude établit une asymétrie d’exposition produite par le ranking mais ne démontre pas, par ce résultat seul, une intention politique de supprimer un camp. | -
FCT-028 | FACT | ✧ | https://arxiv.org/abs/2607.17356 | other:tiktok-audit | 2026-09-08 | Audit TikTok 2026: panel dense de visibilité politique | L’audit TikTok 2026 analyse 556 946 observations horaires normalisées par followers sur 2 753 vidéos provenant de 67 comptes couvrant trois sujets contestés. | -
FCT-029 | FACT | ✧ | https://arxiv.org/abs/2607.17356 | other:tiktok-audit | 2026-09-08 | TikTok: écart apparent disparaît au niveau compte | L’étude indique que l’écart de portée apparemment massif dans une analyse groupée disparaît lorsqu’on analyse au niveau indépendant du compte; elle ne trouve pas de preuve de suppression de portée modérée à forte sur les sujets testés. | -
FCT-030 | FACT | ✧ | https://arxiv.org/abs/2607.17356 | other:tiktok-audit | 2026-09-08 | Pseudoréplication peut fabriquer un faux signal de shadowban | Les auteurs attribuent l’écart apparent à la pseudoréplication et à des confusions de composition, montrant qu’un grand nombre d’observations corrélées ne constitue pas un grand nombre de preuves indépendantes. | -
FCT-031 | FACT | ✧ | https://newsroom.tiktok.com/updating-our-policies-for-political-accounts?lang=en | other:tiktok | 2026-09-08 | TikTok désactive publicité pour comptes politiques | TikTok indique que les comptes de politiciens et partis politiques ont automatiquement accès aux fonctions publicitaires désactivé. | -
FCT-032 | FACT | ✧ | https://newsroom.tiktok.com/updating-our-policies-for-political-accounts?lang=en | other:tiktok | 2026-09-08 | TikTok exclut comptes politiques de plusieurs monétisations | TikTok exclut aussi ces comptes de fonctionnalités comme cadeaux, tips, e-commerce et Creator Fund. | -
FCT-033 | FACT | ✧ | https://newsroom.tiktok.com/updating-our-policies-for-political-accounts?lang=en | other:tiktok | 2026-09-08 | Démonétisation politique TikTok est une règle catégorielle déclarée | Ces restrictions sont une politique publique par catégorie de compte; leur existence ne démontre ni censure clandestine ni ciblage idéologique au sein de la catégorie. | -
FCT-034 | FACT | ✧ | https://www.tiktok.com/community-guidelines/en/integrity-authenticity/ | other:tiktok | 2026-09-08 | TikTok peut rendre des claims électoraux inéligibles au For You Feed | Les règles TikTok rendent inéligibles au For You Feed certains contenus contenant des allégations électorales non vérifiées ou des informations susceptibles d’entraver une décision électorale informée. | -
FCT-035 | FACT | ✧ | https://www.tiktok.com/community-guidelines/en/integrity-authenticity/ | other:tiktok | 2026-09-08 | Inéligibilité FYF est une restriction de recommandation explicite | La politique TikTok distingue contenu interdit et contenu seulement inéligible au For You Feed, ce qui établit une friction de visibilité sans suppression complète. | -
FCT-036 | FACT | ✧ | https://blog.youtube/inside-youtube/us-election-misinformation-update-2023/ | other:youtube | 2026-09-08 | YouTube promeut sources électorales autoritatives en recherche/recommandations | YouTube indique vouloir montrer proéminemment des sources autoritatives lorsqu’un utilisateur cherche des nouvelles ou informations électorales, en recherche et recommandations. | -
FCT-037 | FACT | ✧ | https://blog.youtube/inside-youtube/us-election-misinformation-update-2023/ | other:youtube | 2026-09-08 | YouTube ranking autoritatif != preuve de suppression partisane | La promotion de sources dites autoritatives modifie la structure d’exposition mais ne démontre pas, à elle seule, une suppression ciblée d’un courant politique. | -
FCT-038 | FACT | ✧ | https://link.springer.com/article/10.1140/epjds/s13688-023-00420-7 | other:epj | 2026-09-08 | Étude France 2022: 270M tweets et 16M utilisateurs | L’étude EPJ Data Science analyse environ 270 millions de tweets de plus de 16 millions d’utilisateurs autour de l’invasion de l’Ukraine et de la présidentielle française 2022. | -
FCT-039 | FACT | ✧ | https://link.springer.com/article/10.1140/epjds/s13688-023-00420-7 | other:epj | 2026-09-08 | Comptes suspendus associés à comportements de spam/toxicité | Les comptes suspendus dans cette étude étaient davantage associés à activité élevée, usage excessif des réponses/mentions, spam et contenu nuisible que les comptes actifs légitimes. | -
FCT-040 | FACT | ✧ | https://link.springer.com/article/10.1140/epjds/s13688-023-00420-7 | other:epj | 2026-09-08 | Suspension pendant événement politique != motif politique établi | Les auteurs indiquent ne pouvoir que spéculer sur la cause précise d’une suspension individuelle; le chevauchement avec une élection ne suffit donc pas à prouver un motif politique. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-001
FCT-005 | SRC-002
FCT-006 | SRC-002
FCT-007 | SRC-002
FCT-008 | SRC-003
FCT-009 | SRC-003
FCT-010 | SRC-003
FCT-011 | SRC-004
FCT-012 | SRC-004
FCT-013 | SRC-004
FCT-014 | SRC-004
FCT-015 | SRC-004
FCT-016 | SRC-004
FCT-017 | SRC-004
FCT-018 | SRC-005
FCT-019 | SRC-005
FCT-020 | SRC-005
FCT-021 | SRC-005
FCT-022 | SRC-006
FCT-023 | SRC-006
FCT-024 | SRC-006
FCT-025 | SRC-007
FCT-026 | SRC-007
FCT-027 | SRC-007
FCT-028 | SRC-008
FCT-029 | SRC-008
FCT-030 | SRC-008
FCT-031 | SRC-009
FCT-032 | SRC-009
FCT-033 | SRC-009
FCT-034 | SRC-010
FCT-035 | SRC-010
FCT-036 | SRC-011
FCT-037 | SRC-011
FCT-038 | SRC-012
FCT-039 | SRC-012
FCT-040 | SRC-012

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
FCT-031 | ELIGIBLE:VERIFIE
FCT-032 | ELIGIBLE:VERIFIE
FCT-033 | ELIGIBLE:VERIFIE
FCT-034 | ELIGIBLE:VERIFIE
FCT-035 | ELIGIBLE:VERIFIE
FCT-036 | ELIGIBLE:VERIFIE
FCT-037 | ELIGIBLE:VERIFIE
FCT-038 | ELIGIBLE:VERIFIE
FCT-039 | ELIGIBLE:VERIFIE
FCT-040 | ELIGIBLE:VERIFIE

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
FCT-031 | WRITE | -
FCT-032 | WRITE | -
FCT-033 | WRITE | -
FCT-034 | WRITE | -
FCT-035 | WRITE | -
FCT-036 | WRITE | -
FCT-037 | WRITE | -
FCT-038 | WRITE | -
FCT-039 | WRITE | -
FCT-040 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:11:CAU-001 | NEXT_ACTION:13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-08T08:21:54.894998+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-029","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-030","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-031","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-032","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-033","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-034","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-035","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-036","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-037","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-038","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-039","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-040","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":40,"eligible":40,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:40;attempted:0;success:0;failure:0;blocked:40} | WRITEBACK_EXECUTION_V1:[40 rows, see section]

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
FCT-031 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-032 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-033 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-034 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-035 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-036 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-037 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-038 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-039 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-040 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
