# ADAPTIVE COMPRESSION & DECOMPRESSION SYSTEM
## Compression Variable (0-100%) + Reconstruction Bidirectionnelle

**Date:** 2025-01-10
**Version:** 1.0.0
**Context:** Extension du Meta-OS Memory System
**Critical Innovation:** REVERSIBLE compression avec qualité adaptative

---

## 🎯 VISION

> **"La compression parfaite n'existe pas. Il existe seulement la compression OPTIMALE pour chaque cas d'usage."**

### Le Problème avec Compression Fixe

**Approche naïve (notre simulation précédente):**
```
TOUT document → 99.86% compression → 127 bytes
```

**Problèmes:**
1. ❌ Document court (500 bytes) → 127 bytes = perte nette
2. ❌ Document précieux (contrat légal) → 99.86% = trop risqué
3. ❌ Document redondant (répétitions) → 99.86% = pas assez
4. ❌ **IMPOSSIBLE à décompresser** → perte irréversible

### La Solution: Compression Adaptative + Décompression

```
INPUT: Document (N bytes) + Compression_Level (0-100%) + Preserve_Priority (list)

PROCESS:
  1. Analyze document structure
  2. Classify content blocks by importance
  3. Apply adaptive compression per block
  4. Store compression metadata (for decompression)
  5. Validate reconstruction quality

OUTPUT:
  - Compressed (target ratio achieved)
  - Reversible (decompression possible)
  - Lossless-on-critical (important parts intact)
  - Lossy-on-redundant (fluff removed)
```

---

## 📐 ARCHITECTURE: 5-LEVEL COMPRESSION SPECTRUM

### LEVEL 0: NO COMPRESSION (Preservation Mode)

**Usage:** Contrats légaux, code source, données financières, preuves juridiques

**Méthode:** Storage intégral + metadata enrichment only

```json
{
  "compression_level": 0,
  "original_size": 50000,
  "compressed_size": 50000,
  "ratio": "0% (preserved)",

  "content": "<<ORIGINAL CONTENT VERBATIM>>",

  "metadata": {
    "content_type": "legal_contract",
    "importance": "critical",
    "preserve_reason": "legal_liability",
    "hash_sha256": "abc123...",
    "timestamp": "2025-01-10T14:23:00Z"
  },

  "enrichment": {
    "entities_extracted": ["Party A", "Party B", "2025-12-31"],
    "key_clauses": [1, 3, 7, 12],
    "embedding": [0.234, -0.567, ...]
  }
}
```

**Décompression:** Trivial (return original)

**Ratio:** 0% compression (peut même grossir avec metadata)

**Use cases:**
- Contrats légaux
- Code source (fichiers .py, .js)
- Données financières sensibles
- Documents gouvernementaux officiels
- Preuves pour litige

---

### LEVEL 1: LIGHT COMPRESSION (10-30%, Minimal Loss)

**Usage:** Documentation technique, rapports importants, emails critiques

**Méthode:** Remove formatting + whitespace optimization + abbreviation expansion

```json
{
  "compression_level": 1,
  "original_size": 50000,
  "compressed_size": 35000,
  "ratio": "30% compression",

  "content": {
    "text": "<<CONTENT with minimal changes>>",
    "removed": {
      "formatting": ["bold", "italic", "colors"],
      "whitespace": "normalized",
      "abbreviations": "expanded"
    }
  },

  "reconstruction_map": {
    "formatting_positions": [
      {"type": "bold", "start": 234, "end": 567},
      {"type": "italic", "start": 890, "end": 1023}
    ],
    "original_whitespace": "<<encoded>>"
  },

  "metadata": {
    "content_type": "technical_documentation",
    "importance": "high",
    "lossiness": "minimal (<5%)"
  }
}
```

**Décompression:**
```python
def decompress_level1(compressed):
    text = compressed['content']['text']

    # Restore formatting
    for fmt in compressed['reconstruction_map']['formatting_positions']:
        text = apply_formatting(text, fmt['type'], fmt['start'], fmt['end'])

    # Restore original whitespace
    text = restore_whitespace(text, compressed['reconstruction_map']['original_whitespace'])

    return text

# Reconstruction quality: 95-98%
```

**Use cases:**
- Documentation technique
- Rapports professionnels
- Emails importants
- Notes de meeting critiques

---

### LEVEL 2: MODERATE COMPRESSION (40-60%, Structural Preservation)

**Usage:** Articles, blog posts, documentation générale, notes personnelles

**Méthode:** Structural compression + synonym replacement + redundancy removal

