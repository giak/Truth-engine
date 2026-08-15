# SUBLIMATOR : Architecture et graphe de dépendances

**Rôle :** source unique de vérité sur le fonctionnement du moteur Sublimator : mission, phases, prompts, checkpoints humains, flux de données et validation.
**Dernière mise à jour :** 2026-08-03
**Position dans la chaîne :** Truth Engine (enquête) → **Sublimator (condensation)** → Writer (rédaction et audits)

---

## §1 Mission et position

Sublimator transforme **N enquêtes journalistiques** (dossiers APEX / INVESTIGATION produits par Truth Engine) en **1 article publiable**, avec traçabilité forensique complète : chaque fait conserve une trace vers sa source (`[Lxx]`, identifiants `F-##` / `M1-M4`, URLs vérifiées).

**Trois principes transverses :**
- **Zéro hallucination** : tout `F-##`, `M-##`, acteur, source ou date cité doit exister verbatim dans une entrée ingérée. Omettre en cas de doute.
- **Zéro em-dash (U+2014) dans les articles publiés** (Phase 3). Utiliser « : » avec espace insécable, « - » pour les listes, parenthèses pour les incises. Les fiches internes (quintessences, rapports) tolèrent l'em-dash.
- **Zéro flagornerie, français soutenu** : pas de « excellente question », pas d'anglicisme non justifié.

**Versioning par snapshot de phase.** Le pilote historique `prompt-v35.md` (monolithique, Phases 1-3 + orchestration) est archivé. Il a été remplacé par des prompts isolés par phase : v36 (Phase 1), v37 (Phase 2), phase2_5 (raisonnement narratif), v38 (Phase 3).

---

## §2 Inventaire des fichiers

### Prompts (source unique de vérité par phase)

| Fichier | Phase | Rôle |
|---------|-------|------|
| `prompt-v36.md` | 1 | Extraction d'1 enquête → 1 quintessence canonique 9 sections H2 |
| `prompt-v37_phase2.md` | 2 | Synthèse par auto-clustering topologique → rapport 9 H2, 5 thèses cardinales |
| `prompt-phase2_5_raisonnement_narratif.md` | 2.5 | Raisonnement narratif (Q0-Q8) → `blueprint_narratif.md` (Blocs A/B/C) |
| `prompt-v38_phase3.md` | 3 | Rédaction d'article Substack publiable (LOIS, édict cumulatif, méthode inverse) |
| `prompt-v35.md` | 1-3 | Pilote monolithique historique (archivé, référence infrastructurelle) |

### Sous-prompts d'orchestration (`prompts/`)

| Fichier | Sous-agent | Rôle |
|---------|-----------|------|
| `quintessence_reader.md` | LECTEUR | Lit l'enquête source, mesure les positions (équivalent `grep -n`) |
| `quintessence_extractor.md` | EXTRACTEUR | Extrait les faits atomiques selon la charte v2 (VERBATIM) |
| `quintessence_critic.md` | CRITIQUE | Audit de la quintessence produite (optionnel §13.5) |
| `quintessence_orchestrator.md` | ORCHESTRATEUR | Boucle de régénération ciblée, max 3 itérations (`iteration_count`) |
| `validation_3enquetes.md` | Protocole §13.5 | Ré-exécution de validation, rejouable sur tout hôte LLM |

### Spécifications (SPECS)

| Fichier | Contenu |
|---------|---------|
| `2026-07-06_v40_phase1_REEL_SPECS.md` | SPECS Phase 1 « v2 KISS » (mission : extraction sans anticipation aval) |
| `2026-07-06_v39_sublimator_pipeline_complet_SPECS.md` | Pipeline complet 5 phases + 2 checkpoints, LOI Phase 3, KPIs bout-en-bout |
| `2026-07-06_15-00_v38_dossier_forensique_redaction_SPECS.md` | Dossier forensique Phase 1 (10 sections, traces, métriques M1-M8) |
| `2026-07-05_15-00_v36_preservation_phases_analytiques_SPECS.md` | Préservation des phases analytiques (option C) |
| `2026-07-06_10-00_v37_compress_summary_only_SPECS.md` | Compression `compress_summary` (100 mots) |

