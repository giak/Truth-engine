ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260911-2234-recompense-differee-revolving-door-anticipation | PARENT_RUN_ID:NONE | AS_OF:2026-09-11
INPUT_KIND:RUN_CARD | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/inv157_runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-11_recompense-differee-revolving-door-anticipation/2026-09-11_22-34_recompense-differee-revolving-door-anticipation_INPUT.txt | SUBJECT_SLUG:recompense-differee-revolving-door-anticipation | SUBJECT_FP:sha256:8434f92961fdd6e54a850846c8c46ac2c70af6d05d1b9f85ba0e6a03d9f5e19e | INPUT_SHA256:sha256:f933897d6461ca950db2b1b4bf00c09e2145b0ef5c47b51de13f526c51ec8fb3
COMPLEXITY:8→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France et Union européenne, principalement 2016-2026, avec cas actor-specific reconstructibles. Tracer responsabilité/décision publique -> dossier/acteur privé -> négociation ou anticipation éventuelle -> décision/abstention/information/accès -> sortie de fonction -> emploi/honoraires/board/avantage -> lien probatoire/effet. Gardes : chronology != quid pro quo ; revolving door != corruption ; conflict risk != capture.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
## Résultat analytique technique

L’objet testé est la chaîne `fonction publique -> intérêt/recrutement privé anticipé -> décision publique -> sortie -> emploi/avantage -> lien probatoire`. Le corpus ne soutient pas une équivalence entre porte tournante et corruption. Il ferme en revanche un niveau intermédiaire matériel : un recrutement privé peut commencer avant la sortie de fonction et coexister avec l’exercice de responsabilités directement pertinentes, créant un conflit de risque qui justifie recusal, restrictions ou interdiction sans que la causalité d’une décision biaisée soit démontrée.

### 1. Anticipation : maillon positif fermé, causalité décisionnelle ouverte

`LED-001 / CLM-001 / CAU-001` fournit le cas le plus fort. `FCT-001` reconstruit la séquence Farkas/AFME : prise de contact par le recruteur en avril 2019, entretiens de mai à juillet, offre puis projet de contrat fin juillet, disclosure à l’EBA début août. `FCT-002` ferme l’élément discriminant : pendant cette phase, le directeur exécutif ne s’était pas récusé et travaillait encore sur des dossiers ensuite couverts par les restrictions, dont l’impact et la mise en œuvre de Bâle III. `FCT-003` et `FCT-004` montrent la réponse institutionnelle ultérieure : retrait du travail de politique/supervision, restrictions d’accès et limitations post-service.

Cette séquence dépasse la simple formule `emploi après fonction`. Elle établit `recrutement avant départ + responsabilités concomitantes pertinentes -> risque anticipatoire`. Elle ne ferme toutefois pas `recrutement -> modification d’une décision précise`. `CLM-002` et `CAU-002` restent donc en `GAP_TYPE=CAUSALITY`. Aucun élément inspecté ne démontre une instruction d’AFME, une position EBA modifiée en raison de l’emploi futur, un contrefactuel décisionnel ou une contrepartie promise pour un acte public.

### 2. France : la doctrine préventive distingue risque substantiel et acte impropre

`LED-002 / CLM-003 / CAU-003` borne le cas Djebbari/CMA CGM. `FCT-005` établit un recouvrement direct entre les attributions ministérielles et les activités du groupe ainsi qu’au moins huit rencontres avec le PDG ou des cadres dirigeants sur trois ans. `FCT-006` établit le résultat normatif : la HATVP juge le risque déontologique substantiel, non neutralisable par des réserves, et le projet incompatible.

Ce résultat est fort pour l’évaluation préventive du risque, mais il n’est pas une constatation de favoritisme passé. La décision ne ferme ni une négociation secrète avant un acte public, ni un acte ministériel pris au bénéfice du futur employeur, ni un échange emploi-contre-décision. L’usage probatoire correct est donc : `portfolio overlap + contact density + prospective role -> substantial ethics risk`, pas `-> corruption`.

`LED-003 / CLM-004 / CAU-004` fournit le contrôle négatif indispensable. Dans le dossier Hopium, `FCT-007` établit deux rencontres antérieures, mais aussi l’absence de subvention publique et l’absence, dans les informations disponibles, d’un acte relevant du risque pénal identifié ou d’un élément faisant douter de la manière dont les fonctions avaient été exercées envers l’entreprise. `FCT-008` montre que le projet est autorisé avec des restrictions de représentation d’intérêts. Ce contre-cas réfute l’inférence automatique `même secteur + rencontres + poste privé ultérieur = acte impropre`.

### 3. Kroes/Uber : approche future établie, négociation en fonction et favoritisme non établis

`LED-004 / CLM-005 / CAU-005` est le test contradictoire principal. `FCT-009` montre qu’OLAF a trouvé une approche d’Uber au sujet d’une coopération future alors que Neelie Kroes était encore commissaire, mais n’a pas identifié de négociation professionnelle concrète pendant le mandat et a retenu que la discussion concrète devait être reportée. `FCT-010` indique qu’OLAF n’a pas identifié de processus législatif influencé au bénéfice d’Uber ni de traitement préférentiel établi.

`FCT-011` reconstruit ensuite la demande de rejoindre le conseil consultatif d’Uber pendant la période de refroidissement, l’avis défavorable, le retrait de la demande puis l’entrée au conseil après expiration de cette période. `FCT-012` interdit néanmoins de transformer les non-findings en preuve absolue de non-occurrence : des données électroniques anciennes n’étaient plus conservées et des divulgations sélectives ou caviardées ont limité la reconstruction d’OLAF. Le statut correct est donc `PARTIAL/ACCESS GAP`, non `exonération causale totale` et non `quid pro quo prouvé`.

### 4. Baseline institutionnelle : la porte tournante est un problème de contrôle, pas une qualification pénale par défaut

`FCT-013` matérialise le cadre de l’Union : notification des activités post-service, possibilité d’interdiction ou de conditions, et restriction de lobbying pour certains anciens hauts responsables. `FCT-014` montre que le Médiateur européen a inspecté 100 décisions de la Commission et relevé des cas où l’autorisation subsistait malgré des doutes sur l’efficacité des restrictions. `FCT-015` apporte un dénominateur français utile : sur 639 avis HATVP en 2024, la très grande majorité sont des avis de compatibilité, souvent assortis de réserves, et une minorité des incompatibilités. Ces chiffres mesurent le fonctionnement du contrôle, pas la prévalence de corruption.

`FCT-016` ajoute un contrôle de gouvernance : dans le cas Barroso/Goldman Sachs, le comité d’éthique n’avait pas trouvé de base suffisante pour constater une violation ; une rencontre ultérieure enregistrée comme rencontre Goldman a cependant conduit le Médiateur à demander une réévaluation. Là encore, l’objet établi est la robustesse des règles et l’apparence de lobbying, non une contrepartie antérieure démontrée.

