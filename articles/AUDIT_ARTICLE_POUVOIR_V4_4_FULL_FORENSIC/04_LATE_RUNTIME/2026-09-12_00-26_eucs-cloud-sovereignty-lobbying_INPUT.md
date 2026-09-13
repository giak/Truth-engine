---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-123-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-12"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-123"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-123 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-123

```text
SUBJECT = Big Tech / EUCS : lobbying contre les critères de souveraineté cloud et modification du schéma européen
OBJECT_QUESTION = Dans le dossier EUCS, quelles preuves relient les intérêts de grands fournisseurs cloud américains et leurs coalitions de lobbying -> demandes explicites de suppression des critères de souveraineté -> canaux de décision nationaux/UE -> modification des drafts 2023-2024 -> conséquences d'accès au marché, et jusqu'où peut-on attribuer causalement ce changement au lobbying plutôt qu'aux préférences autonomes d'États membres, clients cloud ou considérations juridiques/techniques ?
SCOPE = Union européenne, Allemagne, France et interface transatlantique, 2021-2026. Cas central : EUCS. Tracer Amazon/AWS et associations industrielles (BSA, CCIA, AmCham/USCIB et autres seulement si documentés) -> position/lettre/register/meeting -> décideur ou forum -> version du schéma -> retrait ou maintien des exigences de souveraineté -> effet d'éligibilité/accès au marché. Inclure les positions françaises/européennes opposées comme contrôles et la réintroduction 2026 de critères de souveraineté dans une architecture distincte seulement pour tester la stabilité du changement. Gardes : lobbying != causalité ; préférence d'État membre != capture ; texte modifié != preuve d'un auteur unique ; intérêt commercial != tasking étatique ; Big Tech != bloc homogène ; retrait EUCS != abandon définitif de la souveraineté numérique ; registre de lobbying prouve un objectif d'influence, pas son efficacité.
MODE = DEEPEN
COVERAGE = NEW_CAUSAL_CASE
CORPUS_REFS = NONE
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
