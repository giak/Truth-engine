ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260911-1828-investissements-strategiques-controle | PARENT_RUN_ID:NONE | AS_OF:2026-09-11
INPUT_KIND:RUN_CARD | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/audit121/INV150_TRANSACTION_2026-09-11/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-11_investissements-strategiques-controle/2026-09-11_18-28_investissements-strategiques-controle_INPUT.txt | SUBJECT_SLUG:investissements-strategiques-controle | SUBJECT_FP:sha256:878b05248345b8bbb3e24ab48f59f1251a9d2de6e9d653be3c55e2caaa533288 | INPUT_SHA256:sha256:fd391a50e4c8dcdebab4fcce31af6a12848060644659cae1eb2ce23dd4b036c0
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/UE principalement 2016-2026; comparateurs UK/Norvège bornés. Trace principal/État lié -> investisseur/fonds -> acquisition -> droits de contrôle -> actif stratégique -> exercice/menace du levier -> adaptation/décision -> effet.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-150 — Investissements stratégiques, acquisitions et fonds souverains

## Verdict exécutif

Le corpus ferme un mécanisme plus précis que « propriété étrangère = ingérence ». Une acquisition ou une prise de participation devient matériellement pertinente lorsque l'investisseur obtient des **droits de contrôle ou de gouvernance** sur un actif stratégique : droits de vote, accès au conseil, veto, information, nomination, contrôle opérationnel, ou capacité de modifier la continuité d'une activité. Ces droits peuvent ensuite être neutralisés, conditionnés, refusés ou, dans certains cas, exercés. Mais la possession de ces droits ne démontre pas à elle seule une coercition politique ni un tasking étatique.

Le nouveau règlement (UE) 2026/1386 formalise exactement cette distinction. Il vise les investissements permettant une participation effective à la gestion ou au contrôle d'une cible européenne, étend le filtrage aux filiales européennes contrôlées par un investisseur étranger et demande d'examiner notamment le bénéficiaire effectif, les structures opaques, le financement étatique, les droits spéciaux et les administrateurs nommés par un gouvernement tiers. Il autorise le filtrage à conduire à des mesures d'atténuation, une interdiction ou un démantèlement. Le règlement va jusqu'à demander si l'investissement peut être utilisé pour **contraindre** un État membre ou l'Union à modifier, adopter ou abandonner un acte. Cette possibilité est un critère de risque ; elle n'est pas une preuve que chaque investissement lié à un État est coercitif.

## 1. France : le filtrage produit des effets matériels avant toute coercition

Le régime français IEF distingue acquisition de contrôle, acquisition de branche et certains franchissements de seuils de droits de vote dans les activités sensibles. Le ministre peut autoriser, autoriser sous conditions ou refuser. Le régime suit la chaîne de contrôle de l'investisseur et peut prendre en compte ses liens avec un gouvernement étranger. En 2024, 182 décisions portaient sur des opérations éligibles et 99 autorisations ont été assorties de conditions ; le ministère indique aussi six refus sur les trois années précédentes. Cela prouve que le filtrage n'est pas seulement déclaratif : il modifie effectivement les droits attachés à des opérations. Cela ne prouve pas que les investisseurs concernés poursuivaient une intention hostile.

Photonis fournit un contrôle positif net. Le projet de rachat par Teledyne a été instruit au titre des IEF ; le Gouvernement a posé des conditions, puis a finalement décidé de ne pas autoriser le rachat et de privilégier une solution nationale en raison du caractère stratégique des technologies de Photonis pour la défense. La chaîne fermée est donc `acquisition envisagée -> contrôle IEF -> risque stratégique identifié -> non-autorisation -> solution nationale`. Elle ferme l'effet du filtrage sur la propriété future de l'actif. Elle ne ferme pas `Teledyne -> objectif de coercition politique`.

Les Chantiers de l'Atlantique fournissent un mécanisme différent. En 2017, l'État français a exercé son droit de préemption sur les titres destinés à Fincantieri afin de renégocier un tour de table et des droits de gouvernance protecteurs. L'accord projeté prévoyait 50 % pour Fincantieri, 1 % prêté par l'État sous engagements, et le maintien d'une minorité de blocage française. La preuve porte ici sur le fait que la **structure de propriété et les droits de gouvernance sont eux-mêmes des objets de souveraineté négociés**. L'opération projetée n'autorise pas à conclure que Fincantieri aurait exercé un levier hostile ; elle montre que les droits de contrôle étaient suffisamment matériels pour justifier une architecture préventive.

## 2. Fonds souverain et subvention étrangère : trois objets à ne pas fusionner

Le dossier e&/PPF Telecom sous le Foreign Subsidies Regulation est un contrôle discriminant. e&, opérateur émirati, est contrôlé par l'Emirates Investment Authority, fonds souverain contrôlé par les Émirats arabes unis. La Commission a identifié des subventions étrangères, notamment une garantie étatique illimitée, mais a conclu qu'elles n'avaient pas eu d'effet négatif réel ou potentiel sur la concurrence **dans le processus d'acquisition** : e& était l'unique candidat et disposait de ressources propres suffisantes. La Commission a néanmoins estimé que les subventions pouvaient distordre la concurrence après l'opération et a rendu contraignants des engagements supprimant la garantie, interdisant certains financements vers les activités européennes de PPF et imposant une surveillance.

Ce dossier ferme quatre séparations : `fonds souverain != tasking politique`; `subvention étrangère != contrôle de sécurité`; `acquisition autorisée sous remèdes != absence de risque`; `risque/distorsion post-transaction != acquisition faussée`. Le FSR protège l'égalité concurrentielle du marché intérieur ; le filtrage IEF/FDI protège sécurité et ordre public. Les deux peuvent concerner la même opération sans répondre à la même question.

