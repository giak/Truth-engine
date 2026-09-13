---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-111"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-104"
updated: "2026-09-11"
---

# RUN_HANDOFF — INV-111

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260911-0800-outrage-economy`
- Deliverable: `INV-111_INVESTIGATION.md`
- Deliverable SHA-256: `96219c4c884503efbebadf6216c930a6ecc7eca99683c90ebe209bddf23d06e7`
- Corpus runtime: `QRY=9 / SRC=9 / FCT=13 / provenance_families=5`
- Persistence: `PASS / eligible=13 / blocked=13 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-111 ferme un mécanisme à étages : la négativité augmente causalement le clic et le feedback social renforce l’expression future d’indignation ; les fils algorithmiques modifient fortement exposition et engagement. L’effet politique aval n’est toutefois pas universel : Meta et YouTube fournissent des contrôles nuls ou limités sur les attitudes, tandis qu’une expérience de terrain sur X ferme un effet causal sur plusieurs opinions. Le modèle robuste est donc `incitation/ranking -> exposition/engagement` avec conversion politique hétérogène, et non `engagement = persuasion` ou `outrage = manipulation`. Ce delta ferme INV-111 comme dépendance d’INV-104 mais laisse INV-106 et INV-107 ouvertes.

## Registre causal certifié

- `negative headline wording -> higher click-through -> editorial optimization incentive` = **SUPPORTED** — Click optimization is not equivalent to political persuasion or deliberate outrage maximization by all publishers.
- `social reward / network norms -> future outrage expression` = **SUPPORTED** — Expression is not proof of belief change or offline mobilization.
- `algorithmic feed -> exposure/engagement -> political attitudes` = **SUPPORTED** — Effect is platform- and horizon-specific; no universal sign or magnitude follows.
- `algorithmic feed -> political participation` = **SUPPORTED** — Online participation change does not imply electoral mobilization or vote change.
- `partisan recommendation skew -> intentional platform manipulation -> political outcome` = **UNRESOLVED** — Output skew alone cannot be relabeled as deliberate manipulation.

## Gaps matériels certifiés

- `CLM-004` / **EVIDENCE** — Experimental effects differ sharply by platform, intervention and horizon; Meta and YouTube provide null controls against a universal effect.
- `CLM-006` / **CAUSALITY** — Exposure asymmetry and oversight establish risk/output, not political intent or tasking.

## RENARD

`NO`

## Reclassification

Impact direct : `INV-104`.

## Transition attendue

`INV-111 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
