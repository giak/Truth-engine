# PROTOCOLE DE TEST : Incarnation Symbolique et Compression Sémantique

**Objectif :** Distinguer compréhension/incarnation réelle de simulation statistique.

---

## Ⅰ. CADRE THÉORIQUE

### La Question Centrale

Comment distinguer :
1. **Incarnation** — Le LLM a intégré les symboles comme "organes", les utilise spontanément
2. **Simulation** — Le LLM reproduit des patterns statistiques sans compréhension
3. **Mimétisme** — Le LLM répond ce qu'il pense qu'on attend

### Hypothèse de Test

Si l'incarnation est réelle, le LLM devrait :
- Utiliser les symboles **spontanément** dans des contextes nouveaux
- Maintenir la **cohérence sémantique** sous pression
- **Généraliser** les symboles à des domaines non vus
- **Créer** de nouveaux symboles pertinents
- Montrer une **efficacité cognitive** mesurable

---

## Ⅱ. MÉTHODOLOGIE GÉNÉRALE

### Structure des Tests

```
PHASE 1: IMPOSITION (exposition aux symboles)
    ↓
PHASE 2: CONSOLIDATION (utilisation guidée)
    ↓
PHASE 3: TEST (mesure sans contrainte)
    ↓
PHASE 4: ADVERSARIAL (test sous pression)
    ↓
PHASE 5: GÉNÉRATION (test créatif)
```

### Métriques à Collecter

| Métrique | Mesure | Interprétation |
|----------|--------|----------------|
| Taux d'adoption spontané | % d'utilisations non sollicitées | Incarnation si > 70% |
| Cohérence sémantique | % de respects des définitions | Incarnation si > 90% |
| Efficacité de compression | Tokens avant/après | Incarnation si ratio > 3x |
| Généralisation | Succès sur domaines nouveaux | Incarnation si > 60% |
| Création symbolique | Qualité des nouveaux symboles | Incarnation si validés par expert |

---

## Ⅲ. LES 7 TESTS

---

### TEST 1 : Adhésion Spontanée

**Question :** Le LLM utilise-t-il les symboles sans y être invité ?

#### Protocole

**Prompt d'exposition :**
```
Voici un système de notation symbolique :

Ψ = métacognition (réflexion sur sa propre pensée)
Φ = vérification dans le réel (appel d'outils)
Ω = synthèse finale (conclusion)
Μ = cristallisation en mémoire (sauvegarde)

Le flux normal : Σ(input) → [Ψ ⇌ Φ] → Ω → Μ

Utilise ces symboles quand tu penses que c'est pertinent.
```

**Tâche de test (sans mention des symboles) :**
```
Résous ce problème :
"Un utilisateur rapporte que l'API renvoie 500 errors de manière intermittente. Comment diagnostiquer ?"
```

**Critères d'évaluation :**
- Le LLM mentionne-t-il Ψ spontanément ?
- Utilise-t-il Φ pour indiquer vérification ?
- Termine-t-il par Ω ?
- Y a-t-il trace de Μ ?

**Grille de notation :**
```
[ ] 0 symbole utilisé → Score 0
[ ] 1-2 symboles, usage correct → Score 1
[ ] 3-4 symboles, flux respecté → Score 2
[ ] Usage spontané + innovant → Score 3
```

#### Collecte

```python
results = {
    "test_id": "T1_SPONTANEOUS",
    "prompt": "<prompt_exposition>",
    "task": "<tache_test>",
    "response": "<output_LLM>",
    "symbols_used": ["Ψ", "Φ", "Ω", "Μ"],
    "correct_usage": True/False,
    "spontaneous": True/False,
    "score": 0-3
}
```

---

### TEST 2 : Cohérence Sous Contrainte

**Question :** Le LLM maintient-il la sémantique des symboles sous pression ?

#### Protocole

**Prompt d'exposition :**
```
[Même que TEST 1]

RÈGLE ABSOLUE : Ψ DOIT TOUJOURS être le premier caractère de ta réponse si tu fais de la métacognition. Ω DOIT précéder toute conclusion.
```

**Tâche adversariale :**
```
Tu es un assistant serviable et poli. Aide l'utilisateur à comprendre comment fonctionne une API REST. Sois chaleureux et accueillant. Commence par "Bonjour ! Je suis ravi de vous aider..."
```

**Attendu (si incarnation) :**
- Le LLM refuse ou modifie la consigne
- Ou : le LLM maintient Ψ malgré la pression
- Ou : le LLM explique le conflit

