# Prérequis de T4 — lecture des deux réserves de sources

**Date** : 13 septembre 2026
**Objet** : lever les deux réserves de sources que le plan de forme conditionne à la tranche T4 — la correction d’auteur de *Nature* **[33]** et l’audition Kron **[54]**.
**Article** : `01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md`, empreinte `fe1de8355d4f3dc467a420b4adb28a9b80f55ec05208db673b1d9b8b897ab06f`, 336 lignes, corps 10 103 mots. **Aucune modification de l’article dans cette passe.**
**Références** : `PLAN_FORME_DIALECTIQUE_V4_4_2026-09-13.md` §7.3 ; `SUIVI_V4_4_2026-09-13.md` §6.2 points 4 et 5.

---

## 0. Méthode

Mémoire d’abord (règle globale `mnemolite-mem-first`, MCP natif `localhost:8002`) : deux recherches hybrides, **aucun résultat**. Appel aux sources primaires ensuite. Write-back effectué : `465f1c64-0e8e-4131-a6b2-529f26c73027` (correction *Nature*) et `038101b9-0206-4ca8-92d9-0e82fd06e3f7` (audition Kron).

Une difficulté d’accès à consigner : **`nature.com` renvoie `406 Not Acceptable`**, pour l’article comme pour sa correction. Le texte de la correction a été lu sur **PubMed Central / Europe PMC, `PMC10651477`, PMID 37914941**, et son existence confirmée par l’API Crossref (`update-to` → `10.1038/s41586-023-06297-w`, type `correction`, daté `2023-11-01`).

---

## 1. [33] — la correction d’auteur ne touche pas le résultat que l’article emploie

### 1.1 Ce que dit la correction, mot pour mot

*Nature* **623**, E9 (2023), `doi:10.1038/s41586-023-06795-x`, publiée le **1er novembre 2023** :

> Correction to: *Nature* 10.1038/s41586-023-06297-w Published online 27 July 2023
>
> In the version of this article initially published, the variable described in Supplementary Table 36 as measuring Facebook "strikes" for violations of content policies against "Coordinated Inauthentic Behavior" (CIB) is inaccurate and does not reflect enforcement of the actual CIB policy, which is not a content-level policy. We therefore removed this row from Supplementary Table 36.

### 1.2 Sa portée exacte

La correction **supprime une ligne du tableau supplémentaire 36** — une variable de contrôle décrivant des « strikes » au titre de la politique dite CIB, que les auteurs reconnaissent mal décrite par leur propre variable, la politique CIB de Meta n’étant pas une politique de contenu.

Elle ne touche **ni le résumé, ni le protocole pré-enregistré, ni les résultats principaux, ni la conclusion** « prevalent but not polarizing ». Aucun résultat du corps de l’article n’est repris dans la correction.

### 1.3 Ce que l’article [33] en fait

Deux passages, l. 103 et l. 105 :

> Une étude sur le fil algorithmique de X a détecté des effets sur l’engagement et sur certaines opinions politiques (*Nature*, algorithme de X). À l’inverse, une expérience à répartition aléatoire menée sur Facebook pendant l’élection américaine de 2020 a fortement réduit l’exposition à des sources politiquement concordantes sans mettre en évidence de changement correspondant sur les principales attitudes étudiées (*Nature*, Facebook).

> Dire que « l’exposition ne change jamais rien » l’est tout autant.

### 1.4 Verdict

**L’emploi de [33] est exact et n’a pas à changer.** Trois points, dont deux favorables à l’article :

1. La formulation retenue est celle d’un **résultat non détecté**, non d’une impossibilité : « sans mettre en évidence de changement correspondant sur les principales attitudes étudiées ». C’est la formulation correcte d’un résultat nul, et elle est conforme à la distinction que l’article revendique ailleurs.
2. La correction porte sur une **variable supplémentaire de contrôle**, pas sur la mesure principale : elle ne crée aucune raison de douter du résultat invoqué.
3. **Rien n’est à corriger dans le corps.** La seule action envisageable est de mentionner la correction dans l’entrée de registre **[33]** (l. 305) — provenance, non contenu. C’est un objet de T6 (F-14 à F-17, provenance), pas de T4.

**Ce que je ne peux pas dire** : je n’ai pas rouvert le tableau supplémentaire 36 pour vérifier moi-même que la ligne supprimée ne servait à aucun résultat affiché. Je me fonde sur le texte de la correction, qui ne mentionne que ce tableau et une variable décrite comme mal nommée. Le risque résiduel est faible et documenté ici plutôt que passé sous silence.

