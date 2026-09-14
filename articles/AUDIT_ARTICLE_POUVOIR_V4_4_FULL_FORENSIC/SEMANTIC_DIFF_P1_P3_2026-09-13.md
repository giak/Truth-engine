# SEMANTIC_DIFF, insertions P1 à P3 et résolution de R4

Contrôle de non-régression de `protocol/SEMANTIC_DIFF.md`. Ce contrôle est heuristique : il ne constitue pas une preuve formelle d'identité sémantique.

**Article** : `01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md`
**État de référence** : `13dd5ef9af2b93ebb9570f9f0d663ca1ddc38910a46a522f5703a195492347ca` (après T1)
**Empreinte finale** : `c89be2cd239168b8097bb83fc5541211d8199fd2529ae24b42fe5ac3421d8e82`
**État intermédiaire** : `f6151222ff2dbb372c0df10b26d77ec81d89592fa7c7e159a5b70952632eb1d7` (après P1 à P3, avant résolution de R4)
**Ampleur** : 1 ligne remaniée en six passes (l. 89), 4 lignes ajoutées (deux paragraphes et leurs blancs), 1 blanc terminal retiré. Corps 9 739 → 10 106 mots (+367, soit +3,8 %). Registre 59 → 62 entrées (+138 mots).
**Historique des empreintes** : `38fc21bc…aceb` (première version de la l. 89 : mention erronée « loi n° 2024-850 » et définition du mandant étranger présentée comme exhaustive) → `f6151222…b1d7` (R5 corrigée) → `c89be2cd…8e82` (résolution de R4, voir D4).
**Objet** : porter dans l'article les trois textes de droit vérifiés du bundle, puis résoudre R4 en changeant l'appui juridique de la l. 89. Textes du bundle `PRO_ISRAEL_TRUTH_ENGINE_FORENSIC_BUNDLE_2026-09-13` (propositions P1, P2, P3 de `EVALUATION_APPORT_BUNDLE_PRO_ISRAEL_2026-09-13.md`).

---

## 1. Décalage des numéros de ligne

Les deux paragraphes sont insérés avant l'ancienne l. 155. **Tout numéro de ligne du plan supérieur ou égal à 155 se lit désormais à +4.** Vérifié sur trois repères : l'ancienne l. 155 est la nouvelle l. 159, l'ancienne l. 243 est la nouvelle l. 247, l'ancienne l. 248 est la nouvelle l. 252. Les numéros inférieurs à 155 sont inchangés (l. 42 et l. 153 vérifiées identiques).

Conséquence pour la suite : **T2, T3, T4, T5 et T6 travaillent sur les numéros du plan décalés de +4 dès qu'ils dépassent 154.** Le tableau de suivi du plan est mis à jour pour le dire.

---

## 2. Passages ajoutés ou modifiés

### D1, l. 155, contraste de seuil entre deux régimes voisins (P2)

```text
ACTEUR:            le législateur français, et par métonymie les deux régimes qu'il pose
ACTION / RELATION: comparaison de deux seuils d'exigence probatoire
OBJET:             l'objet de la preuve exigée par chaque texte
QUANTITÉ:          deux régimes, deux seuils : introduits, aucun chiffre
TEMPORALITÉ:       « entré en vigueur en 2025 »
MODALITÉ:          « ne placent pas leur seuil au même endroit », « peut être constituée »
NÉGATION:          ajoutée : « La différence n'est pas de sévérité » (négation de qualification, et non de fait)
CONDITION:         « si bien que »
EXCEPTION:         aucune
CAUSALITÉ:         aucune relation causale n'est posée : la différence est décrite comme un calibrage
DEGRÉ DE CERTITUDE: constat, même degré que le paragraphe 433-2 qui précède
```

