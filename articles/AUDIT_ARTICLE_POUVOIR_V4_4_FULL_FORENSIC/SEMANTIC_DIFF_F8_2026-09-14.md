# SEMANTIC_DIFF, tranche F8, la mise en forme de publication

Objet : `01_TARGET/ARTICLE_MASTERWORK_SOUVERAINETE_2026.md`, **retenu pour publication** par l’auteur le 14 septembre 2026.
Empreinte avant : `dd8a2f901f54c3ded8556acccbfe52c6b788cedad8dd0e284b69525555d2781a` (état après F7).
Empreinte après : **`6059938242b24e16bfe4c614aa6e7efa3ebe63b39ee8183401be90d7e305a204`**.
Sauvegarde : `/tmp/ARTICLE_MASTERWORK_AVANT_F8.md`.
307 lignes inchangées, 52 267 → **52 941 octets**, 6 293 mots.

Demande : « on travaille sur masterwork, c’est celui que je vais publier. fais la suite ».

**Trois objets, tous des résidus déclarés par les tranches précédentes** : le titre de la partie II et son « otagisation » (F7, §5.1), le bord de cadre de la l. 160 (suivi par F3, F6 et F7), et l’écart typographique ouvert depuis F3. Le choix de publication tranche par lui-même un quatrième point : le masterwork n’est plus un objet à l’état d’hypothèse, il devient le texte à mettre en forme.

---

## 1. Le titre de la partie II : « l’otagisation des actifs »

Le titre portait :

> « ## II. Le verrou du Lawfare : la coercition industrielle et **l’otagisation des actifs** »

Deux défauts, dont le second est le vrai.

1. **Le mot n’existe pas.** « Otagisation » n’apparaît qu’une fois dans tout le dépôt : ce titre. Le mécanisme visé est le contrôle des investissements étrangers, dont l’usage courant est « screening » ou « autorisation préalable ».
2. **Et surtout : aucune sous-section ne documente ce mécanisme.** La partie II ne contient que deux sous-sections, la poursuite pénale extraterritoriale et l’arbitrage d’investissement. Le contrôle des investissements n’y apparaît que **du côté du garde-fou**, sous la forme du veto IEF sur Photonis, cité au §V (l. 213) ; les deux entrées de registre qui documentent le régime lui-même, **[63]** (article R. 151-2 du code monétaire et financier) et **[64]** (décret n° 2026-718), **ne sont jamais citées dans le corps**.

**C’est la même classe de défaut que celui réparé par F7** : un titre qui nomme un instrument sans qu’aucune pièce ne le porte. Deux issues seulement : lui donner une sous-section, ce qui supposerait des pièces que l’article n’a pas ; ou **retirer du titre le nom d’un mécanisme que rien ne documente**. La seconde a été retenue.

**Nouveau titre** :

> « ## II. Le verrou du Lawfare industriel : la coercition juridique sur les actifs »

Il n’invente rien : il reprend le libellé exact du groupe II de l’inventaire F7 (« II. Lawfare industriel ») et la formule déjà employée par la synthèse (« la coercition juridique sur les actifs », l. 194). Le titre, la figure et la synthèse disent désormais la même chose. « Otagisation » : **0 occurrence** dans l’article.

---

## 2. Le bord de cadre de la l. 160

La figure « LA CHAÎNE DE DISTRIBUTION DE LA VÉRITÉ » compte quatorze lignes de contenu ; **treize mesuraient 75 caractères et la quatorzième, la l. 160, en mesurait 74** :

> `│ [Modération algorithmique déléguée aux plateformes privées (Meta/X)]   │`

Le bord droit dépassait d’une colonne vers l’intérieur. C’est le dernier des trois bords de cadre que F2 avait relevés, que F6 avait réduits de deux (dont l’un en touchant la l. 210 de la matrice, désormais remplacée par un tableau par F7). **Corrigé** : la ligne est ramenée à 75.

**Plus aucun bord de cadre divergent dans l’article** : les **24 lignes** des deux cadres larges mesurent 75 (prologue, 10 lignes ; chaîne de distribution, 14 lignes), et les **4 lignes** du schéma New IP mesurent 84.

---

## 3. La conformité typographique, écart ouvert depuis F3

**État avant.** **340 apostrophes ASCII** et 10 typographiques. F3 avait constaté l’écart et avait décidé de ne pas le fermer, au motif qu’un document ne se normalise pas par tranche ; F4, F7 et leurs traces s’y étaient rangées. L’argument tenait tant que le sort du texte n’était pas décidé.

**Ce qui le tranche, et qui n’est pas un goût.** L’autre candidat du même dossier, `ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md`, porte **0 apostrophe ASCII et 725 typographiques**. La convention de la maison, pour un article, est donc typographique : sur ce point précis, **c’était le masterwork qui était l’écart**, non la règle. Un texte destiné à publication ne peut pas partir avec 340 apostrophes droites.

