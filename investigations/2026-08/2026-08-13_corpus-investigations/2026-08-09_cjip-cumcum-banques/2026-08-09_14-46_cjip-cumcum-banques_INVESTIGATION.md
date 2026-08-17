# INVESTIGATION APEX (SUIVI) : ISSUE DES NÉGOCIATIONS CJIP CUMCUM (BNP PARIBAS, SOCIÉTÉ GÉNÉRALE, NATIXIS) ET CHIFFRAGE DE LA RÉCUPÉRATION TOTALE

## RUN_MANIFEST (FINAL)

```
ENGINE_VERSION : 2.8
STATE          : FINAL
RUN_ID         : 20260809-1446-cjip-cumcum-banques
PARENT_RUN_ID  : 20260809-1416-cumcum-cumex-france (branche du FCT-015 / GAP-003 du dossier cumcum)
AS_OF          : 2026-08-09
INPUT_KIND     : UPDATE (suivi de l'issue des négociations CJIP ; résolution partielle du GAP-003 parent)
MISSION_MODE   : INVESTIGATION
INPUT_REF      : NONE (topique : « suivre l'issue des négociations CJIP pour BNP Paribas, Société Générale et Natixis, et chiffrer la récupération totale finale »)
SUBJECT_SLUG   : cjip-cumcum-banques
INVESTIGATION_PATH : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_cjip-cumcum-banques/2026-08-09_14-46_cjip-cumcum-banques_INVESTIGATION.md
SCOPE          : état au 09/08/2026 des négociations CJIP CumCum des 5 établissements perquisitionnés le 28/03/2023 (BNP Paribas, Exane, Société Générale, Natixis, HSBC) ; total des sommes négociées et encaissables ; redressements DGFiP engagés ; ratio récupération/estimation ; période 2023-2026
COMPLEXITY     : CX_SCORE=9 → $CX=COMPLEX (political 2, technical 2, temporal 2, geo 1, narratives 1, data 1)
CHECKPOINT_SEQ : 0 (run mono-session)
LAST_COMPLETED : 15
NEXT_ACTION    : NONE
RESUME_COUNT   : 0
ROUTE_OVERRIDES: []
LOADED_MODULES : KERNEL v2.8 | SYMBOLS | PATTERNS | THREATS | GATES | REQUEST_LOG | EPISTEMIC | TEMPLATE (héritage parent revalidé)
DEGRADED_FLAGS : []
HASH_CAPABILITY: HASH_UNAVAILABLE
```

## 1. RÉSUMÉ EXÉCUTIF

**Réponse à l'OBJECT_QUESTION** (« où en sont les négociations CJIP de BNP Paribas, Société Générale et Natixis, et combien la France récupère-t-elle au total ? ») :

**Aucune CJIP n'a été signée postérieurement au 08/01/2026.** Au 09/08/2026, exactement **2 des 5 établissements perquisitionnés** (28/03/2023) ont soldé leur dossier par CJIP : **Crédit Agricole CIB 88,2 M€ (08/09/2025)** et **HSBC 267,5 M€ (08/01/2026)** = **355,7 M€ négociés à date** (FCT-002, calcul vérifié). Les **trois autres banques (BNP Paribas, Société Générale, Natixis) demeurent dans l'expectative** : c'est le constat de la source la plus récente identifiée (cabinet Kohen Avocats, 19/06/2026, FCT-004 à 007) et rien de postérieur n'a été trouvé à la date du dossier.

1. **État des négociations par établissement** :
   - **HSBC** : CJIP signée le 08/01/2026, 267,5 M€ = **115 M€ de préjudice** (finances publiques) + **152 M€ de pénalités** (décomposition confirmée par Actu-Juridique 11/05/2026, lu intégralement, FCT-003), + programme de mise en conformité.
   - **Crédit Agricole** : CJIP homologuée 08/09/2025, 88,2 M€ (2 500 opérations 2013-2021, gains 49 M€, parent FCT-013).
   - **BNP Paribas** : pas de CJIP ; la banque **conteste un redressement CumCum d'environ 250 M€** (presse financière internationale, 24/06/2025, FCT-004) et reste dans l'expectative (FCT-005).
   - **Société Générale** : pas de CJIP, dans l'expectative (FCT-006) ; à ne pas confondre avec le contentieux fiscal distinct tranché par le CE le 03/12/2025 (n° 451466 : rappels de retenue à la source sur revenus réputés distribués à filiales étrangères, 23,75 M€) qui n'est pas une CJIP CumCum (FCT-006, CONTR-001).
   - **Natixis (BPCE)** : pas de CJIP, dans l'expectative (FCT-007).
