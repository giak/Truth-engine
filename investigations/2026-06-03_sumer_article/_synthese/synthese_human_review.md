# Synthese — Revue humaine

**Date :** 2026-06-06 | **Pilote :** 10 quintessences Sumer
**Sujet principal :** Comparaison France moderne vs 10 civilisations antiques (dette, bureaucratie, droit, monnaie, religion, transmission, capture)
**Convergence :** 90% (9/10 fiches traitent ce sujet) | **HUB = audit des sources de ce sujet**
**Shadow_factor_agregé :** 3.85x (median) | **Complexity :** APEX
**Stats :** 12 transversalités (cible 7+, +71%) | 5 thèses | 5 méta-obs | **53 F### uniques cités (cible 50+)** | 101 F###-slots totaux

---

## Top 3 transversalites

1. **TR-001 — Dette comme outil politique** (5/10 fiches) : andurarum, nexum, monopole sel, riba, rituel
2. **TR-003 — Capture universelle, mecanismes variables** (5/10) : caste, quipu, enarques, etat
3. **TR-002 — Transmission multi-lineaire** (4/10) : CJC direct, Bologne, Cordoue, Jesuites
4. **TR-011 — Fiscalite antique** (8/10) : Sumer/Rome/Chine/MA/Islam/Inde/Ameriques/Andurarum — 9 F###
5. **TR-012 — Transmission des idees** (5/10) : Cordoue, CJC, Grand Bond, Ammisaduqa — 6 F###
6. **TR-009 — L'absence EST le fait** (5/10) : 5 F###
7. **TR-010 — Chainon arabe Cordoue/Tolede** (4/10) : 4 F###

## Top 3 theses cardinales

1. **THESE-001 — TRANSMISSION MULTI-LINEAIRE** (continuite, shadow 2.5x) : pas une fleche Sumer->France, c'est un reseau Cordoue/Bologne/Tolede/Jesuites
2. **THESE-002 — LA DETTE N'EST PAS UNIVERSELLE** (rupture, shadow 5.4x) : 4 civilisations (Inca, Maya, Azteque, Inde dharma) integrent SANS dette
3. **THESE-003 — L'ANDURARUM = RITUEL POLITIQUE** (exception, shadow 5.0x) : CharPin consensus, pas Hudson. Frequence 1/33 ans.

## Top 3 meta-observations

1. **OBS-001 — CORRELATION SHADOW <-> MARGINALISATION** : AM 6.4x (exclue) ↔ MA 1.5x (integree au recit). L'ombre EST un objet d'etude.
2. **OBS-002 — REFUTATION ASYMETRIQUE** : 5 conclusions testees, 1 tient (C4), 1 affaiblie (C2), 2 refutees (C1+C3), 1 intacte avec biais (C5). 40% de survie.
3. **OBS-003 — ASYMETRIE EST/OUEST** : fiches non-occidentales shadow moyen 4.4x vs occidentales 2.55x. L'exotisme produit plus d'ombre.

## GATE_H verdict

- H0 (orthogonalite) : PASS (90% convergence)
- H1 (transversalites) : PASS (8 detectees, cible 7+)
- H2 (F### par these) : PASS (5 par these, cible 3+)
- H3 (glyphes valides) : **PASS (sans override)** — 39 ✦, 2 ✧, 2 ⁅, 13 ❧ (backfill v33.4 effectué : HEAD-check 158 URLs en 13s, distribution réelle)
- H4 (pas circularite) : PASS (IN n'est pas dans suffixes_problematiques)
- H5 (meta_observations) : PASS (5 detectees, cible 5)
- H6 (shadow_factor) : PASS (3.85x agrege, toutes theses >= 1.0)

## Top 5 F### justificatifs (cross-fiches)

- F-META004 (C1 dette universelle REFUTEE 6.5x) → appuie THESE-002
- F-A001 (andurarum = rituel politique) → appuie THESE-003
- F-HUB001 (55% sources etatiques) → appuie THESE-004
- F-IN001 (caste 3000 ans) → appuie THESE-005
- F-R002 (CJC dans Code civil) → appuie THESE-001

## Top 3 gaps

- GAP-005 (Aryabhata ZERO recit occidental) — fait temoin de l'absence
- GAP-002 (keju imperial C, details) — operationnel, pas recurrant
- GAP-007 (Ammisaduqa tamkarum preserve) — exception qui confirme Charpin

## Verdict global

Pilote v33.3 REUSSI. Le LLM hote a detecte 8 transversalites, 5 theses cardinales (1 continuite + 2 ruptures + 1 exception + 1 continuite), 5 meta-observations. Le fichier synthese.yaml passe les **7 GATE_H sans aucun override** (apres backfill glyphes v33.4).

## Backfill v33.4 effectue (work item pilote)

- 158 URLs uniquees HEAD-checkees en 13s (142 OK / 13 cassees / 2 erreurs)
- 212 F### des 10 quintessences : glyphe backfilled (X pour tier 1, X pour tier 2+, X pour URL 4xx/5xx, X pour no-URL)
- Distribution : 55.7% X / 19.8% X / 17.9% X / 6.6% X
- S.shadow_factor: N/A -> 3.1 (top-level field ajoute)
