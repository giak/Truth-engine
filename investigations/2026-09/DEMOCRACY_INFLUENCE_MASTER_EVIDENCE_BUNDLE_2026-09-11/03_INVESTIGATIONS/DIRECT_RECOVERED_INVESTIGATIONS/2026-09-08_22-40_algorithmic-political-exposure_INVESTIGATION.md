ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260908-2240-algorithmic-political-exposure | PARENT_RUN_ID:NONE | AS_OF:2026-09-08
INPUT_KIND:RUN_CARD | MISSION_MODE:DEEPEN | INPUT_REF:PATH:/mnt/data/inv091/truth_engine/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-08_algorithmic-political-exposure/2026-09-08_22-40_algorithmic-political-exposure_INPUT.md | SUBJECT_SLUG:algorithmic-political-exposure | SUBJECT_FP:sha256:5f2d26705d5e64f73888de14aba1136ba20b953cc5bda43afaac49c43b4f4e5d | INPUT_SHA256:sha256:cbbee9cee3d68ae26823118a3bffc52f998da64f63ed397d27a90ca1655e712e
COMPLEXITY:8→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/EU 2018-2026 with directly transposable comparators; platform policy/algorithm -> user/query/profile signals -> ranking/recommendation/search -> measured exposure -> audit/experiment -> persuasion/behavior/electoral effect. Preserve ranking != censorship; personalization != manipulation; exposure != persuasion; platform design != state tasking.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/NETWORK.md,clusters/FRAMING.md,clusters/TEMPORAL.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-091 — Moteurs de recherche et recommandation : structuration de l’exposition politique

## Question

Comment les moteurs de recherche et systèmes de recommandation structurent-ils l’exposition à des contenus ou acteurs politiques sans produire eux-mêmes ces contenus, et à quel point peut-on fermer la chaîne allant du classement à un effet démocratique ? L’enquête sépare explicitement : politique/objectif de plateforme, signaux utilisateur ou requête, classement/recommandation, visibilité mesurée, sélection/engagement, persuasion, comportement et résultat électoral ou politique.

## Verdict

Le **mécanisme de structuration algorithmique de l’exposition est établi**. Le DSA reconnaît formellement ce pouvoir de classement : l’article 27 impose la transparence sur les paramètres principaux des systèmes de recommandation et les options permettant aux utilisateurs de les influencer ; pour les très grandes plateformes, une option de recommandation non fondée sur le profilage doit être disponible. Les plateformes documentent elles-mêmes des contre-factuels opérationnels : Meta propose en Europe des vues chronologiques/non personnalisées sur certaines surfaces ; TikTok permet de désactiver la personnalisation au profit d’un flux populaire et de fils Following/Friends chronologiques. [SRC-001, SRC-006, SRC-009, SRC-010]

Ce pouvoir n’est pas seulement abstrait. Meta a modifié au cours du temps la quantité de contenu politique recommandée et annonce en 2025 une réintégration personnalisée de ce contenu sur la base de signaux explicites et implicites. YouTube décrit un système utilisant clics, watch time, enquêtes, likes et dislikes, et applique pour l’information des règles de promotion de sources jugées « authoritative » et de démotion de contenus « borderline ». YouTube rapporte qu’une politique de démotion lancée en 2019 a réduit de 70 % le watch time provenant de recommandations non abonnées de contenu borderline aux États-Unis. Ces éléments ferment l’arête `design/policy -> ranking -> exposure` mais pas automatiquement `exposure -> persuasion`. [SRC-007, SRC-008, SRC-011, SRC-012]

## Exposition ≠ consommation

Le contrôle Google Search est important : l’étude Nature 2023 montre que les utilisateurs ont choisi de consulter des nouvelles plus partisanes que celles auxquelles les résultats de recherche les exposaient. L’ordre algorithmique structure donc le menu d’attention, mais la sélection de l’utilisateur constitue une arête causale distincte. [SRC-013]

## Effet politique : causal mais non uniforme

Les expériences randomisées empêchent deux conclusions symétriquement excessives.

Sur Facebook, réduire fortement l’exposition à des sources politiquement affines pendant l’élection américaine de 2020 n’a pas produit de baisse détectable de la polarisation affective ni de changement correspondant sur les principales attitudes politiques mesurées. Cela falsifie `forte modification d’exposition -> effet politique nécessaire`. [SRC-014]

À l’inverse, l’expérience randomisée publiée dans Nature en 2026 sur X montre qu’activer pendant sept semaines le fil algorithmique plutôt que chronologique a accru l’engagement et déplacé plusieurs opinions politiques dans une direction plus conservatrice. L’étude n’a cependant pas détecté d’effet significatif sur la partisanerie déclarée ni sur la polarisation affective. Cela ferme **case-specifically** `algorithmic feed -> changed exposure/engagement -> measured opinion shift`, mais pas `recommender system -> résultat électoral`. [SRC-015]

Le résultat commun n’est donc ni « les algorithmes n’ont pas d’effet » ni « les algorithmes manipulent mécaniquement l’opinion ». L’effet dépend du design, du contenu promu/démis, de la situation initiale de l’utilisateur, de la durée et de la variable politique mesurée.

## Risques électoraux et niveau de preuve

La Commission traite explicitement les systèmes de recommandation comme un vecteur possible de risque systémique pour le débat civique et les élections. Elle a demandé en 2024 à YouTube, Snapchat et TikTok des informations sur leurs paramètres et leur rôle dans ces risques, puis a ouvert une procédure TikTok liée à l’élection roumaine, visant notamment l’exploitation coordonnée ou automatisée du système de recommandation. Ces actes justifient une enquête et des obligations d’atténuation ; ils ne constituent pas une preuve qu’un algorithme ou un commanditaire a changé un résultat électoral. [SRC-002, SRC-003, SRC-004]

De même, la conclusion préliminaire de 2026 contre TikTok sur la conception addictive inclut son système hautement personnalisé, mais porte sur les risques de bien-être et de comportement compulsif. Elle ne doit pas être recyclée comme preuve de persuasion politique ou de biais partisan. [SRC-005]

## Frontières forensiques

- `ranking != censorship` : promotion, démotion et ordre peuvent changer la visibilité sans retirer le contenu.
- `personalization != manipulation` : personnaliser est un mécanisme ; la qualification de manipulation exige intention, tromperie ou autre propriété supplémentaire.
- `algorithmic_bias != intentional_tasking` : un résultat asymétrique ne suffit pas à établir qui l’a voulu ou commandé.
- `platform_design != state_tasking` : les obligations ou enquêtes réglementaires ne démontrent pas une instruction étatique sur un classement particulier.
- `exposure != persuasion` : le contrôle Google et le contrôle Meta ferment cette séparation.
- `persuasion != electoral_effect` : même l’expérience X ne mesure pas un changement de résultat électoral.
- `regulatory_inquiry != violation_or_causality` : une demande d’information ou une procédure ouvre une question probatoire ; elle ne la ferme pas.

## Effet démocratique retenu

L’effet directement établi est un **effet sur l’exposition** : les opérateurs de recherche et recommandation déterminent quelles informations deviennent plus ou moins visibles, dans quel ordre et pour quels profils. Un effet sur l’opinion est démontré dans au moins un dispositif expérimental comparable, tandis qu’un autre dispositif de grande ampleur donne un résultat nul sur les attitudes politiques malgré une forte modification de l’exposition. La causalité vers comportement de vote, résultat électoral ou décision publique en France/UE reste non établie.

