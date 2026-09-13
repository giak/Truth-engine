ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260907-2340-funded-counter-disinfo | PARENT_RUN_ID:NONE | AS_OF:2026-09-07
INPUT_KIND:RUN_CARD | MISSION_MODE:RECHECK_EXTEND | INPUT_REF:PATH:/mnt/data/inv079-exec/te/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-07_funded-counter-disinfo/2026-09-07_23-40_funded-counter-disinfo_INPUT.md | SUBJECT_SLUG:funded-counter-disinfo | SUBJECT_FP:sha256:7edb3f03acd573a83cc63a5a4bef4bf58e37941616f1839ca3d64ce17d459cf1 | INPUT_SHA256:sha256:b5f6ad29fc1b5c9ce708f74915f40e558dd3abc474fb51d7b4849353a02d3db1
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/EU 2018-2026; public grants/calls/contracts supporting anti-disinformation, anti-hate, media-literacy or radicalisation-prevention actors; exclude Fonds Marianne as main object and certification already treated in INV-045.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/MONEY.md,clusters/POWER.md,clusters/NETWORK.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
## Question et résultat

L’objet n’est pas de demander si l’État ou l’Union européenne « financent la lutte contre la désinformation » au sens vague. Le corpus permet de fermer une question plus précise : **quels véhicules publics financent quels types d’acteurs et d’activités, avec quels critères, contrôles et limites de responsabilité ?**

Le résultat est double. Premièrement, un écosystème public de financement est bien établi en France et dans l’UE. Il couvre des associations, établissements, consortiums, médias, chercheurs et prestataires travaillant sur la haine en ligne, la prévention de la radicalisation, l’éducation aux médias, la détection de manipulations informationnelles ou la résilience face à la désinformation. Les montants ne sont pas anecdotiques : l’appel national DILCRAH 2025 représente 7,7 M€ [FCT-001], le FIPD 2025 confié au SG-CIPDR 52,7 M€ pour ses politiques de prévention [FCT-008], l’appel Creative Europe d’éducation aux médias 2024 2,57 M€ [FCT-019], deux appels européens de 2025 près de 5 M€ [FCT-022], et la Commission documente plusieurs vagues de financement EDMO par marchés et subventions [FCT-024,FCT-025].

Deuxièmement, **financement public et commandement éditorial ne sont pas la même arête**. Les textes étudiés ferment clairement `objectif public -> règles d’éligibilité -> sélection -> financement -> capacité/livrables`. Ils ne ferment pas, de façon générale, `financeur public -> instruction sur un contenu précis -> retrait/modération de contenu politique licite -> persuasion -> résultat électoral` [FCT-028].

## France : des financements orientés, sélectionnés et contrôlés

La DILCRAH constitue un cas positif de financement public orienté. Son appel national 2025 était doté de 7,7 M€, en hausse de 7 %, et ouvert à diverses personnes morales à but non lucratif [FCT-001,FCT-002]. Les objectifs ne sont pas neutres au sens d’un financement sans objet : la production de ressources, la sensibilisation, le contre-discours en ligne et le développement du signalement des discours de haine font partie des priorités explicites [FCT-003].

Ce cadrage produit une influence réelle au niveau du **programme** : un projet extérieur au périmètre ne peut pas être financé par cet instrument. L’administration instruit les demandes, une commission d’attribution intervient, et la DILCRAH se réserve un contrôle sur la réalité, l’effectivité et l’adéquation des actions [FCT-004]. La délégation utilise également des appels locaux et des conventions pluriannuelles d’objectifs avec certains acteurs [FCT-005]. Le guide local 2025 documente une enveloppe de 3 M€ et un dispositif déconcentré aux préfets [FCT-006], avec contrôle des comptes rendus financiers et articulation aux instances territoriales [FCT-007].

Le FIPD montre une architecture différente. Sa base juridique autorise le financement d’actions de prévention de la délinquance et de la radicalisation [FCT-013], tandis que les orientations d’utilisation et les conditions d’éligibilité relèvent du comité interministériel et que les crédits sont délégués aux préfets [FCT-014]. En 2025, l’enveloppe pilotée par le SG-CIPDR est de 52,7 M€ [FCT-008]. Le programme R couvre la prévention de la radicalisation [FCT-009] et peut financer contre-discours, sensibilisation, formation professionnelle, accompagnement familial, ainsi que des actions portant sur le séparatisme, le complotisme ou les phénomènes d’emprise [FCT-010].

Ce mécanisme établit donc plus que « l’État donne de l’argent à des associations ». Il établit une chaîne `priorité publique -> éligibilité -> subvention -> activité attendue`. Mais le même corpus montre aussi des contraintes formelles : les projets doivent s’inscrire dans les orientations du programme [FCT-011], et les associations sollicitant une subvention sont soumises au contrat d’engagement républicain [FCT-012]. Cela prouve du **gatekeeping administratif** et une capacité d’orientation, pas à lui seul un contrôle de chaque message produit par le bénéficiaire.

## Éducation aux médias : capacité financée et métriques demandées

Le ministère de la Culture soutient directement des porteurs de projets d’éducation aux médias et à l’information [FCT-015]. L’objectif officiel est de renforcer la capacité des citoyens, notamment des jeunes, à s’approprier l’information et à former leur propre opinion [FCT-016]. Là encore, il s’agit d’un objectif normatif et politique au sens large, mais pas d’une instruction éditoriale individualisée.

Le dispositif régional examiné rend visible la chaîne de contrôle : le dossier doit préciser les publics ciblés, le calendrier, la production médiatique, la pérennité et le budget [FCT-017], ainsi que des indicateurs de suivi et d’évaluation [FCT-018]. Un financement public peut donc façonner la structure du projet et ses métriques sans que cela implique que l’administration décide les conclusions ou opinions exprimées dans chaque production.

## Union européenne : subventions, marchés et capacité transfrontalière

Les instruments européens confirment le caractère structurel du phénomène, tout en obligeant à séparer les véhicules. L’appel Creative Europe 2024 d’éducation aux médias disposait de 2,57 M€, avec un plafond de 500 000 € par projet et un taux de cofinancement maximal de 70 % [FCT-019]. Il exigeait des consortiums transnationaux et ouvrait l’éligibilité à des organisations privées ou publiques, universités, médias et acteurs technologiques [FCT-020]. Les livrables attendus incluaient outils, actions transfrontalières, échanges de bonnes pratiques et soutien aux professionnels de l’éducation aux médias [FCT-021].

En avril 2025, la Commission a lancé deux appels proches de 5 M€ au total : 3,15 M€ pour la détection et l’analyse de manipulations informationnelles et le développement de réponses de résilience, et environ 1,6 M€ pour accroître la portée et l’impact de contenus de fact-checking [FCT-022]. Les organisations de la société civile, universités et centres de recherche figuraient parmi les candidats possibles, avec collaboration attendue avec EDMO pour les lauréats [FCT-023].

EDMO fournit un contrôle particulièrement utile contre la confusion `subvention = marché`. La Commission documente un financement de la plateforme centrale par **marchés publics**, alors que les hubs nationaux ou régionaux ont été financés par **subventions** [FCT-024]. Les montants cumulés indiquent un soutien récurrent : 2,5 M€ puis 4 M€ pour EDMO central, environ 11 M€ pour les huit premiers hubs, 8 M€ pour six hubs supplémentaires, puis d’autres refinancements [FCT-025]. Cette répétition établit une infrastructure durable de capacité, mais les différences de véhicule changent la relation juridique entre financeur et exécutant.

