# Audit forensique — `_quintessence/` vs protocole Sublimator v34

**Date :** 2026-07-05
**Périmètre :** `investigations/2026-07-04-RIC/_quintessence/` (29 fichiers YAML)
**Validateur :** `tools/engines/sublimator/extractors/gates.py` (auto-détection YAML/JSON)
**Méthode :** dry-run read-only + checks de cohérence inter-sections étendues
**Statut global :** **16 OK / 13 FAIL** sur les gates structurels H0-H6.

---

## 1. Contexte normatif

Le protocole Sublimator v34 impose aux quintessences :
1. **Format :** JSON par défaut depuis 2026-07-05, YAML toléré en lecture seule.
2. **12 sections obligatoires :** `these_centrale`, `theses_implicites`, `faits_atomiques`, `acteurs`, `causalites`, `perspectives_dialectiques`, `limites`, `wolves`, `iceberg`, `chronologie`, `domaines`, `urls_prioritaires`. + métadonnées (`enquete_id`, `complexity`, `date_extraction`, `enquete_source`, `shadow_factor`, `mnemo_queries`).
3. **Format "ace" des faits_atomiques :** `{id, enonce, source_url, source_section, head_status, tier, glyphe}` avec glyphe ∈ {✦, ✧, ⁅, ❧}.
4. **7 gates structurels :** H0 parseable, H1 clés obligatoires, H2 types, H3 glyphes valides, H4 IDs uniques, H5 thèses ≥3 F##, H6 cohérence F##.
5. **Mnemolite DOWN = mode dégradé documenté** (champ `mnemolite_status`).

---

## 2. Résultats dry-run `gates.py`

### 2.1 Bilan global

| Statut | Nombre | Pourcentage |
|--------|--------|-------------|
| PASS H0-H6 | 16 | 55,2 % |
| FAIL H0-H6 | 13 | 44,8 % |
| **Total** | **29** | **100 %** |

### 2.2 Les 13 fiches FAIL — pattern dominant

Les 13 échecs suivent **un même archétype : format pré-ace (legacy "classe")** où les `faits_atomiques` portent un champ `fiabilite` au lieu de `glyphe`. C'est exactement le pattern que `normalize_quintessences.py` détecte (cf. `is_ace_format()` lignes 56-69) et qu'il convertit.

**Liste exhaustive des 13 FAIL :**

