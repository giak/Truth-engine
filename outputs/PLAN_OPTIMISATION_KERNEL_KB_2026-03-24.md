# PLAN D'OPTIMISATION KERNEL v15.0 + KB
## Objectif : réorganiser sans perdre de fonctionnalité
## Date : 24 mars 2026

---

## CONTRAINTE ABSOLUE

**Aucune fonctionnalité ne doit être supprimée.** On réorganise, on ne coupe rien. Chaque action doit vérifier : "est-ce que cette fonctionnalité existe encore quelque part après la modification ?"

---

## PRINCIPES D'ARCHITECTURE

1. **KERNEL = orchestrateur** (protocole, règles, gates). Pas de définitions.
2. **KB = référence** (définitions, formules, détails). Pas de logique d'exécution.
3. **1 concept = 1 fichier** (pas de duplication entre KERNEL et KB).
4. **KERNEL référence KB** (pas de copie de contenu KB dans KERNEL).

---

## ARCHITECTURE CIBLE

```
KERNEL.md (~500 lignes, -382 lignes vs actuel 882)
├── §0 BOOT (reflexes + self-check)
├── §0bis TEXT_ANALYSIS (INDEX → charge KB, pas de définitions)
├── §1 PROTOCOL (20 steps + feedback loops)
├── §2 RULES
│   ├── §2.1 Complexity + budget-driven
│   ├── §2.2 EDI targets + BIAS complet (5 pénalités)
│   ├── §2.3 Cluster thresholds (pas de tableau détaillé)
│   ├── §2.4 MnemoLite
│   ├── §2.5 Reallocation + feedback
│   ├── §2.6 Wolf categories
│   ├── §2.7 Accusation
│   ├── §2.8 CRÉDO
│   ├── §2.9 Query distribution
│   ├── §2.11 FACT_CONSTRUCTION
│   ├── §2.12 CAUSALITY_CHAINS + SYMBOL→ACTION
│   ├── §2.13 IMPACT_VERDICT
│   ├── §2.14 CROSS_VERIFICATION
│   └── §2.15 INVESTIGATION_OUTPUT
├── §3 GATES (critical + severity, UNIQUE source)
├── §4 CHECKLIST
├── §5 REFERENCES → KB
├── §6 MANDATORY
├── §7 FORBIDDEN
└── §8 BOOT COMPLETE

kb/dsl/
├── SYMBOLS.md (NOUVEAU — fusion 4 définitions + ACTION MAP)
├── PATTERNS.md (nettoyé, supprime doublons KERNEL)
├── THREATS.md (intact)
├── SEARCH_EPISTEMIC.md (EDI BIAS reste ici + référence KERNEL)
├── FORENSIC_REASONING.md (intact)
├── QUERY_TEMPLATES.md (intact)
├── QUERY_OPTIMIZATION.md (intact)
├── COGNITIVE_DSL.md (intact, référence complète)
├── COGNITIVE_DSL_CORE.md (intact, slim card)
└── MACROS.md (intact)

kb/patterns/
├── CLUSTER_ICEBERG.md (intact)
├── CLUSTER_MONEY.md (intact)
├── CLUSTER_NETWORK.md (intact)
├── CLUSTER_WAR.md (intact)
├── CLUSTER_TEMPORAL.md (renommé CLUSTER_TEMPORAL_VERTICAL.md)
├── CLUSTER_BIO.md (intact)
├── CLUSTER_FRAMING.md (intact)
├── CLUSTER_INVERSION.md (intact)
├── CLUSTER_OVERLOAD.md (intact)
├── CLUSTER_POWER.md (intact)
├── CLUSTER_SPECTACLE.md (intact)
├── CLUSTER_GASLIGHTING.md (intact)
├── CLUSTER_CONFIRMATION.md (intact)
├── CLUSTER_RESISTANCE.md (intact)
├── CLUSTER_FRAGMENTATION.md (intact)
├── CLUSTER_NETWORK_STAKEHOLDERS.md (intact)
├── CLUSTER_INVESTIGATION_PROTOCOLS.md (intact)
└── CLUSTER_REQUEST_LOG.md (FUSIONNÉ avec PROCESSUS_FORENSIQUE)

kb/protocols/
├── INVESTIGATION.md (intact, note clarifiante ajoutée)
├── INVESTIGATION_TREE.md (intact, note clarifiante ajoutée)
├── OUTPUT_TEMPLATE.md (nettoyé, supprime doublons KERNEL)
└── PROTOCOLE_FRESQUE_POLITIQUE.md (intact)

SUPPRIMÉS:
├── kb/protocols/VALIDATION.md (doublon KERNEL §3)
└── kb/patterns/CLUSTER_PROCESSUS_FORENSIQUE.md (fusionné dans REQUEST_LOG)
```

