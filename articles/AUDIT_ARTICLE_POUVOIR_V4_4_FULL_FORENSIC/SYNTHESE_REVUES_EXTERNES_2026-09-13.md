# Synthèse des revues externes par rôles — 13 septembre 2026

Objet : `01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md`, empreinte `d6cf21a3…` (état après N1), **non modifié par cette passe**.

Méthode : **neuf fils ChatGPT indépendants**, un rôle par fil, l’article **en pièce jointe** (jamais recopié, jamais désigné par un chemin local). Prompts conservés à côté des réponses dans `07_COLLAB_CHATGPT/reviews_v4_4/`. Aucun round n’a échoué, aucune garde ne s’est déclenchée.

**Cette synthèse vérifie les critiques contre le texte.** Un relecteur externe peut se tromper : trois des critiques les plus fortes sont confirmées par recherche dans le fichier, et deux sont exagérées — c’est écrit ci-dessous, section 4.

---

## 1. Le résultat qui compte : quatre rôles indépendants nomment le même défaut

Aucun de ces quatre fils n’a vu les autres. Ils arrivent pourtant sur la même phrase du même problème, formulée de quatre façons :

| Rôle | Formulation |
|---|---|
| 1 Contradicteur épistémologique | « La proposition vulnérable n’est pas “certains leviers modifient les conditions sans commander”, qui résiste, mais “l’asymétrie de preuve révèle quelque chose de général sur la manière dont le pouvoir devient observable” » |
| 2 Calibration | le texte glisse de « limite de la preuve » à « limite du pouvoir » |
| 8 Avocat du diable | « il transforme une asymétrie d’observabilité en propriété du pouvoir » |
| 10 Spécialiste du domaine | « repositionner l’article comme une contribution de méthode probatoire, et non comme une théorie du “pouvoir sans commande” » |

**Ce que cela veut dire concrètement.** La borne existe déjà dans le texte (l. 33 : « ce qui est établi ici est ce qu’un corpus documentaire permet d’établir, plus qu’une description générale de la manière dont le pouvoir s’exerce »). Mais elle est **dans un paragraphe méthodologique**, tandis que le **titre**, la ligne 15 (« Ce n’est pas le pouvoir qui commande, mais celui dont on peut établir qu’il pèse sans pouvoir établir qu’il a ordonné ») et la **conclusion** parlent du pouvoir sans marquer cette frontière. Quatre lecteurs distincts ont fait le trajet titre → conclusion, et le titre a gagné.

C’est un défaut de **calibration entre le titre et la preuve**, pas un défaut de fait. Il est réparable par retouche, pas par réécriture.

## 2. Le second défaut, plus profond : le standard causal n’est pas symétrique

Énoncé par le rôle 1 comme **bloquant**, retrouvé par le rôle 8 en d’autres mots, et par le rôle 3b sous une autre forme encore :

> l’amont bénéficie parfois de **chronologie + concordance**, alors que l’aval exige une pièce reliant explicitement les termes et l’élimination des explications concurrentes. Tant que le standard probatoire n’est pas symétrisé, le résultat « le dernier lien est moins prouvé » est partiellement produit par la méthode qui le mesure.

R3b le quantifie par un troisième chemin : la conclusion dit « **aucun des cas examinés** » (l. 255) **sans que le dénominateur existe**. Huit ? Onze ? Quarante-cinq investigations ? Seulement les dossiers du corps ? Un « aucun » sans N n’est pas auditable — et c’est la proposition quantitative la plus forte de l’article.

**Conséquence pratique : ce défaut ne se corrige pas par une phrase.** Il demande soit d’écrire le standard unique appliqué à chaque flèche, soit de rabattre la conclusion sur ce que le standard asymétrique permet réellement de dire (« l’écart de preuve peut tenir, en partie, à ce que les documents laissent voir plus volontiers un point de passage qu’un ordre » — l’article l’écrit déjà à la l. 33). **Arbitrage à toi, pas correctif que je m’approprie.**

## 3. Ce que la vérification confirme dans le texte

Chaque ligne ci-dessous a été contrôlée par recherche dans le fichier, pas reprise de confiance.