### 5. Verdict causal

Le continuum probatoire issu de `CLM-001..007` et `CAU-001..005` est :

`mobilité légitime -> chevauchement sectoriel -> recrutement/contact avant départ -> conflit de risque/non-récusation -> décision spécifiquement influencée -> promesse/contrepartie -> quid pro quo`.

Le corpus ferme les quatre premiers niveaux dans des configurations différentes. Il ne ferme pas les trois derniers. `CLM-006` réfute l’équivalence automatique `revolving door = corruption`. `CLM-007` conserve explicitement le noyau fort comme gap : aucun cas inspecté ne démontre `avantage privé anticipé -> acte public modifié -> avantage ultérieur promis ou attribué en contrepartie`.

Le résultat central d’INV-157 est donc **ANTICIPATORY_CONFLICT_SUPPORTED / DECISION_CAPTURE_NOT_ESTABLISHED / QUID_PRO_QUO_NOT_ESTABLISHED**. Le mécanisme à retenir pour la cartographie n’est pas une « récompense différée » prouvée, mais une **incitation anticipatoire plausible et parfois documentée au niveau du conflit de risque**, dont la promotion au niveau corruption/capture exige une preuve actor-specific supplémentaire.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:0|EDI_DECISIVE:4|SRC_COMPLETE:10/10

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **item 1:**
  - **date:** 2019-04-18
  - **event:** AFME recruiter first contacts Farkas about CEO role
  - **support:**
    - FCT-001
- **item 2:**
  - **date:** 2019-05/07
  - **event:** Farkas interviews while remaining EBA Executive Director
  - **support:**
    - FCT-001
    - FCT-002
- **item 3:**
  - **date:** 2019-07-29/30
  - **event:** AFME offer and draft employment contract
  - **support:**
    - FCT-001
- **item 4:**
  - **date:** 2019-08-01/02
  - **event:** Farkas discloses intention to resign and asks EBA authorisation
  - **support:**
    - FCT-001
- **item 5:**
  - **date:** 2019-09-12
  - **event:** EBA restrictions decision
  - **support:**
    - FCT-003
    - FCT-004
- **item 6:**
  - **date:** 2014-09/10
  - **event:** Uber approaches Kroes about possible future cooperation; OLAF later finds no concrete in-office negotiation
  - **support:**
    - FCT-009
- **item 7:**
  - **date:** 2015-09/12
  - **event:** Kroes requests Uber advisory role during cooling-off; unfavourable opinion; request withdrawn
  - **support:**
    - FCT-011
- **item 8:**
  - **date:** 2022-03-22
  - **event:** HATVP authorises Hopium project with restrictions
  - **support:**
    - FCT-007
    - FCT-008
- **item 9:**
  - **date:** 2022-04-05
  - **event:** HATVP declares CMA CGM project incompatible
  - **support:**
    - FCT-005
    - FCT-006

### MANIPULATION_REPORT
- **assumptions:**
  - later employment can be legitimate
  - preventive ethics rulings are not criminal findings
  - no inference from chronology alone
- **clusters:**
  - NONE
- **complexity:** COMPLEX/8
- **implicit:**
  - future private role may create anticipatory incentives
  - repeated contacts may create appearance/conflict risk
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - @PAT[BIO]: timing/professional transition relevant but no biography-wide inference
  - @PAT[TEMP]: chronology is diagnostic, never causal by itself
- **priorities:**
  - pre-departure recruitment evidence
  - recusal timing
  - decision-specific effect
  - negative controls
- **query_guidance:**
  - primary ethics decisions
  - official recruitment chronology
  - official investigative findings
  - institutional denominator
- **rhetorical:**
  - NONE
- **speaker:** mechanism-first forensic investigation contract
- **symbol_stage:** FINAL
- **symbols:**
  - **Κ:** 2/10 LOW
  - **Λ:** 1/10 LOW
  - **Ξ:** 2/10 LOW
  - **Σ:** 1/10 LOW
  - **Φ:** 1/10 LOW
  - **Ψ:** 1/10 LOW
  - **Ω:** 1/10 LOW
  - **κ:** 1/10 LOW
  - **ρ:** 2/10 LOW
  - **€:** 4/10 PLAUSIBLE
  - **↕:** 4/10 PLAUSIBLE
  - **⏰:** 4/10 PLAUSIBLE
  - **⚔:** 1/10 LOW
  - **⫸:** 1/10 LOW
  - **🌐:** 4/10 PLAUSIBLE
- **threats:**
  - @THR[REG_CAPTURE]: reviewed because revolving-door signature is present; decision-capture edge not established
  - @THR[POWER_PROX]: proximity/access tested against decision-specific evidence

### MODULE_EXECUTION
NONE

### SCOPING_REPORT
- **ACTORS_INSTITUTIONS:**
  - EBA
  - AFME
  - HATVP
  - CMA CGM
  - Hopium
  - European Commission
  - OLAF
  - Uber
  - European Ombudsman
- **DOMAINS:**
  - public ethics
  - financial regulation
  - transport policy
  - EU institutional governance
- **EVIDENCE_LIMITS:**
  - Kroes historical Commission electronic data no longer retained
  - selective/withheld Uber material limited OLAF reconstruction
  - no subpoena-grade private employment negotiations for French cases
- **EXCLUSIONS:**
  - generic career mobility without public-decision overlap
  - mere network proximity
  - criminal qualification without adjudicated facts
  - non-European cases except no material comparator was needed
- **GEO:** France and European Union
- **LEAD_QUESTION:** Does later private employment evidence a deferred reward for prior public action?
- **OBJECT_COVERAGE:** Farkas positive anticipation/conflict-risk case; Djebbari CMA preventive incompatibility; Hopium negative control; Kroes official investigative counter-case; systemic EU/HATVP denominator.
- **OBJECT_QUESTION:** When does a later move from public office to a company/cabinet/board remain legitimate mobility, and what evidence is needed to cross conflict risk -> anticipation -> promise/consideration -> influenced decision -> quid pro quo?
- **PERIOD:** primarily 2016-2026, with 2014-2015 Kroes chronology retained as a directly relevant comparator

### CREDO
- **rules:**
  - chronology != quid pro quo
  - revolving door != corruption
  - conflict risk != capture
  - future employment != prior favoritism
  - ethics restriction != wrongdoing
  - absence of evidence != evidence of absence
- **truth_ceiling:** Stop at the highest closed evidentiary edge even if the stronger hypothesis is plausible.

### COGNITIVE_MAP
- **closed_level:** pre-departure recruitment/contact + conflict-risk overlap in Farkas; preventive ethics incompatibility in Djebbari/CMA CGM
- **ladder:**
  - legitimate mobility
  - sector/portfolio overlap
  - pre-departure recruitment/contact
  - non-recusal or unmanaged conflict risk
  - decision-specific influence
  - promise/consideration
  - quid pro quo/deferred reward
