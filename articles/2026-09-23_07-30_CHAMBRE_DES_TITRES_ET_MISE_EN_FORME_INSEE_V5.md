# Chambre des titres et passe de mise en forme — dossier Insee V5

Cible : `articles/2026-09-23_06-00_insee-v5-v38_ce-que-linsee-ne-vous-dira-jamais_ARTICLE.md`
Référence normative : `tools/engines/sublimator/prompt-v38_phase3.md` (§5.3 chambre des titres, LOI 1, 2, 3, 9, charte permanente).
Forme de référence observée : `substack-online/posts/202607767.le-systeme-informatique-detat-autopsie.html` (liens wiki en ligne dans la prose, section « Sources » en fin d'article, aucune note numérotée).

## 1. Titre appliqué

**Titre** : 🔢 Ce que l'INSEE publie, ce que vous lisez
**Sous-titre** : Nous avons testé 6 hypothèses de manipulation et retenu 4 gestes pour lire un chiffre officiel sans se laisser tromper

Pourquoi celui-là. L'ancien titre, « Ce que l'INSEE ne vous dira jamais (et publie pourtant) », promettait une dissimulation que la démonstration refuse : l'article établit que l'institut publie, et que le circuit ne transmet pas. Le nouveau titre nomme exactement la thèse (l'écart entre les deux lectures d'un même chiffre), il tient en 8 mots, et il ne contient aucun absolu à défendre. Le sous-titre passe de 24 à 20 mots, devient une phrase complète avec verbe, et annonce les deux apports du dossier : l'épreuve des 6 hypothèses et les 4 gestes.

## 2. Les 9 propositions (3 chocs, 3 forensiques, 3 conceptuels)

| # | Catégorie | Titre (mots) | Sous-titre (mots) |
|---|---|---|---|
| 1 | Choc | L'INSEE publie tout, et presque rien ne vous parvient (10) | Six hypothèses de manipulation testées, quatre gestes retenus, et la marge que tout chiffre officiel perd en chemin. (18) |
| 2 | Choc | Nous avons attaqué l'INSEE, voici ce qui a tenu (9) | Quatre jours d'enquête adversariale sur la première source statistique du pays, ses six accusations et ses quatre gestes. (18) |
| 3 | Choc | La marge est dans le document, jamais dans le titre (9) | Ce que la légende d'une publication officielle dit vraiment du chômage, et pourquoi aucun journal ne la reprend. (19) |
| 4 | Forensique | Biographie d'un chiffre officiel, de la mesure à la une (10) | Définition, marge, seuil, périmètre, révision : cinq pièces du 8,3 % que le lecteur de presse ne voit jamais. (17) |
| 5 | Forensique | **Ce que l'INSEE publie, ce que vous lisez (8)** — retenu | **Nous avons testé 6 hypothèses de manipulation et retenu 4 gestes pour lire un chiffre officiel sans se laisser tromper (20)** — retenu |
| 6 | Forensique | Anatomie d'une chaîne de transmission statistique (6) | Du questionnaire de l'enquête Emploi au titre du matin : ce que chaque étage retire au chiffre qui le traverse. (20) |
| 7 | Conceptuel | Publier n'est pas dire (4) | Une statistique publique peut être fiable et perdre, en chemin, les conditions qui la rendent lisible. (16) |
| 8 | Conceptuel | L'institut n'est pas le problème, le circuit l'est (9) | La réponse à la question de confiance ne se joue pas dans la fabrication du chiffre mais dans sa transmission. (19) |
| 9 | Conceptuel | Le chiffre naît avec sa marge (6) | Ce que cinq pièces démontrent sur les statistiques publiques, et ce que quatre gestes permettent d'y vérifier. (18) |

Contraintes vérifiées sur les 9 : titre entre 4 et 12 mots, sous-titre entre 10 et 20 mots, aucun « Comment » ni « Pourquoi », aucun point d'exclamation, aucun emoji dans les propositions (l'emoji 🔢 du titre retenu est l'ajout de publication prévu par le prompt).

Deux candidates restent fortes si tu veux une ligne plus dure : la 3 (« La marge est dans le document, jamais dans le titre ») et la 9 (« Le chiffre naît avec sa marge »). La 2 est la plus « récit d'enquête ». Le choix reste réversible et se fait en un remplacement.

## 3. Passe de mise en forme : ce qui a changé

**Nombres en chiffres.** Règle appliquée : tout nombre qui mesure ou compte quelque chose passe en chiffres (sommes, durées, pourcentages, effectifs, comptes d'objets analysés : articles, communes, hypothèses, gestes, chiffres, vannes, clés, niveaux, figures). Quatre exceptions, explicitement conservées en lettres : les fractions (« un dixième », « un tiers », « la moitié »), les ordinaux (« premier », « quatrième »), les paires démonstratives (« les deux régimes d'erreur », « les deux sens », « les deux périmètres », « les deux pistes », « entre les deux »), et l'intérieur des citations verbatim. Le passage a demandé 77 remplacements dans le texte et 20 dans le générateur de figures, dans le texte **et** dans les figures (une correction appliquée d'un côté seulement créerait précisément la désynchronisation que le dossier traque).

