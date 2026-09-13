ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260907-1141-europe-democracy-shield | PARENT_RUN_ID:NONE | AS_OF:2026-09-07
INPUT_KIND:RUN_CARD | MISSION_MODE:DEEPEN | INPUT_REF:PATH:/mnt/data/inv044-work/te/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-07_europe-democracy-shield/2026-09-07_11-41_europe-democracy-shield_INPUT.md | SUBJECT_SLUG:europe-democracy-shield | SUBJECT_FP:sha256:8ce8f96d3b9f47ab473691eb68e5b4636964cb1a5f36fd3d69d7e69c5472273b | INPUT_SHA256:sha256:e93f3c9bdbfcf70fc104c67a3688dc676401806accac9b4ed44a1a2b09760a33
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:European Union 2018-2026, with priority to operational, financial, governance and platform interfaces relevant to France; distinguish funding, coordination, monitoring, signalling, platform action and democratic effect.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/NETWORK.md,clusters/FRAMING.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-044 — Bouclier européen de la démocratie, EDMO, EUvsDisinfo et anti-FIMI : architecture, pouvoirs et limites

## Question et règle de preuve

L'enquête ne cherche pas à déterminer si la lutte contre la désinformation est politiquement souhaitable. Elle teste un objet plus étroit : quels dispositifs composent réellement l'écosystème européen de lutte contre la désinformation et les manipulations de l'information, quels flux publics les soutiennent, qui coordonne quoi, quels liens existent avec la régulation des plateformes, quelles voies de recours sont documentées et jusqu'où la preuve permet de parler de contrôle éditorial ou de « censure ».

La chaîne de preuve retenue est : `forme juridique/mandat -> financement -> gouvernance -> monitoring/recherche/fact-checking -> signal ou évaluation de risque -> action de plateforme ou de régulateur -> recours/correction -> exposition -> comportement -> résultat démocratique contrefactuel`.

Les gardes sont strictes : `anti-FIMI != censure`, `financement != commandement`, `coordination != contrôle`, `participation != capture`, `signalement != retrait`, `fact-check != ordre étatique`, `action de plateforme != ordre de la Commission`, `budget croissant != menace fabriquée`, `réseau institutionnel != chaîne de commandement unitaire`, `action != effet démocratique`.

## 1. Le Bouclier : un cadre stratégique qui agrège plusieurs instruments

Le Bouclier européen de la démocratie existe formellement sous la forme d'une communication conjointe de la Commission et du Haut représentant, JOIN(2025) 791 final, présentée le 12 novembre 2025. Le document regroupe plusieurs lignes d'action : préparation d'un protocole d'incident et de crise lié au DSA, préparation d'un blueprint européen contre les FIMI et la désinformation, création d'un réseau européen de fact-checkers, extension du mandat d'EDMO, soutien à un cadre commun de recherche et articulation avec d'autres capacités européennes. [FCT-001, FCT-002]

Cette forme juridique est importante. La communication établit une stratégie et organise des actions, mais elle ne constitue pas à elle seule un pouvoir général et auto-exécutoire de retrait de contenus. Les mécanismes contraignants doivent être recherchés dans les actes juridiques applicables, notamment le DSA, les compétences des autorités nationales, les obligations propres aux plateformes ou d'autres régimes sectoriels. [FCT-001, FCT-016, FCT-017]

Le Bouclier doit donc être décrit comme une **architecture d'intégration** plutôt que comme une nouvelle autorité unique. Il rapproche des organismes de nature différente : institutions de l'Union, États membres, chercheurs, fact-checkers, médias, plateformes, réseaux d'alerte et structures de communication stratégique. [FCT-002, FCT-027]

## 2. Le Centre européen pour la résilience démocratique : coordination réelle, pouvoir réglementaire non démontré

Le Centre européen pour la résilience démocratique est opérationnel en 2026. La Commission le décrit comme un hub d'échange et un cadre de coopération et de coordination opérationnelles entre institutions de l'UE, États membres, pays candidats et partenaires. Ses objectifs comprennent la connaissance de la situation, la détection et l'anticipation des menaces, l'alerte précoce, le renforcement de la capacité de réponse et la résilience de la société. Son secrétariat assure la coordination opérationnelle entre les membres. [FCT-004, FCT-005]

La participation est large : Parlement européen, Commission, SEAE et États membres figurent dans la structure, avec une plateforme destinée aux acteurs indépendants de la société civile, de la recherche et de l'expertise. [FCT-006]

Cela établit un **centre de coordination**, pas une preuve de commandement éditorial. La distinction est confirmée indirectement par le Parlement européen lui-même : en juin 2026, sa commission spéciale sur le Bouclier a demandé que le Centre soit établi par un acte juridique contraignant, doté de paramètres opérationnels et d'un budget dédié. Cette recommandation indique que, du point de vue de cette commission, le Centre existant n'était pas encore l'autorité pleinement juridicisée qu'elle souhaitait. La recommandation ne crée pas elle-même ces pouvoirs. [FCT-026]

Le niveau I3 de coordination est donc soutenu pour le Centre ; il ne peut être transféré automatiquement à chaque membre ou partenaire comme preuve de tasking central.

## 3. EDMO : financement public massif mais gouvernance formellement séparée

EDMO est un nœud majeur de cette architecture. Les données de la Commission retracent plusieurs vagues de financement : environ 2,5 millions d'euros pour la plateforme centrale initiale, 4 millions lors du refinancement de 2022 et environ 2,5 millions dans le programme DIGITAL 2025. Les hubs ont reçu plusieurs enveloppes : 11 millions pour huit hubs initiaux, 8 millions pour six hubs supplémentaires, 10 millions pour refinancer les huit premiers en 2023 et environ 8,8 millions pour six hubs poursuivant leurs travaux. Avec le hub F.A.C.T., le réseau atteint 15 hubs. [FCT-007, FCT-008]

En mars 2026, la Commission a annoncé un nouveau marché de 2,5 millions d'euros pour poursuivre les activités centrales d'EDMO. La nouvelle phase étend explicitement les capacités de monitoring et d'analyse de l'écosystème informationnel, notamment autour des élections et des crises. La Commission décrit par ailleurs un réseau de plus de 100 organisations. [FCT-009, FCT-010]

Ces montants établissent une dépendance matérielle à des financements publics européens. Ils ne suffisent toutefois pas à établir une direction éditoriale par la Commission. Les principes de gouvernance publiés par EDMO stipulent que les financeurs externes, publics ou privés, ne peuvent appartenir aux organes décisionnels ni influencer priorités, méthodes ou résultats. La Commission peut être présente comme observateur pour suivre l'exécution des conventions de financement. [FCT-011]

La charte de gouvernance d'EDMO prévoit un Executive Board et un Advisory Council ; la Commission y est observatrice sans droit de vote. Une procédure de plainte permet de saisir l'Advisory Council par l'intermédiaire du secrétaire général. [FCT-012]

La conclusion probatoire doit rester symétrique : les financements sont un fait structurel important ; les règles d'indépendance sont également un fait. Les premières ne prouvent pas le commandement, les secondes ne prouvent pas l'absence de toute influence informelle. Aucune des deux catégories ne peut être supprimée de l'analyse.

## 4. Réseau de fact-checkers et cadre commun de recherche : capacité financée et intégrée

Le Bouclier ajoute des capacités nouvelles. En mars 2026, la Commission a signé une subvention de 5 millions d'euros pour un réseau européen de fact-checkers conduit par l'EFCSN avec sept partenaires. Le projet doit renforcer la couverture linguistique, mettre en place un dispositif de protection pour les fact-checkers et créer un répertoire européen indépendant des vérifications. [FCT-013]

Le cadre commun de recherche sur l'intégrité de l'information dispose pour sa première étape d'un appel de 6 millions d'euros, financé à 100 %, sur 24 à 30 mois, avec au moins 60 % de la subvention devant être redistribuée à des tiers. Ses fonctions annoncées sont de réduire les silos de recherche, fournir des capacités technologiques, faciliter l'accès à des outils et données et soutenir des acteurs de la recherche, de la société civile, du fact-checking et de la technologie. [FCT-014, FCT-015]

La communication du Bouclier prévoit que ces capacités, ainsi que le monitoring d'EDMO, alimentent la plateforme de parties prenantes du Centre de résilience démocratique. [FCT-003]

Ce schéma constitue un flux documenté : `fonds publics -> capacités de recherche/fact-checking -> production de connaissances et signaux -> situational awareness`. Il ne documente pas, sans étape supplémentaire, `fonds publics -> ordre de qualifier un contenu -> ordre de retrait`.

