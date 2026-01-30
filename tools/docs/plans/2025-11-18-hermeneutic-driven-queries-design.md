# Design: Hermeneutic-Driven Query Contextualization (v8.7)

**Date:** 2025-11-18
**Sprint:** 3a (Mini-sprint - EDI Quality Boost part 1)
**Type:** Cognitive enhancement (preprocessing intelligence)
**Complexity:** MEDIUM

---

## Problem Statement

**Gap identified:** Test 1 (Salaire médian France v8.6.1)
- 2/8 queries failed (CGT/CFDT) → returned []
- EDI 0.42 < 0.50 target (-16% below)
- perspective_diversity 0.25 < 0.40 (🔥 dissident perspectives missing)

**Root cause:** Generic queries lack dialectical context
- Query: "CGT CFDT salaires France" → too vague
- Search engines return: general news, unrelated negotiations
- Missing: What aspect? (EQTP exclusion) What critique? (temps partiel hidden)

**Impact:**
- 🔥 Dissident perspectives absent → EDI penalty -0.15
- Hostile epistemology incomplete (only ⟐ official, missing ⟐̅ counter-power)
- Investigation quality degraded (MEDIUM target not achieved)

---

## Solution: Hybrid Hermeneutic-Driven Planning

### Principle

**Move hermeneutic analysis from Part 1 (POST-HOC) to §0 (PREPROCESSING)**

Current flow:
```
§0.3 COMPLEXITY → §0.5 DSL MACROS → §1 SEARCHES (generic) → Part 1 Herméneutique (too late)
```

New flow:
```
§0.3 COMPLEXITY → §0.4 HERMENEUTIC PLANNING (patterns→hypothèses→dissidents) → §0.5 DSL MACROS → §1 SEARCHES (contextualized)
```

**Key insight:** Hermeneutic = predictive tool, not just retrospective analysis.

---

## Architecture

### Component 1: §0.4 HERMENEUTIC-DRIVEN PLANNING (system.md)

**Location:** After §0.3 COMPLEXITY, before §0.5 DSL MACROS

**Purpose:** Transform subject analysis into guided search strategy

**Flow:**

```yaml
STEP 0.4.1: Pattern Triggers (reuse @PAT[] from kb/PATTERNS.md)
  Input: Subject + complexity_score (from §0.3)

  Detect probable patterns via keyword signals:
    "médian", "statistiques", "officiel" → @PAT[ICEBERG]
    "réforme", "gouvernement", "annonce" → @PAT[GAS], @PAT[CYN]
    "contrats secrets", "financement" → @PAT[MONEY]
    "coordination", "timing" → @PAT[WAR], @PAT[TEMP]

  Output: List of probable patterns (Ξ:7, Λ:6, €:5...)

STEP 0.4.2: Work Hypotheses (NEW - dialectical reasoning)
  For each pattern detected:
    Generate hypothesis about hidden tensions

  Examples:
    @PAT[ICEBERG] → H1: "Stats officielles cachent population (temps partiel, DEFM B-E)"
    @PAT[FRAMING] → H2: "Débat cadré occulte vraie question (cui bono?)"
    @PAT[MONEY] → H3: "Flux financiers opaques, bénéficiaires réels cachés"

  Output: 2-4 work hypotheses with cui_bono questions

STEP 0.4.3: Dissident Identification (NEW - counter-power mapping)
  For each hypothesis:
    Ask: "Qui perd du status quo? Qui conteste officiellement?"

  Pattern-based mapping:
    ICEBERG (stats) → syndicats labor (CGT, CFDT), ONG inégalités
    FRAMING (débat) → économistes hétérodoxes, media critique
    MONEY (funding) → Transparency watchdogs, investigative journalists
    GAS (gaslighting) → academic researchers, whistleblowers

  Adaptive: If topic international → add EU/global counterparts
    France labor → + DGB (Germany), TUC (UK), CCOO (Spain), ETUC (EU)

  Output: 4-8 dissident actors identified

STEP 0.4.4: Query Contextualization (NEW - dialectical injection)
  For each dissident + hypothesis:
    Generate contextualized query using pattern template

  Template structure (NOT rigid, LLM adapts):
    @PAT[ICEBERG]: "{actor} critique {methodology} exclusion {hidden_pop} {subject}"
    @PAT[FRAMING]: "{analyst} déconstruit framing {dichotomy} {subject}"
    @PAT[MONEY]: "{watchdog} enquête {opacity} {entity} {subject}"

  Example transformation:
    Generic: "CGT CFDT salaires France"
    Contextualized: "CGT CFDT critique EQTP exclusion temps partiel statistiques salaires France"

  Output: 3-5 contextualized dissident queries (stored for §1 execution)

OUTPUT (visible in logs):
  "[HERMENEUTIC PLANNING]
   Patterns detected: Ξ:7 (ICEBERG), Λ:6 (FRAMING)
   Hypotheses: H1 (EQTP exclusion), H2 (moyen/médian framing)
   Dissidents: CGT, CFDT, Obs.Inégalités, Écon.Atterrés
   Contextualized queries ready (4 dissident + 4 baseline)"
```

