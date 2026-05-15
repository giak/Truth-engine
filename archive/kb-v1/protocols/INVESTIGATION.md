# INVESTIGATION — SYSTEMIC PATTERN GRAPH (SPG) Cascade (v2.1)

> **NOTE:** Ce fichier décrit le protocole L0-L6 séquentiel (SPG cascade).
> Pour les branches parallèles multi-agents, voir INVESTIGATION_TREE.md.
> KERNEL.md §5 référence les deux fichiers.

## SPG Architecture Overview

The SYSTEMIC PATTERN GRAPH is a fusion of three architectural approaches:

1. **Systemic Recursion**: Parallel multi-branch investigation with recursion control
2. **Pattern-Driven Query Synthesis**: Dynamic query generation based on active patterns
3. **Knowledge Graph Cascade**: Structured knowledge representation and relationship detection

**Core SPG Parameters**:

- Recursion limit: 2 levels (branch → sub-branch)
- Dynamic budget pool: Shared across all instances
- Termination rules: 3 consecutive irrelevant queries OR 45 mins OR 200 queries
- Priority scheduling: High-score branches get preferential allocation
- Query variants: 3-5 per pattern
- Serendipity budget: 10% for unexpected connections
- Knowledge graph: 5 relationship types, 3 cascade levels, interactive visualization

## L0: Reconnaissance

- Collecte des informations de base
- Génération des queries initiales
- Mémory Lookup

## L1: Validation & Branch Detection

- Cross-checking des informations
- Calcul de l'EDI
- Detect investigation tree triggers
- IF APEX: Launch INVESTIGATION_TREE (SPG enhanced)

## L2: SYSTEMIC PATTERN GRAPH Exploration

- Execute top 5 branches in parallel (SPG instances)
- Each branch = independent Truth Engine with SPG capabilities
- Isolation: No shared results to avoid confirmation bias
- Recursion management: Max 2 levels per branch

## L3: Pattern Detection & Hierarchical Activation (HPA)

- Analyse textuelle DSL
- Hierarchical pattern activation: Levels 1-2
- Chargement des clusters (CLUSTER\_\*.md)
- Génération des hypothèses
- Dynamic pattern detection based on results

## L3.5: Branch Convergence Check & Query Synthesis

- Evaluate branch status (CONVERGED/EXHAUSTED)
- If ≥3 branches exhausted: Relaunch with alternative strategies
- If critical gap unresolved: Launch targeted I2 investigation
- Query synthesis: Generate 3-5 variants per active pattern

## L4: Investigation Approfondie & Knowledge Graph Build

- Recherche des données cachées
- Identification des Wolves
- Calcul des metrics
- Knowledge graph construction: Core entities and relationships
- Shadow data detection (ICEBERG MAX)

## L5: Syntèse & Concordance Detection

- Merge branch results
- Detect concordances/contradictions
- Calculate final EDI
- Dialectique
- Fresque Politique
- Score final
- Interactive knowledge graph visualization

## L6: Validation & SPG Optimization

- Vérification des quality gates
- Correction des lacunes
- If EDI < 0.80: Launch I2 targeted investigation with SPG focus
- Sauvegarde dans MnemoLite
