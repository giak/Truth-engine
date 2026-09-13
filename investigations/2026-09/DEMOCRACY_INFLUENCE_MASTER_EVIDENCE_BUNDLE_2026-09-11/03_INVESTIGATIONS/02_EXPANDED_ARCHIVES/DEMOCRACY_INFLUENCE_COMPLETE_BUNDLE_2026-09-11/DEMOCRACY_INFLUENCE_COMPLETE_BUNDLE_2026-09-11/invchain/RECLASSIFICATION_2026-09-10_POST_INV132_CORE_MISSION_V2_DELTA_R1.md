---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "routing_reclassification_delta"
artifact_id: "RECLASSIFICATION-POST-INV132-2026-09-10-DELTA-R1"
version: "1.0-kiss"
status: "final"
updated: "2026-09-10"
policy_version: "CORE_MISSION_V2/ranking-7/v1"
closed: "INV-132"
baseline_artifact: "RECLASSIFICATION_2026-09-10_POST_INV035_CORE_MISSION_V2_DELTA_R1.md"
baseline_sha256: "73eee53f437a06db532d1be8b22914b85f8c89c7dc2e2294ab291e2bf3cffb07"
selected: "INV-147"
---

<!-- TRACE: incremental=true; current_pool_after_close=26; review=INV-147; reuse=25; removed=INV-132; full_pool_ranking=true -->
<!-- DECISION: priority_unused=true; winner=INV-147; review_reason=explicit_INV132_impact_on_INV147 -->

# Reclassification delta post-INV-132 — CORE_MISSION_V2

## Delta matériel

Voir `INV-132_RUN_HANDOFF.md`. INV-132 sépare empiriquement sociabilité, socialisation/capacité, coordination organisationnelle et tasking. Il ajoute à INV-147 des cas appariables où des structures transnationales comparables reçoivent des qualifications différentes selon leurs propriétés observables, mais il ne construit pas encore le dataset systématique de vocabulaire, seuils probatoires et conséquences institutionnelles requis par INV-147.

## REVIEW

| INV | Gate | model_change | discrimination | effect_closure | symmetry_value | dependency_unlock | coverage_gap | utility | Motif |
|---|---|---|---|---|---|---|---|---|---|
| INV-147 | PASS | VERY_HIGH | VERY_HIGH | MEDIUM | VERY_HIGH | LOW | VERY_HIGH | HIGH | INV-132 renforce le matériau de contrôle sur `network != coordination` et `access != adoption`, mais ne ferme pas le dataset apparié ni l'effet causal. Les scores restent donc inchangés après REVIEW explicite. |

## Verdict

`INV-147` est le gagnant lexicographique du pool fusionné après fermeture d'`INV-132`. Il conserve `VERY_HIGH / VERY_HIGH / MEDIUM / VERY_HIGH / LOW / VERY_HIGH / HIGH` et devance `INV-046`, à égalité sur model_change, discrimination et effect_closure, au quatrième critère `symmetry_value` (`VERY_HIGH` contre `MEDIUM`). `priority=P1/P2` n'est pas utilisée.
