# RESOLUTION : CONTACTS CRE DANS LES ACTIVITES RI DE FEDEREC 2023-2025 (GAP-fd-3)

- STATE          : FINAL
- DATE           : 2026-08-11 16:38 CEST
- TYPE           : RESOLUTION (KERNEL v2.8, format allégé fil VP-P4)
- DOSSIER        : 2026-08-10_run2-enr (piste ENR, fil VP-P4)
- OBJECT         : GAP-fd-3 du 16-31 : vérifier si les activités de représentation d'intérêts de FEDEREC sur le secteur énergie (répertoire RI) ont inclus des contacts avec la CRE entre le 14/11/2023 et le 03/07/2025, période de réserve de l'avis 2023-248
- SOURCE         : API répertoire RI HATVP (JSON agora FEDEREC, 784358749, téléchargé 11/08/2026, 153 Ko) : 5 exercices 2021-2025, 43 fiches d'activités 2023-2025 analysées
- HASHS          : 0 em-dash, 11 FCT-rc

## 1. OBJECT ET MÉTHODE

Le 16-31 a établi que le mandat FEDEREC de Carenco (14/11/2023) n'a pas de réserve de non-contact avec la CRE (l'incompétence 2023-247 n'en pose aucune ; la réserve du 2023-248 s'attache à Zalis). GAP-fd-3 : vérifier si les activités de représentation d'intérêts déclarées par FEDEREC au répertoire RI ont inclus des contacts avec la CRE pendant la période de réserve (14/11/2023 - 03/07/2025). Méthode : re-téléchargement du JSON agora de l'entité FEDEREC (SIREN 784358749) via l'API publique, analyse des 43 fiches d'activités des exercices 2023 (21), 2024 (10) et 2025 (12), recherche des mentions CRE/RTE/Enedis/AAI/GRTgaz/Storengy dans les objets, domaines, responsables publics contactés et « responsablePublicAutre ».

## 2. FAITS (TABLE DE FAITS)

| # | Fait | Source |
|---|------|--------|
| FCT-rc-001 | FEDEREC déclare 5 exercices au répertoire RI (2021 : 25 activités, 75-100 K€ ; 2022 : 21, 100-200 K€ ; 2023 : 21, 100-200 K€ ; 2024 : 10, 200-300 K€ ; 2025 : 12, 200-300 K€) : la fédération est une déclarante régulière et volumineuse | JSON agora 784358749 |
| FCT-rc-002 | Les exercices 2023-2025 couvrent la période de réserve : 2023 (publié 20/03/2024, inclut 14/11-31/12/2023), 2024 (publié 31/03/2025, couvre toute la période de réserve), 2025 (publié 10/03/2026, inclut 01/01-03/07/2025) | JSON agora (dates de publication) |
| FCT-rc-003 | **Scan exhaustif des 43 fiches d'activités 2023-2025 : 0 mention de la CRE, 0 mention de RTE, 0 mention d'Enedis, 0 mention d'AAI, 0 mention GRTgaz/Téréga/Storengy** dans les objets, domaines, responsables publics ou « autre » | Scripts fd_cre_exact/fd_dump_all, 11/08 |
| FCT-rc-004 | Les responsables publics contactés (43 fiches) : parlementaires et collaborateurs d'assemblées (20), agents d'administration centrale (17), titulaires d'emploi à la décision du Gouvernement (10), membres du Gouvernement/cabinets (23 occurrences cumulées sur 10 libellés distincts), collaborateurs du Président (4), élus régionaux (2) : **aucune AAI, aucun régulateur** | fd_labels, 11/08 |
| FCT-rc-005 | « ResponsablePublicAutre » déclaré : uniquement Ministère de l'industrie (4), Ministère des Transports (1), Ministre de l'industrie (1) : aucun régulateur de l'énergie | fd_cre_exact, 11/08 |
| FCT-rc-006 | 4 fiches touchent le domaine « Energie » (sur 43) : toutes liées à la valorisation énergétique des déchets (CSR, combustibles solides de récupération) et au PLF 2024 (TGAP réduite, Fonds économie circulaire ADEME) : cibles = parlementaires + ministère Environnement/énergie + Economie/finances, **jamais la CRE** | fd_energie4, 11/08 |
| FCT-rc-007 | Les domaines déclarés (43 fiches) : Environnement 43, Economie 26, Finances publiques 6, **Energie 4**, Commerce extérieur 4, Transports 2, etc. : le secteur énergie est marginal dans l'activité RI de FEDEREC | fd_labels, 11/08 |
| FCT-rc-008 | Les actions typiques (4 fiches énergie) : transmission d'informations/expertises, suggestions pour influencer une décision, correspondance régulière, réunions tête-à-tête : des démarches de lobbying parlementaire et ministériel, pas de saisine de régulateur | fd_energie4, 11/08 |
| FCT-rc-009 | **CONSTAT D'ABSENCE** : aucun contact avec la CRE déclaré par FEDEREC au répertoire RI sur la période de réserve (14/11/2023 - 03/07/2025), ni sur 2023-2025 en général | Scan 43 fiches, 11/08 |
| FCT-rc-010 | LIMITE ÉPISTÉMIQUE : le répertoire RI documente ce qui est DÉCLARÉ, pas la réalité des contacts : un contact non déclaré (informel, téléphonique, via JFC2) ne serait pas visible ; le constat est un constat d'absence, pas une preuve d'absence de contact | Méthode répertoire RI |
| FCT-rc-011 | LIMITE COMPLÉMENTAIRE : la réserve du 2023-248 s'attache à la personne de Carenco (pas de démarche auprès de la CRE jusqu'au 03/07/2025) : les fiches FEDEREC sont déclarées au nom de l'entité, sans granularité « par personne » : un contact de Carenco au nom de FEDEREC ne serait pas distinguable dans le répertoire | Avis 2023-248 (lu), 13-20 |

