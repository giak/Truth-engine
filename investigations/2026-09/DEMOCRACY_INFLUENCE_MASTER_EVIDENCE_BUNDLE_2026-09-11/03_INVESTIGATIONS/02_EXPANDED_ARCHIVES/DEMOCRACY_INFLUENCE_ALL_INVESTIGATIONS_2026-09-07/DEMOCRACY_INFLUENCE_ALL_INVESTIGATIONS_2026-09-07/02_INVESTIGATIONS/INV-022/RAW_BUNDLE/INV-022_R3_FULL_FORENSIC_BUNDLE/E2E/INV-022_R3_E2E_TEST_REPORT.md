---
artifact: truth-engine-r3-e2e-test-report
investigation_id: INV-022
run_id: 20260906-1057-russie-operations-influence-france
engine: "2.10.6"
bundle_revision: R3
state: FINAL
delivery_certified: true
as_of: "2026-09-06"
library_modified: false
---

<!-- TRACE: real fresh investigation executed end-to-end with canonical R3 bundle; no R3 code patch applied during run -->

# INV-022 — R3 end-to-end test report

## Result

```text
FINAL               PASS
RUN_STATE validate  PASS
PRE kernel gate     PASS under Europe/Paris process timezone
DELIVERY gate       PASS
CERTIFICATION       PASS / archived
DELIVERY SHA256      a5d3c37a2dec09a07a0d2ec2ab00be4fd794b814729a1c749032cdab07ff806e
```

## Final run counts

```text
QRY   69  (WEB 49 | FETCH 20 | EXA 0)
SRC   20  | provenance families 9
FCT   26  | 2 tier ✦ with explicit refutation searches
LED    8
CLM    8
AXS    9  | all SATURATED with non-empty attempt_ids + result_ids
CAU    6
CTRL   3
ACT    5
CP     7
```

## Investigation result boundary

The corpus supports repeated and adaptive Russia-linked operations materially targeting France, documented infrastructure/actor relations for several branches, measurable workload/enforcement effects, and heterogeneous exposure. It does **not** establish a causal effect on French opinion, behavior or an electoral result.

Material gaps preserved include:

- longitudinal France-specific Portal Kombat audience;
- causal persuasion/behavior/electoral effects;
- independent public reproduction of the GRU 29155 → Storm-1516 attribution bridge;
- aggregate deterrent effect of takedowns;
- incomplete public network topology.

## R3 behavior validated

- all accepted SRC rows preserve canonical id, dates, locator, URL, role and family;
- terminal AXS rows require real attempts and results;
- analytical sections are deterministically rendered as Markdown;
- no JSON fence exists in the technical body or forensic Markdown projection;
- JSON remains only as compact inline payloads in runtime-owned machine registries;
- TRACE_MATRIX_V1 covers LED/AXS/CLM;
- MODULE_EXECUTION covers all eight conditional modules;
- EDI_REPORT is structured and rendered, with `diagnostic_not_truth=true`;
- MnemoLite unavailability produces explicit terminal blocks rather than invented memory ids;
- final certificate SHA equals the actual delivered investigation SHA.

## End-to-end defects exposed

### E2E-001 — Git prerequisite contradicts KERNEL contract

First PRE attempt from the clean extracted canonical ZIP:

```text
git: BLOCKED — pas de dépôt git ou aucun commit
all 24 kernel-specific checks: PASS
```

KERNEL phase 19a explicitly says Git branch state MUST NOT be a certification/blocking criterion. No R3 code was patched during the run. A disposable Git repository with one empty commit was created only around the test copy to continue the remaining E2E path.

**Classification:** runtime/verifier environment-contract defect; not an investigation-data defect.

### E2E-002 — Gate timestamp implicitly depends on process timezone

With the disposable Git repository but default UTC process timezone, PRE failed only on:

```text
gate:horodatage FAIL
filename: 2026-09-06_10-57_...
process now: 2026-09-06 09:58 UTC
```

The run filename uses Europe/Paris local time. Re-running the exact same gate with:

```text
TZ=Europe/Paris
```

passed without changing any Truth Engine or investigation content.

**Classification:** verifier timezone/environment defect; not an investigation-data defect.

## Persistence degraded mode

MnemoLite was unavailable from the beginning of the run and remained in `DEGRADED_FLAGS`.

```text
eligible FACT writebacks: 19
attempted: 0
success: 0
failure: 0
blocked: 19
reason: MNEMO_UNAVAILABLE
```

This is a valid terminal R3 persistence state. No memory id was fabricated. The local `_MNEMO_SNAPSHOT.json` was exported successfully.

## Final six-file topology

```text
_INPUT.txt
_RUN_STATE.json
_NARRATIVE.tmp.md
_INVESTIGATION.md
_MNEMO_SNAPSHOT.json
_CERTIFICATION.json
```

No additional pipeline file was introduced inside the run directory.

## SHA256

```text
CERTIFICATION  1849eb3855b4b4ee51ce00d865617942beb0cd8088154f7bf95d177589668df9
INPUT          b4582f7330c39e3a47f6aa7512bfb623ddea7e7e3dd046421e246631a29e05f4
INVESTIGATION  a5d3c37a2dec09a07a0d2ec2ab00be4fd794b814729a1c749032cdab07ff806e
SNAPSHOT       ccadef83af9d6f2dba278bf6f302984705f9a9f3eb9c1855e7299a8f7de8223e
NARRATIVE      79295880570f35fce78ab687b34d0604c56cb8ace01d17cd9a8fcc666cf52766
RUN_STATE      b639fb372d9599c675dbb4e2821fa3c6e66573be303f66297935db385e17662e
```

## Verdict

```text
INVESTIGATION EXECUTION       PASS
R3 FORENSIC CONTRACT          PASS on this run
PRE/DELIVERY KERNEL CHECKS    PASS after environment normalization
FULL E2E AS-SHIPPED ZIP       NOT CLEAN: E2E-001 + E2E-002
LIBRARY R3 CODE MODIFIED      NO
```

The correct next step is to review the produced `_INVESTIGATION.md` and this report before deciding whether to patch R3.
