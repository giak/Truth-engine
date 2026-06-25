# Théorie de la Coordination Acéphale — Plan d'implémentation

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Écrire l'article « Théorie de la Coordination Acéphale » (~12-15k mots) — texte-source théorique du corpus Truth Engine, refondant et absorbant la « Doctrine Stratégique du Verrou Français » existante.

**Architecture:** Texte linéaire en 6 sections (Préface + 4 Couches + Conclusion). Chaque section est écrite séquentiellement avec absorption des contenus pertinents de la Doctrine. Chaque tâche produit une section prête à être enchaînée à la suivante.

**Tech Stack:** Markdown, fichier unique dans `investigations/`

**Fichier cible :** `investigations/2026-06-12_12-00_theorie_coordination_acephale_ARTICLE.md`

**Fichier source (absorption) :** `investigations/2026-06-11_article_synthese_verrou_francais_ARTICLE.md` (454 lignes, 8 414 mots)

---

### Task 0: Structure du fichier + Préface

**Fichier :**
- Create: `investigations/2026-06-12_12-00_theorie_coordination_acephale_ARTICLE.md`

- [ ] **Step 1: Créer l'en-tête et écrire la Préface**

Écrire le fichier avec le titre, sous-titre, et la préface complète.

Contenu de la Préface (~800-1 000 mots) :
- Phrase d'ouverture qui pose les deux propositions vraies simultanément
- Proposition 1 : le système verrouille toute coordination (synthèse des 12 verrous en 2-3 phrases, pas de développement)
- Proposition 2 : des mouvements sans chef ont gagné (Solidarnosc, Zapatistes, Soudan 2019, Cherán, Civil Rights US)
- Le paradoxe : les deux sont vrais. Ce texte n'est pas une résolution mais une mécanique des conditions
- Structure annoncée : 4 couches
- Ton B (froid, abstrait)

```
# Théorie de la Coordination Acéphale
## Mécanique des conditions de l'action collective sans chef, sans parti, sans État

## Préface : Le paradoxe

[contenu complet de la préface]
```

Créer le fichier avec juste la Préface.

- [ ] **Step 2: Vérifier le ton B et l'absence de méta-références**

Relire la Préface. Vérifier :
- Zéro mention du corpus, de P-numéros, de SUSPICION_SCORE, d'architecture d'enquête
- Zéro em-dash (—)
- Guillemets français « »
- Phrases courtes, connecteurs logiques explicites
- Pas d'emphase inutile

- [ ] **Step 3: STOP — Validation utilisateur**

Présenter la Préface. Demander validation avant de passer à la Couche 1.

---

### Task 1: Couche 1 — Le Sol (Théorèmes 1-4)

**Fichier :**
- Modify: `investigations/2026-06-12_12-00_theorie_coordination_acephale_ARTICLE.md` (append after Préface)

- [ ] **Step 1: Extraire les contenus pertinents de la Doctrine**

