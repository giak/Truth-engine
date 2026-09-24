# RENARD CORE V3 — INSEE : fabrication, calcul, vérification des chiffres (chômage, IPC, dette)
## Artefact d'investigation 2026-09-22 — H utilisateur : « le manque de forensique/transparence cache des choses »

**Prior(H) fixé avant données : faible.** Base rate : les instituts statistiques des démocraties développées présentent rarement des falsifications centralisées (contre-exemples : INDEC Argentine, Grèce 2004-2010, Russie) ; la France a un cadre juridique et communautaire inhabituel (loi 1951, Eurostat, IPS). ABSENCE!=CONCEALMENT : les gabs constatés sont documentés comme gaps, pas comme dissimulation.

---

## [DECOMPOSE]

| Atom | Sub-claim | Source_tier_needed | Search_target | Verdict |
|---|---|---|---|---|
| A1 | Le taux de chômage BIT est collecté/calculé selon un process documenté | T2 | méthodo enquête Emploi en continu | VERIFIED |
| A2 | L'IPC est produit par relevés massifs documentés (panier, pondérations, ajustement qualité) | T2/T1 | méthodo IPC | VERIFIED |
| A3 | La dette est mesurée depuis comptabilités publiques (pas inventée) ; plusieurs définitions coexistent | T2 | Insee/FIPECO/Cour des comptes | VERIFIED |
| A4 | Comptes nationaux = synthèse estimée de sources administratives, révisions publiées avec causes | T2 | runs antérieurs + Trésor | VERIFIED |
| A5 | Vérification externe effective (Eurostat GNI, peer reviews, ASP) | T2/T3 | Eurostat/ECA | VERIFIED |
| A6 | « Manque de forensique cache des choses » : traces de manipulation | T2/T3/T5 | axes rivaux, révisions, accès | REFUTED (tel quel) ; requalifié |

## [SHADOW] — traces discriminantes cherchées

| Atom | Trace_if_H_true | Trace_if_H_false | Discriminant? |
|---|---|---|---|
| A1-A2 | méthodos absentes/floues | méthodos publiées, changements tracés | Y |
| A5 | aucun contrôle externe réel | inventories + process tables + peer reviews + sanctions budgétaires | Y |
| A3 | définitions opaques/uniques imposées | multiplicité documentée + audits (Cour des comptes 2019) | Y |
| A4 | révisions sans explication | causes publiées (inflation, imprécision volumes) | Y |
| A6 | alertes syndicats/Eurostat/chercheurs sur falsification | auto-critique publiée par l'Insee (inflation perçue, indices alternatifs) | Y |

## TRACE — lignées (sources réellement consultées)

- **Chômage (A1)** : source = enquête Emploi en continu (EEC), ~110 000 répondants, 6 vagues, calcule 3 critères BIT ; méthodo publique (insee.fr source s1223 ; note méthodo 08/2023 PDF ; JMS 2022 Sauvaget) ; intervalle de confiance 95 % : **±0,3 pt** sur le taux trimestriel (Sénat r16-003) — l'Insee publie la marge d'erreur d'un chiffre qu'on présente partout sans elle. Le chiffre-bit médiatisé est un **estimation d'échantillon**, pas un décompte.
- **IPC (A2)** : ~200 000 relevés prix/mois, ~27 000 points de vente (5 types de collecte : enquêteurs tablettes, caisses grande distribution, internet, données administratives, tarifs réglementés) ; panier COICOP, pondérations N-1 ; **ajustement qualité hédonique** (shrinkflation/cheapflation corrigées — blog Insee 2023, variances.eu 2023) ; loyers effectifs 6,28 % du panier, loyers imputés exclus ; impôts/charges patronales non inclus ; **étude 2019 (page Insee 1521318/Wikipédia)** : sur 1998-2018, inflation des 10 % les plus modestes = 32,9 % vs 30,0 % pour les plus aisés (+2,9 pt) — publiée par l'Insee ; simulateur personnalisé en ligne.
- **Dette (A3)** : dette Maastricht = dette brute non consolidée des APU à **valeur de marché** (varie avec les taux) ≠ dette comptes nationaux ≠ dette nette ; PPP inclus si risques supportés par APU ; engagements hors dette (retraites futures non comptées en Europe, contrairement aux USA) ; table 2025 : dépenses 1 714,1 / recettes 1 561,6 / déficit 152,5 Md€ (FIPECO 08/04/2026) ; Cour des comptes 2019 : périmètre « reflète correctement la réalité » (3 agrégats).
- **Comptes nationaux (A4)** : ESANE/DGFiP, douanes, balance des paiements, ENL 2019, redressements fiscaux pour l'activité dissimulée ; révision 3 ans + rebasing coordonné ; cause de révision 2023 publiée (inflation → imprécision des volumes) [runs antérieurs + Trésor 16/07/2025].
- **Vérification (A5)** : Eurostat **vérification du GNI** — inventories + process tables + GIAQ, enjeux financiers propres (cotisation UE indexée sur GNI) ; peer reviews ESS 3ᵉ tour 2021-2023 ; Cour des comptes européenne 26/2022 (qualité statistiques UE, critiques dont pré-release) ; ASP nationale (avis publics) ; certification des comptes de l'État (Cour des comptes/DGFiP).

