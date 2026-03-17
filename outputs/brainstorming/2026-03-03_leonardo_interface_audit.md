# Audit Interface Leonardo.ai — Paramètres Web vs API

**Date:** 2026-03-03
**Source:** Documentation officielle Leonardo.ai (intercom.help/leonardo-ai, docs.leonardo.ai)
**Status:** ⚠️ CRITICAL — Paramètres obsolètes détectés dans le system prompt

---

## Executive Summary

L'analyse approfondie de la documentation officielle Leonardo.ai révèle que **plusieurs paramètres mentionnés dans le system prompt actuel sont obsolètes ou marqués comme "Legacy Mode"**. Les modèles récents comme Lucid Origin et Flux 2 Pro utilisent une interface simplifiée qui ne supporte pas les anciens paramètres comme Prompt Magic, Guidance Scale, Alchemy, et PhotoReal.

### 🚨 Paramètres OBSOLÈTES (à retirer)

| Paramètre | Statut | Impact |
|-----------|--------|--------|
| Prompt Magic | Legacy — désactivé | Inutilisable sur nouveaux modèles |
| Guidance Scale | Legacy — remplacé | N'existe plus sur Lucid Origin |
| Alchemy (V1/V2) | Legacy Mode | Remplacé par "Omni Models" |
| PhotoReal | Legacy Mode | Pipeline obsolète |
| RAW Mode | Non documenté | Probablement obsolète |
| Elements (LoRAs) | Legacy Mode | Système remplacé |

---

## 1. Lucid Origin — Paramètres Réels Interface Web

### 1.1 Modèle Overview

