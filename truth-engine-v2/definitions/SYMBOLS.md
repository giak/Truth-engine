# SYMBOLS v2.4 — Canonical ontology and routing

This file alone defines symbols, epistemic statuses and cluster routing. Scores route work; they never prove intent, coordination or manipulation.

## §1 Narrative symbols — assess all 15

| Symbol | Name | Question tested | Typical indicators |
|---|---|---|---|
| Ξ | Omission | What material context/data is absent? | selection, denominator, hidden population, missing method |
| € | Money | Which material flows/interests shape the case? | funding, ownership, subsidy, capture, conflict of interest |
| Λ | Framing | How is the interpretive frame constrained? | false choice, loaded terms, talking points, context removal |
| Ω | Inversion | Are action, blame or past statements reversed? | contradiction, projection, denial, memory rewrite |
| Ψ | Sideration | Does volume/urgency/emotion impair judgment? | flood, conflict storm, panic, fatigue, helplessness |
| ↕ | Vertical power | Are rules/resources/accountability asymmetric? | closure, dependency, double standard, structural harm |
| Φ | Spectacle | Does attention/emotion displace substance? | drama, personalization, clickbait, distraction |
| Σ | Semiotics | Do symbols/branding replace material evidence? | simulacrum, green/sports/woke-washing, staged imagery |
| Κ | Cynicism | Is a known façade maintained despite disbelief? | public/private gap, ritual denial, mutual knowledge |
| ρ | Resistance | What evidence-based counter-power exists? | whistleblowing, independent checks, civil resistance |
| κ | Subtle influence | Is choice architecture steering behavior? | defaults, friction asymmetry, social proof, dark patterns |
| ⫸ | Convergence | Do independent indicators materially converge? | actor/funding/timing overlap, repeated institutional pattern |
| ⚔ | Cognitive warfare | Is there evidenced organized influence activity? | coordination, infrastructure, targeting, persistence |
| 🌐 | Network | How are actors and control points connected? | centrality, gatekeepers, endogamy, cross-sector roles |
| ⏰ | Temporal | Does sequencing/timing change interpretation? | synchronized release, deletion, agenda pivot, artificial urgency |

**Final score [0..10]:** 0 assessed absent; 1–2 weak; 3–4 plausible; 5–6 material; 7–8 strong; 9–10 extensive. Every score needs named observations. `✗` means unassessed and blocks.

`DEFERRED(INPUT_NOT_EVIDENCE)` is a temporary phase-0 routing state only for TOPIC/PERSON/UPDATE inputs that contain no substantive current material. It is not a score, absence or fact status. Step 9 must replace all 15 DEFERRED values with evidence-based scores before FACT_REGISTRY; any remaining DEFERRED blocks delivery. A high score means “inspect deeply”, not “hypothesis confirmed”.

## §2 Epistemic symbols and canonical fact statuses

### Source role — claim-relative

| Symbol | Role | Meaning |
|---|---|---|
| ◈ | Direct/primary | Object closest to the claim: record, dataset, filing, full speech, direct observation. Primary for what it directly contains only. |
| ◉ | Analytical/secondary | Analysis that exposes method and traceable evidence. |
| ○ | Discovery/tertiary | Summary, commentary, aggregator or unsupported assertion; useful to locate evidence. |
| ⟐ | Dominant/official | Perspective label, not reliability grade. |
| ⟐̅ | Critical/counter | Perspective label, not reliability grade. |
| 🌍 | Regional/local | Perspective from affected or comparable regions. |
| 🎓 | Academic/expert | Expertise label; method and conflicts still require review. |
| 🔥 | Dissident | Power-position label; suppression does not make a claim true. |

An official source can be ◈ for “the institution declared X” and ○ for “X is true”. Classify evidence per claim, never publisher prestige.

### Fact status — use exactly these in FACT_REGISTRY

