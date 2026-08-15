# Truth Engine v2.5 — Cumulative checkpoint release

## Intent

Prevent loss of material investigation state when a long run exhausts or loses its LLM context. v2.5 externalizes compact canonical state without creating multiple investigation outputs.

Parent archive: `truth-engine-v2.4.zip`
Parent SHA-256: `6cf588242ddd2eb2df1a02a98198dfea602b6f95fad0d95f0074d38e378189ad`

## Preserved

- One investigation path and one delivered Markdown.
- Exactly one `STATE:FINAL` write.
- Existing `@READ/@WEB/@FETCH/@EXA/@MNEMO_*/@WRITE` aliases unchanged.
- Historical phases `0→19a`, gate IDs `G0→G10`, ontology, scores, statuses and registries.
- No article, PART1/PART2, split or checkpoint sidecar.
- Final section counts, MnemoLite behavior, FACT_WRITEBACK and rollback semantics.

## Changed

| Contract | v2.4 limitation | v2.5 behavior |
|---|---|---|
| Persistence | state remained in context until step 19 | compact mandatory `STATE:OPEN` snapshots overwrite the same path |
| Recovery | no same-run restart | RESUME validates an OPEN snapshot, keeps RUN_ID and continues exact NEXT_ACTION |
| Path | resolved at finalization | resolved once at step 0; reused for every checkpoint and FINAL |
| Progress | no durable cursor | CHECKPOINT_SEQ (successful OPEN writes only), LAST_COMPLETED, NEXT_ACTION and RESUME_COUNT |
| Context safety | raw tool output could disappear before final save | material results must be normalized before a successful checkpoint |
| Search | no mid-run persistence | checkpoint after each decisive claim batch and before material branch/correction switches |
| Module state | LOADED_MODULES could be mistaken for live context | RESUME reloads scheduled and still-applicable modules |
| Request log | owner loaded at step 14 | loaded at step 0; prior checkpoint outcomes are reconciled without self-claiming success |
| Failure | only final write failure was specified | one identical retry for transient/unknown checkpoint failure, then block; FINAL failure never claims persistence |
| UPDATE output | “append” could be read as a file operation | DELTA_REPORT is included in the rebuilt FINAL; the file is never appended |

## Snapshot boundaries

- Step 7: scope, claims and research plan.
- Step 9: each decisive claim batch and material partial branch state.
- Step 10: evidence and fact registries.
- Step 11: each completed material causal tree.
- Step 13: verification, contradictions and trace.
- Step 17: EDI and responsibility state.
- Step 19: one FINAL investigation overwrite.

Snapshots contain canonical registries, gaps, next queries and compact trace only. They never append a previous snapshot, persist a narrative draft, dump raw pages or replace final source reopening.

The existing `write` alias exposes no atomic-replace guarantee. v2.5 protects against LLM context loss; it cannot guarantee crash consistency if the host fails during a write. Solving that would require a verified atomic rename/replace primitive and is intentionally not invented here.

## Modified files

- `KERNEL.md`
- `forensic/GATES.md`
- `forensic/REQUEST_LOG.md`
- `protocol/INVESTIGATION.md`
- `protocol/UPDATE.md`
- `output/TEMPLATE.md`
- `tools/DSL.md`
- `tools/MACROS.md`
- `CHANGELOG_V2.5.md`

## Rollback

Rollback is the parent v2.4 archive identified above. A v2.5 `STATE:OPEN` snapshot is not resumable by v2.4; preserve or finalize it before rollback.
