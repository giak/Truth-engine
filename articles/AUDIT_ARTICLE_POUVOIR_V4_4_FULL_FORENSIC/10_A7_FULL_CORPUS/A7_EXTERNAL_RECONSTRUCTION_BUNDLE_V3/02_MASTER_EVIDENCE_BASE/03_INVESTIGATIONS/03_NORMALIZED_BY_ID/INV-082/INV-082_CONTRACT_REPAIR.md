---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "synthesis_contract_repair"
artifact_id: "INV-082-CONTRACT-REPAIR-2026-09-08"
version: "1.0"
status: "applied"
updated: "2026-09-08"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-082"
---

<!-- TRACE: after=INV-085_CLOSED; dependencies=INV-081,INV-085; all_closed=true -->
<!-- DECISION: transition=BLOCKED->BACKLOG; gate=DEPENDENCIES_DONE; repair=object_question+scope; factual_claims_added=false -->
<!-- GATE: synthesis-card requires BACKLOG+DEPENDENCIES_DONE+all_dependencies_CLOSED+nonempty_contract -->

# Contract repair — INV-082 — 2026-09-08 04:48 Europe/Paris

## Defect

The dependency gate was satisfied, but the registry still had `status=BLOCKED` and empty `object_question` / `scope`. `control.py synthesis-card` would correctly refuse that state.

## Minimal repair

```text
STATUS = BACKLOG
GATE = DEPENDENCIES_DONE
OBJECT_QUESTION = Dans quelle mesure la concentration économique et capitalistique des médias se traduit-elle réellement par une concentration éditoriale observable, par quels mécanismes documentés, et quelles preuves permettent de distinguer capacité structurelle, sélection éditoriale, intervention ou tasking, alignement émergent et contrôle causal ?
SCOPE = Synthèse stricte des dépendances fermées INV-081 et INV-085, centrée sur la France et sur les mécanismes effectivement couverts par leurs deltas terminaux. Comparer uniquement les arêtes isomorphes entre propriété/financement, capacité d'accès, sélection des sujets, autorité éditoriale et contrôle externe. Aucune nouvelle collecte web ni nouveau run Truth Engine. Gardes : economic_concentration != editorial_concentration ; ownership != editorial_command ; funding != topic_tasking ; selection_asymmetry != owner_causation ; shared_output != coordination ; reach != persuasion ; editorial_effect != electoral_effect.
TRUTH_ENGINE = NOT_RUN
RENARD = UNDECIDED
```

No evidentiary conclusion is introduced by this repair. It only makes the already-unlocked synthesis executable under the existing control contract.
