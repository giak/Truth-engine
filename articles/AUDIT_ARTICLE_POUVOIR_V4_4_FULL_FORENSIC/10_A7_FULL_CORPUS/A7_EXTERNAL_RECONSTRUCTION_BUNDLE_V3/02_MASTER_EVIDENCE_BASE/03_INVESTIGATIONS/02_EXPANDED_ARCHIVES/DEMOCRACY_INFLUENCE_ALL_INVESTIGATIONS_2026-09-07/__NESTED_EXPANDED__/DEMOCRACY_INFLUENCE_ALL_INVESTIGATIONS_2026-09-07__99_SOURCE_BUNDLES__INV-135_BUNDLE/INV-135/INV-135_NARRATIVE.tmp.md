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
