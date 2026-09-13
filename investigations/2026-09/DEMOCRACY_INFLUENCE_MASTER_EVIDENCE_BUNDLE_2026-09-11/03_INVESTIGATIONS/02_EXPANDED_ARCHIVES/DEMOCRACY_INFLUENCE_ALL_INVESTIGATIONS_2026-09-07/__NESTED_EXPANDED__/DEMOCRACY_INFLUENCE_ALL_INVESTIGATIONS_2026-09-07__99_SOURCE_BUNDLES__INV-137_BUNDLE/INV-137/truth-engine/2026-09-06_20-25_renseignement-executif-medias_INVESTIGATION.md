ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260906-2025-renseignement-executif-medias | PARENT_RUN_ID:NONE | AS_OF:2026-09-06
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/truth-engine/investigations/2026-09/2026-09-06_renseignement-executif-medias/2026-09-06_20-25_renseignement-executif-medias_INPUT.md | SUBJECT_SLUG:renseignement-executif-medias | SUBJECT_FP:sha256:f3d3108e73483bf7448d7d96fd9a36e7cd240f4d419944befcb470446bb8852f | INPUT_SHA256:sha256:f16c6d16732be42fc4b1c6ed007be384d283dc13f58161a4f966140218c43218
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/Europe 2015–2026 with US comparators; trace intelligence assessment -> political disclosure -> media framing -> policy/public response -> later validation/correction; preserve confidence and source caveats.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "truth_engine_investigation"
artifact_id: "INV-137"
run_id: "20260906-2025-renseignement-executif-medias"
status: "final_candidate"
updated: "2026-09-06"
---

<!-- TRACE: source=INV-137_RUN_CARD; runtime=Truth_Engine_2.10.6_R3P1 -->
<!-- DECISION: assessment!=confidence!=political_disclosure!=media_framing!=effect -->

# INV-137 — Renseignement → exécutif → médias : quand l’évaluation devient récit public

## Verdict exécutif

Le mécanisme existe et il est parfois revendiqué. En 2022, les gouvernements américain et britannique ont délibérément utilisé du renseignement déclassifié pour préempter le récit russe sur l’Ukraine. GCHQ et l’IRSEM le décrivent explicitement comme une communication stratégique. Le fait important est que **ce mécanisme d’influence publique n’est pas, par nature, une manipulation** : le contrôle positif Ukraine montre que l’alerte centrale sur une invasion majeure était substantiellement correcte.

Mais la même chaîne peut perdre de l’information. L’objet probatoire n’est donc pas « le renseignement dit vrai/faux » ; c’est :

`évaluation → confiance → sélection/déclassification → briefing → cadrage médiatique → réaction → validation/correction`

À chaque passage, il faut conserver ce qui était connu, par qui, avec quel niveau de confiance et à quelle date.

## 1. Ukraine 2022 : contrôle positif, mais pas chèque en blanc

Le Royaume-Uni a publiquement affirmé en janvier 2022 disposer d’informations selon lesquelles Moscou envisageait d’installer un pouvoir pro-russe à Kyiv et citait Yevhen Murayev comme candidat possible. Deux jours plus tard, Boris Johnson présentait ces informations comme du « renseignement déclassifié » et annonçait que Londres continuerait à rendre publiques des informations sur les cyberattaques, faux pavillons et opérations de désinformation russes.

Le mécanisme de communication est donc documenté par les acteurs eux-mêmes. GCHQ parlera ensuite d’une déclassification rapide et sans précédent visant à prendre de vitesse les actions russes. L’IRSEM décrit la même stratégie comme une décision politique permettant de soutenir la stratégie, de pré-réfuter des récits et de façonner l’interprétation initiale du conflit.

Le 24 février 2022, la Russie lance l’invasion à grande échelle. Le cœur de l’alerte occidentale était donc bien fondé. Ce point interdit une lecture paresseuse où tout renseignement rendu public serait assimilé à une opération de propagande.

En revanche, l’invasion ne valide pas rétroactivement chaque sous-claim. Le Foreign Office n’avait pas publié les éléments étayant le scénario Murayev ; Reuters signalait son démenti et l’absence de dossier probatoire public. RUSI indiquait en outre que cette information pouvait être d’origine américaine puis évaluée par les Britanniques. Le maillon `source analytique → présentateur politique` doit donc rester visible.

## 2. Russian bounties : un cas de dégradation de confiance

Le dossier des primes russes en Afghanistan montre le mouvement inverse. En juin 2020, des titres de presse présentent une opération du renseignement militaire russe visant des forces américaines et alliées comme un « finding » du renseignement. Le sujet devient immédiatement politiquement explosif.

Mais le dossier public se dégrade rapidement. Un suivi du Washington Post indique que des signalements antérieurs avaient été jugés fragmentaires et nécessitant confirmation. En juillet 2020, le général Mark Milley et le secrétaire à la Défense Mark Esper déclarent au Congrès que l’appareil militaire n’a pas corroboré le versement de primes ni une direction russe d’attaques contre les Américains. En avril 2021, l’administration Biden rend public le niveau réel de confiance : **faible à modéré** sur l’encouragement d’attaques incluant des incitations financières, avec une confiance plus élevée sur les contacts du GRU avec des réseaux criminels afghans.

Ce cas établit une chose précise : **la certitude publique apparente a dépassé la confiance finalement rendue publique**. Il ne prouve pas pour autant que la CIA ou des responsables anonymes ont sciemment fabriqué une opération afin d’influencer l’élection de 2020. L’intention de la fuite, l’identité des sources et un éventuel tasking politique restent non établis.

## 3. Nord Stream : renseignement anonyme, caveats visibles, corroboration partielle

En mars 2023, le New York Times rapporte un nouveau renseignement examiné par des responsables américains suggérant qu’un groupe pro-ukrainien a saboté Nord Stream. Le même article conserve plusieurs caveats matériels : aucune conclusion ferme, aucune preuve que Zelensky ou ses principaux collaborateurs aient ordonné l’opération, nature et solidité des renseignements non révélées, responsables divisés sur le poids à leur donner. Reuters reprend le lead en conservant l’absence de conclusion ferme et l’absence de preuve d’un commandement gouvernemental ukrainien.

En février 2024, le Danemark clôt sa propre enquête : sabotage délibéré, mais éléments insuffisants pour poursuivre pénalement et aucun suspect identifié. En août 2024, un élément nouveau renforce toutefois une partie de l’hypothèse de 2023 : la Pologne confirme avoir reçu un mandat d’arrêt européen allemand visant le plongeur ukrainien Volodymyr Z., suspecté d’avoir participé à l’opération.

Ce développement **renforce un maillon participant ukrainien**. Il ne ferme toujours pas le maillon `État ukrainien → tasking`.

## 4. Ce qui se perd entre renseignement et récit public

Les trois familles montrent quatre transformations possibles :

1. une évaluation correcte peut être utilisée volontairement comme outil d’influence publique ;
2. un sous-claim peut rester non démontré même lorsque le scénario général est validé ;
3. une information de faible confiance peut acquérir une apparence de certitude supérieure dans l’espace médiatique ;
4. une hypothèse initialement caveatée peut recevoir plus tard une corroboration partielle sans devenir une attribution complète.

Le niveau de confiance n’est donc pas une note de bas de page. Il fait partie du fait. De même, « selon des responsables du renseignement » n’est pas une source primaire accessible : c’est une relation de provenance opaque qui doit rester visible dans le graphe.

