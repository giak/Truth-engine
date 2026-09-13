ENGINE:2.10.6 | BUNDLE_REVISION:R2A.2 | STATE:FINAL | RUN_ID:20260905-2037-inv010-r2 | PARENT_RUN_ID:NONE | AS_OF:2026-09-05
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/TE_CANONICAL_RUNS/engine/truth-engine-v2_2.10.6-RC_R2A2P1_CANONICAL/investigations/2026-09/2026-09-05_cia-elections-etrangeres/2026-09-05_20-37_cia-elections-etrangeres_INPUT.txt | SUBJECT_SLUG:cia-elections-etrangeres | SUBJECT_FP:sha256:d710b78dd68af3fe4cd940a3bb0e95933a3b7025186d5f54cdfc4e21482ce9dc | INPUT_SHA256:sha256:8faa51cd076286a9f8a520c4b6ac3261006ed1fdd6cde8ab869af81627b34c5e
COMPLEXITY:14→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': 'US government; CIA; State Department; Italian parties; Chilean parties; local intermediaries', 'domains': 'élections; action clandestine; aide; propagande; financement; diplomatie; déstabilisation', 'exclusions': 'pas d’extrapolation contemporaine; ne pas confondre influence électorale et changement de régime', 'geo': 'Italie; Chili; autres cas seulement si discriminants', 'lead_question': 'Les États-Unis, notamment via la CIA, ont-ils tenté d’influencer des élections étrangères entre 1945 et 1975 ?', 'limits': 'sources déclassifiées et littérature indépendante accessibles', 'object_question': 'Dans quels cas historiquement documentés les États-Unis ont-ils matériellement tenté d’influencer des élections étrangères, par quels mécanismes, et jusqu’à quel niveau I0..I7 les effets sont-ils démontrables ?', 'period': '1945-1975'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
## 1. RÉSUMÉ EXÉCUTIF

### Question d’objet

Cette enquête examine trois cas documentés, l’Italie en 1948 et le Chili en 1964 puis 1970, pour répondre à une question plus précise que « les États-Unis ont-ils pratiqué l’ingérence électorale ? » : **quelles opérations ont été réellement décidées et exécutées, par quels mécanismes, avec quelles chaînes d’autorité et de ressources, et jusqu’où peut-on démontrer leurs effets sur les électeurs et sur le résultat politique ?**

Le premier résultat est solide. Dans les trois cas, l’existence de tentatives américaines visant matériellement le processus électoral ou l’accession au pouvoir est établie par des archives officielles américaines inspectables. En Italie, NSC 1/3 du 8 mars 1948 fait explicitement de l’empêchement d’une participation communiste issue des élections une priorité et prescrit des moyens économiques, informationnels et politiques [FCT-001; SRC-001]. Un document postérieur du NSC parle sans détour d’« opérations clandestines improvisées » menées au moment de l’élection italienne [FCT-003; SRC-004]. Au Chili en 1964, les documents de la CIA et du Special Group montrent des programmes de financement, d’organisation et de propagande destinés à faire battre Salvador Allende et à renforcer Eduardo Frei, avec 750 000 dollars proposés en avril, 1,25 million supplémentaire approuvé en mai, et environ 3 millions de dollars approuvés au total selon le rapport CIA de 2000 [FCT-006; FCT-007; FCT-008]. Au Chili en 1970, une opération de propagande anti-Allende est documentée avant le scrutin, puis Track II vise explicitement à provoquer un coup d’État avant l’accession d’Allende [FCT-012; FCT-015; FCT-016].

Le deuxième résultat est tout aussi important : **l’existence d’une opération est beaucoup mieux démontrée que son efficacité causale**. Les archives d’opérateurs prouvent les objectifs, les budgets, les autorisations et certaines actions, mais elles ne constituent pas à elles seules un contrefactuel électoral. En Italie en 1948, l’intervention américaine est établie, mais des travaux indépendants décrivent une campagne américaine improvisée et non unifiée, tandis que les réseaux catholiques, la stratégie de De Gasperi et la dynamique interne de la Démocratie chrétienne fournissent des causes domestiques substantielles [FCT-005; SRC-005; SRC-020; SRC-022]. Aucun document inspecté ne permet d’établir que le Front populaire aurait gagné sans intervention américaine. Le niveau I7, « changement du vainqueur », reste donc non identifié.

Au Chili en 1964, l’appui clandestin à Frei est encore plus massif et mieux documenté [FCT-006 à FCT-008]. Les responsables américains le décrivent rétrospectivement comme indispensable ou décisif [FCT-010], mais cette appréciation est une auto-évaluation d’opérateur. Labarca montre indépendamment que la majorité de Frei repose également sur une organisation démocrate-chrétienne autonome, une mobilisation rurale et sociale et l’intégration de nombreux nouveaux électeurs [FCT-011; SRC-010]. L’intervention américaine a donc créé des capacités et une exposition supplémentaires, mais le déplacement marginal de voix et le contrefactuel du vainqueur restent non identifiables. I5 est soutenu qualitativement; I6 reste non résolu; I7 n’est pas établi.

Le Chili de 1970 fournit un test particulièrement instructif. L’opération anti-Allende n’empêche pas Allende d’arriver en tête du vote populaire avec environ 36,3 %, devant Alessandri à environ 34,9 % [FCT-013]. L’objectif immédiat de l’opération électorale, empêcher cette première place, échoue [CAU-006]. Après le scrutin, la politique change de nature : Track II vise une intervention militaire avant l’investiture [FCT-015; FCT-016]. La CIA établit des contacts, encourage des complots et fournit du matériel à certains groupes [FCT-017]. Mais le dossier public inspecté ne permet pas d’attribuer à la CIA l’intention de tuer le général René Schneider ni l’ensemble des actions autonomes des comploteurs chiliens. Le coup recherché avant l’accession échoue lui aussi [CAU-008].

La conclusion probatoire est donc graduée. **I0 à I3 sont solidement démontrés dans les trois cas** : acteurs, ressources, actions et, pour plusieurs chaînes, autorisation ou coordination. **I4 est démontré de façon partielle à forte selon le mécanisme**, notamment lorsque des campagnes de propagande et des infrastructures de diffusion sont documentées, mais l’exposition individuelle n’est pas reconstruite. **I5 est soutenu qualitativement au Chili en 1964 mais non isolé quantitativement. I6 et I7 restent non résolus pour l’Italie 1948 et le Chili 1964.** Pour le Chili 1970, l’échec de l’objectif immédiat est observable. La règle qui résiste à l’ensemble de l’enquête est donc : `ACTION != EXPOSURE != PERSUASION != BEHAVIOR_CHANGE != WINNER_CHANGE`.

### Verdict du lead et verdict de l’objet

Le lead « les États-Unis, notamment via la CIA, ont tenté d’influencer des élections étrangères » est **confirmé** pour les cas étudiés. L’assertion plus forte « ces opérations ont changé le vainqueur » ne l’est pas pour l’Italie 1948 ni le Chili 1964. Le cas chilien de 1970 montre même que l’existence d’une opération importante peut coexister avec l’échec de son objectif électoral immédiat.

## 2. MANIPULATION_REPORT

Le sujet est classé APEX avec un score de complexité 14. Les quinze dimensions du moteur ont été évaluées sur le corpus final, et non sur l’énoncé utilisateur. Les scores servent à router l’examen, jamais à prouver une hypothèse.

| Symbole | Score | Observation bornée |
|---|---:|---|
| ⚔ | 9 | Des opérations organisées, autorisées et clandestines sont directement documentées. |
| 🌐 | 9 | Les chaînes Maison-Blanche/NSC/CIA/State/ambassades/partis/médias/militaires sont documentées par des arêtes typées. |
| € | 8 | Fonds clandestins, aide économique, budgets de propagande et soutien matériel sont centraux. |
| ↕ | 8 | Forte asymétrie de ressources financières, diplomatiques, informationnelles et de renseignement. |
| ⏰ | 8 | Les actions sont séquencées autour des fenêtres électorales et, en 1970, de la confirmation congressionnelle. |
| ⫸ | 8 | Budgets, autorisations, calendrier et partenariats convergent à l’intérieur d’opérations bornées. |
| Λ | 7 | Le cadrage anticommuniste structure les objectifs et une partie de la communication. |
| κ | 7 | Aide conditionnelle, propagande ciblée et soutien organisationnel visent explicitement à orienter le choix. |
| Ξ | 6 | La déclassification incomplète et l’auto-évaluation des opérateurs limitent l’observabilité de l’effet. |
| Ψ | 6 | Des campagnes de peur/urgence sont documentées, surtout au Chili en 1964; leur effet doit rester séparé de l’intention. |
| ρ | 4 | Partis, Église, électeurs et institutions nationales conservent une agence matérielle. |
| Κ | 3 | Des zones de déni plausible existent, mais elles ne suffisent pas à établir un cynisme généralisé. |
| Σ | 2 | Les symboles et marques sont secondaires aux flux matériels. |
| Φ | 2 | Le spectacle n’est pas un mécanisme central démontré. |
| Ω | 2 | Une inversion systématique du blâme n’est pas nécessaire pour expliquer les cas. |

Clusters effectivement chargés : ICEBERG, MONEY, FRAMING, OVERLOAD, POWER, CONFIRMATION, FRAGMENTATION, WAR, NETWORK, TEMPORAL, ainsi que la branche `forensic/REASONING.md`. Leur convergence ne constitue pas une preuve de coordination globale; elle indique seulement les angles d’audit appliqués.

## 3. CLUSTERS

### MONEY / POWER / NETWORK

