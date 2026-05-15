# CLUSTER_WAR

@SCORING: War=(Coordination×Sophistication×Persistence)/(Attribution×Defense) | ⚔≥5→activate | ≥7→deep_dive | ≥9→state_level
@TRIGGERS: ≥5→selective | ≥7→all_concepts+attribution_analysis+5H | ≥9→state_actor_assessment+full_coordination_map

@CONCEPTS:
| Concept | Detection | Query_Boost |
|---------|-----------|-------------|
| COORDINATION | Multiple actors same message, synchronized timing | "coordinated campaign", "message alignment" |
| SOPHISTICATION | Multi-platform, multi-lingual, adaptive tactics | "professional operation", "state-level" |
| PERSISTENCE | Campaign continues over weeks/months, evolving | "ongoing campaign", "persistent operation" |
| ATTRIBUTION_GAP | Source obscured, false flags, proxy actors | "attribution unclear", "false flag", "proxy" |
| DEFENSE_BYPASS | Targets platform vulnerabilities, algorithm exploitation | "algorithm manipulation", "platform exploit" |
| NARRATIVE_WEAPON | Truth used as weapon, factcheck selective | "weaponized factcheck", "selective truth" |
| INFRASTRUCTURE | Bot networks, troll farms, amplification systems | "bot network", "troll farm", "amplification" |
| PSYOPS | Emotional manipulation, fear/anger targeting | "psychological operation", "emotional targeting" |
| GRAY_ZONE | Below threshold of war, plausible deniability | "gray zone", "below threshold", "plausible denial" |
| ESCALATION_LADDER | Gradual intensification, testing responses | "escalation pattern", "testing response" |

@QUERIES:
`{topic} coordinated campaign message alignment` | `{topic} professional operation state-level` | `{topic} ongoing campaign persistent operation` | `{topic} attribution unclear false flag proxy` | `{topic} algorithm manipulation platform exploit` | `{topic} weaponized factcheck selective truth` | `{topic} bot network troll farm amplification` | `{topic} psychological operation emotional targeting` | `{topic} gray zone below threshold plausible denial` | `{topic} escalation pattern testing response`

@DEEP_DIVE(≥7):
H1 ATTRIBUTION: who is behind this? state/non-state/proxy? | H2 INFRASTRUCTURE: what systems support the operation? | H3 TARGETING: who is the audience and why? | H4 ESCALATION: what is the endgame? | H5 COUNTER: what defenses exist and are they effective?

@MAX(≥9):
State-level assessment → full coordination map → infrastructure identification → escalation trajectory → cross-reference CLUSTER_NETWORK for actor mapping

@OUTPUT: ⚔ score + formula inputs | active concepts + evidence | attribution assessment | coordination map | H1-H5 | escalation level

@CONNECTIONS: parent:⚔ | pairs:[NETWORK,TEMPORAL,MONEY] | patterns:[COORDINATION,SOPHISTICATION,ATTRIBUTION_GAP] | Gate:KERNEL §2
