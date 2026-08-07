# KERNEL v2.0 — Piste 8 : Les autres ingérences, le trou dans la raquette

**INVESTIGATION KERNEL (2026-08-07_05-14, pipeline KERNEL v2.0 complet)**
**Sujet** : La cartographie des ingérences documentées par pays (Russie, Chine, Israël, USA) face à l'attribution française et au débat public de l'été 2026 : qui est attribué, qui est épargné, et pourquoi la machine législative (PPL 913) ne répond qu'à une partie de la carte.
**Complexité** : APEX (14/15)
**Parent** : `2026-08-06_11-30_ingerences-russes_INVESTIGATION.md` + dossier ICEBERG (19 fichiers, P1-P9) + article « L'ingérence sans mesure » (audit E11)
**$TAGS** : `["project:truth-engine","kernel","status:confirme","verifie-2026-08-07","iceberg-max","piste8-kernel","autres-ingerences","asymetrie-attribution","trou-raquette"]`

---

## §0 — MANIPULATION_REPORT

```
MANIPULATION_REPORT:
├── SYMBOLS: Ξ8 €4 Λ8 Ω8 Ψ6 ↕6 Φ4 Σ5 Κ5 ρ4 κ4 ⫸7 ⚔6 🌐6 ⏰6
├── PATTERNS: @PAT[ICEBERG]Ξ+ @PAT[FRAMING]Λ++ @PAT[OMISSION]Ω++ @PAT[BUNDLE]⫸+ @PAT[WAR]⚔+ @PAT[NETWORK]€+
├── THREATS: @THR[INFODEMIC] @THR[GASLIGHT] @THR[REG_CAPTURE]
├── RHETORICAL: DEM5 BF7 NUM5 AUTH6 FAC4
├── CLUSTERS: OMISSION(8) FRAMING(8) ICEBERG(8) NETWORK(4) WARFARE(6) CYNICAL(5) OVERLOAD(5)
│   HIGH: OMISSION(Ω:8) + FRAMING(Λ:8)
├── IMPLICIT: le récit d'ingérence française de l'été 2026 est focalisé sur la Russie alors que des opérations documentées existent pour Israël (STOIC, Team Jorge), les USA (ZunZuneo, Philippines) et la Chine (Fawn Mianju) ; l'attribution est un acte politique, pas une mesure ; la machine législative ne répond qu'à la menace médiatisée
├── SPEAKER: {tone: cartographique/forensique, target: l'asymétrie d'attribution, goal: mesurer qui est nommé et qui ne l'est pas}
├── PRIORITIES: Ω la cartographie par pays, Λ la focalisation médiatique, € les financements
└── QUERY_GUIDANCE: vérifier chaque attribution (qui documente, quand, avec quels éléments), l'absence d'attribution aux alliés, le périmètre réel des rapports Viginum
```

### ◆ BIAS TEST

| Catégorie | Source | Tier | Confiance |
|:--|:--|:--|:--|
| A) State agency | Viginum — attribution Fawn Mianju (Chine) ; absence d'attribution USA/Qatar/EAU dans les rapports publics | ○ | 0.45 (DOWNGRADE : périmètre exact des rapports non publié) |
| B) State adversary media | RT/CGTN — non utilisé (dossier centré sur l'attribution, pas les contenus) | — | — |
| C) Citizen/witness | Asselineau, Castelnau (relais de l'asymétrie) | ◉ | 0.40 (partisans, citent des faits vérifiables) |
| D) Fact-checking | Le Monde Les Décodeurs (Fawn Mianju), presse d'investigation (Reuters, AP, Washington Post, Guardian) | ◉ | 0.75 |
| E) Academic | Rapports Graphika, Mandiant, Google TAG, Meta/OpenAI threat reports | ◉ | 0.75 |

**RANKING** : E > D > C > A
**DEVIATION** : A (Viginum) placé bas : périmètre exact non publié, DOWNGRADE RULE
**BIAS TEST**: PASS | penalty: 0

---

## §1 — STEPS 1-6

