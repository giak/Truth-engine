---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-137-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-137"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-137 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-137

```text
SUBJECT = Renseignement → exécutif → médias : la chaîne d’attribution anonyme comme dispositif d’influence
OBJECT_QUESTION = Comment une évaluation de renseignement ou un briefing non public devient-il une affirmation publique, puis une certitude médiatique et éventuellement une décision politique ; quelles parties de la chaîne sont vérifiables, corrigées ou impossibles à auditer ?
SCOPE = France/UE 2015–2026. Tracer incident → source de renseignement/évaluation → porte-parole/exécutif → médias → mesure politique → correction éventuelle. Comparer briefings nommés, anonymes et documents déclassifiés. Distinguer protection légitime des sources, information probabiliste, fuite stratégique et manipulation démontrée.
MODE = DEEPEN
COVERAGE = PARTIAL
CORPUS_REFS = A004:210182384.lingerence-sans-mesure;A008:208733314.la-fabrique-de-la-menace-comment
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
