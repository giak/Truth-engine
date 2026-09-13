ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260908-1535-spyware-political-compromise | PARENT_RUN_ID:NONE | AS_OF:2026-09-08
INPUT_KIND:RUN_CARD | MISSION_MODE:DEEPEN | INPUT_REF:PATH:/mnt/data/inv141/runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-08_spyware-political-compromise/2026-09-08_15-35_spyware-political-compromise_INPUT.md | SUBJECT_SLUG:spyware-political-compromise | SUBJECT_FP:sha256:00854edc9e4bc5325307b8ee7b0d33acb8be787771fcb5d1f21dec8ba9b2adc4 | INPUT_SHA256:sha256:fa2190d98440b5d5f5801c44b263118d74ada098e1826117f57cf8bbbd0802a9
COMPLEXITY:11→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/Europe 2015-2026; Pegasus/Predator and equivalent spyware only when target, technical compromise, client/operator attribution and downstream use/effect can be separated; distinguish access from coercion/influence and electoral effect.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[RECOVERY_REPLAY_AFTER_UNPERSISTED_RUNTIME_BYTES] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/ICEBERG.md,clusters/FRAMING.md,clusters/POWER.md,clusters/NETWORK.md,clusters/TEMPORAL.md,clusters/RESISTANCE.md | degraded:MNEMO_UNAVAILABLE,LOCAL_CORPUS_PATH_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-141 — Spyware, surveillance et compromission comme levier d’influence

## Objet

L’enquête distingue strictement **ciblage → infection → accès/exfiltration → attribution client/opérateur → usage aval → changement de comportement/décision → effet politique ou électoral**. Une infection n’est ni une attribution, ni un chantage, ni une preuve d’effet électoral.

## 1. France / Maroc : compromission établie, usage politique aval non fermé

Le dossier français établit des compromissions réelles de responsables et journalistes. Le suivi parlementaire français s’est saisi de Pegasus dès 2021 ; les éléments techniques et journalistiques disponibles en 2026 renforcent fortement l’attribution du client visant des responsables français au Maroc. Le cas de Sébastien Lecornu est techniquement confirmé par l’ANSSI dans le dossier rapporté en 2026. Mais l’enquête judiciaire française reste ouverte et le corpus ne ferme pas, pour les cibles françaises, une chaîne générale `données obtenues -> chantage -> décision politique`.

## 2. Pologne / Brejza : la chaîne d’influence la plus complète

La Pologne fournit le cas discriminant le plus fort. L’achat de Pegasus par le CBA via un financement de 25 millions de PLN provenant du Justice Fund est documenté. Krzysztof Brejza, alors chef de campagne de l’opposition, a subi 33 attaques ; Citizen Lab a témoigné d’une exfiltration substantielle de données, y compris à des moments politiquement sensibles. Le rapport du Sénat polonais conclut que des matériaux volés depuis son téléphone ont ensuite été manipulés et utilisés dans des contenus TVP/TVP Info.

Ce cas ferme **case-specifically** `compromission -> données -> réutilisation/manipulation -> diffusion politique`. Il ne ferme pas `diffusion -> changement du résultat électoral`.

## 3. Grèce / Koukakis : effet comportemental, attribution institutionnelle à séparer

Thanasis Koukakis a été infecté par Predator et a également fait l’objet d’une écoute par l’EYP. Ces deux objets ne doivent pas être fusionnés sans preuve de tasking commun. Koukakis a décrit un effet concret sur son travail : sécurité accrue des communications et rencontres physiques avec les sources. Les condamnations grecques de 2026 établissent des infractions liées à l’écosystème privé Intellexa/Krikel ; elles ne suffisent pas à attribuer chaque infection à l’État grec, et l’appel doit être conservé dans le statut judiciaire.

## 4. Espagne / CatalanGate : vaste compromission, attribution et légalité hétérogènes

Citizen Lab a identifié au moins 65 personnes ciblées ou infectées, dont au moins 51 infections Pegasus forensiquement confirmées. Le laboratoire ne conclut pas à une attribution institutionnelle certaine pour l’ensemble du corpus, malgré un fort faisceau vers les autorités espagnoles. En parallèle, le CNI a reconnu 18 interceptions Pegasus autorisées judiciairement ; le Défenseur du peuple a considéré ces autorisations comme constitutionnelles et motivées, tout en demandant un meilleur contrôle.

Le contrôle est décisif : **surveillance autorisée != influence illégitime**. Il faut qualifier chaque chaîne séparément.

## 5. Verdict

Le mécanisme `spyware -> influence` existe, mais **pas par la seule compromission**. Le niveau le mieux vérifié est :

- accès clandestin et exfiltration : vérifiés dans plusieurs cas ;
- réutilisation politique de données : vérifiée case-specifically en Pologne ;
- changement de comportement : vérifié case-specifically chez Koukakis ;
- chantage, modification d’une décision publique ou changement d’un résultat électoral : non établis de manière générale dans le corpus.

## Contrôles

- targeting/list != infection ;
- infection != client attribution ;
- vendor/infrastructure != commanditaire ;
- data access != blackmail ;
- state wiretap overlap != spyware state tasking ;
- authorized surveillance != illegitimate influence ;
- public smear / behavior change != electoral outcome.

## Gaps terminaux

Réouvrir seulement sur : (1) tasking/client authentifié fermant une chaîne France ou Grèce ; (2) preuve de chantage ou de décision modifiée ; (3) design causal reliant l’usage de données espionnées à un résultat électoral/politique.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:6|EDI_DECISIVE:5|SRC_COMPLETE:15/15

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-08
- **freshness:** 2026 updates included for France and Greece
- **period:** 2015-2026

### MANIPULATION_REPORT
- **assumptions:**
  - technical infection evidence is separable from client attribution
  - judicial authorization is a distinct legal dimension
- **clusters:**
  - ICEBERG
  - FRAMING
  - POWER
  - NETWORK
  - TEMPORAL
  - RESISTANCE
- **complexity:** APEX
- **implicit:**
  - downstream effect requires separate proof
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - compromise chain
  - reuse chain
  - effect ladder
  - authorization control
- **priorities:**
  - technical compromise
  - client/operator
  - data access
  - downstream use
  - behavior
  - political/electoral effect
- **query_guidance:** prefer official/parliamentary, forensic labs, court reporting; retain negative attribution/effect controls
- **rhetorical:** forensic bounded attribution
- **speaker:**
  - **goal:** distinguish clandestine access from influence/coercion and effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** spyware capability
  - **S02:** target selection
  - **S03:** infection
  - **S04:** data exfiltration
  - **S05:** client attribution
  - **S06:** operator attribution
  - **S07:** downstream reuse
  - **S08:** media laundering
  - **S09:** behavioral chilling
  - **S10:** coercion
  - **S11:** political advantage
  - **S12:** electoral effect
  - **S13:** legal authorization
  - **S14:** judicial review
  - **S15:** attribution uncertainty
