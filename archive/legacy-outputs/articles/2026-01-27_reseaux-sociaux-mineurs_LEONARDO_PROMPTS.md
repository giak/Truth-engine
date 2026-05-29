# Leonardo.ai Image Prompts — La France Qui Abandonne

**Article:** `/enquetes_verite_2026/articles/2026-01-27_reseaux-sociaux-mineurs_ARTICLE_V4_SUBLIMATOR.md`
**Système:** Promptsmith v2.0 (voir `/prompts/systems/promptsmith-leonardo-v2.0.md`)

---

## Brief Initial

**Sujet principal:** Cover article — asymétrie État français (contrôle virtuel vs abandon physique)

**Éléments à représenter:**
- Main: Smartphone/réseau social contrôlé par l'État
- Contexte: Narco prospère, enfants ASE abandonnés, Macron/Bayrou
- Émotion: Dissonance, hypocrisie, abandon

**Format:** 16:9 (horizontal)
**Palette:** Rouge (alerte) + Bleu froid (institutionnel) + Noir (censure)
**Style:** Editorial photographique, réalisme sobre, composition géométrique

---

## Variant A — Double Écran

**Concept:** Deux écrans côte à côte — contrôle virtuel vs abandon physique

### Positive Prompt (EN) [315 chars]
```
Split screen editorial photograph, left side clean smartphone displaying digital ID verification interface in blue-white institutional colors, right side chaotic urban scene with shadow figures and broken shields, geometric division line, dramatic side lighting, desaturated reds and cold blues, high contrast, the text "LA FRANCE QUI ABANDONNE" in bold sans-serif centered below, newspaper editorial style
```

### Negative Prompt (EN) [156 chars]
```
blurry, low resolution, cartoonish, 3D render, distorted hands, extra fingers, text errors, watermarks, signatures, happy children, clean streets, bright colors, decorative elements
```

### Model & Settings
```
Model: Phoenix 1.0 (complex adherence - split screen)
Prompt Magic: 0.75
Guidance: 8
RAW Mode: ON
Aspect Ratio: 16:9
Negative Prompt: [ci-dessus]
Number of Images: 6
```

---

## Variant B — Iceberg Numérique

**Concept:** Iceberg stylisé — sommet numérique propre, masse sombre avec corruption/abandon

### Positive Prompt (EN) [295 chars]
```
Digital iceberg concept art, upper portion pristine smartphone apps and verification checkmarks in sterile white-blue light, lower portion submerged in darkness revealing broken shields, scattered money bags, and child silhouettes in shadow, cold oceanic palette with deep blacks, dramatic underwater lighting from above, the text "10% PROTECTION 90% ABANDON" in white bold sans-serif at bottom, editorial illustration style
```

### Negative Prompt (EN) [148 chars]
```
blurry, pixelated, cartoonish, photorealistic, warm colors, cheerful elements, happy children, clean water, sparkles, decorative, tropical, text errors, drugs, needles, weapons
```

### Model & Settings
```
Model: Phoenix 1.0 (concept adherence)
Prompt Magic: 0.75
Guidance: 8
RAW Mode: ON
Aspect Ratio: 16:9
Negative Prompt: [ci-dessus]
Number of Images: 6
```

---

## Variant C — Main de Fer

**Concept:** Gantelet numérique écrasant un écran, fond avec symboles institutionnels et déclin

### Positive Prompt (EN) [290 chars]
```
Editorial photograph, iron gauntlet hand emerging from abstract French flag patterns gripping and crushing a smartphone showing app icons, cracks spreading across screen, dramatic chiaroscuro lighting, desaturated red and blue, geometric composition, the text "L'ÉTAT CONTRÔLE" in bold red sans-serif on top left, newspaper cover aesthetic
```

### Negative Prompt (EN) [142 chars]
```
blurry, low resolution, cartoonish, photorealistic, 3D render, deformed hands, missing fingers, happy children, bright colors, peaceful scene, text errors, drugs, cocaine, needles
```

### Model & Settings
```
Model: Phoenix 1.0 (composition adherence)
Prompt Magic: 0.75
Guidance: 8
RAW Mode: OFF
Aspect Ratio: 16:9
Negative Prompt: [ci-dessus]
Number of Images: 6
```

---

## Comparison Table

| Criterion | Variant A (Split) | Variant B (Iceberg) | Variant C (Gauntlet) |
|-----------|------------------:|--------------------:|---------------------:|
| **Clarity** | 9/10 | 8/10 | 7/10 |
| **Impact** | 7/10 | 9/10 | 10/10 |
| **Concept Clarity** | 8/10 | 9/10 | 6/10 |
| **Editorial Fit** | 10/10 | 8/10 | 7/10 |
| **Text Integration** | 9/10 | 10/10 | 6/10 |
| **Leonardo Adherence** | 8/10 | 7/10 | 9/10 |
| **Overall** | **8.5/10** | **8.3/10** | **7.5/10** |

---

## Fusion (Final)

**Rationale:** Fusion de A (split screen structure) + B (metaphorical depth) + C (emotional impact). La structure bicéphale de A permet de montrer l'asymétrie. L'iceberg de B ajoute la dimension Ξ (10% visible, 90% caché). Le gauntlet de C renforce l'idée de contrôle.

### Positive Prompt (EN) [395 chars]
```
Editorial split-screen photograph, left side pristine digital verification interface with smartphone showing age check and government seal in sterile institutional blue-white light, right side chaotic France with shadow figures and broken institutional symbols, dramatic side lighting, desaturated reds and cold blues, geometric vertical division, the text "LA FRANCE QUI ABANDONNE" in bold white sans-serif centered below, the text "10% PROTECTION 90% ABANDON" in smaller white sans-serif at bottom, newspaper cover aesthetic, sophisticated composition
```

### Negative Prompt (EN) [175 chars]
```
blurry, low resolution, pixelated, cartoonish, 3D render, distorted hands, extra fingers, deformed limbs, text errors, misspellings, watermarks, signatures, happy children, clean streets, bright colors, warm tones, decorative elements, tropical, sparkles, drugs, cocaine, needles, weapons, blood
```

### Model & Settings
```
Model: Phoenix 1.0 (fusion complexity requires max adherence)
Prompt Magic: 0.75
Guidance: 8
RAW Mode: ON (prompt >100 mots)
Aspect Ratio: 16:9
Negative Prompt: [ci-dessus]
Number of Images: 8
Seed: [optionnel - tester A/B]
```

---

## Suggested Images List

| # | Sujet | Format | Priority | Variant |
|---|-------|--------|----------|---------|
| 1 | Cover principale | 16:9 | Haute | Fusion |
| 2 | Asymétrie virtuelle/physique | 16:9 | Haute | A |
| 3 | Iceberg (10%/90%) | 16:9 | Moyenne | B |
| 4 | Censure ARCOM | 4:5 | Moyenne | C |
| 5 | Corruption/Désintégration | 16:9 | Basse | A (adapté) |
| 6 | Enfants abandonnés | 4:5 | Moyenne | B (adapté) |

---

**Note:** Pour textes français (accents), Ideogram 3.0 peut avoir des difficultés. Si échec, tester sans accents: `LA FRANCE QUI ABANDONNE` → `LA FRANCE QUI ABANDONNE` (identique) ou variante ASCII.
