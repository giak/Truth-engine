# AUDIT MULTI-RÔLES — `articles/2026-09-23_06-00_insee-v5-v38_ce-que-linsee-ne-vous-dira-jamais_ARTICLE.md`

Date : 23 septembre 2026, 06 h 05 (Europe/Paris).
Cible : version V5 de la séquelle Insee (11 sections, 44 notes, ~8 600 mots avec appareil).
Méthode : seize rôles d'audit exécutés en passes successives **sur le texte réel relu sur disque**, jamais sur la mémoire du texte. Chaque finding porte un ancrage (citation du fichier, citation de source, ou relevé de registre). Quatre vérifications externes ont été conduites en direct pendant l'audit (§5). Les corrections non ambiguës ont été appliquées au fichier ; les choix éditoriaux restent ouverts (§4).

**Avertissement de méthode.** Cet environnement n'expose pas d'outil de sous-agents : les rôles n'ont pas été « spawnés » comme des penseurs séparés mais exécutés comme des passes d'audit distinctes, chacune avec sa grille et son angle, dans l'ordre le moins complaisant possible (les rôles hostiles d'abord). Cela ne change pas la nature des findings, mais il vaut mieux le dire que le laisser croire.

---

## 1. Roster des rôles (16), avec ce que chacun a rapporté

| # | Rôle | Angle | Verdict | Findings |
|---|---|---|---|---|
| 1 | Contradicteur épistémologique | Les catégories tiennent-elles ? | Catégories solides, une attribution fautive | F-09, F-10 |
| 2 | Rédacteur en chef | Promesses tenues, structure, force des conclusions | Promesse chiffrée fausse, titre à fonder | F-05, F-16, F-19 |
| 3 | Fact-checker forensique | Vérification ligne à ligne, verbatims, arithmétique | 4 erreurs réelles, dont 2 dans l'ouverture | F-01, F-02, F-06, F-07, F-21, F-23 |
| 4 | Juriste / conformité | Cadre légal, lois citées, risque réputationnel | Une loi mal datée, un absolu à requalifier | F-13, F-24 |
| 5 | Auditeur méthodologique | Le protocole de falsification tient-il ? | Une durée inventée, un prior non chiffré | F-03, F-11 |
| 6 | Philosophe du langage / calibration | Les distinctions sont-elles calibrées ? | Deux universels non tenus, un tic de ton réparé | F-04, F-15 |
| 7 | Expert en désinformation | Instrumentalisable ? Garde-fous suffisants ? | Risque réel sur deux ancrages | F-08, F-25 |
| 8 | Avocat du diable systémique | Plaide l'inverse : l'article est trop sévère | Argument fort sur le titre et sur le bruit | renforce F-08, F-16 |
| 9 | Pair reviewer statisticien (INSD) | Exactitude technique | Une méthode recensement imprécise, un CV ininterprétable | F-06, F-12 |
| 10 | Lecteur non-spécialiste (« test du métro ») | Compréhension, charge cognitive | Boucle du lecteur non refermée | F-17 |
| 11 | Archiviste de provenance | Hiérarchie des sources, URL, tiers | 3 notes sans provenance, un tiers surestimé | F-06, F-07, F-23 |
| 12 | Avocat de la médiation (défense de la presse) | La critique des médias est-elle juste ? | Échantillon de commodité utilisé comme un « aucun » | F-14 |
| 13 | Sociologue de la confiance | À qui profite la défiance ? | Dimension absente | F-18 |
| 14 | Auditeur KISS / exécution | Chaque affirmation traçable, longueur utile | Traçabilité plus volumineuse que la démonstration | F-19, F-22 |
| 15 | Enseignant en statistique publique | Le kit est-il pédagogiquement juste ? | Le kit contredit la cohérence interne en son état initial ; un geste manque | F-08, F-20 |
| 16 | Contradicteur de cohérence interne | Chasse aux auto-contradictions | 5 auto-contradictions compilées | F-01, F-02, F-04, F-08, F-10 |