| # | Critique | Vérification | Gravité retenue |
|---|---|---|---|
| **V1** | R3b : l’ouverture se contredit — « Quarante-sept jours plus tard, le 22 décembre » puis « **Entre les deux dates**, neuf mois de négociations » | **CONFIRMÉE.** l. 13. Du 5 nov. au 22 déc. il y a 47 jours, pas neuf mois ; les neuf mois vont de février à novembre 2014. L’erreur est **dans la première phrase du corps et incontestable**. Introduite par T3 (ouverture sur le fait daté) ; ni T3 ni le contrôle terminal ne l’ont vue. | **bloquant, et trivial à corriger** |
| **V2** | R2 : « **L’influence normative peut donc être observée** dans l’accès au processus, la formulation d’une demande et les modifications qui l’accompagnent, sans que cette concordance suffise à prouver une capture » (l. 105) affirme une influence observable tout en niant la causalité trois mots plus loin | **CONFIRMÉE verbatim.** C’est exactement le mouvement que l’article interdit ailleurs. | **majeur, correctif local** |
| **V3** | R3b : les seuils 25 % / 10 % du corps (l. 81) sont énoncés sans leur périmètre, alors que l’entrée de registre [63] précise « seuils inapplicables aux investisseurs de l’Union européenne et de l’Espace économique européen » | **CONFIRMÉE.** Le corps est **moins précis que sa propre source**, sur un passage qui sert précisément à distinguer l’investisseur tiers. | **majeur, une incise suffit** |
| **V4** | R3b : « taux de base » (l. 274) adossé à 751 projets traités / 639 avis rendus / 95,5 %, dont **112 projets sans statut expliqué** | **CONFIRMÉE sur les nombres** (l. 149). L’arithmétique est juste (95,5 + 4,5 = 100 ; base = 639), mais le sort des 112 autres n’est pas dit, et le mot « taux de base » est employé après. | **majeur, une incise suffit** |
| **V5** | R3b : « Trois dossiers » (l. 137), « Huit dossiers » (l. 266), « Deux dossiers » (l. 291), « aucun des cas examinés » (l. 255) — **l’unité de comptage n’est pas stabilisée** | **CONFIRMÉE.** L’article définit lui-même trois unités à la l. 187 (cas / affirmation codée / relation) et dit « cet article raisonne en cas ». Les titres comptent ensuite des **entrées de fonction**, pas des cas, et la conclusion compare à « ces deux niveaux » (l. 245) alors que la série de référence compte **trois** termes (l. 87). | **majeur** |
| **V6** | R4 : « **chronologie suspecte** » (l. 169, Hugh Bailey) et « des éléments relatifs à des **dons personnels ultérieurs provenant de certains de ces milieux** » (l. 167) | **CONFIRMÉES verbatim.** Ce ne sont pas des inventions du relecteur. La seconde phrase attribue la provenance sans nommer les milieux ; la première qualifie de « suspecte » la trajectoire d’une personne nommée. | **à arbitrer : risque juridique, pas défaut de fond** |
| **V7** | R4 : vérifier avant publication le décret n° 2026-718, l’article R. 151-2, la directive (UE) 2026/1021 et la nature exacte des procédures DOJ | **CONFIRMÉE sur l’existence** : toutes ces références sont dans le texte (l. 155, 161, 81 ; registre [42], [63], [64]). Ce sont des textes de 2025-2026, donc à re-contrôler **texte en main** avant publication. | **contrôle à faire, non un défaut** |
| **V8** | R9 : deux passages font décrocher — le bloc Bachrach/Baratz/Lukes/Strange + représentativité avant la partie I, et le détail réglementaire du filtrage | **CONFIRMÉE sur le second** ; noté, et **il faut assumer que c’est un correctif récent** (le seuil français ajouté en P6/T1 a coûté en lisibilité ce qu’il a rapporté en tranchant). Le premier décrochage est le prix du cadrage théorique. | **éditorial, à arbitrer** |

## 4. Ce que la vérification ne confirme pas — deux critiques exagérées, une injuste

Je ne reprends pas ces points à mon compte, et ils ne doivent pas servir de base à une correction.

1. **R1, la liste des « capacités » (gravité annoncée : bloquant).** Le relecteur écrit que la synthèse « range ensemble une participation, une part de capital, une livraison interrompue, un texte modifié… Ce ne sont manifestement pas tous des capacités ». **Il a raison sur le fond, tort sur la forme** : l. 251, le texte annonce lui-même « les capacités, c’est-à-dire les positions et les droits tenus, **ainsi que les actes datés** ». Il n’y a donc pas de dérive silencieuse, mais **un mot qui porte deux contenus** — « capacités » coiffe des actes, alors que la grille de la l. 87 définit capacité = position et pouvoir exercé = acte. **Défaut réel, de nature terminologique ; gravité mineure-majeure, pas bloquante.**

