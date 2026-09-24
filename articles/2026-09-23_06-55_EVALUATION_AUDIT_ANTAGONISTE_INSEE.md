# Évaluation de l'audit antagoniste externe — dossier Insee V5

Cible auditée : `articles/2026-09-23_06-00_insee-v5-v38_ce-que-linsee-ne-vous-dira-jamais_ARTICLE.md`
Audit reçu : 20 constats, 4 sources, un tableau de destruction finale.
Date de l'évaluation : 23 septembre 2026.

## 0. Méthode

Trois opérations, dans cet ordre.

**Vérification des citations.** Les 20 passages cités par l'audit ont été recherchés dans le fichier réel, après normalisation des accents, de la casse et des apostrophes. Résultat : **20 sur 20 existent**. L'audit a lu le texte, il ne l'a pas halluciné. C'est rare et cela justifie de le traiter sérieusement. Deux écarts mineurs de citation : l'article écrit « 10 à 18 % » sans les signes +, et le mot « significativité » n'apparaît nulle part (l'audit attribue au texte un vocabulaire que le texte n'emploie pas).

**Vérification de la provenance de l'audit.** Ses liens portent `utm_source=chatgpt.com` : ils viennent d'une session de navigation d'un autre modèle. Les quatre URL ont été ouvertes. Elles résolvent toutes et pointent les bons documents Insee (IR n° 192, table des seuils de pauvreté, Insee Méthodes n° 145 sur la rénovation ERFS, Focus n° 152). Trois d'entre elles ont d'ailleurs **fermé trois de nos notes sans provenance** (voir §7).

**Vérification des constats contre nos propres pièces.** Chaque grief a été confronté non pas à mon intention d'auteur mais au texte et aux sources du dossier, y compris quand la pièce contredit le grief.

## 1. Verdict par constat

| # | Constat de l'audit | Verdict | Action |
|---|---|---|---|
| 1 | « ne signifie rien » transforme la précision en test de significativité | **Partiellement fondé** | Formulé « n'y démontre rien » |
| 2 | ±17 500 déclaré inexploitable et utilisé comme marge | **Non fondé** | Refus rendu explicite dès le corps |
| 3 | « structurellement bas » dépasse la preuve | **Fondé** | Remplacé par « provisoire » |
| 4 | « n'a pas de programme » infère l'intention | **Fondé sur le fond** | Phrase reformulée sans inférence d'intention |
| 5 | « le mot chômage désigne un choix » trop provocateur | **Non fondé** | Vocabulaire harmonisé en « convention » |
| 6 | « presque toujours une phrase sur un seuil » non démontré | **Fondé** | Transformé en propriété du dispositif |
| 7 | « sans qu'aucun changement soit intervenu » trop absolu | **Fondé** | « du seul fait du changement de méthode » |
| 8 | IPC « exclut le logement des propriétaires » incorrect | **Fondé, et le plus utile** | Reformulé en loyers imputés et prix d'achat |
| 9 | ordre de grandeur transformé en compteur automatique | **Partiellement fondé** | « sur ces seules dépenses indexées, de l'ordre de » |
| 10 | « habitants manquants » contient une interprétation | **Fondé** | « écart de 113 habitants » |
| 11 | « Personne ne peut dire » absolu épistémique | **Fondé** | « notre corpus ne permet pas de le dire » |
| 12 | « presque rien n'est dit » surinterprétation | **Partiellement fondé** | Épigraphe conservée, définition corrigée au §8 |
| 13 | « l'Insee publie, il ne dit pas » contredit par l'article | **Partiellement fondé** | Même traitement que 12 |
| 14 | H1 « morte » alors qu'elle n'est pas réfutée | **Fondé** | « ne survit pas à l'épreuve, faute de pièce » |
| 15 | H2 tuée trop vite | **Non fondé** | Aucune : la version faible était déjà conservée |
| 16 | H5 « close sur le plan comptable » contredit | **Fondé** | « close sur pièces » |
| 17 | « un institut qui dissimule ne publie pas... » | **Fondé** | Inférence bornée au grief visé |
| 18 | le titre promet la dissimulation, la démonstration parle de transmission | **Partiellement fondé** | Aucune : le titre est déjà retourné |
| 19 | le calcul « 10 à 18 % » du café-croissant doit disparaître | **Fondé, et plus grave qu'il ne le dit** | Ouverture restructurée (§3) |
| 20 | « le meilleur passage est celui qui accuse le moins » | **Jugement éditorial** | Retenu comme signal, pas comme instruction |

