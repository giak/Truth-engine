# PIPELINE ARTICLE — Guide complet de l'investigation à la publication

**Document unique de référence.** Décrit le pipeline complet : investigation → rédaction → lint → publication.

**Version :** 1.0  
**Date :** 2026-05-29  
**Complète et unifie :** archive/v1/STRUCTURE.md, USER_GUIDE.md (obsolète v8.0), KERNEL_v1_DEPRECATED.md  
**Ne remplace pas :** SUBLIMATOR_v28.0.md, truth-engine-v2/KERNEL.md — documents spécialisés à charger en complément  
**Dépend de :** tools/prompts/systems/SUBLIMATOR_v28.0.md, truth-engine-v2/KERNEL.md, tools/scripts/lint-article.sh

---

> 🔥 **PAR OÙ COMMENCER SELON TON BESOIN**
> 
> | Si tu as… | Va dans… |
> |---|---|
> | Une idée, un sujet, un fait brut | **§1** — Investigation (phase amont) → KERNEL v2 |
> | Une investigation prête | **§2** — Pipeline SUBLIMATOR (rédaction) → 3 tiers + CP |
> | Un brouillon à corriger | **§5** — Lint script + **§3** — LOIS de rédaction |
> | Un article finalisé | **Publication Substack** → `substack-online/posts/` |
> 
> Chaque étape est détaillée dans la section correspondante ci-dessous.

---

## §0 — VUE D'AVION

```
IDÉE / SUJET / FAIT BRUT
         │
         ▼
┌──────────────────────────────────────────────────────┐
│ §1 — INVESTIGATION (phase amont)                     │
│                                                      │
│ 1a. KERNEL v1 (déprécié)   OU   1b. KERNEL v2       │
│      KERNEL_v1_DEPRECATED.md      truth-engine-v2/   │
│                                                      │
│ Phases : Text Analysis → Protocol (0→19) → Output    │
│ Livrables : INVESTIGATION, HYPER_MATRICE,            │
│             ARCHITECTURE, REGISTRE, SATURATION_AUDIT  │
└──────────────────────────┬───────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────┐
│ §2 — PIPELINE SUBLIMATOR (rédaction d'article)       │
│                                                      │
│ TIER 1 — Blueprint : Census → Digest → Dialectique  │
│         → Architecture → Fact-Check → CP#1           │
│                                                      │
│ TIER 2 — Cycle multi-agent : Écrivain → Critique    │
│         → Correcteur → Arbitre (× par section) → CP#4│
│                                                      │
│ TIER 3 — Assemblage → Audit stylistique → CP#5      │
│         → Quality Gate → Article final               │
└──────────────────────────┬───────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────┐
│ §5 — LINT AUTOMATISÉ (vérifie les LOIS 1-8)          │
│ tools/scripts/lint-article.sh (7 checks, CP#5)       │
│ ═══ LOIS appliquées DURANT §2, vérifiées DANS §5 ═══ │
└──────────────────────────┬───────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────┐
│ Publication Substack                                  │
│ HTML → substack-online/posts/                        │
│ Email → email_list.giak.csv                          │
│ CSV → posts.csv                                      │
└──────────────────────────────────────────────────────┘
```

### Fichiers clés du pipeline

| Fichier | Rôle | Étape |
|---------|------|-------|
| `truth-engine-v2/KERNEL.md` | Orchestrateur v2 — 200 lignes, steps 0→19 | §1 |
| `tools/prompts/systems/SUBLIMATOR_v28.0.md` | Pipeline rédaction — 3 tiers, CP#1→CP#5 | §2 |
| `tools/scripts/lint-article.sh` | 7 checks automatisés (LOI 1-8) | §3, §5 |
| `AGENTS.md` | Règles projet, éthique vérité, conventions nommage | §4 |
| `docs/VISION.md` | Philosophie et principes fondamentaux | Contexte |
| `truth-engine-v2/ARCHITECTURE.md` | Dépendances entre fichiers KERNEL v2 | §1 |
| `investigations/INDEX.md` | Index de toutes les investigations | §1 |

---

## §1 — INVESTIGATION (phase amont)

### 1.1 Objectif

Produire des **faits vérifiés** à partir d'un sujet, d'un texte ou d'un corpus. Le template de sortie standard est disponible dans `truth-engine-v2/output/TEMPLATE.md`. L'investigation est la **matière première** de tout article. Un article n'est jamais écrit sans investigation préalable.

### 1.2 Deux KERNELs coexistent

