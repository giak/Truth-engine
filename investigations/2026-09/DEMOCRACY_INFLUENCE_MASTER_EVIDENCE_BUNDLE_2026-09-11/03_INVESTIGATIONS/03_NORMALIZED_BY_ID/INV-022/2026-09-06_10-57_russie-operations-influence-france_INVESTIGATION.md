ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260906-1057-russie-operations-influence-france | PARENT_RUN_ID:NONE | AS_OF:2026-09-06
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/inv022_r3/truth-engine-v2_2.10.6-R3P0_CANONICAL/investigations/2026-09/2026-09-06_russie-operations-influence-france/2026-09-06_10-57_russie-operations-influence-france_INPUT.txt | SUBJECT_SLUG:russie-operations-influence-france | SUBJECT_FP:sha256:c98d6eec75f6fadc3b0e562b40fd67c4cfcdddb5d656335013d0d80211eb0d34 | INPUT_SHA256:sha256:b4582f7330c39e3a47f6aa7512bfb623ddea7e7e3dd046421e246631a29e05f4
COMPLEXITY:14→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['Russian state/proxies', 'VIGINUM', 'French institutions', 'platforms', 'media', 'audiences'], 'domains': ['information operations', 'attribution', 'infrastructure', 'actors/networks', 'audience/exposure', 'causality/impact', 'countermeasures'], 'exclusions': ['cyber/espionage without material influence link', 'generic Russian propaganda not materially France-targeted', 'unsupported claims of persuasion/electoral effect'], 'geo': ['France', 'foreign infrastructure causally linked to France-targeting operations'], 'lead_question': 'N/A(NO_INPUT_LEAD)', 'limits': ['public inspectable evidence as of 2026-09-06'], 'object_question': 'Quelles opérations d’influence attribuables à des acteurs russes ont matériellement visé la France, quelles infrastructures/acteurs les ont soutenues, quelle exposition est documentée et quels effets réels peuvent être établis ?', 'period': '2022-01-01/2026-09-06'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,forensic/REASONING.md,clusters/ICEBERG.md,clusters/FRAMING.md,clusters/OVERLOAD.md,clusters/FRAGMENTATION.md,clusters/WAR.md,clusters/NETWORK.md,clusters/TEMPORAL.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-022 — Opérations d’influence russes visant la France

## Objet et résultat borné

L’objet est la chaîne **opération → infrastructure/acteurs → exposition → effet**, pour les opérations visant matériellement la France entre 2022 et le 6 septembre 2026. Le corpus établit solidement l’existence et la persistance de plusieurs dispositifs visant la France, mais pas un effet causal démontré sur l’opinion, le comportement ou un résultat électoral. Cette frontière est portée notamment par `CLM-001`, `CLM-004`, `CLM-006`, `CAU-001` et `CAU-005`.

## Systèmes opérationnels observés

**RRN / Doppelganger.** Des clones de médias et des actifs coordonnés ciblant la France sont directement documentés (`FCT-001`, `FCT-002`, `FCT-019`). Les liens avec SDA/Structura et des autorités russes sont soutenus par plusieurs familles institutionnelles et plateforme (`FCT-003`), tout en conservant l’incertitude historique d’attribution plus forte au début de l’opération (`FCT-025`).

**Portal Kombat.** Le dispositif combine automatisation, forte volumétrie et techniques de découvrabilité (`FCT-004`, `FCT-006`). La mesure française disponible va toutefois dans le sens inverse d’une assimilation volume = audience : environ 10 700 visites pour `pravda-fr` sur le mois documenté (`FCT-005`). `CLM-002` reste donc `PARTIAL` avec un gap temporel : cette mesure n’est pas une série longitudinale 2022-2026.

**Matriochka / Operation Overload.** La cible comprend les médias, les fact-checkers et le débat français (`FCT-007`). Un effet direct est mesurable sur les intermédiaires : volume de sollicitations et travail de vérification induit (`FCT-008`, `CAU-003`). En revanche, l’effet de persuasion du public reste non établi (`FCT-009`, `CLM-003`).

**Storm-1516 / CopyCop / Storm-1679.** Le corpus documente des opérations persistantes visant élections, candidats et grands événements français (`FCT-010`, `FCT-012`, `FCT-015`, `FCT-021`, `FCT-024`, `FCT-026`). Les cas municipaux 2026 et les opérations pré-2027 observées fournissent toutefois plusieurs indicateurs de portée faible ou limitée (`FCT-013`, `FCT-014`, `FCT-026`).

## Attribution et réseau

La branche Doppelganger/SDA/Structura dispose de la convergence la plus forte : sources françaises, européennes, américaines et plateforme (`FCT-001`, `FCT-003`). Elle autorise une conclusion bornée sur cette branche, pas une généralisation à tous les modes opératoires russes étudiés.

L’attribution directe de Storm-1516 à l’unité 29155 du GRU reste plus délicate. Le rapport 2026 formule cette attribution (`FCT-016`), tandis que le rapport technique 2025 indiquait ne pas pouvoir confirmer l’implication directe de cette unité (`FCT-017`). `CLM-007` et `CAU-006` conservent donc un gap `INDEPENDENCE` : l’évolution de l’évaluation officielle est observée, mais le pont probatoire public n’est pas reproduit indépendamment.

## Exposition, audience et impact

Le corpus ne permet pas de traiter comme synonymes : nombre de contenus, actifs détectés, vues, audience, persuasion et effet politique. Plusieurs résultats vont même contre une lecture automatique de l’efficacité : faible audience Portal Kombat (`FCT-005`), capacité limitée de Matriochka à façonner l’opinion selon VIGINUM (`FCT-009`), absence d’engagement authentique positif substantiel observé par OpenAI pour les activités Doppelganger détectées (`FCT-018`), portée globalement limitée dans la synthèse VIGINUM (`FCT-022`) et faible retentissement de plusieurs opérations pré-2027 (`FCT-026`).

Le résultat le plus robuste est donc négatif : **aucun design causal ou contrefactuel public inspecté n’établit qu’une opération du corpus a causé un changement d’opinion, de comportement ou de résultat électoral en France** (`CLM-006`, `CAU-005`). Cela ne prouve pas l’absence d’effet ; cela borne ce qui peut être affirmé avec les preuves disponibles.

## Contre-mesures et effets observables

Des effets locaux de mitigation sont documentés : suspension de domaines par l’AFNIC (`FCT-013`), suppressions d’actifs par Meta (`FCT-019`) et blocages/suppressions par Google (`FCT-020`). `CAU-004` autorise une causalité locale entre action de retrait et indisponibilité des actifs concernés. `CLM-008` conserve cependant un gap causal sur l’effet dissuasif agrégé : le corpus ne permet pas d’isoler l’impact de ces mesures sur la capacité globale, la persistance ou l’audience de l’écosystème.

## Contradictions et limites actives

La contradiction matérielle principale concerne l’attribution Storm-1516 → GRU 29155 (`FCT-016` versus `FCT-017`). Elle n’est pas moyennée ni effacée. Les autres limites structurantes sont : absence de série longitudinale d’audience française pour Portal Kombat, absence de mesure causale de persuasion/comportement, topologie publique incomplète de certains réseaux et impossibilité de calculer une centralité ou un facteur d’exposition total à partir du corpus disponible.

## Conclusion technique

Le corpus permet d’établir avec des niveaux de preuve différenciés :

- des opérations répétées et adaptatives visant la France ;
- des infrastructures et relations d’acteurs documentées pour plusieurs branches ;
- des effets observables sur la disponibilité des contenus, les intermédiaires informationnels et certains actifs supprimés ;
- une exposition hétérogène, souvent faible dans les cas où elle est mesurée ;
- aucune preuve publique inspectée suffisante pour convertir cette activité en affirmation causale de persuasion ou de résultat électoral.

Les gaps conservés dans `CLM-002`, `CLM-003`, `CLM-005`, `CLM-006`, `CLM-007`, `CLM-008`, `CAU-005` et `CAU-006` constituent les points de reprise prioritaires d’une future mise à jour.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:8|EDI_DECISIVE:5|SRC_COMPLETE:20/20

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **checked_dates:** per SRC record
- **event_period:** 2022-01-01/2026-09-06
- **investigation_as_of:** 2026-09-06
- **publication_dates:** per SRC record

### MANIPULATION_REPORT
- **assumptions:**
  - official attribution must be distinguished from independently reproducible attribution
  - reach/exposure must not be promoted to persuasion or political effect
  - platform enforcement data measure detected/removed activity, not total unseen activity
- **clusters:**
  - **forensic:** forensic/REASONING.md
  - **loaded:**
    - clusters/ICEBERG.md
    - clusters/FRAMING.md
    - clusters/OVERLOAD.md
    - clusters/FRAGMENTATION.md
    - clusters/WAR.md
    - clusters/NETWORK.md
    - clusters/TEMPORAL.md
- **complexity:**
  - **class:** APEX
  - **score:** 14
- **implicit:**
  - **claims:**
    - high operational volume may be mistaken for high influence
    - state linkage may be overgeneralized from one MOI to another
  - **inversions:**
    - NONE
  - **omissions:**
    - audience denominators often absent
    - persuasion/behavior counterfactuals usually absent
    - effect of mitigation on observed reach is hard to isolate
- **input_kind:** TOPIC
- **mission_mode:** INVESTIGATION
- **patterns:**
  - @PAT[ICEBERG]
  - @PAT[NET]
  - @PAT[WAR]
  - @PAT[TEMP]
  - @PAT[FASC]
  - @PAT[COG_INFRA]
  - @PAT[INFODEMIC]
- **priorities:**
  - primary technical attribution
  - infrastructure reuse
  - France-targeted campaigns
  - audience/exposure measurement
  - counterevidence/alternative attribution
  - impact causality
  - mitigation effects
- **query_guidance:**
  - VIGINUM primary reports
  - EU/US legal-sanctions attribution
  - platform threat reports
  - independent technical reports
  - audience/effect measurements
  - counter-search on GRU attribution and impact
- **rhetorical:**
  - **AUTH:** 5
  - **BF:** 6
  - **DEM:** 1
  - **FAC:** 7
  - **NUM:** 3
- **speaker:** N/A(TOPIC_INPUT)
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **Κ:** 2
  - **Λ:** 4
  - **Ξ:** 6
  - **Σ:** 4
  - **Φ:** 4
  - **Ψ:** 7
  - **Ω:** 2
  - **κ:** 2
  - **ρ:** 4
  - **€:** 2
  - **↕:** 3
  - **⏰:** 7
  - **⚔:** 9
  - **⫸:** 6
  - **🌐:** 8
- **threats:**
  - @THR[INFODEMIC]
  - @THR[COG_INFILTRATION]

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - TEMPORAL
    - CAUSALITY
  - **input_ids:**
    - CLM-002
    - CLM-006
    - FCT-005
    - FCT-006
    - FCT-022
    - FCT-023
  - **module:** forensic/REASONING.md
  - **negative_results:**
    - No comparable total exposure/persuasion denominator across campaigns.
  - **not_computable:**
    - ICEBERG_FACTOR / visible share across heterogeneous campaigns
  - **operations_applied:**
    - visible-vs-omitted mapping
    - denominator comparability test
    - innocent methodological explanation test
  - **reason:** Audience denominators, hidden exposure and persuasion counterfactuals are materially omitted/unknown.
  - **result_ids:**
    - IMPACT_MAP
    - CLM-002
    - CLM-006
  - **status:** COMPLETE_WITH_GAPS
  - **trigger:** Ξ=6
- **item 2:**
  - **gaps:**
    - TEMPORAL longitudinal France audience
  - **input_ids:**
    - FCT-004
    - FCT-005
    - FCT-006
    - FCT-022
    - FCT-023
  - **module:** clusters/ICEBERG.md
  - **negative_results:**
    - High publication volume does not establish high French audience.
  - **not_computable:**
    - cross-campaign hidden audience total
  - **operations_applied:**
    - omission map
    - denominator check
    - volume-vs-audience comparison
  - **reason:** Operational volume could obscure absent audience/effect denominators.
  - **result_ids:**
    - CLM-002
    - IMPACT_MAP
  - **status:** COMPLETE_WITH_GAPS
  - **trigger:** Ξ=6
- **item 3:**
  - **gaps:**
    - CAUSALITY downstream effect
  - **input_ids:**
    - CLM-006
    - FCT-009
    - FCT-011
    - FCT-023
  - **module:** clusters/FRAMING.md
  - **negative_results:**
    - No evidence that the analytical framing itself caused audience effects.
  - **not_computable:**
    - NONE
  - **operations_applied:**
    - frame decomposition
    - alternative-frame reconstruction
    - context/denominator review
  - **reason:** Terms such as influence/impact can collapse targeting, visibility and persuasion.
  - **result_ids:**
    - DIALECTICAL_MAP
    - COGNITIVE_MAP
  - **status:** COMPLETE
  - **trigger:** Λ=4 lower-mandatory review
