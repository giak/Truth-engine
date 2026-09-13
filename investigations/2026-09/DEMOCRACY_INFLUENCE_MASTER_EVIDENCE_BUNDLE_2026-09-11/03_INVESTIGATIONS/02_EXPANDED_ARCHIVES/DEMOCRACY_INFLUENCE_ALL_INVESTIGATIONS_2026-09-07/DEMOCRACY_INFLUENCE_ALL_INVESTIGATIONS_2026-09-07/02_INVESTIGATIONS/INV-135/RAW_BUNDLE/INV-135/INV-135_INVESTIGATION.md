ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260906-1842-hack-and-leak | PARENT_RUN_ID:NONE | AS_OF:2026-09-06
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/truth-engine/investigations/2026-09/2026-09-06_hack-and-leak/2026-09-06_18-42_hack-and-leak_INPUT.txt | SUBJECT_SLUG:hack-and-leak | SUBJECT_FP:sha256:128ed24e06eb5a3438da64f8c5f52693c62a34282fcd333100a550f89c97ac56 | INPUT_SHA256:sha256:ba4fd06707cd8aefba0339919bee3e97d81e6109f5370385a293c817b2b75c7b
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:Elections 2016–2026; priority France/Europe with US comparators; separate hack/theft, authenticity/alteration, release timing, amplification, exposure, persuasion and electoral effect; chronology-sensitive attribution.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "truth_engine_investigation"
artifact_id: "INV-135"
run_id: "20260906-1842-hack-and-leak"
status: "final_candidate"
updated: "2026-09-06"
---

<!-- TRACE: source=INV-135_RUN_CARD; runtime=Truth_Engine_2.10.6_R3P1 -->
<!-- DECISION: hack!=leak!=integrity!=timing!=amplification!=effect; attribution_is_time_stamped -->

# INV-135 — Hack-and-leak, kompromat et divulgations synchronisées

## Verdict exécutif

Le mécanisme **hack-and-leak** est réel, documenté et électoralement exploitable, mais il ne doit jamais être résumé par « X a piraté une campagne et changé l’élection ». Le corpus impose une chaîne sérielle :

`compromission → vol → attribution → intégrité des documents → choix du moment → publication → amplification → exposition → persuasion → résultat électoral`

Chaque flèche demande sa propre preuve (`CLM-001`). Les trois cas retenus ferment cette chaîne à des niveaux très différents.

**MacronLeaks 2017** établit une fuite tardive de données issues ou présentées comme issues de la campagne Macron, avec une alerte officielle sur la possibilité de faux contenus et une revendication de la campagne selon laquelle documents authentiques et faux avaient été mêlés (`FCT-001..004`). Ce que le dossier public inspecté ne permet pas de faire est de calculer quelle fraction de l’archive était falsifiée ou d’authentifier chaque pièce. Sur l’attribution, l’état de preuve a changé : le rapport CAPS/IRSEM publié en 2018 rappelait que la France n’avait pas officiellement attribué l’attaque et citait l’ANSSI jugeant la technique trop générique pour conclure (`FCT-005..006`). En avril 2025, la France a officiellement affirmé que le GRU avait utilisé APT28 dans la tentative de déstabilisation du processus électoral français de 2017 (`FCT-007`). Le rapport technique CERT-FR publié le même jour détaille surtout des chaînes APT28 de 2021–2024 et ne rend pas publique, à lui seul, toute la chaîne forensique rétroactive de 2017 (`FCT-008`). La conclusion correcte est donc : **attribution française renforcée et officialisée en 2025, sans réécrire l’incertitude publique de 2017 comme si elle n’avait jamais existé** (`CLM-003`).

Sur l’effet, MacronLeaks est surtout un contrôle négatif. L’analyse Ferrara trouve une amplification importante mais une audience très orientée vers des utilisateurs étrangers et alt-right, moins vers l’électorat français (`FCT-009..010`). La Commission nationale de contrôle conclut que le timing tardif, le discrédit entourant la fuite et la retenue des grands médias ont limité sa portée et que l’épisode n’a pas porté atteinte à la sincérité du scrutin (`FCT-003`). Cela ne prouve pas zéro persuasion individuelle ; cela interdit seulement d’affirmer un effet électoral matériel sans données supplémentaires.

**DNC/Podesta 2016** ferme beaucoup plus haut la chaîne opérationnelle. Le dossier judiciaire américain identifie des officiers et unités du GRU, les techniques de spearphishing et de compromission, les personas DCLeaks/Guccifer 2.0 et la transmission de données volées vers l’organisation qui les a publiées (`FCT-011..013`). Le choix du calendrier est également documenté : le matériel DNC est demandé et publié juste avant la convention démocrate (`FCT-012`), puis les premiers mails Podesta paraissent le 7 octobre (`FCT-013`). Le rapport Mueller constate que la publication du 7 octobre survient moins d’une heure après la diffusion de la vidéo Access Hollywood, mais il **n’établit pas** que les démarches attribuées à Jerome Corsi ont causé cette publication ni que la campagne Trump a conspiré ou coordonné avec le gouvernement russe dans l’opération d’ingérence (`FCT-014..015`). Timing stratégique documenté ne signifie donc pas coordination Trump–Russie prouvée.

Le matériel volé a toutefois eu un **effet d’agenda médiatique** documentable. Berkman décrit la place centrale des emails et scandales dans la couverture de Clinton (`FCT-018`) ; Jamieson soutient que les publications ont déplacé l’agenda de presse dans les dernières semaines (`FCT-019`). Mais la communauté du renseignement américaine a explicitement refusé d’évaluer l’effet des opérations russes sur le résultat de l’élection (`FCT-016`). `CLM-007` et `CAU-001` restent donc fermes : agenda médiatique ≠ nombre de votes changés ≠ vainqueur changé.

Enfin, **Iran / campagne Trump 2024** fournit un contrôle de symétrie. Microsoft a observé une activité de spearphishing liée à l’IRGC (`FCT-020`) ; le DOJ a inculpé trois acteurs en alléguant une opération hack-and-leak destinée à influencer l’élection (`FCT-021`). ODNI/FBI/CISA ont indiqué que des extraits de matériel Trump volé avaient été envoyés à des personnes associées à la campagne Biden et à des médias, sans information montrant une réponse des destinataires de campagne (`FCT-022`). Surtout, les grands médias ayant reçu des documents ont choisi de ne pas en publier substantiellement le contenu (`FCT-023`). Le même mécanisme que 2016 rencontre donc un **goulot d’amplification différent**.

## 1. Le modèle probatoire : une chaîne, pas un label

Le premier résultat d’INV-135 est méthodologique. Une opération peut réussir jusqu’au vol et échouer à la diffusion. Elle peut réussir à diffuser et n’atteindre qu’une audience périphérique. Elle peut dominer l’agenda sans que l’on puisse identifier un seul vote changé. À l’inverse, une archive peut être authentique et son exploitation rester manipulatoire par sélection, cadrage ou timing.

La taxonomie minimale devient :

1. **HACK / ACCESS** : accès non autorisé établi ?
2. **THEFT** : quels objets ont été exfiltrés ?
3. **ATTRIBUTION** : opérateur, intermédiaire, État/commanditaire ?
4. **INTEGRITY** : documents authentiques, altérés, injectés, inconnus ?
5. **TIMING** : publication opportuniste ou tasking documenté ?
6. **AMPLIFICATION** : bots, médias, influenceurs, plateformes, relais politiques ?
7. **EXPOSURE** : audience authentique mesurée ?
8. **RECEPTION** : croyance, perception, comportement ?
9. **OUTCOME** : changement de vote, participation, résultat ?
10. **COUNTERFACTUAL** : que se serait-il passé sans l’opération ?

Cette grille empêche quatre erreurs fréquentes : `hack = État`, `documents authentiques = publication légitime`, `timing = coordination`, `audience = effet électoral`.

## 2. MacronLeaks : le cas où l’attribution évolue

### 2.1 L’événement et l’intégrité

Le 5 mai 2017, à quelques heures de la fin de la campagne officielle, une masse de données présentées comme provenant des messageries de l’équipe Macron est mise en ligne (`FCT-001`). La Commission de contrôle saisit immédiatement l’ANSSI et le parquet. Elle avertit que les données **peuvent être en partie fausses** (`FCT-002`). La campagne Macron affirme de son côté qu’éléments authentiques et faux ont été mélangés (`FCT-004`).

Le point de discipline est essentiel : la campagne est victime et source sur l’intégrité de ses propres données ; son affirmation est matériellement pertinente mais ne constitue pas une authentification indépendante de toute l’archive. INV-135 n’a pas trouvé de rapport public établissant un taux de faux, un inventaire exhaustif des altérations ou une chaîne de hachage forensique de chaque document. `CLM-002` reste donc `PARTIAL/ACCESS` sur ce point.