Exemples : « dix francs » → « 10 francs », « Vingt-sept ans plus tard » → « 27 ans plus tard », « dix-neuf articles » → « 19 articles », « Neuf communes » → « 9 communes », « Quatre jours durant » → « 4 jours durant », « une commune sur cinq » → « 1 commune sur 5 », « vingt articles lisibles sur vingt-neuf candidats » → « 20 articles lisibles sur 29 candidats », « de trois à deux ans » → « de 3 à 2 ans », « cinq cents millions » → « 500 millions ».

**Liens wiki vers le corpus (LOI 9).** Cinq liens en ligne dans la prose, aucun section à plus de 1 lien, sauf la section Sources. Répartition : §8 (autorité du vrai), chapitre d'attaque (fact-checkers), H5 (ingérence sans mesure), geste « seuil et périmètre » (argent qui disparaît), appendice méthode (la machine qui documente les machines). Toutes les URL ont été copiées verbatim depuis `substack-online/index.md`, aucune n'est devinée.

**Section Sources (LOI 2).** Elle n'existait pas. Ajoutée en fin d'article, groupée en trois blocs (Insee, producteurs et contrôleurs publics, presse et analyses), **44 URL distinctes** au total. Deux règles d'honnêteté y sont visibles : les liens pointent des documents précis, pas des racines de site, et les sources dont l'adresse n'a pas été conservée dans les registres sont nommées comme telles (Sénat, cadre juridique, RTL, Rexecode, ONS et Destatis) au lieu de recevoir une URL plausible. L'ensemble du registre renvoie à la méthode publiée, en lien wiki.

**Ce qui a été vérifié dans la charte.** Zéro tiret cadratin. Aucun tableau Markdown (interdit pour Substack). Les acronymes et organismes sont définis à leur première apparition (BIT, IRL, IPC, ERFS, ECRT, OFGL, DGCL, CNERP, CNIS, ASP). Aucun jargon d'auditeur dans la prose (les codes de run restent dans les notes, jamais dans le corps).

**Une déviation assumée et documentée.** LOI 1 interdit les renvois `[n]` dans la prose et les posts publiés ne portent aucune note numérotée. Le dossier conserve ses 44 notes numérotées, parce qu'elles constituent son appareil de traçabilité (chaque note porte la référence de run, la citation verbatim et la date de consultation) et qu'aucun format publié ne permet aujourd'hui de reproduire cette densité autrement. Si tu veux la forme publiée stricte, il faut déplacer la trace dans les phrases (« selon l'Insee », « d'après le Trésor ») et fusionner les notes en une liste sans numéros : c'est une réécriture de l'appareil critique, pas une passe de forme, et je ne l'engage pas sans ton accord.

## 4. Contrôles après passe

- Figures : 11/11 conformes (chiffres alignés sur l'article, formules interdites absentes, grammaire respectée, intégration complète).
- Notes : 44 définies, 44 appelées, séquence complète, aucune orpheline.
- Tirets cadratins : 0. Tableaux Markdown : 0. Liens Substack : 6 (5 dans la prose, 1 dans les sources).
- Volume : 10 650 mots avec notes, 11 figures, 44 URL distinctes.

## 5. Ce qui reste à arbitrer

Le format des notes (§3, déviation LOI 1), le choix du titre parmi les 9 propositions, et le fait que la section Sources cite le registre complet par renvoi à un article publié : si tu préfères un appendice technique détaillé plutôt qu'un renvoi, il faut décider où s'arrête la publication du dossier.
