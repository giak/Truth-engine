# AUDIT SIMPLIFICATION — De la cathédrale au geste unique
## « Tirer la pelote dans un plat de spaghetti »
## Analyse de l'édifice existant, diagnostic des redondances, proposition de simplification radicale

**Date :** 2026-06-27
**Type :** RAPPORT
**Périmètre :** Tout l'édifice fresque systémique : KERNEL.md + 4 prompts + 16 enquêtes + chroniques

---

## §0 — CE QUE LE SYSTÈME PÈSE AUJOURD'HUI

| Métrique | Valeur |
|----------|--------|
| Fichiers .md dans la fresque | **978** |
| Poids total | **7,2 Mo** |
| Enquêtes produites | **16** (10 fresque + 6 PRED/DNC) |
| Prompts distincts | **4** (KERNEL §0→19, Protocole v2.4, Investigation v2.4, FAIT-MINEUR v1.1, PELOTE-MINEUR v1.0) |
| Couches de format | **3** (YAML 14 chap., AFP 4 colonnes, symboles Ξ€ΛΩΨ...) |
| Fils systémiques | **10** (A-I + L) |
| Mécanismes | **42+** (M01-M48) |
| Événements chroniques | **~6 000** |
| Années couvertes | **237** (1789-2026) |

---

## §1 — LE PROBLÈME : TROP DE COUCHES, PLUS DE GESTE

### 1.1 L'arbre des dépendances

```
KERNEL v2.0 (19 étapes, symboles Ξ€ΛΩΨ...)
  ├── Investigation NREF (14 chapitres YAML)
  │     ├── Protocole v2.4 (10 fils, 42 mécanismes)
  │     ├── Prompt investigation v2.4 (format + Pelote)
  │     ├── Référentiel archéologique (80+ événements historiques)
  │     └── Ultrathinking (6 sections)
  │
  ├── FAIT-MINEUR v1.1 (7 phases, remplir dimensions)
  │     ├── 6 GATES qualité
  │     └── Format AFP 4 colonnes
  │
  ├── PELOTE-MINEUR v1.0 (7 phases, tracer fils causals)
  │     ├── 8 GATES PELOTE
  │     └── Sidecar chaîne causale
  │
  └── Chroniques (20 dimensions × 237 ans, ~6 000 événements)
        └── Injections manuelles dans 65+ fichiers
```

**Diagnostic : 4 couches d'abstraction, 3 formats de sortie différents, 2 protocoles concurrents.**

### 1.2 Les 5 redondances critiques

| Redondance | Manifestation |
|------------|---------------|
| **❶ MÊME MÉCANISME, 3 NOMS** | « Kayfabe » (Substack/KERNEL) = M11 = « mensonge collectif » (protocole). L'utilisateur doit connaître les 3 vocabulaires. |
| **❷ REMONTÉE DES FILS DOUBLONNÉE** | Présente dans : (a) investigation NREF (CH2.5), (b) PELOTE-MINEUR (PHASE 4), (c) référentiel archéologique. Le même travail documenté 3 fois. |
| **❸ PELOTE = ALGORITHME 5 QUESTIONS, MAIS PERSONNE NE L'UTILISE** | L'algorithme Pelote (T-1 → T-2 → T-3 → acte → vérification) est défini mais n'est jamais exécuté en tant que tel dans les sessions. Il a été remplacé par PELOTE-MINEUR qui refait la même chose avec 7 phases. |
| **❹ KERNEL §0 (TEXT ANALYSIS) IGNORÉ DANS LA FRESQUE** | Le KERNEL commence par analyser un texte avec 15 symboles (Ξ€ΛΩΨ...). Mais la fresque enquête sur des ÉVÉNEMENTS, pas des textes. Résultat : les enquêtes fresque sautent §0. |
| **❺ 4 PROMPTS AU LIEU D'1 WORKFLOW** | Un utilisateur qui veut enquêter sur un événement doit choisir entre : KERNEL, Investigation v2.4, FAIT-MINEUR, PELOTE-MINEUR. Aucun ne dit clairement quand utiliser lequel. |

### 1.3 La cause racine : 3 besoins confondus

Tout l'édifice confond **3 besoins distincts** en un seul protocole :

| Besoin | Question | Protocole actuel | Problème |
|--------|----------|-----------------|----------|
| **BESOIN A** | « Tel événement récent — comment en est-on arrivé là ? » | Investigation NREF (14 chap.) | Trop lourd pour 1 événement |
| **BESOIN B** | « Quels faits manquent dans les chroniques ? » | FAIT-MINEUR | Chronophage, basse valeur |
| **BESOIN C** | « Quelle est la chaîne causale de ce fil systémique ? » | PELOTE-MINEUR | Se chevauche avec A |

**La thèse de cet audit : les 3 besoins sont le MÊME geste à 3 niveaux de zoom. Il faut UN protocole avec 3 modes, pas 3 protocoles.**

