---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-112"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-104"
updated: "2026-09-11"
---

# RUN_HANDOFF — INV-112

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260911-0603-conspiracy-instrument`
- Deliverable: `INV-112_INVESTIGATION.md`
- Deliverable SHA-256: `8d15ed7dfd57161e0419e6d2fd171330110d08c8761861293edf589d8e7ce2ed`
- Corpus runtime: `QRY=9 / SRC=9 / FCT=11 / provenance_families=6`
- Persistence: `PASS / eligible=11 / blocked=11 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-112 ferme un modèle à trois mécanismes distincts : (1) des opérations actor-specific exploitent intentionnellement des récits complotistes, Storm-1516 fournissant un cas français attribué ; (2) les mobilisations domestiques peuvent intégrer des cadres complotistes sans commandement central ni causalité unique ; (3) engagement et monétisation peuvent soutenir la production et le partage indépendamment du tasking politique. Le corpus ne ferme pas une chaîne générale exposition→persuasion→effet électoral : visibilité, croyance, protestation et revenu restent des observables distincts.

## Registre causal certifié

- `Russian Storm-1516 operators -> fabricated conspiracy-style content -> coordinated distribution infrastructure -> online visibility / opportunistic political reuse` = **SUPPORTED** — Audience persuasion, durable belief change and electoral effect are not measured.
- `state/state-backed COVID conspiracy narratives -> EU audience exposure -> belief/health or political behavior change` = **UNRESOLVED** — Intentional exploitation and exposure pathway are supported; persuasion is unresolved.
- `Yellow Vest frames/networks/tactics -> anti-pass mobilisation in southern France` = **SUPPORTED** — This does not isolate the marginal effect of conspiracy claims from democratic grievances, identity or prior activist networks.
- `conspiracy belief -> reduced digital contact-tracing uptake / lower perceived procedural justice` = **UNRESOLVED** — Behavioral/attitudinal association is measurable; source-specific causation is not.
- `social engagement or monetization incentive -> intentional conspiracy sharing/content supply` = **SUPPORTED** — The evidence does not by itself establish downstream political persuasion or state tasking.

## Gaps matériels certifiés

- `CLM-002` / **CAUSALITY** — Actor-specific exposure -> belief change -> downstream political behavior is not measured in the attributed Storm-1516 cases.
- `CLM-004` / **CAUSALITY** — Need randomized/natural exposure design linking a specific narrative source to belief change and behavior.

## RENARD

`NO`

## Reclassification

Impact direct : `INV-104`.

## Transition attendue

`INV-112 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
