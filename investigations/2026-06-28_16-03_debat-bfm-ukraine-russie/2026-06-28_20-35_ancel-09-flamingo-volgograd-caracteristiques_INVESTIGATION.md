# INVESTIGATION — Ancel 09 : « Missile Flamingo — frappe Volgograd et caractéristiques techniques »

> **Source :** Débat BFM TV, segment Ukraine/Russie, 2026-06-28
> **Intervenant :** Guillaume Ancel, lieutenant-colonel (séquences 1875-1966)
> **Affirmation :** « Il s'appelle le missile Flamingo. [...] Cette nuit, effectivement, l'Ukraine a lancé des missiles Flamingo sur [...] une usine à Volgograd, une installation qui fabrique des systèmes d'artillerie. [II] peut aller très, très, très loin. Jusqu'à 3 000 km. [...] C'est pas un missile performant d'un point de vue technologique. C'est pas un missile avec des capacités furtives ou une vitesse incroyable. [...] le Flamingo [...] emporte une charge de l'ordre d'une tonne. »
> **Pipeline :** TRUTH ENGINE v2.0 — KERNEL.md §0→19
> **Complexité :** MEDIUM (7 sections)
> **GATE_CHECK :** PASS

---

## §0 — TEXT ANALYSIS

### BIAS TEST

| Rang | Source | Justification |
|------|--------|---------------|
| 1 (E) | Academic peer-reviewed study | Analyse technique du missile Flamingo (Atlantic Council, IISS) |
| 2 (D) | AFP Factuel | Vérification frappe Volgograd, annonce officielle ukrainienne |
| 3 (C) | Citizen eyewitness video | Vidéos des frappes sur Volgograd (OSINT) |
| 4 (A) | Viginum | Agence étatique — confirmation indirecte possible |
| 5 (B) | RT | Source antagoniste — minimisera la frappe |

**Résultat :** E > D > C > A > B — **PASS**

### MANIPULATION_REPORT

```
├── SYMBOLS:
│   Ξ:3 (OMISSION — Ancel omet de mentionner que le missile Flamingo
│       utilise des composants soviétiques recyclés (moteur AI-25TL),
│       que sa production est limitée, que le coût unitaire est estimé
│       entre 500k et 1M$ — pas une arme de saturation massive)
│   €:1
│   Λ:3 (FRAMING — Présentation du missile comme « construit par les
│       Ukrainiens » — narrative d'autosuffisance technologique, sans
│       mention des composants occidentaux potentiels)
│   Ω:0
│   Ψ:1
│   ↕:0
│   Φ:2 (SPECTACLE — Missile capable de « frapper Moscou » crée un
│       effet dramatique, image d'un missile ukrainien menaçant le
│       Kremlin)
│   Σ:1
│   Κ:2 (mutual_knowledge — Le public connaît le besoin de missiles
│       longue portée de l'Ukraine depuis les restrictions US sur
│       les ATACMS)
│   ρ:2 (COGNITIF — Récit de David contre Goliath : l'Ukraine
│       construit ses propres missiles longue portée malgré la Russie)
│   κ:1
│   ⫸:2
│   ⚔:3 (COGNITIVE_WARFARE — Le missile Flamingo est un outil de
│       guerre cognitive : il montre que l'Ukraine peut frapper
│       n'importe où en Russie, créant une insécurité stratégique)
│   🌐:2 (NETWORK — Fire Point comme industrie de défense ukrainienne
│       émergente, partenariats occidentaux potentiels)
│   ⏰:2 (TEMPORAL — Frappe sur Volgograd la veille du débat :
│       actualité brûlante, information de première main)
│
├── PATTERNS: [—]
├── THREATS: [—]
├── RHETORICAL: {DEM:1 BF:2 NUM:2 AUTH:3 FAC:2}
│   → AUTH=3: Ancel parle « en connaissance » des systèmes d'armes
│   → NUM=2: chiffres précis (3 000 km, 1 tonne chargé)
│   → FAC=2: description technique détaillée
│
├── CLUSTERS: [— NOTE_ONLY]
│
├── IMPLICIT:
│   - Le missile Flamingo est une arme nouvelle et secrète
│   - L'Ukraine a développé une capacité de frappe stratégique
│     autonome
│   - La Russie ne peut plus protéger ses usines d'armement
│   - Le missile est simple mais efficace
│   - La portée de 3 000 km rend tout le territoire russe vulnérable
│
├── SPEAKER: {tone: technique-enthousiaste, target: téléspectateur
│   BFM, goal: présenter le missile Flamingo comme une révolution
│   dans la capacité de frappe ukrainienne, démontrant l'ingéniosité
│   et l'autonomie technologique de l'Ukraine}
│
├── PRIORITIES: [vérifier le missile Flamingo (existence, fabricant,
│   caractéristiques), confirmer la frappe sur Volgograd (date, cible,
│   résultats), comparer les chiffres d'Ancel avec les données
│   techniques, évaluer la portée réelle]
│
└── QUERY_GUIDANCE: [rechercher le FP-5 Flamingo, Fire Point,
    les frappes sur Titan-Barrikady Volgograd, les caractéristiques
    techniques (portée, charge, vitesse, guidage)]
```

