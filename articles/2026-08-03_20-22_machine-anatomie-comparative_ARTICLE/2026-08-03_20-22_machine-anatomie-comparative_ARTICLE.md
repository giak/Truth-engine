# La machine qui documente les machines : anatomie comparative d’un atelier sans équivalent

*Une enquête peut être produite entièrement par un LLM. La publier sans travail humain dégrade pourtant le résultat. Entre les deux, il y a plus de deux ans de protocole, plusieurs modèles qui se contredisent, beaucoup de temps humain, et, pour la première fois, un dossier de fabrication téléchargeable que chacun pourra ouvrir.*

---

Le 31 juillet 2026, Résistance Cognitive publie une enquête d’environ 7 000 mots sur l’affaire Fedorova.

Le lecteur voit un article.

Derrière cet article se trouvent **120 fichiers**, dont 35 enquêtes successives, 36 résumés structurés, des travaux antérieurs, des comptages, plusieurs plans, quatre brouillons et trois audits critiques.

Parmi eux, un fichier est particulièrement important. Il compte 448 lignes et part d’un tweet de Caroline Fourest. Il contient une synthèse, une analyse des procédés de manipulation, un test des biais possibles, une chronologie, une cartographie des acteurs, plusieurs lectures contradictoires, des chaînes causales, un état des preuves, des scénarios, des limites et des sources.

Cette enquête a été produite **à 100 % par un LLM**, c’est-à-dire un grand modèle de langage.

L’expression mérite d’être prise au sérieux, mais aussi d’être définie précisément. Le texte de l’enquête n’a pas été écrit par un humain puis « amélioré avec de l’IA ». Une fois le sujet donné et le protocole chargé, le modèle a exécuté la recherche, utilisé les outils disponibles, organisé les éléments, formulé les hypothèses, distingué les états de connaissance et rédigé le dossier.

Ce fait me paraît, à lui seul, radical. Un LLM ne se contente plus ici de répondre à une question ou de résumer des documents. Il exécute une forme complète d’enquête selon une architecture prédéfinie.

Mais le même dossier montre aussitôt la limite de cette avancée. Certaines affirmations de cette première enquête seront précisées, réduites ou corrigées par les travaux suivants. Le fichier prouve qu’un LLM peut produire une enquête très structurée. Il ne prouve pas qu’il produit spontanément la vérité.

Toute l’identité de Résistance Cognitive tient dans cette tension : **la machine peut fabriquer l’enquête ; la qualité de la publication dépend encore du temps qu’un humain passe avec elle.**

---

## §1 : Une enquête entièrement produite par un LLM

Le fichier consacré au tweet de Caroline Fourest n’est ni une conversation avec un chatbot, ni un article généré en une commande.

Le modèle reçoit un cadre de travail qui lui indique quoi examiner, quelles recherches ouvrir, comment qualifier une source, comment séparer un fait d’une inférence, quand produire des hypothèses concurrentes, quelles limites signaler et dans quelles conditions il doit refuser de conclure.

Il doit notamment :

- décomposer les affirmations initiales ;

- rechercher les faits et leurs sources ;

- tester le cadrage du sujet et ses propres biais ;

- produire plusieurs lectures du même événement ;

- reconstruire la chronologie, les acteurs et les relations de causalité ;

- distinguer ce qui est confirmé, probable, contesté ou inconnu ;

- exposer les faiblesses de son propre dossier ;

- écrire et enregistrer l’enquête.

