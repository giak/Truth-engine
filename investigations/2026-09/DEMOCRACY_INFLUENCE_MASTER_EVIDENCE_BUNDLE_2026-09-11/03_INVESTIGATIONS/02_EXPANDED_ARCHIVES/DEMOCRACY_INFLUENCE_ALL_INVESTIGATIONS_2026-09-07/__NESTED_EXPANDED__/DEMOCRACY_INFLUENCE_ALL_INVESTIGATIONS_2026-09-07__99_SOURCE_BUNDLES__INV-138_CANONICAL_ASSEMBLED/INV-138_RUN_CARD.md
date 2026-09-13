---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-138-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-138"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-138 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-138

```text
SUBJECT = France comme puissance d’influence à l’étranger : diplomatie, AFD, médias internationaux, réseaux politiques, assistance électorale et renseignement
OBJECT_QUESTION = Quels mécanismes la France utilise-t-elle pour influencer des espaces politiques étrangers, lesquels sont transparents et consentis, lesquels sont coercitifs ou clandestins, et selon quels critères les qualifier sans employer un standard différent de celui appliqué aux puissances visant la France ?
SCOPE = 2000–2026, échantillon de cas documentables. Diplomatie publique, AFD, France Médias Monde, coopération institutionnelle/électorale, réseaux politiques, sanctions/conditionnalité et opérations clandestines uniquement lorsque documentées. Ne pas appeler « ingérence » l’aide, le média international ou la diplomatie par nature ; classifier mécanisme, visibilité, consentement, légalité, coordination et effet.
MODE = DEEPEN
COVERAGE = PARTIAL
CORPUS_REFS = A004:210182384.lingerence-sans-mesure;A091:181572197.lindustrie-de-linfluence-enquete
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