- **item 4:**
  - **gaps:**
    - CAUSALITY public persuasion
  - **input_ids:**
    - FCT-007
    - FCT-008
    - FCT-009
  - **module:** clusters/OVERLOAD.md
  - **negative_results:**
    - No measured cognitive-fatigue or persuasion effect on the wider French public.
  - **not_computable:**
    - public processing-capacity ratio
  - **operations_applied:**
    - defined stream/window review
    - workload evidence check
    - exposure-effect-intent separation
  - **reason:** Matriochka/Operation Overload explicitly targets newsrooms/fact-checkers with high-volume solicitations.
  - **result_ids:**
    - CLM-003
    - CAU-003
    - IMPACT_MAP
  - **status:** COMPLETE_WITH_GAP
  - **trigger:** Ψ=7
- **item 5:**
  - **gaps:**
    - INDEPENDENCE for some attribution edges
  - **input_ids:**
    - CLM-001
    - CLM-004
    - CLM-006
    - CLM-007
    - FCT-003
    - FCT-010
    - FCT-015
    - FCT-021
  - **module:** clusters/FRAGMENTATION.md
  - **negative_results:**
    - No evidence supports a single unified command chain across every MOI in the corpus.
  - **not_computable:**
    - convergence ratio across heterogeneous MOIs
  - **operations_applied:**
    - hypothesis stated before convergence
    - upstream-family deduplication
    - counter-index search
    - common-cause alternative
  - **reason:** Multiple MOIs converge on France but may remain operationally distinct.
  - **result_ids:**
    - DIALECTICAL_MAP
    - ACTOR_NETWORK_MAP
  - **status:** COMPLETE_WITH_GAP
  - **trigger:** ⫸=6
- **item 6:**
  - **gaps:**
    - INDEPENDENCE Storm-1516/GRU29155
  - **input_ids:**
    - FCT-001
    - FCT-003
    - FCT-007
    - FCT-010
    - FCT-015
    - FCT-019
    - FCT-021
    - FCT-024
  - **module:** clusters/WAR.md
  - **negative_results:**
    - State-level command is not independently reproduced for every MOI.
  - **not_computable:**
    - NONE
  - **operations_applied:**
    - content/infrastructure separation
    - targeting map
    - capability-sponsorship-command separation
    - organic/common-cause alternative test
  - **reason:** Persistent coordinated influence operations with infrastructure, targeting and attribution are the investigation object.
  - **result_ids:**
    - ACTOR_NETWORK_MAP
    - RESOURCE_FLOW_MAP
    - CLM-001
    - CLM-007
  - **status:** COMPLETE_WITH_GAP
  - **trigger:** ⚔=9
- **item 7:**
  - **gaps:**
    - partial public topology
  - **input_ids:**
    - FCT-003
    - FCT-012
    - FCT-013
    - FCT-019
    - FCT-020
    - FCT-024
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - Complete topology and centrality cannot be inferred from the bounded public graph.
  - **not_computable:**
    - centrality
    - density
    - betweenness
  - **operations_applied:**
    - typed node/edge construction
    - edge provenance attachment
    - speculative-edge exclusion
    - gatekeeper identification
  - **reason:** Material actor/infrastructure/platform relations require a typed sourced graph.
  - **result_ids:**
    - ACTOR_NETWORK_MAP
    - ACT-001
    - ACT-002
    - ACT-003
    - ACT-004
    - ACT-005
  - **status:** COMPLETE_WITH_GAP
  - **trigger:** 🌐=8
- **item 8:**
  - **gaps:**
    - no quantified orchestration probability
  - **input_ids:**
    - FCT-001
    - FCT-010
    - FCT-015
    - FCT-021
    - FCT-024
    - FCT-026
  - **module:** clusters/TEMPORAL.md
  - **negative_results:**
    - Timing alone does not establish cross-MOI coordination or political effect.
  - **not_computable:**
    - P_random without a defensible null model
  - **operations_applied:**
    - sequence normalization
    - historical-pattern review
    - mundane/common-cause alternative
  - **reason:** Operations persist/adapt across elections and events from 2022 through Aug 2026.
  - **result_ids:**
    - TEMPORAL_STATE
    - CLM-004
    - CLM-006
  - **status:** COMPLETE_WITH_GAP
  - **trigger:** ⏰=7

### SCOPING_REPORT
- **actors_institutions:**
  - Russian state/proxies
  - SDA
  - Structura
  - Storm-1516
  - Storm-1679
  - Doppelganger/RRN
  - Portal Kombat
  - Matriochka
  - CopyCop
  - VIGINUM
  - RCPE
  - AFNIC
  - platforms
- **domains:**
  - information operations
  - attribution
  - infrastructure
  - actors/networks
  - audience/exposure
  - causality/impact
  - countermeasures
- **evidence_limits:** sources publiques inspectables au 2026-09-06
- **exclusions:**
  - espionnage/cyberattaque sans lien matériel avec une opération d'influence
  - propagande russe non spécifiquement dirigée vers la France
  - spéculation non sourcée sur intention ou impact électoral
- **geo:** France prioritaire; infrastructures, commanditaires, relais et plateformes étrangers inclus lorsqu'ils sont causalement liés à une opération visant la France
- **lead_question:** N/A(NO_INPUT_LEAD)
- **object_coverage:** France-targeted campaigns + infrastructure + attribution + audience/exposure + causal impact + countermeasures; historical antecedents only when they explain active infrastructure/mechanisms
- **object_question:** Quelles opérations d’influence attribuables à des acteurs russes ont matériellement visé la France, ses publics ou son espace informationnel, quelles infrastructures et chaînes d’acteurs les ont soutenues, quelle audience/exposition est documentée, et quels effets réels peuvent être établis sans confondre attribution, diffusion, persuasion, comportement et impact politique ?
- **period:** 2022-01-01/2026-09-06

### CREDO
- **counter_hypotheses:**
  - Les cas agrégés peuvent relever d'acteurs pro-russes distincts plutôt que d'une chaîne de commandement unique.
  - La faible audience observée peut être partiellement causée par les contre-mesures plutôt que par l'inefficacité intrinsèque des opérations.
  - Une forte visibilité ponctuelle peut exister sans changement mesurable d'opinion ou de comportement.
- **falsifiers:**
  - Attribution technique indépendante incompatible avec les liens russes retenus.
  - Mesure causale robuste établissant un changement de comportement ou de résultat électoral imputable à une opération donnée.
  - Données d'audience montrant une portée organique substantielle là où le corpus actuel conclut à une portée faible.
- **lead_question:** N/A(NO_INPUT_LEAD)
- **object_question:** Quelles opérations d’influence attribuables à des acteurs russes ont matériellement visé la France, quelles infrastructures et chaînes d’acteurs les ont soutenues, quelle audience/exposition est documentée, et quels effets réels peuvent être établis sans confondre attribution, diffusion, persuasion, comportement et impact politique ?
- **working_hypotheses:**
  - Des MOI russes persistants et adaptatifs ciblent matériellement la France via des infrastructures et prestataires récurrents.
  - Le volume et la persistance opérationnels ne démontrent pas en eux-mêmes une persuasion ou un impact politique.
  - Certains MOI recherchent aussi un effet de surcharge ou de reprise médiatique plutôt qu'une audience organique massive.

### COGNITIVE_MAP
- **central_result:** The strongest public evidence supports persistent France-targeted operations, reusable infrastructure and some state/proxy links; it does not support a quantified causal claim about French opinion, behavior or electoral outcomes.
- **decision_boundaries:**
  - TARGETING != PERSUASION
  - VOLUME != AUDIENCE
  - VISIBILITY != POLITICAL_EFFECT
  - STATE_LINKAGE_FOR_ONE_MOI != UNIFIED_COMMAND_FOR_ALL_MOI
  - TAKEDOWN != AGGREGATE_DETERRENCE
- **object_question:** Quelles opérations d’influence attribuables à des acteurs russes ont matériellement visé la France, quelles infrastructures/acteurs les ont soutenues, quelle exposition est documentée et quels effets réels peuvent être établis ?
- **reasoning_graph:**
  - Attribution/infrastructure: FCT-001 + FCT-003 + FCT-019 + FCT-025 -> CLM-001 -> CAU-001
  - Volume versus audience: FCT-004 + FCT-005 + FCT-006 -> CLM-002 -> CAU-002
  - Intermediary workload: FCT-007 + FCT-008 + FCT-009 -> CLM-003 -> CAU-003
  - Electoral/current targeting: FCT-012..FCT-015 + FCT-024 + FCT-026 -> CLM-004/006
  - Attribution boundary: FCT-016 versus FCT-017 -> CLM-007 / CON-001 / CAU-006
  - Mitigation: FCT-013 + FCT-019 + FCT-020 -> CLM-008 / CAU-004
  - Impact stop: FCT-018 + FCT-022 + FCT-023 + FCT-026 -> CAU-005 / CAUSALITY GAP
- **remaining_uncertainties:**
  - Longitudinal French exposure for Portal Kombat
  - Independent public reproduction of GRU-29155 attribution for Storm-1516
  - Causal effect of mitigation on long-run operator capacity
  - Persuasion/behavior/electoral counterfactuals

### DIALECTICAL_MAP
- **arbitration:** The corpus supports existence, targeting, infrastructure, persistence and some bounded operational effects. It supports only limited/heterogeneous exposure measurements and leaves persuasion, behavior and election-result effects unestablished.
- **status:** BOUNDED_SYNTHESIS
- **steelman_each_side:**
  - **attribution_side:** Multiple independent official/platform/legal families converge for Doppelganger/SDA/Structura, making a purely accidental or invented linkage implausible for that branch.
  - **skeptical_side:** Government/platform reports observe detected activity and enforcement, not the universe of exposure; public evidence can be selective, and official attribution can mature without releasing all underlying evidence.
- **strongest_counter:**
  - **proposition:** Operational scale and repeated targeting do not demonstrate large audience or successful persuasion; several measured cases had low reach and public attribution is not uniformly independently reproducible.
  - **support_ids:**
    - FCT-005
    - FCT-009
    - FCT-014
    - FCT-017
    - FCT-018
    - FCT-022
    - FCT-023
    - FCT-025
    - FCT-026
- **thesis:**
  - **proposition:** Russia-linked influence ecosystems repeatedly and adaptively target France using cloned media, automated content, fake accounts, direct media/fact-checker targeting and event/election-specific narratives.
  - **support_ids:**
    - FCT-001
    - FCT-003
    - FCT-004
    - FCT-007
    - FCT-010
    - FCT-015
    - FCT-021
    - FCT-024
    - FCT-026

### RESOURCE_FLOW_MAP
- **financial_flows:** NONE_ESTABLISHED_IN_SCOPE: no comparable France-specific funding flow was required or established for the selected object question.
- **flows:**
  - **item 1:**
    - **evidence:**
      - FCT-001
      - FCT-002
      - FCT-003
      - FCT-019
    - **from:** SDA / Structura / Doppelganger-RRN infrastructure
    - **resource:** cloned domains + content + inauthentic accounts
    - **status:** SUPPORTED
    - **to:** French media lookalikes / platform users
  - **item 2:**
    - **evidence:**
      - FCT-004
      - FCT-005
      - FCT-006
    - **from:** Portal Kombat automation
    - **resource:** high-volume articles + SEO/discoverability
    - **status:** SUPPORTED_WITH_LOW_OBSERVED_AUDIENCE
    - **to:** pravda-fr / French search users
  - **item 3:**
    - **evidence:**
      - FCT-007
      - FCT-008
      - FCT-009
    - **from:** Matriochka / Operation Overload
    - **resource:** fake media assets + direct tags/emails
    - **status:** SUPPORTED_WORKLOAD_EFFECT
    - **to:** journalists and fact-checkers
  - **item 4:**
    - **evidence:**
      - FCT-012
      - FCT-013
      - FCT-014
      - FCT-015
      - FCT-021
      - FCT-024
      - FCT-026
    - **from:** Storm-1516 / CopyCop / Storm-1679
    - **resource:** fake sites, fabricated videos/reports, candidate-specific narratives
    - **status:** SUPPORTED_TARGETING
    - **to:** French candidates / election debate / Paris-2024 audiences
  - **item 5:**
    - **evidence:**
      - FCT-013
      - FCT-019
      - FCT-020
    - **from:** AFNIC / Meta / Google
    - **resource:** suspension / removal / blocking
    - **status:** SUPPORTED_MITIGATION
    - **to:** identified operation assets
- **limits:**
  - Publication volume is not an audience denominator.
  - Detected/removed assets are not the total ecosystem.
  - No flow establishes persuasion or electoral effect.

