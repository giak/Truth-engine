# INVESTIGATION — Ancel 10 : « Missile Flamingo — « shkand », technologie anti-brouillage et guidage terrain »

> **Source :** Débat BFM TV, segment Ukraine/Russie, 2026-06-28
> **Intervenant :** Guillaume Ancel, lieutenant-colonel (séquences 1893-1914)
> **Affirmation :** « Les Ukrainiens ont réussi à faire un shkand, c'est-à-dire à trouver un moyen technologique de dérouter les systèmes de brouillage russe qui sont très puissants et qui reposaient essentiellement sur le fait de perturber les signaux des GPS. [...] Les Ukrainiens ne le confient pas, donc je pense que c'est vrai, qu'ils aient trouvé un moyen de faire du suivi de terrain, ce qui leur permet de descendre beaucoup plus bas et d'utiliser des routes qui sont normalement difficiles à suivre sans une navigation parfaite. »
> **Pipeline :** TRUTH ENGINE v2.0 — KERNEL.md §0→19
> **Complexité :** MEDIUM (7 sections)
> **GATE_CHECK :** PASS

---

## §0 — TEXT ANALYSIS

### BIAS TEST

| Rang | Source | Justification |
|------|--------|---------------|
| 1 (E) | Academic peer-reviewed study | Analyse des technologies de guidage de missiles (TERCOM, INS) |
| 2 (D) | AFP Factuel | Vérification des capacités anti-brouillage ukrainiennes |
| 3 (C) | Citizen eyewitness video | Non pertinent pour technologie de guidage |
| 4 (A) | Viginum | Agence étatique — biais pro-souveraineté technologique |
| 5 (B) | RT | Source antagoniste — niera les capacités ukrainiennes |

**Résultat :** E > D > C > A > B — **PASS**

### MANIPULATION_REPORT

```
├── SYMBOLS:
│   Ξ:4 (OMISSION — Ancel omet que le TERCOM nécessite des modèles
│       numériques de terrain très haute résolution. Omet que le guidage
│       primaire du Flamingo reste le GPS/INS. Omet que les capacités
│       TERCOM ne sont pas confirmées officiellement. Omet que les
│       missiles de croisière occidentaux utilisent le TERCOM depuis
│       les années 1980 — pas une innovation ukrainienne)
│   €:0
│   Λ:3 (FRAMING — « Shkand » comme mot mystérieux, quasi magique.
│       Présente l'anti-brouillage comme une innovation ukrainienne
│       unique, alors que le TERCOM est une technologie mature)
│   Ω:1
│   Ψ:2 (URGENCY — Le brouillage russe crée une menace existentielle,
│       l'anti-brouillage ukrainien est la contre-mesure décisive)
│   ↕:1
│   Φ:2 (SPECTACLE — Image du missile volant « plus bas que possible »
│       en suivant le terrain, comme dans un film de guerre)
│   Σ:1
│   Κ:2 (mutual_knowledge — Le public sait que le GPS est facile à
│       brouiller, comprendre le défi)
│   ρ:3 (COGNITIF — Dissonance : si le brouillage russe est si
│       puissant, comment les Ukrainiens le déjouent-ils ? Le mystère
│       « shkand » crée de l'intrigue)
│   κ:1
│   ⫸:1
│   ⚔:2 (COGNITIVE_WARFARE — Récit d'ingéniosité technologique
│       ukrainienne, renforce le narratif de supériorité adaptative)
│   🌐:2 (NETWORK — Partenariats potentiels avec Diehl Defence
│       pour améliorer le seeker)
│   ⏰:1
│
├── PATTERNS: [—]
├── THREATS: [—]
├── RHETORICAL: {DEM:1 BF:3 NUM:1 AUTH:3 FAC:2}
│   → BF=3: « shkand » — terme non-standard, possible confusion
│     auditive ou invention. « Je pense que c'est vrai » — admission
│     de spéculation
│   → AUTH=3: Ancel se présente comme connaissant les détails
│     techniques du guidage
│
├── CLUSTERS: [— NOTE_ONLY]
│
├── IMPLICIT:
│   - Le brouillage GPS russe est un problème critique résolu
│   - L'Ukraine a développé une technologie de guidage unique
│   - Le « shkand » est une innovation secrète et révolutionnaire
│   - Le suivi de terrain permet d'éviter la détection radar
│   - Les Ukrainiens gardent secret leur innovation
│
├── SPEAKER: {tone: enthousiaste-technique, target: public BFM,
│   goal: démontrer l'ingéniosité technologique ukrainienne en
│   révélant une capacité de guidage avancée}
│
├── PRIORITIES: [vérifier le terme « shkand », documenter les
│   technologies d'anti-brouillage du Flamingo, analyser le TERCOM
│   comme technologie standard, comparer avec les capacités
│   occidentales]
│
└── QUERY_GUIDANCE: [rechercher les technologies de guidage du
    Flamingo, les capacités TERCOM, l'anti-brouillage GPS ukrainien,
    le guidage inertiel, les systèmes CRPA]
```

