---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-100-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-100"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-100 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-100

```text
SUBJECT = Annulation ou neutralisation judiciaire/administrative d’une élection : Roumanie et comparaisons internationales
OBJECT_QUESTION = Dans quels cas, sur quelles bases juridiques et avec quel niveau de preuve une juridiction ou une autorité administrative peut-elle annuler, invalider ou neutraliser une élection, une candidature ou un résultat au nom d’irrégularités, d’ingérence, de financement, de désinformation ou de sécurité, et comment distinguer remède institutionnel normal, erreur, effet politique et instrumentalisation démontrée ?
SCOPE = France/Europe 2015–2026 avec la Roumanie comme cas central et comparateurs uniquement s’ils sont juridiquement et procéduralement comparables. Tracer base juridique, faits retenus, origine et qualité des preuves, standard de preuve, calendrier, contradictoire, décision, recours, effet sur la compétition et preuve éventuelle d’intention. Séparer accusation d’ingérence, constat juridictionnel, annulation légale, effet électoral et instrumentalisation. INV-143 traite séparément le timing préélectoral.
MODE = DEEPEN
COVERAGE = PARTIAL
CORPUS_REFS = A006:209222653.du-narratif-a-lingerence-le-seuil;A057:192293819.la-democratie-en-cage
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