L’appel européen de 2025 sur l’intégrité informationnelle des jeunes ajoute une autre forme de financement : 6 M€ pour deux projets impliquant jeunes et influenceurs autour des techniques de manipulation, théories du complot et usages malveillants de l’IA générative [FCT-026]. CERV finance de son côté des organisations de la société civile sur des actions de lutte contre le racisme et la haine, incluant sensibilisation, soutien aux victimes, collecte de données et résilience [FCT-027].

## Ce que le financement permet réellement d’inférer

Le corpus justifie quatre conclusions intermédiaires.

1. **La capacité est financée.** Les montants, appels récurrents et dispositifs de renouvellement permettent à des organisations d’embaucher, produire, former, surveiller, analyser ou diffuser. Cette arête est établie.
2. **L’agenda programmatique est orienté.** Un financeur fixe un périmètre, des populations cibles, des types de projets et parfois des indicateurs. Les bénéficiaires s’alignent sur ce périmètre pour être éligibles. Cette arête est également établie.
3. **Les relations ne sont pas uniformes.** Subvention, marché public, convention pluriannuelle et financement déconcentré ne créent pas le même niveau d’obligation ni la même responsabilité.
4. **L’effet politique élevé reste ouvert.** L’existence d’une activité de contre-discours, de signalement, de détection ou de media literacy ne démontre ni que des contenus licites déterminés ont été retirés sur ordre public, ni que l’opinion ou le vote a changé en conséquence.

Le contrôle négatif décisif est FCT-028 : dans les instruments examinés, les documents publics définissent objectifs, conditions, livrables, suivi et évaluation. Ils ne ferment pas une chaîne générale de commandement public portant sur la suppression de contenus politiques licites spécifiques.

## Conséquence pour INV-088 et INV-144

Pour INV-088, ce run ajoute une distinction essentielle : le fact-checking et les activités voisines peuvent être intégrés à une **infrastructure financée de qualification et de résilience**, mais le financement seul ne permet pas d’inférer la conclusion d’un fact-check ou une action de plateforme. Il faut tracer séparément l’organisation financée, son livrable, son éventuelle interface avec une plateforme, la décision de modération et son effet.

Pour INV-144, le delta est plus structurel. Il existe bien une **économie politique de la contre-influence** au sens minimal : budgets publics récurrents, appels, sélection d’acteurs, marchés, subventions, consortiums, indicateurs et renouvellements. Cette économie crée des bénéficiaires, des compétences professionnelles, des routines administratives et des incitations à proposer des projets conformes aux catégories financées. Mais deux thèses fortes restent ouvertes : que cette économie conduise systématiquement à élargir artificiellement la menace, et qu’elle constitue un système coordonné de censure ou de contrôle politique.

La prochaine synthèse devra donc tester au moins deux modèles concurrents plutôt que choisir par intuition : adaptation proportionnée à des risques réels, et expansion bureaucratique/industrielle alimentée par ses propres incitations. Les deux peuvent aussi coexister.

## Plafond probatoire

```text
I0 acteurs/autorités/relations              = VERIFIED
I1 ressources/capacité                      = VERIFIED
I2 financement, sélection, activité         = VERIFIED
I3 coordination/tasking                     = VERIFIED pour règles de programme ; hidden content-specific tasking NOT_ESTABLISHED
I4 livrables/exposition/capacité             = VERIFIED/PARTIAL
I5 réception/motif politique                 = NOT_ESTABLISHED generally
I6 changement comportemental                 = NOT_ESTABLISHED
I7 résultat politique/électoral contrefactuel = NOT_ESTABLISHED
```

Le delta terminal est donc : **financement public récurrent, orientation programmatique, sélection et capacité d’action établis ; commandement éditorial/modération générale et effet politique causal non établis.**
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:5|SRC_COMPLETE:14/14

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-07
- **notes:**
  - DILCRAH 2025 national/local calls
  - FIPD 2025 envelope €52.7m
  - EU 2025/2026 information-integrity and media-literacy calls
  - EDMO funding summary current in 2026
- **status:** CURRENT_THROUGH_2026
- **window:** 2018-2026

### MANIPULATION_REPORT
- **assumptions:**
  - official call documents establish formal program design, not hidden motive
  - budget totals establish resource scale, not effectiveness
  - stated deliverables establish expected activity, not downstream editorial command
- **clusters:**
  - **loaded:**
    - clusters/MONEY.md
    - clusters/POWER.md
    - clusters/NETWORK.md
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - public funding creates bounded capacity and agenda incentives
  - multiple vehicles coexist and should be separated
  - program alignment can be real without censorship command
- **input_kind:** RUN_CARD
- **mission_mode:** RECHECK_EXTEND
- **patterns:**
  - grant
  - procurement
  - CPO
  - counter-speech
  - hate reporting
  - media literacy
  - EDMO
  - CERV
- **priorities:**
  - resource flow
  - selection authority
  - deliverable design
  - accountability
  - negative controls
  - causal ceiling
- **query_guidance:** prove each vehicle and obligation from official program text; distinguish eligibility and funded deliverables from instruction over specific content
- **rhetorical:**
  - **AUTH:** public program documents prove formal rules only
  - **BF:** N/A
  - **DEM:** examples do not establish a universal command architecture
  - **FAC:** separate finance, eligibility, output, removal and political effect
  - **NUM:** budget growth does not establish fabricated threat or effectiveness
- **speaker:**
  - **goal:** forensic funding/influence assessment
  - **target:** objective -> money -> actor -> output -> control/effect
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
  - funding=command
  - public support=censorship
  - deliverable=removal
  - capacity=political effect

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - complete beneficiary concentration and renewal rates
  - **input_ids:**
    - FCT-001
    - FCT-006
    - FCT-008
    - FCT-019
    - FCT-022
    - FCT-025
    - FCT-026
  - **module:** clusters/MONEY.md
  - **negative_results:**
    - budget magnitude does not establish effectiveness or command
  - **not_computable:**
    - total ecosystem market share
  - **operations_applied:**
    - mapped funder-to-vehicle-to-beneficiary class
    - separated grants from procurement
  - **reason:** public budgets, grant envelopes and procurement
  - **result_ids:**
    - CLM-001
    - CLM-003
    - CTRL-002
  - **status:** DONE
  - **trigger:** €
- **item 2:**
  - **gaps:**
    - case-specific private instructions/contracts
  - **input_ids:**
    - FCT-003
    - FCT-004
    - FCT-007
    - FCT-010
    - FCT-012
    - FCT-017
    - FCT-018
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no general removal command established
  - **not_computable:**
    - informal chilling/selection effects
  - **operations_applied:**
    - identified decision authorities
    - separated program alignment from editorial command
  - **reason:** eligibility, selection, objectives and reporting create bounded programmatic authority
  - **result_ids:**
    - CLM-002
    - CLM-004
    - CLM-005
    - CTRL-001
    - CTRL-004
  - **status:** DONE
  - **trigger:** ↕
- **item 3:**
  - **gaps:**
    - beneficiary-to-platform workflow records
  - **input_ids:**
    - FCT-005
    - FCT-011
    - FCT-014
    - FCT-023
    - FCT-024
    - FCT-027
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - network participation does not establish hidden coordination
  - **not_computable:**
    - unrecorded informal influence
  - **operations_applied:**
    - mapped institutional interfaces
    - kept overlap distinct from coordination/command
  - **reason:** interfaces among ministries, prefectures, civil society, consortia and EDMO
  - **result_ids:**
    - CLM-003
    - CLM-006
    - LED-001
    - LED-002
  - **status:** DONE
  - **trigger:** 🌐

### SCOPING_REPORT
- **excluded:**
  - Fonds Marianne as main case (INV-078)
  - fact-check certification gate already closed in INV-045
  - generic claims of censorship without documented funding/action edge
