# SEMANTIC_DIFF, retrait des quatre figures

Date : 13 septembre 2026. Article : `01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md`. Opération : retrait des 4 blocs de figure.

| | |
| --- | --- |
| Empreinte avant | `02fce501c9be9f2fa7a92344f57a7464f8e003cb1f9dab8f8d69c6e27a7de78f` |
| Empreinte après retrait | `21cc596e6e96330a23af936a910fb01e46f3351b5f15142cc832d37a3b516dca` |
| Empreinte après clause de réparation (l. 199) | `a95bea2467029462eb3f71db74e6ebeec583736e02017fc8125de62affebf9b0` |
| Sauvegarde avant | `/tmp/ARTICLE_V4_4_AVANT_SUPPR_FIGURES.md` |
| Lignes | 355 → **335** (−20) |
| Mots du corps | 10 213 → 10 007 après retrait (−206), puis **10 030** après la clause de réparation (+20 de contenu, +23 au compteur avec la ponctuation) |
| Guillemets français | 51 paires → **48 paires** (3 paires vivaient dans la légende de la Figure 2) |
| Images et légendes restantes | 0 et 0 |
| Chemins `figures/png/` dans le texte | 0 |

Chaque figure occupait cinq lignes consécutives : vide, vide, image, vide, légende. La structure de paragraphe a été vérifiée après retrait : aucune ligne vide orpheline, aucun triple saut de ligne, chaque paragraphe précédé d’une seule ligne vide. Les PNG n’ont pas été touchés.

---

## D1. Ce qui a été retiré, verbatim

**Figure 1**, après l’ancienne M 32 :

> `![Figure 1 : Grammaire minimale du pouvoir](figures/png/fig01_grammaire_minimale_pouvoir.png)`
> `*Figure 1. Capacité, pouvoir mobilisable et pouvoir exercé : les trois niveaux de cette chaîne. La ressource tenue est la matière du premier, l’effet observable ce qui rend le troisième constatable, la contribution causale et la qualification doivent être démontrées séparément. Le contre-pouvoir, traité en partie IV, n’est pas un quatrième niveau de cette chaîne : c’est un pouvoir de rouvrir, situé de l’autre côté de la relation, qui mesure ce qu’il en coûte pour rouvrir une option.*`

**Figure 2**, après l’ancienne M 65 :

> `![Figure 2 : Alstom / GE, chaîne causale bornée](figures/png/fig02_alstom_ge_chaine_bornee.png)`
> `*Figure 2. La chaîne documentaire descend loin, mais les relations « pression judiciaire → vente causée », « GE → instrumentalisation du DOJ » et « autorisation → pacte corruptif » restent distinctes et non fermées au même niveau.*`

**Figure 3**, après l’ancienne M 194 :

> `![Figure 3 : Le contre-pouvoir mesure la réversibilité](figures/png/fig03_contre_pouvoir_reversibilite.png)`
> `*Figure 3. L’existence d’un recours ne suffit pas : il faut mesurer si l’option est effectivement rouverte, dans quel délai, à quel coût et avec quel effet.*`

**Figure 4**, après l’ancienne M 221 :

> `![Figure 4 : Ce que les enquêtes ne ferment pas](figures/png/fig04_mur_aretes_ouvertes.png)`
> `*Figure 4. Les arêtes ouvertes ne sont pas des blancs à remplir : elles indiquent exactement quelle relation reste à démontrer et quelle pièce pourrait modifier le verdict.*`

## D2. Une légende n’est pas seulement une image : contrôle de chaque énoncé

Une image ne porte pas de proposition ; une légende en porte. Chaque énoncé de légende a donc été cherché dans le corps, à la numérotation courante.

| Énoncé de légende | Porté par le corps ? | Où |
| --- | --- | --- |
| F1, trois niveaux et effet observable | oui | l. 83, la série canonique |
| F1, contribution causale et qualification démontrées séparément | oui | l. 141 et 143, qualification juridique contre causalité politique |
| F1, définition du contre-pouvoir comme pouvoir de rouvrir | oui | l. 195 |
| **F1, le contre-pouvoir n’est pas un quatrième niveau de la chaîne** | **non, puis oui** | seul porteur : la légende retirée. Clause de réparation appliquée à l. 199 le 13 septembre 2026 : « Le contre-pouvoir qui les rend lisibles n’est pas un niveau de la chaîne : il se situe de l’autre côté de la relation. » |
| F4, titre « Ce que les enquêtes ne ferment pas » | oui | l. 163 à 165, les huit raccourcis et la phrase de réfutabilité |
| F2, les trois relations restent distinctes et non fermées au même niveau | oui | l. 21, l. 57, l. 163 |
| F3, mesurer la réouverture en délai, coût et effet | oui | l. 195, l. 197, l. 199 |
| F4, les relations ouvertes ne sont pas des blancs à remplir | oui | l. 165 (« elle la rend réfutable »), l. 225 (« dossier par dossier »), l. 229 et 230 |

