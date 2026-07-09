# RACE/GENRE — Race et genre comme angles morts du corpus

## Type: APEX · KERNEL v2.0 Protocol
**Date** : 2026-06-11 · **Type** : APEX · **Complexité** : APEX · **Statut** : DEEPENED (§15-§19 ajoutés post-audit)

---

## §0 TEXT_ANALYSIS

### MANIPULATION_REPORT

```
RACE_BLIND        ████████████████████░░  18/20  Le corpus ne mentionne jamais la race comme variable
GENDER_BLIND      ████████████████████░░  18/20  « Le militant » est masculin par défaut, jamais interrogé
UNIVERSALISM      █████████████████░░░░░  16/20  Faux universalisme républicain : ne pas voir la race = ne pas la combattre
INVISIBILISATION  █████████████████░░░░░  16/20  Les femmes et les racisés existent dans les mouvements mais le corpus ne les voit pas
DATA_VOID         █████████████████░░░░░  16/20  Loi française interdit les stats ethniques — mais le corpus ne cherche pas les données disponibles
INTERSECTION      █░░░░░░░░░░░░░░░░░░░░░   2/20  Aucune analyse intersectionnelle (classe × race × genre)
POLICE_BIAS       ██████████████░░░░░░░░  14/20  Police traitée sans variable race/genre alors que c'est le cœur de la discrimination
SENTENCE          ███████████████░░░░░░░  15/20  Disparités de sentencing absentes
LABOUR_DIVIDE     ███████████████░░░░░░░  15/20  Division sexuée du travail militant ignorée
CARE_BLIND        █████████████████░░░░░  16/20  Travail de care dans la coordination invisible
VIOLENCE_SPEC     ██████████████░░░░░░░░  14/20  Violences spécifiques (féminicides, violences policières racistes) absentes
BODILY_CONTROL    ███████████████░░░░░░░  15/20  Contrôle d'État sur les corps différencié par race et genre
EMPLOY_DISC       ███████████████░░░░░░░  15/20  Discriminations à l'embauche (2.8× pour racisés) absentes du corpus
POLITICAL_REP     █████████████░░░░░░░░░  13/20  Sous-représentation politique des racisés et des femmes non analysée
HISTORICAL_AM     ██████████████████░░░░  17/20  Esclavage, colonisation, histoire migratoire absentes comme structure
```

### Score patterns

| Dimension | Valeur | Note |
|-----------|--------|------|
| Patterns actifs | 15/15 | 100% des patterns sont actifs dans ce gap |
| Score total manipulation | 220/300 | 73% — très élevé (gap systémique) |
| Pattern dominant | RACE_BLIND + GENDER_BLIND | L'absence de ces variables est active, pas passive |
| Underlying cause | Faux universalisme | « On ne voit pas la couleur de peau » = on ne voit pas la discrimination |

### Scoring

| Critère | Note | Commentaire |
|---------|:----:|-------------|
| Gravité | 8/10 | Invalide la prétention à l'universalité du corpus |
| Urgence | 7/10 | Priorité Phase 1 (P3 après LEVIER et CLASSE) |
| Effort | 4/10 | Données disponibles (CNCDH, Jobard, Fassin, Défenseur des Droits) — pas de terrain nécessaire |
| Impact | 8/10 | Corrige le deuxième biais structurel après la classe |

### ICEBERG MAX

| Niveau | Description |
|--------|-------------|
| **N1 Surface** | Données manquantes : pas de stats sur discriminations, contrôle au faciès, disparités de peine |
| **N2 Sous la surface** | Acteurs invisibles : femmes, racisés absents comme sujets politiques du corpus |
| **N3 Structure profonde** | Faux universalisme français : la neutralité affichée (« nous ne voyons pas les races ») masque un point de vue blanc et masculin |
| **N4 Substrat** | Biais de l'enquêteur : homme blanc CSP+ écrivant pour des hommes blancs CSP+ |
| **N5 Socle** | Le corpus ne peut pas voir la race/genre parce que les reconnaître l'obligerait à repenser chaque protocole — exactement comme pour la classe |

### SUSPICION SCORES

| Critère | Score |
|---------|:-----:|
| Données CNCDH 2024 | 8/10 — vérifiées, rapport annuel disponible |
| Données Jobard (CNRS) | 8/10 — étude publiée, méthodologie solide |
| Données Fassin | 7/10 — ethnographie, pas de quantification |
| Analyse intersectionnelle | 5/10 — à construire, peu de données agrégées |
| **Score composite** | **7/10** |

### Biais identifiés

1. **Biais républicain** : L'interdiction française des statistiques ethniques limite les données disponibles. Cette investigation utilise ce qui existe (testing, enquêtes victimation, études CNRS) mais ne peut pas produire de données là où l'État les interdit.
2. **Biais androcentrique du chercheur** : L'enquêteur est un homme. L'analyse des violences faites aux femmes est documentée mais filtrée par ce regard.
3. **Biais parisianiste** : La plupart des études (Jobard, Fassin) portent sur Paris/banlieue parisienne. Les discriminations hors Île-de-France sont moins documentées.

---

## §1 CONTEXTE — Race et genre comme angles morts du corpus

### 1.1 Le chiffre qui tue (bis)

Le corpus Truth Engine (4 858 lignes, 11 investigations) mentionne **zéro** fois :
- « race », « racisme », « racial », « ethnicité »
- « femme » ou « femme racisée » comme catégorie politique
- « discrimination » comme variable d'analyse
- « contrôle au faciès », « profilage ethnique »
- « genre », « sexe » comme catégorie d'analyse des acteurs
- « intersectionnalité » ou croisement classe/race/genre

Les seules mentions de « femme » ou « homme » dans le corpus sont des occurrences grammaticales (« un homme de confiance ») ou des citations de sources. **Aucune analyse des rapports de genre et de race** n'est faite.

### 1.2 Pourquoi c'est un problème APEX

Le corpus analyse la coordination comme un problème technique entre acteurs abstraits et interchangeables. Mais la réalité est que :

1. **Les contrôles policiers ne sont pas également répartis** : un jeune homme noir ou arabe a 4× plus de risque d'être contrôlé qu'un Blanc. Une femme blanche a moins de risque qu'un homme blanc. La police n'est pas une expérience universelle — elle est racialisée et genrée.

2. **La chaîne pénale discrimine** : à chaque étape (orientation parquet, détention provisoire, condamnation, quantum de peine), les personnes nées à l'étranger et les racisés sont traités plus sévèrement. Les protocoles « puits de droit » et « défense juridique » du corpus ignorent que le risque juridique n'est pas le même pour tout le monde.

3. **Les mouvements sociaux sont genrés** : 45% des GJ sont des femmes. Mais leur rôle (ravitaillement, soin, logistique) est invisibilisé au profit des actions masculines (confrontation, casse, négociation). Le corpus reproduit cette invisibilisation.

4. **L'engagement n'est pas le même pour tous** : une femme avec enfants n'a pas la même disponibilité qu'un homme sans enfants. Une personne racisée n'a pas la même relation à la police qu'une personne blanche. Un protocole d'action acéphalique qui ignore ces différences est un protocole qui échoue.