- **guards:**
  - funding != command
  - grant != procurement
  - service_contract != editorial_control
  - monitoring != removal
  - public_support != censorship
  - output != political_effect
  - overlap != coordination
- **included:**
  - DILCRAH national/local anti-hate grants
  - FIPD radicalisation-prevention grants
  - Ministry of Culture media-information literacy grants
  - EU media-literacy/disinformation calls
  - EDMO procurement/grants
  - CERV anti-hate civil-society funding
- **routes:**
  - INV-088
  - INV-144

### CREDO
- funding != command
- grant != procurement
- program objective != content order
- monitoring != removal
- public support != censorship
- capacity != political effect
- overlap != coordination

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** RECHECK_EXTEND
- **patterns:**
  - public grants
  - calls for proposals
  - procurement
  - decentralised subsidies
  - counter-speech
  - media literacy
  - disinformation resilience
  - reporting/evaluation
- **priorities:**
  - who funds
  - vehicle
  - eligibility
  - deliverables
  - reporting
  - command boundary
  - effect ceiling
- **query_guidance:** trace public objective -> vehicle -> selection -> funded actor -> deliverable -> control -> downstream effect
- **speaker:**
  - **goal:** classify public support as bounded capacity/agenda infrastructure
  - **target:** funder-vehicle-beneficiary-output-control-effect chain
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **threats:**
  - funding=command
  - grant=procurement
  - monitoring=removal
  - output=effect

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** Calls explicitly define eligible themes, target groups, deliverables, reporting and award decisions.
  - **resolution:** Public funding creates real bounded agenda/capacity incentives and administrative gatekeeping without automatically creating editorial command.
  - **thesis:** Publicly funded anti-disinformation/anti-hate actors are merely independent civil society with no structural state influence.
- **item 2:**
  - **antithesis:** The examined calls fund awareness, counter-speech, reporting, education, detection and resilience; they do not establish a general order to remove specific lawful political content.
  - **resolution:** Funding of counter-influence activity is established; general censorship command is not.
  - **thesis:** State funding of counter-speech and disinformation work proves censorship.
- **item 3:**
  - **antithesis:** The corpus separates grants, decentralised subsidies, multi-year agreements and public procurement.
  - **resolution:** Vehicle-specific authority and obligations must be analysed separately.
  - **thesis:** All relationships are equivalent subsidies.
- **item 4:**
  - **antithesis:** Program metrics and activity outputs do not close persuasion or counterfactual electoral results.
  - **resolution:** Capacity/output are evidenced; high causal effect remains open.
  - **thesis:** Budgets and outputs prove political effectiveness.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **boundary:** selection/control documented; command not established
  - **from:** DILCRAH
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-004
  - **to:** eligible associations/institutions
  - **vehicle:** national grant call
- **item 2:**
  - **boundary:** program objectives shape eligibility
  - **from:** SG-CIPDR / FIPD
  - **support:**
    - FCT-008
    - FCT-011
    - FCT-013
    - FCT-014
  - **to:** radicalisation-prevention project holders
  - **vehicle:** central allocation -> delegated prefectural grants
- **item 3:**
  - **boundary:** grant != procurement; capacity != editorial command
  - **from:** European Commission
  - **support:**
    - FCT-019
    - FCT-022
    - FCT-024
    - FCT-025
    - FCT-026
  - **to:** consortia, hubs, civil-society/research/media actors
  - **vehicle:** Creative Europe/DIGITAL/PPPA grants plus EDMO procurement

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** DILCRAH / prefectures
  - **limits:**
    - grant != command
  - **relation:** national/local grants and CPOs
  - **support:**
    - FCT-001
    - FCT-005
    - FCT-006
    - FCT-007
  - **to:** associations and institutions
- **item 2:**
  - **from:** SG-CIPDR / prefects
  - **limits:**
    - prevention objective != political censorship
  - **relation:** FIPD orientations and grants
  - **support:**
    - FCT-008
    - FCT-009
    - FCT-010
    - FCT-011
    - FCT-013
    - FCT-014
  - **to:** public/private prevention actors
- **item 3:**
  - **from:** European Commission / agencies
  - **limits:**
    - funding/procurement vehicle must be distinguished
    - output != effect
  - **relation:** grants and procurement
  - **support:**
    - FCT-019
    - FCT-022
    - FCT-024
    - FCT-025
    - FCT-026
    - FCT-027
  - **to:** media-literacy, resilience and EDMO actors

### IMPACT_MAP
- **beneficiary_capacity:** VERIFIED/PARTIAL
- **electoral_effect:** NOT_ESTABLISHED_COUNTERFACTUALLY
- **political_behavior:** NOT_ESTABLISHED
- **programmatic_agenda_setting:** VERIFIED
- **public_funding_scale:** VERIFIED_BOUNDED
- **specific_content_removal_command:** NOT_ESTABLISHED
- **support:**
  - FCT-001
  - FCT-008
  - FCT-019
  - FCT-022
  - FCT-025
  - FCT-026
  - FCT-028

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** funders define eligible themes/deliverables and select projects
  - **issue:** civil-society autonomy versus public agenda-setting
  - **pro:** beneficiaries are non-state or mixed actors
  - **resolution:** BOUNDED_PROGRAMMATIC_INFLUENCE
- **item 2:**
  - **contra:** no general specific-lawful-content removal order in the examined instruments
  - **issue:** support versus censorship
  - **pro:** some programs finance counter-speech/reporting/disinformation detection
  - **resolution:** SUPPORT_ESTABLISHED_COMMAND_NOT_ESTABLISHED
- **item 3:**
  - **contra:** procurement and grant mechanisms impose different legal relationships
  - **issue:** grant versus procurement
  - **pro:** both transfer public resources to ecosystem actors
  - **resolution:** VEHICLE_SEPARATION_REQUIRED
- **item 4:**
  - **contra:** no voter/electoral causal design in corpus
  - **issue:** activity versus political effect
  - **pro:** funded projects produce campaigns, tools, training and monitoring
  - **resolution:** EFFECT_CEILING_I5_I7_OPEN

### VERIFICATION_REPORT
- **cross_checks:**
  - DILCRAH objectives versus award/control process
  - FIPD statutory purpose versus local program R deliverables
  - EU grants versus EDMO procurement
  - program outputs versus absence of general removal command
- **facts:** 28
- **limitations:**
  - no complete beneficiary-level census
  - no private instruction records
  - no comparable denominator of rejected/renewed grantees
  - no causal political-outcome dataset
- **negative_controls:**
  - grant/procurement distinction
  - formal reporting/evaluation duties
  - program objectives stop short of general lawful-content removal order
- **primary_or_official_dominant:** true
- **provenance_families:** 6
- **sources:** 14
- **verdict:** READY_FOR_PRE_GATE

### EDI_REPORT
- **corpus:**
  - **circularity:** LOW_TO_MODERATE_OFFICIAL_PROGRAM_DOCUMENTS
  - **coverage:** STRONG_FOR_FORMAL_FUNDING_VEHICLES_ELIGIBILITY_DELIVERABLES_AND_REPORTING_PARTIAL_FOR_BENEFICIARY_LEVEL_OUTCOMES
  - **independence:** SIX_PROVENANCE_FAMILIES_DILCRAH_CIPDR_LEGIFRANCE_CULTURE_EC_CERV
  - **limits:**
    - official sources describe their own programs
    - not a complete beneficiary-level census
    - private contract/tasking records unavailable
    - no causal electoral dataset
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **gap_type:** SCOPE
    - **independent_families:** 5
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 5
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** YES
    - **gap_type:** SCOPE
    - **independent_families:** 4
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** YES
    - **gap_type:** QUALIFICATION
    - **independent_families:** 5
  - **item 5:**
    - **claim_id:** CLM-006
    - **direct_object:** NO_GENERAL_COMMAND_CHAIN
    - **gap_type:** CAUSALITY
    - **independent_families:** 6
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** 6_PROVENANCE_FAMILIES
  - **perspective:** FRENCH_INTERMINISTERIAL+PREFECTURAL+CULTURE+EU_COMMISSION+CERV
  - **stratification:** GRANTS+PROCUREMENT+DECENTRALISATION+CPO+DELIVERABLES+REPORTING
  - **temporal:** 2018-2026