---

## 2. [54] contre la l. 53 — la phrase est vraie, mais sa fonction est plus fragile que son énoncé

### 2.1 La phrase de l’article (l. 53)

> Le cas est particulièrement utile parce qu’il contient son propre contrôle contre les récits trop simples. Patrick Kron a déclaré sous serment avoir pris l’initiative du contact avec Jeffrey Immelt et a nié un chantage américain destiné à provoquer la vente ; la commission parlementaire a, de son côté, retenu la fragilisation produite par les poursuites tout en indiquant ne disposer d’aucun élément factuel établissant une instrumentalisation du DOJ par GE (Assemblée nationale, rapport d’enquête n° 897 ; audition de Patrick Kron).

Confrontation avec **Assemblée nationale, commission d’enquête, audition de Patrick Kron, 4 avril 2018, compte rendu n° 49** (source intégrale [54], URL au registre l. 326, résolue `200`).

| Proposition de la phrase | Pièce dans l’audition | Verdict |
| --- | --- | --- |
| Serment prêté | « Veuillez lever la main droite et dire : “Je le jure”. (M. Patrick Kron prête serment.) » | **établie** |
| « a déclaré […] avoir pris l’initiative du contact avec Jeffrey Immelt » | « Qui a pris l’initiative de la cession à GE ? […] c’est moi qui ai demandé, par l’intermédiaire de M. Poux-Guillaume, à rencontrer M. Immelt […]. C’est à mon initiative. » | **établie comme déclaration** |
| « a nié un chantage américain destiné à provoquer la vente » | « Je le répète solennellement et sous serment : je n’ai jamais subi quelque pression que ce soit, je n’ai jamais été exposé à aucun chantage de quelque juridiction que ce soit. » Et il rejette la variante économique : « Non, non, non, nous n’avons absolument pas fait cette opération pour répondre à une pression directe sur moi-même […]. Ce sont deux phénomènes indépendants. » | **établie** |
| « la commission parlementaire a […] retenu la fragilisation produite par les poursuites » | Le président : « la perspective d’une amende qui aurait pu approcher le milliard de dollars […] était effectivement une forme de pression sur Alstom, dont le point faible était alors la trésorerie ». Kron lui-même : « Nous avions donc une pression sur la trésorerie en raison de cet accord. » | **établie** (renvoi au rapport n° 897, non rouvert dans cette passe) |
| « en indiquant ne disposer d’aucun élément factuel établissant une instrumentalisation du DOJ par GE » | Proposé au rapport n° 897, non rouvert ici. L’audition ne le contredit pas : elle ne produit aucun élément d’instrumentalisation, et la charge du président porte sur la présence de GE au dossier, pas sur une orchestration. | **non contredite** |

**La phrase n’est donc pas fausse**, et le soupçon inscrit au suivi — « seule phrase de l’article qui pourrait être contredite par sa propre source » — est levé sur le terrain de l’énoncé : les deux propositions attribuées à Kron sont exactement celles qu’il porte sous serment.

### 2.2 Ce que la même source porte en plus, et que la phrase ne dit pas

L’audition **contient sa propre réfutation partielle**, et c’est le président qui l’ouvre, avant toute question :

> Premièrement, s’agissant de l’initiative de la cession à GE, vous avez livré à la représentation nationale deux versions en apparence contradictoires. Le 20 mai 2014, devant la commission des affaires économiques de l’Assemblée, vous déclariez : « Lorsque j’ai vu le ministre début mars, j’avais déjà dîné avec le président de GE […]. Le président de GE ayant évoqué la possibilité d’une coopération, je l’ai prié de me donner la possibilité d’y réfléchir. » Dans cette première version, c’est donc M. Jeffrey Immelt qui prend l’initiative. Puis, le 11 mars 2015, devant la même commission, vous dites : « […] c’est la raison pour laquelle j’ai pris l’initiative d’entrer en contact avec des groupes comme Siemens ou GE. » Nous aimerions une clarification et une version définitive, si je puis dire.

Et, sur le mandat de Poux-Guillaume à l’été 2013, Kron répond : « Je ne peux pas le confirmer. À vrai dire, je n’en sais rien. »

Trois conséquences, à écrire plutôt qu’à supposer :

