# INV-002 — Cartographie exhaustive du corpus Substack

**Statut : PASS — cartographie terminée, revue humaine requise avant INV-003+.**

## 1. Périmètre et règle épistémique

Corpus canonique : **121 articles** de la baseline gelée au 26 août 2026. INV-002 cartographie les thèses, acteurs, mécanismes, dimensions, limites explicites et ancrages documentaires visibles. **Elle ne re-fact-checke pas les 121 articles.** Chaque ligne de `INV-002_CORPUS_MAP.csv` porte donc `verification_inv002=NOT_REVERIFIED`. Un claim publié antérieurement reste un claim du corpus tant qu’un nouveau run ne l’a pas revalidé.

Les classes `RICH/MEDIUM/SPARSE/NONE_IN_EXPORT` mesurent seulement la **traçabilité de liens externes dans l’HTML exporté** et la présence de sections Sources ; elles ne mesurent ni la vérité ni la qualité intrinsèque des sources. `ASSERTIVE/MIXED/CALIBRATED` est un triage linguistique destiné à guider le réemploi, pas un verdict de vérité.

## 2. Verdict synthétique

- Pertinence pour le nouveau chantier : **71 DIRECT**, **36 SUPPORTING**, **14 CONTEXT**.

- Réutilisation : **8 ANCHOR**, **63 LEAD_REVERIFY**, **36 SUPPORT**, **14 CONTEXT_ONLY**.

- Couverture des 124 sujets déjà enregistrés : **42 SUBSTANTIAL_PRIOR**, **73 PARTIAL**, **9 NEW**.

- **78 / 124** couvertures initiales ont été requalifiées après lecture du corpus : la liste initiale sous-estimait fortement ce qui avait déjà été abordé.

- Conséquence : **ne pas lancer 112 Truth Engine from scratch**. Les sujets `SUBSTANTIAL_PRIOR` doivent d’abord être rejoués en `RECHECK/EXTEND`; les `PARTIAL` en `DEEPEN`; les `NEW` seulement en greenfield.

## 3. Évolution documentaire du corpus

| Mois | Articles | Médiane liens externes HTML | RICH | NONE_IN_EXPORT |
|---|---:|---:|---:|---:|
| 2025-11 | 21 | 0 | 0 | 18 |
| 2025-12 | 16 | 0 | 1 | 15 |
| 2026-01 | 11 | 0 | 0 | 10 |
| 2026-02 | 9 | 0 | 1 | 5 |
| 2026-03 | 11 | 27 | 9 | 1 |
| 2026-04 | 11 | 17 | 10 | 0 |
| 2026-05 | 23 | 19 | 21 | 0 |
| 2026-06 | 8 | 41.5 | 8 | 0 |
| 2026-07 | 6 | 29.5 | 6 | 0 |
| 2026-08 | 5 | 51 | 5 | 0 |

La rupture est nette : novembre 2025 → février 2026 contient beaucoup d’articles courts ou sans liens externes exploitables dans le snapshot ; à partir de mars 2026 la traçabilité embarquée augmente fortement ; août 2026 contient les enquêtes les plus explicitement calibrées. Cela impose une hiérarchie de réemploi : **ancien texte = lead**, sauf revalidation ; **enquête récente calibrée = anchor potentiel**, mais toujours recheck des claims matériels.

## 4. Huit anchors actuels pour ce nouveau sujet

| A | Article | Pourquoi anchor |
|---:|---|---|
| A001 | 🕵️♂️ Qui fact-checke les fact-checkers ? | Traçabilité riche et formulation relativement calibrée ou limitée ; directement relié aux mécanismes d’influence/pouvoir. |
| A002 | 🔍 Qui fabrique l'autorité du vrai ? | Traçabilité riche et formulation relativement calibrée ou limitée ; directement relié aux mécanismes d’influence/pouvoir. |
| A004 | 🔍 L'ingérence sans mesure | Traçabilité riche et formulation relativement calibrée ou limitée ; directement relié aux mécanismes d’influence/pouvoir. |
| A007 | 🔒 Le peuple n'existe que sur convocation | Traçabilité riche et formulation relativement calibrée ou limitée ; directement relié aux mécanismes d’influence/pouvoir. |
| A008 | 🎬 La fabrique de la menace : comment le documentaire d'Arte transforme une coopération réelle en guerre totale | Traçabilité riche et formulation relativement calibrée ou limitée ; directement relié aux mécanismes d’influence/pouvoir. |
| A023 | ⚔️ La Défense rongée : 449 Md€ sans munitions, 101 voyages ELNET, 24 pays sans standard français : la souveraineté stratégique dissoute de l’intérieur | Traçabilité riche et formulation relativement calibrée ou limitée ; directement relié aux mécanismes d’influence/pouvoir. |
| A058 | 🔥 LA GUERRE DES AUTRES | Traçabilité riche et formulation relativement calibrée ou limitée ; directement relié aux mécanismes d’influence/pouvoir. |
| A063 | ☢️ Le sanctuaire inversé : comment la France a vendu son âme nucléaire en prétendant la sauver | Traçabilité riche et formulation relativement calibrée ou limitée ; directement relié aux mécanismes d’influence/pouvoir. |