- **threats:**
  - infection=attribution
  - surveillance=influence
  - media use=electoral outcome
  - vendor=client

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - causal electoral outcome
  - **input_ids:**
    - LED-001
  - **module:** clusters/ICEBERG.md
  - **negative_results:**
    - no generalized blackmail/electoral effect
  - **not_computable:**
    - classified tasking where unavailable
  - **operations_applied:**
    - bounded mechanism mapping
  - **reason:** relevant to clandestine access, framing, power, networks, time or resistance effects
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-003
    - CLM-005
    - CLM-007
  - **status:** DONE
  - **trigger:** symbol routing
- **item 2:**
  - **gaps:**
    - causal electoral outcome
  - **input_ids:**
    - LED-001
  - **module:** clusters/FRAMING.md
  - **negative_results:**
    - no generalized blackmail/electoral effect
  - **not_computable:**
    - classified tasking where unavailable
  - **operations_applied:**
    - bounded mechanism mapping
  - **reason:** relevant to clandestine access, framing, power, networks, time or resistance effects
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-003
    - CLM-005
    - CLM-007
  - **status:** DONE
  - **trigger:** symbol routing
- **item 3:**
  - **gaps:**
    - causal electoral outcome
  - **input_ids:**
    - LED-001
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no generalized blackmail/electoral effect
  - **not_computable:**
    - classified tasking where unavailable
  - **operations_applied:**
    - bounded mechanism mapping
  - **reason:** relevant to clandestine access, framing, power, networks, time or resistance effects
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-003
    - CLM-005
    - CLM-007
  - **status:** DONE
  - **trigger:** symbol routing
- **item 4:**
  - **gaps:**
    - causal electoral outcome
  - **input_ids:**
    - LED-001
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no generalized blackmail/electoral effect
  - **not_computable:**
    - classified tasking where unavailable
  - **operations_applied:**
    - bounded mechanism mapping
  - **reason:** relevant to clandestine access, framing, power, networks, time or resistance effects
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-003
    - CLM-005
    - CLM-007
  - **status:** DONE
  - **trigger:** symbol routing
- **item 5:**
  - **gaps:**
    - causal electoral outcome
  - **input_ids:**
    - LED-001
  - **module:** clusters/TEMPORAL.md
  - **negative_results:**
    - no generalized blackmail/electoral effect
  - **not_computable:**
    - classified tasking where unavailable
  - **operations_applied:**
    - bounded mechanism mapping
  - **reason:** relevant to clandestine access, framing, power, networks, time or resistance effects
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-003
    - CLM-005
    - CLM-007
  - **status:** DONE
  - **trigger:** symbol routing
- **item 6:**
  - **gaps:**
    - causal electoral outcome
  - **input_ids:**
    - LED-001
  - **module:** clusters/RESISTANCE.md
  - **negative_results:**
    - no generalized blackmail/electoral effect
  - **not_computable:**
    - classified tasking where unavailable
  - **operations_applied:**
    - bounded mechanism mapping
  - **reason:** relevant to clandestine access, framing, power, networks, time or resistance effects
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-003
    - CLM-005
    - CLM-007
  - **status:** DONE
  - **trigger:** symbol routing

### SCOPING_REPORT
- **actors_institutions:**
  - French authorities
  - Moroccan intelligence attribution leads
  - Polish CBA
  - TVP
  - Greek EYP
  - Intellexa/Krikel
  - Spanish CNI
- **domains:**
  - Pegasus
  - Predator
  - political surveillance
  - journalistic chilling
  - electoral information advantage
- **evidence_limits:**
  - classified tasking
  - open French judicial inquiry
  - appeals in Greek case
  - limited causal outcome designs
- **exclusions:**
  - mere target list as infection
  - vendor presence as client attribution
  - surveillance as automatic electoral effect
- **geo:** France/Europe
- **object_coverage:** France/Morocco, Poland, Greece and Spain cover compromise, attribution, downstream use, behavior, legal control and effect ceiling.
- **object_question:** When does digital compromise of officials, journalists or opponents remain clandestine access, and when can blackmail, intimidation, behavior change, decision or political advantage be documented?
- **period:** 2015-2026

### CREDO
- **lead_question:** When is compromise converted into an influence mechanism?
- **object_question:** Spyware access versus downstream influence/effect
- **search_principle:** mechanism-first; separate every edge; test authorization and attribution controls

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - target->infection->data->use->effect
  - attribution ladder
  - legal authorization control
- **priorities:**
  - Poland downstream use
  - Greece behavioral effect
  - France attribution
  - Spain authorization control
- **query_guidance:** direct objects first; case-specific effect ceiling
- **speaker:**
  - **goal:** bounded causal attribution
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **threats:**
  - guilt by vendor
  - effect inflation

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** Infection establishes access; influence requires downstream use or behavior/effect.
  - **resolution:** Poland and Koukakis close specific downstream edges; other cases remain access/attribution only.
  - **thesis:** Spyware infection is itself political influence.
- **item 2:**
  - **antithesis:** Greek EYP wiretap and Predator infection are distinct evidentiary objects.
  - **resolution:** Do not merge chains absent tasking proof.
  - **thesis:** A state-related surveillance overlap proves state tasking of commercial spyware.
- **item 3:**
  - **antithesis:** Spain includes judicially authorized CNI surveillance; Poland documents media reuse but not changed outcome.
  - **resolution:** Classify legality, downstream use and electoral effect separately.
  - **thesis:** Political targeting proves election manipulation.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **from:** Justice Fund
  - **resource:** 25m PLN for Pegasus acquisition
  - **support:**
    - FCT-009
    - FCT-010
  - **to:** CBA

### ACTOR_NETWORK_MAP
- **item 1:**
  - **edge:** compromise/data exfiltration
  - **from:** Polish Pegasus/CBA chain
  - **support:**
    - FCT-011
    - FCT-013
    - FCT-014
  - **to:** Krzysztof Brejza
- **item 2:**
  - **edge:** manipulated public reuse per Senate finding
  - **from:** phone-derived material
  - **support:**
    - FCT-012
  - **to:** TVP/TVP Info
- **item 3:**
  - **edge:** infection; operator/state tasking not fully resolved
  - **from:** Predator operator
  - **support:**
    - FCT-019
    - FCT-023
  - **to:** Thanasis Koukakis
- **item 4:**
  - **edge:** judicially authorized Pegasus interception
  - **from:** Spanish CNI
  - **support:**
    - FCT-027
    - FCT-028
  - **to:** 18 Catalan targets

