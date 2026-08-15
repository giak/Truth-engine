# PERSO_FRESQUE v2.2 — Longitudinal person protocol

**Trigger:** the subject is a person. Force APEX depth, not predetermined suspicion or findings; mark longitudinal lenses NOT APPLICABLE when the question does not need them.

## §1 Lenses

| Lens | Build | Key checks |
|---|---|---|
| Chronology | dated roles, mandates, employers, boards, declarations | gaps, overlaps, source versions |
| Substance | authored/signed/voted/implemented actions | legal competence, actual effect, symbolic action |
| Influence | sourced meetings, donors, lobby contacts, advisers, affiliations | timing, disclosure, alternative access path |
| Position drift | comparable promises, statements, votes and decisions | changed facts/context, scope, honest revision |
| Biography gap | official biography versus primary records | materiality, negative and positive omissions |
| Responsibility | authority + documented action + consequence | intent evidence and bounded scope |

## §2 Search modules

```text
@PF[CHRONO]    official biography + mandates + employer/board registers + archives
@PF[ACTIONS]   votes + laws + amendments + reports + signed decisions + implementation
@PF[INTERESTS] asset/interest declarations + lobbying + donations + contracts + ownership
@PF[PIVOTS]    exact promise/statement before and after + corresponding action
@PF[NETWORK]   typed relationships with dates and provenance
```

Use jurisdiction-appropriate official registers and independent investigations; named examples are query hints, never mandatory authority.

## §3 Analysis discipline

- Compare equivalent statements/actions in context. A changed position is not deception by default.
- Detect text reuse/ghostwriting only with source documents and a reproducible comparison; stylistic intuition is insufficient.
- Quantify public cost/output only with comparable units. Do not divide arbitrary symbolic weights by euros to create a “democratic ROI”.
- Revolving-door timing is a conflict question, not proof of capture.
- Shared affiliation is an edge; tasking/control requires separate evidence.
- Include exculpatory facts and failed allegations with the same traceability.

Optional lens summary (no forced aggregate):

```text
DEMOCRATIC_OUTPUT:{evidenced actions/effects/cost limits}
CAPTURE_RISK:{documented dependencies/COI + counterevidence}
FRAME_DRIFT:{comparable language changes + context}
REVERSALS:{promise→action pairs + explanation/status}
```

## §4 Output

```text
FRESQUE_TIMELINE | ACTION_REGISTRY | INTERESTS/NETWORK | PIVOTS
BIOGRAPHY_GAPS | EXCULPATORY_RECORD | RESPONSIBILITY_MAP | UNKNOWN
```

Apply ordinary FACT_REGISTRY statuses, EDI and REQUEST_LOG. No minimum source mix, score, reversal or named wolf can replace evidence.

_Canonical authority: person-specific longitudinal branch._
