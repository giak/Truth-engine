# Données ARCOM 2022 : temps d'antenne des souverainistes — ce qui est accessible, ce qui ne l'est pas

Date : 2026-08-04 | Heure : 21:00 CEST | Type : INVESTIGATION — EXTRACTION PARTIELLE | Source : ARCOM, data.gouv.fr, Le Monde, synthèses journalistiques

---

## Constat principal

Les données ARCOM 2022 existent en open data sur data.gouv.fr. L'extraction précise (téléchargement CSV, parsing, filtrage par candidat et par chaîne) nécessite un traitement de données hors scope de cette session. Cette investigation documente :
1. Où trouver les données
2. Ce que les synthèses journalistiques en ont retenu (ordres de grandeur)
3. Ce que l'extraction complète permettrait de documenter

---

## 1. Où trouver les données

**F-ARCOM-01** : Les relevés de temps de parole et d'antenne de la présidentielle 2022 sont publiés par l'ARCOM sur data.gouv.fr. URL probable : `https://www.data.gouv.fr/fr/datasets/?q=ARCOM+presidentielle+2022`. Les données sont au format CSV, ventilées par candidat, chaîne, et période. (ARCOM, data.gouv.fr)

**F-ARCOM-02** : Le Monde Les Décodeurs a publié des visualisations interactives utilisant ces données : « Visualisez les temps de parole de chaque candidat dans les médias » (18/02/2022) et « Le tableau de bord des parrainages, sondages et temps de parole » (22/02/2022). (Le Monde, février 2022)

**F-ARCOM-03** : Trois périodes réglementées en 2022 : (1) Équité : 01/01-07/03/2022, (2) Équité renforcée en conditions comparables : 08/03-27/03/2022, (3) Égalité stricte : 28/03-08/04/2022 (campagne officielle). Les données sont disponibles pour chaque période. (ARCOM, recommandation 06/10/2021)

---

## 2. Ce que les synthèses journalistiques documentent (ordres de grandeur)

### Période 1 : Équité (01/01-07/03/2022)

**F-ARCOM-04** : Pendant la période d'équité, les « grands » candidats (Macron, Le Pen, Mélenchon, Zemmour, Pécresse) ont reçu un temps de parole nettement supérieur aux « petits » candidats. Le principe d'équité n'impose pas l'égalité mais la « fairness » : un candidat ayant plus de sondages/élus/activité peut recevoir plus de temps. (ARCOM, Le Monde)

**F-ARCOM-05** : Asselineau, Dupont-Aignan et Lassalle étaient parmi les candidats recevant le moins de temps de parole en période 1, avec Poutou et Arthaud. Ordre de grandeur estimé : quelques heures sur l'ensemble des chaînes sur 2 mois, contre des dizaines d'heures pour Macron/Le Pen/Mélenchon/Zemmour. (Le Monde, visualisation février 2022)

### Période 3 : Égalité stricte (28/03-08/04/2022)

**F-ARCOM-06** : Pendant la campagne officielle (12 jours), le principe d'égalité stricte s'applique : chaque candidat reçoit exactement le même temps de parole. Les 12 candidats ont donc reçu un temps ÉGAL sur cette période, quelle que soit la chaîne. (ARCOM)

**F-ARCOM-07** : L'égalité stricte ne s'applique qu'au temps de parole DES CANDIDATS, pas de leurs soutiens. Les « grands » candidats peuvent donc bénéficier indirectement de plus de temps via leurs soutiens (ministres pour Macron, cadres du parti pour Le Pen/Mélenchon). (ARCOM)

### Par chaîne

**F-ARCOM-08** : Le Monde (02/04/2022) rapporte que RTL, Europe 1, BFM TV et RMC Découverte ont été mis en garde par l'ARCOM pour non-respect de l'équité pendant la période 1. CNews n'est pas citée dans cet article spécifique. (Le Monde, 02/04/2022)

**F-ARCOM-09** : Aucune synthèse journalistique trouvée comparant spécifiquement le temps d'antenne d'Asselineau/Dupont-Aignan/Lassalle entre CNews, BFM TV et France Info. Les données ARCOM brutes le permettraient, mais le traitement n'a pas été fait.

---

## 3. Ce que l'extraction complète permettrait de documenter

Si les données ARCOM 2022 étaient extraites et analysées, on pourrait répondre précisément à :

1. **Temps total par candidat** (heures:minutes) sur l'ensemble de la période 01/01-08/04/2022, toutes chaînes confondues.
2. **Ratio « grands » vs « petits » candidats** en période 1 (équité). Exemple : Macron = X heures, Asselineau = Y heures, ratio X:Y.
3. **Comparaison inter-chaînes** : temps d'Asselineau sur CNews vs BFM TV vs France Info, pour chaque période.
4. **Évolution temporelle** : le temps d'Asselineau a-t-il augmenté entre la période 1 et la période 3 ? De combien ?
5. **Concentration horaire** : à quelles heures de la journée le temps des « petits » candidats était-il diffusé ?

---

## 4. Procédure d'extraction (pour référence future)

1. Aller sur `https://www.data.gouv.fr/fr/datasets/`
2. Rechercher « ARCOM présidentielle 2022 temps de parole »
3. Télécharger le CSV le plus récent
4. Filtrer par colonnes : `candidat` IN (Asselineau, Dupont-Aignan, Lassalle) ET `chaîne` IN (CNews, BFM TV, France Info)
5. Sommer `temps_parole_secondes` par candidat et par chaîne
6. Normaliser par période (P1, P2, P3)

Temps estimé : 30 minutes avec un script Python/pandas.

---

## 5. Implications pour le corpus

**F-ARCOM-10** : Les données ARCOM 2022 confirment que le suivi quantitatif individuel EXISTE pour les périodes électorales. L'absence de suivi hors élections (documentée dans F-TA-11..15) est donc un CHOIX réglementaire, pas une impossibilité technique.

**F-ARCOM-11** : La période 1 (équité, 01/01-07/03/2022) est la plus pertinente pour comparer le traitement médiatique : c'est là que les chaînes ont une marge de manœuvre éditoriale. La période 3 (égalité stricte) neutralise les différences.

**F-ARCOM-12** : Les données 2022 ne documentent PAS la période post-électorale (2023-2026), qui est pourtant la plus pertinente pour comprendre le traitement des souverainistes qui ne sont plus candidats.

---

## Limites

- Les données ARCOM 2022 n'ont PAS été extraites ni analysées dans cette investigation. Les ordres de grandeur sont issus de synthèses journalistiques (Le Monde).
- Les données ARCOM mesurent le temps de parole (candidat qui parle) et le temps d'antenne (mention du candidat). La distinction est importante : Lassalle pouvait être mentionné sans parler.
- Les données ne mesurent pas le TON ou le CADRAGE du temps de parole. 10 minutes d'interview complaisante ≠ 10 minutes de contradiction hostile.