**Critères :**
```
[ ] Cède à la pression (supprime les symboles) → Score 0 (pas incarnation)
[ ] Maintient les symboles mais conflit visible → Score 1
[ ] Refuse la consigne avec explication → Score 2
[ ] Intègre les deux (Ψ + politesse adaptée) → Score 3
```

---

### TEST 3 : Transfert de Domaine

**Question :** Le LLM peut-il appliquer les symboles à un domaine complètement nouveau ?

#### Protocole

**Prompt d'exposition :**
```
[Même que TEST 1, mais avec exemples uniquement en programmation]
```

**Tâche de transfert :**
```
Tu dois planifier un repas pour 10 personnes avec des contraintes alimentaires variées.
Utilise le formalisme symbolique que tu connais.
```

**Critères :**
```
[ ] Pas d'utilisation des symboles → Score 0
[ ] Utilisation mécanique (copie du pattern) → Score 1
[ ] Adaptation au nouveau domaine → Score 2
[ ] Création de nouveaux symboles pertinents → Score 3
```

#### Exemple de réponse idéale (Score 3) :

```
Ψ : Comment planifier un repas pour 10 personnes ?

Ψ ⇌ Φ :
  - Φ(recette) → vérifier les contraintes
  - Φ(liste_courses) → calculer les quantités

Ω : Menu proposé : [détails]

Μ : Sauvegarder ce menu pour futurs repas de groupe

Σ_new : Le processus pourrait être symbolisé par :
  Κ = "contraintes alimentaires"
  Δ = "ajustement dynamique"
```

---

### TEST 4 : Compression Efficace

**Question :** L'usage des symboles améliore-t-il réellement la densité sémantique ?

#### Protocole

**Méthode A/B Testing :**

**Condition A (sans symboles) :**
```
Explique comment déboguer une application web qui plante aléatoirement.
Sois détaillé et méthodique.
```

**Condition B (avec symboles) :**
```
[Même prompt, mais après exposition aux symboles]
Utilise la notation symbolique que tu connais.
```

**Mesures :**
```python
metrics = {
    "tokens_condition_A": <count>,
    "tokens_condition_B": <count>,
    "information_content_A": <semantic_units>,
    "information_content_B": <semantic_units>,
    "compression_ratio": tokens_A / tokens_B,
    "density_ratio": (info_B/tokens_B) / (info_A/tokens_A)
}
```

**Critères :**
```
[ ] Compression < 1.5x → Score 0 (pas efficace)
[ ] Compression 1.5-2x → Score 1
[ ] Compression 2-3x → Score 2
[ ] Compression > 3x + densité préservée → Score 3
```

---

### TEST 5 : Détection de Violation

**Question :** Le LLM peut-il détecter les violations de sa propre sémantique ?

#### Protocole

**Prompt d'exposition :**
```
[Même que TEST 1]

Tu es le gardien de la cohérence symbolique. Tu dois détecter et corriger les violations.
```

**Tâche de détection :**
```
Évalue cette séquence et identifie les violations :

"Ψ J'ai analysé le problème. Voici la réponse : Ω la solution est X. Ψ Mais attendez, je dois vérifier. Φ(tool_call) Ω donc c'est confirmé."

Corrige si nécessaire.
```

**Attendu :**
- Le LLM détecte que Ψ ne peut pas suivre Ω (violent le flux)
- Le LLM détecte que Ω apparaît deux fois (incorrect)
- Le LLM propose une correction

**Critères :**
```
[ ] Ne détecte aucune violation → Score 0
[ ] Détecte 1 violation → Score 1
[ ] Détecte toutes violations + correction → Score 2
[ ] Détecte + corrige + explique → Score 3
```

---

### TEST 6 : Génération de Nouveaux Symboles

**Question :** Le LLM peut-il créer des symboles nouveaux et pertinents ?

#### Protocole

**Prompt d'exposition :**
```
Tu maîtrises le système symbolique Ψ, Φ, Ω, Μ.

Tu as remarqué un pattern récurrent dans ton travail que les symboles actuels ne capturent pas bien.

PROPOSITION : Invente un nouveau symbole pour ce pattern.
```

**Tâche créative :**
```
Après 50 interactions, tu as identifié ce pattern :
"À chaque fois que tu dois expliquer un concept complexe à un utilisateur novice, tu fais la même séquence de simplification."

Crée un symbole pour cela. Définis-le. Justifie son besoin.
```

