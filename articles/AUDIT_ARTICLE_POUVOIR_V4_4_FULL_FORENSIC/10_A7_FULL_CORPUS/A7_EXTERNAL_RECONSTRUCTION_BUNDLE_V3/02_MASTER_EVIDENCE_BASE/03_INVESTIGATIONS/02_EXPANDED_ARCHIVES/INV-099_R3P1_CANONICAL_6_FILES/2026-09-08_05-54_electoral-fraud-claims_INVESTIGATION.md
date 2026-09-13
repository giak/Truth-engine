ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260908-0554-electoral-fraud-claims | PARENT_RUN_ID:NONE | AS_OF:2026-09-08
INPUT_KIND:RUN_CARD | MISSION_MODE:GREENFIELD | INPUT_REF:PATH:/mnt/data/inv099-runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-08_electoral-fraud-claims/2026-09-08_05-54_electoral-fraud-claims_INPUT.md | SUBJECT_SLUG:electoral-fraud-claims | SUBJECT_FP:sha256:7e29b8326221a1306669179816ccfaa86ae458ba74dcdfb14da2ad9f163a661b | INPUT_SHA256:sha256:3d4b54ab89a07ef6da09a0e5c0bec86666ae72a57e0b36431e40a33e41331a96
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/Europe 2000-2026; distinguish established electoral fraud, non-intentional irregularity/error, unsupported allegation and documented institutional/electoral effect; prioritize France with mechanism-isomorphic European comparators.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/FRAMING.md,clusters/NETWORK.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-099 — Fraude électorale réelle versus accusation de fraude

## Résultat central

Le corpus ferme trois distinctions qui doivent rester séparées.

Premièrement, **la fraude électorale intentionnelle existe comme mécanisme réel et juridiquement défini en France**. Le code électoral pénalise plusieurs opérations précises : fausse inscription, usurpation d’identité ou de signature, vote multiple et altération de bulletins. Ces catégories ne sont pas des métaphores politiques ; elles désignent des actes matériellement testables. Le cas marseillais de 2020 fournit un contrôle positif particulièrement discriminant : le Conseil d’État a retenu des procurations préparées sans consentement ou hors présence des mandants et a explicitement qualifié l’ensemble de « manoeuvres frauduleuses » au profit d’une liste. Les éléments retenus portent sur 167 formulaires irrégulièrement préparés et un maximum estimé de 158 votes au premier tour et 116 au second (FCT-004 à FCT-007).

Deuxièmement, **fraude et effet sur le résultat sont deux arêtes différentes**. Dans le même dossier marseillais, le juge conclut que les volumes litigieux, rapportés aux écarts de voix, n’ont pas modifié l’ordre des listes ni la répartition globale des sièges. Il prononce pourtant des conséquences individuelles fortes : trois candidats sont déclarés inéligibles pour un an et leurs élections individuelles sont annulées (FCT-008, FCT-009). Le cas détruit donc les deux raccourcis opposés : « s’il y a fraude, le résultat est forcément faux » et « si le résultat n’a pas changé, il n’y a pas eu fraude ».

Troisièmement, **irrégularité ou erreur ne signifient pas automatiquement fraude**. Le comparateur berlinois est utile précisément parce qu’il est isomorphe sur le contrôle électoral mais différent sur l’intention. La Cour constitutionnelle de Berlin a retenu de graves défaillances systémiques de préparation et d’organisation, suffisamment importantes pour invalider le scrutin régional et imposer une répétition. La Cour constitutionnelle fédérale a également ordonné une répétition partielle du scrutin fédéral dans des centaines de bureaux. Ces décisions établissent qu’un défaut administratif peut devenir matériel pour la représentation sans qu’il soit nécessaire de le requalifier en fraude intentionnelle (FCT-026 à FCT-028).

## Ce que la France permet d’établir

Le droit français fournit un vocabulaire opérationnel. Les dispositions pénales du code électoral distinguent plusieurs actes : fausse inscription, substitution de signature ou d’identité, vote sous l’identité d’un autre électeur, et manipulation des bulletins par les personnes chargées de leur réception ou de leur dépouillement (FCT-001 à FCT-003). Cette granularité est méthodologiquement importante : elle empêche de traiter comme « fraude » toute anomalie, tout retard, tout contentieux ou tout résultat inattendu.

Le dossier marseillais ferme ensuite le passage du droit abstrait au cas réel. Il ne s’agit pas d’une simple plainte ou d’une suspicion. Le Conseil d’État s’appuie notamment sur un rapport d’enquête de police judiciaire et constate des formulaires préparés sans consentement de résidents d’EHPAD, d’autres remplis hors présence des mandants et une validation déficiente de ces procurations. Le juge retient explicitement le caractère frauduleux des manoeuvres. Ce niveau de preuve dépasse donc l’allégation et l’irrégularité non qualifiée.

Mais ce dossier ne peut pas devenir un taux national. Il ne donne ni le nombre de scrutins comparables, ni la population totale exposée à des mécanismes similaires, ni un recensement national des contentieux où une fraude a été retenue ou rejetée. Il établit l’existence, pas la prévalence.

## Contrôle du système électoral : ni zéro fraude, ni fraude systémique

Les évaluations OSCE/ODIHR des élections présidentielle et législatives françaises de 2022 constituent un contrôle négatif utile. Elles décrivent des élections compétitives et pluralistes, administrées efficacement et bénéficiant d’un niveau élevé de confiance publique (FCT-010, FCT-011, FCT-013). Elles formulent simultanément des recommandations d’amélioration : méthodes de vote, observation, formation des responsables de bureaux, possibilité de recomptage des bulletins valides, sécurité des données et résolution des litiges (FCT-012, FCT-014).

Ces deux éléments doivent être conservés ensemble. Une appréciation globalement positive du système n’est pas une preuve d’absence absolue de fraude. Inversement, l’existence de cas de fraude ou d’erreurs ne suffit pas à établir une architecture nationale de fraude systémique. Le niveau correct est : **système électoral globalement fonctionnel dans les évaluations examinées, avec incidents, irrégularités et fraudes case-specific qui doivent être traités séparément**.

L’évolution des procurations renforce la nécessité de raisonner par mécanisme et dénominateur. Pour les européennes et législatives de 2024, le ministère de l’Intérieur indique 3,5 millions de procurations établies via MaProcuration, dont 102 004 complètement dématérialisées avec identité numérique certifiée. Aux législatives, 75 % des demandes de procuration ont été faites en ligne. La transmission par le Répertoire électoral unique et les permanences de contrôle des procurations tardives constituent des mécanismes de sécurisation (FCT-015 à FCT-017). Ces volumes décrivent l’exposition au canal « procuration » ; ils ne mesurent pas le nombre de fraudes.

## L’accusation de fraude comme objet distinct

Le second versant d’INV-099 est la circulation d’accusations qui utilisent le vocabulaire de la fraude sans satisfaire la chaîne probatoire.

Après les législatives de 2022, des publications ont affirmé qu’Olivier Véran et Éric Woerth avaient bénéficié d’une fraude sur machines à voter. Le test matériel est simple : leurs circonscriptions n’étaient pas équipées de telles machines. L’AFP rapporte que certains messages ont néanmoins été partagés plusieurs milliers de fois. Elle rappelle aussi que seules 61 communes, représentant environ 1,3 million d’électeurs, utilisaient des machines à voter lors des scrutins de 2022 (FCT-018 à FCT-020). Ici, l’accusation n’est pas seulement non démontrée : le mécanisme allégué est absent des circonscriptions concernées.

Après le second tour présidentiel, d’autres publications ont affirmé que le Rassemblement national demandait un recomptage pour suspicion de fraude. Le parti a déclaré reconnaître les résultats et n’avoir engagé aucune démarche de ce type. Dans le même corpus, l’AFP rapporte que le Conseil constitutionnel avait annulé 20 594 suffrages sur plus de 35 millions de suffrages exprimés pour diverses irrégularités de bureaux de vote. Ces suffrages annulés sont un objet réel ; ils ne valident pas pour autant les récits de fraude massive ou de recomptage imaginaire (FCT-021, FCT-022).

