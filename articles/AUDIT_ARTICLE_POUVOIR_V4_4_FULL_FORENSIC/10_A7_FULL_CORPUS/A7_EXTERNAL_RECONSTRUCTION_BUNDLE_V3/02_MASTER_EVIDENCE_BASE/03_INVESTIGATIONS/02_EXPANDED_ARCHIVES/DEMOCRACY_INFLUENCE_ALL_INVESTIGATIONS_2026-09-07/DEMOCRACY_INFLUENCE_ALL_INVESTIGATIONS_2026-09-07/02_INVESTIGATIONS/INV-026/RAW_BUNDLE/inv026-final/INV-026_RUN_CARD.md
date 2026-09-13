---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-026-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-026"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-026 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-026

```text
SUBJECT = Israël : influence étatique, diplomatique, industrielle, sécuritaire et informationnelle en France/UE
OBJECT_QUESTION = Quels mécanismes documentables permettent à des acteurs étatiques ou paraétatiques israéliens de chercher à influencer en France ou dans l’UE des décisions publiques, perceptions, coalitions politiques, politiques de sécurité ou l’environnement informationnel ; et jusqu’où peut-on établir financement, tasking, coordination, exposition et effet sans confondre diplomatie, lobbying privé, affinité politique et ingérence ?
SCOPE = France/UE 2017–2026, comparateurs seulement lorsqu’ils discriminent le mécanisme. Inclure diplomatie publique, ministères/ambassades, campagnes informationnelles, opérations numériques attribuées, soutien ou financement d’intermédiaires, relations sécuritaires/industrielles lorsqu’elles visent une décision ou perception politique, et cas judiciaires/parlementaires documentés. Exclure toute assimilation d’organisations juives, pro-israéliennes ou privées à l’État sans preuve de relation ; Israël != tout acteur pro-israélien ; financement/proximité != tasking ; lobbying légal != ingérence ; plaidoyer sur un conflit != opération étatique par nature.
MODE = DEEPEN
COVERAGE = PARTIAL
CORPUS_REFS = A023:199655095.la-defense-rongee-449-md-sans-munitions;A055:192483249.ce-nest-pas-du-satanisme-cest-une;A057:192293819.la-democratie-en-cage
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
