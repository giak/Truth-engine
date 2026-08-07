# KERNEL v2.0 — Investigation A : Données DSA — Contenus retirés en France

**INVESTIGATION KERNEL (2026-08-07, pipeline KERNEL v2.0)**
**Sujet** : Combien de contenus ont été retirés sous DSA en France depuis 2024 ? La machine censure-t-elle massivement ou marginalement ?
**Complexité** : COMPLEX (10/15)
**$TAGS** : `["project:truth-engine","kernel","status:confirme","verifie-2026-08-07","iceberg-max","investigation-a-kernel"]`
**$FORMAT** : table
**BASE** : 5 faits existants (pipeline Viginum→DSA, ARCOM SREN, zéro référé 2018)

---

## §0 — TEXT ANALYSIS

| # | Symbole | Score | Justification |
|:--|:--|:--|:--|
| Ξ1 | ICEBERG | 3 | Données de retrait = couche invisible de l'architecture |
| Ξ2 | DATA_VOID | 3 | L'absence de données est elle-même une donnée |
| Ξ3 | SOURCE_PRIMARY | 3 | Sources = DSA Transparency Database, rapports ARCOM |
| Ξ4 | GAP | 3 | Écart entre architecture légale et données opérationnelles |
| €5 | NARRATIVE | 2 | Le « pipeline censure » testé contre les données réelles |
| €6 | AMPLIFICATION | 1 | Si retraits marginaux → narratif « censure massive » exagéré |
| Λ7 | BLINDFOLD | 2 | L'opacité des données DSA masque l'usage réel |
| Λ8 | ASYMMETRY | 1 | Asymétrie entre architecture construite et usage documenté |

**SCORE** : 18/45 — MEDIUM
**BIAS TEST** : RISK — biais de confirmation : vouloir trouver que la censure est massive pour valider la thèse. Mitigation : chercher ACTIVEMENT les données qui contredisent.

---

## §1 — PIPELINE

### Step 2 — @MNEMO_Q

**BASE: 5 faits** → $TAGS extraits.
Le pipeline Viginum→DSA est documenté (attribution → rapport public → menace amendes 6% CA → retrait plateformes). Mais le VOLUME de retraits effectifs n'est pas documenté.

### Step 3 — COMPLEXITY : COMPLEX (10/15)
Enquête dépendante de données publiques potentiellement inexistantes.

### Step 6 — CRÉDO (12 queries)

```
C:4 — (1) Combien de Statements of Reasons (SoRs) les VLOPs opérant en France ont-elles soumis à la DSA Transparency Database ? (2) ARCOM a-t-il publié un rapport statistique sur les retraits DSA ? (3) Combien de contenus retirés sous DSA en France ? (4) Catégories : désinformation vs terrorisme vs haine ?
R:2 — (5) La DSA Transparency Database est-elle interrogeable par pays ? (6) Y a-t-il des données France-spécifiques dans les rapports de transparence Meta/X/TikTok ?
E:3 — (7) Combien de décisions ARCOM de retrait depuis mai 2024 ? (8) Combien de procédures d'infraction DSA ouvertes par la Commission européenne contre des plateformes en France ? (9) Comparaison : retraits DSA France vs Allemagne (NetzDG) vs UK (Online Safety Act) ?
D:3 — (10) L'absence de données publiques est-elle un choix délibéré ? (11) Si les données n'existent pas, que prouve cette absence ? (12) La machine est-elle construite pour la dissuasion (effet chilling) plutôt que pour la censure active ?
```

### Step 10 — FACT_REGISTRY

| # | Fait | Statut | Source | URL |
|:--|:--|:--|:--|:--|
| ✦A1 | Le pipeline Viginum→DSA est documenté : attribution → rapport public → menace amendes 6% CA → retrait plateformes | CONFIRMED | MnemoLite F6, P2F2 | — |
| ✦A2 | Viginum a documenté 259 phénomènes, 174 ingérences étrangères depuis 2021 | CONFIRMED | MnemoLite F6 | — |
| ✦A3 | L'ARCOM dispose du pouvoir de blocage administratif sans juge depuis la loi SREN (mai 2024) et le décret 2024-1255 | CONFIRMED | MnemoLite | — |
| ✦A4 | **Aucune statistique publique n'a été trouvée sur le nombre de contenus retirés sous DSA en France** | ⚠ NON TROUVÉ | Recherche PELOTE non conclusive | — |
| ✦A5 | La DSA Transparency Database existe (transparency.dsa.ec.europa.eu) mais les données France-spécifiques ne sont pas facilement extractibles | ⚠ PARTIEL | DSA Transparency Database | https://transparency.dsa.ec.europa.eu/ |
| ✦A6 | Le référé « fake news » 2018 n'a jamais été utilisé (zéro jurisprudence) — l'outil le plus ancien n'a jamais servi | CONFIRMED | MnemoLite | — |
| ✦A7 | Aucun rapport statistique ARCOM sur les retraits DSA n'a été trouvé dans les recherches PELOTE | ⚠ NON TROUVÉ | Recherche non conclusive | — |

