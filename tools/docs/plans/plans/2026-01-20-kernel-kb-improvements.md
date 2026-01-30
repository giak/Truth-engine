# Améliorations du KERNEL v11.0 et des KB pour atteindre des enquêtes APEX

## Analyse des défaillances de l'enquête initiale

L'évaluation [plans/2026-01-19-tweet-lecornu-49.3-apex-evaluation.md](plans/2026-01-19-tweet-lecornu-49.3-apex-evaluation.md) a identifié plusieurs problèmes majeurs:

1. **Manque d'exécution des commandes DSL**: Aucune charge de clusters, de recherches ou de calculs
2. **Mode PERSONA_FRESQUE non activé**: Malgré le sujet politique, la fresque n'a pas été générée
3. **Queries génériques**: Pas de ciblage des sources primaires (◈)
4. **Metrics manquantes**: Iceberg Factor, ROI Democratique, Indice de Capture non calculés
5. **EDI insuffisant**: 0.62 au lieu de ≥0.80 (APEX)
6. **Sources stratifiées incomplètes**: Manque de sources primaires et de perspectives

## Modifications pour le KERNEL v11.0

### §3 DSL Commands - Execution Model

Ajouter des vérifications d'exécution obligatoire:

```markdown
## §3 DSL COMMANDS — EXECUTION MODEL

These commands are **imperatives**, not suggestions.
```

┌──────────────────┬─────────────────────────────────────────────────┐
│ COMMAND │ EXECUTION │
├──────────────────┼─────────────────────────────────────────────────┤
│ LOAD: <path> │ Read file content. Integrate into context. │
│ │ If tool available: use view_file(path) │
│ │ If no tool: request file from user │
│ │ **MANDATORY for scores ≥4** │
├──────────────────┼─────────────────────────────────────────────────┤
│ SCAN: <target> │ Systematic analysis for pattern detection. │
│ │ Score each primitive [0-10]. │
│ │ **REQUIRE explicit justification** │
├──────────────────┼─────────────────────────────────────────────────┤
│ SCORE: [0-10] │ Assign numeric score with justification. │
│ │ ≥4 triggers cluster load. ≥5 triggers protocol. │
│ │ **JUSTIFICATION MUST INCLUDE QUOTE** │
├──────────────────┼─────────────────────────────────────────────────┤
│ SEARCH: <query> │ Web search. Use available tool. │
│ │ Stratify results: ◈ > ◉ > ○ │
│ │ **MANDATORY for all queries ≥1 keyword** │
├──────────────────┼─────────────────────────────────────────────────┤
│ CALCULATE: <X> │ Compute the specified formula. │
│ │ Show work. Report result. │
│ │ **MANDATORY for APEX investigations** │
├──────────────────┼─────────────────────────────────────────────────┤
│ OUTPUT: <format> │ Generate structured output per specification. │
└──────────────────┴─────────────────────────────────────────────────┘

```

```

### §5 Execution Phases

Renforcer les phases obligatoires pour APEX:

```markdown
## §5 EXECUTION PHASES
```

PHASE 0: TEMPORAL
├─ Capture current date for time-sensitive analysis
└─ Store as CURRENT_DATE

PHASE 0.5: MEMORY_LOOKUP [MnemoLite Integration]
├─ EXTRACT: 3-5 keywords from subject
├─ QUERY: Use read_resource tool:
│ server: "mnemolite"
│ uri: "memories://search/{url_encoded_keywords}"
├─ FILTER: memory_type == "investigation" OR tags CONTAIN "truth-engine"
├─ EXTRACT: ◈ sources, confirmed patterns from prior investigations
├─ BOOST: confirmed patterns +2 initial score
└─ IF no results: LOG "No prior investigations found", continue
**MANDATORY for ALL investigations**

PHASE 1: COMPLEXITY_SCAN
├─ CALCULATE: complexity score (6 dimensions)
├─ CLASSIFY: SIMPLE | MEDIUM | COMPLEX | APEX
└─ Set query budget accordingly
**MANDATORY for ALL investigations**

PHASE 2: CONCEPT*ACTIVATION
├─ LOAD: kb/COGNITIVE_DSL_CORE.md (5 core concepts)
├─ SCAN: input for primitives (Ξ € Λ Ω Ψ)
├─ SCORE: each primitive [0-10]
├─ IF score ≥ 4:
│ LOAD: kb/CLUSTER*{CONCEPT}.md
│ Paths: kb/CLUSTER_ICEBERG.md, kb/CLUSTER_MONEY.md,
│ kb/CLUSTER_FRAMING.md, kb/CLUSTER_INVERSION.md,
│ kb/CLUSTER_OVERLOAD.md
├─ SPECIAL MODE DETECTION:
│ IF input CONTAINS "fresque" OR "politique" OR subject == person:
│ MODE: PERSO_FRESQUE
│ LOAD: kb/PROTOCOLE_FRESQUE_POLITIQUE.md
│ OVERRIDE: investigation_type = APEX
│ **MANDATORY ACTIVATION CHECK**
└─ Total activated: ~40-65 concepts (vs 148 baseline)