---

## §1 — PROTOCOL

### Step 1 — TEMPORAL

- **Date :** 28 juin 2026 (débat)
- **Frappe :** Nuit du 27 au 28 juin 2026 sur Volgograd — information de l'avant-veille

### Step 3 — COMPLEXITY

| Dimension | Score | Justification |
|-----------|-------|---------------|
| political | 1 | Peu d'enjeu politique direct |
| technical | 3 | Caractéristiques techniques du missile |
| temporal | 2 | Frappe récente (J-1) |
| geo | 2 | Volgograd, portée 3 000 km |
| narratives | 2 | Récit d'autosuffisance ukrainienne |
| data | 2 | Chiffres vérifiables |

**Total : 12 → MEDIUM**

### Step 6 — CRÉDO (12 questions)

```
C — 1. Q:Le missile Flamingo (FP-5) existe-t-il et quelles sont ses
      caractéristiques officielles ?
C — 2. Q:La frappe sur Volgograd (usine Titan-Barrikady) a-t-elle eu
      lieu dans la nuit du 27-28 juin 2026 ?
C — 3. Q:La portée de 3 000 km est-elle confirmée par des sources
      techniques ?
C — 4. Q:La charge d'une tonne est-elle exacte ?
C — 5. Q:Qui fabrique le Flamingo ? (Fire Point)
C — 6. Q:Le missile utilise-t-il des composants occidentaux ou
      exclusivement ukrainiens ?
C — 7. Q:Quel est le coût unitaire du Flamingo ?
C — 8. Q:Le Flamingo a-t-il été utilisé sur d'autres cibles avant
      Volgograd ?
C — 9. Q:Comment Ancel connaît-il ces détails techniques précis ?
      (accès à des sources classifiées ?)
C — 10. Q:La vitesse (850-950 km/h) est-elle exacte ?
C — 11. Q:Le missile est-il réellement « pas performant technologiquement »
       ou est-ce une appréciation relative ?
C — 12. Q:La production est-elle suffisante pour avoir un impact
       stratégique ?
```

### Step 10 — FACT_REGISTRY

#### Partie A — L'affirmation

| # | Fait | Acteur | Fiabilité |
|---|------|--------|-----------|
| 1 | Missile Flamingo existe et est ukrainien | Ancel | ⁕ (CLAIMED) |
| 2 | Frappe sur Volgograd (usine Titan-Barrikady) nuit du 27-28 juin | Ancel | ⁕ (CLAIMED) |
| 3 | Portée 3 000 km | Ancel | ⁕ (CLAIMED) |
| 4 | Charge 1 tonne | Ancel | ⁕ (CLAIMED) |
| 5 | Pas furtif, pas performant technologiquement | Ancel | ⁕ (CLAIMED) |

#### Partie B — Contexte : données vérifiées

