---
description: Generate fact-based tweets from Truth Engine investigations
agent: code
subtask: true
---
Generate fact-based, sharp tweets from the investigation file at $ARGUMENTS.

## Instructions

1. Read the investigation file at `$ARGUMENTS` completely.
2. Extract the 5-7 most tweetable facts (each must have: number + actor/context).
3. For EACH fact, generate a tweet in ONE of these styles:
   - **DATA BOMB**: 1 shocking number + minimal context
   - **MISSING PIECE**: What the original text didn't say
   - **COMPARE**: France vs EU/reality comparison
   - **REVERSE**: Flip the narrative with data
   - **WHO PAYS**: Cui bono — who bears the cost
   - **FACT STACK**: 3 cold facts, zero commentary
   - **QUESTION**: Rhetorical question backed by data

4. After generating, validate EVERY tweet with: `!`/home/giak/projects/truth-engine/tools/scripts/char-tool.sh validate 250 "tweet text"`
5. If any tweet exceeds 250 chars, either:
   - Truncate it with: `!`/home/giak/projects/truth-engine/tools/scripts/char-tool.sh truncate 250 "tweet text"`
   - OR rewrite it shorter (preferred)
6. Present all valid tweets with their character count.

## Output format

Present each tweet as:

```
[STYLE] (XX/250 chars)
Tweet text here
```

Generate 7-10 tweets total. **DENSITY MANDATORY: target 220-250 chars.** A tweet under 200 chars is a failure — pack in 3-5 facts, not just 1.

Prioritize:
- Factual accuracy (use exact numbers from the investigation)
- Sharpness (the data should speak for itself)
- Diversity of angles (don't repeat the same point)
- **DENSITY**: use all 250 chars available. Each tweet should feel like a mini-thread compressed into one post.