2. **R3b, 392 / 182 / 54 % / 6 refus (gravité annoncée : majeur).** Le relecteur conclut que « le lecteur est tenté de fermer l’équation alors qu’elle ne se ferme pas ». **Mais l. 77 le texte écrit noir sur blanc « 6 refus sur la période 2022-2024 »** : la fenêtre est donnée. Il reste un risque de fausse soustraction, pas une erreur. **Gravité mineure.**

3. **R4, « la directive anticorruption de 2026 » : ma première lecture a cru à une invention.** Vérification faite, l’article écrit « **directive européenne 2026/1021** » relative à la lutte contre la corruption (l. 155, registre [42]). **Le relecteur est exact** ; c’est ma recherche qui était mal formulée. Point consigné pour que la vérification ne soit pas refaite à l’envers.

## 5. Ce que les rôles ont trouvé et que la passe interne n’avait pas

| Apport | Rôle | Pourquoi la passe interne ne l’avait pas vu |
|---|---|---|
| **L’asymétrie du standard causal** entre maillons | 1, 8 | Le contrôle terminal vérifiait que chaque proposition **désigne** sa garantie ; il ne comparait pas les **seuils** d’une flèche à l’autre. |
| **Le 0/N de « aucun des cas examinés »** | 3b | Le décompte de chaque nombre était fait, pas celui de **l’unité de comptage** elle-même. |
| **L’erreur de l’ouverture (47 jours / neuf mois)** | 3b | Le contrôle portait sur les garanties et les marqueurs de forme, pas sur l’arithmétique interne d’une dateline. |
| **La capturabilité des formules négatives** | 7 | Questions jamais posées : non pas « est-ce vrai ? » mais « que devient cette phrase tronquée ? ». |
| **Le point de décrochage réel du lecteur** | 9 | Aucun rôle interne ne simule un lecteur qui ne connaît pas le dossier. |
| **Le trajet titre → conclusion** | 1, 2, 8, 10 | Le travail de forme a resserré les bornes internes sans toucher au **titre**, qui est le seul énoncé que personne ne relit dans son contexte. |

## 6. Triage proposé (non appliqué)

**Avant publication, quel que soit l’arbitrage sur le reste :**

1. **V1** — supprimer « Entre les deux dates » à la l. 13. Erreur factuelle incontestable, correctif d’un mot.
2. **V2** — l. 105 : « l’influence normative peut donc être observée » → « une démarche d’influence et une concordance sont observées ; la causalité n’est pas établie ».
3. **V3** — l. 81 : ajouter le périmètre investisseurs à l’endroit des seuils, pas seulement au registre.
4. **V4** — l. 149 : « **parmi les 639 avis rendus**, 95,5 %… ».
5. **V5** — décider l’unité : soit « fonctions de preuve » dans les titres, soit un N nommé pour le test final. À trancher **avant** de toucher aux titres, car cela décide de la nature de la conclusion.

**Puis, arbitrages de fond (chacun un chantier, aucun ne se mélange à l’autre) :**

6. Le standard causal unique (section 2) — le seul point qui peut changer le **statut** de la thèse.
7. Le titre et la ligne 15 (section 1) — calibration, pas réécriture.
8. La capturabilité (R7) : trois citations courtes à border dans la même phrase, dont « N’est établi dans aucun des cas examinés » (l. 255).
9. Le risque juridique V6 : décision, pas rédaction.
10. L’ouverture après la l. 13 et le détail réglementaire (V8) : coupe éditoriale, à traiter avec la longueur.

**Ce que je ne recommande pas de faire** : corriger 1 à 9 dans une seule passe. Les points 6 et 7 déplacent le sens ; les points 1 à 5 sont mécaniques. Les mélanger rendrait toute régression inattribuable.

## 7. Bornes de cette synthèse

- **Aucun fait externe n’a été revérifié.** Les neuf rôles n’avaient pas accès aux 64 sources ; leurs critiques de « vérité externe » ne figurent pas ici.
- **Trois revues seulement ont été lues intégralement** (rôles 1, 3b, et les trios de tous). Les rôles 4 (35 ko) et 2 (19 ko) n’ont été exploités que par leurs sections vérifiées ; **leurs listes détaillées contiennent des points non repris ici**, à lire avant de clore.
- **L’auteur du texte et les relecteurs sont le même modèle.** Le rôle 10 le dit à sa manière : l’apport réel de l’article est méthodologique. Un désaccord interne au modèle n’est pas une validation externe ; il ne dispense d’aucune vérification sur source.
- **L’article n’a pas été modifié.** Empreinte `d6cf21a3…` inchangée après cette passe.
