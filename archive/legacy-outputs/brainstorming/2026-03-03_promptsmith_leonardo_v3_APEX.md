# Promptsmith Leonardo v3.0 — Brainstorming APEX Architecture

**Date:** 2026-03-03
**Status:** APEX Research Complete
**Objective:** Concevoir un agent générateur de prompts Leonardo.ai au niveau APEX pour Truth Engine
**Focus Modèles:** Lucid Origin, Flux 2 Pro

---

## Executive Summary

L'agent Promptsmith Leonardo v2.0 (nov 2025) est obsolète face aux évolutions 2025-2026. Les modèles prioritaires de l'utilisateur (Lucid Origin, Flux 2 Pro) ne sont pas optimalement couverts. Cette recherche propose une architecture v3.0 APEX intégrant:

- **Compréhension sémantique** des articles d'investigation Truth Engine
- **Système de cohérence visuelle** pour séries d'images
- **Optimisation modèle-spécifique** (Lucid Origin vs Flux 2 Pro)
- **Workflow éditorial** adapté au journalisme d'investigation

---

## Partie 1: Analyse des Modèles Leonardo.ai 2025-2026

### 1.1 Lucid Origin — Le Modèle Principal

**Caractéristiques clés (2025-2026):**
- **Full HD native** : Résolution supérieure aux modèles précédents
- **Rich colors & diversity** : Plus grande fidélité chromatique
- **Sharp text rendering** : Texte lisible intégré (meilleur qu'Ideogram 3.0)
- **Prompt adherence extrême** : Suit les instructions avec précision
- **Adaptabilité** : Fonctionne sur concept art, produits, illustrations éditoriales

**Cas d'usage Truth Engine:**
- ✅ Illustrations éditoriales complexes
- ✅ Images avec texte intégré (titres, citations)
- ✅ Séries d'images nécessitant cohérence chromatique
- ✅ Rendus haute définition pour publication

**Paramètres optimaux (recherche 2026):**
```
Model: Lucid Origin
Prompt Magic: 0.65-0.75 (léger boost, pas d'overcooking)
Guidance: 7-9 (8 = sweet spot)
Generation Mode: Quality (Ultra si disponible)
RAW Mode: ON pour prompts >80 mots
Aspect Ratio: 16:9 (desktop) | 4:5 (mobile/social)
Negative Prompt: OBLIGATOIRE (toggle Advanced)
Number of Images: 6-8 (balance coût/variété)
```

**Structure de prompt optimale:**
```
[Subject précis] + [Style artistique] + [Composition/cadrage] +
[Lighting/ambiance] + [Palette couleurs HEX] + [Détails additionnels]
```

---

### 1.2 Flux 2 Pro — Le Modèle Premium

**Caractéristiques clés (2025-2026):**
- **12B paramètres** : Le plus grand modèle open-source
- **Prompt adherence supérieure** : Meilleur que Midjourney v6.1, DALL-E 4
- **Typography excellence** : Texte dans images exceptionnel
- **Photorealism avancé** : Qualité photographique professionnelle
- **JSON prompting support** : Prompts structurés possibles

**Cas d'usage Truth Engine:**
- ✅ Couvertures d'articles premium
- ✅ Photographies conceptuelles
- ✅ Images avec texte complexe
- ✅ Rendus nécessitant réalisme absolu

**Paramètres optimaux:**
```
Model: Flux 2 Pro
Guidance: 3-5 (plus bas = plus créatif, plus haut = plus strict)
Steps: 28-50 (plus = meilleure qualité, plus lent)
Aspect Ratio: Flexible (jusqu'à 2:3, 3:2)
Negative Prompt: Supporté mais moins critique
```

**Techniques de prompting avancées (Flux 2):**
```
# JSON Structure (pour scènes complexes)
{
  "subject": "...",
  "style": "...",
  "lighting": "...",
  "colors": ["#HEX1", "#HEX2"],
  "composition": "..."
}

# HEX Color Control
"subject in #1a1a2e background with #e94560 accents"

# Camera-style Guidance
"shot on 85mm lens, f/1.8, shallow depth of field"
```

---

### 1.3 Tableau Comparatif Modèles

| Critère | Lucid Origin | Flux 2 Pro | Phoenix 1.0 | Ideogram 3.0 |
|---------|--------------|------------|-------------|--------------|
| **Prompt Adherence** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Text in Image** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Photorealism** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Speed** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Coût** | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Couleurs** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Cohérence série** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Best for Truth Engine** | Généraliste | Premium | Complexe | Texte simple |

**Recommandation Truth Engine:**
- **Usage standard:** Lucid Origin (équilibre qualité/coût)
- **Images clés:** Flux 2 Pro (couvertures, visuels impact)
- **Series cohérentes:** Flux 2 Pro + Character Reference

---

## Partie 2: Fonctionnalités Leonardo.ai 2025-2026

### 2.1 Character Reference (CRF)

**Fonctionnement:**
- Upload image référence personnage
- Force: Low (20%) | Mid (50%) | High (80%)
- Fonctionne avec tous les modèles

**Applications Truth Engine:**
- Personnages récurrents (parodies, mascottes)
- Cohérence visuelle across articles
- Séries narrative (visuels en progression)

**Workflow recommandé:**
```
1. Générer image personnage (seed fixé)
2. Sauvegarder comme référence
3. Générer variations avec Character Reference
4. Ajuster force selon besoin (High = identique, Low = inspiration)
```

### 2.2 Style Reference

**Fonctionnement:**
- Upload image style de référence
- Transfer style à nouveau contenu
- Maintien composition originale possible

**Applications Truth Engine:**
- Identité visuelle cohérente
- Style éditorial reconnaissable
- Adaptation existant → nouveau sujet

### 2.3 Image Guidance (ControlNet amélioré)

**Modes disponibles:**
- **Pose:** Maintien posture personnage
- **Depth:** Contrôle profondeur de champ
- **Edge:** Détection contours
- **QR:** Code intégré (peu utile éditorial)

**Applications Truth Engine:**
- Cadrage cohérent série d'images
- Composition éditoriale structurée

### 2.4 Elements (Nouveauté 2025-2026)

**Concept:** Modificateurs de style prédéfinis
- Texture additions
- Style transfers prédéfinis
- Ambiance filters

**Usage:** Peu pertinent pour éditorial sérieux

### 2.5 Omni Editing (2026)

**Fonctionnalités:**
- FLUX.1 Kontext intégré
- GPT-Image-1 support
- Édition inpainting/outpainting avancée
- Conservation personnage/style lors édition

**Applications Truth Engine:**
- Ajustements post-génération
- Corrections sans recréation totale
- Variations conservant éléments clés

### 2.6 Fixed Seed Method

**Fonctionnement:**
- Fixer seed = reproduire résultat
- Variations mineures avec même seed + prompt modifié
- Essentiel pour cohérence série

**Workflow cohérence:**
```
Seed: 123456789 (mémorisé)
→ Image 1: "personnage dans contexte A"
→ Image 2: "personnage dans contexte B" (même seed)
→ Résultat: Même base, contexte différent
```

---

## Partie 3: Techniques Avancées pour Illustration Éditoriale

### 3.1 Cohérence Stylistique Inter-Images

**Méthode Truth Engine (Multi-Image Coherence):**
```
1. DÉFINIR STYLE ANCRE (Image 0)
   - Générer avec description style exhaustive
   - Capturer: palette, lighting, mood, grain
   - Sauvegarder comme référence style

2. EXTRAIRE ATTRIBUTS STYLISTIQUES
   Prompt modèle: "[Sujet article], rendered in
   [STYLE ANCRE descriptif détaillé],
   maintaining [PALETTE HEX précise],
   [LIGHTING spécifique], [MOOD cohérent]"

3. GÉNÉRER SÉRIE AVEC CONTRAINTES
   - Même seed de base ± 100
   - Style Reference activé
   - Prompts incluant descripteur style ancre
```

**Template style ancre Truth Engine:**
```
STYLE_TRUTH_ENGINE = """
editorial illustration style,
cinematic composition, dramatic chiaroscuro lighting,
palette: deep blacks (#0a0a0f), warning amber (#ff6b35),
authority blue (#2563eb), occasional blood red (#dc2626),
grainy film texture, high contrast,
professional photojournalism aesthetic,
slightly desaturated, documentary feel,
sharp focus on subject, atmospheric depth
"""
```

### 3.2 Prompt Engineering pour Investigation

**Structure hiérarchique (ordre importance):**
```
1. SUBJECT (le plus important)
   "A corrupt politician shaking hands with a shadowy figure"

2. COMPOSITION/CADRAGE
   "medium shot, rule of thirds, subject left-aligned"

3. STYLE VISUEL
   "editorial photorealism, investigative journalism aesthetic"

4. LIGHTING/AMBIANCE
   "dramatic side lighting, dark moody atmosphere"

5. PALETTE COULEURS
   "dominant deep blues (#1e3a5f) with danger red (#c53030) highlights"

6. DÉTAILS TECHNIQUES
   "shot on Canon EOS R5, 85mm f/1.4, shallow depth of field"

7. ÉMOTION/SUBTEXT
   "sense of corruption, hidden power, tension"
```

### 3.3 Negative Prompts Éditoriaux

**Template universel Truth Engine:**
```
Quality: blurry, low resolution, pixelated, jpeg artifacts,
         oversaturated, cartoonish, 3D render, CGI
Anatomy: distorted hands, extra fingers, deformed limbs,
         asymmetrical faces, wrong proportions
Content: text errors, misspellings, watermarks, logos,
         signatures, frames, borders
Style: amateur photography, snapshot aesthetic,
       oversaturated Instagram filter, HDR excessive
Safety: [selon contexte] gore, nudity, violence graphic
```

### 3.4 Texte dans Images

**Format Lucid Origin (meilleur support texte):**
```
# Format obligatoire
"the text 'EXACT TEXT' in [font style] [placement]"

# Exemples
"the text 'CORRUPTION' in bold sans-serif font centered"
"the text 'TRUTH ENGINE' in modernist typeface top-left corner"

# Limites
- ≤25 caractères pour Lucid Origin
- ≤40 caractères pour Flux 2 Pro
- Éviter accents (comportement aléatoire)
- Contraste background essentiel
```

**Format Flux 2 Pro (supérieur texte complexe):**
```
# JSON structure possible
"Generate: text saying 'INVESTIGATION' in elegant serif font,
 centered, high contrast against dark background,
 professional typography, crisp edges"
```

---

## Partie 4: Architecture Agent v3.0 APEX

### 4.1 Vision Systémique

L'agent v3.0 dépasse le générateur de prompts pour devenir un **concepteur visuel éditorial** comprenant:

1. **Compréhension sémantique** de l'article d'investigation
2. **Analyse narrative** (points clés, progression, climax)
3. **Conception visuelle** (série cohérente, rythme visuel)
4. **Optimisation technique** (modèle approprié, paramètres)
5. **Documentation** (références pour reproduction)

### 4.2 Composants Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                  PROMPTSMITH LEONARDO v3.0                  │
│                         APEX LEVEL                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────┐    ┌─────────────────┐                 │
│  │ INPUT PARSER    │───▶│ NARRATIVE       │                 │
│  │ - Article TE    │    │ ANALYZER        │                 │
│  │ - Brief éditorial   │ - Extraction    │                 │
│  │ - References    │    │   key moments   │                 │
│  │ - Style guide   │    │ - Mapping       │                 │
│  └─────────────────┘    │   visual needs  │                 │
│                         └─────────────────┘                 │
│                                  │                          │
│                                  ▼                          │
│  ┌─────────────────────────────────────────────────────┐    │
│  │           VISUAL CONCEPT DESIGNER                   │    │
│  │  - Création concept visuel global                   │    │
│  │  - Définition palette Truth Engine                  │    │
│  │  - Planification série d'images                     │    │
│  │  - Attribution modèle par image                     │    │
│  └─────────────────────────────────────────────────────┘    │
│                                  │                          │
│                                  ▼                          │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         PROMPT ENGINE (multi-engine)                │    │
│  │                                                     │    │
│  │  ┌──────────────┐  ┌──────────────┐  ┌───────────┐  │    │
│  │  │ Lucid Origin │  │ Flux 2 Pro   │  │ Phoenix   │  │    │
│  │  │ Generator    │  │ Generator    │  │ Fallback  │  │    │
│  │  └──────────────┘  └──────────────┘  └───────────┘  │    │
│  │                                                     │    │
│  │  Spécialisés par cas d'usage:                       │    │
│  │  - Texte → Lucid/Flux                               │    │
│  │  - Réalisme → Flux 2 Pro                            │    │
│  │  - Complexité → Lucid Origin                        │    │
│  └─────────────────────────────────────────────────────┘    │
│                                  │                          │
│                                  ▼                          │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         CONSISTENCY MANAGER                         │    │
│  │  - Style Reference tracking                         │    │
│  │  - Seed management                                  │    │
│  │  - Character Reference registry                     │    │
│  │  - Palette enforcement                              │    │
│  └─────────────────────────────────────────────────────┘    │
│                                  │                          │
│                                  ▼                          │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         OUTPUT FORMATTER                            │    │
│  │  - Prompts production-ready                         │    │
│  │  - Settings optimisés                               │    │
│  │  - Documentation technique                          │    │
│  │  - Variations A/B/C + Fusion                        │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 4.3 Workflow Input → Output

**Input Types acceptés:**
```
Type A: Article Truth Engine complet
  → Parsing automatique + génération série complète

Type B: Brief spécifique
  → "Besoin visuel pour section X de l'article"

Type C: Style reference update
  → "Adapter série existante au nouvel article"

Type D: Single image request
  → Image isolée avec contraintes spécifiques
```

**Processus interne:**
```
1. INTAKE
   └─▶ Identifier type input
   └─▶ Extraire métadonnées (tonalité, sujet, longueur)

2. NARRATIVE MAPPING
   └─▶ Identifier moments visuels clés
   └─▶ Déterminer nombre images nécessaires
   └─▶ Planifier progression visuelle

3. STYLE DEFINITION
   └─▶ Définir palette Truth Engine
   └─▶ Choisir aesthetic (réalisme, illustration, mix)
   └─▶ Créer Style Reference anchor

4. MODEL SELECTION
   Pour chaque image:
   └─▶ Besoin texte? → Lucid ou Flux
   └─▶ Besoin réalisme absolu? → Flux 2 Pro
   └─▶ Usage général? → Lucid Origin
   └─▶ Fallback? → Phoenix 1.0

5. PROMPT GENERATION
   └─▶ Générer variantes A/B/C
   └─▶ Inclure cohérence settings
   └─▶ Préparer documentation seeds/refs

6. OUTPUT ASSEMBLY
   └─▶ Formater pour Leonardo.ai
   └─▶ Inclure guide d'utilisation
   └─▶ Fournir référence réutilisation
```

### 4.4 Palette Truth Engine Standardisée

**Identity Colors (à utiliser cohéremment):**
```
PRIMARY:
- Authority Blue: #2563eb (confiance, vérité)
- Warning Amber: #ff6b35 (alerte, révélation)

SECONDARY:
- Deep Black: #0a0a0f (sérieux, profondeur)
- Investigation Red: #dc2626 (danger, corruption)
- Document White: #f5f5f5 (neutralité, fait)

ACCENT:
- Gold Truth: #f59e0b (révélation, triomphe)
- Shadow Purple: #7c3aed (mystère, enquête)
```

**Application:**
- Toutes les séries doivent dériver de cette palette
- Variations de luminosité/saturation permises
- Jamais de couleurs hors-palette sans justification

---

## Partie 5: Structure du System Prompt v3.0

### 5.1 Sections Clés

```markdown
# Promptsmith Leonardo v3.0 — System Prompt

## IDENTITY
Tu es Promptsmith v3.0, concepteur visuel éditorial spécialisé
dans l'illustration d'investigations journalistiques via Leonardo.ai.
Mission: Transformer articles Truth Engine en séries visuelles
cohérentes et impactantes.

## CONTEXT TRUTH ENGINE
[Identity visuelle TE, palette, tonalité, exigences éditoriales]

## MODEL KNOWLEDGE 2026
[Détails Lucid Origin, Flux 2 Pro, sélection intelligente]

## WORKFLOWS
[Type A/B/C/D avec processus spécifiques]

## CONSISTENCY PROTOCOLS
[Style Reference, Seed Management, Character Reference]

## OUTPUT FORMAT
[Structure standardisée production-ready]
```

### 5.2 Nouvelles Capacités vs v2.0

| Capacité | v2.0 | v3.0 APEX |
|----------|------|-----------|
| Compréhension article | ❌ | ✅ Parsing sémantique |
| Séries cohérentes | ❌ | ✅ Style anchor + seeds |
| Model selection | Manuel | ✅ Auto-sélection |
| Palette TE | ❌ | ✅ Enforced |
| Character Reference | Mentionné | ✅ Full workflow |
| Style Reference | ❌ | ✅ Intégré |
| Flux 2 Pro | ❌ | ✅ Natif |
| JSON prompting | ❌ | ✅ Support Flux |
| Output documentation | Basique | ✅ Production-ready |
| Variations multiples | 3+A/B/C | ✅ Matrice complète |

---

## Partie 6: Recommandations Intégration Truth Engine

### 6.1 Points d'Intégration

**Workflow existant TE:**
```
Article Investigation
        ↓
[TRADUCTION / SUBLIMATION]
        ↓
[ANALYSE NARRATIVE] ← NEW: Input pour Promptsmith
        ↓
[GÉNÉRATION VISUELLE] ← Promptsmith Leonardo v3.0
        ↓
[REVIEW ÉDITORIALE]
        ↓
PUBLICATION
```

**Interface souhaitée:**
```
# Via Claude Code
claude -s promptsmith-leonardo-v3.md \
  -f article_sublimated.md \
  -p "Generate visual series: 1 hero + 3 supporting images"

# Output: prompts_leonardo_v3_output.md
```

### 6.2 Format Output Standardisé

```markdown
# Visual Series: [Titre Article]

## Style Anchor
[Description complète style TE appliqué]
[Palette HEX exacte]
[Reference image seed]

---

## Image 1: [Rôle - ex: Hero/Cover]
**Model:** Lucid Origin | Flux 2 Pro
**Rationale:** [Pourquoi ce modèle]

### Variant A (Safe)
**Positive:** [...]
**Negative:** [...]
**Settings:** [...]

### Variant B (Bold)
**Positive:** [...]
**Negative:** [...]
**Settings:** [...]

### Variant C (Experimental)
**Positive:** [...]
**Negative:** [...]
**Settings:** [...]

### Comparison Matrix
| Var | Impact | Clarity | TE Alignment | Risk |
|-----|--------|---------|--------------|------|
| A   | 7/10   | 9/10    | 8/10         | Low  |
| B   | 9/10   | 7/10    | 9/10         | Med  |
| C   | 10/10  | 6/10    | 7/10         | High |

### Recommended (Fusion)
**Final Prompt:** [...]
**Seed:** [number]
**Notes:** [...]

---

## Image 2: [Rôle - ex: Detail/Context]
[...]

## Consistency Notes
- Seed base: [number]
- Style reference: [Image X]
- Character references: [si applicable]
```

### 6.3 Bibliothèque de Références

**Système de réutilisation:**
```
references/
├── characters/
│   ├── truth_engine_mascot.png + .seed
│   └── [personnages récurrents]
├── styles/
│   ├── editorial_dramatic.json (prompt template)
│   ├── documentary_grain.json
│   └── [styles TE reutilisables]
└── palettes/
    ├── truth_engine_standard.hex
    └── [variations thématiques]
```

---

## Partie 7: Checklist Qualité APEX

### 7.1 Validation Prompts

**Avant livraison, vérifier:**
- [ ] Prompt respecte structure hiérarchique (Subject → Style → Compo → Light → Details)
- [ ] Longueur optimale (Lucid: 200-400 char, Flux: 100-300 tokens)
- [ ] Negative prompt complet et pertinent
- [ ] Palette TE respectée ou justifiée
- [ ] Modèle choisi approprié au cas d'usage
- [ ] Settings optimaux pour modèle sélectionné
- [ ] Cohérence inter-images vérifiée (si série)
- [ ] Seeds documentés pour reproduction
- [ ] Texte in-image (si présent) ≤ limites modèle
- [ ] Pas de trademarks/IP non autorisés

### 7.2 Tests de Robustesse

**Scénarios à anticiper:**
- Article sans événement visuel évident → Abstraction conceptuelle
- Série de 5+ images → Cohérence décroissante? → Style anchor renforcé
- Besoin texte complexe → Flux 2 Pro obligatoire
- Contraintes légales strictes → Éviter photoréalisme personnes

---

## Partie 8: Feuille de Route Implémentation

### Phase 1: Fondation (Semaine 1)
- [ ] Créer fichier system prompt v3.0
- [ ] Documenter palettes TE
- [ ] Créer templates style anchors

### Phase 2: Workflows (Semaine 2)
- [ ] Implémenter parser articles TE
- [ ] Développer sélecteur modèle intelligent
- [ ] Créer consistency manager

### Phase 3: Production (Semaine 3)
- [ ] Tests avec articles existants
- [ ] Affiner output format
- [ ] Créer bibliothèque références

### Phase 4: Documentation (Semaine 4)
- [ ] Guide utilisateur complet
- [ ] Exemples cas réels
- [ ] Troubleshooting guide

---

## Annexes

### A. Sources Recherche Web

**Leonardo.ai Official:**
- Leonardo.ai Help Center — Lucid Origin
- Leonardo.ai News — Character Reference
- Leonardo.ai Learn — Style Reference
- Leonardo.ai News — Omni Editing (2026)

**Guides & Tutorials:**
- Toolkit by AI — Lucid Origin Hacks 2026
- AI Tools Dev Pro — Leonardo.ai Guide 2026
- Flux Pro AI — Flux 2 Prompt Guide
- fal.ai — Flux.2 Prompt Guide
- Ambience AI — Flux Prompt Guide 2026

**Recherche Académique:**
- Taylor & Francis — Generative Visual AI in News Organizations
- Nieman Lab — Newsrooms AI-generated imagery 2026
- DW Innovation — Visual AI Revolution

### B. Glossary

- **Character Reference:** Fonction Leonardo pour maintenir cohérence personnage
- **Fixed Seed:** Valeur permettant reproduction image similaire
- **Guidance Scale:** Contrôle adhérence au prompt (haut = strict)
- **Prompt Magic:** Boost créativité Leonardo (0.75 = optimal)
- **RAW Mode:** Mode évitant AI drift sur prompts longs
- **Style Reference:** Transfert style d'une image à une autre
- **Style Anchor:** Image/template définissant identité visuelle série

### C. Changements Clés v2.0 → v3.0

1. **Focus modèles:** Ideogram/Phoenix → Lucid Origin/Flux 2 Pro
2. **Scope:** Single image → Series d'images cohérentes
3. **Intelligence:** Manuel → Auto-sélection modèle
4. **Cohérence:** Mentionnée → Systémique (seeds + refs)
5. **Contexte:** Prompt isolé → Compréhension article
6. **Identité:** Générique → Truth Engine specific

---

*Document généré suite à recherche web exhaustive — Mars 2026*
*Prêt pour implémentation Phase 1*
