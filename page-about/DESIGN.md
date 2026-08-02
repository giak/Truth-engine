# Design — « Comment ces articles sont écrits »

> Texte pédagogique destiné à la page About de Résistance Cognitive (Substack).
> Objectif : répondre didactiquement aux questions récurrentes (comment, par quels moyens, de quelle façon les articles sont produits).
> Dernière mise à jour : 2026-08-01.

---

## Décisions validées

| Dimension | Choix | Note |
|-----------|-------|------|
| Destination | Page About / section fixe | ~1 500-2 500 mots |
| Angle | La machine qui documente les machines | Le texte est une pièce du corpus, pas un commentaire : cadrage manifeste (anomalie, cadrage, matière, réduction, vérification, prix/trace, verdict) |
| Ton | Analytique, forensique, manifeste | Registre du blog : parallélismes + chiffres + thèse, formules binaires « Ce n'est pas X : c'est Y. » |
| Niveau technique | Vulgarisé | Jargon expliqué, symboles introduits un à un (comme la page About le fait déjà) |
| Preuves | Un échantillon concret | L'article Arte « La fabrique de la menace » comme fil conducteur |
| Critique | Silence sur les critiques | La démonstration suffit, aucune réponse directe aux commentaires |
| Structure | Linéaire (chaîne de production) | Ouverture → Phase 1 → Phase 2 → Phase 3 → Coût → Fermeture |

## Règles de rédaction (AGENTS.md)

- Français soutenu, zéro anglicisme non justifié
- Zéro em-dash (—) : utiliser `:` pour les titres, `-` pour les listes
- Espaces insécables avant les deux-points, guillemets français « »
- Toute affirmation chiffrée appuyée sur une source vérifiée
- Chaque terme technique expliqué au premier usage
- Cohérence avec la page About existante : les symboles et termes déjà présentés
  (Ξ Λ Ω € ⚔ Ψ, matrice de faits, perspectives dialectiques) peuvent être réutilisés
  tels quels, le lecteur les a déjà vus

---

## Apports intégrés de la page About existante

### Cadrage (ouverture)

- Le constat : « 80 % de l'information passe par cinq entreprises » est le pourquoi
  de la méthode. L'ouvrir en une phrase suffit, sans développer : le lecteur de la
  page l'a déjà lu.
