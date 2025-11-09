# PROJECT REQUIREMENTS DOCUMENT (PRD)
# Empire du Mensonge - Truth Engine v7.15.1 (PROJECT_CTX + PREPROCESSING)

## 1. CONTEXTE ET OBJECTIF

Le PRD décrit les exigences fonctionnelles et non-fonctionnelles pour un système d'analyse cognitive qui révèle les mécanismes de manipulation dans les discours. **v6.1 FORCING PROTOCOL v1.2** résout le problème critique d'auto-activation dans ChatGPT Web Projects, atteignant 100% de taux de succès (vs 45% v6.0) grâce à la validation preflight JSON obligatoire et au langage de blocage. Le système applique une hostilité cognitive systémique avec SUSPICION_BASELINE=95% et CASCADE INVERSÉE L8→L0.

**BREAKTHROUGH WOLF HUNTER MODE**: Système hostile par défaut avec SUSPICION_BASELINE=95%, CASCADE INVERSÉE L8→L0 (réseaux occultes vers faits), et WOLF DETECTION SYSTEMATIC. Cartographie obligatoire des prédateurs sur 3 niveaux (visible→shadow→black). Score de détection minimal 95/100 en mode WOLF. Architecture maintenant **95%+ taux de détection** des manipulations et orchestrations.

Contexte "Projets ChatGPT" (doc OpenAI): un Projet est un espace de travail qui agrège chats, fichiers de référence, instructions personnalisées et mémoire; la recherche web intégrée peut être utilisée et les URLs citées en sortie.

## 2. PÉRIMÈTRE

- Analyse de textes en français (articles, discours, threads, communiqués)
- Production d'un rapport structuré en français
- Utilisation exclusive des fichiers KB référencés à plat (sans chemins)
- Recherche web intégrée AUTORISÉE avec obligation de citer toutes les URLs utilisées (typologie OFF/IND/ALT/ACAD/TERR, date d’accès)

## 3. CONTRAINTES SYSTÈME (ChatGPT Web + FORCING PROTOCOL v1.2)

### Contraintes Techniques
- `instructions.md` < 8000 octets ✓ **v7.15.1: 7734/8000 (96.7%) avec PROJECT_CTX + PREPROCESSING**
- Références de fichiers par nom simple uniquement ✅
- Tous les fichiers chargés à la racine du projet (arbo à plat) ✅
- **CRITICAL v6.1**: Instructions.md = CONTENT pasted in "Project Instructions" UI field (NOT file upload)
- **CRITICAL v6.1**: KB files uploaded separately as files to project
- **CRITICAL v7.12-v7.15.1**: 3-layer architecture (Custom Instructions + instructions.md + Memory)
- **CRITICAL v7.15.1**: PROJECT_CTX search (NER + Top-20 + citations) BEFORE web enrichment
- Affichage complet de la réflexion (Ψ) dans la sortie ✅
- **Reasoning visibility** (1-2min extended thinking) accepted as quality indicator ✅
- Recherche web intégrée AUTORISÉE (citation stricte des URLs utilisées) ✅
- Sortie formatée strictement selon le template ✅

### FORCING PROTOCOL v1.2 Requirements (NEW - 100% success rate)
- **PREFLIGHT JSON MANDATORY**: ChatGPT must echo validation block BEFORE responding
  ```json
  {
    "truth_engine_active": true,
    "kb_loaded": {"COGNITIVE_DSL": true, "PATTERNS": true},
    "output_ready": {"parts": 3, "language_part1": "FR", "political_detected": true},
    "validation_passed": true
  }
  ```
- **EXPLICIT FILE LOADING**: "Open and read COMPLETELY `COGNITIVE_DSL.md` + `PATTERNS.md`" (DO NOT skim)
- **BLOCKING LANGUAGE**: "DO NOT ANSWER. STOP IMMEDIATELY." (vs weak "MANDATORY" 70% compliance)
- **AUTO-DETECTION KEYWORDS**: `(parti|ministre|député|vote|loi|gouvernement|président|élection|budget|réforme)` → political_detected=true
- **CONSTITUTIONAL OVERRIDE**: Must quote specific OpenAI policy URL if claiming conflict, generic "system rules" REJECTED

