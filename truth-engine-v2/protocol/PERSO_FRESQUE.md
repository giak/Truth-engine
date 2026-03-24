# PERSO_FRESQUE — Biography Investigation Protocol (APEX)

**Version:** 2.0
**Activation:** When investigation subject is a person → FORCE APEX
**EDI target:** ≥ 0.75 minimum

---

## MODULES

### 0. Activation Check
- Subject is a person (politician, public figure, CEO, etc.)
- Investigation type set to APEX
- PERSO_FRESQUE mode activated

### 1. Chronological Research (Reconnaissance)
Establish raw timeline without interpretation.
- `site:wikipedia.org "[Name]" parcours OR carrière OR mandats`
- `site:vie-publique.fr "[Name]" biographie OR fonctions`
- `"[Name]" élection première OR mandat local`

### 2. Substance Audit (Primary Sources ◈)
Extract real legislative production.
- `site:assemblee-nationale.fr "[Name]" rapports OR lois OR amendements filetype:pdf`
- `site:senat.fr "[Name]" activité parlementaire OR rapports d'information`
- `"[Name]" proposition de loi déposée OR amendement adopté`

### 3. Influence & Capture Analysis (Network)
Identify shadow hands.
- `site:haute-autorite-transparence.fr "[Name]" déclaration patrimoine OR intérêts`
- `"[Name]" lobbying OR "cabinets de conseil" OR McKinsey`
- `"[Name]" comparaison texte amendement lobby OR FNSEA OR MEDEF`

### 4. Pivot Search (Ω-Long & Convergence)
Find the "fault" and validate the drift.
- `"[Name]" promesse "[Subject]" vs vote réel`
- `"[Name]" revirement OR trahison OR changement de position`
- `site:mediapart.fr OR site:disclose.ngo "[Name]" enquête`

---

## EVALUATION GRID

| Metric | Weight | Description |
|--------|--------|-------------|
| **ROI Démocratique** | 30% | Real substance produced / Public cost |
| **Indice de Capture** | 25% | Ghostwriting + Lobby dependency |
| **Intégrité Sémantique** | 20% | Discourse stability vs Λ-Drift |
| **Cœur Ω (Inversion)** | 25% | Fidelity to commitments score |

**SCORE FINAL: [X / 100]**

---

## DETECTION PATTERNS

### ROI_DEMOCRATIQUE
- Official duration of mandate (years)
- Cumulative salary/funding (CPC)
- Structural laws (SW10) vs spectacle (SW0.1)
- Query: "bilan activité parlementaire", "rapports rédigés par"

### Λ_DRIFT (Semantic Drift)
- Inversion of keywords (Conquest vs Exercise)
- Adoption of corporate framing terms
- High correlation with think-tank "Elements of Language"
- Query: "discours archives", "interventions média", "évolution positionnement"

### GHOST_POWER (Ghostwriting)
- Textual similarity > 80% with lobby proposals
- Stylometric mismatch with persona's usual style
- Rapid response to lobby needs in legislation
- Query: "amendements clés en main", "position lobby"

### Ω_LONG (Longitudinal Inversion)
- Vote opposite to campaign promise (The Pivot)
- Accumulation of reversal points over 5+ years
- Justification via "Pragmatism" (Λ trick)
- Query: "promesses électorales vs votes", "renoncement"

### CUI_BONO_PATH
- Pantouflage anticipation (revolving door)
- Favoritism in votes before sector change
- Delta between declared vs real asset growth (HATVP)
- Query: "déclaration patrimoine", "liens privés", "reconversion"

---

## INVESTIGATION PHASES

### Phase 1: Archaeology
Trace all mandates ◈. Sources: Assemblee-Nationale, Senat, Wikipedia, Vie-Publique.
Calculate: CPC = sum(indemnities + cabinet_budgets)

### Phase 2: Substance Weight Audit
Weights: SW10 (structural laws) | SW5 (reports/amendments) | SW0.1 (tweets/media)
Metric: Democratic_ROI = sum(SW) / CPC

### Phase 3: Pivot Detection (Ω)
Target: Detect The Betrayal Point. Compare: Initial Promise ◈ vs First Block Vote.
Log: Date + Logic of reversal

---

## ITERATION PROTOCOL

1. **Divergence Check (≋):** If source (◉) contradicts official doc (◈), allocate 3 additional queries on that point.
2. **Convergence Target:** C(n) ≥ 0.90. Investigation stops only when new searches return no structuring elements.
3. **95% Hostility Symmetric:** Obligation to search for criticisms (🔥) AND defenses (⟐) for each major action identified.

---

## VALIDATION CRITERIA

- [ ] Minimum 15 sources distilled (◈:5 ◉:5 ○:5)
- [ ] EDI Final ≥ 0.75
- [ ] Exhaustive timeline (zero gap > 12 months)
- [ ] Λ-Drift analysis based on ≥ 3 distinct temporal sources
- [ ] Identification of ≥ 1 "Wolf" (mentor or shadow network)

---

## TRIGGERS

IF PERSO_FRESQUE activated:
1. Lock mode to APEX by default
2. Replace standard Phase 3 with MANDATORY Λ-Drift analysis
3. Set EDI Target ≥ 0.85 (high historical depth required)
4. Trigger WOLF Mode (network expansion)
5. Generate Final "Fresco" structure

---

_Version 2.0 — Biography investigation with APEX tenacity_
_Referenced by: KERNEL.md §1 step 4, protocol/INVESTIGATION.md PERSO_FRESQUE_