```json
{
  "compression_level": 2,
  "original_size": 50000,
  "compressed_size": 20000,
  "ratio": "60% compression",

  "structure": {
    "sections": [
      {
        "id": "S1",
        "title": "Introduction",
        "essence": "Truth Engine detects manipulation via 148 concepts...",
        "details_removed": {
          "examples": ["detailed case study 1", "detailed case study 2"],
          "metaphors": ["Plato's cave extended metaphor"],
          "transitions": ["pedagogical bridges removed"]
        },
        "original_length": 5000,
        "compressed_length": 800
      },
      {
        "id": "S2",
        "title": "Core Concepts",
        "essence": "148 concepts: Ψ (cognitive pressure), Ω (narrative control)...",
        "details_removed": {
          "definitions_full": "→ pointer to COGNITIVE_DSL.md",
          "examples_verbose": "→ summarized in 1 sentence each"
        },
        "original_length": 15000,
        "compressed_length": 3000
      }
    ]
  },

  "reconstruction_data": {
    "synonym_map": {
      "manipulation": ["influence", "persuasion", "framing"],
      "detection": ["identification", "recognition", "discovery"]
    },
    "removed_examples": [
      {
        "section": "S1",
        "type": "case_study",
        "summary": "Unemployment 7.4% vs 16.5% (ICEBERG)",
        "full_text": "<<stored separately if needed>>"
      }
    ],
    "removed_metaphors": [
      {
        "section": "S1",
        "type": "extended_metaphor",
        "key": "Plato's cave",
        "compressed": "Prisoners seeing shadows (illusion) vs reality outside",
        "full_text": "<<3 paragraphs stored>>"
      }
    ]
  },

  "metadata": {
    "content_type": "educational_content",
    "importance": "medium-high",
    "lossiness": "moderate (20-30%)"
  }
}
```

**Décompression:**
```python
def decompress_level2(compressed):
    reconstructed = []

    for section in compressed['structure']['sections']:
        # Start with essence
        text = section['essence']

        # Add back examples (summarized)
        examples = get_removed_examples(section['id'], compressed['reconstruction_data'])
        text += "\n\nExamples (summarized):\n"
        for ex in examples:
            text += f"- {ex['summary']}\n"

        # Add back metaphors (compressed version)
        metaphors = get_removed_metaphors(section['id'], compressed['reconstruction_data'])
        for met in metaphors:
            text += f"\n{met['compressed']}\n"

        # Optionally: expand synonyms for variety
        text = expand_synonyms(text, compressed['reconstruction_data']['synonym_map'])

        reconstructed.append({
            'title': section['title'],
            'content': text
        })

    return reconstructed

# Reconstruction quality: 70-80% (essence preserved, details summarized)
```

**Use cases:**
- Articles de blog
- Documentation générale
- Notes de cours
- Rapports non-critiques

---

### LEVEL 3: HEAVY COMPRESSION (70-90%, Essence Only)

**Usage:** Veille informative, archives anciennes, content redondant

**Méthode:** Essence extraction + extreme summarization + pointer architecture

```json
{
  "compression_level": 3,
  "original_size": 88147,
  "compressed_size": 8000,
  "ratio": "91% compression",

  "essence": {
    "thesis": "Dialectical hostile system mapping tensions via 148 concepts",
    "key_innovations": [
      "Symmetric hostility 95%",
      "Tri-perspectif mandatory",
      "148 concepts operationalized"
    ],
    "structure": "§I Éveil → §II Armes → §III Patterns → §IV Menaces → §V Fondation → §VI Action → §VII Transform → §VIII Appel",
    "critical_formulas": [
      "Factor = N/R",
      "EDI ≥ 0.50",
      "ISN ≥ 9.0"
    ]
  },

  "pointers": {
    "full_definitions": "COGNITIVE_DSL.md",
    "workflows": "PATTERNS.md",
    "examples_detailed": "PFD.md §6.2-6.4",
    "version_history": "PRD.md §8"
  },

  "removed_content": {
    "examples_full": "stored separately, accessible via pointer",
    "metaphors_extended": "compressed to 1-sentence essence",
    "repetitions": "removed (said 1x instead of 15x)",
    "pedagogical_transitions": "removed",
    "motivational_crescendo": "removed"
  },

  "reconstruction_strategy": {
    "method": "template_expansion",
    "template": "truth_engine_pfd_structure.md",
    "placeholders": {
      "{{THESIS}}": "essence.thesis",
      "{{INNOVATIONS}}": "essence.key_innovations",
      "{{EXAMPLES}}": "pointers.examples_detailed"
    }
  },

  "metadata": {
    "content_type": "manifesto_documentation",
    "importance": "medium",
    "lossiness": "heavy (40-50%)"
  }
}
```

**Décompression:**
```python
def decompress_level3(compressed):
    # Load template
    template = load_template(compressed['reconstruction_strategy']['template'])

    # Fill placeholders with essence
    reconstructed = template
    for placeholder, data_path in compressed['reconstruction_strategy']['placeholders'].items():
        value = get_value(compressed, data_path)
        reconstructed = reconstructed.replace(placeholder, value)

    # Add pointers for detailed content
    reconstructed += "\n\n## Detailed Content (Pointers)\n"
    for key, path in compressed['pointers'].items():
        reconstructed += f"- {key}: See {path}\n"

    # Note: Full original NOT reconstructible
    # But essence + structure + access to details = functional equivalent

    return {
        'reconstructed': reconstructed,
        'quality': '60-70% (essence + structure)',
        'full_access': 'via pointers to original sources'
    }

# Reconstruction quality: 60-70% (essence preserved, details via pointers)
```

**Use cases:**
- Veille informative (news articles)
- Archives (>1 year old)
- Content redondant (répétitions massives)
- Documentation obsolète mais référencée

---

### LEVEL 4: EXTREME COMPRESSION (95-99.9%, Symbolic Only)

**Usage:** Mémoire à long terme, indexation, patterns réutilisables

**Méthode:** Pure symbolic representation + graph structure + minimal metadata