Le cluster financier est directement activé au Chili en 1964. Les documents américains montrent une chaîne de décision puis de ressources : Special Group/303 Committee → CIA/ambassade → Frei/PDC et groupes auxiliaires, avec des montants explicitement approuvés [FCT-006; FCT-007; FCT-008]. La présence de fonds ne prouve pas à elle seule le contrôle du bénéficiaire; elle prouve une capacité additionnelle et une relation de soutien. C’est pourquoi l’arête CIA → Frei/PDC est typée `ASSISTED`, et non `COMMANDED`.

En Italie en 1948, la ressource n’est pas seulement monétaire. Elle comprend l’accès à l’aide économique, la diplomatie publique et la capacité clandestine [FCT-001 à FCT-003]. L’effet d’une menace ou d’une promesse d’aide sur un électeur individuel n’est pas observable dans les sources consultées. Le mécanisme est donc un `ENABLER` de l’environnement de campagne, pas une preuve de conversion électorale.

### FRAMING / TEMPORAL / WAR

Les politiques étudiées sont structurées par le cadre de la guerre froide. NSC 1/3 définit la victoire communiste en Italie comme un risque stratégique; les opérations chiliennes visent Allende comme menace politique et géostratégique. Ce cadrage explique l’objectif institutionnel et le calendrier mais ne démontre pas que la représentation du danger était factuellement exacte ni que tous les acteurs locaux partageaient le même modèle causal.

La dimension temporelle est décisive en 1970. Avant le vote, l’action est principalement électorale et informationnelle [FCT-012]. Après la pluralité d’Allende, le centre de gravité se déplace vers le Congrès, l’armée et la possibilité d’un coup avant l’investiture [FCT-015; FCT-016]. Confondre les deux périodes ferait disparaître une rupture causale essentielle.

### ICEBERG / CONFIRMATION

Les archives déclassifiées montrent qu’une partie des mécanismes n’était pas visible publiquement au moment des faits. Cela justifie une recherche de couches cachées, mais pas une présomption que tout événement non expliqué procède d’une action clandestine. Le biais de confirmation est particulièrement dangereux lorsqu’un document d’opérateur qualifie sa propre action de « succès ». Les auto-évaluations CIA ont donc été conservées comme faits sur ce que l’agence affirmait, et non comme preuve indépendante de l’effet sur le vote [FCT-010].

### Explication concurrente la plus forte

L’explication concurrente n’est pas « il n’y a eu aucune intervention ». Cette hypothèse est incompatible avec les archives. La concurrence sérieuse porte sur le **poids causal**. En Italie : mobilisation catholique, stratégie de De Gasperi, économie et dynamique partisane [FCT-005]. Au Chili 1964 : organisation autonome du PDC, expansion vers des électorats ruraux et nouveaux, coalition politique [FCT-011]. Ces explications ne réfutent pas l’intervention; elles empêchent de lui attribuer sans preuve le résultat entier.

## 4. HERMÉNEUTIQUE

### L1 — explicite

Les documents les plus forts explicitent des intentions opérationnelles. NSC 1/3 demande d’empêcher une issue communiste en Italie et décrit plusieurs leviers [FCT-001]. Au Chili 1964, la CIA propose des fonds et des opérations de propagande pour battre Allende et renforcer Frei [FCT-006]. En 1970, Track II vise explicitement un coup avant l’accession d’Allende [FCT-016].

### L2 — implicite

Ces dispositifs supposent que des ressources étrangères peuvent modifier la capacité de campagne, la perception du risque ou la décision d’acteurs institutionnels. Cette hypothèse est plausible mais ne peut pas être confondue avec une mesure d’effet. Les archives d’autorisation n’offrent généralement ni groupe de contrôle ni estimation du nombre de voix déplacées.

### L3 — structurel

Le conflit est organisé par deux catégories concurrentes : sécurité anticommuniste pour les décideurs américains, souveraineté électorale pour l’État cible. La première structure la justification de l’intervention; la seconde permet d’évaluer sa portée institutionnelle sans présupposer son efficacité.

### L4 — symbolique

Au Chili 1964, la propagande de peur utilise un registre symbolique anticommuniste documenté dans les archives et la littérature. Ce symbolisme est un véhicule de persuasion, pas une preuve de persuasion effective de chaque électeur. L’intention de faire peur et l’effet de la peur restent deux propositions différentes.

### L5 — présupposé

Les décideurs américains présupposent à plusieurs reprises qu’une victoire de la gauche alignée ou perçue comme alignée sur Moscou menacerait les intérêts américains. Cette vision justifie l’action dans leurs propres documents. L’enquête ne traite pas ce présupposé géopolitique comme une vérité indépendante.

### L6 — épistémique

La connaissance disponible est asymétrique. Les archives américaines sont exceptionnellement fortes pour documenter les décisions américaines parce qu’elles ont été déclassifiées. Elles sont beaucoup moins fortes pour mesurer l’expérience des électeurs italiens ou chiliens. Cette asymétrie explique pourquoi l’intention et l’action atteignent des niveaux probatoires supérieurs à l’impact.

## 5. FORENSIC REASONING

La branche forensique a été requise par la complexité et l’existence de zones déclassifiées incomplètes. Trois catégories ont été maintenues séparées : `FOUND`, `ESTIMATED`, `UNKNOWN`.

### FOUND

Sont trouvés directement : NSC 1/3 et ses prescriptions électorales [FCT-001]; la référence officielle à des opérations clandestines en Italie [FCT-003]; les budgets et objectifs de la campagne CIA au Chili 1964 [FCT-006 à FCT-008]; le résultat du scrutin chilien de 1970 [FCT-013]; le lancement de Track II et la recherche d’un coup [FCT-015; FCT-016]; la fourniture de matériel à certains comploteurs [FCT-017].

### ESTIMATED

La portée exacte de certaines campagnes de propagande est partiellement reconstituée à partir de documents d’opérateur. Le rôle de ces campagnes dans la marge finale de Frei est au mieux estimable qualitativement, pas quantifiable de manière crédible avec le corpus inspecté.

### UNKNOWN

Restent inconnus : le nombre de voix déplacées en Italie en 1948; l’identité du vainqueur dans un monde sans intervention américaine; le déplacement marginal de voix causé par la campagne américaine au Chili 1964; le degré de connaissance de chaque bénéficiaire local concernant l’ensemble des canaux clandestins; toute éventuelle pièce encore classifiée susceptible de modifier la frontière de responsabilité autour de Schneider.

### Preuve silencieuse

Aucune absence documentaire n’est utilisée pour prouver un complot, une intention ou une non-occurrence. Le dossier public incomplet est traité comme une limite d’accès. Là où un mécanisme clandestin est affirmé, il repose sur un objet déclassifié positif, pas sur « l’absence de preuve visible ».

## 6. PRISME DIALECTIQUE

### P1 — compte institutionnel dominant

Le meilleur argument institutionnel est que les États-Unis agissaient dans un contexte de guerre froide pour empêcher l’expansion de forces communistes ou perçues comme soutenues par l’Union soviétique. De ce point de vue, l’aide à des forces anticommunistes, l’information publique et certaines actions clandestines sont conçues comme une défense de l’équilibre stratégique et, parfois, de partis pluralistes menacés.

Ce récit est réellement présent dans les documents. Il explique les motivations déclarées et les structures d’autorisation. Son falsificateur serait la découverte de documents montrant que les objectifs réels n’avaient aucun rapport avec les risques décrits ou que les opérations alléguées n’ont jamais existé. Les archives consultées réfutent la seconde possibilité mais ne permettent pas de trancher toutes les motivations.

### P2 — compte critique

Le meilleur argument critique est que les États-Unis ont utilisé leur puissance économique, diplomatique et clandestine pour altérer des choix politiques qui appartenaient aux électeurs et institutions d’États souverains. L’Italie 1948 combine aide, information et action clandestine. Le Chili 1964 combine financement secret, propagande et soutien organisationnel. Le Chili 1970 franchit une étape supplémentaire lorsque la politique cherche un coup avant l’accession d’un candidat arrivé en tête.

Ce récit est fortement soutenu sur l’existence et la nature des actions. Il devient plus fragile lorsqu’il transforme l’intention d’influencer en preuve que le résultat a effectivement été déterminé.

### P3 — arbitrage probatoire

L’arbitrage est donc asymétrique. La critique est forte sur l’action et la souveraineté; le compte institutionnel est pertinent pour expliquer le cadre stratégique; aucun des deux ne dispose d’un droit automatique sur le contrefactuel électoral. Pour l’Italie et le Chili 1964, l’enquête s’arrête avant I7. Pour le Chili 1970, l’échec de l’objectif électoral immédiat et de Track II avant l’accession est observable.

Convergence : tous les récits sérieux acceptent que le contexte national compte. Divergence : poids moral et causal attribué à l’intervention. Non résolu : effet marginal sur le vote dans les deux premiers cas.

## 7. CHRONOLOGIE

| Date | Événement | Statut |
|---|---|---|
| 8 mars 1948 | NSC 1/3 définit l’empêchement d’une issue communiste par l’élection italienne comme priorité et prescrit plusieurs leviers [FCT-001]. | Vérifié |
| 20 mars 1948 | Les déclarations de Marshall sur l’aide sont perçues en Italie comme conditionnelles au résultat électoral [FCT-002]. | Probable / source officielle unique |
| 18 avril 1948 | La Démocratie chrétienne obtient environ 48,5 % et une majorité absolue de sièges [FCT-004]. | Probable |
| 12 mai 1948 | NSC 10 fait référence aux opérations clandestines improvisées menées au moment des élections italiennes [FCT-003]. | Vérifié |
| 1 avril 1964 | La CIA propose 750 000 dollars pour financement politique et propagande anti-Allende/pro-Frei [FCT-006]. | Probable |
| 14 mai 1964 | Le Special Group approuve 1,25 million supplémentaire [FCT-007]. | Vérifié |
| 4 septembre 1964 | Frei gagne avec environ 56 %, Allende environ 39 % [FCT-009]. | Probable |
| septembre 1964 | Les responsables américains attribuent une forte efficacité à leur propre opération [FCT-010]. | Fait sur l’auto-évaluation, pas sur le contrefactuel |
| 18 juin 1970 | La CIA planifie une opération de spoiling anti-Allende [FCT-012]. | Probable |
| 4 septembre 1970 | Allende arrive en tête du vote populaire; l’objectif immédiat anti-Allende n’est pas atteint [FCT-013; CAU-006]. | Probable / causalité de l’échec observable |
| septembre-octobre 1970 | La politique se déplace vers l’empêchement de l’accession et la recherche d’un coup [FCT-015; FCT-016]. | Vérifié/Probable selon proposition |
| octobre 1970 | Des contacts et soutiens matériels à des groupes de comploteurs sont documentés [FCT-017]. | Probable |
| 24 octobre 1970 | Le Congrès chilien confirme Allende malgré Track II [CTRL-005]. | Soutenu |