2. **Le chiffrage de la récupération totale finale** (LEAD_QUESTION) : **deux registres, étiquetés distinctement** :
   - **Négocié et engagé à date** : 355,7 M€ de CJIP + **~4,5 Md€ de redressements CumCum engagés par la DGFiP** (audition É. Lombard 07/2025, parent FCT-007 ; « engagés » ≠ « encaissés », les redressements peuvent être contestés — c'est le cas de BNP).
   - **Projection conditionnelle (extrapolation, jamais mesure)** : si les 3 banques restantes concluaient des CJIP du même ordre que HSBC (267,5 M€) ou Crédit Agricole (88,2 M€), le total des CJIP passerait de 0,36 Md€ à **~0,9-1,6 Md€** (fourchette 3×88,2 à 3×267,5 M€ + 355,7 M€, FCT-012, ⁂).
   - **Ratio récupération/estimation** : contre le manque à gagner estimé de **33 Md€ cumulés** (Mannheim, contesté), les 355,7 M€ de CJIP représentent **~1,1 %** de l'estimation ; même en ajoutant les 4,5 Md€ de redressements engagés, on reste sous ~15 % de l'estimation académique (FCT-013, calcul).

**Verdict sur le LEAD_QUESTION** (« peut-on chiffrer la récupération totale finale ? ») : **PARTIELLEMENT SOUTENU** : le total des CJIP est désormais un fait mesuré (355,7 M€, arrêté au 08/01/2026, aucune transaction postérieure identifiée), mais le **GAP-003 parent est résolu partiellement seulement** : l'état des négociations est connu (3 banques en expectative), les **montants finaux des 3 banques restantes restent inconnus** (confidentiels, négociations en cours) et les redressements engagés (~4,5 Md€) ne sont pas des encaissements. La « récupération totale finale » ne peut donc pas être un chiffre unique : c'est une fourchette 0,36 Md€ (acquis) à ~6 Md€ (hypothèse haute incluant redressements encaissés), soit **1 à 18 % de l'estimation de la perte** (FCT-012/013).

**Acteurs** : PNF (signataire CJIP), DGFiP/Bercy (redressements), 5 banques (BNP Paribas + Exane, Société Générale, Natixis, Crédit Agricole, HSBC), FBF (lobby), Conseil d'État (jurisprudence), législateur (LF 2025).

## 2. MANIPULATION_REPORT (15 symboles scorés sur corpus)

| # | Symbole | Score | Justification (corpus) |
|---|---------|-------|------------------------|
| 1 | **Ξ** omission | **7/10** | Aucune communication officielle sur l'état des négociations des 3 banques restantes ; les montants par banque sont confidentiels ; le total des encaissements réels de redressements n'est pas publié ; une CJIP signée entre juin et août 2026 n'est pas impossible (non-retrouvée, pas inexistante). |
| 2 | **€** money | **8/10** | 88,2 + 267,5 = 355,7 M€ (mesuré) ; ~250 M€ redressement BNP contesté ; ~4,5 Md€ redressements engagés ; 23,75 M€ CE 451466 ; projection 0,9-1,6 Md€ (⁂). |
| 3 | **Λ** framing | 6/10 | « Négociations » vs « expectative » ; « paiement volontaire » (banques) vs « amende d'intérêt public » (PNF) ; « solde des poursuites » vs « abandon des poursuites » ; la CJIP est présentée par les banques comme une clôture, par le PNF comme une sanction. |
| 4 | **Ω** inversion | **7/10** | Les banques invoquaient la « zone grise de l'optimisation fiscale » comme défense ; la LF 2025 a rendu ce registre inopérant, et les CJIP (qui comportent une reconnaissance implicite de l'illégalité) fragilisent rétroactivement cette défense (Kohen, FCT-008). |
| 5 | **Ψ** sidération | 2/10 | Champ froid, technique. |
| 6 | **↕** verticalité | **8/10** | CJIP = l'établissement paie, aucune personne physique jugée ; 33 Md€ estimés vs 355,7 M€ négociés ; les banques globales négocient, le contribuable subit la perte antérieure. |
| 7 | **Φ** spectacle | 3/10 | Annonces CJIP = pics médiatiques brefs ; pas de procès public. |
| 8 | **Σ** sémiotique | 3/10 | Faible ; « la place financière » comme cadre de défense. |
| 9 | **Κ** cynisme | **7/10** | Deux CJIP soldeuses en 5 mois après 6 ans de blocage législatif ; le législateur (LF 2025) a dû qualifier l'illégalité pour rendre la défense bancaire inopérante ; les redressements annoncés (4,5 Md€) sont très supérieurs aux transactions pénales (0,36 Md€). |
| 10 | **ρ** résistance | 6/10 | PNF, DGFiP, Sénat, presse financière (Bloomberg, Actu-Juridique), cabinets d'avocats documentant la bascule. |
| 11 | **κ** influence subtile | 6/10 | La FBF a obtenu l'annulation partielle de la doctrine (CE 472587) ; le calendrier des CJIP (2 signées, 3 en attente) peut refléter des rapports de force, non documentés. |
| 12 | **⫸** convergence | **7/10** | Les sources convergent sur l'expectative des 3 banques : Actu-Juridique (11/05/2026), Kohen (19/06/2026), Bloomberg (24/06/2025). |
| 13 | **⚔** guerre cognitive | 1/10 | Aucune opération documentée. |
| 14 | **🌐** réseau | 6/10 | PNF, parquet de Cologne, 5 banques, DGFiP, FBF, Conseil d'État. |
| 15 | **⏰** temporalité | **7/10** | 28/03/2023 perquisitions → 12/2023 CE 472587 → 02/2025 LF 2025 → 09/2025 CJIP CA → 01/2026 CJIP HSBC → 06/2026 encore 3 banques en expectative : le « dégel » pénal se fait au compte-gouttes. |

**BIAS TEST (15/15 scorés).** Aucun symbole au-delà de 8. Le champ Ξ=7 signale la possibilité d'une transaction intervenue entre juin et août 2026 sans couverture accessible : déclarée en PÉRIMÈTRE & LIMITES.

**PATTERNS** : @PAT[ICEBERG] (Ξ=7), @PAT[MONEY] (€=8), @PAT[CYN] (Κ=7). **THREATS** : @THR[DARK_MONEY] (montants confidentiels), @THR[REG_CAPTURE] (FBF, annulation partielle doctrine).

## 3. CLUSTERS (routage SYMBOLS §4)

| Cluster | Diagnostic | Gap |
|---------|------------|-----|
| ICEBERG (Ξ=7) | Émergé : 355,7 M€ CJIP + 4,5 Md€ redressements engagés. Surface : 33 Md€ estimés. Immergé : transactions non publiées, montants par banque. | Une CJIP signée après le 19/06/2026 non détectée n'est pas exclue. |
| MONEY (€=8) | 2 flux : pénal (CJIP 355,7 M€) et fiscal (redressements ~4,5 Md€, dont ~250 M€ contestés par BNP). | Total encaissé non publié. |
| POWER (↕=8) | CJIP sans personnes physiques ; négociation entre pairs (banques globales vs PNF). | — |
| INVERSION (Ω=7) | « Zone grise » invoquée puis rendue inopérante par la loi ; CJIP = reconnaissance implicite. | — |
| TEMPORAL (⏰=7) | Séquence 2023-2026 : le pénal prend le relais du fiscal en 4 vagues. | Calendrier des 3 restantes inconnu. |

