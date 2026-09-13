ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260907-1946-foreign-party-financing-europe | PARENT_RUN_ID:NONE | AS_OF:2026-09-07
INPUT_KIND:RUN_CARD | MISSION_MODE:DEEPEN | INPUT_REF:PATH:/mnt/data/inv094-exec/te/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-07_foreign-party-financing-europe/2026-09-07_19-46_foreign-party-financing-europe_INPUT.md | SUBJECT_SLUG:foreign-party-financing-europe | SUBJECT_FP:sha256:5579e77631b2a7b2c3f7e71530bd0f5e0163bab16ce71504e14879101c988b59 | INPUT_SHA256:sha256:85349d47bde2167889c50ff4d26736f0d3c49541ff6fdeb13acb0aed33460fbf
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/Europe 2012-2026; direct or indirect foreign-origin money or financial advantages reaching parties/candidates; trace principal, vehicle, transfer, law/control, decision/sanction, tasking and effect; complement INV-093 and INV-140.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/MONEY.md,clusters/POWER.md,clusters/NETWORK.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "truth_engine_narrative"
artifact_id: "INV-094-NARRATIVE"
version: "1.0"
status: "technical_frozen"
updated: "2026-09-07"
inv_id: "INV-094"
---

<!-- TRACE: run=20260907-1946-foreign-party-financing-europe; engine=2.10.6/R3P1; facts=FCT-001..FCT-028 -->

# INV-094 — Financement étranger direct ou indirect des partis et candidats européens

## Question et règle de preuve

Cette enquête ferme le bord laissé ouvert par INV-093 : lorsqu'un financement a une origine étrangère ou transite par un véhicule étranger, que peut-on réellement établir sur sa légalité, son bénéficiaire économique, un éventuel commandement politique et son effet électoral ?

La chaîne testée est : `principal étranger -> banque/personne/société/intermédiaire -> prêt/don/avantage -> parti ou candidat -> règle applicable -> contrôle/décision -> contrepartie ou tasking éventuel -> effet politique -> résultat électoral`. Chaque flèche reste indépendante. Les gardes sont donc : `foreign funding != interference`, `funding != command`, `loan != donation`, `intermediary != concealed principal`, `illegality != electoral effect`, `sanction != result changed`.

## 1. Le droit européen comparé ne traite pas « l'argent étranger » comme une catégorie unique

En France, le changement de 2017-2018 est matériel. Avant 2018, le code électoral et le régime de financement des partis interdisaient déjà les contributions et aides matérielles provenant d'un État étranger ou d'une personne morale étrangère, mais les versions examinées ne contenaient pas encore l'interdiction expresse ultérieure des prêts étrangers. Depuis 2018, les prêts d'un État étranger ou d'une personne morale de droit étranger sont expressément interdits, sauf établissements de crédit ou sociétés de financement répondant aux conditions UE/EEE. Pour les partis, les dons de personnes physiques sont en outre réservés aux personnes françaises ou résidant en France. [FCT-001 à FCT-007]

Cette architecture ne se généralise pas telle quelle à toute l'Europe. En Espagne, la loi organique permet des dons non affectés de personnes physiques étrangères sous les limites générales et les règles de mouvements de capitaux, tout en interdisant les financements de gouvernements, organismes et entreprises publiques étrangers ou d'entreprises qui leur sont liées. [FCT-019, FCT-020]

Pour les partis politiques européens, le règlement 1141/2014 interdit notamment les dons anonymes, ceux d'autorités publiques de pays tiers, ceux d'entreprises dominées par elles, ainsi que ceux d'entités privées établies dans un pays tiers et de certaines personnes de pays tiers non électrices aux élections européennes. Les dons non permis doivent être retournés ou faire l'objet d'une procédure de récupération. [FCT-021 à FCT-023]

Le Royaume-Uni applique encore une autre logique de « source permissible » : l'identité réelle du donateur et son éligibilité doivent être vérifiées au-dessus du seuil légal, et les fonds non identifiables ou non permis doivent être retournés. [FCT-024]

Le premier résultat est donc net : **origine étrangère et illégalité ne sont pas synonymes sans qualification de la juridiction, du type de source et du véhicule**. Une personne physique étrangère peut être admissible en Espagne dans des conditions où un État étranger ne l'est pas ; un établissement bancaire UE/EEE peut être admissible comme prêteur dans le droit français post-2018 là où une autre personne morale étrangère ne l'est pas.

## 2. Le prêt FN/RN–First Czech Russian Bank est un cas réel de financement étranger, mais un cas de droit ancien

Le Sénat documente qu'en 2014 le Front national a bénéficié d'un prêt supérieur à 9,1 millions d'euros de First Czech Russian Bank, établissement bancaire russe. Après la faillite de la banque en 2016, la créance a été reprise par la société russe Aviazapchast. Le prêt a été renégocié en 2019. [FCT-008, FCT-009]

Le point juridique décisif est temporel : le prêt a été contracté sous les règles antérieures à l'entrée en vigueur de la réforme de 2017, et la loi nouvelle a expressément préservé les contrats antérieurs. Le parti pouvait donc conserver cette dette au passif pendant son remboursement. [FCT-001, FCT-004, FCT-007, FCT-009]

Cela ferme deux erreurs symétriques. Premièrement, le prêt n'est pas une invention ou une simple allégation : sa source bancaire étrangère et sa chaîne de créance sont établies dans un document parlementaire officiel. Deuxièmement, l'existence de cette dette ne prouve pas qu'un prêt identique serait aujourd'hui juridiquement admissible sous les mêmes conditions ; le droit français a précisément été durci.

La limite probatoire est tout aussi importante. Auditionné par la commission d'enquête du Sénat, le président de la CNCCFP a indiqué que la Commission n'avait jamais pris une position permettant de qualifier positivement ce prêt d'« ingérence » et qu'elle ne disposait d'aucun moyen de savoir s'il était ou non assorti de contreparties. [FCT-010]

Le résultat correct est donc : `prêt étranger établi + dette/chaîne de créance établies + régime ancien établi`, mais `contrepartie politique`, `tasking`, `commandement` et `effet électoral` non établis par ce dossier réglementaire. Dire « financement étranger » est factuel ; dire « commandement étranger » exige une autre preuve.

## 3. Le dossier AfD montre pourquoi l'intermédiaire n'est pas le principal

Le cas allemand fournit un autre mécanisme. En 2017, dix-sept virements totalisant environ 132 000 euros sont arrivés depuis les comptes de deux sociétés suisses sur un compte de l'AfD Bodensee avec une mention les reliant à la campagne numérique d'Alice Weidel. [FCT-011]

L'enquête administrative et pénale a toutefois compliqué la chaîne d'attribution. La liste de donateurs produite par le parti comprenait des personnes qui ont ensuite indiqué ne pas avoir donné ; le parti a déclaré ne pas disposer d'informations fiables sur le véritable donateur. Le rapport du Bundestag indique qu'une enquête assistée par les autorités suisses a finalement fait apparaître le nom d'un donateur présumé, décrit comme un entrepreneur immobilier allemand résidant en Suisse. [FCT-012]

La décision de l'Oberverwaltungsgericht Berlin-Brandenburg ferme encore plus précisément le bord pertinent : économiquement, le don n'était pas attribuable aux deux sociétés suisses de transfert, mais à un donateur non identifié dans le constat juridictionnel. La juridiction a également rejeté l'argument d'un don direct à la candidate : le versement sur le compte du parti contribuait à le qualifier comme don au parti. [FCT-013, FCT-014]

La conséquence institutionnelle est forte : environ 396 000 euros de sanction, soit le triple du montant du don. [FCT-015, FCT-018]

Mais la qualification correcte reste bornée. Le dossier démontre qu'un véhicule étranger peut masquer ou ne pas révéler le bénéficiaire économique réel du flux et qu'une telle opacité peut produire une violation et une sanction lourdes. Il ne démontre pas, dans les pièces examinées, qu'un État étranger était le principal, ni que les sociétés suisses étaient elles-mêmes le principal économique, ni qu'un tasking étatique pilotait le parti. **Le pays du compte de transit n'est pas une preuve de la nationalité ou de la qualité du principal.**

