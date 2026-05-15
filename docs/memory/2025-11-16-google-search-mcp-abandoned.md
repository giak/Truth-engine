# Memory: Google Search MCP Integration ABANDONNÉ

**Date:** 2025-11-16
**Type:** Decision
**Context:** Truth Engine dual-engine search enhancement attempt
**Result:** ABANDONED after load testing (0% success rate)
**Author:** Claude Code (Sonnet 4.5)

---

## Summary

Attempted to integrate `web-agent-master/google-search` (Playwright-based Google scraping) to add a third search engine alongside existing WebSearch (Google API) and MCP web-search (DuckDuckGo).

**Load Test Results (25 queries):**
- Burst (0s delay): 0/10 success (0%)
- Moderate (5s delay): 0/10 success (0%)
- Conservative (30s delay): 0/5 success (0%)
- **TOTAL: 0/25 success (0%)**

## Root Cause

Google anti-bot overlay blocks 100% of Playwright headless searches:
```
elementHandle.click: Timeout 30000ms exceeded.
<div class="AG96lb"> intercepts pointer events
```

No mitigation successful (delays, fingerprinting, IP cooldown).

## Architecture Decision

**KEEP existing Truth Engine architecture:**
1. Claude WebSearch (Google API official) - 95%+ success
2. MCP web-search (DuckDuckGo) - 60-80% success
3. Query Optimization v8.3 (splitting + hybrid fallback)

Adding google-search package would:
- Add 0% success (no benefit)
- Add 13-20 min latency per investigation (pure cost)
- Degrade user experience

## Lessons Learned

1. **Playwright Google scraping = non-viable 2025**
   - Anti-bot detection insurmountable
   - Official APIs infinitely better

2. **Load testing critical before integration**
   - Saved 8-10h dev time by testing first
   - Realistic scenarios (5-30 queries) revealed issues

3. **Existing architecture already optimal**
   - Dual-engine already present (WebSearch + MCP)
   - Avoid "solutionnisme" (adding tools without validating need)

## References

- Post-mortem: [docs/postmortems/2025-11-16-google-search-mcp-ABANDONED.md](../postmortems/2025-11-16-google-search-mcp-ABANDONED.md)
- Archived plan: [docs/plans/archived/2025-11-16-google-search-mcp-integration-ABANDONED.md](../plans/archived/2025-11-16-google-search-mcp-integration-ABANDONED.md)

## Tags

`google-search`, `playwright`, `anti-bot`, `truth-engine`, `abandoned`, `load-testing`, `mcp`, `web-scraping`, `dual-engine`, `decision`
