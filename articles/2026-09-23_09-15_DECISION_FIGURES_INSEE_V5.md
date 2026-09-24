# Décision — les figures de la V5 Insee passent de onze à six

Date : 23 septembre 2026. Décision prise sur la question « onze figures, c'est un peu trop ? ».
Appliquée : le corps porte six figures, le générateur n'en produit plus que six, les versions
antérieures sont conservées en archive.

---

## 1. Ce qui était mesuré avant de trancher

| Figure | Mots depuis la précédente | Constat |
|---|---|---|
| FIG. 01 chaîne de transmission | 1 390 | normal, c'est le schéma d'ouverture |
| FIG. 02 quatre nombres | **153** | deux affiches pleine page dans six phrases |
| FIG. 03 marge publiée/circulée | 547 | |
| FIG. 04 manivelle | 940 | |
| FIG. 05 frise des conventions | **0** | collée à la 04 : aucune ligne de texte entre les deux |
| FIG. 06 mort de H6 | 325 | |
| FIG. 07 Metzing | 442 | |
| FIG. 08 révisions | 426 | |
| FIG. 09 six accusations | 795 | |
| FIG. 10 grille des 4 questions | 501 | |
| FIG. 11 clés de révocation | **312** | |

Six figures en 2 700 mots au milieu du corps, aucune dans le dernier tiers. Le défaut n'était
donc pas le nombre mais la distribution : un embouteillage central et une pénurie finale. Une
image tous les 550 mots absorbe le regard au moment où la démonstration demande le plus
d'attention, et banalise les deux figures qui comptent.

## 2. Le critère de coupe

Une figure est gardée si elle porte une **structure** que la prose ne peut pas porter
(une chaîne, un recoupement, quatre directions, un tableau d'ensemble, une grille de lecture).
Elle est coupée si elle **redit un paragraphe** dans une autre mise en page, ou si elle
transforme un récit en affiche.

| # | Avant | Décision | Raison |
|---|---|---|---|
| 01 | chaîne de transmission | **garder** | les 5 étages, et surtout celui qui disparaît |
| 02 | quatre nombres officiels | **garder**, déplacée | la seule idée d'image est le recoupement des 4 mesures ; sa place est après le paragraphe qui traite leur divergence |
| 03 | marge publiée / circulée | **couper** | deux colonnes dont l'une redit l'autre en négatif, plus une bande « nous nous appliquons la règle » : la cuisine interne en image |
| 04 | manivelle | **garder**, fusion avec 05 | les 4 conventions qui tirent dans 4 directions : la découverte du dossier |
| 05 | frise des conventions | **fusionnée dans 03** | les mêmes quatre conventions, sous forme de dates. Chaque vanne porte maintenant son année dans son cartouche ; la chronologie devient l'attribut du mécanisme au lieu d'un second document |
| 06 | mort de H6 | **couper** | trois boîtes de texte pour un chiffre ; la FIG. 05 affiche déjà la ligne H6 « tuée par la publication de l'accusé » |
| 07 | Metzing | **couper** | cinq panneaux pour une commune, sur le seul cas que le texte qualifie de fragile |
| 08 | révisions | **garder**, réduite | la frise 0,9 → 1,4 → 1,6 est déjà trois lignes du texte ; la distinction « biais orienté / erreurs dans les deux sens » est un vrai objet d'image |
| 09 | six accusations | **garder** | le tableau d'ensemble d'une section entière |
| 10 | grille des 4 questions | **garder**, fusion avec 11 | l'outil transférable |
| 11 | clés de révocation | **fusionnée dans 06** | lire un chiffre et accepter d'être révoqué sont le même geste, à deux étages |

Résultat : **01** chaîne, **02** quatre nombres, **03** manivelle datée, **04** deux régimes
d'erreur, **05** six accusations, **06** grille et révocation. Une figure tous les mille mots.

## 3. L'argument venu du contrôleur, pas de l'esthétique

`check_figures_insee.py` signalait six nombres présents dans les figures et absents de
l'article : « moins 2,0 points » (FIG. 02), « + 0,7 point » (FIG. 03), « loi 2005-841 »
(FIG. 04 et 05), « 253 » (FIG. 06). Trois de ces quatre figures sont celles que la coupe
retire : une figure qui affiche des données que l'article n'énonce pas a cessé d'illustrer,
elle est devenue un second document.

Traitement des deux qui restent :

- FIG. 02 écrit désormais « BIT : moins 2 points », comme le texte (« recule de 2 points »).
- FIG. 03 cite la loi du 26 juillet 2005 : la source correspondante a été ajoutée à la
  ligne « Cadre juridique » de la section Sources (`loi n° 2005-841 du 26 juillet 2005,
  article 35, création de l'indice de référence des loyers, applicable en 2006`), ce qui
  énonce dans l'article la base légale que la figure citait seule.

Contrôle après coupe : **tous les contrôles passent**, chiffres alignés, formules conformes,
grammaire conforme, intégration complète (6 figures annoncées, 6 sur disque).

## 4. Ce qui a été modifié

- `tools/engines/visual/gen_figures_insee.py` : six fonctions, noms de fonctions réalignés sur
  les noms de fichiers (l'ancien générateur avait `fig10()` écrivant `fig05_*.svg`, ce qui ne
  se voit qu'au moment de retoucher une figure).
- `articles/2026-09-23_06-00_..._ARTICLE.md` : six appels de figure, la FIG. 02 déplacée après
  le paragraphe de divergence, la ligne juridique de la section Sources complétée.
- `articles/2026-09-23_insee_V5/figures/svg/archive/` : les onze SVG antérieurs, conservés
  comme trace et hors des contrôles.
- `tools/engines/visual/gen_lecture_figures.py` : intro corrigée, plus de partage corps /
  appendice.

## 5. Ce que la coupe laisse ouvert

Le dossier perd trois occasions de montrer ce qu'il raconte : la marge absente des 19 articles,
la mort de l'hypothèse la plus séduisante, et l'écart de recensement d'une commune. Les trois
sont dans le texte, en prose, et deux des trois y sont des passages forts. Si l'une d'elles
s'impose à la relecture finale, la place est libre : trois des six figures actuelles tiennent
en une seule bande de texte et pourraient céder la leur sans que l'article perde une preuve.