Lire la Doctrine pour extraire :
- §4.3 Types de sanctuaire (pour Th.1)
- §4.4 Les 5 piliers (pour Th.2-3)
- §3.5 Synthèse du motif commun (pour les conditions d'échec)
- Les cas GJ, anti-pass, ZAD NDDL (pour illustrations C)

- [ ] **Step 2: Écrire la Couche 1, Théorèmes 1-4**

Contenu (~1 500-2 000 mots) :

**Th.1 — Sanctuaire** (Scott, hidden transcript)
- Formulation abstraite (B) : tout mouvement a besoin d'un espace soustrait à la surveillance pour exister
- Conditions de validité : 2 types minimum, 1 type = vulnérabilité démontrée (ZAD NDDL)
- Cas concret (C) : Cherán (sanctuaire armé + juridique maintenu depuis 2011)

**Th.2 — Seuil de confiance** (Ostrom, 8 principes des communs)
- Formulation abstraite (B) : la coopération sans contrat exige un seuil minimum de confiance
- Conditions de validité : groupes de taille < 150 (Dunbar), histoire partagée, rituels de confirmation
- Cas concret (C) : les GJ ont échoué à passer ce seuil (78% CSP+, pas de tissu préexistant)

**Th.3 — Protocole de décision** (Graeber, démocratie directe)
- Formulation abstraite (B) : une organisation sans chef a besoin d'une procédure de décision perçue comme légitime par tous
- Conditions de validité : consensus différé, quorum 2/3, mandats impératifs, rotation
- Cas concret (C) : Occupy (consensus pur → paralysie en 6 mois) vs Zapatistes (mandats impératifs → 30 ans)

**Th.4 — Mécanisme de succession** (Sharp, 198 méthodes)
- Formulation abstraite (B) : tout mouvement doit survivre à la perte de nœud quelconque
- Conditions de validité : dead man's switch, cut-out chain, documentation transférable, rotation obligatoire
- Cas concret (C) : FLN/ALN (cellules autonomes, décimation contenue — perte d'un réseau ≠ perte du mouvement)

- [ ] **Step 3: Vérifier le format théorème**

Pour chaque théorème :
- Format (B) abstrait + (C) concret respecté ?
- Condition de validité explicite ?
- Cas illustratif présent ?
- Zéro méta-référence au corpus ?

- [ ] **Step 4: STOP — Validation utilisateur**

---

### Task 2: Couche 1 — Le Sol (Théorèmes 5-8)

**Fichier :**
- Modify: `investigations/2026-06-12_12-00_theorie_coordination_acephale_ARTICLE.md` (append after Th.4)

- [ ] **Step 1: Écrire la Couche 1, Théorèmes 5-8**

Contenu (~1 500-2 000 mots) :

**Th.5 — Ressource commune** (Ostrom, pool resources)
- Formulation abstraite (B) : l'autonomie politique exige une base matérielle non capturable
- Conditions de validité : multiples sources, pas de dépendance >30% à une source unique, transparence interne
- Cas concret (C) : MST (financement par production agricole des terres conquises — autonomie réelle) vs GJ (dons citoyens capturés par la médiatisation)

**Th.6 — Souveraineté narrative** (Tilly, WUNC)
- Formulation abstraite (B) : un mouvement qui ne contrôle pas son récit est défini par ses adversaires
- Conditions de validité : cadre WUNC (Worthiness, Unity, Numbers, Commitment), réplication sans formation, contre-récit permanent
- Cas concret (C) : Zapatistes (maîtrise totale — communiqués, poésie, médias internationaux) vs GJ (capturés en 3 semaines par la diabolisation médiatique)

**Th.7 — Échelle d'escalade** (Sharp + théorie binaire)
- Formulation abstraite (B) : croître sans devenir visible est un problème géométrique
- Conditions de validité : chaque cellule connaît ≤ 2 autres cellules (graphe degré 2), pas de base de données centralisée, pas de hiérarchie visible
- Cas concret (C) : Solidarnosc (structure à double niveau : syndicat public + imprimerie clandestine) vs Hong Kong (réseaux sociaux → surveillance → décapitation)
- Introduction des 5 paliers (micro → local → maillage → régional → national)

**Th.8 — Engagement réciproque** (Scott, infrapolitics)
- Formulation abstraite (B) : la fidélité sans contrat ni hiérarchie exige des mécanismes de réciprocité non-marchands
- Conditions de validité : rituels, risque partagé, secret mutuel, dépendance croisée
- Cas concret (C) : ZAD NDDL (communauté de vie → résilience 9 ans malgré l'échec final)

- [ ] **Step 2: Ajouter la transition vers Couche 2**

2-3 phrases qui :
- Résument les 8 théorèmes comme conditions nécessaires
- Annoncent que la Couche 2 montre l'incarnation en protocoles opérationnels
- Première phrase : « Huit conditions nécessaires. Aucune n'est suffisante seule. Ensemble, elles forment un OS. »

- [ ] **Step 3: STOP — Validation utilisateur**

---

### Task 3: Couche 2 — L'OS (Théorèmes appliqués T2.1-T2.3)

**Fichier :**
- Modify: `investigations/2026-06-12_12-00_theorie_coordination_acephale_ARTICLE.md` (append after Couche 1)

- [ ] **Step 1: Extraire les SOP de la Doctrine**

Lire la Doctrine §5 (SOP 1-6) :
- SOP1 Constitution de cellule → T2.2 (décision) + T2.6 (soin)
- SOP2 Protocole de décision → T2.2
- SOP3 Protocole de succession → T2.3
- SOP4 Protocole financier → T2.4
- SOP5 Protocole de soin → T2.6
- SOP6 Protocole de récit → T2.5

- [ ] **Step 2: Écrire la Couche 2, T2.1-T2.3**

Contenu (~1 500-2 000 mots) :

**T2.1 — Sanctuaire (Th.1 → SOP5)**
- Rappel du théorème racine (1-2 phrases)
- Mécanisme : hidden transcript a besoin d'espace réel. 4 types (physique, politique, numérique, psychologique)
- Plafond de verre : 2 types minimum. ZAD NDDL = 1 type → vulnérabilité totale
- Cas : Cherán (physique + juridique) vs ZAD NDDL (physique seulement)
- Condition de testabilité : tout groupe qui n'a pas sécurisé ≥ 2 types de sanctuaire avant la première action publique échouera mécaniquement

**T2.2 — Décision acéphale (Th.3 → SOP2)**
- Rappel du théorème racine
- Mécanisme : consensus différé + quorum 2/3 + mandat impératif. Taille max du cercle : 7-15 personnes
- Plafond : au-delà de 15, fédération de cercles obligatoire. Pas de fédération = paralysie (Occupy)
- Architecture causale : dépend de T2.1 (on ne décide pas librement sous surveillance)
- Cas : Zapatistes (mandats impératifs, rotation) vs Occupy (consensus sans garde-fou → paralysie)

**T2.3 — Succession (Th.4 → SOP3)**
- Rappel du théorème racine
- Mécanisme : dead man's switch, cut-out chain, rotation obligatoire, documentation redondante
- Plafond : jamais testé empiriquement en contexte français. Score de confiance : 6/10
- Architecture causale : dépend de T2.1 (succession sans sanctuaire = liste d'exécution) et T2.2 (qui a légitimité pour activer le dead man's switch ?)
- Cas : FLN/ALN (cellules autonomes, pas de base de données centrale → survie aux arrestations massives)

- [ ] **Step 3: Vérifier l'architecture causale**

Chaque T2.x doit explicitement lier aux T2.x dont il dépend (sanctuaire → décision → succession). Vérifier que la chaîne causale est lisible dans chaque section.

- [ ] **Step 4: STOP — Validation utilisateur**

---

### Task 4: Couche 2 — L'OS (T2.4-T2.6)

**Fichier :**
- Modify: `investigations/2026-06-12_12-00_theorie_coordination_acephale_ARTICLE.md` (append after T2.3)

- [ ] **Step 1: Écrire la Couche 2, T2.4-T2.6**

Contenu (~1 500-2 000 mots) :

**T2.4 — Financement (Th.5 → SOP4)**
- Rappel : autonomie politique exige base matérielle non capturable
- Mécanisme : 6 050 EUR/mois par cellule, crypto + SEL + tontine + dissidents fortunés. Règle des 3 sources minimum
- Plafond : score 4.5/10. Non testé en procédure réelle. Problème ouvert : dépendance aux CSP+
- Architecture causale : dépend de T2.1 (les transactions passent par le sanctuaire numérique) et T2.3 (que devient le financement si le trésorier est arrêté ?)
- Cas : MST (autofinancement par production agricole) vs GJ (dons capturés)

**T2.5 — Récit (Th.6 → SOP6)**
- Rappel : souveraineté narrative
- Mécanisme : cadre WUNC, réplication sans formation, contre-récit permanent, pluralité des voix
- Plafond : la captation médiatique est le verrou le plus dur. Score 3/10.
- Architecture causale : dépend de T2.1-T2.4 (un récit crédible exige des actions réelles — WUNC n'est pas du storytelling)
- Cas : Zapatistes (maîtrise totale) vs GJ (capturés en 3 semaines). Analyse comparative : pourquoi les Zapatistes ont réussi là où les GJ ont échoué (contrôle du canal + antériorité du récit + cohérence action/parole)

**T2.6 — Soin (Th.8 → SOP5)**
- Rappel : engagement réciproque
- Mécanisme : rotation des tâches, ritualisation, soutien psychologique, protocole de sortie
- Plafond : invisible jusqu'à la première crise interne. 90% de burn-out à 12 mois sans protocole
- Architecture causale : dépend de tous les précédents (le soin est le ciment, pas une couche séparée)
- Cas : aucun mouvement français n'a d'infrastructure de soin. Anti-pass = 28 samedis sans aucun soutien psychologique.

- [ ] **Step 2: Ajouter la synthèse architecturale de la Couche 2**

1-2 phrases qui résument la chaîne causale complète :
```
Sanctuaire → Décision → Succession → Financement → Récit → (tous) → Soin
```
Ajouter : « Pas de sanctuaire → tout le reste est théorique. »

- [ ] **Step 3: STOP — Validation utilisateur**

---

### Task 5: Couche 3 — La Croissance (Escalade et échelle)

**Fichier :**
- Modify: `investigations/2026-06-12_12-00_theorie_coordination_acephale_ARTICLE.md` (append after Couche 2)

- [ ] **Step 1: Extraire la théorie binaire de la Doctrine**

Lire la Doctrine §7 (Plan de Campagne) :
- §7.1 Problème de la montée en échelle
- §7.2 Théorie de la binaire (1→2→4→8→...)
- §7.3 Conditions de division cellulaire
- §7.4 Objectifs intermédiaires

- [ ] **Step 2: Écrire la Couche 3**

Contenu (~2 000-2 500 mots) :

**Introduction** : le problème central — passer de 1 cellule à un mouvement national sans se faire décapiter

**Les 5 paliers** (noyau dur de la couche) :

| Palier | Cellules | Personnes | Changement | Risque principal |
|--------|----------|-----------|------------|------------------|
| Micro | 1 | 7 | Confiance directe | Aucun (invisible) |
| Local | 2-8 | 14-56 | Coordination inter-cellules | Trahison |
| Maillage | 9-64 | 63-448 | Fédération de cercles | Infiltration |
| Régional | 65-256 | 455-1 792 | Visibilité inévitable | Répression |
| National | 257-512 | 1 799-3 584 | Négociation possible | Décapitation |

**Théorème d'échelle** (nouveau — pas dans la Doctrine) : un mouvement peut rester invisible jusqu'au palier régional (~450 personnes en 3 ans) si chaque cellule ne connaît que ≤ 2 autres cellules (graphe de degré 2). Preuve par les cas : Solidarnosc (double réseau visible/invisible), Zapatistes (communautés autonomes sans coordination centralisée visible).

**Sweet spot historique** (nouveau) : l'analyse transversale des 6 cas montre que les mouvements *mixtes* (central pour la coordination stratégique + local pour l'autonomie tactique) survivent plus longtemps :
- Pur horizontal (Occupy) : 6 mois
- Pur vertical (Solidarnosc) : victoire puis effondrement
- Mixte (Civil Rights US, Zapatistes) : 14-30 ans

**La binaire** (repris de la Doctrine, reformulé en mécanisme causal) :
- 1 → 2 → 4 → 8 → 16 → 32 → 64 → 128 → 256 → 512 en 6 ans
- Taux d'échec estimé : ~20% par division (théorique — prédiction falsifiable)
- Condition : chaque division cellulaire est un risque de rupture (trahison, infiltration, conflit de légitimité)

**Conditions de division** (repris et reformulé) :
- La cellule mère doit exister depuis ≥ 6 mois
- Au moins 3 membres de la cellule mère doivent pouvoir encadrer une cellule fille
- Les deux cellules doivent avoir un canal de communication sécurisé direct (pas via une chaîne)
- Chaque cellule ne doit pas connaître plus de 2 autres cellules

- [ ] **Step 3: STOP — Validation utilisateur**

---

### Task 6: Couche 4 — Le Test + Conclusion

**Fichier :**
- Modify: `investigations/2026-06-12_12-00_theorie_coordination_acephale_ARTICLE.md` (append after Couche 3)

- [ ] **Step 1: Écrire la Couche 4**

Contenu (~1 000-1 500 mots) :

**Prédictions d'échec (4) :**
1. **Sanctuaire unique** : si un mouvement n'a qu'un type de sanctuaire, il sera neutralisé en < 2 ans. ZAD NDDL : 9 ans mais neutralisation progressive — confirmation, pas exception (le temps de destruction est proportionnel à la résilience du sanctuaire unique)
2. **Cercle > 15** : si la taille de décision dépasse 15 personnes sans fédération en sous-cercles, paralysie en < 6 mois. Occupy, AG GJ.
3. **Financement unique** : si dépend d'une seule source externe, capturable en < 1 cycle de négociation.
4. **Récit non réplicable** : si le récit ne peut être reproduit sans formation, captation médiatique en < 3 semaines. GJ.

**Prédictions de succès (2) :**
5. **8 conditions remplies** : un mouvement qui remplit les 8 théorèmes de la Couche 1 peut passer du palier Micro au National en 6-8 ans (512 cellules, ~3 500 personnes).
6. **Mixte > pur** : un mouvement mixte (central + local) survit plus longtemps qu'un mouvement pur (horizontal OU vertical).

**Condition de validation** : la théorie est valide si un observateur peut classer un nouveau mouvement comme « prometteur » ou « condamné » avant son issue, sur la seule base des 8 conditions.

- [ ] **Step 2: Écrire la Conclusion**

Contenu (~500-800 mots) :

- Reformulation du paradoxe initial : la théorie existe. Les conditions sont connues. Des mouvements les ont remplies. Pourtant le verrou tient.
- Le verrou n°13 : la théorie ne peut pas forcer quelqu'un à devenir le premier nœud. C'est sa limite intrinsèque.
- Honnêteté finale : la théorie est vraie et insuffisante. Ce n'est pas une faiblesse — c'est une propriété structurelle de toute théorie de l'action collective écrite depuis l'intérieur du système qu'elle analyse.
- Dernière phrase : « La carte est exacte. Le territoire attend. »
- Ton B jusqu'à la dernière phrase, qui bascule en C (concret, adresse au lecteur)

- [ ] **Step 3: STOP — Validation utilisateur**

---

### Task 7: Révision finale et harmonisation

**Fichier :**
- Modify: `investigations/2026-06-12_12-00_theorie_coordination_acephale_ARTICLE.md` (full file)

- [ ] **Step 1: Vérifier la cohérence transversale**

Parcourt l'intégralité du texte pour vérifier :
- Chaque théorème de la Couche 1 est référencé dans la Couche 2 (T2.x ↔ Th.x)
- Les noms de cas sont cohérents d'une couche à l'autre (pas de « ZAD NDDL » devenu « ZAD » ailleurs)
- Le ton B est dominant en Couche 1 et 4, mixte B↔C en Couche 2 et 3
- Zéro em-dash (—)
- Zéro méta-référence au corpus
- Guillemets français « » avec espaces insécables
- Connecteurs logiques présents entre les sections et entre les théorèmes

- [ ] **Step 2: Vérifier l'architecture causale**

Tracer la chaîne causale de bout en bout :
- La Couche 1 pose les 8 théorèmes
- La Couche 2 les applique et montre les dépendances directionnelles
- La Couche 3 montre la croissance (qui dépend de T2.1-T2.6)
- La Couche 4 teste le tout
- Vérifier qu'aucune dépendance n'est implicite

- [ ] **Step 3: Vérifier l'absorption de la Doctrine**

Lire la Doctrine côte à côte avec le nouveau texte :
- Les 5 piliers sont-ils reformulés en théorèmes ?
- Les 6 SOP sont-elles reformulées en T2.x ?
- La binaire est-elle reformulée en T3 (mécanisme causal) ?
- Le verrou n°13 est-il reformulé dans la Conclusion ?
- Les 12 verrous sont-ils condensés dans la Préface (proposition 1) ?
- Rien n'est copié textuellement, tout est reformulé et re-théorisé

- [ ] **Step 4: Comptage final**

Vérifier :
- Longueur cible : 12 000-15 000 mots
- Minimum 4 cas non-occidentaux neufs présents (Soudan 2019, Cherán, Colombie 2021, Iran 2022)
- Tous les théoriciens racines cités (Scott, Ostrom, Graeber, Sharp, Tilly)
- Chaque cas est utilisé dans ≥ 1 section de la Couche 1 ET ≥ 1 section de la Couche 2

- [ ] **Step 5: STOP — Validation utilisateur finale**

Présenter le fichier complet pour validation. Demander si des ajustements sont nécessaires avant publication.