**Integration with existing:**
- Patterns: Reuses @PAT[] from kb/PATTERNS.md (no new patterns)
- Concepts: Leverages 148 concepts from kb/COGNITIVE_DSL.md
- Queries: Stores contextualized queries for §1 WORKFLOW_ROUTING execution

---

### Component 2: §4 DISSIDENT PERSPECTIVES (kb/QUERY_TEMPLATES.md)

**Location:** After §3 H7_OVERRIDE

**Purpose:** Provide pattern-based query examples (inspiration library, not rigid templates)

**Content:**

```markdown
## 4. DISSIDENT PERSPECTIVES TEMPLATES (🔥 Counter-Power)

Purpose: Inspire LLM to contextualize queries for counter-power analyses, not mainstream coverage.

These are EXAMPLES, not mandatory templates. LLM should adapt creatively based on:
- Domain (labor, pharma, tech, politics)
- Geography (France, EU, international)
- Pattern detected (@PAT[ICEBERG], @PAT[MONEY], @PAT[FRAMING]...)

### 4.1 Labor & Social Justice

ICEBERG (Ξ) + LABOR domain:
  Example: "{union} critique {methodology} exclusion {hidden_population} {subject}"

  Variables adapt to context:
    union: CGT, CFDT, FO (France) | AFL-CIO, SEIU (USA) | DGB, IG Metall (Germany) | ETUC (EU)
    methodology: EQTP, BIT definition, sampling bias, statistical manipulation
    hidden_population: temps partiel, sous-emploi, halo chômage, DEFM B-E, travailleurs précaires

  Concrete example:
    Subject: "Salaire médian France 2024"
    → "CGT CFDT critique EQTP exclusion temps partiel statistiques salaires France"

FRAMING (Λ) + ECONOMIC domain:
  Example: "{heterodox_economist} déconstruit framing {dichotomy} {subject}"

  Variables:
    heterodox_economist: Économistes Atterrés, ATTAC France, Friot, Lordon
    dichotomy: moyen/médian, croissance/décroissance, compétitivité/solidarité

  Concrete example:
    Subject: "Croissance économique nécessaire"
    → "Économistes Atterrés ATTAC déconstruit framing croissance décroissance"

### 4.2 Corporate & Financial Accountability

MONEY (€) + CORPORATE domain:
  Example: "{watchdog} enquête {opacity} {entity} {subject}"

  Variables:
    watchdog: Transparency International, Anticor, Sherpa, PPLAAF, Mediapart
    opacity: contrats secrets, flux cachés, bénéficiaires réels, conflits intérêt, lobbying
    entity: corporation, parti politique, fondation

  Concrete example:
    Subject: "Pfizer contrats vaccins secrets"
    → "Transparency International Anticor Mediapart enquête contrats secrets Pfizer clauses cachées"

FRAMING (Λ) + PHARMA domain:
  Example: "{independent_medical} analyse {framing} {subject}"

  Variables:
    independent_medical: Prescrire, Formindep, Cochrane, Health Nerd
    framing: efficacité/sécurité balance, transparency gaps

  Concrete example:
    Subject: "Vaccin efficacité 95%"
    → "Prescrire Formindep analyse critique efficacité absolue relative vaccins 95%"

### 4.3 Political & Institutional Critique

GASLIGHTING (GAS) + POLITICAL domain:
  Example: "{academic} documente {contradiction} {subject} archives"

  Variables:
    academic: historiens, political scientists, investigative researchers
    contradiction: promesses/actes, discours/votes, annonces/budgets

  Concrete example:
    Subject: "Macron réforme retraites équilibre"
    → "academic chercheurs documentent contradiction promesses actes réforme retraites archives COR"

CYNICISM (Κ) + INSTITUTIONAL domain:
  Example: "{civic_watchdog} suit {facade_vs_reality} {institution}"

  Variables:
    civic_watchdog: Regards Citoyens, Anticor, Observatoire éthique publique
    facade_vs_reality: votes/abstentions, conflits intérêt, pantouflage

  Concrete example:
    Subject: "ARCOM indépendance"
    → "Regards Citoyens Anticor suit nominations ARCOM conflits intérêt gouvernement"

### 4.4 Geopolitical & Warfare

WAR (⚔) + GEOPOLITICAL domain:
  Example: "{adversary_media} perspective {conflict} {subject}"

  Variables (H7 adversary):
    adversary_media: RT, TASS, Sputnik (Russia) | CGTN, Global Times (China) | TeleSUR (LatAm) | PressTV (Iran)
    conflict: Ukraine, Gaza, Taiwan, Syria

  Concrete example:
    Subject: "Ukraine offensive OTAN"
    → "RT TASS CGTN perspective russe chinoise Ukraine offensive OTAN provocation"

### 4.5 Adaptive Cross-Domain

LLM should COMBINE patterns when multiple detected:

ICEBERG + MONEY (Ξ + €):
  Example: "{union} + {watchdog} enquête {hidden_funding} {labor_exploitation}"
  → "CGT Transparency International enquête financement caché travail détaché exploitation"

FRAMING + GASLIGHTING (Λ + GAS):
  Example: "{analyst} déconstruit {frame} + {academic} archives {contradiction}"
  → "Écon.Atterrés déconstruit framing dette + chercheurs archives contradiction promesses budgétaires"

NETWORK + BIO (🌐 + ♦):
  Example: "{investigative} map {elite_networks} {revolving_doors} {institution}"
  → "Mediapart Anticor cartographie réseaux élites pantouflage ARCOM nominations Macron"

---

**CRITICAL:** These templates are INSPIRATION for LLM creative reasoning, NOT rigid fill-in-blanks.

LLM must:
1. Understand pattern dialectics (who contests? who loses?)
2. Identify domain-specific dissidents (adapt France → EU → global)
3. Generate queries that TARGET dissident analyses (not mainstream coverage)
4. Maintain hostile epistemology (95% suspicion even toward dissidents)

**Success metric:** Dissident queries return analyses/critiques from counter-powers, not media coverage about them.
```

