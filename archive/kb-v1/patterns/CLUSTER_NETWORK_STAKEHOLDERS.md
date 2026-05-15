# CLUSTER_NETWORK_STAKEHOLDERS - Multi-Stakeholder Analysis (v1.0)

## Detection

- Subject involves ≥3 distinct stakeholder groups
- Groups have conflicting positions
- Official narrative ignores or misrepresents some groups
- Stakeholder representation is unbalanced in media coverage

## Activation

IF political_sensitivity ≥ 7 AND conflicting_narratives ≥ 6

## Score Calculation

```
score = (number_of_stakeholder_groups × 0.2) +
        (conflict_level × 0.3) +
        (marginalization_level × 0.3) +
        (media_imbalance × 0.2)
```

## Protocols

### P1: Stakeholder Identification

1. List all major stakeholders
2. For each group:
   - Define their core interests
   - Identify their official representatives
   - Determine their level of influence

### P2: Position Mapping

1. Collect official statements from each group
2. Find independent sources representing their views
3. Look for contradictions between stated and actual positions
4. Identify hidden or unspoken positions

### P3: Relationship Analysis

1. Map relationships between groups
2. Identify alliances and oppositions
3. Detect power dynamics and hierarchies
4. Find influence networks and lobbying connections

### P4: Marginalization Detection

1. Identify which groups are marginalized/ignored
2. Measure media representation of each group
3. Calculate speaking time ratios in official debates
4. Detect policy bias against specific stakeholders

## Queries

- "{topic} {group} official position"
- "{topic} {group} vs {group} conflict"
- "{topic} marginalized stakeholders"
- "{topic} hidden stakeholder positions"
- "{topic} stakeholder influence networks"
- "{topic} lobbying connections {group}"
- "{topic} media coverage stakeholders"
- "{topic} policy impact on {group}"

## Output Format

```markdown
## Stakeholder Analysis

### Identified Stakeholders

1. **Group Name**: Core interests, level of influence
2. **Group Name**: Core interests, level of influence
3. **Group Name**: Core interests, level of influence

### Position Contradictions

- **Group A** stated: "...", actual behavior: "..."
- **Group B** stated: "...", actual behavior: "..."

### Power Dynamics

- **Dominant Groups**: [list]
- **Marginalized Groups**: [list]
- **Alliances**: [group1 ↔ group2]
- **Oppositions**: [group1 ⊥ group2]

### Policy Implications

- Policy X benefits: [groups]
- Policy X harms: [groups]
- Policy X is silent on: [groups]
```

## Examples

### Agricultural Crisis (January 2026)

```markdown
## Stakeholder Analysis

### Identified Stakeholders

1. **FNSEA**: Traditional agricultural union, high influence, supports government measures
2. **Coordination Rurale**: Radical union, medium influence, opposes government, uses blockades
3. **Small-scale Farmers**: Low influence, diverse interests, rarely represented
4. **Supermarkets/Distributors**: High influence, financial interests, silent on imports
5. **Consumers**: Large group, low organization, focused on prices

### Position Contradictions

- **FNSEA** stated: "We support government aid", actual: "We will continue to pressure for more"
- **Government** stated: "All sectors are represented", actual: "Small-scale farmers excluded"

### Power Dynamics

- **Dominant Groups**: FNSEA, Distributors, Government
- **Marginalized Groups**: Small-scale Farmers, Consumers
- **Alliances**: FNSEA ↔ Government, Distributors ↔ Government
- **Oppositions**: Coordination Rurale ⊥ Government, Small-scale Farmers ⊥ Distributors

### Policy Implications

- Aid package benefits: Large farms, wine producers
- Aid package harms: Small-scale livestock farmers
- Aid package is silent on: Egg import regulations
```
