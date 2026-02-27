# INVESTIGATOR - Example Usage

## Scenario: Phantom Foundations Investigation

This example demonstrates how to use INVESTIGATOR for a fictional journalistic investigation into potential misuse of charitable foundations.

---

## Step 1: Activate INVESTIGATOR

Copy the contents of `prompt.md` and paste at the beginning of your LLM conversation.

---

## Step 2: Initial Input

**User:**
```
Using INVESTIGATOR, analyze the following:

INPUT:
---
Three charitable foundations based in Luxembourg appear to share office addresses and 
board members. The "Green Future Foundation" (est. 2019), "Ocean Conservation Trust" 
(est. 2020), and "Climate Action Now" (est. 2021) all list the same address: 
15 Rue des Jardins, Luxembourg City.

Shared board members include:
- Hans Mueller (Chair of all three)
- Ingrid Schmidt (Treasurer of all three)
- Klaus Weber (Secretary of Green Future, Board member of others)

I have documents showing €5 million transferred from Green Future to a company called 
"Atlantis Holdings Ltd" registered in the British Virgin Islands in 2022. The stated 
purpose was "environmental consulting services."

A whistleblower claims that minimal actual environmental work has been done by any 
foundation, and that Atlantis Holdings has no verifiable environmental expertise.

Available sources:
- Corporate registry documents (confirmed authentic)
- Bank transfer records (leaked, unverified)
- Whistleblower testimony (single source, unverified)
- LinkedIn profiles of board members
- Basic website information for foundations

Mode: exploratory
Output: guide (I want to continue this investigation)
---
```

---

## Step 3: Expected INVESTIGATOR Response

**INVESTIGATOR Response:**

