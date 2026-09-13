---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-089-RUN-HANDOFF"
version: "1.0"
status: "terminal"
updated: "2026-09-08"
inv_id: "INV-089"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
---

<!-- TRACE: source_run=20260908-2150-trusted-flaggers-moderation; delivery=PASS; renard=NO -->

# RUN_HANDOFF — INV-089

## Résultat utile

Le DSA crée pour les trusted flaggers un **pouvoir procédural de priorité**, pas un pouvoir autonome de retrait. La chaîne `désignation -> notification -> examen prioritaire -> décision plateforme -> recours/correction` est documentée. Les données opérationnelles ferment case-specifically l'effet sur le traitement et certaines restrictions, tout en montrant une forte hétérogénéité des résultats.

## Bornes

- `trusted_flagger_signal != platform_decision` ;
- `designation/funding != state_tasking` ;
- `removal != censorship` ;
- `appeal reversal != trusted-flagger-specific error rate` ;
- `platform_action != persuasion/electoral_effect`.

Aucune architecture générale de censure déléguée, de biais politique systémique, de tasking étatique ou d'effet électoral causal n'est établie.

## Certification

```text
truth_engine = DELIVERY_PASS_R3P1
run_id = 20260908-2150-trusted-flaggers-moderation
qrys = 30
sources = 15
facts = 30
provenance_families = 5
tests = 140 passed / 2 skipped
gates = G0-G10 PASS
persistence = PASS
sha256 = 15a64822a17470147d6a3a33e7f2b1e3b76a89c5a9348561c5d36fcf81ddf75c
renard = NO
```

## Route

`INV-089 -> CLOSED`; dépendance `INV-088` réduite : seul `INV-091` reste ouvert parmi ses dépendances directes.
