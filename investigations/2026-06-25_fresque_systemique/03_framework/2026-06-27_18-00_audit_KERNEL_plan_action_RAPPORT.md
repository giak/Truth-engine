# AUDIT KERNEL — Diagnostic profond et plan d'action
## « Le KERNEL analyse des textes. La fresque enquête sur des événements. Comment réconcilier les deux ? »

**Date :** 2026-06-27
**Type :** RAPPORT
**Fichier audité :** `/home/giak/projects/truth-engine/truth-engine-v2/KERNEL.md` (235 lignes, v2.0)
**Écosystème :** 33 fichiers dans truth-engine-v2/ + 978 fichiers dans fresque systemique/

---

## §0 — VERDICT EN UNE PHRASE

> Le KERNEL est un excellent moteur d'analyse de **textes**. Mais il n'a pas de mode pour analyser des **événements**. Résultat : 100 % des enquêtes fresque sautent le KERNEL et utilisent le protocole v2.4 directement. Le KERNEL et la fresque sont deux mondes parallèles qui ne se parlent pas.

---

## §1 — DOUBLE CHECK : EXHAUSTIVITÉ DES FICHIERS

### 1.1 Tous les fichiers référencés existent

| Fichier KERNEL | Chemin | Existe ? | Lu ? |
|----------------|--------|:--------:|:----:|
| SYMBOLS.md | definitions/SYMBOLS.md | ✅ | ✅ |
| PATTERNS.md | definitions/PATTERNS.md | ✅ | ✅ |
| THREATS.md | definitions/THREATS.md | ✅ | ✅ |
| GATES.md | forensic/GATES.md | ✅ | ✅ |
| INVESTIGATION.md | protocol/INVESTIGATION.md | ✅ | ✅ |
| PERSO_FRESQUE.md | protocol/PERSO_FRESQUE.md | ✅ | ✅ |
| EPISTEMIC.md | search/EPISTEMIC.md | ✅ | ✅ |
| TEMPLATES.md | search/TEMPLATES.md | ✅ | ✅ |
| OPTIMIZATION.md | search/OPTIMIZATION.md | ✅ | ✅ |
| REASONING.md | forensic/REASONING.md | ✅ | ✅ |
| REQUEST_LOG.md | forensic/REQUEST_LOG.md | ✅ | ✅ |
| MACROS.md | tools/MACROS.md | ✅ | — |
| DSL.md | tools/DSL.md | ✅ | ✅ |
| TEMPLATE.md | output/TEMPLATE.md | ✅ | ✅ |
| 15 clusters | clusters/*.md | ✅ | — (index seulement) |

**Verdict :** Aucun fichier manquant. Le KERNEL est techniquement correct. Le problème est ailleurs.

---

## §2 — DIAGNOSTIC : DEUX MONDES PARALLÈLES

### 2.1 Le mode « TEXTE » (KERNEL actuel)

Le KERNEL est conçu pour analyser **un texte/article/discours** :

```
INPUT : « Macron a déclaré X sur Y » (un article, un tweet, un discours)
  → §0 : TEXT_ANALYSIS — scorer 15 symboles (Ξ€ΛΩΨ...)
  → §0 : Load clusters si scores ≥5
  → §1 : CREDO 12-20 questions
  → §1 : SEARCH (◈35%, ADV 20%, etc.)
  → §1 : FACT_REGISTRY ✦✧⁅❧
  → §1 : CAUSALITY chains ≥3 links
  → §1 : DIALECTICAL 3 perspectives
  → §1 : OUTPUT investigation (7-15 sections)

DURÉE : 2-3 h | FORMAT : Investigation YAML | COMPLEXITÉ : Symboles + Clusters
```

### 2.2 Le mode « ÉVÉNEMENT » (ce qu'on fait dans la fresque)

La fresque enquête sur **un événement/scandale** :

```
INPUT : « DNC — blindés Centaure contre agriculteurs en Ariège »
  → Identifier les 3-5 fils actifs (B, H, C, E, G)
  → Pour chaque fil : REMONTÉE_DES_FILS (acte → renforcements → manifestation)
  → CHAÎNE CAUSALE 200+ ans
  → PREUVES ✦✧⁅❧
  → CONTRE-VERSION
  → CONTRE-MESURES
  → OUTPUT : Investigation 14 chapitres

DURÉE : 1-3 h | FORMAT : Investigation fresque | COMPLEXITÉ : Fils + Mécanismes + Pelote
```

### 2.3 Le fossé

| Dimension | KERNEL (mode texte) | Fresque (mode événement) |
|-----------|---------------------|--------------------------|
| **Input** | Texte/article/discours | Événement/scandale/crise |
| **Analyse** | Symboles Ξ€ΛΩΨ + clusters | Fils A-L + mécanismes M## |
| **Questions** | CREDO générique (12-20q) | Pelote 5Q par fil |
| **Sources** | ◈◉○ + EDI | ✦✧⁅❧ + HEAD check |
| **Sortie** | Investigation 7-15 sections | Investigation 14 chapitres |
| **Temps** | 2-3 h | 1-3 h |
| **Utilisé ?** | Rarement (0 session récente) | 16 enquêtes produites |

**Conclusion :** Le KERNEL n'est pas cassé. Il est juste inutilisé dans la pratique courante. La fresque a développé SON PROPRE protocole (v2.4) qui court-circuite le KERNEL.

---

## §3 — ANALYSE LIGNE À LIGNE DU KERNEL : CE QUI SERT, CE QUI BLOQUE

### 3.1 Ce qui DOIT être gardé (fondations)

| Section KERNEL | Lignes | Utilité | Verdict |
|----------------|:------:|---------|:-------:|
| CONSTANTS (BASE, INV) | 3 | Références de chemins | ✅ **GARDER** |
| TOOLS (@READ, @WEB, @FETCH, @EXA, @MNEMO) | 10 | Syntaxe des outils | ✅ **GARDER** |
| SEARCH PRIORITY (1.@MNEMO_Q → 4.@EXA) | 7 | Ordre de recherche critique | ✅ **GARDER** |
| DETECTION (input handler) | 5 | Détection URL vs texte | ✅ **ÉTENDRE** (ajouter mode événement) |
| §2 GATES | 14 | Blocages critiques | ✅ **GARDER** |
| §3 MANDATORY | 14 | Règles absolues | ✅ **GARDER** |
| §4 FORBIDDEN | 12 | Interdictions | ✅ **GARDER** |
| §5 FILES | 8 | Références de fichiers | ✅ **GARDER** (mettre à jour) |
| §6 BOOT | 6 | Boot message | ✅ **GARDER** |

### 3.2 Ce qui DOIT être simplifié ou déplacé

| Section KERNEL | Problème | Action |
|----------------|----------|--------|
| §0 TEXT ANALYSIS (lignes avec scores [0-10], clusters, MANIPULATION_REPORT) | 40+ lignes de logique de scoring de texte. Non utilisée par la fresque. | **DÉPLACER** dans un fichier `protocol/TEXT_ANALYSIS.md` — garder un déclencheur dans KERNEL |
| §1 step 0 (TEXT_ANALYSIS obligatoire) | Bloque le mode événement | **RENDRE CONDITIONNEL** — skip si mode événement |
| §1 steps 1-2 (TEMPORAL, MEMORY) | Utiles aux deux modes | **GARDER** |
| §1 steps 3-7 (COMPLEXITY, PERSO, ACCUSATION, CREDO, SCOPING) | Utiles aux deux modes, mais trop détaillés | **SIMPLIFIER** — garder la logique, supprimer le détail |
| §1 steps 8-8t (ANALYSIS, COGNITIVE, DIALECTICAL) | 100% mode texte | **DÉPLACER** dans TEXT_ANALYSIS.md |
| §1 steps 9-13 (SEARCH, CONSTRUCTION, CAUSALITY, IMPACT, VERIFICATION) | Utiles aux deux modes | **GARDER** (simplifier) |
| §1 steps 14-19 (OUTPUT, ARTICLE, EDI, WOLVES, GATE, SAVE) | Utiles aux deux modes | **GARDER** |
| §1 step 16 EDI | Défini 2 fois (KERNEL + EPISTEMIC) | **RÉFÉRENCER EPISTEMIC** au lieu de dupliquer |
| §1 FEEDBACK/REALLOCATION | Trop complexe | **SIMPLIFIER** en 3 règles maximum |

### 3.3 Dead code identifié

| Code | Emplacement | Problème |
|------|-------------|----------|
| `@PAT[BIDERMAN]` | PATTERNS.md | Jamais activé en pratique (score requis trop spécifique) |
| `CLAMPS (maximum scores)` | SYMBOLS.md §5 | Mesure anti-biais jamais exécutée |
| `RESONANCE (symbol interactions)` | SYMBOLS.md §6 | Théorique — jamais utilisé |
| `@PAT[SURV_CAP]` | PATTERNS.md | Pattern très spécifique (surveillance capitaliste) |
| `@PAT[COG_INFRA]` | PATTERNS.md | Pattern très spécifique |
| `@PF[]` (PERSO_FRESQUE) | PERSO_FRESQUE.md | Protocole biographie jamais exécuté |

### 3.4 Incohérences mineures

| ID | Incohérence | Impact |
|----|-------------|--------|
| **I1** | KERNEL §1 step 10 dit `FACT_REGISTRY ✦✧⁅⁂ ⊕⊗⊙` | Correct |
| **I2** | KERNEL §1 step 8t dit `3 perspectives force égale` | Mais §1 ne liste que 3 perspectives, pas 4 comme INVESTIGATION |
| **I3** | EDI défini en KERNEL step 16 ET EPISTEMIC §4 | Duplication sans divergence |

---

## §4 — CE QUE L'ARCHITECTURE.md RÉVÈLE

Le fichier `ARCHITECTURE.md` (non chargé par le KERNEL, mais existant) est un document de design qui décrit l'architecture COMPLÈTE. Il révèle :

1. **33 fichiers** dans l'écosystème KERNEL
2. **7 couches** (Layer 0 à Layer 7)
3. **15 clusters** indexés par symbole
4. **4 bizarreries documentées** (B1-B5) — non corrigées
5. **3 problèmes de duplication** entre KERNEL et fichiers associés

**Ce que ARCHITECTURE.md ne révèle pas :** que la fresque a construit un protocole parallèle (v2.4) qui ne passe pas par le KERNEL.

---

## §5 — LE PROBLÈME FONDAMENTAL EN UN DIAGRAMME

```
┌─────────────────────────────────────────────────────────────────────┐
│                        TRUTH ENGINE v2.0                              │
│                                                                       │
│  ┌─────────────┐                              ┌────────────────────┐ │
│  │  KERNEL.md   │                              │   FRESQUE SYSTEMIQUE│ │
│  │  (235 lignes) │                              │   (978 fichiers)    │ │
│  │              │                              │                    │ │
│  │ MODE TEXTE   │                              │ Protocole v2.4     │ │
│  │  §0: 15 symb │                              │  10 fils A-L       │ │
│  │  §0: clusters│                              │  42 mécanismes     │ │
│  │  §1: CREDO   │       NE COMMUNIQUENT        │  Pelote 5Q         │ │
│  │  §1: FACT_REG│            PAS               │  14 chapitres      │ │
│  │  §1: OUTPUT  │◄══════════════════════════════│  Investigation     │ │
│  │              │                              │                    │ │
│  │ 0 enquête    │                              │ 16 enquêtes        │ │
│  │ récente      │                              │ utilisant la       │ │
│  │ utilisant    │                              │ fresque            │ │
│  │ le KERNEL    │                              │ DIRECTEMENT        │ │
│  └─────────────┘                              └────────────────────┘ │
│                                                                       │
│  PROBLÈME : deux mondes, zéro passerelle.                            │
└─────────────────────────────────────────────────────────────────────┘
```

---

## §6 — PLAN D'ACTION EN 4 ÉTAPES

### ÉTAPE 1 : Ajouter §0 bis MODE PÉLOTE dans KERNEL.md (priorité maximale, 30 lignes)

**Action :** Insérer après la section DETECTION (avant §0) un détecteur de mode.

```markdown
══════════════════════════════════════
MODE PELOTE (détection événement — v2.1)
══════════════════════════════════════

SI input = événement/actualité/scandale (pas un texte à analyser) :
  → BASULER en MODE PELOTE
  → SKIP §0 TEXT ANALYSIS (symboles, clusters)
  → ALLER directement à :

  ◆ 1. IDENTIFIER les 3-5 fils actifs
     Pour chaque fil A-L : ce fil est-il actif dans l'événement ?
     → Output : liste des fils actifs + justification 1 ligne

  ◆ 2. EXÉCUTER algorithme Pelote 5Q pour chaque fil actif
     T-1 (0-10 ans) → T-2 (10-50 ans) → T-3 (50+ ans) → Acte fondateur → Vérification
     → Output : chaîne causale par fil

  ◆ 3. TISSER les N chaînes en UN récit
     « De AAAA à aujourd'hui — comment l'événement X est le produit de 200+ ans
        de verrouillage systémique par les fils {B, C, E, G} »
     → Output : 3-5 paragraphes

  ◆ 4. OUTPUT standard :
     - Chaîne causale (format Pelote)
     - Preuves (✦✧⁅❧ avec URLs)
     - Contre-version (si applicable)
     - Contre-mesures (si NREF souhaité)

  → PUIS continuer normalement à §1 (sans §0)

DÉTECTION :
  Input = « Comment en est-on arrivé là ? »     → MODE PELOTE
  Input = URL d'article d'actualité               → @FETCH → MODE PELOTE
  Input = événement/fait/scandale (+ contexte)   → MODE PELOTE
  Input = texte/article/discours/poste            → MODE TEXTE (§0 normal)
  Input contient @READ[definitions/...]           → MODE TEXTE
```

**Impact :** 30 lignes, zéro fichier cassé. Le KERNEL garde son mode texte intact. On ajoute UNE porte d'entrée pour le mode événement.

### ÉTAPE 2 : Simplifier §1 (le pipeline)

**Action :** Réduire le pipeline 19-step à 2 chemins :

```
IF MODE TEXTE :
  §0 → §1(1-19 complets) → OUTPUT investigation standard

IF MODE PELOTE :
  §0 bis → §1(10 CONSTRUCTION → 11 CAUSALITY → 14 OUTPUT → 19 SAVE)
  Skip : 3 COMPLEXITY, 4 PERSO, 6 CREDO, 8 COGNITIVE, 8t DIALECTICAL
```

**Gains :** Le pipeline mode Pelote passe de 19 à 6 étapes. Temps de session : 2-3h → 30-60 min.

### ÉTAPE 3 : Référencer au lieu de dupliquer

| Section | Actuel | Nouveau | Économie |
|---------|--------|---------|:--------:|
| EDI (step 16) | 6 lignes + BIAS | `→ EPISTEMIC.md §4` | -4 lignes |
| Cluster mapping (step 5) | 4 lignes inline | `→ SYMBOLS.md §4` | -3 lignes |
| OUTPUT format (step 14) | 3 lignes inline | `→ TEMPLATE.md` | -2 lignes |

**Gains :** -9 lignes, -2 redondances.

### ÉTAPE 4 : Marquer l'obsolescence des prompts parallèles

**Action :** Ajouter une note dans FAIT-MINEUR v1.1, PELOTE-MINEUR v1.0, et les prompts d'investigation :

```markdown
> ⚠️ Ce prompt est en cours de remplacement par le MODE PELOTE dans KERNEL.md v2.1.
> Conserver comme référence historique. Utiliser KERNEL.md comme point d'entrée unique.
```

**Impact :** Aucun fichier supprimé. Juste une balise de navigation.

---

## §7 — TABLEAU DE BORD AVANT/APRÈS

| Métrique | Avant (v2.0) | Après (v2.1) |
|----------|:------------:|:------------:|
| Fichiers modifiés | — | **1** (KERNEL.md) |
| Lignes dans KERNEL.md | 235 | **~260** (+25 lignes §0 bis) |
| Prompts actifs | 4 | **1** (KERNEL avec 2 modes) |
| Étapes pour mode Pelote | 19 | **6** |
| Redondances EDI/clusters | 2 | **0** |
| Temps session Pelote | 2-3 h | **30-60 min** |
| Fichiers supprimés | — | **0** (archivage seulement) |
| Compatibilité mode texte | ✅ | ✅ (inchangé) |

---

## §8 — PLAN DE DÉPLOIEMENT

| Phase | Action | Durée | Risque |
|:-----:|--------|:-----:|:------:|
| **1** | Ajouter §0 bis MODE PELOTE dans KERNEL.md | 15 min | **Nul** — ajout uniquement |
| **2** | Simplifier §1 (pipeline conditionnel) | 20 min | **Faible** — garder l'existant |
| **3** | Référencer au lieu de dupliquer (EDI, clusters) | 10 min | **Nul** — sémantiquement identique |
| **4** | Marquer l'obsolescence des prompts parallèles | 5 min | **Nul** — balise seulement |
| **5** | **TEST** : lancer un événement réel en MODE PELOTE | 30 min | Validation |
| **6** | **TEST** : lancer un texte en MODE TEXTE | 30 min | Non-régression |
| **TOTAL** | | **1h50** | |

---

## §9 — LE GESTE UTILISATEUR FINAL (APRÈS v2.1)

```
> « DNC — blindés Centaure contre agriculteurs. Comment en est-on arrivé là ? »

→ [DÉTECTION] Input = événement
→ [MODE PELOTE]

→ [1. IDENTIFICATION] Fils actifs :
   B (Monopole d'État) : le ministère décide seul de la stratégie d'abattage
   H (Exceptionnalisme) : « le bœuf français est sain » comme dogme
   C (Société civile atrophiée) : 3 syndicats unanimes → refusés sans justification
   E (Presse sans contre-pouvoir) : médias reprennent le communiqué du ministère
   G (Laïcité religion civile) : l'État traite l'abattage comme purement technique

→ [2. PELOTE 5Q] Pour chaque fil :
   Fil B : Loi Le Chapelier (1791) → Nationalisations (1945) → CNTS (1952) → Animal Health Law (2016, interprétation restrictive) → arrêté 16 juillet 2025
   ...

→ [3. TISSAGE] La DNC n'est pas une crise sanitaire — c'est le point d'arrivée de 234 ans de monopole d'État ...

→ [4. OUTPUT] Chaîne causale complète + preuves ✦✧⁅❧ + contre-version
```

---

*Audit KERNEL produit le 2026-06-27. 33 fichiers, 7 couches, 1 problème fondamental : deux modes pour deux besoins différents. La solution tient en 30 lignes.*
