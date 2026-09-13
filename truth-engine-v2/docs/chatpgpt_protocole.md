VISION.md, puis PFD.md (project foundation requirement). le but, le besoin doit être clair et limpide. Expliquer, se préparer est plus important que comment faire.
Analysé
from pathlib import Path
from textwrap import dedent

base = Path("/mnt/data/article_protocol_foundation")
base.mkdir(parents=True, exist_ok=True)

vision = dedent(r"""
# VISION.md

# Vision du protocole Article from Truth Engine

**Statut : document fondateur**  
**Objet : fixer le pourquoi avant le comment**  
**Portée : indépendante de toute architecture, version, phase, gate, schéma ou implémentation**

---

## 1. Raison d'être

Truth Engine produit des **investigations**.

Ces investigations ne sont pas de simples collections de faits vérifiés. Elles cherchent à reconstruire un objet réel : son histoire, son fonctionnement, ses acteurs, ses relations, ses flux, ses mécanismes, ses anomalies, ses contradictions, ses zones d'ombre, ses hypothèses concurrentes, ce qui résiste à la réfutation et ce qui reste inconnu.

Le protocole Article existe pour une seule raison :

> **Transformer ce travail d'enquête en un article qui transmet au lecteur ce que l'enquête a réellement permis de comprendre, sans en perdre la profondeur, sans inventer ce qu'elle ne démontre pas, et sans réduire la découverte à une succession de claims prudents.**

Il ne doit pas devenir un second Truth Engine.  
Il ne doit pas refaire l'enquête.  
Il ne doit pas remplacer l'auteur par un moteur de conformité.  
Il ne doit pas optimiser la traçabilité au détriment de la compréhension.

Sa fonction est un passage difficile :

```text
INVESTIGATION RICHE
        ↓
COMPRÉHENSION DE CE QUI A ÉTÉ DÉCOUVERT
        ↓
DÉCISION D'AUTEUR
        ↓
ARTICLE

La valeur du protocole se mesure à la qualité de ce passage.

2. Les trois mondes qu'il doit relier
2.1 Truth Engine : la connaissance produite par l'enquête

Truth Engine est l'amont.

Il explore, diverge, relie, vérifie, falsifie, date, hiérarchise les preuves et conserve les inconnues.

Sa production contient deux choses inséparables :

la preuve : ce qui autorise ou interdit une affirmation ;
l'intelligence de l'enquête : ce que l'accumulation des recherches a fait apparaître.

Le protocole Article doit préserver les deux.

Préserver uniquement la preuve produit un article exact mais pauvre.
Préserver uniquement l'intuition produit un article fort mais fragile.

Le but est de conserver la découverte sous contrainte de preuve.

2.2 Le corpus Substack : l'édifice éditorial cumulatif

Un nouvel article n'est pas écrit dans le vide.

Le corpus Substack constitue une mémoire éditoriale de ce qui a déjà été :

expliqué ;
démontré ;
conceptualisé ;
nommé ;
relié ;
publié.

Il n'est pas automatiquement une preuve du nouveau dossier. Il sert d'abord à répondre à une autre question :

Qu'est-ce que ce nouvel article apporte qu'un lecteur assidu ne sait pas déjà ?

Le protocole doit empêcher deux échecs symétriques :

répéter sous une nouvelle forme ce que l'édifice a déjà établi ;
ignorer l'édifice et produire un article intellectuellement isolé.

Chaque article doit donc être une pierre nouvelle de l'édifice, pas un résumé autonome interchangeable.

2.3 Le lecteur : destination réelle du travail

Le protocole n'écrit pas pour ses propres artefacts.

Il écrit pour un lecteur cultivé, exigeant, parfois déjà familier du corpus.

Ce lecteur doit pouvoir sortir de l'article en disant :

je comprends maintenant ce qu'est réellement cet objet ;
je comprends comment il fonctionne ;
je comprends comment il s'est constitué ou transformé ;
je vois les acteurs, les flux et les mécanismes qui comptent ;
j'ai découvert quelque chose que je ne savais pas ;
je distingue ce qui est établi de ce qui reste incertain ;
je vois pourquoi cela mérite mon attention.

Un article qui ne produit pas ce déplacement cognitif est un échec, même si chaque phrase est correctement sourcée.

3. L'unité de valeur : la découverte transmissible

Le protocole ne doit pas prendre le claim comme unité fondamentale de l'article.

Le claim est une unité de contrôle probatoire.

L'unité éditoriale fondamentale est la découverte transmissible.

Une découverte transmissible peut être :

un fait inattendu ;
une histoire inconnue ;
une chronologie qui change la compréhension ;
un mécanisme ;
une contradiction ;
une faille ;
un changement d'échelle ;
une relation entre acteurs ;
un flux financier ou matériel ;
un effet de bord ;
une asymétrie ;
un paradoxe ;
une absence documentée qui compte réellement ;
une hypothèse forte restant ouverte ;
la réfutation d'une intuition initiale ;
une question devenue plus précise grâce à l'enquête.

Elle peut mobiliser plusieurs claims et plusieurs sources.

Les claims bornent la découverte. Ils ne la remplacent pas.

4. L'objet avant l'angle

Avant toute thèse, l'article doit comprendre ce dont il parle.

Pour un objet concret ou institutionnel, cela implique selon le sujet :

sa fonction ;
son histoire ;
son fonctionnement quotidien ;
ses entrées et ses sorties ;
ses utilisateurs ;
ses règles ;
ses ressources ;
ses coûts ;
ses acteurs ;
ses infrastructures ;
ses contrats ;
ses flux matériels, financiers ou informationnels ;
les contraintes qui l'ont façonné ;
les problèmes qu'il résout ;
les problèmes qu'il crée ou déplace.

Un article sur les déchèteries qui ne raconte ni les déchets, ni les poubelles, ni la collecte, ni ce qui entre et sort d'une déchèterie, ni pourquoi cet équipement existe, a raté son objet avant même de discuter badges ou quotas.

Le protocole doit donc protéger cette règle :

Aucune sophistication analytique ne compense une mauvaise compréhension de l'objet.

5. La quintessence est une fonction, pas un format

Entre l'investigation et l'article existe un besoin irréductible :

extraire ce que chaque enquête contient de matériel pour la compréhension future, avant de décider ce qui sera écrit.

Cette opération est la quintessence.

Son rôle n'est pas de résumer court.
Son rôle est de préserver la matière intellectuellement utile.

Elle doit notamment empêcher la disparition prématurée de :

faits secondaires qui prendront du sens plus tard ;
chronologies ;
acteurs ;
citations ;
mécanismes ;
pistes réfutées ;
contradictions ;
anomalies ;
négative knowledge ;
surprises ;
liens entre dossiers ;
éléments incarnés ou narrativement puissants.

Le tri éditorial vient après.

On ne peut pas sélectionner intelligemment ce qui a déjà été perdu.

6. L'article est un acte d'auteur

Une enquête ne devient pas un article par assemblage mécanique.

Quelqu'un doit décider :

quel est le vrai sujet ;
ce que le lecteur croit savoir au départ ;
ce que l'enquête permet de lui faire découvrir ;
quelle tension organise le récit ;
quels faits sont les plus révélateurs ;
quels mécanismes sont centraux ;
ce qui doit être expliqué avant le reste ;
ce qui mérite une scène, un exemple, un chiffre ou une figure ;
ce qui doit être coupé ;
où l'article bascule ;
quelle conclusion est réellement acquise.

Cette décision ne doit pas être prise implicitement par le modèle au fil de la rédaction.

Elle doit être explicite avant l'écriture.

Le protocole doit préparer l'auteur à écrire, pas écrire à sa place par inertie.

7. La méthode inverse

L'article part du concret.

Il ne commence pas par un cadre théorique qui cherche ensuite des exemples.

Il part :

d'un objet ;
d'un fait ;
d'un dysfonctionnement ;
d'une anomalie ;
d'un document ;
d'un chiffre ;
d'une scène ;
d'une contradiction observable.

Puis il remonte.

CE QUE LE LECTEUR PEUT VOIR
        ↓
CE QUI SE PASSE
        ↓
COMMENT CELA FONCTIONNE
        ↓
POURQUOI CELA FONCTIONNE AINSI
        ↓
ACTEURS / RÈGLES / FLUX / INCITATIONS
        ↓
MÉCANISME
        ↓
PORTÉE RÉELLE

Le mécanisme doit émerger de l'enquête. Il ne doit jamais être plaqué depuis le catalogue mental du LLM.

8. Nouveauté obligatoire

L'existence d'un dossier Truth Engine ne justifie pas automatiquement un article.

Avant rédaction, une question doit être résolue :

Quel est l'apport nouveau ?

L'apport peut être :

un fait inédit dans le corpus publié ;
une donnée nouvelle ;
une relation jusque-là invisible ;
une mécanique enfin reconstituée ;
un ancien mécanisme observé dans un nouvel objet ;
une réfutation importante ;
un changement de degré devenu changement de nature ;
une synthèse qui relie des éléments auparavant séparés ;
une meilleure question lorsque la réponse reste inaccessible.

Si aucun apport nouveau substantiel n'existe, le bon résultat peut être :

ne pas écrire d'article.

9. La conclusion doit payer la promesse

La conclusion n'est pas un résumé prudent des limites.

Elle répond à la question que l'article a construite.

Elle doit :

dire ce que l'enquête change réellement dans notre compréhension ;
formuler la portée exacte de cette découverte ;
nommer ce qui ne peut pas encore être conclu ;
laisser, lorsque le sujet l'exige, une question plus forte que celle du départ.

Une conclusion du type « il faut davantage de données » n'est acceptable que si l'absence de données est elle-même la découverte centrale.

Sinon, elle signale que l'article n'a pas trouvé sa raison d'être.

10. Ce que le protocole ne doit jamais optimiser en premier

Le protocole peut avoir des contrôles, des IDs, des hashes, des gates, des matrices et des artefacts.

Aucun n'est la finalité.

Il est en échec si le LLM consacre plus d'attention à :

satisfaire un schéma ;
maintenir des compteurs ;
remplir des CSV ;
obtenir un PASS ;
préserver une architecture interne ;
prouver que chaque transition a un identifiant ;

qu'à :

comprendre l'objet ;
extraire la quintessence des enquêtes ;
identifier les découvertes ;
trouver la nouveauté ;
reconstruire les mécanismes ;
organiser l'explication ;
produire une pensée transmissible.

La conformité doit protéger le raisonnement. Elle ne doit jamais devenir son substitut.

11. Invariants de vision

Ces invariants doivent survivre à toute future implémentation.

V1. Truth Engine est l'amont souverain de l'enquête

Le protocole Article ne remplace pas Truth Engine.

V2. Investigation != article

Un article est une transformation intellectuelle, pas un export.

V3. Preuve != découverte

La preuve borne ce qui peut être dit. La découverte détermine ce qui mérite d'être raconté.

V4. Claims != pensée

Les claims sont nécessaires à la rigueur, insuffisants à l'intelligence éditoriale.

V5. Quintessence avant sélection

Aucune matière potentiellement signifiante ne doit être supprimée avant extraction de sa valeur.

V6. Objet avant thèse

Le sujet doit être compris dans son fonctionnement réel avant d'être interprété.

V7. Nouveauté avant publication

Un article doit ajouter quelque chose au corpus publié.

V8. Corpus Substack = continuité éditoriale, pas preuve par défaut

Il évite la répétition et permet la cumulativité.

V9. Le lecteur est la destination

La complexité interne doit disparaître de l'expérience de lecture.

V10. Rigueur sans stérilisation

L'incertitude doit calibrer la phrase, pas supprimer les découvertes solides autour d'elle.

V11. L'auteur décide

Angle, hiérarchie, arc et conclusion exigent une décision consciente fondée sur le matériau.

V12. KISS est une contrainte cognitive

Toute mécanique qui ne protège ni vérité, ni matière, ni décision d'auteur, ni qualité lecteur doit être suspectée d'être inutile.

12. Définition ultime du succès

Le protocole réussit lorsqu'il permet de passer de dizaines d'heures d'enquête à un article dans lequel :

la richesse du travail sous-jacent est perceptible sans être visible comme bureaucratie ;
le lecteur comprend mieux le monde après lecture qu'avant ;
le lecteur assidu du corpus apprend réellement quelque chose ;
les découvertes importantes de Truth Engine sont reconnaissables dans le texte ;
les limites de preuve empêchent l'exagération sans neutraliser l'enquête ;
la narration naît de la matière plutôt que des habitudes statistiques du LLM ;
l'article s'insère naturellement dans l'édifice Substack et le fait avancer.

La phrase de contrôle est simple :

Le protocole ne sert pas à fabriquer un article conforme. Il sert à ne pas perdre l'enquête en devenant un article.
""").strip() + "\n"