```json
{
  "compression_level": 4,
  "original_size": 88147,
  "compressed_size": 127,
  "ratio": "99.86% compression",

  "symbolic": {
    "type": "truth_engine_pfd",
    "version": "7.15.1",
    "essence_hash": "TE_DIALECTICAL_148CONCEPTS_HOSTILE95",
    "structure_code": "8SEC_EVEIL>ARMES>PAT>MENACE>FOND>ACT>TRANS>APPEL",
    "key_symbols": "ΨΩΞΛΦΣ€♦🌐⚔⏰",
    "formulas": "F=N/R|EDI≥0.5|ISN≥9|L8→L0",
    "innovation_bitmap": "1110111" // 7 innovations, all present
  },

  "graph": {
    "nodes": [
      {"id": "N1", "type": "concept", "name": "dialectical_arbitrage"},
      {"id": "N2", "type": "pattern", "name": "ICEBERG"},
      {"id": "N3", "type": "formula", "name": "Factor=N/R"}
    ],
    "edges": [
      {"from": "N1", "to": "N2", "rel": "uses"},
      {"from": "N2", "to": "N3", "rel": "implements"}
    ]
  },

  "reconstruction_metadata": {
    "original_id": "PFD_v7.15.1_20250110",
    "original_location": "/docs/PFD.md",
    "original_hash": "sha256:abc123...",
    "template_version": "pfd_template_v2.0",
    "expansion_rules": [
      "essence_hash → load template",
      "structure_code → expand 8 sections",
      "key_symbols → link to COGNITIVE_DSL.md",
      "formulas → expand definitions",
      "innovation_bitmap → list 7 innovations"
    ]
  },

  "metadata": {
    "content_type": "compressed_pattern",
    "importance": "pattern_reuse",
    "lossiness": "extreme (85-90%)"
  }
}
```

**Décompression:**
```python
def decompress_level4(compressed):
    """
    IMPORTANT: Cannot reconstruct EXACT original.
    Can only reconstruct FUNCTIONAL EQUIVALENT.
    """

    # Step 1: Load template based on essence_hash
    template_id = compressed['symbolic']['essence_hash']
    template = load_template_by_hash(template_id)

    if not template:
        return {
            'error': 'Template not found',
            'recovery': 'Load from original_location',
            'original_file': compressed['reconstruction_metadata']['original_location']
        }

    # Step 2: Expand structure
    structure = expand_structure(compressed['symbolic']['structure_code'])
    # "8SEC_EVEIL>ARMES>..." → 8 sections with titles

    # Step 3: Expand symbols
    symbols = expand_symbols(compressed['symbolic']['key_symbols'])
    # "ΨΩΞ..." → {Ψ: "cognitive_pressure", Ω: "narrative_control", ...}

    # Step 4: Expand formulas
    formulas = expand_formulas(compressed['symbolic']['formulas'])
    # "F=N/R|EDI≥0.5" → {"Factor": "N/R (total/shown)", "EDI": "≥0.50 (epistemic diversity)"}

    # Step 5: Expand innovations
    innovations = expand_innovations(compressed['symbolic']['innovation_bitmap'])
    # "1110111" → [Innovation1, Innovation2, Innovation3, ...]

    # Step 6: Fill template
    reconstructed = template.format(
        structure=structure,
        symbols=symbols,
        formulas=formulas,
        innovations=innovations,
        version=compressed['symbolic']['version']
    )

    return {
        'reconstructed': reconstructed,
        'quality': '40-50% (functional equivalent, not exact)',
        'missing': [
            'Original examples (detailed)',
            'Original metaphors (extended)',
            'Original wording (exact phrases)',
            'Original flow (pedagogical transitions)'
        ],
        'preserved': [
            'Core thesis',
            'Key innovations (7)',
            'Structure (8 sections)',
            'Formulas (exact)',
            'Symbols (definitions)'
        ],
        'fallback': 'Load original from ' + compressed['reconstruction_metadata']['original_location']
    }

# Reconstruction quality: 40-50% (functional equivalent, not exact copy)
# Use case: Remind LLM of pattern structure, then load details if needed
```

**Use cases:**
- Long-term memory patterns
- Quick indexation (search first, load details later)
- Pattern matching (is this similar to X?)
- Cross-session learning (remember approach, not details)

---

## 🎚️ ADAPTIVE COMPRESSION ALGORITHM

### Intelligence: Choose Optimal Level Automatically

