ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260911-1805-finance-opaque-beneficiaires-effectifs | PARENT_RUN_ID:NONE | AS_OF:2026-09-11
INPUT_KIND:RUN_CARD | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/audit121/INV149_TRANSACTION_2026-09-11/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-11_finance-opaque-beneficiaires-effectifs/2026-09-11_18-05_finance-opaque-beneficiaires-effectifs_INPUT.txt | SUBJECT_SLUG:finance-opaque-beneficiaires-effectifs | SUBJECT_FP:sha256:de94c260c3d202b06144da962fcc7fda115a178342ed6396fe934209187f8333 | INPUT_SHA256:sha256:0cdc49ecb8b4c999561eada7fa0ea6b00ea10e4fcf0ff6dfd424ceca0618ea9c
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/UE 2010-2026. Finance opaque, bénéficiaires effectifs, sociétés écrans, nominees, facilitateurs et conversion éventuelle en influence politique. Gardes: opacity != laundering; laundering != influence; beneficial owner != political principal; shell != illegality; facilitator != accomplice; foreign != interference; charge != final conviction.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-149 — Finance opaque, blanchiment et bénéficiaires effectifs comme infrastructure d’influence

## Objet

Cette enquête teste un maillon en amont d’INV-148 : identifier le principal réel derrière un flux politique ou économique. Une société écran, un prête-nom, un trust, un montage multi-couche ou un bénéficiaire effectif caché ne prouvent ni blanchiment ni ingérence. Ils deviennent politiquement pertinents lorsqu’ils cassent ou masquent la chaîne `origine des fonds -> contrôle réel -> véhicule -> paiement -> bénéficiaire/intermédiaire -> acte`.

## Résultat central

Le corpus public ferme une chaîne de principe et un contrôle positif fort. Le droit européen 2024 exige d’identifier la personne physique qui possède ou contrôle réellement une entité, y compris par d’autres moyens que la propriété formelle, et impose aux actionnaires/dirigeants mandataires de déclarer leur mandant et les bénéficiaires effectifs de celui-ci. Les entités étrangères sont également soumises à des obligations de transparence dans plusieurs situations d’accès économique à l’Union, dont certains marchés publics. La réforme française de 2026 organise l’accès au registre autour d’un intérêt légitime, tandis que la jurisprudence de la CJUE interdit d’assimiler transparence utile et accès public illimité.

Le point probatoire est donc : `LEGAL_HOLDER != BENEFICIAL_OWNER != NOMINATOR != POLITICAL_PRINCIPAL`. Un registre de bénéficiaires effectifs réduit l’opacité de propriété ; il ne démontre pas à lui seul qui a donné un ordre politique, ni pourquoi un paiement a été effectué.

## Le contrôle positif : la lessiveuse azerbaïdjanaise

Le dossier du Conseil de l’Europe fournit une chaîne rare où l’opacité financière rejoint effectivement une opération d’influence/corruption politique. Les rapports de l’Assemblée décrivent quatre sociétés écrans centrales enregistrées au Royaume-Uni avec bénéficiaires effectifs dissimulés, des fonds provenant notamment d’acteurs proches des plus hauts niveaux du pouvoir azerbaïdjanais, puis des virements vers des responsables ou structures liées à des membres de l’Assemblée parlementaire.

Le cas Luca Volontè ferme plusieurs maillons : plus de deux millions d’euros provenant de sources azerbaïdjanaises ont transité notamment par Metastar et Jetfield vers sa fondation et une société ; les échanges de courriels cités par le Conseil de l’Europe relient ces relations financières à des attentes de récompense autour d’actions parlementaires concernant l’Azerbaïdjan. Le cas Eduard Lintner ferme une autre route : des fonds provenant de la lessiveuse ont été reçus via Polux, Metastar, Hilux et Jetfield, puis utilisés dans un écosystème de lobbying et de relations politiques favorables à l’Azerbaïdjan.

Les jugements allemands récents renforcent sans rendre toutes les lignées indépendantes. En juillet 2025, l’OLG München a condamné Eduard Lintner pour corruption de mandataires dans un schéma où des fonds azerbaïdjanais alimentaient Line M-Trade, qui rémunérait Karin Strenz sous couvert d’un contrat de conseil en échange d’actions conformes aux intérêts azerbaïdjanais. En janvier 2026, le même tribunal a condamné Axel Fischer après avoir retenu une convention avec des représentants azerbaïdjanais, des paiements en espèces et des actes parlementaires favorables. Les deux jugements n’étaient pas encore définitifs dans les communiqués consultés ; ce statut est conservé.

La conclusion n’est pas `shell company = ingérence`. Elle est plus précise : une architecture opaque peut être une infrastructure d’attribution et de paiement qui permet de dissocier le principal réel du payeur apparent. Lorsque des pièces indépendantes reconnectent ensuite fonds, mandant, bénéficiaire politique et acte, l’opacité cesse d’être un simple risque abstrait et devient un élément du mécanisme.