### Audits et rapports

| Fichier | Contenu |
|---------|---------|
| `AUDIT_ANTAGONISTE_v35_2026-07-05.md` | 16 contradictions (9 P1, 7 P2), résolues 16/16 |
| `AUDIT_ANTAGONISTE_v36_ROUND1_2026-07-05_CADRAGE.md` | Cadrage de l'audit v36 |
| `AUDIT_ANTAGONISTE_v36_ROUND2_VERDICT_2026-07-05.md` | Verdict v36 (2 BLOQUANTS, M9 non mesurable) |
| `RAPPORT_MULTI_AGENT_44_ENQUETES_v35_2026-07-05.md` | Audit multi-agent 44 enquêtes (7 questions, 7 preuves) |
| `DIAGNOSTIC_MNEMOLITE_v34.md` | Diagnostic du contrat Mnemolite |
| `_artifacts/` | Journaux d'import, PID, progress (opérationnel) |
| `archive/` | Documents v33.x et v34 (guide, design, spec, prompt-v34.md) |

### Scripts d'audit externes (dans `tools/`)

| Script | Cible |
|--------|-------|
| `tools/audit_phase1_sublimator_v35.py` | Vérification algorithmique des quintessences Phase 1 (C1, C2, C5, C6, C7, C10 ; C3 neutralisé) |
| `tools/audit_phase2_sublimator_v37.py` | Cross-check du rapport Phase 2 vs source `_quintessence_v3/` (C0-C6) |

---

## §3 Chaîne de phases (6 étapes)

```
N enquêtes (investigations/<sujet>/)
   │
   ▼
Phase 1  (prompt-v36)         extraction : 1 quintessence / enquête
   │                          → _quintessence/  (9 sections H2 canoniques)
   ▼
Phase 1.5                     compression : compress_summary (~100 mots)
   │
   ▼
Phase 2  (prompt-v37)         synthèse par auto-clustering topologique
   │                          → _synthese/rapport_synthese_phase2.md (9 H2, 5 thèses)
   │  ◄── CP1 (checkpoint humain, recommandation binaire)
   ▼
Phase 2.5 (prompt-phase2_5)   raisonnement narratif Q0-Q8
   │                          → _synthese/blueprint_narratif.md (Blocs A/B/C)
   │  ◄── CP1.5 (checkpoint humain)
   ▼
Phase 2.6                     plan d'article → _synthese/plan_article.md
   │
   ▼
Phase 3  (prompt-v38)         rédaction d'article
   │                          → articles/YYYY-MM-DD_HH-MM_<sujet>_ARTICLE.md
   │  ◄── CP2 (checkpoint humain) puis publication Substack (CP3)
```