---

## §2 — CE QUI MARCHE (NE PAS TOUCHER)

### 2.1 Les 10 fils (A-H + I + L)

**✅ À garder.** C'est la découverte fondamentale. Le fait que 16 enquêtes indépendantes confirment que B, C, E sont invariants (100 %) est une preuve solide. Les fils sont le squelette.

### 2.2 L'algorithme Pelote (5 questions récursives)

**✅ À garder et à mettre au centre.** C'est le geste intelligent : T-1 → T-2 → T-3 → acte → vérification. C'est simple, récursif, ça marche. Le vrai problème : personne ne l'exécute parce qu'il est enterré dans 200 lignes de protocole.

### 2.3 Les 16 enquêtes

**✅ À garder comme base de preuves.** La banque de données est solide. Le fait que Mazan (2024) confirme le cadre est une preuve de robustesse.

### 2.4 Les chroniques

**✅ À garder comme base de données factuelle.** 978 fichiers, ~6 000 événements — c'est une matière première précieuse. Mais elle ne DOIT PAS être maintenue manuellement.

### 2.5 Le tableau de bord

**✅ À garder.** La vue d'ensemble est essentielle.

---

## §3 — CE QU'IL FAUT SUPPRIMER OU CONDENSER

### 3.1 Condenser les 4 prompts en 1 workflow avec 3 modes

| Prompt actuel | Sort |
|---------------|------|
| KERNEL §0 (Text Analysis, symboles Ξ€ΛΩΨ) | **Intégrer** dans le workflow comme « mode texte » optionnel |
| Protocole v2.4 (42 M, 14 chapitres) | **Fondre** dans le workflow standard |
| Prompt investigation v2.4 (format YAML) | **Remplacer** par format spaghetti simple |
| FAIT-MINEUR v1.1 | **Intégrer** comme « mode remplissage » du workflow |
| PELOTE-MINEUR v1.0 | **Intégrer** comme « mode pelote » du workflow |

### 3.2 Supprimer les formats redondants

| Format | Problème | Solution |
|--------|----------|----------|
| YAML 14 chapitres | Trop lourd, rarement rempli complètement | **1 format unique** — chaîne causale + preuves + contre-version |
| Symboles Ξ€ΛΩΨ⏰ | Trop abstraits, doublonnent les fils/M## | **Garder uniquement** les glyphes source (✦✧⁅❧) et code impact (✅⚠❌💀) |
| AFP 4 colonnes | Nécessite injection manuelle dans 65 fichiers | **Automatiser** la maintenance des chroniques |

### 3.3 Nest pas toucher à l'architecture existante — juste la simplifier

**Règle : aucun fichier existant n'est supprimé ou modifié. On ajoute UN point d'entrée unique qui réutilise l'existant.**

---

## §4 — LA PROPOSITION : « TIRER LA PELOTE DANS LE PLAT DE SPAGHETTI »

### 4.1 Le geste unique

```
┌─────────────────────────────────────────────────────────────────┐
│                        PLAT DE SPAGHETTI                         │
│                                                                   │
│  INPUT : Un fait/événement récent (actus, tweet, rapport, etc.) │
│                                                                   │
│  QUESTION : « Comment en est-on arrivé là ? »                    │
│                                                                   │
│  MÉTHODE :                                                        │
│    1. IDENTIFIER les 3-5 fils actifs (quels brins de spaghetti   │
│       sont accrochés à cet événement ?)                           │
│                                                                   │
│    2. PELOTE — Pour chaque fil, appliquer l'algorithme 5Q :      │
│       T-1 (0-10 ans) → T-2 (10-50 ans) → T-3 (50+ ans)          │
│       → Acte fondateur → Vérification récursive                   │
│                                                                   │
│    3. TISSER les N chaînes causales en UN récit qui montre       │
│       comment l'événement est le point d'arrivée de 200+ ans      │
│       de verrouillage systémique.                                 │
│                                                                   │
│  OUTPUT : « De AAAA à aujourd'hui — la chaîne qui explique »     │
│           + Preuves + Contre-version                              │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 La métaphore du spaghetti

Imagine un plat de spaghetti : des centaines de brins emmêlés. Chaque brin = un fil causal (B, C, E, G...).

L'événement récent = une fourchette plantée dans le plat. Quand tu tires (pelote), tu ne sors PAS tout le plat d'un coup. Tu sors **les brins spécifiques accrochés à ta fourchette** — et en les suivant, tu découvres à quel point ils sont emmêlés, d'où ils viennent, où ils commencent.

**« Tirer la pelote dans un plat de spaghetti »** = prendre un événement, tirer les 3-5 fils qui y sont accrochés, et révéler le système entier par ce geste unique.

### 4.3 Les 3 modes du workflow

```
MODE 1 — PELOTE (rapide, < 30 min)
  Usage : actu, tweet, événement quotidien
  Sortie : chaîne causale + preuves minimales
  Format : 1 page max

