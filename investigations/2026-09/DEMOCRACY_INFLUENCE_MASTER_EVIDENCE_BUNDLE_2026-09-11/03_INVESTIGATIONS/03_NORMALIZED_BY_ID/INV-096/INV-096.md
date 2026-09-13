ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260908-0807-political-microtargeting | PARENT_RUN_ID:NONE | AS_OF:2026-09-08
INPUT_KIND:RUN_CARD | MISSION_MODE:DEEPEN | INPUT_REF:PATH:/mnt/data/inv096-runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-08_political-microtargeting/2026-09-08_08-07_political-microtargeting_INPUT.md | SUBJECT_SLUG:political-microtargeting | SUBJECT_FP:sha256:47c2373fb9cd4c867946917ee6b9ffad66a12fd892d47fc4c6084213903e99b3 | INPUT_SHA256:sha256:a14783da48c0c5376d086a6c7a600872dd88589a305b122919e0860d6fa2f352
COMPLEXITY:8→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/UE 2016-2026; mechanism chain data -> segmentation -> targeting -> delivery -> exposure -> persuasion -> behavior/vote -> electoral effect. UK/US comparators only for isomorphic mechanism/effect designs. Explicit pre/post October 2025 EU discontinuity.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/FRAMING.md,clusters/NETWORK.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-096 — Microtargeting électoral et données personnelles en France/UE

## Résultat central

Le microtargeting politique est un mécanisme réel, mais son effet est beaucoup plus borné que son imaginaire public. Les régulateurs documentent l’usage de données et de techniques de ciblage par des partis et campagnes ; la publicité politique numérique française de 2022 fournit un terrain observable ; et les plateformes ont historiquement fourni des outils de ciblage et de transparence. Cela suffit à établir capacité et usage. Cela ne ferme pas la chaîne jusqu’au vote.

La frontière décisive est : **données != ciblage != delivery != exposition != persuasion != comportement/vote != résultat électoral**. Le corpus ferme bien les premières arêtes dans certains contextes, fournit des résultats expérimentaux mixtes sur la persuasion, et ne ferme pas de manière générale les deux dernières.

## Capacité et pratique

L’ICO décrit explicitement le microtargeting comme l’usage de méthodes d’analyse de données par des partis et groupes de campagne pour adresser des messages spécifiques à de petits groupes ou individus (FCT-030/FCT-031). La CNIL constate parallèlement l’importance croissante des données personnelles dans la prospection politique française (FCT-005). Ces éléments établissent l’existence opérationnelle du mécanisme, pas son efficacité.

La présidentielle française de 2022 offre un cas numérique observable : l’étude Sosnovik et al. analyse un corpus de publicités politiques sur Meta (FCT-018/FCT-019). Mais une distribution démographique d’impressions ne permet pas, seule, de reconstituer les paramètres choisis par l’annonceur, car l’optimisation de delivery peut contribuer à cette distribution (FCT-020).

## Rupture de régime en octobre 2025

Il serait incorrect d’extrapoler directement l’écosystème 2022 à 2026. La CNIL indique que le règlement européen sur la transparence de la publicité politique s’applique depuis octobre 2025 et renforce consentement, collecte et transparence (FCT-001 à FCT-004). Meta a fermé les publicités politiques, électorales et sociales payantes dans l’UE à partir d’octobre 2025 tout en maintenant les contenus organiques (FCT-013/FCT-014). Google a lui aussi annoncé l’arrêt de la publicité politique dans l’UE avant l’entrée en vigueur du nouveau cadre (FCT-016/FCT-017).

Les municipales 2026 se déroulent donc dans un environnement différent. La CNIL recense 739 signalements et 81 plaintes, principalement autour de canaux directs de prospection (FCT-008 à FCT-010). Ces chiffres prouvent une activité de prospection et de contrôle ; ils ne sont ni un taux de microtargeting ni une mesure de fraude.

## Persuasion : effets hétérogènes

Les expériences rapportées par MIT/PNAS fournissent un contrôle positif : sélectionner un message selon un attribut de l’audience peut, dans certains contextes, améliorer substantiellement la persuasion par rapport au meilleur message unique (FCT-025). Mais l’ajout de plusieurs attributs n’apporte pas de gain supplémentaire et l’avantage varie selon les sujets et les designs (FCT-026/FCT-027).

Le comparateur Oxford 2024 va dans l’autre sens pour le microtargeting par LLM : les messages GPT-4 sont persuasifs en moyenne, mais le microciblage individuel n’est pas statistiquement supérieur aux messages non microciblés en agrégé (FCT-028/FCT-029). La conclusion est donc contextuelle : sophistication du profil != puissance persuasive générale.

## De la publicité au vote : chaîne non fermée

Le contrôle causal le plus massif du corpus est l’expérience de retrait de publicités politiques avant l’élection américaine de 2020 : 36 906 utilisateurs Facebook et 25 925 utilisateurs Instagram sont randomisés (FCT-021). La plupart des publicités présidentielles visaient les propres soutiens des partis (FCT-022), mais aucun effet détectable du retrait n’apparaît sur connaissance, polarisation, légitimité perçue, participation, faveur envers les candidats ou turnout (FCT-023).

Cette expérience ne teste pas un contraste pur microciblage versus message générique (FCT-024). Elle interdit néanmoins de convertir automatiquement l’existence d’un marché de publicité ciblée en effet électoral massif. La House of Lords souligne aussi la difficulté à mesurer un effet sur le vote (FCT-032/FCT-033).

## Qualification démocratique

Le microtargeting est une technique d’influence et de persuasion. Il peut devenir problématique lorsque les données sont obtenues ou réutilisées illicitement, lorsque le ciblage est opaque, lorsque des messages contradictoires sont distribués selon les segments ou lorsqu’un sponsor est dissimulé. Mais personnalisation != manipulation et usage de campagne != ingérence étrangère. La sanction CNIL liée à la campagne 2022 illustre cette gradation : un manquement d’information dans la prospection est établi (FCT-011/FCT-012), sans établir persuasion, fraude ou changement de vote.

## Plafond I0–I7

- I0 VERIFIED : acteurs, règles, plateformes et techniques identifiés.
- I1 VERIFIED : capacité de collecter/segmenter/cibler et infrastructure de diffusion établies.
- I2 VERIFIED : usage de techniques de ciblage/prospection et publicité politique numérique documenté.
- I3 PARTIAL : paramètres exacts choisis par l’annonceur pas toujours séparables du delivery algorithmique.
- I4 VERIFIED/PARTIAL case-specifically : exposition/delivery observable dans certains datasets/expériences.
- I5 PARTIAL : persuasion causale dans certains designs, absente ou non supérieure dans d’autres.
- I6 NOT_ESTABLISHED generally : changement de comportement ou de vote non généralisable.
- I7 NOT_ESTABLISHED : aucun effet causal général sur le résultat électoral établi.

## Résidu matériel

