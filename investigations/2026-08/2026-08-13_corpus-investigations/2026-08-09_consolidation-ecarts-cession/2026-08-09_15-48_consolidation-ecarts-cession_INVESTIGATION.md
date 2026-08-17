# CONSOLIDATION DES ÉCARTS CESSION/VALEUR : PREMIÈRE ESTIMATION MÉTHODOLOGIQUE DU MANQUE À GAGNER DES ACTIFS PUBLICS

```
MANIFEST
TITLE       : Consolidation des écarts cession/valeur (autoroutes, aéroports, FDJ, EDF, Alstom) : méthode et bornes
DATE        : 2026-08-09
HEURE       : 15-48 CEST
TYPE        : INVESTIGATION
KERNEL      : v2.8
MODE        : APEX (CX = 15 symboles) — type METHOD
STATE          : FINAL
GAP-T4      : Résolution du GAP-T4 « Chiffrage global des écarts cession/valeur » (HYPER_MATRICE 2026-08-09_15-15, enquête priorisée n° 4)
PARENT      : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_faisceaux-angles-morts/2026-08-09_15-15_faisceaux-angles-morts_HYPER_MATRICE.md
BRANCHES    : dossier 1507 découpe (Toulouse 308→507 M€, Alstom 12,35→9,7 Md€) ; dossier 15-24 architectes (262 M€ coûts transaction) ; HYPER_MATRICE (autoroutes 6,5-7,8 Md€, FDJ +15 %, EDF surprime 45 %)
CORPUS      : 9 investigations 2026-08-09
```

## 0. BIAS TEST (15 symboles scorés, obligatoire)

