# Generic Prompts Design — PROMPT_MASTER + CONTROLEUR APEX

**Date :** 2026-05-27
**Contexte :** Les prompts PROMPT_ARTICLE_MASTER.md et CONTROLEUR_APEX_v2.1.md sont actuellement hardcodés pour la série « Le Changement de Régime ». Objectif : les rendre génériques pour toute série d'investigation Truth Engine.

## Principe : CONFIG block

Chaque fichier commence par un bloc `## CONFIG SÉRIE` que l'utilisateur remplit une fois par série. Tous les `{PLACEHOLDERS}` dans le corps du prompt correspondent à une clé de ce bloc.

Format :
```
SERIE_NOM            = [Le Changement de Régime]    # nom complet
SERIE_REF            = [Le Changement de Régime]    # nom court pour ligne série
HUB_TITRE            = [Le Changement de Régime]
HUB_SOUS_TITRE       = [Pourquoi ce système ne peut pas se réformer]
HUB_FICHIER          = [HUB_le_changement_de_regime.md]
THESE_CARDINALE      = [5 tensions en cascade causale qui se verrouillent mutuellement]
NB_ARTICLES          = [16]
PREFIXE_ENQUETE      = [S]                          # S pour série Changement de Régime
ARTICLE_REF          = [S1 « La Caste Parasite »]   # article modèle
FICHIER_REF          = [S1_la_caste_parasite.md]
SOLUTION_1           = [L'Adieu aux partis]
SOLUTION_2           = [Le Protocole du ré-enracinement]
ENQUETE_DUREE        = [cinq jours (23-26 mai 2026)]
ENQUETE_NB_COMPLEXES = [27]
ARTICLES_PUBLIES     = [86]
PLATEFORME           = [Substack]
```

## PROMPT_ARTICLE_MASTER.md

### Sections inchangées (0, 3 [LOIS], 5, 6 partiel, 8)
- Identité, 8 LOIS, structure narrative, checklist partielle, gestion incertitude

### Sections modifiées (1, 2, 4, 6 partiel, 7, footer)

**Section 1** : placeholders `{SERIE_REF}`, `{NB_ARTICLES}`, `{HUB_FICHIER}` dans les non-négociables

**Section 2** : template structure avec `{SERIE_REF}`, `{NB_ARTICLES}`, `{PLATEFORME}` dans ligne série ; `{ENQUETE_DUREE}`, `{ENQUETE_NB_COMPLEXES}`, `{ARTICLES_PUBLIES}` dans Note enquête ; `{SOLUTION_1}`, `{SOLUTION_2}` dans footer

**Section 4** : remplace la structure hardcodée S1-S16 par un bloc générique avec `{THESE_CARDINALE}` + champ libre pour architecture narrative

**Section 6** : ligne série utilise `{SERIE_REF}`

**Section 7** : `{ARTICLE_REF}`, `{FICHIER_REF}` au lieu de S1

**Footer final** : `{FICHIER_REF}`

## CONTROLEUR_APEX_v2.1.md

CONFIG plus courte (5 clés) : `SERIE_REF`, `HUB_TITRE`, `HUB_SOUS_TITRE`, `PREFIXE_ENQUETE`, `HTML_COMMENTS`

### Modifications
- Titre : « Articles S » → « Articles {PREFIXE_ENQUETE} »
- Contexte reçu pt 4 : thèse cardinale depuis `{THESE_CARDINALE}`
- Règle HTML comments : conditionnelle (si `{HTML_COMMENTS}` = oui)
- Couche 3.4 : sous-titre HUB depuis `{HUB_SOUS_TITRE}`
- Radar S8 : `{PREFIXE_ENQUETE}8 — Auto-cohérence série`
- Footer : version générique

Environ 85 % du fichier reste inchangé (couches 2, 4, 5, radar, verdict).

## Ordre d'implémentation

1. PROMPT_ARTICLE_MASTER.md — ajout CONFIG, remplacement des placeholders
2. CONTROLEUR_APEX_v2.1.md — ajout CONFIG, remplacement des placeholders
3. Vérifier qu'aucun `{PLACEHOLDER}` ne reste sans valeur par défaut