| | KERNEL v1 (déprécié) | KERNEL v2 (actif) |
|---|---|---|
| Fichier | `KERNEL_v1_DEPRECATED.md` | `truth-engine-v2/KERNEL.md` |
| Version | v15.1 | v2.0 |
| Lignes | ~400 | ~200 |
| État | **Ne plus utiliser** | **Référence actuelle** |
| Architecture | Monolithique | Modular (30+ fichiers) |
| Fichiers support | `kb/` (inexistant sur disque) | `truth-engine-v2/definitions/`, `clusters/`, `protocol/`, `search/`, `forensic/`, `tools/`, `output/` |

### 1.3 Pipeline KERNEL v2 (steps 0→19)

```
§0 — TEXT ANALYSIS
  → MANIPULATION_REPORT (15 symbols + patterns + threats)
  → Charge clusters si score ≥5

§1 — PROTOCOL (steps 0→19)
   0  TEXT_ANALYSIS
   1  TEMPORAL (date des événements)
   2  MEMORY (MnemoLite search)
   3  COMPLEXITY (SIMPLE/MEDIUM/COMPLEX/APEX)
   4  PERSO_FRESQUE (si personne)
   5  ACCUSATION? → SYMETRIC_CHECK
   6  CRÉDO (12-20 questions)
   7  SCOPING (domaines, acteurs)
   8  ANALYSIS (raffine MANIPULATION_REPORT)
   8b COGNITIVE (clusters + herméneutique)
   8t DIALECTICAL (3 perspectives)
   9  SEARCH (queries ciblées)
  10  CONSTRUCTION (FACT_REGISTRY)
  11  CAUSALITY (chaînes causales)
  12  IMPACT (qui gagne/perd/meurt/recule)
  13  VERIFICATION (cross-domain)
  14  OUTPUT (investigation structurée)
  15  ARTICLE (post-processing)
  16  EDI (Epistemic Diversity Index)
  17  WOLVES (prédateurs)
  18  GATE_CHECK
  18b GATE_AUTO
  19  SAVE (MnemoLite + fichier)
```

### 1.4 Types de livrables d'investigation

| Type | Suffixe | Contenu |
|------|---------|---------|
| **INVESTIGATION** | `_INVESTIGATION.md` | Rapport complet (7-15 sections selon complexité) |
| **HYPER_MATRICE** | `_HYPER_MATRICE.md` | Données atomiques, faits avec sources |
| **ARCHITECTURE** | `_ARCHITECTURE.md` | Plan narratif + thèse + structure |
| **REGISTRE** | `_REGISTRE.md` | Registre systémique (traçabilité) |
| **SATURATION_AUDIT** | `_SATURATION_AUDIT.md` | Audit de vérification complet |

### 1.5 Format dossier projet (investigations majeures)

Les investigations complexes suivent une structure de dossier standardisée :

```
investigations/YYYY-MM-DD_sujet/
├── 00_DIGEST.md           # Résumé exécutif
├── 01_MATRICE.md          # Matrice de données
├── 02_CLUSTERING.md       # Regroupement par clusters
├── 03_DIALECTIQUE.md      # 3 perspectives
├── 04_ARCHITECTURE.md     # Structure narrative
├── 05_ARTICLE.md          # Article final
├── 06_SATURATION_AUDIT.md # Audit qualité
├── _assemblage/           # Fichiers de travail (prompts, sections)
│   ├── sections/          # Sections individuelles avec cycles Écrivain/Critique/Correcteur
│   │   ├── 1_titre_ECRIVAIN_v1.md
│   │   ├── 1_titre_CRITIQUE_v1.md
│   │   └── 1_titre_CORRECTEUR_v1.md
│   ├── CP1A.md            # Checkpoint 1A
│   └── quality_gate.md    # Quality gate
├── articles/              # Articles finaux (si série)
├── sources/               # Documents sources
└── archive/               # Anciennes versions
```

### 1.6 Métriques d'investigation

| Métrique | Cible SIMPLE | Cible MEDIUM | Cible COMPLEX | Cible APEX |
|----------|-------------|-------------|---------------|------------|
| EDI | ≥0.30 | ≥0.50 | ≥0.70 | ≥0.80 |
| Sources ◈ | ≥1 | ≥2 | ≥3 | ≥3 |
| Wolves | 5 | 5 | 8 | 12 |
| ✦ Faits | 5 | 8 | 10 | 10 |
| Chaînes causales | 1 | 2 | 3 | 5 |
| Queries | 12 | 18 | 25 | 35+ |

---

## §2 — PIPELINE SUBLIMATOR (rédaction d'article)

**Document source :** `tools/prompts/systems/SUBLIMATOR_v28.0.md` (v28.4)

Le pipeline SUBLIMATOR transforme une investigation brute en **article final prêt à publier**. Il est structuré en 3 tiers, ponctués de checkpoints (CP).

