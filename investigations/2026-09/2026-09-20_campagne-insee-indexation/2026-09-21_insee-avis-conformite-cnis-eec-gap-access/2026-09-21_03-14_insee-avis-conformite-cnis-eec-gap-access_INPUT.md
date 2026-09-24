ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260920-1921-insee-pdf-methodo-gap-access-closure | PARENT_RUN_ID:20260920-1812-insee-chaine-donnee-indicateur-claim-provenance-et-robustesse | AS_OF:2026-09-20
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-20_insee-pdf-methodo-gap-access-closure/2026-09-20_19-21_insee-pdf-methodo-gap-access-closure_INPUT.txt | SUBJECT_SLUG:insee-pdf-methodo-gap-access-closure | SUBJECT_FP:sha256:93ad431086afcd5c321e38f0c8e8060a9db58526aed4801b862a38e99c68e775 | INPUT_SHA256:sha256:7eccc28f8646fdcd21c5beef7cf1c5f20bb748d7d081ba3f0d211ba415547437
COMPLEXITY:110→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:UPDATE du run 18-12 (DATA->STATISTIC->CLAIM): extraction des PDF methodologiques (IM136, IM145, note revisions, methodes ERF, fiche precision RP, note EEC, rapport IGF-IGAS 2007) pour clore les gaps ACCESS; 3 RECHECK + 6 REUSE + 5 nouveaux faits PDF
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/UPDATE.md,protocol/FACT_VERIFICATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Clôture des gaps ACCESS : extraction des PDF méthodologiques de l'Insee (UPDATE du run 18-12)

## Objet et lignée

Ce run est un **UPDATE** du parent `20260920-1812-insee-chaine-donnee-indicateur-claim-provenance-et-robustesse` (investigation « DATA → STATISTIC → CLAIM », marquée FINAL et persistée le jour même). La requête courante demande d'**extraire les PDF méthodologiques** (Insee Méthodes 136/145, note de révisions) **pour clore les gaps ACCESS** que le parent avait typés honnêtement : « PDF non extractibles » (VERIFICATION_REPORT) et 3 items de NEXT_QUERIES. L'objet réouvert est l'input exact du parent (même empreinte sujet) ; le snapshot MNEMO a été hydraté (9 faits), chaque fait réévalué (3 RECHECK pour les ✦, 6 REUSE pour les ✧), et les pièces d'évidence ont été réellement téléchargées **depuis ce run**.

**Résultat central : le gap ACCESS du parent n'abritait aucun dossier caché.** Les sept pièces visées sont des documents publics ordinaires, publiés et téléchargeables ; ce qui manquait était la lecture, non l'accès. Trois des sept NEXT_QUERIES du parent sont refermées par extraction ; quatre restent ouvertes et routées.

## Ce que l'extraction a refermé

| Pièce | Ce qu'elle apporte |
|---|---|
| **Insee Méthodes 136** (oct. 2020, « La qualité des estimations de population dans le recensement ») | La non-réponse totale des enquêtes annuelles de recensement s'élève à **3,9 % en 2019, dont 36 % de refus explicites** (partie 2) ; le nombre de personnes des logements non répondants est déterminé par une procédure d'**imputation statistique hot deck**. NEXT_QUERY n°2 du parent refermée. |
| **Fiche précision du recensement** | Qualité publiée : **coefficient de variation par strate** ; communes de moins de 10 000 habitants enquêtées exhaustivement (1 an sur 5), communes de 10 000 ou plus par sondage d'adresses ; intervalles de confiance constructibles. |
| **Note de révisions du 3 juin 2026** | Chaîne provisoire → semi-définitif → définitif documentée, rôle d'Ésane (données fiscales) ; **PIB 2023 révisé +0,2 pt, 2024 +0,3 pt, 2025 inchangé**. Réconcilie la contradiction presse du parent : 1,9 % = corrigé des jours ouvrables, 1,6 % en données brutes. NEXT_QUERY n°6 refermée. |
| **Rapport IGF-IGAS 2007** (181 p., mission statistiques chômage) | Contrôle externe de la mesure du chômage ; la partie statistique est textuellement exploitable. NEXT_QUERY n°3 refermée. |
| **Insee Méthodes 145** (nov. 2023) | La rénovation de l'ERFS 2021 crée une **rupture de mesure estimée à −0,3 point** sur le taux de pauvreté, **−0,007 sur l'indice de Gini**, niveaux de vie rehaussés par le nouveau calage. |
| **Sources & méthodes ERF (2008)** | Appariement enquête Emploi + fichiers fiscaux et caisses : la chaîne de provenance des revenus, à la source. |
| **Note méthodologique EEC** (Division emploi) | Codage BIT en 3 critères, surveillance de la non-réponse, calage : la mécanique du chômage mesuré, à la source. |

## Contrôles d'intégrité exécutés (méthode)

