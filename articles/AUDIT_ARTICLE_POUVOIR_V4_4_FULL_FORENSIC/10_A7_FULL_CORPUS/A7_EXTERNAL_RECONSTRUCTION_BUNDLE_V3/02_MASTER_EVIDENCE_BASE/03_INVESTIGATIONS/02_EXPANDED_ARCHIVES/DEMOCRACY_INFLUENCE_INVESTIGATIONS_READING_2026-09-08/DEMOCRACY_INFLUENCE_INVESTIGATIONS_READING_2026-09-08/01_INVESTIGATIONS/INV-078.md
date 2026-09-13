ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260908-0700-fonds-marianne | PARENT_RUN_ID:NONE | AS_OF:2026-09-08
INPUT_KIND:RUN_CARD | MISSION_MODE:RECHECK_EXTEND | INPUT_REF:PATH:/mnt/data/inv078-work/runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-08_fonds-marianne/2026-09-08_07-00_fonds-marianne_INPUT.md | SUBJECT_SLUG:fonds-marianne | SUBJECT_FP:sha256:71822389c6b96e5d720816264257934eb5c394a285ab3d50cf96da1bd06540ed | INPUT_SHA256:sha256:75b9badcc0213b8e5a03de12764cfe3d4cd253b79dcca8320ac5050444ee0a56
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France, Fonds Marianne 2021-2026; reconstruct public funding, selection, beneficiaries, outputs, controls, accountability and follow-up; separate funding, cabinet intervention, beneficiary political content, editorial tasking, criminal responsibility and political/electoral effect.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/MONEY.md,clusters/POWER.md,clusters/NETWORK.md,clusters/FRAMING.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-078 — Fonds Marianne et financement étatique de la contre-influence

## Résultat central

Le Fonds Marianne fournit un cas très documenté de **financement public d’actions associatives de contre-discours en ligne** dont la conception, la sélection et le contrôle ont connu des défaillances importantes. Le corpus établit l’enveloppe publique, les principaux bénéficiaires, l’implication du cabinet ministériel dans la temporalité et certains arbitrages, des présélections, des faiblesses d’instruction et de suivi, ainsi que des problèmes concrets chez les deux principaux bénéficiaires controversés.

En revanche, trois inférences plus fortes ne résistent pas au standard probatoire. Premièrement, une subvention publique ne démontre pas en soi un **commandement éditorial**. Deuxièmement, l’existence de contenus politiques visant des personnalités ou candidats chez Reconstruire le commun ne démontre pas que ces ciblages aient été **taskés par l’État**. Troisièmement, les inspections, signalements, l’information judiciaire et le titre de perception contesté ne permettent pas de transformer les dysfonctionnements administratifs en **culpabilité pénale définitive**.

Le delta utile pour INV-144 est donc précis : **capacité publique, délégation, intervention politique dans la sélection et défauts de gouvernance sont établis ; commandement éditorial, censure généralisée et effet politique/électoral causal ne le sont pas.**

## 1. Architecture financière et objectif

Le rapport sénatorial fixe l’enveloppe du Fonds Marianne à 2,5 millions d’euros pour 2021. Il indique que 17 associations ont été sélectionnées pour un total d’environ 2,017 millions d’euros. L’objet était de compléter le contre-discours institutionnel par des acteurs associatifs capables de défendre les valeurs républicaines et de combattre les discours séparatistes sur internet. Cette architecture suffit à établir une chaîne **État -> financement -> acteurs associatifs -> production de contenu**. Elle ne suffit pas à qualifier la relation de commande éditoriale.

Une divergence administrative doit rester visible : la réponse du ministère de l’Intérieur publiée en juin 2025 parle de 18 structures retenues. Le corpus courant ne résout pas proprement cette différence avec les 17 associations du rapport sénatorial. Le dénominateur n’est donc pas harmonisé artificiellement.

## 2. Sélection : implication politique et procédure dégradée

Le Sénat conclut que le délai de candidature a été fortement raccourci, que plusieurs associations ont été présélectionnées avant le comité formel et que la ministre est intervenue après le comité pour revenir sur une attribution. Ces éléments établissent que le politique n’a pas seulement défini une orientation générale : le cabinet a matériellement pesé sur le processus.

Le dossier USEPPM est le plus clair pour tester la frontière. Mohamed Sifaoui a rencontré à plusieurs reprises le cabinet avant ou autour du lancement du fonds et a été encouragé à déposer un projet. Le rapport ne trouve toutefois pas d’engagement financier établi lors de ces échanges. Le comité finit par attribuer 355 000 euros, montant dont le passage depuis un arbitrage antérieur de 300 000 euros reste entouré de zones d’ombre. Le projet est décrit comme une « pièce maîtresse » ou un « vaisseau amiral » du fonds.

La conclusion robuste est donc : **accès privilégié, encouragement, centralité du projet et faiblesse de traçabilité sont documentés**. Cela ne permet pas, sans arête supplémentaire, d’affirmer un favoritisme pénal ou une corruption.

## 3. Reconstruire le commun : capacité faible et contenus politiques

Reconstruire le commun avait été créée en octobre 2020 et avait déjà reçu 39 000 euros avant le Fonds Marianne. Elle obtient ensuite 330 000 euros. Des courriels internes cités par le Sénat expriment très tôt des doutes sur sa capacité technique et financière, notamment faute de personnel salarié prévu pour gérer une subvention de cette taille.

Le point le plus sensible concerne les contenus. Le SG-CIPDR connaissait des antécédents de contenus politiques liés au collectif « On vous voit ». Le Sénat n’a pas retrouvé, dans la convention du Fonds Marianne, la condition d’absence de messages politiques évoquée pour le financement antérieur. Une note interne identifiait ensuite des épisodes visant explicitement des personnalités politiques, parfois des candidats, ainsi qu’un faible engagement.

Cela établit **l’existence de contenus politiques financés dans l’écosystème du Fonds Marianne** et un contrôle qualitatif défaillant. Mais le corpus courant ne contient ni ordre éditorial, ni brief, ni validation étatique démontrant que l’administration ou le cabinet aurait commandé le ciblage de ces personnalités. La frontière `beneficiary_output != state_editorial_control` doit donc rester active.

## 4. Contrôle et suites

Les deux dossiers majeurs ont été contrôlés tardivement alors que des signaux existaient dès 2022. Le premier rapport de l’IGA sur l’USEPPM a été suivi de la démission de Christian Gravel ; le ministère a annoncé la mise en œuvre des recommandations. Un second rapport IGA a porté sur l’ensemble des subventions.

La réponse ministérielle de juin 2025 indique que deux associations n’ont pas tenu tous leurs engagements, qu’un titre de perception a été émis contre l’USEPPM et qu’il est contesté. Elle décrit aussi une refonte des procédures : comité de programmation, expertise interne et externe, contrôle documentaire renforcé, création d’un secrétariat général et renforcement des équipes.

Sur le plan judiciaire, une information judiciaire a été ouverte en mai 2023 pour plusieurs qualifications alléguées. Une source de mars 2024 indiquait qu’elle était encore en cours. Le corpus consulté ne permet pas d’établir une décision pénale définitive ultérieure. Il faut donc écrire **information judiciaire / soupçons**, non **culpabilité**.

## 5. Ce que le cas prouve pour l’économie politique de la contre-ingérence

INV-078 apporte quatre éléments directement utiles à INV-144 :

1. l’État peut créer rapidement une capacité financière dédiée à la contre-influence ;
2. la sélection de bénéficiaires peut être affectée par l’urgence politique, la proximité d’acteurs et une procédure insuffisamment formalisée ;
3. une délégation à des acteurs associatifs réduit la visibilité directe de la parole étatique mais crée un problème de contrôle, de traçabilité et de responsabilité ;
4. les mécanismes correctifs existent — inspection, contrôle financier, récupération, réforme — mais peuvent intervenir tardivement.