## 5. Manipulation ou participation normale de l’État ?

Le critère ne peut pas être « l’État cherche à influencer l’opinion », car la communication stratégique officielle le fait explicitement et parfois légitimement. Il faut tester autre chose : exactitude connue au moment de la communication, conservation des caveats, sélection trompeuse éventuelle, présentation d’une hypothèse comme certitude, corrections ultérieures, et surtout preuve d’une intention de tromper lorsque l’on emploie le terme manipulation.

Sur le corpus étudié, l’Ukraine 2022 relève d’une **influence stratégique publique largement fondée sur une alerte correcte**. Le dossier des primes russes documente une **sur-certitude publique par rapport au niveau de confiance ensuite révélé**, mais pas un plan de manipulation prouvé. Nord Stream documente un **briefing anonyme caveaté**, suivi d’une corroboration judiciaire partielle, sans commanditaire étatique établi.

## Conclusion technique

La frontière utile n’oppose pas « renseignement officiel » et « désinformation ». Elle oppose des chaînes probatoires plus ou moins fermées.

Une affirmation issue du renseignement doit être horodatée et conserver : `source accessible/non accessible`, `niveau de confiance`, `institution analytique`, `acteur politique qui décide de publier`, `formulation médiatique`, `corrections`, `validation ultérieure`.

Ce modèle sera directement réutilisable pour auditer la symétrie alliés/adversaires et l’économie institutionnelle de la contre-ingérence. En revanche, `CAU-001..002` restent ouverts : le corpus ne permet pas de calculer combien de soutien public, de sanctions, de décisions alliées ou de comportements électoraux ont été causés par ces divulgations plutôt que par les événements eux-mêmes.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:0|EDI_DECISIVE:9|SRC_COMPLETE:18/18

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **Nord_Stream:** Sep 2022 sabotage -> Mar 2023 anonymous intelligence lead -> Feb 2024 Denmark closes without suspect -> Aug 2024 German warrant for Ukrainian suspect
- **Russian_bounties:** mid-2019/2020 intelligence -> June 2020 press claims -> July 2020 non-corroboration -> April 2021 low-to-moderate confidence disclosure
- **Ukraine:** 2021 troop buildup -> Jan/Feb 2022 disclosures -> 24 Feb invasion -> later assessment of disclosure strategy
- **as_of:** 2026-09-06

### MANIPULATION_REPORT
- **assumptions:**
  - public disclosure can be legitimate or manipulative depending on evidence and intent
  - later validation can strengthen some edges and leave others open
  - different agencies can disagree in good faith
- **clusters:**
  - NONE
- **complexity:**
  - **band:** HIGH
  - **score:** 9
- **implicit:**
  - assessment != fact
  - confidence level is material
  - political disclosure != analytic consensus
  - headline != underlying caveats
  - core prediction true != every subclaim true
  - influence != manipulation
- **input_kind:** TOPIC
- **mission_mode:** INVESTIGATION
- **patterns:**
  - confidence laundering
  - anonymous-source authority
  - strategic prebuttal
  - political selection of intelligence
  - media caveat compression
  - retrospective overvalidation
- **priorities:**
  - primary government/intelligence statements
  - contemporaneous media framing
  - later corrections/confidence disclosures
  - case pairs with positive and negative controls
- **query_guidance:** preserve confidence labels and chronology; trace who knew/said what when; do not infer source intent or causal effect without evidence
- **rhetorical:**
  - NONE
- **speaker:** user/object question
- **symbol_stage:** FINAL
- **symbols:**
  - **M:** 5
  - **Κ:** 5
  - **Λ:** 5
  - **Ξ:** 5
  - **Σ:** 5
  - **Φ:** 5
  - **Ψ:** 5
  - **Ω:** 5
  - **κ:** 5
  - **ρ:** 5
  - **€:** 4
  - **↕:** 5
  - **⏰:** 5
  - **⚔:** 4
  - **⫸:** 5
- **threats:**
  - official_claim=proof
  - intelligence=certainty
  - later event validates all subclaims
  - anonymous source=intentional leak
  - media effect=policy effect
  - error=manipulation

### MODULE_EXECUTION
NONE

### SCOPING_REPORT
- **cases:**
  - Ukraine prebuttal 2021-22
  - Russian bounties 2020-21
  - Nord Stream 2023-24
- **chain:**
  - assessment/source
  - confidence
  - political selection/declassification
  - briefing/disclosure
  - media framing
  - public/policy uptake
  - later validation/correction
- **exclusions:**
  - classified claims with no public trace beyond generic assertion
  - ordinary expert commentary not invoking intelligence authority
  - intentional manipulation inferred from error alone
- **object:** Intelligence assessment -> executive/public disclosure -> media framing as influence mechanism
- **scope:** France/Europe 2015-2026 with US comparators

### CREDO
- official intelligence != proof by status
- confidence labels are evidence
- strategic disclosure != manipulation by definition
- error != lie
- correct core prediction != all subclaims correct
- anonymous source != command chain
- media amplification != causal policy effect
- later correction must travel with earlier claim

### COGNITIVE_MAP
- **causal_boundary:** The scoped evidence does not identify a general counterfactual effect of disclosures on public opinion, allied policy, deterrence or elections.
- **core_model:** Public intelligence is both an evidentiary input and a potential influence instrument; reliability depends on preserving confidence, source opacity, political selection and later correction as separate edges.
- **rival_models:**
  - accurate warning/public diplomacy
  - good-faith analytic error
  - inter-agency divergence
  - selective political disclosure
  - media caveat compression
  - intentional manipulation
- **serial_edges:**
  - assessment
  - confidence
  - selection/declassification
  - briefing
  - media framing
  - uptake
  - validation/correction

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** Ukraine 2022 shows public intelligence can be substantially accurate and strategically useful
  - **resolution:** classify disclosure intent separately from truth value and effect
  - **thesis:** intelligence disclosure is propaganda
- **item 2:**
  - **antithesis:** bounties and Nord Stream show confidence and attribution can remain partial
  - **resolution:** preserve edge-level confidence and chronology
  - **thesis:** official/intelligence attribution is enough
- **item 3:**
  - **antithesis:** Ukraine invasion validated the core warning but not every puppet/false-flag subclaim
  - **resolution:** validate each subclaim independently
  - **thesis:** later validation proves the whole earlier story

### RESOURCE_FLOW_MAP
- **item 1:**
  - **case:** Ukraine 2022
  - **flow:** classified/all-source assessment -> political declassification -> public statement/briefing -> media/allied audience
  - **status:** DOCUMENTED_STRATEGIC_DISCLOSURE
  - **support:**
    - FCT-003
    - FCT-004
    - FCT-008
- **item 2:**
  - **case:** Russian bounties
  - **flow:** classified reporting -> anonymous media sourcing -> political controversy -> later confidence disclosure
  - **status:** DOCUMENTED_WITH_CONFIDENCE_DOWNGRADE
  - **support:**
    - FCT-010
    - FCT-011
    - FCT-012
    - FCT-013
    - FCT-014
- **item 3:**
  - **case:** Nord Stream
  - **flow:** classified intelligence -> anonymous officials -> media report -> later law-enforcement lead
  - **status:** CAVEATED_PARTIAL_ATTRIBUTION
  - **support:**
    - FCT-015
    - FCT-016
    - FCT-017
    - FCT-019
    - FCT-020

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** US/UK intelligence communities
  - **limits:**
    - full source material
    - counterfactual influence effect
  - **relation:** assessment/declassification/briefing
  - **support:**
    - FCT-003
    - FCT-004
    - FCT-008
  - **to:** US/UK executives and public