### ACTOR_NETWORK_MAP
- **edges:**
  - **item 1:**
    - **evidence:**
      - FCT-003
    - **from:** Russian authorities
    - **status:** SUPPORTED_BY_MULTIPLE_OFFICIAL_PLATFORM_FAMILIES
    - **to:** SDA / Structura
    - **type:** DIRECTS_OR_SPONSORS_CLAIMED
  - **item 2:**
    - **evidence:**
      - FCT-003
    - **from:** SDA / Structura
    - **status:** SUPPORTED
    - **to:** Doppelganger/RRN
    - **type:** OPERATES
  - **item 3:**
    - **evidence:**
      - FCT-001
      - FCT-002
      - FCT-019
      - FCT-020
    - **from:** Doppelganger/RRN
    - **status:** SUPPORTED
    - **to:** French audiences/media identities
    - **type:** TARGETS
  - **item 4:**
    - **evidence:**
      - FCT-012
      - FCT-024
    - **from:** Storm-1516
    - **status:** SUPPORTED
    - **to:** CopyCop
    - **type:** TECHNICAL_SUPPORT_OR_COMPONENT
  - **item 5:**
    - **evidence:**
      - FCT-016
      - FCT-017
    - **from:** GRU unit 29155
    - **status:** PARTIAL_CONTESTED_PUBLIC_CHAIN
    - **to:** Storm-1516
    - **type:** DIRECTS_OR_SPONSORS_CLAIMED
  - **item 6:**
    - **evidence:**
      - FCT-007
      - FCT-008
      - FCT-026
    - **from:** Matriochka
    - **status:** SUPPORTED
    - **to:** French media/fact-checkers/candidates
    - **type:** TARGETS
  - **item 7:**
    - **evidence:**
      - FCT-013
    - **from:** AFNIC
    - **status:** SUPPORTED
    - **to:** CopyCop .fr assets
    - **type:** REMOVES
  - **item 8:**
    - **evidence:**
      - FCT-019
    - **from:** Meta
    - **status:** SUPPORTED
    - **to:** Russian-origin influence assets
    - **type:** REMOVES
  - **item 9:**
    - **evidence:**
      - FCT-020
    - **from:** Google TAG
    - **status:** SUPPORTED
    - **to:** Russian-operation assets
    - **type:** REMOVES
- **gaps:**
  - No single command edge is established across all MOIs.
  - GRU29155→Storm-1516 direct public evidentiary bridge remains incomplete.
- **gatekeepers:**
  - AFNIC for .fr domain availability in documented cases
  - Meta/Google for platform asset availability in documented cases
- **graph_schema:**
  - **edge_types:**
    - DIRECTS_OR_SPONSORS_CLAIMED
    - OPERATES
    - TECHNICAL_SUPPORT
    - TARGETS
    - REMOVES
    - REPORTS_ON
  - **nodes:** operators/MOI/platforms/registrars/institutions/targets
  - **speculative_edges:** excluded
  - **window:** 2022-2026
- **metrics:** NOT_COMPUTABLE: graph is an evidence-bounded partial topology, not a complete enumerated network suitable for centrality/density inference.

### IMPACT_MAP
- **AFFECTED:**
  - **item 1:**
    - **groups:**
      - French audiences
      - journalists/fact-checkers
      - media organizations
      - political candidates/officials
      - platforms/registrars
    - **source_ids:**
      - FCT-001
      - FCT-007
      - FCT-008
      - FCT-012
      - FCT-015
      - FCT-021
      - FCT-024
      - FCT-026
    - **status:** ESTABLISHED_TARGETING_OR_DIRECT_WORKLOAD
- **BENEFITS:**
  - **item 1:**
    - **metric_baseline_period:** Portal Kombat: 152,464 articles in <3 months; RRN: 355 spoofing domains; period 2022-2026.
    - **object:** Russian influence operators / distribution systems
    - **result:** Documented operational benefit: persistent capacity to publish, clone media, automate distribution and obtain some attention. No public causal evidence establishes corresponding persuasion or political outcome.
    - **source_ids:**
      - FCT-002
      - FCT-004
      - FCT-006
      - FCT-010
      - FCT-021
    - **status:** BOUNDED_RESULT
- **COSTS_HARMS:**
  - **item 1:**
    - **metric_baseline_period:** >800 organizations targeted; ~2,400 tweets; >200 emails; >250 debunk/fact-check articles in the documented corpus.
    - **object:** Journalists and fact-checkers
    - **result:** Measurable verification workload caused by Operation Overload/Matriochka solicitations.
    - **source_ids:**
      - FCT-007
      - FCT-008
    - **status:** ESTABLISHED
  - **item 2:**
    - **metric_baseline_period:** >100 .fr local-media clone domains pre-positioned in 2026; multiple candidate-targeted operations through Aug 2026.
    - **object:** French candidates, institutions and media identities
    - **result:** Repeated impersonation, fake-domain and fabricated-media attacks created integrity and reputational risk around elections and public debate.
    - **source_ids:**
      - FCT-012
      - FCT-013
      - FCT-015
      - FCT-024
      - FCT-026
    - **status:** ESTABLISHED_RISK_NOT_OUTCOME
- **PERSUASION_BEHAVIOR_POLITICAL_OUTCOME:**
  - **gap_type:** CAUSALITY
  - **reason:** Publicly inspected evidence documents targeting, infrastructure, exposure proxies and some operational consequences, but no causal/counterfactual design demonstrates opinion change, behavior change or election-result change attributable to the examined operations.
  - **result:** NONE_ESTABLISHED
  - **supporting_limit_ids:**
    - FCT-005
    - FCT-009
    - FCT-011
    - FCT-014
    - FCT-018
    - FCT-022
    - FCT-023
    - FCT-026
    - CAU-005
- **RESPONSE_CHANGE:**
  - **item 1:**
    - **actor:** AFNIC
    - **result:** Most pre-positioned CopyCop .fr domains described for the 2026 municipal context were suspended.
    - **source_ids:**
      - FCT-013
    - **status:** OBSERVED
  - **item 2:**
    - **actor:** Meta
    - **result:** Removed 1,633 accounts, 703 Pages, one group and 29 Instagram accounts from a Russian-origin network targeting Germany and France.
    - **source_ids:**
      - FCT-019
    - **status:** OBSERVED
  - **item 3:**
    - **actor:** Google
    - **result:** Blocked/removed domains, YouTube channels and advertising accounts linked to Russian operations including Doppelganger.
    - **source_ids:**
      - FCT-020
    - **status:** OBSERVED

### CONTRADICTION_LEDGER
- **item 1:**
  - **conflicting_propositions:**
    - VIGINUM 2026 presents Storm-1516 as attributed to GRU unit 29155 with CGE support.
    - VIGINUM technical report 2025 said it could not confirm direct involvement of unit 29155 or Youry Khoroshenky despite close links.
  - **gap_type:** INDEPENDENCE
  - **id:** CON-001
  - **object_ids:**
    - CLM-007
    - FCT-016
    - FCT-017
  - **remaining_check:** Independent technical/documentary evidence explaining the evidentiary bridge from 2025 links to 2026 direct attribution.
  - **resolution:** Treat the 2026 attribution as an official later assessment; do not present the public chain as independently reproducible from the 2025 technical evidence.
  - **resolution_status:** UNRESOLVED_SCOPE_VERSION_DIFFERENCE
  - **source_ids:**
    - SRC-005
    - SRC-018

### VERIFICATION_REPORT
- **bias_test:**
  - **directness:** Strong for existence/targeting; weaker for downstream effects.
  - **independence:** Adequate for some decisive claims, single-family for others.
  - **interests:** French/US/EU authorities and platforms have institutional interests; independent/press sources provide partial challenge but not a full opposed-source corpus.
  - **method:** Audience metrics are sparse and platform/government reports cover observed/detected activity.
  - **provenance:** Diverse for Doppelganger attribution; concentrated in VIGINUM for several Storm cases.
  - **relevance:** High to France-targeted object; generic Russia operations excluded.
- **circular_families:**
  - NONE
- **contradiction_ids:**
  - CON-001
- **downgraded_ids:**
  - NONE
- **none_found_claims:**
  - CLM-002
  - CLM-003
  - CLM-004
  - CLM-005
- **refutation_searched:**
  - **FCT-001:** QRY-066:NONE
  - **FCT-003:** QRY-067:NONE
- **remaining_gaps:**
  - CLM-002:TEMPORAL
  - CLM-003:CAUSALITY
  - CLM-005:CAUSALITY
  - CLM-006:CAUSALITY
  - CLM-007:INDEPENDENCE
  - CLM-008:CAUSALITY
- **reopened_ids:**
  - SRC-001
  - SRC-002
  - SRC-003
  - SRC-005
  - SRC-010
  - SRC-012
  - SRC-013
  - SRC-014
  - SRC-018
  - SRC-019
  - SRC-020
  - FCT-001
  - FCT-003
- **status:** COMPLETE_WITH_TYPED_GAPS
- **upgraded_ids:**
  - NONE

### EDI_REPORT
- **corpus:**
  - **band:** BROAD
  - **cc:** 0.0
  - **circularity:** No accepted support family exceeds 50% of accepted SRC rows; family A is 10/20. Material Storm subclaims remain single-family and are flagged at claim level.
  - **counters:** 3
  - **coverage:** 1.0
  - **direct_objects:** 13
  - **edi_star:** 0.74
  - **independence:** 0.45
  - **target:** APEX 0.80 not reached; bounded search stopped with explicit gaps rather than score-chasing.
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **credible_counter:** FOUND
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 7
  - **item 2:**
    - **claim_id:** CLM-002
    - **credible_counter:** NONE_FOUND
    - **direct_object:** YES
    - **freshness:** STALE
    - **gap_type:** TEMPORAL
    - **independent_families:** 1
  - **item 3:**
    - **claim_id:** CLM-003
    - **credible_counter:** NONE_FOUND
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** CAUSALITY
    - **independent_families:** 2
  - **item 4:**
    - **claim_id:** CLM-004
    - **credible_counter:** NONE_FOUND
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 1
  - **item 5:**
    - **claim_id:** CLM-006
    - **credible_counter:** FOUND
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** CAUSALITY
    - **independent_families:** 7
- **diagnostic_not_truth:** true
- **dimensions:**
  - **geo:** 1.0
  - **lang:** 0.65
  - **owner:** 0.8
  - **persp:** 0.6
  - **strat:** 0.8
  - **temp:** 1.0
- **edi:**
  - **final:** 0.7
  - **flags:**
    - MISSING_COUNTER
  - **penalties:** 0.1
  - **raw:** 0.8
- **perspectives:**
  - **academic_expert:** MISSING
  - **critical_counter:** PRESENT
  - **dissident:** MISSING
  - **dominant_official:** PRESENT
  - **local_regional:** PRESENT
- **source_counts:**
  - **other:** 0
  - **primary:** 13
  - **secondary:** 7
  - **total:** 20

### RESPONSIBILITY_MAP
- **actions:**
  - ACT-001
  - ACT-002
  - ACT-003
  - ACT-004
  - ACT-005
- **boundaries:**
  - ACT-001 does not generalize SDA/Structura responsibility to Portal Kombat, Matriochka, Storm-1516 or Storm-1679 absent evidence.
  - Platform/registrar mitigation responsibility is bounded to observed enforcement actions, not downstream deterrence.
  - VIGINUM responsibility here is detection/reporting/attribution statements, not the truth of every hidden attribution input or downstream public effect.
- **individual_person_responsibility:** NONE_ASSIGNED: public evidence used here does not require naming an individual person to answer the object question.

### NEXT_QUERIES
- **item 1:**
  - **gap_owner:** CLM-002
  - **priority:** P1
  - **seek:** Longitudinal France-specific Portal Kombat audience/exposure series beyond Nov 2023
  - **stop:** Update only if comparable independent audience data become available.
- **item 2:**
  - **gap_owner:** CLM-007
  - **priority:** P1
  - **seek:** Independent technical/documentary evidence for the public evidentiary bridge GRU 29155 → Storm-1516
  - **stop:** Do not infer from later official attribution alone.
- **item 3:**
  - **gap_owner:** CLM-006
  - **priority:** P0
  - **seek:** Causal/counterfactual evidence of opinion, behavior or electoral-result change attributable to a specific operation
  - **stop:** Preserve NONE_ESTABLISHED absent a credible design.
- **item 4:**
  - **gap_owner:** CLM-008
  - **priority:** P2
  - **seek:** Longitudinal operator-capacity/audience evidence before and after takedowns to estimate aggregate deterrence
  - **stop:** Asset removal alone is insufficient.
