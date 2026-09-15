# Synthèse des dix revues de rôles — masterwork, 2026-09-15

Rapport de passe. Article audité : `01_TARGET/ARTICLE_MASTERWORK_SOUVERAINETE_2026.md`, état d'entrée
`03546068a80bc0c23779bd8aa8230803` (305 lignes, 9 099 mots, 85 entrées de registre).
Sortie de la passe : `3d671c7188644fc648323e2b94002dc4` (305 lignes, 73 306 octets), 16 éditions appliquées.

---

## 0. Ce qui a réellement été exécuté, et ce qui ne l'a pas été

Le mandat était de « spawner des penseurs différents ». L'inventaire des exécutants disponibles est
sans ambiguïté, et il est tracé ici pour qu'on ne refasse pas l'enquête :

| Exécutant | État constaté le 2026-09-15 | Employé ? |
|---|---|---|
| `claude` CLI | installé, mais `Not logged in · Please run /login` | non |
| `opencode` (OpenRouter) | authentifié, mais solde du compte **0,034 $** sur 10 $ consommés | non (un appel Sonnet a été refusé pour crédit) |
| `opencode` (Groq) | authentifié, palier gratuit **8 000 jetons/minute** : un article de 9 099 mots ne passe pas | non |
| `opencode` (NVIDIA NIM) | authentifié, palier gratuit ; seuls **trois** modèles du catalogue répondent encore | **oui, dix rôles** |
| `opencode` (LM Studio) | serveur local éteint (`127.0.0.1:1234` muet) | non |
| `freebuff` CLI | session interactive seulement, pas de mode non interactif | non |

Harnais : `REVIEWS_ROLES_2026-09-15/_harnais_revues.sh`, dix processus détachés (`setsid`), trois modèles
distincts — `nemotron-3-ultra-550b-a55b` (R1, R3, R4, R8), `nemotron-3-super-120b-a12b` (R2, R5, R6, R9),
`nemotron-3.5-lightning-30b-a3b` (R7, R10). Coût : nul. Durée : environ 45 minutes.
**L'article n'a pas été modifié par la passe** : empreinte `03546068…` identique avant et après.

Trois incidents, tous réparés ou tracés :

1. **R2 et R7 n'ont pas écrit leur rapport** (ils l'ont affiché sur la sortie standard). Leurs textes
   intégraux ont été extraits des journaux ; les fichiers portent un en-tête de provenance.
2. **R3 (fact-checker) a été coupé par le délai** après avoir téléchargé vingt et une sources primaires
   dans `/tmp/factcheck_sources/` (BNP/DOJ, Alstom/DOJ, Total, Synergy, CNIL, Trésor IEF, HATVP, Cour
   des comptes). Il a été relancé sur ces sources locales (`PROMPT_R3B_FACT_CHECK_LOCAL.md`) : son
   rapport est arrivé après la rédaction de cette synthèse et est traité en § 7.
3. Le premier harnais (OpenRouter) a été interrompu par le manque de crédit après un seul rôle.

---

## 1. Verdict par rôle

| Rôle | Modèle | Rapport | Apport principal | Verdict de la passe |
|---|---|---|---|---|
| R1 Contradicteur épistémologique | ultra-550b | 30 ko | La définition de « verrou » est plus étroite que son usage ; le statut « lecture » est brandi en méta et absent du corps | **Fort** : un défaut de fond retenu, deux objections partielles, une surestimation |
| R2 Rédacteur en chef | super-120b | 6 ko (journal) | Parties I à V sans clôture, partie V trop méthodologique, figures redondantes | **Faible** : un contresens (le quatrain existe), le reste déjà arbitré |
| R3 Fact-checker | ultra-550b → super-120b | § 7 | Vingt et une sources primaires téléchargées | **En cours** |
| R4 Juriste | ultra-550b | 16 ko | **La seule faute de droit franche de la passe** (DSA art. 22) + 432-11 à deux branches ; six points vérifiés exacts | **Le plus utile** : deux corrections majeur, quatre points à vérifier, aucune erreur ailleurs |
| R5 Auditeur méthodologique | super-120b | 6,5 ko | Critère de réfutation asymétrique ; grille jamais appliquée ; séries non comparables | **Fort** : trois corrections retenues |
| R6 Philosophe du langage | super-120b | 5,8 ko | « dépendances consenties » ; causalité de la ligne 11 | **Moyen** : deux points justes, quatre sur-corrections (« on », « aucune pièce ») |
| R7 Instrumentalisation | lightning-30b | 10 ko | Lignes 54-55 (adjoints communautaires), ligne 13, métaphores | **Moyen** : un arbitrage réel, deux recommandations écartées |
| R8 Avocat du diable | ultra-550b | 12 ko | La thèse inverse est compatible avec tout le corpus ; trois affirmations inattaquables ; cinq corrections qui tueraient sa plaidoirie | **Fort** : aucune édition, un diagnostic de statut |
| R9 Correcteur de français | super-120b | 5,5 ko | Six remarques, dont aucune n'est retenue (voir § 3) | **Faible** : mesures à l'appui, la revue est fausse |
| R10 Lecteur profane | lightning-30b | 18,5 ko | Trente-sept sigles signalés ; le résumé de mémoire et les cinq questions de compréhension | **Moyen** : cinq glosses réelles sur trente-sept signalées |

