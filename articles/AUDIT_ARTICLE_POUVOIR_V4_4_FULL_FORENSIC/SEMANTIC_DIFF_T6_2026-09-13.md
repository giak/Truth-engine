# SEMANTIC_DIFF — tranche T6, micro : degrés, auto-défense, syntaxe du pouvoir, provenance

**Date** : 13 septembre 2026
**Critiques traitées** : F-09 (« le pouvoir » en position d’agent), F-11 (degrés de certitude non ordonnés), F-13 (auto-défense anticipée), F-14 (statut de provenance absent du registre), F-15 (parenthèses de source en fin de thèse), F-16 (« se lit » employé pour trois objets distincts), F-17 (la pièce [6] ne nomme pas Pedro Baños).
**Article** : `01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md`
**Empreinte avant** : `7833dae408e404ffbee32df8f386f5d999d50149dc93cb13f53b96d20538e456`
**Empreinte après** : `a9db157bd1947989d598038c6d036471682b6399f477d1e8536de16043e29d53`
**Lignes** : 337 → **339**. Deux lignes **insérées** après l’ancienne l. 168 (paragraphe F-11) ; douze lignes **modifiées** sans changer de place : 15, 17, 49, 57, 77, 121, 197, 211, 213, 215, 277, 279. **Aucun repère déplacé avant la l. 168 ; tous les repères à partir de 169 sont décalés de +2.**
**Corps** : 10 149 → **10 248 mots** (+99).
**Sauvegarde avant tranche** : `/tmp/ARTICLE_V4_4_AVANT_T6.md`.

Dernière tranche du plan de forme. Les dix-sept critiques F-01 à F-17 sont closes.

---

## 0. Note d’exécution, à écrire avant le reste

Le script de la tranche n’est pas idempotent : relancé sur un fichier déjà transformé, il s’arrête à la première édition parce que l’ancien texte n’y est plus. **Deux exécutions ont donc été rapportées comme des échecs alors que la première avait abouti.** Le contrôle qui suit n’a pas réappliqué la transformation : il vérifie l’état du fichier contre la sauvegarde `/tmp/ARTICLE_V4_4_AVANT_T6.md`, édition par édition.

Trois conséquences pratiques, pour les tranches futures :

1. Un script de tranche doit **écrire sa propre empreinte de départ** dans la trace, ce que celui-ci ne faisait qu’à l’écran.
2. Le contrôle doit être **séparé** de la transformation, dans un second script qui ne modifie rien. C’est le cas ici : les éditions sont vérifiées par présence du texte neuf **et** absence du texte ancien.
3. La sauvegarde datée est ce qui a permis de trancher entre « appliqué puis relancé » et « jamais appliqué » sans reconstituer l’historique.

---

## 1. F-09 — « le pouvoir » en position d’agent

Le plan listait cinq occurrences (l. 15, 91, 210, 231, 271 en numérotation de diagnostic) et demandait **trois conversions**, en protégeant l’usage définitionnel.

| Repère | Avant | Après |
| --- | --- | --- |
| B 15 | **Le pouvoir apparaît** plus tôt, dans ce qu’un acteur tient et dans ce qu’il en fait | **Ce qui se voit** plus tôt, c’est ce qu’un acteur tient et ce qu’il en fait |
| B 77 | **Le pouvoir devient visible** lorsque ce levier modifie effectivement le prix | **Un acteur qui tient un point de passage devient visible** lorsque son levier modifie effectivement le prix |
| B 217 | **le pouvoir ne se lit pas** d’abord dans une décision finale | **le pouvoir d’un acteur ne se constate pas** d’abord dans une décision finale |

La deuxième reprend mot pour mot la formulation que le plan proposait lui-même. La troisième résout deux critiques d’un coup : le substantif abstrait devient « le pouvoir **d’un acteur** », donc relationnel, et la métaphore de lecture disparaît (F-16).

**Les deux occurrences conservées, et pourquoi.**

- **B 199**, « Le pouvoir ne se réduit donc pas à fermer une option. Il se laisse décrire par ce qu’il en coûte pour la rouvrir. » C’est l’énoncé définitionnel que le plan protège explicitement, et son risque de régression nomme cette phrase : « la phrase l. 210 est une définition, sa forme impersonnelle est correcte ». Conservée telle quelle.
- **B 257**, « Le pouvoir sans commande est moins spectaculaire qu’un centre caché. Il est aussi plus directement vérifiable. » **Cette occurrence n’est protégée par aucune clause du plan.** Je la conserve par décision déclarée : c’est la phrase qui reprend le titre de l’article et qui énonce la thèse dans sa forme nominale, à la fin du bilan. Une conversion produirait « ce qu’un acteur peut établir sans commande est moins spectaculaire qu’un centre caché », qui perd l’écho du titre et n’est pas plus vérifiable. **Arbitrage ouvert** : si l’auteur préfère une neutralisation complète de l’agent, c’est la seule phrase qui reste à convertir, et elle coûte l’écho du titre.

