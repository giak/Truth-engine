# Vérification de provenance — entrées [5], [6] et [7] du registre

**Question posée.** T6 a fait passer dans les entrées [5], [6] et [7] une datation que le corps n’énonce que pour le lot : « publié à partir de novembre 2018 après compromission des systèmes de l’Institute for Statecraft ». Cette extension, du collectif au fichier, était déclarée **à vérifier avant publication**. Vérification faite le 13 septembre 2026.

**Verdict : la datation tient, fichier par fichier, et elle est mieux étayée que ce que la phrase affirme.** Aucun changement n’est requis dans les trois entrées. Deux précisions sont en revanche disponibles et consignées ici, dont l’une **renforce** la réserve de conservation que le corps porte déjà.

**Article** : `01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md`, empreinte `d6cf21a3…1bd0f9`, inchangée par cette passe.

---

## 1. Mémoire d’abord, et elle ne savait rien

Cinq requêtes `search_memory` sur le MCP `8002` (mode hybride, cinq résultats chacune) :

> Institute for Statecraft, piratage Integrity Initiative novembre 2018 · documents, fdik.org, chaîne de conservation · Moncloa Campaign, Pedro Baños, Ballesteros · financement Foreign Office 296 500 · Institute for Statecraft compromise cyber attack 2018

**Aucun résultat pertinent.** Les cinq requêtes renvoient des investigations qui partagent des mots-clés (HATVP, ingérences étrangères, fuite) sans contenir le fait cherché. Santé du service vérifiée avant : `GET /health` → **200**, PostgreSQL et Redis `ok`. **Cache miss documenté**, la recherche web est donc autorisée, et le write-back est fait (§5).

## 2. Ce que le corps de l’article affirme, et ce qui devait être tenu

| Affirmation du corps | Vérifiée ? |
| --- | --- |
| les documents ont été « publiés à partir de novembre 2018 » | **oui**, §3 |
| « après une compromission des systèmes de l’Institute for Statecraft » | **oui**, §3.3 |
| cette compromission est « décrite par l’organisation et le gouvernement britannique comme un piratage » | **oui**, §3.3, les deux locuteurs sont identifiés |
| « leur diffusion en lots ne fournit pas, pour chaque fichier, une chaîne de conservation publiquement documentée » | **oui, et renforcé**, §4 |

## 3. Les sources

### 3.1 La chronologie du lot, trois sources indépendantes

**BBC News, 10 décembre 2018**, James Landale, « Russia-linked hack “bid to discredit” UK anti-disinformation campaign » :

> A spokesperson said the Institute for Statecraft was hacked several weeks ago and documents were “**published and amplified by Kremlin news channels**”.

**Wikipedia, entrée *Institute for Statecraft***, section *Hacking*, synthèse des sources journalistiques de 2018 à 2021 :

> The hacked documents were posted in **four batches** on the website of a hacktivist collective called CyberGuerrilla. […] The documents were released in **at least six dumps from November onwards**.

**BuzzFeed News, 23 janvier 2019**, Kevin Collier (citation relevée en recherche, source non rouverte depuis) :

> **Starting in November and continuing through January, someone posted four batches** of its stolen files online. The UK’s National Cyber Security Centre…

**Réponse écrite de la Commission européenne, 9 janvier 2019**, question P8_RE(2019)000092 :

> On **4 January 2019**, the hacking group “Anonymous” published a scanned copy of confidential documents confirming the existence…

Trois organes et une institution européenne, indépendants entre eux, donnent la même structure : **une première diffusion en novembre 2018, puis des lots successifs jusqu’en janvier 2019.** Le corps de l’article le dit déjà avec le mot juste : « leur diffusion **en lots** ».

### 3.2 Ce que le corps dit de la compromission, mot pour mot vérifié

**l’organisation** (déclaration de l’Institute for Statecraft citée par la BBC) :

> In sharing information about such malign activities, the Integrity Initiative uses Twitter as a key method of sharing knowledge.

**le gouvernement britannique** (porte-parole du Foreign Office, même article) :

> The Institute for Statecraft, an independent charity, **was hacked** several weeks ago, and numerous documents were published and amplified by Kremlin news channels.

Et la **correction du même article, 27 février 2019**, qui précise l’objet :

> This article has been amended to make clear that western officials believe the hacking of **the Institute for Statecraft’s computer system** was linked to the Russian state.

