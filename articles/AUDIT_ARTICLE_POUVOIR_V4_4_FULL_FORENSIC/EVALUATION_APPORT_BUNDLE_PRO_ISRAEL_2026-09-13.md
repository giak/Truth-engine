# Évaluation : ce que le bundle PRO_ISRAEL peut apporter à l'article Pouvoir V4.4

**Objet évalué** : `articles/PRO_ISRAEL_TRUTH_ENGINE_FORENSIC_BUNDLE_2026-09-13` (112 fichiers, 2,0 Mo)
**Article cible** : `AUDIT_ARTICLE_POUVOIR_V4_4_FULL_FORENSIC/01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md`, empreinte `13dd5ef9…47ca` après T1
**Date** : 2026-09-13
**Nature** : analyse et propositions. **Aucune modification de l'article n'a été faite.** Les propositions sont soumises à une décision d'auteur.

---

## 1. Ce qu'est ce bundle, et sa qualité réelle

Branche d'enquête construite le 13 septembre 2026 sur l'influence pro-israélienne et israélienne en France et dans l'UE. Architecture identique au bundle de l'article : `00_READ_FIRST`, `02_METHOD` (KERNEL, ICEBERG, orchestrateur), `03_FOUNDATION`, `04_WAVE`, `05_CONTROL_PLANE` (registre de 172 investigations), `06_SOURCES`, `07_INTEGRITY`.

**Contrôle d'intégrité exécuté** : `07_INTEGRITY/VERIFY_BUNDLE.py` rend `PASS`. Les empreintes du manifeste concordent, et les `deliverable_sha256` des certifications correspondent aux fichiers d'investigation pour INV-026, 027, 028, 160, 161 et 166. Les artefacts sont donc **authentiques et certifiés**, pas fabriqués.

**Couverture physique, d'après `00_READ_FIRST/COVERAGE_MATRIX.csv`** :

| Statut | Investigations | Conséquence |
| --- | --- | --- |
| `COMPLETE_OR_NEAR_COMPLETE` | INV-026, 027, 028, 160, 166 | exploitables au standard de l'article |
| `PARTIAL_PHYSICAL_RECOVERY` | INV-158, 159, 161, 162 | pièces terminales incomplètes : INV-158 sans fichier d'investigation, INV-159 sans investigation ni certification, INV-161 sans run state, INV-162 sans certification |

Le bundle le déclare lui-même : « No missing FINAL, certification or hash is fabricated. » C'est à son honneur, et c'est une contrainte d'usage : **seules cinq investigations sont citables au standard de l'article** (un fait, une pièce).

**Un programme encore en mouvement** : 140 investigations closes sur 172, huit encore passées en revue mais non courues (INV-164 à 172), une prête (INV-163). Citer un programme vivant crée une dépendance de maintenance pour un article publié.

---

## 2. Le point de contact central : la même grammaire

La convergence n'est pas thématique, elle est structurelle. Le bundle retrouve, sur un objet différent, la distinction que l'article construit :

| Le bundle | L'article |
| --- | --- |
| « financement général, grant restreint, transfert entre entités, commande publique, lobbying déclaré et causalité politique » séparés systématiquement (INV-160) | capacité / pouvoir mobilisable / pouvoir exercé / décision finale (l. 93) |
| « Le plafond récurrent : le corpus ferme ressources, accès, financement et tasking projet, actions observables ; il ne ferme pas commandement organisationnel, persuasion, causalité marginale, modèle de contrôle général » (`CHAIN_SUMMARY.md`) | les trois paliers (l. 235 à 239) et les huit raccourcis (l. 167 à 169) |
| R01 « foreign-funded equals foreign agent », R02 « same brand equals same legal person », R03 « not registered equals unlawful », R04 « contract exclusion equals universal exemption » (INV-166) | les huit raccourcis, et l. 89 « la formule “investisseur lié à un État” reste donc trop grossière » |
| « same ELNET brand does not close legal identity or tasking » (INV-166) | l. 157 « Le nom Alstom impose ici une séparation supplémentaire » |

Ce n'est donc pas un complément d'affaires à ajouter. C'est un **second corpus qui butte au même endroit**, et il faut décider si l'article s'en sert ou non, parce que les deux usages n'ont pas le même prix.

---

## 3. Usages recommandés, vérifiés sur sources primaires

