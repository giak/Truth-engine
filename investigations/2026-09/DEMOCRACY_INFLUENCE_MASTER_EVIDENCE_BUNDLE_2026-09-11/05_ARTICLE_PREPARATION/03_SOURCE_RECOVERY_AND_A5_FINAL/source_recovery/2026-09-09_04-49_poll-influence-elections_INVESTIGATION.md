ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260909-0449-poll-influence-elections | PARENT_RUN_ID:NONE | AS_OF:2026-09-09
INPUT_KIND:RUN_CARD | MISSION_MODE:DEEPEN | INPUT_REF:PATH:/mnt/data/inv087/runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-09_poll-influence-elections/2026-09-09_04-49_poll-influence-elections_INPUT.md | SUBJECT_SLUG:poll-influence-elections | SUBJECT_FP:sha256:78a622a562639c12b2935a6e23d8afd0094e73ee4fadae540325f8286b5614ca | INPUT_SHA256:sha256:e57249efd7c162325fa4c53f347cc78340f998a4a5468476e65dadb69e5f1682
COMPLEXITY:8→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/EU 2012-2026 with directly transposable causal comparators; commissioner/method/question/sample/redressment -> publication/horse-race framing -> exposure -> perceived viability -> turnout/strategic vote/preference -> electoral effect. Preserve poll != opinion creation; error != manipulation; method bias != intent; publication != tasking; correlation != effect; horse-race != outcome.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/NETWORK.md,clusters/FRAMING.md,clusters/TEMPORAL.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-087 — Sondages comme technologie d’influence

## Question

Dans quelle mesure la conception, la formulation, la publication et le cadrage médiatique des sondages politiques modifient-ils les perceptions, les préférences, les comportements stratégiques ou les votes ? L’enquête sépare explicitement la fabrication de l’estimation, sa publication, l’information de viabilité qu’elle apporte, l’attention qu’elle modifie éventuellement, puis la participation, le vote stratégique, la préférence et enfin le résultat électoral contrefactuel.

## Verdict

Le corpus établit que les sondages ne sont pas seulement des instruments passifs de mesure : **une fois publiés, ils deviennent aussi des informations sur la viabilité, la proximité du scrutin ou le vainqueur attendu, et ces informations peuvent causalement modifier certains comportements électoraux**. Cette proposition est fermée par plusieurs designs indépendants : expérience naturelle française sur des résultats de sortie des urnes, discontinuité quasi expérimentale sur l’intention de participer, expériences sur le vote stratégique et expériences de bandwagon. [SRC-006, SRC-007, SRC-008, SRC-009, SRC-010]

Cette conclusion ne doit cependant pas être gonflée en « les sondages fabriquent l’opinion » ou « les sondages changent les vainqueurs ». Les effets observés sont hétérogènes, parfois limités à une petite fraction des électeurs, parfois à l’attention ou à l’intention de participer, parfois positifs ou négatifs selon le signal de viabilité. La littérature de synthèse continue d’ailleurs de décrire les effets électoraux du horse-race comme imparfaitement compris. [SRC-008, SRC-012, SRC-013, SRC-015]

## La production du sondage est auditable, mais méthode ≠ manipulation

Le droit français définit le sondage électoral comme une enquête statistique donnant, à une date donnée, une indication quantitative à partir d’un échantillon représentatif. La première publication doit identifier l’organisme, le commanditaire et l’acheteur éventuel, préciser taille d’échantillon, dates de terrain, texte intégral des questions, existence et valeur des marges d’erreur et droit de consulter la notice. [SRC-001, SRC-002]

La notice déposée auprès de la Commission des sondages ajoute l’objet, la méthode de sélection et la composition de l’échantillon, les conditions d’interrogation, la non-réponse et, le cas échéant, les critères de redressement. Elle est rendue publique. Cette architecture rend donc observables plusieurs choix capables d’affecter une estimation publiée. Mais un redressement, un biais ou une erreur n’établissent pas en eux-mêmes une intention de tromper : il faudrait une trace supplémentaire de tasking, de falsification ou de décision délibérée de distorsion. [SRC-004]

La Commission déclare exercer un contrôle systématique et intervenir publiquement lorsqu’elle constate une méconnaissance de la loi, notamment un défaut de qualité. Au 11 mars 2022, elle indiquait avoir contrôlé 120 sondages depuis le début de l’année. Cela établit l’existence d’un contrôle institutionnel dense, pas l’existence d’une manipulation systémique des sondages. [SRC-005]

Enfin, la loi interdit la publication, la diffusion ou le commentaire des sondages électoraux la veille et le jour du scrutin. Le législateur traite donc l’information issue des sondages comme potentiellement conséquente dans la période la plus sensible ; cette précaution juridique n’est pas une preuve causale d’un effet uniforme. [SRC-003]

## Participation : effets réels, interventions différentes

Le cas français des territoires d’outre-mer fournit un des résultats les plus forts du corpus. Avant une réforme de 2005, certains électeurs votaient après que les résultats métropolitains étaient déjà connus ; après la réforme, ils votaient avant. L’étude exploite cette variation pour estimer que connaître l’information de sortie des urnes réduisait la participation d’environ 11 points et augmentait, parmi ceux qui votaient encore, la probabilité de voter pour le vainqueur attendu. [SRC-006]

Un autre design, utilisant une expérience naturelle et une discontinuité par randomisation locale, trouve qu’une publication de sondage augmente d’environ 5 % l’intention de participer, avec plusieurs tests de falsification robustes. [SRC-007]

Ces deux résultats ne sont pas contradictoires au sens causal : ils ne testent pas la même intervention. Connaître un résultat quasi acquis en fin de scrutin n’est pas équivalent à recevoir un nouveau sondage pendant une campagne. Le corpus interdit donc de généraliser une direction unique « les sondages mobilisent » ou « les sondages démobilisent ».

## Vote stratégique : mécanisme établi, prévalence limitée

Dans deux campagnes réelles, Meffert et Gschwend ont manipulé expérimentalement l’information de sondage et les signaux de coalition. Le mécanisme du vote stratégique est soutenu, mais seulement pour un nombre limité d’électeurs ; la majorité des votes non sincères s’explique par d’autres facteurs. [SRC-008]

Une autre expérience web montre qu’informer les répondants de la marge d’erreur des sondages peut augmenter le vote stratégique. Cela confirme que non seulement le niveau du sondage, mais aussi la façon dont l’incertitude est présentée, peut modifier l’interprétation de la viabilité. [SRC-009]

La conclusion robuste est donc `poll information -> strategic response` pour certains électeurs, pas `poll -> strategic voting généralisé`.

## Bandwagon, Titanic et absence d’effet uniforme

Une expérience en ligne avec 1 113 participants, des organisations politiques réelles et des conséquences monétaires trouve qu’après exposition à des sondages préélectoraux, les options présentées comme majoritaires reçoivent en moyenne environ 7 % de votes supplémentaires. Le design fournit une preuve causale interne nette d’un bandwagon dans cet environnement, mais il ne s’agit pas d’un scrutin public français et son externalité doit rester bornée. [SRC-010]

En 2026, trois expériences sur des initiatives nationales trouvent un autre motif : annoncer qu’une initiative risque d’échouer réduit son soutien, un « Titanic effect » ; annoncer une probabilité de succès peut au contraire accroître le soutien. L’étude ne trouve pas d’effet underdog en faveur de l’option perdante. [SRC-012]

À l’inverse, l’étude rolling cross-section de l’élection fédérale allemande de 2021 ne trouve qu’une association limitée pour le SPD ; les autres partis ne montrent pas le même résultat et la direction causale n’est pas fermée, puisque les intentions sont également associées aux sondages publiés le jour suivant. [SRC-013]

Ces résultats écartent les deux thèses excessives : « aucun effet » et « bandwagon automatique ». La meilleure formulation est : **l’information sur la popularité ou la viabilité peut modifier les décisions, mais l’effet dépend fortement du contexte, du signal, du type d’élection et de la variable observée**.

