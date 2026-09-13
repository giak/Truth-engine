ENGINE:2.10.6 | BUNDLE_REVISION:R2A.2 | STATE:FINAL | RUN_ID:20260905-2245-viginum-doctrine-impact | PARENT_RUN_ID:NONE | AS_OF:2026-09-05
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/inv071/te/truth-engine-v2_2.10.6-RC_R2A2P1_CANONICAL/investigations/2026-09/2026-09-05_viginum-doctrine-impact/2026-09-05_22-45_viginum-doctrine-impact_INPUT.md | SUBJECT_SLUG:viginum-doctrine-impact | SUBJECT_FP:sha256:e91830cc31003fba622774b80c01b9f33055acf30f6632c7f249a758509d704c | INPUT_SHA256:sha256:b9ee194eeb7d6406a81555d8b1c974d82d5abf3dce3312caf621d9fab269c708
COMPLEXITY:13→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['VIGINUM', 'SGDSN', 'CES VIGINUM', 'CNIL', 'Arcom', 'RCPE', 'independent electoral information commission', 'online platforms'], 'domains': ['legal authority', 'OSINT/data collection', 'attribution', 'impact assessment', 'electoral response', 'oversight/accountability'], 'exclusions': ['generic disinformation debate not tied to VIGINUM', 'claims about domestic speech absent foreign-interference bridge', 'effect claims without exposure/outcome evidence'], 'geo': 'France', 'lead_question': 'N/A(NO_INPUT_LEAD)', 'limits': ['publicly accessible evidence only', 'MnemoLite unavailable', 'actual opinion/vote effects require causal evidence beyond visibility/risk metrics'], 'object_question': 'Que fait réellement VIGINUM depuis sa création : autorités, critères, méthodes, données, attribution, communication, mesure d’impact, contrôles et effets observés ; et que ses publications ne permettent-elles pas de conclure ?', 'period': '2021-2026'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/NETWORK.md,clusters/ICEBERG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-071 — VIGINUM : doctrine, critères, données, attribution, impact et accountability

## 1. Résumé exécutif

VIGINUM est un **service technique et opérationnel de l’État**, rattaché au SGDSN, dont le mandat public porte sur les ingérences numériques étrangères. Son cadre n’est pas celui d’un fact-checking général des opinions : la qualification d’une INE combine une dimension de contenu trompeur, un comportement artificiel ou automatisé, massif et délibéré, l’implication directe ou indirecte d’un acteur étranger, et une finalité susceptible de porter atteinte aux intérêts fondamentaux de la Nation (FCT-001, FCT-003).

Cette frontière juridique n’empêche pas une **extension matérielle réelle** du dispositif. Le décret de février 2026 ajoute la documentation de la menace, élargit les surfaces observables aux moteurs de recherche et interfaces en ligne, ouvre une mission de R&D sur outils, algorithmes et modèles, et renforce la sensibilisation du public et l’éducation aux médias (FCT-002). Le traitement automatisé de données publiques est donc plus large qu’en 2021 ; la CNIL a explicitement relevé les risques liés à la collecte à grande échelle, demandé des garanties supplémentaires pour la R&D et insisté sur les moyens nécessaires au contrôle du CES (FCT-005, FCT-006).

La méthode publique d’attribution est plus graduée que ne le suggèrent les récits binaires. Depuis 2025, VIGINUM formalise des « modes opératoires informationnels » à partir d’indicateurs techniques et comportementaux, avec la possibilité de caractériser un ensemble cohérent sans connaître encore l’identité, l’origine, les intentions ou les moyens de son opérateur (FCT-007). L’enquête Rokh Solis illustre cette gradation : des marqueurs d’extranéité impliquant des acteurs israéliens et une entreprise d’influence, Blackcore, sont documentés ; la visibilité du dispositif est jugée très faible ; et l’identité/origine des commanditaires reste non établie (FCT-015, FCT-016).

Le point causal principal concerne la mesure d’impact. VIGINUM ne se contente plus de simples métriques brutes : son outil VIGISCORE estime un **risque d’impact** à partir d’éléments techniques, de propagation et de contexte (FCT-012). Mais le rapport municipal 2026 précise explicitement que cette estimation ne doit pas être confondue avec les effets réels sur les opinions ou intentions de vote et que l’impact sur la sincérité du scrutin relève du juge électoral (FCT-013). Il existe donc bien une fonction d’évaluation du risque et des résultats opérationnels, mais pas une mesure causale publique de I5-I7.

Des effets administratifs/opérationnels sont en revanche observables. Pendant les municipales de 2026, VIGINUM et les membres du RCPE ont documenté quatre INE ; les informations ont alimenté notification des acteurs, communication publique et coopération avec les plateformes. Près de 200 pages, comptes et sites inauthentiques ont été rendus inaccessibles dans le cadre de ces échanges (FCT-011, FCT-014). Ce fait ne permet pas d’attribuer à VIGINUM seul la totalité de la décision ou de l’effet, les plateformes restant décisionnaires de leurs mesures.

L’accountability n’est ni absente ni équivalente à une indépendance organique complète. Le CES suit l’activité et les collectes mais demeure placé auprès du SGDSN ; il demande lui-même proportionnalité, neutralité électorale et transparence (FCT-018). La CNIL fournit un contrôle externe spécifique sur les données (FCT-005, FCT-006), le Parlement audite moyens et doctrine (FCT-010, FCT-020), et depuis juillet 2026 une commission indépendante composée de membres issus du Conseil d’État, de la Cour de cassation et de la Cour des comptes peut informer candidats et public et saisir les autorités compétentes en période électorale (FCT-019).