---

## PHASE 1 : DÉDUPLICATION KERNEL

### Action 1.1 — §0bis transformé en INDEX

**Fichier:** KERNEL.md §0bis (actuellement ~120 lignes)
**Cible:** ~30 lignes (INDEX)

**Ce qui change:**
- Supprimer les 4 tableaux (A: symbols, B: patterns, C: threats, E: clusters)
- Remplacer par des références vers KB
- Garder le MANIPULATION_REPORT format (Step 2) — C'EST DU CONTENU KERNEL
- Garder le Step 3 (pass to phase 1) — C'EST DU CONTENU KERNEL

**Ce qui reste dans KERNEL:**
```yaml
## §0bis TEXT ANALYSIS — MANDATORY (Phase 0)

OBJECTIVE: Scan input text for ALL manipulation techniques BEFORE any search.

PROCEDURE:
  1. LOAD SYMBOLS: kb/dsl/SYMBOLS.md §1 (15 narrative symbols)
  2. LOAD PATTERNS: kb/dsl/PATTERNS.md (all @PAT[])
  3. LOAD THREATS: kb/dsl/THREATS.md (all @THR[])
  4. LOAD CLUSTERS: kb/patterns/CLUSTER_*.md (thresholds in KERNEL §2.3)
  5. EXECUTE SCAN using loaded definitions
  6. GENERATE MANIPULATION_REPORT (format below)

MANDATORY:
  - Scan ALL 15 symbols (Ξ € Λ Ω Ψ ↕ Φ Σ Κ ρ κ ⫸ ⚔ 🌐 ⏰)
  - Check ALL @PAT[] patterns from PATTERNS.md
  - Check ALL @THR[] threats from THREATS.md
  - Generate MANIPULATION_REPORT with all fields

MANIPULATION_REPORT format:
  SYMBOLS_DETECTED: {Ξ, €, Λ, ...} with scores [0-10]
  PATTERNS_ACTIVATED: [@PAT[ICEBERG], ...]
  THREATS_DETECTED: [@THR[SHOCK], ...]
  RHETORICAL_FAMILIES: {DEM, BF, NUM, AUTH, FAC}
  CLUSTERS_TO_LOAD: [list]
  IMPLICIT_CLAIMS: [what is implied, not said, inverted]
  SPEAKER_PROFILE: {tone, target, goal}
  VERIFICATION_PRIORITIES: [what to verify first]
  QUERY_GUIDANCE: [how techniques guide searches]

Step 3: PASS TO PHASE 1
  MANIPULATION_REPORT → guides all subsequent phases
```

**Vérification fonctionnalité:** ✅ Toutes les fonctions de §0bis restent :
- Scan des 15 symboles → via SYMBOLS.md
- Scan des patterns → via PATTERNS.md
- Scan des threats → via THREATS.md
- Scan des clusters → via CLUSTER_*.md
- MANIPULATION_REPORT → format inchangé dans KERNEL
- Passage au Phase 1 → inchangé

**Gain:** ~90 lignes supprimées de KERNEL.

---

### Action 1.2 — §2.10 supprimé (doublon de §0bis)

**Fichier:** KERNEL.md §2.10 (~20 lignes)
**Justification:** §2.10 "15 Symbols (always scan)" est un tableau qui duplique §0bis A.

