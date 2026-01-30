# Truth Engine - Guide Utilisateur Pragmatique

**Version:** v8.0
**Date:** 2025-11-12

---

## 🚀 Démarrage Rapide

### Investigation Standard (AVEC web searches - MANDATORY)

```bash
"Analyse: [sujet]. Protocole Truth Engine complet."
```

**Exemple:**
```bash
"Analyse: 'Réforme retraites 64 ans France'. Protocole Truth Engine complet."
```

⚠️ **IMPORTANT v8.1:** Web searches via MCP sont **OBLIGATOIRES** pour toute investigation Truth Engine.

**Ce qui se passe automatiquement:**
1. **Complexity assessment** (SIMPLE/MEDIUM/COMPLEX/APEX)
2. **Web searches MCP** (≥5 à ≥15 queries selon complexity) — **MANDATORY**
3. **Pattern detection** (ICEBERG, MONEY, FRAMING, TEMPORAL, etc.)
4. **Output 3 parties** (analyse française + diagnostics techniques + WOLF si politique)

**Minimums web searches obligatoires:**
- SIMPLE: ≥5 queries
- MEDIUM: ≥8 queries
- COMPLEX: ≥12 queries
- APEX: ≥15 queries

**Si MCP web-search indisponible:**
- COMPLEX/APEX: Investigation **refusée** (erreur)
- SIMPLE/MEDIUM: Mode dégradé avec confirmation utilisateur (EDI ≤0.30, investigation flaggée INSUFFICIENT)

---

## 📁 Structure des Outputs

### Part 1 — Analyse Française (pour humains)

```markdown
## Sources utilisées
[Web1—URL], [Web2—URL], ... (ou "KB only" si pas de web)

## ⚠️ ATTENTION
Gaps de validation si EDI < target ou sources insuffisantes

## Sujet
Description + analyse herméneutique

## Tri-perspectif (95% hostilité symétrique)
- ACADÉMIQUE ⟐🎓: Position mainstream/institutionnelle
- DISSIDENT 🔥⟐̅: Voix censurées/supprimées
- ARBITRAGE: Ce que les ◈ sources primaires disent

## Points critiques (≥4)
Éléments clés détectés

## Recommandations
Actions suggérées

## Gaps & Impact Crédibilité
Ce qui manque + impact sur la fiabilité
```

### Part 2 — Diagnostics Techniques (pour analyse)