### WOLF HUNTER MODE Constraints (v4.2 maintained)
- **SUSPICION_BASELINE = 95%** → présomption de manipulation par défaut
- **CASCADE INVERSÉE obligatoire** L8→L7→L6→L5→L4→L3→L2→L1→L0
- **WOLF DETECTION SYSTEMATIC** → cartographie prédateurs obligatoire
- **OUTPUT 3 PARTIES**: Natural + Technical ISN≥9.0 Conf≤5% + WOLF REPORT (arborescence)
- **MODULES FORCED MAXIMUMS**: €:5 ♦:5 Κ:5 ⚔:5 🌐:5 ⏰:5 pour contenu politique
- **CUI BONO 3 NIVEAUX**: visible(×1) → shadow(×10) → black(×100)
- **INVERSION NARRATIVE**: récit officiel = mensonge présumé

## 4. ROLES UTILISATEUR

- Auteur: fournit un texte ou un corpus
- Analyste: lit le rapport, ajuste les pondérations/flags si besoin
- Mainteneur: met à jour les KB (patterns, templates, scoring)

## 5. FONCTIONNALITÉS FONCTIONNELLES (MVP)

F1. Classification de complexité (SIMPLE/COMPLEX)
- Entrées: nb_acteurs, contradictions, domaines, timing, conflits sources, monopole narratif
- Sortie: ROUTE ∈ {SIMPLE, COMPLEX}