## 5. Le vrai pont réglementaire : Code de conduite et DSA

La thèse inverse — « tout est seulement volontaire, donc sans portée réglementaire » — est également trop faible. En février 2025, la Commission et le Comité européen des services numériques ont approuvé l'intégration du Code de bonnes pratiques contre la désinformation comme Code de conduite dans le cadre du DSA ; la conversion est devenue effective le 1er juillet 2025. [FCT-016]

L'adhésion au Code reste volontaire. Mais pour les très grandes plateformes et moteurs qui adhèrent, le respect des engagements devient un élément pertinent de l'appréciation de conformité aux obligations de gestion des risques systémiques, et les engagements sont intégrés aux audits indépendants annuels. [FCT-017]

Il existe donc une **co-régulation réelle** : un dispositif construit par des parties prenantes et auquel on adhère volontairement acquiert une signification dans la mise en œuvre du DSA pour les signataires concernés. Ce constat est plus précis que deux slogans opposés : « simple autorégulation privée » et « ordre direct de censure de Bruxelles ».

Pour imputer une décision de modération précise, il faut encore fermer les arêtes suivantes : quelle mesure du Code ou quelle obligation DSA était en cause, quel acteur a produit le signal, quelle plateforme ou autorité a pris la décision, sur quel motif, avec quelle marge propre, et quel recours a modifié ou confirmé la décision.

## 6. Recours : le système produit aussi des corrections mesurables

Le DSA impose des mécanismes de motivation et de recours contre les décisions de modération. Les données agrégées publiées par la Commission montrent que depuis 2024 plus de 165 millions de décisions de modération prises par les VLOP/VLOSE ont fait l'objet d'un recours interne, avec près de 30 % de décisions inversées. Pour le premier semestre 2025, les organismes de règlement extrajudiciaire ont examiné plus de 1 800 litiges relatifs à Facebook, Instagram et TikTok et inversé 52 % des dossiers clos. [FCT-018]

Ces chiffres ne permettent pas d'attribuer les décisions initiales au Bouclier ou à des fact-checkers. Ils montrent cependant qu'une description sérieuse du système doit intégrer les voies de contestation et les erreurs corrigées. Une infrastructure de gouvernance informationnelle ne se résume donc pas à son flux descendant ; elle possède aussi des mécanismes de retour, de révision et de recours.

## 7. EUvsDisinfo : communication stratégique institutionnelle, mais frontière explicite sur le retrait

EUvsDisinfo appartient au Service européen pour l'action extérieure et relève d'une logique différente d'EDMO. Le SEAE indique explicitement que son équipe ne coopère pas avec les plateformes sociales pour obtenir le retrait de contenus. Il décrit sa base comme un outil public d'analyse et de sensibilisation. [FCT-019]

Le SEAE précise aussi que la Disinformation Review ne constitue pas une position officielle de l'UE, parce qu'elle résulte d'un monitoring sélectif, et affirme que l'équipe vise les messages de désinformation plutôt que les opinions ou la mise sur liste noire des personnes. [FCT-020]

Cela n'en fait pas un acteur neutre ou extérieur aux institutions : EUvsDisinfo est bien un projet institutionnel du SEAE et s'inscrit dans la communication stratégique de l'Union. Le budget annoncé pour 2021 de la division Strategic Communications and Information Analysis atteignait 11,1 millions d'euros et finançait monitoring, analyse, campagnes de sensibilisation, formations et simulations. [FCT-021]

La qualification correcte est donc : **capacité institutionnelle de monitoring, qualification et communication stratégique**, avec dans le dossier public examiné une frontière explicite contre une fonction directe de retrait de contenus.

## 8. Contrôle indépendant : les lacunes historiques de la Cour des comptes

La Cour des comptes européenne fournit un contrôle externe important, mais historiquement borné. Son rapport spécial de 2021 sur le plan d'action contre la désinformation conclut que le dispositif était pertinent mais incomplet et que certains résultats attendus n'avaient pas été produits. Elle signalait aussi des faiblesses de suivi et d'obligation de rendre compte. [FCT-022]

Le système d'alerte rapide avait facilité les échanges, mais au moment de l'audit il n'avait pas émis d'alertes ni coordonné l'attribution et la réponse communes comme prévu. [FCT-023]

La Cour reconnaissait l'utilité d'EUvsDisinfo pour la sensibilisation, tout en relevant que son placement dans le SEAE pouvait soulever des questions d'indépendance ou donner l'impression d'une position officielle de l'UE. [FCT-024]

Elle identifiait enfin un risque qu'EDMO, alors récent, n'atteigne pas ses objectifs et recommandait des améliorations de gouvernance, de visibilité et de représentation. Ce constat précède les extensions et financements ultérieurs d'EDMO ; il ne peut donc pas être projeté tel quel sur 2026. [FCT-025]

Le contrôle historique démontre surtout une constante : l'expansion d'une capacité institutionnelle n'est pas une preuve de son efficacité. Les indicateurs, l'audit, les faux positifs et les voies de recours doivent rester des objets séparés.

## 9. Modèles concurrents

### Modèle A — Coordination proportionnée de résilience démocratique

Ce modèle est **fortement compatible** avec les faits institutionnels : menaces identifiées, capacités de monitoring, réseaux de recherche, coopération entre États et institutions, obligations de plateformes et mécanismes de recours. [FCT-002, FCT-004, FCT-010, FCT-016, FCT-018]

Il ne peut cependant pas être élevé au rang de conclusion normative automatique : le caractère « proportionné » dépend des cas d'application, des faux positifs, de la transparence, de l'efficacité et du respect des libertés.

### Modèle B — Gouvernance distribuée de l'espace informationnel

Ce modèle est **établi** au niveau structurel. Plusieurs acteurs publics ou financés publiquement produisent des analyses, standards, connaissances, signaux, formations et capacités ; ces outputs s'articulent à des plateformes, au DSA et à des réseaux institutionnels. [FCT-003, FCT-010, FCT-013, FCT-015, FCT-016, FCT-027]

« Distribuée » est ici essentiel : les relations documentées ne forment pas une chaîne hiérarchique simple.

### Modèle C — Expansion bureaucratique/industrielle

Ce modèle est **plausible et partiellement documenté** par la multiplication des programmes et des enveloppes de financement, ainsi que par les recommandations visant encore plus de capacités et de budget. [FCT-007, FCT-008, FCT-013, FCT-014, FCT-026]

Mais `croissance budgétaire -> menace artificiellement fabriquée` n'est pas démontré. Cette hypothèse nécessite précisément la synthèse INV-144 : budgets, marchés, bénéficiaires, métriques et incitations dans le temps.

### Modèle D — Architecture centralisée de censure

Ce modèle n'est **pas établi** par le présent dossier. Les éléments disponibles documentent coordination et co-régulation, mais ils documentent aussi des barrières : indépendance formelle d'EDMO, statut d'observateur de la Commission, absence déclarée de coopération d'EUvsDisinfo au retrait de contenus, recours DSA et séparation des autorités. [FCT-011, FCT-012, FCT-018, FCT-019]

Cette conclusion n'exclut pas l'existence possible de cas individuels d'action excessive ou de coordination contestable. Elle signifie qu'un tel cas doit être démontré par une chaîne spécifique et ne peut être inféré de la seule cartographie institutionnelle.

## 10. Plafond causal et résultat

Le plus haut niveau solidement soutenu est :

- **I0 relation/identité : VERIFIED** pour les principales institutions, programmes et réseaux ;
- **I1 ressources/capacité : VERIFIED** pour les principaux financements EDMO, hubs, fact-checkers, recherche et le budget historique du SEAE ;
- **I2 action documentée : VERIFIED** pour monitoring, analyse, fact-checking, recherche, coordination, communication stratégique et gouvernance DSA ;
- **I3 coordination/tasking : VERIFIED** pour la coordination du Centre et les contrats/programmes, mais non transférable à un tasking éditorial de chaque acteur ;
- **I4 exposition/reach : PARTIAL**, faute de métrique agrégée cohérente pour tout l'écosystème ;
- **I5 réception/persuasion : NOT_ESTABLISHED** au niveau système ;
- **I6 changement comportemental/institutionnel : PARTIAL**, notamment parce que les recours et révisions de plateformes sont mesurables mais leur causalité avec l'écosystème anti-FIMI est hétérogène ;
- **I7 résultat démocratique contrefactuel : NOT_ESTABLISHED**.

