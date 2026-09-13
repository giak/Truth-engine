ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260907-1811-campaign-financing-france | PARENT_RUN_ID:NONE | AS_OF:2026-09-07
INPUT_KIND:RUN_CARD | MISSION_MODE:DEEPEN | INPUT_REF:PATH:/mnt/data/inv093-work/te/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-07_campaign-financing-france/2026-09-07_18-11_campaign-financing-france_INPUT.md | SUBJECT_SLUG:campaign-financing-france | SUBJECT_FP:sha256:88ae8694f81d300659cc1eeea12fc9b371c26c17d6f30359fee00749b1fdbdc1 | INPUT_SHA256:sha256:1024cec0816e579bf11b7c97fb511042c3dff509de0a1118bfb765938a48563e
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France 2012-2026; campaign financing mechanics, donations, loans, party/micro-party support, services, expenses, account control, sanctions and criminal findings; foreign financing only as boundary/context.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/MONEY.md,clusters/POWER.md,clusters/NETWORK.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "truth_engine_narrative"
artifact_id: "INV-093-NARRATIVE"
version: "1.0"
status: "technical_frozen"
updated: "2026-09-07"
inv_id: "INV-093"
---

<!-- TRACE: run=20260907-1811-campaign-financing-france; engine=2.10.6/R3P1; facts=FCT-001..FCT-028 -->

# INV-093 — Financement des campagnes françaises : argent, prêts, partis, prestations et contournements

## Question et règle de preuve

L'enquête ne cherche pas à démontrer que l'argent « achète » mécaniquement une campagne, un candidat ou une élection. Elle reconstruit une chaîne plus exigeante : `source des fonds -> véhicule juridique -> transaction ou prestation -> compte de campagne -> règle applicable -> contrôle CNCCFP -> décision ou recours -> conséquence -> effet politique éventuel`.

Les séparations suivantes gouvernent tout le run : `donation != prêt`, `prêt != financement illicite`, `prestation != avantage caché`, `irrégularité != fraude`, `réformation ou rejet du compte != corruption`, `financement != commandement politique`, `conséquence institutionnelle != résultat électoral modifié`. Le financement étranger n'est utilisé ici que comme frontière juridique ou trou de traçabilité ; son analyse propre relève d'INV-094 et d'INV-140.

## 1. Une architecture fortement réglementée, mais composée de plusieurs canaux

Le droit français n'organise pas un canal unique de financement. Il distingue plusieurs formes de ressources et impose des contraintes différentes selon l'origine et le véhicule. Les dons des personnes physiques sont plafonnés à 4 600 euros pour les mêmes élections. Les personnes morales autres que les partis ou groupements politiques ne peuvent financer un candidat par don, ni lui fournir des biens, services ou avantages à un prix anormalement bas. Les contributions ou aides matérielles provenant d'un État étranger ou d'une personne morale étrangère sont prohibées, sous réserve des exceptions prévues pour certains établissements financiers de l'Union européenne ou de l'Espace économique européen. [FCT-001, FCT-002, FCT-003]

Les prêts consentis par des personnes physiques sont, eux, expressément possibles sous conditions. Ils ne doivent pas constituer une activité habituelle, leur durée est bornée et leur remboursement fait l'objet d'un suivi. Cela interdit de traiter le mot « prêt » comme un synonyme de financement clandestin. [FCT-004]

Le compte de campagne doit retracer les recettes selon leur origine et les dépenses selon leur nature. Les dépenses engagées pour le candidat par des soutiens ou des partis peuvent devoir être intégrées. La Commission nationale des comptes de campagne et des financements politiques dispose ensuite d'une gamme de décisions distinctes : approbation, réformation, rejet, modulation du remboursement, et, selon les cas, transmission au juge de l'élection ou au parquet. [FCT-005, FCT-006, FCT-007, FCT-008]

Le premier résultat est donc négatif à l'égard d'un modèle trop simple : le système n'est pas un espace non réglementé dans lequel tout flux est invisible. Il existe une architecture de déclaration, de contrôle contradictoire, de réformation et de sanction. Cette densité ne signifie toutefois pas que l'origine économique ultime de chaque euro est toujours parfaitement observable.

## 2. Les prêts et l'intervention des partis sont des mécanismes ordinaires

La présidentielle de 2022 fournit un contrôle particulièrement utile. Les données de la CNCCFP montrent que les campagnes combinent argent personnel, dons, financements des partis, prêts et remboursement public. Pour cette élection, les candidats ont déclaré environ 83,5 millions d'euros de dépenses et 85,2 millions d'euros de recettes ; le remboursement de l'État atteint environ 42,2 millions, les dons environ 9 millions et les contributions des partis environ 27 millions. [FCT-020]

Surtout, la CNCCFP a identifié 38 partis ayant participé au financement des douze candidats. Tous les candidats ont bénéficié d'un prêt d'une formation politique et, pour neuf d'entre eux, ce prêt constituait la principale modalité d'intervention du parti. Dans six cas, le parti avait lui-même emprunté auprès d'une banque afin de prêter au candidat, ce que la Commission décrit comme un « prêt miroir ». Pour Valérie Pécresse, Anne Hidalgo et Yannick Jadot, les contributions définitives du parti dominaient au contraire. [FCT-021, FCT-022, FCT-023, FCT-024]

Ces constats ont une fonction méthodologique importante. Un prêt de parti, un prêt miroir, une dette envers une structure politique ou un financement via un véhicule partisan peuvent mériter un audit, mais leur seule existence ne démontre ni contournement, ni fraude, ni contrôle du candidat par le financeur. Le caractère licite ou illicite dépend de la qualité du prêteur, des conditions, de la comptabilisation, de la tarification des prestations et des faits propres au dossier.

La structure des financements évolue également. Le rapport 2024 de la CNCCFP indique une baisse de la part du crédit bancaire dans le financement des candidats, de 23 % en 2017 à 18 % en 2022 puis 8 % lors des législatives de 2024, tandis que les prêts de personnes physiques passent de 5 % à 9 % puis 13 %. [FCT-025, FCT-026]

## 3. Réformation, modulation, rejet et fraude ne sont pas le même objet

La présidentielle de 2017 fournit un deuxième contrôle négatif. La CNCCFP a relevé dans le compte de François Fillon 88 349 euros de dépenses omises et l'utilisation de quatre salles de réunion provenant de personnes morales non autorisées. La Commission a réformé le compte et diminué le remboursement de 50 000 euros ; elle ne l'a pas rejeté. [FCT-017]

Pour Emmanuel Macron, la Commission a examiné 87 600 euros de dons apparaissant initialement supérieurs au plafond individuel. Dans vingt cas sur vingt-quatre, l'analyse a retenu notamment l'imputation au conjoint et la bonne foi ; quatre dons restaient au-dessus du plafond pour un total de 18 300 euros. Là encore, le compte n'a pas été rejeté : le remboursement a été réduit. [FCT-018]

Ces exemples ne prouvent pas que les irrégularités sont bénignes. Ils prouvent autre chose, plus important pour la classification : le droit et le régulateur distinguent la correction comptable, la modulation financière, le rejet du compte et l'infraction pénale. Une analyse qui transforme toute réformation en fraude ou tout dépassement en corruption détruit cette gradation et produit un faux positif méthodologique.

## 4. Sarkozy 2012 et Bygmalion : deux voies juridiques distinctes

Le compte de Nicolas Sarkozy pour la présidentielle de 2012 se situe à un niveau différent. La CNCCFP l'a rejeté en décembre 2012. Elle relevait notamment un dépassement initial du plafond de 363 615 euros, ainsi que 1 567 425 euros de dépenses réintégrées, soit 7,35 % des dépenses déclarées. Elle a également traité comme contribution interdite de personne morale certaines manifestations à caractère électoral financées par le budget de l'État sans refacturation au mandataire. [FCT-009, FCT-010, FCT-011]

Le Conseil constitutionnel a ensuite réformé le compte, fixé les dépenses à 22 975 118 euros et les recettes à 23 094 932 euros, et maintenu le rejet. Le dépassement retenu du plafond autorisé était de 466 118 euros. [FCT-012, FCT-013]

