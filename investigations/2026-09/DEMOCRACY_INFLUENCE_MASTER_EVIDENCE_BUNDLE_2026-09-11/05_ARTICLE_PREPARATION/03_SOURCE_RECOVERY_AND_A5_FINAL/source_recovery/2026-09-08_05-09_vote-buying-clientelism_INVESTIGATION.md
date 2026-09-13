ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260908-0509-vote-buying-clientelism | PARENT_RUN_ID:NONE | AS_OF:2026-09-08
INPUT_KIND:RUN_CARD | MISSION_MODE:GREENFIELD | INPUT_REF:PATH:/mnt/data/inv098-finalreplay/exec/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-08_vote-buying-clientelism/2026-09-08_05-09_vote-buying-clientelism_INPUT.md | SUBJECT_SLUG:vote-buying-clientelism | SUBJECT_FP:sha256:8e5344b7e112cb8ba326075260022f291d614fcde0f3cbcee39ddb49b9576bd3 | INPUT_SHA256:sha256:4c6667cf6fa6510faa2e07e0d78d8ba317b2b1e902bae8c6d195dc679a2d6f4a
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France 2000-2026; distinguish direct vote buying, political clientelism, patronage, distributive favoritism and ordinary targeted public policy; international comparators only for isomorphic methods/mechanisms.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/MONEY.md,clusters/POWER.md,clusters/NETWORK.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
## Question et résultat

L’enquête distingue trois objets qui sont souvent fusionnés : l’achat direct de votes, le clientélisme politique et l’allocation électoraliste de ressources publiques. Le premier est juridiquement défini et établi dans plusieurs cas français. Le deuxième est une relation personnalisée plus large, souvent durable, dans laquelle biens, services ou protection sont échangés contre un soutien politique. Le troisième est observable dans plusieurs travaux quantitatifs français sous forme de favoritisme, de pork-barrel ou de ciblage budgétaire lié aux incitations électorales. Ces trois objets peuvent se recouvrir, mais ils ne sont pas probatoirement interchangeables.

Le plafond probatoire est donc asymétrique : l’existence de mécanismes directs d’inducement électoral est établie au niveau de cas ; des mécanismes de favoritisme et d’allocation électoraliste sont également mesurés ; en revanche, le corpus ne permet ni d’estimer une prévalence nationale de l’achat de votes ou du clientélisme, ni de démontrer une architecture nationale coordonnée, ni de fermer une causalité générale allant de l’avantage matériel au changement de vote puis au résultat électoral.

## Le seuil juridique français : avantage et intention d’influencer

L’article L106 du code électoral vise explicitement les dons ou libéralités en argent ou en nature, les promesses de faveurs, d’emplois et d’autres avantages particuliers lorsqu’ils sont faits en vue d’influencer le vote, d’obtenir un suffrage ou de provoquer une abstention (FCT-001, SRC-001). Le même article prévoit des sanctions pour l’auteur comme pour celui qui agrée ou sollicite l’avantage (FCT-002).

Le juge de l’élection ne se substitue pas au juge pénal : il recherche si des pressions correspondant à ce schéma ont été exercées et si elles ont été de nature à altérer la sincérité du scrutin (FCT-003). Cette architecture sépare déjà trois arêtes : avantage matériel, finalité électorale, puis effet sur la sincérité ou le résultat.

## Cas positifs : argent, logement et distributions

À Corbeil-Essonnes en 2009, le Conseil d’État a tenu pour établis des dons d’argent d’une ampleur significative, persistants jusque pendant la période électorale (FCT-004, SRC-002). Il les a regardés comme capables d’affecter la libre détermination des électeurs et, compte tenu de l’écart de 170 voix, comme ayant altéré la sincérité du scrutin et vicié les résultats (FCT-005). L’ampleur exacte des dons n’était pourtant pas chiffrable précisément (FCT-006) : ce cas établit donc le mécanisme et son effet dans cette élection, pas un taux général.

En 2015 à Sainte-Suzanne, une somme d’argent et une promesse de logement remises à un assesseur ont été considérées comme destinées à influencer son vote, même sans demande explicite formulée en ces termes (FCT-007, SRC-003). Un partisan du candidat avait aussi donné de l’argent à un électeur pour l’inciter à voter pour la liste (FCT-008). Ces violations ont été établies, mais le juge n’a pas considéré qu’elles avaient altéré la sincérité du scrutin au regard de l’écart de voix (FCT-009). L’existence de l’action et le changement du résultat sont donc deux propositions distinctes.

En 2021 à Corbeil-Essonnes, des distributions répétées de colis alimentaires auxquelles participaient des candidats qui n’étaient pas habituellement engagés dans ces actions ont été regardées comme intervenues en vue de l’élection et comme capables d’affecter la libre détermination de certains électeurs (FCT-013, FCT-014, SRC-004). Là encore, l’écart de voix a empêché de conclure qu’elles avaient vicié le résultat.

## Contrôles négatifs : une politique ciblée n’est pas automatiquement un achat de voix

La jurisprudence fournit des falsificateurs importants. À Sainte-Suzanne, des allégations de distribution de matériaux n’ont pas été retenues faute de matérialité suffisante (FCT-010). Les recrutements invoqués comme avantages électoraux n’ont pas été qualifiés comme tels faute de démonstration qu’ils ne répondaient pas aux besoins de la commune ou du CCAS (FCT-011). Une prime concernant plus de 400 agents a été replacée dans la continuité d’une politique municipale antérieure et le grief d’achat de voix a été écarté (FCT-012).

À Dourdan, une distribution de 4 000 masques a été examinée sous l’angle de L106 sans être retenue comme pression ayant altéré la sincérité dans les circonstances de l’espèce (FCT-015, SRC-005). Dans une autre affaire, des aides récurrentes de 100 à 150 euros aux entreprises, un programme habituel de la CCI, un réseau wifi gratuit et une subvention de 90 000 euros correspondant à une formation réellement exécutée n’ont pas été assimilés à des promesses de dons électorales prohibées (FCT-016, FCT-017, SRC-006).

Le contrôle négatif est donc robuste : redistribution, aide ciblée, recrutement, prime ou subvention ne suffisent pas. Il faut documenter l’arête électorale et distinguer une prestation ordinaire ou préexistante d’un avantage particulier destiné à infléchir le vote.

## Le clientélisme est plus large que l’achat ponctuel de votes

L’état de l’art de l’Agence française anticorruption décrit le clientélisme ou patronage comme une relation de pouvoir asymétrique personnalisée, structurée par des échanges de services et de biens : un patron fournit protection ou ressources et reçoit un soutien en retour (FCT-018, SRC-007). Dans sa forme politique, ce soutien peut être électoral et les biens concernés peuvent être des emplois publics, un logement social ou une subvention (FCT-019). L’AFA rappelle aussi l’existence d’une littérature française de cas contemporains en Corse, à Marseille et en banlieue parisienne et souligne la variabilité des définitions (FCT-020).

Cette catégorie ne doit donc pas être réduite à L106. Un échange clientéliste peut être diffus, relationnel et inscrit dans le temps ; inversement, qualifier un phénomène de clientélisme en sciences sociales ne ferme pas automatiquement une infraction pénale ni la preuve d’un contrat individuel avantage contre vote.

## Ce que montrent les données françaises sur le favoritisme et l’électoralisme

Plusieurs travaux quantitatifs montrent que les ressources publiques peuvent suivre des connexions et incitations politiques. Fabre et Sangnier estiment que les communes dont un ministre avait auparavant été maire reçoivent environ 30 % de subventions d’investissement supplémentaires lorsqu’il entre au gouvernement, avec une baisse de taille comparable à sa sortie ; aucun effet similaire n’est observé pour les seules communes d’enfance (FCT-021, FCT-022, SRC-008). Les auteurs privilégient une lecture en termes d’influence souple, de relations adultes ou d’incitations de carrière plutôt que de simple contrôle formel de l’administration (FCT-023).