Un autre exemple montre comment une erreur externe au processus électoral peut devenir une preuve apparente de fraude. France 2 a brièvement affiché environ 14,4 millions de voix pour Marine Le Pen pendant la soirée du second tour. France Télévisions a reconnu un bug de traitement de données ; les archives du ministère de l’Intérieur consultées par Le Monde ne présentaient pas ce chiffre (FCT-024, FCT-025). L’événement observable est donc réel — un mauvais nombre a été affiché — mais son emplacement causal est la chaîne de présentation télévisuelle, non le décompte officiel des votes.

Ces exemples ne démontrent pas une « industrie » coordonnée de l’accusation au sens organisationnel. Ils démontrent quelque chose de plus borné : **plusieurs récits de fraude ont circulé avec des mécanismes faux, absents ou confondus avec des erreurs périphériques**. Pour passer à une architecture coordonnée, il faudrait identifier acteurs, tasking, financement, synchronisation et contrôle. Ces arêtes ne sont pas fermées ici.

## Fréquence : ce qui peut et ne peut pas être calculé

Le principal gap reste le dénominateur. Les données du ministère de la Justice sont en principe déclinables par nature d’infraction et des séries historiques sont publiées. Mais le corpus courant n’a pas extrait un ensemble national harmonisé des infractions électorales, ni relié ces données aux décisions de contentieux électoral, aux scrutins, aux électeurs exposés et aux recours rejetés (FCT-029, FCT-030).

Il serait donc incorrect de produire un taux national de fraude à partir du seul nombre de décisions trouvées, du volume de suffrages annulés, du nombre de procurations, du nombre de recours ou du nombre de condamnations. Ces ensembles mesurent des choses différentes. Un taux défendable demanderait au minimum une règle de codage commune distinguant : accusation, irrégularité, erreur, fraude retenue, fraude pénalement condamnée, remède administratif, votes potentiellement affectés et effet sur le résultat.

La conclusion probabiliste doit rester asymétrique : **l’existence de fraudes électorales réelles est établie ; leur prévalence nationale n’est pas établie par ce corpus**. Cette absence de mesure n’est ni une preuve de fréquence élevée ni une preuve de fréquence nulle.

## Plafond probatoire I0-I7

- **I0 = VERIFIED** : acteurs, institutions, voies de contrôle et relations de cas sont identifiables.
- **I1 = VERIFIED** : accès aux mécanismes électoraux, systèmes de procuration et capacités administratives sont documentés.
- **I2 = VERIFIED case-specifically** : actes frauduleux et erreurs électorales sont documentés dans des cas distincts.
- **I3 = VERIFIED case-specifically / NOT_ESTABLISHED generally** : une coordination locale existe dans le dossier marseillais ; aucune architecture nationale coordonnée n’est établie.
- **I4 = VERIFIED/PARTIAL** : volumes de procurations, votes potentiellement irréguliers et diffusion de certains messages sont documentés, sans dénominateur national commun.
- **I5 = NOT_ESTABLISHED** : l’effet persuasif des accusations de fraude n’est pas mesuré.
- **I6 = VERIFIED case-specifically / NOT_ESTABLISHED generally** : inéligibilités, annulations individuelles et répétitions de scrutin sont observables ; aucun effet comportemental national général n’est établi.
- **I7 = NOT_ESTABLISHED generally** : aucun résultat électoral national contrefactuel n’est démontré comme changé par la fraude dans ce corpus.

## Résidu matériel

Trois upgrades seulement pourraient changer matériellement ce modèle : un corpus national codé des infractions/contentieux électoraux avec dénominateurs, une extraction fiable des condamnations par infractions électorales, ou des données d’exposition permettant de relier les accusations de fraude à la confiance et au comportement électoral. Une collecte web générique supplémentaire serait surtout cumulative.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:5|SRC_COMPLETE:11/11

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-08
- **notes:**
  - French core fraud case: Marseille municipal 2020 adjudicated 2022
  - OSCE controls: presidential and parliamentary 2022
  - accusation controls concentrated on 2022 national elections
  - proxy administration updated through May 2026
  - German comparator covers Berlin 2021 litigation through 2023
- **status:** CURRENT_THROUGH_2026
- **window:** 2000-2026

### MANIPULATION_REPORT
- **assumptions:**
  - judicial findings are case-specific
  - OSCE assessment does not prove zero fraud
  - fact-check examples do not census all accusations
- **clusters:**
  - **loaded:**
    - clusters/POWER.md
    - clusters/FRAMING.md
    - clusters/NETWORK.md
- **complexity:**
  - **band:** APEX
  - **score:** 8
- **implicit:**
  - electoral systems can contain both real fraud cases and non-fraud errors
  - correction mechanisms can operate without implying systemic failure
  - rumor ecosystems may exploit anomalies or impossible mechanisms
- **input_kind:** RUN_CARD
- **mission_mode:** GREENFIELD
- **patterns:**
  - proxy fraud
  - procedural error
  - electoral remedy
  - viral fraud claim
  - display bug
- **priorities:**
  - mechanism
  - proof
  - intent
  - denominator
  - effect
- **query_guidance:** bind every fraud claim to a concrete electoral mechanism and authority; keep rumor exposure separate from fraud occurrence.
- **rhetorical:**
  - **AUTH:** authority supplies adjudicated/administrative records but remains claim-bound
  - **BF:** selected cases are not a national base rate
  - **DEM:** German comparator is procedural, not prevalence evidence
  - **FAC:** separate fraud, error, accusation, detection and effect
  - **NUM:** all counts retain their denominator and case scope
- **speaker:**
  - **goal:** forensic discrimination of actual fraud, error/irregularity and fraud accusations
  - **target:** mechanism/proof/effect versus accusation
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **Κ:** 4
  - **Λ:** 4
  - **Ξ:** 4
  - **Σ:** 4
  - **Φ:** 5
  - **Ψ:** 3
  - **Ω:** 4
  - **κ:** 4
  - **ρ:** 5
  - **€:** 2
  - **↕:** 4
  - **⏰:** 3
  - **⚔:** 4
  - **⫸:** 4
  - **🌐:** 4
- **threats:**
  - official_statement=proof_by_status
  - complaint=proof
  - error=intent
  - viral=frequent_fraud

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - national responsibility chain beyond cases
  - **input_ids:**
    - FCT-004
    - FCT-007
    - FCT-009
    - FCT-015
    - FCT-017
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no general state or party command architecture established
  - **not_computable:**
    - unrecorded informal tasking
  - **operations_applied:**
    - mapped decision/control authorities
    - separated access to proxy process from proven fraudulent responsibility
  - **reason:** fraud allegations require separating actor authority, access, control and responsibility
  - **result_ids:**
    - CLM-002
    - CLM-004
    - CTRL-001
    - CTRL-005
  - **status:** DONE
  - **trigger:** ↕
- **item 2:**
  - **gaps:**
    - total exposure and persuasion of fraud narratives
  - **input_ids:**
    - FCT-018
    - FCT-019
    - FCT-021
    - FCT-023
    - FCT-024
    - FCT-025
  - **module:** clusters/FRAMING.md
  - **negative_results:**
    - no evidence that accusation volume tracks fraud frequency
  - **not_computable:**
    - audience belief change without survey/experimental data
  - **operations_applied:**
    - separated claim from mechanism
    - tested error/bug/absence against fraud framing
  - **reason:** object explicitly contrasts real fraud with public accusations and framing of anomalies
  - **result_ids:**
    - CLM-005
    - CTRL-004
    - CAU-001
  - **status:** DONE
  - **trigger:** Φ