Cette décision n'épuise toutefois pas le dossier Bygmalion. Dans l'arrêt du 26 novembre 2025, la Cour de cassation a rejeté les pourvois contre l'arrêt d'appel pénal de 2024 et confirmé des condamnations liées au financement illégal de la campagne, avec des qualifications comprenant notamment faux, escroquerie ou complicité selon les prévenus. Surtout, la Cour a explicitement borné la portée de l'autorité attachée à la décision du Conseil constitutionnel sur le compte de campagne : celle-ci ne bloque pas, de manière générale, un jugement pénal distinct sur des faits et infractions propres. [FCT-014, FCT-015]

Le cas est donc décisif pour la méthode. `Compte rejeté` et `fraude pénalement établie` ne sont ni synonymes ni mutuellement exclusifs. Ce sont deux voies de contrôle différentes, qui peuvent se succéder et porter sur des objets juridiques distincts. L'existence ultérieure d'une condamnation pénale ne permet pas, en retour, de requalifier automatiquement en fraude chaque réformation administrative observée dans d'autres campagnes.

## 5. Associations, prestations et « kits de campagne » : le véhicule peut être abusé sans être coupable par nature

Le dossier lié à l'association Jeanne et aux campagnes législatives de 2012 documente une autre famille de mécanismes. L'arrêt de la Cour de cassation du 19 juin 2024 retrace l'utilisation d'une association politique et d'une société autour d'un système de « kits de campagne », de prestations facturées et de crédit fournisseur, ainsi que d'autres prises en charge par une société. Les procédures pénales ont abouti à des condamnations pour des infractions comprenant escroquerie, recel et financement illégal selon les acteurs et les faits concernés. [FCT-028]

Ce cas établit qu'un véhicule associatif ou partisan, un prestataire, un kit standardisé ou un crédit fournisseur peuvent être intégrés dans un montage illicite lorsqu'une chaîne factuelle et juridique précise le démontre. Il n'établit pas que les micro-partis, associations de financement, prestations mutualisées ou crédits fournisseurs seraient frauduleux par nature. Le bon niveau d'analyse reste transactionnel : prix, service effectivement rendu, créancier, bénéficiaire, comptabilisation, remboursement, intention et décision judiciaire.

## 6. Le trou réel : l'origine amont de certains fonds individuels

La densité du contrôle aval ne ferme pas toute la chaîne. La CNCCFP explique demander des justificatifs sur l'origine de certains apports personnels importants, mais signale ne pas disposer de moyens juridiques suffisants pour établir pleinement l'origine des fonds prêtés par des personnes physiques ou donnés. Ce point devient plus matériel à mesure que les prêts de personnes physiques progressent dans la structure de financement. [FCT-025, FCT-026, FCT-027]

Il s'agit d'un trou de responsabilité et de traçabilité, pas d'une preuve positive de financement illicite. Le constat justifie une investigation ciblée sur l'origine bénéficiaire des fonds lorsqu'un cas matériel l'exige. Il ne justifie pas d'attribuer une origine étrangère, un prête-nom ou un commanditaire sans pièce supplémentaire. Cette frontière doit être routée vers INV-094 et INV-140.

## 7. Plafond causal et conséquences

Le run ferme solidement plusieurs étages de la chaîne : source juridique autorisée ou interdite, véhicule, transaction ou prestation, intégration au compte, contrôle, réformation ou rejet, et, dans certains dossiers, conséquence judiciaire ou pénale. On peut donc soutenir fortement I0 à I4 de manière cas-spécifique sur les dossiers les mieux documentés.

En revanche, l'enquête ne ferme pas les étages `financement -> commandement politique`, `financement -> persuasion des électeurs` ou `financement -> résultat électoral contrefactuel`. L'argent permet matériellement de mener une campagne ; le remboursement, le rejet ou une condamnation peuvent avoir des conséquences institutionnelles et politiques. Mais ces constats ne suffisent pas à établir qu'un financeur dirige politiquement le candidat, ni qu'un mécanisme de financement donné a changé le résultat du scrutin.

Le modèle le mieux soutenu est donc mixte : la France possède un système de financement électoral fortement réglementé, avec des mécanismes de financement ordinaires et une gradation réelle des contrôles ; des contournements ou fraudes peuvent être établis dans des cas précis lorsque la chaîne probatoire est fermée ; enfin, un trou de traçabilité amont subsiste pour certains fonds individuels. Le modèle « tout financement atypique est un contournement » est réfuté par les contrôles normaux. Le modèle inverse « le contrôle institutionnel rend le système entièrement traçable » est lui aussi trop fort.

<!-- TRACE: terminal_delta=regulated_multi-channel_system+graded_controls+case_specific_abuse+upstream_origin_gap; routes=INV-095,INV-102,INV-094,INV-140 -->
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:6|SRC_COMPLETE:14/14

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **limits:**
  - later criminal judgment must not be back-projected into every earlier account irregularity
  - 2012, 2017, 2022 and 2024 mechanisms are compared only at matched procedural stages
- **sequence:**
  - fundraising/loan/service
  - campaign expenditure
  - account filing
  - CNCCFP adversarial control
  - approval/reform/rejection
  - judicial or prosecutorial escalation where applicable
  - reimbursement/Treasury/criminal consequence
  - possible downstream political/electoral effect
- **status:** ACTIVE

### MANIPULATION_REPORT
- **assumptions:**
  - legal texts establish formal rules, not actual compliance in every campaign
  - CNCCFP decisions establish administrative findings, not criminal guilt unless separately adjudicated
  - criminal judgments establish case-specific liability, not prevalence across all campaigns
  - negative and ordinary financing cases are retained as controls
- **clusters:**
  - **loaded:**
    - clusters/MONEY.md
    - clusters/POWER.md
    - clusters/NETWORK.md
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - regulated does not mean fully traceable
  - loan does not establish illicit source
  - account reform does not establish fraud
  - criminal conviction is case-specific
  - funding does not establish political command
  - institutional consequence does not establish changed result
- **input_kind:** TOPIC
- **mission_mode:** INVESTIGATION
- **patterns:**
  - campaign-account reform
  - party loan
  - mirror loan
  - service/in-kind contribution
  - micro-party/service vehicle
  - ceiling overrun
- **priorities:**
  - legal financing channels
  - loan and party mechanisms
  - service/in-kind accounting
  - gradient of administrative outcomes
  - case-specific criminal schemes
  - origin-of-funds traceability
  - electoral causal ceiling
- **query_guidance:** trace source of funds -> legal vehicle -> donation/loan/service -> campaign account -> CNCCFP reform/reject -> judge/prosecutor -> consequence; preserve administrative/criminal and financing/command boundaries
- **rhetorical:**
  - **AUTH:** official administrative and judicial decisions establish their own legal findings, not broader motive or electoral effect
  - **BF:** N/A
  - **DEM:** lawful campaign financing and oversight are separated from proven abuse
  - **FAC:** avoid vehicle-to-guilt and financing-to-command association fallacies
  - **NUM:** amounts and shares establish financial structure, not motive or causal electoral impact
- **speaker:**
  - **goal:** forensic classification of French campaign-finance mechanisms, controls and case-specific abuses
  - **target:** source-vehicle-transaction-account-control-consequence-effect chain
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **Κ:** 3
  - **Λ:** 4
  - **Ξ:** 4
  - **Σ:** 3
  - **Φ:** 3
  - **Ψ:** 3
  - **Ω:** 4
  - **κ:** 3
  - **ρ:** 4
  - **€:** 5
  - **↕:** 4
  - **⏰:** 4
  - **⚔:** 3
  - **⫸:** 4
  - **🌐:** 4
- **threats:**
  - loan=illicit_financing
  - irregularity=fraud
  - rejected_account=corruption
  - micro_party=fraud
  - funding=political_command
  - sanction=result_changed

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - origin of some physical-person funds
  - **input_ids:**
    - FCT-001
    - FCT-004
    - FCT-020
    - FCT-021
    - FCT-022
    - FCT-023
    - FCT-024
    - FCT-026
  - **module:** clusters/MONEY.md
  - **negative_results:**
    - loan not equivalent to illicit financing
  - **not_computable:**
    - complete beneficial origin for all individual funds
  - **operations_applied:**
    - typed donations, loans, party finance, reimbursements
    - separated resource flow from political command
  - **reason:** trace campaign-finance resource flows and legal vehicles
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CTRL-001
    - CTRL-002
  - **status:** DONE
  - **trigger:** €