## 4. Une violation de financement n'est pas automatiquement une preuve de corruption ou de commandement

Le rapport du Bundestag fournit ici un contrôle particulièrement utile. Pour qu'un don soit qualifié d'« influence donation » au sens du droit allemand, il faut une convention expresse ou implicite mais reconnaissable reliant le don à un avantage économique ou politique déterminé. Le rapport précise également que la proximité temporelle entre un don et une décision publique favorable ne suffit pas, à elle seule, à établir cette qualification. [FCT-016, FCT-017]

Ce seuil est cohérent avec la séparation nécessaire entre plusieurs étages :

`source étrangère -> donation interdite ou anonyme -> sanction` peut être démontré sans que `contrepartie spécifique -> commandement -> acte politique` le soit.

Le droit et les autorités ne traitent donc pas l'irrégularité financière comme une preuve automatique de corruption. Cette distinction est centrale pour INV-095 : un financeur peut avoir fourni une ressource matérielle ; il faut encore établir un accès particulier, une dette politique, une contrepartie, un pouvoir de sélection ou un tasking si l'on veut passer du financement au contrôle du candidat.

## 5. Les contrôles britanniques cassent deux inférences trop faciles

L'enquête de l'Electoral Commission sur UKIP et les structures européennes ADDE/IDDE constitue un bon contrôle négatif. Le polling financé par ces structures portait sur des zones et sujets potentiellement stratégiques pour UKIP, et deux prestataires avaient aussi occupé des fonctions de campaign managers pour des candidats UKIP. Pourtant, après collecte documentaire et auditions, la Commission a conclu qu'elle ne disposait pas de preuves suffisantes pour établir que les sondages avaient été commandés au bénéfice de UKIP ou que UKIP en avait reçu ou tiré bénéfice. Elle a donc conclu qu'ils ne constituaient pas un don à UKIP au sens du droit britannique. [FCT-027]

La Commission a en outre explicité que son appréciation d'une infraction devait satisfaire le standard pénal applicable, ce qui explique qu'elle puisse différer d'une appréciation institutionnelle européenne du même environnement factuel. [FCT-028]

Ce contrôle est important : `pertinence stratégique + chevauchement de personnes + financement externe` ne suffit pas à démontrer `avantage effectivement transféré au parti`.

Le contrôle Brexit Party produit une borne différente. L'Electoral Commission a estimé qu'une architecture de collecte en ligne créait un risque élevé et persistant d'accepter des dons non permis, et le parti a retourné un don de 1 000 livres parce qu'il ne pouvait pas déterminer si la source était permissible. [FCT-025, FCT-026]

Là encore, le bon verdict n'est pas « financement étranger démontré », mais `risque de conformité établi + mécanisme de retour utilisé + origine admissible non vérifiable dans un cas`. Le risque n'est pas l'acte prouvé.

## 6. Ce qui est établi, ce qui ne l'est pas

Le corpus ferme solidement I0 à I4 dans plusieurs cas : catégorie de source, véhicule, transfert, règle juridique, décision administrative ou judiciaire et sanction. Le prêt RN et les virements AfD démontrent que des flux d'origine ou de transit étrangers vers des structures partisanes sont des objets réels, et pas seulement des hypothèses. Les régimes français, allemand, espagnol, européen et britannique montrent simultanément que la qualification juridique varie fortement selon la source et la structure.

En revanche, **I5 n'est pas généralisable à partir du financement**. Le corpus ne ferme pas une chaîne générale `financeur étranger -> ordre politique -> comportement du candidat`. Dans le cas RN, la CNCCFP dit précisément ne pas disposer de preuve de contreparties. Dans le cas allemand, le standard de preuve d'une convention de contrepartie est plus exigeant que la seule existence du don. Dans le contrôle UKIP, le bénéfice lui-même n'est pas établi malgré la proximité organisationnelle.

I6 et I7 restent plus faibles encore. Aucune source examinée ne fournit un design permettant d'isoler une persuasion des électeurs ou de démontrer qu'un financement étranger donné a changé le vainqueur ou le résultat contrefactuel d'une élection.

## Conclusion opérationnelle

INV-094 ferme le principal trou laissé par INV-093 sur la **qualification de l'argent étranger** :

1. des financements étrangers directs ou indirects de partis/candidats existent et peuvent être documentés ;
2. la légalité dépend du régime, de la date et de la catégorie de source ;
3. la France a durci les prêts étrangers à compter de 2018 et préservé les contrats antérieurs ;
4. un intermédiaire étranger ne suffit pas à identifier le principal économique ;
5. une violation financière, une anonymisation ou une sanction ne suffisent pas à établir commandement ou corruption ;
6. le financement ne ferme pas, sans preuve supplémentaire, les arêtes persuasion et résultat électoral.

Le delta à transmettre à INV-095 est donc précis : **les flux financiers peuvent créer capacité, dépendance ou accès potentiel, mais la sélection/cooptation d'un candidat doit être établie par des arêtes supplémentaires — bénéficiaire réel, contrepartie, tasking, accès, veto ou choix organisationnel — et non déduite de l'origine étrangère du financement.**

<!-- TRACE: terminal_delta=foreign_finance_real+legal_regimes_non_isomorphic+intermediary_not_principal+illegality_not_command+causal_ceiling; route=INV-095 -->
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:6|SRC_COMPLETE:14/14

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-07
- **material_breaks:**
  - France 2017 reform effective 2018 tightens foreign loans and donor eligibility
  - 2014 RN loan is grandfathered legacy contract
  - 2017 AfD transfers adjudicated through 2023
- **period:** 2012-2026

### MANIPULATION_REPORT
- **assumptions:**
  - legal texts establish formal source rules, not hidden beneficial ownership in every transaction
  - parliamentary/regulatory reports establish bounded institutional findings, not political motive beyond their evidence
  - court sanctions establish case-specific legal violations, not foreign-state tasking unless adjudicated
  - negative controls are retained
- **clusters:**
  - **loaded:**
    - clusters/MONEY.md
    - clusters/POWER.md
    - clusters/NETWORK.md
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - foreign origin does not automatically establish illegality across jurisdictions
  - foreign funding does not establish command
  - intermediary transfer does not identify the principal
  - illegality does not establish quid-pro-quo
  - sanction does not establish changed election result
  - strategic relevance does not establish received benefit
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - foreign-bank loan
  - foreign legal-person transfer
  - third-country donation
  - intermediary corporate account
  - anonymous economic donor
  - returned impermissible donation
  - externally funded polling
- **priorities:**
  - source category and legal regime
  - France pre/post-2018 change
  - legacy RN foreign-bank loan
  - beneficial/economic donor attribution
  - quid-pro-quo threshold
  - negative controls
  - electoral causal ceiling
- **query_guidance:** trace principal/source -> vehicle -> transfer/benefit -> party/candidate -> rule/control -> institutional consequence -> quid-pro-quo/tasking -> persuasion/result; preserve each edge
- **rhetorical:**
  - **AUTH:** official law/regulatory/court findings establish their bounded legal findings, not broader motive or electoral effect
  - **BF:** N/A
  - **DEM:** foreign-source rules and adjudicated cases are separated from allegations of control
  - **FAC:** avoid foreign-to-interference, intermediary-to-principal, illegality-to-command and sanction-to-result fallacies
  - **NUM:** amounts establish material financial flows and sanctions, not motive or counterfactual electoral effect
- **speaker:**
  - **goal:** forensic classification of foreign-origin financing of European parties/candidates
  - **target:** principal-vehicle-transfer-recipient-rule-control-command-effect chain
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
  - **ρ:** 5
  - **€:** 5
  - **↕:** 5
  - **⏰:** 4
  - **⚔:** 3
  - **⫸:** 4
  - **🌐:** 5