Ce cas est compatible avec une **expansion bureaucratique et un usage politique de la communication publique**, mais il ne suffit pas à démontrer une architecture coordonnée visant à fabriquer artificiellement la menace ou à censurer des opposants. Pour franchir ce seuil, il faudrait des preuves de tasking, des chaînes contractuelles ou éditoriales explicites, et un effet observable sur la diffusion, la persuasion ou une décision politique.

## Plafond probatoire I0-I7

- **I0 VERIFIED** : acteurs, institutions, bénéficiaires et relations financières principales sont documentés.
- **I1 VERIFIED** : la capacité financière et administrative de financer du contre-discours associatif est établie.
- **I2 VERIFIED** : financement, sélection, interventions et contrôles sont documentés case-specifically.
- **I3 PARTIAL** : intervention politique dans la sélection est documentée ; commandement éditorial et coordination de ciblage politique ne le sont pas.
- **I4 PARTIAL** : des productions et signaux d’engagement sont documentés, mais l’exposition totale n’est pas reconstruite.
- **I5 NOT_ESTABLISHED** : persuasion propre des contenus non isolée.
- **I6 NOT_ESTABLISHED generally** : changement de comportement politique non démontré.
- **I7 NOT_ESTABLISHED** : aucun effet électoral ou politique contrefactuel général n’est démontré.

## Résidu matériel

Trois éléments seulement changeraient le modèle : un jugement pénal définitif ou une décision primaire clarifiant les responsabilités ; des documents établissant un tasking éditorial de contenus politiques ; une évaluation causale reliant dépenses et contenus à l’exposition puis à un comportement politique. En leur absence, une collecte générique supplémentaire serait surtout cumulative.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:4|EDI_DECISIVE:6|SRC_COMPLETE:12/12

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-08
- **notes:**
  - core primary findings 2023
  - Cour des comptes publication 2024
  - ministry parliamentary response June 2025
  - no later final criminal adjudication established in current corpus
- **status:** CURRENT_TO_LATEST_PUBLIC_FOLLOWUP_FOUND
- **window:** 2021-2026

### MANIPULATION_REPORT
- **assumptions:**
  - funding is not editorial command
  - political content is not proof of state tasking
  - administrative irregularity is not criminal guilt
  - spending is not political effect
- **clusters:**
  - **loaded:**
    - clusters/MONEY.md
    - clusters/POWER.md
    - clusters/NETWORK.md
    - clusters/FRAMING.md
- **complexity:**
  - **band:** APEX
  - **score:** 8
- **implicit:**
  - public financing creates capacity without proving editorial command
  - political content by a beneficiary can exist without state tasking
  - late controls can document governance failure without proving criminal intent
- **input_kind:** RUN_CARD
- **mission_mode:** RECHECK_EXTEND
- **patterns:**
  - public funding of counter-discourse
  - accelerated/opaque selection
  - beneficiary capacity failure
  - political content by beneficiary
  - late control
  - editorial-tasking allegation
- **priorities:**
  - money flow
  - selection
  - beneficiaries
  - outputs
  - controls
  - responsibility
  - effect
- **query_guidance:** prioritize primary parliamentary and administrative records; bind each stronger claim to a direct edge; preserve denominator, criminal-status and causal-effect gaps.
- **rhetorical:**
  - **AUTH:** parliamentary and administrative sources establish bounded findings, not criminal guilt by status
  - **BF:** major beneficiary cases are not a prevalence estimate
  - **DEM:** the fund is a single French program, not evidence of a general counter-influence architecture
  - **FAC:** separate funding, selection, output, tasking, control, responsibility and effect
  - **NUM:** retain the unresolved 17-versus-18 beneficiary denominator
- **speaker:**
  - **goal:** forensic reconstruction of Fonds Marianne flows, governance, outputs and responsibility boundaries
  - **target:** financeur -> decisionnaire -> beneficiaire -> output -> control -> consequence
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **Κ:** 4
  - **Λ:** 4
  - **Ξ:** 4
  - **Σ:** 4
  - **Φ:** 4
  - **Ψ:** 4
  - **Ω:** 4
  - **κ:** 4
  - **ρ:** 5
  - **€:** 5
  - **↕:** 5
  - **⏰:** 4
  - **⚔:** 4
  - **⫸:** 4
  - **🌐:** 3
- **threats:**
  - funding=command
  - irregularity=corruption
  - political_content=state_order
  - investigation=guilt
  - spend=effect

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - final recovery amount/outcome and reconciled beneficiary denominator
  - **input_ids:**
    - FCT-001
    - FCT-003
    - FCT-011
    - FCT-016
    - FCT-029
    - FCT-036
  - **module:** clusters/MONEY.md
  - **negative_results:**
    - no evidence that funding itself establishes editorial command or political effect
  - **not_computable:**
    - complete transaction-level expenditure without underlying accounts
  - **operations_applied:**
    - reconstructed public funding flow
    - kept envelope, selected amount and beneficiary grants distinct
    - preserved 17/18 denominator contradiction
  - **reason:** the object is a public grant mechanism with a bounded envelope, beneficiary grants, payment tranches and recovery action
  - **result_ids:**
    - CLM-001
    - CLM-003
    - CTRL-001
  - **status:** DONE
  - **trigger:** €
- **item 2:**
  - **gaps:**
    - final judicial disposition
    - direct tasking records
  - **input_ids:**
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-009
    - FCT-023
    - FCT-025
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no final criminal guilt and no generalized political tasking established
  - **not_computable:**
    - undocumented informal instructions without records
  - **operations_applied:**
    - mapped cabinet and SG-CIPDR roles
    - separated selection intervention from editorial tasking and criminal intent
  - **reason:** cabinet, ministry and SG-CIPDR exercised design, selection and oversight authority requiring separation of lawful political impulse from improper tasking
  - **result_ids:**
    - CLM-002
    - CLM-005
    - CTRL-002
    - CTRL-005
  - **status:** DONE
  - **trigger:** ↕
- **item 3:**
  - **gaps:**
    - explicit editorial coordination or tasking chain
  - **input_ids:**
    - FCT-009
    - FCT-010
    - FCT-013
    - FCT-018
    - FCT-037
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no transversal coordinated censorship or beneficiary-command network established
  - **not_computable:**
    - private coordination absent records
  - **operations_applied:**
    - mapped cabinet-beneficiary access
    - tested proximity versus commitment/tasking
  - **reason:** selection and beneficiary relationships create access/proximity edges but network inference requires explicit coordination records
  - **result_ids:**
    - CLM-002
    - CLM-004
    - CTRL-003
  - **status:** DONE
  - **trigger:** 🌐
- **item 4:**
  - **gaps:**
    - tasking evidence
    - exposure-to-behavior causal chain
  - **input_ids:**
    - FCT-004
    - FCT-018
    - FCT-019
    - FCT-020
    - FCT-021
    - FCT-022
  - **module:** clusters/FRAMING.md
  - **negative_results:**
    - no state editorial order, generalized censorship or electoral causal effect established
  - **not_computable:**
    - individual exposure/persuasion absent audience-level design
  - **operations_applied:**
    - separated beneficiary output from state order
    - kept production, engagement, persuasion and electoral effect as distinct edges
  - **reason:** the program financed online counter-discourse and one beneficiary produced political content, so content provenance and downstream effect must be separated
  - **result_ids:**
    - CLM-004
    - CLM-006
    - CTRL-004
    - CTRL-006
    - CAU-001
  - **status:** DONE
  - **trigger:** Φ

### SCOPING_REPORT
- **domains:**
  - public subsidies
  - counter-discourse
  - administrative governance
  - beneficiary outputs
  - judicial follow-up
- **exclusions:**
  - funding as censorship by definition
  - allegation as guilt
  - political content as state tasking
  - expenditure as effect
