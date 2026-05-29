# AUDIT APEX — S11 - L'Agriculture qui meurt

> Score global : **8.6/10** — RÉVISION MINEURE (borderline APEX)
>
> Résumé : Excellent article, factuellement irréprochable (17/17 faits FACTCHECK), §6 de haute qualité, H3 bien distribuées. Les faiblesses sont concentrées sur (1) le lien "À lire ensuite" qui pointe erronément vers S6 au lieu de S13, (2) 2 URLs génériques dans les sources, (3) 3 sauts logiques intentionnalistes, (4) 2 blockquotes longs (>600 chars).

## RADAR SCORE

| S1 Struc. | S2 Source | S3 URLs | S4 Ton | S5 §6 | S6 Fond. | S7 Caus. | S8 Cohér. | S9 Écrit. |
|-----------|-----------|---------|--------|-------|----------|----------|-----------|-----------|
| 9 | 9 | 9 | 8 | 10 | 9 | 6 | 8 | 8 |

## CONTRÔLE GATE

- Gate 1 (Structure) : **PASS** (11/12)
- Gate 2 (Sourçage) : **PASS** (9/10)
- Gate 3 (Ton) : **PASS** (8/10)
- Gate 4 (Fondation) : **PASS** (9/10)
- Gate 5 (Écriture) : **PASS** (8/10)

## FINDINGS (par ordre de gravité)

### F001 — « À lire ensuite » + footer pointent vers S6 (désindustrialisée) au lieu de S13 (Europe)

