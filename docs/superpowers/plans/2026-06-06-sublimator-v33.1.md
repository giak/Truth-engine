# SUBLIMATOR v33.1 — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ajouter 3 checkpoints structurés (§0, §2, §3) avec 4 actions (V/M/R/E) au pipeline SUBLIMATOR v33.0, en maintenant la rétrocompatibilité.

**Architecture:** Modification incrémentale de `SUBLIMATOR_v33.0_spec_agent.md` → `SUBLIMATOR_v33.1_spec_agent.md`. Ajout de 2 LOIS (L13, L14), section §10 CHECKPOINTS, slot `checkpoints` dans le schéma d'état, diagramme topologique mis à jour. Mécanisme obligatoire et bloquant, boucle bornée 3 max.

**Tech Stack:** Markdown + YAML déclaratif, Mermaid (frontmatter v11.14+, base theme), aucun code applicatif. Tests = validation YAML + cohérence structurelle.

**Base spec:** `/home/giak/projects/truth-engine/tools/engines/SUBLIMATOR_v33.0_spec_agent.md` (1156 lignes, 9 agents, 7 gates, 12 LOIS)

**Design source:** `/home/giak/projects/truth-engine/tools/engines/SUBLIMATOR_v33.1_design.md` (230 lignes, 4 sections validées)

---

## File Structure

**Fichiers créés** :
- `tools/engines/SUBLIMATOR_v33.1_spec_agent.md` (nouvelle spec, 1156+ lignes)
- `tools/engines/SUBLIMATOR_v33.1_GUIDE_HUMAN.md` (nouveau guide, 1406+ lignes)
- `docs/superpowers/plans/2026-06-06-sublimator-v33.1.md` (ce plan)

**Fichiers modifiés** :
- `AGENTS.md` (section Engines, ajout v33.1)

**Fichiers archivés** (renommage) :
- `SUBLIMATOR_v33.0_spec_agent.md` → `SUBLIMATOR_v33.0_spec_agent.md.bak`
- `SUBLIMATOR_v33.0_GUIDE_HUMAN.md` → `SUBLIMATOR_v33.0_GUIDE_HUMAN.md.bak`

---

## Task 1 : Backup de la spec v33.0

**Files:**
- Rename: `tools/engines/SUBLIMATOR_v33.0_spec_agent.md` → `tools/engines/SUBLIMATOR_v33.0_spec_agent.md.bak`
- Rename: `tools/engines/SUBLIMATOR_v33.0_GUIDE_HUMAN.md` → `SUBLIMATOR_v33.0_GUIDE_HUMAN.md.bak`

- [ ] **Step 1 : Renommer les deux fichiers v33.0**

```bash
cd /home/giak/projects/truth-engine
mv tools/engines/SUBLIMATOR_v33.0_spec_agent.md tools/engines/SUBLIMATOR_v33.0_spec_agent.md.bak
mv tools/engines/SUBLIMATOR_v33.0_GUIDE_HUMAN.md tools/engines/SUBLIMATOR_v33.0_GUIDE_HUMAN.md.bak
```

- [ ] **Step 2 : Vérifier que les backups existent**

```bash
ls -la /home/giak/projects/truth-engine/tools/engines/SUBLIMATOR_v33.0*.bak
```

Attendu : 2 fichiers `.bak` avec tailles 41.8K et 65.8K

- [ ] **Step 3 : Commit**

```bash
cd /home/giak/projects/truth-engine
git add tools/engines/
git commit -m "chore: backup SUBLIMATOR v33.0 spec and guide before v33.1 refactor"
```

---

## Task 2 : Créer le skeleton de la spec v33.1

**Files:**
- Create: `tools/engines/SUBLIMATOR_v33.1_spec_agent.md` (copie de v33.0 + 1ère modif mineure)

- [ ] **Step 1 : Copier v33.0 → v33.1**

```bash
cd /home/giak/projects/truth-engine
cp tools/engines/SUBLIMATOR_v33.0_spec_agent.md.bak tools/engines/SUBLIMATOR_v33.1_spec_agent.md
```

