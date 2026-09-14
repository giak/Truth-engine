# Plan de narration et de prose, V4.4 — ce que le brainstorm « déchèteries » change ici

**Statut** : **N1 appliquée le 13 septembre 2026** (16 sous-titres, variante longue, décision de l’auteur). Le reste du plan est un refus motivé et n’est pas appliqué.
**Objet mesuré** : `01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md`. Diagnostic à l’empreinte `a9db157b…e29d53`, 10 248 mots, 339 lignes, 6 titres. Après N1 : empreinte `d6cf21a3…1bd0f9`, 10 377 mots, 371 lignes, 22 titres.
**Entrée** : brainstorm de l’auteur sur la narration, la prose, la sémantique et la dialectique, rédigé pour un autre article (déchèteries), transmis le 13 septembre 2026.
**Méthode** : mêmes compteurs appliqués à l’article et à cinq articles publiés du corpus, en Markdown, mesurés comme lui. Aucune préférence esthétique sans mesure.
**Suite des tranches T1 à T6** : closes le 13 septembre 2026. Ce plan ouvre un **second cycle**, noté N.

---

## 0. Ce que j’ai mesuré, et ce que je n’ai pas pu mesurer

Cinq articles du corpus, mesurés par le même script que l’article :

| Compteur | Article | ingérence-sans-mesure | post-démocratie | opacité-accès-différencié | déchèteries | impossible-rassemblement |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Mots (mêmes filtres) | 9 615 | 2 490 | 2 240 | 4 499 | 4 998 | 4 366 |
| **Médiane mots / paragraphe** | **79** | 54 | 46 | 81 | 105 | 84 |
| Médiane mots / phrase | 16 | 17 | 15 | 10 | 19 | 16 |
| Phrases de plus de 35 mots | 11,3 % | 7,8 % | 4,2 % | 0,3 % | 16,5 % | 11,0 % |
| Paragraphes de moins de 15 mots | 4 % | 5 % | 0 % | 4 % | 4 % | 2 % |
| Paragraphes d’une seule phrase | 6 % | 21 % | 2 % | 2 % | 6 % | 11 % |
| Médiane phrases / paragraphe | 4 | 3 | 3 | 7 | 5 | 5 |
| « je / j’ » | **3** | 0 | 0 | 0 | 0 | 0 |
| **Titres pour 1 000 mots** | **0,6** | 4,0 | 9,8 | 2,0 | 2,6 | 1,8 |

Les deux articles que le brainstorm cite comme modèles — *Qui fact-checke les fact-checkers ?* (25 août 2026) et *Qui fabrique l’autorité du vrai ?* (20 août 2026) — **n’ont pas pu être mesurés**. Les deux captures du bundle sont des pages rendues sans conteneur d’article ni `<h1>` (« markup » : 0 occurrence) ; l’extraction la plus large rend 15 480 mots et 465 paragraphes, ce qui est le signe d’une capture polluée par la navigation et les articles liés, pas d’un texte. **Je ne reprends donc pas à mon compte les « 38 à 39 mots de paragraphe médian » du brainstorm** : cette valeur n’est vérifiable ni sur ces deux fichiers, ni sur les cinq articles publiés mesurables, dont la médiane va de 46 à 105.

---

## 1. Les dix points du brainstorm, passés au test

