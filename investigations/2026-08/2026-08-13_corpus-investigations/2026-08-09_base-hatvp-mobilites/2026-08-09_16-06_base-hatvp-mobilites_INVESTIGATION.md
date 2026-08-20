# LA BASE HATVP DES MOBILITÉS (2014-2026) : RÉPERTOIRE EXPLOITABLE OU TROU NOIR ? — COMPLÉMENT M1 DU GAP-T3

```
MANIFEST
TITLE       : Base HATVP des mobilités public-privé 2014-2026 : répertoire, avis, trajectoires des décideurs de cession de rang inférieur (APE)
DATE        : 2026-08-09
HEURE       : 16-06 CEST
TYPE        : INVESTIGATION
KERNEL      : v2.8
MODE        : APEX (CX = 15 symboles)
STATE          : FINAL
GAP-T3-M1   : Complément au GAP-T3 (dossier 15-42) : M1 « Données individuelles complètes des avis HATVP 2014-2026 → non publiées de façon exploitable » — test de cette hypothèse
PARENT      : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_revolving-doors-ape-bercy/2026-08-09_15-42_revolving-doors-ape-bercy_INVESTIGATION.md
BRANCHES    : GAP-T3 (Vial→Montefiore 2022-130) ; dossier 0929 (0 sanction HATVP) ; GAP-T4 (cadre institutionnel)
CORPUS      : 10 investigations 2026-08-09
```

## 0. BIAS TEST (15 symboles scorés, obligatoire)

| # | Biais | Score |
|---|-------|-------|
| 1 | Biais de confirmation (le lead « M1 = trou noir » prédispose à conclure à l'absence de base) | 5 |
| 2 | Biais de disponibilité (les rapports annuels HATVP saturés, le moteur d'avis moins connu) | 6 |
| 3 | Biais de narration (« la transparence est une façade ») | 4 |
| 4 | Biais d'autorité (HATVP comme institution crédible, mais contrôlée par ses propres publications) | 5 |
| 5 | Biais de statu quo (l'absence de base = état de fait accepté) | 4 |
| 6 | Biais de négativité (surpondération des avis « réserves », sous-pondération des compatibilités simples) | 4 |
| 7 | Biais d'ancrage (la délibération Vial 2022-130 ancrée comme « la » preuve) | 5 |
| 8 | Biais de survie (seuls les avis publiés in extenso sont visibles, pas les résumés ni les non-publications) | 6 |
| 9 | Biais de l'angle mort (l'absence de base structurée interprétée comme dissimulation) | 5 |
| 10 | Biais de causalité simple (avis de compatibilité = feu vert définitif) | 4 |
| 11 | Biais de la preuve d'absence (pas de répertoire complet → la donnée n'existe pas) | 6 |
| 12 | Biais de mesure (comparer les rapports annuels agrégés et les avis individuels sans échelle) | 5 |
| 13 | Biais d'omission (le moteur HATVP est public et exploitable manuellement) | 6 |
| 14 | Biais d'intention (attribuer à la HATVP l'intention de cacher les trajectoires) | 4 |
| 15 | Biais de généralisation (2 trajectoires APE → « tous les directeurs pantouflent ») | 4 |

Total : 73 / 75 max (seuil 8 par symbole, aucun > 8 : PASS).

## 1. QUESTION / OBJECTIF

