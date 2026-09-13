---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "routing_reclassification"
artifact_id: "RECLASSIFICATION-2026-09-07-0829"
version: "1.0"
status: "applied"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
selected: "INV-100"
---

<!-- TRACE: after=INV-146_CLOSED; policy=CORE_INGERENCE_ROUTING_2026-09-06_v1.1-kiss -->
<!-- DECISION: select=INV-100; tie_break=none; transition=BACKLOG->READY; launch=false -->
<!-- GATE: target_downstream=INV-102,INV-129; both_feed=INV-133 -->

# Reclassification post-INV-146 — 2026-09-07 08:29 Europe/Paris

## Material change

`INV-146` est `CLOSED`. Le programme n'a plus de synthèse de symétrie directement exécutable. La priorité revient donc aux investigations qui combinent un mécanisme d'ingérence discriminant et un effet réel sur les dépendances de `INV-133`.

La fermeture d'`INV-100` alimenterait simultanément deux synthèses encore bloquées :

- `INV-102` — consentement / verrou institutionnel ;
- `INV-129` — lawfare et coercition juridique.

Ces deux synthèses sont elles-mêmes des dépendances directes d'`INV-133`.

## Pool de tête matérialisé

Ordre : `model_change > discrimination > dependency_unlock > coverage_gap > utility`.

| INV | CORE class | model_change | discrimination | dependency_unlock | coverage_gap | utility | décision |
|---|---|---|---|---|---|---|---|
| INV-100 | D/E | HIGH | HIGH | HIGH | HIGH | HIGH | **SELECT** |
| INV-044 | B/C/E | MEDIUM | HIGH | HIGH | HIGH | HIGH | HOLD |
| INV-054 | D/E | MEDIUM | HIGH | HIGH | HIGH | HIGH | HOLD |
| INV-143 | D | HIGH | HIGH | LOW | HIGH | HIGH | HOLD |
| INV-045 | C/E | MEDIUM | HIGH | HIGH | MEDIUM | HIGH | HOLD |
| INV-079 | B/E | MEDIUM | HIGH | HIGH | MEDIUM | HIGH | HOLD |
| INV-080 | C/D/E | MEDIUM | HIGH | HIGH | MEDIUM | HIGH | HOLD |
| INV-141 | B | MEDIUM | HIGH | LOW | HIGH | HIGH | HOLD |
| INV-142 | B | MEDIUM | HIGH | LOW | HIGH | HIGH | HOLD |
| INV-024 | B/D | MEDIUM | HIGH | LOW | HIGH | HIGH | HOLD |

## Pourquoi INV-100

`INV-100` n'est pas choisi parce que la Roumanie serait un cas politiquement spectaculaire. Il est choisi parce que l'objet est falsifiable et directement discriminant :

`allégation/irrégularité -> preuve -> base juridique -> standard de preuve -> décision -> recours -> effet électoral -> intention éventuelle`

Il permet de distinguer quatre objets souvent fusionnés :

1. une ingérence ou irrégularité alléguée ;
2. un constat institutionnel ou juridictionnel ;
3. une annulation/neutralisation juridiquement fondée ;
4. une instrumentalisation politique démontrée.

Son corpus est seulement `PARTIAL`, contrairement à plusieurs concurrents déjà `SUBSTANTIAL_PRIOR`, ce qui laisse un potentiel de changement de modèle plus élevé.

## Comparaison avec INV-143

`INV-143` reste matériel mais traite le **timing** des procédures avant scrutin. `INV-100` traite la décision terminale d'annuler ou neutraliser l'élection/candidature et son standard de preuve. Les deux objets sont complémentaires, pas doublons.

## Run-contract repair

La ligne legacy d'`INV-100` ne contenait pas `object_question` ni `scope`. Ces champs ont été ajoutés avant la transition `READY`. Aucun fait n'est ajouté au corpus par cette réparation.

Gardes :

```text
accusation_of_interference != judicial_finding
judicial_finding != political_intent
legal_annulment != illegitimate_interference
timing_correlation != instrumentalization
effect_on_competition != proof_of_motive
official_statement != proof
```

## Transition

```text
INV-100 BACKLOG -> READY
ACTIVE = NONE
LAUNCH = NO
```

Le prochain baby-step est `run-card INV-100`, puis lancement uniquement si le gate du run-card passe.