**AJOUT** : « Deux régimes voisins du même droit ne placent pourtant pas leur seuil au même endroit. L'article 433-2 du code pénal se contente d'une influence « réelle ou supposée », si bien que l'infraction peut être constituée sur une influence seulement alléguée. Le régime français d'influence étrangère entré en vigueur en 2025 exige davantage : une relation effective, établie par l'ordre, la demande, la direction ou le contrôle d'un mandant étranger. La différence n'est pas de sévérité, elle est de calibrage : l'un punit l'abus d'une influence, l'autre impose une déclaration sur la foi d'une relation qu'il faut d'abord documenter. »
**VERDICT** : `SAFE`. Aucune affirmation préexistante n'est retirée, contredite ou renforcée ; le paragraphe s'ajoute au voisinage de l. 151 et 153 sans modifier leur portée. Il sert F-11 (hiérarchie des degrés) en montrant deux calibrages légaux distincts.
**Réserve R1** : la première phrase répète le contenu de l. 151 (« une influence réelle ou supposée »), et la datation d'entrée en vigueur est reprise au paragraphe suivant. Ce n'est pas une faute, c'est une redondance de 25 mots qui peut se résorber en une passe de micro-édition (voir § 4).

### D2, l. 157, article 18-11 et décret d'application (P1)

```text
ACTEUR:            le législateur et le pouvoir réglementaire français ; HATVP comme opérateur
ACTION / RELATION: description d'un régime déclaratif et de son champ
OBJET:             deux éléments cumulatifs, la chaîne indirecte, une exclusion de champ, l'état du répertoire
QUANTITÉ:          deux éléments, un décret, trois formes d'action, zéro entité enregistrée
TEMPORALITÉ:       « en vigueur depuis le 1er juillet 2025 », « 31 juillet 2025 », « en vigueur depuis le 2 août 2025 », « consulté le 13 septembre 2026 »
MODALITÉ:          descriptif ; la borne finale est explicitement restrictive
NÉGATION:          deux négations : « écarte » l'exclusion générale, et « ne permet aucune inférence »
CONDITION:         le cumul des deux éléments de l'article 18-11
EXCEPTION:         l'exclusion de la commande publique et des stipulations contractuelles, bornée au seul volet « entrée en communication »
CAUSALITÉ:         aucune
DEGRÉ DE CERTITUDE: faits de droit, établis ; le vide du répertoire est circonscrit par sa date de consultation et par une borne
```

