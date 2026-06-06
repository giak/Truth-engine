# SUBLIMATOR v33.1 — Design

**Date** : 2026-06-06
**Statut** : Design validé, pré-spéc
**Base** : v33.0 (9 agents, 7 gates G0-G6, 12 LOIS)
**Type** : Mineur (rétrocompatible)

## Contexte et motivation

SUBLIMATOR v33.0 est un pipeline full-auto (9 agents, 7 gates, 12 LOIS) qui produit des articles longs via 7 phases (§0 à §6). Test live Sumer/France 2026 : 7/7 gates PASS, article publié (4233 mots, 27 125 chars).

**Problème identifié** : aucune intervention humaine entre les phases productives. §2 (dialecticien) propose 3 thèses sans demander direction, §3 (architecte) construit la chaîne narrative tout seul. L'article publié n'exploite qu'une enquête (Sumer) sur 13 mappées. L'humain ne peut ni pivoter la thèse cardinale, ni réagencer le plan, ni enrichir avec des inputs externes.

**Objectif v33.1** : introduire 3 checkpoints structurés (§0, §2, §3) pour transformer le pipeline full-auto en pipeline **semi-auto à décisions humaines sémantiques**.

## Décisions clés (validées par brainstorming)

| # | Décision | Choix |
|---|----------|-------|
| 1 | Localisation des checkpoints | §0, §2, §3 (3 points) |
| 2 | Actions disponibles | Valider / Modifier / Refuser / Enrichir (4) |
| 3 | Politique d'obligation | Obligatoire et bloquant (pas de skip, pas de timeout) |
| 4 | Format d'interaction | Question tool pur (V/M/R/E + sous-question texte) |
| 5 | Refus répété | Boucle bornée 3 max consécutifs → halte pipeline + bilan |
| 6 | Persistance | Slot `checkpoints` dans state_*.yaml |
| 7 | Cascade | §0 modifié = reset total, §2 = reset §3-§6, §3 = reset §4-§6 |
| 8 | LOIS ajoutées | L13 (CP obligatoire), L14 (boucle bornée 3 max) |
| 9 | Rétrocompat | state v33.0 sans slot `checkpoints` → fallback V |
| 10 | Versionning | v33.0 → v33.1 (mineur, rétrocompat) |

## Section 1 — Architecture

**Insertion des checkpoints dans le pipeline v33.0 existant**

```
Phase 0 ─┬─→ Censeur ──────────→ [CHECKPOINT §0] ─→ Corpus-Consultant ─┐
         │   (profil/portée)        V/M/R/E           (saturation)      │
         │                                                            │
         ▼                                                            ▼
       G0 ✓                                                       G1 ✓
                                                                       │
Phase 2 ──→ Dialecticien ──→ [CHECKPOINT §2] ──→ Architecte ─────────┐│
              (3 thèses)          V/M/R/E         (chaîne)         ││
                                                                 ││
            G2 ✓                                                  ▼▼
Phase 3 ──→ [CHECKPOINT §3] ──→ Fact-Checker ──→ Rédacteur ────→ ...
              V/M/R/E             (verif)         (draft)
```

**Trois points d'insertion clés** :

1. **§0 → G0** : le censeur propose profil + portée + plan adaptatif. L'humain arbitre **avant** que corpus-consultant ne commence son inventaire. Évite 30 secondes de travail inutile si l'humain veut pivoter.

2. **§2 → G2** : dialecticien produit 3 thèses (cardinale + 2 secondaires). L'humain peut **renverser la cardinale** (rare) ou **imposer une 4e thèse** (fréquent). C'est le point le plus stratégique : la thèse cardinale détermine la structure §3.

3. **§3 → G3** : architecte propose chaîne narrative (8 sections, intro, mapping_table). L'humain peut **réordonner**, **renforcer une section faible**, ou **ajouter une section manquante**. Coût d'erreur maximal si on saute ce checkpoint (réécrire le draft coûte 5x plus cher que réécrire le plan).

**Les autres gates G1, G4, G5, G6 restent automatiques.** Pas de checkpoint en §1 (saturation), §4 (fact-check), §5 (drafting) — c'est de l'exécution.

## Section 2 — Composants (4 actions V/M/R/E)

**Structure uniforme pour les 3 checkpoints** (le format est identique en §0, §2, §3) :

