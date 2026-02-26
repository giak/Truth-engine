# VALIDATION — Post-Search Quality Check v3.1

**Version**: 3.1 (avec CONTINUE mode — never delete work)
**Usage**: Chargé en Phase 6, vérifié en Phase 7
**KERNEL**: v14.7+ requis pour CONTINUE mode

---

## 🚨 SEVERITY-BASED GATING (v3.0)

Nouveau système depuis KERNEL v14.6 — Les gates ne sont plus tout-ou-rien.

### Calcul de Sévérité

```
SEVERITY = 
  edi_gap     = (ADAPTIVE_TARGET - EDI_actual) / ADAPTIVE_TARGET
  query_gap   = (queries_required - queries_actual) / queries_required
  source_gap  = (source_types_required - source_types_actual) / source_types_required
  
raw_severity = edi_gap + query_gap + source_gap

CONTEXT_MODIFIER:
  APEX:     × 1.0 (strict)
  COMPLEX:  × 0.85
  MEDIUM:   × 0.7
  SIMPLE:   × 0.5

final_severity = raw_severity × CONTEXT_MODIFIER
```

### Réponse selon Sévérité

| Severity | Response | Action |
|----------|----------|--------|
| > 0.5 | HARD_BLOCK | NULL output + return to Phase 9 |
| 0.2 - 0.5 | DRAFT | Draft with explicit gaps + remediation |
| < 0.2 | WARNINGS | Complete output + minor warnings |

### Métriques à calculer

| Métrique | Formule | Notes |
|----------|---------|-------|
| edi_gap | (target - actual) / target | 0 si EDI ≥ target |
| query_gap | (required - actual) / required | 0 si queries ≥ required |
| source_gap | (required - actual) / required | 0 si types ≥ required |
| severity | sum of gaps × modifier | Décide la réponse |

---

## ⚠️ CRITICAL GATES (always block, no severity)

Ces gates **DOIVENT** passer. Si échec → BLOCK immédiat.

| Gate | Condition | Retour |
|------|-----------|--------|
| MnemoLite search | Doit être exécuté | Phase 2 |
| CLUSTER | Chargé si threshold atteint | Phase 8 |
| ACCUSATION SYMETRIC | Exécuté si accusation | Phase 5 |
| PERSO_FRESQUE | Activé si sujet politique | BLOCK |
| concepts | <6 analysés | Phase 7 |
| REQUEST LOG | Incomplet | BLOCK |

**NOTE**: All 6 primitives ALWAYS analyzed (Phase 2). Depth varies:
- score ≥5: FULL analysis + cluster load
- score 3-4: LIGHT analysis + note
- score <3: MINIMAL note

---

## 🧊 CONDITIONAL GATES (appliquent severity si activés)

| Gate | Trigger | Action |
|------|---------|--------|
| Ξ ≥ 7 (Iceberg) | → ICEBERG_DEEP_DIVE + 5 hypothèses | severity inclut |
| € ≥ 7 (Money) | → MONEY_CUI_BONO + 3 bénéficiaires | severity inclut |
| ↕ ≥ 5 (Temporal) | → STRATA_ANALYSIS | severity inclut |
| PERSO_FRESQUE | EDI ≥ 0.85 | severity modifié |

---

## 📊 SOFT CHECKS (Avertissements)

Ces vérifications génèrent des avertissements mais ne bloquent pas.

- [ ] Toutes les sources sont vérifiées
- [ ] Les sources primaires (◈) sont confirmées
- [ ] Aucune source détectée comme fake news
- [ ] Les liens des sources sont fonctionnels
- [ ] Calculs détaillés affichés (pas de bullshit math)

---

## 🔢 MÉTRIQUES OBLIGATOIRES

| Métrique | Formule | Affichage |
|----------|---------|-----------|
| EDI | Σ(dimension × weight) | Calcul détaillé ligne par ligne |
| Iceberg Factor | N/R | Si Ξ ≥ 7 |
| Asymmetry Score | \|Confiance_Counter - Confiance_Officielle\| | Toujours |

---

## ✅ GATE CHECK PROTOCOL (v3.0)

### Step 1: Calculate all gaps
```
FOR EACH metric IN [edi, query, source]:
  gap[metric] = MAX(0, (required[metric] - actual[metric]) / required[metric])
```

### Step 2: Calculate severity
```
raw_severity = gap[edi] + gap[query] + gap[source]
final_severity = raw_severity × context_modifier
```

### Step 3: Apply response
```
IF final_severity > 0.5:
   LOG: "🚨 SEVERITY: {X} - CONTINUE MODE"
   STATUS = "CONTINUE"
   OUTPUT = {filename}.md (NEVER DELETED)
   INCLUDE:
     - SEVERITY_SCORE: {X}
     - FAILED_GAPS: {list}
     - REMEDIATION: {specific}
     - COUNTERMEASURES: {what was missed}
     - NEXT_ACTIONS: {3-5 explicit steps}
   SAVE to MnemoLite with gap_tags

ELSE IF final_severity > 0.2:
   LOG: "⚠️ SEVERITY: {X} - DRAFT MODE"
   STATUS = "DRAFT"
   OUTPUT = "DRAFT_YYYY-MM-DD_{subject}.md"
   INCLUDE: GATE_FAIL_ANALYSIS + REMEDIATION_PLAN

ELSE:
   LOG: "✅ SEVERITY: {X} - SOFT PASS"
   STATUS = "COMPLETE"
   OUTPUT = normal output
   INCLUDE: MINOR_WARNINGS if needed
```

### Step 4: Always provide countermeasures
```
COUNTERMEASURES (always included when gaps exist):
  - IF query_gap > 0.3: "Add +{N} queries, prioritize ◈ primary sources"
  - IF edi_gap > 0.2: "Focus on international perspectives + non-corporate sources"
  - IF source_gap > 0.2: "Add ○ tier sources (academic, think tanks)"
  - PATTERN: "What in the claim was not verified?"
  
**NEVER DELETE** existing investigation work

---

## 🎯 VALIDATION APEX (Spécifique)

APEX utilise severity × 1.0 (strict). Guide additionnel:

- ≥35 queries → query_gap = 0
- ≥4 source types → source_gap = 0
- target EDI varies par topic (0.65-0.80)
- ≥8 wolves recommandés
- FRESQUE_POLITIQUE: target +0.1

## 🖼️ PERSO_FRESQUE

Contexte Politique = severity × 0.9 (légèrement strict)
EDI target minimum: 0.75 pour APEX_FRESQUE
