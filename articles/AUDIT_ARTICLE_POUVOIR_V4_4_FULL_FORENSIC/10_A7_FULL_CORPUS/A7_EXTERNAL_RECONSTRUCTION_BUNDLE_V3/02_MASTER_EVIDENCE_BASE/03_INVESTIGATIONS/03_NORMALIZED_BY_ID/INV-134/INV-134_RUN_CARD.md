---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-134-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-134"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-134 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-134

```text
SUBJECT = Attribution d’ingérence : chaîne de preuve, degrés de confiance, contradictions, corrections et responsabilités
OBJECT_QUESTION = Lorsqu’un État, un service, une plateforme ou un média attribue une opération à un acteur étranger, quelles preuves permettent de passer de l’incident observable à l’opérateur, puis au commanditaire étatique, à l’intention et à l’effet ; quels degrés de confiance, contradictions, révisions ou rétractations apparaissent ensuite ?
SCOPE = France/UE 2017–2026 avec comparateurs documentables. Auditer des chaînes d’attribution complètes, notamment VIGINUM, rapports de plateformes et cas où versions institutionnelles se contredisent. Cas von der Leyen/GPS 2025 comme test de méthode : distinguer existence d’une perturbation, attribution technique, lien à un État, intention et effet. Toute accusation et tout démenti sont des claims ; aucune autorité n’est une preuve par statut.
MODE = RECHECK_EXTEND
COVERAGE = PARTIAL
CORPUS_REFS = A004:210182384.lingerence-sans-mesure;A006:209222653.du-narratif-a-lingerence-le-seuil;A097:180580808.pravda-quand-lelysee-ironise-sur
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
