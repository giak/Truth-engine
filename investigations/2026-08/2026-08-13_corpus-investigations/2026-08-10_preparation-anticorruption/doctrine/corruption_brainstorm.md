La règle centrale : **n’enquête pas sur « la corruption de l’État » en général**. C’est trop vaste, invérifiable et vulnérable au biais de confirmation.

Enquête sur :

> **une décision identifiable → un flux public → un bénéficiaire → un éventuel contre-avantage → le fonctionnement ou l’échec des contrôles.**

Puis agrège plusieurs cas construits avec la même méthode pour tester l’hypothèse systémique.

## 1. Distinguer trois niveaux d’enquête

| Niveau              | Question                                                                                                | Résultat possible                                                                         |
| ------------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Micro — pénal**   | Une personne a-t-elle reçu ou proposé un avantage contre un acte de fonction ?                          | Corruption, trafic d’influence, favoritisme, prise illégale d’intérêts…                   |
| **Méso — réseau**   | Les mêmes acteurs, entreprises ou intermédiaires bénéficient-ils régulièrement de décisions anormales ? | Réseau d’influence, clientélisme, collusion, concentration des avantages                  |
| **Macro — système** | Les règles, nominations, contrôles et incitations reproduisent-ils durablement ces avantages ?          | Capture réglementaire, capture institutionnelle, corruption systémique au sens analytique |

Une anomalie systémique n’établit pas nécessairement une corruption pénale. Inversement, un pot-de-vin isolé ne démontre pas la capture d’une institution.

## 2. Le protocole d’enquête

### Étape 1 — Réduire brutalement le périmètre

Commence par :

* un acheteur ou organisme public ;
* une famille de dépenses ;
* une période de trois à cinq ans ;
* un ensemble défini de bénéficiaires.

Exemple :

> Tous les marchés de conseil informatique attribués par l’organisme X entre 2021 et 2026, leurs avenants, sous-traitants et anciens agents recrutés par les attributaires.

Les meilleurs terrains documentaires sont généralement :

* commande publique ;
* concessions et délégations de service public ;
* subventions et aides ;
* foncier, urbanisme et immobilier public ;
* opérateurs et agences de l’État ;
* entreprises publiques, SEM et SPL ;
* associations ou fondations financées par l’État ;
* cabinets de conseil et intermédiaires ;
* nominations et mobilités public-privé ;
* financement politique ;
* secteurs réglementés.

Les domaines régaliens ou classifiés sont beaucoup plus difficiles à traiter en OSINT.

### Étape 2 — Écrire des hypothèses concurrentes

Pour chaque anomalie, impose au moins ces hypothèses :

* **H0 :** décision régulière et économiquement justifiée ;
* **H1 :** mauvaise gestion, impréparation ou incompétence ;
* **H2 :** contrainte réelle : urgence, pénurie, technicité, dépendance industrielle ;
* **H3 :** entente entre fournisseurs sans complice public ;
* **H4 :** conflit d’intérêts ou favoritisme ;
* **H5 :** corruption ou trafic d’influence ;
* **H6 :** données incomplètes ou mal interprétées.

Définis ensuite ce qui confirmerait ou invaliderait chaque hypothèse. Une enquête sérieuse cherche activement les éléments disculpants.

### Étape 3 — Reconstituer les cinq chaînes

| Chaîne                         | Questions                                                                                                        |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| **Autorité et décision**       | Qui avait compétence ? Qui a préparé, conseillé, signé, contrôlé et validé ?                                     |
| **Argent et exécution**        | Quelle enveloppe ? Quel contrat ? Quels avenants, factures, paiements, pénalités et livrables ?                  |
| **Bénéficiaire réel**          | Quelle société, quel groupe, quels propriétaires, dirigeants, sous-traitants et intermédiaires ?                 |
| **Contre-avantage**            | Cadeau, emploi, contrat futur, don politique, financement associatif, avantage à un proche, rétrocommission ?    |
| **Contrôle et neutralisation** | Qui devait détecter ou arrêter l’opération ? Quelles alertes furent émises ? Pourquoi n’ont-elles rien produit ? |