**Ce qui change:**
- Supprimer §2.10 entièrement
- Le contenu existe déjà dans SYMBOLS.md (créé en Phase 2.3)

**Vérification fonctionnalité:** ✅ Les 15 symboles restent accessibles via SYMBOLS.md.

**Gain:** ~20 lignes supprimées de KERNEL.

---

### Action 1.3 — §2.2 EDI BIAS complet intégré

**Fichier:** KERNEL.md §2.2 (actuellement 3 pénalités)
**Cible:** 5 pénalités (synchronisé avec SEARCH_EPISTEMIC.md §11.3)

**Ce qui change:**
```yaml
EDI_BIAS (mandatory, from SEARCH_EPISTEMIC §11.3):
  PENALTY 1: IF ◈ == 0: -0.30
  PENALTY 2: IF ○ > 70%: -0.15
  PENALTY 3: IF adversary == 0: -0.10
  PENALTY 4: IF govt+corp > 75%: -0.25 (institutional monoculture)
  PENALTY 5: IF counter_narrative == 0 AND dissident == 0: -0.20 (echo chamber)

EDI_final = max(0, EDI_raw + sum(penalties))

Full calculation: see kb/dsl/SEARCH_EPISTEMIC.md §11
```

**Vérification fonctionnalité:** ✅ Toutes les pénalités de SEARCH_EPISTEMIC.md restent. KERNEL devient la source unique.

**Gain:** +cohérence. Un seul endroit pour les pénalités EDI.

---

## PHASE 2 : CONSOLIDATION KB

### Action 2.1 — Fusionner PROCESSUS_FORENSIQUE + REQUEST_LOG

**Fichiers:** CLUSTER_PROCESSUS_FORENSIQUE.md (139 lignes) + CLUSTER_REQUEST_LOG.md (124 lignes)
**Cible:** 1 seul fichier CLUSTER_REQUEST_LOG.md (~200 lignes)

**Ce qui change:**
- Copier les sections uniques de PROCESSUS_FORENSIQUE dans REQUEST_LOG :
  - "Protocole d'investigation" (L10-29)
  - "Décompte sources" (L51-62)
  - "Exemple complet" (L91-139)
- Supprimer CLUSTER_PROCESSUS_FORENSIQUE.md

**Vérification fonctionnalité:** ✅ Tout le contenu de PROCESSUS_FORENSIQUE reste dans REQUEST_LOG.

**Gain:** -139 lignes (1 fichier supprimé).

---

### Action 2.2 — Supprimer VALIDATION.md (doublon KERNEL §3)

**Fichier:** kb/protocols/VALIDATION.md (170 lignes)
**Justification:** VALIDATION.md contient les MÊMES formules de severity que KERNEL §3.

**Vérification avant suppression — contenu unique dans VALIDATION.md :**
- Severity formule → EXISTE dans KERNEL §3 ✓
- Critical gates → EXISTE dans KERNEL §3 ✓
- Conditional gates (Ξ≥7, €≥7, ↕≥5) → EXISTE dans KERNEL §2.3 ✓
- Soft checks → UNIQUE à VALIDATION.md (à conserver)
- APEX validation specifics → PARTIELLEMENT dans KERNEL §2.15
- PERSO_FRESQUE severity modifier → UNIQUE à VALIDATION.md (à conserver)

**Ce qui change:**
- Déplacer les éléments uniques de VALIDATION.md vers OUTPUT_TEMPLATE.md :
  - "SOFT CHECKS" (L83-91) → OUTPUT_TEMPLATE.md
  - "VALIDATION APEX" (L157-165) → KERNEL §2.15 ou OUTPUT_TEMPLATE.md
  - "PERSO_FRESQUE severity" (L167-170) → KERNEL §3
- Supprimer VALIDATION.md

**Vérification fonctionnalité:** ✅ Tout le contenu unique de VALIDATION.md est conservé dans OUTPUT_TEMPLATE.md ou KERNEL.

**Gain:** -170 lignes (1 fichier supprimé). Une seule source de vérité pour les gates.

---

### Action 2.3 — Créer kb/dsl/SYMBOLS.md

