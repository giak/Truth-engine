---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-121-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-121"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-121 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-121

```text
SUBJECT = Industrie pharmaceutique : lobbying, expertise, recherche, régulation, médias et conflits d’intérêts
OBJECT_QUESTION = Dans quels dossiers pharmaceutiques des financements, expertises, conflits d'intérêts ou actions de lobbying peuvent-ils être reliés à une recommandation, règle, remboursement ou décision publique identifiable, et quelles arêtes restent nécessaires pour établir influence ou capture ?
SCOPE = France/UE, principalement 2010–2026, sur décisions de santé/régulation bornées. Tracer entreprise/financeur -> expert, étude, lobbying ou relation -> instance décisionnelle -> recommandation/delta de texte/décision -> effet. Prioriser déclarations d'intérêts, financements d'études, consultations, avis d'agences, registres et documents versionnés. Gardes : financement != falsification ; conflit != biais démontré ; expertise != tasking ; lobbying != capture ; corrélation de décision != causalité.
MODE = DEEPEN
COVERAGE = PARTIAL
CORPUS_REFS = A001:212538645.qui-fact-checke-les-fact-checkers;A043:194966421.la-constellation-davril;A045:194518266.lingenierie-de-lenclos;A056:192351575.le-reseau-qui-nous-facture;A082:183123537.lempire-du-mensonge-rapport-dautopsie;A089:182308074.france-2025-lanatomie-dune-feodalite;A095:180851146.france-2025-larchitecture-de-lenfer
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