**AJOUT** : « L'article 18-11 de la loi du 11 octobre 2013, dans sa rédaction issue de la loi du 25 juillet 2024, en vigueur depuis le 1er juillet 2025, exige deux éléments cumulatifs : une relation qualifiante avec un mandant étranger, l'ordre, la demande, la direction ou le contrôle, et une action destinée à influer sur la décision publique, qu'il s'agisse d'entrer en communication avec une liste définie de responsables publics, de s'adresser au public ou de transférer des fonds sans contrepartie. Le décret du 31 juillet 2025 étend ce régime à l'influence exercée indirectement, « par le biais d'un ou de plusieurs intermédiaires », et écarte de son seul volet « entrée en communication » la participation à une procédure de commande publique ainsi que les échanges prévus par des stipulations contractuelles. Cette exclusion donne sa forme juridique à la distinction entre une relation commerciale et une relation d'influence ; sa portée étroite interdit de la lire comme une exemption générale. Consulté le 13 septembre 2026, le répertoire public du régime n'affichait encore aucune entité enregistrée : un instrument neuf, dont le corpus d'application est vide, ne permet aucune inférence sur son application. »
**VERDICT** : `SAFE`. Le paragraphe est un apport d'institution, sans affaire ni acteur nommé. Il ne touche aucun terme de la série canonique.
**Sources** : [60] (Légifrance, article 18-11), [61] (Légifrance, décret n° 2025-733, article 1), [62] (HATVP, liste des entités d'influence étrangère enregistrées, consultée le 13 septembre 2026). Les trois sont vérifiées sur source primaire dans `EVALUATION_APPORT_BUNDLE_PRO_ISRAEL_2026-09-13.md`.
**Réserve R2** : la phrase « sa portée étroite interdit de la lire comme une exemption générale » est une interprétation de l'auteur, et non la lettre du décret. Elle est prudente et va dans le sens de la méthode, mais elle ajoute à la description un jugement de portée. L'exclusion porte en effet sur le seul volet « entrée en communication ».
**Réserve R3** : « n'affichait encore aucune entité enregistrée » est une constatation négative. Elle est datée, bornée, et cohérente avec ce qui a été observé le 13 septembre 2026, mais elle porte sur un registre susceptible d'être publié le lendemain. La phrase de borne qui suit est donc nécessaire, et elle est présente.

### D3, l. 89, seuil légal du mandant étranger (P3)

```text
ACTEUR:            le droit français, pris comme auteur d'une définition
ACTION / RELATION: une formule écartée, un seuil préféré
OBJET:             la définition du mandant étranger
QUANTITÉ:          un seuil, deux branches : dirigée ou contrôlée, financée pour plus de la moitié
TEMPORALITÉ:       inchangée
MODALITÉ:          « a refusé cette formule pour lui préférer un seuil »
NÉGATION:          « a refusé cette formule » (négation d'adoption, pas de fait)
CONDITION:         inchangée
EXCEPTION:         « directement ou indirectement »
CAUSALITÉ:         inchangée
DEGRÉ DE CERTITUDE: constat de droit
```

**AVANT** : « […] Il ne remplace ni la preuve d'un contrôle effectif ni celle de l'usage politique de ce contrôle. »
**APRÈS** : « […] Il ne remplace ni la preuve d'un contrôle effectif ni celle de l'usage politique de ce contrôle. Le droit français, mis en présence de la même question, a refusé cette formule pour lui préférer un seuil : comptent notamment parmi les mandants étrangers les personnes morales directement ou indirectement dirigées ou contrôlées par une puissance étrangère, ou financées par elle pour plus de moitié (article 18-11 de la loi n° 2013-907 du 11 octobre 2013, créé par la loi n° 2024-850 du 25 juillet 2024). »
**VERDICT** : `CHANGED_BUT_JUSTIFIED`. La négation double du passage est conservée mot pour mot ; la phrase s'ajoute après elle. La critique de « investisseur lié à un État » n'est ni retirée ni durcie.
**Réserve R4, la plus sérieuse** : l'article 18-11 définit le **mandant étranger d'une activité d'influence**, pas l'actionnaire d'un investissement soumis au contrôle des investissements étrangers. La phrase le rattache par « mis en présence de la même question », qui assume l'analogie sans la nommer. Un lecteur juridique peut lire là un glissement d'objet : deux régimes distincts du même droit, traités comme un seul. **Deux corrections possibles, au choix** : soit nommer le décalage d'objet dans la phrase (« dans un autre domaine, celui de l'influence étrangère, le droit français… »), soit déplacer l'appui vers le régime du contrôle des investissements, qui n'est pas cité à ce seuil.

### D3 bis, l. 89, correction de la première version (R5)

**Deux défauts introduits puis corrigés avant consignation, sur la même phrase.**

1. **Référence fausse.** La définition du mandant étranger se trouve à l'**article 18-11, II, 2° de la loi n° 2013-907 du 11 octobre 2013**, créé par la loi n° 2024-850 du 25 juillet 2024. La première version attribuait la définition à la loi de 2024 elle-même. Vérifié sur Légifrance (`LEGIARTI000050052952`, consulté le 13 septembre 2026) : « Création LOI n° 2024-850 du 25 juillet 2024 - art. 1 (V) », et le texte de l'article porte la définition en son II. La mention inline est désormais exacte et le registre [60] la reprenait déjà correctement.
2. **Définition présentée comme exhaustive.** L'article 18-11 range parmi les mandants étrangers trois catégories : les puissances étrangères hors Union européenne, les personnes morales dirigées, contrôlées ou financées à plus de la moitié, et les partis et groupements politiques étrangers. Écrire « est un mandant étranger une personne morale… » énonçait une catégorie comme si elle épuisait la définition. La phrase dit maintenant « comptent notamment parmi les mandants étrangers les personnes morales… », et les accords passent au pluriel.

**VERDICT** : `CHANGED_BUT_JUSTIFIED` sur les deux points. La négation double de la phrase d'origine reste intacte, la critique de « investisseur lié à un État » reste intacte, et la phrase n'ajoute aucune affaire.
**Réserve R5 bis, non corrigée** : l'article 18-11 exclut les États membres de l'Union européenne de la notion de puissance étrangère. L'article ne le dit pas, et n'en a pas besoin pour l'usage qu'il fait du seuil, mais un lecteur qui veut vérifier la définition complète la trouvera plus étroite qu'ici. Ajouter l'exclusion coûterait une proposition subordonnée et changerait le centre de la phrase. À trancher avec R4.

---

### D4, l. 89, résolution de R4 : changer l'appui plutôt que le retirer

**Décision.** La phrase qui portait l'article 18-11 quitte la partie I. Le raisonnement qu'elle servait est conservé, adossé au règlement (UE) 2026/1386, dont l'objet est celui du paragraphe : le filtrage des investissements.

**Critère de la décision.** L'article se donne une règle : chaque proposition générale doit pointer vers une pièce, et la pièce doit porter sur l'objet de la proposition. L'article 18-11 définit le mandant d'une **activité d'influence**. L'insérer dans un paragraphe sur l'**actionnaire d'un investissement** créait un transfert d'objet, c'est-à-dire exactement le défaut que l'article reproche aux autres. Retirer la phrase était la seconde issue ; elle coûtait l'argument sans le remplacer, alors qu'un texte de même objet existe et est déjà au registre ([22]).

```text
ACTEUR:            le cadre européen de filtrage des investissements, pris comme auteur de la règle
ACTION / RELATION: le lien étatique est une relation à établir, non une qualité présumée
OBJET:             le contrôle d'un investisseur par un gouvernement de pays tiers
QUANTITÉ:          un examen, quatre indices d'établissement
TEMPORALITÉ:       inchangée
MODALITÉ:          « énonce, dans ses motifs », « s'établit par examen », « il énumère »
NÉGATION:          ajoutée : « ne présume pas ce lien » (négation d'imputation, pas de fait)
CONDITION:         la détermination du contrôle conditionne la notification, pas l'issue
EXCEPTION:         aucune
CAUSALITÉ:         aucune relation causale n'est posée
DEGRÉ DE CERTITUDE: constat de droit ; la nature de la pièce est nommée (motifs, considérant 30)
```

**AVANT** : « Le droit français, mis en présence de la même question, a refusé cette formule pour lui préférer un seuil : comptent notamment parmi les mandants étrangers les personnes morales directement ou indirectement dirigées ou contrôlées par une puissance étrangère, ou financées par elle pour plus de moitié (article 18-11 de la loi n° 2013-907 du 11 octobre 2013, créé par la loi n° 2024-850 du 25 juillet 2024). »
**APRÈS** : « Le cadre qui organise ce filtrage ne présume pas ce lien : le règlement européen énonce, dans ses motifs, que le contrôle d'un investisseur par un gouvernement de pays tiers, direct ou indirect, s'établit par examen, et il énumère ce qui sert à l'établir : la structure de propriété, le financement public, des montages de gouvernance comme les actions de préférence, ou d'autres dispositifs visant à influencer les décisions de gestion (règlement européen 2026/1386, considérant 30). »
**VERDICT** : `CHANGED_BUT_JUSTIFIED`. La critique de « investisseur lié à un État » et la négation double de la phrase précédente sont intactes ; la phrase change de pièce et gagne une négation.

**Vérification, sur source primaire** (EUR-Lex, 2026-09-13). Deux citations verbatim du règlement (UE) 2026/1386 :

> « Direct or indirect control by a third-country government could be exercised in several ways and could be determined on the basis of, inter alia, ownership structure, government funding, specific governance arrangements such as golden shares, or other features aimed at influencing management decisions. » (considérant 30)
>
> « where a foreign investor or its subsidiary in the Union is directly or indirectly controlled by a third-country government, it is more likely that it could pursue that third country's policy objectives. » (considérant 30)

Chaque élément de la phrase de l'article correspond à un élément du considérant : structure de propriété, financement public, montages de gouvernance, dispositifs visant à influencer les décisions de gestion. Aucun n'est ajouté.

**Pourquoi le considérant et pas un article.** Le règlement est aussi l'ancêtre direct : il **abroge le règlement (UE) 2019/452**, dont l'article 4(2)(a) portait une formulation voisine (« whether the foreign investor is directly or indirectly controlled by the government [...] including through ownership structure or significant funding »). Citer l'article abrogé aurait été plus faible ; citer l'article en vigueur aurait décrit les conditions de **notification**, qui ne disent pas la même chose. Le considérant énonce le raisonnement du législateur, et la phrase dit explicitement qu'elle en vient : « énonce, dans ses motifs ». La pièce ne porte donc pas plus que ce qu'elle est.

**Ce que la décision coûte.** L'article perd l'illustration la plus nette du seuil chiffré : « financée pour plus de moitié ». Ce seuil n'apparaît plus nulle part dans le corps ; il ne subsiste que dans le registre ([60]). C'est une perte réelle de tranchant au profit de l'exactitude d'objet. Si l'on veut retrouver un seuil chiffré sans revenir au transfert d'objet, il faudrait le chercher dans le droit français du filtrage lui-même (seuils de droits de vote, art. R. 151-3 et suivants du code monétaire et financier), ce qui n'est pas vérifié à ce stade.

**Écritures en mémoire** : `7c0b4cbd` (abrogation du 2019/452 par le 2026/1386), `13343151` (considérant 30), `9558ea88` (article 4(2)(a) du texte abrogé).

---

## 3. Contrôles de non-régression

| Contrôle | Avant (après T1) | Après | Verdict |
| --- | --- | --- | --- |
| em-dash U+2014 | 0 | 0 | conforme |
| tiret demi-cadratin U+2013 | 0 | 0 | conforme |
| apostrophe ASCII | 0 | 0 | conforme |
| guillemets « » | 47 / 47 | 51 / 51 | conforme, appariés |
| doubles espaces | 0 | 0 | conforme |
| marqueurs `[n]` dans le corps | 0 | 0 | conforme |
| entrées du registre | 59, séquence continue | 62, séquence continue, aucun numéro ni URL en double | conforme |
| tableaux Markdown dans le corps | 0 | 0 | conforme |
| puces dans le corps | 0 | 0 | conforme |
| séparateurs `---` | 7 | 7 | conforme |
| figures | 4 | 4 | inchangé, écart ouvert connu |
| flèches ASCII | 0 | 0 | conforme |
| occurrences de « pas » (mot entier) | 103 (avant T1) | **108** | **aucun bloc modifié ne perd une négation** |
| durée d'entrée en vigueur, dates | - | 1er juillet 2025, 2 août 2025, 13 septembre 2026, 26 juin 2026 | ajoutées, cohérentes avec [22], [60], [61], [62] |
| série canonique | capacité / pouvoir mobilisable / pouvoir exercé / décision finale | inchangée | conforme |

**Contrôle des négations, méthode.** Le comptage absolu de « pas » passe de 103 (état d'avant T1) à 108. Le contrôle par blocs, sur les 15 blocs modifiés depuis l'état initial, donne 19 occurrences retirées pour 22 réintroduites : **aucun bloc remplacé ne retire plus de négations qu'il n'en remet**. L'écart entre les deux comptages (5 au total, 3 par blocs) vient de l'alignement ligne à ligne, pas d'une négation disparue.

**Aucune causalité ajoutée**, aucun acteur nommé ajouté, aucune affaire importée, aucun degré de certitude relevé. Les insertions portent sur des textes de droit, pas sur des relations entre acteurs.

---

## 4. Ce que je laisse ouvert, avec sa mesure

1. **R1, redondance de 25 mots.** L. 155 reprend « réelle ou supposée », déjà cité à l. 151. Un retrait possible : « L'article 433-2 du code pénal se contente de cette influence-là ». Gain : 6 mots. Effet : nul sur le fond. À faire en micro-édition, pas dans une tranche.
2. **R4, le glissement d'objet de l. 89 : tranché, voir D4.** L'appui juridique change d'objet au lieu de disparaître. **R5 bis devient sans objet** : l'article 18-11 n'est plus cité en partie I, où son object faisait défaut. Sa portée d'exclusion des États membres de l'Union reste absente de la partie III, mais elle n'y est pas nécessaire.
3. **P4 et P5, non appliquées.** Elles restent disponibles telles quelles dans `EVALUATION_APPORT_BUNDLE_PRO_ISRAEL_2026-09-13.md` : une septième condition dans la liste des l. 243 à 248 (objectif documenté avant l'issue), et une phrase à l'ancienne l. 157 (appartenance, identité et relation à un État sont trois objets distincts). Leur support dans l'article ne se confond pas avec celui des trois insertions ci-dessus.

---

## 5. Ce que cette passe ne prouve pas

Le contrôle porte sur la non-régression des phrases **déjà présentes**. Il ne vérifie pas que les textes de loi cités disent ce qu'on leur fait dire : cette vérification a été faite séparément, sur source primaire, et elle est consignée dans le fichier d'évaluation. Il ne vérifie pas non plus la reproductibilité de [62] dans le temps : une constatation négative datée reste une constatation négative datée.
