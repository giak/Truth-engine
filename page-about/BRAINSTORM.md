# BRAINSTORM — Le fond, la narration, la pédagogie

> Document de travail. L'audit factuel est clos (v4 à v7) : tous les chiffres
> sont vérifiés ou attribués. Ce document traite exclusivement du fond : ce que
> la page dit, à qui elle s'adresse, ce qu'elle démontre, ce qu'elle omet, et
> comment elle le raconte.
> Statut : en discussion, rien n'est encore réécrit. Toute la matière citée ici
> est déjà vérifiée dans le dépôt (audits v4/v5/v6/v7).

---

## 1. Diagnostic : pourquoi le texte est « moyen »

### 1.1 La machine est décrite, jamais montrée

Le texte v7 publié suit la structure du pipeline : anomalie, cadrage, matière,
réduction, vérification, prix et trace, verdict. C'est la structure de la
**machine**. Ce n'est pas la structure de l'**apprentissage**. Un lecteur qui
arrive ne connaît pas le pipeline, il ne cherche pas à connaître le pipeline.
Il cherche à savoir s'il peut faire confiance, ce qu'il va trouver, ce que ça
change pour lui. La page lui administre une visite d'usine composant par
composant, alors qu'il n'a pas encore compris ce que l'usine produit.

Conséquence directe : le lecteur ne voit **jamais une chaîne de preuve
complète**, de bout en bout. Le texte dit « on remonte au fait, à la source, à
la vérification » : il ne le montre jamais. Une phrase d'article, un fait, une
source, une vérification : trois clics auraient suffi à rendre la démonstration
irréfutable. Ils n'existent nulle part.

### 1.2 Le « pourquoi » manque derrière le « quoi »

Le texte donne le quoi : 40 symboles, 15 clusters, 6 dimensions, 95 %, 5
perspectives. Il ne donne presque jamais le pourquoi. Pourquoi 95 % de
suspicion ? Pourquoi la mémoire avant le web ? Pourquoi croiser les modèles ?
Pourquoi refuser de publier un travail incomplet ?

Un enfant qui demande « pourquoi » dix fois de suite ferait tomber le texte en
moins de trois réponses. Or le pourquoi est la matière pédagogique : c'est lui
qui rend le quoi mémorisable. « Le système cherche la manipulation avant les
faits » est la seule phrase qui porte un pourquoi, et elle est noyée dans le
catalogue.

### 1.3 « Défauts connus » : une promesse non tenue

Le sous-titre du texte machine annonce : « pièces, assemblage, contrôle,
défauts connus ». Le texte ne liste **aucun défaut**. Aucun. C'est la promesse
la plus forte du titre, et elle n'est pas honorée.

Or la liste des défauts est la démonstration la plus convaincante de la
méthode : si le système avait quelque chose à cacher, il ne publierait pas ses
défauts. Le dépôt en regorge, tous documentés :