### 1. Valider
- L'agent continue avec la sortie actuelle
- Trace : `audit_log.append({phase: "CP1", action: "validate", actor: "user", ...})`
- Effet : passage à la phase suivante

### 2. Modifier
- L'agent pose une **sous-question structurée** : "Colle ta version modifiée de [thèse/plan/portée]"
- L'humain colle du texte libre OU du YAML structuré
- L'agent remplace sa sortie par la version humaine
- Trace : `action: "modify", payload_size: <n>, n_corrections: <count>`
- Effet : la phase reprend avec le nouvel input, recalcul des gates si impact

### 3. Refuser
- L'agent retourne à la phase précédente
- **Incrémente `n_refus_consecutifs`** pour ce checkpoint
- Trace : `action: "refuse", n_refus_consecutifs: <n>`
- Effet : retry de la phase (max 3) **avec de nouveaux inputs** : l'agent régénère sa sortie depuis zéro (les outputs précédents sont invalidés) puis re-pose le checkpoint. L'humain peut ensuite V/M/R/E comme à l'itération précédente.

### 4. Enrichir
- L'agent pose une **sous-question structurée** : "Colle tes ajouts (F### externes, thèses supplémentaires, sections à ajouter)"
- L'humain colle du YAML/texte
- L'agent **fusionne** ses outputs + ajouts (sans remplacer)
- Trace : `action: "enrich", n_inputs_added: <count>`
- Effet : la phase reprend avec inputs augmentés

**Question type au checkpoint** (template) :
```
L'agent a produit [description courte].
Options :
1. Valider — continuer avec cette sortie
2. Modifier — coller ta version
3. Refuser — retour à [phase précédente]
4. Enrichir — ajouter des inputs
```

**Mécanisme de boucle bornée** :
- Compteur `n_refus_consecutifs` reset à 0 sur V/M/E
- Si `n_refus_consecutifs == 3` → stop pipeline + bilan : "3 refus consécutifs, intervention manuelle requise"

## Section 3 — Data Flow

**Cascade des outputs humains à travers le pipeline**

Le principe : chaque output (agent ou humain) est persisté dans `state_*.yaml`, et le downstream agent lit en priorité la version humaine.

### Schéma de stockage

```yaml
# Extrait de state_sumer-v33-XXX.yaml
artifacts:
  censeur_output: { profil: "A", portee: [...], plan_adaptatif: [...] }  # brut agent
  dialecticien_output: { theses: [...], cardinale: "SYSTEME" }
  architecte_output: { sections: [...], mapping_table: [...] }

# Slots humains (ajoutés par le mécanisme checkpoint)
checkpoints:
  cp1_§0:
    phase: "§0"
    agent_output_ref: "censeur_output"
    human_action: "validate"  # validate | modify | refuse | enrich
    human_output: null        # null si V/R, objet si M/E
    n_refus_consecutifs: 0
    timestamp: "2026-06-06T08:00:00Z"
  cp2_§2:
    phase: "§2"
    agent_output_ref: "dialecticien_output"
    human_action: "modify"
    human_output: { theses: [...], cardinale: "AUTRE" }  # remplace l'output agent
    n_refus_consecutifs: 0
  cp3_§3:
    phase: "§3"
    agent_output_ref: "architecte_output"
    human_action: "enrich"
    human_output: { sections_ajoutees: ["§9 Andurarum"], ... }  # fusionné
    n_refus_consecutifs: 0
```

### Règle de lecture (downstream)

```python
def get_effective_output(phase):
    cp = state[f"checkpoints.cp_{phase}"]
    if cp.human_action == "validate":
        return state[f"artifacts.{cp.agent_output_ref}"]
    elif cp.human_action == "modify":
        return cp.human_output  # version humaine
    elif cp.human_action == "enrich":
        return merge(state[f"artifacts.{cp.agent_output_ref}"], cp.human_output)
    elif cp.human_action == "refuse":
        raise HaltError("refus, phase en retry")
```

### Cascade des checkpoints

| Checkpoint | Impact aval |
|---|---|
| **§0** modifié | Tout le pipeline (portée changée) → reset §1 à §6 |
| **§2** modifié | §1 OK (déjà passé), §3 reprend avec nouvelle cardinale, §4-§6 cascadent |
| **§3** modifié | §1, §2 OK, §4 reprend avec nouveau plan, §5-§6 cascadent |