## 2. Ce que VIGINUM fait réellement

La chaîne opérationnelle soutenue par les sources publiques peut être résumée ainsi :

`surveillance de sources ouvertes -> détection d’indices techniques/comportementaux -> caractérisation d’une opération -> attribution graduée -> appréciation de visibilité/risque -> transmission/coordination -> réponse par les acteurs compétents`.

Les réponses ne relèvent pas toutes de VIGINUM lui-même. Selon les cas, le SGDSN coordonne, les autorités électorales ou l’Arcom utilisent les informations, les plateformes modèrent selon leurs règles, et l’autorité judiciaire peut être saisie. Confondre cette architecture avec une chaîne de commandement unique serait une erreur de niveau.

La collecte repose sur des données accessibles publiquement. Le cadre 2026 permet davantage d’automatisation et de surfaces de collecte que le cadre initial. Le site institutionnel indique une durée de conservation maximale d’un an pour les données concernées et l’interdiction de reconnaissance faciale ou vocale (FCT-004). Cela borne certaines techniques mais ne supprime pas le risque de masse : la CNIL insiste précisément sur la sensibilité du scraping en raison du volume, du nombre de personnes concernées et des usages R&D (FCT-005, FCT-006).

## 3. Doctrine : technique, comportement, narratif

Le concept de MOI apporte un discriminant important. VIGINUM dit s’écarter d’une approche d’abord centrée sur les narratifs pour privilégier l’infrastructure, les comportements et les marqueurs techniques (FCT-007). Cette distinction doit être prise au sérieux : elle affaiblit la thèse selon laquelle une divergence politique ou une affirmation contestable suffirait, seule, à produire une qualification d’ingérence.

Elle ne la rend toutefois pas totalement hors sujet. Le cadre légal comporte aussi un critère de contenu et une finalité d’atteinte. Le jugement final reste donc hybride : technique et comportemental, mais appliqué à des communications et à leur contexte. Le bon test n’est pas « VIGINUM regarde-t-il les narratifs ? », mais « quel élément de la qualification repose sur le contenu, quel élément sur la conduite inauthentique, quel élément sur l’extranéité, et quel degré de preuve soutient chacun ? ».

Cette séparation est particulièrement utile pour l’attribution. Un MOI peut être stable et traçable alors que son commanditaire demeure inconnu. La méthode permet donc de ne pas forcer la chaîne `infrastructure -> opérateur -> client -> État` lorsque seuls les premiers maillons sont documentés.

## 4. Attribution : ce qui est établi et ce qui ne l’est pas

Rokh Solis est le cas test le plus discriminant pour le corpus. VIGINUM affirme que l’opération réunit les critères d’une INE et identifie des marqueurs d’extranéité impliquant des acteurs israéliens ainsi qu’un rapprochement technique avec Blackcore (FCT-015). Le rapport municipal ajoute qu’aucun élément ne permet à ce stade d’établir l’identité et l’origine des commanditaires (FCT-016).

Deux conséquences suivent.

Premièrement, le corpus doit abandonner la formule absolue selon laquelle VIGINUM n’attribuerait jamais de dispositif lié à des acteurs d’un pays allié. Cette formulation est désormais factuellement dépassée. VIGINUM a rendu public un cas impliquant des marqueurs israéliens et une entreprise israélienne d’influence.

Deuxièmement, l’inverse serait tout aussi faux : ce dossier n’établit pas une opération de l’État israélien. Le passage d’acteurs/infrastructures localisés en Israël à un commanditaire étatique est précisément le maillon que VIGINUM laisse ouvert. `FOREIGN_ACTOR != STATE_TASKING` et `TECHNICAL_LINK != COMMAND_SPONSOR`.

Cette gradation est cohérente avec le MOI : la caractérisation technique peut précéder ou rester distincte d’une attribution politique complète.

## 5. Mesurer l’impact : correction du corpus

Le corpus antérieur soutenait que VIGINUM ne disposait pas réellement d’une fonction de mesure des résultats. Cette affirmation doit être **rétrécie**.

Dès novembre 2024, le chef de VIGINUM explique au Sénat que le service préfère parler de « risque d’impact » et cherche des liens avec des changements de comportement dans la vie réelle (FCT-008). En 2026, cette doctrine est concrétisée par VIGISCORE : l’outil croise caractéristiques techniques, dynamique de propagation cross-plateformes et cross-communautés, nouveauté, contexte et seuils de viralité afin d’estimer rapidement le risque d’impact (FCT-012).

Il serait donc faux d’écrire « VIGINUM ne mesure rien ». Le service mesure ou apprécie au moins des dimensions de visibilité, propagation, criticité et risque, et il observe des résultats opérationnels.

Mais il serait tout aussi faux de présenter VIGISCORE comme une mesure d’efficacité persuasionnelle. Le rapport 2026 pose lui-même la limite : l’évaluation de visibilité et de risque d’impact « ne peut être confondue » avec les effets réels sur les opinions et intentions de vote ; la sincérité du scrutin appartient au juge de l’élection (FCT-013).

La formulation robuste devient donc : **VIGINUM dispose d’une méthodologie publique d’estimation du risque d’impact et de suivi d’effets opérationnels, mais ses publications ne démontrent pas l’effet causal d’une INE sur la persuasion, le comportement électoral ou le résultat contrefactuel d’un scrutin.**

## 6. Résultats opérationnels et causalité

