ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260909-2332-turkey-diaspora-state-mobilisation | PARENT_RUN_ID:NONE | AS_OF:2026-09-09
INPUT_KIND:RUN_CARD | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/inv036/runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-09_turkey-diaspora-state-mobilisation/2026-09-09_23-32_turkey-diaspora-state-mobilisation_INPUT.md | SUBJECT_SLUG:turkey-diaspora-state-mobilisation | SUBJECT_FP:sha256:79d1c546860011425f11493e839fec40bd76789b724e17d78a1382b2fe791d49 | INPUT_SHA256:sha256:0b547fa2dd4239bd2405ce1615ffc37f75950f4e8cb7b88214a6e1aca419570f
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France et Europe, principalement 2015-2026. Tracer institution/acteur turc -> organisation, association, reseau religieux ou intermediaire -> financement, message, consigne ou service -> population/cible -> mobilisation, pression ou action -> effet politique/institutionnel. Gardes: diaspora != proxy; religion != tasking; funding != command; mobilisation != coercion; contact != control; participation != ingerence; action != effet electoral.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/NETWORK.md,clusters/POWER.md,clusters/CONFIRMATION.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
## Question et chaîne testée

INV-036 teste une chaîne actor-specific : institution ou acteur turc -> organisation, réseau religieux ou intermédiaire -> financement, supervision, message, consigne ou service -> population/cible -> mobilisation, pression ou action -> effet politique ou institutionnel. Le corpus sépare explicitement diaspora, religion, influence ouverte, mobilisation électorale, tasking, coercition et effet.

## Diyanet et DITIB : un canal structurel réel, pas un proxy automatique

Les autorités allemandes documentent après 2016 une intensification des tentatives d'influence de l'État turc sur sa diaspora [FCT-001]. Elles décrivent DITIB comme structurellement et personnellement liée à Diyanet et indiquent que l'ambassade et les consulats turcs exercent une supervision de service sur les imams Diyanet envoyés en Allemagne, principalement dans des communautés DITIB [FCT-002]. Le financement turc couvre notamment les coûts de personnel de ces imams [FCT-005]. Ces éléments ferment un canal de ressources, supervision et accès communautaire. Ils ne ferment pas un commandement sur chaque association locale ni sur chaque message [FCT-006].

Deux cas montrent que le canal peut dépasser le service religieux ordinaire. Les autorités allemandes ont documenté un soupçon d'espionnage concernant des imams envoyés par Diyanet, tout en indiquant que ce dossier ne suffisait pas à traiter DITIB dans son ensemble comme organisation d'espionnage [FCT-003,FCT-004]. Elles ont aussi relevé des messages de soutien à l'opération militaire turque en Syrie dans des mosquées DITIB et qualifié cette implication de dépassement du service religieux [FCT-007,FCT-008]. Le mécanisme est donc documenté case-specifically; l'espionnage ou le tasking généralisé ne l'est pas.

## UID et campagnes transnationales : mobilisation politique directe

Le gouvernement allemand décrit l'Union of International Democrats comme l'organisation centrale de lobbying de l'AKP en Allemagne et le renseignement intérieur allemand l'inscrit dans une stratégie active d'influence visant la communauté d'origine turque [FCT-009,FCT-011]. La présence d'environ 1,4 million d'électeurs turcs potentiels en Allemagne lors de l'élection turque de 2018 donne l'échelle du public mobilisable, mais ne mesure pas l'effet causal d'UID sur les votes [FCT-012]. En 2017, les activités de campagne de responsables turcs avaient directement débordé en Allemagne avant que ces apparitions ne cessent [FCT-029,FCT-030]. La chaîne `acteur politique turc -> organisation/campagne -> mobilisation transnationale` est donc supportée; `mobilisation -> vote causé` ne l'est pas.

## France : infrastructure d'influence documentée, prévalence et contrôle non généralisables

Le Sénat français estime que des structures liées à la Turquie peuvent mobiliser la diaspora en soutien au gouvernement Erdogan, notamment lors des périodes électorales, et identifie plusieurs leviers d'influence autour de l'organisation religieuse [FCT-013,FCT-014]. La délégation parlementaire au renseignement décrit DITIB France comme une émanation de Diyanet et évoque environ 250 associations et 120 imams détachés turcs ou d'origine turque dans cette sphère [FCT-015,FCT-016]. Mais un contrôle parlementaire antérieur notait que l'islam turc n'avait pas alors produit en France un impact comparable à d'autres courants, ce qui interdit de transformer l'infrastructure en effet social généralisé [FCT-017]. Les réponses françaises sur les imams détachés et l'enseignement montrent en outre qu'une politique publique peut réduire certains canaux sans prouver la disparition de toute influence [FCT-014,FCT-016].

## YTB : politique diasporique ouverte et organisée

YTB affirme explicitement vouloir renforcer les liens de la diaspora avec la patrie, l'identité et la culture, ainsi que sa position sociale, économique, culturelle et juridique [FCT-019]. Cette politique inclut la participation démocratique dans les pays de résidence [FCT-020]. En 2026, YTB a réuni DITIB, IGMG, ATIB, UID, MÜSIAD et d'autres organisations avec des responsables de l'AKP, de la présidence turque et de la diplomatie [FCT-021,FCT-022]. Le Turkish Diaspora Forum porte explicitement sur la participation politique, l'institutionnalisation associative et la représentation dans les pays d'accueil [FCT-023]. Cela ferme une politique étatique de cultivation de réseaux et de représentation. Comme elle est ouverte et déclarée, elle ne vaut pas par elle-même clandestinité, coercition ou ingérence illicite [FCT-024].

## Vote expatrié : résultat observable, causalité ouverte

Pour le premier tour de la présidentielle turque de 2023, YSK comptait 3 423 759 électeurs inscrits à l'étranger; en France, les résultats pays donnent 126 572 voix à Recep Tayyip Erdogan contre 65 733 à Kemal Kilicdaroglu [FCT-025,FCT-026]. Ces valeurs établissent une participation et une distribution de votes, pas l'effet causal de DITIB, UID, YTB ou d'un autre réseau. L'ODIHR documente par ailleurs un environnement électoral plus large avantageant le président sortant et le parti au pouvoir, ce qui constitue un confondant matériel [FCT-027,FCT-028]. Sans dénominateur d'exposition, timing d'intervention et contrefactuel crédible, la chaîne `réseau diasporique -> persuasion -> vote` reste ouverte.

## Verdict causal

INV-036 établit que l'État turc dispose en Europe de plusieurs canaux distincts d'influence diasporique : supervision et financement religieux via Diyanet, mobilisation politique via des organisations liées à l'AKP et des campagnes transnationales, et politique ouverte de structuration/participation via YTB. Des usages au-delà du service communautaire ordinaire sont documentés case-specifically. En revanche, `diaspora = proxy`, `religion = tasking`, `financement = commandement`, `mobilisation = coercition` et `vote observé = vote causé` sont réfutés comme raccourcis. Le plafond probatoire restant porte sur l'instruction actor-specific, la prévalence et l'effet démocratique marginal.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:6|SRC_COMPLETE:15/15

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-09
- **notes:**
  - core DITIB/UID operational cases concentrated 2016-2021
  - French foreign-influence framework updated through 2024
  - YTB network/political-representation material current in 2026
  - 2023 expatriate election results used only as outcome data
- **status:** CURRENT_WITH_HISTORICAL_CASES
- **window:** 2015-2026