## Structures légitimes et facilitateurs

Le GAFI rappelle que les véhicules juridiques et même certaines sociétés écrans ou nominee arrangements peuvent avoir des usages légitimes. La complexité juridique n’est donc pas une preuve de blanchiment. En revanche, les études FATF/Egmont montrent que sociétés écrans, prête-noms et structures multi-juridictionnelles sont fréquemment utilisés pour masquer la propriété réelle dans les cas analysés. Les professionnels d’intermédiation — avocats, comptables, prestataires de sociétés et fiducies, agents immobiliers — peuvent faciliter de tels montages, sciemment ou non. `FACILITATEUR != COMPLICE` reste une garde obligatoire.

Tracfin fournit un contrôle négatif important : les sociétés dites « taxis » et autres structures éphémères peuvent blanchir des flux criminels à grande échelle sans aucun effet politique. Le blanchiment est donc une infrastructure financière possible ; le passage vers influence, corruption ou ingérence exige toujours un bénéficiaire politique, une relation, une action et un effet ou une contrepartie distinctement établis.

## Limites de la transparence

La CJUE a invalidé en 2022 l’accès général et inconditionnel du public aux informations sur les bénéficiaires effectifs en raison de l’atteinte aux droits au respect de la vie privée et à la protection des données. Le nouveau cadre français de 2026 repose sur l’intérêt légitime et prévoit des motifs de refus. La capacité d’enquête n’est donc pas égale à un registre universellement ouvert. Cette limite crée un gap de vérifiabilité publique : certaines chaînes peuvent être accessibles aux autorités ou aux entités assujetties mais rester difficiles à reconstruire depuis des sources ouvertes.

## Verdict causal

Le mécanisme robuste est :

`origine économique -> structure juridique / nominee -> contrôle ou bénéficiaire effectif -> banque / professionnel facilitateur -> paiement / actif / contrat -> bénéficiaire ou intermédiaire politique -> acte -> effet`.

Chaque flèche doit être prouvée séparément. `BENEFICIAL_OWNER != COMMANDITAIRE`, `SHELL != BLANCHIMENT`, `BLANCHIMENT != INFLUENCE`, `FACILITATEUR != COMPLICE`, `ORIGINE_ETRANGERE != INGERENCE`.

INV-149 ferme toutefois un vrai trou du corpus : l’opacité financière n’est pas seulement un problème AML ; dans certains cas documentés, elle est une technologie de séparation entre le principal économique et l’action politique financée.

## Gap restant

Le run ne fournit pas de dénominateur permettant d’estimer la fréquence des chaînes `finance opaque -> influence politique` en France/UE. Il ne permet pas non plus de déduire, à partir d’un bénéficiaire effectif identifié, le commanditaire politique d’un paiement. Ces deux arêtes restent explicitement ouvertes.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:0|EDI_DECISIVE:6|SRC_COMPLETE:12/12

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-11
- **breaks:**
  - 2022 CJEU BO public-access judgment
  - 2024 EU AMLR
  - 2025 Lintner first-instance judgment
  - 2026 Fischer first-instance judgment
  - 2026 French BO-access decree
- **status:** CURRENT
- **window:** France/UE principalement 2010-2026; comparateurs PACE/Allemagne

### MANIPULATION_REPORT
- **assumptions:**
  - classification follows proved control/transfer/action edges, not opacity alone
- **clusters:**
  - MONEY
  - NETWORK
  - POWER
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - political bridge requires evidence beyond AML opacity
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - legal-holder/beneficial-owner conflation
  - shell=crime shortcut
  - laundering=influence shortcut
  - gatekeeper=accomplice shortcut
  - foreign-origin shortcut
  - case-to-prevalence extrapolation
- **priorities:**
  - primary AML/BO law
  - judicial/institutional findings
  - opaque-finance positive control
  - negative controls
  - procedural status
- **query_guidance:** trace source/control through vehicle and transfer to political actor and act; preserve legitimacy and prevalence limits
- **rhetorical:**
  - NONE
- **speaker:** mechanism-first forensic investigation contract
- **symbol_stage:** FINAL
- **symbols:**
  - **ACT:** observable political/parliamentary action
  - **ACTOR:** person/entity acting
  - **BANK:** payment/correspondent institution
  - **BENEFICIAL_OWNER:** natural person ultimately owning or controlling
  - **DECISION:** institutional outcome sought
  - **EFFECT:** downstream outcome distinct from transfer
  - **FACILITATOR:** professional intermediary enabling structure or transfer
  - **GAP:** typed unresolved evidence edge
  - **INTERMEDIARY:** bridge between funds and decision arena
  - **LEGAL_HOLDER:** formal owner/holder
  - **NOMINATOR:** person instructing nominee
  - **PAYMENT:** value transfer
  - **POLITICAL_BENEFICIARY:** political actor or structure receiving value
  - **PRINCIPAL:** economic or political interest behind action
  - **VEHICLE:** legal entity/arrangement or shell