## Horse-race : l’influence peut précéder le changement de vote

Une expérience sur les sondages de campagne montre qu’un leader donné comme largement en tête réduit la quantité d’information que les électeurs consultent avant de décider. Les candidats en retard reçoivent moins d’attention, avec un effet dépendant de l’écart annoncé, et ces changements du processus de délibération peuvent avoir un effet indirect sur le choix. [SRC-011]

Cette arête est conceptuellement importante : un sondage peut influencer l’environnement cognitif sans avoir à provoquer immédiatement un transfert de voix. `poll -> perception de viabilité -> allocation d’attention` constitue déjà un mécanisme de structuration de l’exposition, analogue à d’autres mécanismes étudiés dans le programme, mais par une information statistique plutôt que par une plateforme ou un média.

## Effet électoral et intention du commanditaire : plafond probatoire

Le corpus ne ferme pas une architecture générale `commanditaire -> méthode volontairement biaisée -> publication -> exposition -> persuasion -> changement du vainqueur` pour la France ou l’Union européenne. Le droit rend le commanditaire et de nombreux choix méthodologiques visibles, mais aucune source du run ne démontre que la pratique normale du redressement constitue une manipulation intentionnelle.

De même, les effets comportementaux établis ne suffisent pas à démontrer un vainqueur contrefactuel. Même un effet causal de participation ou de bandwagon dans une population donnée doit encore être agrégé, situé géographiquement, relié aux marges électorales et comparé à un scénario sans exposition.

## Conclusion

`INV-087` établit les sondages comme une **technologie d’information susceptible d’influencer**. Leur effet le mieux démontré passe par les attentes de viabilité : elles peuvent modifier attention, participation, vote stratégique et parfois choix. Mais le corpus ne valide ni une manipulation systémique par les instituts ou commanditaires, ni une loi générale du bandwagon, ni un effet généralisé sur les vainqueurs des élections France/UE.

Le niveau maximal soutenu atteint donc **I6 case-specifically** sur certains comportements. **I7**, le résultat électoral contrefactuel, reste ouvert.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:4|EDI_DECISIVE:7|SRC_COMPLETE:15/15

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-09
- **freshness:** French legal/regulatory framework rechecked through 2026; causal comparators span 2011-2026 with a 2026 Electoral Studies experiment.
- **period:** 2012-2026

### MANIPULATION_REPORT
- **assumptions:**
  - published viability signals can affect decisions for some voters
  - effects can be null, positive or negative depending on design and context
- **clusters:**
  - POWER
  - NETWORK
  - FRAMING
  - TEMPORAL
- **complexity:** APEX
- **implicit:**
  - polls both measure and become information inputs
  - voters can respond strategically without adopting a candidate preference
  - media attention can mediate effects before vote choice
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - question framing
  - sample construction
  - weighting/redressment
  - margin of error
  - publication timing
  - horse-race framing
  - bandwagon
  - Titanic effect
  - strategic voting
  - turnout effect
- **priorities:**
  - France legal transparency
  - causal behavior effects
  - strategic voting
  - horse-race attention
  - negative controls
  - counterfactual electoral effect
- **query_guidance:** separate production choices, publication, perceived viability, attention, turnout, strategic choice, preference and winner; prefer causal designs for downstream claims
- **rhetorical:** bounded poll-production -> viability-information -> behavior -> outcome chain
- **speaker:**
  - **goal:** test polls as influence technology without equating measurement error or methodology with manipulation
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** commissioner
  - **S02:** pollster
  - **S03:** sample
  - **S04:** question wording
  - **S05:** mode
  - **S06:** redressment
  - **S07:** estimate
  - **S08:** publication
  - **S09:** horse-race frame
  - **S10:** exposure
  - **S11:** viability expectation
  - **S12:** information seeking
  - **S13:** turnout
  - **S14:** strategic/preference shift
  - **S15:** electoral effect
- **threats:**
  - error-to-manipulation inflation
  - method-to-intent inflation
  - publication-to-tasking inflation
  - correlation-to-causality inflation
  - bandwagon universalization
  - turnout-intention-to-turnout inflation
  - behavior-to-winner inflation

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - intent/tasking evidence
    - France/EU actual-vote causal designs
    - winner counterfactual
  - **input_ids:**
    - LED-001
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no general manipulation intent
    - no universal bandwagon effect
    - no generalized France/EU winner-change closure
  - **not_computable:**
    - counterfactual election winner absent causal design
    - systematic commissioner/pollster intent absent primary tasking records
  - **operations_applied:**
    - bounded mechanism mapping
  - **reason:** relevant to commissioning/control, poll-production/publication network, horse-race framing and temporal publication effects
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
    - intent/tasking evidence
    - France/EU actual-vote causal designs
    - winner counterfactual
  - **input_ids:**
    - LED-001
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no general manipulation intent
    - no universal bandwagon effect
    - no generalized France/EU winner-change closure
  - **not_computable:**
    - counterfactual election winner absent causal design
    - systematic commissioner/pollster intent absent primary tasking records
  - **operations_applied:**
    - bounded mechanism mapping
  - **reason:** relevant to commissioning/control, poll-production/publication network, horse-race framing and temporal publication effects
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
    - intent/tasking evidence
    - France/EU actual-vote causal designs
    - winner counterfactual
  - **input_ids:**
    - LED-001
  - **module:** clusters/FRAMING.md
  - **negative_results:**
    - no general manipulation intent
    - no universal bandwagon effect
    - no generalized France/EU winner-change closure
  - **not_computable:**
    - counterfactual election winner absent causal design
    - systematic commissioner/pollster intent absent primary tasking records
  - **operations_applied:**
    - bounded mechanism mapping
  - **reason:** relevant to commissioning/control, poll-production/publication network, horse-race framing and temporal publication effects
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
    - intent/tasking evidence
    - France/EU actual-vote causal designs
    - winner counterfactual
  - **input_ids:**
    - LED-001
  - **module:** clusters/TEMPORAL.md
  - **negative_results:**
    - no general manipulation intent
    - no universal bandwagon effect
    - no generalized France/EU winner-change closure
  - **not_computable:**
    - counterfactual election winner absent causal design
    - systematic commissioner/pollster intent absent primary tasking records
  - **operations_applied:**
    - bounded mechanism mapping
  - **reason:** relevant to commissioning/control, poll-production/publication network, horse-race framing and temporal publication effects
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
  - polling organizations
  - commissioners/buyers
  - media publishers
  - Commission des sondages
  - voters
  - independent researchers
- **domains:**
  - survey methodology
  - electoral polling
  - publication rules
  - horse-race framing
  - bandwagon/underdog
  - turnout
  - strategic voting
  - vote choice
- **evidence_limits:**
  - no France/EU causal winner-change design identified
  - commissioner intent not inferable from methodology
  - survey experiments vary in external validity
  - turnout intention is not actual turnout
- **exclusions:**
  - poll error as manipulation
  - redressment as intent
  - publication as tasking
  - stated bandwagon as actual vote
  - behavioral effect as changed winner
- **geo:** France/EU with directly transposable comparators
- **object_coverage:** French legal/Commission framework plus natural, survey, online and campaign experiments on attention, turnout, bandwagon and strategic voting.
- **object_question:** When and how do poll production/publication and horse-race cues change electoral perceptions or behavior, and where does causal closure stop?
- **period:** 2012-2026

### CREDO
- **lead_question:** Can polls move behavior, and under what conditions?
- **object_question:** Trace commissioner/method/question/sample/redressment -> publication/horse-race -> exposure -> viability expectation -> turnout/strategic vote/preference -> electoral effect.
- **search_principle:** mechanism first; methodology requires intent evidence for manipulation, behavior requires causal designs, winner change requires a counterfactual outcome design

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - production->estimate
  - estimate->publication
  - publication->viability
  - viability->attention
  - viability->turnout
  - viability->strategic choice
  - behavior->outcome