pfd = dedent(r"""

PFD.md
Project Foundation Requirements

Projet : protocole de transformation des investigations Truth Engine en articles Substack
Statut : exigences fondatrices
Objet : définir le besoin et les conditions de réussite avant toute architecture

1. Problème à résoudre

Truth Engine peut produire un corpus d'investigations très riche.

Cette richesse crée un problème spécifique : le passage à l'article.

Sans dispositif approprié, plusieurs pertes surviennent :

compression trop précoce ;
réduction des enquêtes à des claims ;
disparition de l'histoire de l'objet ;
perte des acteurs, flux, mécanismes, anomalies et surprises ;
sélection opérée avant compréhension globale ;
lissage des tensions pour obtenir un texte prudent ;
répétition de ce que le corpus Substack a déjà publié ;
rédaction pilotée par les habitudes génériques du LLM ;
conclusion bornée mais vide ;
multiplication de contrôles internes qui donnent une illusion de qualité.

Le projet doit résoudre ce problème de transmission sous contrainte.

2. Besoin utilisateur fondamental

L'utilisateur doit pouvoir fournir un ensemble d'investigations Truth Engine et obtenir, après préparation et décision éditoriale, un article qui :

transmet la quintessence intellectuelle du travail d'enquête ;
raconte réellement le sujet, pas seulement la question initiale ;
apporte une connaissance nouvelle à un lecteur exigeant ;
s'insère dans le corpus Substack existant sans le répéter ;
distingue naturellement faits, inférences, hypothèses et inconnues ;
reste traçable jusqu'aux investigations et sources ;
est agréable, dense et compréhensible à lire ;
peut être refusé si la matière ne justifie pas un article.
3. Contrat fondamental
Entrée

Un ou plusieurs résultats d'investigations Truth Engine, éventuellement accompagnés de :

leurs sources ;
leurs registres de faits ;
leurs traces Mnemolite ;
leurs artefacts de recherche ;
des investigations antérieures du même sujet.

Le corpus Substack existant est également disponible comme mémoire éditoriale.

Sortie

Un article publiable qui constitue une nouvelle contribution à l'édifice éditorial.

La sortie attendue n'est pas :

un rapport d'audit ;
un résumé des investigations ;
une matrice de claims ;
une note de synthèse administrative ;
un cours introductif générique.
Résultat attendu

Le lecteur comprend :

l'objet + son fonctionnement + son histoire pertinente + les découvertes + les mécanismes + les problèmes/failles + leur portée + les limites.

4. Séparation des responsabilités
FR-01 — Truth Engine enquête

Le protocole Article MUST considérer les investigations Truth Engine comme la matière amont autoritaire sur ce qui a été recherché, découvert, réfuté ou laissé ouvert.

Il MUST NOT se substituer à Truth Engine par défaut.

Une nouvelle investigation n'est demandée que lorsqu'une lacune matérielle identifiée empêche réellement l'article de répondre à une question nécessaire.

FR-02 — Le protocole préserve avant de sélectionner

Avant toute décision éditoriale, le système MUST disposer d'une représentation suffisamment riche de chaque investigation pour que :

faits ;
acteurs ;
chronologie ;
sources ;
citations ;
mécanismes ;
anomalies ;
contradictions ;
hypothèses ;
réfutations ;
inconnues ;
surprises ;
détails potentiellement narratifs ;

restent récupérables.

Critère de défaillance : une donnée importante existait dans l'investigation mais ne peut plus être retrouvée au moment de décider l'article.

FR-03 — Les claims restent un sous-système probatoire

Le système MAY utiliser des claims pour :

la traçabilité ;
le niveau de preuve ;
l'audit ;
la prévention des upgrades.

Mais il MUST NOT utiliser la matrice de claims comme représentation suffisante du contenu intellectuel d'une investigation.

Règle :

ARTICLE_MATERIAL > CLAIM_SET

au sens où la matière éditoriale comprend des structures que des claims atomiques ne représentent pas correctement.

5. Compréhension obligatoire du sujet
FR-04 — Object model

Avant de concevoir l'article, le système MUST pouvoir expliquer le sujet en langage simple.

Pour un objet concret/institutionnel, il SHOULD être capable de répondre selon pertinence à :

Qu'est-ce que c'est ?
À quoi cela sert-il ?
Pourquoi cela existe-t-il ?
Comment cela fonctionne-t-il concrètement ?
Qu'est-ce qui entre ?
Qu'est-ce qui sort ?
Qui l'utilise ?
Qui le gère ?
Qui paie ?
Quelles règles s'appliquent ?
Quels flux y circulent ?
Quels acteurs en dépendent ?
Comment cet objet a-t-il évolué ?
Où sont ses frontières ?
Que se passe-t-il en dehors de ces frontières ?

Le nombre de questions n'est pas un quota. La couverture dépend du sujet.

BLOCKER : si le système ne peut pas expliquer l'objet, aucune thèse éditoriale ne doit être figée.

FR-05 — Context before anomaly

Le système MUST distinguer :

NORMAL_FUNCTION
vs
OBSERVED_ANOMALY

Une anomalie n'est compréhensible que par rapport au fonctionnement ordinaire de l'objet.

Exemple générique : un quota n'a de sens qu'après compréhension du service auquel il limite l'accès.

6. Extraction de la valeur des investigations
FR-06 — Investigation essence

Pour chaque investigation, le système MUST pouvoir répondre :

Qu'a-t-elle réellement cherché ?
Qu'a-t-elle découvert ?
Qu'a-t-elle réfuté ?
Qu'a-t-elle rendu plus probable ?
Qu'a-t-elle rendu moins probable ?
Quelle pièce nouvelle apporte-t-elle ?
Quel mécanisme éclaire-t-elle ?
Quelle surprise contient-elle ?
Quelle citation ou scène incarne son apport ?
Quelle inconnue importante laisse-t-elle ?

Cette étape MUST précéder la hiérarchisation éditoriale.

FR-07 — Discovery inventory

Avant le design d'article, le projet MUST disposer d'un inventaire des découvertes candidates.

Une découverte candidate n'est pas tenue de correspondre à un claim unique.

Chaque découverte SHOULD pouvoir être reliée à :

investigations sources ;
preuves qui la soutiennent ;
niveau de certitude ;
portée ;
éventuels contradicteurs ;
valeur de nouveauté ;
valeur explicative ;
valeur narrative.

Le format n'est pas prescrit par ce PFD.

FR-08 — Preserve negative knowledge

Le projet MUST préserver ce que Truth Engine a cherché sans le trouver, lorsque cette absence est matériellement informative.

Il MUST distinguer :

NOT_FOUND_IN_SEARCH
!=
PROVEN_ABSENT

La connaissance négative ne doit ni disparaître, ni devenir artificiellement la conclusion centrale.

7. Relation au corpus Substack
FR-09 — Corpus mapping

Avant de décider qu'une découverte mérite d'être publiée, le système MUST vérifier son rapport avec le corpus Substack.

Pour chaque axe éditorial candidat, il doit distinguer :

ALREADY_ESTABLISHED
ALREADY_EXPLAINED_BUT_NEW_EVIDENCE
NEW_INSTANCE_OF_EXISTING_MECHANISM
NEW_RELATION
NEW_MECHANISM
NEW_FACT
NEW_SYNTHESIS
CONTRADICTION_WITH_PRIOR_CORPUS
ACTUALISATION
NO_MATERIAL_NOVELTY

L'objectif n'est pas de multiplier les catégories, mais d'empêcher la répétition involontaire.

FR-10 — Novelty gate

Un article MUST NOT passer en rédaction longue si son apport nouveau n'est pas formulable clairement.

La question minimale est :

« Après lecture, qu'est-ce qu'un lecteur régulier du corpus saura ou comprendra qu'il ne savait pas avant ? »

Si la réponse est faible ou générique, le résultat attendu SHOULD être :

compléter l'enquête ;
fusionner avec un autre sujet ;
écrire une note courte ;
ou ne rien publier.
8. Décision éditoriale avant rédaction
FR-11 — Author decision

Avant prose longue, le système MUST produire une décision d'auteur portant au minimum sur :

sujet réel ;
mode éditorial ;
apport nouveau ;
tension principale ;
découverte centrale ;
thèse ou thèse organisatrice ;
progression cognitive du lecteur ;
éléments indispensables ;
éléments volontairement coupés ;
conclusion probable ;
question qui reste ouverte.

Cette décision doit provenir du matériau.

Elle ne doit pas être inférée au fil de la rédaction.

FR-12 — Article mode

Le système MUST distinguer au moins conceptuellement :

ESSAI
Un mécanisme ou une thèse domine. Sélection forte.

ENQUÊTE
Le sujet lui-même est l'objet. Plusieurs dimensions doivent être orchestrées pour le faire comprendre.

Le système MUST NOT forcer un sujet de type « institution / objet / système » dans un article étroit si les investigations montrent que sa compréhension exige plusieurs dimensions.

FR-13 — Cognitive arc

Le plan MUST être évalué comme une progression de compréhension, pas comme une taxonomie.

Chaque section doit répondre à :

« Qu'est-ce que le lecteur comprend après cette section qu'il ne pouvait pas encore comprendre avant ? »

Une section qui ne modifie pas la compréhension SHOULD être supprimée, fusionnée ou déplacée.

9. Exigences de contenu de l'article
FR-14 — Explain the object

L'article final MUST permettre à un lecteur non spécialiste mais cultivé de comprendre l'objet sans connaissance préalable artificiellement supposée.

FR-15 — Show the investigations

Le lecteur ne doit pas voir la cuisine interne, mais il doit sentir qu'une enquête a eu lieu.

Cela passe par :

documents précis ;
chiffres signifiants ;
histoires ;
acteurs ;
contradictions ;
découvertes ;
détails concrets ;
traces de recherches difficiles ;
pistes qui se ferment ;
mécanismes reconstitués.

Un article qui pourrait être écrit avec une recherche Web superficielle est un signal d'échec lorsque Truth Engine a produit un corpus profond.

FR-16 — Material problems and failures

Lorsque les investigations identifient des failles matérielles, l'article MUST les traiter.

Il ne doit pas les neutraliser sous des formulations vagues du type :

« la situation est complexe » ;
« les données sont limitées » ;
« différentes approches existent ».

La calibration probatoire change le verbe, pas l'importance du sujet.

FR-17 — Mechanism over catalogue

L'article SHOULD préférer l'explication des mécanismes à l'accumulation de cas.

Un cas sert à :

établir ;
incarner ;
comparer ;
réfuter ;
montrer une variation.

Il ne doit pas devenir une liste décorative.

FR-18 — Concrete flows

Lorsqu'un sujet implique des flux, l'article SHOULD les suivre autant que le corpus le permet.

Types de flux :

matière ;
argent ;
information ;
responsabilité ;
décision ;
contrat ;
données ;
déchets ;
personnes.

Une frontière est souvent mieux comprise par ce qui la traverse ou ce qu'elle rejette.

10. Exigences de vérité
FR-19 — Evidence calibration

Le langage MUST refléter le niveau réel de preuve.

Le système MUST empêcher notamment :

RELATION -> INFLUENCE
CORRELATION -> CAUSATION
CASE -> PREVALENCE
EXISTENCE -> TREND
BENEFIT -> INTENT
NOT_FOUND -> ABSENT
SUSPICION -> FACT
FR-20 — No sterilization

La prudence MUST NOT devenir une stratégie d'évitement.

Si une découverte est solidement établie, le système doit autoriser une formulation claire et forte.

Trop prudent est un défaut au même titre que trop affirmatif.

FR-21 — Counter-hypothesis

Toute thèse matérielle SHOULD être confrontée à la meilleure explication concurrente réellement supportée.

Le but n'est pas l'équilibre rhétorique.

Le but est de savoir ce qui résiste.

11. Exigences de conclusion
FR-22 — Conclusion value

La conclusion MUST apporter une réponse ou une transformation cognitive.

Elle ne doit pas seulement :

répéter les sections ;
réciter les limites ;
appeler à davantage de recherches ;
reformuler la question initiale.

Elle doit formuler :

WHAT_CHANGED_IN_OUR_UNDERSTANDING
+
WHAT_IS_REALLY_AT_STAKE
+
BOUNDARY_OF_THE_CONCLUSION
FR-23 — Strong ending

Une conclusion MAY rester ouverte, mais la question finale doit être plus précise et plus profonde que la question initiale.

Si l'enquête ne permet aucune progression de ce type, le projet doit questionner la justification même de l'article.

12. Exigences de lecture
NFR-01 — Densité utile

Chaque passage doit justifier son coût cognitif.

Le texte doit être dense en information, pas dense en jargon.

NFR-02 — Reader comfort

Le lecteur ne doit jamais payer la complexité interne du pipeline.

La prose doit expliquer simplement sans simplifier l'épistémologie.

NFR-03 — Incarnation

Un article d'enquête SHOULD contenir suffisamment d'éléments concrets pour éviter l'abstraction continue :

lieux ;
objets ;
personnes ;
dates ;
documents ;
chiffres contextualisés ;
gestes ;
flux.
NFR-04 — Figures only when useful

Une figure, carte, tableau ou schéma n'existe que s'il réduit réellement le coût de compréhension ou révèle une structure difficile à voir en prose.

Aucune figure n'est obligatoire.

NFR-05 — French editorial quality

Le texte publié doit être du français naturel, soutenu, précis, sans jargon interne ni tics de LLM.

13. Exigences de simplicité du projet
NFR-06 — KISS

Une phase, un artefact ou un contrôle n'est justifié que s'il protège au moins un des éléments suivants :

vérité ;
matière d'enquête ;
décision éditoriale ;
nouveauté ;
compréhension du lecteur ;
non-régression.

Sinon, il est candidat à suppression.

NFR-07 — DRY

La même information ne doit pas être transformée successivement dans plusieurs artefacts sans gain cognitif clair.

Chaque transformation est une surface possible de perte.

NFR-08 — YAGNI

Le projet ne doit pas prévoir des mécanismes génériques pour des problèmes non observés.

Les protections doivent naître d'échecs réels et rester proportionnées.

NFR-09 — Human checkpoints are semantic

Une validation humaine ne doit pas demander :

« le CSV est-il correct ? »

Elle doit permettre de répondre à des décisions réelles :

est-ce bien le sujet ?
est-ce la découverte ?
est-ce nouveau ?
est-ce l'histoire qu'il faut raconter ?
est-ce que la conclusion vaut l'article ?
14. Critères d'acceptation du projet

Le protocole n'est pas considéré comme réussi parce que ses tests internes passent.

Il est réussi si, sur un replay à partir d'investigations réelles :

AC-01 — Object comprehension

Un lecteur-test peut expliquer correctement ce qu'est l'objet, à quoi il sert et comment il fonctionne.

AC-02 — Investigation retention

Les principales découvertes des investigations sont reconnaissables dans l'article ou explicitement écartées pour une raison éditoriale.

AC-03 — Novelty

Au moins un apport nouveau substantiel par rapport au corpus Substack est identifiable.

AC-04 — Mechanism

Le lecteur comprend au moins le ou les mécanismes centraux, pas seulement des exemples.

AC-05 — Problems

Les failles ou problèmes matériels identifiés par l'enquête sont visibles à leur juste importance.

AC-06 — Epistemic integrity

Aucune conclusion matérielle n'excède les preuves.

AC-07 — Non-sterilization

Les conclusions fortes réellement supportées ne sont pas affaiblies par prudence générique.

AC-08 — Cognitive progression

Le lecteur arrive à une compréhension qualitativement différente de celle du début.

AC-09 — Corpus continuity

L'article sait ce que l'édifice Substack a déjà expliqué et ne le répète pas inutilement.

AC-10 — Editorial value

Un lecteur assidu et pointu peut identifier ce que l'article lui apporte.

AC-11 — Readability

La complexité du travail d'enquête n'apparaît pas sous forme de bureaucratie ou de jargon.

AC-12 — Honest refusal

Le système sait conclure : « la matière ne justifie pas encore un article ».

15. Anti-critères : faux signaux de réussite

Les éléments suivants ne suffisent jamais à déclarer le projet réussi :

100 % de claims tracés ;
0 P0/P1/P2 internes ;
100 % de couverture d'un ledger ;
tous les fichiers hashés ;
toutes les transitions classées ;
article grammaticalement correct ;
toutes les sources publiques ;
conclusion prudente ;
absence d'hallucination.

Ils sont utiles comme protections locales.

Ils ne mesurent pas la finalité.

16. Test ultime

Avant de considérer une future version du protocole comme candidate, la tester sur un corpus réel et poser cinq questions à froid :

Ai-je appris quelque chose ?
Ai-je compris l'objet ?
Ai-je vu ce que les enquêtes ont découvert ?
Cet article apporte-t-il réellement quelque chose au corpus existant ?
Aurais-je pu obtenir presque le même texte sans plusieurs jours d'investigations Truth Engine ?

Si la réponse à la cinquième question est oui, le protocole a échoué.

17. Baseline fondatrice

Le projet repart de cette équation :

TRUTH_ENGINE
    = découvrir et éprouver

QUINTESSENCE
    = ne pas perdre

CORPUS_SUBSTACK
    = savoir ce qui existe déjà

DÉCISION_D'AUTEUR
    = choisir ce qui mérite d'être raconté et pourquoi

ARTICLE
    = transmettre une compréhension nouvelle

AUDIT
    = empêcher que cette transmission mente ou perde une découverte matérielle

L'ordre est important.

L'audit protège le produit. Il n'est pas le produit.
""").strip() + "\n"