| Champ | Valeur |
|-------|--------|
| **Couche** | 1 (Conformité structurelle) |
| **Localisation** | L127, L131 |
| **Problème** | `➡️ **À lire ensuite :** ...**S6 — La France désindustrialisée**` et `📖 **Article suivant :** 🏭 La France désindustrialisée...` — S6 précède S11 dans la série. Le lien devrait pointer vers S13 (L'Europe). |
| **Preuve** | S10 → S11, S11 → S13. S6 a déjà été publié avant S11. |
| **Correction** | Remplacer les deux occurrences de S6 par S13. |
| **Priorité** | Haute |

### F002 — 2 URLs génériques dans Sources

| Champ | Valeur |
|-------|--------|
| **Couche** | 2 (Sourçage & vérifiabilité) |
| **Localisation** | Sources 6, 13 |
| **Problème** | Source 6 (agriculture.gouv.fr/infographie...) et Source 13 (ecologie.gouv.fr/pesticides) pointent vers des pages d'index génériques, pas vers le document spécifique. |
| **Correction** | Source 6 : remplacer par l'URL officielle du bilan PAC France 2021-2027. Source 13 : remplacer par le rapport Écophyto 2023. |
| **Priorité** | Haute |

### F003 — 3 sauts logiques non médiatisés

| Champ | Valeur |
|-------|--------|
| **Couche** | 4.2 (Fidélité interprétative) |
| **Localisation** | §1 L39, §2 L55, §5 L115 |
| **Problème** | Trois formulations où l'article attribue une intention qui n'est pas strictement documentée par la source : (1) « élimination programmée » (Plan Mansholt — intentionnellement fort mais historiquement documenté), (2) « conçue pour » (PAC — le mécanisme proportionnel aux surfaces produit ce résultat, mais la PAC n'a pas été « conçue pour » concentrer), (3) « système de prédation » (saut interprétatif). |
| **Correction** | (1) « élimination programmée » → « réduction drastique programmée par le Plan Mansholt ». (2) « a été conçue pour soutenir... Elle est devenue une machine à concentrer » → « a été conçue pour soutenir... Son mécanisme — aides proportionnelles à la surface — produit mécaniquement une concentration des terres ». (3) « système de prédation » → déjà nuancé par la phrase précédente, acceptable. |
| **Priorité** | Haute |

### F004 — 2 blockquotes >600 chars

| Champ | Valeur |
|-------|--------|
| **Couche** | 5.4 (Respiration) |
| **Localisation** | §1 BQ (622 chars), §2 BQ (732 chars) |
| **Problème** | Règle SUBLIMATOR 5 : pas de blockquote au-delà de 4-5 lignes. Le BQ §1 (hémorragie/Plan Mansholt, 622 chars) et le BQ §2 (opacité PAC, 732 chars) dépassent. Perte d'impact rhétorique. |
| **Correction** | Scinder chaque BQ en deux blocs distincts séparés par une phrase. |
| **Priorité** | Moyenne |

### F005 — Ratio intentionnaliste élevé

| Champ | Valeur |
|-------|--------|
| **Couche** | 3.1 (Détection intentionnaliste) |
| **Localisation** | Multiples |
| **Problème** | Ratio intentionnaliste/structurel estimé à ~67% (3 marqueurs intentionnalistes : « conçue pour », « élimination programmée », « programmée » ; 1 marqueur structurel : « conséquence logique »). |
| **Correction** | Reformulations proposées en F003. Si appliquées, le ratio passe sous 30%. |
| **Priorité** | Moyenne (lié à F003) |

### F006 — HTML comments manquants dans §3, §4, §5

| Champ | Valeur |
|-------|--------|
| **Couche** | 1 (Conformité structurelle — métadonnées) |
| **Localisation** | §3 (pesticides/eau/souveraineté), §4 (libre-échange), §5 (abdication) |
| **Problème** | Seuls §1 et §2 ont des `<!-- CROSS-REF -->`. Les §3, §4, §5 n'ont aucune métadonnée. |
| **Correction** | Ajouter les méta pour chaque section. Proposition : §3 (CROSS-REF: S7, S15), §4 (CROSS-REF: S13, S15), §5 (CROSS-REF: S1, S15). |
| **Priorité** | Basse |

## RECOMMANDATIONS PRIORITAIRES

1. **Haute** — F001 : Corriger « À lire ensuite » et « Article suivant » : S6 → S13
2. **Haute** — F002 : Remplacer URLs génériques sources 6 et 13
3. **Haute** — F003 : Reformuler « élimination programmée », « conçue pour » (PAC), « système de prédation »
4. **Moyenne** — F004 : Scinder les 2 blockquotes longs
5. **Basse** — F006 : Ajouter HTML comments §3, §4, §5

## NOTES LLM (grille de scoring complète)

### Couche 1 — Structure : 11/12
| Point | Pass | Note |
|-------|------|------|
| H1 émoji | ✅ | |
| Sous-titre italique | ✅ | |
| Ligne série | ✅ | |
| §0 présent | ✅ | |
| Sections `## §N :` | ✅ | |
| `---` séparateurs | ✅ | |
| H3 sous-sections | ✅ | 14 H3 dans 6 sections |
| À lire ensuite | ⚠️ | Présent mais cible erronée (S6) |
| Footer | ✅ | |
| Sources H2 | ✅ | |
| URLs spécifiques | ❌ | 2 génériques |
| §6 présent | ✅ | |

### Couche 2 — Sourçage : 9/10
- 2.1 Saturation : 8/10 (quelques lignes sans source, surtout dans §6)
- 2.2 Diversité : 10/10 (17 sources uniques)
- 2.3 URLs : 9/10 (13/15 spécifiques)
- 2.4 Fraîcheur : 10/10 (toutes 2020-2025)

### Couche 3 — Ton : 8/10
- 3.1 Intentionnaliste : 6/10 (ratio ~67%, 3 marqueurs)
- 3.2 Polémique : 10/10 (0 mots)
- 3.3 §6 : 10/10 (4/4 critères : vrais contre-arguments, substantiels, non réfutés, directions alternatives)

### Couche 4 — Fidélité fondation : 9/10
- 4.1 Exactitude : 10/10 (17/17 faits FACTCHECK)
- 4.2 Fidélité interprétative : 6/10 (3 sauts)
- 4.3 Omissions : 10/10
- 4.4 Web : 10/10 (aucun fait suspect)
- 4.5 Agrégations : 10/10 (aucune agrégation trompeuse)

### Couche 5 — Écriture : 8/10
- 5.1 Visibilité du système : 9/10 (architecture, cross-ref, abdication organisée)
- 5.2 Démonstration traçable : 9/10 (connecteurs logiques, chaînes causales)
- 5.3 Respiration : 7/10 (1 wall, 2 blockquotes longs)
- 5.4 Cohérence catégorielle : 5/10 (2 blockquotes >600 chars)

### Radar pondéré
Global = 9×0.08 + 9×0.12 + 9×0.12 + 8×0.08 + 10×0.12 + 9×0.16 + 6×0.07 + 8×0.05 + 8×0.20
= 0.72 + 1.08 + 1.08 + 0.64 + 1.20 + 1.44 + 0.42 + 0.40 + 1.60
= **8.58/10**