- [ ] **Step 2 : Modifier le H1 (titre du document)**

Remplacer dans le fichier `tools/engines/SUBLIMATOR_v33.1_spec_agent.md` la première ligne :
```
# SUBLIMATOR v33.0 — Spécification agent
```
par :
```
# SUBLIMATOR v33.1 — Spécification agent
```

- [ ] **Step 3 : Modifier la date de version dans le frontmatter YAML**

Trouver dans le frontmatter YAML (lignes 1-10) :
```yaml
version: "33.0"
```
remplacer par :
```yaml
version: "33.1"
```

- [ ] **Step 4 : Modifier la description dans le frontmatter**

Remplacer dans le frontmatter :
```yaml
description: "Pipeline full-auto 9 agents, 7 gates G0-G6, 12 LOIS, dédié à la production d'articles longs (4000-5000 mots) pour Substack"
```
par :
```yaml
description: "Pipeline semi-auto 9 agents + 3 checkpoints structurés (§0, §2, §3), 7 gates G0-G6, 14 LOIS, dédié à la production d'articles longs (4000-5000 mots) pour Substack"
```

- [ ] **Step 5 : Vérifier la structure de base**

```bash
cd /home/giak/projects/truth-engine
head -10 tools/engines/SUBLIMATOR_v33.1_spec_agent.md
wc -l tools/engines/SUBLIMATOR_v33.1_spec_agent.md
```

Attendu : titre "v33.1", frontmatter modifié, ~1156 lignes

- [ ] **Step 6 : Commit**

```bash
cd /home/giak/projects/truth-engine
git add tools/engines/SUBLIMATOR_v33.1_spec_agent.md
git commit -m "feat(spec): create v33.1 skeleton from v33.0 backup"
```

---

## Task 3 : Ajouter LOIS L13 et L14 dans §3.2

**Files:**
- Modify: `tools/engines/SUBLIMATOR_v33.1_spec_agent.md` (section §3.2, après L12)

- [ ] **Step 1 : Localiser §3.2 ligne 455**

```bash
cd /home/giak/projects/truth-engine
grep -n "L12" tools/engines/SUBLIMATOR_v33.1_spec_agent.md
```

Attendu : numéro de ligne de L12 (probablement vers 480-500)

- [ ] **Step 2 : Ajouter L13 et L14 après L12**

Trouver le bloc YAML de L12 (probablement) :
```yaml
  - id: L12
    text: "..."
```

Ajouter APRÈS ce bloc (et avant le commentaire de fermeture de la liste LOIS) :
```yaml
  - id: L13
    text: "Tout pipeline SUBLIMATOR DOIT soumettre les outputs des phases §0, §2, §3 à validation humaine via checkpoint structuré avant passage à la phase suivante. Format : question tool V/M/R/E + sous-question texte. Pas de skip, pas de timeout."
    canal: les_deux
    test: lint_orchestrateur.validates_checkpoints_presence()
  - id: L14
    text: "Un même checkpoint ne peut être refusé plus de 3 fois consécutivement. Au 4e cycle, halte pipeline + bilan explicite. Compteur n_refus_consecutifs reset à 0 sur V/M/E."
    canal: les_deux
    test: orchestrateur.borne_refus(3)
```

- [ ] **Step 3 : Vérifier le décompte LOIS**

```bash
cd /home/giak/projects/truth-engine
grep -cE "^  - id: L[0-9]+" tools/engines/SUBLIMATOR_v33.1_spec_agent.md
```

Attendu : 14

- [ ] **Step 4 : Valider YAML**

```bash
cd /home/giak/projects/truth-engine
python3 -c "
import yaml
with open('tools/engines/SUBLIMATOR_v33.1_spec_agent.md') as f:
    content = f.read()
parts = content.split('---')
for i, p in enumerate(parts[1:], 1):
    try:
        yaml.safe_load(p)
    except yaml.YAMLError as e:
        print(f'YAML {i} ERROR: {e}')
        break
else:
    print('All YAML blocks valid')
"
```