**Contrôle** : « le pouvoir » sujet d’un verbe d’apparition passe de 7 à 5 occurrences dans le corps (mesure : `**Le pouvoir|Le pouvoir ` + verbes). Les deux restantes sont celles nommées ci-dessus. `LOCKED_TERMS` intacts.

## 2. F-11 — les quatre degrés, nommés une fois et ordonnés

Un paragraphe neuf, **B 169**, inséré immédiatement après le paragraphe des comptages internes (B 167) et avant le séparateur de la partie IV :

> Quatre mots suffisent à nommer ces états, et ils gardent ici le même sens d’un bout à l’autre. **Établi** : une pièce datée le porte. **Plausible** : des éléments convergent sans qu’aucune pièce relie les termes. **Non établi** : aucune des pièces réunies ne porte l’affirmation. **Non mesuré** : la question a un sens et le dénominateur manque. « Documenté », « constaté » et « observé » se ramènent au premier ; « fragilisé » décrit un effet intermédiaire établi, sans conclusion sur la décision finale.

Trois exigences du plan sont remplies et une est refusée :

| Exigence | État |
| --- | --- |
| Une phrase de calibrage, à l’endroit des comptages internes et non en ouverture | **remplie** — B 169, deux lignes après les chiffres |
| Quatre mots seulement, le reste s’y ramenant | **remplie** — les deux mots surnuméraires du texte, « documenté » et « fragilisé », sont explicitement ramenés |
| Aucun degré chiffré, aucun score, aucun pourcentage | **remplie** — aucun nombre dans le paragraphe |
| Ordonner « non mesuré » **par rapport à** « non établi » | **refusée comme demande de hiérarchie** — le paragraphe les distingue par leur cause, pas par leur rang : l’un est une absence de pièce, l’autre une absence de dénominateur. Les mettre sur une même échelle reviendrait à fabriquer l’ordre que l’article refuse par ailleurs |

Le paragraphe n’introduit aucune affirmation sur le monde : il ne fait que fixer un usage interne. C’est ce qui rend F-11 compatible avec le refus de la métrique commune.

## 3. F-13 — l’auto-défense, deux occurrences sur quatre

Le plan demandait **deux substitutions démonstratives** et la conservation des deux autres. T4 avait délibérément laissé B 213 et B 215 intactes, parce que la conversion du gabarit F-10 y aurait produit la régression que F-13 interdit.

| Repère | Avant | Après |
| --- | --- | --- |
| B 213 | **Ce n’est pas une faiblesse de l’analyse.** C’est précisément ce que doit produire une enquête lorsque plusieurs mécanismes réels coexistent sans qu’une pièce permette de les fondre en une chaîne unique. | C’est ce que doit produire une enquête lorsque plusieurs mécanismes réels coexistent sans qu’une pièce permette de les fondre en une chaîne unique **: des relations séparées, et ce qui manquerait à chacune.** |
| B 215 | **Ce déplacement n’est pas un moyen d’éviter les qualifications fortes.** Il permet au contraire de les réserver aux mécanismes qui les justifient. | Ce déplacement **sert à réserver** les qualifications fortes aux mécanismes qui les justifient. |

La première ne nie plus une critique : elle **nomme ce que l’enquête produit** et qu’un récit causal ne produit pas — des relations séparées, chacune avec ce qui lui manque. La seconde montre la qualification forte effectivement réservée, sans se défendre de ne pas la réserver ; les cinq exemples qui suivent font la démonstration.

**Conservées, avec le motif du plan** : B 253 (« On pourrait considérer cette frontière comme une frustration. Je la considère désormais comme le résultat principal. »), seule auto-défense datée et adossée à un fait ; et le palier de conclusion B 225 (« N’est établi dans aucun des cas examinés »), qui n’est pas une dénégation mais un résultat.

**Une correction en cours de route, à déclarer.** Ma première formulation ajoutait « des relations séparées, **inégalement prouvées**, et ce qui manquerait à chacune », alors que la phrase précédente se termine déjà par « restent distinctes et **inégalement prouvées** ». La répétition, à deux lignes d’écart, était de moi. Corrigée avant le scellement : « des relations séparées, et ce qui manquait à chacune » — la formule reprend le sous-titre et supprime le doublon.

