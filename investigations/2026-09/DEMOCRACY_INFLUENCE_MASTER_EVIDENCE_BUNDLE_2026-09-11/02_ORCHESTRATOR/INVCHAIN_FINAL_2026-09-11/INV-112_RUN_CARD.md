---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-112-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-112"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-112 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-112

```text
SUBJECT = Complotisme comme symptôme, marché et instrument politique : causes réelles, exploitations et erreurs institutionnelles
OBJECT_QUESTION = Dans quels cas des récits complotistes sont-ils produits ou exploités intentionnellement par des acteurs identifiables, par quels canaux, et avec quels effets mesurables distincts des causes sociales ou psychologiques qui favorisent leur réception ?
SCOPE = France/Europe, principalement 2015–2026, en séparant origine spontanée, marché attentionnel et exploitation politique. Tracer acteur -> récit/amplification -> audience -> réception -> action ou effet politique. Prioriser contenus attribués, réseaux de diffusion, données d'audience, financements et études causales. Gardes : croyance complotiste != opération d'influence ; corrélation sociale != cause ; monétisation != tasking ; diffusion != persuasion ; erreur institutionnelle != complot.
MODE = RECHECK_EXTEND
COVERAGE = SUBSTANTIAL_PRIOR
CORPUS_REFS = A001:212538645.qui-fact-checke-les-fact-checkers;A002:212051560.qui-fabrique-lautorite-du-vrai;A008:208733314.la-fabrique-de-la-menace-comment;A059:191154925.pourquoi-les-electeurs-francais-votent;A069:187436825.darwin-et-evolution-enquete-sur-les;A072:186844276.tristan-mendes-france-la-machine;A082:183123537.lempire-du-mensonge-rapport-dautopsie
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