J'ai vérifié moi-même les pièces ci-dessous sur Légifrance et sur le site de la HATVP. Elles sont datées, officielles et citables. Écritures en mémoire Mnemolite : `b2c54622`, `2a475e66`, `51dbb867`, `f3392bb1`.

### U1. Le seuil légal nomme les quatre relations (valeur haute, risque faible)

**Fait vérifié.** Article 18-11 de la loi n° 2013-907 du 11 octobre 2013, créé par la loi n° 2024-850 du 25 juillet 2024, **en vigueur depuis le 1er juillet 2025**. Citation :

> « les personnes physiques ou morales exerçant, **sur l'ordre, à la demande ou sous la direction ou le contrôle d'un mandant étranger** […] et aux fins de promouvoir les intérêts de ce dernier, une ou plusieurs actions destinées à influer sur la décision publique, notamment sur le contenu d'une loi, d'un acte réglementaire ou d'une décision individuelle ou sur la conduite des politiques publiques »

Trois actions couvertes : entrée en communication avec une liste de responsables publics, **toute action de communication à destination du public**, collecte ou versement de fonds sans contrepartie. Mandant étranger défini par seuil : personne morale « dirigée ou contrôlée » par une puissance étrangère ou **« financée pour plus de la moitié »** par elle. Exclusion : le personnel diplomatique accrédité agissant dans l'exercice de ses fonctions.

**Pourquoi cela sert l'article.** C'est le seul instrument du corpus où **le législateur doit énumérer des relations, et non des acteurs**. Là où l'article écrit que la capacité n'est pas le pouvoir exercé, le droit écrit quatre relations qualifiantes et exige, en plus, une action destinée à influer. Et la définition du mandant étranger par seuil de financement ou de contrôle répond directement à l. 89, qui reproche à la formule « investisseur lié à un État » d'être trop grossière : le droit français, lui, distingue.

**Emplacement** : partie III, au voisinage de l. 151 à 153, dans le passage qui traite déjà de l'article 433-2 du code pénal et de la directive 2026/1021. Une phrase pour l. 89 également.

### U2. Deux régimes voisins calibrent différemment la même relation (valeur haute, risque nul)

**Fait vérifié.** L'article 433-2 du code pénal (déjà cité [41]) punit le fait d'**« abuser de son influence réelle ou supposée »** : une influence seulement supposée suffit à constituer l'infraction. L'article 18-11 exige une relation effective : **ordre, demande, direction ou contrôle**.

**Pourquoi c'est le meilleur apport du lot.** Dans un seul ordre juridique, deux régimes contigus fixent deux calibrages de la preuve de relation. Cela donne à l'argument des degrés de certitude (F-11 de mon plan de forme) un ancrage normatif, et cela ne demande aucune nouvelle affaire, aucun nouvel acteur, aucun nouveau domaine : deux articles de loi déjà voisins dans le texte. C'est la même démonstration que l'article fait avec Alstom (« pression établie ne signifie ni vente causée ni orchestration »), mais écrite par le législateur.

### U3. Le décret étend le test aux chaînes indirectes, et écarte les échanges contractuels (valeur haute, risque faible)

**Fait vérifié.** Décret n° 2025-733 du 31 juillet 2025, article 1, en vigueur depuis le 2 août 2025 :

> « Ces dispositions sont applicables lorsque la personne exerce des activités d'influence **indirectement**, sur l'ordre, à la demande ou sous la direction ou le contrôle d'un mandant étranger, **par le biais d'un ou de plusieurs intermédiaires**. »

Et, pour le seul volet « entrée en communication » :

> « ne sont pas pris en compte l'exercice d'un recours administratif, la réalisation d'une démarche administrative en application d'une disposition législative ou réglementaire, **la participation à une procédure relevant de la commande publique** et **les échanges prévus par des stipulations contractuelles**. »

**Pourquoi cela sert l'article.** Deux apports. D'abord, le régime couvre explicitement la chaîne indirecte par un ou plusieurs intermédiaires, ce qui est le problème central de la partie III. Ensuite, il **soustrait nommément** les échanges prévus par des stipulations contractuelles : c'est la forme juridique exacte de la distinction que l'article pose à l. 161 à 163, où les compensations industrielles et les commissions licites servent de contraste aux paiements corruptifs, et où « le mot “réseau” ne prouve rien tant qu'on ignore ce qui circule dans ce réseau ». La loi dit la même chose autrement : tout ce qui passe par un contrat n'est pas de l'influence de la même nature.

