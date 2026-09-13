# Plan consolidé de corrections : article V4.4 (v2)

> Produit le 2026-09-13, remplace la v1. Principe de cadrage : **baisser l'ambition théorique, monter l'ambition probatoire**. Contrainte : rester forensique, analytique, conforme au corpus publié.
>
> Deux diagnostics ont été confrontés : le mien, appuyé sur des mesures faites sur le corpus publié, et celui du pont, appuyé sur la lecture de l'article seul. La v2 retient ce que chaque côté apporte de meilleur, et corrige les erreurs des deux.
>
> État de la cible : **63 éditions appliquées**, empreinte `1cb2f0c12b4736f2893d1238fd6effd0eba3d0abdb1f2fccaee28b9711cdff66`.
>
> **APPLIQUÉ le 2026-09-13 : rangs 1 à 6** (prérequis, garde-fou, titre, lignée, formules abaissées, bilan à paliers, contrôles, codage interne, quatre coordonnées, conformité C1 à C5) **et rang 8** (contrôle terminal : 62 propositions générales examinées, 8 défauts corrigés). **Non appliqué : rang 7**, c'est-à-dire les 4 figures et la compression, qui sont des décisions de l'auteur. Détail : `07_COLLAB_CHATGPT/2026-09-13_patch_log_editions.md` sections 10 et 11, `07_COLLAB_CHATGPT/2026-09-13_CONTROLE_TERMINAL.md` pour le contrôle phrase par phrase, et `RAPPORT_AUDIT_ADVERSARIAL_V4_4.md` sections 18 et 19.
>
> Trois écarts assumés à ce plan : pas de tableau de profil de preuve (forme absente du corpus) ; le gras passe de 35 à 49 segments (hausse, dans la plage du corpus) ; les nombres ne sont convertis qu'en partie (grandeurs mesurées, pas articulations du raisonnement).

## 0. Ce que le corpus accepte comme forme, mesuré

| Forme | Présence dans le corpus publié | Conséquence |
|---|---|---|
| Tableau Markdown | **zéro ligne `|` sur les articles publiés mesurés** (déchèteries, 6 343 mots ; ingérence sans mesure, 6 034 ; opacité, 5 011), et zéro dans V4.4 | **Un tableau central est exclu** |
| Figure, image | **zéro dans tout le corpus publié**, 4 dans V4.4 | Les figures sont un écart de forme |
| Bilan en prose à paliers | présent : « Est démontré : [...] Sont des coûts du système, mais pas des effets : [...] Est suggéré, sans série nationale : [...] » (déchèteries) | **Forme retenue pour le bilan probatoire** |
| Liste numérotée dans le corps | présente : 26 items chez Fedorova, dont « La chaîne probatoire à reconstituer » avec 8 items | **Forme retenue pour l'inventaire des relations ouvertes** |
| Puces `-` dans le corps | 24 items chez un seul article, 0 ailleurs | à éviter |
| Citations numérotées `[n]` dans le corps | **0 occurrence mesurée** sur les trois articles comptés | 77 à convertir |
| Gras, corps seul | 8, 16, 29, 39, 110 segments selon l'article | **V4.4 est à 35, dans la plage : rien à dégraisser** |
| Chiffres | écrits en chiffres | lettres à convertir |

**Correction de la v1.** La v1 recommandait de diviser le gras de V4.4 par deux, en comparant 91 segments à une plage de 12 à 40. **C'était une erreur de mesure** : le comptage portait sur le fichier entier, or la bibliographie met chaque numéro en gras, ce qui ajoutait environ 118 marqueurs. Mesuré sur le corps seul, V4.4 est à 35 segments, au milieu de la distribution réelle (8 à 110). **La recommandation est retirée.**

## 1. Acquis déjà en place, à ne pas refaire

Éditions 36 à 41 : trois niveaux (capacité, pouvoir mobilisable, pouvoir exercé) écrits et alignés ; borne des archives posée ; trois confusions capacité / pouvoir exercé supprimées.

---

## 2. Prérequis, avant toute statistique (adopté du pont)