Attendu : "All YAML blocks valid"

- [ ] **Step 5 : Commit**

```bash
cd /home/giak/projects/truth-engine
git add tools/engines/SUBLIMATOR_v33.1_spec_agent.md
git commit -m "feat(spec): add LOIS L13 (checkpoints obligatoires) and L14 (boucle bornee 3 max)"
```

---

## Task 4 : Modifier §4.2 schéma d'état (slot checkpoints)

**Files:**
- Modify: `tools/engines/SUBLIMATOR_v33.1_spec_agent.md` (section §4.2 ligne 748)

- [ ] **Step 1 : Localiser §4.2**

```bash
cd /home/giak/projects/truth-engine
grep -n "### 4.2 Schéma" tools/engines/SUBLIMATOR_v33.1_spec_agent.md
```

Attendu : ligne 748

- [ ] **Step 2 : Ajouter le slot checkpoints dans le YAML du schéma d'état**

Trouver le bloc YAML du schéma d'état (probablement lignes 750-780) et ajouter APRÈS les slots existants :
```yaml
  checkpoints:
    cp1_§0:
      phase: "§0"
      agent_output_ref: "censeur_output"
      human_action: "validate"  # validate | modify | refuse | enrich
      human_output: null
      n_refus_consecutifs: 0
      timestamp: "ISO8601"
    cp2_§2:
      phase: "§2"
      agent_output_ref: "dialecticien_output"
      human_action: "validate"
      human_output: null
      n_refus_consecutifs: 0
      timestamp: "ISO8601"
    cp3_§3:
      phase: "§3"
      agent_output_ref: "architecte_output"
      human_action: "validate"
      human_output: null
      n_refus_consecutifs: 0
      timestamp: "ISO8601"
```

- [ ] **Step 3 : Documenter la règle de lecture dans le texte après le YAML**

Ajouter un paragraphe après le bloc YAML :
```
**Règle de lecture downstream** : pour une phase X ayant un CP, l'agent aval utilise `state.checkpoints.cpX.human_output` (si M/E) ou `state.artifacts.{ref}` (si V). Si R, l'agent amont régénère sa sortie.
```

- [ ] **Step 4 : Valider YAML**

```bash
cd /home/giak/projects/truth-engine
python3 -c "
import yaml
with open('tools/engines/SUBLIMATOR_v33.1_spec_agent.md') as f:
    parts = f.read().split('---')
for i, p in enumerate(parts[1:], 1):
    try: yaml.safe_load(p)
    except yaml.YAMLError as e: print(f'YAML {i} ERROR: {e}'); break
else: print('OK')
"
```

Attendu : "OK"

- [ ] **Step 5 : Commit**

```bash
cd /home/giak/projects/truth-engine
git add tools/engines/SUBLIMATOR_v33.1_spec_agent.md
git commit -m "feat(spec): add checkpoints slot to state schema §4.2"
```

---

## Task 5 : Modifier §4.4 stratégie d'échec (boucle bornée)

**Files:**
- Modify: `tools/engines/SUBLIMATOR_v33.1_spec_agent.md` (section §4.4 ligne 795)

- [ ] **Step 1 : Localiser §4.4**

```bash
cd /home/giak/projects/truth-engine
grep -n "### 4.4" tools/engines/SUBLIMATOR_v33.1_spec_agent.md
```

Attendu : ligne 795

- [ ] **Step 2 : Ajouter une section "Boucle bornée des checkpoints"**

Trouver la fin de la stratégie d'échec (avant §4.5) et ajouter :
```
#### 4.4.bis Boucle bornée des checkpoints (L14)

Tout checkpoint CPX a un compteur `n_refus_consecutifs` initialisé à 0.

À chaque action humaine sur CPX :
- `validate` → n_refus_consecutifs := 0, CPX validé, passage phase suivante
- `modify` → n_refus_consecutifs := 0, agent reprend avec human_output
- `refuse` → n_refus_consecutifs += 1
  - Si n_refus_consecutifs < 3 : agent régénère sortie CPX, re-pose checkpoint
  - Si n_refus_consecutifs == 3 : HALTE pipeline, bilan figé
- `enrich` → n_refus_consecutifs := 0, agent fusionne + human_output

Condition de halte :
```yaml
halte:
  condition: "n_refus_consecutifs[CPX] >= 3"
  effet: "Bilan explicite : '3 refus consécutifs sur CPX, intervention manuelle requise. État figé pour reprise manuelle.'"
