# Test scope

Canonical drop-in tests cover only components included in this package.

Default/release suite: `python3 -m pytest -q`.
Configured gate suite: `python3 -m pytest tests/extractors/ tests/runtime/ tests/test_verify_gate.py tests/test_verify_forensic_output.py -q`.

R3 adds adversarial coverage for the FINAL forensic output contract:

- SATURATED AXS requires attempts and results;
- terminal CLM requires counter/gap fields;
- SRC rows require complete forensic provenance;
- loaded modules use canonical unique paths;
- SET report sections must be materially projected;
- the technical Markdown body does not replace runtime-owned registries.

Historical tests for external auxiliary tools/full legacy Sublimator remain preserved in the supplied test archive and are intentionally not part of this drop-in.


R3 package P1 adds verifier portability coverage:

- absence of a Git repository is non-blocking and uses a deterministic filesystem STATE_ID fallback;
- `.verify` and transient Python/pytest caches do not perturb the no-Git STATE_ID;
- naive filename timestamps are checked without depending on the process timezone, using the civil UTC+14 upper bound;
- an impossible future timestamp beyond that bound still fails.