### U4. Ce que cet ensemble ne permet pas de dire (et qu'il faut écrire)

Le régime entre en vigueur au 1er juillet 2025, les premières déclarations trimestrielles portent sur les activités menées depuis le 1er octobre 2025, et la campagne s'est ouverte au 1er janvier 2026. Le répertoire public interrogé le 13 septembre 2026 **ne publie aucune entité** : « Le répertoire apparaîtra dès que les premiers enregistrements auront été traités par les équipes de la HATVP. » Un instrument neuf, sans base publiée, ne permet donc **aucune inférence sur son application**. Si l'article cite le régime, il doit dire que le corpus d'application est vide à ce jour, sous peine de laisser croire à un bilan.

---

## 4. Usages méthodologiques, sans nommer aucune affaire

Quatre règles de méthode sont extractibles du bundle sans importer ni acteur ni domaine. Elles renforcent l'article au bon endroit : ses conditions de preuve (l. 243 à 248).

### M1. Le contrôle par objectif déclaré avant l'issue

INV-027 documente un cas où **l'acteur a déclaré son objectif avant l'issue, et l'issue a été contraire** : l'objectif déclaré de prévenir la reconnaissance française de la Palestine, et la reconnaissance intervenue le 22 septembre 2025. Le run conclut : « Repeated access therefore does not imply reliable control of French foreign policy », et borne aussitôt : « This does not prove zero intermediate influence. »

C'est un **contrôle négatif d'une espèce que l'article ne possède pas**. Ses deux contrôles négatifs actuels (New IP non adoptée, Lituanie sans concession) portent sur une issue procédurale ou sur une absence de concession. Ici, l'objectif est déclaré par l'acteur, la capacité et l'accès sont riches, et l'issue est l'inverse de l'objectif déclaré sur la décision finale elle-même.

**Usage recommandé** : nommer l'espèce, pas l'affaire. Ajouter aux six conditions de l. 243 à 248 une septième exigence : **que l'objectif de l'acteur soit documenté avant l'issue**, faute de quoi la congruence observée après coup reste une reconstruction de l'observateur. C'est opératoire, c'est court, et cela rend la condition 5 (« écarter les explications concurrentes ») testable au lieu d'être déclarative.

### M2. Le test d'isomorphisme avant toute transposition

INV-028 établit que le mécanisme américain PAC / Super PAC est **juridiquement non isomorphe** au cadre français (interdiction faite aux personnes morales autres que les partis de financer un candidat, restrictions sur les ressources étrangères). Le run en tire : une comparaison fonctionnelle reste pertinente pour le lobbying, l'accès et les réseaux, mais elle doit être testée sur des cas propres, « sans transformer l'existence d'un voyage, d'un contact, d'un financement ou d'une proximité en preuve de tasking, de capture ou d'effet politique ».

**Usage recommandé** : une phrase, dans la partie I, là où l'article traite déjà de la portée extraterritoriale des règles américaines (l. 50 à 58) et où il refuse de conclure à une compétence universelle (l. 52). Formulation visée : un mécanisme établi dans un ordre juridique donné ne se transporte pas dans un autre sans vérifier que les deux cadres le rendent possible.

### M3. Deux chiffres de construction différente ne se soustraient pas

INV-160 et INV-027 alignent deux mesures d'un même objet qui ne mesurent pas la même chose : une subvention américaine de 1,034 M$ à une entité nommée en 2024, et une catégorie réglementaire déclarée de 100 000 à 200 000 euros avec trois ETP. Le run refuse d'appeler le différentiel « lobbying dissimulé » : « Le différentiel ne peut donc pas être qualifié de lobbying dissimulé ou non déclaré sans comptabilité projet et règles d'affectation. »