## Conclusion

`INV-091` ferme donc le mécanisme générique `platform policy / user signals -> ranking / recommendation -> changed exposure`. Elle ferme aussi, mais uniquement **case-specifically**, la possibilité d’un effet causal sur certaines opinions politiques. Elle ne ferme pas une architecture générale de manipulation algorithmique, un biais partisan intentionnel, un tasking étatique ni un effet causal sur une élection française ou européenne.

Les prochains gains probatoires nécessitent soit un audit reproductible avec dénominateurs d’exposition politique, soit une expérience/quasi-expérience France/UE reliant classement à comportement, soit une pièce authentifiée de tasking portant sur une intervention algorithmique nommée.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:4|EDI_DECISIVE:7|SRC_COMPLETE:15/15

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-08
- **freshness:** DSA recommender obligations and 2024-2026 enforcement prioritized; platform policy and 2023-2026 experiments rechecked
- **period:** 2018-2026

### MANIPULATION_REPORT
- **assumptions:**
  - ordering can change exposure without removing content
  - exposure is upstream of persuasion
- **clusters:**
  - POWER
  - NETWORK
  - FRAMING
  - TEMPORAL
- **complexity:** APEX
- **implicit:**
  - platform optimization objectives shape discovery opportunities
  - user choice can amplify or counter platform exposure
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - ranking objective
  - user/profile signals
  - personalization
  - chronological counterfactual
  - promotion/demotion
  - political-content policy
  - search ordering
  - randomized experiment
- **priorities:**
  - DSA legal mechanics
  - platform counterfactual controls
  - political/news ranking policies
  - measured exposure
  - randomized political-effect evidence
  - tasking/electoral ceiling
- **query_guidance:** separate platform policy, ranking exposure, user selection, persuasion and electoral effect; prefer regulatory/platform primary sources plus randomized experiments
- **rhetorical:** bounded exposure-effect chain
- **speaker:**
  - **goal:** test ranking and recommendation as exposure infrastructure without presuming censorship or persuasion
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** algorithm
  - **S02:** objective
  - **S03:** signal
  - **S04:** profile
  - **S05:** query
  - **S06:** ranking
  - **S07:** recommendation
  - **S08:** promotion
  - **S09:** demotion
  - **S10:** chronological option
  - **S11:** non-profiling option
  - **S12:** exposure
  - **S13:** engagement
  - **S14:** persuasion
  - **S15:** electoral effect
- **threats:**
  - ranking-to-censorship collapse
  - bias-to-intent inflation
  - inquiry-to-violation inflation
  - exposure-to-persuasion inflation
  - comparator-to-France generalization

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - France/EU causal design
    - political exposure denominator
    - tasking evidence
  - **input_ids:**
    - LED-001
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no ranking=censorship collapse
    - no authenticated state tasking
    - no generalized electoral causal closure
  - **not_computable:**
    - generalized electoral effect absent causal design
    - partisan command absent tasking record
  - **operations_applied:**
    - bounded mechanism mapping
  - **reason:** relevant to ranking power, platform-user-regulator network, political-content framing and temporal feed effects
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
    - France/EU causal design
    - political exposure denominator
    - tasking evidence
  - **input_ids:**
    - LED-001
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no ranking=censorship collapse
    - no authenticated state tasking
    - no generalized electoral causal closure
  - **not_computable:**
    - generalized electoral effect absent causal design
    - partisan command absent tasking record
  - **operations_applied:**
    - bounded mechanism mapping
  - **reason:** relevant to ranking power, platform-user-regulator network, political-content framing and temporal feed effects
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
    - France/EU causal design
    - political exposure denominator
    - tasking evidence
  - **input_ids:**
    - LED-001
  - **module:** clusters/FRAMING.md
  - **negative_results:**
    - no ranking=censorship collapse
    - no authenticated state tasking
    - no generalized electoral causal closure
  - **not_computable:**
    - generalized electoral effect absent causal design
    - partisan command absent tasking record
  - **operations_applied:**
    - bounded mechanism mapping
  - **reason:** relevant to ranking power, platform-user-regulator network, political-content framing and temporal feed effects
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
    - France/EU causal design
    - political exposure denominator
    - tasking evidence
  - **input_ids:**
    - LED-001
  - **module:** clusters/TEMPORAL.md
  - **negative_results:**
    - no ranking=censorship collapse
    - no authenticated state tasking
    - no generalized electoral causal closure
  - **not_computable:**
    - generalized electoral effect absent causal design
    - partisan command absent tasking record
  - **operations_applied:**
    - bounded mechanism mapping
  - **reason:** relevant to ranking power, platform-user-regulator network, political-content framing and temporal feed effects
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
  - European Commission
  - Meta
  - TikTok
  - YouTube/Google
  - users
  - independent researchers
- **domains:**
  - recommender transparency
  - personalization
  - ranking
  - search
  - political content
  - election risk
  - exposure
  - causal effect
- **evidence_limits:**
  - France/EU causal electoral experiment absent
  - platform self-description is not independent validation
  - cross-platform experimental results are heterogeneous
  - state/partisan tasking not identified
- **exclusions:**
  - ranking as censorship
  - personalization as manipulation
  - regulatory inquiry as violation
  - algorithmic bias as tasking
  - exposure as persuasion
  - persuasion as electoral outcome
- **geo:** France/EU with directly transposable comparators
- **object_coverage:** Covers EU legal obligations, platform design choices and counterfactual feeds, political/news recommendation policies, search exposure and randomized feed experiments.
- **object_question:** When do search/recommendation systems merely order content, when do they materially change political exposure, and what evidence is required before inferring manipulation, tasking, persuasion or electoral effect?
- **period:** 2018-2026

### CREDO
- **lead_question:** Does algorithmic ordering merely personalize discovery or create a measurable political exposure channel with downstream causal effects?
- **object_question:** Trace policy/algorithm -> signals -> ranking/recommendation -> exposure -> selection/engagement -> persuasion -> behavior/electoral effect.
- **search_principle:** mechanism first; require experimental or quasi-experimental closure for persuasion and tasking evidence for command

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - design->signals
  - signals->ranking
  - ranking->exposure
  - exposure->selection
  - selection->attitude
  - attitude->behavior/outcome
- **priorities:**
  - legal transparency
  - platform counterfactuals
  - political ranking choices
  - measurement
  - randomized evidence
  - external validity
- **query_guidance:** use direct platform/regulator records for mechanics and peer-reviewed experiments for causal effects
- **speaker:**
  - **goal:** bounded algorithmic-exposure mechanism test
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **threats:**
  - black-box intentionality inference
  - user-choice omission
  - platform-specific overgeneralization

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** Chronological/non-profiled alternatives and demotion mechanisms show ordering can change exposure without removing content.
  - **resolution:** Classify ranking as exposure governance; reserve censorship for restriction/removal or equivalent access denial.
  - **thesis:** Algorithmic ranking is equivalent to censorship.
- **item 2:**
  - **antithesis:** Meta randomized evidence found exposure changes without detectable political-attitude change, while X found specific opinion shifts.
  - **resolution:** Treat persuasion as contingent and design-specific, not automatic.
  - **thesis:** If algorithms change exposure they necessarily change political attitudes.