**Ajouts au roster proposé** (au-delà des huit fournis) : pair reviewer d'institut statistique (rôle 9), avocat de la médiation (12), sociologue de la confiance (13), auditeur KISS (14), enseignant de statistique publique (15), archiviste de provenance (11). Les rôles 11, 12 et 14 sont ceux qui ont produit les findings les plus inconfortables après le fact-checker.

---

## 2. Findings consolidés

### Sévérité CRITIQUE — erreurs factuelles ou arithmétiques dans notre propre texte

- **F-01. L'ouverture se contredisait elle-même.** « ces dix francs valent officiellement 1,52 euro, et cette somme ne suffit plus à payer le café seul » était réfuté par la note [3] du même fichier : café au comptoir 1,40 euro. 1,52 euro paie le café et laisse douze centimes ; c'est le croissant qui est hors d'atteinte. Une erreur de tête d'article sur un article qui dénonce les têtes d'article. **Corrigé.**
- **F-02. Arithmétique interne fausse.** « Le panier du matin tenait donc dans dix francs, avec la monnaie promise » : 0,98 euro (6,43 F) + environ 4 F = environ 10,40 F, soit au-dessus de dix francs, et la note [5] du même article donnait « environ 1,6 euro » (10,5 F). La phrase contredisait sa propre note. **Corrigé**, et le dépassement est devenu un argument : la mémoire collective est non seulement sélective, elle est floue dans ses propres termes.
- **F-04. L'universel de thèse était faux.** « Tout est publié ; presque rien n'est dit » est réfuté par le corps du texte lui-même (rapports de qualité « pas toujours publiés », page 610 Md€ illisible, dénominateur du ±17 500 absent). **Corrigé** en « Presque tout est publié ».
- **F-05. Promesse chiffrée fausse.** Le sous-titre annonçait « Six malentendus » ; le corps en déroule sept. Un décompte faux dans le titre d'un article dont la règle interne est le chiffre vérifié. **Corrigé.**
- **F-03. Durée inventée.** « Pendant trois semaines, nous avons attaqué l'institution » et « Trois semaines de recherche adversariale ». Les registres Insee du dépôt s'étendent du 20 au 23 septembre 2026 (vingt-deux sujets d'investigation et quarante-deux runs les 20-21 septembre, deux runs et sept pièces thématiques le 22, re-sourçages le 23) : **quatre jours**. Une inflation de durée non étayée, du type exact que le protocole interdit. **Corrigé.**

### Sévérité HAUTE — calibration, cohérence, provenance

- **F-08. La règle de la marge n'était pas appliquée à l'ouverture.** Le geste 2 enseigne « un mouvement d'un dixième ne signifie rien » alors que l'ouverture installe le « sixième trimestre consécutif » de hausse (0,2 point) comme un fait. Le lecteur attentif pouvait retourner la critique contre l'article. **Corrigé** par une auto-application explicite dans le geste 2 : le niveau est établi, la marche d'un trimestre non.
- **F-09. Attribution fautive des conventions.** Les quatre vannes de l'indexation étaient présentées comme des « choix » sans dire qui les fixe : l'IRL par la loi, le plafond par le Parlement, le barème en loi de finances, les retraites par décret. L'Insee produit l'indice, pas la convention, et la métaphore de la manivelle pouvait laisser croire l'inverse. **Corrigé** par une attribution explicite.
- **F-10. Deux régimes d'erreur confondus.** « structurellement bas » (biais des révisions de croissance) et « les erreurs ne vont pas toujours dans le même sens » (surprises de recettes) se lisaient comme une contradiction. **Corrigé** en nommant les deux régimes.
- **F-06. La citation la plus exposée était la seule note sans provenance.** Note [41], qui porte le « ±17 500 personnes » cité deux fois dans le corps, n'avait ni URL ni référence de run, contrairement à toutes ses voisines. **Corrigé**, et mieux : vérification externe (§5) a retrouvé la fiche et son URL, et l'audit a mis au jour une anomalie de la source elle-même, désormais écrite en note plutôt que tue.
- **F-12. Méthode du recensement imprécise.** « 8 % des adresses des grandes » alors que le producteur écrit « un échantillon d'adresses représentant 8 % de leurs logements ». **Corrigé**, avec un payload supplémentaire vérifié au passage : cinq enquêtes cumulées couvrent environ 40 % de la population des communes de 10 000 habitants ou plus.
- **F-13. Loi mal datée.** « comme le veut la loi de 1989 » : l'IRL ne vient pas de la loi de 1989 mais de l'article 35 de la loi n° 2005-841 du 26 juillet 2005, inséré à l'article 17-1, applicable au 1er janvier 2006, en remplacement de l'indice du coût de la construction. **Corrigé**, avec un gain de thèse : la bascule d'indice a déplacé de l'argent sans qu'aucune ligne budgétaire ne change.
- **F-14. Le « aucun » de l'audit presse sortait de son cadre.** Dix-neuf articles lisibles, fenêtre bornée, sélection autour des jours de communiqués : la note et l'appendice l'affichaient, le corps le taisait. **Corrigé** par une incise dans le corps.
- **F-23. Qualificatif non factuel.** « un institut de conjoncture indépendant » pour Rexecode : « indépendant » est une appréciation. **Corrigé** en « institut de conjoncture privé » (corps et note).

### Sévérité MOYENNE et BASSE — laissées en décisions

- **F-11.** Le « prior » de H1 est un adjectif, pas un taux : aucun dénominateur de base rate (combien d'instituts nationaux pris en défaut dans les démocraties de l'OCDE depuis 1990 ?). L'article promet des priors affichés ; il n'en affiche qu'un qualificatif.
- **F-16.** Le titre « Ce que l'INSEE ne vous dira jamais » est défendable sous la lecture « publier n'est pas dire », mais cette distinction n'était nulle part posée. **Corrigé** en la fondant dans l'ouverture, plutôt qu'en changeant le titre (décision éditoriale laissée ouverte : un titre alternatif du type « Ce que l'INSEE publie et que personne ne répète » reste disponible).
- **F-15.** « systématiquement trahie en aval » : universel tiré d'un échantillon de commodité sur un indicateur. **Corrigé** par un scoping (« sur chacun des objets que nous avons examinés »).
- **F-17.** Le café du début ne revient jamais : la boucle du lecteur ne se ferme qu'aux quatre gestes. **Corrigé** par un rappel explicite dans la section du logement, qui relie fréquence des achats et inflation perçue.
- **F-18.** Dimension absente : à qui profite la défiance ? Le trou de transmission arme aussi ceux qui préfèrent qu'aucune mesure n'existe. **Décision ouverte.**
- **F-19.** 8 600 mots et 44 notes : la traçabilité occupe plus de volume que la démonstration dans l'appareil, et l'appendice B duplique les notes. **Décision ouverte** (variante courte, ou déplacement de l'appareil en ligne).
- **F-20.** Le kit gagnerait un cinquième geste que l'article pratique déjà sans le nommer : croiser avec une source qui n'a pas intérêt au même résultat (Eurostat, ONS, Destatis). **Décision ouverte.**
- **F-21, F-22.** Inégalités de tier mineures (arrondi de l'euro sourcé par Europe 1 et Ouest-France ; jargon « contrefactuel », « cui bono » en appendice). **Signalés, non corrigés.**
- **F-24.** L'absolu « Aucun audit forensique de type argentin n'a jamais été mené sur l'Insee » : un absolu négatif fragile en droit comme en épistémologie. Requalification proposée en décision (audit contradictoire public des microdonnées), non appliquée pour ne pas modifier une affirmation sans arbitrage.
- **F-25.** Ancrage de lecture sur « 610 milliards » avant « 356,4 » : le plus grand nombre s'imprime le premier. **Corrigé** partiellement par une phrase (« le plus grand des deux n'est pas le plus vrai ; il est le plus large »), l'ordre restant inchangé.

---

## 3. Corrections appliquées (récapitulatif vérifié)

Sous-titre (« Sept malentendus ») ; ouverture café (1,52 euro couvre le café, pas le croissant) ; panier du matin (10,40 francs, borne du croissant assumée) ; fondation « publier n'est pas dire » et durée réelle (quatre jours) ; attribution des quatre conventions ; rappel du comptoir (fréquence contre poids) ; méthode du recensement et payload des 40 % ; IRL (loi de 2005, bascule de l'indice du coût de la construction) ; incise sur la fenêtre de l'audit presse ; Rexecode requalifié ; nomination des deux régimes d'erreur ; « Presque tout est publié » ; scoping de « trahie en aval » ; auto-application de la règle de la marge ; phrase de cadrage sur les périmètres ; notes [4], [11], [21], [29], [34], [41] complétées ou requalifiées.