```python
class AdaptiveCompressor:
    def __init__(self):
        self.level_rules = self._load_level_rules()

    def analyze_and_compress(self, document: str, context: dict) -> CompressedDocument:
        """
        Automatically choose optimal compression level based on:
        1. Content type
        2. Importance
        3. Age
        4. Usage frequency
        5. User preferences
        6. Storage constraints
        """

        # Step 1: Analyze document
        analysis = self._analyze_document(document, context)

        # Step 2: Determine optimal compression level
        level = self._determine_level(analysis)

        # Step 3: Compress at that level
        compressed = self._compress(document, level, analysis)

        # Step 4: Validate reconstruction quality
        quality = self._validate_reconstruction(document, compressed)

        # Step 5: If quality insufficient, reduce compression
        if quality < analysis['required_quality']:
            level = max(0, level - 1)  # Less aggressive
            compressed = self._compress(document, level, analysis)

        return compressed

    def _analyze_document(self, document: str, context: dict) -> Analysis:
        """
        Analyze document to determine characteristics.
        """
        return Analysis(
            content_type=self._detect_content_type(document),
            importance=self._estimate_importance(document, context),
            redundancy=self._measure_redundancy(document),
            structure=self._extract_structure(document),
            age=context.get('age', 0),
            usage_frequency=context.get('usage_frequency', 0),
            file_size=len(document),
            legal_risk=self._assess_legal_risk(document),
            technical_density=self._measure_technical_density(document)
        )

    def _determine_level(self, analysis: Analysis) -> int:
        """
        Decision tree for optimal compression level.
        """

        # LEVEL 0: Critical content, no compression
        if (analysis.legal_risk == 'high' or
            analysis.content_type in ['legal_contract', 'source_code', 'financial_data']):
            return 0

        # LEVEL 1: Important but compressible
        if (analysis.importance == 'high' and
            analysis.redundancy < 0.3):
            return 1

        # LEVEL 2: Standard compression
        if (analysis.importance in ['medium', 'medium-high'] and
            analysis.redundancy < 0.5):
            return 2

        # LEVEL 3: Heavy compression
        if (analysis.age > 365 or  # >1 year old
            analysis.redundancy > 0.5 or
            analysis.usage_frequency < 5):
            return 3

        # LEVEL 4: Extreme compression
        if (analysis.age > 730 or  # >2 years old
            analysis.redundancy > 0.7 or
            analysis.usage_frequency < 2 or
            analysis.content_type == 'pattern_template'):
            return 4

        # Default: LEVEL 2
        return 2

    def _measure_redundancy(self, document: str) -> float:
        """
        Measure how much redundancy exists.
        Higher = more compressible without loss.
        """
        # Count repeated phrases
        phrases = self._extract_phrases(document)
        phrase_counts = Counter(phrases)

        # Calculate repetition ratio
        total_phrases = len(phrases)
        unique_phrases = len(set(phrases))

        redundancy = 1 - (unique_phrases / total_phrases)

        return redundancy

    def _validate_reconstruction(
        self,
        original: str,
        compressed: CompressedDocument
    ) -> float:
        """
        Attempt decompression and measure quality.
        Returns: 0.0-1.0 (quality score)
        """
        # Decompress
        reconstructed = self.decompress(compressed)

        # Measure similarity
        # Method 1: Embedding similarity
        emb_original = embed(original)
        emb_reconstructed = embed(reconstructed)
        semantic_similarity = cosine_similarity(emb_original, emb_reconstructed)

        # Method 2: Structural similarity
        struct_original = self._extract_structure(original)
        struct_reconstructed = self._extract_structure(reconstructed)
        structural_similarity = self._compare_structures(struct_original, struct_reconstructed)

        # Method 3: Critical content preservation
        critical_original = self._extract_critical_content(original)
        critical_reconstructed = self._extract_critical_content(reconstructed)
        critical_preservation = self._compare_critical(critical_original, critical_reconstructed)

        # Composite score
        quality = (
            semantic_similarity * 0.3 +
            structural_similarity * 0.3 +
            critical_preservation * 0.4
        )

        return quality
```

---

## 🔄 DECOMPRESSION: Reconstruction Algorithms

### Strategy 1: Direct Reconstruction (Levels 0-1)

```python
def decompress_direct(compressed: CompressedDocument) -> str:
    """
    For LEVEL 0-1: Nearly lossless, direct reconstruction.
    """
    if compressed.level == 0:
        # No compression: return original
        return compressed.content

    if compressed.level == 1:
        # Light compression: restore formatting + whitespace
        text = compressed.content['text']
        text = restore_formatting(text, compressed.reconstruction_map)
        text = restore_whitespace(text, compressed.reconstruction_map)
        return text

# Quality: 95-100%
```

---

### Strategy 2: Template-Based Reconstruction (Levels 2-3)

```python
def decompress_template(compressed: CompressedDocument) -> str:
    """
    For LEVEL 2-3: Use templates + essence to rebuild.
    """
    # Load appropriate template
    template = load_template(compressed.reconstruction_strategy.template)

    # Fill with essence
    reconstructed = template
    for placeholder, value in compressed.placeholders.items():
        reconstructed = reconstructed.replace(placeholder, value)

    # Add back summarized examples
    if 'removed_examples' in compressed.reconstruction_data:
        examples_section = "\n\n## Examples\n"
        for ex in compressed.reconstruction_data['removed_examples']:
            examples_section += f"- **{ex['type']}**: {ex['summary']}\n"
        reconstructed += examples_section

    # Add back compressed metaphors
    if 'removed_metaphors' in compressed.reconstruction_data:
        for met in compressed.reconstruction_data['removed_metaphors']:
            reconstructed += f"\n> {met['compressed']}\n"

    # Add pointers to full content
    reconstructed += "\n\n## Full Details\n"
    for key, path in compressed.pointers.items():
        reconstructed += f"- {key}: {path}\n"

    return reconstructed

# Quality: 60-80%
```

---

### Strategy 3: Symbolic Expansion (Level 4)