| # | Affirmation du brainstorm | Vérification sur cet article | Verdict |
| --- | --- | --- | --- |
| 1 | L’article est fait de « petits bouts de phrases », de « listes de substantifs montées en prose » | 4 % de paragraphes de moins de 15 mots, comme le corpus (0 à 5 %). Les énumérations de quatre items et plus sont à 5,0 pour 1 000 mots, contre 2,3 à 6,2 pour le corpus (mesure de la partie 0 du plan de forme) | **prémisse fausse** |
| 2 | L’unité élémentaire doit être le raisonnement : fait, contradiction, qualification, conséquence | C’est exactement le gabarit F-10, diagnostiqué et corrigé en T4 sur neuf occurrences, et l’ouverture a été réordonnée en T3 sur le modèle « fait puis limite » | **déjà fait** |
| 3 | Le texte ne doit pas écrire « neutre » : il doit nommer ce qui l’inquiète puis se discipliner | L’encart d’ouverture fait les deux en quatre paragraphes : « Je cherchais des commanditaires, des chaînes, un centre. J’ai trouvé des leviers, des accès, des conditions, et presque aucun ordre », puis la série des refus (« un acteur qui finance n’est pas un acteur qui ordonne ») | **déjà fait** |
| 4 | Ouvrir par une anomalie concrète, pas par la documentation | Ouverture actuelle : le communiqué du 5 novembre 2014, la date, le montant, le calendrier, puis « Ce que cet article cherche est ailleurs : dans la chaîne qui y conduit, et dans le point exact où elle s’interrompt ». Le bloc de limitations méthodologiques a été déplacé en T3 | **déjà fait** |
| 5 | Les sous-titres doivent penser, pas étiqueter | **Écart mesuré.** L’article titre 0,6 fois pour 1 000 mots contre 1,8 à 9,8 pour le corpus. Aucun `###`. Les parties I, III et IV courent sur 2 097, 2 789 et 1 338 mots sans une seule respiration | **défaut réel, voir §2** |
| 6 | Pratiquer la contradiction à l’intérieur de l’accusation | Cas Alstom (B 53), gaz russe (B 57), Lituanie (B 59), Rockhopper (B 179), Djebbari (B 241) : fait, puis ce que la pièce ne permet pas, puis la conclusion calibrée | **déjà fait** |
| 7 | Avancer par retournements | La partie IV établit qu’un recours peut exister sans être un contre-pouvoir ; la section finale repose sur une thèse révisée (« après une révision de thèse », B 211 ; « Cette conclusion modifie sensiblement la thèse que j’avais défendue », B 203) | **déjà fait** |
| 8 | Le « je » garantit la méthode ; le narrateur ne doit pas être effacé | **L’article est le seul des six à employer la première personne** : trois occurrences, contre **zéro** dans les cinq articles publiés mesurables | **prémisse fausse pour ce corpus** |
| 9 | Les phrases courtes cristallisent, elles ne transportent pas les données | 5 paragraphes courts hors listes, tous des formules de cristallisation (B 157, B 211, B 219, B 227) ou des entrées de liste. Aucun paragraphe court ne porte de donnée | **déjà fait** |
| 10 | La prose doit accepter la complexité : phrases de 30 à 40 mots, paragraphes de 70 à 100 mots | Médiane 79 mots par paragraphe, 11,3 % de phrases de plus de 35 mots, contre 46 à 105 mots et 0,3 à 16,5 % pour le corpus | **déjà fait** |

**Verdict général** : sept des dix points sont déjà satisfaits, et **le brainstorm se trompe sur deux d’entre eux** pour cet article précis — il recommande plus de paragraphes courts et plus de « je », alors que l’article est déjà dans la plage du corpus sur le premier et qu’il est le seul du corpus à employer le second. **Un défaut réel sort de la mesure : le sous-titrage.**

---

## 2. Le défaut, chiffré

| | Article | Corpus |
| --- | --- | --- |
| Titres de niveau 2 ou 3 | **6** (I, II, III, IV, section finale, « Pour aller plus loin ») | 8 à 22 |
| Sous-titres de niveau 3 | **0** | présents dans les cinq |
| Densité | 1 titre pour **1 603 mots** | 1 pour 102 à 546 mots |
| Plus longue section sans respiration | **2 789 mots** (partie III, 26 paragraphes) | — |

Les cinq articles mesurables titrent tous plus que l’article, et trois d’entre eux deux à seize fois plus. L’article est aussi le plus long de tous : c’est celui qui aurait le plus besoin de repères, et c’est celui qui en a le moins.

**Pourquoi c’est un défaut de fond et pas d’esthétique.** La thèse de l’article est que trois niveaux voisins ne s’impliquent pas l’un l’autre. Une partie de 2 789 mots qui traite successivement du financement de capacité, de la nomination espagnole, de la porte tournante, de la qualification juridique, de la corruption marchés publics, des huit raccourcis et des quatre degrés ne permet pas au lecteur de voir où l’on passe d’une distinction à l’autre. Le texte fait le travail ; sa structure ne le montre pas.

---

## 3. Sous-titres proposés, verbatim

Règles appliquées : aucun énoncé nouveau, aucune affirmation sur le monde qui ne soit déjà dans le paragraphe qui suit, `LOCKED_TERMS` respectés, aucun tiret cadratin, aucun `[n]`. Chaque proposition est celle du bloc qu’elle ouvre, et non une étiquette de thème.

**Partie I** (2 097 mots, 0 sous-titre aujourd’hui → 4)

| Avant | Sous-titre proposé |
| --- | --- |
| B 41 | `### Le levier le plus direct n’est pas une opinion : c’est un accès` |
| B 51 | `### Alstom : le levier est identifiable, son poids dans la décision ne l’est pas` |
| B 63 | `### La condition est un mécanisme ; la coercition qualifie la relation` |
| B 77 | `### Ce qui se voit plus tôt, et ce qui s’arrête avant la décision` |

**Partie II** (1 153 mots → 2)

| Avant | Sous-titre proposé |
| --- | --- |
| B 87 | `### Peser sur une norme avant qu’elle existe` |
| B 101 | `### Sélectionner n’est pas orienter` |

