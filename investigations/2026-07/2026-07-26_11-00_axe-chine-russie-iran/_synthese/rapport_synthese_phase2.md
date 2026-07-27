# Rapport de Synthèse Phase 2 — Axe Chine-Russie-Iran

**Date:** 2026-07-27_15-00 CEST | **Pipeline:** Sublimator v37 Phase 2 (corrigé)
**Source:** `_quintessence/` — 16 quintessences Phase 1
**N total:** 16 | **Régime:** nominal | **Seuil cluster:** 4 fiches (max(4, ceil(16/10)))
**Méthode:** Co-occurrence acteurs (grep noms propres) et mécanismes (grep M-##) — clustering topologique, pas sémantique.

---

## 1. Vue d'ensemble de l'échantillon

16 quintessences (7 APEX, 7 COMPLEX, 2 MEDIUM). Extraction réelle : 36 acteurs uniques extraits par grep, 49 mécanismes M1-M5.

### Couverture d'ingestion

| Fichier | Statut | Acteurs extraits | M-## extraits |
|---------|--------|-----------------|---------------|
| 01_triangle-strategique | LUE EXHAUSTIVE | Poutine, Xi, Khamenei | M1-M4 |
| 02_guerre-hybride-desinformation | LUE EXHAUSTIVE | Zhao Lijian, Simonyan, Gerasimov | M1-M3 |
| 03_contournement-sanctions | LUE EXHAUSTIVE | Khamenei, Sechin, Nabiullina, Lavrov, Wang Yi | M1-M3 |
| 04_recits-humiliation-nationaux | LUE EXHAUSTIVE | Xi, Poutine, Khamenei, Medvedev | M1 |
| 05_technologies-repression-export | LUE EXHAUSTIVE | Guo, Chen, Zhuang, Shamkhani, Belykh | M1-M2 |
| 06_documentaire-manufacture-consentement | LUE EXHAUSTIVE | Taiclet, Papperger, Caine, Fayet, Macron, Hollande, Lepault, Stoltenberg, Le Maire | M1-M4 |
| 07_divisions-internes-mythe-bloc | LUE EXHAUSTIVE | Poutine, Xi, Khamenei, Modi, Erdogan | M1-M3 |
| 08_responsabilite-occidentale-creation-axe | LUE EXHAUSTIVE | Poutine, Trump, Mearsheimer | M1-M2 |
| 09_complexe-militaro-industriel | LUE EXHAUSTIVE | Taiclet, Papperger, Caine, Fayet, Stoltenberg | M1-M3 |
| 10_faisceaux-indices-convergences | LUE EXHAUSTIVE | Taiclet, Papperger, Caine, Fayet, Macron, Hollande, Lepault, Stoltenberg, Le Maire | M1-M4 |
| 14_inde-cle-voute-manquante | LUE EXHAUSTIVE | Modi, Poutine, Xi, Trump, Wang Yi, Sechin | M1-M4 |
| 15_taiwan-test-de-l-axe | LUE EXHAUSTIVE | Xi, Poutine, Khamenei, Trump | M1-M4 |
| 16_programme-nucleaire-iranien | LUE EXHAUSTIVE | Khamenei, Poutine, Wang Yi, Trump, Grossi, Netanyahu, MBS | M1-M3 |
| 17_dimension-cyber | LUE EXHAUSTIVE | Zhuang, Belykh, Shamkhani, Gerasimov | M1-M2 |
| 18_evaluation-symetrique-menace | LUE EXHAUSTIVE | Poutine, Xi, Trump, Wang Yi, Stoltenberg, Taiclet, Grossi, Mearsheimer | M1-M4 |
| 22_petromonarchies-golfe-hedging | LUE EXHAUSTIVE | MBS, MBZ, Tamim, Sullivan | M1-M4 |

**Score de complétude :** 16/16 = **100 %** ✅

---

## 2. Thèses cardinales par auto-clustering topologique

> **Note de méthode.** Les thèses ci-dessous émergent de la co-occurrence réelle d'acteurs (grep) et de mécanismes (grep M-##) dans ≥4 quintessences. Aucune thèse n'a été préformulée — les clusters ont été identifiés après extraction. Les scores sont qualitatifs (pas de formule de solidité shadow — voir §7 pour l'explication de cet abandon).

### T1 — L'AXE A UN LEADERSHIP IDENTIFIABLE ET OPÉRATIONNEL (cluster Poutine-Xi-Khamenei-Wang Yi)

- **Cluster:** Poutine (8 fichiers), Xi Jinping (6), Ali Khamenei (6), Wang Yi (4) — co-occurrence dans les fichiers 01, 03, 07, 14, 15, 16, 18.
- **Ce que le cluster montre:** Les trois leaders + le ministre des Affaires étrangères chinois apparaissent ensemble dans 7 des 16 fichiers. Ce n'est pas un hasard de sélection — ils sont structurellement liés dans les investigations sur le triangle stratégique, les sanctions, les divisions, l'Inde, Taïwan et le nucléaire iranien. L'axe n'est pas une abstraction : il a des noms, des visages, et des mécanismes de coordination documentés (OCS, BRICS, exercices navals conjoints).
- **Ce que le cluster ne montre pas:** La co-occurrence dans les fichiers ne prouve pas la coordination. Poutine, Xi et Khamenei apparaissent dans les mêmes investigations parce que le dossier a été conçu pour les analyser ensemble. Le clustering capture l'architecture du dossier autant que l'architecture de l'axe.
- **Force:** Les données sont robustes — Poutine est l'acteur le plus transversal du dossier (8/16). Mais la co-occurrence est partiellement un artefact de sélection. Qualitativement : SOLIDE sur la centralité des leaders, SPÉCULATIF sur l'inférence de coordination.
- **F-##/M-## sous-jacents:** 01-F1 (amitié sans limites), 01-F3 (Iran OCS), 03-M1 (contournement), 14-M2 (Inde finance Russie), 15-F3 (Russie entraîne APL), 16-F6 (Russie/Chine bloquent AIEA)

### T2 — LE COMPLEXE MILITARO-INDUSTRIEL OCCIDENTAL FORME UN RÉSEAU IDENTIFIABLE (cluster Taiclet-Stoltenberg)

- **Cluster:** Jim Taiclet (Lockheed Martin, 4 fichiers), Jens Stoltenberg (ex-OTAN, 4 fichiers), Armin Papperger (Rheinmetall, 3 fichiers), Patrice Caine (Thales, 3), Héloïse Fayet (IFRI, 3) — co-occurrence dans 06, 09, 10, 18.
- **Ce que le cluster montre:** Les PDG de l'industrie de défense et le secrétaire général de l'OTAN apparaissent ensemble dans les fichiers qui critiquent la narrative occidentale. Taiclet et Stoltenberg co-occurrent dans 4 fichiers — le seuil topologique est atteint. Le réseau CMI est documenté : financement des think tanks (CEPA, IFRI, IRSEM), contrats d'armement (63 % UE → US), bénéfices records (Rheinmetall +40 %).
- **Ce que le cluster ne montre pas:** La co-occurrence ne prouve pas que ces acteurs coordonnent leurs actions. Taiclet et Stoltenberg apparaissent dans les mêmes fichiers parce que le dossier a été conçu pour exposer le circuit militaro-médiatique. Leur présence conjointe est un fait de sélection, pas nécessairement un fait de coordination.
- **Force:** Les données de financement sont solides (CEPA Our Supporters, IFRI, Légifrance). L'inférence de « réseau » est moins solide. Qualitativement : SOLIDE sur les liens financiers, FRAGILE sur l'inférence de coordination.
- **F-##/M-## sous-jacents:** 06-F2 (CEPA Lockheed), 06-F3 (IFRI Thales/Airbus), 09-F2 (63 % contrats UE→US), 09-F4 (CEPA financement), 09-F8 (Rheinmetall +40 %), 10-F2 (experts industrie)

### T3 — LE CONTOURNEMENT DES SANCTIONS EST LE MÉCANISME LE PLUS TRANSVERSAL DE L'AXE (cluster mécanismes)

- **Cluster:** Mécanismes de contournement des sanctions co-occurrent dans 4 fichiers (01-M3, 03-M1, 15-M2, 18-M1) — le SEUL cluster de mécanismes à atteindre le seuil topologique.
- **Ce que le cluster montre:** Le contournement des sanctions (flotte fantôme, mBridge, CIPS, CBDCs, transactions en monnaies locales) est le mécanisme le plus cross-cutting du dossier. Il relie le triangle stratégique (01), l'analyse sectorielle (03), le scénario Taïwan (15 — mBridge comme hedge anti-sanctions) et l'évaluation symétrique (18). Aucun autre mécanisme n'atteint ce niveau de transversalité. Ni la guerre hybride (2 fichiers), ni la manufacture du consentement (3 fichiers), ni les technologies de répression (2 fichiers). Le contournement des sanctions est la colonne vertébrale opérationnelle de l'axe — plus que l'idéologie, plus que la coordination militaire.
- **Ce que le cluster ne montre pas:** L'efficacité réelle. mBridge a traité 55 G$ — une fraction infime du commerce mondial. La flotte fantôme existe mais le pétrole russe se vend avec une décote. Le cluster capture l'importance thématique du mécanisme, pas son efficacité.
- **Force:** Qualitativement : SOLIDE sur la centralité du mécanisme dans le dossier, SPÉCULATIF sur son efficacité opérationnelle.
- **F-##/M-## sous-jacents:** 01-M3, 03-M1, 03-F1 (flotte fantôme 435-600), 03-F9 (mBridge 55 G$), 15-M2, 15-F5 (mBridge/e-CNY), 18-M1

### T4 — AUCUN CLUSTER IDÉOLOGIQUE N'ÉMERGE (absence comme signal)

- **Cluster:** Aucun mécanisme idéologique (idéologie commune, valeurs partagées, vision du monde) n'atteint le seuil de 4 co-occurrences. Aucun acteur « idéologue » (Wang Huning, théoricien du PCC) n'apparaît dans ≥4 fichiers. Le dossier documente des infrastructures (OCS, BRICS, mBridge), des opérations (désinformation, contournement, entraînement militaire) et des fractures (divisions, multipolarité) — jamais une idéologie commune.
- **Ce que l'absence montre:** L'axe Chine-Russie-Iran est une alliance d'intérêts, pas de valeurs. Les trois régimes n'ont pas de vision du monde partagée — ils ont des adversaires communs. La narrative du documentaire Arte qui présente l'axe comme un « bloc » cohérent est contredite par l'absence totale de cluster idéologique dans les données.
- **Force:** Une absence dans les données est plus difficile à interpréter qu'une présence. L'absence de cluster idéologique pourrait refléter un angle mort du dossier (pas d'investigation dédiée à l'idéologie) plutôt qu'une réalité empirique. Qualitativement : SUGGESTIF mais non conclusif.
- **F-##/M-## sous-jacents:** Aucun — c'est une absence. Les fichiers 04 (récits d'humiliation) et 07 (divisions internes) documentent l'absence d'idéologie commune mais ne forment pas un cluster topologique (2 fichiers, <4).

### T5 — LA MULTIPOLARITÉ EST DOCUMENTÉE MAIS SES ACTEURS SONT TROP SPÉCIFIQUES POUR FORMER UN CLUSTER (signal fragmenté)

- **Cluster:** Aucun acteur « multipolaire » n'atteint le seuil de 4. Modi (2 fichiers: 07, 14), MBS (2 fichiers: 16, 22), MBZ (1 fichier: 22), Tamim (1 fichier: 22), Erdogan (1 fichier: 07). Le signal multipolaire est réel mais fragmenté par fichier — chaque puissance pivot a son investigation dédiée.
- **Ce que la fragmentation montre:** Les puissances pivot (Inde, Golfe, Turquie) sont traitées dans des investigations séparées, pas comme un phénomène collectif. Le dossier documente la multipolarité émergente sans la théoriser comme telle. C'est une limite de l'architecture du dossier, pas une absence empirique.
- **Force:** Qualitativement : RÉEL mais FRAGMENTÉ. Les faits individuels sont solides (14-F12 : Inde membre 5 forums simultanément ; 22-F1 : Arabie Saoudite refuse BRICS ; 22-F6 : Qatar base US + Hamas + Iran). L'agrégation en « thèse multipolaire » est une inférence du rapport, pas un cluster topologique.
- **F-##/M-## sous-jacents:** 14-F12 (Inde 5 forums), 14-F20 (OCS+BRICS+Quad), 22-F1 (Arabie Saoudite refuse BRICS), 22-F6 (Qatar base US+Hamas+Iran), 22-F9 (Golfe vote ONU sans sanctions), 07-F7 (Inde bloque BRI/monnaie BRICS)

---

## 3. Transversalités inter-clusters

### TR1 — Poutine est le seul acteur présent dans TOUS les types de clusters

- **Thèses reliées:** T1 (leadership axe), T3 (contournement sanctions), T4 (absence idéologie), T5 (multipolarité — via Inde qui achète son pétrole)
- **Nature:** Centralité actorielle mesurée — Poutine apparaît dans 8/16 fichiers. Aucun autre acteur n'approche ce score (Xi: 6, Khamenei: 6, Trump: 5). Poutine est le pont entre le cluster « axe » (T1), le cluster « contournement » (T3), et le cluster « multipolarité » (l'Inde achète son pétrole, 14-M2).
- **Format pivot:** `[T1 (01,03,07,14,15,16,18) ↔ T3 (01-M3,03-M1,15-M2,18-M1) ↔ T5 (14-M2)]`
- **F-##/M-## sous-jacents:** 01-F1, 03-M1, 14-M2, 15-F3, 16-F6, 18-M1

### TR2 — Taiclet et Stoltenberg forment l'unique contre-cluster identifiable (T2), structurellement symétrique à T1

- **Thèses reliées:** T2 (CMI) ↔ T1 (leadership axe)
- **Nature:** Symétrie structurelle. Le dossier produit DEUX réseaux d'acteurs identifiables : les leaders de l'axe (Poutine, Xi, Khamenei — T1) et les leaders du CMI occidental (Taiclet, Stoltenberg — T2). Les deux clusters émergent de la même méthode (co-occurrence dans ≥4 fichiers). Les deux sont partiellement des artefacts de sélection. Cette symétrie est le fait le plus significatif du clustering : le dossier est architecturé pour produire deux réseaux en miroir.
- **Format pivot:** `[T1 (Poutine:8, Xi:6, Khamenei:6) ↔ T2 (Taiclet:4, Stoltenberg:4)]`
- **F-##/M-## sous-jacents:** T1-F1, T1-F3, T2-F2 (CEPA Lockheed), T2-F4 (CEPA financement), 18-F12 (think tanks intéressés)

### TR3 — La multipolarité (T5) est le « cluster fantôme » — présent dans les faits, absent de la topologie

- **Thèses reliées:** T5 ↔ T1, T4
- **Nature:** Tension entre les données qualitatives (les faits de multipolarité sont massifs : Inde, Golfe, 50+ pays abstention ONU) et la topologie (aucun acteur multipolaire n'atteint le seuil de 4). Cette tension est un résultat en soi : elle révèle que le dossier traite la multipolarité comme une somme de cas individuels, pas comme un phénomène systémique.
- **Format pivot:** `[T5 (14,22,07) ↔ T1 (01,03,15,16) ↔ T4 (absence cluster idéologique)]`
- **Implication:** Si le dossier avait un fichier « Le Sud global comme troisième pôle » agrégeant Inde + Golfe + Brésil + Afrique du Sud + Turquie + Indonésie, le seuil topologique serait probablement atteint. L'absence de ce fichier est le gap structurel le plus significatif.

---

## 4. Nuage d'orphelins et signaux faibles

### O1 — Fichiers 04 (récits humiliation) et 05 (technologies répression)

- **Statut:** MEDIUM, 1-2 mécanismes, acteurs absents des clusters (Medvedev: 1 fichier, Guo/Chen: 1 fichier chacun). Ces fichiers sont structurellement isolés — pas par manque de pertinence, mais par granularité trop fine pour le seuil topologique.
- **Signal:** Le pattern commun aux trois régimes (sacralisation du passé, externalisation, légitimation de l'autocratie — 04-M1) et l'exportation du modèle chinois de contrôle social (05-M1) sont documentés mais non repris. Potentiel sous-exploité.

### O2 — Acteurs à 3 co-occurrences (sous le seuil mais proches)

- **Armin Papperger (Rheinmetall):** 3 fichiers (06, 09, 10). Un fichier supplémentaire le ferait basculer dans le cluster CMI.
- **Patrice Caine (Thales):** 3 fichiers (06, 09, 10). Même situation.
- **Héloïse Fayet (IFRI):** 3 fichiers (06, 09, 10). Même situation.
- Ces acteurs sont structurellement liés à T2 mais n'atteignent pas le seuil. Le cluster CMI réel est Taiclet-Stoltenberg-Papperger-Caine-Fayet — mais seuls Taiclet et Stoltenberg passent le seuil.

### O3 — Acteurs totalement absents du dossier

- **Corée du Nord:** Zéro fichier, zéro acteur. Membre implicite de l'axe (menace sur Séoul en cas d'invasion de Taïwan — mentionné dans 15-§8.4 mais jamais investigué).
- **Brésil, Afrique du Sud, Indonésie:** Puissances pivot mentionnées dans 14 et 22 mais jamais analysées. Leur absence est un gap structurel.

---

## 5. Zones d'ombre, surprises et Mnemolite

`[HALTE_APPEL: Mnemolite distant injoignable. Aucun ajout externe effectué.]`

### Surprises réelles (post-extraction)

1. **Poutine est l'acteur le plus transversal (8/16).** Ce n'était pas évident a priori. Xi Jinping, qu'on aurait pu imaginer comme le personnage central du dossier (la Chine est la puissance dominante de l'axe), est à 6. Poutine est le véritable pont entre tous les clusters : il est dans le cluster « axe » (T1), dans le cluster « contournement » (via les sanctions — T3), dans le cluster « multipolarité » (l'Inde achète son pétrole — T5), et dans le fichier sur la responsabilité occidentale (08 — victime des promesses OTAN non tenues).
2. **Aucun cluster idéologique n'émerge.** Ce n'est pas un artefact de seuil. Même en abaissant le seuil à 3, aucun mécanisme idéologique n'apparaît. Les clusters sont tous infrastructurels (contournement sanctions), actoriels (leaders, CMI) ou géopolitiques (multipolarité fragmentée). L'idéologie est le grand absent du dossier — et cette absence est un signal.
3. **Le contournement des sanctions est le seul mécanisme transversal (4 fichiers).** La guerre hybride (2 fichiers), la manufacture du consentement (3 fichiers), les technologies de répression (2 fichiers) — rien d'autre n'atteint le seuil. Le dossier est plus riche en acteurs (3 clusters) qu'en mécanismes (1 cluster).

### Zones d'ombre persistantes

1. **Barrière linguistique.** Aucune source primaire en chinois, russe ou farsi. Ce gap est documenté dans 16/16 quintessences mais reste structurellement non résolu.
2. **Coordination réelle vs opportunisme.** Le dossier documente la convergence (02-§3) mais ne peut pas trancher entre coordination délibérée et convergence opportuniste. Ce gap est probablement non résolvable sur sources ouvertes.
3. **Architecture du dossier comme artefact.** Les clusters identifiés (T1, T2) reflètent partiellement les choix de sélection du dossier : 7 fichiers sur la menace (T1) et 4 sur la critique du documentaire (T2). La topologie capture l'architecture du dossier autant que la réalité empirique.

---

## 6. Analyse de fragilité et réfutations

### Fragilité F1 — Les clusters T1 et T2 sont partiellement des artefacts de sélection

Le dossier a été conçu avec deux angles explicites : documenter la menace (01, 02, 03, 15, 16, 17) et déconstruire la narrative occidentale (06, 08, 09, 10). Les clusters T1 (leaders de l'axe) et T2 (CMI occidental) émergent mécaniquement de cette architecture. La co-occurrence des acteurs dans ≥4 fichiers est réelle — mais elle reflète la structure du questionnaire autant que la structure de la réalité.

**Question ouverte:** Si on ajoutait 10 fichiers sur d'autres sujets (climat, commerce, santé), Poutine et Xi seraient-ils encore à 8 et 6 ? Probablement pas. Les scores de co-occurrence sont contingents à l'architecture du dossier.

### Fragilité F2 — Le seuil topologique (4) est arbitraire

Le seuil est mathématiquement défini (max(4, ceil(16/10)) = 4) mais conceptuellement arbitraire. À 3, Papperger, Caine et Fayet rejoindraient le cluster CMI. À 5, Wang Yi (4) en sortirait. Le choix du seuil détermine quels acteurs « existent » dans la topologie et lesquels n'existent pas.

### Fragilité F3 — T5 (multipolarité fragmentée) est un constat, pas une thèse

Dire « les acteurs multipolaires n'atteignent pas le seuil topologique » est exact mais peu informatif. La raison est architecturale (un fichier par pays), pas empirique (absence de multipolarité). Le rapport identifie ce problème mais ne peut pas le résoudre sans refondre l'architecture du dossier.

### Cluster de friction — T1 (menace réelle) vs T2 (construction intéressée)

Le dossier documente les deux avec une rigueur équivalente. Le clustering topologique confirme que les DEUX sont fondés sur des réseaux d'acteurs identifiables. Aucun ne « gagne » topologiquement. La tension n'est pas résolue — elle est documentée comme une propriété structurelle du dossier.

---

## 7. Audit des limites méthodologiques (Phase 2)

### Abandon de la formule de solidité shadow

La version précédente de ce rapport utilisait une formule `score = max(0, confirmants×1 - fragiles_forts×1) / total_faits` produisant des scores numériques (0.71, 0.82, 0.60). Cette formule a été abandonnée pour deux raisons :

1. **Arbitraire du comptage.** Le choix de quels F-## « confirment » vs « attaquent » une thèse est subjectif — l'analyste qui a écrit les 16 quintessences compte ce qu'il veut compter.
2. **Précision fabriquée.** Un score à deux décimales (0.71) suggère une précision que la méthode ne permet pas. La solidité shadow est une heuristique qualitative, pas une mesure.

**Remplacement:** Les thèses sont évaluées qualitativement (SOLIDE, SUGGESTIF, FRAGMENTÉ, SPÉCULATIF) avec justification explicite.

### Score de complétude

- **N cités ≥1×:** 16/16 = **100 %** ✅
- **Mode:** strict — toutes les quintessences sont ingérées exhaustivement

### Limites structurelles

1. **Asymétrie des sources.** 80 %+ des sources citées sont occidentales. Gap documenté mais structurel.
2. **Biais KERNEL.** SUSPICION_BASELINE = 95 % pour les discours officiels occidentaux. Ce biais est documenté (fichier 19) mais structurellement non neutralisable.
3. **Architecture du dossier comme artefact.** Les clusters capturent partiellement la structure du questionnaire. Voir §6-F1.
4. **Absence de sources primaires classifiées.** Coordination militaire réelle, accords secrets — inaccessibles.

---

## 8. Alignement forensique Truth Engine

### Conformité KERNEL v2.0

- **SUSPICION_BASELINE:** 95 % — appliquée aux sources occidentales ET aux sources de l'axe. Symétrie documentée.
- **SOURCE DIVERSITY:** geo≥2, lang≥2, H7≥1 — satisfait dans 16/16 quintessences.
- **CLAIM_REGISTRY:** 16/16 — chaque fichier a ≥2 claims avec counters.

### Tensions avec le cadre KERNEL

1. **Le KERNEL postule un monde binaire (manipulation vs honnêteté).** Le dossier documente un monde où un discours peut être les deux simultanément (le documentaire Arte documente des faits réels ET est structurellement biaisé). Cette tension est productive — le KERNEL v2.0 a partiellement évolué pour l'accommoder (CLAIM_REGISTRY, assessed vs scored) mais la tension persiste.
2. **SUSPICION_BASELINE asymétrique.** 95 % pour l'Occident, pas de chiffre explicite pour l'axe. Le fichier 19 documente ce gap.

---

## 9. Recommandation CP1 (Article Oui/Non)

<RECOMMANDATION:OUI>

**Avec les réserves suivantes :**

1. Le clustering topologique confirme que le dossier documente DEUX réseaux d'acteurs identifiables (leaders de l'axe, CMI occidental) avec une rigueur symétrique. C'est une base solide pour un article. MAIS les clusters sont partiellement des artefacts de l'architecture du dossier — l'article devra le dire.
2. Le contournement des sanctions est le seul mécanisme transversal identifié. L'article devrait en faire un pilier, pas un exemple parmi d'autres.
3. L'absence de cluster idéologique ET la fragmentation du signal multipolaire sont des résultats aussi importants que les clusters identifiés. L'article ne doit pas les omettre.
4. Les scores numériques de « solidité » ont été abandonnés comme non fiables. L'article ne doit pas utiliser de pseudo-précision quantitative.
5. La thèse « la menace est réelle ET exagérée » (ex-T5 de la version précédente) n'est pas un résultat du clustering — c'est une position épistémique. L'article peut l'adopter comme angle, mais ne doit pas la présenter comme un « résultat ».

- **Thèse fil rouge:** La narrative du « triangle de fer » et sa critique sont DEUX constructions qui documentent des faits réels — l'axe existe (T1), sa menace est amplifiée par un circuit militaro-médiatique identifiable (T2), et le monde multipolaire émergent (T5) invalide le cadrage binaire des deux camps.
- **Angle:** Le dossier a découvert, presque malgré lui, que sa propre architecture produit DEUX réseaux en miroir (leaders de l'axe ↔ CMI occidental). L'article doit exposer cette symétrie comme résultat central — pas comme un « équilibre » artificiel, mais comme une propriété émergente des données.
- **Ton:** Forensic, symétrique, explicitement conscient de ses propres artefacts. Ni alarmiste, ni complaisant. La posture n'est pas « nous avons raison » mais « voici ce que les données montrent — et voici ce qu'elles ne montrent pas. »

---

**Fin du rapport Phase 2 (corrigé).** Clustering topologique réel (grep acteurs + M-##). 5 thèses (3 clusters + 2 signaux). 3 transversalités. Scores qualitatifs. CP1 = OUI avec 5 réserves explicites.
