# ADDENDA — Cinq biais non identifiés par le corpus : survivorship, publication, confirmation structurel, performance = paralysie, franco-généralisation

**Type :** `ADDENDA` | **Date :** 2026-06-11 | **Cible :** SUSPICION_SCORE de l'ensemble du corpus

---

## §1 PRÉAMBULE

Le corpus Truth Engine excelle dans l'auto-critique : chaque investigation de type APEX, INVESTIGATION ou SOLUTIONS intègre une section SUSPICION_SCORE qui liste les biais de son propre raisonnement. Ces auto-audits couvrent le biais IRA-centré, le biais occidental, le biais déterministe, le biais militant, le biais zapatophile — une trentaine de biais documentés sur l'ensemble des fichiers.

Cependant, cinq biais systémiques traversent le corpus sans jamais être nommés. Ils ne sont pas des omissions accidentelles — ils sont structurels, c'est-à-dire produits par la méthode d'enquête elle-même. Cet addenda les identifie, les documente, et propose une recalibration globale du SUSPICION_SCORE.

---

## §2 BIAIS #1 — SURVIVORSHIP BIAS (Biais de survie)

**Définition** : Le survivorship bias (biais de sélection par la survie) consiste à n'étudier que les cas qui ont « réussi » ou duré assez longtemps pour être documentés, en ignorant les cas qui ont échoué silencieusement. Les Zapatistes, Solidarnosc, l'IRA, le FLN, le LTTE, les FARC — tous ont duré assez longtemps pour produire des archives, des analyses académiques, des articles de presse. Les centaines de groupes armés ou mouvements sociaux morts en six mois, sans jamais atteindre cinquante membres, sans laisser de trace écrite, sont invisibles. L'échantillon est biaisé par construction.

**Manifestation dans le corpus** :
- P8 (CAS) étudie 6 mouvements armés ayant duré plus de 10 ans — 0 mouvement mort en phase de formation.
- P13-DÉFAITE analyse 4 échecs (LTTE, ETA, FARC, PKK) — mais tous ont duré 25 à 60 ans. La défaite après 25 ans n'est pas la même que la défaite après 6 mois.
- VERROU cite 6 cas historiques de coordination — tous choisis parce qu'ils ont laissé des traces.
- ACE analyse Solidarnosc, Zapatistes, Hong Kong — trois cas de « réussite » relative.

**Fichiers affectés** : P8, P13-DÉFAITE, VERROU, ACE, SOLUTIONS

**Impact** : FORT — Le survivorship bias gonfle artificiellement la conclusion que « la durée est possible ». Si l'on incluait les milliers de groupes morts en silence, la probabilité de survie tomberait de 100 % (6/6) à moins de 1 %.

**Correction proposée** : Ajouter une strate « fantôme » au FACT_REGISTRY : des cas non documentés, estimés par extrapolation. Tout taux de succès observé doit être divisé par un facteur de correction estimé à >50x.

---

## §3 BIAIS #2 — PUBLICATION BIAS (Biais de publication)

**Définition** : Le publication bias désigne la sur-représentation des cas documentés dans les langues et les formats accessibles aux chercheurs. Tous les cas du corpus sont documentés en français ou en anglais, par des académiciens occidentaux, dans des revues accessibles via les bases de données du Nord global. Les mouvements non-occidentaux dont la littérature est orale, en langue locale, ou non indexée sont exclus.

**Manifestation dans le corpus** :
- Les 12 mécanismes d'OLI sont documentés via des sources françaises et américaines (Milgram, Asch, Zimbardo, Debord, Chomsky).
- Les cas historiques d'ACE sont tous occidentaux ou occidentalo-centrés (Pologne, Mexique, Hong Kong sous influence britannique).
- La fresque systémique ignore les mécanismes de contrôle équivalents dans les cultures non-occidentales (guanxi en Chine, wasta au Moyen-Orient, jeitinho au Brésil).
- Les mouvements camerounais anglophones, ouïghours, rohingyas, cachemiris sont absents — non par négligence mais par absence de littérature accessible.

**Fichiers affectés** : TOUS (systémique)

**Impact** : FORT — Le publication bias verrouille la prétention à l'universalité du corpus. Ce qui est présenté comme « les mécanismes du verrouillage » est en réalité « les mécanismes du verrouillage tels que documentés par la recherche occidentale ». Les mécanismes équivalents dans d'autres aires culturelles sont inconnus, donc non intégrés.

**Correction proposée** : Marquer chaque mécanisme avec un indice de couverture géographique (Europe, Amériques, Asie, Afrique, Océanie). Un mécanisme documenté sur 1/5 continents reçoit un indice de généralisabilité de 0,2. Un indice agrégé du corpus donnerait aujourd'hui ~0,35.

---

## §4 BIAIS #3 — BIAIS DE CONFIRMATION STRUCTUREL