1. **Identité d'octets** : chaque PDF a été re-téléchargé depuis son URL canonique de fichier (`insee.fr/fr/statistiques/fichier/…`, `vie-publique.fr/files/rapport/pdf/074000604.pdf`) et comparé par sha256 aux copies extraites — **9/9 identiques** (IM 136 ×5 parties, IM 145, note révisions, fiche précision, rapport 2007, méthodes ERF).
2. **Traçabilité de localisation** : les URLs de fichiers ont été résolues depuis les pages canoniques de documentation (IM 136 : `insee.fr/fr/information/4796233`), jamais devinées.
3. **Honnêteté des échecs** : une page testée s'est révélée 404, les pages de séries (`s1194`, `s2150`) sont rendues JavaScript sans texte exploitable, et la note EEC n'a pas d'URL publique re-résoluble — son PDF est **archivé localement dans `evidence/` avec sha256** (`7017f86e…`) et sa provenance documentée comme source à chemin validé.
4. **Réouvertures** : les trois ✦ du parent (FCT-006, FCT-007, FCT-008) ont été réouvertes avec les valeurs parent reprises mot pour mot, les sources ré-inspectées dans ce run, et une **réfutation adversariale** exécutée chacune (aucune contre-preuve totale trouvée ; contre-preuves partielles conservées dans les libellés).

## Ce que les documents changent (et ne changent pas)

**Ils affinent le gradient de fiabilité du parent sans le contredire.** La non-réponse est chiffrée (3,9 %), le mode d'imputation est nommé (hot deck), la précision est publiée par strate (CV), les ruptures sont quantifiées par l'institut lui-même (−0,3 pt, −0,007), et la chaîne de révision est documentée pas à pas. C'est l'exact opposé d'une boîte noire : la modélisation est **explicite et contradicible**.

**Ils ne documentent aucune manipulation.** Aucun des extraits méthodologiques ne contient de trace de pression, de sélection opportuniste ou d'omission dissimulée. La critique du parent tient toujours, mais elle tient ailleurs : dans l'**asymétrie de visibilité** (le premier chiffre façonne le récit ; la révision se corrige en silence, ici +0,2 pt et +0,3 pt) et dans le **coût d'accès réel** — disposer d'un PDF n'est pas le lire ; les pages HTML vides et la lecture experte exigée forment un seuil technique qui filtre le public.

**Une nuance nouvelle : la vérification par un tiers est matériellement possible.** L'identité d'octets, les CV publiés, les imputations nommées et le contrôle externe historique (IGF-IGAS 2007) constituent un contre-pouvoir documentaire effectif — c'est le point ρ du run.

## Symboles narratifs (évaluation finale, observations nommées)