- **threats:**
  - beneficiary=author
  - opacity=wrongdoing
  - BO=political principal
  - suspicious report=crime
  - judgment without finality qualifier
  - not found=does not exist

### MODULE_EXECUTION
NONE

### SCOPING_REPORT
- **chain:**
  - economic origin
  - vehicle/shell/nominee
  - beneficial owner/control
  - bank/facilitator
  - payment/asset/contract
  - political beneficiary/intermediary
  - act
  - decision/effect
- **exclusions:**
  - opacity alone
  - ordinary legitimate shell/nominee use
  - generic AML suspicion without political bridge
  - beneficial owner automatically treated as commanditaire
- **object:** Finance opaque, blanchiment et bénéficiaires effectifs comme infrastructure d influence
- **scope:** France/UE 2010-2026; PACE/Azerbaijan and German adjudication as mechanism controls

### CREDO
- legal holder != beneficial owner != nominator != political principal
- shell != laundering
- laundering != influence
- facilitator != accomplice
- beneficial owner != commanditaire
- foreign != ingérence
- case existence != prevalence
- not found != does not exist

### COGNITIVE_MAP
- **causal_boundary:** opacity is enabling infrastructure; political influence requires a separately evidenced bridge to actor and act
- **core_model:** opaque finance can become attribution-separation infrastructure when source/control, transfer, political beneficiary and act are independently reconnected
- **rival_models:**
  - legitimate corporate structuring
  - ordinary criminal laundering without political object
  - professional facilitation without knowing participation
  - transparent political finance
  - direct bribery without ownership concealment
- **serial_edges:**
  - origin/control
  - vehicle/nominee
  - transfer/facilitator
  - political recipient/intermediary
  - act/decision

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** legal structures and nominee arrangements can be legitimate and BO does not identify political tasking
  - **resolution:** require independent evidence reconnecting control, funds, recipient and political act
  - **thesis:** opaque structure proves hidden political principal
- **item 2:**
  - **antithesis:** Tracfin/FATF show laundering can be purely criminal/economic
  - **resolution:** political bridge is a distinct evidentiary edge
  - **thesis:** laundering evidence proves influence

### RESOURCE_FLOW_MAP
- **item 1:**
  - **case:** Azerbaijani Laundromat/PACE
  - **flow:** Azerbaijani-linked funds -> UK shell vehicles/banks -> political actors/structures -> Azerbaijan-favourable parliamentary activity
  - **status:** SUPPORTED_POSITIVE_CONTROL
  - **support:**
    - FCT-011
    - FCT-012
    - FCT-013
    - FCT-014
- **item 2:**
  - **case:** Lintner/Strenz
  - **flow:** Azerbaijani funds -> Line M / sham consultancy -> parliamentarian -> Azerbaijan-favourable conduct
  - **status:** FIRST_INSTANCE_NOT_FINAL
  - **support:**
    - FCT-015
- **item 3:**
  - **case:** Tracfin corporate misuse
  - **flow:** suspect corporate structures -> AML reporting/registry action
  - **status:** NEGATIVE_CONTROL_NO_POLITICAL_BRIDGE
  - **support:**
    - FCT-010

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** economic source/principal
  - **relation:** ownership/control/funding
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-006
  - **to:** vehicle/nominee
- **item 2:**
  - **from:** vehicle/bank
  - **relation:** transfer
  - **support:**
    - FCT-011
    - FCT-012
    - FCT-013
    - FCT-015
  - **to:** political beneficiary/intermediary
- **item 3:**
  - **from:** political beneficiary/intermediary
  - **relation:** speech/vote/report/election observation
  - **support:**
    - FCT-013
    - FCT-014
    - FCT-015
    - FCT-016
  - **to:** institutional process

### IMPACT_MAP
- **downstream:** elevates strategic ownership/control as next discriminant for INV-150
- **measured_objects:**
  - ownership/control transparency
  - concealment mechanisms
  - cross-border transfer chains
  - political recipient/action links
  - procedural/judicial status
- **not_established:**
  - France/EU prevalence
  - BO=political principal
  - all shell/nominee arrangements illicit
  - general democratic outcome effect

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** FATF explicitly recognizes legitimate uses
  - **issue:** shell/nominee = illicit concealment
  - **pro:** FATF cases show frequent abuse for BO concealment
  - **resolution:** STRUCTURE_IS_RISK_SIGNAL_NOT_WRONGDOING
