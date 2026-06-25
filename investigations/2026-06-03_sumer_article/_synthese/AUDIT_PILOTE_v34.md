# AUDIT PILOTE SUBLIMATOR v34 — Sumer 11 enquêtes

**Date :** 2026-06-07 | **Auditeur :** Buffy (Truth Engine)
**Fichiers audités :** 11 quintessences YAML + synthese.yaml + rapport_synthese.md
**Prompt de référence :** `tools/engines/sublimator/prompt-v34.md`

---

## RÉSUMÉ

Le pilote v34 a produit un travail **solide et cohérent** sur les 11 enquêtes Sumer. Les quintessences sont correctes, la synthèse est structurée, et les 5 thèses cardinales sont justifiées avec des shadow factors crédibles. **Verdict global : VALIDE avec 3 réserves modérées et 1 réserve mineure.**

Les problèmes trouvés sont des **défauts de cohérence interne** ou de **traçabilité Mnemolite**, pas des erreurs factuelles ou des contradictions logiques.

---

## 1. CONFORMITÉ AU PROMPT v34

### Phase 1 — Quintessences

| Exigence prompt | Statut | Note |
|----------------|--------|------|
| 12 sections YAML | ✅ | Toutes présentes dans les 11 fichiers |
| `get_system_snapshot` en ouverture | ✅ | Documenté dans le CP1 (Mnemolite UP, 35 027 mémoires) |
| Au moins 2 `search_memory` par enquête | ✅ | 5 queries par quintessence en moyenne |
| Résultats Mnemolite dans `iceberg` | ✅ | Verdict corrigé pour 9/11 (2 gaps réels) |
| `mnemo_queries` obligatoires | ✅ | Présentes, mais voir réserve #1 |
| `write_memory` après extraction | ⚠️ Non vérifiable | Le prompt dit de sauvegarder chaque quintessence via `write_memory`. Impossible de vérifier si ça a été fait sans lister les mémoires récentes. |
| CP1 avec V/M/R/E | ✅ | Le LLM a affiché le CP1 v2 et attendu validation |

### Phase 2 — Synthèse YAML

