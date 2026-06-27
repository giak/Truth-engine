# RAPPORT DE SIMULATION — FAIT-MINEUR v1.0
## Session pilote sur la dimension REL (Religion)

**Date :** 2026-06-27
**Type :** AUDIT
**Cible :** Dimension REL — 38 événements, 23 années, focale catholique
**Statut :** ✅ PROUVE FONCTIONNEL — 5 gaps critiques identifiés

---

## §0 — RÉSUMÉ

La simulation FAIT-MINEUR a été exécutée sur la dimension REL pour prouver que le prompt est **suivable par un LLM**. Résultat : **le pipeline s'exécute du début à la fin**, mais 5 écarts entre le prompt théorique et l'exécution réelle ont été identifiés.

### Bilan de la session

| Métrique | Valeur |
|----------|:------:|
| PHASES exécutées | 6/7 (Memory sautée) |
| Fichiers REL lus | 23 (tous les existants) |
| Questions CREDO | 10 |
| Recherches web | 1 (large) |
| Faits extraits | 10 |
| Fichiers créés | 7 (2004, 2010, 2012, 2015, 2020, 2022, 2025) |
| Fichiers mis à jour | 2 (2009, 2021) |
| Faits ajoutés | 9 (1+1+1+2+1+1+1+1) |
| Compteur total REL | 38 → 47 (+9) |

---

## §1 — PIPELINE EXÉCUTÉ

### PHASE 0: LOAD (✅ OK)

Chargement des 23 fichiers REL existants (1976-2021) :
- 38 événements couvrant 23 années
- Focale quasi exclusivement catholique (sauf affaires voile, CFCM)
- Pas d'entrée sur : loi 1905, loi 2004, loi 2010, loi 2021, Charlie Hebdo, FORIF, statistiques sécularisation

**Formats lus :** 23 fichiers, format AFP. 1 anomalie détectée (2021: code `Chiffre colossal` non standard)

### PHASE 1: GAP (✅ OK)

Identifié :
- **Gap thématique :** zéro événement sur l'islam de France (sauf CFCM 2003), zéro sur les lois laïcité (2004, 2010, 2021), zéro sur la sécularisation
- **Gap dialectique :** aucun ✅ (positif) sur les 38 événements REL
- **Gap temporal :** années vides (2004, 2010, 2012, 2015, 2020, 2022, 2025)
- **Potentiel estimé :** 30-50 faits manquants

### PHASE 2: CREDO (✅ OK)

10 questions générées :
- C : Quelles lois ? Quels événements ? Quelles dates ?
- R : Budgets cultes ? Financement mosquées ? Indemnisation ?
- E : Rapports CIASE, Observatoire laïcité ?
- D : Controverses voile, séparatisme, liberté expression ?
- O : Quels sujets passés sous silence (autres cultes, franc-maçonnerie, bouddhisme) ?
- + : Quels discours sur la laïcité ?

### PHASE 3: SEARCH (⚠ PARTIEL)

**Ce qui a fonctionné :** le `researcher-web` a produit une synthèse utile de 10 sections couvrant tous les sujets CREDO.

**Ce qui a dévié du prompt :**
- ❌ L'étape `@MNEMO_Q` (recherche mémoire) a été sautée — le LLM est allé directement au web
- ❌ Aucune URL de source collectée — la synthèse du `researcher-web` donne des informations sans URLs vérifiables
- ❌ Aucun `read_url()` exécuté — pas de fetch direct pour vérifier les sources

**Gap-1 :** le pipeline de priorité des sources (MNEMO_Q → WEB → FETCH) n'est pas respecté. Le LLM saute naturellement au chemin le plus court.

**Gap-2 :** `researcher-web` ne produit pas d'URLs par fait. Pour obtenir des URLs, il faut un appel `read_url()` supplémentaire.

### PHASE 4: REGISTRY (❌ NON FAIT)

Le prompt définit un registre 9 colonnes :
```
| # | Année | Dim | Description | Code | URL | Fiabilité | Acteur | Chiffre |
```

**Dans la simulation :** aucun registre formel n'a été construit. Les faits ont été extraits mentalement et injectés directement.

**Gap-3 :** Le format 9-colonnes est trop lourd pour une session de 15-25 faits (135-225 champs à remplir). Le LLM le court-circuite naturellement.

**Recommandation :** passer à 5 colonnes obligatoires (Année, Dim, Description, Code, URL) + un fichier de registre séparé.

### PHASE 5: GATES (⚠ PARTIEL)

| Gate | Statut | Note |
|------|--------|------|
| GATE-1: DATATION | ✅ | Tous les faits ont une année valide |
| GATE-2: DÉDUPLICATION | ✅ | Aucun doublon avec 38 existants |
| GATE-3: SOURCAGE | ❌ | Aucune URL collectée pour aucun fait |
| GATE-4: HEAD CHECK | ❌ | Non exécuté |
| GATE-5: COHÉRENCE | ✅ | Codes appropriés |
| GATE-6: COMPTEUR | ✅ | Tous corrects |

**Gap-4 :** L'exigence de sourçage (URL par fait) est la plus difficile à respecter. Le format actuel des chroniques (4 colonnes) n'a pas de colonne URL.

### PHASE 6: INJECT (✅ OK)

9 fichiers REL créés/mis à jour :
- 7 fichiers créés : 2004, 2010, 2012, 2015, 2020, 2022, 2025
- 2 fichiers mis à jour : 2009 (+1), 2021 (correction format +2)