- **item 2:**
  - **contra:** CJEU found unconditional general-public access disproportionate to privacy/data rights
  - **issue:** BO transparency should be universal public access
  - **pro:** transparency helps attribution/accountability
  - **resolution:** ACCESS_MUST_BE_PURPOSE_AND_RIGHTS_CALIBRATED

### VERIFICATION_REPORT
- **checks:**
  - AMLR BO/control definitions checked
  - nominee disclosure checked
  - CJEU public-access limit preserved
  - French 2026 access regime bounded temporally
  - FATF legitimate-use caveat preserved
  - PACE Laundromat political bridge separated from prevalence
  - Munich judgments marked non-final where source says so
  - Tracfin statistics not promoted to political influence prevalence
- **status:** PASS_WITH_EXPLICIT_GAP

### EDI_REPORT
- **corpus:** 12 accepted sources across 3 provenance families; PACE/Laundromat materials form a partially dependent case lineage
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim:** CLM-001
    - **families:**
      - A
  - **item 2:**
    - **claim:** CLM-002
    - **families:**
      - A
      - B
  - **item 3:**
    - **claim:** CLM-003
    - **families:**
      - A
      - B
  - **item 4:**
    - **claim:** CLM-004
    - **families:**
      - A
      - B
  - **item 5:**
    - **claim:** CLM-005
    - **families:**
      - A
  - **item 6:**
    - **claim:** CLM-006
    - **families:**
      - A
      - B
- **diagnostic_not_truth:** true
- **dimensions:**
  - EU AMLR
  - French BO access
  - CJEU privacy limit
  - FATF BO concealment
  - FATF gatekeepers
  - Tracfin corporate misuse
  - PACE Azerbaijani Laundromat
  - German first-instance adjudication
- **edi:** PRIMARY_OFFICIAL_DOMINANT_WITH_ONE_INSTITUTIONAL_CASE_SYNTHESIS
- **source_counts:**
  - **A:** 8
  - **B:** 3
  - **C:** 1

### RESPONSIBILITY_MAP
- **item 1:**
  - **claim:** BO/control legal definitions
  - **owner:** EU legislature/French implementation
  - **status:** ESTABLISHED
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
- **item 2:**
  - **claim:** Azerbaijani Laundromat shell/payment chain
  - **owner:** PACE institutional inquiry/public records
  - **status:** SUPPORTED_CASE
  - **support:**
    - FCT-011
    - FCT-012
    - FCT-013
    - FCT-014
- **item 3:**
  - **claim:** Lintner/Fischer criminal findings
  - **owner:** OLG Munich
  - **status:** FIRST_INSTANCE_NON_FINAL
  - **support:**
    - FCT-015
    - FCT-016

### NEXT_QUERIES
- **item 1:**
  - **query:** strategic foreign ownership/acquisition -> control rights -> exercised leverage over French/EU strategic asset
  - **route:** NEW_INVESTIGATION
  - **trigger:** INV-150
- **item 2:**
  - **query:** representative prevalence of opaque-finance political influence chains in France/EU
  - **route:** RECHECK
  - **trigger:** denominator dataset becomes available
- **item 3:**
  - **query:** BO identified -> political commanditaire
  - **route:** RECHECK
  - **trigger:** independent tasking/control evidence

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012 | support:- | counter:- | results:FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016 | final:GAP | gap:SCOPE
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-017 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012 | support:- | counter:- | results:FCT-006,FCT-007,FCT-008,FCT-009,FCT-010 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012 | support:- | counter:- | results:FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012 | support:- | counter:- | results:FCT-010,FCT-011,FCT-014 | final:GAP | gap:SCOPE
CLM-001 | attempts:QRY-001,QRY-012,SRC-001,SRC-012 | support:FCT-001,FCT-002,FCT-003,FCT-017 | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-017 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-004,QRY-005,SRC-004,SRC-005 | support:FCT-006,FCT-007,FCT-008 | counter:- | results:FCT-006,FCT-007,FCT-008 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-006,SRC-006 | support:FCT-009 | counter:- | results:FCT-009 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-008,QRY-009,SRC-008,SRC-009 | support:FCT-011,FCT-012,FCT-013,FCT-014 | counter:- | results:FCT-011,FCT-012,FCT-013,FCT-014 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-010,QRY-011,SRC-010,SRC-011 | support:FCT-015,FCT-016 | counter:- | results:FCT-015,FCT-016 | final:SUPPORTED | gap:NONE
CLM-006 | attempts:QRY-005,QRY-007,SRC-005,SRC-007 | support:FCT-007,FCT-010 | counter:FCT-007,FCT-010 | results:FCT-007,FCT-010,FCT-007,FCT-010 | final:REFUTED | gap:NONE
CLM-007 | attempts:QRY-001,QRY-005,QRY-007,SRC-001,SRC-005,SRC-007 | support:FCT-001,FCT-002 | counter:FCT-007,FCT-010 | results:FCT-001,FCT-002,FCT-007,FCT-010 | final:REFUTED | gap:NONE
CLM-008 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012 | support:- | counter:- | results:- | final:GAP | gap:SCOPE