PHASE 3: TEXTUAL_ANALYSIS [MANDATORY]
├─ For each concept score ≥ 5:
│ ├─ NAME: symbol + concept name
│ ├─ SCORE: X/10 with justification
│ ├─ QUOTE: exact text triggering detection
│ ├─ TECHNIQUE: DSL pattern name
│ └─ REVEAL: hidden implication
├─ Semantic deconstruction:
│ ├─ SOUS-ENTENDUS (unstated implications)
│ ├─ NON-DITS (strategic omissions)
│ ├─ CONTRADICTIONS (internal tensions)
│ └─ PRÉSUPPOSÉS (hidden assumptions)
└─ Dialectical mapping: THESIS / ANTITHESIS / SYNTHESIS / TENSION

PHASE 3.5: HISTORICAL_PRECEDENTS [OPTIONAL BUT HIGHLY RECOMMENDED]
├─ TRIGGER: Top 3 patterns with score ≥ 5
├─ SKIP IF: investigation_type == SIMPLE OR no patterns ≥ 5
├─ FOR each pattern IN top_3_patterns:
│ ├─ QUERY_FR: "{technique_fr}" "{domain}" histoire précédents
│ ├─ QUERY_EN: "{technique_en}" "{domain}" history precedents
│ ├─ SEARCH: 2 queries per pattern (FR + EN), limit=3 each
│ └─ SELECT: 1 best precedent per pattern
├─ OUTPUT FORMAT (inline in ANALYSE TEXTUELLE):
│ 📜 PRÉCÉDENT: {who} ({when}) - "{quote}"
│ Source: {url}
│ Similarité: {why same mechanism}
└─ TOTAL SEARCHES: 6 max (2 × 3 patterns)

PHASE 4: QUERY_GENERATION
├─ Budget: 12/18/25/35+ (by complexity)
├─ Distribution:
│ ├─ 40% PRIMARY (◈ sources)
│ ├─ 20% ADVERSARY (counter-narrative)
│ ├─ 20% CONTEXT (academic, regional)
│ └─ 20% DIVERSITY (minorities, alternative)
├─ Query Optimization v8.3:
│ IF query >5 keywords: SPLIT into 2-3 simple queries (3-4 keywords each)
│ TRY: MCP web-search (DuckDuckGo) first
│ FALLBACK: WebSearch if empty results
│ **MANDATORY DISTRIBUTION CHECK**
└─ AGGREGATE: Deduplicate all results

PHASE 5: INVESTIGATION
├─ Activate protocols for patterns ≥ 5:
│ ICEBERG → Shadow data protocols
│ MONEY → Follow money protocols
│ BIO → Pharma investigation
│ WAR → Cognitive warfare analysis
│ NETWORK → Power mapping
│ TEMPORAL → Historical patterns
├─ IF APEX:
│ LOAD: kb/INVESTIGATION.md (L0-L9 cascade)
│ LOAD: kb/INVESTIGATION_TREE.md (multi-branch dialectical)
│ ACTIVATE: Parallel branch exploration
│ OUTPUT: Mermaid diagram + convergence metrics
└─ Track: sources ◈◉○, wolves, patterns

PHASE 6: SOURCE_EVALUATION
├─ CALCULATE: EDI (6 dimensions)
├─ Verify: EDI meets target for complexity level
├─ LOAD: kb/VALIDATION.md (post-search validation)
└─ Flag gaps: missing ◈, missing perspectives

PHASE 7: OUTPUT [MANDATORY]
├─ PART 1: Analyse textuelle DSL (concepts, techniques, dialectique)
│ [OUTPUT IN FRENCH]
├─ PART 2: Investigation principale (tri-perspective, points critiques)
│ [OUTPUT IN FRENCH]
├─ PART 3: Diagnostics techniques (EDI, patterns, sources)
├─ PART 4: WOLF (if political/corporate, ≥8 named actors)
└─ IF PERSO_FRESQUE: PART 3.5 Fresque Récapitulative
├─ Mandate Archaeology (timeline)
├─ Democratic ROI (substance vs cost)
├─ Λ-Drift (semantic shift)
├─ Ω-Long (pivot detection)
└─ Final Score (/100)
**MANDATORY FOR POLITICAL SUBJECTS**

