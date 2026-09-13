---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-093-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-093"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-093 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-093

```text
SUBJECT = Financement des campagnes françaises : argent, prêts, micro-partis, prestations, contournements possibles
OBJECT_QUESTION = Comment les campagnes électorales françaises sont-elles effectivement financées et contrôlées — dons, prêts, micro-partis, mandataires, prestations, dépenses de campagne et flux connexes —, quelles irrégularités ou contournements sont juridiquement documentés, et jusqu’où peut-on relier un flux financier à un avantage politique, une violation, une sanction ou un effet sans convertir anomalie comptable, proximité ou prêt en fraude ou corruption ?
SCOPE = France, 2012–2026, priorité élections présidentielle, législatives et européennes lorsque les données CNCCFP, juridictionnelles ou comptables sont comparables. Tracer source des fonds, véhicule juridique, bénéficiaire, prestation/dépense, règles applicables, contrôle, décision, recours et conséquence. Distinguer don, prêt, prestation, dette, micro-parti, dépense tierce et avantage en nature. Exclure le financement étranger comme objet principal, traité par INV-094/INV-140, sauf lorsqu’il éclaire une règle ou un mécanisme français. Une irrégularité comptable n’est pas en soi une fraude; rejet ou réformation de comptes n’établit pas une corruption; financement n’établit pas commandement politique.
MODE = DEEPEN
COVERAGE = PARTIAL
CORPUS_REFS = A003:210245443.limpossible-rassemblement;A039:198659211.opposition-controlee-anatomie-dun;A101:180309272.ladieu-aux-partis-du-diagnostic-de
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