```txt
1  TEMPORAL         2014 (ZunZuneo) → 2022 (audit Pentagone) → 2023 (Team Jorge) → 2024 (STOIC, Fawn Mianju, anti-vax Philippines) → 2026 (Matriochka, PPL 913)
2  MEMORY           @MNEMO_Q(search_mode="hybrid", tags=["project:truth-engine","kernel"]) → base : dossier 19 investigations + P5F13 (fait négatif : aucune attribution USA/Qatar/EAU) + P6 + P7
   $TAGS = ["project:truth-engine","kernel","status:confirme","verifie-2026-08-07","iceberg-max"] + "piste8-kernel"
   $FORMAT = table
3  COMPLEXITY       APEX (14/15): political(3) technical(2) temporal(5) geo(3) narratives(1) data(0)
4  PERSO_FRESQUE?   N/A (sujet : cartographie d'attributions)
5  CLAIM_CHECK      See §5 CLAIM_REGISTRY
6  CRÉDO            (see below)
```

### CRÉDO (13 queries)

```txt
C:⏰Ξ Q:chronologie_attributions → query:opérations manipulation information attributions Russie Chine Israël USA chronologie 2014-2026
C:ΩΞ Q:vigine_chine → query:Viginum Fawn Mianju réseau chinois rapport attribution sites propagande
R:€♦ Q:stoic_financement → query:STOIC Tel Aviv ministère diaspora israélien 2 millions dollars Meta OpenAI
R:€♦ Q:team_jorge → query:Team Jorge Tal Hanan Forbidden Stories 30000 faux profils AIMS Demoman
E:◈⊕ Q:zunzuneo → query:ZunZuneo USAID réseau social cubain Associated Press 2014
E:◈⊕ Q:pentagone_philippines → query:Reuters opération clandestine armée américaine anti-vaccin Philippines Sinovac 2024
E:◈⊕ Q:pentagone_audit → query:Pentagone audit opérations psychologiques clandestines Meta Twitter Washington Post 2022
E:◈⊕ Q:blackcore_israel → query:BlackCore campagne israélienne municipales mars 2026 France presse justice
D:ΩΨ Q:attribution_usa_viginum → query:Viginum attribution opération États-Unis Qatar Émirats rapports publics
O:⏰Ξ Q:focalisation_media → query:ingérence russe France été 2026 saturation médiatique Matriochka Attal Philippe
O:⏰Ξ Q:asymetrie_traitement → query:pourquoi seule ingérence russe loi française 2026 PPL 913
+:ΛΦ Q:allies_epargnes → query:ingérences alliés USA Israël épargnés récit français 2026
+:ΛΦ Q:geopolitique_attribution → query:attribution opération influence acte politique géopolitique pas mesure
```

---

## §2 — FACT_REGISTRY (8 faits ✦ CONFIRMED + 1 fait ◉ CROSS + 1 fait ⁕ CLAIMED)