- **item 2:**
  - **gaps:**
    - political-command evidence
  - **input_ids:**
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-008
    - FCT-014
    - FCT-015
  - **module:** clusters/POWER.md
  - **negative_results:**
    - funding does not establish command
  - **not_computable:**
    - hidden informal influence without records
  - **operations_applied:**
    - separated account-control power from criminal adjudication
    - bounded funder influence
  - **reason:** separate funder, candidate, CNCCFP and judicial authority
  - **result_ids:**
    - CLM-003
    - CLM-004
    - CTRL-003
    - CTRL-006
  - **status:** DONE
  - **trigger:** ↕
- **item 3:**
  - **gaps:**
    - prevalence of abusive service pricing
  - **input_ids:**
    - FCT-021
    - FCT-022
    - FCT-023
    - FCT-024
    - FCT-028
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - vehicle type does not establish fraud
  - **not_computable:**
    - complete informal networks
  - **operations_applied:**
    - typed party-loan and service edges
    - preserved vehicle versus culpability boundary
  - **reason:** map party, micro-party, financial agent, lender and service-provider edges
  - **result_ids:**
    - CLM-002
    - CLM-005
    - CTRL-004
  - **status:** DONE
  - **trigger:** 🌐

### SCOPING_REPORT
- **classification_dimensions:**
  - source of funds
  - vehicle
  - transaction/service
  - accounting
  - legal rule
  - CNCCFP outcome
  - judicial/criminal outcome
  - reimbursement
  - political command
  - electoral effect
- **exclusions:**
  - loan=illicit financing
  - service=hidden benefit
  - irregularity=fraud
  - reform/rejection=corruption
  - funding=political command
  - foreign financing=domestic mechanism
- **scope:** France 2012-2026 campaign financing: donations, loans, party/micro-party support, services, expenses, account control, sanctions; foreign financing only as boundary/context.
- **status:** ACTIVE

### CREDO
- donation != loan
- loan != illicit_financing
- service != hidden_benefit
- irregularity != fraud
- reformed_or_rejected_account != corruption
- micro_party != fraud
- funding != political_command
- institutional_consequence != electoral_result
- foreign_financing != domestic_financing_mechanism

### COGNITIVE_MAP
- **input_kind:** TOPIC
- **mission_mode:** INVESTIGATION
- **patterns:**
  - campaign account reform
  - party loan
  - mirror loan
  - in-kind contribution
  - service pricing
  - micro-party vehicle
  - ceiling overrun
- **priorities:**
  - legal financing channels
  - loans and party financing
  - services/in-kind expenses
  - gradient of irregularities
  - micro-party abuse case
  - origin-of-funds gap
  - causal ceiling
- **query_guidance:** trace source -> legal vehicle -> transaction/service -> account -> CNCCFP decision -> appeal/prosecutor -> consequence; preserve administrative/criminal and financing/command boundaries
- **speaker:**
  - **goal:** forensic classification of French campaign-finance mechanisms and irregularities
  - **target:** fund -> vehicle -> transaction -> account -> control -> consequence -> effect chain
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **threats:**
  - loan=illicit financing
  - reform=fraud
  - rejection=corruption
  - micro-party=fraud
  - funding=command
  - sanction=result changed

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** CNCCFP has graded outcomes; 2017 cases were reformed/modulated without rejection, while criminal liability requires distinct proof.
  - **resolution:** Administrative irregularity and criminal fraud are separate findings; escalation depends on facts and legal basis.
  - **thesis:** A reformed or rejected campaign account proves fraud or corruption.
- **item 2:**
  - **antithesis:** Party loans were universal among 2022 presidential candidates and mirror loans common; only specific abusive schemes support criminal findings.
  - **resolution:** Vehicle/form is neutral until terms, pricing, disclosure and conduct establish a violation.
  - **thesis:** Loans, mirror loans or micro-parties are hidden-financing devices by nature.
- **item 3:**
  - **antithesis:** CNCCFP reports limited powers to verify the upstream origin of funds lent or donated by individuals.
  - **resolution:** Downstream account control is dense but upstream beneficial-origin traceability remains incomplete.
  - **thesis:** Campaign finance is fully traceable and therefore origin risk is closed.
- **item 4:**
  - **antithesis:** The corpus documents funding and institutional consequences, not political-command or electoral-counterfactual causal evidence.
  - **resolution:** Funding is material but command/effect requires separate evidence.
  - **thesis:** Who finances a campaign controls the candidate or election result.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **from:** individual donor/lender
  - **limits:**
    - donation cap and lender rules apply
    - upstream origin may remain partly unauditable
  - **resource:** money
  - **support:**
    - FCT-001
    - FCT-004
    - FCT-026
    - FCT-027
  - **to:** candidate campaign account
  - **via:** donation or loan
- **item 2:**
  - **from:** political party
  - **limits:**
    - party loan != illicit financing
    - public reimbursement rules create distinct accounting incentives
  - **resource:** campaign finance
  - **support:**
    - FCT-020
    - FCT-021
    - FCT-022
    - FCT-023
    - FCT-024
  - **to:** candidate
  - **via:** loan or definitive contribution
- **item 3:**
  - **from:** service/in-kind provider
  - **limits:**
    - below-market legal-person support can be prohibited
    - service vehicle != hidden benefit by itself
  - **resource:** goods/services/credit
  - **support:**
    - FCT-002
    - FCT-005
    - FCT-010
    - FCT-017
    - FCT-028
  - **to:** campaign
  - **via:** service, expense, advantage or campaign kit

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** donors/lenders/parties
  - **limits:**
    - funding != political command
  - **relation:** funding
  - **support:**
    - FCT-001
    - FCT-004
    - FCT-021
  - **to:** candidate/financial agent
- **item 2:**
  - **from:** candidate/agent/supporters/parties
  - **limits:**
    - account entry != legality finding
  - **relation:** receipts and expenses recorded by origin/nature
  - **support:**
    - FCT-005
  - **to:** campaign account
- **item 3:**
  - **from:** CNCCFP
  - **limits:**
    - administrative control != criminal guilt
  - **relation:** adversarial control / approve-reform-reject / reimbursement
  - **support:**
    - FCT-006
    - FCT-008
  - **to:** campaign account
- **item 4:**
  - **from:** election judge/prosecutor/criminal courts
  - **limits:**
    - case-specific judgment != category-wide guilt
  - **relation:** distinct judicial/criminal consequences
  - **support:**
    - FCT-007
    - FCT-012
    - FCT-014
    - FCT-015
    - FCT-028
  - **to:** candidate or other actors

### IMPACT_MAP
- **electoral_effect:** NOT_ESTABLISHED_COUNTERFACTUALLY
- **institutional_effects:**
  - account reform/rejection
  - reimbursement modulation
  - Treasury overrun payment
  - election-judge referral
  - prosecutor transmission
  - criminal liability in proven schemes
- **support:**
  - FCT-006
  - FCT-007
  - FCT-008
  - FCT-014
  - FCT-015
  - FCT-019

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** 2017 controls produced reform/modulation without rejection; criminal liability is a distinct track
  - **issue:** irregularity versus fraud
  - **pro:** accounts can contain omitted expenses, excess donations or prohibited advantages
  - **resolution:** IRREGULARITY_VERIFIED_FRAUD_NOT_AUTOMATIC
- **item 2:**
  - **contra:** law expressly permits qualifying loans; 2022 party loans were universal
  - **issue:** loan versus illicit financing
  - **pro:** loans can create dependency and traceability concerns
  - **resolution:** LOAN_NORMAL_MECHANISM_TERMS_AND_SOURCE_CONTROL_REQUIRED
- **item 3:**
  - **contra:** one abusive scheme does not make all micro-parties/services illicit
  - **issue:** micro-party/service vehicle versus fraud
  - **pro:** Jeanne-related case documents campaign kits, supplier credit and criminal convictions
  - **resolution:** CASE_SPECIFIC_ABUSE_NOT_CATEGORY_GUILT
