# 🧊 CLUSTER ICEBERG - Omission Patterns
*Extended concepts for deep omission analysis (5KB)*

## Parent: Ξ (ICEBERG)
Activated when Ξ score ≥5

## Related Concepts

### OMISSION_SELECTIVE
**Pattern**: Cherry-picking favorable data points
**Detection**:
- "Selected period" without justification
- Best year shown, others hidden
- Geographic selection bias
**Query boost**: "complete timeline", "all regions", "full period"

### CATEGORY_TRICK
**Pattern**: Hiding in category definitions
**Detection**:
- "Category A" without B, C, D, E
- "Employed" without underemployed
- "Solved" without partially solved
**Query boost**: "all categories", "including category", "broader definition"

### SHADOW_POPULATION
**Pattern**: Invisible populations not counted
**Detection**:
- "Active" without inactive mentioned
- "Registered" without unregistered
- "Official" without unofficial
**Query boost**: "unregistered", "informal", "shadow", "hidden"

### DENOMINATOR_MANIPULATION
**Pattern**: Changing the base to improve ratio
**Detection**:
- Population base undefined
- Denominator switch mid-analysis
- Exclusions not mentioned
**Query boost**: "calculation method", "denominator", "base population"

### TIMEFRAME_CHERRY
**Pattern**: Convenient time window selection
**Detection**:
- Starting point arbitrary
- Ending before bad data
- Comparison years cherry-picked
**Query boost**: "historical data", "10 year", "since 2000"

### AVERAGING_TRICK
**Pattern**: Averages hiding extremes
**Detection**:
- Mean without median
- No standard deviation
- No distribution shown
**Query boost**: "median", "distribution", "percentiles", "range"

### PROXY_SUBSTITUTION
**Pattern**: Measuring proxy not real thing
**Detection**:
- "Indicator of" not direct measure
- Proxy correlation assumed
- Real metric available but hidden
**Query boost**: "direct measurement", "actual numbers", "not proxy"

### COMPARATIVE_ABSENCE
**Pattern**: No comparison provided
**Detection**:
- Single number without context
- No year-over-year
- No international comparison
**Query boost**: "compared to", "versus EU", "year over year"

### METHODOLOGY_OPACITY
**Pattern**: Method hidden or vague
**Detection**:
- "Our methodology" not explained
- "Proprietary calculation"
- Formula not provided
**Query boost**: "methodology", "calculation method", "formula"

### CONFIDENCE_MISSING
**Pattern**: No error bars or confidence intervals
**Detection**:
- Precise number without range
- No confidence interval
- No margin of error
**Query boost**: "confidence interval", "margin error", "uncertainty"

---

## HERMENEUTIC EXPANSION

When CLUSTER_ICEBERG is loaded, generate these hypotheses:

### H1: QUANTITATIVE SHADOW
"What is the real total if we include all hidden categories?"
- Search: Complete data including shadow populations
- Calculation: Visible + Shadow estimates

### H2: TEMPORAL REVELATION
"What appears if we extend the timeframe?"
- Search: Historical data 20+ years
- Pattern: Cyclic patterns hidden by short window

### H3: COMPARATIVE TRUTH
"How does this compare internationally?"
- Search: Same metric other countries
- Reveal: Outlier status or normalcy

### H4: METHODOLOGY IMPACT
"How much does the methodology affect the result?"
- Search: Alternative calculation methods
- Compare: Different methodologies' results

### H5: DISTRIBUTION REALITY
"What does the distribution reveal that the average hides?"
- Search: Percentile data, distribution graphs
- Uncover: Inequality hidden by averages

---

## INVESTIGATION TRIGGERS

IF Ξ ≥7 (High ICEBERG):
1. Activate ALL concepts in this cluster
2. Generate all 5 hypotheses
3. Allocate +5 search queries for deep dive
4. Require ◈ PRIMARY sources for validation
5. Calculate shadow multiplier (reality/shown)

IF Ξ ≥9 (Extreme ICEBERG):
- Flag as CRITICAL OMISSION
- Demand full methodology disclosure
- Search for whistleblower/leaked data
- Calculate "Iceberg Factor" (hidden/visible ratio)