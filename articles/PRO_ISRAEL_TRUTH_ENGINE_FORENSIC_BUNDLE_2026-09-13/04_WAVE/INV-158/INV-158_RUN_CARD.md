---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-158-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-13"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-158"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-158 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-158

```text
SUBJECT = Écosystème de plaidoyer pro-Israël en France : ressources, accès et empreintes décisionnelles
OBJECT_QUESTION = Dans quelle mesure des organisations pro-Israël ou sionistes déclarées en France transforment-elles ressources, accès et plaidoyer en modifications observables de textes, décisions ou positions publiques, et où les chaînes causales s'arrêtent-elles à l'accès, à l'alignement, à l'agenda-setting ou à la simple chronologie ?
SCOPE = France, principalement 2017-2026. Acteurs examinés seulement lorsqu'un mécanisme est documentable : CRIF, ELNET France/Europe, AJC France et interfaces avec l'État israélien ou son ambassade lorsque la relation est prouvée. Cas prioritaires : définition IHRA et résolution 2019 ; initiatives législatives/administratives 2024-2026 contre l'antisémitisme ; voyages, événements et auditions ; reconnaissance française de l'État palestinien et restrictions visant des responsables/colons israéliens comme contrôles négatifs. Tracer acteur -> ressource/financement -> demande/contribution documentée -> accès/cible -> delta de texte/décision -> adoption/non-adoption -> effet. Gardes : identité juive != sionisme != plaidoyer pro-Israël != État israélien ; représentation des Juifs de France != tasking israélien ; financement != commandement ; accès != adoption ; chronologie != causalité ; alignement != capture ; non-adoption != absence d'influence. Les affirmations théologiques/ethniques du transcript sont hors scope sauf si elles deviennent elles-mêmes un objet politique documenté.
MODE = RECHECK_EXTEND
COVERAGE = SUBSTANTIAL_PRIOR
CORPUS_REFS = NONE
DEPENDENCIES = INV-026;INV-027;INV-028

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