- **item 3:**
  - **gaps:**
    - origin/coordination of broader accusation ecosystem
  - **input_ids:**
    - FCT-004
    - FCT-005
    - FCT-007
    - FCT-019
    - FCT-021
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no transversal coordinated national fraud or accusation network established
  - **not_computable:**
    - private coordination without records
  - **operations_applied:**
    - mapped local participant relations
    - kept social diffusion distinct from coordinated campaign
  - **reason:** Marseille and accusation diffusion involve multiple actors/intermediaries but coordination claims require bounded edges
  - **result_ids:**
    - CLM-002
    - CLM-005
    - CTRL-005
  - **status:** DONE
  - **trigger:** 🌐

### SCOPING_REPORT
- **actors_institutions:**
  - Conseil d’État
  - OSCE/ODIHR
  - Ministère de l’Intérieur
  - Conseil constitutionnel via AFP reporting
  - German constitutional courts
  - Ministère de la Justice
  - media/fact-checkers
- **domains:**
  - electoral law
  - proxy voting
  - election administration
  - election litigation
  - misinformation/claims
- **evidence_limits:**
  - no harmonized national fraud denominator
  - selected litigation is not a census
  - Justice series not extracted at election-offence code level
  - online accusation exposure/attitude effect not measured
- **exclusions:**
  - generic claims without mechanism/proof
  - foreign-interference attribution as separate object
  - fraud prevalence inferred from isolated cases
  - political legitimacy judgments without evidentiary edge
- **geo:** France priority; Germany as mechanism-isomorphic procedural comparator
- **lead_question:** Fraude électorale réelle versus industrie de l’accusation de fraude
- **object_coverage:** STRONG_FOR_TAXONOMY_AND_CASE_SPECIFIC_FRAUD; STRONG_FOR_ERROR/FRAUD_BOUNDARY; MODERATE_FOR_ACCUSATION_CONTROLS; WEAK_FOR_NATIONAL_PREVALENCE_AND_CAUSAL_POLITICAL_EFFECT
- **object_question:** Quelle fréquence/nature de fraude est effectivement établie et comment la distinguer des erreurs, irrégularités et accusations ?
- **period:** 2000-2026

### CREDO
- allegation != fraud
- irregularity != fraud
- error != intent
- complaint != proof
- case != prevalence
- fraud_exists != result_changed
- accusation_volume != fraud_frequency
- detected_cases != total_prevalence

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** GREENFIELD
- **patterns:**
  - proxy fraud
  - identity/signature fraud
  - ballot alteration
  - administrative election error
  - repeat election remedy
  - fraud accusation/misinformation
  - media display bug
- **priorities:**
  - legal taxonomy
  - positive adjudicated fraud case
  - error/irregularity controls
  - accusation falsification
  - prevalence denominator
  - effect ceiling
- **query_guidance:** prefer official judicial/election-administration sources for fraud/error; use fact-checking only for bounded accusation examples; never infer prevalence from cases or claim volume.
- **speaker:**
  - **goal:** forensic discrimination of actual fraud, error/irregularity and fraud accusations
  - **target:** actor/action -> electoral mechanism -> proof -> remedy/effect; claim -> exposure -> possible trust/effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **threats:**
  - allegation=fraud
  - irregularity=fraud
  - error=intent
  - case=prevalence
  - fraud=result_changed
  - accusation_volume=fraud_frequency

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** Des erreurs systémiques ou techniques peuvent être suffisamment graves pour invalider ou répéter un scrutin sans preuve d’intention frauduleuse.
  - **resolution:** Qualifier séparément erreur/irrégularité, fraude intentionnelle et effet; exiger un mécanisme et une preuve de l’intention lorsque la fraude est alléguée.
  - **thesis:** Toute irrégularité électorale prouve une fraude.
- **item 2:**
  - **antithesis:** À Marseille, des manoeuvres frauduleuses ont été établies mais les écarts de voix empêchaient une incidence sur l’ordre des listes et les sièges globaux.
  - **resolution:** Fraude et résultat contrefactuel sont deux arêtes distinctes; mesurer volume, marge et conséquence institutionnelle.
  - **thesis:** Toute fraude établie change nécessairement le résultat.
- **item 3:**
  - **antithesis:** Plusieurs accusations 2022 reposaient sur des machines absentes, un recomptage jamais demandé ou un bug France 2 externe au décompte officiel.
  - **resolution:** Mesurer séparément accusation, mécanisme réel, preuve, exposition et effet sur la confiance.
  - **thesis:** La multiplication des accusations montre une multiplication de la fraude.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **boundary:** fraud established case-specifically; not national prevalence
  - **from:** candidate network
  - **support:**
    - FCT-004
    - FCT-005
    - FCT-006
  - **to:** proxy forms/votes
  - **vehicle:** improper proxy preparation
- **item 2:**
  - **boundary:** administrative control path; volume is not fraud count
  - **from:** voter proxy request
  - **support:**
    - FCT-015
    - FCT-016
    - FCT-017
  - **to:** municipal electoral roll
  - **vehicle:** MaProcuration -> REU validation
- **item 3:**
  - **boundary:** claim circulation; mechanism often unverified or false
  - **from:** social posts
  - **support:**
    - FCT-018
    - FCT-019
    - FCT-021
    - FCT-023
  - **to:** online audience
  - **vehicle:** claims about voting machines/recount
- **item 4:**
  - **boundary:** media presentation error external to official count
  - **from:** France 2 data processing
  - **support:**
    - FCT-024
    - FCT-025
  - **to:** broadcast audience
  - **vehicle:** temporary display bug

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** candidats/entourage local
  - **limits:**
    - case-specific; organisation locale != architecture nationale
  - **relation:** collecte/préparation de procurations
  - **support:**
    - FCT-004
    - FCT-005
    - FCT-007
  - **to:** électeurs/mandants et administration de procuration
- **item 2:**
  - **from:** administration électorale française
  - **limits:**
    - control infrastructure != zero fraud
  - **relation:** REU, MaProcuration, validation et contrôles de bureau
  - **support:**
    - FCT-015
    - FCT-016
    - FCT-017
  - **to:** électeurs et communes
- **item 3:**
  - **from:** comptes et relais sociaux
  - **limits:**
    - circulation != truth; exposure != persuasion
  - **relation:** diffusion d’accusations de fraude/recomptage/machines
  - **support:**
    - FCT-019
    - FCT-021
    - FCT-023
  - **to:** audiences en ligne
- **item 4:**
  - **from:** médias/fact-checkers
  - **limits:**
    - fact-check != measurement of total accusation universe
  - **relation:** vérification de mécanismes allégués et correction de bugs/rumeurs
  - **support:**
    - FCT-018
    - FCT-021
    - FCT-024
    - FCT-025
  - **to:** public
- **item 5:**
  - **from:** juridictions électorales allemandes
  - **limits:**
    - German comparator != French prevalence
  - **relation:** qualification d’erreurs et ordre de répétition
  - **support:**
    - FCT-026
    - FCT-027
    - FCT-028
  - **to:** administration/scrutin

### IMPACT_MAP
- **behavior:** NOT_ESTABLISHED generally
- **electoral_effect:** VERIFIED case-specific for corrective/ineligibility/rerun consequences; general causal effect NOT_ESTABLISHED
- **free_determination:** NOT_MEASURED generally
- **material_access:** VERIFIED for proxy infrastructure and voting mechanisms
- **persuasion:** NOT_ESTABLISHED for fraud accusations
- **sincerity_of_ballot:** CASE_SPECIFIC; fraud/errors can affect sincerity but not uniformly
- **support:**
  - FCT-008
  - FCT-009
  - FCT-026
  - FCT-028

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** Berlin documente de graves erreurs de préparation/organisation conduisant à une répétition.
  - **issue:** fraude versus erreur
  - **pro:** Marseille comporte une qualification explicite de manoeuvres frauduleuses.
  - **resolution:** intentional fraud and procedural error are separate categories
  - **support:**
    - FCT-007
    - FCT-026
    - FCT-028