- **threats:**
  - foreign=illegal
  - foreign funding=interference
  - intermediary=principal
  - illegal donation=command
  - sanction=result_changed
  - strategic relevance=benefit_received

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - beneficial principal and quid-pro-quo in selected cases
  - **input_ids:**
    - FCT-001
    - FCT-002
    - FCT-005
    - FCT-006
    - FCT-008
    - FCT-011
    - FCT-019
    - FCT-020
    - FCT-021
    - FCT-022
  - **module:** clusters/MONEY.md
  - **negative_results:**
    - foreign origin is not uniformly illegal across regimes
  - **not_computable:**
    - hidden beneficial ownership without investigative records
  - **operations_applied:**
    - typed loan/donation/material-benefit source rules
    - separated foreign origin from illegality and command
  - **reason:** trace foreign-origin financial flows, source categories and legal vehicles
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-003
    - CTRL-001
    - CTRL-002
  - **status:** DONE
  - **trigger:** €
- **item 2:**
  - **gaps:**
    - political tasking, persuasion and counterfactual result
  - **input_ids:**
    - FCT-010
    - FCT-015
    - FCT-016
    - FCT-017
    - FCT-018
    - FCT-027
    - FCT-028
  - **module:** clusters/POWER.md
  - **negative_results:**
    - financing or sanction does not establish command or changed result
  - **not_computable:**
    - informal command without records
    - electoral causal effect without design
  - **operations_applied:**
    - bounded regulator and court findings
    - tested quid-pro-quo/tasking inference
  - **reason:** separate financing capacity, legal sanction and actual political command
  - **result_ids:**
    - CLM-005
    - CLM-006
    - CTRL-004
    - CTRL-005
    - CTRL-006
  - **status:** DONE
  - **trigger:** ↕
- **item 3:**
  - **gaps:**
    - complete principal chain in opaque transfers
  - **input_ids:**
    - FCT-011
    - FCT-012
    - FCT-013
    - FCT-014
    - FCT-027
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - Swiss transfer companies were not established as economic donor; UKIP benefit not established
  - **not_computable:**
    - unknown principal beyond adjudicated record
  - **operations_applied:**
    - separated transfer vehicle from economic donor
    - separated personnel overlap from received benefit
  - **reason:** map intermediary and economic-donor edges
  - **result_ids:**
    - CLM-004
    - CTRL-003
    - CTRL-006
  - **status:** DONE
  - **trigger:** 🌐

### SCOPING_REPORT
- **exclusions:**
  - generic NGO/media foreign funding outside party/candidate edge (INV-140)
  - domestic campaign-finance mechanics already closed by INV-093
- **guards:**
  - foreign funding != interference
  - funding != command
  - loan != donation
  - intermediary != concealed principal
  - illegality != electoral effect
  - sanction != result changed
- **object_question:** When and how do foreign-origin funds or advantages reach parties/candidates, and what evidence distinguishes legal/illegal funding, circumvention, command and electoral effect?
- **scope:** France/Europe 2012-2026 with France central and Germany/Spain/EU/UK as legal/case controls
- **subject:** Foreign direct or indirect financing of European parties/candidates

### CREDO
- foreign funding != interference
- foreign != illegal per se
- loan != donation
- intermediary != concealed principal
- illegal donation != quid_pro_quo
- funding != political_command
- sanction != result_changed
- strategic relevance != received benefit

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - foreign bank loan
  - foreign legal-person funding
  - third-country donation
  - intermediary company
  - anonymous economic donor
  - returned impermissible donation
  - third-party polling
- **priorities:**
  - legal source categories
  - France pre/post-2018 rule change
  - legacy RN loan
  - intermediary/economic-donor attribution
  - quid-pro-quo threshold
  - negative controls
  - causal ceiling
- **query_guidance:** trace principal/source -> legal vehicle -> transfer/benefit -> recipient -> governing rule -> regulator/court finding -> tasking/quid-pro-quo -> electoral effect; preserve each edge
- **speaker:**
  - **goal:** forensic classification of foreign-origin political financing
  - **target:** principal -> vehicle -> transfer/benefit -> party/candidate -> rule/control -> consequence -> command/effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **threats:**
  - foreign=illegal
  - foreign funding=interference
  - intermediary=principal
  - illegality=command
  - sanction=effect
  - strategic relevance=benefit

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** European regimes classify foreign states, firms, natural persons and qualifying banks differently; CNCCFP did not label the RN loan interference.
  - **resolution:** Foreign origin is a trigger for qualification, not a sufficient interference verdict.
  - **thesis:** Any foreign funding of a party is foreign interference.
- **item 2:**
  - **antithesis:** The AfD case shows transfer companies can differ from the economic donor.
  - **resolution:** Prove the beneficial/economic principal separately from the payment vehicle.
  - **thesis:** A foreign intermediary proves the foreign principal.
- **item 3:**
  - **antithesis:** German official guidance requires a recognizable specific quid-pro-quo; temporal proximity alone is insufficient.
  - **resolution:** Illegality/anonymity and command/corruption are distinct findings.
  - **thesis:** An impermissible donation proves corrupt political command.
- **item 4:**
  - **antithesis:** UKIP control had relevant polling and personnel overlap but insufficient evidence of purpose or receipt.
  - **resolution:** Potential benefit requires evidence of transfer/receipt and legal definition.
  - **thesis:** Potential strategic benefit means an in-kind donation was received.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **amount:** >EUR 9.1m
  - **flow:** FCRB -> FN/RN
  - **period:** 2014
  - **status:** VERIFIED_OFFICIAL_REPORT
  - **support:**
    - FCT-008
  - **type:** loan
- **item 2:**
  - **amount:** ~EUR 132k
  - **flow:** two Swiss company accounts -> AfD Bodensee
  - **period:** 2017
  - **status:** VERIFIED; ECONOMIC DONOR UNIDENTIFIED IN FINAL COURT SUMMARY
  - **support:**
    - FCT-011
    - FCT-013
  - **type:** 17 transfers labelled campaign donation
- **item 3:**
  - **flow:** ADDE/IDDE -> polling contractor
  - **period:** 2015-2016
  - **status:** PAYMENT VERIFIED; DONATION/BENEFIT TO UKIP NOT ESTABLISHED
  - **support:**
    - FCT-027
    - FCT-028
  - **type:** polling funded by European political structures

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** foreign State/legal person/natural person/bank
  - **limits:**
    - foreign source != command
  - **relation:** funds/loan/donation/material advantage
  - **support:**
    - FCT-002
    - FCT-006
    - FCT-008
    - FCT-019
    - FCT-020
    - FCT-021
  - **to:** party/candidate or intermediary
- **item 2:**
  - **from:** intermediary company/account
  - **limits:**
    - intermediary != economic principal
  - **relation:** transfers with declared campaign purpose
  - **support:**
    - FCT-011
    - FCT-013
    - FCT-014
  - **to:** party account
- **item 3:**
  - **from:** regulator/court
  - **limits:**
    - sanction != electoral effect
  - **relation:** qualification/return/sanction
  - **support:**
    - FCT-010
    - FCT-015
    - FCT-018
    - FCT-026
    - FCT-027
  - **to:** party financing transaction

### IMPACT_MAP
- **electoral_effect:** NOT_ESTABLISHED_COUNTERFACTUALLY
- **institutional_effects:**
  - French legal reform restricting foreign loans
  - legacy debt treatment
  - German triple-amount sanction
  - return/recovery duties in EU/UK regimes
- **political_command:** NOT_ESTABLISHED_GENERALLY
- **support:**
  - FCT-006
  - FCT-007
  - FCT-015
  - FCT-018
  - FCT-023
  - FCT-026
- **voter_persuasion:** NOT_ESTABLISHED

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** Spain permits certain foreign-natural-person donations and EU/France distinguish categories
  - **issue:** foreign origin versus illegality
  - **pro:** multiple regimes restrict foreign sources
  - **resolution:** FOREIGN_ORIGIN_REQUIRES_REGIME_SPECIFIC_QUALIFICATION
- **item 2:**
  - **contra:** CNCCFP did not establish interference or counterparty
  - **issue:** foreign financing versus interference
  - **pro:** RN loan had Russian bank origin
  - **resolution:** FINANCING_VERIFIED_INTERFERENCE_NOT_AUTOMATIC
- **item 3:**
  - **contra:** OVG found economic donor not attributable to those companies
  - **issue:** intermediary versus principal
  - **pro:** AfD transfers arrived from Swiss companies
  - **resolution:** TRANSFER_VEHICLE_VERIFIED_PRINCIPAL_SEPARATE
