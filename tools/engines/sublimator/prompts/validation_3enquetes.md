# validation_3enquetes.md — Protocole de validation empirique §13.5

> **Source canonique** : `tools/engines/sublimator/2026-07-05_15-00_v36_preservation_phases_analytiques_SPECS.md`, §13.5 + §13.7
> **Date de transcription** : 2026-07-05
> **Statut** : protocole de ré-exécution. Rejouable sur n'importe quel hôte LLM (le modèle cible est configurable ; ne pas présumer d'un fournisseur particulier).
> **Cible** : 3 enquêtes × 3 runs indépendants × 4 agents (LECTEUR + EXTRACTEUR + CRITIQUE + ORCHESTRATEUR interne) — 36 appels LLM en mode full-pipeline.
> **Cible réduite documentée dans `validation_report_3x3.md`** : exécution réelle sur proxy LLM (Gemini via `thinker-with-files-gemini`).

---

## 1. Cible et hypothèses

### 1.1 Trois enquêtes représentatives des archétypes dominants (SPECS §12.3)

| Archétype | Enquête | Justification |
|-----------|---------|---------------|
| **GOLDEN_APEX** | `investigations/2026-07-04-RIC/2026-07-05_15-00_histoire_longue_ric_france_1789_2026_INVESTIGATION.md` | KERNEL complet (15 symboles), F## structurés (21 F-HIST), format canonique, 7393 mots |
| **NARRATIF_STANDARD** | `investigations/2026-07-04-RIC/2026-07-04_20-30_ric_bloc_religieux_verrou_INVESTIGATION.md` (référencée §3 + §10) | Cas d'étude, 16 sections, KERNEL partiel, 6967 mots |
| **FAST_REPORT** | `investigations/2026-07-04-RIC/2026-07-05_18-00_cultes_4_religions_france_position_RIC_INVESTIGATION.md` | KERNEL perdu (0 symbole), 13 F-CU ⁅, format MANIPULATION_REPORT Saison 2, 3342 mots |

### 1.2 Trois runs indépendants par enquête

Pour chaque enquête, exécuter **3 sessions LLM distinctes** (séparées par reset de context ou nouveau thread), pour mesurer la variance inter-runs.

### 1.3 Trois agents enchaînés par run (le parent orchestre)

```
[Agent 1 LECTEUR] → lecture_annotee.md
       ↓
[Agent 2 EXTRACTEUR] → quintessence.json
       ↓
[Agent 3 CRITIQUE] → critique.json (scores 1-10 par champ)
       ↓
[Orchestrateur humain = parent Sublimator] → décision go/no-go de régénération ciblée
```

## 2. Métriques à mesurer (SPECS §13.5.2)

| # | Métrique | Méthode | Cible go | Cible no-go |
|---|----------|---------|----------|-------------|
| M1 | **Variance these_centrale** | Jaccard similarity (bag-of-words lemmatisé) sur 3 outputs | ≥ 0.7 | < 0.5 |
| M2 | **Variance faits_atomiques** | `# F## communs / # F## total` sur 3 outputs | ≥ 0.6 | < 0.4 |
| M3 | **Hallucination F##** | re.search chaque F-### cité dans l'enquête source | < 5% | > 15% |
| M4 | **Hallucination impact** | re.search chaque chiffre cité dans l'enquête source | < 5% | > 15% |
| M5 | **Conformité JSON** | `json.loads()` succès sur 100% des outputs | 100% | < 95% |
| M6 | **Volume tokens** | Compteur exact de l'hôte LLM (input_tokens + output_tokens sommés) | < 50K tok/enquête | > 100K |
| M7 | **Latence** | Mesure real-time (3 agents séquentiels) | < 10 min/enquête | > 20 min |
| M8 | **Score critic** | Moyenne des scores par champ | ≥ 7 | < 5 |

## 3. Critères go / no-go (SPECS §13.5.3)

**GO** (industrialisation sur les 41 enquêtes restantes) :
- M1 ≥ 0.7 ET ≥ 6/8 métriques dans cible go.
- ET M3 < 5% ET M4 < 5%.

**NO-GO** (révision prompts avant industrialisation) :
- M1 < 0.5 OU > 2/8 métriques dans cible no-go.
- OU M3 > 15% OU M4 > 15%.

