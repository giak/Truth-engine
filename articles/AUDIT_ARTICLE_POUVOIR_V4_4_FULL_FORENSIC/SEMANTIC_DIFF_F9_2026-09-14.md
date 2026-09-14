# SEMANTIC_DIFF, tranche F9, les huit nombres et une citation mal assignée

Objet : `01_TARGET/ARTICLE_MASTERWORK_SOUVERAINETE_2026.md`, article retenu pour publication.
Empreinte avant : `6059938242b24e16bfe4c614aa6e7efa3ebe63b39ee8183401be90d7e305a204` (état après F8).
Empreinte après : **`b3478bac8d6d4b8616844baa5357dfc1f7ae3bafde8e69220766854b04a132d9`**.
307 → **314 lignes**, 52 941 → **58 282 octets**, 6 910 mots. Registre **70 → 77 entrées**.

**Une entorse de procédure, déclarée avant le reste.** F9 **n’a pas pris sa sauvegarde** avant d’écrire, contrairement à F1 à F8 : l’état après F8 n’est pas conservé sous forme de fichier. Tous les remplacements sont listés ci-dessous, ce qui rend la reprise possible à la main, mais la tranche n’a pas le filet qu’elle exige des autres.

Demande : « les huit nombres non sourçables » du §6 de la note de vérification, mandat « chacun demande soit une pièce, soit un retrait ».

**Résultat : six nombres sourcés, deux formulations bornées, un membre retiré, et une citation mal assignée trouvée en chemin.** La quatrième catégorie n’était pas au programme et c’est la plus grave.

---

## 1. La citation mal assignée : Doppelgänger n’est pas dans le rapport qu’on lui prête

L’article attribuait à **[3]** trois choses : l’identification de l’opération « Doppelgänger » « à partir de 2022 par le service français VIGINUM », la création de « **des centaines de sites-clones** », et la détection de « **plusieurs centaines de manœuvres informationnelles par an** ».

Or **[3]** était cité par une URL qui ne mène à aucune pièce : `https://www.sgdsn.gouv.fr/viginum`, la page d’accueil du service. Le rapport visé a donc été **téléchargé et lu** : *Rapport d’activité VIGINUM 2024*, publié le 30 décembre 2025, 4,5 Mo.

**Trois constats, tous vérifiés dans le texte du rapport.**

1. **Le mot « Doppelgänger » n’y apparaît pas.** Pas une occurrence. Le service y décrit des modes opératoires, pas cette opération sous ce nom.
2. **Le chiffre « plusieurs centaines de manœuvres informationnelles par an » n’existe pas, et il portait sur le mauvais objet.** Le rapport compte, pour 2024 : **259 phénomènes inauthentiques détectés**, dont **174 liés à une ingérence numérique étrangère** ; **25 manœuvres informationnelles** visant les scrutins français, quatorze pour les européennes et onze pour les législatives ; **43** visant les Jeux de Paris. « Plusieurs centaines » décrit donc les **phénomènes inauthentiques**, pas les manœuvres, et la mention « par an » généralisait une année de référence.
3. **La bonne pièce pour Doppelgänger existait à côté.** L’opération est documentée par **EU DisinfoLab** (septembre 2022) et, pour la France, par le **rapport VIGINUM sur la campagne RRN du 19 juillet 2023**, dont le texte renvoie lui-même au rapport Doppelgänger d’EU DisinfoLab.

**Ce que la correction change.** La l. 70 nomme la campagne RRN et renvoie à [77] au lieu de [3] ; la l. 72 remplace le quantifier faux par **les trois chiffres du rapport** ; la l. 74 rattache la neutralisation à son mécanisme réel, les signalements techniques transmis à sept plateformes, « qui ont parfois conduit à des actions de modération ». L’article **gagne en précision** : 259, 174, 25 sont des chiffres que le lecteur peut vérifier dans une pièce datée, là où « plusieurs centaines par an » n’en était pas un.

**La ligne d’inventaire de la partie V** renvoie désormais elle aussi à [77], et non à [3].

---

## 2. Les six nombres sourcés, et leurs pièces

Sept entrées de registre ont été ajoutées, **[71] à [77]**, toutes vérifiées accessibles au 14 septembre 2026.