Décompte : **10 fondés, 6 partiellement fondés, 3 non fondés, 1 jugement**. L'audit annonce « au moins 8 FAIL dont 5 sérieux » : le chiffre est surévalué d'environ un tiers, mais la nature des défauts qu'il pointe est réelle.

## 2. Ce que l'audit a vu, et que je n'avais pas vu

**Le constat le plus utile est le numéro 8.** Le texte écrivait que l'indice des prix « exclut le logement des propriétaires ». C'est faux au sens strict, et **notre propre appareil critique le disait déjà** : la note [25] relève un poids du logement de 14,0 % dans l'indice, dont 6,1 % de loyers effectivement payés. Ce que l'indice n'intègre pas, ce sont les loyers imputés des propriétaires occupants et les prix d'achat des logements. Un lecteur hostile pouvait donc retourner le geste le plus normatif de l'article contre l'article. Corrigé, avec la référence au Focus 152 dans la phrase elle-même.

**Le numéro 19 est fondé, et sa portée dépasse ce qu'il en dit.** Voir la section suivante : le problème n'est pas la vulgarité du calcul, c'est qu'il reposait sur une source contestée.

**Les numéros 10, 11, 14, 16, 17 sont des calibrages réels** : quatre formulations portaient plus que ce que nos pièces établissent, dans un dossier dont la règle affichée est justement de ne pas le faire. Les jours où un critique hostile trouve ces glissements avant nous, la leçon est de méthode, pas de vanité.

## 3. Ce que l'audit a raté, et qui est plus grave que ce qu'il dénonce

**Un facteur 10 dans un titre de section.** Le titre de la section sur l'indexation annonçait : « Un dixième de point vaut 5 milliards ». Le corps de la même section, la figure 04 construite sur le même contenu et la source citée disent tous trois **cinq cents millions pour un dixième de point** (5 Md€ par point, sur 500 Md€ de prestations indexées). L'erreur est présente depuis la V3 et a traversé mes propres audits, l'un vérifiant « 5 Md€/pt » comme invariant sans regarder le titre. C'est exactement le type de défaut que l'article reproche à la chaîne de diffusion : un chiffre juste dans le document, faux dans le titre, et personne pour rapprocher les deux. Corrigé.

**Le prix du café 2024-2026 est une source en conflit interne.** L'ouverture s'appuyait sur 1,40 euro au comptoir (RTL citant le Syndicat français du café, 2024). Un reportage TF1 du 17 février 2025, repris par Capital le même jour, donne **près de 2 euros en province et plus de 2,50 à Paris**. Entre 1,40 et 2,00, l'écart est de 40 %, il est supérieur au résultat recherché, et il change le signe de la conclusion : à 1,40 le café a monté moins que l'indice général (1,55 euro attendu pour un prix de 0,98 en 1999), à 2,00 il l'a dépassé d'un quart. Le « 10 à 18 % » de la version précédente tenait donc sur un croissant 1999 non mesuré **et** sur la source basse du café. L'audit effleurait ce point en demandant de supprimer le chiffre ; il n'a pas vu qu'il y avait un conflit de sources sous le chiffre.

**Une série sœur ignorée.** Le pivot de l'ouverture repose sur « la série du café au comptoir s'arrête en 1999 ». C'est exact. Mais l'institut a mesuré la **tasse de café en salle** au-delà de 1999, avec une série elle aussi arrêtée : la page consultée porte la mention « Série arrêtée », et le millésime de fin (2015) vient de l'indexation du site, non d'une lecture directe de son tableau, que nos outils n'extraient pas. L'article ne cite donc que la mention, sans le millésime. Un lecteur qui la trouve peut accuser le texte d'avoir choisi la série qui l'arrange. Le paragraphe le dit désormais.

