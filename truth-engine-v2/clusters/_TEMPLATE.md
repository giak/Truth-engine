# CLUSTER TEMPLATE — Structure Reference

**Usage:** Each cluster file contains ONLY unique data. Structure is defined here.

```
# CLUSTER_{NAME}
@SCORING: {formula} | {glyph}≥5→activate | ≥7→deep_dive | ≥9→max_protocol
@TRIGGERS: ≥5→selective | ≥7→all_concepts+5H | ≥9→max+full_trace

@CONCEPTS: (10 rows)
| Concept | Detection | Query_Boost |

@QUERIES: (10 when ≥5)
- "{topic} {keyword}"

@DEEP_DIVE(≥7): 5H
H1: {mapping} | H2: {evidence} | H3: {history} | H4: {network} | H5: {counter}

@MAX(≥9): {cluster-specific escalation}

@OUTPUT: {glyph} score + active_concepts + evidence + H1-H5 results + PRIMARY_chain + impact

@CONNECTIONS: parent:{glyph} | pairs:[CLUSTER_X,CLUSTER_Y] | patterns:[PAT1,PAT2] | Gate:KERNEL §2
```