```
```

- [ ] **Step 3 : Commit**

```bash
cd /home/giak/projects/truth-engine
git add tools/engines/SUBLIMATOR_v33.1_spec_agent.md
git commit -m "feat(spec): add §4.4.bis boucle bornee checkpoints (L14)"
```

---

## Task 6 : Modifier §4.7 audit log (format checkpoint)

**Files:**
- Modify: `tools/engines/SUBLIMATOR_v33.1_spec_agent.md` (section §4.7 ligne 840)

- [ ] **Step 1 : Localiser §4.7**

```bash
cd /home/giak/projects/truth-engine
grep -n "### 4.7" tools/engines/SUBLIMATOR_v33.1_spec_agent.md
```

Attendu : ligne 840

- [ ] **Step 2 : Ajouter 2 nouveaux types d'events au format NDJSON**

Trouver le bloc qui définit les types d'events et ajouter :
```yaml
  - type: checkpoint
    schema:
      event: "checkpoint"
      phase: "§0|§2|§3"
      action: "validate|modify|refuse|enrich"
      n_refus_consecutifs: int
      actor: "user"
      timestamp: "ISO8601"
  - type: checkpoint_input
    schema:
      event: "checkpoint_input"
      phase: "§0|§2|§3"
      field: "string"  # ex: "cardinale", "sections[3]", "portee.n_investigations"
      old: any
      new: any
      timestamp: "ISO8601"
```

- [ ] **Step 3 : Commit**

```bash
cd /home/giak/projects/truth-engine
git add tools/engines/SUBLIMATOR_v33.1_spec_agent.md
git commit -m "feat(spec): add checkpoint and checkpoint_input events to audit log §4.7"
```

---

## Task 7 : Modifier §5 topologie (3 CP dans le graphe)

**Files:**
- Modify: `tools/engines/SUBLIMATOR_v33.1_spec_agent.md` (section §5.1, §5.3 si graphe mermaid)

- [ ] **Step 1 : Localiser §5.1**

```bash
cd /home/giak/projects/truth-engine
grep -n "### 5.1\|### 5.3" tools/engines/SUBLIMATOR_v33.1_spec_agent.md
```

Attendu : §5.1 ligne 873, §5.3 ligne 891

- [ ] **Step 2 : Ajouter une sous-section "5.1.bis Checkpoints"**

Trouver la fin de §5.1 (avant §5.2 Légende) et ajouter :
```
#### 5.1.bis Checkpoints (CP1, CP2, CP3)

Trois points d'insertion bloquants dans le pipeline :

| CP | Phase amont | Phase aval | Slot state | Sortie validée |
|----|-------------|------------|------------|----------------|
| CP1 | Censeur (§0) | Corpus-Consultant (§1) | `checkpoints.cp1_§0` | `censeur_output` |
| CP2 | Dialecticien (§2) | Architecte (§3) | `checkpoints.cp2_§2` | `dialecticien_output` |
| CP3 | Architecte (§3) | Fact-Checker (§4) | `checkpoints.cp3_§3` | `architecte_output` |

Pas de checkpoint en §1 (saturation auto), §4 (fact-check auto), §5 (drafting auto), §6 (audit/auto).
```

- [ ] **Step 3 : Si un diagramme mermaid existe dans §5.3, ajouter 3 nœuds CP**

Note : §5.3 traite du parallélisme, pas du graphe principal. Le graphe principal est probablement dans §5.1 ou ailleurs. Si aucun diagramme mermaid n'existe dans §5, créer un diagramme simple :