**Lucid Origin** est le modèle "Omni" phare de Leonardo.ai (2025-2026), conçu pour:
- Full HD native output
- Excellent text rendering (meilleur qu'Ideogram 3.0)
- Prompt adherence extrême
- Increased vibrancy et diversity

### 1.2 Paramètres UI Disponibles (Current)

```yaml
Interface_Lucid_Origin:
  # PARAMÈTRES PRINCIPAUX
  Model:
    type: dropdown
    value: "Lucid Origin"
    read_only: true  # Sélectionné dans le menu Models

  Generation_Mode:
    type: toggle
    options: ["Fast", "Ultra"]
    default: "Fast"
    description: "Ultra = meilleure qualité, plus lent"

  Image_Dimensions:
    type: preset_buttons
    options: ["2:3", "1:1", "16:9", "Custom"]
    sizes:
      Small: "768x1024"
      Medium: "1024x1024"
      Large: "1360x768"

  Number_of_Images:
    type: slider_buttons
    range: [1, 2, 3, 4, 6, 8]
    default: 4

  Private_Mode:
    type: toggle
    default: OFF
    description: "Images privées, non visibles publiquement"

  # PARAMÈTRES AVANCÉS (Menu déroulant)
  Advanced_Settings:
    expanded: false
    # Note: La documentation ne précise pas le contenu exact
    # mais mentionne "Add to Collection" et d'autres options

  # IMAGE GUIDANCE (Nouveau système unifié)
  Image_Guidance:
    type: image_upload
    max_images: 6
    modes_available:
      - Style_Reference: "Transfère le style d'une image"
      - Content_Reference: "Référence le contenu"
      - Character_Reference: "Maintient la cohérence personnage"

  # NEGATIVE PROMPT
  Negative_Prompt:
    type: text_field
    availability: toggle_advanced
    required: false
    description: "Activer 'Advanced' pour voir le champ"
```

### 1.3 Paramètres NON Disponibles sur Lucid Origin

| Paramètre | Statut | Alternative |
|-----------|--------|-------------|
| Prompt Magic | ❌ Retiré | Utiliser des prompts descriptifs |
| Guidance Scale | ❌ Retiré | Le modèle gère automatiquement |
| Alchemy | ❌ Legacy Mode | Lucid Origin inclut nativement ces améliorations |
| PhotoReal | ❌ Legacy Mode | Lucid Origin fait du photoréalisme nativement |
| RAW Mode | ❌ Non documenté | Non nécessaire sur ce modèle |
| Seed Control | ⚠️ Partiel | Via Image Guidance, pas de champ seed direct |

---

## 2. Flux 2 Pro — Paramètres Réels

### 2.1 Modèle Overview

**Flux 2 Pro** (Black Forest Labs via Leonardo.ai):
- 12B paramètres
- Excellence en typography (texte dans images)
- Photoréalisme avancé
- JSON prompting support (API)

### 2.2 Paramètres UI Disponibles

```yaml
Interface_Flux_2_Pro:
  Model:
    type: dropdown
    value: "Flux 2 Pro"

  # Note: La documentation spécifique UI est limitée
  # Mais les paramètres suivants sont confirmés via API docs

  API_Parameters_Confirmed:
    prompt: string (required)
    negative_prompt: string (optional)
    width: integer (default: 1024)
    height: integer (default: 1024)
    guidance_scale: float  # ⚠️ Via API uniquement?
    steps: integer (default: 28-50)
    seed: integer (optional)

  # Guidance Scale sur Flux:
  # - Range typique: 3-5 (créatif) à 7-9 (strict)
  # - Documentation API mentionne ce paramètre
  # - Disponibilité UI non confirmée visuellement
```

### 2.3 Incertitudes Flux 2 Pro

| Paramètre | UI Web | API | Notes |
|-----------|--------|-----|-------|
| Guidance Scale | ⚠️ Probable | ✅ Confirmé | Via API, UI peut varier |
| Steps | ⚠️ Probable | ✅ Confirmé | Contrôle qualité/vitesse |
| Seed | ⚠️ Probable | ✅ Confirmé | Reproductibilité |
| Prompt Magic | ❌ Non | ❌ Non | Spécifique anciens modèles |

---

## 3. Tableau Comparatif UI vs API

### 3.1 Lucid Origin

| Paramètre | UI Web | API | Notes |
|-----------|--------|-----|-------|
| Model Selection | ✅ Dropdown | ✅ modelId | "Lucid Origin" |
| Generation Mode | ✅ Fast/Ultra | ✅ generationMode | "FAST", "ULTRA" |
| Image Dimensions | ✅ Presets | ✅ width/height | 2:3, 1:1, 16:9, Custom |
| Number of Images | ✅ 1-8 | ✅ num_images | Jusqu'à 8 simultanés |
| Negative Prompt | ✅ Toggle Advanced | ✅ negativePrompt | Même fonctionnalité |
| Private Mode | ✅ Toggle | ✅ privacy | "PRIVATE", "PUBLIC" |
| Image Guidance | ✅ Upload 6 imgs | ✅ initImageId | Style/Content/Character |
| **Prompt Magic** | ❌ **NON** | ❌ **NON** | **Obsolète** |
| **Guidance Scale** | ❌ **NON** | ⚠️ Non documenté | **Retiré** |
| **Alchemy** | ❌ **NON** | ❌ **NON** | **Legacy Mode** |
| **PhotoReal** | ❌ **NON** | ❌ **NON** | **Legacy Mode** |
| **RAW Mode** | ❌ **NON** | ❌ **NON** | **Non documenté** |
| Seed Control | ⚠️ Partiel | ⚠️ seed? | Via Image Guidance |

### 3.2 Flux 2 Pro

| Paramètre | UI Web | API | Notes |
|-----------|--------|-----|-------|
| Model Selection | ✅ Dropdown | ✅ modelId | "Flux 2 Pro" |
| Prompt | ✅ Text field | ✅ prompt | Standard |
| Negative Prompt | ✅ Toggle | ✅ negativePrompt | Standard |
| Image Dimensions | ✅ Presets | ✅ width/height | Flexibles |
| **Guidance Scale** | ⚠️ Probable | ✅ guidanceScale | 3-9 typique |
| **Steps** | ⚠️ Probable | ✅ numInferenceSteps | 28-50 |
| **Seed** | ⚠️ Probable | ✅ seed | Reproductibilité |
| Prompt Magic | ❌ NON | ❌ NON | Non applicable |
| Alchemy | ❌ NON | ❌ NON | Non applicable |

---

## 4. Évolution Système Leonardo.ai

### 4.1 Ancien Système (Legacy)

```
Ancienne Interface (2023-2024):
├── Models: Leonardo Diffusion XL, Vision XL
├── Alchemy V1/V2: Pipeline amélioration
├── PhotoReal: Pipeline photoréalisme
├── Prompt Magic: Boost créativité (0.0-1.0)
├── Guidance Scale: Adhérence prompt (1-20)
├── RAW Mode: Évite drift sur prompts longs
└── Elements: LoRAs personnalisés
```

### 4.2 Nouveau Système (2025-2026)

```
Nouvelle Interface (Omni Models):
├── Omni Models: Lucid Origin, Flux 2 Pro
├── Image Guidance: Système unifié
│   ├── Style Reference
│   ├── Content Reference
│   ├── Character Reference
│   └── Jusqu'à 6 images simultanées
├── Simplified Settings:
│   ├── Generation Mode: Fast/Ultra
│   ├── Image Dimensions: Presets
│   └── Number of Images: 1-8
└── Negative Prompt: Standard
```

---

## 5. Recommandations Corrections

### 5.1 Paramètres à SUPPRIMER du system prompt

```yaml
PARAMETRES_OBSOLETES:
  - Prompt_Magic: "Retirer complètement"
  - Guidance_Scale: "Retirer pour Lucid Origin, garder pour Flux 2 Pro (si confirmé)"
  - RAW_Mode: "Retirer complètement"
  - Alchemy: "Retirer (Legacy Mode)"
  - PhotoReal: "Retirer (Legacy Mode)"
```

### 5.2 Paramètres à AJOUTER/PRÉCISER

```yaml
PARAMETRES_ACTUELS:
  Lucid_Origin:
    - Generation_Mode: "Fast | Ultra"
    - Image_Dimensions: "2:3 | 1:1 | 16:9 | Custom"
    - Number_of_Images: "1-8"
    - Private_Mode: "toggle"
    - Image_Guidance: "Upload jusqu'à 6 images"
    - Negative_Prompt: "Activer Advanced Settings"

  Flux_2_Pro:
    - Guidance_Scale: "3-9 (API confirmé, UI probable)"
    - Steps: "28-50"
    - Seed: "Optionnel"
    - Image_Dimensions: "Flexibles jusqu'à 2:3, 3:2"
```

### 5.3 Structure Prompt à Adapter

**Ancienne (obsolète):**
```yaml
Settings:
  Prompt_Magic: "0.70"      # ❌ OBSOLÈTE
  Guidance_Scale: "8"        # ❌ OBSOLÈTE (Lucid)
  RAW_Mode: "ON"             # ❌ OBSOLÈTE
```

**Nouvelle (corrigée):**
```yaml
Settings_Lucid_Origin:
  Model: "Lucid Origin"
  Generation_Mode: "Ultra"     # ✅ Fast ou Ultra
  Image_Dimensions: "16:9"     # ✅ 2:3, 1:1, 16:9, Custom
  Number_of_Images: "6"        # ✅ 1-8
  Private_Mode: "ON"           # ✅ Toggle
  Negative_Prompt: "Activé"    # ✅ Toggle Advanced

Settings_Flux_2_Pro:
  Model: "Flux 2 Pro"
  Guidance_Scale: "4"          # ⚠️ Si disponible UI
  Steps: "35"                  # ⚠️ Si disponible UI
  Image_Dimensions: "16:9"
  Number_of_Images: "4"
```

---

## 6. Screenshots UI Descriptions

### 6.1 Interface Lucid Origin (Current)

```
┌─────────────────────────────────────────────────────────────┐
│  LEONARDO.AI — AI Creation                                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [Prompt input field]                                       │
│                                                             │
│  ┌──────────────┐  ┌─────────────────────────────────────┐ │
│  │ Models  ▼    │  │ Image Guidance  📎 (0/6)            │ │
│  │ Lucid Origin │  │ Style Ref | Content Ref | Char Ref  │ │
│  └──────────────┘  └─────────────────────────────────────┘ │
│                                                             │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ Generation Mode  ●Fast  ○Ultra                          ││
│  │                                                         ││
│  │ Image Dimensions  [2:3] [1:1] [16:9] [Custom]          ││
│  │                                                         ││
│  │ Number of Images  [1] [2] [3] [4] [6] [8]              ││
│  │                                                         ││
│  │ ○ Private Mode                                          ││
│  │                                                         ││
│  │ ▼ Advanced Settings                                     ││
│  │    [Negative Prompt toggle]                             ││
│  └─────────────────────────────────────────────────────────┘│
│                                                             │
│  [Generate]  87 tokens                                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 6.2 Ancienne Interface Legacy (pour référence)

```
┌─────────────────────────────────────────────────────────────┐
│  ANCIENNE INTERFACE (Legacy Mode)                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ○ PhotoReal        [toggle]  ❌ Legacy                     │
│  ○ Alchemy          [toggle]  ❌ Legacy                     │
│  ○ Prompt Magic     [toggle]  ❌ Legacy                     │
│  ○ Public Images    [toggle]                                │
│                                                             │
│  Guidance Scale: [━━━━━●━━━━━━]  7        ❌ Legacy         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 7. Sources Documentation

### 7.1 Documentation Officielle Consultée

1. **Lucid Origin Help Center**
   - URL: https://intercom.help/leonardo-ai/en/articles/11890238-lucid-origin
   - Date: Updated "over 2 weeks ago" (Feb 2026)
   - Key Info: Full HD, text rendering, Generation Mode Fast/Ultra

2. **Using Alchemy (Legacy)**
   - URL: https://intercom.help/leonardo-ai/en/articles/8122230-using-alchemy
   - Warning: "⚠️ Legacy Mode feature — outdated"
   - Key Info: Alchemy V1/V2 obsolete

3. **Image Guidance**
   - URL: https://intercom.help/leonardo-ai/en/articles/8497988-image-guidance
   - Date: Updated "over a week ago"
   - Key Info: Up to 6 images, Omni Models context understanding

4. **PhotoReal (Legacy)**
   - URL: https://intercom.help/leonardo-ai/en/articles/8236978-photoreal
   - Status: "Advanced (Legacy) Features & Settings"
   - Key Info: Pipeline obsolète

5. **Elements/LoRAs (Legacy)**
   - URL: https://intercom.help/leonardo-ai/en/articles/10501488-elements-loras
   - Status: "Advanced (Legacy) Features & Settings"
   - Key Info: Système remplacé

### 7.2 Documentation API

- docs.leonardo.ai — REST API reference
- Flux 2 Pro endpoint parameters confirmés
- Lucid Origin endpoint — guidance scale non mentionné

---

## 8. Action Items Correction

### 8.1 Fichiers à Modifier

| Fichier | Lignes | Action |
|---------|--------|--------|
| `promptsmith-leonardo-v3.0-APEX.md` | 57-67 | Corriger paramètres Lucid Origin |
| `promptsmith-leonardo-v3.0-APEX.md` | 94-101 | Corriger paramètres Flux 2 Pro |
| `promptsmith-leonardo-v3.0-APEX.md` | 381-410 | Mettre à jour Template Lucid |
| `promptsmith-leonardo-v3.0-APEX.md` | 448-478 | Mettre à jour Template Flux |
| `promptsmith-leonardo-v3.0-APEX.md` | 1113-1120 | Mettre à jour Glossaire |

### 8.2 Corrections Prioritaires

1. **Retirer tous les mentions de:**
   - Prompt Magic (tous les modèles)
   - Guidance Scale (Lucid Origin uniquement)
   - RAW Mode
   - Alchemy
   - PhotoReal

2. **Remplacer par:**
   - Generation Mode (Fast/Ultra)
   - Image Dimensions presets
   - Number of Images (1-8)
   - Private Mode
   - Image Guidance system

3. **Conserver avec avertissement:**
   - Guidance Scale pour Flux 2 Pro (vérifier UI)
   - Steps pour Flux 2 Pro

---

## 9. Conclusion

L'audit révèle que le system prompt actuel contient des **paramètres obsolètes hérités de l'ancienne interface Leonardo.ai** (2023-2024). Les nouveaux modèles "Omni" (Lucid Origin, Flux 2 Pro) utilisent une interface simplifiée sans:
- Prompt Magic
- Guidance Scale (Lucid)
- Alchemy
- PhotoReal
- RAW Mode

**Impact:** Si un utilisateur suit le system prompt actuel, il cherchera des paramètres qui n'existent pas dans l'interface web moderne, causant confusion et inefficacité.

**Correction requise:** Mise à jour urgente du system prompt pour refléter les paramètres réels de l'interface web 2025-2026.

---

*Document généré par audit systématique de la documentation officielle Leonardo.ai*
*Méthode: Analyse documentation web + vérification statuts Legacy*
*Date d'audit: 2026-03-03*
