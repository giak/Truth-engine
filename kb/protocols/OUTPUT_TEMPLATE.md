# OUTPUT TEMPLATE — Investigation Structure v1.2

**Usage**: Ce template définit les sections **OBLIGATOIRES** pour tout output d'investigation.
**Gate**: Si une section marquée `[REQUIRED]` est vide → output bloqué.

**OUTPUT PATH**: `outputs/investigations/YYYY-MM/`
- Format filename: `YYYY-MM-DD_{sujet_concis}.md`
- Exemple: `2026-02-26_hayer_europe_assegiee.md`

---

## 📌 TL;DR — Executive Summary [NEW v1.1]
<!-- [REQUIRED] 3-line inline summary for quick comprehension -->

| Line | Content | Max Chars |
|------|---------|-----------|
| 1 | **SUJET**: What is being investigated | 80 |
| 2 | **VÉRÉIFICATION**: Key finding (confirmed/rejected) | 80 |
| 3 | **MANIPULATION**: Main technique from Phase 0 | 80 |

**Example**:
```
TL;DR: SUJET: Médicament X efficacité → VÉRÉIFICATION: Données essais masquées → BIAIS: Pharma finance étude
```

---

## 📋 PROTOCOLE D'INVESTIGATION
<!-- [REQUIRED] Métadonnées de l'investigation -->

| Champ | Valeur |
|---|---|
| Date | <!-- FILL --> |
| Complexité | <!-- FILL: SIMPLE/MEDIUM/COMPLEX/APEX --> |
| Budget requêtes | <!-- FILL: 12/18/25/35+ --> |
| EDI Target | <!-- FILL: 0.30/0.50/0.70/0.80 --> |

---

## ✅ COMPLIANCE CHECKLIST — v15.0 Required
<!-- Verification of mandatory steps — see KERNEL.md §4 for full checklist -->

See KERNEL.md §4 for the 16-item compliance checklist. All items must be checked before output.

**IF ANY NO → BLOCK & RETURN**

---

## 🎯 MANIPULATION REPORT — Phase 0 Results
<!-- [REQUIRED] Result of TEXT_ANALYSIS from §0bis - BLOCK if missing -->

### Symbols Detected
| Symbol | Score | Techniques Found |
|--------|-------|------------------|
| Ξ | X/10 | <!-- cherry_picking, ... --> |
| € | X/10 | <!-- dark_money, ... --> |
| Λ | X/10 | <!-- framing_cognitive, ... --> |
| Ω | X/10 | <!-- gaslighting, ... --> |
| Ψ | X/10 | <!-- infodemia, ... --> |
| ↕ | X/10 | <!-- class_division, ... --> |
| Φ | X/10 | <!-- spectacle, ... --> |
| Σ | X/10 | <!-- greenwashing, ... --> |
| Κ | X/10 | <!-- facade_maintenance, ... --> |
| ρ | X/10 | <!-- resistance --> |
| κ | X/10 | <!-- nudging, ... --> |
| ⫸ | X/10 | <!-- cascade, ... --> |
| ⚔ | X/10 | <!-- psyops, ... --> |
| 🌐 | X/10 | <!-- network_closure, ... --> |
| ⏰ | X/10 | <!-- memory_hole, ... --> |

### Patterns Activated
- [ ] ICEBERG — [ ]
- [ ] ASTRO — [ ]
- [ ] GAS — [ ]
- [ ] MONEY — [ ]
- [ ] BIO — [ ]
- [ ] WAR — [ ]
- [ ] NET — [ ]
- [ ] TEMP — [ ]
- [ ] CYN — [ ]
- [ ] FASC — [ ]

### Threats Detected
- [ ] SHOCK — [ ]
- [ ] BIDERMAN — [ ]
- [ ] GASLIGHT_SOC — [ ]
- [ ] INFODEMIC — [ ]
- [ ] DARK_MONEY — [ ]
- [ ] REGULATORY_CAPTURE — [ ]
- [ ] MYTHOLOGIZATION — [ ]
- [ ] NUDGING — [ ]
- [ ] ASTROTURFING — [ ]