**Contrôle du risque déclaré par le plan** : aucune borne n’a été retirée sans être remplacée. La première phrase perd sa dénégation et gagne l’énumération de ce que l’enquête livre ; la seconde perd sa dénégation et garde sa démonstration, qui suit immédiatement.

## 4. F-16 — trois métaphores de lecture sur cinq

| Repère | Avant | Après |
| --- | --- | --- |
| B 57 | **Le succès d’un levier se lit** d’abord dans le coût et l’adaptation qu’il impose | **Le succès d’un levier se mesure** d’abord **au** coût et **à** l’adaptation qu’il impose |
| B 199 | ce coût **se lit** sur quatre coordonnées | ce coût **s’apprécie** sur quatre coordonnées |
| B 217 | le pouvoir **ne se lit pas** d’abord dans une décision finale | le pouvoir d’un acteur **ne se constate pas** d’abord dans une décision finale |

Chacun des trois objets — le levier, le coût, le pouvoir — reçoit désormais le verbe qui lui est propre, comme le plan le demandait. Les deux occurrences conservées sont celles où la métaphore est le propos : B 191 (« Le contre-pouvoir ne se lit donc pas seulement dans l’existence d’un droit de veto ; il se lit dans ce qu’il permet effectivement de préserver ») et « Il se laisse décrire », protégé par F-09.

**Contrôle** : « se lit / se laisse / rend lisibles / se constate » passe de **7 à 5** occurrences dans le corps. Le décompte est net et non ambigu : trois formes de lecture ont disparu, une forme de constatation est entrée, et « rend lisibles » (B 199) subsiste parce qu’il vient de la clause de réparation du 13 septembre, pas de T6.

## 5. F-15 — deux phrases, sur la quinzaine que le plan recense

Le plan limite l’opération « aux seules phrases dont le dernier segment porte une thèse » et interdit explicitement l’application en masse. Deux sites ont été retenus.

| Repère | Avant | Après |
| --- | --- | --- |
| B 17 | […] ait déterminé ces choix **(ministère de l’Économie, 5 novembre 2014 ; Assemblée nationale, rapport d’enquête n° 897 ; audition de Patrick Kron ; Department of Justice)**. | […] ait déterminé ces choix** : ni le communiqué du ministère de l’Économie du 5 novembre 2014, ni le rapport d’enquête n° 897 de l’Assemblée nationale, ni l’audition de Patrick Kron, ni les pièces du Department of Justice.** |
| B 49 | elle montre que cette contrainte est assez matérielle pour justifier un dispositif de protection **(Commission européenne, règlement de blocage)**. | elle montre que cette contrainte est assez matérielle pour justifier un dispositif de protection**, le règlement de blocage européen.** |

Les deux portent la dernière proposition d’un paragraphe de thèse : la borne négative qui ferme le fait daté, et l’énoncé qui qualifie la contrainte américaine.

**Ce qui n’a pas été fait, avec motif** : les treize autres sites parenthésés du corps. La charte de sourçage du projet est un actif ; le plan la protège. Deux exceptions de plus auraient produit une cadence irrégulière — quelques phrases en prose, le reste en rapport d’audit — c’est-à-dire le défaut signalé, en pire.

## 6. F-17 — la pièce [6] ne nommait pas Pedro Baños

| | Texte |
| --- | --- |
| Avant | Des documents de l’Integrity Initiative décrivent une mobilisation autour de **la possible nomination de Pedro Baños** et s’attribuent une influence ; **une chronologie indépendante montre que Baños a été envisagé** avant que Miguel Ángel Ballesteros soit finalement choisi |
| Après | Des documents de l’Integrity Initiative décrivent une mobilisation autour d’**une possible nomination** et s’attribuent une influence ; **Pedro Baños, que la presse espagnole désigne comme le candidat visé,** a été envisagé avant que Miguel Ángel Ballesteros soit finalement choisi |

Le corps cesse d’attribuer au document *Moncloa Campaign* une identification qu’il tient de la presse espagnole ; la précision est donnée à la source qui la porte. La liste des sources citées à la fin du paragraphe ne change pas : [8] et [9] y figuraient déjà.

## 7. F-14 — le statut de provenance, porté par le registre

