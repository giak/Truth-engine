---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-061"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-068"
updated: "2026-09-10"
---

# RUN_HANDOFF — INV-061

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260910-1549-us-think-tanks-france-eu`
- Deliverable: `INV-061_INVESTIGATION.md`
- Deliverable SHA-256: `b2363248a9d17099c8cc4a29cc9a34282db1790d8291af545a871a5b48bcad58`
- Corpus runtime: `QRY=21 / SRC=9 / FCT=18 / provenance_families=5`
- Persistence: `PASS / eligible=18 / blocked=18 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-061 établit un canal transatlantique observable d’accès et d’expertise : des think tanks américains, surtout GMF mais aussi Brookings et Heritage dans des cas bornés, accèdent à des arènes parlementaires françaises/UE par auditions, études commandées, réunions et panels ; GMF documente aussi une architecture partenaire/membre -> événements, expertise et networking. Le plafond causal reste net : accès, commande d’expertise et convening ne démontrent ni adoption d’une recommandation, ni contrôle éditorial par un financeur, ni tasking par l’État américain, ni effet politique causal. Le contrôle isomorphe avec INV-059 soutient donc un mécanisme générique ressources/capacité -> accès/expertise -> exposition/reprise potentielle, pas une architecture coordonnée de commandement.

## Registre causal certifié

- `French/EU institution invites or commissions US-think-tank expert/output -> expert input reaches an official decision venue` = **SUPPORTED** — Closes access/input only; does not close adoption or effect.
- `GMF membership/partner support -> privileged events/networking/expertise access` = **SUPPORTED** — Resource/access architecture is self-described by GMF; sponsor-specific content control is not established.
- `Think-tank expert input or report -> specific French/EU policy adoption` = **UNRESOLVED** — Commissioned/admitted expertise is observable, but marginal contribution to final policy is not isolated.
- `Funder or US state -> think-tank tasking/content control -> French/EU influence action` = **UNRESOLVED** — Funding/proximity/ideological alignment are insufficient substitutes for an authenticated instruction/control chain.
- `High-level GMF convening -> exposure/contact among officials, experts and private actors` = **SUPPORTED** — Exposure opportunity only; persuasion, coordination and policy effect are not identified.

## Gaps matériels certifiés

- `CLM-004` / **RESPONSIBILITY** — No authenticated sponsor-specific instruction, veto, editorial-control or tasking record was identified in the bounded searches.
- `CLM-005` / **CAUSALITY** — No versioned decision footprint isolates a think-tank contribution as a necessary, sufficient or marginal cause of a French/EU policy decision in the inspected corpus.
- `CLM-006` / **RESPONSIBILITY** — No authenticated command/tasking chain was identified; absence of such evidence is not proof of non-existence.

## RENARD

`NO`

## Reclassification

Impact direct : `INV-068`.

## Transition attendue

`INV-061 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