### Step 11 — PELOTE

**Mécanisme 1 — Opacité structurée (HYPOTHÈSE)**

```
DSA Transparency Database existe → données par VLOP, pas par pays → 
extraction France-spécifique difficile → ARCOM ne publie pas de statistiques →
impossible de savoir si la censure est massive ou marginale
```

**Mécanisme 2 — Dissuasion, pas censure (HYPOTHÈSE)**

```
Architecture construite → menace crédible (6% CA) → 
plateformes sur-censurent préventivement → pas besoin d'ordres formels →
pas de trace statistique → machine invisible mais efficace
```

### Step 8t — DIALECTICAL

**A (thèse critique)** : L'absence de données est une politique d'opacité délibérée. Si les retraits étaient marginaux et légitimes (terrorisme, pédopornographie), le gouvernement les publierait pour montrer l'efficacité du dispositif. L'absence de statistiques suggère soit une censure massive qu'on veut cacher, soit une inefficacité qu'on veut masquer.

**B (thèse officielle)** : Les données existent mais sont dispersées entre les VLOPs (Meta, X, TikTok, YouTube) et la Commission européenne. La DSA est récente (février 2024), les rapports de transparence sont en cours de consolidation. L'absence de données France-spécifiques est un problème technique, pas politique.

**Arbitrage** : **INCONCLUSIF**. Les données nécessaires pour trancher n'ont pas été trouvées. Les deux hypothèses restent ouvertes. C'est un angle mort documenté, pas une conclusion.

### Step 13 — VERIFICATION

| Claim | Statut |
|:--|:--|
| « La machine DSA censure massivement en France » | **INVÉRIFIABLE** avec les données disponibles |
| « La machine DSA censure marginalement » | **INVÉRIFIABLE** avec les données disponibles |
| « Le pipeline Viginum→DSA existe » | **CONFIRMED** |
| « L'ARCOM a le pouvoir de bloquer sans juge » | **CONFIRMED** |
| « L'outil le plus ancien (référé 2018) n'a jamais servi » | **CONFIRMED** |

### Step 18 — GATE_CHECK

```
□ 7✦ ≥ minimum COMPLEX (10) : ⚠ FAIL — seulement 7 faits, 3 sont NON TROUVÉ
□ ALL ✦ have URL : ⚠ PARTIAL — A4, A5, A7 sans URL source
□ CRÉDO ≥ 12 queries : PASS (12)
□ DIALECTICAL 3 perspectives : PASS (2 + arbitrage)
□ ∅ fabricated figure : PASS
⚠ GATE_CHECK PARTIAL — investigation limitée par l'indisponibilité des données
```

---

## CONCLUSION — Ce que cette investigation a révélé (et n'a pas révélé)

**Ce qui est CONFIRMED :**
- Le pipeline Viginum→DSA existe structurellement
- L'ARCOM a le pouvoir de blocage sans juge depuis 2024
- Le référé 2018 n'a jamais servi (zéro jurisprudence)
- Aucune statistique publique France-spécifique n'a été trouvée sur les retraits DSA

**Ce qui est INCONCLUSIF :**
- Le volume de contenus retirés sous DSA en France
- La répartition par catégorie (désinformation vs terrorisme vs haine)
- La question centrale : censure massive ou marginale ?

**Implication pour la thèse** : L'architecture est construite, le pouvoir existe, mais **nous ne savons pas comment il est utilisé**. L'opacité des données DSA est soit un problème technique temporaire, soit une politique délibérée. Si c'est délibéré, c'est un fait en soi : on construit une machine de censure sans rendre de comptes sur son usage.

**Action recommandée** : Requête directe à l'ARCOM (droit d'accès aux documents administratifs, CADA) ou scraping programmatique de la DSA Transparency Database pour extraction France-spécifique. Investigation non clôturée.
