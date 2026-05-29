# CONTROLEUR APEX v2 — Couche 5 Écriture & Narration

> **Date :** 2026-05-26
> **Statut :** Design validé, à implémenter

## Contexte

Le protocole CONTROLEUR APEX (v1.1) vérifie qu'un article n'est **pas faux** (4 couches : Structure, Sourçage, Ton, Fondation). Mais il ne vérifie pas le plus important : est-ce que l'article est **bien écrit** pour sa mission — documenter les machines de contrôle ?

Le SUBLIMATOR v28.1 prescrit une méthode d'écriture (PHASE R avec 6 modules cognitifs, LOIS 1-8). Mais aucun audit final ne vérifie que ces prescriptions ont été suivies dans le produit assemblé.

## Problème

Un article peut passer les 4 couches APEX (structure correcte, sourcé, ton neutre, faits exacts) et être :
- Une compilation de faits sans architecture systémique (le lecteur ne voit pas la machine)
- Une juxtaposition sans démonstration (le lecteur ne peut pas suivre le raisonnement)
- Un mur de briques (le lecteur s'arrête avant la fin)

## Solution — Couche 5 : Écriture & Narration

Trois sous-sections notées /10, ajoutées au protocole existant.

### 5.1 — Visibilité du système

Vérifie que l'article documente une **machine de contrôle**, pas une liste de faits.

Critères :
- Liens intersections explicites entre sections (une section appelle les conclusions d'une autre)
- Tensions du HUB maintenues visibles
- Au moins un « bouclage systémique » (montre comment les pièces s'emboîtent)

Grille : 10 = le système EST le protagoniste / 7-9 = connexions faites mais implicites / 4-6 = image d'ensemble floue / 1-3 = faits juxtaposés / 0 = aucune tentative

### 5.2 — Démonstration traçable

Vérifie que l'article construit des **raisonnements**, pas des accumulations.

Critères :
- Chaque § répond à sa sous-question (Architecture §3.1)
- Chaîne causale visible (donc, parce que, qui entraîne)
- Aucun saut logique non documenté
- Objections anticipées

Grille : 10 = démonstration complète / 7-9 = claire mais elliptique / 4-6 = à reconstruire par le lecteur / 1-3 = juxtaposition / 0 = affirmations sans support

### 5.3 — Respiration

Vérifie que l'article ne noie pas le lecteur sous la densité.

Critères :
- Phrases KO présentes (1-2 phrases courtes qui résument)
- Pas de § >15 lignes sans pause
- Transitions explicites entre mouvements
- Densité dosée (macro/micro alternés)

Grille : 10 = se lit d'une traite / 7-9 = fluide / 4-6 = fatigant en continu / 1-3 = mur de briques / 0 = illisible

### Intégration

- **Score Couche 5** = 5.1×0.4 + 5.2×0.3 + 5.3×0.3
- **Gate** : score < 6 → RÉSERVE (article factuellement correct mais mal écrit)
- **Nouvel axe RADAR S9 — Écriture & Narration** = score Couche 5 direct
- **Pondération globale** recalibrée pour intégrer S9 (détail dans implémentation)

## Changements dans protocole

- Ajout de la section `COUCHE 5 — ÉCRITURE & NARRATION` complète
- Ajout de `S9` dans la table des axes RADAR
- Révision de la pondération du score global
- Ajout dans le GUIDE PÉDAGOGIQUE (Partie B)
- Mise à jour du verdict et de la section SORTIE
- Version → v2.0 (ajout majeur : nouvelle couche + nouveau concept)
