# 🖼️ CLUSTER PERSONA_FRESQUE - Longitudinal Analysis

_Extended Persona Investigation Protocol (UltraThink v2.2)_

## Parent: 👤 (PERSONA)

Activated when subject is "person" OR explicitly requested via "fresque"

---

## 🔍 MODULES DE RECHERCHE INTENSIVE (SEARCH_INTEL)

### 0. Activation Check

_Objectif: Vérifier l'activation du mode PERSONA_FRESQUE_

- **Triggers**: Subject est une personnalité politique
- **Action**: Si pas activé, ARRÊTER et activer le mode
- **Checklist**:
  - [ ] Subject is a known politician
  - [ ] PERSO_FRESQUE mode activated
  - [ ] Investigation type set to APEX

### 1. Recherche Chronologique (I0: Reconnaissance)

_Objectif: Établir la timeline brute sans interprétation._

- **Queries**:
  - `site:wikipedia.org "[Nom]" parcours OR carrière OR mandats`
  - `site:vie-publique.fr "[Nom]" biographie OR fonctions`
  - `"[Nom]" élection première OR mandat local`

### 2. Audit de Substance (I1: Primary Sources ◈)

_Objectif: Extraire la production législative réelle._

- **Queries**:
  - `site:assemblee-nationale.fr "[Nom]" rapports OR lois OR amendements filetype:pdf`
  - `site:senat.fr "[Nom]" activité parlementaire OR rapports d'information`
  - `"[Nom]" proposition de loi déposée OR amendement adopté`

### 3. Analyse d'Influence & Capture (I2: Network & Ghostwriting)

_Objectif: Identifier les mains de l'ombre._

- **Queries**:
  - `site:haute-autorite-transparence.fr "[Nom]" déclaration patrimoine OR intérêts`
  - `"[Nom]" lobbying OR "cabinets de conseil" OR McKinsey`
  - `"[Nom]" comparaison texte amendement lobby OR FNSEA OR MEDEF`

### 4. Recherche de Pivot (I3: Ω-Long & Convergence)

_Objectif: Trouver la "faille" et valider la dérive._

- **Queries**:
  - `"[Nom]" promesse "[Sujet]" vs vote réel`
  - `"[Nom]" revirement OR trahison OR changement de position`
  - `site:mediapart.fr OR site:disclose.ngo "[Nom]" enquête OR "le loup"`

---

## 🔄 PROTOCOLE D'ITÉRATION

1. **Divergence Check (≋)**: Si une source (◉) contredit un document officiel (◈), allouer 3 recherches supplémentaires sur ce point précis.
2. **Convergence Target**: C(n) ≥ 0.90. L'enquête ne s'arrête que si les nouvelles recherches ne rapportent plus d'éléments structurants.
3. **95% Hostilité Symétrique**: Obligation de chercher des critiques (🔥) ET des défenses (⟐) pour chaque action majeure identifiée.

---

## 📊 GRILLE D'ÉVALUATION (v2.2)

| Métrique                 | Poids | Description                             |
| :----------------------- | :---: | :-------------------------------------- |
| **ROI Démocratique**     |  30%  | Substance réelle produite / Coût public |
| **Indice de Capture**    |  25%  | Ghostwriting + Dépendance aux lobbies   |
| **Intégrité Sémantique** |  20%  | Stabilité du discours vs Λ-Drift        |
| **Cœur Ω (Inversion)**   |  25%  | Score de fidélité aux engagements       |

**SCORE FINAL: [X / 100]**

---

## ✅ CRITÈRES DE VALIDATION DU RAPPORT

- [ ] Minimum 15 sources distillées (◈:5 ◉:5 ○:5).
- [ ] EDI Final ≥ 0.75.
- [ ] Timeline exhaustive (zéro trou de plus de 12 mois).
- [ ] Analyse Λ-Drift basée sur au moins 3 sources temporelles distinctes.
- [ ] Identification d'au moins 1 "Wolves" (mentor ou réseau d'ombre).

### ROI_DEMOCRATIQUE

**Pattern**: Substance output vs Public cost
**Detection**:

- Official duration of mandate (years)
- Cumulative salary/funding (CPC)
- Number of structural laws (SW10) vs spectacle (SW0.1)
  **Query boost**: "bilan activité parlementaire", "rapports rédigés par", "lois portées par"

### Λ_DRIFT (Semantic Drift)

**Pattern**: Shift from citizen to lobbyist lexicon
**Detection**:

- Inversion of keywords (Conquest vs Exercise)
- Adoption of corporate framing terms
- High correlation with think-tank "Elements of Language"
  **Query boost**: "discours archives", "interventions média", "évolution positionnement"

### GHOST_POWER (Ghostwriting)

**Pattern**: Unattributed lobby influence in production
**Detection**:

- Textual similarity > 80% with lobby proposals (FNSEA, MEDEF, etc.)
- Stylometric mismatch with persona's usual style
- Rapid response to lobby needs in legislation
  **Query boost**: "amendements clés en main", "position lobby", "propositions de loi"

### Ω_LONG (Longitudinal Inversion)

**Pattern**: Structural betrayal of core mandates
**Detection**:

- Vote opposite to campaign promise (The Pivot)
- Accumulation of reversal points over 5+ years
- Justification via "Pragmatism" (Λ trick)
  **Query boost**: "promesses électorales vs votes", "renoncement", "trahisons politiques"

### CUI_BONO_PATH

**Pattern**: Career path favoring private capture
**Detection**:

- Pantouflage anticipation (revolving door)
- Favoritism in votes before sector change
- Delta between declared vs real asset growth (HATVP)
  **Query boost**: "déclaration patrimoine", "liens privés", "reconversion"

---

## INVESTIGATION PHASES (DSL ADAPTATION)

### Phase 1: Archéologie

```yaml
STEP: Archaeology
ACTION: Trace all mandates ◈
SOURCES: Assemblee-Nationale, Senat, Wikipedia, Vie-Publique
CALCULATE: CPC = sum(indemnities + cabinet_budgets)
```

### Phase 2: Audit SW (Substance Weight)

```yaml
STEP: SW_Calculation
WEIGHTS:
  SW10: Structural Laws (◈ codes)
  SW5: Reports / Technical Amendments
  SW0.1: Tweets / Media Λ
METRIC: Democratic_ROI = sum(SW) / CPC
```

### Phase 3: Detection of Pivot (Ω)

```yaml
STEP: Pivot_Search
TARGET: Detect [The Betrayal Point]
COMPARE: Initial Promise ◈ vs First Block Vote
LOG: Date + Logic of reversal
```

---

## INVESTIGATION TRIGGERS

IF PERSONA_FRESQUE Activated:

1. Lock mode to APEX by default
2. Replace Phase 3 with MANDATORY Λ-Drift analysis
3. Set EDI Target ≥ 0.85 (High historical depth required)
4. Trigger WOLF Mode (Network expansion)
5. Generate Final "Fresco" PDF structure
