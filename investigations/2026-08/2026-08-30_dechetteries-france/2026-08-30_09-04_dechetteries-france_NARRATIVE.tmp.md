# Investigation — Déchèteries en France : réseau, réglementation et financement

## RÉSUMÉ EXÉCUTIF

Cette investigation porte sur l'état et la gouvernance du réseau français des déchèteries, traitée comme un objet d'investigation (INPUT_KIND=TOPIC, MISSION_MODE=INVESTIGATION). Le lead fourni étant un thème sans source matérielle, LEAD_QUESTION=N/A(NO_INPUT_LEAD) et l'audit de source est N/A ; l'OBJECT_QUESTION est traité prioritairement.

Faits établis (tous **✧ PROBABLE**, famille de provenance unique — principalement officielle) :

1. **Rôle des déchèteries dans le circuit de collecte** (FCT-001) : en 2021, environ 40 % du tonnage des déchets ménagers et assimilés (DMA) collectés par le service public est issu des dépôts en déchèterie (≈242 kg/hab sur 615 kg/hab). Sources : Insee Première n°2055 (juin 2025, SRC-001) et notre-environnement.gouv.fr (MTECT, SRC-002), ADEME (SRC-006). Corroboration AO official single family → ✧.
2. **Financement** (FCT-002) : en 2023, 22,0 Md€ consacrés à la gestion des déchets en France, dont 63 % (13,9 Md€) pour le service public (SPGD), financé surtout par la TEOM (8,9 Md€) et la REOM (0,9 Md€). Source : SDES (SRC-004). Trajectoire cohérente avec 21,6 Md€ en 2022 (presse reprenant SDES) → ✧.
3. **Cadre réglementaire** (FCT-003) : les déchèteries sont des installations classées (ICPE) de la rubrique 2710, dont le régime a été refondu par le décret n°2012-384 du 20/03/2012 (classification par volumes, régime d'enregistrement), avec prescriptions générales fixées par les arrêtés du 27/03/2012 (registre des déchets sortants, réception des déchets dangereux, contrôle périodique). Source : Enviroveille / CCI France (SRC-003). Texte officiel (Légifrance) inaccessible au bot (403 head-blocked) → source unique non-officielle → ✧.
4. **Accès des professionnels** (FCT-005) : la réglementation permet l'accès des artisans, commerçants et PME aux déchèteries, mais la décision d'accepter et les conditions (notamment tarifaires) relèvent du gestionnaire. Source : Enviroveille / CCI France (SRC-003) → ✧.
5. **Dépôts sauvages** (FCT-004) : le coût national de résorption des dépôts sauvages est estimé entre 30 et 90 M€ par an (Cerema, 2024). Source : ARBE Région Sud (SRC-005) → ✧.

**Gap principal** (CLM-005, AXS-001/007) : le **nombre exact de déchèteries ouvertes en France** n'a pas pu être ancré à une source inspectée dans cette passe. Les rapports ADEME (« La collecte des déchets par le service public ») sont illisibles au bot (aucun texte extractible), et l'annuaire SINOE (data.ademe.fr) agrège des enregistrements historiques cumulés sans total courant d'ouverture lisible. Ce gap est déclaré GAP_TYPE=INDEPENDENCE/SCOPE, non un refus du fait que le réseau est dense et central.

**Conclusion bornée** : en l'état, l'investigation établit (✧) le rôle structurant des déchèteries dans la collecte des DMA, leur encadrement ICPE, leur financement via le SPGD/TEOM et le coût des dépôts sauvages ; mais elle laisse ouvert, par honnêteté forensique, la question du décompte exact du maillage national. Aucune conclusion ne dépasse la force des preuves ; aucune inférence n'est présentée comme fait.

## CHRONOLOGIE

- **2005–…** : enquêtes bisannuelles « Collecte » coordonnées par l'ADEME auprès des EPCI compétents (domaine déchets) ; données consolidées dans SINOE (SRC-001, SRC-002).
- **20/03/2012** : décret n°2012-384 modifiant la nomenclature des ICPE ; la rubrique 2710 est reclassifiée par volumes présents (dangereux / non dangereux) et gagne un régime d'enregistrement (SRC-003).
- **27/03/2012** : arrêtés de prescriptions générales applicables aux installations de collecte (2710-1 et 2710-2) : clôture, réception des déchets dangereux par personnel habilité, registre des déchets sortants, contrôle périodique (SRC-003).
- **2021** : enquête Collecte 2021 ; les déchèteries concentrent ≈40 % du tonnage DMA collecté (≈242 kg/hab), Δ +65 kg/hab de tri sur 10 ans (SRC-001, SRC-002).
- **2023** : dépense intérieure de gestion des déchets = 22,0 Md€, dont 63 % pour le SPGD (13,9 Md€) ; TEOM 8,9 Md€, REOM 0,9 Md€ (SRC-004). 37 Mt de DMA collectées en métropole (SRC-006).
- **2024** : Cerema actualise l'estimation du coût de résorption des dépôts sauvages : 30–90 M€/an (SRC-005). Tri à la source des biodéchets généralisé au 01/01/2024.
- **19/12/2025** : communiqué ADEME MODECOM® 2024 : les déchèteries « jouent un rôle central » ; ~75 % du Tout-Venant en déchèterie relèverait de filières REP (SRC-006).

## DOMAINES

Présentation par axes d'investigation (INVESTIGATION_MAP en CARTE DES PREUVES).

### D1. Mécanismes de collecte / rôle des déchèteries (AXS-005, SATURATED)
FCT-001 établit qu'en 2021 la moitié environ des déchets triés des ménages passe par les déchèteries et colonnes d'apport volontaire, et que 40 % du tonnage DMA provient des dépôts en déchèterie (≈242 kg/hab). Les flux les plus concentrés : encombrants (88 %), déblais/gravats (99 %), déchets dangereux (69 %), déchets verts et biodéchets (78 %) (SRC-001). La déchèterie est donc non un site annexe mais un maillon central du tri des encombrants et déchets occasionnels.

### D2. Règles et contrôles (AXS-002, SATURATED)
FCT-003 et FCT-005 : cadre ICPE rubrique 2710, classement quantitatif (décret 2012-384), prescriptions des arrêtés du 27/03/2012, registre des déchets sortants, et liberté du gestionnaire sur l'accès des professionnels. Limite : le texte officiel (Légifrance) est en 403 au bot → source juriste/technique de second rang, d'où tier ✧ et non ✦.

### D3. Ressources / financement (AXS-004, SATURATED)
FCT-002 : la gestion des déchets mobilise 22,0 Md€ (2023), 63 % via le SPGD (13,9 Md€), principalement TEOM (8,9 Md€) + REOM (0,9 Md€) ; financement incidents : entreprises 41 %, ménages 35 %, administrations 24 %. La TEOM étant assise sur le foncier, les collectivités financent le réseau indépendamment des volumes déposés — un point à vérifier dans une passe ultérieure.

### D4. Acteurs (AXS-003, SATURATED)
Rôles : ADEME (opérateur national, enquêtes SINOE, centralisation des points d'apport REP), collectivités/EPCI (compétence et gestion des déchèteries), éco-organismes REP (alimentent les données), services de l'État (DREAL/DDT pour le contrôle ICPE). FCT-001 et SRC-006 (ADEME) étayent le rôle central de l'ADEME dans la donnée.

### D5. Impacts et écarts (AXS-006, SATURATED)
FCT-004 : coût national de résorption des dépôts sauvages estimé 30–90 M€/an (Cerema 2024). La restriction d'accès et le coût sont cités par les collectivités comme pistes aggravantes/préventives ; le lien causal n'est pas démontré (voir CHAÎNES).

### D6. Contro-hypothèses / maillage (AXS-007, GAP)
Le nombre exact de déchèteries ouvertes n'est pas établi (AXS-001/007 en GAP). Les données ouvertes (annuaire SINOE) sont cumulatives ; les rapports ADEME sont illisibles au bot. GAP_TYPE=INDEPENDENCE. Ceci borne — pas infirme — l'ampleur du réseau.

## RÉSEAU D'ACTEURS

ACTOR_NETWORK_MAP non peuplée en arêtes sourcées : l'investigation n'a pas établi de relations typées datées entre entités (pas de registre, procès-verbal ou contrat inspecté) au-delà du partage de données ADEME/éco-organismes (SRC-006). Cette absence est un gap explicite, non une présomption. RESOURCE_FLOW_MAP : chaîne de financement SPGD→collectivités (TEOM/REOM) et ADEME comme source de données consolidées (FCT-002, SRC-004).

## CHAÎNES / PELOTE

CAUSAL_ROUTE=OPTIONAL posée, résultat = CAUSALITY GAP (CAU-001). Aucune chaîne causale vérifiée : l'hypothèse « restriction d'accès / coût → dépôts sauvages » est documentée seulement comme piste de prévention par les collectivités (ARBE, FCT-004). COST_HARMS associés (30–90 M€) sont des estimations de résorption, pas une preuve de mécanisme causal. CORRELATION ≠ CAUSATION : le lien reste inexpliqué sans étude causale dédiée. Chaîne courte vérifiée préférée à une chaîne longue fabriquée : on s'arrête ici.

## CARTE DIALECTIQUE

- **P1 dominant/officiel** (ADEME, MTECT, SDES, Cerema) : le réseau des déchèteries fonctionne, progresse (tri +21 % en 10 ans) et s'affine avec la REP ; les déchèteries sont un levier de valorisation (SRC-001, SRC-002, SRC-004, SRC-006).
- **P2 critique/contradictoire** : les associations et collectivités signalent la persistance des dépôts sauvages (coût 30–90 M€/an), des marges de tri (69 % d'erreurs dans la poubelle grise) et un potentiel non capté (75 % du Tout-Venant relèverait de filières REP) (SRC-005, SRC-006).
- **P3 arbitrage par les preuves** : les deux perspectives reposent sur des données officielles compatibles ; la divergence porte sur l'interprétation (progrès vs gisement résiduel), pas sur des chiffres contradictoires. Aucune contradiction matérielle non résolue (CONTRADICTION_LEDGER vide). Poids inégal : les estimations de coût et de potentiel sont des ordres de grandeur, non des comptes.

## CARTE DES PREUVES

Voir ci-dessous les blocs machine émis par le runtime (registre des preuves, registre des faits, carte source→fait, registre des réfutations, plan de write-back, registres sémantiques LED/CLM/AXS/CAU, matrice de traçage, rapport EDI et journal des requêtes).

### LEAD_COVERAGE
LED-001 (rôle des déchèteries) → EXPAND → SATURATED (FCT-001). LED-002 (cadre réglementaire/gouvernance) → EXPAND → SATURATED (FCT-003, FCT-005). LED-003 (financement/impacts) → EXPAND → SATURATED (FCT-002, FCT-004). Aucune EXCLUDE : pas de lead hors périmètre.

### OBJECT_COVERAGE
L'OBJECT_QUESTION (état et gouvernance : réseau, réglementation, financement, écarts) est couvert par les axes RULES_CONTROLS/AXS-002, RESOURCES_FLOWS/AXS-004, MECHANISMS/AXS-005, IMPACT_RESPONSIBILITY/AXS-006. La dimension « nombre de sites » reste en GAP explicite (AXS-001/AXS-007). Pas de lead matériel laissé AUDIT-only.

### Fiabilité — notes
Tous les faits sont **✧ PROBABLE** (famille de provenance unique). Aucun ✦ : pour FCT-001/002/004 la famille est A (officielle) ; pour FCT-003/005 la famille est B (technique/juridique de second rang) car Légifrance est 403-blocked. La réfutation a cherché activement des contre-preuves (REFUTATION * , NONE trouvé) ; elle n'a pas trouvé de contradiction matérielle. TERM honnête : source unique → maximum ✧.

## PÉRIMÈTRE & LIMITES

- **Inclusions** : réseau national des déchèteries acceptant les DMA, cadre ICPE, financement SPGD, dépôts sauvages.
- **Exclusions** : déchèteries purement professionnelles hors flux ménagers ; sites détaillés cas par cas ; récit des filières REP par filière.
- **Limites d'accès** : Légifrance en 403 au bot ; rapports ADEME en librairie sans texte extractible ; donnée SINOE cumulative non exploitable pour un total courant ; pas de licence de données téléchargée dans cette passe.
- **Periode** : focus 2012–2026 avec ancrage statistique 2021 (tonnages) et 2023 (dépenses).
- **EDI** : corpus majoritairement officiel A (Insee, MTECT, SDES, ADEME, ARBE) + une source technique B (CCI France) ; pas de source dissidente, académique ou de terrain — pénalité MISSING_COUNTER et NO_DIRECT_EVIDENCE partielle. Le nombre de sites reste un point aveugle (GAP).

## AUDIT DU LEAD / SOURCE

N/A(NO_INPUT_LEAD) : le sujet « déchèteries en France » est un thème, sans document, claim ou URL fourni. Aucune source soumise à auditer ; les sources citées proviennent de la recherche objet.

## ÉTAT DES CONNAISSANCES

- **PROBABLE (✧)** : rôle des déchèteries dans 40 % du tonnage DMA (2021) ; dépense 22,0 Md€ / 63 % SPGD / TEOM 8,9 Md€ (2023) ; statut ICPE 2710 + décret 2012-384 + arrêtés 27/03/2012 ; accessibilité des professionnels relève du gestionnaire ; coût dépôts sauvages 30–90 M€/an (Cerema 2024).
- **UNKNOWN (GAP_TYPE=INDEPENDENCE)** : nombre exact de déchèteries ouvertes en France.
- **CAUSALITY GAP** : lien éventuel entre accès/coût et dépôts sauvages non démontré.
- Aucun fait REFUTE ; aucune contradiction matérielle non résolue.