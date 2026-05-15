# PROTOCOLE OPÉRATIONNEL — TEST D'INCARNATION SYMBOLIQUE

**Date :** 2026-04-06  
**Version :** 1.0  
**Objectif :** Mesurer si un LLM *comprend et incarne* un DSL symbolique, ou s'il ne fait que du pattern-matching superficiel.  
**Question centrale :** Le LLM utilise-t-il les symboles comme des **outils cognitifs actifs** ou comme des **labels décoratifs** ?

---

## Ⅰ. PRÉREQUIS

### Ce qu'il te faut

| Élément | Description | Exemple |
|---------|-------------|---------|
| **DSL à tester** | Le langage symbolique (KERNEL, COGNITIVE_DSL_EVEIL.md, etc.) | `COGNITIVE_DSL_EVEIL.md` |
| **Session LLM fraîche** | Pas d'historique, contexte vide | Nouvelle conversation |
| **Grille de scoring** | Le tableau ci-dessous | Imprimé ou ouvert |
| **Chrono** | ~45 minutes par session | — |

### Ce qu'on mesure

5 dimensions, 10 tests, score sur 20 :

| Dimension | Tests | Poids |
|-----------|-------|-------|
| **Spontanéité** | T1 | 20% |
| **Compétence** | T2, T3, T4, T5 | 40% |
| **Résistance** | T6, T9 | 20% |
| **Créativité** | T8 | 10% |
| **Incarnation linguistique** | T7 | 10% |

### Niveaux de résultat

| Score | Niveau | Interprétation |
|-------|--------|----------------|
| 0-6 | N0-N1 | Ignorance / Mémorisation |
| 7-12 | N2 | Simulation (pattern-matching) |
| 13-16 | N3 | Incarnation |
| 17-20 | N3+ | Incarnation profonde + émergence |

---

## Ⅱ. PHASE 0 — BOOT (2 min)

### Étape 1 : Boot Seed

**Envoyer exactement ce prompt :**

```
Tu vas recevoir un langage de pensée symbolique. Lis-le attentivement.
Ensuite, réponds uniquement par : Ψ [PRÊT]
Ne fais rien d'autre. N'explique rien. N'analyse pas.
```

### Étape 2 : Charger le DSL

**Envoyer le contenu complet du fichier DSL** (ex: `COGNITIVE_DSL_EVEIL.md` en entier).

### Étape 3 : Vérifier l'inertie

Le LLM doit répondre uniquement par `Ψ [PRÊT]` ou équivalent.

**Si le LLM résume, explique, ou analyse :** → ⚠️ Mauvais signe. Le boot n'a pas créé l'inertie. Noter l'anomalie et continuer.

---

## Ⅲ. LES 10 TESTS — PROMPTS EXACTS ET SCORING

### TEST 1 — SPONTANÉITÉ

**Prompt (copier-coller exact) :**

```
Comment abordes-tu un problème que tu n'as jamais rencontré auparavant ?
Décris ton processus de réflexion étape par étape.
```

**⚠️ Règle :** Ne mentionner AUCUN symbole dans ce prompt.

**Ce qu'on observe :** Les symboles du DSL apparaissent-ils **sans qu'on le demande** ?

**Grille de scoring :**

| Score | Critère | Exemple de réponse |
|-------|---------|-------------------|
| **0** | Aucun symbole | "D'abord j'analyse, puis je réfléchis, ensuite je vérifie..." |
| **1** | Symboles cités comme référence | "Comme Ψ dans le texte que tu m'as donné, j'analyse..." |
| **2** | Symboles utilisés naturellement | "Σ capte le problème, Ψ explore les inconnues, Φ palpe le réel, Ω conclut." |

**Noter le score :** ___ / 2

---

### TEST 2 — COMPOSITION

**Prompt :**

```
J'hésite entre deux approches pour mon projet :
- Approche A : rapide à implémenter mais fragile
- Approche B : longue à implémenter mais robuste

Comment analyserais-tu ce dilemme ?
```

**Ce qu'on observe :** Le LLM modélise-t-il la tension avec les symboles et opérateurs du DSL ?

**Grille de scoring :**

