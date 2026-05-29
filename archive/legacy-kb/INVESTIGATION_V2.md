# INVESTIGATION_V2 — Macros (compressed)

## @INV2[ADAPT]
- Input: raw text
- Detect: domain (health/finance/pol/geo/tech), languages (detected + local), geo (entities), sensitive
- Output: profile {domain, lang_targets, geo_targets, sensitive}

## @INV2[QUERY]
- Build query baskets from profile:
  - official/msm | primary/filetype(pdf,csv,doc) | citation/bibliography | adversary/regional(ccTLD+lang) | investigative(leaked/court) | archives(Wayback)
  - Templates and connectors: KB/QUERY_BASKETS + KB/DOMAIN_CONNECTORS
- Iterate I0→I2 with budgets; re‑query if quotas unmet (quotas: KB/QUOTAS)
## @INV2[BFS]
- Follow 1–2 levels of references/footnotes from key sources
- Heuristic: +1 ◈ per ≤2 ◉

## @INV2[ANTI]
- Dedup: simhash + title_norm + domain_root
- Families: gov/IGO/corp/ind/academ → avoid redundancy
- IndependenceScore: diversity of families + low syndication

## @INV2[TEMP]
- Sliding windows: 24h/72h/7j/30j
- Compute P_random per window + cross‑domain sync; aggregate

## @INV2[SCORE]
- CoverageScore: quotas met ratio
- ContradictionCoverage: adversary/≋ presence
- EDI* = 0.5×EDI + 0.3×Coverage + 0.2×Independence
- See KB/SCORES for definitions

## @INV2[OUT]
- Part 1–2–3 standard + “gaps restants” if quotas not fully met