- **geo:** France
- **lead_question:** Fonds Marianne et financement étatique de la contre-influence
- **object_coverage:** STRONG_FOR_STRUCTURE_AND_FAILURES; WEAK_FOR_TASKING_AND_CAUSAL_EFFECT
- **object_question:** Quels flux, sélections, bénéficiaires, livrables, contrôles et responsabilités sont établis, et où s’arrête la preuve de commandement éditorial ou effet politique?
- **period:** 2021-2026

### CREDO
- funding != command
- irregularity != corruption
- selection_failure != political_tasking
- beneficiary_output != state_editorial_control
- allegation != proof
- investigation != guilt
- public_funding != censorship
- expenditure != political_effect

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** RECHECK_EXTEND
- **patterns:**
  - funding
  - selection
  - beneficiary
  - output
  - control
  - accountability
- **priorities:**
  - trace financeur->decisionnaire->beneficiaire->livrable->controle->consequence
- **threats:**
  - proximity=guilt
  - funding=command
  - content=tasking
  - investigation=conviction

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** Le corpus documente des financements et des contenus politiques mais pas d’ordre éditorial étatique sur ces ciblages.
  - **resolution:** Séparer relation financière, critères conventionnels et tasking éditorial.
  - **thesis:** Financer un bénéficiaire signifie commander son contenu.
- **item 2:**
  - **antithesis:** Les dysfonctionnements sont établis, tandis que l’information judiciaire et un titre contesté ne constituent pas un jugement définitif.
  - **resolution:** Conclure à des défaillances de gouvernance; réserver la culpabilité pénale à une décision judiciaire.
  - **thesis:** Les irrégularités de sélection prouvent la corruption.
- **item 3:**
  - **antithesis:** Le suivi interne relevait un faible engagement pour Reconstruire le commun et aucun design causal électoral n’est disponible.
  - **resolution:** Effet général NOT_ESTABLISHED.
  - **thesis:** Le fonds a nécessairement eu un effet politique majeur.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **boundary:** 2025 ministry answer uses 18 retained
  - **from:** FIPD/Fonds Marianne
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
  - **to:** 17 selected associations per Senate
  - **vehicle:** public subsidy call
- **item 2:**
  - **boundary:** no pre-launch financial commitment established
  - **from:** Fonds Marianne
  - **support:**
    - FCT-011
    - FCT-012
  - **to:** USEPPM
  - **vehicle:** 355000 euro grant
- **item 3:**
  - **boundary:** political output not proven state-tasked
  - **from:** Fonds Marianne
  - **support:**
    - FCT-016
    - FCT-017
    - FCT-020
  - **to:** Reconstruire le commun
  - **vehicle:** 330000 euro grant

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** ministry cabinet
  - **limits:**
    - political involvement != editorial tasking
  - **relation:** impulsion, selection participation/intervention
  - **support:**
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-009
  - **to:** SG-CIPDR/Fonds Marianne
- **item 2:**
  - **from:** SG-CIPDR
  - **limits:**
    - denominator discrepancy preserved
  - **relation:** administration of grants and controls
  - **support:**
    - FCT-002
    - FCT-003
    - FCT-008
    - FCT-030
  - **to:** 17/18 beneficiary set
- **item 3:**
  - **from:** state funding
  - **limits:**
    - grant != proof of misuse or tasking
  - **relation:** subvention
  - **support:**
    - FCT-011
    - FCT-036
  - **to:** USEPPM
- **item 4:**
  - **from:** state funding
  - **limits:**
    - political output != state order
  - **relation:** subvention
  - **support:**
    - FCT-016
    - FCT-020
  - **to:** Reconstruire le commun

### IMPACT_MAP
- **audience_effect:** WEAK/PARTIAL
- **beneficiary_output:** VERIFIED case-specifically
- **electoral_effect:** NOT_ESTABLISHED
- **funding_capacity:** VERIFIED
- **persuasion:** NOT_ESTABLISHED
- **selection_influence:** VERIFIED
- **state_editorial_tasking:** NOT_ESTABLISHED
- **support:**
  - FCT-001
  - FCT-006
  - FCT-020
  - FCT-021
  - FCT-022

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** ministry response 2025: 18 retained
  - **issue:** beneficiary denominator
  - **pro:** Sénat: 17 associations
  - **resolution:** UNRESOLVED_DENOMINATOR; do not silently harmonize
  - **support:**
    - FCT-002
    - FCT-032
- **item 2:**
  - **contra:** no state editorial order or convention condition demonstrating tasking is established
  - **issue:** political content versus state tasking
  - **pro:** political personalities/candidates were targeted in beneficiary output
  - **resolution:** output ESTABLISHED; state tasking NOT_ESTABLISHED
  - **support:**
    - FCT-018
    - FCT-019
    - FCT-020
    - FCT-023
- **item 3:**
  - **contra:** current corpus lacks final criminal adjudication
  - **issue:** governance failure versus criminal guilt
  - **pro:** selection/control failures, IGA and PNF procedure documented
  - **resolution:** administrative/political responsibility evidence stronger than criminal culpability evidence
  - **support:**
    - FCT-025
    - FCT-034
    - FCT-035

### VERIFICATION_REPORT
- **circular_families:**
  - multiple Senate pages are one provenance family A; Le Monde articles one family E
- **contradiction_ids:**
  - beneficiary-denominator-17-vs-18
  - political-output-vs-state-tasking
  - governance-failure-vs-criminal-guilt
- **downgraded_ids:**
  - NONE
- **none_found_claims:**
  - state editorial order to target political opponents
  - general censorship architecture
  - general electoral causal effect
  - final criminal guilt in current corpus
- **remaining_gaps:**
  - beneficiary denominator reconciliation
  - final judicial disposition
  - tasking records
  - audience/persuasion/electoral causal chain
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
  - FCT-034
  - FCT-035
  - FCT-036
  - FCT-037
- **sources_reopened:** 12
- **upgraded_ids:**
  - NONE
- **verdict:** READY_FOR_PRE_GATE

### EDI_REPORT
- **corpus:**
  - **circularity:** multiple Senate pages are one provenance family A; Le Monde reports are one secondary family E
  - **coverage:** STRONG structural/governance; WEAK causal effect
  - **independence:** MULTIPLE_PRIMARY_AND_SECONDARY_FAMILIES
  - **limits:**
    - 17 versus 18 beneficiary denominator unresolved
    - no final criminal adjudication established in current corpus
    - no direct state editorial tasking record
    - no audience-to-vote causal design
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES_PRIMARY_FUNDING_RECORDS
    - **gap_type:** SCOPE
    - **independent_families:** 3
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES_PARLIAMENTARY_SELECTION_FINDINGS
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 1
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** YES_BENEFICIARY_GRANTS_AND_CONTROL
    - **gap_type:** NONE
    - **independent_families:** 3
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** YES_OUTPUT_NO_TASKING_EDGE
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 1
  - **item 5:**
    - **claim_id:** CLM-005
    - **direct_object:** YES_REMEDIATION_STATUS
    - **gap_type:** LEGAL_STATUS
    - **independent_families:** 4
  - **item 6:**
    - **claim_id:** CLM-006
    - **direct_object:** BOUNDARY_ONLY
    - **gap_type:** CAUSALITY
    - **independent_families:** 2
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** 6_PROVENANCE_FAMILIES
  - **perspective:** SENATE+INTERIOR+ASSEMBLY+COUR_DES_COMPTES_PUBLICATION+MEDIA_JUDICIAL_STATUS
  - **stratification:** FUNDING+SELECTION+OUTPUT+TASKING+CONTROL+RESPONSIBILITY+EFFECT
  - **temporal:** 2021-2025 public follow-up; as-of 2026-09-08
