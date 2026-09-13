# Bundle scope and authority

## Current target state
- registry rows: 157
- CLOSED: 134
- CLOSED PRIMARY|CASE used as substantive article universe: 113
- historical master evidence snapshot: 100 CLOSED PRIMARY|CASE
- explicit current delta: 13 investigations: INV-024, INV-031, INV-123, INV-148, INV-149, INV-150, INV-151, INV-152, INV-153, INV-154, INV-155, INV-156, INV-157

## Authority degradations to preserve
- `INV-035`: terminal in registry, but substantive handoff content was not recovered on the current surface; do not reconstruct its distinctive result.
- `INV-139`, `INV-140`: recovery-handoff-only authority.
- `INV-156`: protocol-reconstructed R3P1 authority; no canonical runtime replay is claimed.
- Absence of an artifact means absence of recovered evidence, never evidence of non-existence.

## Historical master bundle limitation
The 2026-09-11 master evidence snapshot predates the final 113-dossier article population. It is therefore not sufficient alone. `03_CURRENT_DELTA_13/` and `04_CURRENT_REGISTRY/` are part of the canonical reconstruction input for this bundle.

## Contamination guard
Do not open `90_READ_LAST/` before independently rebuilding at least A1/A2/A3 from the investigation corpus. That directory contains previous article outputs, internal pipeline artifacts and prior external criticism.