```yaml
[DIAGNOSTICS]
IVF:X.X ISN:Y.Y IVS:Z.Z Conf:WW% LEVEL sur PATTERN (data uncertainty: UU%)
  Complexity: N/10 (SIMPLE|MEDIUM|COMPLEX|APEX)
  Sources: total N (◈:X ◉:Y ○:Z)
  EDI: 0.XXX (target 0.XX, gap: ±0.XX)

[MODULES] Λ:X Φ:Y Ξ:Z Ω:A Ψ:B Σ:C Κ:D ρ:E κ:F €:G ♦:H ⚔:I 🌐:J ⏰:K

[SOURCES]
◈ PRIMARY (investigative journalism): N sources
◉ SECONDARY (mainstream verified): N sources
○ TERTIARY (institutional/state): N sources

EDI Breakdown:
  geo_diversity: 0.XX (target 0.XX)
  lang_diversity: 0.XX
  strat_diversity: 0.XX (◈◉○ distribution)
  ownership_diversity: 0.XX
  perspective_diversity: 0.XX
  temporal_diversity: 0.XX

[PATTERNS]
PATTERN_NAME (confidence XX% LEVEL):
  Signal: Description
  Factor: X.X [min-max] validated
    Best: X.X (Source: ◈/◉ highest reliability)
    Validated bounds: [min-max] (N methodologies ≥0.70)
    Full alternatives: [min-max] (all N methodologies)
    Data uncertainty: XX% (divergence ×Y)

[WOLVES] (if political/geopolitical/corporate)
Threshold: N (dynamic: base X - controversy Y - complexity Z)
Found: N actors (FULL WOLF | Partial XX% | Below threshold)

Individual actors: [list with roles]
Enablers: [media, think tanks, academic, tech, consulting]

[REFLECTION] (ALWAYS PRESENT v8.0)
INVESTIGATION_STATUS:
  Iteration: I0|I1|I2
  Complexity: LEVEL (score/10)
  Depth: L0-L9 layers covered
  Convergence: score (SUFFICIENT|ACCEPTABLE|CONTINUE|FORCED_STOP)

GAP_ANALYSIS:
  EDI_gap: target - current = gap (XX% below)
  Sources_gap: ◈ target:X current:Y gap:Z
  Wolves_gap: threshold:X found:Y gap:Z
  Pattern_gaps: [list unconfirmed patterns]
  Depth_gap: L6 counter-narrative reached|NOT reached

ITERATION_RECOMMENDATION:
  STATUS: COMPLETE ✅ | RECOMMENDED 🔄 | ACCEPTABLE ⚠️ | INSUFFICIENT ❌
  PRIORITY_GAPS: [EDI, ◈, WOLF, patterns, depth]
  ESTIMATED_QUERIES: N auto-generated

AUTONOMOUS_I1_PREVIEW: (if iteration recommended)
  Auto-queries would target:
    1. [EDI geo X queries] - descriptions
    2. [◈ PRIMARY X queries] - descriptions
    3. [L6 counter-narrative X queries] - descriptions
    ...
  Execute: "I1 AUTO logs/YYYY-MM-DD_subject.md"
```

### Part 3 — WOLF Report (si applicable)

Seulement si:
- Content type: political/geopolitical/corporate
- Actors found ≥ threshold (dynamique)

```yaml
## Part 3 — WOLF (Qui profite vraiment?)

**Actors Identified**: N/threshold

**Individual Level (×1)**:
[List named individuals with roles]

**Shadow Level (×10)**:
[Institutional actors, NGOs, foundations]

**Black Level (×100)**:
[Systemic beneficiaries, capital flows]

**Enablers** (≥30% ratio):
- Media: [propagation narrative]
- Think tanks: [legitimation intellectuelle]
- Academic: [caution scientifique]
- Tech: [algorithmic amplification]
- Consulting: [implementation]
```

---

## 🎯 Métriques Clés à Surveiller

### EDI (Epistemic Diversity Index)

**Cible selon complexity:**
- SIMPLE ≥0.30
- MEDIUM ≥0.50
- COMPLEX ≥0.70
- APEX ≥0.80

**Si en dessous:** Investigation insuffisamment diversifiée → itération I1 recommandée

### Sources ◈◉○

**Hiérarchie qualité:**
1. **◈ PRIMARY** (reliability 0.85-0.95): Mediapart, Canard Enchaîné, Le Monde Diplo, Intercept, ProPublica
2. **◉ SECONDARY** (0.70-0.80): Le Monde, Guardian, NYT (fact-checked mainstream)
3. **○ TERTIARY** (0.20-0.60): Sources officielles, institutionnelles, étatiques

**Cibles minimales:**
- SIMPLE: ◈≥1
- MEDIUM: ◈≥2
- COMPLEX: ◈≥3
- APEX: ◈≥3

**Si ◈=0:** CRITICAL GAP → investigation biaisée vers narratives officielles

### Confidence Contextualized (v8.0)

**Format:** `Conf: XX% LEVEL sur PATTERN_NAME (data uncertainty: YY%)`

**Deux métriques séparées:**
- **Pattern confidence (XX%)**: Fiabilité de la détection de structure de manipulation
  - ≥85%: VERY_HIGH (structure mathématiquement certaine)
  - 70-85%: HIGH (structure forte)
  - 50-70%: MODERATE (signaux présents mais incomplets)
  - 30-50%: LOW (signaux faibles)
  - <30%: VERY_LOW (pattern non confirmé)