## STATUS_DELTA_V1
DELTA-001 | CAU-001 | SUPPORTED_WITH_LIMIT | SUPPORTED | Normalize terminal CAU status to kernel contract while preserving bounded causal limit.

## OPEN_GAPS_V1
AXS-004 | AXS | GAP | SCOPE | No representative denominator.
CLM-008 | CLM | GAP | SCOPE | No representative denominator; case existence cannot be promoted to frequency.
CAU-001 | CAU | SUPPORTED | CAUSALITY | Prevalence and marginal political effect are not measured.

SEMANTIC_COUNTS_V1:LED:2|CLM:8|AXS:4|CAU:1|CTRL:7|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012"],"evidence_excerpt":"Trace origin -> vehicle/nominee -> beneficial owner/facilitator -> payment -> political intermediary -> act/effect.","kind":"HYPOTHESIS","lead":"Financial opacity can separate the legal payer/holder from the real controlling principal and can become part of a political influence chain when independent evidence reconnects source of funds, intermediary/beneficiary and political act.","linked_ids":["CLM-001","CLM-004"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017"],"routes":["MONEY","NETWORK","POWER"],"source_id":"INV-149-RUN_CARD","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012"],"evidence_excerpt":"Case evidence closes existence, not prevalence.","gap":"No representative denominator permits prevalence estimation; beneficial-owner identification also does not identify political command by itself.","gap_type":"SCOPE","kind":"GAP","lead":"Population denominator for opaque-finance-to-political-influence chains in France/EU.","linked_ids":["CLM-008"],"locator":"GAP","materiality":"HIGH","result_ids":["FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016"],"routes":["RECHECK"],"source_id":"INV-149-RUN_CARD","status":"GAP"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Legal ownership, beneficial ownership, nominator and political principal are distinct objects; none can be substituted for another without evidence.","claimant":"INV-149 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-017"]}
CLM-002 | {"claim":"Shell companies and nominee arrangements can conceal beneficial ownership but are not inherently illicit.","claimant":"INV-149 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-006","FCT-007","FCT-008"]}
CLM-003 | {"claim":"Professional gatekeepers may facilitate concealment or laundering wittingly or unwittingly; professional involvement alone does not establish complicity.","claimant":"INV-149 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-009"]}
CLM-004 | {"claim":"The Azerbaijani Laundromat provides a documented chain from concealed corporate vehicles and cross-border banking to payments reaching political actors/structures and Azerbaijan-favourable political activity in PACE.","claimant":"INV-149 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-011","FCT-012","FCT-013","FCT-014"]}
CLM-005 | {"claim":"Recent Munich judgments provide adjudicated controls that Azerbaijani payments were exchanged for pro-Azerbaijan parliamentary conduct, but the releases consulted stated the judgments were not final.","claimant":"INV-149 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-015","FCT-016"]}
CLM-006 | {"claim":"Money laundering or suspicious corporate structures alone establish political influence.","claimant":"INV-149 synthesis","counter":["FCT-007","FCT-010"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"REFUTED","support":["FCT-007","FCT-010"]}
CLM-007 | {"claim":"Identification of a beneficial owner is sufficient to identify a political commanditaire.","claimant":"INV-149 synthesis","counter":["FCT-007","FCT-010"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"REFUTED","support":["FCT-001","FCT-002"]}
CLM-008 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012"],"claim":"This run establishes a representative prevalence rate for opaque-finance political influence in France/EU.","claimant":"INV-149 synthesis","counter":"NONE_FOUND","gap":"No representative denominator; case existence cannot be promoted to frequency.","gap_type":"SCOPE","materiality":"HIGH","status":"GAP","support":"NONE_FOUND"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012"],"axis":"OWNERSHIP_CONTROL","links":["CLM-001","CLM-007"],"question":"How are legal holder, beneficial owner, nominator and controller separated?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-017"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012"],"axis":"CONCEALMENT_INFRASTRUCTURE","links":["CLM-002","CLM-003"],"question":"Can shells/nominees/professionals conceal source/control without implying illegality?","result_ids":["FCT-006","FCT-007","FCT-008","FCT-009","FCT-010"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012"],"axis":"POLITICAL_BRIDGE","links":["CLM-004","CLM-005"],"question":"Is there a documented chain from opaque finance to political actors and acts?","result_ids":["FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012"],"axis":"PREVALENCE","gap":"No representative denominator.","gap_type":"SCOPE","links":["CLM-008"],"question":"How common are such political chains?","result_ids":["FCT-010","FCT-011","FCT-014"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"GAP"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"Opaque finance is causally relevant only where independent evidence reconnects source/control, transfer, political beneficiary/intermediary, and act; it does not by itself establish prevalence or command.","counter":"FATF/Tracfin show opaque or suspect structures can exist in ordinary criminal laundering without political action; legitimate shell/nominee uses also exist.","gap":"Prevalence and marginal political effect are not measured.","gap_type":"CAUSALITY","limit":"The political bridge requires separate evidence linking money to actor, relationship and act; BO alone does not prove command.","mechanism":"source funds -> legal vehicle/nominee -> real control/beneficial owner -> bank/facilitator -> payment -> political beneficiary/intermediary -> act","question":"When does opacity become part of an influence mechanism rather than merely an AML risk?","status":"SUPPORTED","support":["FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"shell company != laundering","status":"PASS","support":["FCT-007"]}
CTRL-002 | {"control":"laundering != political influence","status":"PASS","support":["FCT-010"]}
CTRL-003 | {"control":"beneficial owner != political principal/commanditaire","status":"PASS","support":["FCT-001","FCT-002"]}
CTRL-004 | {"control":"facilitator != accomplice","status":"PASS","support":["FCT-009"]}
CTRL-005 | {"control":"foreign origin != interference","status":"PASS","support":["FCT-011"]}
CTRL-006 | {"control":"charge or first-instance conviction != final judgment","status":"PASS","support":["FCT-015","FCT-016"]}
CTRL-007 | {"control":"public-access restriction != absence of official beneficial-ownership information","status":"PASS","support":["FCT-004","FCT-005"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:12|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"EMPTY","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | MNEMO_UNAVAILABLE | mnemo | NONE | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://eur-lex.europa.eu/eli/reg/2024/1624/oj/eng | -
QRY-002 | FETCH | FOUND | SRC-002 | https://www.legifrance.gouv.fr/eli/decret/2026/4/24/2026-310/jo/texte | -
QRY-003 | FETCH | FOUND | SRC-003 | https://infocuria.curia.europa.eu/tabs/redirect/juris/liste.jsf?num=C-37%2F20 | -
QRY-004 | FETCH | FOUND | SRC-004 | https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-Beneficial-Ownership-Legal-Persons.html | -
QRY-005 | FETCH | FOUND | SRC-005 | https://www.fatf-gafi.org/content/dam/fatf/documents/reports/FATF-Egmont-Concealment-beneficial-ownership.pdf | -
QRY-006 | FETCH | FOUND | SRC-006 | https://www.fatf-gafi.org/content/fatf-gafi/en/publications/Fatfgeneral/Gatekeeper-TC-Corruption.html | -
QRY-007 | FETCH | FOUND | SRC-007 | https://www.economie.gouv.fr/tracfin/tracfin-publie-son-rapport-dactivite-et-dimpact-2025 | -
QRY-008 | FETCH | FOUND | SRC-008 | https://pace.coe.int/en/files/27474/html | -
QRY-009 | FETCH | FOUND | SRC-009 | https://pace.coe.int/en/files/29559/html | -
QRY-010 | FETCH | FOUND | SRC-010 | https://www.justiz.bayern.de/gerichte-und-behoerden/oberlandesgerichte/muenchen/presse/2025/49.php | -
QRY-011 | FETCH | FOUND | SRC-011 | https://www.justiz.bayern.de/gerichte-und-behoerden/oberlandesgerichte/muenchen/presse/2026/6.php | -
QRY-012 | FETCH | FOUND | SRC-012 | https://www.economie.gouv.fr/tracfin/les-obligations-de-vigilance | -

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | EU-AMLR-2024 | Regulation (EU) 2024/1624 — beneficial ownership transparency | 2024-06-19 | 2026-09-11T16:05:00Z | Articles 51-67: ownership/control, nominees, foreign entities | https://eur-lex.europa.eu/eli/reg/2024/1624/oj/eng
SRC-002 | ◈ | fam:A | FR-BO-ACCESS-2026 | Décret n° 2026-310 — accès registre bénéficiaires effectifs | 2026-04-25 | 2026-09-11T16:05:00Z | intérêt légitime, procédure et refus d’accès | https://www.legifrance.gouv.fr/eli/decret/2026/4/24/2026-310/jo/texte
SRC-003 | ◈ | fam:A | CJEU-LBR-2022 | CJUE — Luxembourg Business Registers C-37/20 C-601/20 | 2022-11-22 | 2026-09-11T16:05:00Z | invalidité de l’accès public général aux données BO | https://infocuria.curia.europa.eu/tabs/redirect/juris/liste.jsf?num=C-37%2F20
SRC-004 | ◈ | fam:B | FATF-BO-LP-2023 | FATF — Guidance on Beneficial Ownership of Legal Persons | 2023-03-10 | 2026-09-11T16:05:00Z | true owners, anonymous shell companies, nominee arrangements | https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-Beneficial-Ownership-Legal-Persons.html
SRC-005 | ◈ | fam:B | FATF-EGMONT-BO | FATF/Egmont — Concealment of Beneficial Ownership | 2018-07-18 | 2026-09-11T16:05:00Z | 106 cases; shell companies and professional intermediaries | https://www.fatf-gafi.org/content/dam/fatf/documents/reports/FATF-Egmont-Concealment-beneficial-ownership.pdf
SRC-006 | ◈ | fam:B | FATF-GATEKEEPERS-2024 | FATF — Horizontal Review of Gatekeepers related to Corruption | 2024-07-08 | 2026-09-11T16:05:00Z | lawyers, accountants, TCSPs, real estate agents as gatekeepers | https://www.fatf-gafi.org/content/fatf-gafi/en/publications/Fatfgeneral/Gatekeeper-TC-Corruption.html
SRC-007 | ◈ | fam:B | TRACFIN-2025 | Tracfin — rapport activité et impact 2025 | 2026-08-27 | 2026-09-11T16:05:00Z | 8,000 sociétés signalées; blanchiment; contrôles négatifs | https://www.economie.gouv.fr/tracfin/tracfin-publie-son-rapport-dactivite-et-dimpact-2025
SRC-008 | ◈ | fam:C | PACE-LAUNDROMATS-2019 | PACE — Laundromats report Doc. 14847 | 2019-03-25 | 2026-09-11T16:05:00Z | Azerbaijani Laundromat, shells, ownership opacity, political recipients | https://pace.coe.int/en/files/27474/html
SRC-009 | ◈ | fam:C | PACE-CORRUPTION-2021 | PACE — report Doc. 15403 | 2021-12-15 | 2026-09-11T16:05:00Z | laundromat funding contributed to corruptive activities in Assembly | https://pace.coe.int/en/files/29559/html
SRC-010 | ◈ | fam:C | OLG-LINTNER-2025 | OLG München — Eduard L. conviction | 2025-07-30 | 2026-09-11T16:05:00Z | Azerbaijan-funded Line M-Trade, Strenz payments and acts | https://www.justiz.bayern.de/gerichte-und-behoerden/oberlandesgerichte/muenchen/presse/2025/49.php
SRC-011 | ◈ | fam:C | OLG-FISCHER-2026 | OLG München — Axel F. conviction | 2026-01-22 | 2026-09-11T16:05:00Z | cash payments linked to PACE speeches/documents/votes | https://www.justiz.bayern.de/gerichte-und-behoerden/oberlandesgerichte/muenchen/presse/2026/6.php
SRC-012 | ◈ | fam:B | TRACFIN-VIGILANCE | Tracfin — obligations de vigilance | 2026-09-11 | 2026-09-11T16:05:00Z | CDD includes beneficial owners | https://www.economie.gouv.fr/tracfin/les-obligations-de-vigilance

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://eur-lex.europa.eu/eli/reg/2024/1624/oj/eng | A | 2024-06-19 | Beneficial owner definition | EU AMLR defines beneficial owners as natural persons owning or controlling a legal entity directly or indirectly; control through other means is assessed independently of ownership interest. | -
FCT-002 | FACT | ✧ | https://eur-lex.europa.eu/eli/reg/2024/1624/oj/eng | A | 2024-06-19 | Nominee transparency | EU AMLR Article 66 requires nominee shareholders/directors to identify their nominator and the nominator beneficial owners and report that information to the entity/central register. | -
FCT-003 | FACT | ✧ | https://eur-lex.europa.eu/eli/reg/2024/1624/oj/eng | A | 2024-06-19 | Foreign entity BO disclosure | EU AMLR Article 67 requires certain foreign legal entities/arrangements to disclose beneficial ownership when entering specified EU relationships, including certain public procurement awards. | -
FCT-004 | FACT | ✧ | https://www.legifrance.gouv.fr/eli/decret/2026/4/24/2026-310/jo/texte | A | 2026-04-25 | French register access | France 2026 BO-register access requires a legitimate-interest assessment for relevant private/public applicants and allows refusal on enumerated grounds. | -
FCT-005 | FACT | ✧ | https://infocuria.curia.europa.eu/tabs/redirect/juris/liste.jsf?num=C-37%2F20 | A | 2022-11-22 | Public-access limit | CJEU invalidated unconditional access by any member of the general public to beneficial-ownership information under the prior AML directive because of serious interference with privacy/data-protection rights. | -
FCT-006 | FACT | ✧ | https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-Beneficial-Ownership-Legal-Persons.html | B | 2023-03-10 | Shell/nominee risk | FATF strengthened standards so authorities can access adequate, accurate and up-to-date information on true owners and explicitly targets abuse of anonymous shell companies. | -
FCT-007 | FACT | ✧ | https://www.fatf-gafi.org/content/dam/fatf/documents/reports/FATF-Egmont-Concealment-beneficial-ownership.pdf | B | 2018-07-18 | Legitimate shell uses | FATF/Egmont notes shell companies can have legitimate purposes; shell-company status alone does not establish illicit activity. | -
FCT-008 | FACT | ✧ | https://www.fatf-gafi.org/content/dam/fatf/documents/reports/FATF-Egmont-Concealment-beneficial-ownership.pdf | B | 2018-07-18 | Concealment pattern | In FATF/Egmont case studies, legal persons—especially shell companies—were a key feature of schemes used to disguise beneficial ownership, often across multiple jurisdictions. | -
FCT-009 | FACT | ✧ | https://www.fatf-gafi.org/content/fatf-gafi/en/publications/Fatfgeneral/Gatekeeper-TC-Corruption.html | B | 2024-07-08 | Gatekeeper risk | FATF states lawyers, accountants, trust/company service providers and real-estate agents can facilitate high-level corruption and laundering wittingly or unwittingly. | -
FCT-010 | FACT | ✧ | https://www.economie.gouv.fr/tracfin/tracfin-publie-son-rapport-dactivite-et-dimpact-2025 | B | 2026-08-27 | Generic laundering control | Tracfin 2025 reported more than 8,000 companies to commercial registries, 80% of which were struck off; this demonstrates large-scale suspect corporate misuse but does not establish political influence. | -
FCT-011 | FACT | ✧ | https://pace.coe.int/en/files/27474/html | C | 2019-03-25 | Azerbaijani Laundromat structure | PACE describes four core UK shell companies with concealed beneficial ownership used in the Azerbaijani Laundromat, with funds linked to persons close to the highest levels of Azerbaijani power. | -
FCT-012 | FACT | ✧ | https://pace.coe.int/en/files/27474/html | C | 2019-03-25 | Volonte flow | PACE reports that more than EUR 2 million from Azerbaijani sources reached Luca Volontè through Laundromat-linked companies and banks into his foundation/company, alongside communications concerning rewards and Azerbaijan-related parliamentary activity. | -
FCT-013 | FACT | ✧ | https://pace.coe.int/en/files/27474/html | C | 2019-03-25 | Lintner flow | PACE reports Eduard Lintner received hundreds of thousands of euros via Laundromat companies and organised Azerbaijan-related lobbying/election-observation activity; the report also traces payments to other PACE members. | -
FCT-014 | FACT | ✧ | https://pace.coe.int/en/files/29559/html | C | 2021-12-15 | Political-corruption bridge | PACE later stated that the Azerbaijani Laundromat provided money contributing to corruptive activities within the Assembly and that multiple former members were sanctioned for ethical breaches. | -
FCT-015 | FACT | ✧ | https://www.justiz.bayern.de/gerichte-und-behoerden/oberlandesgerichte/muenchen/presse/2025/49.php | C | 2025-07-30 | Lintner conviction status | OLG München convicted Eduard L. in July 2025 for bribery of office holders: Azerbaijani funds were provided to Line M-Trade, which paid Karin Strenz under a sham consulting arrangement in exchange for pro-Azerbaijan activity; judgment was not final in the release. | -
FCT-016 | FACT | ✧ | https://www.justiz.bayern.de/gerichte-und-behoerden/oberlandesgerichte/muenchen/presse/2026/6.php | C | 2026-01-22 | Fischer conviction status | OLG München convicted Axel F. in January 2026 after finding an agreement with Azerbaijani representatives involving cash payments and pro-Azerbaijan PACE acts; judgment was not final in the release. | -
FCT-017 | FACT | ✧ | https://www.economie.gouv.fr/tracfin/les-obligations-de-vigilance | B | 2026-09-11 | CDD beneficial owners | Tracfin states obliged professionals must exercise vigilance over clients and the beneficial owners of operations/business relationships. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-002
FCT-005 | SRC-003
FCT-006 | SRC-004
FCT-007 | SRC-005
FCT-008 | SRC-005
FCT-009 | SRC-006
FCT-010 | SRC-007
FCT-011 | SRC-008
FCT-012 | SRC-008
FCT-013 | SRC-008
FCT-014 | SRC-009
FCT-015 | SRC-010
FCT-016 | SRC-011
FCT-017 | SRC-012

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

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:SEARCH
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:FACTS
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:CAUSAL_GAP
CP-004 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 | NEXT_ACTION:VERIFY
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:INVESTIGATION_ACCOUNTABILITY
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:FINALIZE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-11T16:19:34.776454+00:00","fact_mem":{},"mnemo_row":"MNEMO_UNAVAILABLE — local memory service not available; no memory ids fabricated.","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":17,"eligible":17,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_UNAVAILABLE — local memory service not available; no memory ids fabricated. | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:17;attempted:0;success:0;failure:0;blocked:17} | WRITEBACK_EXECUTION_V1:[17 rows, see section]

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