### 2.1 Tier 1 — Blueprint (préparation)

Ce tier produit la **matière narrative** : il structure les données de l'investigation en un plan d'article.

```
1. CENSUS — Recensement de toutes les données disponibles (faits, sources, chiffres)
       │
       ▼
2. DIGEST — Synthèse des données. Résumé exécutif + points clés
       │
       ▼
3. DIALECTIQUE — 3 perspectives : thèse / antithèse / synthèse
       │
       ▼
4. ARCHITECTURE — Structure narrative : H1 → H2 → H3, transitions, thèse
       │
       ▼
5. FACT-CHECK — Vérification croisée des faits. Marquer les doutes
       │
       ▼
   CP#1 — Validation par l'utilisateur (ou boucle d'itération)
```

**Étapes supplémentaires selon profil :**

| Étape | Profil C (colère) | Profil D (désespoir) | Profil B (blocage) |
|-------|------------------|--------------------|-------------------|
| CP#1A | Reconstruction | Rédemption | Catalyseur |
| CP#1B | Check tonalité | Check tonalité | Check tonalité |


### 2.2 Tier 2 — Cycle multi-agent (rédaction section par section)

Chaque section de l'article (un H2 avec ses H3) traverse un **cycle à 4 voix** :

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  ÉCRIVAIN   │ →   │  CRITIQUE   │ →   │ CORRECTEUR  │ →   │   ARBITRE   │
│ Rédige la   │     │ Analyse les │     │ Applique les│     │ Valide ou   │
│ section v1  │     │ faiblesses  │     │ corrections │     │ rejette →   │
└─────────────┘     └─────────────┘     └─────────────┘     │ boucle      │
                                                             └─────────────┘
```

**Règles du cycle :**

- **Écrivain** : produit la section avec les LOIS 1-8 appliquées (voir §3)
- **Critique** : liste les violations des LOIS (voir §3), les faiblesses narratives, les manques factuels. Ne propose PAS de corrections.
- **Correcteur** : réécrit la section en corrigeant TOUS les points du Critique. Ne change PAS ce qui n'est pas critiqué.
- **Arbitre** : vérifie que les corrections sont suffisantes. Si non → boucle Critique→Correcteur. Si oui → section validée.
- Le cycle s'arrête quand l'Arbitre valide **et** que l'utilisateur approuve.

**Fichiers produits :**
```
_assemblage/sections/
├── 1_titre_ECRIVAIN_v1.md     # Production initiale
├── 1_titre_CRITIQUE_v1.md     # Analyse du Critique
├── 1_titre_CORRECTEUR_v1.md   # Version corrigée
├── 1_titre_ECRIVAIN_v2.md     # Si le cycle a bouclé
└── 1_titre_FINAL.md           # Version arbitrée
```

**Checkpoint : CP#4** — Validation intermédiaire après chaque section.


### 2.3 Tier 3 — Assemblage + Quality Gate

Une fois toutes les sections validées individuellement :

```
1. ASSEMBLAGE — Concaténation des sections dans l'ordre de l'Architecture
       │
       ▼
2. AUDIT STYLISTIQUE — Vérification complète des 8 LOIS + cohérence globale
       │
       ▼
3. CP#5 — LINT OBLIGATOIRE : exécuter tools/scripts/lint-article.sh
       │    Toute violation bloque la publication.
       ▼
4. QUALITY GATE — Relecture humaine : niveau de confiance, vérification finale
       │
       ▼
5. ARTICLE FINAL → articles/YYYY-MM-DD_HH-MM_sujet_ARTICLE.md
```

### 2.4 Profils de lecteur (diagnostic SUBLIMATOR)

Le Tier 1 commence par un **diagnostic de profil** qui conditionne tout le ton de l'article :

| Profil | Sentiment dominant | Stratégie | Exemple |
|--------|-------------------|-----------|---------|
| **A** | Colère | Canaliser sans apaiser | « Ils mentent. Voici les preuves. » |
| **B** | Désespoir | Redonner de l'agentivité | « Ce n'est pas fini. Voici ce qu'on peut faire. » |
| **C** | Blocage cognitif | Déconstruire le blocage | « Vous croyez X. Regardez les faits Y. » |
| **D** | Réceptif neutre | Pédagogie + densité | « Voici le mécanisme, étape par étape. » |

---

## §3 — LOIS DE RÉDACTION (1-8)

### LOI 1 — Sources présentes avec URLs

**Règle :** L'article doit contenir une section `## Sources` avec des URLs valides. Chaque fait important doit être sourcé.

**Vérification :** `grep -c '^## Sources' article.md` — échoue si absent ou vide.

**Script :** `check_loi1_sources()`