Insérer après §5.1.bis :
```mermaid
---
title: SUBLIMATOR v33.1 — Topologie avec checkpoints
config:
  theme: base
  themeVariables:
    primaryColor: "#fff5e6"
    primaryBorderColor: "#d4a017"
---
flowchart LR
    P0["§0 Censeur"]:::phase --> CP1{{"CP1<br/>V/M/R/E"}}:::cp
    CP1 --> P1["§1 Corpus"]:::phase
    P1 --> G1[/"G1"/]:::gate
    G1 --> P2["§2 Dialecticien"]:::phase
    P2 --> CP2{{"CP2<br/>V/M/R/E"}}:::cp
    CP2 --> P3["§3 Architecte"]:::phase
    P3 --> CP3{{"CP3<br/>V/M/R/E"}}:::cp
    CP3 --> P4["§4 Fact-Check"]:::phase
    P4 --> G4[/"G4"/]:::gate
    G4 --> P5["§5 Rédacteur"]:::phase
    P5 --> P6["§6 Audit"]:::phase

    classDef phase fill:#e6f0ff,stroke:#0066cc
    classDef cp fill:#fff5e6,stroke:#d4a017,stroke-width:3px
    classDef gate fill:#e6ffe6,stroke:#009900
```

- [ ] **Step 4 : Commit**

```bash
cd /home/giak/projects/truth-engine
git add tools/engines/SUBLIMATOR_v33.1_spec_agent.md
git commit -m "feat(spec): add §5.1.bis checkpoints table and mermaid topology"
```

---

## Task 8 : Créer §10 CHECKPOINTS (section dédiée)

**Files:**
- Modify: `tools/engines/SUBLIMATOR_v33.1_spec_agent.md` (ajout section §10 à la fin, avant ou après §9 CHANGELOG)

- [ ] **Step 1 : Localiser la fin de la spec**

```bash
cd /home/giak/projects/truth-engine
tail -30 tools/engines/SUBLIMATOR_v33.1_spec_agent.md
```

- [ ] **Step 2 : Ajouter §10 CHECKPOINTS à la fin**

Ajouter avant `## §9 CHANGELOG` (ou après, peu importe l'ordre — la numérotation suit la date d'ajout) :
```markdown
## §10 CHECKPOINTS (v33.1+)

### 10.1 Principe

Les 3 checkpoints (CP1 §0, CP2 §2, CP3 §3) sont des points d'insertion **obligatoires et bloquants** où l'humain arbitre la sortie de l'agent amont avant passage à l'agent aval. Implémentés via question tool, format V/M/R/E.

### 10.2 Les 4 actions

#### Valider (V)
- L'agent continue avec la sortie actuelle
- Trace : `{"event":"checkpoint","phase":"§X","action":"validate",...}`
- Effet : passage à la phase suivante

#### Modifier (M)
- L'agent pose : "Colle ta version modifiée"
- L'humain colle texte libre OU YAML structuré
- L'agent remplace sa sortie par la version humaine
- Trace : `{"event":"checkpoint","action":"modify","payload_size":N,...}`
- Effet : phase reprend avec nouvel input, recalcul gates si impact

#### Refuser (R)
- L'agent retourne à la phase précédente
- `n_refus_consecutifs += 1`
- Trace : `{"event":"checkpoint","action":"refuse","n_refus_consecutifs":N,...}`
- Effet : retry phase avec **nouveaux inputs** (sortie précédente invalidée), max 3

#### Enrichir (E)
- L'agent pose : "Colle tes ajouts (F### externes, thèses, sections)"
- L'humain colle YAML/texte
- L'agent **fusionne** (sans remplacer) ses outputs + ajouts
- Trace : `{"event":"checkpoint","action":"enrich","n_inputs_added":N,...}`
- Effet : phase reprend avec inputs augmentés

### 10.3 Boucle bornée (L14)

Compteur `n_refus_consecutifs` reset à 0 sur V/M/E. Si == 3 → HALTE pipeline + bilan.

### 10.4 Cascade

| CP modifié | Impact aval |
|---|---|
| §0 | Reset §1 à §6 (portée changée) |
| §2 | §1 OK, reset §3 à §6 (nouvelle cardinale) |
| §3 | §1, §2 OK, reset §4 à §6 (nouveau plan) |

### 10.5 Question type (template)

```
L'agent a produit [description courte, 2-3 phrases].