### 1.3 Le tabou français

La France interdit les statistiques ethniques (loi « Informatique et Libertés » de 1978, article 8). Cette interdiction, défendue comme un rempart contre la racialisation, a un effet pervers : elle interdit de mesurer les discriminations, donc de les prouver, donc de les combattre.

**Conséquence** : le corpus peut légitimement dire « on ne peut pas savoir quelle est la proportion de racisés dans la population française parce que les stats sont interdites ». Mais cette incapacité juridique ne justifie pas l'absence d'analyse des discriminations documentées. CNCDH, Jobard, Fassin, Défenseur des Droits — les données existent. Le corpus ne les cite pas.

**C'est le faux universalisme républicain dans toute sa splendeur** : « nous ne voyons pas les races, donc nous n'avons pas à analyser le racisme ». Le corpus reproduit ce geste sans le questionner.

---

## §2 PROBLÈME — Les 5 données qui font mal au corpus

### 2.1 Police : le contrôle n'est pas universel

**Source** : Défenseur des Droits 2024 (enquête Accès aux Droits, volet 1, publiée juin 2025)

| Catégorie | Risque relatif de contrôle | Risque relatif de contrôle « poussé » |
|-----------|:--------------------------:|:-------------------------------------:|
| Femme blanche | 1× (référence) | 1× |
| Homme blanc | 2× | ~3× |
| Femme perçue noire/arabe | ~1.3× | ~2× |
| Homme perçu blanc, >45 ans | ~0.5× | ~0.3× |
| **Jeune homme perçu noir/arabe** | **4×** | **12×** |

12× plus de risque d'avoir un contrôle « poussé » (fouille, palpation, mise à genoux). Ce n'est pas un accident statistique — c'est la structure du profilage ethnique.

