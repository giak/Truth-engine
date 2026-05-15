# CLUSTER_TEMPORAL

@SCORING: P_orch=sync×0.30+vocab×0.25+cui_bono×0.20+hist×0.15+suppress×0.10 | ⏰≥5→activate | ≥7→deep_dive | ≥9→orchestration_confirmed
@TRIGGERS: ≥5→selective | ≥7→all_concepts+P_random_calc+5H | ≥9→orchestration_proof+timeline_reconstruction

@CONCEPTS:
| Concept | Detection | Query_Boost |
|---------|-----------|-------------|
| TIMING_SYNC | Multiple events <12h apart, coordinated announcements | "simultaneous announcement", "coordinated release" |
| VOCAB_UNIFORM | Identical terminology across outlets, shared talking points | "talking points", "language guide", "messaging" |
| CUI_BONO_TIMING | Beneficiaries prepared before event, positions pre-positioned | "prepared statement", "pre-positioned" |
| HISTORICAL_PATTERN | Same timing pattern as previous operations | "similar timing", "same pattern", "repeat" |
| SUPPRESSION_WINDOW | Counter-evidence disappears before/during event | "removed article", "deleted tweet", "retracted" |
| ARTIFICIAL_URGENCY | "Immediate action required", manufactured deadline | "urgent", "time-sensitive", "act now" |
| DISTRACTION_TIMING | Unrelated scandal released during critical moment | "distraction", "news dump", "Friday release" |
| ANNIVERSARY_MANIPULATION | Date chosen for emotional resonance, not factual | "anniversary", "symbolic date", "commemoration" |
| SILENCE_PERIOD | Strategic silence before/after key events | "no comment", "silent period", "media blackout" |
| NARRATIVE_SHIFT | Sudden topic change, agenda pivot | "suddenly", "now focusing on", "new priority" |

@QUERIES:
`{topic} simultaneous announcement coordinated` | `{topic} talking points messaging guide` | `{topic} prepared statement pre-positioned` | `{topic} similar timing same pattern repeat` | `{topic} removed article deleted retracted` | `{topic} urgent time-sensitive manufactured deadline` | `{topic} distraction news dump Friday release` | `{topic} anniversary symbolic date commemoration` | `{topic} silent period media blackout` | `{topic} suddenly agenda pivot topic change`

@DEEP_DIVE(≥7):
H1 TEMPORAL MAP: full timeline, who spoke when, gaps? | H2 P_RANDOM: probability of coincidence? | H3 CUI BONO TIMING: who was ready before event? | H4 SUPPRESSION TRACE: what disappeared and when? | H5 DISTRACTION ANALYSIS: what else happened simultaneously?

@MAX(≥9):
Orchestration confirmed → full timeline reconstruction → P_random calculation → source coordination evidence → narrative synchronization proof → impact on public perception

@OUTPUT: ⏰ score + P_orch | active concepts + evidence | P_random | timeline map | H1-H5 | orchestration assessment

@CONNECTIONS: parent:⏰ | pairs:[ICEBERG,WAR,NETWORK] | patterns:[TIMING_SYNC,VOCAB_UNIFORM,SUPPRESSION_WINDOW] | Gate:KERNEL §2