- **unclosed_levels:**
  - decision-specific influence caused by expected private benefit
  - promise/consideration tied to public act
  - quid pro quo

### DIALECTICAL_MAP
- **perspectives:**
  - **item 1:**
    - **best_case:** Even unproven conflicts can damage impartiality and trust; preventive prohibition may be justified when restrictions cannot neutralise risk.
    - **id:** P1
    - **position:** strict integrity/governance
    - **support:**
      - FCT-006
      - FCT-014
  - **item 2:**
    - **best_case:** Most mobility can be compatible under safeguards; professional movement and prior official contact do not establish misconduct.
    - **id:** P2
    - **position:** mobility/expertise rights
    - **support:**
      - FCT-007
      - FCT-008
      - FCT-015
  - **item 3:**
    - **best_case:** Recruitment before departure can create anticipatory incentives; Farkas shows the mechanism can exist at conflict-risk level.
    - **id:** P3
    - **limit:** No inspected case closes specific decision change or quid pro quo.
    - **position:** deferred-reward/capture hypothesis
    - **support:**
      - FCT-001
      - FCT-002

### RESOURCE_FLOW_MAP
- **item 1:**
  - **case:** Farkas/AFME
  - **flow:** prospective CEO employment -> recruitment/interviews/offer while public role continues -> later private position
  - **status:** ANTICIPATORY_PRIVATE_BENEFIT_CONTEXT_SUPPORTED
  - **support:**
    - FCT-001
    - FCT-002
- **item 2:**
  - **case:** Djebbari/CMA CGM
  - **flow:** prospective executive role -> direct portfolio overlap + repeated prior official contacts -> preventive incompatibility
  - **status:** ETHICS_RISK_SUPPORTED_NO_EXCHANGE_PROVEN
  - **support:**
    - FCT-005
    - FCT-006
- **item 3:**
  - **case:** Djebbari/Hopium
  - **flow:** prospective remunerated board role -> sector overlap + two prior meetings -> compatibility with restrictions
  - **status:** NEGATIVE_CONTROL
  - **support:**
    - FCT-007
    - FCT-008
- **item 4:**
  - **case:** Kroes/Uber
  - **flow:** future-cooperation approach -> later cooling-off request -> eventual board role after cooling-off
  - **status:** APPROACH_SUPPORTED_CONCRETE_IN_OFFICE_NEGOTIATION_NOT_ESTABLISHED
  - **support:**
    - FCT-009
    - FCT-011

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** AFME/recruiter
  - **relation:** recruitment/interviews/job offer
  - **support:**
    - FCT-001
  - **to:** Adam Farkas while EBA Executive Director
- **item 2:**
  - **from:** Adam Farkas
  - **relation:** continued work during recruitment
  - **support:**
    - FCT-002
  - **to:** EBA policy topics including Basel III implementation
- **item 3:**
  - **from:** CMA CGM senior executives
  - **relation:** at least eight official meetings over three years
  - **support:**
    - FCT-005
  - **to:** Jean-Baptiste Djebbari
- **item 4:**
  - **from:** Hopium CEO
  - **relation:** two official meetings
  - **support:**
    - FCT-007
  - **to:** Jean-Baptiste Djebbari
- **item 5:**
  - **from:** Uber/associated contact
  - **relation:** approach about possible future cooperation
  - **support:**
    - FCT-009
  - **to:** Neelie Kroes while Commissioner

### IMPACT_MAP
- **decision_effect:** No specific public decision change attributable to expected private employment established in inspected cases.
- **democratic_effect:** NOT_COMPUTABLE; the run concerns integrity/conflict mechanisms, not measured electoral persuasion or voting effects.
- **institutional:**
  - recusal/reallocation of responsibilities
  - post-service lobbying/contact restrictions
  - prohibition of a proposed private role
  - compatibility subject to safeguards
- **support:**
  - FCT-003
  - FCT-006
  - FCT-008
  - FCT-014
  - FCT-015

### CONTRADICTION_LEDGER
- **item 1:**
  - **issue:** Farkas conflict assessment
  - **resolution:** Conflict-risk chronology supported; specific biased decision not established.
  - **side_a:** Recruitment overlapped with unrelinquished relevant responsibilities.
  - **side_b:** EBA argued his specific duties during the period did not create a conflict; later imposed restrictions.
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
- **item 2:**
  - **issue:** Kroes/Uber in-office recruitment
  - **resolution:** Approach supported; stronger negotiation/favouritism claim not established; access limitations preserved.
  - **side_a:** Uber approached her about possible future cooperation.
  - **side_b:** OLAF found no concrete in-office professional negotiation or regulatory favouring.
  - **support:**
    - FCT-009
    - FCT-010
    - FCT-012
- **item 3:**
  - **issue:** Djebbari sector proximity
  - **resolution:** Case-specific contact density, portfolio nexus and prior acts matter; sector adjacency alone is not dispositive.
  - **side_a:** CMA CGM case deemed incompatible due substantial ethics risk.
  - **side_b:** Hopium case compatible with restrictions despite sector overlap and prior meetings.
  - **support:**
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-008

### VERIFICATION_REPORT
- **contradictions_material:** 3
- **critical_result:** No evidence object in the inspected corpus closes promise/consideration -> public act -> later benefit as quid pro quo.
- **domains:**
  - **INSTITUTIONAL_GOVERNANCE:** 4
  - **LEGAL_ETHICS:** 10
  - **REGULATORY:** 2
- **fact_level_refutations:** 0
- **pdf_visual_check:** HATVP CMA CGM relevant page visually inspected; Hopium and OLAF screenshot fetches returned cache misses, so their parsed PDF text was used and the access limitation is recorded.
- **primary_source_facts:** 16
- **status:** PASS_WITH_CAUSAL_GAPS
- **verified_facts:** 16

### EDI_REPORT
- **corpus:**
  - **families:** 5
  - **notes:** Primary institutional corpus across EU Ombudsman, EBA, HATVP, OLAF/Commission and EUR-Lex; deliberately optimised for decision/recruitment chronology rather than media-volume diversity.
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim:** anticipatory recruitment overlap
    - **facts:**
      - FCT-001
      - FCT-002
    - **status:** COVERED
  - **item 2:**
    - **claim:** decision influence caused by anticipated reward
    - **facts:**
      - FCT-002
      - FCT-010
    - **status:** GAP_CAUSALITY
  - **item 3:**
    - **claim:** quid pro quo/deferred reward
    - **facts:**
      - NONE
    - **status:** GAP_CAUSALITY
  - **item 4:**
    - **claim:** negative controls
    - **facts:**
      - FCT-007
      - FCT-008
      - FCT-009
      - FCT-010
    - **status:** COVERED