Le rapport municipal documente une conséquence tangible : près de 200 pages, comptes et sites inauthentiques rendus inaccessibles dans le cadre de la coopération avec les acteurs du numérique (FCT-014). Cette observation monte plus haut que la seule « détection ». Elle établit une chaîne institutionnelle de réponse.

Elle ne permet toutefois pas de conclure que VIGINUM a, seul, causé ces retraits. Le mécanisme observé est coopératif : VIGINUM partage des éléments techniques, les plateformes investiguent et appliquent leurs propres règles, tandis que d’autres acteurs comme l’Arcom sont impliqués. La causalité raisonnable est donc **contributive**, non exclusive.

Le même principe vaut pour les affirmations selon lesquelles la communication publique aurait « arrêté » certaines opérations. Une cessation après exposition est un signal compatible avec un effet de la publicité, mais elle peut aussi coïncider avec une faible traction initiale, une action de plateforme, un changement de tactique ou une fin planifiée. Sans design comparatif, l’attribution causale reste bornée.

À l’échelle de l’opinion et du vote, la preuve est encore plus faible. VIGISCORE estime un risque ; les effets I5/I6 électoraux restent non isolés ; I7 n’est pas établi.

## 7. Accountability et contrôles

Le CES est une vraie couche de contrôle : il est informé des collectes, reçoit les analyses et formule des recommandations. Son avis 2025 demande explicitement la proportionnalité des collectes, la formation éthique des agents OSINT, des processus de qualification clairement définis, une stricte neutralité en période électorale et une transparence rigoureuse envers le public (FCT-018).

Il faut toutefois qualifier son indépendance institutionnelle : il est placé auprès du SGDSN. Il constitue un mécanisme de supervision éthique/scientifique interne-adjacent, pas une autorité administrative indépendante.

La CNIL est une couche distincte. Son avis sur la réforme 2026 reconnaît la finalité légitime du traitement mais souligne que le scraping à grande échelle crée des risques spécifiques et demande des garanties sur la réutilisation R&D/IA, la minimisation et l’effectivité du contrôle (FCT-005, FCT-006). Ce point est important parce qu’il évite l’erreur « cadre juridique = absence de risque ».

Le Parlement ajoute une supervision budgétaire et doctrinale. En 2024, le Sénat estime le budget global autour de 7,3 M€, chiffre une opération sophistiquée à 120–140 k€ à partir des réponses du service et juge les moyens alors insuffisants par rapport aux ambitions (FCT-010, FCT-020). Ce sont des données de capacité et d’accountability, pas une preuve de performance.

Enfin, le décret du 22 juillet 2026 ajoute une commission indépendante d’information du public en période électorale. Elle peut recevoir des signalements, informer candidats/partis et public, transmettre aux autorités compétentes et exerce ses fonctions « en toute indépendance » ; sa composition juridictionnelle et financière la sépare du service opérationnel (FCT-019). Cette réforme modifie la carte de gouvernance à conserver avec un `AS_OF` visible.

## 8. Pouvoirs, ressources, limites

Les ressources de VIGINUM sont réelles mais modestes comparées à de grandes agences. Le Sénat estimait le budget global 2024 à environ 7,3 M€ et rapportait qu’une seule opération sophistiquée pouvait mobiliser 120–140 k€ hors frais généraux (FCT-010). Le même rapport indiquait une capacité de cinq opérations permanentes simultanées et un objectif de montée en effectifs (FCT-020).

Ces données soutiennent deux lectures rivales qui doivent rester ouvertes. Pour les défenseurs du dispositif, elles montrent un service encore petit face à une menace transnationale industrialisée. Pour les critiques, l’extension juridique et algorithmique mérite précisément une supervision proportionnée, quelle que soit la taille actuelle du budget. Les chiffres seuls ne tranchent pas ce débat normatif.

## 9. Carte probatoire I0–I7

**I0 — identité / relation : VERIFIED.** Mandat, rattachement SGDSN, CES, CNIL, RCPE et nouvelle commission sont documentés.

**I1 — ressources / capacité / accès : VERIFIED.** Budget, personnel/capacité historique, accès à des données publiques et automatisation sont établis.

**I2 — action documentée : VERIFIED.** Détection, caractérisation, rapports, alertes, partage d’indicateurs, sensibilisation et coopération sont observables.

**I3 — coordination / tasking / contrôle : SUPPORTED ou VERIFIED selon le maillon précis.** La coordination institutionnelle française est explicite. Pour les opérations étrangères, la relation opérateur/infrastructure peut être solide tandis que le commanditaire final reste inconnu, comme Rokh Solis.

**I4 — exposition / reach : PARTIAL.** Les métriques de visibilité et propagation sont utilisées, mais leur fiabilité dépend des plateformes et des données disponibles.

**I5 — réception / persuasion : UNRESOLVED.** Aucun dispositif public consulté n’isole la persuasion causée par les campagnes étudiées.

**I6 — changement comportemental / institutionnel : MIXED.** Des réponses institutionnelles et de plateforme sont vérifiées ; un changement de comportement électoral attribuable à une INE ou à VIGINUM n’est pas établi.

**I7 — résultat contrefactuel : NOT_ESTABLISHED.** Aucun élément ne permet de dire quel résultat électoral aurait eu lieu sans une opération ou sans l’intervention de VIGINUM.

## 10. Contre-thèses

### A. « VIGINUM est un ministère de la Vérité »