### 2.2 2017 n’est pas 2025

Le rapport CAPS/IRSEM de 2018 résume les indices alors disponibles : hameçonnage rapproché d’APT28, métadonnées en cyrillique et autres traces. Mais il rappelle aussi la prudence de l’ANSSI et la possibilité de faux drapeau (`FCT-005..006`).

La situation change le 29 avril 2025. Le ministère français des Affaires étrangères affirme officiellement que le GRU a utilisé le mode opératoire APT28 dans la tentative de déstabilisation du processus électoral français de 2017 (`FCT-007`). Cette attribution ultérieure est une nouvelle donnée et doit corriger toute phrase restée figée à « non attribué ».

Mais il faut éviter l’erreur inverse : le CERT-FR publié le même jour expose des campagnes et chaînes de compromission APT28 surtout observées entre 2021 et 2024 (`FCT-008`). Le communiqué politique attribue bien l’épisode 2017 ; le rapport technique public associé ne déroule pas, dans son texte accessible, une démonstration spécifique MacronLeaks équivalente au dossier américain DNC. Le verdict est donc **officiellement attribué en 2025**, avec une granularité publique différente de celle du dossier DNC.

### 2.3 Effet : un échec relatif, pas une absence d’opération

Ferrara observe une activité sociale importante autour du hashtag mais un engagement majoritairement étranger/alt-right (`FCT-009..010`). La Commission nationale de contrôle considère que le timing, le discrédit et la retenue des grands médias ont limité l’épisode et n’ont pas altéré la sincérité du scrutin (`FCT-003`).

Cela réfute deux simplifications opposées :

- « l’opération a échoué donc il n’y a pas eu d’ingérence » ;
- « il y a eu ingérence donc l’élection a été changée ».

L’opération et l’effet sont deux objets.

## 3. DNC/Podesta 2016 : chaîne opérationnelle beaucoup plus fermée

### 3.1 Hack et attribution

L’acte d’accusation Netyksho détaille les unités du GRU, le spearphishing, les réseaux DNC/DCCC compromis et le vol de documents (`FCT-011`). Le rapport Mueller reprend l’opération russe de hacking et de diffusion (`FCT-014`). Le rapport sénatorial bipartite renforce le rôle de WikiLeaks dans la campagne d’influence (`FCT-017`).

Le statut juridique doit néanmoins rester exact : un acte d’accusation est une accusation pénale, pas une condamnation des accusés. La robustesse du modèle vient de la convergence de plusieurs produits institutionnels et investigations, pas d’une transformation du mot « indictment » en « jugement ».

### 3.2 Timing

La preuve de timing est inhabituelle : l’acte d’accusation reproduit des échanges où l’organisation de publication demande des éléments avant la convention démocrate et publie plus de 20 000 emails/documents trois jours avant celle-ci (`FCT-012`). Pour Podesta, la première vague part le 7 octobre (`FCT-013`).

Mueller documente ensuite la proximité temporelle avec Access Hollywood tout en refusant le raccourci causal : certaines déclarations de Corsi ont été examinées, mais l’enquête n’établit pas qu’il a effectivement provoqué la publication (`FCT-015`). `CLM-006` est donc un bon exemple de frontière : **timing stratégique = soutenu ; coordination spécifique Trump/Corsi → WikiLeaks → publication = non établie**.

### 3.3 Agenda ≠ résultat

Le corpus américain est plus fort sur l’effet intermédiaire que le corpus français. Berkman mesure une couverture centrée sur les emails et scandales de Clinton (`FCT-018`). Jamieson argumente que les dumps ont déplacé l’agenda dans les dernières semaines (`FCT-019`). Ce sont des effets informationnels plausibles et documentés.

Ils ne répondent pas au niveau I7. L’ICA 2017 dit explicitement qu’elle **n’évalue pas** l’impact des activités russes sur le résultat (`FCT-016`). Une élection serrée n’autorise pas à remplir ce vide par intuition rétrospective.

## 4. Iran 2024 : le même mécanisme, un autre goulot d’étranglement

Le cas 2024 permet un test important parce que la cible est républicaine. Microsoft observe une opération de spearphishing liée à l’IRGC (`FCT-020`). Le DOJ inculpe ensuite trois acteurs et décrit un schéma hack-and-leak (`FCT-021`). Les agences américaines indiquent que des extraits volés ont été envoyés à des personnes associées à la campagne Biden et à des rédactions, sans réponse connue des destinataires de campagne (`FCT-022`).

L’étage médiatique change radicalement : Politico, le New York Times et le Washington Post reçoivent du matériel mais n’en publient pas substantiellement le contenu, selon AP (`FCT-023`). Ce contraste avec 2016 est une quasi-expérience descriptive du **media gate**, pas une expérience causale sur le vote. Il montre néanmoins qu’une opération de leak a besoin d’intermédiaires d’amplification ; le vol seul ne garantit pas la portée.

## 5. Comparaison des trois cas

| Maillon | Macron 2017 | DNC/Podesta 2016 | Iran/Trump 2024 |
|---|---|---|---|
| Hack/vol | établi | fortement établi | fortement allégué/attribué |
| Attribution État | officialisée en 2025, public technique 2017 moins détaillé | forte base publique GRU | forte base publique IRGC, procédure pénale en cours |
| Intégrité corpus | mix allégué, fraction inconnue | corpus traité comme volé ; falsification systémique non nécessaire au dossier | documents authentifiés par certaines rédactions, corpus complet non public |
| Timing stratégique | très tardif | fortement documenté | tentative en cours de campagne |
| Amplification | forte en ligne, faible gate média FR | très forte couverture mainstream | gate média fortement restrictif |
| Exposition | audience surtout étrangère/alt-right dans l’étude Ferrara | agenda médiatique massif | distribution tentée ; reprise substantielle limitée |
| Persuasion | non identifiée | non identifiée causalement | non identifiée |
| Changement du vainqueur | non établi | non établi | non établi |

La leçon n’est pas qu’aucune opération n’a d’effet. La leçon est que **le niveau de preuve décroît à mesure qu’on avance vers le résultat politique**.

## 6. Contre-théories obligatoires

### « Une fuite de documents vrais est du journalisme, pas une manipulation »

Parfois oui, selon l’origine et le contexte. Mais un vol clandestin commandité par un État, suivi d’une sélection et d’un calendrier destiné à maximiser un dommage électoral, est un mécanisme distinct de la véracité intrinsèque des documents. `authenticité ≠ légitimité du procédé`.

### « Les faux dans MacronLeaks prouvent que tout était faux »

Non. Le dossier public ne soutient pas cette généralisation. Il soutient la possibilité ou l’allégation d’un mélange, pas un taux de falsification global.

### « La France n’attribuait pas en 2017, donc l’accusation russe était fausse »

Non. L’absence d’attribution publique à l’époque était une limite de preuve publique, pas une preuve d’innocence. L’attribution française de 2025 est une donnée nouvelle.

### « La France attribue en 2025, donc tous les indices russes de 2017 étaient déjà des preuves suffisantes »

Non plus. Un verdict ultérieur ne transforme pas rétroactivement chaque indice faible en preuve forte. La chaîne doit être datée.

### « WikiLeaks a publié le jour d’Access Hollywood, donc Trump a coordonné la publication »

La proximité temporelle est établie. La causalité spécifique et la coordination ne le sont pas dans le rapport Mueller.

### « Le DNC hack a changé l’élection »

Le matériel a influencé l’agenda médiatique ; la communauté du renseignement n’a pas évalué l’effet sur le résultat et le corpus scoped ne fournit pas de contrefactuel winner-changing.

## 7. Highest supported I0–I7

```text
I0 identity/relation = VERIFIED/PARTIAL selon cas
I1 capability/access = VERIFIED — phishing/compromission/outils documentés
I2 documented action = VERIFIED — vols et publications documentés dans les trois familles
I3 coordination/tasking = STRONG pour GRU release chain; PARTIAL pour Macron 2017 public chain; STRONG-ALLEGED IRGC 2024
I4 exposure/reach = MEASURED/PARTIAL — fort agenda 2016; audience périphérique Macron; gate média restrictif 2024
I5 reception/persuasion = NOT_ESTABLISHED causalement
I6 behavior/institutional/electoral change = NOT_ESTABLISHED causalement
I7 counterfactual outcome = NOT_ESTABLISHED
```

## 8. Gaps matériels

