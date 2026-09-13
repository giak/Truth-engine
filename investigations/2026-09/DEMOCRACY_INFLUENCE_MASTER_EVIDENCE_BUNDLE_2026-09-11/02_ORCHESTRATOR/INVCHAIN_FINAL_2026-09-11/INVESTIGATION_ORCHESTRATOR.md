---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "investigation_orchestrator"
artifact_id: "INVESTIGATION_ORCHESTRATOR"
version: "2.4-kiss"
status: "active"
updated: "2026-09-10"
canonical_state_ref: "INVESTIGATION_REGISTRY.csv"
method_ref: "METHOD_PACK.md"
---

<!-- DECISION: mission_first=true; mechanism_first=true; portfolio_lanes=true; full_pool_semantics=true; incremental_reclassification=true; mechanical_apply=true; cohort_inheritance=false -->
<!-- INVARIANT: registry_is_state_source; orchestrator_owns_selection_semantics; method_pack_owns_per_run_method; planning_lane_never_overrides_reclassification -->

# Investigation Orchestrator

## 1. Mission

Construire une cartographie falsifiable des mécanismes par lesquels des acteurs publics ou privés, domestiques ou étrangers modifient ou cherchent à modifier préférences, perceptions, comportements, élections, institutions ou politiques publiques d'une démocratie.

Qualifier à partir des **mécanismes observables et des preuves**, pas du camp, du statut ou du vocabulaire appliqué à l'acteur. Distinguer participation, influence légitime, persuasion, lobbying, propagande, manipulation, capture, corruption, coercition et ingérence. Mesurer les effets et tester les asymétries de qualification sans chercher à confirmer une théorie générale prédéterminée.

## 2. Invariants probatoires

1. `MECHANISM_FIRST > ACTOR_FIRST`.
2. Toute accusation et tout démenti sont des claims à prouver.
3. Source officielle != vérité interprétative automatique.
4. `funding != command`; `network != coordination`; `proximity != tasking`; `correlation != causality`.
5. `absence_of_evidence != evidence_of_guilt`; `not_found != does_not_exist`.
6. Séparer fait, document, témoignage, accusation, inférence, hypothèse, intention, causalité et effet.
7. Tester activement explications rivales et cas négatifs.
8. Répétitions dérivées d'une même source != corroborations indépendantes.
9. Même standard pour État, médias, ONG, entreprises, plateformes, services, partis, alliés et adversaires.
10. `operation != exposure != persuasion != behavior != democratic/electoral_effect`.
11. `capacity != use`; `dependency != coercion`; `access != adoption`; `legal_design != enforcement`.

## 3. Trois voies seulement

Le registre peut contenir beaucoup de `BACKLOG`, mais l'orchestrateur les traite dans trois voies logiques. La voie est indiquée dans `next_action`; elle est **advisory** et ne remplace jamais le statut canonique ni une reclassification.

```text
A. TRUTH_ENGINE
   PRIMARY|CASE avec contrat complet et CORE_MISSION_V2=PASS
   -> PLAN_TE_NEXT | PLAN_TE_LATER | PLAN_TE_CANDIDATE_NEW

B. SYNTHESIS
   SYNTHESIS, dépendances CLOSED, question/scope complets
   -> dependency-only; jamais Truth Engine ni web générique

C. HOLD / REFRAME
   intérêt contextuel, bundle actor-first, psychologie générale ou mécanisme déjà couvert
   -> aucun run tant qu'un mécanisme/cas/edge nouveau n'est pas isolé
```

`PLAN_TE_NEXT` n'est pas une file d'exécution autoritaire : après chaque fermeture, le gagnant est recalculé selon la règle §5. `PLAN_TE_LATER` signifie seulement « candidat encore matériel à la dernière classification ». `PLAN_REFRAME_HOLD` interdit un lancement dans la forme actuelle.

## 4. CORE_MISSION_V2 — hard gate

Un `PRIMARY|CASE` n'entre dans le pool classable que si **toutes** les conditions suivantes passent :

```text
observable_mechanism = action/chaîne matérielle identifiable ;
democratic_target = préférence, perception, comportement, élection, institution ou politique publique matériellement affectable ;
falsifiable_claim = proposition centrale confirmable, bornable ou réfutable ;
material_evidence_path = pièce primaire, données, contrat/flux, décision, trace technique, archive, dataset ou contradiction exploitable ;
new_value = MECHANISM_DELTA OR DISCRIMINATING_CASE OR SYMMETRY_CONTROL OR EFFECT_EDGE_CLOSURE.
```

Si une condition échoue : `HOLD` logique dans le backlog, pas de lancement. Ne pas transformer automatiquement tout HOLD en `DEFERRED`.

### Actor-first

Un pays, une organisation, un réseau ou une personnalité ne passe que s'il fournit au moins un :

```text
MECHANISM_DELTA
DISCRIMINATING_CASE
SYMMETRY_CONTROL
EFFECT_EDGE_CLOSURE
```

`acteur intéressant`, `acteur puissant` ou `acteur suspect` ne suffit pas.

### Modules contextuels

Sociologie générale, psychologie, histoire ou idéologie sont consommées comme modules causaux/contextuels. Elles ne deviennent `PRIMARY` que si elles ferment une arête observable `acteur/ressource -> action -> cible -> exposition/effet` dans un cas borné.

## 5. Sélection et reclassification

Après chaque fermeture ou changement matériel, la population logique reste le pool complet `BACKLOG|READY PRIMARY|CASE`.

Ordre strict après hard gate :

```text
model_change
> discrimination
> effect_closure
> symmetry_value
> dependency_unlock
> coverage_gap
> utility
```