Le résultat est visible dans l’enquête APEX consacrée à l’affaire Fedorova, reproduite dans le [dossier ZIP](https://drive.proton.me/urls/MR7M17238R#GYDY1Hm67NRH). On peut discuter ses conclusions, relever ses erreurs ou contester sa méthode. On ne peut pas réduire ce fichier à quelques paragraphes de prose automatique : il s’agit bien d’un objet d’enquête produit par un modèle.

« 100 % LLM » ne signifie cependant pas « sans humain ».

Un humain a conçu le protocole et choisi le point de départ. Il lit ce que le modèle a produit, fait corriger ce qui lui paraît inexact et décide de ce qui peut être publié. Il peut consacrer deux heures à un sujet ou plusieurs jours à le reprendre.

L’automatisation concerne donc la production d’une pièce d’enquête. Elle n’abolit ni la conception de la méthode, ni l’arbitrage, ni la responsabilité éditoriale.

Cette distinction n’affaiblit pas l’expérience. Elle la rend compréhensible. Le seuil franchi n’est pas celui d’un « journaliste artificiel » autonome et fiable. C’est celui d’une machine capable d’exécuter, seule, un protocole d’enquête suffisamment élaboré pour produire une matière que l’on peut ensuite auditer, contredire et transformer.

---

## §2 : Plus de deux ans pour écrire les règles de la machine

Truth Engine n’est pas simplement une très longue consigne adressée à un modèle.

J’y travaille depuis plus de deux ans, sans y être à temps plein. Le projet s’est construit par essais, erreurs, ajouts, suppressions et réorganisations. Ce temps n’a pas seulement servi à améliorer une consigne. Il a servi à développer un protocole et le cadre logiciel capable de l’exécuter.

Au centre se trouve le KERNEL de Truth Engine v2 (reproduit dans le [dossier ZIP](https://drive.proton.me/urls/MR7M17238R#GYDY1Hm67NRH)). Il orchestre une architecture distribuée dans une trentaine de fichiers : ontologie, schémas de manipulation, menaces cognitives, étapes d’analyse, recherche, mémoire, modules spécialisés, vérification et formats de sortie. Le document d’architecture décrit leurs relations et le passage des données d’une étape à l’autre.

Le système emploie un **métalangage cognitif**. Des symboles comme Ξ, Λ, Ω ou Φ ne servent pas à donner une apparence savante au texte final. Ils compressent des catégories, des opérations et des conditions de chargement : quel phénomène chercher, quel module activer, comment marquer l’état d’une preuve, quelle vérification doit bloquer la sortie.

Autrement dit, ce langage essaie de transformer des consignes diffuses (« sois critique », « vérifie tes sources », « envisage un autre point de vue ») en opérations explicites et répétables.

Le KERNEL impose notamment :

- une suspicion symétrique envers les sources officielles, militantes, médiatiques et envers Truth Engine lui-même ;

- un registre des affirmations et des faits ;

- une analyse des cadrages, des manipulations possibles et des biais ;

- plusieurs perspectives défendues avec une force comparable ;

- une recherche des causes, des intérêts et des conséquences ;

- des seuils de contrôle capables d’interrompre une sortie jugée incomplète.

Cette conception me paraît unique parmi les systèmes publics que j’ai pu examiner. Cela ne suffit pas à dire qu’elle est révolutionnaire.

L’architecture contient d’ailleurs sa propre liste de « bizarreries » et de problèmes possibles : redondances, formules dupliquées, références fragiles, consommation inutile de contexte. Certains scores peuvent donner une impression de mesure plus solide qu’elle ne l’est réellement. Aucun protocole expérimental indépendant n’a encore démontré que ce métalangage rend les conclusions plus exactes qu’une méthode plus simple.

Je ne sais donc toujours pas si ce métalangage est un progrès réel ou une complication de plus.

Je sais en revanche ce qu’il permet déjà d’observer : soumis à ce cadre, un LLM peut produire une enquête complexe, structurée, sourcée et critiquable comme un objet autonome. **L’originalité de l’architecture est visible ; sa supériorité reste à démontrer.**

---

## §3 : Plusieurs LLM, parce qu’aucun ne mérite ma confiance

Parler de « l’IA » au singulier déforme le fonctionnement réel de Résistance Cognitive.

J’utilise plusieurs modèles de langage. Ils n’ont ni les mêmes qualités, ni les mêmes défauts, ni les mêmes angles morts. L’un peut être meilleur pour structurer une masse documentaire, un autre pour repérer une faiblesse logique, un autre encore pour contester un récit trop séduisant. Ils ont aussi leurs manies, leurs prudences excessives, leurs complaisances et leurs biais.

Je les fais donc travailler les uns contre les autres.

Un modèle produit une enquête ou un plan. Un autre reçoit la mission de l’auditer. Il peut demander de nouvelles recherches, signaler un saut logique, contester une source, relever une contradiction ou juger que la thèse dépasse les preuves. Le premier résultat n’est pas sacralisé ; il devient la matière première du suivant.

Cette pluralité ne crée pas une vérité automatique. Plusieurs modèles peuvent répéter la même erreur, partager des données d’entraînement proches ou se laisser convaincre par le même récit. Un audit par LLM n’est pas l’équivalent d’une expertise humaine indépendante. Et, au bout de la chaîne, la décision reste la mienne.

Mais les désaccords entre modèles ont une valeur pratique : ils empêchent qu’une seule manière de raisonner occupe tout l’espace. Ils transforment les différences de biais en friction productive.

La formule est paradoxale : je confie à des LLM la production intégrale des enquêtes parce que j’ai construit un cadre capable de les faire travailler ; je consacre ensuite beaucoup de temps à les contrôler parce que je ne leur fais pas confiance.

Truth Engine n’est pas une machine à laquelle je délègue mon jugement. C’est une machine destinée à produire assez de recherche, de contradiction et de matière pour que ce jugement puisse s’exercer.

### Indépendant, mais sans rédaction

Je suis seul. Je ne suis pas payé pour ce travail et je ne bénéficie d’aucun soutien financier, institutionnel, éditorial ou technique. Aucun employeur, actionnaire, annonceur, parti, rédaction ou organisme ne décide des sujets, de l’angle ou du moment de publication.

Cette situation fonde une indépendance matérielle réelle. Elle ne garantit ni ma neutralité, ni mon exactitude. Elle signifie seulement qu’aucun intérêt extérieur ne dispose d’un pouvoir formel sur la production. La contrepartie est immédiate : je n’ai ni équipe, ni secrétariat de rédaction, ni service juridique, ni réseau de correspondants pour compenser mes propres angles morts.

Je cherche à rester le plus neutre possible. Il ne s’agit pas de prétendre n’avoir aucune conviction, mais de séparer les faits, les inférences et les jugements ; d’appliquer la suspicion aux sources qui confortent ma thèse comme à celles qui la contredisent ; de signaler les réserves et de corriger ce qui se révèle inexact. C’est en ce sens que j’essaie de me rapprocher de la [Déclaration de Munich sur les devoirs et les droits des journalistes](https://cdjm.org/les-chartes/), sans prétendre qu’un protocole automatisé suffise à en garantir le respect.

Je nomme cette pratique **journalisme cognitif forensique** : journalistique par la recherche, la vérification et la publication de faits d’intérêt public ; cognitive parce qu’elle organise le travail conjoint de plusieurs modèles et d’un humain ; forensique parce qu’elle cherche à conserver les pièces, distinguer les degrés de preuve et rendre le raisonnement contestable.

### Le même procédé, mais pas la même qualité

Tous les articles de Résistance Cognitive sont produits selon la même architecture générale. Ce qui change est le nombre d’enquêtes ouvertes, le nombre de contre-enquêtes et d’audits, ainsi que le temps passé à lire, contester, relancer et corriger les modèles.

Certains articles sont produits plus vite. Leur résultat est moins bon.

Cette variation interdit de présenter Truth Engine comme une chaîne industrielle à qualité constante. Le protocole fournit une ossature commune ; il ne remplace pas l’attention. Quand je travaille réellement en binôme avec les modèles, les thèses se resserrent, les sources sont reprises et les contradictions deviennent visibles. Quand je laisse davantage les LLM travailler seuls, la prose peut rester convaincante alors que la solidité baisse.

**Même protocole ne signifie donc pas même qualité.** La différence se fait dans la profondeur de l’enquête et dans la présence humaine : du temps, de la concentration, du doute et la volonté de refaire ce qui paraît pourtant déjà terminé.

---

## §4 : Ce qu’il y a derrière l’article Fedorova

Le dossier Fedorova permet d’observer cette différence d’échelle.

Il ne contient pas une recherche unique suivie d’un article. L’enquête avance par couches. Une première investigation ouvre une question. Une autre vérifie un acteur. Une contre-enquête cherche ce qui pourrait invalider le premier récit. Des résumés communs rapprochent les résultats. Un rapport de synthèse organise la matière. Un plan tente d’en faire une histoire lisible. Un audit attaque ce plan. Plusieurs versions de l’article sont ensuite réécrites et de nouveau auditées.

Trois moteurs se partagent ces transformations.

**Truth Engine enquête.** Il applique le KERNEL, ouvre les strates, recherche les sources, distingue les faits des hypothèses et produit les dossiers APEX : le nom donné au niveau d’enquête le plus exigeant du protocole. Dans le cas Fedorova, sa sortie est constituée des 35 enquêtes brutes.**Sublimator condense.** Il extrait les faits atomiques, les acteurs, les causalités, les données, les limites et les sources ; il dédoublonne et remet chaque enquête dans un format commun. Sa sortie est constituée des 36 « quintessences » : une par strate, plus celle de la synthèse terminale.

**Writer transforme cette matière en publication.** Il rapproche les quintessences, produit le rapport de synthèse, construit un blueprint (le plan narratif détaillé), rédige les versions de l’article et les soumet à des audits antagonistes. C’est à ce stade que le dossier documentaire devient un texte lisible, et que le récit peut être rejeté s’il dépasse les preuves.

Ces moteurs ne sont pas trois auteurs artificiels autonomes qui se passeraient mécaniquement un dossier. Ce sont trois fonctions du système, exécutées par des LLM et pilotées par mes décisions, mes relances et mes corrections. Leur séparation permet de ne pas demander au même geste de rechercher, de compresser et de raconter.

### Penser et écrire ne sont pas la même tâche

L’écriture de l’article Fedorova a exigé des consignes d’orchestration et des rôles d’agents conçus spécifiquement pour ce dossier. Le Writer général ne suffisait pas : il fallait répartir la construction de la thèse, l’articulation des raisonnements, l’organisation narrative, la rédaction et la critique.

Il est difficile de demander au même modèle de soupeser trente-cinq enquêtes, de construire une pensée cohérente, de préserver les incertitudes et, simultanément, d’écrire dans un français irréprochable. Lorsqu’on lui demande de tout faire au même moment, il tend à sacrifier soit la profondeur du raisonnement, soit la qualité de la langue, soit la fidélité aux preuves.

Les synthèses et le blueprint ne sont donc pas des couches bureaucratiques ajoutées pour donner du volume au dossier. Ils séparent les charges cognitives. Les synthèses stabilisent la matière et les relations entre les faits. Le blueprint articule la pensée avant la rédaction. Le Writer peut alors se concentrer sur le texte, puis les audits vérifier que la qualité narrative n’a pas déformé le dossier.

### Un atelier de cartographie, pas une chaîne de montage

Le schéma Truth Engine → Sublimator → Writer décrit des fonctions, pas une succession irréversible. Truth Engine ressemble moins à une usine qu’à un **atelier de cartographie à distance**.

Internet n’est pas le territoire. Il est l’ensemble des traces que ce territoire laisse publiquement accessibles : documents, chiffres, images, déclarations, archives, bases de données. Chaque LLM travaille à partir de ces traces avec sa propre projection. Il révèle certains reliefs, en écrase d’autres et introduit ses déformations. Confronter plusieurs modèles revient donc moins à consulter plusieurs détenteurs de la vérité qu’à superposer plusieurs cartes imparfaites.

Le KERNEL fournit la légende et les règles de projection. Truth Engine établit les premiers relevés et dessine les couches d’enquête. Sublimator les ramène à des catégories, des coordonnées et une échelle communes. Les synthèses superposent les calques. Le blueprint organise le parcours du lecteur. Writer transforme enfin cet atlas technique en une carte lisible. Mon rôle est de choisir l’échelle, comparer les projections, demander de nouveaux relevés et décider quelles incertitudes doivent rester visibles.

L’atelier fonctionne par retours successifs. Une contradiction découverte pendant l’écriture peut rouvrir une enquête. Une nouvelle strate peut obliger Sublimator à reconstruire une partie ou la totalité des quintessences, déplacer la synthèse, renverser la thèse centrale et imposer une nouvelle version de l’article. On peut revenir du brouillon à la source, de l’audit à l’enquête ou de la conclusion à une nouvelle question. Le processus est **récursif et révisable** : la carte entière peut changer lorsqu’un seul relevé important se révèle faux.

L’article est la carte remise au lecteur. [Le ZIP du dossier de fabrication](https://drive.proton.me/urls/MR7M17238R#GYDY1Hm67NRH) contient l’atlas de travail : relevés, calques, légendes, corrections et tracés abandonnés. La mémoire conserve les cartes précédentes pour les futures enquêtes. Mais la carte n’est jamais le territoire : elle montre ce que les traces publiques permettent d’en reconstruire et doit laisser en blanc ce qu’elles ne permettent pas de connaître.

Cette cartographie produit ainsi trois objets emboîtés.

### 1. Un article destiné à être lu

C’est la carte publique et narrative. Elle doit rendre une enquête compréhensible sans obliger le lecteur à parcourir des centaines de pages de relevés intermédiaires.

### 2. Un dossier destiné à être inspecté

Il conserve les enquêtes, contre-enquêtes, « quintessences », comptages, synthèses, plans, audits et brouillons disponibles. C’est l’atlas de fabrication : on peut y retrouver l’origine d’une affirmation, observer une contradiction ou comparer le récit initial au texte publié.

### 3. Une mémoire destinée aux travaux suivants

Les faits, acteurs, mécanismes, sources et limites ne meurent pas avec la publication. Ils forment une réserve de cartes réutilisables : ils peuvent être rappelés, rapprochés d’un autre dossier et réexaminés lorsque de nouveaux éléments apparaissent.

Les opérations principales restent les mêmes (enquêter, condenser, relier, écrire, contester, corriger, conserver et réutiliser), mais leur ordre n’est jamais définitivement acquis. Chaque résultat peut devenir le point de départ d’une nouvelle boucle.

### Le récit le plus séduisant a été abandonné

La première construction de l’article Fedorova reposait sur un angle puissant : une procédure administrative utilisée comme projectile dans une guerre entre groupes de pouvoir. Le texte devait prendre la forme d’un « roman noir ».

L’audit a conclu que le plan avait tordu la réalité documentée pour la faire entrer dans un récit trop propre. Cet angle a été abandonné. La version finale défend une thèse plus étroite : l’État n’a pas rendu publique la chaîne de preuve qui permettrait de transformer une parole contestable en acte d’ingérence.

Ce recul compte davantage que le volume du dossier. Cent fichiers peuvent contenir cent fois la même erreur. Ici, l’accumulation a au moins permis de retirer au texte son meilleur récit parce que les preuves ne le portaient pas assez.

### Une trace riche, mais pas exhaustive

Il faut toutefois corriger une idée trop flatteuse : toutes les transformations ne sont pas enregistrées dans un journal complet.

Les commits Git (des instantanés enregistrés dans l’historique du projet) figent certains états importants. Les fichiers du dossier conservent de nombreuses étapes et corrections. Mais je peux aussi poser une question ponctuelle à un modèle ou lui demander de modifier un élément précis. Ces micro-interventions ne donnent pas toutes lieu à un commit, à une nouvelle version ou à une entrée détaillée dans un changelog, c’est-à-dire un journal des modifications. Elles peuvent toucher une enquête, une contre-enquête, une quintessence, un audit ou l’article lui-même.

Le ZIP ne constitue donc pas une chaîne de traçabilité parfaite où chaque phrase aurait son acte de naissance. Il s’agit d’une **archive de travail très riche, mais partielle** : elle permet de reconstruire les grandes transformations, pas chaque échange ni chaque retouche.

Cette nuance n’annule pas l’intérêt du dossier. Elle indique simplement ce que le lecteur pourra vérifier et ce qui continuera de dépendre de mon témoignage. Le ZIP qui accompagne cet article n’est pas un certificat d’infaillibilité. C’est un atelier suffisamment ouvert pour que chacun puisse examiner la fabrication, les reprises et les points aveugles d’un cas réel.

---

## §5 : En France, quels sont les parents les plus proches ?

Résistance Cognitive n’a inventé ni l’enquête longue, ni la critique des médias, ni l’analyse systémique, ni la transparence méthodologique. Plusieurs expériences françaises en possèdent une partie.

[**Le Monde diplomatique**](https://www.monde-diplomatique.fr/diplo/apropos/) est le parent le plus évident pour l’analyse de longue durée. Il relie les événements à l’histoire, aux structures économiques et aux rapports de pouvoir, sur des sujets internationaux et avec un usage important de la cartographie. Mais c’est une rédaction collective. Son produit public est principalement l’article, la carte et l’archive éditoriale, pas le dossier de fabrication complet ni une chaîne d’enquêtes LLM auditables.

[**Élucid**](https://elucid.media/charte-deontologique-elucid) partage le souci d’indépendance, la critique économique et politique, la pédagogie, les graphiques et la volonté de fournir des outils de compréhension. Le média est financé par ses abonnés et réunit plusieurs contributeurs. Dans les matériaux publics examinés, il n’expose pas un protocole unique reliant, pour chaque article, enquêtes LLM, contre-enquêtes, audits, versions et mémoire.

[**Mediapart**](https://www.mediapart.fr/charte-de-deontologie) place au centre les faits vérifiés et sourcés, leur contextualisation, l’accès aux documents lorsque c’est possible et les corrections publiques explicites. Son contrôle repose cependant sur une rédaction, des journalistes et une organisation éditoriale humaine. La transparence documentaire n’équivaut pas à la publication systématique de toutes les couches de travail.

[**Les Jours**](https://lesjours.fr/obsessions/vie-jours/ep97-choix-redaction/) a inventé une autre forme de mémoire journalistique avec ses « obsessions » : des séries qui relient les épisodes d’un même sujet et lui donnent de la profondeur. Cette continuité se trouve dans le récit publié ; elle ne prend pas la forme d’une mémoire structurée alimentant un protocole d’enquête automatisé.

[**Disclose**](https://disclose.ngo/fr/article/disclose-partage-ses-methodes-et-outils-pour-enqueter) mène des enquêtes d’intérêt public et partage des méthodes et des outils pour permettre à d’autres d’enquêter. Le projet repose sur une équipe et une pratique journalistique collective. Son objet n’est pas de rendre public, pour chaque article, un processus multi-LLM complet.

[**Splann !**](https://splann.org/enqu%C3%AAte/littoral/loi-zan-lezardee/) accompagne certaines enquêtes d’une « boîte noire » qui explique les données, les calculs et les choix méthodologiques. Cette ouverture documente une méthode particulière. Elle n’englobe pas nécessairement les hypothèses abandonnées, les audits adversariaux, les brouillons et la mémoire réutilisable.

Ces comparaisons sont plus utiles qu’une proclamation d’unicité. Elles montrent précisément ce qui existe déjà en France : profondeur historique, critique économique et médiatique, investigation, séries cumulatives, outils partagés, données et méthodes ouvertes.

Elles montrent aussi ce que je n’y ai pas trouvé sous la même forme : une personne seule qui fait produire ses enquêtes par plusieurs LLM, les met en contradiction à travers un métalangage cognitif commun, transforme leurs résultats en article, conserve une partie importante de leurs états intermédiaires et réinjecte cette matière dans la suite du corpus.

---

## §6 : Les équivalents internationaux confirment le caractère hybride

À l’étranger, certains projets se rapprochent encore davantage d’un morceau de la méthode.

[**Bellingcat**](https://www.bellingcat.com/about/editorial-standards-practices/) est un collectif d’enquête en sources ouvertes. Il montre comment authentifier des images, retrouver des lieux et reconstruire des événements à partir de matériaux publics. Sa force est la reproductibilité de certaines démonstrations. Mais il s’agit d’une organisation humaine spécialisée, pas d’un atelier individuel dont l’enquête brute est produite par un ensemble de LLM.

[**The Markup**](https://themarkup.org/about) a publié, pour certaines enquêtes technologiques, l’article, les données, le code et la méthode. Sur la reproductibilité des calculs, ce modèle peut aller plus loin que Résistance Cognitive. Il n’expose toutefois pas nécessairement la généalogie narrative complète : hypothèses, plans rejetés, audits du texte et mémoire réutilisée.

[**Cory Doctorow**](https://pluralistic.net/2021/05/09/the-memex-method/) utilise son blog comme une mémoire externe : les faits et les idées accumulés deviennent la matière de synthèses futures. Résistance Cognitive partage ce principe cumulatif, mais ajoute une couche de dossiers structurés et d’enquêtes générées selon un même protocole.

[**Molly White**](https://influence.citationneeded.news/about/colophon) relie une newsletter indépendante, des bases structurées, une méthode explicite et du code ouvert. C’est probablement le cas individuel le plus proche. Ses différents outils forment cependant plusieurs productions publiques ; ils ne constituent pas, à ma connaissance, le même système récursif reliant enquête LLM, synthèse, plan, audit, texte et mémoire.

Pris séparément, presque tous les gestes de Résistance Cognitive ont donc un précédent. L’enquête ouverte existe. La mémoire cumulative existe. Le code et les méthodes publics existent. Les corrections visibles existent. Le travail indépendant existe.

Ce qui demeure sans équivalent identifié est leur assemblage.

---

## §7 : Où se trouve exactement la singularité ?

Elle ne tient pas à un adjectif comme « long », « critique », « sourcé » ou « indépendant ». Elle ne tient même pas, à elle seule, à l’utilisation de plusieurs modèles de langage.

Elle tient à la réunion des propriétés suivantes :

1. **un système développé pendant plus de deux ans**, et non une suite de consignes improvisées ;

2. **un métalangage cognitif** qui encode les opérations, les états de connaissance et les contrôles ;

3. **des enquêtes produites intégralement par des LLM** à partir de ce protocole ;

4. **plusieurs modèles mis en contradiction**, chacun apportant ses capacités et ses biais ;

5. **un humain qui reste dans toutes les boucles**, non pour rédiger chaque enquête, mais pour choisir, relancer, contester, corriger et assumer la publication ;

6. **une architecture récursive commune à tous les articles**, capable de revenir de l’écriture à l’enquête et de reconstruire ensuite résumés, synthèse, thèse et texte ;

7. **une orchestration adaptée à chaque dossier**, qui sépare la recherche, la condensation, l’architecture de la pensée et la qualité de l’écriture ;

8. **un dossier intermédiaire** qui conserve enquêtes, résumés, audits, plans et brouillons ;

9. **une mémoire cumulative** capable de réinjecter les résultats antérieurs dans une nouvelle enquête ;

10. **une production individuelle, non rémunérée et multi-domaine**, réalisée uniquement à partir de sources ouvertes, là où ces fonctions sont d’ordinaire réparties entre plusieurs métiers ;

11. **une ouverture partielle du processus**, assez importante pour permettre un examen réel, sans prétendre enregistrer chaque micro-modification.

Je n’ai trouvé aucun projet public réunissant exactement ces onze propriétés.

Cette formulation est volontairement plus étroite que « personne ne fait ce que je fais ». Elle ne prétend pas connaître chaque laboratoire privé, chaque rédaction interne ou chaque chercheur indépendant dans le monde. Elle dit quelque chose de vérifiable : parmi les systèmes publics examinés, les parents les plus proches ne combinent pas toute cette architecture.

La meilleure définition de Résistance Cognitive n’est donc ni « blog écrit par IA », ni « média automatisé », ni « laboratoire de recherche ».

C’est un **atelier indépendant de journalisme cognitif forensique, dans lequel plusieurs LLM produisent et contestent les dossiers tandis qu’un humain pilote les boucles, reconstruit la pensée et décide ce qui mérite d’être publié**.

---

## §8 : Ce que cette singularité ne prouve pas

Un dispositif original peut être médiocre. Un protocole sophistiqué peut ritualiser des erreurs au lieu de les supprimer. Une machine qui produit plus vite peut aussi produire plus vite des raisonnements faux.

Il faut donc séparer six affirmations.

### 1. La production automatisée ne garantit pas la vérité

L’enquête APEX montre qu’un LLM peut exécuter seul une forme d’enquête. Ses corrections ultérieures montrent qu’il peut aussi produire une chronologie fragile, une qualification trop forte ou une causalité séduisante mais insuffisamment établie.

La prouesse concerne la capacité de production, pas l’infaillibilité du résultat.

### 2. Plusieurs modèles ne constituent pas une rédaction indépendante

Leurs désaccords sont utiles, mais ils peuvent partager des biais et des erreurs. Je choisis les questions, je décide quels audits poursuivre et je garde le dernier mot. La pluralité des modèles augmente la contradiction interne ; elle ne remplace pas un contradicteur humain extérieur.

### 3. L’OSINT ouvre un champ immense, mais laisse le hors-champ intact

Tout le travail repose sur l’OSINT : des sources accessibles publiquement sur Internet ou dans des bases ouvertes. Textes de loi, décisions, rapports, budgets, registres d’entreprises, marchés publics, archives audiovisuelles, publications sociales, études, jeux de données et déclarations constituent une masse documentaire considérable. Le monde numérique laisse assez de traces pour reconstruire des chronologies, cartographier des acteurs, confronter des discours et faire apparaître des mécanismes que la lecture isolée d’un article ne montre pas.

Mais une trace publique n’est ni complète, ni nécessairement vraie. Je n’ai pas accès aux pièces confidentielles, aux sources internes, aux conversations privées ni aux documents protégés. Je ne mène pas d’entretien, je ne vais pas sur le terrain et je ne confronte pas directement les personnes mises en cause à mes conclusions avant publication. Aucun contradicteur humain ne partage la fabrication du dossier.

Truth Engine peut donc enquêter profondément sur **ce que le numérique rend observable**. Il ne peut pas reconstituer à lui seul tout ce que les acteurs n’ont pas publié, tout ce qui n’a laissé aucune trace ou tout ce qu’une présence sur le terrain aurait permis de comprendre.

### 4. Le formalisme peut créer une fausse précision

Des symboles, des scores et des seuils rendent le protocole opérable. Ils peuvent aussi donner à un jugement qualitatif l’apparence d’une mesure scientifique. Tant que leurs effets ne sont pas évalués sur un corpus indépendant, ils doivent être lus comme des instruments de discipline, pas comme des preuves mathématiques.

### 5. La traçabilité reste incomplète

Le ZIP permet d’observer beaucoup plus que l’article final, mais il ne contient pas chaque conversation, chaque ordre ponctuel ni chaque retouche. Une archive partielle peut révéler les grandes transformations ; elle ne permet pas de certifier l’origine de chaque phrase.

### 6. La qualité dépend du travail humain

Tous les articles suivent la même architecture, mais tous ne reçoivent pas la même quantité d’attention. Le dossier Fedorova montre ce que le système peut produire lorsqu’il est beaucoup sollicité. Il ne prouve pas que chaque texte du corpus atteint ce niveau.

Pour démontrer que Truth Engine améliore réellement la fiabilité, il faudrait maintenant un autre travail : échantillonner plusieurs articles, refaire leurs vérifications, mesurer les erreurs, comparer différentes profondeurs d’enquête et confronter les résultats à d’autres méthodes.

**Être unique ne signifie pas encore avoir raison.**

---

## §9 : Ce que cet atelier peut construire pour d’autres

Résistance Cognitive est une publication, mais aussi un démonstrateur. Le territoire que j’y cartographie est aujourd’hui l’enquête OSINT ; l’atelier qui fabrique les cartes peut être transposé à d’autres **métiers du dossier** : ces activités où il faut réunir des documents, interroger un corpus, appliquer des règles, repérer des contradictions et produire une analyse contrôlable.

Ce que je peux apporter ne se réduit pas à la rédaction de prompts. Je peux intervenir depuis la cartographie d’un besoin jusqu’au prototype fonctionnel : formaliser les opérations intellectuelles d’un métier, préparer et indexer ses corpus, concevoir une architecture RAG, répartir les tâches entre agents, orchestrer plusieurs LLM, construire la mémoire, les évaluations et les seuils de contrôle, puis développer les outils qui rendent l’ensemble utilisable.

Une telle architecture peut servir à des rédactions, des chercheurs, des associations, des cabinets ou des équipes chargées d’audit, de conformité, de veille et de *due diligence*. Plus largement, elle peut aider toute organisation confrontée à des dossiers volumineux, évolutifs ou contradictoires.

L’avantage n’est pas de faire produire davantage de texte par un modèle de langage. Il est de traiter un corpus plus vaste sans perdre la provenance des informations, de séparer la recherche, le raisonnement et l’écriture, de confronter plusieurs modèles plutôt que d’en subir un seul, et de pouvoir rouvrir le dossier lorsqu’un fait nouveau déplace la carte. Le système peut accélérer la collecte et la préanalyse, élargir la couverture documentaire et rendre les désaccords plus visibles avant la décision humaine.

Les limites font partie de l’offre. Ce type d’atelier n’est ni universel ni immédiatement transposable : il faut l’adapter au métier, à ses données, à ses risques et à ses critères de qualité. Un corpus privé exige une gouvernance adaptée. Plusieurs LLM peuvent partager la même erreur. Une expertise de domaine reste nécessaire pour les usages sensibles, tout comme une validation humaine capable d’arrêter le système ou de reprendre l’enquête.

Je ne propose donc pas un modèle infaillible ni le remplacement automatique d’une responsabilité professionnelle. Je peux concevoir et développer un atelier cognitif sur mesure, destiné à absorber une partie lourde du travail documentaire tout en laissant à l’humain le contrôle, l’arbitrage et la responsabilité.

**Si vous avez un corpus difficile à exploiter, un processus intellectuel répétitif ou un métier du dossier à repenser, c’est le type de problème que je peux étudier et prototyper.**

---

## §10 : Verdict

Résistance Cognitive n’a inventé aucun des principes fondamentaux dont il se sert : enquêter, sourcer, confronter des hypothèses, conserver une mémoire, auditer un texte, publier une méthode ou utiliser un logiciel pour augmenter le travail d’un auteur.

Il a en revanche construit une combinaison que je n’ai pas retrouvée ailleurs sous une forme publique : un métalangage cognitif développé pendant plus de deux ans, exécuté par plusieurs LLM qui se contrôlent imparfaitement les uns les autres, capable de produire une enquête entière sans rédaction humaine, puis piloté dans des boucles successives par un humain dont le temps et le doute déterminent largement la qualité finale.

Cette production est indépendante, non rémunérée et entièrement fondée sur des sources ouvertes. Ces trois propriétés rendent le travail possible sans tutelle ; elles en fixent aussi les frontières. Je peux exploiter une masse documentaire inaccessible à un lecteur isolé. Je ne peux pas remplacer une source humaine, une interview, un droit de réponse ni une observation de terrain par davantage de calcul ou de texte.

La question « est-ce révolutionnaire ? » contient en réalité deux questions.

Qu’un LLM puisse produire seul un dossier comme l’enquête APEX, à partir d’un signal initial et d’un protocole formel, constitue à mes yeux une rupture dans la manière dont une enquête peut être fabriquée.

Que le métalangage de Truth Engine rende cette enquête plus juste, plus robuste ou plus utile qu’une méthode plus simple reste, en revanche, une hypothèse.

Je ne veux pas résoudre cette contradiction avec un slogan.

[Le ZIP publié avec cet article](https://drive.proton.me/urls/MR7M17238R#GYDY1Hm67NRH) permettra de lire le README, d’ouvrir les enquêtes, de comparer leurs quintessences, d’observer le plan rejeté, de suivre les audits et de revenir aux versions de l’article. Il ne montrera pas tout. Il montrera assez pour que le débat porte enfin sur les pièces plutôt que sur la promesse.

Après plus de deux ans, je ne sais toujours pas si j’ai construit une révolution ou une perte de temps extraordinairement élaborée.

Je sais seulement que ce système produit des cartes, qu’il se trompe, que ses déformations deviennent plus visibles lorsque je confronte les projections et les calques, et que chacun pourra désormais examiner les relevés qui les ont produites.

**Je cartographie. Vous décidez.**

---

### Documents et repères utilisés

**Truth Engine et Résistance Cognitive**

- [Dossier de fabrication Fedorova (ZIP)](https://drive.proton.me/urls/MR7M17238R#GYDY1Hm67NRH) : le protocole complet, les 35 enquêtes APEX, leurs quintessences, les audits et les versions de l’article
- [À propos de Résistance Cognitive](https://giak.substack.com/about)
- [CDJM : Déclaration de Munich sur les devoirs et les droits des journalistes](https://cdjm.org/les-chartes/)

**Comparaisons**

- [Le Monde diplomatique : À propos](https://www.monde-diplomatique.fr/diplo/apropos/)
- [Élucid : Charte déontologique](https://elucid.media/charte-deontologique-elucid)
- [Mediapart : Charte de déontologie](https://www.mediapart.fr/charte-de-deontologie)
- [Les Jours : Le choix éditorial des « obsessions »](https://lesjours.fr/obsessions/vie-jours/ep97-choix-redaction/)
- [Disclose : Méthodes et outils d’enquête](https://disclose.ngo/fr/article/disclose-partage-ses-methodes-et-outils-pour-enqueter)
- [Splann !, exemple de « boîte noire » méthodologique](https://splann.org/enqu%C3%AAte/littoral/loi-zan-lezardee/)
- [Bellingcat : Règles éditoriales, vérification et corrections](https://www.bellingcat.com/about/editorial-standards-practices/)
- [The Markup : À propos](https://themarkup.org/about)
- [Cory Doctorow : « The Memex Method »](https://pluralistic.net/2021/05/09/the-memex-method/)
- [Molly White : Méthode, limites et code de Tech Influence Watch](https://influence.citationneeded.news/about/colophon)

Comparaison arrêtée au **3 août 2026**. Elle porte sur les méthodes et productions rendues publiques par les projets cités. Elle ne mesure ni leur qualité générale, ni leur audience, ni leur impact.
