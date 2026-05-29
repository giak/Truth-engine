# DESIGN DOC : SUBLIMATOR v8.0 — THE APEX MATRIX

**Date** : 2026-02-23
**Status** : Approved (via Brainstorming)
**Topic** : Refactoring the Sublimator prompt engine for universal, forensic-grade investigation articles.

## 1. Problem Statement
The previous iterations of the writing prompt (v3.0 to v7.0) suffered from two main weaknesses :
1. **Data Loss / Fragmentation** : The LLM sometimes "forgot" critical data points when dealing with 5-10+ investigation files.
2. **Brittle Calibration** : The categories (Political, Financial, etc.) were too specific and failed to adapt to novel or hybrid investigation types.
3. **Role Ambiguity** : The transition from data extraction to high-impact storytelling wasn't sufficiently codified.

## 2. Proposed Solution
Implementing a **Matrix-First Architecture**. The prompt will force the creation of an intermediate "Forensic Matrix" markdown file that acts as the single source of truth (SSOT) for the final article.

## 3. Design Components

### 3.1 Role : The Forensic Architect & Storyteller
The LLM role is redefined as an expert who must first architect the data structure before narrating the results. This prevents "writing from memory" and forces "writing from data".

### 3.2 Phase 1 : The Forensic Matrix (ENQUETE_CONSOLIDEE_MATRIX.md)
A mandatory output that aggregates every forensic atom from all input files.
- **Columns** : `Element` | `Evidence (◈ Source)` | `Systemic Function` | `Danger Level`.
- **Constraint** : Must be exhaustive (no data left behind).

### 3.3 Phase 2 : Adaptive Calibration
The LLM will perform a "Complexity Audit" on its own Matrix to decide :
- **Article Length** : Scaled to Evidence Density.
- **Narrative Pillars** : Detected dynamically (Real Estate, Tech, Geopolitics, etc.) based on data clustering.

### 4. Narrative Requirements (The Forge)
- **Collision Hooks** : Every section must start with a collision between PR and Data.
- **Evidence Density Index (EDI)** : Inclusion of data points per 500 words.
- **Format** : Title and Subtitles must include emojis as requested by the user.
- **Style** : "Cold Cut" (No adjectives, precision-driven impact).

## 5. Success Criteria
- [ ] 100% data retention from investigation tracks.
- [ ] Article quality comparable to the Sarah Knafo 'Magnum Opus' (Step Id: 503).
- [ ] Fully generic adaptability to any topic.