Tie-break final seulement : ordre canonique du registre. `priority=P1/P2` n'est jamais un critère caché.

### Reclassification incrémentale sûre

1. partir du registre courant + dernière baseline intégrale ;
2. retirer les items sortis, ajouter les nouveaux ;
3. marquer `REVIEW` si contrat/fingerprint change, dépendance impactée ou `reclass_impact` explicite ;
4. `REUSE` seulement si fingerprint + politique + baseline restent valides ;
5. frontière inconnue/globale, baseline absente, politique changée ou ordre canonique dérivé => full-pool intégral ;
6. fusionner REVIEW+REUSE sur **tout** le pool ;
7. ne jamais hériter d'un « current cohort » ;
8. `control.py reclass-plan` borne le travail mais ne remplace jamais le jugement sémantique ;
9. `control.py apply` recalcule mécaniquement le gagnant et refuse un contrat incomplet ;
10. sélectionner au plus un item.

## 6. Priorité scientifique du portefeuille

Une nouvelle investigation Truth Engine n'est créée ou promue que si elle ferme prioritairement l'un de ces goulots :

```text
TASKING        : financeur/État/réseau -> instruction ou contrôle authentifié
POLICY_FOOTPRINT: contribution identifiable -> delta de texte/décision -> adoption
EFFECT         : exposition -> attitude/comportement/décision avec design causal ou quasi-causal
SYMMETRY       : même mécanisme + preuve comparable -> qualification/conséquence comparable ou non
COERCION       : dépendance/capacité -> exercice concret du levier -> coût/options/effet
COORDINATION   : réseau/coappartenance -> action coordonnée documentée -> décision/effet
```

Ne pas ajouter un nouvel ID simplement pour « couvrir un acteur ». Un nouvel ID doit avoir `object_question`, `scope`, falsificateur implicite et voie probatoire dès sa création.

## 7. Synthèses

Une synthèse ne préempte jamais automatiquement un PRIMARY.

Sélection possible seulement si :

```text
all_direct_dependencies = CLOSED
AND CORE_MISSION_V2_synthesis = PASS
AND expected_model_change_or_discrimination = MATERIAL
```

Elle consomme uniquement les handoffs/recoveries bornées des dépendances. Aucun Truth Engine ni web générique.

### Hygiène des dépendances

Un `SYNTHESIS` peut rester bloqué par un `PRIMARY` actuellement `PLAN_REFRAME_HOLD`. **Ne jamais lancer ce PRIMARY uniquement pour débloquer la synthèse.** Deux sorties légales :

1. le PRIMARY est reformulé parce qu'un mécanisme réellement matériel est isolé puis repasse CORE_MISSION_V2 ;
2. une revue explicite du design de synthèse démontre que la dépendance n'est pas nécessaire et modifie le DAG avec trace.

`dependency_unlock` ne sauve jamais un item hors mission.

## 8. Transition et lancement

### PRIMARY|CASE

```text
BACKLOG -> READY
gate = CORE_MISSION_V2_SELECTED_<date>_<artifact>
control.py validate
control.py preflight INV-XXX
control.py run-card INV-XXX
launch only if PASS
READY -> TE_ACTIVE
```

`TE_ACTIVE` signifie propriété du control-plane, jamais exécution en arrière-plan. Aucun autre `PRIMARY|CASE` ne peut être lancé tant que l'actif n'est pas terminal.

### SYNTHESIS

```text
status = BACKLOG
gate = CORE_MISSION_V2_SYNTHESIS_SELECTED_<date>_<artifact>
control.py validate
control.py synthesis-card INV-XXX
execute dependency-only synthesis if PASS
```

Baby-step invariant : au plus un `READY`, `TE_ACTIVE` ou `SYNTHESIS_SELECTED`.

## 9. Runtime

Truth Engine 2.10.6/R3P1 + `METHOD_PACK.md` restent l'autorité par run. Performance work peut supprimer démarrages/processus/tests dupliqués, pas les contrôles sémantiques.

Chemin préféré :

```text
canonical pack SHA check
-> transactional FACTS/tail mutations
-> survival checkpoint
-> PRE once
-> persistence once
-> DELIVERY once
```

Fresh FETCH reste obligatoire pour chaque source web matérielle, même si un handoff fournit un `SOURCE_LEAD`.

## 10. Post-run

```text
Truth Engine artifacts
-> terminal RUN_HANDOFF
   -> central delta + contradictory review + causal ceiling + RENARD
   -> explicit reclass_impact
-> control.py reclass-plan --handoff ...
-> semantic REVIEW rows only
-> routing_reclassification_delta
-> control.py apply
   -> REVIEW+REUSE full-pool coverage
   -> TE_ACTIVE -> CLOSED
   -> winner BACKLOG -> READY
-> replay must be ALREADY_APPLIED
-> validate + preflight winner
-> explicit launch only if requested/authorized
```

`control.py apply` reste mécanique : aucun repair de contrat, aucun score inventé, aucun handoff synthétique.

## 11. Stop rules

Ne pas ouvrir/lancer uniquement pour :

- compléter le graphe ;
- fermer une synthèse finale ;
- accumuler des cas isomorphes ;
- documenter un acteur célèbre sans mécanisme nouveau ;
- confirmer une suspicion sans falsificateur ;
- remplacer un manque de causalité par davantage de contexte ;
- convertir un module psychologique général en « preuve » d'une opération ;
- faire passer un `PLAN_TE_NEXT` devant le gagnant d'une reclassification fraîche.

La priorité reste : **découvrir, falsifier et mesurer les mécanismes qui affectent réellement le fonctionnement démocratique**.