**Usage recommandé** : c'est la règle que l'article énonce déjà pour ses propres comptages (l. 38 : « sans quoi les chiffres cités plus loin mesureraient autre chose que ce qu'ils annoncent ») mais qu'il n'applique pas explicitement aux chiffres des autres. Une phrase dans la partie III suffit.

### M4. La frontière de catégories

`00_READ_FIRST/README.md` pose comme règle : « The investigations must not collapse Jewish identity, Zionism, pro-Israel advocacy, Israeli nationality, Israeli-state relation and state tasking into one category. Actor and relation evidence control classification. »

C'est la généralisation exacte de ce que l'article fait pour Alstom à l. 157. La règle est importable sans nommer le domaine : **l'appartenance nationale, l'identité d'un acteur et sa relation à un État sont trois objets distincts, et c'est la relation qui classe.** Une phrase, à la suite de l. 157.

---

## 5. Usages conditionnels : ils exigent d'élargir le sujet de l'article

Ces usages ont une vraie valeur probatoire, mais **ils demandent de nommer des acteurs et un objet géopolitique**. Ce n'est plus un enrichissement, c'est un autre article. Je les expose pour que la décision soit explicite, pas pour les recommander.

| Réf. | Apport | Ce qu'il apporte à l'article | Prix |
| --- | --- | --- | --- |
| S1 | Le cas à objectif déclaré contredit (INV-027) | un quatrième palier, entre « non établi » et « établi contraire » : la relation est non seulement non établie, elle échoue au test le plus évident alors que la capacité est riche | nommer l'acteur et l'issue ; risque d'instrumentalisation élevé |
| S2 | Un second taux de base : 82 déclarations d'invitation à voyager par 47 députés sous la XVIIe législature, dont 38 financées par un même acteur, 6 par Taïwan, 4 par le Qatar (INV-161, source AN à revérifier) | un second « taux de base rare » comparable à HATVP 751 / 639 / 95,5 % (l. 147), avec deux financeurs de comparaison | nommer l'acteur ; et le rapport de l'Assemblée doit être relu avant usage |
| S3 | Le décalage de dénominateur (1,034 M$ de subvention contre 100 à 200 k€ déclarés) | une seconde illustration de M3, chiffrée | nommer l'acteur |
| S4 | Le tasking contractuel de projet : cofinancement à 50/50, critères de sélection, jalons, justificatifs de dépenses et rapports conditionnant le paiement (INV-162) | un degré intermédiaire documenté dans l'échelle de l. 149, entre « financement = moyens » et « ordre » | INV-162 est `PARTIAL_PHYSICAL_RECOVERY` sans certification, et la page primaire du dispositif n'était plus inspectable au moment du run |

Sur S2, une divergence à trancher si l'option est retenue : une mémoire antérieure du corpus annonce « 60+ voyages parlementaires » quand INV-161 compte 38 invitations financées sur une législature. Les deux peuvent être vrais sur des périodes différentes, mais il faut le vérifier avant publication.

---

## 6. Ce qu'il ne faut pas faire

1. **Ne pas reprendre la constatation FCT-008 d'INV-166.** Elle n'est pas reproductible. Le détail est en partie 7.
2. **Ne pas citer comme fait** les investigations en `PARTIAL_PHYSICAL_RECOVERY` : INV-158 (aucun fichier d'investigation), INV-159 (deux fichiers, aucune investigation), INV-161 (pas de run state), INV-162 (pas de certification).
3. **Ne pas citer les huit investigations seulement planifiées** (INV-164 à 172) : elles sont passées en revue, pas courues. Un plan n'est pas une pièce.
4. **Ne pas importer le conflit de convergence comme preuve.** L'article refuse explicitement de lire une collection de cas convergents comme une démonstration (l. 250 : « Ces dossiers ne sont pas une collection d'exemples convergents »). Le second corpus butte au même endroit, ce qui est un résultat de méthode sur la documentation, pas un fait sur le monde. Et l'article ne cite que des sources nommées : l'invoquer sans le nommer violerait sa propre règle de sourçage ; le nommer, c'est changer son sujet.
5. **Ne pas importer l'affaire Rokh Solis** (INV-169) : le commanditaire est inconnu selon la source primaire et le gap d'accès est qualifié de sévère par le programme lui-même.
6. **Ne pas importer le lawfare** (INV-159, INV-172) ni les voyages de presse (INV-164) : non courus, ou hors du périmètre probatoire de l'article.

---

## 7. Défaut détecté dans le bundle, avec sa preuve

**INV-166, fait FCT-008, statut `SUPPORTED`, matérialité `IMPORTANT`** :

> « The current public list contains registered actors including APCO Worldwide, COM PUBLICS, Forward Global and others, but no entity named ELNET appears on the inspected list. »

**Ce fait ne se reproduit pas.** La page citée par le run, `https://www.hatvp.fr/repertoire-de-linfluence-etrangere/liste-des-entites-influence-enregistrees/`, interrogée le 13 septembre 2026, affiche :

> « Le répertoire apparaîtra dès que les premiers enregistrements auront été traités par les équipes de la HATVP. »

Aucune entité n'y est publiée. Or APCO Worldwide, COM PUBLICS et Forward Global sont des acteurs du **répertoire des représentants d'intérêts**, registre de lobbying distinct, qui affiche de son côté « 0 sur 4080 entités ». L'hypothèse la plus probable est donc une **transposition depuis l'autre registre**. Je n'ai pas pu trancher définitivement : la page a pu changer entre le run et ma vérification, ou charger sa liste en JavaScript.

**Portée de ce défaut.** Il ne renverse pas la conclusion d'INV-166, qui refusait déjà correctement l'inférence « absence au registre donc manquement » (CAU-004, statut `REFUTED`). Il la prive de son support factuel : la prémisse « la liste existe et l'acteur n'y figure pas » n'est pas établie. C'est un cas d'école de ce que vaut une constatation négative sur un registre qui ne publie rien, et c'est exactement le genre de chose que l'article appelle un « non mesuré » qui vaut mieux qu'une intuition.

**Effet sur l'article** : nul si l'on n'importe pas FCT-008. C'est le cas dans ma recommandation.

---

## 8. Propositions soumises à décision

Trois ajouts, tous vérifiés sur source primaire, tous bornés, aucun n'important d'affaire.

| | Proposition | Volume | Sources | Risque de régression |
| --- | --- | --- | --- | --- |
| P1 | Partie III, après l. 153 : le régime français d'influence étrangère nomme quatre relations (ordre, demande, direction, contrôle) et exige en outre une action destinée à influer ; il couvre la chaîne indirecte par intermédiaires ; il écarte les échanges prévus par des stipulations contractuelles. Le corpus d'application est vide à ce jour. | un paragraphe | [60] art. 18-11, [61] décret 2025-733 | faible : ajoute un instrument, ne retire rien |
| P2 | Partie III, dans le même passage : l'article 433-2 du code pénal se contente d'une influence « réelle ou supposée », l'article 18-11 exige une relation effective. Deux régimes contigus, deux calibrages. | deux à trois phrases | [41] et [60], déjà au registre | faible : sert F-11, aucun terme de la série n'est touché |
| P3 | Partie I, à l. 89 : le droit français définit le mandant étranger par seuil, « dirigée ou contrôlée » ou « financée pour plus de la moitié », là où « investisseur lié à un État » ne discrimine pas. | une phrase | [60] | faible : renforce la critique déjà présente |

Deux règles de méthode, gratuites et sans domaine :

| | Proposition | Volume |
| --- | --- | --- |
| P4 | Ajouter aux conditions de l. 243 à 248 une septième exigence : que l'objectif de l'acteur soit documenté **avant** l'issue (M1). | une ligne de liste |
| P5 | Ajouter à l. 157 une phrase : l'appartenance, l'identité et la relation à un État sont trois objets distincts, et c'est la relation qui classe (M4). | une phrase |

**Coût total** : environ 300 mots, deux entrées de registre, aucun changement de série terminologique, donc aucun impact sur T1 ni sur les tranches suivantes. Les trois propositions sont indépendantes de T2 à T6 et peuvent être appliquées dans n'importe quel ordre.

**Ce que P1 à P3 ne font pas** : elles n'ajoutent aucune affaire, aucun acteur nommé, aucune accusation, et ne touchent pas au plafond probatoire de l'article. Elles ajoutent une institution de droit français récente qui **dit la même chose que l'article**, ce qui est le seul apport de ce bundle qui soit à la fois fort et sans risque d'instrumentalisation.

---

## 9. Verdict

Le bundle est de bonne qualité interne et sa convergence avec l'article est réelle, mais **presque tout son contenu probatoire est inutilisable pour cet article sans en changer le sujet**. Ce qu'il faut en prendre tient en trois textes de loi vérifiés et deux règles de méthode. Ce qu'il faut en refuser, c'est l'importation d'affaires : la valeur rhétorique serait immédiate et le coût épistémique aussi, parce que l'article devrait alors citer des acteurs nommés sur des relations qu'il déclare lui-même non établies.

Un point à retenir pour la suite du dossier : le bundle contient **le seul contrôle négatif à objectif préalablement déclaré** que j'aie vu dans les deux corpus, et il est structurellement supérieur aux deux contrôles négatifs actuels de l'article. Si un jour l'article accepte d'élargir son périmètre, c'est là qu'est la pièce la plus forte. En l'état, sa forme importable est la règle P4, et elle vaut d'être prise.