## 8. DOMAINES

### Politique électorale

Les trois cas prouvent une intervention étrangère intentionnelle dans un processus électoral ou son issue institutionnelle. Les modes diffèrent : environnement économique et politique en Italie; financement et propagande au Chili 1964; spoiling puis coup au Chili 1970.

### Finance et ressources

Le Chili 1964 est le cas le plus quantifié. Les budgets approuvés et les finalités sont directement documentés [FCT-006 à FCT-008]. En Italie, le dossier inspecté confirme l’existence d’une action clandestine et d’un levier d’aide, sans produire un total monétaire homogène comparable.

### Information et propagande

La propagande n’est pas un simple appendice. Elle est explicitement intégrée aux plans italiens et chiliens. Mais la chaîne vers la persuasion mesurée demeure incomplète. On observe l’émission et une partie de la capacité de diffusion; on n’observe pas un traitement causal individualisé.

### Diplomatie et économie

En Italie, le lien entre l’aide américaine et le résultat électoral est utilisé publiquement comme levier [FCT-002]. Il s’agit d’une forme de pression ou de signal économique qui agit sur l’environnement décisionnel sans nécessiter une opération clandestine.

### Renseignement et action clandestine

Les opérations clandestines sont explicitement documentées. Elles incluent financement, organisation, propagande et, en 1970, contacts militaires et soutien matériel. La clandestinité modifie l’imputabilité publique mais ne dispense pas l’enquête de distinguer soutien, coordination et commandement.

### Droit et souveraineté

L’enquête n’attribue pas automatiquement une qualification pénale contemporaine à des faits historiques relevant de cadres juridiques différents. Le constat institutionnel est plus simple : des organes américains ont cherché à modifier des choix relevant des électeurs et institutions italiennes ou chiliennes.

### Effets

C’est le domaine le moins résolu. Les données montrent des résultats électoraux, mais pas ce qu’ils auraient été sans intervention. Une opération peut être massive et échouer sur son objectif immédiat, comme en 1970.

## 9. RÉSEAU D’ACTEURS

Le réseau n’est pas une carte d’associations vagues; seules les arêtes documentées sont retenues.

**Italie 1948.** Le président Truman et le NSC autorisent et coordonnent des mesures exécutives [ACT-001; CTRL-001]. State et d’autres agences mettent en œuvre des leviers publics. La CIA et des canaux américains apportent une assistance politique clandestine à des forces anticommunistes [FCT-003]. En parallèle, les réseaux catholiques italiens mobilisent indépendamment pour la Démocratie chrétienne [FCT-005]. La relation entre Washington et la DC est donc un soutien documenté, pas une preuve de commandement de la DC.

**Chili 1964.** Special Group/303 autorise les opérations [CTRL-002]. CIA et ambassade servent de canaux opérationnels. Frei/PDC et des groupes auxiliaires reçoivent des capacités supplémentaires [ACT-002]. Mais le PDC possède également sa propre infrastructure militante, ses propres objectifs et ses propres mécanismes de mobilisation [ACT-003; FCT-011].

**Chili 1970.** Le 40 Committee autorise le spoiling [CTRL-003]. Après le vote, Nixon et la direction CIA poussent Track II [ACT-004; CTRL-004]. La CIA contacte des groupes de comploteurs chiliens; ces groupes conservent une agence propre [ACT-005]. Le Congrès chilien constitue une contre-force institutionnelle et confirme Allende [CTRL-005].

La centralité américaine est forte dans la chaîne de ressources et d’autorisation des opérations américaines. Elle ne signifie pas centralité causale unique dans l’ensemble du système politique cible.

## 10. CHAÎNES / PELOTE

### PELOTE A — Italie 1948

`Perception stratégique d’un risque communiste` → `NSC 1/3` → `leviers économiques, informationnels et politiques` → `soutien public et clandestin aux forces anticommunistes` → `capacité de campagne/environnement informationnel modifiés` → `résultat DC 48,5 %`.

Les liens jusqu’à la modification des capacités sont soutenus [CAU-001; CAU-002]. Le dernier lien, « intervention américaine → identité du vainqueur », ne survit pas au test causal : les causes nationales sont fortes et aucun contrefactuel crédible n’isole l’intervention [CAU-003].

### PELOTE B — Chili 1964

`Objectif battre Allende` → `Special Group/303` → `fonds + organisation + propagande` → `Frei/PDC et groupes auxiliaires disposent de capacités supplémentaires` → `audience exposée à une campagne anti-Allende/pro-Frei` → `Frei 56 %`.

Les maillons ressources/capacités sont documentés [CAU-004]. Le passage exposition → votes supplémentaires reste non isolé [CAU-005]. La CIA affirme que son soutien fut indispensable [FCT-010]; l’analyse indépendante révèle une mobilisation domestique concurrente [FCT-011].

### PELOTE C — Chili 1970, scrutin

`Objectif empêcher Allende` → `spoiling anti-Allende` → `propagande et recherche de quelques voix critiques` → `Allende arrive néanmoins premier`.

Ici, l’objectif observable échoue. La chaîne « spoiling → empêcher la première place » est réfutée par le résultat [CAU-006]. Cela n’implique pas que la campagne n’a déplacé aucune voix; cela signifie qu’elle n’a pas atteint le résultat politique recherché.

### PELOTE D — Chili 1970, accession

`Allende arrive premier` → `objectif empêcher accession` → `Track II / recherche d’un coup` → `contacts militaires et soutien matériel` → `complots locaux` → `Congrès confirme Allende`.

Track II est un enabler du coup-planning [CAU-007], mais le résultat « empêcher l’accession » échoue [CAU-008]. La responsabilité américaine est démontrée pour l’encouragement et certains soutiens, pas pour chaque action autonome des groupes chiliens.

### Couverture causale

Les quatre chaînes expliquent les principaux faits de mécanisme. Les gaps portent sur les effets marginaux des campagnes électorales en 1948 et 1964, non sur l’existence des opérations.

## 11. CARTE DES PREUVES

### Couverture des leads

| Lead | Route | Résultat |
|---|---|---|
| LED-001 Italie 1948 | EXPAND/LINK | SATURATED; FCT-001 à FCT-005 |
| LED-002 Chili 1964 | EXPAND/LINK | SATURATED; FCT-006 à FCT-011 |
| LED-003 Chili 1970 | EXPAND/LINK | SATURATED; FCT-012 à FCT-018 |
| LED-004 séparation action/effet | LINK | SATURATED par les chaînes causales et gaps |
| LED-005 influence électorale vs régime | LINK/CONTEXT | SATURATED; rupture 1970 explicitée |

### Couverture de l’objet

Les axes source, histoire, cas, ressources, mécanismes, acteurs, contrôles et contre-hypothèses sont saturés dans le périmètre. L’axe impact/responsabilité est terminal en `GAP_TYPE=CAUSALITY` pour les contrefactuels Italie 1948 et Chili 1964.

### Claims décisifs

- CLM-001 : politique américaine explicitement électorale en Italie, SUPPORTED.
- CLM-002 : mesures overt/covert ont matériellement modifié la campagne, SUPPORTED.
- CLM-003 : changement du vainqueur italien, GAP causal.
- CLM-004 : action clandestine américaine en soutien à Frei/anti-Allende, SUPPORTED.
- CLM-005 : changement de marge/majorité par l’intervention, GAP causal.
- CLM-006 : le spoiling 1970 n’empêche pas Allende d’arriver premier, SUPPORTED.
- CLM-007 : Track II vise un coup avant accession, SUPPORTED.

### Contradictions matérielles

**CON-001.** Les perceptions américaines d’une opération réussie en Italie se heurtent à une littérature décrivant une intervention improvisée et à des causes domestiques fortes. Résolution : intervention oui; détermination du vainqueur non démontrée.

**CON-002.** La CIA attribue une valeur causale majeure à son soutien à Frei, mais Labarca documente une mobilisation PDC autonome. Résolution : capacités et contribution plausibles; effet marginal non identifié.

**CON-003.** La CIA encourage un coup et soutient certains comploteurs, mais le dossier public n’établit pas une intention CIA de tuer Schneider. Résolution : responsabilité pour coup-promotion; attribution du meurtre non établie.

### Diversité du corpus

L’EDI diagnostique un corpus riche en sources primaires américaines et plus faible en perspectives locales indépendantes. Cela est acceptable pour prouver les décisions américaines, mais insuffisant pour transformer les auto-évaluations américaines en causalité électorale. L’EDI est un diagnostic de diversité, non un score de vérité.

## 12. CARTE DIALECTIQUE

### Scénario A — intervention décisive

Ce scénario affirme que la puissance matérielle américaine a modifié assez de ressources, d’information ou d’acteurs institutionnels pour changer les résultats. Il est plausible au niveau des mécanismes, particulièrement au Chili 1964, mais il manque une estimation indépendante du déplacement de voix ou du vainqueur contrefactuel.