Le delta central est donc double.

Premièrement, il existe bien en 2026 un **écosystème européen structuré et financé de gouvernance/résilience informationnelle**, combinant coordination institutionnelle, recherche, fact-checking, communication stratégique et co-régulation des grandes plateformes. Le réduire à quelques initiatives indépendantes et sans articulation serait faux.

Deuxièmement, les preuves examinées ne permettent pas de transformer cet écosystème en une **chaîne unitaire de censure commandée par la Commission**. La preuve s'arrête avant cette qualification générale. Le point le plus matériel à suivre n'est donc pas le nombre d'organismes, mais les arêtes concrètes `signal -> décision de plateforme/régulateur -> recours -> effet`, ainsi que l'économie politique des financements et métriques.

## 11. Routage

Le résultat alimente directement deux synthèses :

- **INV-040** : le dossier fournit une cartographie probatoire des pouvoirs formels, capacités de coordination et intermédiaires dans le champ informationnel européen ;
- **INV-144** : il fournit des flux financiers, programmes, structures, métriques manquantes et incitations potentielles à analyser sans présumer une « industrie de la menace ».

Les questions de décision de modération ou de certification de fact-checkers doivent rester principalement dans **INV-043** et **INV-045** lorsqu'un cas précis permet de fermer la chaîne causale.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:4|SRC_COMPLETE:14/14

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **anchor_events:**
  - 2018: EU Action Plan against Disinformation
  - 2020: EDMO active
  - 2025-07: Disinformation Code effective as DSA Code of Conduct
  - 2025-11: European Democracy Shield presented
  - 2026-02: European Centre for Democratic Resilience operational
  - 2026-03/04: new EDMO, fact-checking and research funding actions
  - 2026-06: Parliament special committee recommends stronger legal basis
- **as_of:** 2026-09-07
- **rules:**
  - policy announcement != legal power
  - historical audit finding != current unchanged state
  - funding date != operational effect date
- **window:** 2018-2026

### MANIPULATION_REPORT
- **assumptions:**
  - formal independence safeguards are treated as evidence of governance design, not proof of perfect practical independence
  - public institutional sources are authoritative for their own mandates and funding but not for normative legitimacy or causal effectiveness
  - negative evidence about direct removal power is bounded to the examined public record
- **clusters:**
  - **loaded:**
    - clusters/POWER.md
    - clusters/NETWORK.md
    - clusters/FRAMING.md
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - public funding does not settle editorial control
  - coordination does not settle content action
  - anti-disinformation purpose does not settle legitimacy
- **input_kind:** TOPIC
- **mission_mode:** INVESTIGATION
- **patterns:**
  - distributed governance
  - public-private resilience network
  - co-regulation through DSA code
  - strategic communication
  - situational awareness
  - fact-checking and research capacity
- **priorities:**
  - legal form and powers
  - funding/resource flows
  - governance independence
  - signal-to-action boundary
  - appeals/audits
  - effect ceilings
- **query_guidance:** trace legal form -> money -> governance -> monitoring/signal -> platform/regulatory action -> appeal -> exposure -> behavior -> counterfactual
- **rhetorical:**
  - **AUTH:** official descriptions bounded to mandate claims
  - **BF:** N/A
  - **DEM:** normative democratic legitimacy separated from mechanism evidence
  - **FAC:** avoid network-to-command generalization
  - **NUM:** budget/network counts do not establish effect
- **speaker:**
  - **goal:** forensic classification of EU counter-FIMI architecture
  - **target:** mandate-funding-governance-action-effect chains
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **Κ:** 3
  - **Λ:** 5
  - **Ξ:** 4
  - **Σ:** 4
  - **Φ:** 3
  - **Ψ:** 3
  - **Ω:** 4
  - **κ:** 3
  - **ρ:** 5
  - **€:** 5
  - **↕:** 5
  - **⏰:** 4
  - **⚔:** 3
  - **⫸:** 5
  - **🌐:** 6
- **threats:**
  - funding=command
  - coordination=control
  - anti-FIMI=censorship
  - platform action=EU order
  - audit criticism=current unchanged state

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - current total cross-program budget denominator
  - **input_ids:**
    - FCT-001
    - FCT-002
    - FCT-007
    - FCT-013
    - FCT-014
    - FCT-016
    - FCT-026
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no unitary statutory command authority established
  - **not_computable:**
    - hidden informal influence over grantees
  - **operations_applied:**
    - typed legal form and resource flows
    - separated recommendation from existing authority
  - **reason:** separate formal mandates, funding and regulatory authority
  - **result_ids:**
    - CLM-001
    - CLM-004
    - CLM-005
    - CTRL-001
    - CTRL-006
  - **status:** DONE
  - **trigger:** ↕
- **item 2:**
  - **gaps:**
    - case-level informal coordination records
  - **input_ids:**
    - FCT-003
    - FCT-004
    - FCT-006
    - FCT-010
    - FCT-011
    - FCT-012
    - FCT-015
    - FCT-019
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - network membership does not establish central control
  - **not_computable:**
    - complete informal contact graph
  - **operations_applied:**
    - typed coordination, observer and information-flow edges
    - preserved independent governance boundaries
  - **reason:** map Centre, Commission, EEAS, EDMO, fact-checkers, researchers and platforms without association fallacies
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-004
    - CTRL-002
    - CTRL-003
  - **status:** DONE
  - **trigger:** 🌐
- **item 3:**
  - **gaps:**
    - matched causal dataset linking signals to moderation and electoral effect
  - **input_ids:**
    - FCT-016
    - FCT-017
    - FCT-018
    - FCT-019
    - FCT-020
    - FCT-022
    - FCT-024
    - FCT-026
  - **module:** clusters/FRAMING.md
  - **negative_results:**
    - centralized censorship command not established
    - purely voluntary/no regulatory significance framing rejected
  - **not_computable:**
    - counterfactual democratic outcome
  - **operations_applied:**
    - retained co-regulatory significance
    - retained removal and appeal boundaries
    - bounded historical audit criticism
  - **reason:** test censorship-machine and purely-voluntary framings against legal and operational evidence
  - **result_ids:**
    - CLM-002
    - CLM-003
    - CLM-006
    - CTRL-003
    - CTRL-004
    - CTRL-005
  - **status:** DONE
  - **trigger:** Λ

### SCOPING_REPORT
- **classification_dimensions:**
  - legal form
  - mandate
  - funding
  - governance
  - coordination
  - monitoring
  - signalling
  - platform action
  - appeal
  - metric
  - effect
- **exclusions:**
  - anti_FIMI=censorship
  - funding=command
  - coordination=control
  - flagging=removal
  - fact-checking=state speech
  - content action=political effect
  - network=unitary command
- **scope:** EU counter-FIMI/disinformation architecture 2018-2026; mandates, funding, governance, signal/action interfaces, safeguards and measured effects.
- **status:** ACTIVE

### CREDO
- anti-FIMI != censorship
- funding != command
- coordination != control
- participation != capture
- flagging != removal
- fact-check != state order
- platform moderation != Commission order
- budget growth != fabricated threat
- institutional network != coherent command architecture
- action != democratic effect

### COGNITIVE_MAP
- **causal_boundary:** Architecture and resources are strongly documented; direct signal-to-removal causality is case-specific; I5-I7 persuasion/behavior/counterfactual effects are not established ecosystem-wide.
- **core_model:** A distributed EU counter-FIMI ecosystem exists across strategy, public funding, operational coordination, independent/arm-length monitoring and fact-checking, EEAS strategic communications and DSA co-regulation.
- **relation_chain:**
  - mandate/legal form
  - funding/procurement
  - governance
  - monitoring/research/fact-checking
  - signal/risk assessment
  - platform/regulatory action
  - appeal/correction
  - exposure
  - behavior
  - counterfactual democratic outcome
- **rival_models:**
  - proportionate democratic-resilience coordination
  - distributed governance with arm-length intermediaries
  - bureaucratic/industrial expansion around threat response
  - centralized censorship architecture

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** The examined record shows heterogeneous legal forms, non-voting/independence safeguards, explicit EUvsDisinfo non-removal, and platform appeal rights.
  - **resolution:** A distributed influence/governance ecosystem is established; centralized command over lawful political speech is not.
  - **thesis:** EU anti-disinformation bodies form a centralized censorship machine.
