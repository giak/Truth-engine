---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-099-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-08"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-099"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-099 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-099

```text
SUBJECT = Fraude électorale réelle versus industrie de l’accusation de fraude : fréquence, mécanismes, vérifiabilité
OBJECT_QUESTION = Quelle est la fréquence et la nature des fraudes électorales effectivement établies en France et en Europe, par quels mécanismes et avec quels effets documentés, et quelles preuves permettent de distinguer fraude avérée, irrégularité ou erreur administrative, allégation non établie et campagne stratégique de délégitimation du scrutin ?
SCOPE = France/Europe 2000–2026, priorité à la France et aux scrutins nationaux ou locaux documentables ; comparateurs internationaux seulement lorsque mécanismes et standards de contrôle sont matériellement isomorphes. Tracer type de fraude ou irrégularité, acteur, mode opératoire, volume et dénominateur, détection, preuve, décision judiciaire ou administrative, correction/recours, effet sur les suffrages ou la sincérité du scrutin et diffusion éventuelle des accusations. Distinguer fraude intentionnelle, erreur, irrégularité procédurale, contentieux, accusation et effet. Gardes : allegation != fraud ; irregularity != fraud ; error != intent ; complaint != proof ; case != prevalence ; fraud_exists != result_changed ; accusation_volume != fraud_frequency ; detected_cases != total_prevalence. Alimenter INV-102.
MODE = GREENFIELD
COVERAGE = NEW
CORPUS_REFS = NONE
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