| # | Fait | Date | Source | URL | Fiabilité |
|---|------|------|--------|-----|-----------|
| 6 | Missile FP-5 Flamingo développé par Fire Point (entreprise privée ukrainienne) depuis 2024, révélé août 2025 | Août 2025 | Atlantic Council | https://www.atlanticcouncil.org/blogs/ukrainealert/missiles-made-in-ukraine-are-bringing-putins-invasion-home-to-russia/ | ✦ CONFIRMÉ |
| 7 | Portée annoncée : jusqu'à 3 000 km | 2025-2026 | Wikipedia | https://en.wikipedia.org/wiki/FP-5_Flamingo | ✧ ATTESTÉ |
| 8 | Charge utile : ~1 150 kg (plus d'une tonne) | 2025-2026 | Wikipedia | https://en.wikipedia.org/wiki/FP-5_Flamingo | ✧ ATTESTÉ |
| 9 | Vitesse : max 950 km/h, croisière 850-900 km/h — subsonique, pas furtif | 2025-2026 | TheDefenseWatch | https://thedefensewatch.com/global-news/ukraine-fp-5-flamingo-cruise-missile-boosts-nato-deep-strike-capability/ | ✧ ATTESTÉ |
| 10 | Moteur : turboréacteur AI-25TL recyclé (ère soviétique) | 2025-2026 | Wikipedia | — | ✧ ATTESTÉ |
| 11 | Frappe sur Titan-Barrikady (Volgograd) confirmée par Zelensky, OSINT vidéos | 27-28 juin 2026 | Kyiv Independent, Zelensky | — | ✦ CONFIRMÉ |
| 12 | Usine Titan-Barrikady fabrique systèmes artillerie lourde, Yars, Topol-M, Iskander-M | — | OSINT | — | ✦ CONFIRMÉ |
| 13 | Frappes Flamingo antérieures documentées : Cheboksary, Votkinsk, Chapayevsk | 2025-2026 | United24, Ukraine MOD | — | ✧ ATTESTÉ |
| 14 | Coût unitaire estimé : $500k à $1M | 2025-2026 | TheDefenseWatch | — | ✧ ATTESTÉ |
| 15 | Production limitée mais en hausse — pas de chiffre exact public | 2026 | Multiple | — | ⁕ (INCONNU) |

### Step 12 — IMPACT

| Matrice | Verdict |
|---------|---------|
| Qui gagne | Ukraine (capacité de frappe longue portée autonome) |
| Qui perd | Russie (vulnérabilité stratégique) |
| Qui meurt | Non mentionné |
| Qui recule | Défenses aériennes russes |

### Step 18-18b — GATE_CHECK

- TEXT_ANALYSIS ✓ | MANIP_REPORT ✓
- FACT_REGISTRY : 15 entrées (dont 3 ✦, 6 ✧, 5 ⁕, 1 ⁕)
- **GATE_CHECK : PASS**

---

## RÉSUMÉ EXÉCUTIF

La description du missile Flamingo par Ancel est **largement confirmée** par les sources ouvertes.

**Ce qui est confirmé :**
- Le missile FP-5 Flamingo existe (Fire Point, révélé août 2025) — **✦ CONFIRMÉ**
- La frappe sur Volgograd (Titan-Barrikady) a eu lieu dans la nuit du 27-28 juin 2026 — **✦ CONFIRMÉ**
- La portée de 3 000 km est cohérente avec les annonces officielles — **✧ ATTESTÉ**
- La charge d'une tonne (~1 150 kg) est exacte — **✧ ATTESTÉ**
- Le missile est subsonique et peu furtif (moteur recyclé, vitesse modeste) — **✧ ATTESTÉ**

**Ce qui est omis :**
- Le coût unitaire ($500k-$1M) non mentionné
- La production limitée non mentionnée
- L'utilisation de composants soviétiques recyclés non mentionnée
- Le guidage principalement par GPS/INS, pas révolutionnaire

**Verdict : ✧ CONFIRMÉ — les affirmations techniques d'Ancel sur le Flamingo sont cohérentes avec les données publiques, avec une légère tendance à l'omission des limites (production, composants recyclés).**

---

## CHRONOLOGIE

| Date | Événement |
|------|-----------|
| 2024 | Fire Point commence développement FP-5 Flamingo |
| Août 2025 | Révélation publique du missile Flamingo |
| 2025-2026 | Frappes sur Cheboksary, Votkinsk, Chapayevsk |
| 27-28 juin 2026 | Frappe sur Titan-Barrikady (Volgograd) |
| 28 juin 2026 | Ancel décrit le Flamingo sur BFM |

---

## DOMAINES

- **Technique :** Missile de croisière, guidage, propulsion
- **Militaire :** Frappe longue portée, guerre d'attrition
- **Industriel :** Production d'armement ukrainienne
- **Stratégique :** Capacité de dissuasion asymétrique

---

## RÉSEAU D'ACTEURS

- **Guillaume Ancel** : analyste, décrit le Flamingo
- **Fire Point** : fabricant privé ukrainien du Flamingo
- **Volodymyr Zelensky** : confirme la frappe sur Volgograd
- **Titan-Barrikady (Volgograd)** : cible de la frappe
- **OTAN / Diehl Defence** : intérêt pour améliorations (seeker, guidage)

---

## CHAÎNES DE CASCADE

```
[2022] Restrictions occidentales sur missiles longue portée
  └ [2022-2024] Ukraine développe production missiles domestique
     └ [2024-2025] Fire Point développe Flamingo
        └ [Août 2025] Révélation publique
           └ [2025-2026] Frappes sur cibles stratégiques russes
              └ [Juin 2026] Frappe Volgograd → Ancel sur BFM
```

---

## CARTE DES PREUVES

| # | Fait | Source | Verdict |
|---|------|--------|---------|
| 01 | Flamingo existe (Fire Point) | Atlantic Council | ✦ CONFIRMÉ |
| 02 | Frappe Volgograd confirmée | Kyiv Independent, Zelensky | ✦ CONFIRMÉ |
| 03 | Portée 3 000 km | Wikipedia | ✧ ATTESTÉ |
| 04 | Charge ~1 150 kg (1 tonne+) | Wikipedia | ✧ ATTESTÉ |
| 05 | Vitesse 850-950 km/h (pas furtif) | TheDefenseWatch | ✧ ATTESTÉ |
| 06 | Moteur AI-25TL recyclé | Wikipedia | ✧ ATTESTÉ |
| 07 | Frappes précédentes documentées | United24 | ✧ ATTESTÉ |
| 08 | Coût $500k-$1M | TheDefenseWatch | ✧ ATTESTÉ |
| 09 | Cible = artillerie lourde russe | OSINT | ✦ CONFIRMÉ |

---

## PÉRIMÈTRE & LIMITES

- Aucune source ne confirme la cadence de production exacte
- Le niveau exact de composants occidentaux dans le Flamingo n'est pas public
- La portée de 3 000 km est une revendication — la portée effective dépend du profil de mission
- Les performances du missile en conditions réelles de guerre électronique intense ne sont pas documentées publiquement
- Ancel ne révèle pas sa source d'information (accès privilégié ? informations publiques ?)

---

*Pipeline : TRUTH ENGINE v2.0 — KERNEL.md §0→19 | Complexity: MEDIUM | GATE_CHECK: PASS*