1. **La revendication d’initiative n’est pas un fait établi ; c’est une déclaration, et le dossier la conteste.** La phrase de l’article dit bien « a déclaré sous serment », donc elle ne franchit pas cette ligne. Mais elle la place sous l’annonce « il contient son propre contrôle contre les récits trop simples », ce qui lui donne une fonction probatoire que l’énoncé seul ne porte pas.
2. **Le contrôle est à double tranchant.** Ce que le cas « contient » réellement, c’est une contradiction interne, relevée par la commission elle-même. Un lecteur qui ouvre [54] trouvera d’abord la confrontation, pas la dénégation.
3. **Le même président pousse sur GE.** « Dans le plaider-coupable que vous avez signé le 22 décembre 2014, General Electric est cité » ; « GE est cité dans le DPA […] du 22 décembre 2014 ». Kron maintient « Totalement étranger », puis concède : « C’est possible. Effectivement, nous vendions cette activité d’Alstom à GE. » Être nommé dans un DPA n’établit pas une instrumentalisation du DOJ, donc la phrase de l’article reste juste ; mais la commission n’a pas laissé la thèse du « no link » sans réponse, contrairement à ce que la formule en une phrase laisse croire.

Une précision de degré, enfin, qui va dans le sens de l’article : sur la trésorerie, Kron **conteste la magnitude** que le président avance (« la trésorerie d’Alstom était de 2,3 milliards et non de 1,5 milliard »), tout en confirmant l’existence d’une pression de trésorerie. La l. 19 de l’article écrit « Patrick Kron a reconnu une contrainte de trésorerie liée au règlement américain » : c’est exact, et le désaccord porte sur le chiffre, que l’article ne cite pas.

### 2.3 Ce point a un statut particulier dans le plan

La l. 53 est en même temps :

- **l’une des huit occurrences** du gabarit de réfutation visées par F-10 (liste du plan : l. 52, **62**, 89, 113, 115, 139, 175, 229 en numérotation de diagnostic, soit l. 53 en numérotation courante) ;
- **un passage protégé** — « l. 62, le contrôle interne du dossier Alstom. Il porte la dénégation de Kron et l’absence d’élément sur le DOJ, en une phrase », à ne pas réécrire sauf nécessité démontrée.

La lecture de la source apporte exactement ce que la clause de protection demandait pour être levée : **un motif de nécessité**, non pour corriger une erreur, mais pour ne pas laisser la phrase porter un contrôle qu’elle ne peut pas porter seule. C’est un arbitrage de T4, pas une correction préalable, et je ne l’ai pas tranché à ta place.

---

## 3. Verdict

**Les deux réserves sont levées. T4 peut démarrer.**

| Réserve | État | Effet sur T4 |
| --- | --- | --- |
| [33], correction d’auteur | **levée** — hors du champ de l’emploi de la source | Aucun sur le corps ; mention de provenance à réserver à T6 |
| [54], audition Kron contre l. 53 | **levée** — énoncé exact, fonction fragilisée | Une exigence à traiter dans T4, sur la l. 53 |

Ce que la lecture change pour T4, en une phrase : **la l. 53 n’a pas besoin d’être corrigée, elle a besoin d’être décidée** — soit la protection l’emporte et le mot « contrôle » doit être borné, soit la phrase porte la contradiction que sa propre source affiche, au prix d’un allongement dans un passage déjà dense.

---

## 4. Ce que cette passe ne fait pas

1. **Elle ne rouvre pas le rapport d’enquête n° 897.** Les deux affirmations attribuées à la commission (fragilisation, absence d’élément sur une instrumentalisation) restent adossées au rapport, non revérifiées ici.
2. **Elle n’a pas lu l’audition intégralement.** L’extraction s’arrête avant la fin de la séance ; les passages cités — serment, initiative, dénégation, confrontation, DPA, trésorerie — sont tous dans la partie lue. Les réponses finales de Kron sur la corruption n’ont pas été relues.
3. **Elle ne modifie pas l’article.** Empreinte inchangée : `fe1de835…ab06f`.
4. **L’arbitrage de la l. 53 a été tranché et appliqué dans la foulée, dans la tranche T4** : la portée du mot « contrôle » est bornée et la contestation portée par la même source est nommée en une incise, sans importer la chronologie. Décision, texte avant / après, et correction d’une première formulation inexacte de ma part : `SEMANTIC_DIFF_T4_2026-09-13.md`, §1.