Un nouvel effort ne changerait le modèle que s’il apporte des exports de campagnes/prestataires montrant les paramètres réels de ciblage, des données séparant choix annonceur et optimisation plateforme, ou un design causal France/UE reliant assignation de ciblage, exposition réelle, persuasion, vote et résultat. Une recherche générique supplémentaire sur Cambridge Analytica ou la puissance supposée des données serait cumulative.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:6|SRC_COMPLETE:12/12

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-08
- **notes:**
  - France 2022 Meta political-ad ecosystem
  - RPP applies from 10 Oct 2025
  - Meta/Google paid political ad exits create discontinuity
  - Municipal 2026 CNIL data are first post-RPP French election controls
- **status:** CURRENT_THROUGH_2026
- **window:** 2016-2026

### MANIPULATION_REPORT
- **assumptions:**
  - microtargeting is inherently manipulative
  - delivery demographics reveal advertiser targeting
  - persuasion implies vote change
  - capability implies general effectiveness
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
  - first-party voter data
  - audience segmentation
  - platform ad delivery
  - transparency libraries
  - experimental persuasion
  - EU regulatory discontinuity
- **priorities:**
  - data source
  - target selector
  - delivery
  - exposure
  - persuasion
  - vote/outcome
- **query_guidance:** prefer regulators, platform policies, ad data and randomized experiments; preserve targeting/delivery and persuasion/vote boundaries.
- **rhetorical:**
  - **AUTH:** authority supplies adjudicated/administrative records but remains claim-bound
  - **BF:** selected cases are not a national base rate
  - **DEM:** German comparator is procedural, not prevalence evidence
  - **FAC:** separate fraud, error, accusation, detection and effect
  - **NUM:** all counts retain their denominator and case scope
- **speaker:**
  - **goal:** forensic decomposition of political microtargeting
  - **target:** data->message->delivery->effect chain
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
  - data=targeting
  - targeting=delivery
  - exposure=persuasion
  - persuasion=vote
  - capability=effect
  - pre2025=post2025

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - exact advertiser selectors in France
  - **input_ids:**
    - FCT-003
    - FCT-005
    - FCT-013
    - FCT-016
    - FCT-030
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no generalized foreign/state command chain established
  - **not_computable:**
    - unrecorded vendor/campaign settings
  - **operations_applied:**
    - mapped campaign/platform/regulator roles
    - separated data possession from targeting and delivery
  - **reason:** separate campaign data access, platform delivery authority and regulator constraints
  - **result_ids:**
    - CLM-001
    - CLM-005
    - CTRL-001
    - CTRL-002
  - **status:** DONE
  - **trigger:** ↕
- **item 2:**
  - **gaps:**
    - France/UE persuasion-to-vote design
  - **input_ids:**
    - FCT-021
    - FCT-023
    - FCT-025
    - FCT-028
    - FCT-032
  - **module:** clusters/FRAMING.md
  - **negative_results:**
    - no general mind-control or vote-change effect
  - **not_computable:**
    - counterfactual election outcome
  - **operations_applied:**
    - separated exposure, persuasion and vote
    - compared positive and negative experiments
  - **reason:** test persuasion claims without laundering capability into effect
  - **result_ids:**
    - CLM-003
    - CLM-004
    - CTRL-004
    - CTRL-005
    - CAU-001
  - **status:** DONE
  - **trigger:** Φ
- **item 3:**
  - **gaps:**
    - vendor/campaign transaction-level logs
  - **input_ids:**
    - FCT-018
    - FCT-019
    - FCT-020
    - FCT-030
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no general covert network established
  - **not_computable:**
    - private coordination without records
  - **operations_applied:**
    - mapped advertiser/platform/audience interfaces
    - kept platform optimization distinct from advertiser choice
  - **reason:** map campaign->platform->audience chain without inferring coordination beyond observed edges
  - **result_ids:**
    - CLM-002
    - CTRL-002
    - CTRL-003
  - **status:** DONE
  - **trigger:** 🌐

### SCOPING_REPORT
- **actors_institutions:**
  - CNIL
  - political parties/candidates
  - Meta
  - Google
  - ICO
  - research teams
- **domains:**
  - data protection
  - political advertising
  - campaign analytics
  - platform delivery
  - persuasion experiments
  - electoral behavior
- **evidence_limits:**
  - no exhaustive French campaign targeting logs
  - Ad Library does not fully expose advertiser selectors
  - platform exits after Oct 2025 break comparability
  - experimental persuasion does not equal election outcome
- **exclusions:**
  - prospection=microtargeting
  - targeting=delivery
  - personalization=manipulation
  - persuasion=vote change
  - foreign interference without sponsor/tasking evidence
- **geo:** France/UE; UK/US isomorphic comparators
- **lead_question:** Microtargeting électoral et données personnelles en France/UE
- **object_coverage:** STRONG_FOR_CAPABILITY_AND_REGULATION; MODERATE_FOR_DELIVERY_AND_PERSUASION; WEAK_FOR_VOTE_AND_OUTCOME
- **object_question:** Quand la chaîne data->targeting->delivery->exposure->persuasion->vote est-elle réellement documentée?
- **period:** 2016-2026

### CREDO
- data_collection != targeting
- targeting != delivery
- delivery != exposure
- exposure != persuasion
- persuasion != vote_change
- personalization != manipulation
- campaign_use != foreign_interference
- claimed_capability != demonstrated_effect

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - first-party voter data
  - audience segmentation
  - platform ad delivery
  - transparency libraries
  - experimental persuasion
  - EU regulatory discontinuity
- **priorities:**
  - data source
  - target selector
  - delivery
  - exposure
  - persuasion
  - vote/outcome
- **query_guidance:** prefer regulators, platform policy, public ad data and randomized experiments; preserve targeting/delivery and persuasion/vote boundaries.
- **speaker:**
  - **goal:** forensic decomposition of political microtargeting
  - **target:** data->message->delivery->effect chain
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **threats:**
  - capability=effect
  - delivery=targeting
  - personalization=manipulation
  - experimental attitude=vote
  - pre2025=post2025 EU

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** Les expériences montrent des effets hétérogènes; certains ciblages persuadent davantage, d’autres non.
  - **resolution:** Capacité et certains gains persuasifs sont réels; puissance générale et vote change ne le sont pas.
  - **thesis:** Le microtargeting permet de manipuler précisément les électeurs.
- **item 2:**
  - **antithesis:** Le delivery algorithmique peut modifier qui voit une publicité après paramétrage annonceur.
  - **resolution:** Exiger paramètres d’audience/exports ou randomisation avant d’attribuer la distribution au ciblage choisi.
  - **thesis:** Une distribution démographique différente prouve que l’annonceur a ciblé ce groupe.
- **item 3:**
  - **antithesis:** RPP applicable et sortie de Meta/Google de la publicité politique payante UE à partir d’octobre 2025.
  - **resolution:** Segmenter strictement avant/après octobre 2025 et distinguer publicité payante, organique et canaux directs.
  - **thesis:** France 2022 décrit directement France 2026.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **boundary:** data possession != targeting event
  - **from:** personal data
  - **support:**
    - FCT-003
    - FCT-005
    - FCT-030
  - **to:** target audience definition
  - **vehicle:** campaign analytics/segmentation