- **edi:**
  - **assessment:** STRONG_FORMAL_RESOURCE_AND_PROGRAM_DESIGN_COVERAGE_WITH_COMMAND_AND_HIGH_CAUSAL_GAPS
  - **flags:**
    - PRIMARY_OFFICIAL_DOMINANT
    - MULTIPLE_VEHICLES
    - EXPLICIT_REPORTING_CONTROLS
    - NO_GENERAL_CONTENT_REMOVAL_COMMAND
    - NO_CAUSAL_ELECTORAL_DESIGN
- **source_counts:**
  - **claim_source:** 0
  - **primary:** 14
  - **provenance_families:** 6
  - **secondary:** 0
  - **total:** 14

### RESPONSIBILITY_MAP
- **boundary:** public authorities can set program goals, eligibility, award criteria and reporting; this does not establish control of each downstream editorial/moderation decision
- **not_established:**
  - general public instruction to remove specific lawful political content
  - general editorial command over beneficiaries
  - causal voter persuasion
  - counterfactual electoral result
- **verified:**
  - DILCRAH award/control process
  - FIPD statutory and program objectives
  - EMI grant/evaluation requirements
  - EU grant and procurement budgets
  - specified anti-hate/disinformation/media-literacy activities

### NEXT_QUERIES
- RECHECK only if beneficiary-level contracts or instructions reveal content-specific tasking
- RECHECK if complete grant-beneficiary datasets allow concentration/renewal analysis
- DEFER political-effect claim pending exposure/outcome design

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-004,QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-001,FCT-008,FCT-019,FCT-022,FCT-025,FCT-026 | final:GAP | gap:SCOPE
LED-002 | attempts:QRY-015,QRY-016,QRY-017 | support:- | counter:- | results:FCT-028 | final:GAP | gap:RESPONSIBILITY
AXS-001 | attempts:QRY-001,QRY-003,QRY-004,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-001,FCT-006,FCT-008,FCT-019,FCT-022,FCT-024,FCT-025,FCT-026,FCT-027 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-003,QRY-006,QRY-010,QRY-014 | support:- | counter:- | results:FCT-002,FCT-004,FCT-007,FCT-012,FCT-020,FCT-027 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-001,QRY-005,QRY-008,QRY-010,QRY-011,QRY-013,QRY-014 | support:- | counter:- | results:FCT-003,FCT-009,FCT-010,FCT-015,FCT-016,FCT-021,FCT-022,FCT-026,FCT-027 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-002,QRY-003,QRY-006,QRY-007,QRY-012 | support:- | counter:- | results:FCT-005,FCT-006,FCT-011,FCT-013,FCT-014,FCT-024 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-001,QRY-003,QRY-009 | support:- | counter:- | results:FCT-004,FCT-007,FCT-017,FCT-018 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-015,QRY-016,QRY-017 | support:- | counter:- | results:FCT-028 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,QRY-003,QRY-004,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,SRC-001,SRC-003,SRC-004,SRC-010,SRC-011,SRC-012,SRC-013,SRC-014 | support:FCT-001,FCT-006,FCT-008,FCT-019,FCT-022,FCT-025,FCT-026,FCT-027 | counter:CTRL-001 | results:FCT-001,FCT-006,FCT-008,FCT-019,FCT-022,FCT-025,FCT-026,FCT-027,CTRL-001 | final:SUPPORTED | gap:SCOPE
CLM-002 | attempts:QRY-001,QRY-005,QRY-009,QRY-010,QRY-011,QRY-013,QRY-014,SRC-001,SRC-005,SRC-009,SRC-010,SRC-011,SRC-013,SRC-014 | support:FCT-003,FCT-010,FCT-017,FCT-018,FCT-021,FCT-022,FCT-026,FCT-027 | counter:CTRL-003 | results:FCT-003,FCT-010,FCT-017,FCT-018,FCT-021,FCT-022,FCT-026,FCT-027,CTRL-003 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-003 | attempts:QRY-002,QRY-003,QRY-006,QRY-007,QRY-012,SRC-002,SRC-003,SRC-006,SRC-007,SRC-012 | support:FCT-005,FCT-006,FCT-011,FCT-014,FCT-024,FCT-025 | counter:CTRL-002 | results:FCT-005,FCT-006,FCT-011,FCT-014,FCT-024,FCT-025,CTRL-002 | final:SUPPORTED | gap:SCOPE
CLM-004 | attempts:QRY-001,QRY-005,QRY-010,QRY-011,QRY-013,QRY-014,SRC-001,SRC-005,SRC-010,SRC-011,SRC-013,SRC-014 | support:FCT-003,FCT-010,FCT-021,FCT-022,FCT-026,FCT-027 | counter:CTRL-003 | results:FCT-003,FCT-010,FCT-021,FCT-022,FCT-026,FCT-027,CTRL-003 | final:SUPPORTED | gap:QUALIFICATION
CLM-005 | attempts:QRY-001,QRY-003,QRY-006,QRY-009,SRC-001,SRC-003,SRC-006,SRC-009 | support:FCT-004,FCT-007,FCT-012,FCT-017,FCT-018 | counter:CTRL-004 | results:FCT-004,FCT-007,FCT-012,FCT-017,FCT-018,CTRL-004 | final:SUPPORTED | gap:BIAS
CLM-006 | attempts:QRY-001,QRY-005,QRY-008,QRY-010,QRY-011,QRY-012,QRY-014,SRC-001,SRC-005,SRC-008,SRC-010,SRC-011,SRC-012,SRC-014 | support:FCT-028 | counter:CTRL-005 | results:FCT-028,CTRL-005 | final:SUPPORTED | gap:RESPONSIBILITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-001 | CLM | SUPPORTED | SCOPE | The corpus is a mechanism sample, not a complete beneficiary-level census.
CLM-002 | CLM | SUPPORTED | RESPONSIBILITY | Programmatic alignment does not establish instruction over each downstream publication or moderation decision.
CLM-003 | CLM | SUPPORTED | SCOPE | Not every contractual term or beneficiary subgrant is public.
CLM-004 | CLM | SUPPORTED | QUALIFICATION | These objectives do not by themselves prove censorship of lawful political speech.
CLM-005 | CLM | SUPPORTED | BIAS | Formal controls do not prove perfect neutrality or effectiveness.
CLM-006 | CLM | SUPPORTED | RESPONSIBILITY | Case-specific contracts, instructions or platform workflows could change the responsibility assessment if produced.
CAU-001 | CAU | GAP | CAUSALITY | The chain is well evidenced through program design, selection and funded capacity/outputs, but not as a general chain to specific lawful-content removal, persuasion or electoral outcome.