- **MacronLeaks** : inventaire forensique public complet de l’intégrité du corpus non trouvé ; chaîne technique publique rétroactive 2017 → GRU/APT28 moins détaillée que le communiqué politique 2025.
- **DNC/Podesta** : effet médiatique documentable ; effet winner-changing non identifié ; causalité précise de la publication du 7 octobre par rapport à Access Hollywood non établie.
- **Iran 2024** : procédure pénale à distinguer d’une condamnation ; uptake politique et effet électoral non établis.
- **Tous les cas** : pas de contrefactuel propre permettant de convertir exposition/agenda en votes décisifs.

## 9. Conclusion technique

INV-135 impose une règle de travail : **ne jamais coder “hack-and-leak = ingérence réussie” comme un seul claim**.

Le registre doit porter séparément :

`HACK → THEFT → ATTRIBUTION → INTEGRITY → TIMING → RELEASE → AMPLIFICATION → EXPOSURE → PERSUASION → OUTCOME → COUNTERFACTUAL`

Le corpus démontre trois choses robustes : des opérations hack-and-leak étatiques existent ; le timing et les intermédiaires de publication sont des leviers opérationnels réels ; et la preuve de l’effet électoral final est beaucoup plus rare que la preuve du piratage ou de la diffusion. La symétrie du cas iranien 2024 confirme que cette discipline doit s’appliquer indépendamment du camp politique ciblé.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:0|EDI_DECISIVE:7|SRC_COMPLETE:16/16

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **DNC:** 2016 hack/releases -> 2017 ICA -> 2018 indictment -> 2019 Mueller -> 2020 Senate
- **Iran2024:** June spearphishing -> July/August stolen-material outreach -> September US attribution/indictment
- **MacronLeaks:** 2017 event -> 2018 published non-attribution/caveats -> 2025 official French GRU/APT28 attribution
- **as_of:** 2026-09-06

### MANIPULATION_REPORT
- **assumptions:**
  - stolen genuine material can be manipulative through selection/timing
  - falsification is not required for hack-and-leak interference
  - later attribution can update earlier uncertainty
- **clusters:**
  - NONE
- **complexity:**
  - **band:** HIGH
  - **score:** 9
- **implicit:**
  - hack != attribution
  - authentic document != non-manipulative use
  - timing != coordination
  - publication != authentic exposure
  - exposure != persuasion
  - agenda effect != vote effect
  - later attribution != retroactive certainty
- **input_kind:** TOPIC
- **mission_mode:** INVESTIGATION
- **patterns:**
  - hack-and-leak chain decomposition
  - temporal attribution updating
  - integrity/provenance separation
  - strategic timing analysis
  - amplification gate
  - effect inflation
- **priorities:**
  - chronology-sensitive attribution
  - separate authenticity from provenance
  - test strategic timing without timing=coordination shortcut
  - measure amplification separately from persuasion
  - use media response as control
- **query_guidance:** prefer primary judicial/technical/election-control records; time-stamp attribution; distinguish claimant statements from forensic authentication; retain causal gaps unless identified design exists
- **rhetorical:**
  - NONE
- **speaker:** user/object question
- **symbol_stage:** FINAL
- **symbols:**
  - **M:** 4
  - **Κ:** 4
  - **Λ:** 5
  - **Ξ:** 5
  - **Σ:** 4
  - **Φ:** 5
  - **Ψ:** 4
  - **Ω:** 4
  - **κ:** 4
  - **ρ:** 5
  - **€:** 2
  - **↕:** 5
  - **⏰:** 5
  - **⚔:** 3
  - **⫸:** 5
- **threats:**
  - retrospective certainty laundering
  - timing fallacy
  - authenticity overgeneralization
  - media-agenda to vote-effect leap
  - partisan asymmetry

### MODULE_EXECUTION
NONE

### SCOPING_REPORT
- **cases:**
  - MacronLeaks 2017
  - DNC/Podesta 2016
  - Iran/Trump campaign 2024
- **chain:**
  - hack/theft
  - attribution
  - authenticity/alteration
  - timing
  - amplification
  - exposure
  - persuasion
  - outcome
- **exclusions:**
  - generic cyberespionage without leak/electoral purpose
  - mere publication of lawful opposition research
  - effect inferred from exposure alone
- **object:** Hack-and-leak / kompromat electoral interference
- **scope:** 2016–2026; France priority with US comparators

### CREDO
- hack != leak
- leak != falsification
- authentic document != legitimate operation
- timing != coordination
- publication != persuasion
- exposure != vote change
- official attribution != complete public proof
- earlier uncertainty != proof of absence
- indictment != conviction

### COGNITIVE_MAP
- **causal_boundary:** No winner-changing electoral effect is established for the scoped cases.
- **core_model:** Hack-and-leak effectiveness is a serial chain with multiple potential choke points; operational success and political success are different objects.
- **rival_models:**
  - ordinary leak by non-state actor
  - mixed authentic/fabricated corpus
  - successful theft but failed amplification
  - large media agenda effect without winner-changing vote effect
- **serial_edges:**
  - compromise
  - theft
  - provenance attribution
  - integrity
  - release timing
  - amplification
  - exposure
  - persuasion
  - outcome

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** theft, selective release and timing can themselves be manipulative without falsifying content
  - **resolution:** integrity and operational purpose must be graded separately
  - **thesis:** stolen authentic documents reveal real information
- **item 2:**
  - **antithesis:** contemporary evidence can have been insufficient even if later evidence strengthens attribution
  - **resolution:** time-stamp each attribution state
  - **thesis:** late attribution proves earlier suspicions were correct
- **item 3:**
  - **antithesis:** Macron 2017 and Iran 2024 show amplification can stall; US 2016 shows agenda effects without identified vote counterfactual
  - **resolution:** stop at highest supported edge
  - **thesis:** major exposure means election changed

### RESOURCE_FLOW_MAP
- **item 1:**
  - **classification:** HACK_AND_LEAK
  - **flow:** stolen/purported campaign data
  - **from:** Macron campaign mailboxes
  - **support:**
    - FCT-001
    - FCT-004
  - **to:** online leak ecosystem
- **item 2:**
  - **classification:** STATE_HACK_AND_LEAK
  - **flow:** stolen emails/documents
  - **from:** GRU-compromised DNC/Podesta accounts
  - **support:**
    - FCT-011
    - FCT-012
    - FCT-013
  - **to:** DCLeaks/Guccifer2.0/WikiLeaks
- **item 3:**
  - **classification:** ATTEMPTED_HACK_AND_LEAK
  - **flow:** unsolicited excerpts/documents
  - **from:** Trump campaign stolen material
  - **support:**
    - FCT-021
    - FCT-022
  - **to:** Biden-associated recipients + media

### ACTOR_NETWORK_MAP
- **item 1:**
  - **actor:** Macron campaign / unknown 2017 intruders / APT28-GRU 2025 attribution
  - **limits:**
    - whole-corpus integrity
    - public 2017 technical bridge
    - vote effect
  - **relation:** campaign compromise and leak; later official state attribution
  - **support:**
    - FCT-001
    - FCT-005
    - FCT-007
    - FCT-008
- **item 2:**
  - **actor:** GRU Units 26165/74455 -> DCLeaks/Guccifer2.0 -> WikiLeaks
  - **limits:**
    - October 7 trigger/coordination with Trump campaign
    - winner-changing effect
  - **relation:** hack/theft and staged dissemination chain
  - **support:**
    - FCT-011
    - FCT-012
    - FCT-013
    - FCT-014
    - FCT-017
- **item 3:**
  - **actor:** IRGC-linked actors -> Trump campaign material -> Biden associates/media
  - **limits:**
    - recipient uptake
    - mainstream publication
    - electoral effect
  - **relation:** 2024 hack-and-leak attempt
  - **support:**
    - FCT-020
    - FCT-021
    - FCT-022
- **item 4:**
  - **actor:** major newsrooms
  - **limits:**
    - direct social circulation bypasses gate
  - **relation:** secondary amplification gate
  - **support:**
    - FCT-003
    - FCT-018
    - FCT-023

### IMPACT_MAP
- **downstream:** INV-146 can compare ally/adversary language using isomorphic hack-and-leak chains; INV-137 can inspect how intelligence attribution becomes media certainty; INV-143 can reuse timing logic for institutional October-surprise cases.
- **measured_objects:**
  - intrusion/theft
  - publication timing
  - social/media amplification
  - publisher restraint
  - attribution evolution
- **not_established:**
  - whole-corpus integrity for MacronLeaks
  - winner-changing electoral effect in any scoped case
  - general causal effect of newsroom publication on vote choice