- **item 4:**
  - **contra:** CNCCFP reports limited upstream fund-origin powers for physical persons
  - **issue:** control versus completeness
  - **pro:** CNCCFP has detailed account-control and referral powers
  - **resolution:** DENSE_DOWNSTREAM_CONTROL_WITH_UPSTREAM_GAP
- **item 5:**
  - **contra:** no causal design closes command, persuasion or result edges
  - **issue:** funding versus political effect
  - **pro:** money and services enable campaigning and sanctions can affect institutions
  - **resolution:** MECHANISM_VERIFIED_COUNTERFACTUAL_EFFECT_NOT_ESTABLISHED

### VERIFICATION_REPORT
- **independence_limits:**
  - CNCCFP reports combine regulator self-description with published decisions
  - Vie-publique hosts the CNCCFP 2024 report used for origin-of-funds gap
  - case-specific criminal judgments do not estimate prevalence across all campaigns
  - no causal design linking ordinary financing mechanisms to election outcome
- **negative_checks:**
  - 2017 Fillon reform/modulation retained
  - 2017 Macron reform/modulation retained
  - 2022 normal party-loan prevalence retained
  - administrative-account/criminal-track distinction retained
  - micro-party vehicle not generalized as fraud
  - origin-of-funds gap retained
  - no political-command claim
  - no electoral-counterfactual claim
- **source_families:** 5
- **source_records_complete:** 14/14
- **status:** PASS_WITH_EXPLICIT_GAPS
- **web_fact_trace:** 28/28 facts mapped to accepted FETCH-backed sources

### EDI_REPORT
- **corpus:**
  - **circularity:** LOW_TO_MODERATE
  - **coverage:** LEGAL_ARCHITECTURE_AND_CASE_GRADIENT_STRONG
  - **independence:** HIGH_FOR_LAW_AND_FINAL_JUDGMENTS_MODERATE_FOR_REGULATOR_AGGREGATES
  - **limits:**
    - CNCCFP supplies both process description and many aggregate observations
    - Vie-publique mirrors the CNCCFP 2024 report for the origin-of-funds gap
    - single criminal cases do not establish prevalence of abuse
    - no matched causal dataset closes electoral effect
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **gap_type:** SCOPE
    - **independent_families:** 3
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES_WITH_CASE_SPECIFIC_ABUSE_BOUNDARY
    - **gap_type:** QUALIFICATION
    - **independent_families:** 3
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** YES_WITH_NEGATIVE_CONTROLS
    - **gap_type:** QUALIFICATION
    - **independent_families:** 3
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** YES_CASE_SPECIFIC
    - **gap_type:** QUALIFICATION
    - **independent_families:** 3
  - **item 5:**
    - **claim_id:** CLM-005
    - **direct_object:** YES_CASE_SPECIFIC
    - **gap_type:** COVERAGE
    - **independent_families:** 1
  - **item 6:**
    - **claim_id:** CLM-006
    - **direct_object:** YES_WITH_RESPONSIBILITY_AND_CAUSAL_GAPS
    - **gap_type:** CAUSALITY
    - **independent_families:** 2
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** 5_PROVENANCE_FAMILIES
  - **perspective:** LEGIFRANCE+CNCCFP+CONSEIL_CONSTITUTIONNEL+COUR_DE_CASSATION+VIE_PUBLIQUE
  - **stratification:** RULES+VEHICLES+ACCOUNT_CONTROL+JUDICIAL_CRIMINAL_CONSEQUENCES
  - **temporal:** 2012-2026
- **edi:**
  - **assessment:** STRONG_LEGAL_AND_CASE_CONTROL_COVERAGE_WITH_UPSTREAM_ORIGIN_AND_DOWNSTREAM_CAUSAL_GAPS
  - **flags:**
    - REGULATOR_SELF_DESCRIPTION_FOR_PROCESS
    - OFFICIAL_JUDICIAL_CASES_PRESENT
    - NORMAL_FINANCING_CONTROLS_PRESENT
    - ORIGIN_OF_FUNDS_GAP
    - NO_POLITICAL_COMMAND_EVIDENCE
    - NO_ELECTORAL_COUNTERFACTUAL_EFFECT
- **source_counts:**
  - **claim_source:** 0
  - **primary:** 13
  - **provenance_families:** 5
  - **secondary:** 1
  - **total:** 14

### RESPONSIBILITY_MAP
- **item 1:**
  - **highest_supported:** campaign-account responsibility and case-specific legal consequences
  - **not_supported:** fraud from every reform or rejection
  - **object:** candidate/financial agent
  - **support:**
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-008
- **item 2:**
  - **highest_supported:** financing/service role; case-specific abuse can be criminally established
  - **not_supported:** inherent illegality of vehicle type
  - **object:** party/micro-party/service vehicle
  - **support:**
    - FCT-021
    - FCT-022
    - FCT-023
    - FCT-024
    - FCT-028
- **item 3:**
  - **highest_supported:** lawful or prohibited source/status rules plus partial traceability
  - **not_supported:** political command from funding alone
  - **object:** funders/lenders
  - **support:**
    - FCT-001
    - FCT-003
    - FCT-004
    - FCT-027

### NEXT_QUERIES
- **item 1:**
  - **query:** primary loan agreements or beneficial-origin records for high-value physical-person campaign loans/donations
  - **route:** INV-094/INV-140
  - **trigger:** identified filing, court exhibit or CNCCFP power expansion
- **item 2:**
  - **query:** structured cross-election dataset of micro-party/service pricing reforms, rejections and criminal findings
  - **route:** INV-095
  - **trigger:** identified machine-readable CNCCFP/judicial dataset