Le registre est le document qu’on ouvre pour vérifier une pièce ; il renvoyait jusqu’ici à une réserve énoncée dans le corps (« à considérer avec les réserves de provenance indiquées dans le texte »). Trois entrées portent désormais le statut en elles-mêmes.

| Entrée | Avant | Après |
| --- | --- | --- |
| **[5]** | document exposé publiquement. | publié à partir de novembre 2018 après compromission des systèmes de l’Institute for Statecraft ; chaîne de conservation non documentée pour ce fichier. |
| **[6]** | document exposé publiquement, à considérer avec les réserves de provenance indiquées dans le texte. | document publié à partir de novembre 2018 après compromission des systèmes de l’Institute for Statecraft ; chaîne de conservation non documentée pour ce fichier. **L’identification du candidat visé est établie par les entrées [8] et [9].** |
| **[7]** | auto-attribution du projet, document exposé publiquement. | auto-attribution du projet, publié à partir de novembre 2018 après compromission des systèmes de l’Institute for Statecraft ; chaîne de conservation non documentée pour ce fichier. |

Le plan nommait deux entrées ; j’en traite trois, parce que **[7] portait exactement le même défaut** : « document exposé publiquement » laissait croire à une publication ordinaire, alors que le corps applique la réserve aux trois documents du même lot. Traiter [7] en laissant les deux autres serait la même incohérence en sens inverse.

**Ce que cette édition fait, et ne fait pas.** « Chaîne de conservation non documentée pour ce fichier » est la transposition exacte de la phrase du corps, qui dit que « leur diffusion en lots ne fournit pas, pour chaque fichier, une chaîne de conservation publiquement documentée ». **En revanche, la datation collective est étendue à des entrées individuelles** : le corps énonce la publication de novembre 2018 pour « ces documents » en bloc, et l’entrée l’affirme désormais fichier par fichier, ce qui appelait un contrôle sur pièce.

**Réserve close le 13 septembre 2026, et la datation tient.** Les trois fichiers ont été retrouvés dans le listing du serveur qui les héberge, avec un horodatage : **25 novembre 2018** pour les trois, l’un à 21:04 et les deux autres à 21:44 (`VERIFICATION_PROVENANCE_II_5_6_7_2026-09-13.md` §4). La chronologie du lot est corroborée par la BBC, par la synthèse de Wikipédia et par une réponse écrite de la Commission européenne : **diffusion en plusieurs lots à partir de novembre 2018**. Conclusion : **la formulation du registre est conservée telle quelle, et l’article n’est pas modifié par cette vérification.** La date précise n’est **pas** portée au registre, parce qu’un horodatage de serveur n’est pas une date de publication. Détail, citations et bornes : `VERIFICATION_PROVENANCE_II_5_6_7_2026-09-13.md`.

## 8. SEMANTIC_DIFF, champ par champ

| Champ | Avant → Après | Effet |
| --- | --- | --- |
| **AGENTIVITÉ** | « le pouvoir » sujet d’un verbe d’apparition : 7 → **5** | Trois des cinq occurrences listées par F-09 portent désormais un acteur, une position ou un levier en position sujet |
| **MÉTAPHORE DE LECTURE** | 7 → **5** occurrences dans le corps | Les trois objets distincts de F-16 reçoivent leur verbe propre |
| **MODALITÉ** | « peut / peuvent » 80 → **80** · « hypothèse » 4 → **4** | Inchangée. Aucun « pouvoir » nouvellement asserté |
| **CAUSALITÉ** | « démontre » 11 → **11** · « réfutation de thèse » (ne prouve, ne démontre, ne suffit, ne tient, ne permet, ne fournit) 31 → **31** | Inchangée. F-13 retire des dénégations **d’auto-défense**, jamais des bornes de preuve |
| **NÉGATION** | `\bpas\b` 109 → **107** · `\bne\b` 88 → **89** · négations simples 57 → **57** | Les deux « pas » retirés sont les deux auto-défenses de B 213 et B 215, qui sont des « n’est pas » — donc hors du gabarit « négation simple », inchangé à 57. Le « ne » ajouté vient du paragraphe F-11 (« aucune des pièces réunies ne porte l’affirmation ») |
| **DEGRÉ DE CERTITUDE** | « non mesuré / pas mesuré » 3 → **3** · « hypothèse » 4 → **4** | Le vocabulaire était déjà présent ; F-11 lui donne un ordre d’usage, pas de nouvelles occurrences |
| **SOURÇAGE** | 2 parenthèses intégrées au corps, 3 entrées de registre enrichies | Aucun numéro de registre ajouté, retiré ni renuméroté |
| **LOCKED_TERMS** | capacité, pouvoir mobilisable, pouvoir exercé, effet observable, décision finale, contre-pouvoir, levier | Aucune collision nouvelle. « Pouvoir » employé comme nom commun à B 15, 77, 199, 217, 257 : jamais comme nom d’un niveau de la série |