Contrôles après corrections : 0 tiret cadratin ou demi-cadratin, 44 notes définies et 44 appelées dans le corps, aucun ancien tic résiduel (« Six malentendus », « Pendant trois semaines », « Tout est publié »), aucun chiffre de l'appareil perdu.

---

## 4. Décisions qui appartiennent à l'éditeur

1. **Titre** : conserver « Ce que l'INSEE ne vous dira jamais » avec la distinction désormais fondée, ou passer au titre de transmission (« ce que l'INSEE publie et que personne ne répète »).
2. **F-11** : ajouter un dénominateur de base rate pour H1, ou écrire que le taux n'est pas estimable et pourquoi.
3. **F-18** : ajouter le paragraphe « à qui profite la défiance ».
4. **F-19** : trancher entre l'article long et une variante courte avec appareil déporté.
5. **F-20** : ajouter le cinquième geste (croisement avec une source aux intérêts opposés).
6. **F-24** : requalifier l'absolu sur l'absence d'audit forensique.

---

## 5. Vérifications externes conduites pendant l'audit

- **Insee, « Présentation du recensement de la population »** — page consultée en direct le 23 septembre 2026 (https://www.insee.fr/fr/information/2383265). Établit le verbatim de la méthode (« une commune sur cinq chaque année » ; « un échantillon d'adresses représentant 8 % de leurs logements ») et le chiffre de couverture cumulée (« 40 % environ de la population des communes de 10 000 habitants ou plus »). Tier T1.
- **Insee, « La précision des résultats du recensement »** — fiche méthodologique, texte indexé retrouvé le 23 septembre 2026 (https://www.insee.fr/fr/statistiques/fichier/2383177/fiche-precision.pdf). Le verbatim « coefficient de variation de 0,01 %, soit une imprécision de + ou - 17 500 personnes » est confirmé par l'index du document ; le PDF lui-même reste non extractible par nos outils. Le dénominateur n'est pas chiffré dans le document, et l'ordre de grandeur implicite du coefficient (175 millions pour produire ±17 500) n'est celui d'aucun ensemble français : l'anomalie est désormais écrite en note [41] au lieu d'être passée sous silence.
- **Origine de l'IRL** — l'article 35 de la loi n° 2005-841 du 26 juillet 2005 a créé l'IRL à l'article 17-1 de la loi du 6 juillet 1989, applicable au 1er janvier 2006 en remplacement de l'indice du coût de la construction (sources juridiques secondaires concordantes, recherche du 23 septembre 2026). Tier T3 pour la formulation, le fait étant recoupé sur trois sources indépendantes.
- **Datation du corpus Insee** — relevé du dépôt : `investigations/2026-09/2026-09-20_campagne-insee-indexation`, `2026-09-22_blindage-insee-4-axes`, `2026-09-22_insee`, runs horodatés du 20 au 23 septembre 2026. Tier T1 (registres internes). C'est cette pièce qui réfute « trois semaines ».

---

## 6. Ce que cet audit n'a pas pu trancher

- Le contenu du**corps intégral de la dépêche** du 7 août 2026 (paywall) et l'identité de l'agence rédactrice restent hors de portée : l'article le dit, l'audit ne peut pas mieux.
- La page portant les **610 Md€** reste à lecture dégradée : la contradiction de périmètres est donc documentée mais asymétriquement sourcée.
- Le **dénominateur de l'imprécision du recensement** est introuvable dans les documents accessibles ; l'anomalie est signalée, pas résolue.
- La **masse des loyers SDES** (issue d'un run antérieur) n'a pas été re-fetchée ici : si l'article devait produire une scène d'indexation chiffrée supplémentaire, elle doit l'être avant publication.
- Enfin, l'audit est **interne** : il a été conduit par la même chaîne qui a produit l'article. Un œil extérieur — relecteur humain, ou contradictoire documentaire — reste la seule épreuve non circulaire.

---

## 7. Double check du 23 septembre 2026, 06 h 20 — y compris contre l'audit lui-même

Le double check ne porte pas sur l'article mais sur **l'audit**, et il a trouvé trois choses, dont une erreur de l'audit.

**7.1. L'audit avait surestimé son propre finding F-07.** L'audit soupçonnait la note [11] de citer un titre de presse construit (guillemets sans vérification). Vérification par recherche le 23 septembre 2026 : le titre existe, en ligne, daté, avec URL — Le Figaro, « Le chômage progresse pour le sixième trimestre consécutif, à 8,3% », 7 août 2026 (https://www.lefigaro.fr/conjoncture/le-chomage-progresse-pour-le-sixieme-trimestre-consecutif-a-8-3-20260807). Le défaut réel n'était donc pas la fabrication d'un titre mais **l'absence d'URL** : note [11] et corps restaurés en citation vérifiée, avec source. L'audit a produit un faux positif de sévérité : à inscrire à son passif.

**7.2. L'audit avait recopié un compte sans le vérifier — dans le décompte même qu'il prétendait auditer.** F-03 citait « quatorze dossiers le 20-21 » : ce chiffre venait de l'appendice A de l'article, que l'audit a repris sur foi. Relevé réel du dépôt : la campagne des 20-21 septembre contient **vingt-deux sujets d'investigation et quarante-deux runs**, la journée du 22 **deux runs et sept pièces thématiques**. L'appendice A annonçait quatorze et sept, et sa liste de quatorze omettait précisément les six investigations `inv-a` à `inv-f` (mandat et arbitrage des conventions, origine des conventions, référentiels alternatifs, justification des conventions, impact parlementaire et budgétaire, fait négatif adversarial) — c'est-à-dire les pièces qui portent la partie la plus délicate du dossier. **Corrigé dans l'article** (comptes et liste) et dans le présent artefact. Un audit qui prend un chiffre de l'appareil pour argent comptant commet l'erreur qu'il reproche à la presse.

**7.3. Le double check a de plus attrapé une faute mécanique commise pendant les corrections.** L'insertion de « Le Figaro, 7 août 2026 » dans l'appareil de sources a été appliquée par erreur à l'intérieur de la note [26] au lieu de l'appendice B (la chaîne recherchée était capitalisée, l'appendice ne l'était pas). Corrigé : « Le Figaro » est dans l'appendice B, la note [26] est revenue à son état initial. Leçon : une correction appliquée est une correction à re-vérifier, et la chaîne de caractères d'une correction est elle-même un objet fragile.

**7.4. État vérifié après le double check** (article `2026-09-23_06-00`) : 0 tiret cadratin ou demi-cadratin, 44 notes définies et 44 appelées, appendice A aligné sur le dépôt, note [11] pourvue d'URL, note [26] propre, aucune occurrence résiduelle de « quatorze dossiers » ni de « trois semaines ». Décompte exact des modifications appliquées depuis la version soumise à l'audit : **vingt et une localisations** (dont six notes), plus quatre modifications issues du double check.

**7.5. Ce que le double check confirme et ce qu'il ne confirme pas.** Il confirme les findings F-01, F-02, F-04, F-05, F-06, F-08, F-09, F-10, F-12, F-13, F-14, F-23, qui reposent sur des pièces vérifiables citées plus haut. Il **ne** confirme pas F-11 (prior de H1), F-18, F-19, F-20, F-24, qui restent des jugements éditoriaux : la décision t'appartient, et aucun de ces points n'est un fait que l'on pourrait trancher par une source.
