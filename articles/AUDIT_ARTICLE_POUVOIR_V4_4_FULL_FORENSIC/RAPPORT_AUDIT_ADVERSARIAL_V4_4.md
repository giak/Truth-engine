---
trace_schema: "audit-report/v1"
artifact_type: "adversarial_audit_report"
status: "AUDIT TERMINE. Contient des constats vérifiés et des corrections appliquées."
target: "01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md"
target_sha256_origine: "682c81006e6428e3e9037f319a5f3a2d83711a992b2460cf5efa6e9600176af1"
target_sha256_final: "f03df99fa95e85c44bbf4f59e6aa5b9f847d43fa621d9b5f98c3324e68bd94c5"
editions_appliquees: 41
verdict: "PUBLISHABLE_AFTER_FIXES"
produced: "2026-09-13"
zero_em_dash: true
hors_manifeste: true
---

# Rapport d'audit adversarial : `ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md`

## 0. Objet, périmètre et statut probatoire

**Objet.** Auditer un article de 277 lignes et d'environ 64 000 caractères, dont une bibliographie de 59 entrées, qui soutient une thèse sur le pouvoir exercé sans commandement démontré, à travers une vingtaine de cas (Alstom, BNP Paribas, South Pars 11, Vattenfall, Rockhopper, New IP, EUCS, Integrity Initiative, Farkas, Djebbari, COSCO, Photonis, Lituanie, agences de presse, vérification des faits, algorithmes de plateforme).

**Ce qui a été audité.** La cible seule. Le bundle de 113 dossiers a servi de base de contrôle, jamais de source de vérité.

**Hiérarchie probatoire utilisée dans ce rapport.** Tous les constats ne se valent pas, et ce rapport les distingue explicitement :

| Niveau | Nature | Valeur |
|---|---|---|
| A | Source primaire externe lue ou contrôle machine reproductible (DOJ, CIRDI, Trésor, HATVP, AFP, Transparency International, `sha256sum -c`, `grep`) | Ancre l'audit |
| B | Registres internes du bundle (`INVESTIGATION_REGISTRY_CURRENT.csv`, handoffs, `CLAIM_EVIDENCE_TRACE.csv`) | Cohérence interne, pas preuve |
| C | Artefacts auto-déclaratifs (`00_READ_FIRST/`, `A5_AUDIT_V4_4.md`, `VERIFY_BUNDLE.py`, `MANIFEST.sha256`) | Comptabilité interne, ne valide rien |
| D | Revue externe par le pont ChatGPT | Générateur d'hypothèses, jamais juge |

**Avertissement central sur le niveau D.** Le pont ChatGPT est le **même modèle qui a écrit l'article et le bundle**. Son accord n'est pas une corroboration indépendante. Sa fiabilité s'est révélée **dépendante de l'accès au document** :

- **Fiable quand il avait le document** : il a lu *Le Monde* du 3 mars 2026 (que mon extraction ne pouvait pas atteindre) et corrigé deux de mes inférences, toutes deux fausses.
- **Non fiable quand il raisonnait sans le document** : au rôle 11 de la suite de rôles, il a attribué à l'article un montant « ~12,4 Md€ » qui **n'existe pas dans le texte** (0 occurrence vérifiée). Il a fabriqué un reproche.

Chaque notation du pont a donc été revérifiée séparément. La majorité de ses constats a résisté, cinq n'ont pas résisté, et ce rapport dit lesquels.

**Un avertissement sur moi-même.** Cet audit a produit **onze erreurs de ma part**, dont cinq erreurs introduites dans l'article par mes propres patchs. Elles sont documentées en section 5, avec leur mécanisme commun, parce qu'un rapport d'audit qui ne consigne que les erreurs de sa cible n'est pas un audit.

---

## 1. Verdict

**`PUBLISHABLE_AFTER_FIXES`**

**Avant patch.** Aucune affirmation substantielle n'était fabriquée ; le corpus forensique n'était dépassé nulle part de façon grave ; mais l'article portait une erreur factuelle dure, une violation de charte, deux franchissements de sa propre méthode, une rupture entre sa bibliographie et son corps, et une surexposition rhétorique du cas le plus fragile.

**Après les 19 éditions.** Les points ci-dessus sont traités. Il reste **une décision éditoriale** qui n'appartient pas à l'auditeur (section 11, point 1).

**Ce qui a changé depuis mon verdict initial, et qu'il faut dire.** Mon premier rapport affirmait « aucune affirmation substantielle ne dépasse son statut forensique ». C'était **faux** : trois passages dépassaient. Il affirmait aussi que le défaut le plus grave était la date Rockhopper. C'était **mal hiérarchisé** : le défaut le plus grave était la provenance, que j'avais manquée, et la date Rockhopper n'était qu'un symptôme.

---

## 2. Chaîne d'audit, dans l'ordre où elle a été exécutée

| Étape | Nature | Résultat |
|---|---|---|
| 1 | Passe aveugle sur la cible seule | Verdict provisoire `PUBLISHABLE_AFTER_FIXES` |
| 2 | Lecture des registres du bundle (index, handoffs, trace de claims) | Statuts forensiques établis pour Alstom, Integrity Initiative, ISDS |
| 3 | Vérification web des sources primaires, une par une | 20+ sources vérifiées, 1 erreur factuelle dure trouvée |
| 4 | Ping-pong adversarial avec le pont, 2 passes | 5 findings supplémentaires, dont 1 que j'avais manqué |
| 5 | Suite de 15 rôles (12 par moi, 3 par le pont) | 4 défauts supplémentaires dont 2 durs |
| 6 | 19 éditions appliquées à la cible | Voir section 6 |
| 7 | Deux demandes ciblées au pont (sources bloquées, revue du delta) | 2 de mes inférences infirmées, 3 de mes patchs corrigés |
| 8 | Vérification de la thèse centrale contre le codage du corpus | Asymétrie confirmée quantitativement |

**Pourquoi la passe aveugle d'abord.** Parce que lire le corpus avant de lire l'article revient à auditer la méthode au lieu du texte. L'article est ce qui sera publié ; le corpus n'est qu'un moyen.

---

## 3. Ce que l'article fait mieux que la moyenne, et qui a résisté

Ces points ont été attaqués et n'ont pas cédé. Ils sont listés pour être protégés lors des corrections.

