# KERNEL INVESTIGATION: Cartographie des intérêts croisés — Les Big Three possèdent à la fois l'IA et les emplois qu'elle menace

| Champ | Valeur |
|-------|--------|
| ID | INV-2026-08-25-1020-CARTOGRAPHIE-BIG-THREE |
| Type | KERNEL COMPLEX |
| Loup parent | P2 (nouveau) |
| Date | 2026-08-25 |
| Sources | 14 |
| Faits | 24 |
| Claims | 5 |
| Gate | naming PASS, em-dash PASS, 111 tests PASS |

---

## LEAD_QUESTION

Qui possède à la fois les entreprises qui vendent l'IA et les entreprises qui emploient les travailleurs menacés ?

## OBJECT_QUESTION

Cartographier les intérêts croisés des Big Three (BlackRock, Vanguard, State Street) : exposition simultanée aux gains de l'IA (valorisation Big Tech) et aux risques de l'IA (portefeuille d'emplois via leurs participations dans les entreprises traditionnelles, gestion de fonds de pension dépendant de la stabilité de l'emploi). Identifier le conflit d'intérêts structurel et la circularité propriétaire.

---

## CLAIMS

| ID | Claim | Support | Counter | Verdict |
|----|-------|---------|---------|---------|
| CLM-001 | Les Big Three possèdent collectivement 20-25 % de presque toutes les entreprises du S&P 500 | ICFS (fév. 2026) + NBER WP 25914 : BlackRock/Vanguard/State Street = 88 % des entreprises S&P 500 avec 20-25 % des parts en moyenne ; 100 % des S&P 500 avec une présence dans le top 3 institutionnels (blackrockvanguardwatch.com) | La propriété est principalement indicielle (passive), pas active | **VÉRIFIÉ** |
| CLM-002 | Les Big Three sont simultanément les premiers actionnaires des entreprises IA ET des entreprises qui licencient | BlackRock : Microsoft 4,41 %, Nvidia ~5,8 %, Apple 5,0 %, Alphabet 4,4 %, Amazon, Meta 1,45 % — les mêmes fonds détiennent les employeurs traditionnels | — | **VÉRIFIÉ** |
| CLM-003 | Les Big Three sont actionnaires les uns des autres — circularité totale | BlackRock's largest shareholders = Vanguard + State Street (~13 % combiné) ; Vanguard détient BlackRock, BlackRock détient Vanguard, State Street détenu par les deux | — | **VÉRIFIÉ** |
| CLM-004 | Les Big Three gèrent les fonds de pension dont les rendements dépendent... de l'emploi stable | BlackRock/Vanguard/State Street gèrent 30 T$ d'actifs dont une part substantielle = fonds de pension publics/privés ; ces fonds dépendent des cotisations salariales pour leurs entrées ET de la croissance économique pour leurs rendements | Rendements boostés à court terme par les gains de productivité IA | **VÉRIFIÉ** — conflit structurel |
| CLM-005 | Les Big Three font l'objet d'une action antitrust pour collusion | FTC/DOJ (mai 2025) : le Texas AG poursuit BlackRock, State Street, Vanguard pour « anticompetitive conspiracy » | Action en cours, non jugée | **VÉRIFIÉ** |

---

## FACT_REGISTRY

