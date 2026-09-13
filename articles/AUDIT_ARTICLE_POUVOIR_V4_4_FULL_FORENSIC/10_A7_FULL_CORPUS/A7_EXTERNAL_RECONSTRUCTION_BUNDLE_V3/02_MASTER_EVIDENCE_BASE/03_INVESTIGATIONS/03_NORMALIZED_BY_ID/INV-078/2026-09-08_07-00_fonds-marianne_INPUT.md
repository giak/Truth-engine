---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-078-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-08"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-078"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-078 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-078

```text
SUBJECT = Fonds Marianne et financement étatique de la contre-influence : anatomie complète
OBJECT_QUESTION = Quels flux financiers, décisions de sélection, bénéficiaires, objectifs, livrables, contrôles, conflits d’intérêts ou irrégularités documentés composent le Fonds Marianne, et quelles preuves permettent de distinguer financement public de contre-influence, dysfonctionnement de gouvernance, favoritisme, commandement éditorial, opération politique et effet ?
SCOPE = France, Fonds Marianne 2021–2026. Reconstituer création, gouvernance, crédits, appels/sélection, bénéficiaires et montants, objectifs/livrables, contrôles administratifs, parlementaires ou judiciaires, conflits d’intérêts et suites. Tracer financeur -> décisionnaire -> bénéficiaire -> prestation/livrable -> contrôle -> conséquence. Gardes : funding != command ; irregularity != corruption ; selection_failure != political_tasking ; beneficiary_output != state_editorial_control ; allegation != proof ; investigation != guilt ; public_funding != censorship ; expenditure != political_effect. Alimenter INV-144.
MODE = RECHECK_EXTEND
COVERAGE = SUBSTANTIAL_PRIOR
CORPUS_REFS = A002:212051560.qui-fabrique-lautorite-du-vrai;A039:198659211.opposition-controlee-anatomie-dun;A072:186844276.tristan-mendes-france-la-machine
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
