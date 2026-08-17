# APPLICATION DE LA DOCTRINE AUX FAISCEAUX : ARTEFACTS PROBATOIRES DE L'ICEBERG MAX v2

## RUN_MANIFEST

```
ENGINE_VERSION : 2.8
STATE          : FINAL
RUN_ID         : 20260810-1650-iceberg-v2-doctrine
PARENT_RUN_ID  : 20260810-1644-iceberg-max-v2 (HYPER_MATRICE ICEBERG MAX v2)
AS_OF          : 2026-08-10
INPUT_KIND     : CORRECTIVE (demande utilisateur : la doctrine du dossier preparation-anticorruption n'a pas été appliquée aux faisceaux)
MISSION_MODE   : INVESTIGATION
SUBJECT_SLUG   : iceberg-v2-doctrine
SCOPE          : appliquer aux 9 faisceaux de l'ICEBERG MAX v2 les artefacts probatoires de la doctrine (corruption_brainstorm.md, corruption_brainstorm_2.md, corruption_definition.md) : grille d'évaluation des sources, matrice versions/traces, registre des rumeurs séparé, test des 8 critères de systémicité (§12), conclusion graduée exacte ; aucun fait nouveau
COMPLEXITY     : CX_SCORE=14 → $CX=COMPLEX
CHECKPOINT_SEQ : 0
LAST_COMPLETED : 5
LOADED_MODULES : corruption_brainstorm.md | corruption_brainstorm_2.md | corruption_definition.md | KERNEL v2.8
```

## 1. RECONNAISSANCE DE L'ÉCART (ce que l'ICEBERG MAX v2 avait et n'avait pas)

| Exigence doctrine | Présent dans ICEBERG v2 | Artefact manquant |
|-------------------|-------------------------|-------------------|
| Conclusion graduée (corruption_brainstorm §12) | Partiel : verdict « opacité organisée » | La formulation exacte prescrite manque (§6 ici) |
| Hypothèses concurrentes H0-H6 (corruption_brainstorm §2) | Absent au niveau méta | Testé par critère (§5) |
| Grille d'évaluation des sources 12 dimensions (b2 §3) | Absente | §2 ici |
| Matrice versions/traces (b2 §8) | Absente | §3 ici |
| Registre des rumeurs séparé (b2 §7) | Confondu avec les lièvres/anguilles/loups | §4 ici |
| Critère du lien de contrepartie (corruption_definition §6) | Implicite | Explicité §5 |
| Discipline RAW→FAITS→RELATIONS→HYPOTHÈSES→QUALIFICATIONS | Respectée dans les dossiers parents | Relue §6 |

L'ICEBERG MAX v2 restait une **synthèse d'agrégation** : il reliait des faits déjà vérifiés mais n'appliquait pas les instruments qui transforment une synthèse en dossier probatoire.

## 2. GRILLE D'ÉVALUATION DES SOURCES DÉTERMINANTES (12 dimensions, b2 §3)

Échelle par dimension : FORTE / MOYENNE / FAIBLE / N/A (source non mobilisable pour la dimension).

