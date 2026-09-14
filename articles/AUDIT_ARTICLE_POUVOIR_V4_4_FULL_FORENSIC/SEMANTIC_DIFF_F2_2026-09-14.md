# SEMANTIC_DIFF, tranche F2, résolution de la notation `[N]`

Objet : `01_TARGET/ARTICLE_MASTERWORK_SOUVERAINETE_2026.md`.
Empreinte avant : `6b0b5af69dc652cbdb7e78157915d7bea04fc494191ebd0ac7bd2b32f13ecfb1` (état après F1).
Empreinte après : **`c1165fd10e0f951daab72f1e4f1ee72c9b709e121e7046acf2fa7bcfab8afc82`**.
Sauvegarde : `/tmp/ARTICLE_MASTERWORK_AVANT_F2.md`.

Source de la tranche : `VERIFICATION_MASTERWORK_5_FAITS_2026-09-14.md` §7.2, qui avait **rectifié le diagnostic** sans appliquer le remède.

**Dix lignes modifiées, aucune ajoutée ni supprimée** : 62, 66, 67, 113, 127, 129, 181, 207, 211, 215. 308 lignes avant et après. 5 244 → 5 247 mots.

---

## 1. Le défaut, tel qu’il était

`[N]` portait **deux référentiels différents dans le même document**, et même dans le même tableau.

| Référentiel | Où | Exemple |
|---|---|---|
| Entrée de registre, p. ex. la contribution UIT sur New IP | corps et une partie du tableau de synthèse | « la coalition IETF/ISOC [28] », « Monopole dépêches (60 %+) [29] » |
| Code d’investigation interne | trois cellules du **même** tableau de synthèse | « 9 stations police Fujian **[25]** », « Rédaction norme Big Four **[63]** », « 101 voyages ELNET **[27]** » |

Le lecteur qui suivait `[27]` dans le tableau tombait sur le document UIT, alors que la cellule parlait d’ELNET. Et le corps employait une **troisième** notation pour la même chose : « `INV-046` », « `(INV-062, INV-063)` », « `INV-026/027` ».

Sept codes d’investigation étaient visibles dans un article destiné à des lecteurs qui n’ont pas accès au dossier. La convention d’écriture du dossier l’interdit déjà : « aucun identifiant interne visible dans le corps » (`SUIVI`, §7).

## 2. La règle appliquée

Un seul référentiel reste : **`[N]` désigne et désignera une entrée du registre**. Les investigations sont nommées par leur objet.

Deux cas, et deux traitements seulement :

1. **L’objet de l’investigation est déjà nommé par le texte qui l’entoure** (titre de puce, ou phrase précédente). Le code est alors **supprimé**, sans remplacement : la référence était redondante.
2. **L’objet n’est pas nommé.** Le code est remplacé par une **désignation d’objet**, construite sur l’intitulé de l’investigation tel qu’il figure dans `03_FORENSIC_INDEX/CORPUS_121_AUDIT.csv`.

## 3. Les dix éditions

### Cas 1, code supprimé

| Ligne | Avant | Après |
|---|---|---|
| **62** | « L’investigation sur les infrastructures numériques de contrôle **(INV-046)** démontre » | « L’investigation sur les infrastructures numériques de contrôle démontre » |
| **127** | « Les investigations sur la production de normes et la sous-traitance publique **(INV-062, INV-063)** établissent » | « Les investigations sur la production de normes et la sous-traitance publique établissent » |
| **129** | « L’**investigation INV-063** documente des cas où » | « L’investigation documente des cas où » |
| **181** | « Organisation de diplomatie publique et lobbying **(INV-027)** » et, quatre cellules plus loin, « … la Palestine en sept. 2025 **[27]** » | les deux mentions disparaissent |

La l. 129 mérite un mot : la puce s’intitule « La rédaction des normes européennes par les Big Four », sous une phrase qui annonce « Les investigations sur la production de normes et la sous-traitance publique ». Le code n’ajoutait rien. La l. 181 est le seul cas où **la même ligne portait les deux référentiels à la fois** : le code `(INV-027)` et la citation `[27]`, tous deux visant ELNET, l’un la désignant correctement, l’autre renvoyant au document UIT. Supprimer les deux était la seule issue : il n’existe aucune entrée de registre pour ELNET.

### Cas 2, code remplacé par une désignation d’objet

| Ligne | Intitulé de l’investigation au dossier | Formulation d’arrivée |
|---|---|---|
| **66** | « Émirats arabes unis : influence **clandestine et réputationnelle** en Europe, dont réseaux de renseignement privé lorsque démontrés » | « L’investigation **consacrée à l’influence clandestine et réputationnelle** documente le cas où » |
| **67** | « Israël : influence étatique, diplomatique, industrielle, sécuritaire et informationnelle **en France/UE** » | « L’investigation **consacrée à l’influence israélienne en France** documente » |
| **113** | « Chine : **United Front** et frontière entre diaspora, influence et contrôle politique » | « L’investigation **consacrée au Front uni** documente les révélations de la DGSI » |

### Les trois cellules du tableau de synthèse