- **edi:**
  - **assessment:** STRONG_FOR_FUNDING_SELECTION_AND_CONTROL_FAILURES; MODERATE_FOR_RESPONSIBILITY; WEAK_FOR_EDITORIAL_TASKING_AND_POLITICAL_EFFECT
  - **flags:**
    - PARLIAMENTARY_PRIMARY
    - ADMINISTRATIVE_FOLLOWUP
    - JUDICIAL_STATUS_SECONDARY
    - DENOMINATOR_CONTRADICTION
- **source_counts:**
  - **primary:** 9
  - **provenance_families:** 6
  - **secondary:** 3
  - **tertiary:** 0
  - **total:** 12

### RESPONSIBILITY_MAP
- **boundary:** political/administrative responsibility and criminal responsibility are separate.
- **not_established:**
  - final criminal guilt of named persons
  - state order to target political opponents editorially
  - general censorship architecture
  - electoral causal effect
- **verified:**
  - cabinet role in accelerated/opaque process
  - SG-CIPDR control failures
  - beneficiary-specific performance/compliance problems
  - administrative remediation

### NEXT_QUERIES
- RECHECK final judicial disposition only if a primary PNF/court record becomes public
- RECHECK execution/result of USEPPM recovery title
- RECHECK 17-versus-18 denominator from administrative grant list
- DEFER generalized censorship/electoral-effect claims absent tasking and causal evidence

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-005 | support:- | counter:- | results:FCT-004,FCT-005,FCT-006,FCT-007,FCT-023 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-003,QRY-004,QRY-012 | support:- | counter:- | results:FCT-009,FCT-010,FCT-011,FCT-016,FCT-017,FCT-020 | final:SATURATED | gap:NONE
LED-003 | attempts:QRY-008,QRY-009,QRY-010,QRY-011 | support:- | counter:- | results:FCT-028,FCT-029,FCT-030,FCT-031,FCT-034,FCT-035 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-001,QRY-003,QRY-012 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-011,FCT-016,FCT-036 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-002,QRY-003 | support:- | counter:- | results:FCT-005,FCT-006,FCT-007,FCT-009,FCT-010,FCT-012 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-002,QRY-003,QRY-004,QRY-008,QRY-012 | support:- | counter:- | results:FCT-008,FCT-017,FCT-020,FCT-021,FCT-022,FCT-028,FCT-036 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-002,QRY-003,QRY-004 | support:- | counter:- | results:FCT-018,FCT-019,FCT-020,FCT-023 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011 | support:- | counter:- | results:FCT-025,FCT-026,FCT-027,FCT-029,FCT-030,FCT-031,FCT-033,FCT-034,FCT-035 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-001,QRY-004 | support:- | counter:- | results:FCT-020,FCT-021,FCT-022 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,SRC-001 | support:FCT-001,FCT-002,FCT-003,FCT-004 | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-002,QRY-003,QRY-005,SRC-002,SRC-003,SRC-005 | support:FCT-005,FCT-006,FCT-007,FCT-009,FCT-012,FCT-023 | counter:FCT-010 | results:FCT-005,FCT-006,FCT-007,FCT-009,FCT-012,FCT-023,FCT-010 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-003 | attempts:QRY-002,QRY-003,QRY-004,QRY-008,QRY-012,SRC-002,SRC-003,SRC-004,SRC-008,SRC-012 | support:FCT-008,FCT-017,FCT-020,FCT-021,FCT-022,FCT-028,FCT-036 | counter:- | results:FCT-008,FCT-017,FCT-020,FCT-021,FCT-022,FCT-028,FCT-036 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-003,QRY-004,QRY-005,SRC-003,SRC-004,SRC-005 | support:FCT-018,FCT-019,FCT-020 | counter:FCT-023 | results:FCT-018,FCT-019,FCT-020,FCT-023 | final:PARTIAL | gap:RESPONSIBILITY
CLM-005 | attempts:QRY-006,QRY-007,QRY-008,QRY-010,QRY-011,SRC-006,SRC-007,SRC-008,SRC-010,SRC-011 | support:FCT-025,FCT-026,FCT-027,FCT-029,FCT-030,FCT-031,FCT-034,FCT-035 | counter:- | results:FCT-025,FCT-026,FCT-027,FCT-029,FCT-030,FCT-031,FCT-034,FCT-035 | final:SUPPORTED | gap:LEGAL_STATUS
CLM-006 | attempts:QRY-004,QRY-005,SRC-004,SRC-005 | support:FCT-021,FCT-022,FCT-023 | counter:- | results:FCT-021,FCT-022,FCT-023 | final:SUPPORTED | gap:CAUSALITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-002 | CLM | SUPPORTED | RESPONSIBILITY | L’implication et l’opacité n’établissent pas à elles seules favoritisme pénal ou corruption.
CLM-004 | CLM | PARTIAL | RESPONSIBILITY | Aucun ordre, brief éditorial ou validation étatique du ciblage politique n’est établi dans les sources examinées.
CLM-005 | CLM | SUPPORTED | LEGAL_STATUS | Le corpus courant ne permet pas d’établir une responsabilité pénale définitive des personnes visées.
CLM-006 | CLM | SUPPORTED | CAUSALITY | Pas de chaîne exposition -> persuasion -> comportement -> résultat, ni de tasking éditorial transversal.
CAU-001 | CAU | GAP | CAUSALITY | No evidence chain identifies state tasking of political targeting or exposure-to-vote causal effect.

SEMANTIC_COUNTS_V1:LED:3|CLM:6|AXS:6|CAU:1|CTRL:6|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-005"],"evidence_excerpt":"délai réduit, présélection, intervention après comité, recommandation d’interdire l’interférence du cabinet.","kind":"MECHANISM_LEAD","lead":"Le Fonds Marianne établit un mécanisme de délégation publique de contre-discours avec implication politique dans le design et la sélection, mais cela ne suffit pas à prouver un commandement éditorial sur les contenus.","linked_ids":["FCT-004","FCT-005","FCT-006","FCT-007","FCT-023"],"locator":"sélection et suivi","materiality":"DECISIVE","result_ids":["FCT-004","FCT-005","FCT-006","FCT-007","FCT-023"],"routes":["VERIFY","POWER","MONEY"],"source_id":"SRC-002","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-003","QRY-004","QRY-012"],"evidence_excerpt":"355k USEPPM; 330k Reconstruire; political content documented; tasking not documented.","kind":"RESPONSIBILITY_LEAD","lead":"Les deux plus grosses subventions concentrent des risques différents: proximité et amont de sélection pour l’USEPPM, capacité faible et contenus politiques pour Reconstruire le commun.","linked_ids":["FCT-009","FCT-010","FCT-011","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020"],"locator":"USEPPM + Reconstruire le commun","materiality":"DECISIVE","result_ids":["FCT-009","FCT-010","FCT-011","FCT-016","FCT-017","FCT-020"],"routes":["VERIFY","NETWORK","FRAMING"],"source_id":"SRC-003","status":"SATURATED"}
LED-003 | {"attempt_ids":["QRY-008","QRY-009","QRY-010","QRY-011"],"evidence_excerpt":"titre de perception contesté; nouveaux contrôles; instruction pénale ouverte/en cours.","kind":"CONTROL_LEAD","lead":"Les suites administratives sont observables: récupération contestée, refonte de la sélection, renforcement des contrôles et des équipes; la responsabilité pénale finale reste une arête séparée.","linked_ids":["FCT-028","FCT-029","FCT-030","FCT-031","FCT-034","FCT-035"],"locator":"réponse publiée le 3 juin 2025","materiality":"IMPORTANT","result_ids":["FCT-028","FCT-029","FCT-030","FCT-031","FCT-034","FCT-035"],"routes":["VERIFY","ACCOUNTABILITY"],"source_id":"SRC-008","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Le Fonds Marianne constitue un mécanisme documenté de financement public de contre-discours associatif en ligne.","claimant":"INV-078","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-004"]}
CLM-002 | {"claim":"La procédure de sélection a connu des dysfonctionnements substantiels et une implication du cabinet ministériel dépassant une simple impulsion politique abstraite.","claimant":"INV-078","counter":["FCT-010"],"gap":"L’implication et l’opacité n’établissent pas à elles seules favoritisme pénal ou corruption.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-005","FCT-006","FCT-007","FCT-009","FCT-012","FCT-023"]}
CLM-003 | {"claim":"Les deux principaux dossiers problématiques montrent des défaillances de sélection, capacité et suivi, avec des contrôles tardifs et des engagements non entièrement tenus.","claimant":"INV-078","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-008","FCT-017","FCT-020","FCT-021","FCT-022","FCT-028","FCT-036"]}
CLM-004 | {"claim":"Des contenus politiques visant des personnalités ou candidats ont été produits par Reconstruire le commun, mais le corpus ne démontre pas que l’État ait commandé ces ciblages éditoriaux.","claimant":"INV-078","counter":["FCT-023"],"gap":"Aucun ordre, brief éditorial ou validation étatique du ciblage politique n’est établi dans les sources examinées.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-018","FCT-019","FCT-020"]}
CLM-005 | {"claim":"Des mécanismes de responsabilité et de correction ont été activés: inspections, démission administrative, récupération contestée, réformes de contrôle et information judiciaire.","claimant":"INV-078","counter":"NONE_FOUND","gap":"Le corpus courant ne permet pas d’établir une responsabilité pénale définitive des personnes visées.","gap_type":"LEGAL_STATUS","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-025","FCT-026","FCT-027","FCT-029","FCT-030","FCT-031","FCT-034","FCT-035"]}
CLM-006 | {"claim":"Le Fonds Marianne ne permet pas, sur le corpus courant, de démontrer un effet électoral causal général ni une architecture générale de censure ou de commandement éditorial par l’État.","claimant":"INV-078","counter":"NONE_FOUND","gap":"Pas de chaîne exposition -> persuasion -> comportement -> résultat, ni de tasking éditorial transversal.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-021","FCT-022","FCT-023"]}