**Fixer l'unité probatoire.** Le texte raisonne en **cas** (une vingtaine), le corpus de travail code des **affirmations** (445), et la thèse porte sur des **relations causales**. Publier un chiffre sans dire quelle unité il compte fabriquerait une précision artificielle, et c'est exactement le défaut que l'article reproche aux autres.

Trois définitions à poser dans le paragraphe de méthode :

1. **le cas** : un dossier nommé, avec ses pièces ;
2. **l'affirmation codée** : une proposition élémentaire extraite d'une investigation, avec son niveau de preuve ;
3. **la relation** : le lien entre deux niveaux du même cas (capacité vers exercice, exercice vers effet, effet vers décision).

Aucun chiffre n'est publié avant que l'unité soit énoncée.

## 3. Garde-fou méthodologique, à écrire une fois (adopté du pont)

**La variable finale n'est pas la même d'un cas à l'autre.** La sortie à expliquer est une vente chez Alstom, une modification de texte dans l'EUCS, une nomination dans le cas espagnol, une sélection dans le fact-checking, une attitude dans les études de plateformes, une décision juridictionnelle chez Rockhopper.

Conséquence, à énoncer dans le texte : le profil de preuve doit rester **un profil**, jamais devenir une métrique commune. La relation finale doit être définie dossier par dossier, et aucun score global n'est produit. Cette phrase protège l'article de sa propre dérive, et elle remplace la « métrique de réversibilité » de la v1.

---

## Axe A. Baisser l'ambition théorique

### A1. Titre et sous-titre (priorité 0)

Le pont propose : *« Le pouvoir sans commande : jusqu'où les preuves permettent-elles d'aller ? »*. Il garde la formule d'appel, retire la promesse explicative, et tient en une ligne.

Proposition consolidée, qui garde la question du pont et borne l'objet :

> **# 🎚️ Le pouvoir sans commande : jusqu'où les preuves permettent-elles d'aller**
>
> *Enquête sur ce qu'un corpus documentaire permet d'établir entre capacité, levier exercé, effet observable et décision finale : les relations fermées, les relations ouvertes, et la pièce qui manquerait à chacune.*

Variante courte pour le sous-titre : *Ce qu'une enquête documentaire peut établir du pouvoir, et où exactement s'arrête la preuve.*

### A2. Formules à abaisser (priorité 0)

| Formule actuelle | Portée à retirer | Remplacement |
|---|---|---|
| « Ces affaires conduisent à une **définition pratique du pouvoir** » | promet une définition générale | « conduisent à une **règle pratique d'analyse** » |
| « On peut donc **définir un contre-pouvoir** » | idem | « Pour cette enquête, un contre-pouvoir se définit comme [...] » |
| « Le fil commun tient en une phrase » | loi générale | « Dans les cas examinés, une règle se répète » |
| « **plus important pour une théorie du pouvoir** » | revendique une théorie | « plus important pour ce que l'enquête peut conclure » |
| « Le pouvoir **se mesure** au coût nécessaire pour rouvrir » | promet une mesure | « le coût de réouverture est l'une des quatre coordonnées de la réversibilité » |
| « Le point d'arrivée est **le pouvoir** » | annonce une notion | « Le point d'arrivée est **ce qu'on peut en établir** » |

### A3. La lignée, en trois phrases (priorité 0)

**Correction d'attribution.** Le pont écrit « Lukes l'action sur l'agenda et les préférences ». C'est inexact : la **non-décision et le contrôle de l'agenda** appartiennent à Bachrach et Baratz (1962) ; **Lukes** (1974) ajoute le **façonnement des préférences**. La formulation doit séparer les deux, sinon un lecteur informé relèvera l'approximation là où la citation est censée protéger.

Texte proposé, à placer après le fait d'ouverture, avant la grammaire probatoire :

> L'idée qu'un pouvoir puisse peser sans ordre direct n'est pas nouvelle. Bachrach et Baratz ont décrit en 1962 la non-décision, ce pouvoir de garder un sujet hors de l'agenda ; Lukes y a ajouté en 1974 le façonnement des préférences et des options ; Susan Strange a systématisé l'ensemble en 1988 sous le nom de pouvoir structurel. Ce cadre est ici emprunté, et il n'est pas présenté comme un résultat de l'enquête. L'apport recherché est plus étroit, et il est vérifiable : déterminer, dossier par dossier, jusqu'où la preuve ferme la chaîne entre capacité, usage du levier, effet observable et décision finale.

