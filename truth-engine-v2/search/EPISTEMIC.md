# SEARCH EPISTEMIC v2.8 — Corpus diversity diagnostic

This file owns source-role classification and EDI. EDI measures diversity/coverage of the collected corpus, not truth, confidence or moral legitimacy.

## §1 Claim-relative source roles

| Role | Use | Checks |
|---|---|---|
| ◈ Direct/primary | closest inspectable object for the exact claim | authenticity, provenance, completeness, scope, date |
| ◉ Analytical/secondary | analysis of traceable evidence | method, access to originals, expertise, conflicts, reproducibility |
| ○ Discovery/tertiary | locate objects/context or record an assertion | upstream source, attribution, unsupported interpretation |

Classify per claim. An official release is ◈ for what was officially announced, not automatically for whether the announced fact is true. A leak is ◈ only after provenance/authenticity review. Whistleblower, academic, dissident, state, corporate and independent labels do not set reliability.

Corroboration requires independent upstream evidence. Syndication, copied datasets and circular citation count once. Use EVIDENCE_REGISTRY `SRC-ID` and `UPSTREAM_FAMILY` rather than publisher count.

## §2 Diversity dimensions [0..1]

Determine applicability before scoring. A genuinely local/monolingual/instantaneous question may make a dimension N/A; renormalize remaining weights and explain.

```text
geo   = mean(local_or_affected_presence, affected_regions_coverage, relevant_external_comparison)
lang  = mean(original_language_coverage, relevant_languages_coverage, traceable_translation)
strat = mean(direct_evidence_coverage, analytical_challenge_coverage, low_upstream_circularity)
owner = mean(ownership_type_coverage, low_dominant_owner_share, ownership_traceability)
persp = materially_supported_applicable_perspectives / applicable_perspectives
temp  = covered_relevant_temporalities / relevant_temporalities
```

Perspective set has exactly five members: `⟐ dominant/official`, `⟐̅ critical/counter`, `🌍 local/regional`, `🎓 academic/expert`, `🔥 dissident`. Presence requires a material, relevant contribution; a token citation does not count.

Temporalities: contemporaneous, recent, archival, historical — include only those the question needs.

## §3 Canonical EDI

```text
weights = geo:.25 lang:.20 strat:.20 owner:.15 persp:.15 temp:.05
EDI_raw = Σ(weight[d]×score[d]) / Σ(weight[d]) for applicable d
EDI = clamp(EDI_raw - unique_penalties, 0, 1)
```

Penalties are corpus warnings, applied once per underlying cause:

| Flag | Trigger | Penalty |
|---|---|---:|
| OWNERSHIP_CONCENTRATION | one upstream owner/family >60% | .10 |
| POWER_BLOC_CONCENTRATION | one materially interested power bloc >75% | .15 |
| MISSING_COUNTER | credible opposed perspective applicable but absent | .10 |
| NO_DIRECT_EVIDENCE | decisive claims need direct objects but none obtained | .15 |
| CIRCULAR_EVIDENCE | >50% accepted support shares one upstream object | .15 |
| UNTRACEABLE_TRANSLATION | decisive translated evidence lacks traceable original | .05 |

Do not stack OWNERSHIP and POWER_BLOC for the same concentration; keep the larger. Do not penalize a missing perspective that is genuinely unavailable/non-applicable; report the gap.

Bands: `≥.65 BROAD | ≥.50 ADEQUATE | ≥.35 LIMITED | <.35 MONOCULTURE_RISK`.

Base targets: SIMPLE .30, MEDIUM .50, COMPLEX .70, APEX .80. Explicit legacy branch targets may override when selected and recorded: PERSO .75, SENSITIVE .65, PROSPECTIVE .50, INTERNATIONAL .65. Targets trigger search while material gaps remain; they cannot block an honest inconclusive result or upgrade a fact.

## §4 Coverage, independence and convergence

```text
COV = met_applicable_search_targets / applicable_search_targets
IND = unique_upstream_evidence_families / accepted_evidence_sources
CC  = resolved_material_contradictions / material_contradictions; if none, N/A
EDI* = .5×EDI + .3×COV + .2×IND
C(n) = 1 - new_unique_material_items_n / total_unique_material_items_after_n
```

All denominators must be >0; otherwise output `N/A`. `EDI*` and `C(n)` remain process diagnostics. Convergence means diminishing new material, not correctness.

Iteration guide: I0 map leads/claims/axes/sources → I1 fill decisive gaps → I2 triangulate/contradict → I3 synthesize/reopen. LEAD_AUDIT saturation does not imply OBJECT_INVESTIGATION saturation. Stop only when KERNEL lead/axis coverage is terminal, after bounded gate corrections, or when access is exhausted; record why.

## §5 Decisive-claim coverage

Global EDI can look adequate while one decisive claim still depends on a single evidence family. Therefore report a non-scalar coverage profile for every decisive CLM-ID:

```text
CLM-ID | direct object:YES/NO/N/A | independent families:{n}
credible counter:FOUND/NONE_FOUND/N/A | freshness:CURRENT/STALE/UNKNOWN | GAP_TYPE
```

This profile does not create a new score or status. It routes a bounded correction when a decisive claim lacks an applicable direct object, independent provenance, current evidence or credible counter-search. A broad corpus cannot compensate for a decisive single point of failure.

## §6 Adversarial/counter perspective (H7)

For politically or materially contested subjects, seek the strongest source that represents opposed interests or interpretation and actually engages the claim. Search by actor, jurisdiction, original language, watchdog/opposition/defense terms and underlying documents.

State-funded adversarial media, dissident outlets and institutional opponents are discovery/perspective candidates, not privileged truth sources. Recheck current ownership, access, evidence and relevance. If no credible counter-source is found, log `NONE_FOUND`; do not fabricate balance.

## §7 Required output

```text
[SOURCES] ◈:{n} ◉:{n} ○:{n}
EDI:{final} raw:{raw} penalties:{sum}[flags] N/A:{dimensions}
geo:{g} lang:{l} strat:{s} owner:{o} persp:{p} temp:{t}
⟐:{n} ⟐̅:{n} 🌍:{n} 🎓:{n} 🔥:{n} | COV:{c} IND:{i} CC:{cc} EDI*:{e}
DECISIVE_CLAIM_COVERAGE:{profiles}
DIAGNOSTIC_NOT_TRUTH
```

_Canonical authority: source roles and EDI._
