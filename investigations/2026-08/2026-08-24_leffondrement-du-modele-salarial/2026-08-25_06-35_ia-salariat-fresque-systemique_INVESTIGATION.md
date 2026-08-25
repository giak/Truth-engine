# INVESTIGATION KERNEL v2.8 (UPDATE) : IA & SALARIAT — FRESQUE SYSTÉMIQUE TRANSDISCIPLINAIRE

> **Périmètre** : fresque de synthèse critique et transdisciplinaire sur le problème « IA et salariat », à partir des 17 investigations KERNEL du 2026-08-24 (série « L'effondrement du modèle salarial ») complétées par les dimensions manquantes : anthropologique, narrative, communication/marketing, technique (données 2026).
>
> **COMPANIONS (17 investigations, toutes gate PASS)** :
> - Maître : `2026-08-24_18-22_leffondrement-du-modele-salarial_INVESTIGATION.md` (11 claims, 18 faits)
> - RENARD CORE : `2026-08-24_20-00_leffondrement-modele-salarial-renard_INVESTIGATION.md`
> - RENARD CORE v2 : `2026-08-24_20-25_leffondrement-renard-v2_INVESTIGATION.md`
> - 10 ZONES D'OMBRE : `2026-08-24_20-30_leffondrement-10-zones_INVESTIGATION.md` + `2026-08-24_DEEP_DIVE_10_ZONES.md`
> - Série IA & SOCIÉTÉ #1-10 : histoire, droit-travail, professions, géopolitique, énergie, éducation, psychologie, démocratie, philosophie, revenu-universel
> - Cas : CAPGEMINI. Forensic transcript : `2026-08-24_TRANSCRIPT_FORENSIC.md`. Brainstorm transverse : `2026-08-24_BRAINSTORM_THESE_TRANSVERSE.md`

## RUN_MANIFEST

| Champ | Valeur |
|---|---|
| ENGINE_VERSION | 2.8 |
| STATE | FINAL |
| RUN_ID | 20260825-0635-ia-salariat-fresque-systemique |
| PARENT_RUN_ID | 20260824-1822-leffondrement-du-modele-salarial |
| AS_OF | 2026-08-25 |
| INPUT_KIND | UPDATE |
| MISSION_MODE | INVESTIGATION |
| INPUT_REF | NONE (topique transverse, corpus = 17 investigations parentes) |
| SUBJECT_SLUG | ia-salariat-fresque-systemique |
| INVESTIGATION_PATH | investigations/2026-08/2026-08-25_ia-salariat-fresque-systemique/2026-08-25_06-35_ia-salariat-fresque-systemique_INVESTIGATION.md |
| SCOPE | Fresque systémique : IA et salariat sous 12 dimensions (juridique, technique, psychologique, anthropologique, politique, économique, sociale, éthique, narrative, scientifique, communication/marketing, géopolitique). Logiques de pouvoir, intérêts en jeu, récits dominants, conséquences concrètes. Période 2013-2026, focale France + Europe + US. |
| COMPLEXITY | 14 → APEX |
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
| Frey & Osborne (47 % emplois informatables) | 2013 |
| Taxe robot Hamon, rejet Parlement européen | 16/02/2017 |
| Étude DiPLab travailleurs du clic France | 15/02/2019 |
| CSG (création → 9,2 %) | 1991 → 2018 |
| Allègements généraux cotisations | 20,9 Md€ (2014) → 77 Md€ (2024) |
| Déficit Sécurité sociale 2025 | 21,6 Md€ (Cour des comptes, 27/05/2026) |
| Étude Coface/OEM (3,8 % / 16,3 %) | 01/04/2026 |
| Rapport Sénat « L'entreprise 5.0 » (n° 572) | 2025-2026 |
| Révélation France Travail CCRE (LQDN/Radio France) | 20/07/2026 |
| New standards comptables US pays-par-pays | fin 2025 |
| Données FACT/ITEP/Reuters sur fiscalité Big Tech | 2026 (fév-août) |
| Date d'investigation | 2026-08-25 |

## MANIPULATION_REPORT — le récit dominant

| Champ | Valeur |
|---|---|
| INPUT_KIND | UPDATE (topique) |
| MISSION_MODE | INVESTIGATION |
| SYMBOL_STAGE | CORPUS_FINAL |
| PATTERNS | @PAT[ICEBERG] (travail invisible, non-remplacements), @PAT[MONEY] (business model anxiogène, paradis data), @PAT[POLITICAL], @PAT[FASC] (faisceaux), @PAT[CYN] (stratégies « plus pour la forme ») |
| THREATS | @THR[SHOCK] (fenêtre 12-18 mois), @THR[DARK_MONEY] (OpenAI Ireland, profits délocalisés), @THR[PREDICTIVE_SURV] (France Travail CCRE), @THR[NARR_LAUNDER] (récit de licenciements IA) |
| RHETORICAL | DEM:3, BF:3, NUM:4 (chiffres sans sources, bases changeantes), AUTH:4 (leaders IA en posture d'autorité), FAC:4 (stratégies-spectacle) |
| COMPLEXITY | 14 → APEX |
| CLUSTERS | ICEBERG, MONEY, FRAMING, POWER, NETWORK, TEMPORAL, OVERLOAD, SPECTACLE |
| IMPLICIT | Omissions centrales du récit dominant : données réelles d'adoption (31 % en production), travail invisible du micro-travail, contre-exemples (Allemagne, CSG, taxe GAFAM, Mistral), effet de polarisation interne (élite IA vs laggards), boucle « les vendeurs de peur et les vendeurs d'IA ont le même intérêt » |
| SPEAKER | Récit multipolaire : leaders de labos IA, créateurs de contenu YouTube, cabinets de conseil, médias, États. Ton catastrophiste ou « performance art » (75 % des dirigeants) |
| ASSUMPTIONS | Substitution massive = inévitable et proche ; l'IA est un substitut du travail, pas une transformation ; le déficit social est causé par l'IA (faux : dépense) |
| PRIORITIES | Tester : le récit d'urgence vs les données d'adoption ; l'asymétrie réelle vs la « subvention » ; les intérêts convergents |
| QUERY_GUIDANCE | Sources primaires 2026 : Sénat, Cour des comptes, FIPECO, ITEP, FACT, SIEPR, Writer/Workplace Intelligence, La Quadrature du Net |

## CRÉDO

**LEAD_QUESTION** : La vidéo « L'effondrement du modèle salarial » et, plus largement, le récit dominant de la panique IA sont-ils factuellement fiables et proportionnés ?

**OBJECT_QUESTION** : Quelles logiques de pouvoir, quels intérêts et quels récits structurent le problème « IA et salariat », et quelles sont les conséquences concrètes, documentées ou bornées, sur le travail, le financement social et la décision publique ?

### AXS — 12 axes transdisciplinaires

| AXS-ID | DIMENSION | QUESTION | SOURCES PRINCIPALES | STATUS |
|---|---|---|---|---|
| AXS-001 | Juridique | L'État est-il désarmé face à la substitution ? (AI Act, RGPD art. 22, taxe GAFAM, Piliers 1/2, droit du travail) | droit-travail inv., 10-zones Z5 | SATURATED |
| AXS-002 | Technique | L'IA peut-elle réellement remplacer le travail cognitif ? (scaling wall, agents 2026, ROI) | 10-zones Z6, Writer 2026, Okhrem/Gartner 2026 | SATURATED |
| AXS-003 | Psychologique | Comment la peur opère-t-elle sur les travailleurs et les décideurs ? | psychologie inv., Writer (stress/sabotage) | SATURATED |
| AXS-004 | Anthropologique | Que devient le sens du travail quand la tâche se fragmente ? | DiPLab, Projet Sens, polarisation professions | PARTIEL (openedition bloqué) |
| AXS-005 | Politique | Le débat institutionnel existe-t-il ? Qui décide sans vote ? | démocratie inv., 10-zones Z8, brainstorm transverse | SATURATED |
| AXS-006 | Économique | L'asymétrie fiscale est-elle réelle et le trou chiffrable ? | fiscale inv., FIPECO, 10-zones Z3/Z4 | SATURATED |
| AXS-007 | Sociale | Qui est exposé, qui est protégé ? (professions, revenus) | sociologie-professions inv., Sénat r25-572 | SATURATED |
| AXS-008 | Éthique | La « taxe robot » et le partage de la valeur sont-ils pensables ? | philosophie inv., 10-zones Z7 | SATURATED |
| AXS-009 | Narrative | Comment le récit de la panique est-il construit et par qui ? | TRANSCRIPT_FORENSIC, SIEPR, PBS, doom industry | SATURATED |
| AXS-010 | Scientifique | Que disent les données (Frey/Autor, BCE/EIB, Coface) ? | histoire inv., BCE/EIB/Anthropic/DG Trésor | SATURATED |
| AXS-011 | Communication/Marketing | Qui vend la peur, qui vend l'IA, qui vend la transformation ? | DEEP DIVE #1, SIEPR, Writer, cabinet-conseil | SATURATED |
| AXS-012 | Géopolitique | Qui produit, qui régule, qui capte la valeur ? | géopolitique inv., paradis data, Draghi | SATURATED |

## SYMBOL_SCORES (15/15, CORPUS_FINAL — le récit dominant, pas seulement la vidéo)

| Sym | Nom | Score | Observations |
|---|---|---|---|
| Ξ | Omission | 7 | Le récit omet : données réelles d'adoption (31 % agents en production), travail invisible (250-260 000 micro-travailleurs FR), contre-exemples (Allemagne 47,9 %, CSG 9,2 % déjà en place, taxe GAFAM), causes réelles du déficit (dépense +3,6 % vs recettes +2,6 %), boucle des intérêts |
| € | Money | 7 | Dépenses IA mondiales 301 Md$ (IDC 2026) ; business model anxiogène (Patreon, club surhumain.ai) ; profits délocalisés (Microsoft 3,5 Md$ Irlande, 23,3 Md$ par 55 firmes, Apple 17,1 Md$ à l'Irlande) ; cabinets de conseil vendant la transformation |
| Λ | Framing | 6 | « Effondrement », « apocalypse de l'emploi », « subvention involontaire » = cadrages ; « performance art » des stratégies IA (75 % des dirigeants) ; trilemme présenté comme exhaustif |
| Ω | Inversion | 4 | Les leaders IA amplifient la peur qu'ils vendent (SIEPR : Amodei) ; licenciements présentés comme causés par l'IA alors que la stratégie a échoué (Ferguson : prétexte) ; « le problème est la solution » (Patreon reproduit l'asymétrie dénoncée) |
| Ψ | Sidération | 6 | Infodémie de chiffres contradictoires (BIT 5 % vs FMI 33 %), urgence « fenêtre 12-18 mois », FOMO des dirigeants (64 % craignent de perdre leur emploi) |
| ↕ | Vertical power | 7 | Asymétrie structurelle : travail visible taxé vs travail invisible non taxé vs profits délocalisables ; élite IA vs laggards (92 % cultivent l'élite, 60 % licencieront les non-adoptants) ; contrôle social automatisé (France Travail, 6 M profilés) |
| Φ | Spectacle | 5 | Titres dramatiques YouTube, doom industry (PBS, juin 2026), couverture médiatique des licenciements IA |
| Σ | Semiotics | 4 | Stratégies IA « plus pour la forme » que pour le guidage (75 %) ; « IA éthique et transparente » de France Travail vs refus CADA ; cloud « souverain » (Bleu = Microsoft+Orange+Capgemini) |
| Κ | Cynicism | 6 | Écart public/privé documenté (stratégies-spectacle, 48 % déception massive) ; asymétrie d'information décideur/citoyen (« personne ne l'a voté ») |
| ρ | Resistance | 3 | Contre-pouvoirs documentés mais minoritaires : LQDN (France Travail), syndicats (CFDT, CGT, Ugict), OIT, fact-checkers ; aucun rapport parlementaire dédié « IA et financement social » |
| κ | Subtle influence | 5 | CTA Patreon final (FOMO), architecture de l'urgence, dark patterns des plateformes ; scoring et profilage (26 variables) |
| ⫸ | Convergence | 6 | Faisceaux indépendants : asymétrie fiscale + triple fuite (cotisations/import/données) + érosion lente + contrôle social + performativité des stratégies. Convergence de fait, pas de coordination |
| ⚔ | Cognitive warfare | 2 | Aucune infrastructure de campagne coordonnée démontrée ; amplification organique par intérêts convergents |
| 🌐 | Network | 5 | OpenAI/Anthropic → Dublin (IS 12,5 %, pertes massives → impôt ~0) ; créateurs → Patreon ; cabinets → clients ; États → stratégies IA ; médias → attention |
| ⏰ | Temporal | 5 | Urgence artificielle (« 12-18 mois », « fenêtre maximale ») vs cycles réels de 30-80 ans (1945, 1991, 2018) ; timing des révélations (CCRE présenté en comité d'éthique déc. 2025, révélé juil. 2026) |

## CLAIM_REGISTRY — claims transverses

| CLM-ID | CLAIM | SUPPORT | COUNTER | STATUS | GAP_TYPE |
|---|---|---|---|---|---|
| CLM-101 | L'asymétrie fiscale (cotisations sur travail, zéro sur IA) est réelle | URSSAF, FIPECO, code général des impôts | Ce n'est pas une « subvention » : c'est un choix de financement ; CSG/TVA déjà décorrélées (52 % du financement) | VERIFIE (fait) / ⊙ (cadrage « subvention ») | — |
| CLM-102 | La substitution massive est en cours et va s'accélérer brutalement | Coface/OEM : 16,3 % de l'emploi menacé à 2-5 ans (exposition technique, pas destruction) | 82 % des entreprises FR sans IA (Insee 2024) ; 31 % des agents en production (2026) ; 25 % des initiatives livrent le ROI attendu ; 40 % de projets annulés d'ici 2027 | PROBABLE (directionnel) / ❧ (ampleur) | DONNEES_AMPLITUDE |
| CLM-103 | Le modèle social s'effondre sous l'effet de l'IA dans 12-18 mois | Aucune source institutionnelle | Déficit 2025 = 21,6 Md€ causé par la dépense (+3,6 %) pas l'IA ; recettes +2,6 % ; bornes 4-8 Md€/an (pessimiste) vs 77 Md€ allègements | REFUTE (horizon) | — |
| CLM-104 | Le travail invisible (micro-travail) échappe à l'assiette sociale | DiPLab : 250-260 000 en FR, 21 €/mois ; Banque mondiale : centaines de millions | Données 2019, pas de mise à jour française ; les plateformes créent aussi des revenus déclarés | PROBABLE | DONNEES_ACTUALISATION |
| CLM-105 | Les profits de l'IA sont structurellement délocalisables | FACT : Microsoft 3,5 Md$ via Irlande ; ITEP : 51 Md$ évités par 4 firmes ; Reuters : Apple 17,1 Md$ à l'Irlande (40 %) | Pilier 2 OCDE (15 %) en vigueur ; taxe GAFAM 0,7 Md€ ; l'UE peut réagir | VERIFIE (fait) / ⊙ (inévitabilité) | — |
| CLM-106 | Le récit de la panique sert les intérêts convergents des vendeurs d'IA et des vendeurs de peur | SIEPR (amplification par les leaders), DEEP DIVE #1 (Patreon), Ferguson (prétexte), Verdugo (promoteurs) | Les leaders peuvent être sincèrement inquiets ; la peur peut aussi freiner l'adoption | PROBABLE (mécanisme documenté, pas d'intention prouvée) | INTENTION |
| CLM-107 | L'État applique déjà l'IA au contrôle social | LQDN/Radio France : CCRE, 26 variables, 6 M de personnes profilables, contrôles 730 000 (2025) → 1,5 M (2027) | France Travail communique « IA éthique » ; comité d'éthique consulté ; question écrite au Sénat | VERIFIE (déploiement en test) | PORTEE |
| CLM-108 | La décision sans légitimation est le mode normal du système, et l'IA l'accélère | Brainstorm transverse : 3/8 cas de « capture de la solution » (IA, cloud, ENR) ; CSG 1991 = transition silencieuse | « Personne ne l'a voté » = imputé, pas documenté ; la version « l'IA remplace le décideur » est une hypothèse non documentée | PARTIEL (3/8) / ⁂ (version C) | DOCUMENTATION |

## FACT_REGISTRY_V1 — faits nouveaux de la session (2026-08-25)

| FCT-ID | EPI | TIER | URL | FAMILIES | DATE | SUJET | VALEUR | MEM |
|---|---|---|---|---|---|---|---|---|
| FCT-101 | FACT | ✧ | https://www.senat.fr/rap/r25-572/r25-5724.html | A,D | 2026 | Emploi français fragilisé par l'IA générative (Coface/OEM, 923 professions) | 3,8 % aujourd'hui ; 16,3 % (≈5 M) à 2-5 ans en IA agentique ; exposition technique ≠ destruction nette | mem:- |
| FCT-102 | FACT | ✧ | https://www.senat.fr/rap/r25-572/r25-5724.html | A,D | 2026 | Géographie de l'exposition (Sénat/Coface) | Ingénierie 26,9 %, informatique pic 31 %, admin 23,8 %, créatifs 23,8 %, droit 21,6 % ; 10 % les plus hauts revenus menacés à 22,1 % ; manufacturier protégé | mem:- |
| FCT-103 | FACT | ✧ | https://www.telecom-paris.fr/micro-travailleurs | C,E | 2019 | Micro-travailleurs du clic en France (DiPLab) | 250 000-260 000 ; revenu moyen ~21 €/mois ; sans contrat ni protection sociale | mem:- |
| FCT-104 | FACT | ✧ | https://thefactcoalition.org/ireland-ai-and-microsofts-vanishing-tax-bill/ | D | 2026-08 | Fiscalité Microsoft/IA (FACT) | 3,5 Md$ d'économies via l'Irlande ; plus d'impôt en espèces à l'Irlande qu'aux US ; 23,3 Md$ par 55 firmes US ; taux fédéraux Microsoft 2,5 %, Meta 3,5 %, Google 8 %, Amazon 1,4 % ; -12 Md$ via dépréciation accélérée | mem:- |
| FCT-105 | FACT | ✧ | https://itep.org/trump-meta-tesla-alphabet-amazon-obbba-taxes/ | D | 2026-02-06 | Impôt US 2025 des 4 Big Tech (ITEP) | 315 Md$ de profits, taux effectif 4,9 %, Tesla 0 %, 51 Md$ d'impôt fédéral évités | mem:- |
| FCT-106 | FACT | ✧ | https://www.reuters.com/legal/transactional/apple-paid-40-its-global-taxes-ireland-last-fiscal-year-2026-08-21/ | C,D | 2026-08-21 | Apple et l'Irlande (Reuters/10-K FY2025) | 17,1 Md$ versés à l'Irlande, ~40 % du total mondial (43,2 Md$) | mem:- |
| FCT-107 | FACT | ✦ | https://www.ccomptes.fr/fr/publications/securite-sociale-2026 | A,D | 2026-05-27 | Comptes Sécurité sociale (Cour des comptes) | Déficit 2025 : 21,6 Md€ (doublé en 2 ans) ; 2026 : 19,4 Md€ attendus (recettes nouvelles > économies) ; recettes +2,6 % vs dépenses +3,6 % ; risques +3 Md€ (2026) et +5 Md€ (2027) ; équilibre demandé en 2030 | mem:- |
| FCT-108 | FACT | ✧ | https://www.laquadrature.net/2026/07/20/france-travail-deploie-un-outil-de-profilage-algorithmique-a-des-fins-de-controle/ | B | 2026-07-20 | France Travail, algorithme CCRE (LQDN/Radio France) | Profilage 26 variables, entraîné sur 60 000 contrôles ; 2 campagnes × 7 000 tests (ruptures conventionnelles) ; objectif 6 M profilés/mois (RSA obligatoire depuis 01/01/2026) ; contrôles 200 000 (2017) → 730 000 (2025) → 1,5 M (2027) | mem:- |
| FCT-109 | FACT | ✧ | https://cse.belgique.be/fr/accueil/rapports-avis/rapports-2026/lintelligence-artificielle-et-le-marche-du-travail-en-belgique-fevrier-2026 | A | 2026-02 | IA et marché du travail belge (CSE) | 35 % des entreprises utilisent l'IA (+20 pts en 2 ans) ; 1 travailleur sur 3 ; « pas de perte massive d'emplois » ; 39 % besoins de formation vs 14 % formés | mem:- |
| FCT-110 | FACT | ✧ | https://siepr.stanford.edu/publications/policy-brief/what-really-happening-jobs-separating-ai-hype-reality | E | 2026-07-06 | Amplification de la peur par les leaders IA (SIEPR/Stanford) | Les craintes d'apocalypse de l'emploi sont souvent amplifiées par les leaders de l'IA eux-mêmes (ex. Dario Amodei) | mem:- |
| FCT-111 | FACT | ✧ | https://www.fipeco.fr/fiche/Les-cotisations-sociales | A,D | 2026-06-20 | Cotisations sociales 2025 (FIPECO) | Produit net 443 Md€ (14,8 % PIB) ; assiette 1 078 Md€ (738 privé + 171 fonctionnaires + 105 indépendants) ; 1 point = 10,8 Md€ ; élasticité 0,95 (+1 % revenus = +4,4 Md€) ; cotisations = 55 % des ressources des ASSO (98 % en 1980) | mem:- |
| FCT-112 | FACT | ✧ | https://writer.com/blog/enterprise-ai-adoption-2026/ | C | 2026-04-07 | Adoption IA en entreprise 2026 (Writer/Workplace Intelligence, n=2 400) | 79 % des organisations rencontrent des défis ; 75 % des dirigeants : stratégie « plus pour la forme » ; 48 % déception massive ; 29 % ROI significatif (gén. IA) ; 92 % cultivent une « élite IA » ; 60 % prévoient des licenciements pour non-adoptants ; 29 % des salariés sabotent la stratégie IA | mem:- |
| FCT-113 | FACT | ✧ | https://paul-okhrem.com/enterprise-ai-agents-statistics-2026/ | D | 2026-08-08 | Agents IA en production (compilation Gartner/McKinsey/IBM) | ~80 % des apps embarquent un agent, 31 % en production ; >40 % des projets agentiques annulés d'ici 2027 (Gartner) ; 25 % des initiatives livrent le ROI attendu (IBM) ; 6 % de vrais « high performers » (McKinsey) ; 52 % : qualité des données = blocage n°1 | mem:- |

## EVIDENCE_REGISTRY — sources de la session

| SRC-ID | TYPE | TITLE | URL | FAMILY | ROLE | LOCATOR | DATE |
|---|---|---|---|---|---|---|---|
| SRC-101 | ◈ | Sénat, rapport « L'entreprise 5.0 » n° 572 | https://www.senat.fr/rap/r25-572/r25-5724.html | A | ◉ | C. « conversion massive » ; Coface/OEM ; professions ; Verdugo ; Ferguson | 2025-2026 |
| SRC-102 | ◈ | Cour des comptes, Sécurité sociale 2026 | https://www.ccomptes.fr/fr/publications/securite-sociale-2026 | A,D | ◈ | « Le déficit a doublé en deux ans... 21,6 Md€ en 2025 » | 2026-05-27 |
| SRC-103 | ◈ | FIPECO, « Les cotisations sociales » | https://www.fipeco.fr/fiche/Les-cotisations-sociales | A,D | ◈ | Assiette, produit, élasticité, 55 % des ASSO | 2026-06-20 |
| SRC-104 | ◈ | La Quadrature du Net, France Travail CCRE | https://www.laquadrature.net/2026/07/20/france-travail-deploie-un-outil-de-profilage-algorithmique-a-des-fins-de-controle/ | B | ◈ | Document interne, 26 variables, 60 000 contrôles | 2026-07-20 |
| SRC-105 | ◈ | FACT Coalition, Microsoft/Irlande | https://thefactcoalition.org/ireland-ai-and-microsofts-vanishing-tax-bill/ | D | ◉ | « saved almost $3.5 billion... more cash tax to Ireland than to the U.S. federal government » | 2026-08 |
| SRC-106 | ◈ | ITEP, 4 Big Tech | https://itep.org/trump-meta-tesla-alphabet-amazon-obbba-taxes/ | D | ◉ | « $315 billion in U.S. profits... 4.9 percent » | 2026-02-06 |
| SRC-107 | ◈ | Reuters, Apple/Irlande | https://www.reuters.com/legal/transactional/apple-paid-40-its-global-taxes-ireland-last-fiscal-year-2026-08-21/ | C,D | ◈ | 17,1 Md$, 40 % du total | 2026-08-21 |
| SRC-108 | ◈ | DiPLab (Télécom Paris, CNRS) | https://www.telecom-paris.fr/micro-travailleurs | C,E | ◈ | 260 000, 21 €/mois | 2019-05-24 |
| SRC-109 | ◈ | SIEPR/Stanford, « What is really happening to jobs? » | https://siepr.stanford.edu/publications/policy-brief/what-really-happening-jobs-separating-ai-hype-reality | E | ◉ | Mahoney, McEntarfer, Wahal ; amplification par les leaders | 2026-07-06 |
| SRC-110 | ◈ | Writer/Workplace Intelligence, adoption 2026 | https://writer.com/blog/enterprise-ai-adoption-2026/ | C | ◉ | n=2 400 ; 75 % stratégie « pour la forme » | 2026-04-07 |
| SRC-111 | ◈ | Paul Okhrem, stats agents 2026 | https://paul-okhrem.com/enterprise-ai-agents-statistics-2026/ | D | ◉ | Compilation Gartner/McKinsey/IBM/IDC | 2026-08-08 |
| SRC-112 | ◈ | CSE Belgique, IA et marché du travail | https://cse.belgique.be/fr/accueil/rapports-avis/rapports-2026/lintelligence-artificielle-et-le-marche-du-travail-en-belgique-fevrier-2026 | A | ◈ | 35 %, +20 pts, 1/3, 39 %/14 % | 2026-02 |
| SRC-113 | ◈ | Sénat, question écrite France Travail/IA | https://www.senat.fr/questions/base/2026/qSEQ260709657.html | A | ◈ | Modèle prédictif « quels sont les chômeurs qui cherchent bien » | 2026-07-31 |
| SRC-114 | ○ | Quartz, marché des données d'entraînement | https://qz.com/ai-training-data-pricing-licensing-deals-market-052126 | C | ○ | 3,59 Md$ (2025) → 4,44 Md$ (2026) | 2026-05-27 |
| SRC-115 | ○ | Neudata, accords de licence IA | https://www.neudata.co/blog/ai-data-licensing-market-analysis | C | ○ | Perplexity 37 % des accords, OpenAI 29 % | 2025-06-10 |

## CAUSALITY_REGISTRY — les boucles de pouvoir

| CAU-ID | EDGE | TYPE | SOURCE | GAP |
|---|---|---|---|---|
| CAU-101 | Récit de peur (leaders IA, médias, créateurs) → anxiété publique → adoption accélérée (peur de rater) → dépenses IA (301 Md$) → valorisations → incitation à amplifier le récit | FEEDBACK_LOOP | SRC-109 (SIEPR), SRC-110 (Writer), IDC (via SRC-111) | L'intention des leaders n'est pas prouvée (BENEFIT != INTENT) |
| CAU-102 | Asymétrie fiscale réelle (cotisations sur travail, zéro sur conso intermédiaire) → coût relatif IA/travail favorable → substitution marginale → érosion lente de l'assiette | CAUSE | FIPECO, URSSAF, fiscale inv. (CAU-001..004) | Amplitude non mesurée en France (non-remplacements invisibles) |
| CAU-103 | Micro-travail (tâches atomisées, sans employeur) → échappe à l'assiette de 1 078 Md€ → érosion sans licenciement visible | ENABLER | SRC-108 (DiPLab) | Données françaises de 2019, non actualisées |
| CAU-104 | Profits IA immatériels → délocalisables (Dublin, etc.) → recettes fiscales faibles (4,9 % effectif) → déficit → discours d'austérité → contrôle accru des dépenses sociales (CCRE) | CAUSE | SRC-105, 106, 107 ; SRC-104 (LQDN) | La séquence austérité → contrôle est partiellement inférée (LQDN la documente pour FT) |
| CAU-105 | Panique → licenciements présentés comme causés par l'IA (prétexte, échec stratégique) → anxiété des salariés → conformité/adoption forcée | CAUSE | Ferguson (Sénat r25-572), SRC-110 (60 % licencieront les non-adoptants) | La part « prétexte » vs « réelle » n'est pas quantifiée |
| CAU-106 | Élite IA vs laggards (92 % cultivent l'élite) → polarisation interne → inégalités de salaires/promotions → fragmentation du collectif de travail | CAUSE | SRC-110 (Writer) | Effet sur la négociation collective non documenté |
| CAU-107 | « Personne ne l'a voté » (décision sans légitimation) + IA → automatisation de la décision (scoring, profilage) → déplacement du pouvoir de décision hors du débat public | HYPOTHESE | Brainstorm transverse (version C), SRC-104 (CCRE) | Version C non documentée empiriquement (BREAK) ; CCRE documente le profilage, pas la décision politique |

## ACTOR_NETWORK_MAP

| ACT-ID | NAME | ROLE | DOCUMENTED_ACTION | SOURCE | INTENT |
|---|---|---|---|---|---|
| ACT-101 | Labos IA (OpenAI, Anthropic, Google) | Vendeurs d'IA | Structure Dublin (IS 12,5 %, pertes massives → impôt ~0) ; Amodei amplifie les craintes (SIEPR) ; licences de données (News Corp ~250 M$, Perplexity/OpenAI) | SRC-105, 109, 114, 115 ; 10-zones Z1 | CLAIMED (profit) ; amplification : CLAIMED par SIEPR |
| ACT-102 | Créateur « IA et Stratégie » (Sam) | Vendeur de peur | Vidéo 32 min sans sources ; Patreon, Discord « trié », club surhumain.ai ; « thèses que je ne peux pas défendre publiquement » | DEEP DIVE #1 ; investigation parente | CLAIMED (monétisation) |
| ACT-103 | Cabinets de conseil (McKinsey, BCG, IDC...) | Vendeurs de transformation | Produisent les chiffres de ROI (171 % agents, 3,7x) et les stratégies « pour la forme » (75 %) | SRC-111, 110 | CLAIMED (honoraires) |
| ACT-104 | États (France, UE, Allemagne) | Régulateurs/acheteurs | France : stratégie IA, compensation 77 Md€ d'allègements, CCRE (profilage) ; Allemagne : taxe numérique appelée (Klingbeil, 01/2026) ; UE : AI Act, SURE 2.0 (CES) | SRC-104, 107 ; 10-zones Z5, Z8 ; géopolitique inv. | MIXTE |
| ACT-105 | Syndicats (CFDT, CGT, Ugict) | Contre-pouvoir | Guides IA, demande de dialogue social ; aucun ne réclame de « taxe IA » | 10-zones Z8 | PROVEN (encadrement) |
| ACT-106 | LQDN + Radio France | Contre-pouvoir technique | Révélation CCRE, demande d'accès au code, saisine CADA | SRC-104 | PROVEN (transparence) |
| ACT-107 | Travailleurs du clic | Invisibles | Entraînent les modèles, ~21 €/mois, sans statut ; centaines de millions (Banque mondiale) | SRC-108 ; RFI, Franceinfo | UNKNOWN |
| ACT-108 | Salariés français | Exposés/acteurs | 75 % utilisent des outils non validés (shadow AI) ; 29 % sabotent la stratégie IA ; 64 % des dirigeants craignent de perdre leur emploi | Sénat r25-572 ; SRC-110 | MIXTE |

## CONTROL_MAP

| CTRL-ID | CONTROLLER | MECHANISM | RULE/AUTHORITY | DOCUMENTED RESULT | FCT/SRC | GAP |
|---|---|---|---|---|---|---|
| CTRL-101 | État français | Cotisations sociales | Code de la sécurité sociale | Assiette 1 078 Md€, produit 443 Md€ | FCT-111 | — |
| CTRL-102 | État français | RGDU/allègements | LFSS | 77 Md€ d'allègements non conditionnés | Cour 2025 (parente) | Conditionnalité absente |
| CTRL-103 | États de marché | Pilier 2 OCDE (15 %) | LF 2025 | Applicable aux groupes >750 M€ | 10-zones Z5 | OpenAI/Anthropic dans le périmètre mais pertes → ~0 |
| CTRL-104 | UE | AI Act (haut risque) | Règlement 2024/1689 | Obligations annexe III au 02/12/2027 | article actuel | Calendrier long |
| CTRL-105 | France Travail | CCRE (profilage) | Document comité d'éthique 10/12/2025 | 26 variables, 6 M profilables, test 2×7 000 | FCT-108 | Code source non publié ; CADA saisie |
| CTRL-106 | Entreprises | Stratégie IA « pour la forme » | Direction | 75 % admettent le décalage ; 69 % licenciements IA prévus | SRC-110 | Aucune sanction |

## RESOURCE_FLOW_MAP

| FLOW-ID | FROM | TO | NATURE | MECHANISM | STATUS |
|---|---|---|---|---|---|
| FLOW-101 | Travail visible | URSSAF/Sécu | Cotisations (443 Md€) | Prélèvement sur salaires | ACTIVE |
| FLOW-102 | Entreprises | Fournisseurs IA | Abonnements/API (301 Md$ mondial) | Facture service, zéro cotisation | ACTIVE |
| FLOW-103 | Profits IA | Paradis de la data (Irlande...) | 23,3 Md$ d'économies déclarées (55 firmes) | Prix de transfert, localisation | ACTIVE |
| FLOW-104 | Utilisateurs (FR/UE) | Modèles IA | Données professionnelles non taxées | Extraction via usage | ACTIVE |
| FLOW-105 | Travailleurs du clic | Plateformes | Micro-tâches (~21 €/mois) | Rémunération à l'unité | ACTIVE |
| FLOW-106 | État | Sécu | Compensation allègements (77 Md€) | Article L131-7 CSS | ACTIVE |
| FLOW-107 | État | France Travail | Budget contrôle (730 000 → 1,5 M contrôles) | Objectif gouvernemental 2027 | ACTIVE |
| FLOW-108 | Salariés | Entreprises | Valeur augmentée par l'IA (élite IA 5x) | Captation par les super-users | ACTIVE (polarisation) |

## IMPACT_MAP

| IMP-ID | EFFECT | AFFECTED | EVIDENCE | STATUS |
|---|---|---|---|---|
| IMP-101 | Érosion lente de l'assiette des cotisations | Sécu, branches | Bornes : 4-8 Md€/an (scénario pessimiste cadres, deep dive Z3) ; 60-70 Md€ (scénario 16,3 % sur 5 ans, élasticité FIPECO 0,95) | PROBABLE (directionnel, amplitude non observée) |
| IMP-102 | Polarisation du travail (élite IA vs laggards) | Salariés | Writer : 92 % cultivent l'élite, 60 % licencieront les non-adoptants, super-users 3x promotions | VERIFIE (enquête) |
| IMP-103 | Contrôle social automatisé | 6 M de chômeurs/RSA | CCRE : 26 variables, listes prioritaires, contrôles 730 000 (2025) | VERIFIE (en test) |
| IMP-104 | Perte de recettes fiscales sur profits délocalisés | États de marché | 4,9 % effectif US ; 17,1 Md$ Apple vers l'Irlande | VERIFIE |
| IMP-105 | Anxiété massive et sabotage | Salariés, dirigeants | 64 % des dirigeants craignent de perdre leur emploi ; 29 % des salariés sabotent ; 73 % des CEO stressés | VERIFIE (enquête) |
| IMP-106 | Vide politique sur « IA et financement social » | Débat public | Aucun rapport parlementaire dédié ; syndicats sans position « taxe IA » | VERIFIE (absence documentée) |
| IMP-107 | Fuites de données via shadow AI | Entreprises | 67 % : fuite due à des outils non approuvés ; 35 % : entrée de données propriétaires dans des outils publics | VERIFIE (enquête) |
| IMP-108 | Création nette d'emplois non mesurée en France | Statistique publique | Aucun suivi des non-remplacements ; cas documentés isolés (Capgemini 2 400, DeepL 250) | GAP |

## CONTRADICTION_LEDGER

| CONTRADICTION | ENTITIES | RESOLUTION |
|---|---|---|
| « Substitution massive en cours » vs 82 % des entreprises FR sans IA (2024) ; 31 % des agents en production (2026) ; 25 % des initiatives livrent le ROI | CLM-102, FCT-113, Insee | L'exposition technique (Coface 16,3 %) ne préjuge pas de la destruction ; l'adoption réelle est lente et décevante |
| « La France, pays le plus exposé » vs Allemagne 47,9 % (coin fiscal supérieur, même modèle Bismarck) | 10-zones Z2 | Omission stratégique de la vidéo ; la France n'est pas unique |
| « La taxe IA est infaisable » vs taxe GAFAM 0,7 Md€ existante + amendement 6 % + Pilier 2 (15 %) transposé | 10-zones Z5 | Exagération : taxer l'inférence est difficile, taxer le CA numérique est faisable |
| « Effondrement en 12-18 mois » vs recettes sociales +2,6 % en 2025 ; déficit piloté par la dépense (+3,6 %) | CLM-103, FCT-107 | Réfuté à l'horizon court ; vulnérabilité structurelle réelle à moyen terme |
| « L'IA remplace le travail » vs l'IA est entraînée par du travail invisible (250-260 000 micro-travailleurs FR) | CLM-104, FCT-103 | L'IA remplace ET consomme du travail ; le récit ne voit que la première moitié |
| « La peur vient des travailleurs » vs amplification par les leaders IA eux-mêmes (SIEPR : Amodei) | CLM-106, FCT-110 | La peur est aussi un produit vendu en amont (labos) et en aval (créateurs) |
| « L'IA éthique et transparente » (France Travail) vs refus de communication du code, CADA saisie | CLM-107, FCT-108 | Écart déclaratif/documentaire documenté |
| ROI annoncé 171 % (agents) vs 25 % des initiatives livrent le ROI attendu (IBM) | FCT-113, SRC-111 | Moyenne trompeuse : distribution très inégale, 6 % de vrais high performers |

## EDI_REPORT (Epistemic Diversity Index)

| Dimension | Score | Commentaire |
|---|---|---|
| A (primary/official) | Fort | Sénat, Cour des comptes, FIPECO, CSE Belgique, Insee, URSSAF |
| B (critical/competing) | Moyen | LQDN (France Travail), syndicats (CFDT/CGT/Ugict), CGT |
| C (affected/witness) | Moyen | Enquêtes salariés/dirigeants (Writer, n=2 400), témoignages travailleurs du clic (DiPLab, RFI, Franceinfo) |
| D (independent investigation) | Fort | OCDE, FIPECO, ITEP, FACT Coalition, Gartner/IBM/McKinsey (compilations) |
| E (academic/expert) | Moyen | SIEPR/Stanford, DiPLab/CNRS, Frey/Autor ; openedition (anthropologie) INACCESSIBLE (Anubis) |

**Verdict EDI** : corpus équilibré A/D/E + C émergent. Faiblesses : anthropologie du travail (source bloquée), témoignages directs de salariés français licenciés (absents), point de vue des travailleurs du clic non français (indirect).

## WOLVES — les loups (angles morts restants)

| LOUP-ID | ANGLE MORT | NATURE | EFFORT NECESSAIRE |
|---|---|---|---|
| L-001 | Amplitude réelle des non-remplacements en France (le « trou » statistique central) | DATA | Suivi des flux d'emplois par poste non pourvu ; aucune source publique |
| L-002 | Anthropologie du travail à l'ère des agents (sens, identité, dignité) | LITTERATURE | Article openedition bloqué (Anubis) ; enquête Projet Sens (60 managers) non lue en primaire |
| L-003 | Effet des agents IA sur les métiers réellement déployés (31 % en production) | DATA | Études de cas sectorielles post-déploiement, quasi inexistantes en 2026 |
| L-004 | Devenir du micro-travail en France depuis 2019 | DATA | Pas de réplication de DiPLab ; la directive plateformes est en suspens |
| L-005 | La « capture de la solution » au-delà de 3/8 cas | CONCEPT | Nécessite un test systématique des échecs de capture (CSG, Mistral, GDPR, Community Notes) |
| L-006 | Performativité des stratégies IA publiques (État acheteur) | ENQUETE | Les marchés publics IA (État) et leurs effets ; « cloud souverain » Bleu |
| L-007 | Réponse fiscale européenne coordonnée (taxe numérique allemande, SURE 2.0, Pilier 1) | SUIVI | En cours, à suivre 2026-2027 |
| L-008 | La boucle « peur → dépense → valorisation » : cartographie précise des flux (301 Md$ IDC) | DONNEES_MARCHE | Données IDC/analystes propriétaires |

## TRACE_MATRIX (résumé)

| ENTITY-ID | TYPE | QRY/SRC ATTEMPTS | RESULT | STATUS |
|---|---|---|---|---|
| AXS-001 Juridique | AXIS | 10-zones Z5, droit-travail inv. (gate b64477d7) | AI Act, RGPD 22, taxe GAFAM 0,7 Md€, Pilier 2 : l'État n'est pas désarmé | SATURATED |
| AXS-002 Technique | AXIS | 10-zones Z6, SRC-110, SRC-111 | Scaling wall (Marcus/LeCun) ; agents : 31 % en production, 40 % annulations, 25 % ROI | SATURATED |
| AXS-003 Psychologique | AXIS | psychologie inv. (gate 539a7dee), SRC-110 | Peur/urgence/FOMO ; stress 73 % CEO ; sabotage 29 % | SATURATED |
| AXS-004 Anthropologique | AXIS | SRC-108, Projet Sens (snippet), openedition (BLOQUE) | Fragmenté : le travail se décompose en micro-tâches ; sens non documenté en primaire | PARTIEL (GAP ACCESS) |
| AXS-005 Politique | AXIS | démocratie inv., 10-zones Z8, brainstorm | Vide politique sur IA+financement social ; « personne ne l'a voté » = 3/8 cas | SATURATED |
| AXS-006 Économique | AXIS | fiscale inv., FIPECO, 10-zones Z3/Z4 | Asymétrie réelle ; trou borné 4-8 Md€/an pessimiste ; CSG = solution existante | SATURATED |
| AXS-007 Sociale | AXIS | SRC-101 (Sénat), professions inv. | 3,8 % fragilisé, 16,3 % exposés, 10 % hauts revenus à 22,1 % ; polarisation | SATURATED |
| AXS-008 Éthique | AXIS | philosophie inv., 10-zones Z7 | Partage de la valeur : participation atténuable (dérogatoire, intéressement, PPV) | SATURATED |
| AXS-009 Narrative | AXIS | TRANSCRIPT_FORENSIC, SRC-109, PBS (snippet) | Le récit de peur est amplifié par les vendeurs d'IA eux-mêmes ; doom industry | SATURATED |
| AXS-010 Scientifique | AXIS | histoire inv., BCE/EIB/Anthropic/Trésor | Ni apocalypse ni indolence ; polarisation des effets ; 82 % des entreprises FR sans IA | SATURATED |
| AXS-011 Marketing | AXIS | DEEP DIVE #1, SRC-110, SRC-111 | Trois étages de monétisation : labos (vente), créateurs (peur), conseil (transformation « pour la forme ») | SATURATED |
| AXS-012 Géopolitique | AXIS | géopolitique inv., SRC-104-107 | Triple fuite (cotisations, import, données) ; paradis de la data ; dépendance US | SATURATED |

## REQUEST_LOG

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---|---:|---|---|---|---|
| 1 | SYS | search_memory (IA salariat effondrement) | FOUND : 6 investigations parentes (gates PASS) | MnemoLite | — |
| 2 | SYS | @READ ALWAYS LOAD (SYMBOLS, PATTERNS, THREATS, GATES, REQUEST_LOG) | LOADED | KERNEL | — |
| 3 | SYS | @READ investigation maîtresse 18-22 + BRAINSTORM + DEEP_DIVE_10_ZONES | LOADED (corpus complet) | dossier parent | — |
| 4 | ◈ | QRY-101 : rapport Sénat L'entreprise 5.0 | FOUND | SRC-101 | senat.fr |
| 5 | ◈ | QRY-102 : Cour des comptes Sécurité sociale 2026 | FOUND | SRC-102 | ccomptes.fr |
| 6 | ◈ | QRY-103 : FIPECO cotisations sociales | FOUND | SRC-103 | fipeco.fr |
| 7 | ◈ | QRY-104 : France Travail algorithme CCRE | FOUND | SRC-104 | laquadrature.net |
| 8 | ◈ | QRY-105 : FACT Coalition Microsoft Irlande | FOUND | SRC-105 | thefactcoalition.org |
| 9 | ◈ | QRY-106 : ITEP 4 Big Tech 51 Md$ | FOUND | SRC-106 | itep.org |
| 10 | ◈ | QRY-107 : Reuters Apple Irlande 17,1 Md$ | FOUND | SRC-107 | reuters.com |
| 11 | ◈ | QRY-108 : DiPLab travailleurs du clic | FOUND | SRC-108 | telecom-paris.fr |
| 12 | ◈ | QRY-109 : SIEPR Stanford jobs AI | FOUND | SRC-109 | siepr.stanford.edu |
| 13 | ◈ | QRY-110 : Writer adoption entreprise 2026 | FOUND | SRC-110 | writer.com |
| 14 | ◈ | QRY-111 : agents IA en production 2026 | FOUND | SRC-111 | paul-okhrem.com |
| 15 | ◈ | QRY-112 : CSE Belgique IA marché du travail | FOUND | SRC-112 | cse.belgique.be |
| 16 | ◈ | QRY-113 : marché données entraînement | FOUND | SRC-114, 115 | qz.com, neudata.co |
| 17 | FAILED | QRY-114 : openedition socio-anthropologie (Fouquet) | FAILED: Anubis anti-robot | — | journals.openedition.org |
| 18 | ◈ | QRY-115 : travailleurs du clic Afrique/Banque mondiale | FOUND | RFI, Aleteia | rfi.fr, aleteia.org |
| 19 | ◈ | QRY-116 : anthropologie du travail / Projet Sens | FOUND (snippet) | aefinfo | aefinfo.fr |
| 20 | SYS | FINAL @WRITE | PENDING_AT_SERIALIZATION | — | INVESTIGATION_PATH |

COUNT: ◈15 ◉2 ○2 | unique evidence objects : 15 | upstream families : 5 (A, B, C, D, E)
LEADS:terminal 8/8 (CLM-101..108) | AXES:terminal 11/12 + 1 PARTIEL (AXS-004, GAP ACCESS) | N/A:—
FAILURES:1 (openedition Anubis) | unresolved gaps : DATA (L-001, L-003, L-004), LITTERATURE (L-002), CONCEPT (L-005), INTENTION (CLM-106)

## PÉRIMÈTRE & LIMITES

- Fresque de synthèse : les faits établis par les 17 investigations parentes (gate PASS) sont repris comme acquis ; seuls les faits nouveaux de la session (FCT-101..113) ont été vérifiés en primaire ici (lecture directe des sources).
- MEMORY != EVIDENCE : les investigations parentes sont des mémoires du corpus ; leurs verdicts ont été réutilisés comme acquis de corpus, pas re-fetchés individuellement.
- AXS-004 (anthropologie) : la source primaire (socio-anthropologie, openedition) est inaccessible (anti-robot Anubis) ; l'axe est PARTIEL, appuyé sur DiPLab et des snippets (Projet Sens, BBC Afrique).
- CLM-106 (intention des leaders) : le mécanisme d'amplification est documenté (SIEPR), l'intention ne l'est pas (BENEFIT != INTENT).
- CLM-108 (version C : l'IA remplace le décideur) : hypothèse non documentée empiriquement, conservée comme telle (BREAK du brainstorm parent).
- Les bornes 4-8 Md€/an et 60-70 Md€ sont des ordres de grandeur (élasticité FIPECO 0,95), pas des prévisions.
- Aucun write-back Mnemolite effectué : les faits FCT-101..113 restent en mem:- (writeback non requis pour une fresque de synthèse sans candidats ✦ nouveaux ; la plupart sont ✧ à source unique).

---

# SYNTHÈSE — LA FRESQUE EN 12 DIMENSIONS

## Le récit dominant : trois étages qui ont intérêt au même scénario

La fresque révèle d'abord une structure : le récit « l'IA va détruire le travail et faire s'effondrer le modèle social » est produit et amplifié par trois étages d'acteurs dont les intérêts convergent sans qu'aucune coordination ne soit démontrée.

**Étage 1, les vendeurs d'IA.** Les laboratoires (OpenAI, Anthropic, Google) investissent 301 milliards de dollars en 2026 (IDC). Le SIEPR de Stanford documente que les craintes d'apocalypse de l'emploi sont « souvent amplifiées par les leaders de l'IA eux-mêmes », citant Dario Amodei. La peur est un argument de vente : elle justifie l'urgence d'adopter, donc la dépense.

**Étage 2, les vendeurs de peur.** Le créateur de la vidéo analysée (71 000 abonnés, Patreon, Discord « trié », club surhumain.ai) monétise l'anxiété des cadres : le diagnostic (asymétrie fiscale réelle) est exact, mais la « solution » vendue (abonnement pour accéder à des « thèses que je ne peux pas défendre publiquement ») reproduit exactement l'asymétrie d'information qu'il dénonce. C'est le pattern « capture de la solution », documenté en 3 cas sur 8 par le brainstorm transverse (IA, cloud, ENR).

**Étage 3, les vendeurs de transformation.** Cabinets de conseil et analystes publient des ROI éclatants (171 % pour les agents, 3,7x pour l'IA générative) alors que l'enquête Writer (2 400 répondants, avril 2026) montre que 75 % des dirigeants admettent que leur stratégie IA est « plus pour la forme » que pour le guidage réel, que 48 % parlent de « déception massive », et que seuls 29 % voient un ROI significatif. Les trois étages vendent le même récit : il faut agir maintenant, ou tout s'effondre.

## Ce qui est vrai (les fondations du récit)

1. **L'asymétrie fiscale est réelle.** Les cotisations sociales frappent le travail (assiette de 1 078 milliards d'euros, produit de 443 milliards) ; un abonnement à une API est une charge déductible sans cotisation. Le coin fiscal français (47,2 %, OCDE) est parmi les plus élevés du monde développé.
2. **La France est structurellement exposée.** Modèle bismarckien, financement social encore dépendant du travail, même si la part des cotisations est passée de 98 % (1980) à 55 % (2025) des ressources des administrations de sécurité sociale.
3. **L'IA frappe les cols blancs et les hauts revenus.** Le rapport Sénat « L'entreprise 5.0 » (Coface/OEM) : 3,8 % de l'emploi fragilisé aujourd'hui, 16,3 % (près de 5 millions de personnes) exposés à l'IA agentique à 2-5 ans ; les 10 % les plus hauts revenus sont menacés à 22,1 %. Les métiers manufacturiers sont protégés : c'est un choc de répartition, pas un effondrement horizontal.
4. **La triple fuite existe.** Cotisations (l'IA ne cotise pas) + import de services (les fournisseurs sont américains) + données (la valeur informationnelle des utilisateurs français n'est pas taxée). Les profits de l'IA sont immatériels donc structurellement délocalisables : Microsoft économise 3,5 milliards de dollars via l'Irlande, Apple y verse 40 % de son impôt mondial, Amazon/Alphabet/Meta/Tesla paient 4,9 % de taux effectif sur 315 milliards de profits.

## Ce qui est faux ou exagéré (les distorsions du récit)

1. **« L'effondrement dans 12-18 mois » n'est compatible avec aucun chiffre.** Les recettes sociales ont progressé de 2,6 % en 2025. Le déficit de 21,6 milliards d'euros est piloté par la dépense (+3,6 %), pas par l'IA. Le « trou » potentiel, même dans un scénario pessimiste, est borné à 4-8 milliards d'euros par an, très inférieur aux 77 milliards d'allègements de cotisations déjà consentis.
2. **« La substitution massive est en cours » n'est pas observée.** 82 % des entreprises françaises n'utilisaient aucune IA en 2024 (Insee). En 2026, 31 % seulement des entreprises exécutent un agent IA en production ; 40 % des projets agentiques sont à risque d'annulation d'ici 2027 (Gartner) ; 25 % des initiatives livrent le ROI attendu (IBM). L'exposition technique (16,3 %) n'est pas une destruction.
3. **« La France est le pays le plus exposé » omet le miroir allemand.** L'Allemagne a un coin fiscal supérieur (47,9 %) et le même modèle bismarckien.
4. **« La taxe IA est infaisable » est exagéré.** La taxe GAFAM existe (0,7 milliard, amendement pour la doubler à 6 %), le Pilier 2 OCDE (15 %) est transposé, l'AI Act encadre les usages d'emploi.
5. **Le cadrage « subvention » est rhétorique.** Ne pas taxer l'IA n'est pas subventionner l'IA : c'est la contrepartie d'un choix de financement de 1945, déjà à moitié corrigé par la CSG depuis 1991.

## Ce qui n'est pas mesuré (les trous dans la raquette)

1. **Le non-remplacement.** La thèse la plus crédible de la vidéo (l'érosion passe par les postes non pourvus, invisibles statistiquement) est plausible mais aucune donnée publique française ne la mesure. C'est le trou central.
2. **Le travail invisible.** 250 000-260 000 micro-travailleurs du clic en France (DiPLab, 2019), 21 euros par mois en moyenne, sans statut : le travail qui entraîne l'IA échappe à l'assiette, aux statistiques et au débat. Si l'IA généralise ce modèle, l'érosion se produira sans aucun licenciement visible.
3. **L'anthropologie.** Ce que devient le sens du travail quand la tâche se fragmente en micro-tâches reste largement non documenté (source primaire inaccessible, enquêtes en cours).

## Les conséquences concrètes (ce qui se passe déjà)

1. **Polarisation du travail.** 92 % des directions cultivent une « élite IA », 60 % prévoient de licencier les non-adoptants, 29 % des salariés sabotent la stratégie IA, 64 % des dirigeants craignent de perdre leur emploi. La fracture n'attend pas la substitution : elle est en train de se creuser en interne.
2. **Contrôle social automatisé.** L'État applique l'IA à ceux qui ont perdu leur emploi : l'algorithme « Ciblage du Contrôle de la Recherche d'Emploi » (France Travail, révélé par La Quadrature du Net et Radio France) profile 6 millions de personnes avec 26 variables, alors que les contrôles passent de 200 000 (2017) à 730 000 (2025), avec un objectif de 1,5 million en 2027. La panique privée (perdre mon emploi) et la mécanique publique (contrôler les sans-emploi) sont les deux faces de la même automatisation.
3. **Performativité.** 75 % des stratégies IA sont « plus pour la forme » : le risque n'est pas l'IA, c'est la stratégie-spectacle qui licencie sans transformation réelle (69 % prévoient des licenciements, 39 % n'ont aucune stratégie de revenus).
4. **Érosion fiscale lente.** Les bornes (4-8 Md€/an) et la délocalisation structurelle des profits dessinent une érosion lente, absorbable sur une décennie, pas un effondrement.
5. **Vide politique.** Aucun rapport parlementaire dédié à « IA et financement de la protection sociale » ; les syndicats demandent l'encadrement sans proposer de taxe IA ; le débat est laissé aux vendeurs.

## Le verdict de la fresque

Le problème « IA et salariat » n'est pas celui que raconte la panique. Il n'y a pas d'effondrement à douze mois : il y a une vulnérabilité structurelle réelle (financement assis sur le travail), une érosion lente et mal mesurée (non-remplacements, micro-travail), une délocalisation massive des profits (paradis de la data), et une polarisation du travail qui s'accélère (élite IA, contrôle social automatisé).

La vraie question n'est pas « l'IA va-t-elle casser la Sécurité sociale ? ». Elle est double. Qui paiera, dans un monde où le travail visible finance tout, pour le travail invisible et l'infrastructure qui font l'IA ? Et qui décidera, quand l'automatisation s'applique non plus aux tâches mais aux décisions ? Sur la première question, les données existent et les leviers aussi (CSG, taxe GAFAM, Pilier 2, conditionnalité des 77 milliards d'allègements). Sur la seconde, le débat n'a même pas commencé : c'est le vrai angle mort que la panique occupe.

---

ENGINE:2.8 | MANIFEST:FINAL | RUN_ID:20260825-0635-ia-salariat-fresque-systemique | PARENT_RUN_ID:20260824-1822-leffondrement-du-modele-salarial | AS_OF:2026-08-25 | INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:NONE
CHECKPOINT_SEQ:0 | LAST_COMPLETED:18b | NEXT_ACTION:NONE | RESUME_COUNT:0
Investigation:IA & salariat — fresque systémique transdisciplinaire | complexity:14→APEX | route overrides:NONE | scope:12 dimensions, France/Europe/US, 2013-2026
modules:SYMBOLS.md,PATTERNS.md,THREATS.md,GATES.md,REQUEST_LOG.md
degraded:NONE | query target/actual:16/16 (dont 1 échec, 1 snippet)

COUNT: ◈15 ◉2 ○2 | unique evidence objects:15 | upstream families:5
LEADS:terminal 8/8 | AXES:terminal 11/12 + PARTIEL 1 | N/A:—
FAILURES:1 (openedition) | unresolved gaps:DATA:3 LITTERATURE:1 CONCEPT:1 INTENTION:1
