# VISION — Sublimator

**Date** : 2026-06-07
**Statut** : DRAFT 2 + extension lignée v23-v33.4 (ajoutées 12 lignes, 3 ères, 1 note fossile)
**Sujet** : Philosophie et idéal opérationnel du moteur SUBLIMATOR
**Périmètre** : Sublimator seul (Truth Engine = amont, Visual = aval futur)
**Suivra** : PFD (Project Foundation Document), PRD (Project Requirement Document), architecture

---

## Table des matières

0. Préambule
1. Mission
2. Le monde dans lequel Sublimator existe
3. L'Idéal
4. Philosophie : la Sublimation
5. Les 3 Piliers : Forensique, Structurelle, Éditoriale
6. Ce que Sublimator n'est PAS
7. Le Voyage
8. Les 4 Briques
9. Manifeste

---

## §0 Préambule

Sublimator n'est pas un outil. C'est une discipline outillée.

Il existe dans un écosystème à quatre pôles :

- **Truth Engine** (amont). Produit les enquêtes brutes, longues, denses, parfois désordonnées. Une enquête = 10 à 60 000 mots de matière forensique en prose française, structurée selon le plan Truth Engine (sections numérotées, du résumé exécutif au FACT_REGISTRY).
- **Mnemolite** (mémoire). Base de connaissance vectorielle (PostgreSQL 18 + pgvector HNSW, 34 outils MCP) qui indexe toutes les investigations, articles, et notes du projet. Recherche hybride lexicale + vectorielle + reranking. C'est la mémoire long-terme du système, interrogeable en temps réel par le LLM hôte.
- **Sublimator** (centre). Exploite ces enquêtes, interroge Mnemolite pour le cross-référencement, agrège, révèle la structure transversale. Produit un article publishable, défendable, traçable.
- **Substack** (aval). Le lieu de lecture. Le lecteur y vient pour comprendre, pas pour consommer. La défiance est l'hypothèse de travail.

Ce document décrit l'**idéal** de Sublimator. Pas ce qu'il est aujourd'hui (un patchwork de versions v23.0 à v33.4, dont deux specs coexistent sans réconciliation, dont un fichier archive est mal étiqueté, dont Mnemolite n'est pas encore intégré au pipeline). Pas ce qu'il sera demain (une v34 intégrant Mnemolite à écrire). Ce qu'il **devrait être**, dans sa forme accomplie.

Les documents ultérieurs (PFD, PRD, architecture) décriront le comment. Celui-ci décrit le pourquoi.

Trois disciplines voisines irriguent ce texte : le journalisme forensique (chaque claim est une pièce à conviction), la rédaction longue (le rythme cognitif est un service au lecteur), la traçabilité documentaire (chaque fait a une source vérifiable).

## §1 Mission

**Transformer N enquêtes en 1 article publishable, sans jamais inventer, sans jamais paraphraser mollement, sans jamais abdiquer la rigueur source.**

L'investigation journalistique française contemporaine produit de la matière. Une pratique régulière publie 1 à 4 enquêtes Substack par semaine, chacune entre 10 000 et 60 000 mots. Cette matière est dense, traçable, mais inutilisable telle quelle par le lecteur final. Le journaliste qui voudrait agréger 10 enquêtes sur un même phénomène (la dette, la transmission des idées, la bureaucratie, la capture) devrait produire un article de 6 000 à 8 000 mots qui :