- **item 2:**
  - **boundary:** delivery distribution != exact advertiser-selected target
  - **from:** ad creative + audience definition
  - **support:**
    - FCT-018
    - FCT-019
    - FCT-022
  - **to:** observed impressions
  - **vehicle:** platform ad delivery
- **item 3:**
  - **boundary:** experimental persuasion != vote/outcome; negative RCT constrains general effect
  - **from:** message exposure
  - **support:**
    - FCT-025
    - FCT-028
  - **to:** attitude/behavior/vote
  - **vehicle:** persuasion

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** campaign/party
  - **limits:**
    - lawful campaigning != manipulation
  - **relation:** collect/use voter data -> segment/message
  - **support:**
    - FCT-005
    - FCT-030
  - **to:** potential voters
- **item 2:**
  - **from:** campaign advertiser
  - **limits:**
    - public delivery data may not reveal exact selectors
  - **relation:** audience parameters + creative
  - **support:**
    - FCT-015
    - FCT-017
    - FCT-019
  - **to:** platform delivery system
- **item 3:**
  - **from:** Meta/Google
  - **limits:**
    - post-Oct-2025 exits do not remove organic/direct channels
  - **relation:** paid-ad infrastructure and policy
  - **support:**
    - FCT-013
    - FCT-016
  - **to:** EU political advertisers
- **item 4:**
  - **from:** regulators
  - **limits:**
    - complaint != violation prevalence
  - **relation:** consent/transparency/enforcement
  - **support:**
    - FCT-001
    - FCT-003
    - FCT-004
    - FCT-008
    - FCT-011
  - **to:** political campaigns and processors

### IMPACT_MAP
- **actual_use:** VERIFIED
- **advertiser_targeting_parameters:** PARTIAL
- **behavior/vote:** NOT_ESTABLISHED generally
- **capacity:** VERIFIED
- **delivery/exposure:** VERIFIED/PARTIAL case-specifically
- **electoral_effect:** NOT_ESTABLISHED
- **persuasion:** PARTIAL/HETEROGENEOUS
- **post_2025_EU_paid_platform_channel:** MATERIALLY_REDUCED/ALTERED
- **support:**
  - FCT-018
  - FCT-021
  - FCT-023
  - FCT-025
  - FCT-028
  - FCT-033

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** multi-attribute targeting adds no benefit; Oxford reports no aggregate LLM microtargeting advantage
  - **issue:** targeting efficacy
  - **pro:** MIT/PNAS reports persuasive advantage from one-attribute targeting in some settings
  - **resolution:** PERSUASION PARTIAL/HETEROGENEOUS, not general
  - **support:**
    - FCT-025
    - FCT-026
    - FCT-027
    - FCT-028
- **item 2:**
  - **contra:** large 2020 removal RCT finds no detectable effects on listed political outcomes including turnout
  - **issue:** political ads and electoral behavior
  - **pro:** real campaigns target and deliver political ads at scale
  - **resolution:** OPERATION/EXPOSURE can be real while general behavioral effect remains NOT_ESTABLISHED
  - **support:**
    - FCT-018
    - FCT-021
    - FCT-022
    - FCT-023
- **item 3:**
  - **contra:** RPP plus Meta/Google paid-ad exits materially alter available channels
  - **issue:** continuity France 2022 to 2026
  - **pro:** data-driven political communication continues
  - **resolution:** POST-2025 regime must be modeled separately
  - **support:**
    - FCT-005
    - FCT-013
    - FCT-016

### VERIFICATION_REPORT
- **circular_families:**
  - CNIL pages treated as one regulator family; platform self-statements kept separate from independent experimental evidence
- **contradiction_ids:**
  - targeting-efficacy
  - ads-vs-behavior
  - pre-post-2025-eu
- **downgraded_ids:**
  - NONE
- **none_found_claims:**
  - general microtargeting mind-control effect
  - general changed-vote causal chain
  - general election-result effect
  - foreign interference from campaign targeting alone
- **remaining_gaps:**
  - French advertiser-selected targeting logs
  - person-level delivery/exposure linkage
  - persuasion-to-vote design
  - post-2025 non-Meta/Google channel denominator
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
- **sources_reopened:** 12
- **upgraded_ids:**
  - NONE
- **verdict:** READY_FOR_PRE_GATE

### EDI_REPORT
- **corpus:**
  - **circularity:** CNIL pages treated as one family; platform self-statements do not establish persuasion/effect
  - **coverage:** STRONG_FOR_CAPABILITY_REGULATION_AND_SELECTED_EFFECT_DESIGNS; WEAK_FOR_FRANCE_VOTE_OUTCOME
  - **independence:** REGULATORS+PLATFORMS+ACADEMIC+PARLIAMENTARY
  - **limits:**
    - no exhaustive French advertiser targeting logs
    - no person-level French exposure-to-vote linkage
    - platform exits after Oct 2025 break temporal comparability
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **gap_type:** NONE
    - **independent_families:** 3
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** BOUNDARY
    - **gap_type:** SCOPE
    - **independent_families:** 2
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** MIXED_EXPERIMENTS
    - **gap_type:** CAUSALITY
    - **independent_families:** 3
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** NEGATIVE_LARGE_RCT
    - **gap_type:** CAUSALITY
    - **independent_families:** 3
  - **item 5:**
    - **claim_id:** CLM-005
    - **direct_object:** REGIME_BREAK
    - **gap_type:** TEMPORAL
    - **independent_families:** 3
  - **item 6:**
    - **claim_id:** CLM-006
    - **direct_object:** QUALIFICATION_BOUNDARY
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 3
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** 9_PROVENANCE_FAMILIES
  - **perspective:** REGULATOR+PLATFORM+ACADEMIC+PARLIAMENTARY
  - **stratification:** DATA+TARGETING+DELIVERY+EXPOSURE+PERSUASION+VOTE
  - **temporal:** 2016-2026 with explicit Oct-2025 break
- **edi:**
  - **assessment:** STRONG_MECHANISM_DISCRIMINATION; DOWNSTREAM_VOTE_EFFECT_UNRESOLVED
  - **flags:**
    - REAL_OPERATIONAL_CAPACITY
    - TARGETING_DELIVERY_BOUNDARY
    - MIXED_PERSUASION_EVIDENCE
    - NEGATIVE_LARGE_RCT
    - POST_2025_REGIME_BREAK
- **source_counts:**
  - **primary:** 8
  - **provenance_families:** 9
  - **secondary:** 4
  - **tertiary:** 0
  - **total:** 12

### RESPONSIBILITY_MAP
- **boundary:** Targeting is an influence technique; manipulation/ingérence require additional deception, sponsor/tasking, illegality or effect evidence.
- **not_established:**
  - general covert manipulation architecture
  - foreign sponsor/tasking from targeting alone
  - general voter-behavior change
  - changed election outcome
  - advertiser-selected targeting inferred solely from demographic delivery