MODE 2 — ENQUÊTE (approfondi, 1-3 h)
  Usage : scandale, crise, événement majeur
  Sortie : chaîne causale + preuves + contre-version + contre-mesures
  Format : investigation complète (CH2-CH12)

MODE 3 — CHRONIQUE (maintenance, 15-45 min)
  Usage : remplir les trous temporels des chroniques
  Sortie : N lignes dans fichiers AFP
  Format : maintenance base de données
```

---

## §5 — LA RECOMMANDATION POUR KERNEL.md

Le KERNEL.md actuel a un **mode par défaut** qui est le TEXT ANALYSIS (§0) — conçu pour analyser un article/text. Mais 100 % des sessions récentes sont passées par la fresque (événements, pas textes).

**Proposition : ajouter dans KERNEL.md un §0 bis — « MODE PELOTE » — avec le détecteur suivant :**

```
══════════════════════════════════════
MODE PELOTE (détection automatique)
══════════════════════════════════════

SI input = événement/actualité (pas un texte à analyser) :
  → BASULER en MODE PELOTE
  → SKIP §0 TEXT ANALYSIS
  → SKIP symboles Ξ€ΛΩΨ...
  → SKIP clusters
  → ALLER directement à :
     1. Quel fil(s) cet événement active-t-il ?
     2. Algorithme Pelote 5Q pour chaque fil
     3. OUTPUT : chaîne causale « De 1789 à aujourd'hui »

DÉTECTION :
  Input starts with http             → MODE FETCH → MODE PELOTE
  Input = « comment en est-on arrivé là ? »     → MODE PELOTE
  Input = événement/fait/scandale   → MODE PELOTE
  Input contient 3+ dates différentes → MODE PELOTE
  Input = texte/article/poste/réseau → MODE TEXTE (§0 normal)
```

**Cette section peut tenir en 30 lignes et dispense de charger FAIT-MINEUR, PELOTE-MINEUR et Investigation séparément.**

---

## §6 — L'ESSENTIEL DE LA RECOMMANDATION

### En une phrase

> Un seul workflow avec 3 modes (PELOTE / ENQUÊTE / CHRONIQUE), une seule méthode (Pelote 5Q), un seul format de sortie (chaîne causale + preuves), et un point d'entrée unique dans KERNEL.md.

### Ce qui ne change pas

- Les **10 fils** (A-H + I + L) — gardés
- Les **42 mécanismes** (M01-M48) — gardés comme vocabulaire
- Les **16 enquêtes** — gardées comme base de preuves
- Les **chroniques** — gardées comme base de données
- Le **tableau de bord** — gardé comme vue d'ensemble

### Ce qui change

- **4 prompts → 1 workflow** avec 3 modes
- **3 formats → 1 format** (chaîne causale + preuves)
- **2 algorithmes Pelote → 1 algorithme** (5Q récursives)
- **Maintenance manuelle des chroniques → semi-automatisée**
- **KERNEL.md : ajout §0 bis MODE PELOTE** (30 lignes)

### Le geste utilisateur final

```
> « Macron limoge un général. Comment en est-on arrivé là ? »
→ [Identification automatique : Fil B Monopole d'État, Fil D Justice domestiquée]
→ [Pelote 5Q : T-1 (loi programmation militaire 2023) → T-2 (LPM 2014-2019) 
   → T-3 (Réforme armée 1996) → Acte (Constitution 1958 art.15)]
→ [OUTPUT : « De 1958 à 2026 — la chaîne du contrôle présidentiel sur l'armée »]

> « DNC — blindés Centaure contre agriculteurs. Comment en est-on arrivé là ? »
→ [Identification automatique : Fil B Monopole, Fil H Exceptionnalisme, Fil C Sté civile]
→ [Pelote 5Q : ...]
→ [OUTPUT : « De 1791 à 2025 — la chaîne du monopole agricole »]
```

---

## §7 — PROCHAINES ÉTAPES RECOMMANDÉES

| Étape | Action | Effet |
|-------|--------|-------|
| **1** | Ajouter §0 bis MODE PELOTE dans KERNEL.md (30 lignes) | Point d'entrée unique |
| **2** | Fabriquer 1 prompt unique avec 3 modes (PELOTE/ENQUÊTE/CHRONIQUE) | Remplacer les 4 prompts |
| **3** | Tester le MODE PELOTE sur un événement réel (ex : DNC) | Valider la simplicité |
| **4** | Automatiser l'injection chroniques (script au lieu d'écriture manuelle) | Maintenance allégée |
| **5** | Archiver les prompts v1 comme obsolètes dans `archive/` | Propreté du repo |

---

*Audit produit le 2026-06-27. 978 fichiers, 7,2 Mo, 16 enquêtes, 4 prompts → le geste unique est possible.*