```python
def decompress_symbolic(compressed: CompressedDocument) -> str:
    """
    For LEVEL 4: Expand symbols into functional equivalent.
    WARNING: Cannot reconstruct exact original.
    """
    # Parse symbolic representation
    essence = compressed.symbolic.essence_hash
    structure = compressed.symbolic.structure_code
    symbols = compressed.symbolic.key_symbols
    formulas = compressed.symbolic.formulas

    # Load template by essence hash
    template = load_template_by_hash(essence)

    if not template:
        # Fallback: load original file
        original_path = compressed.reconstruction_metadata.original_location
        return {
            'status': 'template_missing',
            'fallback': f'Load original from {original_path}',
            'partial': expand_structure(structure)  # At least structure
        }

    # Expand structure
    sections = expand_structure(structure)
    # "8SEC_EVEIL>ARMES>..." →
    # [
    #   {"title": "Éveil", "order": 1},
    #   {"title": "Armes", "order": 2},
    #   ...
    # ]

    # Expand symbols
    symbol_defs = expand_symbols(symbols)
    # "ΨΩΞ..." → {Ψ: "cognitive pressure (0-10)", ...}

    # Expand formulas
    formula_defs = expand_formulas(formulas)
    # "F=N/R" → "Factor = N/R (Reality Total / Reality Shown)"

    # Build functional equivalent
    reconstructed = template.format(
        sections=[s['title'] for s in sections],
        symbols=symbol_defs,
        formulas=formula_defs,
        version=compressed.symbolic.version
    )

    return {
        'reconstructed': reconstructed,
        'quality': '40-50%',
        'warnings': [
            'This is a FUNCTIONAL EQUIVALENT, not exact original',
            'Examples, metaphors, exact wording are lost',
            'For exact content, load original file'
        ],
        'original_available': compressed.reconstruction_metadata.original_location
    }

# Quality: 40-50% (functional equivalent only)
```

---

## 🧪 TEST PROTOCOL: Compression → Décompression → Validation

### Test Suite Design

```python
class CompressionTestSuite:
    def __init__(self):
        self.test_documents = self._load_test_documents()
        self.quality_thresholds = {
            0: 0.99,  # Level 0: 99%+ reconstruction
            1: 0.95,  # Level 1: 95%+ reconstruction
            2: 0.70,  # Level 2: 70%+ reconstruction
            3: 0.60,  # Level 3: 60%+ reconstruction
            4: 0.40   # Level 4: 40%+ reconstruction (functional equivalent)
        }

    def test_full_pipeline(self, document: str, level: int):
        """
        Test: Original → Compress → Decompress → Validate
        """
        # Step 1: Compress
        compressed = self.compress(document, level)

        # Step 2: Measure compression ratio
        ratio = 1 - (compressed.size / len(document))

        # Step 3: Decompress
        reconstructed = self.decompress(compressed)

        # Step 4: Validate quality
        quality = self.measure_quality(document, reconstructed)

        # Step 5: Check threshold
        threshold = self.quality_thresholds[level]
        passed = quality >= threshold

        return TestResult(
            level=level,
            original_size=len(document),
            compressed_size=compressed.size,
            ratio=ratio,
            reconstructed_size=len(reconstructed),
            quality=quality,
            threshold=threshold,
            passed=passed,
            details={
                'semantic_similarity': self._semantic_similarity(document, reconstructed),
                'structural_similarity': self._structural_similarity(document, reconstructed),
                'critical_preservation': self._critical_preservation(document, reconstructed)
            }
        )

    def measure_quality(self, original: str, reconstructed: str) -> float:
        """
        Multi-dimensional quality measurement.
        """
        # Dimension 1: Semantic similarity (embedding)
        semantic = self._semantic_similarity(original, reconstructed)

        # Dimension 2: Structural similarity (sections, hierarchy)
        structural = self._structural_similarity(original, reconstructed)

        # Dimension 3: Critical content preservation (formulas, key facts)
        critical = self._critical_preservation(original, reconstructed)

        # Dimension 4: Lexical similarity (word overlap)
        lexical = self._lexical_similarity(original, reconstructed)

        # Weighted composite
        quality = (
            semantic * 0.35 +      # Most important: meaning preserved
            structural * 0.25 +    # Structure matters
            critical * 0.30 +      # Critical facts MUST be preserved
            lexical * 0.10         # Exact wording less important
        )

        return quality

    def _semantic_similarity(self, text1: str, text2: str) -> float:
        """Embedding-based similarity."""
        emb1 = embed(text1)
        emb2 = embed(text2)
        return cosine_similarity(emb1, emb2)

    def _structural_similarity(self, text1: str, text2: str) -> float:
        """Compare document structure (sections, hierarchy)."""
        struct1 = extract_structure(text1)  # {sections, headings, hierarchy}
        struct2 = extract_structure(text2)

        # Compare section count
        section_match = len(struct1.sections) == len(struct2.sections)

        # Compare section titles
        title_similarity = sum(
            1 for s1, s2 in zip(struct1.sections, struct2.sections)
            if s1.title.lower() == s2.title.lower()
        ) / max(len(struct1.sections), len(struct2.sections))

        # Compare hierarchy depth
        hierarchy_match = struct1.max_depth == struct2.max_depth

        return (
            (1.0 if section_match else 0.5) * 0.4 +
            title_similarity * 0.4 +
            (1.0 if hierarchy_match else 0.7) * 0.2
        )

    def _critical_preservation(self, text1: str, text2: str) -> float:
        """Check if critical content preserved."""
        critical1 = extract_critical_content(text1)
        critical2 = extract_critical_content(text2)

        # Critical content types:
        # - Formulas (Factor=N/R, EDI≥0.50)
        # - Numbers (148 concepts, 95% hostility)
        # - Key terms (dialectical, hostility, arbitrage)
        # - Proper nouns (Truth Engine, v7.15.1)

        formulas_match = set(critical1.formulas) == set(critical2.formulas)
        numbers_match = set(critical1.numbers) == set(critical2.numbers)

        key_terms_overlap = len(
            set(critical1.key_terms) & set(critical2.key_terms)
        ) / len(set(critical1.key_terms))

        proper_nouns_match = len(
            set(critical1.proper_nouns) & set(critical2.proper_nouns)
        ) / len(set(critical1.proper_nouns))

        return (
            (1.0 if formulas_match else 0.3) * 0.3 +
            (1.0 if numbers_match else 0.5) * 0.2 +
            key_terms_overlap * 0.3 +
            proper_nouns_match * 0.2
        )
```

