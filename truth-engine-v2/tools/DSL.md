# COGNITIVE DSL v2.1 — Reference aliases

This card compresses references; it defines no ontology, threshold, formula or gate.

## §1 Knowledge-base aliases

```text
@KB[KERNEL] → KERNEL.md
@KB[SYM]    → definitions/SYMBOLS.md
@KB[PAT]    → definitions/PATTERNS.md
@KB[THR]    → definitions/THREATS.md
@KB[INV]    → protocol/INVESTIGATION.md
@KB[PERSO]  → protocol/PERSO_FRESQUE.md
@KB[EPI]    → search/EPISTEMIC.md
@KB[QRY]    → search/TEMPLATES.md
@KB[OPT]    → search/OPTIMIZATION.md
@KB[GATE]   → forensic/GATES.md
@KB[FORENSIC]→ forensic/REASONING.md
@KB[LOG]    → forensic/REQUEST_LOG.md
@KB[OUT]    → output/TEMPLATE.md
@KB[MACRO]  → tools/MACROS.md
```

Legacy aliases: `@KB[DSL]→this`, `@KB[SEARCH]→@KB[EPI]`, `SEARCH_EPISTEMIC.md→search/EPISTEMIC.md`.

## §2 Operational aliases

```text
@A[MEANING]   → SYMBOLS §1
@A[EPISTEMIC] → SYMBOLS §2
@ROUTE[x]     → SYMBOLS §4
@PAT[x]       → PATTERNS
@THR[x]       → THREATS
@HERM[text]   → INVESTIGATION §1 L1-L6
@PRISM[3P]    → INVESTIGATION §2
@FACT[x]      → SYMBOLS §2 status + INVESTIGATION §3 registry
@PELOTE[x]    → INVESTIGATION §4
@VERIFY[x]    → INVESTIGATION §5
@WOLF[x]      → INVESTIGATION §6 responsibility map
@EDI[x]       → EPISTEMIC §3
@QRY[x]       → TEMPLATES; OPTIMIZATION only on failure/noise
@GAP[x]       → ⁅ UNKNOWN; stop inference; state missing evidence
@SAVE[x]      → KERNEL step 19/19a
```

## §3 Reasoning syntax

```text
L1 EXPLICIT → L2 IMPLICIT → L3 STRUCTURAL → L4 SYMBOLIC → L5 PRESUPPOSED → L6 EPISTEMIC
P1 DOMINANT | P2 STRONGEST_CRITICAL | P3 EVIDENCE_ARBITRATION
LINK ∈ {CAUSE,ENABLER,PRECEDENT,CONTEXT,UNKNOWN}
INTENT ∈ {PROVEN,CLAIMED,UNKNOWN}
OPS: → ← ∧ ∨ ¬ | ≥ ≤ > < = ≈ ± | ⊕ ⊗ ⊙ ≋
```

## §4 Compatibility names

```text
$IC=ICEBERG | $FA=FASC/CONVERGENCE | $DD=DEEP_DIVE | $AS=ASTRO
$GS=GASLIGHT | $CW=COGNITIVE_WAR | $NW=NETWORK | $TM=TEMPORAL | $MT=MONEY | $BIO=BIO
@INV[CASCADE] = network→operations→temporal→claims, with every link verified
@MODE[DEEP]/@MODE[APEX] = KERNEL complexity depth; never forced findings
```

_Canonical authority remains in the referenced files._