- **item 3:**
  - **antithesis:** Platform objectives, user signals and regulatory inquiries can produce or investigate skew without a tasking chain.
  - **resolution:** Require authenticated intent/tasking evidence before command attribution.
  - **thesis:** Political bias in output proves partisan or state command.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **from:** user behavior/query/profile
  - **resource:** signals and inferred relevance
  - **support:**
    - FCT-002
    - FCT-017
    - FCT-022
    - FCT-025
  - **to:** ranking system
- **item 2:**
  - **from:** ranking/recommender system
  - **resource:** ordered visibility and discovery opportunities
  - **support:**
    - FCT-013
    - FCT-015
    - FCT-019
    - FCT-021
    - FCT-023
    - FCT-024
  - **to:** user attention
- **item 3:**
  - **from:** platform policy/regulation
  - **resource:** objectives, eligibility constraints, transparency and control requirements
  - **support:**
    - FCT-001
    - FCT-003
    - FCT-004
    - FCT-014
    - FCT-015
    - FCT-019
  - **to:** ranking system

### ACTOR_NETWORK_MAP
- **item 1:**
  - **edge:** designs objectives, signals and eligibility
  - **from:** platform operator
  - **support:**
    - FCT-012
    - FCT-015
    - FCT-017
    - FCT-021
    - FCT-022
    - FCT-023
  - **to:** ranking/recommender
- **item 2:**
  - **edge:** transparency, user-choice and systemic-risk obligations plus enforcement scrutiny
  - **from:** European Commission / DSA
  - **support:**
    - FCT-001
    - FCT-003
    - FCT-004
    - FCT-006
    - FCT-008
  - **to:** platform operator
- **item 3:**
  - **edge:** changes ordering/exposure before user selection
  - **from:** ranking/recommender
  - **support:**
    - FCT-013
    - FCT-017
    - FCT-020
    - FCT-024
    - FCT-026
    - FCT-027
  - **to:** user

### IMPACT_MAP
- **case_specific:**
  - YouTube borderline-content exposure reduction
  - Meta political-content ranking controls
  - X randomized opinion shifts
- **effect_limit:** Mechanism closes strongly through exposure. Causal persuasion closes only case-specifically in the X comparator; generalized France/EU political behavior or electoral outcome does not.
- **not_established:**
  - ranking equals censorship
  - systematic partisan intent across platforms
  - state tasking of ranking decisions
  - uniform persuasion effect
  - French/EU electoral causal effect
- **verified:**
  - ranking/recommendation materially structures exposure
  - platforms explicitly promote/demote or personalize political/news information
  - EU users receive non-profiled or chronological counterfactual options
  - search exposure and user-selected consumption can diverge
  - randomized feed changes can have zero or measurable political-attitude effects depending on platform/design

### CONTRADICTION_LEDGER
- **item 1:**
  - **ids:**
    - FCT-024
    - FCT-026
    - FCT-027
  - **resolution:** Ranking structures available exposure, while user selection can materially alter consumed information.
  - **status:** RESOLVED_STAGE_SEPARATION
  - **tension:** exposure power versus user choice
- **item 2:**
  - **ids:**
    - FCT-028
    - FCT-029
    - FCT-030
  - **resolution:** Political effects are contingent on platform, design, baseline feed and outcome measured; no universal effect rule.
  - **status:** RESOLVED_HETEROGENEOUS
  - **tension:** Meta null effect versus X opinion effect
- **item 3:**
  - **ids:**
    - FCT-004
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-008
    - FCT-009
  - **resolution:** Risk obligations and proceedings justify scrutiny but do not establish realized electoral causality.
  - **status:** RESOLVED_EVIDENCE_LEVEL
  - **tension:** regulatory election-risk scrutiny versus causal proof

### VERIFICATION_REPORT
- **circular_families:**
  - Platform policy descriptions are self-reports and treated as mechanics claims; peer-reviewed Nature experiments and EU legal/enforcement sources provide independent controls.
- **downgraded_ids:**
  - NONE
- **none_found_claims:**
  - authenticated state tasking of a named ranking decision
  - generalized cross-platform partisan command
  - France/EU causal electoral outcome from recommender exposure
- **remaining_gaps:**
  - France/EU randomized or quasi-experimental political-effect design
  - auditable platform-specific exposure denominators by political category
  - tasking/intent evidence beyond product objectives
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
  - **coverage:** EU law/enforcement, Meta/TikTok/YouTube ranking controls, Google Search exposure study, Meta and X randomized experiments
  - **independence:** regulator, three platform families and peer-reviewed research
  - **limits:**
    - platform mechanics partly self-described
    - causal experiments mostly US comparators
    - no France/EU electoral outcome closure
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **gap_type:** NONE
    - **independent_families:** 3
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES
    - **gap_type:** INTENT
    - **independent_families:** 3
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** YES
    - **gap_type:** CLASSIFICATION
    - **independent_families:** 2
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** YES
    - **gap_type:** GENERALIZATION
    - **independent_families:** 3
  - **item 5:**
    - **claim_id:** CLM-005
    - **direct_object:** YES
    - **gap_type:** EXTERNAL_VALIDITY
    - **independent_families:** 3
  - **item 6:**
    - **claim_id:** CLM-006
    - **direct_object:** YES
    - **gap_type:** TASKING
    - **independent_families:** 2
  - **item 7:**
    - **claim_id:** CLM-007
    - **direct_object:** YES
    - **gap_type:** EFFECT
    - **independent_families:** 2
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** multi-platform/regulatory/research
  - **perspective:** law+platform+experiment+user-choice
  - **stratification:** design->signals->ranking->exposure->selection->attitude->outcome
  - **temporal:** 2018-2026
- **edi:**
  - **assessment:** STRONG_FOR_RANKING_TO_EXPOSURE; MIXED_BUT_CAUSAL_FOR_EXPOSURE_TO_ATTITUDE; WEAK_FOR_TASKING_AND_ELECTORAL_OUTCOME
  - **flags:**
    - RANKING_POWER
    - USER_CHOICE
    - POLITICAL_POLICY
    - RANDOMIZED_NULL
    - RANDOMIZED_EFFECT
    - TASKING_GAP
    - ELECTORAL_EFFECT_GAP
- **source_counts:**
  - **primary_or_direct:** 12
  - **provenance_families:** 5
  - **secondary_or_peer_reviewed:** 3
  - **total:** 15

### RESPONSIBILITY_MAP
- **item 1:**
  - **actor:** Meta
  - **documented_action:** changes political-content ranking and offers EU non-ranked/chronological alternatives
  - **intent:** PRODUCT_PERSONALIZATION_AND_COMPLIANCE
  - **scope:** partisan command not established
  - **support:**
    - FCT-012
    - FCT-013
    - FCT-014
    - FCT-015
    - FCT-016
- **item 2:**
  - **actor:** TikTok
  - **documented_action:** personalizes For You and permits EU non-personalized/popular and chronological alternatives; can make election claims ineligible for recommendation
  - **intent:** RECOMMENDATION_AND_RISK_CONTROL
  - **scope:** platform-authored persuasion and electoral causality not established
  - **support:**
    - FCT-017
    - FCT-018
    - FCT-019
    - FCT-020