## 4. HERMÉNEUTIQUE (statut : ANALYSE)

- **L1 (texte) :** communiqués CJIP (CA, HSBC), article Actu-Juridique 11/05/2026 (lu intégralement), analyse Kohen Avocats 19/06/2026 (lue), presse financière (Bloomberg 24/06/2025), jurisprudence (CE 472587, 451466, série 423811/423812/438135/471147, CAA Paris 24PA02158, Cass. com. 23-14.047).
- **L2 (structure) :** deux temps : (a) le solde par CJIP des banques les plus exposées (CA, HSBC, 2025-2026) ; (b) l'expectative des trois autres, dont la position est dégradée par la loi et la doctrine intervenues entre-temps.
- **L3 (intérêt) :** la CJIP est devenue l'instrument de régulation du contentieux fiscal de masse : l'État échange une sanction rapide contre une reconnaissance implicite de l'illégalité, sans jugement des personnes physiques. Les 3 banques restantes ont intérêt à attendre (le quantum des CJIP précédentes fixe la référence), le PNF a intérêt à faire tomber des précédents (effet d'entraînement).
- **L4 (sémiotique) :** la « deuxième transaction » (titre Actu-Juridique) : le vocabulaire commercial (« transaction ») contraste avec la qualification pénale (blanchiment aggravé de fraude fiscale).
- **L5 (comparaison) :** cohérence avec le corpus parent : « les entreprises paient sans procès, les exécutants prennent » ; le ratio récupération/estimation (1-18 %) reproduit la signature du dossier enrichissement légalisé.
- **L6 (contexte) :** 2026 : besoin de recettes publiques, jurisprudence favorable à l'administration (CE 451466, 03/12/2025), dispositif LF 2025 en vigueur depuis le 01/01/2026.

**Lecture concurrente** : les banques restantes peuvent soutenir que leurs opérations étaient des prêts de titres légitimes et que leur dossier diffère de ceux soldés. La synthèse retenue : l'expectative est un fait documenté (3 sources indépendantes), le quantum final est un inconnu déclaré (GAP partiel).

## 5. FORENSIC REASONING (ICEBERG MAX)

**Émergé (mesuré, arrêté au 08/01/2026)** : CJIP CA 88,2 M€ + CJIP HSBC 267,5 M€ = 355,7 M€ ; redressements CumCum engagés ~4,5 Md€ (07/2025) ; redressement BNP contesté ~250 M€ (06/2025, ⚠️ source non relue directement).

**Surface (estimé, contesté)** : 33 Md€ cumulés (Mannheim) ; projections CJIP 0,9-1,6 Md€ (⁂) ; hypothèse haute récupération ~6 Md€ (incluant redressements encaissés, non vérifiés).

**Immergé (inféré)** : transactions entre 19/06/2026 et 09/08/2026 non publiées ; montants par banque (confidentiels) ; part des 4,5 Md€ effectivement encaissés.

**ICEBERG LOAD :** 5 strates émergées confirmées, 2 en surface, 3 inférées. La récupération totale est mesurable dans sa composante CJIP (355,7 M€) et non mesurable dans ses composantes fiscales (encaissements non publiés) et futures (3 banques).

## 6. PRISME DIALECTIQUE

