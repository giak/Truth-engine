# TRUTH ENGINE — GATES v2.1

Loaded at phase 0; executed at steps 18/18b. Gates protect evidence integrity. Targets guide effort but never force findings.

## §1 Runtime rules

1. **Fallback:** failed/noisy query → simplify/reformulate once with `@WEB`; use `@FETCH` for a known result URL. Exa 429 disables Exa for the run. Log failures; do not fabricate replacement results.
2. **Symmetry:** every significant claim receives strongest evidence-consistent support, credible counter and explicit missing check. Equal scrutiny does not mean equal proof.
3. **Traceability:** every supported fact points to the specific source used. Search pages/snippets are discovery traces, not confirmation.
4. **No quota truth:** query, source, fact, chain and EDI targets may trigger more work while a material gap remains; saturation or unavailable evidence yields an explicit limitation.
5. **Stop inference:** unsupported step → `⁅ UNKNOWN/GAP`; never bridge it for narrative completeness.

## §2 Critical gates

| Gate | Pass condition | On failure |
|---|---|---|
| G0 Analysis | MANIPULATION_REPORT exists; 15 symbols assessed; none `✗` | return step 0 |
| G1 Scope | central question, period, geography and exclusions explicit | return step 7 |
| G2 Claims | all material claims registered with support/counter/gap | return step 5 |
| G3 Facts | factual work has FACT_REGISTRY; each row has canonical status | return step 10 |
| G4 Confirmation | every `✦` has specific claim-relevant evidence and URL | downgrade or return step 9/10 |
| G5 Causality | every CAUSE/ENABLER is sourced; chronology is not relabeled cause | downgrade link or return step 11 |
| G6 Responsibility | every named individual has sourced action and bounded responsibility; intent typed | remove/downgrade or return step 17 |
| G7 Contradiction | material conflict is represented, not hidden | return step 13 |
| G8 Output | required sections and REQUEST_LOG exist; unknowns are explicit | return step 14 |
| G9 Serialization | complete string + resolved safe path before any write; no invented success | stop before step 19 |

MnemoLite unavailability is degraded mode, not a blocker, unless the investigation explicitly depends on inaccessible prior state.

## §3 Advisory gap severity

```text
edi_gap   = max(0, EDI_target-EDI_actual) / max(EDI_target,0.01)
query_gap = max(0, query_target-query_actual) / max(query_target,1)
coverage_gap = unmet_applicable_targets / applicable_targets
cx = SIMPLE:.50 | MEDIUM:.70 | COMPLEX:.85 | APEX:1.00
GAP_SEVERITY = clamp(mean(edi_gap,query_gap,coverage_gap) × cx, 0, 1)

<.20 proceed + disclose | .20–.49 one targeted correction loop
≥.50 draft/inconclusive unless bounded correction can resolve a material gap
```

This score measures process coverage, not truth. It cannot override a critical gate or upgrade evidence.

## §4 Bounded corrections

| Gap | Correction | Limit |
|---|---|---:|
| decisive claim weak | targeted primary/counter-evidence queries | 2 loops |
| source circularity | locate independent provenance or original object | 1 loop |
| missing/indirect URL | fetch exact document/page; otherwise downgrade | 2 attempts |
| unexplained causal link | search direct enabler; otherwise type PRECEDENT/CONTEXT/UNKNOWN | 2 attempts |
| one-sided corpus | strongest credible underrepresented perspective | 1 loop |
| failed query | simplify, localize or use known URL | 1 reformulation |
| output/log omission | repair from actual runtime record only | 1 loop |

After the limit, preserve the gap. Do not keep searching to satisfy a number.

## §5 Pre-delivery checklist

```text
□ G0–G9 pass or non-applicable reason is explicit
□ 15 narrative symbols assessed from observations
□ Loaded clusters exactly match SYMBOLS.md §4
□ Claims have support, credible counter or NONE_FOUND, and GAP
□ FACT_REGISTRY uses canonical statuses; every ✦ has specific evidence/URL
□ Memory-derived leads were revalidated before decisive use
□ Causal links are typed; no forced depth/convergence
□ Impact entries are evidenced or NONE ESTABLISHED/NOT APPLICABLE
□ Responsibility map contains no unsupported person/intent
□ EDI reports applicable dimensions, penalties and limitations
□ REQUEST_LOG contains actual material calls; serialization-pending rows are honest
□ Investigation/article preserve epistemic status and contradictions
```

Proceed to step 19 only when critical gates pass. Advisory gaps remain visible in `PÉRIMÈTRE & LIMITES`.

_Canonical authority: integrity gates and bounded correction._