**Désaccord avec ma v1, adopté du pont.** La v1 proposait d'organiser le bilan selon les quatre structures de Strange (sécurité, production, finance, connaissance). **À écarter** : le Department of Justice, l'arbitrage et l'instrument anti-coercition ne se rangent pas proprement dans « sécurité » sans forcer la taxonomie. Strange sert à créditer la lignée, pas à découper l'article. Le classement se fera par **famille de levier**, décrite cas par cas.

---

## Axe B. Monter l'ambition probatoire

### B1. Le bilan probatoire, en prose à trois paliers (opération centrale, priorité 1)

Forme mesurée comme conforme : le bilan à paliers de la déchèterie. Emplacement : après le « fil commun », avant les trois questions pratiques.

> **Est établi** : les positions et les droits (parts, décrets, notifications, participations), les actes datés (une confiscation payée, une livraison interrompue, un texte modifié, une autorisation refusée), et dans plusieurs cas l'effet intermédiaire (un coût, un prix, une condition, une adaptation).
>
> **Est établi sans que la décision finale le soit** : [les cas où l'exercice est documenté et où la sortie politique n'est pas attribuable].
>
> **N'est établi dans aucun des cas examinés** : le lien entre l'exercice d'un levier et la décision politique finale, et l'existence d'une coordination entre leviers.

Puis, sous cette forme de **liste numérotée** (modèle : « La chaîne probatoire à reconstituer » chez Fedorova), l'inventaire des relations ouvertes :

> Pour que la relation manquante soit établie, il faudrait documenter, cas par cas : 1. l'acte exact et son auteur ; 2. la date ; 3. la pièce qui relie l'acte à l'effet intermédiaire ; 4. la pièce qui relie l'effet intermédiaire à la décision ; 5. ...

### B2. Les contrôles déjà présents, à exploiter explicitement (priorité 1)

Le pont en a listé neuf, et sa liste est meilleure que la mienne. À nommer comme tels dans le texte, au lieu de les ranger dans une série uniforme :

- **contrôle positif** : gaz russe 2022 (condition, refus, interruption, coût, adaptation) ;
- **contrôles négatifs** : New IP (tentative organisée, échec), Chine-Lituanie (pression réelle, aucune concession) ;
- **exercice jusqu'au veto** : Photonis ;
- **quasi-contrôle apparié** : Djebbari / CMA CGM refusé contre Djebbari / Hopium autorisé ;
- **taux de base rare** : HATVP, 751 projets, 639 avis, 95,5 % de compatibilité ;
- **paire d'effets opposés** : algorithme de X contre fil Facebook ;
- **réversibilité d'une décision favorable** : Rockhopper, sentence annulée ;
- **relations fermées et causalités ouvertes dans un même dossier** : Alstom.

### B3. Le codage interne, publié comme contrôle et non comme résultat (priorité 0)

Formulation adoptée du pont, plus prudente que la mienne :

> Le corpus de travail permet un contrôle interne. Dans le sous-corpus qu'il code lui-même, sur 445 affirmations réparties en 45 investigations, 357 portent l'absence de signal causal et 88 sa présence. Ce codage est auto-déclaré, il ne couvre qu'une partie des investigations, et il ne mesure ni une prévalence réelle ni la validité des affirmations. Il établit une seule chose : la prudence causale de cet article correspond à celle de sa propre base.

**À ne pas écrire** : « 80 % des causalités ne sont pas établies ». Ce serait transformer un codage interne en fréquence du monde.

**Chiffres vérifiés à la source**, le 2026-09-13, dans `03_FORENSIC_INDEX/CLAIM_EVIDENCE_TRACE.csv` (445 lignes de données, hors en-tête) :