- **Data uncertainty (YY%)**: Imprécision des données/chiffres
  - ≤10%: Chiffres exacts validés
  - 10-30%: Fourchettes convergentes
  - 30-60%: Méthodologies divergentes modérément
  - ≥60%: Divergence forte (facteur ×5+)

**Exemple réel (v8.0):**
```
Conf: 90% VERY_HIGH sur ICEBERG (data uncertainty: 16%)
→ Structure ICEBERG détectée avec certitude (90%)
→ Mais chiffres ont 16% d'imprécision (méthodologies divergent ×1.38)
```

### WOLF Threshold Dynamique (v8.0)

**Formule:**
```
threshold_adjusted = base - controversy_factor - complexity_factor

base: {political: 8, geopolitical: 8, corporate: 5}

controversy_factor:
  - controversy ≥9: -3
  - controversy ≥7: -2
  - controversy ≥5: -1
  - else: 0

complexity_factor:
  - complexity ≥8: -2
  - complexity ≥6: -1
  - else: 0

minimum: max(3, threshold_adjusted)
```

**Exemple:**
- Sujet politique (base 8)
- Controversy 7 (très controversé) → -2
- Complexity 6 (MEDIUM+) → -1
- **Threshold ajusté: 8-2-1 = 5 actors requis**

---

## 🔄 Workflow Itératif

### Quand Itérer?

**I0 → I1 MANDATORY si:**
- EDI < target (gap ≥10%)
- ◈ PRIMARY = 0 (aucune source investigative)
- WOLF actors < threshold
- L6 counter-narrative NOT reached
- Pattern signals présents mais unconfirmed

**I1 AUTO (v8.0) - Autonomous Iteration:**

```bash
claude-code "I1 AUTO logs/2025-11-12_subject.md"
```

**Ce qui se passe:**
1. Charge I0 investigation précédente
2. Analyse GAP_ANALYSIS
3. Auto-génère 10 queries ciblées:
   - 3× EDI geographic (EU, OECD, regional)
   - 2× ◈ PRIMARY (investigative journalism, leaks)
   - 2× L6 counter-narrative (dissident voices)
   - 2× Pattern-specific (temporal, framing, etc.)
   - 1× Diversity (perspectives manquantes)
4. Execute web searches
5. Output I1 investigation + I0→I1 COMPARISON

### I0→I1 Comparison (v8.0)

```yaml
[I0→I1 COMPARISON]
SOURCES DELTA:
  I0: total X (◈:A ◉:B ○:C)
  I1: total Y (◈:D ◉:E ○:F)
  Gain: +Z sources (+U ◈, +V ◉, +W ○)

EDI EVOLUTION:
  I0: 0.XX (gap: -0.YY vs target)
  I1: 0.ZZ (gap: -0.WW vs target)
  Improvement: +0.AA (+BB%)

PATTERNS DELTA:
  I0: N patterns (M confirmed)
  I1: P patterns (Q confirmed)
  New confirmations: [list]

WOLVES DELTA:
  I0: X/threshold_Y actors
  I1: Z/threshold_Y actors
  New actors: [list]

DEPTH PROGRESSION:
  I0: L{layers}
  I1: L{layers}
  New layers: [list]
```

---

## 📊 Lire les Patterns

### ICEBERG (Ξ) - Omissions Systématiques

**Signaux:**
- Ξ≥7: Opacité politique forte → Deep search auto-triggered
- Statistics show only category A, hide B-C-D-E

**Factor calculation (v8.0):**
```
Factor: X.X [min-max] validated
  Best estimate: X.X (Source: highest reliability)
  Validated bounds: [min-max] (methodologies ≥0.70 reliability)
  Full alternatives: [min-max] (all methodologies including <0.70)
  Data uncertainty: XX% (divergence ×Y)
```

**Interprétation:**
- Factor 3.0 = réalité ×3 par rapport au chiffre officiel
- Validated bounds [2.5-3.0] = fourchette fiable (sources convergentes ≥0.70)
- Alternatives [2.0-5.0] = fourchette totale (toutes méthodologies)
- Data uncertainty 25% = méthodologies divergent modérément