**Phase 1 : Extraction.** Une quintessence par enquête, format canonique strict : 9 sections H2 numérotées 1-9 (Métadonnées & trace source, Faits atomiques préservés, Acteurs nominaux, Sources externes citées, Chronologie datée, Mécanismes / chaînes causales, Verbatim et citations, Notes méthodologiques source, Limites connues de cette extraction). Garde anti-dérive : maximum 4 mécanismes (M1-M4), les écartés sont signalés en §9. Auto-évaluation 5 critères [GO] (C0 anti-dérive structurelle, C1 noms canoniques, C2 exhaustivité F-##, C4 traçabilité [Lxx], C5 refus Phase 1). Aucune émission si un critère est NON.

**Phase 2 : Synthèse.** Rapport unique 9 H2, auto-clustering **topologique** (définition mathématique, pas sémantique) : un cluster = ensemble de ≥2 acteurs/M-## co-occurrents dans ≥4 quintessences (seuil plancher `max(4, ceil(N/10))`). 5 thèses cardinales, chacune avec étendue `(N fiches / N total)`, score de Solidité shadow (formule pondérée), niveau de confiance sur 4 crans, « pourquoi », « pourquoi pas », réfutation, F-##/M-## sous-jacents. §9 : recommandation binaire `<RECOMMANDATION:OUI|NON>` (CP1). Anti-patterns verrouillés : clustering sémantique « vibe » interdit, saut de niveau probatoire interdit (niveau 1 ≠ niveau 3), score gonflé interdit.

**Phase 2.5 : Raisonnement narratif.** Prompt interrogatif (Q0-Q8) : sujet et mode (essai/enquête), fait qui surprend, tension dramatique, thèse ou thèse organisatrice, angle (catalogue : autopsie, procès, contre-enquête, anatomie, paradoxe, fresque…), arc narratif, coupe (essai) ou orchestration (enquête : phares/appui/contexte), KO sentences, question ouverte. Sortie : blueprint en 3 blocs (matrice de décision, plan article, liste de coupe ou cartographie du corpus). Contraintes : une thèse, pas cinq ; KO sentences vérifiables sans inférence ; lexique de gradation des niveaux probatoires ; usage réglementé du mot « propagande ».

**Phase 3 : Rédaction.** L'article consomme le rapport Phase 2 (matériau factuel) et le blueprint (décisions éditoriales : le blueprint prime). Doctrine : édict cumulatif (chaque mécanisme déjà documenté est cité avec URL, pas réexpliqué), méthode inverse (partir du fait brut, remonter la chaîne causale), anti-sycophantie, concepts ≠ données. Calibration stylistique par 3 transformations : hyper-explicitation → asyndète, périphrase → apposition, sur-assertion → modalisation. Diagnostic pré-rédactionnel obligatoire (interne, jamais publié). Auto-audit antagoniste avant émission.

---

## §4 Checkpoints humains

| Checkpoint | Position | Décision |
|-----------|----------|----------|
| CP1 | Fin Phase 2 | V/M/R/E sur la recommandation binaire (`<RECOMMANDATION:OUI|NON>`) |
| CP1.5 | Fin Phase 2.5 | V/M/R/E sur le blueprint (thèse, angle, arc, coupe) |
| CP2 | Fin Phase 3 | V/M/R/E sur l'article + auto-audit (mots, thèse, URLs, audit L8) |
| CP3 | Publication | Relecture humaine complète avant mise en ligne Substack |

Actions : **V** valider, **M** modifier, **R** refuser (retour phase amont, max 3 refus), **E** enrichir. Une seule passe par checkpoint : pas de régénération sans action humaine. L'état est préservé entre les refus (les fichiers déjà produits sont sauvés).

---

## §5 Flux de données

```
investigations/<sujet>/_quintessence/   ← 36 fichiers (35 strates + synthèse terminale, cas Fedorova)
investigations/<sujet>/_synthese/       ← rapport_synthese_phase2.md, blueprint_narratif.md, plan_article.md
articles/YYYY-MM-DD_HH-MM_<sujet>_ARTICLE.md
substack-online/index.md                ← indexation après CP3
```

- Identifiants : `F-[A-Z]+-\d+` (faits atomiques), `M1-M4` (mécanismes), traces `[Lxx]` avec marque `(mesuré)` ou `(estimé)`.
- Chaque fait du registre doit avoir une URL cliquable pointant vers une page spécifique (jamais une racine de domaine).

---

## §6 Contrat Mnemolite

- **v35** : `get_system_snapshot` au démarrage, **HALTE** si DOWN (aucun fichier produit).
- **v37** : mode dégradé par défaut : §5 commence par `[HALTE_APPEL: Mnemolite distant injoignable. Aucun ajout externe effectué.]`. Pas d'invention de contenu Mnemolite.
- **v38** : Mnemolite indisponible en Phase 3, pas d'apport externe.
- Règle commune : `search_memory(..., search_mode="hybrid", ...)` obligatoire quand le branchement existe.

---

## §7 Validation

1. **Auto-évaluation [GO]** par phase : C0-C5 (Phase 1), C0-C6 (Phase 2). Aucune émission si un critère est NON.
2. **Auto-audit antagoniste** Phase 3 (LOI L8) : 6 types de failles (logique, mots-tic, micro-définitions, équation synthèse, sourcing, ton).
3. **Sub-agent CRITIQUE** (`prompts/quintessence_critic.md`), invoqué via `filePaths` après chaque quintessence.
4. **Checklists manuelles du pilote** aux checkpoints CP1/CP1.5/CP2/CP3.
5. **Scripts d'audit** : `tools/audit_phase1_sublimator_v35.py`, `tools/audit_phase2_sublimator_v37.py`.

### Métriques

| Groupe | Métriques | Seuils GO (exemples) |
|--------|-----------|----------------------|
| Phase 1 | M1-M8 (Jaccard thèse, intersection F##, hallucination F##/impact, JSON parse, volume tokens, latence, score critic) | M1 ≥ 0.7, M3/M4 < 5 %, M5 = 100 % |
| Phase 2 | N2.1-N2.4 (F-## partagés par cluster, transversalités, JSON valides) | ≥ 3 F-## / cluster |
| Phase 2.5 | N2.5.1-N2.5.4 (thèse fil rouge, transversalités, recommandation, volume) | 5/5 sections |
| Phase 3 | M3.1-M3.6 (volume, sources, cross-links, gras, lexique L4, compliance LOI L9) | 3000-5000 mots (essai), sources ≥ 5 § |
| Bout-en-bout | E2E.1-E2E.4 (latence, réutilisation F-## ≥ 70 %, transversalités, conformité LOI L9) | variable |

---

## §8 Problèmes connus et dette technique

- **Validation algorithmique Python retirée (2026-07-06)** : `sublimator_validate.py` / `sublimator_retry.py` ne portent plus la conformité ; elle est portée par le sub-agent CRITIQUE et les checklists manuelles. Tests et références stale purgés le 2026-08-15.
- **Drift de numérotation des LOIS Phase 3** : le README cite 8 LOIS, SPECS v39 formalise L1-L9, `prompt-v38` référence « Lois 1-16 ». À unifier.
- **Drift de volumétrie Phase 3** : SPECS v39 impose 3000-5000 mots ; `prompt-v38` admet 2200-2800 (essai) et 5000-8000 (enquête). À clarifier.
- **Drift des checkpoints** : GUIDE.md (v34) décrit 4 checkpoints (CP1 par enquête, CP2, CP2.5, CP3) ; le pipeline v35+ n'en garde que 2 actifs (CP1, CP2) auxquels phase2_5 ajoute CP1.5. GUIDE.md est obsolète.
- **M9 non mesurable empiriquement** : le compteur de violations d'isolation dépend du tagging LLM `sublimator:enquete_id`, non garanti par le code.
- **Phase 0 supprimée (2026-07-05)** : `cartographie.json` retiré comme overengineering. `extractors/` ré-hébergé le 2026-08-15 avec `gates.py` (H0-H7) + `head_check.py` (HEAD-check anti-SSRF), sans `cartographie.py`.
- **Mnemolite aspirationnel** : le contrat inter-phases est documenté (SPECS v39 §7.5) mais pas branché ; la validation repose sur checklists + CRITIQUE.

---

## §9 Recommandations

| ID | Action | Effort | Impact |
|----|--------|--------|--------|
| R1 | Aligner la numérotation des LOIS (README 8 / SPECS L1-L9 / v38 1-16) | 30 min | HAUT |
| R2 | Réconcilier GUIDE.md (v34) avec le pipeline v36-v38 (2-3 CP) | 30 min | MOYEN |
| R3 | Purger les références aux validateurs Python et à la Phase 0 dans `tests/` | 1 h | MOYEN |
| R4 | Créer `tools/audit_phase3_em_dash.py` (audit zéro em-dash des articles, cf. `knowledge.md`) | 30 min | HAUT |
| R5 | Instrumenter E2E.1-E2E.4 sur un corpus de 5+ enquêtes avant industrialisation | 2 h | HAUT |

---

*Architecture v1 : Sublimator. Dernière mise à jour : 2026-08-03. Source vivante : `tools/engines/sublimator/`. Les copies figées dans un dossier d'enquête (`10_protocole/`) sont des instantanés datés.*
