---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-015-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-015"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-015 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-015

```text
SUBJECT = Otpor, CANVAS et exportation des techniques de mobilisation politique
OBJECT_QUESTION = Dans quels cas les méthodes associées à Otpor/CANVAS ont-elles été effectivement transférées à des mouvements politiques, par quels financements, formations ou intermédiaires, et quels effets sur capacité de mobilisation ou résultat politique peuvent être établis sans confondre assistance, inspiration, orchestration et contrôle ?
SCOPE = Serbie puis cas internationaux documentables, principalement 1998–2026. Tracer organisme/formateur/financeur -> formation/ressource -> organisation bénéficiaire -> adoption observable de méthodes -> mobilisation mesurée -> résultat éventuel. Prioriser documents de programme, budgets, supports de formation, témoignages croisés et données de mobilisation. Gardes : formation != tasking ; financement != commandement ; méthode similaire != transfert prouvé ; mobilisation != résultat politique ; assistance extérieure != orchestration.
MODE = GREENFIELD
COVERAGE = NEW
CORPUS_REFS = NONE
DEPENDENCIES = NONE

TRUTH_ENGINE_PACK = TRUTH_ENGINE_2.10.6_R3P1_CANONICAL.zip
TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
ORCHESTRATOR = INVESTIGATION_ORCHESTRATOR.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md. Preserve the selected contract from INVESTIGATION_ORCHESTRATOR.md; do not broaden the run to adjacent context.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
