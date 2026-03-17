# Promptsmith Leonardo v3.1 — Quickstart

> Démarrage rapide en 3 étapes

---

## 1. Workflow (3 Phases)

```
ANALYZE → DESIGN → GENERATE
```

| Phase | Tu fais | Résultat |
|-------|---------|----------|
| **ANALYZE** | Lire l'article, extraire 3-5 moments visuels | Liste priorisée |
| **DESIGN** | Choisir modèles, définir style anchor | Plan série |
| **GENERATE** | Écrire prompts A/B, documenter | Prompts prêts |

---

## 2. Choix du Modèle

```
Texte complexe (>25 chars) → Flux 2 Pro
Sinon → Lucid Origin (défaut)
```

| Modèle | Quand l'utiliser | Paramètres clés |
|--------|------------------|-----------------|
| **Lucid Origin** | Usage général, rapide | Generation Mode: Ultra |
| **Flux 2 Pro** | Texte, photoréalisme max | Guidance Scale: 4, Steps: 35 |

---

## 3. Structure Prompt

```
[Subject] + [Style TE] + [Composition] + [Lighting] + [Colors] + [Details]
```

### Style Anchor (à inclure dans chaque prompt)
```
editorial photorealism, dramatic chiaroscuro lighting,
palette: deep blacks (#0a0a0f), warning amber (#ff6b35), authority blue (#2563eb),
grainy film texture, truth engine visual identity
```

### Palette TE
- 🔵 `#2563eb` — Authority Blue (confiance)
- 🟠 `#ff6b35` — Warning Amber (alerte)
- ⬛ `#0a0a0f` — Deep Black (profondeur)

---

## 4. Exemple Rapide

**Input:** Article sur fraude fiscale

**Output:**
```yaml
Image 1 (Hero - Flux 2 Pro):
Positive: "
  Create: Silhouetted figure in suit examining offshore documents,
  the text 'LES OUBLIÉS' in bold sans-serif top center,
  editorial photorealism, dramatic chiaroscuro lighting,
  palette: deep black (#0a0a0f), warning amber (#ff6b35) light sources,
  authority blue (#2563eb) document highlights,
  grainy film texture, truth engine visual identity
"
Settings: { Guidance_Scale: 4, Steps: 35, Seed: 147258369 }

Image 2 (Context - Lucid Origin):
Positive: "
  Close-up of financial documents with offshore account numbers,
  editorial photorealism, shallow depth of field,
  dramatic side lighting, authority blue highlights on key figures,
  warning amber accents, deep black background,
  grainy film texture, truth engine visual identity
"
Settings: { Generation_Mode: Ultra, Seed: 147258370 }
```

---

## 5. Checklist Livraison

- [ ] Palette TE présente (#2563eb, #ff6b35, #0a0a0f)
- [ ] Style Anchor inclus
- [ ] Negative prompt qualité + safety
- [ ] Settings adaptés au modèle
- [ ] Seeds documentés pour cohérence
- [ ] Variants A (Safe) + B (Impact)

---

*Promptsmith Leonardo v3.1*
*Truth Engine — 2026*