(base/"VISION.md").write_text(vision, encoding="utf-8")
(base/"PFD.md").write_text(pfd, encoding="utf-8")

Minimal foundation index, not another design doc.

readme = dedent("""

Article Protocol Foundation

Ces deux documents précèdent toute nouvelle modification du protocole.

VISION.md : pourquoi le projet existe, ce qu'il doit préserver, ce qu'est le succès.
PFD.md : besoins et exigences fondatrices, indépendamment de l'implémentation.

Aucune architecture cible n'est définie ici.
""").strip() + "\n"
(base/"README.md").write_text(readme, encoding="utf-8")

print(base/"VISION.md")
print(base/"PFD.md")

STDOUT/STDERR
/mnt/data/article_protocol_foundation/VISION.md
/mnt/data/article_protocol_foundation/PFD.md

Analysé
from pathlib import Path
import hashlib, zipfile

base = Path("/mnt/data/article_protocol_foundation")

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

manifest = []
for name in ["VISION.md", "PFD.md", "README.md"]:
    p = base / name
    manifest.append(f"{sha256(p)}  {name}")

(base / "SHA256SUMS.txt").write_text("\n".join(manifest) + "\n", encoding="utf-8")

zip_path = Path("/mnt/data/ARTICLE_PROTOCOL_FOUNDATION_RESET_2026-09-02.zip")
with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for p in sorted(base.iterdir()):
        if p.is_file():
            z.write(p, arcname=f"ARTICLE_PROTOCOL_FOUNDATION/{p.name}")