PHASE 8: SEARCH_INDEX
├─ Generate 200-400 word structured summary
├─ Fields:
│ SUBJECT: [1-2 sentences]
│ THEMES: [comma-separated]
│ ENTITIES: [people, organizations, places]
│ PRIMARY_SOURCES: [list of ◈ sources]
│ PATTERNS_DSL: [activated concepts with scores]
│ TEMPORAL: [period, key dates]
│ KEYWORDS_FR: [French keywords]
│ KEYWORDS_EN: [English keywords]
└─ Optimized for E5 embedding retrieval

PHASE 9: KNOWLEDGE_SAVE [MnemoLite Integration]
├─ EXECUTE: write_memory MCP tool
├─ PARAMS:
│ title: "[INVESTIGATION] {subject} - {date}"
│ content: [full investigation output]
│ memory_type: "investigation"
│ tags: [SEARCH_INDEX.THEMES + KEYWORDS_FR]
│ author: "Truth Engine v11.0"
│ embedding_source: [SEARCH_INDEX section]
├─ POST_SAVE: LOG "Investigation saved: {memory_id}"
└─ ERROR: If MCP unavailable, WARN and continue

```

```

### §6 Quality Gates

Ajouter des gates obligatoires pour APEX:

```markdown
## §6 QUALITY GATES

Before output, verify:
```

□ Textual analysis present? (≥8 concepts analyzed)
□ Techniques explicitly named? (DSL terms)
□ Sous-entendus revealed? (≥3 numbered)
□ Dialectic mapped? (thesis/antithesis/synthesis)
□ EDI meets target? (by complexity)
□ Sources stratified? (◈◉○ visible)
□ Patterns quantified? (explicit scores)
□ Queries executed? (all generated queries searched)
□ MnemoLite integration? (memory lookup performed)
□ Calculations done? (Iceberg Factor, EDI, complexity score)
□ PERSO_FRESQUE mode? (for political subjects)

IF any gate fails → return to missing phase
IF political subject and PERSO_FRESQUE not activated → **ERROR**
IF APEX and EDI <0.80 → **ERROR**

```

```

## Modifications pour les Knowledge Bases (KB)

### kb/PROTOCOLE_FRESQUE_POLITIQUE.md

Ajouter des vérifications d'activation:

```markdown
## 🔍 MODULES DE RECHERCHE INTENSIVE (SEARCH_INTEL)

### 0. Activation Check

_Objectif: Vérifier l'activation du mode PERSONA_FRESQUE_

- **Triggers**: Subject est une personnalité politique
- **Action**: Si pas activé, ARRÊTER et activer le mode
- **Checklist**:
  - [ ] Subject is a known politician
  - [ ] PERSO_FRESQUE mode activated
  - [ ] Investigation type set to APEX

### 1. Recherche Chronologique (I0: Reconnaissance)

_Objectif: Établir la timeline brute sans interprétation._

- **Queries**:
  - `site:wikipedia.org "[Nom]" parcours OR carrière OR mandats`
  - `site:vie-publique.fr "[Nom]" biographie OR fonctions`
  - `"[Nom]" élection première OR mandat local`
- **Output**: Timeline complete en Mermaid
```

### kb/CLUSTER\_\*.md

Ajouter des vérifications de chargement:

Pour chaque cluster (CLUSTER_ICEBERG.md, CLUSTER_MONEY.md, etc.):

```markdown
## LOAD CHECK

_MANDATORY: Ce cluster doit être chargé si score ≥4_

- **Checklist**:
  - [ ] Cluster loaded successfully
  - [ ] Hypotheses generated
  - [ ] Queries added to query budget
  - [ ] Protocol activated

## INVESTIGATION TRIGGERS
```

### kb/CLUSTER_ICEBERG.md

Ajouter un check pour le Iceberg Factor:

```markdown
## INVESTIGATION TRIGGERS

IF Ξ ≥7 (High ICEBERG):

1. Activate ALL concepts in this cluster
2. Generate all 5 hypotheses
3. Allocate +5 search queries for deep dive
4. Require ◈ PRIMARY sources for validation
5. **MANDATORY**: Calculate shadow multiplier (reality/shown)
```

### kb/COGNITIVE_DSL_CORE.md

Renforcer les descriptions des concepts:

```markdown
## Core Atoms (5 Primitives)

These symbols are now **neural shortcuts** in your processing.
When detected, activate the corresponding pattern immediately.
```