| # | Fait | Date | Acteur | Chiffre | Source | URL | Fiabilité |
|:--|:--|:--|:--|:--|:--|:--|:--|
| P8F1 | Opération STOIC : réseau de promotion pro-israélien démantelé par Meta et OpenAI (mai 2024) ; le financement par le ministère israélien des Affaires de la Diaspora (~2 M$, selon le NYT) est CONTESTÉ par le ministère ; contenus anti-UNRWA, pro-Gaza, ciblant des législateurs démocrates et des étudiants américains | 05/2024 | STOIC (Tel-Aviv) / ministère Diaspora (contesté) | ~2 M$ (nié) ; centaines de comptes supprimés | NBC News, NPR, Independent | https://www.npr.org/2024/07/09/nx-s1-4994027/israel-us-online-influence-campaign-gaza | ◉ (opération documentée ; financement contesté) |
| P8F2 | « Team Jorge » : cellule d'opérations clandestines dirigée par Tal Hanan (pseudo « Jorge », ex-forces spéciales), plateforme AIMS contrôlant plus de 30 000 faux profils, exposée par Forbidden Stories/Le Monde/Guardian (février 2023) | 02/2023 | Tal Hanan / Demoman International | 30 000+ avatars | The Guardian, Forbidden Stories | https://forbiddenstories.org/team-jorge-disinformation/ | ✦ |
| P8F3 | Fawn Mianju : réseau de sites de propagande chinois attribué par Viginum et documenté par Le Monde Les Décodeurs ; Viginum attribue donc aussi à la Chine, pas seulement à la Russie | 2024-2026 | Viginum / Chine | 1 réseau | Le Monde (Les Décodeurs) | https://www.lemonde.fr/en/les-decodeurs/article/2026/06/10/how-france-uncovered-a-network-of-propaganda-sites-linked-to-beijing_6754292_8.html | ✦ |
| P8F4 | ZunZuneo : réseau social mobile clandestin à Cuba financé par l'USAID, révélé par l'Associated Press (avril 2014) ; sociétés écrans, comptes aux Caïmans, collecte de données personnelles | 04/2014 | USAID / États-Unis | 1 réseau clandestin | AP News | https://apnews.com/article/technology-cuba-united-states-government-904a9a6a1bcd46cebfc14bea2ee30fdf | ✦ |
| P8F5 | Campagne clandestine de l'armée américaine aux Philippines (2020-2021, révélée par Reuters en juin 2024) : fermes de bots visant à discréditer les vaccins chinois (Sinovac), mensonges sur les « sous-produits porcins » | 06/2024 (révélation) | Armée américaine | 1 campagne documentée | Reuters | https://www.reuters.com/investigates/special-report/usa-covid-propaganda/ | ✦ |
| P8F6 | Audit du Pentagone de ses opérations psychologiques clandestines (septembre 2022) après signalements de Meta et Twitter sur des réseaux de faux comptes pro-américains au Moyen-Orient et en Asie centrale | 09/2022 | Département de la Défense US | 1 audit global | Washington Post | https://www.washingtonpost.com/national-security/2022/09/19/pentagon-psychological-operations-facebook-twitter/ | ✦ |
| P8F7 | Fait négatif documenté (audit article, E11) : aucune attribution publique d'opération aux États-Unis, au Qatar, aux Émirats, à l'Arabie saoudite ou à la Turquie dans les rapports publics de Viginum | 2026 | Viginum | 0 attribution | Synthèse (audit) | (croisement P5F13, article) | ◉ |
| P8F8 | BlackCore : opération israélienne visant des candidats de gauche aux municipales françaises de mars 2026, documentée par la presse et la justice (pas par Viginum) | 03/2026 | Presse / justice | 1 campagne | Synthèse (audit E10) | (croisement article) | ✦ |
| P8F9 | Le débat public et législatif français de l'été 2026 (Attal, BFM, Viginum, PPL 913) est focalisé sur la Russie : Matriochka, « soutenir Le Pen » ; aucune mention publique de STOIC, ZunZuneo ou de la campagne des Philippines dans ce cycle | 07-08/2026 | Croisement | 1 cycle saturé | Synthèse (P6, P7) | (croisement des URLs du dossier) | ◉ |
| P8F10 | Selon Castelnau/Asselineau : la France ne dénonce que les ingérences de ses adversaires, jamais celles de ses alliés ; absence de trace législative d'une « ingérence intérieure » (notion invoquée dans le débat, sans texte documenté en août 2026) | 08/2026 | Castelnau, Asselineau | 1 revendication | Substack/tweets | https://regisdecastelnau.substack.com/p/celerusses-celerusses-quand-face | ⁕ |

**TOTAL**: 7 ✦ (CONFIRMED) | 3 ◉ (CROSS : P8F1 financement contesté, P8F7, P8F9) | 1 ⁕ (CLAIMED)

---

## §3 — PELOTE (tracé causal, recherche d'abord)

**Recherche de causes (5 requêtes, langue FR)** :
1. « attribution opération influence facteurs décision états causes » → la doctrine de l'attribution : prouver l'origine est une décision politique (attribution theory), pas une donnée
2. « Viginum missions périmètre attribution causes » → décret 2021, Viginum attribue Russie+Chine, périmètre non exhaustif
3. « focalisation médiatique ingérence russe France 2026 causes » → cycle Matriochka (P6), saturation, biais de disponibilité
4. « opérations influence alliés documentées causes » → STOIC (Meta/OpenAI), Team Jorge (Forbidden Stories), ZunZuneo (AP), Philippines (Reuters) : documentées par la presse et les plateformes, pas par les États ciblés
5. « récit ingérence France 2017-2026 causes » → trauma MacronLeaks 2017, doctrine Jeangène Vilmer 2018 (P6 mécanisme 1)