- **item 2:**
  - **from:** anonymous US intelligence/official sources
  - **limits:**
    - source intent
    - complete confidence metadata
  - **relation:** Russian-bounties and Nord Stream reporting
  - **support:**
    - FCT-010
    - FCT-015
  - **to:** US media/public debate
- **item 3:**
  - **from:** media framing
  - **limits:**
    - causal policy/electoral effect
  - **relation:** amplification and controversy
  - **support:**
    - FCT-010
    - FCT-014
    - FCT-017
  - **to:** political/public agenda

### IMPACT_MAP
- **downstream:** INV-144 can use the attribution/disclosure-economy model; INV-146 can compare ally/adversary standards; future media-analysis work can test caveat survival quantitatively.
- **measured_objects:**
  - public confidence labels
  - disclosure chronology
  - media wording
  - later corrections
  - partial judicial corroboration
  - declared strategic communication intent
- **not_established:**
  - general intent to manipulate by intelligence services
  - counterfactual public opinion shift
  - counterfactual sanctions/allied-policy shift
  - electoral effect of bounty reporting
  - Ukrainian government tasking in Nord Stream

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** specific puppet-regime subclaim lacked public evidentiary package and was denied
  - **issue:** Ukraine intelligence credibility
  - **pro:** core invasion warning was broadly correct
  - **resolution:** CORE_WARNING_VALIDATED_SUBCLAIMS_SEPARATE
- **item 2:**
  - **contra:** bounty payments/directed attacks uncorroborated; IC confidence low-to-moderate
  - **issue:** Russian bounty program
  - **pro:** GRU contacts with Afghan criminal networks and concern were acknowledged
  - **resolution:** PUBLIC_CERTAINTY_EXCEEDED_LATER_DISCLOSED_CONFIDENCE
- **item 3:**
  - **contra:** no firm 2023 conclusion; Denmark no suspect; no Ukrainian-government tasking proof
  - **issue:** Nord Stream attribution
  - **pro:** 2023 intel suggested pro-Ukrainian group; 2024 warrant named Ukrainian suspect
  - **resolution:** PARTICIPANT_HYPOTHESIS_STRENGTHENED_STATE_TASKING_OPEN

### VERIFICATION_REPORT
- **checks:**
  - positive control included
  - negative/downgrade control included
  - confidence labels preserved
  - source/political presenter separated
  - media framing separated from underlying assessment
  - later corrections retained
  - intent not inferred from error
  - causal effect kept open
- **status:** PASS_PENDING_EXTERNAL_GATE

### EDI_REPORT
- **corpus:**
  - **circularity:** Multiple Reuters items share one newsroom; RUSI analyses share one institution; bounties stories often derive from overlapping anonymous intelligence sources; Nord Stream 2023 coverage originates from a limited classified-intelligence pool.
  - **counters:** 4
  - **coverage:** 0.9
  - **direct_objects:** 8
  - **edi_star:** 0.83
  - **independence:** 0.79
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 7
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES
    - **freshness:** HISTORICAL_VALIDATED
    - **gap_type:** NONE
    - **independent_families:** 5
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** YES
    - **freshness:** HISTORICAL
    - **gap_type:** ATTRIBUTION
    - **independent_families:** 3
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** YES
    - **freshness:** HISTORICAL_CORRECTED
    - **gap_type:** NONE
    - **independent_families:** 5
  - **item 5:**
    - **claim_id:** CLM-005
    - **direct_object:** PARTIAL
    - **freshness:** HISTORICAL
    - **gap_type:** INTENT
    - **independent_families:** 3
  - **item 6:**
    - **claim_id:** CLM-006
    - **direct_object:** YES
    - **freshness:** CURRENT_TO_2024
    - **gap_type:** ATTRIBUTION
    - **independent_families:** 4
  - **item 7:**
    - **claim_id:** CLM-007
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 6
  - **item 8:**
    - **claim_id:** CLM-008
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 5
  - **item 9:**
    - **claim_id:** CLM-009
    - **direct_object:** PARTIAL
    - **freshness:** CURRENT
    - **gap_type:** CAUSALITY
    - **independent_families:** 4
- **diagnostic_not_truth:** true
- **dimensions:**
  - **geo:** 0.9
  - **lang:** 0.95
  - **owner:** 0.82
  - **persp:** 0.82
  - **strat:** 0.95
  - **temp:** 1.0
- **edi:**
  - **final:** 0.83
  - **flags:**
    - CLASSIFIED_SOURCE_OPACITY
    - ANONYMOUS_SOURCE_DEPENDENCE
    - RUSI_SAME_OWNER_MULTIPLE_ARTICLES
    - REUTERS_SAME_OWNER_MULTIPLE_ARTICLES
    - CAUSAL_EFFECT_UNRESOLVED
  - **penalties:** 0.07
  - **raw:** 0.9
- **source_counts:**
  - **primary:** 6
  - **secondary:** 12
  - **total:** 18

### RESPONSIBILITY_MAP
- **item 1:**
  - **claim:** Ukraine 2022 broad invasion warning
  - **owner:** US/UK intelligence + executives
  - **status:** SUBSTANTIALLY_VALIDATED
  - **support:**
    - FCT-005
    - FCT-006
- **item 2:**
  - **claim:** Murayev puppet-regime subclaim
  - **owner:** UK Foreign Office public statement
  - **status:** PARTIAL_PUBLIC_EVIDENCE
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-007
- **item 3:**
  - **claim:** Russian bounties
  - **owner:** anonymous intelligence sourcing + later US IC/Pentagon disclosures
  - **status:** LOW_TO_MODERATE_CONFIDENCE_NOT_FULLY_CORROBORATED
  - **support:**
    - FCT-010
    - FCT-011
    - FCT-012
    - FCT-013
- **item 4:**
  - **claim:** Nord Stream pro-Ukrainian group
  - **owner:** anonymous US intelligence 2023 + German law-enforcement lead 2024
  - **status:** PARTIAL_STRENGTHENED_AT_PARTICIPANT_LEVEL
  - **support:**
    - FCT-015
    - FCT-016
    - FCT-019
    - FCT-020

### NEXT_QUERIES
- **item 1:**
  - **query:** quantitative headline/body caveat retention for intelligence-based stories
  - **route:** DO
  - **trigger:** future media-method investigation
- **item 2:**
  - **query:** declassified/source-level evidence behind Murayev January 2022 claim
  - **route:** RECHECK
  - **trigger:** new official/declassified material
- **item 3:**
  - **query:** Russian bounties declassified IC assessment/source chain
  - **route:** RECHECK
  - **trigger:** new declassification
- **item 4:**
  - **query:** Nord Stream final German prosecutorial/judicial findings
  - **route:** RECHECK
  - **trigger:** new indictment/trial/judgment
- **item 5:**
  - **query:** ally/adversary disclosure vocabulary and evidence thresholds
  - **route:** MERGE
  - **trigger:** INV-146