**Pénalité :** ❌ FAIL si section Sources absente ou sans URLs


### LOI 2 — URLs précises

**Règle :** Les URLs doivent pointer vers la **page exacte** contenant l'information, pas vers une page d'accueil. Pas de `google.com`, `lemonde.fr` sans chemin.

**Script :** Vérification manuelle (non automatisée)


### LOI 3 — Émoji 🔒 en H1

**Règle :** Le titre H1 doit commencer par un émoji (de préférence 🔒, mais tout émoji est accepté).

**Raison :** L'émoji sert de marqueur visuel dans le fil Substack et améliore le taux d'ouverture.

**Script :** `check_loi3_emoji()`

**Pénalité :** ⚠️ WARNING (vérification manuelle recommandée — un article sans émoji peut être intentionnel)


### LOI 4 — Transitions faibles interdites

**Règle :** `« Mais »` et `« Cependant »` en début de phrase affaiblissent la force rhétorique. Maximum 3 occurrences par article.

**Exemptions :** `mais`/`cependant` en milieu de phrase (après une virgule, dans une parenthèse, ou après un verbe)

**Seuils :**

| Occurrences | Résultat |
|-------------|----------|
| 0 | ✅ PASS |
| 1-3 | ⚠️ WARNING |
| ≥4 | ❌ FAIL |

**Script :** `check_loi4_transitions()` — utilise awk avec regex `(^|[.!?]\s+)(Mais|Cependant)\b`


### LOI 5 — Calibration des sections

**Règle :** Chaque section H2 (hors Sources) doit faire entre 100 et 800 mots. L'intro (avant le premier H2) n'est pas comptée.

**Raison :** Les sections trop longues créent un « mur de briques » qui fait décrocher le lecteur. Les sections trop courtes fragmentent le propos.

**Script :** `check_loi5_calibration()`

**Pénalité :** ❌ FAIL pour chaque section hors fourchette


### LOI 6 — Gras 3-5 par section

**Règle :** Chaque section H2 doit contenir entre 3 et 5 segments en **gras** (`**...**`). L'intro avant le premier H2 est ignorée. La section `## Sources` est exclue.

**Raison :** Le gras structure la lecture rapide : le lecteur doit pouvoir survoler l'article et capter l'essentiel.

**Script :** `check_loi6_gras()` — utilise awk avec `while(match(line, /\*\*[^*]+\*\*/))`

**Pénalité :** ❌ FAIL si <3 ou >5 gras par section


### LOI 7 — Compression forensique

**Règle :** (Non automatisée. Vérification manuelle ou par LLM.)
- Supprimer les transitions introductives (« Il est intéressant de noter que… »)
- Acronyme direct : écrire « INSEE » pas « Institut national de la statistique et des études économiques » sauf à la première occurrence
- Pas de phrases vides : chaque phrase doit apporter un fait, un chiffre ou un lien causal
- Bibliographie ≤10% du volume total


### LOI 8 — Aucun ID interne dans le texte

**Règle :** Les IDs techniques (F001, D045, et tout pattern `F###` ou `D###`) ne doivent **pas** apparaître dans le texte visible. Ils sont réservés à la phase d'investigation.

**Exemptions :**
- URLs contenant des IDs (`https://example.com/D045/data`) → ignoré
- Markdown links `[texte](url)` → ignoré si l'ID est dans l'URL
- Commentaires HTML `<!-- D045 -->` → ignoré
- Blocs de code ` ``` ` → ignoré

**Script :** `check_loi8_ids()` — utilise awk avec tracking d'état pour les blocs de code ` ``` `

**Check complémentaire :** `check_loi8_lien()` — détecte `[LIEN_A_INSERER]` résiduel dans le texte. ❌ FAIL si présent.

**Pénalité :** ❌ FAIL par occurrence dans le texte visible

---

## §4 — CONVENTIONS

### 4.1 Nommage des fichiers

**Règle absolue :** Tout fichier dans `investigations/`, `articles/`, et `audits/` suit le format :

```
YYYY-MM-DD_HH-MM_sujet-type_TYPE.md
```

| Élément | Format | Exemple |
|---------|--------|---------|
| Date | `YYYY-MM-DD` | `2026-03-16` |
| Heure | `HH-MM` (optionnel si même jour) | `14-30` |
| Sujet | `kebab-case` (minuscules, tirets) | `reseaux-influence-elections` |
| Type | `MAJUSCULES` | `ARTICLE` |

**Types de fichiers :** Voir `AGENTS.md` — la table des suffixes (`_ARTICLE.md`, `_HYPER_MATRICE.md`, etc.) et leurs dossiers associés y est définie.