- **item 3:**
  - **actor:** YouTube
  - **documented_action:** uses behavioral signals and authoritativeness/borderline classifiers to promote or demote recommended content
  - **intent:** RELEVANCE_SATISFACTION_AND_RESPONSIBILITY
  - **scope:** self-described mechanics; political intent not inferred
  - **support:**
    - FCT-021
    - FCT-022
    - FCT-023
    - FCT-024
    - FCT-025
- **item 4:**
  - **actor:** European Commission
  - **documented_action:** sets transparency/non-profiling obligations and investigates systemic/election risks
  - **intent:** DSA_OVERSIGHT
  - **scope:** inquiry/guidance is not proof of realized harm
  - **support:**
    - FCT-001
    - FCT-003
    - FCT-004
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-008
    - FCT-009
    - FCT-010
    - FCT-011
- **item 5:**
  - **actor:** Independent researchers
  - **documented_action:** separate exposure from choice and experimentally test feed effects
  - **intent:** MEASUREMENT
  - **scope:** external validity to France/EU remains bounded
  - **support:**
    - FCT-026
    - FCT-027
    - FCT-028
    - FCT-029
    - FCT-030

### NEXT_QUERIES
- Reopen electoral-effect closure on a France/EU randomized or credible quasi-experimental design linking ranking exposure to political behavior or electoral outcome.
- Reopen tasking only with authenticated state/party/platform instructions tied to a named ranking or recommendation intervention.
- Reopen systematic-bias claims with platform-wide political exposure denominators and reproducible audit methods rather than complaint samples.

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-003,QRY-005,QRY-011,QRY-017,QRY-021,QRY-025,QRY-027,QRY-029 | support:- | counter:- | results:FCT-001,FCT-003,FCT-006,FCT-012,FCT-017,FCT-021,FCT-026,FCT-028,FCT-029 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-001,QRY-003 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-011,QRY-013,QRY-015,QRY-017,QRY-019 | support:- | counter:- | results:FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,FCT-020 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-017,QRY-021,QRY-023 | support:- | counter:- | results:FCT-019,FCT-021,FCT-022,FCT-023,FCT-024,FCT-025 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-025 | support:- | counter:- | results:FCT-026,FCT-027 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-027,QRY-029 | support:- | counter:- | results:FCT-028,FCT-029,FCT-030 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-005,QRY-007,QRY-009,QRY-015 | support:- | counter:- | results:FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-015 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-012,QRY-018,QRY-020,QRY-022,SRC-006,SRC-009,SRC-010,SRC-011 | support:FCT-012,FCT-013,FCT-017,FCT-018,FCT-021,FCT-023,FCT-024 | counter:- | results:FCT-012,FCT-013,FCT-017,FCT-018,FCT-021,FCT-023,FCT-024 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-014,QRY-016,QRY-018,QRY-022,SRC-007,SRC-008,SRC-009,SRC-011 | support:FCT-014,FCT-015,FCT-016,FCT-019,FCT-022,FCT-023 | counter:- | results:FCT-014,FCT-015,FCT-016,FCT-019,FCT-022,FCT-023 | final:SUPPORTED | gap:INTENT
CLM-003 | attempts:QRY-012,QRY-018,QRY-020,QRY-022,QRY-026,SRC-006,SRC-009,SRC-010,SRC-011,SRC-013 | support:FCT-024 | counter:FCT-013,FCT-017,FCT-020,FCT-027 | results:FCT-024,FCT-013,FCT-017,FCT-020,FCT-027 | final:PARTIAL | gap:CLASSIFICATION
CLM-004 | attempts:QRY-028,QRY-030,SRC-014,SRC-015 | support:FCT-029 | counter:FCT-028,FCT-030 | results:FCT-029,FCT-028,FCT-030 | final:PARTIAL | gap:GENERALIZATION
CLM-005 | attempts:QRY-028,QRY-030,SRC-014,SRC-015 | support:FCT-029,FCT-030 | counter:FCT-028 | results:FCT-029,FCT-030,FCT-028 | final:SUPPORTED | gap:EXTERNAL_VALIDITY
CLM-006 | attempts:QRY-006,QRY-008,QRY-010,QRY-016,SRC-003,SRC-004,SRC-005,SRC-008 | support:FCT-008 | counter:FCT-007,FCT-009,FCT-011,FCT-015 | results:FCT-008,FCT-007,FCT-009,FCT-011,FCT-015 | final:PARTIAL | gap:TASKING
CLM-007 | attempts:QRY-004,QRY-006,QRY-008,QRY-028,QRY-030,SRC-002,SRC-003,SRC-004,SRC-014,SRC-015 | support:FCT-004,FCT-008 | counter:FCT-005,FCT-007,FCT-009,FCT-028,FCT-030 | results:FCT-004,FCT-008,FCT-005,FCT-007,FCT-009,FCT-028,FCT-030 | final:PARTIAL | gap:EFFECT

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-002 | CLM | SUPPORTED | INTENT | Intent is established at design/policy level, not necessarily partisan intent.
CLM-003 | CLM | PARTIAL | CLASSIFICATION | Ranking can change exposure without content removal, and user choice remains a separate stage.
CLM-004 | CLM | PARTIAL | GENERALIZATION | Randomized evidence is heterogeneous across Meta and X.
CLM-005 | CLM | SUPPORTED | EXTERNAL_VALIDITY | Direct causal evidence reviewed is a US X comparator, not France/EU electoral outcome evidence.
CLM-006 | CLM | PARTIAL | TASKING | No authenticated state instruction or partisan command chain over a named ranking decision was identified.
CLM-007 | CLM | PARTIAL | EFFECT | No France/EU experiment or design closes exposure -> persuasion -> behavior -> electoral outcome.