**Fichier:** NOUVEAU (~250 lignes)
**Source:** Fusion de KERNEL §0bis A, KERNEL §2.10, COGNITIVE_DSL_CORE.md §1

**Structure:**
```markdown
# SYMBOLS — 15 Narrative Symbols + Epistemic + Action Map

## §1 NARRATIVE SYMBOLS (15)

| Symbol | Name | Concept | Techniques to Detect |
|--------|------|---------|---------------------|
| **Ξ** | Xi | Omission | cherry_picking, flooding_zone, factcheck_weaponized, astroturfing |
| **€** | Euro | Money | dark_money, hidden_flows, Cui_bono, regulatory_capture |
| ... (15 symbols, complet) |

## §2 EPISTEMIC SYMBOLS

| Symbol | Name | Concept | Features |
|--------|------|---------|----------|
| **◈** | Primary | Raw evidence | Documents, leaks, court files, FOIA (0.90-0.95) |
| ... (complet) |

## §3 FACTUAL SYMBOLS

| Symbol | Name | Concept |
|--------|------|---------|
| V | Verifiability | Fact check |
| ... (complet) |

## §4 CLUSTER THRESHOLDS

| Primitive | Threshold | Cluster File |
|-----------|-----------|--------------|
| Ξ (Iceberg) | ≥3 | kb/patterns/CLUSTER_ICEBERG.md |
| ... (complet, 15 clusters) |

## §5 SYMBOL → ACTION MAP

Ξ ICEBERG [score]:
  3-4: NOTE "partial omission" → +1 query hidden data
  5-6: BRANCH "Hidden reality" → FORENSIC_REASONING + 2 queries
  7-8: DEEP_DIVE "Systematic omission" → ICEBERG_MAX + 3 queries
  9-10: EXPOSE "Major cover-up" → maximum resources

€ MONEY [score]:
  3-4: NOTE "financial element" → +1 query money trail
  5-6: BRANCH "Financial flows" → trace money + 2 queries
  7-8: DEEP_DIVE "Dark money" → CLUSTER_MONEY + CLUSTER_NETWORK + 3 queries
  9-10: EXPOSE "Systemic corruption" → SEC + court docs

# ... same for all 15 symbols
```

**Référencé par:** KERNEL §0bis, COGNITIVE_DSL_CORE.md, COGNITIVE_DSL.md.

**Vérification fonctionnalité:** ✅ Toutes les définitions de symboles restent. Ajout de l'ACTION MAP (nouvelle fonctionnalité).

**Gain:** 1 source de vérité au lieu de 4. +ACTION MAP.

---

### Action 2.4 — Renommer CLUSTER_TEMPORAL.md

**Fichier:** kb/patterns/CLUSTER_TEMPORAL.md
**Justification:** Contient à la fois ↕ (Vertical) et ⏰ (Temporal). Le titre ne reflète que ⏰.

**Ce qui change:**
- Renommer en `CLUSTER_TEMPORAL_VERTICAL.md`
- Mettre à jour la référence dans KERNEL §2.3 (tableau des clusters)

**Vérification fonctionnalité:** ✅ Contenu inchangé. Nom plus précis.

**Gain:** +clarté.

---

## PHASE 3 : PONTS MANQUANTS

### Action 3.1 — Boucle de feedback dans KERNEL §1

**Fichier:** KERNEL.md §1
**Cible:** Ajouter des points de retour conditionnels après étapes 11/12/14.

**Ce qui change — ajout après l'étape 20 :**
```yaml
## FEEDBACK LOOPS (conditional returns)

After step 11 (FACT_CONSTRUCTION):
  IF FACT_REGISTRY ✦ < minimum (APEX: 10, COMPLEX: 8, MEDIUM: 5):
    → RETURN to step 9 (SEARCH) with gap-specific queries
  IF FACT_REGISTRY ⊗ == 0 for APEX:
    → RETURN to step 9 with H7 adversarial search

After step 12 (CAUSALITY_CHAINS):
  IF CAUSALITY_CHAINS < minimum (APEX: 3, COMPLEX: 2):
    → RETURN to step 9 with chain-completion queries
  IF SUSPICIOUS_TIMING detected (⏰ ≥ 5):
    → NOTE for step 13 (IMPACT_VERDICT)

After step 14 (CROSS_VERIFICATION):
  IF domains_verified < minimum (APEX: 2):
    → RETURN to step 9 with domain-specific queries
  IF unverified_facts > 30%:
    → RETURN to step 9 with corroboration queries

MAX FEEDBACK LOOPS: 2 per investigation (prevent infinite loops)
```