Le fonds souverain norvégien GPFG constitue un contrôle négatif indispensable. Il appartient à l'État norvégien et son cadre général est défini politiquement, mais le cadre officiel sépare ce mandat général de la gestion opérationnelle confiée à Norges Bank. Cette délégation ne prouve évidemment pas l'absence de toute influence politique possible ; elle suffit en revanche à réfuter l'équivalence automatique `fonds souverain -> tasking politique de chaque participation`. La qualité de fonds souverain ne permet donc jamais, seule, d'inférer un ordre politique sur une entreprise détenue.

## 3. De la propriété au contrôle opérationnel : le cas Piraeus

Le port du Pirée montre que l'étage `ownership -> operational control` peut être fermé sans fermer l'étage `operational control -> political coercion`. COSCO SHIPPING a acquis 51 % des droits de vote en 2016, puis 67 % en 2021 après réalisation des conditions de l'accord de privatisation. Les annonces de PPA identifient la chaîne de détention jusqu'à China COSCO SHIPPING Corporation, décrite comme entreprise publique chinoise dans la notification de 2016. La majorité de vote est donc un fait de gouvernance matériel.

Cette gouvernance n'est pas purement nominale. En 2020, le conseil de PPA a autorisé une transaction avec Piraeus Container Terminal, autre société du groupe COSCO, pour fournir des services de gestion opérationnelle au Pier I. Cela ferme au moins `contrôle actionnarial/groupe -> coordination corporate -> décisions opérationnelles`. Mais le dossier public ne ferme pas `Pékin -> instruction politique -> PPA -> décision grecque ou européenne`.

L'étude TRAN du Parlement européen traite explicitement la dépendance et la coercition/influence comme des dimensions de risque des investissements maritimes chinois. Cette qualification est utile pour formuler l'hypothèse à tester ; elle n'est pas une preuve que le contrôle de COSCO au Pirée a déjà été exercé comme coercition politique. Le port est donc un cas utile précisément parce qu'il contient **beaucoup de contrôle réel mais une arête politique encore ouverte**.

## 4. Le screening n'est pas la preuve de l'intention qu'il prévient

Le contrôle britannique de Newport Wafer Fab fournit un comparateur borné. Nexperia avait porté sa participation à 100 % ; en 2022, le gouvernement britannique a ordonné la cession d'au moins 86 %, en invoquant des risques pour la technologie, le savoir-faire et le cluster de semi-conducteurs. Le fait qu'une autorité impose un unwind démontre le pouvoir juridique du screening et la matérialité du risque évalué. Il ne démontre pas, par lui-même, que l'investisseur avait déjà exercé une coercition politique.

