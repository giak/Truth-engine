---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "routing_reclassification_delta"
artifact_id: "RECLASSIFICATION-POST-INV131-2026-09-10-DELTA-R1"
version: "1.0-kiss"
status: "final"
updated: "2026-09-10"
policy_version: "CORE_MISSION_V2/ranking-7/v1"
closed: "INV-131"
baseline_artifact: "RECLASSIFICATION_2026-09-10_POST_INV131_CORE_MISSION_V2_FULLPOOL_R1.md"
baseline_sha256: "bfecc214dd53024a5baa592f4d00cd30d0eab8d5af9ef06069331bb21ff7fd48"
selected: "INV-021"
---

<!-- TRACE: incremental=true; current_pool_after_close=29; review=INV-147; reuse=28; removed=NONE; full_pool_ranking=true -->
<!-- DECISION: priority_unused=true; winner=INV-021; review_reason=explicit_INV131_impact_on_INV147 -->

# Reclassification delta post-INV-131 — CORE_MISSION_V2

## Delta matériel

Voir `INV-131_RUN_HANDOFF.md`. Le run algérien ajoute à `INV-147` un comparateur mécanistique matériel, notamment influence cultuelle transparente, levier consulaire/coercitif avec contrôle d'efficacité, et opération clandestine sous procédure. Il ne fournit cependant pas le dataset systématique de labels, seuils probatoires et conséquences institutionnelles exigé par le contrat `INV-147`.

## REVIEW

| INV | Gate | model_change | discrimination | effect_closure | symmetry_value | dependency_unlock | coverage_gap | utility | Motif |
|---|---|---|---|---|---|---|---|---|---|
| INV-147 | PASS | VERY_HIGH | VERY_HIGH | MEDIUM | VERY_HIGH | LOW | VERY_HIGH | HIGH | INV-131 renforce le matériau apparié et démontre pourquoi la comparaison doit être mécanisme-par-mécanisme, mais ne ferme ni dénominateur d'enforcement, ni corpus lexical systématique, ni chaîne aval d'effet. Scores conservés après REVIEW explicite. |

## Verdict

`INV-021` est le gagnant lexicographique du full-pool fusionné après fermeture d'`INV-131`. `INV-147` ne le dépasse pas car `effect_closure=MEDIUM` contre `HIGH` pour `INV-021` après égalité sur `model_change` et `discrimination`. `priority=P1/P2` n'est pas utilisée.
