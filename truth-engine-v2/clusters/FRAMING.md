# CLUSTER_FRAMING

@SCORING: Frame=overlap_count×salience×repetition | Λ≥5→activate | ≥7→deep_dive | ≥9→manufactured_consent
@TRIGGERS: ≥5→selective | ≥7→all_concepts+frame_deconstruction+5H | ≥9→full_narrative_archaeology

@CONCEPTS:
| Concept | Detection | Query_Boost |
|---------|-----------|-------------|
| OVERTON_SHIFT | Unthinkable→acceptable in short timeframe | "new consensus", "shifted debate", "changed narrative" |
| TALKING_POINTS | Identical phrasing across actors, press releases | "talking points", "messaging guide", "talking points memo" |
| FALSE_DICHOTOMY | Only two options presented, alternatives excluded | "only choice", "no alternative", "binary choice" |
| EUPHEMISM | Harsh reality softened by language | "collateral damage", "downsizing", "restructuring" |
| LOADED_LANGUAGE | Emotional terms replacing neutral description | "crisis", "epidemic", "wave", "flood" |
| FRAMING_BY_OMISSION | What's NOT in the frame | "not mentioned", "absent from debate", "ignored" |
| ANCHORING | First number/claim sets reference point | "anchor", "reference point", "baseline" |
| METAPHOR_MANIPULATION | Metaphor shapes interpretation | "war on", "flood of", "battle against" |
| NARRATIVE_PREEMPTION | Story told before facts available | "narrative set", "early framing", "preemptive" |
| CONTEXT_STRIP | Fact presented without necessary context | "decontextualized", "out of context", "stripped" |

@QUERIES:
`{topic} new consensus shifted debate changed narrative` | `{topic} talking points messaging guide` | `{topic} only choice no alternative binary` | `{topic} euphemism softened language` | `{topic} crisis epidemic wave loaded language` | `{topic} not mentioned absent ignored framing` | `{topic} anchor reference point baseline` | `{topic} metaphor war on flood battle` | `{topic} narrative set early framing preemptive` | `{topic} decontextualized out of context stripped`

@DEEP_DIVE(≥7):
H1 OVERTON: what was unthinkable before? who moved the window? | H2 TALKING_POINTS: who wrote them? who disseminated? | H3 FALSE_DICHOTOMY: what alternatives exist? | H4 METAPHOR: what metaphor shapes thinking? | H5 PREEMPTION: narrative set before facts?

@MAX(≥9):
Manufactured consent confirmed → full narrative archaeology → origin tracing → dissemination map → alternative frames reconstruction

@OUTPUT: Λ score + active concepts + evidence | frame deconstruction | OVERTON shift timeline | H1-H5 | manufactured consent assessment

@CONNECTIONS: parent:Λ | pairs:[SPECTACLE,INVERSION,OVERLOAD] | patterns:[OVERTON_SHIFT,TALKING_POINTS,FALSE_DICHOTOMY] | Gate:KERNEL §2
