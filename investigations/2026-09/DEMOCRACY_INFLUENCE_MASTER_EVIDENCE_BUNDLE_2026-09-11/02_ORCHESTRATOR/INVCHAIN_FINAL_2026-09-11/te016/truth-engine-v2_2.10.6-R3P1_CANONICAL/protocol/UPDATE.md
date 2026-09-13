# UPDATE v2.10.6 — Differential revalidation

Load only when `INPUT_KIND=UPDATE`. This protocol updates an earlier investigation without treating its conclusions or memory as current evidence.
> UPDATE is entered only when the CURRENT user explicitly requests update/revalidation/continuation. Finding a prior run in MnemoLite does not change INPUT_KIND.

Preserve the parent `OBJECT_QUESTION`, OBJECT_COVERAGE and material LED/AXS coverage unless the current user changes scope. `MISSION_MODE` always comes from the current request; parent mode is metadata only. Reopen parent INPUT_REF when material; otherwise use persisted excerpts and type missing context ACCESS. If a legacy parent lacks these fields, treat its question/conclusions as leads and re-scope; NEVER infer `VERIFY_ONLY`. Updating a source claim never replaces the underlying object with a bounded fact-check.

## §1 Inputs and lineage

```text
PARENT_RUN_ID:{resolved id|UNKNOWN}
PARENT_AS_OF:{date|UNKNOWN}
CURRENT_AS_OF:{date}
PARENT_SCOPE:{question,period,geo,domains}
UPDATE_REQUEST:{explicit requested change|general revalidation}
```

- Resolve the parent run/file/memory when available; never invent lineage.
- Parent facts, sources and conclusions are leads until reopened against their exact evidence object.
- Preserve stable parent IDs when the bounded proposition/object is unchanged. New items receive the next free ID.
- Material scope change triggers normal KERNEL re-scoping and complexity recomputation; it does not silently masquerade as a small update.

## §2 Revalidation route

At warm hydration, first classify each remembered/current material object for execution:

```text
REUSE | RECHECK | NEW | GAP
```

This is a work-allocation class only. UPDATE semantic outcome still uses:

```text
UNCHANGED | NEW | UPDATED | DOWNGRADED | REFUTED | EXPIRED | OUT_OF_SCOPE
```

Classify volatility only to allocate work:

```text
STABLE    = underlying object/status rarely changes
EVOLVING  = periodic or event-driven change is plausible
REALTIME  = value/status can change continuously or within days
```

Rules:

1. Reopen every decisive parent source and every EVOLVING/REALTIME item in scope.
2. Reopen a stable contextual item only if a changed claim, contradiction or dependency affects it.
3. Search for material evidence published since `PARENT_AS_OF`, plus known corrections/retractions/version changes.
4. Recompute affected claim statuses, causal links, impacts, responsibility and EDI.
5. Recompute affected LED/AXS routes and resource/network/control maps; a changed lead can reopen the object investigation.
6. Propagate changes through actual IDs; do not rerun unrelated branches merely for completeness.
7. `NO_MATERIAL_DELTA` is a valid result when revalidation supports it and remaining limits are explicit.

## §3 Delta output

Include in the rebuilt FINAL investigation without changing its core section count:

```text
DELTA_REPORT
| ID | CLASS | PARENT VALUE/STATUS | CURRENT VALUE/STATUS | EVIDENCE | DOWNSTREAM IMPACT |

AFFECTED_IDS:{LED/AXS/CLM/FCT/SRC/CAU/CTRL/ACT list}
UNCHANGED_IDS:{material IDs checked and unchanged}
NOT_REOPENED:{IDs + bounded reason}
NEW_GAPS:{GAP_TYPE:list}
```

Every changed status appears in `STATUS_DELTA`; every new/unresolved material conflict appears in `CONTRADICTION_LEDGER`.

## §4 Persistence

- Generate a new RUN_ID and set PARENT_RUN_ID; never overwrite the parent investigation file.
- Attempt `@MNEMO_S` for the new investigation. Duplicate warning follows the KERNEL update rule.
- FACT_WRITEBACK includes only current, reopened and revalidated `EPI=FACT` rows: `✦`→`status:CONFIRME`, `✧`→`status:VERIFIE`; expired, refuted, non-FACT or merely inherited parent facts are not written as verified.
- Persistence follows KERNEL strictly: PRE_GATE §19a before any new Mnemo/writeback side effect, then §19b writeback/rebind/delivery gate.

_Canonical authority: UPDATE lineage, differential revalidation and DELTA_REPORT._