**Partie III** (2 789 mots → 5)

| Avant | Sous-titre proposé |
| --- | --- |
| B 119 | `### Financer une capacité n’est pas commander une opération` |
| B 123 | `### Trois dossiers, un même fil, trois issues différentes` |
| B 137 | `### La qualification juridique n’est pas la causalité` |
| B 145 | `### Corruption établie, pacte corruptif non établi` |
| B 163 | `### Trois unités, un contrôle interne, quatre degrés` |

**Partie IV** (1 338 mots → 3)

| Avant | Sous-titre proposé |
| --- | --- |
| B 177 | `### Un recours existe : est-ce un contre-pouvoir ?` |
| B 189 | `### La cible peut être son propre contre-pouvoir` |
| B 201 | `### La décision finale change de nature d’un dossier à l’autre` |

**Section finale** (1 261 mots → 2)

| Avant | Sous-titre proposé |
| --- | --- |
| B 219 | `### Trois paliers ne se démontrent pas au même prix` |
| B 236 | `### Huit dossiers, huit fonctions de preuve` |

**Total : 16 sous-titres**, soit 22 titres pour 10 377 mots, **2,1 titres pour 1 000 mots**. Cela place l’article entre `opacité-accès-différencié` (2,0) et `déchetteries` (2,6), et **en dessous du maximum du corpus** (post-démocratie : 9,8). Le plus long bloc sans respiration passe de 2 789 mots à **923 mots**.

### 3.1 Ce qui a été appliqué, et les six écarts au tableau ci-dessus

**Dix des seize intitulés sont appliqués verbatim.** Six ont été reformulés en cours de route, pour un motif vérifiable : **ils répétaient mot pour mot la première phrase du paragraphe qu’ils ouvrent**, ce qui fait d’un titre une redite et non une question.

| Cible | Proposition initiale | Appliqué | Motif |
| --- | --- | --- | --- |
| B 51 | `### Alstom : le levier est identifiable, son poids dans la décision ne l’est pas` | `### Alstom : une pression établie, une vente non attribuable` | la phrase d’ouverture dit « car le levier est identifiable mais son poids dans la décision finale ne l’est pas » |
| B 63 | `### La condition est un mécanisme ; la coercition qualifie la relation` | `### Financer sous conditions n’est pas contraindre` | cette formule est la **chute** du bloc (B 85) ; en titre, elle la désamorce |
| B 77 | `### Ce qui se voit plus tôt, et ce qui s’arrête avant la décision` | `### Tenir une position n’est pas l’activer` | reprise littérale de l’ouverture (B 15) ; l’intitulé reprend le point du bloc (B 87) |
| B 137 | `### La qualification juridique n’est pas la causalité` | `### Qualifier n’est pas causer` | la phrase d’ouverture dit « la séparation entre qualification juridique et causalité » |
| B 189 | `### La cible peut être son propre contre-pouvoir` | `### Une option peut être rouverte, mais des années plus tard` | la phrase d’ouverture dit « un contre-pouvoir peut aussi exister au sein même de la cible » |
| B 201 | `### La décision finale change de nature d’un dossier à l’autre` | `### Aucun score commun, un profil par dossier` | la phrase d’ouverture dit « La décision finale, elle, n’est pas la même d’un dossier à l’autre » |

**Une affirmation de ce plan que la mesure a corrigée** : le §3 annonçait « aucune section ne dépasse alors 900 mots ». Faux : le bloc « Corruption établie, pacte corruptif non établi » fait **923 mots**. L’affirmation est rectifiée ci-dessus, pas effacée. Aucun sous-titre supplémentaire n’a été ajouté pour la faire tenir : le bloc est homogène (corruption dans les marchés publics, Alstom, Bailey, compensations légitimes), et le couper aurait séparé le contre-exemple de son cas.

**Variante courte, 9 sous-titres** : ne garder que B 41, B 51, B 63, B 77, B 119, B 123, B 137, B 163, B 219. Densité 1 pour 700 mots, encore sous le corpus pour l’article le plus long. **Variante longue écartée** : un sous-titre par paragraphe donnerait 117 titres, sans rapport avec le corpus.

---

## 4. Ce que je recommande de ne pas faire