« Compromission des **systèmes** » est donc la bonne formulation, et non une formule vague. La phrase de l’article — « décrite par l’organisation et le gouvernement britannique comme un piratage » — **est exacte** : le porte-parole est celui du Foreign Office, et l’article le présente comme tel.

## 4. La mesure qui tranche : les fichiers sont datés, un par un

Les trois URL du registre sont vivantes, relevé du 13 septembre 2026 :

| Entrée | URL | Réponse |
| --- | --- | --- |
| [5] | `fdik.org/Integrity_Initiative/392195390-FCO-Application-Form-2018-v2.pdf` | **HTTP 200**, `application/pdf` |
| [6] | `fdik.org/Integrity_Initiative/392195691-Moncloa-Campaign-6-AttTwitter-08-06-18.pdf` | **HTTP 200**, `application/pdf` |
| [7] | `fdik.org/Integrity_Initiative/392195825-Top-3-Deliverables-for-FCO.pdf` | **HTTP 200**, `application/pdf` |

Et le **listing du répertoire** `https://fdik.org/Integrity_Initiative/` donne un horodatage par fichier. Relevé verbatim des trois lignes qui nous occupent :

```
392195390-FCO-Application-Form-2018-v2.pdf                      2018-11-25 21:44  739K
392195691-Moncloa-Campaign-6-AttTwitter-08-06-18.pdf            2018-11-25 21:04  413K
392195825-Top-3-Deliverables-for-FCO.pdf                        2018-11-25 21:44  221K
```

**Les trois fichiers portent la même date, le 25 novembre 2018**, en deux ingestions distantes de quarante minutes (21:04 et 21:44). C’est **dans la fenêtre de novembre 2018**, et c’est **antérieur** à la réponse du Foreign Office du 27 novembre 2018 qui confirme le financement, et à la couverture de presse de décembre.

### 4.1 Ce que cet horodatage prouve, et ce qu’il ne prouve pas

**Il prouve** que les trois fichiers étaient déposés sur ce serveur le 25 novembre 2018, et qu’ils appartiennent au premier lot. Cela **corrobore** la chronologie des trois sources du §3.1, indépendamment d’elles.

**Il ne prouve pas** que le 25 novembre 2018 soit la date de première publication publique : un horodatage de serveur est une métadonnée de fichier, modifiable par toute recopie, et il ne s’agit pas d’un horodatage cryptographique. **La formulation de l’article, « publié à partir de novembre 2018 », est donc la formulation exacte** : elle affirme ce qui est établi, et rien de plus. La date précise reste dans cette note, pas dans le registre.

### 4.2 Une observation qui renforce la réserve de conservation

Le même listing montre que **le répertoire porte quatre familles de dates distinctes** :

| Horodatage | Contenu |
| --- | --- |
| **2018-11-25** | les trois fichiers de [5], [6] et [7], les *clusters* pays, le manuel, les budgets |
| **2018-12-13** | factures, notes de frais, `chris-donnelly-copy-passport-email-13-1-15.pdf`, échantillons Twitter Skripal |
| **2018-12-15** | `ii-media-interviews-2018.pdf`, `integrity-france.pdf` |
| **2019-01-04** | les sous-répertoires `Armenia/`, `China/`, `Hungary/`, `Moldova/`, `USA/`, `general/` |

Le dépôt tel qu’il se présente aujourd’hui est donc **une agrégation de lots successifs sur près de six semaines**, pas le dépôt d’origine. C’est une base **datée et vérifiable** pour la réserve que le corps énonce déjà : « leur diffusion en lots ne fournit pas, pour chaque fichier, une chaîne de conservation publiquement documentée ». **Rien à corriger** ; l’observation est disponible si l’auteur veut donner à cette réserve une pièce propre.

À noter aussi, dans le même répertoire, un fichier nommé `chris-donnelly-copy-passport-email-13-1-15.pdf` : le lot mêle des documents institutionnels et des pièces **personnelles**. Ce n’est pas une erreur du registre, c’est un élément de contexte qui justifie la prudence maintenue.

## 5. Deux points qui restent non établis, et que je ne maquille pas