- **item 6:**
  - **query:** counter-interference institutional incentives for public attribution/disclosure
  - **route:** MERGE
  - **trigger:** INV-144

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021,FCT-022,FCT-023 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021,FCT-022,FCT-023 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021,FCT-022,FCT-023 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-021,FCT-022,FCT-023 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018 | support:- | counter:- | results:FCT-010,FCT-011,FCT-012,FCT-013,FCT-014 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018 | support:- | counter:- | results:FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018 | support:- | counter:- | results:FCT-002,FCT-007,FCT-011,FCT-012,FCT-013,FCT-015,FCT-016,FCT-017 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018 | support:- | counter:- | results:FCT-003,FCT-004,FCT-008,FCT-021,FCT-022 | final:SATURATED | gap:NONE
AXS-007 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018 | support:- | counter:- | results:FCT-005,FCT-008,FCT-009,FCT-014,FCT-021 | final:SATURATED | gap:NONE
AXS-008 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021,FCT-022,FCT-023 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-002,QRY-003,QRY-008,QRY-009,QRY-011,QRY-014,SRC-002,SRC-003,SRC-008,SRC-009,SRC-011,SRC-014 | support:FCT-003,FCT-004,FCT-008,FCT-010,FCT-012,FCT-015 | counter:- | results:FCT-003,FCT-004,FCT-008,FCT-010,FCT-012,FCT-015 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-005,QRY-007,QRY-008,SRC-005,SRC-007,SRC-008 | support:FCT-005,FCT-006,FCT-023 | counter:- | results:FCT-005,FCT-006,FCT-023 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-001,QRY-004,QRY-005,QRY-006,SRC-001,SRC-004,SRC-005,SRC-006 | support:FCT-001,FCT-002,FCT-007 | counter:FCT-005 | results:FCT-001,FCT-002,FCT-007,FCT-005 | final:PARTIAL | gap:ATTRIBUTION
CLM-004 | attempts:QRY-009,QRY-010,QRY-011,QRY-012,SRC-009,SRC-010,SRC-011,SRC-012 | support:FCT-010,FCT-011,FCT-012,FCT-013 | counter:FCT-010(original media framing) | results:FCT-010,FCT-011,FCT-012,FCT-013,FCT-010(original media framing) | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-013,SRC-013 | support:FCT-014 | counter:- | results:FCT-014 | final:PARTIAL | gap:INTENT
CLM-006 | attempts:QRY-014,QRY-015,QRY-016,QRY-017,SRC-014,SRC-015,SRC-016,SRC-017 | support:FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020 | counter:- | results:FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020 | final:PARTIAL | gap:ATTRIBUTION
CLM-007 | attempts:QRY-010,QRY-011,QRY-012,QRY-014,QRY-015,SRC-010,SRC-011,SRC-012,SRC-014,SRC-015 | support:FCT-011,FCT-012,FCT-013,FCT-015,FCT-016,FCT-017 | counter:- | results:FCT-011,FCT-012,FCT-013,FCT-015,FCT-016,FCT-017 | final:SUPPORTED | gap:NONE
CLM-008 | attempts:QRY-002,QRY-003,QRY-005,QRY-008,QRY-018,SRC-002,SRC-003,SRC-005,SRC-008,SRC-018 | support:FCT-003,FCT-004,FCT-005,FCT-008,FCT-021,FCT-022 | counter:- | results:FCT-003,FCT-004,FCT-005,FCT-008,FCT-021,FCT-022 | final:SUPPORTED | gap:NONE
CLM-009 | attempts:QRY-008,QRY-013,QRY-018,SRC-008,SRC-013,SRC-018 | support:FCT-008,FCT-009,FCT-014,FCT-021 | counter:- | results:FCT-008,FCT-009,FCT-014,FCT-021 | final:PARTIAL | gap:CAUSALITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-003 | CLM | PARTIAL | ATTRIBUTION | The scoped public record does not expose source material/tasking proving the Murayev-installation subclaim.
CLM-005 | CLM | PARTIAL | INTENT | No direct evidence of source intent, tasking or coordinated electoral manipulation was found in the scoped public record.
CLM-006 | CLM | PARTIAL | ATTRIBUTION | Ultimate commanditaire/state tasking remains unresolved in the scoped record.
CLM-009 | CLM | PARTIAL | CAUSALITY | No design isolates what policy/public outcomes would have occurred without the disclosure.
CAU-001 | CAU | UNRESOLVED | CAUSALITY | Disclosure effect on allied/public behavior is not isolated from observable troop movements, diplomacy, invasion itself and other communications.
CAU-002 | CAU | UNRESOLVED | CAUSALITY | No direct causal design links caveat compression to a specific decision/outcome.