- **verified:**
  - campaigns/parties can use data analytics for targeting
  - platforms provide or provided delivery infrastructure
  - EU/CNIL impose explicit restrictions
  - Meta/Google chose to exit paid political ads in EU

### NEXT_QUERIES
- RECHECK campaign/vendor exports exposing actual French audience selectors and creative variants before Oct 2025
- RECHECK platform data separating advertiser targeting from optimization/delivery
- RECHECK France/UE randomized or quasi-experimental targeting->exposure->vote designs
- DEFER generic Cambridge-Analytica-style capability claims without effect data

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-007 | support:- | counter:- | results:FCT-018,FCT-019,FCT-020 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-008 | support:- | counter:- | results:FCT-021,FCT-022,FCT-023,FCT-024 | final:SATURATED | gap:NONE
LED-003 | attempts:QRY-001,QRY-005,QRY-006 | support:- | counter:- | results:FCT-001,FCT-003,FCT-004,FCT-013,FCT-016 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-001,QRY-002,QRY-004,QRY-011 | support:- | counter:- | results:FCT-003,FCT-004,FCT-005,FCT-011,FCT-030 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-005,QRY-006,QRY-007 | support:- | counter:- | results:FCT-015,FCT-017,FCT-018,FCT-019,FCT-020 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-007,QRY-008 | support:- | counter:- | results:FCT-018,FCT-019,FCT-021,FCT-022 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-009,QRY-010,QRY-012 | support:- | counter:- | results:FCT-025,FCT-026,FCT-027,FCT-028,FCT-029,FCT-032 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-008,QRY-012 | support:- | counter:- | results:FCT-021,FCT-023,FCT-024,FCT-033 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-001,QRY-005,QRY-006 | support:- | counter:- | results:FCT-001,FCT-003,FCT-004,FCT-013,FCT-014,FCT-016 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-002,QRY-007,QRY-011,SRC-002,SRC-007,SRC-011 | support:FCT-005,FCT-018,FCT-030 | counter:- | results:FCT-005,FCT-018,FCT-030 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-007,SRC-007 | support:- | counter:FCT-019,FCT-020 | results:FCT-019,FCT-020 | final:REFUTED | gap:SCOPE
CLM-003 | attempts:QRY-009,QRY-010,QRY-012,SRC-009,SRC-010,SRC-012 | support:FCT-025 | counter:FCT-026,FCT-027,FCT-028,FCT-029,FCT-032 | results:FCT-025,FCT-026,FCT-027,FCT-028,FCT-029,FCT-032 | final:PARTIAL | gap:CAUSALITY
CLM-004 | attempts:QRY-008,QRY-012,SRC-008,SRC-012 | support:- | counter:FCT-021,FCT-023,FCT-024,FCT-033 | results:FCT-021,FCT-023,FCT-024,FCT-033 | final:PARTIAL | gap:CAUSALITY
CLM-005 | attempts:QRY-001,QRY-005,QRY-006,SRC-001,SRC-005,SRC-006 | support:- | counter:FCT-001,FCT-013,FCT-014,FCT-016 | results:FCT-001,FCT-013,FCT-014,FCT-016 | final:REFUTED | gap:TEMPORAL
CLM-006 | attempts:QRY-001,QRY-004,QRY-011,SRC-001,SRC-004,SRC-011 | support:- | counter:FCT-003,FCT-011,FCT-030,FCT-031 | results:FCT-003,FCT-011,FCT-030,FCT-031 | final:REFUTED | gap:RESPONSIBILITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-002 | CLM | REFUTED | SCOPE | Optimization/delivery platform and advertiser selection are not separable from aggregate delivery distributions alone.
CLM-003 | CLM | PARTIAL | CAUSALITY | Effects heterogeneous by issue/design; multi-attribute and LLM microtargeting do not show general added benefit.
CLM-004 | CLM | PARTIAL | CAUSALITY | No general chain to vote; large removal RCT reports no detectable turnout/participation effect.
CLM-005 | CLM | REFUTED | TEMPORAL | RPP and platform exits create a structural discontinuity from October 2025.
CLM-006 | CLM | REFUTED | RESPONSIBILITY | Need sponsor/tasking, deception/coercion and effect evidence separately; ordinary campaigning can use targeting.
CAU-001 | CAU | GAP | CAUSALITY | No France/UE design in current corpus closes targeting assignment -> actual exposure -> persuasion -> vote -> changed electoral result.