Options :
1. Valider — continuer avec cette sortie
2. Modifier — coller ta version
3. Refuser — retour à [phase précédente]
4. Enrichir — ajouter des inputs
```

### 10.6 Rétrocompatibilité

state_*.yaml v33.0 sans slot `checkpoints` → fallback CP validate (aucune interférence). Les runs anciens continuent de fonctionner comme v33.0.
```

- [ ] **Step 3 : Valider YAML**

```bash
cd /home/giak/projects/truth-engine
python3 -c "
import yaml
with open('tools/engines/SUBLIMATOR_v33.1_spec_agent.md') as f:
    parts = f.read().split('---')
for i, p in enumerate(parts[1:], 1):
    try: yaml.safe_load(p)
    except yaml.YAMLError as e: print(f'YAML {i} ERROR: {e}'); break
else: print('OK')
"
```

Attendu : "OK"

- [ ] **Step 4 : Commit**

```bash
cd /home/giak/projects/truth-engine
git add tools/engines/SUBLIMATOR_v33.1_spec_agent.md
git commit -m "feat(spec): add §10 CHECKPOINTS section (v33.1 feature)"
```

---

## Task 9 : Mettre à jour CHANGELOG §9 (entry v33.1)

**Files:**
- Modify: `tools/engines/SUBLIMATOR_v33.1_spec_agent.md` (section §9, début)

- [ ] **Step 1 : Localiser §9**

```bash
cd /home/giak/projects/truth-engine
grep -n "## §9 CHANGELOG" tools/engines/SUBLIMATOR_v33.1_spec_agent.md
```

- [ ] **Step 2 : Ajouter l'entry v33.1 en tête du CHANGELOG**

Trouver la première ligne de §9 (probablement `## §9 CHANGELOG`) et ajouter APRÈS l'entry existante v33.0 :
```markdown

### v33.1 (2026-06-06)

**Type** : Mineur (rétrocompatible)

**Nouveautés** :
- 3 checkpoints structurés (CP1 §0, CP2 §2, CP3 §3) avec 4 actions V/M/R/E
- 2 nouvelles LOIS : L13 (CP obligatoire), L14 (boucle bornée 3 max)
- Slot `checkpoints` dans le schéma d'état §4.2
- Section §10 CHECKPOINTS dédiée
- Diagramme topologique §5.1.bis avec 3 CP

**Migration** :
- state_*.yaml v33.0 → fallback CP validate, aucune action requise
- Spec v33.0 archivée en `.bak`

**Breaking changes** : aucun
```

- [ ] **Step 3 : Commit**

```bash
cd /home/giak/projects/truth-engine
git add tools/engines/SUBLIMATOR_v33.1_spec_agent.md
git commit -m "docs(spec): add v33.1 entry to CHANGELOG §9"
```

---

## Task 10 : Copier et adapter GUIDE_HUMAN v33.1

**Files:**
- Create: `tools/engines/SUBLIMATOR_v33.1_GUIDE_HUMAN.md` (copie v33.0 + ajouts)

- [ ] **Step 1 : Copier v33.0 → v33.1**

```bash
cd /home/giak/projects/truth-engine
cp tools/engines/SUBLIMATOR_v33.0_GUIDE_HUMAN.md.bak tools/engines/SUBLIMATOR_v33.1_GUIDE_HUMAN.md
```

- [ ] **Step 2 : Modifier le H1**

Remplacer dans `tools/engines/SUBLIMATOR_v33.1_GUIDE_HUMAN.md` :
```
# SUBLIMATOR v33.0 — Guide humain
```
par :
```
# SUBLIMATOR v33.1 — Guide humain
```

- [ ] **Step 3 : Vérifier la copie**

