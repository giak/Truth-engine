# SEMANTIC_DIFF, tranche T1

Contrôle de non-régression de `protocol/SEMANTIC_DIFF.md`. Ce contrôle est heuristique : il ne constitue pas une preuve formelle d'identité sémantique.

**Article** : `01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md`
**Empreinte avant T1** : `1cb2f0c12b4736f2893d1238fd6effd0eba3d0abdb1f2fccaee28b9711cdff66`
**Empreinte après T1** : `13dd5ef9af2b93ebb9570f9f0d663ca1ddc38910a46a522f5703a195492347ca`
**Ampleur** : 16 lignes modifiées sur 346, aucune ligne ajoutée ni supprimée. Corps 9 669 → 9 739 mots (+70, soit +0,7 %).
**Objet de la tranche** : fixer la série canonique et supprimer la collision du mot « capacité » (F-01, F-04).

---

## 1. Série canonique retenue

`capacité` (position tenue) → `pouvoir mobilisable` (possibilité effective d'activer) → `pouvoir exercé` (activation constatée, avec l'effet observable qui l'accompagne) → `décision finale` (la sortie à expliquer, propre à chaque dossier).
Déclarée à l. 93, la seule série du texte qui soit définie. `contre-pouvoir` = pouvoir de rouvrir une option, situé de l'autre côté de la relation, et non un quatrième niveau.

---

## 2. Passages substantiellement modifiés

### D1, l. 34, légende de la Figure 1

```text
ACTEUR:            non concerné (légende de figure)
ACTION / RELATION: capacité → pouvoir mobilisable → pouvoir exercé ; puis effet observable, contribution causale, qualification
OBJET:             les niveaux de la chaîne causale et les deux opérations terminales
QUANTITÉ:          « 6 objets distincts » devient « trois niveaux » plus « deux étapes à démontrer séparément »
TEMPORALITÉ:       inchangée
MODALITÉ:          « doivent être démontrées séparément » conservé
NÉGATION:          « n'est pas un septième objet » devient « n'est pas un quatrième niveau », même portée
CONDITION:         inchangée
EXCEPTION:         inchangée
CAUSALITÉ:         inchangée
DEGRÉ DE CERTITUDE: inchangé
```

**AVANT** : « Ressource, capacité, action, effet, contribution causale et qualification sont 6 objets distincts ; chaque flèche doit être démontrée séparément. Le contre-pouvoir […] n'est pas un septième objet de cette chaîne : c'est une capacité située de l'autre côté de la relation ».
**APRÈS** : « Capacité, pouvoir mobilisable et pouvoir exercé : les trois niveaux de cette chaîne. La ressource tenue est la matière du premier, l'effet observable ce qui rend le troisième constatable, la contribution causale et la qualification doivent être démontrées séparément. Le contre-pouvoir […] n'est pas un quatrième niveau de cette chaîne : c'est un pouvoir de rouvrir ».
**DIFF** : la série de six quitte son statut de liste pour devenir trois niveaux plus deux opérations terminales ; « capacité » cesse de désigner le contre-pouvoir. La ressource et l'effet conservent leur place, en apposition.
**VERDICT** : `CHANGED_BUT_JUSTIFIED`. Le sens de chaque objet est préservé, leur hiérarchie est explicitée, et la collision est levée.
**Réserve** : le PNG de la Figure 1 représente toujours six objets. **L'image et sa légende divergent depuis T1.** À redessiner ou à retirer avec les trois autres figures.

### D2, l. 38, définition de la relation

```text
ACTEUR:            non concerné
ACTION / RELATION: le lien entre deux niveaux voisins
OBJET:             les trois relais de la chaîne
QUANTITÉ:          trois relais conservés
TEMPORALITÉ:       inchangée
MODALITÉ:          inchangée
NÉGATION:          inchangée
CONDITION:         inchangée
EXCEPTION:         inchangée
CAUSALITÉ:         inchangée
DEGRÉ DE CERTITUDE: inchangé
```

**AVANT** : « entre deux niveaux d'analyse : de la capacité à l'usage, de l'usage à l'effet, de l'effet à la décision ».
**APRÈS** : « entre deux niveaux voisins : de la capacité au pouvoir mobilisable, du pouvoir mobilisable au pouvoir exercé, du pouvoir exercé à la décision finale ».
**DIFF** : « usage » et « effet » employés comme niveaux sont remplacés par les termes de la série. « deux niveaux d'analyse » devient « deux niveaux voisins », ce qui rend la phrase compatible avec ses trois relais.
**VERDICT** : `CHANGED_BUT_JUSTIFIED`. Aucune relation nouvelle, aucun relais ajouté ou supprimé.

### D3, l. 40, la limite de la variable finale

```text
ACTEUR:            l'enquête
ACTION / RELATION: la décision finale n'est pas la même d'un dossier à l'autre
OBJET:             la décision finale et ses six formes
QUANTITÉ:          six formes conservées
TEMPORALITÉ:       inchangée
MODALITÉ:          « aucun score global n'est produit » conservé
NÉGATION:          « n'est pas la même d'un dossier à l'autre » conservé
CONDITION:         inchangée
EXCEPTION:         inchangée
CAUSALITÉ:         inchangée
DEGRÉ DE CERTITUDE: inchangé
```

**AVANT** : « tient à la variable finale […] La sortie à expliquer est une vente […] et la relation finale est définie dossier par dossier ».
**APRÈS** : « tient à la décision finale […] Ce qui reste à expliquer est une vente […] et le lien entre le pouvoir exercé et la décision finale est défini dossier par dossier ».
**DIFF** : deux des quatre noms de la variable sont supprimés ; « relation finale » devient le lien explicite entre le troisième niveau et la décision finale, ce qui renvoie à sa définition de l. 38.
**VERDICT** : `SAFE`.

### D4, l. 93, déclaration de la série de référence (ajout)

```text
ACTEUR:            cet article
ACTION / RELATION: une convention de vocabulaire
OBJET:             les trois termes de la série
QUANTITÉ:          trois
TEMPORALITÉ:       présent, valable pour la suite du texte
MODALITÉ:          « s'y ramène » : convention, pas observation
NÉGATION:          aucune
CONDITION:         aucune
EXCEPTION:         aucune
CAUSALITÉ:         aucune
DEGRÉ DE CERTITUDE: convention déclarée, non un résultat
```

**AVANT** : la phrase s'arrête à « Une position tenue sans usage n'établit rien de plus que l'existence d'une position. »
**APRÈS** : ajout de « Ces trois termes forment la série de référence de cet article : toute autre formulation du même enchaînement s'y ramène. »
**DIFF** : ajout d'une phrase de convention, 21 mots.
**VERDICT** : `CHANGED_BUT_JUSTIFIED`. C'est le rattachement exigé par F-04. Aucune affirmation nouvelle sur le monde : la phrase porte sur le vocabulaire de l'article, non sur un fait.

### D5, l. 196, capacité de réponse du contre-pouvoir

```text
ACTEUR:            l'Union européenne
ACTION / RELATION: créer un pouvoir de réponse
OBJET:             l'instrument anti-coercition
QUANTITÉ:          inchangée
TEMPORALITÉ:       « n'existait pas auparavant sous la même forme » conservé
MODALITÉ:          inchangée
NÉGATION:          « n'existait pas auparavant sous la même forme » conservé
CONDITION:         inchangée
EXCEPTION:         « ne démontrent pas, à eux seuls, leur efficacité future » conservé
CAUSALITÉ:         inchangée
DEGRÉ DE CERTITUDE: inchangé
```

**AVANT** : « une capacité de réponse ». **APRÈS** : « un pouvoir de réponse ».
**DIFF** : un mot, pour que « capacité » ne désigne pas le contre-pouvoir.
**VERDICT** : `SAFE`.

### D6, l. 206, définition du contre-pouvoir (collision principale)

```text
ACTEUR:            un acteur ou une institution
ACTION / RELATION: rouvrir une option
OBJET:             une option qu'un autre avait renchérie, réduite ou rendue moins accessible
QUANTITÉ:          inchangée
TEMPORALITÉ:       inchangée
MODALITÉ:          inchangée
NÉGATION:          inchangée
CONDITION:         inchangée
EXCEPTION:         inchangée
CAUSALITÉ:         inchangée
DEGRÉ DE CERTITUDE: inchangé
```

**AVANT** : « **la capacité d'un acteur ou d'une institution à rouvrir une option** ».
**APRÈS** : « **le pouvoir, pour un acteur ou une institution, de rouvrir une option** ».
**DIFF** : le mot en gras change ; l'agent, l'action et l'objet sont identiques.
**VERDICT** : `CHANGED_BUT_JUSTIFIED`. C'est la collision que F-01 vise : « capacité » désignait ici le contraire de ce qu'il désigne à l. 93. L'agent est conservé explicitement entre virgules.

### D7, l. 210, les quatre coordonnées

```text
ACTEUR:            cet article
ACTION / RELATION: le coût de réouverture se lit sur quatre coordonnées
OBJET:             substitut, délai, coût, recours
QUANTITÉ:          quatre coordonnées conservées
TEMPORALITÉ:       inchangée
MODALITÉ:          inchangée
NÉGATION:          « n'agrège pas » conservé
CONDITION:         inchangée
EXCEPTION:         inchangée
CAUSALITÉ:         inchangée
DEGRÉ DE CERTITUDE: « ne sont pas commensurables » conservé
```

**AVANT** : « Le pouvoir n'est donc pas seulement la capacité de fermer une option […] ce coût se lit sur quatre coordonnées que cette enquête n'agrège pas ».
**APRÈS** : « Le pouvoir ne se réduit donc pas à fermer une option […] ce coût se lit sur quatre coordonnées qui portent toutes sur le troisième niveau et que cette enquête n'agrège pas ».
**DIFF** : « la capacité de fermer » disparaît (c'était l'activation, donc le troisième niveau, appelé « capacité ») ; les quatre coordonnées sont explicitement rattachées au troisième niveau, ce qui est le rattachement exigé par F-04. La négation est conservée sous une autre forme : « n'est pas seulement » devient « ne se réduit pas à ».
**VERDICT** : `CHANGED_BUT_JUSTIFIED`.

### D8, l. 231, la règle de la conclusion

```text
ACTEUR:            non concerné
ACTION / RELATION: le pouvoir se lit dans une capacité puis dans le pouvoir exercé
OBJET:             accès fermé, option renchérie, condition imposée, information rendue visible
QUANTITÉ:          quatre exemples conservés
TEMPORALITÉ:       « lorsqu'il a été observé » conservé
MODALITÉ:          inchangée
NÉGATION:          « ne se lit pas d'abord dans une décision finale » conservé
CONDITION:         inchangée
EXCEPTION:         inchangée
CAUSALITÉ:         inchangée
DEGRÉ DE CERTITUDE: « beaucoup plus faible » conservé
```

**AVANT** : « dans l'exercice d'un levier […] Sur l'effet politique final ».
**APRÈS** : « dans le pouvoir exercé […] Sur le lien à la décision finale ».
**DIFF** : troisième niveau renommé ; « effet politique final » devient le lien à la décision finale, seul nom retenu.
**VERDICT** : `SAFE`. La comparaison de force probante porte sur les mêmes deux niveaux.

### D9, l. 235 à 239, les trois paliers

```text
ACTEUR:            non concerné
ACTION / RELATION: ce qui est établi, ce qui est établi sans la décision finale, ce qui n'est établi dans aucun cas
OBJET:             capacités, positions, droits, actes datés / pouvoir exercé documenté / lien à la décision finale et coordination entre leviers
QUANTITÉ:          trois paliers conservés
TEMPORALITÉ:       inchangée
MODALITÉ:          « sans que la décision finale le soit » conservé
NÉGATION:          « N'est établi dans aucun des cas examinés » conservé mot pour mot
CONDITION:         inchangée
EXCEPTION:         inchangée
CAUSALITÉ:         « le lien entre » conservé
DEGRÉ DE CERTITUDE: inchangé
```

**AVANT** : « les positions et les droits » / « l'exercice d'un levier est documenté et où la sortie politique n'est pas attribuable » / « le lien entre l'exercice d'un levier et la décision politique finale ».
**APRÈS** : « les capacités, c'est-à-dire les positions et les droits tenus » / « le pouvoir exercé est documenté et où le lien à la décision finale n'est pas attribuable » / « le lien entre le pouvoir exercé et la décision finale ».
**DIFF** : trois noms de la variable et deux noms du troisième niveau alignés sur la série. Le premier palier nomme désormais le niveau qu'il décrit au lieu de ses seuls exemples.
**VERDICT** : `SAFE`. Aucun palier déplacé, aucune force probante modifiée.

---

## 3. Passages modifiés par le seul nom de la variable

Alignement sur `décision finale`, sans autre changement. Aucun champ de contrôle modifié (quantité, modalité, négation, condition, exception, causalité, degré de certitude inchangés).

| Localisation | Avant | Après | Verdict |
| --- | --- | --- | --- |
| l. 3, sous-titre | « capacité, usage du levier, effet observable et décision finale » | « capacité, pouvoir mobilisable, pouvoir exercé et décision finale » | `SAFE` |
| l. 15 | « la décision politique finale » | « la décision finale » | `SAFE` |
| l. 27 | « capacité, usage du levier, effet observable et décision finale » | « capacité, pouvoir mobilisable, pouvoir exercé et décision finale » | `SAFE` |
| l. 173 | « attribuer un résultat politique final » | « attribuer la décision finale » | `SAFE` |
| l. 229 | « sans démonstration du résultat politique final » | « sans démonstration du lien à la décision finale » | `SAFE` |

Sur l. 15 et l. 229, le qualificatif « politique » est retiré. Justification : la variable finale est définie à l. 40 par six formes dont une sélection éditoriale et une exposition mesurée, de sorte que « politique » ne discrimine pas ; le retenir aurait maintenu deux noms pour un même emplacement.

---

## 4. Contrôles objectifs

`HARD_GATE` déterministe, avant et après, identique sur les onze items mesurés :

| Contrôle | Avant | Après |
| --- | --- | --- |
| tiret cadratin U+2014 | 0 | 0 |
| tiret demi-cadratin U+2013 | 0 | 0 |
| double espace | 0 | 0 |
| guillemets français ouvrants / fermants | 47 / 47 | 47 / 47 |
| apostrophes ASCII | 0 | 0 |
| renvois `[n]` dans le corps | 0 | 0 |
| entrées de registre `[n]` | 59 | 59 |
| tableaux Markdown | 0 | 0 |
| puces dans le corps | 0 | 0 |
| séparateurs `---` | 7 | 7 |
| figures | 4 | 4 |

Recherche de résidus interdits, après T1 : `variable finale` 0, `sortie politique` 0, `résultat politique` 0, `décision politique finale` 0, `usage du levier` 0, `exercice d'un levier` 0, `six objets` 0, `septième objet` 0.

Emplois de « capacité » restants : 17 occurrences. Trois appartiennent à la série canonique (l. 3, 27, 38, 93 deux fois, 231, 235) et désignent le premier niveau. Les autres sont des emplois courants ou des instances du premier niveau, non des collisions : l. 75 « capacité de riposte », l. 83 « capacité de blocage », l. 91 « Tenir cette position n'est encore qu'une capacité », l. 125 « leur capacité à modifier », l. 133 « capacité de diffusion ou de mobilisation », l. 135 « capacité financée », l. 173 « des capacités », l. 200 « capacité d'action », l. 212 « financement de capacités », l. 227 « capacité juridique ».

---

## 5. Verdict de tranche

Aucune `REGRESSION`. Deux `CHANGED_BUT_JUSTIFIED` structurels (D1, D2) et cinq justifiés par la levée de collision (D4, D6, D7, D9, plus D3) ; le reste `SAFE`. Aucune négation supprimée, aucune modalisation durcie, aucune causalité ajoutée, aucune exception retirée.

**Réserve ouverte, non refermable par cette tranche** : le PNG de la Figure 1 contredit sa légende. À traiter avec la décision sur les quatre figures.
