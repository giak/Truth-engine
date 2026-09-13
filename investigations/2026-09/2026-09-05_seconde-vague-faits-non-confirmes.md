# Seconde vague — ciblage des faits non confirmés (runs 8–12)

> Document de ciblage campagne-level. Chaque fait ✧ (VERIFIE, L1–L3) issu des runs 8–12 est listé
> avec sa faiblesse probatoire ; la seconde vague (Run 13) vise l'élévation vers ✦ (CONFIRME, L4 :
> 2 familles + réfutation + clé d'évidence stable) ou la disqualification honnête (GAP/EXCLUDED).
> Règle KERNEL : `✦ → CONFIRME (L4)` ; `✧ → VERIFIE (L1–L3)`. Les faits ✧ restent « non confirmés ».

## Méthode d'extraction

- Source : `*_RUN_STATE.json` de chaque run certifié (champs `tier`, `families`, `refutations`).
- Critère « non confirmé » : `tier == ✧` (VERIFIE), renforcé si `len(families) < 2` (corroboration faible)
  ou `refutations == []` (pas de contre-requête enregistrée).

## Inventaire (15 faits ✧)

| Fait | Run | Sujet court | Familles | Réfutation | Gravité |
|---|---|---|---|---|---|
| R8-FCT-005 | 8 | CRS R42738 : 469 interventions militaires US (1798–2023), 251 depuis 1991 | 1 | non | SINGLE-FAMILY |
| R8-FCT-006 | 8 | Weinstein (WP 1991) : NED « faisait covertly ce que la CIA faisait il y a 25 ans » | 1 | non | SINGLE-FAMILY |
| R8-FCT-007 | 8 | Russie/Chine/Iran : accusation d'orchestration occidentale non étayée | 1 | non | SINGLE-FAMILY |
| R9-FCT-005 | 9 | La Fabrique de l'industrie actionnée UIMM/France Industrie/Gifas/GIM ; Finchelstein Jaurès/Havas | 1 | non | SINGLE-FAMILY |
| R9-FCT-007 | 9 | Franc-maçonnerie France : 175 000+ membres (2014), influence politique en déclin | 2 | oui | ok |
| R10-FCT-005 | 10 | Forbidden Stories : ministère israélien de la Justice a tenté de dissimuler liens NSO/Pegasus | 1 | non | SINGLE-FAMILY |
| R10-FCT-006 | 10 | Municipales 2026 : officines liées à Tel-Aviv ont visé LFI | 1 | non | SENSIBLE + SINGLE-FAMILY |
| R10-FCT-007 | 10 | Walt & Mearsheimer (2006) : influence structurelle du lobby pro-israélien | 1 | non | SINGLE-FAMILY |
| R11-FCT-005 | 11 | Telos (2023) : lobbying allemand structurel anti-nucléaire à Bruxelles | 2 | non | NO-REFUTATION |
| R11-FCT-006 | 11 | Sortie nucléaire allemande = politique intérieure, pas d'obstacle à la neutralité technologique | 2 | non | NO-REFUTATION |
| R11-FCT-007 | 11 | Jean-Jaurès (2022) : compromis taxonomie obtenu France/Commission contre Verts allemands | 2 | non | NO-REFUTATION |
| R12-FCT-005 | 12 | Brillant (AFP 01/2026) : 25 tentatives 2024 « très grande majorité sans effet sur le débat public » | 1 | non | SINGLE-FAMILY |
| R12-FCT-006 | 12 | Loi Nuñez n.913 (Sénat 22/07/2026) : référé permanent contre fausses informations | 1 | non | SINGLE-FAMILY |
| R12-FCT-007 | 12 | Brouillage/spoofing GPS russe Baltique documenté depuis 2022 (~80 incidents AP) | 2 | non | NO-REFUTATION |

## Priorité Run 13 (7 cibles — les plus sensibles / vérifiables)

