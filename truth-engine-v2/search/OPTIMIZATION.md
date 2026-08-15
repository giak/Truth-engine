# QUERY OPTIMIZATION v2.8 — Failure/noise recovery

Load only when a query is empty, noisy, blocked or overbroad. No productivity claim is assumed; use actual REQUEST_LOG results.

## §1 Simplify (`SPLIT_QUERY`)

For a query with several entities/concepts/clauses:

1. Keep one named entity or exact phrase.
2. Add one evidence object/action.
3. Add one date, jurisdiction or file type only if discriminating.
4. Create at most three independent queries; do not split Boolean synonyms into combinatorial spam.

```text
A = {entity} {object/action}
B = "{exact phrase}" {date/source}
C = {entity variant/native name} {repository term}
```

## §2 Execute (`EXECUTE_QUERIES_OPTIMIZED`)

```text
for each deduplicated query:
  @WEB → inspect relevance
  if useful URL → @FETCH exact page/document
  if empty/noisy → one reformulation (synonym, native name, shorter query, site/filetype)
  if still empty → mark persistent GAP
after reasonable @WEB/@FETCH routes, @EXA may be used once as last resort
Exa 429 → disable Exa for run; never retry it
```

Do not call `@FETCH` without a known URL. Do not replace a failed query with an unsourced model-memory answer.

## §3 Blocked/inaccessible sources (`HYBRID_FALLBACK`)

Try, in order: canonical alternate URL/version → archive or repository copy → quoted identifier/title search → independent source that links/embeds the object. Record that a mirror is a mirror and preserve provenance. If content cannot be inspected, it cannot support `✦`.

## §4 Result selection

- Prefer exact object and relevant section over domain authority.
- Keep one row per material evidence object; collapse syndication.
- Reject title-only match, wrong namesake/date/jurisdiction, navigation page and circular citation.
- Reallocate remaining budget to unresolved material LED/CLM/AXS routes, not saturated branches. Failed reformulations remain distinct QRY ATTEMPT_IDS with observed perimeter; a saturated lead audit does not cancel unresolved object axes.

## §5 Diagnostics

```text
[QUERY_OPTIMIZATION]
original:{n} split:{n} reformulated:{n} fetched:{n}
useful_objects:{n} duplicates:{n} failures:{n} persistent_gaps:{list}
Exa:{unused|used|disabled_429}
```

_Canonical authority: search failure/noise recovery._