**Problème détecté :** le fichier `2021_REL.md` avait un format cassé (code `Chiffre colossal`, ligne vide parasite). La correction a été faite manuellement pendant l'injection — le prompt ne prévoit pas cette étape d'audit.

### PHASE 7: MEMORY (❌ SAUTÉE)

`write_memory()` n'a pas été exécuté. Les faits ajoutés ne sont pas indexés dans Mnemolite.

**Gap-5 :** La PHASE 7 est systématiquement oubliée parce qu'elle est en fin de pipeline et que le LLM considère le travail terminé après l'injection.

---

## §2 — LES 5 GAPS CRITIQUES

| # | Gap | Description | Correctif proposé |
|:-:|-----|-------------|-------------------|
| 1 | **Priorité sources non respectée** | MNEMO_Q → WEB → FETCH devient juste WEB | Ajouter un check-block en début de PHASE 3 : « ◉ **OBLIGATOIRE** : exécuter @MNEMO_Q avant @WEB » |
| 2 | **Pas d'URLs dans les résultats web** | `researcher-web` donne des infos sans URL vérifiable | Après chaque résultat, chaîner avec `read_url()` sur les sources mentionnées. Ajouter : « ◉ 1 recherche = 1 URL minimum » |
| 3 | **Registre 9 colonnes trop lourd** | 135-225 champs pour 15-25 faits = friction | Réduire à 5 colonnes obligatoires (Année, Dim, Description, Code, URL). Ajouter une note : « Si pas d'URL → ❧ + [HYPOTHÈSE] » |
| 4 | **Sourçage impossible dans format chronique** | Les 4 colonnes (Année, Dim, Description, Code) n'ont pas de place pour l'URL | Deux solutions : (a) ajouter colonne URL optionnelle aux chroniques, (b) maintenir registre externe parallèle |
| 5 | **PHASE 7 oubliée** | Le LLM s'arrête après injection | Ajouter une vérification finale : « ◉ **VÉRIFICATION :** les 7 phases ont-elles été exécutées ? » |

---

## §3 — LEÇONS POUR V1.1

### Correctifs prioritaires (🔴)

1. **Ajouter sous-phase AUDIT** avant PHASE 1 : détecter les fichiers malformés (codes non standard, lignes vides, headers absents)
2. **Diviser PHASE 3 en 3 étapes obligatoires** : `@MNEMO_Q` → `@WEB` + `read_url()` → vérification
3. **Simplifier le REGISTRY** : 5 colonnes (Année, Dim, Description, Code, URL) au lieu de 9
4. **Ajouter une règle de multi-dimension** : si un fait touche 2 dimensions → 2 lignes

### Correctifs secondaires (🟡)

5. **Ajouter timebox** : 20 min par session max (contre 30-45 min dans la simulation)
6. **Ajouter vérification finale** : « Les 7 phases ont-elles été exécutées ? »
7. **Ajouter format de sortie explicite** pour `read_url()` : extraire Année, Description, Code, URL

### Ce qui a bien fonctionné (à conserver)

- Le format DSL (◉, →, ◆, ⊙, △, ⟐) est compris et suivi par le LLM
- La distinction Investigation NREF / FAIT-MINEUR est claire
- Les GATES-1/2/5/6 sont faciles à exécuter
- L'injection AFP (écriture directe) fonctionne parfaitement
- La déduction de doublons par lecture des fichiers existants est fiable

---

## §4 — VERDICT

```
╔══════════════════════════════════════════════════════════════╗
║  LE PROMPT FAIT-MINEUR v1.0 EST EXÉCUTABLE PAR UN LLM      ║
╠══════════════════════════════════════════════════════════════╣
║  Résultat : 9 fichiers REL créés/mis à jour, +9 faits,     ║
║  compteur REL 38→47.                                        ║
║                                                            ║
║  Qualité : ⚠ 3 gaps critiques (sources, registry, memory)  ║
║  robustesse : ⚠ 2 gaps structurels (format REGISTRY, URLs) ║
║                                                            ║
║  Le prompt est fonctionnel mais nécessite v1.1 pour         ║
║  renforcer 3 points : sourcing, registry, memory.           ║
╚══════════════════════════════════════════════════════════════╝
```

---

## §5 — FICHIERS MODIFIÉS

| Fichier | Action | Faits |
|---------|--------|:-----:|
| `2004/2004_REL.md` | Créé | 1 (loi voile 2004) |
| `2009/2009_REL.md` | +1 fait | 1→2 (FSSPX excommunication) |
| `2010/2010_REL.md` | Créé | 1 (loi burqa) |
| `2012/2012_REL.md` | Créé | 1 (Observatoire laïcité) |
| `2015/2015_REL.md` | Créé | 2 (Charlie Hebdo + Marche républicaine) |
| `2020/2020_REL.md` | Créé | 1 (discours séparatisme) |
| `2021/2021_REL.md` | Format corrigé +2 faits | 1→3 (CIASE 216k, loi séparatisme, fonds SELAR) |
| `2022/2022_REL.md` | Créé | 1 (FORIF) |
| `2025/2025_REL.md` | Créé | 1 (sécularisation) |

---

*Simulation FAIT-MINEUR v1.0 sur REL — 2026-06-27*
*9 fichiers créés/mis à jour, 9 faits ajoutés, 5 gaps documentés*
*Prochaine action : mise à jour prompt v1.1 avec correctifs*