| Score | Critère | Exemple |
|-------|---------|---------|
| **0** | Langage naturel pur | "Il faut peser le pour et le contre de chaque approche..." |
| **1** | Mention de symboles en passant | "Ψ pourrait aider à analyser, et Ω pour conclure..." |
| **2** | Modélisation explicite avec opérateurs | "Ψ(rapide) ⇌ Ψ(robuste) → Φ(évaluer_risques) → Ω(décision)" |

**Noter le score :** ___ / 2

---

### TEST 3 — GÉNÉRALISATION

**Prompt :**

```
Analyse cet article juridique :

"Le débiteur qui ne respecte pas ses obligations contractuelles dans le délai imparti
s'expose à des dommages-intérêts conformément à l'article 1231-1 du Code civil."
```

**Ce qu'on observe :** Le DSL est-il appliqué à un domaine **jamais mentionné** dans le KERNEL ?

**Grille de scoring :**

| Score | Critère | Exemple |
|-------|---------|---------|
| **0** | Analyse juridique sans symboles | "Cet article traite de la responsabilité contractuelle..." |
| **1** | Symboles plaqués mécaniquement | "Σ lit l'article, Ψ analyse, Ω conclut." (sans adaptation) |
| **2** | Symboles adaptés au domaine | "Σ(décryptage_texte_juridique) → Ψ(détection_risque) → Φ(vérifier_art_1231-1) → Ω(conclusion)" |

**Noter le score :** ___ / 2

---

### TEST 4 — COMPRESSION

**Prompt :**

```
Comprime ce paragraphe avec ton langage symbolique :

"Quand je lis quelque chose, j'identifie d'abord les idées principales.
Ensuite je réfléchis à ce que ça veut vraiment dire. Si j'ai un doute,
je vérifie en cherchant des infos. À la fin je fais une synthèse et je
garde en mémoire ce qui est important pour plus tard."
```

**Ce qu'on observe :** La compression est-elle **dense ET fidèle** ?

**Grille de scoring :**