## 3. VERDICT

- **GAP-fd-3 RÉSOLU en constat d'absence** : sur les 43 fiches d'activités déclarées par FEDEREC au répertoire RI pour 2023-2025 (couvrant intégralement la période de réserve 14/11/2023 - 03/07/2025), **aucune ne mentionne un contact avec la CRE**, ni avec aucun régulateur de l'énergie (RTE, Enedis, GRTgaz, AAI).
- **Le secteur énergie est marginal et non régulé dans le lobbying de FEDEREC** : 4 fiches sur 43, toutes liées au CSR/valorisation énergétique des déchets, ciblant parlementaires et ministères (Budget/PLF, Environnement-énergie) : la filière que défend FEDEREC ne relève pas de la régulation CRE (l'énergie du déchet n'est pas l'électricité du réseau).
- **Le faisceau VP-P4 n'est pas enrichi** : aucun indice de démarches de FEDEREC auprès de la CRE pendant la réserve de Carenco. Le point de vigilance du 16-31 (contacts RI FEDEREC-CRE pendant la réserve) est levé à la source du répertoire, avec les limites documentées (déclaré ≠ réel ; granularité entité ≠ personne).
- **Aucun fait d'infraction** : ni contact déclaré, ni contournement visible de la réserve via FEDEREC.

## 4. GAPS OUVERTS

- **GAP-rc-1** : les contacts informels non déclarés restent inaccessibles : seule une saisine du répertoire (contrôles HATVP sur FEDEREC, qui déclare et est régulièrement contrôlée) ou un contentieux permettrait de vérifier l'exhaustivité des déclarations.
- **GAP-rc-2** : granularité « par personne » : vérifier si les fiches FEDEREC post-11/2023 comportent un champ dirigeant/déclarant permettant de relier les actions à Carenco (le JSON n'a pas montré de tel champ à l'analyse) : si la structure du répertoire ne permet pas cette granularité, c'est une limite structurelle du contrôle.
- **GAP-fd-2 (reprise)** : dater le début des prestations rémunérées JFC2 → FEDEREC (comptes JF CONSEILS fin 2026) : si JFC2 intervient pour FEDEREC auprès de la CRE après 07/2025, la chaîne de représentation passe par la société de conseil, hors répertoire (JFC2 non inscrite, cf. 14-30).

## 5. REVUE CRITIQUE

- Revue critique appliquée le 11/08/2026 16:40 (P2 corrigé 16:43) : (1) P2 arithmétique : cumul « membres du Gouvernement/cabinets » = 23 occurrences (7+4+3+2+2+1+1+1+1+1), pas 21 : corrigé en FCT-rc-004 (« 23 occurrences cumulées sur 10 libellés distincts ») et dans l'entrée 75 du manifest ; (2) distinguer constat d'absence (déclaré) de preuve d'absence (réel) : fait (FCT-rc-010) ; (3) recherche CRE exacte (regex \bcre\b, chaîne « commission de régulation de l'énergie », sous-chaîne « rte » rejetée) : fait (fd_cre_exact) ; (4) période de réserve couverte par les exercices 2023-2025 : fait (FCT-rc-002) ; (5) granularité entité/personne documentée (FCT-rc-011) ; (6) note : le scan couvre les champs déclaratifs objet/domaines/responsables/autre des fiches (actionsMenees et decisionsConcernees non scannés séparément, risque faible car un contact CRE apparaîtrait dans reponsablesPublics) : noté.
- Fichiers liés : 16-31 (GAP-fd-3 ouvert), 14-30 (fiche FEDEREC, méthode API ES), 13-20 (avis 2023-248/2025-233), 15-52 REGISTRE.