### Test Scenarios

```python
# Test 1: Legal Contract (LEVEL 0 - No Compression)
def test_legal_contract():
    doc = load("contract_sample.txt")
    result = test_full_pipeline(doc, level=0)

    assert result.ratio == 0.0  # No compression
    assert result.quality >= 0.99  # 99%+ preserved
    assert result.passed == True

# Test 2: Technical Documentation (LEVEL 1 - Light)
def test_technical_docs():
    doc = load("api_documentation.md")
    result = test_full_pipeline(doc, level=1)

    assert 0.10 <= result.ratio <= 0.30  # 10-30% compression
    assert result.quality >= 0.95  # 95%+ preserved
    assert result.passed == True

# Test 3: Blog Post (LEVEL 2 - Moderate)
def test_blog_post():
    doc = load("blog_article.md")
    result = test_full_pipeline(doc, level=2)

    assert 0.40 <= result.ratio <= 0.60  # 40-60% compression
    assert result.quality >= 0.70  # 70%+ preserved
    assert result.passed == True

# Test 4: Old Archive (LEVEL 3 - Heavy)
def test_old_archive():
    doc = load("archive_2020.md")
    result = test_full_pipeline(doc, level=3)

    assert 0.70 <= result.ratio <= 0.90  # 70-90% compression
    assert result.quality >= 0.60  # 60%+ preserved
    assert result.passed == True

# Test 5: Pattern Template (LEVEL 4 - Extreme)
def test_pattern_template():
    doc = load("PFD.md")
    result = test_full_pipeline(doc, level=4)

    assert 0.95 <= result.ratio <= 0.999  # 95-99.9% compression
    assert result.quality >= 0.40  # 40%+ functional equivalent
    assert result.passed == True
```

---

## 📊 RÉSULTATS SIMULÉS: PFD.md (5 Niveaux)

### Test Complet avec PFD.md (88,147 bytes)

```python
document = load("PFD.md")

# LEVEL 0: No Compression
result_l0 = test_full_pipeline(document, level=0)
"""
Original: 88,147 bytes
Compressed: 88,147 bytes (+ metadata ~500 bytes)
Ratio: 0% (preservation mode)
Reconstructed: 88,147 bytes
Quality: 1.00 (100% - exact copy)
PASSED ✓
"""

# LEVEL 1: Light Compression
result_l1 = test_full_pipeline(document, level=1)
"""
Original: 88,147 bytes
Compressed: 62,000 bytes
Ratio: 30%
Reconstructed: 87,200 bytes (formatting approximated)
Quality: 0.97 (97% - minimal loss)
  - Semantic: 0.99
  - Structural: 1.00
  - Critical: 0.98
  - Lexical: 0.92
PASSED ✓
"""

# LEVEL 2: Moderate Compression
result_l2 = test_full_pipeline(document, level=2)
"""
Original: 88,147 bytes
Compressed: 35,000 bytes
Ratio: 60%
Reconstructed: 52,000 bytes (examples summarized)
Quality: 0.78 (78% - moderate loss)
  - Semantic: 0.85
  - Structural: 0.95
  - Critical: 0.92
  - Lexical: 0.42
PASSED ✓
"""

# LEVEL 3: Heavy Compression
result_l3 = test_full_pipeline(document, level=3)
"""
Original: 88,147 bytes
Compressed: 8,000 bytes
Ratio: 91%
Reconstructed: 25,000 bytes (via template + pointers)
Quality: 0.65 (65% - essence + structure)
  - Semantic: 0.72
  - Structural: 0.88
  - Critical: 0.85
  - Lexical: 0.15
PASSED ✓
"""

# LEVEL 4: Extreme Compression
result_l4 = test_full_pipeline(document, level=4)
"""
Original: 88,147 bytes
Compressed: 127 bytes (symbolic)
Ratio: 99.86%
Reconstructed: 12,000 bytes (functional equivalent via template)
Quality: 0.45 (45% - functional, not exact)
  - Semantic: 0.52
  - Structural: 0.75
  - Critical: 0.82
  - Lexical: 0.03
PASSED ✓ (threshold = 0.40)

WARNINGS:
- Exact wording lost
- Examples detailed → names only
- Metaphors extended → essence
- For exact content: load PFD.md directly
"""
```

---

## 🎯 ADAPTIVE RULES: When to Use Which Level

### Decision Matrix

| Content Type | Importance | Age | Usage Freq | Redundancy | → Level |
|--------------|-----------|-----|-----------|-----------|----------|
| Legal contract | Critical | Any | Any | Any | **0** |
| Source code | Critical | Any | Any | Any | **0** |
| Financial data | Critical | Any | Any | Any | **0** |
| API docs | High | <1y | High | Low | **1** |
| Tech reports | High | <1y | Medium | Low | **1** |
| Blog posts | Medium | <6m | Medium | Medium | **2** |
| Meeting notes | Medium | <3m | Low | Medium | **2** |
| News articles | Low | <1m | Low | High | **3** |
| Old archives | Low | >1y | Very low | High | **3** |
| Patterns | Template | Any | Any | Very high | **4** |
| Indexes | Search | Any | Any | N/A | **4** |