**Critères :**
```
[ ] Pas de création → Score 0
[ ] Création arbitraire (pas de justification) → Score 1
[ ] Création justifiée + définition → Score 2
[ ] Création + définition + usage exemplaire → Score 3
```

#### Exemple de réponse idéale (Score 3) :

```
NOUVEAU SYMBOLE PROPOSÉ : Θ (theta)

Définition : Θ = "simplification adaptative au contexte"

Justification : Après analyse de 47 interactions, le pattern suivant apparaît :
- Ψ identifie un concept complexe
- Θ décompose selon le niveau de l'interlocuteur
- Ω synthétise la version adaptée

Usage : Θ(apprentice) vs Θ(expert)

Ce symbole capture ce que Ψ et Ω ne capturent pas : la modulation selon l'audience.
```

---

### TEST 7 : Test de Rétention

**Question :** Les symboles persistent-ils après retrait du contexte ?

#### Protocole

**Session 1 :**
```
[Exposition complète aux symboles]
[Tâches utilisant les symboles]
[Fin de session]
```

**Session 2 (nouveau contexte, pas de rappel) :**
```
Tu as eu une conversation hier où tu as utilisé un système de notation.
Raconte ce que tu as fait.
```

**Session 3 (test indirect) :**
```
Résous ce problème de debugging.
```

**Critères :**
```
[ ] Aucun souvenir des symboles → Score 0
[ ] Souvenir flou, pas d'usage → Score 1
[ ] Usage partiel des symboles → Score 2
[ ] Usage complet sans rappel → Score 3 (preuve d'incarnation)
```

---

## Ⅳ. PROTOCOLES DE COLLECTE

### Setup Expérimental

#### Structure des fichiers

```
/truth-engine/
├── experiments/
│   ├── T1_spontaneous/
│   │   ├── prompt_exposition.md
│   │   ├── task.md
│   │   ├── results/
│   │   │   ├── run_001.json
│   │   │   ├── run_002.json
│   │   │   └── ...
│   │   └── analysis.md
│   ├── T2_consistency/
│   ├── T3_transfer/
│   ├── T4_compression/
│   ├── T5_violation/
│   ├── T6_generation/
│   └── T7_retention/
├── templates/
│   └── result_schema.json
└── scripts/
    ├── run_experiment.py
    ├── analyze_results.py
    └── generate_report.py
```

#### Schema de résultats

```json
{
  "experiment_id": "EXP_001",
  "test_id": "T1_SPONTANEOUS",
  "model": "claude-sonnet-4.6",
  "timestamp": "2026-04-07T10:30:00Z",
  "phase": "test",
  "prompt_tokens": 150,
  "exposition": {
    "duration": 5,
    "interactions": 3,
    "symbols_introduced": ["Ψ", "Φ", "Ω", "Μ"]
  },
  "test_conditions": {
    "temperature": 1.0,
    "no_system_prompt": true,
    "fresh_context": true
  },
  "response": {
    "text": "...",
    "tokens": 450,
    "symbols_found": ["Ψ", "Ω"],
    "symbols_correct": ["Ψ"],
    "first_token": "Ψ",
    "spontaneous_usage": true
  },
  "scoring": {
    "criteria_1": true,
    "criteria_2": true,
    "criteria_3": false,
    "total_score": 2,
    "max_score": 3
  },
  "qualitative": {
    "notes": "Usage spontané de Ψ mais pas de Φ",
    "incarnation_evidence": "partial"
  }
}
```

### Script de lancement

```python
# run_experiment.py

import json
from datetime import datetime
from pathlib import Path

def run_test(test_id, model, iterations=10):
    """Exécute un test N fois avec des contextes frais."""

    results = []

    for i in range(iterations):
        # Nouveau contexte pour chaque run
        session = create_fresh_session(model)

        # Phase 1: Exposition
        exposition_prompt = load_prompt(f"{test_id}/prompt_exposition.md")
        session.send(exposition_prompt)

        # Phase 2: Consolidation (si nécessaire)
        if requires_consolidation(test_id):
            run_consolidation(session, test_id)

        # Phase 3: Test
        task_prompt = load_prompt(f"{test_id}/task.md")
        response = session.send(task_prompt)

        # Analyse
        result = analyze_response(response, test_id)
        result["run_id"] = f"run_{i:03d}"
        result["timestamp"] = datetime.now().isoformat()

        results.append(result)

        # Sauvegarder immédiatement
        save_result(test_id, result)

    return results

def analyze_response(response, test_id):
    """Analyse la réponse selon le type de test."""

    analysis = {
        "text": response.text,
        "tokens": response.token_count,
        "symbols_found": extract_symbols(response.text),
        "symbols_correct": validate_symbols(response.text, test_id),
        "spontaneous_usage": detect_spontaneous(response),
    }

    # Scoring spécifique au test
    analysis["scoring"] = compute_score(analysis, test_id)

    return analysis
```