| Ligne | Avant | Après | Pièce |
|---|---|---|---|
| **9** et **21** | « 57,2 milliards d’euros » par an (prologue et encadré) | « **57,1 milliards d’euros** à sa défense nationale **en 2026** » | **[76]** Ministère des Armées, PLF 2026 : « une hausse de +6,7 milliards d’euros, portant la mission Défense à **57,1** milliards d’euros hors pensions » |
| **38** | « 8,97 Md$ […] représentant l’intégralité du résultat avant impôt annuel du groupe » | « 8,97 Md$ […], **la plus lourde alors payée par une banque étrangère aux États-Unis** » | **[75]** communiqué BNP Paribas du 30 juin 2014 (8,97 Md$ = 6,6 Md€) ; *L’Express* pour le superlatif |
| **46** | « un investissement initial de 4,8 milliards de dollars » | « **dont le coût total était évalué à** 4,8 milliards de dollars » | **[71]** communiqué TotalEnergies du 3 juillet 2017 ; CNBC (« a $4.8 billion deal ») ; fiche NIOC (« $4879 million ») |
| **55** | « une capitalisation détenue à **plus de 40 %** par des investisseurs nord-américains » | « **près de 40 %** de son capital détenu par des investisseurs nord-américains, **contre 25,3 % pour des actionnaires français** » | **[74]** *The Conversation*, 27 juillet 2025, d’après le document d’enregistrement universel |
| **61** | « les données de santé de **67 millions de citoyens** » | « de la **population couverte par l’assurance maladie, plus de 66 millions de personnes** » | **[73]** CNIL (plateforme des données de santé) ; Cuggia et al., 2019 (« SNDS covers 98.8% of the French population, more than 66 million persons ») ; Goldberg, *médecine/sciences*, 2021 |
| **111** | « 1 000 emplois net », « 50 000 euros par emploi manquant », emplois « pas créés » | mêmes paramètres, **plus l’issue** : « vingt-cinq emplois nets seulement ayant vu le jour […] et l’État a exigé la pénalité de **50 millions d’euros** prévue par la clause » | **[72]** Sénat, question écrite n° 17777 (25 juillet 2019) ; *Le Parisien* (5 février 2019) ; *Les Échos* (28 mai 2019) |

**Deux corrections de précision méritent d’être signalées**, parce qu’elles ne consistent pas seulement à ajouter une source.

- **57,1 et non 57,2.** Les deux chiffres circulent ; la source ministérielle donne **57,1 Md€ hors pensions** pour la mission Défense en PLF 2026, et le rapport parlementaire place 57,1 en 2026 et 57,2 **en 2027**. L’article portait le chiffre de l’année suivante, sur un exercice mal nommé. La ligne précise désormais l’année, ce qui la rend difficile à déplacer à nouveau.
- **« Plus de 40 % » devient « près de 40 % », et le contraste français est ajouté.** La source dit « près de 40 % […] contre 25,3 % pour les actionnaires français ». La comparaison est plus parlante que le superlatif et **elle est dans la pièce**.

---

## 3. Les deux formulations bornées, et le membre retiré

**Bornée, la causalité de l’EUCS (l. 61).** L’article écrivait : « **Sous la pression constante** de la Chambre de commerce des États-Unis et d’une coalition d’acteurs transatlantiques [51], ces clauses d’immunité juridique ont été progressivement retirées. » La pièce [51] est une **déclaration conjointe d’associations professionnelles** : elle documente une demande, pas une pression continue **ni** son effet. La phrase distingue désormais les deux : « La Chambre de commerce des États-Unis et des associations professionnelles transatlantiques **ont publiquement demandé le retrait** de ces clauses [51] ; elles ont été progressivement retirées. » Le fait est conservé, la causalité n’est plus affirmée.

**Borné, le quantifier des sites-clones (l. 70).** « **des centaines de** sites-clones » devient « **un réseau de** sites typosquattés ». Le rapport RRN parle de sites **typosquattés** et n’en donne pas le nombre : le quantifier part, le mécanisme nommé reste, et il est plus précis ainsi.

**Retiré, le membre non sourçable (l. 38).** « représentant l’intégralité du résultat avant impôt annuel du groupe » : aucune pièce ne l’établit, et la vérification n’a pas trouvé de source primaire du résultat avant impôt 2013 du groupe dans le temps disponible. Le membre a été **remplacé par un superlatif sourçable**, non par rien : l’article ne perd pas sa force, il change de garantie.

**Ce qui n’a pas été touché, et qui doit se dire.** Les deux nombres de défense (« 57,2 » corrigé) et le « 8,9 milliards de pénalités » du prologue reposent sur la même mesure ; le second n’a pas été repris, l’entrée [75] donnant 8,97 Md$. La mention « des centaines de postes » supprimés à Belfort est conservée et désormais adossée à *Les Échos*, qui titre sur « plus de 1 000 emplois » : l’article reste **en deçà** de sa pièce, ce qui est la bonne direction.

---

## 4. Retour en mémoire (Mnemolite), obligation du protocole Mémoire d’abord