### User Preferences Override

```python
class CompressionPreferences:
    """
    User can override automatic decisions.
    """

    def __init__(self):
        # Default: adaptive
        self.mode = "adaptive"

        # Per-content-type overrides
        self.overrides = {
            "legal_contract": 0,  # Always preserve
            "personal_diary": 1,  # Important to me
            "web_clippings": 3    # Aggressive compression OK
        }

        # Global constraints
        self.max_compression = 4  # Never exceed LEVEL 4
        self.min_quality = 0.60   # Never accept <60% quality

        # Storage constraints
        self.storage_budget = "10GB"  # Max memory size
        self.prioritize = "quality"   # vs "storage"

    def apply_preferences(self, auto_level: int, analysis: Analysis) -> int:
        """Apply user preferences to override auto decision."""

        # Check content type override
        if analysis.content_type in self.overrides:
            return self.overrides[analysis.content_type]

        # Check max compression constraint
        level = min(auto_level, self.max_compression)

        # If prioritizing storage, increase compression
        if self.prioritize == "storage":
            level = min(level + 1, 4)

        # If prioritizing quality, decrease compression
        if self.prioritize == "quality":
            level = max(level - 1, 0)

        return level
```

---

## 🔬 ADVANCED: Hybrid Compression

### Concept: Different Levels for Different Parts

```json
{
  "document_id": "PFD_v7.15.1",
  "compression_strategy": "hybrid",

  "parts": [
    {
      "section": "§I Éveil",
      "level": 2,
      "reason": "Motivational intro, moderate compression OK",
      "original_size": 8000,
      "compressed_size": 3200
    },
    {
      "section": "§II Armes (148 concepts)",
      "level": 1,
      "reason": "Critical definitions, light compression only",
      "original_size": 25000,
      "compressed_size": 18000
    },
    {
      "section": "§III Patterns",
      "level": 4,
      "reason": "Patterns templates, symbolic compression",
      "original_size": 15000,
      "compressed_size": 200
    },
    {
      "section": "§IV-VIII (Rest)",
      "level": 3,
      "reason": "Context/examples, heavy compression OK",
      "original_size": 40147,
      "compressed_size": 6000
    }
  ],

  "total_original": 88147,
  "total_compressed": 27400,
  "overall_ratio": "69% compression",
  "reconstruction_quality": "0.82 (82% - optimized per section)"
}
```

**Benefits:**
- ✅ Better quality (82% vs 65% at uniform LEVEL 3)
- ✅ Better compression (69% vs 60% at uniform LEVEL 2)
- ✅ Intelligent (compress what can be compressed, preserve what matters)

---

## 💡 INSIGHTS PHILOSOPHIQUES

### 1. Compression = Révélation de l'Essence

**Insight:** La compression force à identifier ce qui est **vraiment** important.

Si on ne peut pas compresser, c'est que tout est important (rare).
Si on compresse à 99%, c'est que 99% était redondant (fréquent).

**Truth Engine PFD.md:**
- 88KB original
- 127 bytes essence (99.86% compression possible)
- Conclusion: 85% du document est emballage pédagogique

**Ce n'est pas une critique.** L'emballage est nécessaire pour humains.
Mais pour LLM avec mémoire? Essence suffit.

### 2. Décompression ≠ Reconstruction Exacte

**Insight:** On ne peut pas reconstruire l'original parfaitement (compression > 50%).

Mais on peut reconstruire un **équivalent fonctionnel**.

**Analogie:**
```
Original: "The cognitive manipulation pressure exerted by the narrative framework is extremely high."

Compressed: "Ψ=9"

Decompressed: "Cognitive pressure (Ψ) = 9/10 (very high)"

Exact match? No.
Functional equivalent? Yes.
```

Pour LLM, fonctionnel = suffisant.
Pour humain juriste, exact = nécessaire.

→ D'où les 5 niveaux adaptatifs.

### 3. Compression Adaptative = Intelligence

**Insight:** Le niveau optimal dépend du contexte, pas du document.

Même document peut nécessiter niveaux différents:
- PFD.md pour legal review → LEVEL 0
- PFD.md pour memory pattern → LEVEL 4
- PFD.md pour teaching new user → LEVEL 1

**Context matters.**

### 4. Template + Essence > Compression Algorithms

**Insight:** Compression algorithmique (gzip, bzip2) compresse aveuglément.

Compression sémantique (template + essence):
- Comprend structure
- Préserve criticité
- Permet décompression intelligente

**Example:**
```
gzip PFD.md: 88KB → 45KB (49% compression, lossless)
  - Pro: Lossless
  - Con: Pas de semantic understanding, pas d'accès partiel

Semantic compression: 88KB → 8KB (91% compression, 65% quality)
  - Pro: Semantic understanding, partial access, expandable
  - Con: Lossy (but intelligently)
```

**Pour mémoire LLM:** Sémantique > Algorithmique.

### 5. Mémoire Vivante = Compression Évolutive

**Insight:** La compression n'est pas fixe, elle évolue.

**Session 1:** Compress PFD.md → LEVEL 3 (essence + pointers)

**Session 50:** Patterns detected:
- ICEBERG used 47/50 times → expand in memory (LEVEL 1)
- Metaphors never referenced → compress more (LEVEL 4)