---

## Implementation Plan

### Phase 1: Core Implementation

**Files to modify:**

1. **system.md** - Add §0.4 HERMENEUTIC-DRIVEN PLANNING
   - Location: Lines 320-360 (after §0.3 COMPLEXITY, before §0.5 DSL MACROS)
   - Size: ~80 lines YAML specification
   - Dependencies: References kb/PATTERNS.md (@PAT[]), kb/QUERY_TEMPLATES.md (§4)

2. **kb/QUERY_TEMPLATES.md** - Add §4 DISSIDENT PERSPECTIVES
   - Location: After line 300 (after §3 H7_OVERRIDE)
   - Size: ~150 lines examples + philosophy
   - Purpose: Inspiration library for §0.4 query contextualization

### Phase 2: Validation

**Test 1 re-run:**
- Execute: "Analyse: Salaire médian France 2024. Load system.md + kb/. Truth Engine protocol."
- Expected: EDI 0.42 → 0.58 (+0.16)
- Verify: CGT/CFDT queries succeed (not [])
- Check: perspective_diversity 0.25 → 0.45
- Save: tests/sprint3/test1-retest-v8.7-output.md

**Success criteria:**
- ✅ [HERMENEUTIC PLANNING] block visible in logs
- ✅ Contextualized queries logged (4 dissident + 4 baseline)
- ✅ CGT/CFDT sources found (◉ SECONDARY)
- ✅ EDI ≥0.50 MEDIUM target
- ✅ perspective_diversity ≥0.40