Dubois et Monnery analysent la réserve de 348 sénateurs sur 2014-2017, pour un volume annuel proche de 50 millions d’euros (FCT-024, SRC-009). Ils observent que 79 % des subventions financent des communes, que la réserve est intégralement dépensée dans le département dans 97 % des cas et qu’environ 8 % du montant annuel va au fief électoral du sénateur (FCT-025). Leur résultat général est cohérent avec des comportements stratégiques d’allocation électoraliste, sans documenter pour autant un échange individuel explicite subvention contre vote (FCT-026).

Lévêque, sur plus de 189 000 responsables politiques locaux, trouve que les familles de candidats ayant soutenu les maires élus en 2008 obtiennent 35 % de permis de construire de plus que les familles d’opposants entre 2008 et 2014 (FCT-027, SRC-010). L’écart diminue avec la concurrence politique et disparaît après des élections serrées (FCT-028). Enfin, Cassette et Farvaque mettent en évidence un cycle budgétaire : la dette moyenne sur le mandat pénalise la réélection, mais l’accumulation de dette juste avant l’élection augmente sa probabilité (FCT-029, SRC-011). Ce dernier résultat documente un électoralisme budgétaire possible, pas un achat de votes.

## Ce que ces résultats ne permettent pas d’affirmer

Ces études ne partagent ni la même unité, ni le même mécanisme, ni la même période. Une subvention supplémentaire à une commune liée à un ministre, un fléchage vers un fief sénatorial, un permis de construire favorable à un soutien politique et une hausse de dette avant scrutin sont quatre objets différents. Ils établissent que les connexions et incitations électorales peuvent affecter l’allocation de ressources. Ils ne démontrent pas, par eux-mêmes, que chaque bénéficiaire a reçu un avantage à condition de voter d’une manière déterminée.

Le corpus ne fournit pas non plus de dénominateur national permettant d’estimer combien d’électeurs, de communes ou de scrutins sont exposés à des échanges prohibés. Les décisions de justice positives ne peuvent pas être converties en prévalence nationale. La chaîne causale générale reste ouverte après le ciblage : avantage ou ressource -> condition/attente de soutien -> exposition effective -> changement de vote -> résultat agrégé.

## Plafond probatoire

I0 — acteurs, relations juridiques et canaux d’allocation : VERIFIED.

I1 — ressources, capacité et accès discrétionnaire : VERIFIED, avec portée dépendante du mécanisme.

I2 — actions : VERIFIED pour des dons/promesses/distributions dans des cas L106 et pour des allocations différentielles mesurées dans les études.

I3 — coordination, tasking ou quid pro quo : VERIFIED seulement dans quelques cas directs ; PARTIAL ou NOT_ESTABLISHED à l’échelle générale.

I4 — exposition ou bénéfice reçu : VERIFIED case-specifically et mesuré agrégativement selon les datasets.

I5 — persuasion ou changement individuel de préférence : NOT_ESTABLISHED généralement.

I6 — changement de comportement ou résultat institutionnel : VERIFIED case-specifically pour l’altération de sincérité à Corbeil 2009 ; NOT_ESTABLISHED généralement.

I7 — résultat politique ou électoral contrefactuel national : NOT_ESTABLISHED.

La conclusion robuste est donc double : l’achat direct de votes et des formes de favoritisme ou d’électoralisme distributif existent comme mécanismes documentés en France ; leur fréquence nationale, leur articulation en architecture clientéliste générale et leur effet électoral causal agrégé restent non établis.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:5|SRC_COMPLETE:11/11

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-08
- **notes:**
  - Article L106 version in force since 2002
  - jurisprudence sampled 2009, 2015, 2016 and 2021
  - empirical studies cover municipal/senatorial data chiefly 2008-2017 and are interpreted within their publication scope
- **status:** CURRENT_THROUGH_2026
- **window:** 2000-2026

### MANIPULATION_REPORT
- **assumptions:**
  - court findings are treated as case-specific adjudicated facts, not national frequency
  - academic estimates are study-level effects with their own units
  - absence of a national denominator is not evidence of absence
- **clusters:**
  - **loaded:**
    - clusters/MONEY.md
    - clusters/POWER.md
    - clusters/NETWORK.md
- **complexity:**
  - **band:** APEX
  - **score:** 8
- **implicit:**
  - material resources can be political instruments
  - personalized exchange differs from universal program rules
  - electoral incentives may shape allocation without explicit vote contract
- **input_kind:** RUN_CARD
- **mission_mode:** GREENFIELD
- **patterns:**
  - vote inducement
  - patron-client exchange
  - electoral gift
  - pork-barrel allocation
  - political favoritism
  - electoral cycle
- **priorities:**
  - legal threshold
  - positive cases
  - negative controls
  - clientelism boundary
  - quantitative favoritism
  - prevalence and effect ceiling
- **query_guidance:** prefer French law and case law for direct inducement; use peer-reviewed quantitative work for allocation patterns; never collapse electoral targeting into quid pro quo or outcome.
- **rhetorical:**
  - **AUTH:** legal and judicial authority establishes doctrine/case facts, not prevalence
  - **BF:** case law is selected evidence, not a national denominator
  - **DEM:** local examples do not establish national architecture
  - **FAC:** separate benefit, intent, exchange, exposure, behavior and outcome
  - **NUM:** 30%, 35%, 79/97/8 and case vote margins stay bounded to source designs
- **speaker:**
  - **goal:** forensic discrimination of vote buying, clientelism and electoralist redistribution
  - **target:** advantage/resource -> exchange/targeting -> electoral support -> effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **Κ:** 4
  - **Λ:** 4
  - **Ξ:** 4
  - **Σ:** 4
  - **Φ:** 3
  - **Ψ:** 3
  - **Ω:** 4
  - **κ:** 3
  - **ρ:** 4
  - **€:** 5
  - **↕:** 5
  - **⏰:** 4
  - **⚔:** 3
  - **⫸:** 4
  - **🌐:** 5
- **threats:**
  - redistribution=vote_buying
  - targeted_policy=clientelism
  - benefit=quid_pro_quo
  - case=prevalence
  - correlation=exchange
  - material_transfer=electoral_effect

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - national denominator and transaction-level exchange records
  - **input_ids:**
    - FCT-004
    - FCT-007
    - FCT-008
    - FCT-021
    - FCT-024
    - FCT-025
    - FCT-027
  - **module:** clusters/MONEY.md
  - **negative_results:**
    - no single monetary threshold distinguishes lawful policy from vote buying
  - **not_computable:**
    - national monetary volume of vote-buying exchanges
  - **operations_applied:**
    - separated private/material inducements from public allocation mechanisms
    - tracked resource vehicle, beneficiary and electoral link
  - **reason:** central mechanisms involve cash gifts, housing, subsidies, permits and public transfers
  - **result_ids:**
    - CLM-001
    - CLM-004
    - CLM-005
    - CAU-001
  - **status:** DONE
  - **trigger:** €
- **item 2:**
  - **gaps:**
    - individual condition/expectation and responsibility chains
  - **input_ids:**
    - FCT-001
    - FCT-018
    - FCT-019
    - FCT-021
    - FCT-025
    - FCT-027
  - **module:** clusters/POWER.md
  - **negative_results:**
    - targeted policy alone does not establish clientelist control
  - **not_computable:**
    - informal expectations without records
  - **operations_applied:**
    - located benefit/control authority
    - separated capacity and discretionary allocation from proven electoral command or quid pro quo
  - **reason:** object concerns asymmetric discretion over benefits and possible exchange for political support
  - **result_ids:**
    - CLM-002
    - CLM-003
    - CLM-004
    - CTRL-003
    - CTRL-004
  - **status:** DONE
  - **trigger:** ↕