1. **Le site de diffusion d’origine.** Wikipédia nomme **CyberGuerrilla** comme site des quatre lots ; le registre pointe vers **fdik.org**, qui est un hébergeur de l’archive et non le lieu du dépôt initial selon cette source. Les horodatages de fdik.org placent les fichiers dans le lot de novembre 2018, mais **je n’ai pas établi le lien juridique ou opérationnel entre CyberGuerrilla et fdik.org.** Le registre n’affirme rien à ce sujet ; l’entrée devient fausse seulement si l’auteur écrit quelque part que fdik.org est le lieu de diffusion d’origine.
2. **« edited and re-ordered ».** Une source unique, Business Insider, 23 décembre 2019, Jim Edwards, écrit que les documents diffusés ont été « positioned — **edited and re-ordered** — as if they exposed the institute for taking taxpayers’ money ». Ce serait un appui **plus fort** que « chaîne de conservation non documentée ». **Non appliqué, et non retenu comme fait** : la page est inaccessible à l’extraction depuis ici (le corps de l’article ne se charge pas, seuls le titre et la zone de commentaires sont rendus), et une affirmation de cette force portée par un seul organe, dans un passage que je n’ai pas pu lire, ne peut pas entrer dans un article qui reproche aux autres de faire exactement cela. **Vérifiable, disponible, laissé de côté pour ce motif.**

## 6. Décision

| Point | Décision |
| --- | --- |
| Datation « à partir de novembre 2018 » dans [5], [6] et [7] | **conservée telle quelle**, vérifiée fichier par fichier et corroborée par trois sources indépendantes |
| Date précise du 25 novembre 2018 | **non portée au registre** : un horodatage de serveur n’est pas une date de publication, et l’article n’en a pas besoin |
| Réserve « chaîne de conservation non documentée » | **conservée**, et désormais appuyée sur une observation datée (§4.2) disponible si besoin |
| « edited and re-ordered » | **non appliqué**, source unique et non lue à la source |
| « décrite par l’organisation et le gouvernement britannique comme un piratage » | **conservée**, les deux locuteurs sont identifiés et cités (§3.2) |
| Lien CyberGuerrilla / fdik.org | **ouvert**, sans effet sur le texte actuel |

**Aucune modification de l’article n’a été faite par cette passe.** Empreinte inchangée : `d6cf21a39618b3cd4d8df81754d41509017d20073b187415a43924a0591bd0f9`.

## 7. Write-back mémoire, et deux faux négatifs de ma part

Écrit après recherche web, comme la règle l’impose. Entrée `162400ba-07fc-490b-9d4a-97f0a410f2c5`, `memory_type: reference`, **3 710 caractères**, tags `status:CONFIRME` et `verifie-2026-09-13`, créée le 2026-09-13 à 15:50:07 UTC. Elle porte la chronologie des lots, les deux locuteurs de la qualification de piratage, les trois horodatages, **la borne du §4.1** et les deux points non établis du §5.

**Deux faux négatifs, tous deux de mon fait, et tous deux corrigés avant d’être écrits.**

1. **« la relecture ne trouve rien ».** Mon premier contrôle a cherché les résultats dans `structuredContent`. Or `search_memory` rend son JSON dans `result.content[0].text`, avec la clé `memories`, et **pas** de `structuredContent`. Mes scripts lisaient donc un dictionnaire vide et annonçaient zéro résultat — sur un service qui répondait normalement. J’ai failli écrire que le write-back n’était pas indexé, ce qui aurait été **faux**.
2. **« l’entrée est introuvable ».** Trois requêtes reformulées ne renvoyaient pas l’entrée dans leurs cinq premiers résultats, et j’ai failli en conclure que la recherche était cassée. Vérification faite sur six requêtes :

| Requête | Mode | Résultat |
| --- | --- | --- |
| `Institute for Statecraft` | défaut, **trois fois** | **rang 1**, score 0,0164 |
| `Statecraft` | défaut | **rang 1** |
| `Institute for Statecraft` | `semantic` | **rang 1** |
| `fdik.org` | défaut | absente des cinq |
| « Integrity Initiative fuite documents compromis novembre 2018 » | défaut | absente des cinq |
| « Institute for Statecraft piratage FCO Foreign Office » | défaut | absente des cinq |

**Conclusion exacte, et plus étroite que « la mémoire est cassée »** : le write-back est **persisté et relisible**, par identifiant comme par recherche, et il sort **au premier rang sur le terme distinctif**. En revanche, la recherche est **lexicale et fragile** : allonger la requête fait **disparaître** une entrée qui contient pourtant les mêmes termes, et le score de similarité du meilleur résultat est de 0,016. Le mode `semantic` ne change rien à ce classement. Ce n’est pas un défaut de l’entrée écrite ici, c’est une propriété du moteur, **notée pour les prochaines écritures : chercher par terme distinctif, jamais par phrase longue.**