---

## §1 — PROTOCOL

### Step 1 — TEMPORAL

- **Date :** 28 juin 2026
- **Contexte :** Guerre des drones, guerre électronique intensive depuis 2022

### Step 3 — COMPLEXITY

| Dimension | Score | Justification |
|-----------|-------|---------------|
| political | 1 | Peu d'enjeu politique |
| technical | 3 | Guidage, anti-brouillage, TERCOM |
| temporal | 2 | Technologie développée depuis 2022 |
| geo | 1 | Applicable à tout le territoire russe |
| narratives | 2 | Récit d'ingéniosité ukrainienne |
| data | 2 | Données techniques vérifiables |

**Total : 11 → MEDIUM**

### Step 6 — CRÉDO (12 questions)

```
C — 1. Q:Le terme « shkand » existe-t-il dans la terminologie des
      missiles ? (aucune source ne le confirme)
C — 2. Q:Le Flamingo utilise-t-il le TERCOM (terrain contour matching)
      comme technologie de guidage ?
C — 3. Q:Le TERCOM est-il une innovation ukrainienne ou une
      technologie standard occidentale ?
C — 4. Q:Comment le Flamingo résiste-t-il au brouillage GPS russe ?
D — 5. Q:L'Ukraine a-t-elle accès aux modèles numériques de terrain
      haute résolution pour le territoire russe ?
C — 6. Q:Le guidage du Flamingo est-il principalement GPS/INS ou
      a-t-il d'autres capacités ?
C — 7. Q:Quelles contre-mesures russes existent contre le TERCOM ?
C — 8. Q:Le guidage terrain est-il une technologie mature (utilisée
      par Tomahawk, Storm Shadow depuis décennies) ?
C — 9. Q:Les Ukrainiens utilisent-ils des antennes CRPA (Controlled
      Reception Pattern Antenna) contre le brouillage ?
D — 10. Q:Ancel a-t-il une source spécifique pour cette information
       ou est-ce une spéculation ?
C — 11. Q:Diehl Defence collabore-t-il avec Ukraine pour améliorer
       le seeker du Flamingo ?
C — 12. Q:Le guidage terrain permet-il vraiment de voler « plus bas » ?
```

### Step 10 — FACT_REGISTRY

#### Partie A — L'affirmation

| # | Fait | Acteur | Fiabilité |
|---|------|--------|-----------|
| 1 | « Shkand » : moyen de dérouter le brouillage russe | Ancel | ⁕ (CLAIMED) |
| 2 | Suivi de terrain (TERCOM-like) pour vol à basse altitude | Ancel | ⁕ (CLAIMED) |

#### Partie B — Contexte : technologies de guidage

| # | Fait | Date | Source | URL | Fiabilité |
|---|------|------|--------|-----|-----------|
| 3 | TERCOM (terrain contour matching) : technologie mature utilisée par missiles de croisière US (Tomahawk) depuis 1980s | 1980-2026 | Academic | — | ✦ CONFIRMÉ |
| 4 | Flamingo utilise GPS/INS comme guidage primaire — pas de confirmation officielle de TERCOM | 2025-2026 | Wikipedia | https://en.wikipedia.org/wiki/FP-5_Flamingo | ✧ ATTESTÉ |
| 5 | Ukraine utilise antennes CRPA (Controlled Reception Pattern Antenna) pour résister au brouillage GPS | 2024-2026 | TheDefenseWatch | — | ✧ ATTESTÉ |
| 6 | TERCOM nécessite modèles numériques de terrain haute résolution (DEM) — accès ukrainien non confirmé pour territoire russe | — | The Dock on the Bay | https://medium.com/the-dock-on-the-bay/ukraines-flamingo-fp-5-cruise-missile-coming-with-tercom-guidance-data-a1c26e391870 | ⁕ (SPÉCULATION) |
| 7 | Diehl Defence intéressé par amélioration du seeker du Flamingo | 2026 | TheDefenseWatch | — | ✧ ATTESTÉ |
| 8 | Guidage basse altitude = contournement radar, mais nécessite navigation précise | — | Academic | — | ✦ CONFIRMÉ |
| 9 | Aucune source ne mentionne le terme « shkand » — probable erreur de transcription ou de formulation | — | — | — | ⁕ (INVÉRIFIABLE) |

### Step 12 — IMPACT