### Audit log

Chaque checkpoint ajoute 1-2 events NDJSON :
```ndjson
{"event":"checkpoint","phase":"§2","action":"modify","n_refus_consecutifs":0,"actor":"user","timestamp":"..."}
{"event":"checkpoint_input","phase":"§2","field":"cardinale","old":"SYSTEME","new":"AUTRE","timestamp":"..."}
```

## Section 4 — Error handling + Testing + Migration

### Error handling

| Cas | Comportement |
|---|---|
| **3 refus consécutifs au même CP** | Stop pipeline + bilan : "3 refus sur CP_X, intervention manuelle requise. État figé." État préservé pour reprise manuelle. |
| **Phase échoue après modif humaine** | Halte explicite : "Votre modif de CP_X a cassé la phase Y. Voici l'erreur : [trace]. Options : (1) Revenir à l'output agent, (2) Re-modifier, (3) Abandonner." |
| **Phase échoue après enrich humain** | Idem, avec diff montrant ce que l'enrich a ajouté. L'agent isole le chunk fautif. |
| **Audit log corrompu** | Halte immédiat, intégrité critique. Pas de reprise. |
| **L'humain ne répond pas** | Pas de timeout (checkpoints obligatoires et bloquants). L'humain répond quand il veut. |
| **Modification/Enrich hors format** | Halte : "Format attendu : [YAML/texte]. Reprise avec format correct." |

### Testing

**3 niveaux de tests** :

1. **Tests unitaires des 4 actions sur chaque CP** (12 cas minimum) :
   - CP1-§0 × {V, M, R, E}
   - CP2-§2 × {V, M, R, E}
   - CP3-§3 × {V, M, R, E}
   - Critères : n_refus_consecutifs, cascade, audit_log entries

2. **Tests d'intégration de la cascade** :
   - Modifier §2 → vérifier que §3 recalcule
   - Enrichir §3 → vérifier que §4 utilise mapping_table augmentée
   - 3 refus → vérifier halte + bilan

3. **Test e2e avec humain simulé** :
   - Scénario nominal : V × 3 → article publié
   - Scénario pivot : M en §2 → recalcul §3
   - Scénario stop : R × 3 en §2 → halte

### Migration v33.0 → v33.1

**Diff conceptuel** :
- v33.0 : 9 agents, 7 gates G0-G6, 12 LOIS
- v33.1 : +3 checkpoints (CP1, CP2, CP3), +2 LOIS (L13, L14), +1 slot state (checkpoints)

**Rétrocompatibilité** :
- state_*.yaml v33.0 sans slot `checkpoints` → fallback CP validate (pas d'interférence)
- Runtime config v33.0 → v33.1 par défaut, opt-in pour anciens runs

**Nouvelles LOIS** :
- **L13** (CP obligatoire) : "Tout pipeline SUBLIMATOR DOIT soumettre les outputs des phases §0, §2, §3 à validation humaine via checkpoint structuré avant passage à la phase suivante."
- **L14** (boucle bornée) : "Un même checkpoint ne peut être refusé plus de 3 fois consécutivement. Au 4e cycle, halte pipeline."

**Versionning** : v33.0 → v33.1 (mineur, pas majeur car rétrocompat).

## Notes ouvertes

1. **Compatibilité agents arrière-plan** : si l'agent est dispatché en arrière-plan, comment les checkpoints fonctionnent ? Décision : hors scope v33.1, traité en v33.2+ si besoin.

2. **Reprise manuelle après halte** : pas de mécanisme de reprise automatique depuis état figé. L'humain doit redémarrer le pipeline avec un nouveau session_id. Décision : acceptable pour v33.1 (l'halte est exceptionnelle).

3. **Merge enrich** : stratégie de fusion non spécifiée pour cas complexes (champs qui se contredisent). Décision : LLM fait le merge, en cas de contradiction il demande clarification (halte + sous-question).

4. **Test live v33.1 sur Sumer** : le pipeline Sumer v33.0 a déjà produit un article. v33.1 devrait produire un MEILLEUR article en permettant à l'humain d'enrichir §2 avec la thèse multi-civilisationnelle (Rome, Chine, Andurarum). Validation A/B possible.