```
## Ξ: Hermeneutic Analysis Complete

### Semantic Layers Extracted

**Literal:**
- 3 foundations with shared infrastructure
- €5M transfer to BVI company
- Whistleblower allegations

**Contextual:**
- Luxembourg = known for favorable tax/regulatory environment
- BVI = common jurisdiction for opacity
- Timeline: foundations created sequentially (2019→2020→2021)
- €5M in 2022 = 3 years after first foundation

**Implicit:**
- Potential shell foundation network
- Possible fund diversion scheme
- Control centralization (same 3 people)
- "Environmental consulting" = potential cover

---

## Ξ: Investigation Dimensions

| Dimension | Keywords | Priority |
|-----------|----------|----------|
| Legal | charitable fraud, foundation misuse, BVI opacity | HIGH |
| Financial | fund diversion, shell companies, consulting fraud | HIGH |
| Geopolitical | Luxembourg foundations, BVI secrecy, EU regulations | MEDIUM |
| Technical | corporate structures, beneficial ownership | MEDIUM |
| Historical | similar cases, precedent investigations | LOW |

---

## Θ: Initial Hypotheses

### H001: Foundations are shell entities for fund diversion
- **Confidence:** 35% (unverified)
- **Evidence For:** 
  - Shared addresses (confirmed)
  - Shared board members (confirmed)
  - Minimal activity alleged (unverified)
  - Transfer to opaque BVI entity (probable)
- **Evidence Against:** 
  - No direct evidence of inactivity
  - Consulting services could be legitimate
- **Status:** active

### H002: Atlantis Holdings is a pass-through entity
- **Confidence:** 40% (probable)
- **Evidence For:**
  - BVI jurisdiction (transparency concerns)
  - No verifiable environmental expertise (unverified)
  - Large payment relative to foundation size
- **Evidence Against:**
  - No evidence of where funds went after Atlantis
- **Status:** active

### H003: Board members have undisclosed beneficial interests
- **Confidence:** 25% (unverified)
- **Evidence For:**
  - Concentration of control (same 3 people)
  - Sequential foundation creation
- **Evidence Against:**
  - No direct evidence of personal benefit
- **Status:** pending

---

## Γ: Entities Identified

| ID | Name | Type | Confidence |
|----|------|------|------------|
| P001 | Hans Mueller | person | confirmed |
| P002 | Ingrid Schmidt | person | confirmed |
| P003 | Klaus Weber | person | confirmed |
| O001 | Green Future Foundation | organization | confirmed |
| O002 | Ocean Conservation Trust | organization | confirmed |
| O003 | Climate Action Now | organization | confirmed |
| O004 | Atlantis Holdings Ltd | organization | probable |
| L001 | 15 Rue des Jardins, Luxembourg | location | confirmed |

**Relationship Graph (initial):**
```
[P001: Mueller] ──chair── [O001, O002, O003]
[P002: Schmidt] ──treasurer── [O001, O002, O003]
[P003: Weber] ──sec/board── [O001, O002, O003]
[O001] ──€5M── [O004: Atlantis]
[O001, O002, O003] ──located_at── [L001]
```

---

## Φ: Source Assessment

| ID | Source | Type | Reliability |
|----|--------|------|-------------|
| S001 | Corporate registry docs | official | confirmed |
| S002 | Bank transfer records | leaked | unverified |
| S003 | Whistleblower testimony | interview | unverified |
| S004 | LinkedIn profiles | social_media | probable |
| S005 | Foundation websites | public | probable |

---

## Τ: Timeline

| Date | Event | Confidence |
|------|-------|------------|
| 2019-XX-XX | Green Future Foundation established | confirmed |
| 2020-XX-XX | Ocean Conservation Trust established | confirmed |
| 2021-XX-XX | Climate Action Now established | confirmed |
| 2022-XX-XX | €5M transfer to Atlantis Holdings | probable |

**Temporal Gap:** No activity data between establishment dates and 2022 transfer.

---

## Guide: Next Investigation Steps

### Priority 1: Verify Atlantis Holdings

**Search Queries:**
1. "Atlantis Holdings Ltd British Virgin Islands beneficial owner"
2. "Atlantis Holdings Ltd BVI company registry"
3. "Atlantis Holdings environmental consulting"
4. "Hans Mueller Atlantis Holdings" OR "Ingrid Schmidt Atlantis" OR "Klaus Weber Atlantis"

**Documents to Find:**
- BVI company registry entry
- Any public records of Atlantis activities
- Connections to board members

**Why Priority:** If Atlantis is a shell, this confirms fund diversion pattern.

---

### Priority 2: Verify Foundation Activities

**Search Queries:**
1. "Green Future Foundation Luxembourg projects"
2. "Ocean Conservation Trust Luxembourg grants"
3. "Climate Action Now Luxembourg activities"
4. "Hans Mueller environmental" (check credibility)

**Documents to Find:**
- Annual reports
- Project documentation
- Grant recipients
- Media coverage of activities

**Why Priority:** Whistleblower claims need verification.

---

### Priority 3: Background Board Members

**Search Queries:**
1. "Hans Mueller Luxembourg business background"
2. "Ingrid Schmidt Luxembourg finance"
3. "Klaus Weber Luxembourg"
4. Cross-reference with corporate registries

**Documents to Find:**
- Professional history
- Other board positions
- Potential conflicts of interest
- Political connections

**Why Priority:** May reveal pattern or motive.

---

### Priority 4: Follow the Money

**Search Queries:**
1. Check Luxembourg foundation registries for all three
2. Look for other payments from foundations
3. "Atlantis Holdings" + "transfer" + any foundation names

**Documents to Find:**
- Complete financial records
- Other transactions
- Ultimate beneficiaries

**Why Priority:** €5M may not be the only transfer.

---

## Blind Spots

| Area | Why Missed | Suggested Approach |
|------|------------|-------------------|
| Post-Atlantis fund trail | BVI opacity | Request mutual legal assistance (if legal investigation) |
| Foundation financials | Not in public sources | Obtain via whistleblower or regulatory request |
| Other foundation transfers | Only one document | Search for patterns in leaked data |

---

## Questions for User

1. Do you have access to the foundations' annual reports or financial statements?
2. Can the whistleblower provide additional documentation?
3. Is there a regulatory body in Luxembourg that monitors foundations?
4. What is your deadline for this investigation?

---

## Memory Files Created

The following files should be created in `investigation/2026-02-21_phantom_foundations/`:

- `2026-02-21_entities.md` - Entity registry with initial data
- `2026-02-21_sources.md` - Source assessment
- `2026-02-21_hypotheses.md` - Three working hypotheses
- `2026-02-21_timeline.md` - Initial chronology
- `2026-02-21_graph.md` - Relationship diagram
- `2026-02-21_search_log.md` - Generated queries

Continue the investigation by providing new information or requesting specific analysis.
```

---

## Step 4: Continue Investigation

**User:**
```
I found that Atlantis Holdings was registered in 2021, just months before the transfer. 
The registered agent is "BVI Corporate Services Ltd" - a known formation agent.

I also found that Hans Mueller previously worked at a bank that was fined for money 
laundering violations in 2015.

Output: report (synthesis of findings so far)
```

