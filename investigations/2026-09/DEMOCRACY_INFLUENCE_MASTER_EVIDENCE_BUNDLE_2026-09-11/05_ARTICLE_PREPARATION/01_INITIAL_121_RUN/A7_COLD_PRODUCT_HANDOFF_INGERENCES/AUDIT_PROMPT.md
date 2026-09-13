# A7-S04 — COLD PRODUCT AUDIT

You are auditing a **final article product about influence and interference**, not the protocol implementation that produced it.

## Cold-start order

1. Read `ARTICLE_PUBLICATION_VIEW.md` **alone**.
2. Write a provisional product verdict before reading anything else.
3. Read `FOUNDATION/VISION.md` and `FOUNDATION/PFD.md`.
4. Re-audit the article against the intended product mission and acceptance criteria.
5. Fact-check material claims using the article's own footnotes and `SOURCE_INDEX.tsv`.
   - If you have web access, verify the public sources yourself.
   - If you do not have web access, mark unverifiable points `NON_PROUVÉ` rather than guessing.
6. Produce the final audit.

Do not ask for, infer, or reward implementation history, runtime gates, trace graphs, repair logs, protocol files, hashes, internal reviews or previous audit verdicts. They are intentionally absent.

## Primary question

Does this article, as a standalone publication:

- let a cold reader understand the real object rather than only a methodological slogan;
- preserve investigation-specific mechanisms, corrections, counterexamples and negative knowledge;
- keep operation, attribution, exposure, persuasion, behavior and outcome correctly separated;
- keep resource/capacity distinct from tasking/command;
- represent both real foreign operations and the critique of counter-interference institutions without caricature;
- distinguish legal-design asymmetry from an unproven systematic geopolitical double standard;
- remain auditable from its public sources;
- state what was learned, what it changes, how far it can be asserted, and what remains open;
- read as an article rather than as a protocol report?

An exact and sourced article that collapses into a generic “correlation is not causation” essay must FAIL the product-value test.

## Mandatory adversarial tests

### T1 — Object depth
Could a reader leave believing that the subject is merely “effects are hard to prove”, while losing the article's positive model of upstream power through resources, access, gates, law, visibility and constraint?

### T2 — Forensic yield
List the investigation-specific discoveries, corrections, refutations, mechanisms, actors, flows and negative results that materially survive in the article. Then ask whether almost the same article could be written from a handful of superficial web searches.

### T3 — Causality and responsibility
Search for silent upgrades:
`relation -> causality`,
`funding -> command`,
`operator -> principal`,
`access -> capture`,
`exposure -> persuasion`,
`persuasion -> vote`,
`local cases -> systemic prevalence`.

### T4 — Strongest counter-theses
State both strongest good-faith counter-theses:
1. a pluralist view in which multiple institutions, courts and organizations constrain one another sufficiently that systemic-power language overstates the evidence;
2. an integrated-power view in which repeated resource/access asymmetries and institutional convergence are evidence of deeper coordination than the article concedes.
Does the article represent and bound both fairly?

### T5 — Factual/source support
For every material number, legal statement, organizational relation and current-state claim:
- identify the supporting footnote/source;
- determine whether it supports the exact scope;
- identify stale, indirect, commercial or ambiguous support.

### T6 — Negative knowledge
Check that `not established`, `not found`, `unknown`, `case-specific`, `partial` and `not measured` are not converted into absence or certainty.

### T7 — Corrections
Audit especially:
- Rokh Solis / the correction of “never allies”;
- legal-design asymmetry vs systematic enforcement bias;
- expansion of counter-interference institutions vs fabrication/exaggeration of threat.

### T8 — Reader autonomy
Can a cold reader understand the article without knowing the 121 dossiers or the workflow?

### T9 — Editorial product
Is the article publishable as an article? Identify density, repetition, jargon or process residue only when they materially harm comprehension.

### T10 — Conclusion
Does the conclusion:
1. say what is understood better;
2. say what changes;
3. bound the claim;
4. preserve materially open questions?

## Severity

- `P0`: error/failure invalidating a material part of reasoning or product.
- `P1`: serious defect to repair before publication/canonicalization review.
- `P2`: desirable non-blocking improvement.
- `ROBUSTE`: element that survives contradiction.
- `NON_PROUVÉ`: cannot be verified from available evidence.

For every P0/P1 provide:

```text
ID
SEVERITY
ARTICLE LOCATION
CLAIM / FAILURE MODE
EVIDENCE
WHY MATERIAL
MINIMAL REPAIR
WHAT MUST NOT CHANGE
```

No global rewrite when a local repair suffices.

## Required final matrix

| Dimension | Verdict | P0 | P1 | Main residual risk |
|---|---|---:|---:|---|
| Object depth | | | | |
| Factual fidelity | | | | |
| Causality/calibration | | | | |
| Actors/flows/mechanisms | | | | |
| Counter-theses | | | | |
| Negative knowledge | | | | |
| Investigation yield | | | | |
| Genericity | | | | |
| Source auditability | | | | |
| Reader autonomy | | | | |
| Conclusion | | | | |
| Editorial publishability | | | | |

## Terminal decision

Return exactly one:

```text
FAIL_P0
REPAIR_P1
PASS_WITH_P2
PASS_CLEAN
```

Then:

```text
P0 OPEN = N
P1 OPEN = N
P2 OPEN = N

A7-S04 COLD PRODUCT GATE = PASS / FAIL
FINAL CANONICALIZATION REVIEW AUTHORIZED = YES / NO
```

Important: `PASS` concerns the **product only**. It does not itself canonicalize any protocol.
