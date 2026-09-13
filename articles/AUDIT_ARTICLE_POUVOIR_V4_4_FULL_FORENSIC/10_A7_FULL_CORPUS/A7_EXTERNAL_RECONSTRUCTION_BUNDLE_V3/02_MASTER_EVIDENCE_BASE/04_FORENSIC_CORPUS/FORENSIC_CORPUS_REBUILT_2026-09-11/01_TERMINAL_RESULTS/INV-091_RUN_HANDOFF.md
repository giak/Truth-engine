---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-091-RUN-HANDOFF"
version: "1.0"
status: "terminal"
updated: "2026-09-08"
inv_id: "INV-091"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
---

<!-- TRACE: source_run=20260908-2240-algorithmic-political-exposure; delivery=PASS; renard=NO -->

# RUN_HANDOFF — INV-091

## Résultat utile

La chaîne `règle/algorithme + signaux utilisateur -> classement/recommandation -> exposition différenciée` est établie. Le passage de l'exposition à l'effet politique est **contingent**, pas automatique : un contrôle randomisé Facebook modifie l'exposition sans effet politique correspondant, tandis qu'une expérience randomisée sur X observe des changements d'engagement et de plusieurs opinions sous fil algorithmique.

## Bornes

- `ranking != censorship` ;
- `personalization != manipulation` ;
- `visibility_change != political_motive` ;
- `exposure != persuasion` ;
- `persuasion != electoral_effect` ;
- `algorithmic_bias != intentional_tasking` ;
- `platform_design != state_tasking`.

Aucun effet électoral causal France/UE, biais partisan intentionnel généralisé ou tasking étatique n'est établi.

## Certification

```text
truth_engine = DELIVERY_PASS_R3P1
run_id = 20260908-2240-algorithmic-political-exposure
qrys = 30
sources = 15
facts = 30
provenance_families = 5
tests = 140 passed / 2 skipped
gates = G0-G10 PASS
persistence = PASS / 22 blocked MNEMO_UNAVAILABLE / 8 EVIDENCE ineligible
sha256 = 1e64402c22b4daa16a3ce5963cc1626b5fb42a46cf681b8b1f86006ca4433bf1
renard = NO
```

## Route

`INV-091 -> CLOSED`. Les cinq dépendances directes d'`INV-088` sont désormais CLOSED : `INV-088` devient dependency-complete, mais reste non sélectionnée tant qu'un cycle CORE_MISSION_V2 ne l'autorise pas explicitement.
