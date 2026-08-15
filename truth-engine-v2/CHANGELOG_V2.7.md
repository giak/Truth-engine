# Truth Engine v2.7 — Behavior-hardened generic investigation release

## Why v2.7 exists

Behavioral simulations showed that v2.6 fixed the fact-check regression directionally but still allowed three formal loopholes:

1. `OBJECT_QUESTION` could remain too narrow while material expansion leads were treated as context.
2. An axis could end in a bare `GAP` without auditable research attempts.
3. After context loss, a compact checkpoint could retain lead summaries but not enough source text to verify exact supplied claims.

The first resume simulation also exposed a false success: non-empty excerpts contained timestamps only. v2.7 therefore requires materially self-contained excerpts, not merely non-empty strings.

## Generic input contract

The corruption transcript is an anti-regression case, not the product model. KERNEL accepts any substantive text/source, including a tweet, idea, claim, transcript, report, code/data excerpt or URL, and any investigation subject.

Generic lead kinds:

`CLAIM | EVENT | ENTITY | OBJECT | RELATION | MECHANISM | CONTEXT`

Generic investigation axes:

`SOURCE_AUDIT | SCOPE_HISTORY | EVIDENCE_CASES | RESOURCES_FLOWS | MECHANISMS | ACTORS_RELATIONS | RULES_CONTROLS | IMPACT_RESPONSIBILITY | COUNTER_HYPOTHESES`

Only applicable axes execute. `N/A` remains logical irrelevance; absent evidence is an auditable `GAP`.

## Corrections

- `ROUTES` is now a list: a lead may require both source audit and object expansion; `EXCLUDE(reason)` is exclusive.
- `OBJECT_COVERAGE` maps every DECISIVE/IMPORTANT `EXPAND/LINK` lead to OBJECT_QUESTION or a named branch.
- A material event, object, relation, flow or mechanism cannot remain `AUDIT`-only in INVESTIGATION mode.
- Every applicable axis stores `ATTEMPT_IDS:{QRY/SRC}` and `RESULT_IDS`; a bare status cannot pass G8/G9.
- `SATURATED`, `GAP` and `N/A` now have explicit terminal semantics.
- `INPUT_REF` preserves a validated URL/path when reopenable; otherwise `INLINE_UNSTABLE` is explicit.
- Every supplied DECISIVE/IMPORTANT lead retains a bounded, exact, materially self-contained `EVIDENCE_EXCERPT`. A heading/timestamp alone is invalid.
- Resume reopens validated input when possible, otherwise uses preserved excerpts and types unavailable context as `GAP_TYPE=ACCESS`.
- `RESOURCE_FLOW_MAP` generalizes financial tracing to money, data, material, authority and access without weakening financial-unit distinctions.
- Causal and impact routes now use subject-neutral language.

## Simulation evidence

The validation used the real 19-chapter regression transcript plus adversarial and generic fixtures.

- v2.6 pre-correction: 4/7 critical contract scenarios passed; three failed as listed above.
- Final consolidated behavioral simulations: 29/29 passed — contract/state 12/12, real-regression mutation 6/6, source-instruction injection 5/5 and worst-case resume 6/6.
- Structural/invariant checks: 20/20 passed, including 24 historical phases, 11 gates, module resolution, generic KERNEL vocabulary, one-write output and alias compatibility.
- The old 120-billion source-only output is rejected by G1/G2/G8.
- The `INLINE_UNSTABLE` round trip retained 19/19 segments and substantive excerpts for all 14 important/decisive leads in compact state.
- Generic routing simulations: tweet, idea, long transcript, scientific report, code/log, explicit fact-check and hostile source text all route without a corruption-specific KERNEL contract.

These are deterministic contract and state simulations executed by the current system. They are strong anti-regression evidence, not a mathematical proof that every probabilistic LLM/tool combination will comply on every run.

## Preserved

- One investigation Markdown, one path, no article or PART output.
- Cumulative compact OPEN checkpoints and same-run RESUME.
- Historical phase IDs `0→19a`, gate IDs `G0→G10`, fact ontology and all existing tool aliases. `@READ_SRC` is the only added alias and is restricted to current-user-authorized source paths.
- No forced fact, mechanism, amount, responsible person, causal depth or APEX from case count.
- `BENEFIT≠INTENT`, `ROLE≠RESPONSIBILITY`, `ASSOCIATION≠COORDINATION`.

## Parent

Parent archive: `truth-engine-v2.6.zip`
Parent SHA-256: `f16694b4f671a01164f36f4ebcc3462ba2504f209bcf96115d574c160a3de830`

A v2.7 `STATE:OPEN` snapshot is not resumable by v2.6 because INPUT_REF, EVIDENCE_EXCERPT, ROUTES, OBJECT_COVERAGE and axis attempt/result contracts are new canonical state.