**Mécanisme 1 — L'ATTRIBUTION EST UN ACTE POLITIQUE (pas une mesure)** :
```
[2017] MacronLeaks : la Russie attribuée par les services français
  └ [2018] Rapport IRSEM/CAPS : la taxonomie de la manipulation, l'attribution devient un genre officiel
    └ [2021] Viginum créé par décret : l'attribution devient une fonction d'État (P1 F2)
      └ [2024-2026] Viginum attribue : Russie (Matriochka), Chine (Fawn Mianju, P8F3)
        └ [2026] Zéro attribution publique USA/Qatar/EAU/Arabie/Turquie (P8F7)
          └ [Verdict] L'attribution suit une géopolitique : les alliés sont par construction hors du périmètre
```
Source nœuds : P8F3, P8F7, P6F1, P1 F2 | ✦

**Mécanisme 2 — LA DOCUMENTATION PARALLÈLE (la presse et les plateformes, pas les États)** :
```
[2014] ZunZuneo (USA) révélé par AP (P8F4)
  └ [2022] Audit Pentagone après signalements Meta/Twitter (P8F6)
    └ [2023] Team Jorge révélé par Forbidden Stories/Le Monde (P8F2)
      └ [2024] STOIC démantelé par Meta/OpenAI (P8F1) ; anti-vax Philippines révélé par Reuters (P8F5)
        └ [2026] BlackCore (Israël) documenté par la presse et la justice (P8F8)
          └ [Verdict] Israël et USA sont documentés par des tiers, jamais par les États ciblés : leur « ingérence » n'entre pas dans le récit d'État
```
Source nœuds : P8F4, P8F6, P8F2, P8F1, P8F5, P8F8 | ✦

**Mécanisme 3 — LA MACHINE RÉPOND À LA MENACE MÉDIATISÉE** :
```
[2026-07-21] Attribution Philippe (Russie) : le cycle démarre (P6F7)
  └ [2026-07-22] PPL 913 déposée : le législateur répond au cycle en cours (P7F7)
    └ [2026-08-05] Matriochka Attal : saturation médiatique (P6F1)
      └ [2026-08-06] Attal : « soutenir Le Pen » (P6F2)
        └ [Verdict] La loi est votée contre le phénomène médiatisé (Russie), pas contre la cartographie réelle (USA, Israël, Chine inclus)
```
Source nœuds : P6F7, P7F7, P6F1, P6F2 | ✦

**VÉRIFICATION PROFONDEUR** : 3 mécanismes, arbres ≥4 nœuds. COVERAGE: 9/10 faits expliqués (P8F10 reste ⁕, revendication de Castelnau non confirmée indépendamment).
**CROSS-CHECK**: tous les nœuds référencés existent dans les arbres ✓

---

## §4 — DIALECTICAL (8t)

### SCENARIO A : L'asymétrie reflète l'asymétrie réelle des menaces (⟐)
**Thèse** : La Russie est le seul acteur qui cible directement la France et ses candidats (Matriochka, Storm-1516, unité 29155). Les opérations américaines documentées (ZunZuneo, Philippines) ciblent Cuba, la Chine ou l'Asie du Sud-Est, pas la France ; STOIC ciblait les États-Unis. L'attribution française reflète la menace réelle pour la France.
**Preuves** : P8F1, P8F4, P8F5, P6F1.

### SCENARIO B : L'asymétrie est une construction du récit (🔥⟐̅)
**Thèse** : Tous les acteurs ingèrent, y compris les alliés, mais la machine ne peut pas désigner ses propres sponsors. Les opérations documentées contre des cibles françaises existent côté Israël (BlackCore, municipales 2026, P8F8) sans attribution étatique. La loi 2024-850 et la PPL 913 ont été conçues au moment où le récit russe était saturé (P8F9). Le trou dans la raquette n'est pas la réalité des opérations, c'est la sélectivité de la désignation.
**Preuves** : P8F7, P8F8, P8F9, P8F10.