### MANIPULATION_REPORT
- **assumptions:**
  - official influence assessments are evidence of assessments, not automatic proof of each local tasking chain
  - diaspora participation is not interference by identity
  - vote outcomes require separate causal proof
- **clusters:**
  - NETWORK
  - POWER
  - CONFIRMATION
- **complexity:** HIGH
- **implicit:**
  - state-linked infrastructure can be open and lawful
  - the same network can contain religious, social and political functions
  - cross-border electoral participation is not clandestine by nature
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - religious-personnel supervision
  - diaspora network cultivation
  - party-linked lobbying
  - cross-border campaign
  - political representation
  - intelligence suspicion
- **priorities:**
  - state/intermediary relation
  - tasking/supervision
  - specific action
  - prevalence denominator
  - downstream effect
- **query_guidance:** Prefer official German/French findings, Turkish institutional self-descriptions and election data; retain negative controls and require actor-specific instruction for proxy attribution.
- **rhetorical:**
  - Erdogan network umbrella
  - mosque proxy umbrella
  - diaspora fifth-column umbrella
- **speaker:**
  - **goal:** forensic state-to-diaspora mechanism decomposition
  - **target:** state/party -> intermediary -> resource/instruction -> action/exposure -> effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** Turkish-state
  - **S02:** Diyanet
  - **S03:** DITIB
  - **S04:** imam
  - **S05:** consulate
  - **S06:** UID
  - **S07:** AKP
  - **S08:** YTB
  - **S09:** NGO
  - **S10:** funding
  - **S11:** tasking
  - **S12:** message
  - **S13:** mobilisation
  - **S14:** vote
  - **S15:** host-effect
- **threats:**
  - diaspora=proxy
  - religion=tasking
  - funding=command
  - association=state control
  - mobilisation=coercion
  - vote share=causal effect

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - actor-specific tasking in unresolved cases
  - **input_ids:**
    - FCT-001
    - FCT-002
    - FCT-009
    - FCT-019
    - FCT-021
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no general proxy classification from affiliation
  - **not_computable:**
    - hidden instructions absent from public record
  - **operations_applied:**
    - state-intermediary mapping
    - contact-tasking separation
    - organisation-member separation
  - **reason:** separate Diyanet/DITIB/UID/YTB relations from actor-specific tasking
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-004
    - CLM-005
    - CAU-001
    - CAU-003
    - CAU-004
  - **status:** PASS
  - **trigger:** state-diaspora organisations and intermediary chains
- **item 2:**
  - **gaps:**
    - prevalence
    - electoral causality
  - **input_ids:**
    - FCT-005
    - FCT-007
    - FCT-013
    - FCT-015
    - FCT-025
    - FCT-026
  - **module:** clusters/POWER.md
  - **negative_results:**
    - vote distribution does not identify causal network effect
  - **not_computable:**
    - individual exposure and counterfactual voting
  - **operations_applied:**
    - resource-to-action separation
    - prevalence ceiling
    - electoral-effect ceiling
  - **reason:** map resources, access, messages and adaptation without effect inflation
  - **result_ids:**
    - CLM-003
    - CLM-006
    - CLM-007
    - CLM-008
    - CAU-005
  - **status:** PASS
  - **trigger:** political mobilisation, religious supervision and electoral scale
- **item 3:**
  - **gaps:**
    - adjudicated tasking
    - effect design
  - **input_ids:**
    - FCT-003
    - FCT-006
    - FCT-010
    - FCT-017
    - FCT-020
    - FCT-027
  - **module:** clusters/CONFIRMATION.md
  - **negative_results:**
    - general DITIB espionage
    - general diaspora proxy
    - causal vote effect
  - **not_computable:**
    - undisclosed intelligence tasking
  - **operations_applied:**
    - retained negative controls
    - bounded official assessments
    - separated open policy from clandestine activity
  - **reason:** test strongest umbrella claims against organisation-level and impact controls
  - **result_ids:**
    - CLM-002
    - CLM-006
    - CLM-008
    - CTRL-001
    - CTRL-004
    - CTRL-006
    - CTRL-007
  - **status:** PASS
  - **trigger:** risk of converting state-association proximity into command

### SCOPING_REPORT
- **actors_institutions:**
  - Turkish state
  - Diyanet
  - DITIB
  - UID
  - YTB
  - AKP officials
  - Turkish consulates
  - French and German authorities
  - Turkish-origin diaspora
- **domains:**
  - religion
  - diaspora policy
  - lobbying
  - election mobilisation
  - intelligence suspicion
  - political representation
- **evidence_limits:**
  - Germany has richer actor-specific public record than France
  - French parliamentary findings often describe infrastructure/assessment rather than tasking documents
  - no exhaustive diaspora organisation denominator
  - no individual exposure-to-vote causal design
- **exclusions:**
  - diaspora identity as proxy
  - all Milli Görüs activity attributed to AKP
  - all Turkish nationalist organisations treated as state-controlled
  - vote preference treated as proof of tasking
- **geo:** France and Europe, with Germany as strongest documented comparator
- **period:** 2015-2026

### CREDO
- diaspora != proxy
- religion != tasking
- funding != command
- contact != control
- mobilisation != coercion
- participation != interference
- suspicion != adjudicated espionage
- organisation != every member
- vote share != causal effect
- state capability != use in every case

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - Diyanet supervision
  - DITIB imam channel
  - UID lobbying
  - YTB network cultivation
  - cross-border campaign
  - diaspora voting
- **priorities:**
  - specific state relation
  - instruction/supervision
  - action
  - target/exposure
  - prevalence
  - effect
- **query_guidance:** close actor-specific edges; use France/Germany differences as controls
- **speaker:**
  - **goal:** bounded influence/interference classification
  - **tone:** forensic
- **threats:**
  - guilt by association
  - religion-politics conflation
  - campaign-effect inflation
  - Germany-to-France overgeneralisation

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** Open diaspora support, religious service and political participation are not equivalent to hidden state command; individual and local autonomy remains material.
  - **support:**
    - FCT-002
    - FCT-003
    - FCT-009
    - FCT-019
    - FCT-020
  - **synthesis:** Classify each chain by supervision/tasking, transparency, action and effect rather than by Turkish identity or organisational affiliation.
  - **thesis:** Turkey has a real state-linked infrastructure for maintaining and mobilising ties with diaspora communities in Europe.
- **item 2:**
  - **antithesis:** The same electorate operates inside a broader campaign environment and no exposure/counterfactual design isolates DITIB/UID/YTB effects.
  - **support:**
    - FCT-025
    - FCT-026
    - FCT-027
    - FCT-028
  - **synthesis:** Mobilisation infrastructure and electoral outcome are both established; causal conversion from one to the other remains open.
  - **thesis:** Pro-Erdogan expatriate vote shares are compatible with effective diaspora mobilisation.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **flow:** Turkish state/Diyanet -> imam personnel and supervision -> DITIB communities
  - **resource:** salary/personnel authority and religious access
  - **support:**
    - FCT-002
    - FCT-005
- **item 2:**
  - **flow:** AKP-linked political network -> UID/campaign events -> expatriate voter mobilisation opportunity
  - **resource:** organisation, speakers and political messaging
  - **support:**
    - FCT-009
    - FCT-029
- **item 3:**
  - **flow:** YTB -> programs/convening -> European Turkish NGOs and youth/political representation
  - **resource:** state support, network access and institutional coordination
  - **support:**
    - FCT-019
    - FCT-021
    - FCT-023
