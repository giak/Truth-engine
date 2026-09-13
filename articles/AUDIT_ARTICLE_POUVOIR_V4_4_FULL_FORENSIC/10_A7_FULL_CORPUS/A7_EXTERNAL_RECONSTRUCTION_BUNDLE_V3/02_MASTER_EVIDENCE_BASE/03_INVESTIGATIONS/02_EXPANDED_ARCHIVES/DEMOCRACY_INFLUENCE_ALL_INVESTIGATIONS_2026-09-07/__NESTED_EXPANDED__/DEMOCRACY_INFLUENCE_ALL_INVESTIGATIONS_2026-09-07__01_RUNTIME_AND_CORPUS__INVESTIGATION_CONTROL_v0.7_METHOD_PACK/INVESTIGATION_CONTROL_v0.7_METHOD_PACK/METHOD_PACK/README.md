# METHOD_PACK v0.1

Minimal project layer for the investigation program.

## Files

- `METHOD_PACK.md` — canonical project contract.
- `RUN_CARD_TEMPLATE.md` — prompt/input card for one Truth Engine run.
- `RUN_HANDOFF_TEMPLATE.md` — cross-run sidecar after Truth Engine FINAL.
- `RENARD_CORE_V3_USER.md` — user-supplied RENARD CORE V3, preserved as the reference prompt.
- `RENARD_PROJECT_OVERLAY.md` — mandatory project corrections/integration applied over that reference.
- `PILOT_GATE.md` — acceptance criteria before industrial execution.
- `samples/INV-010_RUN_CARD.md` — first pilot card generated from the registry, **not executed**.
- `tools/build_run_card.py` — generates a card from the canonical registry; no hidden state.

## Lifecycle

```text
registry row
-> RUN_CARD
-> Truth Engine v2.10.6 canonical investigation
-> RUN_HANDOFF
-> RENARD gate
   -> NO -> close/update registry
   -> REQUIRED -> RENARD delta sidecar -> update handoff/registry
-> triage every new idea
-> choose one next MAIN_DYNAMIC item
```

## Non-goal

METHOD_PACK does not replace Truth Engine, does not alter its final format and does not create a second fact database.
