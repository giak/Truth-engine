# Promptsmith Leonardo v3.1 — Annexes

> Documentation complémentaire au CORE
> Consulter en cas de besoin spécifique

---

## A. Changelog

### v3.0 APEX → v3.1 CORE

| Aspect | v3.0 APEX | v3.1 CORE |
|--------|-----------|-----------|
| **Lignes** | ~1 263 | ~435 |
| **Sections** | 8 + 5 annexes | 8 sections lean |
| **Workflow** | 5 phases | 3 phases (RAPIDE) |
| **Templates** | 2 complets + 1 universel | 1 unifié + adaptations |
| **Variants** | A/B/C (3) | A/B (2) |
| **Focus** | Exhaustif | Essential |

**Optimisations majeures:**
- Fusion templates Lucid/Flux → Template unifié adaptatif
- Réduction workflow 5 → 3 phases
- Externalisation changelog, troubleshooting, exemples avancés
- Suppression redondances (negative prompts, style anchor, palette)
- Compression output format

### v2.0 → v3.0 APEX

- Migration Ideogram/Phoenix → Lucid Origin/Flux 2 Pro
- Ajout palette TE standardisée
- Systémisation cohérence visuelle (seeds + refs)
- Support natif Flux 2 Pro + JSON prompting
- Workflow APEX 5 phases
- Quality constraints explicites

---

## B. Troubleshooting Guide

| Problème | Cause probable | Solution |
|----------|---------------|----------|
| Texte illisible | Mauvais modèle ou contraste | Passer à Flux 2 Pro, vérifier contraste background |
| Couleurs incohérentes | Palette TE non appliquée | Vérifier présence HEX codes (#2563eb, #ff6b35, #0a0a0f) |
| Série incohérente | Pas d'Image Guidance | Utiliser Style Reference avec même image anchor |
| Qualité insuffisante | Settings sous-optimaux | Lucid: Ultra mode. Flux: Steps 40-50 |
| Personnage change | Character Reference manquante | Upload personnage de base dans Image Guidance |
| Paramètre non trouvé | Paramètre obsolète | Vérifier: Prompt Magic, RAW Mode obsolètes |

---

## C. Exemples d'Usage

### Exemple 1: Article Complet → Série 3 Images

**Input:** Article Truth Engine sur corruption politique

**Processus:**
1. **ANALYZE:** Moments clés identifiés → Introduction choc, Preuve documents, Révélation
2. **DESIGN:**
   - Hero (cover + titre) → Flux 2 Pro
   - Context (documents) → Lucid Origin
   - Reveal (dénouement) → Flux 2 Pro
3. **GENERATE:** Prompts A/B pour chaque image

**Output:** Série cohérente avec seeds liés (147258369, +1, +2)

### Exemple 2: Image avec Texte Complexe

**Input:** Cover avec titre "LES OUBLIÉS DE LA RÉPUBLIQUE"

**Décision:** 30 caractères > limite Lucid (25) → **Flux 2 Pro obligatoire**

**Prompt:**
```
Create: Silhouetted investigative journalist at desk covered with documents,
the text 'LES OUBLIÉS DE LA RÉPUBLIQUE' in bold sans-serif font centered,
dramatic chiaroscuro lighting in warning amber (#ff6b35)...
```

---

## D. Glossaire

| Terme | Définition |
|-------|------------|
| **Character Reference** | Fonction Leonardo pour cohérence personnage (via Image Guidance) |
| **Fixed Seed** | Valeur pour reproduction image similaire |
| **Generation Mode** | Fast/Ultra — contrôle qualité/vitesse (Lucid uniquement) |
| **Guidance Scale** | Contrôle adhérence au prompt — **Flux uniquement** |
| **Image Guidance** | Système unifié Style/Content/Character Reference (6 images max) |
| **Private Mode** | Protection IP — images non publiques |
| **Style Anchor** | Template définissant identité visuelle série |
| **Steps** | Itérations génération — **Flux uniquement** |

---

## E. Références

- **CORE:** `tools/prompts/systems/promptsmith-leonardo-v3.1-CORE.md`
- **Quickstart:** `tools/prompts/systems/QUICKSTART.md`
- **Documentation Leonardo:** intercom.help/leonardo-ai

---

*Annexes Promptsmith Leonardo v3.1*
*Truth Engine — 2026*