- **item 4:**
  - **flow:** diaspora electorate -> Turkish presidential election -> recorded foreign-country vote totals
  - **resource:** formal external voting rights
  - **support:**
    - FCT-025
    - FCT-026

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** Turkish state/Diyanet
  - **relation:** personnel finance/supervision and religious administration
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-005
  - **to:** DITIB/imams
- **item 2:**
  - **from:** AKP/Turkish officials
  - **relation:** party-linked lobbying and cross-border campaign
  - **support:**
    - FCT-009
    - FCT-029
    - FCT-030
  - **to:** UID and expatriate voters
- **item 3:**
  - **from:** YTB/Turkish state and AKP officials
  - **relation:** diaspora policy, convening and representation agenda
  - **support:**
    - FCT-019
    - FCT-021
    - FCT-023
  - **to:** DITIB/IGMG/ATIB/UID and Turkish diaspora
- **item 4:**
  - **from:** French/German authorities
  - **relation:** oversight, restriction and policy mitigation
  - **support:**
    - FCT-003
    - FCT-014
    - FCT-016
    - FCT-017
  - **to:** foreign religious/diaspora influence channels

### IMPACT_MAP
- **case_specific_effects:**
  - political Syria-support messaging in DITIB mosques
  - cross-border referendum campaign activity
  - formal diaspora political representation programs
  - French/German policy responses to foreign religious influence
- **highest_supported_edge:** Turkish state/party institution -> identified diaspora intermediary -> supervision/funding/message/campaign or network-building action
- **not_established:**
  - general control of Turkish-origin diaspora
  - organisation-wide DITIB espionage
  - quantified prevalence of political tasking in France
  - marginal causal effect on expatriate votes
  - named host-country policy/election outcome caused by Turkish diaspora networks
- **support:**
  - FCT-007
  - FCT-009
  - FCT-013
  - FCT-019
  - FCT-029

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** espionage suspicion was individual and local governance/tasking is not comprehensively established
  - **issue:** DITIB state linkage vs proxy classification
  - **pro:** Diyanet finance/supervision and political message cases are documented
  - **resolution:** state-linked influence channel SUPPORTED; blanket proxy/espionage classification REFUTED
  - **support:**
    - FCT-002
    - FCT-003
    - FCT-005
    - FCT-006
    - FCT-007
- **item 2:**
  - **contra:** much activity is open, lawful and participation-oriented
  - **issue:** diaspora mobilisation vs interference
  - **pro:** UID, YTB and Turkish officials intentionally cultivate political participation and campaign channels
  - **resolution:** intentional cross-border influence/mobilisation SUPPORTED; interference requires additional clandestinity/coercion/rule-bypass evidence
  - **support:**
    - FCT-009
    - FCT-019
    - FCT-020
    - FCT-023
    - FCT-029
    - FCT-030
- **item 3:**
  - **contra:** OSCE campaign-wide confounding and absence of intervention-specific exposure/counterfactual design
  - **issue:** infrastructure vs electoral effect
  - **pro:** large expatriate electorate and pro-Erdogan vote distributions are observed
  - **resolution:** scale/outcome SUPPORTED; network-caused vote effect UNRESOLVED
  - **support:**
    - FCT-025
    - FCT-026
    - FCT-027
    - FCT-028

### VERIFICATION_REPORT
- **circular_families:**
  - A German federal/parliamentary findings
  - B German domestic-intelligence assessment
  - C French parliamentary inquiries/intelligence oversight
  - D Turkish state/YTB/YSK self-description and election data
  - E OSCE election observation
- **contradiction_ids:**
  - ditib-linkage-vs-general-proxy
  - open-diaspora-policy-vs-interference
  - vote-outcome-vs-causal-network-effect
- **downgraded_ids:**
  - diaspora=fifth-column
  - Diyanet funding=command every imam
  - DITIB=espionage organisation
  - UID=all Turkish associations
  - Erdogan vote share=network causality
- **none_found_claims:**
  - general tasking of French Turkish-origin associations
  - organisation-wide DITIB espionage finding
  - causal DITIB/UID/YTB effect on 2023 France diaspora vote
  - host-country election/policy outcome causally changed by Turkish diaspora network
- **remaining_gaps:**
  - actor-specific tasking documents
  - France prevalence denominator
  - exposure-to-vote causal design
- **verification:** 30 material facts resolve to 15 fresh FETCH traces across five provenance families; association, supervision, tasking, mobilisation and effect remain separated.

### EDI_REPORT
- **corpus:** 15 sources / 30 facts
- **decisive_claim_coverage:**
  - CLM-001
  - CLM-002
  - CLM-003
  - CLM-004
  - CLM-006
  - CLM-008
- **diagnostic_not_truth:** true
- **dimensions:**
  - religious supervision
  - party-linked lobbying
  - state diaspora policy
  - political mobilisation
  - electoral scale/effect
- **edi:** official host-state findings + Turkish institutional self-description + election-data and OSCE controls
- **source_counts:**
  - **A:** 6
  - **B:** 1
  - **C:** 3
  - **D:** 4
  - **E:** 1

### RESPONSIBILITY_MAP
- **boundary:** State institution, party network, religious intermediary, association/member, open mobilisation, clandestine tasking and downstream democratic effect are distinct claims.
- **not_established:**
  - all Turkish diaspora actors as state proxies
  - all DITIB imams politically tasked
  - organisation-wide DITIB espionage
  - French prevalence of tasking
  - causal diaspora-network vote conversion
- **verified:**
  - Diyanet/DITIB personnel-supervision channel
  - specific beyond-religion messaging case
  - UID central AKP lobby classification in Germany
  - YTB open diaspora-network and political-representation policy
  - cross-border Turkish campaign activity
  - diaspora electorate and vote distribution