- La recherche mémoire est limitée à 5 résultats : « le système n'a rien oublié » est faux, c'est documenté dans DESIGN.md.
- Les heures par article sont des déclarations de l'auteur, « il ne sort d'aucun compteur ».
- Le registre des posts a des trous (le post #113 est absent de l'index).
- La mémoire contient des doublons et des entrées de test (deux entrées Bucha identiques, observé).
- Certains articles publiés sont de moindre qualité (déclaration de l'auteur dans sa réponse au lecteur).
- Les compteurs internes sont incompatibles entre eux (714 fichiers, 261 dossiers, 105 enquêtes : quatre systèmes de comptage).

C'est de l'or narratif. La méthode ne consiste pas à ne jamais se tromper :
elle consiste à ne jamais maquiller. La page devrait le **prouver**, pas le dire.

### 1.4 Le lecteur est un objet, pas un sujet

Dans le texte actuel, le lecteur est successivement : une ressource cognitive
(le constat), un juge potentiel (la trace), un consommateur (S'abonner). Il
n'est jamais l'apprenti, le témoin, le partenaire. Le texte parle **de** lui,
rarement **à** lui, jamais **avec** lui.

La page About est le seul endroit où l'on s'adresse à un inconnu qui vient de
débarquer. Elle devrait être écrite comme on parle à quelqu'un qui pose des
questions, pas comme on rédige une fiche technique de sécurité.

### 1.5 Deux questions non traitées : « pourquoi te croire ? » et « c'est écrit par une IA ? »

La hiérarchie réelle des questions d'un nouveau lecteur :

1. Qu'est-ce que ce blog ? (identité)
2. **Pourquoi te croire ?** (crédibilité : la question n° 1, la moins traitée)
3. **C'est écrit par une IA ?** (transparence : omniprésente depuis le commentaire Bihan)
4. Comment c'est fait ? (méthode : massivement traitée, mais déclarativement)
5. Qu'est-ce que j'en retire ? (valeur : les articles)
6. Comment je participe ? (abonnement, libre de droit)

La page actuelle traite 4 massivement, 5 et 6 partiellement, 2 et 3 à peine.
Or 2 et 3 sont les questions qui font rester ou partir. La réponse à 2 est la
démonstration (montrer une chaîne). La réponse à 3 est la transparence (assumer
l'IA, et montrer ce qui la contient : l'humain aux commandes, le croisement des
modèles, la trace).

Le design dit « silence sur les critiques : la démonstration suffit ». C'est
juste pour les commentaires. Mais la page About est le lieu où la question de
l'IA se pose à chaque visiteur, avant même toute critique. Ne pas y répondre,
c'est laisser la question ouverte. Le texte v6b a d'ailleurs déjà récupéré
« l'humain n'est pas en surveillance passive : il est aux commandes à chaque
étape » : la direction est bonne, il faut l'assumer jusqu'au bout.

---

## 2. Le principe directeur : la page comme échantillon

La pédagogie ne consiste pas à décrire la méthode. Elle consiste à **pratiquer
la méthode sous les yeux du lecteur**. La page About devrait être un échantillon
de ce qu'elle décrit : un spécimen, pas un schéma.

Concrètement, trois démonstrations possibles, toutes faisables avec la matière
existante :

1. **Une chaîne de preuve filée.** Prendre une phrase d'un article publié,
   remonter au fait, à la source, à la vérification. Avec les liens. Trois
   clics. « Depuis n'importe quelle phrase, on remonte » : il faut le montrer
   sur une phrase réelle.
2. **Une ligne de matrice réelle.** Montrer une ligne de la matrice des faits :
   le fait, la date, la source, l'adresse, le degré ✦. Pas 40 symboles : une
   ligne.
3. **Une correction réelle.** Montrer un avant/après d'une passe forensique :
   un timecode corrigé, une source requalifiée. La preuve que le premier jet
   n'est jamais l'article, en une image.

Une seule de ces trois suffirait. Les trois feraient de la page la démonstration
vivante de son propre propos.

---

## 3. Trois architectures narratives

### A. Le parcours du lecteur (les questions dans l'ordre où il les pose)

La page est structurée par les questions du visiteur, pas par les composants du
système :

- « Vous venez d'arriver. Voici ce que vous allez trouver. »
- « Pourquoi te croire ? » → la chaîne de preuve (une démonstration).
- « C'est écrit par une IA ? » → oui, et voici ce qui contient l'IA.
- « Comment tu vérifies ? » → la méthode en trois idées, pas en vingt.
- « Qu'est-ce que ça change ? » → le constat, la ressource cognitive, la réplique.
- « Comment je participe ? » → abonnement, libre de droit, contact.

Forces : chaque section répond à une question que le lecteur se pose vraiment.
Le lecteur est le personnage principal : il avance, il comprend, il décide.
Failles : le risque de mise en scène artificielle si les questions ne sont pas
naturelles, et la tentation du marketing (« on ne vend pas des barils de
lessive », rappel v4).

### B. La démonstration filée (une seule chaîne, de bout en bout)

Le texte entier est organisé autour d'UN exemple réel, filé du constat à la
publication : l'affaire Clichy (deux tweets à 44 minutes, 5,3 milliards de
contrats publics). Le lecteur suit une enquête réelle du déclencheur au verdict,
et découvre chaque mécanisme quand l'enquête le rencontre, dans l'ordre où elle
le rencontre.

Forces : la pédagogie par le singulier. Le lecteur ne mémorise pas un catalogue,
il suit une histoire. Chaque composant (matrice, sources, vérification) apparaît
au moment où l'enquête en a besoin, donc avec son pourquoi.
Failles : si le lecteur n'adhère pas à l'exemple, tout le texte tombe. Et
l'exemple doit être choisi pour sa lisibilité, pas pour sa violence.

### C. Le récit de la contre-machine (l'histoire de la construction)

Le texte raconte pourquoi une personne seule a construit une machine pour
documenter les machines : l'obsession, la découverte des patterns, la décision
de ne plus subir, l'outil, le prix, les défauts. C'est le récit d'origine du
projet, du « je » à la machine, avec la réponse à 2 (« pourquoi te croire ? »)
et à 3 (« c'est écrit par une IA ? ») intégrées dans la trame.

Forces : l'arc narratif complet, l'émotion possible, la réponse naturelle aux
questions de confiance et de transparence.
Failles : le « je » peut devenir confessions, et le design v3 a déjà rejeté le
ton « je » artisan/ébéniste (« bizarre »). Il faut un « je » factuel, pas
intime : celui de la réponse au commentaire Bihan, pas celui du journal intime.

### Combinaison recommandée : A + B

Le parcours du lecteur (A) comme charpente, la démonstration filée (B) comme
matière : chaque question du lecteur est répondue non par une description, mais
par un morceau de démonstration. Le « je » factuel de C (la réponse Bihan) comme
voix, pas comme structure. L'émotion du constat (« vous êtes une ressource
cognitive exploitée industriellement ») comme ouverture, pas comme simple
accroche.

---

## 4. Les défauts connus : le contenu qui manque

Section dédiée, promise par le sous-titre et absente du texte. Matière disponible
(toute vérifiée) :

- La recherche mémoire plafonne à 5 résultats : le système ne « se souvient » pas de tout.
- Les heures par article sont des déclarations, pas des compteurs.
- Le registre des posts a un trou (#113) et quatre systèmes de comptage incompatibles (714 / 261 / 105 / 39 345).
- La mémoire contient des doublons et des entrées de test.
- Certains articles publiés sont de moindre qualité : l'auteur le dit.
- Le système peut se tromper : la méthode consiste à le signaler, pas à l'éviter.

Le ton : froid, assumé, sans repentance. « La machine a des défauts connus.
Les voici. Ils ne sont pas corrigés en silence : ils sont publiés. C'est la
différence entre une affirmation et une chaîne de preuve. » Cette section fait
plus pour la crédibilité que tout le catalogue de symboles.

---

## 5. Synthèse : la structure recommandée pour la page About

En appliquant A + B, avec la voix factuelle de C, la page About deviendrait :

1. **Ouverture : le constat.** « Neuf propriétaires contrôlent 90 % de
   l'audience. Vous n'êtes pas un citoyen informé : vous êtes une ressource
   cognitive exploitée industriellement. » (déjà présent, c'est le meilleur
   morceau : le garder, l'ouvrir.)
2. **La démonstration.** Une chaîne de preuve réelle, trois clics, une phrase
   d'article remontée à sa source. « Tout est vérifiable. Le voici, vérifié. »
3. **La question de l'IA, frontalement.** « Ce blog est écrit avec une IA.
   Voici pourquoi ce n'est pas ce que vous croyez. » L'humain aux commandes,
   les modèles croisés, la trace. (transformer la question en démonstration,
   sans nommer aucune critique)
4. **Ce que vous recevez.** Une enquête par semaine, gratuit, libre de droit.
5. **La méthode en trois idées.** L'hostilité symétrique (la même grille pour
   tous), la manipulation avant les faits, la trace ✦ (quatre degrés, aucun
   binaire). Trois idées, chacune avec son pourquoi. (la méthode reste
   subordonnée : identité → preuve → promesse → CTA d'abord, conformément à la
   décision vestibule v6c)
6. **Les défauts connus.** La liste, courte, assumée.
7. **Le bilan en chiffres.** Compact (vérifié : 119 articles, 2,2 M mots de
   dossiers, 40 symboles, 15 clusters).
8. **Verdict.** « Je cartographie. Vous décidez. » + la citation de clôture.

Le texte machine (le document de référence complet) garde sa structure
mécanique : il est le dossier, pas le vestibule. Mais il doit honorer son
sous-titre : une section « défauts connus » réelle.

---

## 6. La matière disponible pour démontrer (déjà vérifiée)

- **Clichy** : deux tweets à 44 minutes (12 h 20 / 13 h 04), 51 000 abonnés
  (51 831 exacts, audit v4 ; le texte publié dit 51 000 : c'est ce chiffre
  qu'il faut réutiliser pour rester cohérent), 5,3 Md€ (4,3 contrat
  SEDIF-Veolia + 1 Md FMHP). Chaîne complète disponible.
- **BFMTV** : quatre invités dont trois sans expertise, lieutenant-colonel hors
  service depuis 21 ans, 9 propriétaires ~90 % (RSF/Acrimed).
- **Arte** : 94 minutes, 30 séquences, 28 timecodes, 15 passes, 25 corrections,
  3 rapports, 6 actes, plus de 30 révisions (git log).
- **14 juillet** : 9 sections, 20 faits sourcés, 8 faisceaux forensiques.
- **Corrections réelles** : timecodes de référence croisée corrigés (git log),
  corrections classées par gravité (audits ChatGPT conservés).

---

## 7. Décisions validées avec l'auteur (2026-08-02)

1. **Architecture narrative : A + B.** Parcours du lecteur (les questions dans
   l'ordre où il les pose) + démonstration filée sur un exemple réel, voix
   factuelle du « je » (celle de la réponse au commentaire Bihan).
2. **Question IA : traitée frontalement.** Section assumée : « Ce blog est
   écrit avec une IA. Voici pourquoi ce n'est pas ce que vous croyez. »
   L'humain aux commandes, les modèles croisés, la trace.
3. **Défauts connus : publiés.** La liste du §4 est intégrée aux deux textes,
   y compris « certains articles sont de moindre qualité » (déclaration
   personnelle, assumée).
4. **Chaîne de démonstration : Clichy.** Deux tweets du 27 juin 2026 à
   44 minutes d'intervalle, 51 000 abonnés / 13 500 vues, 5,3 Md€ de contrats
   publics (4,3 Md€ SEDIF-Veolia + 1 Md€ FMHP). URL de l'article :
   https://giak.substack.com/p/un-geyser-de-6-metres-a-clichy-autopsie
5. **Périmètre : démonstration partagée.** La page About (vestibule) et le
   texte machine (dossier) portent la même chaîne Clichy, développée
   différemment selon la cible.

⚠️ Chiffre du bilan : la page About passe de « 118 articles publiés » à
« 119 articles publiés » (convention v5 : nombre de lignes du registre index,
après l'ajout du post machine #120 ; le post #113 reste absent de l'index).
**Décision tranchée en v8c (2026-08-02, à la demande de l'auteur) : 119
conservé, conformément à la convention v5.**

---

*Pour mémoire : ce document est une fiche interne. La règle zéro em-dash ne
s'applique qu'aux articles publiés (Phase 3).*