SEMANTIC_COUNTS_V1:LED:2|CLM:6|AXS:6|CAU:1|CTRL:6|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-004","QRY-010","QRY-011","QRY-012","QRY-013"],"evidence_excerpt":"Recurring French and EU instruments finance anti-hate, radicalisation-prevention, media-literacy and disinformation-resilience capacity through several vehicles.","gap":"Complete beneficiary-level market map, concentration, renewal rates and outcome metrics remain incomplete.","gap_type":"SCOPE","kind":"SYSTEM_GAP","lead":"Publicly financed counter-influence ecosystem as an economy of programs, grants and procurement","linked_ids":["CLM-001","CLM-002","CLM-003","CAU-001"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-008","FCT-019","FCT-022","FCT-025","FCT-026"],"routes":["INV-144"],"source_id":"INV-079_RUN_CARD","status":"GAP"}
LED-002 | {"attempt_ids":["QRY-015","QRY-016","QRY-017"],"evidence_excerpt":"Program objectives and reporting are documented; a general instruction chain to specific lawful-content removal or electoral effect is not.","gap":"Need contracts/instructions/workflow records and causal exposure-outcome data.","gap_type":"RESPONSIBILITY","kind":"RESPONSIBILITY_GAP","lead":"Funding/capacity to command, removal and political effect","linked_ids":["CLM-006","CTRL-005","CTRL-006","CAU-001"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-028"],"routes":["INV-088","INV-144","INV-133"],"source_id":"INV-079_RUN_CARD","status":"GAP"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"France and the EU maintain a real, recurring and materially funded ecosystem of associations, consortia and service providers working on anti-hate, radicalisation prevention, media literacy and disinformation resilience.","claimant":"INV-079 synthesis","counter":"CTRL-001","gap":"The corpus is a mechanism sample, not a complete beneficiary-level census.","gap_type":"SCOPE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-006","FCT-008","FCT-019","FCT-022","FCT-025","FCT-026","FCT-027"]}
CLM-002 | {"claim":"Funding rules can shape capacity and agenda at the program level by defining eligible themes, target groups, expected deliverables and reporting obligations.","claimant":"INV-079 synthesis","counter":"CTRL-003","gap":"Programmatic alignment does not establish instruction over each downstream publication or moderation decision.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-003","FCT-010","FCT-017","FCT-018","FCT-021","FCT-022","FCT-026","FCT-027"]}
CLM-003 | {"claim":"The financing architecture is plural rather than unitary: national calls, decentralised grants, multi-year agreements, EU grants and public procurement coexist.","claimant":"INV-079 synthesis","counter":"CTRL-002","gap":"Not every contractual term or beneficiary subgrant is public.","gap_type":"SCOPE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-005","FCT-006","FCT-011","FCT-014","FCT-024","FCT-025"]}
CLM-004 | {"claim":"Some public programs explicitly finance counter-speech, hate-speech reporting, disinformation detection/analysis, resilience campaigns and media-literacy outputs.","claimant":"INV-079 synthesis","counter":"CTRL-003","gap":"These objectives do not by themselves prove censorship of lawful political speech.","gap_type":"QUALIFICATION","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-003","FCT-010","FCT-021","FCT-022","FCT-026","FCT-027"]}
CLM-005 | {"claim":"Selection, financial reporting and evaluation requirements are materially documented, so state support is accompanied by administrative gatekeeping and accountability mechanisms.","claimant":"INV-079 synthesis","counter":"CTRL-004","gap":"Formal controls do not prove perfect neutrality or effectiveness.","gap_type":"BIAS","materiality":"HIGH","status":"SUPPORTED","support":["FCT-004","FCT-007","FCT-012","FCT-017","FCT-018"]}
CLM-006 | {"claim":"The examined corpus does not establish a general chain public funder -> funded actor -> mandated removal of specific lawful political content -> political/electoral effect.","claimant":"INV-079 synthesis","counter":"CTRL-005","gap":"Case-specific contracts, instructions or platform workflows could change the responsibility assessment if produced.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-028"]}

