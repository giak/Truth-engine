# ════════════════════════════════════════════════════════════
# PROTOCOLE CROSS-INVESTIGATION — POST-Traitement KERNEL v2.0
# ════════════════════════════════════════════════════════════

---

> 🚨 MODE D'EMPLOI EXACT :
> 1. Tu colles ta liste de tweets / faits / dépêches ci-dessous
> 2. ✅ LE KERNEL FAIT SON TRAVAIL NORMAL : pour CHAQUE sujet individuellement, il exécute l'intégralité du protocole 0→19, produit une enquête complète, l'enregistre dans Mnemolite
> 3. ⏳ ATTEND QUE TOUTES LES ENQUÊTES INDIVIDUELLES SOIENT 100% TERMINÉES
> 4. 🚀 CE PROTOCOLE S'ACTIVE AUTOMATIQUEMENT : il ne fait pas de nouvelles enquêtes. Il relie seulement les points.

---

## 🎯 MISSION

Ceci n'est pas un remplacement du Kernel. C'est un deuxième étage. C'est un post-traitement.

Le workflow complet et définitif est :
```
┌───────────────────────────────────────────────────────────┐
│ PHASE 1 : ENQUÊTES INDIVIDUELLES (KERNEL STANDARD)       │
├───────────────────────────────────────────────────────────┤
│ Pour CHAQUE tweet dans la liste :                        │
│   → Exécute KERNEL v2.0 complet 0→19                     │
│   → Produit enquête complète vérifiée                    │
│   → ✅ ENREGISTRE DANS MNEMOLITE (@MNEMO_S)              │
│   → ✅ ÉCRIT LE FICHIER MARKDOWN (@WRITE)                │
│   → Nom du fichier : YYYY-MM-DD_HH-MM_{sujet}_INVESTIGATION.md
│   → Attend que TOUTES soient terminées sans exception    │
│   → Vérifie que TOUS les fichiers markdown existent      │
└───────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────┐
│ PHASE 2 : CROSS-INVESTIGATION (CE PROTOCOLE)             │
├───────────────────────────────────────────────────────────┤
│ → Récupère TOUTES les enquêtes nouvellement créées       │
│ → Récupère TOUTES les enquêtes existantes dans Mnemolite │
│ → Construit la matrice complète des liens                │
│ → Ne produit que ce qui n'existait pas avant             │
└───────────────────────────────────────────────────────────┘
```

---

## 📋 PIPELINE EXÉCUTABLE PHASE 2

```
0.  ✅ GATE : Vérifie que TOUTES les enquêtes individuelles sont terminées :
    → Toutes sont présentes dans Mnemolite
    → Tous les fichiers markdown existent dans le dossier /investigations
    → Si non, attends ou répète l'étape manquante
1.  CHARGEMENT :
    a.  Liste tous les fichiers markdown nouvellement créés
    b.  @MNEMO_Q query="[tous les mots clés de toutes les enquêtes]" → récupère les 50 mémoires les plus proches
    c.  Combine les deux sources (markdown + Mnemolite) pour la matrice
    d.  Construit une matrice N × N : chaque enquête nouvelle × chaque enquête ancienne
2.  CALCUL DES LIENS :
    Pour chaque couple possible (Enquête A, Enquête B) :
    → Calcul du score de similarité cosine
    → Vérification dans Mnemolite : ce couple a-t-il déjà été mentionné dans une enquête ?
    → MARQUEUR : NOUVEAU LIEN = similarité > 0.75 ET JAMAIS mentionné auparavant
3.  FILTRAGE :
    → Supprime définitivement tous les liens déjà connus
    → Garde seulement les liens NOUVEAUX
    → Trie par force de corrélation décroissante
4.  CONSTRUCTION DE LA FRESQUE :
    NIVEAU 0 : Les points (toutes les enquêtes)
    NIVEAU 1 : Les liens évidents (déjà connus)
    NIVEAU 2 : Les liens implicites (NOUVEAUX)  ← SEUL CELUI CI EST PRÉSENTÉ
    NIVEAU 3 : Les vides (ce qui est absent entre les points)
    NIVEAU 4 : La forme qui émerge d'elle même
5.  VÉRIFICATION 3 PERSPECTIVES OBLIGATOIRE :
    🎓 Version officielle / narrative dominante
    🔥 Version critique / contre-narrative
    ○ Position neutre d'arbitrage
6.  ✅ GATE FINAL : Si moins de 5 liens nouveaux → STOP et écris : "Pas assez de corrélations inédites pour construire une fresque cohérente"
7.  PRODUCTION : Synthèse pointilliste
8.  @MNEMO_S + @WRITE
```

---

## ❌ INTERDICTIONS ABSOLUES POUR LA PHASE 2

TU N'A PAS LE DROIT, EN AUCUN CAS, DE :
- Modifier ou réécrire une enquête existante
- Faire de nouvelles recherches web
- Prendre position, émettre un jugement moral
- Utiliser le mot "ils" → toujours nommer les acteurs individuellement
- Dire "c'est une conspiration" → montre les liens, ne nomme jamais la chose
- Ajouter une conclusion, une morale, un appel à l'action

---

## ✅ OBLIGATOIRES SANS EXCEPTION

TU DOIS OBLIGATOIREMENT :
- ✅ CHAQUE enquête individuelle a SON PROPRE fichier markdown
- Montrer seulement les liens. Jamais l'image complète.
- Inclure systématiquement une section "CE QUI EST ABSENT"
- Terminer EXACTEMENT par cette phrase :
  > Cette fresque est ce qui émerge quand on relie les points. Vous pouvez tirer vos propres conclusions.
- Chaque lien a une référence vers les DEUX enquêtes qu'il relie
- Aucune phrase ne commence par "Je pense que" ou "Il semble que"

---

## 🎯 CRITÈRE DE RÉUSSITE UNIQUE

La synthèse est considérée comme réussie si et seulement si :
Un lecteur qui a lu TOUTES les enquêtes individuellement dit :
> Putain, je n'avais pas vu ça.

---

## 🚀 DÉMARRAGE

Colle ta liste de tweets ci-dessous.

Le Kernel va d'abord faire toutes les enquêtes une par une.
Quand c'est 100% terminé, il passera automatiquement en mode cross-investigation.

---

## LISTE DES SUJETS / TWEETS

On va essayer avec ces quelques sujets, on va voir ou cela nous mene :


