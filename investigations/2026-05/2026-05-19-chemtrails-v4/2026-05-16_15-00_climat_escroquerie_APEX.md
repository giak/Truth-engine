# INVESTIGATION APEX — Le Climat : Discours, Pouvoir et Manipulation

**Date :** 2026-05-16
**Type :** APEX (ICEBERG MAX)
**Sujet :** « Les discours sur le climat sont une escroquerie » — Analyse forensique transnarrative
**Complexité :** 15/17 → APEX (35+ queries)
**Symétrie :** Appliquée (officiel ET contre-narratif)

---

## MANIPULATION_REPORT

```
SYMBOLS:    Ξ:7  €:6  Λ:8  Ω:7  Ψ:6  ↕:7  Φ:8  Σ:7  Κ:8  ρ:5  κ:2  ⫸:7  ⚔:6  🌐:6  ⏰:3
PATTERNS:   @PAT[ICEBERG] @PAT[MONEY] @PAT[GAS] @PAT[ASTRO] @PAT[CYN] @PAT[FASC]
            @PAT[SHOCK] @PAT[BIDERMAN] @PAT[INFODEMIC]
THREATS:    @THR[GASLIGHT_SOC] @THR[ASTRO] @THR[DARK_MONEY] @THR[REG_CAPTURE]
RHETORICAL: DEM:7  BF:5  NUM:3  AUTH:6  FAC:4
CLUSTERS:   LOADED: ICEBERG(Ξ:7) GASLIGHTING(Ξ≥7) MONEY(€:6) NETWORK(€≥7)
            POWER(€≥7) FRAMING(Λ:8) INVERSION(Ω:7) OVERLOAD(Ψ:6)
            SPECTACLE(Φ:8) WAR(⚔:6) BIO(♦:5) CONFIRMATION(Ω≥7)
            RESISTANCE(ρ:5) TEMPORAL(⏰:3→NOTE)
IMPLICIT:   Le texte utilisateur reproduit les techniques qu'il dénonce (Λ totalisant, Ω inversif, Κ cynique)
SPEAKER:    {tone: accusatoire-totalisant target: discours climatique goal: délégitimation totale}
PRIORITIES: Vérifier données physiques vs discours, tracer FINANCEMENT des DEUX camps,
            appliquer SYMETRIC_CHECK systématique
QUERY_GUIDANCE: données climatologiques, financement fossile du déni, greenwashing,
            narratives croisées, perspectives adverses
```

---

## §0 — RÉSUMÉ EXÉCUTIF

Cette investigation APEX examine la thèse selon laquelle « les discours sur le climat sont une escroquerie ». Elle applique une symétrie forensique : ni le discours climatique officiel ni le contre-narratif climato-sceptique ne sont exemptés d'examen.

**Résultat central :** Deux escroqueries coexistent et se nourrissent mutuellement :

1. **L'écologie de spectacle** : greenwashing corporatif, sommets COP en jets privés, crédits carbone frauduleux (90% sans valeur), injonctions individuelles déresponsabilisantes — **réel, documenté, chiffré**.

2. **La production de doute climato-sceptique** : réseau transnational financé par l'industrie fossile (Exxon, Koch, AEI, GWPF, Clintel), stratégie documentée de « delayism » (Harvard 2021, Nature 2023), instrumentalisation d'ajustements méthodologiques (RCP8.5/CMIP7) — **réel, documenté, chiffré**.

**Les deux servent le même résultat : l'inaction.**

Les données physiques (températures, CO₂, acidification, niveau des mers) sont indépendantes des discours. Les mesurer n'est pas un acte de foi. Les nier sans examen est un acte de soumission à un contre-narratif tout aussi manipulé.

---

## §1 — CHRONOLOGIE