- **item 3:**
  - **gaps:**
    - comparable network-level denominator across territories
  - **input_ids:**
    - FCT-007
    - FCT-008
    - FCT-018
    - FCT-019
    - FCT-027
    - FCT-028
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no evidence of a coordinated national clientelist network architecture
  - **not_computable:**
    - unobserved informal reciprocal ties
  - **operations_applied:**
    - mapped patron/intermediary/beneficiary relations
    - kept local relational exchange distinct from transversal national architecture
  - **reason:** clientelism is relational and may involve candidate, intermediaries, beneficiaries and local political networks
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-005
    - CAU-001
  - **status:** DONE
  - **trigger:** 🌐

### SCOPING_REPORT
- **actors_institutions:**
  - Conseil d’État
  - electoral candidates and local officials
  - Agence française anticorruption
  - French municipalities
  - senators
  - central government
- **domains:**
  - electoral law
  - municipal elections
  - clientelism
  - public subsidies
  - building permits
  - political budget cycles
- **evidence_limits:**
  - no national denominator for L106 cases/exposure
  - case law is selected and not prevalence data
  - quantitative studies use different outcomes and periods
  - quid-pro-quo often unobserved in aggregate datasets
- **exclusions:**
  - generic redistribution without electoral edge
  - foreign vote buying not needed for French object
  - allegations without adjudicated or empirical support
  - national architecture inferred from local cases
- **geo:** France; comparators only method-isomorphic
- **lead_question:** Achat de votes, clientélisme et redistribution électoraliste en France
- **object_coverage:** STRONG_FOR_LEGAL_BOUNDARY_AND_CASE_SPECIFIC_EXISTENCE; MODERATE_FOR_DISTRIBUTIVE_FAVORITISM; WEAK_FOR_NATIONAL_PREVALENCE_AND_CAUSAL_ELECTORAL_EFFECT
- **object_question:** Quelles formes sont documentées, avec quelle preuve, fréquence et effet, et comment distinguer quid pro quo électoral et politique publique ciblée ?
- **period:** 2000-2026

### CREDO
- redistribution != vote_buying
- targeted_policy != clientelism
- benefit != quid_pro_quo
- allegation != proof
- conviction_or_annulment_case != prevalence
- correlation != causal_exchange
- local_case != national_architecture
- material_transfer != electoral_effect

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** GREENFIELD
- **patterns:**
  - direct inducement
  - personalized reciprocal exchange
  - discretionary public allocation
  - political connection
  - electoral timing
- **priorities:**
  - threshold
  - positive controls
  - negative controls
  - clientelism definition
  - favoritism evidence
  - effect ceiling
- **query_guidance:** separate legal inducement, social-science clientelism, distributive favoritism and voter response; do not convert one into another
- **speaker:**
  - **goal:** forensic distinction
  - **target:** resource -> electoral relation -> effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **threats:**
  - benefit=exchange
  - electoral timing=vote buying
  - local evidence=national prevalence

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** La jurisprudence écarte des primes, recrutements, aides récurrentes, subventions et certaines distributions lorsqu’un lien électoral prohibé n’est pas suffisamment établi.
  - **resolution:** L’objet probant est avantage + intention/pression électorale + contexte, puis une arête distincte vers la sincérité/résultat.
  - **thesis:** Tout avantage matériel accordé près d’une élection constitue un achat de voix.
- **item 2:**
  - **antithesis:** La littérature décrit des relations personnalisées durables et asymétriques d’échange de biens/services contre soutien politique, plus larges que L106.
  - **resolution:** Vote-buying direct est un sous-mécanisme possible; clientélisme/patronage est une catégorie relationnelle plus large et ne vaut pas qualification pénale automatique.
  - **thesis:** Le clientélisme se confond avec l’infraction ponctuelle d’achat de voix.
- **item 3:**
  - **antithesis:** Les études établissent favoritisme, connexions et cycles électoralistes, mais ne mesurent pas directement un contrat individuel avantage contre vote.
  - **resolution:** Pattern distributif = mécanisme potentiel/indice causal borné; quid pro quo et effet électoral exigent des arêtes supplémentaires.
  - **thesis:** Les écarts de subventions ou permis prouvent un échange de votes.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **boundary:** case-specific electoral inducement established in some jurisprudence
  - **from:** candidat/entourage
  - **support:**
    - FCT-004
    - FCT-007
    - FCT-008
    - FCT-013
  - **to:** électeur ou assesseur
  - **vehicle:** argent, promesse de logement ou bien matériel
- **item 2:**
  - **boundary:** 30% study-level connection effect; not individual vote exchange
  - **from:** État central
  - **support:**
    - FCT-021
    - FCT-022
    - FCT-023
  - **to:** communes liées à d’anciens maires devenus ministres
  - **vehicle:** subventions d’investissement
- **item 3:**
  - **boundary:** electoralist allocation pattern; not direct vote quid pro quo
  - **from:** sénateur via réserve
  - **support:**
    - FCT-024
    - FCT-025
    - FCT-026
  - **to:** communes/département/fief
  - **vehicle:** subventions publiques
- **item 4:**
  - **boundary:** local favoritism association; mechanism depends on political competition
  - **from:** mairie
  - **support:**
    - FCT-027
    - FCT-028
  - **to:** demandeurs de permis politiquement connectés
  - **vehicle:** permis de construire

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** candidat
  - **limits:**
    - case-specific; not prevalence
  - **relation:** don, promesse ou avantage visant le vote
  - **support:**
    - FCT-007
    - FCT-008
  - **to:** électeur/assesseur
- **item 2:**
  - **from:** patron politique
  - **limits:**
    - social-science category; legal qualification separate
  - **relation:** protection/biens/services contre soutien
  - **support:**
    - FCT-018
    - FCT-019
  - **to:** clients
- **item 3:**
  - **from:** ministre ancien maire
  - **limits:**
    - soft influence interpretation; no vote contract
  - **relation:** political connection associated with investment subsidies
  - **support:**
    - FCT-021
    - FCT-023
  - **to:** ancienne commune
- **item 4:**
  - **from:** sénateur
  - **limits:**
    - electoralist pattern; not direct quid pro quo
  - **relation:** discretionary reserve allocations
  - **support:**
    - FCT-024
    - FCT-025
    - FCT-026
  - **to:** département/fief
- **item 5:**
  - **from:** maire/majorité
  - **limits:**
    - local sample; association/interpretation not national architecture
  - **relation:** building-permit favoritism association
  - **support:**
    - FCT-027
    - FCT-028
  - **to:** supporters or families

### IMPACT_MAP
- **behavior:** NOT_ESTABLISHED generally beyond judicial inference/case context
- **electoral_effect:** CASE_SPECIFIC; general causal effect NOT_ESTABLISHED
- **free_determination:** VERIFIED case-specifically in jurisprudence as capable of being affected
- **material_access:** VERIFIED case-specifically and quantitatively for gifts/subsidies/permits
- **persuasion:** NOT_MEASURED generally
- **sincerity_of_ballot:** VERIFIED case-specifically; Corbeil 2009 altered, other cases not
- **support:**
  - FCT-005
  - FCT-009
  - FCT-014
  - FCT-021
  - FCT-027
  - FCT-029

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** routine recruitment, bonuses, recurrent aid, grants or masks can fail the threshold
  - **issue:** benefit versus electoral inducement
  - **pro:** direct money/housing/food cases can be electoral pressure
  - **resolution:** benefit alone is insufficient; electoral purpose/pressure and context are required
  - **support:**
    - FCT-007
    - FCT-013
    - FCT-011
    - FCT-012
    - FCT-015
    - FCT-016
    - FCT-017
- **item 2:**
  - **contra:** their outcomes do not observe individual vote contracts
  - **issue:** electoralist allocation versus quid pro quo
  - **pro:** multiple studies find strategic or connection-linked allocation patterns
  - **resolution:** favoritism/electoralism supported; direct clientelist exchange remains a separate evidentiary edge
  - **support:**
    - FCT-021
    - FCT-025
    - FCT-026
    - FCT-027
    - FCT-028
    - FCT-029