- **priorities:**
  - method transparency
  - behavioral causality
  - heterogeneity
  - negative controls
  - effect ceiling
- **query_guidance:** official sources for poll-production rules; independent causal research for behavioral effects
- **speaker:**
  - **goal:** bounded poll-influence mechanism test
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **threats:**
  - method-intent conflation
  - horse-race-effect inflation
  - winner-change inference

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** Natural and randomized designs identify turnout, bandwagon, strategic-choice and information-seeking effects in some settings.
  - **resolution:** Treat polls as both measurement and information inputs; test each downstream outcome separately.
  - **thesis:** Polls merely measure opinion and therefore cannot influence it.
- **item 2:**
  - **antithesis:** French law requires methodological disclosure and redressment transparency; adjustment is a statistical operation, not proof of deceptive intent.
  - **resolution:** Require case-specific evidence of intentional distortion or tasking before classifying manipulation.
  - **thesis:** Polls manipulate elections because weighting and redressment change raw estimates.
- **item 3:**
  - **antithesis:** Effects are heterogeneous, sometimes small, party-specific or limited to turnout/attention; no general France/EU winner counterfactual is closed.
  - **resolution:** Do not promote behavioral effects to electoral-outcome causality.
  - **thesis:** Bandwagon effects mean polls change election winners.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **from:** commissioner/pollster
  - **resource:** questionnaire, sample, mode, weighting and published estimate
  - **support:**
    - FCT-003
    - FCT-004
    - FCT-007
    - FCT-011
  - **to:** media/public
- **item 2:**
  - **from:** published poll/media
  - **resource:** viability, closeness and winner-loser information
  - **support:**
    - FCT-013
    - FCT-016
    - FCT-023
    - FCT-026
  - **to:** voters
- **item 3:**
  - **from:** voters
  - **resource:** attention, turnout, strategic choice or preference response
  - **support:**
    - FCT-013
    - FCT-014
    - FCT-016
    - FCT-018
    - FCT-020
    - FCT-021
    - FCT-025
    - FCT-026
  - **to:** electoral behavior
- **item 4:**
  - **from:** French oversight
  - **resource:** disclosure, notices, corrections and blackout rule
  - **support:**
    - FCT-003
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-008
    - FCT-009
    - FCT-010
  - **to:** poll information environment

### ACTOR_NETWORK_MAP
- **item 1:**
  - **edge:** funds or requests poll
  - **from:** commissioner/buyer
  - **support:**
    - FCT-003
  - **to:** polling organization
- **item 2:**
  - **edge:** produces estimate and methodological notice
  - **from:** polling organization
  - **support:**
    - FCT-004
    - FCT-005
    - FCT-007
    - FCT-008
  - **to:** publisher/Commission
- **item 3:**
  - **edge:** disseminates poll and horse-race signal
  - **from:** publisher/media
  - **support:**
    - FCT-011
    - FCT-023
    - FCT-024
  - **to:** voters
- **item 4:**
  - **edge:** controls legal/quality compliance and can issue public corrections
  - **from:** Commission des sondages
  - **support:**
    - FCT-009
    - FCT-010
  - **to:** published-poll ecosystem
- **item 5:**
  - **edge:** may alter attention, turnout, strategy or preference
  - **from:** voters
  - **support:**
    - FCT-013
    - FCT-014
    - FCT-016
    - FCT-018
    - FCT-020
    - FCT-021
    - FCT-026
  - **to:** electoral behavior

### IMPACT_MAP
- **effect_limit:** I6 behavior is case-specifically supported; I7 counterfactual election-winner effect remains unclosed.
- **heterogeneous:**
  - strategic voting affects a minority in embedded campaigns
  - German 2021 association was party-specific and not causally closed
  - direct-democracy experiments found Titanic and success-expectation effects but no underdog effect
- **not_established:**
  - general intentional manipulation by poll commissioners or pollsters
  - uniform bandwagon response
  - general France/EU electoral winner change
  - poll error as evidence of manipulation
- **verified:**
  - French polling production/publication is subject to detailed disclosure and oversight
  - poll or exit-poll information can alter turnout or turnout intention in specific causal designs
  - bandwagon effects occur in some controlled and natural settings
  - polls can alter information seeking and strategic voting for subsets of voters

### CONTRADICTION_LEDGER
- **item 1:**
  - **ids:**
    - FCT-014
    - FCT-021
    - FCT-019
    - FCT-028
    - FCT-029
    - FCT-030
  - **resolution:** Poll effects exist but are conditional on context, treatment and outcome; no universal bandwagon law.
  - **status:** RESOLVED_HETEROGENEOUS
  - **tension:** causal bandwagon findings versus heterogeneous/null/limited effects
- **item 2:**
  - **ids:**
    - FCT-013
    - FCT-016
  - **resolution:** Exit-result information and poll-release information are distinct interventions and outcomes; direction cannot be generalized across designs.
  - **status:** RESOLVED_INTERVENTION_DIFFERENCE
  - **tension:** polls can depress or increase participation
- **item 3:**
  - **ids:**
    - FCT-007
    - FCT-008
    - FCT-012
  - **resolution:** Auditable redressment is compatible with normal statistical practice; manipulation requires independent intent/tasking evidence.
  - **status:** RESOLVED_EVIDENCE_LEVEL
  - **tension:** methodological adjustment versus manipulation claim

### VERIFICATION_REPORT
- **circular_families:**
  - French legal/regulatory sources establish rules and oversight, not behavioral effects; independent academic studies supply causal and negative controls.
- **downgraded_ids:**
  - NONE
- **none_found_claims:**
  - generalized France/EU counterfactual winner effect
  - systematic commissioner/pollster tasking to distort estimates
  - uniform bandwagon/underdog response
- **remaining_gaps:**
  - France/EU election-level causal designs
  - case-specific intentional distortion evidence
  - publication/framing exposure denominators
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
  - **coverage:** French statutory and Commission oversight plus multiple causal/experimental poll-effect designs from France and comparative democracies
  - **independence:** legal, regulator and independent academic provenance families
  - **limits:**
    - some experiments use simulated or survey outcomes
    - observational German evidence does not close causal direction
    - winner-change counterfactual absent
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **gap_type:** GENERALIZATION
    - **independent_families:** 3
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES
    - **gap_type:** NONE
    - **independent_families:** 3
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** YES
    - **gap_type:** NONE
    - **independent_families:** 2
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** YES
    - **gap_type:** INTENT
    - **independent_families:** 2
  - **item 5:**
    - **claim_id:** CLM-005
    - **direct_object:** YES
    - **gap_type:** PREVALENCE
    - **independent_families:** 2
  - **item 6:**
    - **claim_id:** CLM-006
    - **direct_object:** YES
    - **gap_type:** GENERALIZATION
    - **independent_families:** 2
  - **item 7:**
    - **claim_id:** CLM-007
    - **direct_object:** YES
    - **gap_type:** CAUSALITY
    - **independent_families:** 3
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** law/regulator/poll ecosystem/research
  - **perspective:** production+publication+attention+turnout+strategy+vote
  - **stratification:** method->publication->viability->behavior->outcome
  - **temporal:** 2011-2026
- **edi:**
  - **assessment:** STRONG_FOR_REGULATORY_TRANSPARENCY_AND_CASE_SPECIFIC_BEHAVIOR; MODERATE_FOR_BANDWAGON_STRATEGIC_GENERALIZATION; WEAK_FOR_INTENT_AND_WINNER_CHANGE
  - **flags:**
    - METHOD_DISCLOSURE
    - PUBLICATION_BLACKOUT
    - TURNOUT_EFFECT
    - BANDWAGON_CASES
    - STRATEGIC_VOTING
    - ATTENTION_EFFECT
    - HETEROGENEITY
    - INTENT_GAP
    - WINNER_EFFECT_GAP