SEMANTIC_COUNTS_V1:LED:2|CLM:9|AXS:8|CAU:2|CTRL:4|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018"],"evidence_excerpt":"trace incident/source assessment through executive/public communication and correction","kind":"HYPOTHESIS","lead":"The public-intelligence chain must be decomposed into assessment -> confidence -> political selection/declassification -> briefing -> media framing -> policy/public response -> later validation/correction; proof at one edge does not prove the next.","linked_ids":["AXS-001","AXS-002","AXS-003","AXS-004","AXS-005","AXS-006","AXS-007","AXS-008","CLM-001","CLM-002","CLM-003","CLM-004","CLM-005","CLM-006","CLM-007","CLM-008","CLM-009"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021","FCT-022","FCT-023"],"routes":["OBJECT_INVESTIGATION","MECHANISMS","COUNTER_HYPOTHESES"],"source_id":"INV-137_RUN_CARD","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018"],"evidence_excerpt":"distinguish protection of sources, probabilistic assessment, strategic leak and manipulation demonstrated","kind":"METHOD_CONSTRAINT","lead":"Official intelligence disclosure, anonymous briefing, media wording and later correction are separate evidence classes; low/moderate/high confidence must not be normalized into binary truth.","linked_ids":["CLM-001","CLM-002","CLM-003","CLM-004","CLM-005","CLM-006","CLM-007","CLM-008","CLM-009","CTRL-001","CTRL-002","CTRL-003","CTRL-004"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021","FCT-022","FCT-023"],"routes":["COUNTER_HYPOTHESES","RULES_CONTROLS"],"source_id":"INV-137_RUN_CARD","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Public intelligence is a serial evidentiary and communication chain: assessment/raw reporting -> analytic confidence -> political selection/declassification -> briefing -> media framing -> public/policy response -> later validation or correction; one edge does not inherit certainty from another.","claimant":"INV-137 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-003","FCT-004","FCT-008","FCT-010","FCT-012","FCT-015"]}
CLM-002 | {"claim":"The core Western warning that Russia was preparing a major invasion of Ukraine was strongly validated by the February 24, 2022 invasion; this is a positive control showing that strategic intelligence disclosure can be substantially accurate.","claimant":"INV-137 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-005","FCT-006","FCT-023"]}
CLM-003 | {"claim":"Validation of the invasion warning does not automatically validate every disclosed subclaim: the January 2022 public claim that Russia was considering Yevhen Murayev for a puppet government had no public evidentiary package, was denied, and was not independently closed by the scoped record.","claimant":"INV-137 synthesis","counter":"FCT-005","gap":"The scoped public record does not expose source material/tasking proving the Murayev-installation subclaim.","gap_type":"ATTRIBUTION","materiality":"HIGH","status":"PARTIAL","support":["FCT-001","FCT-002","FCT-007"]}
CLM-004 | {"claim":"In the 2020 Russian-bounties case, early media framing expressed greater apparent certainty than the later public record supported: contemporaneous officials described intelligence as sketchy/unconfirmed, the military could not corroborate payments/directed attacks, and the 2021 IC judgment was disclosed as low-to-moderate confidence.","claimant":"INV-137 synthesis","counter":"FCT-010(original media framing)","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-010","FCT-011","FCT-012","FCT-013"]}
CLM-005 | {"claim":"The bounty reporting generated material political controversy and demands for action, but the scoped evidence does not establish that intelligence officials intentionally leaked or stripped caveats in order to manipulate the 2020 election or policy.","claimant":"INV-137 synthesis","counter":"NONE_FOUND","gap":"No direct evidence of source intent, tasking or coordinated electoral manipulation was found in the scoped public record.","gap_type":"INTENT","materiality":"HIGH","status":"PARTIAL","support":["FCT-014"]}
CLM-006 | {"claim":"The March 2023 Nord Stream intelligence leak was publicly caveated: a pro-Ukrainian group was suggested but there were no firm conclusions and no evidence of Ukrainian government direction; a 2024 German arrest warrant for a Ukrainian suspect partially strengthened the participant-level hypothesis without closing state tasking.","claimant":"INV-137 synthesis","counter":"NONE_FOUND","gap":"Ultimate commanditaire/state tasking remains unresolved in the scoped record.","gap_type":"ATTRIBUTION","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020"]}
CLM-007 | {"claim":"Confidence labels and caveats are part of the evidence, not editorial decoration. A defensible public account must preserve distinctions such as low/moderate confidence, anonymous-source opacity, no-firm-conclusion and no-government-evidence rather than collapsing them into a binary attribution.","claimant":"INV-137 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-011","FCT-012","FCT-013","FCT-015","FCT-016","FCT-017"]}
CLM-008 | {"claim":"Governments can deliberately use intelligence disclosure as an influence/public-diplomacy instrument while remaining factually accurate; intentional influence is therefore not equivalent to manipulation. The 2022 Ukraine prebuttal is a documented example of strategic communication whose core warning proved accurate.","claimant":"INV-137 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-003","FCT-004","FCT-005","FCT-008","FCT-021","FCT-022"]}
CLM-009 | {"claim":"The general causal effect of public intelligence disclosures on allied policy, public opinion, deterrence or electoral outcomes is not identified by the scoped evidence; contemporaneous influence and agenda effects are observable, but counterfactual impact remains unresolved.","claimant":"INV-137 synthesis","counter":"NONE_FOUND","gap":"No design isolates what policy/public outcomes would have occurred without the disclosure.","gap_type":"CAUSALITY","materiality":"HIGH","status":"PARTIAL","support":["FCT-008","FCT-009","FCT-014","FCT-021"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018"],"axis":"CHAIN_MODEL","links":["CLM-001"],"question":"Which edges transform intelligence assessment into public/political belief?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021","FCT-022","FCT-023"],"sought_objects":["CHAIN_MODEL"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018"],"axis":"UKRAINE_POSITIVE_CONTROL","links":["CLM-002","CLM-003"],"question":"Did 2021-22 invasion intelligence prove broadly accurate, and which subclaims remained unverified?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-021","FCT-022","FCT-023"],"sought_objects":["UKRAINE_WARNING"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018"],"axis":"BOUNTIES_DOWNGRADE","links":["CLM-004","CLM-005"],"question":"Did media/political certainty exceed later disclosed confidence in the Russian-bounties case?","result_ids":["FCT-010","FCT-011","FCT-012","FCT-013","FCT-014"],"sought_objects":["BOUNTY_CONFIDENCE"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018"],"axis":"NORDSTREAM_ANONYMOUS_INTEL","links":["CLM-006"],"question":"How far did anonymous intelligence in 2023 close attribution, and what did later judicial leads add?","result_ids":["FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020"],"sought_objects":["NORDSTREAM"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018"],"axis":"CAVEAT_SURVIVAL","links":["CLM-007"],"question":"Which caveats survived political and media transmission?","result_ids":["FCT-002","FCT-007","FCT-011","FCT-012","FCT-013","FCT-015","FCT-016","FCT-017"],"sought_objects":["CONFIDENCE","CAVEATS"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018"],"axis":"LEGITIMATE_INFLUENCE","links":["CLM-008"],"question":"Can intelligence disclosure be an intentional influence activity without being manipulation?","result_ids":["FCT-003","FCT-004","FCT-008","FCT-021","FCT-022"],"sought_objects":["PUBLIC_DIPLOMACY"],"status":"SATURATED"}
AXS-007 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018"],"axis":"CAUSAL_EFFECT","links":["CLM-009","CAU-001","CAU-002"],"question":"Can public disclosure be shown to cause support, sanctions, deterrence or electoral effects?","result_ids":["FCT-005","FCT-008","FCT-009","FCT-014","FCT-021"],"sought_objects":["CAUSAL_EFFECT"],"status":"SATURATED"}
AXS-008 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018"],"axis":"ALTERNATIVES","links":["CLM-001","CLM-007","CLM-008"],"question":"Test benign error, analytic divergence, strategic disclosure, selective leak, politicisation and intentional manipulation as distinct rival models.","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021","FCT-022","FCT-023"],"sought_objects":["RIVAL_MODELS"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"FCT-009(effect difficult to isolate)","gap":"Disclosure effect on allied/public behavior is not isolated from observable troop movements, diplomacy, invasion itself and other communications.","gap_type":"CAUSALITY","limit":"No counterfactual identification of support or policy change caused specifically by disclosure.","mechanism":"Strategic intelligence disclosure -> earlier/common threat perception -> allied/public coordination or support","status":"UNRESOLVED","support":["FCT-003","FCT-004","FCT-008","FCT-021"]}
CAU-002 | {"counter":"FCT-011;FCT-012;FCT-016;FCT-017","gap":"No direct causal design links caveat compression to a specific decision/outcome.","gap_type":"CAUSALITY","limit":"Media/political uptake is observable but source intent and counterfactual policy/electoral effect are not identified.","mechanism":"Anonymous/official intelligence briefing -> media certainty -> political action or electoral judgment","status":"UNRESOLVED","support":["FCT-010","FCT-014","FCT-015"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Positive control: the central 2021-22 warning of a major Russian invasion was substantially validated by the February 24 invasion; the method must not treat all public intelligence as propaganda.","status":"SUPPORTED","support":["FCT-005","FCT-006"]}
CTRL-002 | {"control":"Downgrade control: Russian-bounties reporting was later publicly qualified as low-to-moderate confidence and uncorroborated by senior military leadership, showing that later confidence disclosures can materially weaken earlier public certainty.","status":"SUPPORTED","support":["FCT-011","FCT-012","FCT-013"]}
CTRL-003 | {"control":"Partial-corroboration control: the 2024 German warrant strengthened the narrower pro-Ukrainian-participant hypothesis from the 2023 Nord Stream leak without establishing Ukrainian government tasking.","status":"SUPPORTED","support":["FCT-015","FCT-019","FCT-020"]}
CTRL-004 | {"control":"No-bad-faith shortcut: selective disclosure, anonymous sourcing or caveat loss can be documented without inferring intentional manipulation unless source/tasking evidence supports that intent.","status":"SUPPORTED","support":["FCT-007","FCT-008","FCT-015","FCT-016"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:18|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"EMPTY","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | subject-fp lookup | MNEMO_Q
SYS-003 | SYS | OK | web | INV-137 | WEB_RESEARCH
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.gov.uk/government/news/kremlin-plan-to-install-pro-russian-leadership-in-ukraine-exposed | UK intelligence puppet plan January 2022
QRY-002 | FETCH | FOUND | SRC-002 | https://www.gov.uk/government/speeches/pm-statement-on-ukraine-25-january-2022 | UK PM declassified intelligence January 25 2022
QRY-003 | FETCH | FOUND | SRC-003 | https://www.gchq.gov.uk/speech/director-gchq-global-security-amid-russia-invasion-of-ukraine | GCHQ intelligence declassification Ukraine March 2022
QRY-004 | FETCH | FOUND | SRC-004 | https://www.rusi.org/explore-our-research/publications/commentary/brief-or-not-brief-uk-intelligence-and-public-disclosure | RUSI UK intelligence public disclosure February 2022
QRY-005 | FETCH | FOUND | SRC-005 | https://www.rusi.org/explore-our-research/publications/commentary/ukraine-and-intelligence-prebuttal-quick-post-mortem | RUSI intelligence prebuttal post-mortem February 24 2022
QRY-006 | FETCH | FOUND | SRC-006 | https://www.euronews.com/2022/01/23/uk-ukraine-crisis-britain-russia-interview | Reuters Murayev puppet claim denied January 2022
QRY-007 | FETCH | FOUND | SRC-007 | https://www.euronews.com/2022/02/26/ukraine-crisis-intelligence | Reuters British intelligence invasion scoop February 2022
QRY-008 | FETCH | FOUND | SRC-008 | https://www.irsem.fr/publications/mediatisation-du-renseignement-et-guerre-en-ukraine | IRSEM mediatisation renseignement Ukraine 2022
QRY-009 | FETCH | FOUND | SRC-009 | https://www.washingtonpost.com/national-security/russian-operation-targeted-coalition-troops-in-afghanistan-intelligence-finds/2020/06/26/ac710092-b80f-11ea-9b0f-c797548c1154_story.html | Washington Post Russian bounties intelligence June 2020
QRY-010 | FETCH | FOUND | SRC-010 | https://www.washingtonpost.com/national-security/democrats-assail-administration-officials-for-not-forcing-trump-to-address-russian-operation-targeting-us-troops/2020/06/30/4744f408-badf-11ea-80b9-40ece9a701dc_story.html | Washington Post bounties sketchy confirmation June 2020
QRY-011 | FETCH | FOUND | SRC-011 | https://sg.news.yahoo.com/pentagon-tells-congress-russian-bounty-191255137.html | Reuters Milley bounties not corroborated July 2020
QRY-012 | FETCH | FOUND | SRC-012 | https://www.defense.gov/News/Transcripts/Transcript/Article/2576490/pentagon-press-secretary-john-f-kirby-holds-a-press-briefing/ | Pentagon low moderate confidence Russian bounties April 2021
QRY-013 | FETCH | FOUND | SRC-013 | https://www.theguardian.com/world/2021/apr/15/russian-bounty-us-troops-afghanistan | Guardian low moderate confidence bounties media political impact April 2021
QRY-014 | FETCH | FOUND | SRC-014 | https://archive.ph/HntrW | NYT anonymous intelligence pro-Ukrainian Nord Stream March 2023
QRY-015 | FETCH | FOUND | SRC-015 | https://www.investing.com/news/commodities-news/new-intelligence-points-to-proukraine-group-in-nord-stream-attack-nyt-3024134 | Reuters pro-Ukrainian Nord Stream intelligence March 2023
QRY-016 | FETCH | FOUND | SRC-016 | https://www.reuters.com/world/europe/germany-issues-arrest-warrant-ukrainian-diver-nord-stream-probe-media-report-2024-08-14/ | Reuters Germany arrest warrant Ukrainian Nord Stream August 2024
QRY-017 | FETCH | FOUND | SRC-017 | https://www.reuters.com/world/europe/denmark-ends-investigation-into-nord-stream-pipeline-blasts-2024-02-26/ | Reuters Denmark Nord Stream investigation closes February 2024
QRY-018 | FETCH | FOUND | SRC-018 | https://www.rusi.org/explore-our-research/publications/commentary/ukraine-model-intelligence-disclosure-may-not-be-new-normal | RUSI Ukraine model intelligence disclosure 2023

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:other:uk-fcdo | UK-FCDO-PUPPET-2022 | Kremlin plan to install pro-Russian leadership in Ukraine exposed | 2022-01-22 | 2026-09-06T18:30:00Z | UK statement: information indicates Russia considering Murayev; named alleged intelligence links | https://www.gov.uk/government/news/kremlin-plan-to-install-pro-russian-leadership-in-ukraine-exposed
SRC-002 | ◈ | fam:other:uk-pm | UK-PM-DECLASS-2022 | PM statement on Ukraine: 25 January 2022 | 2022-01-25 | 2026-09-06T18:30:00Z | PM says UK declassified compelling intelligence and would continue disclosures | https://www.gov.uk/government/speeches/pm-statement-on-ukraine-25-january-2022
SRC-003 | ◈ | fam:other:gchq | GCHQ-DECLASS-2022 | Director GCHQ speech on global security amid war in Ukraine | 2022-03-31 | 2026-09-06T18:30:00Z | GCHQ describes unprecedented intelligence release to get ahead of Russian actions | https://www.gchq.gov.uk/speech/director-gchq-global-security-amid-russia-invasion-of-ukraine
SRC-004 | ◉ | fam:other:rusi | RUSI-BRIEF-2022 | To Brief, Or Not to Brief: UK Intelligence and Public Disclosure | 2022-02-02 | 2026-09-06T18:30:00Z | Analysis of source/presentation risks; reports UK story may be US-sourced and UK-assessed | https://www.rusi.org/explore-our-research/publications/commentary/brief-or-not-brief-uk-intelligence-and-public-disclosure
SRC-005 | ◉ | fam:other:rusi | RUSI-PREBUTTAL-2022 | Ukraine and Intelligence Prebuttal: A Quick Post-Mortem | 2022-02-24 | 2026-09-06T18:30:00Z | Western invasion warnings largely proved correct; effect of prebuttal remains difficult to isolate | https://www.rusi.org/explore-our-research/publications/commentary/ukraine-and-intelligence-prebuttal-quick-post-mortem
SRC-006 | ◉ | fam:other:reuters | REUTERS-MURAYEV-2022 | Ukrainian politician mocks UK claims he could lead Kremlin puppet government | 2022-01-23 | 2026-09-06T18:30:00Z | Reuters: UK declined to provide evidence; Murayev denied claim | https://www.euronews.com/2022/01/23/uk-ukraine-crisis-britain-russia-interview
SRC-007 | ◉ | fam:other:reuters | REUTERS-UKRAINE-INTEL-2022 | Britain spy chief claims intelligence scoop on Putin invasion | 2022-02-26 | 2026-09-06T18:30:00Z | Reuters: months of US/UK warnings preceded invasion and were broadly vindicated | https://www.euronews.com/2022/02/26/ukraine-crisis-intelligence
SRC-008 | ◈ | fam:other:irsem | IRSEM-MEDIA-INTEL-2022 | Médiatisation du renseignement et guerre en Ukraine | 2022-03-01 | 2026-09-06T18:30:00Z | IRSEM: intelligence can be public communication supporting strategy; effects difficult to isolate; risk of politicisation | https://www.irsem.fr/publications/mediatisation-du-renseignement-et-guerre-en-ukraine
SRC-009 | ◉ | fam:other:washington-post | WAPO-BOUNTY-2020-A | Russian operation targeted coalition troops in Afghanistan, intelligence finds | 2020-06-27 | 2026-09-06T18:30:00Z | Original reporting framed bounty operation as intelligence finding based on anonymous officials | https://www.washingtonpost.com/national-security/russian-operation-targeted-coalition-troops-in-afghanistan-intelligence-finds/2020/06/26/ac710092-b80f-11ea-9b0f-c797548c1154_story.html
SRC-010 | ◉ | fam:other:washington-post | WAPO-BOUNTY-2020-B | Intelligence reports on Russian bounty operation first reached White House in early 2019 | 2020-06-30 | 2026-09-06T18:30:00Z | Follow-up says early reporting was considered sketchy and needed additional confirmation | https://www.washingtonpost.com/national-security/democrats-assail-administration-officials-for-not-forcing-trump-to-address-russian-operation-targeting-us-troops/2020/06/30/4744f408-badf-11ea-80b9-40ece9a701dc_story.html
SRC-011 | ◉ | fam:other:reuters | REUTERS-BOUNTY-JUL2020 | U.S. does not know if Russia directed Taliban attacks, Pentagon says | 2020-07-09 | 2026-09-06T18:30:00Z | Milley/Esper say military could not corroborate bounty intelligence or directed attacks | https://sg.news.yahoo.com/pentagon-tells-congress-russian-bounty-191255137.html
SRC-012 | ◈ | fam:other:us-dod | DOD-BOUNTY-2021 | Pentagon Press Secretary John F. Kirby Holds a Press Briefing | 2021-04-16 | 2026-09-06T18:30:00Z | Pentagon stresses low-to-moderate confidence and careful wording; no claim of confirmed payments | https://www.defense.gov/News/Transcripts/Transcript/Article/2576490/pentagon-press-secretary-john-f-kirby-holds-a-press-briefing/
SRC-013 | ◉ | fam:other:guardian | GUARDIAN-BOUNTY-2021 | US has low to moderate confidence in reports of Russian bounty on US troops | 2021-04-15 | 2026-09-06T18:30:00Z | Reports sparked political outrage; later IC confidence disclosed as low to moderate | https://www.theguardian.com/world/2021/apr/15/russian-bounty-us-troops-afghanistan
SRC-014 | ◉ | fam:other:nytimes | NYT-NORDSTREAM-2023 | Intelligence Suggests Pro-Ukrainian Group Sabotaged Pipelines, U.S. Officials Say | 2023-03-07 | 2026-09-06T18:30:00Z | Anonymous officials: intelligence suggests pro-Ukrainian group; no firm conclusions, no evidence Zelensky/top aides directed operation | https://archive.ph/HntrW
SRC-015 | ◉ | fam:other:reuters | REUTERS-NORDSTREAM-2023 | New intelligence points to pro-Ukraine group in Nord Stream attack - NYT | 2023-03-07 | 2026-09-06T18:30:00Z | Reuters preserves no-firm-conclusions and no-government-evidence caveats | https://www.investing.com/news/commodities-news/new-intelligence-points-to-proukraine-group-in-nord-stream-attack-nyt-3024134
SRC-016 | ◉ | fam:other:reuters | REUTERS-NORDSTREAM-2024-WARRANT | Poland received German request to arrest Nord Stream suspect but he left country | 2024-08-14 | 2026-09-06T18:30:00Z | German European arrest warrant for Ukrainian suspect; supports narrower Ukrainian-participant hypothesis, not state tasking | https://www.reuters.com/world/europe/germany-issues-arrest-warrant-ukrainian-diver-nord-stream-probe-media-report-2024-08-14/
SRC-017 | ◉ | fam:other:reuters | REUTERS-NORDSTREAM-2024-DK | Denmark ends probe into deliberate Nord Stream pipeline blasts | 2024-02-26 | 2026-09-06T18:30:00Z | Denmark finds deliberate sabotage but insufficient grounds for criminal case; no suspect identified | https://www.reuters.com/world/europe/denmark-ends-investigation-into-nord-stream-pipeline-blasts-2024-02-26/
SRC-018 | ◉ | fam:other:rusi | RUSI-UKRAINE-MODEL-2023 | The Ukraine Model for Intelligence Disclosure May Not be the New Normal | 2023-12-06 | 2026-09-06T18:30:00Z | Later assessment: public intelligence limited Russian obfuscation but model not universally transferable | https://www.rusi.org/explore-our-research/publications/commentary/ukraine-model-intelligence-disclosure-may-not-be-new-normal

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.gov.uk/government/news/kremlin-plan-to-install-pro-russian-leadership-in-ukraine-exposed | other:uk-fcdo | 2022-01-22 | UK puppet-regime disclosure | The UK Foreign Office publicly said it had information indicating Russia was considering Yevhen Murayev as a potential pro-Russian leader in Kyiv and listed former Ukrainian politicians it said had links to Russian intelligence. | -
FCT-002 | FACT | ✧ | https://www.euronews.com/2022/01/23/uk-ukraine-crisis-britain-russia-interview | other:reuters | 2022-01-23 | Murayev denial and evidence disclosure | Reuters reported Murayev denied the allegation and that the British foreign ministry declined to provide evidence supporting its public claim. | -
FCT-003 | FACT | ✧ | https://www.gov.uk/government/speeches/pm-statement-on-ukraine-25-january-2022 | other:uk-pm | 2022-01-25 | Political decision to declassify | Boris Johnson told Parliament the UK had declassified compelling intelligence about Russian intent and would continue disclosing cyber, false-flag and disinformation activity. | -
FCT-004 | FACT | ✧ | https://www.gchq.gov.uk/speech/director-gchq-global-security-amid-russia-invasion-of-ukraine | other:gchq | 2022-03-31 | GCHQ strategic disclosure doctrine | GCHQ director Jeremy Fleming described rapid declassification of intelligence to get ahead of Russian actions as unprecedented and explicitly welcomed intelligence being used publicly. | -
FCT-005 | FACT | ✧ | https://www.rusi.org/explore-our-research/publications/commentary/ukraine-and-intelligence-prebuttal-quick-post-mortem | other:rusi | 2022-02-24 | Broad Ukraine warning validation | RUSI assessed on the day of the invasion that Western warnings of a large Russian attack were largely proved correct, while warning that intelligence disclosure is not a substitute for strategy. | -
FCT-006 | FACT | ✧ | https://www.euronews.com/2022/02/26/ukraine-crisis-intelligence | other:reuters | 2022-02-26 | Invasion warning operational validation | Reuters reported that US and British services had warned for months of an invasion and that the February 24 invasion broadly vindicated the central warning. | -
FCT-007 | FACT | ✧ | https://www.rusi.org/explore-our-research/publications/commentary/brief-or-not-brief-uk-intelligence-and-public-disclosure | other:rusi | 2022-02-02 | Source and messenger separation | RUSI reported that the UK puppet-regime intelligence may have been US-sourced and assessed as accurate by UK officials, and stressed that mode of presentation and messenger affect public interpretation. | -
FCT-008 | FACT | ✧ | https://www.irsem.fr/publications/mediatisation-du-renseignement-et-guerre-en-ukraine | other:irsem | 2022-03-01 | Intelligence as public communication | IRSEM described the 2022 disclosure wave as a political decision using intelligence as public communication to support strategy and shape the initial narrative. | -
FCT-009 | FACT | ✧ | https://www.irsem.fr/publications/mediatisation-du-renseignement-et-guerre-en-ukraine | other:irsem | 2022-03-01 | Limits on measuring communication effect | IRSEM stated that the effectiveness of intelligence communication is difficult to isolate and identify tangibly and warned of risks of politicisation or manipulation when interpretations are erroneous. | -
FCT-010 | FACT | ✧ | https://www.washingtonpost.com/national-security/russian-operation-targeted-coalition-troops-in-afghanistan-intelligence-finds/2020/06/26/ac710092-b80f-11ea-9b0f-c797548c1154_story.html | other:washington-post | 2020-06-27 | Bounties original media certainty | The Washington Post headline and lead presented a Russian military intelligence bounty operation against coalition troops as an intelligence finding, based on anonymous officials. | -
FCT-011 | FACT | ✧ | https://www.washingtonpost.com/national-security/democrats-assail-administration-officials-for-not-forcing-trump-to-address-russian-operation-targeting-us-troops/2020/06/30/4744f408-badf-11ea-80b9-40ece9a701dc_story.html | other:washington-post | 2020-06-30 | Bounties internal uncertainty | A Washington Post follow-up reported that earlier White House intelligence reporting on the alleged bounty program had been considered sketchy and in need of additional confirmation. | -
FCT-012 | FACT | ✧ | https://sg.news.yahoo.com/pentagon-tells-congress-russian-bounty-191255137.html | other:reuters | 2020-07-09 | Bounties lack of military corroboration | Reuters reported General Mark Milley and Defense Secretary Mark Esper told Congress that the US military could not corroborate the bounty intelligence or confirm Russia directed attacks on US personnel. | -
FCT-013 | FACT | ✧ | https://www.defense.gov/News/Transcripts/Transcript/Article/2576490/pentagon-press-secretary-john-f-kirby-holds-a-press-briefing/ | other:us-dod | 2021-04-16 | Bounties later confidence level | The Pentagon publicly characterized the relevant intelligence-community judgment as low-to-moderate confidence and emphasized the need for careful wording because the allegation was serious. | -
FCT-014 | FACT | ✧ | https://www.theguardian.com/world/2021/apr/15/russian-bounty-us-troops-afghanistan | other:guardian | 2021-04-15 | Bounties political amplification | The Guardian reported that the 2020 press stories triggered political outrage and demands to confront Russia; the 2021 disclosure stated only low-to-moderate confidence in the bounty reporting. | -
FCT-015 | FACT | ✧ | https://archive.ph/HntrW | other:nytimes | 2023-03-07 | Nord Stream anonymous intelligence claim | The New York Times reported anonymous US officials saying new intelligence suggested a pro-Ukrainian group conducted the Nord Stream sabotage, while explicitly stating there were no firm conclusions and no evidence Zelensky or top aides directed it. | -
FCT-016 | FACT | ✧ | https://archive.ph/HntrW | other:nytimes | 2023-03-07 | Nord Stream source opacity and divisions | The same report said officials would not disclose the nature or strength of the intelligence, officials were divided on how much weight to give it, and major gaps remained. | -
FCT-017 | FACT | ✧ | https://www.investing.com/news/commodities-news/new-intelligence-points-to-proukraine-group-in-nord-stream-attack-nyt-3024134 | other:reuters | 2023-03-07 | Nord Stream caveats preserved in wire copy | Reuters repeated the pro-Ukrainian-group lead while preserving the absence of firm conclusions and absence of evidence of Ukrainian government involvement. | -
FCT-018 | FACT | ✧ | https://www.reuters.com/world/europe/denmark-ends-investigation-into-nord-stream-pipeline-blasts-2024-02-26/ | other:reuters | 2024-02-26 | Nord Stream deliberate sabotage without attribution | Danish authorities concluded the pipeline blasts were deliberate sabotage but said evidence was insufficient to pursue a criminal case and identified no suspect. | -
FCT-019 | FACT | ✧ | https://www.reuters.com/world/europe/germany-issues-arrest-warrant-ukrainian-diver-nord-stream-probe-media-report-2024-08-14/ | other:reuters | 2024-08-14 | Nord Stream later judicial lead | Polish prosecutors confirmed receipt of a German European arrest warrant for Ukrainian diver Volodymyr Z.; Reuters reported German investigators believed he was part of the sabotage team. | -
FCT-020 | FACT | ✧ | https://www.reuters.com/world/europe/germany-issues-arrest-warrant-ukrainian-diver-nord-stream-probe-media-report-2024-08-14/ | other:reuters | 2024-08-14 | Nord Stream government-tasking gap | The German-warrant reporting identified suspected Ukrainian participants but did not establish that Zelensky or the Ukrainian government ordered the sabotage. | -
FCT-021 | FACT | ✧ | https://www.rusi.org/explore-our-research/publications/commentary/ukraine-model-intelligence-disclosure-may-not-be-new-normal | other:rusi | 2023-12-06 | Disclosure can constrain adversary narratives | RUSI later assessed that UK Defence Intelligence public updates played an important role in limiting Russian ability to obfuscate the invasion, while cautioning that the Ukraine disclosure model is not universally transferable. | -
FCT-022 | FACT | ✧ | https://www.gchq.gov.uk/speech/director-gchq-global-security-amid-russia-invasion-of-ukraine | other:gchq | 2022-03-31 | Public intelligence as influence instrument | GCHQ framed intelligence release as a means of ensuring that a preferred factual account was heard before adversary narratives, demonstrating that intelligence disclosure can be a deliberate influence instrument without thereby being deceptive. | -
FCT-023 | FACT | ✧ | https://www.irsem.fr/publications/mediatisation-du-renseignement-et-guerre-en-ukraine | other:irsem | 2022-03-01 | France had a different assessment before invasion | IRSEM reported that US services shared their invasion assessment with France while French services were initially more reserved about Russian intent, illustrating that intelligence communities can legitimately diverge before outcomes resolve uncertainty. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-006
FCT-003 | SRC-002
FCT-004 | SRC-003
FCT-005 | SRC-005
FCT-006 | SRC-007
FCT-007 | SRC-004
FCT-008 | SRC-008
FCT-009 | SRC-008
FCT-010 | SRC-009
FCT-011 | SRC-010
FCT-012 | SRC-011
FCT-013 | SRC-012
FCT-014 | SRC-013
FCT-015 | SRC-014
FCT-016 | SRC-014
FCT-017 | SRC-015
FCT-018 | SRC-017
FCT-019 | SRC-016
FCT-020 | SRC-016
FCT-021 | SRC-018
FCT-022 | SRC-003
FCT-023 | SRC-008

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

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 LEADS | NEXT_ACTION:7 SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 SCOPE | NEXT_ACTION:9 SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 SEARCH | NEXT_ACTION:10 FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10 FACTS | NEXT_ACTION:11 CAUSAL_GAP
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 CAUSAL_GAP | NEXT_ACTION:13 VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 VERIFY | NEXT_ACTION:17 INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:18 FINALIZATION

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-06T19:28:07.894077+00:00","fact_mem":{},"mnemo_row":"BLOCKED:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":23,"eligible":23,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:BLOCKED:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:23;attempted:0;success:0;failure:0;blocked:23} | WRITEBACK_EXECUTION_V1:[23 rows, see section]

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
