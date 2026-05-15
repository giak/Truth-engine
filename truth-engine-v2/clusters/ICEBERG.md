# CLUSTER_ICEBERG

@SCORING: Factor=N/R (N=omission_dims, R=visible/hidden) | Ξ≥5→activate | ≥7→deep_dive | ≥9→MAX
@TRIGGERS: ≥5→selective | ≥7→all_10_concepts+5H+5q | ≥9→full_shadow_reconstruction+impact

@CONCEPTS:
| Concept | Detection | Query_Boost |
|---------|-----------|-------------|
| OMISSION_SELECTIVE | "Selected period" unexplained, geographic bias | "complete timeline", "all regions" |
| CATEGORY_TRICK | Undefined categories, hidden subcategories | "all categories", "broader definition" |
| SHADOW_POPULATION | "Active" without inactive, "Registered" without unregistered | "unregistered", "informal", "shadow" |
| DENOMINATOR_MANIPULATION | Population base undefined, denominator switch | "calculation method", "denominator" |
| TIMEFRAME_CHERRY | Arbitrary start/end, cherry-picked comparison years | "historical data", "10 year", "since 2000" |
| AVERAGING_TRICK | Mean without median, no standard deviation | "median", "distribution", "percentiles" |
| PROXY_SUBSTITUTION | "Indicator of" not direct measure, real metric hidden | "direct measurement", "actual numbers" |
| COMPARATIVE_ABSENCE | Single number without context, no YoY | "compared to", "versus EU", "year over year" |
| METHODOLOGY_OPACITY | "Proprietary calculation", formula absent | "methodology", "calculation method" |
| CONFIDENCE_MISSING | Precise number without range, no error bars | "confidence interval", "margin error" |

@QUERIES:
`{topic} complete data all categories` | `{topic} methodology explained calculation` | `{topic} confidence interval margin error` | `{topic} median distribution percentiles` | `{topic} compared to international benchmark` | `{topic} historical data 20+ years` | `{topic} shadow population unregistered` | `{topic} denominator base population` | `{topic} direct measurement not proxy` | `{topic} all regions full period`

@DEEP_DIVE(≥7):
H1 QUANTITATIVE SHADOW: real total including hidden categories? | H2 TEMPORAL REVELATION: extend timeframe? | H3 COMPARATIVE TRUTH: international comparison? | H4 METHODOLOGY IMPACT: how much methodology affects result? | H5 DISTRIBUTION REALITY: distribution vs average?

@MAX(≥9):
Missing dims systematic ID → gap quantification → 3+q/dim PRIMARY → Shadow Factor = Total/Visible → narrative reconstruction → official vs reconstructed contradiction → impact assessment

@OUTPUT: Ξ score + signals | active concepts + evidence | shadow multiplier | H1-H5 | PRIMARY chain | impact(0-10)

@CONNECTIONS: parent:Ξ | pairs:[MONEY,NETWORK,TEMPORAL] | patterns:[OMISSION_SELECTIVE,DENOMINATOR_MANIPULATION,SHADOW_POPULATION] | Gate:KERNEL §2