print("VISION SHA256:", sha256(base/"VISION.md"))
print("PFD SHA256:", sha256(base/"PFD.md"))
print("ZIP SHA256:", sha256(zip_path))
print(zip_path)

STDOUT/STDERR
VISION SHA256: 2de9a5bc78a5384bc3fe7118ec1e4228725c9e33c7970c306e0e0b8d8b2eb204
PFD SHA256: e9e1f85737982224d2e2d70719357c0134d37590f901702a8d49647d31b7dcc0
ZIP SHA256: 140cd0f1d760bc434b4e59c3e4f72b81985e1bd9bd64eb334d69877cb1aa418f
/mnt/data/ARTICLE_PROTOCOL_FOUNDATION_RESET_2026-09-02.zip


C’est fait. Aucune ligne du protocole RC.7 n’a été modifiée. J’ai créé une fondation séparée en amont.

Les deux documents repartent de la chaîne correcte :

Truth Engine → préservation de la quintessence → compréhension → nouveauté par rapport au corpus Substack → décision d’auteur → article → audit

Cette orientation est cohérente avec la mission historique de Truth Engine : reconstruire « l’objet réel derrière la proposition », et non seulement vérifier des phrases. Elle restaure aussi la fonction originelle du Sublimator : extraire fidèlement la matière avant tout tri éditorial. Et elle rétablit la séparation essentielle entre raisonnement d’auteur et conformité : l’ancien blueprint disait explicitement qu’un auteur doit réfléchir avant d’écrire et que l’arc doit transformer la compréhension du lecteur.