### Scénario B — résultat principalement domestique, intervention contributive

Ce scénario affirme que les résultats s’expliquent principalement par les structures nationales, les partis, les coalitions et la mobilisation, l’intervention étrangère ajoutant une capacité mais n’étant pas déterminante. Il est fortement compatible avec l’Italie 1948 et le Chili 1964, mais ne peut pas non plus prouver exactement ce qui se serait passé sans intervention.

### Convergences

Les deux scénarios acceptent l’existence des opérations. Les deux peuvent accepter qu’une intervention déplace des ressources sans suffire à déterminer le vainqueur. Les conflits portent sur la magnitude causale.

### Responsabilité

- Truman/NSC : responsabilité documentée pour l’autorisation de mesures électorales en Italie [ACT-001].
- CIA/Special Group-303 : responsabilité documentée pour financement, organisation et propagande au Chili 1964 [ACT-002].
- Frei/PDC et réseaux chiliens : responsabilité pour leur propre campagne; bénéficiaire ne signifie pas marionnette [ACT-003].
- Nixon/CIA leadership : responsabilité documentée pour Track II [ACT-004].
- Groupes de comploteurs chiliens : responsabilité propre pour leurs plans et actions; association avec la CIA ne transfère pas automatiquement l’intégralité de la causalité [ACT-005].

### Impact

Le coût institutionnel le mieux établi est l’intrusion étrangère dans l’environnement de choix politique. Le bénéfice le mieux établi est l’apport de ressources et de capacités aux acteurs anticommunistes. L’effet final sur les électeurs n’est quantifiable ni en Italie 1948 ni au Chili 1964.

## 13. PÉRIMÈTRE & LIMITES

L’enquête couvre 1945-1975 mais concentre la preuve sur trois cas : Italie 1948, Chili 1964 et Chili 1970. Les autres opérations américaines de la guerre froide ne sont pas utilisées pour généraliser une fréquence ou une doctrine universelle.

Les sources principales sont des archives déclassifiées américaines, des documents institutionnels italiens et des travaux académiques. Les sources américaines sont primaires pour la question « que décidait et faisait l’appareil américain ? », mais intéressées pour la question « quelle efficacité avait-il ? ».

Les limites les plus importantes sont les suivantes : absence de véritable dispositif contrefactuel électoral pour 1948 et 1964; exposition individuelle à la propagande non reconstruite; déclassification potentiellement incomplète; connaissance des bénéficiaires locaux non homogène; impossibilité d’inférer un contrôle local complet depuis un transfert de fonds; impossibilité d’attribuer toutes les actions des comploteurs chiliens à la CIA.

Aucun chiffre d’« influence totale » n’est calculé. Les montants monétaires sont conservés dans leur contexte propre. Les votes, budgets, armes, autorité et accès sont des unités différentes et ne sont pas agrégées en score causal.

## 14. ÉTAT DES CONNAISSANCES

### Connu / confirmé

- Une politique américaine explicite de prévention d’une issue communiste en Italie en 1948 [FCT-001].
- Des opérations clandestines américaines associées à l’élection italienne [FCT-003].
- Un programme CIA de financement, organisation et propagande au Chili 1964 [FCT-006 à FCT-008].
- Une victoire nette de Frei en 1964 [FCT-009].
- Une opération anti-Allende avant le scrutin de 1970 [FCT-012].
- Allende arrive premier [FCT-013].
- Track II cherche un coup avant son accession [FCT-015; FCT-016].
- La CIA soutient matériellement certains comploteurs tout en n’étant pas démontrée comme auteur direct de chaque action [FCT-017].

### Probable / soutenu avec une famille dominante

- L’aide économique a servi de levier perceptible dans la campagne italienne [FCT-002].
- L’exposition à des opérations informationnelles a été large dans certains cas, sans mesure individuelle complète.

### Revendiqué

- L’auto-évaluation CIA selon laquelle son soutien fut indispensable à la victoire de Frei [FCT-010]. Le fait confirmé est l’existence de cette auto-évaluation, pas sa vérité causale.

### Contesté / partiel

- « Washington a fait gagner la DC en Italie » : non démontré.
- « Washington a donné à Frei sa majorité » : non démontré.
- « La CIA a tué Schneider » : formulation trop forte au regard des sources publiques inspectées.

### Inconnu

- Nombre exact de voix déplacées en Italie en 1948.
- Nombre exact de voix déplacées au Chili en 1964.
- Vainqueur contrefactuel dans ces deux élections sans intervention américaine.

### Réfuté dans le périmètre

- L’hypothèse que le spoiling de 1970 a empêché Allende d’arriver premier [CAU-006].
- L’hypothèse que Track II a empêché l’accession d’Allende en 1970 [CAU-008].

## 15. SUSPICION / VÉRIFICATION

La suspicion initiale principale était que l’expression « intervention américaine » pouvait agréger des réalités hétérogènes : aide publique, pression économique, soutien clandestin, propagande, financement partisan, action militaire indirecte. La vérification confirme cette hétérogénéité. Il n’existe pas une échelle morale ou causale unique allant mécaniquement de l’influence à la prise de contrôle.

Les 18 faits matériels ont été rouverts ou bornés par des sources exactes. Les faits les plus forts sur l’existence des opérations ont reçu des recherches adversariales explicites. Aucune contre-source crédible n’a réfuté l’existence de l’intervention en Italie 1948 ou au Chili 1964. En revanche, les recherches adversariales sur l’effet ont produit des limites importantes et des causalités domestiques concurrentes.

Les upgrades principaux concernent les faits pour lesquels une source officielle et une famille indépendante convergent : FCT-001, FCT-003, FCT-007 et FCT-008. Aucun fait n’a été « confirmé » par cohérence narrative seule.

Le contrôle final doit donc conserver deux phrases simultanément vraies : **les opérations américaines d’influence électorale sont historiquement documentées**; **le degré auquel elles ont changé les vainqueurs est beaucoup moins démontrable que leur existence**.

### Audit du lead

Le lead général « les États-Unis/CIA ont historiquement influencé des élections étrangères » survit à la vérification sur les cas étudiés. Il ne doit pas être extrapolé automatiquement à toute élection étrangère, à toute période contemporaine, ni à une capacité systématique de choisir les vainqueurs.

### Conditions de réouverture

Une réouverture est justifiée seulement par une preuve matériellement discriminante : panel ou variation d’exposition permettant d’identifier un effet de vote; nouvelle archive déclassifiée modifiant la chaîne de commandement; document altérant la frontière de responsabilité Schneider; ou preuve crédible d’un contrefactuel de vainqueur. Répéter les mêmes archives ou ajouter des commentaires secondaires ne suffit pas.

## SOURCES