**Après** : **0 apostrophe ASCII, 349 typographiques**, et la ligature rétablie dans « plusieurs centaines de **manœuvres** informationnelles » (1 occurrence, V4.4 écrivant « manœuvre »).

**Trois contrôles de non-régression, parce qu’un remplacement global peut casser ce qu’il ne voit pas.**

1. **Aucune URL ne contenait d’apostrophe**, ni droite ni encodée autrement que par `%27`. Les 70 entrées du registre sont intactes et **aucun lien n’a été altéré** : vérifié par relevé de toutes les occurrences `http` du fichier.
2. **Aucune apostrophe ne servait de balise Markdown** : l’article n’emploie ni guillemets droits ni code en ligne dans le corps.
3. **Les cadres monospace conservent leurs largeurs** : le remplacement est d’un caractère pour un caractère, et les 28 lignes de cadre mesurent la même chose avant et après.

**Une limite déclarée, non traitée.** La typographie française demande une **espace insécable** avant « : ; ? ! », à l’intérieur des guillemets français « », et dans les nombres (57,2 Md€). L’article n’en porte pas. La tranche ne les ajoute pas : le rendu dépend de la plateforme, et cette décision appartient à l’auteur, pas à un audit. Elle est donc nommée ici et laissée ouverte.

---

## 4. Ce que la tranche ne fait pas

1. **Les entrées [63] et [64] restent jamais citées.** La tranche ne les cite pas pour faire baisser un compteur : une entrée ajoutée sans besoin réel dans la phrase serait de la décoration, exactement ce que F5 refusait de faire pour les deux livrables. Le sort du registre, qui compte **29 entrées sur 70 jamais citées**, reste une décision à prendre : les conserver comme documentation de l’enquête, ou les retirer.
2. **Les huit nombres non sourçables** du §6 de la note de vérification ne sont pas traités ici : **F9 les a traités** (`SEMANTIC_DIFF_F9_2026-09-14.md`).
3. **Le titre de l’article garde ses quatre adjectifs** (« judiciaires, financiers, normatifs et d’élites ») pour un contenu plus large : compression antérieure à F7.
4. **Le recouvrement des standards techniques entre les parties I et III** n’est pas traité.
5. **Les espaces insécables** (§3), pour la raison dite.

---

## 5. Contrôles

| Contrôle | Résultat |
|---|---|
| Lignes modifiées | **4 zones** : l. 81 (titre de la partie II), l. 160 (cadre), l. 72 (« manœuvres »), et le remplacement typographique global |
| Lignes ajoutées ou supprimées | **0** (307 avant, 307 après) |
| Empreinte | `dd8a2f90…` → **`6059938242b24e16…`** |
| Octets | 52 267 → **52 941** |
| Apostrophes | ASCII **340 → 0** · typographiques **10 → 349** |
| Ligature | « manoeuvres » **1 → 0** · « manœuvres » **0 → 1** |
| « otagisation » | **1 → 0** |
| Titre de la partie II | aligné sur le groupe II de l’inventaire et sur la l. 194 |
| Bords de cadre divergents | **1 → 0** · cadres larges : **24 lignes à 75** · schéma New IP : **4 lignes à 84** |
| URL altérées | **0** (relevé exhaustif des occurrences `http`) |
| Registre | **70**, numérotation continue |
| Renvois `[n]` du corps sans entrée | **0** |
| Entrées jamais citées | **29**, inchangé |
| Tiret cadratin | **0** |
| Tableaux | **23 lignes**, toutes à **4 colonnes** |

---

## 6. Ce que la tranche coûte, et ce qui reste ouvert

**Ce qu’elle coûte.** Le retrait d’« otagisation » retire au titre de la partie II le seul mot qui évoquait l’usage offensif du contrôle des investissements, et il faut le dire franchement : **ce mot ne correspondait à aucune pièce de l’article**. Ce que la tranche perd est une promesse, pas un contenu. La normalisation typographique, elle, ne coûte rien au texte ; elle rend seulement visibles, dans l’historique des empreintes, une modification mécanique de 349 caractères.

**Ce qui reste ouvert**, dans l’ordre où cela pèse pour une publication :

1. **Les huit nombres non sourçables** du §6 de la note de vérification : c’était le prochain objet probatoire, et **F9 l’a traité**. Ce qui reste ouvert après F9 est dans la trace de cette tranche.
2. **Le registre** : 29 entrées sur 70 jamais citées, dont [63] et [64].
3. **Le recouvrement des standards techniques** entre les parties I et III.
4. **Le titre de l’article** et ses quatre adjectifs.
5. **Les espaces insécables**, décision de rendu.
