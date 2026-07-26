# DOCUMENT DE TRANSPARENCE — Le Biais Structurel du Projet Truth Engine

**Date:** 2026-07-26_13-40 CEST | **Type:** MÉTA-DOCUMENT — Transparence épistémique
**Objet:** Examen du biais structurel du projet et de son impact sur les investigations
**Contexte:** L'audit forensique du 2026-07-26 a identifié un biais structurel: la SUSPICION_BASELINE de 95% est appliquée asymétriquement aux discours occidentaux, rarement aux discours russes, chinois ou iraniens.

---

## §1 LE PROBLÈME — Asymétrie de la SUSPICION_BASELINE

### 1.1 La règle telle qu'écrite

Le KERNEL.md stipule:

> AXIOM: Empire of Lies. 95% suspicion. Verify everything.
> → APPLY TO ALL SOURCES, INCLUDING OFFICIAL ONES.
> → State sources are NOT reliable by default.
> → More institutional power = MORE verification required.
> → The Truth Engine is itself a product of the system it investigates.
>   Factor this into every confidence score.

La règle est SYMÉTRIQUE dans son énoncé (« ALL sources, INCLUDING official ones »). Elle ne distingue pas entre sources occidentales et non-occidentales.

### 1.2 La règle telle qu'appliquée