Ces anchors ne sont pas des vérités canoniques : ils sont simplement les meilleurs points de départ du corpus actuel.

## 5. Mécanismes récurrents cartographiés

| Mécanisme | Articles touchés |
|---|---:|
| DROIT_REGULATION | 49 |
| FINANCEMENT_FLUX | 46 |
| ELECTION_CONSENTEMENT | 40 |
| GUERRE_SECURITE | 40 |
| COERCITION_ADMIN | 38 |
| CAPTURE_INSTITUTIONNELLE | 35 |
| CADRAGE_NARRATIF | 27 |
| LOBBYING_RESEAUX | 23 |
| SURVEILLANCE_DONNEES | 22 |
| DEPENDANCE_ECONOMIQUE | 22 |

Le motif transversal le plus fréquent dans le corpus est compatible avec une chaîne du type `ressource/argent → intermédiaire/réseau → information/expertise/média → règle/décision/comportement`. **INV-002 constate la récurrence narrative et documentaire de ce motif ; elle ne démontre pas qu’il existe un centre commun, une coordination générale ni une causalité unique.**

## 6. Dimensions transdisciplinaires déjà présentes

| Dimension | Articles touchés |
|---|---:|
| ECONOMIQUE | 61 |
| POLITIQUE | 56 |
| JURIDIQUE | 46 |
| TECHNIQUE | 29 |
| SCIENTIFIQUE | 29 |
| SOCIALE | 26 |
| ETHIQUE | 22 |
| ANTHROPOLOGIQUE | 21 |

Le corpus est déjà très politique, économique, juridique et technique. Les dimensions **psychologique, anthropologique, communication/marketing** existent, mais restent moins systématiquement adossées à des tests causaux et comparateurs. Elles devront être renforcées par les nouvelles investigations plutôt que simplement réemployées.

## 7. Asymétrie majeure de couverture

Le corpus est fort sur **France/UE, souveraineté, médias, censure/modération, État, architecture réglementaire, énergie, défense, défiance, capture et fact-checking**. Il est beaucoup plus faible sur une comparaison réellement symétrique des puissances et techniques étrangères : USAID/NED comme architecture complète, United Front chinois, Turquie, Maroc/Algérie, Royaume-Uni, réseaux transatlantiques, révolutions de couleur, achat de votes et fraude électorale. La future fresque doit corriger cette asymétrie pour ne pas généraliser un système mondial à partir d’un corpus essentiellement franco-européen.

## 8. Les neuf sujets réellement NEW

| ID | Sujet | Action |
|---|---|---|
| INV-015 | Otpor, CANVAS et exportation des techniques de mobilisation politique | DEEPEN |
| INV-016 | Printemps arabes : spontanéité, réseaux sociaux, assistance occidentale, ONG, diplomatie et intérêts géopolitiques | DEEPEN |
| INV-025 | Chine : United Front et frontière entre diaspora, influence et contrôle politique | DEEPEN |
| INV-031 | Royaume-Uni : influence financière, diplomatique, médiatique et renseignement en Europe | DEEPEN |
| INV-036 | Turquie : État, diaspora, religion, associations et mobilisation politique en Europe | DEEPEN |
| INV-038 | Maroc et Algérie : influence politique, diplomatique et diasporique en France — séparer les deux États dans l’enquête | DEEPEN |
| INV-098 | Achat de votes, clientélisme et redistribution électoraliste : formes modernes et réalité française | DEEPEN |
| INV-099 | Fraude électorale réelle versus industrie de l’accusation de fraude : fréquence, mécanismes, vérifiabilité | DEEPEN |
| INV-118 | CFR / Trilateral Commission / réseaux transatlantiques : influence intellectuelle versus coordination politique | DEFER |

`NEW` signifie : aucune investigation substantielle identifiée dans les 121 articles, **pas** absence totale de mention.

## 9. Évaluation des 12 idées initiales W10