### IMPACT_MAP
- **effect_limit:** Case-specific downstream influence/behavior edges exist; generalized democratic outcome causality remains open.
- **not_established:**
  - general blackmail
  - general policy change
  - changed election result
- **verified:**
  - Brejza data exfiltration and media reuse
  - Koukakis changed communication/source practices

### CONTRADICTION_LEDGER
- **item 1:**
  - **ids:**
    - FCT-025
    - FCT-026
    - FCT-027
    - FCT-028
  - **resolution:** Separate 18 admitted authorized CNI cases from the broader technically observed set.
  - **status:** RESOLVED
  - **tension:** CatalanGate extensive targeting vs attribution certainty
- **item 2:**
  - **ids:**
    - FCT-019
    - FCT-021
    - FCT-022
    - FCT-023
  - **resolution:** Private ecosystem criminal responsibility is documented; state tasking remains separately bounded.
  - **status:** RESOLVED
  - **tension:** Greek Predator infection vs state tasking

### VERIFICATION_REPORT
- **circular_families:**
  - Polish Senate hearing/final report share parliamentary provenance; Le Monde 2026 articles share newsroom/consortium provenance; Citizen Lab correction is not independent corroboration of CatalanGate.
- **downgraded_ids:**
  - NONE
- **none_found_claims:**
  - general blackmail chain
  - general policy decision change
  - changed election outcome across reviewed cases
- **remaining_gaps:**
  - authenticated client/tasking for every French target
  - Greek state tasking for Predator cases
  - causal electoral outcome design
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
  - **coverage:** multi-case France/Poland/Greece/Spain
  - **independence:** mixed; shared provenance explicitly bounded
  - **limits:**
    - classified tasking
    - ongoing/appealed proceedings
    - no election-outcome experiment
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 2
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES
    - **gap_type:** CAUSALITY
    - **independent_families:** 1
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** YES
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 1
  - **item 4:**
    - **claim_id:** CLM-005
    - **direct_object:** YES
    - **gap_type:** ATTRIBUTION
    - **independent_families:** 2
  - **item 5:**
    - **claim_id:** CLM-007
    - **direct_object:** CASE_SPECIFIC
    - **gap_type:** CAUSALITY
    - **independent_families:** 3
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** multi-institution
  - **perspective:** official+parliamentary+technical+rights+press
  - **stratification:** target->infection->data->use->behavior/political effect
  - **temporal:** 2015-2026
- **edi:**
  - **assessment:** STRONG_FOR_TECHNICAL_COMPROMISE_AND_CASE_SPECIFIC_DOWNSTREAM_USE; MODERATE_FOR_CLIENT_ATTRIBUTION; WEAK_FOR_GENERAL_OUTCOME_CAUSALITY
  - **flags:**
    - FORENSIC_LAB
    - PARLIAMENTARY_RECORD
    - JUDICIAL_STATUS
    - AUTHORIZATION_CONTROL
    - CAUSAL_GAP
- **source_counts:**
  - **primary_or_direct:** 10
  - **provenance_families:** 10
  - **secondary:** 5
  - **total:** 15

### RESPONSIBILITY_MAP
- **item 1:**
  - **actor:** Polish procurement/operational institutions
  - **documented_action:** Pegasus acquisition and use documented in government/Senate records
  - **intent:** SURVEILLANCE
  - **scope:** case-specific; criminal responsibility separate
  - **support:**
    - FCT-009
    - FCT-010
    - FCT-011
    - FCT-013
- **item 2:**
  - **actor:** TVP/TVP Info
  - **documented_action:** public use of manipulated material derived from Brejza phone according to Senate finding
  - **intent:** PUBLICATION
  - **scope:** downstream media use; election-result effect unproven
  - **support:**
    - FCT-012
- **item 3:**
  - **actor:** Intellexa/Krikel-linked defendants
  - **documented_action:** unlawful access/privacy offenses in Predator case
  - **intent:** UNLAWFUL_ACCESS
  - **scope:** Greek court judgment, appeal context
  - **support:**
    - FCT-021
    - FCT-023
- **item 4:**
  - **actor:** Spanish CNI
  - **documented_action:** 18 admitted Pegasus interceptions with judicial authorization
  - **intent:** INTELLIGENCE_SURVEILLANCE
  - **scope:** authorized subset only
  - **support:**
    - FCT-027
    - FCT-028

### NEXT_QUERIES
- Reopen France only on authenticated tasking/client-use records or judicial findings closing downstream use.
- Reopen Greece state-attribution edge only on judicial/documentary tasking evidence.
- Reopen electoral-effect edge only on causal designs linking spyware-derived information to vote/result or policy decision.

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001 | support:- | counter:- | results:FCT-001 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-003,QRY-013,QRY-025 | support:- | counter:- | results:FCT-003,FCT-013,FCT-025 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-005,QRY-025 | support:- | counter:- | results:FCT-005,FCT-026 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-013 | support:- | counter:- | results:FCT-014 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-011,QRY-013 | support:- | counter:- | results:FCT-012,FCT-014 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-019 | support:- | counter:- | results:FCT-020 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-011,QRY-017,QRY-027 | support:- | counter:- | results:FCT-012,FCT-018,FCT-028 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-004,QRY-006,QRY-008,SRC-002,SRC-003,SRC-004 | support:FCT-003,FCT-005,FCT-006 | counter:FCT-007,FCT-008 | results:FCT-003,FCT-005,FCT-006,FCT-007,FCT-008 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-002 | attempts:QRY-012,QRY-014,SRC-006,SRC-007 | support:FCT-011,FCT-012,FCT-013,FCT-014 | counter:- | results:FCT-011,FCT-012,FCT-013,FCT-014 | final:SUPPORTED | gap:CAUSALITY
CLM-003 | attempts:QRY-020,QRY-022,SRC-010,SRC-011 | support:FCT-019,FCT-020 | counter:FCT-022 | results:FCT-019,FCT-020,FCT-022 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-004 | attempts:QRY-022,QRY-024,SRC-011,SRC-012 | support:FCT-021,FCT-023 | counter:FCT-022 | results:FCT-021,FCT-023,FCT-022 | final:PARTIAL | gap:RESPONSIBILITY
CLM-005 | attempts:QRY-026,QRY-028,SRC-013,SRC-014 | support:FCT-025,FCT-026 | counter:FCT-027,FCT-028 | results:FCT-025,FCT-026,FCT-027,FCT-028 | final:PARTIAL | gap:ATTRIBUTION
CLM-006 | attempts:QRY-028,SRC-014 | support:FCT-027,FCT-028 | counter:- | results:FCT-027,FCT-028 | final:SUPPORTED | gap:NONE
CLM-007 | attempts:QRY-012,QRY-020,QRY-028,SRC-006,SRC-010,SRC-014 | support:FCT-012,FCT-020,FCT-028 | counter:- | results:FCT-012,FCT-020,FCT-028 | final:SUPPORTED | gap:CAUSALITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-001 | CLM | SUPPORTED | RESPONSIBILITY | Judicial investigation remains open and not every compromised French target has a complete command/use chain.
CLM-002 | CLM | SUPPORTED | CAUSALITY | Changed election outcome is not causally established.
CLM-003 | CLM | SUPPORTED | RESPONSIBILITY | Predator infection and EYP wiretap do not by themselves prove one state tasking chain.
CLM-004 | CLM | PARTIAL | RESPONSIBILITY | Convictions do not establish state tasking for every infection and are subject to appeal.
CLM-005 | CLM | PARTIAL | ATTRIBUTION | Only 18 admitted CNI interceptions had reviewed judicial authorizations; the remainder require separate attribution.
CLM-007 | CLM | SUPPORTED | CAUSALITY | No general causal design links spyware exposure to policy or election outcomes across the reviewed cases.