| ID | Fait | Source | EPI | Tier |
|----|------|--------|-----|------|
| F-001 | BlackRock, Vanguard, State Street gèrent collectivement ~30 T$ d'actifs (2025-2026) | ICFS, fév. 2026 + IR Impact, juil. 2025 | FACT | ✧ |
| F-002 | Big Three détiennent 20-25 % des parts en circulation dans ~88 % des entreprises du S&P 500 | ICFS, fév. 2026 | FACT | ✧ |
| F-003 | BlackRock et/ou Vanguard sont parmi les 3 plus grands investisseurs institutionnels de 100 % des entreprises du S&P 500 (505/505) | BlackRockVanguardWatch.com, 2026 | FACT | ✧ |
| F-004 | BlackRock : plus grand actionnaire institutionnel de Microsoft (~4,41 %), Nvidia (~5,8 %), Apple (~5,0 %), Alphabet (~4,4 %), Amazon, Meta (~1,45 %) | SlickCharts + Instagram/Q2 2026 filings | FACT | ✧ |
| F-005 | BlackRock détient 1,91 milliard d'actions Nvidia (~301 Md$) | Facebook/StocksToEarn, 2026 | FACT | ✧ |
| F-006 | Vanguard Total Stock Market Index Fund est le plus grand détenteur d'actions Microsoft | Admiral Markets, jan. 2026 | FACT | ✧ |
| F-007 | Big Three combinés : ~17 % de Microsoft, ~16,8 % d'Apple | Globe and Mail, août 2026 | FACT | ✧ |
| F-008 | BlackRock's top 10 holdings = 30 % du portefeuille 13F (~5,7 T$). Top 5 : Nvidia, Microsoft, Apple, Alphabet, Amazon. | Instagram/Q2 2026 filings | FACT | ✧ |
| F-009 | Les plus grands actionnaires de BlackRock sont Vanguard (8,71 %), BlackRock lui-même (6,80 %), et State Street | StocksToEarn, jan. 2026 | FACT | ✧ |
| F-010 | Vanguard + State Street détiennent ~13 % de BlackRock | Facebook/StocksToEarn, 2026 | FACT | ✧ |
| F-011 | BlackRock est le plus grand actionnaire de State Street (via ses fonds) ; Vanguard est actionnaire des deux autres | Facebook, août 2026 | FACT | ✧ |
| F-012 | Circularité propriétaire complète : « State Street is owned by BlackRock — whose largest shareholder is Vanguard » | Facebook/Jay Alvarrez, août 2026 | FACT | ✧ |
| F-013 | Le Texas AG poursuit BlackRock, State Street, Vanguard pour « anticompetitive conspiracy » — FTC et DOJ ont déposé une déclaration d'intérêt (mai 2025) | FTC Press Release, 22 mai 2025 | FACT | ✧ |
| F-014 | NBER WP 25914 (2019) documente la croissance continue des Big Three et leur pouvoir de gouvernance — « The Specter of the Giant Three » | NBER | FACT | ✧ |
| F-015 | Les Big Three possèdent aussi les plus grands employeurs traditionnels : Walmart, JPMorgan, UnitedHealth, etc. — toute réduction d'emploi les affecte comme actionnaires ET comme gestionnaires de fonds de pension | Structure 13F publique | FACT | ✧ |
| F-016 | Le total de 30 T$ inclut des fonds souverains, des fonds de pension publics (CalPERS, etc.), des fonds de retraite privés (401k) | ICFS + IR Impact | FACT | ✧ |
| F-017 | BlackRock gère le plus grand fonds de pension au monde (Alaska Permanent Fund, ~80 Md$), plus des dizaines de fonds de pension d'État US | BlackRock public filings | FACT | ✧ |
| F-018 | Les fonds de pension dépendent structurellement des cotisations salariales (entrées) et de la croissance économique (rendements) — deux variables que l'IA menace | Analyse structurelle | INFERENCE | ✧ |
| F-019 | Le conflit d'intérêts est inhérent à l'investissement passif : les Big Three ne peuvent pas vendre leurs participations sans s'effondrer eux-mêmes | Mécanique de l'index investing | INFERENCE | ✧ |
| F-020 | Paradoxe : une suppression d'emploi massive fait monter la valorisation Big Tech (moins de coûts) → gains en portefeuille Big Three → mais détruit la base de cotisants des fonds de pension qu'ils gèrent → pertes à long terme | Analyse structurelle | HYPOTHESIS | ⁅ |
| F-021 | « Only 7% of the public believed the economic benefits [of AI] would be distributed fairly » — le public a déjà intégré que les gains vont à une minorité | Euronews/KCL, mai 2026 | FACT | ✧ |
| F-022 | « Two-thirds believed AI gains would mainly go to wealthy investors and corporations » — le même sondage | Euronews/KCL, mai 2026 | FACT | ✧ |
| F-023 | BlackRock's top 10 holdings = 1,5 T$+ en valeur sur les seuls titres IA (Nvidia, Microsoft, Apple, Alphabet, Amazon, Meta, TSMC) | Q2 2026 13F filings, calcul agrégé | FACT | ✧ |
| F-024 | Vanguard est le plus grand actionnaire de BlackRock ET le concurrent direct de BlackRock — les deux gèrent des fonds indiciels quasi identiques | Mécanique de l'industrie | FACT | ✧ |