- **Thèse (dominante) :** « La France solde le CumCum » : 2 CJIP en 5 mois, verrou législatif 2026, redressements massifs engagés.
- **Antithèse (critique) :** « La récupération reste symbolique » : 355,7 M€ négociés contre 33 Md€ estimés (~1,1 %), aucune personne physique jugée, 3 banques sur 5 non soldées, redressements contestables (BNP).
- **Arbitrage par les preuves :** la thèse est confirmée sur la trajectoire (2 CJIP, effet d'entraînement) ; l'antithèse est confirmée sur les ratios. **La synthèse** : la récupération est réelle et croissante, mais l'ordre de grandeur (Md€) reste sans commune mesure avec la perte estimée (dizaines de Md€), et le solde final dépend de négociations confidentielles en cours.

## 7. CHRONOLOGIE

| Date | Événement | Source | Statut |
|------|-----------|--------|--------|
| 28/03/2023 | Perquisitions PNF + parquet de Cologne : 5 établissements (BNP Paribas, Exane, Société Générale, Natixis, HSBC) | parent FCT-004 | ✦ |
| 08/12/2023 | CE n° 472587 (FBF) : annulation partielle de la doctrine « bénéficiaire effectif » | parent FCT-010 | ✦ |
| 14/02/2025 | LF 2025 (art. 96) : CumCum placés en illégalité explicite, applicable 01/01/2026 | parent FCT-011 | ✦ |
| 24/06/2025 | BNP Paribas conteste un redressement CumCum ~250 M€ | Bloomberg | ✦ |
| 07/2025 | Audition É. Lombard : redressements cumulés ~4,5 Md€ engagés | parent FCT-007 | ✦ |
| 08/09/2025 | CJIP Crédit Agricole CIB : 88,2 M€ (première) | parent FCT-013 | ✦ |
| 12/02/2025 | Cass. com. n° 23-14.047 : contrôle concret de la proportionnalité de la majoration d'abus de droit (80 %) | Kohen | ✦ |
| 03/12/2025 | CE n° 451466 (contentieux fiscal Société Générale, filiales étrangères : 23,75 M€) : vigilance accrue sur flux intragroupes | Kohen | ✦ |
| 08/01/2026 | CJIP HSBC : 267,5 M€ (115 M€ préjudice + 152 M€ pénalités) | Le Monde, Actu-Juridique | ✦ |
| 16/03/2026 | BOFiP BOI-INT-DG-20-20-20-30 mis à jour (bénéficiaire effectif, résident) | Kohen/BOFiP | ✦ |
| 17/03/2026 | CAA Paris (Aaxen, n° 24PA02158) : décharge RAS pour structure à substance réelle (équilibre du dispositif) | Kohen | ✦ |
| 11/05/2026 | Actu-Juridique : « deuxième transaction » (HSBC) ; 4 autres banques dans le viseur de Bercy et du PNF | Actu-Juridique (lu) | ✦ |
| 19/06/2026 | Kohen Avocats : BNP Paribas, Exane, Société Générale, Natixis « demeurent dans l'expectative » | Kohen (lu) | ✦ |
| 09/08/2026 | Aucune CJIP postérieure au 08/01/2026 identifiée (vérification à date du dossier) | ce dossier | ⁅ |

## 8. DOMAINES (par axe)

| Axe | Question | Résultat clé | Faits | Statut |
|-----|----------|--------------|-------|--------|
| AXS-001 ÉTAT NÉGOCIATIONS | Où en sont les 5 établissements ? | 2 soldées par CJIP (CA, HSBC) ; 3 en expectative (BNP/Exane, SocGen, Natixis) ; aucune CJIP postérieure au 08/01/2026 | FCT-001 à 007 | SATURATED (à date) |
| AXS-002 RÉCUPÉRATION TOTALE | Combien la France récupère-t-elle ? | 355,7 M€ CJIP (mesuré) + ~4,5 Md€ redressements engagés ; projection 0,9-1,6 Md€ (⁂) ; ratio 1,1 % vs 33 Md€ | FCT-002/012/013 | SATURATED (partiel, GAP montants banques) |
| AXS-003 CADRE JURIDIQUE | Qu'est-ce qui pousse les banques à négocier ? | LF 2025 + BOFiP 03/2026 + jurisprudence CE/CAA/Cass. : la défense « zone grise » est inopérante | FCT-008 à 011 | SATURATED |

## 9. RÉSEAU D'ACTEURS (+ CONTROL_MAP)

| Acteur | Rôle | Action documentée | Preuve | Responsabilité |
|--------|------|-------------------|--------|----------------|
| PNF | Pénal | Signataire des CJIP (CA, HSBC) ; enquêtes en cours sur les 3 autres | FCT-001/002 | ρ |
| DGFiP/Bercy | Fiscal | Redressements ~4,5 Md€ engagés ; ~250 M€ contestés par BNP | FCT-004, parent FCT-007 | ROLE |
| Crédit Agricole CIB | Établissement | CJIP 88,2 M€ (09/2025) | parent FCT-013 | Réglé |
| HSBC | Établissement | CJIP 267,5 M€ (01/2026) + mise en conformité | FCT-003 | Réglé |
| BNP Paribas / Exane | Établissements | Expectative ; conteste ~250 M€ | FCT-004/005 | Négociation en cours |
| Société Générale | Établissement | Expectative ; contentieux fiscal distinct (CE 451466, 23,75 M€) | FCT-006 | Négociation en cours |
| Natixis (BPCE) | Établissement | Expectative | FCT-007 | Négociation en cours |
| FBF | Lobby | Annulation partielle doctrine (CE 472587, 2023) | parent FCT-016 | Influence passée |
| Conseil d'État, CAA, Cass. | Juridictions | Série 2020-2026 : bénéficiaire effectif, proportionnalité | FCT-010/011 | ρ |

**CONTROL_MAP** :

| Contrôleur | Mécanisme | Résultat | Gap |
|------------|-----------|----------|-----|
| CTRL-001 PNF (CJIP) | Négociation pénale conventionnelle | 355,7 M€ (2/5 banques) | 3 banques non soldées ; quantum confidentiel |
| CTRL-002 DGFiP (redressements) | Contrôle fiscal | ~4,5 Md€ engagés | Encaissements non publiés ; contentieux (BNP ~250 M€) |
| CTRL-003 Loi + doctrine | LF 2025 + BOFiP 03/2026 | Défense « zone grise » inopérante | Effet rétroactif discuté (L80 A LPF, CE 472587) |

## 10. CHAÎNES / PELOTE (causalité)

**CAU-001 : La LF 2025 a neutralisé la défense des banques restantes.**
Étage 1 : LF 2025 art. 96 (illégalité explicite des CumCum, appl. 01/01/2026, parent FCT-011). Étage 2 : BOFiP BOI-INT-DG-20-20-20-30 (16/03/2026) précisant bénéficiaire effectif et résidence (FCT-009). Étage 3 : la défense « zone grise de l'optimisation » devient inopérante, accroissant le coût d'attente des 3 banques (Kohen, FCT-008). Type : SYSTÈME. Confidence : high sur les étages 1-2, medium sur l'effet causal direct (pas de mesure).

**CAU-002 : Les CJIP créent un effet d'entraînement sur les banques non soldées.**
Étage 1 : CJIP CA (09/2025) puis HSBC (01/2026) avec reconnaissance implicite de l'illégalité (FCT-002/003). Étage 2 : ces précédents fragilisent les contentieux fiscaux pendants des autres établissements (Kohen, FCT-008). Étage 3 : BNP, SocGen, Natixis restent en expectative (FCT-004 à 007). Type : MÉCANISME. Confidence : high sur les étages 1-2, la causalité sur l'issue finale (étage 3) est non mesurable.

**CAU-003 (extrapolation étiquetée) : « Si les 3 banques concluent des CJIP du même ordre, le total passerait à ~0,9-1,6 Md€. »**
Hypothèse : 3 × (88,2 à 267,5 M€) + 355,7 M€ = 620,3 M€ à 1 158,2 M€ (FCT-012, ⁂). Counter : les montants peuvent être inférieurs (poids différent des opérations) ou supérieurs (effet dissuasif renforcé). Type : PROJECTION (non mesuré). Confidence : low.

**CAU-004 (rejetée) : « Les redressements engagés (~4,5 Md€) sont des sommes recouvrées. »** RÉFUTÉE : « engagés » ≠ « encaissés » ; le contentieux est ouvert (BNP conteste ~250 M€, Bloomberg 06/2025) et l'annulation de la doctrine par le CE 472587 (2023) a montré la fragilité des bases doctrinales antérieures à 2025 (FCT-004, CONTR-002).

## 11. CARTE DES PREUVES

### CLAIM_REGISTRY

| ID | Claim | Support | Contre-évidence | Statut |
|----|-------|---------|-----------------|--------|
| CLM-001 | « Aucune CJIP CumCum n'a été signée après le 08/01/2026 » | Actu-Juridique 11/05/2026 (« deuxième transaction »), Kohen 19/06/2026 (3 banques en expectative) | Une transaction postérieure au 19/06/2026 sans couverture accessible n'est pas exclue | SOUTENU à date (vérif. 09/08/2026) |
| CLM-002 | « La récupération CJIP totale est de 355,7 M€ » | 88,2 (CA) + 267,5 (HSBC), calcul vérifié | Versements échelonnés possibles (parent FCT-014) | SOUTENU |
| CLM-003 | « BNP, Société Générale et Natixis n'ont pas soldé leur dossier » | Kohen 19/06/2026, Actu-Juridique 11/05/2026 | Absence de preuve ≠ preuve d'absence (limite Ξ=7) | SOUTENU (expectative) |
| CLM-004 | « La défense "zone grise" des banques restantes est inopérante depuis 2026 » | LF 2025 (illégalité explicite), BOFiP 03/2026, effet d'entraînement des CJIP | Contentieux antérieurs à 2025 peuvent se prévaloir du CE 472587 et de L80 A LPF | SOUTENU (partiel) |
| CLM-005 | « La récupération totale finale peut être chiffrée » | Composante CJIP mesurée (355,7 M€) | Encaissements de redressements non publiés ; montants des 3 banques confidentiels | PARTIELLEMENT SOUTENU (fourchette, pas de chiffre unique) |
| CLM-006 | « Le redressement de ~250 M€ de BNP a été payé » | — | Aucune source de paiement ; BNP le conteste (Bloomberg 06/2025) | NON PROUVÉ |

### FACT_REGISTRY (13 faits)

| ID | Fait | Chiffre | Source | Statut |
|----|------|---------|--------|--------|
| FCT-001 | État des négociations au 09/08/2026 : 2 CJIP signées (CA 08/09/2025, HSBC 08/01/2026) ; 3 établissements en expectative (BNP Paribas, Société Générale, Natixis) ; aucune CJIP postérieure au 08/01/2026 identifiée | 2/5 | SRC-01 Kohen 19/06/2026 ; SRC-02 Actu-Juridique 11/05/2026 | ✦ |
| FCT-002 | Total des CJIP signées : 88,2 + 267,5 = 355,7 M€ (calcul vérifié) | 355,7 M€ | SRC-02 ; parent FCT-013/014 | ✦ |
| FCT-003 | Décomposition CJIP HSBC (08/01/2026) : 115 M€ de préjudice aux finances publiques + 152 M€ de pénalités = 267,5 M€ ; + programme de mise en conformité | 115 + 152 M€ | SRC-02 (lu intégralement) ; SRC-01 | ✦ |
| FCT-004 | BNP Paribas : pas de CJIP ; conteste un redressement CumCum d'environ 250 M€ | ~250 M€ | SRC-03 Bloomberg 24/06/2025 (via agent, non relu à la source) | ✦ ⚠️ |
| FCT-005 | Exane (filiale de BNP Paribas) : perquisitionnée le 28/03/2023, toujours dans l'expectative, aucune CJIP | — | SRC-01 | ✦ |
| FCT-006 | Société Générale : dans l'expectative, aucune CJIP CumCum ; contentieux fiscal distinct : CE 03/12/2025 n° 451466, rappels de retenue à la source sur revenus réputés distribués à filiales étrangères, 23,75 M€ (à ne pas confondre avec une CJIP) | 23,75 M€ | SRC-01 | ✦ |
| FCT-007 | Natixis (BPCE) : dans l'expectative, aucune CJIP | — | SRC-01 | ✦ |
| FCT-008 | La LF 2025 (art. 119 bis CGI réécrit, appl. 01/01/2026) place les CumCum en illégalité explicite, rendant la défense « zone grise de l'optimisation » inopérante ; les CJIP déjà conclues fragilisent les contentieux pendants des autres banques | — | SRC-01 ; SRC-02 ; parent FCT-011 | ✦ |
| FCT-009 | BOFiP BOI-INT-DG-20-20-20-30 mis à jour le 16/03/2026 : bénéficiaire effectif + statut de résident comme conditions d'exonération conventionnelle | — | SRC-01 | ✦ |
| FCT-010 | Jurisprudence 2020-2026 consolidant le « bénéficiaire effectif » : CE Euro Stockage n° 423811 et Atlantique Négoce n° 423812 (05/06/2020), UBS Asset Management Life n° 438135 (11/05/2021), Foncière Vélizy Rose n° 471147 (08/11/2024), CAA Paris Aaxen n° 24PA02158 (17/03/2026, décharge : équilibre avec structures légitimes) | — | SRC-01 | ✦ |
| FCT-011 | Cass. com. 12/02/2025 n° 23-14.047 : contrôle concret de la proportionnalité de la majoration d'abus de droit (80 %) exigé du juge | 80 % | SRC-01 | ✦ |
| FCT-012 | Projection conditionnelle (extrapolation, ⁂) : si les 3 banques restantes concluaient des CJIP de 88,2 à 267,5 M€ chacune, le total passerait à 620 M€ - 1 158 M€ (355,7 + 3×88,2 à 3×267,5) | 0,62-1,16 Md€ | calcul annexe (SRC-02/01) | ⁂ |
| FCT-013 | Ratio récupération/estimation : 355,7 M€ / 33 Md€ ≈ 1,1 % ; avec 4,5 Md€ de redressements engagés : < 15 % de l'estimation académique (calcul, périmètres différents) | 1,1 % | calcul (parent FCT-005/007) | ⁂ |

### CONTRADICTION_LEDGER

| ID | Contradiction | Résolution | Statut |
|----|---------------|------------|--------|
| CONTR-001 | CE 03/12/2025 n° 451466 (23,75 M€, contentieux fiscal Société Générale) vs « CJIP Société Générale » | Pas de confusion possible : l'arrêt est un contentieux administratif sur des rappels de retenue à la source (filiales étrangères), distinct de la négociation pénale CJIP ; aucune CJIP Société Générale n'existe à date | DOCUMENTÉE |
| CONTR-002 | « 4,5 Md€ de redressements engagés » (07/2025) vs « 355,7 M€ de CJIP » : pourquoi l'écart ? | Registres distincts : les redressements sont notifiés et contestables (BNP ~250 M€, CE 472587), les CJIP sont des sommes négociées et payées ; « engagés » ≠ « encaissés » | DOCUMENTÉE (non unifiée) |
| CONTR-003 | 33 Md€ estimés (Mannheim) vs récupération : la perte est-elle surévaluée ? | Estimations contestées par la FBF (parent CONTR-001) ; le ratio 1,1 % est un rapport de grandeurs, pas une preuve de sous-récupération | DOCUMENTÉE |

### EDI

```
geo:0.50 lang:0.85 strat:0.70 owner:0.60 persp:0.70 temp:0.80
EDI_raw = .25×.50 + .20×.85 + .20×.70 + .15×.60 + .15×.70 + .05×.80 = 0.6825
Pénalité : MISSING_COUNTER (-.10) : la parole des banques restantes (défense détaillée, mémoire) n'est pas matériellement présente ; les montants confidentiels.
EDI = 0.58 (NARROW-MEDIUM, écart déclaré vs cible APEX 0.80)
COV = 0.85 | IND = 0.60 (8 familles amont / 13 sources acceptées)
EDI* = .5×.58 + .3×.85 + .2×.60 = 0.665
Perspectives : ⟐ 4 | ⟐̅ 3 | 🌍 1 | 🎓 1 (Mannheim, hérité) | 🔥 1 (Actu-Juridique)
DECISIVE_CLAIM_COVERAGE : CLM-001 direct:OUI familles:3 counter:PARTIAL | CLM-002 direct:OUI familles:3 counter:FOUND | CLM-005 direct:OUI familles:3 counter:FOUND
DIAGNOSTIC_NOT_TRUTH
```

### TRACE_MATRIX (extrait)

| FCT | QRY | SRC | URL (référence) | Statut |
|-----|-----|-----|-----------------|--------|
| FCT-001/005/006/007/008/009/010/011 | QRY-001 | SRC-01 | kohenavocats.com/cumcum-cjip-fraude-fiscale-dividendes-2026/ (19/06/2026, lu) | ✦ |
| FCT-001/002/003 | QRY-001 | SRC-02 | actu-juridique.fr/fiscalite/fiscal-finances/fraude-cumcum-deuxieme-transaction-pour-une-banque-dans-le-viseur-de-bercy/ (11/05/2026, lu intégralement) | ✦ |
| FCT-004 | QRY-001 | SRC-03 | Bloomberg (24/06/2025), via agent ; non relu directement | ✦ |
| FCT-002/012/013 | QRY-002 | SRC-01/02 + calculs | ce dossier | ✦/⁂ |

## 12. CARTE DIALECTIQUE (scénarios + responsabilité)

| Scénario | Hypothèse | Support | Contre | Lecture |
|----------|-----------|--------|--------|---------|
| S1 « Solde total à venir » | Les 3 banques concluent des CJIP (effet d'entraînement) | CJIP CA + HSBC, LF 2025, BOFiP 03/2026 | Aucune CJIP depuis 5 mois ; BNP conteste | Possible, non daté |
| S2 « Solde partiel » | 1-2 banques concluent, 1-2 contestent devant le juge | BNP ~250 M€ contestés ; CE 472587 | Effet d'entraînement documenté | Retenue |
| S3 « Chiffrage impossible du total final » | Le total dépend de négociations confidentielles | Montants par banque non publiés | Composante CJIP mesurée (355,7 M€) | Retenue (fourchette, pas de chiffre unique) |

**IMPACT_MAP** :

| Acteur | Gain | Perte |
|--------|------|-------|
| Trésor français | 355,7 M€ CJIP + redressements engagés (~4,5 Md€, partiellement encaissables) | 33 Md€ estimés (fourchette) ; contentieux à soutenir |
| Banques soldées (CA, HSBC) | Sortie du risque pénal, certitude | Amendes 355,7 M€, réputation |
| Banques en expectative (BNP/Exane, SocGen, Natixis) | Délai, négociation du quantum | Risque accru (LF 2025, précédents), provisions, contentieux |
| Actionnaires étrangers | — | Perte du schéma (dispositif 2026) |

**RESPONSIBILITY_MAP** : aucune personne physique jugée ; les établissements paient sans reconnaissance pénale de culpabilité (CJIP) ou contestent (BNP). La responsabilité des négociations est partagée entre PNF (quantum), banques (stratégie), législateur (verrou 2025) et FBF (influence passée, CE 472587).

## 13. PÉRIMÈTRE & LIMITES

**Inclusions** : état des négociations CJIP CumCum des 5 établissements perquisitionnés ; total des sommes négociées ; redressements DGFiP engagés ; cadre juridique 2023-2026. Période : 28/03/2023 - 09/08/2026.

**Exclusions explicites** : le fond des affaires CumCum (dossier parent) ; les contentieux fiscaux individuels non CumCum (sauf CE 451466 cité pour lever une confusion) ; les affaires CumEx allemandes.

**GAP déclarés** :
- GAP-003 (RÉSOLU PARTIELLEMENT le 09/08/2026) : l'état des négociations est désormais documenté (2/5 réglées, 3 en expectative, aucune CJIP postérieure au 08/01/2026), mais les **montants finaux des 3 banques restantes restent inconnus** (confidentiels) : le gap passe de « non publié » à « non finalisé ».
- GAP-004 (ACCESS) : une CJIP signée entre le 19/06/2026 et le 09/08/2026 sans couverture accessible n'est pas exclue (Ξ=7) ; re-vérification recommandée après le 01/09/2026.
- GAP-005 (METHOD) : le total des encaissements réels de redressements (~4,5 Md€ engagés) n'est pas publié ; « engagé » ≠ « encaissé ».
- GAP-006 (CORPUS) : la défense détaillée des 3 banques restantes est absente du corpus (MISSING_COUNTER, EDI).

## 14. ÉTAT DES CONNAISSANCES

- **CONNU (✦)** : 2 CJIP signées (CA 88,2 M€ ; HSBC 267,5 M€ = 115+152 M€) ; 3 banques en expectative ; BNP conteste ~250 M€ ; aucune CJIP postérieure au 08/01/2026 identifiée ; LF 2025 + BOFiP 03/2026 ; jurisprudence 2020-2026 ; CE 451466 (23,75 M€, contentieux fiscal SocGen distinct).
- **PROBABLE (✧)** : la défense « zone grise » des banques restantes est inopérante depuis 2026 ; l'effet d'entraînement des CJIP.
- **HYPOTHÈSE (⁂)** : projection CJIP 0,62-1,16 Md€ ; ratio 1,1 % vs 33 Md€.
- **CONTESTÉ (⊗)** : montant de la perte (33 Md€, Mannheim vs FBF) ; validité des redressements antérieurs à 2025 (CE 472587).
- **INCONNU (⁅)** : montants finaux des 3 banques ; encaissements réels des redressements ; transactions non publiées 06-08/2026.
- **RÉFUTÉ (❧)** : « les redressements engagés sont recouvrés » (engagé ≠ encaissé) ; « Société Générale a conclu une CJIP » (CE 451466 est un contentieux fiscal, pas une CJIP).

## 15. SUSPICION / VÉRIFICATION

**AUDIT DU LEAD** : input UPDATE branché sur le FCT-015/GAP-003 du dossier cumcum parent. Le verdict d'objet (état des négociations) est distinct du verdict de lead (chiffrage de la récupération totale).

**Vérifications contradictoires exécutées** : CONTR-001 (CE 451466 ≠ CJIP SocGen, lecture directe de l'analyse Kohen) ; CONTR-002 (redressements vs CJIP : registres distincts, « engagé » ≠ « encaissé ») ; CONTR-003 (33 Md€ contestés, ratio présenté comme rapport de grandeurs). L'article Actu-Juridique du 11/05/2026 a été lu intégralement (décomposition HSBC 115+152 M€, 4 banques restantes dans le viseur) ; l'analyse Kohen du 19/06/2026 a été lue (expectative des 3 banques, défense « zone grise » inopérante, jurisprudence 2020-2026). Le chiffre BNP (~250 M€, Bloomberg 24/06/2025) provient d'un agent de recherche et n'a pas été relu à la source : étiqueté en conséquence (SRC-03, ⚠️ agent, non relu directement).

**Verdict final : PRÉSUMPTION FORTE (partielle)** : au 09/08/2026, la France a négocié 355,7 M€ de CJIP (2/5 établissements), les 3 autres banques (BNP Paribas, Société Générale, Natixis) sont en expectative, leur défense neutralisée par le verrou de 2026, et la récupération totale finale ne peut être qu'une fourchette (0,36 Md€ acquis à ~6 Md€ en hypothèse haute incluant des redressements non encaissés), sans commune mesure avec les 33 Md€ estimés de perte. Le GAP-003 parent est résolu partiellement : l'état des négociations est documenté, les montants finaux restent confidentiels.

---

# ANNEXE A. SOURCES

| SRC-ID | Source | Locator / date | Rôle | URL |
|--------|--------|----------------|------|-----|
| SRC-01 | Kohen Avocats, « Fraude CumCum et CJIP : la transformation du contentieux de l'arbitrage de dividendes (2023-2026) » | 19/06/2026 | ◈ | https://kohenavocats.com/cumcum-cjip-fraude-fiscale-dividendes-2026/ |
| SRC-02 | Actu-Juridique, « Fraude CumCum : deuxième transaction pour une banque dans le viseur de Bercy » (F. Perrotin) | 11/05/2026 | ◈ | https://www.actu-juridique.fr/fiscalite/fiscal-finances/fraude-cumcum-deuxieme-transaction-pour-une-banque-dans-le-viseur-de-bercy/ |
| SRC-03 | Bloomberg, BNP Paribas conteste le redressement CumCum (~250 M€) | 24/06/2025 | ◈ | (via agent de recherche, non relu directement : étiqueté ⚠️) |
| SRC-04 | Héritage parent 20260809-1416 (FCT-005/007/011/013/014, SRC-02/05/06/09/11/12) | 2026-08-09 | ◈ | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_cumcum-cumex-france/2026-08-09_14-16_cumcum-cumex-france_INVESTIGATION.md |

# ANNEXE B. REQUEST_LOG

```
ENGINE:2.8 | MANIFEST:FINAL | RUN_ID:20260809-1446-cjip-cumcum-banques | PARENT_RUN_ID:20260809-1416 | AS_OF:2026-08-09 | INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:NONE
CHECKPOINT_SEQ:0 | LAST_COMPLETED:15 | NEXT_ACTION:NONE | RESUME_COUNT:0
Investigation:cjip-cumcum-banques | complexity:9→COMPLEX | route overrides:NONE | scope:2023-2026, 5 banques
modules:SYMBOLS|PATTERNS|THREATS|GATES|REQUEST_LOG|EPISTEMIC|TEMPLATE|KERNEL
degraded:NONE | query target/actual: 3/3

COUNT: ◈4 | unique evidence objects:13 | upstream families:8
LEADS:terminal 1/1 | AXES:terminal 3/3 | N/A:none
FAILURES:3 (agents incomplets au 1er passage, relancés ; article Actu-Juridique initialement tronqué, relu intégralement) | FALLBACKS:1 (lecture directe des 2 sources)
unresolved gaps:GAP-003 RÉSOLU PARTIELLEMENT (état documenté, montants finaux confidentiels) ; GAP-004..GAP-006
```

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---:|---|---|---|---|---|
| 1 | SYS | @MNEMO_Q « CJIP BNP Société Générale Natixis CumCum récupération totale » | NO_RESULT (0 mémoire) | Mnemolite | — |
| 2 | SYS | @READ parent 20260809-1416 (FCT-015, GAP-003) + modules | Chargés (héritage revalidé) | run 20260809-1416 | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_cumcum-cumex-france/ |
| 3 | ◈ | QRY-001 (AXS-001/002/003) : état CJIP par banque, total récupération, cadre juridique | FOUND partiel (3 agents incomplets → relances) ; BNP ~250 M€ (Bloomberg 06/2025, via agent) | SRC-03 | presse financière |
| 4 | ◈ | QRY-002 : relance « CJIP postérieure au 08/01/2026 ? » | AUCUNE CONFIRMÉE ; source la plus récente : Kohen 19/06/2026 | SRC-01 | kohenavocats.com |
| 5 | ◈ | Lecture directe Actu-Juridique 11/05/2026 (2 passages, texte complet) | FOUND : décomposition HSBC 115+152 M€, 4 banques restantes dans le viseur de Bercy et du PNF, LF 2019/2025, CE 472587 | SRC-02 | actu-juridique.fr (lu intégralement) |
| 6 | ◈ | Lecture directe Kohen 19/06/2026 | FOUND : expectative des 3 banques, défense « zone grise » inopérante, jurisprudence 2020-2026, BOFiP 03/2026, CE 451466 (23,75 M€) | SRC-01 | kohenavocats.com (lu) |
| 7 | SYS | @MNEMO_S + FACT_WRITEBACK | PENDING_AT_SERIALIZATION | — | — |
| 8 | SYS | STATE:FINAL write | PENDING_AT_SERIALIZATION (ce fichier) | — | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_cjip-cumcum-banques/2026-08-09_14-46_cjip-cumcum-banques_INVESTIGATION.md |

# ANNEXE C. GATES (G0-G10)

| Gate | Vérification | Résultat |
|------|--------------|----------|
| G0 | Modules chargés ; manifest FINAL ; 15 symboles scorés, aucun ✗ | ✅ |
| G1 | LEAD vs OBJECT distincts ; 3 axes terminaux ; périmètre explicite | ✅ |
| G2 | 6 CLM avec support/counter/gap | ✅ |
| G3 | FACT_REGISTRY 13 faits, statuts canoniques (✦/✧/⁂/⁅) | ✅ |
| G4 | Chaque ✦ → SRC-ID + URL ; SRC-03 (Bloomberg via agent) étiqueté ⚠️ non relu directement | ✅ |
| G5 | CAU-001 à 004 typés ; CAU-004 rejetée (engagé ≠ encaissé) | ✅ |
| G6 | CONTROL_MAP + RESPONSIBILITY_MAP ; rôles ≠ responsabilités | ✅ |
| G7 | CONTR-001 à 003 documentés et résolus | ✅ |
| G8 | TRACE_MATRIX ; QRY-001/002 tracés ; IDs résolus | ✅ |
| G9 | Manifest FINAL, NEXT_ACTION NONE, aucun PENDING requis | ✅ |
| G10 | Un seul chemin ; une seule write FINAL ; PENDING_AT_SERIALIZATION honnête | ✅ |

**GAP_SEVERITY** : edi_gap = (0.80-0.58)/0.80 = 0.275 ; query_gap = N/A ; coverage_gap = 0. **GAP_SEVERITY = 0.28 ≥ 0.20 → seuil dépassé : dossier de suivi à statut PARTIEL (gaps GAP-003 partiel, GAP-004 à GAP-006 déclarés), re-vérification recommandée après le 01/09/2026.**

---

*TL;DR : SUJET : issue des négociations CJIP CumCum (BNP Paribas, Société Générale, Natixis) et chiffrage de la récupération totale. OBJET : au 09/08/2026, 2/5 établissements soldés par CJIP (Crédit Agricole 88,2 M€ 09/2025 + HSBC 267,5 M€ 01/2026 = 355,7 M€, décomposition HSBC 115 M€ préjudice + 152 M€ pénalités) ; BNP (conteste ~250 M€), Société Générale et Natixis « demeurent dans l'expectative » (Kohen 19/06/2026, source la plus récente) ; aucune CJIP postérieure au 08/01/2026 identifiée ; défense « zone grise » inopérante depuis la LF 2025 + BOFiP 03/2026. RÉCUPÉRATION TOTALE : 355,7 M€ CJIP (mesuré) + ~4,5 Md€ redressements engagés (non encaissés, contestables) ; projection 0,62-1,16 Md€ si les 3 banques négocient (⁂) ; ratio ~1,1 % vs 33 Md€ estimés. SOURCE : branche du FCT-015/GAP-003 parent, résolu partiellement (état documenté, montants finaux confidentiels). MANIPULATION : Ξ=7, €=8, ↕=8, Κ=7, ⫸=7 ; non-verdict. LIMITE : GAP-003 partiel (montants par banque non finalisés), GAP-004 (CJIP 06-08/2026 non publiée possible), GAP-005 (encaissements non publiés), GAP-006 (défense des banques absente).*