- **item 2:**
  - **antithesis:** EDMO rules formally bar funders from decision-making and give the Commission observer-only status.
  - **resolution:** Funding dependence is material and must be disclosed, but command requires separate evidence.
  - **thesis:** Because EDMO and fact-checkers are EU-funded, their conclusions are Commission-directed.
- **item 3:**
  - **antithesis:** For adhering VLOPs/VLOSEs the Disinformation Code is a DSA compliance benchmark and audit object.
  - **resolution:** The architecture contains a real co-regulatory bridge without equating every moderation outcome with an EU order.
  - **thesis:** The system is purely voluntary and therefore has no regulatory significance.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **from:** European Commission / Digital Europe
  - **limits:**
    - funding != editorial command
  - **resource:** procurement and grants
  - **support:**
    - FCT-007
    - FCT-008
    - FCT-009
    - FCT-010
  - **to:** monitoring, research, fact-checking and media-literacy capacity
  - **via:** EDMO Central and hubs
- **item 2:**
  - **from:** European Commission / Digital Europe
  - **limits:**
    - grant objectives != control of individual verdicts
  - **resource:** EUR 5m grant
  - **support:**
    - FCT-013
  - **to:** multilingual fact-check capacity, protection scheme and repository
  - **via:** EFCSN-led European fact-checking network
- **item 3:**
  - **from:** European Commission / Digital Europe
  - **limits:**
    - research support != regulatory action
  - **resource:** EUR 6m call
  - **support:**
    - FCT-014
    - FCT-015
  - **to:** research infrastructure and third-party support
  - **via:** Common Research Framework
- **item 4:**
  - **from:** EEAS budget
  - **limits:**
    - historical budget; not current total system budget
  - **resource:** EUR 11.1m 2021 StratCom budget
  - **support:**
    - FCT-021
  - **to:** monitoring, analysis, campaigns, training and simulations
  - **via:** Strategic Communications and Information Analysis Division

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** European Commission + High Representative
  - **limits:**
    - Joint Communication != self-executing takedown authority
  - **relation:** Joint Communication / strategic framework
  - **support:**
    - FCT-001
    - FCT-002
  - **to:** European Democracy Shield actions
- **item 2:**
  - **from:** European Centre for Democratic Resilience
  - **limits:**
    - coordination != control of every participant
  - **relation:** exchange, operational cooperation and coordination
  - **support:**
    - FCT-004
    - FCT-005
    - FCT-006
  - **to:** EU institutions, Member States, candidate countries and stakeholder platform
- **item 3:**
  - **from:** Commission funding
  - **limits:**
    - funding != command
  - **relation:** procurement/grants
  - **support:**
    - FCT-007
    - FCT-008
    - FCT-009
    - FCT-013
    - FCT-014
  - **to:** EDMO, hubs, fact-check network, research framework
- **item 4:**
  - **from:** EDMO / research / fact-check communities
  - **limits:**
    - monitoring != removal
  - **relation:** monitoring, analysis and expertise
  - **support:**
    - FCT-003
    - FCT-010
    - FCT-015
  - **to:** situational awareness / Centre stakeholder platform
- **item 5:**
  - **from:** DSA Disinformation Code
  - **limits:**
    - benchmark != specific moderation order
  - **relation:** voluntary adhesion plus compliance benchmark/audit
  - **support:**
    - FCT-016
    - FCT-017
  - **to:** adhering VLOPs/VLOSEs
- **item 6:**
  - **from:** EUvsDisinfo / EEAS
  - **limits:**
    - explicitly no platform-removal cooperation in cited EEAS Q&A
  - **relation:** monitoring, exposure and strategic communication
  - **support:**
    - FCT-019
    - FCT-020
    - FCT-021
  - **to:** public information environment

### IMPACT_MAP
- **I0_identity_relation:** VERIFIED for institutions, programmes and governance relations
- **I1_resources_capability:** VERIFIED for major EDMO/fact-check/research funding and EEAS historical budget
- **I2_documented_action:** VERIFIED for monitoring, analysis, fact-checking, coordination, communication and DSA-code governance
- **I3_coordination_tasking:** VERIFIED for Centre coordination and programme contracts; NOT transferable to editorial tasking of independent actors
- **I4_exposure_reach:** PARTIAL; network scale and DSA moderation volumes documented but ecosystem-specific reach not unified
- **I5_reception_persuasion:** NOT_ESTABLISHED ecosystem-wide
- **I6_behavior_institutional_change:** PARTIAL for platform reversals/appeals and institutional process changes; causal attribution heterogeneous
- **I7_counterfactual_outcome:** NOT_ESTABLISHED
- **downstream:** Feeds INV-040 on democratic-governance design and INV-144 on budgets, markets, metrics and incentives.

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** EDMO governance rules bar funders from decision-making and make Commission participation observer-only
  - **issue:** EDMO independence versus EU funding
  - **pro:** large and repeated EU funding streams are documented
  - **resolution:** FUNDING_DEPENDENCE_VERIFIED_COMMAND_NOT_ESTABLISHED
- **item 2:**
  - **contra:** EUvsDisinfo explicitly denies content-removal cooperation; DSA provides appeals; EDMO has no documented unilateral takedown power in examined sources
  - **issue:** counter-disinformation versus censorship
  - **pro:** system coordinates monitoring, fact-checking, risk mitigation and platform accountability
  - **resolution:** GOVERNANCE_AND_CO-REGULATION_VERIFIED_CENTRAL_CENSORSHIP_NOT_ESTABLISHED
- **item 3:**
  - **contra:** for adhering VLOPs/VLOSEs commitments are DSA compliance benchmark and audit object
  - **issue:** voluntary code versus regulatory force
  - **pro:** Code adherence is voluntary
  - **resolution:** CO_REGULATORY_SIGNIFICANCE_ESTABLISHED_DIRECT_ORDER_NOT
- **item 4:**
  - **contra:** ECA historical audit found incomplete accountability and weak RAS performance; Parliament committee seeks stronger legal basis
  - **issue:** mature system versus accountability gaps
  - **pro:** 2026 architecture is larger and has more formal governance/appeal mechanisms
  - **resolution:** CAPACITY_EXPANDED_OUTCOME_ACCOUNTABILITY_STILL_PARTIAL

### VERIFICATION_REPORT
- **independence_limits:**
  - Commission/EEAS/Parliament sources dominate institutional-description claims
  - EDMO independence safeguards are self-governance documents
  - ECA audit is independent but historically bounded to 2020-era system
  - no matched case dataset tracing fact-check/signal -> moderation -> electoral outcome
- **negative_checks:**
  - EUvsDisinfo non-removal boundary retained
  - EDMO funder-independence rules retained
  - ECA 2021 accountability criticisms retained
  - Parliament 2026 stronger-legal-basis recommendation retained as recommendation not law
  - no I7 claim
- **source_families:** 5
- **source_records_complete:** 14/14
- **status:** PASS_WITH_EXPLICIT_GAPS
- **web_fact_trace:** 27/27 facts mapped to accepted FETCH-backed sources

### EDI_REPORT
- **corpus:**
  - **circularity:** LOW_TO_MODERATE
  - **coverage:** ARCHITECTURE_AND_GOVERNANCE_STRONG
  - **independence:** MODERATE_WITH_INSTITUTIONAL_CONCENTRATION
  - **limits:**
    - many core architecture facts necessarily come from EU institutional sources
    - EDMO independence evidence partly self-described
    - outcome causality data sparse
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 4
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES_WITH_NEGATIVE_BOUNDARY
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 3
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** YES
    - **gap_type:** CAUSALITY
    - **independent_families:** 2
  - **item 4:**
    - **claim_id:** CLM-006
    - **direct_object:** PARTIAL
    - **gap_type:** CAUSALITY
    - **independent_families:** 3
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** 5_PROVENANCE_FAMILIES
  - **perspective:** COMMISSION+EEAS+PARLIAMENT+ECA+EDMO
  - **stratification:** LEGAL_FORM+FUNDING+GOVERNANCE+OPERATIONAL_ROLE+AUDIT+REMEDIES
  - **temporal:** 2018-2026
- **edi:**
  - **assessment:** HIGH_ARCHITECTURE_COVERAGE_WITH_CONTENT_ACTION_AND_OUTCOME_GAPS
  - **flags:**
    - INSTITUTIONAL_SOURCE_CONCENTRATION
    - FUNDING_NOT_COMMAND
    - CO_REGULATION_NOT_DIRECT_ORDER
    - HISTORICAL_AUDIT_LIMIT
    - NO_ECOSYSTEM_COUNTERFACTUAL_EFFECT