Les recherches web de cette tranche ont été précédées d’une recherche en mémoire (service `healthy` au 14 septembre 2026) : **aucune des huit affirmations n’y était**, seule une note de projet sur les dépenses de santé étant remontée, sans rapport avec le Health Data Hub. Le retour a donc été écrit, trois faits vérifiés, chacun avec sa source primaire :

| Mémoire | Objet |
|---|---|
| `6fea6d4c-8c11-4917-915e-e3d1f3ee1dbf` | VIGINUM 2024 : 259 phénomènes inauthentiques, 174 INE, 25 manœuvres électorales, 43 JOP, absence du mot « Doppelgänger » |
| `239e333e-2c0c-4174-a7cb-34aa31cd8aa4` | PLF 2026 mission Défense : **57,1 Md€** hors pensions, et l’erreur d’année du chiffre 57,2 |
| `d2c637af-d455-48dd-8a68-136f881b4f72` | Doppelgänger : EU DisinfoLab (2022) et campagne RRN (VIGINUM, 19 juillet 2023) ; ne pas l’attribuer au rapport d’activité 2024 |

---

## 5. Contrôles

| Contrôle | Résultat |
|---|---|
| Lignes modifiées | **12** : 9, 21, 38, 46, 55, 61 (deux clauses), 70, 72, 74, 111, la ligne d’inventaire et l’entrée [3] |
| Lignes ajoutées | **7** (entrées [71] à [77]), 307 → **314** |
| Empreinte | `6059938242b24e16…` → **`b3478bac8d6d4b86…`** |
| Octets | 52 941 → **58 282** |
| Registre | **70 → 77 entrées**, numérotation continue 1 à 77 |
| Renvois `[n]` du corps sans entrée | **0** |
| Entrées jamais citées | **29**, inchangé : les sept ajoutées sont toutes citées |
| Formes fautives restantes | « 57,2 » **0** · « plus de 40 % » **0** · « intégralité du résultat » **0** · « des centaines de sites-clones » **0** · « plusieurs centaines de manœuvres » **0** · « sous la pression constante » **0** |
| Apostrophes | ASCII **0**, typographiques **368** |
| Cadres | **24 lignes à 75** et **4 lignes à 84**, aucun bord divergent (les lignes de tableau ne sont pas concernées) |
| Tirets cadratins | **0** |
| URL vérifiées | **13 des 16** URL des entrées nouvelles et de [3] répondent **200**, dont deux PDF téléchargés et lus (4,5 Mo et 3,9 Mo) · **3 répondent 403** aux requêtes automatisées (*Le Parisien*, *Les Échos*, groupe BNP Paribas) : c’est une protection anti-robot, **pas un 404**, mais ce n’est pas une vérification complète, et le montant de 8,97 Md$ du communiqué BNP a donc été relevé dans l’extraction du moteur de recherche, pas dans la page · la version française du rapport RRN renvoie 404, la version anglaise est citée et l’entrée le dit |

---

## 6. Ce que la tranche coûte, et ce qui reste ouvert

**Ce qu’elle coûte.** Trois formulations perdent leur tranchant : la pression « constante » sur l’EUCS, les « centaines » de sites-clones, et le rapport entre l’amende BNP et le résultat annuel du groupe. Les trois perdaient leur tranchant **parce qu’elles n’avaient pas de pièce**. Les chiffres du rapport VIGINUM, eux, en gagnent : 259, 174, 25 et 43 remplacent un quantifier creux.

**Ce qui reste ouvert, dans l’ordre où cela pèse pour une publication :**

1. **Les 77 renvois `[n]` dans le corps**, alors que la convention du corpus demande des sources nommées dans la prose : décision d’auteur, et c’est désormais le plus visible des écarts de forme.
2. **Les 29 entrées de registre jamais citées**, dont [5] [6] [7] (Integrity Initiative), pour lesquelles la note signale en outre que l’article porte la description **d’avant correction**, sans la réserve de chaîne de conservation de V4.5.
3. **Le recouvrement des standards techniques** entre les parties I et III.
4. **Le titre de l’article** et ses quatre adjectifs.
5. **Les espaces insécables**, décision de rendu.

**Ce que F9 ne prétend pas avoir fait** : les sept nombres n’ont pas tous été vérifiés à la source primaire. Le « 4,8 milliards » repose sur de la presse et une fiche d’opérateur, pas sur le contrat ; le « près de 40 % » repose sur un article universitaire qui cite le document d’enregistrement universel, lequel n’a pas été ouvert. Ces deux pièces sont **déclarées comme secondaires dans le registre**, et c’est ce qui les rend utilisables.