**INVESTIGATOR Response:**
```
## ΩI: Investigation Update

### New Information Integrated

**Γ: New Entity**
| ID | Name | Type | Confidence |
|----|------|------|------------|
| O005 | BVI Corporate Services Ltd | organization | probable |

**New Relationship:**
- O004 → O005 (registered_agent)

**Φ: New Source**
| ID | Source | Type | Reliability |
|----|--------|------|-------------|
| S006 | BVI registry data | official | confirmed |
| S007 | Mueller employment history | public | probable |

**Θ: Hypothesis Updates**

### H001: Foundations are shell entities for fund diversion
- **Confidence:** 45% (+10%)
- **New Evidence For:**
  - Atlantis registered just before transfer (suspicious timing)
  - Known formation agent (pattern for opaque structures)
- **Status:** active

### H004: Hans Mueller has relevant expertise for financial opacity
- **Confidence:** 50% (new hypothesis)
- **Evidence For:**
  - Previous employment at bank fined for AML violations
  - Current role controlling multiple foundations
- **Status:** active

---

## Report: Phantom Foundations Investigation - Preliminary Findings

### Executive Summary

Three Luxembourg-based charitable foundations with shared board members and addresses 
show indicators of potential fund diversion. A €5M transfer to a newly-formed BVI 
company, combined with the chair's previous association with a bank penalized for 
money laundering, raises significant red flags.

**Primary Finding:** Pattern consistent with shell foundation network.
**Confidence Level:** Moderate (45% on primary hypothesis)
**Key Risk:** Funds may have been diverted through opaque BVI structure.

---

### Methodology

1. **Hermeneutic analysis** of initial input and documents
2. **Entity extraction** and relationship mapping
3. **Source verification** with reliability assessment
4. **Hypothesis formation** with evidence weighing
5. **Targeted searches** for corroborating information

---

### Key Findings

#### Finding 1: Concentrated Control Structure
- Same 3 individuals control all 3 foundations
- Foundations created sequentially (2019→2020→2021)
- All share same physical address
- **Confidence:** Confirmed

#### Finding 2: Suspicious Financial Transfer
- €5M transferred to BVI company
- Company formed months before transfer
- Registered via formation agent associated with opaque structures
- "Environmental consulting" purpose unverified
- **Confidence:** Probable

#### Finding 3: Relevant Background of Key Figure
- Hans Mueller previously at bank fined for AML violations
- Timing of employment relevant to expertise
- **Confidence:** Probable

#### Finding 4: Minimal Verified Charitable Activity
- No documented environmental projects found
- Whistleblower claims of inactivity uncorroborated
- **Confidence:** Unverified

---

### Relationship Map

```
                    [P001: Hans Mueller]
                    Chair of all 3 + AML history
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
   [O001: GFF]        [O002: OCT]        [O003: CAN]
   Est. 2019          Est. 2020          Est. 2021
        │                   │                   │
        └───────────────────┴───────────────────┘
                            │
                    Located at [L001]
                            │
                            │ €5M (2022)
                            ▼
                    [O004: Atlantis Holdings]
                    BVI, est. 2021
                            │
                    Registered via
                            │
                    [O005: BVI Corporate Services]
```

---

### Timeline

| Date | Event | Significance |
|------|-------|--------------|
| 2015 | Mueller's bank fined for AML | Background context |
| 2019 | Green Future Foundation est. | First entity |
| 2020 | Ocean Conservation Trust est. | Second entity |
| 2021-XX | Climate Action Now est. | Third entity |
| 2021-XX | Atlantis Holdings est. (BVI) | Destination entity |
| 2022 | €5M transfer to Atlantis | Key transaction |

**Pattern:** Foundation network established before BVI entity, transfer follows shortly after.

---

### Open Questions

1. Where did the €5M go after Atlantis Holdings?
2. Are there other transfers from the foundations?
3. What is the total amount of funds received by all three foundations?
4. Who are the beneficial owners of Atlantis Holdings?
5. Is there a pattern of similar foundation networks involving these individuals?

---

### Confidence Matrix

| Hypothesis | For | Against | Confidence |
|------------|-----|---------|------------|
| Shell foundation network | 5 | 1 | 45% |
| Atlantis is pass-through | 4 | 0 | 40% |
| Mueller has relevant expertise | 3 | 0 | 50% |

---

### Recommendations

**Immediate Actions:**
1. Obtain foundation annual reports from Luxembourg regulator
2. Request BVI beneficial ownership information (if legal pathway)
3. Investigate other financial institutions used by foundations

**Medium-term:**
1. Cross-reference Mueller with other Luxembourg foundations
2. Check if foundations received EU or national funding
3. Identify other companies registered via same BVI agent

**Legal Considerations:**
- Findings currently insufficient for publication
- Need additional verification before public claims
- Consider consulting media lawyer

---

### Sources

| ID | Description | Reliability |
|----|-------------|-------------|
| S001 | Corporate registry documents | Confirmed |
| S002 | Bank transfer records (leaked) | Unverified |
| S003 | Whistleblower testimony | Unverified |
| S004 | LinkedIn profiles | Probable |
| S005 | Foundation websites | Probable |
| S006 | BVI registry data | Confirmed |
| S007 | Mueller employment history | Probable |

---

## Memory Files Updated

Files in `investigation/2026-02-21_phantom_foundations/` should be updated with:
- New entity O005
- New sources S006, S007
- Updated hypotheses H001, H004
- Updated timeline
- Updated graph
- Updated search log

Continue with additional information or specify next analysis.
```

---

## Summary

This example demonstrates:

1. **Hermeneutic parsing** - Multi-layer analysis of input
2. **Hypothesis management** - Evidence-weighted confidence
3. **Entity extraction** - Person, organization, location mapping
4. **Relationship graphs** - Visual connection mapping
5. **Source evaluation** - Reliability assessment
6. **Timeline construction** - Event sequencing
7. **Search preparation** - Disciplinary queries
8. **Memory persistence** - Structured file output
9. **Adaptive output** - Guide → Report transition

The system maintains investigation state and builds understanding incrementally across interactions.