- **diagnostic_not_truth:** true
- **dimensions:**
  - **geo:** 0.7
  - **lang:** 0.65
  - **owner:** 0.35
  - **persp:** 0.4
  - **strat:** 0.85
  - **temp:** 0.75
- **edi:**
  - **band:** ADEQUATE
  - **score:** 0.63
- **source_counts:**
  - **◈:** 10
  - **◉:** 0
  - **○:** 0

### RESPONSIBILITY_MAP
- **item 1:**
  - **actor:** EBA
  - **evidence:**
    - FCT-003
    - FCT-004
  - **limit:** institutional response does not establish corrupt motive
  - **responsibility:** manage conflict and access during/after Farkas transition
- **item 2:**
  - **act_id:** ACT-004
  - **actor:** Adam Farkas
  - **evidence:**
    - FCT-001
    - FCT-002
  - **intent:** NOT_INFERRED
  - **limit:** no decision-specific favouring or quid pro quo established
  - **responsibility:** continued official responsibilities during the recruitment interval before later recusal/restrictions
- **item 3:**
  - **actor:** HATVP
  - **evidence:**
    - FCT-006
    - FCT-008
  - **limit:** ethics ruling is not criminal adjudication
  - **responsibility:** preventive compatibility assessment
- **item 4:**
  - **actor:** OLAF
  - **evidence:**
    - FCT-009
    - FCT-010
    - FCT-012
  - **limit:** historical data and selective disclosure constrained reconstruction
  - **responsibility:** investigate alleged Kroes conflict/favouritism

### NEXT_QUERIES
- **item 1:**
  - **query:** primary employment negotiation records tied to a specific public decision before departure in France/EU
  - **route:** RECHECK
  - **trigger:** new judicial/FOI/employment-record evidence
- **item 2:**
  - **query:** adjudicated corruption or influence-peddling case where post-office employment is the promised consideration for a prior public act
  - **route:** RECHECK
  - **trigger:** named case with primary decision record
- **item 3:**
  - **query:** representative denominator linking revolving-door cases to measured decision outcomes rather than ethics opinions
  - **route:** RESEARCH_GAP
  - **trigger:** dataset or causal-design availability

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-007,QRY-008,QRY-009 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-010 | support:- | counter:- | results:FCT-005,FCT-006 | final:SATURATED | gap:NONE
LED-003 | attempts:QRY-011 | support:- | counter:- | results:FCT-007,FCT-008 | final:SATURATED | gap:NONE
LED-004 | attempts:QRY-004,QRY-012 | support:- | counter:- | results:FCT-009,FCT-010,FCT-011,FCT-012 | final:SATURATED | gap:NONE
LED-005 | attempts:QRY-005,QRY-014,QRY-015 | support:- | counter:- | results:FCT-014,FCT-015 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-007,QRY-008,QRY-009,QRY-010 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-005,FCT-006,CAU-001,CAU-003 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-007,QRY-012 | support:- | counter:- | results:FCT-002,FCT-010,CAU-002,CAU-005 | final:GAP | gap:CAUSALITY
AXS-003 | attempts:QRY-007,QRY-012,QRY-016 | support:- | counter:- | results:FCT-001,FCT-009,FCT-010,FCT-016,CAU-002 | final:GAP | gap:CAUSALITY
AXS-004 | attempts:QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-007,FCT-008,FCT-009,FCT-010,FCT-013,CAU-004 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-013,QRY-014,QRY-015 | support:- | counter:- | results:FCT-013,FCT-014,FCT-015 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-007,QRY-012,SRC-001,SRC-006 | support:FCT-001,FCT-002 | counter:FCT-009 | results:FCT-001,FCT-002,FCT-009 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-007,QRY-008,SRC-001,SRC-002 | support:- | counter:FCT-002,FCT-003 | results:FCT-002,FCT-003 | final:GAP | gap:CAUSALITY
CLM-003 | attempts:QRY-010,SRC-004 | support:FCT-005,FCT-006 | counter:- | results:FCT-005,FCT-006 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-011,SRC-005 | support:- | counter:FCT-007,FCT-008 | results:FCT-007,FCT-008 | final:REFUTED | gap:NONE
CLM-005 | attempts:QRY-012,SRC-006 | support:FCT-009 | counter:FCT-009,FCT-010 | results:FCT-009,FCT-009,FCT-010 | final:PARTIAL | gap:ACCESS
CLM-006 | attempts:QRY-011,QRY-012,QRY-013,QRY-015,QRY-016,SRC-005,SRC-006,SRC-007,SRC-009,SRC-010 | support:- | counter:FCT-007,FCT-008,FCT-010,FCT-013,FCT-015,FCT-016 | results:FCT-007,FCT-008,FCT-010,FCT-013,FCT-015,FCT-016 | final:REFUTED | gap:NONE
CLM-007 | attempts:QRY-007,QRY-010,QRY-012,QRY-016,SRC-001,SRC-004,SRC-006,SRC-010 | support:- | counter:FCT-002,FCT-006,FCT-010,FCT-016 | results:FCT-002,FCT-006,FCT-010,FCT-016 | final:GAP | gap:CAUSALITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
AXS-002 | AXS | GAP | CAUSALITY | No inspected case closes anticipated private benefit -> specific changed public decision with a defensible counterfactual.
AXS-003 | AXS | GAP | CAUSALITY | No inspected France/EU case establishes a benefit promised or granted in exchange for an identified public act.
CLM-002 | CLM | GAP | CAUSALITY | Recruitment overlap and non-recusal are documented, but no inspected record closes an altered decision, counterfactual effect or quid pro quo.
CLM-005 | CLM | PARTIAL | ACCESS | OLAF found an approach for future cooperation but no concrete in-office negotiation; historical Commission data had expired and disclosure was incomplete, so stronger absence claims are not justified.
CLM-007 | CLM | GAP | CAUSALITY | The corpus reaches anticipatory conflict risk in Farkas and preventive ethics risk in Djebbari/CMA CGM, but not decision influence -> promised private benefit -> quid pro quo.
CAU-002 | CAU | GAP | CAUSALITY | Missing edge from anticipated private benefit to identifiable changed public act, and from that act to promised/granted reward.
CAU-005 | CAU | UNRESOLVED | ACCESS | Expired Commission data and selective disclosure prevent upgrading non-finding into proof of non-occurrence; available evidence nevertheless does not close the stronger causal chain.