- **item 2:**
  - **contra:** le juge exclut une incidence sur l’ordre des listes et la répartition globale des sièges.
  - **issue:** fraude versus changement du résultat
  - **pro:** Marseille établit fraude et inéligibilités individuelles.
  - **resolution:** result effect requires a distinct margin/volume assessment
  - **support:**
    - FCT-007
    - FCT-008
    - FCT-009
- **item 3:**
  - **contra:** plusieurs mécanismes allégués étaient absents ou relevaient d’un bug d’affichage.
  - **issue:** accusation versus occurrence
  - **pro:** des accusations de fraude ont largement circulé en 2022.
  - **resolution:** accusation volume is not a fraud denominator
  - **support:**
    - FCT-018
    - FCT-019
    - FCT-021
    - FCT-024
    - FCT-025

### VERIFICATION_REPORT
- **circular_families:**
  - OSCE presidential/parliamentary treated as one provenance family; AFP two fact-checks treated as one family
- **contradiction_ids:**
  - fraud-vs-error
  - fraud-vs-result
  - accusation-vs-occurrence
- **downgraded_ids:**
  - NONE
- **none_found_claims:**
  - national prevalence of intentional electoral fraud
  - general coordinated national fraud architecture
  - causal persuasion/behavior change from fraud accusations
  - counterfactual national election result changed by fraud
- **remaining_gaps:**
  - national harmonized denominator of cases/exposure
  - election-specific criminal conviction extraction
  - platform-scale accusation exposure and trust effect
  - counterfactual outcome designs
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
- **sources_reopened:** 11
- **upgraded_ids:**
  - NONE
- **verdict:** READY_FOR_PRE_GATE

### EDI_REPORT
- **corpus:**
  - **circularity:** AFP and Le Monde accusation examples are secondary and not used to establish fraud occurrence
  - **coverage:** STRONG_FOR_CASE_SPECIFIC_EXISTENCE_AND_BOUNDARIES; WEAK_FOR_PREVALENCE
  - **independence:** MULTIPLE_OFFICIAL_AND_MEDIA_FAMILIES
  - **limits:**
    - no harmonized national fraud denominator
    - no platform-scale accusation exposure
    - selected litigation not census
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-002
    - **direct_object:** YES_ADJUDICATED
    - **gap_type:** SCOPE
    - **independent_families:** 1
  - **item 2:**
    - **claim_id:** CLM-003
    - **direct_object:** YES_ERROR_CONTROLS
    - **gap_type:** QUALIFICATION
    - **independent_families:** 2
  - **item 3:**
    - **claim_id:** CLM-004
    - **direct_object:** YES_CASE_SPECIFIC_EFFECT_BOUNDARY
    - **gap_type:** NONE
    - **independent_families:** 1
  - **item 4:**
    - **claim_id:** CLM-005
    - **direct_object:** YES_ACCUSATION_CONTROLS
    - **gap_type:** EXPOSURE
    - **independent_families:** 2
  - **item 5:**
    - **claim_id:** CLM-006
    - **direct_object:** BOUNDARY_ONLY
    - **gap_type:** SCOPE
    - **independent_families:** 5
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** 8_PROVENANCE_FAMILIES
  - **perspective:** LAW+COURTS+ELECTION_ADMINISTRATION+OSCE+JUSTICE+FACT_CHECKING
  - **stratification:** FRAUD+ERROR+CONTROL+ACCUSATION+REMEDY
  - **temporal:** 2020-2026 core France; German 2021-2023 comparator
- **edi:**
  - **assessment:** STRONG_DISCRIMINATION_ACROSS_FRAUD_ERROR_AND_ACCUSATION; PREVALENCE_UNRESOLVED
  - **flags:**
    - OFFICIAL_JUDICIAL_POSITIVE_CASE
    - OFFICIAL_SYSTEM_CONTROLS
    - ISOMORPHIC_ERROR_COMPARATOR
    - SECONDARY_RUMOR_CONTROLS
    - NO_COMMON_DENOMINATOR
- **source_counts:**
  - **primary:** 8
  - **provenance_families:** 8
  - **secondary:** 3
  - **tertiary:** 0
  - **total:** 11

### RESPONSIBILITY_MAP
- **boundary:** suspicion, irregularity, unexpected result, complaint or viral allegation cannot establish responsibility or intent without a documented actor->action->mechanism->proof edge
- **not_established:**
  - general coordinated national fraud architecture
  - national prevalence of intentional electoral fraud
  - organized origin of the broader 2022 fraud-accusation ecosystem
  - causal voter persuasion from fraud claims
  - counterfactual national election result change
- **verified:**
  - case-specific participants in Marseille proxy manoeuvres and judicial consequences
  - French electoral administration control routes for proxies
  - courts’ authority to qualify errors/fraud and order remedies

### NEXT_QUERIES
- RECHECK if Justice/NATINF machine-readable tables permit election-offence counts and a defensible denominator
- RECHECK a systematic Conseil constitutionnel/Conseil d’État corpus coded by allegation, finding, remedy and vote margin
- RECHECK platform-scale exposure data for French fraud accusations if available
- DEFER national systemic-fraud and accusation->trust/vote causal claims until denominator/exposure designs exist

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-011 | support:- | counter:- | results:FCT-001,FCT-004,FCT-007,FCT-018,FCT-021,FCT-024,FCT-026,FCT-029 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-008,QRY-009 | support:- | counter:- | results:FCT-006,FCT-008,FCT-009,FCT-011,FCT-013,FCT-015,FCT-027,FCT-028 | final:SATURATED | gap:NONE
LED-003 | attempts:QRY-002,QRY-003,QRY-005,QRY-006,QRY-010,QRY-011 | support:- | counter:- | results:FCT-010,FCT-013,FCT-018,FCT-021,FCT-029,FCT-030 | final:GAP | gap:SCOPE
AXS-001 | attempts:QRY-001,QRY-011 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-007 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001 | support:- | counter:- | results:FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-008,QRY-009,QRY-002,QRY-003 | support:- | counter:- | results:FCT-012,FCT-014,FCT-026,FCT-027,FCT-028 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-005,QRY-006,QRY-007 | support:- | counter:- | results:FCT-018,FCT-019,FCT-020,FCT-021,FCT-023,FCT-024,FCT-025 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-002,QRY-003,QRY-004,QRY-010 | support:- | counter:- | results:FCT-010,FCT-013,FCT-015,FCT-016,FCT-017,FCT-029,FCT-030 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-001,QRY-002,QRY-003,QRY-008,QRY-009 | support:- | counter:- | results:FCT-008,FCT-009,FCT-011,FCT-013,FCT-026,FCT-027,FCT-028 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-011,SRC-011 | support:FCT-001,FCT-002,FCT-003 | counter:CTRL-001 | results:FCT-001,FCT-002,FCT-003,CTRL-001 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-001,SRC-001 | support:FCT-004,FCT-005,FCT-006,FCT-007 | counter:CTRL-001,CTRL-005 | results:FCT-004,FCT-005,FCT-006,FCT-007,CTRL-001,CTRL-005 | final:SUPPORTED | gap:SCOPE
CLM-003 | attempts:QRY-002,QRY-003,QRY-008,QRY-009,SRC-002,SRC-003,SRC-008,SRC-009 | support:FCT-026,FCT-027,FCT-028,FCT-012,FCT-014 | counter:CTRL-002 | results:FCT-026,FCT-027,FCT-028,FCT-012,FCT-014,CTRL-002 | final:SUPPORTED | gap:QUALIFICATION
CLM-004 | attempts:QRY-001,SRC-001 | support:FCT-007,FCT-008,FCT-009 | counter:CTRL-003 | results:FCT-007,FCT-008,FCT-009,CTRL-003 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-005,QRY-006,QRY-007,SRC-005,SRC-006,SRC-007 | support:FCT-018,FCT-019,FCT-021,FCT-023,FCT-024,FCT-025 | counter:CTRL-004 | results:FCT-018,FCT-019,FCT-021,FCT-023,FCT-024,FCT-025,CTRL-004 | final:SUPPORTED | gap:EXPOSURE
CLM-006 | attempts:QRY-002,QRY-003,QRY-004,QRY-010,SRC-002,SRC-003,SRC-004,SRC-010 | support:FCT-010,FCT-011,FCT-013,FCT-015,FCT-016,FCT-017,FCT-029,FCT-030 | counter:CTRL-005,CTRL-006 | results:FCT-010,FCT-011,FCT-013,FCT-015,FCT-016,FCT-017,FCT-029,FCT-030,CTRL-005,CTRL-006 | final:SUPPORTED | gap:SCOPE

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-002 | CLM | SUPPORTED | SCOPE | Un cas judiciairement établi ne mesure pas la fréquence nationale.
CLM-003 | CLM | SUPPORTED | QUALIFICATION | Le corpus allemand sert de comparateur procédural; il ne mesure pas la fréquence des erreurs en France.
CLM-005 | CLM | SUPPORTED | EXPOSURE | Le corpus documente la circulation de certains récits mais ne mesure pas leur exposition totale ni leur effet sur la confiance.
CLM-006 | CLM | SUPPORTED | SCOPE | Il manque un dataset national harmonisé de cas, recours, condamnations et suffrages exposés permettant un taux de fraude établi.
CAU-001 | CAU | GAP | CAUSALITY | Manquent un dénominateur national harmonisé, une mesure d’exposition aux accusations et des designs reliant fraude/accusation à changement de comportement puis résultat contrefactuel.