**Trois figures à défaut de rendu.** En regardant les figures après régénération (pas en lisant leur XML), une collision est apparue dans la FIG. 07 : les blocs de texte des deux panneaux débordaient sur leur note de pied, et le pied de page gauche recouvrait le pied droit. La cause est dans le moteur : après compression proportionnelle et plancher, la hauteur du bloc n'était pas revérifiée. Corrigé à la racine (compression itérative des gouttières puis des corps, hauteur augmentée, pied de page auto-ajusté). Deux de ces trois défauts préexistaient à mes corrections, ce qui signifie qu'ils étaient présents lors de la livraison d'hier.

## 4. Ce que l'audit a faux

**Sa critique numéro un se réfute avec sa propre citation.** L'audit affirme que nous transformons la marge publiée en test de significativité. Or la légende du producteur, qu'il cite lui-même, porte : « Estimation à +/- 0,3 point près du niveau du taux de chômage **et de son évolution d'un trimestre à l'autre** ». La marge est attachée par le producteur à l'évolution trimestrielle : constater qu'une marche de 0,2 point tient dedans n'est pas une extrapolation, c'est la lecture de la légende. Le grief pertinent n'était que le mot « rien » ; il est corrigé. Et l'article **s'appliquait déjà cette règle à lui-même** deux sections plus loin (« Est établi : le niveau et son ordre de grandeur. N'est pas établi : la marche d'un trimestre »), ce que l'audit n'a pas relevé, alors qu'il relève précisément le manque d'auto-application.

**Le numéro 2 n'a pas de contradiction à établir.** L'audit soutient qu'on ne peut pas à la fois publier un ±17 500 et refuser de savoir à quel ensemble il se rapporte. Mais le texte ne s'en sert pas comme d'une marge : il rapporte ce que la fiche publie, puis refuse de l'exploiter faute de dénominateur, et la note [41] consigne même l'anomalie arithmétique (un coefficient de variation de 0,01 % impliquerait un ensemble de 175 millions de personnes). Rapporter une publication n'est pas l'utiliser. J'ai tout de même rendu le refus explicite dès le corps, ce qui supprime l'ambiguïté sans changer le fond.

**Le numéro 5 est déjà traité par son propre contexte.** Le paragraphe enchaîne : « il désigne un choix. Non que le choix soit mauvais. Le BIT est le standard international, le plus difficile à manipuler politiquement ». L'audit propose comme correction ce que la phrase suivante dit déjà.

**Le numéro 15 l'est aussi.** L'audit reproche à H2 d'être « morte trop vite » et propose de la traiter comme non soutenue en version forte. Le texte écrit exactement cela : « L'hypothèse est morte de la contradiction des signes... Elle survit en version faible ».

**Le numéro 18 ne tient qu'en lisant le titre seul.** Le titre complet est « Ce que l'INSEE ne vous dira jamais (et publie pourtant) », et le paragraphe 8 explique la distinction qui l'explique. Si l'audit avait raison sur la promesse, il aurait raison contre un titre amputé.

## 5. Le changement éditorial substantiel

L'ouverture a été restructurée, et ce n'est pas une correction de vocabulaire.

**Avant** : dix francs, un café, un croissant, la conversion fausse, puis un chiffre, « le panier a monté de 10 à 18 % de plus que l'indice », et la conclusion « la perception est fondée ».

**Après** : dix francs, un café, un croissant, la conversion fausse (6,55957), le prix officiel de 1999 (0,98 euro, série Insee), puis **le conflit de sources** sur le prix actuel, l'écart affiché entre elles, et cette phrase : « un écart de panier se calcule dans les deux sens ; nous ne le retenons pas comme résultat, et cette retenue vaut pour tout l'article ».

Le raisonnement est celui-ci : nous ne pouvons pas demander au lecteur de refuser les chiffres sans condition tout en lui servant, dès la deuxième section, un pourcentage construit sur un prix non mesuré et une source unique contestée. Le paragraphe sur les causes documentées de la perception est conservé, parce qu'il repose sur l'Insee elle-même (arrondi de 2002 à +1,5 % sur les cafés, Focus n° 87, « nettement accru la divergence »). La note [5] devient la note de sensibilité : elle donne le calcul dans les deux hypothèses (+10 % avec le relevé bas, plus de 30 % avec le relevé haut) et dit pourquoi nous ne le publions pas. Le lecteur qui veut refaire le calcul a tout ; celui qui veut un chiffre n'en reçoit pas de faux.

