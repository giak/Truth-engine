# SCL (Symbolic Compression Language) — Decompression Key

**Version:** v7.8 TIER 1
**Purpose:** Compressed example notation for Truth Engine pattern specifications
**Source:** Extracted from [kb/PATTERNS.md](../kb/PATTERNS.md) (SCL Decompression Key section)

**Note:** This is reference documentation for understanding SCL notation used in PATTERNS.md compressed examples. Not required for runtime operations.

---

## 📘 SCL (Symbolic Compression Language) - Decompression Key [v7.8 TIER 1]

**Purpose**: Compressed examples use SCL notation for space efficiency. First 2 examples per pattern remain in full verbose format for training.

**Grammar**:
```
EX{N}{SYM}:{TYPE} P{pub}/H{hid}{NETS} →{METH}→ {CALC} →{CLASS} "{LABEL}" |{META}
```

**Token definitions**:
- `EX{N}` = Example number (1-99)
- `{SYM}` = Pattern symbol (♦=BIO, €=MONEY, 🌐=NET, ⚔=WAR, ⏰=TEMP, Ξ=ICEBERG)
- `{TYPE}` = Actor type (Pol=Political, Corp=Corporate, Acad=Academic, Med=Media, Civ=Civil)
- `P{pub}/H{hid}` = Public positions count / Hidden networks count
- `{NETS}` = Network breakdown {F+C+S+T+K} (Family+Cabinets+Schools+ThinkTanks+Klubs)
  - For MONEY: {shell+crypto+...} (financial channels)
  - For TEMPORAL: E{events}W{days} S{sync}V{vocab}B{bono}H{hist}Z{suppress}
  - For other patterns: Pattern-specific networks
- `{METH}` = Priority method (P0=Quick, P1=Full, P2=Networks, P3=Qualitative)
- `{CALC}` = Calculation steps (variable=formula=result format)
- `{CLASS}` = Classification (Symbol with +/++/+++ intensity)
- `"{LABEL}"` = Short classification label (quoted)
- `|{META}` = Optional metadata (8D:X 5D:Y DR:LEVEL, etc.)

**Separators** (critical for parsing):
- `:` = Field separator | `/` = Ratio | `{}` = Group | `+` = Addition
- `→` = Transformation step | `|` = Metadata delimiter | `"` = Literal string

**Example expansion**:
```
SCL: EX1♦:Pol P12/H45{F3+C8+S12+T15+K7} →P1→ H/P=45/12=3.75 D=20/28=0.71 I=34/45=0.76 R=4×0.71/0.3=9.47 BIO=3.75×0.71+0.76+9.47=12.89 →♦+++ "Caste" |8D:8.0 5D:0.8 DR:EXT

EXPANDS TO:
Example 1: Political Elite (PRIORITY_1)
Actor: Political elite, 12 public positions, 45 hidden networks
Networks: Family(3) + Cabinets(8) + Schools(12) + ThinkTanks(15) + Clubs(7)
Method: PRIORITY_1 (full quantified calculation)
Calculation:
  Base: H/P = 45/12 = 3.75
  Density: D = 20/28 = 0.71 (high closure)
  Inbreeding: I = 34/45 = 0.76 (extreme)
  DemoRisk: R = 4×0.71/0.3 = 9.47
  Bio_Factor: 3.75×0.71+0.76+9.47 = 12.89
Classification: ♦+++ "Caste reproduction"
Metadata: 8D avg 8.0, 5D avg 0.8, DemocraticRisk EXTREME
```

**Usage**: LLM should mentally expand SCL to full format when analyzing. First 2 examples per pattern provide training template.