**Définition** : Le biais de confirmation n'est pas ici un biais individuel — c'est un biais structurel inscrit dans la question de recherche. Toute l'enquête du corpus part de la prémisse « existe-t-il des solutions ? » ou « pourquoi les mouvements échouent-ils ? ». Cette question prédétermine la réponse : elle présuppose qu'il y a quelque chose à corriger. Si la question de départ avait été « pourquoi certains mouvements réussissent-ils ? », les cadres d'analyse auraient été différents.

**Manifestation dans le corpus** :
- L'enquête DEFEAT demande « pourquoi les mouvements armés échouent-ils ? » — et trouve 6 raisons. Si elle avait demandé « pourquoi certains mouvements armés survivent-ils ? », elle aurait trouvé la variable sanctuaire (P8).
- OLI demande « comment le système verrouille-t-il la coordination ? » — et trouve 12 mécanismes. Si elle avait demandé « quelles sont les failles du système ? », elle aurait trouvé autre chose.
- Les SOLUTIONS sont construites comme réponses à un problème posé. La circularité est parfaite : le problème détermine la solution.

**Fichiers affectés** : TOUS (méta-systémique)

**Impact** : FORT — Le biais de confirmation structurel est le plus difficile à corriger car il est inscrit dans la méthode. La seule correction est de produire une enquête sœur qui inverse la question : « qu'est-ce qui marche ? », sans préjuger que le système doit être abattu.

**Correction proposée** : Ajouter une investigation complémentaire intitulée « Ce qui marche » — analysant les réussites de coordination non pas comme exceptions à un échec général mais comme phénomènes à part entière.

---

## §5 BIAIS #4 — PERFORMANCE = PARALYSIE

**Définition** : Le corpus produit 13 479 lignes d'analyse de l'impossibilité d'agir. Chaque ligne supplémentaire démontre la lucidité de l'enquêteur mais reproduit la paralysie qu'elle décrit. Le métabolème central est : plus on analyse le verrou, plus on s'y enferme. Le corpus est un symptome du mal qu'il prétend guérir.

**Manifestation dans le corpus** :
- OLI (669 lignes) décrit 12 mécanismes — zéro prescription opérationnelle.
- VERROU (954 lignes) analyse 12 clusters de verrouillage — le seul fichier qui prescrit le fait sur 4 pages sur 15.
- SOLUTIONS (479 lignes) propose un modèle non testé — zéro mètre carré d'autonomie réelle construit.
- SYNTHÈSE (221 lignes) résout la contradiction OLI/ACE sur le papier mais ne produit aucune action.
- Le fichier le plus long du corpus (ACE, ~1 200 lignes) analyse l'action acéphalique — sans jamais en lancer une.

**Fichiers affectés** : TOUS (méta-systémique)

**Impact** : FORT — Le biais est nommé dans l'audit (« boucle de lucidité paralysante ») mais jamais intégré dans un SUSPICION_SCORE. Le corpus sait qu'il est paralysant mais n'en tire pas la conséquence méthodologique : arrêter d'écrire, commencer à faire.

**Correction proposée** : Imposer une règle de « ratio action/analyse » : tout fichier de plus de 300 lignes doit inclure un protocole testable en moins de 7 jours. À défaut, le fichier est marqué SPECULATIF et son SUSPICION_SCORE ne peut pas dépasser 4/10.

---

## §6 BIAIS #5 — FRANCO-GÉNÉRALISATION

**Définition** : Le corpus utilise la France comme cas d'étude principal mais présente ses résultats comme universels. Les mécanismes spécifiquement français (article 450-1 du Code pénal, LOPMI, BAC, TRACFIN, comparaison exclusive avec le Benelux) sont théorisés comme des lois générales du verrouillage.

**Manifestation dans le corpus** :
- OLI mentionne les 12 mécanismes comme s'ils étaient universels — mais ils sont documentés via des sources françaises et américaines.
- P1-P9 sont construits autour du cadre légal français.
- SOLUTIONS compare le modèle zapatiste au contexte français sans calibrer pour d'autres contextes.
- Le Benelux est cité comme seul terme de comparaison juridique (PX-DROIT-COMPARE).
- Les mécanismes non-français (guanxi, wasta, jeitinho, ubuntu) sont absents.

**Fichiers affectés** : OLI, P1-P9, SOLUTIONS

**Impact** : MOYEN — La franco-généralisation est partiellement corrigée par l'inclusion de cas internationaux (Zapatistes, Solidarnosc, LTTE, FARC). Mais le cadre d'analyse reste franco-centré. Un enquêteur indien ou brésilien produirait un corpus différent.

**Correction proposée** : Marquer chaque fichier avec un indice de généralisabilité (France-seulement / Europe / Occident / Global). Les conclusions des fichiers marqués France-seulement ne devraient pas être extrapolées sans cette mention explicite.