### NEXT_QUERIES
- Reopen only on authenticated actor-specific instruction/reporting records linking a French/European association or imam to Turkish state/party tasking.
- Build a denominator of Turkish-linked French associations/imams and classify verified tasking versus ordinary religious/social activity.
- Seek precinct/person-level or natural-experiment designs around campaign restrictions, Diyanet/UID exposure or organisational membership and expatriate voting.
- Use INV-037/INV-130/INV-131 as symmetry comparators without importing Turkey findings by analogy.

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-007,QRY-008,QRY-009 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-005,QRY-006,QRY-013,QRY-015 | support:- | counter:- | results:FCT-009,FCT-010,FCT-011,FCT-012,FCT-025,FCT-026,FCT-027,FCT-028,FCT-029,FCT-030 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-010,QRY-011,QRY-012 | support:- | counter:- | results:FCT-019,FCT-020,FCT-021,FCT-022,FCT-023,FCT-024 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-006,QRY-007,QRY-008,QRY-009,QRY-013,QRY-014 | support:- | counter:- | results:FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,FCT-025,FCT-026,FCT-027,FCT-028 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-016,QRY-018,QRY-020,QRY-025,QRY-026,QRY-027,SRC-001,SRC-003,SRC-005,SRC-010,SRC-011,SRC-012 | support:FCT-001,FCT-002,FCT-005,FCT-009,FCT-019,FCT-021,FCT-023 | counter:FCT-006,FCT-010,FCT-020,FCT-024 | results:FCT-001,FCT-002,FCT-005,FCT-009,FCT-019,FCT-021,FCT-023,FCT-006,FCT-010,FCT-020,FCT-024 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-016,QRY-017,QRY-018,QRY-020,QRY-023,QRY-024,SRC-001,SRC-002,SRC-003,SRC-005,SRC-008,SRC-009 | support:FCT-002,FCT-005,FCT-015 | counter:FCT-003,FCT-006,FCT-010,FCT-016,FCT-017 | results:FCT-002,FCT-005,FCT-015,FCT-003,FCT-006,FCT-010,FCT-016,FCT-017 | final:REFUTED | gap:NONE
CLM-003 | attempts:QRY-017,QRY-018,QRY-019,SRC-002,SRC-003,SRC-004 | support:FCT-003,FCT-004,FCT-007,FCT-008 | counter:FCT-003,FCT-006 | results:FCT-003,FCT-004,FCT-007,FCT-008,FCT-003,FCT-006 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-020,QRY-021,QRY-030,SRC-005,SRC-006,SRC-015 | support:FCT-009,FCT-011,FCT-012,FCT-029,FCT-030 | counter:FCT-010 | results:FCT-009,FCT-011,FCT-012,FCT-029,FCT-030,FCT-010 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-025,QRY-026,QRY-027,SRC-010,SRC-011,SRC-012 | support:FCT-019,FCT-020,FCT-021,FCT-022,FCT-023,FCT-024 | counter:- | results:FCT-019,FCT-020,FCT-021,FCT-022,FCT-023,FCT-024 | final:SUPPORTED | gap:NONE
CLM-006 | attempts:QRY-022,QRY-023,QRY-024,SRC-007,SRC-008,SRC-009 | support:FCT-013,FCT-014,FCT-015,FCT-016,FCT-018 | counter:FCT-017 | results:FCT-013,FCT-014,FCT-015,FCT-016,FCT-018,FCT-017 | final:PARTIAL | gap:MEASUREMENT
CLM-007 | attempts:QRY-028,QRY-029,SRC-013,SRC-014 | support:FCT-025,FCT-026 | counter:FCT-027,FCT-028 | results:FCT-025,FCT-026,FCT-027,FCT-028 | final:SUPPORTED | gap:NONE
CLM-008 | attempts:QRY-020,QRY-022,QRY-024,QRY-026,QRY-027,QRY-028,QRY-029,QRY-030,SRC-005,SRC-007,SRC-009,SRC-011,SRC-012,SRC-013,SRC-014,SRC-015 | support:FCT-009,FCT-013,FCT-021,FCT-023,FCT-026 | counter:FCT-010,FCT-017,FCT-027,FCT-028,FCT-030 | results:FCT-009,FCT-013,FCT-021,FCT-023,FCT-026,FCT-010,FCT-017,FCT-027,FCT-028,FCT-030 | final:PARTIAL | gap:CAUSALITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-006 | CLM | PARTIAL | MEASUREMENT | No denominator measures what share of French Turkish-origin associations, mosques or individuals receive actor-specific political tasking or act on it.
CLM-008 | CLM | PARTIAL | CAUSALITY | No matched exposure, tasking and counterfactual design links a named DITIB/UID/YTB intervention to individual vote change or a host-country policy outcome.
CAU-002 | CAU | UNRESOLVED | RESPONSIBILITY | Actor-specific instruction, transmitted reporting and adjudicated attribution are required to upgrade from suspicion to proven intelligence tasking.
CAU-005 | CAU | UNRESOLVED | CAUSALITY | Need individual or precinct-level exposure denominator plus actor-specific intervention timing and credible counterfactual or natural experiment.

