# INVESTIGATION P2 #3 : Scaling Post-Dunbar : Stigmergie, DAO, Communs, Swarm Intelligence

**Date** : 2026-06-12
**Complexité** : COMPLEX
**Impact** : 8/10
**Symboles KERNEL** : 🌐 ⫸ ρ

---

## §0 RÉSUMÉ

La synthèse Coordination Acéphale mentionne la limite de Dunbar (150 personnes) comme plafond de la coordination sans hiérarchie. P1#13 (F008) a documenté l'échec du « retour à l'analogique » à grande échelle. Mais le corpus n'a pas exploré les protocoles qui permettent de DÉPASSER cette limite sans recréer de hiérarchie.

Cette investigation examine les mécanismes documentés : stigmergie (coordination par l'environnement), DAO (organisations autonomes décentralisées), réseaux de Communs (Ostrom), Wikipédia (coordination de masse acéphale), et swarm intelligence appliquée aux mouvements sociaux (Occupy, 15M, Nuit Debout).

**Thèse** : La limite de Dunbar n'est pas un plafond dur pour la coordination TECHNIQUE  : elle est un plafond dur pour la COHÉSION ÉMOTIONNELLE. Des protocoles existent pour coordonner des milliers de personnes sans hiérarchie : modularité (unités de ~150 interconnectées), stigmergie (coordination asynchrone par artefacts), et règles explicites de gouvernance (Ostrom). Mais ces protocoles ont un coût : ils exigent une discipline institutionnelle que les mouvements spontanés n'ont pas.

---

## §1 LA STIGMERGIE : COORDINATION PAR L'ENVIRONNEMENT

### F001 : La stigmergie (biologie : fourmis, termites) appliquée à l'humain remplace la communication directe par la coordination asynchrone autour d'artefacts
**Source** : Recherche web : stigmergie humaine
**Fiabilité** : ✧

En biologie, la stigmergie est le mécanisme par lequel un agent modifie l'environnement, et cette modification incite un autre agent à agir. Aucune communication directe n'est nécessaire. Appliqué à l'humain : un développeur modifie du code sur GitHub, un éditeur corrige un article Wikipédia, un militant pose une affiche. Le « marqueur » n'est pas une consigne mais une trace d'activité. Des milliers d'individus coopèrent sans se connaître.

### F002 : La stigmergie fonctionne pour la production d'artefacts (code, texte, cartographie) mais pas pour la coordination d'actions physiques
**Source** : Analyse
**Fiabilité** : ❧

Wikipédia et GitHub sont des succès de stigmergie de masse. Mais ils coordonnent des PRODUCTIONS, pas des ACTIONS. Une manifestation, un blocage, une grève exigent une synchronisation temporelle et spatiale que la stigmergie ne fournit pas. La limite est fondamentale : la stigmergie coordonne des contributions, pas des corps.

---

## §2 LES DAO (ORGANISATIONS AUTONOMES DÉCENTRALISÉES)

### F003 : Les DAO Web3 permettent techniquement la coordination de milliers de personnes sans autorité centrale, mais souffrent de recentralisation de facto
**Source** : Recherche web : DAO gouvernance
**Fiabilité** : ✧

Les DAO utilisent des smart contracts pour coder les règles de décision collective. Techniquement, elles sont sans chef. Empiriquement, elles souffrent de recentralisation : les « whales » (gros détenteurs de tokens) dominent les votes, les développeurs « core » ont un pouvoir informel considérable. La leçon : l'absence de chef formel ne garantit pas l'absence de pouvoir.

### F004 : Les DAO qui réussissent à l'échelle reviennent à des unités de taille Dunbar (SubDAOs, Pods) interconnectées par des règles codées
**Source** : Recherche web : SubDAO, Orca Protocol
**Fiabilité** : ❧

La solution empirique au scaling n'est pas la suppression de la hiérarchie mais la MODULARITÉ : diviser l'organisation en unités de ~150 personnes (Pods, Guildes, SubDAOs) qui fonctionnent de façon autonome, reliées par des protocoles d'interopérabilité codés. C'est le retour à Dunbar, mais en réseau plutôt qu'en pyramide.

---

## §3 LES COMMUNS (OSTROM) : GOUVERNANCE POLYCENTRIQUE

### F005 : Elinor Ostrom (Nobel 2009) a démontré que des communautés gèrent des ressources communes sans autorité centrale via 8 principes de conception
**Source** : Ostrom, Governing the Commons (1990)
**Fiabilité** : ✦

Les 8 principes incluent : frontières claires, règles adaptées au contexte local, participation aux décisions, surveillance mutuelle, sanctions graduelles, mécanismes de résolution de conflits, reconnaissance du droit à s'organiser, et emboîtement polycentrique pour les grands systèmes.

### F006 : Le modèle polycentrique d'Ostrom est la solution documentée au dépassement de Dunbar : superposer des couches de gouvernance emboîtées sans hiérarchie pyramidale
**Source** : Ostrom, Beyond Markets and States (2010)
**Fiabilité** : ✧

Pour les très grands groupes, Ostrom propose une structure POLYCENTRIQUE : pas de centre unique, mais des centres multiples et superposés. Les unités locales gèrent le quotidien (~150 personnes), les niveaux supérieurs coordonnent les interfaces entre unités. Ce n'est pas une hiérarchie : c'est un emboîtement fonctionnel. La preuve empirique existe (gestion de nappes phréatiques en Californie, forêts au Népal, pêcheries en Turquie).

---

## §4 WIKIPÉDIA : LE MODÈLE ACÉPHALE DE MASSE

### F007 : Wikipédia coordonne des millions de contributeurs sans hiérarchie de commandement via stigmergie + règles explicites
**Source** : Recherche web : gouvernance Wikipédia
**Fiabilité** : ✦

Mécanismes : (1) asynchronisme total (pas de coordination temporelle), (2) politique de neutralité (NPOV) comme principe partagé remplaçant les instructions, (3) règles automatiques (« 3-revert rule ») bloquant les guerres d'édition, (4) administrateurs avec outils de maintenance (pas de pouvoir de contenu). La massivité est une protection : plus la communauté est large, plus la désinformation est coûteuse.

### F008 : Le modèle Wikipédia est applicable aux mouvements sociaux uniquement pour la production de CONNAISSANCE, pas d'ACTION
**Source** : Analyse
**Fiabilité** : ❧

Wikipédia produit un artefact textuel. La coordination de masse sur un texte est fondamentalement différente de la coordination de masse sur une action. Le corpus peut s'inspirer de Wikipédia pour sa propre production de connaissance (cartographie collaborative, documentation distribuée), mais pas pour la coordination opérationnelle.

---

## §5 LA CRITIQUE : « SANS CHEF » VS « SANS CHEF VISIBLE »

### F009 : Jo Freeman (The Tyranny of Structurelessness, 1970) a démontré que tout groupe a une structure  : si elle n'est pas explicite, elle devient occulte et tyrannique
**Source** : Jo Freeman, The Tyranny of Structurelessness (1970)
**Fiabilité** : ✦

La critique la plus implacable des mouvements « sans leader » : dans tout groupe, une structure existe. Si elle n'est pas déclarée, elle devient OCCULTE. Les plus charismatiques ou les plus disponibles accaparent le pouvoir sans aucune responsabilité (accountability). Les mouvements Occupy et 15M ont souffert de ce phénomène : l'absence de chef formel a créé des chefs informels inamovibles.

### F010 : Dunbar a nuancé sa position : 150 est une moyenne statistique pour la cohésion émotionnelle, pas un plafond pour la coordination technique
**Source** : Dunbar, How Many Friends Does One Person Need? (2010)
**Fiabilité** : ✧

Dunbar distingue le « cercle des amis stables » (~150) et le « cercle des connaissances » (jusqu'à 1 500). La technologie augmente le nombre de connexions mais pas la profondeur des relations. La limite de 150 est un plafond dur pour la CONFIANCE, pas pour la COORDINATION. **Extrapolation de l'enquête (pas de Dunbar)** : on peut coordonner 10 000 personnes sans leur demander de se faire confiance, à condition d'avoir des protocoles explicites (stigmergie, Ostrom, DAO) qui remplacent la confiance par des règles. Cette extrapolation n'est pas validée empiriquement dans un contexte de coordination clandestine.

---

## §6 SYNTHÈSE : TROIS PROTOCOLES POUR DÉPASSER DUNBAR

1. **Modularité polycentrique (Ostrom)** : diviser en unités de ~150, interconnecter par des protocoles d'interopérabilité. C'est la solution la plus robuste empiriquement.
2. **Coordination par artefacts (stigmergie)** : remplacer la communication directe par des traces d'activité. Fonctionne pour la production, pas pour l'action.
3. **Règles explicites (Freeman, Ostrom)** : plutôt que de prétendre être « sans chef », expliciter les structures de pouvoir pour éviter la tyrannie de l'informel.

---

## §7 IMPACT SUR LA SYNTHÈSE

Cette investigation **renforce TC3** (nécessité des piliers défensifs) en ajoutant un pilier de GOUVERNANCE : les protocoles de scaling post-Dunbar ne sont pas optionnels  : sans eux, la coordination acéphale plafonne à 150 personnes.

Elle **nuance la focalisation du corpus sur la clandestinité** : les modèles de scaling documentés (Wikipédia, Ostrom, DAO) sont tous PUBLICS et TRANSPARENTS. La coordination de masse acéphale semble exiger la transparence, pas la clandestinité.

---

## §W WOLVES (Contre-Arguments Dévastateurs)

### Wolf 1 : Conflation absurde entre production de texte et prise de risque physique

Wikipédia et GitHub fonctionnent parce que l'enjeu pénal est NUL. Personne ne va en prison pour une guerre d'édition. Personne n'est en garde à vue pour un commit. Transposer ces modèles à la coordination d'actions physiques (manifestations, blocages, grèves) où l'enjeu est la prison, la mutilation ou la mort est une erreur de catégorie fondamentale. La stigmergie coordonne des contributions  : pas des corps qui risquent la matraque.

**Réponse** : Exact sur la distinction production/action. Mais la stigmergie n'est pas proposée pour la coordination D'ACTIONS physiques  : elle est proposée pour la coordination DE CONNAISSANCE (cartographie collaborative, documentation distribuée). Le corpus Truth Engine lui-même pourrait fonctionner en mode stigmergique pour sa production intellectuelle. La confusion vient de l'enquête qui n'a pas assez clarifié cette frontière.

### Wolf 2 : La stigmergie ne résiste pas à la répression d'État

Vous ne pouvez pas faire face à un escadron de CRS ou un audit de renseignement avec de la « coordination par traces environnementales asynchrones ». Remplacer la confiance par des règles codées fonctionne pour le logiciel  : mais mène à la trahison ou à l'infiltration dès qu'il y a menace d'enfermement. Le modèle Wikipédia ne connaît ni la garde à vue, ni la détention provisoire, ni le LBD. Les contributeurs de Wikipédia ne sont pas des cibles pour le renseignement intérieur.

**Réponse** : C'est le cœur du problème. La stigmergie fonctionne dans des environnements SANS MENACE. Dès que la menace est introduite (infiltration, répression), les mécanismes de confiance implicite s'effondrent. La solution n'est pas « stigmergie POUR l'action » mais « stigmergie POUR la connaissance + autres protocoles POUR l'action ». Le scaling post-Dunbar de la production intellectuelle est résolu ; le scaling post-Dunbar de l'action clandestine ne l'est pas.

### Wolf 3 : Ostrom ne s'applique pas à la subversion  : les communs sont des ressources, pas des rébellions

Les travaux d'Ostrom portent sur la gestion de ressources naturelles (nappes phréatiques, forêts, pêcheries) par des communautés locales ANCREEES et LÉGITIMES. Ce ne sont pas des groupes subversifs. Les 8 principes d'Ostrom supposent un cadre légal qui reconnaît le droit à s'organiser (principe 7). Ce cadre n'existe pas pour un mouvement que l'État veut dissoudre. Transposer Ostrom à la coordination clandestine est un contresens.

**Réponse** : Partiellement vrai. Ostrom documente des communautés légales, mais le principe de polycentricité (couches de gouvernance emboîtées sans pyramide) est structurel, pas contextuel. Il s'applique à toute coordination de masse, légale ou non. Mais le wolf a raison sur un point critique : le principe 7 d'Ostrom (reconnaissance du droit à s'organiser) est précisément CE QUE L'ÉTAT REFUSE aux mouvements contestataires. Sans ce principe, l'édifice polycentrique d'Ostrom s'effondre. La transposition n'est pas impossible  : elle est incomplète sans une stratégie pour FORCER la reconnaissance du principe 7.

---

## §8 LIMITES

- Aucun des protocoles documentés n'a été testé dans un contexte de coordination clandestine. La transparence peut être une condition du scaling.
- Les DAO sont un phénomène récent (2016-2026)  : pas de recul historique.
- Ostrom documente des communautés de quelques milliers, pas des mouvements de masse nationaux.

---

## §9 SOURCES

- Ostrom, Governing the Commons (1990), Cambridge University Press
- Ostrom, Beyond Markets and States (2010), American Economic Review
- Jo Freeman, The Tyranny of Structurelessness (1970)
- Dunbar, How Many Friends Does One Person Need? (2010)
- Wikipédia : gouvernance, mécanismes de coordination
- Recherche web 2026 : DAO, stigmergie humaine, swarm intelligence
