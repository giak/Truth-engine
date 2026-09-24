# Audit automatisé Phase 1 Sublimator v35 : n=42 + 1 LEGACY

**Date :** 2026-07-08  
**Méthodologie :** 6 critères objectifs (C1, C2, C5, C6, C7, C10) + scoring binaire 1/0.5/0 sur 6 points max.  
**C3 (zéro em-dash) NEUTRALISÉ 2026-07-08** : scope originel = articles (Phase 3), pas fiches internes (Phase 1 quintessence). Champ `n_em_dash` reste tracké informativement. Cf. docstring pour note scope complète.
**Critères subjectifs exclus :** C4 (Refus Phase 1), C8 (Fidélité citations), C9 (Pas de jugement) ; réservés à l'audit manuel échantillonné (cf. n=6).  
**Critère C10** : strict = match exact des 9 noms canoniques ; lenient = tolérance de la variante §9 « Limites (case-limites) ».

---

## 1. Synthèse globale n=42 canoniques

- **Total fichiers canoniques :** 14
- **Score strict moyen :** 5.5 / 6.0
- **Score lenient moyen :** 6.0 / 6.0

### 1.1 Taux par critère (canoniques)

| Critère | ✅ | ⚠️ | ❌ | Taux OK strict | Taux OK+Warn |
|---------|----|----|----|----------------|---------------|
| **C1** | 14 | 0 | 0 | 100.0% | 100.0% |
| **C2** | 14 | 0 | 0 | 100.0% | 100.0% |
| **C3** | 14 | 0 | 0 | 100.0% | 100.0% |
| **C5** | 14 | 0 | 0 | 100.0% | 100.0% |
| **C6** | 14 | 0 | 0 | 100.0% | 100.0% |
| **C7** | 14 | 0 | 0 | 100.0% | 100.0% |
| **C10** | 14 | 0 | 0 | 100.0% | 100.0% |
| **C10_strict** | 0 | 14 | 0 | 0.0% | 100.0% |
| **Δ Source** | 0 | 0 | 0 | 0.0% | 0.0% |

## 2. Tableau détaillé (42 canoniques)

| Fichier | C1 | C2 | C3* | C5 | C6 | C7 | C10 (strict) | C10 (variant §9) | Δ Source | Score strict |
|---------|----|----|-----|----|----|----|---------------|--------------------|----------|---------------|

*C3 = zéro em-dash, NEUTRALISÉ (informatif uniquement, hors score).*

*Δ Source = contrôle Delta Source-Quintessence (v2026-07-08) : compare les F-## source vs quintessence. ❌ si fabrication détectée.*

| `2026-09-20_1704_insee-biais-modes-calcul-fresque-systemique_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ? | 5.5/6 |
| `2026-09-20_1812_insee-chaine-donnee-indicateur-claim-provenance-et-robustesse_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ? | 5.5/6 |
| `2026-09-20_1921_insee-pdf-methodo-gap-access-closure_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ? | 5.5/6 |
| `2026-09-20_2008_dgf-impact-ecart-population-metzing_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ? | 5.5/6 |
| `2026-09-20_2050_dgcl-notes-elasticite-part-population_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ? | 5.5/6 |
| `2026-09-20_2105_prosopographie-dirigeants-insee-ecoles-bercy-conflits_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ? | 5.5/6 |
| `2026-09-20_2110_indexation-conventions-gains-milliards_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ? | 5.5/6 |
| `2026-09-20_2154_irl-ecart-loyers-reels-elc_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ? | 5.5/6 |
| `2026-09-20_2155_cui-bono-quantification-gap-closure_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ? | 5.5/6 |
| `2026-09-21_0255_insee-taux-de-reponse-par-vague-precision-des-estimations_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ? | 5.5/6 |
| `2026-09-21_0314_insee-avis-conformite-cnis-eec-gap-access_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ? | 5.5/6 |
| `2026-09-21_0347_insee-effet-controle-externe-et-analyse-independante_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ? | 5.5/6 |
| `2026-09-21_0428_insee-chiffrage-indexation-effet-ipc-dotations_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ? | 5.5/6 |
| `2026-09-21_0446_insee-comparaison-internationale-prix-et-taux-de-reponse_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ? | 5.5/6 |

## 4. Patterns de déviation

- **C10 strict = ❌** : 0/42 = 0.0%
- **C10 strict = ⚠️** : 14/42 = 33.3%
- **C7 = ❌** (ni Verbatim ni Notes canoniques) : 0/42 = 0.0%

## 5. Distribution des noms H2 réels (top patterns)

- `## 1. Métadonnées & trace source` : 14 occurrences
- `## 2. Faits atomiques préservés` : 14 occurrences
- `## 3. Acteurs nominaux` : 14 occurrences
- `## 4. Sources externes citées` : 14 occurrences
- `## 5. Chronologie datée` : 14 occurrences
- `## 6. Mécanismes / chaînes causales` : 14 occurrences
- `## 7. Verbatim et citations` : 14 occurrences
- `## 8. Notes méthodologiques source` : 14 occurrences
- `## 9. Limites connues de cette extraction (case-limites)` : 14 occurrences