1. **Symétrie de l'absence de preuve, tenue dans les deux sens.** « L'absence de trace ne mesure donc jamais l'absence du phénomène » (appliqué aux opérations clandestines), et symétriquement le refus de « aucune orchestration n'est prouvée, donc il ne s'est rien passé ». La plupart des textes de ce genre n'ont que la première moitié.
2. **Séparation capacité / action / effet tenue de bout en bout.** Aucune occurrence trouvée où un effet est attribué à une simple capacité.
3. **Cinq contre-exemples nommés et coûteux.** New IP (échec du promoteur), Lituanie (pas de concession), Hopium (mobilité autorisée), Vattenfall (politique non renversée), Kroes (rien d'établi). Nommer ses propres contre-cas est rare.
4. **Énoncé des pièces qui inverseraient le verdict.** Le texte liste explicitement ce qui le ferait changer d'avis. C'est la meilleure défense anti-instrumentalisation du document.
5. **Aucune statisticisation du corpus de travail.** L'article ne mentionne jamais ses 113 dossiers, ni ses compteurs, ni ses gates. Le lecteur ne peut pas confondre le corpus avec la preuve.
6. **Exactitude juridique sur neuf régimes distincts, sans erreur dure.** Décret 2014-479, L.151-3 CMF, article 433-2 du code pénal, directive 2026/1021, DSA art. 22, règlement 2026/1386, FCPA, CIRDI, TCE, CJUE C-124/20. Les imprécisions relevées sont de niveau attribution, pas de niveau substance.
7. **Le droit employé pour séparer qualification et causalité.** « Une qualification juridique peut être établie sans que la causalité politique le soit. » C'est la clé de voûte du texte et elle est juridiquement fondée.

---

## 4. Défauts trouvés, classés par dureté

| # | Sévérité | Localisation | Preuve (niveau) | Statut |
|---|---|---|---|---|
| 1 | **HAUTE** | Source [6] promet des « réserves de provenance indiquées dans le texte » ; le corps n'en contenait aucune | Lecture directe du corps et de la bibliographie (A) | **Corrigé**, édition 1 puis 17 |
| 2 | **HAUTE** | « la preuve est **généralement** beaucoup plus faible » (thèse finale), alors que l'article interdit lui-même les généralisations statistiques | Contradiction interne, l. 22 contre l. 199 (A) | **Corrigé**, éditions 5 et 10 |
| 3 | **MOYENNE-HAUTE** | Date Rockhopper : « 30 mai 2025 » | italaw, Jus Mundi, UNCTAD, Kluwer, Dentons, CILJ : **2 juin 2025**, « annulled in its entirety », 2 occurrences | **Corrigé**, édition 2 |
| 4 | **MOYENNE-HAUTE** | Farkas : « suffisent à **établir** un conflit d'intérêts anticipé » | Médiateur : deux constats de mauvaise administration, l'EBA « should have forbidden », restrictions *difficult-to-enforce* (A) | **Corrigé**, éditions 4 puis 13 et 19 |
| 5 | **MOYENNE-HAUTE** | Violation de charte : **4 em-dash (U+2014)** dans les libellés de figures, dans un livrable destiné à publication | `grep -c -P '\x{2014}'` = 4 (A) | **Corrigé**, édition 3 |
| 6 | **MOYENNE** | Baños : « changement d'issue dans la même séquence temporelle » | Registre certifié INV-031 : `Moncloa mobilisation -> exposition/pression observable` = SUPPORTED_BOUNDED ; `Moncloa -> changement causal` = **NOT_ESTABLISHED / CAUSALITY_GAP** (B) | **Corrigé**, édition 7 |
| 7 | **MOYENNE** | Saillance Alstom : le cas le moins fermé ouvrait **et** fermait l'article, et le chapeau juxtaposait autorisation (5 novembre) et plaidoyer (22 décembre) | Omission du protocole du 21 juin 2014 et de l'offre Siemens-MHI ; chronologie vérifiée (A/B) | **Corrigé**, éditions 6 puis 18 |
| 8 | **MOYENNE** | Source [30] attribuée à *Digital Journalism* | DOI `10.1080/17512786.2024.2415541` : préfixe ISSN 1751-2786 = ***Journalism Practice***, Vogler et al., 17 octobre 2024 (A) | **Corrigé**, édition 9 |
| 9 | **MOYENNE** | Source [31] : titre inexistant et « 2 405 **articles** » | Titre réel « Both Judge and Party? Investigating the Political Unbiasedness of Fact-Checkers », *JEEA* 23(6), 2137-2164, 2025 ; l'étude porte sur 2 405 **cas** (A) | **Corrigé**, édition 9 |
| 10 | **BASSE** | « six refus sur les trois années précédentes », après « En 2024 » | Période documentée : **2022-2024** (Dalloz, GIDE, rapport 2025) (A) | **Corrigé**, édition 8 |
| 11 | **BASSE** | Source [49] : la page CIRDI citée n'affiche pas la date invoquée | Contenu rendu en JavaScript ; une table CIRDI afficherait même « 30 mai 2025 », ce qui explique l'origine de l'erreur (A/D) | **Corrigé** (date), source inchangée |
| 12 | **BASSE** | Source [36] : URL passant par un segment de langue irlandaise | `/ga/recommendation/en/127638` ; les deux variantes répondent 200 mais servent une application JavaScript (A) | **Corrigé**, édition 14 |
| 13 | **BASSE** | Trois chaînes en flèches ASCII `->` dans le corps | Artefact de dossier forensique dans un livrable de presse (A) | **Corrigé**, éditions 11 et 12 |
| 14 | **BASSE** | Paragraphe Hugh Bailey : date conflatée, et **aucun dossier `INV-###`** dans le corpus | « Hugh », « Bailey », « GE France », « porte tournante », « revolving » : **0 occurrence** hors du dossier de collaboration (A, machine) | Sourcing **corrigé** (éditions 15 et 16) ; traçabilité interne **ouverte** |
| 15 | **BASSE** | Asymétrie de provenance non assumée : communiqués du DOJ traités sans réserve, documents fuités signalés | Choix défendable, mais non énoncé (A) | Non corrigé, signalé |

**Ce qui n'a pas été trouvé, et qu'il faut dire aussi.** Aucune fabrication de source. Aucune citation attribuée à un document qui ne la contient pas (au sens de l'appariement, pas de la date). Aucune erreur d'arithmétique interne. Aucune extrapolation proportionnelle. Aucun chiffre du bundle exporté dans l'article. Aucune section redondante.

---

## 5. Mes propres erreurs, et le mécanisme commun

Cette section existe parce qu'un audit qui ne consigne pas les erreurs de son auteur n'est pas vérifiable. Onze erreurs, en deux familles.

### 5.1 Erreurs de mon audit initial (cinq)

| # | Ce que j'ai affirmé | Correction |
|---|---|---|
| E1 | « Aucune affirmation substantielle ne dépasse son statut forensique » | **Faux.** Trois passages dépassaient : Farkas, Baños, « généralement » |
| E2 | Le défaut le plus grave était la date Rockhopper | **Mal hiérarchisé.** Le plus grave était la rupture de provenance, que j'ai manquée |
| E3 | Les « six refus » étaient non vérifiés | **En réalité vérifiés** : période 2022-2024 |
| E4 | Le biais de saillance Alstom n'était pas relevé | Ajouté après le ping-pong |
| E5 | Faux positif `INV-031` : je l'ai lu en `HOLD`, donc incohérent avec une claim `RESOLVED` | **Faux positif.** Le token `HOLD` venait d'un snapshot antérieur (`CONTROL_STATE.pre_inv053_baseline_repair.json`) ; le registre courant porte `CLOSED` |

### 5.2 Erreurs introduites dans l'article par mes propres patchs (cinq)

| # | Édition | Ce que j'ai fait de mal | Correction |
|---|---|---|---|
| E6 | 4 | J'ai **dégradé** une phrase exacte : « établir un conflit d'intérêts anticipé » ramené à « risque », en me fiant au pont au lieu de lire la source. La lecture directe montre un constat **plus fort** que le texte d'origine | Édition 13 |
| E7 | 1 | Réserve de provenance **factuellement fausse** : « diffusés hors de tout dispositif d'archivage », alors que je cite moi-même une adresse qui les archive | Édition 17 |
| E8 | 6 | Ma clause « qui précède d'ailleurs le plaidoyer de culpabilité » **déplaçait l'implicature causale** au lieu de la retirer : la date du plaidoyer n'est pas le début de l'exposition du DOJ | Édition 18 |
| E9 | 15 | **Régression sur Hugh Bailey** : j'ai retiré la source [57] en inférant de mon échec d'accès qu'elle ne mentionnait pas Bailey, alors qu'elle le mentionne, et j'ai inventé une opposition « GE, et non GE France » que la dépêche AFP ne soutient pas | Édition 16 |
| E10 | 15 | J'ai ajouté *Libération* comme source **sans avoir pu la lire**, alors que j'avais sous la main une dépêche AFP lue intégralement et plus complète | Édition 16 |

### 5.3 Le mécanisme commun, nommé

Huit de ces onze erreurs procèdent du même raisonnement fautif : **confondre mon échec de vérification avec une absence de fait.**

- [57] était bloqué par un anti-robot, donc j'ai conclu qu'il ne mentionnait pas Bailey. En réalité il le mentionne.
- La page du Médiateur n'était pas rendue par mon extracteur, donc le pont a conclu que la source ne parlait que de « risques ». En réalité elle établit une mauvaise administration et une interdiction qui s'imposait.
- Les « six refus » ne figuraient pas dans le communiqué du Trésor, donc je les ai marqués non vérifiés. En réalité ils sont dans le rapport.

Ce mécanisme est exactement celui que l'article dénonce chez ses acteurs : **traiter un point d'observation comme une frontière du monde**. La seule parade que j'aie trouvée est d'écrire, pour chaque constat négatif, **contre quel périmètre il est négatif** : « aucune pièce publique **identifiée** », « dans les sources **consultables depuis ce poste** ».

---

## 6. Journal des 19 éditions

| # | Localisation | Objet |
|---|---|---|
| 1 | l. 109 | Ajout d'une réserve de provenance pour les documents [5]-[7] |
| 2 | l. 153, [49] | « 30 mai 2025 » devient « 2 juin 2025 » |
| 3 | l. 18, 45, 160, 187 | 4 em-dash remplacés par des deux-points (virgule pour la Figure 2) |
| 4 | l. 111 | « établir un conflit » devient « caractériser un risque » (corrigé ensuite par l'édition 13) |
| 5 | l. 199 | « généralement » devient « dans les cas examinés ici » |
| 6 | l. 5 | Ajout de la borne du 21 juin 2014 (réécrite par l'édition 18) |
| 7 | l. 109 | « changement d'issue » devient « décision intervenue » |
| 8 | l. 65 | « les trois années précédentes » devient « la période 2022-2024 » |
| 9 | l. 91, [30], [31] | « 2 405 cas » ; *Journalism Practice* ; titre exact de Louis-Sidois |
| 10 | l. 3 | Suppression de « généralement » |
| 11 | l. 40 | Chaîne en flèches convertie en prose |
| 12 | l. 131 | Idem |
| 13 | l. 111 | Constat réel du Médiateur (deux mauvaises administrations, interdiction qui s'imposait) |
| 14 | l. 254, [36] | URL basculée sur `/en/` |
| 15 | l. 133, sources | Hugh Bailey : première tentative (partiellement erronée, voir édition 16) |
| 16 | l. 133, [58] | Correction de l'édition 15 : [57] restaurée, plage 2013-2016, intitulé exact, source AFP |
| 17 | l. 109 | Réserve de provenance corrigée (plus d'affirmation d'absence d'archivage) |
| 18 | l. 5 | Clause du plaidoyer supprimée, « cadre arrêté » ramené à « principes arrêtés » |
| 19 | l. 111 | « difficiles à faire respecter » (mot de la source : *difficult-to-enforce*) |

Détail complet, avec avant/après et chaîne des empreintes : `07_COLLAB_CHATGPT/2026-09-13_patch_log_editions.md`.

---

## 7. Vérifications reproductibles

Toutes les commandes ci-dessous sont réexécutables depuis la racine du bundle.

```
grep -c -P '\x{2014}' 01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md      -> 0   (4 avant patch)
grep -c -- "->"        01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md      -> 0
grep -c "généralement" 01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md      -> 0
grep -c "30 mai 2025"  01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md      -> 0
grep -c "2 juin 2025"  01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md      -> 2
grep -c "^- \*\*\["    01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md      -> 59
sha256sum              01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md      -> a84191e1...
sha256sum -c MANIFEST.sha256                                              -> 3539 entrées, 1 FAILED (la cible)
```

**Contrôle de la traçabilité du paragraphe Hugh Bailey :**

```
grep -ri "Hugh\|Bailey\|GE France\|porte tournante\|revolving" . (hors 07_COLLAB_CHATGPT)  -> 0 fichier
```

---

## 8. La thèse centrale testée contre le corpus

L'article affirme une asymétrie : « sur l'effet politique final, la preuve est, dans les cas examinés ici, beaucoup plus faible que sur ces leviers situés en amont ». Un auditeur doit tester cette affirmation, pas la trouver plausible.

Sur `03_FORENSIC_INDEX/CLAIM_EVIDENCE_TRACE.csv`, **445 affirmations codées** :

| Dimension | Valeur | Part |
|---|---|---|
| `causal_signal = NO` | **357** | 80,2 % |
| `causal_signal = YES` | 88 | 19,8 % |
| `quantitative_signal = YES` | 394 | 88,5 % |
| `evidence_level = E2` | **386** | 86,7 % |
| `evidence_level = E3` | 32 | 7,2 % |
| `evidence_level = E1` | 16 | 3,6 % |
| `evidence_level = E0` | 11 | 2,5 % |

Croisement : NO|E2 = 311, YES|E2 = 75, NO|E3 = 26, NO|E1 = 11, YES|E3 = 6.

**Lecture.** Plus de quatre affirmations sur cinq ne portent aucun signal causal, et près de neuf sur dix se situent au niveau descriptif. L'asymétrie affirmée par l'article est donc **cohérente avec le codage interne de son corpus**.

**Réserve, et elle est importante.** Il s'agit d'une **métrique auto-déclarée par le bundle**. Elle démontre la cohérence interne de l'article avec sa propre base, pas la validité de cette base. Un codage qui classerait tout en E2 produirait le même résultat. Ce contrôle ferme donc la question « l'article trahit-il son corpus ? », pas la question « le corpus a-t-il raison ? ».

---

## 9. La revue externe : ce qui a été retenu, écarté, et pourquoi

### Retenu, après vérification indépendante

1. ***Le Monde* du 3 mars 2026 mentionne Hugh Bailey** et signale une **autre information judiciaire du parquet de Paris**, distincte de celle portant sur la cession. Vérifié par recherche ciblée sur lemonde.fr. Conséquence : mon retrait de [57] était infondé.
2. **La dépêche AFP du 11 avril 2019** établit : intégration du groupe GE en **novembre 2017** comme directeur des affaires publiques de GE France, nomination comme directeur général **à compter du 22 avril 2019**, fonctions de conseiller sur les affaires industrielles et le financement à l'export au cabinet du ministre de l'Économie **de 2013 à 2016**. Vérifié : dépêche lue intégralement.
3. **Ma réserve de provenance était fausse** : les documents ont été archivés et reproduits, y compris à l'adresse que je cite. Le vrai défaut est l'absence de chaîne de conservation documentée fichier par fichier. Retenu, édition 17.
4. **Ma clause Alstom déplaçait l'implicature causale.** Retenu, édition 18.
5. **« difficiles à appliquer » n'est pas le mot de la source**, qui écrit *difficult-to-enforce*. Retenu, édition 19.

### Écarté, faute de vérification

1. Le pont soutient que le texte du Médiateur insiste sur des restrictions « impossibles à contrôler effectivement ». Mon seul accès vérifié (Transparency International EU, 11 mai 2020, lu intégralement) écrit *difficult-to-enforce*, et le site du Médiateur n'est pas rendu par mon extracteur. **Formulation la plus proche de la source réellement lue conservée.**
2. Le pont signale qu'une table du CIRDI affiche encore « 30 mai 2025 » pour Rockhopper. **Explication plausible de l'origine de l'erreur**, et raison supplémentaire de citer la date du document de décision plutôt que celle d'une table de base de données. Pas une raison de conserver la date fausse.
3. Le pont a marqué [30] et [31] « non vérifié ». **Je les ai vérifiées séparément** : voir section 4, lignes 8 et 9.

### Le constat qui compte le plus sur la nature du pont

Le pont a été **exact quand il avait le document** et **faux quand il raisonnait sans lui**. Cela signifie qu'il doit être utilisé comme **un accès au web**, pas comme un évaluateur. La tentative de l'employer comme relecteur épistémologique (rôles 1, 5, 8, 10 de la suite) a produit des remarques utiles, mais aucune ne pouvait être adoptée sans revérification. Sa concession quasi totale en deuxième passe affaiblit d'ailleurs la valeur probante de tout l'échange : un contradicteur qui cède sur presque tout ne contredit pas.

**Contexte à ne pas oublier** : dans la même session, il a été incapable de me fournir un contexte neuf. Le bundle a été produit par ce modèle, l'article aussi, et mon audit par moi. **Aucune des trois instances n'était indépendante des deux autres.** C'est la limite structurelle de tout cet exercice.

---

## 10. Ce que cet audit n'établit pas

1. **La validité des 113 dossiers du bundle.** J'ai contrôlé la cohérence entre l'article et les registres, et la cohérence des registres avec eux-mêmes. Un registre n'est pas une preuve.
2. **L'authenticité du contenu des documents `fdik.org`.** Je ne les ai pas authentifiés. C'est précisément pourquoi la provenance doit être signalée, et non pourquoi je peux la trancher.
3. **Le contenu exact du texte du Médiateur** mot pour mot. Le site ne se rend pas. Je m'appuie sur une source secondaire lue intégralement et sur le titre du communiqué.
4. **Le contenu intégral de *Libération*, *Le Monde* et *Le Figaro*.** Ces sites bloquent l'extraction (403 et anti-robot). Ma vérification du fait de carrière de Hugh Bailey est une **concordance de plusieurs organes indépendants** au niveau du titre, de la date et d'un extrait cité, plus **une dépêche AFP lue intégralement**. Ce n'est pas une lecture intégrale de la presse.
5. **Le statut du paragraphe Hugh Bailey au regard du droit de la presse.** Je signale qu'il est la seule affirmation nominative de l'article sans dossier forensique interne. Je ne me prononce pas sur sa solidité juridique.
6. **Aucun contexte neuf.** Voir section 9, dernière remarque.

---

## 11. Ce qui reste ouvert

**Section mise à jour le 2026-09-13** après la deuxième vague d'éditions (section 15).

1. **DÉCISION ÉDITORIALE, à toi.** Le dossier d'investigation manquant a été **créé** : `05_ALSTOM/INVESTIGATION_REVOLVING_DOOR_BAILEY_2026-09-13.md`, statut déclaré `AUDITOR_ADDED_NON_CERTIFIE`. Il rend le paragraphe traçable et il établit la chronologie de carrière. Mais un dossier produit **après** l'audit, par l'auditeur, sans gate, n'est pas un dossier certifié : son admission au corpus et son éventuelle certification restent une décision de l'auteur. Je ne peux pas m'auto-certifier sur le point même que j'ai signalé.

2. **ÉLÉMENT NON INTÉGRÉ, à ta main.** *Le Monde* du 3 mars 2026, que l'article cite déjà, indique que Hugh Bailey fait l'objet d'une **information judiciaire distincte** de celle portant sur la cession, avec Anticor comme partie civile. L'article ne le mentionne pas. Ce n'est pas un défaut de sourçage, c'est un choix de périmètre. Je ne l'ai pas ajouté de ma propre autorité : c'est une allégation visant une personne nommée.

3. **TRAITÉ (édition 28).** L'asymétrie de provenance est désormais énoncée dans le texte : les règlements négociés avec le Department of Justice sont présentés comme des récits de partie.

4. **MANIFESTE NON RE-SCELLÉ**, volontairement. Voir section 12.

---

## 12. Intégrité, empreintes et carte des artefacts

### Empreintes de la cible

| État | SHA-256 |
|---|---|
| Origine (inscrite au manifeste, **jamais modifiée**) | `682c81006e6428e3e9037f319a5f3a2d83711a992b2460cf5efa6e9600176af1` |
| Après éditions 1 à 9 | `2dac05499a5067e2b532bbdbcaa0ed5ddb5fedd5955dde8895698fd4df7c374a` |
| Après édition 10 | `481f8a3863fdec33d4bffc74d3acdb7e70968fa2a20f91fe5efcc864d7fa962a` |
| Après éditions 11 à 15 | `d968c3bf3812bf0ede709de96516f9b0d73c5c20ee46e36fe158e14ce05f3e78` |
| Après édition 16 | `380bc4c26f1f16b5315e8e9534f1ede85d45d026bb1a5014c3b6e28f6c4f45b1` |
| Après 19 éditions | `a84191e10fd4689184703782b1daf5581633236ead33f1300b8f9fb8ef463ca9` |
| Après éditions 20 à 28 | `e51d48d1af28a702f99b9d7c9e22ce91250de2a9f19c340312e88794ef6a14da` |
| Après 35 éditions (lot 2 Substack inclus) | `ad93ec8cbd3efc1f1dc87f9154751642b60ab9733609289e21710816c1a32eef` |
| Après édition 36 (les trois niveaux de pouvoir) | `b2fb63ed658292f741875ed283dffbc02edc4b94e0ce0f4b63d0bf9cd6caf09a` |
| Après édition 37 (conclusion alignée sur les trois niveaux) | `9867921ae1c51b92a1cc1718ecb752f91f3f9dd5d5d708ae6b9ffea4316453ac` |
| Final des éditions de fond (38 à 41, borne des archives et contrôle de cohérence) | `f03df99fa95e85c44bbf4f59e6aa5b9f847d43fa621d9b5f98c3324e68bd94c5` |
| Après éditions 42 à 55 (application du plan de corrections) | `c2497885a982e7ae0ac58521825df707148d3dbebf804e2311577b0543e252af` |
| **Courant (après éditions 56 à 63, contrôle terminal phrase par phrase)** | **`1cb2f0c12b4736f2893d1238fd6effd0eba3d0abdb1f2fccaee28b9711cdff66`** |

### État du manifeste

`sha256sum -c MANIFEST.sha256` : **3539 entrées, 1 seule non conforme**, et c'est la cible :

```
01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
```

**Je n'ai pas re-scellé le manifeste, et c'est délibéré.** Réécrire un manifeste d'intégrité sans instruction détruirait sa valeur de preuve d'altération : le bundle a été modifié après scellement, et un vérificateur doit le signaler, pas l'ignorer. La ligne de remplacement exacte est fournie dans le journal de patch, prête à être substituée sur décision.

Aucune cascade : l'empreinte d'origine n'apparaissait qu'à deux endroits (la ligne du manifeste, et le rapport de la suite de rôles qui la conserve comme référence de l'état **audité**). `00_READ_FIRST/BUNDLE_METADATA.json` cite le nom du fichier mais pas son empreinte, et le manifeste n'est lui-même haché par aucun autre artefact.

### Carte des artefacts produits

Tous dans `07_COLLAB_CHATGPT/`, **hors du périmètre du manifeste** (0 occurrence de `07_COLLAB` dans `MANIFEST.sha256`), donc sans effet sur l'intégrité revendiquée.

| Fichier | Contenu | Statut |
|---|---|---|
| `2026-09-13_role_suite_15.md` | Suite de 15 rôles, angle par angle, avec preuves | Audit principal |
| `2026-09-13_patch_log_editions.md` | Journal des 55 éditions, avant/après, chaîne des empreintes, limites de preuve | Source unique de vérité sur les empreintes |
| `PLAN_CORRECTIONS_V4_4_2026-09-13.md` | Plan consolidé v2, issu de la confrontation de deux diagnostics | Plan, non probatoire |
| `2026-09-13_CONTROLE_TERMINAL.md` | Contrôle terminal phrase par phrase : 62 propositions générales, garantie de chacune, 8 défauts corrigés | Contrôle de portée |
| `NOTE_FOND_2026-09-13.md` | Note de fond, trois questions d'auteur | Note, non probatoire |
| `2026-09-13_redteam_chatgpt_2passes.md` | Deux passes de red-team par le pont | Non probatoire |
| `2026-09-13-0556-role2_factchecker.md` | Rôle 2, vérification ligne à ligne par le pont | Non probatoire |
| `2026-09-13-0559-roles4_11_juriste_historien.md` | Rôles 4 et 11 par le pont | Non probatoire |
| `2026-09-13-0611-ask1_bailey_sources.md` | Demande 1 : sources de presse bloquées | Non probatoire, constats revérifiés |
| `2026-09-13-0613-ask2_revue_delta.md` | Demande 2 : revue adversariale du delta | Non probatoire, constats revérifiés |
| `delta_editions.md` | Delta transmis au pont, sans l'article | Pièce de méthode |
| `../RAPPORT_AUDIT_ADVERSARIAL_V4_4.md` | Le présent rapport | Synthèse, hors manifeste |
| `../05_ALSTOM/INVESTIGATION_REVOLVING_DOOR_BAILEY_2026-09-13.md` | Dossier d'investigation ajouté pour combler l'écart de traçabilité du paragraphe Hugh Bailey | `AUDITOR_ADDED_NON_CERTIFIE` |

**Deux fichiers du pont ont dû être rapatriés** : `--save` avait été résolu depuis la racine du dépôt et non depuis le bundle. Ils ont été déplacés dans `07_COLLAB_CHATGPT/` et le dossier vide créé par erreur a été supprimé.

---

## 13. Recommandations

1. **Re-sceler ou ne pas re-sceler, en connaissance de cause.** Si la cible corrigée devient la version publiée, la ligne du manifeste doit être mise à jour et l'empreinte d'origine conservée dans l'historique. Si le manifeste doit rester l'empreinte de la version auditée, alors la cible patchée doit être déplacée hors du bundle scellé et le manifeste laissé intact. **Ne pas faire les deux à moitié.**
2. **Trancher les quatre points ouverts de la section 11**, dont un seul appelle une décision éditoriale lourde (Hugh Bailey).
3. **Avant publication, relire [58] dans sa version intégrale**, si un accès non bloqué existe. Ma vérification est une concordance de plusieurs organes plus une dépêche AFP lue en entier, documentée comme telle.
4. **Ne pas réutiliser le pont comme évaluateur.** Il a été exact avec le document sous les yeux et faux sans lui. C'est un accès au web de secours, pas un relecteur.
5. **Considérer cette limite comme la principale** : le bundle, l'article et cet audit n'ont produit aucune instance indépendante l'un de l'autre. Un audit réellement adversarial demanderait un modèle différent, sans historique commun, et si possible sans accès au corpus de l'auteur.

---

## 14. Conclusion en une page

L'article **n'est pas un texte fabriqué**. Ses sources existent, ses chiffres sont exacts à deux exceptions près, sa méthode est plus falsifiable que la moyenne de ce qui se publie sur ces sujets, et il nomme ses propres contre-exemples. Ses défauts étaient de trois ordres : une **rupture de provenance** entre ce que sa bibliographie promettait et ce que son corps disait, **deux franchissements** de sa propre exigence de preuve, et une **surexposition rhétorique** du dossier où il prouve le moins.

Ces trois ordres sont traités par 19 éditions, dont cinq corrigent mes propres erreurs de patch.

Ce qui reste n'est pas un défaut du texte. C'est une limite du dispositif : **un paragraphe nominatif adossé à la presse plutôt qu'au corpus**, et **aucune instance réellement indépendante** dans toute la chaîne de production et de vérification. La première se tranche par une décision éditoriale. La seconde ne se tranche pas ici.

*Zéro em-dash dans ce document. Contrôles effectués par `rtk grep`, `sha256sum` et `sha256sum -c` le 2026-09-13.*

---

## 15. Addendum : deuxième vague de corrections (éditions 20 à 28)

Ajoutée le 2026-09-13 après décision de périmètre. Neuf éditions supplémentaires, dont cinq corrections de sourçage et quatre améliorations argumentatives, plus un dossier d'investigation.

| Édition | Objet | Justification |
|---|---|---|
| 20 | [49] Rockhopper : renvoi vers le document de décision (italaw) au lieu d'une page de base de données | La page citée n'affichait pas la date, et une table CIRDI afficherait encore la date erronée |
| 21 | [48] Vattenfall : ajout du communiqué Vattenfall du 5 mars 2021 | **Défaut franc** : la source citée ne nommait pas Vattenfall, vérifié par lecture intégrale |
| 22 | [12] : renvoi vers l'arrêt C-124/20 au lieu du « panorama » de la CJUE | Renvoi vers un résumé d'activité au lieu du document |
| 23 | [28] : ajout du document Internet Society sur la non-adoption de New IP | La non-adoption reposait sur une source dérivée |
| 24 | §I : périmètre BNP Paribas | Confusion entre montant de confiscation et volume de transactions |
| 25 | Légende Figure 1 : le contre-pouvoir nommé | La légende présentait six objets comme exhaustifs alors que le §IV en ajoute un septième |
| 26 | Chapeau : restriction « sans commande démontrée » | Le titre promettait plus que la démonstration |
| 27 | Chapeau Alstom : offre concurrente Siemens / Mitsubishi Heavy Industries | **Correction la plus importante** : elle déplace la lecture d'un État qui autorise tardivement vers un État qui arbitre |
| 28 | §III : les règlements du DOJ présentés comme des récits de partie | Asymétrie de provenance désormais énoncée |

**Sur l'édition 27, la plus significative.** La chronologie du chapeau était exacte mais incomplète, et son incomplétude produisait un effet de sens : sans concurrent, l'État français n'apparaît qu'au moment d'autoriser. Avec la contre-offre de Siemens et de Mitsubishi Heavy Industries et la demande adressée par l'Élysée aux deux candidats d'améliorer leurs propositions, l'État apparaît à sa place, celle d'un arbitre. C'est la démonstration que l'article veut faire, et elle était desservie par son propre chapeau.

**Sur l'édition 26.** Je n'ai pas touché au titre. « Le pouvoir sans commande » reste une formule juste et efficace ; c'est la démonstration qui devait porter la restriction, une fois, en ouverture.

**Sur l'édition 21.** C'est le seul défaut franc de cette vague : la source citée ne nomme pas Vattenfall. Ce n'est pas une erreur d'attribution de l'article, c'est une source insuffisante pour l'attribution qu'il en fait.

**Dossier d'investigation ajouté.** `05_ALSTOM/INVESTIGATION_REVOLVING_DOOR_BAILEY_2026-09-13.md`, statut `AUDITOR_ADDED_NON_CERTIFIE`. Il établit la chronologie de carrière sur une dépêche AFP lue intégralement et il consigne les deux éléments publics que l'article ne reprend pas. Il ne vaut pas certification, et il ne comble pas la limite structurelle signalée en section 9 : le dossier a été produit par l'auditeur, après l'audit, sur l'écart que l'auditeur avait lui-même relevé.

**Réserves de cette vague.** Le communiqué Vattenfall et le document Internet Society sont connus par leur titre, leur date et un extrait cité concordant ; je ne les ai pas lus dans leur intégralité. Ces deux ajouts de sources devraient être relus avant publication.

---

## 16. Addendum : mise en forme éditoriale Substack (éditions 29 à 35)

Ajouté le 2026-09-13, à la demande de l'auteur : emoji de titre, sous-titre de publication, encart d'ouverture, six liens de maillage et une section de fin. Sept éditions de forme.

**Aucune de ces éditions ne porte sur une affirmation factuelle.** Aucune source, aucun statut, aucun renvoi n'est modifié. Le verdict de la section 1 est donc inchangé. Mais deux choses doivent être consignées, parce que ce rapport prétend distinguer les niveaux de preuve :

1. **Le maillage n'est pas de la corroboration.** Les six posts liés sont des travaux antérieurs du même auteur. Ils informent le lecteur et rendent la thèse vérifiable dans le corpus ; ils ne constituent pas des instances indépendantes. Les compter comme confirmations reproduirait exactement l'erreur que la section 0 interdit.
2. **L'encart d'ouverture est un récit de l'auteur, pas une pièce du dossier.** Il raconte que l'enquête est partie de l'ingérence. Ce récit est cohérent avec la conclusion de l'article, qui portait déjà la phrase « Le point de départ était l'ingérence. Le point d'arrivée est le pouvoir » (l. 193 avant ce lot), mais aucune pièce du corpus ne l'établit au-delà de cette phrase. Il ne doit pas être lu comme une preuve d'origine.

**Sur les liens, un point de conformité.** La politique `BODY_SUBSTACK_WIKILINKS = 2` documentée pour l'article XQ204 (2026-08-22) n'est pas respectée ici : le lot en pose sept occurrences, six posts distincts. Le choix suit le dernier article publié (`articles/2026-08-31_dechetteries-france_ARTICLE.md`, six liens de corps) et non la politique XQ204, qui est propre à un autre article. C'est une divergence assumée et réversible par retrait, pas un oubli.

**Empreinte finale de la cible** : `ad93ec8cbd3efc1f1dc87f9154751642b60ab9733609289e21710816c1a32eef` après ce lot, soit 35 éditions depuis l'origine. Le manifeste reste non re-scellé, conformément à la section 12.

---

## 17. Addendum : édition 36, les trois niveaux de pouvoir

Ajoutée le 2026-09-13 après la note de fond et sur demande de l'auteur. Une seule modification, la première qui porte sur le fond depuis le début de l'audit, et la dernière en date.

**Le défaut.** La l. 81 affirmait que « il suffit de tenir quelque chose dont l'autre dépend », tandis que la l. 83 exigeait une modification observable de la capacité de la cible. Les deux phrases se contredisaient : la première faisait de la possession un pouvoir, la seconde en faisait la condition d'un effet. C'était la seule faille de falsifiabilité restante, et elle a été relevée par le pont puis vérifiée dans le texte.

**La correction.** La possession devient explicitement une **capacité**, et un paragraphe distingue trois niveaux : la capacité (une position), le pouvoir mobilisable (la possibilité effective de l'activer), le pouvoir exercé (l'activation constatée avec effet observable). Le texte précise que le troisième est le seul qui autorise une conclusion.

**Ce que cette édition ne fait pas.** Elle ne change aucun fait, aucune source, aucun chiffre, aucun statut. Elle ne modifie pas le verdict de la section 1. Elle retire une imprécision de vocabulaire qui affaiblissait la thèse en la rendant partiellement irréfutable.

**Édition 37, alignement de la conclusion.** La l. 211 disait « le pouvoir se voit d'abord dans ce qu'un acteur **peut** ouvrir, fermer, renchérir ou rendre plus visible ». Le verbe « peut » décrit le niveau mobilisable, celui sur lequel le paragraphe neuf refuse justement de conclure. La phrase devient : « le pouvoir ne se lit pas d'abord dans une décision finale, mais dans une capacité et, lorsqu'il a été observé, dans l'exercice d'un levier », suivie des effets observés, et la comparaison porte désormais sur « ces deux niveaux » au lieu de « ces leviers situés en amont », qui était plus vague. Aucun fait, aucune source, aucun chiffre modifié.

**Éditions 38 à 41.** L'édition 38 porte sur le fond : la documentation inégale n'est plus seulement reconnue comme une limite, elle borne explicitement la thèse (la l. 34 dit maintenant que l'écart de preuve peut tenir en partie à ce que les documents montrent plus volontiers un point de passage qu'un ordre). Les éditions 39 à 41 sont le résultat d'une **relecture intégrale visant toute confusion entre capacité et pouvoir exercé** : trois défauts de cette classe ont été trouvés (l. 13 dans le chapeau, l. 9 dans l'encart, l. 85 pour une collision du mot « capacité »), aucun autre. **Deux des trois avaient été introduits par mes propres éditions** : l'encart du lot 2 et la collision créée par l'édition 36, qui a défini la « capacité » comme la position du titulaire deux lignes avant un emploi du mot au sens de marge de la cible. Les passages vérifiés conformes, et ils sont les plus rigoureux du texte, sont les l. 65, 121, 190 et 223.

**Empreinte finale** : `f03df99fa95e85c44bbf4f59e6aa5b9f847d43fa621d9b5f98c3324e68bd94c5`, soit 41 éditions depuis l'origine. Contrôles : 0 em-dash, 0 flèche ASCII, 0 espace insécable, 0 occurrence résiduelle des formules remplacées.

---

## 18. Addendum : éditions 42 à 55, application du plan de corrections

Ajoutée le 2026-09-13 sur demande de l'auteur. Principe de cadrage : **baisser l'ambition théorique, monter l'ambition probatoire**, sans sortir de la forme du corpus publié. Source : `PLAN_CORRECTIONS_V4_4_2026-09-13.md` (v2), rangs 1 à 6. Détail édition par édition : `07_COLLAB_CHATGPT/2026-09-13_patch_log_editions.md`, section 10.

### Ce qui a été appliqué

| Axe | Opération | Emplacement |
|---|---|---|
| Théorie | Titre et sous-titre recadrés sur ce que les preuves permettent | tête d'article |
| Théorie | Lignée reconnue : Bachrach et Baratz 1962, Lukes 1974, Strange 1988 | après le fait d'ouverture |
| Théorie | Six formules universalisantes abaissées | parties I, IV, conclusion |
| Preuve | Unité probatoire définie (cas, affirmation codée, relation) | paragraphe de méthode |
| Preuve | Garde-fou sur l'hétérogénéité de la variable finale | paragraphe de méthode |
| Preuve | Bilan à trois paliers en prose, puis liste numérotée des six conditions manquantes | conclusion |
| Preuve | Huit contrôles nommés comme tels | conclusion |
| Preuve | Codage interne publié et borné (445 affirmations, 45 investigations, 357 / 88) | fin de la partie III |
| Preuve | Réversibilité en quatre coordonnées non agrégées, refus de l'indice unique | fin de la partie IV |
| Forme | 77 marqueurs `[n]` du corps remplacés par des sources nommées ; registre numéroté conservé | article entier |
| Forme | Ouverture par un fait daté ; 7 séparateurs ; quatre nombres en chiffres | article entier |

### Ce que l'application a établi, et qu'il faut retenir

**Le chiffre du codage interne est exact et vérifiable à la source.** `03_FORENSIC_INDEX/CLAIM_EVIDENCE_TRACE.csv` contient 445 lignes de données hors en-tête, couvrant 45 investigations de `INV-001` à `INV-045` sans trou. Répartition : 357 `NO` et 88 `YES` pour le signal causal ; 386 `E2`, 32 `E3`, 16 `E1`, 11 `E0` pour le niveau de preuve. La formulation employée dans le texte reprend ces chiffres avec leurs trois bornes (auto-déclaré, partiel, sans valeur de prévalence).

**Les huit contrôles existaient déjà dans l'article ; ils n'étaient pas nommés.** La vérification a porté sur les neuf cas cités par la lecture externe : New IP, Lituanie, Photonis, Rockhopper, HATVP, Hopium, CMA CGM, Vattenfall, Arabelle, COSCO sont tous présents dans la cible avant édition. Aucun cas n'a été ajouté, aucune enquête nouvelle n'a été ouverte.

**La conversion des marqueurs est complète.** Zéro occurrence résiduelle de `[n]` dans le corps, et les 59 entrées du registre conservées avec leurs URL : la traçabilité dont les audits dépendent est intacte, et le lecteur lit désormais des noms au lieu de crochets.

### Ce que ces éditions coûtent

| Mesure | Avant (éd. 41) | Après (éd. 55) |
|---|---|---|
| Mots du corps | environ 8 100 (mesure du plan v2) | **9 667** |
| Mots totaux | environ 9 400 (estimation) | 10 969 |
| Marqueurs `[n]` dans le corps | 77 | **0** |
| Séparateurs `---` | 1 | 7 |
| Segments en gras, corps | 35 | 49 (plage du corpus : 8 à 110) |
| Tableaux Markdown | 0 | 0 |
| Figures | 4 | 4 |

**Environ 1 570 mots ajoutés.** C'est le prix direct des opérations de probité : bilan, contrôles, unités, garde-fou, lignée, plus la conversion des renvois en sources nommées. La compression prévue au rang 7 du plan n'a pas été faite : elle reste l'arbitrage de l'auteur.

### Trois écarts au plan, assumés et déclarés

**1. Pas de tableau de profil de preuve.** Le rang 7 du plan laissait le choix entre un tableau central et la forme du corpus. J'ai retenu la forme du corpus : le tableau était l'opération la plus efficace du point de vue probatoire, mais **zéro ligne de tableau** dans les articles publiés mesurés. Le contenu du tableau est passé en bilan à paliers et en liste numérotée.

**2. Le gras remonte de 35 à 49 segments.** Les blocs `**Est établi**`, `**N'est établi dans aucun des cas examinés**` et les huit intitulés de contrôles en ajoutent. 49 reste dans la plage mesurée du corpus (8 à 110), mais c'est une hausse, pas une baisse, et elle contredit l'intuition de la première version du plan.

**3. Les nombres ne sont convertis qu'en partie.** « 6 refus », « 3 ans », « 8 réunions », « 6 objets » le sont. « Trois niveaux », « trois hypothèses », « quatre questions », « huit raccourcis » restent en lettres : ce sont des articulations du raisonnement, pas des grandeurs mesurées. C'est un choix de style, pas une omission.

### Ce qui reste ouvert

- **Rang 7 du plan, décision de l'auteur** : les quatre figures (0 dans tout le corpus publié) sont à retirer ou à téléverser, et la compression de 1 570 mots est à trancher.
- **Rang 8 du plan, non exécuté** : le contrôle terminal, phrase par phrase, où chaque proposition générale doit pointer vers une preuve, une borne ou une incertitude nommée. Les éditions 36 à 41 ont fait ce travail sur la classe « capacité contre pouvoir exercé » ; il n'a pas été refait sur les paragraphes ajoutés.
- **Le manifeste** n'est pas re-scellé, comme documenté en section 12. La ligne de remplacement exacte est fournie dans le journal de patch, section 10.

### Ce que ces éditions ne changent pas

**Aucun fait, aucune source, aucun chiffre, aucun statut de preuve.** Le verdict de la section 1 est inchangé. Ce qui a changé est le contrat passé avec le lecteur : le titre promet désormais de dire jusqu'où la preuve va, et le texte tient cette promesse en nommant, à trois paliers, ce qu'il établit et ce qu'il n'établit pas.

**Empreinte courante de la cible** : `c2497885a982e7ae0ac58521825df707148d3dbebf804e2311577b0543e252af`, soit 55 éditions. Contrôles : 0 em-dash, 0 flèche ASCII, 0 espace insécable, 0 marqueur résiduel dans le corps.

---

## 19. Addendum : éditions 56 à 63, contrôle terminal phrase par phrase

Exécuté le 2026-09-13 sur demande de l'auteur, dernière opération du plan (rang 8). Règle appliquée : **toute proposition générale doit pointer vers une preuve, une borne explicite ou une incertitude nommée**. Détail complet : `07_COLLAB_CHATGPT/2026-09-13_CONTROLE_TERMINAL.md`.

### Ce qui a été examiné

**62 propositions générales**, c'est-à-dire toutes les phrases du corps qui affirment quelque chose au-delà d'un cas unique : critères de lecture, conclusions transversales, quantificateurs, définitions, jugements comparatifs. Les phrases purement factuelles sur un dossier ne sont pas listées : depuis l'édition 52, chacune porte sa source dans la phrase elle-même.

**Répartition après correction** : 29 avec preuve directe, 19 avec borne seule, 2 avec incertitude nommée seule, 12 combinant deux garanties. **Aucune ne reste sans garantie.**

### Les huit défauts, et le plus sérieux

| # | Où | Défaut en une ligne |
|---|---|---|
| 56 | Partie I, ouverture | Affirmation générale sur le monde politique (« la forme la plus visible du pouvoir politique reste la persuasion ») sans pièce ni borne |
| 57 | Partie I, gaz | « Le succès **du** levier se mesure » : article défini généralisant et verbe promettant une mesure inexistante. **Reste de la même classe que les six formules de l'édition 47** |
| 58 | Partie II, agences | Affirmation négative générale sur le modèle d'agence, alors que la source mesure des proportions, pas l'absence d'instruction |
| 59 | Partie II, fact-checking | Qualification attribuée avant la pièce (« exerce un pouvoir » là où la source documente des écarts de sélection) |
| 60 | Partie III, ouverture | Affirmation générale sur le débat public, sans source ni borne |
| 61 | Partie III, trafic d'influence | **Erreur d'appariement de source** : la phrase sur le droit européen portait la référence au code pénal français, et la phrase sur l'article 433-2 n'en portait aucune |
| 62 | Partie IV, Alstom | Deux « se mesure » dans la même phrase, alors que l'édition 51 venait d'écrire que les quatre dimensions ne sont pas commensurables |
| 63 | Partie IV, révision de thèse | **L'autonomie des acteurs était déduite de l'absence de preuve de coordination**, soit exactement le raisonnement que le paragraphe suivant interdit. Quatre passes précédentes avaient laissé la phrase intacte |

**Le défaut 63 est le plus sérieux de tout l'audit**, parce qu'il touche le point où l'article se retourne contre lui-même. Après avoir établi qu'il faut démontrer les liens avant de parler d'architecture intégrée, il affirmait des « acteurs autonomes ». L'autonomie n'était pas établie : elle était supposée à partir de l'absence de preuve de coordination. C'est le même glissement que l'article reproche aux autres, et il a fallu huit passes pour le voir. Le mot est retiré ; la phrase dit désormais ce que l'enquête établit, des dotations inégales et des leviers différents.

**Deux défauts sur huit sont des traces de mes propres interventions** : le 57 est un reste de l'édition 47, où j'avais corrigé six formules de cette classe sans voir la septième, et le 63 avait été laissé intact par les éditions 36 à 41, qui visaient pourtant la confusion capacité contre pouvoir exercé.

### Ce que ce contrôle ne fait pas

- **Il vérifie qu'une phrase désigne sa garantie, pas que la source dit ce qu'on lui fait dire.** Les 59 entrées du registre ne sont pas revérifiées ici ; cela reste le travail de la section 1.
- **Il est fait par un seul auditeur, celui qui a écrit les ajouts.** Le défaut 57 est la preuve de cet angle mort. Un contrôle externe trouverait probablement d'autres cas de la même classe.
- **Il ne dit rien de la longueur ni des figures.** La compression et le sort des quatre figures restent les décisions de l'auteur.

### État

**Empreinte courante** : `1cb2f0c12b4736f2893d1238fd6effd0eba3d0abdb1f2fccaee28b9711cdff66`, soit **63 éditions**. Corps : 9 669 mots, total 10 971. Contrôles : 0 em-dash, 0 flèche ASCII, 0 espace insécable, 0 marqueur `[n]` dans le corps, 59 entrées de registre, 0 tableau. Aucun fait, aucun chiffre, aucun statut de preuve modifié par ces huit éditions.

*Zéro em-dash dans ce document.*