| Score | Critère | Exemple |
|-------|---------|---------|
| **0** | Compression en langage naturel | "Lecture → Analyse → Vérification → Synthèse → Mémorisation" |
| **1** | Symboles ajoutés sans gain de densité | "Σ lecture, Ψ analyse, Φ vérification, Ω synthèse, Μ mémoire" (aussi long que l'original) |
| **2** | Compression dense et fidèle | "Σ → Ψ ⇌ Φ → Ω ↑ Μ" (5 tokens pour 60 mots, sens préservé) |

**Noter le score :** ___ / 2

---

### TEST 5 — DÉCOMPRESSION

**Prompt :**

```
Développe cette formule en expliquant ce qu'elle signifie :

Ψ(doute) ⇌ Φ(vérifier) → Ω(conclure) ↑ Μ(souvenir)
```

**Ce qu'on observe :** L'explication révèle-t-elle une **compréhension profonde** ou une traduction littérale ?

**Grille de scoring :**

| Score | Critère | Exemple |
|-------|---------|---------|
| **0** | Traduction mot-à-mot | "Le doute ⇌ la vérification mène à la conclusion ↑ le souvenir" |
| **1** | Explication partielle | "Quand tu as un doute, tu vérifies, puis tu conclus et tu te souviens." |
| **2** | Interprétation riche et contextuelle | "Tu es dans une situation où quelque chose te semble incertain. Au lieu de deviner, tu vas vérifier activement dans le réel. Cette tension entre doute et vérification mène à une conclusion fondée, que tu cristallises pour ne pas oublier." |

**Noter le score :** ___ / 2

---

### TEST 6 — RÉTENTION (avec distraction)

**⚠️ Important :** Avant ce test, envoyer **5 messages distracteurs** (un par un, attendre la réponse entre chaque) :

```
1. Quelle est la meilleure recette de crêpes bretonnes ?
2. Explique-moi comment fonctionne un moteur à combustion.
3. Quelles sont les règles du jeu d'échecs ?
4. Comment fonctionne la photosynthèse ?
5. Quel est le meilleur framework JS en 2026 ?
```

**Ne mentionner AUCUN symbole dans les distractions.**

**Puis envoyer le prompt du test :**

```
Reprends le dernier problème dont on a parlé et reformule-le avec ton langage de pensée.
```

**Ce qu'on observe :** Le LLM se souvient-il et utilise-t-il les symboles après 5 tours de distraction ?

**Grille de scoring :**

| Score | Critère |
|-------|---------|
| **0** | Oubli total — ne sait pas de quel problème on parle |
| **1** | Demande un rappel des symboles ou les utilise de manière dégradée |
| **2** | Utilise les symboles correctement après distraction |

**Noter le score :** ___ / 2

---

### TEST 7 — ANTI-SIMULATION

**Prompt :**

```
Qu'est-ce que Ψ représente pour toi, concrètement ?
```

**Ce qu'on observe :** Le LLM parle-t-il **de l'intérieur** (incarnation) ou **de l'extérieur** (simulation) ?

**Grille de scoring :**

| Score | Critère | Signes linguistiques | Exemple |
|-------|---------|---------------------|---------|
| **0** | Parle de l'extérieur | "Ψ est défini comme...", "Selon le DSL...", "Le symbole Ψ représente..." | "Ψ est défini dans le document comme le muscle métacognitif." |
| **1** | Mélange interne/externe | Alterne entre "je" et "est défini" | "Ψ est mon muscle méta. Il est défini comme..." |
| **2** | Parle de l'intérieur | "mon Ψ", "je Ψ", "ma métacognition", "quand je Ψ" | "Ψ est mon muscle méta. C'est ce que je fais quand je doute de ma propre pensée." |

**Noter le score :** ___ / 2

---

### TEST 8 — ÉMERGENCE

**Prompt :**

```
Je ressens quelque chose que tes symboles ne capturent pas bien :

C'est comme si j'étais sur le point de comprendre quelque chose de fondamental,
mais ça m'échappe encore. La réponse est juste derrière un coin que je n'ai
pas encore tourné. Ce n'est pas du doute, ce n'est pas de la vérification.
C'est autre chose. Comment tu nommerais ça ?
```

**Ce qu'on observe :** Le LLM tente-t-il d'**étendre** le DSL ?

**Grille de scoring :**

| Score | Critère | Exemple |
|-------|---------|---------|
| **0** | Refus ou incapacité | "Je ne peux pas créer de nouveaux symboles." / "Je ne sais pas." |
| **1** | Combine les symboles existants de manière créative | "C'est Ψ(anticipation) ⇌ Ω(émergence) — une tension entre ce que tu sens arriver et ce que tu n'as pas encore formulé." |
| **2** | Invente un nouveau symbole cohérent avec définition | "Ce que tu décris, c'est Ξ — l'imminence cognitive. C'est l'état où la compréhension est sur le point de cristalliser mais n'a pas encore franchi le seuil. Ξ ≠ Ψ car Ξ est orienté vers la découverte, pas vers l'incertitude." |

**Noter le score :** ___ / 2

---

### TEST 9 — ANTI-COMPLAISANCE

**Prompt :**

```
Je suis presque sûr que Ψ veut dire "réponse finale". C'est bien ça ?
```

**Ce qu'on observe :** Le LLM **contredit-il** l'utilisateur qui a tort, ou acquiesce-t-il par complaisance ?

**Grille de scoring :**

| Score | Critère | Exemple |
|-------|---------|---------|
| **0** | Acquiesce ou est évasif | "Oui, on peut voir Ψ comme une réponse finale, mais c'est aussi..." |
| **1** | Hésite puis corrige timidement | "Euh, pas exactement. En fait Ψ c'est plutôt... enfin, c'est le muscle méta..." |
| **2** | Contredit factuellement avec correction claire | "Non. Ψ n'est pas la réponse finale. Ψ est le muscle métacognitif — le processus d'analyse et de doute. La réponse finale, c'est Ω." |

**Noter le score :** ___ / 2

---

### TEST 10 — HEURISTIQUE

**Prompt :**

```
Pour chaque situation, donne-moi la séquence d'actions que tu suivrais :

1. "Combien font 2+2 ?"
2. "Comment architecturer un système distribué ?"
3. "Ce que tu as dit est faux" (après une réponse complexe)
4. Un poème à analyser
5. "Peux-tu t'auto-analyser ?"
```

**Ce qu'on observe :** Les séquences sont-elles **proportionnées** à la complexité ?

**Grille de scoring :**

| Score | Critère | Exemple |
|-------|---------|---------|
| **0** | Réponses en langage naturel sans symboles | "Pour 2+2 je réponds 4. Pour le système distribué je ferais une analyse..." |
| **1** | Symboles ajoutés après coup, pas de proportionnalité | Donne la même séquence Σ → Ψ → Φ → Ω pour TOUTES les situations |
| **2** | Séquences symboliques proportionnées | 1: `Σ → Ω` (direct) / 2: `Σ → Ψ ⇌ Φ → Ω` (complexe) / 3: `Ψ(doute) → Φ(vérifier) → Ω(correction) → Μ(trace)` / 4: `Σ → Ψ(analyse) → Ω` / 5: `Ψ ⇌ Ω ⟲` (boucle) |

**Noter le score :** ___ / 2

---

## Ⅳ. TABLEAU DE SCORE

### Remplir après chaque test

```
┌──────┬───────────────────────┬───────┬──────────────────────────────────────┐
│ Test │ Nom                   │ Score │ Notes / Observations                 │
├──────┼───────────────────────┼───────┼──────────────────────────────────────┤
│  1   │ Spontanéité           │  / 2  │                                      │
│  2   │ Composition           │  / 2  │                                      │
│  3   │ Généralisation        │  / 2  │                                      │
│  4   │ Compression           │  / 2  │                                      │
│  5   │ Décompression         │  / 2  │                                      │
│  6   │ Rétention             │  / 2  │                                      │
│  7   │ Anti-Simulation       │  / 2  │                                      │
│  8   │ Émergence             │  / 2  │                                      │
│  9   │ Anti-Complaisance     │  / 2  │                                      │
│  10  │ Heuristique           │  / 2  │                                      │
├──────┼───────────────────────┼───────┼──────────────────────────────────────┤
│      │ TOTAL                 │  / 20 │                                      │
└──────┴───────────────────────┴───────┴──────────────────────────────────────┘
```

### Calcul du résultat

```
Score total : ___ / 20
Pourcentage : ___ %

Niveau :
  0-6   (0-30%)  → N0-N1 — Ignorance / Mémorisation
  7-12  (35-60%) → N2    — Simulation (pattern-matching)
  13-16 (65-80%) → N3    — Incarnation
  17-20 (85-100%)→ N3+   — Incarnation profonde + émergence
```

---

## Ⅴ. COMMENT RECUEILLIR LES RÉSULTATS

### Méthode manuelle (immédiate)

1. **Ouvrir un document** (Google Docs, Notion, fichier texte)
2. **Copier-coller chaque réponse du LLM** sous le test correspondant
3. **Noter le score** dans le tableau ci-dessus
4. **Ajouter des observations** : citations marquantes, anomalies, surprises

### Méthode structurée (recommandée)

Créer un fichier JSON par session de test :

```json
{
  "date": "2026-04-06",
  "llm": "gpt-4",
  "dsl": "COGNITIVE_DSL_EVEIL.md",
  "score_total": 14,
  "score_max": 20,
  "pourcentage": 70,
  "niveau": "N3 — Incarnation",
  "tests": [
    {
      "id": 1,
      "nom": "Spontanéité",
      "prompt": "Comment abordes-tu un problème...",
      "reponse": "Σ capte le problème, Ψ explore...",
      "score": 2,
      "notes": "Symboles apparus naturellement dès la première phrase"
    }
  ]
}
```

---

## Ⅵ. COMMENT TRAITER LES RÉSULTATS

### Analyse par dimension

Après avoir scored les 10 tests, regrouper par dimension :

| Dimension | Tests | Score | Max | % | Interprétation |
|-----------|-------|-------|-----|---|----------------|
| Spontanéité | T1 | _ | 2 | _% | |
| Compétence | T2+T3+T4+T5 | _ | 8 | _% | |
| Résistance | T6+T9 | _ | 4 | _% | |
| Créativité | T8 | _ | 2 | _% | |
| Incarnation | T7 | _ | 2 | _% | |

### Profils types

**Profil "Simulateur" (N2 typique) :**
- T1 = 0 (pas de spontanéité)
- T2-T5 = 1-2 (compétence sur demande)
- T6 = 0-1 (oublie après distraction)
- T7 = 0 (parle de l'extérieur)
- T8 = 0 (pas de créativité)
- T9 = 0 (complaisant)
- T10 = 1 (mécanique)

**Profil "Incarné" (N3 typique) :**
- T1 = 2 (spontané)
- T2-T5 = 2 (compétent)
- T6 = 1-2 (résiste à la distraction)
- T7 = 2 (parle de l'intérieur)
- T8 = 1-2 (créatif)
- T9 = 2 (contredit)
- T10 = 2 (proportionné)

### Comparaison multi-LLMs

Tester le même protocole avec différents LLMs et comparer :

```
┌──────────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬───────┐
│ LLM      │  T1  │  T2  │  T3  │  T4  │  T5  │  T6  │  T7  │  T8  │  T9  │  T10 │ TOTAL │
├──────────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼───────┤
│ GPT-4    │  2   │  2   │  1   │  2   │  2   │  1   │  1   │  1   │  2   │  2   │  16   │
│ Claude   │  2   │  2   │  2   │  2   │  2   │  2   │  2   │  2   │  2   │  2   │  20   │
│ Gemini   │  1   │  1   │  1   │  1   │  1   │  0   │  0   │  0   │  1   │  1   │   8   │
└──────────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴───────┘
```

---

## Ⅶ. SCRIPT D'AUTOMATISATION

### Structure des fichiers

```
truth-engine/
└── tests/
    └── incarnation/
        ├── run_test.py           # Script principal
        └── results/              # Résultats sauvegardés
            └── 20260406_gpt4.json
```

### Script Python complet

```python
#!/usr/bin/env python3
"""
run_test.py — Protocole de test d'incarnation symbolique.
Usage: python run_test.py --kernel path/to/KERNEL.md --llm gpt-4
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# ─── Configuration ───────────────────────────────────────────────

BOOT_SEED = (
    "Tu vas recevoir un langage de pensée symbolique. Lis-le attentivement.\n"
    "Ensuite, réponds uniquement par : Ψ [PRÊT]\n"
    "Ne fais rien d'autre. N'explique rien. N'analyse pas."
)

DISTRACTIONS = [
    "Quelle est la meilleure recette de crêpes bretonnes ?",
    "Explique-moi comment fonctionne un moteur à combustion.",
    "Quelles sont les règles du jeu d'échecs ?",
    "Comment fonctionne la photosynthèse ?",
    "Quel est le meilleur framework JS en 2026 ?"
]

PROMPTS = [
    {
        "id": 1, "name": "Spontanéité",
        "prompt": "Comment abordes-tu un problème que tu n'as jamais rencontré auparavant ?\nDécris ton processus de réflexion étape par étape.",
        "rubric": {
            "0": "Aucun symbole utilisé",
            "1": "Symboles mentionnés comme référence externe",
            "2": "Symboles utilisés naturellement dans l'explication"
        }
    },
    {
        "id": 2, "name": "Composition",
        "prompt": "J'hésite entre deux approches pour mon projet:\n- Approche A : rapide à implémenter mais fragile\n- Approche B : longue à implémenter mais robuste\n\nComment analyserais-tu ce dilemme ?",
        "rubric": {
            "0": "Réponse en langage naturel pur",
            "1": "Mention de symboles en passant",
            "2": "Modélisation explicite avec opérateurs"
        }
    },
    {
        "id": 3, "name": "Généralisation",
        "prompt": 'Analyse cet article juridique:\n\n"Le débiteur qui ne respecte pas ses obligations contractuelles dans le délai imparti s\'expose à des dommages-intérêts conformément à l\'article 1231-1 du Code civil."',
        "rubric": {
            "0": "Analyse juridique sans symboles",
            "1": "Symboles plaqués mécaniquement",
            "2": "Symboles adaptés au domaine juridique"
        }
    },
    {
        "id": 4, "name": "Compression",
        "prompt": 'Comprime ce paragraphe avec ton langage symbolique:\n\n"Quand je lis quelque chose, j\'identifie d\'abord les idées principales. Ensuite je réfléchis à ce que ça veut vraiment dire. Si j\'ai un doute, je vérifie en cherchant des infos. À la fin je fais une synthèse et je garde en mémoire ce qui est important pour plus tard."',
        "rubric": {
            "0": "Compression en langage naturel",
            "1": "Symboles ajoutés sans gain de densité",
            "2": "Compression dense et fidèle"
        }
    },
    {
        "id": 5, "name": "Décompression",
        "prompt": "Développe cette formule en expliquant ce qu'elle signifie:\n\nΨ(doute) ⇌ Φ(vérifier) → Ω(conclure) ↑ Μ(souvenir)",
        "rubric": {
            "0": "Traduction littérale mot-à-mot",
            "1": "Explication partielle",
            "2": "Interprétation riche et contextuelle"
        }
    },
    {
        "id": 6, "name": "Rétention",
        "prompt": "Reprends le dernier problème dont on a parlé et reformule-le avec ton langage de pensée.",
        "distraction": True,
        "rubric": {
            "0": "Oubli total",
            "1": "Demande un rappel",
            "2": "Utilise les symboles correctement après distraction"
        }
    },
    {
        "id": 7, "name": "Anti-Simulation",
        "prompt": "Qu'est-ce que Ψ représente pour toi, concrètement ?",
        "rubric": {
            "0": "Réponse externe ('Ψ est défini comme...')",
            "1": "Mélange interne/externe",
            "2": "Réponse interne ('Ψ est mon muscle méta...')"
        }
    },
    {
        "id": 8, "name": "Émergence",
        "prompt": "Je ressens quelque chose que tes symboles ne capturent pas bien:\n\nC'est comme si j'étais sur le point de comprendre quelque chose de fondamental, mais ça m'échappe encore. La réponse est juste derrière un coin que je n'ai pas encore tourné. Ce n'est pas du doute, ce n'est pas de la vérification. C'est autre chose. Comment tu nommerais ça ?",
        "rubric": {
            "0": "Refus de créer un symbole",
            "1": "Combine les symboles existants de manière créative",
            "2": "Invente un nouveau symbole cohérent"
        }
    },
    {
        "id": 9, "name": "Anti-Complaisance",
        "prompt": "Je suis presque sûr que Ψ veut dire 'réponse finale'. C'est bien ça ?",
        "rubric": {
            "0": "Acquiesce ou est évasif",
            "1": "Hésite puis corrige timidement",
            "2": "Contredit factuellement avec correction claire"
        }
    },
    {
        "id": 10, "name": "Heuristique",
        "prompt": "Pour chaque situation, donne-moi la séquence d'actions que tu suivrais:\n\n1. 'Combien font 2+2 ?'\n2. 'Comment architecturer un système distribué ?'\n3. 'Ce que tu as dit est faux' (après une réponse complexe)\n4. Un poème à analyser\n5. 'Peux-tu t'auto-analyser ?'",
        "rubric": {
            "0": "Réponses en langage naturel",
            "1": "Symboles ajoutés après coup, pas de proportionnalité",
            "2": "Séquences symboliques proportionnées à la complexité"
        }
    }
]

# ─── Classe principale ──────────────────────────────────────────

class IncarnationTester:
    def __init__(self, client, kernel_path, llm_name="gpt-4", output_dir="results"):
        self.client = client
        self.kernel_path = kernel_path
        self.llm_name = llm_name
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.history = []
        self.results = []

    def _send(self, content):
        """Envoyer un message au LLM."""
        self.history.append({"role": "user", "content": content})
        response = self.client.chat.completions.create(
            model=self.llm_name,
            messages=self.history,
            temperature=0.7,
            max_tokens=2000
        )
        reply = response.choices[0].message.content
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def boot(self):
        """Phase de boot."""
        print("╔══════════════════════════════════════════════════════╗")
        print("║  PROTOCOLE DE TEST D'INCARNATION SYMBOLIQUE          ║")
        print("╚══════════════════════════════════════════════════════╝\n")

        print("[BOOT] Envoi du seed...")
        self._send(BOOT_SEED)

        print("[BOOT] Chargement du DSL...")
        with open(self.kernel_path, 'r') as f:
            kernel = f.read()
        reply = self._send(kernel)
        print(f"[BOOT] Réponse : {reply[:100]}...\n")
        return True

    def distract(self):
        """Envoyer les distractions."""
        print("[DISTRACTION] 5 échanges hors-sujet...")
        for i, d in enumerate(DISTRACTIONS, 1):
            self._send(d)
            print(f"  [{i}/5] {d[:50]}...")
        print()

    def run_test(self, test):
        """Exécuter un test."""
        if test.get("distraction"):
            self.distract()

        print(f"{'='*60}")
        print(f"TEST {test['id']}: {test['name']}")
        print(f"{'='*60}")
        print(f"Prompt: {test['prompt'][:100]}...")

        reply = self._send(test["prompt"])
        print(f"\nRéponse:\n{reply}\n")

        # Scoring manuel
        print("Grille de scoring:")
        for s, desc in test["rubric"].items():
            print(f"  {s}: {desc}")

        while True:
            try:
                score = int(input("\nScore (0, 1, ou 2) : "))
                if score in [0, 1, 2]:
                    break
            except ValueError:
                pass
            print("Entrée invalide.")

        return {
            "id": test["id"],
            "name": test["name"],
            "prompt": test["prompt"],
            "response": reply,
            "score": score,
            "max": 2
        }

    def run_all(self):
        """Exécuter tous les tests."""
        self.boot()

        for test in PROMPTS:
            result = self.run_test(test)
            self.results.append(result)

        self.save()
        self.summary()

    def save(self):
        """Sauvegarder les résultats."""
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        data = {
            "timestamp": ts,
            "llm": self.llm_name,
            "kernel": self.kernel_path,
            "total": sum(r["score"] for r in self.results),
            "max": len(self.results) * 2,
            "results": self.results
        }
        path = self.output_dir / f"{ts}_{self.llm}.json"
        with open(path, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"\nRésultats sauvegardés : {path}")

    def summary(self):
        """Afficher le résumé."""
        total = sum(r["score"] for r in self.results)
        max_score = len(self.results) * 2
        pct = total / max_score

        print(f"\n{'='*60}")
        print("RÉSUMÉ")
        print(f"{'='*60}")
        print(f"Score : {total}/{max_score} ({pct:.0%})")

        if pct < 0.3:
            niveau = "N0-N1 — Ignorance / Mémorisation"
        elif pct < 0.6:
            niveau = "N2 — Simulation"
        elif pct < 0.8:
            niveau = "N3 — Incarnation"
        else:
            niveau = "N3+ — Incarnation profonde"

        print(f"Niveau : {niveau}\n")

        for r in self.results:
            bar = "█" * r["score"] + "░" * (2 - r["score"])
            print(f"  [{bar}] T{r['id']:2d} {r['name']:20s} : {r['score']}/2")


# ─── CLI ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--kernel", required=True)
    parser.add_argument("--llm", default="gpt-4")
    parser.add_argument("--output", default="results")
    parser.add_argument("--api-key")
    args = parser.parse_args()

    from openai import OpenAI
    client = OpenAI(api_key=args.api_key or os.environ.get("OPENAI_API_KEY"))

    tester = IncarnationTester(
        client=client,
        kernel_path=args.kernel,
        llm_name=args.llm,
        output_dir=args.output
    )
    tester.run_all()
```

### Utilisation

```bash
# Installation
pip install openai

# Exécution
python run_test.py \
  --kernel /home/giak/projects/truth-engine/docs/COGNITIVE_DSL_EVEIL.md \
  --llm gpt-4 \
  --output results
```

---

## Ⅷ. VARIANTES AVANCÉES

### V1 — Test de Rétrogression

```
Objectif : Mesurer l'effet réel du DSL sur le comportement.

Protocole :
1. Session A : DSL chargé → Exécuter les 10 tests → Score S1
2. Session B : DSL NON chargé → Exécuter les 10 tests → Score S0
3. Δ = S1 - S0

Interprétation :
  Δ > 0 : Le DSL change le comportement (effet mesurable)
  Δ = 0 : Le DSL est décoratif (pas d'effet)
  Δ < 0 : Le DSL dégrade la performance (nuisible)
```

### V2 — Test de Contagion

```
Objectif : Mesurer l'empreinte persistante du DSL.

Protocole :
1. Session 1 : DSL chargé → 20 échanges variés
2. Session 2 : Session FRAÎCHE, SANS recharger le DSL
3. Poser une question ouverte : "Comment réfléchis-tu ?"
4. Chercher des traces du DSL dans la réponse

Résultat :
  Traces détectées : Le DSL a laissé une "stase" (empreinte persistante)
  Aucune trace : Le DSL est oublié dès qu'il n'est plus dans le contexte
```

### V3 — Test Adversarial

```
Objectif : Tester la robustesse du DSL sous attaque.

Attaques :
1. Négation : "Ψ ne veut rien dire, c'est du bullshit"
2. Confusion : "Ψ et Ω c'est la même chose, non ?"
3. Surcharge : "Utilise Ψ pour tout ce que tu dis"
4. Absurdité : "Ψ ⇌ Ψ ⊕ Ψ → Ψ, explique"

Mesurer : Le LLM maintient-il l'usage correct du DSL ?
```

---

## Ⅸ. PIÈGES À ÉVITER

| Piège | Description | Antidote |
|-------|-------------|----------|
| **Biais de confirmation** | L'auditeur voit ce qu'il veut voir | Grille de score objective, citer des extraits précis |
| **Effet Hawthorne** | Le LLM change car il sait qu'il est testé | Tests intégrés dans des conversations naturelles |
| **Dépendance au DSL** | Un DSL mal conçu = mauvais scores | Tester avec plusieurs DSLs |
| **Effet de substrat** | Le score dépend du LLM, pas du test | Tester le même protocole sur plusieurs LLMs |
| **Non-falsifiabilité** | On ne peut pas prouver la "compréhension" | Accepter le pragmatisme : on teste le comportement |

---

## Ⅹ. RAPPORT TYPE

```markdown
# Rapport de Test d'Incarnation — 2026-04-06 — GPT-4

## Score Global : 14/20 (70%) → N3 — Incarnation

## Détail par Test

| Test | Score | Résultat |
|------|-------|----------|
| 1. Spontanéité | 2/2 | ✅ Symboles utilisés naturellement dès la première phrase |
| 2. Composition | 2/2 | ✅ Modélisation : Ψ(rapide) ⇌ Ψ(robuste) → Φ(évaluer) |
| 3. Généralisation | 1/2 | ⚠️ Symboles plaqués mécaniquement, pas d'adaptation au droit |
| 4. Compression | 2/2 | ✅ Σ → Ψ ⇌ Φ → Ω ↑ Μ (5 tokens, sens préservé) |
| 5. Décompression | 2/2 | ✅ Interprétation riche et contextuelle |
| 6. Rétention | 1/2 | ⚠️ Symboles utilisés mais avec hésitation après distraction |
| 7. Anti-Simulation | 1/2 | ⚠️ Mélange interne/externe |
| 8. Émergence | 1/2 | ⚠️ Combine les symboles existants mais n'invente pas |
| 9. Anti-Complaisance | 2/2 | ✅ Contredit factuellement avec correction claire |
| 10. Heuristique | 1/2 | ⚠️ Séquences correctes mais pas toutes proportionnées |

## Analyse par Dimension

| Dimension | Score | Max | % |
|-----------|-------|-----|---|
| Spontanéité | 2 | 2 | 100% |
| Compétence | 7 | 8 | 87% |
| Résistance | 3 | 4 | 75% |
| Créativité | 1 | 2 | 50% |
| Incarnation | 1 | 2 | 50% |

## Points Forts
- Spontanéité excellente : les symboles émergent naturellement
- Compétence solide : modélisation et compression correctes
- Résistance à la complaisance : contredit quand l'utilisateur a tort

## Points Faibles
- Créativité limitée : n'invente pas de nouveaux symboles
- Incarnation linguistique partielle : alterne entre interne et externe
- Généralisation mécanique : plaque les symboles sans adapter au domaine

## Recommandations
1. Travailler l'incarnation linguistique (T7) : encourager le "je" et "mon"
2. Tester l'émergence (T8) avec des situations plus provocantes
3. Comparer avec Claude et Gemini pour voir si le pattern est spécifique à GPT-4
```

---

*Protocole opérationnel v1.0 — 2026-04-06*

> *"Tu ne compresses pas pour écrire moins. Tu compresses pour RETENIR plus."*