- **item 4:**
  - **contra:** UK regulator found insufficient evidence of purpose/receipt/benefit
  - **issue:** proximity/benefit versus donation
  - **pro:** UKIP-relevant polling and personnel overlap existed
  - **resolution:** RELEVANCE_AND_OVERLAP_NOT_DONATION_PROOF
- **item 5:**
  - **contra:** no causal electoral-result design
  - **issue:** sanction versus electoral result
  - **pro:** German donation breach produced large sanction
  - **resolution:** INSTITUTIONAL_CONSEQUENCE_VERIFIED_ELECTORAL_EFFECT_NOT_ESTABLISHED

### VERIFICATION_REPORT
- **fact_count:** 28
- **facts_tier:** 28 VERIFIE (✧)
- **negative_controls:**
  - CNCCFP RN loan non-interference finding boundary
  - Spain foreign-natural-person legal donations
  - UKIP ADDE/IDDE no-donation conclusion
  - Brexit risk/return not foreign-interference finding
- **provenance_families:** 7
- **query_count:** 14
- **result:** READY_FOR_PRE_GATE
- **source_count:** 14

### EDI_REPORT
- **corpus:**
  - **circularity:** LOW_TO_MODERATE
  - **coverage:** STRONG_LEGAL_RULES_AND_CASE_CONTROLS
  - **independence:** HIGH_ACROSS_7_PROVENANCE_FAMILIES
  - **limits:**
    - French Senate summarizes CNCCFP testimony for RN loan
    - Bundestag report and Berlin courts overlap on AfD facts but have distinct institutional roles
    - no causal electoral-effect dataset
    - not a prevalence census of all foreign finance
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES_WITH_BOUNDARIES
    - **gap_type:** SCOPE
    - **independent_families:** 4
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES_WITH_BOUNDARIES
    - **gap_type:** QUALIFICATION
    - **independent_families:** 2
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** YES_WITH_BOUNDARIES
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 2
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** YES_WITH_BOUNDARIES
    - **gap_type:** ATTRIBUTION
    - **independent_families:** 2
  - **item 5:**
    - **claim_id:** CLM-005
    - **direct_object:** YES_WITH_BOUNDARIES
    - **gap_type:** QUALIFICATION
    - **independent_families:** 3
  - **item 6:**
    - **claim_id:** CLM-006
    - **direct_object:** YES_WITH_BOUNDARIES
    - **gap_type:** CAUSALITY
    - **independent_families:** 3
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** 7_PROVENANCE_FAMILIES
  - **perspective:** FR_LAW+FR_SENATE_CNCCFP+DE_BUNDESTAG+DE_COURTS+ES_BOE+EU_LAW+UK_REGULATOR
  - **stratification:** RULES+LEGACY_CASE+INTERMEDIARY_ATTRIBUTION+SANCTIONS+NEGATIVE_CONTROLS
  - **temporal:** 2012-2026
- **edi:**
  - **assessment:** STRONG_RULE_AND_CASE_COVERAGE_WITH_COMMAND_AND_CAUSAL_GAPS
  - **flags:**
    - PRIMARY_OFFICIAL_SOURCES_DOMINANT
    - NEGATIVE_CONTROLS_PRESENT
    - NON_ISOMORPHIC_LEGAL_REGIMES
    - NO_GENERAL_COMMAND_PROOF
    - NO_ELECTORAL_COUNTERFACTUAL_EFFECT
- **source_counts:**
  - **claim_source:** 0
  - **primary:** 14
  - **provenance_families:** 7
  - **secondary:** 0
  - **total:** 14

### RESPONSIBILITY_MAP
- **boundary:** source/vehicle/illegality can be established without command/effect
- **not_established:**
  - foreign-State tasking in AfD case
  - quid-pro-quo attached to RN loan
  - general political command from foreign funding
  - voter persuasion
  - counterfactual electoral result
- **verified:**
  - France/Germany/Spain/EU/UK legal source rules
  - RN loan source vehicle and later creditor chain
  - AfD party-account receipt and unidentified economic donor finding
  - regulatory/court consequences

### NEXT_QUERIES
- **item 1:**
  - **need:** candidate-selection consequences only if financing source can be linked to tasking/access/selection
  - **route:** INV-095
- **item 2:**
  - **need:** causal designs on exposure/persuasion/result; do not infer from finance
  - **route:** INV-102
- **item 3:**
  - **condition:** new primary beneficial-owner, contract/counterparty, prosecutor/court, or causal electoral evidence
  - **reopen:** INV-094

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-005,QRY-006,QRY-008,QRY-012 | support:FCT-010,FCT-016,FCT-017,FCT-027,FCT-028 | counter:- | results:FCT-010,FCT-016,FCT-017,FCT-027,FCT-028 | final:GAP | gap:RESPONSIBILITY
LED-002 | attempts:QRY-005,QRY-006,QRY-008,QRY-012,QRY-013 | support:FCT-008,FCT-015,FCT-025,FCT-027 | counter:- | results:FCT-008,FCT-015,FCT-025,FCT-027 | final:GAP | gap:CAUSALITY
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-010,QRY-011,QRY-014 | support:FCT-002,FCT-003,FCT-005,FCT-006,FCT-019,FCT-020,FCT-021,FCT-022,FCT-024 | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-019,FCT-020,FCT-021,FCT-022,FCT-024 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005 | support:FCT-001,FCT-004,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010 | counter:- | results:FCT-001,FCT-004,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-006,QRY-007,QRY-008,QRY-009 | support:FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-018 | counter:- | results:FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-018 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-005,QRY-006,QRY-008,QRY-012 | support:FCT-010,FCT-016,FCT-017,FCT-027,FCT-028 | counter:- | results:FCT-010,FCT-016,FCT-017,FCT-027,FCT-028 | final:GAP | gap:RESPONSIBILITY
AXS-005 | attempts:QRY-012,QRY-013,QRY-014 | support:FCT-024,FCT-025,FCT-026,FCT-027,FCT-028 | counter:- | results:FCT-024,FCT-025,FCT-026,FCT-027,FCT-028 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-005,QRY-006,QRY-008,QRY-012,QRY-013 | support:FCT-008,FCT-015,FCT-025,FCT-027 | counter:- | results:FCT-008,FCT-015,FCT-025,FCT-027 | final:GAP | gap:CAUSALITY
CLM-001 | attempts:QRY-002,QRY-004,QRY-010,QRY-011,QRY-014,SRC-002,SRC-004,SRC-010,SRC-011,SRC-014 | support:FCT-002,FCT-003,FCT-005,FCT-006,FCT-019,FCT-020,FCT-021,FCT-022,FCT-024 | counter:CTRL-001 | results:FCT-002,FCT-003,FCT-005,FCT-006,FCT-019,FCT-020,FCT-021,FCT-022,FCT-024,CTRL-001 | final:SUPPORTED | gap:SCOPE
CLM-002 | attempts:QRY-001,QRY-003,QRY-004,QRY-005,SRC-001,SRC-003,SRC-004,SRC-005 | support:FCT-001,FCT-004,FCT-006,FCT-007,FCT-008,FCT-009 | counter:CTRL-002 | results:FCT-001,FCT-004,FCT-006,FCT-007,FCT-008,FCT-009,CTRL-002 | final:SUPPORTED | gap:QUALIFICATION
CLM-003 | attempts:QRY-005,SRC-005 | support:FCT-008,FCT-009,FCT-010 | counter:CTRL-002;CTRL-005 | results:FCT-008,FCT-009,FCT-010,CTRL-002;CTRL-005 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-004 | attempts:QRY-006,QRY-007,QRY-008,QRY-009,SRC-006,SRC-007,SRC-008,SRC-009 | support:FCT-011,FCT-012,FCT-013,FCT-014,FCT-015 | counter:CTRL-003 | results:FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,CTRL-003 | final:SUPPORTED | gap:ATTRIBUTION
CLM-005 | attempts:QRY-006,QRY-008,QRY-009,SRC-006,SRC-008,SRC-009 | support:FCT-015,FCT-016,FCT-017,FCT-018 | counter:CTRL-004;CTRL-005 | results:FCT-015,FCT-016,FCT-017,FCT-018,CTRL-004;CTRL-005 | final:SUPPORTED | gap:QUALIFICATION
CLM-006 | attempts:QRY-005,QRY-006,QRY-012,QRY-013,SRC-005,SRC-006,SRC-012,SRC-013 | support:FCT-010,FCT-017,FCT-025,FCT-026,FCT-027,FCT-028 | counter:CTRL-006 | results:FCT-010,FCT-017,FCT-025,FCT-026,FCT-027,FCT-028,CTRL-006 | final:SUPPORTED | gap:CAUSALITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
AXS-004 | AXS | GAP | RESPONSIBILITY | No general command/tasking inference is supported; CNCCFP and Bundestag controls explicitly preserve a higher evidentiary threshold.
AXS-006 | AXS | GAP | CAUSALITY | No examined source provides a causal design identifying persuasion or a changed electoral result attributable to the foreign-origin financing.
CLM-001 | CLM | SUPPORTED | SCOPE | Cross-country rules are not isomorphic and do not by themselves establish prevalence of circumvention.
CLM-002 | CLM | SUPPORTED | QUALIFICATION | Legality under the old framework does not establish absence or presence of political consideration.
CLM-003 | CLM | SUPPORTED | RESPONSIBILITY | Tasking, quid-pro-quo and electoral effect are not established by the loan record examined.
CLM-004 | CLM | SUPPORTED | ATTRIBUTION | The final judicial finding was unidentified donor/impermissible party donation, not foreign-state tasking.
CLM-005 | CLM | SUPPORTED | QUALIFICATION | A financing-law breach may exist without proving political command or corrupt exchange.
CLM-006 | CLM | SUPPORTED | CAUSALITY | No matched exposure/persuasion/counterfactual design is present in the examined corpus.
CAU-001 | CAU | UNRESOLVED | CAUSALITY | Tasking/quid-pro-quo, persuasion and counterfactual result remain open even where source/vehicle/transfer/control are verified.

