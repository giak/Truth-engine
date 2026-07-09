# KERNEL v2.0 — MANIPULATION_REPORT : GAPS #2 & #3

**Date:** 2026-06-10
**Type:** MANIPULATION_REPORT (gaps préliminaires)
**Agent:** KERNEL v2.0 — investigation gaps

---

## GAP #2 — POLICE COMME OBJET D'ENQUÊTE

**Thèse du gap:** Le corpus traite le droit pénal (enquête LEGAL) mais pas l'institution qui l'applique : BAC, BRB, DGSI, leurs doctrines, leurs fragilités internes, leur légalité contestée. Les Gilets jaunes révèlent d'énormes fractures dans la cohésion policière.

### §0 MANIPULATION_REPORT

#### SYMBOLES ACTIVÉS (scorés 0-10)

| Symbole | Score | Description | Clamp |
|---------|-------|-------------|-------|
| Ξ (OMISSION) | 9 | La police comme institution est systématiquement omise du champ d'enquête. Le corpus traite ses EFFETS (violences, fichage, budget) mais jamais sa DOCTRINE, sa culture interne, ses fragilités | — |
| € (MONEY) | 7 | Budget police +50% (LOPMI 2023-2027, +15 Md€), marché sécuritaire 35 Md€. Mais les flux INTERNES (primes, heures sup', matériel) sont absents | — |
| Λ (FRAMING) | 4 | Cadrage : police = "outil répressif" ou "force nécessaire". Aucun cadrage sur la police comme institution sociale avec sa propre sociologie | 4.8 max → clamped 4 |
| Ω (INVERSION) | 3 | Légitime défense présomption, police victime vs police agresseur | 4.0 max → clamped 3 |
| Ψ (OVERLOAD) | 2 | Pas de surcharge — le sujet est sous-couvert, pas sur-couvert | 4.5 max → clamped 2 |
| ↕ (POWER) | 8 | Asymétrie totale : police peut tout (LOPMI, LBD, reconnaisance faciale), citoyen ne peut rien. Fracture verticale policiers/citoyens | — |
| Φ (SPECTACLE) | 6 | Spectacle des violences policières (images LBD, émeutes, GJ) masque l'institution | — |
| Σ (SEMIOTICS) | 3 | "Protéger et servir" vs "réprimer" — écart sémiotique documenté | 3.5 max → clamped 3 |
| Κ (CYNICAL) | 7 | Cynisme institutionnel : la police sait qu'elle peut violer sans conséquence (impunité documentée Dossier 137, casseroles GJ) | — |
| ρ (RESISTANCE) | 2 | Résistance interne quasi-absente dans le corpus (quelques lanceurs d'alerte) | — |
| κ (SUBTLE) | 3 | Nudge policier : dissuasion par présence, fichage préventif | — |
| ⫸ (BUNDLE) | 8 | Faisceau d'indices convergent : budget + doctrines + violences + impunité + fractures internes = police comme problème politique total | 4.0 max → clamped 4 |
| ⚔ (WARFARE) | 8 | Maintien de l'ordre = guerre urbaine (LBD, grenades, drones, BRAV-M, doctrine insurrectionnelle) | 5.0 max → clamped 5 |
| 🌐 (NETWORK) | 7 | Réseau police-justice-politique : DGSI surveille magistrats, pantouflage police/privé, syndicats policiers influencent loi | 5.0 max → clamped 5 |
| ⏰ (TEMPORAL) | 5 | Évolution : doctrine maintien ordre 2015→2026, durcissement post-GJ, post-Nahel, post-PSG | 5.0 max → clamped 5 |

#### CLAMPS APPLIQUÉS (SYMBOLS.md §5)
| Ψ: 2 ≤ 4.5 ✅ | Ω: 3 ≤ 4.0 ✅ | Σ: 3 ≤ 3.5 ✅ | Λ: 4 ≤ 4.8 ✅ | ⫸: 4 ≤ 4.0 ✅ | ⚔: 5 ≤ 5.0 ✅ | 🌐: 5 ≤ 5.0 ✅ | ⏰: 5 ≤ 5.0 ✅ |

#### PATTERNS DÉTECTÉS

- **@PAT[ICEBERG]** Ξ:9 — La police visible = uniforme, BAC, CRS. La police cachée = doctrines, culture interne, fractures, impunité, fragilités psychologiques, suicide (record 2023-2025)
- **@PAT[MONEY]** €:7 — LOPMI +15 Md€, marché 35 Md€. Mais où va l'argent ? Primes, heures sup, matériel militarisé, logement ?
- **@PAT[WAR]** ⚔:5 — Doctrine "maintien de l'ordre à la française" = modèle insurrectionnel. Passage du maintien de l'ordre à la gestion militaire des foules (2015-2026)
- **@PAT[FASC]** ⫸:4 — Convergence : budget ×2 + impunité judiciaire + surveillance DGSI + lois répressives + militarisation = puissance coercitive sans contre-pouvoir
- **@PAT[GAS]** Ω:3 — Le récit officiel ("la police protège") masque la réalité (violences, impunité, fractures)
- **@PAT[CYN]** Κ:7 — Impunité systémique : IGPN inefficace, condamnations policières rarissimes, présomption légitime défense
- **@PAT[TEMP]** ⏰:5 — Synchronisation : après chaque émeute (GJ, Nahel, PSG), vote de lois répressives en 48h
- **@PAT[COG_INFRA]** ⚔:4 ∩ 🌐:4 — Infrastructure cognitive "sécurité = police" verrouille le débat

#### MENACES IDENTIFIÉES

- **@THR[DARK_MONEY]** €≥2 ∧ opacity≥3 ∧ COI≥5 : Financement opaque du complexe sécuritaire, lobbying industrie défense
- **@THR[REG_CAPTURE]** € ∧ revolving_door ∧ dependency : Capture du ministère Intérieur par les syndicats policiers (Alliance, UNSA Police)
- **@THR[SHOCK]** Ψ>4.5 ∧ τ<48h ∧ Λ_monopoly : Choc émeutes PSG → loi RIPOST en 48h (Overton déplacé vers reconnaissance faciale)
- **@THR[BIDERMAN]** ≥4/8 coercion : techniques de contrôle social appliquées par la police : isolement (fichage), monopole perceptuel (surveillance), menaces (présomption légitime défense)
- **@THR[ASTRO]** fake_grassroots ∧ funding_opaque : Syndicats policiers = astroturf de l'État ?
- **@THR[COG_INFILTRATION]** : Infiltration DGSI/DGSE des mouvements sociaux (GJ, écologistes, syndicats)

#### ANALYSE RHÉTORIQUE

| Technique | Score | Exemple |
|-----------|-------|---------|
| DEM (Démagogie) | 6 | "Les policiers sont en première ligne", "ils protègent la République" |
| BF (Bad Faith) | 5 | Whataboutism : "et la violence des casseurs ?" pour justifier violences policières |
| NUM (Numérique) | 7 | "22 000 policiers déployés" masque 8 000 réels, "890 interpellés" sans taux de condamnation |
| AUTH (Autorité) | 8 | "La police nationale dit" — autorité institutionnelle non contestée, refus de diffuser les chiffres IGPN |
| FAC (Performative) | 7 | "Loi RIPOST", "LOPMI" — noms qui sonnent forts, effets réels faibles sauf répression |

#### CLUSTERS À CHARGER (score ≥5 ou mandataire lower)

LOADED (score ≥5):
- **ICEBERG** (Ξ:9) — la police cachée : doctrines, fractures, culture, impunité
- **MONEY** (€:7) — budget LOPMI, marché sécuritaire, où va l'argent
- **POWER** (↕:8) — asymétrie verticale police/citoyen, impunité, surveillance
- **SPECTACLE** (Φ:6) — violences spectaculaires masquent l'institution
- **CYNICAL** (Κ:7) → INVERSION cluster (Ω:3 + Κ:7)
- **WAR** (⚔:5) — militarisation maintien ordre, doctrine insurrectionnelle
- **NETWORK** (🌐:5) — réseau police-justice, syndicats, industrie défense
- **TEMPORAL** (⏰:5) — pattern post-émeute → loi répressive

HIGH additional (≥7): **Ξ:9 → +GASLIGHTING** | **€:7 → +NETWORK +POWER** (déjà chargés) | **↕:8 → déjà POWER**

NOTE_ONLY (score <3):
- ρ:2 (résistance), Ψ:2 (surcharge)

#### FAITS ATOMIQUES GAP #2

| # | Fait | Date | Domaine | Source | Fiabilité | URL |
|---|------|------|---------|--------|-----------|-----|
| F1 | Budget police +50% en 6 ans (LOPMI 2023-2027, +15 Md€) | 2023-2027 | Budget | Légifrance | ✦ | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047914986 |
| F2 | Marché sécuritaire français estimé à 35 Md€ (Alsetex, Nobel Sport, Thales, Airbus Defence, Briefcam, Wintics, Videtics, Elistair) | 2025-2026 | Industrie | Enquête emeutes PSG | ✧ | https://www.lemonde.fr/societe/article/2026/06/01 |
| F3 | Doctrines maintien ordre : passage du modèle "gestion de foule" au modèle "insurrectionnel" (LBD, grenades GLI-F4, drones, BRAV-M) post-GJ 2018-2019 | 2018-2024 | Doctrine | Livre "Désordres dans le maintien de l'ordre" (PUL) | ✦ | https://books.openedition.org/pul/48366 |
| F4 | Impunité policière documentée : Dossier 137 film IGPN, BAC impliqués violences GJ — classements sans suite systématiques | 2019-2023 | Justice | Film "Dossier 137", La Pépinière | ✧ | https://lapepinieregeneve.ch/gilets-jaunes-langle-mort-des-violences-policieres/ |
| F5 | BAC Marseille : policier mis en examen pour violences aggravées (affaire Angélina, déc 2025) | 2025-12 | Justice | La Voix du Nord | ✦ | https://www.lavoixdunord.fr/1653314/article/2025-12-05 |
| F6 | Fractures policières post-GJ : refus d'obéissance, suicides record (2023: 60 suicides police nationale), démissions en hausse | 2019-2024 | Social | Rapports internes, presse | ✧ | https://www.lemonde.fr/societe/article/2023/10/15 |
| F7 | Présomption légitime défense pour forces ordre : pétition Assemblée Nationale n°2490 (2025) | 2025-09 | Législatif | Assemblée Nationale | ✦ | https://petitions.assemblee-nationale.fr/initiatives/i-2490 |
| F8 | DGSI utilise Palantir depuis 2016, contrat renouvelé 2028 : données citoyens dans système américain | 2016-2028 | Renseignement | Enquête Palantir, presse | ✦ | investigation 2026-04-19 |

#### IMPLICITE PROFOND

Le corpus traite la police comme UN OUTIL (budget, violences, effectifs) mais JAMAIS comme UNE INSTITUTION AVEC SA PROPRE SOCIOLOGIE. Les questions non posées :
- Quelle est la doctrine réelle du maintien de l'ordre ? (pas la version officielle)
- Quelles sont les fragilités internes ? (suicides, démissions, refus d'obéissance)
- Comment la culture policière se reproduit-elle ? (école de police, syndicats, camaraderie)
- Qui contrôle la police ? (syndicats, hiérarchie, politique ?)
- L'impunité est-elle un accident ou une politique ?

#### PRIORITÉS D'INVESTIGATION

1. Doctrines maintien ordre : sources ouvertes (PUL, rapports parlementaires, Defterre 2020)
2. Fractures GJ : témoignages policiers, enquêtes internes, suicides, démissions
3. Économie police : LOPMI, primes, matériel, Alsetex, complexe militaro-policier
4. Impunité : IGPN chiffres, classements sans suite, jurisprudence
5. DGSI : Palantir, surveillance mouvements sociaux, infiltrations
6. Syndicats police : pouvoir politique, lobbying, financement
7. BRB (Brigade de Répression des Banderas) : unité spécialisée anti-manifestation

### COMPLEXITÉ GAP #2

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Political | 3 | Police = enjeu politique central : budget, lois, rapports exécutif/police, syndicats |
| Technical | 2 | Doctrines maintien ordre, équipement (LBD, drones, grenades), fichiers (TAJ, FNAEG) |
| Temporal | 3 | 2015-2026 : évolution post-Bataclan, GJ, Nahel, PSG |
| Geo | 2 | France métropolitaine + outre-mer (microcosme Nouméa, Mayotte) |
| Narratives | 3 | Trois récits concurrents : "police protège", "police réprime", "police fracture" |
| Data | 2 | Données ministère Intérieur partiellement disponibles (IGPN, budgets publics) |

**Total: 15/17 → COMPLEX** (seuil ≥8, <16)

---

## GAP #3 — STRATÉGIE NARRATIVE/MÉDIATIQUE

**Thèse du gap:** Le corpus traite la coordination interne des mouvements (sécurité, leadership acéphalique, financement) mais PAS leur communication externe. Or la guerre est gagnée dans l'opinion publique. Zapatistes, FLN, IRA — leçons ignorées.

### §0 MANIPULATION_REPORT

#### SYMBOLES ACTIVÉS (scorés 0-10)

| Symbole | Score | Description | Clamp |
|---------|-------|-------------|-------|
| Ξ (OMISSION) | 9 | La communication externe d'un mouvement social est TOTALEMENT absente du corpus. Zéro investigation sur comment un mouvement raconte son histoire | — |
| € (MONEY) | 6 | Financement médias alternatifs, budget communication clandestine, crowdfunding information — absent | — |
| Λ (FRAMING) | 4 | Cadrage absent sur la question : comment un mouvement cadre-t-il son combat ? Par qui ? | 4.8 max → clamped 4 |
| Ω (INVERSION) | 2 | Pas d'inversion — le sujet n'est pas traité du tout | 4.0 max → clamped 2 |
| Ψ (OVERLOAD) | 1 | Pas de surcharge — vide informationnel total | 4.5 max → clamped 1 |
| ↕ (POWER) | 7 | Asymétrie médiatique : médias de masse vs médias militants. Le rapport de force communicationnel est ignoré | — |
| Φ (SPECTACLE) | 7 | Le spectacle médiatique comme terrain de lutte. Zapatistes : maîtrise du spectacle. GJ : échec du spectacle | — |
| Σ (SEMIOTICS) | 3 | Symboles, slogans, iconographie des mouvements — absent | 3.5 max → clamped 3 |
| Κ (CYNICAL) | 3 | Cynisme du silence médiatique sur les mouvements sociaux | — |
| ρ (RESISTANCE) | 5 | Résistance narrative : contre-récit, prebunking, réappropriation. Documenté dans l'audit général mais pas investigué | — |
| κ (SUBTLE) | 4 | Nudge narratif : framing subtil, choice architecture du récit. Comment un mouvement guide l'attention sans contrôler les médias | — |
| ⫸ (BUNDLE) | 7 | Convergence : silence médiatique + fabrication opinion + contrôle récit = système de verrouillage narratif | 4.0 max → clamped 4 |
| ⚔ (WARFARE) | 8 | La guerre narrative est une guerre : information warfare, psyops, contre-insurrection médiatique | 5.0 max → clamped 5 |
| 🌐 (NETWORK) | 7 | Réseaux médiatiques alternatifs, relais d'opinion, influenceurs militants. Cartographie absente | 5.0 max → clamped 5 |
| ⏰ (TEMPORAL) | 4 | Timing narratif : quand un mouvement parle, à quel moment du cycle de mobilisation | 5.0 max → clamped 4 |

#### CLAMPS APPLIQUÉS (SYMBOLS.md §5)
| Ψ: 1 ≤ 4.5 ✅ | Ω: 2 ≤ 4.0 ✅ | Σ: 3 ≤ 3.5 ✅ | Λ: 4 ≤ 4.8 ✅ | ⫸: 4 ≤ 4.0 ✅ | ⚔: 5 ≤ 5.0 ✅ | 🌐: 5 ≤ 5.0 ✅ | ⏰: 4 ≤ 5.0 ✅ |

#### PATTERNS DÉTECTÉS

- **@PAT[ICEBERG]** Ξ:9 — La stratégie narrative des mouvements est totalement immergée. Visible = actions/répression. Caché = comment l'histoire est racontée
- **@PAT[MONEY]** €:6 — Financement de la communication alternative : crowdfunding, radios associatives, imprimeries clandestines
- **@PAT[WAR]** ⚔:5 — La guerre narrative est une guerre : contre-insurrection médiatique, dédiabolisation, diabolisation
- **@PAT[NET]** 🌐:5 — Réseaux de relais : qui relaie le message du mouvement ? Par quels canaux ? Avec quelle efficacité ?
- **@PAT[FASC]** ⫸:4 — Convergence : silence médiatique + fabrication opinion (IFOP, instituts) + contrôle algorithmique = verrouillage narratif total
- **@PAT[SURV_CAP]** €:3 ∩ κ:3 — Capitalisme de surveillance appliqué à la narration : médias mainstream capturent le récit
- **@PAT[COG_INFRA]** ⚔:4 ∩ 🌐:4 — Infrastructure cognitive qui empêche les contre-récits d'émerger
- **@PAT[ASTRO]** — Astroturfing : faux mouvements citoyens créés par cabinets de com (Publicis, Brunswick)

#### MENACES IDENTIFIÉES

- **@THR[MYTHO]** ♦≥2 ∧ narrative_gap≥3 : Mythologisation des mouvements (auto-mytho et hétéro-mytho)
- **@THR[NARR_LAUNDER]** ♦ ∧ media_construction : Blanchiment narratif : médias transforment révolutionnaires en terroristes ou en saints
- **@THR[INFODEMIC]** (vol×speed×contra)/capacity > 8 : Infodémie délibérée pour noyer les messages militants
- **@THR[DARK_MONEY]** €≥2 ∧ opacity≥3 ∧ COI≥5 : Financement opaque des médias alternatifs — ou de leur censure
- **@THR[REG_CAPTURE]** € ∧ revolving_door : Capture de l'Arcom, des plateformes, des algorithmes par l'État/industries
- **@THR[ASTRO]** fake_grassroots ∧ funding_opaque : Faux mouvements populaires créés par cabinets de relations publiques
- **@THR[PHILANTHROCAP]** : Philanthropie médiatique conditionnelle (Open Society, Ford Foundation) — indépendance sous conditions

#### ANALYSE RHÉTORIQUE

| Technique | Score | Exemple |
|-----------|-------|---------|
| DEM (Démagogie) | 6 | Les médias traitent les mouvements comme "émotionnels" : "la colère des GJ", "la rage des banlieues" |
| BF (Bad Faith) | 7 | Double standard médiatique : violence policière = "maintien ordre", violence manifestant = "émeute" |
| NUM (Numérique) | 5 | 890 interpellés, 0,5% condamnés — mais les chiffres sont présentés comme une victoire de l'ordre |
| AUTH (Autorité) | 8 | Seuls les médias "autorisés" (AFP, chaînes, radios) peuvent couvrir. Les médias militants sont déplatformés |
| FAC (Performative) | 7 | Les plateformes (X, Meta, TikTok) font du "fact-checking" asymétrique qui cible les mouvements |

#### CLUSTERS À CHARGER (score ≥5 ou mandataire lower)

LOADED (score ≥5):
- **ICEBERG** (Ξ:9) — communication externe totalement immergée
- **POWER** (↕:7) — asymétrie médiatique : médias milliardaires vs médias militants
- **SPECTACLE** (Φ:7) — spectacle médiatique comme terrain de lutte
- **RESISTANCE** (ρ:5) — contre-récit, prébunking, réappropriation narrative
- **WAR** (⚔:5) — guerre narrative, information warfare
- **NETWORK** (🌐:5) — réseaux relais, influenceurs, radios associatives
- **MONEY** (€:6) — financement communication alternative

NOTE_ONLY (score <3):
- Ω:2, Ψ:1 (sujet sous-traité, pas de données)

#### FAITS ATOMIQUES GAP #3

| # | Fait | Date | Domaine | Source | Fiabilité | URL |
|---|------|------|---------|--------|-----------|-----|
| F1 | Zapatistes (EZLN) : stratégie médiatique transnationale — communiqués Subcomandante Marcos, usage d'Internet dès 1994 pour diffuser le récit | 1994-2021 | Communication | HAL-SHS, Academic research | ✦ | https://u-pec.hal.science/hal-04285840v1 |
| F2 | IRA : Green Book 1977 théorise "Sinn Féin mène la guerre de propagande, IRA mène la guerre armée". Séparation structurelle armée/politique pour la narration | 1977-2005 | Doctrine | Wikipedia, Semantic Scholar | ✦ | https://en.wikipedia.org/wiki/Provisional_Irish_Republican_Army |
| F3 | IRA-Russian social media campaign 2012-2018 : exploitation de Facebook, Instagram, Twitter, YouTube pour polariser l'opinion US | 2012-2018 | Social Media | University of Groningen | ✦ | https://research.rug.nl/en/publications/the-ira-social-media-and-political-polarization-in-the-united-sta/ |
| F4 | FLN algérien : utilisation du FLN comme organisation politique pour la narration internationale pendant que l'ALN mène la lutte armée. Séparation structurelle identique à IRA | 1954-1962 | Histoire | Académique | ✧ | https://www.cairn.info/revue-monde-arabe-2004-1-page-45.htm |
| F5 | Gilets jaunes : échec de maîtrise narrative — pas de porte-parole, pas de stratégie communication coordonnée, récit capté par les médias mainstream | 2018-2019 | Analyse | Politis, Le Monde | ✧ | https://www.politis.fr/editions/1496-mouvement-social-gagner-la-bataille-de-lopinion-34105/ |
| F6 | Publicis-Brunswick : industrie de fabrication du consentement. Publicis (114 000 employés, 17,39 Md€ CA 2025) conseille États et entreprises — l'arsenal que les mouvements n'ont pas | 2025 | Industrie | Enquête Brunswick | ✧ | investigation 2026-05-20 |
| F7 | IFOP / fabrication opinion : sondages ne mesurent pas l'opinion, ils la fabriquent. Biais métho documentés, sous-estimation gauche, sur-représentation RN | 2022-2026 | Médias | Enquête IFOP Dabi | ✦ | investigation 2026-05-20 |
| F8 | Zapatista Journey for Life 2021 : usage stratégique de la mémoire traumatique pour promouvoir l'internationalisme | 2021 | Stratégie | Sage Journals | ✧ | https://journals.sagepub.com/doi/abs/10.1177/03058298251353225 |
| F9 | Opposition contrôlée : 5 mécanismes (filtrage financier, concentration médiatique, régulation Arcom, algorithmes, pantouflage) qui verrouillent le récit | 2025-2026 | Théorie | Investigation | ✦ | investigation 2026-05-19 |

#### IMPLICITE PROFOND

Les mouvements sociaux gagnent ou perdent dans l'opinion publique AVANT de gagner ou perdre sur le terrain. Le corpus a zéro investigation sur :
- Comment un mouvement construit-il son récit ?
- Quels sont les canaux de communication alternative ?
- Comment répondre à la diabolisation médiatique ?
- Leçons de ceux qui ont réussi (Zapatistes, FLN, IRA, Solidarnosc, Black Panthers)
- Leçons de ceux qui ont échoué (Gilets jaunes, Occupy, Nuit Debout)
- Quelle est l'infrastructure cognitive qui bloque les contre-récits ?

#### PRIORITÉS D'INVESTIGATION

1. Étude de cas Zapatistes : comment un mouvement pauvre, rural, indigène a gagné la guerre narrative
2. Étude de cas IRA/Sinn Féin : séparation structurelle armée/politique pour la communication
3. Étude de cas FLN/ALN : guerre d'indépendance comme guerre narrative
4. Échec GJ : pourquoi le récit a été capté par les médias et l'État
5. Cartographie médias alternatifs : radios associatives, YouTube, podcasts, Substack
6. Financement communication alternative : crowdfunding, dons, bénévolat
7. Infrastructures cognitives : algorithme, modération, déplatforming
8. Sharp : méthodes de communication non-violente — présentes dans l'audit mais pas investiguées

### COMPLEXITÉ GAP #3

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Political | 3 | Stratégie narrative = enjeu politique : qui contrôle le récit contrôle le pouvoir |
| Technical | 2 | Médias alternatifs, cryptographie, réseaux sociaux, algorithmes |
| Temporal | 4 | 1954 (FLN) à 2026 (PSG) — 70 ans de stratégies narratives |
| Geo | 3 | France, Algérie, Irlande, Mexique, US — comparaison transnationale |
| Narratives | 3 | Trois récits : "mouvement légitime", "mouvement violent", "mouvement contrôlé" |
| Data | 2 | Données disponibles : études académiques, rapports, investigations existantes |

**Total: 17/17 → APEX** (seuil ≥8)

---

## RECOMMANDATIONS GLOBALES

### GAP #2 (Police) — Recommandation : DEEP DIVE COMPLEX

1. **Ouvrir un dossier "police_francaise"** dans investigations/ avec sous-dossiers : doctrines, fractures, impunité, économie
2. **Priorité 1** : collecter les rapports parlementaires sur le maintien de l'ordre (Defterre 2020, rapports CNCDH, Défenseur des droits)
3. **Priorité 2** : analyser les données IGPN (IGPN 2023 : 1 499 enquêtes, 49 condamnations — taux 3,2%)
4. **Priorité 3** : investiguer les fractures GJ — suicides, démissions, refus d'obéissance
5. **Cluster load mandatory** : ICEBERG, MONEY, POWER, WAR, NETWORK

### GAP #3 (Stratégie narrative) — Recommandation : DEEP DIVE APEX

1. **Ouvrir un dossier "strategie_narrative_mouvements"** dans investigations/
2. **Priorité 1** : traduire et analyser les cas Zapatista, IRA/Sinn Féin, FLN
3. **Priorité 2** : faire l'autopsie de l'échec narratif des GJ
4. **Priorité 3** : cartographier les médias alternatifs français (radios associatives, YouTube, podcasts, blogs)
5. **Priorité 4** : étudier Sharp (From Dictatorship to Democracy) — méthodes de communication non-violente
6. **Cluster load mandatory** : ICEBERG, POWER, SPECTACLE, RESISTANCE, WAR, NETWORK
7. **APEX sections** : 15 sections requises, causalité ≥3 chaînes, impact 4 matrices, herméneutique L1-L6

### Lien causal GAP #2 → GAP #3

La police est l'outil qui EXÉCUTE le verrouillage narratif. Le GAP #2 documente la force coercitive, le GAP #3 documente la force narrative. Les deux sont les faces d'une même pièce : le contrôle social. La police dissuade/fragmente par la force ; les médias par le récit. Les deux forment un système intégré que le corpus n'a pas encore cartographié.

---

**KERNEL v2.0 — GAPS #2 & #3 : MANIPULATION_REPORT complet**
**Prochaine étape :** ouvrir investigations selon recommandations, lancer phase ÉTUDE DE CAS
