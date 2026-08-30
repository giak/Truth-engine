# XQ204 — audit de rollback des figures — 25 août 2026

## Verdict

**PASS — rollback exact vers les figures XQ203.**

La tentative D « mobile-first » est classée `REJECTED_VISUAL_REGRESSION / YAGNI`. Elle reste archivée uniquement pour traçabilité sous `annexes/rejected/XQ204_PASS_D_VISUAL_REGRESSION/`. L’article XQ204 ne référence que les cinq PNG canoniques dans `figures/`.

## Empreintes
| Fichier | SHA-256 XQ203 | SHA-256 courant | Identique |
|---|---|---|---|
| `FIG_01_VERIFICATION_ET_LABEL.png` | `163e4b38be25f9a1fc2a03ce38db9be1bcc4f4fa5d0630dde4bcb83e2b87ddbd` | `163e4b38be25f9a1fc2a03ce38db9be1bcc4f4fa5d0630dde4bcb83e2b87ddbd` | PASS |
| `FIG_01_VERIFICATION_ET_LABEL.svg` | `4ff8a69f22eaccf1aae4963d45d205a8cd2cf3641bbca9ecafc227b51fdc0df7` | `4ff8a69f22eaccf1aae4963d45d205a8cd2cf3641bbca9ecafc227b51fdc0df7` | PASS |
| `FIG_02_CONTINUUM_EPISTEMIQUE.png` | `07713c717b3f3af0c0a9d4bf3f8f494af47c28e75dae3eb378d8f8b306a4c4db` | `07713c717b3f3af0c0a9d4bf3f8f494af47c28e75dae3eb378d8f8b306a4c4db` | PASS |
| `FIG_02_CONTINUUM_EPISTEMIQUE.svg` | `0a6143aae5ac1be17f5f195f6a84146f9fb3db1298ee91076dece9ba5c78edb8` | `0a6143aae5ac1be17f5f195f6a84146f9fb3db1298ee91076dece9ba5c78edb8` | PASS |
| `FIG_03_MODELE_AU_SLOGAN_X12.png` | `a704f1711ad4c3f7ec67e9b554162b434de57483fa48976052e923c48623b21d` | `a704f1711ad4c3f7ec67e9b554162b434de57483fa48976052e923c48623b21d` | PASS |
| `FIG_03_MODELE_AU_SLOGAN_X12.svg` | `be4275e48fc448e882d3f269d95ebc506c7fa50a86e038e877d0a0c2d132efae` | `be4275e48fc448e882d3f269d95ebc506c7fa50a86e038e877d0a0c2d132efae` | PASS |
| `FIG_04_CORRECTION_CONTEXTUALISATION_REPARATION.png` | `f32f435740d80916c2a55b224e29437355145d34116fccede02402f459181671` | `f32f435740d80916c2a55b224e29437355145d34116fccede02402f459181671` | PASS |
| `FIG_04_CORRECTION_CONTEXTUALISATION_REPARATION.svg` | `220293fce6558fce44bf75e9415429290de06e64539976c84c394af64519790d` | `220293fce6558fce44bf75e9415429290de06e64539976c84c394af64519790d` | PASS |
| `FIG_05_FALSIFICATION_REPARATION.png` | `b22a72ebe333052d7a918138e0fc6d044b6aba799ab70125c7907e520b81b1d7` | `b22a72ebe333052d7a918138e0fc6d044b6aba799ab70125c7907e520b81b1d7` | PASS |
| `FIG_05_FALSIFICATION_REPARATION.svg` | `a3499d165aa982e17583fdee455407676ea68f3cc4f7dd13cc2b0d23719ee404` | `a3499d165aa982e17583fdee455407676ea68f3cc4f7dd13cc2b0d23719ee404` | PASS |

## Contrôles
- 10/10 fichiers graphiques (5 SVG + 5 PNG) identiques octet pour octet à XQ203.
- 5/5 SVG parsés comme XML valides.
- 5/5 PNG : 2 400 × 1 500 px.
- 5 références d’image dans l’article ; aucune référence `mobile`, `rejected` ou variante D.
- Aucun besoin « mobile-first » n’est retenu pour la publication Substack.

## Décision
`XQ204_PASS_D_MOBILE_FIGURES = REJECTED`  
`XQ204_FIGURE_ROLLBACK = PASS`  
`CANONICAL_FIGURES = XQ203_RESTORED_BYTE_IDENTICAL`