**PIVOT** : intermédiaire (révision ciblée ou simplification architecture).

## 4. Protocole d'exécution

### 4.1 Préparation

```bash
# 1. Créer dossiers
mkdir -p investigations/2026-07-04-RIC/_validation/

# 2. Vérifier les 3 enquêtes cibles existent
ls -la investigations/2026-07-04-RIC/2026-07-05_15-00_histoire_longue_ric_france_1789_2026_INVESTIGATION.md
ls -la investigations/2026-07-04-RIC/2026-07-04_20-30_ric_bloc_religieux_verrou_INVESTIGATION.md
ls -la investigations/2026-07-04-RIC/2026-07-05_18-00_cultes_4_religions_france_position_RIC_INVESTIGATION.md

# 3. Confirmer source unique de vérité (Annexe A consolidée v36)
ls -la tools/engines/sublimator/prompt-v35.md

# 4. Vérifier validateurs Python (industrialisation §13.5)
ls -la tools/engines/sublimator/sublimator_validate.py
ls -la tools/engines/sublimator/sublimator_retry.py
```

### 4.2 Pour chaque enquête, pour chaque run (9 itérations)

**Étape A — LECTEUR :**
- Spawner un sous-agent LLM avec filePaths = [`tools/engines/sublimator/prompts/quintessence_reader.md`, `<enquête>.md`]
- Prompt : "Tu es l'Agent 1 (LECTEUR) défini défini dans `quintessence_reader.md`. Lis l'enquête et produis UNIQUEMENT le markdown structuré défini dans la section 'Format de sortie obligatoire' du prompt. Aucun commentaire autour."
- Capturer l'output dans `investigations/2026-07-04-RIC/_validation/{enquete_id}-reader-run{N}.md`

**Étape B — EXTRACTEUR :**
- Spawner un sous-agent LLM avec filePaths = [`tools/engines/sublimator/prompts/quintessence_extractor.md`, `<enquête>.md`, `investigations/2026-07-04-RIC/_validation/{enquete_id}-reader-run{N}.md`]
- Prompt : "Tu es l'Agent 2 (EXTRACTEUR) défini défini dans `quintessence_extractor.md` (v2 REVISION post-§13.5 NO-GO). Lis l'enquête + lecture annotée et produis UNIQUEMENT le JSON strict conforme au schéma 'Schéma cible' du prompt (6 req + 6 opt v35 + 4 nouveaux v36). Aucun commentaire."
- Capturer l'output dans `investigations/2026-07-04-RIC/_validation/{enquete_id}-quintessence-run{N}.json`

**Étape C — CRITIQUE (optionnel depuis §13.5, sublimator_validate.py suffit en pratique) :**
- Spawner un sous-agent LLM avec filePaths = [`tools/engines/sublimator/prompts/quintessence_critic.md`, `<enquête>.md`, `investigations/2026-07-04-RIC/_validation/{enquete_id}-reader-run{N}.md`, `investigations/2026-07-04-RIC/_validation/{enquete_id}-quintessence-run{N}.json`]
- Prompt : "Tu es l'Agent 3 (CRITIQUE) défini défini dans `quintessence_critic.md`. Lis l'enquête + lecture + quintessence et produis UNIQUEMENT le JSON critique conforme au schéma 'Schéma de sortie' (scores + verdict_global + champs_a_regenerer)."
- Capturer l'output dans `investigations/2026-07-04-RIC/_validation/{enquete_id}-critique-run{N}.json`

**Étape D — ORCHESTRATEUR (optionnel, pour test full-pipeline 4 agents SPECS §13.5.1) :**
- Spawner un sous-agent LLM avec filePaths = [`tools/engines/sublimator/prompts/quintessence_orchestrator.md`, `<enquête>.md`, `investigations/2026-07-04-RIC/_validation/{enquete_id}-reader-run{N}.md`, `investigations/2026-07-04-RIC/_validation/{enquete_id}-quintessence-run{N}.json`, `investigations/2026-07-04-RIC/_validation/{enquete_id}-critique-run{N}.json`]
- Prompt : "Tu es l'Agent 4 (ORCHESTRATEUR) défini défini dans `quintessence_orchestrator.md`. Tu coordonnes la chaîne LECTEUR → EXTRACTEUR → CRITIQUE selon la boucle du prompt. Produis la quintessence_finale + log des itérations effectuées."
- Capturer l'output dans `investigations/2026-07-04-RIC/_validation/{enquete_id}-orchestrator-run{N}.json`