```bash
cd /home/giak/projects/truth-engine
head -5 tools/engines/SUBLIMATOR_v33.1_GUIDE_HUMAN.md
wc -l tools/engines/SUBLIMATOR_v33.1_GUIDE_HUMAN.md
```

Attendu : titre "v33.1", ~1406 lignes

- [ ] **Step 4 : Commit**

```bash
cd /home/giak/projects/truth-engine
git add tools/engines/SUBLIMATOR_v33.1_GUIDE_HUMAN.md
git commit -m "feat(guide): create v33.1 skeleton from v33.0 backup"
```

---

## Task 11 : Ajouter section Checkpoints dans GUIDE_HUMAN

**Files:**
- Modify: `tools/engines/SUBLIMATOR_v33.1_GUIDE_HUMAN.md` (ajout section §X, entre §9 et §10)

- [ ] **Step 1 : Localiser la fin du guide**

```bash
cd /home/giak/projects/truth-engine
grep -n "^## " tools/engines/SUBLIMATOR_v33.1_GUIDE_HUMAN.md
```

Attendu : §0 à §15 (16 sections, 1406 lignes)

- [ ] **Step 2 : Ajouter §X Checkpoints (entre §9 et §10)**

Trouver la fin de §9 et insérer avant §10 :
```markdown
## §9.5 Checkpoints humains (v33.1+)

### Quand l'humain intervient

À **3 moments** du pipeline, l'agent s'arrête et demande une décision humaine via question tool :

| Checkpoint | Phase amont | Question type |
|------------|-------------|---------------|
| **CP1** | §0 Censeur (profil/portée) | "Quel profil/portée veux-tu ?" |
| **CP2** | §2 Dialecticien (3 thèses) | "Quelle thèse cardinale ?" |
| **CP3** | §3 Architecte (chaîne 8 sections) | "Quel plan narratif ?" |

### Les 4 actions

L'agent pose systématiquement la question :

```
L'agent a produit [description courte].

Options :
1. Valider — continuer avec cette sortie
2. Modifier — coller ta version
3. Refuser — retour à [phase précédente]
4. Enrichir — ajouter des inputs
```

**Valider** = OK, on continue. **Modifier** = tu colles ta propre version, l'agent l'utilise. **Refuser** = retour à la phase précédente (max 3 fois). **Enrichir** = tu ajoutes des inputs (F### externes, thèses, sections), l'agent fusionne.

### Boucle bornée

Si tu refuses 3 fois de suite le même checkpoint, l'agent s'arrête et fait un bilan. Tu peux alors reprendre manuellement.

### Cascade

Si tu modifies CP1, tout le pipeline redémarre depuis §1. Si tu modifies CP2, §1 reste, mais §3-§6 redémarrent. Si tu modifies CP3, §1-§2 restent, §4-§6 redémarrent.
```

- [ ] **Step 3 : Commit**

```bash
cd /home/giak/projects/truth-engine
git add tools/engines/SUBLIMATOR_v33.1_GUIDE_HUMAN.md
git commit -m "feat(guide): add §9.5 Checkpoints section in human guide"
```

---

## Task 12 : Validation finale de la spec v33.1

**Files:**
- Read: `tools/engines/SUBLIMATOR_v33.1_spec_agent.md`
- Read: `tools/engines/SUBLIMATOR_v33.1_GUIDE_HUMAN.md`

- [ ] **Step 1 : Vérifier que tous les YAML sont valides**

```bash
cd /home/giak/projects/truth-engine
python3 << 'PY'
import yaml
for f in ['tools/engines/SUBLIMATOR_v33.1_spec_agent.md', 'tools/engines/SUBLIMATOR_v33.1_GUIDE_HUMAN.md']:
    with open(f) as fp:
        parts = fp.read().split('---')
    valid = True
    for i, p in enumerate(parts[1:], 1):
        try:
            yaml.safe_load(p)
        except yaml.YAMLError as e:
            print(f'{f} YAML {i} ERROR: {e}')
            valid = False
    print(f'{f}: {"OK" if valid else "FAIL"}')
PY
```

Attendu : "OK" pour les 2 fichiers

