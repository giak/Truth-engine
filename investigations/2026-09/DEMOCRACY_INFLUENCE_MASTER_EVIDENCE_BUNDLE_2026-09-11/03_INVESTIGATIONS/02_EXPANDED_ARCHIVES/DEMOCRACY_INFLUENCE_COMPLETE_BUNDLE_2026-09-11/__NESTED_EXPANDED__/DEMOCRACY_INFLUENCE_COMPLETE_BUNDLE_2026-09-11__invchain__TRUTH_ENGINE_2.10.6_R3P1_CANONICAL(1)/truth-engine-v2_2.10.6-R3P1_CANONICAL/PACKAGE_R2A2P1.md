# Truth Engine 2.10.6 / R2A.2 — package revision P1

Package-only hygiene correction. No KERNEL, investigative semantics, runtime persistence rule, source tier, cluster, gate or output contract changed.

## Changes
- removed generated `.pytest_cache/` and `__pycache__/`;
- removed run-specific `inv010_narrative_source.md`;
- removed tests for production components explicitly external to this drop-in; their supplied originals remain archived;
- retained `tests/test_verify_gate.py`;
- release test command now covers extractors + runtime + verifier.

## External-by-design
`tools/verify_facts.py`, `tools/detect_contradictions.py`, `tools/monitor_urls.py`, `tools/classify_legacy.py`, `tools/lint_search_mode.py`, and the full legacy Sublimator v35 tree remain external and are not reimplemented.