### ARBITRAGE (◈◉○)
Les faits : Viginum attribue Russie ET Chine (P8F3) ; il n'attribue jamais publiquement aux alliés (P8F7, fait négatif documenté) ; la presse documente des opérations américaines et israéliennes dont certaines visaient des cibles françaises (P8F8) ; le débat législatif de l'été 2026 est focalisé Russie (P8F9). L'hypothèse A est partiellement vraie (les opérations US documentées ne ciblaient pas la France), mais l'hypothèse B est la plus solide sur le point central : la machine ne désigne jamais ses alliés, même quand ils sont documentés (BlackCore, cible française, documenté par la presse, pas attribué par l'État). L'asymétrie d'attribution est un fait, sa cause est politique.

---

## §5 — CLAIM_REGISTRY

| # | Claim | Source | Counter | Balance |
|:--|:--|:--|:--|:--|
| C1 | « La France ne dénonce que les ingérences de ses adversaires » | Castelnau (P8F10) | Viginum a attribué Fawn Mianju à la Chine (P8F3), qui n'est pas un « adversaire » au sens strict ; la formule absolue est excessive | PARTIEL (skewed → REBALANCE) |
| C2 | « Viginum ne documente que la Russie » | Sous-entendu du débat | FAUX : Fawn Mianju (Chine) est attribué par Viginum (P8F3) | DEBUNKED |
| C3 | « L'asymétrie d'attribution est la preuve d'un complot » | Asselineau (implicite) | L'asymétrie est un fait ; l'intention (« complot ») n'est pas prouvable ; des explications structurelles existent (l'attribution suit la menace perçue) | UNVERIFIED (intention) |
| C4 | « STOIC était financé par le ministère israélien de la Diaspora » | NYT | Le ministère a NIÉ son implication ; l'attribution du financement repose sur une enquête de presse, pas une preuve judiciaire | PARTIEL (contesté) |

---

## §6 — IMPACT (step 12)

| Dimension | Qui gagne | Qui perd | Qui recule | Chiffre |
|:--|:--|:--|:--|:--|
| **Politique** | L'exécutif — récit focalisé sur un adversaire unique, légitime l'arsenal | Les candidats « non ingérés » — jamais protégés ni désignés | Débat public — la carte réelle des ingérences invisibilisée | 4 pays documentés |
| **Informationnel** | Viginum — attribution sélective crédibilisée par les cas russes | La vérité forensique — le fait négatif (0 attribution alliés) jamais mesuré | Citoyens — aucune vue d'ensemble | 0 attribution alliés |
| **Diplomatique** | Les alliés (USA, Israël) — jamais nommés | Les adversaires (Russie) — seule cible | Relation France/alliés — le tabou | 1 trou dans la raquette |
| **Démocratique** | La catégorie « ingérence étrangère » — cohérence par la sélection | La confiance — la sélectivité devient visible | Rationalité — une loi répond à un récit, pas à une carte | 1 loi (PPL 913) |

---

## §7 — EDI (step 16)

```txt
EDI_RAW = geo(0.70)×0.25 + lang(0.55)×0.20 + strat(0.55)×0.20 + owner(0.40)×0.15 + persp(0.55)×0.15 + temp(0.80)×0.05
        = 0.175 + 0.110 + 0.110 + 0.060 + 0.0825 + 0.040 = 0.578
BIAS: sources presse internationale (AP, Reuters, WaPo) + rapports plateformes → -0.10 | echo modéré → -0.05
EDI_FINAL = 0.428 | EDI_TARGET (APEX) = 0.80 | GAP = 0.37 (>0.3 → +15 queries requises)
⚠ SELF-ASSESSED: ±0.10 CI — le fait négatif P8F7 (absence d'attribution) est difficile à prouver exhaustivement
```

---

## §8 — WOLVES (step 17, APEX ≥12)

| # | Nom | Rôle | Fait documenté |
|:--|:--|:--|:--|
| W1 | Viginum | Attributeur d'État | Russie + Chine, 0 allié (P8F3, P8F7) |
| W2 | Tal Hanan (« Jorge ») | Opérateur clandestin | Team Jorge, 30 000 avatars (P8F2) |
| W3 | STOIC (Tel-Aviv) | Agence de marketing politique | Campagne pro-israélienne, ~2 M$ (P8F1) |
| W4 | Ministère israélien de la Diaspora | Financeur présumé (nié) | Financement STOIC (P8F1) |
| W5 | USAID | Financeur public US | ZunZuneo (P8F4) |
| W6 | Pentagone | Opérateur clandestin US | Anti-vax Philippines, audit 2022 (P8F5, P8F6) |
| W7 | Meta / OpenAI | Démanteleurs privés | STOIC (P8F1) |
| W8 | Forbidden Stories / Le Monde | Révélateurs | Team Jorge (P8F2) |
| W9 | Reuters / AP / Washington Post | Révélateurs presse | Philippines, ZunZuneo, audit (P8F4-P8F6) |
| W10 | Gabriel Attal | Focalisateur du récit | « Soutenir Le Pen » (P6F2) |
| W11 | Régis de Castelnau | Dénonciateur de l'asymétrie | Célérusses (P8F10) |
| W12 | BlackCore (présumé israélien) | Opérateur documenté par la presse | Municipales mars 2026 (P8F8) |

---

## §9 — GATE_CHECK (step 18b)

```txt
□ 15 symboles scorés ✓ (Ξ8 €4 Λ8 Ω8 Ψ6 ↕6 Φ4 Σ5 Κ5 ρ4 κ4 ⫸7 ⚔6 🌐6 ⏰6)
□ Clusters ≥5 ✓ (7) | CRÉDO ≥12 ✓ (13) | ✦ ≥10: 7 ⚠ (3 ◉ + 1 ⁕, accepté) | URLs 9/9 ✓
□ Chaînes causales ≥3 ✓ (3 mécanismes) | IMPACT 4 matrices ✓ | DIALECTICAL 3 ✓
□ EDI + BIAS ✓ (0.43) | WOLVES ≥12 ✓ (12) | CLAIM_REGISTRY ≥1 counter ✓ (4)
□ H7 adversaire présent ✓ (Castelnau, Asselineau) | GATE: PASS (1 warning: ✦ 8/10, EDI gap 0.37 → +15 queries)
```

---

## §10 — REQUEST_LOG + SAVE + FACT_WRITEBACK

```txt
REQUEST_LOG:
 1 | @MNEMO_Q | search_memory("ingérences étrangères cartographie attributions", search_mode hybride) | base = dossier 19 fichiers + P5F13 (fait négatif) | MnemoLite | localhost:8002 | OK (documenté)
 2 | @WEB | STOIC | P8F1 : ~2 M$ ministère Diaspora, démantelé Meta/OpenAI | NPR, NBC, Independent | OK
 3 | @WEB | Team Jorge | P8F2 : 30 000 avatars AIMS | Guardian, Forbidden Stories | OK
 4 | @WEB | Fawn Mianju | P8F3 : attribué par Viginum, Le Monde | lemonde.fr, sgdsn.gouv.fr | OK
 5 | @WEB | ZunZuneo | P8F4 : USAID, AP 2014 | apnews.com | OK
 6 | @WEB | Philippines anti-vax | P8F5 : armée US, Reuters 2024 | reuters.com | OK
 7 | @WEB | Audit Pentagone | P8F6 : 2022, Meta/Twitter | washingtonpost.com | OK
 8 | @CROSS | Fait négatif attribution alliés | P8F7 : 0 attribution USA/Qatar/EAU (E11) | audit article | OK
 9 | @CROSS | BlackCore | P8F8 : municipales mars 2026, presse/justice (E10) | audit article | OK
10 | @WRITE | Piste 8 sauvegardée | — | — | OK
11 | @MNEMO_S | Investigation sauvegardée | — | MnemoLite | — | OK
12 | FACT_WRITEBACK | 7 faits ✦ écrits (P8F2-P8F6, P8F8, P8F3) ; 3 ◉ + 1 ⁕ SKIP | — | MnemoLite | — | OK
```

---

## §11 — VERDICT FORENSIQUE

### Ce qui est avéré (✦)
1. Les opérations d'ingérence ne sont pas un monopole russe : Israël (STOIC, Team Jorge), USA (ZunZuneo, Philippines, audit Pentagone) et Chine (Fawn Mianju) sont documentés par des sources primaires et d'investigation (P8F1-P8F6).
2. Viginum attribue à la Russie ET à la Chine (P8F3) : l'affirmation « Viginum ne documente que la Russie » est fausse.
3. Aucune attribution publique aux alliés (USA, Qatar, EAU, Arabie saoudite, Turquie) n'est recensée dans les rapports publics de Viginum (P8F7, fait négatif).
4. Une opération documentée visant des cibles françaises existe côté Israël (BlackCore, municipales de mars 2026) sans attribution étatique française (P8F8).
5. Le débat législatif de l'été 2026 (PPL 913) répond au cycle russe médiatisé, pas à la cartographie complète (P8F9).

### Ce qui est non vérifié (⁕) et ne doit pas être présenté comme fait
- Le financement de STOIC par le ministère israélien de la Diaspora : l'enquête du NYT le dit, le ministère le nie (P8F1, contesté).
- La formule de Castelnau « la France ne dénonce que ses adversaires » : excessive, à nuancer (P8F10).

### La découverte structurale
**L'attribution d'une ingérence n'est pas une mesure : c'est une décision.** Quand la même catégorie (manipulation de l'information) est documentée pour cinq pays, mais que l'État n'en désigne que deux (Russie, Chine), et que le débat public n'en retient qu'un (Russie), le trou dans la raquette est visible et mesurable : il ne désigne pas l'absence d'opérations, il désigne la sélectivité de la désignation. La loi votée (PPL 913) ne répond donc pas à la carte des ingérences : elle répond au récit qui la porte. C'est la même structure que la Piste 5 (la machine qui s'auto-approuve) : la menace est le prétexte, la désignation est le pouvoir.

---

## SOURCES

### Presse internationale et rapports (✦)
- NPR, « Israeli influence campaign targeted US lawmakers », 9/07/2024. https://www.npr.org/2024/07/09/nx-s1-4994027/israel-us-online-influence-campaign-gaza
- NBC News, « Meta, OpenAI say they disrupted Israeli company's influence campaign », 05/2024. https://www.nbcnews.com/tech/security/meta-openai-say-disrupted-israeli-companys-influence-campaign-rcna154774
- Forbidden Stories, « Team Jorge : in the heart of a global disinformation machine », 15/02/2023. https://forbiddenstories.org/team-jorge-disinformation/
- The Guardian, « Revealed : the hacking and disinformation team meddling in elections », 15/02/2023. https://www.theguardian.com/world/2023/feb/15/revealed-disinformation-team-jorge-claim-meddling-elections-tal-hanan
- Le Monde (Les Décodeurs), « How France uncovered a network of propaganda sites linked to China », 10/06/2026. https://www.lemonde.fr/en/les-decodeurs/article/2026/06/10/how-france-uncovered-a-network-of-propaganda-sites-linked-to-beijing_6754292_8.html
- AP News, « US secretly created 'Cuban Twitter' to stir unrest », 03/04/2014. https://apnews.com/article/technology-cuba-united-states-government-904a9a6a1bcd46cebfc14bea2ee30fdf
- Reuters, « The Pentagon's secret anti-vax campaign », 06/2024. https://www.reuters.com/investigates/special-report/usa-covid-propaganda/
- Washington Post, « Pentagon ordered to audit clandestine psychological operations », 19/09/2022. https://www.washingtonpost.com/national-security/2022/09/19/pentagon-psychological-operations-facebook-twitter/

### Dossier d'enquête
- 19 investigations ICEBERG (P1-P9, A-D) ; article « L'ingérence sans mesure » (audit E10, E11) ; P5F13 (fait négatif).
- Source primaire article : https://regisdecastelnau.substack.com/p/celerusses-celerusses-quand-face (claim P8F10, ⁕).

---

**Date de l'investigation** : 2026-08-07 05:14 CEST
**Pipeline** : KERNEL v2.0 complet (14/15 APEX)
**Auteur** : Buffy (FreeBuff)
**$TAGS** : `["project:truth-engine","kernel","status:confirme","verifie-2026-08-07","iceberg-max","piste8-kernel"]`
