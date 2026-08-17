# RESOLUTION : GAP-LL2-1 : CHIFFRAGE DU PLAN D'AUDIT DES FILIÈRES ENR PAR QUESTION ÉCRITE (REC. N°1 CdC)

- STATE          : FINAL
- DATE           : 2026-08-10 22:15 CEST
- TYPE           : RESOLUTION (KERNEL v2.8, format allégé axe piste, GAP-ll2-1 du document 21-58)
- DOSSIER        : 2026-08-10_run2-enr (fil Valeco/EnBW, axe légitimité GAP-ll2-1)
- OBJECT         : convertir l'argument du ministre « un plan d'audit complet des filières requiert néanmoins des moyens humains significatifs, qui sont aujourd'hui le principal frein à leur généralisation » (réponse au rapport CdC 18/03/2026) en chiffre (ETP, budget), via une question écrite parlementaire et sa réponse ministérielle
- VERDICT        : CONSTAT D'ABSENCE. Aucune QE ne demande ni ne chiffre le plan d'audit des filières ENR (rec. n°1 CdC) à la date du 10/08/2026. La QE la plus proche, n° 13737 (S. Delannoy, JO 24/03/2026, 6 jours après le rapport), interroge le contrôle/fraude (rec. n°4) et la consolidation des données ; sa réponse (JO 09/06/2026) fournit des chiffres DGCCRF/ANAH/PNCEE/Tracfin mais NE répond PAS à la question de la collecte des coûts ni ne chiffre le plan d'audit : écart question/réponse documenté
- GAP_SEVERITY   : 0.15 (résolu en constat d'absence exhaustif : 36 351 QE scannées, dataset officiel complet)

## 1. Méthode : scan exhaustif du dataset officiel des QE de l'Assemblée nationale

- Source : dataset open data officiel de l'AN « Questions écrites » (`data.assemblee-nationale.fr/static/openData/repository/{16,17}/questions/questions_ecrites/Questions_ecrites.json.zip`), téléchargé le 10/08/2026.
- Périmètre : **36 351 QE scannées** (18 710 de la 16e législature 2022-2024 + 17 641 de la 17e législature 2024-2026), texte complet question + réponse de chaque QE.
- Mots-clés de filtrage (score pondéré) : « plan d'audit », « collecte des coûts », « coûts et recettes », « sur-rémunération », « audit des filières », « tableau de bord », « contrôle des installations », « moyens humains », « charges de service public », « obligation d'achat », « soutien aux énergies renouvelables », « Cour des comptes », « CRE ».
- Seuil de pertinence : score >= 5. Résultats : 267 QE (L16) + 416 QE (L17) = 683 QE candidates, toutes lues par tri décroissant de score.
- Artefacts : `data/qe_enr/scan16_resultats.txt` (924 Ko), `data/qe_enr/scan17_resultats.txt` (1,3 Mo), JSON des 2 QE clés archivés.

## 2. Résultat principal : constat d'absence

**Aucune QE (ni AN, ni identifiée au Sénat) ne demande le chiffrage du plan d'audit des filières ENR ou de la collecte des coûts/recettes des installations. Aucune réponse ministérielle ne chiffre les « moyens humains significatifs » de la rec. n°1 CdC.**

- Le syntagme « plan d'audit » : 0 occurrence dans les 36 351 QE (ni question ni réponse).
- « collecte des coûts » / « coûts et recettes » : 7 QE en L16, toutes hors sujet (audiovisuel, impôts locaux, déchets, TVA, commerce, eau) ; 0 en L17.
- Le sujet du rapport CdC ENR de mars 2026 n'a été saisi par AUCUN parlementaire en QE sur le volet collecte/audit à la date du 10/08/2026.

## 3. La QE la plus proche : n° 13737 (Sandra Delannoy, JO 24/03/2026)

### 3.1 La question (JO 24/03/2026, p. 2462)

> « Mme Sandra Delannoy interroge M. le ministre de l'économie, des finances et de la souveraineté industrielle, énergétique et numérique sur les carences persistantes de l'État dans la détection, le suivi et la sanction des fraudes aux dispositifs de soutien aux énergies renouvelables financés par les charges de service public de l'énergie (SPE). Dans son rapport de mars 2026, la Cour des comptes relève que, malgré un coût cumulé de 26,3 milliards d'euros entre 2016 et 2024 et des engagements hors bilan atteignant 87 milliards d'euros à fin 2024, l'État ne dispose toujours pas d'une vision consolidée des irrégularités affectant ces dispositifs. Elle souligne en particulier l'absence de bilan national des contrôles, le caractère lacunaire du suivi des anomalies signalées, ainsi que que les sanctions prononcées demeurent quasi inexistantes. [...] elle lui demande de bien vouloir indiquer, de manière précise et exhaustive : le nombre total de contrôles réalisés annuellement depuis 2020 sur les installations bénéficiant de ces dispositifs, ainsi que leur taux de couverture ; le nombre d'irrégularités, anomalies ou fraudes détectées sur la même période, en distinguant leur nature et leur gravité ; le montant total des aides indûment versées identifié à ce jour, ainsi que les montants effectivement recouvrés et ceux restant à recouvrer ; le nombre de sanctions administratives ou contentieuses effectivement prononcées, ainsi que leur typologie ; les délais moyens de traitement des signalements d'anomalies par les services de l'État. »

- Source : dataset AN `QANR5L17QE13737.json` (JO question : 2026-03-24, p. 2462, n° 20260012) ; URL officielle : questions.assemblee-nationale.fr/q/17-13737E.
- Auteur : Sandra Delannoy, députée non inscrite (acteurRef PA840119) ; ministère interrogé : Économie, finances et souveraineté industrielle, énergétique et numérique.
- Localisation : 6 jours après le rapport CdC (18/03/2026) : la QE cite les chiffres exacts du rapport (26,3 Md€, 87 Md€) dès le 24/03/2026.

### 3.2 La réponse (JO 09/06/2026, p. 5200) : les chiffres fournis

> « Depuis 2019, la DGCCRF a mis en place un plan de surveillance pluriannuel renforcé pour lutter contre la fraude dans le secteur de la rénovation énergétique. Le nombre d'établissements contrôlés n'a ainsi cessé de croître depuis cette date : en 2024, il s'élevait à 984, en hausse de 20 % par rapport à 2023. [...] la DGCCRF ne contrôle pas directement ce dispositif dont la réglementation est édictée par la direction générale de l'énergie et du climat (DGEC) et dont le public cible est plus large que les seuls consommateurs. [...] Au total, la DGCCRF a permis la saisie pénale de près de 10 millions d'euros et a prononcé pour 1,5 millions d'amendes administratives en 2024. Le montant total du préjudice économique des dossiers d'enquête ayant donné lieu à des suites répressives (procès-verbaux pénaux ou articles 40) peut être évalué à 131 millions d'euros, par inférence statistique. Cela représente un effet de levier considérable compte tenu des effectifs consacrés à la rénovation énergétique au niveau de la DGCCRF, à savoir 52 ETP. [...] selon Tracfin, le potentiel de fraude annuel sur l'ensemble des aides à la rénovation énergétique (MaPrimeRénov et CEE) est estimé à 100 millions d'euros. Par ailleurs, en 2025, c'est près de 21 439 dossiers qui ont été détectés par l'ANAH comme relevant d'une tentative de fraude, représentant un montant total de 174 millions d'euros de fraudes évitées. [...] La fraude subie [...] s'élèvent ainsi à 85 millions d'euros depuis 2020, soit 0,4 % des 19,2 milliards d'euros d'aides distribuées sur cette période. [...] en 2024, les sanctions prononcées s'élèvent à 2,97 TWh cumac annulés et 8,9 millions d'euros d'amende [PNCEE]. »

### 3.3 L'écart question/réponse (fait clé)

La réponse ne répond PAS aux items demandés (contrôles sur les installations ENR bénéficiant du soutien SPE, irrégularités, montants recouvrés, sanctions, délais de traitement). Elle bascule sur la rénovation énergétique des logements (DGCCRF 984 établissements, ANAH, PNCEE CEE) et reconnaît elle-même que « la DGCCRF ne contrôle pas directement ce dispositif » (le soutien ENR géré par la DGEC). Le seul chiffre d'effectifs : 52 ETP DGCCRF dédiés à la rénovation énergétique (pas au contrôle des installations ENR soutenues). La question de la collecte des coûts (rec. n°1) reste entièrement sans réponse.

## 4. Synthèse des chiffres publics sur les moyens de contrôle (au 10/08/2026)

| Acteur | Chiffre | Source |
|--------|---------|--------|
| DGCCRF contrôles rénovation énergétique 2024 | 984 établissements (+20 % vs 2023) | QE 13737, réponse JO 09/06/2026 |
| DGCCRF ETP rénovation énergétique | 52 ETP | idem |
| DGCCRF saisies pénales 2024 | ~10 M€ | idem |
| DGCCRF amendes administratives 2024 | 1,5 M€ | idem |
| DGCCRF préjudice (inférence statistique) | 131 M€ | idem |
| Tracfin potentiel fraude annuel (rénovation + CEE) | 100 M€ | idem |
| ANAH dossiers de fraude détectés 2025 | 21 439 (174 M€ fraudes évitées) | idem |
| Fraude subie établie depuis 2020 | 85 M€ (0,4 % de 19,2 Md€ d'aides) | idem |
| PNCEE sanctions 2024 | 2,97 TWh cumac annulés + 8,9 M€ | idem |
| **Plan d'audit des filières (rec. n°1 CdC)** | **AUCUN chiffre public (ETP, budget)** | **Absence constatée sur 36 351 QE** |

## 5. Pourquoi l'absence est un résultat (pas un échec)

1. La rec. n°1 du rapport CdC (18/03/2026) a une échéance 2026 et la réponse du ministre dans le contradictoire (21-58) subordonne sa mise en œuvre à des « moyens humains significatifs » non chiffrés.
2. La QE 13737 (Delannoy), posée 6 jours après le rapport, montre que la mécanique parlementaire fonctionne et cite les chiffres exacts du rapport : le canal existe.
3. Mais AUCUN parlementaire n'a posé la question du chiffrage de la collecte des coûts / plan d'audit en 5 mois (mars-août 2026). L'argument « moyens humains » n'a donc jamais été confronté à une exigence de chiffrage public.
4. L'écart question/réponse de la QE 13737 confirme le motif structurel du dossier : le contrôle des installations ENR soutenues (SPE, DGEC) est un angle mort, même quand une députée le vise explicitement, la réponse glisse vers la rénovation énergétique (seul secteur où des chiffres existent).
5. Action documentaire : la QE à poser (modèle) doit demander nommément « le nombre d'ETP consacrés par la CRE et la DGEC à la collecte des coûts et recettes des installations ENR, le budget du plan d'audit des filières, et le calendrier de publication du tableau de bord de l'économie des filières (rec. n°1 CdC) » : c'est la seule voie pour forcer un chiffre, et elle n'existe pas encore.

## 6. Table de faits

| ID | Proposition | Source | Localisation | Nature | Statut |
|----|-------------|--------|--------------|--------|--------|
| FCT-ll21-001 | Le dataset officiel « Questions écrites » AN comprend 18 710 QE (L16) + 17 641 QE (L17) = 36 351 QE | data.assemblee-nationale.fr (zip JSON téléchargés 10/08/2026) | repository/16/ et repository/17/ | Fait | ÉTABLI |
| FCT-ll21-002 | Scan exhaustif : « plan d'audit » = 0 occurrence dans les 36 351 QE | scan 16 + 17 (scripts) | data/qe_enr/scan*.txt | Fait | ÉTABLI |
| FCT-ll21-003 | « coûts et recettes » / « collecte des coûts » : 7 QE L16 hors sujet, 0 QE L17 | scan 16 + 17 | idem | Fait | ÉTABLI |
| FCT-ll21-004 | Aucune QE ne chiffre le plan d'audit des filières ENR (rec. n°1 CdC) au 10/08/2026 | scan exhaustif | idem | Fait (absence) | ÉTABLI |
| FCT-ll21-005 | QE 13737 (Sandra Delannoy, non inscrite) posée le 24/03/2026, 6 jours après le rapport CdC, citant 26,3 Md€ et 87 Md€ | QANR5L17QE13737.json | JO question 24/03/2026 p. 2462 n° 20260012 | Fait | ÉTABLI |
| FCT-ll21-006 | La QE 13737 demande contrôles, irrégularités, indus, recouvrements, sanctions, délais de traitement sur les installations ENR soutenues | idem | texte question | Fait | ÉTABLI |
| FCT-ll21-007 | Réponse du 09/06/2026 (JO p. 5200 n° 20260023) : DGCCRF 984 établissements contrôlés 2024, 52 ETP rénovation énergétique, ~10 M€ saisies, 1,5 M€ amendes, 131 M€ préjudice inféré | idem | texte réponse | Fait | ÉTABLI |
| FCT-ll21-008 | Réponse : Tracfin 100 M€ potentiel fraude annuel (rénovation + CEE) ; ANAH 21 439 dossiers 2025 (174 M€ évités) ; fraude subie 85 M€ depuis 2020 (0,4 % de 19,2 Md€) ; PNCEE 2,97 TWh cumac + 8,9 M€ 2024 | idem | texte réponse | Fait | ÉTABLI |
| FCT-ll21-009 | La réponse reconnaît que « la DGCCRF ne contrôle pas directement ce dispositif » (soutien ENR régi par la DGEC) : non-alignement question/réponse | idem | texte réponse | Fait (aveu) | ÉTABLI |
| FCT-ll21-010 | La réponse ne fournit AUCUN chiffre sur la collecte des coûts des installations ni sur le plan d'audit des filières | idem | lecture intégrale réponse | Fait (absence) | ÉTABLI |
| FCT-ll21-011 | Le ministère interrogé est l'Économie/finances/souveraineté industrielle et énergétique ; l'auteur est Sandra Delannoy (non inscrite, PA840119) | idem | métadonnées JSON | Fait | ÉTABLI |
| FCT-ll21-012 | Aucune QE Sénat équivalente identifiée (base basile inaccessible en OSINT direct, anti-bot ; non confirmée) | senat.fr/basile | 10/08/2026 | Limite | PARTIEL |
| FCT-ll21-013 | Une QE ciblée (modèle fourni) demandant ETP/budget CRE-DGEC + calendrier du tableau de bord serait la voie pour forcer un chiffre ; elle n'existe pas encore | Analyse | §5 | Inférence | CORROBORÉ |

## 7. Grille de verdict 3 axes (doctrine §13)

```text
PÉNAL    : 0 fait. L'absence de QE n'est pas une infraction.
LÉGAL    : oui. Rien d'illégal : la collecte des coûts n'est pas obligatoire et le silence parlementaire n'est pas une violation.
LÉGITIME : contestable. L'argument « moyens humains significatifs, principal frein » (réponse ministre, 21-58) n'a jamais été soumis à un chiffrage public en 5 mois ; la seule QE visant le contrôle (13737) a reçu une réponse qui glisse vers la rénovation énergétique, confirmant l'angle mort du contrôle des installations ENR soutenues. Le critère 3 (contrôle possible et effectué) et le critère 7 (opacité structurelle ou accidentelle) sont défavorablement renseignés : l'absence de chiffres est maintenue par l'absence de demande chiffrée.
```

## 8. Conclusion graduée

Le GAP-ll2-1 est résolu en constat d'absence exhaustif : sur les 36 351 QE publiées par l'Assemblée nationale (16e + 17e législatures), aucune ne chiffre le plan d'audit des filières ENR ni la collecte des coûts demandée par la rec. n°1 CdC. La QE 13737 (S. Delannoy, 24/03/2026) est le meilleur point d'appui : elle cite les chiffres du rapport 6 jours après sa publication et force une réponse ministérielle datée (09/06/2026), mais celle-ci confirme l'angle mort (la DGCCRF « ne contrôle pas directement ce dispositif ») sans fournir le moindre chiffre sur la collecte des coûts. La conversion de l'argument « moyens humains significatifs » en montant public ne peut donc pas se faire par une QE existante : elle exige une QE nouvelle (modèle §5) ou le test budgétaire du PLF 2027 (check-list P1-P10 du 19-07, jaune AAÎ CRE, programme 174 DGEC). L'absence de chiffrage n'est pas un vide documentaire mais un fait établi : le contrôle n'est pas seulement refusé, il n'est même pas demandé.

## 9. Sources

1. Dataset open data AN « Questions écrites » : `https://data.assemblee-nationale.fr/static/openData/repository/16/questions/questions_ecrites/Questions_ecrites.json.zip` et `/17/...` (téléchargés 10/08/2026, 36 351 QE).
2. QE n° 13737 : `QANR5L17QE13737.json` (archivé `data/qe_enr/`), URL officielle questions.assemblee-nationale.fr/q/17-13737E ; JO question 24/03/2026 p. 2462, JO réponse 09/06/2026 p. 5200.
3. QE n° 5466 (L16, Roseren, charges négatives 2022-2023) : archivé `data/qe_enr/QANR5L17QE5466.json` (contenu QE L16, fichier nommé selon convention de copie ; précédent documenté de la mécanique de réévaluation CRE par délibérations 2022-202 et 2022-272).
4. Scans complets : `data/qe_enr/scan16_resultats.txt`, `data/qe_enr/scan17_resultats.txt`.
5. Rapport CdC 18/03/2026 + réponses CRE/ministre (21-58) : références croisées.