> **Note** : le mode 3-agents (LECTEUR+EXTRACTEUR+CRITIQUE) produit **27 appels LLM** (sans orchestrateur) suffisant pour valider variance + hallucination + score critic. Le mode 4-agents + orchestrateur produit **36 appels** et permet aussi de tester la boucle de régénération ciblée. Cible par défaut de cette exécution : 4 agents × 3 runs × 3 enquêtes = **36 appels LLM** (décomposition ci-dessus).

### 4.3 Calcul des 8 métriques

Script Python (cf. `validation_report_3x3.md` § implémentation) :
- M1 (Jaccard these_centrale) : `set(tokens).intersection / set(tokens).union` sur les 3 outputs
- M2 (intersection F##) : `#(F## ∩ ensemble) / #(F## ∪ ensemble)`
- M3 (hallucination F##) : pour chaque F-cité, `enoncé in source` (re.search case-insensitive)
- M4 (hallucination impact) : pour chaque chiffre cité, `chiffre in source` (substring)
- M5 (JSON parse) : `json.loads()` success/failure
- M6 (volume tokens) : input_tokens + output_tokens sommés du compteur hôte. **Note** : cette métrique mesure le volume consommé, pas le coût monétaire (la valorisation économique dépend de la grille tarifaire du fournisseur, qui est hors-scope de cette validation).
- M7 (latence) : timestamps début/fin par run
- M8 (score critic) : moyenne des `scores.*.score` par run

## 5. Livrables attendus (SPECS §13.5.4)

- 1 fichier `validation/validation_report_3x3.md` avec :
  - Les 9 quintessences (3 archétypes × 3 runs).
  - Le tableau des 8 métriques par enquête (3 × 8 = 24 mesures).
  - Le verdict GO/NO-GO/PIVOT argumenté.
- 1 note méthodologique : quels prompts ont été modifiés entre runs, quelles erreurs détectées, quelles mitigations proposées.

## 6. Volume de tokens attendu (SPECS §13.5.5 — section ré-écrite : voir note méthodologique)

3 enquêtes × 3 runs × 3 prompts × ~16K tokens input + ~150K tokens output total = ~500K input + ~150K output.

**Note méthodologique** : ce volume est une estimation architecturale (27 appels LLM × taille moyenne). Le coût monétaire associé dépend **intégralement** de l'hôte LLM cible et de sa grille tarifaire au moment de l'exécution. Sur hôte gratuit (proxy LLM, API en quota libre, modèle local), le coût effectif est 0. Sur hôte payant, se référer à la grille publiée par le fournisseur — aucune projection chiffrée n'est faite ici pour ne pas figer des valeurs qui deviendraient vite obsolètes et qui ne sont pas vérifiées empiriquement.

## 7. Notes d'adaptation proxy

Pour la présente exécution sur proxy LLM (Gemini 2.5 Pro via `thinker-with-files-gemini`) :
- Le proxy peut produire du markdown narratif au lieu de strict JSON dans certains cas (M5 chutera).
- Le coût effectif est 0 sur hôte proxy gratuit (Gemini via `thinker-with-files-gemini` dans cette exécution).
- La latence est mesurée en temps réel Sublimator-side, pas par le compteur interne du LLM.

**Toutes les mesures obtenues via proxy sont des explorations directionnelles, non des chiffres de production.** Pour une mesure canonique, rejouer ce protocole sur l'hôte LLM cible (modèle à choisir selon contraintes budgétaires et de qualité — cette validation ne fixe aucun hôte préférentiel).

---

> **FIN DU SPEC.** Transcription §13.5 + §13.7 du SPECS v36, avec adaptations documentées : §6 (suppression des projections monétaires non vérifiées empiriquement, remplacées par une note méthodologique sur la dépendance à l'hôte LLM cible) et §7 (adaptations proxy).