| Ligne | Avant | Après |
|---|---|---|
| **207** | « 9 stations police Fujian **[25]** » | « **Neuf relais de police Fujian** » |
| **211** | « Rédaction norme Big Four **[63]** » | « Rédaction norme Big Four » |
| **215** | « 101 voyages ELNET **[27]** » | « 101 voyages ELNET » |

La l. 207 ne perd pas seulement son code : « 9 stations » devient « Neuf relais », pour rester **cohérente avec la correction du fait 3 de F1**, qui a ramené le corps de neuf stations à neuf relais de stations.

## 4. Trois répétitions que ma propre rédaction a introduites, corrigées avant scellement

Le remplacement d’un code par une désignation produit mécaniquement des redites là où le titre voisin nomme déjà l’objet. Trois cas, tous introduits par l’édition du §3, tous corrigés dans le même scellement, selon la même procédure que C1 :

| Ligne | Version intermédiaire | Défaut | Version retenue |
|---|---|---|---|
| **66** | « consacrée à l’influence **émiratie** en Europe … des entités liées au renseignement **émirati** … **en Europe** » | l’adjectif et le nom de région deux fois chacun | « consacrée à l’influence clandestine et réputationnelle » |
| **67** | « à l’influence **israélienne** en France documente … **en France**, liées à un opérateur privé **israélien** » | « en France » et l’adjectif deux fois chacun | « documente des opérations de manipulation de contenu et d’influence numérique, liées à un opérateur privé » |
| **113** | « consacrée au **Front uni chinois** » | le titre de la section est « du **Front Uni chinois** » | « consacrée au Front uni » |

**Une conséquence à déclarer.** À la l. 67, la mention « en France » du second membre a été retirée pour supprimer la redite : le fait que les opérations se déroulent en France n’est donc plus porté que par la première moitié de la phrase. Aucun contenu n’est perdu, mais la phrase a été raccourcie au-delà du strict remplacement du code.

## 5. Contrôles

| Contrôle | Résultat |
|---|---|
| Lignes modifiées | **10**, exactement 62, 66, 67, 113, 127, 129, 181, 207, 211, 215 |
| Lignes ajoutées ou supprimées | **0** (308 avant, 308 après) |
| Codes `INV-` restants dans le fichier | **0** (sept avant) |
| Renvois `[N]` dans le corps **sans entrée de registre** | **0** (trois avant : `[25]`, `[27]`, `[63]`) |
| Encadré de synthèse | huit lignes de bord ramenées à 75 caractères |
| Tiret cadratin | **0** |
| Registre | 64 entrées, inchangé |

**La collision est fermée** : plus un seul `[N]` du corps ne renvoie à autre chose qu’à une entrée du registre, et plus aucun lecteur ne peut suivre un lien qui mène au mauvais document.

## 6. Correction d’un compte que j’avais donné faux

La vérification annonçait **30** entrées de registre jamais citées. **Le compte exact est 29**, et il l’était déjà avant F2.

L’erreur : j’avais ajouté `[27]` à la liste en constatant qu’il servait de code d’investigation dans le tableau, sans vérifier qu’il servait **aussi** de citation légitime, ce qu’il faisait à la l. 132 pour la contribution UIT sur New IP. Seuls `[25]` et `[63]` rejoignent donc la liste : **27 + 2 = 29**.

Les 29 entrées concernées : [1] [2] [4] [5] [6] [7] [8] [9] [14] [15] [16] [17] [19] [20] [21] [22] [23] [25] [26] [43] [45] [46] [47] [48] [60] [61] [62] [63] [64]. Le compte est corrigé dans `VERIFICATION_MASTERWORK_5_FAITS_2026-09-14.md` §7.3, dans `SEMANTIC_DIFF_F1_2026-09-14.md` §4.3 et dans `SUIVI` §6.12.

## 7. Ce que F2 ne ferme pas

1. **Une référence nommée reste une référence invérifiable.** Les six investigations désormais nommées (l. 62, 66, 67, 113, 127, 129) reposent sur des dossiers de recherche **absents du registre** : un lecteur ne peut ni les consulter ni les contrôler. Le remède propre est d’ajouter une entrée de registre par investigation, avec sa ou ses sources primaires ; il n’est pas appliqué ici, faute de sélection de sources dans cette tranche. **Deux affirmations du corps reposent ainsi sur une pièce que le lecteur ne peut pas atteindre** : les infrastructures de contrôle (l. 62) et la rédaction des normes par les Big Four (l. 129).
2. **« 121 investigations instruites » (l. 194)** subsiste. Ce n’est pas un code, c’est un **décompte interne** : il n’entre donc pas dans l’objet de F2, et un lecteur ne peut pas plus le vérifier. À trancher, comme le reste de la phrase.
3. **Deux bords de cadre dérivent d’une colonne**, mesurés après F2 : **l. 160** à **74** caractères dans un encadré à **75** (« chaîne de distribution de la vérité »), et **l. 210** à **76** dans l’encadré à 75 (« matrice de l’asphyxie »). Ni l’une ni l’autre n’est modifiée par F2 : **une tranche ne répare que les lignes qu’elle touche** : c’est la règle appliquée en F1, où la l. 19 a été recalée parce qu’elle était éditée. Ces deux réparations d’un caractère restent disponibles, nommées et mesurées.