**Règles :**
- Pas d'espaces — utiliser tirets ou underscores
- Pas d'accents dans les noms de fichiers
- Date = date de création, Heure = optionnel si même jour


### 4.2 Structure des dossiers (état réel)

```
truth-engine/
├── articles/               # Articles finaux prêts à publier
│   └── YYYY-MM-DD_*.md
├── investigations/         # Dossiers d'enquête par sujet
│   ├── YYYY-MM-DD_sujet/   # Dossier projet complexe
│   │   ├── 00_DIGEST.md
│   │   ├── 01_MATRICE.md
│   │   ├── 02_CLUSTERING.md
│   │   ├── 03_DIALECTIQUE.md
│   │   ├── 04_ARCHITECTURE.md
│   │   ├── 05_ARTICLE.md
│   │   ├── 06_SATURATION_AUDIT.md
│   │   ├── _assemblage/    # Fichiers de travail SUBLIMATOR
│   │   ├── articles/       # Articles finaux (série)
│   │   ├── sources/        # Documents sources
│   │   └── archive/        # Anciennes versions
│   └── INDEX.md            # Index de toutes les investigations
├── audits/                 # Audits SATURATION et APEX
│   └── YYYY-MM-DD_*.md
├── tools/
│   ├── scripts/            # Scripts de validation
│   │   └── lint-article.sh
│   ├── prompts/            # Prompts systèmes
│   │   └── systems/        # SUBLIMATOR, etc.
│   └── tests/              # Tests des outils
├── truth-engine-v2/        # KERNEL v2 (30+ fichiers)
│   ├── KERNEL.md           # Kernel principal (steps 0→19)
│   ├── ARCHITECTURE.md     # Architecture du module
│   ├── definitions/        # Symboles, patterns
│   ├── clusters/           # Clusters d'investigation
│   ├── protocol/           # Protocole détaillé
│   ├── search/             # Moteurs de recherche
│   ├── forensic/           # Forensique
│   ├── tools/              # Utilitaires
│   └── output/             # Templates de sortie
├── substack-online/        # Export Substack
│   ├── posts/              # Posts HTML exportés
│   ├── posts.csv           # Index des posts
│   └── email_list.giak.csv # Liste des abonnés
├── sources/                # Documents sources bruts (PDF, etc.)
├── prompts/                # Prompts spécifiques (non-systèmes)
├── docs/
│   ├── specs/              # Spécifications (PRD, TAD, WARP, PIPELINE)
│   ├── user/               # Guides utilisateur
│   └── VISION.md           # Philosophie
├── archive/                # Anciennes versions
│   └── v1/
│       ├── STRUCTURE.md    # Structure projet (obsolète)
├── AGENTS.md               # Règles du projet pour l'IA
├── KERNEL_v1_DEPRECATED.md # Ancien kernel (ne pas utiliser)
├── README.md               # README du projet
└── package.json            # Métadonnées projet
```


### 4.3 Conventions d'écriture

| Règle | Description | Source |
|-------|-------------|--------|
| **Émoji H1** | 🔒 ou autre émoji en début de titre | LOI 3 |
| **Gras stratégique** | 3-5 segments **gras** / section | LOI 6 |
| **Chiffres en chiffres** | « 75 % » pas « soixante-quinze pour cent » | SUBLIMATOR LOI 7 |
| **Espace insécable** | Avant `%`, `€`, `:`, `;`, `!`, `?` | SUBLIMATOR |
| **Compactor** | « 10 Mds€ », « 415 TWh » | SUBLIMATOR |
| **Acronyme direct** | « INSEE » à la première occurrence sauf ambiguïté | LOI 7 |
| **Pas d'anglicismes** | « agenda » → « ordre du jour », « focus » → « attention » | SUBLIMATOR glossaire |
| **Guillemets français** | « » pas "" | SUBLIMATOR |
| **Citations en français** | Traduire les citations anglaises | SUBLIMATOR |
| **Pas de `LIEN_A_INSERER`** | Remplacer par l'URL réelle avant publication | LOI 8 |


### 4.4 Mode série

Quand un article fait partie d'une série (ex : série « Macron »), les articles sont stockés dans le dossier `investigations/YYYY-MM-DD_sujet/articles/` avec une numérotation :

```
S1_le-titre.md
S2_le-titre.md
S13_le-titre.md
```

Les articles de série ne sont pas placés dans `articles/` directement — ils sont livrés à l'utilisateur dans leur dossier d'investigation.

---

## §5 — SCRIPTS ET AUTOMATISATION

### 5.1 lint-article.sh — Vue d'ensemble

**Fichier :** `tools/scripts/lint-article.sh`

Script bash qui vérifie automatiquement **7 règles** sur un fichier article Markdown. S'exécute **obligatoirement** avant CP#5 (validation finale).