**Un seul énoncé perd son porteur unique.** Il est documenté au §5 de `SUIVI_V4_4_2026-09-13.md`, avec la clause de réparation disponible. **Elle n’a pas été appliquée** : elle touche une zone que T3 et F-04 vont retravailler.

Perte secondaire, lexicale : le terme « arêtes ouvertes », titre de la Figure 4, disparaît du document. Le concept subsiste sous « relations ouvertes » (sous-titre l. 3) et « liens non établis » (l. 163 et 165).

## D3. Aucun renvoi orphelin

Vérifié sur le texte après retrait : **0 occurrence de « figure »**, 0 appel d’image, 0 légende, 0 chemin de fichier résiduel. Aucun « cf. figure », « voir ci-dessus », « voir ci-dessous », « encadré », « graphique », « infographie » dans le corps. Les deux occurrences de « schéma » aux l. 19 et 151 désignent un schéma corruptif, pas un objet visuel.

## D4. Champs `SEMANTIC_DIFF`

| Champ | Effet du retrait |
| --- | --- |
| ACTEUR | aucun. Les légendes ne nommaient aucun acteur nouveau : elles renvoyaient à Alstom, GE, au DOJ, aux cas déjà traités. |
| ACTION / RELATION | aucune relation logique retirée du raisonnement : les sept relations citées par les légendes sont dans le corps (§D2). |
| QUANTITÉ | aucune. Les légendes ne portaient aucun chiffre. |
| TEMPORALITÉ | aucune. |
| MODALITÉ | **réduite d’un cran, volontairement.** Le conditionnel de la légende 4, « quelle pièce pourrait modifier le verdict », disparaît. Le corps porte l’équivalent à l. 165, « Si une pièce nouvelle établissait demain […] », et à l. 229 et 230, à l’infinitif dans une liste de conditions. |
| NÉGATION | **quatre occurrences de « pas » sont parties avec les figures**, et le contrôle phrase par phrase les identifie toutes : « n’est pas un quatrième niveau de cette chaîne » (légende 1, déclaration orpheline du §D2), « ne suffit pas » (légende 3), « Ce que les enquêtes ne ferment pas » (titre de la Figure 4, perdu de vue au premier décompte), « ne sont pas des blancs à remplir » (légende 4, sens repris à l. 165). Décompte brut : 110 avant, 107 après, moins la négation rendue par la clause de réparation à l. 199. Un premier relevé n’en comptait que trois, en oubliant le titre de la Figure 4 : corrigé ici. |
| CONDITION | aucune. |
| EXCEPTION | aucune. |
| CAUSALITÉ | aucune. Les légendes ne posaient aucune relation causale ; elles décrivaient l’état de la preuve. |
| DEGRÉ DE CERTITUDE | aucun changement de degré. Les légendes 2 et 4 résumaient des degrés déjà écrits dans le corps. |

Verdict : **SAFE, une perte déclarée, une perte compensée**. Aucune régression bloquante au sens du protocole. La déclaration orpheline du §D2 a été compensée le jour même par la clause insérée à l. 199, sur décision de l’auteur. Les trois autres négations perdues sont reprises par le corps aux l. 165, 195 et 197. Aucune négation ne reste sans porteur.

## D5. HARD_GATE après retrait

Tiret cadratin U+2014 : 0. Tiret demi-cadratin U+2013 : 0. Apostrophes ASCII : 0. Guillemets français : 48 ouvrants, 48 fermants, équilibrés. Doubles espaces : 0. `[n]` dans le corps : 0. Tableaux dans le corps : 0. Puces dans le corps : 0. Séparateurs : 7, inchangés. Registre : 64 entrées, séquence continue. Triple saut de ligne : absent.
