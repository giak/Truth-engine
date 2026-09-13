---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-090-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-08"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-090"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-090 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-090

```text
SUBJECT = Shadow banning, démonétisation, déréférencement et friction algorithmique : existence, fréquence, recours
OBJECT_QUESTION = Dans quels cas les plateformes appliquent-elles réellement shadow banning, démonétisation, déréférencement ou friction algorithmique à des contenus ou acteurs politiques, par quelles règles, signaux ou interventions, à quelle fréquence, avec quels recours ou corrections, et quels effets mesurables sur l’exposition sans confondre baisse de portée, modération ordinaire, changement d’algorithme et ciblage politique ?
SCOPE = France/UE 2018–2026, avec comparateurs étrangers uniquement lorsque le mécanisme est isomorphe. Tracer plateforme -> règle/signal ou éventuelle demande externe -> cible/contenu -> action de ranking, déréférencement, démonétisation ou restriction -> portée/exposition avant-après -> notification -> recours/correction -> effet observable. Prioriser politiques et transparence plateformes, DSA/régulateurs/juridictions, audits ou expériences, datasets et cas documentés. Gardes : reduced_reach != shadowban ; moderation != political_motive ; demonetization != censorship ; ranking_change != targeted_suppression ; complaint != proof ; detected_case != prevalence ; platform_action != state_tasking ; exposure_change != persuasion ; exposure_change != electoral_effect.
MODE = RECHECK_EXTEND
COVERAGE = SUBSTANTIAL_PRIOR
CORPUS_REFS = A002:212051560.qui-fabrique-lautorite-du-vrai;A004:210182384.lingerence-sans-mesure;A071:186904003.larchitecture-de-la-censure-europeenne;A097:180580808.pravda-quand-lelysee-ironise-sur;A098:180481861.quand-lelysee-attaque-un-journaliste
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
ORCHESTRATOR = INVESTIGATION_ORCHESTRATOR.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md. Preserve the selected contract from INVESTIGATION_ORCHESTRATOR.md; do not broaden the run to adjacent context.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
