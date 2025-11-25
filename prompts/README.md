# Prompts — Guide d'Utilisation

**Version :** 4.0
**Date :** 2025-11-25
**Truth Engine :** v10.1 TEXTUAL (Progressive Activation + Analyse DSL Obligatoire)
**Tweet Engine :** v4.0 Hook-First (MICRO/MEDIUM/LONG + Fact-Check + Auto-Save)
**Usage :** Guide pragmatique des prompts Truth Engine + Dashboard suivi

---

## 📁 Structure

```
prompts/
├── README.md                           # Ce guide
├── systems/                            # System prompts agentiques
│   ├── tweet-engine-v4.0.md           # CURRENT: Hook-first viral engine (MICRO/MEDIUM/LONG)
│   ├── tweet-engine-v3.0.md           # LEGACY: Articles longs fact-checkés (MODE 1-4)
│   └── promptsmith-leonardo-v2.0.md   # CURRENT: Leonardo.ai prompts
├── outputs/                            # Productions finales
│   └── 2025-11-23_trump-ukraine-braquage.md  # Exemple tweet APEX
└── archive/                            # Anciennes versions
    ├── tweet-long-2025.md             # v4.7 (archived, replaced by tweet-engine-v3.0)
    ├── tweet-engine-v1.0.md           # v1.0 (REJECTED - approche prescriptive)
    └── ...                            # Anciennes itérations
```

---

## 📋 Dashboard Prompts & Utilisation

| Prompt | Version | Dernière MAJ | Statut | Usage | Performance |
|--------|---------|--------------|--------|-------|-------------|
| [systems/tweet-engine-v4.0.md](systems/tweet-engine-v4.0.md) | v4.0 | 2025-11-25 | ✅ **NEW** | Hook-first viral (MICRO/MEDIUM/LONG) + fact-check + auto-save | 1 output testé |
| [systems/tweet-engine-v3.0.md](systems/tweet-engine-v3.0.md) | v3.0 | 2025-11-25 | 📦 Legacy | Articles longs fact-checkés (MODE 1-4) | Remplacé par v4.0 |
| [systems/promptsmith-leonardo-v2.0.md](systems/promptsmith-leonardo-v2.0.md) | v2.0 | 2025-11-20 | ✅ Stable | Génération prompts Leonardo.ai | Text accuracy 90%+ |

### Métriques Truth Engine

| Métrique | Nov 2025 | Objectif Quotidien | Objectif Mensuel | Tendance |
|----------|----------|-------------------|------------------|----------|
| **Investigations APEX** (longues) | 3 | **1/jour** | **30/mois** | 📈 |
| **Infographies IA** (Leonardo) | 0 | **1/jour** (avec APEX) | **30/mois** | 🔄 En cours |
| **Investigations SIMPLE/MEDIUM** | 0 | **3-4/jour** | **90-120/mois** | 🎯 Nouveau |
| **Tweets courts** (quick analyses) | 0 | **3-4/jour** | **90-120/mois** | 🎯 Nouveau |
| EDI moyen investigations APEX | 0.68 | ≥0.70 | ≥0.75 | ⚠️ À améliorer |
| Reach moyen tweets (post-v4.0) | - | 500+ vues | 1000+ vues | 🔄 Test en cours |

### Évolutions Récentes