- **source_counts:**
  - **claim_source:** 0
  - **primary:** 11
  - **provenance_families:** 5
  - **secondary:** 3
  - **total:** 14

### RESPONSIBILITY_MAP
- **item 1:**
  - **highest_supported:** strategic framework defining and connecting multiple actions
  - **not_supported:** single statutory authority commanding all downstream actors
  - **object:** European Democracy Shield
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-027
- **item 2:**
  - **highest_supported:** operational coordination/exchange hub with secretariat and broad participation
  - **not_supported:** fully-fledged binding regulatory authority with dedicated budget
  - **object:** European Centre for Democratic Resilience
  - **support:**
    - FCT-004
    - FCT-005
    - FCT-006
    - FCT-026
- **item 3:**
  - **highest_supported:** EU-funded monitoring, research and fact-check capacity with published independence safeguards
  - **not_supported:** Commission editorial tasking of specific outputs
  - **object:** EDMO/fact-checking ecosystem
  - **support:**
    - FCT-007
    - FCT-008
    - FCT-009
    - FCT-010
    - FCT-011
    - FCT-012
    - FCT-013
- **item 4:**
  - **highest_supported:** DSA/code creates risk-mitigation benchmarks and appeals/audits
  - **not_supported:** general causal attribution of specific removals to EDMO/EUvsDisinfo/Commission
  - **object:** platform content actions
  - **support:**
    - FCT-016
    - FCT-017
    - FCT-018
    - FCT-019

### NEXT_QUERIES
- **item 1:**
  - **query:** case-level records linking an EDMO/fact-check/centre signal to a specific platform moderation or regulator enforcement decision
  - **route:** INV-043_OR_INV-045
  - **trigger:** identified primary case record
- **item 2:**
  - **query:** cross-program budget, procurement and beneficiary denominator for 2025-2027 counter-FIMI ecosystem
  - **route:** INV-144
  - **trigger:** synthesis input
- **item 3:**
  - **query:** matched outcome studies measuring exposure, persuasion or electoral effects of EU counter-disinformation interventions
  - **route:** DEFER
  - **trigger:** identified causal design

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-007,QRY-008,QRY-009,QRY-011,QRY-014 | support:- | counter:- | results:FCT-001,FCT-002,FCT-004,FCT-007,FCT-010,FCT-013,FCT-015,FCT-016,FCT-021,FCT-027 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-005,QRY-006,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-011,FCT-012,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-022,FCT-026 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-007,QRY-008,QRY-009,QRY-011,QRY-014 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-010,FCT-013,FCT-015,FCT-016,FCT-021,FCT-027 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-003,QRY-004,QRY-007,QRY-008,QRY-011 | support:- | counter:- | results:FCT-007,FCT-008,FCT-009,FCT-013,FCT-014,FCT-021 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-005,QRY-006,QRY-012 | support:- | counter:- | results:FCT-011,FCT-012,FCT-024,FCT-025 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-009,QRY-010,QRY-011 | support:- | counter:- | results:FCT-016,FCT-017,FCT-018,FCT-019,FCT-020 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-001,QRY-002,QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-004,FCT-005,FCT-006,FCT-023,FCT-026,FCT-027 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-010,QRY-012,QRY-013 | support:- | counter:- | results:FCT-018,FCT-022,FCT-023,FCT-024,FCT-025,FCT-026 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,QRY-002,QRY-004,QRY-007,QRY-008,QRY-009,QRY-011,QRY-014,SRC-001,SRC-002,SRC-004,SRC-007,SRC-008,SRC-009,SRC-011,SRC-014 | support:FCT-001,FCT-002,FCT-003,FCT-004,FCT-010,FCT-013,FCT-015,FCT-016,FCT-021,FCT-027 | counter:CTRL-002;CTRL-004 | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-010,FCT-013,FCT-015,FCT-016,FCT-021,FCT-027,CTRL-002;CTRL-004 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-002 | attempts:QRY-005,QRY-006,QRY-009,QRY-011,SRC-005,SRC-006,SRC-009,SRC-011 | support:FCT-011,FCT-012,FCT-019,FCT-020,FCT-016,FCT-017 | counter:CTRL-003 | results:FCT-011,FCT-012,FCT-019,FCT-020,FCT-016,FCT-017,CTRL-003 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-003 | attempts:QRY-009,SRC-009 | support:FCT-016,FCT-017 | counter:CTRL-004 | results:FCT-016,FCT-017,CTRL-004 | final:SUPPORTED | gap:CAUSALITY
CLM-004 | attempts:QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,SRC-003,SRC-004,SRC-005,SRC-006,SRC-007,SRC-008 | support:FCT-007,FCT-008,FCT-009,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015 | counter:CTRL-001 | results:FCT-007,FCT-008,FCT-009,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,CTRL-001 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-005 | attempts:QRY-002,QRY-013,SRC-002,SRC-013 | support:FCT-004,FCT-005,FCT-006,FCT-026 | counter:CTRL-006 | results:FCT-004,FCT-005,FCT-006,FCT-026,CTRL-006 | final:SUPPORTED | gap:TEMPORAL
CLM-006 | attempts:QRY-006,QRY-010,QRY-012,SRC-006,SRC-010,SRC-012 | support:FCT-012,FCT-018,FCT-022,FCT-023,FCT-024,FCT-025 | counter:CTRL-005 | results:FCT-012,FCT-018,FCT-022,FCT-023,FCT-024,FCT-025,CTRL-005 | final:PARTIAL | gap:CAUSALITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-001 | CLM | SUPPORTED | RESPONSIBILITY | The ecosystem is institutionally distributed; a single coherent command hierarchy over all actors is not established.
CLM-002 | CLM | SUPPORTED | RESPONSIBILITY | Platform-specific or regulator-specific content actions must be traced case by case under DSA or national law; INV-043/045 own those downstream questions.
CLM-003 | CLM | SUPPORTED | CAUSALITY | A benchmark does not show that any specific moderation decision was caused by EU institutions or by a fact-checking organisation.
CLM-004 | CLM | SUPPORTED | RESPONSIBILITY | Formal safeguards do not prove perfect practical independence; conversely funding alone does not prove command.
CLM-005 | CLM | SUPPORTED | TEMPORAL | Parliament’s committee recommendation had not yet itself created the requested legal powers as of the run date.
CLM-006 | CLM | PARTIAL | CAUSALITY | No common 2026 outcome metric links the entire Shield ecosystem to reduced manipulation, improved voter autonomy or a counterfactual democratic outcome.
CAU-001 | CAU | UNRESOLVED | CAUSALITY | Direct signal-to-moderation attribution and I5-I7 persuasion/behavior/counterfactual effects are not established at ecosystem level.

