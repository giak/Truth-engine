# REGRESSION ANALYSIS: KERNEL.md vs system.md

**Date**: 2026-01-19
**Analysis**: Brutal honesty, zero sycophancy

---

## 🔴 CRITICAL REGRESSIONS FOUND

### Missing KB References

| system.md | Line | KERNEL.md | Status |
|-----------|------|-----------|--------|
| `LOAD: kb/COGNITIVE_DSL_CORE.md` | 87 | ❌ MISSING | **REGRESSION** |
| `LOAD: kb/CLUSTER_{concept}.md` | 104 | ✅ Present (generic) | Partial |
| `LOAD: kb/PROTOCOLE_FRESQUE_POLITIQUE.md` | 126 | ❌ MISSING | **REGRESSION** |
| `LOAD: kb/INVESTIGATION_TREE.md` | 306 | ❌ MISSING | **REGRESSION** |
| `LOAD: kb/INVESTIGATION.md` | implied | ✅ Line 272 | OK |

### Missing Explicit KB Load Instructions

```
KERNEL.md §2.1 says:
  "Score ≥4 → LOAD: CLUSTER_ICEBERG"

BUT does not include full path:
  SHOULD BE: "LOAD: kb/CLUSTER_ICEBERG.md"

This is ambiguous. File extension and path missing.
```

### Missing Modes

| Feature | system.md | KERNEL.md |
|---------|-----------|-----------|
| PERSO_FRESQUE mode | ✅ Lines 124-128 | ❌ MISSING |
| INVESTIGATION_TREE | ✅ Lines 301-311 | ❌ MISSING |
| Query Optimization v8.3 | ✅ Lines 269-282 | ⚠️ Partial (line 268) |

---

## 🟡 MISSING DETAILS

### Phase 3.5: HISTORICAL_PRECEDENTS

system.md has PHASE 3.5 (lines 206-247) for searching historical precedents.
KERNEL.md does NOT have this phase.

### MnemoLite Integration Details

system.md has explicit tool syntax:
```yaml
EXECUTE: ReadMcpResourceTool(
  server="mnemolite",
  uri="memories://search/{url_encoded_keywords}"
)
```

KERNEL.md says only:
```
PHASE 0.5: MEMORY_LOOKUP
├─ Query prior investigations (if memory available)
```

**Loss**: How to query MnemoLite is not specified.

### Output Structure Details

system.md specifies SEARCH_INDEX fields explicitly (lines 397-437).
KERNEL.md mentions fields but doesn't show example format.

---

## 🟢 IMPROVEMENTS IN KERNEL.md

| Improvement | Details |
|-------------|---------|
| DSL Ontology | §1 adds 5 foundational principles (missing in system.md) |
| Command Semantics | §3 defines LOAD explicitly (undefined in system.md) |
| EDI Formula | §4.2 has complete formula with weights |
| Boot Concept | §0 and §8 establish activation model |

---

## ⚠️ VERDICT: NOT READY FOR PRODUCTION

KERNEL.md is a better **bootloader** but an incomplete **replacement** for system.md.

### To Fix:

1. Add explicit KB paths for each LOAD command
2. Add PERSO_FRESQUE mode section
3. Add INVESTIGATION_TREE activation for APEX
4. Add PHASE 3.5 HISTORICAL_PRECEDENTS
5. Add MnemoLite query syntax
6. Add SEARCH_INDEX example format

### Recommendation:

KERNEL.md should be the **BOOT** section.
system.md content should follow as **EXECUTION** section.
Or merge both.