SEMANTIC_COUNTS_V1:LED:1|CLM:7|AXS:6|CAU:1|CTRL:7|ACT:5

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001"],"evidence_excerpt":"Separate capability, infection, client attribution, data obtained, subsequent use and effect.","kind":"OBJECT_LEAD","lead":"Spyware compromise may become an influence mechanism only when technical access can be connected to a client/operator and a downstream use or effect.","linked_ids":["AXS-001","AXS-002","AXS-003","AXS-004","AXS-005","AXS-006"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001"],"routes":["DERIVE","VERIFY","BREAK"],"source_id":"RUN_CARD","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"French officials and journalists were genuinely compromised with Pegasus; Morocco attribution is strongly supported in the accessible 2026 record.","claimant":"INV-141","counter":["FCT-007","FCT-008"],"gap":"Judicial investigation remains open and not every compromised French target has a complete command/use chain.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-003","FCT-005","FCT-006"]}
CLM-002 | {"claim":"Poland provides a documented case where Pegasus compromise of an opposition campaign chief was followed by exfiltration and media use of manipulated material.","claimant":"INV-141","counter":"NONE_FOUND","gap":"Changed election outcome is not causally established.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-011","FCT-012","FCT-013","FCT-014"]}
CLM-003 | {"claim":"Koukakis provides a case-specific behavioral effect of spyware/surveillance on journalistic practice.","claimant":"INV-141","counter":["FCT-022"],"gap":"Predator infection and EYP wiretap do not by themselves prove one state tasking chain.","gap_type":"RESPONSIBILITY","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-019","FCT-020"]}
CLM-004 | {"claim":"Predator convictions in Greece establish unlawful conduct by a private spyware ecosystem in specific cases.","claimant":"INV-141","counter":["FCT-022"],"gap":"Convictions do not establish state tasking for every infection and are subject to appeal.","gap_type":"RESPONSIBILITY","materiality":"IMPORTANT","status":"PARTIAL","support":["FCT-021","FCT-023"]}
CLM-005 | {"claim":"CatalanGate establishes extensive political/civil-society targeting and infection but does not by itself conclusively attribute the whole operation to a specific Spanish authority.","claimant":"INV-141","counter":["FCT-027","FCT-028"],"gap":"Only 18 admitted CNI interceptions had reviewed judicial authorizations; the remainder require separate attribution.","gap_type":"ATTRIBUTION","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-025","FCT-026"]}
CLM-006 | {"claim":"Authorized surveillance must be separated from unlawful or manipulative influence.","claimant":"INV-141","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-027","FCT-028"]}
CLM-007 | {"claim":"Spyware compromise does not generally establish blackmail, policy change or electoral-result change; downstream effects must be proven case by case.","claimant":"INV-141","counter":"NONE_FOUND","gap":"No general causal design links spyware exposure to policy or election outcomes across the reviewed cases.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-012","FCT-020","FCT-028"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-003","QRY-013","QRY-025"],"axis":"technical_compromise","links":["LED-001"],"question":"Which targets were actually infected or had data exfiltrated, not merely listed or targeted?","result_ids":["FCT-003","FCT-013","FCT-025"],"sought_objects":["forensic infection traces","data exfiltration evidence"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-005","QRY-025"],"axis":"client_attribution","links":["LED-001"],"question":"Which client/operator can be attributed and at what confidence?","result_ids":["FCT-005","FCT-026"],"sought_objects":["client records","official attribution","forensic nexus"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-013"],"axis":"data_access","links":["LED-001"],"question":"Is there evidence that compromised data actually left the device?","result_ids":["FCT-014"],"sought_objects":["exfiltration evidence"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-011","QRY-013"],"axis":"downstream_use","links":["LED-001"],"question":"Was obtained material used for media, coercion, intimidation or decision advantage?","result_ids":["FCT-012","FCT-014"],"sought_objects":["reuse records","media artifacts","coercive communications"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-019"],"axis":"behavioral_effect","links":["LED-001"],"question":"Did surveillance change target behavior or operational practice?","result_ids":["FCT-020"],"sought_objects":["target behavior evidence"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-011","QRY-017","QRY-027"],"axis":"political_electoral_effect","links":["LED-001"],"question":"Is a policy, election result or political decision causally changed?","result_ids":["FCT-012","FCT-018","FCT-028"],"sought_objects":["causal design","decision evidence","outcome attribution"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"CASE_SPECIFIC_USE_OR_BEHAVIOR_ONLY","counter":["FCT-028"],"limit":"Case-specific downstream use/behavior is documented; generalized blackmail, policy-change and electoral-result effects are not established.","mechanism":"technical compromise -> data access/exfiltration -> downstream reuse or target adaptation -> possible political advantage/effect","status":"SUPPORTED","support":["FCT-013","FCT-014","FCT-012","FCT-020"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"targeting/list != infection","status":"PASS","support":["FCT-025","FCT-029","FCT-030"]}
CTRL-002 | {"control":"infection != client attribution","status":"PASS","support":["FCT-025","FCT-026"]}
CTRL-003 | {"control":"vendor/infrastructure != commanditaire","status":"PASS","support":["FCT-021","FCT-022"]}
CTRL-004 | {"control":"data access != blackmail","status":"PASS","support":["FCT-014"]}
CTRL-005 | {"control":"state wiretap overlap != spyware state tasking","status":"PASS","support":["FCT-019","FCT-022"]}
CTRL-006 | {"control":"authorized surveillance != illegitimate influence","status":"PASS","support":["FCT-027","FCT-028"]}
CTRL-007 | {"control":"public smear or behavior change != electoral outcome","status":"PASS","support":["FCT-012","FCT-020"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"acquired Pegasus using Justice Fund financing","actor":"Polish CBA / Justice Ministry financing chain","intent":"PROVEN_PURCHASE","status":"DONE","support":["FCT-009","FCT-010"]}
ACT-002 | {"action":"targeted/exfiltrated opposition campaign chief device according to forensic and Senate record","actor":"Polish Pegasus operators / CBA context","intent":"SURVEILLANCE","status":"DONE","support":["FCT-011","FCT-013","FCT-014"]}
ACT-003 | {"action":"used manipulated phone-derived material in public broadcasting according to Senate findings","actor":"TVP/TVP Info","intent":"PUBLIC_DISSEMINATION","status":"DONE","support":["FCT-012"]}
ACT-004 | {"action":"infected journalist with Predator","actor":"Predator operator not fully resolved in public record","intent":"SURVEILLANCE","status":"DONE","support":["FCT-019","FCT-023"]}
ACT-005 | {"action":"conducted admitted judicially authorized Pegasus interceptions","actor":"Spanish CNI","intent":"INTELLIGENCE_SURVEILLANCE","status":"DONE","support":["FCT-027","FCT-028"]}

SEARCH_ACTIVITY_V1:WEB:15|FETCH:15|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | MNEMO_UNAVAILABLE | MnemoLite | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | France Pegasus parliamentary intelligence inquiry
QRY-002 | FETCH | FETCHED | SRC-001 | https://www.senat.fr/rap/r21-547/r21-5473.html | France Pegasus parliamentary intelligence inquiry
QRY-003 | WEB | FOUND | - | - | France Pegasus Lecornu ANSSI judicial investigation 2026
QRY-004 | FETCH | FETCHED | SRC-002 | https://www.lemonde.fr/pixels/article/2026/07/16/projet-pegasus-cinq-ans-apres-les-revelations-sur-un-systeme-mondial-d-espionnage-de-telephones-l-enquete-judiciaire-se-poursuit_6723735_4408996.html | France Pegasus Lecornu ANSSI judicial investigation 2026
QRY-005 | WEB | FOUND | - | - | Morocco Pegasus Morgan new evidence 2026
QRY-006 | FETCH | FETCHED | SRC-003 | https://www.lemonde.fr/pixels/article/2026/07/16/de-nouvelles-preuves-demontrent-que-le-maroc-a-bien-utilise-le-logiciel-espion-pegasus_6723736_4408996.html | Morocco Pegasus Morgan new evidence 2026
QRY-007 | WEB | FOUND | - | - | French government response Pegasus 2021 investigations
QRY-008 | FETCH | FETCHED | SRC-004 | https://www.senat.fr/questions/base/2021/qSEQ210723956.html | French government response Pegasus 2021 investigations
QRY-009 | WEB | FOUND | - | - | Poland Pegasus purchase CBA Justice Fund 25 million
QRY-010 | FETCH | FETCHED | SRC-005 | https://www.gov.pl/web/sprawiedliwosc/ministerstwo-upublicznia-dokumenty-dotyczace-zakupu-systemu-pegasus | Poland Pegasus purchase CBA Justice Fund 25 million
QRY-011 | WEB | FOUND | - | - | Poland Senate final report Brejza Pegasus election TVP
QRY-012 | FETCH | FETCHED | SRC-006 | https://www.senat.gov.pl/download/gfx/senat/pl/defaultaktualnosci/1924/15764/1/raport_koncowy_z_prac_komisji_nadzwyczajnej.pdf | Poland Senate final report Brejza Pegasus election TVP
QRY-013 | WEB | FOUND | - | - | Citizen Lab Brejza 33 Pegasus attacks data exfiltration Senate hearing
QRY-014 | FETCH | FETCHED | SRC-007 | https://www.senat.gov.pl/prace/komisje-senackie/przebieg%2C9512%2C1.html | Citizen Lab Brejza 33 Pegasus attacks data exfiltration Senate hearing
QRY-015 | WEB | FOUND | - | - | Polish Senate adopts Pegasus report 51 38
QRY-016 | FETCH | FETCHED | SRC-008 | https://www.senat.gov.pl/aktualnoscilista/inne/art%2C15772%2Csenat-podjal-uchwale-w-sprawie-raportu-komisji-nadzwyczajnej-do-spraw-nielegalnej-inwigilacji.html | Polish Senate adopts Pegasus report 51 38
QRY-017 | WEB | FOUND | - | - | European Parliament PEGA spyware resolution 2023 democracy Poland Greece Spain
QRY-018 | FETCH | FETCHED | SRC-009 | https://www.europarl.europa.eu/news/en/press-room/20230609IPR96217/spyware-meps-call-for-full-investigations-and-safeguards-to-prevent-abuse | European Parliament PEGA spyware resolution 2023 democracy Poland Greece Spain
QRY-019 | WEB | FOUND | - | - | Greece Koukakis Predator Amnesty behavior sources
QRY-020 | FETCH | FETCHED | SRC-010 | https://www.amnesty.org/en/latest/news/2023/01/greeces-surveillance-scandal-must-shake-us-out-of-complacency/ | Greece Koukakis Predator Amnesty behavior sources
QRY-021 | WEB | FOUND | - | - | Greek Intellexa conviction appeal March 2026 Reuters
QRY-022 | FETCH | FETCHED | SRC-011 | https://www.reuters.com/business/finance/intellexa-founder-says-he-plans-appeal-greek-court-ruling-over-wiretapping-2026-03-24/ | Greek Intellexa conviction appeal March 2026 Reuters
QRY-023 | WEB | FOUND | - | - | Greek Predator court four guilty February 2026 eKathimerini
QRY-024 | FETCH | FETCHED | SRC-012 | https://www.ekathimerini.com/news/1296353/four-businesspeople-found-guilty-in-spyware-trial/ | Greek Predator court four guilty February 2026 eKathimerini
QRY-025 | WEB | FOUND | - | - | CatalanGate Citizen Lab 65 51 Spain attribution
QRY-026 | FETCH | FETCHED | SRC-013 | https://citizenlab.ca/research/catalangate-extensive-mercenary-spyware-operation-against-catalans-using-pegasus-candiru/ | CatalanGate Citizen Lab 65 51 Spain attribution
QRY-027 | WEB | FOUND | - | - | Spain CNI admits 18 Pegasus judicial authorizations Ombudsman
QRY-028 | FETCH | FETCHED | SRC-014 | https://elpais.com/espana/2022-05-18/el-defensor-avala-las-18-escuchas-con-pegasus-admitidas-por-el-cni-pero-pide-un-mejor-control-judicial.html | Spain CNI admits 18 Pegasus judicial authorizations Ombudsman
QRY-029 | WEB | FOUND | - | - | Citizen Lab CatalanGate correction label error methodology unaffected
QRY-030 | FETCH | FETCHED | SRC-015 | https://citizenlab.ca/research/catalangate-report-correcting-a-case/ | Citizen Lab CatalanGate correction label error methodology unaffected

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | SENAT-FR-R21-547-PEGASUS | Activité de la délégation parlementaire au renseignement pour l'année 2021-2022 — affaire Pegasus | 2022-02-24 | 2026-09-08 | Affaire Pegasus | https://www.senat.fr/rap/r21-547/r21-5473.html
SRC-002 | ○ | fam:other:media-fr | LEMONDE-2026-07-16-PEGASUS-JUDICIAL | Projet Pegasus : cinq ans après, l’enquête judiciaire se poursuit | 2026-07-16 | 2026-09-08 | Enquête judiciaire / cibles françaises | https://www.lemonde.fr/pixels/article/2026/07/16/projet-pegasus-cinq-ans-apres-les-revelations-sur-un-systeme-mondial-d-espionnage-de-telephones-l-enquete-judiciaire-se-poursuit_6723735_4408996.html
SRC-003 | ○ | fam:other:media-fr | LEMONDE-2026-07-16-MOROCCO-PEGASUS | De nouvelles preuves démontrent que le Maroc a bien utilisé Pegasus | 2026-07-16 | 2026-09-08 | Nouveaux documents NSO / éléments ANSSI | https://www.lemonde.fr/pixels/article/2026/07/16/de-nouvelles-preuves-demontrent-que-le-maroc-a-bien-utilise-le-logiciel-espion-pegasus_6723736_4408996.html
SRC-004 | ◈ | fam:A | SENAT-QE-23956 | Réponse de la France dans l’affaire d’espionnage Projet Pegasus | 2021-09-16 | 2026-09-08 | Réponse du ministère de l’Europe et des affaires étrangères | https://www.senat.fr/questions/base/2021/qSEQ210723956.html
SRC-005 | ◈ | fam:B | GOVPL-JUSTICE-PEGASUS-2025 | Ministerstwo upublicznia dokumenty dotyczące zakupu systemu Pegasus | 2025-04-11 | 2026-09-08 | Declassified purchase documents | https://www.gov.pl/web/sprawiedliwosc/ministerstwo-upublicznia-dokumenty-dotyczace-zakupu-systemu-pegasus
SRC-006 | ◈ | fam:C | SENAT-PL-PEGASUS-FINAL-REPORT-2023 | Raport końcowy Komisji Nadzwyczajnej ds. nielegalnej inwigilacji | 2023-09-06 | 2026-09-08 | Inwigilacja senatora Krzysztofa Brejzy | https://www.senat.gov.pl/download/gfx/senat/pl/defaultaktualnosci/1924/15764/1/raport_koncowy_z_prac_komisji_nadzwyczajnej.pdf
SRC-007 | ◈ | fam:C | SENAT-PL-PEGASUS-HEARING-9512 | Polish Senate committee hearing with Citizen Lab on Pegasus | 2022-01-24 | 2026-09-08 | Citizen Lab testimony on Krzysztof Brejza | https://www.senat.gov.pl/prace/komisje-senackie/przebieg%2C9512%2C1.html
SRC-008 | ◈ | fam:C | SENAT-PL-PEGASUS-RESOLUTION-2023 | Senat podjął uchwałę w sprawie raportu Komisji Nadzwyczajnej | 2023-09-07 | 2026-09-08 | Senate resolution adopting commission findings | https://www.senat.gov.pl/aktualnoscilista/inne/art%2C15772%2Csenat-podjal-uchwale-w-sprawie-raportu-komisji-nadzwyczajnej-do-spraw-nielegalnej-inwigilacji.html
SRC-009 | ◈ | fam:other:eu-parliament | EP-PEGA-RESOLUTION-2023 | Spyware: MEPs call for full investigations and safeguards to prevent abuse | 2023-06-15 | 2026-09-08 | Plenary resolution and country recommendations | https://www.europarl.europa.eu/news/en/press-room/20230609IPR96217/spyware-meps-call-for-full-investigations-and-safeguards-to-prevent-abuse
SRC-010 | ◉ | fam:E | AMNESTY-GREECE-PREDATOR-2023 | Greece’s surveillance scandal must shake us out of complacency | 2023-01-26 | 2026-09-08 | Koukakis targeting and impact on journalistic work | https://www.amnesty.org/en/latest/news/2023/01/greeces-surveillance-scandal-must-shake-us-out-of-complacency/
SRC-011 | ○ | fam:other:wire | REUTERS-2026-03-24-INTELLEXA-APPEAL | Intellexa founder plans appeal of Greek spyware ruling | 2026-03-24 | 2026-09-08 | Greek conviction and appeal status | https://www.reuters.com/business/finance/intellexa-founder-says-he-plans-appeal-greek-court-ruling-over-wiretapping-2026-03-24/
SRC-012 | ○ | fam:other:greek-media | EKATHIMERINI-2026-02-26-PREDATOR | Four businesspeople found guilty in 2022 spyware scandal | 2026-02-26 | 2026-09-08 | Athens court verdict | https://www.ekathimerini.com/news/1296353/four-businesspeople-found-guilty-in-spyware-trial/
SRC-013 | ◈ | fam:D | CITIZENLAB-CATALANGATE-2022 | CatalanGate: Extensive Mercenary Spyware Operation against Catalans Using Pegasus and Candiru | 2022-04-18 | 2026-09-08 | Key findings and attribution | https://citizenlab.ca/research/catalangate-extensive-mercenary-spyware-operation-against-catalans-using-pegasus-candiru/
SRC-014 | ○ | fam:other:spanish-media | ELPAIS-2022-05-18-CNI-PEGASUS | El Defensor avala las 18 escuchas con Pegasus admitidas por el CNI | 2022-05-18 | 2026-09-08 | Ombudsman review of 18 CNI interceptions | https://elpais.com/espana/2022-05-18/el-defensor-avala-las-18-escuchas-con-pegasus-admitidas-por-el-cni-pero-pide-un-mejor-control-judicial.html
SRC-015 | ◈ | fam:D | CITIZENLAB-CATALANGATE-CORRECTION-2022 | CatalanGate Report: Correcting a Case | 2022-12-22 | 2026-09-08 | Correction and methodology review | https://citizenlab.ca/research/catalangate-report-correcting-a-case/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.senat.fr/rap/r21-547/r21-5473.html | A | 2022-02-24 | France DPR response | The French parliamentary intelligence delegation opened follow-up work on Pegasus immediately after the July 2021 disclosures because of possible consequences for French territory and nationals. | -
FCT-002 | EVIDENCE | ✧ | https://www.senat.fr/rap/r21-547/r21-5473.html | A | 2022-02-24 | France initial forensic scope | The Senate report records that Amnesty analyses found Pegasus traces on 37 of 67 tested phones and reports the consortium assessment that Morocco was the principal alleged origin of targeting involving French numbers. | -
FCT-003 | EVIDENCE | ✧ | https://www.lemonde.fr/pixels/article/2026/07/16/projet-pegasus-cinq-ans-apres-les-revelations-sur-un-systeme-mondial-d-espionnage-de-telephones-l-enquete-judiciaire-se-poursuit_6723735_4408996.html | other:media-fr | 2026-07-16 | Lecornu compromise | Le Monde reports that ANSSI analysis established that Sébastien Lecornu had been targeted twice by Pegasus while he was minister of the armed forces. | -
FCT-004 | FACT | ✧ | https://www.lemonde.fr/pixels/article/2026/07/16/projet-pegasus-cinq-ans-apres-les-revelations-sur-un-systeme-mondial-d-espionnage-de-telephones-l-enquete-judiciaire-se-poursuit_6723735_4408996.html | other:media-fr | 2026-07-16 | France judicial status 2026 | The French judicial investigation opened after the 2021 Pegasus revelations was still ongoing in July 2026. | -
FCT-005 | EVIDENCE | ✧ | https://www.lemonde.fr/pixels/article/2026/07/16/de-nouvelles-preuves-demontrent-que-le-maroc-a-bien-utilise-le-logiciel-espion-pegasus_6723736_4408996.html | other:media-fr | 2026-07-16 | Morocco client identification | New material reported in 2026, including internal NSO records and corroborating sources, identifies the Pegasus client codename Morgan with Morocco. | -
FCT-006 | EVIDENCE | ✧ | https://www.lemonde.fr/pixels/article/2026/07/16/de-nouvelles-preuves-demontrent-que-le-maroc-a-bien-utilise-le-logiciel-espion-pegasus_6723736_4408996.html | other:media-fr | 2026-07-16 | French target technical correlation | The reported French technical evidence links the Pegasus client that targeted French government figures with many targets of specific interest to Morocco; this strengthens attribution but does not itself prove downstream political use. | -
FCT-007 | FACT | ✧ | https://www.senat.fr/questions/base/2021/qSEQ210723956.html | A | 2021-09-16 | French government seriousness | The French foreign ministry stated in September 2021 that the reported Pegasus facts, if established, would be extremely serious. | -
FCT-008 | FACT | ✧ | https://www.senat.fr/questions/base/2021/qSEQ210723956.html | A | 2021-09-16 | French investigation ordered | The same government response stated that France had ordered investigations into the materiality of the reported espionage and that those investigations were ongoing at that time. | -
FCT-009 | FACT | ✧ | https://www.gov.pl/web/sprawiedliwosc/ministerstwo-upublicznia-dokumenty-dotyczace-zakupu-systemu-pegasus | B | 2025-04-11 | Poland Pegasus purchase documentation | Poland’s Justice Ministry published declassified documents concerning acquisition of Pegasus with Justice Fund resources. | -
FCT-010 | FACT | ✧ | https://www.gov.pl/web/sprawiedliwosc/ministerstwo-upublicznia-dokumenty-dotyczace-zakupu-systemu-pegasus | B | 2025-04-11 | Poland Pegasus financing chain | The published documents describe a 25 million PLN transfer agreement to the CBA signed by then deputy justice minister Michał Woś. | -
FCT-011 | EVIDENCE | ✧ | https://www.senat.gov.pl/download/gfx/senat/pl/defaultaktualnosci/1924/15764/1/raport_koncowy_z_prac_komisji_nadzwyczajnej.pdf | C | 2023-09-06 | Brejza election timing | The Polish Senate commission found that Pegasus attacks on Krzysztof Brejza overlapped the 2019 European and parliamentary election calendars while he led the opposition campaign staff. | -
FCT-012 | EVIDENCE | ✧ | https://www.senat.gov.pl/download/gfx/senat/pl/defaultaktualnosci/1924/15764/1/raport_koncowy_z_prac_komisji_nadzwyczajnej.pdf | C | 2023-09-06 | Brejza downstream media use | The commission found that materials stolen from Brejza’s phone were later manipulated and used in TVP and TVP Info materials. | -
FCT-013 | EVIDENCE | ✧ | https://www.senat.gov.pl/prace/komisje-senackie/przebieg%2C9512%2C1.html | C | 2022-01-24 | Brejza attack count | The Polish Senate hearing records 33 Pegasus attacks against Krzysztof Brejza’s phone. | -
FCT-014 | EVIDENCE | ✧ | https://www.senat.gov.pl/prace/komisje-senackie/przebieg%2C9512%2C1.html | C | 2022-01-24 | Brejza data exfiltration | Citizen Lab testified that forensic evidence showed substantial data leaving Brejza’s device, including at politically sensitive moments. | -
FCT-015 | FACT | ✧ | https://www.senat.gov.pl/aktualnoscilista/inne/art%2C15772%2Csenat-podjal-uchwale-w-sprawie-raportu-komisji-nadzwyczajnej-do-spraw-nielegalnej-inwigilacji.html | C | 2023-09-07 | Polish Senate adoption | The Polish Senate adopted the extraordinary commission’s Pegasus report by 51 votes to 38. | -
FCT-016 | EVIDENCE | ✧ | https://www.senat.gov.pl/aktualnoscilista/inne/art%2C15772%2Csenat-podjal-uchwale-w-sprawie-raportu-komisji-nadzwyczajnej-do-spraw-nielegalnej-inwigilacji.html | C | 2023-09-07 | Polish Senate constitutional finding | As a parliamentary finding, the adopted report states that Pegasus was used against several people critical of the PiS government and that the practices examined grossly violated constitutional standards; this is not a substitute for individual criminal adjudication. | -
FCT-017 | FACT | ✧ | https://www.europarl.europa.eu/news/en/press-room/20230609IPR96217/spyware-meps-call-for-full-investigations-and-safeguards-to-prevent-abuse | other:eu-parliament | 2023-06-15 | European Parliament vote | The European Parliament adopted its spyware resolution by 411 votes in favour, 97 against and 37 abstentions. | -
FCT-018 | EVIDENCE | ✧ | https://www.europarl.europa.eu/news/en/press-room/20230609IPR96217/spyware-meps-call-for-full-investigations-and-safeguards-to-prevent-abuse | other:eu-parliament | 2023-06-15 | EU spyware democratic risk finding | The resolution states that illicit spyware use can put democracy at stake and issues targeted recommendations concerning, among others, Poland, Greece and Spain. | -
FCT-019 | EVIDENCE | ✧ | https://www.amnesty.org/en/latest/news/2023/01/greeces-surveillance-scandal-must-shake-us-out-of-complacency/ | E | 2023-01-26 | Koukakis compromise and separate EYP wiretap | Amnesty reports that Thanasis Koukakis’s phone was infected with Predator and that it was separately revealed he had also been wiretapped by Greece’s National Intelligence Service; the two facts do not by themselves prove a single command chain. | -
FCT-020 | EVIDENCE | ✧ | https://www.amnesty.org/en/latest/news/2023/01/greeces-surveillance-scandal-must-shake-us-out-of-complacency/ | E | 2023-01-26 | Koukakis behavioral effect | Koukakis told Amnesty that the surveillance changed his work: he strengthened communication security and met sources in person. | -
FCT-021 | FACT | ✧ | https://www.reuters.com/business/finance/intellexa-founder-says-he-plans-appeal-greek-court-ruling-over-wiretapping-2026-03-24/ | other:wire | 2026-03-24 | Greek Predator conviction status | Reuters reports that a Greek court found Intellexa founder Tal Dilian and three others guilty of breaching personal data in the Predator wiretapping scandal. | -
FCT-022 | FACT | ✧ | https://www.reuters.com/business/finance/intellexa-founder-says-he-plans-appeal-greek-court-ruling-over-wiretapping-2026-03-24/ | other:wire | 2026-03-24 | Greek attribution control | The defendants planned appeals, while charges against the state intelligence service had been dropped and the Greek government denied wrongdoing; the private-ecosystem conviction therefore does not itself establish state tasking for each infection. | -
FCT-023 | FACT | ✧ | https://www.ekathimerini.com/news/1296353/four-businesspeople-found-guilty-in-spyware-trial/ | other:greek-media | 2026-02-26 | Predator business ecosystem convictions | An Athens court found four businesspeople linked to Intellexa/Krikel guilty of unlawful access and communications/privacy offences in the Predator case. | -
FCT-024 | FACT | ✧ | https://www.ekathimerini.com/news/1296353/four-businesspeople-found-guilty-in-spyware-trial/ | other:greek-media | 2026-02-26 | Predator victim categories | The Greek case concerned illegal wiretapping involving politicians, journalists, business leaders and senior military officials, demonstrating the breadth of the target class without establishing one common political purpose. | -
FCT-025 | EVIDENCE | ✧ | https://citizenlab.ca/research/catalangate-extensive-mercenary-spyware-operation-against-catalans-using-pegasus-candiru/ | D | 2022-04-18 | CatalanGate forensic scale | Citizen Lab identified at least 65 Catalan individuals targeted or infected with mercenary spyware and forensically confirmed Pegasus infections in at least 51 individuals. | -
FCT-026 | EVIDENCE | ✧ | https://citizenlab.ca/research/catalangate-extensive-mercenary-spyware-operation-against-catalans-using-pegasus-candiru/ | D | 2022-04-18 | CatalanGate attribution boundary | Citizen Lab did not conclusively attribute the operation to a specific entity, while judging that strong circumstantial evidence indicated a nexus with Spanish authorities. | -
FCT-027 | FACT | ✧ | https://elpais.com/espana/2022-05-18/el-defensor-avala-las-18-escuchas-con-pegasus-admitidas-por-el-cni-pero-pide-un-mejor-control-judicial.html | other:spanish-media | 2022-05-18 | Spain admitted CNI interceptions | Spain’s CNI acknowledged 18 Pegasus interceptions involving Catalan independence figures that had judicial authorization. | -
FCT-028 | EVIDENCE | ✧ | https://elpais.com/espana/2022-05-18/el-defensor-avala-las-18-escuchas-con-pegasus-admitidas-por-el-cni-pero-pide-un-mejor-control-judicial.html | other:spanish-media | 2022-05-18 | Spain legality control | Spain’s Ombudsman concluded that the reviewed judicial authorizations were extensively reasoned and constitutional, while calling for better judicial control; authorized surveillance therefore cannot be equated automatically with unlawful political influence. | -
FCT-029 | FACT | ✧ | https://citizenlab.ca/research/catalangate-report-correcting-a-case/ | D | 2022-12-22 | CatalanGate correction | Citizen Lab disclosed and corrected a case-labeling error in CatalanGate after re-analysis. | -
FCT-030 | EVIDENCE | ✧ | https://citizenlab.ca/research/catalangate-report-correcting-a-case/ | D | 2022-12-22 | CatalanGate methodology control | Citizen Lab reported that the correction did not change the number of infected individuals and did not affect its technical method for detecting Pegasus infections; this is a methodological control, not proof of attribution. | -
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
FCT-002 | SKIP:NOT_ELIGIBLE
FCT-003 | SKIP:NOT_ELIGIBLE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | SKIP:NOT_ELIGIBLE
FCT-006 | SKIP:NOT_ELIGIBLE
FCT-007 | ELIGIBLE:VERIFIE
FCT-008 | ELIGIBLE:VERIFIE
FCT-009 | ELIGIBLE:VERIFIE
FCT-010 | ELIGIBLE:VERIFIE
FCT-011 | SKIP:NOT_ELIGIBLE
FCT-012 | SKIP:NOT_ELIGIBLE
FCT-013 | SKIP:NOT_ELIGIBLE
FCT-014 | SKIP:NOT_ELIGIBLE
FCT-015 | ELIGIBLE:VERIFIE
FCT-016 | SKIP:NOT_ELIGIBLE
FCT-017 | ELIGIBLE:VERIFIE
FCT-018 | SKIP:NOT_ELIGIBLE
FCT-019 | SKIP:NOT_ELIGIBLE
FCT-020 | SKIP:NOT_ELIGIBLE
FCT-021 | ELIGIBLE:VERIFIE
FCT-022 | ELIGIBLE:VERIFIE
FCT-023 | ELIGIBLE:VERIFIE
FCT-024 | ELIGIBLE:VERIFIE
FCT-025 | SKIP:NOT_ELIGIBLE
FCT-026 | SKIP:NOT_ELIGIBLE
FCT-027 | ELIGIBLE:VERIFIE
FCT-028 | SKIP:NOT_ELIGIBLE
FCT-029 | ELIGIBLE:VERIFIE
FCT-030 | SKIP:NOT_ELIGIBLE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-004 | WRITE | -
FCT-007 | WRITE | -
FCT-008 | WRITE | -
FCT-009 | WRITE | -
FCT-010 | WRITE | -
FCT-015 | WRITE | -
FCT-017 | WRITE | -
FCT-021 | WRITE | -
FCT-022 | WRITE | -
FCT-023 | WRITE | -
FCT-024 | WRITE | -
FCT-027 | WRITE | -
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
ATTEMPT-001 | {"created_at":"2026-09-08T15:39:22.382440+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-029","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":14,"eligible":14,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:14;attempted:0;success:0;failure:0;blocked:14} | WRITEBACK_EXECUTION_V1:[14 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-004 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-007 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-008 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-009 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-010 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-015 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-017 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-021 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-022 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-023 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-024 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-027 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-029 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