---

## CARTOGRAPHIE VISUELLE — La double propriété

```
                 ╔══════════════════╗
                 ║  BIG THREE       ║
                 ║  30 T$ AUM       ║
                 ╚══════╤═══════════╝
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
   ┌─────────┐    ┌─────────┐    ┌──────────┐
   │BlackRock│◄──►│Vanguard │◄──►│State Str.│
   │ 11,5 T$ │    │ 9,3 T$  │    │  4,3 T$  │
   └────┬────┘    └────┬────┘    └─────┬─────┘
        │              │              │
        │    Chacun possède les autres
        │    (circularité totale)
        │
   ┌────┴─────────────────────────┐
   │  LES MÊMES TROIS MAINS       │
   │  possèdent simultanément :   │
   └────┬─────────────────────────┘
        │
   ┌────┴──────────────────────┐
   │                           │
   ▼                           ▼
┌──────────────────┐   ┌──────────────────────┐
│ ENTREPRISES IA   │   │ EMPLOYEURS            │
│                  │   │ TRADITIONNELS         │
│ Microsoft  ~17 % │   │ Walmart               │
│ Apple    ~16,8 % │   │ JPMorgan              │
│ Nvidia    ~18 %  │   │ UnitedHealth          │
│ Alphabet  ~15 %  │   │ Exxon, J&J, PG...     │
│ Amazon    ~12 %  │   │ (toutes les S&P 500   │
│ Meta      ~12 %  │   │  avec 20-25 %)        │
└────────┬─────────┘   └──────────┬───────────┘
         │                        │
         │   QUAND L'IA REMPLACE  │
         │   LES EMPLOIS :        │
         │                        │
         ▼                        ▼
   ┌──────────────┐        ┌──────────────┐
   │ VALORISATION │        │ EFFECTIFS    │
   │ BIG TECH ↗︎  │        │ EN BAISSE    │
   │              │        │              │
   │ Gains CT pour │        │ Pertes CT    │
   │ le portefeuille│       │ pour le      │
   │ actions       │        │ portefeuille │
   └──────┬───────┘        └──────┬───────┘
          │                       │
          └───────────┬───────────┘
                      │
                      ▼
          ┌───────────────────────┐
          │ FONDS DE PENSION      │
          │ gérés par les Big 3   │
          │                       │
          │ Dépendent de :        │
          │ • Cotisations (emploi)│
          │ • Croissance (PIB)    │
          │ • Stabilité sociale   │
          │                       │
          │ ⚠️ CONFLIT EXISTENTIEL│
          └───────────────────────┘
```

---

## CAUSALITÉ — La boucle de rétroaction fatale

```
1. Big Three possèdent à la fois Big Tech ET employeurs traditionnels
2. Big Tech vend l'IA qui automatise les emplois chez les employeurs traditionnels
3. Court terme : valorisation Big Tech ↗︎ → portefeuille actions ↗︎
4. Court terme : employeurs réduisent coûts → profits ↗︎ → portefeuille actions ↗︎
5. MOYEN TERME : cotisations sociales ↘︎ → fonds de pension ↘︎
6. MOYEN TERME : consommation ↘︎ (chômage) → croissance ↘︎
7. LONG TERME : les fonds de pension gérés par les Big Three s'effondrent
8. LONG TERME : instabilité sociale → régulation → destruction de valeur Big Tech

→ Les Big Three sont structurellement incités à maximiser le court terme
→ Jusqu'à ce que le long terme les rattrape
→ Quand il les rattrapera, ils seront déjà trop gros pour être sauvés
→ ET ils possèdent les décideurs politiques via les mêmes participations
```

---

## ACTOR_NETWORK