---

## §7 FAISCEAUX — Connexions aux fichiers affectés

| Faisceau | Biais | Fichiers connectés |
|----------|-------|---------------------|
| ADDENDA + P8 | Survivorship : les 6 cas armés de P8 ont tous duré >10 ans — les centaines de groupes morts en 6 mois sont invisibles | P8-CAS, P13-DÉFAITE |
| ADDENDA + VERROU | Survivorship : les 6 cas historiques de VERROU sont choisis car documentés — les coordinations mort-nées sont absentes | VERROU |
| ADDENDA + ACE | Survivorship + publication : Solidarnosc, Zapatistes, HK sont des cas documentés en anglais — les milliers d'échecs et les cas non-occidentaux sont absents | ACE |
| ADDENDA + OLI | Publication : 12 mécanismes documentés via sources occidentales — les mécanismes non-occidentaux sont absents | OLI-001 |
| ADDENDA + SYNTHÈSE | Performance = paralysie : la synthèse résout la contradiction OLI/ACE sur le papier sans produire d'action — c'est le biais qu'elle documente sans le nommer | SYNTHÈSE |
| ADDENDA + SOLUTIONS | Franco-généralisation : le modèle zapatiste est calibré pour la France sans test dans d'autres démocraties occidentales | SOLUTIONS |
| ADDENDA + P3 (FERMETURE) | Confirmation structurel : la question « comment fermer le système ? » prédétermine la réponse — une question sur ses faiblesses donnerait d'autres résultats | P3-FERMETURE |

---

## §8 FACT_REGISTRY

| ID | Fait | Fiabilité | Source |
|----|------|:---------:|--------|
| F-ADD-001 | Les 6 mouvements armés étudiés par P8 ont tous duré >10 ans — taux de survie observé 100 % d'un échantillon biaisé par construction | ✧ | Analyse enquêteur |
| F-ADD-002 | Les 12 mécanismes d'OLI sont documentés via 18 sources dont 16 occidentales (France/USA) — indice de couverture géographique ~0,35/1,0 | ✦ | OLI §12 |
| F-ADD-003 | Tous les fichiers du corpus partent de la question « pourquoi ça échoue ? » — aucun ne part de « qu'est-ce qui marche ? » | ✦ | Analyse transversale |
| F-ADD-004 | Le corpus totalise 13 479 lignes d'analyse — 0 protocole testé en conditions réelles | ✧ | Audit corpus |
| F-ADD-005 | Les mécanismes spécifiquement français (art.450-1, LOPMI, TRACFIN) sont présentés comme universels sans indice de généralisabilité | ✦ | P10-RISQUE, P4, OLI |

---

## §9 SUSPICION_SCORE — Recalibration globale du corpus

### État actuel

Le score composite moyen du corpus est d'environ **5,2/10** (moyenne des SUSPICION_SCORE de chaque fichier APEX, INVESTIGATION et SOLUTIONS).

### Impact des 5 nouveaux biais

| Biais | Coefficent de correction | Justification |
|-------|:-----------------------:|---------------|
| Survivorship | -0,30 | Gonflement artificiel des taux de succès observés — tous les ratios doivent être divisés |
| Publication | -0,15 | Ampleur modérée car le corpus utilise des sources vérifiées, mais la couverture géographique est faible |
| Confirmation structurel | -0,10 | Correction modérée — le biais est partiellement compensé par la diversité des questions du corpus |
| Performance = paralysie | -0,15 | Ce biais est le plus grave car il touche la raison d'être du corpus : produire de l'action |
| Franco-généralisation | -0,10 | Correction modérée — le corpus inclut des cas non-français mais le cadre d'analyse reste franco-centré |

### Score recalibré

**Corpus average avant : 5,2/10**
**Correction totale : -0,80**
**Corpus average après : 4,4/10**

### Conséquence méthodologique

Un score de 4,4/10 place le corpus en zone « spéculatif avec fondements ». Les conclusions ne doivent pas être traitées comme des vérités mais comme des hypothèses de travail. La recommandation est la suivante : tout fichier qui n'atteint pas 5/10 après recalibration doit inclure un avertissement explicite en tête de document : « Ce fichier a un SUSPICION_SCORE inférieur à 5/10. Ses conclusions ne doivent pas être citées sans cette mention. »

### Biais de cet addenda

Cet addenda n'échappe pas à ses propres biais :
1. **Biais correcteur** : la tendance à sur-corriger les biais identifiés — le score de 4,4/10 est peut-être trop bas par réaction.
2. **Biais rétrospectif** : les 5 biais sont identifiés après coup — ils paraissent évidents maintenant qu'ils sont nommés, mais ils ne l'étaient pas pendant la rédaction.
3. **Biais d'exhaustivité illusoire** : ces 5 biais ne sont probablement pas les seuls — d'autres biais systémiques restent non identifiés.
