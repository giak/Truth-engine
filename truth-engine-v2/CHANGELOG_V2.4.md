# Truth Engine v2.4 — Conservative-directive release

## Intent

Preserve the v2.3 investigative behavior and single-file output while restoring an explicit code-like control language. This release changes only demonstrated contract defects and does not remove historical cognitive primitives, heuristics or forensic scaffolding.

Parent archive: `truth-engine-v2.3.zip`
Parent SHA-256: `515bc752bfb37ba8dec7ce4c9e72947c8df493ce8389ef0076170caceda09114`

## KEEP

- Existing tool aliases, `BASE`, `INV` and investigation filename.
- Exactly one investigation and one `@WRITE` attempt.
- Historical phases `0→19a`, including `8b`, `8t` and `18b`.
- All historical glyphs, 15 narrative symbols and canonical fact statuses.
- CRÉDO, PELOTE, EDI, WOLVES, three-perspective dialectic and four complexity levels.
- CLAIM/FACT/EVIDENCE/TRACE/CONTRADICTION/CAUSALITY/RESPONSIBILITY registries and IDs.
- MnemoLite, FACT_WRITEBACK, REQUEST_LOG, lazy loading and bounded corrections.
- Exact output section contracts and explicit `UNKNOWN/INCONCLUSIVE/GAP/NONE ESTABLISHED` outcomes.
- Fenced pseudo-code structure and `text` info strings.

## RESTORE

- Canonical directives: `MUST`, `NEVER`, `IF→`, `ON_FAIL→`, `BLOCK_IF`, `DEGRADE_IF`, `EMIT`, `FREEZE`.
- Explicit auto-execution on usable input.
- Explicit exact-tool and failure semantics.
- Historic forbidden markers `❌` at the prohibition boundary.
- Stable phase/gate slots after removal of non-investigative output: step `15 RESERVED`; existing gates remain `G0…G10`, with serialization at `G10`.

## MODIFY

| Contract | v2.3 issue | v2.4 resolution |
|---|---|---|
| Path | `{sujet}` had no explicit binding | `{sujet}:=SUBJECT_SLUG`; raw input remains forbidden in paths |
| Manifest | fields appeared before resolution | mutable `STATE:OPEN`, finalized and frozen as `STATE:FINAL` at step 18b |
| UPDATE lineage | unresolved parent had no representable final state | transient `PENDING`; final `UNKNOWN` plus access gap when unresolved |
| BIO routing | `♦→BIO.md` used a numeric threshold although ♦ is a factual lens | contextual `PERSON/BIOGRAPHY` trigger; no fabricated ♦ narrative score |
| Module failure | scheduled `@READ` failure unspecified | canonical owner failure blocks; optional helper failure degrades or yields inconclusive |
| Hash | `SHA1_UTF8` was required unconditionally | preflight deterministic capability before manifest freeze; otherwise omit source tag and log `HASH_UNAVAILABLE` |
| Gap severity | zero/N/A denominators ambiguous | calculate from non-N/A components; empty component set returns N/A |
| Serialization | G10 required a resolved safe path but KERNEL did not materialize one before the gate | resolve, validate and freeze the path before G10 |
| Person route | forced APEX obscured score override | preserve APEX route and record `ROUTE_OVERRIDES+=PERSON_APEX` |
| Output trace | route override absent | final manifest and REQUEST_LOG now record route overrides |

## REMOVE

- Dead `$FORMAT` state and unused `$INV_TAGS` alias from KERNEL.
- No cognitive primitive, symbol, heuristic, target, section, registry, memory behavior or investigative phase was removed.
- Article and PART1/PART2 output remain absent, as established in v2.3.

## Modified files

- `KERNEL.md`
- `definitions/SYMBOLS.md`
- `clusters/BIO.md`
- `forensic/GATES.md`
- `forensic/REQUEST_LOG.md`
- `protocol/INVESTIGATION.md`
- `output/TEMPLATE.md`
- `tools/DSL.md`
- `tools/MACROS.md`
- `CHANGELOG_V2.4.md`

## Compatibility and rollback

The directory tree, operational filenames, tool aliases, memory interfaces, phase IDs and evidence IDs remain compatible. v2.4 intentionally changes control salience and repairs the contracts listed above; it is not claimed to be byte-for-byte or behavior-identical.

Rollback is the parent archive identified by the SHA-256 above.
