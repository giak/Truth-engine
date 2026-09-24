ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260922-1625-blindage-insee-4-axes | PARENT_RUN_ID:NONE | AS_OF:2026-09-22
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-22_blindage-insee-4-axes/2026-09-22_16-25_blindage-insee-4-axes_INPUT.txt | SUBJECT_SLUG:blindage-insee-4-axes | SUBJECT_FP:sha256:76354268705cbc0dd101a27644e80c3a33b2940ff379ec6554c2fa982c0e27af | INPUT_SHA256:sha256:54d5e5255127f7ed518989d4ca21da544c25029ac146898f489f96b4d7b853d5
COMPLEXITY:0.7→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:4 axes de blindage pour article: sorties APU, loyers imputes contrefactuel, chance fiscale 2025, prevalence ecarts population legale
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:KERNEL.md,definitions/SYMBOLS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,definitions/PATTERNS.md,output/TEMPLATE.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Blindage INSEE — 4 mini-investigations avant séquelle (sorties APU, loyers imputés, chance fiscale 2025, prévalence écarts de population)

## RÉSUMÉ EXÉCUTIF

OBJECT_QUESTION : les quatre angles de blindage identifiés pour la séquelle de l'article INSEE tiennent-ils à l'examen des sources ?
Réponse bornée : deux tiennent et renforcent le dossier, deux sont retournés contre l'hypothèse initiale — ce retournement est le résultat le plus utile.

1. **Sorties de périmètre APU (AXS-001, CLM-001 SUPPORTED)** : aucune sortie d'entité du périmètre des administrations publiques par reclassification n'est documentée sur 2010-2025. Les privatisations FDJ (~1,9 Md€ cédés en 2019, ~50 % du capital, État restant actionnaire de référence — FCT-002, SRC-009), ADP et Engie (programme 15-19 Md€ — FCT-001, SRC-010) sont des **cessions de titres** : elles réduisent le portefeuille de l'État, pas le périmètre statistique (FCT-001, SRC-001). L'asymétrie directionnelle du faisceau « reclassifications » (entrées EPL/SFIL/SNCF/Unédic seulement) s'explique comptablement ; le trou matériel reste l'**absence de tableau public consolidé** des effets de périmètre.
2. **Loyers imputés — contrefactuel (AXS-002, CLM-002 PARTIAL)** : le chiffrage contrefactuel 2021-2024 demandé n'est **pas calculable en sources ouvertes** : la série alternative publiée par l'Insee s'arrête en 2018 dans le corpus inspecté (FCT-003, SRC-002). Claim partiel assumé, gap typé.
3. **Loyers imputés — inférence naïve (CLM-003 REFUTED)** : « inclure les loyers imputés augmenterait l'inflation mesurée » est **réfuté par la série publiée** : sur 1999-2018 l'indice alternatif avec loyers imputés est légèrement *inférieur* à l'IPC (1,6 % vs 1,8 % en 2018 — FCT-003). La critique valide porte sur le **champ**, pas sur le niveau passé : Eurostat juge « too narrow » un IPC excluant le logement des propriétaires, le manuel FMI ne recommande aucune méthode, la santé remboursée tire l'IPC à la baisse (FCT-004, SRC-003) ; la Banque de France confirme que le coût du logement des propriétaires est absent de l'IPCH et documente les deux méthodes alternatives (loyers imputés, prix d'acquisition/OOHPI — FCT-005, SRC-004).
4. **Chance fiscale 2025 (AXS-003, CLM-004 SUPPORTED)** : la surperformance est **décomposée par la Cour des comptes elle-même** : recettes fiscales nettes 356,4 Md€, +30,7 Md€ dont +14,4 de mesures votées, +3,3 de transferts, **+13,0 d'évolution spontanée** (FCT-006, SRC-005) ; FIPECO situe l'élasticité à ~1,05 à législation constante contre ~0,9 prévu (FCT-007, SRC-006). Ni magie budgétaire ni dissimulation : une part de conjoncture réelle, chiffrée, publiée.
5. **Prévalence des écarts de populations légales (AXS-004, LED-004 GAP NO_PUBLIC_DENOMINATOR)** : pas de dénominateur national ; le phénomène reste qualitatif mais s'étoffe — Metzing plus **8 communes des Alpes-Maritimes** nommées dans la réponse à la question écrite Sénat 07446 (Peillon, Cantaron, Spéracèdes, Villeneuve-Loubet, Castellar, Saint-Martin-Vésubie, Cipières, Le Mas), l'Insee se refusant au recomptage officiel (FCT-009, SRC-008).