SEMANTIC_COUNTS_V1:LED:1|CLM:7|AXS:6|CAU:1|CTRL:9|ACT:5

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-003","QRY-005","QRY-011","QRY-017","QRY-021","QRY-025","QRY-027","QRY-029"],"evidence_excerpt":"platform policy and user/profile signals -> ranking/recommendation -> measured exposure; causal political effects vary by design and platform","kind":"DECISIVE","lead":"How do search and recommendation systems alter political exposure, and when does a measured exposure change become persuasion, behavior or democratic effect?","linked_ids":["AXS-001","AXS-002","AXS-003","AXS-004","AXS-005","AXS-006"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-003","FCT-006","FCT-012","FCT-017","FCT-021","FCT-026","FCT-028","FCT-029"],"routes":["POWER","NETWORK","FRAMING","TEMPORAL"],"source_id":"RUN_CARD","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Search and recommendation systems materially structure what users are exposed to even when the platform does not author or remove the underlying content.","claimant":"INV-091","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-012","FCT-013","FCT-017","FCT-018","FCT-021","FCT-023","FCT-024"]}
CLM-002 | {"claim":"Platform operators intentionally select ranking objectives and signals that can increase, decrease or reorder political/news exposure.","claimant":"INV-091","counter":"NONE_FOUND","gap":"Intent is established at design/policy level, not necessarily partisan intent.","gap_type":"INTENT","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-014","FCT-015","FCT-016","FCT-019","FCT-022","FCT-023"]}
CLM-003 | {"claim":"A measured visibility or exposure change is equivalent to censorship or political manipulation.","claimant":"INV-091","counter":["FCT-013","FCT-017","FCT-020","FCT-027"],"gap":"Ranking can change exposure without content removal, and user choice remains a separate stage.","gap_type":"CLASSIFICATION","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-024"]}
CLM-004 | {"claim":"Algorithmic political exposure has a uniform causal effect on political attitudes across platforms.","claimant":"INV-091","counter":["FCT-028","FCT-030"],"gap":"Randomized evidence is heterogeneous across Meta and X.","gap_type":"GENERALIZATION","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-029"]}
CLM-005 | {"claim":"Recommendation systems can causally alter political opinions under some conditions.","claimant":"INV-091","counter":["FCT-028"],"gap":"Direct causal evidence reviewed is a US X comparator, not France/EU electoral outcome evidence.","gap_type":"EXTERNAL_VALIDITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-029","FCT-030"]}
CLM-006 | {"claim":"Algorithmic bias or platform ranking design establishes state tasking or partisan command.","claimant":"INV-091","counter":["FCT-007","FCT-009","FCT-011","FCT-015"],"gap":"No authenticated state instruction or partisan command chain over a named ranking decision was identified.","gap_type":"TASKING","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-008"]}
CLM-007 | {"claim":"The reviewed evidence establishes a causal effect on French or EU electoral outcomes.","claimant":"INV-091","counter":["FCT-005","FCT-007","FCT-009","FCT-028","FCT-030"],"gap":"No France/EU experiment or design closes exposure -> persuasion -> behavior -> electoral outcome.","gap_type":"EFFECT","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-004","FCT-008"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-003"],"axis":"legal_transparency_and_choice","links":["LED-001"],"question":"What ranking transparency and non-profiling choices does EU law require?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004"],"sought_objects":["Article 27 parameters","Article 38 non-profiling option"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-011","QRY-013","QRY-015","QRY-017","QRY-019"],"axis":"platform_design_controls","links":["LED-001"],"question":"How do platforms explicitly alter personalized, chronological, popular or political-content ranking?","result_ids":["FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018","FCT-020"],"sought_objects":["feed options","political controls","system cards"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-017","QRY-021","QRY-023"],"axis":"visibility_mechanism","links":["LED-001"],"question":"Can ranking or recommendation change exposure without removal?","result_ids":["FCT-019","FCT-021","FCT-022","FCT-023","FCT-024","FCT-025"],"sought_objects":["promotion","demotion","recommendation eligibility","watchtime exposure"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-025"],"axis":"search_user_choice","links":["LED-001"],"question":"How much does ranked search exposure differ from user-selected consumption?","result_ids":["FCT-026","FCT-027"],"sought_objects":["search results","clicks","partisan exposure"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-027","QRY-029"],"axis":"causal_political_effect","links":["LED-001"],"question":"Do randomized changes in algorithmic feeds change political attitudes or behavior?","result_ids":["FCT-028","FCT-029","FCT-030"],"sought_objects":["randomized feed experiments","attitudes","engagement"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-005","QRY-007","QRY-009","QRY-015"],"axis":"tasking_and_intent","links":["LED-001"],"question":"Does algorithmic bias or platform design establish external/state tasking or intentional partisan manipulation?","result_ids":["FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-015"],"sought_objects":["tasking record","targeted political intent","regulatory findings"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"PARTIAL","counter":["FCT-005","FCT-007","FCT-009","FCT-027","FCT-028","FCT-030"],"limit":"The chain is strongly closed through ranking and exposure, and one comparator closes exposure-to-opinion under a specific X design; generalized persuasion, state tasking and France/EU electoral effects remain unclosed.","mechanism":"platform policy/objective + user/query/profile signals -> ranking/recommendation/search ordering -> changed visibility/exposure -> user selection/engagement -> possible persuasion/opinion change -> possible behavior/electoral effect","status":"SUPPORTED","support":["FCT-012","FCT-013","FCT-015","FCT-017","FCT-018","FCT-021","FCT-022","FCT-023","FCT-024","FCT-026","FCT-028","FCT-029"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"ranking != censorship","status":"PASS","support":["FCT-013","FCT-017","FCT-020"]}
CTRL-002 | {"control":"visibility_change != political_motive","status":"PASS","support":["FCT-024","FCT-027"]}
CTRL-003 | {"control":"personalization != manipulation","status":"PASS","support":["FCT-013","FCT-017","FCT-020"]}
CTRL-004 | {"control":"correlation != causality","status":"PASS","support":["FCT-026","FCT-027"]}
CTRL-005 | {"control":"complaint_or_regulatory_inquiry != proof","status":"PASS","support":["FCT-006","FCT-007","FCT-008","FCT-009"]}
CTRL-006 | {"control":"algorithmic_bias != intentional_tasking","status":"PASS","support":["FCT-006","FCT-007","FCT-015"]}
CTRL-007 | {"control":"platform_design != state_tasking","status":"PASS","support":["FCT-004","FCT-006","FCT-015"]}
CTRL-008 | {"control":"exposure != persuasion","status":"PASS","support":["FCT-027","FCT-028"]}
CTRL-009 | {"control":"persuasion != electoral_effect","status":"PASS","support":["FCT-029","FCT-030"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"selects ranking objectives, signals, eligibility and ordering rules for recommender/search surfaces","actor":"Online platform operator","intent":"PRODUCT_AND_RISK_DESIGN","status":"DONE","support":["FCT-012","FCT-014","FCT-015","FCT-017","FCT-021","FCT-022","FCT-023"]}
ACT-002 | {"action":"supplies behavior/query/profile signals and may select personalized, chronological or non-profiling alternatives","actor":"User","intent":"USE_AND_CONTROL","status":"DONE","support":["FCT-002","FCT-003","FCT-013","FCT-017","FCT-018","FCT-025","FCT-027"]}
ACT-003 | {"action":"requires recommender transparency, non-profiling options and systemic-risk mitigation and conducts information requests or proceedings","actor":"European Commission / DSA framework","intent":"REGULATORY_OVERSIGHT","status":"DONE","support":["FCT-001","FCT-003","FCT-004","FCT-006","FCT-008","FCT-010"]}
ACT-004 | {"action":"measure ranked exposure, user choice and randomized feed effects","actor":"Researchers","intent":"CAUSAL_AND_AUDIT_MEASUREMENT","status":"DONE","support":["FCT-026","FCT-027","FCT-028","FCT-029","FCT-030"]}
ACT-005 | {"action":"supplies underlying content whose visibility can be promoted, demoted, recommended or reordered without platform authorship","actor":"Content producer","intent":"CONTENT_SUPPLY","status":"DONE","support":["FCT-019","FCT-020","FCT-023","FCT-024"]}

SEARCH_ACTIVITY_V1:WEB:15|FETCH:15|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | MNEMO_UNAVAILABLE | MnemoLite | - | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | DSA article 27 38 recommender transparency main parameters non profiling option
QRY-002 | FETCH | FOUND | SRC-001 | https://eur-lex.europa.eu/eli/reg/2022/2065/oj | DSA article 27 38 recommender transparency main parameters non profiling option
QRY-003 | WEB | FOUND | - | - | Commission DSA election guidelines recommender systems Articles 27 38 electoral risk mitigation
QRY-004 | FETCH | FOUND | SRC-002 | https://digital-strategy.ec.europa.eu/en/library/guidelines-providers-vlops-and-vloses-mitigation-systemic-risks-electoral-processes | Commission DSA election guidelines recommender systems Articles 27 38 electoral risk mitigation
QRY-005 | WEB | FOUND | - | - | Commission request information recommender systems electoral process civic discourse YouTube Snapchat TikTok
QRY-006 | FETCH | FOUND | SRC-003 | https://digital-strategy.ec.europa.eu/en/news/commission-sends-requests-information-youtube-snapchat-and-tiktok-recommender-systems-under-digital | Commission request information recommender systems electoral process civic discourse YouTube Snapchat TikTok
QRY-007 | WEB | FOUND | - | - | Commission TikTok Romania election risks recommender systems coordinated inauthentic manipulation
QRY-008 | FETCH | FOUND | SRC-004 | https://digital-strategy.ec.europa.eu/en/news/commission-opens-formal-proceedings-against-tiktok-election-risks-under-digital-services-act | Commission TikTok Romania election risks recommender systems coordinated inauthentic manipulation
QRY-009 | WEB | FOUND | - | - | Commission TikTok addictive design highly personalised recommender system preliminary breach
QRY-010 | FETCH | FOUND | SRC-005 | https://digital-strategy.ec.europa.eu/en/news/commission-preliminarily-finds-tiktoks-addictive-design-breach-digital-services-act | Commission TikTok addictive design highly personalised recommender system preliminary breach
QRY-011 | WEB | FOUND | - | - | Meta DSA Europe chronological non personalized search system cards ranking
QRY-012 | FETCH | FOUND | SRC-006 | https://about.fb.com/news/2023/08/new-features-and-additional-transparency-measures-as-the-digital-services-act-comes-into-effect/ | Meta DSA Europe chronological non personalized search system cards ranking
QRY-013 | WEB | FOUND | - | - | Meta political content feed ranking control less more political content 2025
QRY-014 | FETCH | FOUND | SRC-007 | https://about.fb.com/news/2021/02/reducing-political-content-in-news-feed/ | Meta political content feed ranking control less more political content 2025
QRY-015 | WEB | FOUND | - | - | Meta personalized political content recommendation explicit implicit signals 2025
QRY-016 | FETCH | FOUND | SRC-008 | https://about.fb.com/news/2025/01/meta-more-speech-fewer-mistakes/ | Meta personalized political content recommendation explicit implicit signals 2025
QRY-017 | WEB | FOUND | - | - | TikTok turn off personalization For You LIVE chronological following election unverified claims recommendation
QRY-018 | FETCH | FOUND | SRC-009 | https://newsroom.tiktok.com/fulfilling-commitments-dsa-update/?lang=en-150 | TikTok turn off personalization For You LIVE chronological following election unverified claims recommendation
QRY-019 | WEB | FOUND | - | - | TikTok Europe non personalized popular feed search chronological DSA
QRY-020 | FETCH | FOUND | SRC-010 | https://newsroom.tiktok.com/compliance-digital-services-act-eu?from_seo_redirect=1&lang=en-150 | TikTok Europe non personalized popular feed search chronological DSA
QRY-021 | WEB | FOUND | - | - | YouTube recommendations signals authoritative borderline demotion watchtime
QRY-022 | FETCH | FOUND | SRC-011 | https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/ | YouTube recommendations signals authoritative borderline demotion watchtime
QRY-023 | WEB | FOUND | - | - | YouTube recommendation system real time profile watch history interests signals
QRY-024 | FETCH | FOUND | SRC-012 | https://support.google.com/youtube/answer/16533387?hl=en | YouTube recommendation system real time profile watch history interests signals
QRY-025 | WEB | FOUND | - | - | Google Search partisan exposure engagement user choice algorithmic curation Nature 2023
QRY-026 | FETCH | FOUND | SRC-013 | https://www.nature.com/articles/s41586-023-06078-5 | Google Search partisan exposure engagement user choice algorithmic curation Nature 2023
QRY-027 | WEB | FOUND | - | - | Facebook like minded exposure experiment polarization political attitudes 2020 election
QRY-028 | FETCH | FOUND | SRC-014 | https://www.nature.com/articles/s41586-023-06297-w | Facebook like minded exposure experiment polarization political attitudes 2020 election
QRY-029 | WEB | FOUND | - | - | X algorithmic chronological feed randomized experiment political opinions engagement 2023
QRY-030 | FETCH | FOUND | SRC-015 | https://www.nature.com/articles/s41586-026-10098-2 | X algorithmic chronological feed randomized experiment political opinions engagement 2023

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | EU-DSA-2022-2065-A27-A38 | DSA Regulation 2022/2065 — recommender transparency and non-profiling option | 2022-10-19 | 2026-09-08 | Articles 27 and 38 | https://eur-lex.europa.eu/eli/reg/2022/2065/oj
SRC-002 | ◈ | fam:A | EC-ELECTION-GUIDELINES-2024 | Commission DSA election-risk guidelines | 2024-04-26 | 2026-09-08 | guidelines | https://digital-strategy.ec.europa.eu/en/library/guidelines-providers-vlops-and-vloses-mitigation-systemic-risks-electoral-processes
SRC-003 | ◈ | fam:A | EC-RFI-RECOMMENDERS-2024 | Commission requests information on YouTube Snapchat TikTok recommender systems | 2024-10-02 | 2026-09-08 | press release | https://digital-strategy.ec.europa.eu/en/news/commission-sends-requests-information-youtube-snapchat-and-tiktok-recommender-systems-under-digital
SRC-004 | ◈ | fam:A | EC-TIKTOK-ROMANIA-2024 | Commission formal proceedings TikTok election risks | 2024-12-17 | 2026-09-08 | press release | https://digital-strategy.ec.europa.eu/en/news/commission-opens-formal-proceedings-against-tiktok-election-risks-under-digital-services-act
SRC-005 | ◈ | fam:A | EC-TIKTOK-ADDICTIVE-2026 | Commission preliminary finding on TikTok addictive design | 2026-02-06 | 2026-09-08 | press release | https://digital-strategy.ec.europa.eu/en/news/commission-preliminarily-finds-tiktoks-addictive-design-breach-digital-services-act
SRC-006 | ◉ | fam:B | META-DSA-2023 | Meta DSA transparency and non-ranked options in Europe | 2023-08-22 | 2026-09-08 | ranking controls | https://about.fb.com/news/2023/08/new-features-and-additional-transparency-measures-as-the-digital-services-act-comes-into-effect/
SRC-007 | ◉ | fam:B | META-POLITICAL-CONTENT-2025 | Meta political content in feeds — updated policy | 2025-05-28 | 2026-09-08 | political content control | https://about.fb.com/news/2021/02/reducing-political-content-in-news-feed/
SRC-008 | ◉ | fam:B | META-MORE-SPEECH-2025 | Meta more speech and personalized political-content recommendations | 2025-01-07 | 2026-09-08 | personalized political content | https://about.fb.com/news/2025/01/meta-more-speech-fewer-mistakes/
SRC-009 | ◉ | fam:C | TIKTOK-DSA-UPDATE-2023 | TikTok DSA recommender controls | 2023-08-04 | 2026-09-08 | recommender controls | https://newsroom.tiktok.com/fulfilling-commitments-dsa-update/?lang=en-150
SRC-010 | ◉ | fam:C | TIKTOK-DSA-COMPLIANCE-2023 | TikTok DSA compliance in Europe | 2023-08-28 | 2026-09-08 | popular feed | https://newsroom.tiktok.com/compliance-digital-services-act-eu?from_seo_redirect=1&lang=en-150
SRC-011 | ◉ | fam:D | YOUTUBE-RECOMMENDER-2021 | YouTube recommendation system | 2021-09-15 | 2026-09-08 | recommendation system | https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/
SRC-012 | ◉ | fam:D | YOUTUBE-HELP-RECOMMENDER-2026 | YouTube Help — recommendation system current description | 2026-09-08 | 2026-09-08 | current help page checked 2026-09-08 | https://support.google.com/youtube/answer/16533387?hl=en
SRC-013 | ◉ | fam:E | NATURE-GOOGLE-SEARCH-2023 | Users choose to engage with more partisan news than exposed to on Google Search | 2023-05-24 | 2026-09-08 | Nature 618 342-348 | https://www.nature.com/articles/s41586-023-06078-5
SRC-014 | ◉ | fam:E | NATURE-META-LIKEMINDED-2023 | Like-minded sources on Facebook are prevalent but not polarizing | 2023-07-27 | 2026-09-08 | Nature 620 137-144 | https://www.nature.com/articles/s41586-023-06297-w
SRC-015 | ◉ | fam:E | NATURE-X-ALGORITHM-2026 | The political effects of X’s feed algorithm | 2026-02-18 | 2026-09-08 | Nature 652 416-423 | https://www.nature.com/articles/s41586-026-10098-2

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://eur-lex.europa.eu/eli/reg/2022/2065/oj | A | 2022-10-19 | Recommender transparency duty | DSA Article 27 requires platforms using recommender systems to explain in plain language the main parameters determining suggested information and their relative importance. | -
FCT-002 | FACT | ✧ | https://eur-lex.europa.eu/eli/reg/2022/2065/oj | A | 2022-10-19 | User influence over ranking | DSA Article 27 requires platforms to disclose options by which users can modify or influence recommender parameters and make selectable options directly accessible where information is prioritized. | -
FCT-003 | FACT | ✧ | https://eur-lex.europa.eu/eli/reg/2022/2065/oj | A | 2022-10-19 | Non-profiling option for VLOPs | For very large online platforms, the DSA requires at least one recommender-system option not based on profiling, creating a regulatory counterfactual to personalized ranking. | -
FCT-004 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/library/guidelines-providers-vlops-and-vloses-mitigation-systemic-risks-electoral-processes | A | 2024-04-26 | Election guidelines include recommender systems | The Commission election-risk guidelines explicitly place Articles 27 and 38 recommender obligations among DSA measures relevant to electoral-process risk mitigation. | -
FCT-005 | EVIDENCE | ✧ | https://digital-strategy.ec.europa.eu/en/library/guidelines-providers-vlops-and-vloses-mitigation-systemic-risks-electoral-processes | A | 2024-04-26 | Guidance is not proof of realized electoral harm | The existence of election-risk guidance establishes a recognized risk-management obligation, not that a specific recommender system changed an election outcome. | -
FCT-006 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/news/commission-sends-requests-information-youtube-snapchat-and-tiktok-recommender-systems-under-digital | A | 2024-10-02 | Commission scrutiny of recommender design | The Commission requested detailed information from YouTube, Snapchat and TikTok on recommender-system parameters and their role in systemic risks including electoral processes and civic discourse. | -
FCT-007 | EVIDENCE | ✧ | https://digital-strategy.ec.europa.eu/en/news/commission-sends-requests-information-youtube-snapchat-and-tiktok-recommender-systems-under-digital | A | 2024-10-02 | Request for information is investigatory | A Commission request for information identifies a regulatory question and evidence demand; it is not itself a finding that the recommender system amplified a political risk. | -
FCT-008 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/news/commission-opens-formal-proceedings-against-tiktok-election-risks-under-digital-services-act | A | 2024-12-17 | TikTok Romania proceeding targets recommender risk | The Commission opened formal proceedings on TikTok election risks after the Romanian presidential election, including risks linked to coordinated inauthentic manipulation or automated exploitation of recommender systems. | -
FCT-009 | EVIDENCE | ✧ | https://digital-strategy.ec.europa.eu/en/news/commission-opens-formal-proceedings-against-tiktok-election-risks-under-digital-services-act | A | 2024-12-17 | Formal proceeding is not final attribution | The Romanian-election proceeding records suspicion and an enforcement inquiry, not a final finding that TikTok or a state actor caused the electoral result. | -
FCT-010 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/news/commission-preliminarily-finds-tiktoks-addictive-design-breach-digital-services-act | A | 2026-02-06 | Personalized recommender included in addictive-design finding | The Commission preliminarily found TikTok in breach over addictive design features including a highly personalized recommender system, infinite scroll and autoplay. | -
FCT-011 | EVIDENCE | ✧ | https://digital-strategy.ec.europa.eu/en/news/commission-preliminarily-finds-tiktoks-addictive-design-breach-digital-services-act | A | 2026-02-06 | Wellbeing finding does not establish political effect | That preliminary finding concerns addictive-design and wellbeing risks and does not by itself establish political persuasion, ideological bias or electoral impact. | -
FCT-012 | FACT | ✧ | https://about.fb.com/news/2023/08/new-features-and-additional-transparency-measures-as-the-digital-services-act-comes-into-effect/ | B | 2023-08-22 | Meta exposes ranking logic through system cards | Meta stated it released 22 system cards explaining how AI systems rank Feed, Reels, Stories and other surfaces and the predictions used to determine relevance. | -
FCT-013 | FACT | ✧ | https://about.fb.com/news/2023/08/new-features-and-additional-transparency-measures-as-the-digital-services-act-comes-into-effect/ | B | 2023-08-22 | Meta offers non-ranked EU alternatives | Meta said EU users could choose chronological Stories and Reels from followed accounts and keyword-based Search results rather than Meta-personalized ranking. | -
FCT-014 | FACT | ✧ | https://about.fb.com/news/2021/02/reducing-political-content-in-news-feed/ | B | 2025-05-28 | Meta political-content control changes exposure policy | Meta documented a political-content control allowing users to see less political content and, by changing the default setting, potentially see more political content from followed and recommended accounts. | -
FCT-015 | FACT | ✧ | https://about.fb.com/news/2025/01/meta-more-speech-fewer-mistakes/ | B | 2025-01-07 | Meta re-personalizes political recommendations | Meta announced that political content would again be ranked and recommended using explicit signals such as likes and implicit signals such as viewing, for users predicted to want more of it. | -
FCT-016 | EVIDENCE | ✧ | https://about.fb.com/news/2021/02/reducing-political-content-in-news-feed/ | B | 2026-09-08 | Platform policy changes political exposure by design | Meta’s documented reduction and later personalized re-expansion of political content shows that platform ranking policy can intentionally change political-content exposure without changing the underlying corpus of posts. | -
FCT-017 | FACT | ✧ | https://newsroom.tiktok.com/fulfilling-commitments-dsa-update/?lang=en-150 | C | 2023-08-04 | TikTok permits disabling personalization in Europe | TikTok announced that European users could turn off personalization so For You and LIVE would show locally and globally popular videos instead of recommendations based on personal interests. | -
FCT-018 | FACT | ✧ | https://newsroom.tiktok.com/compliance-digital-services-act-eu?from_seo_redirect=1&lang=en-150 | C | 2023-08-28 | TikTok chronological following feed counterfactual | TikTok stated that when personalization is disabled, Following and Friends feeds show followed creators in chronological order rather than profile-based ranking. | -
FCT-019 | FACT | ✧ | https://newsroom.tiktok.com/fulfilling-commitments-dsa-update/?lang=en-150 | C | 2023-08-04 | TikTok recommendation eligibility can change exposure | TikTok stated that a video containing unverified claims about an unfolding election can be made ineligible for recommendation, with notice and appeal to the user. | -
FCT-020 | EVIDENCE | ✧ | https://newsroom.tiktok.com/fulfilling-commitments-dsa-update/?lang=en-150 | C | 2026-09-08 | Personalization choice changes ordering not authorship | TikTok’s personalized versus popular/chronological options create materially different ordering and discovery regimes while the platform does not itself author the underlying user content. | -
FCT-021 | FACT | ✧ | https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/ | D | 2021-09-15 | Recommendations drive large share of YouTube viewing | YouTube states recommendations drive a significant amount of overall viewership, more than channel subscriptions or search. | -
FCT-022 | FACT | ✧ | https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/ | D | 2021-09-15 | YouTube ranking uses behavioral signals | YouTube describes clicks, watch time, survey responses, sharing, likes and dislikes as signals used to predict and rank recommended videos. | -
FCT-023 | FACT | ✧ | https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/ | D | 2021-09-15 | YouTube promotes authoritative and demotes borderline information | For news and information, YouTube says human-evaluator-derived authoritativeness scores can promote content while content classified as borderline is demoted in recommendations. | -
FCT-024 | FACT | ✧ | https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/ | D | 2021-09-15 | YouTube demotion materially changed measured exposure | YouTube reported that its 2019 demotion of borderline content produced a 70% drop in watch time on non-subscribed recommended borderline content in the United States. | -
FCT-025 | FACT | ✧ | https://support.google.com/youtube/answer/16533387?hl=en | D | 2026-09-08 | YouTube current recommendation inputs remain personalized | YouTube’s current help documentation says recommendations use viewing and search history, subscriptions, likes, dislikes and feedback, and that homepage and Shorts recommendations are personalized surfaces. | -
FCT-026 | FACT | ✧ | https://www.nature.com/articles/s41586-023-06078-5 | E | 2023-05-24 | Google Search exposure less partisan than chosen engagement | A Nature study found users engaged with more partisan news than they were exposed to in Google Search results, indicating user choice increased partisan consumption beyond ranked exposure. | -
FCT-027 | EVIDENCE | ✧ | https://www.nature.com/articles/s41586-023-06078-5 | E | 2023-05-24 | Search ranking is not equivalent to consumed information | The Google Search result separates algorithmically presented exposure from user-selected clicks, falsifying any simple ranking-equals-consumption assumption. | -
FCT-028 | FACT | ✧ | https://www.nature.com/articles/s41586-023-06297-w | E | 2023-07-27 | Meta experiment changed like-minded exposure without political-attitude effect | A randomized Facebook experiment substantially reduced exposure to like-minded sources during the 2020 US election but did not detect corresponding reductions in affective polarization or changes in key political attitudes. | -
FCT-029 | FACT | ✧ | https://www.nature.com/articles/s41586-026-10098-2 | E | 2026-02-18 | X randomized feed experiment found political-opinion shifts | A randomized seven-week experiment on X found that switching users from a chronological to an algorithmic feed increased engagement and shifted several political opinions in a more conservative direction. | -
FCT-030 | EVIDENCE | ✧ | https://www.nature.com/articles/s41586-023-06297-w | E | 2026-09-08 | Political effects are platform and design contingent | Randomized evidence across Meta and X shows that substantial changes in algorithmic exposure can yield either no detectable political-attitude effect or measurable opinion shifts; exposure effects therefore cannot be generalized into a universal persuasion or electoral effect. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-002
FCT-005 | SRC-002
FCT-006 | SRC-003
FCT-007 | SRC-003
FCT-008 | SRC-004
FCT-009 | SRC-004
FCT-010 | SRC-005
FCT-011 | SRC-005
FCT-012 | SRC-006
FCT-013 | SRC-006
FCT-014 | SRC-007
FCT-015 | SRC-008
FCT-016 | SRC-007,SRC-008
FCT-017 | SRC-009
FCT-018 | SRC-010
FCT-019 | SRC-009
FCT-020 | SRC-009,SRC-010
FCT-021 | SRC-011
FCT-022 | SRC-011
FCT-023 | SRC-011
FCT-024 | SRC-011
FCT-025 | SRC-012
FCT-026 | SRC-013
FCT-027 | SRC-013
FCT-028 | SRC-014
FCT-029 | SRC-015
FCT-030 | SRC-014,SRC-015

## REFUTATION_REGISTRY_V1

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | SKIP:NOT_ELIGIBLE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | SKIP:NOT_ELIGIBLE
FCT-008 | ELIGIBLE:VERIFIE
FCT-009 | SKIP:NOT_ELIGIBLE
FCT-010 | ELIGIBLE:VERIFIE
FCT-011 | SKIP:NOT_ELIGIBLE
FCT-012 | ELIGIBLE:VERIFIE
FCT-013 | ELIGIBLE:VERIFIE
FCT-014 | ELIGIBLE:VERIFIE
FCT-015 | ELIGIBLE:VERIFIE
FCT-016 | SKIP:NOT_ELIGIBLE
FCT-017 | ELIGIBLE:VERIFIE
FCT-018 | ELIGIBLE:VERIFIE
FCT-019 | ELIGIBLE:VERIFIE
FCT-020 | SKIP:NOT_ELIGIBLE
FCT-021 | ELIGIBLE:VERIFIE
FCT-022 | ELIGIBLE:VERIFIE
FCT-023 | ELIGIBLE:VERIFIE
FCT-024 | ELIGIBLE:VERIFIE
FCT-025 | ELIGIBLE:VERIFIE
FCT-026 | ELIGIBLE:VERIFIE
FCT-027 | SKIP:NOT_ELIGIBLE
FCT-028 | ELIGIBLE:VERIFIE
FCT-029 | ELIGIBLE:VERIFIE
FCT-030 | SKIP:NOT_ELIGIBLE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-006 | WRITE | -
FCT-008 | WRITE | -
FCT-010 | WRITE | -
FCT-012 | WRITE | -
FCT-013 | WRITE | -
FCT-014 | WRITE | -
FCT-015 | WRITE | -
FCT-017 | WRITE | -
FCT-018 | WRITE | -
FCT-019 | WRITE | -
FCT-021 | WRITE | -
FCT-022 | WRITE | -
FCT-023 | WRITE | -
FCT-024 | WRITE | -
FCT-025 | WRITE | -
FCT-026 | WRITE | -
FCT-028 | WRITE | -
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
ATTEMPT-001 | {"created_at":"2026-09-08T20:58:14.125558+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-029","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":22,"eligible":22,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:22;attempted:0;success:0;failure:0;blocked:22} | WRITEBACK_EXECUTION_V1:[22 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-002 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-003 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-004 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-006 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-008 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-010 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-012 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-013 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-014 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-015 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-017 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-018 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-019 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-021 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-022 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-023 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-024 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-025 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-026 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-028 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-029 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