Le même principe vaut pour les mesures françaises. Les pouvoirs de police permettent de suspendre des droits de vote, imposer une cession ou rétablir la situation antérieure lorsque l'opération n'est pas autorisée ou que des conditions ne sont pas respectées. Ces outils confirment que les **droits de propriété et de vote sont des leviers juridiquement réversibles** lorsqu'un risque stratégique est identifié. Mais `mitigation != culpabilité`, `refus != ingérence`, `screening != attribution d'intention`.

## 5. Ce que le run ferme et ce qu'il ne ferme pas

Le résultat robuste est un gradient :

```text
CAPITAL / PARTICIPATION
-> DROITS JURIDIQUES DE CONTRÔLE
-> GOUVERNANCE / INFORMATION / OPÉRATION
-> DÉPENDANCE OU CAPACITÉ DE BLOCAGE
-> EXERCICE OU MENACE DU LEVIER
-> ADAPTATION / DÉCISION
-> EFFET POLITIQUE
```

Le corpus ferme souvent les trois premiers étages. Il ferme parfois l'intervention publique destinée à empêcher les étages suivants. Il ferme beaucoup plus rarement l'exercice d'un droit actionnarial comme **coercition politique d'un État sur un autre État**.

Cette absence n'est pas une preuve d'innocuité. Elle déplace le prochain objet d'enquête : lorsque la propriété ne suffit pas à démontrer la coercition, le levier le plus discriminant devient la **dépendance à un flux difficilement substituable** — énergie, matières critiques, infrastructures financières ou crédit — où la menace de coupure ou la conditionnalité peut être observable sans passer par un conseil d'administration.

## Bornes

- `ownership != control` ;
- `control != operational exercise` ;
- `operational exercise != political coercion` ;
- `state-linked investor != state tasking` ;
- `foreign subsidy != foreign command` ;
- `screening concern != hostile intent` ;
- `mitigation/refusal != proof of wrongdoing` ;
- `dependency != exercised leverage`.

Le run ne fournit pas de dénominateur général permettant d'estimer la fréquence avec laquelle des investissements étrangers stratégiques deviennent des instruments politiques. Il ne démontre pas non plus une architecture générale de commandement étatique derrière les fonds souverains. Il ferme un mécanisme de **capacité de contrôle** et borne strictement le passage de cette capacité à la coercition.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:0|EDI_DECISIVE:5|SRC_COMPLETE:13/13

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-11
- **breaks:**
  - 2017 STX preemption/Franco-Italian agreement
  - 2021 Photonis refusal publication
  - 2022 Newport Wafer Fab unwind
  - 2024 e&/PPF FSR commitments
  - 2025 French IEF 2024 report
  - 2026 EU FDI screening regulation
- **status:** CURRENT
- **window:** France/UE principalement 2016-2026; comparateurs UK/Norvège bornés

### MANIPULATION_REPORT
- **assumptions:**
  - qualification follows proved ownership/control/exercise/effect edges
- **clusters:**
  - POWER
  - MONEY
  - NETWORK
- **complexity:**
  - **band:** HIGH
  - **score:** 9
- **implicit:**
  - political coercion is downstream of control and exercise, not ownership itself
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - foreign-owner=ingérence
  - majority=coercion
  - state-owned=tasked
  - screened=guilty
  - mitigated=wrongdoing
  - subsidised=commanded
- **priorities:**
  - primary legal sources
  - official screening outcomes
  - corporate governance filings
  - negative controls
  - jurisdiction separation
- **query_guidance:** close capital/control/operational/political edges separately; preserve screening-risk vs hostile-intent distinction
- **rhetorical:**
  - NONE
- **speaker:** mechanism-first forensic investigation contract
- **symbol_stage:** FINAL
- **symbols:**
  - **ACTOR:** person/entity acting
  - **ASSET:** strategic target/technology/infrastructure
  - **BENEFICIAL_OWNER:** ultimate natural/entity controller as legally defined
  - **BOARD:** board appointment/representation rights
  - **COERCION:** exercise/threat to alter a target decision
  - **CONTROL:** effective management/governance rights
  - **EFFECT:** downstream institutional/economic outcome
  - **FSR:** foreign-subsidy distortion review
  - **LEVERAGE:** actionable control/dependency capability
  - **OWNERSHIP:** capital/economic holding
  - **PRINCIPAL:** economic/political interest behind investor
  - **SCREENING:** security/public-order review
  - **STATE_LINK:** government ownership/funding/special-right relation
  - **VETO:** blocking/special rights
  - **VOTE:** voting rights
- **threats:**
  - guilt by ownership
  - risk-to-intent promotion
  - screening-to-prevalence extrapolation
  - state-linkage overclaim
  - not found=does not exist

### MODULE_EXECUTION
NONE

### SCOPING_REPORT
- **chain:**
  - principal/state link
  - investor/fund
  - acquisition
  - control rights
  - strategic asset
  - operational/dependency leverage
  - exercise/threat
  - adaptation/decision
  - effect
- **exclusions:**
  - foreign capital alone
  - screening alone
  - generic geopolitics without ownership/control edge
- **object:** Strategic foreign ownership/control as potential leverage
- **scope:** France/UE 2016-2026; bounded UK/Norway controls

### CREDO
- ownership != control
- control != coercion
- state-linked investor != state tasking
- foreign subsidy != foreign command
- screening concern != hostile intent
- mitigation/refusal != wrongdoing
- operational control != public-policy coercion
- case existence != prevalence

### COGNITIVE_MAP
- **causal_boundary:** control becomes political leverage only when an actor-specific exercise/threat changes a target decision
- **core_model:** strategic investment creates a capability gradient from capital to control to operational leverage; political coercion is a further evidence step
- **rival_models:**
  - ordinary portfolio investment
  - commercial acquisition
  - security-risk prevention without hostile intent
  - state-linked investment with arm’s-length management
  - corporate operational integration without public-policy tasking
- **serial_edges:**
  - capital
  - control rights
  - governance/operation
  - dependency/blocking capacity
  - exercise/threat
  - adaptation
  - effect

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** capital ownership may be commercial and screening is preventive
  - **resolution:** require control rights plus exercised/credible leverage and a target effect
  - **thesis:** foreign strategic ownership is interference
- **item 2:**
  - **antithesis:** GPFG has arm’s-length operational management; e&/PPF had state linkage without acquisition-process distortion
  - **resolution:** state link is a risk/context edge, not tasking proof
  - **thesis:** state-owned fund means state command
- **item 3:**
  - **antithesis:** corporate voting and operations are documented but EP study does not confirm political leverage objective from public information
  - **resolution:** close corporate control; preserve political causal gap
  - **thesis:** Piraeus majority control proves Greek policy capture

### RESOURCE_FLOW_MAP
- **item 1:**
  - **case:** Photonis/Teledyne
  - **flow:** foreign acquisition bid -> IEF review/conditions -> non-authorisation -> national solution
  - **status:** SUPPORTED_SCREENING_OUTCOME
  - **support:**
    - FCT-008
- **item 2:**
  - **case:** STX/Fincantieri
  - **flow:** foreign strategic buyer -> French preemption -> negotiated capital/governance/technology safeguards
  - **status:** SUPPORTED_GOVERNANCE_CONTROL
  - **support:**
    - FCT-009
- **item 3:**
  - **case:** e&/PPF
  - **flow:** UAE state-linked investor/subsidies -> acquisition -> FSR review -> commitments restricting post-transaction subsidy channel
  - **status:** SUPPORTED_FSR_CONTROL
  - **support:**
    - FCT-010
    - FCT-011
    - FCT-012
    - FCT-013
- **item 4:**
  - **case:** Piraeus/COSCO
  - **flow:** 67% voting rights -> related-group operational coordination -> political coercion NOT_CLOSED
  - **status:** CONTROL_WITH_POLITICAL_GAP
  - **support:**
    - FCT-015
    - FCT-016
    - FCT-017
- **item 5:**
  - **case:** Newport Wafer Fab/Nexperia
  - **flow:** 100% acquisition -> national-security review -> order to divest >=86%
  - **status:** BOUNDED_UK_COMPARATOR
  - **support:**
    - FCT-018

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** foreign/state-linked principal
  - **relation:** ownership/funding/control
  - **support:**
    - FCT-002
    - FCT-010
  - **to:** investor/fund
- **item 2:**
  - **from:** investor
  - **relation:** acquisition/voting/governance rights
  - **support:**
    - FCT-001
    - FCT-006
    - FCT-015
  - **to:** strategic target
- **item 3:**
  - **from:** COSCO-controlled PPA
  - **relation:** related-party operational services
  - **support:**
    - FCT-016
  - **to:** PCT/Pier I
- **item 4:**
  - **from:** screening authority
  - **relation:** condition/refuse/unwind/suspend rights
  - **support:**
    - FCT-004
    - FCT-007
    - FCT-008
    - FCT-018
  - **to:** foreign investment/control rights

### IMPACT_MAP
- **downstream:** promotes dependency-based coercion as next discriminant, especially energy/critical materials
- **measured_objects:**
  - control rights
  - screening interventions
  - governance safeguards
  - state-linked investment remedies
  - operational corporate coordination
- **not_established:**
  - prevalence of political coercion via FDI
  - state tasking in each sovereign-fund investment
  - general Beijing->Piraeus->Greek policy causal chain

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** screening and negative controls show ownership can remain commercial/preventive
  - **issue:** foreign ownership=ingérence
  - **pro:** strategic ownership can create control/dependency
  - **resolution:** REQUIRES_CONTROL_PLUS_EXERCISED_LEVERAGE
- **item 2:**
  - **contra:** GPFG independent operations; e&/PPF acquisition process not found distorted
  - **issue:** state-linked=tasked
  - **pro:** EU 2026 regulation treats government control/funding/special rights as risk factors
  - **resolution:** STATE_LINK_IS_CONTEXT_NOT_TASKING
- **item 3:**
  - **contra:** EP study says political leverage objective not confirmed by public information
  - **issue:** Piraeus=proven political coercion
  - **pro:** 67% voting rights and operational coordination are material
  - **resolution:** CONTROL_CLOSED_POLITICAL_EDGE_OPEN

### VERIFICATION_REPORT
- **checks:**
  - EU 2026 FDI regulation separated risk factors from proof
  - French IEF aggregate statistics not promoted to hostile-intent prevalence
  - Photonis refusal sourced to official parliamentary response
  - STX preemption/governance sourced to official French material
  - FSR separated from security screening
  - GPFG retained as state-owned negative control
  - Piraeus control separated from political coercion
  - UK comparator bounded as non-EU
- **status:** PASS_WITH_EXPLICIT_GAP

### EDI_REPORT
- **corpus:** 13 accepted sources across 3 provenance families; French IEF policy pages share an institutional lineage and are not counted as independent prevalence evidence
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
    - **claim:** CLM-005
    - **families:**
      - A
      - B
  - **item 4:**
    - **claim:** CLM-007
    - **families:**
      - B
      - C
  - **item 5:**
    - **claim:** CLM-008
    - **families:**
      - A
      - C
- **diagnostic_not_truth:** true
- **dimensions:**
  - EU FDI screening law
  - French IEF aggregates/powers
  - Photonis outcome
  - STX governance safeguards
  - FSR e&/PPF findings
  - sovereign-fund negative control
  - Piraeus corporate control
  - political-leverage gap
  - UK unwind comparator
- **edi:** PRIMARY_OFFICIAL_DOMINANT_WITH_BOUNDED_ANALYTICAL_RISK_STUDY
- **source_counts:**
  - **A:** 7
  - **B:** 4
  - **C:** 2

### RESPONSIBILITY_MAP
- **item 1:**
  - **claim:** EU FDI screening criteria/powers
  - **owner:** EU legislature
  - **status:** ESTABLISHED
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
    - FCT-004
- **item 2:**
  - **claim:** French IEF interventions/Photonis
  - **owner:** French Government/DG Trésor
  - **status:** OFFICIAL
  - **support:**
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-008
- **item 3:**
  - **claim:** e&/PPF FSR findings
  - **owner:** European Commission
  - **status:** FINAL_COMMITMENT_DECISION
  - **support:**
    - FCT-010
    - FCT-011
    - FCT-012
    - FCT-013
- **item 4:**
  - **claim:** Piraeus voting/operational control
  - **owner:** Piraeus Port Authority filings
  - **status:** DOCUMENTED_CORPORATE_CONTROL
  - **support:**
    - FCT-015
    - FCT-016
- **item 5:**
  - **claim:** Piraeus political coercion
  - **owner:** INV-150 synthesis
  - **status:** NOT_ESTABLISHED
  - **support:**
    - FCT-017

### NEXT_QUERIES
- **item 1:**
  - **query:** energy or critical-material dependency -> explicit threat/restriction -> target adaptation/public decision in France/EU
  - **route:** NEW_INVESTIGATION
  - **trigger:** INV-151
- **item 2:**
  - **query:** foreign strategic ownership -> actor-specific political coercion in EU
  - **route:** RECHECK
  - **trigger:** new documentary/tasking evidence
- **item 3:**
  - **query:** generic foreign ownership without control/exercise
  - **route:** DROP
  - **trigger:** mechanism insufficient

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-004,FCT-008,FCT-009,FCT-015,FCT-016,FCT-017,FCT-018 | final:GAP | gap:DENOMINATOR
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-001,FCT-002,FCT-004,FCT-006,FCT-007 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-005,FCT-008,FCT-009,FCT-018 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-010,FCT-011,FCT-012,FCT-013,FCT-014 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-015,FCT-016 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-003,FCT-017 | final:GAP | gap:CAUSALITY
CLM-001 | attempts:QRY-001,QRY-002,QRY-003,SRC-001,SRC-002,SRC-003 | support:FCT-001,FCT-004,FCT-005,FCT-006 | counter:- | results:FCT-001,FCT-004,FCT-005,FCT-006 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-001,QRY-003,QRY-004,QRY-005,QRY-006,QRY-013,SRC-001,SRC-003,SRC-004,SRC-005,SRC-006,SRC-013 | support:FCT-004,FCT-006,FCT-007,FCT-008,FCT-009,FCT-018 | counter:- | results:FCT-004,FCT-006,FCT-007,FCT-008,FCT-009,FCT-018 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-005,SRC-005 | support:FCT-008 | counter:- | results:FCT-008 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-006,SRC-006 | support:FCT-009 | counter:- | results:FCT-009 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-007,QRY-009,SRC-007,SRC-009 | support:FCT-010,FCT-014 | counter:FCT-010,FCT-014 | results:FCT-010,FCT-014,FCT-010,FCT-014 | final:REFUTED | gap:NONE
CLM-006 | attempts:QRY-007,QRY-008,SRC-007,SRC-008 | support:FCT-010,FCT-011,FCT-012,FCT-013 | counter:- | results:FCT-010,FCT-011,FCT-012,FCT-013 | final:SUPPORTED | gap:NONE
CLM-007 | attempts:QRY-010,QRY-011,QRY-012,SRC-010,SRC-011,SRC-012 | support:FCT-015,FCT-016,FCT-017 | counter:- | results:FCT-015,FCT-016,FCT-017 | final:PARTIAL | gap:CAUSALITY
CLM-008 | attempts:QRY-001,QRY-004,QRY-013,SRC-001,SRC-004,SRC-013 | support:FCT-004,FCT-007,FCT-018 | counter:FCT-004,FCT-007,FCT-018 | results:FCT-004,FCT-007,FCT-018,FCT-004,FCT-007,FCT-018 | final:REFUTED | gap:NONE
CLM-009 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:- | final:GAP | gap:DENOMINATOR

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
AXS-005 | AXS | GAP | CAUSALITY | Public material demonstrates risk and dependency, but does not close a general actor-specific control->political-coercion chain in the scoped France/EU cases.
CLM-007 | CLM | PARTIAL | CAUSALITY | Public evidence closes voting control and corporate operation but not state tasking to a public-policy outcome.
CLM-009 | CLM | GAP | DENOMINATOR | No representative denominator and no general causal design from ownership to political coercion.
CAU-001 | CAU | SUPPORTED | CAUSALITY | No representative France/EU denominator and no general closed political-coercion chain in this run.

SEMANTIC_COUNTS_V1:LED:2|CLM:9|AXS:5|CAU:1|CTRL:7|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013"],"evidence_excerpt":"Trace principal -> investor -> acquisition -> control rights -> strategic asset -> exercise/threat -> decision/effect.","kind":"HYPOTHESIS","lead":"Strategic ownership becomes a potential interference/coercion mechanism only when capital confers actionable control rights over a strategic asset and those rights or dependencies are exercised or credibly mobilised.","linked_ids":["CLM-001","CLM-002","CLM-003","CLM-004","CLM-005","CLM-006","CLM-007","CLM-008"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018"],"routes":["POWER","MONEY","NETWORK"],"source_id":"INV-150-RUN_CARD","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013"],"evidence_excerpt":"Screening and ownership cases close capability/control more often than political tasking/effect.","gap":"No representative denominator; case existence and screening intensity cannot be promoted to prevalence of coercive use.","gap_type":"DENOMINATOR","kind":"GAP","lead":"Representative denominator for foreign strategic ownership converted into political coercion in France/EU.","linked_ids":["CLM-009"],"locator":"GAP","materiality":"HIGH","result_ids":["FCT-004","FCT-008","FCT-009","FCT-015","FCT-016","FCT-017","FCT-018"],"routes":["RECHECK"],"source_id":"INV-150-RUN_CARD","status":"GAP"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Foreign ownership or an FDI-screening concern is not, by itself, interference or coercion.","claimant":"INV-150 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-004","FCT-005","FCT-006"]}
CLM-002 | {"claim":"Control rights are materially distinct from mere capital ownership and can be conditioned, suspended, refused or unwound by screening authorities.","claimant":"INV-150 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-004","FCT-006","FCT-007","FCT-008","FCT-009","FCT-018"]}
CLM-003 | {"claim":"Photonis is a French positive control for screening changing the ownership outcome of a strategic asset without proving hostile intent by the bidder.","claimant":"INV-150 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-008"]}
CLM-004 | {"claim":"The STX/Fincantieri case shows that governance architecture, voting structure and technology/workload safeguards can be treated as strategic controls in acquisition negotiations.","claimant":"INV-150 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-009"]}
CLM-005 | {"claim":"A sovereign-wealth-fund or state-linked investor automatically acts under political tasking in each portfolio company.","claimant":"strongest adverse shortcut","counter":["FCT-010","FCT-014"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"REFUTED","support":["FCT-010","FCT-014"]}
CLM-006 | {"claim":"The e&/PPF case shows foreign subsidies and state linkage can trigger competition remedies even when the acquisition process itself was not found distorted.","claimant":"INV-150 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-010","FCT-011","FCT-012","FCT-013"]}
CLM-007 | {"claim":"Piraeus closes ownership/control and intra-group operational coordination, but not a public-evidence chain from Beijing tasking to a Greek/EU political decision.","claimant":"INV-150 synthesis","counter":"NONE_FOUND","gap":"Public evidence closes voting control and corporate operation but not state tasking to a public-policy outcome.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-015","FCT-016","FCT-017"]}
CLM-008 | {"claim":"The existence of screening, mitigation or an unwind order proves prior hostile political use of the investment.","claimant":"strongest adverse shortcut","counter":["FCT-004","FCT-007","FCT-018"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"REFUTED","support":["FCT-004","FCT-007","FCT-018"]}
CLM-009 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013"],"claim":"This run establishes how frequently strategic foreign ownership becomes political coercion in France/EU.","claimant":"INV-150 synthesis","counter":"NONE_FOUND","gap":"No representative denominator and no general causal design from ownership to political coercion.","gap_type":"DENOMINATOR","materiality":"HIGH","status":"GAP","support":"NONE_FOUND"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013"],"axis":"LEGAL_CONTROL","links":["CLM-001","CLM-002"],"question":"When does an acquisition confer effective control and what rights are screened?","result_ids":["FCT-001","FCT-002","FCT-004","FCT-006","FCT-007"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013"],"axis":"SCREENING_INTERVENTION","links":["CLM-003","CLM-004","CLM-008"],"question":"Are control rights actually conditioned/refused/unwound?","result_ids":["FCT-005","FCT-008","FCT-009","FCT-018"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013"],"axis":"STATE_LINKAGE","links":["CLM-005","CLM-006"],"question":"Does state ownership/subsidy establish political tasking?","result_ids":["FCT-010","FCT-011","FCT-012","FCT-013","FCT-014"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013"],"axis":"OPERATIONAL_EXERCISE","links":["CLM-007"],"question":"Can ownership translate into operational corporate control?","result_ids":["FCT-015","FCT-016"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013"],"axis":"POLITICAL_COERCION","gap":"Public material demonstrates risk and dependency, but does not close a general actor-specific control->political-coercion chain in the scoped France/EU cases.","gap_type":"CAUSALITY","links":["CLM-007","CLM-009"],"question":"Is foreign ownership/control shown to be exercised to force a French/EU public decision?","result_ids":["FCT-003","FCT-017"],"sought_objects":["CHAIN","COUNTER","STATUS"],"status":"GAP"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"CONTROL_RIGHTS_PLUS_EXERCISED_OR_CREDIBLE_LEVERAGE_REQUIRED","counter":"GPFG arm’s-length governance and e&/PPF acquisition-process findings show state ownership/subsidy does not automatically prove political tasking; Piraeus public evidence does not close Beijing->Greek political decision.","gap":"No representative France/EU denominator and no general closed political-coercion chain in this run.","gap_type":"CAUSALITY","limit":"Political coercion requires actor-specific evidence of exercise/threat and target adaptation; screening or majority ownership alone is insufficient.","mechanism":"principal/state link -> investor -> acquisition -> control rights -> strategic asset -> operational/dependency leverage -> exercised threat/action -> adaptation/public decision","question":"When does strategic foreign ownership become a political leverage mechanism rather than a corporate property relation or screening risk?","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-008","FCT-009","FCT-015","FCT-016"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"ownership != control","status":"PASS","support":["FCT-001","FCT-006"]}
CTRL-002 | {"control":"control != coercion","status":"PASS","support":["FCT-003","FCT-017"]}
CTRL-003 | {"control":"state-linked investor != state tasking","status":"PASS","support":["FCT-010","FCT-014"]}
CTRL-004 | {"control":"foreign subsidy != foreign command","status":"PASS","support":["FCT-011","FCT-012","FCT-013"]}
CTRL-005 | {"control":"screening concern != hostile intent","status":"PASS","support":["FCT-004","FCT-005"]}
CTRL-006 | {"control":"mitigation/refusal != wrongdoing","status":"PASS","support":["FCT-004","FCT-008","FCT-018"]}
CTRL-007 | {"control":"corporate operational coordination != public-policy coercion","status":"PASS","support":["FCT-016","FCT-017"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:13|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"EMPTY","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | MNEMO_UNAVAILABLE | mnemo | NONE | MNEMO_Q
SYS-003 | SYS | PASS | runtime | FCT-013 | REPAIR_FACT
SYS-004 | SYS | PASS | runtime | FCT-014 | REPAIR_FACT
SYS-005 | SYS | PASS | runtime | FCT-017 | REPAIR_FACT
SYS-006 | SYS | PASS | runtime | FCT-013 | REPAIR_FACT
SYS-007 | SYS | PASS | runtime | FCT-014 | REPAIR_FACT
SYS-008 | SYS | PASS | runtime | FCT-017 | REPAIR_FACT
SYS-009 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32026R1386 | -
QRY-002 | FETCH | FOUND | SRC-002 | https://www.tresor.economie.gouv.fr/Articles/2025/07/30/publication-du-rapport-annuel-sur-le-controle-ief-en-2024 | -
QRY-003 | FETCH | FOUND | SRC-003 | https://www.tresor.economie.gouv.fr/services-aux-entreprises/investissements-etrangers-en-france/les-conditions-d-une-operation-soumise-a-autorisation-prealable | -
QRY-004 | FETCH | FOUND | SRC-004 | https://www.tresor.economie.gouv.fr/services-aux-entreprises/investissements-etrangers-en-france/les-pouvoirs-de-police-du-ministre-charge-de-l-economie | -
QRY-005 | FETCH | FOUND | SRC-005 | https://www.assemblee-nationale.fr/dyn/15/questions/QANR5L15QE33511 | -
QRY-006 | FETCH | FOUND | SRC-006 | https://www.elysee.fr/emmanuel-macron/2017/09/27/declaration-conjointe-du-president-de-la-republique-emmanuel-macron-et-de-paolo-gentiloni-president-du-conseil-des-ministres-de-la-republique-italienne | -
QRY-007 | FETCH | FOUND | SRC-007 | https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_24_4842/IP_24_4842_EN.pdf | -
QRY-008 | FETCH | FOUND | SRC-008 | https://competition-policy.ec.europa.eu/foreign-subsidies-regulation/about_en | -
QRY-009 | FETCH | FOUND | SRC-009 | https://www.regjeringen.no/en/documents/meld.-st.-7-2025-2026/id3155109/?ch=1 | -
QRY-010 | FETCH | FOUND | SRC-010 | https://olp.gr/en/investor-relations/corporate-announcements/corporate-announcements-2021/notification-of-significant-change-of-voting-rights-pursuant-to-law-3556-2007 | -
QRY-011 | FETCH | FOUND | SRC-011 | https://www.olp.gr/en/investor-relations/corporate-announcements/corporate-announcements-2020/public-disclosure-of-inside-information-according-to-regulation-eu-5962014-and-implementing-regulation-eu-20161055 | -
QRY-012 | FETCH | FOUND | SRC-012 | https://www.europarl.europa.eu/RegData/etudes/STUD/2023/747278/IPOL_STU%282023%29747278_EN.pdf | -
QRY-013 | FETCH | FOUND | SRC-013 | https://assets.publishing.service.gov.uk/media/6375ef068fa8f5771111bd60/NWF_Final_Order_Public_Notice_16112022.pdf | -

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | EU-FDI-2026 | Regulation (EU) 2026/1386 — screening foreign investments | 2026-06-26 | 2026-09-11T16:28:00Z | definitions, government control, beneficial owner, mitigation/prohibition/unwind, coercion-risk criterion | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32026R1386
SRC-002 | ◈ | fam:A | FR-IEF-2024 | DG Trésor — rapport annuel IEF 2024 | 2025-07-30 | 2026-09-11T16:28:00Z | 392 dossiers; 182 eligible; 54% conditioned; six refus over prior three years | https://www.tresor.economie.gouv.fr/Articles/2025/07/30/publication-du-rapport-annuel-sur-le-controle-ief-en-2024
SRC-003 | ◈ | fam:A | FR-IEF-CONDITIONS | DG Trésor — conditions et issues du contrôle IEF | 2024-12-30 | 2026-09-11T16:28:00Z | control thresholds, chain of control, authorise/condition/refuse, government links | https://www.tresor.economie.gouv.fr/services-aux-entreprises/investissements-etrangers-en-france/les-conditions-d-une-operation-soumise-a-autorisation-prealable
SRC-004 | ◈ | fam:A | FR-IEF-POLICE | DG Trésor — pouvoirs de police IEF | 2024-12-31 | 2026-09-11T16:28:00Z | unwind, suspend voting rights, mandate, asset/dividend restrictions | https://www.tresor.economie.gouv.fr/services-aux-entreprises/investissements-etrangers-en-france/les-pouvoirs-de-police-du-ministre-charge-de-l-economie
SRC-005 | ◈ | fam:B | FR-PHOTONIS-2021 | Assemblée nationale — réponse ministérielle Photonis/Teledyne | 2021-09-07 | 2026-09-11T16:28:00Z | decision not to authorise Teledyne acquisition of Photonis | https://www.assemblee-nationale.fr/dyn/15/questions/QANR5L15QE33511
SRC-006 | ◈ | fam:B | FR-STX-2017 | Élysée — accord franco-italien STX/Fincantieri | 2017-09-27 | 2026-09-11T16:28:00Z | preemption, 50/50 capital structure, 1% share loan and technology/workload safeguards | https://www.elysee.fr/emmanuel-macron/2017/09/27/declaration-conjointe-du-president-de-la-republique-emmanuel-macron-et-de-paolo-gentiloni-president-du-conseil-des-ministres-de-la-republique-italienne
SRC-007 | ◈ | fam:A | EU-FSR-EPPF-2024 | European Commission — e& / PPF Telecom conditional approval under FSR | 2024-09-24 | 2026-09-11T16:28:00Z | UAE sovereign-linked investor, subsidies, no acquisition-process distortion, post-transaction commitments | https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_24_4842/IP_24_4842_EN.pdf
SRC-008 | ◈ | fam:A | EU-FSR-LIVE | European Commission — Foreign Subsidies Regulation scope (living page; underlying Regulation (EU) 2022/2560) | 2022-12-23 | 2026-09-11T16:28:00Z | FSR internal-market distortion tool; underlying Regulation (EU) 2022/2560 published 2022-12-23; living page checked 2026-09-11 | https://competition-policy.ec.europa.eu/foreign-subsidies-regulation/about_en
SRC-009 | ◈ | fam:B | NO-GPFG-2026 | Norway Ministry of Finance — The Government Pension Fund 2026 | 2026-03-27 | 2026-09-11T16:28:00Z | official report: broad political mandate/framework versus operational management/portfolio decisions | https://www.regjeringen.no/en/documents/meld.-st.-7-2025-2026/id3155109/?ch=1
SRC-010 | ◈ | fam:B | PPA-COSCO-2021 | Piraeus Port Authority — COSCO 67% voting rights | 2021-10-07 | 2026-09-11T16:28:00Z | 67% voting rights; upstream COSCO chain | https://olp.gr/en/investor-relations/corporate-announcements/corporate-announcements-2021/notification-of-significant-change-of-voting-rights-pursuant-to-law-3556-2007
SRC-011 | ◈ | fam:B | PPA-RELATED-2020 | Piraeus Port Authority — related-party Pier I project management transaction | 2020-04-01 | 2026-09-11T16:28:00Z | PPA and PCT as related COSCO subsidiaries; project management services for Pier I | https://www.olp.gr/en/investor-relations/corporate-announcements/corporate-announcements-2020/public-disclosure-of-inside-information-according-to-regulation-eu-5962014-and-implementing-regulation-eu-20161055
SRC-012 | ◈ | fam:C | EP-TRAN-PORTS-2023 | European Parliament TRAN study — Chinese Investments in European Maritime Infrastructure | 2023-10-02 | 2026-09-11T16:28:00Z | study risk dimensions include dependency and coercion/influence; analytical risk framing != proof of exercised coercion | https://www.europarl.europa.eu/RegData/etudes/STUD/2023/747278/IPOL_STU%282023%29747278_EN.pdf
SRC-013 | ◈ | fam:C | UK-NWF-2022 | UK Government — Nexperia/Newport Wafer Fab final order | 2022-11-16 | 2026-09-11T16:28:00Z | 100% acquisition; order to divest at least 86% on national-security grounds | https://assets.publishing.service.gov.uk/media/6375ef068fa8f5771111bd60/NWF_Final_Order_Public_Notice_16112022.pdf

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32026R1386 | A | 2026-06-26 | Foreign investment and control | Regulation (EU) 2026/1386 defines foreign investment around lasting/direct links enabling effective participation in management or control and extends coverage to Union subsidiaries controlled by foreign investors. | -
FCT-002 | FACT | ✧ | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32026R1386 | A | 2026-06-26 | Beneficial owner and government control | The 2026 EU framework explicitly examines beneficial owners, opaque ownership, significant government funding, special rights and state-appointed directors when assessing foreign-investment risk. | -
FCT-003 | FACT | ✧ | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32026R1386 | A | 2026-06-26 | Coercion as risk criterion | The 2026 EU framework asks whether a foreign investor or controlling/beneficial party is likely to pursue a third-country policy objective, including using the investment to coerce a Member State or the Union to modify, adopt or cease an act. | -
FCT-004 | FACT | ✧ | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32026R1386 | A | 2026-06-26 | Screening outcomes | The EU framework defines screening as capable of authorising, mitigating, prohibiting or unwinding foreign investments on security/public-order grounds. | -
FCT-005 | FACT | ✧ | https://www.tresor.economie.gouv.fr/Articles/2025/07/30/publication-du-rapport-annuel-sur-le-controle-ief-en-2024 | A | 2025-07-30 | French screening activity 2024 | France received 392 IEF files in 2024; 182 eligible authorisations were delivered and 54% were subject to conditions; the ministry reports six refusal decisions over the preceding three years. | -
FCT-006 | FACT | ✧ | https://www.tresor.economie.gouv.fr/services-aux-entreprises/investissements-etrangers-en-france/les-conditions-d-une-operation-soumise-a-autorisation-prealable | A | 2024-12-30 | French control chain and outcomes | French IEF follows the investor chain of control and may authorise, condition or refuse; links with a foreign government/public body may be considered in refusal analysis. | -
FCT-007 | FACT | ✧ | https://www.tresor.economie.gouv.fr/services-aux-entreprises/investissements-etrangers-en-france/les-pouvoirs-de-police-du-ministre-charge-de-l-economie | A | 2024-12-31 | French police powers | For unauthorised investments or breached conditions, the minister can require modification or restoration, withdraw authorisation, impose divestment, suspend voting rights, appoint a representative or restrict asset/dividend disposal. | -
FCT-008 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/15/questions/QANR5L15QE33511 | B | 2021-09-07 | Photonis refusal | The French Government states that it decided not to authorise Teledyne’s acquisition of Photonis and to prefer a national solution in order to preserve strategic defence interests. | -
FCT-009 | FACT | ✧ | https://www.elysee.fr/emmanuel-macron/2017/09/27/declaration-conjointe-du-president-de-la-republique-emmanuel-macron-et-de-paolo-gentiloni-president-du-conseil-des-ministres-de-la-republique-italienne | B | 2017-09-27 | STX preemption and governance safeguards | France exercised preemption during the STX/Fincantieri negotiations and described a 50/50 capital structure with a 1% share loan whose recovery could protect against technology/workload transfer risks. | -
FCT-010 | FACT | ✧ | https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_24_4842/IP_24_4842_EN.pdf | A | 2024-09-24 | e& state-linked investor | The Commission states that e& is controlled by the Emirates Investment Authority, a sovereign wealth fund controlled by the UAE. | -
FCT-011 | FACT | ✧ | https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_24_4842/IP_24_4842_EN.pdf | A | 2024-09-24 | e& acquisition-process finding | The Commission found that foreign subsidies to e&/EIA did not produce actual or potential negative effects on competition in the PPF acquisition process; e& was the sole bidder and had sufficient own resources. | -
FCT-012 | FACT | ✧ | https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_24_4842/IP_24_4842_EN.pdf | A | 2024-09-24 | e& post-transaction commitments | The Commission found potential post-transaction distortive effects and accepted commitments removing an unlimited state guarantee, restricting EIA/e& financing of PPF EU activities and requiring information on future acquisitions. | -
FCT-013 | FACT | ✧ | https://competition-policy.ec.europa.eu/foreign-subsidies-regulation/about_en | A | 2022-12-23 | FSR distinct object | Regulation (EU) 2022/2560 creates an EU framework to address distortions in the internal market caused by foreign subsidies; this competition/subsidy-control object is distinct from national-security foreign-investment screening. | -
FCT-014 | FACT | ✧ | https://www.regjeringen.no/en/documents/meld.-st.-7-2025-2026/id3155109/?ch=1 | B | 2026-03-27 | Sovereign-fund negative control | Norway’s official GPFG governance framework separates the political owner’s overall mandate/framework from operational management carried out by Norges Bank under delegated governance. State ownership therefore does not by itself establish political tasking of each portfolio company. | -
FCT-015 | FACT | ✧ | https://olp.gr/en/investor-relations/corporate-announcements/corporate-announcements-2021/notification-of-significant-change-of-voting-rights-pursuant-to-law-3556-2007 | B | 2021-10-07 | Piraeus majority voting rights | COSCO Shipping Hong Kong increased its voting rights in Piraeus Port Authority from 51% to 67%; the disclosed chain runs upward to China COSCO Shipping Corporation. | -
FCT-016 | FACT | ✧ | https://www.olp.gr/en/investor-relations/corporate-announcements/corporate-announcements-2020/public-disclosure-of-inside-information-according-to-regulation-eu-5962014-and-implementing-regulation-eu-20161055 | B | 2020-04-01 | Piraeus operational group coordination | PPA’s board authorised a related-party agreement under which Piraeus Container Terminal, another COSCO-group entity, would provide project-management services for PPA’s Pier I operations. | -
FCT-017 | FACT | ✧ | https://www.europarl.europa.eu/RegData/etudes/STUD/2023/747278/IPOL_STU%282023%29747278_EN.pdf | C | 2023-10-02 | Piraeus political-leverage gap | The European Parliament TRAN study evaluates Chinese maritime investments across risk dimensions including dependency and coercion/influence. This supports treating political leverage as a risk hypothesis to test, not as proof that COSCO’s Piraeus control has already been used as political coercion. | -
FCT-018 | FACT | ✧ | https://assets.publishing.service.gov.uk/media/6375ef068fa8f5771111bd60/NWF_Final_Order_Public_Notice_16112022.pdf | C | 2022-11-16 | Newport Wafer Fab unwind comparator | The UK ordered Nexperia to sell at least 86% of Newport Wafer Fab after a 100% acquisition, citing national-security risks concerning technology/know-how and the South Wales semiconductor cluster. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-001
FCT-005 | SRC-002
FCT-006 | SRC-003
FCT-007 | SRC-004
FCT-008 | SRC-005
FCT-009 | SRC-006
FCT-010 | SRC-007
FCT-011 | SRC-007
FCT-012 | SRC-007
FCT-013 | SRC-008
FCT-014 | SRC-009
FCT-015 | SRC-010
FCT-016 | SRC-011
FCT-017 | SRC-012
FCT-018 | SRC-013

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

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:SEARCH
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:FACTS
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:CAUSAL_GAP
CP-004 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 | NEXT_ACTION:VERIFY
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:INVESTIGATION_ACCOUNTABILITY
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:FINALIZE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-11T16:42:17.593355+00:00","fact_mem":{},"mnemo_row":"MNEMO_UNAVAILABLE — local memory service not available; no memory ids fabricated.","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":18,"eligible":18,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_UNAVAILABLE — local memory service not available; no memory ids fabricated. | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:18;attempted:0;success:0;failure:0;blocked:18} | WRITEBACK_EXECUTION_V1:[18 rows, see section]

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