SEMANTIC_COUNTS_V1:LED:2|CLM:6|AXS:6|CAU:1|CTRL:6|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-005","QRY-006","QRY-008","QRY-012"],"evidence_excerpt":"Foreign-origin financing and disguised-source cases are documentable, but official French and German controls do not permit financing alone to close a tasking/quid-pro-quo edge.","gap":"No cross-case evidence establishes that foreign origin alone proves command, consideration or policy tasking.","gap_type":"RESPONSIBILITY","kind":"EVIDENCE_GAP","lead":"Foreign funding to political command or quid-pro-quo","linked_ids":["CLM-005","CAU-001","CTRL-005"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-010","FCT-016","FCT-017","FCT-027","FCT-028"],"route":"INV-095","routes":["INV-095"],"source_id":"INV-094_RUN_CARD","status":"GAP","support":["FCT-010","FCT-016","FCT-017","FCT-027","FCT-028"]}
LED-002 | {"attempt_ids":["QRY-005","QRY-006","QRY-008","QRY-012","QRY-013"],"evidence_excerpt":"The corpus establishes money routes, legal qualification and sanctions, but none of the examined authorities quantifies persuasion or a changed election result caused by the financing.","gap":"Voter persuasion and counterfactual electoral result remain unestablished.","gap_type":"CAUSALITY","kind":"CAUSAL_GAP","lead":"Foreign financing to persuasion or electoral-result counterfactual","linked_ids":["CLM-006","CAU-001","CTRL-006"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-008","FCT-015","FCT-025","FCT-027"],"route":"INV-095/INV-102","routes":["INV-095","INV-102"],"source_id":"INV-094_RUN_CARD","status":"GAP","support":["FCT-008","FCT-015","FCT-025","FCT-027"]}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"European political-finance regimes distinguish foreign-source categories rather than treating all foreign money as uniformly illegal: rules differ for states, legal persons, natural persons, banks and electoral eligibility.","claimant":"INV-094 synthesis","counter":"CTRL-001","gap":"Cross-country rules are not isomorphic and do not by themselves establish prevalence of circumvention.","gap_type":"SCOPE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-002","FCT-003","FCT-005","FCT-006","FCT-019","FCT-020","FCT-021","FCT-022","FCT-024"]}
CLM-002 | {"claim":"France materially tightened foreign-loan rules from 2018 while grandfathering prior contracts, making the 2014 RN/FCRB loan a legacy-law case rather than proof of a post-2018 legal permission.","claimant":"INV-094 synthesis","counter":"CTRL-002","gap":"Legality under the old framework does not establish absence or presence of political consideration.","gap_type":"QUALIFICATION","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-004","FCT-006","FCT-007","FCT-008","FCT-009"]}
CLM-003 | {"claim":"The RN/FCRB loan establishes a substantial foreign-origin party loan and later Russian creditor chain, but CNCCFP did not establish that it constituted interference or carried a counterparty.","claimant":"INV-094 synthesis","counter":"CTRL-002;CTRL-005","gap":"Tasking, quid-pro-quo and electoral effect are not established by the loan record examined.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-008","FCT-009","FCT-010"]}
CLM-004 | {"claim":"The AfD Bodensee case demonstrates that an intermediary corporate transfer route can conceal or fail to establish the economic donor and can trigger major party-finance sanctions without proving a foreign state principal.","claimant":"INV-094 synthesis","counter":"CTRL-003","gap":"The final judicial finding was unidentified donor/impermissible party donation, not foreign-state tasking.","gap_type":"ATTRIBUTION","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-011","FCT-012","FCT-013","FCT-014","FCT-015"]}
CLM-005 | {"claim":"Foreign financing, anonymity, impermissibility and influence/quid-pro-quo are separate legal and evidentiary categories; official German guidance requires a recognizable specific exchange for an influence donation, and temporal proximity alone is insufficient.","claimant":"INV-094 synthesis","counter":"CTRL-004;CTRL-005","gap":"A financing-law breach may exist without proving political command or corrupt exchange.","gap_type":"QUALIFICATION","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-015","FCT-016","FCT-017","FCT-018"]}
CLM-006 | {"claim":"The examined controls do not establish that foreign-origin financing by itself caused voter persuasion or changed an election result; proximity, possible benefit, fundraising risk or sanction are insufficient to close that causal chain.","claimant":"INV-094 synthesis","counter":"CTRL-006","gap":"No matched exposure/persuasion/counterfactual design is present in the examined corpus.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-010","FCT-017","FCT-025","FCT-026","FCT-027","FCT-028"]}