### AXIS_REGISTRY_V1
AXS-001 | {"assessment":"VERIFIED_BOUNDED","attempt_ids":["QRY-001","QRY-003","QRY-004","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014"],"axis":"funding_flows","links":["CLM-001","CLM-003"],"question":"Which public budgets and instruments support the relevant actors?","result_ids":["FCT-001","FCT-006","FCT-008","FCT-019","FCT-022","FCT-024","FCT-025","FCT-026","FCT-027"],"sought_objects":["BUDGET","GRANT","CONTRACT","CPO"],"status":"SATURATED"}
AXS-002 | {"assessment":"VERIFIED","attempt_ids":["QRY-001","QRY-003","QRY-006","QRY-010","QRY-014"],"axis":"selection_and_eligibility","links":["CLM-002","CLM-005"],"question":"Who can apply and how are projects selected?","result_ids":["FCT-002","FCT-004","FCT-007","FCT-012","FCT-020","FCT-027"],"sought_objects":["ELIGIBILITY","SELECTION","AWARD_COMMISSION","CONSORTIUM"],"status":"SATURATED"}
AXS-003 | {"assessment":"VERIFIED","attempt_ids":["QRY-001","QRY-005","QRY-008","QRY-010","QRY-011","QRY-013","QRY-014"],"axis":"deliverables_and_activity","links":["CLM-002","CLM-004"],"question":"What activities and outputs are public funds designed to purchase or support?","result_ids":["FCT-003","FCT-009","FCT-010","FCT-015","FCT-016","FCT-021","FCT-022","FCT-026","FCT-027"],"sought_objects":["COUNTER_SPEECH","REPORTING","MEDIA_LITERACY","DETECTION","TRAINING"],"status":"SATURATED"}
AXS-004 | {"assessment":"VERIFIED","attempt_ids":["QRY-002","QRY-003","QRY-006","QRY-007","QRY-012"],"axis":"vehicle_and_authority","links":["CLM-003","CTRL-002"],"question":"Are relationships grants, procurement, decentralised subsidies or other vehicles, and who controls them?","result_ids":["FCT-005","FCT-006","FCT-011","FCT-013","FCT-014","FCT-024"],"sought_objects":["GRANT","PROCUREMENT","PREFECT","COMMITTEE"],"status":"SATURATED"}
AXS-005 | {"assessment":"VERIFIED_BOUNDED","attempt_ids":["QRY-001","QRY-003","QRY-009"],"axis":"accountability_and_effectiveness","links":["CLM-005","CTRL-004"],"question":"What reporting, evaluation and control duties accompany the funding?","result_ids":["FCT-004","FCT-007","FCT-017","FCT-018"],"sought_objects":["REPORT","INDICATOR","EVALUATION","FINANCIAL_CONTROL"],"status":"SATURATED"}
AXS-006 | {"assessment":"NOT_ESTABLISHED_FOR_COMMAND_OR_I6_I7","attempt_ids":["QRY-015","QRY-016","QRY-017"],"axis":"command_and_political_effect","links":["CLM-006","CTRL-005","CTRL-006"],"question":"Does public funding establish editorial/moderation command or political/electoral effect?","result_ids":["FCT-028"],"sought_objects":["TASKING","CONTENT_REMOVAL","EDITORIAL_CONTROL","POLITICAL_EFFECT"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"CTRL-002;CTRL-004;CTRL-005;CTRL-006","gap":"The chain is well evidenced through program design, selection and funded capacity/outputs, but not as a general chain to specific lawful-content removal, persuasion or electoral outcome.","gap_type":"CAUSALITY","limit":"Public funding can shape eligible agendas and capacity without proving downstream command or political effect.","mechanism":"public objective -> call/eligibility -> selection/grant or procurement -> funded capacity -> specified output/activity -> audience/platform/institutional exposure -> possible moderation or opinion effect -> possible political/electoral result","status":"GAP","support":["FCT-001","FCT-003","FCT-004","FCT-010","FCT-017","FCT-021","FCT-022","FCT-024","FCT-026"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"French and EU instruments document explicit eligibility, objectives, budgets and reporting/evaluation requirements rather than unrestricted transfers.","status":"VERIFIED","support":["FCT-001","FCT-004","FCT-006","FCT-007","FCT-017","FCT-018","FCT-019","FCT-020"]}
CTRL-002 | {"control":"Public funding uses distinct legal/administrative vehicles, including grants, decentralised subsidies, multi-year agreements and procurement; these vehicles should not be conflated.","status":"VERIFIED","support":["FCT-005","FCT-011","FCT-014","FCT-024","FCT-025"]}
CTRL-003 | {"control":"Several programs expressly support counter-speech, reporting of online hate, disinformation detection, media literacy or resilience, so public funding can shape the category of eligible activity and organisational capacity.","status":"VERIFIED","support":["FCT-003","FCT-009","FCT-010","FCT-015","FCT-016","FCT-021","FCT-022","FCT-026","FCT-027"]}
CTRL-004 | {"control":"Selection and monitoring mechanisms are documented in DILCRAH, FIPD and EMI calls, limiting the inference that grants are uncontrolled transfers.","status":"VERIFIED","support":["FCT-004","FCT-007","FCT-012","FCT-017","FCT-018"]}
CTRL-005 | {"control":"The examined public documents establish programmatic objectives and deliverables, not a general public-authority command chain over specific editorial conclusions or lawful-content removals.","status":"VERIFIED_NEGATIVE","support":["FCT-028"]}
CTRL-006 | {"control":"No examined source closes the high causal chain from public grant or contract to voter persuasion or counterfactual electoral outcome.","status":"VERIFIED_NEGATIVE","support":["FCT-028"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:17|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | MNEMO_UNAVAILABLE degraded; exact snapshot search unavailable in this environment | MnemoLite | NONE | MNEMO_Q
SYS-003 | SYS | PARTIAL | runtime | ATTEMPT-001 | PERSIST_REBIND
SYS-004 | SYS | PASS | runtime | ATTEMPT-002 | PERSIST_REBIND
QRY-001 | FETCH | PASS | SRC-001 | https://www.dilcrah.gouv.fr/actualites/lancement-de-lappel-projets-national-2025-en-faveur-de-la-lutte-contre-la-haine-et-les-discriminations | FETCH exact source for INV-079: DILCRAH — appel national 2025
QRY-002 | FETCH | PASS | SRC-002 | https://www.dilcrah.gouv.fr/la-delegation/soutien-aux-associations | FETCH exact source for INV-079: DILCRAH — soutien aux associations
QRY-003 | FETCH | PASS | SRC-003 | https://www.dilcrah.gouv.fr/files/2025-08/Guide%20de%20l%27appel%20%C3%A0%20projets%20local%202025.pdf | FETCH exact source for INV-079: DILCRAH — guide appel local 2025
QRY-004 | FETCH | PASS | SRC-004 | https://www.cipdr.gouv.fr/circulaire-fipd-2025/ | FETCH exact source for INV-079: SG-CIPDR — circulaire FIPD 2025
QRY-005 | FETCH | PASS | SRC-005 | https://www.eure.gouv.fr/contenu/telechargement/56864/419004/file/AAP%20FIPD%202025.pdf | FETCH exact source for INV-079: Préfecture Eure — FIPD 2025 Programme R
QRY-006 | FETCH | PASS | SRC-006 | https://www.prefectures-regions.gouv.fr/ile-de-france/Region-et-institutions/L-action-de-l-Etat/Cohesion-sociale-vie-associative-sport-et-jeunesse/Fonds-interministeriel-de-prevention-de-la-delinquance-lancement-de-l-appel-a-projets-2025 | FETCH exact source for INV-079: Préfecture IDF — FIPD Paris 2025
QRY-007 | FETCH | PASS | SRC-007 | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000025503132/LEGISCTA000039438438/2025-12-31 | FETCH exact source for INV-079: Légifrance — FIPD legal basis
QRY-008 | FETCH | PASS | SRC-008 | https://www.culture.gouv.fr/catalogue-des-demarches-et-subventions/appels-a-projets-candidatures/education-aux-medias-et-a-l-information-emi-residences-de-journalistes | FETCH exact source for INV-079: Ministère de la Culture — EMI national support
QRY-009 | FETCH | PASS | SRC-009 | https://www.culture.gouv.fr/catalogue-des-demarches-et-subventions/appels-a-projet-partenaires/appel-a-projet-education-aux-medias-et-a-l-information | FETCH exact source for INV-079: DRAC Pays de la Loire — EMI 2026
QRY-010 | FETCH | PASS | SRC-010 | https://digital-strategy.ec.europa.eu/en/funding/call-proposals-cross-border-media-literacy-projects | FETCH exact source for INV-079: European Commission — Cross-border Media Literacy 2024
QRY-011 | FETCH | PASS | SRC-011 | https://digital-strategy.ec.europa.eu/en/news/eu-funding-eu5-million-strengthen-media-literacy-and-resilience-disinformation | FETCH exact source for INV-079: European Commission — nearly €5m media literacy/disinformation calls
QRY-012 | FETCH | PASS | SRC-012 | https://digital-strategy.ec.europa.eu/en/policies/european-digital-media-observatory | FETCH exact source for INV-079: European Commission — EDMO funding architecture
QRY-013 | FETCH | PASS | SRC-013 | https://digital-strategy.ec.europa.eu/en/funding/supporting-trustworthy-social-media-sphere-young-europeans | FETCH exact source for INV-079: European Commission — trustworthy social media sphere 2025
QRY-014 | FETCH | PASS | SRC-014 | https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/cerv/wp-call/2025/call-fiche_cerv-2025-equal_en.pdf | FETCH exact source for INV-079: EU CERV — Equality 2025 call
QRY-015 | FETCH | PASS | - | https://digital-strategy.ec.europa.eu/en/news/eu-funding-eu5-million-strengthen-media-literacy-and-resilience-disinformation | REFUTATION: seek primary evidence that public funding instruments directly command removal of specific lawful political content or dictate individual editorial conclusions
QRY-016 | FETCH | NONE | - | https://www.dilcrah.gouv.fr/actualites/lancement-de-lappel-projets-national-2025-en-faveur-de-la-lutte-contre-la-haine-et-les-discriminations | REFUTATION: seek primary evidence contradicting the documented DILCRAH instruction, award-commission and effectiveness-control process
QRY-017 | FETCH | NONE | - | https://www.eure.gouv.fr/contenu/telechargement/56864/419004/file/AAP%20FIPD%202025.pdf | REFUTATION: seek primary evidence contradicting the documented Programme R scope including counter-speech, awareness, training and conspiracy/separatism prevention

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | DILCRAH-NAT-2025 | DILCRAH — appel national 2025 | 2025-03-19 | 2026-09-07T23:44:00+02:00 | budget, priorities, eligibility, selection, control | https://www.dilcrah.gouv.fr/actualites/lancement-de-lappel-projets-national-2025-en-faveur-de-la-lutte-contre-la-haine-et-les-discriminations
SRC-002 | ◈ | fam:A | DILCRAH-SUPPORT | DILCRAH — soutien aux associations | 2026-09-07 | 2026-09-07T23:44:00+02:00 | national/local calls, CPO, controls, project scope | https://www.dilcrah.gouv.fr/la-delegation/soutien-aux-associations
SRC-003 | ◈ | fam:A | DILCRAH-LOCAL-2025 | DILCRAH — guide appel local 2025 | 2025-01-01 | 2026-09-07T23:44:00+02:00 | local envelope, CORAH, financial reporting | https://www.dilcrah.gouv.fr/files/2025-08/Guide%20de%20l%27appel%20%C3%A0%20projets%20local%202025.pdf
SRC-004 | ◈ | fam:B | CIPDR-FIPD-2025 | SG-CIPDR — circulaire FIPD 2025 | 2025-06-12 | 2026-09-07T23:44:00+02:00 | national FIPD envelope and strategic allocation | https://www.cipdr.gouv.fr/circulaire-fipd-2025/
SRC-005 | ◈ | fam:B | EURE-FIPD-R-2025 | Préfecture Eure — FIPD 2025 Programme R | 2025-01-01 | 2026-09-07T23:44:00+02:00 | radicalisation, counter-speech, training, conspiracy/separatism | https://www.eure.gouv.fr/contenu/telechargement/56864/419004/file/AAP%20FIPD%202025.pdf
SRC-006 | ◈ | fam:B | IDF-FIPD-2025 | Préfecture IDF — FIPD Paris 2025 | 2024-12-11 | 2026-09-07T23:44:00+02:00 | grant framework and republican engagement contract | https://www.prefectures-regions.gouv.fr/ile-de-france/Region-et-institutions/L-action-de-l-Etat/Cohesion-sociale-vie-associative-sport-et-jeunesse/Fonds-interministeriel-de-prevention-de-la-delinquance-lancement-de-l-appel-a-projets-2025
SRC-007 | ◈ | fam:C | LEGIFRANCE-FIPD | Légifrance — FIPD legal basis | 2019-12-01 | 2026-09-07T23:44:00+02:00 | R132-4-1 and R132-4-2 fund purpose/orientation/delegation | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000025503132/LEGISCTA000039438438/2025-12-31
SRC-008 | ◈ | fam:D | CULTURE-EMI | Ministère de la Culture — EMI national support | 2026-09-07 | 2026-09-07T23:44:00+02:00 | grant support and media-information literacy objectives | https://www.culture.gouv.fr/catalogue-des-demarches-et-subventions/appels-a-projets-candidatures/education-aux-medias-et-a-l-information-emi-residences-de-journalistes
SRC-009 | ◈ | fam:D | CULTURE-EMI-PDL-2026 | DRAC Pays de la Loire — EMI 2026 | 2026-03-13 | 2026-09-07T23:44:00+02:00 | project dossier, budgets, target counts, monitoring indicators | https://www.culture.gouv.fr/catalogue-des-demarches-et-subventions/appels-a-projet-partenaires/appel-a-projet-education-aux-medias-et-a-l-information
SRC-010 | ◈ | fam:E | EC-MEDIA-LITERACY-2024 | European Commission — Cross-border Media Literacy 2024 | 2024-10-22 | 2026-09-07T23:44:00+02:00 | budget, co-financing, eligibility, deliverables | https://digital-strategy.ec.europa.eu/en/funding/call-proposals-cross-border-media-literacy-projects
SRC-011 | ◈ | fam:E | EC-DISINFO-CALLS-2025 | European Commission — nearly €5m media literacy/disinformation calls | 2025-04-30 | 2026-09-07T23:44:00+02:00 | detection, resilience, reach, eligible actors, EDMO collaboration | https://digital-strategy.ec.europa.eu/en/news/eu-funding-eu5-million-strengthen-media-literacy-and-resilience-disinformation
SRC-012 | ◈ | fam:E | EC-EDMO-FUNDING | European Commission — EDMO funding architecture | 2026-07-01 | 2026-09-07T23:44:00+02:00 | procurement vs grants, central and hubs funding | https://digital-strategy.ec.europa.eu/en/policies/european-digital-media-observatory
SRC-013 | ◈ | fam:E | EC-YOUTH-INFO-INTEGRITY-2025 | European Commission — trustworthy social media sphere 2025 | 2025-09-12 | 2026-09-07T23:44:00+02:00 | €6m two-project call, youth, influencers, manipulation/deepfakes | https://digital-strategy.ec.europa.eu/en/funding/supporting-trustworthy-social-media-sphere-young-europeans
SRC-014 | ◈ | fam:other:cerv | CERV-EQUAL-2025 | EU CERV — Equality 2025 call | 2025-01-01 | 2026-09-07T23:44:00+02:00 | civil society anti-hate projects, awareness, victims, data, conspiracy/hate speech | https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/cerv/wp-call/2025/call-fiche_cerv-2025-equal_en.pdf

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.dilcrah.gouv.fr/actualites/lancement-de-lappel-projets-national-2025-en-faveur-de-la-lutte-contre-la-haine-et-les-discriminations | A | 2025-03-19 | DILCRAH national 2025 budget | The DILCRAH 2025 national call allocated €7.7 million to support associations, a 7% increase from the previous year. | -
FCT-002 | FACT | ✧ | https://www.dilcrah.gouv.fr/actualites/lancement-de-lappel-projets-national-2025-en-faveur-de-la-lutte-contre-la-haine-et-les-discriminations | A | 2025-03-19 | DILCRAH eligible entities | The DILCRAH national call was open to non-profit legal persons including associations, public institutions, cultural institutions and educational institutions. | -
FCT-003 | FACT | ✧ | https://www.dilcrah.gouv.fr/actualites/lancement-de-lappel-projets-national-2025-en-faveur-de-la-lutte-contre-la-haine-et-les-discriminations | A | 2025-03-19 | DILCRAH online-hate priorities | DILCRAH priorities included production of alternative online speech and development of reporting of hate speech on the Internet. | -
FCT-004 | FACT | ✧ | https://www.dilcrah.gouv.fr/actualites/lancement-de-lappel-projets-national-2025-en-faveur-de-la-lutte-contre-la-haine-et-les-discriminations | A | 2025-03-19 | DILCRAH selection and control | Applications were instructed by DILCRAH and submitted to its grant-award commission; DILCRAH reserved the right to check the reality, effectiveness and alignment of funded actions. | -
FCT-005 | FACT | ✧ | https://www.dilcrah.gouv.fr/la-delegation/soutien-aux-associations | A | 2026-09-07 | DILCRAH durable and local support channels | DILCRAH uses annual national and local calls and also multi-year objective agreements with major long-standing actors. | -
FCT-006 | FACT | ✧ | https://www.dilcrah.gouv.fr/files/2025-08/Guide%20de%20l%27appel%20%C3%A0%20projets%20local%202025.pdf | A | 2025-01-01 | DILCRAH local 2025 envelope | The 2025 local DILCRAH call had an envelope of €3 million and was fully decentralised to prefects. | -
FCT-007 | FACT | ✧ | https://www.dilcrah.gouv.fr/files/2025-08/Guide%20de%20l%27appel%20%C3%A0%20projets%20local%202025.pdf | A | 2025-01-01 | DILCRAH local governance and financial follow-up | Local calls use CORAH/CORAHD-type institutional review and require close scrutiny of financial reports and prior grant-use forms. | -
FCT-008 | FACT | ✧ | https://www.cipdr.gouv.fr/circulaire-fipd-2025/ | B | 2025-06-12 | FIPD 2025 envelope | The 2025 FIPD envelope managed and steered by SG-CIPDR was €52.7 million. | -
FCT-009 | FACT | ✧ | https://www.eure.gouv.fr/contenu/telechargement/56864/419004/file/AAP%20FIPD%202025.pdf | B | 2025-01-01 | FIPD Programme R mission | FIPD Programme R supports actions for prevention of radicalisation. | -
FCT-010 | FACT | ✧ | https://www.eure.gouv.fr/contenu/telechargement/56864/419004/file/AAP%20FIPD%202025.pdf | B | 2025-01-01 | FIPD Programme R activity scope | Programme R can fund counter-speech, public-awareness workshops, professional training, family support and other preventive actions; the call explicitly includes separatism, conspiracy phenomena and sectarian deviations. | -
FCT-011 | FACT | ✧ | https://www.prefectures-regions.gouv.fr/ile-de-france/Region-et-institutions/L-action-de-l-Etat/Cohesion-sociale-vie-associative-sport-et-jeunesse/Fonds-interministeriel-de-prevention-de-la-delinquance-lancement-de-l-appel-a-projets-2025 | B | 2024-12-11 | FIPD grant framework | The Paris 2025 FIPD call describes support as grants to project holders whose actions fit national prevention orientations. | -
FCT-012 | FACT | ✧ | https://www.prefectures-regions.gouv.fr/ile-de-france/Region-et-institutions/L-action-de-l-Etat/Cohesion-sociale-vie-associative-sport-et-jeunesse/Fonds-interministeriel-de-prevention-de-la-delinquance-lancement-de-l-appel-a-projets-2025 | B | 2024-12-11 | Republican engagement condition | Associations seeking FIPD grants must subscribe to the republican engagement contract, including commitments concerning constitutional principles, secularism and public order. | -
FCT-013 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000025503132/LEGISCTA000039438438/2025-12-31 | C | 2019-12-01 | FIPD statutory purpose | Article R132-4-1 of the Internal Security Code provides that FIPD finances delinquency-prevention and radicalisation-prevention actions. | -
FCT-014 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000025503132/LEGISCTA000039438438/2025-12-31 | C | 2019-12-01 | FIPD allocation authority | Article R132-4-2 provides that the interministerial committee sets orientations and eligibility conditions for FIPD credits and that credits are delegated to prefects. | -
FCT-015 | FACT | ✧ | https://www.culture.gouv.fr/catalogue-des-demarches-et-subventions/appels-a-projets-candidatures/education-aux-medias-et-a-l-information-emi-residences-de-journalistes | D | 2026-09-07 | Culture Ministry EMI grant mechanism | The Ministry of Culture supports media and information literacy by allocating grants to project holders. | -
FCT-016 | FACT | ✧ | https://www.culture.gouv.fr/catalogue-des-demarches-et-subventions/appels-a-projets-candidatures/education-aux-medias-et-a-l-information-emi-residences-de-journalistes | D | 2026-09-07 | Culture Ministry EMI objective | The stated EMI objective is to help citizens, especially young people, appropriate information and develop the freedom and capacity to form their own opinion. | -
FCT-017 | FACT | ✧ | https://www.culture.gouv.fr/catalogue-des-demarches-et-subventions/appels-a-projet-partenaires/appel-a-projet-education-aux-medias-et-a-l-information | D | 2026-03-13 | DRAC EMI application evidence | The Pays de la Loire EMI call requires a project description with target-person counts, timetable, planned media production, sustainability prospects and a full projected budget. | -
FCT-018 | FACT | ✧ | https://www.culture.gouv.fr/catalogue-des-demarches-et-subventions/appels-a-projet-partenaires/appel-a-projet-education-aux-medias-et-a-l-information | D | 2026-03-13 | DRAC EMI monitoring indicators | The same call requires monitoring and evaluation indicators for targeted publics, making reporting part of the grant-design rather than leaving outputs unspecified. | -
FCT-019 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/funding/call-proposals-cross-border-media-literacy-projects | E | 2024-10-22 | Creative Europe media literacy budget | The 2024 cross-border media-literacy call had a €2.57 million budget, a maximum EU grant of €500,000 per two-year project and a 70% maximum co-financing rate. | -
FCT-020 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/funding/call-proposals-cross-border-media-literacy-projects | E | 2024-10-22 | Creative Europe eligible consortia | The call required consortia of at least three entities from at least three participating countries and allowed non-profits, public authorities, universities, media organisations and technology providers among eligible participants. | -
FCT-021 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/funding/call-proposals-cross-border-media-literacy-projects | E | 2024-10-22 | Creative Europe expected deliverables | Expected outputs included cross-border media-literacy tools/actions, exchange of best practices and support for media-literacy professionals. | -
FCT-022 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/news/eu-funding-eu5-million-strengthen-media-literacy-and-resilience-disinformation | E | 2025-04-30 | EU 2025 resilience and reach calls | The Commission launched two calls totalling nearly €5 million: €3.15 million for detecting/analyzing malicious manipulation and resilience responses, and about €1.6 million to increase reach and impact of independent fact-checked content. | -
FCT-023 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/news/eu-funding-eu5-million-strengthen-media-literacy-and-resilience-disinformation | E | 2025-04-30 | EU 2025 eligible civil-society/research actors | Civil-society organisations, universities and research centres were among eligible applicants, and winning projects were expected to collaborate with EDMO. | -
FCT-024 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/european-digital-media-observatory | E | 2026-07-01 | EDMO uses both procurement and grants | EDMO central has been financed through public procurement while national/regional hubs have been financed through grants, so procurement and subsidy are distinct vehicles inside the same ecosystem. | -
FCT-025 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/european-digital-media-observatory | E | 2026-07-01 | EDMO funding is materially recurrent | Commission figures list €2.5m then €4m procurement for EDMO central, about €11m for the first eight hubs, €8m for six additional hubs and further refinancing rounds. | -
FCT-026 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/funding/supporting-trustworthy-social-media-sphere-young-europeans | E | 2025-09-12 | EU youth information-integrity call | A €6 million Commission call was designed to fund two projects involving young Europeans and influencers on manipulation techniques, conspiracy theories and malicious uses of generative AI/deepfakes. | -
FCT-027 | FACT | ✧ | https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/cerv/wp-call/2025/call-fiche_cerv-2025-equal_en.pdf | other:cerv | 2025-01-01 | CERV funds civil-society anti-hate capacity | The CERV Equality 2025 call includes support for civil-society projects combating racism and hate, including awareness, victim support, data collection and resilience activities. | -
FCT-028 | FACT | ✧ | https://www.dilcrah.gouv.fr/actualites/lancement-de-lappel-projets-national-2025-en-faveur-de-la-lutte-contre-la-haine-et-les-discriminations | A,B,D,E,other:cerv | 2025-01-01 | Funding documents do not themselves establish content-removal command | Across the examined DILCRAH, FIPD, EMI, Creative Europe, EDMO and CERV instruments, public documents define eligibility, objectives, deliverables, reporting or evaluation; they do not by themselves establish a general instruction chain from funder to removal of specific lawful political content. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-001
FCT-005 | SRC-002
FCT-006 | SRC-003
FCT-007 | SRC-003
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
FCT-021 | SRC-010
FCT-022 | SRC-011
FCT-023 | SRC-011
FCT-024 | SRC-012
FCT-025 | SRC-012
FCT-026 | SRC-013
FCT-027 | SRC-014
FCT-028 | SRC-001,SRC-005,SRC-008,SRC-010,SRC-011,SRC-012,SRC-014

## REFUTATION_REGISTRY_V1
FCT-004 | QRY-016 | NONE
FCT-010 | QRY-017 | NONE
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
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8
CP-002 | SEARCH | PASS | LAST_COMPLETED:9:ECOSYSTEM | NEXT_ACTION:10
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11:CAU-001 | NEXT_ACTION:12
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-07T21:50:40.953730+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PARTIAL","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:CONFIRME","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:CONFIRME","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:CONFIRME","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":28,"eligible":28,"failure":0,"success":0}}
ATTEMPT-002 | {"created_at":"2026-09-07T21:53:08.433150+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":28,"eligible":28,"failure":0,"success":0}}

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