Coût assumé : l'ouverture perd de la frappe. Gain : elle démontre, dès sa deuxième section, la règle que l'article vend à la fin.

## 6. Ce qui reste ouvert, et qui n'est pas à moi de trancher

**L'épigraphe « l'Insee publie, il ne dit pas ».** L'audit demande de la remplacer par « l'Insee publie les conditions du chiffre, mais elles ne suivent pas le chiffre jusqu'à son lecteur ». J'ai corrigé le point précis où le texte dépassait (« jamais mis en avant » était faux : l'institut publie des Focus dédiés) sans abandonner la formule. Raison : la formule est définie en clair au paragraphe 8 et adossée à une mesure (zéro mention de la marge sur dix-neuf articles), alors que la reformulation proposée dilue l'argument dans une phrase que n'importe quel rapport officiel pourrait signer. Décision réversible, à ton arbitrage.

**L'absolu négatif conservé** : « Aucun audit forensique de type argentin n'a jamais été mené sur l'Insee ». C'est la même famille de défaut que le numéro 11 (une absence de recherche présentée comme une absence dans le monde). Il avait déjà été signalé hier et laissé ouvert. Il l'est toujours.

**Le statut de H1.** Corrigé en « non étayée », mais la formulation garde « ne survit pas », qui reste une image. Si l'on veut la rigueur complète du protocole, il faut écrire NON_ÉTAYÉE en toutes lettres et perdre la chute du chapitre.

**La longueur.** 9 477 mots, 44 notes, 11 figures. L'audit ne le dit pas, mais un texte de cette taille est un objet éditorial à part : la variante courte reste à décider.

## 7. Ce que l'audit apporte au-delà de ses constats

Sa quatrième source a produit la trouvaille la plus inattendue de la journée, que **l'audit lui-même n'a pas vue** en la citant. La publication du 8,3 % porte, en tête, un avertissement de champ : « à partir de cette publication, le champ des principaux indicateurs conjoncturels du marché du travail porte sur le champ France, étendant ainsi le champ précédent France hors Mayotte », séries rétropolées, Mayotte rehaussant le taux de 0,06 point et abaissant le taux d'emploi des 15-64 ans de 0,17 point. Autrement dit : la série phare du chômage a changé de périmètre le jour même où le pays comparait ses trimestres, et le dossier, qui consacre un de ses quatre gestes au périmètre, ne l'avait pas relevé sur son propre chiffre d'ouverture. Le paragraphe ajouté le dit, en précisant ce que notre corpus ne permet pas d'affirmer (nous y cherchions la marge, non le champ, donc nous ne soutenons pas que la presse l'a passée sous silence). C'est exactement la scène que le grief 8 reprochait à la phrase sur l'IPC : un universel de méthode non appliqué à notre propre mesure.

Et trois de ses quatre sources ont fermé trois de nos notes les plus faibles : les notes [8], [16] et [17] portent désormais une URL vérifiée en direct, là où la note [8] s'appuyait sur un simple renvoi de registre et les notes [16] et [17] sur des références internes sans adresse. La table Insee des seuils de pauvreté (parution du 9 juillet 2026) donne les quatre niveaux et **porte elle-même la mention de rupture de série** : « à partir de 2020, cette série est calculée avec une chaîne de production de l'ERFS rénovée ». Le document Insee Méthodes n° 145 (novembre 2023) donne le mécanisme de la rénovation et son effet sur les indicateurs. Les notes [16] et [17] ont désormais une URL vérifiée en direct, et la section pauvreté cite le producteur datant sa propre rupture plutôt que notre commentaire. Pour le 0,3 point, la note précise honnêtement qu'il vient de nos registres, non du texte extractible de la page : nous ne transformons pas une vérification partielle en verbatim.

Leçon de méthode, la même que celle des corrections de la nuit : **un audit se vérifie comme une source**. Ici, 20 citations vraies, 4 URL vraies, 3 constats non fondés et 2 pièces récupérées pour notre propre appareil critique. Le bon usage d'un audit antagoniste n'est pas de lui obéir ni de le récuser, c'est de le traiter comme un témoin : ce qu'il apporte de vérifiable entre dans le dossier, ce qu'il affirme sans pièce reste dehors.