- **item 3:**
  - **contra:** Sainte-Suzanne 2015 and Corbeil 2021 found violations/electoral distributions without result invalidation
  - **issue:** violation or pressure versus changed election result
  - **pro:** Corbeil 2009 led to annulment
  - **resolution:** effect on result is case-specific and depends on extent/context/vote margin
  - **support:**
    - FCT-005
    - FCT-009
    - FCT-014

### VERIFICATION_REPORT
- **circular_families:**
  - A contains multiple Conseil d’État/Legifrance sources and is treated as one provenance family for independence
- **contradiction_ids:**
  - benefit-vs-inducement
  - electoralism-vs-quidproquo
  - violation-vs-result
- **downgraded_ids:**
  - NONE
- **none_found_claims:**
  - national prevalence of L106 vote buying
  - general national coordinated clientelist architecture
  - general causal voter persuasion from material benefits
- **remaining_gaps:**
  - national denominator of cases/exposure
  - transaction-level quid-pro-quo evidence in aggregate studies
  - causal exposure -> vote change -> counterfactual outcome
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
- **sources_reopened:** 11
- **upgraded_ids:**
  - NONE
- **verdict:** READY_FOR_PRE_GATE

### EDI_REPORT
- **corpus:**
  - **circularity:** CONTROLLED; court decisions not counted as independent families from one another
  - **coverage:** STRONG_FOR_EXISTENCE_AND_BOUNDARIES; MODERATE_FOR_FAVORITISM; WEAK_FOR_PREVALENCE_AND_GENERAL_EFFECT
  - **independence:** COURT_FAMILY_PLUS_FIVE_OTHER_PROVENANCE_FAMILIES
  - **limits:**
    - selected jurisprudence not census
    - academic designs differ
    - no common national denominator
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES_CASE_SPECIFIC
    - **gap_type:** SCOPE
    - **independent_families:** 1
  - **item 2:**
    - **claim_id:** CLM-003
    - **direct_object:** YES_NEGATIVE_CONTROLS
    - **gap_type:** NONE
    - **independent_families:** 1
  - **item 3:**
    - **claim_id:** CLM-004
    - **direct_object:** YES_MULTI_STUDY
    - **gap_type:** CAUSALITY
    - **independent_families:** 4
  - **item 4:**
    - **claim_id:** CLM-005
    - **direct_object:** CAUSAL_BOUNDARY
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 4
  - **item 5:**
    - **claim_id:** CLM-006
    - **direct_object:** CASE_SPECIFIC_EFFECT
    - **gap_type:** CAUSALITY
    - **independent_families:** 2
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** 6_PROVENANCE_FAMILIES
  - **perspective:** LAW+COURTS+AFA+ECONOMICS+PUBLIC_ADMINISTRATION
  - **stratification:** DIRECT_INDUCEMENT+CLIENTELISM+PORK+FAVORITISM+ELECTORAL_CYCLE
  - **temporal:** case law 2009-2021; empirical datasets mainly 2008-2017; current legal rule checked 2026
- **edi:**
  - **assessment:** STRONG_LEGAL_CASE_BOUNDARY_PLUS_MULTIPLE_INDEPENDENT_EMPIRICAL_FAMILIES
  - **flags:**
    - OFFICIAL_LAW_AND_CASELAW
    - NEGATIVE_CONTROLS
    - PEER_REVIEWED_DISTRIBUTIVE_STUDIES
    - NO_NATIONAL_PREVALENCE_DENOMINATOR
- **source_counts:**
  - **primary:** 6
  - **provenance_families:** 6
  - **secondary:** 5
  - **tertiary:** 0
  - **total:** 11

### RESPONSIBILITY_MAP
- **boundary:** benefit, discretion, targeting, connection and electoral timing do not by themselves establish an exchange contract or voter response
- **not_established:**
  - general national quid-pro-quo architecture
  - national prevalence of vote buying/clientelism
  - systematic coordination across local cases
  - general causal persuasion or electoral outcome
- **verified:**
  - candidates/intermediaries can provide material inducements in case-specific L106 findings
  - officials have discretionary or influential access to public resource-allocation channels in empirical studies
  - political connections can correlate with preferential allocations

### NEXT_QUERIES
- RECHECK if a machine-readable national corpus of L106 election/ciminal cases permits a denominator and prevalence coding
- RECHECK if transaction-level records or investigations establish explicit quid pro quo in distributive datasets
- RECHECK newer causal studies of individualized benefits and vote behavior in France
- DEFER national architecture/electoral-effect claim until denominator and exposure-outcome design exist

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007 | support:- | counter:- | results:FCT-001,FCT-004,FCT-007,FCT-013,FCT-018,FCT-019 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-021,FCT-022,FCT-023,FCT-024,FCT-025,FCT-026,FCT-027,FCT-028,FCT-029 | final:SATURATED | gap:NONE
LED-003 | attempts:QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-008,QRY-009,QRY-010 | support:- | counter:- | results:FCT-005,FCT-009,FCT-014,FCT-021,FCT-025,FCT-027,FCT-029 | final:GAP | gap:SCOPE
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-007,FCT-015,FCT-016,FCT-017 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-002,QRY-003,QRY-004 | support:- | counter:- | results:FCT-004,FCT-005,FCT-007,FCT-008,FCT-013,FCT-014 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-003,QRY-005,QRY-006 | support:- | counter:- | results:FCT-010,FCT-011,FCT-012,FCT-015,FCT-016,FCT-017 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-007 | support:- | counter:- | results:FCT-018,FCT-019,FCT-020 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-021,FCT-022,FCT-023,FCT-024,FCT-025,FCT-026,FCT-027,FCT-028,FCT-029 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-002,QRY-003,QRY-004,QRY-008,QRY-009,QRY-010,QRY-011 | support:- | counter:- | results:FCT-005,FCT-009,FCT-014,FCT-021,FCT-025,FCT-027,FCT-029 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,SRC-001,SRC-002,SRC-003,SRC-004 | support:FCT-001,FCT-004,FCT-007,FCT-008,FCT-013 | counter:CTRL-001,CTRL-002 | results:FCT-001,FCT-004,FCT-007,FCT-008,FCT-013,CTRL-001,CTRL-002 | final:SUPPORTED | gap:SCOPE
CLM-002 | attempts:QRY-007,SRC-007 | support:FCT-018,FCT-019,FCT-020 | counter:CTRL-004 | results:FCT-018,FCT-019,FCT-020,CTRL-004 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-003 | attempts:QRY-003,QRY-005,QRY-006,SRC-003,SRC-005,SRC-006 | support:FCT-010,FCT-011,FCT-012,FCT-015,FCT-016,FCT-017 | counter:CTRL-003 | results:FCT-010,FCT-011,FCT-012,FCT-015,FCT-016,FCT-017,CTRL-003 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-008,QRY-009,QRY-010,QRY-011,SRC-008,SRC-009,SRC-010,SRC-011 | support:FCT-021,FCT-022,FCT-023,FCT-024,FCT-025,FCT-026,FCT-027,FCT-028,FCT-029 | counter:CTRL-004 | results:FCT-021,FCT-022,FCT-023,FCT-024,FCT-025,FCT-026,FCT-027,FCT-028,FCT-029,CTRL-004 | final:SUPPORTED | gap:CAUSALITY
CLM-005 | attempts:QRY-008,QRY-009,QRY-010,QRY-011,SRC-008,SRC-009,SRC-010,SRC-011 | support:FCT-023,FCT-026,FCT-028,FCT-029 | counter:CTRL-005 | results:FCT-023,FCT-026,FCT-028,FCT-029,CTRL-005 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-006 | attempts:QRY-002,QRY-003,QRY-004,QRY-011,SRC-002,SRC-003,SRC-004,SRC-011 | support:FCT-005,FCT-009,FCT-014,FCT-029 | counter:CTRL-006 | results:FCT-005,FCT-009,FCT-014,FCT-029,CTRL-006 | final:SUPPORTED | gap:CAUSALITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-001 | CLM | SUPPORTED | SCOPE | Le corpus de jurisprudence sélectionné établit l’existence du mécanisme, pas sa fréquence nationale.
CLM-002 | CLM | SUPPORTED | RESPONSIBILITY | Les catégories de sciences sociales ne déterminent pas à elles seules une qualification pénale ou un quid pro quo prouvé dans chaque cas.
CLM-004 | CLM | SUPPORTED | CAUSALITY | Les mécanismes et unités diffèrent entre transferts ministériels, réserve sénatoriale, permis et cycle budgétaire; ils ne forment pas une mesure unique de clientélisme.
CLM-005 | CLM | SUPPORTED | RESPONSIBILITY | Il faudrait des traces d’échange/conditionnement, un dénominateur des bénéficiaires et une attribution du mécanisme pour passer du pattern à l’échange clientéliste spécifique.
CLM-006 | CLM | SUPPORTED | CAUSALITY | Absence de design national reliant exposition à l’avantage, changement de vote et résultat contrefactuel.
CAU-001 | CAU | GAP | CAUSALITY | Manquent un dénominateur d’exposition, des traces individualisées de conditionnement et des designs reliant avantage à changement de vote puis résultat contrefactuel.