| Symbol | Status | Rule |
|---|---|---|
| ✦ | CONFIRMED | Specific claim-relevant direct evidence; provenance/authenticity checked; material contradiction resolved; independent corroboration where needed. |
| ✧ | PROBABLE | Strong support but one material check, scope issue or independent corroboration remains. |
| ⁕ | CLAIMED | Attributed assertion with no adequate direct verification. |
| ⁂ | SPECULATED | Explicit hypothesis/inference; no direct proof. |
| ⊗ | CONTRADICTED | Material evidence conflicts and is unresolved. |
| ⊙ | PARTIAL | Separable elements are supported, others are not. |
| ⁅ | UNKNOWN | Evidence absent, inaccessible or insufficient; explicit GAP. |
| ❧ | REFUTED | Stronger claim-relevant evidence establishes the claim false within stated scope. |

`⁇` is a read-only legacy alias of `⁅`; normalize new output to `⁅`.

These 8 status glyphs are EPISTEMIC statuses for the narrative fact registry. The machine `FACT_REGISTRY_V1` `tier` field (FACT_VERIFICATION §4.5) is source quality and admits only {✦,✧,⁅,❧}; the epistemic statuses ⁕⁂⊗⊙ map to the `epi` text field, never to `tier`.

Corroboration markers: `⊕` independent concordance; `⊗` material contradiction; `⊙` partial agreement; `≋` narrative divergence; `⚑` temporal/coordination red flag requiring verification.

## §3 Factual lenses

| Symbol | Lens | Checks |
|---|---|---|
| V | Verifiability | provenance, directness, authenticity |
| C | Coherence | logic, scope, internal contradiction |
| S | Sources | independence, diversity, circularity |
| T | Temporality | date, sequence, contemporaneous knowledge |
| M | Memory | precedent and prior records; never proof by itself |
| E | Economic | flows, funding, ownership, externalities |
| A | Actors | actions, authority, responsibility boundaries |
| ♦ | Biography | chronology, affiliations, revolving doors, omissions |

## §4 Canonical cluster routing

| Primitive | Load trigger | Lower mandatory review | File |
|---|---:|---:|---|
| Ξ | 5 | 3 | clusters/ICEBERG.md |
| € | 5 | 3 | clusters/MONEY.md |
| Λ | 5 | 4 | clusters/FRAMING.md |
| Ω | 5 | 4 | clusters/INVERSION.md |
| Ψ | 5 | 4 | clusters/OVERLOAD.md |
| ↕ | 5 | 4 | clusters/POWER.md |
| Φ, Σ | 5 | — | clusters/SPECTACLE.md |
| Κ | 5 | — | clusters/INVERSION.md |
| ρ | 5 | — | clusters/RESISTANCE.md |
| κ | 5 | — | clusters/CONFIRMATION.md |
| ⫸ | 5 | — | clusters/FRAGMENTATION.md |
| ⚔ | 5 | — | clusters/WAR.md |
| 🌐 | 5 | — | clusters/NETWORK.md |
| ⏰ | 5 | — | clusters/TEMPORAL.md |
| ♦ | PERSON/BIOGRAPHY | — | clusters/BIO.md |

Rules: for numeric rows, load at/above threshold; below it, load only an applicable lower-mandatory row; otherwise note without loading. `♦` is a contextual factual lens, not a sixteenth narrative score: `INPUT_KIND=PERSON` or an explicit biographical investigation loads `clusters/BIO.md` directly; NEVER fabricate a ♦ score. Additional review: `Ξ≥7 → clusters/GASLIGHTING.md`, `€≥7 → clusters/NETWORK.md + clusters/POWER.md`, `Ω≥7 → clusters/CONFIRMATION.md`. Deduplicate files. Cluster evidence may refine a narrative score downward or upward; it cannot bootstrap its own trigger.

## §5 Resonance — query hints only

`Ψ+Ω` fear/inversion | `Λ+Σ` frame/symbols | `€+♦` money/biography | `Ξ+⏰` omission/timing | `⚔+🌐` operations/network.

These combinations add cross-checks; they do not add confidence or establish coordination.

_Canonical authority: ontology, statuses and routing._