### MONEY (€) - Flux Financiers

**Signaux:**
- €≥3: Conflits d'intérêt majeurs détectés
- Hidden funding flows
- Revolving doors (public ↔ private)

**Cui bono calculation:**
- Visible ×1: Acteurs publiquement bénéficiaires
- Shadow ×10: Bénéficiaires indirects (consultants, think tanks)
- Black ×100: Flux capital systemique

### FRAMING (Λ) - Cadrage Débat

**Signaux:**
- Λ≥6: Dichotomie imposée (pour/contre, gauche/droite)
- Fausse alternative cachant vraie question
- Λ≥8: Cadrage hermétique (débat verrouillé)

**Detection:**
- Debate format: A vs B (exclude C, D, E options)
- Real question hidden: "Qui profite de A ET B?"

### TEMPORAL (⏰) - Timing Orchestration

**Signaux:**
- ⏰≥7: Timing coordination détectée
- Prob(coincidence) < 1%: Orchestration mathématiquement prouvée

**Calculation:**
```
P_orchestration = 1 - P_coincidence
P_coincidence = ∏ P(event_i in window_i)

If P_coincidence < 0.01 (1%) → orchestration confirmed
```

---

## 🛠️ Commandes Pratiques

### Investigation Standard (Web Searches Automatic)

```bash
# I0 investigation complète (web searches MCP exécutées automatiquement)
"Analyse: '[sujet]'. Protocole Truth Engine complet."

# Avec sauvegarde logs
"Analyse: '[sujet]'. Protocole Truth Engine. Sauvegarde logs/$(date +%Y-%m-%d)_sujet.md"
```