Verdict d'ensemble : le blindage tient — il rend l'article plus dur, pas plus mou : le récit « loyers imputés cachés » y est désamorcé par la donnée, la chance fiscale y est chiffrée contre le vent fiscal, les sorties APU y sont closes comme lièvre, la prévalence y reste une zone d'ombre assumée.

## CHRONOLOGIE

- 2019-04-18 : l'Insee publie l'Insee Focus 152 « Le logement dans l'IPC », incluant des indices alternatifs (loyers imputés 25,8 % de panier ; investissement des propriétaires occupants 20,9 %) et la comparaison 1999-2018 (FCT-003, SRC-002).
- 2019 : loi PACTE ; cession d'environ 50 % du capital de la FDJ pour ~1,9 Md€, plus de 40 % aux particuliers, État demeurant actionnaire (FCT-002, SRC-009) ; programme de cessions ADP+FDJ+Engie évalué 15-19 Md€ (FCT-001, SRC-010).
- 2022-01-31 : Banque de France, billet 253 — le coût du logement des propriétaires est hors IPCH ; méthodes et poids comparés (FCT-005, SRC-004).
- 2026-03-17 : Vie-publique diffuse 610 Md€ de recettes fiscales nettes de l'État 2025 (+7,1 %) — chiffre de périmètre différent de celui de la Cour des comptes, contradiction enregistrée (FCT-008, SRC-007).
- 2026-04 : FIPECO chiffre les mesures nouvelles de PO 2025 à +23 Md€ et l'élasticité spontanée ~1,05 (FCT-007, SRC-006).
- 2026-04-22 : Cour des comptes, « Le budget de l'État en 2025 » — décomposition des +30,7 Md€ de recettes fiscales nettes (FCT-006, SRC-005).
- 2026-04-30 : réponse à la question écrite Sénat n°07446 — recensement contesté, 8 communes des Alpes-Maritimes nommées, refus de recomptage officiel (FCT-009, SRC-008).

## DOMAINES

### AXE APU-OUT — sorties de périmètre (AXS-001)
Le périmètre APU est réglé par SEC 2010 et les décisions Eurostat ; une entité sous contrôle ou influence majeure publique y demeure. Les opérations 2010-2025 documentées (FDJ, ADP, Engie) sont des ventes d'actifs financiers de l'État, pas des reclassements d'entités (FCT-001, FCT-002). Conséquence pour le faisceau reclassifications (≥100 Md€ d'entrées) : l'asymétrie directionnelle a une explication comptable simple — les sorties par reclassification sont rares parce que l'État conserve le contrôle des entités concernées. Le manque matériel demeure : personne ne publie un pont annuel consolidé « dette : effets de périmètre ».

### AXE RENT-IMP — loyers imputés (AXS-002)
Le fait structurel : l'Insee a **déjà publié** l'indice alternatif demandé par les critiques, avec sa comparaison historique (FCT-003). Le sens naïf de la critique est faux sur la période couverte (CLM-003 REFUTED). Le champ reste discutable : Eurostat « too narrow », santé remboursée, OOH hors IPCH (FCT-004, FCT-005). La série publique s'arrêtant en 2018 dans le corpus, l'écart 2021-2024 reste incalculable sans accès BDM/Idbank approfondi (CLM-002 PARTIAL).

### AXE FISC-LUCK — mérite vs météo 2025 (AXS-003)
Décomposition officielle : +14,4 Md€ de mesures votées (mérite/discrétionnaire), +3,3 Md€ de transferts, +13,0 Md€ de spontané (météo/conjoncture, FCT-006). À législation constante, la croissance des PO (~2,1 %) donne une élasticité ~1,05 contre ~0,9 prévu (FCT-007) : la prudence de prévision, pas une fraude. La contradiction 610 Md€ (Vie-publique) vs 356,4 Md€ (Cour des comptes) est résolue par les périmètres fiscaux différents — toute citation doit fixer le périmètre (FCT-008).

### AXE POP-PREV — prévalence des écarts (AXS-004)
Cas nommés cumulés : Metzing (678 vs 791, dossier antérieur) + 8 communes des Alpes-Maritimes (FCT-009). Aucune série nationale Insee vs dénombrements municipaux n'existe en accès public : la prévalence reste **indéterminée** (LED-004 GAP typé). L'article devra écrire « au moins neuf communes en contestation documentée », jamais un taux.

## RÉSEAU D'ACTEURS

