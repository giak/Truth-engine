# Leonardo.ai Prompt — "PERDRE ENFANTS" WWI Propaganda Poster

**Date:** 2025-11-19 19:45
**Context:** Tweet investigation Mandon "accepter perdre nos enfants" (18/11/2025)
**Infographic:** Option 2 — Poster propaganda WWI 1914 style documentary
**Iterations:** v1 → v5 (user feedback: text smaller, soldiers realistic candid, armed with rifles, no yellow banner)

---

## FINAL PROMPT (v5) — ARMED POILUS MARCHING

### Positive Prompt (EN) [497 chars]

```
1914 WWI French propaganda poster based on authentic documentary photograph, the text "PERDRE ENFANTS" in bold distressed military stencil font upper third, candid shot of French poilus soldiers in WWI uniforms and Adrian helmets carrying Lebel rifles shouldered and slung over backs with full military packs marching toward front in natural unposed formation captured in motion, shot from low-angle perspective showing columns receding toward distant horizon, realistic battlefield atmosphere with dust and worn equipment, dramatic cinematic lighting, blood red typography on deep black backdrop, sepia-toned photographic realism with coarse film grain, torn paper edges, gritty documentary authenticity
```

### Negative Prompt (EN) [268 chars]

```
blurry, low resolution, pixelated, unarmed soldiers, empty hands, perfectly aligned toy soldiers, rigid military parade formation, symmetrical rows, staged studio photography, abstract silhouettes, shapeless crowd, cartoonish, 3D render, modern uniforms, modern weapons, cheerful colors, soft lighting, clean fonts, watermarks, misspelled text, fantasy armor, posed soldiers standing at attention
```

### Model & Settings

```yaml
Model: Ideogram 3.0
Rationale: Text-in-image MEILLEUR (≤25 chars "PERDRE ENFANTS" = 14 chars), photographic realism + detailed equipment rendering

Prompt Magic: 0.75
Guidance: 8
RAW Mode: ON (prompt >100 words)
Aspect Ratio: 16:9
Negative Prompt: [above]
Number of Images: 6-8
Seed: [optional for A/B testing]
```

---

## ITERATION HISTORY

### v1 (Original Fusion)
- Text: "massive bold" (TOO BIG per user)
- Soldiers: "faded silhouettes in misty background lower third"
- Yellow banner: present (purpose unclear)

**User feedback**: "c'est un peu gros le texte" + "soldats legerement plus en contre plongé, que l'on voyes le nombre"

### v2 (Text Size + Low-Angle)
- Text: "bold" (reduced from "massive")
- Soldiers: "dense formation [...] shot from low-angle perspective filling lower two-thirds"
- Yellow banner: "single warning yellow diagonal accent stripe" (still present)

**User feedback**: "cela ne fait pas réaliste la troupe de soldats, c'est un 'tas'. des colonnes qui marchent vers le front est mieux, le rendu doit etre plus réaliste, proche de la réalité. il y a plein d'images qui existent de la 1914 WWI pour s'insipirer"

### v3 (Realistic WWI Columns)
- Base: "realistic photographic base inspired by historical WWI photographs"
- Soldiers: "organized columns of French poilus soldiers in authentic WWI uniforms and Adrian helmets marching in tight formation"
- Details: "sepia-toned photographic realism", "historical accuracy"

**User feedback**: "option D" (remove yellow banner) + "les soldats sont rangés comme des petit soldats de plombs. cela doit faire réaliste, comme uen photo prise sue le vif de soldats qui marchent vers le front"

### v4 (Candid Documentary Photo)
- Base: "authentic documentary photograph [...] candid shot"
- Soldiers: "natural unposed formation captured in motion"
- Yellow banner: REMOVED (Option D)
- Negative: Added "perfectly aligned toy soldiers, rigid military parade formation, symmetrical rows, staged studio photography, posed soldiers standing at attention"

**User feedback**: "les soldats ne sot pas équipés de fusils, ils doivent etre équpés"

### v5 (Armed Poilus) — FINAL
- Equipment: "carrying Lebel rifles shouldered and slung over backs with full military packs"
- Negative: Added "unarmed soldiers, empty hands"
- All previous improvements maintained

---

## KEY SPECIFICATIONS

**Text Requirements**:
- Text: "PERDRE ENFANTS" (14 characters, within ≤25 limit Ideogram 3.0)
- Position: Upper third (not centered, leaves space for soldiers)
- Font: Bold distressed military stencil
- Color: Blood red on deep black backdrop

**Soldier Requirements**:
- Uniforms: French poilus WWI authentic + Adrian helmets
- Weapons: Lebel rifles (shouldered/slung) + full military packs
- Formation: Natural unposed candid (NOT aligned toy soldiers)
- Perspective: Low-angle showing columns receding toward horizon
- Movement: Captured in motion (documentary feel)

**Aesthetic Requirements**:
- Base: Authentic documentary photograph 1914 WWI
- Treatment: Sepia-toned, coarse film grain, torn paper edges
- Lighting: Dramatic cinematic from above
- Atmosphere: Realistic battlefield (dust, worn equipment)
- Style: Gritty documentary authenticity (NOT staged studio)

**Exclusions** (Negative Prompt):
- ❌ Unarmed soldiers, empty hands
- ❌ Perfectly aligned toy soldiers
- ❌ Rigid military parade formation
- ❌ Staged studio photography
- ❌ Abstract silhouettes, shapeless crowd
- ❌ Modern uniforms/weapons
- ❌ Cartoonish, 3D render
- ❌ Text misspellings, watermarks

---

## PRODUCTION NOTES

**Why Ideogram 3.0 over Phoenix 1.0**:
- Text-in-image: Ideogram 3.0 = fewer misspellings for short text (≤25 chars)
- Photographic realism: Ideogram 3.0 handles detailed equipment better
- Complex prompt: RAW mode ON prevents AI drift (prompt >100 words)

**Expected Output**:
- WWI documentary photograph aesthetic (sepia, grain argentique)
- French poilus in authentic uniforms + Adrian helmets + Lebel rifles
- Natural candid movement (NOT parade rigidity)
- Low-angle perspective showing depth/numbers
- Blood red "PERDRE ENFANTS" text upper third
- Torn poster edges, coarse halftone grain
- Oppressive propaganda atmosphere

**If Results Unsatisfactory**:
1. Try Phoenix 1.0 (better prompt adherence, may sacrifice text quality)
2. Increase Guidance 8 → 9 (stricter control)
3. Add specific reference: "inspired by Roger Berson 1914 photographs" or "Albert Kahn Archives du Planet style"
4. Split into 2 images: text layer + photo layer, composite in Photoshop

---

## RELATED FILES

- Investigation: `/home/giak/projects/truth-engine/logs/2025-11-19_18-12-15_mandon-perdre-enfants-guerre.md` (289KB)
- Tweet: `/home/giak/projects/truth-engine/logs/2025-11-19_18-32-23_mandon-perdre-enfants-tweet.md` (12KB)
- System prompt: `/home/giak/projects/truth-engine/prompts/promptsmith-leonardo.md` (v2.0)

---

**Status:** Ready for production Leonardo.ai
**Copy-paste:** Positive + Negative prompts + Settings into Leonardo.ai UI
**Generate:** 6-8 images, select best candidate

**End of document**