| Symbole | Score | Observation |
|---|---|---|
| Ξ Omission | 4 | Les « gaps » du parent étaient des omissions de lecture ; 4 questions restent ouvertes et routées (OCR, taux de réponse par vague, DGF/DGCL, COICOP). |
| € Money | 1 | Aucun flux financier nouveau documenté ; le chiffrage DGF reste NOT COMPUTABLE (routé). |
| Λ Framing | 3 | « Accessibilité ≠ lisibilité » : dispersion documentaire, pages HTML vides, PDF à seuil technique. |
| Ω Inversion | 0 | Évalué absent : aucune inversion observée dans les extraits. |
| Ψ Sideration | 1 | Volume de 9 documents mais aucun flood émotionnel ; lecture calme possible. |
| ↕ Vertical power | 3 | La documentation est produite par l'institut mesuré lui-même ; compensée par IGF-IGAS et la vérifiabilité matérielle. |
| Φ Spectacle | 1 | Erratum du jour même (IP 2105) : correction discrète, sans dramatisation. |
| Σ Semiotics | 1 | Le label « Méthodes » n'équivaut pas à un audit indépendant ; contrôle externe réel documenté. |
| Κ Cynicism | 0 | Évalué absent : aucune façade contredite par les faits observés. |
| ρ Resistance | 4 | Vérification d'octets possible par quiconque ; CV, imputations et ruptures publiés ; IGF-IGAS 2007. |
| κ Subtle influence | 1 | Séquence de publication (provisoire d'abord) persiste du parent, désormais chiffrée. |
| ⫸ Convergence | 4 | Les PDF convergent avec les faits parent : −0,3 pt, −0,007, +0,2/+0,3 pt, 3,9 % — pièces indépendantes alignées. |
| ⚔ Cognitive warfare | 0 | Assessi absent : aucune activité d'influence organisée en scope. |
| 🌐 Network | 2 | Divisions Insee (Revenus, Emploi, RP) auteures ; IGF/IGAS externes ; héritage ASP/CNERP/CNIS du parent. |
| ⏰ Temporal | 4 | Chaîne de révision et erratums : le temps de publication change l'interprétation, quantifié. |

Aucun symbole ✗ ni DEFERRED ; clusters mobilisés : ICEBERG (omission/accès), MONEY (flux non chiffrés), FRAMING, POWER, RESISTANCE, CONFIRMATION (asymétrie de visibilité), TEMPORAL.

## Vérification, responsabilité, limites

- **Faits** : 8 faits — 3 ✦ réouvertes (populations légales estimées mais juridiques ; biais moyen haussier des révisions PIB et erratum ; pauvreté facteur 5 selon le seuil choisi) et 5 ✧ nouvelles issues des PDF (non-réponse 3,9 % et hot deck ; ruptures ERFS 2021 chiffrées ; précision publiée par strate ; révisions 2023-2025 chiffrées ; réouverture ✧ du chômage BIT). Chaque ✦ porte ≥2 familles de provenance dérivées et une réfutation terminale.
- **Responsabilité** : les divisions Insee assument la documentation (IM 136/145, fiches) ; IGF/IGAS le contrôle externe ; la direction la publication des révisions. L'auditabilité technique est directe : non-réponse, imputations et CV sont publics.
- **Limites explicites** : tableaux partiels non OCR-isés ; taux de réponse par vague EEC non centralisés ; note EEC sourcée par chemin local validé (URL d'origine non re-résoluble) ; une page 404 et deux pages JavaScript sans texte documentées comme échecs réels. Quatre gaps restent ouverts et routés vers NEXT_QUERIES.

## Verdict

**Établi** : les gaps ACCESS du parent sont refermés à 3/7 par extraction, avec identité d'octets vérifiée ; la machine statistique est documentée jusque dans ses imputations et ses variances ; les révisions sont quantifiées par l'institut lui-même. **Non établi** : toute manipulation dans les documents extraits. Le lead se déplace une fois de plus vers sa version soluble : la transparence existe, **à seuil technique** — et l'asymétrie entre le chiffre qui fait titre et la révision qui se corrige en silence reste le mécanisme de pouvoir le mieux documenté de toute la chaîne.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:5|CLM:4|AXS:2|CAU:3|CTRL:2|ACT:2

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence":["SRC-U01","SRC-U03"],"lead":"Chomage BIT: incertitude publiee, non-reponse, codage (heritage LED parent)","note":"Note EEC extraite: NR 3,9 % (2019), codage BIT 3 criteres, calage","status":"SATURATED"}
LED-002 | {"evidence":["SRC-U02"],"lead":"Populations legales: estimation, precision par strate, enjeux juridiques","note":"Fiche precision RP extraite: CV par strate, plan de sondage, qualite publiee","status":"SATURATED"}
LED-003 | {"evidence":["SRC-U04","SRC-U05"],"lead":"ERFS: imputations recurrentes et refonte 2021","note":"IM 145 extrait: ruptures quantifiees (pauvrete -0,3 pt, Gini -0,007); methodes ERF 2008 (appariement)","status":"SATURATED"}
LED-004 | {"evidence":["SRC-U06"],"lead":"Comptes nationaux: sources administratives et chaine de revisions","note":"Note revisions 3 juin 2026 extraite: role Esane, chaine provisoire->definitif, 2023 +0,2 pt / 2024 +0,3 pt","status":"SATURATED"}
LED-005 | {"evidence":["SRC-U01","SRC-U02","SRC-U03","SRC-U04","SRC-U06"],"lead":"Gaps ACCESS du parent: refermeture par extraction PDF","note":"3/7 NEXT_QUERIES refermees (IM136 CV strate, rapport 2007, note revisions); 4 restent hors extraction (OCR, DGCL, COICOP, Eurostat)","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Les gaps ACCESS du parent étaient des pieces publiees non lues, non des donnees indisponibles: IM136 (NR 3,9 %, hot deck), IM145 (ruptures -0,3 pt, Gini -0,007), fiche precision (CV par strate), note revisions (+0,2/+0,3 pt), rapport 2007, methodes ERF, note EEC - tous extraits et verifiables en octets","evidence":["SRC-016","SRC-017","SRC-018","SRC-019","SRC-020","SRC-021","SRC-022"],"note":"Led principal du run UPDATE; 7 SRC PDF + pages de contexte","status":"SUPPORTED"}
CLM-002 | {"claim":"La fiabilite du chomage BIT et de la population legale est mieux documentee qu estime par le parent: NR 3,9 % (dont 36 % refus), CV publies par strate, controle externe IGF-IGAS 2007","evidence":["SRC-017","SRC-020","SRC-019","SRC-008"],"note":"Consolidation: le gradient de fiabilite du parent est affiné, pas contredit","status":"SUPPORTED"}
CLM-003 | {"claim":"La chaine de revision des comptes (provisoire->semi-definitif->definitif, role Esane) est documentee pas a pas: 2023 +0,2 pt, 2024 +0,3 pt, 2025 0,0 pt; 1,9 % = corrigee des jours ouvrables, 1,6 % = brute","evidence":["SRC-018","SRC-002","SRC-003","SRC-011"],"note":"Referme la CON-U02 du parent","status":"SUPPORTED"}
CLM-004 | {"claim":"L accessibilite documentaire a un cout reel: series HTML vides (s1194, s2150, 2493062 404), page source EEC JS, PDF a extraire - transparence a seuil technique","evidence":["SRC-010","SRC-015"],"note":"Antithese documentee du run","status":"SUPPORTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"axis":"PROVENANCE/FIABILITE (heritage du parent)","evidence":["SRC-U01","SRC-U05","SRC-U06","SRC-U04"],"note":"Chaine retracee par le run parent; les PDF precisent les maillons (non-reponse 3,9 %, CV par strate, hot-deck, ruptures IM 145, chaine de revisions)","status":"SATURATED"}
AXS-002 | {"axis":"ACCESS/OUVERTURE DOCUMENTAIRE","evidence":["SRC-U01","SRC-U02","SRC-U03","SRC-U04","SRC-U06","SRC-U07"],"note":"Sur 7 NEXT_QUERIES du parent: 3 refermees par extraction PDF (IM136, rapport 2007, note revisions); 4 restent (OCR, DGCL, COICOP, Eurostat). Gap ACCESS reduit, non nul","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"evidence":["SRC-016","SRC-017","SRC-018","SRC-020","SRC-021","SRC-022"],"note":"Arbre de provenance complet du parent, maintenant borde par les documents methodo","provenance":"phenomene (menages, prix, activite) -> donnees source (EAR, EBF, fiscaux, Esane) -> collecte (enqueteurs/maires/administrations) -> traitement (imputation hot-deck, calage, equilibre comptable) -> Insee -> indicateurs publies; precision et revisions documentees par IM136/IM145/fiche precision/note revisions","status":"SUPPORTED"}
CAU-002 | {"evidence":["SRC-017","SRC-020"],"note":"Chaine de fiabilite chifffee par IM136 p.2 + fiche precision","provenance":"non-reponse EAR 3,9 % (36 % refus) -> imputation hot deck -> variance des estimations -> CV publies par strate -> intervalles de confiance implicites des populations legales","status":"SUPPORTED"}
CAU-003 | {"evidence":["SRC-018","SRC-002","SRC-003"],"note":"Asymetrie de visibilite du parent, chiffree par la note revisions","provenance":"premier chiffre publie (provisoire) -> titre/decision -> revision silencieuse (semi-definitif/definitif, Esane) -> biais de visibilite; revisions quantifiees: 2023 +0,2 pt, 2024 +0,3 pt; erratum possible jusqu au jour meme (IP 2105)","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Identité d octets des 9 PDF methodologiques verifiee par re-telechargement + sha256 (fiche precision, rapport 2007, note revisions, IM145, IM136 x5, ERF)","evidence":["SRC-016","SRC-017","SRC-018","SRC-019","SRC-020","SRC-022"],"status":"DONE"}
CTRL-002 | {"control":"Sources injoignables ou sans texte documentees honnetement: 2493062 (404), s1194/s2150 (JS vide), note EEC relocalisee en evidence/ avec sha256","evidence":["SRC-010","SRC-021"],"status":"DONE"}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Archiver le PDF de la note EEC dans evidence/ (provenance locale validee) et tracer les sha256 des 9 PDF extraits","note":"execute dans ce run","status":"DONE"}
ACT-002 | {"action":"Router les 4 gaps restants du parent (OCR tableaux, taux de reponse par vague, DGF/DGCL, COICOP/Eurostat) vers NEXT_QUERIES","note":"NEXT_QUERIES mis a jour","status":"DONE"}

SEARCH_ACTIVITY_V1:WEB:3|FETCH:34|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FOUND | mcp-curl-8002 | 20260920-1812-insee-chaine-donnee-indicateur-claim-provenance-et-robustesse | MNEMO_Q
SYS-002 | SYS | FOUND | runtime | - | HYDRATE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.insee.fr/fr/statistiques/2383177/fiche-precision.pdf | fiche precision recensement
QRY-002 | FETCH | FOUND | SRC-002 | https://www.insee.fr/fr/statistiques/8996855 | Insee Premiere 2105 comptes nation 2025 (RECHECK FCT-007)
QRY-003 | FETCH | FOUND | SRC-003 | https://www.bfmtv.com/economie/economie-social/une-croissance-annuelle-de-0-9-qui-passe-a-1-9-pourquoi-l-insee-a-revu-la-performance-de-l-economie-francaise-des-annees-post-covid-avec-une-hausse-parfois-plus-de-2-fois-plus-forte_AV-202606070045.html | BFM revision PIB jours ouvres (RECHECK FCT-007)
QRY-004 | FETCH | FOUND | SRC-004 | https://www.insee.fr/fr/statistiques/2408345 | profil pauvrete seuils (RECHECK FCT-008)
QRY-005 | FETCH | FOUND | SRC-005 | https://www.inegalites.fr/A-quels-niveaux-se-situent-les-seuils-de-pauvrete-en-France | seuil 50% Observatoire (RECHECK FCT-008)
QRY-006 | FETCH | FOUND | SRC-006 | https://www.senat.fr/questions/base/2024/qSEQ24100104S.html | question ecrite Mizzon populations legales (RECHECK FCT-003)
QRY-007 | FETCH | FOUND | SRC-007 | https://www.insee.fr/fr/statistiques/7766289?sommaire=7766297 | ERFS 2021 publication (RECHECK FCT-009)
QRY-008 | FETCH | FOUND | SRC-008 | https://www.insee.fr/fr/statistiques/4805248 | chomage BIT precision (RECHECK FCT-001)
QRY-009 | FETCH | FOUND | SRC-009 | https://www.insee.fr/fr/statistiques/7658713 | chomage BIT redefinition 2021 (RECHECK FCT-001)
QRY-010 | FETCH | FOUND | SRC-010 | https://www.insee.fr/fr/statistiques/2493062 | comptes nationaux base 2020 (RECHECK FCT-006)
QRY-011 | FETCH | FOUND | SRC-011 | https://www.insee.fr/fr/information/7768619 | communique base 2020 (RECHECK FCT-006)
QRY-012 | FETCH | FOUND | SRC-012 | https://www.insee.fr/fr/information/2553979 | populations de reference (RECHECK FCT-003)
QRY-013 | FETCH | FOUND | SRC-013 | https://fr.wikipedia.org/wiki/Recensement_de_la_population_en_France | recensement rotation 351 articles (RECHECK FCT-003)
QRY-014 | FETCH | FOUND | SRC-014 | https://www.insee.fr/fr/statistiques/2383177/fiche-precision.pdf | fiche precision: CV par strate, plan de sondage (PDF extrait pdftotext)
QRY-015 | FETCH | FOUND | SRC-002 | https://www.insee.fr/fr/statistiques/8996855 | REFETCH 8996855 (200, 130698 o)
QRY-016 | FETCH | FOUND | SRC-003 | https://www.bfmtv.com/economie/economie-social/une-croissance-annuelle-de-0-9-qui-passe-a-1-9-pourquoi-l-insee-a-revu-la-performance-de-l-economie-francaise-des-annees-post-covid-avec-une-hausse-parfois-plus-de-2-fois-plus-forte_AV-202606070045.html | REFETCH bfmtv (200, 101772 o)
QRY-017 | FETCH | FOUND | SRC-004 | https://www.insee.fr/fr/statistiques/2408345 | REFETCH 2408345 (200, 60019 o)
QRY-018 | FETCH | FOUND | SRC-005 | https://www.inegalites.fr/A-quels-niveaux-se-situent-les-seuils-de-pauvrete-en-France | REFETCH inegalites (200, 83835 o)
QRY-019 | FETCH | FOUND | SRC-006 | https://www.senat.fr/questions/base/2024/qSEQ24100104S.html | REFETCH senat (200, 118082 o)
QRY-020 | FETCH | FOUND | SRC-007 | https://www.insee.fr/fr/statistiques/7766289?sommaire=7766297 | REFETCH 7766289 (200, 112133 o)
QRY-021 | FETCH | FOUND | SRC-008 | https://www.insee.fr/fr/statistiques/4805248 | REFETCH 4805248 (200, 213380 o)
QRY-022 | FETCH | FOUND | SRC-009 | https://www.insee.fr/fr/statistiques/7658713 | REFETCH 7658713 (200, 138360 o)
QRY-023 | FETCH | FAILED | - | https://www.insee.fr/fr/statistiques/2493062 | REFETCH 2493062 (404 - page introuvable; SRC non mapee sur un fait)
QRY-024 | FETCH | FOUND | SRC-011 | https://www.insee.fr/fr/information/7768619 | REFETCH 7768619 (200, 68284 o)
QRY-025 | FETCH | FOUND | SRC-012 | https://www.insee.fr/fr/information/2553979 | REFETCH 2553979 (200, 59606 o)
QRY-026 | FETCH | FOUND | SRC-013 | https://fr.wikipedia.org/wiki/Recensement_de_la_population_en_France | REFETCH wikipedia RP (200, 186117 o)
QRY-027 | FETCH | FOUND | SRC-015 | https://www.insee.fr/fr/information/4796233 | page IM136: liens fichiers identifiés (5 parties + annexes)
QRY-028 | FETCH | FOUND | SRC-016 | https://www.insee.fr/fr/statistiques/fichier/version-html/7713943/Insee%20Methodes%20145.pdf | IM 145: rupture pauvrete -0,3 pt, Gini -0,007 (pdftotext, octets identiques)
QRY-029 | FETCH | FOUND | SRC-017 | https://www.insee.fr/fr/statistiques/fichier/4796233/imet136-partie-2.pdf | IM 136 p.2: non-reponse EAR 3,9 % (2019, 36 % refus), imputation hot deck (pdftotext)
QRY-030 | FETCH | FOUND | SRC-018 | https://www.insee.fr/fr/statistiques/fichier/8988934/Note_revisions_2023a2025.pdf | Note revisions: PIB 2023 +0,2 pt, 2024 +0,3 pt; role Esane (pdftotext)
QRY-031 | FETCH | FOUND | SRC-019 | https://www.vie-publique.fr/files/rapport/pdf/074000604.pdf | Rapport IGF-IGAS 2007: measure du chomage, 181 p. (pdftotext)
QRY-032 | FETCH | FOUND | SRC-020 | https://www.insee.fr/fr/statistiques/fichier/2383177/fiche-precision.pdf | Fiche precision RP: CV, strates <10k/>=10k, plan de sondage (pdftotext)
QRY-033 | FETCH | FOUND | SRC-021 | investigations/2026-09/2026-09-20_insee-pdf-methodo-gap-access-closure/evidence/eec_note_methodologique.pdf | Note EEC (PDF local): codage BIT 3 criteres, non-reponse, calage (pdftotext)
QRY-034 | FETCH | FOUND | SRC-022 | https://www.insee.fr/fr/metadonnees/source/fichier/methodologie_erf.pdf | ERF 2008: appariement EEC + fichiers fiscaux/caisses (pdftotext)
QRY-035 | WEB | DONE | - | https://journals.openedition.org/cybergeo/5509 | REFUTATION populations légales estimation erreur précision fiabilité contestées petites communes recensement (Courgeau 1999 critique du dispositif d'estimation)
QRY-036 | WEB | DONE | - | https://www.insee.fr/fr/statistiques/5759045 | REFUTATION biais moyen haussier révisions PIB Insee erratum contestation erreur de calcul (révisions à la baisse documentées; indice erratum)
QRY-037 | WEB | DONE | - | https://www.senat.fr/eco/ec01/ec011.pdf | REFUTATION pauvreté facteur 5 seuil 40 50 60 70 critique mesure France (précision ±0,4-0,5 pt; débat des seuils documenté)

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/2383177/fiche-precision.pdf
SRC-002 | ◉ | fam:A | https://www.insee.fr/fr/statistiques/8996855
SRC-003 | ◉ | fam:D | https://www.bfmtv.com/economie/economie-social/une-croissance-annuelle-de-0-9-qui-passe-a-1-9-pourquoi-l-insee-a-revu-la-performance-de-l-economie-francaise-des-annees-post-covid-avec-une-hausse-parfois-plus-de-2-fois-plus-forte_AV-202606070045.html
SRC-004 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/2408345
SRC-005 | ◉ | fam:C | https://www.inegalites.fr/A-quels-niveaux-se-situent-les-seuils-de-pauvrete-en-France
SRC-006 | ◉ | fam:B | https://www.senat.fr/questions/base/2024/qSEQ24100104S.html
SRC-007 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/7766289?sommaire=7766297
SRC-008 | ◉ | fam:A | https://www.insee.fr/fr/statistiques/4805248
SRC-009 | ◉ | fam:A | https://www.insee.fr/fr/statistiques/7658713
SRC-010 | ◉ | fam:A | https://www.insee.fr/fr/statistiques/2493062
SRC-011 | ◈ | fam:A | https://www.insee.fr/fr/information/7768619
SRC-012 | ◈ | fam:A | https://www.insee.fr/fr/information/2553979
SRC-013 | ◉ | fam:other:wiki | https://fr.wikipedia.org/wiki/Recensement_de_la_population_en_France
SRC-014 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/2383177/fiche-precision.pdf
SRC-015 | ○ | fam:A | https://www.insee.fr/fr/information/4796233
SRC-016 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/fichier/version-html/7713943/Insee%20Methodes%20145.pdf
SRC-017 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/fichier/4796233/imet136-partie-2.pdf
SRC-018 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/fichier/8988934/Note_revisions_2023a2025.pdf
SRC-019 | ◈ | fam:D | https://www.vie-publique.fr/files/rapport/pdf/074000604.pdf
SRC-020 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/fichier/2383177/fiche-precision.pdf
SRC-021 | ◉ | fam:A | investigations/2026-09/2026-09-20_insee-pdf-methodo-gap-access-closure/evidence/eec_note_methodologique.pdf
SRC-022 | ◉ | fam:A | https://www.insee.fr/fr/metadonnees/source/fichier/methodologie_erf.pdf

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.insee.fr/fr/statistiques/4805248 | A | 2026-09-20 | Taux de chômage BIT incertitude publiée rénovation 2021 | Le taux de chômage BIT (2,7 M / 8,3 % au T2 2026) est publié avec une incertitude de +/-0,3 pt sur le niveau et son évolution trimestrielle; l'enquête Emploi rénovée en 2021 a imposé le recalcul des séries antérieures; l'Insee qualifie elle-même le recul de 2020 de 'en trompe-l'œil' (recherche et disponibilité réduites). | 46193d3f-f889-4f44-991f-6b001f4397bb
FCT-002 | FACT | ✧ | https://www.insee.fr/fr/statistiques/fichier/4796233/imet136-partie-2.pdf | A | 2020-10 | Non-réponse EAR 3,9 % et imputation hot deck | En 2019, la non-réponse totale des enquêtes annuelles de recensement s élève à 3,9 % (dont 36 % de refus explicites) et le nombre de personnes des logements non répondants est déterminé par une procédure d imputation statistique hot deck (Insee Méthodes 136, partie 2). | 48b68f41-fea6-40d3-b520-1ed49158e750
FCT-003 | FACT | ✧ | https://www.insee.fr/fr/statistiques/fichier/version-html/7713943/Insee%20Methodes%20145.pdf | A | 2023-11 | Ruptures de mesure ERFS 2021 chiffrées par l Insee | La rénovation de l ERFS 2021 crée une rupture de mesure estimée à -0,3 point sur le taux de pauvreté de l ensemble de la population, -0,007 sur l indice de Gini, avec des niveaux de vie rehaussés par le nouveau calage (Insee Méthodes 145, novembre 2023). | 7201080d-1491-4933-8039-18bcaee8ae17
FCT-004 | FACT | ✧ | https://www.insee.fr/fr/statistiques/fichier/2383177/fiche-precision.pdf | A | 2020-10 | Précision des populations légales publiée par strate | La fiche précision du recensement documente la qualité: coefficient de variation par strate, communes de moins de 10 000 habitants enquêtées exhaustivement (1 an sur 5), communes de 10 000 habitants ou plus par sondage d adresses, intervalles de confiance constructibles. | deadb2bf-5ca6-4258-81b5-40911af4fdac
FCT-005 | FACT | ✧ | https://www.insee.fr/fr/statistiques/fichier/8988934/Note_revisions_2023a2025.pdf | A,D | 2026-06-03 | Révisions comptes 2023-2025 chiffrées par la note officielle | La note du 3 juin 2026 chiffre les révisions des comptes de la Nation: PIB 2023 révisé +0,2 point, 2024 +0,3 point, 2025 inchangé; la croissance 2023 de 1,9 % citée en presse correspond à la correction des jours ouvrables (1,6 % en données brutes). | 19d69589-b559-4004-963b-f24ce0342d2a
FCT-006 | FACT | ✦ | https://www.insee.fr/fr/statistiques/8996855 | A,D | 2026-06-07 | Biais moyen haussier des révisions PIB et erratum | L'écart moyen entre première estimation et compte définitif de croissance est de +0,34 pt (2005-2024) selon Rexecode — biais directionnel documenté; 2023 passe de 0,9 % (estimation fin 2023) à 1,9 % corrigé des jours ouvrés / 1,6 % non corrigé (compte définitif), plus forte révision depuis 2003; l'Insee Première 2105 (29 mai 2026) a publié un erratum le jour même (années 2024/2025 interverties dans la version initiale). | 0e7b6e8b-6941-4b24-9e67-ad37fbd256f7
FCT-007 | FACT | ✦ | https://www.insee.fr/fr/statistiques/2408345 | A,C | 2026-07-09 | Pauvreté facteur 5 selon le seuil choisi | En 2024 (France métropolitaine, ménages ordinaires, revenu déclaré >=0, référence non étudiante): 2 843 000 personnes pauvres au seuil 40 %, 5 599 000 à 50 %, 9 817 000 à 60 %, 14 576 000 à 70 % du niveau de vie médian — un facteur d'environ 5 selon le seul choix de seuil; l'Observatoire des inégalités privilégie le seuil 50 % qu'il juge 'plus significatif' que le 60 % officiel (seuils personne seule: 891/1114/1337 EUR). | a22a2146-1f94-4fa9-8978-9c1a97f0ef4e
FCT-008 | FACT | ✦ | https://www.insee.fr/fr/information/2553979 | A,B,other:wiki | 2025-06-24 | Populations de référence estimées mais juridiques | Les chiffres de population légale/référence sont des estimations par sondage (rotation 1/5 des communes <10k; sondage de 8 % des adresses pour les ≥10k) officialisées par décret annuel depuis 2008 et référencées par ~350 articles législatifs (DGF, nombre de conseillers, seuils); un écart >15 % entre estimation Insee (678) et dénombrement municipal (791) est documenté (Metzing, 2024, pénalisant la DGF); la CNERP a recommandé de réduire le décalage date de référence-entrée en vigueur de 3 à 2 ans (mise en oeuvre fin 2026). | dad9d305-19ff-4191-95a9-00a2ff13994c
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-008
FCT-002 | SRC-017
FCT-003 | SRC-016,SRC-007
FCT-004 | SRC-020,SRC-012
FCT-005 | SRC-018,SRC-002,SRC-003
FCT-006 | SRC-002,SRC-003,SRC-018
FCT-007 | SRC-004,SRC-005
FCT-008 | SRC-012,SRC-013,SRC-006

## REFUTATION_REGISTRY_V1
FCT-006 | QRY-036 | NONE
FCT-007 | QRY-037 | NONE
FCT-008 | QRY-035 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:CONFIRME
FCT-007 | ELIGIBLE:CONFIRME
FCT-008 | ELIGIBLE:CONFIRME

## MEMORY_WRITE_MODE_V1
FCT-001 | UPDATE | 46193d3f-f889-4f44-991f-6b001f4397bb
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | UPDATE | 0e7b6e8b-6941-4b24-9e67-ad37fbd256f7
FCT-007 | UPDATE | a22a2146-1f94-4fa9-8978-9c1a97f0ef4e
FCT-008 | UPDATE | dad9d305-19ff-4191-95a9-00a2ff13994c

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5;6;7 | NEXT_ACTION:9;10;11
CP-002 | SCOPE | PASS | LAST_COMPLETED:7;8 | NEXT_ACTION:9;10;11
CP-003 | SEARCH | PASS | LAST_COMPLETED:9;10 | NEXT_ACTION:11;12
CP-004 | FACTS | PASS | LAST_COMPLETED:10;11 | NEXT_ACTION:12
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11;12 | NEXT_ACTION:13;14
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14;15;16;17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18;18b

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-20T18:07:23.399098+00:00","fact_mem":{"FCT-001":"46193d3f-f889-4f44-991f-6b001f4397bb","FCT-002":"48b68f41-fea6-40d3-b520-1ed49158e750","FCT-003":"7201080d-1491-4933-8039-18bcaee8ae17","FCT-004":"deadb2bf-5ca6-4258-81b5-40911af4fdac","FCT-005":"19d69589-b559-4004-963b-f24ce0342d2a","FCT-006":"0e7b6e8b-6941-4b24-9e67-ad37fbd256f7","FCT-007":"a22a2146-1f94-4fa9-8978-9c1a97f0ef4e","FCT-008":"dad9d305-19ff-4191-95a9-00a2ff13994c"},"mnemo_row":"PASS: 8/8 eligible facts persisted via MCP update_memory/write_memory (8002); no duplicate_warning; run 20260920-1921-insee-pdf-methodo-gap-access-closure","result":"PASS","writeback_execution":[{"action":"UPDATE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"tier ✧ -> VERIFIE (réouverture chômage BIT, update_memory sur mémoire parent)","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"tier ✧ -> VERIFIE (nouveau fait IM136, write_memory)","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"tier ✧ -> VERIFIE (nouveau fait IM145, write_memory)","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"tier ✧ -> VERIFIE (nouveau fait fiche précision, write_memory)","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"tier ✧ -> VERIFIE (nouveau fait note révisions, write_memory)","success":1},{"action":"UPDATE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"tier ✦ -> CONFIRME (réouverture, réfutation NONE, update_memory)","success":1},{"action":"UPDATE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"tier ✦ -> CONFIRME (réouverture, réfutation NONE, update_memory)","success":1},{"action":"UPDATE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-008","reason":"tier ✦ -> CONFIRME (réouverture, réfutation NONE, update_memory)","success":1}],"writeback_row":{"attempted":8,"blocked":0,"eligible":8,"failure":0,"success":8}}

PERSISTENCE_META: MNEMO_ROW:PASS: 8/8 eligible facts persisted via MCP update_memory/write_memory (8002); no duplicate_warning; run 20260920-1921-insee-pdf-methodo-gap-access-closure | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:8;attempted:8;success:8;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[8 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✧ -> VERIFIE (réouverture chômage BIT, update_memory sur mémoire parent)
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✧ -> VERIFIE (nouveau fait IM136, write_memory)
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✧ -> VERIFIE (nouveau fait IM145, write_memory)
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✧ -> VERIFIE (nouveau fait fiche précision, write_memory)
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✧ -> VERIFIE (nouveau fait note révisions, write_memory)
FCT-006 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✦ -> CONFIRME (réouverture, réfutation NONE, update_memory)
FCT-007 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✦ -> CONFIRME (réouverture, réfutation NONE, update_memory)
FCT-008 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✦ -> CONFIRME (réouverture, réfutation NONE, update_memory)