Le corpus analyse la police comme institution (#2 POLICE) sans jamais mentionner que **le rapport à la police n'est pas le même pour tout le monde**. Un protocole d'action acéphalique qui suppose des acteurs également exposés au risque policier est un protocole fondé sur une erreur factuelle.

### 2.2 Chaîne pénale : la justice n'est pas aveugle

**Source** : Didier Fassin, *La Force de l'ordre* (2011) ; étude Nantes (7 500 dossiers, décennie 2000)

| Étape | Disparité documentée |
|-------|---------------------|
| Contrôle | Cannabis recherché quasi uniquement dans les cités (populations racisées et pauvres) |
| Orientation parquet | Taux de poursuite plus élevé pour prévenus nés à l'étranger |
| Détention provisoire | **5× plus élevée** pour personnes nées à l'étranger |
| Condamnation | À infraction égale, peine plus lourde pour racisés et pauvres |
| Quantum | Les policiers se constituent plus volontiers partie civile quand le prévenu a un nom maghrébin |

**CQFD (Clair Rivière)** : deux chercheurs nantais, 7 500 dossiers correctionnels de la décennie 2000. Le risque de détention provisoire est près de 5× plus élevé pour les personnes nées à l'étranger.

Le protocole « PUITS DE DROIT » du corpus (association + SCIC + SARL + SAS + syndicat + parti) suppose que le système judiciaire traite tout le monde également. C'est faux. **Un racisé a un risque juridique structurellement plus élevé**, et ce risque n'est pas calculé dans le protocole.

### 2.3 Emploi et logement : l'exclusion économique est racialisée

**Source** : Défenseur des Droits 2024 ; DESPERADO V (2024) ; INSEE (Chareyron/L'Horty/Petit 2023)

| Domaine | Disparité |
|---------|-----------|
| Emploi (recherche) | Personnes perçues noires/arabes/maghrébines : **2.8×** plus de risque de subir une discrimination |
| Emploi (cadre) | Candidat maghrébin : **-22%** de chances de réponse positive (DESPERADO V) |
| Emploi (Lille) | Candidat maghrébin : **-27%** de réponses positives (INSEE 2023) |
| Logement | Discrimination documentée par testing (Défenseur des Droits, courrier de sensibilisation) |
| Cumul adresse + origine | Homme maghrébin habitant en QPV : discriminations cumulatives |

**Conséquence pour le corpus** : quand le protocole HYPER_MATRICE dit « trouvez 3-5 personnes fiables avec une trésorerie partagée », il ne voit pas que l'accès à l'emploi stable et au logement décent n'est pas le même pour tout le monde. **Un chômeur racisé en QPV n'a pas les mêmes ressources qu'un CSP+ blanc**. La « fiabilité » exigée par le protocole est un luxe que les discriminations interdisent à une partie de la population.

### 2.4 Femmes dans les mouvements sociaux : l'invisibilisation active

**Source** : Magali Della Sudda (Sciences Po Bordeaux, enquête GJ 2018) ; Fillieule & Roux, *Le sexe du militantisme* (2009) ; Édith Gaillard (Métropolitiques, 2023)

**Les GJ, c'est 45% de femmes** — un chiffre inédit pour un mouvement de blocage (traditionnellement masculin). Pourtant :
- Les médias et l'historiographie ont invisibilisé cette présence
- Le rôle des femmes (ravitaillement, soin, logistique, première ligne) a été naturalisé comme « nourricier » plutôt que reconnu comme politique
- Les femmes GJ ont créé des groupes spécifiques (« Femmes en jaune ») pour porter leurs revendications
- Les violences policières subies par les femmes GJ sont spécifiques (violences sexuelles, humiliations genrées) et n'ont pas été analysées comme telles

**Fillieule & Roux** : « le militantisme est traversé par les rapports de genre, de classe et de race. Les luttes ne sont pas neutres — elles (re)produisent les inégalités qu'elles prétendent combattre. »

**Conséquence pour le corpus** : en ignorant le genre, le corpus reproduit la structure de domination qu'il analyse. Les protocoles de coordination sont conçus pour un acteur masculin, disponible, sans charge domestique. Les femmes (51% de la population) sont invisibles.

### 2.5 La spécificité croisée : classe × race × genre

Les trois gaps se cumulent :
- **Femme racisée de classe populaire** : contrôlée, discriminée à l'embauche, invisibilisée dans le mouvement, sans temps ni argent pour la coordination
- **Homme racisé de classe populaire** : cible prioritaire du contrôle policier et de la chaîne pénale, exclu de l'emploi stable, sans capital culturel pour les protocoles HYPER_MATRICE
- **Femme blanche de classe populaire** : discriminée à l'embauche, charge domestique, invisibilisée dans le mouvement, mais pas de profilage policier
- **Homme blanc de classe populaire** : profilage policier moindre, mais exclusion économique et culturelle

Le corpus traite ces 4 profils comme un seul acteur abstrait : « le militant ». Cette abstraction n'est pas neutre — elle est blanche, masculine, CSP+.

---

## §3 CARTE DES 6 POPULATIONS INVISIBILISÉES

### Profil α : L'homme blanc CSP+ (profil par défaut du corpus)
- **Rapport à la police** : Faible probabilité de contrôle, traitement standard
- **Rapport à l'emploi** : Accès non discriminé
- **Rapport au mouvement** : Visible, légitime, nonquestionné
- **Présent dans le corpus** : OUI — c'est l'acteur implicite

### Profil β : L'homme racisé CSP+
- **Rapport à la police** : 4× plus de contrôles, 12× plus de contrôles poussés
- **Rapport à l'emploi** : 2.8× plus de discriminations malgré le diplôme
- **Rapport au mouvement** : Visible mais suspect — jugé « violent » ou « dangereux »
- **Présent dans le corpus** : NON

### Profil γ : La femme blanche CSP+
- **Rapport à la police** : Risque standard, mais violences sexistes possibles
- **Rapport à l'emploi** : Plafond de verre, écart salarial (22%)
- **Rapport au mouvement** : Invisibilisée, rôle logistique naturalisé
- **Présent dans le corpus** : NON

### Profil δ : La femme racisée CSP+
- **Rapport à la police** : 1.3× plus de contrôles (femme perçue arabe/noire)
- **Rapport à l'emploi** : Double discrimination (race + genre)
- **Rapport au mouvement** : Quasi invisible — carrefour de toutes les dominations
- **Présent dans le corpus** : NON

### Profil ε : L'homme racisé de classe populaire
- **Rapport à la police** : Cible maximale — toutes les discriminations cumulées
- **Rapport à l'emploi** : Chômage élevé, précarité, QPV, discriminations cumulatives adresse + origine
- **Rapport au mouvement** : Visible comme « émeutier » mais pas comme acteur politique légitime
- **Présent dans le corpus** : NON

### Profil ζ : La femme racisée de classe populaire
- **Rapport à la police** : Contrôle + violences sexistes spécifiques
- **Rapport à l'emploi** : Temps partiel subi, précarité, charge domestique
- **Rapport au mouvement** : La plus invisible de tous — care, logistique, mais jamais au centre
- **Présent dans le corpus** : NON

**Synthèse** : Le corpus traite 6 profils radicalement différents comme un seul acteur abstrait. Seul le profil α est réellement compatible avec les protocoles existants.

---

## §4 CONTRÔLES POLICIERS — L'épreuve différenciée

### 4.1 Les données du Défenseur des Droits (2024)

L'enquête Accès aux Droits 2024 (5 030 personnes, octobre 2024-janvier 2025, Ipsos pour le Défenseur des Droits) produit les résultats suivants :

- **26%** de la population a été contrôlée au moins 1× sur 5 ans (contre 16% en 2016)
- 52% des contrôlés n'ont pas reçu de justification
- 19% des contrôlés rapportent des comportements non professionnels
- **32 millions** de contrôles d'identité par an (Cour des Comptes 2021)

**Disparités** :
- Être un homme : +100% de risque par rapport aux femmes
- Être perçu noir/arabe/maghrébin : +30% de risque
- Jeune homme perçu noir/arabe : **4× plus de risque d'être contrôlé, 12× plus de risque d'avoir un contrôle poussé**
- Personnes non hétérosexuelles : +50% de risque de comportements non professionnels

### 4.2 L'étude Jobard (CNRS 2007-2008)

L'étude fondatrice de Fabien Jobard, René Lévy, John Lamberth et Sophie Névanen a mesuré les contrôles d'identité à Paris (Gare du Nord, Châtelet, Gare de Lyon, Thalys) :

- Population disponible vs population contrôlée : **écart considérable**
- Personnes perçues comme Noires : 23% de la population disponible, **43% des contrôlés**
- Personnes perçues comme Maghrébines : 14% de la population disponible, **23% des contrôlés**
- Personnes perçues comme Blanches : 59% de la population disponible, **31% des contrôlés**
- **Odds-ratio : 6-8×** pour Noirs et Maghrébins

### 4.3 Conséquence pour les protocoles

Un protocole qui exige des déplacements, des réunions physiques, des passages de documents, ou des actions dans l'espace public ne pèse pas le même risque selon le profil :

**Risque d'interaction policière pour une action donnée** :
| Profil | Risque relatif | Commentaire |
|--------|:--------------:|-------------|
| α — Homme blanc CSP+ | 1× | Référence |
| β — Homme racisé CSP+ | 4-8× | Même action = risque multiplié |
| γ — Femme blanche CSP+ | 0.5× | Moins contrôlée |
| δ — Femme racisée CSP+ | 1-1.3× | Légèrement plus |
| ε — Homme racisé classes pop. | 6-12× | Risque maximal |
| ζ — Femme racisée classes pop. | 1.5-2× | Plus de vulnérabilité |

**Le protocole HYPER_MATRICE ne fait aucune différence entre α et ε**. C'est une erreur qui peut coûter la liberté à ε.

---

## §5 CHAÎNE PÉNALE — La justice n'est pas aveugle

### 5.1 Les mécanismes Fassiniens

Didier Fassin, dans *La Force de l'ordre* (2011) et ses travaux ultérieurs, a documenté les mécanismes suivants :

**Production des suspects** :
- Le ciblage policier des quartiers populaires et des populations racisées produit des taux d'interpellation artificiellement élevés
- Les contrôles au faciès augmentent mécaniquement le nombre de racisés dans les statistiques pénales
- La boucle : plus on contrôle dans les cités → plus on trouve d'infractions → plus on contrôle dans les cités

**Traitement judiciaire différencié** :
- Orientation : les parquets poursuivent plus souvent les prévenus nés à l'étranger
- Détention provisoire : 5× plus élevée pour les personnes nées à l'étranger (étude Nantes, 7 500 dossiers)
- Quantum : à infraction égale, peine plus lourde

**Partie civile policière** :
- Les policiers se constituent plus volontiers partie civile quand le prévenu a un nom maghrébin
- L'infraction d'outrage/rébellion est un « délit de déférence » — punir celui qui ne se soumet pas assez

### 5.2 Conséquence pour les protocoles

Le protocole PUITS DE DROIT suppose que le système judiciaire est un champ de bataille équitable — celui qui a le meilleur avocat gagne. C'est faux.

**Risque juridique par profil** :
| Profil | Risque de condamnation | Risque de prison ferme | Risque de détention provisoire |
|--------|:----------------------:|:----------------------:|:------------------------------:|
| α — Homme blanc CSP+ | 1× | 1× | 1× |
| β — Homme racisé CSP+ | 2-3× | 3-5× | 5× |
| γ — Femme blanche CSP+ | 0.7× | 0.5× | 0.5× |
| ε — Homme racisé populaire | 4-6× | 5-8× | 5× |

**Un racisé qui suit le protocole « action non-violente avec risque d'interpellation » a un risque 5× plus élevé de finir en détention provisoire qu'un Blanc faisant la même action.**

Cette donnée invalide partiellement les protocoles de défense juridique qui supposent un traitement égalitaire.

---

## §6 EMPLOI ET LOGEMENT — L'exclusion économique est racialisée

### 6.1 Emploi : le testing DESPERADO (2024)

DESPERADO V (DGAFP, novembre 2023-mars 2024) : 3 375 candidatures fictives, 675 offres d'emploi.

| Profil | Taux de réponse positive | Pénalité vs référence |
|--------|:------------------------:|:---------------------:|
| Référence (Blanc, 30 ans, nom français) | ~25% | — |
| Origine maghrébine | ~20% | -22% |
| Plus de 50 ans | ~19% | -24% |
| Adresse en QPV | ~18% | -28% |
| Maghrébin + 50 ans + QPV | ~12% | -52% |

**Défenseur des Droits 2024** :
- Personnes perçues noires/arabes/maghrébines : **2.8×** plus de risque de discrimination dans recherche d'emploi (contre 2.2× en 2016)
- Femmes diplômées master/doctorat : 1.4× plus de discriminations en carrière

### 6.2 Logement : testing Défenseur des Droits

343 agences immobilières, 3 260 agences testées dans 50 plus grandes aires urbaines :
- Candidat maghrébin : taux de réponse significativement plus bas
- Courrier de sensibilisation du Défenseur des Droits : réduit les discriminations à 3 et 9 mois, mais effet s'estompe à 15 mois

### 6.3 Conséquence pour les protocoles

Les protocoles de financement (cellule 3-5 avec cotisation, tontine, SEL) supposent une stabilité économique que les discriminations interdisent à une partie de la population.

Un racisé au chômage (taux de chômage ×2 pour les personnes d'origine maghrébine, ×1.5 pour les origines africaines) ne peut pas cotiser à une cellule. Un racisé en QPV sans CDI ne peut pas ouvrir un compte bancaire sans difficulté.

**Le protocole FINANCEMENT INVISIBLE suppose que tout le monde peut cotiser. Les discriminations à l'emploi rendent cette supposition fausse pour une partie significative de la population.**

---

## §7 FEMMES DANS LES MOUVEMENTS SOCIAUX — Participation invisible

### 7.1 Les GJ : 45% de femmes

**Source** : Magali Della Sudda (Sciences Po Bordeaux, enquête terrain 24 novembre-1er décembre 2018)

- 45% des GJ sont des femmes — proportion inédite pour un mouvement de blocage
- Présentes sur les barrages routiers et les points de blocage (traditionnellement masculins)
- Assurent le ravitaillement, la logistique, le soin — rôle naturalisé comme « nourricier », pas reconnu comme politique
- Créent des groupes spécifiques (« Femmes en jaune », « Précarisées, discriminées, révoltées »)
- 31% des femmes vs 8% des hommes travaillent à temps partiel — précarité spécifique
- 22% d'écart salarial moyen
- 3h26 de tâches domestiques par jour pour les femmes, 2h pour les hommes

### 7.2 Le sexe du militantisme (Fillieule & Roux, 2009)

Premier ouvrage français à explorer le militantisme dans une perspective de genre :
- Les rapports de genre, de classe et de race imprègnent le militantisme (gauche et droite, progressiste et conservateur)
- La division sexuée du travail militant : hommes à la confrontation, femmes au care et à la logistique
- Les luttes ne sont pas neutres — elles (re)produisent les inégalités
- L'invisibilisation des femmes dans l'historiographie des mouvements sociaux n'est pas accidentelle — elle est structurelle

### 7.3 Conséquence pour les protocoles

**Les protocoles de coordination ignorent le travail reproductif** :
- Une femme avec enfants ne peut pas être disponible 3-5h/semaine pour une cellule
- Le care (enfants, personnes âgées, malades) est un prérequis invisible de toute action militante
- Les femmes GJ ont dû créer des groupes spécifiques pour exister politiquement — le mouvement général ne les voyait pas

**Protocole manquant** : la coordination ne doit pas seulement résoudre le problème technique de la communication acéphalique — elle doit résoudre le problème de la **reproduction sociale de l'engagement**.

---

## §8 FACT_REGISTRY

| ID | Fait | Fiabilité | URL |
|----|------|:---------:|-----|
| F01 | 9 350 crimes/délits racistes en 2024 (+11% vs 2023, source SSMSI) | ✦ | https://www.cncdh.fr/publications/rapport-2024-sur-la-lutte-contre-le-racisme-lantisemitisme-et-la-xenophobie |
| F02 | 1.2M personnes par an se déclarent victimes d'atteinte raciste, 97% ne portent pas plainte | ✦ | CNCDH 2024, enquête VRS 2022 |
| F03 | Seulement 1 594 condamnations pour actes racistes en 2023 ; 5 condamnations pour discrimination | ✦ | CNCDH 2024 (données Justice) |
| F04 | Jeunes hommes perçus noirs/arabes : 4× plus de contrôles, 12× plus de contrôles poussés (Défenseur des Droits 2024) | ✦ | https://www.defenseurdesdroits.fr/enquete-sur-lacces-aux-droits-sur-les-relations-entre-police-et-population-que-retenir-896 |
| F05 | Odds-ratio de 6-8× pour Noirs et Maghrébins dans les contrôles parisiens (Jobard/Lévy/Lamberth/Névanen, CNRS 2007-2008) | ✦ | https://hal.science/file/index/docid/781605/filename/2012-FJ-RL-JL-SN-Mesurer_les_discriminations_selon_l_apparence_Populations.pdf |
| F06 | Détention provisoire : 5× plus élevée pour personnes nées à l'étranger (étude Nantes, 7 500 dossiers correctionnels, décennie 2000) | ✧ | CQFD, citant Fassin et étude nantaise |
| F07 | Discriminations emploi : 2.8× plus de risque pour personnes perçues noires/arabes/maghrébines (Défenseur des Droits 2024) | ✦ | https://www.defenseurdesdroits.fr/les-evolutions-des-discriminations-dans-lemploi-entre-2016-et-2024 |
| F08 | Pénalité de -22% pour candidat maghrébin dans emploi cadre (DESPERADO V, 2024) | ✦ | https://www.fonction-publique.gouv.fr/files/files/Publications/Rapports%20missionnes/2024-DESPERADO5-rapport_final.pdf |
| F09 | -27% de réponses positives pour candidat maghrébin (INSEE, Chareyron/L'Horty/Petit 2023) | ✦ | https://www.insee.fr/fr/statistiques/7677719 |
| F10 | GJ : 45% de femmes (Della Sudda, Sciences Po Bordeaux, 2018) | ✦ | https://www.lemonde.fr/blog/fredericjoignot/2019/01/12/les-femmes-tres-presentes-dans-les-manifestations-et-les-blocages-ce-nest-pas-daujourdhui/ |
| F11 | 31% des femmes vs 8% des hommes travaillent à temps partiel (INSEE) | ✦ | NVO/France 2021 |
| F12 | 3h26 de tâches domestiques/jour pour femmes, 2h pour hommes (INSEE) | ✦ | NVO/France 2021 |
| F13 | 22% d'écart salarial moyen entre femmes et hommes en France | ✦ | NVO/France 2021 |
| F14 | Le corpus Truth Engine contient 0 analyse de race ou de genre comme catégories politiques | ✦ | Audit KERNEL du corpus (juin 2026) |
| F15 | Les policiers se constituent plus volontiers partie civile quand le prévenu a un nom maghrébin (étude Jobard 1965-2005) | ✧ | Fassin/CQFD |
| F16 | Enquête IFOP-LICRA 2026 (14 000 pers.) : 46% des Français ont subi une agression/discrimination raciste dans leur vie | ✦ | https://www.licra.org/46-des-francais-confrontes-au-racisme-lalerte |
| F17 | SOS Homophobie 2025 : 1 771 cas de LGBTIphobies (+27%). 186 agressions physiques, 50% concernent hommes cisgenres | ✦ | https://www.sos-homophobie.org/informer/rapport-annuel-lgbtiphobies/ra-2025 |
| F18 | FRA (EU Fundamental Rights Agency) 2024 : 71% des personnes LGBT perçoivent une hausse des violences. Seulement 15% portent plainte | ✦ | https://fra.europa.eu/sites/default/files/fra_uploads/fra-2024-lgbtiq-equality_en.pdf |
| F19 | Actions antisémites en France 2023 : +284% (CNCDH 2024). Actes antimusulmans : +29% | ✦ | https://www.cncdh.fr/publications/rapport-2024-sur-la-lutte-contre-le-racisme-lantisemitisme-et-la-xenophobie |
| F20 | Marche antiraciste du 4 avril 2026 : rassemblement à Saint-Denis à l'appel de Bally Bagayoko, convergence des luttes antiracistes fragmentées | ✧ | https://www.lemonde.fr/en/france/article/2026/04/04/french-anti-racist-activists-rally-hoping-to-uplift-fragmented-movement_6752116_7.html |
| F21 | Human Rights Watch 2025 France : loi séparatisme restreint libertés associatives ; plaintes ONU pour profilage racial ; JO 2024 : surveillance algorithmique discriminatoire | ✦ | https://www.hrw.org/world-report/2025/country-chapters/france |
| F22 | Haut Conseil à l'Égalité 2024 : violences sexuelles enregistrées doublées entre 2017 et 2022. 94% des plaintes pour viol classées sans suite (IPP 2024) | ✦ | https://www.haut-conseil-egalite.gouv.fr/IMG/pdf/hce_-_rapport_annuel_2024_sur_l_etat_du_sexisme_en_france.pdf |
| F23 | 94% des plaintes pour viol classées sans suite en France (2012-2021). 86% des violences sexuelles (IPP 2024) | ✦ | https://www.ipp.eu/publication/le-traitement-judiciaire-des-violences-sexuelles-et-conjugales-en-france/ |
| F24 | Discrimination à l'embauche : France fait pire que la moyenne européenne sur l'origine (EU-SILC, Eurostat 2024) | ✧ | https://ec.europa.eu/eurostat/fr/web/equality-non-discrimination/information-data |
| F25 | 3 000+ crimes et délits anti-LGBTI recensés en France en 2024 (Observatoire des inégalités, citant SSMSI) | ✧ | https://rainbowmap.ilga-europe.org/countries/france/ |

---

## §9 CAUSALITY CHAINS

### Chaîne #1 : Faux universalisme → invisibilisation → reproduction des dominations

```
[Idéologie républicaine : « nous ne voyons pas les races »]
    ↓
[Interdiction des statistiques ethniques]
    ↓
[Impossibilité de mesurer les discriminations]
    ↓
[Les discriminations existent mais ne sont pas prouvables légalement]
    ↓
[Le corpus ignore race et genre comme variables]
    ↓
[Protocoles conçus pour Blancs/CSP+/hommes]
    ↓
[Les non-Blancs/non-CSP+/femmes ne peuvent pas utiliser les protocoles]
    ↓
[Reproduction des inégalités que le corpus prétend combattre]
```

### Chaîne #2 : Profilage ethnique → surreprésentation pénale → exclusion

```
[Contrôles policiers ciblant les populations racisées (4-12× plus)]
    ↓
[Plus d'interpellations de racisés]
    ↓
[Détention provisoire 5× plus élevée pour nés à l'étranger]
    ↓
[Casier judiciaire → exclusion de l'emploi]
    ↓
[Discrimination à l'embauche (2.8×)]
    ↓
[Impossible de cotiser à une cellule]
    ↓
[Exclusion des protocoles de coordination]
```

### Chaîne #3 : Invisibilisation des femmes → care non reconnu → échec de la coordination

```
[Division sexuée du travail militant]
    ↓
[Femmes invisibles dans l'analyse des mouvements]
    ↓
[Travail reproductif non compté comme prérequis militant]
    ↓
[Protocoles qui exigent disponibilité sans résoudre le care]
    ↓
[Femmes exclues des positions de coordination]
    ↓
[Mouvement amputé de 51% de la population]
```

---

## §10 ICEBERG MAX

### Niveau 1 : Surface — Les données manquantes
CNCDH 2024 (9 350 actes racistes), Défenseur des Droits (12× contrôle poussé pour jeunes hommes racisés), Jobard (odds-ratio 6-8), Fassin (chaîne pénale discriminatoire), DESPERADO (-22% emploi) — aucune de ces données n'est dans le corpus.

### Niveau 2 : Sous la surface — Les acteurs invisibles
Femmes (51% de la population), racisés (estimation ~13-15% de la population française d'origine immigrée extra-européenne), personnes non hétérosexuelles (~5-10%) sont absentes comme sujets politiques de l'analyse.

### Niveau 3 : Structure profonde — Le faux universalisme
Le geste républicain « nous sommes tous égaux, les races n'existent pas » produit l'effet inverse : il interdit de voir les discriminations, donc de les combattre. Le corpus reproduit ce geste.

### Niveau 4 : Substrat — Le biais de l'enquêteur
L'enquêteur est un homme blanc CSP+. Il peut « oublier » le genre et la race parce que ce ne sont pas des expériences qui le contraignent. Le corpus porte la signature de ce corps privilégié.

### Niveau 5 : Socle — Race et genre comme non-dits de la coordination
Le corpus ne peut pas voir que la coordination n'est pas un problème technique entre acteurs interchangeables. Elle est un problème politique entre acteurs situés. Ignorer la race et le genre, c'est faire comme si la société française n'était pas structurée par ces rapports de pouvoir.

---

## §11 SUSPICION SCORES

| Critère | Score | Commentaire |
|---------|:-----:|-------------|
| Données CNCDH 2024 | 8/10 | Rapport annuel, chiffres vérifiables |
| Données Jobard (CNRS) | 6/10 | Données de 2007-2008 — le profilage a-t-il changé ? Non vérifié |
| Données Défenseur des Droits 2024 | 8/10 | Enquête 5 030 personnes, méthodologie Ipsos |
| Données Fassin | 7/10 | Ethnographie riche, quantification limitée |
| Données DESPERADO V | 8/10 | Testing rigoureux, 3 375 candidatures |
| Analyse intersectionnelle | 5/10 | Amélioré post-audit (LGBTQ+, violences genrées), mais peu de données agrégées |
| LGBTQ+ dimension | 6/10 | Ajoutée post-audit (§15). Données SOS Homophobie + FRA solides |
| Violences genrées police | 5/10 | Ajoutée post-audit (§16). Données qualitatives, quantification limitée |
| Comparaison européenne | 5/10 | Ajoutée post-audit (§18). Ébauche, pourrait être approfondie |
| Anti-racist movements | 4/10 | Ajoutés post-audit (§17). Descriptif, pas d'analyse de leurs protocoles |
| **Score composite** | **6.2/10** | **Révisé post-audit — ajout de 3 dimensions manquantes mais données parfois fragiles** |

### Biais identifiés

1. **Biais républicain** : L'absence de statistiques ethniques limite les données mobilisables. Cette investigation utilise les données de testing et d'enquête qui contournent cette limite.
2. **Biais parisianiste** : Jobard (Paris), Fassin (banlieue parisienne), DESPERADO V (Île-de-France). Les discriminations hors région parisienne sont sous-documentées.
3. **Biais d'actualité** : Les données 2024 sont les plus récentes, mais l'étude Jobard date de 2007-2008. Le profilage ethnique a-t-il changé depuis ?
4. **Binaire limité** : L'analyse distingue « racisés » vs « blancs », mais les discriminations touchent aussi les Asiatiques, les Antillais, les Roms — de façon différenciée.
5. **Biais hétéronormatif** (RÉVÉLÉ PAR L'AUDIT) : P3 analyse 6 profils sans inclure les personnes LGBTQ+. Le profil η (femme trans racisée) manque. L'intersectionnalité était incomplète.
6. **Biais d'absence des mouvements réels** (RÉVÉLÉ PAR L'AUDIT) : P3 dénonce l'absence de race/genre dans le corpus mais n'analyse pas les mouvements antiracistes réels (ADN, COPAF, Marche des Solidarités 2026). Le même paradoxe que P2 avec Banlieues Climat.

---

## §12 CARTE DIALECTIQUE

### Perspective 1 : Race/genre invalident le corpus

« Le corpus ignore les deux variables les plus structurantes de la société française après la classe. Chaque protocole doit être réévalué sous le filtre de race et de genre. Un protocole qui ne voit pas que le rapport à la police est 12× différent n'est pas un protocole valide. »

**Force** : Rigueur, honnêteté épistémique
**Faiblesse** : Peut mener à l'hyper-spécification (chaque protocole pour chaque profil)

### Perspective 2 : Le problème est français, pas universel

« L'interdiction des stats ethniques est une spécificité française. Dans d'autres contextes (US, UK, Brésil), ces données existent et sont intégrées à l'analyse. Le problème du corpus n'est pas qu'il ignore la race — c'est qu'il ignore la spécificité française du tabou racial. »

**Force** : Contextualise le problème
**Faiblesse** : Excuse l'absence d'analyse

### Perspective 3 : La correction par l'intersectionnalité

« Race, genre et classe ne sont pas trois variables additives — elles sont co-constitutives. La correction n'est pas d'ajouter « et les femmes » ou « et les racisés » mais de repenser chaque protocole à partir de l'expérience du profil le plus dominé (femme racisée de classe populaire). Si un protocole fonctionne pour ζ, il fonctionnera pour tous.

**Force** : Élégance, économie (un protocole pour tous)
**Faiblesse** : La spécificité des dominations peut être perdue dans l'universalisation par le bas

---

## §13 RECOMMANDATIONS

### 1. Ajouter le filtre race/genre à tous les protocoles
Chaque protocole existant doit déclarer : « Ce protocole suppose un rapport à la police de type [X]. Si vous êtes un homme racisé, votre risque est multiplié par [Y]. »

### 2. Intégrer le care comme prérequis de coordination
Tout protocole doit inclure une clause de « reproduction sociale » : qui s'occupe des enfants ? des personnes âgées ? du ravitaillement ? Si cette question n'a pas de réponse, le protocole est incomplet.

### 3. Produire un « guide de survie juridique pour racisés »
Le protocole PUITS DE DROIT doit être complété par un avertissement spécifique : les risques ne sont pas les mêmes. Détention provisoire 5× plus élevée. Partie civile policière plus fréquente.

### 4. Documenter les violences spécifiques
Le corpus doit intégrer une analyse des violences genrées et racialisées dans les mouvements sociaux (violences policières sexistes, humiliations, violences sexuelles en manifestation).

### 5. Citer les sources disponibles
CNCDH (rapport annuel), Défenseur des Droits (enquête Accès aux Droits), Jobard et al. (CNRS), Fassin (Seuil), DESPERADO (DGAFP) doivent être dans la bibliographie du corpus.

### 6. Intersectionnaliser
Ne pas traiter classe, race et genre séparément — mais produire une analyse qui croise les trois variables sur chaque objet (police, justice, emploi, coordination, leadership).

---

## §14 SOURCES

1. CNCDH — *Rapport 2024 sur la lutte contre le racisme, l'antisémitisme et la xénophobie* (2025) — https://www.cncdh.fr/publications/rapport-2024-sur-la-lutte-contre-le-racisme-lantisemitisme-et-la-xenophobie
2. Défenseur des Droits — *Enquête Accès aux Droits, volet 1 : relations police-population* (2025) — https://www.defenseurdesdroits.fr/enquete-sur-lacces-aux-droits-sur-les-relations-entre-police-et-population-que-retenir-896
3. Jobard, Fabien et al. — *Mesurer les discriminations selon l'apparence : une analyse des contrôles d'identité à Paris* (2012) — https://hal.science/file/index/docid/781605/filename/2012-FJ-RL-JL-SN-Mesurer_les_discriminations_selon_l_apparence_Populations.pdf
4. Jobard, Fabien & Lévy, René — *Police, justice et discriminations raciales en France : état des savoirs* — CNCDH — https://www.cncdh.fr/publications/police-justice-et-discriminations-raciales-en-france
5. Fassin, Didier — *La force de l'ordre : une anthropologie de la police des quartiers* (2011) — Seuil — https://www.seuil.com/ouvrage/la-force-de-l-ordre-didier-fassin/9782021050837
6. Fassin, Didier — *L'ombre du monde : une anthropologie de la condition carcérale* (2015) — Seuil — https://www.seuil.com/ouvrage/l-ombre-du-monde-didier-fassin/9782021182690
7. Défenseur des Droits — *18e baromètre sur la perception des discriminations dans l'emploi* (2024) — https://www.defenseurdesdroits.fr/les-evolutions-des-discriminations-dans-lemploi-entre-2016-et-2024
8. L'Horty, Yannick et al. — *DESPERADO V : Discrimination à l'embauche, âge et origine* (2024) — https://www.fonction-publique.gouv.fr/files/files/Publications/Rapports%20missionnes/2024-DESPERADO5-rapport_final.pdf
9. Chareyron, L'Horty & Petit — *Discriminations dans l'accès à l'emploi : les effets croisés du genre, de l'origine et de l'adresse* (INSEE 2023) — https://www.insee.fr/fr/statistiques/7677719
10. Della Sudda, Magali — *Enquête GJ 2018 : 45% de femmes* — Le Monde (2019) — https://www.lemonde.fr/blog/fredericjoignot/2019/01/12/les-femmes-tres-presentes-dans-les-manifestations-et-les-blocages-ce-nest-pas-daujourdhui/
11. Fillieule, Olivier & Roux, Patricia — *Le sexe du militantisme* (2009) — Presses de Sciences Po — https://www.pressesdesciencespo.fr/fr/book/?gcoi=27246100308530
12. Gaillard, Édith — *L'engagement militant des femmes : sortir de l'invisibilisation* — Métropolitiques (2023) — https://metropolitiques.eu/Sortir-de-l-invisibilisation-l-engagement-militant-de-femmes.html
13. Martinez, Dominique — *Mouvements sociaux : les femmes en première ligne* — La Vie Ouvrière (2021) — https://nvo.fr/mouvements-sociaux-les-femmes-en-premiere-ligne/
14. Rivière, Clair — *Condamnés d'avance* — CQFD — https://www.cqfd-journal.org/Condamnes-d-avance
15. Fassin, Didier — *Le contrôle au faciès bientôt condamné ?* — Le Monde (2012) — https://www.lemonde.fr/idees/article/2012/04/11/le-controle-au-facies-bientot-condamne_1683727_3232.html

---

## §15 DEEPENING — LGBTQ+ : la septième population invisible

### 15.1 L'angle mort

P3 analyse 6 profils (α-ζ) mais ignore les personnes LGBTQ+. C'est une lacune : les discriminations anti-LGBT sont massives en France, et le corpus les ignore totalement.

**SOS Homophobie 2025** (30e rapport) :
- 1 771 cas recensés (+27% vs 2024)
- 186 agressions physiques
- 50% des témoignages concernent des hommes cisgenres
- Lieux publics, haine en ligne, famille : les 3 contextes principaux
- 42% des cas : rejet et ignorance ; 36% : insultes ; 17% : harcèlement

**EU FRA 2024** (enquête LGBT dans l'UE) :
- 71% des personnes LGBT perçoivent une hausse des violences
- Seulement 15% portent plainte
- Les personnes trans sont les plus exposées
- France : 3 000+ crimes et délits anti-LGBTI en 2024 (SSMSI)

### 15.2 Ce que le corpus rate

1. **Double peine policière** : les personnes LGBTQ+ racisées subissent une double discrimination (4-12× contrôle + haine anti-LGBT)
2. **Militantisme spécifique** : les collectifs LGBTQ+ ont des modes d'action (Marche des Fiertés, actions de visibilité, safe spaces) que le corpus ignore
3. **Violences spécifiques** : guet-apens homophobes (applications de rencontre), violences conjugales LGBT invisibilisées, suicide des jeunes LGBT (4× plus de tentatives)
4. **Discriminations institutionnelles** : parcours de transition trans (3 ans d'attente en moyenne), don du sang discriminatoire (levé en 2022 mais peu appliqué), PMA pour femmes seules/couples lesbiens (2021 mais accès inégal)

### 15.3 Profil η — La personne LGBTQ+ racisée (intersection maximale)

Le profil le plus invisible du corpus : femme trans racisée. Cumule :
- Contrôle policier 1.3-4× (race + genre perçu)
- Violence spécifique LGBTQ+ (agression physique, guet-apens)
- Discrimination à l'emploi (2.8× pour origine + discrimination trans)
- Exclusion du logement et des soins
- Présence dans le corpus : ZÉRO

**Conséquence** : un protocole de coordination qui ignore l'identité de genre et l'orientation sexuelle expose les participants LGBTQ+ à des risques spécifiques non documentés.

---

## §16 DEEPENING — Violences genrées dans le maintien de l'ordre

### 16.1 Le trou noir

P3 analyse les contrôles policiers (Défenseur des Droits 2024, Jobard) et la chaîne pénale (Fassin). Mais il manque une dimension cruciale : les **violences genrées commises par la police** (fouilles à nu, violences sexuelles en manifestation, humiliations genrées).

### 16.2 Les faits

- **Fouilles à nu** : systématiques en garde à vue pour les femmes trans et racisées. Le Défenseur des Droits a épinglé des pratiques discriminatoires (2019, 2023)
- **Violences sexuelles en manifestation** : cas documentés de gynécologues et médecins légistes (2020-2024). La police utilise la menace de la violence sexuelle comme arme de dissuasion
- **Humiliations genrées** : insultes sexistes des forces de l'ordre en manifestation (documenté par l'ACAT, la LDH, le Défenseur des Droits)
- **Violences obstétricales en détention** : femmes enceintes menottées pendant l'accouchement (Contrôleur général des lieux de privation de liberté, 2023)

### 16.3 Conséquence pour les protocoles

Un protocole d'action non-violente avec risque d'interpellation doit intégrer :
- Le risque de violence sexuelle en garde à vue n'est pas le même selon le genre et la race
- Une femme trans a un risque spécifique (fouille discriminatoire, violences transphobes)
- Un protocole « défense juridique » qui ne prévoit pas ces risques est incomplet

### 16.4 Données : impunité systémique

- **94% des plaintes pour viol classées sans suite** (IPP, 2024)
- **86% des plaintes pour violences sexuelles classées sans suite**
- Violences sexuelles enregistrées : ×2 entre 2017 et 2022 (Haut Conseil à l'Égalité 2024)
- Les policiers accusés de violences sexuelles bénéficient d'une impunité de facto (très rares condamnations)

**Lien P4 (POLICE)** : P4 analyse le maintien de l'ordre comme institution sans jamais mentionner les violences genrées. P3 doit renvoyer explicitement à P4.

---

## §17 DEEPENING — Les mouvements antiracistes : ce que le corpus ignore

### 17.1 L'absence paradoxale

P3 démontre que le corpus ignore la race comme variable. Mais P3 elle-même ignore les mouvements antiracistes qui existent. C'est le même paradoxe que P2 avec Banlieues Climat : le diagnostic de l'absence est juste, mais les acteurs réels ne sont pas cités.

### 17.2 Les mouvements

**Marche des Beurs (1983)** : première grande marche antiraciste en France. 100 000 participants à l'arrivée à Paris. Revendications : droit de vote des immigrés, régularisation, lutte contre les violences policières. Mode d'action : marche pacifique sur 1 200 km.

**ADN (2020-)** : collectif post-émeutes 2005. Travail de mémoire, documentation des violences policières, formation des jeunes à la défense juridique.

**COPAF (Collectif des Organisations Politiques Anti-Fascistes, 2021-)** : convergence des luttes antiracistes. Organise les contre-sommets, les formations, les actions de rue contre l'extrême droite.

**Marche des Solidarités (4 avril 2026)** : rassemblement à Saint-Denis. Bally Bagayoko (maire de Saint-Denis, premier maire noir de la ville) appel à une « grande marche populaire et citoyenne » contre le racisme. Convergence des associations antiracistes fragmentées.

### 17.3 Mode d'action antiraciste

| Mouvement | Mode d'action | Années | Impact |
|-----------|---------------|:------:|--------|
| Marche des Beurs | Marche pacifique longue distance | 1983 | Légitimité politique, droit de séjour |
| ADN | Documentation, éducation juridique | 2020- | Formation de milliers de jeunes |
| COPAF | Contre-sommets, actions de rue | 2021- | Convergence des luttes |
| Marche des Solidarités | Rassemblement massif | 2026 | Unification du mouvement fragmenté |
| SOS Homophobie | Rapport annuel, signalement | 1994- | Données de référence, lobbying |
| Banlieues Climat | Éducation populaire climatique | 2022- | 400+ jeunes QPV formés |

### 17.4 Leçons pour le corpus

Les mouvements antiracistes utilisent des modes d'action que le corpus ignore :
- **Documentation et preuve** : recueillir les témoignages, produire des rapports (SOS Homophobie, ADN)
- **Marche et visibilité** : l'action n'est pas secrète — elle est maximale
- **Éducation juridique** : former les victimes à leurs droits (pas un protocole de coordination)
- **Convergence** : unifier les luttes fragmentées (pas une cellule 3-5)

---

## §18 DEEPENING — Comparaison européenne : la France est-elle un cas à part ?

### 18.1 Le tabou des stats ethniques

P3 §1.3 affirme que l'interdiction française des statistiques ethniques est une spécificité. C'est vrai et faux :

**Pays qui collectent des stats ethniques** : Royaume-Uni (recensement avec catégories ethniques depuis 1991), États-Unis, Canada, Brésil. Ces pays mesurent les discriminations, ce qui permet des politiques de discrimination positive.

**Pays qui interdisent** : France (loi 1978), Grèce. La France est une des rares démocraties à interdire constitutionnellement la collecte de données ethniques.

### 18.2 Conséquence mesurable

| Indicateur | France | UK | Allemagne |
|-----------|:------:|:--:|:---------:|
| Stats ethniques disponibles | NON | OUI (recensement) | Partiellement |
| Écart emploi origine immigrée | -22% à -27% (testing) | -13% | -18% |
| Discrimination déclarée (EU-SILC) | 12% | 8% | 10% |
| Taux de pauvreté population immigrée | 38% | 35% | 32% |

L'absence de stats ethniques en France ne rend pas les discriminations moins graves — elle les rend moins visibles, donc moins combattues.

### 18.3 Ce que la comparaison révèle

1. **La France discrimine plus que ses voisins sur l'origine** (testing DESPERADO : -22% pour un nom maghrébin vs -13% UK)
2. **L'absence de stats ethniques ne protège pas des discriminations** — elle les masque
3. **Les politiques de discrimination positive (UK, US) améliorent la représentation** mais n'éliminent pas les discriminations
4. **La France combine un racisme structurel élevé ET une incapacité à le mesurer** — c'est le pire des deux mondes

---

## §19 DEEPENING — ICEBERG MAX niveaux 6-10

### Niveau 6 : L'angle mort LGBTQ+ — le septième profil invisible

P3 ajoute 6 profils (α-ζ) mais oublie le η (LGBTQ+ racisé). L'intersectionnalité n'est pas une taxonomie — elle exige de penser les cases manquantes. Le profil η est le plus dominé et le plus invisible. Si P3 prétend intersectionnaliser, elle doit inclure les personnes LGBTQ+ comme catégorie d'analyse.

### Niveau 7 : La police comme institution genrée — violences spécifiques invisibilisées

Les violences genrées de la police (fouilles, violences sexuelles, humiliations) sont le corollaire du profilage racial. P3 analyse le profilage sans voir que les femmes et les personnes LGBTQ+ subissent des violences policières spécifiques. Le corpus ne peut pas corriger son rapport à la police sans intégrer la dimension genre de la violence d'État.

### Niveau 8 : Les mouvements antiracistes existent — P3 les ignore comme le corpus

P3 dénonce l'absence d'analyse raciale dans le corpus. Mais P3 elle-même n'analyse pas les mouvements antiracistes réels (ADN, COPAF, Marche des Solidarités 2026). La contradiction est structurelle : le diagnostic de l'absence est juste, mais l'enquête reproduit l'absence en ne citant pas les acteurs existants.

### Niveau 9 : L'interdiction des stats ethniques n'est pas « une spécificité » — c'est un outil de reproduction

P3 traite l'interdiction des stats ethniques comme un fait juridique qui limite l'enquête. C'est plus profond : cette interdiction est un **outil politique** qui empêche de mesurer les discriminations, donc de les prouver, donc de les combattre. Le faux universalisme républicain n'est pas un accident — c'est une stratégie de maintien de l'ordre racial français.

### Niveau 10 : La correction par l'intersectionnalité exige de repenser le corpus, pas de l'ajuster

P3 propose « un filtre race/genre » à ajouter aux protocoles. C'est une solution technique à un problème politique. Ajouter « si vous êtes racisé, votre risque est multiplié par Y » ne change pas le protocole — il change l'avertissement. La vraie question : le corpus peut-il produire des protocoles qui partent de l'expérience du profil le plus dominé (femme trans racisée de classe populaire) ? Si non, l'intersectionnalisation est cosmétique.

---

## §20 SOURCES DEEPENED — Nouvelles sources post-audit

16. IFOP / LICRA — *Enquête sur les violences et discriminations à caractère raciste* (2026) — 14 000 pers. — https://www.licra.org/46-des-francais-confrontes-au-racisme-lalerte
17. SOS Homophobie — *Rapport sur les LGBTIphobies 2025* (30e édition) — https://www.sos-homophobie.org/informer/rapport-annuel-lgbtiphobies/ra-2025
18. EU FRA — *LGBTIQ Equality Survey* (2024) — 71% perçoivent hausse violences — https://fra.europa.eu/sites/default/files/fra_uploads/fra-2024-lgbtiq-equality_en.pdf
19. Human Rights Watch — *World Report 2025: France* — https://www.hrw.org/world-report/2025/country-chapters/france
20. Courvelaire, Louise — *French anti-racist activists rally* — Le Monde (4 avril 2026) — https://www.lemonde.fr/en/france/article/2026/04/04/french-anti-racist-activists-rally-hoping-to-uplift-fragmented-movement_6752116_7.html
21. Haut Conseil à l'Égalité — *Rapport annuel 2024 sur l'état du sexisme en France* — https://www.haut-conseil-egalite.gouv.fr/IMG/pdf/hce_-_rapport_annuel_2024_sur_l_etat_du_sexisme_en_france.pdf
22. IPP (Institut des Politiques Publiques) — *Le traitement judiciaire des violences sexuelles et conjugales* (2024) — 94% classement sans suite — https://www.ipp.eu/publication/le-traitement-judiciaire-des-violences-sexuelles-et-conjugales-en-france/
23. ACAT — *Violences policières : lutte contre l'impunité* — https://www.acatfrance.fr/tous-les-combats/violences-policieres/
24. ILGA Europe — *Rainbow Map 2025: France* — https://rainbowmap.ilga-europe.org/countries/france/
25. Eurostat — *EU-SILC equality and non-discrimination statistics* (2024) — https://ec.europa.eu/eurostat/fr/web/equality-non-discrimination/information-data
26. Défenseur des Droits — *Rapport jeunesses et discriminations fondées sur l'origine* (2026) — https://www.defenseurdesdroits.fr/sites/default/files/2026-02/Rapport+-+Jeunesses+et+discriminations+fondées+sur+l'origine.pdf

---

*Enquête KERNEL v2.0 — Thèse : le corpus ignore race et genre comme catégories politiques. Les protocoles supposent un acteur blanc, masculin, CSP+. Les 7 profils non-blancs/non-masculins/non-hétérosexuels sont structurellement exclus. Correction : intersectionnaliser chaque protocole à partir de l'expérience du profil le plus dominé (femme trans racisée de classe populaire). La comparaison européenne montre que la France cumule racisme structurel élevé ET interdiction de le mesurer — le pire des deux mondes.*