**Usage :**

```bash
./tools/scripts/lint-article.sh chemin/vers/article.md
```

**Les 7 checks automatisés :**

| Check | LOI | Code | Ce qu'il vérifie |
|-------|-----|------|------------------|
| 1 | LOI 1 | `check_loi1_sources()` | Section `## Sources` présente avec ≥1 URL |
| 2 | LOI 3 | `check_loi3_emoji()` | H1 commence par un émoji (⚠️ warning) |
| 3 | LOI 4 | `check_loi4_transitions()` | `Mais`/`Cependant` en début de phrase (≤3) |
| 4 | LOI 5 | `check_loi5_calibration()` | Chaque section H2 entre 100 et 800 mots |
| 5 | LOI 6 | `check_loi6_gras()` | **gras** entre 3 et 5 par section H2 |
| 6 | LOI 8a | `check_loi8_ids()` | Aucun ID factice `F###`/`D###` dans le texte visible |
| 7 | LOI 8b | `check_loi8_lien()` | Aucun `[LIEN_A_INSERER]` résiduel |

**Codes de sortie :**

| Sortie | Signification |
|--------|---------------|
| 0 | Aucune violation bloquante (⚠️ warning acceptés) |
| 1 | Au moins une violation ❌ FAIL |

**Format du rapport :**

```
╔══════════════════════════════════════════════════╗
║   LINT — /path/to/article.md                     ║
╚══════════════════════════════════════════════════╝
  ✅ LOI 1 : Sources présentes
  ⚠️  LOI 3 : Émoji en H1
  ✅ LOI 4 : Transitions faibles
  ❌ LOI 5 : Calibration sections
      Section §2 : 871 mots (max 800)
  ✅ LOI 6 : Gras 3-5/section
  ✅ LOI 8 : IDs factices
  ✅ LOI 8 : LIEN_A_INSERER

  Résultat : 5 ✅ / 1 ❌ / 1 ⚠️
```


### 5.2 Erreurs fréquentes et solutions

| Erreur | Cause probable | Solution |
|--------|---------------|----------|
| `count='0\n0'` | `grep -c` sans `\|\| true` | Le script inclut `\|\| true` depuis v1.1 |
| Double `else` dans LOI 8 | Erreur de syntaxe bash | Corrigé — une seule branche else |
| Faux positifs IDs dans code blocks | `grep` ne tracke pas l'état | Corrigé — utilisation d'`awk` avec tracking `c==0`/`c==1` |
| Section trop longue non détectée | H2 mal formaté (espace manquant) | Vérifier `## ` (dièse + espace) |


### 5.3 Intégration SUBLIMATOR

Le script est appelé automatiquement dans CP#5 du pipeline SUBLIMATOR :

> **CP#5 — LINT OBLIGATOIRE AVANT CP#5** : Exécuter le script de linting avant de soumettre le checkpoint.

Le prompt SUBLIMATOR (v28.4) liste explicitement les 7 checks du script et demande :

> *« Toute violation ❌ bloque la publication. Corriger et relancer jusqu'à zéro violation. »*

---

## §6 — NAVIGATION DANS LE PROJET

### 6.1 Ce qui est actif vs obsolète

| Fichier / Dossier | Statut | Remarque |
|-------------------|--------|----------|
| `truth-engine-v2/` | ✅ Actif | KERNEL v2, utiliser pour toute investigation |
| `KERNEL_v1_DEPRECATED.md` | ❌ Obsolète | Remplacé par `truth-engine-v2/KERNEL.md` |
| `kb/` | ❌ N'existe pas | Mentionné dans KERNEL_v1 — ne plus référencer |
| `tools/prompts/systems/SUBLIMATOR_v28.0.md` | ✅ Actif | Pipeline rédaction v28.4 |
| `tools/scripts/lint-article.sh` | ✅ Actif | 7 checks automatisés |
| `AGENTS.md` | ✅ Actif | Règles projet pour l'IA |
| `docs/VISION.md` | ✅ Actif | Philosophie générale |
| `archive/v1/STRUCTURE.md` | ❌ Obsolète | Parle de `kb/`, ne reflète pas la réalité |
| `docs/user/USER_GUIDE.md` | ⚠️ Partiellement obsolète | v8.0 — référence KERNEL v1, pas SUBLIMATOR |
| `docs/specs/WARP.md` | ⚠️ Non maintenu | Ancien système MCP, pas le pipeline actuel |
| `docs/specs/PRD.md` | ⚠️ Partiellement obsolète | Écrit pour le système WARP — le pipeline a évolué |
| `docs/specs/TAD.md` | ✅ Valide | Architecture technique |
| `truth-engine-v2/ARCHITECTURE.md` | ✅ Actif | Dépendances du module KERNEL v2 |
| `investigations/` | ✅ Actif | Toutes les investigations récentes |
| `articles/` | ✅ Actif | Articles finaux publiés |
| `audits/` | ✅ Actif | Audits SATURATION / APEX |
| `substack-online/` | ✅ Actif | Export Substack (HTML, CSV) |
| `sources/` | ✅ Actif | Documents sources bruts |
| `archive/` | ⚠️ Archive | Anciennes versions systèmes, à ne pas modifier |
| `archive/system-versions/` | ⚠️ Archive | Anciennes versions du kernel |
| `archive/prompts/` | ⚠️ Archive | Anciens prompts systèmes |