- SRC-001 — FRUS 1948, NSC 1/3, 8 mars 1948 : https://history.state.gov/historicaldocuments/frus1948v03/d475
- SRC-002 — FRUS, télégramme Dunn, 20 mars 1948 : https://history.state.gov/historicaldocuments/frus1948v03/d528
- SRC-003 — FRUS, télégramme Dunn, 22 mars 1948 : https://history.state.gov/historicaldocuments/frus1948v03/d529
- SRC-004 — FRUS, NSC 10 draft, 12 mai 1948 : https://history.state.gov/historicaldocuments/frus1945-50Intel/d274
- SRC-005 — Kaeten Mistry, Modern Italy (2011) : https://www.cambridge.org/core/journals/modern-italy/article/abs/rethinking-american-intervention-in-the-1948-italian-election-beyond-a-successfailure-dichotomy/1BF2C98295B5449978091FA2EBF77383
- SRC-006 — James E. Miller, Diplomatic History (1983) : https://academic.oup.com/dh/article-abstract/7/1/35/410050
- SRC-007 — FRUS, CIA memorandum, Chili, 1 avril 1964 : https://history.state.gov/historicaldocuments/frus1964-68v31/d250
- SRC-008 — FRUS, Special Group, mai 1964 : https://history.state.gov/historicaldocuments/frus1964-68v31/d258
- SRC-009 — FRUS, résultat et postmortem CIA, septembre 1964 : https://history.state.gov/historicaldocuments/frus1964-68v31/d269
- SRC-010 — José Tomás Labarca, Latin American Research Review (2017) : https://www.cambridge.org/core/journals/latin-american-research-review/article/por-los-que-quieren-un-gobierno-de-avanzada-popular-nuevas-practicas-politicas-en-la-campana-presidencial-de-la-democracia-cristiana-chile-19621964/E9A033E7B37997628DA2119963BFDE67
- SRC-011 — FRUS, CIA pre-election planning, Chili 1970 : https://history.state.gov/historicaldocuments/frus1969-76v21/d29
- SRC-012 — FRUS, CIA intelligence memo, 7 septembre 1970 : https://history.state.gov/historicaldocuments/frus1969-76ve16/d18
- SRC-013 — FRUS, CIA coup planning, 9 septembre 1970 : https://history.state.gov/historicaldocuments/frus1969-76v21/d72
- SRC-014 — FRUS, Track II directive, 16 octobre 1970 : https://history.state.gov/historicaldocuments/frus1969-76v21/d154
- SRC-015 — FRUS, Track II after Schneider, 28 octobre 1970 : https://history.state.gov/historicaldocuments/frus1969-76v21/d168
- SRC-016 — FRUS, CIA Chilean Task Force report, 18 novembre 1970 : https://history.state.gov/historicaldocuments/frus1969-76ve16/d39
- SRC-017 — CIA Report to Congress on Activities in Chile (2000) : https://irp.fas.org/cia/product/chile/
- SRC-018 — National Security Archive, documents Chili 1964 : https://nsarchive2.gwu.edu/news/20040925/index.htm
- SRC-019 — US DOJ, Schneider v. Kissinger : https://www.justice.gov/osg/brief/schneider-v-kissinger-opposition
- SRC-020 — Camera dei deputati, étude historique : https://bpr.camera.it/bpr/allegati/show/23482_230_t
- SRC-021 — Senato della Repubblica, données rétrospectives : https://www.senato.it/show-doc?id=301865&idoggetto=0&leg=16&part=doc_dc-relpres_r&tipodoc=DDLPRES
- SRC-022 — Quirinale, biographie historique d’Alcide De Gasperi : https://archivio.quirinale.it/aspr/presidente/biografia/alcide-de-gasperi
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:5|CLM:7|AXS:9|CAU:8|CTRL:5|ACT:5

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_excerpt":"Topic lead only; not evidence","gap":"NONE","gap_type":"NONE","kind":"EVENT","lead":"United States materially attempted to influence the 1948 Italian election","linked_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005"],"locator":"user-specified investigation object","materiality":"DECISIVE","routes":["EXPAND","LINK"],"source_id":"NONE","status":"SATURATED"}
LED-002 | {"evidence_excerpt":"Topic lead only; not evidence","gap":"NONE","gap_type":"NONE","kind":"EVENT","lead":"United States/CIA materially attempted to influence the 1964 Chilean presidential election","linked_ids":["FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011"],"locator":"user-specified investigation object","materiality":"DECISIVE","routes":["EXPAND","LINK"],"source_id":"NONE","status":"SATURATED"}
LED-003 | {"evidence_excerpt":"Topic lead only; not evidence","gap":"NONE","gap_type":"NONE","kind":"EVENT","lead":"United States/CIA attempted to influence the 1970 Chilean presidential election and subsequent accession process","linked_ids":["FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018"],"locator":"user-specified investigation object","materiality":"DECISIVE","routes":["EXPAND","LINK"],"source_id":"NONE","status":"SATURATED"}
LED-004 | {"evidence_excerpt":"Methodological investigation constraint","gap":"NONE","gap_type":"NONE","kind":"MECHANISM","lead":"Operation existence must be separated from exposure, persuasion, behavioral change, and winner counterfactual","linked_ids":["FCT-010","FCT-011","FCT-014","FCT-016"],"locator":"method boundary","materiality":"DECISIVE","routes":["LINK"],"source_id":"NONE","status":"SATURATED"}
LED-005 | {"evidence_excerpt":"Scope constraint","gap":"NONE","gap_type":"NONE","kind":"CONTEXT","lead":"Electoral influence must be distinguished from destabilization and regime change","linked_ids":["FCT-012","FCT-015","FCT-016","FCT-018"],"locator":"scope boundary","materiality":"IMPORTANT","routes":["LINK","CONTEXT"],"source_id":"NONE","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Italy 1948: U.S. policy explicitly sought to prevent communist electoral participation/win","claimant":"investigation hypothesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":"FCT-001"}
CLM-002 | {"claim":"Italy 1948: covert and overt U.S. measures materially influenced the campaign","claimant":"investigation hypothesis","counter":"FCT-005 and SRC-005 show local agency/non-unified operation","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":"FCT-002,FCT-003"}
CLM-003 | {"claim":"Italy 1948: U.S. intervention changed the identity of the winner","claimant":"investigation hypothesis","counter":"FCT-005 plus lack of valid counterfactual","gap":"winner counterfactual not identifiable from available evidence","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"GAP","support":"operator perceptions of success only"}
CLM-004 | {"claim":"Chile 1964: CIA covert action materially supported Frei and anti-Allende campaigning","claimant":"investigation hypothesis","counter":"NONE_FOUND on operation existence","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":"FCT-006,FCT-007,FCT-008"}
CLM-005 | {"claim":"Chile 1964: U.S. intervention changed Frei's margin or majority","claimant":"investigation hypothesis","counter":"FCT-011 independent domestic mobilization rival","gap":"marginal vote effect/majority counterfactual not independently identified","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"GAP","support":"FCT-010 operator causal self-assessment"}
CLM-006 | {"claim":"Chile 1970: U.S. pre-election spoiling campaign failed to prevent Allende plurality","claimant":"investigation hypothesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":"FCT-013,FCT-014"}
CLM-007 | {"claim":"Chile 1970: post-election Track II sought a coup to prevent/undo Allende accession","claimant":"investigation hypothesis","counter":"local plotter agency limits attribution of specific violence","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":"FCT-015,FCT-016,FCT-017"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-002","QRY-023","QRY-025","QRY-028","QRY-033","QRY-038"],"axis":"SOURCE_AUDIT","gap":"NONE","gap_type":"NONE","links":["LED-001","LED-002","LED-003"],"question":"Are the core records authentic/inspectable and what do they directly establish?","result_ids":["FCT-001","FCT-003","FCT-006","FCT-012","FCT-017"],"sought_objects":"FRUS, Senate, CIA reports","status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-001","QRY-026","QRY-027","QRY-038"],"axis":"SCOPE_HISTORY","gap":"NONE","gap_type":"NONE","links":["LED-001","LED-003","LED-005"],"question":"What changed from improvised 1948 electoral intervention to institutionalized covert action and Chile?","result_ids":["FCT-001","FCT-003","FCT-008","FCT-012","FCT-016"],"sought_objects":"NSC policy chronology, authorities","status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-002","QRY-028","QRY-030","QRY-033","QRY-038","QRY-041","QRY-042"],"axis":"EVIDENCE_CASES","gap":"NONE","gap_type":"NONE","links":["LED-001","LED-002","LED-003"],"question":"What happened in Italy 1948, Chile 1964, Chile 1970?","result_ids":["FCT-001","FCT-004","FCT-006","FCT-009","FCT-013","FCT-016"],"sought_objects":"case-level primary records and election results","status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-023","QRY-028","QRY-029","QRY-038","QRY-039"],"axis":"RESOURCES_FLOWS","gap":"NONE","gap_type":"NONE","links":["LED-001","LED-002","LED-003"],"question":"What money, aid, propaganda, organizational resources and weapons moved through which channels?","result_ids":["FCT-002","FCT-003","FCT-006","FCT-007","FCT-008","FCT-017"],"sought_objects":"approved funds, aid leverage, propaganda assets, material support","status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-005","QRY-011","QRY-012","QRY-032","QRY-034","QRY-035"],"axis":"MECHANISMS","gap":"NONE","gap_type":"NONE","links":["LED-004"],"question":"By what mechanisms could intervention affect electoral choice or accession?","result_ids":["CAU-001","CAU-002","CAU-004","CAU-006","CAU-007"],"sought_objects":"funding, propaganda, aid conditionality, organizational support, coup contacts","status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-026","QRY-031","QRY-038","QRY-039"],"axis":"ACTORS_RELATIONS","gap":"NONE","gap_type":"NONE","links":["LED-001","LED-002","LED-003"],"question":"Which U.S. and local actors were aligned, cooperating, coordinated or tasked?","result_ids":["ACT-001","ACT-002","ACT-003","ACT-004","ACT-005"],"sought_objects":"NSC, CIA, State, embassies, parties, media, military","status":"SATURATED"}
AXS-007 | {"attempt_ids":["QRY-002","QRY-028","QRY-029","QRY-035","QRY-038"],"axis":"RULES_CONTROLS","gap":"NONE","gap_type":"NONE","links":["LED-001","LED-002","LED-003"],"question":"Who authorized, supervised or constrained covert action?","result_ids":["CTRL-001","CTRL-002","CTRL-003","CTRL-004","CTRL-005"],"sought_objects":"NSC, Special Group/303, 40 Committee, CIA chain","status":"SATURATED"}
AXS-008 | {"attempt_ids":["QRY-010","QRY-011","QRY-012","QRY-044","QRY-045","QRY-046","QRY-047"],"axis":"IMPACT_RESPONSIBILITY","gap":"I6/I7 winner/margin counterfactuals are not identifiable for Italy 1948 or Chile 1964; 1970 immediate prevention objective failed","gap_type":"CAUSALITY","links":["LED-004"],"question":"What effects are demonstrable from I4 through I7 and who can be assigned responsibility for which actions?","result_ids":["CAU-003","CAU-005","CAU-006","CAU-008"],"sought_objects":"reach, persuasion, vote shift, winner counterfactual","status":"GAP"}
AXS-009 | {"attempt_ids":["QRY-009","QRY-015","QRY-016","QRY-017","QRY-018","QRY-019","QRY-020","QRY-021","QRY-022","QRY-031","QRY-041","QRY-042"],"axis":"COUNTER_HYPOTHESES","gap":"NONE","gap_type":"NONE","links":["LED-004","LED-005"],"question":"Which domestic or structural causes explain outcomes without U.S. intervention?","result_ids":["FCT-005","FCT-011","CAU-003","CAU-005"],"sought_objects":"Catholic Church, party strategy, coalition shifts, electorate, local agency","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"domestic voters could discount the threat; no treatment-effect estimate","from":"US aid leverage and public conditionality","gap":"NONE","gap_type":"NONE","link_type":"ENABLER","mechanism":"make perceived access to US economic assistance contingent on electoral outcome","source":"FCT-001,FCT-002","status":"SUPPORTED","to":"altered electoral information environment in Italy 1948"}
CAU-002 | {"counter":"Mistry finds intervention improvised and influenced by Italians; Catholic and party mobilization were independently material","from":"US covert financial and political assistance","gap":"NONE","gap_type":"NONE","link_type":"ENABLER","mechanism":"increase campaign resources and organizational capacity of selected anti-Communist parties","source":"FCT-003","status":"SUPPORTED","to":"anti-Communist campaign capacity in Italy 1948"}
CAU-003 | {"counter":"large domestic Catholic mobilization, De Gasperi/party strategy and non-unified US campaign; no credible winner counterfactual","from":"US overt/covert intervention in Italy 1948","gap":"no source isolates whether the identity of the winner would have changed absent US intervention","gap_type":"CAUSALITY","link_type":"CAUSE","mechanism":"combined funding, aid leverage, information operations and diplomatic signaling","source":"FCT-001,FCT-002,FCT-003,FCT-004,FCT-005","status":"UNRESOLVED","to":"Christian Democratic victory rather than a Popular Front victory"}
CAU-004 | {"counter":"PDC had autonomous organization and social mobilization","from":"CIA/US funding, organization and propaganda in Chile 1964","gap":"NONE","gap_type":"NONE","link_type":"ENABLER","mechanism":"finance Frei/PDC campaign capacity, ancillary organizations and anti-Allende propaganda","source":"FCT-006,FCT-007,FCT-008","status":"SUPPORTED","to":"expanded pro-Frei campaign capacity and audience exposure"}
CAU-005 | {"counter":"CIA causal assessment is self-evaluation; Labarca documents strong independent PDC mobilization and first-time voters","from":"US-supported campaign exposure in Chile 1964","gap":"marginal vote effect and winner counterfactual cannot be isolated from available evidence","gap_type":"CAUSALITY","link_type":"CAUSE","mechanism":"persuasion/fear plus improved campaign capacity converts exposure into votes","source":"FCT-009,FCT-010,FCT-011","status":"UNRESOLVED","to":"Frei vote margin and absolute majority"}
CAU-006 | {"counter":"Allende nevertheless finished first; CIA later described the spoiling operation as not succeeding","from":"CIA anti-Allende spoiling operation in Chile 1970","gap":"NONE","gap_type":"NONE","link_type":"CAUSE","mechanism":"propaganda intended to move a small critical share of voters away from Allende","source":"FCT-012,FCT-013,FCT-014","status":"REFUTED","to":"prevent Allende from finishing first in popular vote"}
CAU-007 | {"counter":"local plotter groups retained agency and varied capability; CIA rejected the Viaux plan before fatal attack","from":"Nixon/White House Track II direction","gap":"NONE","gap_type":"NONE","link_type":"ENABLER","mechanism":"direct CIA military contacts, pressure, coup encouragement and material support","source":"FCT-015,FCT-016,FCT-017","status":"SUPPORTED","to":"Chilean military coup plotting before Allende accession"}
CAU-008 | {"counter":"Track II failed and Allende took office","from":"Track II coup effort","gap":"NONE","gap_type":"NONE","link_type":"CAUSE","mechanism":"coup before congressional confirmation/inauguration","source":"FCT-016,FCT-017","status":"REFUTED","to":"prevent Allende accession to presidency"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"controller":"President/NSC/Secretary of State","documented_action":"President approved paragraph 8; executive departments/agencies directed to implement under State coordination","gap":"NONE","information":"fear of Popular Front victory; US aid dependence; six-week election window","outcome":"overt and covert intervention measures executed","oversight":"formal NSC/Presidential authorization visible in FRUS","rule":"NSC 1/3 policy authorization and interagency coordination","source":"FCT-001,FCT-003","status":"SATURATED"}
CTRL-002 | {"controller":"Special Group / 303 Committee","documented_action":"approved election-support programs and additional funding for Frei/PDC and related operations","gap":"NONE","information":"Chile electoral polling, party budgets, anti-Allende objective","outcome":"multi-million-dollar covert campaign implemented","oversight":"subcabinet covert-action committee","rule":"review/approval of covert political action","source":"FCT-006,FCT-007,FCT-008","status":"SATURATED"}
CTRL-003 | {"controller":"40 Committee / Ambassador / CIA Station","documented_action":"authorized anti-Allende propaganda/spoiling while formally excluding direct support to a presidential candidate","gap":"NONE","information":"Allende leading candidate; multiple non-left candidates","outcome":"operation failed to prevent Allende plurality","oversight":"40 Committee and ambassadorial coordination","rule":"1970 pre-election covert action limited to spoiling rather than direct candidate support","source":"FCT-012,FCT-014","status":"SATURATED"}
CTRL-004 | {"controller":"President Nixon / White House / CIA DCI","documented_action":"directed CIA to prevent Allende accession and seek/stimulate a military coup with US role hidden","gap":"NONE","information":"Allende plurality and likely congressional confirmation","outcome":"military contacts/material support occurred; effort failed to prevent accession","oversight":"high-level White House direction; compartmented from normal diplomatic chain","rule":"Track II special direction outside normal State/Defense/Ambassador coordination","source":"FCT-015,FCT-016,FCT-017","status":"SATURATED"}
CTRL-005 | {"controller":"Chilean constitutional Congress / armed-forces constitutional norm","documented_action":"Congress confirmed Allende; Schneider remained obstacle to coup efforts until fatal abduction attempt","gap":"NONE","information":"Allende plurality; Schneider constitutional position","outcome":"Allende acceded despite US Track I/II pressure","oversight":"domestic constitutional process","rule":"Congress selects among top candidates absent absolute majority; constitutionalist military leadership resists political intervention","source":"FCT-013,FCT-017","status":"SATURATED"}

### ACTION_REGISTRY_V1
ACT-001 | {"documented_action":"approved priority measures intended to prevent Communist electoral participation in Italian government in 1948","intent":"PROVEN","name":"Harry S. Truman / US National Security Council","responsibility_scope":"authorization of stated US policy and coordinated measures","role":"US presidential/national-security authority","source":"FCT-001","status":"SATURATED"}
ACT-002 | {"documented_action":"financed, organized and implemented covert political/propaganda support intended to defeat Allende and benefit Frei/PDC","intent":"PROVEN","name":"US Central Intelligence Agency / Special Group-303 Committee","responsibility_scope":"documented covert campaign actions; not proven sole cause of electoral result","role":"covert-action operator and authorizer in Chile 1964","source":"FCT-006,FCT-007,FCT-008","status":"SATURATED"}
ACT-003 | {"documented_action":"ran autonomous mass campaign, rural/social mobilization and participatory organization while receiving US support","intent":"PROVEN","name":"Eduardo Frei/PDC campaign and Chilean supporting networks","responsibility_scope":"domestic campaign strategy/mobilization; individual knowledge of every covert channel not generalized beyond records","role":"local electoral actors and beneficiaries","source":"FCT-008,FCT-011","status":"SATURATED"}
ACT-004 | {"documented_action":"directed/implemented effort to prevent Allende accession through a military coup and covert pressure","intent":"PROVEN","name":"Richard Nixon / CIA leadership","responsibility_scope":"authorization and implementation of Track II; not equivalent to direct authorship of every local plotter action","role":"US executive direction for Track II 1970","source":"FCT-015,FCT-016","status":"SATURATED"}
ACT-005 | {"documented_action":"planned coup/kidnapping actions; some groups received CIA contact/material support while retaining their own command and agency","intent":"PROVEN","name":"Chilean coup plotter groups","responsibility_scope":"their documented plots/actions; CIA responsibility must be bounded by specific support/tasking evidence","role":"local military/civilian actors","source":"FCT-017","status":"SATURATED"}

SEARCH_ACTIVITY_V1:WEB:25|FETCH:22|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FOUND | READ | definitions/SYMBOLS.md | @READ[definitions/SYMBOLS.md]
SYS-002 | SYS | FOUND | READ | definitions/PATTERNS.md | @READ[definitions/PATTERNS.md]
SYS-003 | SYS | FOUND | READ | definitions/THREATS.md | @READ[definitions/THREATS.md]
SYS-004 | SYS | FOUND | READ | forensic/GATES.md | @READ[forensic/GATES.md]
SYS-005 | SYS | FOUND | READ | forensic/REQUEST_LOG.md | @READ[forensic/REQUEST_LOG.md]
SYS-006 | SYS | MNEMO_UNAVAILABLE | MNEMO | NONE | MNEMO_Q
SYS-007 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-008 | SYS | FOUND | READ | protocol/INVESTIGATION.md | @READ[protocol/INVESTIGATION.md]
SYS-009 | SYS | PASS | READ | clusters/ICEBERG.md | @READ[clusters/ICEBERG.md]
SYS-010 | SYS | PASS | READ | clusters/MONEY.md | @READ[clusters/MONEY.md]
SYS-011 | SYS | PASS | READ | clusters/FRAMING.md | @READ[clusters/FRAMING.md]
SYS-012 | SYS | PASS | READ | clusters/OVERLOAD.md | @READ[clusters/OVERLOAD.md]
SYS-013 | SYS | PASS | READ | clusters/POWER.md | @READ[clusters/POWER.md]
SYS-014 | SYS | PASS | READ | clusters/CONFIRMATION.md | @READ[clusters/CONFIRMATION.md]
SYS-015 | SYS | PASS | READ | clusters/FRAGMENTATION.md | @READ[clusters/FRAGMENTATION.md]
SYS-016 | SYS | PASS | READ | clusters/WAR.md | @READ[clusters/WAR.md]
SYS-017 | SYS | PASS | READ | clusters/NETWORK.md | @READ[clusters/NETWORK.md]
SYS-018 | SYS | PASS | READ | clusters/TEMPORAL.md | @READ[clusters/TEMPORAL.md]
SYS-019 | SYS | PASS | READ | forensic/REASONING.md | @READ[forensic/REASONING.md]
SYS-020 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | site:cambridge.org "Rethinking American intervention in the 1948 Italian election" Mistry
QRY-002 | FETCH | FOUND | SRC-001 | https://history.state.gov/historicaldocuments/frus1948v03/d475 | FETCH https://history.state.gov/historicaldocuments/frus1948v03/d475
QRY-003 | WEB | FOUND | - | - | site:academic.oup.com "The United States and the Italian Election of 1948" Miller
QRY-004 | WEB | FOUND | - | - | site:senato.it 18 aprile 1948 democrazia cristiana 48.5 fronte popolare
QRY-005 | WEB | FOUND | - | - | Chile 1964 Frei campaign scare campaign Margaret Power quantifiable vote effect
QRY-006 | WEB | FOUND | - | - | Chile 1964 Labarca Frei 56 percent election Christian Democracy campaign
QRY-007 | WEB | FOUND | - | - | CIA Chile 1970 Hinchey report failed block Allende accession
QRY-008 | WEB | FOUND | - | - | Chile 1970 CIA Schneider direct responsibility no evidence Church Committee
QRY-009 | WEB | FOUND | - | - | Italy 1948 election American intervention did not determine outcome Catholic Church De Gasperi Marshall Plan academic
QRY-010 | WEB | FOUND | - | - | REFUTATION Italy 1948 winner: evidence Christian Democrats would have won without US intervention
QRY-011 | WEB | FOUND | - | - | REFUTATION Chile 1964 margin: evidence Frei would have won without US covert support campaign
QRY-012 | WEB | FOUND | - | - | REFUTATION Chile 1964 56 percent: scare campaign effect not quantifiable
QRY-013 | WEB | FOUND | - | - | REFUTATION Chile 1970 Allende plurality: evidence US campaign prevented Allende from coming first
QRY-014 | WEB | FOUND | - | - | REFUTATION Chile 1970 Schneider CIA direct responsibility kidnapping death evidence
QRY-015 | WEB | FOUND | - | - | Soviet support Italian Communist Party 1948 election funding Moscow
QRY-016 | WEB | FOUND | - | - | Chile 1964 right support Frei Naranjazo domestic coalition Catholic Church
QRY-017 | WEB | FOUND | - | - | site:cambridge.org Italy 1948 Catholic Church election Christian Democrats 48.5 communist funding Soviet
QRY-018 | WEB | FOUND | - | - | site:oxfordacademic.com Italy 1948 Catholic Church De Gasperi election American intervention
QRY-019 | WEB | FOUND | - | - | "Italy 1948" "Catholic Church" De Gasperi election US intervention academic
QRY-020 | WEB | FOUND | - | - | "1948 Italian election" Soviet funding PCI Moscow
QRY-021 | WEB | FOUND | - | - | "Taking off the gloves" Italy 1948 covert funding critical victory Miller
QRY-022 | WEB | FOUND | - | - | site:camera.it 18 aprile 1948 Democrazia Cristiana 48,5 Fronte Popolare 35
QRY-023 | FETCH | FOUND | SRC-002 | https://history.state.gov/historicaldocuments/frus1948v03/d528 | FETCH https://history.state.gov/historicaldocuments/frus1948v03/d528
QRY-024 | FETCH | FOUND | SRC-003 | https://history.state.gov/historicaldocuments/frus1948v03/d529 | FETCH https://history.state.gov/historicaldocuments/frus1948v03/d529
QRY-025 | FETCH | FOUND | SRC-004 | https://history.state.gov/historicaldocuments/frus1945-50Intel/d274 | FETCH https://history.state.gov/historicaldocuments/frus1945-50Intel/d274
QRY-026 | FETCH | FOUND | SRC-005 | https://www.cambridge.org/core/journals/modern-italy/article/abs/rethinking-american-intervention-in-the-1948-italian-election-beyond-a-successfailure-dichotomy/1BF2C98295B5449978091FA2EBF77383 | FETCH https://www.cambridge.org/core/journals/modern-italy/article/abs/rethinking-american-intervention-in-the-1948-italian-election-beyond-a-successfailure-dichotomy/1BF2C98295B5449978091FA2EBF77383
QRY-027 | FETCH | FOUND | SRC-006 | https://academic.oup.com/dh/article-abstract/7/1/35/410050 | FETCH https://academic.oup.com/dh/article-abstract/7/1/35/410050
QRY-028 | FETCH | FOUND | SRC-007 | https://history.state.gov/historicaldocuments/frus1964-68v31/d250 | FETCH https://history.state.gov/historicaldocuments/frus1964-68v31/d250
QRY-029 | FETCH | FOUND | SRC-008 | https://history.state.gov/historicaldocuments/frus1964-68v31/d258 | FETCH https://history.state.gov/historicaldocuments/frus1964-68v31/d258
QRY-030 | FETCH | FOUND | SRC-009 | https://history.state.gov/historicaldocuments/frus1964-68v31/d269 | FETCH https://history.state.gov/historicaldocuments/frus1964-68v31/d269
QRY-031 | FETCH | FOUND | SRC-010 | https://www.cambridge.org/core/journals/latin-american-research-review/article/por-los-que-quieren-un-gobierno-de-avanzada-popular-nuevas-practicas-politicas-en-la-campana-presidencial-de-la-democracia-cristiana-chile-19621964/E9A033E7B37997628DA2119963BFDE67 | FETCH https://www.cambridge.org/core/journals/latin-american-research-review/article/por-los-que-quieren-un-gobierno-de-avanzada-popular-nuevas-practicas-politicas-en-la-campana-presidencial-de-la-democracia-cristiana-chile-19621964/E9A033E7B37997628DA2119963BFDE67
QRY-032 | FETCH | FOUND | SRC-011 | https://history.state.gov/historicaldocuments/frus1969-76v21/d29 | FETCH https://history.state.gov/historicaldocuments/frus1969-76v21/d29
QRY-033 | FETCH | FOUND | SRC-012 | https://history.state.gov/historicaldocuments/frus1969-76ve16/d18 | FETCH https://history.state.gov/historicaldocuments/frus1969-76ve16/d18
QRY-034 | FETCH | FOUND | SRC-013 | https://history.state.gov/historicaldocuments/frus1969-76v21/d72 | FETCH https://history.state.gov/historicaldocuments/frus1969-76v21/d72
QRY-035 | FETCH | FOUND | SRC-014 | https://history.state.gov/historicaldocuments/frus1969-76v21/d154 | FETCH https://history.state.gov/historicaldocuments/frus1969-76v21/d154
QRY-036 | FETCH | FOUND | SRC-015 | https://history.state.gov/historicaldocuments/frus1969-76v21/d168 | FETCH https://history.state.gov/historicaldocuments/frus1969-76v21/d168
QRY-037 | FETCH | FOUND | SRC-016 | https://history.state.gov/historicaldocuments/frus1969-76ve16/d39 | FETCH https://history.state.gov/historicaldocuments/frus1969-76ve16/d39
QRY-038 | FETCH | FOUND | SRC-017 | https://irp.fas.org/cia/product/chile/ | FETCH https://irp.fas.org/cia/product/chile/
QRY-039 | FETCH | FOUND | SRC-018 | https://nsarchive2.gwu.edu/news/20040925/index.htm | FETCH https://nsarchive2.gwu.edu/news/20040925/index.htm
QRY-040 | FETCH | FOUND | SRC-019 | https://www.justice.gov/osg/brief/schneider-v-kissinger-opposition | FETCH https://www.justice.gov/osg/brief/schneider-v-kissinger-opposition
QRY-041 | FETCH | FOUND | SRC-020 | https://bpr.camera.it/bpr/allegati/show/23482_230_t | FETCH https://bpr.camera.it/bpr/allegati/show/23482_230_t
QRY-042 | FETCH | FOUND | SRC-021 | https://www.senato.it/show-doc?id=301865&idoggetto=0&leg=16&part=doc_dc-relpres_r&tipodoc=DDLPRES | FETCH https://www.senato.it/show-doc?id=301865&idoggetto=0&leg=16&part=doc_dc-relpres_r&tipodoc=DDLPRES
QRY-043 | FETCH | FOUND | SRC-022 | https://archivio.quirinale.it/aspr/presidente/biografia/alcide-de-gasperi | FETCH https://archivio.quirinale.it/aspr/presidente/biografia/alcide-de-gasperi
QRY-044 | WEB | FOUND | - | - | REFUTATION Italy 1948 US intervention: evidence that US did not intervene in Italian election 1948
QRY-045 | WEB | FOUND | - | - | REFUTATION Chile 1964 CIA covert support: evidence no US covert support Frei campaign 1964
QRY-046 | WEB | FOUND | - | - | REFUTATION Chile 1970 spoiling failed: evidence US covert campaign prevented Allende from winning plurality 1970
QRY-047 | WEB | FOUND | - | - | REFUTATION Chile 1970 Track II coup: evidence CIA was not directed to instigate coup before Allende accession

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://history.state.gov/historicaldocuments/frus1948v03/d475
SRC-002 | ◈ | fam:A | https://history.state.gov/historicaldocuments/frus1948v03/d528
SRC-003 | ◈ | fam:A | https://history.state.gov/historicaldocuments/frus1948v03/d529
SRC-004 | ◈ | fam:A | https://history.state.gov/historicaldocuments/frus1945-50Intel/d274
SRC-005 | ◉ | fam:E | https://www.cambridge.org/core/journals/modern-italy/article/abs/rethinking-american-intervention-in-the-1948-italian-election-beyond-a-successfailure-dichotomy/1BF2C98295B5449978091FA2EBF77383
SRC-006 | ◉ | fam:E | https://academic.oup.com/dh/article-abstract/7/1/35/410050
SRC-007 | ◈ | fam:A | https://history.state.gov/historicaldocuments/frus1964-68v31/d250
SRC-008 | ◈ | fam:A | https://history.state.gov/historicaldocuments/frus1964-68v31/d258
SRC-009 | ◈ | fam:A | https://history.state.gov/historicaldocuments/frus1964-68v31/d269
SRC-010 | ◉ | fam:E | https://www.cambridge.org/core/journals/latin-american-research-review/article/por-los-que-quieren-un-gobierno-de-avanzada-popular-nuevas-practicas-politicas-en-la-campana-presidencial-de-la-democracia-cristiana-chile-19621964/E9A033E7B37997628DA2119963BFDE67
SRC-011 | ◈ | fam:A | https://history.state.gov/historicaldocuments/frus1969-76v21/d29
SRC-012 | ◈ | fam:A | https://history.state.gov/historicaldocuments/frus1969-76ve16/d18
SRC-013 | ◈ | fam:A | https://history.state.gov/historicaldocuments/frus1969-76v21/d72
SRC-014 | ◈ | fam:A | https://history.state.gov/historicaldocuments/frus1969-76v21/d154
SRC-015 | ◈ | fam:A | https://history.state.gov/historicaldocuments/frus1969-76v21/d168
SRC-016 | ◈ | fam:A | https://history.state.gov/historicaldocuments/frus1969-76ve16/d39
SRC-017 | ◈ | fam:A | https://irp.fas.org/cia/product/chile/
SRC-018 | ◉ | fam:D | https://nsarchive2.gwu.edu/news/20040925/index.htm
SRC-019 | ◈ | fam:A | https://www.justice.gov/osg/brief/schneider-v-kissinger-opposition
SRC-020 | ◉ | fam:D | https://bpr.camera.it/bpr/allegati/show/23482_230_t
SRC-021 | ◈ | fam:A | https://www.senato.it/show-doc?id=301865&idoggetto=0&leg=16&part=doc_dc-relpres_r&tipodoc=DDLPRES
SRC-022 | ◈ | fam:A | https://archivio.quirinale.it/aspr/presidente/biografia/alcide-de-gasperi

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://history.state.gov/historicaldocuments/frus1948v03/d475 | A,E | 1948-03-08 | Italy 1948 US electoral intervention | NSC 1/3 explicitly made preventing communist participation through the April election a US priority and prescribed aid leverage, public messaging, letter-writing and continued assistance to anti-Communist parties; independent scholarship confirms a US intervention campaign existed. | -
FCT-002 | FACT | ✧ | https://history.state.gov/historicaldocuments/frus1948v03/d528 | A | 1948-03-20 | Italy 1948 aid leverage in campaign | Ambassador Dunn reported Secretary Marshall statements were presented in Italy as making suspension of US aid a consequence of a Popular Front victory; Communist press denounced this as electoral blackmail. | -
FCT-003 | FACT | ✦ | https://history.state.gov/historicaldocuments/frus1945-50Intel/d274 | A,E | 1948-05-12 | Italy 1948 covert political operations | NSC 10 later referred to improvised covert operations used at the time of the Italian elections; Miller independently characterizes 1948 as the first significant US covert political operation. | -
FCT-004 | FACT | ✧ | https://bpr.camera.it/bpr/allegati/show/23482_230_t | A,D | 1948-04-18 | Italy 1948 election outcome | Italian parliamentary historical sources report a decisive Christian Democratic victory, about 48.5 percent for the DC, with an absolute majority of Chamber seats. | -
FCT-005 | FACT | ✧ | https://bpr.camera.it/bpr/allegati/show/23482_230_t | A,D | 1948-04-18 | Italy 1948 domestic Catholic mobilization | An Italian parliamentary historical study identifies Catholic Action civic committees and church mobilization as materially contributing votes to the Christian Democrats; the Quirinale account likewise describes a highly mobilized, apocalyptic domestic campaign. | -
FCT-006 | FACT | ✧ | https://history.state.gov/historicaldocuments/frus1964-68v31/d250 | A | 1964-04-01 | Chile 1964 CIA campaign proposal | CIA proposed $750,000 for political and propaganda action to defeat Allende, strengthen Frei campaign organization, steer democratic votes, support ancillary groups and use specialized propaganda including black propaganda; the proposal also contemplated buying votes if required. | -
FCT-007 | FACT | ✦ | https://history.state.gov/historicaldocuments/frus1964-68v31/d258 | A,D | 1964-05-14 | Chile 1964 additional covert funding | The Special Group approved an additional $1.25 million for covert use in the Chilean presidential election, primarily to increase financial support to Frei and allow the PDC to campaign at full potential. | -
FCT-008 | FACT | ✦ | https://irp.fas.org/cia/product/chile/ | A,D | 1964-09-04 | Chile 1964 US covert intervention | The CIA 2000 report states that the 1964 campaign aimed to prevent Allende, made Frei the principal beneficiary, used propaganda and political action, and reached $3 million in approved funding; independent document archivists corroborate the declassified funding architecture. | -
FCT-009 | FACT | ✧ | https://history.state.gov/historicaldocuments/frus1964-68v31/d269 | A,E | 1964-09-04 | Chile 1964 election outcome | Frei won decisively with about 56 percent against Allende at about 39 percent; independent scholarship confirms the absolute-majority outcome while stressing multiple domestic causes. | -
FCT-010 | FACT | ✧ | https://history.state.gov/historicaldocuments/frus1964-68v31/d269 | A | 1964-09-05 | Chile 1964 CIA causal self-assessment | CIA and US officials assessed their financial, organizational and propaganda support as indispensable or significant to Frei success; this is an operator self-assessment, not an independent counterfactual estimate. | -
FCT-011 | FACT | ✧ | https://www.cambridge.org/core/journals/latin-american-research-review/article/por-los-que-quieren-un-gobierno-de-avanzada-popular-nuevas-practicas-politicas-en-la-campana-presidencial-de-la-democracia-cristiana-chile-19621964/E9A033E7B37997628DA2119963BFDE67 | E | 2017-01-01 | Chile 1964 domestic mobilization rival | Labarca finds that Frei majority cannot be explained only by the scare campaign or right-wing support: PDC participatory organization, rural social immersion and mobilization of many first-time presidential voters were material to the result. | -
FCT-012 | FACT | ✧ | https://history.state.gov/historicaldocuments/frus1969-76v21/d29 | A | 1970-06-18 | Chile 1970 pre-election spoiling mechanism | CIA planning assessed a floating vote and proposed anti-Allende spoiling and propaganda operations with the US role hidden; the document expressed a possibility of influencing a small critical number of votes, not proof of actual vote movement. | -
FCT-013 | FACT | ✧ | https://history.state.gov/historicaldocuments/frus1969-76ve16/d18 | A | 1970-09-07 | Chile 1970 popular vote outcome | CIA reported Allende first with about 36.3 percent, Alessandri about 34.9 percent and Tomic about 27.8 percent, requiring a congressional selection because no candidate had an absolute majority. | -
FCT-014 | FACT | ✧ | https://irp.fas.org/cia/product/chile/ | A | 1970-09-04 | Chile 1970 electoral spoiling failed | The CIA 2000 report states that by August the spoiling operation was not succeeding and describes the major 1970 CIA effort to block Allende election/accession as failed; Allende nevertheless won a plurality. | -
FCT-015 | FACT | ✧ | https://history.state.gov/historicaldocuments/frus1969-76v21/d72 | A | 1970-09-09 | Chile 1970 direct military contact planning | CIA proposed direct contacts with Chilean military officers to evaluate and stimulate a coup route after the election; the political-constitutional route was judged weak. | -
FCT-016 | FACT | ✧ | https://history.state.gov/historicaldocuments/frus1969-76v21/d154 | A | 1970-10-16 | Chile 1970 Track II coup policy | A CIA cable transmitted firm continuing US policy that Allende be overthrown by a coup, preferably before the congressional vote, with maximum pressure and the US hand hidden; the later CIA report independently reproduces this Track II mandate within the same operator provenance family. | -
FCT-017 | FACT | ✧ | https://irp.fas.org/cia/product/chile/ | A | 1970-10-22 | Chile 1970 Schneider responsibility boundary | CIA encouraged coup plotting and supplied weapons to one plotter group, but the available public record does not establish that CIA intended Schneider to be killed; the Viaux group that carried out the fatal abduction attempt was described as acting independently of CIA at that time. | -
FCT-018 | FACT | ✧ | https://irp.fas.org/cia/product/chile/ | A | 1973-09-11 | Chile 1973 coup anti-conflation boundary | CIA reported that it did not instigate the September 1973 coup, while acknowledging awareness of coup plotting and earlier 1970 efforts to instigate a coup; this distinction prevents retroactive conflation of Track II 1970 with direct authorship of the 1973 coup. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-005
FCT-002 | SRC-002
FCT-003 | SRC-004,SRC-006
FCT-004 | SRC-020,SRC-021
FCT-005 | SRC-020,SRC-022
FCT-006 | SRC-007
FCT-007 | SRC-008,SRC-018
FCT-008 | SRC-017,SRC-018
FCT-009 | SRC-009,SRC-010
FCT-010 | SRC-009
FCT-011 | SRC-010
FCT-012 | SRC-011
FCT-013 | SRC-012
FCT-014 | SRC-017
FCT-015 | SRC-013
FCT-016 | SRC-014,SRC-017
FCT-017 | SRC-017,SRC-015,SRC-019
FCT-018 | SRC-017

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-044 | NONE
FCT-003 | QRY-044 | NONE
FCT-007 | QRY-045 | NONE
FCT-008 | QRY-045 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:CONFIRME
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:CONFIRME
FCT-008 | ELIGIBLE:CONFIRME
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
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-05T21:12:52.588393+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:CONFIRME","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:CONFIRME","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:CONFIRME","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":18,"eligible":18,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:18;attempted:0;success:0;failure:0;blocked:18} | WRITEBACK_EXECUTION_V1:[18 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-002 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-003 | ELIGIBLE:CONFIRME | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-004 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-005 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-006 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-007 | ELIGIBLE:CONFIRME | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-008 | ELIGIBLE:CONFIRME | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
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