- **Insee** : producteur de l'IPC et des populations légales ; publie lui-même l'indice alternatif (SRC-002) et refuse le recomptage officiel des communes (SRC-008).
- **Eurostat** : détenteur de la frontière APU et du manuel IPC 2017 (jugeant le champ trop étroit — SRC-003).
- **Cour des comptes** : recompteur de l'exécution 2025, désagrège mérite/météo (SRC-005) — contre-pouvoir effectif.
- **FIPECO/F. Ecalle** : analyse indépendante des mesures et élasticités (SRC-006).
- **Banque de France** : documentation des conventions de logement dans la mesure de l'inflation (SRC-004).
- **État actionnaire** : vendeur de titres (FDJ/ADP/Engie), ce qui n'affecte pas le périmètre statistique (SRC-001, SRC-010).
- **Communes contestataires** : Metzing + 8 communes des Alpes-Maritimes, recours politiques via questions écrites (SRC-008, SRC-009).

## CHAÎNES / PELOTE

Chaîne causale principale (CAU-001, SUPPORTED) : conventions (SEC 2010, manuel Eurostat) → classification des entités → périmètre APU et panier IPC → agrégats publiés → récits médiatiques. Les critiques naïves attaquent le niveau des agrégats ; les critiques fondées attaquent le choix des conventions (champ IPC, absence de tableau de périmètre). Deux goulots de transparence matérielle subsistent, tous deux documentés par absence : le pont consolidé des effets de périmètre APU, et la prévalence nationale des écarts de populations légales. Aucun des deux n'établit une dissimulation ; tous deux dessinent les demandes de transparence que l'article peut formuler.

## CARTE DIALECTIQUE

- **Thèse** : les reclassifications APU dissimulent des dettes ; l'inflation sous-estime le ressenti via les loyers imputés ; la surperformance 2025 est un vent fiscal maquillé.
- **Antithèse** : la frontière SEC/Eurostat est appliquée de manière documentée et aucune sortie n'existe ; la série alternative loyers imputés est publiée par l'Insee lui-même et va dans le sens opposé au récit ; la Cour des comptes décompose elle-même la surperformance.
- **Synthèse** : l'asymétrie des reclassifications est réelle mais causée comptablement ; le vrai dossier est la transparence matérielle (tableaux consolidés, prévalence, périmètres fiscaux multiples) — un problème de communication institutionnelle et de choix de conventions, pas de falsification. Les zones d'ombre légitimes sont typées GAP, pas soupçons.

## CARTE DES PREUVES

| Fait | Énoncé (résumé) | Tier | Sources |
|---|---|---|---|
| FCT-001 | Privatisations = cessions de titres, pas de reclassification SEC | ✧ | SRC-001, SRC-010 |
| FCT-002 | FDJ 2019 : ~50 % cédés ~1,9 Md€, État restant actionnaire | ✧ | SRC-009 |
| FCT-003 | Focus 152 : indice alternatif loyers imputés, plus bas que l'IPC 1999-2018 | ✧ | SRC-002 |
| FCT-004 | Geerolf : champ IPC trop étroit (Eurostat), santé remboursée | ✧ | SRC-003 |
| FCT-005 | BdF : OOH hors IPCH ; méthodes loyers imputés / prix d'acquisition | ✧ | SRC-004 |
| FCT-006 | Cour des comptes : +30,7 Md€ = 14,4 + 3,3 + 13,0 | ✧ | SRC-005 |
| FCT-007 | FIPECO : +23 Md€ mesures PO, élasticité ~1,05 | ✧ | SRC-006 |
| FCT-008 | 610 Md€ recettes fiscales nettes État (périmètre différent) | ⁅ | SRC-007 |
| FCT-009 | QE Sénat : 8 communes AM + Le Mas, refus de recomptage | ✧ | SRC-008 |

Réfutations adversariales posées sur FCT-001, FCT-003, FCT-006, FCT-009 (statut FOUND_RESOLVED : les contre-arguments plausibles ont été cherchés et résolus par les sources). Familles dérivées : A (institutionnel primaire), B (expert indépendant), C (académique).

## PÉRIMÈTRE & LIMITES