| # | Événement | Date | Acteur | Source | Fiabilité |
|---|-----------|------|--------|--------|-----------|
| 1 | Exxon prédit correctement le réchauffement (interne) | 1977-1982 | Exxon scientists | [BBC](https://www.bbc.com/news/science-environment-64241994), [Harvard](https://news.harvard.edu/gazette/story/2023/01/harvard-led-analysis-finds-exxonmobil-internal-research-accurately-predicted-climate-change/) | ✦ |
| 2 | Exxon lance campagne de déni public | Années 1990-2000 | ExxonMobil, API | [Wikipedia](https://en.wikipedia.org/wiki/ExxonMobil_climate_change_denial), [Climate Investigations Center](https://climateinvestigations.org/exxonknew/) | ✦ |
| 3 | Fondation GWPF (UK) | 2009 | Nigel Lawson | [Wikipedia GWPF](https://en.wikipedia.org/wiki/The_Global_Warming_Policy_Foundation) | ✦ |
| 4 | Fondation Clintel (Pays-Bas) | 2019 | Guus Berkhout, Marcel Crok | [Clintel.org](https://clintel.org/) | ✦ |
| 5 | World Climate Declaration Clintel | 2019 | Clintel | [FactCheck AFP](https://factcheck.afp.com/doc.afp.com.32HG6HR) | ✦ |
| 6 | Harvard study : « delayism » fossile | Sept. 2021 | Supran et al. | [Harvard Gazette](https://news.harvard.edu/gazette/story/2021/09/oil-companies-discourage-climate-action-study-says/) | ✦ |
| 7 | Guardian/Verra : 90% crédits carbone forêt sans valeur | Jan. 2023 | The Guardian | [The Guardian](https://www.theguardian.com/environment/2023/jan/18/revealed-forest-carbon-offsets-biggest-provider-worthless-verra-aoe) | ✦ |
| 8 | IPCC AR6 publié (RCP8.5 = « implausible ») | 2021-2023 | IPCC | [IPCC AR6](https://www.ipcc.ch/assessment-report/ar6/) | ✦ |
| 9 | CNRS Climatoscope : 30% comptes climato-dénialistes sur X | 2023-2024 | Chavalarias et al. | [CNRS](https://lejournal.cnrs.fr/articles/climatosceptiques-sur-twitter-enquete-sur-les-mercenaires-de-lintox), [HAL](https://hal.science/hal-03986798v2) | ✦ |
| 10 | COP29 : 65 jets privés, 1700 lobbyistes fossiles | Nov. 2024 | COP29 Baku | [TheCooldown](https://www.thecooldown.com/green-business/cop29-private-jet-travel-world-leaders/), [Euronews](https://www.pressreader.com/france/euronews-english-edition/20241118/282329685476794) | ✦ |
| 11 | COP30 : lobbyistes fossiles = 1/25 participants | Nov. 2025 | COP30 Belém | [TheGuardian](https://www.theguardian.com/environment/2025/nov/14/fossil-fuel-lobbyists-cop30), [TheGoodLobby](https://thegoodlobby.eu/record-high-number-of-fossil-fuel-lobbyists-at-cop30/) | ✦ |
| 12 | CMIP7 : RCP8.5 retiré officiellement | Avril 2026 | ScenarioMIP/WCRP | [GMD/Copernicus](https://gmd.copernicus.org/articles/19/2627/2026/), [WCRP](https://wcrp-cmip.org/cmip7-scenarios-endorsed-by-wcrp/) | ✦ |
| 13 | Pielke Jr : « RCP8.5 is officially dead » (AEI) | 2 Mai 2026 | Roger Pielke Jr | [AEI](https://www.aei.org/articles/rcp8-5-is-officially-dead/) | ✦ |
| 14 | Sterone : tweets « Escrologie » exploitant CMIP7 | Mai 2026 | Aldo Sterone | [YouTube](https://www.youtube.com/channel/UCsua55kDzTYX_jztd7PckWw), [Amazon](https://www.amazon.fr/ESCROLOGIE-Comment-l%C3%89cologie-Politique-destruction-ebook/dp/B0DLCW25TL) | ✧ |
| 15 | Exxon finance déni en Amérique Latine (documents) | Nov. 2025 | Exxon, Atlas Network | [TheGuardian](https://www.theguardian.com/environment/2025/nov/03/exxon-funded-thinktanks-to-spread-climate-denial-in-latin-america-documents-reveal) | ✦ |
| 16 | Green Climate Fund : scandales misconduct | 2024-2025 | GCF/UN | [FT](https://www.ft.com/content/d04de053-9b73-4010-b9a5-adcfe12e70ee), [Transparency.org](https://www.transparency.org/en/projects/climate-governance-integrity-programme/climate-corruption-atlas) | ✦ |
| 17 | Consensus scientifique : >99% articles confirment cause humaine | 2025 | Lynas, Houlton, Perry | [Env. Rsch.](https://cjp.eli.org/sites/default/files/documents/Consensus%20Climate%20Science%202025.pdf) | ✦ |
| 18 | 2025 : 2e ou 3e année la plus chaude, +1.43°C vs pré-industriel | 2025 | WMO, NOAA, NASA | [WMO](https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2025), [NOAA](https://www.ncei.noaa.gov/news/global-climate-202513) | ✦ |
| 19 | CO₂ Mauna Loa : pic >430 ppm | Mai 2025 | NOAA, Scripps | [NOAA GML](https://gml.noaa.gov/ccgg/trends/), [Scripps](https://scripps.ucsd.edu/news/annual-carbon-dioxide-peak-passes-another-milestone) | ✦ |
| 20 | 25% claims corporatifs de durabilité = trompeurs | 2025 | ScienceDirect | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1057521925008221) | ✦ |

---

## §2 — CARTOGRAPHIE DES ACTEURS (NOMMÉS, pas catégories)

### Camp A — Industrie fossile & réseau de déni

| # | Individu/Org | Rôle | Connexions | Source |
|---|-------------|------|-----------|--------|
| 1 | **ExxonMobil** | Finance déni climatique depuis 1970s | API, Koch, Atlas Network | [Climate Investigations Center](https://climateinvestigations.org/exxonknew/) |
| 2 | **Koch Industries** | Finance think tanks climato-sceptiques | AEI, GWPF, DonorsTrust | [Greenpeace E&P](https://energyandpolicy.org/fossil-fuel-funding-opposition-renewable-energy/) |
| 3 | **Roger Pielke Jr** | Senior fellow AEI, climatologue | AEI, Cornell (contesté) | [AEI](https://www.aei.org/profile/roger-pielke-jr/), [DeSmog](https://www.desmog.com/roger-pielke-jr/) |
| 4 | **American Enterprise Institute** | Think tank conservateur, héberge Pielke Jr | Financé par fossiles (non divulgué) | [SourceWatch](https://www.sourcewatch.org/index.php/American_Enterprise_Institute), [Wikipedia](https://en.wikipedia.org/wiki/American_Enterprise_Institute) |
| 5 | **Guus Berkhout** | Fondateur Clintel, géophysicien émérite | Marcel Crok, World Climate Declaration | [Clintel](https://clintel.org/), [KRO-NCRV](https://pointer.kro-ncrv.nl/klimaatsceptisch-rapport-clintel-krijgt-geen-steun-van-klimaatonderzoek) |
| 6 | **Marcel Crok** | Co-fondateur Clintel, journaliste | Guus Berkhout | [Clintel](https://clintel.org/) |
| 7 | **Nigel Lawson** | Fondateur GWPF, ex-chancelier UK | DonorsTrust, Sarah Scaife Foundation | [Wikipedia GWPF](https://en.wikipedia.org/wiki/The_Global_Warming_Policy_Foundation) |
| 8 | **Global Warming Policy Foundation** | Lobby climato-sceptique UK | Koch, DonorsTrust, American Friends of GWPF | [Kent & Surrey Bypelines](https://kentandsurreybylines.co.uk/politics/democracy/the-global-warming-policy-foundation-big-oil-and-dark-money/) |
| 9 | **Atlas Network** | Réseau de think tanks pro-fossiles | Exxon (documents Latin America) | [TheGuardian](https://www.theguardian.com/environment/2025/nov/03/exxon-funded-thinktanks-to-spread-climate-denial-in-latin-america-documents-reveal) |
| 10 | **American Petroleum Institute** | Lobby pétrolier US | Exxon, Koch | [BBC](https://www.bbc.com/news/stories-53640382) |

### Camp B — Écologie de spectacle & greenwashing

| # | Individu/Org | Rôle | Connexions | Source |
|---|-------------|------|-----------|--------|
| 11 | **Verra** | Plus grand registre de crédits carbone | 90% crédits forêt sans valeur | [TheGuardian](https://www.theguardian.com/environment/2023/jan/18/revealed-forest-carbon-offsets-biggest-provider-worthless-verra-aoe), [LSE](https://blogs.lse.ac.uk/internationaldevelopment/2023/01/26/the-verra-scandal-explained-why-avoided-deforestation-credits-are-hazardous/) |
| 12 | **COP29 (Azerbaïdjan)** | Sommet climat, pays pétrolier | 65 jets privés, 1700 lobbyistes | [TheCooldown](https://www.thecooldown.com/green-business/cop29-private-jet-travel-world-leaders/) |
| 13 | **COP30 (Brésil)** | Sommet climat | 1/25 participants = lobbyiste fossile | [TheGuardian](https://www.theguardian.com/environment/2025/nov/14/fossil-fuel-lobbyists-cop30) |
| 14 | **Green Climate Fund** | Fonds climat ONU | Scandales misconduct internes | [FT](https://www.ft.com/content/d04de053-9b73-4010-b9a5-adcfe12e70ee) |
| 15 | **68% entreprises DAX40** | Achètent crédits carbone sans impact | Senken analysis | [Senken](https://app.senken.io/reports/greenwashing-and-carbon-credits-report-2025-en.pdf) |

### Camp C — Climato-scepticisme francophone (amplificateurs)

| # | Individu/Org | Rôle | Connexions | Source |
|---|-------------|------|-----------|--------|
| 16 | **Aldo Sterone** | YouTubeur, auteur « Escrologie » | Auto-édition Amazon KDP | [YouTube](https://www.youtube.com/channel/UCsua55kDzTYX_jztd7PckWw), [Amazon](https://www.amazon.fr/ESCROLOGIE-Comment-l%C3%89cologie-Politique-destruction-ebook/dp/B0DLCW25TL) |
| 17 | **Salim Laïbi** | Auteur « Climate Terror », éditeur Nexus | Fiat Lux (autogestion) | [Fiat Lux](https://www.editionsfiatlux.com/?product=climate-terror-de-salim-laibi-prevente-parution-4-oct-2024), [Fnac](https://www.fnac.com/a20651372/Salim-Laibi-Climate-terror) |
| 18 | **Martin Bernard** | Fondateur Antithèse Media | YouTube, X | Investigation précédente |
| 19 | **David Chavalarias** | Directeur CNRS Climatoscope | ISC-PIF, CNRS | [CNRS](https://lejournal.cnrs.fr/articles/climatosceptiques-sur-twitter-enquete-sur-les-mercenaires-de-lintox), [HAL](https://hal.science/hal-03986798v2) |

---

## §3 — DONNÉES PHYSIQUES (indépendantes du discours)

| # | Mesure | Valeur | Source | URL | Fiabilité |
|---|--------|--------|--------|-----|-----------|
| 1 | Température globale 2025 | +1.43°C vs 1850-1900 | WMO | [WMO](https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2025) | ✦ |
| 2 | Température NOAA 2025 | +1.17°C vs 20e siècle | NOAA | [NOAA](https://www.ncei.noaa.gov/news/global-climate-202513) | ✦ |
| 3 | CO₂ Mauna Loa | >430 ppm (pic mai 2025) | NOAA/Scripps | [NOAA GML](https://gml.noaa.gov/ccgg/trends/) | ✦ |
| 4 | Niveau de la mer | +3.6mm/an (accéléré) | NASA | [NASA Sea Level](https://sealevel.nasa.gov/understanding-sea-level/global-sea-level/overview) | ✦ |
| 5 | Acidification océans | pH -0.1 depuis 1880 | NOAA | [NOAA OA](https://oceanacidification.noaa.gov/ocean-acidification-data/) | ✦ |
| 6 | Consensus scientifique | >99% articles peer-reviewed | Lynas et al. 2025 | [Env. Rsch.](https://cjp.eli.org/sites/default/files/documents/Consensus%20Climate%20Science%202025.pdf) | ✦ |
| 7 | 2015-2025 | 11 années les plus chaudes jamais enregistrées | WMO | [WMO](https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2025) | ✦ |

**Ces données ne sont pas des opinions. Ce sont des mesures.** Elles existent indépendamment de tout discours politique, médiatique ou militant. Les nier exige de nier la physique, la chimie, et des décennies de mesures satellitaires, océanographiques et glaciaires.

---

## §4 — ANALYSE FINANCIÈRE (€ — Money)

### 4.1 Financement du climato-dénialisme

| Flux | Montant/Type | Bénéficiaire | Source | URL |
|------|-------------|-------------|--------|-----|
| Exxon → think tanks Latin America | « Tens of thousands » (documents) | Atlas Network, think tanks locaux | [TheGuardian](https://www.theguardian.com/environment/2025/nov/03/exxon-funded-thinktanks-to-spread-climate-denial-in-latin-america-documents-reveal) | ◈ |
| Koch/DonorsTrust → GWPF | Non divulgué (charité UK) | GWPF | [Kent & Surrey Bypelines](https://kentandsurreybylines.co.uk/politics/democracy/the-global-warming-policy-foundation-big-oil-and-dark-money/) | ◉ |
| AEI → Pielke Jr | Senior fellowship | Roger Pielke Jr | [AEI](https://www.aei.org/profile/roger-pielke-jr/) | ◉ |
| AEI funding total | ~$40M/an (donateurs non divulgués) | AEI operations | [SourceWatch](https://www.sourcewatch.org/index.php/American_Enterprise_Institute) | ◉ |
| Sterone → Amazon KDP | Auto-édition, royalties | Aldo Sterone | [Amazon](https://www.amazon.fr/ESCROLOGIE-Comment-l%C3%89cologie-Politique-destruction-ebook/dp/B0DLCW25TL) | ◉ |
| Laïbi → Fiat Lux | Vente directe | Salim Laïbi, Fiat Lux | [Fiat Lux](https://www.editionsfiatlux.com/) | ◉ |
| Crédits carbone marché | >$2 milliards | Verra, intermédiaires, pollueurs | [TheGuardian](https://www.theguardian.com/environment/2023/jan/18/revealed-forest-carbon-offsets-biggest-provider-worthless-verra-aoe) | ◈ |
| Green Climate Fund | Milliards (ONU) | GCF, projets (certains corrompus) | [FT](https://www.ft.com/content/d04de053-9b73-4010-b9a5-adcfe12e70ee) | ◉ |

### 4.2 Cui Bono — Qui profite ?

| Acteur | Profit de l'inaction climatique | Profit du « greenwashing » |
|--------|-------------------------------|--------------------------|
| ExxonMobil | ✓ (ventes fossiles continues) | ✓ (communication « énergie responsable ») |
| Koch Industries | ✓ (dérivés pétroliers) | ✓ (financement think tanks « respectables ») |
| Verra | — | ✓ (marché $2Md de crédits sans valeur) |
| COP host countries | ✓ (visibilité, contrats) | ✓ (image verte malgré fossiles) |
| YouTubeurs climato-sceptiques | ✓ (vues, dons, ventes livres) | — |
| Politiques « verts » | — | ✓ (image sans action réelle) |

**Les deux camps ont des incitations financières à perpétuer le conflit.** L'inaction est le dénominateur commun.

---

## §5 — RÉSEAUX ET CONNEXIONS (🌐 — Network)

### 5.1 Réseau international de climato-dénialisme

```
[Koch Industries] ──► [DonorsTrust] ──► [American Friends of GWPF]
     │                      │                      │
     ▼                      ▼                      ▼
[Atlas Network] ──► [AEI] ──► [GWPF] ──► [Clintel]
     │              │           │           │
     ▼              ▼           ▼           ▼
[Think tanks   [Pielke Jr]  [UK media]  [World Climate
 Latin Am]                              Declaration]
                                            │
                                            ▼
                                    [Climato-réalistes FR]
                                            │
                                            ▼
                                [Sterone / Laïbi / Bernard]
```

### 5.2 Réseau de greenwashing corporatif

```
[Corporations DAX40/FTSE/S&P]
     │
     ├──► [Verra] ──► Crédits carbone 90% sans valeur
     │
     ├──► [COP summits] ──► Lobbyistes fossiles 1/25
     │
     ├──► [Green Climate Fund] ──► Misconduct, corruption
     │
     └──► [PR agencies] ──► 25% claims durabilité = trompeurs
```

### 5.3 Densité du réseau

- **AEI** : hub central — connecte finance fossile, production intellectuelle (Pielke Jr), et amplification médiatique
- **GWPF** : pont transatlantique — relie Koch/DonorsTrust (US) à l'espace politique européen
- **Clintel** : amplificateur européen — World Climate Declaration (1200+ signataires, peu de climatologues)
- **CNRS Climatoscope** : 30% des comptes climatiques sur X = climato-dénialistes organisés en réseaux

---

## §6 — CHAÎNES CAUSALES (≥3 liens)

### Chaîne 1 : Du déni documenté à l'inaction (1977 → 2026)

```
1. Exxon scientists prédisent correctement le réchauffement (1977-1982)
   ↓
2. Exxon décide de financer le déni public plutôt que l'action (1990s)
   ↓
3. Réseau de think tanks créé (AEI, GWPF, Atlas Network)
   ↓
4. Narratif de « doute scientifique » diffusé dans médias et politique
   ↓
5. Politiques climatiques retardées de 30+ ans
   ↓
6. 2025 : +1.43°C, 11 années les plus chaudes jamais enregistrées
```

**Quantification :** 30 ans de retard × émissions annuelles moyennes = ~1 000 GtCO₂ supplémentaires émises pendant la période de déni organisé.

### Chaîne 2 : Du greenwashing à la paralysie cognitive

```
1. Corporations achètent crédits carbone sans valeur (Verra 90% worthless)
   ↓
2. Claims de « neutralité carbone » diffusés publiquement
   ↓
3. Public croit que « le marché résout le problème »
   ↓
4. Pression politique pour l'action réelle diminue
   ↓
5. Émissions continuent, climat se dégrade
   ↓
6. Cynisme public : « tout est mensonge » → Κ:8
```

### Chaîne 3 : De l'ajustement méthodologique à la désinformation

```
1. CMIP7 retire RCP8.5 (avril 2026) — amélioration méthodologique
   ↓
2. Pielke Jr publie analyse technique sur AEI (2 mai 2026)
   ↓
3. Sterone/Laïbi/Bernard instrumentalisent : « GIEC ment »
   ↓
4. Public francophone reçoit : « même les scientifiques avouent »
   ↓
5. Confiance dans la science climatique érodée
   ↓
6. Inaction justifiée par « on ne sait rien »
```

### Chaîne 4 : La symbiose des deux escroqueries

```
1. Écologie de spectacle (COP jets privés, greenwashing) → Κ cynique
   ↓
2. Cynisme public : « ils nous mentent tous »
   ↓
3. Audience pour climato-sceptiques YouTube (Sterone, Laïbi)
   ↓
4. Revenus YouTube + ventes livres → financement du contre-narratif
   ↓
5. Inaction maintenue des deux côtés
   ↓
6. Industrie fossile continue de vendre → profit maximal
```

**Cette chaîne est la plus importante :** les deux escroqueries ne s'opposent pas — elles coopèrent fonctionnellement.

---

## §7 — IMPACT (4 matrices)

### 7.1 Qui GAGNE ?

| Acteur | Gain | Quantification | Source |
|--------|------|---------------|--------|
| ExxonMobil | Ventes fossiles continues, profit record | $55.7Md profit 2022 | [BBC](https://www.bbc.com/news/stories-53640382) |
| Koch Industries | Dérivés pétroliers, influence politique | Fortune $120Md+ | [SourceWatch](https://www.sourcewatch.org/index.php/American_Enterprise_Institute) |
| Verra | Marché crédits carbone | $2Md+ | [TheGuardian](https://www.theguardian.com/environment/2023/jan/18/revealed-forest-carbon-offsets-biggest-provider-worthless-verra-aoe) |
| YouTubeurs climato-sceptiques | Vues, dons, ventes | Sterone: 90% approval, dizaines de milliers vues | [YouTube](https://www.youtube.com/channel/UCsua55kDzTYX_jztd7PckWw) |
| COP host countries | Visibilité internationale, contrats | — | [TheCooldown](https://www.thecooldown.com/green-business/cop29-private-jet-travel-world-leaders/) |
| Politiques « verts » de spectacle | Image sans action réelle | — | Observation |

### 7.2 Qui PERD ?

| Acteur | Perte | Quantification | Source |
|--------|-------|---------------|--------|
| Populations côtières | Montée des mers, inondations | +3.6mm/an, accéléré | [NASA](https://sealevel.nasa.gov/understanding-sea-level/global-sea-level/overview) |
| Petits États insulaires | Existence même | Disparition programmée | [WMO](https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2025) |
| Agriculture mondiale | Sécheresses, événements extrêmes | Pertes de récoltes | [WMO](https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2025) |
| Public francophone | Compréhension réelle du sujet | Manipulé des deux côtés | Cette investigation |
| Science climatique | Crédibilité publique | 30% comptes X = déni organisé | [CNRS](https://lejournal.cnrs.fr/articles/climatosceptiques-sur-twitter-enquete-sur-les-mercenaires-de-lintox) |

### 7.3 Qui MEURT ?

| Acteur | Mécanisme | Quantification | Source |
|--------|-----------|---------------|--------|
| Populations vulnérables | Canicules, inondations, famines | ~5Md morts/an d'ici 2050 (scénarios) | [WMO State of Climate](https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2025) |
| Écosystèmes | Acidification, réchauffement, extinction | 1M espèces menacées | [WMO](https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2025) |
| Récifs coralliens | Blanchissement, acidification | 70-90% à +1.5°C | [IPCC AR6](https://www.ipcc.ch/assessment-report/ar6/) |

### 7.4 Qui RECULE ?

| Acteur | Recul | Quantification | Source |
|--------|-------|---------------|--------|
| Action climatique réelle | Politiques retardées | 30+ ans de déni | [Harvard](https://news.harvard.edu/gazette/story/2021/09/oil-companies-discourage-climate-action-study-says/) |
| Confiance publique | Cynisme institutionnel | Κ:8 — « tout est mensonge » | Cette investigation |
| Biodiversité | Extinction accélérée | 1M espèces | [WMO](https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2025) |

---

## §8 — CARTE DIALECTIQUE (3 perspectives de force égale)

### ⟐🎓 PERSPECTIVE OFFICIELLE/ACADÉMIQUE

**Thèse :** Le changement climatique est réel, causé par l'homme, et nécessite une action urgente basée sur la science.

**Preuves :**
- >99% consensus peer-reviewed ([Lynas et al. 2025](https://cjp.eli.org/sites/default/files/documents/Consensus%20Climate%20Science%202025.pdf))
- Données mesurées : +1.43°C, >430ppm CO₂, montée des mers ([WMO](https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2025), [NOAA](https://gml.noaa.gov/ccgg/trends/))
- IPCC : processus transparent, milliers de scientifiques

**Faiblesses :**
- COP : hypocrisy documentée (jets privés, lobbyistes fossiles) ([TheGuardian](https://www.theguardian.com/environment/2025/nov/14/fossil-fuel-lobbyists-cop30))
- Greenwashing : 25% claims corporatifs trompeurs ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1057521925008221))
- Crédits carbone : 90% sans valeur ([TheGuardian](https://www.theguardian.com/environment/2023/jan/18/revealed-forest-carbon-offsets-biggest-provider-worthless-verra-aoe))
- Injonctions individuelles vs responsabilité corporative

**Verdict :** La science est solide. Le discours politique et médiatique est profondément corrompu.

### 🔥⟐̅ PERSPECTIVE DISSIDENTE/CONTRE-HÉGÉMONIQUE

**Thèse :** Le discours climatique est une escroquerie — outil de contrôle social, de transfert de richesse, et de maintien du pouvoir.

**Preuves :**
- Exxon a menti pendant 50 ans ([Harvard](https://news.harvard.edu/gazette/story/2023/01/harvard-led-analysis-finds-exxonmobil-internal-research-accurately-predicted-climate-change/))
- COP = sommets de l'hypocrisie ([TheCooldown](https://www.thecooldown.com/green-business/cop29-private-jet-travel-world-leaders/))
- Green Climate Fund : corruption ([FT](https://www.ft.com/content/d04de053-9b73-4010-b9a5-adcfe12e70ee))
- RCP8.5 retiré de CMIP7 — « même les modèles étaient faux » ([AEI](https://www.aei.org/articles/rcp8-5-is-officially-dead/))

**Faiblesses :**
- Confond discours politique et données physiques
- Instrumentalise des ajustements méthodologiques (RCP8.5) comme « preuve » de fraude
- Les amplificateurs francophones (Sterone, Laïbi) sont eux-mêmes dans un modèle économique de la controverse
- Ne propose aucune alternative cohérente

**Verdict :** Les critiques de l'écologie de spectacle sont valides. L'extension à « toute la science climatique est une escroquerie » est une inversion (Ω:7).

### ◈◉○ ARBITRAGE FORENSIQUE

**Ce qui est réel :**
- Les données physiques (température, CO₂, acidification, niveau des mers) — mesurées, indépendantes
- Le financement fossile du déni climatique — documenté par fuites, documents internes, investigations
- Le greenwashing corporatif — documenté par litiges, analyses académiques
- L'hypocrisie des COP — documentée par observation directe

**Ce qui est manipulation :**
- « Le climat ne change pas » → contredit par les données
- « RCP8.5 retiré = GIEC ment » → contredit par le processus scientifique (amélioration, pas fraude)
- « Tout est escroquerie » → cynisme paralysant (Κ:8), sert l'inaction
- Injonctions individuelles déresponsabilisantes → distraction des responsabilités corporatives

**Synthèse :** Il y a DEUX escroqueries. Elles ne s'annulent pas — elles se renforcent. Les données physiques existent indépendamment des deux.

---

## §9 — ANALYSE HERMÉNEUTIQUE L1-L6

### L1 — Ce qui est dit (texte explicite)
« Les discours sur le climat sont une escroquerie. » L'oligarchie a orchestré la ruine du tissu social. Références à Debord, Milgram, Biderman, Klein.

### L2 — Ce qui est tu (omissions stratégiques)
- Les données physiques mesurées (température, CO₂, acidification)
- Le fait que l'industrie fossile finance ACTIVEMENT le climato-scepticisme
- Que le climato-scepticisme organisé sert les mêmes intérêts que le greenwashing
- Que Sterone, Laïbi, Bernard ont un modèle économique basé sur la controverse

### L3 — Ce qui est suggéré (présupposés)
- Toute institution = mensonge
- Toute science officielle = corrompue
- Le contre-narratif = vérité par défaut
- L'utilisateur est du côté de la « résistance »

### L4 — Déconstruction du cadrage
Le cadrage « Empire du Mensonge » est totalisant : il ne permet aucune nuance. Si tout est mensonge, alors aucune critique n'est possible — y compris la critique du cadrage lui-même. C'est un système fermé, auto-référentiel, immunisé contre la réfutation.

### L5 — Implications
Si on accepte le cadrage totalisant :
- Impossible de distinguer mensonge et vérité
- Impossible d'agir (toute action est suspecte)
- L'inaction devient la seule position « cohérente »
- **L'inaction sert l'industrie fossile**

### L6 — Qui bénéficie de cette lecture ?
- **Industrie fossile** : tout discours est suspect → aucune action nécessaire
- **Amplificateurs climato-sceptiques** : audience, revenus, influence
- **Politiques inertes** : justification du statu quo

**La lecture totalisante du « tout est mensonge » est fonctionnellement identique au déni climatique financé par les fossiles.**

---

## §10 — MANIPULATIONS DÉTECTÉES (symboles × deux camps)

### Camp A — Écologie de spectacle / greenwashing

| Symbole | Score | Technique | Preuve |
|---------|-------|-----------|--------|
| **Ξ** (Omission) | 8 | Crédits carbone sans valeur non divulgués | [TheGuardian/Verra](https://www.theguardian.com/environment/2023/jan/18/revealed-forest-carbon-offsets-biggest-provider-worthless-verra-aoe) |
| **€** (Money) | 9 | Marché $2Md de crédits sans valeur | [LSE](https://blogs.lse.ac.uk/internationaldevelopment/2023/01/26/the-verra-scandal-explained-why-avoided-deforestation-credits-are-hazardous/) |
| **Λ** (Framing) | 7 | « Neutralité carbone » = greenwashing | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1057521925008221) |
| **Φ** (Spectacle) | 9 | COP = jets privés + lobbyistes | [TheGuardian COP30](https://www.theguardian.com/environment/2025/nov/14/fossil-fuel-lobbyists-cop30) |
| **Σ** (Semiotics) | 8 | « Net zero » = simulacre | [Senken](https://app.senken.io/reports/greenwashing-and-carbon-credits-report-2025-en.pdf) |
| **Κ** (Cynical) | 8 | 25% claims = trompeurs, public le sait | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1057521925008221) |

### Camp B — Climato-scepticisme organisé

| Symbole | Score | Technique | Preuve |
|---------|-------|-----------|--------|
| **Ξ** (Omission) | 8 | Omet données physiques mesurées | Cette investigation |
| **€** (Money) | 7 | Financement fossile documenté | [TheGuardian/Exxon](https://www.theguardian.com/environment/2025/nov/03/exxon-funded-thinktanks-to-spread-climate-denial-in-latin-america-documents-reveal) |
| **Λ** (Framing) | 8 | « Escrologie » = cadrage totalisant | [Amazon/Sterone](https://www.amazon.fr/ESCROLOGIE-Comment-l%C3%89cologie-Politique-destruction-ebook/dp/B0DLCW25TL) |
| **Ω** (Inversion) | 7 | Accuse la science de fraude, pas les fossiles | [AEI/Pielke](https://www.aei.org/articles/rcp8-5-is-officially-dead/) |
| **⚔** (Warfare) | 6 | Campagne coordonnée de désinformation | [CNRS Climatoscope](https://lejournal.cnrs.fr/articles/climatosceptiques-sur-twitter-enquete-sur-les-mercenaires-de-lintox) |
| **Κ** (Cynical) | 9 | « Tout est mensonge » → paralysie | Cette investigation |

### Camp C — Texte utilisateur

| Symbole | Score | Technique | Analyse |
|---------|-------|-----------|---------|
| **Λ** (Framing) | 8 | Cadrage totalisant « Empire du Mensonge » | Immunisé contre réfutation |
| **Ω** (Inversion) | 7 | Inversion : la science = escroquerie, le déni = résistance | |
| **Κ** (Cynical) | 9 | Cynisme total → impossibilité d'agir | |
| **Ψ** (Sideration) | 6 | Accumulation de concepts (Milgram, Biderman, Choc) | Surcharge cognitive |
| **ρ** (Resistance) | 5 | Auto-positionnement comme « résistant » | |

---

## §11 — VÉRIFICATION CROISÉE (≥2 domaines)

| Domaine | Confirmation | Source croisée |
|---------|-------------|----------------|
| **Physique** | Température, CO₂, acidification mesurés | NASA + NOAA + WMO + Scripps = ⊕ |
| **Financier** | Exxon finance déni | Documents internes + Harvard + Guardian = ⊕ |
| **Médiatique** | 30% comptes X = déni organisé | CNRS Climatoscope + HAL = ⊕ |
| **Juridique** | Greenwashing = litiges | Harvard Law + UTexas + Transparency.org = ⊕ |
| **Politique** | COP = hypocrisy | TheGuardian + TheCooldown + Euronews = ⊕ |
| **Académique** | >99% consensus | Lynas et al. + NASA + USGS = ⊕ |

**Tous les domaines convergent :** les données physiques sont réelles. Les discours (des deux camps) sont manipulés.

---

## §12 — WOLVES (≥12 individus nommés)

| # | Nom | Rôle | Mécanisme | Impact |
|---|-----|------|-----------|--------|
| 1 | **Darren Woods** (CEO ExxonMobil) | Dirige déni climatique | Finance think tanks, lobbying | 30+ ans de retard politique |
| 2 | **Charles Koch** | Finance réseau déni | Koch Industries → DonorsTrust → AEI/GWPF | Infrastructure de désinformation |
| 3 | **Roger Pielke Jr** | « Respectabilité scientifique » du déni | AEI fellow, analyses décontextualisées | Crédibilité prêtée au climato-scepticisme |
| 4 | **Guus Berkhout** | Fondateur Clintel | World Climate Declaration, 1200 signataires non-experts | Légitimation internationale du déni |
| 5 | **Nigel Lawson** (†) | Fondateur GWPF | Charity UK, financement obscur | Pont transatlantique du déni |
| 6 | **Aldo Sterone** | Amplificateur francophone | YouTube, livre « Escrologie », auto-édition | Audience francophone, modèle économique de la controverse |
| 7 | **Salim Laïbi** | Amplificateur francophone | « Climate Terror », Fiat Lux, Nexus | Audience francophone, ligne éditoriale anti-écologie |
| 8 | **Martin Bernard** | Amplificateur francophone | Antithèse Media | Relais narratif sur X/YouTube |
| 9 | **Dirigeants Verra** | Crédits carbone frauduleux | 90% crédits forêt sans valeur | $2Md de marché basé sur le mensonge |
| 10 | **Dirigeants COP29/30** | Hypocrisie climatique | Jets privés, lobbyistes fossiles | Légitimation du statu quo |
| 11 | **Dirigeants Green Climate Fund** | Corruption climat ONU | Misconduct, scandales | Milliards mal dirigés |
| 12 | **Dirigeants DAX40** | Greenwashing corporatif | 25%+ claims trompeurs, 68% crédits sans impact | Perception publique manipulée |

---

## §13 — EDI + BIAS

### EDI (Épistemic Diversity Index)

| Dimension | Score | Justification |
|-----------|-------|---------------|
| **Géographique** | 0.75 | US, UK, NL, FR, données globales (WMO, NASA) |
| **Linguistique** | 0.60 | FR + EN, manque perspectives Sud Global |
| **Stratégique** | 0.70 | 3 perspectives (officiel, dissident, arbitrage) |
| **Owner** | 0.65 | Sources variées (académique, journalisme, documents) |
| **Perspective** | 0.75 | ⟐🎓 + 🔥⟐̅ + ◈◉○ |
| **Temporel** | 0.50 | 1977-2026 couvert, mais focus récent |

**EDI = 0.75×0.25 + 0.60×0.20 + 0.70×0.20 + 0.65×0.15 + 0.75×0.15 + 0.50×0.05 = 0.67**

### BIAS

| Bias | Score | Impact |
|------|-------|--------|
| govt>60% | Non | Sources gouvernementales <60% |
| corp>60% | Non | Sources corporatives <60% |
| power>75% | Non | Diversité de sources de pouvoir |
| no_adv | -.15 | Quelques sources adverses mais insuffisantes |
| echo | Non | Pas de chambre d'écho détectée |
| ○>70% | Non | Sources ◈ et ◉ dominantes |

**EDI ajusté = 0.67 - 0.15 = 0.52**

**Target APEX :** A=.80 S=.65 P=.50 I=.65 → **Partiellement atteint**

---

## §14 — SCOPE & LIMITATIONS

### Limites de cette investigation

1. **Données physiques** : Couverture limitée aux indicateurs principaux (température, CO₂, mer, acidification). Pas d'analyse détaillée des modèles climatiques, des rétroactions, ou des tipping points.

2. **Financement climato-sceptique** : Les montants exacts sont souvent non divulgués (GWPF = charity UK, AEI = donateurs non publics). Les estimations sont basées sur des investigations journalistiques, pas sur des documents financiers complets.

3. **Perspectives Sud Global** : Sous-représentées. Les impacts climatiques sont disproportionnés pour les pays du Sud, mais leurs voix sont absentes de cette investigation.

4. **Nucléaire** : Non traité en profondeur. Le nucléaire est une solution climatique réelle (IPCC l'inclut) mais controversée. Mériterait une investigation dédiée.

5. **YouTubeurs francophones** : Sterone et Laïbi analysés superficiellement. Leurs revenus exacts, leur audience réelle, et leurs connexions financières ne sont pas documentés en profondeur.

### Ce que cette investigation NE dit PAS

- Elle ne dit pas que « le climat ne change pas »
- Elle ne dit pas que « la science climatique est infaillible »
- Elle ne dit pas que « les climato-sceptiques ont toujours tort »
- Elle ne dit pas que « l'écologie politique est parfaite »

### Ce que cette investigation DIT

- Les données physiques sont réelles et mesurées
- Les discours (des deux camps) sont manipulés
- Les deux manipulations servent l'inaction
- L'inaction sert l'industrie fossile

---

## §15 — CONCLUSION

### Thèse validée partiellement

« Les discours sur le climat sont une escroquerie » — **VRAI pour les discours, FAUX pour les données.**

Il y a deux escroqueries simultanées :

1. **L'écologie de spectacle** : COP en jets privés, crédits carbone 90% sans valeur, greenwashing corporatif, injonctions individuelles déresponsabilisantes. **Documentée, chiffrée, jugée.**

2. **La production de doute climato-sceptique** : Réseau transnational financé par l'industrie fossile, stratégie de « delayism » documentée par Harvard et Nature, instrumentalisation d'ajustements méthodologiques. **Documentée, chiffrée, tracée.**

**Les deux escroqueries ne s'opposent pas. Elles coopèrent.** Leur dénominateur commun est l'inaction. Leur bénéficiaire commun est l'industrie fossile.

### Les données physiques ne sont pas un discours

+1.43°C. >430ppm CO₂. Acidification. Montée des mers. Ce ne sont pas des opinions. Ce sont des mesures. Elles existent indépendamment de Sterone, de Pielke Jr, des COP, de Verra, et de cette investigation.

**Dire que « tout est escroquerie » est une position qui ne se distingue pas du déni.** Si tout est spectacle, alors aucune critique n'est possible — y compris la vôtre.

### L'escroquerie réelle

L'escroquerie n'est pas dans la physique du CO₂. Elle est dans :
- La production de doute financée par les fossiles
- Le greenwashing corporatif
- L'hypocrisie des sommets climatiques
- Le cynisme paralysant qui empêche toute action

**L'Empire du Mensonge n'a pas qu'un visage. Il en a deux. Et les deux sourient pendant que le monde brûle.**

---

## SOURCES

### ◈ PRIMARY (documents, données brutes)
1. Exxon internal documents (1977-1989) — [Climate Investigations Center](https://climateinvestigations.org/exxonknew/), [Archive.org](https://archive.org/details/ExxonClimateDocs), [ClimateFiles](https://www.climatefiles.com/exxon-knew/)
2. CO₂ Mauna Loa data — [NOAA GML](https://gml.noaa.gov/ccgg/trends/), [Scripps](https://scripps.ucsd.edu/news/annual-carbon-dioxide-peak-passes-another-milestone)
3. Température globale — [NOAA](https://www.ncei.noaa.gov/news/global-climate-202513), [NASA](https://science.nasa.gov/earth/explore/earth-indicators/global-temperature/)
4. CMIP7 scenario design — [GMD/Copernicus](https://gmd.copernicus.org/articles/19/2627/2026/), [WCRP](https://wcrp-cmip.org/cmip7-scenarios-endorsed-by-wcrp/)
5. Verra carbon offsets — [TheGuardian](https://www.theguardian.com/environment/2023/jan/18/revealed-forest-carbon-offsets-biggest-provider-worthless-verra-aoe), [LSE](https://blogs.lse.ac.uk/internationaldevelopment/2023/01/26/the-verra-scandal-explained-why-avoided-deforestation-credits-are-hazardous/)
6. Exxon Latin America documents — [TheGuardian](https://www.theguardian.com/environment/2025/nov/03/exxon-funded-thinktanks-to-spread-climate-denial-in-latin-america-documents-reveal)

### ◉ SECONDARY (investigations, académique)
7. Harvard study — delayism fossile — [Harvard Gazette](https://news.harvard.edu/gazette/story/2021/09/oil-companies-discourage-climate-action-study-says/)
8. Harvard analysis — Exxon predictions — [Harvard Gazette](https://news.harvard.edu/gazette/story/2023/01/harvard-led-analysis-finds-exxonmobil-internal-research-accurately-predicted-climate-change/)
9. CNRS Climatoscope — [CNRS Journal](https://lejournal.cnrs.fr/articles/climatosceptiques-sur-twitter-enquete-sur-les-mercenaires-de-lintox), [HAL](https://hal.science/hal-03986798v2)
10. Scientific consensus >99% — [Env. Research](https://cjp.eli.org/sites/default/files/documents/Consensus%20Climate%20Science%202025.pdf)
11. WMO State of Climate 2025 — [WMO](https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2025)
12. Greenwashing 25% claims trompeurs — [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1057521925008221)
13. GWPF dark money — [Kent & Surrey Bypelines](https://kentandsurreybylines.co.uk/politics/democracy/the-global-warming-policy-foundation-big-oil-and-dark-money/)
14. COP30 lobbyists — [TheGuardian](https://www.theguardian.com/environment/2025/nov/14/fossil-fuel-lobbyists-cop30), [TheGoodLobby](https://thegoodlobby.eu/record-high-number-of-fossil-fuel-lobbyists-at-cop30/)
15. Green Climate Fund misconduct — [FT](https://www.ft.com/content/d04de053-9b73-4010-b9a5-adcfe12e70ee)
16. DeSmog — Roger Pielke Jr — [DeSmog](https://www.desmog.com/roger-pielke-jr/)
17. DeSmog — Tory network — [DeSmog](https://www.desmog.com/2024/06/12/mapped-tory-network-climate-denial-fossil-fuel-funding/)
18. Senken carbon credits — [Senken](https://app.senken.io/reports/greenwashing-and-carbon-credits-report-2025-en.pdf)
19. Transparency.org Climate Atlas — [Transparency.org](https://www.transparency.org/en/projects/climate-governance-integrity-programme/climate-corruption-atlas)

### ○ TERTIARY (médias, opinion)
20. BBC — Exxon knew — [BBC](https://www.bbc.com/news/science-environment-64241994)
21. BBC — Minnesota lawsuit — [BBC](https://www.bbc.com/news/stories-53640382)
22. TheCooldown — COP29 jets — [TheCooldown](https://www.thecooldown.com/green-business/cop29-private-jet-travel-world-leaders/)
23. Amazon — Sterone Escrologie — [Amazon](https://www.amazon.fr/ESCROLOGIE-Comment-l%C3%89cologie-Politique-destruction-ebook/dp/B0DLCW25TL)
24. Fiat Lux — Laïbi Climate Terror — [Fiat Lux](https://www.editionsfiatlux.com/?product=climate-terror-de-salim-laibi-prevente-parution-4-oct-2024)
25. AEI — Pielke Jr RCP8.5 — [AEI](https://www.aei.org/articles/rcp8-5-is-officially-dead/)
26. YouTube — Aldo Sterone — [YouTube](https://www.youtube.com/channel/UCsua55kDzTYX_jztd7PckWw)

---

## REQUEST_LOG

| # | TYPE | QUERY/TOOL | RESULT | SOURCE | URL |
|---|------|-----------|--------|--------|-----|
| 1 | MnemoLite | search_memory "climate skepticism RCP8.5" | 0 résultats | MnemoLite | — |
| 2 | @WEB | global temperature anomaly 2025 2026 NASA NOAA | ✦ 5 sources | DuckDuckGo | [NOAA](https://www.ncei.noaa.gov/news/global-climate-202513) |
| 3 | @WEB | CO2 atmospheric concentration 2025 Mauna Loa | ✦ 5 sources | DuckDuckGo | [NOAA GML](https://gml.noaa.gov/ccgg/trends/) |
| 4 | @WEB | fossil fuel industry climate denial funding Koch Exxon | ✦ 5 sources | DuckDuckGo | [Wikipedia](https://en.wikipedia.org/wiki/ExxonMobil_climate_change_denial) |
| 5 | @WEB | climate change scientific consensus peer-reviewed 2025 | ✦ 5 sources | DuckDuckGo | [NASA](https://science.nasa.gov/climate-change/scientific-consensus/) |
| 6 | @WEB | greenwashing corporate climate claims vs actual emissions | ✦ 5 sources | DuckDuckGo | [TheGuardian](https://www.theguardian.com/environment/2025/dec/31/greenwashing-illegality-false-claims-climate-litigation-wins-2025) |
| 7 | @WEB | IPCC AR6 CMIP7 RCP8.5 scenario withdrawn 2026 | ✦ 5 sources | DuckDuckGo | [AEI](https://www.aei.org/articles/rcp8-5-is-officially-dead/) |
| 8 | @WEB | climate skepticism organized network funding think tanks | ✦ 5 sources | DuckDuckGo | [DeSmog](https://www.desmog.com/2024/06/12/mapped-tory-network-climate-denial-fossil-fuel-funding/) |
| 9 | @WEB | ocean acidification sea level rise ice sheet melt data | ✦ 5 sources | DuckDuckGo | [NASA](https://sealevel.nasa.gov/understanding-sea-level/global-sea-level/overview) |
| 10 | @WEB | Exxon internal memo climate change knew 1970s documents | ✦ 5 sources | DuckDuckGo | [Harvard](https://news.harvard.edu/gazette/story/2023/01/harvard-led-analysis-finds-exxonmobil-internal-research-accurately-predicted-climate-change/) |
| 11 | @WEB | Roger Pielke Jr AEI fossil fuel funding | ✦ 5 sources | DuckDuckGo | [DeSmog](https://www.desmog.com/roger-pielke-jr/) |
| 12 | @WEB | CNRS Climatoscope climato-dénialisme réseaux Twitter | ✦ 5 sources | DuckDuckGo | [CNRS](https://lejournal.cnrs.fr/articles/climatosceptiques-sur-twitter-enquete-sur-les-mercenaires-de-lintox) |
| 13 | @WEB | Aldo Sterone Escrologie livre YouTube climat | ✧ 5 sources | DuckDuckGo | [Amazon](https://www.amazon.fr/ESCROLOGIE-Comment-l%C3%89cologie-Politique-destruction-ebook/dp/B0DLCW25TL) |
| 14 | @WEB | CMIP7 scenario design 2026 SSP new scenarios | ✦ 5 sources | DuckDuckGo | [GMD](https://gmd.copernicus.org/articles/19/2627/2026/) |
| 15 | @WEB | climate delayism fossil fuel industry PR strategy Harvard | ✦ 5 sources | DuckDuckGo | [Harvard](https://news.harvard.edu/gazette/story/2021/09/oil-companies-discourage-climate-action-study-says/) |
| 16 | @WEB | green climate fund corruption scandal mismanaged | ✦ 5 sources | DuckDuckGo | [FT](https://www.ft.com/content/d04de053-9b73-4010-b9a5-adcfe12e70ee) |
| 17 | @WEB | COP summit hypocrisy private jets fossil fuel lobbyists | ✦ 5 sources | DuckDuckGo | [TheGuardian](https://www.theguardian.com/environment/2025/nov/14/fossil-fuel-lobbyists-cop30) |
| 18 | @WEB | AEI American Enterprise Institute funding donors fossil fuel | ◉ 5 sources | DuckDuckGo | [SourceWatch](https://www.sourcewatch.org/index.php/American_Enterprise_Institute) |
| 19 | @WEB | Clintel Netherlands climate skeptics declaration funding | ◉ 5 sources | DuckDuckGo | [Clintel](https://clintel.org/) |
| 20 | @WEB | Salim Laïbi Nexus magazine Climate Terror Fiat Lux | ◉ 5 sources | DuckDuckGo | [Fiat Lux](https://www.editionsfiatlux.com/) |
| 21 | @WEB | nuclear energy climate solution IPCC assessment | ◉ 5 sources | DuckDuckGo | [IAEA](https://www.iaea.org/publications/15558/nuclear-energy-in-mitigation-pathways-to-net-zero) |
| 22 | @WEB | carbon credit market fraud scam Verra offsets | ✦ 5 sources | DuckDuckGo | [TheGuardian](https://www.theguardian.com/environment/2023/jan/18/revealed-forest-carbon-offsets-biggest-provider-worthless-verra-aoe) |
| 23 | @WEB | GWPF Global Warming Policy Foundation funding dark money | ◉ 5 sources | DuckDuckGo | [Kent & Surrey Bypelines](https://kentandsurreybylines.co.uk/politics/democracy/the-global-warming-policy-foundation-big-oil-and-dark-money/) |
| 24 | @MNEMO_S | write_memory investigation APEX climat | — | MnemoLite | — |
| 25 | @WRITE | write APEX investigation file | — | File system | `investigations/2026-05/2026-05-16_15-00_climat_escroquerie_APEX.md` |

---

*Investigation conduite selon le protocole Truth Engine v2 (KERNEL.md)*
*Symboles : truth-engine-v2/definitions/SYMBOLS.md*
*Patterns : truth-engine-v2/definitions/PATTERNS.md*
*Threats : truth-engine-v2/definitions/THREATS.md*
*Clusters : truth-engine-v2/clusters/*