- Positionnement : « une personne seule avec des outils IA », entre trois mondes :
  médias mainstream (n'y touchent pas), médias alternatifs (manquent de rigueur),
  études académiques (trop lentes et confidentielles).
- La promesse du pipeline : produire ce que les journalistes font à la main
  (recherche, croisement de données, fact-check, visualisation) en les automatisant,
  sans retirer l'humain de la boucle.

### Phase 1 — enrichie : le scan avant la recherche

Le langage symbolique est un point pédagogique fort : **avant toute recherche**, le
sujet est scruté avec un langage codé de concepts de manipulation (l'iceberg, le
cadrage, l'inversion, le cui bono, la guerre informationnelle, la surcharge).
⚠️ La page About dit « 148 concepts » : c'est une déclaration interne du système
(DSL.md) ; le recompte partiel donne 40 symboles + 10 à 17 patterns + 16 menaces.
Le texte peut citer « un langage codé » sans le chiffre, ou citer 148 comme
déclaration du système. Chaque concept est scoré de 0 à 10 ; les scores déclenchent
des familles de patterns (ICEBERG, GASLIGHTING, INVERSION, FRAMING, MONEY, POWER,
NETWORK, WAR) qui orientent l'enquête. ⚠️ La page About annonce « 9 patterns » et
« 16 clusters » : PATTERNS.md contient 10 définitions core et 17 @PAT[] uniques ;
clusters/ contient 15 fichiers réels (17 avec index et template). Écarts documentés,
à ne pas reproduire tels quels dans le texte.

Présentation vulgarisée : 3-4 symboles avec leur traduction, puis la phrase clé
« le système cherche la manipulation avant de chercher les faits ».

Garde-fous de la Phase 1 (déjà sur la page, à reformuler didactiquement) :
- Refus de publier un travail incomplet (la porte de contrôle)
- Faits non vérifiés explicitement marqués (matrice ✦✧⁅❧ : dur, mou, non vérifié, spéculatif)
- Sources stratifiées : primaire, secondaire, tertiaire
- Vérification croisée sur au moins deux domaines
- Diversité épistémique : géographie, langue, type de source, propriétaire, perspective, temporalité
- Trois perspectives dialectiques : officiel, dissident, arbitrage

### Phase 2 — enrichie

- Les perspectives dialectiques (officiel / dissident / arbitrage) font partie du
  croisement : chaque thèse est confrontée à ses contradicteurs avant d'entrer dans
  l'article.

### Fermeture — enrichie

- « L'Empire du Mensonge exige une Immunité Cognitive » : punchline de clôture possible.
- Libre de droit : tout le contenu est récupérable, citez la source. Renforce la
  traçabilité : ce n'est pas seulement vérifiable, c'est ouvert.

### La mémoire du système (Mnemolite) — la capitalisation

Mnemolite est le composant mémoire de Truth Engine : une base de connaissance
vectorielle où chaque enquête, chaque source, chaque quintessence, chaque note est
indexée et interrogeable sémantiquement. C'est la **capitalisation** : le système
se souvient de ce qu'il a déjà vérifié, et s'en sert pour tout le reste.

Rôle dans le pipeline (KERNEL.md) :
- **Étape 2 du protocole** : la recherche mémoire précède la recherche web.
  Avant d'ouvrir un navigateur, le système interroge sa propre mémoire. Si le
  sujet a déjà été traité, les sources existantes remontent d'abord.
- **Étape 19** : chaque enquête terminée est sauvegardée dans la mémoire.
- **Nuance (vérifiée dans KERNEL §1 step 2)** : si la recherche mémoire échoue
  pendant une enquête, le protocole la saute et continue (log de la défaillance),
  il ne bloque pas. Le blocage total (HALTE) est réservé au pipeline de production
  d'articles (Sublimator), où la mémoire est une condition de démarrage.
  → Le design initial disait « mémoire DOWN = refus de travailler » : FAUX pour
  l'investigation, vrai pour la production d'article. Correction appliquée.

État réel (2026-08-01, vérifié via MCP) :
- 39 345 entrées indexées, 97,8 % avec embedding sémantique
- dont 4 764 entrées classées « investigation », 698 notes, 94 quintessences,
  50 articles, 80 références, 45 décisions
- ⚠️ « 4 764 investigations » = entrées de mémoire, PAS 4 764 enquêtes distinctes :
  la base contient des doublons (deux entrées Bucha identiques à 1 min d'intervalle,
  observé) et des entrées de test (« TEST — Chine investigation »). Le dépôt compte
  lui 714 fichiers `*_INVESTIGATION.md` ; l'INDEX.md déclare 261 dossiers ; la page
  About dit 105 enquêtes. Quatre systèmes de comptage incompatibles. Le texte doit
  éviter tout chiffre d'enquêtes non attribué.

Preuve pédagogique (vérifiée) : une recherche « La fabrique de la menace » dans la
mémoire remonte les documents clés du dossier : l'article Arte publié, le README du
dossier, la quintessence APEX, le plan de refonte et le rapport de prépublication.
⚠️ La recherche était limitée à 5 résultats : « remonte les documents clés » est
juste, « n'a rien oublié » serait une exagération. Le dossier contient 10 fichiers.

Point pédagogique fort : la connexion entre enquêtes. Le plan de refonte Arte
critiquait l'article de ne pas relier ses conclusions aux enquêtes antérieures
(concentration médiatique, guerre cognitive). La mémoire existe précisément pour
cela : chaque article s'appuie sur ce que le système sait déjà, et chaque nouvelle
enquête enrichit le capital des suivantes.

Présentation vulgarisée : « une mémoire interne » ; le nom propre (Mnemolite)
peut apparaître une fois entre parenthèses ou être omis. Chiffres prudents :
« des dizaines de milliers d'entrées indexées » est sûr ; tout décompte précis
(39 345, 4 764, 105, 261) doit être attribué à son système de mesure.

### La diversité des modèles — croiser les avis, pas seulement les sources

Point ajouté à la demande de l'auteur : plusieurs LLM sont utilisés, non pour la
puissance ou la performance, mais pour les **biais**. Les entraînements diffèrent,
les harnais diffèrent, les contextes système diffèrent. Chaque modèle a ses angles
morts. Croiser les sources ne suffit pas : il faut aussi croiser les avis des
modèles. La page About actuelle ne mentionne pas ce point : c'est un apport nouveau.

Preuves matérielles dans le dépôt :
- **L'audit adversarial** (`tools/engines/auditor/`) fait tourner 10 phases sur
  5 modèles LOCAUX via Ollama : phi4-mini 3.8B, qwen3:8b, granite3.2:8b. Quatre
  regards indépendants (Greffier, Logicien, Cartographe, Contrebandier) lisent le
  même article, chacun avec un prompt et un format de sortie différents, puis une
  synthèse converge et un veto final tranche. C'est la formalisation du principe :
  un seul modèle juge moins bien que quatre modèles qui se contredisent.
- **Le dossier Arte** : le plan de refonte est « une synthèse d'analyses Buffy +
  ChatGPT » ; trois rapports d'audit sont produits par ChatGPT ; d'autres documents
  du projet nomment « Buffy » (= deepseek-v4-pro, attesté dans un audit du
  2026-07-31) et « Theo » (= Gemini).
- Donc : modèles propriétaires (ChatGPT/OpenAI, Gemini/Google), modèles ouverts
  locaux (phi4-mini, qwen3:8b, granite3.2:8b via Ollama), et un autre modèle distant
  (deepseek). Les biais d'entraînement et de contexte système sont compensés par la
  confrontation, comme les biais de source le sont par la stratification ◈◉○.

Présentation vulgarisée : « le système ne fait pas confiance à un seul avis
machine : plusieurs modèles, des entraînements différents, des contextes différents,
se relisent et se contredisent. Un article passe sous au moins deux regards de
modèles différents, parfois cinq. »

---

## Structure du texte (6 blocs)

> ⚠️ RÉVISÉ (v3, 2026-08-01) : la structure initiale en « 3 phases » a été remplacée
> par 6 blocs-mécanismes dans le registre manifeste du corpus. Le fil conducteur
> Arte reste la preuve chiffrée principale, mais l'ouverture s'ancre sur l'anomalie
> Clichy (tweet, point de départ typique) et BFMTV. La section « v3 » du SUIVI.md
> documente les retours auteur successifs qui ont mené à cette structure.

### Ouverture — la question et la réponse en une phrase

Le point de départ est la question récurrente : « comment c'est écrit ? ».
Réponse immédiate : un protocole de production en trois phases, documenté de bout en bout,
dans lequel un humain reste aux commandes à chaque étape.
Justification en une phrase : un modèle de langage livré à lui-même produit du texte fluide
et faux ; le protocole existe pour empêcher le faux de survivre.
Positionnement : une personne seule, avec des outils IA, entre trois mondes qui ne
produisent pas ce niveau d'enquête.
Annonce du plan : trois phases, avec l'article sur le documentaire Arte comme fil conducteur.

### Phase 1 — L'enquête : transformer une question en dossier

- Un protocole de recherche de 20 étapes, exécuté pour chaque sujet.
- Le scan préalable : le langage symbolique (un langage codé de concepts de
  manipulation, scorés 0 à 10),
  « le système cherche la manipulation avant de chercher les faits ».
- La mémoire d'abord : avant toute recherche web, le système interroge sa propre
  mémoire (Mnemolite) : enquêtes précédentes, sources déjà vérifiées, quintessences.
  Il ne repart jamais de zéro.
- Décomposer le sujet, lancer des recherches, croiser les sources.
- La matrice de faits : chaque fait consigné avec sa date, sa source, son URL
  et son niveau de fiabilité (fait dur, fait mou, non vérifié, spéculatif).
- Les garde-fous : refus de publier un travail incomplet, faits non vérifiés
  marqués, sources stratifiées, vérification croisée ≥2 domaines, diversité
  épistémique (6 dimensions), perspectives dialectiques (officiel/dissident/arbitrage).
- Preuve Arte : documentaire de 94 minutes découpé en 30 séquences chronométrées
  (28 + 2 paratexte), avec citation exacte, locuteur et technique pour chacune.
  Une matrice, pas une impression.

### Phase 2 — La réduction : de plusieurs dossiers à une matière exploitable

- Chaque enquête est distillée en une quintessence : faits, acteurs, sources, mécanismes.
- Les quintessences sont croisées pour faire émerger les thèses centrales.
- Les trois perspectives (officiel, dissident, arbitrage) sont confrontées à chaque étape.
- La mémoire relie : chaque quintessence produite est indexée dans la mémoire du
  système. Le croisement des enquêtes passe par la mémoire : l'article Arte est
  relié aux enquêtes antérieures sur la concentration médiatique et la guerre
  cognitive, au lieu de les ignorer.
- Pourquoi : l'article n'est pas « tapé d'un seul jet » ; l'écriture s'appuie sur une
  matière déjà certifiée, jamais sur ce que le modèle « se rappelle ».
- Preuve Arte : l'article repose sur 19 enquêtes distinctes (dossier
  `axe-chine-russie-iran`, 19 fichiers INVESTIGATION + 19 quintessences).
  L'écriture est une synthèse de dossiers vérifiés, pas une génération.
  ⚠️ Le commentaire public de l'auteur dit « 25 enquêtes » : non confirmé par
  le dépôt, le dossier documente 19.

### Phase 3 — L'écriture : la rédaction sous contraintes

- Chaque affirmation doit provenir d'un fait du dossier, chaque timecode exact,
  chaque source citée.
- Moment clé : le premier jet n'est jamais l'article.
- Le croisement des avis : l'écriture n'est pas soumise à un seul modèle. Les
  audits croisés mobilisent plusieurs LLM (modèles locaux via Ollama : phi4-mini,
  qwen3:8b, granite3.2:8b ; modèles propriétaires : ChatGPT, Gemini ; et d'autres
  comme deepseek). Quatre regards indépendants relisent le même texte, puis une
  synthèse et un veto tranchent. L'idée : les biais d'entraînement, de harnais et
  de contexte système diffèrent d'un modèle à l'autre ; les confronter, c'est
  neutraliser les angles morts de chacun. On croise les sources, et on croise les
  modèles qui les lisent.
- Preuve Arte (échantillon détaillé) :
  - ~15 passes de corrections forensiques (README du dossier)
  - plan de refonte complet (documentaire réorganisé en six actes)
  - 28 timecodes vérifiés (README ; une correction ultérieure a porté sur
    deux timecodes de référence croisée non mis en gras, git log)
  - 25 corrections classées par gravité lors d'un audit croisé (rapport
    d'exécution forensique, ChatGPT)
  - trois rapports d'audit externes documentés (ChatGPT : directeur de refonte,
    exécution des corrections, prépublication)
  - ⚠️ « 32 sources » (README du dossier) vs « 19 sources » (commentaire public
    de l'auteur) : les deux chiffres cohabitent, le README est la source du dépôt
  - chaque passe corrige des erreurs, des ambiguïtés, des conclusions trop timides

### Le coût réel — le prix de la rigueur

Section courte et chiffrée :
- 16 à 30 heures par article selon la complexité ⚠️ (déclaration de l'auteur,
  non vérifiable dans le dépôt : à présenter comme telle ou à retirer)
- des centaines de corrections par version (attesté par le git log : 30+ commits
  sur le seul article Arte, avec vagues de corrections numérotées)
- une relecture à voix haute systématique
- Message : la qualité est le résultat d'un coût assumé, pas d'un prompt.
- Répond indirectement à : « combien de temps ? » et « comment tu vérifies tout ? ».

### Fermeture — la traçabilité comme garantie

- Le processus complet est conservé dans un dépôt de versionnement :
  chaque version, chaque correction, chaque audit, chaque source.
- La mémoire capitalise : en plus des fichiers, tout est indexé dans la mémoire du
  système (39 345 entrées indexées au 2026-08-01, dont 714 fichiers d'enquête dans
  le dépôt). Chaque nouvelle enquête enrichit les suivantes.
- De n'importe quelle phrase d'un article, on remonte jusqu'au fait, puis à la source.
- Tout est libre de droit, récupérable, citable.
- Punchline possible : « L'Empire du Mensonge exige une Immunité Cognitive. »

---

## Vérification des chiffres (page About vs dépôt) — audit 2026-08-01

| Chiffre | Page About | Vérification dépôt | Statut |
|---------|-----------|--------------------|--------|
| 148 concepts | oui | DSL.md le déclare ; recompte partiel : 40 symboles (15+8+17) + 10-17 patterns + 16 menaces. Non reproductible exactement. | ⚠️ déclaration interne |
| 15 symboles narratifs | oui (étape 1) | SYMBOLS.md §1 : 15 | ✅ confirmé |
| 9 patterns | oui (étape 1) | PATTERNS.md : 10 définitions §1, 17 @PAT[] uniques dans le fichier | ⚠️ écart 9 vs 10-17 |
| 5 familles rhétoriques | oui (étape 1) | DEM/BF/NUM/AUTH/FAC (KERNEL §0) | ✅ confirmé |
| 16 clusters | oui | 15 fichiers de cluster réels (+ _INDEX + _TEMPLATE = 17 fichiers) ; plan Arte dit « 17 clusters » | ⚠️ écart 15/16/17 |
| 19 protocoles d'investigation | oui | protocol/ : 2 fichiers (INVESTIGATION, PERSO_FRESQUE) ; aucune trace « 19 protocoles » dans le dépôt | ❌ non vérifiable |
| 105 enquêtes en six semaines | oui | 714 fichiers `*_INVESTIGATION.md` dans investigations/ ; INDEX.md déclare 261 dossiers | ⚠️ non recoupé exactement |
| 2,9 millions de mots | oui | non comptabilisé dans le dépôt ; draft About (substack-online/) dit « 3,2 millions » | ⚠️ contradiction interne |
| 117 articles / 8 mois | commentaire | draft About dit « 116 articles » ; articles/ contient 67 fichiers `*_ARTICLE.md` | ⚠️ écart 116/117/67 |
| 80 % cinq entreprises | oui (constat) | déclaration d'auteur, pas sourcée dans le dépôt | ⚠️ déclaration publique |
| 25 enquêtes (article Arte) | commentaire | dossier axe-chine-russie-iran : 19 INVESTIGATION + 19 quintessences | ❌ 25 non confirmé, 19 documenté |
| 19 sources (article Arte) | commentaire | README du dossier : 32 sources | ⚠️ écart 19 vs 32 |
| 16-30 h par article | commentaire | non vérifiable dans le dépôt | ⚠️ à reconfirmer |
| 39 345 entrées mémoire | non | get_memory_health (MCP, 2026-08-01) | ✅ vérifié (mais inclut doublons + tests + conversations) |
| 4 764 entrées « investigation » | non | MCP ; mais doublons et entrées de test observés ; 714 fichiers réels | ⚠️ ne pas présenter comme enquêtes distinctes |
| 94 quintessences, 50 articles | non | get_memory_health (MCP, 2026-08-01) | ✅ vérifié (entrées de mémoire) |
| 5 modèles d'audit (Ollama) | non | tools/engines/auditor/README.md : phi4-mini 3.8B, qwen3:8b, granite3.2:8b | ✅ vérifié |
| Buffy = deepseek-v4-pro, Theo = Gemini | non | audit_antagoniste_blueprint.md (2026-07-31) | ✅ vérifié |

**Règle d'usage pour le texte** : les chiffres ✅ peuvent être cités avec leur
mesure exacte. Les chiffres ⚠️ doivent être soit évités, soit présentés comme
« publiés sur cette page » (recyclage, pas assertion nouvelle), soit attribués
explicitement (« le dépôt compte 19 enquêtes », « la mémoire indexe 39 345 entrées »).
Les ❌ sont à éviter. Toute nouvelle assertion chiffrée doit d'abord être vérifiée
dans le dépôt, comme le ferait l'enquête elle-même.

---

## Non-retenus (explicitement)

- Réponse directe au commentaire « écriture IA innommable » (silence sur les critiques)
- Le constat développé (80 %, ressource cognitive) : déjà sur la page, le texte
  pédagogique n'a pas à le répéter
- Liste exhaustive des 148 concepts : 3-4 symboles traduits suffisent
- Approche narrative inversée (autopsie remontante) : trop forensique pour un objectif didactique
- Approche thématique par risques : le pipeline complet doit apparaître frontalement
