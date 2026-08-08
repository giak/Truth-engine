# INVESTIGATION v2.1 — Evidence construction pipeline

Loaded at KERNEL step 8b. KERNEL owns order/load/save; this file owns cognitive, dialectical, factual, causal, verification and responsibility operations.

## §0 Data contracts

```text
SCOPING_REPORT:
  QUESTION | PERIOD | GEO | DOMAINS | ACTORS/INSTITUTIONS | EXCLUSIONS | EVIDENCE_LIMITS

CLAIM_REGISTRY:
  ID | CLAIM | CLAIMANT | MATERIALITY | SUPPORT | COUNTER/NONE_FOUND | GAP | STATUS

COGNITIVE_MAP:
  CLUSTER_SCORES | HERMENEUTIC L1-L6 | FORENSIC(if Ξ≥5) | ALTERNATIVES | QUERY_GUIDANCE

DIALECTICAL_MAP:
  P1_DOMINANT | P2_CRITICAL | P3_EVIDENCE_ARBITRATION | TENSIONS | SILENCES | IMPACT

FACT_REGISTRY:
  | # | Fait | Date | Acteur | Chiffre | Source | URL | Fiabilité |
  Fiabilité = source role + fact status + corroboration, e.g. `◈ ✦ ⊕`.
```

Use canonical meanings from `definitions/SYMBOLS.md`. A registry row is a bounded claim, not a paragraph mixing statuses.

## §1 Cognitive analysis

### 1. Cluster review

For each loaded cluster only:

1. Extract quoted/observable indicators from subject text.
2. Apply its formula only with defined inputs; otherwise `NOT COMPUTABLE`.
3. Search the strongest innocent/competing explanation.
4. Record score change, evidence and remaining gap.

Cluster score routes scrutiny. It cannot establish intent, coordination, capture or deception.

### 2. Hermeneutic L1–L6

| Layer | Question | Output discipline |
|---|---|---|
| L1 Explicit | What is literally asserted? | quote/bounded paraphrase |
| L2 Implicit | What must be assumed or is omitted? | label inference |
| L3 Structural | Which frame, categories and incentives organize it? | test alternatives |
| L4 Symbolic | Which images/emotions/codes carry meaning? | separate effect from intent |
| L5 Presupposed | Which worldview or audience knowledge is assumed? | state uncertainty |
| L6 Epistemic | Who can produce, retain, access or contest the evidence? | map data/control gaps |

### 3. Forensic branch

If `Ξ≥5`, execute `forensic/REASONING.md`. Keep `FOUND`, `ESTIMATED` and `UNKNOWN` separate. No hidden-total reconstruction without comparable units and scope.

## §2 Dialectical map

Build three perspectives with equal steelmanning:

1. `P1 ⟐/🎓` — strongest dominant/institutional account.
2. `P2 ⟐̅/🔥` — strongest credible critical/adversarial account.
3. `P3 ◈◉○` — evidence arbitration claim by claim.

For each: claims, actors, interests, best evidence, falsifier and silences. Equal argumentative force does not equal equal evidentiary weight. If no credible counter-source is found, write `NONE_FOUND` and preserve the strongest counter-argument; never invent a source or false balance.

Output:

```text
SCENARIO_A | SCENARIO_B | CONVERGENCES | DIVERGENCES | UNRESOLVED | SHARED_SILENCES
ARBITRATION: claim→support→counter→status→next check
```

## §3 Search and factual construction

### Search transformation

- Convert each CLAIM_REGISTRY gap and CRÉDO question into the shortest query that can locate an evidence object.
- Search original language/name variants, primary repositories and credible counterevidence.
- Open the exact document/page; a result snippet is not evidence.
- Track upstream provenance. Syndicated copies or analyses using one source are one evidence family.
- Use query budgets as targets; stop on saturation, not on a cosmetically complete count.

### FACT_REGISTRY

For each material result:

1. State one falsifiable fact with scope.
2. Extract what/who/when/where/how much.
3. Assign source role `◈◉○` for that fact.
4. Assign exactly one canonical status `✦✧⁕⁂⊗⊙⁅❧`.
5. Record specific URL and independent corroboration `⊕` when present.
6. Preserve contradiction as a separate row or linked note; never average incompatible claims.