- **source_counts:**
  - **primary_or_direct:** 5
  - **provenance_families:** 5
  - **secondary_or_peer_reviewed:** 10
  - **total:** 15

### RESPONSIBILITY_MAP
- **item 1:**
  - **actor:** Polling organizations
  - **documented_action:** produce and disclose poll methods and estimates
  - **intent:** MEASUREMENT
  - **scope:** method choices do not establish manipulation intent
  - **support:**
    - FCT-001
    - FCT-004
    - FCT-007
- **item 2:**
  - **actor:** Commissioners/buyers/publishers
  - **documented_action:** commission, buy or disseminate polling information
  - **intent:** INFORMATION_OR_MEDIA_FRAMING
  - **scope:** commissioning/publication does not establish control of result
  - **support:**
    - FCT-003
    - FCT-011
- **item 3:**
  - **actor:** Commission des sondages / legislature
  - **documented_action:** impose transparency, quality-control and timing rules
  - **intent:** ELECTORAL_INFORMATION_INTEGRITY
  - **scope:** regulation does not prove polls are generally manipulative
  - **support:**
    - FCT-006
    - FCT-007
    - FCT-009
    - FCT-010
- **item 4:**
  - **actor:** Voters
  - **documented_action:** respond in some designs through turnout, strategic choice, attention or preference
  - **intent:** ELECTORAL_DECISION
  - **scope:** effects heterogeneous; changed winner not established
  - **support:**
    - FCT-013
    - FCT-014
    - FCT-016
    - FCT-018
    - FCT-020
    - FCT-021
    - FCT-026
- **item 5:**
  - **actor:** Independent researchers
  - **documented_action:** estimate poll effects using natural, randomized, survey and observational designs
  - **intent:** CAUSAL_MEASUREMENT
  - **scope:** external validity differs by design
  - **support:**
    - FCT-013
    - FCT-016
    - FCT-018
    - FCT-021
    - FCT-023
    - FCT-026
    - FCT-028
    - FCT-029
    - FCT-030

### NEXT_QUERIES
- Reopen intentional-manipulation claims only with primary evidence of commissioner/pollster tasking, fabricated methodology or deliberate publication suppression/distortion.
- Reopen France/EU outcome closure only with credible quasi-experimental or randomized exposure designs linking polls to actual turnout/vote and a counterfactual electoral result.
- Reopen prevalence only with systematic cross-election estimates separating attention, strategic voting, preference change and actual vote effects.

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-003,QRY-005,QRY-007,QRY-009,QRY-011,QRY-013,QRY-015,QRY-017,QRY-019,QRY-021,QRY-023,QRY-025,QRY-027,QRY-029 | support:- | counter:- | results:FCT-006,FCT-013,FCT-014,FCT-016,FCT-018,FCT-020,FCT-021,FCT-023,FCT-025,FCT-026,FCT-027,FCT-028,FCT-029,FCT-030 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-001,QRY-003,QRY-005,QRY-007,QRY-009 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-021,QRY-029 | support:- | counter:- | results:FCT-023,FCT-024,FCT-025,FCT-030 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-011,QRY-019,QRY-023,QRY-025 | support:- | counter:- | results:FCT-014,FCT-021,FCT-026,FCT-027,FCT-028,FCT-029 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-011,QRY-013 | support:- | counter:- | results:FCT-013,FCT-015,FCT-016,FCT-017 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-015,QRY-017 | support:- | counter:- | results:FCT-018,FCT-019,FCT-020 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-021,QRY-025,QRY-027,QRY-029 | support:- | counter:- | results:FCT-012,FCT-022,FCT-028,FCT-029,FCT-030 | final:GAP | gap:CAUSALITY
CLM-001 | attempts:QRY-012,QRY-014,QRY-016,QRY-020,QRY-024,QRY-026,QRY-030,SRC-006,SRC-007,SRC-008,SRC-010,SRC-012,SRC-013,SRC-015 | support:FCT-013,FCT-014,FCT-016,FCT-021,FCT-026 | counter:FCT-019,FCT-028,FCT-029,FCT-030 | results:FCT-013,FCT-014,FCT-016,FCT-021,FCT-026,FCT-019,FCT-028,FCT-029,FCT-030 | final:SUPPORTED | gap:GENERALIZATION
CLM-002 | attempts:QRY-012,QRY-016,QRY-020,QRY-024,QRY-026,QRY-030,SRC-006,SRC-008,SRC-010,SRC-012,SRC-013,SRC-015 | support:FCT-019,FCT-026,FCT-027,FCT-028,FCT-029,FCT-030 | counter:FCT-014,FCT-021 | results:FCT-019,FCT-026,FCT-027,FCT-028,FCT-029,FCT-030,FCT-014,FCT-021 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-002,QRY-004,QRY-006,QRY-008,QRY-010,SRC-001,SRC-002,SRC-003,SRC-004,SRC-005 | support:FCT-001,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011 | counter:- | results:FCT-001,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-004,QRY-008,QRY-010,SRC-002,SRC-004,SRC-005 | support:FCT-003,FCT-004,FCT-005,FCT-007,FCT-008,FCT-012 | counter:- | results:FCT-003,FCT-004,FCT-005,FCT-007,FCT-008,FCT-012 | final:PARTIAL | gap:INTENT
CLM-005 | attempts:QRY-016,QRY-018,SRC-008,SRC-009 | support:FCT-018,FCT-020 | counter:FCT-019 | results:FCT-018,FCT-020,FCT-019 | final:SUPPORTED | gap:PREVALENCE
CLM-006 | attempts:QRY-022,QRY-030,SRC-011,SRC-015 | support:FCT-023,FCT-024,FCT-025 | counter:FCT-030 | results:FCT-023,FCT-024,FCT-025,FCT-030 | final:SUPPORTED | gap:GENERALIZATION
CLM-007 | attempts:QRY-010,QRY-016,QRY-020,QRY-026,QRY-030,SRC-005,SRC-008,SRC-010,SRC-013,SRC-015 | support:- | counter:FCT-012,FCT-019,FCT-022,FCT-028,FCT-029,FCT-030 | results:FCT-012,FCT-019,FCT-022,FCT-028,FCT-029,FCT-030 | final:REFUTED | gap:CAUSALITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
AXS-006 | AXS | GAP | CAUSALITY | No general France/EU design closes commissioner intent -> poll production/publication -> exposure -> changed winner.
CLM-001 | CLM | SUPPORTED | GENERALIZATION | Effect size and direction vary by context, outcome and design; no universal poll effect.
CLM-004 | CLM | PARTIAL | INTENT | Intentional distortion requires case-specific evidence beyond the existence of weighting/redressment.
CLM-005 | CLM | SUPPORTED | PREVALENCE | Most insincere voting is not explained by strategic response to polls.
CLM-006 | CLM | SUPPORTED | GENERALIZATION | Media and campaign context moderate whether attention changes translate into behavior.
CLM-007 | CLM | REFUTED | CAUSALITY | No identified design closes commissioner/tasking, exposure, persuasion and counterfactual winner for France/EU.