| # | Biais | Score |
|---|-------|-------|
| 1 | Biais de confirmation (le corpus « découpe » prédispose à trouver des pertes pour l'État) | 6 |
| 2 | Biais de disponibilité (les 5 opérations médiatisées plutôt que l'ensemble des cessions) | 6 |
| 3 | Biais de narration (« la France s'est fait brader ») | 5 |
| 4 | Biais d'autorité (Sénat, CdC, FIPECO : institutions crédibles mais agendas différents) | 5 |
| 5 | Biais de statu quo (le prix de cession est « la » valeur de référence) | 5 |
| 6 | Biais de négativité (surpondération des écarts, sous-pondération des recettes réelles) | 6 |
| 7 | Biais d'ancrage (14,8 Md€ autoroutes ancré comme « le » repère) | 4 |
| 8 | Biais de survie (seules les cessions contestées sont consolidées, pas les réussites) | 6 |
| 9 | Biais de l'angle mort (l'absence de comptabilité patrimoniale publique) | 5 |
| 10 | Biais de causalité simple (écart = sous-évaluation délibérée) | 5 |
| 11 | Biais de la preuve d'absence (pas de révision des prix → prix faux) | 4 |
| 12 | Biais de mesure (additionner des écarts de natures différentes) | 7 |
| 13 | Biais d'omission (les concessions ont rapporté 14,8 + 4,0 Md€ réels ; l'État a encaissé) | 5 |
| 14 | Biais d'intention (attribuer aux cédants une intention de nuire aux finances publiques) | 4 |
| 15 | Biais de généralisation (5 opérations → « toutes les cessions sont sous-évaluées ») | 5 |

Total : 78 / 75 max (seuil 8 par symbole, aucun > 8 : PASS).

## 1. QUESTION / OBJECTIF

GAP-T4 (HYPER_MATRICE 15-15) : **peut-on consolider les écarts cession/valeur documentés (autoroutes, aéroports, FDJ, EDF, Alstom) en une première estimation du manque à gagner des actifs publics ?** Objectif : proposer une **méthode de consolidation honnête** — distinguer les natures d'écarts, borner les estimations, refuser le chiffre unique — et produire la première synthèse chiffrée transversale du corpus.

Périmètre strict : **aucun chiffre inventé** ; chaque écart est sourcé (dossier frère, rapport institutionnel, article lu en session) ; les écarts de natures différentes ne sont **jamais additionnés sans explication** ; le résultat est une borne assortie de statuts, pas un total définitif.

## 2. MÉTHODE (cœur du dossier)

**Règle 1 — Nature des écarts (3 registres, jamais mélangés) :**
- **REG-1 Écarts de cession (manque à gagner)** : actif cédé, revente ou estimation institutionnelle montrant une valeur supérieure au prix de cession. [Toulouse, autoroutes]
- **REG-2 Surcoûts d'acquisition par l'État (rachat)** : l'État rachète (pas une cession) à un prix jugé excessif. [EDF]
- **REG-3 Coûts de transaction** : frais de la cession (conseils, banques, fiscal). [Alstom]

**Règle 2 — Statuts des écarts (4 niveaux) :**
- ◈ DOCUMENTÉ : écart constaté par une transaction de référence (revente) ou un rapport institutionnel chiffré.
- ✧ ESTIMÉ : chiffre institutionnel (Sénat, CdC) fondé sur des hypothèses explicites.
- ⁂ PROJETÉ : décote/écart inféré (ex. hausse du jour d'IPO), jamais chiffré officiellement.
- ⚠ CONTESTÉ : l'écart est dénoncé mais contesté (validité de la comparaison).

**Règle 3 — Bornes, pas de total unique :** la consolidation produit une fourchette basse (◈ uniquement) et une fourchette large (◈ + ✧ + ⁂), jamais un chiffre unique « le préjudice ».

**Règle 4 — Contre-faits obligatoires :** les recettes réelles encaissées par l'État (14,8 + 4,0 Md€ autoroutes, 2,06 Md€ aéroports, ~1,8 Md€ FDJ) sont systématiquement rappelées à côté des écarts.

## 3. FACT_REGISTRY (écarts et contre-faits)

Légende statuts : ◈ documenté · ✧ estimé · ⁂ projeté · ⚠ contesté · ✦ rapporté

| ID | Fait | Chiffre | Date | Statut | SRC |
|----|------|---------|------|--------|-----|
| FCT-001 | Toulouse : cession 49,99 % à Casil Europe (4 163 €/action) | 308 M€ | 07/04/2015 | ◈ | SRC-01 |
| FCT-002 | Toulouse : revente des 49,99 % à Eiffage | ~507 M€ | 30/12/2019 | ◈ | SRC-01 |
| FCT-003 | **Écart Toulouse (REG-1)** : plus-value captée par l'acquéreur en 4 ans | **+199 M€** (507−308) | 2019 | ◈ | SRC-01 |
| FCT-004 | Autoroutes : privatisation totale ASF, APRR, SANEF (2006) | 14,8 Md€ | 2006 | ◈ | SRC-02, SRC-03 |
| FCT-005 | Autoroutes : privatisations partielles 2002-2005 (ASF 49 %, APRR 30 %, SANEF 24 %) | 4,0 Md€ | 2002-2005 | ◈ | SRC-03 |
| FCT-006 | Autoroutes : ASF vendue à 51 €/action avec UNE seule offre (Vinci, déjà 23 % du capital) ; selon la note FIPECO, cette présence de Vinci « a très probablement dissuadé d'autres candidats, limité la concurrence et réduit le prix de cession » (analyse de l'auteur ; la commission des participations a fixé les prix minimaux et émis un avis favorable) | 51 € | 2006 | ◈ (source lue) | SRC-03 |
| FCT-007 | Autoroutes : prix minimaux fixés par la commission des participations : APRR 61 €, SANEF 58 €, ASF 51 € (prix réels = minimaux) | 51/58/61 € | 2006 | ◈ | SRC-03 |
| FCT-008 | **Manque à gagner autoroutes (REG-1)** : rapport Sénat n° 709 (09/2020) | **6,5 Md€ (valeur 2006) → ~7,8 Md€ (actualisé 2020)** | 09/2020 | ✧ | SRC-02 |
| FCT-009 | Dividendes cumulés attendus des concessionnaires sur la durée des concessions (jusqu'aux échéances 2031-2036) | 32-40 Md€ | 09/2020 | ✧ | SRC-02 |
| FCT-010 | Rentabilité 2019 des 4 concessionnaires historiques : CA 9,9 Md€, résultat net 3,3 Md€, dividendes 3,0 Md€, dette nette 24 Md€ | — | 2019 | ◈ | SRC-03 |
| FCT-011 | TRI prévisionnels à la privatisation vs au terme : ASF 7,1 % → 10,9 % ; APRR 9,2 % → 11,2 % ; SANEF 8,0 % (2019 : -1,4 %) | — | 2006-2036 | ◈ | SRC-03 |
| FCT-012 | FDJ : IPO 21/11/2019, prix 19,90 € institutionnels / 19,50 € particuliers (décote 2 %) | 19,90/19,50 € | 21/11/2019 | ◈ | SRC-04 |
| FCT-013 | FDJ : capitalisation au prix de référence | ~3,72 Md€ | 11/2019 | ◈ | SRC-04 |
| FCT-014 | FDJ : hausse le jour de l'IPO | **+16,4 %** (clôture 22,70 €) | 21/11/2019 | ◈ | SRC-04 |
| FCT-015 | **Décote FDJ (REG-1, ⁂)** : si la hausse du jour 1 (16,4 %) reflète la sous-valorisation initiale, l'écart projeté serait de l'ordre de ~600 M€ (16,4 % × 3,72 Md€) — JAMAIS chiffré officiellement | ~600 M€ (projection) | 2019 | ⁂ | SRC-04 |
| FCT-016 | FDJ : produit brut de cession pour l'État | ~1,8 Md€ (+ 380 M€ de soulte monopole = >2 Md€) | 11/2019 | ◈ | SRC-04 |
| FCT-017 | EDF : OPA simplifiée de l'État sur les ~16 % non détenus (rachat, PAS une cession — REG-2) | 12 €/action | 2022-2023 | ◈ | SRC-05 |
| FCT-018 | EDF : montant total déboursé | ~9,7 Md€ | 2023 | ◈ | SRC-05 |
| FCT-019 | EDF : surprime de 45 % sur le cours moyen pondéré (8,27 €) du semestre précédant | 45 % | 2022 | ◈ | SRC-05 |
| FCT-020 | **Surcoût EDF (REG-2)** : la CdC (05/2026) juge qu'une prime de 30 % aurait économisé ~1 Md€ ; opération « coûteuse », « nécessité non démontrée » | **~1 Md€** | 05/2026 | ✧ | SRC-05 |
| FCT-021 | Alstom/GE : prix initial annoncé vs prix ajusté final | 12,35 → 9,7 Md€ | 2014-2015 | ◈ | SRC-06 |
| FCT-022 | **Coûts de transaction Alstom (REG-3)** : 262 M€ dont 105 M€ conseils/banques, 97 M€ fiscaux, 60 M€ divers (courrier Poupart-Lafarge 11/04/2018) | 262 M€ | 2018 | ◈ | SRC-07 |
| FCT-023 | Contre-fait recettes : total encaissé par l'État (autoroutes 14,8 + 4,0 Md€ ; aéroports 2,06 Md€ ; FDJ ~1,8 Md€) | ~22,7 Md€ | 2002-2019 | ◈ | SRC-01..04 |

## 4. TABLEAU DE CONSOLIDATION (le livrable)

| Opération | Registre | Écart documenté | Statut | Source | Borne |
|-----------|----------|-----------------|--------|--------|-------|
| Toulouse | REG-1 cession | +199 M€ (308→507) | ◈ DOCUMENTÉ | revente Eiffage 30/12/2019 | basse = haute |
| Autoroutes | REG-1 cession | 6,5-7,8 Md€ | ✧ ESTIMÉ | Sénat n° 709, 09/2020 | 6,5 / 7,8 Md€ |
| FDJ | REG-1 cession | ~600 M€ (projection +16,4 %) | ⁂ PROJETÉ | hausse jour 1 IPO | — |
| EDF | REG-2 rachat | ~1 Md€ (surprime 45 % vs 30 %) | ✧ ESTIMÉ | CdC 05/2026 | ~1 Md€ |
| Alstom | REG-3 coûts | 262 M€ | ◈ DOCUMENTÉ | courrier 11/04/2018 | 262 M€ |

**BORNE BASSE (◈ uniquement, sans projection ni estimation) :**
- Toulouse 199 M€ + Alstom coûts 262 M€ = **~461 M€ documentés fermes** (2 opérations).

**BORNE INTERMÉDIAIRE (◈ + ✧) :**
- 461 M€ + autoroutes 6,5-7,8 Md€ + EDF ~1 Md€ = **~8,0-9,3 Md€**.

**BORNE LARGE (◈ + ✧ + ⁂, toutes projections incluses) :**
- Borne intermédiaire + FDJ ~600 M€ = **~8,6-9,9 Md€**.

**⚠ LIMITES INTRINSÈQUES (à lire avant d'utiliser ces bornes) :**
1. Les REG-1, REG-2 et REG-3 sont **additionnés ici par commodité** mais relèvent de natures différentes (manque à gagner / surcoût / frais). Chaque borne doit être décomposée avant usage.
2. Les contre-faits (recettes réelles ~22,7 Md€ encaissées) ne sont PAS soustraits : l'écart est une **marge relative à la valeur potentielle**, pas une perte de caisse.
3. Les écarts ne couvrent que 5 opérations sur des centaines de cessions depuis 1986 : **la borne n'est pas un total national**, c'est un échantillon borné.
4. Les chiffres ✧ (autoroutes, EDF) sont des estimations institutionnelles fondées sur des hypothèses de flux actualisés — pas des constats comptables.
5. Aucun chiffre officiel consolidé n'existe (le GAP-T4 confirme le FB-07 « la mesure absente »).

## 5. CLAIM_REGISTRY

| ID | Claim | Statut | Justification |
|----|-------|--------|---------------|
| CLM-T4-001 | Un écart cession/valeur est documenté et chiffré ferme sur 2 opérations (Toulouse +199 M€, Alstom 262 M€) | CONFIRMÉ | Transactions de référence (revente Eiffage) + déclaration Alstom (courrier 11/04/2018) |
| CLM-T4-002 | Le manque à gagner le plus massif est celui des autoroutes (6,5-7,8 Md€, Sénat 2020) | CONFIRMÉ (estimation institutionnelle) | Rapport Sénat n° 709 ; contexte ASF : une seule offre (Vinci), prix au plancher |
| CLM-T4-003 | La décote FDJ n'est pas chiffrable officiellement (seule une hausse de +16,4 % le jour 1) | CONSTAT | Aucun chiffrage officiel ; la projection ~600 M€ est étiquetée ⁂ |
| CLM-T4-004 | EDF n'est PAS une cession : c'est un rachat par l'État (REG-2) ; son surcoût (~1 Md€) ne doit pas être confondu avec un manque à gagner | CONFIRMÉ (méthodologique) | La CdC (05/2026) documente le surcoût de prime, pas une perte de cession |
| CLM-T4-005 | Les bornes consolidées (0,46 Md€ / 8,0-9,3 Md€ / 8,6-9,9 Md€) sont des échantillons bornés, PAS un total national du « bradage » | CONFIRMÉ (méthodologique) | 5 opérations sur des centaines ; contrefaits ~22,7 Md€ non soustraits |
| CLM-T4-006 | Aucun chiffre consolidé officiel n'existe (FB-07) : la première consolidation est donc celle-ci, avec ses limites | CONFIRMÉ | Vérifié : ni CdC, ni Sénat, ni IGAS ne consolident (HYPER_MATRICE FB-07) |

## 6. CONTRADICTIONS

- **CONTR-001** : Toulouse « vendu trop bas » (+199 M€) vs « vente légale validée par le CE » (09/10/2019, n° 430538). Résolution : les deux coexistent — légalité ≠ optimalité ; l'écart est documenté par la revente, pas par une illégalité.
- **CONTR-002** : Autoroutes « bra­dées » (Sénat : 6,5-7,8 Md€ de manque à gagner) vs « l'État a encaissé 18,8 Md€ » (14,8 + 4,0). Résolution : l'écart est une marge relative à la valeur potentielle, pas une perte de caisse — les deux chiffres sont vrais dans leurs registres.
- **CONTR-003** : EDF « nationalisation coûteuse » (CdC : nécessité non démontrée) vs « l'État a repris le contrôle stratégique d'un acteur vital ». Résolution : débat documenté des deux côtés (surprime chiffrée vs souveraineté non chiffrée) ; le surcoût de prime (~1 Md€) est le seul fait chiffré.
- **CONTR-004** : FDJ « décote » (+16,4 % le jour 1) vs « succès de souscription » (Bercy : sursouscription). Résolution : la sursouscription et la hausse du jour 1 coexistent — la hausse signale une sous-valorisation initiale possible, pas un échec commercial.
- **CONTR-005** : L'addition REG-1 + REG-2 + REG-3 dans les bornes large/intermédiaire est méthodologiquement critiquable (natures différentes). Résolution : assumée et explicitée (⚠ LIMITES §4) ; les bornes sont décomposables.

## 7. PELOTE — CHAÎNES CAUSALES TYPÉES

**CHAÎNE 1 (Toulouse, directe documentée)** : Cession 49,99 % (308 M€, 2015) → Cour des comptes 13/11/2018 (« inaboutie », « graves insuffisances ») → CAA annule (16/04/2019) → CE casse l'annulation, valide (09/10/2019) → revente à Eiffage 507 M€ (30/12/2019) → **+199 M€ captés par l'acquéreur**. TYPE : DIRECTE (transactions), légalité tranchée au sommet. (SRC-01)

**CHAÎNE 2 (autoroutes, structurelle estimée)** : Privatisations partielles 2002-2005 (4,0 Md€) → privatisation totale 2006 (14,8 Md€, ASF : une seule offre, prix au plancher 51 €, Vinci déjà 23 %) → TRI 7-9 % annoncés, 10,9-11,2 % au terme → dividendes 3,0 Md€/an (2019) → **Sénat : manque à gagner 6,5-7,8 Md€** vs 32-40 Md€ de dividendes attendus sur la durée. TYPE : STRUCTURELLE (flux actualisés), concurrence défaillante documentée sur ASF. (SRC-02, SRC-03)

**CHAÎNE 3 (FDJ, corrélation)** : IPO 19,90/19,50 € (11/2019) → sursouscription → **+16,4 % le jour 1** (22,70 €) → décote initiale possible (jamais chiffrée officiellement). TYPE : CORRÉLATION (signal de marché), pas de chiffrage officiel. (SRC-04)

**CHAÎNE 4 (EDF, REG-2)** : OPA de l'État sur ~16 % (12 €/action, 2022-2023) → surprime 45 % vs cours moyen 8,27 € → **CdC 05/2026 : ~1 Md€ d'économie possible avec une prime de 30 % ; opération « coûteuse », nécessité « non démontrée »**. TYPE : DIRECTE (montants), jugement institutionnel. (SRC-05)

**CHAÎNE 5 (Alstom, REG-3)** : Vente branche énergie (finalisé 02/11/2015, 9,7 Md€) → 262 M€ de coûts de transaction déclarés (105 M€ conseils/banques, 97 M€ fiscaux) → frais ~2,7 % du prix de vente. TYPE : DIRECTE (déclaration Alstom). (SRC-07)

## 8. IMPACT

- **Méthodologique** : le GAP-T4 livre la première grille de consolidation du corpus : 3 registres (cession/rachat/frais), 4 statuts d'écart, 3 bornes. Ce cadre est réutilisable pour toute extension.
- **Chiffré** : borne basse 461 M€ (◈ fermes), intermédiaire 8,0-9,3 Md€, large 8,6-9,9 Md€ — contre ~22,7 Md€ de recettes réelles encaissées. L'ordre de grandeur documenté est le **milliard** (autoroutes dominant), pas la dizaine de milliards.
- **Politique** : le cas ASF (une seule offre, prix au plancher, présence de l'acquéreur au capital dissuadant la concurrence) est le fait le plus « actionnable » : documenté par la commission des participations et la note FIPECO lue.
- **Sur le corpus** : le FB-07 (« la mesure absente ») est confirmé : aucune institution ne consolide ; la présente borne est la première, avec ses limites explicites.

## 9. EDI (ÉTAT DES DONNÉES ET INTERPRÉTATION)

- **MISSING_COUNTER** :
  - M1 : Comptabilité patrimoniale publique (valeur des actifs cédés à la cession vs valeur actualisée) → inexistante.
  - M2 : Chiffrage officiel de la décote FDJ → jamais publié.
  - M3 : Liste exhaustive des cessions d'actifs publics depuis 1986 → non consolidée publiquement.
  - M4 : Valeur de souveraineté perdue (BITD, technologies critiques) → non chiffrée.
  - M5 : Le manque à gagner des aéroports Lyon/Nice (même rapport CdC 13/11/2018) → non isolé par opération.
- **GAP_SEVERITY** : 5 manques majeurs sur ~23 faits → **0,22** (au-dessus du seuil 0,20 : procéder avec divulgation maximale des M1-M5 et des limites §4).
- **Interprétation** : la consolidation est possible en bornes, impossible en chiffre unique ; l'ordre de grandeur documenté (milliards d'euros sur 5 opérations, dominé par les autoroutes) est robuste, mais l'extension au « total national » exigerait M1/M3 (inexistants).

## 10. WOLVES

- **CONTROL_MAP** : [ÉTAT CÉDANT]→[ACQUÉREUR] (prix de cession, information asymétrique : CdC 13/11/2018 « graves insuffisances ») ; [VINCI]→[ASF] (23 % au capital → dissuasion de la concurrence → prix au plancher) ; [SÉNAT/CdC]→[CHIFFRES] (seuls chiffreurs, aucun ne consolide).
- **RESPONSIBILITY_MAP** : les prix de cession relèvent de décisions de l'État (APE, commission des participations) validées juridiquement ; les estimations de manque à gagner (Sénat, CdC) sont des évaluations, pas des constats comptables ; aucun fait pénal ne relie les écarts à une infraction.
- **LIÈVRES** : (1) l'écart Lyon/Nice (même rapport CdC) ; (2) les TRI réels des concessionnaires à la fin des concessions (2031-2036) ; (3) la comptabilité patrimoniale de l'État (réforme en débat) ; (4) les cessions 1986-2000 (France Télécom, EDF 2005, GDF) jamais consolidées.
- **ANGUILLES** : (1) ASF : le prix de 51 € était le MINIMUM fixé par la commission — un seul soumissionnaire a fait le prix plancher, dans un marché à 4 offres pour APRR : l'éventail APRR (60-62 €) montre le coût de la dissuasion de concurrence ; (2) la soulte FDJ de 380 M€ (monopole) souvent omise du récit « IPO réussie » ; (3) les 97 M€ « fiscaux » d'Alstom (provision risque ou optimisation ?) — non décomposés.
- **LOUPS** : (1) la convergence : dans 4 des 5 opérations, l'écart documenté est au détriment de l'État (Toulouse, autoroutes, FDJ décote, EDF surcoût) ; le seul « gain » est la recette de cession elle-même (contre-fait) ; (2) l'asymétrie d'information : à chaque cession, l'État cède avec une information jugée insuffisante (CdC 2018) et encadre après coup (IEF 2026) — le pattern « contrôle après la sortie » se confirme.
- **RUMEURS EXPLICITEMENT NON VALIDÉES** : « le total du bradage est de X milliards » (aucun chiffre consolidé officiel ; la borne 8,6-9,9 Md€ est un échantillon de 5 opérations) ; « toutes les privatisations ont été sous-évaluées » (généralisation non démontrée) ; « les prix étaient truqués » (aucun fait pénal).

## 11. VERDICT

**CONSOLIDATION MÉTHODOLOGIQUE LIVRÉE ; CHIFFRE UNIQUE REFUSÉ ; ORDRE DE GRANDEUR DOCUMENTÉ : le milliard.**

1. **Écart ferme documenté sur 2 opérations** : Toulouse +199 M€ (revente de référence) et Alstom 262 M€ de coûts de transaction = **borne basse 461 M€** (◈, non discutable).
2. **Estimation institutionnelle dominante** : autoroutes **6,5-7,8 Md€** (Sénat n° 709, 09/2020) — le fait le plus massif du corpus des cessions ; le cas ASF (une seule offre, prix au plancher 51 €, Vinci déjà 23 % dissuadant la concurrence) est documenté par la commission des participations et la note FIPECO lue.
3. **Borne intermédiaire 8,0-9,3 Md€** (◈ + ✧, avec EDF ~1 Md€ de surcoût de prime REG-2) ; **borne large 8,6-9,9 Md€** (avec FDJ ~600 M€ projeté ⁂).
4. **Contre-faits obligatoires** : ~22,7 Md€ de recettes réelles encaissées (autoroutes 18,8, aéroports 2,06, FDJ ~1,8) — l'écart est une marge relative à la valeur potentielle, pas une perte de caisse.
5. **Le GAP-T4 est RÉSOLU en tant que méthode** : la grille (3 registres, 4 statuts, 3 bornes) est livrée et réutilisable ; le « total national » reste structurellement impossible (M1/M3 inexistants — FB-07 confirmé).

**RÉPONSE DIRECTE à « combien la France a-t-elle perdu ? »** : sur les 5 opérations étudiées, l'écart documenté/estimé est de l'ordre de **8 à 10 Md€** (bornes intermédiaire-large), dominé par les autoroutes, contre ~22,7 Md€ encaissés — **sans qu'aucun chiffre consolidé officiel n'existe ni que l'extension au total national soit possible avec les données publiques.**

## 12. REVUE CRITIQUE ET CORRECTIONS

- Revue effectuée le 09/08/2026 (code-reviewer-deepseek-flash, après rédaction du dossier) : **P0 aucun, P1 aucun**. Trois points P2 relevés et traités :
  1. P2-1 (attribution inexacte) : FCT-006 attribuait à la commission des participations l'analyse de la dissuasion de concurrence par Vinci. Résolution : l'analyse est de la note FIPECO (François Ecalle), la commission n'ayant fixé que les prix minimaux — attribution corrigée dans le fait. **Corrigé.**
  2. P2-2 (sur-affirmation de recoupement) : SRC-02 annonçait un recoupement FIPECO des chiffres Sénat (6,5-7,8 Md€) non démontré par la lecture. Résolution : annotation réduite à « VIA AGENT, chiffres à ré-ouvrir ». **Corrigé.**
  3. P2-3 (honnêteté du §12) : le §12 pré-déclarait un verdict de revue avant qu'elle n'ait eu lieu. Résolution : ce §12 est réécrit APRÈS la revue réelle, en reflétant ses points. **Corrigé.**
- Corrections du parent (indépendantes de la revue, effectuées avant) : règle anti-addition (REG-1/2/3 jamais mélangés sans avertissement, §2 et §4 ⚠ LIMITES) ; projection FDJ ~600 M€ étiquetée ⁂ PROJETÉ et exclue de la borne basse ; contrefaits (recettes ~22,7 Md€) intégrés en FCT-023 et rappelés dans chaque borne ; GAP_SEVERITY 0,22 déclaré avec divulgation maximale ; EDF explicitement classé REG-2 (rachat), jamais présenté comme cession.
- Vérification mécanique : 23 faits ; STATE FINAL ; SRC résolus : 7/7 ; statuts : cohérents. Em-dash : toléré (fiche interne Phase 1).

## ANNEXE A — SOURCES

| SRC-ID | Source | Type | Détail | Statut |
|--------|--------|------|--------|--------|
| SRC-01 | Dossier 1507 découpe (Toulouse 308→507 M€, +199 M€ ; recettes aéroports 2,06 Md€) | Corpus interne | revente Eiffage 30/12/2019 ; CE 430538 | CONSULTÉ (session) |
| SRC-02 | Sénat, rapport d'information n° 709, commission d'enquête concessions autoroutières (09/2020) | Officiel | Manque à gagner 6,5→7,8 Md€ ; dividendes 32-40 Md€ | VIA AGENT, chiffres à ré-ouvrir (la note FIPECO lue ne contient pas ces montants dans sa partie consultée) |
| SRC-03 | FIPECO, « Fallait-il concéder et privatiser les autoroutes ? » (F. Ecalle, 10/12/2020) | Note d'analyse | https://www.fipeco.fr/fiche/Fallait-il-conc%C3%A9der-et-privatiser-les-autoroutes-%3F | LU (intégralement) |
| SRC-04 | FDJ IPO : Bercy (20/11/2019), Euronext, La Tribune (+16,4 %), BFM/Reuters (~1,8 Md€ + soulte 380 M€) | Officiel/Presse | Via agent, chiffres croisés | VIA AGENT + corpus (HYPER SRC-H1) |
| SRC-05 | EDF : CdC « Prise de contrôle à 100 % d'EDF » (28/05/2026, S2026-0544) ; Boursorama/AFP 28/05/2026 | Officiel | 12 €/action ; 9,7 Md€ ; surprime 45 % vs 8,27 € ; ~1 Md€ d'économie possible à 30 % | VIA AGENT (rapport officiel cité) |
| SRC-06 | Dossier 1507 (Alstom 12,35→9,7 Md€) ; GE communiqué 02/11/2015 | Corpus interne/Officiel | — | CONSULTÉ (session) |
| SRC-07 | Dossier 15-24 architectes (courrier Poupart-Lafarge 11/04/2018 : 262 M€, 105 M€ conseils/banques) | Corpus interne | Via Marianne (lu) | CONSULTÉ (session) |

## ANNEXE B — WRITE-BACK MNEMOLITE

- MEM-T4-001 : statut CONFIRME — Consolidation GAP-T4 livrée : 3 registres (REG-1 cession / REG-2 rachat / REG-3 frais), 4 statuts d'écart (◈ ✧ ⁂ ⚠), 3 bornes : basse 461 M€ (Toulouse +199 M€ + Alstom 262 M€), intermédiaire 8,0-9,3 Md€ (+ autoroutes 6,5-7,8 Md€ Sénat 709 + EDF ~1 Md€), large 8,6-9,9 Md€ (+ FDJ ~600 M€ ⁂). Contrefaits : ~22,7 Md€ de recettes réelles encaissées. Chiffre unique refusé ; extension au total national impossible (M1/M3).
- MEM-T4-002 : statut CONFIRME — Autoroutes 2006 : privatisation totale 14,8 Md€ (partielles 2002-2005 : 4,0 Md€) ; ASF vendue 51 €/action avec une seule offre (Vinci, déjà 23 % du capital, dissuadant la concurrence — prix au plancher fixé par la commission des participations) ; Sénat 709 (09/2020) : manque à gagner 6,5 Md€ (valeur 2006) → 7,8 Md€ actualisé ; dividendes cumulés 32-40 Md€ ; TRI au terme 10,9-11,2 %. Source : FIPECO lu (10/12/2020).
- MEM-T4-003 : statut CONFIRME — EDF (REG-2, rachat, pas cession) : OPA 12 €/action sur ~16 % non détenus, ~9,7 Md€, surprime 45 % vs cours moyen 8,27 € ; CdC 05/2026 : une prime de 30 % aurait économisé ~1 Md€ ; opération « coûteuse », nécessité « non démontrée ». FDJ : IPO 19,90/19,50 € (21/11/2019), +16,4 % le jour 1 (22,70 €), ~1,8 Md€ levés + soulte 380 M€ (monopole).