## [ADVERSARY]

| Axis | H_prediction | Rival_prediction | Observation | Favors |
|---|---|---|---|---|
| Méthodos | absentes/floues | publiées/détaillées | A1, A2 : publiées, longues, tracées | Rival |
| Contrôle externe | inexistant | effectif + à conséquences | A5 : GNI verification à enjeux financiers, peer reviews, ECA | Rival |
| Révisions | opportunistes cachées | documentées | causes publiées ; MAIS asymétrie possible à tester (open) | Rival + réserve |
| Accès | cachées | réel mais barrières | CASD, open data 150 000+ séries, GitHub, simulateur, indices alternatifs | Rival |
| Inflation perçue | sous-estimation délibérée | conventions standards + hétérogénéité | l'Insee publie LUI-MÊME l'écart des modestes (+2,9 pt/20 ans) | Rival |

**CHALLENGER** (chaîne volontairement fausse) : « l'Insee cache car personne ne lit les méthodos » → delta : l'invisibilité n'est pas la dissimulation ; un institut dissimulateur ne publierait ni ses biais (étude modestes), ni des indices alternatifs, ni le simulateur, ni le CASD, ni les IC (±0,3 pt). Fragilité centrale de H : aucune trace d'alerte interne/Eurostat/chercheur sur falsification (vs INDEC/Grece qui avaient toutes les deux des traces et des condamnations).

**COUNTERFACTUAL** : retirons n'importe laquelle des pièces (méthodos, GNI verification, CASD) — la conclusion « process public + vérification externe réelle » survit sur les deux autres. Robuste.

## [EVALUATE]

| Atom | Source_tier | Independent? | Survives_break? | Status | Confidence |
|---|---|---|---|---|---|
| A1 chômage process | T2 | Y | Y | S (VERIFIED) | 0.9 |
| A2 IPC process | T2 | Y | Y | S | 0.85 |
| A3 dette définitions | T2 | Y | Y | S | 0.9 |
| A4 comptes synthèse | T2 | Y | Y | S | 0.85 |
| A5 vérification externe | T2 | Y | Y | S | 0.85 |
| A6 « cache des choses » | T5→T3 | — | Y | R (REFUTED tel quel) | 0.75 |

EPISTEMIC_LEDGER : verified: 5 | supported: 2 | disputed: 0 | open: 3 | refuted: 1
CALIBRATION := 5/6 = **0.83** ✔

## CE QUE H A LAISSÉ VIVANT (les vrais angles, tous documentés)

1. **L'opacité d'expertise** : tout est publié, presque rien n'est *communiqué* ; le chiffre-titre (8,3 %, 1,9 %, 115 %) arrive sans son IC (±0,3 pt), sans ses conventions, sans ses alternatives. L'asymétrie n'est pas Insee↔citoyen mais **journaliste↔convention** (rappel session : 49 % des cat A = chômage BIT ; chômage+halo 10,1 % vs BIT 7,4 %).
2. **L'espace conventionnel** : chaque choix (loyers imputés exclus ; hédonique qui *baisse* l'inflation mesurée ; dette à valeur de marché ; périmètre APU ; retraites hors dette en Europe) est défendable ET déplace des milliards — la liberté directionnelle des récits est **dans les conventions, pas dans les données**. « On peut faire dire ce qu'on veut aux statistiques » : VRAI dans les marges de conventions, FAUX au niveau de la falsification des données brutes.
3. **Révisions asymétriques** (2023-2024 à la hausse, dénominateur) : non tranché, gap quantitatif typé — LA question forensique restante.
4. **Reclassifications du périmètre APU** (France Télécom/EPR, banques, SNCF-retraites) : chaque cas est publié mais le CUMUL de ces bascules n'est jamais raconté — à chiffrer (open).
5. **Pas d'audit forensique indépendant du type « moteur de données »** (comme un INDEC-killer ou un GSO) : les contrôles sont réglementaires (Eurostat/ASP/Cour des comptes), pas adversariaux. C'est un gap par design, pas une preuve de dissimulation — mais c'est le vide que la demande utilisateur pointe légitimement.

## [REPORT]

| Field | Content |
|---|---|
| what_changed_since_last | Passage du « faisceau suspects » (ICEBERG) au *process* : lignées complètes chômage/IPC/dette/comptes + verification externe |
| surviving_H | H requalifiée : « opacité d'expertise + espace conventionnel à enjeux », pas dissimulation |
| killed_H | « le manque de forensique de l'Insee cache des choses » (telle que formulée) |
| confidence_before -> confidence_after | 0.45 -> 0.83 |
| next_priority | (1) chiffrer les reclassifications APU cumulées 2010-2025 ; (2) décomposer révisions PIB vs ratio déficit ; (3) teste IC ±0,3 pt sur les séries médiatisées |
| CALIBRATION | verified 5 / (5+1) = 0.83 |

_Fichiers : ce document ; écritures mémoire MCP (état H + ledger + gaps). Sources consultées listées dans TRACE. Les items « supported » (peer review France spécifique, reclassifications détaillées) ne sont PAS citables comme vérifiés._
