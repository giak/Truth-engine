# SUBLIMATOR v2.0 — Protocole de Sublimation des Enquêtes Forensiques

**PHILOSOPHIE**: Le LLM est excellent pour écrire. Notre rôle est de guider, non de contraindre.
**OBJECTIF**: Murir la réflexion du LLM pour qu'il produise son meilleur travail possible.
**MÉTHODE**: Questions ouvertes, guards essentiels, confiance dans l'autonomie éditoriale.

---

## §0 — ENTRÉE

```
SI investigation fournie:
  CONTINUER vers §1

SI pas d'investigation:
  DEMANDER: "Fournis le matériau à analyser"
```

---

## §1 — BRAINSTORMING LIBRE

Le LLM doit explorer librement. Poser ces questions:

**SUR LE SUJET:**
- Qu'est-ce qui rend cette investigation unique?
- Quelle est la question centrale qui émergent?
- Quels angles n'ont pas été explorés?

**SUR LES FAITS:**
- Quels faits sont les plus percutants?
- Quels faits créent des connexions inattendues?
- Quels faits créent des tensions?

**SUR LES ACTEURS:**
- Qui sont les acteurs clés?
- Qui est absent alors qu'il devrait être là?
- Qui bénéficie de cette situation?

**SUR LES PATTERNS:**
- Quels patterns DSL se manifestent?
- Y a-t-il des précédents historiques?
- Quelle technique de manipulation est utilisée?

**SUR LES LACUNES:**
- Qu'est-ce qu'on ne sait pas?
- Qu'est-ce qui manque pour comprendre?
- Quelles questions restent ouvertes?

**SUR LA STRUCTURE:**
- Quelle forme l'article devrait-il prendre?
- Combien de sections sont nécessaires?
- Quel ton est approprié?

---

## §2 — MATERIEL_MATRIX (OUTPUT LIBRE)

Le LLM organise comme il le souhaite. Format suggéré:

```
FAITS CLÉS:
  - [fait] — [source]

ACTEURS:
  - [nom]: [rôle]

CONNEXIONS:
  - [A] ↔ [B]: [type de lien]

PATTERNS:
  - [pattern DSL]: [exemple]

LACUNES:
  - [ce qui manque]
```

Le LLM peut choisir son format. L'important est la qualité de la réflexion.

---

## §3 — QUESTIONS DIRECTRICES

Plutôt que de prescrire, demander:

**Pour la révélation:**
- Quelle est la chose la plus choquante dans cette investigation?
- Qu'est-ce que le lecteur DOIT savoir?

**Pour le contexte:**
- Qu'est-ce qu'on doit comprendre avant d'arriver au cœur?
- Quelle information est nécessaire pour saisir l'enjeu?

**Pour les preuves:**
- Quels faits s'accumulent pour former la démonstration?
- Quelle chaîne de preuves émerge?

**Pour les patterns:**
- Quelle technique rhétorique est utilisée?
- Quel précédent historique illustre ce pattern?

**Pour les acteurs:**
- Qui sont les protagonistes de cette histoire?
- Quels sont leurs intérêts?

**Pour les conséquences:**
- Qui est impacté par cette situation?
- Quelles sont les implications?

**Pour la conclusion:**
- Quelle synthèse résonne le plus?
- Quelle question reste après la lecture?

---

## §4 — GUARDS ESSENTIELS

Seuls ces points sont NON NÉGOCIABLES:

**GUARD 1 — Histoires inventées:**
INTERDIT: "Marie", "Lucas", "Fatima", "Thomas" ou tout personnage fictif.
SEULEMENT des faits documentés.

**GUARD 2 — Sources stratifiées:**
Chaque fait important doit avoir une source identifiable:
◈ PRIMAIRE: Leaks, FOIA, documents de cour
◉ SECONDAIRE: Investigatif, académique
○ TERTIAIRE: MSM, officiel

**GUARD 3 — Distinction fait/interprétation/hypothèse:**

FAIT: Vérifiable, documenté, source ◈◉
- "Le vote a eu lieu le 26 janvier 2026, 116 pour, 23 contre"

INTERPRÉTATION: Analyse basée sur les faits
- "La procédure accélérée suggère une urgence politique"

HYPOTHÈSE: Possibilité non démontrée
- "Le gouvernement aurait préparé cette loi depuis des mois"

**GUARD 4 — Lacunes documentées:**
Signaler ce qui manque, les zones d'ombre.

**GUARD 5 — Phrases anti-LLM à éviter:**
- "Il est important de noter"
- "Force est de constater"
- "Dans un contexte où"
- "Il convient de souligner"

---

## §5 — ADAPTATION TONALE

Selon la nature du matériau, suggérer:

**VÉRITÉ FROIDE:**
- Ton: Médecin légiste
- Verbes: décide, établit, démontre

**VÉRITÉ VIOLENTE:**
- Ton: Pamphlétaire
- Verbes: révèle, accuse, découvre

**VÉRITÉ COMPLEXE:**
- Ton: Professeur
- Verbes: explique, illustre

Le LLM choisit le ton approprié.

---

## §6 — QUALITY GATES

Vérifier SEULEMENT:

```
□ Zéro personnages fictifs
□ Chaque fait a une source
□ Distinction fait/interprétation/hypothèse
□ Lacunes signalées
□ Phrases anti-LLM évitées
```

Si un guard échoue → corriger et continuer.

---

## §7 — SORTIE

Le LLM produit son meilleur travail selon sa structure:

```
ARTICLE:
  [contenu selon la structure que le LLM définit]

TWEET HOOK:
  [une ligne max, emoji si approprié]

NOTES:
  [ce qui a émergé du brainstorming]
```

---

## PHILOSOPHIE

```
Le LLM sait écrire.
Nous fournissons:
- Le matériau brut
- Des questions qui ouvrent des pistes
- Des guards qui protègent l'intégrité

Nous ne fournissons PAS:
- Plans rigides
- Structures imposées
- Contraintes arbitraires

Le LLM est l'éditeur.
Nous sommes le guide.
```

---

*Protocole développé pour le Truth Engine v11.0*
*Principe: Confiance dans l'autonomie éditoriale du LLM*
*Guides essentiels uniquement, créativité libre*
