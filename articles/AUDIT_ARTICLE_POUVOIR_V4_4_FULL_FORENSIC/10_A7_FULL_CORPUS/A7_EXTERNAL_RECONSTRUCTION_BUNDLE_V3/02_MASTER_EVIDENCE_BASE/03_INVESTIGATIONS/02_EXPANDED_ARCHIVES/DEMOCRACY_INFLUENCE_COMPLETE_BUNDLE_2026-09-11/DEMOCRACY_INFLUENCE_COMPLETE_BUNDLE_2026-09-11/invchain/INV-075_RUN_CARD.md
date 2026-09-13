---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-075-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-075"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-075 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-075

```text
SUBJECT = Audiovisuel public : argent, gouvernance, production privée, nominations et indépendance éditoriale
OBJECT_QUESTION = Dans l'audiovisuel public français, quels mécanismes de financement, nomination, gouvernance et recours à la production privée peuvent affecter priorités éditoriales ou sélection des contenus, et quelles preuves permettent d'établir ou de réfuter une intervention politique identifiable ?
SCOPE = France, principalement 2015–2026. Tracer règle/budget/nomination/contrat -> pouvoir formel ou incitation -> décision éditoriale identifiable -> contenu/exposition -> effet éventuel. Prioriser textes, contrats d'objectifs, budgets, nominations, décisions ARCOM, marchés de production, documents internes publiés et contentieux. Gardes : financement public != contrôle éditorial ; nomination != tasking ; biais perçu != intervention ; production privée != dépendance ; contenu != effet politique.
MODE = RECHECK_EXTEND
COVERAGE = SUBSTANTIAL_PRIOR
CORPUS_REFS = A025:199654938.medias-censure-et-desinformation;A049:193809543.audiovisuel-public-anatomie-dune
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
