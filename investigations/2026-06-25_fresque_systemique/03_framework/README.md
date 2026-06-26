# 03_framework — Protocole d'Investigation Systémique

## À quoi sert ce dossier ?

Ce dossier contient le **cadre d'analyse** de la fresque systémique. C'est ici que vit le protocole qui définit *comment* enquêter sur les défaillances silencieuses de la société française, et *avec quels outils* (42 mécanismes, 8 fils, 10 stratégies de résistance).

L'idée : plutôt que de décrire ce qui ne va pas (ça, c'est le travail des enquêtes dans `02_enquetes/`), ce dossier fournit la **grille de lecture** — un langage commun pour diagnostiquer, comparer et agréger les enquêtes.

## Fichiers

| Fichier | Rôle |
|---------|------|
| `2026-06-26_18-30_protocole_investigation_FRAMEWORK_v2.0.md` | **Protocole v2.4 (Pelote de Laine)** — le document de référence. Définit les 10 fils (A-L), les 42 mécanismes (M01-M42), les 10 stratégies (R01-R10), le format YAML de sortie (14 chapitres dont REMONTEE_DES_FILS et CONTRE_MESURES), le barème NREF (12 exigences), la Méthode de la Pelote de Laine (algorithme récursif 5 questions), et le workflow d'exécution. |
| `2026-06-26_21-00_prompt_investigation_v2_PROMPT.md` | **Prompt d'investigation v2.4** — le point d'entrée unique pour lancer une enquête. Contient la mission, le schéma YAML complet (14 chapitres), les contraintes NREF (12 exigences), et l'étape obligatoire de la Pelote de Laine avant l'écriture. |
| `2026-06-25_20-00_empire_mensonge_concepts_extraits_HYPER_MATRICE.md` | **Matrice source** — extraction des concepts de l'article *L'Empire du Mensonge* qui a inspiré les mécanismes M34-M42 et les stratégies R01-R10. |
| `TABLEAU_DE_BORD.md` | **Tableau de bord v2.4** — agrège les 10 enquêtes produites, leurs synthèses, les métriques Pelote, les patterns transversaux, et la file d'attente. |
| `archive/` | Anciennes versions du protocole (v1.0, v1.3) et du prompt v1, conservées pour référence historique. |

## Comment ça s'utilise

1. **Pour lancer une enquête** → utilise le prompt `2026-06-26_21-00_prompt_investigation_v2_PROMPT.md`
2. **Pour comprendre les mécanismes** → consulte le protocole `v2.0.md` (sections M01-M42, R01-R10, carte de navigation)
3. **Pour vérifier la qualité** → applique le barème NREF (12 exigences, dont NREF-11 Pelote et NREF-12 Contre-mesures)
4. **Pour agréger** → alimente le TABLEAU_DE_BORD.md après chaque enquête

## Évolution

- **v1.0** : 8 fils identifiés à partir du sang contaminé
- **v1.1** : 33 mécanismes actifs extraits des articles de la Résistance Cognitive
- **v1.2** : 9 nouveaux mécanismes (M34-M42) et 10 stratégies de résistance de *L'Empire du Mensonge*
- **v1.3** : séparation protocole/prompt, phase Ultrathinking
- **v2.0** : standard NREF — chaîne de preuve, contre-version, déclaration des biais, conditions de réfutation
- **v2.4 (Pelote)** : Méthode de la Pelote de Laine (algorithme 5 questions récursives), REMONTEE_DES_FILS standardisé (marquage, gaps_verifies, cross_reference), CONTRE_MESURES (ch.3.5), 12 exigences NREF
