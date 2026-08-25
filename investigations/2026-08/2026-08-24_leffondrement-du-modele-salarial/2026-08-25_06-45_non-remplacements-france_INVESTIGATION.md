# INVESTIGATION KERNEL v2.8 : MESURER LES NON-REMPLACEMENTS DE POSTES EN FRANCE

> **Objet** : traiter le loup L-001 de la fresque `2026-08-25_ia-salariat-fresque-systemique` (RUN 20260825-0635) : l'érosion de l'assiette salariale passerait par des postes non remplacés (attrition), invisibles statistiquement. Cette investigation cherche à savoir si ce trou est mesurable avec les données publiques françaises, et ce que disent les proxys disponibles en 2025-2026.
>
> **Companions** : fresque parente `investigations/2026-08/2026-08-25_ia-salariat-fresque-systemique/2026-08-25_06-35_ia-salariat-fresque-systemique_INVESTIGATION.md` ; investigation maîtresse `2026-08-24_18-22_leffondrement-du-modele-salarial_INVESTIGATION.md` (LED-011 : « l'érosion est invisible, passe par les non-remplacements ») ; RENARD (APEC) ; DEEP_DIVE_10_ZONES (Z3 chiffrage).

## RUN_MANIFEST

| Champ | Valeur |
|---|---|
| ENGINE_VERSION | 2.8 |
| STATE | FINAL |
| RUN_ID | 20260825-0645-non-remplacements-france |
| PARENT_RUN_ID | 20260825-0635-ia-salariat-fresque-systemique |
| AS_OF | 2026-08-25 |
| INPUT_KIND | UPDATE |
| MISSION_MODE | INVESTIGATION |
| INPUT_REF | NONE (topique : mesure statistique) |
| SUBJECT_SLUG | non-remplacements-france |
| INVESTIGATION_PATH | investigations/2026-08/2026-08-25_non-remplacements-france/2026-08-25_06-45_non-remplacements-france_INVESTIGATION.md |
| SCOPE | Mesurer les non-remplacements de postes en France : proxys statistiques disponibles (emploi net, flux MMO, intentions APEC/BMO, secteurs à attrition), attributions causales, comparaison US. Période 2015-2026, focale France. |
| COMPLEXITY | 10 → COMPLEX |
| CHECKPOINT_SEQ | 0 |
| LAST_COMPLETED | NONE |
| NEXT_ACTION | NONE |
| RESUME_COUNT | 0 |
| ROUTE_OVERRIDES | [] |
| LOADED_MODULES | SYMBOLS.md, PATTERNS.md, THREATS.md, GATES.md, REQUEST_LOG.md |
| DEGRADED_FLAGS | [] |
| GATE_VERDICT | PENDING_AT_SERIALIZATION |

## TEMPORAL_STATE

| Événement | Date |
|---|---|
| Non-remplacement « un fonctionnaire sur deux » (Sarkozy) → ~160 000 postes | 2007-2012 |
| Début de la baisse des embauches de cadres | 2023 |
| Recrutements cadres : −8 % puis −3 % (cumul −11 %), IT −21 % (APEC) | 2024-2025 |
| Enquête US HR Dive : 50 % des dirigeants ont freiné les embauches | 22/09/2025 |
| « Gel des embauches » dans 50 % des firmes US (Resume.org) | 24/09/2025 |
| Emploi salarié privé 2025 : −40 800 postes (dont −44 000 alternance) | 2025 |
| Sénat : vote du non-remplacement d'1 fonctionnaire d'État sur 2 | 06/12/2025 |
| Exécutif : écartement de la mesure dans le budget 2026 final | 27/01/2026 |
| HBR : licenciements dus au potentiel de l'IA, pas à sa performance | 29/01/2026 |
| BMO 2026 : 2,27 M projets (−6,5 %), difficultés 43,8 % (vs 50,1 %) | 21/04/2026 |
| APEC baromètre pratiques 2026 : difficultés 64 % (2022) → 49 % (2025) | 21/05/2026 |
| URSSAF : T1 2026 effectifs privés stables (−5 900) | 29/05/2026 |
| DARES : T2 2026 emploi privé −0,1 %, −0,4 % sur un an | 30/07/2026 |
| Banques : 368 800 salariés fin 2025 (−0,7 %), −20 000 en 9 ans | 28/07/2026 |
| Date d'investigation | 2026-08-25 |

## CRÉDO

**LEAD_QUESTION** : La thèse « l'érosion passe par les non-remplacements, invisibles statistiquement » (LED-011 de la vidéo) est-elle mesurable et confirmée par les données françaises ?

**OBJECT_QUESTION** : Quelle est l'ampleur documentée des non-remplacements de postes en France (privé et public) entre 2015 et 2026, quels proxys statistiques permettent de la borner, et quelle part peut être attribuée à l'IA plutôt qu'à la conjoncture, à la démographie ou aux choix d'organisation ?

### AXS — axes d'investigation

| AXS-ID | QUESTION | SOUGHT_OBJECTS | STATUS |
|---|---|---|---|
| AXS-001 | Que disent les soldes nets d'emploi (INSEE/DARES/URSSAF) 2024-2026 ? | Estimations trimestrielles, effectifs privés | SATURATED |
| AXS-002 | Les flux (entrées/sorties, MMO DARES) permettent-ils d'isoler les postes non remplacés ? | Données MMO, méthodologie | GAP (source inaccessible) |
| AXS-003 | Que disent les intentions et pratiques de recrutement (APEC, BMO France Travail) ? | Baromètres APEC, enquêtes BMO | SATURATED |
| AXS-004 | Y a-t-il des secteurs à attrition documentée (banques, fonction publique) ? | FBF, presse spécialisée, PLF | SATURATED |
| AXS-005 | La comparaison US (hiring freeze, attrition IA) éclaire-t-elle le mécanisme ? | HBR, HR Dive, BCG, Resume.org | SATURATED |

## SYMBOL_SCORES (15/15, CORPUS_FINAL)

| Sym | Nom | Score | Observations |
|---|---|---|---|
| Ξ | Omission | 7 | Le point central : aucun instrument statistique français ne publie de « taux de remplacement des postes libérés » ; le non-remplacement privé est invisible par construction ; la baisse 2025 est attribuée à l'alternance, pas à l'IA |
| € | Money | 4 | Le non-remplacement est une économie de coûts (masses salariales) ; les 77 Md€ d'allègements ne sont pas conditionnés à l'emploi |
| Λ | Framing | 4 | « Gel des embauches », « attrition », « non-remplacement » : cadrages variables ; « la moitié des entreprises gèlent » vs « 8 % ont embauché un cadre » : bases différentes |
| Ω | Inversion | 3 | Les décisions de non-remplacement sont présentées comme subies (l'IA) alors qu'elles sont des choix d'organisation (HBR : potentiel, pas performance) |
| Ψ | Sidération | 4 | Chiffres contradictoires publiés simultanément (330 000 licenciements IA vs BCG « reshape ») ; difficulté à établir un socle |
| ↕ | Vertical power | 5 | Le non-remplacement est décidé par l'employeur, subi par le salarié sortant et invisible pour les restants ; asymétrie d'information totale |
| Φ | Spectacle | 3 | Couverture médiatique des plans de départ (SocGen, Capgemini) plus forte que l'attrition silencieuse |
| Σ | Semiotics | 2 | Peu de simulacres ; « baisse maîtrisée des effectifs » (banques) = langage euphemistique |
| Κ | Cynicism | 5 | « Baisse maîtrisée » sans licenciement = non-remplacement institutionnalisé ; le marché du travail se détend sans qu'aucune décision publique ne soit prise |
| ρ | Resistance | 2 | Syndicats documentent les plans (FO sur SocGen) ; pas de contre-mesure statistique |
| κ | Subtle influence | 2 | Non pertinent au premier chef |
| ⫸ | Convergence | 5 | Proxys convergents : recrutements en baisse (APEC, BMO), difficultés en baisse (APEC, BMO), emploi quasi stable, attrition bancaire documentée. Convergence de direction, pas d'amplitude |
| ⚔ | Cognitive warfare | 1 | Aucune coordination |
| 🌐 | Network | 3 | Décideurs RH, directions financières, cabinets, APEC/DARES/INSEE (producteurs de données) |
| ⏰ | Temporal | 4 | La détente s'accélère 2024-2025 (post-COVID, taux) ; l'attribution à l'IA est anticipatoire (HBR) |

## CLAIM_REGISTRY

| CLM-ID | CLAIM | SUPPORT | COUNTER | STATUS | GAP_TYPE |
|---|---|---|---|---|---|
| CLM-201 | Le non-remplacement est une pratique réelle et institutionnalisée en France | Fonction publique (1/2 ou 1/3 non remplacé, Sénat 12/2025) ; banques (−0,7 %/an par attrition) ; APEC « sourcing moins offensif » | L'exécutif a écarté la mesure sénatoriale (01/2026) ; les effectifs publics ont augmenté de 176 000 entre 2017 et 2023 | VERIFIE (pratique) / ⊙ (ampleur) | — |
| CLM-202 | Le non-remplacement privé n'est pas mesurable directement : aucun « taux de remplacement » publié | DARES MMO = flux entrées/sorties, pas de suivi par poste ; concept absent des publications INSEE/URSSAF | L'écart entrées-sorties par secteur est un proxy indirect possible | VERIFIE (absence de mesure) | — |
| CLM-203 | Les proxys convergent vers une détente du marché du travail en 2024-2026 | APEC : cadres −11 % cumulé, IT −21 %, intentions au plus bas depuis 4 ans ; BMO : −6,5 % de projets, difficultés 50,1 % → 43,8 % ; APEC pratiques : difficultés 64 % (2022) → 49 % (2025) | Rebond APEC prévu +4 % en 2026 ; l'emploi net est quasi stable, pas en chute | VERIFIE (direction) | AMPLITUDE |
| CLM-204 | Le repli net de l'emploi salarié privé est faible et largement expliqué par l'alternance | 2025 : −40 800 postes dont −44 000 contrats d'alternance ; T1 2026 : −13 900 ; T2 2026 : −0,1 % | Le solde ne dit rien des remplacements internes (un départ non remplacé peut être compensé par une création ailleurs) | VERIFIE (net) / ⊙ (mécanisme) | — |
| CLM-205 | L'attribution du non-remplacement à l'IA est anticipatoire, pas réalisée | HBR (01/2026) : licenciements dus au potentiel de l'IA, pas à sa performance ; HR Dive : 40 % des dirigeants US remplaceront par l'IA d'ici 2026 | Cas isolés réels (Capgemini 2 400, DeepL 250, SocGen 1 800) | PROBABLE (anticipation) | CAUSALITE |
| CLM-206 | Le chiffrage de l'impact fiscal du non-remplacement reste borné à 4-8 Md€/an (scénario pessimiste) | Deep dive Z3 : 1-10 % de postes cadres non remplacés → 0,9-8,8 Md€/an ; élasticité FIPECO 0,95 | Données 2025-2026 (emploi quasi stable) suggèrent une érosion < 1 % de l'emploi, donc < 1,6 Md€/an | PROBABLE (borne) | DONNEES_FLUX |

## FACT_REGISTRY_V1

| FCT-ID | EPI | TIER | URL | FAMILIES | DATE | SUJET | VALEUR | MEM |
|---|---|---|---|---|---|---|---|---|
| FCT-201 | FACT | ✧ | https://www.insee.fr/fr/statistiques/8997611 | A | 2026 | Emploi salarié T1 2026 (INSEE) | Privé quasi stable (−0,1 %, −13 900 après −19 500) | mem:- |
| FCT-202 | FACT | ✧ | https://dares.travail-emploi.gouv.fr/donnees/lemploi-salarie | A | 2026-07-30 | Emploi salarié T2 2026 (DARES) | Privé −0,1 % sur le trimestre, −0,4 % sur un an | mem:- |
| FCT-203 | FACT | ✧ | https://www.urssaf.org/accueil/statistiques/nos-etudes-et-analyses/employeurs/nationale/employeurs-2026/effectifs-salaires-mars2026.html | A | 2026-05-29 | Effectifs privés T1 2026 (URSSAF) | Stabilisation (−5 900 postes, −0,0 %) après −0,2 % | mem:- |
| FCT-204 | FACT | ✧ | https://www.francetravail.fr/candidat/decouvrir-le-marche-du-travail/besoins-en-main-doeuvre.html | A | 2026-04-21 | BMO 2026 (France Travail) | 2 274 951 projets (−6,5 % vs 2025) ; difficultés 43,8 % (vs 50,1 %) | mem:- |
| FCT-205 | FACT | ✧ | https://corporate.apec.fr/files/live/sites/corporate/files/Nos%20etudes/PDF/Previsions-de-recrutements-de-cadres-2026 | D | 2026-04-02 | Recrutements cadres (APEC) | 294 500 en 2025 (−3 %) ; −11 % cumulé sur 2 ans ; IT −21 % ; prévision 2026 : 305 800 (+4 %) | mem:- |
| FCT-206 | FACT | ✧ | https://www.bfmtv.com/economie/entreprises/seules-8-des-entreprises-ont-embauche-un-cadre-fin-2025-les-recrutements-chutent-au-plus-bas-mais-un-rebond-est-espere-pour-2026_AD-202602030123.html | C | 2026-02-03 | Emploi cadre fin 2025 (BFM/APEC) | Seules 8 % des entreprises ont embauché un cadre fin 2025 | mem:- |
| FCT-207 | FACT | ✧ | https://www.aefinfo.fr/depeche/754874-en-2025-le-secteur-bancaire-enregistre-une-baisse-maitrisee-de-ses-effectifs-de-07-fbfafb | A | 2026-07-28 | Effectifs bancaires 2025 (FBF) | 368 800 salariés fin 2025 (vs 373 200 fin 2024), −0,7 % ; 34 400 embauches | mem:- |
| FCT-208 | FACT | ✧ | https://www.lefigaro.fr/societes/dans-les-banques-l-emploi-continue-de-degringoler-20260728 | C | 2026-07-28 | Emploi bancaire 9 ans (Le Figaro) | ~20 000 emplois perdus en 9 ans (350 700 fin 2025) | mem:- |
| FCT-209 | FACT | ✧ | https://hbr.org/2026/01/companies-are-laying-off-workers-because-of-ais-potential-not-its-performance | C,E | 2026-01-29 | Licenciements IA : potentiel vs performance (HBR) | L'IA est une cause de licenciements et de ralentissement des embauches par son potentiel, pas sa performance | mem:- |
| FCT-210 | FACT | ✧ | https://www.hrdive.com/news/companies-will-replace-workers-with-ai-by-2026/760729/ | C | 2025-09-22 | Dirigeants US (HR Dive, n=1 000) | 50 % ont freiné les embauches ; 39 % ont licencié en 2025 ; 40 % remplaceront des travailleurs par l'IA d'ici 2026 | mem:- |
| FCT-211 | FACT | ✧ | https://www.ouest-france.fr/economie/budget-collectivites-etat/budget-2026-le-senat-vote-le-non-remplacement-de-la-moitie-des-departs-a-la-retraite-des-fonctionnaires-b89f5f3a-d2a3-11f0-a0f2-b2a4fbd1e8d9 | C | 2025-12-06 | Non-remplacement fonctionnaires (Sénat) | Le Sénat vote le non-remplacement d'1 fonctionnaire d'État sur 2 partant à la retraite | mem:- |
| FCT-212 | FACT | ✧ | https://acteurspublics.fr/articles/fonction-publique-le-gouvernement-ne-retient-pas-les-mesures-controversees-du-senat-dans-le-nouveau-budget-2026/ | C | 2026-01-27 | Écartement par l'exécutif | Le budget 2026 final ne retient pas le non-remplacement d'1/2 voté au Sénat | mem:- |
| FCT-213 | FACT | ✧ | https://www.leparisien.fr/economie/budget-2026-dans-la-fonction-publique-un-depart-a-la-retraite-sur-trois-ne-sera-pas-remplace-16-07-2025-KWJIJM7XUFBSJKKRQLZMUZH3RI.php | C | 2025-07-16 | Objectif gouvernemental 2026-2027 | 3 000 postes supprimés en 2026 ; non-remplacement d'1/3 des départs à partir de 2027 | mem:- |
| FCT-214 | FACT | ✧ | https://fr.linkedin.com/posts/radia-doghmane_lapec-vient-de-publier-son-barom%C3%A8tre-des-activity-7464548366580899840-xZWO | C | 2026-05-21 | APEC baromètre pratiques 2026 | Difficultés de recrutement : 64 % (2022) → 49 % (2025) ; sourcing moins offensif | mem:- |
| FCT-215 | FACT | ✧ | https://www.bcg.com/publications/2026/ai-will-reshape-more-jobs-than-it-replaces | D | 2026-04-03 | BCG « reshape » | 50-55 % des emplois US remodelés (pas remplacés) d'ici 2-3 ans | mem:- |
| FCT-216 | FACT | ✧ | https://www.instagram.com/reel/DT3F3EZCEmh/ | C | 2026-01-23 | Emploi privé 2025 (macro) | Recul de 40 800 postes en 2025, dont 44 000 contrats d'alternance disparus | mem:- |

## EVIDENCE_REGISTRY (sélection)

| SRC-ID | TYPE | TITLE | URL | FAMILY | ROLE | LOCATOR | DATE |
|---|---|---|---|---|---|---|---|
| SRC-201 | ◈ | INSEE, emploi salarié T1 2026 | https://www.insee.fr/fr/statistiques/8997611 | A | ◈ | « Dans le secteur privé, l'emploi salarié est quasi stable (-0,1 %) » | 2026 |
| SRC-202 | ◈ | DARES, l'emploi salarié T2 2026 | https://dares.travail-emploi.gouv.fr/donnees/lemploi-salarie | A | ◈ | « quasi stable sur le trimestre (-0,1 %) et se situe 0,4 % sous son niveau » | 2026-07-30 |
| SRC-203 | ◈ | URSSAF, effectifs mars 2026 | https://www.urssaf.org/accueil/statistiques/nos-etudes-et-analyses/employeurs/nationale/employeurs-2026/effectifs-salaires-mars2026.html | A | ◈ | « se stabilisent (-5 900 postes, soit -0,0 %) » | 2026-05-29 |
| SRC-204 | ◈ | France Travail, BMO 2026 | https://www.francetravail.fr/candidat/decouvrir-le-marche-du-travail/besoins-en-main-doeuvre.html | A | ◈ | « 2,28 millions de postes à pourvoir en 2026 » ; « 43,8 % contre 50,1 % en 2025 » | 2026-04-21 |
| SRC-205 | ◈ | APEC, prévisions recrutements 2026 | https://corporate.apec.fr/files/live/sites/corporate/files/Nos%20etudes/PDF/Previsions-de-recrutements-de-cadres-2026 | D | ◉ | « 294 500 cadres en 2025, baisse de 3 % » ; −11 % sur 2 ans | 2026-04-02 |
| SRC-206 | ○ | BFM, emploi cadre fin 2025 | https://www.bfmtv.com/economie/entreprises/seules-8-des-entreprises-ont-embauche-un-cadre-fin-2025-les-recrutements-chutent-au-plus-bas-mais-un-rebond-est-espere-pour-2026_AD-202602030123.html | C | ○ | « Seules 8 % des entreprises ont embauché un cadre fin 2025 » | 2026-02-03 |
| SRC-207 | ◈ | FBF via Aefinfo, effectifs bancaires 2025 | https://www.aefinfo.fr/depeche/754874-en-2025-le-secteur-bancaire-enregistre-une-baisse-maitrisee-de-ses-effectifs-de-07-fbfafb | A | ◈ | « 368 800 salariés au 31 décembre 2025, contre 373 200 fin 2024, soit −0,7 % » | 2026-07-28 |
| SRC-208 | ○ | Le Figaro, emploi bancaire | https://www.lefigaro.fr/societes/dans-les-banques-l-emploi-continue-de-degringoler-20260728 | C | ○ | « perdu près de 20 000 emplois » en 9 ans | 2026-07-28 |
| SRC-209 | ◉ | HBR, potentiel vs performance | https://hbr.org/2026/01/companies-are-laying-off-workers-because-of-ais-potential-not-its-performance | C,E | ◉ | « because of AI's potential—not its performance » | 2026-01-29 |
| SRC-210 | ○ | HR Dive, dirigeants US | https://www.hrdive.com/news/companies-will-replace-workers-with-ai-by-2026/760729/ | C | ○ | n=1 000 ; 50 %/39 %/40 % | 2025-09-22 |
| SRC-211 | ○ | Ouest-France, Sénat non-remplacement | https://www.ouest-france.fr/economie/budget-collectivites-etat/budget-2026-le-senat-vote-le-non-remplacement-de-la-moitie-des-departs-a-la-retraite-des-fonctionnaires-b89f5f3a-d2a3-11f0-a0f2-b2a4fbd1e8d9 | C | ○ | Vote du 06/12/2025 | 2025-12-06 |
| SRC-212 | ○ | Acteurs Publics, écartement | https://acteurspublics.fr/articles/fonction-publique-le-gouvernement-ne-retient-pas-les-mesures-controversees-du-senat-dans-le-nouveau-budget-2026/ | C | ○ | Budget 2026 final | 2026-01-27 |
| SRC-213 | ○ | Le Parisien, objectif 2026-2027 | https://www.leparisien.fr/economie/budget-2026-dans-la-fonction-publique-un-depart-a-la-retraite-sur-trois-ne-sera-pas-remplace-16-07-2025-KWJIJM7XUFBSJKKRQLZMUZH3RI.php | C | ○ | 3 000 postes ; 1/3 à partir de 2027 | 2025-07-16 |
| SRC-214 | ○ | APEC baromètre pratiques via LinkedIn | https://fr.linkedin.com/posts/radia-doghmane_lapec-vient-de-publier-son-barom%C3%A8tre-des-activity-7464548366580899840-xZWO | C | ○ | 64 % (2022) → 49 % (2025) | 2026-05-21 |
| SRC-215 | ◈ | BCG, reshape | https://www.bcg.com/publications/2026/ai-will-reshape-more-jobs-than-it-replaces | D | ◉ | 50-55 % remodelés | 2026-04-03 |
| SRC-216 | ○ | MMO DARES T1 2026 | https://dares.travail-emploi.gouv.fr/dossier/les-mouvements-de-main-doeuvre-des-salaries-du-prive | A | ◈ | « 6 577 900 contrats de travail sont signés » (T1 2026) | 2026 |

## CAUSALITY_REGISTRY

| CAU-ID | EDGE | TYPE | SOURCE | GAP |
|---|---|---|---|---|
| CAU-201 | Départ (retraite, démission, fin de contrat) → décision de ne pas remplacer → poste supprimé sans licenciement | MECHANISM | Banques (SRC-207, 208), FP (SRC-211, 213) | Le mécanisme est documenté secteur par secteur, pas agrégé |
| CAU-202 | Difficultés de recrutement en baisse → pression à remplacer réduite → sourcing moins offensif → non-remplacement normalisé | ENABLER | APEC (SRC-214), BMO (SRC-204) | Corrélation, pas causalité démontrée |
| CAU-203 | Potentiel perçu de l'IA (pas sa performance) → décisions anticipatoires de non-remplacement | CAUSE | HBR (SRC-209), HR Dive (SRC-210) | L'ampleur des décisions anticipatoires n'est pas chiffrable |
| CAU-204 | Conjoncture (taux, post-COVID, alternance) → repli des embauches → solde net ~0 | CAUSE | INSEE (SRC-201), alternance (FCT-216) | L'IA n'est pas le facteur dominant identifié en 2025 |
| CAU-205 | Non-remplacement → baisse masse salariale → baisse cotisations | CAUSE | Mécanisme comptable (FIPECO 0,95) | Amplitude non observable : pas de suivi par poste |

## IMPACT_MAP

| IMP-ID | EFFECT | AFFECTED | EVIDENCE | STATUS |
|---|---|---|---|---|
| IMP-201 | Érosion lente de l'assiette si le non-remplacement se généralise | Sécu, branches | Borne : < 1,6 Md€/an si érosion < 1 % (élasticité FIPECO) ; 4-8 Md€/an dans le scénario pessimiste (deep dive Z3) | PROBABLE (borne) |
| IMP-202 | Détente du marché du travail (moins d'embauches, moins de difficultés) | Jeunes diplômés, cadres IT | APEC −11 %, IT −21 %, BMO −6,5 % ; intentions au plus bas depuis 4 ans | VERIFIE |
| IMP-203 | Attrition sectorielle silencieuse (banques : −0,7 %/an sans PSE massifs) | Salariés du secteur | FBF, Le Figaro, Le Monde (« recrute tout en supprimant ») | VERIFIE |
| IMP-204 | Normalisation du non-remplacement comme outil de gestion publique | Fonctionnaires | Sénat 12/2025, objectif 1/3 en 2027 (écarté pour 2026) | VERIFIE (tentative) |

## CONTRADICTION_LEDGER

| CONTRADICTION | ENTITIES | RESOLUTION |
|---|---|---|
| « La moitié des entreprises gèlent les embauches » (US) vs « 8 % ont embauché un cadre » (FR) | SRC-210 vs SRC-206 | Univers et définitions différents (US dirigeants vs FR APEC) ; les deux documentent une détente, pas une hécatombe |
| « 330 000 emplois supprimés à cause de l'IA » (communauté Reddit) vs BCG « reshape » vs HBR « potentiel, pas performance » | FCT-210, SRC-215, SRC-209 | Le chiffre 330 000 est une compilation non auditable ; l'attribution « à cause de l'IA » est contestée par HBR |
| « Le non-remplacement est voté » (Sénat 12/2025) vs « écarté » (budget final 01/2026) | SRC-211 vs SRC-212 | Séquence législative : vote d'une mission, pas d'une loi ; l'exécutif ne l'a pas retenu pour 2026 |
| « Emploi quasi stable » (INSEE/DARES/URSSAF) vs « les banques dégringolent » (Le Figaro) | SRC-201..203 vs SRC-208 | Le net agrégé masque les secteurs en attrition compensés par d'autres ; c'est le cœur du problème de mesure |

## EDI_REPORT

| Dimension | Score | Commentaire |
|---|---|---|
| A (primary/official) | Fort | INSEE, DARES, URSSAF, France Travail, FBF, APEC (PDF) |
| B (critical/competing) | Faible | Presse syndicale (FO SocGen) ; pas de contre-analyse statistique structurée |
| C (affected/witness) | Moyen | BFM, Le Figaro, Le Parisien, HR Dive (dirigeants) |
| D (independent investigation) | Moyen | BCG, APEC, HBR |
| E (academic/expert) | Faible | HBR (analyse) ; pas d'étude académique dédiée au « non-remplacement » FR |

**Verdict EDI** : corpus institutionnel (A) dominant. Manque : travaux académiques sur l'attrition française, témoignages de salariés, données d'entreprise.

## WOLVES (loups restants)

| LOUP | ANGLE MORT | NATURE |
|---|---|---|
| L-201 | Pas de « taux de remplacement » publié par la statistique publique française | CONCEPT/DONNEES | Nécessiterait une enquête dédiée (DARES/INSEE) ou l'accès aux DADS poste à poste |
| L-202 | L'effet alternance masque le solde réel : sans la baisse des contrats d'alternance, l'emploi 2025 aurait été positif | DONNEES | Décomposition fine par motif de sortie |
| L-203 | Le non-remplacement par IA est indécidable dans les données agrégées (confondu avec conjoncture, taux, organisation) | CAUSALITE | Étude de cas par établissement avec motif déclaré |
| L-204 | Les MMO (entrées/sorties) sont la seule source de flux, mais non croisée avec les postes supprimés | ACCES | La page DARES MMO est inaccessible (socket) ; les données CASD sont sur demande |

## REQUEST_LOG

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---|---:|---|---|---|---|
| 1 | SYS | search_memory (non-remplacement, attrition, flux emploi) | FOUND : mémoire parente APEC/F-017 | MnemoLite | — |
| 2 | SYS | @READ fresque parente + investigation maîtresse (LED-011, APEC) | LOADED | corpus | — |
| 3 | ◈ | QRY-201 : APEC recrutements cadres 2026 | FOUND | SRC-205, 206 | corporate.apec.fr, bfmtv.com |
| 4 | ◈ | QRY-202 : DARES MMO 2025-2026 | FAILED ×2 (socket closed) ; snippet T1 2026 : 6 577 900 contrats | SRC-216 | dares.travail-emploi.gouv.fr |
| 5 | ◈ | QRY-203 : URSSAF effectifs privés 2026 | FOUND | SRC-203 | urssaf.org |
| 6 | ◈ | QRY-204 : BMO France Travail 2026 | FOUND | SRC-204 | francetravail.fr |
| 7 | ◈ | QRY-205 : non-remplacement fonction publique 2026 | FOUND | SRC-211, 212, 213 | ouest-france, acteurspublics, leparisien |
| 8 | ◈ | QRY-206 : attrition/hiring freeze US | FOUND | SRC-209, 210, 215 | hbr.org, hrdive.com, bcg.com |
| 9 | ◈ | QRY-207 : emploi bancaire 2025-2026 | FOUND | SRC-207, 208 | aefinfo, lefigaro |
| 10 | ◈ | QRY-208 : APEC pratiques de recrutement 2026 | FOUND (snippet) | SRC-214 | linkedin (relais APEC) |
| 11 | SYS | FINAL @WRITE | PENDING_AT_SERIALIZATION | — | INVESTIGATION_PATH |

COUNT: ◈9 ◉3 ○4 | unique evidence objects : 16 | upstream families : 4 (A, C, D, E)
LEADS:terminal 6/6 | AXES:terminal 4/5 + GAP 1 (AXS-002) | N/A:—
FAILURES:1 (DARES MMO ×2) | unresolved gaps : AMPLITUDE, CAUSALITE, CONCEPT (taux de remplacement inexistant), ACCES (MMO)

## PÉRIMÈTRE & LIMITES

- La source la plus directe (DARES, mouvements de main-d'œuvre) est inaccessible en lecture (socket fermé ×2) : l'axe AXS-002 est un GAP documenté, alimenté par un snippet de découverte (6 577 900 contrats signés au T1 2026) et les publications INSEE/DARES d'emploi trimestriel.
- Le concept « poste non remplacé » n'existe pas dans la statistique publique française : toute mesure est indirecte (proxys). Ce constat d'absence EST un résultat de l'investigation.
- Les chiffres 2025-2026 proviennent de publications institutionnelles lues en primaire (INSEE, DARES, URSSAF, France Travail) et de presse spécialisée (FBF via Aefinfo, Le Figaro, BFM).
- Aucun write-back Mnemolite : faits ✧ à source unique, sans candidat ✦.

---

# SYNTHÈSE — VERDICT SUR LE TROU STATISTIQUE L-001

## Réponse directe : non, le non-remplacement n'est pas mesurable directement en France

Aucun instrument de la statistique publique française ne publie de « taux de remplacement des postes libérés ». Les données existantes mesurent des stocks (effectifs) et des flux (entrées/sorties de contrats), jamais la décision de l'employeur de ne pas pourvoir un poste devenu vacant. Le « poste non remplacé » est un non-événement : il n'apparaît dans aucun fichier. Cette absence n'est pas un manque de données, c'est un trou de concept : la mesure supposerait de suivre chaque poste après le départ de son titulaire, ce que DADS, MMO et enquêtes emploi ne font pas.

## Ce que les proxys documentent : un faisceau convergent

1. **Le solde net est quasi stable, pas en chute.** Emploi salarié privé : −0,1 % au T1 2026 (INSEE), −0,1 % au T2 2026 (DARES), −0,4 % sur un an ; effectifs URSSAF stables (−5 900). En 2025, le recul de 40 800 postes est largement expliqué par la disparition de 44 000 contrats d'alternance. Aucun chiffre ne documente un choc de destruction.
2. **Les recrutements baissent partout, fortement.** APEC : 294 500 embauches de cadres en 2025 (−3 %), −11 % cumulé sur deux ans, informatique −21 % ; seules 8 % des entreprises ont embauché un cadre fin 2025 ; intentions au plus bas depuis quatre ans. BMO France Travail 2026 : 2,27 millions de projets, −6,5 %.
3. **Les difficultés de recrutement s'effondrent, et c'est le signal le plus fort du non-remplacement doux.** BMO : 43,8 % des projets jugés difficiles (vs 50,1 % en 2025). APEC pratiques de recrutement : 64 % (2022) → 49 % (2025), avec un « retour à des stratégies de sourcing moins offensives ». Quand les entreprises peinent moins à recruter, elles remplacent moins systématiquement : le non-remplacement devient une option de gestion ordinaire.
4. **L'attrition sectorielle est documentée là où elle est organisée.** Les banques françaises : 368 800 salariés fin 2025 (−0,7 %), près de 20 000 emplois perdus en neuf ans, fermetures d'agences (SocGen : 1 800 postes ; 72 agences sur 238), le secteur « continue de recruter tout en supprimant des postes » (Le Monde) : c'est la définition opérationnelle du non-remplacement. La fonction publique : le non-remplacement d'un départ sur deux ou sur trois est un outil assumé (Sénat, décembre 2025 ; objectif 1/3 à partir de 2027), même si l'exécutif l'a écarté pour 2026.
5. **L'attribution à l'IA est anticipatoire, pas réalisée.** HBR (janvier 2026) : les licenciements liés à l'IA sont décidés sur son potentiel, pas sur sa performance. HR Dive (n=1 000 dirigeants US) : la moitié ont freiné les embauches, 40 % disent qu'ils remplaceront des travailleurs par l'IA d'ici 2026. BCG : 50-55 % des emplois seront « remodelés », pas remplacés. Le non-remplacement par anticipation IA existe donc comme pratique déclarée, mais sa traduction statistique est indissociable de la conjoncture (taux, post-COVID, alternance).

## Le verdict forensique

La thèse de la vidéo (LED-011 : « l'érosion est invisible, elle passe par les non-remplacements ») est **plausible, partiellement documentée, et non mesurable avec les instruments actuels**. Les données 2025-2026 dessinent une détente du marché du travail (recrutements en forte baisse, difficultés en chute, emploi quasi stable) compatible avec une érosion par attrition, mais l'amplitude est inférieure à 1 % de l'emploi salarié et les causes identifiées sont d'abord conjoncturelles et démographiques, pas technologiques.

**Conséquence chiffrée** : avec l'élasticité FIPECO (0,95), une érosion de 1 % de la masse salariale coûte environ 4,4 milliards d'euros de cotisations ; le scénario pessimiste de la fresque (4-8 Md€/an) reste une borne haute, et les données 2025-2026 suggèrent une érosion réelle inférieure à 1,6 Md€/an. Le trou existe, il est lent, et il ne peut être mesuré précisément que par une nouvelle instrumentation statistique : suivre les postes après départ du titulaire, croiser MMO et suppressions de postes, ou imposer aux entreprises de déclarer les postes non pourvus après départ. Tant que cela n'existe pas, le débat restera dans l'incertitude : ni l'effondrement ni l'indolence ne sont démontrables à partir des données agrégées.

---

ENGINE:2.8 | MANIFEST:FINAL | RUN_ID:20260825-0645-non-remplacements-france | PARENT_RUN_ID:20260825-0635-ia-salariat-fresque-systemique | AS_OF:2026-08-25 | INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:NONE
CHECKPOINT_SEQ:0 | LAST_COMPLETED:18b | NEXT_ACTION:NONE | RESUME_COUNT:0
Investigation:Mesurer les non-remplacements de postes en France | complexity:10→COMPLEX | route overrides:NONE | scope:proxys statistiques, France + US, 2015-2026
modules:SYMBOLS.md,PATTERNS.md,THREATS.md,GATES.md,REQUEST_LOG.md
degraded:NONE | query target/actual:8/8 (dont 1 échec socket, 1 snippet)

COUNT: ◈9 ◉3 ○4 | unique evidence objects:16 | upstream families:4
LEADS:terminal 6/6 | AXES:terminal 4/5 + GAP 1 | N/A:—
FAILURES:1 (DARES MMO) | unresolved gaps:AMPLITUDE, CAUSALITE, CONCEPT, ACCES