- **item 3:**
  - **query:** causal design linking financing mechanism or sanction to voter behavior or electoral outcome
  - **route:** INV-102
  - **trigger:** identified quasi-experiment or matched electoral study

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-002,QRY-014 | support:FCT-004,FCT-026,FCT-027 | counter:- | results:FCT-004,FCT-026,FCT-027 | final:GAP | gap:RESPONSIBILITY
LED-002 | attempts:QRY-005,QRY-009,QRY-010,QRY-011,QRY-012 | support:FCT-008,FCT-016,FCT-019,FCT-020,FCT-021,FCT-022,FCT-023,FCT-024 | counter:- | results:FCT-008,FCT-016,FCT-019,FCT-020,FCT-021,FCT-022,FCT-023,FCT-024 | final:GAP | gap:CAUSALITY
AXS-001 | attempts:QRY-001,QRY-002,QRY-003 | support:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005 | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-002,QRY-011,QRY-012,QRY-014 | support:FCT-004,FCT-021,FCT-022,FCT-023,FCT-024,FCT-025,FCT-026 | counter:- | results:FCT-004,FCT-020,FCT-021,FCT-022,FCT-023,FCT-024,FCT-025,FCT-026 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-001,QRY-003,QRY-006,QRY-009,QRY-013 | support:FCT-002,FCT-005,FCT-010,FCT-017,FCT-028 | counter:- | results:FCT-002,FCT-005,FCT-010,FCT-017,FCT-028 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010 | support:FCT-006,FCT-008,FCT-017,FCT-018,FCT-019,FCT-014,FCT-015 | counter:- | results:FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-017,FCT-018,FCT-019 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-013 | support:FCT-028 | counter:- | results:FCT-028 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-005,QRY-009,QRY-010,QRY-011,QRY-012,QRY-014 | support:FCT-016,FCT-020,FCT-021,FCT-022,FCT-023,FCT-024 | counter:- | results:FCT-016,FCT-019,FCT-020,FCT-021,FCT-022,FCT-023,FCT-024,FCT-027 | final:GAP | gap:CAUSALITY
CLM-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-009,QRY-011,QRY-012,SRC-001,SRC-002,SRC-003,SRC-004,SRC-009,SRC-011,SRC-012 | support:FCT-001,FCT-004,FCT-005,FCT-006,FCT-016,FCT-020,FCT-021,FCT-022,FCT-023,FCT-024 | counter:CTRL-001 | results:FCT-001,FCT-004,FCT-005,FCT-006,FCT-016,FCT-020,FCT-021,FCT-022,FCT-023,FCT-024,CTRL-001 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-002 | attempts:QRY-002,QRY-012,QRY-013,SRC-002,SRC-012,SRC-013 | support:FCT-004,FCT-021,FCT-022,FCT-023,FCT-024,FCT-028 | counter:CTRL-002;CTRL-004 | results:FCT-004,FCT-021,FCT-022,FCT-023,FCT-024,FCT-028,CTRL-002;CTRL-004 | final:SUPPORTED | gap:QUALIFICATION
CLM-003 | attempts:QRY-004,QRY-005,QRY-009,QRY-010,SRC-004,SRC-005,SRC-009,SRC-010 | support:FCT-006,FCT-007,FCT-008,FCT-017,FCT-018,FCT-019 | counter:CTRL-003 | results:FCT-006,FCT-007,FCT-008,FCT-017,FCT-018,FCT-019,CTRL-003 | final:SUPPORTED | gap:QUALIFICATION
CLM-004 | attempts:QRY-006,QRY-007,QRY-008,SRC-006,SRC-007,SRC-008 | support:FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015 | counter:CTRL-003 | results:FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,CTRL-003 | final:SUPPORTED | gap:QUALIFICATION
CLM-005 | attempts:QRY-013,SRC-013 | support:FCT-028 | counter:CTRL-004 | results:FCT-028,CTRL-004 | final:SUPPORTED | gap:COVERAGE
CLM-006 | attempts:QRY-014,SRC-014 | support:FCT-025,FCT-026,FCT-027 | counter:CTRL-005;CTRL-006 | results:FCT-025,FCT-026,FCT-027,CTRL-005;CTRL-006 | final:SUPPORTED | gap:CAUSALITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
AXS-006 | AXS | GAP | CAUSALITY | No examined source or comparative causal design establishes that a lawful financing channel by itself commanded a candidate or changed the electoral outcome.
CLM-001 | CLM | SUPPORTED | RESPONSIBILITY | Regulation does not imply complete upstream traceability of every fund source.
CLM-002 | CLM | SUPPORTED | QUALIFICATION | Specific abusive arrangements remain possible and must be proven transaction by transaction.
CLM-003 | CLM | SUPPORTED | QUALIFICATION | Administrative irregularity can coexist with or later lead to criminal facts, but the legal findings remain distinct.
CLM-004 | CLM | SUPPORTED | QUALIFICATION | The criminal judgment does not turn every accounting reform or overrun into fraud.
CLM-005 | CLM | SUPPORTED | COVERAGE | General prevalence of abusive micro-party pricing or supplier-credit structures is not established by one final case.
CLM-006 | CLM | SUPPORTED | CAUSALITY | Beneficial origin and causal electoral effect require separate evidence.
CAU-001 | CAU | UNRESOLVED | CAUSALITY | Upstream beneficial origin of some individual funds and downstream political/electoral counterfactual effect remain unestablished.

SEMANTIC_COUNTS_V1:LED:2|CLM:6|AXS:6|CAU:1|CTRL:6|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-002","QRY-014"],"evidence_excerpt":"Physical-person loans are lawful and increasingly used, while CNCCFP reports limited powers to establish the upstream origin of funds lent or donated by individuals.","gap":"Upstream beneficial origin of some individual loan/donation funds is not fully auditable with current CNCCFP powers.","gap_type":"RESPONSIBILITY","kind":"EVIDENCE_GAP","lead":"Origin of funds behind physical-person loans and donations","linked_ids":["CLM-006","CTRL-005"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-004","FCT-026","FCT-027"],"route":"INV-094/INV-140","routes":["INV-094","INV-140"],"source_id":"INV-093_RUN_CARD","status":"GAP","support":["FCT-004","FCT-026","FCT-027"]}
LED-002 | {"attempt_ids":["QRY-005","QRY-009","QRY-010","QRY-011","QRY-012"],"evidence_excerpt":"The corpus establishes financing vehicles, controls and sanctions, but does not identify a causal design showing that an ordinary lawful funding channel commanded a candidate or changed an election result.","gap":"Political-command and electoral-counterfactual effects are not established from financing alone.","gap_type":"CAUSALITY","kind":"CAUSAL_GAP","lead":"Campaign-finance mechanism to political command or electoral outcome","linked_ids":["CLM-002","CLM-006","CAU-001","CTRL-006"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-008","FCT-016","FCT-019","FCT-020","FCT-021","FCT-022","FCT-023","FCT-024"],"route":"INV-095/INV-102","routes":["INV-095","INV-102"],"source_id":"INV-093_RUN_CARD","status":"GAP","support":["FCT-008","FCT-016","FCT-019","FCT-020","FCT-021","FCT-022","FCT-023","FCT-024"]}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"French campaign financing is a multi-channel regulated system combining candidate resources, donations, loans, party financing, services/in-kind support and public reimbursement under account-control rules.","claimant":"INV-093 synthesis","counter":"CTRL-001","gap":"Regulation does not imply complete upstream traceability of every fund source.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-004","FCT-005","FCT-006","FCT-016","FCT-020","FCT-021","FCT-022","FCT-023","FCT-024"]}
CLM-002 | {"claim":"Loans, party loans and micro-party or party service vehicles are not illicit by category; legality depends on lender status, terms, accounting, pricing, disclosure and case-specific conduct.","claimant":"INV-093 synthesis","counter":"CTRL-002;CTRL-004","gap":"Specific abusive arrangements remain possible and must be proven transaction by transaction.","gap_type":"QUALIFICATION","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-004","FCT-021","FCT-022","FCT-023","FCT-024","FCT-028"]}
CLM-003 | {"claim":"CNCCFP approval, reform, reimbursement modulation, rejection, election-judge referral and prosecutor transmission are distinct control outcomes and cannot be collapsed into a single fraud category.","claimant":"INV-093 synthesis","counter":"CTRL-003","gap":"Administrative irregularity can coexist with or later lead to criminal facts, but the legal findings remain distinct.","gap_type":"QUALIFICATION","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-006","FCT-007","FCT-008","FCT-017","FCT-018","FCT-019"]}
CLM-004 | {"claim":"The Sarkozy/Bygmalion sequence shows that a final campaign-account ruling and a later criminal proceeding can coexist: account overrun/rejection and criminal concealment or illegal-financing offences are distinct adjudicative tracks.","claimant":"INV-093 synthesis","counter":"CTRL-003","gap":"The criminal judgment does not turn every accounting reform or overrun into fraud.","gap_type":"QUALIFICATION","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015"]}
CLM-005 | {"claim":"A micro-party/association and campaign-service structure can be used in an unlawful financing scheme, as shown case-specifically by the Jeanne-related criminal litigation, but that does not make the vehicle type inherently fraudulent.","claimant":"INV-093 synthesis","counter":"CTRL-004","gap":"General prevalence of abusive micro-party pricing or supplier-credit structures is not established by one final case.","gap_type":"COVERAGE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-028"]}
CLM-006 | {"claim":"Campaign-finance control has a material origin-of-funds gap for some physical-person loans/donations, while the examined evidence does not establish political command or a changed electoral result from ordinary financing channels.","claimant":"INV-093 synthesis","counter":"CTRL-005;CTRL-006","gap":"Beneficial origin and causal electoral effect require separate evidence.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-025","FCT-026","FCT-027"]}