### Rhetorical Families
| Family | Score | Markers |
|--------|-------|---------|
| DEM | X/10 | <!-- --> |
| BF | X/10 | <!-- --> |
| NUM | X/10 | <!-- --> |
| AUTH | X/10 | <!-- --> |
| FAC | X/10 | <!-- --> |

### Clusters to Load
- [ ] <!-- ICEBERG, MONEY, FRAMING, ... -->

### Implicit Claims
1. <!-- What is IMPLIED -->
2. <!-- What is NOT SAID -->
3. <!-- What is INVERTED -->

### Speaker Profile
- **Tone**: <!-- aggressive/defensive/prophetic/victim -->
- **Target**: <!-- who is the enemy? -->
- **Goal**: <!-- what objective? -->

### Verification Priorities
1. <!-- what to verify first -->
2. <!-- ... -->
3. <!-- ... -->

### Query Guidance
- <!-- how detected techniques should guide searches -->

---

## 🔍 REQUEST LOG
<!-- [REQUIRED] Toutes les recherches effectuées -->

| # | TYPE | QUERY | RÉSULTAT | SOURCE |
|---|---|---|---|---|
| 1 | <!-- ◈/◉/○ --> | <!-- FILL --> | <!-- FILL --> | <!-- FILL --> |
<!-- Minimum: 12 queries pour SIMPLE, 35+ pour APEX -->

**VALIDATION**: source_types ≥ 4? <!-- PASS/FAIL -->

---

## 📊 ANALYSE DES CONCEPTS
<!-- [REQUIRED] Minimum 5 concepts pour MEDIUM, 8 pour APEX -->

### Ξ (ICEBERG) — SCORE X/10
- **QUOTE**: "<!-- FILL -->"
- **TECHNIQUE**: <!-- FILL -->
- **REVEAL**: <!-- FILL -->

### € (MONEY) — SCORE X/10
<!-- Répéter pour chaque concept ≥5 -->

**VALIDATION**: concepts_analyzed ≥ 5? <!-- PASS/FAIL -->

---

## 🧊 ICEBERG_DEEP_DIVE
<!-- [REQUIRED if Ξ ≥ 7] Analyse approfondie de l'omission -->

### Hypothèses générées
1. H1: <!-- FILL -->
2. H2: <!-- FILL -->
3. H3: <!-- FILL -->
4. H4: <!-- FILL -->
5. H5: <!-- FILL -->

### Shadow Multiplier
- Réalité totale (N): <!-- FILL -->
- Révélé (R): <!-- FILL -->
- **Factor = N/R = <!-- FILL -->**

### Queries Deep Dive
| # | QUERY | RÉSULTAT |
|---|---|---|
| 1 | <!-- FILL --> | <!-- FILL --> |
<!-- Minimum 5 queries deep dive -->

**VALIDATION**: iceberg_hypotheses ≥ 5? <!-- PASS/FAIL -->

---

## 🐺 WOLF_MAPPING
<!-- [REQUIRED] Minimum 3 acteurs pour MEDIUM, 8 pour APEX -->

| WOLF | RÔLE | CENTRALITÉ | INTÉRÊTS | PREUVES |
|---|---|---|---|---|
| <!-- NOM PROPRE --> | <!-- FILL --> | <!-- 0.0-1.0 --> | <!-- FILL --> | <!-- Query # --> |
<!-- Répéter pour chaque acteur -->

**VALIDATION**: wolves_named ≥ 3? <!-- PASS/FAIL -->

---

## 🔢 EDI_CALCULATION
<!-- [REQUIRED] Calcul détaillé, pas de bullshit -->