### CONTRADICTION_LEDGER
- **item 1:**
  - **early:** 2017/2018 no official attribution; generic attack caveat
  - **issue:** MacronLeaks Russian attribution
  - **later:** 2025 France officially attributes 2017 destabilization attempt to GRU/APT28
  - **resolution:** ATTRIBUTION_STRENGTHENED_OVER_TIME; PUBLIC_TECHNICAL_BRIDGE_STILL_LESS_DETAILED
- **item 2:**
  - **contra:** no complete public forensic authentication located
  - **issue:** MacronLeaks document falsification
  - **pro:** campaign said genuine and false mixed; commission warned some could be false
  - **resolution:** PARTIAL_NOT_QUANTIFIED
- **item 3:**
  - **contra:** Mueller did not establish Corsi caused release or Trump campaign conspiracy with Russia
  - **issue:** DNC October 7 timing
  - **pro:** release less than an hour after Access Hollywood; strategic timing elsewhere documented
  - **resolution:** TIMING_SUPPORTED; SPECIFIC_COORDINATION_NOT_ESTABLISHED
- **item 4:**
  - **contra:** IC explicitly did not assess outcome effect
  - **issue:** DNC electoral effect
  - **pro:** media agenda effects observed/argued
  - **resolution:** AGENDA_EFFECT_SUPPORTED; WINNER_EFFECT_UNRESOLVED
- **item 5:**
  - **contra:** no Biden recipient reply; major outlets withheld substantive publication
  - **issue:** Iran 2024 amplification
  - **pro:** material sent to campaigns/media
  - **resolution:** DELIVERY_ATTEMPT_SUPPORTED; UPTAKE_EFFECT_NOT_ESTABLISHED

### VERIFICATION_REPORT
- **checks:**
  - Macron attribution chronology preserved
  - campaign authenticity claim not promoted to whole-corpus fact
  - indictment status explicit
  - timing not converted to coordination
  - media agenda not converted to vote outcome
  - Iran Republican-target symmetry included
- **status:** PASS_PENDING_EXTERNAL_GATE

### EDI_REPORT
- **corpus:**
  - **circularity:** US DOJ/Mueller/Senate partly share investigative evidence; France Diplomatie and CERT-FR are same state ecosystem; media-agenda sources are separate academic families.
  - **counters:** 4
  - **coverage:** 0.93
  - **direct_objects:** 9
  - **edi_star:** 0.85
  - **independence:** 0.83
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 6
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES
    - **freshness:** HISTORICAL
    - **gap_type:** ACCESS
    - **independent_families:** 3
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** ATTRIBUTION
    - **independent_families:** 3
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** YES
    - **freshness:** HISTORICAL
    - **gap_type:** CAUSALITY
    - **independent_families:** 2
  - **item 5:**
    - **claim_id:** CLM-005
    - **direct_object:** YES
    - **freshness:** HISTORICAL
    - **gap_type:** NONE
    - **independent_families:** 4
  - **item 6:**
    - **claim_id:** CLM-007
    - **direct_object:** YES
    - **freshness:** HISTORICAL
    - **gap_type:** CAUSALITY
    - **independent_families:** 4
  - **item 7:**
    - **claim_id:** CLM-008
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** CAUSALITY
    - **independent_families:** 4
- **diagnostic_not_truth:** true
- **dimensions:**
  - **geo:** 0.9
  - **lang:** 0.92
  - **owner:** 0.9
  - **persp:** French control commission + French attribution + US criminal/intelligence records + academic/media controls
  - **strat:** 0.95
  - **temp:** 1.0
- **edi:**
  - **final:** 0.85
  - **flags:**
    - MACRON_WHOLE_CORPUS_INTEGRITY_UNRESOLVED
    - MACRON_2017_PUBLIC_TECHNICAL_BRIDGE_LIMITED
    - DNC_WINNER_EFFECT_UNRESOLVED
    - IRAN_2024_OUTCOME_UNRESOLVED
  - **penalties:** 0.06
  - **raw:** 0.91
- **source_counts:**
  - **primary:** 9
  - **secondary:** 7
  - **total:** 16

### RESPONSIBILITY_MAP
- **item 1:**
  - **claim:** MacronLeaks attribution 2017
  - **owner:** French state/ANSSI contemporary public record
  - **status:** UNATTRIBUTED_AT_TIME
  - **support:**
    - FCT-005
    - FCT-006
- **item 2:**
  - **caveat:** public CERT report linked to announcement focuses on 2021-2024 chains
  - **claim:** MacronLeaks attribution 2025
  - **owner:** France Diplomatie
  - **status:** OFFICIALLY_ATTRIBUTED_GRU_APT28
  - **support:**
    - FCT-007
- **item 3:**
  - **claim:** DNC hack/release
  - **owner:** US DOJ/Mueller/Senate
  - **status:** STRONG_PUBLIC_BASIS
  - **support:**
    - FCT-011
    - FCT-012
    - FCT-013
    - FCT-014
    - FCT-017
- **item 4:**
  - **claim:** Iran 2024 hack-and-leak
  - **owner:** US DOJ/ODNI-FBI-CISA/Microsoft
  - **status:** STRONG_PUBLIC_BASIS_WITH_INDICTMENT_STATUS
  - **support:**
    - FCT-020
    - FCT-021
    - FCT-022

### NEXT_QUERIES
- **item 1:**
  - **query:** MacronLeaks 2017 APT28 forensic attribution chain
  - **route:** RECHECK
  - **trigger:** new declassified/technical French 2017 evidence
- **item 2:**
  - **query:** IRGC Trump campaign hack-and-leak judicial outcome
  - **route:** RECHECK
  - **trigger:** new adjudication Iran 2024 defendants
- **item 3:**
  - **query:** compare terminology and evidence thresholds for Russian vs Iranian vs allied/domestic hack-and-leak
  - **route:** MERGE
  - **trigger:** INV-146
- **item 4:**
  - **query:** separate lawful procedure timing from strategic information release timing
  - **route:** MERGE
  - **trigger:** INV-143