### AXIS_REGISTRY_V1
AXS-001 | {"assessment":"VERIFIED for program envelope and major grants; denominator 17/18 discrepancy preserved.","attempt_ids":["QRY-001","QRY-003","QRY-012"],"axis":"PUBLIC_FUNDING_FLOW","links":["FCT-001","FCT-002","FCT-003","FCT-011","FCT-016","FCT-036"],"question":"Quels crédits publics ont été fléchés, attribués et vers quels bénéficiaires?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-011","FCT-016","FCT-036"],"sought_objects":["enveloppe","bénéficiaires","montants","tranches"],"status":"SATURATED"}
AXS-002 | {"assessment":"FAILURES_ESTABLISHED; political involvement documented, but corrupt intent not established by procedure alone.","attempt_ids":["QRY-002","QRY-003"],"axis":"SELECTION_GOVERNANCE","links":["FCT-005","FCT-006","FCT-007","FCT-009","FCT-010","FCT-012"],"question":"La sélection a-t-elle suivi une procédure robuste, équitable et traçable?","result_ids":["FCT-005","FCT-006","FCT-007","FCT-009","FCT-010","FCT-012"],"sought_objects":["délai","instruction","présélection","cabinet","arbitrage"],"status":"SATURATED"}
AXS-003 | {"assessment":"MATERIAL_CONTROL_FAILURES_ESTABLISHED case-specifically.","attempt_ids":["QRY-002","QRY-003","QRY-004","QRY-008","QRY-012"],"axis":"BENEFICIARY_OUTPUT_AND_CONTROL","links":["FCT-008","FCT-017","FCT-020","FCT-021","FCT-022","FCT-028","FCT-036"],"question":"Les prestations, livrables et contrôles ont-ils été adéquats?","result_ids":["FCT-008","FCT-017","FCT-020","FCT-021","FCT-022","FCT-028","FCT-036"],"sought_objects":["contenus","engagement","pièces","suivi","tranches"],"status":"SATURATED"}
AXS-004 | {"assessment":"NOT_ESTABLISHED: political content is documented, direct state editorial tasking is not.","attempt_ids":["QRY-002","QRY-003","QRY-004"],"axis":"EDITORIAL_TASKING","links":["FCT-018","FCT-019","FCT-020","FCT-023"],"question":"Les contenus politiques produits ont-ils été commandés ou validés par l’État?","result_ids":["FCT-018","FCT-019","FCT-020","FCT-023"],"sought_objects":["instruction éditoriale","brief","validation contenu","tasking"],"status":"SATURATED"}
AXS-005 | {"assessment":"VERIFIED administrative/parliamentary follow-up; final criminal responsibility NOT_ESTABLISHED in current corpus.","attempt_ids":["QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011"],"axis":"ACCOUNTABILITY_AND_REMEDIATION","links":["FCT-025","FCT-026","FCT-027","FCT-029","FCT-030","FCT-031","FCT-033","FCT-034","FCT-035"],"question":"Quelles corrections administratives, financières, parlementaires ou judiciaires ont suivi?","result_ids":["FCT-025","FCT-026","FCT-027","FCT-029","FCT-030","FCT-031","FCT-033","FCT-034","FCT-035"],"sought_objects":["IGA","démission","titre perception","réformes","PNF"],"status":"SATURATED"}
AXS-006 | {"assessment":"NOT_ESTABLISHED generally; weak engagement is evidence against assuming large effect.","attempt_ids":["QRY-001","QRY-004"],"axis":"POLITICAL_EFFECT","links":["FCT-004","FCT-020","FCT-021","FCT-022"],"question":"Les financements ou contenus ont-ils produit un effet politique ou électoral mesurable?","result_ids":["FCT-020","FCT-021","FCT-022"],"sought_objects":["audience","persuasion","vote","policy effect"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":["FCT-022","FCT-023"],"gap":"No evidence chain identifies state tasking of political targeting or exposure-to-vote causal effect.","gap_type":"CAUSALITY","limit":"Funding, selection and some outputs are directly observable; state editorial tasking and downstream persuasion/electoral effect are not identified.","mechanism":"public funds -> selection/governance -> beneficiary capacity -> content production -> exposure -> persuasion/behavior -> political or electoral effect","status":"GAP","support":["FCT-001","FCT-011","FCT-016","FCT-020","FCT-021"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"funding != editorial_command","status":"VERIFIED","support":["FCT-001","FCT-004","FCT-020"]}
CTRL-002 | {"control":"selection_failure != corruption","status":"VERIFIED","support":["FCT-005","FCT-006","FCT-012","FCT-034"]}
CTRL-003 | {"control":"beneficiary_political_output != state_tasking","status":"VERIFIED","support":["FCT-018","FCT-019","FCT-020","FCT-023"]}
CTRL-004 | {"control":"investigation != guilt","status":"VERIFIED","support":["FCT-034","FCT-035"]}
CTRL-005 | {"control":"administrative_reform != admission_of_criminal_liability","status":"VERIFIED","support":["FCT-030","FCT-031"]}
CTRL-006 | {"control":"expenditure != political_effect","status":"VERIFIED","support":["FCT-003","FCT-016","FCT-021"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:12|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL:MNEMO_UNAVAILABLE | mnemo | NONE | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | OK | SRC-001 | https://www.senat.fr/rap/r22-829-1/r22-829-12.html | FETCH Sénat introduction fonds Marianne enveloppe associations
QRY-002 | FETCH | OK | SRC-002 | https://www.senat.fr/travaux-parlementaires/commissions/commission-des-finances/controle-en-clair/commission-denquete-sur-le-fonds-marianne.html | FETCH Sénat contrôle en clair Fonds Marianne conclusions
QRY-003 | FETCH | OK | SRC-003 | https://www.senat.fr/rap/r22-829-1/r22-829-15.html | FETCH Sénat rapport USEPPM sélection 355000
QRY-004 | FETCH | OK | SRC-004 | https://www.senat.fr/rap/r22-829-1/r22-829-17.html | FETCH Sénat rapport suivi Reconstruire le commun contenus politiques
QRY-005 | FETCH | OK | SRC-005 | https://www.senat.fr/rap/r22-829-1/r22-829-11.html | FETCH Sénat recommandations fonds Marianne
QRY-006 | FETCH | OK | SRC-006 | https://www.interieur.gouv.fr/actualites/communiques-de-presse/publication-du-rapport-de-liga-relatif-a-subvention-versee-a | FETCH Ministère Intérieur premier rapport IGA Fonds Marianne USEPPM
QRY-007 | FETCH | OK | SRC-007 | https://www.interieur.gouv.fr/actualites/communiques-de-presse/publication-du-second-rapport-de-liga-relatif-au-fonds-marianne | FETCH Ministère Intérieur second rapport IGA Fonds Marianne
QRY-008 | FETCH | OK | SRC-008 | https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE1083 | FETCH Assemblée nationale question 1083 Fonds Marianne réponse 2025
QRY-009 | FETCH | OK | SRC-009 | https://ccomptes.fr/fr/publications?at1=42FE2FE25C25A25E311231122FA2FE310C310C31022D310&at2=13885&at3=CFEF5115B18BAEBC3069C2FA42F35C03&at4=ZagsOhsFc2kDggyoKnSm8Zfyr6OcelWs&f%5B0%5D=daterange%3A2024&items_per_page=10&page=7&v=2 | FETCH Cour des comptes publication SG-CIPDR 2024
QRY-010 | FETCH | OK | SRC-010 | https://www.lemonde.fr/societe/article/2023/05/04/fonds-marianne-une-information-judiciaire-ouverte-notamment-pour-detournement-de-fonds-et-abus-de-confiance_6172130_3224.html | FETCH Le Monde information judiciaire Fonds Marianne PNF mai 2023
QRY-011 | FETCH | OK | SRC-011 | https://www.lemonde.fr/societe/article/2024/03/04/la-cour-des-comptes-severe-avec-le-comite-interministeriel-de-prevention-de-la-delinquance-et-de-la-radicalisation_6220002_3224.html | FETCH Le Monde Cour comptes CIPDR instruction Fonds Marianne 2024
QRY-012 | FETCH | OK | SRC-012 | https://www.publicsenat.fr/actualites/politique/fonds-marianne-ce-qua-revele-laudition-tres-tendue-de-mohamed-sifaoui | FETCH Public Sénat audition Sifaoui Fonds Marianne

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | SENAT-R22-829-INTRO | Sénat — Rapport n°829, introduction et périmètre financier | 2023-07-04 | 2026-09-08T07:03:00+02:00 | enveloppe 2,5 M€; 17 associations; 2,017 M€ sélectionnés | https://www.senat.fr/rap/r22-829-1/r22-829-12.html
SRC-002 | ◈ | fam:A | SENAT-FM-CONTROLE | Sénat — Commission d’enquête Fonds Marianne, constats et recommandations | 2023-07-06 | 2026-09-08T07:03:00+02:00 | délais, présélection, intervention politique, suivi | https://www.senat.fr/travaux-parlementaires/commissions/commission-des-finances/controle-en-clair/commission-denquete-sur-le-fonds-marianne.html
SRC-003 | ◈ | fam:A | SENAT-R22-829-BENEF | Sénat — Rapport n°829, USEPPM et Reconstruire le commun | 2023-07-04 | 2026-09-08T07:03:00+02:00 | rendez-vous, 355000, 330000, capacités et garanties | https://www.senat.fr/rap/r22-829-1/r22-829-15.html
SRC-004 | ◈ | fam:A | SENAT-R22-829-SUIVI | Sénat — Rapport n°829, contrôle et contenus de Reconstruire le commun | 2023-07-04 | 2026-09-08T07:03:00+02:00 | contenus politiques, faible engagement, contrôle tardif | https://www.senat.fr/rap/r22-829-1/r22-829-17.html
SRC-005 | ◈ | fam:A | SENAT-R22-829-RECO | Sénat — Rapport n°829, douze recommandations | 2023-07-04 | 2026-09-08T07:03:00+02:00 | contrôles, objectifs, cabinet ministériel | https://www.senat.fr/rap/r22-829-1/r22-829-11.html
SRC-006 | ◈ | fam:B | INT-IGA-FM-1 | Ministère de l’Intérieur — Publication du rapport IGA sur l’USEPPM | 2023-06-06 | 2026-09-08T07:03:00+02:00 | rapport IGA; démission Christian Gravel; recommandations | https://www.interieur.gouv.fr/actualites/communiques-de-presse/publication-du-rapport-de-liga-relatif-a-subvention-versee-a
SRC-007 | ◈ | fam:B | INT-IGA-FM-2 | Ministère de l’Intérieur — Publication du second rapport IGA Fonds Marianne | 2023-07-06 | 2026-09-08T07:03:00+02:00 | ensemble des subventions 2021 | https://www.interieur.gouv.fr/actualites/communiques-de-presse/publication-du-second-rapport-de-liga-relatif-au-fonds-marianne
SRC-008 | ◈ | fam:C | AN-QE-1083 | Assemblée nationale — Question écrite n°1083 et réponse du ministère de l’Intérieur | 2025-06-03 | 2026-09-08T07:03:00+02:00 | récupération USEPPM; mesures 2024-2025; dénominateur administratif | https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE1083
SRC-009 | ◈ | fam:D | CDC-SGCIPDR-2024 | Cour des comptes — Publication sur le SG-CIPDR | 2024-03-04 | 2026-09-08T07:03:00+02:00 | publication d’observations définitives sur le SG-CIPDR | https://ccomptes.fr/fr/publications?at1=42FE2FE25C25A25E311231122FA2FE310C310C31022D310&at2=13885&at3=CFEF5115B18BAEBC3069C2FA42F35C03&at4=ZagsOhsFc2kDggyoKnSm8Zfyr6OcelWs&f%5B0%5D=daterange%3A2024&items_per_page=10&page=7&v=2
SRC-010 | ○ | fam:E | LM-FM-PNF-2023 | Le Monde — Information judiciaire ouverte sur le Fonds Marianne | 2023-05-04 | 2026-09-08T07:03:00+02:00 | PNF; détournement fonds publics; abus confiance; prise illégale intérêts | https://www.lemonde.fr/societe/article/2023/05/04/fonds-marianne-une-information-judiciaire-ouverte-notamment-pour-detournement-de-fonds-et-abus-de-confiance_6172130_3224.html
SRC-011 | ○ | fam:E | LM-CIPDR-CDC-2024 | Le Monde — Cour des comptes sévère avec le SG-CIPDR | 2024-03-04 | 2026-09-08T07:03:00+02:00 | instruction Fonds Marianne encore en cours; gouvernance SG-CIPDR | https://www.lemonde.fr/societe/article/2024/03/04/la-cour-des-comptes-severe-avec-le-comite-interministeriel-de-prevention-de-la-delinquance-et-de-la-radicalisation_6220002_3224.html
SRC-012 | ○ | fam:other:public-senat | PS-FM-SIFAOUI-2023 | Public Sénat — Audition de Mohamed Sifaoui | 2023-06-15 | 2026-09-08T07:03:00+02:00 | seconde tranche; contrat consultant CIPDR | https://www.publicsenat.fr/actualites/politique/fonds-marianne-ce-qua-revele-laudition-tres-tendue-de-mohamed-sifaoui

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.senat.fr/rap/r22-829-1/r22-829-12.html | A | 2026-09-08 | Enveloppe annoncée du Fonds Marianne | Le rapport sénatorial indique que le Fonds Marianne disposait d’une enveloppe totale de 2,5 millions d’euros en 2021. | -
FCT-002 | FACT | ✧ | https://www.senat.fr/rap/r22-829-1/r22-829-12.html | A | 2026-09-08 | Sélection de 17 associations | Le rapport sénatorial indique que l’appel à projets a abouti à la sélection de 17 associations. | -
FCT-003 | FACT | ✧ | https://www.senat.fr/rap/r22-829-1/r22-829-12.html | A | 2026-09-08 | Montant total sélectionné | Les 17 associations sélectionnées bénéficiaient d’une enveloppe totale de 2,017 millions d’euros selon le rapport du Sénat. | -
FCT-004 | FACT | ✧ | https://www.senat.fr/rap/r22-829-1/r22-829-12.html | A | 2026-09-08 | Objet du Fonds Marianne | Le Fonds Marianne visait à compléter le contre-discours institutionnel par des actions de la société civile sur internet pour défendre les valeurs républicaines et combattre les discours séparatistes. | -
FCT-005 | FACT | ✧ | https://www.senat.fr/travaux-parlementaires/commissions/commission-des-finances/controle-en-clair/commission-denquete-sur-le-fonds-marianne.html | A | 2026-09-08 | Délai de candidature réduit | La commission d’enquête du Sénat conclut que le cabinet a réduit de deux mois à trois semaines le délai de l’appel à projets, limitant le temps disponible pour construire les dossiers. | -
FCT-006 | FACT | ✧ | https://www.senat.fr/travaux-parlementaires/commissions/commission-des-finances/controle-en-clair/commission-denquete-sur-le-fonds-marianne.html | A | 2026-09-08 | Présélection de plusieurs associations | Le Sénat conclut que plusieurs associations avaient en réalité été présélectionnées avant le comité de sélection du 21 mai 2021. | -
FCT-007 | FACT | ✧ | https://www.senat.fr/travaux-parlementaires/commissions/commission-des-finances/controle-en-clair/commission-denquete-sur-le-fonds-marianne.html | A | 2026-09-08 | Intervention ministérielle après le comité | Le Sénat indique que plusieurs jours après le comité de sélection, la ministre déléguée a décidé de revenir sur le choix d’attribuer une subvention à une association. | -
FCT-008 | FACT | ✧ | https://www.senat.fr/travaux-parlementaires/commissions/commission-des-finances/controle-en-clair/commission-denquete-sur-le-fonds-marianne.html | A | 2026-09-08 | Contrôles tardifs sur deux bénéficiaires | Le Sénat relève que des problèmes majeurs dans les productions de l’USEPPM et de Reconstruire le commun étaient visibles dès le début de 2022, mais que les contrôles sur pièces n’ont été engagés qu’en 2023. | -
FCT-009 | FACT | ✧ | https://www.senat.fr/rap/r22-829-1/r22-829-15.html | A | 2026-09-08 | Rencontres cabinet-Sifaoui avant lancement | La mission sénatoriale établit au moins trois rendez-vous entre Mohamed Sifaoui et le cabinet ministériel en mars et avril 2021, avant ou autour du lancement du fonds. | -
FCT-010 | FACT | ✧ | https://www.senat.fr/rap/r22-829-1/r22-829-15.html | A | 2026-09-08 | Encouragement à déposer sans promesse financière établie | Le Sénat estime probable qu’un financement de contre-discours ait été évoqué avec Mohamed Sifaoui et qu’il ait été encouragé à candidater, mais conclut qu’aucun engagement financier n’est établi à ce stade. | -
FCT-011 | FACT | ✧ | https://www.senat.fr/rap/r22-829-1/r22-829-15.html | A | 2026-09-08 | Subvention USEPPM de 355000 euros | Le comité de sélection du 21 mai 2021 a attribué 355 000 euros à l’USEPPM. | -
FCT-012 | FACT | ✧ | https://www.senat.fr/rap/r22-829-1/r22-829-15.html | A | 2026-09-08 | Zone d’ombre sur le passage de 300000 à 355000 euros | Le rapport sénatorial décrit comme difficile à démêler le passage d’un arbitrage antérieur de 300 000 euros à la subvention finale de 355 000 euros. | -
FCT-013 | FACT | ✧ | https://www.senat.fr/rap/r22-829-1/r22-829-15.html | A | 2026-09-08 | USEPPM conçue comme pièce maîtresse | Le rapport sénatorial indique que le projet USEPPM a rapidement été considéré par le cabinet et le SG-CIPDR comme une pièce maîtresse ou un vaisseau amiral du Fonds Marianne. | -
FCT-014 | FACT | ✧ | https://www.senat.fr/rap/r22-829-1/r22-829-15.html | A | 2026-09-08 | Reconstruire le commun créée en octobre 2020 | Reconstruire le commun avait été constituée le 29 octobre 2020, moins d’un an avant l’attribution du Fonds Marianne. | -
FCT-015 | FACT | ✧ | https://www.senat.fr/rap/r22-829-1/r22-829-15.html | A | 2026-09-08 | Première subvention de 39000 euros | Reconstruire le commun avait reçu une première subvention de 39 000 euros en décembre 2020 pour accompagner son lancement. | -
FCT-016 | FACT | ✧ | https://www.senat.fr/rap/r22-829-1/r22-829-15.html | A | 2026-09-08 | Subvention Fonds Marianne de 330000 euros | Reconstruire le commun a reçu une subvention de 330 000 euros au titre du Fonds Marianne. | -
FCT-017 | FACT | ✧ | https://www.senat.fr/rap/r22-829-1/r22-829-15.html | A | 2026-09-08 | Doutes internes sur la capacité de gestion | Des courriels internes cités par le Sénat exprimaient dès juin 2021 des doutes sur la capacité technique et financière de Reconstruire le commun à gérer 330 000 euros, notamment en l’absence de personnel salarié prévu. | -
FCT-018 | FACT | ✧ | https://www.senat.fr/rap/r22-829-1/r22-829-15.html | A | 2026-09-08 | Antécédents de contenus politiques connus | Le rapport indique que le SG-CIPDR connaissait la proximité de Reconstruire le commun avec le collectif On vous voit et le fait que ce collectif avait parfois diffusé des contenus politiques. | -
FCT-019 | FACT | ✧ | https://www.senat.fr/rap/r22-829-1/r22-829-15.html | A | 2026-09-08 | Condition d’absence de contenu politique non retrouvée dans la convention Marianne | Le Sénat n’a trouvé dans les documents transmis aucun élément attestant, pour la convention Fonds Marianne, d’une condition d’absence de messages politiques analogue à celle évoquée pour la première subvention. | -
FCT-020 | FACT | ✧ | https://www.senat.fr/rap/r22-829-1/r22-829-17.html | A | 2026-09-08 | Contenus visant des personnalités et candidats | Une note interne citée par le Sénat indiquait que certains épisodes produits par Reconstruire le commun ciblaient explicitement des personnalités politiques, parfois des candidats aux élections. | -
FCT-021 | FACT | ✧ | https://www.senat.fr/rap/r22-829-1/r22-829-17.html | A | 2026-09-08 | Faible engagement identifié | Le suivi interne relevait un faible taux d’engagement pour les productions de Reconstruire le commun. | -
FCT-022 | FACT | ✧ | https://www.senat.fr/rap/r22-829-1/r22-829-17.html | A | 2026-09-08 | Contrôle qualitatif jugé insuffisant | Compte tenu de la subvention de 330 000 euros et des signaux disponibles, le Sénat juge difficilement compréhensible que les productions n’aient pas été examinées plus en détail avant les révélations médiatiques de mars 2023. | -
FCT-023 | FACT | ✧ | https://www.senat.fr/rap/r22-829-1/r22-829-11.html | A | 2026-09-08 | Recommandation contre l’interférence du cabinet | La recommandation n°12 du Sénat propose d’interdire toute interférence du cabinet ministériel dans l’instruction des demandes de subvention et de tracer par écrit toute intervention ultérieure du ministre ou de son cabinet. | -
FCT-024 | FACT | ✧ | https://www.senat.fr/rap/r22-829-1/r22-829-11.html | A | 2026-09-08 | Recommandations sur objectifs et contrôles | Le Sénat recommande de préciser les objectifs quantitatifs des conventions, renforcer les restitutions et consolider les moyens de contrôle financier. | -
FCT-025 | FACT | ✧ | https://www.interieur.gouv.fr/actualites/communiques-de-presse/publication-du-rapport-de-liga-relatif-a-subvention-versee-a | B | 2026-09-08 | Premier rapport IGA et démission de Christian Gravel | Après le premier rapport de l’IGA sur la subvention USEPPM, Christian Gravel a remis sa démission de secrétaire général du CIPDR, qui a été acceptée. | -
FCT-026 | FACT | ✧ | https://www.interieur.gouv.fr/actualites/communiques-de-presse/publication-du-rapport-de-liga-relatif-a-subvention-versee-a | B | 2026-09-08 | Engagement ministériel de mise en œuvre des recommandations IGA | Le ministère de l’Intérieur a annoncé que la totalité des recommandations du premier rapport IGA serait mise en œuvre. | -
FCT-027 | FACT | ✧ | https://www.interieur.gouv.fr/actualites/communiques-de-presse/publication-du-second-rapport-de-liga-relatif-au-fonds-marianne | B | 2026-09-08 | Second rapport IGA sur l’ensemble des subventions | Le second rapport de l’IGA, remis fin juin 2023 et publié le 6 juillet, porte sur l’ensemble des subventions versées en 2021 dans le cadre du Fonds Marianne. | -
FCT-028 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE1083 | C | 2026-09-08 | Réponse 2025: deux associations n’ont pas tenu tous leurs engagements | Dans sa réponse parlementaire publiée le 3 juin 2025, le ministère de l’Intérieur indique que deux associations lauréates n’ont pas tenu l’ensemble des engagements prévus par leurs conventions. | -
FCT-029 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE1083 | C | 2026-09-08 | Réponse 2025: titre de perception contre l’USEPPM contesté | Le ministère indique qu’un titre de perception a été émis contre l’USEPPM et que l’association en conteste les éléments. | -
FCT-030 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE1083 | C | 2026-09-08 | Réponse 2025: renforcement de la sélection | Le ministère indique qu’en 2024 un comité de programmation a sélectionné les dossiers, avec expertise par les services instructeurs et des experts extérieurs et vérification de la présence des documents requis. | -
FCT-031 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE1083 | C | 2026-09-08 | Réponse 2025: renforcement organisationnel et contrôle | Le ministère indique que plusieurs mesures de sécurisation ont été engagées en 2024, avec création d’un secrétariat général, recrutement d’un administrateur de l’État en septembre 2024 et renforcement des équipes prévu d’ici mi-2025. | -
FCT-032 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE1083 | C | 2026-09-08 | Divergence de dénominateur 17 versus 18 | La réponse ministérielle de 2025 parle de 18 structures retenues, alors que le rapport sénatorial de 2023 en dénombre 17; cette divergence de dénominateur n’est pas résolue par le corpus courant. | -
FCT-033 | FACT | ✧ | https://ccomptes.fr/fr/publications?at1=42FE2FE25C25A25E311231122FA2FE310C310C31022D310&at2=13885&at3=CFEF5115B18BAEBC3069C2FA42F35C03&at4=ZagsOhsFc2kDggyoKnSm8Zfyr6OcelWs&f%5B0%5D=daterange%3A2024&items_per_page=10&page=7&v=2 | D | 2026-09-08 | Contrôle ultérieur de la Cour des comptes | La Cour des comptes a publié le 4 mars 2024 des observations définitives consacrées au secrétariat général du CIPDR. | -
FCT-034 | FACT | ✧ | https://www.lemonde.fr/societe/article/2023/05/04/fonds-marianne-une-information-judiciaire-ouverte-notamment-pour-detournement-de-fonds-et-abus-de-confiance_6172130_3224.html | E | 2026-09-08 | Information judiciaire ouverte par le PNF | Une information judiciaire a été ouverte en mai 2023 sur la gestion du Fonds Marianne, notamment pour des soupçons de détournement de fonds publics, abus de confiance et prise illégale d’intérêts. | -
FCT-035 | FACT | ✧ | https://www.lemonde.fr/societe/article/2024/03/04/la-cour-des-comptes-severe-avec-le-comite-interministeriel-de-prevention-de-la-delinquance-et-de-la-radicalisation_6220002_3224.html | E | 2026-09-08 | Instruction judiciaire toujours en cours en mars 2024 | Le Monde indiquait le 4 mars 2024 que l’instruction du PNF sur le Fonds Marianne était toujours en cours. | -
FCT-036 | FACT | ✧ | https://www.publicsenat.fr/actualites/politique/fonds-marianne-ce-qua-revele-laudition-tres-tendue-de-mohamed-sifaoui | other:public-senat | 2026-09-08 | Seconde tranche USEPPM non versée | Christian Gravel a rappelé que la seconde tranche de la subvention USEPPM n’avait pas été versée après des relances restées sans réponse concernant des pièces comptables. | -
FCT-037 | FACT | ✧ | https://www.publicsenat.fr/actualites/politique/fonds-marianne-ce-qua-revele-laudition-tres-tendue-de-mohamed-sifaoui | other:public-senat | 2026-09-08 | Sifaoui consultant du CIPDR pendant la période de mise en place | L’audition rapportée par Public Sénat indique que Mohamed Sifaoui était déjà rémunéré comme consultant du CIPDR pendant une période couvrant la mise en place du Fonds Marianne. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-001
FCT-005 | SRC-002
FCT-006 | SRC-002
FCT-007 | SRC-002
FCT-008 | SRC-002
FCT-009 | SRC-003
FCT-010 | SRC-003
FCT-011 | SRC-003
FCT-012 | SRC-003
FCT-013 | SRC-003
FCT-014 | SRC-003
FCT-015 | SRC-003
FCT-016 | SRC-003
FCT-017 | SRC-003
FCT-018 | SRC-003
FCT-019 | SRC-003
FCT-020 | SRC-004
FCT-021 | SRC-004
FCT-022 | SRC-004
FCT-023 | SRC-005
FCT-024 | SRC-005
FCT-025 | SRC-006
FCT-026 | SRC-006
FCT-027 | SRC-007
FCT-028 | SRC-008
FCT-029 | SRC-008
FCT-030 | SRC-008
FCT-031 | SRC-008
FCT-032 | SRC-008
FCT-033 | SRC-009
FCT-034 | SRC-010
FCT-035 | SRC-011
FCT-036 | SRC-012
FCT-037 | SRC-012

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
FCT-034 | ELIGIBLE:VERIFIE
FCT-035 | ELIGIBLE:VERIFIE
FCT-036 | ELIGIBLE:VERIFIE
FCT-037 | ELIGIBLE:VERIFIE

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
FCT-034 | WRITE | -
FCT-035 | WRITE | -
FCT-036 | WRITE | -
FCT-037 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:12
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:11:CAU-001 | NEXT_ACTION:13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-08T05:12:11.047916+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-029","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-030","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-031","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-032","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-033","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-034","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-035","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-036","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-037","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":37,"eligible":37,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:37;attempted:0;success:0;failure:0;blocked:37} | WRITEBACK_EXECUTION_V1:[37 rows, see section]

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
FCT-034 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-035 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-036 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-037 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
