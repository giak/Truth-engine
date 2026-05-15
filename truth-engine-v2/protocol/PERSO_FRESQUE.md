# PERSO_FRESQUE — Biography Investigation Protocol (APEX)

**Version:** 2.1 | **Trigger:** subject=person → FORCE APEX | **EDI target:** ≥0.75

---

## §0 MODULES (DSL)

```
@PF[M0]: person→APEX | EDI≥0.75
@PF[M1:chrono]: wiki+vie-publique+AN | "parcours|carrière|mandats"
@PF[M2:substance◈]: AN+Sénat+lois | "rapports|amendements|proposition" filetype:pdf
@PF[M3:influence]: HATVP+lobby+MEDEF | "déclaration patrimoine|lobbying|cabinets"
@PF[M4:pivot]: promesse≠vote+revirement | "trahison|changement position" + mediapart/disclose
```

## §1 EVALUATION GRID

```
SCORE = ROI_dem(30%) + Capture(25%) + Λ_drift(20%) + Ω_cœur(25%) → /100
@PF[ROI] = Σ(SW) / CPC | SW10=loi_struct | SW5=rapport | SW0.1=tweet/média
@PF[Capture] = ghostwriting + lobby_dependency
@PF[Λ_drift] = keyword_inversion + corporate_frame_adoption + thinktank_language
@PF[Ω_cœur] = promesse≠vote + reversal_accumulation(5y) + "pragmatisme"(Λ_trick)
```

## §2 DETECTION PATTERNS

```
@PF[ROI_DEM]: mandate_years | CPC=Σ(indemnités+budget_cabinet) | SW vs CPC
@PF[Λ_DRIFT]: conquest≠exercise | corporate_terms | thinktank_elements
@PF[GHOST_POWER]: similarity>80%_lobby | stylometric_mismatch | rapid_response
@PF[Ω_LONG]: vote_opposite_promise | reversals(5y+) | justification="pragmatisme"
@PF[CUI_BONO]: pantouflage_anticipation | favoritism_pre_sector | HATVP_delta
```

## §3 PHASES

```
P1[Archaeology]: mandats◈ (AN+Sénat+wiki+vie-publique) → CPC=Σ(indemnités+budgets)
P2[Substance]: SW10/SW5/SW0.1 → Democratic_ROI=Σ(SW)/CPC
P3[Pivot Ω]: promesse◈ vs 1er_bloc_vote → date+logique_renversement
```

## §4 ITERATION + VALIDATION

```
@ITER: ≋(◉≠◈)→+3q | C(n)≥0.90→stop | hostility_symmetric(🔥+⟐) per action
@VALID: ◈≥5◉≥5○≥5 | EDI≥0.75 | timeline_gap≤12mo | Λ_src≥3 | wolf≥1
```

---

_Version 2.1 — 135→72L. Compressed DSL. See KERNEL.md §1 step 4._