SEMANTIC_COUNTS_V1:LED:3|CLM:6|AXS:6|CAU:1|CTRL:6|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007"],"evidence_excerpt":"Le droit et la jurisprudence documentent des échanges matériels destinés à influencer le vote, tandis que les contrôles négatifs excluent les avantages publics ordinaires sans arête électorale suffisante.","kind":"DISCRIMINATION_LEAD","lead":"Distinguer achat direct de voix, clientélisme et redistribution électoraliste par l’existence d’un avantage et d’une arête de soutien politique/électoral documentée.","linked_ids":["CLM-001","CLM-002","CLM-003"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-004","FCT-007","FCT-013","FCT-018","FCT-019"],"routes":["INV-102"],"source_id":"INV-098_RUN_CARD","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"evidence_excerpt":"Plusieurs études quantitatives françaises montrent des allocations corrélées à des liens politiques ou incitations électorales, mais avec des unités et mécanismes distincts du vote-buying direct.","kind":"MECHANISM_LEAD","lead":"Tester si des datasets français établissent un favoritisme ou une allocation électoraliste sans convertir ces patterns en achat individuel de votes.","linked_ids":["CLM-004","CLM-005"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-021","FCT-022","FCT-023","FCT-024","FCT-025","FCT-026","FCT-027","FCT-028","FCT-029"],"routes":["INV-102"],"source_id":"INV-098_RUN_CARD","status":"SATURATED"}
LED-003 | {"attempt_ids":["QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-008","QRY-009","QRY-010"],"evidence_excerpt":"Le corpus ferme l’existence de mécanismes directs et de patterns distributifs, mais aucun dénominateur national comparable des cas/expositions n’est disponible pour estimer une prévalence nationale.","gap":"Aucun dénominateur national comparable des cas L106, des échanges clientélistes ou de la population exposée n’est disponible dans le corpus; les cas et études ne permettent pas d’estimer une prévalence nationale.","gap_type":"SCOPE","kind":"SYSTEM_GAP","lead":"Mesurer la prévalence nationale et l’effet causal global du vote-buying/clientélisme sur le vote et les résultats.","linked_ids":["CLM-005","CLM-006","CAU-001"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-005","FCT-009","FCT-014","FCT-021","FCT-025","FCT-027","FCT-029"],"routes":["RECHECK(dataset national L106/quid-pro-quo)","DEFER(effect causal national)"],"source_id":"INV-098_RUN_CARD","status":"GAP"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"L’achat direct de votes est un mécanisme juridiquement défini et factuellement établi dans plusieurs cas français: argent, promesse de logement ou distributions matérielles peuvent constituer des pressions électorales lorsqu’elles visent à influencer le vote.","claimant":"INV-098 synthesis","counter":["CTRL-001","CTRL-002"],"gap":"Le corpus de jurisprudence sélectionné établit l’existence du mécanisme, pas sa fréquence nationale.","gap_type":"SCOPE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-004","FCT-007","FCT-008","FCT-013"]}
CLM-002 | {"claim":"Le clientélisme politique est un concept plus large et temporellement plus diffus que l’achat direct de voix: il couvre des échanges personnalisés de biens, services ou protection contre un soutien politique/électoral.","claimant":"INV-098 synthesis","counter":"CTRL-004","gap":"Les catégories de sciences sociales ne déterminent pas à elles seules une qualification pénale ou un quid pro quo prouvé dans chaque cas.","gap_type":"RESPONSIBILITY","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-018","FCT-019","FCT-020"]}
CLM-003 | {"claim":"Une politique publique ciblée, un recrutement, une prime, une subvention ou une distribution matérielle ne constituent pas automatiquement un achat de voix; le lien électoral, la preuve de l’avantage et le contexte sont déterminants.","claimant":"INV-098 synthesis","counter":"CTRL-003","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-010","FCT-011","FCT-012","FCT-015","FCT-016","FCT-017"]}
CLM-004 | {"claim":"Des travaux empiriques français documentent des formes mesurables de favoritisme, pork-barrel ou allocation électoraliste de ressources publiques liées aux connexions et incitations politiques.","claimant":"INV-098 synthesis","counter":"CTRL-004","gap":"Les mécanismes et unités diffèrent entre transferts ministériels, réserve sénatoriale, permis et cycle budgétaire; ils ne forment pas une mesure unique de clientélisme.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-021","FCT-022","FCT-023","FCT-024","FCT-025","FCT-026","FCT-027","FCT-028","FCT-029"]}
CLM-005 | {"claim":"Les patterns de favoritisme ou d’électoralisme agrégés ne prouvent pas, sans arête supplémentaire, un quid pro quo individuel avantage contre vote, ni une architecture nationale coordonnée de clientélisme.","claimant":"INV-098 synthesis","counter":"CTRL-005","gap":"Il faudrait des traces d’échange/conditionnement, un dénominateur des bénéficiaires et une attribution du mécanisme pour passer du pattern à l’échange clientéliste spécifique.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-023","FCT-026","FCT-028","FCT-029"]}
CLM-006 | {"claim":"L’effet électoral est démontré seulement de façon bornée: certains cas sont jugés capables d’altérer la sincérité et Corbeil 2009 conduit à l’annulation, tandis que d’autres violations ou distributions ne changent pas le résultat; aucune causalité nationale générale n’est établie.","claimant":"INV-098 synthesis","counter":"CTRL-006","gap":"Absence de design national reliant exposition à l’avantage, changement de vote et résultat contrefactuel.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-005","FCT-009","FCT-014","FCT-029"]}

