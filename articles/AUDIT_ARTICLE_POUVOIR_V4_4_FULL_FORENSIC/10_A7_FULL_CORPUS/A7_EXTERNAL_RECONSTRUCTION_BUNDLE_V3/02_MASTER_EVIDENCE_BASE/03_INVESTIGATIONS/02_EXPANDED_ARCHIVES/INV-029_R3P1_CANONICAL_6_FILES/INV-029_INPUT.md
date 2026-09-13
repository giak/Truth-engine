---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-029-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-10"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-029"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-029 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-029

```text
SUBJECT = Allemagne : exercice de puissance au sein de l’UE — institutions, coalitions, poids économique et réglementaire
OBJECT_QUESTION = Par quels mécanismes institutionnels, de coalition, économiques ou réglementaires l'Allemagne peut-elle convertir préférences nationales et ressources en décisions européennes identifiables, et quels cas permettent de distinguer influence normale, pouvoir structurel et contrainte sur les choix d'autres États ?
SCOPE = Union européenne, principalement 2010–2026, sur dossiers décisionnels bornés. Tracer préférence allemande -> position/coalition/ressource -> procédure UE -> modification ou décision identifiable -> effet distributif/institutionnel. Prioriser documents Conseil/Commission/Parlement, positions nationales, textes versionnés, données de vote/coalition et analyses de négociation. Gardes : poids économique != contrôle ; position allemande != décision UE ; coalition != domination ; gain national != capture ; corrélation de préférences != causalité.
MODE = DEEPEN
COVERAGE = PARTIAL
CORPUS_REFS = A024:199655040.leurope-piege-francais-12-contentieux;A060:190739827.le-sabotage-energetique-francais;A063:189855247.le-sanctuaire-inverse-comment-la
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
