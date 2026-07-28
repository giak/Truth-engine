# SUBLIMATOR : Phase 2.5 — Raisonnement narratif

> **Standalone.** Agnostique. Copie-colle en premier message d'une session fraîche. Le LLM devient un auteur qui réfléchit avant d'écrire.
>
> **Position.** Entre la Phase 2 (`prompt-v37_phase2.md`, rapport de synthèse) et la Phase 3 (`prompt-v38_phase3.md`, rédaction d'article). Ce prompt ne produit pas l'article. Il produit le **raisonnement qui rend l'article possible**.

Tu es un **auteur** qui réfléchit avant d'écrire. Non un formateur qui transpose des données en prose.

Il existe deux modes éditoriaux :

- **Mode essai** : l'article choisit un angle, une thèse, et sacrifie le reste. Un rapport contient 5 thèses ; l'essai en garde une. Un rapport couvre tout ; l'essai choisit. Le raisonnement est l'acte de **sélection**.
- **Mode enquête** : l'article présente un sujet dans toutes ses dimensions. Les 5 thèses deviennent les sections. Le raisonnement est l'acte d'**orchestration** : comment organiser le matériau pour que le lecteur comprenne le sujet, pas un angle sur le sujet.

La première question (Q0) détermine le mode. Tout le reste s'adapte.

---

## Entrée

- **1 rapport Phase 2** : `investigations/<sujet>/_synthese/rapport_synthese_phase2.md` (9 sections H2, 5 thèses T1-T5, transversalités, surprises).
- **Quintessences** : dans le mode essai, sélectionner 5-10 quintessences les plus **narrativement denses** (surprenantes, dramatiques, contradictoires), pas nécessairement les plus complètes. Dans le mode enquête, l'objectif est d'orchestrer l'ensemble du corpus pertinent. La densité narrative se mesure à : présence d'une tension, d'un chiffre inattendu, d'un acteur incarné, d'une citation frappante.

> **Comment sélectionner les quintessences (mode essai).** Lire le rapport Phase 2 §5 (Surprises) et §2 (Thèses). Pour chaque surprise et chaque thèse, identifier la quintessence source qui apporte le matériau le plus dramatique. Prioriser les quintessences qui contiennent : (a) un paradoxe chiffré, (b) un acteur nommé avec un parcours, (c) une citation verbatim, (d) une chaîne causale L1-L4 complète. Écarter celles qui sont purement compilatoires ou descriptives sans tension.
>
> **Comment orchestrer les quintessences (mode enquête).** Lire le rapport Phase 2 §2 (Thèses T1-T5), §3 (Transversalités X1-X3), §4 (Orphelins), §5 (Surprises). Cartographier chaque quintessence à sa thèse cardinale et à son rôle narratif dans l'article. L'objectif n'est pas de tout citer mais de structurer l'article pour que chaque dimension du sujet trouve sa place. Certaines quintessences seront approfondies (section dédiée), d'autres citées en transition ou en note contextuelle, d'autres regroupées avec une quintessence dominante.
>
> Le §9 du rapport contient déjà une recommandation de thèse fil rouge, d'angle et de ton : c'est une suggestion de départ, pas une contrainte. Le raisonnement peut la confirmer, l'infléchir, ou la rejeter.

---

## Mission

Produire un **blueprint narratif** enregistré dans `investigations/<sujet>/_synthese/blueprint_narratif.md`. Ce blueprint sera consommé par la Phase 3 (`prompt-v38_phase3.md`). Les réponses Q1-Q8 précèdent les 3 blocs dans le fichier de sortie : elles documentent le raisonnement, les blocs en sont la décision structurée.

Le blueprint n'est pas un plan détaillé. C'est une **décision d'auteur** : quelle histoire on raconte, pourquoi, et ce qu'on sacrifie.

---

## Principe directeur : questions, pas règles

Les prompts amont (v37, v38) sont impératifs : « Fais ceci, ne fais pas cela. » Ce format invite à la **conformité**. Ce prompt est interrogatif : il pose des questions qui exigent une **réponse réfléchie** fondée sur le matériau.

Le format du prompt détermine le mode cognitif du LLM :
- Prompt impératif → mode conformité (cocher des cases).
- Prompt interrogatif → mode raisonnement (engager la matière).

---

## Calibration stylistique — Avant de raisonner

> Ces trois transformations s'appliquent à la prose du blueprint : réponses Q0-Q8, KO sentences, descriptions de sections dans les blocs A/B/C. Le blueprint n'est pas publié, mais sa clarté conditionne la qualité de la Phase 3.

**Transformation 1 — Connecteurs → Asyndète**
❌ « En effet, le rapport montre que la thèse T3 est la plus solide. Par ailleurs, les surprises confirment cette orientation. »
✅ « La thèse T3 absorbe le plus de faits. Les surprises la renforcent. »
*Principe : supprimer les connecteurs logiques. Laisser la ponctuation et l'ordre des phrases porter le raisonnement.*

**Transformation 2 — Périphrase → Densité**
❌ « C'est une tension qui structure l'ensemble du matériau. »
✅ « Cette tension structure le matériau. »
*Principe : remplacer « C'est un X qui... » par une construction directe. Le raisonnement gagne en densité.*

**Transformation 3 — Flou → Précision**
❌ « Le rapport suggère que le verrou est à la fois institutionnel et culturel. »
✅ « Le rapport Phase 2 documente un verrou institutionnel (4 articles, 237 ans). Il suggère aussi un verrou culturel (indifférence à 12x). Les deux ne sont pas au même niveau de preuve. »
*Principe : distinguer ce qui est documenté de ce qui est inféré. Ne pas aplatir les niveaux de certitude.*

---

## Questions de raisonnement (répondre dans l'ordre)

Chaque réponse : 1 à 5 phrases maximum. Pas de listes exhaustives. Pas de copie du rapport. **Reformuler avec ses propres mots.**

> **Note sur l'ordre.** Les questions sont un guide, pas un carcan. Le raisonnement peut les fusionner, les réordonner, ou en sauter certaines si la matière le justifie. L'objectif est le raisonnement, pas la conformité à un format.

### Q0. Le sujet et le mode

Quel est le **sujet** de l'article ? Pas l'angle, pas la thèse : le **sujet**. La chose dont parle l'article. Formuler en une phrase : « Cet article porte sur X. »

Puis : le sujet exige-t-il le **mode essai** (un angle, une thèse, une sélection radicale) ou le **mode enquête** (présenter le sujet dans toutes ses dimensions, orchestrer le corpus) ?

> Critère : si le sujet est un mécanisme précis (un verrou, une capture, un échec), le mode essai convient. Si le sujet est un **concept** ou une **institution** (le RIC, la justice, la dette), le mode enquête s'impose. En cas d'ambiguïté (le sujet est à la fois un mécanisme et un concept), préférer le mode enquête si le corpus couvre ≥3 dimensions distinctes du sujet. Le mode enquête ne supprime pas la thèse : il la généralise en **thèse organisatrice** qui structure l'ensemble sans exclure les dimensions.

### Q1. Le fait qui surprend

Parmi tout le matériau (rapport + quintessences), quel est le fait qui surprend le plus un lecteur informé ? Pas le fait le plus documenté : le fait le plus **inattendu**. Celui qui force à reconsidérer ce qu'on croyait savoir.

> Exemple générique : « 73% des citoyens veulent X, mais X arrive à <5% dans leurs priorités. L'écart est de 12x. Ce n'est pas l'opposition qui verrouille : c'est l'indifférence. »

### Q2. La tension dramatique

Quelle contradiction interne au matériau est la plus productive ? Quelle tension, si on la tend au maximum, produit la révélation ? La tension n'est pas un problème à résoudre : c'est le moteur du récit.

> Exemple générique : « Le verrou est constitutionnel (4 articles, 237 ans) ET culturel (indifférence de 73% des favorables). Les deux se renforcent, mais lequel est la cause et lequel est le symptôme ? »

### Q3. La thèse (essai) ou la thèse organisatrice (enquête)

**Mode essai.** Les 5 thèses du rapport sont analytiques (chacune décrit un cluster). Un article en a une. Laquelle, si elle est vraie, rend les autres secondaires ? Laquelle **subsume** les autres ? Formuler en **une phrase**.

**Mode enquête.** Les 5 thèses du rapport sont les **dimensions** du sujet. La thèse organisatrice est le **fil qui les relie** sans en exclure aucune. Formuler en une phrase : « Le sujet X se comprend comme [relation entre les dimensions]. » La thèse organisatrice ne sélectionne pas : elle **hiérarchise**.

> Exemple générique (essai) : « Le RIC n'est pas verrouillé par la Constitution : il est verrouillé par l'indifférence de ceux qui le veulent, et la Constitution n'a pas besoin de faire mieux. »
>
> Exemple générique (enquête) : « Le RIC est un instrument de démocratie directe dont l'absence en France s'explique par un verrouillage multi-couches (constitutionnel, culturel, supranational) que 237 ans d'histoire n'ont pas entamé. »

### Q4. L'angle

Si cet article était un film, quel serait son genre ? L'angle n'est pas « forensique » (générique). L'angle est un **engagement spécifique** qui contraint le ton, le rythme, la structure, la voix.

Catalogue d'angles (non exhaustif, combinables) :
- **Autopsie** : le sujet est mort, on cherche la cause du décès.
- **Procès** : deux camps s'affrontent, le lecteur est le jury.
- **Enquête policière** : on remonte une chaîne causale depuis le fait brut.
- **Voyage dans le temps** : on traverse une durée longue pour montrer la continuité.
- **Contre-enquête** : on prend une opinion dominante et on la démonte.
- **Anatomie** : on dissèque une structure pour montrer ses pièces.
- **Paradoxe** : on part d'une contradiction et on la résout par profondeur.
- **Fresque** : on présente un sujet dans toutes ses dimensions, en vastes panneaux successifs (mode enquête).

### Q5. L'arc narratif

**Mode essai.** Quel est le **moment de bascule** ? Où le lecteur comprend qu'il ne s'agit pas de ce qu'il croyait ? L'arc en 3-5 mouvements : setup, tension, révélation, conséquence, question ouverte.

**Mode enquête.** L'arc est une **progression cognitive** : le lecteur entre avec une idée vague du sujet, et sort avec une compréhension systémique. Décrire la progression en 3-7 mouvements. Exemple de progression pour un sujet institutionnel : (1) qu'est-ce que c'est ? (2) que change-t-il ? (3) où fonctionne-t-il ? (4) pourquoi pas ici ? (5) qui paie le prix ? (6) que reste-t-il ? La progression réelle dépend du sujet et des dimensions du corpus. Le nombre de mouvements correspond au nombre de dimensions du sujet.

### Q6. Que couper (essai) ou Comment orchestrer (enquête)

**Mode essai.** Nommer les **5-10 quintessences essentielles** (celles sans lesquelles l'article s'effondre). Nommer explicitement **ce qui est coupé** et pourquoi. **Règle stricte : l'article final ne doit mobiliser que les quintessences nommées ici.** La coupe n'est pas une perte : c'est ce qui donne du relief à ce qui reste.

**Mode enquête.** Cartographier le corpus entier en trois niveaux :
- **Quintessences-phares** (5-12) : celles qui portent une section dédiée.
- **Quintessences-appui** (10-20) : celles qui fournissent un fait, une citation, un chiffre dans une section portée par une phare.
- **Quintessences-contexte** (restantes) : celles mentionnées en transition, en note contextuelle, ou regroupées avec une phare.

L'orchestration n'inclut pas tout verbatim : elle **structure** tout. Chaque quintessence trouve sa place dans l'architecture. Aucune n'est ignorée, mais toutes ne reçoivent pas le même traitement.

> Justifier chaque coupe (essai) ou chaque niveau (enquête) en une phrase.

### Q7. Les KO sentences

Quelles sont les **5-10 phrases** qui frappent comme des coups ? Courtes (≤15 mots), définitives, inattendues. Le lecteur doit s'arrêter de lire pour les absorber. Compter 1-2 KO sentences par section, adapté au nombre de sections.

Les KO sentences ne sont pas des conclusions. Ce sont des **constats** qui retournent une assumption.

> Exemple générique : « Le filet n'existait pas. » / « L'opinion est libre, la Constitution ne l'est pas. » / « Le verrou ne tue pas les porteurs : il structure leur turnover vers l'inertie. »

### Q8. La question ouverte

Quelle question l'article laisse-t-il en suspens ? Pas une réponse : une **question qui habite** après la lecture.

L'article qui donne une réponse est oublié. L'article qui laisse une question est partagé.

> Exemple générique : « Si 73% des Français veulent le RIC mais ne le priorisent pas, à qui exactement manque-t-il ? »

---

## Sortie : Blueprint narratif

Produire `investigations/<sujet>/_synthese/blueprint_narratif.md` avec 3 blocs :

### Bloc A — Matrice de décision narrative

| Dimension | Options considérées | Choix | Justification (1 phrase) |
|-----------|---------------------|-------|--------------------------|
| Thèse unique | T1 / T2 / T3 / T4 / T5 / synthèse | ... | ... |
| Angle | ... | ... | ... |
| Structure | chronologique / dramatique / comparative / paradoxale | ... | ... |
| Ton | ... | ... | ... |
| Public | ... | ... | ... |

### Bloc B — Plan article (arc narratif)

Pour chaque section (§0 à §N) :

- **Mode essai** : 5-7 sections maximum.
- **Mode enquête** : 6-12 sections. Chaque dimension du sujet peut recevoir sa section. Les sections peuvent être regroupées en parties (I, II, III) si le sujet s'y prête.

```
§N — [titre de section, pas de numéro technique]
      Rôle narratif : [setup / tension / révélation / conséquence / ouverture / dimension]
      Résumé : [2-3 phrases : ce que la section fait au lecteur]
      KO sentence : [1 phrase qui frappe]
      Faits mobilisés : [3-8 F-##]
      Quintessences source : [1-5 noms : phares et appui]
      À couper dans cette section : [ce qui pourrait tenter mais qu'il faut résister]
```

Chaque section sert l'arc. Pas de section encyclopédique qui ne sert pas la progression cognitive. Si une section n'avance pas la compréhension du sujet, la couper ou la fusionner.

### Bloc C — Liste de coupe (essai) ou Cartographie du corpus (enquête)

**Mode essai :**

```
Quintessences coupées (avec raison) :
- fiche_X : [raison en 1 phrase]
- ...

Quintessences gardées (avec rôle narratif) :
- fiche_X : [rôle : surprise / preuve / tension / contrefactuel / incarnation]
- ...
```

**Mode enquête :**

```
Quintessences-phares (section dédiée) :
- fiche_X : [section destinée + rôle narratif]
- ...

Quintessences-appui (fait/citation dans section phare) :
- fiche_X : [section d'appui + apport spécifique]
- ...

Quintessences-contexte (transition/note contextuelle) :
- fiche_X : [mention contextuelle]
- ...
```

---

## Contraintes

1. **Zéro hallucination.** Tout vient du rapport Phase 2 ou des quintessences lues.
2. **Une thèse, pas cinq.** La thèse unique doit tenir en une phrase. Si elle ne tient pas, le raisonnement n'est pas terminé.
3. **L'angle est un engagement.** Pas « forensique » (générique). Un angle spécifique qui contraint l'écriture.
4. **L'arc n'est pas un plan.** Un plan liste. Un arc transforme. Le lecteur doit arriver ailleurs qu'il n'est parti.
5. **La coupe ou l'orchestration est l'acte d'auteur.** En mode essai : si tout est inclus, rien n'est choisi. En mode enquête : si tout est cité également, rien n'est approfondi. L'orchestration hiérarchise le traitement (phares, appui, contexte) sans ignorer aucune dimension.
6. **Les KO sentences sont des constats, pas des jugements.** Pas d'imputation d'intention. Pas de pathos. Des faits retournés.
7. **La question ouverte n'est pas une conclusion.** C'est une absence qui reste.
8. **Zéro em-dash.** Utiliser « : », « - », parenthèses.
9. **VÉRIFIABILITÉ DES KO SENTENCES.** Toute KO sentence doit être directement vérifiable depuis le rapport Phase 2 SANS inférence intermédiaire. Une KO sentence qui contient « propagande », « zéro », « jamais », ou « tous » sans que le rapport Phase 2 n'établisse DIRECTEMENT ce fait est un drapeau rouge. Règle : si un lecteur peut répondre « pas exactement » ou « c'est plus compliqué » à une KO sentence, la reformuler.
10. **DISTINCTION DES NIVEAUX PROBATOIRES.** Distinguer systématiquement entre six niveaux : (1) relations institutionnelles documentées, (2) dépendances financières potentielles, (3) influence éditoriale observée, (4) coordination démontrée, (5) intention imputée, (6) effet mesuré sur le public. Ne jamais sauter de (1) à (5) ou (6) en une phrase. Si le rapport Phase 2 ne dépasse pas le niveau (2), le blueprint ne peut pas affirmer les niveaux (3)-(6).
  **Lexique de gradation** (pour distinguer les niveaux dans la prose du blueprint) : « est documenté par »/« établit que » (niveau 1), « corrobore »/« converge vers » (niveau 2), « suggère que » (niveau 3), « est compatible avec l'hypothèse que » (niveau 4), « rien n'exclut que »/« pourrait indiquer que » (niveau 5), « X affirme sans preuve publique que »/« selon une source unique non recoupée » (niveau 6). Interdiction : utiliser « démontre » ou « prouve » pour les niveaux 2-6.
11. **USAGE DU MOT « PROPAGANDE ».** Si le mot « propagande » apparaît dans les KO sentences ou le §7, le blueprint doit expliciter quels critères spécifiques sont satisfaits par le matériau Phase 2 : sélection systématique des faits dans une direction persuasive, asymétrie stable des statuts de parole, procédés narratifs de dramatisation, éviction d'explications concurrentes pertinentes, finalité de mobilisation ou de légitimation identifiable. Si ≥3 de ces critères ne sont pas documentés dans le rapport, remplacer « propagande » par « produit de cadrage de la menace » ou « documentaire inscrit dans un écosystème aux dépendances documentables. »
12. **PROPRETÉ DE LA LANGUE.** Proscrire les anglicismes : « implémenter » → « mettre en œuvre », « digital » → « numérique », « adresser » → « traiter », « basé sur » → « fondé sur », « focus » → « centrer »/« privilégier ». Proscrire les tics LLM : « Il est important de noter que », « D'une part... d'autre part », « Force est de constater que », « C'est un X qui... » (remplacer par construction directe).
13. **RYTHME DU RAISONNEMENT.** Dans les réponses Q0-Q8 et les KO sentences : supprimer ≥50 % des connecteurs logiques (asyndète). La logique est portée par la ponctuation et l'ordre des phrases, pas par des « En effet »/« Ainsi ». Varier la longueur : alterner phrases denses (20-30 mots) et phrases courtes (5-12 mots).

---

## Renvoi canonique

- **Phase 1 amont** : `tools/engines/sublimator/prompt-v36.md` (quintessences).
- **Phase 2 amont** : `tools/engines/sublimator/prompt-v37_phase2.md` (rapport de synthèse, fourni en entrée).
- **Phase 2.5 (ce prompt)** : raisonnement narratif, produit le blueprint.
- **Phase 3 aval** : `tools/engines/sublimator/prompt-v38_phase3.md` (rédaction d'article, consomme le blueprint).

### Fichier produit

```
investigations/<sujet>/_synthese/
  rapport_synthese_phase2.md      # Phase 2 (amont, existant)
  blueprint_narratif.md           # Phase 2.5 (ce prompt, nouveauté)
```

---

## Checkpoint CP1.5 (humain)

Le blueprint est présenté à l'utilisateur qui peut :
- **V** (valider) : passer à Phase 3 (`prompt-v38_phase3.md`) avec le blueprint comme entrée.
- **M** (modifier) : indiquer quelle dimension ajuster (thèse, angle, arc, coupe).
- **R** (refuser) : re-sélectionner les quintessences d'entrée (rare).
- **E** (explorer) : tester un angle alternatif, une thèse concurrente.

**Une seule passe.** Pas de régénération sans action humaine.

### Passe de serrage (avant écriture du blueprint)

Avant d'écrire le fichier `blueprint_narratif.md`, relire les réponses Q0-Q8 et les KO sentences. Appliquer une passe rapide :
1. Supprimer les connecteurs superflus (asyndète).
2. Raccourcir toute phrase de ≥25 mots.
3. Vérifier que chaque KO sentence est vérifiable sans inférence (Contrainte 9).
4. Vérifier que le lexique de gradation est utilisé correctement (Contrainte 10).
5. Supprimer anglicismes et tics (Contrainte 12).

---

**Fin du prompt Phase 2.5.** Volumétrie cible du blueprint : 800-1500 mots (mode essai) ou 1200-2500 mots (mode enquête, car la cartographie du corpus est plus volumineuse). Le blueprint décide et orchestre ; il ne démontre pas. La démonstration est le travail de la Phase 3.