| Mesure | Valeur |
|---|---|
| affirmations codées | **445** |
| investigations couvertes | **45**, de `INV-001` à `INV-045`, sans trou |
| `causal_signal` | **357 NO** / **88 YES** |
| `evidence_level` | **386 E2** / 32 E3 / 16 E1 / 11 E0 |
| `quantitative_signal` | 394 YES / 51 NO |
| `primary_source_signal` | 116 YES / 329 NO |

La formulation du pont (« INV-001–045 ») est donc exacte. Le chiffre de 357 est un **comptage interne à un sous-corpus**, et il doit être publié avec cette borne, jamais comme un taux.

### B4. Les quatre coordonnées de la réversibilité, sans agrégation (priorité 1)

> La réversibilité se lit sur quatre coordonnées, et l'enquête ne les agrège pas : un substitut existe-t-il, en combien de temps, à quel coût, et par quel recours une option peut-elle être rouverte. Ces dimensions ne sont pas commensurables. Fabriquer un indice unique reviendrait à produire la mesure que cet article reproche aux autres de ne pas publier.

---

## Axe C. Conformité au corpus, après stabilisation du fond

| # | Opération | Mesure de départ |
|---|---|---|
| C1 | Ouvrir sur un fait daté, et déplacer l'abstraction après | chapeau actuel abstrait |
| C2 | Convertir les citations en sources nommées et liées dans la prose | 77 marqueurs, environ 40 paragraphes, 6 séquences de 3 références ou plus |
| C3 | Conserver le registre numéroté final | les rapports d'audit s'y réfèrent |
| C4 | Ajouter les séparateurs rythmiques entre les parties | 1 seul `---` aujourd'hui |
| C5 | Convertir les nombres écrits en lettres | usage du corpus |
| C6 | Trancher sur les 4 figures | 0 figure dans le corpus publié : les retirer, ou les téléverser en assumant l'écart |
| C7 | Compression des redondances, optionnelle | 8 100 mots de corps contre environ 5 700 de médiane ; jamais aux dépens des contrôles |

---

## 5. Ce qu'il ne faut pas faire

1. Pas de tableau Markdown (zéro dans le corpus).
2. Pas d'indice unique de pouvoir ou de causalité.
3. Pas de structure en quatre cases de Strange.
4. Ne pas présenter le codage interne comme une fréquence du monde.
5. Ne pas supprimer les contre-exemples ni le taux de base HATVP.
6. Ne pas supprimer le registre numéroté final.
7. Ne pas découper en série : le résultat est transversal.
8. Ne pas transformer l'auto-révision en confession.
9. Ne pas ajouter d'enquête pour remplir une catégorie.

## 6. Ce que le texte perd, et qui doit être accepté

- **La frappe d'une thèse inconditionnelle** et l'effet de découverte.
- **Une partie de la portée politique** : plus facile d'en tirer une accusation systémique, ni un centre coordinateur.
- **Une part du lectorat** qui vient chercher une révélation ou un responsable.

Ce coût est cohérent avec la révision déjà assumée : la coexistence de leviers ne démontre plus une architecture intégrée.

## 7. Ordre d'exécution

| Rang | Opérations | Effort |
|---|---|---|
| 1 | Prérequis (§2) : unité probatoire ; garde-fou (§3) : hétérogénéité de la variable finale | faible |
| 2 | A3 lignée, A1 titre et sous-titre, B3 codage interne | faible |
| 3 | A2 les six formules abaissées | faible |
| 4 | B1 bilan à trois paliers et liste numérotée des relations ouvertes | moyen |
| 5 | B2 contrôles nommés comme tels, B4 quatre coordonnées | moyen |
| 6 | C1 à C5 conformité | moyen |
| 7 | C6 figures, C7 compression | décision de l'auteur |
| 8 | Contrôle terminal, phrase par phrase : chaque proposition générale doit pointer vers une preuve, une borne ou une incertitude nommée | moyen |

## 8. À vérifier avant publication

- Communiqué Vattenfall du 5 mars 2021 et document Internet Society sur New IP : connus par titre, date et extrait concordant, non lus intégralement.
- Sources de presse [58] et [59] : concordance de plusieurs organes seulement, extraction bloquée.
- Manifeste du bundle toujours non re-scellé, cible divergente, comme documenté.

*Zéro em-dash dans ce document.*