### 6.2 Cheatsheet : Où trouver quoi

| Je cherche... | Aller dans... |
|---------------|---------------|
| Comment lancer une investigation | `truth-engine-v2/KERNEL.md` + `truth-engine-v2/ARCHITECTURE.md` |
| Comment rédiger un article | `tools/prompts/systems/SUBLIMATOR_v28.0.md` |
| Quelles sont les LOIS | §3 de ce document |
| Vérifier mon article avant publication | `./tools/scripts/lint-article.sh article.md` |
| Conventions de nommage | §4.1 de ce document + `AGENTS.md` |
| Les règles d'éthique | `AGENTS.md` (section ÉTHIQUE DE LA VÉRITÉ) |
| La philosophie du projet | `docs/VISION.md` |
| L'index des investigations | `investigations/INDEX.md` |
| Les articles publiés | `articles/` |
| Les exports Substack | `substack-online/posts/` + `posts.csv` |
| Les outils de validation | `tools/scripts/` |
| Les prompts systèmes | `tools/prompts/systems/` |
| Les prompts spécifiques (ex: critique série) | `prompts/` |


### 6.3 Séquence de chargement recommandée (session IA)

Quand l'utilisateur dit « écris un article sur X » ou « lance une investigation sur X », le LLM doit charger les fichiers dans cet ordre :

```
1. AGENTS.md                    → Règles du projet, éthique, RTK, conventions
2. docs/specs/PIPELINE_ARTICLE.md  → Vue d'ensemble (ce document)
3. truth-engine-v2/KERNEL.md    → Kernel investigation
   (ou SUBLIMATOR selon la demande)
4. tools/prompts/systems/SUBLIMATOR_v28.0.md  → Pipeline rédaction
5. tools/scripts/lint-article.sh  → Script de validation final
   (lecture rapide, pas d'exécution)
```

---

## §7 — GLOSSAIRE

| Terme | Définition |
|-------|------------|
| **CP#1, CP#4, CP#5** | Checkpoints du pipeline SUBLIMATOR. Points de validation avec l'utilisateur. |
| **Census** | Étape Tier 1 : recensement de toutes les données disponibles |
| **Dialectique** | 3 perspectives complémentaires sur un sujet |
| **Digest** | Synthèse des données d'investigation |
| **EDI** | Epistemic Diversity Index — mesure la diversité des perspectives dans une investigation |
| **Écrivain/Critique/Correcteur/Arbitre** | Les 4 rôles du cycle multi-agent (Tier 2) |
| **Fact-Check** | Vérification croisée des faits avec sources |
| **HYPER_MATRICE** | Matrice de faits atomiques sourcés |
| **H1** | Titre principal de l'article (un seul, commence par `# `) |
| **H2** | Titre de section (`## `) |
| **H3** | Sous-section (`### `) |
| **KERNEL v1** | Ancien moteur d'investigation (déprécié) |
| **KERNEL v2** | Nouveau moteur d'investigation (modulaire, actif) |
| **Lint** | Vérification automatisée du fichier article |
| **LOI 1-8** | Règles de rédaction (voir §3) |
| **MnemoLite** | Base de mémoire persistante pour le LLM (traces des investigations passées) |
| **Quality Gate** | Dernière validation avant publication (humaine ou LLM) |
| **RTK** | Rust Token Killer — proxy CLI qui réduit la consommation de tokens de 60-90% |
| **SATURATION_AUDIT** | Audit de vérification complet d'une investigation |
| **SUBLIMATOR** | Pipeline de rédaction d'article (3 tiers, 8 LOIS, checkpoints) |
| **Tier 1/2/3** | Les 3 étapes du pipeline SUBLIMATOR (Blueprint, Cycle, Assemblage) |
| **Wolves** | Prédateurs identifiés dans une investigation (acteurs nuisibles) |

---

## §8 — CAS CONCRET : « Le peuple est le seul souverain »

