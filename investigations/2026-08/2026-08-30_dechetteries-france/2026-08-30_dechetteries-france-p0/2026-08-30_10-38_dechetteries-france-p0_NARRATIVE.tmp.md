# KERNEL investigation P0 — Lire l'acte primaire : la délibération CUB de 1980 (déchèterie de Gradignan)

RUN_ID : 20260830-1038-dechetteries-france-p0 · PARENT_RUN_ID : 20260830-0957-dechetteries-france-chaine
AS_OF : 2026-08-30 · INPUT_KIND : UPDATE · MISSION_MODE : INVESTIGATION · via KERNEL v2.10.6 (candidat R2A_BASELINE)

## Résumé

Cette passe lance la **priorité haute (P0)** du dossier : tenter de lire l'acte primaire d'ouverture de la déchèterie de Gradignan (délibération CUB de 1980) pour faire passer FCT du statut LOCALIZED à INSPECTED, et confirmer la cote exacte auprès des Archives.

## 1. Résultats obtenus

1. **La notice « Délibérations de 1980 » est confirmée INSPECTED** (FCT-001, ✧) : dans l'arbre du fonds **BXM 511 W** « Délibérations de la communauté urbaine de Bordeaux (1967-2003) », la notice **8586 = « Délibérations de 1980 »** (chemin `view:8586/n:411`), encadrée par 1979 (8580) et 1981 (8593). Source : capture Wayback du 16/01/2023 du fonds (le site live est bloqué par Anubis). C'est une **localisation précise et vérifiée** de l'acte, au niveau du registre annuel.

2. **Le registre PDF OCR de 1980 n'est pas lu** (LED-001, GAP ACCESS) : le live `view:8586` et la page délibérations v2ont bloqués par Anubis (HTTP 200 → page « Making sure you're not a bot ») ; aucune capture Wayback des pages de détail/registre ne subsiste (CDX vide) ; la cote/n° de délibération n'est pas corroborée par une source libre. L'acte **reste LOCALIZED** — la lecture du contenu requiert un accès interactif (navigateur) ou la salle de lecture, ou confirmation par courriel `archives@bordeaux-metropole.fr`.

3. **Corroboration officielle renforcée** (FCT-002, ✧) : une **seconde occurrence officielle** désormais inspectée (actualité de l'exposition des Archives BM, capture Wayback 18/09/2025) : « création de la première déchetterie en France ouverte à Gradignan le **17 novembre 1980**, adoption en 1993 du plan TRIVAC ». Cela renforce l'affirmation du panneau (même institution, support distinct), sans constituer une corroboration indépendante (LED-002, GAP INDEPENDENCE).

## 2. Verdict épistémique

- **Acte primaire** : LOCALIZED (FCT-001 ✧), non INSPECTED — le chemin exact est établi, le contenu non vérifié. Aucune contradiction matérielle ; limite d'accès technique (Anubis) documentée, pas une dissimulation.
- **Revendication 17/11/1980** : corroborée intra-famille (2 supports officiels inspectés), corroboration indépendante toujours GAP.
- **Chaîne causale** délibération → ouverture non vérifiée étape par étape (GAP CAUSALITY, CAU-001) tant que le registre n'est pas lu.

## 3. Limites

Lecture du registre requiert accès interactif ou salle de lecture ; RetroNews/Sud Ouest payants pour la presse 1980-85 ; aucune capture Wayback des pages de détail.

## 4. Traçabilité

2 sources officielles inspectées (famille A : panneau d'exposition référencé SRC-001 et actualité SRC-002), 2 faits ✧ (FCT-001 localisation notice 8586, FCT-002 2e occurrence officielle), 2 LED (LED-001 GAP ACCESS, LED-002 GAP INDEPENDENCE), 3 AXS (AXS-001/002 GAP typés, AXS-003 N/A), 2 CLM, 1 CAU (GAP CAUSALITY), 1 réfutation exécutée (NONE), 1 barrière technique Anubis documentée. 8 checkpoints PASS. Sections complètes.