### AXIS_REGISTRY_V1
AXS-001 | {"assessment":"VERIFIED","attempt_ids":["QRY-001","QRY-002","QRY-003"],"axis":"legal_sources_and_limits","links":["CLM-001","CLM-002"],"question":"What sources of campaign funds and support are legally allowed or prohibited?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005"],"sought_objects":["DONATION","LOAN","LEGAL_PERSON_SUPPORT","FOREIGN_CONTRIBUTION","CAMPAIGN_ACCOUNT"],"status":"SATURATED","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005"]}
AXS-002 | {"assessment":"VERIFIED","attempt_ids":["QRY-002","QRY-011","QRY-012","QRY-014"],"axis":"loan_and_party_financing","links":["CLM-001","CLM-002","CTRL-002"],"question":"Are loans and party financing exceptional workarounds or normal documented mechanisms?","result_ids":["FCT-004","FCT-020","FCT-021","FCT-022","FCT-023","FCT-024","FCT-025","FCT-026"],"sought_objects":["PHYSICAL_PERSON_LOAN","PARTY_LOAN","MIRROR_LOAN","PARTY_CONTRIBUTION"],"status":"SATURATED","support":["FCT-004","FCT-021","FCT-022","FCT-023","FCT-024","FCT-025","FCT-026"]}
AXS-003 | {"assessment":"VERIFIED","attempt_ids":["QRY-001","QRY-003","QRY-006","QRY-009","QRY-013"],"axis":"service_in_kind_accounting","links":["CLM-001","CLM-005","CTRL-004"],"question":"How are services, third-party expenses and in-kind advantages treated in campaign accounts?","result_ids":["FCT-002","FCT-005","FCT-010","FCT-017","FCT-028"],"sought_objects":["SERVICE","IN_KIND_SUPPORT","THIRD_PARTY_EXPENSE","CAMPAIGN_KIT","SUPPLIER_CREDIT"],"status":"SATURATED","support":["FCT-002","FCT-005","FCT-010","FCT-017","FCT-028"]}
AXS-004 | {"assessment":"VERIFIED_DISTINCT_OUTCOMES","attempt_ids":["QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010"],"axis":"irregularity_severity_and_sanction","links":["CLM-003","CLM-004","CTRL-003"],"question":"Do account irregularities map automatically to fraud, rejection or criminal liability?","result_ids":["FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-017","FCT-018","FCT-019"],"sought_objects":["REFORM","MODULATION","REJECTION","CEILING_OVERRUN","CRIMINAL_OFFENCE"],"status":"SATURATED","support":["FCT-006","FCT-008","FCT-017","FCT-018","FCT-019","FCT-014","FCT-015"]}
AXS-005 | {"assessment":"VERIFIED_CASE_SPECIFIC","attempt_ids":["QRY-013"],"axis":"micro_party_service_vehicle","links":["CLM-002","CLM-005","CTRL-004"],"question":"Can a micro-party/association/service vehicle facilitate unlawful financing and is the vehicle inherently illicit?","result_ids":["FCT-028"],"sought_objects":["ASSOCIATION","MICRO_PARTY","CAMPAIGN_KIT","SUPPLIER_CREDIT","CRIMINAL_FINDING"],"status":"SATURATED","support":["FCT-028"]}
AXS-006 | {"assessment":"NOT_ESTABLISHED","attempt_ids":["QRY-005","QRY-009","QRY-010","QRY-011","QRY-012","QRY-014"],"axis":"political_electoral_effect","gap":"No examined source or comparative causal design establishes that a lawful financing channel by itself commanded a candidate or changed the electoral outcome.","gap_type":"CAUSALITY","links":["CLM-006","CAU-001","LED-002"],"question":"Does the financing mechanism establish political command or a counterfactual change in electoral outcome?","result_ids":["FCT-016","FCT-019","FCT-020","FCT-021","FCT-022","FCT-023","FCT-024","FCT-027"],"sought_objects":["POLITICAL_COMMAND","VOTER_PERSUASION","COUNTERFACTUAL_RESULT"],"status":"GAP","support":["FCT-016","FCT-020","FCT-021","FCT-022","FCT-023","FCT-024"]}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"Normal loans, party financing, account reforms and reimbursement modulation interrupt any inference from financing to illegality; no causal evidence closes political command or electoral-result edges.","from":"source of funds / financing vehicle","gap":"Upstream beneficial origin of some individual funds and downstream political/electoral counterfactual effect remain unestablished.","gap_type":"CAUSALITY","limit":"I0-I4 are strongly supported case-specifically for fund/vehicle/transaction/rule/control-consequence; political command, voter persuasion and counterfactual result are not established.","limits":["loan != illicit_financing","irregularity != fraud","reformed_account != corruption","funding != political_command","institutional_consequence != electoral_result"],"mechanism":"fund source -> donation/loan/party or service vehicle -> campaign receipt/expense -> campaign account -> CNCCFP control/reform/reject -> judge/prosecutor -> reimbursement/Treasury/criminal consequence -> possible political/electoral effect","status":"UNRESOLVED","support":["FCT-001","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-014","FCT-015","FCT-028"],"to":"account control -> administrative/criminal consequence -> political/electoral effect"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Normal-mechanism control: donations, bank/party loans, definitive party contributions and physical-person loans are recognized financing channels subject to distinct rules.","status":"DONE","support":["FCT-001","FCT-004","FCT-020","FCT-021","FCT-022","FCT-023","FCT-024","FCT-026"]}
CTRL-002 | {"control":"Loan control: all 2022 presidential candidates had a party loan and six had mirror-loan structures; a loan or mirror loan is therefore not evidence of illicit financing by itself.","status":"DONE","support":["FCT-021","FCT-022","FCT-023"]}
CTRL-003 | {"control":"Severity control: 2017 Fillon and Macron account irregularities were reformed/modulated without rejection, while 2012 Sarkozy account rejection and later Bygmalion criminal convictions arise from materially different findings.","status":"DONE","support":["FCT-009","FCT-012","FCT-014","FCT-015","FCT-017","FCT-018"]}
CTRL-004 | {"control":"Vehicle control: the Jeanne case shows an association/service vehicle can be abused case-specifically, but does not make every micro-party, association, service contract or supplier-credit arrangement fraudulent.","status":"DONE","support":["FCT-028"]}
CTRL-005 | {"control":"Traceability control: CNCCFP reports an upstream origin-of-funds gap for some individual loans/donations despite detailed campaign-account controls.","status":"DONE","support":["FCT-025","FCT-026","FCT-027"]}
CTRL-006 | {"control":"Causality control: financing, reimbursement, reform, rejection or conviction can have institutional consequences but do not by themselves prove command of the candidate, voter persuasion or a changed election result.","status":"DONE","support":["FCT-006","FCT-008","FCT-014","FCT-015","FCT-019"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:14|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | MNEMO_UNAVAILABLE degraded; exact snapshot search unavailable in this environment | MnemoLite | NONE | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | PASS | SRC-001 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039446180 | FETCH exact Code électoral L52-8 financing donations legal persons foreign funding
QRY-002 | FETCH | PASS | SRC-002 | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000035570026 | FETCH exact Code électoral L52-7-1 physical-person campaign loans
QRY-003 | FETCH | PASS | SRC-003 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000052092735 | FETCH exact Code électoral L52-12 campaign account receipts expenses
QRY-004 | FETCH | PASS | SRC-004 | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000039446173/2026-05-25 | FETCH exact Code électoral L52-15 CNCCFP approve reject reform prosecutor Treasury
QRY-005 | FETCH | PASS | SRC-005 | https://cnccfp.fr/elections/ | FETCH exact CNCCFP elections account workflow decisions reimbursement
QRY-006 | FETCH | PASS | SRC-006 | https://www.cnccfp.fr/wp-content/uploads/2013/05/cnccfp_activite_2012_2013.pdf | FETCH exact CNCCFP 2012-2013 Sarkozy campaign account rejection
QRY-007 | FETCH | PASS | SRC-007 | https://www.legifrance.gouv.fr/cons/id/CONSTEXT000028024281 | FETCH exact Conseil constitutionnel 2013-156 PDR Sarkozy campaign account
QRY-008 | FETCH | PASS | SRC-008 | https://www.courdecassation.fr/decision/6926ab8a77bf00d0f5ea186d | FETCH exact Cour de cassation 24-82.486 Bygmalion financing campaign 2012
QRY-009 | FETCH | PASS | SRC-009 | https://www.cnccfp.fr/wp-content/uploads/2017/05/cnccfp_rapport_activite_2017.pdf | FETCH exact CNCCFP 2017 presidential accounts financing sources Fillon Macron irregularities
QRY-010 | FETCH | PASS | SRC-010 | https://cnccfp.fr/election-presidentielle-des-10-et-24-avril-2022-publication-au-journal-officiel-des-decisions-de-la-commission/ | FETCH exact CNCCFP presidential 2022 decisions accounts reform
QRY-011 | FETCH | PASS | SRC-011 | https://www.cnccfp.fr/wp-content/uploads/2023/06/cnccfp-rapport_activite_2022-synthese.pdf | FETCH exact CNCCFP 2022 presidential aggregate expenses receipts donations party contributions
QRY-012 | FETCH | PASS | SRC-012 | https://www.cnccfp.fr/wp-content/uploads/2024/06/cnccfp-rapport_2023-web.pdf | FETCH exact CNCCFP 2023 report presidential 2022 party loans mirror loans 38 parties
QRY-013 | FETCH | PASS | SRC-013 | https://www.courdecassation.fr/decision/6672836f8111810008ba932a | FETCH exact Cour de cassation 23-82.194 kits campaign micro-party Jeanne 2012
QRY-014 | FETCH | PASS | SRC-014 | https://www.vie-publique.fr/files/rapport/pdf/299362.pdf | FETCH exact CNCCFP 2024 report origin funds bank loans physical-person loans campaign

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | LEGIARTI000039446180 | Code électoral — article L52-8 | 2020-06-30 | 2026-09-07T18:23:00+02:00 | Article L52-8, version en vigueur depuis 30/06/2020 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039446180
SRC-002 | ◈ | fam:A | LEGIARTI000035570026 | Code électoral — article L52-7-1 | 2018-01-01 | 2026-09-07T18:23:00+02:00 | Article L52-7-1, version en vigueur depuis 01/01/2018 | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000035570026
SRC-003 | ◈ | fam:A | LEGIARTI000052092735 | Code électoral — article L52-12 | 2026-04-09 | 2026-09-07T18:23:00+02:00 | Article L52-12, version en vigueur depuis 09/04/2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000052092735
SRC-004 | ◈ | fam:A | LEGIARTI000039446173 | Code électoral — article L52-15 | 2020-06-30 | 2026-09-07T18:23:00+02:00 | Article L52-15, version en vigueur depuis 30/06/2020 | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000039446173/2026-05-25
SRC-005 | ◈ | fam:B | CNCCFP-ELECTIONS-WORKFLOW | Élections et comptes de campagne — CNCCFP | 2026-09-07 | 2026-09-07T18:23:00+02:00 | Sections obligations du mandataire, décisions, remboursement, parcours du compte | https://cnccfp.fr/elections/
SRC-006 | ◈ | fam:B | CNCCFP-RA-2012-2013 | CNCCFP — Quinzième rapport d'activité 2012-2013 | 2013-05-01 | 2026-09-07T18:23:00+02:00 | p.45, section c) La décision de rejet | https://www.cnccfp.fr/wp-content/uploads/2013/05/cnccfp_activite_2012_2013.pdf
SRC-007 | ◈ | fam:C | ECLI:FR:CC:2013:2013.156.PDR | Décision n° 2013-156 PDR du 4 juillet 2013 | 2013-07-04 | 2026-09-07T18:23:00+02:00 | Décision 2013-156 PDR, dispositif art. 2-4 et motifs | https://www.legifrance.gouv.fr/cons/id/CONSTEXT000028024281
SRC-008 | ◈ | fam:D | ECLI:FR:CCASS:2025:CR01455 | Cour de cassation, crim., 26 novembre 2025, n°24-82.486 | 2025-11-26 | 2026-09-07T18:23:00+02:00 | Faits/procédure; motifs 25-29; dispositif | https://www.courdecassation.fr/decision/6926ab8a77bf00d0f5ea186d
SRC-009 | ◈ | fam:B | CNCCFP-RA-2017 | CNCCFP — Rapport d'activité 2017 | 2018-04-30 | 2026-09-07T18:23:00+02:00 | pp.29-35, 47-50; sections contrôle, recettes, modulation | https://www.cnccfp.fr/wp-content/uploads/2017/05/cnccfp_rapport_activite_2017.pdf
SRC-010 | ◈ | fam:B | CNCCFP-PRES-2022-DECISIONS | Présidentielle 2022 — décisions CNCCFP | 2023-01-27 | 2026-09-07T18:23:00+02:00 | Publication des décisions du 14 décembre 2022 | https://cnccfp.fr/election-presidentielle-des-10-et-24-avril-2022-publication-au-journal-officiel-des-decisions-de-la-commission/
SRC-011 | ◈ | fam:B | CNCCFP-RA-2022-PRES | CNCCFP — Rapport d'activité 2022, tiré à part présidentielle | 2023-06-15 | 2026-09-07T18:23:00+02:00 | Infographie grands chiffres de la présidentielle 2022 | https://www.cnccfp.fr/wp-content/uploads/2023/06/cnccfp-rapport_activite_2022-synthese.pdf
SRC-012 | ◈ | fam:B | CNCCFP-RA-2023 | CNCCFP — Rapport d'activité 2023 | 2024-06-01 | 2026-09-07T18:23:00+02:00 | p.84, rapprochement comptes présidentielle 2022 | https://www.cnccfp.fr/wp-content/uploads/2024/06/cnccfp-rapport_2023-web.pdf
SRC-013 | ◈ | fam:D | ECLI:FR:CCASS:2024:CR00817 | Cour de cassation, crim., 19 juin 2024, n°23-82.194 | 2024-06-19 | 2026-09-07T18:23:00+02:00 | Faits/procédure §§2-10; réponse §§18-25; dispositif | https://www.courdecassation.fr/decision/6672836f8111810008ba932a
SRC-014 | ◉ | fam:E | VIEPUB-CNCCFP-RA-2024 | CNCCFP — Rapport d'activité 2024 (diffusion Vie-publique) | 2025-07-01 | 2026-09-07T18:23:00+02:00 | p.51, origine des fonds apportés par les candidats | https://www.vie-publique.fr/files/rapport/pdf/299362.pdf

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039446180 | A | 2020-06-30 | Donation cap | A person physically resident in France or of French nationality may donate to a candidate, with donations capped at EUR 4,600 for the same elections. | -
FCT-002 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039446180 | A | 2020-06-30 | Corporate contribution prohibition | Legal persons other than political parties/groupings may not finance a candidate by donations or by supplying goods, services or advantages below usual prices. | -
FCT-003 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039446180 | A | 2020-06-30 | Foreign contribution boundary | A candidate may not receive contributions or material assistance from a foreign State or foreign legal person; loans from foreign legal persons are also prohibited except qualifying EU/EEA credit or finance institutions. | -
FCT-004 | FACT | ✧ | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000035570026 | A | 2018-01-01 | Physical-person loans | Physical persons may lend to a candidate when not doing so habitually; such loans are limited to five years and must be reported annually for repayment follow-up. | -
FCT-005 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000052092735 | A | 2026-04-09 | Campaign account completeness | The campaign account must trace all campaign receipts by origin and campaign expenses by nature, including qualifying expenses made for the candidate by supporters and supporting political parties. | -
FCT-006 | FACT | ✧ | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000039446173/2026-05-25 | A | 2020-06-30 | CNCCFP decision powers | CNCCFP may approve, reject or reform campaign accounts after an adversarial procedure and determines the statutory reimbursement. | -
FCT-007 | FACT | ✧ | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000039446173/2026-05-25 | A | 2020-06-30 | Escalation and Treasury consequence | Non-filing, rejection or a post-reform ceiling overrun triggers referral to the election judge; suspected statutory irregularities may be transmitted to prosecutors, and a final ceiling overrun creates a Treasury payment equal to the overrun. | -
FCT-008 | FACT | ✧ | https://cnccfp.fr/elections/ | B | 2026-09-07 | Control workflow | CNCCFP describes approval, approval after reform, rejection for substantive or particularly serious irregularity, and reimbursement modulation as distinct outcomes. | -
FCT-009 | FACT | ✧ | https://www.cnccfp.fr/wp-content/uploads/2013/05/cnccfp_activite_2012_2013.pdf | B | 2012-12-19 | Sarkozy 2012 CNCCFP rejection | CNCCFP rejected Nicolas Sarkozy’s 2012 presidential campaign account, initially finding a EUR 363,615 ceiling overrun. | -
FCT-010 | FACT | ✧ | https://www.cnccfp.fr/wp-content/uploads/2013/05/cnccfp_activite_2012_2013.pdf | B | 2012-12-19 | Sarkozy 2012 reintegrations | CNCCFP reported EUR 1,567,425 of reintegrations, 7.35% of declared spending, showing material omissions from the filed account. | -
FCT-011 | FACT | ✧ | https://www.cnccfp.fr/wp-content/uploads/2013/05/cnccfp_activite_2012_2013.pdf | B | 2012-12-19 | Sarkozy 2012 prohibited legal-person support | CNCCFP also treated election-related presidential events paid from the State budget without reimbursement to the financial agent as a prohibited legal-person contribution. | -
FCT-012 | FACT | ✧ | https://www.legifrance.gouv.fr/cons/id/CONSTEXT000028024281 | C | 2013-07-04 | Constitutional Council final account | After reform, the Constitutional Council fixed Sarkozy’s 2012 account at EUR 22,975,118 of expenses and EUR 23,094,932 of receipts and rejected the remainder of his appeal. | -
FCT-013 | FACT | ✧ | https://www.legifrance.gouv.fr/cons/id/CONSTEXT000028024281 | C | 2013-07-04 | Final 2012 ceiling overrun | The Constitutional Council’s 2013-156 PDR decision retained an authorised-ceiling overrun of EUR 466,118. | -
FCT-014 | FACT | ✧ | https://www.courdecassation.fr/decision/6926ab8a77bf00d0f5ea186d | D | 2025-11-26 | Bygmalion final criminal judgment | The Cour de cassation rejected the appeals from the 2024 Paris appeal judgment and thereby confirmed criminal convictions including illegal campaign financing connected with the 2012 presidential campaign. | -
FCT-015 | FACT | ✧ | https://www.courdecassation.fr/decision/6926ab8a77bf00d0f5ea186d | D | 2025-11-26 | Administrative-account versus criminal track | The Cour de cassation held that the Constitutional Council campaign-account decision does not generally extinguish the distinct criminal adjudication; its res judicata effect is bounded to the relevant candidate obligations/offences. | -
FCT-016 | FACT | ✧ | https://www.cnccfp.fr/wp-content/uploads/2017/05/cnccfp_rapport_activite_2017.pdf | B | 2017 | 2017 financing structure | For the 2017 presidential election CNCCFP reported EUR 74.9 million in total receipts and documented a mixed financing structure including personal resources, bank loans, party loans/contributions, individual donations and in-kind support. | -
FCT-017 | FACT | ✧ | https://www.cnccfp.fr/wp-content/uploads/2017/05/cnccfp_rapport_activite_2017.pdf | B | 2017-12-21 | Fillon omitted expenses control | CNCCFP found EUR 88,349 of omitted campaign expenses and prohibited in-kind use of four meeting rooms in François Fillon’s 2017 account; it reformed the account and reduced reimbursement by EUR 50,000 rather than rejecting it. | -
FCT-018 | FACT | ✧ | https://www.cnccfp.fr/wp-content/uploads/2017/05/cnccfp_rapport_activite_2017.pdf | B | 2017-12-21 | Macron over-limit donations control | Emmanuel Macron’s 2017 account reported EUR 1,016,758 of individual donations; CNCCFP examined EUR 87,600 apparently exceeding the per-person cap, accepted spouse attribution/good faith in 20 of 24 cases, retained EUR 18,300 of excess in four cases and reduced reimbursement without rejecting the account. | -
FCT-019 | FACT | ✧ | https://cnccfp.fr/election-presidentielle-des-10-et-24-avril-2022-publication-au-journal-officiel-des-decisions-de-la-commission/ | B | 2022-12-14 | 2022 presidential account outcomes | CNCCFP states that the eleven 2022 presidential decisions published in January 2023 all approved the candidates’ accounts after reform; Marine Le Pen’s decision was published separately because she appealed. | -
FCT-020 | FACT | ✧ | https://www.cnccfp.fr/wp-content/uploads/2023/06/cnccfp-rapport_activite_2022-synthese.pdf | B | 2022 | 2022 aggregate campaign finance | For the 2022 presidential election CNCCFP reported EUR 83.5 million declared expenses, EUR 85.2 million declared receipts, EUR 42.2 million State reimbursement, EUR 9 million declared donations and EUR 27 million party contributions. | -
FCT-021 | FACT | ✧ | https://www.cnccfp.fr/wp-content/uploads/2024/06/cnccfp-rapport_2023-web.pdf | B | 2022 | Party participation breadth 2022 | CNCCFP later identified 38 political parties participating financially in the 12 presidential candidates’ 2022 campaigns. | -
FCT-022 | FACT | ✧ | https://www.cnccfp.fr/wp-content/uploads/2024/06/cnccfp-rapport_2023-web.pdf | B | 2022 | Party loans normal mechanism | All 12 presidential candidates in 2022 benefited from a loan from a political formation; for nine candidates the loan was the largest form of party intervention. | -
FCT-023 | FACT | ✧ | https://www.cnccfp.fr/wp-content/uploads/2024/06/cnccfp-rapport_2023-web.pdf | B | 2022 | Mirror loans | For six 2022 presidential candidates, the lending party had itself borrowed from a bank to finance the candidate loan, a mechanism CNCCFP calls a mirror loan. | -
FCT-024 | FACT | ✧ | https://www.cnccfp.fr/wp-content/uploads/2024/06/cnccfp-rapport_2023-web.pdf | B | 2022 | Definitive party contributions variant | For Valérie Pécresse, Anne Hidalgo and Yannick Jadot, definitive party contributions rather than loans were the largest part of party intervention. | -
FCT-025 | FACT | ✧ | https://www.vie-publique.fr/files/rapport/pdf/299362.pdf | E | 2024 | Bank-loan trend | CNCCFP reported the share of bank borrowing in candidate financing falling from 23% in 2017 to 18% in 2022 and 8% in 2024 legislative elections. | -
FCT-026 | FACT | ✧ | https://www.vie-publique.fr/files/rapport/pdf/299362.pdf | E | 2024 | Physical-person loan trend | CNCCFP reported physical-person loans rising from 5% of financing in 2017 to 9% in 2022 and 13% in 2024. | -
FCT-027 | FACT | ✧ | https://www.vie-publique.fr/files/rapport/pdf/299362.pdf | E | 2024 | Origin-of-funds control gap | CNCCFP states that it asks candidates to justify the origin of large personal contributions but lacks sufficient statutory means to establish the origin of funds lent by physical persons or donated, leaving a real origin-of-funds control gap. | -
FCT-028 | FACT | ✧ | https://www.courdecassation.fr/decision/6672836f8111810008ba932a | D | 2024-06-19 | Micro-party Jeanne campaign-kit mechanism | In case 23-82.194, the Cour de cassation records that a political association and a company were mandated around 2012 legislative campaigns, with a paid campaign-kit system, supplier credit and other corporate support; the criminal proceedings produced convictions for fraud-related and concealment offences. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-002
FCT-005 | SRC-003
FCT-006 | SRC-004
FCT-007 | SRC-004
FCT-008 | SRC-005
FCT-009 | SRC-006
FCT-010 | SRC-006
FCT-011 | SRC-006
FCT-012 | SRC-007
FCT-013 | SRC-007
FCT-014 | SRC-008
FCT-015 | SRC-008
FCT-016 | SRC-009
FCT-017 | SRC-009
FCT-018 | SRC-009
FCT-019 | SRC-010
FCT-020 | SRC-011
FCT-021 | SRC-012
FCT-022 | SRC-012
FCT-023 | SRC-012
FCT-024 | SRC-012
FCT-025 | SRC-014
FCT-026 | SRC-014
FCT-027 | SRC-014
FCT-028 | SRC-013

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
ATTEMPT-001 | {"created_at":"2026-09-07T16:32:16.165907+00:00","fact_mem":{},"mnemo_row":"BLOCKED:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":28,"eligible":28,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:BLOCKED:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:28;attempted:0;success:0;failure:0;blocked:28} | WRITEBACK_EXECUTION_V1:[28 rows, see section]

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