Cette formule est trop forte comme description factuelle du mandat. Le droit et la méthodologie exigent davantage qu’un désaccord narratif : comportement coordonné/inauthentique, acteur étranger et finalité d’atteinte font partie du dispositif. VIGINUM affirme ne pas faire de fact-checking général (FCT-003, FCT-007).

Le risque de mission creep n’est toutefois pas imaginaire. Les missions, surfaces de collecte et usages R&D ont été élargis en 2026 et la CNIL demande des garanties supplémentaires (FCT-002, FCT-005, FCT-006). La critique robuste porte donc sur les **frontières, procédures, données et voies de recours**, pas sur une assimilation non démontrée à une police générale de l’opinion.

### B. « VIGINUM est une simple vigie sans pouvoir »

Cette formule est également fausse. Ses productions alimentent des décisions et des réponses : alertes, communication publique, relations avec plateformes, saisines possibles, information des acteurs ciblés. Les retraits de près de 200 actifs numériques en 2026 montrent une capacité de conséquence concrète (FCT-014).

### C. « Les opérations détectées changent les élections »

Non établi. Le propre rapport de VIGINUM sépare risque d’impact et effets réels sur opinions/vote (FCT-013). La prudence affichée au Sénat en 2024 est cohérente avec cette limite (FCT-008).

### D. « VIGINUM ne regarde que les adversaires géopolitiques »

La thèse absolue ne résiste plus à Rokh Solis. Le service a publié des éléments liés à des acteurs israéliens et à Blackcore (FCT-015). En revanche, ce cas ne permet pas d’attribuer l’opération à l’État israélien : le commanditaire reste non établi (FCT-016).

## 11. Corrections à appliquer au corpus

1. Remplacer `VIGISCORE = aucune mesure d’impact` par : `VIGISCORE = estimation du risque d’impact ; ne mesure pas les effets réels sur opinions ou intentions de vote`.
2. Remplacer `VIGINUM n’attribue jamais des opérations liées à des acteurs d’un pays allié` par une formulation datée : en 2026, Rokh Solis documente des marqueurs impliquant des acteurs israéliens/Blackcore, sans commanditaire final établi.
3. Conserver la critique sur l’écart entre **mesure causale** et **capacité d’action**, mais ne pas effacer les métriques de risque, les évaluations de visibilité et les résultats opérationnels.
4. Distinguer CES, CNIL, Parlement et commission électorale indépendante : ils n’ont ni le même statut ni le même pouvoir.
5. Toute future affirmation sur une sanction ou mesure coercitive déclenchée « par VIGINUM » doit retracer le maillon institutionnel exact : VIGINUM informe/caractérise, d’autres autorités peuvent décider.

## 12. Conclusion forensique

VIGINUM est mieux décrit comme une **infrastructure étatique d’OSINT et de sécurité informationnelle, juridiquement bornée par l’extranéité mais en expansion fonctionnelle**, que comme une simple cellule d’observation ou comme une police générale du vrai.

La preuve publique est forte pour son mandat, ses outils, ses capacités et ses circuits de réponse. Elle est moyenne à forte pour certaines attributions techniques, à condition de respecter les degrés d’incertitude. Elle est faible pour les effets de persuasion et insuffisante pour les résultats électoraux contrefactuels.

