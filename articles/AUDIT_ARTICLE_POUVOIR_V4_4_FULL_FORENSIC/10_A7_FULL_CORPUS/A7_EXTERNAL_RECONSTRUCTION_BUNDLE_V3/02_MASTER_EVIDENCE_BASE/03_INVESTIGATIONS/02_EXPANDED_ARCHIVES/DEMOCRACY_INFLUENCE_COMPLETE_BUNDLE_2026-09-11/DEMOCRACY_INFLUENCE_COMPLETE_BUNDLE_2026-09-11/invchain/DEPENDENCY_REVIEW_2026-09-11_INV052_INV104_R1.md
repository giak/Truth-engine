---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "dependency_design_review"
artifact_id: "DEPENDENCY-REVIEW-INV052-INV104-2026-09-11-R1"
version: "1.0-kiss"
status: "final"
updated: "2026-09-11"
---

<!-- RULE: do_not_run_HOLD_merely_to_unlock_synthesis=true -->
<!-- DECISION: INV-058 removed from INV-052; INV-106 and INV-107 removed from INV-104 -->

# Dependency design review — INV-052 / INV-104

## INV-052

`INV-058` is not necessary to answer the synthesis question. Its object is generic NGO accountability/governance. Equivalent controls already exist in closed dependencies:

- `INV-049`: OSF grants/resources established; beneficiary tasking/control not established.
- `INV-051`: foundation resources -> capacity/access/agenda effects; funding != command and access != capture.
- `INV-053`: public/private funding -> NGO capacity/advocacy; SOS Méditerranée supplies a legal separation control between humanitarian subsidy and political activity.
- `INV-054`: funded civil-society capacity and self-directed litigation; donor tasking of a named case not established.
- `INV-057`: funder objective/monitoring -> intermediary output with variable autonomy; funding -> command/tasking remains unproven without authenticated instruction.

Running `INV-058` would therefore add a generic control layer, not a material causal edge. Remove it from the direct synthesis DAG. `INV-058` remains BACKLOG/HOLD and is not declared disproven.

## INV-104

`INV-106` and `INV-107` are broad threat-production/moral-panic modules. Neither isolates the causal bridge required by INV-104: `institutional mistrust -> greater vulnerability to manipulation/outrage/conspiracy exploitation`.

Closed dependencies already provide the necessary endpoints:

- `INV-103`: levels/determinants of institutional trust and explicit causal ceiling.
- `INV-111`: causal effects of negativity/social reinforcement/ranking on attention and some platform-specific political attitudes, with null controls.
- `INV-112`: actor-specific exploitation of conspiracy narratives, domestic mobilization and attention-market incentives, without a general exposure->persuasion->electoral-effect chain.

The synthesis can therefore test whether the bridge exists; if it is absent, the correct result is `NOT_ESTABLISHED`, not a forced run of unrelated broad modules. Remove `INV-106` and `INV-107` from the direct synthesis DAG. They remain BACKLOG/HOLD.

## Gate

Both dependency edits satisfy `INVESTIGATION_ORCHESTRATOR.md §7`: explicit design review demonstrates the HOLD dependencies are not necessary. No evidence claim is added and no CLOSED result is reinterpreted.