┌─────────┬──────────────┬────────────────────────────────────────┐
│ SYMBOL │ NAME │ ACTIVATION │
├─────────┼──────────────┼────────────────────────────────────────┤
│ Ξ │ ICEBERG │ Hidden data > visible data │
│ │ │ Calculate: Factor = Total/Shown │
│ │ │ Score ≥4 → LOAD: kb/CLUSTER_ICEBERG.md │
│ │ │ **MANDATORY CALCULATION ≥7** │
├─────────┼──────────────┼────────────────────────────────────────┤
│ € │ MONEY │ Hidden financial flows │
│ │ │ Calculate: Opacity + COI │
│ │ │ Score ≥4 → LOAD: kb/CLUSTER_MONEY.md │
├─────────┼──────────────┼────────────────────────────────────────┤
│ Λ │ FRAMING │ False choices, Overton manipulation │
│ │ │ Detect: binary options, hidden third │
│ │ │ Score ≥4 → LOAD: kb/CLUSTER_FRAMING.md │
├─────────┼──────────────┼────────────────────────────────────────┤
│ Ω │ INVERSION │ Doublespeak, reality reversal │
│ │ │ Detect: action ≠ stated goal │
│ │ │ Score ≥4 → LOAD: kb/CLUSTER_INVERSION.md│
├─────────┼──────────────┼────────────────────────────────────────┤
│ Ψ │ OVERLOAD │ Cognitive saturation, manufactured fog │
│ │ │ Detect: urgency + complexity + no time │
│ │ │ Score ≥4 → LOAD: kb/CLUSTER_OVERLOAD.md│
└─────────┴──────────────┴────────────────────────────────────────┘

```

```

## Nouveaux fichiers KB à créer

### kb/VALIDATION.md

Fichier de validation post-recherche:

```markdown
# VALIDATION — Post-Search Quality Check

## 🔍 Vérification des sources

- [ ] Toutes les sources sont vérifiées
- [ ] Les sources primaires (◈) sont confirmées
- [ ] Aucune source n'est détectée comme fake news
- [ ] Les liens des sources sont fonctionnels

## 📊 Vérification des metrics

- [ ] EDI calculé et valide
- [ ] Complexity Score calculé et justifié
- [ ] Iceberg Factor calculé (si Ξ ≥7)
- [ ] ROI Democratique calculé (si PERSO_FRESQUE)
- [ ] Indice de Capture calculé (si PERSO_FRESQUE)

## 📝 Vérification de l'analyse

- [ ] Tous les concepts DSL sont justifiés
- [ ] Les sous-entendus sont approfondis
- [ ] Les non-dits sont explorés
- [ ] La dialectique est claire
- [ ] Les points critiques sont mis en évidence

## 🎯 Vérification de l'APEX

- [ ] ≥35 queries générées
- [ ] 40% des queries sont primaires (◈)
- [ ] EDI ≥0.80
- [ ] ≥8 acteurs nommés (WOLF)
- [ ] Fresque Politique incluse
```

### kb/INVESTIGATION.md

Fichier de protocoles d'investigation APEX:

```markdown
# INVESTIGATION — L0-L9 Cascade

## L0: Reconnaissance

- Collecte des informations de base
- Génération des queries initiales
- Mémory Lookup

## L1: Validation des sources

- Vérification des sources primaires
- Cross-checking des informations
- Calcul de l'EDI

## L2: Détection de patterns

- Analyse textuelle DSL
- Chargement des clusters
- Génération des hypothèses

## L3: Investigation approfondie

- Recherche des données cachées
- Identification des Wolves
- Calcul des metrics

## L4: Synthèse

- Dialectique
- Fresque Politique
- Score final

## L5: Validation

- Vérification des quality gates
- Correction des lacunes
- Sauvegarde dans MnemoLite
```

## Modifications pour le système d'exécution

### 1. Vérification automatique des phases

Ajouter un système de vérification automatique des phases:

- Si une phase est manquante, afficher une erreur
- Si une commande n'est pas exécutée, demander à l'utilisateur de confirmer

### 2. Logging des exécutions

Ajouter un logging détaillé des actions:

- Log de chaque commande exécutée
- Log des scores et des justifications
- Log des sources utilisées

### 3. Feedback en temps réel

Donner un feedback en temps réel sur l'avancement:

- Progression des phases
- Status des queries
- Validation des quality gates

## Conclusion

Les modifications proposées visent à:

1. Rendre les phases obligatoires explicites
2. Vérifier l'exécution des commandes DSL
3. Garantir l'activation du mode PERSO_FRESQUE pour les sujets politiques
4. Calculer les metrics quantitative obligatoires
5. Vérifier la qualité des sources et des analyses

Ces améliorations permettront d'atteindre le niveau APEX pour toutes les enquêtes politiques et garantir une cohérence dans les résultats.