| Dimension | Rapport CdC Dutreil (18/11/2025, lu intégralement) | Sénat 760 (17/06/2026, pages 12-15 lues) | AN 3056 T1+T2 (08/07/2026, lus intégralement) | Réponse Bercy (PDF « Destinataire n'ayant pas répondu », lu) | Blast + Oxfam (lus intégralement) | CRE contradictoire (rapport CdC ENR 18/03/2026) |
|-----------|--------|---------|---------|---------|---------|---------|
| Accès (pouvait-elle savoir ?) | FORTE (a exploité la BNDP en intégralité) | FORTE (auditionne Bercy) | FORTE (auditions, pouvoirs) | FORTE (est la partie concernée) | MOYENNE (enquêtes, pas accès direct) | FORTE (autorité de régulation) |
| Directivité (observé vs rapporté) | FORTE (documents primaires) | FORTE (auditions directes) | FORTE (auditions directes) | FORTE (elle-même) | MOYENNE (documents + témoins) | FORTE (données propres) |
| Proximité temporelle | FORTE (2025, sur 2005-2024) | FORTE (2026) | FORTE (2026) | FORTE (2025) | MOYENNE (2024-2026) | FORTE (2026) |
| Précision (dates/montants vérifiables) | FORTE (110, 65 %, 30 M€, pages citées) | FORTE (0,5 ETP, « dizaines de M€ ») | FORTE (verbatims, l. citées) | FAIBLE (0 contenu, silence) | MOYENNE (460 Md€, 160 Md€ dérivé) | FORTE (7,3 vs 7,44 Md€) |
| Falsifiabilité | FORTE (pages, tableaux) | FORTE (verbatims) | FORTE (l. 7471, 11285...) | FORTE (l'absence est falsifiable) | MOYENNE (dérivations étiquetées) | FORTE |
| Authenticité | FORTE (PDF officiel, hash) | FORTE (senat.fr) | FORTE (assemblee-nationale.fr) | FORTE (ccomptes.fr, HTTP 200) | MOYENNE (PDF scanné OCR) | FORTE |
| Indépendance | FORTE (cour constitutionnelle des finances) | FORTE (haute assemblée) | FORTE (AN) | FAIBLE (juge et partie) | MOYENNE (indépendante mais militante) | FORTE (régulateur) |
| Intérêt (que gagne/risque la source ?) | FAIBLE biais (contrôle) | FAIBLE biais | FAIBLE biais | INTÉRÊT DIRECT (défend sa politique) | INTÉRÊT (plaidoyer) | INTÉRÊT (défend son bilan) |
| Cohérence interne | FORTE | FORTE | FORTE | N/A (vide) | FORTE (notes méthodologiques) | FORTE |
| Cohérence externe | FORTE (recoupe Sénat 760) | FORTE (recoupe CdC) | TENSION (ne nomme pas la BNDP que CdC/Sénat nomment) | N/A | FORTE (recoupe CdC sur 110/65 %) | FORTE (recoupe CdC) |
| Stabilité | FORTE (document figé) | FORTE | FORTE | N/A | FORTE | FORTE |
| Complétude | FORTE pour son objet (limites notées en GAP) | FORTE | PARTIELLE (réponses écrites non publiées, annexe anonymisée) | N/A (absence totale) | PARTIELLE (verrou secret fiscal) | PARTIELLE (échantillonnage collecte) |

**Lecture** : les 3 rapports officiels (CdC, Sénat, AN) sont des sources FORTES et cohérentes entre elles sur le cœur des faits (110 donataires, 65 %, module non financé, 0,5 ETP). La seule TENSION externe documentée : la commission AN ne nomme jamais la BNDP que la CdC (Annexe 4) et le Sénat 760 (p. 14) nomment (dossier 07-51 : H1 méconnaissance vs H2 ellipse, non tranchable). Bercy est la seule source FAIBLE : son silence est lui-même l'objet d'enquête (dossier 08-04).

## 3. MATRICE VERSIONS / TRACES POUR 3 FAITS CENTRAUX (b2 §8)

### Fait central 1 : LE SILENCE DE BERCEY (3 rapports officiels, 0 réponse publiée)

| Élément | Contenu |
|---------|---------|
| Version institutionnelle | Aucune (le ministre de l'économie n'a pas répondu au rapport CdC Dutreil : « Destinataire n'ayant pas répondu », PDF officiel 08-04) |
| Actes officiels | Aucun acte public de réponse aux rapports Sénat 760 (rec. n° 6), AN 3056 (19 rec.), CdC Dutreil (8 rec.) |
| Traces financières | Le module statistique e-enregistrement n'a jamais été financé (0,5 ETP DESF, « quelques dizaines de M€ » CPO, PAP 156 sans ligne) : 07-26, 07-33 |
| Documents internes | Note DGFiP du 31/01 (13 335/40 000 IFI à RFR nul) « connue par une fuite » (Montchalin nie 13/01, Lescure confirme 15/01) : 27j |
| Témoignages | de Courson (16/06) : « profond regret de ne pas avoir obtenu toutes les informations », courrier recommandé 11/06 : 27j |
| Médias | Aucune reprise d'une réponse gouvernementale ; réponse au 3056 attendue ~08/09 (protocole 07-39) |
| Résultats matériels | QE 11677 (Lachaud) : réponse ministérielle JO 10/03/2026 avec « enrichissement en cours » de la BNDP mais 0 chiffrage : 08-46 |
| Contradictions | Bercy dit « en cours » (03/2026, QE) alors que le Sénat (06/2026) constate le module non financé : tension documentée 08-50 |
| Verdict provisoire | Le silence est un fait documenté, borné (« aucune réponse publiée », pas « aucun travail »). Il ne démontre NI mauvaise foi NI refus délibéré : il documente une absence de compte rendu public sur 5,5 Md€/an de dépense fiscale |

### Fait central 2 : LA CONNAISSANCE PATRIMONIALE CONFINÉE (BNDP)

| Élément | Contenu |
|---------|---------|
| Version institutionnelle | Bercy (QE 11677) : BNDP = « outil de gestion insuffisamment renseigné » pour usages statistiques ; enrichissement en cours |
| Actes officiels | Arrêté 11/04/2005 (création BNDP) ; LOI 2022-1726 (L. 141-5 CJF) ; décret 2023-520 (R. 141-4 : accès direct + conventions d'accès continu) |
| Traces financières | Aucune ligne budgétaire publique (coût BNDP non documenté, 07-46) ; module « quelques dizaines de M€ » jamais voté |
| Documents internes | Convention CdC/DGFiP : jamais trouvée (G-05, 09-11) ; Annexe 4 CdC : « données communiquées par la DGFiP à la Cour » + habilitation des rapporteurs |
| Réseaux sociaux | N/A motivé : aucune trace sociale pertinente identifiée sur ce fait (le corpus n'a pas collecté de signaux sociaux sur la BNDP) |
| Témoignages | Lenglart (Insee, 07/04/2026) : demande une base « à construire » alors que la BNDP existe depuis 2005 : 08-42 |
| Médias | Comparatif européen : DE publie annuellement (113,2 Md€ 2024), la France non depuis 2010 : 09-05 |
| Contradictions | L'Insee demande une base à créer le jour où la DGFiP est auditionnée ; la commission AN ne nomme jamais la BNDP que 2 autres institutions nomment : 07-51 |
| Verdict provisoire | Le confinement de la connaissance est documenté par 4 gestes (droit, habilitation, partenariat IPP, CASD) et 3 absences (convention, financement, réponse). L'explication « technique » (BNDP insuffisante) est partiellement vraie (volet DMTG) mais ne rend pas compte du refus de financer la production statistique |

### Fait central 3 : L'INVISIBILITÉ DES AVENANTS (pilote SESN, 103,6 M€)

| Élément | Contenu |
|---------|---------|
| Version institutionnelle | SESN publie des DECP et des avis (120 résultats sur sa page) ; la CdC (10/04/2026) documente 148 avenants pour 76 marchés |
| Actes officiels | Rapport CdC p. 50-57 : 11 M€ déjà accordés aux MOE, 83 M€ en cours, 92-97 M€ MOE unique (R.214-120) |
| Traces financières | 45 marchés recensés = 103 578 507,98 € ; 0 DECP de modification publiée (0/45), 0 avis BOAMP de modification (0/225) : pilote, phase 1-3 |
| Documents internes | DCE et justifications de durée (accord-cadre TOARC 12 ans) : non publics, demandes CADA rédigées non envoyées |
| Témoignages | Aucun (phase 9 droit de réponse non engagée : DELIVERABLE_PENDING) |
| Médias | Aucune enquête indépendante sur les avenants SESN identifiée (généalogie : pas de RÉPÈTE) |
| Contradictions | Le modèle événementiel montre que les modifications de prix sont exonérées de publication DECP (arrêté 22/12/2022 III) : l'absence de DECP ne prouve pas l'absence de modification, elle documente l'invisibilité structurelle |
| Verdict provisoire | Fait systémique DOCUMENTÉ : le contrôle citoyen des modifications contractuelles est impossible par construction. NI preuve de fraude NI preuve d'irrégularité : les 3 cas approfondis (SMDA, Ribécourt, TOARC) ont été requalifiés réguliers |

## 4. REGISTRE DES RUMEURS (SÉPARÉ DES FAITS, b2 §7)

Une rumeur ne passe jamais silencieusement au registre des faits : promotion exigée = trace dure + triangulation indépendante. Statuts : NON VÉRIFIÉE / PARTIELLEMENT CONFIRMÉE / CONTREDITE / FAUSSE / INDÉCIDABLE.

| # | Rumeur originale | Première occurrence | Origine déclarée | Éléments vérifiables | Propagation | Intérêts possibles | Vérifications effectuées | Statut |
|---|------------------|---------------------|------------------|----------------------|-------------|--------------------|--------------------------|--------|
| R1 | « Le manque de données successorales est un prétexte, la base existe » | Corpus BNDP, 10/08 | Inférence de l'enquête (2 régimes de parole) | BNDP existe depuis 2005 ; Insee demande une base à créer ; DE publie | Interne corpus | Discréditer l'argument technique de Bercy | H1 (méconnaissance) vs H2 (ellipse) non tranchables : 07-51 | INDÉCIDABLE (partiellement soutenue : la production statistique est effectivement morte) |
| R2 | « La note DGFiP sur les IFI a été cachée puis fuite » | 27j, 10/08 | Dossier 06-59 (auditions 3056) | Note du 31/01 (13 335/40 000 IFI à RFR nul) ; Montchalin nie 13/01, Lescure confirme 15/01 | Presse + commission | Éviter la divulgation de données IFI | Deux ministres, positions contradictoires documentées ; l'origine de la fuite inconnue | PARTIELLEMENT CONFIRMÉE (la note existe et a transité ; l'intention de la cacher non démontrée) |
| R3 | « Les 110 donataires du Dutreil sont des familles connues » | Corpus Dutreil, 09-10/08 | Presse (Blast) + Oxfam | 110 personnes, 65 %, 30 M€ (CdC) ; Arnault 44,4→6,5 % (dérivé Oxfam) | Blast, Oxfam, corpus | Dénoncer le centile | Annexes anonymisées ; secret fiscal maintenu ; les 110 restent innommables | INDÉCIDABLE (les montants sont établis, l'identité est légalement verrouillée) |
| R4 | « Le bradage des actifs publics » (Macron et prédécesseurs) | 15-15, 09/08 | Rumeur politique | Toulouse +199 M€ ; autoroutes 6,5-7,8 Md€ ; FDJ +15 % IPO | Médias, réseaux | Accusation politique | Écarts documentés cas par cas, MAIS généralisation « bradage » non soutenue (les écarts s'expliquent partiellement par conception, risque, calendrier) | CONTREDITE (en tant que généralisation ; note : les écarts cas par cas restent documentés, cf. FB-01) |
| R5 | « La concentration archéologique SESN (42,29 %) cache un favoritisme » | Pilote SESN, axe 4, 10/08 | Hypothèse initiale du pilote | INRAP 23,74 % + EVEHA 18,55 % = 42,29 % | Interne pilote | Signal d'anomalie | Code du patrimoine L. 523-1/523-8/523-9/523-10 : diagnostics INRAP réservés, fouilles agréées, contrôle SRA ; H0/H2 favorisées | CONTREDITE (structure réglementée) |
| R6 | « Les banques-conseils de l'État sont rémunérées au-dessus du marché » | Corpus banques-conseils, 09/08 | Hypothèse d'enquête | Mandats identifiés en nature (Lazard/FDJ côté État, SocGen/Toulouse) ; montants non publics | Interne corpus | Mesurer la rente | Montants jamais publiés (jaunes budgétaires sans ventilation) : GAP | NON VÉRIFIÉE (impossible à tester sans documents CADA) |
| R7 | « La CRE laisse sur-rémunérer les ENR sans contrôle » | Run 2 ENR, 10/08 | Hypothèse P3 | Sur-rémunérations + sanctions « quasi-inexistantes » (CdC 18/03/2026) ; mais la CRE affirme marché concurrentiel | Interne corpus | Quantifier les effets d'aubaine | NI concentration anormale démontrée NI fraude liée à un décideur public : P3 partielle | PARTIELLEMENT CONFIRMÉE (trou de contrôle documenté, pas de manœuvre) |

**Règle appliquée** : aucune des rumeurs R1-R7 n'a été promue au rang de fait dans l'ICEBERG MAX v2 sans sa vérification associée. Les faits du corpus et les rumeurs de ce registre restent séparés.

## 5. TEST DES 8 CRITÈRES DE SYSTÉMICITÉ (corruption_brainstorm §12)

Objectif : vérifier ce qui transforme (ou non) des cas individuels en démonstration systémique. Verdict par critère : ÉTABLI / PARTIEL / NON ÉTABLI.

| # | Critère | Verdict | Preuves du corpus | Limite |
|---|---------|---------|-------------------|--------|
| 1 | Population complète ou échantillon justifié | PARTIEL | Pilote SESN : univers complet 45 marchés (2021-2026, 103,6 M€) ; corpus Dutreil : 110 donataires exhaustifs (CdC) | Le corpus national (toutes institutions) n'est pas exhaustif : échantillons raisonnés |
| 2 | Mécanisme récurrent, pas seulement des scandales | ÉTABLI | Pattern en 5 temps (15-15) : actif → sortie contestée → écart → contrôle tardif → sanction sélective ; FB-08/FB-09 : confinement de la connaissance + silence répété | Mécanisme documenté dans les modalités, pas dans un plan unique |
| 3 | Bénéficiaires ou réseaux qui persistent dans le temps | PARTIEL | 4/6 directeurs APE partis en finance privée (Azéma, Turrini, Bézard, Vial) ; banques-conseils récurrentes (Lazard, Goldman, SocGen) | Lien causal cession/mobilité non établi ; pas de graphe de réseau complet (Phase 6 non faite) |
| 4 | Asymétrie mesurable dans l'accès aux décisions/ressources | ÉTABLI | BNDP : 3 ayants droit + exceptions (CdC, IPP) vs zéro public ; 0,5 ETP vs 9 000 Md€ de transmission ; 1/3 des IFI à RFR nul | Asymétrie mesurée sur la connaissance, pas sur l'accès aux décisions individuelles |
| 5 | Répétition des mêmes dérogations | PARTIEL | Avenants invisibles (0/45 DECP, 0/225 BOAMP) ; procédures négociées répétées ; guichets ouverts ENR | Seuil juridique par fondement : la répétition n'est pas l'irrégularité |
| 6 | Inefficacité ou neutralisation régulière des contrôles | ÉTABLI | Sanctions quasi-inexistantes ENR (CdC) ; contrôle 6-10 ans après les flux ; 0 réponse de Bercy sur 3 rapports ; de Courson sans toutes les informations | Neutralisation documentée par l'absence de suite, pas par une obstruction démontrée |
| 7 | Reproduction du système (nominations, mobilités, dépendances) | PARTIEL | Pantouflage APE documenté (FB-04) ; mêmes intermédiaires dans plusieurs dossiers (banques-conseils) | Reproduction dans les profils, pas de mécanisme institutionnel démontré de bout en bout |
| 8 | Cas négatifs (que se passe-t-il sans le réseau ?) | ÉTABLI | JO 2024/SOLIDEO maîtrisé (6,6 Md€ sans dérapage) ; SMDA, Ribécourt, TOARC requalifiés réguliers ; concentration archéo expliquée ; CRE contredit la concentration ENR | Les cas négatifs prouvent que la méthode distingue le régulier de l'anormal : pas qu'un réseau existe |

**Résultat du test** : 4 critères ÉTABLIS (2, 4, 6, 8), 4 PARTIELS (1, 3, 5, 7), 0 NON ÉTABLI. Aucun des 8 critères de la doctrine n'est invalidé, mais la moitié ne sont que partiels. La démonstration systémique est **SERIEUSE mais INCOMPLÈTE** : elle suffit à documenter un système d'opacité et de sélectivité (au sens analytique de corruption_definition.md), pas à démontrer une corruption pénale individuelle ni une « capture complète ».

## 6. CONCLUSION GRADUÉE EXACTE (formulation prescrite par corruption_brainstorm §12)

**Ce qui est établi (faits vérifiés, sources primaires)** :
1. Des transferts massifs organisés par le droit (Dutreil 5,5 Md€/an dont 110 personnes = 65 % ; niches 91,83 Md€ ; taxe holdings démantelée).
2. Une connaissance patrimoniale confinée (BNDP exploitée par la CdC, inaccessible au public, production statistique morte depuis 2010).
3. Un pattern de silence administratif documenté (3 rapports officiels, 0 réponse publiée de Bercy).
4. Une invisibilité structurelle des modifications contractuelles (148 avenants, 0 publication DECP/BOAMP).
5. Une sélectivité répressive (CJIP sans personnes physiques ; sanctions quasi-inexistantes ENR).
6. Une porte tournante documentée (4/6 directeurs APE partis en finance privée), sans lien causal démontré.

**Ce qui n'est PAS établi** : aucun pacte corruptif individuel ; aucune entente démontrée ; aucune intention ; aucun plan coordonné. Le critère du lien de contrepartie (corruption_definition §6) n'est satisfait dans AUCUN dossier : ce qui relie les faits entre eux est un pattern d'architecture, pas une preuve de connexion humaine.

**Conclusion graduée (formule exacte de la doctrine)** :

> « Les données établissent une capture durable du processus et un risque élevé d'atteintes à la probité. Elles ne permettent pas, en l'état, de démontrer un pacte corruptif individuel. »

**Reformulation du verdict ICEBERG v2** : « opacité organisée » est une étiquette analytique défendable au sens FAIBLE (multicanaux, récurrents, sous-régulés, documentés par les institutions elles-mêmes) et contestable au sens FORT (corruption organisée d'en haut). Le corpus soutient le sens faible ; il ne soutient PAS le sens fort. La formulation « risque élevé d'atteintes à la probité » est la limite exacte de ce que les 9 faisceaux permettent d'écrire.

**Suite nécessaire pour faire progresser le test** (les 4 critères partiels) :
- C1 population : étendre le recensement SESN aux 76 marchés (CADA).
- C3 réseaux : Phase 6 cartographie des acteurs (graphe minimal) sur les cas documentés.
- C5 dérogations : vérification du fondement juridique événement par événement (modèle R.2194).
- C7 reproduction : croiser banques-conseils et trajectoires APE (loup W5).

**Statut final** : ce document est un instrument de travail interne. Toute publication reste conditionnée au droit de réponse (Phase 9, jamais engagée), aux matrices juridiques par qualification (Phase 10 du pilote), et à la prudence d'expression (bonne foi : intérêt général + base factuelle + sérieux + prudence + absence d'animosité).
