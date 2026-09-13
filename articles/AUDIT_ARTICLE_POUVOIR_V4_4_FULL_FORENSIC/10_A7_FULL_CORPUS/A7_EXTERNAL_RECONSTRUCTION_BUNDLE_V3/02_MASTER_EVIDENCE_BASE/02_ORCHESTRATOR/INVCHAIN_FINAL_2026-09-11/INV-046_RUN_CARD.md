---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-046-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-10"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-046"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-046 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-046

```text
SUBJECT = Chat Control, eIDAS, identité numérique, portefeuille européen : sécurité versus infrastructure potentielle de contrôle
OBJECT_QUESTION = Quelles capacités concrètes de Chat Control, eIDAS et du portefeuille européen d'identité modifient réellement collecte, authentification, accès, traçabilité ou contrôle des communications, et dans quelles conditions ces capacités peuvent-elles affecter libertés, anonymat ou participation démocratique sans présumer un usage politique abusif ?
SCOPE = Union européenne, textes adoptés/proposés et implémentations 2021–2026. Tracer règle -> capacité technique -> acteur habilité -> donnée/action accessible -> contrôle/recours -> effet observé ou plausible sous conditions explicitables. Prioriser textes juridiques, architecture technique, analyses d'impact, autorités de contrôle et jurisprudence. Gardes : capacité != usage ; identité numérique != surveillance ; sécurité != neutralité ; risque != abus prouvé ; métadonnée != contenu ; architecture de contrôle != influence politique.
MODE = RECHECK_EXTEND
COVERAGE = SUBSTANTIAL_PRIOR
CORPUS_REFS = A067:188810196.le-gulag-digital-surveilles-a-100;A071:186904003.larchitecture-de-la-censure-europeenne;A074:186286764.ce-que-macron-appelle-protection;A109:180129975.leurope-construit-elle-un-credit-40d;A110:180128122.leurope-construit-elle-un-credit
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