- **item 5:**
  - **query:** more cases without new mechanism
  - **route:** DROP
  - **trigger:** generic additional hack cases

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021,FCT-022,FCT-023 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-006,QRY-007,QRY-008,QRY-009,QRY-013,QRY-014,QRY-016 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-014,FCT-015,FCT-016,FCT-021,FCT-022,FCT-023 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016 | support:- | counter:- | results:FCT-001,FCT-004,FCT-011,FCT-012,FCT-018,FCT-021,FCT-023 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016 | support:- | counter:- | results:FCT-005,FCT-006,FCT-007,FCT-008 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016 | support:- | counter:- | results:FCT-003,FCT-009,FCT-010 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016 | support:- | counter:- | results:FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-017 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016 | support:- | counter:- | results:FCT-016,FCT-018,FCT-019 | final:SATURATED | gap:NONE
AXS-007 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016 | support:- | counter:- | results:FCT-020,FCT-021,FCT-022,FCT-023 | final:SATURATED | gap:NONE
AXS-008 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016 | support:- | counter:- | results:FCT-003,FCT-018,FCT-023 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,QRY-007,QRY-011,QRY-013,QRY-016,SRC-001,SRC-007,SRC-011,SRC-013,SRC-016 | support:FCT-001,FCT-011,FCT-012,FCT-018,FCT-021,FCT-023 | counter:- | results:FCT-001,FCT-011,FCT-012,FCT-018,FCT-021,FCT-023 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-001,QRY-006,SRC-001,SRC-006 | support:FCT-001,FCT-002,FCT-004 | counter:No complete public forensic corpus-authentication report located. | results:FCT-001,FCT-002,FCT-004,No complete public forensic corpus-authentication report located. | final:PARTIAL | gap:ACCESS
CLM-003 | attempts:QRY-002,QRY-003,QRY-004,SRC-002,SRC-003,SRC-004 | support:FCT-005,FCT-006,FCT-007,FCT-008 | counter:Earlier non-attribution is not exculpatory proof; later political attribution is not the same object as a case-specific public technical report. | results:FCT-005,FCT-006,FCT-007,FCT-008,Earlier non-attribution is not exculpatory proof; later political attribution is not the same object as a case-specific public technical report. | final:SUPPORTED | gap:ATTRIBUTION
CLM-004 | attempts:QRY-001,QRY-005,SRC-001,SRC-005 | support:FCT-003,FCT-009,FCT-010 | counter:Online discussion volume was non-trivial and other scholarship argues election-blackout vulnerabilities. | results:FCT-003,FCT-009,FCT-010,Online discussion volume was non-trivial and other scholarship argues election-blackout vulnerabilities. | final:SUPPORTED | gap:CAUSALITY
CLM-005 | attempts:QRY-007,QRY-008,QRY-010,SRC-007,SRC-008,SRC-010 | support:FCT-011,FCT-012,FCT-013,FCT-014,FCT-017 | counter:Indictment allegations retain procedural status; attribution is reinforced by Mueller/Senate findings,not by the indictment alone. | results:FCT-011,FCT-012,FCT-013,FCT-014,FCT-017,Indictment allegations retain procedural status; attribution is reinforced by Mueller/Senate findings,not by the indictment alone. | final:SUPPORTED | gap:NONE
CLM-006 | attempts:QRY-007,QRY-008,SRC-007,SRC-008 | support:FCT-012,FCT-013,FCT-014,FCT-015 | counter:Temporal coincidence with Access Hollywood is not itself proof of coordinated timing with the Trump campaign. | results:FCT-012,FCT-013,FCT-014,FCT-015,Temporal coincidence with Access Hollywood is not itself proof of coordinated timing with the Trump campaign. | final:SUPPORTED | gap:COORDINATION
CLM-007 | attempts:QRY-009,QRY-011,QRY-012,SRC-009,SRC-011,SRC-012 | support:FCT-016,FCT-018,FCT-019 | counter:Jamieson argues some attitude/agenda changes should be credited to hacked-content coverage. | results:FCT-016,FCT-018,FCT-019,Jamieson argues some attitude/agenda changes should be credited to hacked-content coverage. | final:PARTIAL | gap:CAUSALITY
CLM-008 | attempts:QRY-013,QRY-014,QRY-015,QRY-016,SRC-013,SRC-014,SRC-015,SRC-016 | support:FCT-020,FCT-021,FCT-022,FCT-023 | counter:The criminal indictment remains allegations until adjudicated. | results:FCT-020,FCT-021,FCT-022,FCT-023,The criminal indictment remains allegations until adjudicated. | final:SUPPORTED | gap:CAUSALITY
CLM-009 | attempts:QRY-001,QRY-011,QRY-016,SRC-001,SRC-011,SRC-016 | support:FCT-003,FCT-018,FCT-023 | counter:Direct social distribution can bypass newsrooms. | results:FCT-003,FCT-018,FCT-023,Direct social distribution can bypass newsrooms. | final:SUPPORTED | gap:CAUSALITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-002 | CLM | PARTIAL | ACCESS | Whole-corpus integrity and exact falsified fraction remain unresolved.
CLM-003 | CLM | SUPPORTED | ATTRIBUTION | Publicly inspectable 2017 technical attribution chain remains less detailed than the 2025 state attribution statement.
CLM-004 | CLM | SUPPORTED | CAUSALITY | Individual-level persuasion and counterfactual vote effect not identified.
CLM-006 | CLM | SUPPORTED | COORDINATION | Exact causal trigger for October 7 WikiLeaks release remains unresolved in the scoped public record.
CLM-007 | CLM | PARTIAL | CAUSALITY | No clean counterfactual identifying winner-changing electoral effect.
CLM-008 | CLM | SUPPORTED | CAUSALITY | Persuasion/electoral effect not established.
CLM-009 | CLM | SUPPORTED | CAUSALITY | Cross-case causal effect of publisher restraint on vote choice not identified.
CAU-001 | CAU | UNRESOLVED | CAUSALITY | Exposure and agenda effects are observable in parts of the corpus, but no identified counterfactual connects the operation to a winner-changing vote shift.
CAU-002 | CAU | UNRESOLVED | CAUSALITY | Cross-case media behavior differs materially, but cases are not exchangeable and no scoped design identifies the causal vote effect of publication restraint.