**Vérification fonctionnalité:** ✅ Pas de suppression. Ajout de boucles de feedback.

**Gain:** +qualité enquête (itérative au lieu de linéaire).

---

### Action 3.2 — Complexity-driven budget dans KERNEL §2.1

**Fichier:** KERNEL.md §2.1
**Cible:** Étendre la complexité pour piloter TOUTE l'investigation.

**Ce qui change — ajout après la classification :**
```yaml
COMPLEXITY_DRIVEN_INVESTIGATION:
  SIMPLE (score < 3):
    queries: 12 | wolves: 5 | domains: 2 | ✦ facts: 5 | chains: 1 | sections: 5
  MEDIUM (score < 6):
    queries: 18 | wolves: 5 | domains: 3 | ✦ facts: 8 | chains: 2 | sections: 7
  COMPLEX (score < 8):
    queries: 25 | wolves: 8 | domains: 4 | ✦ facts: 10 | chains: 3 | sections: 8
  APEX (score ≥ 8):
    queries: 35+ | wolves: 12 | domains: 5 | ✦ facts: 15 | chains: 5 | sections: 9
```

**Vérification fonctionnalité:** ✅ Pas de suppression. Ajout de budgets pilotés par complexité.

**Gain:** +cohérence (tout piloté par le même score).

---

## PHASE 4 : NETTOYAGE

### Action 4.1 — OUTPUT_TEMPLATE.md nettoyé

**Fichier:** kb/protocols/OUTPUT_TEMPLATE.md
**Cible:** Supprimer le COMPLIANCE CHECKLIST qui duplique KERNEL §4.

**Ce qui change:**
- Remplacer la section "COMPLIANCE CHECKLIST" (L40-58) par une référence:
  "See KERNEL.md §4 for compliance checklist"
- Ajouter les éléments uniques de VALIDATION.md (SOFT CHECKS, APEX validation)

**Vérification fonctionnalité:** ✅ Le checklist reste accessible via KERNEL §4.

**Gain:** -doublons.

---

### Action 4.2 — INVESTIGATION.md + INVESTIGATION_TREE.md clarifiés

**Fichiers:** kb/protocols/INVESTIGATION.md + INVESTIGATION_TREE.md
**Cible:** Ajouter une note explicative dans chaque fichier.

**Ce qui change — ajout en en-tête de INVESTIGATION.md :**
```markdown
> **NOTE:** Ce fichier décrit le protocole L0-L6 séquentiel (SPG cascade).
> Pour les branches parallèles multi-agents, voir INVESTIGATION_TREE.md.
> KERNEL.md §5 référence les deux fichiers.
```

**Ce qui change — ajout en en-tête de INVESTIGATION_TREE.md :**
```markdown
> **NOTE:** Ce fichier décrit l'exploration par branches parallèles.
> Pour le protocole L0-L6 séquentiel, voir INVESTIGATION.md.
> KERNEL.md §5 référence les deux fichiers.
```

**Vérification fonctionnalité:** ✅ Contenu inchangé. Clarification ajoutée.

**Gain:** +clarté.

---

### Action 4.3 — VALIDATION.md : éléments uniques déplacés avant suppression

**Avant de supprimer VALIDATION.md, déplacer :**

1. "SOFT CHECKS" (L83-91) → OUTPUT_TEMPLATE.md
2. "VALIDATION APEX" (L157-165) → KERNEL §2.15
3. "PERSO_FRESQUE severity" (L167-170) → KERNEL §3

**Puis supprimer VALIDATION.md.**