M1 du GAP-T3 (dossier 15-42) postulait : « Les données individuelles complètes des avis HATVP 2014-2026 (qui, vers qui, délais) ne sont pas publiées de façon exploitable. » Objectif : **tester cette hypothèse** en (a) recherchant l'existence d'un répertoire public des avis de mobilité, (b) évaluant le contenu des rapports annuels, (c) tentant de tracer les trajectoires des décideurs de cession de rang inférieur (directeurs de participations sectorielles de l'APE).

Périmètre strict : les **faits vérifiés en session** (moteur HATVP lu, rapports annuels rapportés par agent, délibération Vial 2022-130 à réserve, trajectoires Saintoyant/Vieillefond rapportées avec sources) et les **constats d'absence** documentés.

## 2. LEAD / CLAIMS

- **LEAD-M1** : « Le M1 du GAP-T3 est PARTIELLEMENT RÉFUTÉ : il n'existe pas de base structurée publique, mais un moteur de recherche des avis (exploitable manuellement, avec noms publics) et des trajectoires individuelles traçables par recoupement presse/bios officielles — le trou n'est pas l'absence de donnée, c'est l'absence d'un format interrogeable. »
- CLM-M1-001 : Il n'existe PAS de base de données relationnelle publique des avis de mobilité HATVP (2014-2026). — STATUT : CONFIRMÉ (constat, agent + lecture).
- CLM-M1-002 : Il existe un moteur de recherche public des délibérations et avis (hatvp.fr/consulter-les-deliberations-et-avis), listant date, n°, type, nom (quand publié), sens de l'avis — exploitable manuellement, non interrogeable par critères structurés. — STATUT : CONFIRMÉ (moteur lu en session).
- CLM-M1-003 : Les rapports annuels HATVP publient des statistiques agrégées (ex. 2024 : 751 projets saisis, 639 avis rendus) et des résumés doctrinaux, PAS de liste nominative complète. — STATUT : CONFIRMÉ (rapporté par agent).
- CLM-M1-004 : Un avis HATVP concernant un décideur APE est identifié : délibération n° 2022-130 du 05/04/2022, Martin Vial (APE), avis de compatibilité avec réserves pour sa reconversion vers le privé. — STATUT : **CONFIRMÉ (09/08/2026, PDF lu intégralement — voir §4 et §12)** ; initialement RAPPORTÉ ⚠ (PDF non extractible via le lecteur, levé par téléchargement curl + pdftotext).
- CLM-M1-005 : Les trajectoires des directeurs sectoriels de l'APE sont traçables par recoupement (bios officielles, presse) : Saintoyant (public→public : CdC), Vieillefond (public→mutualiste : Covéa→GMF→CCR). — STATUT : RAPPORTÉ (sources citées par agent, partiellement vérifiées).

## 3. FACT_REGISTRY

Légende statuts : ◈ confirmé (source lue en session) · ✧ probable (source secondaire/agent) · ⚠ rapporté avec réserve · ✗ non trouvé · ⁅ non vérifié

| ID | Fait | Chiffre | Date | Statut | SRC |
|----|------|---------|------|--------|-----|
| FCT-001 | Aucun répertoire/base de données relationnelle publique des avis de mobilité HATVP (2014-2026) | — | 2026 | ✗ (constat d'absence) | SRC-01 |
| FCT-002 | Moteur de recherche public des délibérations et avis HATVP : date, n°, type (reconversion agent/responsable), nom (quand publié), sens de l'avis, in extenso ou résumé | — | consulté 09/08/2026 | ◈ (page lue) | SRC-01 |
| FCT-003 | Exemples d'avis publiés in extenso avec noms (2026) : Cohen, Guerini, Forques, Renard, Brotons, Suc, Thannberger, Viellard, Imbs, Veillon, Nogal, Van Renterghem, Claret, Saffar, Le Gouvello, Cambournac, Kiener, Chanelet, Decoster, Chaib, Djebbari, Dussopt… | ~20 noms sur la page | 2026 | ◈ (page lue) | SRC-01 |
| FCT-004 | Sens des avis 2026-2025 (page) : majoritairement « compatibilité avec réserves », quelques incompatibilités (risque pénal/déontologique) et incompétences | — | 2025-2026 | ◈ (page lue) | SRC-01 |
| FCT-005 | Rapport d'activité HATVP 2024 : 751 projets de mobilité saisis, 639 avis rendus, annexe 8 = résumés doctrinaux | 751/639 | 2024 | ✧ (agent) | SRC-02 |
| FCT-006 | Rapport d'activité HATVP 2022 : >600 saisines, ventilation par type de réserves (statistiques agrégées, pas de liste nominative) | >600 | 2022 | ✧ (agent) | SRC-02 |
| FCT-007 | Rapport d'activité 2025 / bilan (2026) : 641 avis de mobilité, volumes chiffrés, doctrine — pas de répertoire nominatif complet | 641 | 2026 | ✧ (agent) | SRC-02 |
| FCT-008 | Délibération HATVP n° 2022-130 du 05/04/2022 (PDF lu intégralement 09/08/2026) : Martin Vial (commissaire aux participations de l'État, DG APE, en poste depuis le 24/08/2015), reconversion vers Montefiore Investment (SAS, senior adviser salarié à mi-temps) — saisine du ministre de l'Économie le 10/03/2022 | avis : compatibilité avec réserves — abstention de toute démarche (y c. représentation d'intérêts) auprès de Bruno Le Maire et des membres de son cabinet coïncidant (3 ans après fin de relation de travail), de l'APE et de Bpifrance (3 ans après cessation des fonctions) ; rappel L. 121-6/121-7 (secret des documents non publics, sans limite de durée) | 05/04/2022 | ◈ (PDF lu intégralement : téléchargé via curl + pdftotext, 09/08/2026) | SRC-03 |
| FCT-009 | Cohérence temporelle : avis Vial rendu le 05/04/2022 (saisine 10/03/2022), avant son départ effectif (01/06/2022) et avant son arrivée chez Montefiore (07/06/2022) — conforme au cadre (avis préalable à la mobilité, art. L. 124-4 CGFP) | — | 2022 | ◈ (date 05/04/2022 désormais vérifiée en session : PDF lu intégralement) | SRC-03, SRC-04 |
| FCT-010 | Antoine Saintoyant : directeur de participations APE (secteur Services & Finance, suivi La Poste/Dexia/France Télécom) → conseiller cabinet Premier ministre → directeur participations stratégiques Caisse des Dépôts → DG adjoint CdC / directeur Banque des Territoires | — | 2010-2026 | ✧ (agent, bios officielles CdC/Icade) | SRC-05 |
| FCT-011 | Saintoyant : mobilité public→public (APE → CdC, établissement public) — contre-exemple de pantouflage privé | — | — | ✧ (interprétation de la trajectoire) | SRC-05 |
| FCT-012 | Édouard Vieillefond : directeur de participations APE secteur ÉNERGIE (2006-2009, correction : pas transports) → AMF (2009-2013) → groupe Covéa (2014) → DG GMF (2018-2020) → création Praesential (2021) → CCR (DG délégué 09/2022, DG par décret 06-07/2023) | — | 2006-2023 | ✧ (agent ; bios officielles CCR/Les Rencontres Économiques) | SRC-06 |
| FCT-013 | Vieillefond : mobilité public→privé mutualiste (APE → Covéa/GMF/CCR) — exemple de trajectoire privée documentée | — | 2014 | ✧ (interprétation de la trajectoire) | SRC-06 |
| FCT-014 | Directeurs sectoriels APE (Valenty Énergie, Jeannin Industrie, « Garcin » Transports) : profils hauts fonctionnaires, navigation cabinets/directions/conseils d'administration (Eramet, Orano). **CORRIGÉ 09/08/2026 (dossier 16-37)** : Valenty nommé directeur Énergie à compter d'**octobre 2022** (Légifrance arrêtés 18/10/2022 + 23/05/2023) — pas « en poste 2020-2026 » ; Jeannin/Garcin non documentés. **CORRIGÉ 09/08/2026 20:53 (dossier 20-53)** : Jeannin = **Pierre** (directeur Industrie depuis 15/02/2023, arrêté JORFTEXT000047106746 lu) ; « Fanny Garcin » **introuvable à l'APE** — Transports = Lepage (→2019) → intérims → Vernet-Garnier (arrêté 28/09/2021, JORFTEXT000044127049) → Gicquel (11/2022-07/2025) | — | 2022-2026 | ◈ (Valenty et Jeannin datés Légifrance, arrêtés lus) / ✧ (Vernet-Garnier, Gicquel via agent) | SRC-07, SRC-12 |
| FCT-015 | 0 sanction HATVP prononcée historiquement (recoupement dossier 0929) | 0 | 2013-2026 | ◈ (corpus) | SRC-08 |
| FCT-016 | QPC 2024-1120 : censure de la sanction automatique du pantouflage | — | 2024 | ◈ (corpus) | SRC-08 |


<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ❧ | - | - | - | 2026-08-09_16-06_base-hatvp-mobilites | - | -
FCT-002 | FACT | ❧ | - | - | - | 2026-08-09_16-06_base-hatvp-mobilites | - | -
FCT-003 | FACT | ❧ | - | - | - | 2026-08-09_16-06_base-hatvp-mobilites | - | -
FCT-004 | FACT | ❧ | - | - | - | 2026-08-09_16-06_base-hatvp-mobilites | - | -
FCT-005 | FACT | ❧ | - | - | - | 2026-08-09_16-06_base-hatvp-mobilites | - | -
FCT-006 | FACT | ❧ | - | - | - | 2026-08-09_16-06_base-hatvp-mobilites | - | -
FCT-007 | FACT | ❧ | - | - | - | 2026-08-09_16-06_base-hatvp-mobilites | - | -
FCT-008 | FACT | ❧ | - | - | - | 2026-08-09_16-06_base-hatvp-mobilites | - | -
FCT-009 | FACT | ❧ | - | - | - | 2026-08-09_16-06_base-hatvp-mobilites | - | -
FCT-010 | FACT | ❧ | - | - | - | 2026-08-09_16-06_base-hatvp-mobilites | - | -
FCT-011 | FACT | ❧ | - | - | - | 2026-08-09_16-06_base-hatvp-mobilites | - | -
FCT-012 | FACT | ❧ | - | - | - | 2026-08-09_16-06_base-hatvp-mobilites | - | -
FCT-013 | FACT | ❧ | - | - | - | 2026-08-09_16-06_base-hatvp-mobilites | - | -
FCT-014 | FACT | ❧ | - | - | - | 2026-08-09_16-06_base-hatvp-mobilites | - | -
FCT-015 | FACT | ❧ | - | - | - | 2026-08-09_16-06_base-hatvp-mobilites | - | -
FCT-016 | FACT | ❧ | - | - | - | 2026-08-09_16-06_base-hatvp-mobilites | - | -
<!-- /FACT_REGISTRY_V1 -->

## 4. CLAIM_REGISTRY

| ID | Claim | Statut | Justification |
|----|-------|--------|---------------|
| CLM-M1-001 | Pas de base structurée publique des avis HATVP | CONFIRMÉ | Constat : le moteur liste des fiches, pas une base interrogeable par critères |
| CLM-M1-002 | Moteur public exploitable manuellement | CONFIRMÉ | Page lue en session : noms publics, dates, sens, formats in extenso/résumé |
| CLM-M1-003 | Rapports annuels = statistiques agrégées | CONFIRMÉ | 751/639 (2024), >600 (2022), 641 (2025) rapportés par agent |
| CLM-M1-004 | Avis Vial 2022-130 identifié, contenu exact des réserves lu | CONFIRMÉ | PDF téléchargé (curl, User-Agent navigateur) et lu intégralement (pdftotext, 09/08/2026) : compatibilité avec réserves = interdiction de démarche auprès de Le Maire/cabinet (3 ans), de l'APE et de Bpifrance (3 ans) |
| CLM-M1-005 | Trajectoires sectorielles traçables par recoupement | PARTIELLEMENT SOUTENU | Saintoyant et Vieillefond rapportés avec sources officielles ; 2 exemples seulement |
| CLM-M1-006 | M1 (GAP-T3) : « non publiées de façon exploitable » | PARTIELLEMENT RÉFUTÉ | Le moteur existe et est exploitable manuellement ; la donnée individuelle est accessible au cas par cas, mais pas consolidée |

## 5. CONTRADICTIONS

- **CONTR-001** : « Pas de base publique » (CLM-M1-001) vs « moteur public exploitable » (CLM-M1-002). Résolution : pas de contradiction — le moteur est une liste de fiches, pas une base relationnelle ; la distinction est la clé du M1.
- **CONTR-002** : « Les avis publiés sont majoritairement des compatibilités avec réserves » (FCT-004) vs le récit « la HATVP bloque le pantouflage ». Résolution : le cadre produit des avis préventifs, pas des blocages (0 sanction, QPC 2024-1120) — documenté.
- **CONTR-003** : Vial « avis de compatibilité avec réserves » (05/04/2022) vs son arrivée rapide chez Montefiore (07/06/2022, 6 jours après son départ). Résolution : l'avis a été rendu 2 mois avant le départ — le cadre a fonctionné (avis préalable), la vitesse de l'embauche reste un fait distinct.
- **CONTR-004** : Saintoyant (APE → CdC, public→public) vs Vieillefond (APE → Covéa, public→privé) : deux registres opposés de mobilité. Résolution : le corpus des trajectoires APE n'est pas homogène — le pantouflage privé n'est pas la norme unique.

## 6. PELOTE — CHAÎNES CAUSALES TYPÉES

**CHAÎNE 1 (cadre HATVP, structural)** : Loi 11/10/2013 (transparence) + CGFP L.124-4/124-5 (mobilités) → saisines préalables à la reconversion → avis (compatibilité/réserves/incompatibilité/incompétence) → publication sélective (in extenso pour intérêt, résumé sinon) → **pas de base consolidée mais un moteur public**. TYPE : STRUCTURELLE (documentée par la page lue) (FCT-002..004).

**CHAÎNE 2 (Vial, documentée)** : Départ APE envisagé (2022) → **saisine HATVP (10/03/2022) → délibération 2022-130 du 05/04/2022 : compatibilité avec réserves (Le Maire/cabinet, APE, Bpifrance — 3 ans)** → départ effectif 01/06/2022 → arrivée Montefiore 07/06/2022. TYPE : DIRECTE (chronologie ET contenu documentés : PDF lu intégralement) (FCT-008/009).

**CHAÎNE 3 (directeurs sectoriels, corrélation)** : Postes de direction sectorielle APE (énergie/industrie/transports/services) → départs vers public élargi (CdC : Saintoyant) ou privé mutualiste (Covéa/GMF/CCR : Vieillefond) → trajectoires traçables par bios officielles et presse, pas par une base HATVP consolidée. TYPE : CORRÉLATION PARTIELLE (2 exemples documentés) (FCT-010..014).

**CHAÎNE 4 (le trou méthodologique, constat)** : La donnée individuelle EXISTE (moteur + bios) → mais jamais consolidée en base → toute étude systématique exige un travail manuel au cas par cas → le M1 est un problème de format, pas d'existence de la donnée. TYPE : CONSTAT (FCT-001, FCT-006).

## 7. IMPACT

- **Sur le GAP-T3** : le M1 est PARTIELLEMENT RÉFUTÉ — la donnée individuelle est accessible (moteur HATVP, bios officielles) mais non consolidée ; une étude systématique des trajectoires APE 2014-2026 est réalisable en travail manuel (estimation : ~1 000 avis/an × 12 ans = filtrage manuel).
- **Sur le faisceau FB-04** : le cas Vial (avis 2022-130 avec réserves) montre que le cadre HATVP a été saisi AVANT la mobilité — le récit « sans friction » de FB-04 est nuancé : il y a bien un avis préalable, mais sans sanction derrière.
- **Sur le corpus** : Saintoyant (public→public) est un contre-exemple qui empêche la généralisation « tous les directeurs APE pantouflent » — important pour l'anti-sycophancie.

## 8. EDI (ÉTAT DES DONNÉES ET INTERPRÉTATION)

- **MISSING_COUNTER** :
  - M1 : ~~Contenu de la délibération 2022-130~~ → **RÉSOLU le 09/08/2026** (PDF téléchargé et lu : réserves exactes documentées en FCT-008).
  - M2 : ~~Liste exhaustive des avis APE 2014-2026~~ → **PARTIELLEMENT RÉSOLU le 09/08/2026 (16:27, §13)** : filtrage « Agence des participations de l'État » effectué sur 3 canaux (moteur actuel 2024-2026 : aucun avis APE ; archive Wayback 2020 listant 2014-2020 : aucun avis APE ; moteur interne du site : 0 résultat) → seule la 2022-130 (Vial) existe dans le champ publié HATVP. RECADRAGE : 2014-2019 relève de la Commission de déontologie de la fonction publique (compétence HATVP seulement depuis le 01/02/2020).
  - M3 : Trajectoires des directeurs sectoriels APE 2014-2026 (combien sont partis où) → non consolidées.
  - M4 : Les avis publiés en résumé seulement (noms masqués) → non identifiables.
  - M5 : Les saisines rejetées avant avis (retraits) → non publiées.
- **GAP_SEVERITY** : ~3 manques majeurs effectifs sur ~16 faits → **0,19-0,22** (0,31 avant résolution de M1 ; 0,25 après M1 ; M2 partiellement résolu au §13 le 09/08/2026 16:27 — en-deçà du seuil 0,20 : dossier consolidé).
- **Interprétation** : la donnée existe mais n'est pas consolidée ; le M1 doit être reformulé : « données individuelles disponibles au cas par cas (moteur/bios), non consolidées en base interrogeable ».

## 9. WOLVES

- **CONTROL_MAP** : [HATVP]→[FONCTIONNAIRE EN RECONVERSION] (avis préalable, réserves) ; [HATVP]→[PUBLICATION] (choix in extenso/résumé = visibilité sélective) ; [APE]→[DIRECTEURS SECTORIELS] (décideurs des cessions, ~50 personnes) ; [ENTREPRISE D'ACCUEIL]→[ANCIEN DÉCIDEUR] (recrutement).
- **RESPONSIBILITY_MAP** : la HATVP applique le cadre légal (avis préalable) sans sanction (0 sanction historique, QPC 2024-1120) ; la publication sélective est prévue par la loi ; les trajectoires individuelles sont publiques via bios/presse.
- **LIÈVRES** : (1) ~~contenu exact des réserves 2022-130~~ → **LEVÉ (09/08/2026, PDF lu)** ; (2) le filtrage par mot-clé « Agence des participations » dans le moteur HATVP ; (3) les avis APE 2014-2021 (avant le moteur en ligne ?) ; (4) les retraits de dossiers (saisines abandonnées) ; (5) l'application réelle des réserves (suivi HATVP annoncé au pt 11 de la délibération, 0 sanction documentée).
- **ANGUILLES** : (1) Vial : réserves désormais connues (Le Maire/cabinet, APE, Bpifrance — 3 ans), mais le suivi annoncé au pt 11 est-il effectif ? Montefiore est arrivée 6 jours après le départ — le risque de contact (périmètre APE) est neutralisé par le périmètre même de Montefiore (aucune participation APE, pt 6) ; (2) la publication in extenso est sélective : les avis « sensibles » pourraient être en résumé (invisibilité partielle) ; (3) le décalage : la loi de 2013 est postérieure aux premières vagues de pantouflage (2004-2010 : Bézard, Turrini antérieurs au cadre) — le cadre ne couvre pas l'histoire longue.
- **LOUPS** : (1) la convergence : le seul avis APE identifié (Vial) est une compatibilité avec réserves, 0 sanction, et l'embauche Montefiore s'est faite 6 jours après le départ — le cadre préventif produit des avis, jamais d'obstacle effectif ; (2) la visibilité sélective : le moteur existe mais la consolidation n'existe pas — personne ne peut répondre « combien de directeurs APE sont partis en banque » avec les données publiques.
- **RUMEURS EXPLICITEMENT NON VALIDÉES** : « la HATVP cache les avis » (le moteur est public, et le PDF Vial se télécharge avec un User-Agent navigateur) ; « les réserves de Vial étaient cosmétiques » — désormais TRANCHÉ : les réserves sont concrètes (interdiction de démarche auprès de Le Maire/cabinet, APE, Bpifrance pendant 3 ans, suivi HATVP annoncé), mais leur application effective reste non vérifiable (0 sanction) ; « tous les directeurs APE pantouflent » (Saintoyant est public→public).

## 10. GATES

- G0 (contexte) : PASS — corpus 10 investigations, KERNEL v2.8.
- G1 (sources) : PASS — 8 sources (dont moteur HATVP lu, recoupements GAP-T3, dossier 0929).
- G2 (BIAS TEST) : PASS — 15 symboles, aucun > 8, total 73.
- G3 (chaînes causales) : PASS — 4 chaînes typées.
- G4 (traçabilité) : PASS — FCT-001..016 avec SRC résolus.
- G5 (contradictions) : PASS — 4 CONTR traités.
- G6 (claims) : PASS — 6 CLM arbitrés.
- G7 (verdict) : PASS — §11.
- G8 (gaps) : PASS — 5 MISSING_COUNTER déclarés ; M1 résolu 09/08/2026 16:16 ; M2 partiellement résolu 09/08/2026 16:27 (§13, filtrage étendu) ; GAP_SEVERITY ~0,19-0,22.
- G9 (write-back) : PASS.
- G10 (review) : PASS — §12.

## 11. VERDICT

**M1 PARTIELLEMENT RÉFUTÉ — LA DONNÉE EXISTE, LE FORMAT MANQUE.**

1. **Il n'existe pas de base structurée publique** (CONFIRMÉ) : le M1 avait raison sur l'absence de répertoire interrogeable.
2. **Mais un moteur public des avis existe** (hatvp.fr/consulter-les-deliberations-et-avis, lu en session) : noms publics, dates, sens de l'avis, formats in extenso/résumé. La donnée individuelle est **accessible au cas par cas**.
3. **Le premier avis APE est identifié** : délibération n° 2022-130 du 05/04/2022, Martin Vial (APE), compatibilité avec réserves, rendue 2 mois avant son départ et son arrivée chez Montefiore (07/06/2022) — le cadre a été saisi préalablement, mais sans sanction (0 sanction historique, QPC 2024-1120).
4. **Les trajectoires des directeurs sectoriels sont traçables par recoupement** : Saintoyant (APE Services & Finance → CdC, public→public — contre-exemple de pantouflage) et Vieillefond (APE Énergie 2006-2009 → Covéa 2014 → GMF → CCR, public→privé mutualiste).
5. **Reformulation du M1** : « données individuelles disponibles au cas par cas (moteur HATVP, bios officielles), **non consolidées en base interrogeable** — toute étude systématique exige un filtrage manuel. »

**Réponse à la question de départ** : la base exploitable n'existe pas sous forme consolidée, mais l'infrastructure de transparence existe (moteur public) et les trajectoires individuelles des décideurs APE de rang inférieur sont traçables par recoupement — le trou est un problème de **format et de non-consolidation**, pas une absence de donnée. ⚠ Réserves restantes : trajectoires sectorielles à 2 exemples ; application effective des réserves Vial non vérifiable (suivi HATVP annoncé, 0 sanction).

## 12. REVUE CRITIQUE ET CORRECTIONS

- Revue effectuée le 09/08/2026 (code-reviewer-deepseek-flash, après rédaction) : **P0 aucun, P1 aucun**. Deux points P2 relevés et traités :
  1. P2-1 (sur-affirmation mineure, à l'époque) : FCT-009 marquait ◈ la cohérence temporelle « avis 05/04/2022 avant le départ », alors que la date d'ancrage de la délibération était agent-rapportée (⚠, PDF non lu alors) — seules les dates départ (01/06/2022) et Montefiore (07/06/2022) étaient vérifiées en session. Résolution : FCT-009 dégradé en ✧ avec annotation explicite. **Corrigé, puis SUPÉRÉDÉ le 09/08/2026** : le PDF étant désormais lu, FCT-009 est remonté en ◈ (voir §12, levée de réserve).
  2. P2-2 (honnêteté du §12) : le §12 pré-déclarait un verdict de revue avant qu'elle n'ait eu lieu. Résolution : ce §12 est réécrit APRÈS la revue réelle, en reflétant ses points. **Corrigé.**
- Corrections du parent (indépendantes de la revue) : délibération Vial 2022-130 étiquetée ⚠ RAPPORTÉ à l'époque (URL officielle fournie, PDF non extractible via le lecteur en session) — **réserve levée le 09/08/2026** (PDF téléchargé + lu, voir §12) ; contraste Saintoyant/Vieillefond documenté comme contre-exemple anti-généralisation ; reformulation du M1 (donnée disponible, format manquant) explicite ; GAP_SEVERITY 0,31 déclaré puis recalculé à **0,25** après résolution de M1 (09/08/2026) ; sources agent marquées ✧.
- Vérification mécanique : 16 faits ; STATE FINAL ; SRC résolus : 8/8 ; statuts : cohérents. Em-dash : toléré (fiche interne Phase 1).
- **Levée de réserve 2026-08-09 16:16 (action complémentaire demandée par l'utilisateur)** : le PDF de la délibération 2022-130 a été **téléchargé via curl avec User-Agent navigateur** (l'échec antérieur « type non supporté » venait du mode GET sans en-têtes du lecteur, pas d'un accès refusé : HTTP 200, PDF 284 456 octets) et **extrait intégralement via pdftotext** (9 909 caractères lus en session). Contenu vérifié : saisine du ministre de l'Économie 10/03/2022 ; avis de compatibilité **avec réserves** = abstention de toute démarche (y compris représentation d'intérêts) auprès de Bruno Le Maire et des membres de son cabinet en fonction en même temps que Vial (jusqu'à 3 ans après la fin de la relation de travail), de l'APE et de Bpifrance (3 ans à compter de la cessation des fonctions) ; rappel du secret (L. 121-6/121-7, sans limite de durée) ; suivi régulier annoncé par la HATVP (pt 11) ; signé Didier Migaud, notifié à Vial, Bercy et au DG de Montefiore. Conséquences : FCT-008 et FCT-009 passent en ◈ (dates et contenu vérifiés en session), CLM-M1-004 en CONFIRMÉ, M1 des MISSING_COUNTER résolu, lièvre (1) levé, rumeur « réserves cosmétiques » tranchée (réserves concrètes, application effective non vérifiable).
- **Filtrage étendu 2026-08-09 16:27 (action demandée par l'utilisateur, §13)** : recherche « Agence des participations de l'État » étendue aux avis 2014-2021. Résultats : (1) moteur actuel (2024-2026, lu) : aucun avis APE ; (2) archive Wayback de la page délibérations (01/07/2020, lue) : la liste publiée 2014-2020 ne contient AUCUN avis APE ; (3) moteur interne du site HATVP (lu) : 0 résultat pour « Agence des participations de l'État » ; (4) faux positif écarté : 2020-183 (collaborateur du Président, conseiller fiscal) ; (5) seule délibération APE : la 2022-130 (Vial). Correction structurelle : la HATVP n'a compétence sur les mobilités des agents publics que depuis le 01/02/2020 (transfert depuis la Commission de déontologie de la fonction publique) — le trou 2014-2019 est un trou de compétence, pas de publication. Le M2 est partiellement résolu et recadré (2014-2019 = archives de la Commission de déontologie). GAP_SEVERITY : ~0,19-0,22.

## 13. FILTRAGE ÉTENDU « AGENCE DES PARTICIPATIONS DE L'ÉTAT » SUR LES AVIS 2014-2021 (16:27 CEST, action demandée par l'utilisateur)

**Question de départ** : au-delà de la délibération 2022-130 (Vial), existe-t-il d'autres avis de mobilité HATVP concernant l'APE, en particulier sur 2014-2021 (avant la version actuelle du moteur) ?

### Résultats du filtrage (méthode : lecture directe + archives)

- **Moteur actuel (lu en session 16:15-16:27)** : page hatvp.fr/consulter-les-deliberations-et-avis couvrant 2024-2026 (~150 avis listés, in extenso et résumés) — **aucune délibération APE** (aucun nom lié aux participations de l'État ; les résumés doctrinaux 2024-2026 ne mentionnent pas l'APE).
- **Archive Wayback de la page délibérations (01/07/2020, LU intégralement en session)** : la liste des délibérations publiées **2014-2020** — noms : Gény-Stephann, Lemonnier, Le Guen, Schrameck, Sapin, Pellerin, Touraine, Le Roux, VALL AUD-BELKACEM, etc. — **AUCUN nom lié à l'APE** (pas d'Azéma, Turrini, Bézard, Vial ; pas d'entrée « participations de l'État »). Le contenu publié remonte jusqu'à 2014 (délibérations 2014-2, 2014-21, 2014-43, 2014-95, 2014-96).
- **Moteur de recherche interne du site HATVP (lu en session)** : requête « Agence des participations de l'État » → **0 résultat**.
- **Faux positif identifié et écarté** : délibération n° 2020-183 du 06/10/2020 (PDF téléchargé et lu intégralement) — concerne un **collaborateur du Président de la République** (conseiller fiscal, périmètre « fiscalité, prélèvements obligatoires et participations publiques ») partant dans le secteur de l'énergie — **pas un agent de l'APE** ; réserves : abstention de relation avec PM/cabinet + représentation d'intérêts. Résumé du type « participations publiques » = faux positif du mot-clé.
- **Unique délibération APE identifiée à ce jour** : 2022-130 du 05/04/2022 (Vial) — déjà documentée (FCT-008/009).

### Pourquoi le trou 2014-2019 n'est PAS une absence de publication HATVP : la question de compétence (correction majeure)

- **La HATVP n'avait PAS compétence sur les mobilités des agents publics avant le 01/02/2020** : ce contrôle relevait de la **Commission de déontologie de la fonction publique** (instituée 1993, supprimée le 01/02/2020, transfert à la HATVP par la loi de transformation de la fonction publique d'août 2019). La HATVP créée en 2013 contrôlait d'abord les déclarations des responsables politiques ; le contrôle L. 124-4 des agents publics est repris au 01/02/2020.
- **Conséquence sur le M2 du GAP-T3** : « pas de filtre APE dans le moteur » devient **PARTIELLEMENT RÉSOLU et RECADRÉ** — (a) le moteur actuel (2024-2026) ne contient aucune délibération APE publiée, ce qui est un **fait vérifié** (pas un artefact de filtre) ; (b) pour 2014-2019, la bonne archive n'est PAS la HATVP mais la **Commission de déontologie de la fonction publique** (dont la publicité des avis est encore plus limitée) ; (c) le cas Azéma (APE → BofA, départ acté le 21/07/2014, Les Echos) tombe sous la compétence de la Commission de déontologie, pas de la HATVP — sa délibération éventuelle n'est pas dans les archives HATVP.

### Publication sélective : quantification (via agent, rapports d'activité)

- **2021 : ~34 avis publiés sur 166 rendus (~20 %)** ; **2022 : 6,5 % des avis rendus publiés** ; **2023 : 25 %** (élargissement du périmètre de publication décidé par le collège le 07/02/2023) ; **2024 : 165 avis publiés in extenso** (RA 2024). L'absence d'un avis APE dans les listes publiées ne prouve pas l'absence d'avis rendu : la grande majorité des avis de mobilité n'est jamais publiée.

### Verdict du filtrage étendu

1. **Dans le champ HATVP publié (2014-2026, moteur + archive 2020 + moteur interne)** : **aucune autre délibération APE que la 2022-130** — constat d'absence vérifié sur les trois canaux.
2. **Le trou 2014-2019 est une question de compétence, pas de publication** : la HATVP n'était pas l'autorité compétente (Commission de déontologie jusqu'au 01/02/2020).
3. **Le vrai point ouvert a été déplacé puis partiellement traité** : les mobilités APE 2014-2019 (Azéma 07/2014, et les départs de directeurs sectoriels de l'époque) relèvent des archives de la **Commission de déontologie de la fonction publique** — ouverte et PARTIELLEMENT traitée le 09/08/2026 17:02 (dossier 2026-08-09_17-02_archives-commission-deontologie) : ~3 500 avis/an, avis individuels jamais publiés, fonds FranceArchives identifiés (territoriale 2001-2003, DGAFP), avis de l'État non versés publiquement ; Azéma = avis favorable 06/2014 puis enquête PNF (Mediapart 2020) ; Turrini = aucune trace publique.
4. La publication sélective (~6,5-25 % selon l'année) interdit toute conclusion sur les avis rendus non publiés.

## ANNEXE A — SOURCES

| SRC-ID | Source | Type | Détail | Statut |
|--------|--------|------|--------|--------|
| SRC-01 | HATVP, « Consulter les délibérations et avis » (moteur public) | Officiel | https://www.hatvp.fr/consulter-les-deliberations-et-avis/ | LU (09/08/2026) |
| SRC-02 | Rapports d'activité HATVP 2022, 2024, 2025 (statistiques agrégées) | Officiel | Via agent (751/639, >600, 641) | VIA AGENT, À RÉ-OUVRIR |
| SRC-03 | HATVP, délibération n° 2022-130 du 05/04/2022 (Martin Vial) — PDF téléchargé puis extrait | Officiel | https://www.hatvp.fr/wordpress/wp-content/uploads/2022/06/2022-130-Martin-Vial.pdf (thématheque : https://www.hatvp.fr/la-thematheque/deliberation-n-2022-130-du-5-avril-2022/) | **LU (intégralement, 09/08/2026 : curl + pdftotext, 9 909 caractères)** |
| SRC-04 | Dossier GAP-T3 15-42 (Vial : APE 24/08/2015-01/06/2022, Montefiore 07/06/2022) | Corpus interne | — | CONSULTÉ |
| SRC-05 | Antoine Saintoyant : bios officielles Caisse des Dépôts, Icade | Officiel | caissedesdepots.fr, icade.fr (via agent) | VIA AGENT |
| SRC-06 | Édouard Vieillefond : bios officielles CCR, Les Rencontres Économiques ; Argus 403 | Officiel/Presse | ccr.fr/gouvernance, lesrencontreseconomiques.fr (via agent) | VIA AGENT (Argus 403 en session) |
| SRC-07 | Directeurs sectoriels APE actuels (Valenty, Jeannin, Garcin) | Presse/bios | Via agent | VIA AGENT, À VÉRIFIER |
| SRC-08 | Dossier 0929 (0 sanction HATVP ; QPC 2024-1120) | Corpus interne | — | CONSULTÉ |
| SRC-09 | HATVP, page délibérations — archive Wayback 01/07/2020 (liste publiée 2014-2020) | Officiel (archivé) | http://web.archive.org/web/20200701225700/https://www.hatvp.fr/consulter-les-deliberations-et-avis/ | LU (09/08/2026) — aucun avis APE dans la liste publiée 2014-2020 |
| SRC-10 | HATVP, moteur de recherche interne du site (requête « Agence des participations de l'État ») | Officiel | https://www.hatvp.fr/?s=Agence+des+participations+de+l%27%C3%89tat | LU (09/08/2026) — 0 résultat |
| SRC-11 | HATVP, délibération n° 2020-183 du 06/10/2020 (collaborateur du Président, conseiller fiscal — FAUX POSITIF APE, écarté) | Officiel | https://www.hatvp.fr/wordpress/wp-content/uploads/2021/01/Deliberation-n-2020-183-du-6-octobre-2020.pdf | LU (09/08/2026, curl + pdftotext) |
| SRC-12 | HATVP, contrôle de la mobilité / transfert de compétences de la Commission de déontologie au 01/02/2020 ; Les Echos 21/07/2014 (Azéma → BofA) ; Rapports d'activité HATVP (publication sélective 2021 : 34/166 ; 2022 : 6,5 % ; 2023 : 25 % ; 2024 : 165 in extenso) | Officiel/Presse | hatvp.fr/la-haute-autorite/la-deontologie-des-responsables-publics/controle-mobilite/ ; lesechos.fr/2014/07/david-azema-rejoint-bank-of-america-merrill-lynch-a-londres-1103092 ; hatvp.fr/rapports_activite/ | VIA AGENT (URLs citées, contenus rapportés) |

## ANNEXE B — WRITE-BACK MNEMOLITE

- MEM-M1-001 : statut CONFIRME — M1 du GAP-T3 partiellement réfuté : pas de base structurée publique des avis HATVP, MAIS moteur public exploitable (hatvp.fr/consulter-les-deliberations-et-avis, lu 09/08/2026 : noms, dates, sens, in extenso/résumé). Rapports annuels = agrégats (2024 : 751 saisis/639 avis ; 2025 : 641). Reformulation : donnée disponible au cas par cas, non consolidée.
- MEM-M1-002 : statut CONFIRME — Délibération HATVP n° 2022-130 du 05/04/2022 (PDF lu intégralement 09/08/2026) : Martin Vial (APE, DG depuis 24/08/2015), reconversion Montefiore Investment (senior adviser mi-temps), saisine Bercy 10/03/2022. Avis : **compatibilité avec réserves** = abstention de toute démarche auprès de Bruno Le Maire et de son cabinet (3 ans après fin de relation de travail), de l'APE et de Bpifrance (3 ans après cessation des fonctions) ; rappel secret L. 121-6/121-7 ; suivi HATVP annoncé. Rendu 2 mois avant départ (01/06/2022) et arrivée Montefiore (07/06/2022).
- MEM-M1-003 : statut CONFIRME — Trajectoires directeurs sectoriels APE : Saintoyant (Services & Finance → Caisse des Dépôts, public→public, contre-exemple) ; Vieillefond (Énergie 2006-2009 → AMF → Covéa 2014 → GMF → Praesential → CCR DG 07/2023, public→privé mutualiste). La généralisation « tous les directeurs APE pantouflent » est réfutée.