1. **Ne pas multiplier les paragraphes courts.** L’article est à 4 %, comme le corpus. Descendre suppose de couper des paragraphes de raisonnement en « fait / contradiction / formule », c’est-à-dire de défaire exactement ce que T3 et T4 viennent de reconstruire. Le brainstorm vise ici un autre article que le sien.
2. **Ne pas ajouter de « je ».** L’article en a trois, le corpus publié mesurable en a zéro. La première personne est déjà là où elle compte : l’encart d’origine et le changement de position. En ajouter ailleurs ferait bouger l’article **hors** de sa famille éditoriale, pas dedans.
3. **Ne pas transformer la liste de B 221 en prose.** « Une participation, un décret, une notification, une part de capital, une confiscation payée, une livraison interrompue, un texte modifié, une autorisation refusée, une exposition judiciaire » est l’inventaire de ce qui est établi, sous le palier qui porte ce nom. Le brainstorm dénonce les listes qui **transportent des données à la place d’un raisonnement** ; ici le raisonnement est dans les deux paragraphes qui précèdent, et la liste est sa conclusion. La convertir en phrases allongerait le palier sans rien ajouter.
4. **Ne pas réécrire les phrases de plus de 35 mots.** 11,3 % contre 0,3 à 16,5 % : dans la plage, et le corpus le plus récent (déchèteries) est à 16,5 %.
5. **Ne pas toucher aux titres de niveau 2 ni aux titres courants.** Ils ont été fixés en T5 et sont mesurés comme les plus conformes du document (densité mise à part, tous les titres de l’article énoncent un mécanisme ou une thèse, comme le brainstorm le recommande).

---

## 5. Tranche proposée

| Tranche | Contenu | Lignes touchées | Effet | Contrôle |
| --- | --- | --- | --- | --- |
| **N1** | 16 sous-titres de niveau 3, insérés avant les paragraphes listés au §3 | **+32 lignes**, 339 → **371** | Aucun mot d’argument ajouté ; aucun paragraphe déplacé ; aucun numéro de registre touché | **faite** le 2026-09-13, empreinte `d6cf21a3…1bd0f9` |
| **N2** | Variante courte de 9 sous-titres | non retenue | — | l’auteur a choisi la variante longue |

**Contrôles de N1.** Empreinte `a9db157b…e29d53` → `d6cf21a39618b3cd4d8df81754d41509017d20073b187415a43924a0591bd0f9`. Corps 10 248 → **10 377** mots, dont **129 exactement** apportés par les seize intitulés. **Corps hors titres : 10 178 → 10 178 mots, identique**, et les compteurs de non-régression sont inchangés sur ce périmètre (`\bpas\b` 106, `\bne\b` 89, négations simples 57, réfutation de thèse 31, « démontre » 11, « peut / peuvent » 80, « hypothèse » 4, phrases 495). HARD_GATE vert sur les onze items, registre à 64 entrées inchangé, guillemets 52/52.

**Un chiffre à lire correctement** : le décompte `\bpas\b` du corps complet passe de **107 à 113**. Ce n’est pas de l’écriture dans l’argument : **six** des nouveaux intitulés portent un « n’est pas » (« n’est pas une opinion », « n’est pas contraindre », « n’est pas l’activer », « n’est pas orienter », « n’est pas commander », « n’est pas causer »), et le septième « pas » du corps appartient au titre `## IV. Le contre-pouvoir n’annule pas le pouvoir`, qui existait déjà. Mesure : 107 avant, dont 1 dans un titre ; 113 après, dont 7 dans des titres ; **hors titres, 106 dans les deux cas**. Mon premier calcul annonçait « quatre occurrences ajoutées et 111 au total » : il était faux, et il est corrigé ici plutôt que laissé passer.

**Coût structurel, à connaître avant de décider** : chaque insertion décale les lignes suivantes de +2, donc **la carte D → courant devra être refaite**, comme après T6. Les ancres du `SUIVI` §4 (figures retirées) devront être recalculées une seconde fois. C’est le seul effet indésirable, et il est mécanique.

**Ce que N1 ne fait pas** : aucune coupe, aucune phrase réécrite, aucun changement de thèse, aucune entrée de registre, aucun déplacement de paragraphe. La tranche est entièrement additive.

---

## 6. Décisions ouvertes

1. **N1 dans la variante de 16 ou dans la variante de 9 ?** Mon avis : 16 pour un texte de cette taille, mais l’écart avec `impossible-rassemblement` (1 pour 546) reste défendable si l’auteur veut un rendu plus continu.
2. **Les sous-titres doivent-ils être visibles sur Substack ?** Si la mise en page publiée les rend en petit corps, une partie du bénéfice disparaît. Cela se décide au moment de la mise en forme, pas ici.
3. **La longueur.** Elle reste la question de fond, et elle n’est pas traitée par N1 : 10 248 mots contre environ 5 700 de médiane de corpus. Le brainstorm ne la règle pas non plus, et il recommande au contraire des paragraphes plus longs. **Aucune tranche T1 à T6 n’est une coupe, aucune tranche N ne l’est non plus.**
