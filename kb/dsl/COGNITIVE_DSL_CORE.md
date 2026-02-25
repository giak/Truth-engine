# 🧠 COGNITIVE DSL - CORE CONCEPTS v9.3

_6 concepts fondamentaux pour scan initial (~2.5KB)_

## Ξ (XI) - ICEBERG Pattern

**Detection**: Surface shown < 10% of reality
**Score**: 0-10 based on omission signals
**Triggers**:

- "according to" without source → +2
- Missing comparative data → +3
- Single metric without context → +3
- Absence of methodology → +2
  **Activation**: If score ≥5 → Load CLUSTER_ICEBERG.md
  **Queries**: "{topic} complete data", "{topic} full report", "{topic} methodology"

## € (EURO) - MONEY Pattern

**Detection**: Hidden financial flows and interests
**Score**: 0-10 based on economic signals
**Triggers**:

- Benefit without beneficiary named → +3
- Policy change without cost analysis → +2
- "Investment" without ROI → +2
- Missing funding sources → +3
  **Activation**: If score ≥5 → Load CLUSTER_MONEY.md
  **Queries**: "{topic} funding", "{topic} who profits", "{topic} cost benefit"

## Λ (LAMBDA) - FRAMING Pattern

**Detection**: Imposed false choices and boundaries
**Score**: 0-10 based on framing signals
**Triggers**:

- "We must choose between" → +3
- "The debate is" → +2
- Binary options presented → +3
- Missing third option → +2
  **Activation**: If score ≥5 → Load CLUSTER_FRAMING.md
  **Queries**: "{topic} alternatives", "{topic} false dilemma", "{topic} other options"

## Ω (OMEGA) - INVERSION Pattern

**Detection**: Reality reversal and doublespeak
**Score**: 0-10 based on contradiction signals
**Triggers**:

- Action opposite to stated goal → +4
- "Protection" that harms → +3
- "Freedom" that restricts → +3
- War called peace → +4
  **Activation**: If score ≥5 → Load CLUSTER_INVERSION.md
  **Queries**: "{topic} contradiction", "{topic} opposite effect", "{topic} doublespeak"

## Ψ (PSI) - OVERLOAD Pattern

**Detection**: Cognitive saturation and confusion
**Score**: 0-10 based on overload signals
**Triggers**:

- 10+ sources saying different things → +3
- Urgent + Complex + No time → +3
- Technical jargon overuse → +2
- Information avalanche → +2
  **Activation**: If score ≥5 → Load CLUSTER_OVERLOAD.md
  **Queries**: "{topic} summary", "{topic} key points", "{topic} simple explanation"

## ↕ (UPDOWN) - VERTICAL STRATIFICATION Pattern

**Detection**: Power asymmetries (top/bottom), class divisions, vertical solidarity/blocking
**Score**: 0-10 based on stratification signals
**Triggers**:

- Elite-only access mentioned → +3
- Bottom-up perspective absent → +3
- Vertical solidarity mentioned → +2
- Top-down imposition → +3
- Asymmetric impact (some benefit, others suffer) → +3
  **Activation**: If score ≥5 → Load CLUSTER_TEMPORAL.md (contains ↕ analysis)
  **Queries**: "{topic} who benefits", "{topic} who loses", "{topic} class impact"

---

## ACTIVATION PROTOCOL

```yaml
SCAN_PROTOCOL:
  VERSION: "v2.0 ENHANCED"
  INPUT: text + subject
  PRE_PROCESS:
    - Extract entities, dates, locations from text
    - Query MnemoLite for related investigations
    - Boost scores for confirmed patterns (+2)
  PROCESS:
    FOR each concept IN [Ξ, €, Λ, Ω, Ψ, ↕]:
      score = calculate_weighted_score(triggers_detected)
      IF score ≥ 5:
        IF concept == ↕: LOAD: CLUSTER_TEMPORAL.md
        ELSE: LOAD: CLUSTER_{concept}.md
        ACTIVATE: @MACRO[ACTIVATE_CLUSTER]
        EXECUTE:
          - Load cluster file
          - Execute cluster-specific protocols
          - Generate cluster-specific queries
          - Add to investigation budget
  OUTPUT:
    scores: weighted_scores
    activated: activated_clusters
    queries_generated: cluster_specific_queries
```