SEMANTIC_COUNTS_V1:LED:5|CLM:7|AXS:5|CAU:5|CTRL:5|ACT:4

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-007","QRY-008","QRY-009"],"evidence_excerpt":"Recruiter contact 18 Apr 2019; interviews May-July; offer 29 Jul; no recusal during recruitment; Basel III work continued.","kind":"MECHANISM","lead":"Farkas entered an AFME recruitment process while still EBA Executive Director and continued working on policy matters relevant to the future employer until recusal after disclosure.","linked_ids":["AXS-001","CLM-001","CAU-001"],"locator":"paras 35-38 + annex timeline","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004"],"routes":["EXPAND","LINK"],"source_id":"SRC-001","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-010"],"evidence_excerpt":"Direct portfolio overlap; at least eight meetings; substantial ethical risk; proposed role incompatible.","kind":"MECHANISM","lead":"Djebbari/CMA CGM tests whether heavy portfolio overlap and repeated official contacts can make a future role ethically incompatible without proving a prior quid pro quo.","linked_ids":["AXS-001","AXS-004","CLM-003","CAU-003"],"locator":"paras 7-10","materiality":"IMPORTANT","result_ids":["FCT-005","FCT-006"],"routes":["EXPAND","LINK"],"source_id":"SRC-004","status":"SATURATED"}
LED-003 | {"attempt_ids":["QRY-011"],"evidence_excerpt":"Two meetings; no public subsidy; no identified Article 432-13 act; no element casting doubt on prior exercise; compatibility with reservations.","kind":"MECHANISM","lead":"Djebbari/Hopium is a negative control: same broad sector plus two prior official meetings did not produce an identified prior-act conflict and the move was authorised with restrictions.","linked_ids":["AXS-004","CLM-004","CAU-004"],"locator":"paras 8-14","materiality":"IMPORTANT","result_ids":["FCT-007","FCT-008"],"routes":["EXPAND","LINK"],"source_id":"SRC-005","status":"SATURATED"}
LED-004 | {"attempt_ids":["QRY-004","QRY-012"],"evidence_excerpt":"Approach for future cooperation found; concrete discussion postponed; no in-office professional negotiation or legislative favouring established; incomplete historical data and selective disclosure noted.","kind":"MECHANISM","lead":"Kroes/Uber tests whether an in-office approach for future cooperation crossed into concrete negotiation or decision favouring; OLAF found approach but not the stronger edges and documented evidence-access limits.","linked_ids":["AXS-002","AXS-003","CLM-005","CAU-005"],"locator":"summary + sections 2.3.1-2.3.4","materiality":"DECISIVE","result_ids":["FCT-009","FCT-010","FCT-011","FCT-012"],"routes":["AUDIT","EXPAND","LINK"],"source_id":"SRC-006","status":"SATURATED"}
LED-005 | {"attempt_ids":["QRY-005","QRY-014","QRY-015"],"evidence_excerpt":"100 Commission decisions inspected; some senior moves approved despite mitigation concerns.","kind":"CONTEXT","lead":"Systemic controls distinguish common managed mobility from the rarer cases where restrictions are insufficient; risk regulation is not a corruption prevalence measure.","linked_ids":["AXS-005","CLM-006"],"locator":"100-file strategic inquiry","materiality":"IMPORTANT","result_ids":["FCT-014","FCT-015"],"routes":["CONTEXT","LINK"],"source_id":"SRC-008","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"A recruitment process for a future industry role can overlap in time with continued exercise of public regulatory responsibilities.","claimant":"INV-157 synthesis","counter":["FCT-009"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002"]}
CLM-002 | {"claim":"The Farkas/AFME recruitment overlap changed a specific EBA regulatory decision in AFME's favour.","claimant":"INV-157 causal test","counter":["FCT-002","FCT-003"],"gap":"Recruitment overlap and non-recusal are documented, but no inspected record closes an altered decision, counterfactual effect or quid pro quo.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"GAP","support":"NONE_FOUND"}
CLM-003 | {"claim":"Djebbari/CMA CGM establishes a substantial preventive ethics risk from portfolio overlap and repeated contacts without itself establishing prior favoritism or corruption.","claimant":"INV-157 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-005","FCT-006"]}
CLM-004 | {"claim":"Sector adjacency and prior official meetings are sufficient by themselves to establish improper revolving-door conduct.","claimant":"automatic-equivalence hypothesis","counter":["FCT-007","FCT-008"],"gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"REFUTED","support":"NONE_FOUND"}
CLM-005 | {"claim":"Kroes entered concrete professional negotiations with Uber while still a Commissioner.","claimant":"Uber Files allegation tested by OLAF","counter":["FCT-009","FCT-010"],"gap":"OLAF found an approach for future cooperation but no concrete in-office negotiation; historical Commission data had expired and disclosure was incomplete, so stronger absence claims are not justified.","gap_type":"ACCESS","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-009"]}
CLM-006 | {"claim":"Revolving door, later private employment or ethics restrictions are equivalent to corruption or quid pro quo.","claimant":"automatic-equivalence hypothesis","counter":["FCT-007","FCT-008","FCT-010","FCT-013","FCT-015","FCT-016"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"REFUTED","support":"NONE_FOUND"}
CLM-007 | {"claim":"A deferred private reward was promised or granted in exchange for an identified public act in the inspected France/EU cases.","claimant":"INV-157 core hypothesis","counter":["FCT-002","FCT-006","FCT-010","FCT-016"],"gap":"The corpus reaches anticipatory conflict risk in Farkas and preventive ethics risk in Djebbari/CMA CGM, but not decision influence -> promised private benefit -> quid pro quo.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"GAP","support":"NONE_FOUND"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-007","QRY-008","QRY-009","QRY-010"],"axis":"MECHANISMS","links":["LED-001","LED-002"],"question":"Can recruitment or job negotiation begin before departure while public responsibilities continue?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-005","FCT-006","CAU-001","CAU-003"],"sought_objects":["recruitment chronology","recusal records","job offer timing","public-duty overlap"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-007","QRY-012"],"axis":"IMPACT_RESPONSIBILITY","gap":"No inspected case closes anticipated private benefit -> specific changed public decision with a defensible counterfactual.","gap_type":"CAUSALITY","links":["LED-001","LED-004"],"question":"Is there evidence that anticipated private employment changed a specific public decision or abstention?","result_ids":["FCT-002","FCT-010","CAU-002","CAU-005"],"sought_objects":["decision-specific record","before/after position","tasking or request","counterfactual decision evidence"],"status":"GAP"}
AXS-003 | {"attempt_ids":["QRY-007","QRY-012","QRY-016"],"axis":"COUNTER_HYPOTHESES","gap":"No inspected France/EU case establishes a benefit promised or granted in exchange for an identified public act.","gap_type":"CAUSALITY","links":["LED-001","LED-004"],"question":"Is a promise, quid pro quo or deferred reward for a public act established?","result_ids":["FCT-001","FCT-009","FCT-010","FCT-016","CAU-002"],"sought_objects":["pre-decision promise","employment consideration tied to act","communication linking benefit to act","adjudicated quid pro quo"],"status":"GAP"}
AXS-004 | {"attempt_ids":["QRY-011","QRY-012","QRY-013"],"axis":"RULES_CONTROLS","links":["LED-003","LED-004"],"question":"Do comparable revolving-door cases exist where proximity and later employment do not establish misconduct?","result_ids":["FCT-007","FCT-008","FCT-009","FCT-010","FCT-013","CAU-004"],"sought_objects":["compatibility opinion","absence of prior relevant act","restrictions","negative finding"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-013","QRY-014","QRY-015"],"axis":"SCOPE_HISTORY","links":["LED-005"],"question":"What do institutional denominators show about the baseline frequency of authorised, restricted and prohibited mobility?","result_ids":["FCT-013","FCT-014","FCT-015"],"sought_objects":["Commission sample","HATVP mobility statistics","legal post-service rules"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"Documented temporal overlap plus continuing relevant official responsibilities supports the conflict-risk mechanism only.","counter":["FCT-009","FCT-010"],"limit":"Closes anticipation/conflict-risk chronology, not a biased decision or exchange.","mechanism":"prospective-employer recruitment begins while official remains in regulatory role -> concurrent duties on employer-relevant issues -> unmanaged/late-recused conflict risk","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003"],"type":"CONFLICT_RISK"}
CAU-002 | {"counter":["FCT-002","FCT-010","FCT-016"],"gap":"Missing edge from anticipated private benefit to identifiable changed public act, and from that act to promised/granted reward.","gap_type":"CAUSALITY","limit":"No decision-specific counterfactual or exchange evidence in inspected cases.","mechanism":"anticipated private employment -> altered public decision -> later job/benefit as quid pro quo","status":"GAP","support":"NONE_FOUND","type":"CAUSE"}
CAU-003 | {"causal_right":"Official ethics determination supports risk-generation from overlap and contact density, not behavioral corruption causation.","counter":["FCT-007"],"limit":"HATVP determination is preventive and does not establish that prior ministerial decisions were improperly influenced.","mechanism":"direct portfolio overlap + repeated contacts with prospective employer -> post-office role -> substantial appearance/impartiality risk","status":"SUPPORTED","support":["FCT-005","FCT-006"],"type":"PREVENTIVE_RISK"}
CAU-004 | {"causal_right":"Negative comparator demonstrates that proximity and chronology alone do not force an impropriety classification.","counter":["FCT-005","FCT-006"],"limit":"Case-specific negative control; does not imply all such moves are benign.","mechanism":"same-sector future role + limited prior official contacts + no identified relevant official act/subsidy -> compatibility with restrictions","status":"SUPPORTED","support":["FCT-007","FCT-008"],"type":"NEGATIVE_CONTROL"}
CAU-005 | {"counter":["FCT-009","FCT-010"],"gap":"Expired Commission data and selective disclosure prevent upgrading non-finding into proof of non-occurrence; available evidence nevertheless does not close the stronger causal chain.","gap_type":"ACCESS","limit":"OLAF did not establish concrete negotiation or favouring and documented access limitations.","mechanism":"in-office approach for future Uber cooperation -> concrete negotiation or regulatory favour -> later board role","status":"UNRESOLVED","support":["FCT-009","FCT-011"],"type":"UNRESOLVED_CAUSAL"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"chronology != quid pro quo","status":"DONE","support":["FCT-007","FCT-009","FCT-016"]}
CTRL-002 | {"control":"revolving door != corruption","status":"DONE","support":["FCT-007","FCT-008","FCT-015"]}
CTRL-003 | {"control":"conflict risk != proven decision capture","status":"DONE","support":["FCT-002","FCT-006","FCT-010"]}
CTRL-004 | {"control":"ethics restriction or incompatibility != proof of wrongdoing","status":"DONE","support":["FCT-006","FCT-008","FCT-013"]}
CTRL-005 | {"control":"absence of found quid-pro-quo evidence != proof that no quid pro quo can exist outside the inspected corpus","status":"DONE","support":["FCT-012"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Preserve Farkas as the positive anticipation/conflict-risk case, but cap the inference before decision bias or quid pro quo.","actor":"routing/control plane","intent":"prevent causal inflation","status":"DONE","support":["FCT-001","FCT-002","FCT-003"]}
ACT-002 | {"action":"Use Hopium and Kroes findings as explicit negative/counter controls against chronology-only inference.","actor":"future synthesis/article protocol","intent":"preserve symmetry and falsifiability","status":"DONE","support":["FCT-007","FCT-008","FCT-009","FCT-010"]}
ACT-003 | {"action":"Reopen deferred-reward corruption only on primary evidence tying a pre-decision promise/negotiation to an identified public act and subsequent benefit.","actor":"future investigation","intent":"close missing quid-pro-quo edge","status":"DEFERRED","support":["FCT-002","FCT-012"]}
ACT-004 | {"action":"Continued to exercise EBA responsibilities during the AFME recruitment process before later recusal/restrictions.","actor":"Adam Farkas","intent":"NOT_INFERRED; action/timing only","status":"DONE","support":["FCT-001","FCT-002"]}

SEARCH_ACTIVITY_V1:WEB:6|FETCH:10|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"EMPTY","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL | mnemo | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | https://www.ombudsman.europa.eu/ga/recommendation/en/127638 | Adam Farkas EBA AFME recruitment chronology conflict interest
QRY-002 | WEB | FOUND | - | https://www.hatvp.fr/wordpress/wp-content/uploads/2022/05/2022-123-Jean-Baptiste-Djebbari.pdf | Jean-Baptiste Djebbari CMA CGM HATVP 2022-123
QRY-003 | WEB | FOUND | - | https://www.hatvp.fr/wordpress/wp-content/uploads/2022/05/2022-104-Jean-Baptiste-Djebbari.pdf | Jean-Baptiste Djebbari Hopium HATVP 2022-104
QRY-004 | WEB | FOUND | - | https://www.politico.eu/wp-content/uploads/2024/03/07/final-report-oc-2022-0514-redacted_final57.pdf | Neelie Kroes Uber OLAF final report OC/2022/0514/A1
QRY-005 | WEB | FOUND | - | https://www.ombudsman.europa.eu/en/decision/en/155953 | European Commission revolving doors 100 decisions Ombudsman 2019 2021
QRY-006 | WEB | FOUND | - | https://www.ombudsman.europa.eu/ro/recommendation/en/90956 | Barroso Goldman Sachs European Ombudsman recommendation 2018
QRY-007 | FETCH | FOUND | SRC-001 | https://www.ombudsman.europa.eu/ga/recommendation/en/127638 | Ombudsman Farkas recommendation inspected
QRY-008 | FETCH | FOUND | SRC-002 | https://www.eba.europa.eu/publications-and-media/press-releases/adam-farkas-steps-down-eba-executive-director | EBA Farkas resignation and restrictions inspected
QRY-009 | FETCH | FOUND | SRC-003 | https://www.eba.europa.eu/sites/default/files/document_library/About%20Us/Internal%20Organisation/Occupational%20activities%20after%20leaving%20the%20EBA/1025899/Senior%20Staff_2019%20AFME_Adam%20Farkas.pdf | EBA detailed Farkas occupational activity assessment inspected
QRY-010 | FETCH | FOUND | SRC-004 | https://www.hatvp.fr/wordpress/wp-content/uploads/2022/05/2022-123-Jean-Baptiste-Djebbari.pdf | HATVP Djebbari CMA CGM decision inspected
QRY-011 | FETCH | FOUND | SRC-005 | https://www.hatvp.fr/wordpress/wp-content/uploads/2022/05/2022-104-Jean-Baptiste-Djebbari.pdf | HATVP Djebbari Hopium decision inspected
QRY-012 | FETCH | FOUND | SRC-006 | https://www.politico.eu/wp-content/uploads/2024/03/07/final-report-oc-2022-0514-redacted_final57.pdf | OLAF Kroes Uber final report inspected
QRY-013 | FETCH | FOUND | SRC-007 | https://eur-lex.europa.eu/eli/reg/2013/1023/oj/eng | EU Staff Regulations Article 16 inspected
QRY-014 | FETCH | FOUND | SRC-008 | https://www.ombudsman.europa.eu/en/decision/en/155953 | European Ombudsman strategic revolving-door inquiry inspected
QRY-015 | FETCH | FOUND | SRC-009 | https://www.hatvp.fr/presse/rapport-dactivite-2024-de-la-haute-autorite/ | HATVP 2024 mobility statistics inspected
QRY-016 | FETCH | FOUND | SRC-010 | https://www.ombudsman.europa.eu/ro/recommendation/en/90956 | Ombudsman Barroso Goldman Sachs recommendation inspected

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | EO-2168-2019-KR | European Ombudsman — Recommendation 2168/2019/KR, EBA/Farkas/AFME | 2020-05-07 | 2026-09-11T20:36:43Z | paras 35-38 and Annex timeline: recruitment 18 Apr-Jul 2019; offer 29 Jul; no recusal during recruitment; Basel III work | https://www.ombudsman.europa.eu/ga/recommendation/en/127638
SRC-002 | ◈ | fam:B | EBA-2019-09-17-FARKAS | European Banking Authority — Adam Farkas steps down as Executive Director | 2019-09-17 | 2026-09-11T20:36:43Z | press release: conflict assessment; policy/supervisory removal; 18/24-month post-service restrictions | https://www.eba.europa.eu/publications-and-media/press-releases/adam-farkas-steps-down-eba-executive-director
SRC-003 | ◈ | fam:B | EBA-SENIOR-STAFF-2019-FARKAS-AFME | EBA — Senior Staff 2019 AFME Adam Farkas detailed assessment | 2022-01-13 | 2026-09-11T20:36:43Z | Decision 12 Sep 2019; restrictions during service and after departure; Basel III and related topics | https://www.eba.europa.eu/sites/default/files/document_library/About%20Us/Internal%20Organisation/Occupational%20activities%20after%20leaving%20the%20EBA/1025899/Senior%20Staff_2019%20AFME_Adam%20Farkas.pdf
SRC-004 | ◈ | fam:C | HATVP-2022-123-DJEBBARI-CMACGM | HATVP — Délibération 2022-123, Jean-Baptiste Djebbari / CMA CGM | 2022-04-05 | 2026-09-11T20:36:43Z | paras 7-10: direct portfolio overlap; at least eight meetings; substantial ethics risk; incompatibility | https://www.hatvp.fr/wordpress/wp-content/uploads/2022/05/2022-123-Jean-Baptiste-Djebbari.pdf
SRC-005 | ◈ | fam:C | HATVP-2022-104-DJEBBARI-HOPIUM | HATVP — Délibération 2022-104, Jean-Baptiste Djebbari / Hopium | 2022-03-22 | 2026-09-11T20:36:43Z | paras 8-14: no identified art.432-13 act; two meetings; no subsidy; compatibility with three-year restrictions | https://www.hatvp.fr/wordpress/wp-content/uploads/2022/05/2022-104-Jean-Baptiste-Djebbari.pdf
SRC-006 | ◈ | fam:D | OLAF-OC-2022-0514-A1-FINAL | OLAF — Final report OC/2022/0514/A1, Neelie Kroes / Uber | 2023-12-01 | 2026-09-11T20:36:43Z | summary and sections 2.3.1-2.3.4: approach for future role; no concrete in-office negotiation or favouring established; evidence-access limits | https://www.politico.eu/wp-content/uploads/2024/03/07/final-report-oc-2022-0514-redacted_final57.pdf
SRC-007 | ◈ | fam:E | EURLEX-1023-2013-ARTICLE16 | EUR-Lex — Regulation (EU, Euratom) 1023/2013, Article 16 Staff Regulations | 2013-10-29 | 2026-09-11T20:36:43Z | Article 16: two-year notification; conflict review; 12-month senior lobbying/advocacy prohibition in principle | https://eur-lex.europa.eu/eli/reg/2013/1023/oj/eng
SRC-008 | ◈ | fam:A | EO-OI-1-2021-KR | European Ombudsman — Decision OI/1/2021/KR on Commission revolving doors | 2022-05-16 | 2026-09-11T20:36:43Z | sample of 100 Commission decisions 2019-2021; approvals/restrictions; systemic recommendation | https://www.ombudsman.europa.eu/en/decision/en/155953
SRC-009 | ◈ | fam:C | HATVP-RA-2024-MOBILITES | HATVP — Rapport d’activité 2024, mobilités public-privé | 2025-05-26 | 2026-09-11T20:36:43Z | 751 mobility projects; 639 opinions; 95.5% compatibility; 74.3% with reservations; 4.5% incompatibility | https://www.hatvp.fr/presse/rapport-dactivite-2024-de-la-haute-autorite/
SRC-010 | ◈ | fam:A | EO-194-334-543-2017-EA | European Ombudsman — Recommendations on Barroso / Goldman Sachs and Ethics Committee | 2018-03-06 | 2026-09-11T20:36:43Z | Ethics Committee found insufficient grounds for violation; later Goldman-registered meeting prompted reassessment recommendation | https://www.ombudsman.europa.eu/ro/recommendation/en/90956

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.ombudsman.europa.eu/ga/recommendation/en/127638 | A | 2019-04-18/2019-08-02 | Farkas recruitment chronology | AFME recruitment began with a recruiter contact on 18 April 2019; interviews occurred in May, June and July; a job offer followed on 29 July and draft contract on 30 July; Farkas informed the EBA Chair on 1 August and formally resigned/requested authorisation on 2 August. | -
FCT-002 | FACT | ✧ | https://www.ombudsman.europa.eu/ga/recommendation/en/127638 | A | 2019-04-18/2019-08-26 | Farkas recusal during recruitment | The EBA confirmed that Farkas did not recuse himself from his responsibilities while the AFME recruitment process was ongoing and that he worked on issues later covered by restrictions, including the EU impact and implementation of finalised Basel III standards. | -
FCT-003 | FACT | ✧ | https://www.eba.europa.eu/publications-and-media/press-releases/adam-farkas-steps-down-eba-executive-director | B | 2019-09-12 | EBA restrictions on Farkas | The EBA removed Farkas from policy and supervisory work and imposed post-service restrictions including a 24-month lobbying/advocacy and professional-contact ban toward EBA and an 18-month restriction on AFME work directly linked to his last three years of EBA work. | -
FCT-004 | FACT | ✧ | https://www.eba.europa.eu/sites/default/files/document_library/About%20Us/Internal%20Organisation/Occupational%20activities%20after%20leaving%20the%20EBA/1025899/Senior%20Staff_2019%20AFME_Adam%20Farkas.pdf | B | 2019-09-12 | Farkas restrictions detailed scope | The detailed EBA assessment restricted access to policy/supervisory information and listed topics such as Basel III among areas from which Farkas was to be separated before departure and temporarily restricted after departure. | -
FCT-005 | FACT | ✧ | https://www.hatvp.fr/wordpress/wp-content/uploads/2022/05/2022-123-Jean-Baptiste-Djebbari.pdf | C | 2022-04-05 | Djebbari CMA CGM portfolio and contacts | HATVP found Djebbari’s transport responsibilities directly linked to CMA CGM activities and recorded at least eight meetings with the group’s CEO or senior executives during the preceding three years. | -
FCT-006 | FACT | ✧ | https://www.hatvp.fr/wordpress/wp-content/uploads/2022/05/2022-123-Jean-Baptiste-Djebbari.pdf | C | 2022-04-05 | Djebbari CMA CGM incompatibility | HATVP considered the ethical risk substantial and not neutralisable by reservations, and declared the proposed CMA CGM executive role incompatible with Djebbari’s government functions over the preceding three years. | -
FCT-007 | FACT | ✧ | https://www.hatvp.fr/wordpress/wp-content/uploads/2022/05/2022-104-Jean-Baptiste-Djebbari.pdf | C | 2022-03-22 | Djebbari Hopium negative control | For the Hopium board project, HATVP recorded two prior meetings with Hopium’s CEO, no public subsidy to Hopium, and no identified element casting doubt on how Djebbari had exercised his functions toward that company; it excluded the identified criminal-risk concern on the information available. | -
FCT-008 | FACT | ✧ | https://www.hatvp.fr/wordpress/wp-content/uploads/2022/05/2022-104-Jean-Baptiste-Djebbari.pdf | C | 2022-03-22 | Djebbari Hopium restrictions | HATVP approved the Hopium project with reservations barring Djebbari for three years from approaches, including interest representation, to specified former government colleagues, cabinet members and transport services. | -
FCT-009 | FACT | ✧ | https://www.politico.eu/wp-content/uploads/2024/03/07/final-report-oc-2022-0514-redacted_final57.pdf | D | 2014-09/2014-10 | Kroes Uber future cooperation approach | OLAF found evidence that Uber approached Neelie Kroes while she was still a Commissioner to discuss possible future cooperation, but found that she intended to postpone concrete discussion until after her mandate and found no evidence of concrete professional negotiation while she was in office. | -
FCT-010 | FACT | ✧ | https://www.politico.eu/wp-content/uploads/2024/03/07/final-report-oc-2022-0514-redacted_final57.pdf | D | 2010-2014 | Kroes Uber decision favouring | OLAF did not identify evidence that Kroes influenced Commission legislative processes in Uber’s favour or treated Uber differently from comparable economic operators while she was Commissioner. | -
FCT-011 | FACT | ✧ | https://www.politico.eu/wp-content/uploads/2024/03/07/final-report-oc-2022-0514-redacted_final57.pdf | D | 2015-09-22/2016-05-01 | Kroes cooling-off advisory role request | Kroes notified the Commission on 22 September 2015 that she wished to join an Uber advisory role; the Ethics Committee issued an unfavourable opinion, she withdrew the request in December 2015, and she joined Uber’s Public Policy Advisory Board after the cooling-off period in May 2016. | -
FCT-012 | FACT | ✧ | https://www.politico.eu/wp-content/uploads/2024/03/07/final-report-oc-2022-0514-redacted_final57.pdf | D | 2022-2023 | OLAF Kroes evidence-access limits | OLAF reported that Commission electronic data from Kroes’s time in office were no longer retained and that selective disclosure and withheld/redacted Uber records hampered a fully transparent and comprehensive reconstruction of events. | -
FCT-013 | FACT | ✧ | https://eur-lex.europa.eu/eli/reg/2013/1023/oj/eng | E | 2013-10-29 | EU Staff Regulations post-service rule | Article 16 requires officials to notify occupational activities undertaken within two years of leaving service; related activities that could conflict with institutional interests may be prohibited or conditioned, and former senior officials are in principle barred for 12 months from lobbying their former institution on matters they handled. | -
FCT-014 | FACT | ✧ | https://www.ombudsman.europa.eu/en/decision/en/155953 | A | 2019-2021 | Commission revolving-door sample | The European Ombudsman inspected 100 Commission decisions from 2019-2021 on post-service or outside activities and found that some senior-staff moves were approved despite reservations over whether restrictions could adequately mitigate conflict, knowledge or contact risks. | -
FCT-015 | FACT | ✧ | https://www.hatvp.fr/presse/rapport-dactivite-2024-de-la-haute-autorite/ | C | 2024 | HATVP mobility denominator | In 2024 HATVP received 751 mobility projects and issued 639 opinions; 95.5% were compatibility opinions, 74.3% with reservations, while incompatibility opinions represented 4.5% of the total. | -
FCT-016 | FACT | ✧ | https://www.ombudsman.europa.eu/ro/recommendation/en/90956 | A | 2016-2018 | Barroso Goldman Sachs governance control | The Commission Ethics Committee found insufficient grounds to establish a legal-obligation violation in Barroso’s Goldman Sachs employment; a later meeting registered as a Goldman Sachs meeting created the appearance of lobbying and led the Ombudsman to recommend reassessment. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-002
FCT-004 | SRC-003
FCT-005 | SRC-004
FCT-006 | SRC-004
FCT-007 | SRC-005
FCT-008 | SRC-005
FCT-009 | SRC-006
FCT-010 | SRC-006
FCT-011 | SRC-006
FCT-012 | SRC-006
FCT-013 | SRC-007
FCT-014 | SRC-008
FCT-015 | SRC-009
FCT-016 | SRC-010

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

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:CAUSAL
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:FINALIZE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-11T20:42:32.990116+00:00","fact_mem":{},"mnemo_row":"BLOCKED:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":16,"eligible":16,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:BLOCKED:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:16;attempted:0;success:0;failure:0;blocked:16} | WRITEBACK_EXECUTION_V1:[16 rows, see section]

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
