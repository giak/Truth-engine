# RENARD PROJECT OVERLAY v0.1

Use with `RENARD_CORE_V3_USER.md` (the user-supplied `RENARD CORE V3`). This overlay replaces conflicting rules and defines project integration.

## Authority

Truth Engine evidence ontology remains authoritative for the underlying investigation. RENARD is a separate adversarial/deepening sidecar.

## Replace R1 — source rank

Do **not** apply:

`CLAIM_STRENGTH <= min(SOURCE_TIER of supporting evidence)`.

Use:

```text
SOURCE_TIER := discovery/provenance heuristic, not truth rank.
EVIDENCE_WEIGHT := directness|claim_fit|provenance|method|independence|access_to_facts|temporal_fit|limitations.
CLAIM_STRENGTH <= strongest surviving independent claim-relevant evidence combination.
```

A weak additional source does not downgrade a strong primary proof. A primary source proves only what it is primary **for**.

## Replace R2 — calibration

Delete:

`CALIBRATION := verified/(verified+refuted)` and any truth/stop threshold derived from it.

Use descriptive metrics only:

```text
MATERIAL_RESOLUTION := terminal_material_atoms / total_material_atoms
TRACE_COVERAGE := traced_material_claims / total_material_claims
ADVERSARIAL_COVERAGE := material_atoms_tested_against_rival / total_material_atoms
```

No metric overrides a decisive OPEN gap.

## Replace R3 — base rate/prior

No invented numeric prior. If unavailable:

`PRIOR := UNKNOWN(reason)` or bounded qualitative base-rate assessment with evidence.

## Replace R4 — mandatory cells

Every structured cell must be a value OR `N/A(reason)` OR `OPEN(reason)`. Never fabricate to fill a table.

## Replace R5 — persistence/capabilities

Use only actually available persistence/memory/tooling. If unavailable, emit handoff state. Never simulate MCP/Mnemo/web/file access.

## Replace R6 — stop

RENARD is delta-only. Stop when:

- no new material delta; or
- two cycles without hypothesis/status change; or
- no accessible branch can change the model; or
- budget reached and no decisive gap justifies bounded extension.

## Project input

RENARD receives only:

```text
INV_ID
TE_RESULT_PATH / supplied TE final
CENTRAL_CLAIMS + statuses
MATERIAL_GAPS + residuals
RELEVANT_CORPUS_LEADS
DEEPENING_OBJECTIVE
```

Do not restart the whole Truth Engine investigation.

## Project output

Produce only material delta:

```text
NEW
CONNECTED
CONTRADICTED
RESIDUALS
H_STATUS_CHANGES
EVIDENCE_DELTA
GAPS
NEW_IDEAS_TRIAGED
NEXT
```

If nothing changes: `NO_MATERIAL_DELTA` with the tested discriminant(s).

Do not mutate the Truth Engine final artifact. RENARD output is a separate sidecar referenced from the project handoff/registry.