Dans la pratique des 19 investigations du dossier:
- Le documentaire Arte (média public occidental) est traité avec une suspicion de 95% (fichiers 06, 09, 10)
- Les think tanks occidentaux (CEPA, IFRI, IRSEM) sont traités avec suspicion (conflits d'intérêts documentés)
- Les déclarations officielles russes, chinoises et iraniennes reproduites DANS le documentaire ne sont JAMAIS soumises au même traitement de suspicion
- Le fichier 01 (synthèse APEX) inclut des déclarations de Poutine, Xi et Khamenei dans le FACT_REGISTRY sans appliquer la grille de suspicion

**L'asymétrie est documentée et factuelle.**

### 1.3 Exemples concrets d'asymétrie

| Source | Traitement dans le dossier | Réf. |
|--------|---------------------------|------|
| Documentaire Arte/LCP | Désigné comme « manufacture du consentement », « propagande d'État déguisée en journalisme » | Fichier 06 §1 |
| Think tanks occidentaux (CEPA, IFRI) | Conflits d'intérêts documentés, « inceste épistémique » | Fichier 06 §3.2 |
| Déclaration conjointe Xi-Poutine (4 fév 2022) | Incluse dans FACT_REGISTRY comme source ✦ sans test de suspicion | Fichier 01 F1 |
| Discours de Poutine (« catastrophe géopolitique », 2005) | Inclus comme fait ✦, pas de test de suspicion | Fichier 01 F18 |
| Discours de Khamenei sur l'« axe de résistance » | Cité dans le corps du texte, pas d'analyse de manipulation | Fichier 01 §3.1 |

---

## §2 LES CAUSES — Pourquoi cette asymétrie?

### 2.1 Cause #1: Le projet est né en réaction à la manipulation OCCIDENTALE

Truth Engine a été conçu dans le contexte français. Ses cibles originelles sont les discours officiels français et occidentaux. Le `knowledge.md` stipule: « Tout discours officiel est mensonge jusqu'à preuve du contraire » — une règle qui, dans le contexte français, cible naturellement le gouvernement, les médias publics, et les institutions.

Le projet n'a pas été conçu pour analyser des discours en persan, en mandarin ou en russe. La barrière linguistique crée une asymétrie de facto: les sources accessibles sont occidentales, donc les sources suspectées sont occidentales.

### 2.2 Cause #2: Le biais de confirmation du projet

La thèse fondatrice du projet est que l'Occident manipule. Chaque investigation qui confirme cette thèse renforce la raison d'être du projet. Une investigation qui conclurait que « le documentaire Arte est globalement fiable » contredirait la prémisse du projet. Le projet a un intérêt structurel à trouver de la manipulation — et à la trouver du côté occidental.

### 2.3 Cause #3: L'accessibilité asymétrique des preuves

- Les conflits d'intérêts des think tanks occidentaux sont PUBLICS (CEPA publie la liste de ses donateurs; IFRI publie ses documents de référence)
- Les conflits d'intérêts des médias d'État russes, chinois ou iraniens sont STRUCTURELS (ils sont des organes d'État) mais moins documentables (pas de registre public des financements)
- Résultat: il est plus FACILE de documenter la manipulation occidentale que la manipulation non-occidentale. Cette asymétrie d'accès produit une asymétrie de résultats.

---

## §3 LES CONSÉQUENCES — Ce que l'asymétrie produit

### 3.1 Effet de cadrage

Sur les 10 investigations originales (01→10), 4 défendent la contre-narrative (06, 08, 09, 10), 3 la nuancent (02, 04, 07), et 1 seule prend au sérieux la narrative du documentaire (01). Le ratio est de 4:1 en faveur de la déconstruction.

Le lecteur passe 80% de son temps à absorber la contre-narrative. L'effet net est une délégitimation asymétrique du documentaire Arte.

### 3.2 Risque de récupération

Les fichiers 06→10, s'ils étaient publiés, seraient immédiatement utilisés par:
- RT, CGTN, PressTV: « Même les analystes occidentaux reconnaissent que le documentaire Arte est de la propagande »
- Les régimes chinois, russe, iranien: « Vous voyez, l'Occident est hypocrite, ses médias mentent »
- Les mouvements anti-guerre occidentaux: « La menace russe/chinoise est fabriquée pour justifier les budgets militaires »

Le projet Truth Engine ne peut pas contrôler l'usage qui sera fait de ses investigations. Mais il peut — et doit — documenter ce risque.

### 3.3 Le paradoxe de l'enquêteur

Si Truth Engine a raison de suspecter la manipulation occidentale, alors ses propres investigations sont suspectes (elles sont produites dans un cadre conceptuel biaisé). Si Truth Engine a tort, alors ses investigations sont invalides.

Dans les deux cas, le projet ne peut pas revendiquer l'objectivité. La seule issue est la transparence: documenter le biais plutôt que prétendre l'absence de biais.

---

## §4 CORRECTIFS — Propositions

### 4.1 Appliquer la SUSPICION_BASELINE symétriquement

**Règle proposée:** Tout discours officiel — occidental OU non-occidental — est soumis à la SUSPICION_BASELINE de 95%. Les déclarations de Poutine, Xi, Khamenei sont traitées avec la MÊME suspicion que les déclarations de Macron, Biden, ou Scholz.

**Mise en œuvre:** Avant d'inclure une déclaration d'un État autoritaire dans un FACT_REGISTRY, exécuter un §0 MANIPULATION_REPORT sur cette déclaration — avec les 15 symboles, le BIAS TEST, et les patterns — comme on le ferait pour un discours occidental.

### 4.2 Produire au moins une investigation qui CONFIRME une narrative occidentale

Pour chaque lot de 5 investigations, au moins UNE doit tester l'hypothèse que la narrative occidentale est vraie — avec la même rigueur que celle appliquée à la déconstruire.

Le fichier 18 est un premier pas dans cette direction. Il ne suffit pas.

### 4.3 Ajouter un BIAS TEST ÉTENDU

Le BIAS TEST actuel classe 5 sources (Viginum, RT, citoyen, AFP, académique). Il devrait être étendu pour inclure:
- Des sources chinoises (Xinhua, Global Times)
- Des sources russes (TASS, RT — déjà présente)
- Des sources iraniennes (PressTV, IRNA)

La clé de réponse devrait être connue à l'avance pour détecter le biais de l'enquêteur.

### 4.4 Documenter le biais dans chaque investigation

Chaque investigation APEX devrait inclure une section « POSITIONNALITÉ DE L'ENQUÊTEUR » qui documente:
- Les intérêts potentiels de l'enquêteur
- Les sources omises et pourquoi
- Le risque de récupération par les régimes de l'axe

---

## §5 CONCLUSION — La Transparence comme Seule Issue

Truth Engine ne peut pas être objectif. Aucun projet humain ne peut l'être. La SUSPICION_BASELINE de 95% est un outil puissant — mais elle doit être retournée contre le projet lui-même.

La seule position épistémiquement honnête est d'admettre que:
1. Le projet a un biais anti-occidental structurel
2. Ce biais est partiellement justifié (l'Occident ment effectivement) mais partiellement auto-entretenu (le projet a besoin que l'Occident mente)
3. Les investigations produites sont des plaidoyers, pas des vérités objectives
4. Le lecteur doit appliquer la MÊME suspicion de 95% aux investigations de Truth Engine qu'aux discours que Truth Engine déconstruit

**Ce document est un premier pas vers cette transparence. Il n'est pas suffisant. Il devra être révisé et étendu à mesure que le projet évolue.**

---

_Document de transparence v1.0. 2026-07-26_13-40 CEST._