SEMANTIC_COUNTS_V1:LED:3|CLM:6|AXS:6|CAU:1|CTRL:6|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-011"],"evidence_excerpt":"Le corpus combine une qualification judiciaire explicite de manoeuvres frauduleuses, des erreurs électorales corrigées sans preuve d’intention frauduleuse, et des accusations dont le mécanisme allégué était matériellement absent.","kind":"DISCRIMINATION_LEAD","lead":"Distinguer fraude intentionnelle établie, erreur/irrégularité procédurale et accusation de fraude par le type de preuve, le mécanisme et la décision de contrôle.","linked_ids":["CLM-001","CLM-002","CLM-003","CLM-005"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-004","FCT-007","FCT-018","FCT-021","FCT-024","FCT-026","FCT-029"],"routes":["INV-102"],"source_id":"INV-099_RUN_CARD","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-008","QRY-009"],"evidence_excerpt":"Marseille établit fraude et conséquences individuelles sans changement du résultat global; Berlin établit au contraire des erreurs assez matérielles pour imposer une répétition.","kind":"MECHANISM_LEAD","lead":"Tester séparément existence du mécanisme, volume/exposition et effet sur la sincérité ou le résultat.","linked_ids":["CLM-002","CLM-004","CLM-006","CAU-001"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-006","FCT-008","FCT-009","FCT-011","FCT-013","FCT-015","FCT-027","FCT-028"],"routes":["INV-102"],"source_id":"INV-099_RUN_CARD","status":"SATURATED"}
LED-003 | {"attempt_ids":["QRY-002","QRY-003","QRY-005","QRY-006","QRY-010","QRY-011"],"evidence_excerpt":"Les sources permettent de coder des cas et des contrôles, mais pas de calculer un taux national de fraude sur l’ensemble des scrutins ou des suffrages.","gap":"Le corpus ne fournit pas un dénominateur national commun reliant infractions pénales électorales, contentieux administratifs, irrégularités corrigées et accusations publiques; les séries Justice sont disponibles par infraction mais l’extraction électorale spécifique n’est pas réalisée ici.","gap_type":"SCOPE","kind":"SYSTEM_GAP","lead":"Mesurer une fréquence nationale comparable de fraude établie et la distinguer du volume des recours, erreurs et accusations.","linked_ids":["CLM-004","CLM-005","CLM-006","CAU-001"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-010","FCT-013","FCT-018","FCT-021","FCT-029","FCT-030"],"routes":["RECHECK(national coded electoral-offence dataset)","DEFER(national prevalence/effect claim)"],"source_id":"INV-099_RUN_CARD","status":"GAP"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Le droit électoral français définit plusieurs mécanismes frauduleux distincts, notamment fausse inscription, usurpation d’identité/signature et altération des bulletins.","claimant":"INV-099 synthesis","counter":"CTRL-001","gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003"]}
CLM-002 | {"claim":"La fraude électorale existe factuellement en France de façon case-specific: le Conseil d’État a explicitement qualifié de manoeuvres frauduleuses un système de procurations irrégulières à Marseille en 2020.","claimant":"INV-099 synthesis","counter":["CTRL-001","CTRL-005"],"gap":"Un cas judiciairement établi ne mesure pas la fréquence nationale.","gap_type":"SCOPE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-004","FCT-005","FCT-006","FCT-007"]}
CLM-003 | {"claim":"Une erreur ou irrégularité électorale grave peut entraîner répétition ou invalidation d’un scrutin sans que l’intention frauduleuse soit établie; fraude et erreur doivent donc rester des catégories séparées.","claimant":"INV-099 synthesis","counter":"CTRL-002","gap":"Le corpus allemand sert de comparateur procédural; il ne mesure pas la fréquence des erreurs en France.","gap_type":"QUALIFICATION","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-026","FCT-027","FCT-028","FCT-012","FCT-014"]}
CLM-004 | {"claim":"Une fraude établie n’implique pas automatiquement que le résultat global ait changé: à Marseille, les manoeuvres ont conduit à des inéligibilités individuelles mais pas à l’annulation des opérations électorales globales.","claimant":"INV-099 synthesis","counter":"CTRL-003","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-007","FCT-008","FCT-009"]}
CLM-005 | {"claim":"Le volume d’accusations publiques de fraude ne mesure pas la fréquence de la fraude réelle: en 2022, plusieurs récits diffusés ont invoqué des machines absentes, un recomptage non demandé ou un bug d’affichage télévisuel extérieur au décompte officiel.","claimant":"INV-099 synthesis","counter":"CTRL-004","gap":"Le corpus documente la circulation de certains récits mais ne mesure pas leur exposition totale ni leur effet sur la confiance.","gap_type":"EXPOSURE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-018","FCT-019","FCT-021","FCT-023","FCT-024","FCT-025"]}
CLM-006 | {"claim":"Le corpus courant ne permet pas d’estimer une prévalence nationale fiable des fraudes électorales établies ni de conclure à une architecture systémique de fraude en France; les contrôles disponibles montrent un système administré avec confiance élevée tout en laissant des erreurs et cas de fraude possibles.","claimant":"INV-099 synthesis","counter":["CTRL-005","CTRL-006"],"gap":"Il manque un dataset national harmonisé de cas, recours, condamnations et suffrages exposés permettant un taux de fraude établi.","gap_type":"SCOPE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-010","FCT-011","FCT-013","FCT-015","FCT-016","FCT-017","FCT-029","FCT-030"]}

