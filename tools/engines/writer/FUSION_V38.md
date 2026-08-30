# Fusion v38 → Writer : architecture

**Date** : 2026-08-19
**Objet** : réconcilier les deux moteurs de prose du projet en une division du travail unique.

## Problème

Deux moteurs produisent de la prose publiée, sans réconciliation :

- `prompt-v38_phase3.md` : 16 LOIs mélangeant prose, sourcing, causalité, épistémique et règles Substack.
- `tools/engines/writer/` : 9 principes positifs + pont KERNEL-Writer + reviewer + `validate.py`.

Constats factuels : v38 n'a pas produit un article « assez bon » ; Writer n'a jamais été utilisé ; ChatGPT a produit le V6 en ré-inventant le sourcing (58 footnotes) et en dégradant le vocabulaire KERNEL (~40 statuts hétérogènes).

## Décision

**Writer est le moteur de prose. v38 cesse d'être un moteur concurrent et devient une checklist de contraintes d'article, appliquée en validation par-dessus Writer, pas en génération.**

Pipeline cible :

```text
KERNEL           → faits (FACT_REGISTRY, EPI/tier/status, mem:<uuid>)
Sublimator v36   → quintessence (condensation)
Sublimator v37   → synthèse (thèses, clusters)
phase2_5         → blueprint narratif (angle, arc, KO, coupe)
WRITER           → prose (9 principes + pont KERNEL-Writer + reviewer + validate.py)
CHECKLIST v38    → contraintes article (sourcing hybride, édifice, Mnemolite,
                   propagande, niveaux probatoires)
```

## Mapping des 16 LOIs

| LOI v38 | Destination | Statut |
|---|---|---|
| LOI 1 Sourcing hybride | checklist article | amendée 2026-08-19 |
| LOI 2 Sources fin d'article | checklist article | conservée |
| LOI 3 Forme pure (em-dash, tableaux) | `validate.py` + `knowledge.md` | déjà couvert |
| LOI 4 Norme de langue (anglicismes, tics) | STANDARD §2 + `knowledge.md` | déjà couvert |
| LOI 5 Rythme cognitif (asyndète, KO) | STANDARD §6 + phase2_5 | déjà couvert |
| LOI 6 Gras stratégique | checklist article | conservée |
| LOI 7 Densité narrative | STANDARD §1 + §8 | déjà couvert |
| LOI 8 Zéro cuisine interne (F###) | checklist article | conservée |
| LOI 9 Citer l'édifice (wiki-style) | checklist article (Substack) | conservée |
| LOI 10 Personnes vérifiées | pont KERNEL-Writer (step 2) | déjà couvert |
| LOI 11 Zéro métaphore biologique | STANDARD §2 | déjà couvert |
| LOI 12 Allégations sourcées | pont KERNEL-Writer + LOI 1 | déjà couvert |
| LOI 13 Niveaux de preuve A/B/C/D | STANDARD §7 + palette de modalisation | à intégrer dans STANDARD |
| LOI 14 Agrégations décomposées | STANDARD §0 | déjà couvert |
| LOI 15 KO sentences vérifiables | phase2_5 (contrainte 9) + reviewer | déjà couvert |
| LOI 16 Chaîne causale non linéaire | STANDARD §3 | déjà couvert |

## Ce que la checklist article conserve (non-LOI)

- **Mnemolite lecture d'abord** (règle 6) : `read_memory`/`search_memory(status:CONFIRME)`, jamais d'invention de `memory_id`.
- **Usage réglementé du mot « propagande »** (règle 7).
- **Édict cumulatif** (1.1) : citer l'édifice, ne pas réexpliquer.
- **Méthode inverse** (1.2) : introduction méthodologique.
- **Les 6 niveaux probatoires** (LOI 16 + phase2_5 contrainte 10).

## Ce qui est supprimé ou absorbé

- Structure générique §0-§5 de v38 (§2.1) : remplacée par le blueprint (phase2_5).
- « Calibration stylistique » de v38 : redondante avec STANDARD (exemple + contre-exemple).
- Workflow « deux passes » (assemblage/sculpture) : redondant avec Writer (écrire + relecture).
- « Chambre des Titres » : conservée en pratique, à rattacher à Writer step 3.

## État d'avancement

- [x] LOI 1 amendée (sourcing hybride : nommé en phrase + renvoi discret URL/date).
- [ ] Intégrer la palette de modalisation A/B/C/D (LOI 13) dans STANDARD §7.
- [ ] Rattacher la Chambre des Titres à Writer step 3.
- [ ] Archiver les sections v38 redondantes (structure générique, calibration, deux passes).