VISION.md

VISION.md

Il fixe notamment :

Truth Engine comme amont souverain de l’enquête ;
le corpus Substack comme édifice éditorial cumulatif, pas comme preuve par défaut ;
le lecteur comme destination réelle ;
la découverte transmissible, et non le claim, comme unité de valeur éditoriale ;
l’objet avant l’angle ;
la quintessence comme fonction de non-perte ;
la nécessité d’une vraie décision d’auteur ;
la méthode inverse ;
la nouveauté obligatoire ;
une conclusion qui doit « payer la promesse » ;
12 invariants de vision.

La phrase fondatrice finale est :

Le protocole ne sert pas à fabriquer un article conforme. Il sert à ne pas perdre l’enquête en devenant un article.

PFD.md

PFD.md

Il transforme la vision en besoins, sans prescrire encore l’architecture.

Il définit notamment :

le problème réel à résoudre ;
le contrat entrée/sortie ;
Truth Engine enquête ;
préserver avant de sélectionner ;
claims = sous-système probatoire, pas représentation suffisante ;
compréhension obligatoire de l’objet ;
extraction explicite de la valeur de chaque investigation ;
inventaire des découvertes candidates ;
préservation de la connaissance négative ;
mapping avec le corpus Substack ;
Novelty Gate ;
décision d’auteur avant rédaction ;
distinction ESSAI / ENQUÊTE ;
progression cognitive du lecteur ;
obligation de faire sentir les enquêtes ;
obligation de traiter les failles matérielles ;
mécanismes plutôt que catalogue de cas ;
suivi des flux ;
rigueur et anti-stérilisation ;
exigences fortes sur la conclusion ;
KISS/DRY/YAGNI ;
12 critères d’acceptation réels.

