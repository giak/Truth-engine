# VALIDATION — Post-Search Quality Check v2.0

**Version**: 2.0 (avec gates bloquantes)
**Usage**: Chargé en Phase 6, vérifié en Phase 7

---

## 🚨 HARD GATES (Bloquantes)

Ces gates **DOIVENT** passer. Si échec → output bloqué, retour à la phase indiquée.

| Gate | Condition | Minimum | Retour si échec |
|------|-----------|---------|-----------------|
| `source_types` | Types de sources utilisés | ≥4 | Phase 4 |
| `concepts_analyzed` | Concepts with score ≥5, analyzed in depth | ≥5 (MEDIUM), ≥8 (APEX) | Phase 3 |
| `wolves_named` | Acteurs nommés individuellement | ≥3 (MEDIUM), ≥8 (APEX) | Phase 4 |
| `edi_target` | EDI atteint la cible | ≥0.50 (MEDIUM), ≥0.80 (APEX) | Phase 4 |
| `dialectic_complete` | Thèse/Antithèse/Tensions | TRUE | Phase 3 |

**NOTE**: ~40-65 concepts = total activated (all scores). ≥5/≥8 = threshold-gated for in-depth analysis.

---

## 🧊 CONDITIONAL GATES (Si pattern activé)

| Gate | Condition | Trigger | Minimum |
|------|-----------|---------|---------|
| `iceberg_hypotheses` | Hypothèses générées | Ξ ≥ 7 | 5 |
| `iceberg_shadow_calc` | Shadow multiplier calculé | Ξ ≥ 7 | Oui |
| `money_cui_bono` | Bénéficiaires identifiés | € ≥ 7 | 3 |
| `strata_vertical` | Analyse Top/Bottom | ↕ ≥ 5 | Oui |
| `edi_fresque` | EDI élevé pour profondeur historique | PERSO_FRESQUE activé | ≥ 0.85 |

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

## ✅ GATE CHECK PROTOCOL

```
FOR EACH gate IN hard_gates:
  IF gate.actual < gate.minimum:
    LOG: "❌ GATE FAIL: {gate.name}"
    LOG: "   Required: {gate.minimum}, Actual: {gate.actual}"
    LOG: "   Action: Return to Phase {gate.return_phase}"
    BLOCK_OUTPUT: TRUE
    RETURN TO: gate.return_phase

IF all gates PASS:
  LOG: "✅ ALL GATES PASSED"
  CONTINUE TO: Output
```

---

## 🎯 VALIDATION APEX (Spécifique)

Pour les investigations de type APEX, vérifications additionnelles :

- [ ] ≥35 queries exécutées
- [ ] 35% des queries sont primaires (◈)
- [ ] 10% des queries ciblent des acteurs nommés (WOLF)
- [ ] EDI ≥ 0.80
- [ ] ≥8 acteurs nommés (WOLF)
- [ ] ≥5 branches explorées
- [ ] Fresque Politique incluse (si sujet politique)
- [ ] ICEBERG_DEEP_DIVE section remplie (si Ξ ≥ 7)

## 🖼️ VALIDATION PERSO_FRESQUE (Spécifique)

Si mode `PERSO_FRESQUE` activé, gate supplémentaire bloquante :

| Gate | Condition | Minimum | Retour si échec |
|------|-----------|---------|-----------------|
| `edi_fresque` | EDI atteint cible fresque | ≥ 0.85 | Phase 4 |

```
IF PERSO_FRESQUE AND edi_fresque < 0.85:
  LOG: "❌ GATE FAIL: edi_fresque"
  LOG: "   Required: 0.85 (PERSO_FRESQUE), Actual: {edi}"
  LOG: "   Action: Return to Phase 4 — diversifier sources temporelles"
  BLOCK_OUTPUT: TRUE
```