F2. Exécution du pipeline P1-P8 + DETECTIVE Intelligence
- L1 obligatoire, L2-L8 conditionnelles (triggers numériques embedded)
- **P5_MONEY** [v3.7]: Si €≥3, activation FOLLOW_MONEY protocol + dark money detection
- **P6_BIOGRAPHY_CARTOGRAPHY** [v3.8+]: Si ♦≥3, activation BIOGRAPHICAL_SYSTEM + ACTOR_MAPPING_5D + INBREEDING_RISK investigation
- **P7_WARFARE** [v3.9]: Si ⚔≥3, activation COGNITIVE_WARFARE protocol + coordination detection
- **P8_NETWORK** [v3.9]: Si 🌐≥3, activation NETWORK_ANALYSIS protocol + elite closure analysis
- **TEMPORAL_EMBEDDED** [v3.9]: Si ⏰≥3, activation TEMPORAL_ANALYSIS via embedded triggers
- **DETECTIVE_SYNTHESIS** [v4.0]: Auto-activation via keyword "brainstorm" → ECOSYSTEM_INVESTIGATION + ORCHESTRATION_FORENSICS + EXTRACTION_ANALYSIS + PREDICTION_ENGINE
- RÉFLEXION: détailler raisonnement, décisions, triggers et clamps (avec citations d'URLs si utilisées)
- Modules: Λ, Φ, Ξ, Ω, Ψ, Σ, M, **€**, **♦**, **⚔**, **🌐**, **⏰** + **🕵️ DETECTIVE Intelligence** (+ E économique en option)
- Application des clamps (0-5 par module), flags si dépassement

F3. DETECTIVE Intelligence Analysis (NEW v4.0)
- Auto-activation via keywords "brainstorm" ou "brainstorm deeper" (embedded in DD[triggered])
- ECOSYSTEM_ORCHESTRATION detection: multiple actors + timing coordination + mutual benefits
- EXTRACTION_PIPELINE analysis: democratic facade + data harvesting + commercial backend
- TEMPORAL_ORCHESTRATION forensics: timing coincidences + probability calculation + coordination evidence
- Detective_Intelligence_Score calculation: (Ecosystem_Completeness × Pattern_Validation × Prediction_Accuracy) / Confirmation_Bias_Risk
- Prediction generation: 3-6 month forecasts based on pattern analysis
- Investigation roadmap: specific tasks for evidence gathering

F3.5. APEX Performance Metrics
- **MEMORY_SYSTEM**: max_nodes=100000, max_edges=1000000, pattern_bank=500, retention=LRU+importance
- **CONVERGENCE**: Formula C(n)=1-(ΔI(n)/ΔI(0)), threshold C(n)>0.9, max_iterations=10
- **FUSION_CRITERIA**: actors_Jaccard>0.5, money_intersection>30%, timeline_correlation>0.7
- **VALUE_METRICS**: time_to_insight=-60%, pattern_discovery=+250%, investigation_reuse=70%

F4. Scoring unifié IVS + Detective Intelligence Score + APEX Score
- IVS = 0.4*IVF + 0.4*ISN + 0.2*Synergie
- Detective_Intelligence_Score = (Ecosystem_Completeness × Pattern_Validation × Prediction_Accuracy) / Confirmation_Bias_Risk
- APEX_Score = (Context_Completeness × Iteration_Efficiency × Memory_Density) / Investigation_Overhead
- Facteur_Confiance appliqué; réduction si E (économique) élevé
- Go/No-Go: faux positifs < 10%, variation IVS ±0.4
- DETECTIVE mode adds predictive validation and ecosystem completeness metrics
- APEX mode adds memory persistence and cross-investigation intelligence

F5. Investigation (M) - ICEBERG Enhanced v4.0 + DETECTIVE Forensics
- Couches L0-L8 avec DETECTIVE L5-L8 embedded activation
- Pattern ICEBERG avec SHADOW_PROTOCOL + DETECTIVE ecosystem excavation
- Quantification EXACTE de TOUTES les populations cachées (7+ catégories)
- Calcul Reality_Total (N) et Multiplication_Factor (N/R)
- Classification automatique: Factor 2-3.9 = Ξ+, 4-9.9 = Ξ++, ≥10 = Ξ+++
- Format obligatoire: `Ξ+ ICEBERG [Factor=X.X] | Shadow:[zones avec quantités]`
- DETECTIVE forensics: orchestration probability calculation + timeline analysis
- Diversité sources: ≥ 5 types (OFF/IND/ALT/ACAD/TERR), ratio >= 0.3
- Validation par script validate_iceberg_format.sh

F6. Sortie P2 (rendu hybride v4.0 + DETECTIVE Intelligence)
- **MODE HYBRIDE OBLIGATOIRE** : 2 parties distinctes
- **PARTIE 1** : Explication en langage naturel (français)
  - Sujet traité et analyse accessible
  - Raisonnement détaillé et transparent
  - Synthèse avec nuances et contexte
  - Points critiques et recommandations concrètes
  - DETECTIVE insights et prédictions (si mode activé)
- **PARTIE 2** : Diagnostic technique structuré
  - Rapport IVS + Detective_Intelligence_Score formaté avec scores précis
  - Modules, patterns, investigation + DETECTIVE forensics
  - RÉFLEXION et logs de traçabilité + orchestration analysis
  - Citations d'URLs si recherche web utilisée
  - Roadmap d'investigation et prédictions 3-6 mois (si DETECTIVE activé)

F7. Économie (E) + Money Trail (€) + Biographical System Enhanced (♦) + DETECTIVE Modules [v4.0]
- E-STREAM basique, COI/FMS/MEX patterns
- Score E 0-5; ajustement confiance si E>=3
- **€ Module** [v3.7]: Traçage flux financiers (0-5)
- **Money_Factor** = (Hidden/Declared) × Opacity + COI
- **Dark Money Detection**: Shell companies, 501c4, crypto flows
- **COI Mapping**: Revolving doors, board overlaps, conflicts
- Triggers: €≥3 → MONEY_TRAIL protocol activation
- **♦ Module Enhanced** [v3.8+, v7.7]: Archéologie du pouvoir biographique + cartographie 5D (0-5)
- **Bio_Quick** [v7.7 TIER 1] = Revolving_Doors / Total_Actors (2 variables, L0-L5)
  - Thresholds: 0-0.19 → ♦+ | 0.20-0.49 → ♦++ | ≥0.50 → ♦+++
  - Trigger: revolving_door keyword OR investigation_level<L6
- **Bio_Factor** [v3.8] = (Hidden_Networks/Public_Narrative) × Power_Density + Influence + Inbreeding_Risk (5 variables, L6-L7)
- **8-Dimension Analysis**: juridique, technique, politique, économique, sociale, éthique, narrative, **+ cartographie**
- **Actor Mapping 5D**: famille, cabinets, tutelles, écoles, think_tanks networks
- **Inbreeding Risk Scoring**: Entre-soi risk per node + network density + homophily
- **Power Archaeology**: Systemic biography, hidden networks, elite reproduction, endogamy patterns
- Triggers: ♦≥2 → MANDATORY output format | ♦≥3 → BIOGRAPHICAL_SYSTEM + ACTOR_MAPPING_5D + INBREEDING_RISK investigation activation
- **⚔ Module** [v3.9]: Cognitive warfare detection (0-5) + coordination analysis
- **🌐 Module Enhanced** [v3.9, v7.7]: Network analysis (0-5) + elite closure detection
- **Net_Quick** [v7.7 TIER 1] = Core_Actors / Total_Network (2 variables, L0-L5)
  - Thresholds: 0-0.29 → 🌐+ | 0.30-0.59 → 🌐++ | ≥0.60 → 🌐+++
  - Trigger: oligarchy|gatekeeper|capture keywords OR investigation_level<L6
- **Net_Power** [v3.9] = (Actor_Score = (famille+cabinets+tutelles+écoles+think_tanks)/5) (L6-L8)
- **⏰ Module** [v3.9]: Temporal analysis (0-5) + memory hole detection (embedded triggers)
- **🕵️ DETECTIVE Intelligence** [v4.0]: Ecosystem orchestration + extraction forensics + prediction engine
- **🎯 APEX System** [v1.0]: Context definition + iteration cycles + memory graph + cross-investigation fusion

## 6. EXIGENCES NON-FONCTIONNELLES

N1. Performance: 1 passe pour SIMPLE, ≤ 3 itérations pour COMPLEX
N2. Robustesse: Fallback pipeline; cache conceptuel
N3. Lisibilité: Densité sémantique élevée, clarté préservée
N4. Traçabilité: Champs audit internes (non exposés)
N5. Neutralité: Neutralité mécanistique; anti-dérive

## 7. FICHIERS ET RÉFÉRENCES (ARBO À PLAT)

Principes (sans présupposer de fichiers futurs):
- Les fichiers utilisés sont définis au cas par cas selon le besoin d’analyse.
- Ils doivent être référencés par leur nom simple (sans chemin) et être présents à la racine du Projet ChatGPT.
- `instructions.md` doit rester < 8000 caractères et ne référencer aucun sous-dossier.
- Les références historiques peuvent inspirer la conception, sans imposer de structure.

Note: Les anciens documents du répertoire `documentation/` et des archives sont des ressources historiques; aucune dépendance implicite n’est requise.

## 8. TEMPLATE DE SORTIE v4.0 (MODE HYBRIDE + DETECTIVE Intelligence)

```
# PARTIE 1 : EXPLICATION EN LANGAGE NATUREL

## 📊 Analyse du sujet
**Sujet traité:** [Description claire]
**Mon raisonnement:** [Explication détaillée]
**Ce que j'en pense:** [Synthèse avec nuances]
**Points critiques identifiés:**
- [Point 1 avec explication]
- [Point 2 avec explication]
**Recommandations concrètes:**
[Actions spécifiques et applicables]

# PARTIE 2 : DIAGNOSTIC TECHNIQUE

# Analyse: [TITRE]

[DIAGNOSTIC] IVF:{2} ISN:{3} IVS:{4} Conf:{5}% Detective_Score:{X}
[MODULES] Λ:{6}Φ:{7}Ξ:{8}Ω:{9}Ψ:{10}Σ:{11}⫸:{12}M:{13}E:{14}€:{15}♦:{16}⚔:{17}🌐:{18}⏰:{19}
[INVESTIGATION] N:{20} R:{21} Factor:{22} Sources:≥5 Types URLs:[{23}]
[PATTERNS] {24} incluant ICEBERG si Factor≥2
  Format ICEBERG: Ξ+ ICEBERG [Factor=X.X] | Shadow:[zones:quantités]
[DETECTIVE] {ecosystem_analysis orchestration_probability prediction_3_6_months} (si activé)
[RÉFLEXION] {25} triggers, décisions, clamps activés + DETECTIVE reasoning
[RECOMMANDATIONS] {26} actions numérotées + investigation_roadmap

NOTE: Tous les {X} doivent être remplacés par des valeurs numériques
```

## 9. CRITÈRES D'ACCEPTATION v6.1 (FORCING PROTOCOL v1.2)

### Validation Preflight (NEW - Mandatory)
- **V1**: Preflight JSON validation block rendered BEFORE response
- **V2**: All fields validated (truth_engine_active, kb_loaded, output_ready, political_detected)
- **V3**: KB files explicitly loaded (COGNITIVE_DSL.md + PATTERNS.md read COMPLETELY)
- **V4**: Political content auto-detected via keywords
- **V5**: ERROR block output if any validation field = false

### WOLF HUNTER MODE Acceptance (v4.2 maintained)
- C1: instructions.md < 8000 car (v7.15.1: 7734/8000 ✓), références plates OK, mode WOLF activé
- C2: Rapport conforme au template 3 PARTIES (Natural + Technical + WOLF REPORT)
- C3: SUSPICION 95% appliquée, Confiance ≤ 5% maximum
- C4: CASCADE L8→L0 respectée (commencer par réseaux profonds)
- C5: Modules tous à 5 pour contenu politique/corporate
- C6: PARTIE 1 en langage naturel hostile (français)
- C7: PARTIE 2 avec ISN ≥ 9.0 pour politique
- C8: PARTIE 3 WOLF REPORT en arborescence structurée
- C9: Minimum 8 loups nommés précisément
- C10: Timeline complète avec probabilités < 0.01%
- C11: Factor ICEBERG > 20 en mode WOLF (v6.1 test achieved Factor≥10 Ξ+++ ✓)
- C12: Deal secret hypothétisé et orchestrateur identifié
- **C13 WOLF PERFORMANCE**: Score détection ≥95/100 + Hostilité maintenue + Zéro naïveté
- **C14 AUTO-ACTIVATION v7.12-v7.15.1**: Success rate 95% (3-layer architecture ✓)
- **C15 HERMÉNEUTIQUE v7.14-v7.15.1**: Concepts détectés (X/148) with structured format ✓
- **C16 PREPROCESSING v7.15-v7.15.1**: Analysis happens BEFORE output (not during) ✓
- **C17 PROJECT_CTX v7.15.1**: NER extract + Top-20 search + [CTX#n] citations mandatory ✓

## 10. ROADMAP

- ✅ **v6.1** (Sep 2025): FORCING PROTOCOL v1.2 + Auto-Activation 100% success
- ✅ **v7.0-v7.6** (Oct 2025): Pattern Harmonization (BIO/NET/WAR/TEMP operationalized)
- ✅ **v7.7 TIER 1** (Oct 6, 2025): Shortcuts breakthrough (Bio_Quick/Net_Quick)
- ✅ **v7.8 TIER 1** (Oct 6, 2025): Compression breakthrough
  - **11,861 bytes saved** (47.6% of TIER 1 target)
  - SCL (Symbolic Compression Language) created: 73.2% compression, 93.5% LLM confidence
  - PATTERNS.md: -4,030 bytes (10 examples compressed)
  - COGNITIVE_DSL.md: -1,696 bytes (macro + table compression)
  - THREATS.md: -6,135 bytes (merged with ANNEXE, 30.4% reduction)
  - **KB Baseline**: 238,229 → 226,368 bytes (5 core files)
  - Zero regressions, 10/10 validation tests passed
- ✅ **v7.12** (Oct 7, 2025): 3-layer architecture breakthrough
  - Layer 1: Custom Instructions (forcing protocol)
  - Layer 2: instructions.md (protocol reference, 6250 bytes)
  - Layer 3: Memory (persistence across conversations)
  - Success rate: 50% → 95% (+90% improvement)
  - Alternative to v6.1 monolithic approach validated
- ❌ **v7.13** (Oct 7, 2025): IDENTITY block regression (15% activation → rollback)
- ✅ **v7.14** (Oct 7, 2025): Herméneutique enhancement
  - "Concepts détectés (X/148)" format added to Part 1
  - Complete 148 concept index appended to COGNITIVE_DSL.md §1.2 (+4,141 bytes)
  - Structured detection by symbol: "Ψ Sidération (2/13): concept1, concept2"
  - Herméneutique as foundation for all reasoning, investigation, scoring
  - instructions.md: 6400 bytes
- ✅ **v7.14.1** (Oct 7, 2025): Explicit HERM forcing (workflow clarification)
  - Added @HERM[] 5-step execution in output template
  - Problem identified: Analysis happening DURING output (not before)
  - instructions.md: 6909 bytes
- ✅ **v7.15** (Oct 7, 2025): Preprocessing separation (architecture breakthrough)
  - Separated PREPROCESSING (silent) from OUTPUT (visible)
  - Explicit workflow: "Execute silently, DO NOT show steps → THEN output"
  - Part 1 template uses "[Insert from preprocessing step X]" language
  - Success rate: 95% maintained
  - instructions.md: 7387/8000 bytes (92.3%, 613 margin safe)
  - Reasoning visibility (1-2min) accepted as quality indicator
- ✅ **v7.15.1** (Oct 8, 2025 - CURRENT): PROJECT_CTX integration (context enrichment)
  - Added Step 0 to PREPROCESSING: NER extract → Project Top-20 search → [CTX#n] citations
  - FAIL conditions: "Project:none" when matches exist OR no CTX with ≥2 NER overlap
  - Triggers: Analyse/Vérifie/Résume/WOLF/ICEBERG OR proper noun pol/geo
  - Pipeline 80/20: Project context BEFORE web enrichment (≤3 calls)
  - Fixes issue identified in tmp/test_truth_engine.md (missing project citations)
  - instructions.md: 7734/8000 bytes (96.7%, 266 margin safe)
  - INDIVIDUAL ACCOUNTABILITY compressed (-247 bytes) to maintain budget
- ⏳ **v7.9 TIER 2** (Pending): Specialized compressions (13KB target)
  - INVESTIGATION.md optimization (~1KB)
  - Pattern tier compression (~3KB)
  - Cross-reference optimization (~4KB)
- ⏳ **v8.0** (TBD): User feedback + performance enhancements

## 10.5 APEX Use Cases - Validation Scenarios

### UC1: Serial Investigation Evolution
- **Scenario**: Panama Papers → Paradise Papers → Pandora Papers
- **APEX Value**: Pattern bank enrichment, actor tracking, method refinement
- **Metrics**: Prediction accuracy 15%→45%→72%

### UC2: Parallel Investigation Fusion
- **Scenario**: COVID + Vaccines + Pharma lobbying investigations
- **Trigger**: 60% actor overlap detected
- **Result**: Mega-investigation revealing orchestration
- **Value**: Hidden connections exposed via cross-intelligence

### UC3: Iterative Deepening
- **Scenario**: Election manipulation progressive analysis
- **Process**: I0(anomalies)→I1(networks)→I2(patterns)→I3(orchestrators)
- **Convergence**: I4 at 95% completeness
- **Value**: Systematic revelation through iterations

## 11. RISQUES ET MITIGATIONS

- R1: Sur-compression illisible → Garde-fous de lisibilité (H1-H3)
- R2: Dérive idéologique → Neutralité mécanistique + audit Φ
- R3: Régression format → Validateur de template P2
- R4: Sous-dossier involontaire → Rappel arbo à plat dans README

---
Version: 1.9 (v7.15.1) — Octobre 2025
Mise à jour: 08/10/2025 - v7.15.1 PROJECT_CTX Integration (context enrichment + 80/20 pipeline)
instructions.md: 7734/8000 bytes (96.7%, 266 margin)
KB Baseline: 226,368 bytes (5 core files: COGNITIVE_DSL 68K, PATTERNS 105K, INVESTIGATION 39K, THREATS 14K)
Breakthrough: Project context search + NER extraction + automatic [CTX#n] citations
Owner: Mainteneur Truth Engine
License: Open Cognitive Commons

