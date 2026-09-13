# PATTERNS v2.2 — Diagnostic signatures and formulas

Patterns generate questions and comparable measurements. They are not verdicts. Show inputs, units, missing values and sensitivity; never invent a denominator or convert a heuristic into probability.

## §1 Shared scoring discipline

```text
OBSERVE → MEASURE when comparable data exist → TEST counter-explanation → CLASSIFY → RECORD GAP.
Normalize a formula to [0..10] only when its input scale is explicit.
LOW 1–2 | PLAUSIBLE 3–4 | MATERIAL 5–6 | STRONG 7–8 | EXTENSIVE 9–10.
No input → NOT COMPUTABLE, not zero. Division by zero → NOT COMPUTABLE.
```

## §2 Core @PAT[]

### @PAT[ICEBERG] — Ξ

- Signature: selective period/category/denominator/method plus material omitted population or value.
- Measured factor, only for comparable quantities: `ICEBERG_FACTOR = total_relevant / visible_claimed`.
- If total is unknown: record omission dimensions and bounds; do not manufacture a ratio.
- Flow: claim → definition → exclusions → reconstructed range → sensitivity → gap.

### @PAT[MONEY] — €

- Signature: material beneficiary + opaque flow/ownership/COI + decision relevance.
- When amounts are comparable: `MONEY_FACTOR = hidden_or_indirect / declared_direct`.
- Otherwise score documented signals: funding opacity, revolving door, subsidy, capture, externality, ownership concentration.
- Flow: payer → channel → intermediary → beneficiary → decision → disclosed/hidden.

### @PAT[BIO] — ♦

- Signature: public biography omits decision-relevant affiliations, access path or revolving doors.
- With a graph: `DENSITY = observed_links / possible_links`; state node/edge definitions.
- Without a graph: use a sourced chronology across education, career, family, clubs, boards, donations, media and politics.
- Flow: position → prior tie → documented action → timing → responsibility boundary.

### @PAT[NET] — 🌐

- Signature: repeated actors plus evidenced links and control points.
- Metrics only on an explicit graph: density, degree/betweenness, components and ownership/control edges.
- A shared school, event or employer is association, not coordination.
- Flow: nodes → typed edges → provenance → gatekeepers → alternative topology.

### @PAT[WAR] — ⚔

- Signature: message/timing coordination plus infrastructure, targeting or tasking evidence.
- Diagnostic index: mean of observed `coordination,sophistication,persistence,targeting` minus uncertainty for attribution/independence; document scales.
- Similar wording alone may arise from wire copy, common facts or imitation. Test these first.
- Flow: content → distribution → infrastructure → command/tasking evidence → attribution confidence.

### @PAT[TEMP] — ⏰

- `P_ORCH = .30×sync + .25×vocab + .20×prepared_benefit + .15×historical_match + .10×suppression`, each observed input [0..10].
- This is a review index, not a statistical probability.
- `P_random` may be reported only from a defensible stated null model, sample/window and assumptions; otherwise `NOT ESTIMATED`.
- Flow: full timeline → independent clocks → common upstream cause → coordination evidence → alternatives.

### @PAT[GAS] — Ω

- Signature: archived statement/action conflicts with current denial plus attack on witness/memory or replacement narrative.
- Flow: exact claim → contemporaneous archive → current claim → material contradiction → plausible correction/context → assessment.
- A correction, changed evidence or honest policy reversal is not automatically gaslighting.

### @PAT[ASTRO] — €/⫸

- Signature: purported grassroots movement plus opaque funding and evidenced coordination/professional infrastructure.
- Flow: origin → legal entity/domain → funders → staff/vendors → message/timing → genuine-member evidence.
- Rapid growth or polished communication alone is insufficient.

### @PAT[CYN] — Κ

- Signature: documented private/public contradiction or repeated institutional maintenance of a façade despite acknowledged failure.
- Flow: public rule → internal knowledge → action → beneficiary → accountability.
- Route: `clusters/INVERSION.md`.

### @PAT[FASC] — ⫸

- Signature: at least three materially independent indices converge on the same bounded hypothesis.
- `CONVERGENCE = supported_independent_indices / applicable_independent_indices`.
- Independence must be demonstrated; syndication or a common source counts once.
- Route: `clusters/FRAGMENTATION.md`.

## §3 Extended patterns

| Pattern | Trigger to investigate | Required falsifier/check |
|---|---|---|
| @PAT[POLITICAL] | visible policy/power redistribution | mandate, legal competence, baseline and duration |
| @PAT[GEOPOLITICAL] | multi-actor interest divergence | perspectives from involved, neighboring and non-aligned actors |
| @PAT[DEEPFAKE] | synthetic-media artifacts or provenance gap | original file, metadata, reverse search, expert/tool limits |
| @PAT[SURV_CAP] | data extraction + behavioral use + opaque value transfer | product terms, data flows, revenue and user controls |
| @PAT[COG_INFRA] | large-scale targeting/distribution system | infrastructure, reach, governance and alternative explanation |

## §4 Rhetorical families

| Code | Family | Markers to quote and test |
|---|---|---|
| DEM | Demagogy | homogeneous “people/elites”, scapegoat, effortless solution |
| BF | Bad faith/sophistry | motte-and-bailey, moving goalposts, Gish gallop, whataboutism, straw man |
| NUM | Numeric abuse | missing base/denominator/range, incomparable periods, proxy substitution |
| AUTH | Authority performance | unsupported authority, tone policing, DARVO, credential substitution |
| FAC | Performative façade | symbolic policy, false equivalence, washing, action/claim gap |

Score [0..10] from quoted instances, materiality and repetition. Disagreement or emotional language alone is not manipulation.

## §5 Composite patterns

- `@PAT[SHOCK]`: acute event + artificial urgency + narrowed alternatives. Check real deadlines and counterfactual options.
- `@PAT[BIDERMAN]`: multiple coercive conditions. Use as descriptive checklist, not diagnosis by analogy.
- `@PAT[INFODEMIC]`: information rate/contradictions exceed stated processing capacity. Measure the sampled stream and window.

_Canonical authority: pattern signatures and formulas._