1. Restitue la trame factuelle de chaque enquête
2. Révèle les transversalités (les concepts, acteurs, mécanismes présents dans au moins K enquêtes, K étant un seuil paramétrable, typiquement 3)
3. Identifie les thèses cardinales (les quelques énoncés qui résistent à la falsification)
4. Tienne la rigueur source (chaque chiffre, chaque date, chaque nom a une URL)
5. Respecte la langue (français soutenu, zéro em-dash dans l'article final, zéro anglicisme non justifié)
6. Soit lisible d'un trait (rythme, alternance densité/respiration, micro-définitions)
7. Soit défendable (chaque claim est vérifiable, chaque URL est résolue, aucun mandat n'est périmé)

**Aucun humain seul ne peut faire cela en moins de 40 heures de travail.** Sublimator est le co-agent qui rend ce travail faisable en 4 heures de jugement humain, plus 30 minutes de relecture finale.

La mission n'est pas d'aller plus vite. La mission est d'**aller plus loin dans la rigueur** que ce qu'un humain seul peut tenir manuellement, sur une agrégation de 10 enquêtes, sans rien sacrifier à la défendabilité.

---

## §2 Le monde dans lequel Sublimator existe

L'année 2026 est celle de la génération de texte à l'infini. N'importe quel modèle de langage peut produire 10 000 mots en 30 secondes. N'importe quel éditeur peut les publier. La barrière à l'entrée de la production textuelle a disparu.

**Le problème n'est plus la production. C'est la confiance.**

Le lecteur Substack de 2026 ne manque pas d'articles. Il manque d'**articles auxquels il peut se fier**. La défiance est devenue l'hypothèse de travail par défaut. Quiconque publie sans chaîne de preuve jointe est soupçonné d'hallucination, de paraphrase, de recyclage. Avec raison : la production de masse hallucine, paraphrase, recycle. La soupape naturelle du lecteur est la défiance.

Dans ce monde, la **chaîne de traçabilité** devient l'avantage compétitif central. Pas le style. Pas la vitesse. Pas le nombre d'articles publiés. La **chaîne de preuve**. Chaque claim, chaque chiffre, chaque citation doit pouvoir être remonté jusqu'à une source primaire vérifiable, et chaque source doit être vivante (URL HEAD 200 OK) au moment de la publication. Le glyphe de fiabilité (✦ tier 1, ✧ tier 2, ⁅ URL cassée, ❧ pas d'URL) n'est pas un détail ergonomique : c'est un **contrat de transparence** passé avec le lecteur.

Sublimator existe parce que cette chaîne de preuve est **impossible à tenir manuellement** sur une agrégation de 10 enquêtes. Le taux d'erreur humain sur 600 000 mots de matière brute est élevé (estimation qualitative, non mesurée empiriquement). Sublimator ramène ce taux à un niveau arbitré par les gates mécaniques et l'audit log. La différence n'est pas marginale. Elle est existentielle : sans outillage, l'agrégation de plusieurs enquêtes est un mensonge par approximation. Avec outillage, c'est un acte forensique.

Le journalisme forensique n'est pas un style. C'est un **acte de résistance** dans un monde qui a banalisé la production textuelle. Sublimator est l'outillage de cette résistance.

---

## §3 L'Idéal

**Sublimator est un alchimiste textuel qui transforme le minerai enquête en or article, en utilisant le feu des LOIS, le creuset des GATES, et le souffle du jugement humain.**

Dans sa forme accomplie :

- Le journaliste arrive avec N enquêtes (1 à 10 dans la pratique actuelle, plus si le contexte LLM et la patience humaine le permettent).
- Il charge la configuration d'agrégation (K = seuil transversalité, N_thèses = nombre de thèses cardinales cibles, complexité cible).
- Sublimator orchestre 3 phases :
  - **Phase 1 — Per-enquête**. Chaque enquête est lue. Ses faits atomiques sont extraits. Ses 12 sections de quintessence sont produites (thèse centrale, thèses implicites, F###, acteurs, causalités, perspectives dialectiques, limites, wolves, iceberg, chronologie, domaines, URLs prioritaires).
  - **Phase 2 — Cross-enquête**. Les N quintessences sont croisées. Les transversalités sont détectées. Les thèses cardinales sont identifiées. Les méta-observations sont synthétisées. Python valide la structure de la sortie.
  - **Phase 3 — Article**. L'article est architecturé (chaîne de révélations), rédigé (draft unique), audité (antagoniste aveugle qui cherche 4 types de failles), poli (14 LOIS), titré (9 propositions : 3 choc, 3 forensiques, 3 conceptuelles).
- Le journaliste arbitre 3 checkpoints (1 par phase, 4 actions possibles : Valider, Modifier, Refuser, Enrichir).
- L'article est publié, défendable, auditable, reproductible.

**Ce qui fait la valeur de Sublimator** :

- **Zéro hallucination.** Chaque claim a une source. Chaque source a été vérifiée mécaniquement (HEAD-check URL). Chaque glyphe est attribué selon la fiabilité.
- **Traçabilité à 100 %.** Chaque F### est identifiable dans la fiche d'origine. Chaque transversalité liste ses fiches_concernees. Chaque thèse cardinale liste ses f_atomiques_justificatifs.
- **4 briques, pas 3.** Python déterministe (I/O, parsing, structure, validation mécanique), Mnemolite (mémoire vectorielle, recherche hybride, cross-référencement), LLM hôte sémantique (lecture cursive, transversalités, thèses, méta-observations, audit), humain souverain (validation finale, arbitrage des checkpoints, publication).
- **Le journaliste garde le contrôle final.** 3 checkpoints bloquants. Publication manuelle. Aucune décision automatique de publier.

**Ce qui fait la frugalité de Sublimator** : il ne tente pas de tout faire. Il fait 3 choses, et il les fait avec la chaîne de preuve intacte du début à la fin.

---

## §4 Philosophie : la Sublimation

**Étymologie.** Le verbe latin *sublimare* signifie « élever, porter au plus haut ». L'alchimie médiévale désignait par *sublimatio* l'opération qui transforme le vif-argent en or, ou plus exactement la matière volatile en matière fixe et précieuse. La sublimation n'est pas une métaphore ornementale : c'est une **opération de séparation** (le pur du vulgaire) et de **fixation** (le volatile en permanent).

**Notre transposition, qui n'a rien de décoratif :**

- L'**enquête** est le minerai : dense, brut, hétérogène, parfois toxique (surinformation, redondance, approximations). Le journaliste le tire de la mine avec effort. Le minerai ne devient pas or par caprice.
- L'**article** est l'or : compact, traçable, défendable, précieux pour le lecteur. Sa densité est le résultat d'un travail de séparation.
- Les **LOIS** (12 ou 14) sont le feu : la température qui purifie, qui élimine le vulgaire (anglicisme non justifié, métaphore biologique, citation non attribuée, em-dash, mandat périmé) et fixe le précieux.
- Les **GATES** sont le creuset : le contenant qui empêche le métal de se perdre, qui impose la forme, qui détecte la fuite. Aujourd'hui GATE_G (complétude mécanique, fonctionnel, 26 tests). Demain un système de gates unifié.
- Le **LLM hôte** est le soufflet : l'agent conversationnel (opencode/Codebuff) qui lit le minerai, reconnaît le métal, pilote les outils, invoque Mnemolite, détecte les patterns. Le LLM hôte n'est pas un récepteur passif de prompts : c'est le pilote actif de la session, qui interroge Python et Mnemolite selon les besoins de l'enquête.
- **Mnemolite** est la bibliothèque de l'atelier : la mémoire vive qui indexe chaque fait, chaque article, chaque investigation. Interrogeable directement via son MCP Server (34 outils), elle fournit au LLM hôte le contexte que sa fenêtre de tokens ne peut pas contenir. Les fichiers markdown locaux restent le fallback si Mnemolite est indisponible ou si une investigation n'y a pas été sauvegardée.
- Le **Python** est l'enclume : la rigidité mécanique qui empêche le batteur de frapper faux, qui compte, qui dédoublonne, qui vérifie les URLs.
- L'**humain** est l'orfèvre : le juge final qui décide quand l'or est prêt, qui refuse la livraison si le titre n'est pas assez dense, qui corrige la dernière phrase si elle n'est pas juste, qui signe.

**Trois corollaires opératoires de cette image :**

1. Si une décision de design ne sert pas la sublimation (la séparation du pur et du vulgaire, la fixation du précieux), elle doit être coupée. Aucun feature n'est gratuit.
2. Si une brique empiète sur le domaine d'une autre (Python qui décide de la cardinale d'une thèse, LLM qui décide du glyphe d'une URL, humain qui refuse sans raison), la brique a empiété. La souveraineté de l'une n'est pas la licence d'envahir.
3. Si l'or final n'est pas défendable (un claim sans source, un mandat périmé, une URL inventée), la sublimation a échoué. On refait, on ne publie pas.

**L'orfèvre est souverain, pas tyran.** L'humain arbitre, mais il arbitre dans le domaine de la valeur (esthétique, justesse, contexte lectorat). Il n'est pas le plus fort des quatre briques ; il est celui qui a le dernier mot parce que l'article est signé.

---

## §5 Les 3 Piliers

Sublimator repose sur 3 piliers indissociables. Si l'un manque, les deux autres s'effondrent.

Note : ces « 3 Piliers » qualifient les **dimensions de qualité** de l'article final (confiance, valeur ajoutée, lisibilité). Ils sont distincts des « 4 Briques » du §8, qui qualifient les **composants architecturaux** du système (Python, Mnemolite, LLM hôte, Humain). Piliers = le quoi. Briques = le comment.

### Pilier 1 — FORENSIQUE

**Tout claim a une source. Toute source est vérifiée. Toute vérification est mécanique et reproductible.**

Ce pilier produit la **confiance**. Sans lui, l'article n'est qu'un texte de plus dans le flux.

**Implique** :

- Chaque fait atomique (F###) porte une URL.
- Chaque URL est testée par HEAD-check au moment de la production.
- Chaque F### porte un glyphe de fiabilité visible :
  - ✦ U+2726 : tier 1 (source primaire, URL HEAD 200 OK)
  - ✧ U+2727 : tier 2+ (source secondaire, URL HEAD 200 OK)
  - ⁅ U+2045 : URL présente mais 4xx/5xx (source cassée, à remplacer)
  - ❧ U+2767 : pas d'URL (source absente, à investiguer)
- Le glyphe est visible dans l'article (le lecteur voit immédiatement la qualité de la source).
- Aucune URL inventée (toujours résolue depuis l'index corpus ou Mnemolite).
- Aucun mandat périmé (DG, ministre, président vérifiés à la date de publication).

### Pilier 2 — STRUCTURELLE

**La forêt est plus que la somme des arbres. Sublimator révèle la structure cachée des N enquêtes.**

Ce pilier produit la **valeur ajoutée**. Sans lui, l'article n'est qu'une compilation.

**Implique** :

- N enquêtes → 1 matrice maître de F### (la volumétrie suit le tier de complexité, voir spec v34 §X cibles par tier).
- Détection automatique des transversalités (F### présents dans au moins K enquêtes, K = seuil paramétrable, typiquement K = 3).
- Brainstorm de thèses cardinales (3 à 5, au-delà le lecteur perd le fil).
- Méta-observations (1 à 5, patterns cross-fiche : corrélations numériques, asymétries, paradoxes).
- Cartographie explicite des positions (continuité, rupture, exception).
- Identification des gaps (F### orphelins, sans transversalité ni thèse, qui signalent des angles morts).
- Architecture narrative (chaîne de révélations : chaque section H2 ouvre la suivante, aucune ne se répète).

### Pilier 3 — ÉDITORIALE

**Le lecteur est souverain. Le texte est un service. La forme respecte l'intelligence.**

Ce pilier produit la **lisibilité**. Sans lui, l'article est illisible même s'il est vrai et structuré.

**Implique** : 14 LOIS formelles appliquées systématiquement.

- L1 sourcing organique : la source est dans la phrase, pas en note de bas de page.
- L2 sources finales : section ## Sources avec URLs précises (page spécifique, jamais racine).
- L3 forme pure : zéro em-dash, un seul émoji en H1, au plus un blockquote par article.
- L4 langue soutenue : zéro anglicisme non justifié, zéro formule creuse, syntaxe stable.
- L5 rythme : alternance densité/respiration, au moins une KO sentence (phrase courte isolée) par section.
- L6 gras stratégique : au plus 1 % du texte en gras, jamais de nom propre sauf objet central.
- L7 compression : zéro transition faible (Cependant, Mais, Voici, Il est important de), sources au plus 10 % du volume.
- L8 zéro cuisine : zéro ID interne (M\d+, FT\d+, F### tout format, D\d+), zéro référence à la structure du projet.
- L9 édifice inline : articles cités en gras avec URL réelle, au plus 3 par section, 2 pour §0 et VERDICT.
- L10 mandats vérifiés : DG, ministre, président, secrétaire général à la date de publication.
- L11 zéro métaphore biologique : pas d'homéostasie, d'organisme, de métabolisme pour qualifier État, marché, parti.
- L12 allégations sourcées : toute relation causale est documentée ou formulée comme question ouverte.
- L13 checkpoints obligatoires : 3 CP par article (CP1 §0, CP2 §2, CP3 §3), 4 actions V/M/R/E, jamais de skip.
- L14 boucle bornée : 3 refus max par CP, halte pipeline au 4e, bilan explicite, état préservé.

**En complément** : 9 propositions de titre (3 choc + 3 forensiques + 3 conceptuels), 1 audit antagoniste aveugle (lit le draft sans l'avoir écrit, signale 4 types de failles : logiques, mots-tic, micro-définitions, équation de synthèse).

**Les 3 piliers sont des contraintes, pas des options.** Un article sans pilier forensique est un mensonge. Un article sans pilier structurel est une compilation. Un article sans pilier éditorial est illisible. Sublimator refuse de publier un article qui manque l'un des trois.

---

## §6 Ce que Sublimator n'est PAS

**Anti-patterns explicitement rejetés.** Si Sublimator devient l'un de ces objets, il a échoué. Cette section est aussi importante que les précédentes : nommer les tentations, c'est les reconnaître pour mieux les repousser.

### Pas un LLM qui écrit sur demande
Sublimator n'est pas un chatbot qui produit du texte en réponse à un prompt. Chaque sortie est traçable, chaque entrée est versionnée, chaque décision est documentée dans un audit log NDJSON. Aucune génération n'est jamais « magique » : elle est l'output d'un module, avec ses inputs, ses gates, son auteur (humain ou LLM), son horodatage.

### Pas une boîte noire
Le journaliste peut, à tout moment, inspecter l'état d'une cellule, l'audit log d'une phase, la liste des transversalités détectées, le glyphe attribué à chaque F###, la chaîne de causalité d'une thèse. Aucune décision n'est opaque. Si une décision est contestable, elle doit être contestable **explicitement**, avec son raisonnement visible.

### Pas un content spinner
Sublimator ne paraphrase pas. Il **révèle**. La différence : un spinner transforme A en A' (équivalent mais différent, sans valeur ajoutée). Sublimator transforme {A, B, C, D, E} en une synthèse A∧B∧C∧D∧E qui n'existait dans aucune des sources. La révélation est l'émergence d'une structure qui n'était lisible dans aucune enquête prise isolément.

### Pas un outil marketing
Sublimator ne maximise ni le SEO, ni le temps sur page, ni le taux de conversion, ni le nombre de partages. Il maximise la **défendabilité**. Si l'article est moins viral mais plus solide, c'est un succès. Si l'article est plus viral mais moins défendable, c'est un échec. Aucune métrique d'engagement n'est dans le GATE.

### Pas un autopilot
Sublimator ne publie jamais sans validation humaine explicite. Les 3 checkpoints sont bloquants. Le journaliste peut refuser (R), modifier (M), enrichir (E) à chaque phase. La publication est toujours manuelle. L14 boucle bornée (3 refus max) existe pour protéger le journaliste de lui-même, pas pour le remplacer.

### Pas un remplacement du journaliste
Sublimator amplifie le jugement humain, il ne le remplace pas. Le journaliste reste l'orfèvre (cf. §4) : il décide quand l'or est prêt, il refuse la livraison si la dernière phrase est maladroite, il reformule le titre si la formulation est faible. Sublimator propose. Le journaliste dispose.

### Pas dépendant d'un LLM unique
L'architecture (LLM hôte = l'agent conversationnel du moment, prompts versionnés en constantes Python, fixtures de test E2E) est conçue pour qu'un changement d'agent hôte (Codebuff, Claude Code, Cursor, ou autre client compatible) n'invalide pas la chaîne. Les tests E2E fonctionnent avec des mocks. Le passage d'un agent hôte à un autre est une opération de re-test, pas de réécriture.

### Pas une cathédrale
Sublimator n'est pas un monolithe. C'est 4 briques indépendantes (Python, Mnemolite, LLM hôte, Humain), 2 modules Python opérationnels, 1 prompt système, 3 phases macro. Chaque brique est testable isolément. Chaque brique peut être remplacée ou améliorée sans casser les autres. La cathédrale n'est pas l'ennemi en soi, mais elle est l'ennemi de la frugalité.

---

## §7 Le Voyage

Sublimator a déjà vécu deux ères et au moins 18 versions. Chacune a apporté une brique. Aucune n'a tenu la promesse complète. Cette section assume l'histoire sans complaisance, fossilisation comprise.

**Ère 1 — LLM-as-craftsman (v23.0 à v32.0).** Le LLM est un artisan à qui l'on confie des sections, et l'humain tranche. Cette ère pose les fondations : les 14 LOIS, le concept de Profil (A/B/C/D), la procédure de checkpoints manuels, la distinction article-données / article-concept. Elle culmine avec v32.0 « Le Processus », refonte majeure déclenchée par un test grandeur nature (l'enquête **émeutes PSG 2026**, juin 2026), qui introduit 3 CPs bloquants (CP#1 BRIEF, CP#2 Draft V1, CP#3 Final), le Profil C fast-track, le calibrage organique de la densité.

**Ère 2 — LLM-as-orchestrator (v33.0 à v33.4).** Le LLM devient un orchestrateur qui invoque 9 agents déclarés, applique 7 gates, signe seul l'article. Cette ère pivote deux fois : v33.2 déporte la mécanique vers Python (5 modules : parse_atomic, extract_utile, curator, gate_g, orchestrator), v33.3 réintroduit le LLM hôte comme détecteur sémantique (Agent F Syntheseur). Le pilote Sumer (juin 2026) tourne sur cette ère, **avec succès malgré la spec, pas grâce à elle**.

**Ère 3 — Quatre briques intégrées (v34+).** La VISION. Le pipeline batch (3 phases) subsiste comme colonne vertébrale, mais chaque phase est outillée par les 4 briques : Python pour la mécanique, Mnemolite pour la mémoire cross-référence, le LLM hôte pour la sémantique, l'humain pour les 3 checkpoints bloquants. L'automatisation est maximale, le jugement humain reste souverain.

| Version | Date | Apport | Limite honnête |
|---------|------|--------|----------------|
| v23.0 → v27.1 | 2024-2025 | Cold Fusion, Adaptive, Digest, Checklist, Two-Tier, Typo | Artisanal. Pas de LLM dans la boucle. Pas de Profil. |
| v28.0 → v28.4 | 2025 | Multi-Agent Pipeline, cycle Écrivain→Critique→Correcteur→Arbitre, scoring 5 critères, 4 Profils A/B/C/D, lint intégré | LLM passif, humain orchestrateur. Spécifications orales, pas de spec_agent.md. |
| v29.0 « L'Édifice » | 2025 | ÉDIFICE CUMULATIF, corpus Substack cité, LOI 9 | Première formulation de l'idéal d'édifice, jamais tenue. |
| v30.0 « Le Concept » | 2025 | Articles-données vs articles-concepts, pattern anticipation, §0 introduction méthodologique | Distinction juste, implémentation faible. |
| v31.0 « Le Protocole » | 2025 | LOI 3 durcie (em-dash ZÉRO), LOI 10/11/12, §3.11 réécrit | LOIS plus strictes, mais boucle de validation inchangée. |
| v32.0 « Le Processus » | 2026 | Refonte PSG 2026, 3 CPs (CP#1/#2/#3), Profil C fast-track, §6.0.5 Compression, §6.4 Red Teaming, §6.1.5 Chambre des Titres, LOI 6 Gras Stratégique Rétinien, calibrage organique, 825 lignes | Toujours pas d'orchestrateur LLM. Vérification humaine pour tout. 6 CPs manuels. |
| v33.0 « L'Orchestrateur » | 2026-06 | 9 agents déclarés, 7 gates G0-G6, orchestrateur LLM, 550 lignes cible | 9 agents jamais implémentés en code. Spec sans implémentation. |
| v33.1 « L'Orchestrateur + Humain » | 2026-06-06 | 3 CPs humains structurés, L13/L14, slot state, boucle bornée 3 refus | 3 CPs et slot state conceptuels. Patch sur v33.0, pas de code nouveau. |
| v33.2 « Extraction Rigoureuse » | 2026-06-06 | Extraction atomique, 5 modules Python, 1493-1512 lignes, GATE_G | Patchwork : §X et §W ajoutés en appendice après le changelog. `spec_version` incohérent (lit 33.0/33.1 dans le code, titre dit v33.2). 2ème système de gates (G0-G6) coexiste avec v33.3 (H0-H6) sans réconciliation. |
| v33.3 « Agent Syntheseur » | 2026-06-06 | Agent F LLM hôte, GATE_H 7 checks, 277 lignes (delta) | Pointe vers §X.9 et §W.13 inexistants dans v33.2. Modules Python `syntheur_*` non écrits. Design et plan créés, exécution dérisoire. |
| v33.4 « Backfill Glyphes » | 2026-06-06 | Backfill Unicode, 158 URLs HEAD-checkées (142 OK, 13 cassées, 2 erreurs), 212 F###-slots annotés | Pas de spec. Workstream commémoré par les commits, pas par un document. |
| v33.5 « Trois Couches Cohérentes » | cible | 14 modules Python, 4 rôles LLM, 3 validations humaines, ≤ 500 lignes spec, ≤ 2000 lignes code | ABANDONNÉ. La v34 intègre Mnemolite et supprime le code mort (llm_lecteur, llm_curator, llm_verifier). |
| v34 « Léger (Mnemolite Integration) » | 2026-06-07 | Intégration MCP Mnemolite, réduction Python (778 → 185 lignes, 2 modules : head_check + gates), prompt système unique versionné, 15 tests PASS | Étapes 1-2 livrées. Étape 3 livrée (maj docs). Reste Étape 4 (pilote). |

**Fossile documentaire.** Le fichier `tools/engines/sublimator/archive/2026-06-06_sublimator_v28.0.md` (51.5K, 825 lignes) est en réalité la **spec v32.0** mal étiquetée. La v33.0 spec §8.1 ligne 1269 prévoyait de le renommer `_archive_SUBLIMATOR_v32.0.md`, renommage jamais exécuté. Le changelog interne ligne 755-769 documente toute la lignée v23.0 → v32.0. Les specs v23.0 à v28.4 elles-mêmes ont été supprimées lors des cleanups git `198b278` (22M élagués) et `facbbc8` (versions obsolètes purgées). L'histoire de l'ère 1 est donc reconstruite à partir de ce changelog unique, sans accès aux sources originales.

**Architecture réelle (post-réduction v34 Léger).** Il n'y a pas d'API LLM externe à « câbler ». Le LLM hôte EST l'agent conversationnel (opencode/Codebuff). Il est le pilote unique : il lit les enquêtes, extrait les F###, interroge Mnemolite, produit quintessences et synthèses, rédige l'article. Python est réduit à 2 modules mécaniques : `head_check.py` (vérification HTTP des URLs, 33 lignes) et `gates.py` (validation structurelle H0-H6, 152 lignes). Les modules `parse_atomic.py`, `extract_utile.py`, `curator.py`, `gate_g.py`, `orchestrator.py` ont été supprimés (Étape 1 de la réduction v34 Léger, juin 2026). Le prompt système unique vit dans `tools/engines/sublimator/prompt-v34.md`, pas dans des constantes Python.

**L'idéal progresse.** La réduction v34 Léger (juin 2026) a ramené Python à l'essentiel : 2 modules mécaniques (head_check + gates), 15 tests. Le LLM hôte est le pilote unique de la conversation, armé d'un prompt système versionné. Mnemolite est intégré via MCP. Ce qui reste à faire : le pilote grandeur nature (Étape 4).

**Le pilote Sumer (juin 2026) a été le premier test grandeur nature** : 10 enquêtes agrégées, 53 F### uniques cités, 12 transversalités détectées, 5 thèses cardinales identifiées, 1 article de ~3 800 mots produit. Le pilote a réussi **malgré** la spec, pas grâce à elle. La spec sera réécrite pour mériter le pilote.

---

## §8 Les 4 Briques

Sublimator n'a pas de brique unique. Il a **4 briques complémentaires**, chacune avec son domaine propre, aucune avec le pouvoir absolu. Cette section est la traduction opérationnelle de l'image alchimique de §4.

### Brique 1 — Python (mécanique, déterministe)

**Domaine** : I/O, parsing regex, structure YAML, comptage, déduplication (Jaccard), HEAD-check URLs, scoring glyphe, validation de format, sérialisation d'état, audit log NDJSON.

**Forces** : rapide, fiable, testable, reproductible, déterministe. La couverture par tests unitaires est une exigence, pas un idéal.

**Faiblesses** : zéro compréhension sémantique. Ne sait pas ce qu'est une « thèse cardinale », seulement qu'un YAML doit contenir un champ `theses_cardinales` avec un certain schéma. Ne sait pas ce qu'est un « em-dash », seulement la séquence de bytes U+2014.

**Modules existants** (2 opérationnels, 15 tests PASS) :
- `head_check.py` (33 lignes) : vérification HTTP des URLs (HEAD request) + attribution des glyphes de fiabilité (✦✧⁅❧).
- `gates.py` (152 lignes) : validation structurelle H0-H6 des YAML de quintessence et de synthèse. Pas de GATE_G (supprimé, le LLM hôte compte ses F### lui-même).

Note : Mnemolite s'intègre via son MCP Server natif, pas via un wrapper Python. Le LLM hôte appelle les outils MCP directement (search, projects, read, health). Aucun bridge Python nécessaire.

### Brique 2 — Mnemolite (mémoire, vectorielle)

**Nature** : PostgreSQL 18 + pgvector HNSW, embeddings locaux (nomic-embed-text-v1.5), recherche hybride lexicale + vectorielle + reranking, 34 outils MCP, API REST + MCP Server, Vue 3 dashboard. Codebase externe à Sublimator, déployée indépendamment.

**Domaine dans Sublimator** : mémoire long-terme du projet. Indexe toutes les investigations, tous les articles publiés, toutes les notes. Fournit au LLM hôte le contexte que sa fenêtre de tokens ne peut pas contenir. Permet la détection de transversalités cross-séries (un concept qui apparaît dans 3 enquêtes de sujets différents, invisible à l'humain).

**Forces** : recherche hybride (lexical + vectoriel), partitionnement temporel, pas d'API externe, déjà en production, 34 outils MCP accessibles en une commande shell (`mnemo search`, `mnemo projects`, `mnemo read`, `mnemo health`).

**Faiblesses** : non intégrée au pipeline Sublimator actuel. Le LLM hôte lit les enquêtes « de tête » sans jamais interroger Mnemolite. La v34 activera l'intégration via le MCP Server natif de Mnemolite, que le LLM hôte interrogera directement.

**Cas d'usage canonique** : le journaliste enquête sur la capture de l'État. Le LLM hôte, via Mnemolite, découvre que le concept de « capture par monopole d'information » apparaît dans 3 dossiers disjoints (Sumer/Edubba, Amériques/quipu, France/ENA). Cette transversalité cross-série est invisible à l'humain seul.

### Brique 3 — LLM hôte (sémantique, stochastique)

**Nature** : l'agent conversationnel (opencode/Codebuff). Pas d'API externe, pas de pipeline autonome. Le LLM hôte reçoit des prompts structurés générés par Python, enrichis du contexte Mnemolite, et produit des outputs sémantiques dans le flux de la conversation.

**Domaine** : lecture cursive d'enquêtes, détection de transversalités, formulation de thèses cardinales, identification de méta-observations, application des LOIS sémantiques (L1, L4, L5, L7, L10, L12), audit antagoniste, propositions de titre.

**Forces** : comprend le sens, généralise, détecte les patterns cross-domaine, formule en français soutenu, identifie ce qui n'est pas dit.

**Faiblesses** : stochastique (deux exécutions peuvent diverger), hallucine possible, pas déterministe, fenêtre de tokens limitée. Doit être **borné** par des gates mécaniques (Python) et **alimenté** en contexte par Mnemolite. La fenêtre de tokens est son point faible : Mnemolite compense en fournissant les faits pertinents sans saturer le contexte.

**Rôles** (définis dans le prompt système `tools/engines/sublimator/prompt-v34.md`) :

- **Phase 1 — Censeur Quintessence** : lit une enquête + contexte Mnemolite → produit 12 sections de quintessence. Appelle `head_check(url)` et `gates.validate()`.
- **Phase 2 — Censeur Synthèse** : lit N quintessences + contexte Mnemolite obligatoire → produit 8 sections de synthese.yaml.
- **Phase 3 — Titre Créateur** : rédige l'article 6000-8000 mots, applique 14 LOIS, génère 9 titres.
- **Phase 3 — Auditeur Article** : antagoniste aveugle, signale 4 types de failles (logique, mots-tic, micro-définitions, équation de synthèse).

Le prompt système unique contient les 4 rôles dans un seul fichier versionné. Pas de `prompts.py`.

### Brique 4 — Humain (arbitrage, souverain)

**Domaine** : validation finale, arbitrage des checkpoints (V/M/R/E), refus de publication, modification de la dernière phrase, correction d'un glyphe contestable, décision de re-run si l'output est faible, signature de l'article.

**Forces** : contexte du lectorat, jugement de valeur, signature finale, capacité de refuser un output même si toutes les gates passent (parce que la dernière phrase n'est pas juste, parce que le ton n'est pas le bon, parce que le titre ne porte pas).

**Faiblesses** : lent, coûteux, fatigue, biais cognitifs. Doit être **protégé** par la boucle bornée L14, l'audit log, et le contexte Mnemolite qui lui évite de vérifier manuellement des faits déjà documentés.

**Note sur la couverture de tests.** Le package `tests/extractors/` contient **15 tests PASS** (0 fail, 0 skip) couvrant le module `gates.py` (checks H0-H6). Les modules `parse_atomic.py`, `extract_utile.py`, `curator.py`, `gate_g.py`, `orchestrator.py` ont été supprimés lors de la réduction v34 Léger (juin 2026) — leurs tests également. `head_check.py` n'a pas de tests unitaires dédiés (les appels HTTP réels sont testés manuellement en pilote).

**Validations** (v34 cible) :

- `VALIDATION_QUINTESSENCE` (5 min par fiche) : these_centrale plausible ? F### bien chiffrés ? shadow_factor cohérent ? GATE_G PASS ?
- `VALIDATION_SYNTHESE` (10 min par agrégation) : sujet_majoritaire correct ? 5 thèses tiennent ? méta-observations originales ? GATE_H 7/7 PASS ?
- `VALIDATION_ARTICLE` (30 min par article) : 14 LOIS respectées ? 9 titres proposés ? 0 URL inventée ? 0 mandat périmé ?

### L'axiome fondateur

**Aucune des 4 briques n'est tyran.**

- Le Python ne décide pas de la cardinale d'une thèse. Il vérifie que le champ YAML existe et contient au moins 3 f_atomiques_justificatifs. Point.
- Mnemolite ne décide pas de la pertinence d'un fait. Elle retourne les résultats de recherche ; le LLM hôte et l'humain jugent.
- Le LLM hôte ne décide pas de la publication. Il propose. Le journaliste dispose.
- L'humain ne décide pas du glyphe d'une URL. Il peut contester un glyphe et demander une re-vérification HEAD, mais le scoring mécanique reste mécanique.

Chaque brique a son domaine. Chaque sortie de brique est validable par les autres. La souveraineté de l'humain est dans le **dernier mot sur la valeur** (esthétique, justesse, contexte lectorat), pas dans le **premier mot sur la mécanique** (regex, comptage, glyphe, URL).

**Pyramide des dépendances.** Python ne dépend de personne. Mnemolite ne dépend que de son propre déploiement. Le LLM hôte dépend de Python (pour les données préparées) et de Mnemolite (pour le contexte). L'humain dépend des trois autres pour l'information, mais aucune des trois ne dépend de lui pour fonctionner. L'humain est le consommateur final, pas le goulot d'étranglement.

---

## §9 Manifeste

**L'enquête est le minerai. L'article est l'or. Le lecteur est le souverain. La mémoire est le territoire.**

Sublimator n'existe pas pour produire du texte. Il existe pour transformer la matière brute du journalisme forensique, outillée par la mémoire vectorielle, en une **offre de confiance** : un article dense, traçable, défendable, qui respecte l'intelligence du lecteur et lui donne les moyens de vérifier.

Dans un monde saturé de génération automatique, la rareté n'est plus le texte. La rareté est la **chaîne de preuve**. Sublimator est l'outillage de cette rareté : Python pour la mécanique, Mnemolite pour la mémoire, le LLM hôte pour la sémantique, l'humain pour le jugement.

Il ne remplacera jamais le journaliste. Il ne le libérera pas non plus de la rigueur. Il rendra seulement cette rigueur **faisable à l'échelle** : N enquêtes en 1 article, 4 heures de jugement humain, zéro hallucination, 100 % traçabilité, mémoire vectorielle activée.

Le but n'est pas la perfection. Le but est la **défendabilité de l'article final devant un lecteur qui ouvre les URL**. Si le lecteur clique sur la première source et trouve une page valide, le pari est tenu. Si le lecteur ne peut pas suivre la chaîne de preuve, le pari est perdu, quelle que soit la qualité littéraire.

**Trois disciplines, un seul instrument :**

- **Le forensique** (chaque claim est une pièce à conviction) produit la confiance. Python + Mnemolite le rendent mécanique.
- **Le structurel** (la forêt est plus que les arbres) produit la valeur ajoutée. Mnemolite + LLM hôte le rendent possible à l'échelle.
- **L'éditorial** (le lecteur est souverain) produit la lisibilité. Le LLM hôte + l'humain le rendent vivant.

Sublimator est l'instrument qui joue les trois en même temps, sans jamais en sacrifier un seul.

**Et derrière l'instrument, l'orfèvre.** Le journaliste qui refuse un titre faible, qui modifie une phrase, qui conteste un glyphe, qui signe l'article final. Sublimator n'existe pas sans cet orfèvre. L'orfèvre n'existe pas sans cet instrument. L'or n'existe pas sans le feu. Et le feu n'éclaire rien sans la mémoire de ce qui a déjà brûlé.

C'est cette alchimie à quatre, et elle seule, qui guide chaque décision de design. Pas la performance. Pas l'élégance technique. Pas la sophistication algorithmique. **La défendabilité de l'article final devant un lecteur qui ouvre les URL, servie par une mémoire qui n'oublie rien.**

---

*Fin de la VISION Sublimator. Document DRAFT 3, à valider avant passage au PFD (Project Foundation Document), puis au PRD, puis à l'architecture. La spec v34 sera le premier livrable technique post-VISION.*

*Version : 2.0 — 2026-06-07 — DRAFT 3 : refonte « 4 briques » (Python + Mnemolite + LLM hôte + Humain). Correction du modèle call_llm (pas d'API externe, le LLM hôte est l'agent). Roadmap v33.5 abandonnée au profit de v34 « Mnemolite Integration » (MCP direct, fusion des gates, suppression code mort).*