```
geo = (continents: X/6 × 0.4) + (zones: X/10 × 0.3) + (local: X × 0.3) = Y
lang = (languages: X/10 × 0.3) + (%non-EN: X × 0.4) + (families: X/5 × 0.3) = Y
strat = (%◈: X × 0.5) + (%◉: X × 0.3) + (%○: X × 0.2) = Y
owner = (types: X/6 × 0.6) + (%non-corp: X × 0.4) = Y
persp = (persp: X/7 × 0.5) + (balance: X × 0.3) + (dissident: X × 0.2) = Y
temp = (temporalities: X/5 × 0.6) + (archival: X × 0.4) = Y

EDI = (geo × 0.25) + (lang × 0.20) + (strat × 0.20) + (owner × 0.15) + (persp × 0.15) + (temp × 0.05)
EDI = <!-- FILL: X.XX -->
```

**VALIDATION**: EDI ≥ target? <!-- PASS/FAIL -->

---

## 🎭 CARTOGRAPHIE DIALECTIQUE
<!-- [REQUIRED] Thèse/Antithèse/Tensions -->

### THÈSE (OFFICIELLE)
- Message: <!-- FILL -->
- Sources: <!-- FILL -->

### ANTITHÈSE (COUNTER)
- Message: <!-- FILL -->
- Sources: <!-- FILL -->

### TENSIONS
1. <!-- FILL -->
2. <!-- FILL -->

**VALIDATION**: dialectic_complete? <!-- PASS/FAIL -->

---

## 🔗 EVIDENCE CHAINS [NEW v1.2]
<!-- [REQUIRED] Links between findings - how do they connect? -->

### Chain 1: [Cause → Effect → Consequence]
- **NODE A** → **NODE B** → **NODE C**
- **Evidence**: Query #X, Query #Y
- **Confidence**: HIGH/MEDIUM/LOW

### Chain 2: 
<!-- Add more chains as needed -->

---

## 🎯 CONFIANCE PAR FINDING [NEW v1.2]
<!-- [REQUIRED] Confidence level for each key finding -->

| Finding | Evidence | Confidence | Justification |
|---------|----------|------------|---------------|
| <!-- FILL --> | <!-- Query # --> | HIGH/MEDIUM/LOW | <!-- Why? --> |

---

## ❓ INCONNUES [NEW v1.2]
<!-- [REQUIRED] What didn't we find? Unanswered questions, gaps -->

| Question | Why Unanswered | Potential Source |
|----------|----------------|------------------|
| <!-- FILL --> | <!-- Not searched / No source / Source blocked --> | <!-- Where to look --> |

---

## 🧭 SUITES [NEW v1.2]
<!-- [REQUIRED] Follow-up leads, next steps -->

| Piste | Priority | Why Important |
|-------|----------|---------------|
| <!-- FILL --> | HIGH/MEDIUM/LOW | <!-- FILL --> |

---

## 📊 SOFT CHECKS (from VALIDATION.md — avertissements, ne bloquent pas)

- [ ] Toutes les sources sont vérifiées
- [ ] Les sources primaires (◈) sont confirmées
- [ ] Aucune source détectée comme fake news
- [ ] Les liens des sources sont fonctionnels
- [ ] Calculs détaillés affichés (pas de bullshit math)

---

## ✅ VALIDATION FINALE

| Gate | Requis | Actuel | Status |
|---|---|---|---|
| source_types | ≥4 | <!-- FILL --> | <!-- PASS/FAIL --> |
| concepts_analyzed | ≥5 | <!-- FILL --> | <!-- PASS/FAIL --> |
| wolves_named | ≥3 | <!-- FILL --> | <!-- PASS/FAIL --> |
| edi_target | ≥X.XX | <!-- FILL --> | <!-- PASS/FAIL --> |
| iceberg_hypotheses | ≥5 (if Ξ≥7) | <!-- FILL --> | <!-- PASS/FAIL --> |
| dialectic_complete | TRUE | <!-- FILL --> | <!-- PASS/FAIL --> |

**GLOBAL STATUS**: <!-- ALL_PASS / BLOCKED -->

IF BLOCKED → Return to Phase indicated by first FAIL gate.