SEMANTIC_COUNTS_V1:LED:3|CLM:6|AXS:6|CAU:1|CTRL:6|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-007"],"evidence_excerpt":"political ads and Ad Library are observable; delivery demographics do not uniquely identify advertiser-selected targeting.","kind":"MECHANISM_LEAD","lead":"La France 2022 montre une infrastructure réelle de publicité politique numérique et d’observation de sa diffusion, mais les données publiques ne reconstruisent pas nécessairement le ciblage choisi par l’annonceur.","linked_ids":["FCT-018","FCT-019","FCT-020"],"locator":"French 2022 Meta political ads","materiality":"DECISIVE","result_ids":["FCT-018","FCT-019","FCT-020"],"routes":["VERIFY","FRAMING"],"source_id":"SRC-007","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-008"],"evidence_excerpt":"36,906 Facebook + 25,925 Instagram; no detectable effects on listed political outcomes including turnout.","kind":"CAUSALITY_LEAD","lead":"Le grand RCT Meta 2020 fournit un contrôle causal négatif contre l’hypothèse d’un effet agrégé massif des publicités politiques sur le comportement électoral.","linked_ids":["FCT-021","FCT-022","FCT-023","FCT-024"],"locator":"randomized removal experiment","materiality":"DECISIVE","result_ids":["FCT-021","FCT-022","FCT-023","FCT-024"],"routes":["VERIFY","CAUSALITY"],"source_id":"SRC-008","status":"SATURATED"}
LED-003 | {"attempt_ids":["QRY-001","QRY-005","QRY-006"],"evidence_excerpt":"RPP since Oct 2025; consent/direct collection restrictions; Meta and Google stop EU political ads.","kind":"TEMPORAL_LEAD","lead":"Octobre 2025 est une rupture de régime en UE: le ciblage politique fondé sur données personnelles est fortement encadré et Meta/Google ferment leurs canaux de publicité politique payante dans l’UE.","linked_ids":["FCT-001","FCT-003","FCT-004","FCT-013","FCT-016"],"locator":"RPP + platform exits October 2025","materiality":"DECISIVE","result_ids":["FCT-001","FCT-003","FCT-004","FCT-013","FCT-016"],"routes":["VERIFY","POWER"],"source_id":"SRC-001","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Le microtargeting politique fondé sur données est une capacité et une pratique opérationnelle réelle, pas seulement une hypothèse technique.","claimant":"INV-096","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-005","FCT-018","FCT-030"]}
CLM-002 | {"claim":"Les données publiques de delivery permettent en général de déduire exactement le ciblage choisi par l’annonceur.","claimant":"HYPOTHESIS_TEST","counter":["FCT-019","FCT-020"],"gap":"Optimization/delivery platform and advertiser selection are not separable from aggregate delivery distributions alone.","gap_type":"SCOPE","materiality":"DECISIVE","status":"REFUTED","support":"NONE_FOUND"}
CLM-003 | {"claim":"Le microtargeting produit un avantage persuasif robuste et général par rapport au meilleur message non ciblé.","claimant":"HYPOTHESIS_TEST","counter":["FCT-026","FCT-027","FCT-028","FCT-029","FCT-032"],"gap":"Effects heterogeneous by issue/design; multi-attribute and LLM microtargeting do not show general added benefit.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-025"]}
CLM-004 | {"claim":"L’exposition à la publicité politique numérique change de façon générale le comportement électoral ou le turnout.","claimant":"HYPOTHESIS_TEST","counter":["FCT-021","FCT-023","FCT-024","FCT-033"],"gap":"No general chain to vote; large removal RCT reports no detectable turnout/participation effect.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":"NONE_FOUND"}
CLM-005 | {"claim":"Le marché UE 2026 est directement comparable à France 2022 pour la publicité politique payante sur Meta/Google.","claimant":"HYPOTHESIS_TEST","counter":["FCT-001","FCT-013","FCT-014","FCT-016"],"gap":"RPP and platform exits create a structural discontinuity from October 2025.","gap_type":"TEMPORAL","materiality":"IMPORTANT","status":"REFUTED","support":"NONE_FOUND"}
CLM-006 | {"claim":"L’usage de données, le ciblage ou la personnalisation suffisent à qualifier une manipulation ou une ingérence étrangère.","claimant":"HYPOTHESIS_TEST","counter":["FCT-003","FCT-011","FCT-030","FCT-031"],"gap":"Need sponsor/tasking, deception/coercion and effect evidence separately; ordinary campaigning can use targeting.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"REFUTED","support":"NONE_FOUND"}

### AXIS_REGISTRY_V1
AXS-001 | {"assessment":"USE/CAPACITY VERIFIED; lawful EU political-ad targeting materially narrowed since Oct 2025.","attempt_ids":["QRY-001","QRY-002","QRY-004","QRY-011"],"axis":"DATA_AND_PROFILING","links":["FCT-003","FCT-004","FCT-005","FCT-011","FCT-030"],"question":"Quelles données peuvent réellement alimenter un profil ou segment politique?","result_ids":["FCT-003","FCT-004","FCT-005","FCT-011","FCT-030"],"sought_objects":["mechanism","evidence","effect"],"status":"SATURATED"}
AXS-002 | {"assessment":"PARTIAL: infrastructure and delivery observable; advertiser-selected parameters not generally reconstructed.","attempt_ids":["QRY-005","QRY-006","QRY-007"],"axis":"TARGETING_VS_DELIVERY","links":["FCT-015","FCT-017","FCT-018","FCT-019","FCT-020"],"question":"Peut-on distinguer paramètres choisis par l’annonceur et delivery optimisé par la plateforme?","result_ids":["FCT-015","FCT-017","FCT-018","FCT-019","FCT-020"],"sought_objects":["mechanism","evidence","effect"],"status":"SATURATED"}
AXS-003 | {"assessment":"VERIFIED/PARTIAL case-specifically; public French data remains incomplete for full person-level exposure.","attempt_ids":["QRY-007","QRY-008"],"axis":"EXPOSURE","links":["FCT-018","FCT-019","FCT-021","FCT-022"],"question":"Quelle exposition réelle est mesurée plutôt que seulement une capacité de ciblage?","result_ids":["FCT-018","FCT-019","FCT-021","FCT-022"],"sought_objects":["mechanism","evidence","effect"],"status":"SATURATED"}
AXS-004 | {"assessment":"HETEROGENEOUS/PARTIAL: advantage in some experiments, absent in others; no general overpowering effect.","attempt_ids":["QRY-009","QRY-010","QRY-012"],"axis":"PERSUASION","links":["FCT-025","FCT-026","FCT-027","FCT-028","FCT-029","FCT-032"],"question":"Le ciblage accroît-il causalement la persuasion par rapport à un message générique?","result_ids":["FCT-025","FCT-026","FCT-027","FCT-028","FCT-029","FCT-032"],"sought_objects":["mechanism","evidence","effect"],"status":"SATURATED"}
AXS-005 | {"assessment":"NOT_ESTABLISHED generally; major RCT found no detectable turnout/participation/favourability effect from ad removal.","attempt_ids":["QRY-008","QRY-012"],"axis":"BEHAVIOR_AND_VOTE","links":["FCT-021","FCT-023","FCT-024","FCT-033"],"question":"La persuasion ou l’exposition se traduit-elle en participation, choix de vote ou turnout?","result_ids":["FCT-021","FCT-023","FCT-024","FCT-033"],"sought_objects":["mechanism","evidence","effect"],"status":"SATURATED"}
AXS-006 | {"assessment":"NO: major paid-platform channel discontinuity; organic/first-party/direct channels remain distinct.","attempt_ids":["QRY-001","QRY-005","QRY-006"],"axis":"EU_REGIME_CHANGE","links":["FCT-001","FCT-003","FCT-004","FCT-013","FCT-014","FCT-016"],"question":"Le mécanisme 2016-2024 est-il encore opératoire de la même façon en UE après octobre 2025?","result_ids":["FCT-001","FCT-003","FCT-004","FCT-013","FCT-014","FCT-016"],"sought_objects":["mechanism","evidence","effect"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":["FCT-020","FCT-023","FCT-024","FCT-026","FCT-029","FCT-033"],"gap":"No France/UE design in current corpus closes targeting assignment -> actual exposure -> persuasion -> vote -> changed electoral result.","gap_type":"CAUSALITY","limit":"Upstream capacity/use and some exposure/persuasion links are case-specific; downstream vote/outcome chain is not generally identified.","mechanism":"personal data -> segmentation/profiling -> advertiser targeting -> platform delivery -> individual exposure -> persuasion -> behavior/vote -> electoral outcome","status":"GAP","support":["FCT-005","FCT-018","FCT-021","FCT-025","FCT-028","FCT-030"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"data_collection != targeting","status":"VERIFIED","support":["FCT-005","FCT-011","FCT-030"]}
CTRL-002 | {"control":"targeting != delivery","status":"VERIFIED","support":["FCT-019","FCT-020"]}
CTRL-003 | {"control":"delivery != exposure","status":"VERIFIED","support":["FCT-019","FCT-021"]}
CTRL-004 | {"control":"exposure != persuasion","status":"VERIFIED","support":["FCT-023","FCT-025","FCT-028"]}
CTRL-005 | {"control":"persuasion != vote_change","status":"VERIFIED","support":["FCT-023","FCT-024","FCT-033"]}
CTRL-006 | {"control":"campaign_use != foreign_interference","status":"VERIFIED","support":["FCT-005","FCT-030","FCT-031"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:12|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL:MNEMO_UNAVAILABLE | mnemo | NONE | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | OK | SRC-001 | https://www.cnil.fr/fr/respecter-les-droits-des-electeurs-sur-leurs-donnees-personnelles | FETCH CNIL droits électeurs RPP ciblage publicité politique 2026
QRY-002 | FETCH | OK | SRC-002 | https://www.cnil.fr/fr/elections-municipales-2026-le-plan-daction-de-la-cnil | FETCH CNIL plan action municipales 2026 données personnelles ciblage
QRY-003 | FETCH | OK | SRC-003 | https://www.cnil.fr/fr/municipales-2026-bilan-observatoire | FETCH CNIL bilan municipales 2026 signalements plaintes
QRY-004 | FETCH | OK | SRC-004 | https://www.cnil.fr/fr/la-cnil-prononce-quinze-nouvelles-sanctions-dans-le-cadre-de-la-procedure-simplifiee-depuis-janvier | FETCH CNIL sanction prospection politique élections 2022
QRY-005 | FETCH | OK | SRC-005 | https://about.fb.com/fr/news/2025/07/fin-de-la-publicite-portant-sur-un-enjeu-politique-electoral-ou-social-au-sein-de-lue-en-reponse-a-la-nouvelle-reglementation-europeenne/ | FETCH Meta fin publicités politiques UE octobre 2025
QRY-006 | FETCH | OK | SRC-006 | https://blog.google/company-news/inside-google/around-the-globe/google-europe/political-advertising-in-eu/ | FETCH Google stop political advertising EU October 2025
QRY-007 | FETCH | OK | SRC-007 | https://arxiv.org/abs/2302.06917 | FETCH étude Meta publicités politiques France présidentielle 2022
QRY-008 | FETCH | OK | SRC-008 | https://www.nature.com/articles/s41562-025-02328-w | FETCH Nature political advertising removal Facebook Instagram 2020 election
QRY-009 | FETCH | OK | SRC-009 | https://mitsloan.mit.edu/press/study-microtargeting-works-just-not-way-people-think | FETCH MIT Sloan PNAS microtargeting persuasion 2023
QRY-010 | FETCH | OK | SRC-010 | https://www.ox.ac.uk/news/2024-06-26-effectiveness-large-language-models-political-microtargeting-assessed-new-study | FETCH Oxford PNAS LLM political microtargeting 2024
QRY-011 | FETCH | OK | SRC-011 | https://ico.org.uk/for-the-public/your-data-and-elections/political-campaigning-practices-online-campaigning/ | FETCH ICO online campaigning microtargeting definition and practice
QRY-012 | FETCH | OK | SRC-012 | https://publications.parliament.uk/pa/ld5801/ldselect/lddemdigi/77/7708.htm | FETCH House Lords targeted political advertising efficacy microtargeting

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | CNIL-ELECTEURS-2026 | CNIL — Respecter les droits des électeurs sur leurs données personnelles | 2026-01-30 | 2026-09-08T09:45:00+02:00 | RPP depuis octobre 2025; information, consentement et ciblage | https://www.cnil.fr/fr/respecter-les-droits-des-electeurs-sur-leurs-donnees-personnelles
SRC-002 | ◈ | fam:A | CNIL-MUN2026-PLAN | CNIL — Municipales 2026 : plan d’action | 2026-01-30 | 2026-09-08T09:45:00+02:00 | croissance usages données; 2020 signalements; RPP 10 octobre 2025 | https://www.cnil.fr/fr/elections-municipales-2026-le-plan-daction-de-la-cnil
SRC-003 | ◈ | fam:A | CNIL-MUN2026-BILAN | CNIL — Municipales 2026 : bilan observatoire | 2026-04-08 | 2026-09-08T09:45:00+02:00 | 739 signalements; 81 plaintes; 4 contrôles; 1 sanction simplifiée | https://www.cnil.fr/fr/municipales-2026-bilan-observatoire
SRC-004 | ◈ | fam:A | CNIL-SANCTION-POL-2024 | CNIL — Sanctions simplifiées, dont prospection politique | 2024-06-12 | 2026-09-08T09:45:00+02:00 | campagne 2022; manquements information prospection | https://www.cnil.fr/fr/la-cnil-prononce-quinze-nouvelles-sanctions-dans-le-cadre-de-la-procedure-simplifiee-depuis-janvier
SRC-005 | ○ | fam:B | META-EU-POLADS-2025 | Meta — Fin de la publicité politique, électorale ou sociale dans l’UE | 2025-07-25 | 2026-09-08T09:45:00+02:00 | arrêt début octobre 2025; contenu politique organique maintenu | https://about.fb.com/fr/news/2025/07/fin-de-la-publicite-portant-sur-un-enjeu-politique-electoral-ou-social-au-sein-de-lue-en-reponse-a-la-nouvelle-reglementation-europeenne/
SRC-006 | ○ | fam:C | GOOGLE-EU-POLADS-2024 | Google — An update on political advertising in the EU | 2024-11-14 | 2026-09-08T09:45:00+02:00 | arrêt avant octobre 2025; historique transparence et restrictions ciblage | https://blog.google/company-news/inside-google/around-the-globe/google-europe/political-advertising-in-eu/
SRC-007 | ◈ | fam:D | ARXIV-2302.06917 | Sosnovik et al. — Meta political ads in 2022 French election | 2023-02-14 | 2026-09-08T09:45:00+02:00 | analyse publicités politiques et politiques publiques sur Meta France 2022 | https://arxiv.org/abs/2302.06917
SRC-008 | ◈ | fam:E | DOI-10.1038-s41562-025-02328-w | Nature Human Behaviour — Effects of political advertising removal before US 2020 election | 2026-03-02 | 2026-09-08T09:45:00+02:00 | RCT 36,906 Facebook + 25,925 Instagram; aucun effet détectable sur principaux outcomes | https://www.nature.com/articles/s41562-025-02328-w
SRC-009 | ◈ | fam:other:mit | MIT-PNAS-MICROTARGET-2023 | MIT Sloan — Microtargeting works, just not the way people think | 2023-06-21 | 2026-09-08T09:45:00+02:00 | expériences; avantage ciblage simple; pas de gain multi-attributs | https://mitsloan.mit.edu/press/study-microtargeting-works-just-not-way-people-think
SRC-010 | ◈ | fam:other:oxford | OXFORD-LLM-MICROTARGET-2024 | University of Oxford — Effectiveness of LLM political microtargeting | 2024-06-26 | 2026-09-08T09:45:00+02:00 | RCT preregistré; messages GPT-4 persuasifs; microciblés pas supérieurs en agrégé | https://www.ox.ac.uk/news/2024-06-26-effectiveness-large-language-models-political-microtargeting-assessed-new-study
SRC-011 | ◈ | fam:other:ico | ICO-MICROTARGETING | ICO — Political campaigning practices: online campaigning | 2024-03-08 | 2026-09-08T09:45:00+02:00 | partis/groupes utilisent analytics pour messages spécifiques à petits groupes/personnes | https://ico.org.uk/for-the-public/your-data-and-elections/political-campaigning-practices-online-campaigning/
SRC-012 | ◈ | fam:other:hol | HOL-DIGITAL-DEMOCRACY-2020 | House of Lords — Democracy and Digital Technologies: targeted advertising | 2020-06-29 | 2026-09-08T09:45:00+02:00 | échelle ciblage; efficacité/persuasion incertaine; difficulté mesure vote | https://publications.parliament.uk/pa/ld5801/ldselect/lddemdigi/77/7708.htm

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.cnil.fr/fr/respecter-les-droits-des-electeurs-sur-leurs-donnees-personnelles | A | 2026-09-08 | RPP applicable depuis octobre 2025 | La CNIL indique que le règlement européen sur la transparence de la publicité politique ajoute depuis octobre 2025 des obligations supplémentaires à la prospection politique. | -
FCT-002 | FACT | ✧ | https://www.cnil.fr/fr/respecter-les-droits-des-electeurs-sur-leurs-donnees-personnelles | A | 2026-09-08 | Information sur logique et paramètres de ciblage | Pour le ciblage et la diffusion de publicité politique, les électeurs doivent recevoir des informations supplémentaires sur la logique et les paramètres du ciblage ainsi que les catégories de données utilisées. | -
FCT-003 | FACT | ✧ | https://www.cnil.fr/fr/respecter-les-droits-des-electeurs-sur-leurs-donnees-personnelles | A | 2026-09-08 | Consentement requis pour ciblage publicitaire politique | La CNIL indique que le RPP impose un consentement pour le ciblage et la diffusion de publicité politique en ligne fondés sur des données personnelles. | -
FCT-004 | FACT | ✧ | https://www.cnil.fr/fr/respecter-les-droits-des-electeurs-sur-leurs-donnees-personnelles | A | 2026-09-08 | Collecte directe et données sensibles | Le cadre présenté par la CNIL restreint le ciblage politique en ligne aux données collectées directement et interdit le profilage fondé sur des catégories sensibles. | -
FCT-005 | FACT | ✧ | https://www.cnil.fr/fr/elections-municipales-2026-le-plan-daction-de-la-cnil | A | 2026-09-08 | Usage croissant de données en communication politique | La CNIL constate que communication et prospection politiques reposent de plus en plus sur des données personnelles et que de nouveaux usages se développent via réseaux sociaux et IA. | -
FCT-006 | FACT | ✧ | https://www.cnil.fr/fr/elections-municipales-2026-le-plan-daction-de-la-cnil | A | 2026-09-08 | Signalements municipales 2020 | Pour les municipales 2020, la CNIL avait reçu 3 948 signalements dans 329 communes, principalement sur SMS et appels; ces signalements décrivent de la prospection et ne mesurent pas à eux seuls le microtargeting. | -
FCT-007 | FACT | ✧ | https://www.cnil.fr/fr/elections-municipales-2026-le-plan-daction-de-la-cnil | A | 2026-09-08 | Première échéance française sous RPP | Les municipales 2026 constituent la première grande échéance française après l’entrée en application du RPP le 10 octobre 2025. | -
FCT-008 | FACT | ✧ | https://www.cnil.fr/fr/municipales-2026-bilan-observatoire | A | 2026-09-08 | Bilan CNIL municipales 2026 | La CNIL a reçu 739 signalements et instruit 81 plaintes lors des municipales 2026; quatre contrôles et une procédure simplifiée de sanction étaient engagés au bilan publié. | -
FCT-009 | FACT | ✧ | https://www.cnil.fr/fr/municipales-2026-bilan-observatoire | A | 2026-09-08 | Canaux de prospection 2026 | Parmi les signalements 2026, 63 % concernaient des SMS, 16 % des courriers, 13 % des courriels, 7 % des appels et 1 % un réseau social. | -
FCT-010 | FACT | ✧ | https://www.cnil.fr/fr/municipales-2026-bilan-observatoire | A | 2026-09-08 | Plaintes ne valent pas preuve de microtargeting | Les plaintes 2026 portaient notamment sur l’origine des données et parfois des suspicions de détournement de finalité; elles ne fournissent pas un dénominateur de microtargeting avéré. | -
FCT-011 | FACT | ✧ | https://www.cnil.fr/fr/la-cnil-prononce-quinze-nouvelles-sanctions-dans-le-cadre-de-la-procedure-simplifiee-depuis-janvier | A | 2026-09-08 | Manquement réel en prospection électorale 2022 | La CNIL a sanctionné anonymement une association politique pour défaut d’information lors de prospection pendant les élections présidentielle et législatives 2022. | -
FCT-012 | FACT | ✧ | https://www.cnil.fr/fr/la-cnil-prononce-quinze-nouvelles-sanctions-dans-le-cadre-de-la-procedure-simplifiee-depuis-janvier | A | 2026-09-08 | Sanction 2022 porte sur transparence, pas effet électoral | Le manquement décrit concernait l’information RGPD sur des outils de prospection; la décision ne démontre ni persuasion ni changement de vote. | -
FCT-013 | FACT | ✧ | https://about.fb.com/fr/news/2025/07/fin-de-la-publicite-portant-sur-un-enjeu-politique-electoral-ou-social-au-sein-de-lue-en-reponse-a-la-nouvelle-reglementation-europeenne/ | B | 2026-09-08 | Meta arrête les publicités politiques payantes UE | Meta a annoncé qu’à partir de début octobre 2025 les publicités politiques, électorales ou sur enjeux sociaux ne seraient plus autorisées sur ses plateformes dans l’UE. | -
FCT-014 | FACT | ✧ | https://about.fb.com/fr/news/2025/07/fin-de-la-publicite-portant-sur-un-enjeu-politique-electoral-ou-social-au-sein-de-lue-en-reponse-a-la-nouvelle-reglementation-europeenne/ | B | 2026-09-08 | Meta maintient les contenus politiques organiques | Meta précise que l’arrêt des publicités payantes n’empêche pas candidats et utilisateurs de publier et débattre de contenus politiques. | -
FCT-015 | FACT | ✧ | https://about.fb.com/fr/news/2025/07/fin-de-la-publicite-portant-sur-un-enjeu-politique-electoral-ou-social-au-sein-de-lue-en-reponse-a-la-nouvelle-reglementation-europeenne/ | B | 2026-09-08 | Meta disposait avant 2025 de transparence publicitaire | Meta affirme avoir appliqué depuis 2018 autorisation des annonceurs, disclosure du financeur et bibliothèque publicitaire contenant des informations de ciblage et budget. | -
FCT-016 | FACT | ✧ | https://blog.google/company-news/inside-google/around-the-globe/google-europe/political-advertising-in-eu/ | C | 2026-09-08 | Google arrête aussi la publicité politique UE | Google a annoncé l’arrêt de la publicité politique dans l’UE avant l’entrée en vigueur des nouvelles règles d’octobre 2025. | -
FCT-017 | FACT | ✧ | https://blog.google/company-news/inside-google/around-the-globe/google-europe/political-advertising-in-eu/ | C | 2026-09-08 | Google avait restreint le ciblage électoral | Google indique avoir imposé depuis 2019 vérification, disclosure du payeur, rapport de transparence et restrictions sur le ciblage des annonces électorales. | -
FCT-018 | FACT | ✧ | https://arxiv.org/abs/2302.06917 | D | 2026-09-08 | France 2022: corpus massif de publicités politiques Meta | L’étude Sosnovik et al. analyse un corpus massif de publicités politiques diffusées sur Meta pendant la présidentielle française de 2022. | -
FCT-019 | FACT | ✧ | https://arxiv.org/abs/2302.06917 | D | 2026-09-08 | Ad Library rend observable une partie de la chaîne | L’étude exploite la Meta Ad Library pour observer des publicités politiques et leur diffusion. | -
FCT-020 | FACT | ✧ | https://arxiv.org/abs/2302.06917 | D | 2026-09-08 | Différences de diffusion ne prouvent pas le ciblage choisi | Les distributions démographiques observées peuvent refléter à la fois les choix de l’annonceur et l’optimisation de delivery de la plateforme; elles ne suffisent donc pas à reconstruire les paramètres de ciblage choisis. | -
FCT-021 | FACT | ✧ | https://www.nature.com/articles/s41562-025-02328-w | E | 2026-09-08 | Grand RCT de retrait des publicités politiques | L’étude Nature randomise 36 906 utilisateurs Facebook et 25 925 utilisateurs Instagram pour retirer les publicités politiques pendant six semaines avant l’élection américaine de 2020. | -
FCT-022 | FACT | ✧ | https://www.nature.com/articles/s41562-025-02328-w | E | 2026-09-08 | Ciblage majoritaire vers les propres soutiens | Dans ce RCT, la plupart des publicités présidentielles étaient ciblées vers les soutiens du propre parti et les publicités de collecte de fonds étaient les plus fréquentes. | -
FCT-023 | FACT | ✧ | https://www.nature.com/articles/s41562-025-02328-w | E | 2026-09-08 | Aucun effet détectable sur principaux résultats | L’étude ne détecte pas d’effet du retrait des publicités politiques sur connaissance, polarisation, légitimité perçue, participation, faveur envers les candidats ou turnout, globalement ou par parti. | -
FCT-024 | FACT | ✧ | https://www.nature.com/articles/s41562-025-02328-w | E | 2026-09-08 | RCT publicité politique != test pur du microtargeting | Le traitement expérimental porte sur la présence de publicités politiques comme ensemble, pas sur un contraste pur microciblage versus message générique. | -
FCT-025 | FACT | ✧ | https://mitsloan.mit.edu/press/study-microtargeting-works-just-not-way-people-think | other:mit | 2026-09-08 | Avantage persuasif du ciblage simple dans PNAS 2023 | Dans les expériences rapportées par MIT, sélectionner une publicité sur un attribut de l’audience pouvait être environ 70 % plus efficace pour déplacer le soutien à une politique que diffuser le meilleur message unique à tous. | -
FCT-026 | FACT | ✧ | https://mitsloan.mit.edu/press/study-microtargeting-works-just-not-way-people-think | other:mit | 2026-09-08 | Pas de gain additionnel multi-attributs | Dans la même étude, ajouter plusieurs attributs individuels au ciblage n’apportait pas de bénéfice supplémentaire par rapport à un seul attribut. | -
FCT-027 | FACT | ✧ | https://mitsloan.mit.edu/press/study-microtargeting-works-just-not-way-people-think | other:mit | 2026-09-08 | Effet dépend du contexte | Les auteurs soulignent que l’avantage du ciblage varie fortement entre politiques et peut être plus faible hors du contexte expérimental. | -
FCT-028 | FACT | ✧ | https://www.ox.ac.uk/news/2024-06-26-effectiveness-large-language-models-political-microtargeting-assessed-new-study | other:oxford | 2026-09-08 | LLM messages persuasifs mais microciblage sans avantage agrégé | L’expérience randomisée présentée par Oxford constate que les messages GPT-4 sont globalement persuasifs, mais que les messages microciblés ne sont pas statistiquement plus persuasifs que les messages non microciblés en agrégé. | -
FCT-029 | FACT | ✧ | https://www.ox.ac.uk/news/2024-06-26-effectiveness-large-language-models-political-microtargeting-assessed-new-study | other:oxford | 2026-09-08 | Capacité LLM ne vaut pas efficacité du microciblage | L’étude Oxford met en doute les extrapolations selon lesquelles la personnalisation individuelle par LLM produirait automatiquement un gain persuasif. | -
FCT-030 | FACT | ✧ | https://ico.org.uk/for-the-public/your-data-and-elections/political-campaigning-practices-online-campaigning/ | other:ico | 2026-09-08 | ICO définit une pratique opérationnelle de microtargeting | L’ICO indique que partis et groupes de campagne utilisent des méthodes d’analyse de données regroupées sous le terme microtargeting pour adresser des messages spécifiques à de petits groupes ou individus. | -
FCT-031 | FACT | ✧ | https://ico.org.uk/for-the-public/your-data-and-elections/political-campaigning-practices-online-campaigning/ | other:ico | 2026-09-08 | Opacité pour la personne ciblée comme risque | L’ICO souligne qu’un problème central est que le public peut ne pas savoir que ses données sont utilisées pour le cibler avec de la publicité politique. | -
FCT-032 | FACT | ✧ | https://publications.parliament.uk/pa/ld5801/ldselect/lddemdigi/77/7708.htm | other:hol | 2026-09-08 | House of Lords: efficacité politique difficile à établir | Le rapport de la House of Lords relève qu’il n’est pas clair que la publicité politique microciblée à grande échelle persuade réellement ou change le cours des événements démocratiques. | -
FCT-033 | FACT | ✧ | https://publications.parliament.uk/pa/ld5801/ldselect/lddemdigi/77/7708.htm | other:hol | 2026-09-08 | Vote difficile à mesurer comme outcome publicitaire | Le rapport souligne qu’à la différence de ventes commerciales, les votes sont rares et non directement vérifiables, ce qui complique fortement l’évaluation de l’efficacité du ciblage politique. | -
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
FCT-013 | SRC-005
FCT-014 | SRC-005
FCT-015 | SRC-005
FCT-016 | SRC-006
FCT-017 | SRC-006
FCT-018 | SRC-007
FCT-019 | SRC-007
FCT-020 | SRC-007
FCT-021 | SRC-008
FCT-022 | SRC-008
FCT-023 | SRC-008
FCT-024 | SRC-008
FCT-025 | SRC-009
FCT-026 | SRC-009
FCT-027 | SRC-009
FCT-028 | SRC-010
FCT-029 | SRC-010
FCT-030 | SRC-011
FCT-031 | SRC-011
FCT-032 | SRC-012
FCT-033 | SRC-012

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

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:11:CAU-001 | NEXT_ACTION:13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-08T07:54:22.252337+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-029","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-030","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-031","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-032","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-033","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":33,"eligible":33,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:33;attempted:0;success:0;failure:0;blocked:33} | WRITEBACK_EXECUTION_V1:[33 rows, see section]

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