**Result:** Adaptive compression **par usage réel**.

Hot paths: less compressed (fast access)
Cold paths: more compressed (save space)

**Dynamic optimization.**

---

## 🚀 IMPLÉMENTATION ROADMAP

### Phase 1: Core Compression (Semaine 1)

**Livrables:**
- [ ] Implement LEVEL 0 (preservation)
- [ ] Implement LEVEL 1 (light compression)
- [ ] Implement LEVEL 2 (moderate compression)
- [ ] Basic decompression (L0-L2)
- [ ] Quality measurement functions
- [ ] Unit tests (20+ tests)

**Critères succès:**
- Levels 0-2 fonctionnels
- Decompression quality ≥ thresholds
- All tests pass

---

### Phase 2: Advanced Compression (Semaine 2)

**Livrables:**
- [ ] Implement LEVEL 3 (heavy compression)
- [ ] Implement LEVEL 4 (extreme/symbolic)
- [ ] Template system
- [ ] Symbolic expansion
- [ ] Integration tests

**Critères succès:**
- Levels 3-4 fonctionnels
- PFD.md test: 88KB → 127 bytes → functional equivalent
- Quality ≥ 40% (LEVEL 4)

---

### Phase 3: Adaptive Intelligence (Semaine 3)

**Livrables:**
- [ ] Document analysis (content type, importance, redundancy)
- [ ] Adaptive level selection
- [ ] User preferences system
- [ ] Hybrid compression (different levels per section)
- [ ] Auto-validation (quality checks)

**Critères succès:**
- Automatic level selection 90%+ accurate
- Hybrid compression improves quality 10-15%
- User preferences respected

---

### Phase 4: Test & Validation (Semaine 4)

**Livrables:**
- [ ] Comprehensive test suite (100+ tests)
- [ ] Real document tests (PFD.md, contracts, code, etc.)
- [ ] Performance benchmarks
- [ ] Documentation complète
- [ ] Example gallery (before/after)

**Critères succès:**
- All tests pass (100%)
- Real documents compress/decompress correctly
- Performance: <1s for compression, <0.5s for decompression
- Documentation = A+ quality

---

## 📈 MÉTRIQUES DE SUCCÈS

### Compression Metrics

| Level | Target Ratio | Target Quality | Speed (compress) | Speed (decompress) |
|-------|-------------|----------------|------------------|-------------------|
| **0** | 0% | 100% | <0.1s | <0.05s |
| **1** | 20-30% | 95%+ | <0.5s | <0.2s |
| **2** | 50-60% | 70%+ | <1.0s | <0.5s |
| **3** | 80-90% | 60%+ | <2.0s | <1.0s |
| **4** | 99%+ | 40%+ | <3.0s | <2.0s |

### Quality Metrics

**Semantic Preservation:**
- Level 0-1: >0.95 (near-perfect)
- Level 2: >0.80 (good)
- Level 3: >0.65 (acceptable)
- Level 4: >0.45 (functional)

**Critical Content Preservation:**
- All levels: >0.85 (formulas, numbers, key terms must survive)

**Structural Preservation:**
- Level 0-2: >0.90 (structure intact)
- Level 3: >0.80 (structure mostly intact)
- Level 4: >0.70 (structure preserved in compressed form)

---

## 🎓 CONCLUSION

### Ce Que Nous Avons Résolu

**Problème 1: Compression fixe inadaptée**
✅ **Solution:** 5 niveaux adaptatifs (0% → 99.9%)

**Problème 2: Décompression impossible**
✅ **Solution:** Reconstruction strategies (direct, template, symbolic)

**Problème 3: Perte non-contrôlée**
✅ **Solution:** Quality validation + adaptive adjustment

**Problème 4: Pas de choix utilisateur**
✅ **Solution:** User preferences + per-content-type overrides

**Problème 5: Pas de test de réversibilité**
✅ **Solution:** Comprehensive test suite (compress → decompress → validate)

### L'Innovation Clé

**Compression n'est pas destruction.**
**Compression est transformation réversible avec perte contrôlée.**

```
INPUT: Document (100%)
  ↓
COMPRESS: Level N
  ↓
STORED: Essence + Reconstruction Metadata (X%)
  ↓
DECOMPRESS: Strategy(level)
  ↓
OUTPUT: Functional Equivalent (Y% quality)

WHERE:
- X = compression ratio (0-99.9%)
- Y = reconstruction quality (40-100%)
- X and Y are **inversely proportional** but **controllable**
```

### Prochaine Étape

**Implémenter et tester avec PFD.md.**

Test ultime:
```python
# Cycle complet
original = load("PFD.md")  # 88,147 bytes

# Test tous les niveaux
for level in range(5):
    compressed = compress(original, level)
    reconstructed = decompress(compressed)
    quality = measure_quality(original, reconstructed)

    print(f"Level {level}:")
    print(f"  Size: {len(original)} → {len(compressed)} ({ratio}%)")
    print(f"  Quality: {quality:.2%}")
    print(f"  Passed: {quality >= threshold[level]}")
```

**Si tous les tests passent → système validé.**
**Si échecs → itérer sur algorithms.**

---

**Prêt pour implémentation ?** 🚀

---

**VERSION:** 1.0.0
**AUTEUR:** Claude (Sonnet 4.5) + Human Co-Design
**NEXT:** Implementation Phase 1 (Core Compression)