```text
KNOWLEDGE_STATE:
KNOWN       = current ✦ within stated scope
PROBABLE    = ✧
CLAIMED     = ⁕
HYPOTHESES  = ⁂
CONTESTED   = ⊗/⊙
UNKNOWN     = ⁅
REFUTED     = ❧
```

Targets for confirmed facts guide effort only. Fewer facts with honest limitations beat upgraded weak evidence.

## §4 PELOTE — causal tracing

Run only when the question is causal or an explanatory chain materially affects the conclusion.

### A. Discover candidate mechanisms

Search before naming causes. Adapt these families to the event’s language:

```text
{event} causes/origins/historical roots
{event} institutional or systemic failure
{event} competing explanations
{event} enabling law/institution/material condition
{event} contemporaneous inquiry/commission/archive
```

Fetch the strongest sources and extract candidate mechanisms with provenance. Merge candidates that share the same evidenced trajectory.

### B. Trace each mechanism backward

Start at the nearest evidenced law, decision, institution, material condition or event. At each step:

1. Hypothesize the immediately prior enabler.
2. Search/fetch a specific source; reformulate once if noisy.
3. Classify the link:
   - `CAUSE`: evidence supports production of the outcome.
   - `ENABLER`: made it materially possible/easier but did not determine it.
   - `PRECEDENT`: earlier analogous/legal model; descriptive only.
   - `CONTEXT`: background condition; descriptive only.
   - `UNKNOWN`: proposed link not established.
4. Record source, competing explanation and confidence.
5. Stop at meaningful root, max depth 6 or exhausted evidence. Never insert a node to meet depth.

```text
| FROM | LINK_TYPE | MECHANISM | TO | SOURCE | COUNTER | STATUS |
```

### C. Weave and coverage

- Merge trees only on the same evidenced ancestor; otherwise state independence.
- A sequence or precedent is not silently upgraded to cause.
- For each FACT_REGISTRY row, cite the exact existing node that explains it, or `UNEXPLAINED`.
- At most two focused attempts may fill an important unexplained link; then retain `⁅`.
- Descriptive facts survive a causal gap. The causal conclusion does not.

Output `TIMELINE`, typed `PELOTE_TREES`, `COVERAGE N/N`, competing explanations and gaps. A short verified chain is valid.

## §5 Verification

For every decisive `✦/✧/⊗/⊙`:

1. Reopen the exact source and verify it contains the claimed material.
2. Check date/version, definition, population, jurisdiction and units.
3. Separate source authenticity from the truth of its assertions.
4. Test independence and upstream circularity.
5. Seek the strongest credible disconfirming object or record `NONE_FOUND`.
6. Upgrade/downgrade using SYMBOLS.md only; reasoning coherence cannot upgrade status.

Domain prompts: legal—operative text/jurisdiction; financial—filing/beneficial ownership/accounting period; scientific—design/data/uncertainty/replication; conflict—time/location/provenance/access; humanitarian—definitions/coverage/local testimony; technical—version/configuration/reproduction conditions.

Do not label `COVER-UP` from discrepancy alone. Record the observable event: non-disclosure, deletion, inconsistency, access refusal or verified concealment, with status.

```text
VERIFICATION_REPORT:
REOPENED:{n} | UPGRADED:{ids} | DOWNGRADED:{ids} | CONTRADICTIONS:{ids}
CIRCULAR:{families} | NONE_FOUND:{claims} | REMAINING_GAPS:{list}
```

## §6 Impact and responsibility (`WOLVES`)

Impact map: `QUI GAGNE | QUI PERD | QUI MEURT | QUI RECULE`. For each, identify metric, baseline, period and source. Use `NONE ESTABLISHED` or `NOT APPLICABLE` when warranted; categories may be empty.

Responsibility map includes a person only when a source connects them to a relevant signature, command, vote, decision, implementation, ownership, documented benefit or public claim.

```text
| NAME | ROLE | DOCUMENTED_ACTION | SOURCE | INTENT | RESPONSIBILITY_SCOPE |
INTENT = PROVEN | CLAIMED | UNKNOWN
```

No individual minimum. Do not infer intent from benefit, responsibility from title, guilt from association, or coordination from network proximity.

## §7 Output handoff

At step 14, apply `output/TEMPLATE.md` and `forensic/REQUEST_LOG.md`. Dense French prose; one sentence, one bounded claim; citations adjacent; hypotheses and unknowns visibly labeled. Article post-processing may simplify prose, never epistemic status.

_Canonical authority: investigation operations and intermediate data contracts._