L’OSINT permet souvent de fermer les trois premières chaînes. La quatrième — le pacte secret et le contre-avantage — nécessite fréquemment des témoignages, documents internes, données bancaires ou pouvoirs judiciaires.

Ton objectif réaliste n’est donc pas toujours de « prouver la corruption » comme le ferait un juge, mais de produire un dossier assez précis pour :

* établir des faits publics ;
* documenter une irrégularité ;
* formuler une inférence défendable ;
* justifier l’ouverture d’une enquête dotée de moyens coercitifs.

## 3. Partir des documents, pas des personnes

Une investigation centrée d’emblée sur un élu ou un fonctionnaire conduit facilement à sélectionner uniquement ce qui l’accable.

Commence par la transaction :

1. besoin public invoqué ;
2. base légale et budget ;
3. procédure retenue ;
4. candidatures et critères ;
5. décision d’attribution ;
6. contrat initial ;
7. exécution réelle ;
8. avenants et modifications ;
9. paiement final ;
10. bénéficiaires et éventuels contre-flux.

Les personnes n’entrent dans l’enquête qu’en fonction de leur rôle documenté.

## 4. Les sources publiques essentielles

| Objet                          | Sources prioritaires                                                                                                                                                                                          |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Marchés publics**            | [DECP consolidées sur data.gouv.fr](https://www.data.gouv.fr/datasets/donnees-essentielles-de-la-commande-publique-fichiers-consolides), BOAMP, PLACE, TED, profils d’acheteurs                               |
| **Contrats et exécution**      | Demandes CRPA/CADA : contrat, rapport d’analyse communicable, avenants, bons de commande, factures, ordres de service, réception, décompte final                                                              |
| **Entreprises**                | DATA INPI/RNE, SIRENE, BODACC, actes et comptes déposés                                                                                                                                                       |
| **Bénéficiaires effectifs**    | L’accès est désormais restreint, mais une demande ciblée peut être faite à l’INPI en justifiant d’un intérêt légitime. [INPI](https://www.inpi.fr/ressources/formalites-dentreprises/beneficiaires-effectifs) |
| **Associations et fondations** | JOAFE, RNA, comptes publiés, conventions de subvention et [catalogue data.gouv.fr](https://www.data.gouv.fr/pages/donnees_associations)                                                                       |
| **Intérêts et influence**      | Déclarations publiques, mobilités public-privé et [open data HATVP](https://www.hatvp.fr/open-data/), [répertoire des représentants d’intérêts](https://www.hatvp.fr/open-data-repertoire/)                   |
| **Financement politique**      | Comptes des partis, comptes de campagne et décisions de la [CNCCFP](https://cnccfp.fr/)                                                                                                                       |
| **Budget de l’État**           | PAP, RAP, jaunes budgétaires, opérateurs et données d’exécution sur [budget.gouv.fr](https://www.budget.gouv.fr/budget-etat)                                                                                  |
| **Finances locales**           | Budgets, balances comptables, comptes financiers et données DGFiP/DGCL sur [collectivites-locales.gouv.fr](https://www.collectivites-locales.gouv.fr/)                                                        |
| **Contrôles**                  | Cour des comptes, chambres régionales, inspections générales, rapports parlementaires, décisions juridictionnelles                                                                                            |
| **Droit applicable**           | Légifrance, jurisprudence administrative et pénale, doctrine CADA                                                                                                                                             |

Attention : une obligation de publication ne garantit ni l’exhaustivité ni la qualité des données. Un marché absent des DECP n’est pas nécessairement caché ; une ligne manquante reste d’abord une donnée manquante.

## 5. Exploiter réellement la CADA

Après signature d’un marché, de nombreuses pièces deviennent en principe communicables, sous occultation des secrets protégés : acte d’engagement, prix global, rapport d’analyse concernant l’attributaire, avenants, factures, bons de commande, ordres de service, actes de sous-traitance, procès-verbaux de réception et décompte final. [Doctrine CADA sur les marchés publics](https://www.cada.fr/administration/marches-publics)

Demande des **documents existants et précisément identifiés**, pas une explication générale :

> Je sollicite, en format électronique natif, la communication des documents suivants relatifs au marché nº X : acte d’engagement et annexes communicables, rapport d’analyse des offres après occultation des secrets protégés, avenants, bons de commande, factures, procès-verbaux de réception et décompte général définitif.

Ajoute que tu acceptes l’occultation des données légalement protégées. Procède par lots raisonnables.

L’administration dispose normalement d’un mois. Son silence vaut refus. La CADA doit être saisie dans les deux mois suivant ce refus ; cette saisine est gratuite et constitue normalement un préalable au contentieux administratif. [CADA](https://www.cada.fr/particulier/quand-et-comment-saisir-la-cada)

## 6. Les principaux signaux d’alerte

### Avant l’attribution

* besoin mal défini ou artificiellement urgent ;
* spécifications semblant écrites pour un fournisseur précis ;
* découpage de commandes autour d’un seuil ;
* procédure dérogatoire répétée ;
* délai anormalement court ;
* consultant préparant le marché puis candidatant directement ou indirectement ;
* critères modifiés tardivement ;
* membres de la décision ayant des liens antérieurs avec un candidat.

### Lors de l’attribution

* un seul candidat de façon répétée ;
* même attributaire malgré des offres apparemment moins favorables ;
* notation incohérente avec les commentaires ;
* avantage informationnel accordé à un candidat ;
* entreprises concurrentes partageant adresse, dirigeants ou sous-traitants ;
* rotation artificielle des gagnants ;
* concentration inhabituelle chez un fournisseur.

### Pendant l’exécution

* avenants importants ou successifs ;
* transformation du périmètre initial ;
* prestations hors marché ;
* absence de livrable vérifiable ;
* factures rondes, répétitives ou peu descriptives ;
* validation et contrôle réalisés par la même personne ;
* pénalités prévues mais systématiquement abandonnées ;
* sous-traitant récurrent apparaissant seulement après attribution ;
* paiement avant service fait ;
* renouvellements automatiques ou dépendance volontairement entretenue.

### Après la décision

* recrutement du décideur par le bénéficiaire ;
* contrat de conseil ou conférence rémunérée ;
* emploi d’un proche ;
* don à un parti, une association ou une structure liée ;
* acquisition immobilière ou enrichissement inexpliqué ;
* intervention d’un ancien responsable public comme intermédiaire ;
* avis de contrôle ignoré ou recommandation jamais appliquée.

Ce sont des **signaux de triage**, jamais des preuves autonomes.

### Opacité institutionnelle : les auditions de la commission des affaires économiques ne sont jamais transcrites (pattern réutilisable)

Fait établi à la source primaire (scan exhaustif des 281 comptes rendus des sessions 2024-2025 et 2025-2026 de l'Assemblée nationale, pattern `l17cion-eco{session}{n:03d}_compte-rendu.pdf`) :

* la commission des affaires économiques ne publie **aucun compte rendu écrit** des auditions ordinaires, quel que soit l'auditionné : régulateurs (CRE, Autorité de la concurrence, ARCEP, Médiateur de l'énergie), administration (DGCCRF, DGDDI, Bpifrance), entreprises, ministres, experts. Mention systématique : « Ce point de l'ordre du jour n'a pas fait l'objet d'un compte rendu écrit. Les débats sont accessibles sur le portail vidéo » ;
* **seule exception : les auditions en application de l'article 13 de la Constitution** (nominations présidentielles : EDF, CEA, INRAE, Orano, etc.) sont transcrites intégralement (69 000-115 000 caractères chacune) ;
* la commission des affaires culturelles et de l'éducation applique la même politique (ARCOM/Ajdari : CR 003 du 08/10/2025 et CR 021 du 03/12/2025, « Cette audition n'a pas fait l'objet d'un compte rendu écrit ») ;
* la commission des finances applique la politique INVERSE : transcription intégrale généralisée, y compris les régulateurs (gouverneur de la Banque de France, 18/02/2026, 108 410 caractères ; présidente de l'AMF, 10/06/2026, 86 334 caractères).

Conséquences opérationnelles pour tout futur dossier :

1. **Ne jamais citer un CR écrit d'audition ordinaire de la commission eco** : il n'existe pas. Vérifier à la source (pattern PDF ci-dessus) ; si la mention « pas de compte rendu écrit » apparaît, la parole est confinée à la vidéo du portail (non indexée, non citable).
2. **La non-transcription est un choix, pas une fatalité** : la commission finances transcrit le régulateur bancaire, la commission eco renvoie le régulateur énergétique à la vidéo. Documenter ce contraste dans la grille de légitimité (critère 7 du §13 : opacité structurelle, pas accidentelle).
3. **Canal de contournement** : transcription locale whisper de la vidéo d'audition (outillage validé, réutilisable) pour documenter la position orale ; position écrite via le fascicule « Réponses des administrations » des rapports de la Cour des comptes.
4. **Vérifier si une recommandation de contrôle est posée en audition** : son absence est un signal. Constat documenté : la rec. n°1 CdC (collecte des coûts ENR) n'a fait l'objet d'aucune question en 1 h 30 d'audition de la présidente de la CRE le 29/04/2026 (transcription whisper complète, 0 mention de collecte/échantillonnage).

Preuves (dans `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_run2-enr/`) : `2026-08-10_22-38_gap-ll22-cr-audition-wargon_RESOLUTION.md` (CR 81, mention exacte), `2026-08-10_23-39_non-transcription-regulateurs_RESOLUTION.md` (281 CR), `2026-08-11_04-09_contre-test-culture-finances_RESOLUTION.md` (culture/finances + constat d'absence), `2026-08-10_23-20_transcription-whisper-wargon_RESOLUTION.md` (contournement whisper).

## 7. L’analyse quantitative

Les indicateurs les plus utiles sont :

* part des marchés attribuée aux cinq premiers fournisseurs ;
* fréquence des procédures négociées ;
* taux d’appels d’offres à candidature unique ;
* montant cumulé des avenants rapporté au montant initial ;
* durée entre publication et clôture ;
* récurrence des mêmes sous-traitants ;
* proximité des montants avec les seuils procéduraux ;
* prix unitaire comparé à des achats homogènes ;
* évolution avant/après une nomination ;
* concentration des subventions chez des structures liées ;
* délais entre décision publique et mobilité professionnelle.

Compare seulement des opérations réellement homogènes : même produit, même volume, même niveau de service, même transfert de risque et même période.

À éviter :

* utiliser la loi de Benford comme détecteur universel ;
* transformer un algorithme opaque en « score de corruption » ;
* traiter une corrélation de graphe comme une relation causale ;
* comparer un prix public et un prix grand public sans intégrer spécifications, garanties, maintenance, logistique et risques ;
* considérer vingt articles reprenant la même fuite comme vingt sources indépendantes.

## 8. La discipline probatoire

Je te conseille cinq couches strictement séparées :

```text
RAW → FAITS → RELATIONS → HYPOTHÈSES → QUALIFICATIONS/PUBLICATION
```

* **RAW** : document original conservé sans modification ;
* **FAITS** : propositions atomiques exactement sourcées ;
* **RELATIONS** : liens entre acteurs uniquement lorsqu’ils sont documentés ;
* **HYPOTHÈSES** : explications testables, avec hypothèses rivales ;
* **QUALIFICATIONS** : lecture pénale ou systémique, toujours distincte des faits.

Pour chaque affirmation :

| Champ                | Contenu                                                |
| -------------------- | ------------------------------------------------------ |
| ID                   | Identifiant stable                                     |
| Proposition          | Une seule affirmation vérifiable                       |
| Source               | Document exact                                         |
| Localisation         | Page, paragraphe, ligne ou cellule                     |
| Nature               | Fait, déclaration, allégation, inférence               |
| Axe                  | Pénal / légal / légitime (un fait peut informer plusieurs axes) |
| Directivité          | Preuve directe ou circonstancielle                     |
| Indépendance         | Origine réelle de la source                            |
| Contradictions       | Éléments opposés                                       |
| Statut               | Établi, corroboré, allégué, inféré, contredit, inconnu |
| Formulation publique | Phrase juridiquement prudente                          |

Ne résume jamais une source avant de l’avoir archivée. Conserve :

* original ;
* URL et date d’acquisition ;
* empreinte SHA-256 ;
* version OCR séparée ;
* copie de travail ;
* historique des corrections.

## 9. Utiliser les LLM sans contaminer la preuve

Dans un pipeline multi-LLM :

* un LLM peut extraire les noms, dates, montants et clauses ;
* il peut comparer plusieurs versions d’un contrat ;
* il peut chercher des contradictions ;
* il peut générer des hypothèses rivales ou préparer un questionnaire ;
* il ne doit jamais devenir la source d’un fait ;
* toute donnée extraite doit revenir au document et à la page exacte ;
* les calculs financiers, dédoublonnages et rapprochements SIREN doivent rester déterministes ;
* le consensus de plusieurs LLM ne constitue aucune corroboration ;
* la compression sémantique ne doit jamais remplacer le dossier probatoire original.

Le rôle idéal du multi-LLM est la **red team**, pas la certification.

## 10. Témoins, sources et droit de réponse

Demande d’abord aux sources :

* ce qu’elles ont personnellement vu ;
* à quelle date ;
* dans quelle fonction ;
* quels documents corroborent leur récit ;
* qui d’autre peut confirmer indépendamment ;
* ce qui pourrait contredire leur version.

Sépare toujours :

* observation directe ;
* document vu mais non possédé ;
* récit reçu d’un tiers ;
* interprétation personnelle ;
* rumeur organisationnelle.

Avant publication, adresse aux personnes concernées un questionnaire factuel, précis et non accusatoire. Accorde un délai raisonnable. Reproduis loyalement leurs réponses, leurs démentis et les éléments disculpants. L’absence de réponse n’est pas un aveu.

En matière de diffamation, la jurisprudence examine notamment l’intérêt général, la base factuelle suffisante, le sérieux de l’enquête, la prudence de l’expression et l’absence d’animosité personnelle. [Cour de cassation, 26 février 2025](https://www.legifrance.gouv.fr/juri/id/JURITEXT000051283974)

## 11. Sécurité et limites juridiques

* N’incite jamais une source à pirater, voler ou détourner un document.
* Ne paie pas pour une donnée obtenue illégalement.
* Ne modifie jamais l’original reçu.
* Sépare les coordonnées des sources du dossier éditorial.
* Chiffre les supports et utilise une authentification forte.
* Retire métadonnées et données personnelles inutiles avant publication.
* Fais examiner par un avocat les pièces couvertes potentiellement par le secret de l’instruction, le secret professionnel, le secret des affaires ou la défense nationale.

Point important pour un auteur indépendant : la définition légale française du journaliste protégé par le secret des sources vise une activité exercée **à titre régulier et rétribué** dans une entreprise de presse ou de communication. Ne présume donc pas que cette protection s’applique automatiquement à un enquêteur indépendant non rémunéré. [Article 2 de la loi de 1881](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000021662491)

## 12. Démontrer une corruption systémique

Pour passer du cas individuel au système, il faut établir :

1. une population complète ou un échantillon justifié ;
2. un mécanisme récurrent, pas seulement plusieurs scandales différents ;
3. des bénéficiaires ou réseaux qui persistent dans le temps ;
4. une asymétrie mesurable dans l’accès aux décisions ou ressources ;
5. la répétition des mêmes dérogations ;
6. l’inefficacité ou la neutralisation régulière des contrôles ;
7. la reproduction du système par nominations, financements, dépendances ou mobilités ;
8. des cas négatifs permettant de comprendre ce qui se passe lorsque le réseau est absent.

Même ainsi, la conclusion correcte peut être :

> « Les données établissent une capture durable du processus et un risque élevé d’atteintes à la probité. Elles ne permettent pas, en l’état, de démontrer un pacte corruptif individuel. »

Cette formulation est plus forte qu’une accusation trop large : elle indique exactement ce qui est démontré et ce qui manque.

## 13. L’axe légitimité : légal ≠ légitime dans l’évaluation des verdicts

### La règle

La légalité d’un mécanisme n’exonère pas de sa légitimité. Un verdict d’enquête doit distinguer **trois axes évalués séparément** :

| Axe | Question | Exemples de réponse |
| --- | -------- | ------------------- |
| **Pénal** | Une infraction est-elle établie aux éléments constitutifs ? | 0 fait, 1 fait, dossier à transmettre |
| **Légal** | Le mécanisme est-il conforme à la norme ? | Oui, non, zone grise |
| **Légitime** | Le mécanisme sert-il l’intérêt général ? | Oui, non, contestable |

L’erreur de cadrage à éviter : conclure « c’est légal donc rien à signaler ». Le légal est un **plancher, pas un plafond**. Légaliser une rente ou une capture n’en fait pas une décision défendable. L’OCDE qualifie la capture des politiques publiques de pouvant être légale (moyens légaux ou illégaux), distincte du pénal : la légalité décrit la conformité à la norme, pas l’acceptabilité. [OCDE, Preventing Policy Capture](https://www.oecd.org/en/publications/preventing-policy-capture_9789264065239-en.html)

### La grille obligatoire de conclusion (3 axes)

Chaque dossier final doit produire une grille de verdict à 3 axes, même quand l’axe pénal est clos :

```text
PÉNAL   : [0 fait / 1 fait / à transmettre] + éléments constitutifs visés
LÉGAL   : [oui / non / zone grise] + base normative exacte
LÉGITIME : [oui / non / contestable] + critères ci-dessous
```

Si « légal = oui » et « légitime = non », le verdict doit le dire **explicitement** et qualifier la nature de l’illégitimité (rente, capture, opacité, refus du contrôle, transfert de souveraineté), sans la réduire au silence parce qu’aucune infraction n’est établie.

### Les 8 critères d’évaluation de la légitimité

1. **Qui a écrit la règle ou le mécanisme ?** (législateur, régulateur, acteur privé ; quelle procédure, quels débats)
2. **Y avait-il un garde-fou au moment de l’écriture ?** (plafond de rendement, clause de partage de rente, mécanisme de contrôle mesurable)
3. **Le contrôle est-il possible et effectué ?** (données collectées, accès, publications, refus de communiquer)
4. **Qui paie et qui bénéficie réellement ?** (payeur final, bénéficiaire effectif, intermédiaires)
5. **Le bénéficiaire est-il légitime au regard de l’objet de la dépense publique ?** (opérateur national, actionnariat, souveraineté, recette fiscale)
6. **Des alternatives auraient-elles mieux servi l’intérêt général ?** (appel d’offres, plafond, partage de rente, concurrence)
7. **L’opacité est-elle structurelle ou accidentelle ?** (absence de publication, PV non déposés, données inaccessibles, refus répétés ; pattern §6 : auditions de la commission des affaires économiques jamais transcrites hors art. 13)
8. **Le mécanisme a-t-il été corrigé ou sanctuarisé dans le temps ?** (clause de révision, rétroactivité, garde-fous ajoutés tardivement et échoués)

### Le contrôle déclaratif : les fonctions bénévoles à déclarer (point 6 de la FAQ HATVP, critère conflit d'intérêts)

Source : page officielle HATVP « La déclaration d'intérêts » (rubrique de déclaration n° 6 « Fonctions bénévoles susceptibles de faire naître un conflit d'intérêts »), lue intégralement le 11/08/2026. Texte exact :

> « Toutes les activités bénévoles ne sont pas concernées, mais uniquement celles qui sont susceptibles de faire naître un conflit d'intérêts. Le conflit d'intérêt est défini à l'article 2 de la loi du 11 octobre 2013 comme "toute situation d'interférence entre un intérêt public et des intérêts publics ou privés qui est de nature à influencer ou à paraître influencer l'exercice indépendant, impartial et objectif d'une fonction". »

La FAQ fixe **deux critères cumulatifs** pour apprécier la déclarabilité d'une fonction bénévole :

1. **L'interférence potentielle** : l'activité bénévole et le mandat/fonction publique portent-ils sur le même secteur d'activité ou les mêmes thématiques ?
2. **L'intensité de l'interférence** : le déclarant est-il conduit, dans ses fonctions publiques, à entrer en contact avec la structure où il exerce l'activité bénévole ? Attribue-t-il des subventions à ce type de structures ?

Règles complémentaires de la même page : les activités bénévoles doivent être déclarées en rubrique n° 6 (et non en rubrique n° 1 activités professionnelles) ; seules les fonctions non déjà déclarées ailleurs y figurent ; en cas de doute, le déclarant peut consulter la HATVP.

Conséquences opérationnelles pour les dossiers anticorruption :

1. **Un mandat bénévole peut être un fait déclaratif pertinent** : ne pas le traiter comme « sans objet » sous prétexte de non-rémunération. La déclarabilité dépend du **conflit d'intérêts potentiel**, pas de la rémunération.
2. **Test en deux questions pour chaque fonction bénévole d'un responsable public** : (a) même secteur/thématiques que ses fonctions publiques ? (b) contacts ou subventions possibles avec la structure ? Deux non = hors champ déclaratif probable ; un oui = déclarabilité plausible ; deux oui = déclarable avec quasi-certitude.
3. **Dans une enquête, le point 6 permet de qualifier une omission** : un mandat bénévole non déclaré alors qu'il crée une interférence réelle est un signal de **conflit d'intérêts non géré** (axe pénal potentiel, selon les faits) et d'**opacité** (critère 7 de cette grille).
4. **Ne pas confondre contrôle déclaratif et contrôle des mobilités** : le point 6 relève des DPI (déclarations de situation), l'art. 23 de la loi 2013-907 relève des avis de compatibilité des mobilités (ex-régulateur → entreprise). Les deux dispositifs sont distincts et se complètent.

**Application documentée au cas FEDEREC/Carenco (fil VP-P4, run2-enr)** :

* **Argument chronologique décisif (à énoncer en premier)** : Carenco est président délégué de FEDEREC/FEDERREC (fédération professionnelle des entreprises du recyclage, Livre IV du Code du travail) depuis le 14/11/2023, **postérieurement** à la fin de toutes ses fonctions publiques (ministre délégué Outre-mer jusqu'au 20/07/2023, président de la CRE 2017-2022). Le point 6 concerne les fonctions bénévoles exercées **pendant** un mandat public, à déclarer dans la DPI en cours : aucun mandat public n'étant en cours au 14/11/2023, **aucune DPI ne couvre le mandat FEDEREC** (limite établie dans `2026-08-11_17-06_gap6-dpi-publique-carenco_RESOLUTION.md`). La question d'une omission déclarative ne se pose donc pas, indépendamment du test ci-dessous.
* Test du critère 1 (interférence potentielle), analyse secondaire : le recyclage n'est pas le secteur de la régulation énergétique (CRE) ni des Outre-mer ; les fiches d'activités RI de FEDEREC montrent un secteur énergie marginal (4/43, toutes liées à la valorisation énergétique des déchets/CSR, hors compétence CRE). Appréciation : interférence **faible** (jugement calibré ; contre-argument possible : la valorisation énergétique des déchets touche le secteur de l'énergie et Carenco a eu des fonctions énergie, directeur de cabinet du ministre de l'Écologie et de l'Énergie selon le RA 2023 ; il n'en reste pas moins sans mandat public au moment du mandat FEDEREC).
* Test du critère 2 (intensité) : aucune donnée ne montre que Carenco aurait été conduit, en fonctions, à contacter FEDEREC ou à lui attribuer des subventions : intensité **faible**.
* Conclusion (nuancée) : le mandat FEDEREC est **hors champ de la DPI** (chronologie) ; le test des deux critères, mené à titre secondaire, aboutirait à une appréciation « faible » sur les deux axes. Le point pertinent reste l'incompétence HATVP 2023-247 (fédération pro hors art. 23, cf. documents 16-31 et 16-45 du run2-enr). **Aucun fait d'infraction** n'en résulte.

Preuves (dans `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_run2-enr/`) : `2026-08-11_16-45_gap4-mandat-federec-benevolat_RESOLUTION.md` (bénévolat présumé), `2026-08-11_17-06_gap6-dpi-publique-carenco_RESOLUTION.md` (DPI retirée, 3 voies), `2026-08-11_16-38_gap3-federec-contacts-cre-repertoire-ri_RESOLUTION.md` (0 contact CRE déclaré), `2026-08-11_16-31_gap1-saisine-hatvp-federec_RESOLUTION.md` (avis d'incompétence 2023-247).

### Les formulations

* Si pénal 0 + légal oui + légitime non : « Les données établissent un mécanisme **légal mais illégitime** : rente/capture [préciser], protégé par [refus du contrôle / opacité / absence de garde-fou]. La légalité n’exonère pas : elle décrit la conformité à la norme, pas l’acceptabilité. »
* Ne jamais écrire « transfert légal, donc 0 problème » : écrire « transfert légal et quantifié, 0 infraction établie, mais **illégitime** car [raison sourcée] ». [Application au fil Valeco/EnBW : 2026-08-10_21-42_legal-vs-legitime-valeco_APPLICATION.md et trajectoire législative 2026-08-10_21-46_gap1-qui-a-ecrit-la-regle-oa_INVESTIGATION.md]
* Distinguer **fait, inférence et jugement normatif** : « illégitime » est une évaluation (label), pas un fait ; elle doit s’appuyer sur les faits énumérés (chiffres, textes, refus documentés) et être formulée comme telle.

## 14. Signaler les faits

Selon le dossier :

* l’[AFA](https://www.agence-francaise-anticorruption.gouv.fr/fr/signaler-des-atteintes-probite) reçoit les signalements relatifs aux six atteintes à la probité ;
* le [PNF](https://www.tribunal-de-paris.justice.fr/75/adresser-une-plainte-ou-un-signalement) reçoit les dossiers complexes relevant notamment de la corruption et du trafic d’influence ;
* le procureur territorialement compétent peut recevoir un signalement ou une plainte ;
* le Parquet européen est pertinent lorsque les intérêts financiers de l’Union sont atteints ;
* le Défenseur des droits peut orienter et protéger un lanceur d’alerte contre les représailles. [Défenseur des droits](https://www.defenseurdesdroits.fr/orienter-et-proteger-les-lanceurs-dalerte-180)

Un bon dossier de signalement contient :

* résumé factuel de deux pages ;
* chronologie ;
* acteurs et rôles ;
* montants et flux ;
* qualifications envisagées sans les présenter comme acquises ;
* index des pièces ;
* originaux ;
* éléments contradictoires ;
* questions non résolues.

## Pilote que je recommande

Commence par :

> **un acheteur public + une famille d’achats + cinq exercices + les trente contrats les plus importants.**

Puis :

1. extraction des DECP ;
2. normalisation SIREN/SIRET ;
3. mesure de la concentration, des procédures et avenants ;
4. sélection de trois anomalies et de deux cas normaux comparables ;
5. demandes CADA ciblées ;
6. cartographie des dirigeants, intérêts, sous-traitants et mobilités ;
7. recherche du contre-avantage ;
8. contradiction et droit de réponse ;
9. qualification précise ;
10. publication ou signalement.

C’est assez petit pour être terminé, assez dense pour tester la méthode et assez standardisé pour être répliqué ensuite sur d’autres organismes.
