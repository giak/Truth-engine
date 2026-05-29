# Leonardo.ai Prompts — Pourquoi les Électeurs Français Votent pour Leurs Bourreaux

**Article:** `articles/2026-03-17_0620_electeurs_bourreaux_ARTICLE.md`
**Date:** 2026-03-17

---

## Image 1: HERO (Cover)

**Model:** Flux 2 Pro
**Rationale:** Impact maximal, paradoxe visible sans explication

### Recommended
```
French voting machine revealed as theatrical prop, seven gears spinning behind velvet curtain, each gear labeled with documentary text in french: CORRUPTION, CLIENTÉLISME, MÉDIAS, LOBBYING, CENSURE, PRÉCARITÉ, ÉTAT CAPTIF. In foreground, ballot slip showing politician name with legal case number. Editorial photorealism, dramatic chiaroscuro from stage light, palette: deep blacks (#0a0a0f), warning amber (#ff6b35), authority blue (#2563eb), grainy film texture, professional investigative journalism aesthetic, truth engine visual identity
```

**Settings:**
```yaml
Model: "Flux 2 Pro"
Guidance_Scale: "4"
Steps: "35"
Aspect_Ratio: "16:9"
Seed: "123456789"
```

---

## Image 2: CONTEXT (7 Piliers)

**Model:** Lucid Origin
**Rationale:** Illustration des 7 mécanismes de la démocratie captive

### Recommended
```
Corporate infographic style visualization: seven pillars of French democracy turned into structural supports holding up a decaying building labeled "RÉPUBLIQUE". Each pillar cracked: corruption pillar with euro signs, clientelism with briefcases, media with TV towers, lobbying with law books, censorship with X TikTok logos, poverty with poverty line, state capture with corporate handshake. Documentary photography aesthetic, high contrast, palette: deep blacks (#0a0a0f), warning amber (#ff6b35), authority blue (#2563eb), text in french, the text 'CORRUPTION' 'CLIENTÉLISME' 'MÉDIAS' 'LOBBYING' 'CENSURE' 'PRÉCARITÉ' 'ÉTAT CAPTIF' in bold sans-serif font
```

**Settings:**
```yaml
Model: "Lucid Origin"
Generation_Mode: "Ultra"
Image_Dimensions: "16:9"
Number_of_Images: "4"
Private_Mode: "ON"
Seed: "123456790"
```

---

## Image 3: CONTEXT (Censure Architecture)

**Model:** Flux 2 Pro
**Rationale:** Montrer la cascade EU → France → Plateformes

### Recommended
```
Three-layer architectural diagram of European censorship: foundation labeled "DSA 2024" made of surveillance cameras, middle section "ARCOM FRANCE" made of legal documents and gavel, top layer "PLATEFORMES X TIKTOK META" made of smartphone screens. Each layer connected by data pipelines. Photorealistic architectural photography, dramatic side lighting, palette: deep blacks (#0a0a0f), warning amber (#ff6b35), authority blue (#2563eb), text in french, the text 'DSA' 'ARCOM' 'CENSURE' in elegant serif font
```

**Settings:**
```yaml
Model: "Flux 2 Pro"
Guidance_Scale: "4"
Steps: "35"
Aspect_Ratio: "16:9"
Seed: "123456791"
```

---

## Image 4: CONTEXT (Candidats Problématiques)

**Model:** Lucid Origin
**Rationale:** Montrer les candidats accusés/condamnés réélus

### Recommended
```
Abstract portrait series: six silhouettes of French politicians who won elections despite legal cases. Each silhouette surrounded by floating symbols: gavel for convicted, question mark for under investigation, euro signs for corruption, handcuffs for crimes. Background is blurred voting crowd. Editorial photography, dramatic lighting from silhouette edge, palette: deep blacks (#0a0a0f), warning amber (#ff6b35), truth engine visual identity, text in french, the text 'BAYLET' 'DATI' 'ABAD' 'BOURDOULEIX' 'DEGALLAIX' 'PERDRIAU' in bold sans-serif font
```

**Settings:**
```yaml
Model: "Lucid Origin"
Generation_Mode: "Ultra"
Image_Dimensions: "1:1"
Number_of_Images: "6"
Private_Mode: "ON"
Seed: "123456792"
```

---

## CONSISTENCY SUMMARY

| Element | Value |
|---------|-------|
| **Seed Base** | 123456789 |
| **Style Anchor** | editorial photorealism, dramatic chiaroscuro, grainy film texture |
| **Palette** | #0a0a0f (deep black), #ff6b35 (warning amber), #2563eb (authority blue) |
| **Models** | Flux 2 Pro (Hero, Censure), Lucid Origin (Piliers, Candidats) |
| **Text** | Always in french |

---

## RÈGLE TEXT FRANÇAIS

| Modèle | Limite | Format |
|--------|--------|--------|
| Lucid | ≤25 chars | `the text 'XXX' in bold sans-serif font` |
| Flux | ≤40 chars | `the text 'XXX' in elegant serif font` |

**Note:** Toujours préciser `text in french` dans le prompt.
