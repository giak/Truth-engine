# Design — Refonte élégance schémas mermaid v33.0

**Date** : 2026-06-06
**Statut** : approuvé
**Périmètre** : 5 schémas du guide (`SUBLIMATOR_v33.0_GUIDE_HUMAN.md`) : §1.1, §2.3, §6.2, §7.1, §9.8

## Choix de design (résumé)

| Dimension | Choix |
|---|---|
| Scope | Modéré (fix + classDefs + subgraphs + base + linear + direction) |
| Thème visuel | Coloré pédagogique (5+ couleurs par fonction) |
| Cohérence | Thème partagé (vert/rouge/jaune) + couleur dominante par section |
| Syntaxe | Frontmatter YAML v11.14+ (préféré à `%%{init}%%`) |
| Edges | `linear` (au lieu de `basis` default) |
| Direction | TD pour hiérarchies, LR conservé pour §2.3 et §9.8 |

## Palette partagée (classDefs)

| Nom | Rôle | Fill | Stroke | Text |
|---|---|---|---|---|
| `phasePass` | succès / PASS | `#dcfce7` | `#16a34a` | `#14532d` |
| `phaseFail` | FAIL / HALT | `#fee2e2` | `#dc2626` | `#7f1d1d` |
| `phaseDecide` | décision (diamond) | `#fef9c3` | `#ca8a04` | `#713f12` |
| `phaseRetry` | retry / boucle | `#ffedd5` | `#ea580c` | `#7c2d12` |
| `phaseAudit` | audit / transverse | `#ede9fe` | `#7c3aed` | `#4c1d95` |
| `phaseData` | pipeline / flux | `#dbeafe` | `#2563eb` | `#1e3a8a` |
| `phaseExit` | terminaux (stade) | `#e2e8f0` | `#475569` | `#0f172a` |

## Couleur dominante par section

| Section | Schéma | Dominante | Application |
|---|---|---|---|
| §1.1 | Architecture globale | `phaseData` | Nœuds PIPE ; transverses en `phaseAudit` |
| §2.3 | Voyage 6 phases | `phaseData` | Subgraphs S0-S6 en `phaseData`, HALT en `phaseFail` |
| §6.2 | Stratégie d'échec | `phaseRetry` | Algorithme = chemin retry→halt, gates en `phaseDecide` |
| §7.1 | Graphe des phases | `phaseData` | Pipeline principal + halte rouge |
| §9.8 | Walkthrough | `phaseAudit` | Sequence diagram : lifeline en `phaseAudit`, gates en `phaseDecide` |

## Frontmatter (snippet commun)

```yaml
---
config:
  theme: base
  themeVariables:
    primaryColor: '#f8fafc'
    primaryTextColor: '#0f172a'
    primaryBorderColor: '#334155'
    lineColor: '#64748b'
    fontFamily: 'system-ui, -apple-system, sans-serif'
    fontSize: '13px'
  flowchart:
    curve: linear
    htmlLabels: true
---
```

## Modifications structurelles par schéma

### §1.1 (Architecture globale)
- 3 subgraphs existants (EXT/CORE/SIDE) conservés
- Nœuds P0-P6, G0-G6 renommés en étapes lisibles : `PH0["§0"]` → `PH0["§0<br/>Diagnostic"]`
- Diamonds (G0-G6) → class `phaseDecide`
- PIPE subgraph → class `phaseData`
- SIDE subgraph → class `phaseAudit`
- ARTICLE terminal → class `phaseExit`

### §2.3 (Voyage 6 phases)
- 7 subgraphs S0-S6 → class `phaseData` par défaut
- HALT0-HALT6 → class `phaseFail`
- Diamonds G0-G6 → class `phaseDecide`
- Arête PASS → `linkStyle` en vert ; FAIL → en rouge
- PUBLICATION terminal → class `phaseExit`

### §6.2 (Stratégie d'échec)
- Diamonds CHECK/R1/A1 → class `phaseDecide`
- PASS nœud → class `phasePass`
- RETRY nœud → class `phaseRetry`
- HALT nœud → class `phaseFail`
- ONEFIN → class `phaseAudit`
- Toutes les arêtes des diamonds sont labelisées (déjà OK)

### §7.1 (Graphe des phases)
- Diamonds G0-G6 → class `phaseDecide`
- P0-P6 → class `phaseData`
- R0-R6 (retry) → class `phaseRetry`
- HALT terminal → class `phaseFail`
- PUBLISH terminal → class `phaseExit`
- INIT terminal → class `phaseExit`
- Arête PASS → `linkStyle` vert épais ; FAIL → rouge

### §9.8 (Walkthrough)
- Sequence diagram : `%%{init}%%` directive (pas de frontmatter pour sequence)
- Participants O, CE, CC, D, AR, FC, R, S, AU, TC → class `phaseAudit` sur les lifelines
- Messages O→O internes → `phaseDecide` (les gates)
- Acteur U (humain) → `phaseExit` au début/fin
- `par` blocks pour parallélisme §1 et §6
- `note over` explicatifs pour les gates PASS/FAIL

## Validation

1. Render de chaque bloc sur [mermaid.live](https://mermaid.live/) (vérif syntaxe)
2. Render GitHub : commit, vérif rendu sur github.com
3. Render VSCode : extension Mermaid, vérif preview
4. Cross-refs texte : vérifier que les renvois aux schémas (§1.1, §2.3, etc.) restent valides
5. Pas d'invention : aucun nœud ajouté, juste re-styling + re-naming