### AXIS_REGISTRY_V1
AXS-001 | {"assessment":"LEGAL_AND_ELECTORAL_THRESHOLD_DOCUMENTED","attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006"],"axis":"legal_threshold","links":["CLM-001","CLM-003"],"question":"Quel seuil juridique distingue un avantage ordinaire d’un avantage destiné à influencer vote ou abstention ?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-007","FCT-015","FCT-016","FCT-017"],"sought_objects":["BENEFIT","INTENT_TO_INFLUENCE","VOTE","ABSTENTION","PRESSURE"],"status":"SATURATED"}
AXS-002 | {"assessment":"MULTIPLE_CASE_SPECIFIC_POSITIVE_CONTROLS","attempt_ids":["QRY-002","QRY-003","QRY-004"],"axis":"positive_cases","links":["CLM-001"],"question":"Existe-t-il en France des cas administrativement établis de dons, argent, logement ou biens destinés à influencer des électeurs ?","result_ids":["FCT-004","FCT-005","FCT-007","FCT-008","FCT-013","FCT-014"],"sought_objects":["MONEY","HOUSING","FOOD","INDUCEMENT"],"status":"SATURATED"}
AXS-003 | {"assessment":"STRONG_NEGATIVE_CONTROLS","attempt_ids":["QRY-003","QRY-005","QRY-006"],"axis":"negative_controls","links":["CLM-003"],"question":"Quels avantages ou politiques ciblés le juge refuse-t-il d’assimiler à des pressions électorales faute de preuve suffisante ?","result_ids":["FCT-010","FCT-011","FCT-012","FCT-015","FCT-016","FCT-017"],"sought_objects":["ROUTINE_PROGRAM","EMPLOYMENT","BONUS","MASKS","SUBSIDY"],"status":"SATURATED"}
AXS-004 | {"assessment":"BROADER_SOCIAL_SCIENCE_CONCEPT_DOCUMENTED","attempt_ids":["QRY-007"],"axis":"clientelism_boundary","links":["CLM-002"],"question":"Comment la littérature distingue-t-elle clientélisme/patronage de l’infraction ponctuelle d’achat de voix ?","result_ids":["FCT-018","FCT-019","FCT-020"],"sought_objects":["PATRON_CLIENT","PERSONALIZED_EXCHANGE","POLITICAL_SUPPORT","JOBS","HOUSING","SUBSIDIES"],"status":"SATURATED"}
AXS-005 | {"assessment":"MEASURABLE_FAVORITISM_AND_ELECTORALIST_PATTERNS","attempt_ids":["QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"axis":"distributive_favoritism","links":["CLM-004","CLM-005"],"question":"Les allocations publiques françaises présentent-elles des patterns compatibles avec favoritisme ou électoralisme ?","result_ids":["FCT-021","FCT-022","FCT-023","FCT-024","FCT-025","FCT-026","FCT-027","FCT-028","FCT-029"],"sought_objects":["SUBSIDIES","FIEF","BUILDING_PERMITS","POLITICAL_CONNECTIONS","ELECTORAL_CYCLE"],"status":"SATURATED"}
AXS-006 | {"assessment":"CASE_SPECIFIC_EFFECTS_AND_NO_NATIONAL_PREVALENCE_DENOMINATOR","attempt_ids":["QRY-002","QRY-003","QRY-004","QRY-008","QRY-009","QRY-010","QRY-011"],"axis":"prevalence_and_effect","links":["CLM-005","CLM-006","CAU-001"],"question":"Peut-on inférer fréquence nationale, persuasion des bénéficiaires ou changement électoral global ?","result_ids":["FCT-005","FCT-009","FCT-014","FCT-021","FCT-025","FCT-027","FCT-029"],"sought_objects":["PREVALENCE","EXPOSURE_DENOMINATOR","PERSUASION","BEHAVIOR","ELECTORAL_OUTCOME"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"CTRL-001;CTRL-003;CTRL-004;CTRL-005;CTRL-006","gap":"Manquent un dénominateur d’exposition, des traces individualisées de conditionnement et des designs reliant avantage à changement de vote puis résultat contrefactuel.","gap_type":"CAUSALITY","limit":"La chaîne est fortement établie jusqu’à l’avantage et, dans quelques cas L106, jusqu’à l’intention d’influencer; les datasets agrégés établissent ciblage/favoritisme mais pas un quid pro quo individuel ni une réponse électorale générale.","mechanism":"ressource/avantage -> ciblage ou relation personnalisée -> condition/attente de soutien politique ou électoral -> réception/exposition -> changement éventuel de vote -> résultat agrégé","status":"GAP","support":["FCT-001","FCT-004","FCT-007","FCT-008","FCT-018","FCT-019","FCT-021","FCT-025","FCT-027"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Existence d’un don ou avantage matériel ne suffit pas: le droit et le juge exigent un lien avec l’intention d’influencer le vote ou l’abstention et apprécient le contexte électoral.","status":"VERIFIED","support":["FCT-001","FCT-003","FCT-015","FCT-016"]}
CTRL-002 | {"control":"Une violation ou pression au sens de L106 peut être établie sans que la sincérité du scrutin soit altérée si l’ampleur ou l’écart de voix ne permet pas de changer le résultat.","status":"VERIFIED","support":["FCT-009","FCT-014"]}
CTRL-003 | {"control":"Des recrutements, primes, aides récurrentes, subventions ou infrastructures peuvent être écartés comme achat de voix lorsqu’ils répondent à un besoin ou s’inscrivent dans une politique antérieure/récurrente.","status":"VERIFIED","support":["FCT-011","FCT-012","FCT-016","FCT-017"]}
CTRL-004 | {"control":"Pork-barrel, favoritisme et allocation électoraliste sont des objets empiriques plus larges que l’échange direct et explicite avantage contre vote.","status":"VERIFIED","support":["FCT-021","FCT-023","FCT-026","FCT-027","FCT-029"]}
CTRL-005 | {"control":"Des cas judiciaires positifs ou des corrélations locales ne fournissent pas un taux de prévalence nationale du vote-buying ou du clientélisme.","status":"VERIFIED","support":["FCT-006","FCT-020","FCT-026","FCT-028"]}
CTRL-006 | {"control":"Un transfert matériel ou un ciblage favorable ne démontre pas automatiquement persuasion, changement de comportement électoral ou résultat contrefactuel; l’effet est une arête distincte.","status":"VERIFIED","support":["FCT-005","FCT-009","FCT-014","FCT-029"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:3|FETCH:11|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL:MNEMO_UNAVAILABLE | mnemo | NONE | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | OK | SRC-001 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006353253/2026-04-12 | FETCH Code électoral — article L106
QRY-002 | FETCH | OK | SRC-002 | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000020869399/ | FETCH Conseil d’État, 8 juin 2009, n°322236, Corbeil-Essonnes
QRY-003 | FETCH | OK | SRC-003 | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000030755736 | FETCH Conseil d’État, 19 juin 2015, n°385592, Sainte-Suzanne
QRY-004 | FETCH | OK | SRC-004 | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2021-07-22/450129 | FETCH Conseil d’État, 22 juillet 2021, n°450129, Corbeil-Essonnes
QRY-005 | FETCH | OK | SRC-005 | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000043852126 | FETCH Conseil d’État, 22 juillet 2021, n°449614, Dourdan
QRY-006 | FETCH | OK | SRC-006 | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000032772236/ | FETCH Conseil d’État, 17 juin 2016, n°395481, La Réunion
QRY-007 | FETCH | OK | SRC-007 | https://www.agence-francaise-anticorruption.gouv.fr/files/files/Etat%20de%20l%27art%20corruption.pdf | FETCH AFA — État de l’art sur la corruption
QRY-008 | FETCH | OK | SRC-008 | https://www.sciencedirect.com/science/article/pii/S0047272724002123 | FETCH Fabre & Sangnier — The political allocation of public investment subsidies
QRY-009 | FETCH | OK | SRC-009 | https://droit.cairn.info/revue-francaise-d-administration-publique-2024-2-page-455?lang=fr | FETCH Dubois & Monnery — Réserve parlementaire et ciblage électoral
QRY-010 | FETCH | OK | SRC-010 | https://link.springer.com/article/10.1007/s11127-019-00718-z | FETCH Lévêque — Political connections and building permits in France
QRY-011 | FETCH | OK | SRC-011 | https://www.sciencedirect.com/science/article/abs/pii/S0165176513005612 | FETCH Cassette & Farvaque — Political budget cycles and reelection in French municipalities
QRY-012 | WEB | NONE | - | - | REFUTATION vote-buying-clientelism Fabre Sangnier 30% minister former mayor investment subsidies France alternative explanation
QRY-013 | WEB | NONE | - | - | REFUTATION vote-buying-clientelism Dubois Monnery 348 senators 50 million 79% 97% 8% reserve electoral fief France alternative explanation
QRY-014 | WEB | NONE | - | - | REFUTATION vote-buying-clientelism Leveque 189000 politicians 35% building permits 2008 2014 France alternative explanation

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | LEGIFRANCE-L106 | Code électoral — article L106 | 2026-04-12 | 2026-09-08T05:10:00+02:00 | elements constitutifs et peines | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006353253/2026-04-12
SRC-002 | ◈ | fam:A | CE-322236 | Conseil d’État, 8 juin 2009, n°322236, Corbeil-Essonnes | 2009-06-08 | 2026-09-08T05:11:00+02:00 | dons argent; libre détermination; marge 170 voix; annulation | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000020869399/
SRC-003 | ◈ | fam:A | CE-385592 | Conseil d’État, 19 juin 2015, n°385592, Sainte-Suzanne | 2015-06-19 | 2026-09-08T05:11:30+02:00 | argent; logement; recrutements; prime; sincérité | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000030755736
SRC-004 | ◈ | fam:A | CE-450129 | Conseil d’État, 22 juillet 2021, n°450129, Corbeil-Essonnes | 2021-07-22 | 2026-09-08T05:12:00+02:00 | colis alimentaires; finalité électorale; sincérité | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2021-07-22/450129
SRC-005 | ◈ | fam:A | CE-449614 | Conseil d’État, 22 juillet 2021, n°449614, Dourdan | 2021-07-22 | 2026-09-08T05:12:30+02:00 | 4000 masques; L106; contrôle négatif | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000043852126
SRC-006 | ◈ | fam:A | CE-395481 | Conseil d’État, 17 juin 2016, n°395481, La Réunion | 2016-06-17 | 2026-09-08T05:13:00+02:00 | aides 100-150 euros; wifi; subvention 90000; contrôle négatif | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000032772236/
SRC-007 | ◈ | fam:B | AFA-ETAT-ART-CORRUPTION | AFA — État de l’art sur la corruption | 2021 | 2026-09-08T05:13:30+02:00 | clientélisme/patronage; échange personnalisé; cas français | https://www.agence-francaise-anticorruption.gouv.fr/files/files/Etat%20de%20l%27art%20corruption.pdf
SRC-008 | ◉ | fam:C | JPE-2025-105276 | Fabre & Sangnier — The political allocation of public investment subsidies | 2025-01 | 2026-09-08T05:14:00+02:00 | minister-mayor municipalities; ~30% investment subsidies | https://www.sciencedirect.com/science/article/pii/S0047272724002123
SRC-009 | ◉ | fam:D | RFAP-2024-186-455 | Dubois & Monnery — Réserve parlementaire et ciblage électoral | 2024 | 2026-09-08T05:14:30+02:00 | 348 senators; reserve; own department/fief | https://droit.cairn.info/revue-francaise-d-administration-publique-2024-2-page-455?lang=fr
SRC-010 | ◉ | fam:E | PUBLIC-CHOICE-2020 | Lévêque — Political connections and building permits in France | 2020 | 2026-09-08T05:15:00+02:00 | >189000 politicians; 35% permit differential; 2008-2014 | https://link.springer.com/article/10.1007/s11127-019-00718-z
SRC-011 | ◉ | fam:other:debt-cycle | ECON-LETTERS-2014 | Cassette & Farvaque — Political budget cycles and reelection in French municipalities | 2014 | 2026-09-08T05:15:30+02:00 | pre-election debt accumulation and reelection probability | https://www.sciencedirect.com/science/article/abs/pii/S0165176513005612

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006353253/2026-04-12 | A | 2026-09-08 | Article L106: avantage contre vote ou abstention | L’article L106 du code électoral vise les dons ou libéralités en argent ou en nature, promesses de libéralités, faveurs, emplois publics ou privés et autres avantages particuliers faits en vue d’influencer le vote, d’obtenir un suffrage ou de déterminer une abstention, directement ou par un tiers. | -
FCT-002 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006353253/2026-04-12 | A | 2026-09-08 | Article L106: sanctions offre et sollicitation | L’article L106 prévoit deux ans d’emprisonnement et 15 000 euros d’amende pour l’auteur et punit des mêmes peines ceux qui agréent ou sollicitent les mêmes dons, libéralités ou promesses. | -
FCT-003 | FACT | ✧ | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000032772236/ | A | 2016-06-17 | Juge électoral: pression L106 et sincérité distinctes du pénal | Le Conseil d’État rappelle qu’il n’applique pas lui-même les sanctions pénales de L106 mais recherche si des pressions au sens de cet article ont été exercées et ont été de nature à altérer la sincérité du scrutin. | -
FCT-004 | FACT | ✧ | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000020869399/ | A | 2009-06-08 | Corbeil 2009: dons d’argent significatifs et persistants | Le Conseil d’État a tenu pour établis des dons d’argent d’une ampleur significative du maire sortant à des habitants de Corbeil-Essonnes, pratique persistante y compris pendant la période électorale. | -
FCT-005 | FACT | ✧ | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000020869399/ | A | 2009-06-08 | Corbeil 2009: libre détermination et écart de 170 voix | Le Conseil d’État a jugé que ces dons avaient pu affecter la libre détermination des électeurs et, au regard d’un écart de 170 voix entre 6 621 et 6 451, étaient de nature à altérer la sincérité du scrutin et à en vicier les résultats. | -
FCT-006 | FACT | ✧ | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000020869399/ | A | 2009-06-08 | Corbeil 2009: ampleur exacte des dons non déterminée | La décision constate que l’ampleur exacte des dons d’argent ne pouvait être précisément déterminée, tout en les tenant pour matériellement significatifs. | -
FCT-007 | FACT | ✧ | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000030755736 | A | 2015-06-19 | Sainte-Suzanne 2015: argent et promesse de logement | À la veille du second tour, le candidat a remis une somme d’argent et promis un logement à un assesseur adverse; le Conseil d’État a considéré ces avantages comme destinés à influencer son vote même sans demande explicite de vote en sa faveur. | -
FCT-008 | FACT | ✧ | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000030755736 | A | 2015-06-19 | Sainte-Suzanne 2015: argent donné à un électeur par un partisan | Un agent communal partisan du candidat a donné une somme d’argent à un électeur pour l’inciter à voter pour sa liste; la décision qualifie le fait de violation de L106. | -
FCT-009 | FACT | ✧ | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000030755736 | A | 2015-06-19 | Sainte-Suzanne 2015: violation L106 sans changement du résultat | Malgré les violations de L106 établies, le Conseil d’État a jugé qu’elles n’avaient pas altéré la sincérité du scrutin compte tenu de l’écart de voix. | -
FCT-010 | FACT | ✧ | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000030755736 | A | 2015-06-19 | Sainte-Suzanne 2015: allégation de matériaux non établie | L’allégation selon laquelle de nombreux électeurs auraient reçu gratuitement du matériel de construction n’a pas été tenue pour matériellement établie par les deux attestations produites. | -
FCT-011 | FACT | ✧ | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000030755736 | A | 2015-06-19 | Sainte-Suzanne 2015: recrutements 58 et 45 non prouvés comme avantages électoraux | Le requérant invoquait le recrutement de 58 jeunes animateurs et de 45 personnes par le CCAS; faute de preuve que ces recrutements ne répondaient pas aux besoins de la commune ou du CCAS, le Conseil d’État a écarté leur qualification d’avantages prohibés par L106. | -
FCT-012 | FACT | ✧ | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000030755736 | A | 2015-06-19 | Sainte-Suzanne 2015: prime à plus de 400 agents dans une politique antérieure | Une prime exceptionnelle versée à plus de 400 agents non titulaires a été regardée comme s’inscrivant dans la continuité d’une politique municipale approuvée en 2011; le moyen d’achat de voix a été écarté. | -
FCT-013 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2021-07-22/450129 | A | 2021-07-22 | Corbeil 2021: distributions répétées de colis alimentaires par des candidats | Des candidats ont participé à de nombreuses distributions de colis alimentaires d’avril à juin 2020 dans différents quartiers alors qu’ils n’étaient pas habituellement engagés dans ces associations ou ce type d’action. | -
FCT-014 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2021-07-22/450129 | A | 2021-07-22 | Corbeil 2021: distribution électorale mais résultat non altéré | Le Conseil d’État a regardé ces distributions comme intervenues en vue des élections et capables d’affecter la libre détermination de certains électeurs, mais pas comme suffisantes pour altérer la sincérité et vicier les résultats au regard de l’écart de voix. | -
FCT-015 | FACT | ✧ | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000043852126 | A | 2021-07-22 | Dourdan 2021: distribution de 4000 masques ne suffit pas à établir pression électorale | Une distribution de 4 000 masques chirurgicaux provenant de dons d’un réseau d’entraide a été examinée sous L106; le Conseil d’État n’en a pas tiré une pression électorale de nature à altérer la sincérité du scrutin dans les circonstances de l’espèce. | -
FCT-016 | FACT | ✧ | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000032772236/ | A | 2016-06-17 | Réunion 2016: aides récurrentes de 100 à 150 euros et wifi non assimilés à dons électoraux | Des aides récurrentes de 100 à 150 euros aux entreprises pour des stagiaires, un programme habituel de la CCI et l’annonce d’un réseau wifi gratuit n’ont pas été regardés comme des promesses de dons de nature à altérer la sincérité du scrutin. | -
FCT-017 | FACT | ✧ | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000032772236/ | A | 2016-06-17 | Réunion 2016: subvention de 90000 euros avec formation réellement exécutée | Une subvention de 90 000 euros à l’association des maires pour un programme de formation effectivement réalisé n’a pas été regardée comme une promesse de don électorale prohibée dans cette affaire. | -
FCT-018 | FACT | ✧ | https://www.agence-francaise-anticorruption.gouv.fr/files/files/Etat%20de%20l%27art%20corruption.pdf | B | 2021 | AFA: clientélisme comme échange personnalisé asymétrique de biens et services | L’état de l’art de l’AFA décrit le clientélisme ou patronage comme des relations de pouvoir asymétriques personnalisées fondées sur l’échange de services et de biens, où un patron apporte protection ou ressources à des clients qui apportent en échange leur soutien. | -
FCT-019 | FACT | ✧ | https://www.agence-francaise-anticorruption.gouv.fr/files/files/Etat%20de%20l%27art%20corruption.pdf | B | 2021 | AFA: clientélisme politique contre soutien électoral, emplois logement subvention | L’AFA rapporte que la littérature distingue parfois le clientélisme politique comme soutien politique et électoral, souvent en échange de biens maîtrisés par les élus tels que des emplois publics, un logement social ou une subvention. | -
FCT-020 | FACT | ✧ | https://www.agence-francaise-anticorruption.gouv.fr/files/files/Etat%20de%20l%27art%20corruption.pdf | B | 2021 | AFA: cas français contemporains et catégorie plus large que l’infraction pénale | L’état de l’art mentionne des études de cas contemporaines en Corse, à Marseille et en banlieue parisienne et souligne que la catégorie de clientélisme est descriptive et normative, avec des définitions variables; elle n’est donc pas réductible à l’infraction pénale d’achat de voix. | -
FCT-021 | FACT | ✧ | https://www.sciencedirect.com/science/article/pii/S0047272724002123 | C | 2025-01 | Pork français: 30 pour cent de subventions d’investissement pour communes liées à un ministre-maire | Fabre et Sangnier estiment que les communes où un ministre avait été maire reçoivent environ 30 % de subventions d’investissement supplémentaires lorsque ce responsable entre au gouvernement, avec une baisse de taille similaire lorsqu’il en sort. | -
FCT-022 | FACT | ✧ | https://www.sciencedirect.com/science/article/pii/S0047272724002123 | C | 2025-01 | Pork français: absence d’effet comparable pour commune d’enfance | Les auteurs ne trouvent pas d’effet comparable pour les communes où les ministres avaient seulement vécu pendant leur enfance. | -
FCT-023 | FACT | ✧ | https://www.sciencedirect.com/science/article/pii/S0047272724002123 | C | 2025-01 | Pork français: interprétation par influence souple plutôt que contrôle formel | L’étude présente des éléments complémentaires compatibles avec une influence souple des ministres et des relations adultes ou préoccupations de carrière, plutôt qu’avec leur seul contrôle formel de l’administration. | -
FCT-024 | FACT | ✧ | https://droit.cairn.info/revue-francaise-d-administration-publique-2024-2-page-455?lang=fr | D | 2014-2017 | Réserve sénatoriale: 348 sénateurs et environ 50 millions euros par an | Dubois et Monnery étudient les allocations de réserve de 348 sénateurs sur 2014–2017; les dépenses annuelles de réserve sénatoriale restent autour de 50 millions d’euros, soit un peu plus de 140 000 euros par sénateur en moyenne. | -
FCT-025 | FACT | ✧ | https://droit.cairn.info/revue-francaise-d-administration-publique-2024-2-page-455?lang=fr | D | 2014-2017 | Réserve sénatoriale: 79 pour cent communes, 97 pour cent département, 8 pour cent fief | Dans les données 2014–2017, 79 % des subventions sénatoriales financent des communes; dans 97 % des cas la réserve d’un sénateur est intégralement dépensée dans son département et environ 8 % du montant annuel est fléché vers son fief électoral. | -
FCT-026 | FACT | ✧ | https://droit.cairn.info/revue-francaise-d-administration-publique-2024-2-page-455?lang=fr | D | 2024 | Réserve sénatoriale: résultats cohérents avec usage électoraliste sans prouver échange individuel de vote | Les auteurs concluent à des comportements stratégiques cohérents avec un usage électoraliste des subventions; leur design porte sur l’allocation de ressources publiques et ne documente pas un échange individuel explicite avantage contre vote. | -
FCT-027 | FACT | ✧ | https://link.springer.com/article/10.1007/s11127-019-00718-z | E | 2008-2014 | Permis français: plus de 189000 politiciens et 35 pour cent de permis supplémentaires pour familles de soutiens | Lévêque analyse plus de 189 000 responsables politiques locaux dans des villes françaises de plus de 3 500 habitants et trouve que les familles de candidats ayant soutenu les maires élus en 2008 obtiennent 35 % de permis de construire de plus que les familles d’opposants entre 2008 et 2014. | -
FCT-028 | FACT | ✧ | https://link.springer.com/article/10.1007/s11127-019-00718-z | E | 2008-2014 | Permis français: favoritisme diminue avec concurrence et disparaît après élections serrées | L’écart de permis diminue avec la concurrence politique et disparaît après des élections serrées; l’auteur interprète les résultats comme du favoritisme politique local, sans en faire une mesure nationale d’achat direct de voix. | -
FCT-029 | FACT | ✧ | https://www.sciencedirect.com/science/article/abs/pii/S0165176513005612 | other:debt-cycle | 2014 | Cycle budgétaire municipal: dette préélectorale et probabilité de réélection | Cassette et Farvaque trouvent que la dette moyenne du mandat réduit la probabilité de réélection tandis qu’une accumulation de dette juste avant l’élection augmente cette probabilité; ce résultat documente un cycle électoral de dépense visible mais pas un quid pro quo individuel. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-006
FCT-004 | SRC-002
FCT-005 | SRC-002
FCT-006 | SRC-002
FCT-007 | SRC-003
FCT-008 | SRC-003
FCT-009 | SRC-003
FCT-010 | SRC-003
FCT-011 | SRC-003
FCT-012 | SRC-003
FCT-013 | SRC-004
FCT-014 | SRC-004
FCT-015 | SRC-005
FCT-016 | SRC-006
FCT-017 | SRC-006
FCT-018 | SRC-007
FCT-019 | SRC-007
FCT-020 | SRC-007
FCT-021 | SRC-008
FCT-022 | SRC-008
FCT-023 | SRC-008
FCT-024 | SRC-009
FCT-025 | SRC-009
FCT-026 | SRC-009
FCT-027 | SRC-010
FCT-028 | SRC-010
FCT-029 | SRC-011

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

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:11:CAU-001 | NEXT_ACTION:13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-08T03:37:51.646170+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-029","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":29,"eligible":29,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:29;attempted:0;success:0;failure:0;blocked:29} | WRITEBACK_EXECUTION_V1:[29 rows, see section]

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
