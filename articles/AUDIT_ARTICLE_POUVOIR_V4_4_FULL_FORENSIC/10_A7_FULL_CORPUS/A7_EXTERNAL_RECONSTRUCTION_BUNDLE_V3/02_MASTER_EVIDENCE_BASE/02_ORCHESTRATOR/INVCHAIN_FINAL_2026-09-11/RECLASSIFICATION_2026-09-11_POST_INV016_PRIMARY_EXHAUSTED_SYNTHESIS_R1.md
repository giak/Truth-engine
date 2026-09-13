---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "routing_frontier_transition"
artifact_id: "POST-INV016-PRIMARY-EXHAUSTED-SYNTHESIS-2026-09-11-R1"
version: "1.0-kiss"
status: "final"
updated: "2026-09-11"
policy_version: "CORE_MISSION_V2/ranking-7/v1"
closed: "INV-016"
selected: "INV-040"
---

<!-- TRACE: primary_pool_after_close=12; primary_PASS=0; primary_HOLD=12; no_primary_winner=true -->
<!-- DECISION: do_not_force_HOLD=true; synthesis_frontier_review=INV-038,INV-040,INV-068; selected=INV-040 -->

# Frontière post-INV-016 — PRIMARY épuisés, passage aux synthèses

## Fermeture primaire

`INV-016` est DELIVERY-certified et terminal. Après son retrait, les douze `PRIMARY|CASE` encore en backlog sont tous `HOLD` sous `CORE_MISSION_V2`. Aucun gagnant primaire ne peut donc être fabriqué sans violer le hard gate.

Restent HOLD : `INV-009`, `INV-024`, `INV-031`, `INV-032`, `INV-034`, `INV-058`, `INV-105`, `INV-106`, `INV-107`, `INV-108`, `INV-109`, `INV-123`.

## Gate synthèses prêtes

| INV | Dépendances | CORE_MISSION_V2_synthesis | Gain attendu | Verdict |
|---|---|---|---|---|
| INV-038 | INV-130; INV-131 tous CLOSED | PASS | MATERIAL — comparaison isomorphe Maroc/Algérie, forte discrimination actor-specific mais périmètre étroit | Éligible |
| INV-040 | INV-039;041;042;043;044;045;046;047;048 tous CLOSED | PASS | MATERIAL — confronte neuf mécanismes UE et les modèles déficit/délégation/co-législation/contre-pouvoir; plus fort gain transversal immédiat | **SELECT** |
| INV-068 | INV-059;061;062;063;064;065;066;067;085 tous CLOSED | PASS | MATERIAL — teste funding/access/reprise/tasking dans la chaîne think tank→média→décideur | Éligible |

## Décision

`INV-040` devient l’unique `SYNTHESIS_SELECTED`. Aucun Truth Engine ni web générique n’est autorisé. La synthèse consomme exclusivement les sorties terminales de ses neuf dépendances.
