# CLUSTER_BIO

@SCORING: Bio=(Hidden_Networks/Public_Positions)×Density+Inbreeding+Demo_Risk | ♦≥5→activate | ≥7→deep_dive | ≥9→elite_reproduction
@TRIGGERS: ≥5→selective | ≥7→all_concepts+8D_analysis+5H | ≥9→full_biography_archaeology

@CONCEPTS:
| Concept | Detection | Query_Boost |
|---------|-----------|-------------|
| ELITE_REPRODUCTION | Same families/schools/clubs reproduce power | "dynasty", "legacy", "old money", "same school" |
| REVOLVING_DOOR | Person moves between public/private sectors | "former position", "lobbyist", "consultant" |
| HIDDEN_NETWORKS | Connections not visible in official bio | "classmate", "club member", "family tie" |
| SOCIAL_CAPITAL | Access through relationships, not merit | "knows the right people", "connections" |
| MERITOCRACY_ILLUSION | Success attributed to merit, actually network | "self-made", "merit", "hard work" myth |
| CLASS_CONTINUITY | Power stays within same social class | "aristocracy", "bourgeoisie", "establishment" |
| CULTURAL_CAPITAL | Taste/education as power marker | "Ivy League", "grande école", "cultural codes" |
| INFLUENCE_MAPPING | Who influences whom behind the scenes | "advisor", "mentor", "behind the scenes" |
| BIOGRAPHY_WHITENWASH | Negative aspects removed from public bio | "omitted", "hidden past", "sanitized" |
| ACCESS_HIDDEN | How person got position not transparent | "how did they get there", "appointment process" |

@QUERIES:
`{person} dynasty legacy old money same school` | `{person} former position lobbyist consultant` | `{person} classmate club member family tie` | `{person} knows the right people connections` | `{person} self-made merit myth reality` | `{person} aristocracy bourgeoisie establishment` | `{person} Ivy League grande école cultural codes` | `{person} advisor mentor behind the scenes` | `{person} omitted hidden past sanitized` | `{person} how did they get there appointment process`

@DEEP_DIVE(≥7):
H1 8D_ANALYSIS: education, career, family, clubs, boards, donations, media, politics | H2 REVOLVING_DOOR: timeline of public→private moves | H3 HIDDEN_NETWORKS: what connections are invisible? | H4 MERITOCRACY: real path to power vs claimed | H5 BIO_WHITENWASH: what is omitted from official bio?

@MAX(≥9):
Elite reproduction confirmed → full biography archaeology → 8-dimensional analysis → network mapping → cross-reference CLUSTER_NETWORK for topology

@OUTPUT: ♦ score + 8D analysis | active concepts + evidence | network map | H1-H5 | elite reproduction assessment

@CONNECTIONS: parent:♦ | pairs:[NETWORK,POWER,MONEY] | patterns:[ELITE_REPRODUCTION,REVOLVING_DOOR,HIDDEN_NETWORKS] | Gate:KERNEL §2