SEMANTIC_COUNTS_V1:LED:0|CLM:8|AXS:4|CAU:5|CTRL:10|ACT:4

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Turkey maintains multiple documented state-linked diaspora influence channels in Europe through Diyanet-sent religious personnel, consular/state oversight, YTB diaspora policy and party-linked lobbying networks.","claimant":"INV-036","counter":["FCT-006","FCT-010","FCT-020","FCT-024"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-005","FCT-009","FCT-019","FCT-021","FCT-023"]}
CLM-002 | {"claim":"DITIB membership, Turkish origin, mosque attendance or Diyanet financing by itself proves state tasking, espionage or political control of every local actor.","claimant":"strongest adverse hypothesis","counter":["FCT-003","FCT-006","FCT-010","FCT-016","FCT-017"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"REFUTED","support":["FCT-002","FCT-005","FCT-015"]}
CLM-003 | {"claim":"Specific Diyanet/DITIB channels have been used or suspected for functions beyond ordinary religious service, including political messaging about the Syria operation and alleged information collection by Turkey-sent imams.","claimant":"INV-036","counter":["FCT-003","FCT-006"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-003","FCT-004","FCT-007","FCT-008"]}
CLM-004 | {"claim":"UID and Turkish government campaign activity provide a documented cross-border political-mobilisation channel directed at Turkish-origin voters in Germany.","claimant":"INV-036","counter":["FCT-010"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-009","FCT-011","FCT-012","FCT-029","FCT-030"]}
CLM-005 | {"claim":"YTB openly pursues homeland ties, identity/patriotism and diaspora social-political representation and convenes major European Turkish organisations with Turkish state and AKP officials.","claimant":"INV-036","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-019","FCT-020","FCT-021","FCT-022","FCT-023","FCT-024"]}
CLM-006 | {"claim":"French parliamentary material supports a material Turkish influence infrastructure around religion and diaspora organisations, but the prevalence and downstream impact of political control across French Turkish-origin communities are not established.","claimant":"INV-036","counter":["FCT-017"],"gap":"No denominator measures what share of French Turkish-origin associations, mosques or individuals receive actor-specific political tasking or act on it.","gap_type":"MEASUREMENT","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-013","FCT-014","FCT-015","FCT-016","FCT-018"]}
CLM-007 | {"claim":"The 2023 expatriate vote distribution, including a strong Erdogan lead in France, demonstrates political participation and an observable outcome but does not identify which diaspora network, if any, caused individual votes.","claimant":"INV-036","counter":["FCT-027","FCT-028"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-025","FCT-026"]}
CLM-008 | {"claim":"Turkish state-linked diaspora organisations are demonstrated to have caused Erdogan electoral advantages abroad or a named French/German democratic-policy outcome as the marginal cause.","claimant":"strongest causal hypothesis","counter":["FCT-010","FCT-017","FCT-027","FCT-028","FCT-030"],"gap":"No matched exposure, tasking and counterfactual design links a named DITIB/UID/YTB intervention to individual vote change or a host-country policy outcome.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-009","FCT-013","FCT-021","FCT-023","FCT-026"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-007","QRY-008","QRY-009"],"axis":"state_religious_network","links":["Turkish state","German authorities","French authorities"],"question":"Quand la relation Diyanet/DITIB ferme-t-elle une chaîne de supervision, financement, message ou action sans généraliser au membre local?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018"],"sought_objects":["Diyanet","DITIB","imams","funding","supervision","espionage allegation","message"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-005","QRY-006","QRY-013","QRY-015"],"axis":"political_mobilisation","links":["AKP","UID","consulates","diaspora voters"],"question":"Quels canaux relient AKP/État turc à des organisations et à la mobilisation électorale transnationale?","result_ids":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-025","FCT-026","FCT-027","FCT-028","FCT-029","FCT-030"],"sought_objects":["UID","campaign rallies","diaspora electorate","voting"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-010","QRY-011","QRY-012"],"axis":"open_diaspora_policy","links":["YTB","AKP officials","European Turkish NGOs"],"question":"Que démontre la politique officielle YTB sur la construction de liens et de représentation sans confondre soutien ouvert et ingérence?","result_ids":["FCT-019","FCT-020","FCT-021","FCT-022","FCT-023","FCT-024"],"sought_objects":["YTB","NGO forum","homeland ties","political representation"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-006","QRY-007","QRY-008","QRY-009","QRY-013","QRY-014"],"axis":"effect_and_prevalence","links":["France","Germany","YSK","OSCE"],"question":"Quels dénominateurs et résultats permettent ou non de passer de réseau/action à effet politique ou électoral?","result_ids":["FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018","FCT-025","FCT-026","FCT-027","FCT-028"],"sought_objects":["association counts","imams","registered voters","turnout","candidate votes","OSCE controls"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"The personnel/supervision edge is directly documented by German authorities and specific beyond-religion messaging is observed.","counter":["FCT-006","FCT-017"],"limit":"Supervision, finance and a message case are supported; command of every imam/local association and population-wide effect are not.","mechanism":"Turkish state/Diyanet -> supervision and financing of Turkey-sent imams -> community religious channel -> capacity for state-linked messaging/influence","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-005","FCT-007"]}
CAU-002 | {"causal_right":"Counterintelligence concern exists; responsibility ceiling remains below organisation-wide tasking.","counter":["FCT-003"],"gap":"Actor-specific instruction, transmitted reporting and adjudicated attribution are required to upgrade from suspicion to proven intelligence tasking.","gap_type":"RESPONSIBILITY","limit":"Authorities documented a concrete espionage suspicion and response, but this corpus does not establish organisation-wide DITIB espionage or adjudicated tasking for every suspected imam.","mechanism":"Diyanet-sent imam -> information collection about opponents -> Turkish state intelligence use","status":"UNRESOLVED","support":["FCT-003","FCT-004"]}
CAU-003 | {"causal_right":"The chain closes through organised cross-border political activity and exposure opportunity, not through electoral causation.","counter":["FCT-010"],"limit":"Lobby/campaign activity is directly documented; marginal persuasion or vote conversion is not.","mechanism":"AKP/Turkish officials -> UID/consular or campaign channels -> events and mobilisation directed at expatriate voters -> political participation","status":"SUPPORTED","support":["FCT-009","FCT-011","FCT-012","FCT-029","FCT-030"]}
CAU-004 | {"causal_right":"YTB states the goals and convenes the network openly.","counter":"NONE_FOUND","limit":"Open network cultivation and participation goals are supported; hidden command, coercion and host-country policy capture are not.","mechanism":"YTB -> support/convening/representation agenda -> Turkish NGO network and diaspora political-social participation capacity","status":"SUPPORTED","support":["FCT-019","FCT-020","FCT-021","FCT-022","FCT-023","FCT-024"]}
CAU-005 | {"causal_right":"Current corpus cannot isolate a marginal democratic effect.","counter":["FCT-017","FCT-027","FCT-028"],"gap":"Need individual or precinct-level exposure denominator plus actor-specific intervention timing and credible counterfactual or natural experiment.","gap_type":"CAUSALITY","limit":"Infrastructure and electoral outcomes coexist, but exposure, persuasion and counterfactual outcome are not identified.","mechanism":"state-linked diaspora infrastructure -> exposure/mobilisation -> expatriate vote choice or host-country institutional outcome","status":"UNRESOLVED","support":["FCT-013","FCT-015","FCT-025","FCT-026"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Diaspora identity or Turkish origin is not a proxy for state tasking.","status":"PASS","support":["FCT-010","FCT-017","FCT-020"]}
CTRL-002 | {"control":"Religious service and Diyanet/DITIB affiliation are not by themselves proof of political instruction.","status":"PASS","support":["FCT-003","FCT-006"]}
CTRL-003 | {"control":"Turkish state financing of imam personnel establishes a resource/supervision edge, not command of every local message or association action.","status":"PASS","support":["FCT-005","FCT-006"]}
CTRL-004 | {"control":"A concrete espionage suspicion against individual imams did not automatically satisfy the threshold to treat DITIB as an espionage organisation.","status":"PASS","support":["FCT-003"]}
CTRL-005 | {"control":"UID AKP-lobby classification is organisation-specific and does not convert all Turkish NGOs or diaspora members into AKP agents.","status":"PASS","support":["FCT-009","FCT-010"]}
CTRL-006 | {"control":"YTB homeland-tie and representation policy is explicit/open; open diaspora policy is influence but not clandestine interference by default.","status":"PASS","support":["FCT-019","FCT-020","FCT-023","FCT-024"]}
CTRL-007 | {"control":"France 2020 impact testimony prevents infrastructure from being treated as already proven broad social effect.","status":"PASS","support":["FCT-017"]}
CTRL-008 | {"control":"Ending detached imams/foreign-paid teaching mitigates one channel but does not prove that all residual influence disappeared.","status":"PASS","support":["FCT-014","FCT-016"]}
CTRL-009 | {"control":"Expatriate vote totals and pro-Erdogan vote share are outcomes, not causal attribution to DITIB, UID or YTB.","status":"PASS","support":["FCT-025","FCT-026"]}
CTRL-010 | {"control":"OSCE-wide campaign imbalance is a confounder; diaspora vote patterns cannot be assigned to one intermediary without exposure and counterfactual evidence.","status":"PASS","support":["FCT-027","FCT-028"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Require actor-specific tasking or instruction before classifying a mosque, association or diaspora actor as a state proxy.","actor":"future investigations","intent":"diaspora != proxy","status":"DONE","support":["FCT-003","FCT-006","FCT-010"]}
ACT-002 | {"action":"Separate open diaspora policy and electoral mobilisation from clandestine/coercive interference; record both without collapsing the categories.","actor":"future investigations","intent":"influence != interference","status":"DONE","support":["FCT-019","FCT-023","FCT-029","FCT-030"]}
ACT-003 | {"action":"For prevalence, build denominators of associations/imams/organisations with proven instruction, not only counts of Turkish-linked institutions.","actor":"future investigations","intent":"case != prevalence","status":"DONE","support":["FCT-015","FCT-016","FCT-017"]}
ACT-004 | {"action":"For electoral effect, seek intervention-specific exposure, timing and counterfactual designs rather than infer from pro-Erdogan diaspora vote shares.","actor":"future investigations","intent":"mobilisation != vote causation","status":"DONE","support":["FCT-025","FCT-026","FCT-027","FCT-028"]}

SEARCH_ACTIVITY_V1:WEB:15|FETCH:15|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL:MNEMO_UNAVAILABLE | mnemo | NONE | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | PASS | - | - | Turkey influence diaspora Germany DITIB Diyanet official 2017
QRY-002 | WEB | PASS | - | - | DITIB Diyanet imams espionage suspicion Germany official 2017
QRY-003 | WEB | PASS | - | - | Turkey financial support DITIB Diyanet imams Germany official 2018
QRY-004 | WEB | PASS | - | - | DITIB mosques Turkish Syria war propaganda Germany official 2018
QRY-005 | WEB | PASS | - | - | UID central AKP lobby organisation Germany official 2021
QRY-006 | WEB | PASS | - | - | BfV Turkey influence strategy diaspora Germany 2019 UID MIT
QRY-007 | WEB | PASS | - | - | France Senate foreign influence Turkey diaspora DITIB imams 2024
QRY-008 | WEB | PASS | - | - | France parliamentary intelligence report Turkey DITIB 250 associations 120 imams 2023
QRY-009 | WEB | PASS | - | - | France Senate Turkey Diyanet Strasbourg diaspora influence 2020
QRY-010 | WEB | PASS | - | - | YTB Turkish diaspora policy strengthen homeland ties official
QRY-011 | WEB | PASS | - | - | YTB Europe umbrella Turkish NGOs DITIB UID AKP 2026
QRY-012 | WEB | PASS | - | - | Turkish Diaspora Forum political representation participation YTB 2026
QRY-013 | WEB | PASS | - | - | YSK 2023 abroad voter statistics France Erdogan official
QRY-014 | WEB | PASS | - | - | OSCE Turkey 2023 election final report abroad voters incumbent advantage
QRY-015 | WEB | PASS | - | - | Turkish politicians campaign appearances Germany 2017 referendum federal government
QRY-016 | FETCH | FOUND | SRC-001 | https://www.bundestag.de/webarchiv/presse/hib/2017_10/529360-529360 | https://www.bundestag.de/webarchiv/presse/hib/2017_10/529360-529360
QRY-017 | FETCH | FOUND | SRC-002 | https://www.bundestag.de/webarchiv/presse/hib/2017_03/501214-501214 | https://www.bundestag.de/webarchiv/presse/hib/2017_03/501214-501214
QRY-018 | FETCH | FOUND | SRC-003 | https://www.bundestag.de/webarchiv/presse/hib/2018_03/547046-547046 | https://www.bundestag.de/webarchiv/presse/hib/2018_03/547046-547046
QRY-019 | FETCH | FOUND | SRC-004 | https://www.bundestag.de/webarchiv/presse/hib/2018_04/549594-549594 | https://www.bundestag.de/webarchiv/presse/hib/2018_04/549594-549594
QRY-020 | FETCH | FOUND | SRC-005 | https://www.bundestag.de/presse/hib/829064-829064 | https://www.bundestag.de/presse/hib/829064-829064
QRY-021 | FETCH | FOUND | SRC-006 | https://www.verfassungsschutz.de/SharedDocs/publikationen/DE/verfassungsschutzberichte/2020-07-verfassungsschutzbericht-2019.pdf?__blob=publicationFile&v=11 | https://www.verfassungsschutz.de/SharedDocs/publikationen/DE/verfassungsschutzberichte/2020-07-verfassungsschutzbericht-2019.pdf?__blob=publicationFile&v=11
QRY-022 | FETCH | FOUND | SRC-007 | https://www.senat.fr/rap/r23-739-1/r23-739-18.html | https://www.senat.fr/rap/r23-739-1/r23-739-18.html
QRY-023 | FETCH | FOUND | SRC-008 | https://www.assemblee-nationale.fr/dyn/opendata/RAPPANR5L16B1454.html | https://www.assemblee-nationale.fr/dyn/opendata/RAPPANR5L16B1454.html
QRY-024 | FETCH | FOUND | SRC-009 | https://www.senat.fr/rap/r19-595-1/r19-595-12.html | https://www.senat.fr/rap/r19-595-1/r19-595-12.html
QRY-025 | FETCH | FOUND | SRC-010 | https://www.ytb.gov.tr/en/corporate/presidency-for-turks-abroad-and-related-communities | https://www.ytb.gov.tr/en/corporate/presidency-for-turks-abroad-and-related-communities
QRY-026 | FETCH | FOUND | SRC-011 | https://www.ytb.gov.tr/en/news/ytb-brings-together-umbrella-turkish-ngos-in-europe | https://www.ytb.gov.tr/en/news/ytb-brings-together-umbrella-turkish-ngos-in-europe
QRY-027 | FETCH | FOUND | SRC-012 | https://tdf.ytb.gov.tr/pages/odak-toplantilar | https://tdf.ytb.gov.tr/pages/odak-toplantilar
QRY-028 | FETCH | FOUND | SRC-013 | https://www.ysk.gov.tr/doc/dosyalar/docs/14%20May%C4%B1s%202023%20Cumhurba%C5%9Fkan%C4%B1%20ve%2025.%20D%C3%B6nem%20MV%20Genel%20Se%C3%A7imleri%20%C4%B0statistikleri.pdf | https://www.ysk.gov.tr/doc/dosyalar/docs/14%20May%C4%B1s%202023%20Cumhurba%C5%9Fkan%C4%B1%20ve%2025.%20D%C3%B6nem%20MV%20Genel%20Se%C3%A7imleri%20%C4%B0statistikleri.pdf
QRY-029 | FETCH | FOUND | SRC-014 | https://odihr.osce.org/odihr/elections/turkiye/553963 | https://odihr.osce.org/odihr/elections/turkiye/553963
QRY-030 | FETCH | FOUND | SRC-015 | https://www.bundesregierung.de/breg-en/service/archive/archive/-i-have-no-interest-in-any-escalation-says-chancellor-455904 | https://www.bundesregierung.de/breg-en/service/archive/archive/-i-have-no-interest-in-any-escalation-says-chancellor-455904

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | BT-18-13658-summary | Einfluss der Türkei auf Diaspora | 2017-10-09 | 2026-09-09T21:40:00Z | Federal government answer on post-coup Turkish influence, consulates, DITIB/Diyanet | https://www.bundestag.de/webarchiv/presse/hib/2017_10/529360-529360
SRC-002 | ◈ | fam:A | BT-18-11576-summary | Spionageverdacht gegen Imame bei Ditib | 2017-03-29 | 2026-09-09T21:40:00Z | Espionage suspicion bounded to Diyanet-sent imams and government response | https://www.bundestag.de/webarchiv/presse/hib/2017_03/501214-501214
SRC-003 | ◈ | fam:A | BT-19-988-summary | Türkei unterstützt Ditib | 2018-03-12 | 2026-09-09T21:40:00Z | Turkish financial support and Diyanet imam personnel costs | https://www.bundestag.de/webarchiv/presse/hib/2018_03/547046-547046
SRC-004 | ◈ | fam:A | BT-19-1471-summary | Kritik an türkischer Kriegspropaganda | 2018-04-05 | 2026-09-09T21:40:00Z | Government concern about Diyanet-imam support messaging in DITIB mosques | https://www.bundestag.de/webarchiv/presse/hib/2018_04/549594-549594
SRC-005 | ◈ | fam:A | BT-19-27463-summary | Lobbyorganisation der türkischen Regierungspartei AKP | 2021-03-18 | 2026-09-09T21:40:00Z | UID characterized as central AKP lobby organisation in Germany | https://www.bundestag.de/presse/hib/829064-829064
SRC-006 | ◈ | fam:B | BfV-VSB-2019 | Verfassungsschutzbericht 2019 | 2020-07-09 | 2026-09-09T21:40:00Z | Turkey influence strategy, UID, diaspora voting significance, intelligence activity | https://www.verfassungsschutz.de/SharedDocs/publikationen/DE/verfassungsschutzberichte/2020-07-verfassungsschutzbericht-2019.pdf?__blob=publicationFile&v=11
SRC-007 | ◈ | fam:C | SENAT-739-2024 | Lutte contre les influences étrangères malveillantes - Turquie/diasporas | 2024-07-23 | 2026-09-09T21:40:00Z | Turkish diaspora mobilisation and six religious-governance influence levers | https://www.senat.fr/rap/r23-739-1/r23-739-18.html
SRC-008 | ◈ | fam:C | AN-DPR-1454 | Rapport DPR 2022-2023 - influences étrangères | 2023-06-29 | 2026-09-09T21:40:00Z | DITIB/Diyanet influence in France; associations and detached imams; ELCO/EILE control | https://www.assemblee-nationale.fr/dyn/opendata/RAPPANR5L16B1454.html
SRC-009 | ◈ | fam:C | SENAT-595-2020 | Radicalisation islamiste : faire face et lutter ensemble | 2020-07-07 | 2026-09-09T21:40:00Z | Turkey/Diyanet influence assessment and France impact control | https://www.senat.fr/rap/r19-595-1/r19-595-12.html
SRC-010 | ◈ | fam:D | YTB-INSTITUTION | YTB Institution and diaspora policy | 2026-09-09 | 2026-09-09T21:40:00Z | Mission, homeland ties, identity/culture/patriotism and diaspora policy | https://www.ytb.gov.tr/en/corporate/presidency-for-turks-abroad-and-related-communities
SRC-011 | ◈ | fam:D | YTB-NGO-EUROPE-2026 | YTB brings together umbrella Turkish NGOs in Europe | 2026-03-01 | 2026-09-09T21:40:00Z | YTB meeting with DITIB/IGMG/ATIB/UID and AKP/presidency/diplomatic officials | https://www.ytb.gov.tr/en/news/ytb-brings-together-umbrella-turkish-ngos-in-europe
SRC-012 | ◈ | fam:D | YTB-TDF-2026 | Türk Diaspora Forumu 2026 - focus meetings | 2026-09-09 | 2026-09-09T21:40:00Z | Political participation, civil-society institutionalisation and host-country representation agenda | https://tdf.ytb.gov.tr/pages/odak-toplantilar
SRC-013 | ◈ | fam:D | YSK-2023-STAT | YSK 14 May 2023 election statistics | 2023-06-01 | 2026-09-09T21:40:00Z | Registered voters abroad, turnout, candidate votes by country including France | https://www.ysk.gov.tr/doc/dosyalar/docs/14%20May%C4%B1s%202023%20Cumhurba%C5%9Fkan%C4%B1%20ve%2025.%20D%C3%B6nem%20MV%20Genel%20Se%C3%A7imleri%20%C4%B0statistikleri.pdf
SRC-014 | ◈ | fam:E | OSCE-ODIHR-TUR-2023 | Türkiye 2023 general elections ODIHR final report | 2023-09-29 | 2026-09-09T21:40:00Z | Election context, incumbent advantage, participation and freedoms | https://odihr.osce.org/odihr/elections/turkiye/553963
SRC-015 | ◈ | fam:A | BREG-2017-TUR-CAMPAIGN | German Chancellor on end of Turkish campaign appearances | 2017-03-22 | 2026-09-09T21:40:00Z | Turkish government politicians campaign appearances in Germany and decision to end them | https://www.bundesregierung.de/breg-en/service/archive/archive/-i-have-no-interest-in-any-escalation-says-chancellor-455904

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.bundestag.de/webarchiv/presse/hib/2017_10/529360-529360 | A | 2026-09-09 | Post-coup influence intensification | The German federal government reported an intensification after the July 2016 coup attempt of Turkish state efforts to influence the Turkish diaspora in Germany, including activity by consular representatives. | -
FCT-002 | FACT | ✧ | https://www.bundestag.de/webarchiv/presse/hib/2017_10/529360-529360 | A | 2026-09-09 | Diyanet-DITIB supervision channel | The same federal answer described DITIB as structurally and personally linked to Diyanet and stated that Turkish embassy/consulates exercise service supervision over Turkey-sent Diyanet imams working mainly in DITIB communities, creating multiple influence opportunities. | -
FCT-003 | FACT | ✧ | https://www.bundestag.de/webarchiv/presse/hib/2017_03/501214-501214 | A | 2026-09-09 | Imam espionage attribution ceiling | In March 2017 the German government said the espionage suspicion concerned Diyanet-sent imams working in DITIB communities; the legal threshold for intelligence-service surveillance of DITIB as an organisation had not been met on that basis. | -
FCT-004 | FACT | ✧ | https://www.bundestag.de/webarchiv/presse/hib/2017_03/501214-501214 | A | 2026-09-09 | Political instrumentalisation warning | German authorities raised the espionage issue with the Turkish foreign ministry and told DITIB that political influence or instrumentalisation of DITIB by Turkey was unacceptable, showing a state-to-organisation concern without proving organisation-wide espionage. | -
FCT-005 | FACT | ✧ | https://www.bundestag.de/webarchiv/presse/hib/2018_03/547046-547046 | A | 2026-09-09 | DITIB Turkish personnel financing | The German government reported that Turkey financially supported DITIB mainly through personnel costs for Diyanet religious officers/imams deployed in DITIB communities. | -
FCT-006 | FACT | ✧ | https://www.bundestag.de/webarchiv/presse/hib/2018_03/547046-547046 | A | 2026-09-09 | DITIB governance knowledge ceiling | The German answer noted DITIB supervision of affiliated associations but did not claim complete knowledge of how every regional association was governed; financial/personnel linkage therefore does not prove command over every local action. | -
FCT-007 | FACT | ✧ | https://www.bundestag.de/webarchiv/presse/hib/2018_04/549594-549594 | A | 2026-09-09 | Syria-support messaging in mosques | The German government reported information that Diyanet imams in DITIB mosques promoted support for Turkey's military operation in Syria. | -
FCT-008 | FACT | ✧ | https://www.bundestag.de/webarchiv/presse/hib/2018_04/549594-549594 | A | 2026-09-09 | Religious-service boundary | The government criticized such involvement beyond religious services as contributing to carrying Turkish political conflict into German society; this closes a message-channel case, not a quantified population effect. | -
FCT-009 | FACT | ✧ | https://www.bundestag.de/presse/hib/829064-829064 | A | 2026-09-09 | UID AKP lobby classification | In 2021 the German federal government described the Union of International Democrats as the central lobby organisation of Turkey's governing AKP in Germany, with 15 regional associations in western Germany and Berlin. | -
FCT-010 | FACT | ✧ | https://www.bundestag.de/presse/hib/829064-829064 | A | 2026-09-09 | UID dominance control | The same answer reported no official German federal-government contacts with UID in the preceding five years and no evidence at that time of determining domination of the UID board by Turkish far-right currents; AKP-lobby status does not make every member a state proxy. | -
FCT-011 | FACT | ✧ | https://www.verfassungsschutz.de/SharedDocs/publikationen/DE/verfassungsschutzberichte/2020-07-verfassungsschutzbericht-2019.pdf?__blob=publicationFile&v=11 | B | 2026-09-09 | BfV diaspora influence strategy | The 2019 German domestic-intelligence report described UID as the largest Turkish state/government-near interest group and placed it within an active influence strategy directed at the Turkish-origin community in Germany. | -
FCT-012 | FACT | ✧ | https://www.verfassungsschutz.de/SharedDocs/publikationen/DE/verfassungsschutzberichte/2020-07-verfassungsschutzbericht-2019.pdf?__blob=publicationFile&v=11 | B | 2026-09-09 | BfV scale and intelligence context | The report noted about 1.4 million Turkish citizens in Germany were eligible for the 2018 Turkish elections and about 600,000 participated, while also reporting recurring attempts to instrumentalise the diaspora and sustained Turkish intelligence activity; these facts establish scale/capability, not marginal electoral causation. | -
FCT-013 | FACT | ✧ | https://www.senat.fr/rap/r23-739-1/r23-739-18.html | C | 2026-09-09 | France diaspora mobilisation assessment | The French Senate 2024 foreign-influence report states that Turkish-linked structures are capable of mobilising the Turkish diaspora in support of the Erdogan government, especially in electoral periods. | -
FCT-014 | FACT | ✧ | https://www.senat.fr/rap/r23-739-1/r23-739-18.html | C | 2026-09-09 | France religious influence levers | The Senate identifies six influence levers through Muslim religious organisation, including mosques, federations, representative governance, halal, imam training and imam designation, and notes that ending detached imams does not by itself eliminate foreign influence over training/designation. | -
FCT-015 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/opendata/RAPPANR5L16B1454.html | C | 2026-09-09 | France DITIB-Diyanet linkage | The French parliamentary intelligence report describes DITIB in France as an emanation of Turkey's Diyanet and a vector through which Turkey has weighed on the organisation of Islam in France. | -
FCT-016 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/opendata/RAPPANR5L16B1454.html | C | 2026-09-09 | France DITIB scale and policy control | That report cites roughly 250 associations and about 120 Turkish or Turkish-origin detached imams in the DITIB sphere and records France's move away from foreign-appointed/paid ELCO teaching and detached imams; scale and policy response do not prove tasking of each association or imam. | -
FCT-017 | FACT | ✧ | https://www.senat.fr/rap/r19-595-1/r19-595-12.html | C | 2026-09-09 | France impact negative control | A 2020 French Senate inquiry recorded testimony that Turkish Islam had not, at that time, produced an impact in France comparable to other Islamist currents, providing a direct control against treating infrastructure as demonstrated broad effect. | -
FCT-018 | FACT | ✧ | https://www.senat.fr/rap/r19-595-1/r19-595-12.html | C | 2026-09-09 | Strasbourg influence assessment boundary | The same inquiry recorded official assessments of a Turkish state influence strategy in Alsace/Strasbourg involving DITIB and related religious/educational projects; these institutional assessments are evidence of an influence concern, not themselves a tasking document for each local entity. | -
FCT-019 | FACT | ✧ | https://www.ytb.gov.tr/en/corporate/presidency-for-turks-abroad-and-related-communities | D | 2026-09-09 | YTB explicit homeland-ties policy | Turkey's Presidency for Turks Abroad and Related Communities states that strengthening diaspora ties with the homeland, protecting identity/culture and strengthening patriotism and the diaspora's social, economic, cultural and legal position are core policy objectives. | -
FCT-020 | FACT | ✧ | https://www.ytb.gov.tr/en/corporate/presidency-for-turks-abroad-and-related-communities | D | 2026-09-09 | Open diaspora policy control | YTB presents this as an open, multidimensional diaspora policy and also frames democratic participation in countries of residence as an objective; open state support and participation policy are influence channels but not clandestine interference by default. | -
FCT-021 | FACT | ✧ | https://www.ytb.gov.tr/en/news/ytb-brings-together-umbrella-turkish-ngos-in-europe | D | 2026-09-09 | YTB umbrella-NGO coordination forum | In March 2026 YTB convened leaders of DITIB, IGMG, ATIB, UID, MÜSIAD and other European Turkish organisations together with an AKP deputy chair, a presidential chief adviser and Turkey's ambassador to Berlin. | -
FCT-022 | FACT | ✧ | https://www.ytb.gov.tr/en/news/ytb-brings-together-umbrella-turkish-ngos-in-europe | D | 2026-09-09 | YTB meeting tasking ceiling | YTB described the meeting agenda as community issues, youth/education and stronger inter-institutional cooperation; the meeting proves high-level network contact/coordination capacity but does not itself prove operational tasking for a political action. | -
FCT-023 | FACT | ✧ | https://tdf.ytb.gov.tr/pages/odak-toplantilar | D | 2026-09-09 | YTB political representation agenda | The 2026 Turkish Diaspora Forum includes a focus track on social and political representation covering the diaspora's political participation process, civil-society institutionalisation, youth participation and representation in host-country politics. | -
FCT-024 | FACT | ✧ | https://tdf.ytb.gov.tr/pages/odak-toplantilar | D | 2026-09-09 | Representation versus interference control | An explicit state policy to support diaspora political/social representation establishes intentional influence capacity and network cultivation; it remains distinct from coercion, hidden command or unlawful interference unless additional edges are proven. | -
FCT-025 | FACT | ✧ | https://www.ysk.gov.tr/doc/dosyalar/docs/14%20May%C4%B1s%202023%20Cumhurba%C5%9Fkan%C4%B1%20ve%2025.%20D%C3%B6nem%20MV%20Genel%20Se%C3%A7imleri%20%C4%B0statistikleri.pdf | D | 2026-09-09 | YSK expatriate electorate scale | YSK reported 3,423,759 registered voters abroad for the first round of the 14 May 2023 presidential election, with 1,691,287 voting at foreign polling places and 49.40% turnout in that table. | -
FCT-026 | FACT | ✧ | https://www.ysk.gov.tr/doc/dosyalar/docs/14%20May%C4%B1s%202023%20Cumhurba%C5%9Fkan%C4%B1%20ve%2025.%20D%C3%B6nem%20MV%20Genel%20Se%C3%A7imleri%20%C4%B0statistikleri.pdf | D | 2026-09-09 | YSK France vote distribution | YSK country results recorded 126,572 votes for Recep Tayyip Erdogan and 65,733 for Kemal Kilicdaroglu in France; the observed vote distribution is an outcome, not evidence that DITIB, UID, YTB or another network caused those votes. | -
FCT-027 | FACT | ✧ | https://odihr.osce.org/odihr/elections/turkiye/553963 | E | 2026-09-09 | OSCE election-context confounding | ODIHR concluded that the 2023 Turkish elections were competitive but that the incumbent president and ruling parties enjoyed an unjustified advantage, including media bias and restrictions on freedoms; diaspora vote patterns therefore sit within a broader non-random campaign environment. | -
FCT-028 | FACT | ✧ | https://odihr.osce.org/odihr/elections/turkiye/553963 | E | 2026-09-09 | OSCE causal-effect ceiling | ODIHR documents election conditions and participation but does not provide a causal design isolating the marginal effect of diaspora organisations or state-linked religious networks on expatriate voting behaviour. | -
FCT-029 | FACT | ✧ | https://www.bundesregierung.de/breg-en/service/archive/archive/-i-have-no-interest-in-any-escalation-says-chancellor-455904 | A | 2026-09-09 | Turkish campaign appearances in Germany | In March 2017 the German chancellor publicly noted the decision that Turkish government politicians would no longer appear at campaign rallies in Germany, confirming that Turkish domestic referendum campaigning had extended into Germany. | -
FCT-030 | FACT | ✧ | https://www.bundesregierung.de/breg-en/service/archive/archive/-i-have-no-interest-in-any-escalation-says-chancellor-455904 | A | 2026-09-09 | Cross-border campaign classification | Campaign appearances by foreign office-holders directed at expatriate voters are direct cross-border political mobilisation, but when openly conducted and subject to host-country law they are not by themselves evidence of clandestine tasking or coercive interference. | -
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
FCT-028 | SRC-014
FCT-029 | SRC-015
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

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:search
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:facts
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:causal
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:verify
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:accountability
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:finalize

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-09T21:40:47.410211+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-029","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-030","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":30,"eligible":30,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:30;attempted:0;success:0;failure:0;blocked:30} | WRITEBACK_EXECUTION_V1:[30 rows, see section]

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