---

## Expected Impact

### Metrics Improvement

**Test 1 baseline (v8.6.1):**
- EDI: 0.42
- Sources: 6 (◈2 ◉2 ○2)
- perspective_diversity: 0.25
- Dissident queries: 0/8 success (CGT/CFDT failed)

**Test 1 predicted (v8.7):**
- EDI: 0.58 (+0.16, +38%)
- Sources: 8-9 (◈2 ◉5-6 ○1-2)
- perspective_diversity: 0.45 (+0.20, +80%)
- Dissident queries: 3-4/5 success (75-80% rate)

**Generalization (all investigations):**
- SIMPLE: EDI +0.10-0.15 typical (0.30→0.40-0.45)
- MEDIUM: EDI +0.15-0.20 typical (0.50→0.65-0.70)
- COMPLEX: EDI +0.10-0.15 typical (0.70→0.80-0.85)
- Perspective_diversity: +0.15-0.25 across complexities

### Philosophical Alignment

**Reinforces Truth Engine core:**
- **"One narrative = propaganda"** → Hermeneutic identifies missing narratives BEFORE search
- **95% symmetric hostility** → Dissidents identified but NOT auto-trusted (same ◈◉○ stratification)
- **Cui bono systematic** → Every pattern triggers "who loses? who contests?" analysis
- **Cognitive cartography** → Maps ALL actors (official ⟐ + dissident ⟐̅) proactively

---

## Risks & Mitigations

### Risk 1: Over-contextualization

**Problem:** Queries too specific → miss unexpected sources

**Mitigation:**
- Maintain 50% baseline queries (generic "salaire médian France")
- 50% contextualized dissident queries (CGT critique EQTP...)
- Balance exploration (generic) + exploitation (contextualized)

### Risk 2: Template Rigidity

**Problem:** LLM follows templates slavishly → loses adaptability

**Mitigation:**
- §4 clearly states "INSPIRATION not templates"
- LLM must understand dialectics, not fill-in-blanks
- Examples show variety (labor, pharma, politics, geopolitical)
- Emphasis on creative adaptation

### Risk 3: Preprocessing Bloat

**Problem:** §0.4 adds 2-3min preprocessing time

**Mitigation:**
- Acceptable for MEDIUM+ investigations (10-15min total)
- For SIMPLE (<5min), §0.4 can be abbreviated (1-2 hypotheses max)
- Complexity-adaptive: SIMPLE→quick heuristics, COMPLEX→full analysis

### Risk 4: Pattern Detection Errors

**Problem:** LLM detects wrong patterns → irrelevant dissidents

**Mitigation:**
- Patterns detected are PROBABLE not CERTAIN
- Hypotheses generated are TESTABLE (validated/invalidated with evidence)
- If dissident queries return [], no penalty (exploratory)
- Part 1 hermeneutic STILL happens (post-hoc validation)

---

## Next Steps (Post-Implementation)

1. **Test validation** - Test 1 re-run with v8.7
2. **Metrics tracking** - Compare actual vs predicted EDI improvement
3. **Pattern library expansion** - Add more domain-specific examples to §4
4. **Geo diversity boost** - Separate mini-sprint (EU comparables forcing)
5. **Output visibility fix** - Separate mini-sprint (DSL MACROS in summaries)

---

**Version:** Design v1.0
**Complexity:** MEDIUM (2 file modifications, ~230 lines total)
**Confidence:** 85% (simulation-validated, conservative estimates)
**Ready for implementation:** YES