SEMANTIC_COUNTS_V1:LED:1|CLM:7|AXS:6|CAU:1|CTRL:9|ACT:5

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-003","QRY-005","QRY-007","QRY-009","QRY-011","QRY-013","QRY-015","QRY-017","QRY-019","QRY-021","QRY-023","QRY-025","QRY-027","QRY-029"],"evidence_excerpt":"French law and Commission rules make methodology and timing auditable; causal studies show turnout, bandwagon, strategic-vote and attention effects in some designs, with heterogeneous and bounded external validity.","kind":"DECISIVE","lead":"When do published polls measurably alter perceived viability, information seeking, turnout, strategic voting or vote choice, and where does the chain stop before an electoral outcome?","linked_ids":["AXS-001","AXS-002","AXS-003","AXS-004","AXS-005","AXS-006"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-006","FCT-013","FCT-014","FCT-016","FCT-018","FCT-020","FCT-021","FCT-023","FCT-025","FCT-026","FCT-027","FCT-028","FCT-029","FCT-030"],"routes":["POWER","NETWORK","FRAMING","TEMPORAL"],"source_id":"RUN_CARD","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Published poll or exit-poll information can causally alter electoral behavior in some settings.","claimant":"INV-087","counter":["FCT-019","FCT-028","FCT-029","FCT-030"],"gap":"Effect size and direction vary by context, outcome and design; no universal poll effect.","gap_type":"GENERALIZATION","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-013","FCT-014","FCT-016","FCT-021","FCT-026"]}
CLM-002 | {"claim":"Poll effects are heterogeneous rather than mechanically bandwagon-producing.","claimant":"INV-087","counter":["FCT-014","FCT-021"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-019","FCT-026","FCT-027","FCT-028","FCT-029","FCT-030"]}
CLM-003 | {"claim":"French law makes commissioner, questions, methodology, margins and timing partly auditable and imposes a short pre-election publication blackout.","claimant":"INV-087","counter":["NONE_FOUND"],"gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-001","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011"]}
CLM-004 | {"claim":"Method choices and redressment can change the published estimate, but methodological adjustment alone does not establish manipulation or intent.","claimant":"INV-087","counter":["NONE_FOUND"],"gap":"Intentional distortion requires case-specific evidence beyond the existence of weighting/redressment.","gap_type":"INTENT","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-003","FCT-004","FCT-005","FCT-007","FCT-008","FCT-012"]}
CLM-005 | {"claim":"Poll information can affect strategic voting for a bounded subset of voters.","claimant":"INV-087","counter":["FCT-019"],"gap":"Most insincere voting is not explained by strategic response to polls.","gap_type":"PREVALENCE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-018","FCT-020"]}
CLM-006 | {"claim":"Horse-race polling can change information seeking and candidate attention before any vote switch occurs.","claimant":"INV-087","counter":["FCT-030"],"gap":"Media and campaign context moderate whether attention changes translate into behavior.","gap_type":"GENERALIZATION","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-023","FCT-024","FCT-025"]}
CLM-007 | {"claim":"A generalized France/EU chain from poll commissioning or horse-race coverage to a changed election winner is established.","claimant":"INV-087","counter":["FCT-012","FCT-019","FCT-022","FCT-028","FCT-029","FCT-030"],"gap":"No identified design closes commissioner/tasking, exposure, persuasion and counterfactual winner for France/EU.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"REFUTED","support":["NONE_FOUND"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-003","QRY-005","QRY-007","QRY-009"],"axis":"regulatory_and_methodological_transparency","links":["LED-001"],"question":"What parts of poll production and publication are legally observable in France?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012"],"sought_objects":["commissioner","sample","question wording","margin of error","redressment","timing"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-021","QRY-029"],"axis":"publication_and_horse_race_exposure","links":["LED-001"],"question":"Can poll publication and horse-race cues alter what voters attend to or infer about candidate viability?","result_ids":["FCT-023","FCT-024","FCT-025","FCT-030"],"sought_objects":["frontrunner cue","candidate attention","information seeking","viability"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-011","QRY-019","QRY-023","QRY-025"],"axis":"bandwagon_underdog","links":["LED-001"],"question":"Do outcome expectations generate bandwagon, Titanic or underdog effects?","result_ids":["FCT-014","FCT-021","FCT-026","FCT-027","FCT-028","FCT-029"],"sought_objects":["bandwagon","Titanic effect","underdog","vote choice"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-011","QRY-013"],"axis":"turnout","links":["LED-001"],"question":"Can poll or exit-poll information causally alter participation or turnout intention?","result_ids":["FCT-013","FCT-015","FCT-016","FCT-017"],"sought_objects":["turnout","turnout intention","exit-poll information"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-015","QRY-017"],"axis":"strategic_voting","links":["LED-001"],"question":"Can polling information shift voters from sincere to strategic choices?","result_ids":["FCT-018","FCT-019","FCT-020"],"sought_objects":["strategic voting","coalition signal","margin of error"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-021","QRY-025","QRY-027","QRY-029"],"axis":"generalization_and_electoral_outcome","gap":"No general France/EU design closes commissioner intent -> poll production/publication -> exposure -> changed winner.","gap_type":"CAUSALITY","links":["LED-001"],"question":"Can these effects be generalized to France/EU election winners or intentional poll manipulation?","result_ids":["FCT-012","FCT-022","FCT-028","FCT-029","FCT-030"],"sought_objects":["external validity","France/EU causal outcome","intentional manipulation","counterfactual winner"],"status":"GAP"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"PARTIAL","counter":["FCT-012","FCT-019","FCT-022","FCT-028","FCT-029","FCT-030"],"limit":"Causal effects are established for specific intermediate outcomes and some consequential choices, but direction, prevalence and external validity are heterogeneous; no general France/EU winner-change chain or intentional commissioner manipulation is closed.","mechanism":"commissioner/method/question/sample/redressment -> published estimate and horse-race framing -> perceived viability/expected outcome -> information seeking/turnout/strategic choice/preference -> possible electoral effect","status":"SUPPORTED","support":["FCT-003","FCT-007","FCT-013","FCT-014","FCT-016","FCT-018","FCT-020","FCT-021","FCT-023","FCT-025","FCT-026"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"poll != creation of opinion","status":"PASS","support":["FCT-001","FCT-013","FCT-030"]}
CTRL-002 | {"control":"poll error != manipulation","status":"PASS","support":["FCT-004","FCT-005","FCT-012"]}
CTRL-003 | {"control":"methodological redressment != intent","status":"PASS","support":["FCT-007","FCT-008","FCT-012"]}
CTRL-004 | {"control":"publication != tasking","status":"PASS","support":["FCT-003","FCT-009","FCT-012"]}
CTRL-005 | {"control":"correlation != causal poll effect","status":"PASS","support":["FCT-028","FCT-029"]}
CTRL-006 | {"control":"bandwagon finding != universal response","status":"PASS","support":["FCT-014","FCT-019","FCT-026","FCT-030"]}
CTRL-007 | {"control":"turnout intention != actual turnout","status":"PASS","support":["FCT-016","FCT-013"]}
CTRL-008 | {"control":"horse-race attention effect != vote change","status":"PASS","support":["FCT-023","FCT-024","FCT-025"]}
CTRL-009 | {"control":"behavioral effect != changed election winner","status":"PASS","support":["FCT-013","FCT-014","FCT-021","FCT-026","FCT-030"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"designs samples, questions, fieldwork, weighting/redressment and estimates","actor":"Polling organizations","intent":"MEASURE_ESTIMATE_PUBLIC_OPINION","status":"DONE","support":["FCT-001","FCT-004","FCT-007"]}
ACT-002 | {"action":"commissions, buys or publishes polls and frames electoral viability","actor":"Commissioners, buyers and media publishers","intent":"INFORM_OR_FRAME_ELECTORAL_COMPETITION","status":"DONE","support":["FCT-003","FCT-011","FCT-023","FCT-024"]}
ACT-003 | {"action":"requires methodological disclosure, public notices, quality control and a short blackout","actor":"French legislature and Commission des sondages","intent":"ELECTORAL_INFORMATION_INTEGRITY","status":"DONE","support":["FCT-003","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010"]}
ACT-004 | {"action":"uses polls as information about viability, closeness or likely outcome","actor":"Voters","intent":"INFORMATION_OR_STRATEGIC_DECISION","status":"DONE","support":["FCT-013","FCT-016","FCT-018","FCT-020","FCT-026"]}
ACT-005 | {"action":"tests causal and observational poll effects on attention, turnout, strategic choice and voting","actor":"Independent researchers","intent":"MEASURE_CAUSAL_EFFECTS","status":"DONE","support":["FCT-013","FCT-016","FCT-018","FCT-021","FCT-023","FCT-026","FCT-028","FCT-029","FCT-030"]}

SEARCH_ACTIVITY_V1:WEB:15|FETCH:15|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | MNEMO_UNAVAILABLE | MnemoLite | - | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | France law 77-808 electoral opinion polls definition representative sample electoral debate
QRY-002 | FETCH | FOUND | SRC-001 | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000522846/2026-05-22 | France law 77-808 electoral opinion polls definition representative sample electoral debate
QRY-003 | WEB | FOUND | - | - | France law polls article 2 commissioner buyer sample questions margins of error
QRY-004 | FETCH | FOUND | SRC-002 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032454564 | France law polls article 2 commissioner buyer sample questions margins of error
QRY-005 | WEB | FOUND | - | - | France law polls article 11 publication ban day before election
QRY-006 | FETCH | FOUND | SRC-003 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032454547/2026-03-02 | France law polls article 11 publication ban day before election
QRY-007 | WEB | FOUND | - | - | Commission des sondages notices article 3 methods sample nonresponse redressment public notice
QRY-008 | FETCH | FOUND | SRC-004 | https://www.commission-des-sondages.fr/notices/ | Commission des sondages notices article 3 methods sample nonresponse redressment public notice
QRY-009 | WEB | FOUND | - | - | Commission des sondages presidential election 2022 controls 120 polls quality publication requirements March 11 2022
QRY-010 | FETCH | FOUND | SRC-005 | https://www.commission-des-sondages.fr/hist/communiques/communique-sondages-elections-presidentielles-11-mars-2022.htm | Commission des sondages presidential election 2022 controls 120 polls quality publication requirements March 11 2022
QRY-011 | WEB | FOUND | - | - | Exit polls turnout bandwagon voting natural experiment France 2005 overseas territories
QRY-012 | FETCH | FOUND | SRC-006 | https://www.sciencedirect.com/science/article/abs/pii/S0014292115000483 | Exit polls turnout bandwagon voting natural experiment France 2005 overseas territories
QRY-013 | WEB | FOUND | - | - | Causal effect polls turnout intention local randomization regression discontinuity 2021
QRY-014 | FETCH | FOUND | SRC-007 | https://www.cambridge.org/core/journals/political-analysis/article/abs/causal-effect-of-polls-on-turnout-intention-a-local-randomization-regression-discontinuity-approach/A5FE30BF50090E36E5D46449C84BC8F2 | Causal effect polls turnout intention local randomization regression discontinuity 2021
QRY-015 | WEB | FOUND | - | - | Polls coalition signals strategic voting experimental investigation Meffert Gschwend
QRY-016 | FETCH | FOUND | SRC-008 | https://onlinelibrary.wiley.com/doi/full/10.1111/j.1475-6765.2010.01986.x | Polls coalition signals strategic voting experimental investigation Meffert Gschwend
QRY-017 | WEB | FOUND | - | - | Strategic voting role of polls embedded web survey margin of error 2015 Rich
QRY-018 | FETCH | FOUND | SRC-009 | https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/abs/strategic-voting-and-the-role-of-polls-evidence-from-an-embedded-web-survey/35D2C502A55AD4BFA8E1C77B5601D997 | Strategic voting role of polls embedded web survey margin of error 2015 Rich
QRY-019 | WEB | FOUND | - | - | Bandwagon effect online voting experiment real political organizations 7 percent votes
QRY-020 | FETCH | FOUND | SRC-010 | https://academic.oup.com/ijpor/article/33/2/412/5857291 | Bandwagon effect online voting experiment real political organizations 7 percent votes
QRY-021 | WEB | FOUND | - | - | Experimental analysis campaign polls electoral information seeking dominant frontrunner less deliberation
QRY-022 | FETCH | FOUND | SRC-011 | https://www.sciencedirect.com/science/article/abs/pii/S0261379415001614 | Experimental analysis campaign polls electoral information seeking dominant frontrunner less deliberation
QRY-023 | WEB | FOUND | - | - | Bandwagon or Titanic outcome expectations voting direct democracy 2026 Strijbis
QRY-024 | FETCH | FOUND | SRC-012 | https://www.sciencedirect.com/science/article/pii/S0261379426000387 | Bandwagon or Titanic outcome expectations voting direct democracy 2026 Strijbis
QRY-025 | WEB | FOUND | - | - | German federal election 2021 bandwagon polls social class voting intentions SPD limited evidence
QRY-026 | FETCH | FOUND | SRC-013 | https://link.springer.com/article/10.1007/s11615-022-00417-3 | German federal election 2021 bandwagon polls social class voting intentions SPD limited evidence
QRY-027 | WEB | FOUND | - | - | Power of Polls cross national experimental analysis ten experiments six countries 2021
QRY-028 | FETCH | FOUND | SRC-014 | https://www.cambridge.org/core/elements/abs/power-of-polls/D3CC77369A6659153BD13E1FE3054EBB | Power of Polls cross national experimental analysis ten experiments six countries 2021
QRY-029 | WEB | FOUND | - | - | Horse race game framed journalism effects turnout vote choice attitudes polls review 2019
QRY-030 | FETCH | FOUND | SRC-015 | https://academic.oup.com/edited-volume/28311/chapter-abstract/215019781 | Horse race game framed journalism effects turnout vote choice attitudes polls review 2019

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | LEGIFRANCE-LOI-77-808 | Légifrance — Loi n°77-808 relative à la publication et diffusion de certains sondages d’opinion | 2026-05-22 | 2026-09-09 | Articles 1-13; définition, obligations, contrôle et période électorale | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000522846/2026-05-22
SRC-002 | ◈ | fam:A | LEGIFRANCE-77-808-ART2 | Légifrance — Loi n°77-808, article 2 | 2016-04-27 | 2026-09-09 | Mentions obligatoires lors de la première publication/diffusion | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032454564
SRC-003 | ◈ | fam:A | LEGIFRANCE-77-808-ART11 | Légifrance — Loi n°77-808, article 11 | 2016-04-27 | 2026-09-09 | Interdiction de publication/diffusion/commentaire la veille et le jour du scrutin | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032454547/2026-03-02
SRC-004 | ◈ | fam:B | COMMISSION-SONDAGES-NOTICES | Commission des sondages — Notices et article 3 | 2026-09-09 | 2026-09-09 | Exigences de notice: objet, échantillon, interrogation, non-réponse, redressement; notices publiques | https://www.commission-des-sondages.fr/notices/
SRC-005 | ◈ | fam:B | COMMISSION-SONDAGES-COMMUNIQUE-2022-03-11 | Commission des sondages — Communiqué sur les sondages de l’élection présidentielle 2022 | 2022-03-11 | 2026-09-09 | Contrôle systématique; 120 sondages contrôlés depuis le 1er janvier; mentions obligatoires | https://www.commission-des-sondages.fr/hist/communiques/communique-sondages-elections-presidentielles-11-mars-2022.htm
SRC-006 | ◉ | fam:E | EER-2015-EXIT-POLLS | European Economic Review — Exit polls, turnout, and bandwagon voting: Evidence from a natural experiment | 2015-07-01 | 2026-09-09 | Abstract and design; France overseas reform; turnout and bandwagon estimates | https://www.sciencedirect.com/science/article/abs/pii/S0014292115000483
SRC-007 | ◉ | fam:C | POLITICAL-ANALYSIS-2021-POLLS-TURNOUT | Political Analysis — The Causal Effect of Polls on Turnout Intention | 2021-02-15 | 2026-09-09 | Abstract; natural experiment/local randomization; +5% turnout intention | https://www.cambridge.org/core/journals/political-analysis/article/abs/causal-effect-of-polls-on-turnout-intention-a-local-randomization-regression-discontinuity-approach/A5FE30BF50090E36E5D46449C84BC8F2
SRC-008 | ◉ | fam:C | EJPR-2011-MEFFERT-GSCHWEND | European Journal of Political Research — Polls, coalition signals and strategic voting | 2011-01-11 | 2026-09-09 | Abstract; embedded experiments in two real campaigns; strategic voting limits | https://onlinelibrary.wiley.com/doi/full/10.1111/j.1475-6765.2010.01986.x
SRC-009 | ◉ | fam:C | PS-2015-RICH-STRATEGIC-VOTING | PS: Political Science & Politics — Strategic Voting and the Role of Polls | 2015-04-02 | 2026-09-09 | Abstract; embedded survey experiment; margin-of-error information and strategic voting | https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/abs/strategic-voting-and-the-role-of-polls-evidence-from-an-embedded-web-survey/35D2C502A55AD4BFA8E1C77B5601D997
SRC-010 | ◉ | fam:D | IJPOR-2021-BANDWAGON-EXPERIMENT | International Journal of Public Opinion Research — Bandwagon Effect in an Online Voting Experiment With Real Political Organizations | 2020-06-15 | 2026-09-09 | Experiment; 1,113 participants; majority options +7% votes; real monetary consequences | https://academic.oup.com/ijpor/article/33/2/412/5857291
SRC-011 | ◉ | fam:E | ELECTORAL-STUDIES-2016-POLLS-INFO | Electoral Studies — An experimental analysis of the impact of campaign polls on electoral information seeking | 2016-01-01 | 2026-09-09 | Abstract; poll exposure, information seeking, candidate attention and indirect vote-choice effects | https://www.sciencedirect.com/science/article/abs/pii/S0261379415001614
SRC-012 | ◉ | fam:E | ELECTORAL-STUDIES-2026-STRIJBIS | Electoral Studies — Bandwagon or Titanic? How outcome expectations influence voting in direct democracy | 2026-06-01 | 2026-09-09 | Three survey experiments; negative Titanic effect, positive success expectation, no underdog effect | https://www.sciencedirect.com/science/article/pii/S0261379426000387
SRC-013 | ◉ | fam:E | PVS-2023-GERMAN-BANDWAGON | Politische Vierteljahresschrift — Jumping on the Bandwagon: Poll Effects in the 2021 German Federal Election | 2022-08-10 | 2026-09-09 | GLES rolling cross-section; SPD association; causal-direction limitation | https://link.springer.com/article/10.1007/s11615-022-00417-3
SRC-014 | ◉ | fam:C | CAMBRIDGE-ELEMENTS-2021-POWER-POLLS | Cambridge Elements — The Power of Polls? A Cross-National Experimental Analysis | 2021-09-14 | 2026-09-09 | Summary; randomized poll availability, 10 experiments, six countries | https://www.cambridge.org/core/elements/abs/power-of-polls/D3CC77369A6659153BD13E1FE3054EBB
SRC-015 | ◉ | fam:D | OXFORD-HANDBOOK-2019-HORSE-RACE | Oxford Handbook of Electoral Persuasion — Horse-Race and Game-Framed Journalism’s Effects | 2019-05-09 | 2026-09-09 | Review chapter abstract; poll/horse-race effects on turnout, vote choice and attitudes | https://academic.oup.com/edited-volume/28311/chapter-abstract/215019781

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000522846/2026-05-22 | A | 2016-04-27 | Legal definition of electoral poll | French law defines a poll as a statistical survey intended to provide, at a given date, a quantitative indication of opinions, wishes, attitudes or behaviours from a sample and requires the sample to be representative of the population concerned. | -
FCT-002 | FACT | ✧ | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000522846/2026-05-22 | A | 2016-04-27 | Electoral-debate scope | The French polling law covers polls made public in France on subjects directly or indirectly related to electoral debate and treats vote simulations derived from such polls as polls for the law. | -
FCT-003 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032454564 | A | 2016-04-27 | Commissioner and buyer disclosure | At first publication or diffusion, French law requires disclosure of the polling organization and the name and capacity of the commissioner and, when different, the buyer. | -
FCT-004 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032454564 | A | 2016-04-27 | Sample dates and full questions disclosure | The first publication must state the number interviewed, fieldwork dates and the full wording of questions on electoral-debate subjects. | -
FCT-005 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032454564 | A | 2016-04-27 | Margins of error and notice right | The first publication must state that polls have margins of error, publish applicable margins of error and indicate the public right to consult the statutory notice. | -
FCT-006 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032454547/2026-03-02 | A | 2016-04-27 | Pre-election publication blackout | For general elections and referendums, French law prohibits publication, diffusion or commentary of electoral polls on the day before and the day of the vote, with the specified national rule beginning Saturday at 00:00 for presidential, legislative, European elections and national referendums. | -
FCT-007 | FACT | ✧ | https://www.commission-des-sondages.fr/notices/ | B | 2016-04-27 | Notice methodology disclosure | Before publication, the polling organization must file a notice specifying the poll object, sample selection and composition, interview conditions, nonresponse and, where applicable, the criteria used to weight or adjust raw results. | -
FCT-008 | FACT | ✧ | https://www.commission-des-sondages.fr/notices/ | B | 2016-04-27 | Notices are publicly accessible | The Commission des sondages makes statutory notices public online from publication or diffusion of the poll, creating an auditable record of methodology and redressment criteria. | -
FCT-009 | FACT | ✧ | https://www.commission-des-sondages.fr/hist/communiques/communique-sondages-elections-presidentielles-11-mars-2022.htm | B | 2022-03-11 | Systematic Commission control | The Commission des sondages stated that it systematically exercises control and publishes corrections when its review finds breach of the law, in particular a defect in poll quality. | -
FCT-010 | FACT | ✧ | https://www.commission-des-sondages.fr/hist/communiques/communique-sondages-elections-presidentielles-11-mars-2022.htm | B | 2022-03-11 | 120 polls controlled in early 2022 | By 11 March 2022, the Commission stated that it and its statistical experts had controlled 120 polls since 1 January 2022 in the presidential-election period. | -
FCT-011 | FACT | ✧ | https://www.commission-des-sondages.fr/hist/communiques/communique-sondages-elections-presidentielles-11-mars-2022.htm | B | 2022-03-11 | Presidential publication disclosure requirements | The Commission reiterated that first publication must disclose the organization, commissioner or buyer, sample size, dates, full questions, margins of error and access to the notice; for the 2022 presidential election, every publication or diffusion also had to indicate margins of error. | -
FCT-012 | EVIDENCE | ✧ | https://www.commission-des-sondages.fr/hist/communiques/communique-sondages-elections-presidentielles-11-mars-2022.htm | B | 2022-03-11 | Regulation is not proof of manipulation | The existence of disclosure, quality-control and blackout rules establishes that polls are treated as potentially consequential electoral information; it does not establish that any particular commissioner or polling organization intentionally manipulated an election. | -
FCT-013 | FACT | ✧ | https://www.sciencedirect.com/science/article/abs/pii/S0014292115000483 | E | 2015-07-01 | Exit-poll information reduced turnout | A natural experiment exploiting a French voting reform estimated that knowledge of mainland exit-poll information reduced turnout in affected overseas territories by about 11 percentage points. | -
FCT-014 | FACT | ✧ | https://www.sciencedirect.com/science/article/abs/pii/S0014292115000483 | E | 2015-07-01 | Exit-poll information increased bandwagon voting | The same natural experiment found that voters who still turned out after seeing exit-poll information were more likely to vote for the expected winner, providing evidence of a bandwagon response. | -
FCT-015 | FACT | ✧ | https://www.sciencedirect.com/science/article/abs/pii/S0014292115000483 | E | 2015-07-01 | French reform supplies counterfactual variation | The study used the 2005 reform that moved voting in western French overseas territories to before the mainland result, comparing the same constituencies with and without prior knowledge of mainland exit-poll information. | -
FCT-016 | FACT | ✧ | https://www.cambridge.org/core/journals/political-analysis/article/abs/causal-effect-of-polls-on-turnout-intention-a-local-randomization-regression-discontinuity-approach/A5FE30BF50090E36E5D46449C84BC8F2 | C | 2021-02-15 | Poll release increased turnout intention | A study combining a natural experiment with local-randomization regression discontinuity found that release of a poll increased turnout intention by about 5 percent. | -
FCT-017 | FACT | ✧ | https://www.cambridge.org/core/journals/political-analysis/article/abs/causal-effect-of-polls-on-turnout-intention-a-local-randomization-regression-discontinuity-approach/A5FE30BF50090E36E5D46449C84BC8F2 | C | 2021-02-15 | Turnout-intention effect survived falsification tests | The reported turnout-intention effect was robust to falsification tests on predetermined covariates, placebo outcomes and changes in the estimation window. | -
FCT-018 | FACT | ✧ | https://onlinelibrary.wiley.com/doi/full/10.1111/j.1475-6765.2010.01986.x | C | 2011-01-11 | Polls can support strategic voting | Experiments embedded in two real election campaigns causally manipulated polls and coalition signals and found evidence consistent with strategic voting. | -
FCT-019 | FACT | ✧ | https://onlinelibrary.wiley.com/doi/full/10.1111/j.1475-6765.2010.01986.x | C | 2011-01-11 | Strategic voting affected only a small subset | The same study concluded that the strategic-voting mechanism was supported only for a small number of voters and that most insincere vote decisions were explained by other factors. | -
FCT-020 | FACT | ✧ | https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/abs/strategic-voting-and-the-role-of-polls-evidence-from-an-embedded-web-survey/35D2C502A55AD4BFA8E1C77B5601D997 | C | 2015-04-02 | Margin-of-error information changed strategic voting | An embedded web-survey experiment found respondents told the margin of error in pre-election polls were more likely to vote strategically, while also emphasizing limits to strategic voting even in favorable settings. | -
FCT-021 | FACT | ✧ | https://academic.oup.com/ijpor/article/33/2/412/5857291 | D | 2020-06-15 | Experimental bandwagon effect on consequential votes | In an online experiment with politically active organizations and real monetary consequences, majority options received on average about 7 percent more votes after participants saw pre-election poll results. | -
FCT-022 | EVIDENCE | ✧ | https://academic.oup.com/ijpor/article/33/2/412/5857291 | D | 2020-06-15 | Bandwagon experiment external-validity limit | The bandwagon experiment used 1,113 U.S.-based online participants allocating money among political organizations rather than casting binding public-election ballots, so its causal internal evidence should not be generalized mechanically to France or actual elections. | -
FCT-023 | FACT | ✧ | https://www.sciencedirect.com/science/article/abs/pii/S0261379415001614 | E | 2016-01-01 | Dominant frontrunner reduced information seeking | An online experiment found that when polls signalled a dominant frontrunner, voters considered less campaign information before deciding. | -
FCT-024 | FACT | ✧ | https://www.sciencedirect.com/science/article/abs/pii/S0261379415001614 | E | 2016-01-01 | Trailing candidates received less attention | The same study found candidates trailing in polls received significantly less attention than leading candidates, conditional on the size of the polling gap. | -
FCT-025 | FACT | ✧ | https://www.sciencedirect.com/science/article/abs/pii/S0261379415001614 | E | 2016-01-01 | Poll-induced deliberation changes can affect vote choice | The study reported evidence that poll-induced changes in the decision process can indirectly influence vote choice. | -
FCT-026 | FACT | ✧ | https://www.sciencedirect.com/science/article/pii/S0261379426000387 | E | 2026-06-01 | Outcome expectations can depress support for expected losers | Three 2026 survey experiments on national initiatives found a negative bandwagon or Titanic effect: expectations that an initiative would fail reduced intention to vote for it. | -
FCT-027 | FACT | ✧ | https://www.sciencedirect.com/science/article/pii/S0261379426000387 | E | 2026-06-01 | Positive success expectation but no underdog effect | The same study found evidence that expecting an initiative to succeed could increase support, but found no evidence that voters shifted toward the losing option as an underdog response. | -
FCT-028 | EVIDENCE | ✧ | https://link.springer.com/article/10.1007/s11615-022-00417-3 | E | 2022-08-10 | German 2021 evidence was limited and party-specific | In the 2021 German federal election rolling cross-section, higher poll results were associated with higher SPD voting intention among voters exposed to polls, while comparable effects were not significant for the other major parties. | -
FCT-029 | EVIDENCE | ✧ | https://link.springer.com/article/10.1007/s11615-022-00417-3 | E | 2022-08-10 | German observational association did not close causality | The German study explicitly did not establish the assumed causal direction because voting intention was also associated with poll results published the following day, consistent with a common underlying swing in opinion. | -
FCT-030 | EVIDENCE | ✧ | https://academic.oup.com/edited-volume/28311/chapter-abstract/215019781 | D | 2019-05-09 | General horse-race electoral effects remain uncertain | A review of horse-race and game-framed journalism concluded that the impact of polls on political processes remains relatively understudied and poorly understood, requiring separate analysis of turnout, vote choice, participation and attitudes rather than assuming one uniform effect. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-002
FCT-004 | SRC-002
FCT-005 | SRC-002
FCT-006 | SRC-003
FCT-007 | SRC-004
FCT-008 | SRC-004
FCT-009 | SRC-005
FCT-010 | SRC-005
FCT-011 | SRC-005
FCT-012 | SRC-005
FCT-013 | SRC-006
FCT-014 | SRC-006
FCT-015 | SRC-006
FCT-016 | SRC-007
FCT-017 | SRC-007
FCT-018 | SRC-008
FCT-019 | SRC-008
FCT-020 | SRC-009
FCT-021 | SRC-010
FCT-022 | SRC-010
FCT-023 | SRC-011
FCT-024 | SRC-011
FCT-025 | SRC-011
FCT-026 | SRC-012
FCT-027 | SRC-012
FCT-028 | SRC-013
FCT-029 | SRC-013
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
FCT-012 | SKIP:NOT_ELIGIBLE
FCT-013 | ELIGIBLE:VERIFIE
FCT-014 | ELIGIBLE:VERIFIE
FCT-015 | ELIGIBLE:VERIFIE
FCT-016 | ELIGIBLE:VERIFIE
FCT-017 | ELIGIBLE:VERIFIE
FCT-018 | ELIGIBLE:VERIFIE
FCT-019 | ELIGIBLE:VERIFIE
FCT-020 | ELIGIBLE:VERIFIE
FCT-021 | ELIGIBLE:VERIFIE
FCT-022 | SKIP:NOT_ELIGIBLE
FCT-023 | ELIGIBLE:VERIFIE
FCT-024 | ELIGIBLE:VERIFIE
FCT-025 | ELIGIBLE:VERIFIE
FCT-026 | ELIGIBLE:VERIFIE
FCT-027 | ELIGIBLE:VERIFIE
FCT-028 | SKIP:NOT_ELIGIBLE
FCT-029 | SKIP:NOT_ELIGIBLE
FCT-030 | SKIP:NOT_ELIGIBLE

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
FCT-013 | WRITE | -
FCT-014 | WRITE | -
FCT-015 | WRITE | -
FCT-016 | WRITE | -
FCT-017 | WRITE | -
FCT-018 | WRITE | -
FCT-019 | WRITE | -
FCT-020 | WRITE | -
FCT-021 | WRITE | -
FCT-023 | WRITE | -
FCT-024 | WRITE | -
FCT-025 | WRITE | -
FCT-026 | WRITE | -
FCT-027 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:CAUSAL
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:FINALIZE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-09T02:58:54.464608+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":25,"eligible":25,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:25;attempted:0;success:0;failure:0;blocked:25} | WRITEBACK_EXECUTION_V1:[25 rows, see section]

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
FCT-013 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-014 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-015 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-016 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-017 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-018 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-019 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-020 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-021 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-023 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-024 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-025 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-026 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-027 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