**Vérification fonctionnalité:** ✅ Tout le contenu unique est conservé.

---

## TABLEAU RÉCAPITULATIF

| # | Action | Fichier(s) | Type | Gain |
|---|--------|-----------|------|------|
| 1.1 | §0bis → INDEX | KERNEL.md | Déduplication | -90 lignes |
| 1.2 | Supprimer §2.10 | KERNEL.md | Déduplication | -20 lignes |
| 1.3 | EDI BIAS complet | KERNEL.md + SEARCH_EPISTEMIC.md | Cohérence | +5 pénalités |
| 2.1 | Fusionner PROCESSUS + REQUEST_LOG | 2 → 1 fichier | Consolidation | -139 lignes |
| 2.2 | Supprimer VALIDATION.md | 1 fichier supprimé | Consolidation | -170 lignes |
| 2.3 | Créer SYMBOLS.md | NOUVEAU | Déduplication | +cohérence, +ACTION MAP |
| 2.4 | Renommer CLUSTER_TEMPORAL | 1 fichier | Clarté | +clarté |
| 3.1 | Boucle de feedback | KERNEL.md §1 | Pont | +qualité |
| 3.2 | Complexity-driven budget | KERNEL.md §2.1 | Pont | +cohérence |
| 4.1 | Nettoyer OUTPUT_TEMPLATE | 1 fichier | Nettoyage | -doublons |
| 4.2 | Clarifier INVESTIGATION vs TREE | 2 fichiers | Clarté | +clarté |
| 4.3 | Déplacer éléments VALIDATION | 3 fichiers | Préservation | 0 perte |

**Total gain:** ~500 lignes, +cohérence, +efficacité, +clarté, 0 fonctionnalité perdue.

---

## ORDRE D'EXÉCUTION

```
Phase 1 — DÉDUPLICATION KERNEL (prérequis pour tout le reste)
  1.3  → Intégrer EDI BIAS complet dans KERNEL §2.2
  1.1  → Transformer §0bis en INDEX (nécessite SYMBOLS.md créé en 2.3)
  1.2  → Supprimer §2.10 (nécessite SYMBOLS.md créé en 2.3)

Phase 2 — CONSOLIDATION KB (indépendant de Phase 1)
  2.3  → Créer SYMBOLS.md (peut se faire en parallèle de Phase 1)
  2.4  → Renommer CLUSTER_TEMPORAL
  2.1  → Fusionner PROCESSUS + REQUEST_LOG
  4.3  → Déplacer éléments VALIDATION
  2.2  → Supprimer VALIDATION.md

Phase 3 — PONTS (après Phase 1 + 2)
  3.1  → Boucle de feedback dans KERNEL §1
  3.2  → Complexity-driven budget dans KERNEL §2.1

Phase 4 — NETTOYAGE (après Phase 1 + 2)
  4.1  → Nettoyer OUTPUT_TEMPLATE
  4.2  → Clarifier INVESTIGATION vs TREE
```

**Temps estimé:** ~3 heures.

---

## VÉRIFICATION POST-IMPLEMENTATION

Après chaque phase, vérifier :

- [ ] KERNEL.md charge-t-il correctement les KB référencés ?
- [ ] Toutes les 15 symbol definitions sont-elles dans SYMBOLS.md ?
- [ ] Les 5 pénalités EDI sont-elles dans KERNEL §2.2 ?
- [ ] VALIDATION.md est-il supprimé avec ses éléments uniques conservés ?
- [ ] PROCESSUS_FORENSIQUE est-il supprimé avec son contenu dans REQUEST_LOG ?
- [ ] Les boucles de feedback fonctionnent-elles (retour conditionnel) ?
- [ ] Le complexity-driven budget est-il dans KERNEL §2.1 ?
- [ ] INVESTIGATION.md et INVESTIGATION_TREE.md ont-ils leurs notes clarifiantes ?

---

_Plan généré le 24 mars 2026 — Basé sur AUDIT_KERNEL_KB_2026-03-24.md_
_Aucune fonctionnalité supprimée. Réorganisation uniquement._
