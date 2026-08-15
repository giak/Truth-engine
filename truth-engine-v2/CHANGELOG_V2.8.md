# Truth Engine v2.8 — Semantic compression release

## Purpose

v2.8 reduces the fixed KERNEL context cost without changing Truth Engine's product, evidence model,
investigation depth, persistence lifecycle or public interfaces. It is a conservative refactor of v2.7,
not a feature release.

## Measured change

| Metric | v2.7 | v2.8 | Change |
|---|---:|---:|---:|
| `KERNEL.md` bytes | 33,256 | 27,931 | -16.01% |
| `KERNEL.md` modern-model tokens (`o200k_base`) | 8,134 | 7,033 | -13.54% |
| `KERNEL.md` lines | 518 | 399 | -22.97% |

The compression is smaller than an aggressive 20–30% rewrite by design. Further deletion would remove
attention-boundary safeguards or replace clear contracts with opaque indirection.

## Semantic core

Repeated prose now resolves to canonical predicates:

`MODE_RULE | INV_FIRST | ADAPT_OK | ROUTE_OK | COVER_OK | NA_OK | GAP_OK | SAT_OK |
TERM_LED | TERM_AXS | STOP_OK | ANCHOR_OK | EXCERPT_OK | TRACE_OK | CP_OK | RESUME_OK | FINAL_OK`

Each critical invariant remains present at definition, action and gate/recency boundaries. Heuristics are
typed separately as `PREFER`, `TARGET` and `BOUND`; none can become a truth or finding quota.

## Preserved interfaces and behavior

- all existing tool aliases and exact call syntax;
- 24 phases `0→19a` and gates `G0→G10`;
- generic inputs and axes;
- `INVESTIGATION` by default and explicit-exclusive `VERIFY_ONLY` only;
- full lead segmentation, object coverage and distinct lead/object search routes;
- auditable `GAP`, `SATURATED`, `N/A`, evidence anchors and trace matrix;
- one cumulative OPEN checkpoint path and exactly one FINAL dossier;
- no article, split output or checkpoint sidecar;
- trust boundary, causal discipline, responsibility safeguards and Mnemo/writeback behavior.

## Resume compatibility

The persisted schema is unchanged. A valid schema-identical v2.7 `STATE:OPEN` snapshot may be resumed:

1. validate its complete v2.7 schema, path, IDs and `NEXT_ACTION`;
2. set `ENGINE_VERSION:=2.8`;
3. add `RESUME_MIGRATION_2_7` to `ROUTE_OVERRIDES` and log the migration;
4. continue at the exact stored action and write the next checkpoint as v2.8.

Other versions remain blocked.

## Cross-file cleanup

- runtime module headers align on v2.8;
- `INVESTIGATION.md` defers terminal-state definitions to the KERNEL semantic core;
- `DSL.md` and `MACROS.md` preserve their public alias names but reference canonical KERNEL predicates instead
  of re-expanding the same contracts.

## Rollback

The untouched v2.7 tree remains the rollback source. A v2.8 OPEN checkpoint should be resumed with v2.8;
v2.7 does not know the explicit migration marker even though the core registries are schema-compatible.