| Date | Changement | Impact | Fichiers |
|------|------------|--------|----------|
| 2025-11-25 | **tweet-engine v4.0 (hook-first)** | Architecture 6 layers, hook-first, 3 modes (MICRO/MEDIUM/LONG), auto-save | systems/tweet-engine-v4.0.md |
| 2025-11-25 | **tweet-engine v3.0 → Legacy** | Remplacé par v4.0, garde pour articles longs si besoin | systems/tweet-engine-v3.0.md |
| 2025-11-23 | **tweet-engine v2.0 (agentique)** | Approche réflexive MODE 1-4 vs prescriptive v1.0 | (archived) |
| 2025-11-23 | Organisation arborescence (systems/outputs/archive) | Meilleure structure prompts | prompts/* |
| 2025-11-20 | Promptsmith Leonardo v2.0 | Best practices 2025 (Ideogram 3.0, prompts 200-400 chars) | systems/promptsmith-leonardo-v2.0.md |
| 2025-11-18 | **tweet-long v4.7 (archived)** | Character substitution, visual bypass, DSA-safe | archive/tweet-long-2025.md |

---

## 🚀 PROTOCOLE COMPLET : COPY-PASTE

**Instructions :** Ouvrir cette section → Copier commandes → Coller dans terminal → Exécuter

---

### 📍 Workflow APEX (Investigation Longue) — 1/jour

**Durée totale :** 3h15 (investigation 2h30 + tweet 30min + infographie 15min)

**Commandes complètes (copier-coller) :**

```bash
# ═══════════════════════════════════════════════════════
# ÉTAPE 1 : INVESTIGATION APEX (2h30)
# ═══════════════════════════════════════════════════════

claude-code "Investigation APEX: '[SUJET DU JOUR]'.
Load system.md + kb/COGNITIVE_DSL_CORE.md.
Progressive concept activation. Full textual DSL analysis mandatory.
L0-L9 full cascade. WOLF MODE if political.
Target: EDI≥0.70, sources≥15, wolves≥8 if political.
Patterns: ICEBERG MAX, MONEY, NETWORK, TEMPORAL.
Save logs/$(date +%Y-%m-%d_%H-%M)_[sujet-court].md"

# Résultat: logs/2025-11-18_09-30_plf-2025.md

# ═══════════════════════════════════════════════════════
# ÉTAPE 2 : GÉNÉRATION TWEET AGENTIQUE (30min)
# ═══════════════════════════════════════════════════════

claude-code "Load prompts/systems/tweet-engine-v3.0.md.

MODE 1 (PLAN): Analyze investigation logs/[FICHIER_CRÉÉ_ÉTAPE_1].md
Generate 10-section narrative plan (Acte I-II-III structure).

MODE 2 (SECTIONS): Write sections progressively.
Budget: 25,000 chars, format citoyen (no jargon).

MODE 3 (ASSEMBLY): Polish narrative flow.

MODE 4 (VALIDATE): Fact-check dates/sources.

Save prompts/outputs/$(date +%Y-%m-%d)_[sujet-court].md"

# Résultat: prompts/outputs/2025-11-23_plf-2025.md

# ═══════════════════════════════════════════════════════
# ÉTAPE 3 : GÉNÉRATION INFOGRAPHIE LEONARDO.AI (15min)
# ═══════════════════════════════════════════════════════

claude-code "Load prompts/systems/promptsmith-leonardo-v2.0.md.

Generate infographic from VISUAL BYPASS CONCEPT:
- Source: logs/[FICHIER_CRÉÉ_ÉTAPE_2].md section VISUAL BYPASS
- Format: 16:9 (horizontal X/Twitter)
- Texte zones: [COPIER DEPUIS VISUAL BYPASS, ≤25 CHAR PAR ZONE]
- Palette: [COPIER DEPUIS VISUAL BYPASS]
- Style: [COPIER DEPUIS VISUAL BYPASS, description neutre sans marques]

Output:
- 3 variants (Balance, Iceberg, Colonnes)
- Comparison table (clarity, impact, DSA-safe)
- Fusion final (meilleur des 3)
- Ready-to-use Leonardo.ai prompts"

# Résultat: 4 prompts Leonardo prêts à copier
# → Aller sur Leonardo.ai → Coller prompt Fusion → Générer

# ═══════════════════════════════════════════════════════
# ÉTAPE 4 : PUBLICATION (T-10 à T+30)
# ═══════════════════════════════════════════════════════

# T-10 min : DM 5-10 followers "Thread dans 10 min, RT si possible ?"
# T0      : Tweet court + infographie Leonardo
# T+2 min : Thread long (réponse au tweet court)
# T+5 min : Vérifier 10+ RT/likes (sinon @elonmusk si <5)
# T+30 min: Répondre commentaires

# Timing optimal: Mardi-Jeudi 9h-11h ou 18h-20h
```

**Exemples SUJET DU JOUR (APEX) :**
- "Budget PLF/PLFSS 2025 écart HCFP 60 Md€ vs 3 Md€"
- "McKinsey perquisitions novembre 2025 chronologie scandales"
- "Acoss 2027 crise financement trésorerie Sécu Banque Territoires"
- "HATVP sous-financement conflits intérêts pantouflage 1000/an"

**Diversification hebdomadaire :** 60% sensible (Mar, Ven, Dim) / 40% neutre (Lun, Mer, Jeu, Sam)

---

### 📍 Workflow SIMPLE/MEDIUM (Investigation Rapide) — 3-4/jour

**Durée totale :** 20-40 min par investigation (investigation 15-30min + tweet 5-10min)

**Commandes complètes (copier-coller) :**

```bash
# ═══════════════════════════════════════════════════════
# ÉTAPE 1 : INVESTIGATION SIMPLE/MEDIUM (15-30min)
# ═══════════════════════════════════════════════════════

claude-code "Analyse: '[SUJET RAPIDE]'.
Load system.md + kb/COGNITIVE_DSL_CORE.md.
Progressive activation. Full textual analysis.
Target: EDI≥0.30 (SIMPLE) ou ≥0.50 (MEDIUM), sources≥5-10.
L0-L2 protocols (Surface, Acteurs, Cui Bono).
Save logs/$(date +%Y-%m-%d_%H-%M)_[sujet-court].md"

# Résultat: logs/2025-11-18_14-20_salaire-median-2024.md

# ═══════════════════════════════════════════════════════
# ÉTAPE 2 : TWEET COURT (5-10min)
# ═══════════════════════════════════════════════════════

claude-code "Load prompts/systems/tweet-engine-v3.0.md.

MODE 1 (PLAN): Analyze investigation logs/[FICHIER_CRÉÉ_ÉTAPE_1].md
Generate SHORT tweet plan (3-4 sections, <2000 chars).

MODE 2 (SECTIONS): Write concise narrative.
Format citoyen, no jargon, sources institutionnelles.

Save prompts/outputs/$(date +%Y-%m-%d)_[sujet-court]-tweet.md"

# Résultat: Tweet prêt à publier (copier-coller)

# ═══════════════════════════════════════════════════════
# ÉTAPE 3 : PUBLICATION DIRECTE
# ═══════════════════════════════════════════════════════

# Copier tweet → Publier directement (pas de protocol T-10/T0/T+5)
# Répondre commentaires si engagement >20 likes
```

**Exemples SUJET RAPIDE (SIMPLE/MEDIUM) :**

**SIMPLE (20min) :**
- "Salaire médian France 2024 évolution vs inflation"
- "Taux chômage octobre 2025 comparaison UE"
- "Déficit budgétaire France 2025 prévisions vs 2024"

**MEDIUM (30-40min) :**
- "Réforme assurance chômage 2025 impact 500k demandeurs"
- "Loi immigration votes Assemblée novembre 2025"
- "Prix énergie hiver 2025 bouclier tarifaire fin"

**Répartition quotidienne :**
- 14h00-14h20 : Investigation 1 (SIMPLE neutre, fact-check)
- 14h20-14h40 : Investigation 2 (SIMPLE neutre, data viz)
- 14h40-15h10 : Investigation 3 (MEDIUM neutre ou sensible)
- 15h10-15h40 : Investigation 4 (MEDIUM, optionnel)

---

## ⚡ Nouveautés Truth Engine v10.1 (2025-11-25)

### 🎯 Progressive Concept Activation

**Innovation majeure** : Truth Engine v10.1 charge uniquement les concepts pertinents au lieu des 148 concepts systématiquement.

**Fonctionnement :**
1. **Core scan** : 5 concepts essentiels analysent le texte (Ξ, €, Λ, Ω, Ψ)
2. **Score** : Chaque concept reçoit un score 0-10
3. **Activation** : Si score ≥5 → Charge cluster thématique (10-15 concepts liés)
4. **Économie** : -92% mémoire (28KB vs 370KB), 4× plus rapide

**Résultat :**
- Utilisation concepts : 2.7% → **100%** (seuls concepts pertinents chargés)
- Patterns détectés : 1 → **7+** (meilleure détection)
- Performance : **4× plus rapide**

### 📊 Analyse Textuelle DSL [OBLIGATOIRE]

**Nouveauté v10.1** : L'analyse textuelle DSL est maintenant **MANDATORY** dans tous les outputs.

**Structure output PART 1 (toujours présente) :**

```markdown
## ANALYSE TEXTUELLE DSL

### Concepts Activés (X/148)
Λ (FRAMING) = 8/10
  Quote: "texte exact du tweet/article"
  Technique: EMOTIONAL_TRIGGER + FALSE_DICHOTOMY
  Révèle: Binary framing cachant complexité

[Minimum 10 concepts analysés avec scores + quotes]

### Techniques Rhétoriques
1. EMOTIONAL_TRIGGER (9/10)
2. FALSE_DICHOTOMY (9/10)
3. SYNECDOQUE (8/10)
[...]

### Déconstruction Sémantique
1. SOUS-ENTENDUS : [implications non dites]
2. NON-DITS : [omissions stratégiques]
3. CONTRADICTIONS : [tensions internes]
4. PRÉSUPPOSÉS : [assumptions cachées]

### Cartographie Dialectique
THÈSE : [Position du texte]
ANTITHÈSE : [Position opposée]
SYNTHÈSE : [Ce qui se passe réellement]
TENSION : [Contradiction non résolue]
```

**Vocabulaire précis (exit "herméneutique") :**
- ~~"Analyse herméneutique"~~ → **"Analyse textuelle DSL"**
- ~~"Herméneutique divergente"~~ → **"Génération d'hypothèses"**
- ~~"Synthèse herméneutique"~~ → **"Cartographie dialectique"**
- ~~"Patterns herméneutiques"~~ → **Techniques rhétoriques**

**Exemple complet** : [prompts/outputs/2025-11-25_bardella-mercosur-analyse.md](outputs/2025-11-25_bardella-mercosur-analyse.md)

### 🔧 Prompt Minimal v10.1

```bash
"Analyse: '[VOTRE SUJET]'.
Load system.md + kb/COGNITIVE_DSL_CORE.md.
Progressive activation. Full textual DSL analysis.
Truth Engine protocol."
```

**Automatique** :
- ✅ Activation progressive concepts
- ✅ Analyse textuelle DSL (PART 1)
- ✅ Investigation principale (PART 2)
- ✅ Diagnostics techniques (PART 3)
- ✅ WOLF report si applicable (PART 4)

---

## 🔍 Truth Engine — Investigation Protocol

### Niveaux de Complexité (Auto-Détecté)

Truth Engine évalue automatiquement la complexité du sujet (0-10 scale, 6 dimensions) et adapte les ressources.

| Niveau | Complexité | Critères | Sources Min | EDI Min | Exemples |
|--------|------------|----------|-------------|---------|----------|
| **SIMPLE** | 0-3 | Factuel, local, court terme | 5 | 0.30 | Salaire médian France, taux chômage |
| **MEDIUM** | 4-6 | Multi-acteurs, national, moyen terme | 10 | 0.50 | Réforme retraites, loi immigration |
| **COMPLEX** | 7-8 | Systémique, international, long terme | 15 | 0.70 | PLF 2025, McKinsey scandales |
| **APEX** | 9-10 | Géopolitique, réseaux pouvoir, historique | 20+ | 0.80 | Ukraine/OTAN, capture institutionnelle |

### Protocoles d'Investigation (L0-L9)

| Level | Nom | Durée | Description | Quand activer |
|-------|-----|-------|-------------|---------------|
| **L0** | Surface | 5min | Recherche basique, définitions | Toujours (baseline) |
| **L1** | Acteurs | 10min | Qui sont les protagonistes ? Qui paie ? | MEDIUM+ |
| **L2** | Cui Bono | 15min | Qui profite ? (visible ×1, shadow ×10, black ×100) | COMPLEX+ |
| **L3** | Patterns | 20min | Détection patterns (ICEBERG, MONEY, BIO, etc.) | COMPLEX+ |
| **L4** | Timing | 25min | Analyse temporelle, coïncidences prob<0.01% ? | COMPLEX+ |
| **L5** | Archéologie | 30min | Contexte historique, précédents | APEX |
| **L6** | Counter-Narrative | TOUJOURS | Assume official=lie, cherche narratifs alternatifs | MANDATORY |
| **L7** | Warfare | Si ⚔≥2 | Patterns conflit, armes, financement | Géopolitique |
| **L8** | Network | Si 🌐≥2 | Cartographie réseaux influence, pantouflage | Systémique |
| **L9** | Temporal | Si ⏰≥2 | Patterns historiques, cycles, récurrences | Long terme |

### Options d'Investigation

**Basic Investigation (Quick) :**
```bash
claude-code "Analyse: [SUJET].
Load system.md + kb/COGNITIVE_DSL_CORE.md.
Progressive activation. Full textual analysis.
Truth Engine protocol."
```
→ Complexité auto-détectée, protocoles L0-L6 minimum
→ Analyse textuelle DSL obligatoire

**Investigation Ciblée (Specify Depth) :**
```bash
claude-code "Analyse: [SUJET].
Load system.md + kb/COGNITIVE_DSL_CORE.md.
Progressive activation. Full textual analysis.
Investigation L2 CUI_BONO + L8 NET.
Target: EDI≥0.60, sources≥12."
```
→ Force protocoles spécifiques L2 (qui profite) + L8 (réseaux)
→ Analyse textuelle DSL obligatoire

**Investigation APEX (Full Depth) :**
```bash
claude-code "Investigation APEX: [SUJET].
Load system.md + kb/COGNITIVE_DSL_CORE.md.
Progressive activation. Full textual DSL analysis mandatory.
Target: EDI≥0.80, sources≥20, wolves≥12 if political.
ICEBERG MAX. L0-L9 full cascade.
Save logs/$(date +%Y-%m-%d)_[sujet].md"
```
→ Tous protocoles L0-L9, pattern detection max, wolf hunting
→ Analyse textuelle DSL complète (concepts, techniques, déconstruction, dialectique)

**Investigation Tree (Multi-Branch Dialectique) :**
```bash
claude-code "Investigation APEX: [SUJET].
Load system.md + kb/COGNITIVE_DSL_CORE.md + kb/INVESTIGATION_TREE.md.
Progressive activation. Full textual DSL analysis mandatory.
Multi-branch dialectical analysis.
Target: EDI≥0.80, sources≥20, wolves≥12.
COMPARABLES_ASYMMETRY across branches."
```
→ Hypothèses adversariales parallèles, comparaison asymétries
→ Analyse textuelle DSL pour chaque branche

### Patterns Détectables

Truth Engine peut détecter 20+ patterns manipulation. Activation automatique si signaux présents.

| Pattern | Symbole | Trigger | Description |
|---------|---------|---------|-------------|
| **ICEBERG** | Ξ | Omissions ≥3 | 90% réalité cachée, 10% visible |
| **MONEY** | € | Montants ≥3 | Flux financiers cachés, cui bono |
| **BIOPOWER** | Σ | Santé/corps | Contrôle populations via santé |
| **NETWORK** | 🌐 | Acteurs ≥5 | Réseaux influence, pantouflage |
| **WARFARE** | ⚔ | Conflit ≥2 | Proxy wars, armes, financement |
| **TEMPORAL** | ⏰ | Historique ≥2 | Cycles, précédents, récurrences |
| **DIVERSION** | Φ | Spectacle | Distraction pendant vol légal |
| **INVERSION** | Ω | Contradiction | "Guerre=paix", réalité inversée |
| **FRAMING** | Λ | Fausses dichotomies | Gauche/Droite cache vrais enjeux |
| **SIDERATION** | Ψ | Overload | Saturation cognitive (34GB/jour > 5GB seuil) |

**Activer pattern spécifique :**
```bash
claude-code "Analyse [SUJET]. Load system.md + kb/.
Active ICEBERG MAX + MONEY deep + NET analysis."
```

### Wolf Hunting (Cartographie Acteurs)

Pour sujets politiques/géopolitiques/corporate, Truth Engine identifie bénéficiaires cachés.

**Seuils :**
- **Politique** : ≥8 individus (politiciens, conseillers, lobbyistes)
- **Corporate** : ≥5 entreprises/dirigeants
- **Enablers** : ≥30% total (médias, académiques, think tanks, consulting)

**Activer Wolf Mode :**
```bash
claude-code "Analyse [SUJET]. Load system.md + kb/.
WOLF HUNTER MODE: Individual actors ≥8, enablers ≥30%.
L2 CUI_BONO + L8 NET mandatory."
```

**Output WOLF Report :**
- Bénéficiaires visibles (×1)
- Bénéficiaires shadow (×10)
- Bénéficiaires black (×100)
- Ratio individus/institutions ≥50%
- Network graph (pantouflage, revolving door)

### Query Optimization (v8.3 Automatique)

Truth Engine optimise automatiquement les recherches web complexes.

**Fonctionnement :**
- Détecte queries >5 keywords
- Split en 2-3 queries simples (3-4 keywords chacune)
- MCP (DuckDuckGo) essayé en premier
- WebSearch (Google API) fallback si résultats vides
- Agrégation et déduplication

**Bénéfices :**
- Taux productif : 0-40% baseline → 80-100% optimisé
- Découverte PRIMARY SOURCES (◈) que queries complexes manquent
- EDI boost typique : +0.15-0.27

**Automatique :** Rien à faire, optimisation transparente. Voir `[QUERY_OPTIMIZATION]` metrics dans diagnostics Part 2.

### Exemples Complets

**1. Investigation Simple (Fact-Check) :**
```bash
claude-code "Analyse: 'Chômage 7.4% France oct 2024'.
Load system.md + kb/COGNITIVE_DSL_CORE.md.
Progressive activation. Full textual analysis.
Verify official sources."
```
→ Complexité: SIMPLE (2/10)
→ Sources: 5 (INSEE, Eurostat, OECD)
→ Durée: 10 min
→ Output: Validation fact + contexte + analyse textuelle DSL

**2. Investigation Medium (Réforme) :**
```bash
claude-code "Analyse: 'Réforme retraites 2023 impacts'.
Load system.md + kb/.
L2 CUI_BONO: Qui profite report déficits 2027 ?
Target: EDI≥0.50, sources≥10."
```
→ Complexité: MEDIUM (5/10)
→ Sources: 12 (Cour comptes, COR, syndicats, think tanks)
→ Patterns: MONEY €++, TEMPORAL ⏰+
→ Durée: 45 min

**3. Investigation Complex (Scandale Systémique) :**
```bash
claude-code "Investigation APEX: 'McKinsey contrats publics France 2017-2025'.
Load system.md + kb/.
L2 CUI_BONO + L4 TIMING + L8 NET.
WOLF MODE: Individual actors ≥8, pantouflage tracking.
Target: EDI≥0.70, sources≥15."
```
→ Complexité: COMPLEX (8/10)
→ Sources: 23 (Sénat, AFP, Mediapart, Consultor.fr, HATVP)
→ Patterns: MONEY €+++, NETWORK 🌐+++, TEMPORAL ⏰++
→ Wolves: 12 individus (Tadjeddine, ministres, consultants)
→ Durée: 2h30

**4. Investigation APEX (Géopolitique) :**
```bash
claude-code "Investigation APEX: 'Ukraine OTAN expansion 1991-2022'.
Load system.md + kb/INVESTIGATION_TREE.md.
Multi-branch: Hypothesis NATO (Western narrative) vs Hypothesis Russia (adversary).
L0-L9 full cascade + COMPARABLES_ASYMMETRY.
H7_OVERRIDE: Query RT, TASS, CGTN (adversary sources).
Target: EDI≥0.80, sources≥20, geo_diversity≥0.50."
```
→ Complexité: APEX (9/10)
→ Sources: 28 (NYT, WaPo, RT, TASS, academic papers, Wikileaks cables)
→ Patterns: WARFARE ⚔+++, NETWORK 🌐+++, TEMPORAL ⏰+++, INVERSION Ω++
→ EDI: 0.82 (multi-perspective dialectique)
→ Durée: 4h

---

## 🚀 Workflows Par Cas d'Usage

### 1️⃣ Investigation Truth Engine Complète

**Cas d'usage :** Analyser sujet complexe (politique, économie, géopolitique)

```bash
# Étape 1: Investigation APEX
claude-code "Investigation APEX: [SUJET].
Load system.md + kb/ via MnemoLite semantic search.
Target: EDI≥0.70, sources≥15, wolves≥8 if political.
Save logs/$(date +%Y-%m-%d)_[sujet].md"

# Résultat: logs/YYYY-MM-DD_sujet.md
```

**Critères qualité :**
- EDI ≥0.70 (COMPLEX/APEX)
- Sources ≥15 (dont ≥3 primaires ◈)
- Cui bono identifié (L2)
- Patterns détectés (ICEBERG, MONEY, etc.)
- Wolves cartographiés si politique (≥8 individus)

---

### 2️⃣ Tweet Agentique (v2.0)

**Cas d'usage :** Transformer investigation → Tweet narratif structuré

```bash
# Étape 1: Investigation (voir workflow 1)

# Étape 2: Génération tweet agentique MODE 1-4
claude-code "Load prompts/systems/tweet-engine-v3.0.md.

MODE 1 (PLAN): Analyze logs/[fichier].md
MODE 2 (SECTIONS): Write 10 sections progressively (25K chars budget)
MODE 3 (ASSEMBLY): Polish narrative
MODE 4 (VALIDATE): Fact-check

Save prompts/outputs/YYYY-MM-DD_[sujet].md"
```

**Résultat :**
- Tweet long narratif (Acte I-II-III structure)
- Format citoyen (no jargon technique, blockquotes citations)
- Validation progressive section par section
- Architecture agentique :
  - ✅ Approche réflexive (questions vs prescriptif)
  - ✅ Baby-step execution (validation loops)
  - ✅ Format citoyen (traduit DSL, no tableaux, no préfixes techniques)
  - ✅ Fact-checking automatique dates/sources

**Protocole publication :**
- **T-10 min** : DM 5-10 followers "Thread dans 10 min, RT si possible ?"
- **T0** : Tweet court + infographie
- **T+2 min** : Thread long (réponse)
- **T+5 min** : Vérifier 10+ RT/likes
- **T+30 min** : Répondre commentaires
- **Timing optimal** : Mardi-Jeudi 9h-11h ou 18h-20h

---

### 3️⃣ Infographie IA (Leonardo.ai)

**Cas d'usage :** Générer infographie data viz avec texte précis

```bash
# Étape 1: Préparer brief (concept visuel de votre investigation/tweet)

# Étape 2: Générer prompts Leonardo
claude-code "Load prompts/systems/promptsmith-leonardo-v2.0.md.

User brief:
- Format: 16:9
- Texte zones: [MAX 25 CHAR PAR ZONE]
- Palette: [COULEURS HEX]
- Style: [DESCRIPTION NEUTRE SANS MARQUES]

Generate 3 variants + fusion final."
```

**Résultat :**
- 3 variants (A, B, C) avec prompts complets
- Comparison table (scoring clarity/impact/text quality)
- Fusion finale optimale
- Settings Leonardo.ai (Ideogram 3.0, Prompt Magic 0.75, Guidance 8, RAW mode)

**Utilisation Leonardo.ai :**
1. Copier "Fusion (Final) - Positive Prompt"
2. Copier "Negative Prompt"
3. Settings : Ideogram 3.0, 16:9, Prompt Magic 0.75, Guidance 8, RAW mode ON
4. Generate 6-8 images
5. Sélectionner meilleure (vérifier texte sans misspellings)

**⚠️ Contraintes critiques :**
- Texte ≤25 caractères par zone textuelle
- Éviter marques/logos connus
- Utiliser Ideogram 3.0 (meilleur pour texte vs Phoenix)

---

## 📚 Référence Rapide Prompts

### systems/tweet-engine-v4.0.md ⭐ NEW

**Fonction :** Investigation Truth Engine → Tweet viral (hook-first, 3 longueurs)

**Architecture 6 layers :**
- **MODE 0** : Setup interactif (length auto-détecté, user confirme)
- **LAYER 1** : Analyse investigation (FactLedger, AcronymLedger)
- **LAYER 2** : Hook Generator (6 formulas, premiers 250 chars critiques)
- **LAYER 3** : Content Engine (MICRO/MEDIUM/LONG)
- **LAYER 4** : Fact-check (WebSearch, corrections auto)
- **LAYER 5** : Quality Gates (5 checks: structure, acronymes, anti-LLM, accessibility, length)
- **LAYER 6** : Auto-save (logs/{date}_tweet_{subject}_{MODE}.md)

**3 modes longueur :**

| Mode | Chars | Words | Sections | Usage |
|------|-------|-------|----------|-------|
| **MICRO** | <500 | <100 | 0 | Hook pur, max viral |
| **MEDIUM** | 1500-2500 | 350-400 | 3-5 | Analyse développée |
| **LONG** | 8000-25000 | 1500-4000 | 7-9 | Synthèse investigation complète |

**6 hook formulas (auto-sélection) :**

| Formula | Pattern | Trigger |
|---------|---------|---------|
| PROVOCATIVE | "Pourquoi personne ne parle de X ?" | controversy ≥7 |
| CONTRARIAN | "On vous dit X. Les chiffres disent Y." | debunks_narrative |
| CONSEQUENCE | "Votre facture augmente. Voici pourquoi." | citizen_impact |
| PATTERN | "3 ministres. 3 versions. 0 cohérence." | has_contradiction |
| EMOTIONAL | "187,000€/an. C'est ce que gagne X." | default |
| REVELATION | "Document interne. Ce qu'il révèle." | has_primary_source |

**3 user checkpoints :**
1. Après setup (confirme length)
2. Après hook (valide avant contenu)
3. Après quality gates (approbation finale)

**Commandes :**
```bash
# Auto-detect length
Mode TWEET: logs/investigation.md

# Force specific length
Mode TWEET MICRO: logs/investigation.md
Mode TWEET MEDIUM: logs/investigation.md
Mode TWEET LONG: logs/investigation.md
```

**Philosophy :** "Stop the scroll first. Inform after. Verify always."

**Design doc :** [docs/plans/2025-11-25-tweet-engine-v4-design.md](../docs/plans/2025-11-25-tweet-engine-v4-design.md)

---

### systems/tweet-engine-v3.0.md (Legacy)

**Fonction :** Investigation Truth Engine → Tweet long narratif (approche agentique)

**Inputs requis :**
- Investigation Truth Engine complète (logs markdown)
- Ou données brutes à analyser (3 investigations max pour agrégation)

**Outputs :**
1. Tweet long narratif (Acte I-II-III, 10-11 sections, 25K chars budget)
2. Format citoyen (no jargon DSL, blockquotes citations, no tableaux)
3. Validation progressive (fact-checking dates/sources automatique)

**Architecture MODE 1-4 :**
- **MODE 1 (⊙ PLAN)** : Maturation cognitive via 4 questions réflexives (Essence, Pattern, Révélation, Architecture)
- **MODE 2 (⊕ SECTION)** : Baby-step execution, écriture section par section avec validation loops
- **MODE 3 (✓ ASSEMBLY)** : Polissage narratif, cohérence globale
- **MODE 4 (🔍 VALIDATE)** : Fact-check exhaustif (dates, montants, acteurs, procédures)

**Principes non-négociables :**
- Chiffres exacts > adjectifs vagues
- Honnêteté brutale (gaps documentés)
- Pédagogie citoyenne (traduire DSL en langage naturel)
- Cui bono systématique
- Hook immédiat + formule finale mémorable

**Formatting citoyen :**
- ❌ INTERDIT : Préfixes techniques ("⊕ SECTION 1"), tableaux markdown, symboles Truth Engine (◈◉○, Ξ:7)
- ✅ AUTORISÉ : Titres narratifs simples, gras/italique, séparateurs `---`, blockquotes `> ` pour citations

**Philosophie v2.0 :**
- Approche **réflexive** (guider le LLM avec questions) vs **prescriptive** (steps rigides)
- "Il faut guider le LLM, pas lui dire comment penser"
- Sublime investigations en récit, ne réduit pas à checklist

**Fichier :** 22KB, 4 modes agentiques, prompt réflexif complet

**Différence vs v1.0 (REJECTED) :**
- v1.0 : Approche prescriptive (steps 1-10 rigides)
- v2.0 : Approche réflexive (questions fondamentales → maturation cognitive)

---

### systems/promptsmith-leonardo-v2.0.md

**Fonction :** Agent concepteur prompts Leonardo.ai optimisés 2025

**Inputs requis :**
- Format (16:9 ou 4:5)
- Texte exact (≤25 char par zone)
- Palette couleurs (HEX codes)
- Style (description neutre sans marques)

**Outputs :**
1. Variant A (approche 1)
2. Variant B (approche 2)
3. Variant C (approche 3)
4. Comparison table (scoring)
5. Fusion finale (optimal A+B+C)

**Ground Truth Leonardo 2025 :**
- **Ideogram 3.0** : MEILLEUR pour texte dans images
- **Phoenix 1.0** : Prompt adherence extrême, contexte complexe
- Prompt optimal : 200-400 chars (vs ancien mythe 1200-1500)
- Negative prompts : OBLIGATOIRES
- Texte format : `the text "EXACT"` avec quotation marks
- Limite texte : ≤25 caractères (pas ≤3 mots!)

**Settings recommandés :**
- Model: Ideogram 3.0 (text) ou Phoenix 1.0 (complex)
- Prompt Magic: 0.75
- Guidance: 8
- RAW Mode: ON si prompt >400 chars
- Aspect Ratio: 16:9 (horizontal) ou 4:5 (vertical)
- Negative Prompt: ON
- Number of Images: 6-8

**Fichier :** 237 lignes, 6 recherches web 2025, best practices validées

---

## 🔧 Maintenance & Amélioration

### Mettre à jour un prompt

```bash
# 1. Identifier gap/amélioration
# Exemple: EDI faible, pattern manqué, shadowban persistant

# 2. Éditer fichier prompt
nano prompts/[prompt-file].md

# 3. Incrémenter version
# Exemple: v4.0 → v4.1

# 4. Documenter changement dans Dashboard ci-dessus

# 5. Tester avec investigation réelle
claude-code "Apply prompts/[prompt-file].md v4.1 on [test-case]"

# 6. Valider performance (reach, EDI, qualité texte)
# Si OK → commit, sinon rollback
```

### Signaler un problème

**Prompt systems/tweet-engine-v3.0.md :**
- Section trop longue → Ajuster budget allocation
- Erreur dates/sources non détectée → Améliorer MODE 4 (VALIDATE)
- Jargon DSL non traduit → Renforcer règles formatting citoyen
- Baby-step validation skippée → Ajouter contraintes MODE 2

**Prompt systems/promptsmith-leonardo-v2.0.md :**
- Misspellings fréquents → Ajuster longueur texte ou negative prompts
- Style visuel incorrect → Affiner description style
- Prompt trop long → Activer RAW mode ou simplifier

---

## 📖 Cas d'Usage Complets

### Exemple 1 : PLF/PLFSS 2025 (Nov 2025)

**Investigation → Tweet → Infographie**

```bash
# ÉTAPE 1: Investigation APEX (3h)
claude-code "Analyse PLF 2025 et PLFSS 2025.
Load system.md + kb/.
Target: EDI≥0.70, sources≥15, L0-L9 deep.
ICEBERG MAX."

# Résultat: logs/2025-11-18_PLF-PLFSS-2025-FAISCEAU-INDICES.md
# EDI: 0.68, Sources: 65 web searches, 7 révélations convergentes

# ÉTAPE 2: Tweet Agentique v2.0 (30 min)
claude-code "Load prompts/systems/tweet-engine-v3.0.md.
MODE 1 (PLAN): Analyze PLF/PLFSS investigation.
MODE 2-3: Write 10 sections, polish narrative.
MODE 4: Fact-check dates/montants.
Save prompts/outputs/2025-11-23_budget-2025.md"

# Résultat:
# - Tweet long: 10 sections narratives, 7 révélations, Acte I-II-III
# - Format citoyen: No jargon DSL, blockquotes citations clés
# - Validation: Dates/montants fact-checked automatiquement
# - Structure: Hook → Révélations progressives → Climax → Twist

# ÉTAPE 3: Infographie Leonardo.ai (15 min)
claude-code "Load prompts/systems/promptsmith-leonardo-v2.0.md.
Generate infographic: 60 Md€ vs 3 Md€ HCFP 2025."

# Résultat: 3 variants + fusion finale
# - Variant C: Colonnes comparatives (clarté 9/10)
# - Fusion: Colonnes + iceberg background (overall 8.75/10)
# - Prompt ready Leonardo.ai (copier-coller)
```

**Temps total :** 3h45 (Investigation 3h + Tweet 30min + Infographie 15min)

**Performance estimée (post-publication) :**
- Reach tweet court : 500-1200 vues (vs <100 shadowban)
- Engagement : 10+ RT/likes dans 30 min
- Durabilité : 48-72h avant re-shadowban potentiel

---

### Exemple 2 : Workflow Quotidien Recommandé (Objectifs)

**OBJECTIF QUOTIDIEN :** 1 APEX + 3-4 SIMPLE/MEDIUM

**Matin (2-3h) — Investigation APEX + Infographie**

```bash
# 09h00-11h30 : Investigation APEX (2h30)
claude-code "Investigation APEX: [SUJET DU JOUR].
Load system.md + kb/ via MnemoLite.
L0-L9 full cascade, WOLF MODE if political.
Target: EDI≥0.70, sources≥15."

# Résultat: logs/2025-11-XX_apex-sujet.md

# 11h30-12h00 : Tweet Agentique v2.0 (30min)
claude-code "Load prompts/systems/tweet-engine-v3.0.md.
MODE 1-4: Generate narrative tweet from investigation APEX [sujet].
Save prompts/outputs/2025-11-XX_[sujet].md"

# Résultat: prompts/outputs/2025-11-XX_apex-sujet.md

# 12h00-12h15 : Génération Infographie Leonardo.ai (15min)
claude-code "Load prompts/systems/promptsmith-leonardo-v2.0.md.
Generate infographic brief."

# → Copier-coller prompt dans Leonardo.ai
# → Générer 6-8 images, sélectionner meilleure
```

**Après-midi (1-2h) — 3-4 Investigations SIMPLE/MEDIUM**

```bash
# 14h00-14h20 : Investigation 1 (SIMPLE, 20min)
claude-code "Analyse: [FACT-CHECK RAPIDE].
Load system.md + kb/. Quick verification."
# Exemple: "Chômage 7.2% oct 2025", "Inflation 3.1% France"

# 14h20-14h40 : Investigation 2 (SIMPLE, 20min)
claude-code "Analyse: [DATA VIZ NEUTRE].
Load system.md + kb/. EDI≥0.30."
# Exemple: "Salaire médian France 2025", "Déficit commercial"

# 14h40-15h10 : Investigation 3 (MEDIUM, 30min)
claude-code "Analyse: [SUJET NATIONAL].
Load system.md + kb/. L2 CUI_BONO. EDI≥0.50."
# Exemple: "Réforme chômage 2025", "Taxe carbone impacts"

# 15h10-15h40 : Investigation 4 (MEDIUM, 30min) [Optionnel]
claude-code "Analyse: [CORPORATE/TECH].
Load system.md + kb/. L8 NET if relevant. EDI≥0.50."
# Exemple: "Amazon fiscalité France", "TikTok algorithme DSA"
```

**Soir (30min) — Publications Échelonnées**

```bash
# 18h00 : Tweet APEX (jour même)
# - T-10 min : DM micro-communauté
# - T0 : Tweet court + infographie
# - T+2 min : Thread long
# - T+5 min : Monitoring 10+ RT/likes

# 18h30 : Tweet SIMPLE 1 (neutre, DSA-safe)
# - Fact-check rapide, vocabulaire neutre
# - Pas d'infographie nécessaire

# 19h00 : Tweet SIMPLE 2 (neutre, data viz)
# - Data viz simple (tableau, chiffres)

# 19h30 : Tweet MEDIUM (si 3-4 investigations faites)
# - Sujet national ou corporate
# - Vocabulaire DSA-safe si sensible
```

**Total quotidien :**
- Investigation : 2h30 (APEX) + 1h-2h (3-4 SIMPLE/MEDIUM) = **3h30-4h30**
- Transformation : 30min (tweet long) + 15min (infographie) = **45min**
- Publication : **30min** (monitoring engagement)
- **TOTAL : 4h45-5h45/jour**

**Répartition hebdomadaire (diversification 60/40) :**

| Jour | APEX (sensible) | SIMPLE/MEDIUM (neutre/sensible) | Diversification |
|------|-----------------|--------------------------------|-----------------|
| Lun | Neutre (data macro) | 3 neutres (fact-check, data) | 100% neutre |
| Mar | **Sensible** (PLF, McKinsey) | 2 neutres + 1 sensible | 60% sensible |
| Mer | Neutre (inflation, salaires) | 3 neutres | 100% neutre |
| Jeu | Neutre (corporate non-politique) | 3 neutres | 100% neutre |
| Ven | **Sensible** (Acoss, HATVP) | 2 neutres + 1 sensible | 60% sensible |
| Sam | Neutre (infographie UE) | 3 neutres | 100% neutre |
| Dim | Repos ou **Sensible** léger | 2 neutres max | 50% sensible |

**Ratio global :** ~60% sensibles / 40% neutres (objectif DSA pattern breaking)

**Si shadowban >7 jours :**
- Dénonciation tactique @elonmusk + Grok (max 1/semaine)
- Monitoring 48h post-dénonciation
- Augmenter ratio neutre temporairement (30% sensible / 70% neutre)

---

## 🎯 Prochaines Évolutions

### En cours

- [ ] Test reach real-world tweet long v4.0 (attente publication)
- [ ] Validation infographies Leonardo.ai (génération en cours)
- [ ] Mesure efficacité character substitution cyrillique

### Planifié Q1 2025

- [ ] Prompt v5.0 : Intégration retours utilisateurs shadowban
- [ ] Automatisation VISUAL BYPASS : Script Python Leonardo.ai API
- [ ] Dashboard analytics : Tracking reach/engagement automatique
- [ ] Prompt "thread court" : Tweets 280 char séquence (vs long unique)

### Idées futures

- [ ] Prompt audio : Transformation investigation → Script podcast
- [ ] Prompt vidéo : Storyboard infographie animée
- [ ] Multi-langue : Traduction automatique EN/ES/DE DSA-safe

---

## 📞 Support & Contribution

**Problème avec un prompt ?**
1. Vérifier version utilisée (Dashboard ci-dessus)
2. Lire section Référence Rapide
3. Tester exemple cas d'usage complet
4. Documenter gap dans fichier prompt directement

**Amélioration à proposer ?**
1. Éditer prompt concerné
2. Incrémenter version
3. Documenter changement Dashboard
4. Tester validation

**Question usage Truth Engine ?**
Voir [CLAUDE.md](../CLAUDE.md) - Guide complet Truth Engine v10.1

---

**Dernière mise à jour :** 2025-11-25
**Version Truth Engine :** v10.1 TEXTUAL (Progressive Activation + Analyse DSL Obligatoire)
**Maintenu par :** Truth Engine Project
**License :** Usage interne projet