---

## 2. Les trois objections qui reviennent de rôles indépendants

Ce sont elles qui portent, parce que trois modèles différents, sans se connaître, ont buté sur le
même endroit.

### 2.1 « Des dépendances consenties » (R1, R5, R6)

L'épilogue écrivait : « elle s'asphyxie par des dépendances consenties ». Le mot attribue une intention
au moment même où l'article écrit, quinze lignes plus bas, que « documenter une contrainte structurelle
n'équivaut pas à prouver un acte de coercition intentionnelle ». R5 le dit le plus nettement : l'article
montre que les décisions sont rationnelles sous contrainte, pas qu'elles sont consenties.

**Appliqué** : « elle s'asphyxie par des dépendances **acceptées une par une, et jamais choisies
ensemble** ». La formule ne perd pas la pointe et retrouve l'argument réel de l'article (« Que chaque
décision prise isolément soit rationnelle ne dit rien du choix collectif que personne n'a eu à faire »).

### 2.2 La définition de « verrou » ne couvre pas son usage (R1)

Le prologue définissait le verrou comme « un mécanisme documenté qui réduit la marge de décision d'une
**autorité publique** ». Sur les quatorze lignes de l'inventaire, R1 en compte trois qui échouent au
critère : BNP Paribas et TotalEnergies (entreprises privées) et les signaleurs de confiance. L'ouverture
de la partie I le reconnaissait d'ailleurs à demi-mot : « Lorsqu'un État **ou une entreprise**… ».

**Appliqué** : « un mécanisme **ou un dispositif** documenté qui réduit **une capacité de décision** sans
qu'aucun ordre formel ait été donné : celle d'un État, d'une entreprise stratégique ou d'un espace
public d'information. » La définition adhère maintenant aux quatorze lignes, et elle reprend le mot qui
porte la thèse (« capacité »), au lieu du mot qui la contredisait (« autorité publique »).

### 2.3 Le critère de réfutation n'était pas exécuté dans ses deux volets (R5)

L'épilogue annonçait deux observations décisives : un chaînage organique entre deux verrous « fermerait
la thèse forte », et l'absence d'effet de dépendances comparables « la retirerait ». Le test n'était
appliqué qu'au premier volet (Hugh Bailey), et le second restait déclaratif.

**Appliqué** : « Ce second volet est partiellement instruit plus haut : l'avis d'incompatibilité rendu
par la HATVP en mai 2022 et la résistance lituanienne sont deux cas où la dépendance n'a pas produit
l'effet attendu. Ni l'un ni l'autre ne porte sur la condition d'ensemble, qui est une accumulation et
non une décision. » Le critère est désormais exécuté là où le corpus le permet, et son reste est nommé.

---

## 3. Ce qui est écarté, et sur quelle vérification

Une revue de rôles qui n'est pas recontrôlée fabrique du travail. Chaque objection ci-dessous a été
jugée contre le texte, pas contre son air de vraisemblance.

**R9 (correcteur de français) : six remarques, zéro retenue.**
Ses deux tiers de rapport portent sur les **espaces insécables**. Mesure faite sur le corpus publié :
`0` occurrence d'espace insécable dans neuf fichiers sur onze, `185` et `122` dans deux fichiers
(*déchèteries*, dont un brouillon). La convention maison n'est donc pas l'insécable, et la revue est
sans objet. Ses trois « réécritures de paragraphe » ne modifient, en comparaison différentielle, que des
espaces. Sa remarque 5-6 (« au titre de » n'est pas de la prose) se heurte à l'usage : c'est la formule
de renvoi du droit français, et l'article l'emploie précisément pour citer le régime, pas pour écrire.
Sa remarque 1 (« incohérence terminologique » : « verrou industriel » → « verrou de l'industrie ») est
écartée pour la raison inverse de celle qu'il donne : le jeu canonique est bien un jeu unique — celui des
**domaines** — « l'exécution, l'industrie, la norme et les élites », repris tel quel par le chapô, par
l'incipit de la partie V et par la matrice ; les titres de partie nomment le verrou par son adjectif,
ce qui est une variation, pas une contradiction.

**R10 (lecteur profane) : trente-sept sigles signalés, cinq vérifiés.**
Sa liste est inutilisable telle quelle : elle déclare non définis le DOJ (défini ligne 28, « le
département de la Justice »), le FCPA (« Foreign Corrupt Practices Act américain », ligne 71), le CIRDI,
le TCE, l'EUCS, l'ISOС, le DSA, la HATVP, l'OLAF, tous glosés à leur première occurrence. Les cinq
manques réels, vérifiés un par un : **JCPOA**, **US CLOUD Act**, **ePrivacy**, **IETF**, **SGDSN** —
plus la mention « SGDSN » en clair. C'est ce qui a été corrigé, pas la liste.

**R2 (rédacteur en chef) : son défaut principal est un contresens.**
Il écrit que « l'épilogue omet le quatrain final attendu » et propose d'en insérer un. Les quatre
puces de l'épilogue (lignes 208-211) **sont** le quatrain : il a cherché un poème et n'a pas vu la
strophe en prose. Ses six autres remarques — clôtures manquantes aux parties I à IV, partie V à
déplacer en annexe, figures redondantes — sont des arbitrages déjà rendus dans les passes précédentes,
et deux d'entre eux contre son avis, pour des raisons qui tiennent : les clôtures de parties sont dans
la partie V par construction, et une phrase de synthèse par partie ferait terminer l'article cinq fois.

**R7 : deux recommandations écartées, une laissée à l'auteur.**
La suppression de « la guillotine du dollar » et de « l'artère vitale » a déjà été arbitrée dans un sens
contraire : le chiasme est le seul endroit où l'article montre son mécanisme en une image, et il a été
conservé en connaissance de cause. La ligne 13 (« un complot permanent orchestré par un ordre
clandestin ») est le rebut explicite de la phrase, pas une affirmation. Reste le point des lignes 54-55,
qui n'est pas tranchable par moi : voir § 5.

**R6 : quatre sur-corrections.**
Le « on » des puces finales et le « personne n'a entrepris » de la ligne 213 sont la figure de clôture
de l'article — une anaphore — et les acteurs sont nommés dans le corps. Les trois « aucune pièce » sont
l'idiome du registre, dont la préface définit elle-même le corpus ; ajouter « examinée » trois fois
n'ajoute pas de calibration, seulement de la lourdeur.

**R1 : une de ses quatre objections générales est surestimée.**
Il écrit que « la graduation annoncée des preuves n'est pas appliquée dans le corps, toutes les lignes
recevant la même autorité ». C'est faux sur les faits : le corps borne explicitement les lignes faibles —
Deloitte (« ne démontre ni capture ni contrôle »), agences (« hypothèse non établie »), signaleurs
(« effets non mesurés »), Rockhopper (« le nombre de réformes bloquées n'est pas établi »). Ce qui
manque est une **hiérarchie visible**, pas des bornes ; et cette hiérarchie, la partie V la donne.

**R8 : ses cinq « corrections qui rendraient mon dossier impossible » sont hors périmètre.**
Quatre exigent une mesure nouvelle (taux réel de blocage sur l'ensemble des opérations sensibles,
capture chez Deloitte, chaînage entre deux verrous, dépendance européenne aux agences) : l'une d'elles —
le chaînage — est le chantier que l'article déclare lui-même ouvert. La cinquième (comparer le coût de
résistance au coût du rachat) est faisable en partie seulement : le prix du rachat d'Arabelle par EDF
n'est pas dans le registre.

---

## 4. Tranche appliquée (16 éditions, vérifiées une à une)

| # | Ligne | Objet | Source |
|---|---|---|---|
| 1 | 15 | Définition de « verrou » élargie (mécanisme **ou dispositif**, **capacité** de décision, État / entreprise / espace public) | R1 |
| 2 | 11 | « fleurons industriels… démembrés » → « l'un de ses fleurons industriels les plus stratégiques **a été cédé** » | R1, R6 |
| 3 | 37 | Glose JCPOA | R10 |
| 4 | 41 | « Il suit le rapport du coût… » → « un rapport **documenté** entre… » | R1 |
| 5 | 47 | Glose du *US CLOUD Act* | R10 |
| 6 | 48 | Glose de la directive ePrivacy | R10 |
| 7 | 58 | SGDSN en clair | R10 |
| 8 | 103 | Glose de l'IETF | R10 |
| 9 | 84 | « l'instrumentalisation d'une procédure pénale » → « l'**usage** d'une procédure pénale » | R1 |
| 10 | 112 | **DSA art. 22** : statut attribué par le coordinateur national, droit au traitement prioritaire, la plateforme décide | R4 |
| 11 | 120 | Suppression de « orienter la docilité des appareils d'État » (attribution psychologique) | R1 |
| 12 | 134 | Article 432-11 : les **deux branches** distinguées (pacte / abus d'influence) | R4 |
| 13 | 136 | Directive 2026/1021 : « seuil minimal de peine maximale » | R4 |
| 14 | 139 | Renvoi final 432-11 : pacte pour la corruption passive, pas de pacte pour le trafic d'influence | R4 |
| 15 | 184 | Une phrase : les trois séries (refus, incompatibilité, conditionnement) ne sont pas comparables | R5 |
| 16 | 188 | **La grille appliquée** : deux résultats opposés, Alstom subi / Photonis levé | R5 |
| 17 | 198 | « dépendances consenties » → « acceptées une par une, et jamais choisies ensemble » | R1, R5, R6 |
| 18 | 202 | Second volet du critère de réfutation instruit (HATVP, Lituanie) | R5 |

Contrôles : les 19 chaînes nouvelles à 1 occurrence exacte, les 14 chaînes retirées à 0 ; 0 cadratin,
0 apostrophe ASCII, 0 guillemet droit, 0 tableau ; 6 figures appelées, 6 fichiers présents.

---

## 5. Ce qui reste à trancher par l'auteur

1. **Lignes 54-55** — « mandaté par des entités liées au renseignement émirati » et « l'investigation
   consacrée à l'**influence israélienne** en France ». Les deux faits sont documentés (pièces [65] et
   [66]) et la borne est adjacente (« le commanditaire reste non identifié »). R7 demande de retirer les
   deux adjoints ; je ne le recommande pas — l'article nomme les opérations documentées, et retirer
   l'adjoint laisserait croire à une précaution — mais la décision est éditoriale, pas factuelle.
2. **« La guillotine du dollar »** et **« son artère vitale »** : R7 propose de les retirer. Décision
   antérieure : les garder. Maintenu, avec le désaccord consigné.
3. **Le verrou III est le plus faible des quatre**, et les trois revues qui parlent de hiérarchie le
   confirment (Deloitte sans capture, agences non mesurées, signaleurs sans effet mesuré). Rien dans le
   corpus ne le renforce : c'est une limite à assumer, pas à corriger.
4. **Le second volet du critère de réfutation** est maintenant instruit par deux cas ; il reste
   ouvert, et l'article le dit.

---

## 6. Ce que les revues confirment comme solide

- **R4 (juriste)** : six points vérifiés sans réserve — article 432-13 (délai de trois ans depuis la
  cessation des fonctions, surveillance appréciée dans le cadre des fonctions effectives), article 433-2
  (deux branches, influence réelle ou supposée), chaîne Alstom/FCPA/IEF (la pression pénale américaine
  et la décision administrative française ne sont pas confondues), chiffres IEF 2024 (337 décisions,
  182 dans le champ, 54 % de conditions, six refus en trois ans), Chat Control (règlement 2026/1881
  jusqu'au 3 avril 2028, détection volontaire, bout en bout exclu), HATVP (trois catégories, 7 % et
  77 % sur 2023, 751 projets en 2024).
- **R8 (avocat du diable)** : trois affirmations qu'il déclare ne pas pouvoir attaquer — la chaîne
  Alstom bornée pièce par pièce et sa borne assumée ; l'articulation des verrous posée trois fois comme
  lecture ; le mécanisme de sur-conformité de Total adossé à l'actionnariat et à la dette.
- **R8, conclusion de fond** : la thèse inverse (« la souveraineté s'est exercée, cas par cas ») est
  **compatible avec l'intégralité du corpus**. Ce n'est pas un défaut : c'est la conséquence exacte du
  choix de l'article de ne pas conclure au système. À dire franchement, cela signifie que l'article ne
  peut pas être « incontournable » par la preuve — il l'est par la méthode et par les pièces.

---

## 7. Fact-check (R3, arrivé après la première rédaction de cette synthèse)

Rapport : `R3_FACT_CHECKER_FORENSIQUE.md` (7 131 octets). Sept points instruits. **Cinq sont
déclarés non vérifiables, mais pour une raison de harnais et non de fait** : les copies locales
(Alstom/DOJ, Synergy, Trésor IEF) sont des pages d'erreur (404, redirection, connexion refusée).
Cela ne dit rien de l'article ; cela dit que le téléchargement a échoué et le rôle le déclare
honnêtement au lieu de trancher.

**Un apport réel, appliqué.** Sur BNP Paribas, le communiqué de la banque (pièce [75]) décrit une
**suspension temporaire, pour un an à compter du 1er janvier 2015, de certaines opérations directes de
compensation en dollars, portant principalement sur le financement du négoce international de matières
premières, pour la partie pétrole et gaz**. L'article écrivait « une interdiction temporaire d'un an de
réaliser des opérations de compensation en dollars pour les activités de financement du pétrole et du
gaz », ce qui élargissait le périmètre et employait « interdiction » là où la banque écrit
« suspension ». Corrigé (tranche F17), ainsi que la phrase suivante (« l'arrêt de fait de ses opérations
en dollars »). Le dossier phare est le premier à devoir porter la formulation de sa propre pièce.

**Une erreur du rôle, écartée après vérification.** R3 conclut à une divergence sur les mobilités
(« 74,3 % d'avis assortis de réserves » contre les 77 % de l'article). La comparaison est fausse : le
document qu'il a lu est le bilan **2024** de la HATVP, quand l'article attribue explicitement les 7 %
d'incompatibilité et les 77 % de compatibilités avec réserves à **2023**, source Cour des comptes
(pièces [84] [85]). Deux années, deux sources, aucune divergence. Les autres « renvois muets » de sa
liste relèvent du même échec de téléchargement. Deux points confirmés sur pièce : BNP (8,97 Md$, plaider
coupable du 30 juin 2014) et le Health Data Hub (« SNDS covers 98.8% of the French population, more than
66 million persons »).

Les copies restent dans `/tmp/factcheck_sources/` (21 fichiers) jusqu'à la clôture de la session.

---

## 8. Passe de relecture en flux après les éditions (F15 à F17)

Après application des tranches, l'article a été relu en continuité, du titre à l'épilogue. Trois
défauts introduits ou révélés par les éditions précédentes, et corrigés en F16 :

- le prologue répétait « sans qu'aucun ordre formel ait été donné » et « sans jamais exiger
  d'instruction écrite explicite » à deux phrases d'intervalle, avec « capacité de décision » deux fois ;
- la glose du *US CLOUD Act* insérée en F14 avait allongé une phrase déjà longue, l'apposition placée
  au milieu du sujet ; scindée en deux phrases ;
- le libellé de ligne de la matrice « Interception et identité numérique » ne correspondait plus au
  contenu (identification, détection) après la correction du chapeau eIDAS.

Deux corrections de cohérence ont été appliquées en même temps : l'antécédent flottant de l'ouverture
de la partie II (« qui les exposent » désignait les outils et non les actifs) et la date du Conseil
d'État dans la ligne de matrice du Front uni.

---

*Zéro cadratin dans ce document. Contrôles par `grep`, `python3` et `md5sum` le 2026-09-15.*
