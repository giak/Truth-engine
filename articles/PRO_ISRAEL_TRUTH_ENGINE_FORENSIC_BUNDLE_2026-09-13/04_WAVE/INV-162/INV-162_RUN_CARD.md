---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-162-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-13"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-162"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-162 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-162

```text
SUBJECT = Voices of Israel / financements publics vers société civile
OBJECT_QUESTION = Quels bénéficiaires et projets France/UE reçoivent des fonds israéliens de diplomatie publique et quels livrables sont exigés ?
SCOPE = Israël 2023-2026 + France/UE : calls, contrats, bénéficiaires, livrables, montants.
MODE = DEEPEN
COVERAGE = NEW_MECHANISM_OR_EFFECT_GAP
CORPUS_REFS = NONE
DEPENDENCIES = INV-158

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