SEMANTIC_COUNTS_V1:LED:2|CLM:6|AXS:6|CAU:1|CTRL:6|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-007","QRY-008","QRY-009","QRY-011","QRY-014"],"evidence_excerpt":"The sources document multiple linked institutions, grants, monitoring and co-regulatory mechanisms, but different legal forms and governance boundaries.","kind":"HYPOTHESIS","lead":"The EU has built a distributed public-private/institutional counter-FIMI ecosystem rather than one unitary censorship command structure.","linked_ids":["CLM-001","CLM-002","CLM-003","CLM-004","CLM-005"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-004","FCT-007","FCT-010","FCT-013","FCT-015","FCT-016","FCT-021","FCT-027"],"routes":["ARCHITECTURE","GOVERNANCE","CONTENT_BOUNDARY"],"source_id":"INV-044_RUN_CARD","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-005","QRY-006","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013"],"evidence_excerpt":"EDMO independence rules, EUvsDisinfo removal boundary, DSA appeals and ECA audit findings all preserve these distinctions.","kind":"METHOD_CONSTRAINT","lead":"Funding, coordination, flagging, platform moderation and democratic effect are separate edges and must not be collapsed.","linked_ids":["CTRL-001","CTRL-002","CTRL-003","CTRL-004","CTRL-005","CTRL-006"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-011","FCT-012","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-022","FCT-026"],"routes":["CONTROL","CAUSALITY","ACCOUNTABILITY"],"source_id":"INV-044_RUN_CARD","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"By 2026 the EU has a documented multi-layer counter-disinformation/FIMI ecosystem linking a strategic Shield, an operational coordination centre, EDMO monitoring, EU-funded fact-checking and research capacity, EEAS strategic communications and DSA platform-risk governance.","claimant":"INV-044 synthesis","counter":"CTRL-002;CTRL-004","gap":"The ecosystem is institutionally distributed; a single coherent command hierarchy over all actors is not established.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-010","FCT-013","FCT-015","FCT-016","FCT-021","FCT-027"]}
CLM-002 | {"claim":"The examined evidence supports coordination, monitoring, research, fact-checking, strategic communication and regulatory-risk mitigation, but does not support the stronger proposition that EDMO or EUvsDisinfo possesses a general unilateral power to order removal of lawful political content.","claimant":"INV-044 synthesis","counter":"CTRL-003","gap":"Platform-specific or regulator-specific content actions must be traced case by case under DSA or national law; INV-043/045 own those downstream questions.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-011","FCT-012","FCT-019","FCT-020","FCT-016","FCT-017"]}
CLM-003 | {"claim":"The DSA-linked Code of Conduct creates a real co-regulatory bridge: adhesion is voluntary, yet for adhering VLOPs/VLOSEs the commitments are a compliance benchmark and subject to independent audit.","claimant":"INV-044 synthesis","counter":"CTRL-004","gap":"A benchmark does not show that any specific moderation decision was caused by EU institutions or by a fact-checking organisation.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-016","FCT-017"]}
CLM-004 | {"claim":"EU financial support for EDMO, its hubs, the European fact-checking network and the common research framework is substantial and structurally important, while EDMO publishes governance safeguards intended to separate funders from editorial and research decisions.","claimant":"INV-044 synthesis","counter":"CTRL-001","gap":"Formal safeguards do not prove perfect practical independence; conversely funding alone does not prove command.","gap_type":"RESPONSIBILITY","materiality":"HIGH","status":"SUPPORTED","support":["FCT-007","FCT-008","FCT-009","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015"]}
CLM-005 | {"claim":"The European Centre for Democratic Resilience is operational as a coordination hub in 2026, but the Parliament special committee itself sought a binding legal act, dedicated budget and clearer operational parameters, indicating that the current centre should not be described as an already fully-fledged regulatory authority.","claimant":"INV-044 synthesis","counter":"CTRL-006","gap":"Parliament’s committee recommendation had not yet itself created the requested legal powers as of the run date.","gap_type":"TEMPORAL","materiality":"HIGH","status":"SUPPORTED","support":["FCT-004","FCT-005","FCT-006","FCT-026"]}
CLM-006 | {"claim":"Accountability mechanisms are mixed: EDMO has governance/complaint provisions and DSA users have appeal routes with substantial reversal rates, while the Court of Auditors historically found incomplete accountability and weak performance metrics in the earlier EU anti-disinformation architecture.","claimant":"INV-044 synthesis","counter":"CTRL-005","gap":"No common 2026 outcome metric links the entire Shield ecosystem to reduced manipulation, improved voter autonomy or a counterfactual democratic outcome.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-012","FCT-018","FCT-022","FCT-023","FCT-024","FCT-025"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-007","QRY-008","QRY-009","QRY-011","QRY-014"],"axis":"ARCHITECTURE","links":["CLM-001"],"question":"What entities and mechanisms make up the EU counter-FIMI/disinformation ecosystem and how are they linked?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-010","FCT-013","FCT-015","FCT-016","FCT-021","FCT-027"],"sought_objects":["MANDATE","CENTRE","EDMO","FACT_CHECK_NETWORK","RESEARCH_FRAMEWORK","EEAS","DSA"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-003","QRY-004","QRY-007","QRY-008","QRY-011"],"axis":"FUNDING","links":["CLM-004","CTRL-001"],"question":"What public funding or procurement flows support EDMO, hubs, fact-checking and research capacity?","result_ids":["FCT-007","FCT-008","FCT-009","FCT-013","FCT-014","FCT-021"],"sought_objects":["GRANT","PROCUREMENT","BUDGET","RECIPIENT"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-005","QRY-006","QRY-012"],"axis":"GOVERNANCE_INDEPENDENCE","links":["CLM-004","CLM-006","CTRL-001","CTRL-005"],"question":"What formal safeguards or dependencies exist between funders, governance and editorial/research choices?","result_ids":["FCT-011","FCT-012","FCT-024","FCT-025"],"sought_objects":["GOVERNANCE","OBSERVER","VOTE","COMPLAINT","INDEPENDENCE"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-009","QRY-010","QRY-011"],"axis":"CONTENT_ACTION_BOUNDARY","links":["CLM-002","CLM-003","CTRL-003","CTRL-004"],"question":"Which actors can signal, analyse, regulate or remove content, and what direct removal authority is actually documented?","result_ids":["FCT-016","FCT-017","FCT-018","FCT-019","FCT-020"],"sought_objects":["SIGNAL","ANALYSIS","MODERATION","REMOVAL","REGULATORY_POWER"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-001","QRY-002","QRY-012","QRY-013","QRY-014"],"axis":"COORDINATION_CAPACITY","links":["CLM-005","CTRL-002","CTRL-006"],"question":"What operational coordination and early-warning capacity exists, and what are its legal or institutional limits?","result_ids":["FCT-004","FCT-005","FCT-006","FCT-023","FCT-026","FCT-027"],"sought_objects":["COORDINATION","EARLY_WARNING","RAPID_RESPONSE","LEGAL_BASIS"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-010","QRY-012","QRY-013"],"axis":"EFFECT_ACCOUNTABILITY","links":["CLM-006","CTRL-005"],"question":"What metrics, audits, appeals and independent controls show whether the system works or overreaches?","result_ids":["FCT-018","FCT-022","FCT-023","FCT-024","FCT-025","FCT-026"],"sought_objects":["METRIC","AUDIT","APPEAL","REVERSAL","OUTCOME"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"Independent governance, platform discretion, national authorities, user appeals, market incentives and other information sources can interrupt or confound every downstream edge.","gap":"Direct signal-to-moderation attribution and I5-I7 persuasion/behavior/counterfactual effects are not established at ecosystem level.","gap_type":"CAUSALITY","limit":"The run establishes architecture, resource flows and formal interfaces better than case-level content-action causality or democratic outcome effects.","mechanism":"EU strategy/funding -> coordination and monitoring/research/fact-checking capacity -> signals or risk assessments -> platform/regulatory/communication responses -> exposure and information-environment change -> voter/institutional effect","status":"UNRESOLVED","support":["FCT-002","FCT-003","FCT-004","FCT-010","FCT-013","FCT-015","FCT-016","FCT-017"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Funding control: EU grants and procurement establish resource dependence and programme design, but do not by themselves prove editorial command over EDMO, fact-checkers or researchers.","status":"DONE","support":["FCT-007","FCT-008","FCT-009","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015"]}
CTRL-002 | {"control":"Coordination control: the European Centre explicitly coordinates exchange, situational awareness and response capacity, but coordination is not evidence that every participant is controlled by a central authority.","status":"DONE","support":["FCT-004","FCT-005","FCT-006"]}
CTRL-003 | {"control":"Removal control: EUvsDisinfo explicitly states it does not cooperate with platforms on content removal; no examined EDMO governance source grants EDMO unilateral takedown authority.","status":"DONE","support":["FCT-019","FCT-020","FCT-011","FCT-012"]}
CTRL-004 | {"control":"DSA boundary control: the Disinformation Code is voluntary to join but can become a benchmark and audit object for adhering VLOPs/VLOSEs, so self-regulatory commitments can acquire co-regulatory significance without becoming direct editorial orders from EDMO or EUvsDisinfo.","status":"DONE","support":["FCT-016","FCT-017"]}
CTRL-005 | {"control":"Temporal control: the 2021 Court of Auditors findings are an independent baseline on accountability, Rapid Alert System performance and early EDMO risks; they cannot be projected unchanged onto the expanded 2025-2026 architecture.","status":"DONE","support":["FCT-022","FCT-023","FCT-024","FCT-025"]}
CTRL-006 | {"control":"Legal-status control: the Parliament special committee’s June 2026 call for a binding legal act, dedicated budget and stronger tools is a political recommendation and evidence of perceived current limitations, not proof that those requested powers already exist.","status":"DONE","support":["FCT-026"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:14|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | MNEMO_UNAVAILABLE degraded; exact snapshot search unavailable in this environment | MnemoLite | NONE | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | PASS | SRC-001 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:52025JC0791 | European Democracy Shield joint communication
QRY-002 | FETCH | PASS | SRC-002 | https://commission.europa.eu/european-centre-democratic-resilience_en | European Centre for Democratic Resilience role membership
QRY-003 | FETCH | PASS | SRC-003 | https://digital-strategy.ec.europa.eu/en/policies/european-digital-media-observatory | EDMO funding phases hubs 15
QRY-004 | FETCH | PASS | SRC-004 | https://digital-strategy.ec.europa.eu/en/news/european-digital-media-observatory-continues-its-activities | EDMO continuation 2026 extended mandate
QRY-005 | FETCH | PASS | SRC-005 | https://edmo.eu/edmo-news/guiding-principles-for-the-edmo-network | EDMO guiding principles independence funders
QRY-006 | FETCH | PASS | SRC-006 | https://edmo.eu/about-us/edmoeu-governance/governance-charter/ | EDMO governance charter complaint observer
QRY-007 | FETCH | PASS | SRC-007 | https://digital-strategy.ec.europa.eu/en/news/commission-boosts-independent-fact-checking-eu5-million-grant-under-european-democracy-shield | European fact-checking network 5 million 2026
QRY-008 | FETCH | PASS | SRC-008 | https://digital-strategy.ec.europa.eu/en/events/information-session-digital-2026-bestuse-awareness-common-research-framework-information-integrity | Common Research Framework information integrity 6 million
QRY-009 | FETCH | PASS | SRC-009 | https://digital-strategy.ec.europa.eu/en/library/code-conduct-disinformation | Code of Conduct Disinformation DSA audit benchmark
QRY-010 | FETCH | PASS | SRC-010 | https://digital-strategy.ec.europa.eu/en/policies/dsa-impact-platforms | DSA moderation appeals reversals 2026
QRY-011 | FETCH | PASS | SRC-011 | https://www.eeas.europa.eu/eeas/questions-and-answers-about-east-stratcom-task-force_en | EUvsDisinfo role removal content budget
QRY-012 | FETCH | PASS | SRC-012 | https://op.europa.eu/webpub/eca/special-reports/disinformation-9-2021/en/ | ECA audit EU disinformation action plan
QRY-013 | FETCH | PASS | SRC-013 | https://www.europarl.europa.eu/news/en/press-room/20260622IPR45921/des-propositions-visant-a-ameliorer-le-bouclier-de-la-democratie-europeenne | EP special committee Democracy Shield recommendations
QRY-014 | FETCH | PASS | SRC-014 | https://www.europarl.europa.eu/thinktank/en/academic/EPRS_ATA(2026)782603 | EPRS European Democracy Shield overview

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | CELEX:52025JC0791 | European Democracy Shield: Empowering Strong and Resilient Democracies | 2025-11-12 | 2026-09-07T11:50:00+02:00 | actions / information-space section | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:52025JC0791
SRC-002 | ◈ | fam:A | commission:ECDR | European Centre for Democratic Resilience | 2026-02-24 | 2026-09-07T11:50:00+02:00 | overview / role / objectives / members | https://commission.europa.eu/european-centre-democratic-resilience_en
SRC-003 | ◈ | fam:A | commission:EDMO-policy | European Digital Media Observatory - EDMO | 2026-06-22 | 2026-09-07T11:50:00+02:00 | funding / EDMO Central / Hubs | https://digital-strategy.ec.europa.eu/en/policies/european-digital-media-observatory
SRC-004 | ◈ | fam:A | commission:EDMO-2026 | European Digital Media Observatory continues its activities | 2026-03-09 | 2026-09-07T11:50:00+02:00 | award / extended mandate / network | https://digital-strategy.ec.europa.eu/en/news/european-digital-media-observatory-continues-its-activities
SRC-005 | ◉ | fam:D | edmo:guiding-principles | Guiding Principles for the EDMO Network | undated | 2026-09-07T11:50:00+02:00 | independence / transparency / neutrality | https://edmo.eu/edmo-news/guiding-principles-for-the-edmo-network
SRC-006 | ◉ | fam:D | edmo:governance-charter | Governance Charter - EDMO | undated | 2026-09-07T11:50:00+02:00 | Executive Board / Advisory Council / complaints | https://edmo.eu/about-us/edmoeu-governance/governance-charter/
SRC-007 | ◈ | fam:A | commission:factcheck-grant-2026 | Commission boosts independent fact-checking with a €5 million grant under the European Democracy Shield | 2026-03-31 | 2026-09-07T11:50:00+02:00 | grant / EFCSN / protection scheme | https://digital-strategy.ec.europa.eu/en/news/commission-boosts-independent-fact-checking-eu5-million-grant-under-european-democracy-shield
SRC-008 | ◈ | fam:A | commission:CRF-2026 | Information Session - Common Research Framework on Information Integrity | 2026-04-29 | 2026-09-07T11:50:00+02:00 | core aims / budget / redistribution | https://digital-strategy.ec.europa.eu/en/events/information-session-digital-2026-bestuse-awareness-common-research-framework-information-integrity
SRC-009 | ◈ | fam:A | commission:code-disinformation-2025 | The Code of Conduct on Disinformation | 2025-02-13 | 2026-09-07T11:50:00+02:00 | DSA integration / voluntary / audits | https://digital-strategy.ec.europa.eu/en/library/code-conduct-disinformation
SRC-010 | ◈ | fam:A | commission:DSA-impact-2026 | The impact of the Digital Services Act on digital platforms | 2026-06-01 | 2026-09-07T11:50:00+02:00 | appeals / reversal statistics / transparency | https://digital-strategy.ec.europa.eu/en/policies/dsa-impact-platforms
SRC-011 | ◈ | fam:E | eeas:east-stratcom-qa | Questions and Answers about the East StratCom Task Force | 2021 | 2026-09-07T11:50:00+02:00 | budget / EUvsDisinfo / platform-removal boundary | https://www.eeas.europa.eu/eeas/questions-and-answers-about-east-stratcom-task-force_en
SRC-012 | ◈ | fam:C | eca:SR09-2021 | Disinformation affecting the EU: tackled but not tamed | 2021-04-27 | 2026-09-07T11:50:00+02:00 | conclusions / RAS / EDMO / accountability | https://op.europa.eu/webpub/eca/special-reports/disinformation-9-2021/en/
SRC-013 | ◈ | fam:B | ep:EUDS-2026-06-23 | Special committee adopts proposals to improve the European Democracy Shield | 2026-06-23 | 2026-09-07T11:50:00+02:00 | centre legal mandate / dedicated budget / binding tools | https://www.europarl.europa.eu/news/en/press-room/20260622IPR45921/des-propositions-visant-a-ameliorer-le-bouclier-de-la-democratie-europeenne
SRC-014 | ◈ | fam:B | eprs:782603 | The European Democracy Shield: An overview | 2026-01-15 | 2026-09-07T11:50:00+02:00 | information-space actions / incident protocol / research framework | https://www.europarl.europa.eu/thinktank/en/academic/EPRS_ATA(2026)782603

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:52025JC0791 | A | 2025-11-12 | European Democracy Shield legal form | The European Democracy Shield was issued as Joint Communication JOIN(2025) 791 final by the European Commission and the High Representative. | -
FCT-002 | FACT | ✧ | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:52025JC0791 | A | 2025-11-12 | European Democracy Shield information-space actions | The Shield lists actions including a DSA incidents and crisis protocol, an EU Blueprint for countering FIMI and disinformation, a European Network of Fact-Checkers, an extended EDMO mandate and a common research support framework. | -
FCT-003 | FACT | ✧ | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:52025JC0791 | A | 2025-11-12 | EDMO feed into resilience centre | The Joint Communication states that EDMO monitoring and the common research support framework will feed into the Stakeholder Platform under the European Centre for Democratic Resilience. | -
FCT-004 | FACT | ✧ | https://commission.europa.eu/european-centre-democratic-resilience_en | A | 2026-02-24 | European Centre operational-coordination role | The European Centre for Democratic Resilience is described as a hub for exchange and as a framework for operational cooperation and coordination among participating Member States, EU institutions and candidate or potential candidate countries. | -
FCT-005 | FACT | ✧ | https://commission.europa.eu/european-centre-democratic-resilience_en | A | 2026-09-04 | European Centre objectives and secretariat | The Centre lists situational awareness, early warning, rapid-response capacity and societal resilience as objectives; its Secretariat ensures operational coordination between members. | -
FCT-006 | FACT | ✧ | https://commission.europa.eu/european-centre-democratic-resilience_en | A | 2026-09-04 | European Centre participation breadth | The Centre page lists the European Parliament, European Commission, EEAS and all EU Member States as participating institutions or states, alongside a stakeholder platform for independent stakeholders. | -
FCT-007 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/european-digital-media-observatory | A | 2026-06-22 | EDMO central funding phases | Commission funding information lists EDMO Central procurement phases of EUR 2.5 million initially, EUR 4 million in 2022, and approximately EUR 2.5 million under the Digital Europe 2025 work programme. | -
FCT-008 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/european-digital-media-observatory | A | 2026-06-22 | EDMO hub funding phases | Commission funding information lists EUR 11 million for the first eight EDMO hubs, EUR 8 million for six additional hubs, EUR 10 million to refinance the first eight in 2023, and about EUR 8.8 million for six continuing hubs; the network totals 15 hubs including F.A.C.T. | -
FCT-009 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/news/european-digital-media-observatory-continues-its-activities | A | 2026-03-09 | EDMO 2026 continuation award | The Commission awarded EUR 2.5 million for continuation of EDMO central activities after an open 2025 call. | -
FCT-010 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/news/european-digital-media-observatory-continues-its-activities | A | 2026-03-09 | EDMO extended situational-awareness mandate | In the new phase EDMO is to develop independent monitoring and analytical capabilities for online information-ecosystem situational awareness, especially during elections and crises; the Commission describes 15 hubs and a community of more than 100 organisations. | -
FCT-011 | FACT | ✧ | https://edmo.eu/edmo-news/guiding-principles-for-the-edmo-network | D | undated | EDMO funder independence rule | EDMO guiding principles state that external public or private funders may not sit in consortium decision-making bodies or influence priorities, methods or results; the Commission may participate only as an observer to monitor funding-agreement deployment. | -
FCT-012 | FACT | ✧ | https://edmo.eu/about-us/edmoeu-governance/governance-charter/ | D | undated | EDMO governance and complaints | EDMO governance is entrusted to an Executive Board and Advisory Council; a Commission representative participates in the Advisory Council as a non-voting observer, and complaints about EDMO activities or staff may be brought to the Advisory Council via the Secretary-General. | -
FCT-013 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/news/commission-boosts-independent-fact-checking-eu5-million-grant-under-european-democracy-shield | A | 2026-03-31 | European fact-checking network grant | The Commission signed a EUR 5 million grant led by EFCSN with seven partner organisations to expand fact-checking capacity, a protection scheme and an independent European repository of fact-checks. | -
FCT-014 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/events/information-session-digital-2026-bestuse-awareness-common-research-framework-information-integrity | A | 2026-04-29 | Common Research Framework budget | The 2026 Common Research Framework call funds one proposal with EUR 6 million at a 100% funding rate over 24 to 30 months, with at least 60% of the grant to be redistributed as financial support to third parties. | -
FCT-015 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/events/information-session-digital-2026-bestuse-awareness-common-research-framework-information-integrity | A | 2026-04-29 | Common Research Framework functions | The Common Research Framework aims to bridge research silos, expand capabilities, provide technological infrastructure and facilitate use of regulatory research tools; target stakeholders include research, civil society, fact-checking and technology providers. | -
FCT-016 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/library/code-conduct-disinformation | A | 2025-02-13 | Disinformation Code DSA integration | The Commission and European Board for Digital Services endorsed integration of the voluntary Code of Practice on Disinformation into the DSA framework, effective 1 July 2025. | -
FCT-017 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/library/code-conduct-disinformation | A | 2025-07-01 | Disinformation Code compliance benchmark | For adhering VLOPs and VLOSEs, compliance with the Code becomes a relevant benchmark for DSA compliance on disinformation risks and the commitments are subject to annual independent audit. | -
FCT-018 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/policies/dsa-impact-platforms | A | 2026-06 | DSA moderation appeal reversals | The Commission reports that since 2024 users appealed more than 165 million VLOP/VLOSE moderation decisions through platform mechanisms, with almost 30% reversed; in the first half of 2025, out-of-court bodies reviewed over 1,800 disputes and reversed 52% of closed cases. | -
FCT-019 | FACT | ✧ | https://www.eeas.europa.eu/eeas/questions-and-answers-about-east-stratcom-task-force_en | E | 2021 | EUvsDisinfo removal boundary | The EEAS states that the East StratCom Task Force does not cooperate with social-media platforms on removal of content; its EUvsDisinfo database is publicly accessible. | -
FCT-020 | FACT | ✧ | https://www.eeas.europa.eu/eeas/questions-and-answers-about-east-stratcom-task-force_en | E | 2021 | EUvsDisinfo official-position boundary | The EEAS states that the EUvsDisinfo Disinformation Review is based on selective media monitoring and cannot be considered an official EU position, and that the team focuses on disinformation messages rather than targeting opinions or blacklisting people. | -
FCT-021 | FACT | ✧ | https://www.eeas.europa.eu/eeas/questions-and-answers-about-east-stratcom-task-force_en | E | 2021 | EEAS StratCom budget and activities | The EEAS states that the 2021 budget for its Strategic Communications and Information Analysis Division addressing disinformation and manipulative interference was EUR 11.1 million, supporting monitoring, analysis, awareness campaigns, training and simulations. | -
FCT-022 | FACT | ✧ | https://op.europa.eu/webpub/eca/special-reports/disinformation-9-2021/en/ | C | 2021-04-27 | ECA overall audit finding | The European Court of Auditors concluded that the 2018 EU disinformation action plan was relevant but incomplete and had not delivered all intended results; it found fragmented monitoring and accountability weaknesses. | -
FCT-023 | FACT | ✧ | https://op.europa.eu/webpub/eca/special-reports/disinformation-9-2021/en/ | C | 2021-04-27 | ECA Rapid Alert System finding | At the time of the audit the EU Rapid Alert System had facilitated information sharing but had not issued alerts or coordinated common attribution and response as initially envisaged. | -
FCT-024 | FACT | ✧ | https://op.europa.eu/webpub/eca/special-reports/disinformation-9-2021/en/ | C | 2021-04-27 | ECA EUvsDisinfo independence concern | The Court found EUvsDisinfo instrumental in raising awareness but noted that its placement inside the EEAS raises questions about independence and could create a perception that it represents an official EU position. | -
FCT-025 | FACT | ✧ | https://op.europa.eu/webpub/eca/special-reports/disinformation-9-2021/en/ | C | 2021-04-27 | ECA EDMO risk finding | The Court identified a risk that the newly created EDMO would not achieve its objectives and recommended measures on stakeholder representation, awareness and lessons learned; this finding predates the later EDMO expansion. | -
FCT-026 | FACT | ✧ | https://www.europarl.europa.eu/news/en/press-room/20260622IPR45921/des-propositions-visant-a-ameliorer-le-bouclier-de-la-democratie-europeenne | B | 2026-06-23 | EP committee asks stronger legal basis | The European Parliament special committee supported the Centre but called for it to be established in a binding legal act with operational parameters and a dedicated budget, while also advocating stronger platform accountability and other binding tools. | -
FCT-027 | FACT | ✧ | https://www.europarl.europa.eu/thinktank/en/academic/EPRS_ATA(2026)782603 | B | 2026-01-15 | EPRS architecture summary | The European Parliament Research Service describes the Shield information-space package as complementing existing digital rules with a DSA incident/crisis protocol, work with the Disinformation Code, a FIMI blueprint, fact-checker network, extended EDMO monitoring and common research support. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-002
FCT-005 | SRC-002
FCT-006 | SRC-002
FCT-007 | SRC-003
FCT-008 | SRC-003
FCT-009 | SRC-004
FCT-010 | SRC-004
FCT-011 | SRC-005
FCT-012 | SRC-006
FCT-013 | SRC-007
FCT-014 | SRC-008
FCT-015 | SRC-008
FCT-016 | SRC-009
FCT-017 | SRC-009
FCT-018 | SRC-010
FCT-019 | SRC-011
FCT-020 | SRC-011
FCT-021 | SRC-011
FCT-022 | SRC-012
FCT-023 | SRC-012
FCT-024 | SRC-012
FCT-025 | SRC-012
FCT-026 | SRC-013
FCT-027 | SRC-014

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

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8
CP-002 | SEARCH | PASS | LAST_COMPLETED:9:ECOSYSTEM | NEXT_ACTION:10
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11:CAU-001 | NEXT_ACTION:12
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-07T10:06:52.795542+00:00","fact_mem":{},"mnemo_row":"BLOCKED:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":27,"eligible":27,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:BLOCKED:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:27;attempted:0;success:0;failure:0;blocked:27} | WRITEBACK_EXECUTION_V1:[27 rows, see section]

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