| Matrice | Verdict |
|---------|---------|
| Qui gagne | Ukraine (capacité anti-brouillage) |
| Qui perd | Russie (brouillage inefficace) |
| Qui meurt | — |
| Qui recule | — |

### Step 18-18b — GATE_CHECK

- TEXT_ANALYSIS ✓ | MANIP_REPORT ✓
- FACT_REGISTRY : 9 entrées (dont 3 ✦, 3 ✧, 2 ⁕, 1 ⁕)
- **GATE_CHECK : PASS**

---

## RÉSUMÉ EXÉCUTIF

L'affirmation d'Ancel sur la capacité anti-brouillage du Flamingo est **plausible mais spéculative** dans ses détails.

**Ce qui est vérifié :**
- Le guidage TERCOM (suivi de terrain) est une technologie standard des missiles de croisière — pas une innovation ukrainienne
- Le Flamingo utilise GPS/INS ; les capacités TERCOM ne sont pas officiellement confirmées
- L'Ukraine utilise des antennes CRPA anti-brouillage
- Diehl Defence explore des améliorations

**Ce qui est problématique :**
- Le terme « shkand » n'existe dans aucune source technique — probable erreur de transcription ou de formulation d'Ancel
- Le TERCOM nécessite des modèles de terrain haute résolution — l'accès ukrainien aux DEM russes n'est pas confirmé
- Ancel lui-même admet spéculer (« les Ukrainiens ne le confient pas, donc je pense que c'est vrai »)
- La technologie de guidage terrain existe depuis les années 1980 — ce n'est pas une innovation révolutionnaire

**Verdict : ⁕ PLAUSIBLE MAIS SPÉCULATIF — la capacité anti-brouillage est réelle (antennes CRPA, INS), mais le « shkand » comme technologie secrète révolutionnaire est probablement une exagération médiatique. Le suivi de terrain est une technologie standard, pas une innovation ukrainienne unique.**

---

## CHRONOLOGIE

| Date | Événement |
|------|-----------|
| 1980s | TERCOM développé pour missiles Tomahawk |
| 2022 | Brouillage GPS russe intensif contre armes ukrainiennes |
| 2024 | Ukraine déploie antennes CRPA anti-brouillage |
| 2025 | Flamingo révélé — guidage GPS/INS |
| 2026 | Diehl Defence intérêt pour améliorations seeker |
| 28 juin 2026 | Ancel décrit le « shkand » sur BFM |

---

## DOMAINES

- **Technologique :** Guidage de missiles, anti-brouillage, TERCOM
- **Militaire :** Guerre électronique
- **Médiatique :** Terminologie technique, spéculation

---

## RÉSEAU D'ACTEURS

- **Guillaume Ancel** : analyste, spécule sur la technologie
- **Fire Point** : fabricant du Flamingo
- **Diehl Defence** : entreprise allemande, partenariat potentiel
- **Russie (guerre électronique)** : brouillage GPS Krasukha, R-330Zh

---

## CHAÎNES DE CASCADE

```
[2022-2024] Brouillage GPS russe massif
  └ [2024-2025] Ukraine développe contre-mesures (CRPA, INS renforcé)
     └ [2025] Flamingo : GPS/INS + possible TERCOM
        └ [2026] Ancel : « shkand »
           → Plausible (anti-brouillage réel) mais spéculatif
             (TERCOM non confirmé, « shkand » inventé)
```

---

## CARTE DES PREUVES

| # | Fait | Source | Verdict |
|---|------|--------|---------|
| 01 | TERCOM technologie standard (1980s) | Academic | ✦ CONFIRMÉ |
| 02 | Flamingo GPS/INS primaire | Wikipedia | ✧ ATTESTÉ |
| 03 | CRPA utilisé par Ukraine | TheDefenseWatch | ✧ ATTESTÉ |
| 04 | Diehl Defence intérêt | TheDefenseWatch | ✧ ATTESTÉ |
| 05 | « Shkand » non référencé | — | ⁕ INVÉRIFIABLE |
| 06 | Accès DEM russe non confirmé | — | ⁕ SPÉCULATION |
| 07 | Guidage terrain = vol bas | Academic | ✦ CONFIRMÉ |

---

## PÉRIMÈTRE & LIMITES

- Le terme « shkand » pourrait être une erreur de transcription du SRT (mot mal compris, déformé à l'oral)
- Ancel admet lui-même spéculer (« je pense que c'est vrai »)
- Les spécifications exactes du Flamingo ne sont pas publiques
- Le TERCOM est une technologie mature — son intégration dans le Flamingo est plausible mais non confirmée
- L'efficacité réelle en conditions de guerre électronique intense n'est pas documentée

---

*Pipeline : TRUTH ENGINE v2.0 — KERNEL.md §0→19 | Complexity: MEDIUM | GATE_CHECK: PASS*