### AXIS_REGISTRY_V1
AXS-001 | {"assessment":"VERIFIED_NON_ISOMORPHIC","attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-010","QRY-011","QRY-014"],"axis":"legal_foreign_source_categories","links":["CLM-001","CLM-002"],"question":"How do European regimes classify foreign states, foreign legal persons, foreign natural persons and financial institutions?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-019","FCT-020","FCT-021","FCT-022","FCT-024"],"sought_objects":["FOREIGN_STATE","FOREIGN_LEGAL_PERSON","FOREIGN_NATURAL_PERSON","EU_EEA_BANK","THIRD_COUNTRY_ENTITY"],"status":"SATURATED","support":["FCT-002","FCT-003","FCT-005","FCT-006","FCT-019","FCT-020","FCT-021","FCT-022","FCT-024"]}
AXS-002 | {"assessment":"VERIFIED","attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005"],"axis":"france_legacy_and_reform","links":["CLM-002","CLM-003","CTRL-002"],"question":"Did French law change in a way material to the 2014 RN foreign-bank loan?","result_ids":["FCT-001","FCT-004","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010"],"sought_objects":["PRE_2018_RULE","POST_2018_RULE","GRANDFATHERED_LOAN","FOREIGN_BANK_LOAN"],"status":"SATURATED","support":["FCT-001","FCT-004","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010"]}
AXS-003 | {"assessment":"VERIFIED_CASE_SPECIFIC","attempt_ids":["QRY-006","QRY-007","QRY-008","QRY-009"],"axis":"intermediary_and_beneficial_source","links":["CLM-004","CLM-005"],"question":"Can foreign corporate routes or intermediaries obscure the economic donor, and what is actually established in adjudicated cases?","result_ids":["FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-018"],"sought_objects":["INTERMEDIARY","ECONOMIC_DONOR","ANONYMOUS_DONOR","PARTY_ACCOUNT","SANCTION"],"status":"SATURATED","support":["FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-018"]}
AXS-004 | {"assessment":"NOT_ESTABLISHED_BEYOND_CASE_SPECIFIC_LEGAL_BREACH","attempt_ids":["QRY-005","QRY-006","QRY-008","QRY-012"],"axis":"illegality_vs_command","gap":"No general command/tasking inference is supported; CNCCFP and Bundestag controls explicitly preserve a higher evidentiary threshold.","gap_type":"RESPONSIBILITY","links":["CLM-003","CLM-005","LED-001"],"question":"Does an unlawful or foreign-origin donation establish political command, quid-pro-quo or corrupt influence?","result_ids":["FCT-010","FCT-016","FCT-017","FCT-027","FCT-028"],"sought_objects":["ILLEGALITY","QUID_PRO_QUO","TASKING","POLITICAL_COMMAND","FOREIGN_PRINCIPAL"],"status":"GAP","support":["FCT-010","FCT-016","FCT-017","FCT-027","FCT-028"]}
AXS-005 | {"assessment":"VERIFIED_NEGATIVE_CONTROLS","attempt_ids":["QRY-012","QRY-013","QRY-014"],"axis":"negative_controls_and_risk","links":["CLM-005","CLM-006","CTRL-006"],"question":"Do strategic relevance, overlapping personnel, or compliance risk suffice to prove receipt of impermissible foreign support?","result_ids":["FCT-024","FCT-025","FCT-026","FCT-027","FCT-028"],"sought_objects":["POSSIBLE_BENEFIT","OVERLAP","COMPLIANCE_RISK","ACTUAL_DONATION"],"status":"SATURATED","support":["FCT-024","FCT-025","FCT-026","FCT-027","FCT-028"]}
AXS-006 | {"assessment":"NOT_ESTABLISHED","attempt_ids":["QRY-005","QRY-006","QRY-008","QRY-012","QRY-013"],"axis":"electoral_effect","gap":"No examined source provides a causal design identifying persuasion or a changed electoral result attributable to the foreign-origin financing.","gap_type":"CAUSALITY","links":["CLM-006","CAU-001","LED-002"],"question":"Does the financing evidence establish persuasion or a counterfactual election-result change?","result_ids":["FCT-008","FCT-015","FCT-025","FCT-027"],"sought_objects":["EXPOSURE","PERSUASION","VOTER_BEHAVIOR","COUNTERFACTUAL_RESULT"],"status":"GAP","support":["FCT-008","FCT-015","FCT-025","FCT-027"]}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"Spain allows some foreign-natural-person donations; French legacy loan was lawful under prior rules; German anonymous-donor sanctions do not establish a foreign-state principal; UKIP negative control breaks proximity/benefit inference.","from":"foreign principal / foreign-origin funds","gap":"Tasking/quid-pro-quo, persuasion and counterfactual result remain open even where source/vehicle/transfer/control are verified.","gap_type":"CAUSALITY","limit":"I0-I4 supported strongly case-specifically for source category, vehicle, transfer, legal rule and institutional consequence; I5 political command is only case-specific/not established generally; I6 persuasion and I7 counterfactual result are not established.","limits":["foreign funding != interference","funding != command","intermediary != concealed principal","illegality != electoral effect","sanction != result changed"],"mechanism":"foreign principal -> bank/company/person/intermediary -> party/candidate account or material benefit -> legal classification/control -> return/sanction/legacy debt -> possible political command -> exposure/persuasion -> electoral result","status":"UNRESOLVED","support":["FCT-002","FCT-006","FCT-008","FCT-010","FCT-013","FCT-015","FCT-016","FCT-017","FCT-027"],"to":"party/candidate financing -> institutional/electoral effect"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Legal-regime control: Spain permits certain donations from foreign natural persons while barring foreign public financing; France and EU rules draw different category boundaries. Foreign origin is therefore not uniformly synonymous with illegality.","status":"DONE","support":["FCT-002","FCT-005","FCT-019","FCT-020","FCT-021","FCT-022"]}
CTRL-002 | {"control":"Legacy-law control: France explicitly grandfathered contracts predating the 2018 foreign-loan restriction; the RN 2014 loan must be assessed under the rule then in force.","status":"DONE","support":["FCT-001","FCT-004","FCT-007","FCT-008","FCT-009"]}
CTRL-003 | {"control":"Attribution control: in the AfD Bodensee case the Swiss corporate transfer route did not establish those companies as the economic donor, and the court finding remained an unidentified donor/impermissible party donation rather than a foreign-state principal.","status":"DONE","support":["FCT-011","FCT-012","FCT-013","FCT-014","FCT-015"]}
CTRL-004 | {"control":"Quid-pro-quo control: German official guidance requires a recognizable specific exchange for an influence donation; temporal proximity to a favorable act alone is insufficient.","status":"DONE","support":["FCT-016","FCT-017"]}
CTRL-005 | {"control":"French interference-label control: CNCCFP expressly declined to classify the RN Russian-bank loan as interference on its evidentiary record and said it lacked means to know whether counterparties existed.","status":"DONE","support":["FCT-010"]}
CTRL-006 | {"control":"Benefit/risk control: the UKIP investigation found strategic relevance and overlapping personnel but insufficient evidence of benefit/receipt; the Brexit Party review found compliance risk and one returned unresolved-source donation, not proven foreign interference.","status":"DONE","support":["FCT-025","FCT-026","FCT-027","FCT-028"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:14|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | MNEMO_UNAVAILABLE degraded; exact snapshot search unavailable in this environment | MnemoLite | NONE | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | PASS | SRC-001 | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000023883022/2015-03-21 | FETCH exact French electoral code L52-8 pre-2018 foreign contributions
QRY-002 | FETCH | PASS | SRC-002 | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000039446180/2021-06-10 | FETCH exact French electoral code L52-8 current foreign contributions and loans
QRY-003 | FETCH | PASS | SRC-003 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000034152918/2017-03-08 | FETCH exact French political-party finance Article 11-4 pre-2018
QRY-004 | FETCH | PASS | SRC-004 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000035588686/2026-08-11 | FETCH exact French political-party finance Article 11-4 current
QRY-005 | FETCH | PASS | SRC-005 | https://www.senat.fr/rap/r23-739-1/r23-739-113.html | FETCH exact Senate 2024 report RN Russian bank loan and CNCCFP evidence limit
QRY-006 | FETCH | PASS | SRC-006 | https://dserver.bundestag.de/btd/19/305/1930520.pdf | FETCH exact Bundestag party-finance report 2015-2019 AfD Swiss transfers and influence-donation standard
QRY-007 | FETCH | PASS | SRC-007 | https://www.berlin.de/gerichte/verwaltungsgericht/presse/pressemitteilungen/2021/pressemitteilung.1096347.php | FETCH exact Berlin Verwaltungsgericht 2021 AfD donation judgment summary
QRY-008 | FETCH | PASS | SRC-008 | https://www.berlin.de/gerichte/oberverwaltungsgericht/presse/pressemitteilungen/2023/pressemitteilung.1300934.php | FETCH exact OVG Berlin-Brandenburg 2023 AfD donation sanction judgment
QRY-009 | FETCH | PASS | SRC-009 | https://www.gesetze-im-internet.de/partg/__31c.html | FETCH exact German Parties Act section 31c sanctions
QRY-010 | FETCH | PASS | SRC-010 | https://boe.es/buscar/act.php?id=BOE-A-2007-13022 | FETCH exact Spain Organic Law 8/2007 Article 7 foreign contributions
QRY-011 | FETCH | PASS | SRC-011 | https://eur-lex.europa.eu/eli/reg/2014/1141/oj/eng | FETCH exact EU Regulation 1141/2014 Article 20 donations to European political parties
QRY-012 | FETCH | PASS | SRC-012 | https://www.electoralcommission.org.uk/political-registration-and-regulation/our-enforcement-work/investigations/investigation-uk-independence-party-ukip | FETCH exact UK Electoral Commission UKIP ADDE/IDDE investigation
QRY-013 | FETCH | PASS | SRC-013 | https://www.electoralcommission.org.uk/media-centre/political-parties-and-non-party-campaigners-accepting-payments-online-0 | FETCH exact UK Electoral Commission Brexit Party online payments review
QRY-014 | FETCH | PASS | SRC-014 | https://www.electoralcommission.org.uk/full-guidance/political-party-donations-and-loans-great-britain | FETCH exact UK Electoral Commission party donations and loans guidance

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | LEGIARTI000023883022 | Code électoral — article L52-8, version 2011-2018 | 2011-04-20 | 2026-09-07T19:46:00+02:00 | Article L52-8; version 20/04/2011-01/01/2018 | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000023883022/2015-03-21
SRC-002 | ◈ | fam:A | LEGIARTI000039446180 | Code électoral — article L52-8, current post-2017 rule | 2020-06-30 | 2026-09-07T19:46:00+02:00 | Article L52-8; foreign contributions/material assistance and loan exception | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000039446180/2021-06-10
SRC-003 | ◈ | fam:A | LEGIARTI000034152918 | Loi 88-227 — article 11-4, version 2017 pre-reform | 2017-03-08 | 2026-09-07T19:46:00+02:00 | Article 11-4; version 08/03/2017-01/01/2018 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000034152918/2017-03-08
SRC-004 | ◈ | fam:A | LEGIARTI000035588686 | Loi 88-227 — article 11-4, post-2017 reform | 2018-01-01 | 2026-09-07T19:46:00+02:00 | Article 11-4; current foreign-source and loan rules; transition clause | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000035588686/2026-08-11
SRC-005 | ◈ | fam:B | SENAT-R23-739-1-13 | Sénat — rapport sur les influences étrangères malveillantes, financement politique | 2024-07-10 | 2026-09-07T19:46:00+02:00 | Section financement politique; audition CNCCFP; encadré prêt RN/FCRB | https://www.senat.fr/rap/r23-739-1/r23-739-113.html
SRC-006 | ◈ | fam:C | BT-DRS-19-30520 | Deutscher Bundestag — Bericht Parteienfinanzen 2015-2019 | 2021-06-09 | 2026-09-07T19:46:00+02:00 | pp.41-43; AfD transfers; unidentified donor; Einflussspende standard | https://dserver.bundestag.de/btd/19/305/1930520.pdf
SRC-007 | ◈ | fam:D | VG-BERLIN-2K536-19 | VG Berlin — AfD verliert Parteispendenprozess | 2021-06-22 | 2026-09-07T19:46:00+02:00 | Press release 36/2021; 17 transfers about EUR132k | https://www.berlin.de/gerichte/verwaltungsgericht/presse/pressemitteilungen/2021/pressemitteilung.1096347.php
SRC-008 | ◈ | fam:D | OVG-3B28-21 | OVG Berlin-Brandenburg — AfD Sanktionszahlungen Parteispende | 2023-03-02 | 2026-09-07T19:46:00+02:00 | Judgment 2 Mar 2023; unidentified donor; party-vs-candidate donation; ~EUR396k | https://www.berlin.de/gerichte/oberverwaltungsgericht/presse/pressemitteilungen/2023/pressemitteilung.1300934.php
SRC-009 | ◈ | fam:C | PARTG-31C | Parteiengesetz — §31c unlawful or undisclosed donations | 2026-09-07 | 2026-09-07T19:46:00+02:00 | §31c triple/double amount sanctions | https://www.gesetze-im-internet.de/partg/__31c.html
SRC-010 | ◈ | fam:E | BOE-A-2007-13022-ART7 | España — Ley Orgánica 8/2007 financiación partidos, artículo 7 | 2015-04-01 | 2026-09-07T19:46:00+02:00 | Artículo 7; foreign natural persons allowed under conditions; foreign public funding prohibited | https://boe.es/buscar/act.php?id=BOE-A-2007-13022
SRC-011 | ◈ | fam:other:eu-law | CELEX-32014R1141-ART20 | Regulation (EU, Euratom) 1141/2014 — Article 20 | 2014-11-04 | 2026-09-07T19:46:00+02:00 | Article 20(5)-(6); prohibited third-country/public/anonymous donations; return/recovery | https://eur-lex.europa.eu/eli/reg/2014/1141/oj/eng
SRC-012 | ◈ | fam:other:uk-electoral-commission | EC-UKIP-ADDE-IDDE | UK Electoral Commission — Investigation UKIP/ADDE/IDDE | 2018-01-01 | 2026-09-07T19:46:00+02:00 | Investigation findings; evidence standard; polling not donation | https://www.electoralcommission.org.uk/political-registration-and-regulation/our-enforcement-work/investigations/investigation-uk-independence-party-ukip
SRC-013 | ◈ | fam:other:uk-electoral-commission | EC-BREXIT-PARTY-ONLINE | UK Electoral Commission — Brexit Party online payments review | 2019-05-21 | 2026-09-07T19:46:00+02:00 | Risk review; return of GBP1000 unresolved-source donation | https://www.electoralcommission.org.uk/media-centre/political-parties-and-non-party-campaigners-accepting-payments-online-0
SRC-014 | ◈ | fam:other:uk-electoral-commission | EC-PARTY-DONATIONS-LOANS-GB | UK Electoral Commission — Political party donations and loans guidance | 2023-11-21 | 2026-09-07T19:46:00+02:00 | Checks on true identity/permissible source and return of unidentified funds | https://www.electoralcommission.org.uk/full-guidance/political-party-donations-and-loans-great-britain

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000023883022/2015-03-21 | A | 2011-04-20 | Foreign contributions, pre-2018 candidate rule | The 2011-2018 version of French Code électoral L52-8 prohibited a candidate from receiving direct or indirect contributions or material assistance from a foreign State or foreign legal person; that version did not expressly add the later foreign-loan prohibition. | -
FCT-002 | FACT | ✧ | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000039446180/2021-06-10 | A | 2020-06-30 | Foreign contributions, current candidate rule | Current French L52-8 prohibits a candidate from receiving contributions or material assistance from a foreign State or foreign legal person and also prohibits loans from them except qualifying EU/EEA credit or finance institutions. | -
FCT-003 | FACT | ✧ | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000039446180/2021-06-10 | A | 2020-06-30 | EU/EEA credit-institution exception | French candidate-finance law permits loans from political parties and qualifying credit/finance institutions headquartered in the EU or EEA; other legal persons may not lend to or guarantee a candidate. | -
FCT-004 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000034152918/2017-03-08 | A | 2017-03-08 | Foreign assistance, pre-2018 party rule | The pre-2018 French party-finance Article 11-4 prohibited direct or indirect contributions or material assistance from a foreign State or foreign legal person, while not expressly stating the later foreign-loan rule. | -
FCT-005 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000035588686/2026-08-11 | A | 2018-01-01 | Post-2017 French party donor rule | Since 1 January 2018, a physical person may donate to a French party only if French or resident in France; legal-person lending is generally limited to parties and qualifying EU/EEA credit or finance institutions. | -
FCT-006 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000035588686/2026-08-11 | A | 2018-01-01 | Post-2017 foreign-loan prohibition for parties | Since 2018 French party finance agents may not receive foreign-State or foreign-legal-person contributions/material assistance and may not receive their loans except from the qualifying EU/EEA credit/finance institutions specified by law. | -
FCT-007 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000035588686/2026-08-11 | A | 2018-01-01 | French transition for pre-existing loans | The 2017 reform expressly states that the new foreign-loan restrictions do not apply to contracts concluded before the reform entered into force. | -
FCT-008 | FACT | ✧ | https://www.senat.fr/rap/r23-739-1/r23-739-113.html | B | 2014 | RN/FN Russian-bank loan | The French Senate reports that the Front national received in 2014 a loan of more than EUR 9.1 million from First Czech Russian Bank, a Russian bank; after the bank failed in 2016, the claim was taken over by Russian company Aviazapchast. | -
FCT-009 | FACT | ✧ | https://www.senat.fr/rap/r23-739-1/r23-739-113.html | B | 2019 | RN loan legacy treatment | The Senate reports that the 2014 loan was renegotiated in 2019 and, because it was contracted under the pre-2018 rules, the party could retain the debt on its balance sheet while repaying it. | -
FCT-010 | FACT | ✧ | https://www.senat.fr/rap/r23-739-1/r23-739-113.html | B | 2024 | CNCCFP non-attribution of interference | The president of CNCCFP told the Senate that CNCCFP had never taken a position allowing him to classify the RN Russian-bank loan positively as interference and that the commission had no means to know whether the loan carried counterparties. | -
FCT-011 | FACT | ✧ | https://dserver.bundestag.de/btd/19/305/1930520.pdf | C,D | 2017 | AfD Swiss-account transfers | The Bundestag report records 17 transfers totalling about EUR 132,000 from accounts of two Swiss pharmaceutical-trading companies to the AfD Bodensee account, marked for Alice Weidel social-media campaigning. | -
FCT-012 | FACT | ✧ | https://dserver.bundestag.de/btd/19/305/1930520.pdf | C | 2018 | AfD purported donor-list contradiction | The Bundestag report records that several purported donors later said they had not donated and that the AfD said it lacked reliable knowledge of the true donor; Swiss-assisted criminal investigation later identified a suspected German real-estate entrepreneur living in Switzerland. | -
FCT-013 | FACT | ✧ | https://www.berlin.de/gerichte/oberverwaltungsgericht/presse/pressemitteilungen/2023/pressemitteilung.1300934.php | D | 2023-03-02 | AfD economic-source finding | The OVG Berlin-Brandenburg held that the 2017 donation was economically not attributable to the two Swiss companies but to an unidentified donor. | -
FCT-014 | FACT | ✧ | https://www.berlin.de/gerichte/oberverwaltungsgericht/presse/pressemitteilungen/2023/pressemitteilung.1300934.php | D | 2023-03-02 | AfD party-versus-candidate classification | The OVG rejected the argument that the transfers were a direct personal candidate donation; the transfer to the party account supported classification as a party donation. | -
FCT-015 | FACT | ✧ | https://www.berlin.de/gerichte/oberverwaltungsgericht/presse/pressemitteilungen/2023/pressemitteilung.1300934.php | C,D | 2023-03-02 | AfD sanction amount | The Bundestag administration imposed about EUR 396,000 in sanctions, three times the donation amount, and the OVG confirmed the lower-court judgment. | -
FCT-016 | FACT | ✧ | https://dserver.bundestag.de/btd/19/305/1930520.pdf | C | 2021-06-09 | German quid-pro-quo proof standard | The Bundestag party-finance report explains that an impermissible influence donation requires an express or implicit but recognizable agreement linking the donation to a specific economic or political advantage. | -
FCT-017 | FACT | ✧ | https://dserver.bundestag.de/btd/19/305/1930520.pdf | C | 2021-06-09 | Temporal proximity insufficient in Germany | The Bundestag report states that temporal proximity between a donation and a favorable public act is insufficient by itself to establish an impermissible influence donation; the party-finance authority often depends on criminal investigative results because it lacks its own investigative powers. | -
FCT-018 | FACT | ✧ | https://www.gesetze-im-internet.de/partg/__31c.html | C | 2026-09-07 | German statutory sanction structure | German Parties Act §31c provides a claim for three times an unlawfully accepted donation not forwarded as required, and twice the amount for donations not properly published in the party report. | -
FCT-019 | FACT | ✧ | https://boe.es/buscar/act.php?id=BOE-A-2007-13022 | E | 2015-04-01 | Spain foreign natural-person donations | Spanish Organic Law 8/2007 Article 7 permits political parties to receive non-earmarked donations from foreign natural persons subject to the same private-donation limits and capital-control rules. | -
FCT-020 | FACT | ✧ | https://boe.es/buscar/act.php?id=BOE-A-2007-13022 | E | 2015-04-01 | Spain foreign-public-source prohibition | Spain prohibits parties from accepting any financing from foreign governments, public bodies/entities/public companies or companies directly or indirectly related to them. | -
FCT-021 | FACT | ✧ | https://eur-lex.europa.eu/eli/reg/2014/1141/oj/eng | other:eu-law | 2014-11-04 | EU European-party prohibited public donations | Regulation 1141/2014 bars European political parties/foundations from anonymous donations, EP political-group budget donations, and donations from public authorities in Member States or third countries or undertakings they dominate. | -
FCT-022 | FACT | ✧ | https://eur-lex.europa.eu/eli/reg/2014/1141/oj/eng | other:eu-law | 2014-11-04 | EU European-party third-country private-source prohibition | The same EU regulation bars donations from private entities based in a third country and from third-country individuals not entitled to vote in European Parliament elections. | -
FCT-023 | FACT | ✧ | https://eur-lex.europa.eu/eli/reg/2014/1141/oj/eng | other:eu-law | 2014-11-04 | EU impermissible-donation recovery | An impermissible donation under Regulation 1141/2014 must be returned within 30 days or, if return is impossible, reported for recovery through the European Parliament framework. | -
FCT-024 | FACT | ✧ | https://www.electoralcommission.org.uk/full-guidance/political-party-donations-and-loans-great-britain | other:uk-electoral-commission | 2023-11-21 | UK identity and permissibility checks | UK Electoral Commission guidance says parties accepting donations over GBP 500 must take reasonable steps to know the true donor identity and verify that the source is permissible; unidentified or impermissible donations should be returned. | -
FCT-025 | FACT | ✧ | https://www.electoralcommission.org.uk/media-centre/political-parties-and-non-party-campaigners-accepting-payments-online-0 | other:uk-electoral-commission | 2019-05-21 | Brexit Party fundraising risk finding | The UK Electoral Commission found the Brexit Party online fundraising structure created a high and ongoing risk of receiving and accepting impermissible donations; this was a risk/compliance finding, not a finding that foreign donations had been accepted. | -
FCT-026 | FACT | ✧ | https://www.electoralcommission.org.uk/media-centre/political-parties-and-non-party-campaigners-accepting-payments-online-0 | other:uk-electoral-commission | 2019-05-21 | Brexit Party returned unresolved-source donation | The Electoral Commission recorded that the Brexit Party returned one GBP 1,000 donation because it could not determine whether the source was permissible. | -
FCT-027 | FACT | ✧ | https://www.electoralcommission.org.uk/political-registration-and-regulation/our-enforcement-work/investigations/investigation-uk-independence-party-ukip | other:uk-electoral-commission | 2018 | UKIP ADDE/IDDE negative finding | After investigating whether UKIP received impermissible donations from ADDE/IDDE, the Electoral Commission concluded it did not; despite strategic relevance and overlapping personnel, evidence was insufficient to show polling was commissioned for UKIP or that UKIP received or benefited from it. | -
FCT-028 | FACT | ✧ | https://www.electoralcommission.org.uk/political-registration-and-regulation/our-enforcement-work/investigations/investigation-uk-independence-party-ukip | other:uk-electoral-commission | 2018 | UKIP offence proof threshold | The UK Electoral Commission explicitly noted that its conclusion differed from a European Parliament Bureau conclusion because its UK offence investigation required it to be satisfied beyond reasonable doubt that an offence had been committed. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-002
FCT-004 | SRC-003
FCT-005 | SRC-004
FCT-006 | SRC-004
FCT-007 | SRC-004
FCT-008 | SRC-005
FCT-009 | SRC-005
FCT-010 | SRC-005
FCT-011 | SRC-006,SRC-007
FCT-012 | SRC-006
FCT-013 | SRC-008
FCT-014 | SRC-008
FCT-015 | SRC-008,SRC-009
FCT-016 | SRC-006
FCT-017 | SRC-006
FCT-018 | SRC-009
FCT-019 | SRC-010
FCT-020 | SRC-010
FCT-021 | SRC-011
FCT-022 | SRC-011
FCT-023 | SRC-011
FCT-024 | SRC-014
FCT-025 | SRC-013
FCT-026 | SRC-013
FCT-027 | SRC-012
FCT-028 | SRC-012

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
ATTEMPT-001 | {"created_at":"2026-09-07T18:03:08.235248+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":28,"eligible":28,"failure":0,"success":0}}

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