## 9. Deltas déclarés

1. **Deux « pas » en moins.** C’est la seule perte de négation de la tranche. Elle est **voulue**, c’est le mécanisme même de F-13 : une auto-défense est une négation. Les deux phrases sont citées au §3, et la substitution démonstrative est à leur place. Aucune négation portant un niveau de preuve n’est retirée.
2. **+2 lignes, décalage de +2 à partir de la l. 169.** La carte D → courant doit être refaite pour tout ce qui suit B 168.
3. **La cinquième occurrence de F-09 reste non convertie** et n’est protégée par aucune clause du plan. Décision déclarée au §1, réversible.
4. **F-11 refuse d’ordonner « non mesuré » au-dessus de « non établi ».** Le plan demandait une hiérarchie ; le paragraphe produit une distinction par la cause. Motif au §2.
5. **F-14 étend à trois entrées une réserve que le plan n’en nommait que deux, et fait passer une datation collective au singulier fichier par fichier.** §7 : **vérifié le 2026-09-13, la datation tient pour les trois pièces** (horodatage du 25 novembre 2018 relevé sur le serveur qui les héberge). Réserve close, aucune modification de l’article.
6. **Correction en cours de route** : la répétition « inégalement prouvées » que ma propre édition F-13 avait créée, corrigée avant scellement. §3.

## 10. Contrôles

| Contrôle | Mesure |
| --- | --- |
| Éditions vérifiées | **13 sur 13**, par présence du texte neuf **et** absence du texte ancien ; plus la micro-correction du §3 |
| Empreinte | `7833dae4…456` → `a9db157bd1947989d598038c6d036471682b6399f477d1e8536de16043e29d53` |
| Lignes | 337 → **339** (+2, insertions F-11) |
| Mots du corps | 10 149 → **10 248** |
| Tiret cadratin / apostrophe ASCII / double espace | **0 / 0 / 0** |
| Guillemets français | **52 / 52** appariés |
| Images, tableaux, puces dans le corps | **0 / 0 / 0** |
| `[n]` dans le corps | **0** |
| Registre | **64** entrées, séquence continue de 1 à 64, aucun doublon de numéro ni d’URL |
| Séparateurs `---` | **7**, inchangés |

## 11. Ce que T6 ne fait pas

- **Aucune relecture des 59 entrées du registre.** T6 modifie le texte de trois entrées ; il ne revérifie pas que les pièces disent ce que les entrées leur font dire. La réserve du contrôle terminal antérieur est inchangée.
- **Aucune relecture de la correction de [33].** La provenance demandée par F-14 portait sur les documents de l’Integrity Initiative ; l’entrée [33], correction d’auteur de *Nature*, n’est pas touchée. Le plan la rangeait pourtant dans F-14 : ce point reste ouvert et n’est pas traité, faute d’être un défaut de provenance au même sens.
- **Aucune correction de l’image de la Figure 1**, toujours hors du corps.
- **Aucune coupe.** Le corps passe de 10 149 à 10 248 mots, contre environ 5 700 de médiane de corpus. La question de la longueur reste entière et n’appartient pas aux tranches.

---

## 12. Ce que la découverte du §2 du suivi impose de corriger

Le contrôle par contenu des repères a produit un écart que je déclare ici plutôt que de le taire : **la table D → A du suivi n’est pas reproductible à partir du fichier enregistré comme D.** `/tmp/ARTICLE_V4_4_AVANT_T1.md`, dont l’empreinte `1cb2f0c1…` est celle que le suivi donne pour D, compte **346 lignes**, alors que la table D → A décrit des plages allant jusqu’à 355 et déclare « 352 à 355 hors document ». Une table recalculée directement sur ce fichier donne **dix-sept segments** au lieu de seize et diffère de la table publiée sur cinq de ses bornes, dont la fin du document.

Deux hypothèses, aucune tranchée : soit la numérotation D du plan n’est pas celle de ce fichier, soit la table publiée est fausse à partir de la l. 220. **La table mesurée, segment par segment, est désormais consignée dans `SUIVI_V4_4_2026-09-13.md` §2, avec ses zones d’incertitude marquées.** La règle du projet reste la seule qui protège : **vérifier une référence par son contenu, jamais par son numéro.**