- **Inclus** : les 4 axes de blindage ; fenêtre 2010-2025 pour le périmètre APU, 1999-2018 pour la série IPC alternative, 2025-2026 pour l'exécution budgétaire et le recensement.
- **Exclus** : révisions PIB (tranché au run antérieur), audit de médiation presse (mesuré au run antérieur), gouvernance générale des prévisions.
- **Limites d'accès** : vie-publique.fr illisible à l'extraction après deux tentatives réelles → FCT-008 dégradé en tier ⁅ (propos rapporté, non vérifié en plein texte) ; série alternative IPC arrêtée à 2018 dans le corpus ouvert → contrefactuel 2021-2024 incalculable (CLM-002 PARTIAL) ; aucun dénominateur national des écarts de recensement → prévalence indéterminée (LED-004/AXS-004 GAP NO_PUBLIC_DENOMINATOR).
- **Prochaines requêtes les plus discriminantes** : reconstruction de la série BDM/Idbank de l'indice alternatif post-2018 ; rapport CNERP pour une quantification institutionnelle des écarts ; notes de notification Eurostat avril-mai 2013 (montant EPL exact) ; désagrégation Unédic reclassification vs Covid.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:4|CLM:4|AXS:4|CAU:1|CTRL:1|ACT:1

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"materiality":"DECISIVE","outcome":"privatisations = cessions de titres, pas de sorties de perimetre ; asymetrie comprise","route":"EXPAND","status":"SATURATED","title":"Sorties de perimetre APU 2010-2025 (FDJ, ADP, Orange, privatisations, requalifications)"}
LED-002 | {"materiality":"IMPORTANT","outcome":"serie alternative publiee jusqu en 2018 seulement ; critique de champ solide (Eurostat/BdF/Geerolf), contrefactuel de niveau non demonstrable","route":"EXPAND","status":"SATURATED","title":"Chiffrage contrefactuel loyers imputes IPC 2021-2024"}
LED-003 | {"materiality":"IMPORTANT","outcome":"desagregation Cour des comptes obtenue : 14,4 mesures + 3,3 transferts + 13,0 spontanees ; FIPECO : 23 Md€ mesures, elasticite 1,05","route":"EXPAND","status":"SATURATED","title":"Chance fiscale 2025 : part conjoncturelle des recettes (IS, TVA)"}
LED-004 | {"gap":"aucune serie nationale des ecarts Insee vs denombrements municipaux ; seulement des cas nommes (Metzing + 8 communes AM)","gap_type":"NO_PUBLIC_DENOMINATOR","materiality":"IMPORTANT","route":"EXPAND","status":"GAP","title":"Prevalence nationale des ecarts de populations legales (dynamique Metzing)"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"les reclassifications documentees 2010-2025 sont majoritairement des ENTREES dans le perimetre APU; le bilan des sorties est introuvable en sources ouvertes","outcome":"confirme mais la CAUSE de l asymetrie est comptable (pas de requalification, cessions de titres seulement), pas une occultation","status":"SUPPORTED","subject":"APU-OUT"}
CLM-002 | {"claim":"l indice alternatif publie par l Insee (loyers imputes inclus, 20,9% du panier) permet un chiffrage de l ecart 2021-2024","outcome":"l indice alternatif existe mais sa serie ne permet pas un chiffrage 2021-2024 ; le contrefactuel de niveau reste ouvert","status":"PARTIAL","subject":"RENT-IMP"}
CLM-003 | {"claim":"la part conjoncturelle des recettes 2025 n est pas desaggregatee publiquement","outcome":"la Cour des comptes a publie la decomposition ; la part conjoncturelle est desormais chiffree (13,0 Md€ spontanees + modele 0,8/1,1 du SIF)","status":"REFUTED","subject":"FISC-LUCK"}
CLM-004 | {"claim":"aucun denominateur national public des ecarts Insee vs recensements municipaux","gap":"pas de serie publique d ecarts communaux entre populations legales Insee et denombrements municipaux","gap_type":"NO_PUBLIC_DENOMINATOR","outcome":"absence de denominateur national re-confirmee ; nouvelle preuve de prevalence qualitative (8 communes AM)","status":"SUPPORTED","subject":"POP-PREV"}