Le point de vigilance démocratique le plus solide n’est donc pas « VIGINUM prouve que les opérations étrangères changent les votes » : il ne le prouve pas. C’est l’écart entre une capacité institutionnelle croissante — collecte automatisée, R&D, signalement, exposition et coordination — et une capacité publique encore limitée à mesurer causalement les effets ultimes. Cet écart justifie précisément des frontières juridiques visibles, une traçabilité des qualifications et des contrôles réellement effectifs.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:4|CLM:9|AXS:8|CAU:5|CTRL:4|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempts":["QRY-001","QRY-002"],"claim":"VIGINUM has no meaningful function for measuring results/impact; public threat measurement is far below precision of powers.","outcome":"NARROWED: actual opinion/vote effects remain unmeasured, but VIGISCORE is an explicit risk-impact methodology and operational mitigation outputs are measured.","ref":"A004:210182384.lingerence-sans-mesure","sources":["SRC-009","SRC-007"],"status":"SATURATED"}
LED-002 | {"attempts":["QRY-001"],"claim":"A public narrative can be transformed into an INE qualification and then coercive consequences.","outcome":"BOUNDED: VIGINUM criteria and administrative/judicial information channels are documented; any individual coercive chain requires case-specific evidence and cannot be inferred from the general architecture.","ref":"A006:209222653.du-narratif-a-lingerence-le-seuil","sources":["SRC-001","SRC-013"],"status":"SATURATED"}
LED-003 | {"attempts":["QRY-002"],"claim":"VIGINUM is part of a broader public communication/information-governance apparatus.","outcome":"CONTEXT ONLY: coordination and public communication functions are real; this run does not establish a general domestic narrative-control mandate.","ref":"A013:203962785.un-geyser-de-6-metres-a-clichy-autopsie","sources":["SRC-009"],"status":"SATURATED"}
LED-004 | {"attempts":["QRY-004"],"claim":"Direct VIGINUM-media-expert causal links form a coordinated influence machine.","outcome":"NOT_ESTABLISHED: institutional cooperation and information sharing exist, but the named-person causal/command claims are not supported by the VIGINUM evidence inspected.","ref":"A072:186844276.tristan-mendes-france-la-machine","sources":["SRC-009","SRC-012"],"status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"VIGINUM has a legally bounded foreign-interference mandate, not a generic mandate to arbitrate all truth online.","status":"SUPPORTED","support":["FCT-001","FCT-003"]}
CLM-002 | {"claim":"The 2026 reform materially expanded VIGINUM data surfaces, documentation, R&D and public-information roles.","status":"SUPPORTED","support":["FCT-002","FCT-005","FCT-006"]}
CLM-003 | {"claim":"VIGINUM methodology can characterize coherent technical operations before ultimate actor/sponsor identity is known.","status":"SUPPORTED","support":["FCT-007","FCT-016"]}
CLM-004 | {"claim":"Public attribution is graduated; operator/infrastructure evidence does not automatically establish the final sponsor.","status":"SUPPORTED","support":["FCT-015","FCT-016"]}
CLM-005 | {"claim":"VIGISCORE measures estimated risk of impact, not actual persuasion or change in voting intentions.","status":"SUPPORTED","support":["FCT-012","FCT-013"]}
CLM-006 | {"claim":"VIGINUM and partner institutions can produce observable operational consequences such as notifications, public exposure and platform removals.","status":"SUPPORTED","support":["FCT-014","FCT-019"]}
CLM-007 | {"claim":"Oversight exists but is layered: CES is attached to SGDSN, CNIL supplies independent data-protection scrutiny, Parliament audits, and a separate independent electoral commission was added in July 2026.","status":"SUPPORTED","support":["FCT-005","FCT-006","FCT-018","FCT-019"]}
CLM-008 | {"claim":"The corpus claim that VIGINUM attributes only Russia/China and never operations linked to allied-country actors is false as an absolute.","status":"CONTRADICTED","support":["FCT-015","FCT-016"]}
CLM-009 | {"claim":"The corpus claim that VIGINUM has no impact-measurement function is too strong; the narrower claim that actual opinion/vote causal effects are not measured by VIGISCORE survives.","status":"PARTIAL","support":["FCT-008","FCT-012","FCT-013","FCT-014"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempts":[],"name":"Legal authority and evolution","result":"Authority, statutory criteria and 2026 expansion","status":"SATURATED"}
AXS-002 | {"attempts":[],"name":"Data collection and privacy","result":"Automated public-data collection, retention and safeguards","status":"SATURATED"}
AXS-003 | {"attempts":[],"name":"Detection methodology","result":"MOI, technical/behavioral indicators and narrative boundary","status":"SATURATED"}
AXS-004 | {"attempts":[],"name":"Attribution","result":"Foreign actor, operator, infrastructure and sponsor confidence levels","status":"SATURATED"}
AXS-005 | {"attempts":[],"name":"Impact measurement","result":"Visibility, risk-of-impact and actual opinion/vote effects","status":"SATURATED"}
AXS-006 | {"attempts":[],"name":"Operational consequences","result":"Notifications, public exposure, platform moderation and judicial channels","status":"SATURATED"}
AXS-007 | {"attempts":[],"name":"Oversight/accountability","result":"CES, CNIL, Parliament, election bodies and 2026 independent commission","status":"SATURATED"}
AXS-008 | {"attempts":[],"name":"Corpus contradiction tests","result":"No-measurement and allies-only attribution claims","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"MECHANISM","limit":"Does not establish correctness of every attribution or downstream electoral effect.","mechanism":"public-source detection -> technical characterization -> SGDSN/RCPE decision support","status":"SUPPORTED","support":["FCT-001","FCT-007","FCT-011","FCT-012"]}
CAU-002 | {"causal_right":"CONTRIBUTORY","limit":"Joint process with platforms; VIGINUM-alone marginal effect is not isolated.","mechanism":"technical indicator sharing -> platform identification/moderation -> assets made inaccessible","status":"SUPPORTED","support":["FCT-014"]}
CAU-003 | {"gap":"Temporal association and reported mitigation exist, but no design isolates the contribution of disclosure from platform actions, organic failure or other events.","gap_type":"MITIGATION_CAUSATION","mechanism":"public exposure/notifications -> reduced campaign visibility or operator stopping","status":"UNRESOLVED","support":["FCT-014"]}
CAU-004 | {"gap":"VIGISCORE estimates risk; actual opinion/voting effects are explicitly outside the measurement reported.","gap_type":"PERSUASION_CAUSATION","mechanism":"foreign influence exposure -> opinion/voting change","status":"UNRESOLVED","support":["FCT-012","FCT-013"]}
CAU-005 | {"gap":"No causal design or counterfactual evidence isolates VIGINUM intervention on election outcomes.","gap_type":"ELECTORAL_COUNTERFACTUAL","mechanism":"VIGINUM intervention -> electoral result/counterfactual winner","status":"UNRESOLVED","support":["FCT-013"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"CES follows VIGINUM activity and data collections","limit":"CES is placed with SGDSN; it is oversight, not an independent regulator.","status":"PASS","support":["FCT-018"]}
CTRL-002 | {"control":"CNIL data-protection review","status":"PASS","support":["FCT-005","FCT-006"]}
CTRL-003 | {"control":"Independent election information commission from July 2026","status":"PASS","support":["FCT-019"]}
CTRL-004 | {"control":"Parliamentary budget/mission scrutiny","status":"PASS","support":["FCT-010","FCT-020"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:10|FETCH:14|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | subject-fp lookup | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-004 | SYS | PASS | verify.py | pre | PRE_GATE_VERIFY
SYS-005 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | investigation-summary | MNEMO_S
SYS-006 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
SYS-007 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | snapshot:v1 | SNAPSHOT_MEMORY_WRITE
QRY-001 | WEB | FOUND | - | - | site:legifrance.gouv.fr VIGINUM décret 2026-70 missions données
QRY-002 | WEB | FOUND | - | - | site:sgdsn.gouv.fr VIGINUM élections municipales 2026 VIGISCORE
QRY-003 | WEB | FOUND | - | - | site:sgdsn.gouv.fr VIGINUM Rokh Solis Blackcore
QRY-004 | WEB | FOUND | - | - | site:sgdsn.gouv.fr VIGINUM mode opératoire informationnel MOI
QRY-005 | WEB | FOUND | - | - | site:senat.fr VIGINUM impact risque impact audition 2024
QRY-006 | WEB | FOUND | - | - | site:senat.fr VIGINUM budget 7.3 millions 120000 140000
QRY-007 | WEB | FOUND | - | - | site:sgdsn.gouv.fr comité éthique scientifique VIGINUM avis 2025
QRY-008 | WEB | FOUND | - | - | site:legifrance.gouv.fr CNIL VIGINUM 2025-108 scraping données
QRY-009 | WEB | FOUND | - | - | site:legifrance.gouv.fr commission indépendante information public ingérences élections 2026
QRY-010 | WEB | FOUND | - | - | site:sgdsn.gouv.fr VIGINUM guerre Ukraine efficacité limitée RRN
QRY-011 | FETCH | FOUND | SRC-001 | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000054460802 | FETCH Décret 2021-922 art. 3, version 24 juillet 2026
QRY-012 | FETCH | FOUND | SRC-002 | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053458618 | FETCH Décret 2026-70 du 11 février 2026
QRY-013 | FETCH | FOUND | SRC-003 | https://www.sgdsn.gouv.fr/viginum/comprendre-viginum/les-missions-de-viginum | FETCH Les missions de VIGINUM
QRY-014 | FETCH | FOUND | SRC-004 | https://www.sgdsn.gouv.fr/viginum/comprendre-viginum/viginum-un-cadre-juridique-precis-et-transparent | FETCH Cadre juridique précis et transparent
QRY-015 | FETCH | FOUND | SRC-005 | https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000053461680 | FETCH CNIL délibération 2025-108
QRY-016 | FETCH | FOUND | SRC-006 | https://www.sgdsn.gouv.fr/publications/definitions-et-objectifs-du-concept-de-mode-operatoire-informationnel-moi | FETCH Méthodologie Mode opératoire informationnel
QRY-017 | FETCH | FOUND | SRC-007 | https://www.senat.fr/compte-rendu-commissions/20241104/etrang.html | FETCH Audition SGDSN VIGINUM PLF 2025
QRY-018 | FETCH | FOUND | SRC-008 | https://www.senat.fr/rap/r23-739-1/r23-739-110.html | FETCH Rapport Sénat ingérences - budget VIGINUM
QRY-019 | FETCH | FOUND | SRC-009 | https://www.sgdsn.gouv.fr/files/files/viginum/Publications/20260611_SGDSN_VIGINUM_Rapport-public_Elections-municipales.pdf | FETCH Rapport élections municipales 2026
QRY-020 | FETCH | FOUND | SRC-010 | https://www.sgdsn.gouv.fr/viginum/publications/rokh-solis-analyse-dun-mode-operatoire-informationnel-ayant-cible-les | FETCH Rokh Solis élections municipales 2026
QRY-021 | FETCH | FOUND | SRC-011 | https://www.sgdsn.gouv.fr/viginum/publications/guerre-en-ukraine-trois-annees-doperations-informationnelles-russes | FETCH Guerre en Ukraine : trois années opérations russes
QRY-022 | FETCH | FOUND | SRC-012 | https://www.sgdsn.gouv.fr/files/files/Publications/2025%2012%2022%20-%20AVIS%20DU%20COMITE%CC%81%20E%CC%81THIQUE%20ET%20SCIENTIFIQUE%20DE%20VIGINUM.pdf | FETCH Avis CES VIGINUM décembre 2025
QRY-023 | FETCH | FOUND | SRC-013 | https://www.legifrance.gouv.fr/eli/decret/2026/7/22/2026-646/jo/texte | FETCH Décret 2026-646 commission indépendante élections
QRY-024 | FETCH | FOUND | SRC-014 | https://www.senat.fr/rap/r23-739-1/r23-739-119.html | FETCH Rapport Sénat moyens VIGINUM 58/95 ETP

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:other:legifrance | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000054460802
SRC-002 | ◈ | fam:other:legifrance | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053458618
SRC-003 | ◈ | fam:other:viginum | https://www.sgdsn.gouv.fr/viginum/comprendre-viginum/les-missions-de-viginum
SRC-004 | ◈ | fam:other:viginum | https://www.sgdsn.gouv.fr/viginum/comprendre-viginum/viginum-un-cadre-juridique-precis-et-transparent
SRC-005 | ◉ | fam:other:cnil | https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000053461680
SRC-006 | ◈ | fam:other:viginum | https://www.sgdsn.gouv.fr/publications/definitions-et-objectifs-du-concept-de-mode-operatoire-informationnel-moi
SRC-007 | ◉ | fam:other:senat | https://www.senat.fr/compte-rendu-commissions/20241104/etrang.html
SRC-008 | ◉ | fam:other:senat | https://www.senat.fr/rap/r23-739-1/r23-739-110.html
SRC-009 | ◈ | fam:other:viginum | https://www.sgdsn.gouv.fr/files/files/viginum/Publications/20260611_SGDSN_VIGINUM_Rapport-public_Elections-municipales.pdf
SRC-010 | ◈ | fam:other:viginum | https://www.sgdsn.gouv.fr/viginum/publications/rokh-solis-analyse-dun-mode-operatoire-informationnel-ayant-cible-les
SRC-011 | ◈ | fam:other:viginum | https://www.sgdsn.gouv.fr/viginum/publications/guerre-en-ukraine-trois-annees-doperations-informationnelles-russes
SRC-012 | ◉ | fam:other:ces-viginum | https://www.sgdsn.gouv.fr/files/files/Publications/2025%2012%2022%20-%20AVIS%20DU%20COMITE%CC%81%20E%CC%81THIQUE%20ET%20SCIENTIFIQUE%20DE%20VIGINUM.pdf
SRC-013 | ◈ | fam:other:legifrance | https://www.legifrance.gouv.fr/eli/decret/2026/7/22/2026-646/jo/texte
SRC-014 | ◉ | fam:other:senat | https://www.senat.fr/rap/r23-739-1/r23-739-119.html

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000054460802 | other:legifrance | 2026-07-24 | Mandat légal actuel | L'article 3 consolidé charge VIGINUM de détecter, caractériser et documenter les opérations d'ingérence numérique étrangère en analysant des données publiquement accessibles sur plateformes, moteurs de recherche et interfaces en ligne. | -
FCT-002 | FACT | ✧ | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053458618 | other:legifrance | 2026-02-13 | Extension des missions 2026 | Le décret 2026-70 a élargi le dispositif : documentation, accès aux moteurs/interfaces, nouvelles missions de recherche-développement et de sensibilisation/éducation aux médias, ainsi qu'un cadre de collecte refondu. | -
FCT-003 | FACT | ✧ | https://www.sgdsn.gouv.fr/viginum/comprendre-viginum/les-missions-de-viginum | other:viginum | 2026-05-15 | Périmètre opérationnel déclaré | VIGINUM se présente comme un service technique et opérationnel de l'État ; l'INE est définie par quatre critères combinant contenu, comportement, acteur étranger et finalité/atteinte, et le service dit ne pas exercer de techniques de renseignement ni de fact-checking général. | -
FCT-004 | FACT | ✧ | https://www.sgdsn.gouv.fr/viginum/comprendre-viginum/viginum-un-cadre-juridique-precis-et-transparent | other:viginum | 2026-05 | Collecte et conservation | Le cadre public indique que seules les données nécessaires sont collectées de manière automatisée selon des critères techniques, pour une conservation maximale d'un an, avec interdiction de reconnaissance faciale ou vocale. | -
FCT-005 | FACT | ✧ | https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000053461680 | other:cnil | 2025-11-06 | Alerte CNIL sur le scraping | La CNIL qualifie la collecte/scraping en ligne de traitement sensible au regard du nombre de personnes, du volume et des risques pour les droits ; elle appelle à un cadre général plus robuste pour les organismes publics recourant à ce type de collecte. | -
FCT-006 | FACT | ✧ | https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000053461680 | other:cnil | 2025-11-06 | Garanties R&D et contrôle | À propos de la réforme 2026 et de la réutilisation de données pour des outils d'IA, la CNIL demande des précisions et garanties de transparence, de minimisation et de contrôle, et souligne la nécessité de moyens suffisants pour que le CES exerce un contrôle effectif. | -
FCT-007 | FACT | ✧ | https://www.sgdsn.gouv.fr/publications/definitions-et-objectifs-du-concept-de-mode-operatoire-informationnel-moi | other:viginum | 2026-01-22 | Méthode MOI | Le concept de mode opératoire informationnel utilisé par VIGINUM est centré sur les indicateurs techniques et comportements en ligne plutôt que sur les narratifs ; il permet de décrire un ensemble cohérent sans connaître nécessairement identité, origine, intentions ou ressources de l'attaquant. | -
FCT-008 | FACT | ✧ | https://www.senat.fr/compte-rendu-commissions/20241104/etrang.html | other:senat | 2024-11 | Prudence sur la mesure d impact | Le chef de VIGINUM déclare au Sénat privilégier la notion de risque d'impact et chercher des liens avec des changements de comportement dans la vie réelle plutôt que prétendre mesurer directement l'impact causal d'une campagne. | -
FCT-009 | FACT | ✧ | https://www.senat.fr/compte-rendu-commissions/20241104/etrang.html | other:senat | 2024 | Volume de détection | VIGINUM indique au Sénat avoir identifié 230 phénomènes inauthentiques de manipulation de l'information en 2023 et avoir dépassé ce total au 1er octobre 2024 ; cinq manoeuvres ont alimenté des actions de communication stratégique du Quai d'Orsay sur l'année écoulée. | -
FCT-010 | FACT | ✧ | https://www.senat.fr/rap/r23-739-1/r23-739-110.html | other:senat | 2024 | Budget et coût opération sophistiquée | Le Sénat estime le budget global 2024 de VIGINUM à environ 7,3 M€ et rapporte une estimation VIGINUM de 120 000 à 140 000 € pour détecter et caractériser une INE sophistiquée sur trente jours, hors moyens généraux. | -
FCT-011 | FACT | ✧ | https://www.sgdsn.gouv.fr/files/files/viginum/Publications/20260611_SGDSN_VIGINUM_Rapport-public_Elections-municipales.pdf | other:viginum | 2026-06-11 | Élections municipales - opérations détectées | VIGINUM documente quatre ingérences numériques étrangères détectées et caractérisées pendant les élections municipales de mars 2026. | -
FCT-012 | FACT | ✧ | https://www.sgdsn.gouv.fr/files/files/viginum/Publications/20260611_SGDSN_VIGINUM_Rapport-public_Elections-municipales.pdf | other:viginum | 2026-06-11 | VIGISCORE | Le RCPE utilise VIGISCORE, méthodologie développée par VIGINUM, pour estimer rapidement le risque d'impact à partir d'éléments techniques, de la propagation cross-plateformes/cross-communautés, de la nouveauté et du contexte ; il ne s'agit pas d'une mesure directe de persuasion. | -
FCT-013 | FACT | ✧ | https://www.sgdsn.gouv.fr/files/files/viginum/Publications/20260611_SGDSN_VIGINUM_Rapport-public_Elections-municipales.pdf | other:viginum | 2026-06-11 | Limite opinions et vote | Le rapport municipal précise explicitement que l'évaluation de visibilité et de risque d'impact ne doit pas être confondue avec l'évaluation des effets réels sur les opinions ou intentions de vote ; l'effet sur la sincérité du scrutin relève du juge de l'élection. | -
FCT-014 | FACT | ✧ | https://www.sgdsn.gouv.fr/files/files/viginum/Publications/20260611_SGDSN_VIGINUM_Rapport-public_Elections-municipales.pdf | other:viginum | 2026-06-11 | Effet opérationnel plateformes | À la suite d'échanges techniques avec des plateformes, près de 200 pages, comptes et sites web inauthentiques ont été rendus inaccessibles rapidement pendant la période municipale ; cet effet est une conséquence opérationnelle observable, sans isoler la contribution causale de VIGINUM seul. | -
FCT-015 | FACT | ✧ | https://www.sgdsn.gouv.fr/viginum/publications/rokh-solis-analyse-dun-mode-operatoire-informationnel-ayant-cible-les | other:viginum | 2026-06-11 | Rokh Solis et Blackcore | VIGINUM conclut que Rokh Solis réunit les critères d'une INE, identifie des marqueurs d'extranéité impliquant des acteurs israéliens et notamment Blackcore, tout en constatant une très faible visibilité et en poursuivant l'enquête sur les opérateurs à l'origine du dispositif. | -
FCT-016 | FACT | ✧ | https://www.sgdsn.gouv.fr/files/files/viginum/Publications/20260611_SGDSN_VIGINUM_Rapport-public_Elections-municipales.pdf | other:viginum | 2026-06-11 | Commanditaires Rokh Solis non établis | Dans le rapport municipal, VIGINUM indique qu'aucun élément ne permet à ce stade d'établir l'identité et l'origine des commanditaires ayant pu recourir au dispositif lié à Blackcore. | -
FCT-017 | FACT | ✧ | https://www.sgdsn.gouv.fr/viginum/publications/guerre-en-ukraine-trois-annees-doperations-informationnelles-russes | other:viginum | 2025-02-24 | Efficacité limitée de campagnes russes | La synthèse VIGINUM sur trois années d'opérations russes décrit plusieurs dispositifs persistants mais juge leurs effets relativement limités dans les cas examinés, tout en relevant des épisodes viraux et une capacité à exploiter des controverses préexistantes. | -
FCT-018 | FACT | ✧ | https://www.sgdsn.gouv.fr/files/files/Publications/2025%2012%2022%20-%20AVIS%20DU%20COMITE%CC%81%20E%CC%81THIQUE%20ET%20SCIENTIFIQUE%20DE%20VIGINUM.pdf | other:ces-viginum | 2025-12 | Recommandations CES | Le CES demande notamment proportionnalité des collectes, formation éthique OSINT, processus clairement définis de qualification en période électorale, stricte neutralité de la documentation et transparence rigoureuse de l'information du public. | -
FCT-019 | FACT | ✧ | https://www.legifrance.gouv.fr/eli/decret/2026/7/22/2026-646/jo/texte | other:legifrance | 2026-07-24 | Commission électorale indépendante | Le décret 2026-646 crée une commission d'information du public qui reçoit les signalements d'ingérence, peut informer candidats/partis et public, saisir les autorités compétentes et exerce ses fonctions en toute indépendance ; elle est composée d'un membre du Conseil d'État, d'un magistrat de la Cour de cassation et d'un magistrat de la Cour des comptes. | -
FCT-020 | FACT | ✧ | https://www.senat.fr/rap/r23-739-1/r23-739-119.html | other:senat | 2024 | Capacité humaine Sénat | Le rapport sénatorial indique que VIGINUM pouvait alors mener cinq opérations permanentes simultanément, visait 58 ETP fin 2024 et affichait une ambition de 95 ETP en 2027 ; la commission jugeait les moyens non alignés sur les ambitions. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-003
FCT-004 | SRC-004
FCT-005 | SRC-005
FCT-006 | SRC-005
FCT-007 | SRC-006
FCT-008 | SRC-007
FCT-009 | SRC-007
FCT-010 | SRC-008
FCT-011 | SRC-009
FCT-012 | SRC-009
FCT-013 | SRC-009
FCT-014 | SRC-009
FCT-015 | SRC-010
FCT-016 | SRC-009
FCT-017 | SRC-011
FCT-018 | SRC-012
FCT-019 | SRC-013
FCT-020 | SRC-014

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

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-05T22:49:40.411487+00:00","fact_mem":{},"mnemo_row":"BLOCKED:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":20,"eligible":20,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:BLOCKED:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:20;attempted:0;success:0;failure:0;blocked:20} | WRITEBACK_EXECUTION_V1:[20 rows, see section]

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