| Exigence prompt | Statut | Note |
|----------------|--------|------|
| 7 sections YAML | ✅ | date_synthese, complexity, theses, meta_observations, transversalites, gaps, mnemo_context |
| 3-5 thèses cardinales | ✅ | 5 thèses (THESE-001 à THESE-005) |
| `f_atomiques_justificatifs` par thèse | ✅ | 3-5 faits par thèse |
| `cartes_positions` supprimé | ✅ | Conforme au prompt (« n'existe plus ») |
| Au moins 5 `search_memory` cross-séries | ✅ | 10 queries documentées dans mnemo_context.searches |
| Shadow factor global + justification | ✅ | 3.8 avec justification détaillée |

### Phase 2.5 — Rapport de synthèse

| Exigence prompt | Statut | Note |
|----------------|--------|------|
| §1 Vue d'ensemble | ✅ | 2 paragraphes, clair |
| §2 Justification détaillée des 5 thèses | ✅ | Pourquoi / Pourquoi pas / Réfutation / Shadow |
| §3 Transversalités | ✅ | 10 découvertes, la plus inattendue identifiée |
| §4 Surprises et angles morts | ✅ | 5 surprises + 10 gaps |
| §5 Critique de la synthèse | ✅ | Fragilités, manques, améliorations |
| §6 Recommandation | ✅ | OUI article, THESE-003 fil rouge, 7 actes |

---

## 2. CROSS-CHECK CP1 v2 vs RÉALITÉ DES FICHIERS

### Claim : « 11/11 quintessences enrichies avec mnemo_cross_refs »

**Vérifié.** Les 11 fichiers YAML contiennent tous une section `mnemo_cross_refs`. ✅

### Claim : « Sections iceberg corrigées, verdict 'base non indexée' remplacé »

**Vérifié.** Les 9 quintessences qui avaient le verdict erroné l'ont corrigé :
- sumer_v1 : « Mnemolite INDEXEE pour Sumer : 12 memoires trouvees »
- rome_v1 : « Mnemolite INDEXEE pour Rome : 4 memoires trouvees »
- chine_v1 : « Mnemolite INDEXEE pour Chine : 12 memoires »
- islam : « Mnemolite INDEXEE pour Islam : 2 memoires »
- inde : « Mnemolite INDEXEE pour Inde : 1 memoire directe »
- andurarum_autopsy : « Mnemolite INDEXEE pour Andurarum : 2 memoires identiques (doublon) »
- sumer_iceberg, rome_iceberg, chine_iceberg : vérifiés également

Les 2 gaps réels (moyen_age, ameriques) sont correctement maintenus comme « REELLEMENT NON INDEXEE ». ✅

### Claim : « 2 gaps assumés : moyen_age et ameriques »

**Vérifié.** Les deux fichiers ont `mnemo_cross_refs` avec `level: GAP` et 0 mémoire trouvée. ✅

### Claim : « Doublons andurarum (627f9e5d + b954741d, 08:51 et 08:53) »

**Vérifié.** Le fichier andurarum_autopsy_quintessence.yaml documente les deux mémoires comme IDENTITY et DOUBLON, avec les timestamps exacts. ✅

### Claim : « Doublon islam (12283cc0 + 3522d543) »

**Vérifié.** Le fichier islam_quintessence.yaml documente le doublon. ✅

### Claim : « Chine ICEBERG BOUSSOLE rétractée 5/7 → 3/7, EDI* 0.492 → 0.40 »

**Vérifié.** Le fichier chine_iceberg_quintessence.yaml contient F-013 : « Shadow Factor révisé V1→V2 : 3.2× → 3.8×. EDI* : 0.492 → 0.40 ». ✅

### Stats du CP1 vs comptage réel

| Métrique | CP1 claim | Comptage réel | Statut |
|----------|-----------|---------------|--------|
| Total faits | 136 | 136 | ✅ |
| Total acteurs | 85 | 85 | ✅ |
| Shadow moyen | 3.74 | 3.736 | ✅ |
| Mnemo refs uniques | 14 | 14 | ✅ |
| Mnemo refs totales | 16 | 16 | ✅ |

Les comptages sont exacts. Aucune triche.

---

## 3. RÉSERVES

### RÉSERVE #1 (MODÉRÉE) : Incohérence mnemo_queries vs mnemo_cross_refs

**Problème :** Les sections `mnemo_queries` affichent `results_count: 0` pour la quasi-totalité des requêtes textuelles, alors que les sections `mnemo_cross_refs` montrent des hits directs via recherche par tag.

Exemple — islam_quintessence.yaml :
```yaml
mnemo_queries:
- query: Islam Bayt al-Hikma Bagdad Cordoue Tolède traduction savoir grec
  results_count: 0       # ← 0
- query: Islam riba charia oulémas finance islamique intégration
  results_count: 0       # ← 0

mnemo_cross_refs:
- id: 12283cc0-...       # ← mémoires bien trouvées !
  level: DIRECT
```

**Impact :** Un lecteur du YAML qui ne lit que `mnemo_queries` conclurait que Mnemolite est vide, ce qui est factuellement faux. La section `mnemo_queries` devrait refléter les résultats RÉELS (tag-based) qui ont permis de trouver les cross-refs.

**Correction recommandée :** Remplacer les `results_count: 0` par les counts réels obtenus via recherche tag (ex: `results_count: 2` pour islam), ou ajouter une note explicative « tag_only mode: 0 results on text, 2 on tags » dans chaque query.

### RÉSERVE #2 (MODÉRÉE) : Ambiguïté « 10/10 mémoires lues »

**Problème :** Le CP1 v2 écrit « 10/10 mémoires Mnemolite lues (8 fichiers + 2 doublons) ». Or il y a 11 quintessences, dont 9 avec au moins 1 cross-ref et 2 sans (moyen_age, ameriques). L'expression « 10/10 » ne correspond à aucun décompte évident.

**Hypothèse :** Le LLM voulait dire « 10 mémoires Mnemolite lues au total » (8 uniques + 2 doublons), pas « 10/10 quintessences ». L'ambiguïté est bénigne mais révèle une formulation imprécise.

**Correction recommandée :** Clarifier dans le prompt v34 que le CP1 doit lister le compte exact : « X/Y quintessences avec ≥1 cross-ref, Z mémoires uniques trouvées, W doublons ».

### RÉSERVE #3 (MODÉRÉE) : Le rapport de synthèse sur-vend THESE-003 (Islam)

**Problème :** Le rapport de synthèse fait de THESE-003 (transmission Rome → Bagdad → Cordoue → Tolède → Bologne) le « fil rouge » de l'article et le présente comme « la thèse la plus solide (shadow 2,0) ». Or cette thèse repose sur **3 fiches** (islam, moyen_age, rome_iceberg). C'est la thèse avec le **plus petit nombre de fiches support**, ce qui est paradoxal pour la « plus solide ».

La solidité vient du fait que les 3 fiches ont des shadows bas (2.8, 1.5, 3.4), mais la thèse elle-même n'est pas testée par les 8 autres enquêtes. Une thèse à 3/11 est structurellement moins robuste qu'une thèse à 5/11 (comme THESE-002 ou THESE-004).

**Ce n'est pas une erreur**, mais une **décision éditoriale forte** qui mérite d'être explicitée : le pilote a choisi l'angle le plus contre-intuitif et le mieux documenté, pas le plus transversal.

**Correction recommandée :** Ajouter dans le rapport une phrase du type : « THESE-003 est la plus solide PARMI les thèses à fort potentiel narratif, mais elle ne couvre que 3/11 enquêtes. THESE-002 et THESE-004 sont plus transversales (5/11) et mériteraient une place dans l'article. »

### RÉSERVE #4 (MINEURE) : GAP-010 redondant avec GAP-001 à GAP-009

**Problème :** GAP-010 (« Mnemolite non indexé pour moyen_age et ameriques ») est de nature différente des 9 autres gaps (qui listent des civilisations absentes de l'étude). Mélanger un gap méthodologique (indexation Mnemolite) avec des gaps de contenu (civilisations manquantes) affaiblit la clarté de la section.

**Correction recommandée :** Séparer en deux listes : `gaps_civilisationnels` (GAP-001 à GAP-009) et `gaps_methodologiques` (GAP-010).

---

## 4. FORCES DU PILOTE

1. **Correction d'erreur auto-détectée.** Le pilote a identifié que son propre verdict « base non indexée » était faux pour 9/11 enquêtes, l'a corrigé, et a documenté la correction. C'est exactement le comportement attendu d'un pipeline forensique.

2. **Doublons détectés et documentés.** Les doublons andurarum (08:51 et 08:53) et islam (08:50 et 08:52) ont été correctement identifiés comme des duplications accidentelles du pipeline de la matinée. Le rapport recommande de les nettoyer.

3. **Rétractation de la BOUSSOLE Chine.** Le passage de « OUI 5/7 » à « OUI conditionnel 3/7 » est une correction majeure documentée avec EDI* révisé. Le pilote ne cache pas ses erreurs précédentes.

4. **Mnemolite tag_only correctement diagnostiqué.** Le pilote a compris que le mode `tag_only` explique les 0 hits sur requêtes textuelles et l'a documenté dans la synthèse. La recommandation d'indexer les quintessences avec des tags explicites est pertinente.

5. **10 gaps civilisationnels documentés.** Égypte, Grèce, Perse, Carthage, Mésoamérique, Afrique subsaharienne, Japon, Russie, Byzance : la liste est honnête et ne prétend pas à l'exhaustivité.

6. **Recommandation claire.** « OUI article, THESE-003 fil rouge, 7 actes, ton journaliste d'enquête » : la recommandation est actionnable et spécifique.

7. **Zéro hallucination détectée.** Aucun fait inventé. Tous les F### ont des URLs vérifiées (HEAD 200). Les shadow factors sont cohérents avec la densité documentaire.

---

## 5. CONFORMITÉ GLOBALE

| Critère | Score | Note |
|--------|-------|------|
| Extraction (Phase 1) | 9/10 | Réserves #1 (mnemo_queries incohérentes) |
| Synthèse YAML (Phase 2) | 9/10 | Conforme au prompt, cartes_positions bien supprimé |
| Rapport (Phase 2.5) | 8/10 | Réserves #3 (sur-vente THESE-003) et #4 (GAP-010 mélangé) |
| Honnêteté intellectuelle | 10/10 | Corrections auto-détectées, gaps assumés, doublons documentés |
| Traçabilité | 9/10 | Tous les F### sourcés, URLs HEAD 200, mais mnemo_queries trompeuses |
| **GLOBAL** | **9/10** | **VALIDÉ — prêt pour Phase 3 avec corrections mineures** |

---

## 6. RECOMMANDATIONS POUR LA PHASE 3

Avant de lancer la rédaction de l'article :

1. **Corriger les mnemo_queries** (réserve #1) : remplacer les `results_count: 0` par les vrais counts tag-based, ou documenter explicitement le mode tag_only dans chaque query.

2. **Nuancer THESE-003 dans le rapport** (réserve #3) : ajouter une phrase sur sa couverture limitée (3/11) vs THESE-002/THESE-004 (5/11).

3. **Séparer GAP-010** (réserve #4) en gap méthodologique distinct.

4. **Nettoyer les doublons Mnemolite** : supprimer b954741d (andurarum) et 3522d543 (islam) — les deux doublons créés accidentellement à 2 minutes d'écart.

5. **Vérifier l'indexation des 11 quintessences** dans Mnemolite via `write_memory` avec `memory_type="quintessence"` et `tags=["truth-engine", "quintessence", "sumer"]` avant la Phase 3.

---

## 7. CONCLUSION

Le pilote Sublimator v34 a passé l'épreuve avec un score de **9/10**. Les réserves sont des défauts de présentation et de cohérence interne, pas des erreurs factuelles. La chaîne de traçabilité (212 → 136 faits → 5 thèses → 1 recommandation) est intacte. Zéro hallucination. Le pipeline est **prêt pour la Phase 3** après les corrections mineures listées ci-dessus.

La découverte la plus significative du pilote n'est pas dans les thèses elles-mêmes, mais dans le **comportement du pipeline** : capacité d'auto-correction (verdict iceberg), détection de doublons, diagnostic du mode tag_only, et rétractation documentée de la BOUSSOLE Chine. Ce sont ces méta-capacités qui font la valeur du Sublimator, au-delà du contenu produit.
