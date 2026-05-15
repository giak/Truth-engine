# CLUSTER_FRAGMENTATION

@SCORING: ⫸=convergence_score×index_count | ⫸≥5→activate | ≥7→deep_dive | ≥9→faisceau_constitué
@TRIGGERS: ≥5→selective | ≥7→all_concepts+convergence_analysis+5H | ≥9→full_faisceau

@CONCEPTS:
| Concept | Detection | Query_Boost |
|---------|-----------|-------------|
| INDICES_CONVERGENCE | Multiple independent indices point same direction | "converging evidence", "multiple indicators" |
| TEMPORAL_MAPPING | Events align in suspicious pattern | "timeline", "sequence", "pattern" |
| ACTOR_OVERLAP | Same actors appear across domains | "same person", "overlapping", "connected" |
| FINANCIAL_TRACE | Money flows connect seemingly unrelated events | "funding source", "financial link" |
| NARRATIVE_SYNC | Narratives align across unrelated outlets | "same story", "identical framing", "sync" |
| INSTITUTIONAL_PATTERN | Same institutional behavior across contexts | "pattern", "systematic", "consistent" |
| GEOGRAPHIC_SPREAD | Same phenomenon in multiple locations | "multiple countries", "widespread", "global" |
| ESCALATION_PATTERN | Gradual intensification across domains | "escalation", "increasing", "growing" |
| SUPPRESSION_SYNC | Same topics suppressed simultaneously | "censored together", "simultaneous suppression" |
| BENEFICIARY_ALIGNMENT | Same beneficiaries across events | "same beneficiary", "who profits" |

@QUERIES:
`{topic} converging evidence multiple indicators` | `{topic} timeline sequence pattern alignment` | `{topic} same person overlapping connected actors` | `{topic} funding source financial link connection` | `{topic} same story identical framing sync` | `{topic} pattern systematic institutional behavior` | `{topic} multiple countries widespread global` | `{topic} escalation increasing growing pattern` | `{topic} censored together simultaneous suppression` | `{topic} same beneficiary who profits alignment`

@DEEP_DIVE(≥7):
H1 CONVERGENCE: how many independent indices align? | H2 TEMPORAL: do events align in time? | H3 ACTORS: who appears across domains? | H4 FINANCIAL: what money connects the dots? | H5 BENEFICIARY: who benefits from the convergence?

@MAX(≥9):
Faisceau constitué → full convergence analysis → multi-domain mapping → cross-reference CLUSTER_MONEY + CLUSTER_TEMPORAL for financial and temporal links

@OUTPUT: ⫸ score + convergence level | active concepts + evidence | convergence map | H1-H5 | faisceau assessment

@CONNECTIONS: parent:⫸ | pairs:[MONEY,TEMPORAL,NETWORK] | patterns:[INDICES_CONVERGENCE,TEMPORAL_MAPPING,FINANCIAL_TRACE] | Gate:KERNEL §2