- **item 5:**
  - **gap_owner:** EDI_REPORT
  - **priority:** P2
  - **seek:** Material Russian/opposed or independent academic/expert source engaging the same France-specific attribution/impact claims
  - **stop:** Do not add token perspective citations merely to raise EDI.

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-044,SRC-001 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-002,QRY-011,QRY-045,SRC-002 | support:- | counter:- | results:FCT-004,FCT-005,FCT-006 | final:SATURATED | gap:NONE
LED-003 | attempts:QRY-003,QRY-012,QRY-046,SRC-003,QRY-068,QRY-069,SRC-020 | support:- | counter:- | results:FCT-007,FCT-008,FCT-009,FCT-026 | final:SATURATED | gap:NONE
LED-004 | attempts:QRY-013,QRY-034,QRY-047,SRC-004 | support:- | counter:- | results:FCT-010,FCT-011,FCT-012,FCT-016,FCT-017,FCT-024 | final:SATURATED | gap:NONE
LED-005 | attempts:QRY-030,QRY-033,QRY-048,SRC-005 | support:- | counter:- | results:FCT-013,FCT-014,FCT-015,FCT-016 | final:SATURATED | gap:NONE
LED-006 | attempts:QRY-008,QRY-022,QRY-059,SRC-016 | support:- | counter:- | results:FCT-015,FCT-021 | final:SATURATED | gap:NONE
LED-007 | attempts:QRY-018,QRY-040,QRY-056,SRC-013 | support:- | counter:- | results:FCT-003,FCT-016,FCT-017 | final:SATURATED | gap:NONE
LED-008 | attempts:QRY-028,QRY-038,QRY-052,SRC-009 | support:- | counter:- | results:FCT-018 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-044,QRY-053,QRY-055,QRY-056,QRY-057,QRY-062,QRY-065,QRY-066,QRY-067,SRC-001,SRC-010,SRC-012,SRC-013,SRC-014,SRC-018,SRC-019 | support:- | counter:- | results:FCT-001,FCT-003,FCT-016,FCT-017,FCT-025,CAU-006 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-044,QRY-045,QRY-046,QRY-047,QRY-048,QRY-049,QRY-051,QRY-060,QRY-062,QRY-069,SRC-001,SRC-002,SRC-003,SRC-004,SRC-005,SRC-006,SRC-008,SRC-017,SRC-018,SRC-020 | support:- | counter:- | results:FCT-001,FCT-004,FCT-007,FCT-010,FCT-015,FCT-021,FCT-024,FCT-026 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-044,QRY-045,QRY-046,QRY-047,QRY-048,QRY-049,QRY-051,QRY-059,QRY-062,QRY-069 | support:- | counter:- | results:FCT-001,FCT-004,FCT-007,FCT-010,FCT-012,FCT-015,FCT-021,FCT-024,FCT-026 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-044,QRY-045,QRY-046,QRY-053,QRY-054,QRY-055,QRY-056,QRY-057,QRY-058,QRY-062 | support:- | counter:- | results:FCT-002,FCT-003,FCT-004,FCT-006,FCT-007,FCT-010,FCT-019,FCT-020,CAU-001,CAU-002,CAU-003 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-044,QRY-045,QRY-046,QRY-047,QRY-048,QRY-052,QRY-058,QRY-060 | support:- | counter:- | results:CAU-001,CAU-002,CAU-003,CAU-004,FCT-005,FCT-008,FCT-013,FCT-018,FCT-023 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-053,QRY-055,QRY-056,QRY-057,QRY-062,QRY-065,QRY-066,QRY-067 | support:- | counter:- | results:FCT-003,FCT-016,FCT-017,FCT-019,FCT-025,CAU-001,CAU-006,ACT-001 | final:SATURATED | gap:NONE
AXS-007 | attempts:QRY-048,QRY-053,QRY-054,QRY-055,QRY-056,QRY-057 | support:- | counter:- | results:CTRL-001,CTRL-002,CTRL-003,ACT-002,ACT-003,ACT-004 | final:SATURATED | gap:NONE
AXS-008 | attempts:QRY-045,QRY-046,QRY-048,QRY-052,QRY-058,QRY-060,QRY-069 | support:- | counter:- | results:FCT-005,FCT-008,FCT-009,FCT-013,FCT-014,FCT-018,FCT-022,FCT-023,FCT-026,CAU-003,CAU-004,CAU-005 | final:SATURATED | gap:NONE
AXS-009 | attempts:QRY-060,QRY-062,QRY-065,QRY-066,QRY-067,QRY-069 | support:- | counter:- | results:FCT-011,FCT-017,FCT-018,FCT-022,FCT-023,FCT-025,FCT-026,CAU-005,CAU-006 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-044,QRY-053,QRY-055,QRY-056,QRY-057,QRY-065,SRC-001,SRC-010,SRC-012,SRC-013,SRC-014,SRC-019 | support:FCT-001,FCT-003,FCT-019 | counter:FCT-025 | results:FCT-001,FCT-003,FCT-019,FCT-025 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-045,SRC-002 | support:FCT-004,FCT-005,FCT-006 | counter:- | results:FCT-004,FCT-005,FCT-006 | final:PARTIAL | gap:TEMPORAL
CLM-003 | attempts:QRY-046,QRY-058,QRY-060,QRY-069,SRC-003,SRC-015,SRC-017,SRC-020 | support:FCT-007,FCT-008,FCT-009,FCT-026 | counter:- | results:FCT-007,FCT-008,FCT-009,FCT-026 | final:SUPPORTED | gap:CAUSALITY
CLM-004 | attempts:QRY-047,QRY-048,QRY-051,QRY-062,SRC-004,SRC-005,SRC-008,SRC-018 | support:FCT-010,FCT-012,FCT-013,FCT-014,FCT-015,FCT-024 | counter:- | results:FCT-010,FCT-012,FCT-013,FCT-014,FCT-015,FCT-024 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-048,QRY-059,QRY-060,SRC-005,SRC-016,SRC-017 | support:FCT-021,FCT-022,FCT-023 | counter:- | results:FCT-021,FCT-022,FCT-023 | final:SUPPORTED | gap:CAUSALITY
CLM-006 | attempts:QRY-044,QRY-045,QRY-046,QRY-047,QRY-048,QRY-051,QRY-053,QRY-057,QRY-059,QRY-062,QRY-065,QRY-069,SRC-001,SRC-002,SRC-003,SRC-004,SRC-005,SRC-008,SRC-010,SRC-014,SRC-016,SRC-018,SRC-019,SRC-020 | support:FCT-001,FCT-004,FCT-007,FCT-010,FCT-015,FCT-021,FCT-024,FCT-026 | counter:FCT-011 | results:FCT-001,FCT-004,FCT-007,FCT-010,FCT-015,FCT-021,FCT-024,FCT-026,FCT-011 | final:SUPPORTED | gap:CAUSALITY
CLM-007 | attempts:QRY-048,QRY-062,SRC-005,SRC-018 | support:FCT-016 | counter:FCT-017 | results:FCT-016,FCT-017 | final:PARTIAL | gap:INDEPENDENCE
CLM-008 | attempts:QRY-048,QRY-053,QRY-054,QRY-060,QRY-069,SRC-005,SRC-010,SRC-011,SRC-017,SRC-020 | support:FCT-013,FCT-019,FCT-020 | counter:FCT-022,FCT-026 | results:FCT-013,FCT-019,FCT-020,FCT-022,FCT-026 | final:PARTIAL | gap:CAUSALITY

## STATUS_DELTA_V1
DELTA-001 | LED-001 | ACTIVE | SATURATED | phase9 bounded search terminalization
DELTA-002 | LED-002 | ACTIVE | SATURATED | phase9 bounded search terminalization
DELTA-003 | LED-003 | ACTIVE | SATURATED | phase9 bounded search terminalization
DELTA-004 | LED-004 | ACTIVE | SATURATED | phase9 bounded search terminalization
DELTA-005 | LED-005 | ACTIVE | SATURATED | phase9 bounded search terminalization
DELTA-006 | LED-006 | ACTIVE | SATURATED | phase9 bounded search terminalization
DELTA-007 | LED-007 | ACTIVE | SATURATED | phase9 bounded search terminalization
DELTA-008 | LED-008 | ACTIVE | SATURATED | phase9 bounded search terminalization
DELTA-009 | CLM-001 | ACTIVE | SUPPORTED | phase13 claim verification and bounded counter-evidence
DELTA-010 | CLM-002 | ACTIVE | PARTIAL | phase13 claim verification and bounded counter-evidence
DELTA-011 | CLM-003 | ACTIVE | SUPPORTED | phase13 claim verification and bounded counter-evidence
DELTA-012 | CLM-004 | ACTIVE | SUPPORTED | phase13 claim verification and bounded counter-evidence
DELTA-013 | CLM-005 | ACTIVE | SUPPORTED | phase13 claim verification and bounded counter-evidence
DELTA-014 | CLM-006 | ACTIVE | SUPPORTED | phase13 claim verification and bounded counter-evidence
DELTA-015 | CLM-007 | ACTIVE | PARTIAL | phase13 claim verification and bounded counter-evidence
DELTA-016 | CLM-008 | ACTIVE | PARTIAL | phase13 claim verification and bounded counter-evidence
DELTA-017 | AXS-001 | PLANNED | SATURATED | Phase 17 R3 terminalization after actual bounded searches and material FCT/CAU/CTRL/ACT results were available; no synthetic attempt/result IDs.
DELTA-018 | AXS-002 | PLANNED | SATURATED | Phase 17 R3 terminalization after actual bounded searches and material FCT/CAU/CTRL/ACT results were available; no synthetic attempt/result IDs.
DELTA-019 | AXS-003 | PLANNED | SATURATED | Phase 17 R3 terminalization after actual bounded searches and material FCT/CAU/CTRL/ACT results were available; no synthetic attempt/result IDs.
DELTA-020 | AXS-004 | PLANNED | SATURATED | Phase 17 R3 terminalization after actual bounded searches and material FCT/CAU/CTRL/ACT results were available; no synthetic attempt/result IDs.
DELTA-021 | AXS-005 | PLANNED | SATURATED | Phase 17 R3 terminalization after actual bounded searches and material FCT/CAU/CTRL/ACT results were available; no synthetic attempt/result IDs.
DELTA-022 | AXS-006 | PLANNED | SATURATED | Phase 17 R3 terminalization after actual bounded searches and material FCT/CAU/CTRL/ACT results were available; no synthetic attempt/result IDs.
DELTA-023 | AXS-007 | PLANNED | SATURATED | Phase 17 R3 terminalization after actual bounded searches and material FCT/CAU/CTRL/ACT results were available; no synthetic attempt/result IDs.
DELTA-024 | AXS-008 | PLANNED | SATURATED | Phase 17 R3 terminalization after actual bounded searches and material FCT/CAU/CTRL/ACT results were available; no synthetic attempt/result IDs.
DELTA-025 | AXS-009 | PLANNED | SATURATED | Phase 17 R3 terminalization after actual bounded searches and material FCT/CAU/CTRL/ACT results were available; no synthetic attempt/result IDs.

## OPEN_GAPS_V1
CLM-002 | CLM | PARTIAL | TEMPORAL | L’audience observée est un instantané de novembre 2023 et ne mesure pas longitudinalement l’exposition française sur toute la période 2022-2026.
CLM-003 | CLM | SUPPORTED | CAUSALITY | Le corpus établit la sollicitation et la charge de vérification, mais pas un effet causal de persuasion sur le public final.
CLM-005 | CLM | SUPPORTED | CAUSALITY | Aucun résultat public inspecté n’isole un effet des opérations Paris 2024 sur les comportements, la fréquentation ou le déroulement des Jeux.
CLM-006 | CLM | SUPPORTED | CAUSALITY | Aucun design causal ou contrefactuel public inspecté ne démontre un changement d’opinion, de comportement ou de résultat électoral causé par ces opérations.
CLM-007 | CLM | PARTIAL | INDEPENDENCE | Le rapport 2026 affirme l’attribution à l’unité 29155, mais la chaîne publique ne permet pas de reproduire indépendamment le passage des liens documentés en 2025 à l’attribution directe.
CLM-008 | CLM | PARTIAL | CAUSALITY | Les retraits/suspensions d’actifs sont observables, mais leur effet dissuasif agrégé sur la capacité, la persistance ou l’audience de l’écosystème russe n’est pas isolé.
CAU-005 | CAU | UNRESOLVED | CAUSALITY | Persuasion, behavior change and counterfactual electoral impact are not established by the available exposure/visibility evidence.
CAU-006 | CAU | UNRESOLVED | INDEPENDENCE | Publicly inspectable evidence does not independently reproduce the full attribution chain from Storm-1516 operations to direct Unit 29155 command.