- [ ] **Step 2 : Vérifier le décompte LOIS = 14**

```bash
cd /home/giak/projects/truth-engine
grep -cE "^  - id: L[0-9]+" tools/engines/SUBLIMATOR_v33.1_spec_agent.md
```

Attendu : 14

- [ ] **Step 3 : Vérifier que §10 existe**

```bash
cd /home/giak/projects/truth-engine
grep -E "^## §10" tools/engines/SUBLIMATOR_v33.1_spec_agent.md
```

Attendu : "## §10 CHECKPOINTS (v33.1+)"

- [ ] **Step 4 : Vérifier que L13 et L14 sont dans la spec**

```bash
cd /home/giak/projects/truth-engine
grep -E "^  - id: L1[34]" tools/engines/SUBLIMATOR_v33.1_spec_agent.md
```

Attendu : 2 lignes (L13, L14)

- [ ] **Step 5 : Vérifier que le slot checkpoints existe dans §4.2**

```bash
cd /home/giak/projects/truth-engine
grep -E "^  checkpoints:" tools/engines/SUBLIMATOR_v33.1_spec_agent.md
```

Attendu : 1 ligne

- [ ] **Step 6 : Vérifier que le diagramme mermaid §5.1.bis existe**

```bash
cd /home/giak/projects/truth-engine
grep -cE "^```mermaid" tools/engines/SUBLIMATOR_v33.1_spec_agent.md
```

Attendu : ≥3 mermaid blocks (vs 1 dans v33.0)

- [ ] **Step 7 : Commit final si tout est OK**

```bash
cd /home/giak/projects/truth-engine
git status
git log --oneline -10
```

---

## Task 13 : Mettre à jour AGENTS.md (section Engines)

**Files:**
- Modify: `AGENTS.md` (section Engines)

- [ ] **Step 1 : Trouver la section Engines dans AGENTS.md**

```bash
cd /home/giak/projects/truth-engine
grep -n "SUBLIMATOR" AGENTS.md
```

- [ ] **Step 2 : Ajouter mention de v33.1**

Trouver la ligne qui référence SUBLIMATOR v33.0 et ajouter après :
```markdown
- **SUBLIMATOR v33.1** : pipeline semi-auto avec 3 checkpoints structurés (§0, §2, §3) et 14 LOIS. Spec : `tools/engines/SUBLIMATOR_v33.1_spec_agent.md`, Guide : `tools/engines/SUBLIMATOR_v33.1_GUIDE_HUMAN.md`. v33.0 archivée en `.bak`.
```

- [ ] **Step 3 : Commit**

```bash
cd /home/giak/projects/truth-engine
git add AGENTS.md
git commit -m "docs(agents): add SUBLIMATOR v33.1 entry to Engines section"
```

---

## Self-Review Checklist

- [ ] Tous les YAML des 2 fichiers (spec + guide) valides
- [ ] 14 LOIS (L1-L14) présentes et numérotées
- [ ] §10 CHECKPOINTS existe avec 6 sous-sections (10.1-10.6)
- [ ] Slot `checkpoints` dans §4.2 schéma d'état
- [ ] §4.4.bis boucle bornée
- [ ] §4.7 events `checkpoint` et `checkpoint_input`
- [ ] §5.1.bis table des 3 CP + diagramme mermaid
- [ ] §9 CHANGELOG entry v33.1
- [ ] §9.5 Checkpoints dans GUIDE_HUMAN
- [ ] AGENTS.md mis à jour

## Notes d'implémentation

- **Ordre des tasks** : 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 12 → 13. Pas de parallèle possible car tasks 2-9 modifient le même fichier.
- **Pas de test runner formel** : la validation est structurelle (YAML valide, décompte LOIS, présence sections). C'est une spec déclarative, pas du code applicatif.
- **Rétrocompat** : le fallback CP validate pour state v33.0 n'est pas codé, juste documenté en §10.6.
- **Test live** : après implémentation, on peut relancer le pipeline Sumer/France avec v33.1 et voir si l'humain peut enrichir §2 avec la thèse multi-civilisationnelle.