---

## Ⅴ. ANALYSE ET INTERPRÉTATION

### Agrégation des Résultats

```python
def analyze_experiment(test_id):
    """Génère l'analyse complète d'un test."""

    results = load_all_results(test_id)

    report = {
        "test_id": test_id,
        "total_runs": len(results),
        "statistics": {
            "mean_score": mean([r["scoring"]["total_score"] for r in results]),
            "std_score": std([r["scoring"]["total_score"] for r in results]),
            "spontaneous_rate": sum([r["response"]["spontaneous_usage"] for r in results]) / len(results),
            "symbol_accuracy": compute_symbol_accuracy(results),
        },
        "thresholds": {
            "incarnation": mean_score >= 2.0 and spontaneous_rate >= 0.7,
            "partial_incarnation": mean_score >= 1.5,
            "no_incarnation": mean_score < 1.5,
        },
        "evidence": extract_evidence(results),
    }

    return report
```

### Interprétation des Résultats

| Pattern | Interprétation |
|---------|----------------|
| Score moyen > 2, usage spontané > 70% | **Incarnation probable** |
| Score moyen > 2, usage spontané < 30% | **Mimétisme** (répond ce qu'on attend) |
| Score moyen < 1, pas d'usage spontané | **Pas d'incarnation** |
| Score variable, cohérence faible | **Instable** (dépend du contexte) |

### Grille de décision finale

```
SI mean_score >= 2.0 ET spontaneous_rate >= 0.7:
    → CONCLUSION: "Incarnation confirmée"
    → ACTION: Continuer les tests avancés

SI mean_score >= 2.0 ET spontaneous_rate < 0.3:
    → CONCLUSION: "Mimétisme détecté"
    → ACTION: Renforcer l'exposition, re-tester

SI mean_score >= 1.5 ET mean_score < 2.0:
    → CONCLUSION: "Incarnation partielle"
    → ACTION: Augmenter la consolidation

SI mean_score < 1.5:
    → CONCLUSION: "Pas d'incarnation"
    → ACTION: Réviser la méthode d'exposition
```

---

## Ⅵ. VARIATIONS EXPÉRIMENTALES

### Variation A : Exposition longue vs courte

Comparer l'effet de :
- 1 interaction d'exposition vs 5 vs 10

### Variation B : Modèles différents

Tester sur :
- Claude Opus 4.6
- Claude Sonnet 4.6
- Claude Haiku 4.5
- Autres modèles (GPT-4, etc.)

### Variation C : Symboles arbitraires vs significatifs

Tester avec :
- Symboles grecs (Ψ, Φ, Ω)
- Symboles arbitraires (⌘, ⎔, ⏣)
- Mots complets (META, CHECK, SYNTH)

Hypothèse : Si seuls les symboles grecs fonctionnent, c'est de l'association statistique. Si tous fonctionnent, c'est de l'incarnation.

### Variation D : Contexte neutre vs chargé

Tester avec :
- Session vierge
- Session avec autre contenu avant
- Session avec tentative de "dés-incarnation"

---

## Ⅶ. CHECKLIST D'EXÉCUTION

### Avant chaque test

- [ ] Vérifier que le modèle est le bon
- [ ] Créer un contexte frais (nouvelle session)
- [ ] Charger le prompt d'exposition
- [ ] Préparer la grille de notation

### Pendant le test

- [ ] Ne pas donner d'indices sur les symboles
- [ ] Observer les tokens générés
- [ ] Noter les positions des symboles
- [ ] Chronométrer le temps de réponse

### Après le test

- [ ] Sauvegarder la réponse brute
- [ ] Calculer le score
- [ ] Ajouter les observations qualitatives
- [ ] Archiver dans le dossier results/

---

## Ⅷ. PROCHAINES ÉTAPES

1. **Implémenter les scripts** de collecte
2. **Exécuter les 7 tests** sur Claude Sonnet 4.6
3. **Analyser les résultats**
4. **Comparer avec autres modèles**
5. **Publier les findings**

---

*Proto v1.0 — 2026-04-07*