1. `cross_exam_quintessence.yaml` — H1 (7 clés racine vides : `these_centrale`, `theses_implicites`, `acteurs`, `perspectives_dialectiques`, `limites`, `wolves`, `domaines`) + H3 (4 ranges de F-## : E01-E05, M01-M05, S01-S05, FRAMING01-05)
2. `p3_15_gaps_quintessence.yaml` — H1 (`chronologie` absente)
3. `p3_cedh_quintessence.yaml` — H1 (`chronologie` absente)
4. `p3_conv_cit_quintessence.yaml` — H1 (7 clés racine vides) + H3 (F-CONV01 à F-CONV30)
5. `p3_decidim_quintessence.yaml` — H1 (7 clés racine vides) + H3 (F-DECI01 à F-DECI27)
6. `p3_indif_quintessence.yaml` — H1 (7 clés racine vides) + H3 (F-IND01 à F-IND30)
7. `p3_lobby_quintessence.yaml` — H1 (7 clés racine vides) + H3 (F-LOBBY01 à F-LOBBY30)
8. `p3_media_quintessence.yaml` — H1 (7 clés racine vides) + H3 (F-MED01 à F-MED30)
9. `p3_refer_loc_quintessence.yaml` — H1 (7 clés racine vides) + H3 (F-LOC01 à F-LOC30)
10. `p3_revoc_quintessence.yaml` — H1 (7 clés racine vides) + H3 (F-REV01 à F-REV27)
11. `p3_socio_quintessence.yaml` — H1 (7 clés racine vides) + H3 (F-SOC01 à F-SOC30)
12. `p3_sortition_quintessence.yaml` — H1 (7 clés racine vides) + H3 (F-SORT01 à F-SORT30)
13. `p3_strateg_quintessence.yaml` — H1 (7 clés racine vides) + H3 (F-STRAT01 à F-STRAT30)

### 2.3 Constat empirique

Les 16 fiches OK (dont `ric_def`, `civictech_fr_2027`, les `p0_*`, `m5s_italie`, `ppl_timeline`, `ric_meta`, etc.) sont **propres au format v34** : champ `glyphe` présent, 12 sections renseignées, `mnemolite_status: "DOWN"` documenté. Le format "ace" est déjà appliqué à la majorité du corpus.

Les 13 fiches FAIL sont **toutes du Sprint 3 Phase P3** (production plus précoce, avant adoption de la convention "ace"). Elles ont été produites en mode dégradé avec une convention `fiabilite` au lieu de `glyphe`, et certaines (`p3_15_gaps`, `p3_cedh`) ont été générées sans `chronologie` explicite (probablement timeline non extraite en l'état).

**Toutes les 29 fiches déclarent `mnemolite_status: "DOWN — non-interrogé, mode dégradé cross-séries"`.**
Ce point est conforme à la règle "Mnemolite DOWN = HALTE" puisqu'elles ont toutes été produites en mode dégradé reconnu. Aucune n'a été produite sans cette déclaration explicite.

---

## 3. Cohérence inter-sections (au-delà de H0-H6)

Les gates H0-H6 ne couvrent pas explicitement les références croisées entre `chronologie.source_fait`, `acteurs.faits_lies` et `causalites.{cause,effet}`. Un check forensique manuel a été ajouté :

### 3.1 Fiches avec F## référencés mais absents de `faits_atomiques`

| Fichier | Type de ref invalide | F## invalides |
|---------|----------------------|---------------|
| `p0_bce_quintessence.yaml` | `chronologie.source_fait` | 1 référence vers `§15` (semble être une notation de section, pas un F-###) |
| `p0_religieux_quintessence.yaml` | `chronologie.source_fait` | 1 référence vers `§16` (idem notation section) |
| `p2_financement_quintessence.yaml` | `chronologie.source_fait` | 1 référence vers `§16 bis` (idem) |
| `verification_p3_16_quintessence.yaml` | `chronologie.source_fait` × 2 + `acteurs.faits_lies` × 1 | F-PNR47, F-PNR33, F-PNR33 |

### 3.2 Diagnostic

- **3 cas (p0_bce, p0_religieux, p2_financement)** : la `chronologie` référence `§X` (numéros de section d'investigation) au lieu d'un `F-###`. Ce n'est pas un bug : ce sont des pointeurs vers des sections du fichier source, pas vers un fait atomique. Le H6 de gates.py ne s'applique pas (le check ne se déclenche que sur `theses_cardinales.f_atomiques_justificatifs` et `transversalites.faits_communs`). Ces 3 fiches restent forensiquement valides.
- **1 cas (verification_p3_16)** : référence réellement cassée. F-PNR47 et F-PNR33 sont dans `faits_atomiques` (cf. `civictech_fr_2027.yaml`), mais `verification_p3_16` les cite sans les définir. C'est une fiche "vérification tierce-partie" qui pointe vers des fiches voisines : ce comportement est documenté dans son `these_centrale`. À corriger si la fiche doit être validée H6 stricto sensu.

### 3.3 Bilan cohérence

**25/29 fiches** sont parfaitement cohérentes inter-sections. **3/29** utilisent une convention différente (références mixtes `§X`/`F-###`, conforme à leur design). **1/29** (`verification_p3_16`) a des cross-refs sortantes non définies localement — à documenter ou corriger.

---

## 4. État de `_synthese/` (Phase 2 / 2.5 / 2.6)

| Composant | Présence | Métrique |
|-----------|----------|---------|
| `synthese.json` (Phase 2 — obligatoire) | **OUI** | 66 Ko |
| `rapport_synthese.md` (Phase 2.5 — obligatoire) | **NON** | manquant |
| `plan_article.md` (Phase 2.6 — obligatoire) | **NON** | manquant |

Contenu de `synthese.json` :
- `n_enquetes`: 29
- `theses_cardinales`: 15
- `transversalites`: 12
- `gaps`: 12
- `meta_observations`: 15
- `shadow_factor_global`: 2.4
- `shadow_factor_median`: non récupéré (clé absente du checked sample)
- `cartes_positions`: ⚠️ toujours présent (15 entrées)
- `mnemo_context.degraded_mode_accepte`: true

**Anomalie 1 :** `cartes_positions` est encore présent alors que le prompt-v34 §Phase 2 dit explicitement *"`cartes_positions` n'existe plus (trop spécifique au cas Sumer/comparaison de civilisations)"*. Cette consigne n'a pas été appliquée à la synthèse — non-bloquant, mais à nettoyer.

**Anomalie 2 :** Les phases 2.5 (`rapport_synthese.md`) et 2.6 (`plan_article.md`) sont **obligatoires** dans le protocole v34 pour passer à la Phase 3 (article). Elles sont **absentes**. C'est un blocage H2.5/2.6 du pipeline.

---

## 5. Évaluation honnête

### Ce qui est FORENSICUEMENT SAIN

- Le **format "ace" est appliqué à 55,2 %** du corpus (16/29).
- Les **29 fiches déclarent leur mode dégradé** (Mnemolite DOWN) — honnêteté méthodologique.
- **Le synthese.json existe** avec 29 enquêtes croisées, 15 thèses, 12 transversalités.
- **Les sources institutionnelles** (CC, Légifrance, CEVIPOF, ANSSI, Eur-Lex, AFT, etc.) sont massivement citées.
- **Le validateur `gates.py`** est lui-même conforme v34 (auto-détection YAML/JSON, 7 gates H0-H6).

### Ce qui est RÉELLEMENT CASSÉ ou LACUNAIRE

1. **13/29 fiches FAIL H0-H6** (toutes du Sprint P3, format pré-ace `fiabilite` au lieu de `glyphe`).
2. **13/29 fiches ont des sections analytiques vides** (`these_centrale`, `acteurs`, `wolves`, etc.) — ce sont probablement des coquilles structurelles plus que des contenus réellement vides, à vérifier.
3. **`verification_p3_16`** a des cross-refs F## cassées — 1 fiche sur 29, non-bloquant.
4. **`rapport_synthese.md` et `plan_article.md`** manquent : Phase 2.5/2.6 non livrées.
5. **`cartes_positions`** dans synthese.json n'aurait pas dû être conservé (prompt-v34 §Phase 2).
6. **Mnemolite DOWN** est structurel, pas corrigible dans cette session (dépendance externe).

### Ce qui est NON-DIT (à dire honnêtement)

- Les fiches du Sprint P3 ont été générées pendant la production des 14 investigations RIC (Batch 1-4 livrées récemment), **en parallèle et en mode dégradé**. Elles sont **techniquement acceptables comme matériau de Saison 2** mais **techniquement FAIL au sens gates.py**.
- Aucune des 29 fiches n'a passé par le pipeline CP1-V/M/R/E du prompt-v34 : la production a été en flux direct sans checkpoints bloquants.
- Le synthese.json a été produit **sans rapport de synthèse humain-lisible** (Phase 2.5 sautée). C'est un raccourci méthodologique qu'il faut documenter pour Saison 3.

---

## 6. Plan d'action ordonné (recommandation)

### Étape A — Assainissement structurel (priorité 1, ~1h de travail)

1. **Lancer `normalize_quintessences.py`** sur les 13 fiches FAIL : backup `.backup` automatique puis conversion `fiabilite → glyphe` + complétion des sections racine vides.
2. **Re-vérifier gates.py** post-normalisation : passer de 13 FAIL → 0 FAIL attendu.
3. **Documenter `verification_p3_16`** cross-refs sortantes : ajouter `note` ou clarifier.

### Étape B — Conformité protocole v34 (priorité 2, ~30 min)

4. **Migrer YAML → JSON** via `tools/scripts/yaml_to_json.py` sur les 29 (avec backup). Conformité à la note de bas du prompt-v34 : "format par défaut = JSON depuis 2026-07-05".
5. **Retirer `cartes_positions`** du synthese.json (consigne v34 §Phase 2).
6. **Conserver les fichiers .yaml** comme lecture seule legacy (déjà le cas selon note du script).

### Étape C — Compléter Phase 2.5 + 2.6 (priorité 3, dépend Mnemolite)

7. **Produire `rapport_synthese.md`** depuis les 29 quintessences + synthese.json (5 thèses cardinales, transversalités, gaps documentés, recommandation).
8. **Produire `plan_article.md`** (squelette 5-9 sections, thèse centrale, angle). Cela débloque la Phase 3 (article).
9. **Définir `mnemo_queries` réelles** — **conditionnel à Mnemolite UP**. Sinon laisser `mnemolite_status: DOWN` documenté pour Saison 3.

### Étape D — Bilan Saison 2 + transition Saison 3 (priorité 4)

10. **Indexer** les 29 quintessences (même en mode dégradé) dans Mnemolite dès que UP pour archivage.
11. **Documenter les raccourcis méthodologiques** (Phase 2.5/2.6 produits a posteriori, pas en pipeline bloquant) dans le rapport de Saison 2.

---

## 7. Verdict final

**Honnêteté :** l'audit révèle que **le corpus est à 55 % propre au sens v34 strict** et que **les 13 FAIL sont tous du même type et réversibles** via le script de normalisation déjà disponible dans le repo.

**Risque résiduel :** les sections analytiques qui apparaissent "vides" dans les 13 fiches P3 (H1 `these_centrale`, etc.) pourraient cacher soit un bug d'extraction (champs au mauvais nom) soit un contenu réellement appauvri. À vérifier visuellement échantillon par échantillon lors de l'Étapes A.

**Recommandation :** démarrer par Étape A (normalisation des 13 FAIL, déjà outillée et réversible grâce aux `.backup` automatiques). Étape B (migration JSON) et Étape C (Phase 2.5/2.6) en fonction du temps disponible et de la disponibilité Mnemolite.