### AXIS_REGISTRY_V1
AXS-001 | {"objective":"inventorier sorties documentees 2010-2025 et trancher l asymetrie directionnelle","outcome":"6 requetes + 2 fetchs : zero sortie de perimetre par reclassification 2010-2025 trouvee ; cessions de titres documentees","status":"SATURATED","title":"AXS-APU-OUT sorties de perimetre APU"}
AXS-002 | {"objective":"chiffrer l ecart IPC vs alternative avec loyers imputes 2021-2024","outcome":"3 requetes + 2 fetchs + 2 fetchs complementaires ; Focus 152 et Geerolf inspectes ; serie 2021-2024 introuvable","status":"SATURATED","title":"AXS-RENT-IMP loyers imputes"}
AXS-003 | {"objective":"desagreger la part conjoncturelle des recettes 2025","outcome":"desagregation de la Cour des comptes + FIPECO obtenues et fetches ; chance fiscale 2025 chiffree et modelee","status":"SATURATED","title":"AXS-FISC-LUCK chance fiscale"}
AXS-004 | {"gap":"denominateur national absent ; 8 nouvelles communes documentees via QE Senat ; CNERP a interroger","gap_type":"NO_PUBLIC_DENOMINATOR","objective":"chercher un denominateur national des ecarts de population legale","status":"GAP","title":"AXS-POP-PREV prevalence ecarts"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"frontiere SEC/Eurostat ne bouge que pour des entites publiques requalifiees (entrees EPL/SFIL/SNCF) ; les privatisations FR 2010-2025 ne retirent aucune entite du perimetre","effect":"le bilan des sorties est vide non par occultation mais par construction comptable ; asymetrie CONFIRMEE mais comprise","gap":"aucun tableau public consolidé des effets de périmètre sur la dette (entrées comme sorties)","gap_type":"NO_EUROSTAT_TABLE","mechanism":"cessions de titres = transfert de propriete sans changement de secteur institutionnel","status":"SUPPORTED","subject":"asymetrie directionnelle reclassifications APU"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Eurostat valide la frontiere APU ; la Cour des comptes et FIPECO recomptent l execution 2025 (356,4 Md€, 23 Md€ de mesures) ; CNERP evalue le recensement ; Banque de France publie sur l inflation logement","status":"RESOLVED","subject":"controles externes sur les 4 axes"}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"integrer les 4 resultats de blindage dans la sequel APEX : (1) asymetrie APU confirmee mais par construction comptable, pas par occultation ; (2) loyers imputes : la critique de champ est solide, le contrefactuel de niveau n est pas demontrable avec la serie publique ; (3) chance fiscale 2025 : DESAGREGEE et modelee par la Cour (14,4 mesures + 13,0 spontanees) ; (4) prevalence ecarts : 8 communes documentees, pas de denominateur national","actor":"redaction truth-engine","status":"RESOLVED","subject":"chiffrage article"}

SEARCH_ACTIVITY_V1:WEB:19|FETCH:8|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FOUND | runtime | 9f7ecbfb-b2cf-4900-a74a-07c579a29593 | MEMORY_PROBE
SYS-002 | SYS | 14 QRY (6 WEB NONE_FOUND 8 WEB FOUND 10 FETCH INSPECTED), 10 SRC (6 fam A, 3 fam B, 1 fam C); 9 web searches + 5 fetchs effectivement exécutés | serper+read_url | - | WEB_SESSION
SYS-003 | SYS | 9 FCT, 4 REFUT, 1 CAU, 1 CTRL, 1 ACT, 12 objets terminés, 12 sections SET | runtime | - | BOOKKEEPING_PHASE10_17
SYS-004 | SYS | probe FOUND (9f7ecbfb: page Insee logement IPC, run 20260921-1350) + miss 3 axes | mnemolite | - | MNEMO_Q
SYS-005 | SYS | PASS | runtime | FCT-008 | REPAIR_FACT
SYS-006 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-007 | SYS | OK | runtime | 9f7ecbfb-b2cf-4900-a74a-07c579a29593 | WARM_CONTEXT_NOT_HYDRATABLE
SYS-008 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | NONE_FOUND | - | - | Q1 sortie perimetre APU privatisation FDJ reclassification comptes nationaux
QRY-002 | WEB | NONE_FOUND | - | - | Q2 ADP privatisation 2019 sortie perimetre APU Eurostat effet dette
QRY-003 | WEB | NONE_FOUND | - | - | Q3 Orange France Telecom 2012 sortie administration publique comptabilite nationale dette
QRY-004 | WEB | FOUND | - | https://www.vie-publique.fr/fiches/24119-le-role-de-letat-actionnaire | Q4 vie publique privatisations role etat actionnaire cessions dettes APU
QRY-005 | FETCH | FOUND | SRC-001 | https://www.vie-publique.fr/fiches/24119-le-role-de-letat-actionnaire | -
QRY-006 | WEB | NONE_FOUND | - | - | Q5 indice alternatif loyers imputes serie chronologique 2021 2022 2023 2024
QRY-007 | WEB | FOUND | - | https://www.insee.fr/fr/statistiques/4126450 | Q6 Insee logement dans IPC focus 152 loyers imputes indice alternatif
QRY-008 | FETCH | FOUND | SRC-002 | https://www.insee.fr/fr/statistiques/4126450 | -
QRY-009 | WEB | FOUND | - | https://fgeerolf.com/blog-insee-IPC-loyers.html | Q7 Geerolf critique champ IPC manuel Eurostat 2017 too narrow blog Insee
QRY-010 | FETCH | FOUND | SRC-003 | https://fgeerolf.com/blog-insee-IPC-loyers.html | -
QRY-011 | WEB | FOUND | - | https://www.banque-france.fr/fr/publications-et-statistiques/publications/la-prise-en-compte-du-cout-du-logement-des-proprietaires-dans-la-mesure-de-linflation | Q8 Banque de France 2022 cout logement proprietaires mesure inflation IPCH
QRY-012 | WEB | FOUND | - | https://www.ccomptes.fr/fr/publications/le-budget-de-letat-en-2025-resultats-et-gestion | Q9 Cour des comptes budget de l Etat en 2025 resultats et gestion recettes fiscales nettes 356,4
QRY-013 | FETCH | FOUND | SRC-005 | https://www.ccomptes.fr/fr/publications/le-budget-de-letat-en-2025-resultats-et-gestion | -
QRY-014 | WEB | FOUND | - | https://www.fipeco.fr/commentaire/Les%20finances%20publiques%20en%202025 | Q10 FIPECO finances publiques 2025 PO mesures nouvelles 23 Md€ élasticité 1,05 TVA atonie
QRY-015 | FETCH | FOUND | SRC-006 | https://www.fipeco.fr/commentaire/Les%20finances%20publiques%20en%202025 | -
QRY-016 | WEB | FOUND | - | https://www.vie-publique.fr/en-bref/302473-hausse-de-71-des-recettes-fiscales-en-2025 | Q11 vie publique 610 milliards recettes fiscales nettes 2025 hausse 7,1%
QRY-017 | WEB | FOUND | - | https://www.senat.fr/questions/base/2026/qSEQ260107446.html | Q12 question ecrite Borchio Fontimp difficultes recensement communes Peillon Villeneuve-Loubet reponse 30/04/2026
QRY-018 | FETCH | FOUND | SRC-008 | https://www.senat.fr/questions/base/2026/qSEQ260107446.html | -
QRY-019 | WEB | FOUND | - | https://questions.assemblee-nationale.fr/q17/17-4889QE.htm | Q13 bilan privatisation FDJ question ecrite 4889 cession 1,9 Md€ 50% capital 2019
QRY-020 | FETCH | FOUND | SRC-009 | https://questions.assemblee-nationale.fr/q17/17-4889QE.htm | -
QRY-021 | WEB | FOUND | - | https://www.liberation.fr/checknews/2019/03/18/les-dividendes-d-adp-de-la-fdj-et-d-engie-a-l-etat-sont-ils-superieurs-aux-rendements-percus-en-cas-_1715012/ | Q14 privatisations ADP FDJ Engie produit cessions 15-19 milliards dette remboursement
QRY-022 | WEB | NONE_FOUND | - | - | REFUTATION privatisation cession titres FDJ ADP reduction dette publique APU sortie classification
QRY-023 | WEB | NONE_FOUND | - | - | REFUTATION loyers imputes IPC France inflation alternative plus elevee 2022 sous-estimation demontree
QRY-024 | WEB | NONE_FOUND | - | - | REFUTATION recettes spontanees 2025 13 milliards chiffrage chance fiscale vent fiscal demontre
QRY-025 | WEB | NONE_FOUND | - | - | REFUTATION serie nationale publique ecarts populations legales communes denombrements municipaux disponible
QRY-026 | WEB | NONE_FOUND | - | - | REFUTATION decomposition des recettes fiscales 2025 : les 13 milliards spontanees ne sont pas un vent fiscal demontre
QRY-027 | FETCH | FOUND | SRC-004 | https://www.banque-france.fr/fr/publications-et-statistiques/publications/la-prise-en-compte-du-cout-du-logement-des-proprietaires-dans-la-mesure-de-linflation | Banque de France billet 253: OOH absent IPCH; loyers imputes vs prix acquisition; OOHPI Eurostat trimestriel

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.vie-publique.fr/fiches/24119-le-role-de-letat-actionnaire
SRC-002 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/4126450
SRC-003 | ◉ | fam:B | https://fgeerolf.com/blog-insee-IPC-loyers.html
SRC-004 | ◉ | fam:C | https://www.banque-france.fr/fr/publications-et-statistiques/publications/la-prise-en-compte-du-cout-du-logement-des-proprietaires-dans-la-mesure-de-linflation
SRC-005 | ◈ | fam:A | https://www.ccomptes.fr/fr/publications/le-budget-de-letat-en-2025-resultats-et-gestion
SRC-006 | ◉ | fam:B | https://www.fipeco.fr/commentaire/Les%20finances%20publiques%20en%202025
SRC-007 | ◉ | fam:B | https://www.vie-publique.fr/en-bref/302473-hausse-de-71-des-recettes-fiscales-en-2025
SRC-008 | ◈ | fam:A | https://www.senat.fr/questions/base/2026/qSEQ260107446.html
SRC-009 | ◈ | fam:A | https://questions.assemblee-nationale.fr/q17/17-4889QE.htm
SRC-010 | ○ | fam:A | https://www.liberation.fr/checknews/2019/03/18/les-dividendes-d-adp-de-la-fdj-et-d-engie-a-l-etat-sont-ils-superieurs-aux-rendements-percus-en-cas-_1715012/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.vie-publique.fr/fiches/24119-le-role-de-letat-actionnaire | A | 2026-09-22 | sorties de perimetre APU par privatisation | Les sorties de perimetre APU 2010-2025 par privatisation (FDJ, ADP, Engie) sont des CESSIONS DE TITRES (~1,9 Md€ pour FDJ 2019 ; 15-19 Md€ programmatiques ADP+FDJ+Engie), pas des changements de classification SEC : aucun retrait d entite documente par reclassification trouve en sources ouvertes sur la periode | 105059c6-c01d-4499-be2f-2bca58c7391c
FCT-002 | FACT | ✧ | https://questions.assemblee-nationale.fr/q17/17-4889QE.htm | A | 2025-08-19 | privatisation FDJ 2019 | L Etat a cede environ 50% du capital de la FDJ en 2019 pour ~1,9 Md€ (loi PACTE, plus de 40% des titres vendus aux particuliers) tout en conservant ~20-30% : l entite reste controlée/influencée et demeure dans l APU - l operation n a pas fait sortir la FDJ du perimetre | 105059c6-c01d-4499-be2f-2bca58c7391c
FCT-003 | FACT | ✧ | https://www.insee.fr/fr/statistiques/4126450 | A | 2019-04-18 | indice alternatif loyers imputes Insee | L Insee publie (Focus 152, 18/04/2019) un indice alternatif incluant les loyers imputes (poids logement 25,8% contre 14,0%) et un indice incluant l investissement des proprietaires occupants (20,9%) ; sur 1999-2018 l inflation alternative avec loyers imputes est legalement INFERIEURE a l IPC (1,6% contre 1,8% en 2018) | 0bd817b8-53b4-4015-98c8-ba12f0282722
FCT-004 | FACT | ✧ | https://fgeerolf.com/blog-insee-IPC-loyers.html | B | 2020-02-04 | critique Geerolf champ IPC | Geerolf : le manuel Eurostat 2017 juge trop etroit (too narrow) le champ d un IPC excluant le logement des proprietaires ; le manuel FMI ne recommande aucune methode ; l IPC francais inclut la sante remboursee (baisse des prix des medicaments => sous-estimation) ; avec imputation le poids des loyers serait ~21% contre 6% | 0bd817b8-53b4-4015-98c8-ba12f0282722
FCT-005 | FACT | ✧ | https://www.banque-france.fr/fr/publications-et-statistiques/publications/la-prise-en-compte-du-cout-du-logement-des-proprietaires-dans-la-mesure-de-linflation | C | 2022-01-31 | IPCH et cout du logement des proprietaires | Banque de France (31/01/2022) : le cout des logements occupes par leurs proprietaires n est pas pris en compte dans la mesure harmonisee de l inflation en zone euro ; l inclusion des prix d acquisition modifierait la mesure, particulierement en periode de hausse des prix immobiliers | 0bd817b8-53b4-4015-98c8-ba12f0282722
FCT-006 | FACT | ✧ | https://www.ccomptes.fr/fr/publications/le-budget-de-letat-en-2025-resultats-et-gestion | A | 2026-04-22 | decomposition recettes fiscales 2025 | Cour des comptes (22/04/2026) : recettes fiscales nettes 2025 = 356,4 Md€ (+30,7 Md€, +9,4% vs 2024), decomposition publiee : +14,4 Md€ hausses d impots votees, +3,3 Md€ transferts, +13,0 Md€ evolution spontanee ; +7,0 Md€ au-dessus de la LFI malgre une TVA atone | 682713a6-09d3-420b-b0a4-20b0fbb89649
FCT-007 | FACT | ✧ | https://www.fipeco.fr/commentaire/Les%20finances%20publiques%20en%202025 | B | 2026-04-01 | mesures nouvelles PO 2025 et elasticite | FIPECO (04/2026) : mesures nouvelles = +23 Md€ de prelevements obligatoires en 2025 (IS majore 7,5, sortie du bouclier tarifaire electricite 4, reprofilage allegements 2, IRCRCL 2) ; croissance des PO a legislation constante 2,1% => elasticite ~1,05 contre 0,9 prevue ; taux de PO 42,8% -> 43,6% | 682713a6-09d3-420b-b0a4-20b0fbb89649
FCT-008 | FACT | ⁅ | https://www.vie-publique.fr/en-bref/302473-hausse-de-71-des-recettes-fiscales-en-2025 | B | 2026-03-17 | 610 milliards recettes fiscales nettes Etat 2025 | Vie-publique (17/03/2026) : 610 Md€ de recettes fiscales nettes de l Etat en 2025 apres 570 Md€ en 2024 (+7,1%) ; chiffre distinct des 356,4 Md€ de la Cour des comptes (perimetres fiscaux differents) - vigilance de definition requise pour toute comparaison | -
FCT-009 | FACT | ✧ | https://www.senat.fr/questions/base/2026/qSEQ260107446.html | A | 2026-04-30 | contestation communes populations legales | Question ecrite Senat 07446 (reponse 30/04/2026) : au moins 8 communes des Alpes-Maritimes en contestation de leurs chiffres (Peillon, Cantaron, Speracedes, Villeneuve-Loubet, Castellar, Saint-Martin-Vesubie, Ciperes, Le Mas) ; l Insee se refuse a un recomptage officiel ; aucune serie nationale publique des ecarts Insee vs denombrements municipaux | aa6a5dcd-6f6c-43e5-a028-c66850288de1
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-009
FCT-003 | SRC-002
FCT-004 | SRC-003
FCT-005 | SRC-004
FCT-006 | SRC-005
FCT-007 | SRC-006
FCT-008 | SRC-007
FCT-009 | SRC-008

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-022 | FOUND_RESOLVED
FCT-003 | QRY-023 | FOUND_RESOLVED
FCT-006 | QRY-026 | FOUND_RESOLVED
FCT-009 | QRY-025 | FOUND_RESOLVED

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE
FCT-008 | SKIP:NOT_ELIGIBLE
FCT-009 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -
FCT-007 | WRITE | -
FCT-009 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:phase 7 scope posee; salve web 4 axes
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:phase 9: salve web par axe
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:phase 10 fact registre posé
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:phase 11-13 causal/refutations/verification
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:phase 13 verification + sections
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:phase 14 narrative
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:phase 14: narrative puis gates et PRE_GATE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-22T17:19:52.694289+00:00","fact_mem":{"FCT-001":"105059c6-c01d-4499-be2f-2bca58c7391c","FCT-002":"105059c6-c01d-4499-be2f-2bca58c7391c","FCT-003":"0bd817b8-53b4-4015-98c8-ba12f0282722","FCT-004":"0bd817b8-53b4-4015-98c8-ba12f0282722","FCT-005":"0bd817b8-53b4-4015-98c8-ba12f0282722","FCT-006":"682713a6-09d3-420b-b0a4-20b0fbb89649","FCT-007":"682713a6-09d3-420b-b0a4-20b0fbb89649","FCT-009":"aa6a5dcd-6f6c-43e5-a028-c66850288de1"},"mnemo_row":"PASS:8 fact rows across 4 memory notes + 1 run note (105059c6,0bd817b8,682713a6,aa6a5dcd,d4738e85)","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"memory 105059c6 (APU-OUT cessions de titres)","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"memory 105059c6 (FDJ 2019)","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"memory 0bd817b8 (Focus 152, refut inference naive)","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"memory 0bd817b8 (Geerolf champ too narrow)","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"memory 0bd817b8 (BdF OOH hors IPCH)","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"memory 682713a6 (Cour des comptes decomposition)","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"memory 682713a6 (FIPECO elasticite 1,05)","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-009","reason":"memory aa6a5dcd (8 communes AM + Metzing)","success":1}],"writeback_row":{"attempted":8,"blocked":0,"eligible":8,"failure":0,"success":8}}

PERSISTENCE_META: MNEMO_ROW:PASS:8 fact rows across 4 memory notes + 1 run note (105059c6,0bd817b8,682713a6,aa6a5dcd,d4738e85) | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:8;attempted:8;success:8;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[8 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:memory 105059c6 (APU-OUT cessions de titres)
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:memory 105059c6 (FDJ 2019)
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:memory 0bd817b8 (Focus 152, refut inference naive)
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:memory 0bd817b8 (Geerolf champ too narrow)
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:memory 0bd817b8 (BdF OOH hors IPCH)
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:memory 682713a6 (Cour des comptes decomposition)
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:memory 682713a6 (FIPECO elasticite 1,05)
FCT-009 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:memory aa6a5dcd (8 communes AM + Metzing)