1. **R10-FCT-006** — officines liées à Tel-Aviv vs LFI (municipales 2026) — le plus sensible ; à confirmer ou disqualifier.
2. **R10-FCT-005** — Forbidden Stories / Pegasus (dissimulation ministère Justice israélien) — vérifiable via dossier Forbidden Stories.
3. **R8-FCT-005** — CRS R42738 469 interventions — vérifiable via rapport officiel CRS.
4. **R8-FCT-006** — citation Weinstein WP 1991 — vérifiable via archives originales.
5. **R9-FCT-005** — La Fabrique de l'industrie / Finchelstein — vérifiable via registre des entreprises + charte Fabrique.
6. **R12-FCT-006** — loi Nuñez n.913 — fait juridique, source officielle Sénat (famille A obligatoire).
7. **R12-FCT-005** — déclaration Brillant AFP (faible impact) — vérifiable via AFP.

## Traitement des 8 autres (veille / runs ultérieurs)

R8-FCT-007, R10-FCT-007, R11-FCT-005/006/007, R12-FCT-007, R9-FCT-007 : corroboration
supplémentaire et réfutations à prévoir dans une vague 3 ; R9-FCT-007 quasi-conforme (2 familles + réfutation).
## Statut (mise à jour après Run 13 — 2026-09-05)

**Run 13 exécuté et certifié (DELIVERY gate PASS)** : `2026-09-05_seconde-vague-elevation-faits-non-confirmes/`.

| Cible | Origine | Verdict Run 13 |
|---|---|---|
| Officines Tel-Aviv vs LFI | R10-FCT-006 | ✦ CONFIRME (rapport VIGINUM/Blackcore, commanditaires non identifiés) |
| Dissimulation Pegasus | R10-FCT-005 | ✦ CONFIRME (Guardian/Forbidden Stories + caveat Amnesty) |
| CRS 469 interventions | R8-FCT-005 | ✦ CONFIRME (congress.gov officiel + WarCosts) |
| Citation Weinstein | R8-FCT-006 | ✦ CONFIRME (Washington Post 22/09/1991 original) |
| Fabrique de l'industrie | R9-FCT-005 | ✦ CONFIRME (la-fabrique.fr officiel ; correction GIFAS) |
| Loi Nuñez n.913 | R12-FCT-006 | ✦ CONFIRME (Sénat officiel + vie-publique, avis CE) |
| Brillant 25 tentatives | R12-FCT-005 | ✦ CONFIRME (AFP Factuel + Maires de France) |

**Reste en veille (vague 3)** : R8-FCT-007, R9-FCT-007, R10-FCT-007, R11-FCT-005/006/007, R12-FCT-007.

## Statut final (après vague 3 — Run 14, 2026-09-05)

**Run 14 exécuté et certifié (DELIVERY gate PASS)** : `2026-09-05_vague3-elevation-faits-non-confirmes-restants/`.

| Cible | Origine | Verdict Run 14 |
|---|---|---|
| Narratif russe révolutions de couleur | R8-FCT-007 | ✦ CONFIRME (CSIS + Wikipedia ; financements civiques documentés, orchestration non prouvée) |
| Franc-maçonnerie déclin | R9-FCT-007 | ✦ CONFIRME (450.fm + hiram + GLDF ; déclin relatif, 170 000 en 2025) |
| Walt & Mearsheimer / lobby | R10-FCT-007 | ✦ CONFIRME (Harvard LRB + Guardian ; thèse contestée, Rosen-Weissman sans condamnation) |
| NZIA nucléaire | R11-FCT-005 | ✦ CONFIRME **corrigé** (Euractiv + WNN : nucléaire inclus parmi 17 technologies — réfute Telos) |
| Sortie nucléaire allemande | R11-FCT-006 | ✦ CONFIRME (OSW + WNA : politique domestique) |
| Taxonomie / Berlin | R11-FCT-007 | ✦ CONFIRME (Europarl + BMWK : Berlin cède, 278/328/33) |
| Brouillage GPS Baltique | R12-FCT-007 | ✦ CONFIRME (AP + DW ; attribution par faisceau d'indices) |

**Campagne d'élévation des 14 faits ✧ des runs 8–12 : COMPLÈTE.** (7 au run 13 + 7 au run 14.)