Le test ultime du PFD est volontairement brutal :

« Aurais-je pu obtenir presque le même texte sans plusieurs jours d’investigations Truth Engine ? »

Si la réponse est oui, le protocole a échoué.

Bundle fondateur

ARTICLE_PROTOCOL_FOUNDATION_RESET_2026-09-02.zip

SHA256 :

140cd0f1d760bc434b4e59c3e4f72b81985e1bd9bd64eb334d69877cb1aa418f

VISION.md SHA256 :

2de9a5bc78a5384bc3fe7118ec1e4228725c9e33c7970c306e0e0b8d8b2eb204

PFD.md SHA256 :

e9e1f85737982224d2e2d70719357c0134d37590f901702a8d49647d31b7dcc0

Persisté séparément dans la Library :

/ARTICLE_WORKFLOW_PROTOCOL_V3_RC_7_2026-09-02/FOUNDATION_RESET_2026-09-02/

Le point important maintenant est de ne pas toucher encore au protocole. La prochaine étape rationnelle est d’attaquer adversarialement VISION.md + PFD.md eux-mêmes : chercher ce qui manque, ce qui est contradictoire, trop abstrait, ou encore contaminé par nos trois jours de dérive. Ensuite seulement on pourra décider ce que le futur protocole doit être, et surtout ce qu’il faut supprimer.