Parcours réel de l'article `articles/2026-05-28_14-10_peuple-souverain-resistance_ARTICLE.md` à travers le pipeline.

**Contexte :** Article d'essai politique (pas une enquête factuelle). Pas d'investigation KERNEL formelle — les articles d'opinion ou d'essai peuvent sauter la phase §1. Le pipeline SUBLIMATOR s'applique à partir de §2 (rédaction en sections) avec validation LOIS + lint.

### Étape 1 — Investigation (phase amont)

Non applicable : l'article est un essai, pas une enquête sourcée. Certains articles ne nécessitent pas d'investigation KERNEL — le pipeline s'adapte.

### Étape 2 — Architecture narrative

Visible dans la structure de l'article final :

```
H1 : 🗡️ Le peuple est le seul souverain : le système de désorganisation
├── La machine        (introduction, paradoxe Weil + flux)
├── Le piège          (impuissance réflexive, Fisher + Sloterdijk)
├── L'écart           (légal vs légitime, dictature légale)
├── Le système de désorganisation (5 sous-sections §1-§5)
│   ├── §1 Fragmenter
│   ├── §2 Captiver
│   ├── §3 Obéir
│   ├── §4 Sidérer
│   └── §5 Dissoudre
├── La confession     (performatif, méta)
├── L'axiome          (thèse centrale répétée)
├── La dissolution    (esquisse de réponse)
├── Le choix          (conclusion binaire)
└── Sources           (19 URLs, LOI 1 ✅)
```

**Observations :**
- **H1** avec émoji 🗡️ (LOI 3 ✅ warning uniquement)
- **7 H2** sections de longueur variée
- **Gras** stratégique : 3-5 par section (LOI 6 ✅)
- **19 URLs** dans ## Sources (LOI 1 ✅)
- **Zéro ID interne** F###/D### (LOI 8 ✅)
- **Zéro **[LIEN_A_INSERER]** (LOI 8 ✅)
- **« Mais »/« Cependant »** : utilisation modérée (LOI 4 ✅)

### Étape 3 — Cycle multi-agent (Tier 2)

Pas de traces dans `_assemblage/sections/` — le cycle a probablement été exécuté en session LLM sans sauvegarde des fichiers intermédiaires. C'est un cas fréquent pour les articles simples ou les essais.

### Étape 4 — Lint (CP#5)

Exécution réelle du script :

```
$ ./tools/scripts/lint-article.sh articles/2026-05-28_14-10_peuple-souverain-resistance_ARTICLE.md

  ✅ LOI 1 : Sources présentes (19 URLs)
  ⚠️  LOI 3 : Émoji en H1
  ✅ LOI 4 : Transitions faibles
  ✅ LOI 5 : Calibration sections
  ✅ LOI 6 : Gras 3-5/section
  ✅ LOI 8 : IDs factices
  ✅ LOI 8 : LIEN_A_INSERER

  Résultat : 6 OK / 0 violations / 1 warnings
  EXIT: 0 ✅
```

**0 violations, exit 0 ✅** (6/7 checks passent, 1 warning LOI 3 non-bloquant — l'émoji 🗡️ est présent mais différent du 🔒 recommandé).

### Étape 5 — Publication

L'article est publié sur Substack : `giak.substack.com` sous le titre « Le peuple est le seul souverain : le système de désorganisation ».

### Enseignements

- Le pipeline n'est pas rigide : les essais peuvent sauter l'investigation KERNEL.
- Le cycle multi-agent (Tier 2) peut être exécuté sans traces disques.
- Le lint script reste obligatoire même pour les articles sans investigation.
- Un warning LOI 3 (émoji non standard) est acceptable — jugement humain requis.

---

## §9 — CE QUI MANQUE (ROADMAP)

Le pipeline actuel couvre ~80 % du workflow. Les points d'amélioration identifiés :

| Manque | Impact | Solution possible |
|--------|--------|-------------------|
| **Orchestration automatisée** | Friction : l'utilisateur doit naviguer entre 5+ fichiers manuellement | Makefile ou script d'orchestration qui enchaîne investigation → rédaction → lint |
| **Templates démarrage rapide** | Perte de temps : chaque nouvelle investigation repart de zéro | Commander templates via `truth-engine-v2/output/TEMPLATE.md` |
| **Traçabilité multi-agent** | Impossible de rejouer un cycle Écrivain/Critique pour debug | Convention : sauvegarder TOUJOURS les fichiers `_ECRIVAIN_v1.md`, `_CRITIQUE_v1.md` dans `_assemblage/sections/` |
| **Métriques de qualité** | Pas de mesure objective de la qualité d'un article | Dashboard : taux de PASS au lint par article, temps moyen par section, etc. |