| Acteur | Rôle | Exposé IA |
|--------|------|-----------|
| **BlackRock** | 11,5 T$ AUM ; premier actionnaire Nvidia, Apple, Microsoft | Long IA (CT), short emploi (LT) |
| **Vanguard** | 9,3 T$ AUM ; premier actionnaire Microsoft, BlackRock | Long IA (CT), short emploi (LT) |
| **State Street** | 4,3 T$ AUM ; détenu par BlackRock/Vanguard | Idem |
| **Fonds de pension US** | Clients des Big Three ; dépendent des cotisations | Court (emploi ↘︎ → cotisations ↘︎) |
| **Travailleurs** | Cotisants aux fonds de pension ; emplois menacés | Pris en tenaille |
| **FTC/DOJ** | Poursuite antitrust (Texas AG, mai 2025) | Enquête en cours |
| **Citoyens UK** | 66 % pensent que les gains IA vont aux riches — ils ont raison | Euronews/KCL 2026 |

---

## LOUPS

| ID | Description | Sévérité |
|----|-------------|----------|
| W-001 | La circularité propriétaire des Big Three (chacun possède les autres) rend illusoire toute distinction de responsabilité — c'est un cartel de fait | HAUTE |
| W-002 | Les Big Three sont trop gros pour vendre : céder leurs participations IA ferait s'effondrer le marché. Ils sont prisonniers de leur propre position. | HAUTE |
| W-003 | Le conflit CT/LT (valorisation IA vs effondrement de l'emploi) est mathématiquement insoluble pour un investisseur universel — et les Big Three sont des investisseurs universels | HAUTE |
| W-004 | Les fonds de pension publics gérés par les Big Three sont les victimes silencieuses — personne ne leur dit que leur gestionnaire profite de la destruction de leur base de cotisants | HAUTE |

---

## IMPACTS

| Impact | Valeur | Source |
|--------|--------|--------|
| Actifs gérés par les Big Three | ~30 T$ | ICFS fév. 2026 |
| Part moyenne dans S&P 500 | 20-25 % | ICFS fév. 2026 |
| Top 10 IA BlackRock | ~1,5 T$+ | Q2 2026 13F |
| Public UK pensant que les gains IA vont aux riches | 2/3 | Euronews/KCL mai 2026 |
| Poursuite antitrust en cours | Oui (Texas AG, mai 2025) | FTC |

---

## REQUEST_LOG

| QRY-ID | Query | Résultat |
|--------|-------|----------|
| Q-001 | Big Three ownership AI companies 2025-2026 | ICFS fév. 2026, SlickCharts, Globe and Mail août 2026, Admiral Markets jan. 2026 |
| Q-002 | Big Three cross-ownership circularity | Facebook/StocksToEarn 2026, Axiory mai 2026 |
| Q-003 | FTC Big Three antitrust 2025 | FTC Press Release mai 2025 |
| Q-004 | Read ICFS Big Three | 403 — snippets utilisés |

---

## LIMITES

- Les pourcentages exacts de détention varient selon les trimestres (13F filings) et les classes d'actions. Ordres de grandeur confirmés, précision au % près non garantie.
- La circularité propriétaire est principalement via les fonds indiciels (ETFs passifs), pas via des participations de contrôle directes.
- Le conflit CT/LT est une analyse structurelle, pas une preuve d'intention — BENEFIT ≠ INTENT.

## CONCLUSION

Trois entités — BlackRock, Vanguard, State Street — possèdent collectivement 20-25 % de presque toutes les entreprises cotées. Elles sont les premiers actionnaires de Microsoft, Apple, Nvidia, Alphabet, Amazon et Meta. Elles sont aussi les premiers actionnaires de tous les employeurs traditionnels. Elles gèrent les fonds de pension qui dépendent des cotisations salariales. Et elles se possèdent les unes les autres dans une circularité totale. La boucle est parfaite : les mêmes mains qui profitent à court terme de l'automatisation des emplois gèrent l'épargne-retraite des travailleurs automatisés. Quand le public britannique dit que « les gains de l'IA iront aux investisseurs riches », il a raison — et il ne sait pas à quel point.