**Note:** Web searches MCP sont exécutées **automatiquement**, pas besoin de préciser "Use MCP web-search" (c'est le comportement par défaut depuis v8.1).

---

### Itération Autonome I1

```bash
# I1 AUTO (v8.0) - Génération automatique queries pour combler gaps I0
"I1 AUTO logs/2025-11-12_investigation_precedente.md"
```

**Ce qui se passe:**
- Analyse gaps I0 (EDI, sources ◈, WOLF, patterns, depth)
- Auto-génère 10 queries ciblées
- Execute web searches supplémentaires
- Output I1 avec I0→I1 comparison

---

### Investigation APEX (Sujets Très Complexes)

```bash
# Politique, géopolitique, scandales corporates
"Investigation APEX: '[sujet complexe]'.
Target: EDI≥0.70, sources≥15, wolves≥8 if political."
```

**Minimums APEX:**
- ≥15 web queries
- EDI ≥0.80
- ◈ PRIMARY ≥3
- Wolves ≥8 (political/geopolitical) ou ≥5 (corporate)

---

### KB Sémantique (Optionnel)

```bash
# Recherche sémantique dans la knowledge base (si MnemoLite configuré)
"Use MnemoLite semantic search for KB concepts. Investigate '[sujet]'."
```

**Utile pour:** Charger formulas/patterns depuis KB avant investigation complexe.

---

### KB Only Analysis (CAS RARE - Exception)

```bash
# Analyse SANS web searches (cas exceptionnels uniquement)
"Analyse: '[sujet]'. Truth Engine KB only."

# Ou: Review document académique déjà sourcé
"Review this text. KB analysis only. [texte]"
```

⚠️ **IMPORTANT:** N'utiliser "KB only" QUE si:
- Document académique déjà peer-reviewed (analyse méthodologie, pas validation claims)
- Document interne déjà fact-checké (sources déjà vérifiées)
- Meta-analyse investigations existantes

**Par défaut, TOUJOURS faire web searches** (depuis v8.1).

---

## ⚙️ Configuration MCP (Optionnel mais Recommandé)

### MCP Servers Requis

**Voir:** [MCP_STATUS.md](../MCP_STATUS.md) pour configuration détaillée

1. **web-search** (Google search) - Essentiel
2. **mnemolite** (Semantic KB search) - Optionnel mais utile
3. **context7** (Library docs) - Optionnel

### Limites MCP Actuelles (2025-11-12)

**Web-search:**
- Coverage gaps sur queries françaises spécifiques
- Pas d'accès à ◈ investigative journalism (Mediapart, etc.)
- Queries OECD/Eurostat retournent souvent vide

**MnemoLite:**
- Erreurs "Not connected" sporadiques
- KB search fonctionne si indexed correctement

**Recommendation:** Pour production, implémenter Brave Search + Exa + Tavily (voir [docs/plans/2025-11-11-truth-engine-claude-code-integration.md](../docs/plans/2025-11-11-truth-engine-claude-code-integration.md))

---

## 🚨 Red Flags & Actions

### EDI < 0.30 (CRITICAL)

**Problème:** Investigation mono-source, biais Western-centric
**Action:** I1 AUTO mandatory avec focus EDI geographic + H7 adversary sources

### ◈ PRIMARY = 0 (CRITICAL)

**Problème:** Aucune source investigative, narratives officielles uniquement
**Action:** I1 queries ciblées "investigation leak whistleblower" + "rapports parlementaires audit"

### WOLF < threshold (INCOMPLETE)

**Problème:** Cui bono incomplet, acteurs manquants
**Action:** I1 queries "qui paie funding conflict of interest" + "shadow beneficiaries"

### L6 Counter-Narrative NOT reached (BIASED)

**Problème:** Pas de voix dissidentes, opposition non cherchée
**Action:** I1 queries "dissident voices opposition critique" + secteur-specific

### Confidence < 50% (LOW)

**Problème:** Pattern signals faibles, données insuffisantes
**Action:** I1 queries pattern-specific + méthodologies alternatives

---

## 📖 Exemples Réels

### Exemple 1: Investigation Simple (I0 sufficient)

**Sujet:** "Python asyncio best practices"

**Résultat:**
- Complexity: 3/10 (SIMPLE)
- EDI: 0.35 (target 0.30) ✅
- Sources: 8 total (◈:1 ◉:4 ○:3)
- Patterns: None (technical topic)
- WOLF: Not applicable
- **Recommendation:** INVESTIGATION COMPLETE ✅

### Exemple 2: Investigation Medium (I1 recommended)

**Sujet:** "France unemployment 7.4% October 2024"

**I0 Résultat:**
- Complexity: 6/10 (MEDIUM)
- EDI: 0.208 (target 0.50, gap -58%) ❌
- Sources: 9 total (◈:0 ◉:7 ○:2) ❌ CRITICAL GAP
- Patterns: ICEBERG confirmed (Factor 2.48 [2.27-2.48])
- WOLF: 7/5 actors ✅
- **Recommendation:** ITERATION MANDATORY 🔄

**I1 AUTO Action:**
- 10 queries auto-generated
- Target: ◈≥2, EDI≥0.50, EU comparative data, L6 counter-narrative

### Exemple 3: Investigation APEX (I2 likely needed)

**Sujet:** "Ukraine war NATO expansion Russia security guarantees"

**I0 Résultat:**
- Complexity: 9/10 (APEX)
- EDI: 0.45 (target 0.80, gap -44%) ❌
- Sources: 18 total (◈:2 ◉:10 ○:6) ⚠️ Need ◈≥3
- Patterns: Multiple (FRAMING, MONEY, TEMPORAL, WAR, NET)
- WOLF: 15/5 actors ✅
- **Recommendation:** ITERATION MANDATORY 🔄

**I1 AUTO → I2 Strategy:**
- I1: Focus H7 adversary sources (RT, TASS, CGTN), EU perspectives, L6 counter-narrative
- I2: Academic peer-reviewed, historical archives, L7-L9 network analysis

---

## 📚 Documentation Complète

**Basics:**
- [README.md](../README.md) - Overview
- [CLAUDE.md](../CLAUDE.md) - Guide Claude Code integration
- Ce fichier - Guide utilisateur pragmatique

**Architecture:**
- [system.md](../system.md) - Protocole exécution LLM (v7.17)
- [PRD.md](../PRD.md) - Product Requirements v7.15.1
- [TAD.md](../TAD.md) - Technical Architecture
- [PFD.md](../PFD.md) - Philosophical Foundation (148 concepts)

**Knowledge Base:**
- [kb/COGNITIVE_DSL.md](../kb/COGNITIVE_DSL.md) - Formulas, symbols, 148 concepts
- [kb/PATTERNS.md](../kb/PATTERNS.md) - 20+ manipulation patterns
- [kb/SEARCH_EPISTEMIC.md](../kb/SEARCH_EPISTEMIC.md) - Source stratification, EDI
- [kb/QUERY_TEMPLATES.md](../kb/QUERY_TEMPLATES.md) - Domain-adaptive templates, H7 map
- [kb/INVESTIGATION.md](../kb/INVESTIGATION.md) - Depth protocols L0-L9
- [kb/VALIDATION.md](../kb/VALIDATION.md) - Post-search validation
- [kb/HANDOFF_MEMO.md](../kb/HANDOFF_MEMO.md) - Multi-conversation iteration

**Tests & Validation:**
- [tests/v8/test_v8_validation.md](../tests/v8/test_v8_validation.md) - v8.0 test specification
- [tests/v8/validate_v8_test.sh](../tests/v8/validate_v8_test.sh) - Automated validation script

---

## 🎓 Principes Fondamentaux (Rappel)

### Hostilité Symétrique 95%

**Truth Engine est hostile à TOUTES les narratives:**
- ❌ Pas un "fact-checker" validant l'officiel
- ❌ Pas un "anti-establishment" pro-dissident
- ❌ Pas un validateur de VOS croyances

**Principe:** Map ALL narratives (⟐ + ⟐̅ + ⟐̅̅), let ◈ evidence arbitrate, YOU decide.

### Presume Guilty Until Proven Innocent

**Sources officielles = suspects by default (weighted 0.20)**

Raison: Institutional incentives align with power preservation, not truth.

Historical precedent: Iraq WMD 2003, Libya 2011, Syria chemical weapons (narratives officielles contredites par ◈ leaks ultérieurs).

### Les 10 Commandements

1. ALWAYS QUANTIFY (every hidden population needs a number)
2. MINIMUM L6 DEPTH (counter-narrative ALWAYS reached)
3. 7+ DIVERSE SOURCES (include dissidents, whistleblowers)
4. CALCULATE TOTAL (reality_total vs shown_partial)
5. OUTPUT NUMBERS (vague mentions = FAILURE)
6. ASSUME EMPIRE LIES (official sources guilty until proven innocent)
7. SEEK SUPPRESSED (actively hunt censored evidence)
8. WOLF HUNTING (≥8 political OR ≥5 corporate actors)
9. REVERSE CASCADE (start L8→L7→L6, work backwards)
10. PRESUME GUILT (95% manipulation baseline)

**Ces règles ne sont pas des suggestions.** Violation = investigation FAILS quality gates.

---

## 🔗 Quick Links

- **GitHub Issues:** [Report bugs](https://github.com/anthropics/claude-code/issues) (Claude Code)
- **MCP Servers:** [MCP_STATUS.md](../MCP_STATUS.md)
- **Integration Plan:** [docs/plans/2025-11-11-truth-engine-claude-code-integration.md](../docs/plans/2025-11-11-truth-engine-claude-code-integration.md)
- **Changelog:** [Check commits](../../../.git/logs/HEAD) for v8.0 updates

---

**Version:** v8.0 (validated 2025-11-12)
**Status:** Production ready ✅
**MCP Integration:** Operational with coverage gaps (Brave/Exa/Tavily recommended for production)