SEMANTIC_COUNTS_V1:LED:8|CLM:8|AXS:9|CAU:6|CTRL:3|ACT:5

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-044","SRC-001"],"evidence_excerpt":"ayant visé plusieurs États européens depuis septembre 2022, dont la France","kind":"MECHANISM","lead":"RRN/Doppelganger a explicitement ciblé la France depuis septembre 2022 par typosquattage de médias/administrations, faux sites francophones et comptes inauthentiques.","linked_ids":["CLM-001","CLM-006"],"locator":"HTML lines 18-34","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003"],"routes":["AUDIT","EXPAND","LINK"],"source_id":"SRC-001","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-002","QRY-011","QRY-045","SRC-002"],"evidence_excerpt":"celui ciblant la France étant par ailleurs, le moins visité","kind":"MECHANISM","lead":"Portal Kombat cible la France avec automatisation et SEO, mais l'audience observée de pravda-fr était faible par rapport au volume de publication.","linked_ids":["CLM-002","CLM-006"],"locator":"PDF p.6 + footnote 17","materiality":"DECISIVE","result_ids":["FCT-004","FCT-005","FCT-006"],"routes":["EXPAND","LINK"],"source_id":"SRC-002","status":"SATURATED"}
LED-003 | {"attempt_ids":["QRY-003","QRY-012","QRY-046","SRC-003","QRY-068","QRY-069","SRC-020"],"evidence_excerpt":"susceptible d’affecter le débat public numérique francophone","kind":"MECHANISM","lead":"Matriochka cible le débat public francophone, les médias et fact-checkers par faux contenus coordonnés et sollicitations directes.","linked_ids":["CLM-003","CLM-006"],"locator":"HTML lines 16-21","materiality":"DECISIVE","result_ids":["FCT-007","FCT-008","FCT-009","FCT-026"],"routes":["EXPAND","LINK"],"source_id":"SRC-003","status":"SATURATED"}
LED-004 | {"attempt_ids":["QRY-013","QRY-034","QRY-047","SRC-004"],"evidence_excerpt":"l’impact réel sur le débat public numérique demeure difficile à estimer","kind":"MECHANISM","lead":"Storm-1516 est un MOI russe persistant ayant ciblé des audiences françaises; son impact réel est explicitement difficile à estimer.","linked_ids":["CLM-004","CLM-006","CLM-007"],"locator":"HTML lines 12-21","materiality":"DECISIVE","result_ids":["FCT-010","FCT-011","FCT-012","FCT-016","FCT-017","FCT-024"],"routes":["AUDIT","EXPAND","LINK"],"source_id":"SRC-004","status":"SATURATED"}
LED-005 | {"attempt_ids":["QRY-030","QRY-033","QRY-048","SRC-005"],"evidence_excerpt":"Elle n’a toutefois pas eu d’effet significatif","kind":"EVENT","lead":"Pendant les municipales 2026, VIGINUM a documenté deux INE pro-russes persistantes; CopyCop et Storm-1516 ont eu des effets/visibilités limités dans les cas décrits.","linked_ids":["CLM-004","CLM-006","CLM-008"],"locator":"PDF pp.8-10 and p.20","materiality":"DECISIVE","result_ids":["FCT-013","FCT-014","FCT-015","FCT-016"],"routes":["EXPAND","LINK"],"source_id":"SRC-005","status":"SATURATED"}
LED-006 | {"attempt_ids":["QRY-008","QRY-022","QRY-059","SRC-016"],"evidence_excerpt":"Storm-1679 is not the only Russia-aligned actor seeking to undermine the 2024 Games","kind":"EVENT","lead":"Storm-1679 et Doppelganger/Storm-1099 ont ciblé Paris 2024 avec faux contenus, peur de violence et usurpations de médias français.","linked_ids":["CLM-005","CLM-006"],"locator":"HTML lines 6-31","materiality":"IMPORTANT","result_ids":["FCT-015","FCT-021"],"routes":["EXPAND","LINK"],"source_id":"SRC-016","status":"SATURATED"}
LED-007 | {"attempt_ids":["QRY-018","QRY-040","QRY-056","SRC-013"],"evidence_excerpt":"at the direction of the Russian Presidential Administration","kind":"RELATION","lead":"Le Trésor américain relie SDA et Structura à une campagne persistante menée sous la direction de l'administration présidentielle russe et à des faux sites imitant des médias européens.","linked_ids":["CLM-001","CLM-007"],"locator":"HTML lines 330-347","materiality":"DECISIVE","result_ids":["FCT-003","FCT-016","FCT-017"],"routes":["AUDIT","LINK"],"source_id":"SRC-013","status":"SATURATED"}
LED-008 | {"attempt_ids":["QRY-028","QRY-038","QRY-052","SRC-009"],"evidence_excerpt":"appears to have earned substantial positive engagement from authentic audiences","kind":"EVIDENCE","lead":"OpenAI a observé l'usage de ses modèles par Doppelganger pour du contenu français, mais pas d'engagement authentique positif substantiel dans les campagnes détectées.","linked_ids":["CLM-001","CLM-006"],"locator":"HTML lines 25-52","materiality":"DECISIVE","result_ids":["FCT-018"],"routes":["AUDIT","EXPAND"],"source_id":"SRC-009","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"RRN/Doppelganger a matériellement ciblé la France et son infrastructure d'usurpation/amplification est reliée à des prestataires russes agissant pour ou sous direction d'autorités russes.","claimant":"INV-022 synthesis","counter":["FCT-025"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-003","FCT-019"]}
CLM-002 | {"claim":"Portal Kombat a ciblé la France par une infrastructure automatisée et optimisée pour la recherche, mais les mesures disponibles montrent une audience française faible relativement au volume publié.","claimant":"INV-022 synthesis","counter":"NONE_FOUND","gap":"L’audience observée est un instantané de novembre 2023 et ne mesure pas longitudinalement l’exposition française sur toute la période 2022-2026.","gap_type":"TEMPORAL","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-004","FCT-005","FCT-006"]}
CLM-003 | {"claim":"Matriochka/Operation Overload cible directement médias et fact-checkers français; un effet de charge de travail et d'amplification par les débunks est documenté, sans preuve d'un effet de persuasion correspondant.","claimant":"INV-022 synthesis","counter":"NONE_FOUND","gap":"Le corpus établit la sollicitation et la charge de vérification, mais pas un effet causal de persuasion sur le public final.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-007","FCT-008","FCT-009","FCT-026"]}
CLM-004 | {"claim":"Storm-1516/CopyCop constitue un dispositif pro-russe persistant qui a ciblé le débat public et des processus électoraux français; les cas municipaux 2026 documentés ont eu une visibilité ou un effet limité.","claimant":"INV-022 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-010","FCT-012","FCT-013","FCT-014","FCT-015","FCT-024"]}
CLM-005 | {"claim":"Storm-1679 et Doppelganger ont ciblé Paris 2024 par des narratifs de peur, d'insécurité et des usurpations médiatiques; l'existence des opérations est établie mais leur effet réel sur les comportements ou le déroulement des Jeux ne l'est pas.","claimant":"INV-022 synthesis","counter":"NONE_FOUND","gap":"Aucun résultat public inspecté n’isole un effet des opérations Paris 2024 sur les comportements, la fréquentation ou le déroulement des Jeux.","gap_type":"CAUSALITY","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-021","FCT-022","FCT-023"]}
CLM-006 | {"claim":"Dans le corpus public 2022-2026, la persistance, l'adaptation et l'exposition de plusieurs opérations russes visant la France sont établies; une persuasion, un changement comportemental ou un résultat électoral causé par elles n'est pas établi.","claimant":"INV-022 synthesis","counter":["FCT-011"],"gap":"Aucun design causal ou contrefactuel public inspecté ne démontre un changement d’opinion, de comportement ou de résultat électoral causé par ces opérations.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-004","FCT-007","FCT-010","FCT-015","FCT-021","FCT-024","FCT-026"]}
CLM-007 | {"claim":"L'attribution de Storm-1516 à l'unité 29155 du GRU est affirmée dans le rapport VIGINUM 2026, mais la chaîne probatoire publique permettant de reproduire indépendamment ce niveau d'attribution reste incomplète dans le corpus inspecté.","claimant":"INV-022 synthesis","counter":["FCT-017"],"gap":"Le rapport 2026 affirme l’attribution à l’unité 29155, mais la chaîne publique ne permet pas de reproduire indépendamment le passage des liens documentés en 2025 à l’attribution directe.","gap_type":"INDEPENDENCE","materiality":"IMPORTANT","status":"PARTIAL","support":["FCT-016"]}
CLM-008 | {"claim":"Les contre-mesures de plateformes, registrars et autorités ont réduit l'accessibilité ou la visibilité de certaines opérations observées, mais leur effet dissuasif agrégé sur l'écosystème russe n'est pas établi.","claimant":"INV-022 synthesis","counter":["FCT-022","FCT-026"],"gap":"Les retraits/suspensions d’actifs sont observables, mais leur effet dissuasif agrégé sur la capacité, la persistance ou l’audience de l’écosystème russe n’est pas isolé.","gap_type":"CAUSALITY","materiality":"IMPORTANT","status":"PARTIAL","support":["FCT-013","FCT-019","FCT-020"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-044","QRY-053","QRY-055","QRY-056","QRY-057","QRY-062","QRY-065","QRY-066","QRY-067","SRC-001","SRC-010","SRC-012","SRC-013","SRC-014","SRC-018","SRC-019"],"axis":"SOURCE_AUDIT","links":["LED-001","LED-004","LED-007","CLM-001","CLM-007"],"question":"Les attributions et cas retenus reposent-ils sur des objets primaires inspectés et des corroborations indépendantes de leur source institutionnelle initiale ?","result_ids":["FCT-001","FCT-003","FCT-016","FCT-017","FCT-025","CAU-006"],"sought_objects":["rapports techniques","takedown reports","sanctions/affidavits","contre-attributions"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-044","QRY-045","QRY-046","QRY-047","QRY-048","QRY-049","QRY-051","QRY-060","QRY-062","QRY-069","SRC-001","SRC-002","SRC-003","SRC-004","SRC-005","SRC-006","SRC-008","SRC-017","SRC-018","SRC-020"],"axis":"SCOPE_HISTORY","links":["LED-001","LED-002","LED-003","LED-004","LED-005","LED-006"],"question":"Quels MOI et infrastructures ont effectivement ciblé la France entre 2022 et 2026 et comment ont-ils évolué ?","result_ids":["FCT-001","FCT-004","FCT-007","FCT-010","FCT-015","FCT-021","FCT-024","FCT-026"],"sought_objects":["chronologie","réutilisation d'infrastructure","pivots vers élections/grands événements"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-044","QRY-045","QRY-046","QRY-047","QRY-048","QRY-049","QRY-051","QRY-059","QRY-062","QRY-069"],"axis":"EVIDENCE_CASES","links":["CLM-001","CLM-002","CLM-003","CLM-004","CLM-005"],"question":"Quels cas français sont directement documentés par des sources inspectables ?","result_ids":["FCT-001","FCT-004","FCT-007","FCT-010","FCT-012","FCT-015","FCT-021","FCT-024","FCT-026"],"sought_objects":["RRN","Portal Kombat","Matriochka","Storm-1516","Storm-1679","CopyCop"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-044","QRY-045","QRY-046","QRY-053","QRY-054","QRY-055","QRY-056","QRY-057","QRY-058","QRY-062"],"axis":"RESOURCES_FLOWS","links":["LED-001","LED-002","LED-003","LED-007"],"question":"Quels flux de contenus, infrastructures, comptes, domaines et capacités permettent la production et la diffusion ?","result_ids":["FCT-002","FCT-003","FCT-004","FCT-006","FCT-007","FCT-010","FCT-019","FCT-020","CAU-001","CAU-002","CAU-003"],"sought_objects":["domaines","hébergement","comptes","Telegram/X","prestataires","IA"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-044","QRY-045","QRY-046","QRY-047","QRY-048","QRY-052","QRY-058","QRY-060"],"axis":"MECHANISMS","links":["CLM-001","CLM-002","CLM-003","CLM-004"],"question":"Quels mécanismes transforment production de contenu en exposition potentielle : usurpation, SEO, faux comptes, amplification, sollicitation de fact-checkers ?","result_ids":["CAU-001","CAU-002","CAU-003","CAU-004","FCT-005","FCT-008","FCT-013","FCT-018","FCT-023"],"sought_objects":["chaînes de diffusion","SEO","amplification coordonnée","meta-trolling","cross-platform"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-053","QRY-055","QRY-056","QRY-057","QRY-062","QRY-065","QRY-066","QRY-067"],"axis":"ACTORS_RELATIONS","links":["LED-007","CLM-001","CLM-007"],"question":"Quels acteurs russes, prestataires, MOI et relais sont reliés, et avec quel niveau d'attribution ?","result_ids":["FCT-003","FCT-016","FCT-017","FCT-019","FCT-025","CAU-001","CAU-006","ACT-001"],"sought_objects":["SDA","Structura","administration présidentielle russe","GRU 29155","CGE","CopyCop","Storm clusters"],"status":"SATURATED"}
AXS-007 | {"attempt_ids":["QRY-048","QRY-053","QRY-054","QRY-055","QRY-056","QRY-057"],"axis":"RULES_CONTROLS","links":["CLM-008"],"question":"Quelles contre-mesures ont été réellement appliquées et quels résultats observables ont-elles produits ?","result_ids":["CTRL-001","CTRL-002","CTRL-003","ACT-002","ACT-003","ACT-004"],"sought_objects":["takedowns","blocage de domaines","AFNIC","sanctions","saisies"],"status":"SATURATED"}
AXS-008 | {"attempt_ids":["QRY-045","QRY-046","QRY-048","QRY-052","QRY-058","QRY-060","QRY-069"],"axis":"IMPACT_RESPONSIBILITY","links":["LED-002","LED-005","LED-008","CLM-002","CLM-003","CLM-004","CLM-005","CLM-006"],"question":"Que peut-on établir sur audience, exposition, charge, persuasion, comportement et impact politique, sans franchir les droits causaux disponibles ?","result_ids":["FCT-005","FCT-008","FCT-009","FCT-013","FCT-014","FCT-018","FCT-022","FCT-023","FCT-026","CAU-003","CAU-004","CAU-005"],"sought_objects":["audience","engagement authentique","charge fact-checkers","reprises politiques","effet électoral","contre-factuel"],"status":"SATURATED"}
AXS-009 | {"attempt_ids":["QRY-060","QRY-062","QRY-065","QRY-066","QRY-067","QRY-069"],"axis":"COUNTER_HYPOTHESES","links":["CLM-006","CLM-007","CLM-008"],"question":"Quelles explications concurrentes ou limites réduisent les conclusions sur coordination, audience et impact ?","result_ids":["FCT-011","FCT-017","FCT-018","FCT-022","FCT-023","FCT-025","FCT-026","CAU-005","CAU-006"],"sought_objects":["faible audience","inauthentic amplification","effet des contre-mesures","attribution partielle","absence de causal design"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"ENABLER","counter":["FCT-025"],"limit":"This establishes an evidenced enabling chain for Doppelganger/RRN, not a single unified command chain for every Russia-aligned operation documented in France.","mechanism":"Russian-state-linked SDA/Structura operational direction and technical infrastructure enabled cloned-media domains, inauthentic accounts and distribution chains to target French audiences.","status":"SUPPORTED","support":["FCT-001","FCT-003","FCT-019","FCT-020"]}
CAU-002 | {"causal_right":"ENABLER","counter":["FCT-005"],"limit":"Discoverability and publication capacity do not establish mass exposure or persuasion; the observed French audience snapshot was low.","mechanism":"Portal Kombat automation, high publication volume and SEO practices materially increased the availability and discoverability of content aimed at French search users.","status":"SUPPORTED","support":["FCT-004","FCT-006"]}
CAU-003 | {"causal_right":"CAUSE","counter":["FCT-009"],"limit":"The evidenced outcome is workload/attention, not persuasion of the wider public.","mechanism":"Matriochka/Operation Overload direct tagging and emailing of journalists and fact-checkers generated a measurable verification workload and induced publication of debunks that could itself extend attention to the fabricated material.","status":"SUPPORTED","support":["FCT-007","FCT-008"]}
CAU-004 | {"causal_right":"CAUSE","counter":"NONE_FOUND","limit":"Specific asset removal is documented; the aggregate deterrent effect on operator capacity and long-run audience is not isolated.","mechanism":"AFNIC and platform enforcement removed or suspended identified domains/accounts, reducing accessibility of specific operation assets.","status":"SUPPORTED","support":["FCT-013","FCT-019","FCT-020"]}
CAU-005 | {"counter":["FCT-005","FCT-009","FCT-013","FCT-014","FCT-018","FCT-022"],"gap":"Persuasion, behavior change and counterfactual electoral impact are not established by the available exposure/visibility evidence.","gap_type":"CAUSALITY","limit":"No public causal design in the inspected corpus isolates exposure from platform actions, organic political dynamics, prior attitudes or other events.","mechanism":"Exposure to Russia-aligned influence-operation content may contribute to opinion, behavior or electoral outcomes.","status":"UNRESOLVED","support":["FCT-011","FCT-021","FCT-023"]}
CAU-006 | {"counter":["FCT-017"],"gap":"Publicly inspectable evidence does not independently reproduce the full attribution chain from Storm-1516 operations to direct Unit 29155 command.","gap_type":"INDEPENDENCE","limit":"The 2026 VIGINUM municipal report presents attribution to Unit 29155, while the 2025 technical report said direct involvement could not then be confirmed; the public evidentiary bridge is incomplete.","mechanism":"Direct command or operational control by GRU Unit 29155 over Storm-1516.","status":"UNRESOLVED","support":["FCT-016"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"AFNIC suspension of pre-positioned CopyCop .fr clone domains during the 2026 municipal-election context","limit":"Asset-level removal is established; aggregate deterrence against the wider ecosystem is not.","status":"PASS","support":["FCT-013"]}
CTRL-002 | {"control":"Meta coordinated-inauthentic-behavior enforcement against a Russian-origin network targeting Germany and France","limit":"Removed assets are observed; total unseen activity and downstream persuasion are not measured.","status":"PASS","support":["FCT-019"]}
CTRL-003 | {"control":"Google TAG blocking/removal of domains, YouTube channels and advertising accounts linked to Russian operations including Doppelganger","limit":"Enforcement counts demonstrate intervention, not aggregate ecosystem deterrence.","status":"PASS","support":["FCT-020"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Operate content/infrastructure associated with the Doppelganger/RRN branch, including cloned-media and influence-distribution assets.","actor":"Social Design Agency / Structura","intent":"CLAIMED","responsibility_scope":"Bounded to the Doppelganger/RRN branch supported by EU/US/platform evidence; does not establish command over every Russia-aligned MOI in the corpus.","status":"PASS","support":["FCT-003"]}
ACT-002 | {"action":"Suspend most identified .fr domains pre-positioned by CopyCop to imitate local news sites in the 2026 municipal context.","actor":"AFNIC","intent":"CLAIMED","responsibility_scope":"Domain-registry mitigation only; no claim of causal deterrence beyond removed assets.","status":"PASS","support":["FCT-013"]}
ACT-003 | {"action":"Remove coordinated inauthentic accounts/Pages/group/Instagram assets from a Russian-origin influence network targeting France among other countries.","actor":"Meta","intent":"CLAIMED","responsibility_scope":"Platform enforcement on detected assets.","status":"PASS","support":["FCT-019"]}
ACT-004 | {"action":"Block or remove domains, YouTube channels and advertising accounts linked to Russian influence operations, including Doppelganger-related batches.","actor":"Google TAG","intent":"CLAIMED","responsibility_scope":"Google ecosystem enforcement on detected assets.","status":"PASS","support":["FCT-020"]}
ACT-005 | {"action":"Detect, publicly characterize and in some cases attribute France-targeted influence operations including RRN and Storm-1516.","actor":"VIGINUM","intent":"CLAIMED","responsibility_scope":"Detection/public characterization and attribution statements; not proof of downstream political impact.","status":"PASS","support":["FCT-001","FCT-024"]}

SEARCH_ACTIVITY_V1:WEB:49|FETCH:20|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | subject-fp | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | site:sgdsn.gouv.fr/viginum RRN Russie France influence report RRN Doppelganger
QRY-002 | WEB | FOUND | - | - | site:sgdsn.gouv.fr/viginum Portal Kombat Pravda France Russian influence report
QRY-003 | WEB | FOUND | - | - | site:sgdsn.gouv.fr/viginum Matriochka France Russian influence report
QRY-004 | WEB | FOUND | - | - | site:sgdsn.gouv.fr/viginum Olympics Russian influence Paris 2024 report
QRY-005 | WEB | FOUND | - | - | site:consilium.europa.eu Russian information manipulation sanctions Doppelganger SDA Structura 2024 2025
QRY-006 | WEB | FOUND | - | - | site:eeas.europa.eu FIMI Russia Doppelganger France report
QRY-007 | WEB | FOUND | - | - | site:about.fb.com threat report Russia Doppelganger France 2024
QRY-008 | WEB | FOUND | - | - | site:microsoft.com Russia Paris Olympics influence campaign Storm-1679 2024 France
QRY-009 | WEB | FOUND | - | - | "RRN" VIGINUM audience impressions France 2023 Doppelganger views
QRY-010 | WEB | FOUND | - | - | "Doppelganger" France audience impressions Meta Adversarial Threat Report
QRY-011 | WEB | FOUND | - | - | "Portal Kombat" audience traffic France VIGINUM pravda-fr views
QRY-012 | WEB | FOUND | - | - | "Matriochka" audience engagement France VIGINUM views
QRY-013 | WEB | FOUND | - | - | "Storm-1516" France VIGINUM audience impact 2025
QRY-014 | WEB | FOUND | - | - | "Paris 2024" Russian influence audience VIGINUM impact
QRY-015 | WEB | FOUND | - | - | site:consilium.europa.eu "Doppelganger" "Social Design Agency" "Structura"
QRY-016 | WEB | FOUND | - | - | site:eur-lex.europa.eu "Social Design Agency" Structura Doppelganger sanctions
QRY-017 | WEB | FOUND | - | - | site:consilium.europa.eu "Social Design Agency" "Structura" "Doppelganger" Russia sanctions 2024
QRY-018 | WEB | FOUND | - | - | site:home.treasury.gov Social Design Agency Structura Doppelganger September 2024
QRY-019 | WEB | FOUND | - | - | site:justice.gov Doppelganger Social Design Agency Structura domains 2024 affidavit
QRY-020 | WEB | FOUND | - | - | site:about.fb.com "Doppelganger" Russia France coordinated inauthentic behavior 2024
QRY-021 | WEB | FOUND | - | - | site:blog.google threat analysis group Doppelganger Russia France 2024
QRY-022 | WEB | FOUND | - | - | site:microsoft.com "Paris Olympics" Russian influence campaign 2024 report
QRY-023 | WEB | FOUND | - | - | "Operation Overload" Check First Reset report 2024 Matryoshka fact-checkers audience
QRY-024 | WEB | FOUND | - | - | site:france24.com fake websites Russian Doppelganger France traffic influence Viginum
QRY-025 | WEB | FOUND | - | - | site:about.fb.com/news/2024 Russia Doppelganger takedown France influence operations Meta Q1 2024
QRY-026 | WEB | FOUND | - | - | site:about.fb.com/news/2023 Russia Doppelganger France threat report Meta 2023
QRY-027 | WEB | FOUND | - | - | site:transparency.meta.com "Doppelganger" Russia France threat report
QRY-028 | WEB | FOUND | - | - | site:openai.com threat intelligence report Russia influence France Storm-1516 Doppelganger 2024 2025
QRY-029 | WEB | FOUND | - | - | "Rokh Solis" Russia Russian attribution VIGINUM 2026 municipal France
QRY-030 | WEB | FOUND | - | - | "municipales 2026" Russie ingérence VIGINUM quatre opérations Russia France
QRY-031 | WEB | FOUND | - | - | "2026" "Storm-1516" France municipal elections VIGINUM Russia
QRY-032 | WEB | FOUND | - | - | "2026" "Doppelganger" France elections VIGINUM Russia
QRY-033 | WEB | FOUND | - | - | site:sgdsn.gouv.fr/files/files/viginum/Publications 20260611 municipales Storm-1679 Matriochka audience limitée visibility France elections 2026
QRY-034 | WEB | FOUND | - | - | site:sgdsn.gouv.fr/files/files/Publications 20250507 Storm-1516 GRU 29155 Centre expertise géopolitique attribution
QRY-035 | WEB | FOUND | - | - | site:home.treasury.gov Storm-1516 GRU 29155 Center for Geopolitical Expertise Russia sanctions 2024 2025
QRY-036 | WEB | FOUND | - | - | site:state.gov Storm-1516 GRU 29155 Center for Geopolitical Expertise Russia influence
QRY-037 | WEB | FOUND | - | - | site:openai.com influence operations Russia Storm-1516 France 2024 report
QRY-038 | WEB | FOUND | - | - | site:openai.com "Doppelganger" Russia influence operation 2024 2025
QRY-039 | WEB | FOUND | - | - | site:home.treasury.gov "Center for Geopolitical Expertise" Russia influence sanctions 2024
QRY-040 | WEB | FOUND | - | - | site:home.treasury.gov "Social Design Agency" Structura Russia influence sanctions 2024
QRY-041 | WEB | FOUND | - | - | site:consilium.europa.eu "Social Design Agency" Russia destabilising activities 2024
QRY-042 | WEB | FOUND | - | - | site:eur-lex.europa.eu "Ilya Gambashidze" "Social Design Agency" "Structura" Russia 2024
QRY-043 | WEB | FOUND | - | - | site:sgdsn.gouv.fr VIGINUM trois ans opérations informationnelles russes capacité influencer opinion limitée Matriochka 2025
QRY-044 | FETCH | FOUND | SRC-001 | https://www.sgdsn.gouv.fr/viginum/publications/rrn-une-campagne-numerique-de-manipulation-de-linformation-complexe-et | inspect VIGINUM RRN France technical summary
QRY-045 | FETCH | FOUND | SRC-002 | https://www.sgdsn.gouv.fr/files/files/20240212_NP_SGDSN_VIGINUM_RAPPORT-RESEAU-PORTAL-KOMBAT_VF.pdf | inspect VIGINUM Portal Kombat technical report
QRY-046 | FETCH | FOUND | SRC-003 | https://www.sgdsn.gouv.fr/publications/matriochka-une-campagne-prorusse-ciblant-les-medias-et-la-communaute-des-fact-checkers | inspect VIGINUM Matriochka report
QRY-047 | FETCH | FOUND | SRC-004 | https://www.sgdsn.gouv.fr/publications/analyse-du-mode-operatoire-informationnel-russe-storm-1516 | inspect VIGINUM Storm-1516 report
QRY-048 | FETCH | FOUND | SRC-005 | https://www.sgdsn.gouv.fr/files/files/viginum/Publications/20260611_SGDSN_VIGINUM_Rapport-public_Elections-municipales.pdf | inspect VIGINUM 2026 municipal elections report
QRY-049 | FETCH | FOUND | SRC-006 | https://www.sgdsn.gouv.fr/viginum/publications/synthese-de-la-menace-informationnelle-ayant-vise-les-jeux-olympiques-et | inspect VIGINUM Paris 2024 information threat summary
QRY-050 | FETCH | FOUND | SRC-007 | https://www.sgdsn.gouv.fr/viginum/publications/guerre-en-ukraine-trois-annees-doperations-informationnelles-russes | inspect VIGINUM three years Russian information operations synthesis
QRY-051 | FETCH | FOUND | SRC-008 | https://www.sgdsn.gouv.fr/publications/storm-1516-detection-dune-operation-dingerence-numerique-etrangere-ciblant-emmanuel | inspect VIGINUM Storm-1516 Macron February 2026 incident
QRY-052 | FETCH | FOUND | SRC-009 | https://openai.com/index/disrupting-malicious-uses-of-ai-doppelganger/ | inspect OpenAI Doppelganger disruption and impact assessment
QRY-053 | FETCH | FOUND | SRC-010 | https://about.fb.com/news/2022/11/metas-adversarial-threat-report-q3-2022/ | inspect Meta Q3 2022 Russian CIB network targeting France
QRY-054 | FETCH | FOUND | SRC-011 | https://blog.google/threat-analysis-group/tag-bulletin-q3-2024/ | inspect Google TAG Q3 2024 Russia-linked French-language campaigns
QRY-055 | FETCH | FOUND | SRC-012 | https://www.justice.gov/usao-edpa/pr/justice-department-disrupts-covert-russian-government-sponsored-foreign-malign | inspect DOJ Doppelganger disruption attribution
QRY-056 | FETCH | FOUND | SRC-013 | https://home.treasury.gov/news/press-releases/jy2195 | inspect US Treasury SDA Structura Kremlin-directed influence sanctions
QRY-057 | FETCH | FOUND | SRC-014 | https://www.consilium.europa.eu/fr/press/press-releases/2023/07/28/information-manipulation-in-russia-s-war-of-aggression-against-ukraine-eu-lists-seven-individuals-and-five-entities/ | inspect EU Council RRN sanctions SDA Structura
QRY-058 | FETCH | FOUND | SRC-015 | https://checkfirst.network/operation-overload-how-pro-russian-actors-flood-newsrooms-with-fake-content-and-seek-to-divert-their-efforts/ | inspect Check First Operation Overload targeting France and fact-checkers
QRY-059 | FETCH | FOUND | SRC-016 | https://blogs.microsoft.com/on-the-issues/2024/06/02/russia-cyber-bots-disinformation-2024-paris-olympics/ | inspect Microsoft Russia Paris Olympics influence activity
QRY-060 | FETCH | FOUND | SRC-017 | https://www.sgdsn.gouv.fr/files/files/Publications/20250224_TLP-CLEAR_NP_SGDSN_VIGINUM_Guerre%20en%20Ukraine_Trois%20ann%C3%A9es%20d'op%C3%A9rations%20informationnelles%20russes_1.0_VF.pdf | inspect VIGINUM three-year synthesis PDF impact sections
QRY-061 | WEB | FOUND | - | - | site:sgdsn.gouv.fr/files Storm-1516 29155 unable to confirm direct involvement Khoroshenky 2025 VIGINUM PDF
QRY-062 | FETCH | FOUND | SRC-018 | https://www.sgdsn.gouv.fr/files/2025-05/20250507_TLP-CLEAR_NP_SGDSN_VIGINUM_Rapport%20technique_Storm-1516.pdf | inspect VIGINUM Storm-1516 technical PDF attribution section 4.4
QRY-063 | WEB | FOUND | - | - | "Doppelganger" Russia attribution disputed alternative attribution Social Design Agency
QRY-064 | WEB | FOUND | - | - | "Social Design Agency" Structura Doppelganger attribution dispute independent operator
QRY-065 | FETCH | FOUND | SRC-019 | https://www.disinfo.eu/doppelganger | inspect EU DisinfoLab original Doppelganger attribution limits
QRY-066 | WEB | FOUND | - | - | REFUTATION doppelganger france targeting Russia origin alternative attribution evidence
QRY-067 | WEB | FOUND | - | - | REFUTATION sda structura state direction Doppelganger independent operator alternative attribution evidence
QRY-068 | WEB | FOUND | - | - | site:lemonde.fr août 2026 Attal Glucksmann Philippe Matriochka Storm-1516 VIGINUM
QRY-069 | FETCH | FOUND | SRC-020 | https://www.lemonde.fr/politique/article/2026/08/07/presidentielle-2027-glucksmann-attal-philippe-les-ingerences-russes-s-invitent-dans-la-campagne_6740451_823448.html | inspect Le Monde August 2026 VIGINUM-targeted presidential candidates and reported visibility

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | VIGINUM-RRN-2023-06-13 | RRN : une campagne numérique de manipulation de l’information complexe et persistante | 2023-06-13 | 2026-09-06 | HTML lines 18-34 | https://www.sgdsn.gouv.fr/viginum/publications/rrn-une-campagne-numerique-de-manipulation-de-linformation-complexe-et
SRC-002 | ◈ | fam:A | VIGINUM-PORTAL-KOMBAT-2024-02-12 | Portal Kombat — Un réseau structuré et coordonné de propagande prorusse | 2024-02-12 | 2026-09-06 | PDF pp.2-8; audience p.6 + footnote 17 | https://www.sgdsn.gouv.fr/files/files/20240212_NP_SGDSN_VIGINUM_RAPPORT-RESEAU-PORTAL-KOMBAT_VF.pdf
SRC-003 | ◈ | fam:A | VIGINUM-MATRIOCHKA-2024-06-10 | Matriochka : une campagne prorusse ciblant les médias et la communauté des fact-checkers | 2024-06-10 | 2026-09-06 | HTML lines 12-19 | https://www.sgdsn.gouv.fr/publications/matriochka-une-campagne-prorusse-ciblant-les-medias-et-la-communaute-des-fact-checkers
SRC-004 | ◈ | fam:A | VIGINUM-STORM1516-2025-05-06 | Analyse du mode opératoire informationnel russe Storm-1516 | 2025-05-06 | 2026-09-06 | HTML lines 12-17; impact paragraph in page text | https://www.sgdsn.gouv.fr/publications/analyse-du-mode-operatoire-informationnel-russe-storm-1516
SRC-005 | ◈ | fam:A | VIGINUM-MUNICIPALES-2026-06-11 | Protection du débat public contre les ingérences numériques étrangères durant les élections municipales de 2026 | 2026-06-11 | 2026-09-06 | PDF pp.8-10 and p.20 impact methodology | https://www.sgdsn.gouv.fr/files/files/viginum/Publications/20260611_SGDSN_VIGINUM_Rapport-public_Elections-municipales.pdf
SRC-006 | ◈ | fam:A | VIGINUM-PARIS2024-2024-09-13 | Synthèse de la menace informationnelle ayant visé les Jeux Olympiques et Paralympiques de Paris 2024 | 2024-09-13 | 2026-09-06 | HTML lines 14-23 | https://www.sgdsn.gouv.fr/viginum/publications/synthese-de-la-menace-informationnelle-ayant-vise-les-jeux-olympiques-et
SRC-007 | ◈ | fam:A | VIGINUM-RUSSIA-3Y-2025-02-24 | Guerre en Ukraine : trois années d’opérations informationnelles russes | 2025-02-24 | 2026-09-06 | HTML lines 14-25; Matriochka impact in linked report | https://www.sgdsn.gouv.fr/viginum/publications/guerre-en-ukraine-trois-annees-doperations-informationnelles-russes
SRC-008 | ◈ | fam:A | VIGINUM-STORM1516-MACRON-2026-02-06 | Storm-1516 : détection d’une opération d’ingérence numérique étrangère ciblant Emmanuel Macron | 2026-02-06 | 2026-09-06 | HTML publication summary | https://www.sgdsn.gouv.fr/publications/storm-1516-detection-dune-operation-dingerence-numerique-etrangere-ciblant-emmanuel
SRC-009 | ◉ | fam:other:openai | OPENAI-DOPPELGANGER-2024-05-01 | Operation Doppelganger: Russian influence activity targeting Ukraine | 2024-05-01 | 2026-09-06 | HTML lines 25-52 | https://openai.com/index/disrupting-malicious-uses-of-ai-doppelganger/
SRC-010 | ◉ | fam:other:meta | META-ATR-Q3-2022 | Meta’s Adversarial Threat Report, Third Quarter 2022 | 2022-11-22 | 2026-09-06 | HTML lines 239-270 | https://about.fb.com/news/2022/11/metas-adversarial-threat-report-q3-2022/
SRC-011 | ◉ | fam:other:google | GOOGLE-TAG-Q3-2024 | TAG Bulletin: Q3 2024 | 2024-09-12 | 2026-09-06 | HTML lines 226-260 | https://blog.google/threat-analysis-group/tag-bulletin-q3-2024/
SRC-012 | ◈ | fam:other:us-doj | USDOJ-DOPPELGANGER-2024-09-04 | Justice Department Disrupts Covert Russian Government-Sponsored Foreign Malign Influence Operation | 2024-09-04 | 2026-09-06 | HTML lines 40-58 | https://www.justice.gov/usao-edpa/pr/justice-department-disrupts-covert-russian-government-sponsored-foreign-malign
SRC-013 | ◈ | fam:other:us-treasury | USTREASURY-JY2195-2024-03-20 | Treasury Sanctions Actors Supporting Kremlin-Directed Malign Influence Efforts | 2024-03-20 | 2026-09-06 | HTML lines 330-347 | https://home.treasury.gov/news/press-releases/jy2195
SRC-014 | ◈ | fam:other:eu-council | EU-COUNCIL-RRN-2023-07-28 | Manipulation de l’information dans la guerre d’agression de la Russie contre l’Ukraine : l’UE inscrit sept personnes et cinq entités | 2023-07-28 | 2026-09-06 | HTML lines 34-43 | https://www.consilium.europa.eu/fr/press/press-releases/2023/07/28/information-manipulation-in-russia-s-war-of-aggression-against-ukraine-eu-lists-seven-individuals-and-five-entities/
SRC-015 | ◉ | fam:D | CHECKFIRST-OVERLOAD-2024-06-04 | Operation Overload: how pro-Russian actors flood newsrooms with fake content and seek to divert their efforts | 2024-06-04 | 2026-09-06 | HTML lines 0-17 | https://checkfirst.network/operation-overload-how-pro-russian-actors-flood-newsrooms-with-fake-content-and-seek-to-divert-their-efforts/
SRC-016 | ◉ | fam:other:microsoft | MICROSOFT-PARIS2024-2024-06-02 | How Russia is trying to disrupt the 2024 Paris Olympic Games | 2024-06-02 | 2026-09-06 | HTML lines 6-31 | https://blogs.microsoft.com/on-the-issues/2024/06/02/russia-cyber-bots-disinformation-2024-paris-olympics/
SRC-017 | ◈ | fam:A | VIGINUM-RUSSIA-3Y-PDF-2025-02-24 | Guerre en Ukraine — Trois années d’opérations informationnelles russes (PDF) | 2025-02-24 | 2026-09-06 | PDF pp.3-6; Matriochka impact p.6 | https://www.sgdsn.gouv.fr/files/files/Publications/20250224_TLP-CLEAR_NP_SGDSN_VIGINUM_Guerre%20en%20Ukraine_Trois%20ann%C3%A9es%20d'op%C3%A9rations%20informationnelles%20russes_1.0_VF.pdf
SRC-018 | ◈ | fam:A | VIGINUM-STORM1516-PDF-2025-05-07 | Analyse du mode opératoire informationnel russe Storm-1516 — rapport technique PDF | 2025-05-07 | 2026-09-06 | PDF p.29, section 4.4; pp.3-6 for targeting | https://www.sgdsn.gouv.fr/files/2025-05/20250507_TLP-CLEAR_NP_SGDSN_VIGINUM_Rapport%20technique_Storm-1516.pdf
SRC-019 | ◉ | fam:D | EUDISINFOLAB-DOPPELGANGER-2022-09-27 | Doppelganger – Media clones serving Russian propaganda | 2022-09-27 | 2026-09-06 | HTML lines 44-75 | https://www.disinfo.eu/doppelganger
SRC-020 | ◉ | fam:D | LEMONDE-INGERENCES-2026-08-07 | Présidentielle 2027 : Glucksmann, Attal, Philippe… les ingérences russes s’invitent dans la campagne | 2026-08-07 | 2026-09-06 | HTML lines 323-353 | https://www.lemonde.fr/politique/article/2026/08/07/presidentielle-2027-glucksmann-attal-philippe-les-ingerences-russes-s-invitent-dans-la-campagne_6740451_823448.html

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.sgdsn.gouv.fr/viginum/publications/rrn-une-campagne-numerique-de-manipulation-de-linformation-complexe-et | A,D,other:eu-council,other:meta | 2022-09/2023-06 | doppelganger-france-targeting | Un réseau d’influence d’origine russe connu comme RRN/Doppelganger a ciblé la France en usurpant des médias et en amplifiant des contenus sur plusieurs plateformes. | -
FCT-002 | FACT | ✧ | https://www.sgdsn.gouv.fr/viginum/publications/rrn-une-campagne-numerique-de-manipulation-de-linformation-complexe-et | A | 2023-06-13 | rrn-spoofed-domains-fr | VIGINUM a détecté 355 domaines usurpant des médias dans RRN; quatre imitaient spécifiquement 20 Minutes, Le Monde, Le Parisien et Le Figaro, avec au moins 58 articles. | -
FCT-003 | FACT | ✦ | https://home.treasury.gov/news/press-releases/jy2195 | other:eu-council,other:meta,other:us-doj,other:us-treasury | 2022/2024 | sda-structura-state-direction | SDA et Structura ont été reliées à Doppelganger/RRN par Meta et l’Union européenne; le Trésor américain et le DOJ les décrivent comme opérant une campagne d’influence sous direction ou pour le compte d’autorités russes. | -
FCT-004 | FACT | ✧ | https://www.sgdsn.gouv.fr/files/files/20240212_NP_SGDSN_VIGINUM_RAPPORT-RESEAU-PORTAL-KOMBAT_VF.pdf | A | 2023-09/2024-02 | portal-kombat-france-infrastructure | Portal Kombat comptait au moins 193 sites; l’écosystème pravda incluait pravda-fr destiné à la France et partageait infrastructure, automatisation et techniques SEO. | -
FCT-005 | FACT | ✧ | https://www.sgdsn.gouv.fr/files/files/20240212_NP_SGDSN_VIGINUM_RAPPORT-RESEAU-PORTAL-KOMBAT_VF.pdf | A | 2023-11 | portal-kombat-france-audience | Selon Similarweb cité par VIGINUM, pravda-fr a reçu environ 10 700 visites en novembre 2023, le niveau le plus faible des cinq portails pravda occidentaux étudiés; leur moyenne était environ 31 000 visites. | -
FCT-006 | FACT | ✧ | https://www.sgdsn.gouv.fr/files/files/20240212_NP_SGDSN_VIGINUM_RAPPORT-RESEAU-PORTAL-KOMBAT_VF.pdf | A | 2023-06/2023-09 | portal-kombat-output-engagement | Les cinq portails pravda ont publié 152 464 articles en moins de trois mois, tandis que VIGINUM décrit sur VK et Telegram une volumétrie d’engagement excessivement faible voire nulle. | -
FCT-007 | FACT | ✧ | https://www.sgdsn.gouv.fr/publications/matriochka-une-campagne-prorusse-ciblant-les-medias-et-la-communaute-des-fact-checkers | A | 2023-09/2024-06 | matriochka-france-targeting | Matriochka diffuse de faux contenus de façon coordonnée auprès de médias, personnalités et fact-checkers dans plus de soixante pays; elle cible notamment la politique française, des personnalités françaises et Paris 2024. | -
FCT-008 | FACT | ✧ | https://checkfirst.network/operation-overload-how-pro-russian-actors-flood-newsrooms-with-fake-content-and-seek-to-divert-their-efforts/ | D | 2024-06 | operation-overload-workload | Check First a documenté plus de 800 organisations ciblées, près de 2 400 tweets, plus de 200 emails ciblés et plus de 250 articles de fact-check/debunk mentionnant les faux contenus; la France figure parmi les principales cibles. | -
FCT-009 | EVIDENCE | ✧ | https://www.sgdsn.gouv.fr/files/files/Publications/20250224_TLP-CLEAR_NP_SGDSN_VIGINUM_Guerre%20en%20Ukraine_Trois%20ann%C3%A9es%20d'op%C3%A9rations%20informationnelles%20russes_1.0_VF.pdf | A | 2025-02-24 | matriochka-impact-limit | VIGINUM estime que la capacité de Matriochka à façonner l’opinion demeure très limitée et que le succès de certaines opérations repose surtout sur l’attention médiatique obtenue. | -
FCT-010 | FACT | ✧ | https://www.sgdsn.gouv.fr/publications/analyse-du-mode-operatoire-informationnel-russe-storm-1516 | A | 2023-08/2025-03 | storm1516-77-operations | VIGINUM a analysé 77 opérations imputées à Storm-1516 jusqu’au 5 mars 2025; le MOI a ciblé des audiences occidentales dont françaises et repose sur un réseau coordonné et évolutif. | -
FCT-011 | EVIDENCE | ✧ | https://www.sgdsn.gouv.fr/publications/analyse-du-mode-operatoire-informationnel-russe-storm-1516 | A | 2025-05-06 | storm1516-impact-uncertain | VIGINUM indique que l’impact réel de Storm-1516 sur le débat public numérique reste difficile à estimer, tout en observant certaines opérations très visibles et parfois reprises par des responsables politiques. | -
FCT-012 | FACT | ✧ | https://www.sgdsn.gouv.fr/files/2025-05/20250507_TLP-CLEAR_NP_SGDSN_VIGINUM_Rapport%20technique_Storm-1516.pdf | A | 2024-06 | storm1516-fr-legislative-copycop | Après la dissolution de juin 2024, un domaine ensemble-24.fr lié à CopyCop a usurpé l’identité de la coalition Ensemble et proposé une fausse prime de 100 euros en échange d’une voix et d’un numéro de sécurité sociale. | -
FCT-013 | FACT | ✧ | https://www.sgdsn.gouv.fr/files/files/viginum/Publications/20260611_SGDSN_VIGINUM_Rapport-public_Elections-municipales.pdf | A | 2025-02/2026-03 | copycop-municipal-domains-effect | Plus de cent domaines en .fr imitant des sites de presse locaux ont été prépositionnés par CopyCop; durant les municipales 2026, la plupart ont été suspendus par l’Afnic et VIGINUM indique que l’opération n’a pas eu d’effet significatif. | -
FCT-014 | FACT | ✧ | https://www.sgdsn.gouv.fr/files/files/viginum/Publications/20260611_SGDSN_VIGINUM_Rapport-public_Elections-municipales.pdf | A | 2026-03 | storm1516-bournazel-limited-audience | Une opération Storm-1516/CopyCop visant Pierre-Yves Bournazel pendant les municipales 2026 a atteint une audience limitée, bien inférieure à d’autres opérations antérieures ciblant la France. | -
FCT-015 | FACT | ✧ | https://www.sgdsn.gouv.fr/files/files/viginum/Publications/20260611_SGDSN_VIGINUM_Rapport-public_Elections-municipales.pdf | A | 2026-01/2026-03 | storm1679-matriochka-municipal | VIGINUM a détecté sept opérations imputées à Storm-1679 et Matriochka visant les municipales 2026 par de faux reportages usurpant des médias et institutions français. | -
FCT-016 | EVIDENCE | ✧ | https://www.sgdsn.gouv.fr/files/files/viginum/Publications/20260611_SGDSN_VIGINUM_Rapport-public_Elections-municipales.pdf | A | 2026-06-11 | storm1516-gru29155-claim-2026 | Le rapport VIGINUM de juin 2026 présente Storm-1516 comme attribué à l’unité 29155 du GRU avec l’appui du Centre d’expertise géopolitique. | -
FCT-017 | EVIDENCE | ✧ | https://www.sgdsn.gouv.fr/files/2025-05/20250507_TLP-CLEAR_NP_SGDSN_VIGINUM_Rapport%20technique_Storm-1516.pdf | A | 2025-05-07 | storm1516-gru29155-limit-2025 | Le rapport technique VIGINUM de mai 2025 indiquait ne pas être en mesure de confirmer l’implication directe de l’unité 29155 ou de Youry Khoroshenky dans la conduite de Storm-1516, malgré des liens étroits relevés. | -
FCT-018 | FACT | ✧ | https://openai.com/index/disrupting-malicious-uses-of-ai-doppelganger/ | other:openai | 2024-05 | doppelganger-openai-france-impact | OpenAI a identifié des usages de ses modèles par Doppelganger pour produire ou corriger du contenu en français; les campagnes détectées n’ont pas obtenu d’engagement positif authentique substantiel selon son évaluation. | -
FCT-019 | FACT | ✧ | https://about.fb.com/news/2022/11/metas-adversarial-threat-report-q3-2022/ | other:meta | 2022-09/2022-12 | meta-doppelganger-france | Meta a supprimé 1 633 comptes, 703 Pages, un groupe et 29 comptes Instagram d’un réseau originaire de Russie ciblant principalement l’Allemagne mais aussi la France; il reposait sur de faux sites imitant des médias. | -
FCT-020 | FACT | ✧ | https://blog.google/threat-analysis-group/tag-bulletin-q3-2024/ | other:google | 2024-Q3 | google-russia-france-enforcement | Google TAG a bloqué ou supprimé plusieurs domaines, chaînes YouTube et comptes publicitaires liés à des opérations russes diffusant du contenu en français; plusieurs lots étaient explicitement reliés à Doppelganger. | -
FCT-021 | FACT | ✧ | https://blogs.microsoft.com/on-the-issues/2024/06/02/russia-cyber-bots-disinformation-2024-paris-olympics/ | other:microsoft | 2023-06/2024-06 | russia-paris2024-storm1679 | Microsoft a documenté Storm-1679 et Doppelganger/Storm-1099 ciblant Paris 2024 avec de faux contenus sur la violence, la sécurité et l’IOC, y compris des usurpations de médias français. | -
FCT-022 | EVIDENCE | ✧ | https://www.sgdsn.gouv.fr/files/files/Publications/20250224_TLP-CLEAR_NP_SGDSN_VIGINUM_Guerre%20en%20Ukraine_Trois%20ann%C3%A9es%20d'op%C3%A9rations%20informationnelles%20russes_1.0_VF.pdf | A | 2022/2025 | russian-operations-reach-limit | Dans sa synthèse 2025, VIGINUM considère que la portée des campagnes russes présentées reste relativement limitée, malgré des moyens importants et quelques exceptions virales. | -
FCT-023 | EVIDENCE | ✧ | https://www.sgdsn.gouv.fr/files/files/viginum/Publications/20260611_SGDSN_VIGINUM_Rapport-public_Elections-municipales.pdf | A | 2026-06-11 | impact-methodology-visibility-not-effect | Le rapport municipal 2026 souligne que vues, likes et autres métriques de visibilité ne suffisent pas à mesurer des effets sociologiques, politiques ou économiques et requiert une évaluation prudente multi-indicateurs. | -
FCT-024 | FACT | ✧ | https://www.sgdsn.gouv.fr/publications/storm-1516-detection-dune-operation-dingerence-numerique-etrangere-ciblant-emmanuel | A | 2026-02-04/2026-02-06 | storm1516-macron-2026 | VIGINUM a imputé avec une confiance élevée à Storm-1516, avec soutien technique de CopyCop, une fausse vidéo ciblant Emmanuel Macron diffusée en février 2026. | -
FCT-025 | EVIDENCE | ✧ | https://www.disinfo.eu/doppelganger | D | 2022-09-27 | doppelganger-early-attribution-limit | En septembre 2022, EU DisinfoLab établissait une opération Russia-based mais ne formulait pas d’attribution spécifique concluante et indiquait ne pas pouvoir exclure entièrement un false flag; des attributions plus précises sont intervenues ultérieurement. | -
FCT-026 | FACT | ✧ | https://www.lemonde.fr/politique/article/2026/08/07/presidentielle-2027-glucksmann-attal-philippe-les-ingerences-russes-s-invitent-dans-la-campagne_6740451_823448.html | D | 2026-07/08 | pre2027-france-targeting-low-reach | Fin juillet-début août 2026, Le Monde rapporte, sur la base d’alertes VIGINUM, des campagnes attribuées à Storm-1516 et Matriochka visant Edouard Philippe, Raphaël Glucksmann et Gabriel Attal; les contenus sont décrits comme ayant un très faible retentissement sur le débat public. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-010,SRC-014,SRC-019
FCT-002 | SRC-001
FCT-003 | SRC-010,SRC-012,SRC-013,SRC-014
FCT-004 | SRC-002
FCT-005 | SRC-002
FCT-006 | SRC-002
FCT-007 | SRC-003
FCT-008 | SRC-015
FCT-009 | SRC-017
FCT-010 | SRC-004,SRC-018
FCT-011 | SRC-004
FCT-012 | SRC-018
FCT-013 | SRC-005
FCT-014 | SRC-005
FCT-015 | SRC-005
FCT-016 | SRC-005
FCT-017 | SRC-018
FCT-018 | SRC-009
FCT-019 | SRC-010
FCT-020 | SRC-011
FCT-021 | SRC-016
FCT-022 | SRC-017
FCT-023 | SRC-005
FCT-024 | SRC-008
FCT-025 | SRC-019
FCT-026 | SRC-020

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-066 | NONE
FCT-003 | QRY-067 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:CONFIRME
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE
FCT-008 | ELIGIBLE:VERIFIE
FCT-009 | SKIP:NOT_ELIGIBLE
FCT-010 | ELIGIBLE:VERIFIE
FCT-011 | SKIP:NOT_ELIGIBLE
FCT-012 | ELIGIBLE:VERIFIE
FCT-013 | ELIGIBLE:VERIFIE
FCT-014 | ELIGIBLE:VERIFIE
FCT-015 | ELIGIBLE:VERIFIE
FCT-016 | SKIP:NOT_ELIGIBLE
FCT-017 | SKIP:NOT_ELIGIBLE
FCT-018 | ELIGIBLE:VERIFIE
FCT-019 | ELIGIBLE:VERIFIE
FCT-020 | ELIGIBLE:VERIFIE
FCT-021 | ELIGIBLE:VERIFIE
FCT-022 | SKIP:NOT_ELIGIBLE
FCT-023 | SKIP:NOT_ELIGIBLE
FCT-024 | ELIGIBLE:VERIFIE
FCT-025 | SKIP:NOT_ELIGIBLE
FCT-026 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -
FCT-007 | WRITE | -
FCT-008 | WRITE | -
FCT-010 | WRITE | -
FCT-012 | WRITE | -
FCT-013 | WRITE | -
FCT-014 | WRITE | -
FCT-015 | WRITE | -
FCT-018 | WRITE | -
FCT-019 | WRITE | -
FCT-020 | WRITE | -
FCT-021 | WRITE | -
FCT-024 | WRITE | -
FCT-026 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8
CP-003 | SEARCH:INV-022 | PASS | LAST_COMPLETED:9:INV-022 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL:CAU-006 | PASS | LAST_COMPLETED:11:CAU-006 | NEXT_ACTION:12
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-06T09:59:11.578374+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:CONFIRME","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":19,"eligible":19,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:19;attempted:0;success:0;failure:0;blocked:19} | WRITEBACK_EXECUTION_V1:[19 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-002 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-003 | ELIGIBLE:CONFIRME | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-004 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-005 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-006 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-007 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-008 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-010 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-012 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-013 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-014 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-015 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-018 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-019 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-020 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-021 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-024 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-026 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