| ID | Couverture | Utilité | Décision |
|---|---|---|---|
| INV-113 | PARTIAL | MEDIUM | DEEPEN |
| INV-114 | PARTIAL | MEDIUM | DEEPEN |
| INV-115 | PARTIAL | MEDIUM | DEEPEN |
| INV-116 | PARTIAL | MEDIUM | DEEPEN |
| INV-117 | PARTIAL | MEDIUM | DEEPEN |
| INV-118 | NEW | MEDIUM | DEFER |
| INV-119 | SUBSTANTIAL_PRIOR | HIGH | RECHECK |
| INV-120 | PARTIAL | HIGH | DEEPEN |
| INV-121 | PARTIAL | MEDIUM | DEEPEN |
| INV-122 | SUBSTANTIAL_PRIOR | HIGH | RECHECK |
| INV-123 | SUBSTANTIAL_PRIOR | HIGH | RECHECK |
| INV-124 | PARTIAL | HIGH | DEEPEN |

Conclusions : `INV-119`, `INV-122`, `INV-123` sont déjà suffisamment présents pour commencer par un **RECHECK**, pas un nouveau départ. `INV-118` (CFR/Trilateral) reste sans base corpus suffisante : **DEFER**, sauf apparition ultérieure d’un lead matériel. Les autres idées sont légitimes mais doivent approfondir ce qui n’est encore que partiellement traité.

## 10. Nouveaux gaps ajoutés par INV-002

Cinq investigations ont été ajoutées et **évaluées immédiatement**, donc pas laissées en inbox indéterminée :

- **INV-125 — Infrastructures numériques critiques et souveraineté : cloud, hébergement, données, câbles, puces, extraterritorialité et dépendance comme leviers de pouvoir** — `PARTIAL`, utilité `HIGH`, `P1`, action `DO/DEEPEN`.
- **INV-126 — Corps intermédiaires, syndicats, fédérations professionnelles et chambres consulaires : représentation légitime versus capture de la décision** — `PARTIAL`, utilité `HIGH`, `P1`, action `DO/DEEPEN`.
- **INV-127 — Soft power culturel et académique : universités, bourses, instituts, échanges, langue, culture et formation des élites** — `NEW`, utilité `MEDIUM`, `P2`, action `DO/DEEPEN`.
- **INV-128 — Influence-for-hire : renseignement privé, cabinets d’intelligence, réputation, infiltration et campagnes clandestines pour clients étatiques ou privés** — `PARTIAL`, utilité `HIGH`, `P1`, action `DO/DEEPEN`.
- **INV-129 — Lawfare et coercition juridique : contentieux stratégique, SLAPP, sanctions administratives, procédures et droit comme instruments d’influence** — `PARTIAL`, utilité `HIGH`, `P1`, action `DO/DEEPEN`.

Ces ajouts restent modestes : ils comblent des trous transversaux détectés dans le corpus sans ouvrir une nouvelle arborescence opportuniste.

## 11. Risques de régression si le corpus est réutilisé naïvement

1. **Titre/thèse forte ≠ claim démontré.** Beaucoup d’articles emploient déjà `machine`, `architecture`, `capture`, `sabotage`, `caste`, `mensonge`, etc. Le futur Truth Engine doit atomiser ces formulations avant héritage.
2. **Réseau ≠ coordination.** Plusieurs textes relient personnes, financeurs, cabinets, ONG ou institutions. Ces graphes sont des leads tant que mécanisme, chronologie, indépendance et effet ne sont pas établis.
3. **Financement ≠ contrôle du verdict.** Les enquêtes récentes sur le fact-checking corrigent explicitement cette dérive ; cette correction doit devenir rétroactive pour les anciens articles.
4. **Opération ≠ impact.** `L’ingérence sans mesure` fournit déjà le garde-fou : détection/attribution n’établit pas exposition, persuasion ni effet électoral.
5. **Officialité ≠ vérité, mais document primaire ≠ simple opinion.** La valeur probatoire doit rester claim-specific.
6. **Corpus ancien ≠ baseline probatoire actuelle.** Les articles sans traçabilité externe dans l’export doivent être revalidés depuis leurs sources avant réemploi.

## 12. Décision INV-002

**PASS pour la cartographie. HOLD pour la suite.** `INV-002` est fermée ; `INV-003..INV-008` restent bloquées sur `HUMAN_REVIEW_INV-002`. Aucun Truth Engine supplémentaire ne doit être lancé avant analyse de cette carte et éventuel recadrage des sujets, priorités et règles de réemploi. RENARD = NO pour INV-002 : la valeur est dans la cartographie et le triage, pas dans une passe adversariale supplémentaire.

## 13. Artefacts

- `INV-002_CORPUS_MAP.csv` : 121 lignes, carte article par article.
- `INV-002_INVESTIGATION_COVERAGE.csv` : évaluation des 124 sujets initiaux.
- `INV-002_COVERAGE_CHANGES.csv` : 78 requalifications.
- `INV-002_THEME_MATRIX.csv` : acteurs/mécanismes/dimensions.
- `INV-002_STATS.json` : métriques de contrôle.