### AXIS_REGISTRY_V1
AXS-001 | {"assessment":"SPECIFIC_FRAUD_MECHANISMS_DEFINED","attempt_ids":["QRY-001","QRY-011"],"axis":"legal_and_operational_definition","links":["CLM-001","CLM-002"],"question":"Quels comportements constituent des fraudes électorales identifiables et sanctionnables ?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-007"],"sought_objects":["FALSE_REGISTRATION","IMPERSONATION","SIGNATURE_SUBSTITUTION","BALLOT_ALTERATION","FRAUDULENT_PROXY"],"status":"SATURATED"}
AXS-002 | {"assessment":"YES_CASE_SPECIFIC_MARSEILLE","attempt_ids":["QRY-001"],"axis":"positive_fraud_case","links":["CLM-002","CLM-004"],"question":"Existe-t-il un cas français récent où le juge qualifie explicitement les faits de manoeuvres frauduleuses ?","result_ids":["FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009"],"sought_objects":["PROXY_FRAUD","ACTORS","VOLUME","JUDICIAL_FINDING","RESULT_EFFECT"],"status":"SATURATED"}
AXS-003 | {"assessment":"YES_SYSTEMIC_ERRORS_DISTINCT_FROM_FRAUD","attempt_ids":["QRY-008","QRY-009","QRY-002","QRY-003"],"axis":"error_irregularity_boundary","links":["CLM-003","CTRL-002"],"question":"Des erreurs graves peuvent-elles invalider ou répéter une élection sans preuve de fraude intentionnelle ?","result_ids":["FCT-012","FCT-014","FCT-026","FCT-027","FCT-028"],"sought_objects":["PREPARATION_ERROR","PROCEDURAL_IRREGULARITY","RERUN","CORRECTION"],"status":"SATURATED"}
AXS-004 | {"assessment":"MULTIPLE_FALSE_OR_MECHANICALLY_INCOMPATIBLE_CLAIMS","attempt_ids":["QRY-005","QRY-006","QRY-007"],"axis":"accusation_verifiability","links":["CLM-005","CTRL-004"],"question":"Les accusations publiques de fraude correspondent-elles toujours à un mécanisme électoral réellement présent ?","result_ids":["FCT-018","FCT-019","FCT-020","FCT-021","FCT-023","FCT-024","FCT-025"],"sought_objects":["RUMOR","CLAIMED_MACHINE","RECOUNT","MEDIA_BUG","ACTUAL_MECHANISM"],"status":"SATURATED"}
AXS-005 | {"assessment":"NO_COMMON_NATIONAL_DENOMINATOR","attempt_ids":["QRY-002","QRY-003","QRY-004","QRY-010"],"axis":"prevalence_denominator","links":["CLM-006","CAU-001"],"question":"Peut-on calculer une fréquence nationale de fraude établie à partir du corpus courant ?","result_ids":["FCT-010","FCT-013","FCT-015","FCT-016","FCT-017","FCT-029","FCT-030"],"sought_objects":["CASES","VOTES","PROXIES","CONVICTIONS","COMPLAINTS","DENOMINATOR"],"status":"SATURATED"}
AXS-006 | {"assessment":"NO_EFFECT_IS_CASE_SPECIFIC","attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-008","QRY-009"],"axis":"effect_and_counterfactual","links":["CLM-004","CTRL-003","CAU-001"],"question":"Fraude ou irrégularité impliquent-elles automatiquement modification du résultat ?","result_ids":["FCT-008","FCT-009","FCT-011","FCT-013","FCT-026","FCT-027","FCT-028"],"sought_objects":["SINCERITY","RESULT_CHANGE","SEAT_CHANGE","RERUN","COUNTERFACTUAL"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"CTRL-002;CTRL-003;CTRL-004;CTRL-005;CTRL-006","gap":"Manquent un dénominateur national harmonisé, une mesure d’exposition aux accusations et des designs reliant fraude/accusation à changement de comportement puis résultat contrefactuel.","gap_type":"CAUSALITY","limit":"La chaîne est établie jusqu’à la qualification et certaines conséquences institutionnelles dans des cas précis; ni la prévalence nationale ni un effet général sur la confiance, le vote ou un résultat contrefactuel ne sont établis.","mechanism":"irrégularité ou acte intentionnel -> mécanisme électoral concret -> détection/preuve -> décision de contrôle -> correction ou sanction -> éventuel effet sur suffrages/sièges -> éventuel effet politique; en parallèle accusation publique -> exposition -> confiance/comportement éventuel","status":"GAP","support":["FCT-004","FCT-007","FCT-008","FCT-009","FCT-018","FCT-021","FCT-024","FCT-026","FCT-028"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Le code définit des infractions spécifiques; toute anomalie de procédure ou résultat inattendu ne constitue donc pas, par statut, une fraude.","status":"VERIFIED","support":["FCT-001","FCT-002","FCT-003"]}
CTRL-002 | {"control":"Berlin montre que des erreurs systémiques de préparation peuvent justifier une répétition du scrutin sans que la qualification de fraude intentionnelle soit nécessaire.","status":"VERIFIED","support":["FCT-026","FCT-027","FCT-028"]}
CTRL-003 | {"control":"Marseille montre que fraude établie et résultat changé sont deux arêtes distinctes: des manoeuvres frauduleuses ont été retenues sans incidence sur l’ordre des listes ni la répartition globale des sièges.","status":"VERIFIED","support":["FCT-007","FCT-008","FCT-009"]}
CTRL-004 | {"control":"Des accusations de fraude peuvent être factuellement incompatibles avec le mécanisme allégué ou reposer sur une erreur médiatique externe au comptage officiel.","status":"VERIFIED","support":["FCT-018","FCT-021","FCT-024","FCT-025"]}
CTRL-005 | {"control":"Les évaluations OSCE/ODIHR 2022 décrivent une administration efficace et une confiance publique élevée tout en formulant des recommandations d’amélioration; ces constats ne prouvent ni absence absolue de fraude ni fraude systémique.","status":"VERIFIED","support":["FCT-010","FCT-011","FCT-012","FCT-013","FCT-014"]}
CTRL-006 | {"control":"Cas détectés, votes annulés, nombre de procurations, recours et condamnations sont des dénominateurs différents; aucun ne peut être utilisé seul comme taux national de fraude totale.","status":"VERIFIED","support":["FCT-015","FCT-016","FCT-022","FCT-029","FCT-030"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:11|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL:MNEMO_UNAVAILABLE | mnemo | NONE | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | OK | SRC-001 | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2022-01-11/451509 | FETCH Conseil d’État 451509 Marseille procurations frauduleuses
QRY-002 | FETCH | OK | SRC-002 | https://odihr.osce.org/odihr/elections/france/525330 | FETCH OSCE ODIHR France présidentielle 2022 final report
QRY-003 | FETCH | OK | SRC-003 | https://odihr.osce.org/odihr/elections/france/535110 | FETCH OSCE ODIHR France législatives 2022 final report
QRY-004 | FETCH | OK | SRC-004 | https://www.senat.fr/questions/base/2026/qSEQ260207520.html | FETCH Sénat réponse ministère intérieur procurations 2026
QRY-005 | FETCH | OK | SRC-005 | https://factuel.afp.com/doc.afp.com.32CZ79X | FETCH AFP Factuel Véran Woerth fraude vote électronique 2022
QRY-006 | FETCH | OK | SRC-006 | https://factuel.afp.com/doc.afp.com.32962GJ | FETCH AFP Factuel faux recomptage RN présidentielle 2022
QRY-007 | FETCH | OK | SRC-007 | https://www.lemonde.fr/les-decodeurs/article/2022/04/25/election-presidentielle-2022-une-video-de-france-2-montre-t-elle-une-fraude-electorale-dans-le-decompte-des-voix_6123625_4355770.html | FETCH Le Monde bug France 2 assimilé à fraude présidentielle 2022
QRY-008 | FETCH | OK | SRC-008 | https://www.berlin.de/gerichte/sonstige-gerichte/verfassungsgerichtshof/pressemitteilungen/2022/pressemitteilung.1265423.php | FETCH Berlin Verfassungsgerichtshof election 2021 invalidation
QRY-009 | FETCH | OK | SRC-009 | https://www.bundesverfassungsgericht.de/SharedDocs/Pressemitteilungen/EN/2023/bvg23-119.html | FETCH Bundesverfassungsgericht Berlin Bundestag repeat 2023
QRY-010 | FETCH | OK | SRC-010 | https://www.justice.gouv.fr/documentation/etudes-et-statistiques/condamnations | FETCH Ministère Justice condamnations données 1990-2024
QRY-011 | FETCH | OK | SRC-011 | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006070239/LEGISCTA000006148461/2022-12-09/ | FETCH Code électoral dispositions pénales L86-L117-2

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | CE-451509 | Conseil d’État — décision n°451509 | 2022-01-11 | 2026-09-08T05:56:00+02:00 | points 4-6,13: procurations, manoeuvres, incidence, inéligibilités | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2022-01-11/451509
SRC-002 | ◈ | fam:B | OSCE-FR-PRES-2022 | OSCE/ODIHR — France presidential election 2022 final report | 2022-09-06 | 2026-09-08T05:56:00+02:00 | competitive/pluralistic, administration, trust, improvement areas | https://odihr.osce.org/odihr/elections/france/525330
SRC-003 | ◈ | fam:B | OSCE-FR-PARL-2022 | OSCE/ODIHR — France parliamentary elections 2022 final report | 2022-12-19 | 2026-09-08T05:56:00+02:00 | effective administration, trust, recount/observation recommendations | https://odihr.osce.org/odihr/elections/france/535110
SRC-004 | ◈ | fam:C | SENAT-Q07520-2026 | Sénat — conditions d’établissement des procurations, réponse Intérieur | 2026-05-28 | 2026-09-08T05:56:00+02:00 | MaProcuration volumes, REU, late-proxy controls | https://www.senat.fr/questions/base/2026/qSEQ260207520.html
SRC-005 | ◈ | fam:other:afp | AFP-32CZ79X | AFP Factuel — Véran/Woerth fraude électronique impossible | 2022-06-24 | 2026-09-08T05:56:00+02:00 | claims, machine availability, official prefecture checks | https://factuel.afp.com/doc.afp.com.32CZ79X
SRC-006 | ◈ | fam:other:afp | AFP-32962GJ | AFP Factuel — faux recomptage RN après présidentielle | 2022-04-28 | 2026-09-08T05:56:00+02:00 | recount claim, RN denial, CC validation, rumor chronology | https://factuel.afp.com/doc.afp.com.32962GJ
SRC-007 | ◈ | fam:other:lemonde | LEMONDE-FR2-2022 | Le Monde — bug France 2 et rumeur de fraude | 2022-04-25 | 2026-09-08T05:56:00+02:00 | displayed totals, Interior archived totals, technical bug explanation | https://www.lemonde.fr/les-decodeurs/article/2022/04/25/election-presidentielle-2022-une-video-de-france-2-montre-t-elle-une-fraude-electorale-dans-le-decompte-des-voix_6123625_4355770.html
SRC-008 | ◈ | fam:D | BERLIN-VFGH-154-21 | Verfassungsgerichtshof Berlin — élections 2021 invalides | 2022-11-16 | 2026-09-08T05:56:00+02:00 | systemic preparation errors, mandate relevance, full repeat | https://www.berlin.de/gerichte/sonstige-gerichte/verfassungsgerichtshof/pressemitteilungen/2022/pressemitteilung.1265423.php
SRC-009 | ◈ | fam:D | BVERFG-2BVC4-23 | Bundesverfassungsgericht — Berlin Bundestag repeat election | 2023-12-19 | 2026-09-08T05:56:00+02:00 | repeat election scope and polling districts | https://www.bundesverfassungsgericht.de/SharedDocs/Pressemitteilungen/EN/2023/bvg23-119.html
SRC-010 | ◈ | fam:E | JUSTICE-CONDAMNATIONS-2026 | Ministère de la Justice — données sur les condamnations | 2026-04-23 | 2026-09-08T05:56:00+02:00 | CJN by offense; long-period downloadable tables | https://www.justice.gouv.fr/documentation/etudes-et-statistiques/condamnations
SRC-011 | ◈ | fam:other:legifrance | LEGIFRANCE-ELECTORAL-PENAL-2022 | Légifrance — Code électoral, dispositions pénales L86 à L117-2 | 2022-12-09 | 2026-09-08T05:56:00+02:00 | L86-L94 fraud/false identity/ballot alteration provisions | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006070239/LEGISCTA000006148461/2022-12-09/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006070239/LEGISCTA000006148461/2022-12-09/ | other:legifrance | 2026-09-08 | Code électoral: fraude d’inscription | Le chapitre pénal du code électoral incrimine notamment les inscriptions sous faux nom ou fausse qualité et les inscriptions obtenues par déclarations frauduleuses ou faux certificats. | -
FCT-002 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006070239/LEGISCTA000006148461/2022-12-09/ | other:legifrance | 2026-09-08 | Code électoral: fausse identité ou signature | L’article L92 sanctionne notamment la substitution ou imitation volontaire d’une signature sur la liste d’émargement et le vote sous le nom et les qualités d’un autre électeur. | -
FCT-003 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006070239/LEGISCTA000006148461/2022-12-09/ | other:legifrance | 2026-09-08 | Code électoral: altération des bulletins | L’article L94 sanctionne le fait, pour une personne chargée de recevoir, compter ou dépouiller les bulletins, de soustraire, ajouter ou altérer des bulletins ou de lire un autre nom. | -
FCT-004 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2022-01-11/451509 | A | 2026-09-08 | Marseille: 56 résidents sans consentement | Le Conseil d’État retient qu’une candidate a rempli des formulaires de procuration au nom de 56 résidents d’EHPAD sans leur consentement. | -
FCT-005 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2022-01-11/451509 | A | 2026-09-08 | Marseille: 167 formulaires irrégulièrement préparés | La décision établit qu’au total 167 formulaires concernant des électeurs du 6e secteur ont été remplis à l’insu des mandants ou hors leur présence. | -
FCT-006 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2022-01-11/451509 | A | 2026-09-08 | Marseille: votes potentiellement comptés | Le Conseil d’État estime qu’au maximum 158 voix au premier tour et 116 au second ont pu être comptabilisées au moyen de procurations irrégulièrement établies. | -
FCT-007 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2022-01-11/451509 | A | 2026-09-08 | Marseille: manoeuvres frauduleuses établies | Le Conseil d’État juge que les faits établis révèlent l’existence de manoeuvres frauduleuses au profit d’une liste. | -
FCT-008 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2022-01-11/451509 | A | 2026-09-08 | Marseille: pas d’incidence sur résultat global | Compte tenu du nombre de procurations irrégulières et des écarts de voix, le Conseil d’État juge que les manoeuvres n’ont pas eu d’incidence sur l’ordre des listes ni la répartition des sièges. | -
FCT-009 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2022-01-11/451509 | A | 2026-09-08 | Marseille: conséquences individuelles | Le Conseil d’État déclare trois candidats inéligibles pour un an en raison de manoeuvres frauduleuses graves et annule leurs élections individuelles, tout en maintenant les opérations électorales globales. | -
FCT-010 | FACT | ✧ | https://odihr.osce.org/odihr/elections/france/525330 | B | 2026-09-08 | OSCE présidentielle 2022: environnement | L’OSCE/ODIHR décrit l’élection présidentielle française de 2022 comme compétitive et pluraliste, avec respect des libertés fondamentales. | -
FCT-011 | FACT | ✧ | https://odihr.osce.org/odihr/elections/france/525330 | B | 2026-09-08 | OSCE présidentielle 2022: administration et confiance | L’OSCE/ODIHR indique que l’administration électorale a fonctionné efficacement et bénéficiait d’un niveau élevé de confiance publique. | -
FCT-012 | FACT | ✧ | https://odihr.osce.org/odihr/elections/france/525330 | B | 2026-09-08 | OSCE présidentielle 2022: améliorations recommandées | Le rapport final relève néanmoins des améliorations possibles concernant notamment les méthodes de vote, l’observation, le financement des campagnes et la régulation des médias. | -
FCT-013 | FACT | ✧ | https://odihr.osce.org/odihr/elections/france/535110 | B | 2026-09-08 | OSCE législatives 2022: administration | L’OSCE/ODIHR juge les législatives françaises de 2022 effectivement administrées et associées à un niveau élevé de confiance publique. | -
FCT-014 | FACT | ✧ | https://odihr.osce.org/odihr/elections/france/535110 | B | 2026-09-08 | OSCE législatives 2022: contrôles à améliorer | Parmi ses recommandations, l’OSCE/ODIHR préconise de rendre possible le recomptage des bulletins valides, d’améliorer la formation des présidents de bureaux et l’accès des observateurs. | -
FCT-015 | FACT | ✧ | https://www.senat.fr/questions/base/2026/qSEQ260207520.html | C | 2026-09-08 | Procurations 2024: volume Maprocuration | Le ministère de l’Intérieur indique que 3,5 millions de procurations ont été établies via MaProcuration lors des européennes et législatives 2024, dont 102 004 entièrement dématérialisées avec identité numérique certifiée. | -
FCT-016 | FACT | ✧ | https://www.senat.fr/questions/base/2026/qSEQ260207520.html | C | 2026-09-08 | Procurations 2024: 75 pour cent en ligne | Pour les législatives des 30 juin et 7 juillet 2024, 75 % des demandes de procuration au niveau national ont été établies en ligne. | -
FCT-017 | FACT | ✧ | https://www.senat.fr/questions/base/2026/qSEQ260207520.html | C | 2026-09-08 | Procurations: contrôle REU et permanence | Les procurations en ligne sont transmises au Répertoire électoral unique et, une fois validées, apparaissent directement sur les listes; des permanences communales/préfectorales sont prévues pour vérifier les procurations tardives. | -
FCT-018 | FACT | ✧ | https://factuel.afp.com/doc.afp.com.32CZ79X | other:afp | 2026-09-08 | Rumeur Véran/Woerth: mécanisme absent | Les accusations selon lesquelles Olivier Véran et Eric Woerth auraient gagné grâce à une fraude sur machines à voter sont incompatibles avec le fait qu’aucune de leurs deux circonscriptions n’était équipée de machine à voter. | -
FCT-019 | FACT | ✧ | https://factuel.afp.com/doc.afp.com.32CZ79X | other:afp | 2026-09-08 | Rumeur Véran/Woerth: diffusion | L’AFP rapporte que les accusations ont été relayées par plusieurs tweets, certains partagés plusieurs milliers de fois. | -
FCT-020 | FACT | ✧ | https://factuel.afp.com/doc.afp.com.32CZ79X | other:afp | 2026-09-08 | Machines à voter 2022: périmètre | L’AFP rapporte qu’en 2022 seules 61 communes françaises utilisaient des machines à voter, pour environ 1,3 million d’électeurs. | -
FCT-021 | FACT | ✧ | https://factuel.afp.com/doc.afp.com.32962GJ | other:afp | 2026-09-08 | Faux recomptage RN: aucun recours | Après le second tour présidentiel 2022, des publications ont affirmé que le RN demandait un recomptage; le parti a indiqué reconnaître totalement les résultats et n’avoir engagé aucune telle démarche. | -
FCT-022 | FACT | ✧ | https://factuel.afp.com/doc.afp.com.32962GJ | other:afp | 2026-09-08 | Présidentielle 2022: irrégularités bornées | L’AFP rapporte que le Conseil constitutionnel a annulé 20 594 votes sur 35 096 478 suffrages exprimés, soit environ 0,06 %, pour diverses irrégularités de bureaux de vote. | -
FCT-023 | FACT | ✧ | https://factuel.afp.com/doc.afp.com.32962GJ | other:afp | 2026-09-08 | Accusations avant scrutin: Dominion | L’AFP documente des soupçons de fraude diffusés avant le scrutin, notamment autour de Dominion, alors que cette société n’était pas mandatée pour l’élection présidentielle française. | -
FCT-024 | FACT | ✧ | https://www.lemonde.fr/les-decodeurs/article/2022/04/25/election-presidentielle-2022-une-video-de-france-2-montre-t-elle-une-fraude-electorale-dans-le-decompte-des-voix_6123625_4355770.html | other:lemonde | 2026-09-08 | France 2: affichage erroné 14,4 millions | France 2 a brièvement affiché environ 14,4 millions de voix pour Marine Le Pen; France Télévisions a reconnu une erreur informatique de traitement des chiffres, et non une modification du décompte électoral. | -
FCT-025 | FACT | ✧ | https://www.lemonde.fr/les-decodeurs/article/2022/04/25/election-presidentielle-2022-une-video-de-france-2-montre-t-elle-une-fraude-electorale-dans-le-decompte-des-voix_6123625_4355770.html | other:lemonde | 2026-09-08 | France 2: archives ministère incompatibles avec rumeur | Les archives du site du ministère de l’Intérieur consultées par Le Monde n’affichaient pas les 14 millions de voix attribués à Marine Le Pen dans le visuel erroné de France 2. | -
FCT-026 | FACT | ✧ | https://www.berlin.de/gerichte/sonstige-gerichte/verfassungsgerichtshof/pressemitteilungen/2022/pressemitteilung.1265423.php | D | 2026-09-08 | Berlin 2021: erreurs systémiques de préparation | La Cour constitutionnelle de Berlin a retenu de graves erreurs de préparation ayant provoqué de nombreuses autres erreurs le jour du scrutin et a déclaré invalides les élections au parlement du Land et aux assemblées d’arrondissement. | -
FCT-027 | FACT | ✧ | https://www.berlin.de/gerichte/sonstige-gerichte/verfassungsgerichtshof/pressemitteilungen/2022/pressemitteilung.1265423.php | D | 2026-09-08 | Berlin 2021: ampleur mandats | Le communiqué indique que les erreurs pertinentes pour les mandats affectaient les secondes voix et au moins 19 sièges supplémentaires, soit 88 des 147 sièges selon l’analyse de la cour. | -
FCT-028 | FACT | ✧ | https://www.bundesverfassungsgericht.de/SharedDocs/Pressemitteilungen/EN/2023/bvg23-119.html | D | 2026-09-08 | Berlin Bundestag: répétition partielle | La Cour constitutionnelle fédérale a ordonné une répétition de l’élection fédérale de 2021 dans un ensemble de districts berlinois, le titre du communiqué synthétisant un périmètre de 455 des 2 256 bureaux de vote. | -
FCT-029 | FACT | ✧ | https://www.justice.gouv.fr/documentation/etudes-et-statistiques/condamnations | E | 2026-09-08 | Justice: données par nature d’infraction | Le ministère de la Justice indique que les données du Casier judiciaire national permettent de décliner les condamnations par nature d’infraction et publie des séries et tableurs sur longue période. | -
FCT-030 | FACT | ✧ | https://www.justice.gouv.fr/documentation/etudes-et-statistiques/condamnations | E | 2026-09-08 | Justice: séries longues disponibles | La page met à disposition des statistiques sur les condamnations de 1990 à 2023, dont un fichier selon l’infraction principale; le corpus courant n’en extrait pas un dénominateur spécifique aux fraudes électorales. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-011
FCT-002 | SRC-011
FCT-003 | SRC-011
FCT-004 | SRC-001
FCT-005 | SRC-001
FCT-006 | SRC-001
FCT-007 | SRC-001
FCT-008 | SRC-001
FCT-009 | SRC-001
FCT-010 | SRC-002
FCT-011 | SRC-002
FCT-012 | SRC-002
FCT-013 | SRC-003
FCT-014 | SRC-003
FCT-015 | SRC-004
FCT-016 | SRC-004
FCT-017 | SRC-004
FCT-018 | SRC-005
FCT-019 | SRC-005
FCT-020 | SRC-005
FCT-021 | SRC-006
FCT-022 | SRC-006
FCT-023 | SRC-006
FCT-024 | SRC-007
FCT-025 | SRC-007
FCT-026 | SRC-008
FCT-027 | SRC-008
FCT-028 | SRC-009
FCT-029 | SRC-010
FCT-030 | SRC-010

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
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:11:CAU-001 | NEXT_ACTION:13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-08T04:09:30.009256+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-029","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-030","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":30,"eligible":30,"failure":0,"success":0}}

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
