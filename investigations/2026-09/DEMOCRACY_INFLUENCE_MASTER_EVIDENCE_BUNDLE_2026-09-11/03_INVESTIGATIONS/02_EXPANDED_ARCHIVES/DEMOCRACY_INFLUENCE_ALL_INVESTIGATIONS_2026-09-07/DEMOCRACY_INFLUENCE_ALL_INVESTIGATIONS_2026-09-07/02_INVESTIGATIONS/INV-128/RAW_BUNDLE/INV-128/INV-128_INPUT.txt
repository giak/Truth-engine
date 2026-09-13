---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-128-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-128"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-128 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-128

```text
SUBJECT = Influence-for-hire : renseignement privé, cabinets d’intelligence, réputation, infiltration et campagnes clandestines pour clients étatiques ou privés
OBJECT_QUESTION = Quels services d’influence clandestine peuvent être achetés sur le marché privé — faux comptes, hacking, infiltration, faux médias, amplification, renseignement, réputation et suppression de contenu — et dans quels cas peut-on établir une chaîne client → prestataire → action → cible → exposition/effet sans confondre capacité annoncée, démonstration commerciale, opération exécutée, attribution et résultat ?
SCOPE = 2010–2026, priorité France/Europe avec comparateurs internationaux lorsque les traces sont meilleures. Étudier notamment les prestataires d’influence-for-hire et leurs chaînes documentées (Team Jorge, STOIC/Zero Zeno, Alp Services/EAU et cas comparables), en séparant strictement identité du client, contrat/paiement, capacité, action effectivement exécutée, cible, portée et effet. Exclure le lobbying déclaré et la PR ordinaire (INV-042/064), le cybercrime sans objectif politique ou réputationnel, et toute attribution de client fondée sur la seule nationalité, géographie ou proximité.
MODE = DEEPEN
COVERAGE = PARTIAL
CORPUS_REFS = A004:210182384.lingerence-sans-mesure;A071:186904003.larchitecture-de-la-censure-europeenne;A091:181572197.lindustrie-de-linfluence-enquete
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