SEMANTIC_COUNTS_V1:LED:2|CLM:9|AXS:8|CAU:2|CTRL:4|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016"],"evidence_excerpt":"OBJECT_QUESTION requires separating intrusion, attribution, integrity/alteration, timing, amplification and measurable electoral effect.","kind":"HYPOTHESIS","lead":"Hack-and-leak must be decomposed into theft/attribution, document integrity, release timing, amplification/exposure, persuasion and electoral outcome; proof can stop at any edge.","linked_ids":["AXS-001","AXS-002","AXS-003","AXS-004","AXS-005","AXS-006","AXS-007","AXS-008","CLM-001","CLM-002","CLM-003","CLM-004","CLM-005","CLM-006","CLM-007","CLM-008","CLM-009"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021","FCT-022","FCT-023"],"routes":["OBJECT_INVESTIGATION","MECHANISMS","COUNTER_HYPOTHESES"],"source_id":"INV-135_RUN_CARD","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-006","QRY-007","QRY-008","QRY-009","QRY-013","QRY-014","QRY-016"],"evidence_excerpt":"SCOPE requires hack, leak, possible falsification, publication, relays, exposure and effect to remain separate evidentiary objects.","kind":"METHOD_CONSTRAINT","lead":"Authenticity, attribution, strategic timing and effect are separate claims; later attribution may update an earlier uncertainty without retroactively making all contemporary allegations proven.","linked_ids":["CLM-001","CLM-002","CLM-003","CLM-004","CLM-005","CLM-006","CLM-007","CLM-008","CLM-009","CAU-001","CAU-002","CTRL-001","CTRL-002","CTRL-003","CTRL-004"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-014","FCT-015","FCT-016","FCT-021","FCT-022","FCT-023"],"routes":["RULES_CONTROLS","TEMPORAL_ATTRIBUTION"],"source_id":"INV-135_RUN_CARD","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"A hack-and-leak operation is not one claim but a chain: compromise/theft -> provenance/attribution -> document integrity -> release timing -> amplification/exposure -> reception/persuasion -> behavioral/electoral outcome; adjacent edges cannot inherit proof.","claimant":"INV-135 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-011","FCT-012","FCT-018","FCT-021","FCT-023"]}
CLM-002 | {"claim":"MacronLeaks 2017 is established as a late campaign data theft/leak event, but the public record inspected does not authenticate every item or quantify how much of the released corpus was altered; the campaign alleged genuine and false material were mixed and the election commission warned that some data could be false.","claimant":"INV-135 synthesis","counter":"No complete public forensic corpus-authentication report located.","gap":"Whole-corpus integrity and exact falsified fraction remain unresolved.","gap_type":"ACCESS","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-001","FCT-002","FCT-004"]}
CLM-003 | {"claim":"MacronLeaks attribution strengthened materially over time: the 2018 French strategic report described the attack as not officially attributed and technically generic, while France in 2025 officially stated that GRU use of APT28 had been employed in the 2017 electoral destabilization attempt; the public 2025 CERT report itself focuses on 2021-2024 infection chains rather than publishing the full 2017 forensic bridge.","claimant":"INV-135 synthesis","counter":"Earlier non-attribution is not exculpatory proof; later political attribution is not the same object as a case-specific public technical report.","gap":"Publicly inspectable 2017 technical attribution chain remains less detailed than the 2025 state attribution statement.","gap_type":"ATTRIBUTION","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-005","FCT-006","FCT-007","FCT-008"]}
CLM-004 | {"claim":"MacronLeaks achieved substantial online activity but the strongest scoped evidence indicates audience skew toward foreign/alt-right users; the French election commission concluded the episode did not impair the sincerity of the ballot, and no causal changed-vote estimate is identified.","claimant":"INV-135 synthesis","counter":"Online discussion volume was non-trivial and other scholarship argues election-blackout vulnerabilities.","gap":"Individual-level persuasion and counterfactual vote effect not identified.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-003","FCT-009","FCT-010"]}
CLM-005 | {"claim":"The 2016 DNC/Podesta hack-and-leak has a much stronger public operational chain than MacronLeaks: US investigative records identify GRU officers/units, theft methods, release personas and transfer/release of stolen materials.","claimant":"INV-135 synthesis","counter":"Indictment allegations retain procedural status; attribution is reinforced by Mueller/Senate findings, not by the indictment alone.","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-011","FCT-012","FCT-013","FCT-014","FCT-017"]}
CLM-006 | {"claim":"Strategic timing is strongly supported in the 2016 US case: stolen DNC material was sought/released just before the Democratic convention and Podesta material began on 7 October; however Mueller did not establish that intermediary efforts caused the October 7 release or that the Trump campaign conspired/coordordinated with the Russian government in the interference operation.","claimant":"INV-135 synthesis","counter":"Temporal coincidence with Access Hollywood is not itself proof of coordinated timing with the Trump campaign.","gap":"Exact causal trigger for October 7 WikiLeaks release remains unresolved in the scoped public record.","gap_type":"COORDINATION","materiality":"HIGH","status":"SUPPORTED","support":["FCT-012","FCT-013","FCT-014","FCT-015"]}
CLM-007 | {"claim":"The hacked Democratic material measurably entered and altered the US media agenda, but the reviewed evidence does not identify the counterfactual number of votes changed or whether the operation changed the election winner; the US Intelligence Community explicitly declined to assess outcome effect.","claimant":"INV-135 synthesis","counter":"Jamieson argues some attitude/agenda changes should be credited to hacked-content coverage.","gap":"No clean counterfactual identifying winner-changing electoral effect.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-016","FCT-018","FCT-019"]}
CLM-008 | {"claim":"The 2024 Iranian case reproduces the hack-and-leak mechanism against a Republican campaign: IRGC-linked intrusion activity and DOJ allegations support theft/disclosure intent, stolen Trump material was sent to Biden-associated individuals and media, but no recipient reply was recorded and major newsrooms withheld substantive publication.","claimant":"INV-135 synthesis","counter":"The criminal indictment remains allegations until adjudicated.","gap":"Persuasion/electoral effect not established.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-020","FCT-021","FCT-022","FCT-023"]}
CLM-009 | {"claim":"Publisher/platform response is a distinct control layer in hack-and-leak operations: French mainstream restraint in 2017 and US newsroom nonpublication in 2024 reduced secondary amplification compared with the intensive mainstream use of hacked Democratic material in 2016; reduced amplification still does not prove zero persuasion.","claimant":"INV-135 synthesis","counter":"Direct social distribution can bypass newsrooms.","gap":"Cross-case causal effect of publisher restraint on vote choice not identified.","gap_type":"CAUSALITY","materiality":"HIGH","status":"SUPPORTED","support":["FCT-003","FCT-018","FCT-023"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016"],"axis":"CHAIN_MODEL","links":["CLM-001"],"question":"Which links in hack→leak→amplification→effect require independent proof?","result_ids":["FCT-001","FCT-004","FCT-011","FCT-012","FCT-018","FCT-021","FCT-023"],"sought_objects":["CHAIN_MODEL"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016"],"axis":"MACRON_EVENT","links":["CLM-002"],"question":"What is actually established about theft, document integrity and release timing in MacronLeaks?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004"],"sought_objects":["MACRON_EVENT"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016"],"axis":"MACRON_ATTRIBUTION","links":["CLM-003"],"question":"How did attribution change from 2017/2018 uncertainty to the 2025 French position?","result_ids":["FCT-005","FCT-006","FCT-007","FCT-008"],"sought_objects":["MACRON_ATTRIBUTION"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016"],"axis":"MACRON_REACH_EFFECT","links":["CLM-004","CAU-001"],"question":"What exposure and electoral effect are supported?","result_ids":["FCT-003","FCT-009","FCT-010"],"sought_objects":["MACRON_REACH_EFFECT"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016"],"axis":"DNC_CHAIN","links":["CLM-005","CLM-006"],"question":"How strongly are hack, release channel and timing established for 2016 DNC/Podesta?","result_ids":["FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-017"],"sought_objects":["DNC_CHAIN"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016"],"axis":"DNC_EFFECT","links":["CLM-007","CAU-001","CAU-002"],"question":"What media agenda effects are observed and what electoral effect remains unresolved?","result_ids":["FCT-016","FCT-018","FCT-019"],"sought_objects":["DNC_EFFECT"],"status":"SATURATED"}
AXS-007 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016"],"axis":"IRAN_2024","links":["CLM-008"],"question":"Does a later hack-and-leak case reproduce the same chain and where does it stop?","result_ids":["FCT-020","FCT-021","FCT-022","FCT-023"],"sought_objects":["IRAN_2024"],"status":"SATURATED"}
AXS-008 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016"],"axis":"MEDIA_GATE","links":["CLM-009","CTRL-002"],"question":"Can publisher response materially alter amplification without proving persuasion?","result_ids":["FCT-003","FCT-018","FCT-023"],"sought_objects":["MEDIA_GATE"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"MacronLeaks showed limited domestic reach/media restraint; US IC explicitly did not assess 2016 winner effect; Iran 2024 publication gate differed.","gap":"Exposure and agenda effects are observable in parts of the corpus, but no identified counterfactual connects the operation to a winner-changing vote shift.","gap_type":"CAUSALITY","limit":"Requires individual-level or comparable exposure/outcome data and a defensible counterfactual capable of estimating a winner-changing vote shift.","mechanism":"Hack-and-leak operation -> exposure/reception -> changed political perception/vote -> electoral outcome","question":"Did any scoped hack-and-leak operation change enough individual votes to alter the election outcome?","status":"UNRESOLVED","support":["FCT-003","FCT-010","FCT-016","FCT-019","FCT-022","FCT-023"]}
CAU-002 | {"counter":"The scoped cases show materially different newsroom responses, but they differ simultaneously in election, actor, timing, content and context.","gap":"Cross-case media behavior differs materially, but cases are not exchangeable and no scoped design identifies the causal vote effect of publication restraint.","gap_type":"CAUSALITY","limit":"Requires a design that isolates publication/amplification from confounders; descriptive cross-case contrast cannot identify the causal vote effect.","mechanism":"Newsroom publication/restraint of stolen material -> exposure intensity/framing -> persuasion -> vote choice","question":"Did media publication or restraint causally mediate persuasion and vote choice in the scoped cases?","status":"UNRESOLVED","support":["FCT-003","FCT-018","FCT-019","FCT-023"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Macron temporal-attribution control: 2017/2018 uncertainty and 2025 official French GRU/APT28 attribution are both retained with their dates and evidence types; neither is allowed to erase the other.","status":"SUPPORTED","support":["FCT-005","FCT-006","FCT-007","FCT-008"]}
CTRL-002 | {"control":"Amplification control: Macron 2017 and Trump 2024 show that media restraint/nonpublication can break the leak→mainstream-amplification edge even when stolen material is available.","status":"SUPPORTED","support":["FCT-003","FCT-023"]}
CTRL-003 | {"control":"Outcome control: strong DNC operational attribution coexists with the Intelligence Community explicit refusal to assess election-outcome effect.","status":"SUPPORTED","support":["FCT-011","FCT-012","FCT-013","FCT-016"]}
CTRL-004 | {"control":"Symmetry control: the 2024 Iranian targeting of a Republican campaign is analyzed with the same separation of intrusion, stolen material, recipient response, media amplification and effect used for Russian/Democratic and Macron cases.","status":"SUPPORTED","support":["FCT-020","FCT-021","FCT-022","FCT-023"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:16|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"EMPTY","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | subject-fp lookup | MNEMO_Q
SYS-004 | SYS | OK | web | INV-135 | WEB_RESEARCH
SYS-005 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000036649861 | French election control commission final report 2017
QRY-002 | FETCH | FOUND | SRC-002 | https://www.diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/russie-attribution-de-cyberattaques-contre-la-france-au-service-de-renseignement-militaire-russe | France official APT28/GRU attribution 2025
QRY-003 | FETCH | FOUND | SRC-003 | https://www.cert.ssi.gouv.fr/cti/CERTFR-2025-CTI-006/ | CERT-FR APT28 technical report 2025
QRY-004 | FETCH | FOUND | SRC-004 | https://www.diplomatie.gouv.fr/IMG/pdf/les_manipulations_de_l_information_2__cle04b2b6.pdf | CAPS IRSEM information manipulation report
QRY-005 | FETCH | FOUND | SRC-005 | https://firstmonday.org/ojs/index.php/fm/article/download/8005/6516 | Ferrara MacronLeaks social bot study
QRY-006 | FETCH | FOUND | SRC-006 | https://www.euronews.com/2017/05/06/france-le-macronleaks-dernier-soubresaut-avant-le-second-tour-de-la | Macron campaign hack statement coverage
QRY-007 | FETCH | FOUND | SRC-007 | https://www.justice.gov/archives/sco/file/1080281/dl?inline= | DOJ Netyksho GRU indictment
QRY-008 | FETCH | FOUND | SRC-008 | https://www.justice.gov/storage/report_volume1.pdf | Mueller report Volume I
QRY-009 | FETCH | FOUND | SRC-009 | https://www.intelligence.senate.gov/2017/01/06/publications-assessing-russian-activities-and-intentions-recent-us-elections/ | US Intelligence Community assessment 2017
QRY-010 | FETCH | FOUND | SRC-010 | https://www.intelligence.senate.gov/2020/08/18/press-rubio-statement-senate-intel-release-volume-5-bipartisan-russia-report/ | Senate Intelligence Volume 5 release
QRY-011 | FETCH | FOUND | SRC-011 | https://cyber.harvard.edu/publications/2017/08/mediacloud | Berkman 2016 election media ecosystem report
QRY-012 | FETCH | FOUND | SRC-012 | https://academic.oup.com/book/39751/chapter-abstract/339810214 | Oxford hacked content press agenda chapter
QRY-013 | FETCH | FOUND | SRC-013 | https://www.justice.gov/usao-dc/pr/three-irgc-cyber-actors-indicted-hack-and-leak-operation-designed-influence-2024-us | DOJ Iranian hack-and-leak indictment 2024
QRY-014 | FETCH | FOUND | SRC-014 | https://archive.dni.gov/index.php/newsroom/press-releases/press-releases-2024/3994-odni-pr-22 | ODNI FBI CISA Iran stolen material statement
QRY-015 | FETCH | FOUND | SRC-015 | https://blogs.microsoft.com/on-the-issues/2024/08/08/iran-targeting-2024-us-election/ | Microsoft Iran election targeting 2024
QRY-016 | FETCH | FOUND | SRC-016 | https://www.pbs.org/newshour/politics/news-outlets-leaked-insider-material-taken-from-trump-campaign-they-chose-not-to-print-it | AP newsroom response to hacked Trump material

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:other:cnccep | CNCCEP-2017-FINAL | French election control commission final report 2017 | 2018-02-28 | 2026-09-06T16:45:00Z | MacronLeaks timing, possible false content, media restraint, sincerity of ballot | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000036649861
SRC-002 | ◈ | fam:other:france-diplomatie | FR-APT28-2025 | France official APT28/GRU attribution 2025 | 2025-04-29 | 2026-09-06T16:45:00Z | Official political attribution including 2017 electoral destabilization attempt | https://www.diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/russie-attribution-de-cyberattaques-contre-la-france-au-service-de-renseignement-militaire-russe
SRC-003 | ◈ | fam:other:anssi-certfr | CERTFR-APT28-2025 | CERT-FR APT28 technical report 2025 | 2025-04-29 | 2026-09-06T16:45:00Z | Technical APT28 campaigns 2021-2024; scope caveat for 2017 attribution | https://www.cert.ssi.gouv.fr/cti/CERTFR-2025-CTI-006/
SRC-004 | ◈ | fam:other:caps-irsem | CAPS-IRSEM-2018 | CAPS IRSEM information manipulation report | 2018-08-28 | 2026-09-06T16:45:00Z | 2017 MacronLeaks attribution evidence and uncertainty at the time | https://www.diplomatie.gouv.fr/IMG/pdf/les_manipulations_de_l_information_2__cle04b2b6.pdf
SRC-005 | ◈ | fam:other:first-monday | FERRARA-MACRONLEAKS-2017 | Ferrara MacronLeaks social bot study | 2017-07-31 | 2026-09-06T16:45:00Z | 17m tweet dataset; audience composition and limited French reach | https://firstmonday.org/ojs/index.php/fm/article/download/8005/6516
SRC-006 | ◈ | fam:other:euronews | EURONEWS-MACRONLEAKS-2017 | Macron campaign hack statement coverage | 2017-05-06 | 2026-09-06T16:45:00Z | Campaign acknowledgement of genuine and allegedly false documents | https://www.euronews.com/2017/05/06/france-le-macronleaks-dernier-soubresaut-avant-le-second-tour-de-la
SRC-007 | ◈ | fam:other:us-doj | DOJ-NETYKSHO-2018 | DOJ Netyksho GRU indictment | 2018-07-13 | 2026-09-06T16:45:00Z | GRU hack, transfer and timed publication allegations with detailed charging record | https://www.justice.gov/archives/sco/file/1080281/dl?inline=
SRC-008 | ◈ | fam:other:mueller-report | MUELLER-V1-2019 | Mueller report Volume I | 2019-04-18 | 2026-09-06T16:45:00Z | Russian hacking/releases findings and WikiLeaks timing/coordination boundaries | https://www.justice.gov/storage/report_volume1.pdf
SRC-009 | ◈ | fam:other:us-ic-senate | ICA-2017 | US Intelligence Community assessment 2017 | 2017-01-06 | 2026-09-06T16:45:00Z | IC attribution and explicit no-assessment of election outcome effect | https://www.intelligence.senate.gov/2017/01/06/publications-assessing-russian-activities-and-intentions-recent-us-elections/
SRC-010 | ◈ | fam:other:us-senate | SSCI-V5-2020 | Senate Intelligence Volume 5 release | 2020-08-18 | 2026-09-06T16:45:00Z | Bipartisan findings on Russian influence and WikiLeaks role | https://www.intelligence.senate.gov/2020/08/18/press-rubio-statement-senate-intel-release-volume-5-bipartisan-russia-report/
SRC-011 | ◈ | fam:other:harvard-berkman | BERKMAN-2017 | Berkman 2016 election media ecosystem report | 2017-08-16 | 2026-09-06T16:45:00Z | Media agenda and hacked-email coverage | https://cyber.harvard.edu/publications/2017/08/mediacloud
SRC-012 | ◈ | fam:other:oxford-academic | JAMIESON-2020 | Oxford hacked content press agenda chapter | 2020-08-20 | 2026-09-06T16:45:00Z | Argument that hacked content altered press agenda; not a vote-outcome experiment | https://academic.oup.com/book/39751/chapter-abstract/339810214
SRC-013 | ◈ | fam:other:us-doj | DOJ-IRGC-HACKLEAK-2024 | DOJ Iranian hack-and-leak indictment 2024 | 2024-09-27 | 2026-09-06T16:45:00Z | IRGC defendants alleged hack-and-leak targeting Trump campaign | https://www.justice.gov/usao-dc/pr/three-irgc-cyber-actors-indicted-hack-and-leak-operation-designed-influence-2024-us
SRC-014 | ◈ | fam:other:us-ic | US-IC-IRAN-2024 | ODNI FBI CISA Iran stolen material statement | 2024-09-18 | 2026-09-06T16:45:00Z | Stolen Trump material sent to Biden associates and media; no reply information | https://archive.dni.gov/index.php/newsroom/press-releases/press-releases-2024/3994-odni-pr-22
SRC-015 | ◈ | fam:other:microsoft-threat-intel | MSFT-IRAN-2024 | Microsoft Iran election targeting 2024 | 2024-08-08 | 2026-09-06T16:45:00Z | IRGC-linked spearphishing and cyber-enabled influence preparation | https://blogs.microsoft.com/on-the-issues/2024/08/08/iran-targeting-2024-us-election/
SRC-016 | ◈ | fam:other:associated-press | AP-HACKLEAK-MEDIA-2024 | AP newsroom response to hacked Trump material | 2024-08-13 | 2026-09-06T16:45:00Z | Major newsrooms received material but withheld substantive publication | https://www.pbs.org/newshour/politics/news-outlets-leaked-insider-material-taken-from-trump-campaign-they-chose-not-to-print-it

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000036649861 | other:cnccep | 2017-05-05 | MacronLeaks release timing and official response | The French election-control commission records that data presented as coming from Macron campaign email accounts were released on the evening of 5 May, in the final hours before the second-round campaign ended; the commission contacted ANSSI and prosecutors were seized. | -
FCT-002 | FACT | ✧ | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000036649861 | other:cnccep | 2017-05-06 | MacronLeaks possible-false-content warning | The commission warned that material circulating as campaign data could be partly false and urged media and citizens not to relay the contents during the statutory reserve period. | -
FCT-003 | FACT | ✧ | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000036649861 | other:cnccep | 2017-05-07 | MacronLeaks ballot-sincerity conclusion | The commission concluded that the very late release, accompanying discredit and restraint of major media limited the reach of the hack and that it had not impaired the sincerity of the presidential ballot. | -
FCT-004 | FACT | ✧ | https://www.euronews.com/2017/05/06/france-le-macronleaks-dernier-soubresaut-avant-le-second-tour-de-la | other:euronews | 2017-05-06 | Campaign claimed genuine and false material were mixed | Macron campaign statements acknowledged that at least some personal/professional emails were genuine while alleging that false documents or information were mixed into the release; this is a claimant statement, not a forensic authentication of the whole archive. | -
FCT-005 | FACT | ✧ | https://www.diplomatie.gouv.fr/IMG/pdf/les_manipulations_de_l_information_2__cle04b2b6.pdf | other:caps-irsem | 2017-06-01 | 2017 attribution remained officially unresolved | The 2018 CAPS/IRSEM report states France had not officially attributed the Macron attack and quotes ANSSI director Guillaume Poupard saying the attack was so generic and simple that it could have been anyone. | -
FCT-006 | FACT | ✧ | https://www.diplomatie.gouv.fr/IMG/pdf/les_manipulations_de_l_information_2__cle04b2b6.pdf | other:caps-irsem | 2017-05-01 | APT28 targeting clues were suggestive not dispositive | The CAPS/IRSEM report describes APT28-linked phishing attempts, Cyrillic metadata and other clues around MacronLeaks while explicitly noting that individual indicators did not prove Russian responsibility and could include false-flag possibilities. | -
FCT-007 | FACT | ✧ | https://www.diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/russie-attribution-de-cyberattaques-contre-la-france-au-service-de-renseignement-militaire-russe | other:france-diplomatie | 2025-04-29 | France later attributes 2017 destabilization attempt to GRU/APT28 | On 29 April 2025 France officially stated that GRU use of the APT28 intrusion set had also been employed in the attempted destabilization of the French electoral process in 2017. | -
FCT-008 | FACT | ✧ | https://www.cert.ssi.gouv.fr/cti/CERTFR-2025-CTI-006/ | other:anssi-certfr | 2025-04-29 | Public ANSSI technical report is focused on 2021-2024 APT28 campaigns | The CERT-FR report released with the 2025 attribution details APT28 infection chains observed between 2021 and 2024 and publicly links APT28 operators to Russia; its public text does not itself expose a case-specific 2017 MacronLeaks forensic chain. | -
FCT-009 | FACT | ✧ | https://firstmonday.org/ojs/index.php/fm/article/download/8005/6516 | other:first-monday | 2017-05-07 | MacronLeaks social discussion was large but audience skewed foreign | Ferrara analyzed nearly 17 million tweets and found the users who engaged with MacronLeaks were predominantly foreigners with pre-existing alt-right/alternative-news interests rather than a broad French-voter audience. | -
FCT-010 | FACT | ✧ | https://firstmonday.org/ojs/index.php/fm/article/download/8005/6516 | other:first-monday | 2017-05-07 | MacronLeaks bot/amplification evidence does not identify vote effect | Ferrara found coordinated/automated amplification patterns and argued the audience composition helps explain scarce success; this is exposure/engagement evidence, not a counterfactual estimate of changed votes. | -
FCT-011 | FACT | ✧ | https://www.justice.gov/archives/sco/file/1080281/dl?inline= | other:us-doj | 2016-07-01 | DNC/Clinton campaign hack attributed in indictment to GRU officers | The 2018 Netyksho indictment charges twelve GRU officers with spearphishing Clinton campaign personnel and hacking DNC/DCCC networks to steal emails and documents. | -
FCT-012 | FACT | ✧ | https://www.justice.gov/archives/sco/file/1080281/dl?inline= | other:us-doj | 2016-07-22 | DNC release was explicitly timed before Democratic convention | The indictment alleges the conspirators transferred stolen DNC material to Organization 1, which asked for material before the Democratic convention; over 20,000 emails/documents were released on 22 July, about three days before the convention. | -
FCT-013 | FACT | ✧ | https://www.justice.gov/archives/sco/file/1080281/dl?inline= | other:us-doj | 2016-10-07 | Podesta release formed a second timed dump | The indictment states Organization 1 released the first set of emails stolen from Clinton campaign chairman John Podesta on 7 October 2016 and continued releases through the eve of the election. | -
FCT-014 | FACT | ✧ | https://www.justice.gov/storage/report_volume1.pdf | other:mueller-report | 2019-04-18 | Mueller report establishes Russian hacking/release operation but not campaign conspiracy | The Mueller report describes the GRU hacking and dissemination operation as established Russian interference while stating the investigation did not establish that Trump campaign members conspired or coordinated with the Russian government in the interference activities. | -
FCT-015 | FACT | ✧ | https://www.justice.gov/storage/report_volume1.pdf | other:mueller-report | 2016-10-07 | Access Hollywood / Podesta temporal coincidence is established; causal coordination was not | Mueller records WikiLeaks releasing the first Podesta emails less than an hour after publication of the Access Hollywood tape, but the investigation did not establish that intermediary efforts described by Jerome Corsi caused that release. | -
FCT-016 | FACT | ✧ | https://www.intelligence.senate.gov/2017/01/06/publications-assessing-russian-activities-and-intentions-recent-us-elections/ | other:us-ic-senate | 2017-01-06 | US Intelligence Community did not assess electoral-outcome effect | The declassified US Intelligence Community assessment explicitly did not assess the impact of Russian activities on the outcome of the 2016 election and noted targeted/compromised election systems were not involved in vote tallying. | -
FCT-017 | FACT | ✧ | https://www.intelligence.senate.gov/2020/08/18/press-rubio-statement-senate-intel-release-volume-5-bipartisan-russia-report/ | other:us-senate | 2020-08-18 | Senate found WikiLeaks played key role in Russian influence campaign | The bipartisan Senate Intelligence Committee reported that Russia engaged in an aggressive multifaceted influence effort and that WikiLeaks played a key role and very likely knew it was assisting a Russian intelligence influence effort. | -
FCT-018 | FACT | ✧ | https://cyber.harvard.edu/publications/2017/08/mediacloud | other:harvard-berkman | 2016-11-08 | Hacked-email material materially entered the US media agenda | The Berkman Klein analysis of more than two million election stories found Clinton coverage heavily focused on scandals and emails and describes leaked DNC/Podesta material as a mechanism by which anti-Clinton narratives entered mainstream coverage. | -
FCT-019 | FACT | ✧ | https://academic.oup.com/book/39751/chapter-abstract/339810214 | other:oxford-academic | 2016-11-08 | Press-agenda effect is argued more strongly than vote-outcome effect | Jamieson argues regular releases of hacked material altered the press agenda in the final campaign weeks; the chapter is an agenda-setting analysis and does not provide a clean experimental counterfactual proving the election winner changed. | -
FCT-020 | FACT | ✧ | https://blogs.microsoft.com/on-the-issues/2024/08/08/iran-targeting-2024-us-election/ | other:microsoft-threat-intel | 2024-06-15 | Microsoft observed IRGC-linked spearphishing of a presidential campaign | Microsoft reported that an IRGC-connected actor sent a spearphishing email in June 2024 to a high-ranking official of a US presidential campaign from a compromised former-adviser account, as part of activity assessed as enabling election influence. | -
FCT-021 | FACT | ✧ | https://www.justice.gov/usao-dc/pr/three-irgc-cyber-actors-indicted-hack-and-leak-operation-designed-influence-2024-us | other:us-doj | 2024-09-27 | DOJ alleges IRGC hack-and-leak operation against Trump campaign | The DOJ indictment alleges three IRGC cyber actors conducted a sustained hack-and-leak operation to obtain non-public Trump campaign material and use it to influence the 2024 US presidential election; indictment allegations remain allegations until adjudicated. | -
FCT-022 | FACT | ✧ | https://archive.dni.gov/index.php/newsroom/press-releases/press-releases-2024/3994-odni-pr-22 | other:us-ic | 2024-09-18 | Stolen Trump material was sent to Biden associates and media with no recorded reply | ODNI/FBI/CISA said Iranian actors sent unsolicited excerpts of stolen non-public Trump campaign material to individuals associated with the Biden campaign and continued sending material to US media; there was no information that campaign recipients replied. | -
FCT-023 | FACT | ✧ | https://www.pbs.org/newshour/politics/news-outlets-leaked-insider-material-taken-from-trump-campaign-they-chose-not-to-print-it | other:associated-press | 2024-08-13 | Major US newsrooms withheld substantive publication of leaked Trump documents | Associated Press reported Politico, The New York Times and The Washington Post had received confidential Trump campaign material but had not disclosed its substantive contents, contrasting with the extensive mainstream use of hacked Democratic material in 2016. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-006
FCT-005 | SRC-004
FCT-006 | SRC-004
FCT-007 | SRC-002
FCT-008 | SRC-003
FCT-009 | SRC-005
FCT-010 | SRC-005
FCT-011 | SRC-007
FCT-012 | SRC-007
FCT-013 | SRC-007
FCT-014 | SRC-008
FCT-015 | SRC-008
FCT-016 | SRC-009
FCT-017 | SRC-010
FCT-018 | SRC-011
FCT-019 | SRC-012
FCT-020 | SRC-015
FCT-021 | SRC-013
FCT-022 | SRC-014
FCT-023 | SRC-016

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

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 LEADS | NEXT_ACTION:7 SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 SCOPE | NEXT_ACTION:9 SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 SEARCH | NEXT_ACTION:10 FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10 FACTS | NEXT_ACTION:11 CAUSAL_GAP
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 CAUSAL_GAP | NEXT_ACTION:13 VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 VERIFY | NEXT_ACTION:17 INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:18 FINALIZATION

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-06T16:53:16.973915+00:00","fact_mem":{},"mnemo_row":"BLOCKED:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":23,"eligible":23,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:BLOCKED:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:23;attempted:0;success:0;failure:0;blocked:23} | WRITEBACK_EXECUTION_V1:[23 rows, see section]

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
