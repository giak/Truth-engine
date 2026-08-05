# Quintessence — ARCOM 2022 : temps de parole des souverainistes, extraction quantitative

Source : `investigations/2026-08/corpus-souverainete-2027/enquetes/2026-08-04_21-30_arcom_2022_temps_parole_souverainistes_INVESTIGATION.md`

Date : 2026-08-04 | Heure : 21:35 CEST | Type : quintessence | Complexité : APEX

---

## 1. Métadonnées & trace source

- **Autorité** : INVESTIGATION ARCOM 2022, 2026-08-04_21-30
- **Statut** : APEX (27 faits, 10 sections)
- **Symboles dominants** : Ξ=9 (invisibilisation médiatique), Λ=7 (asymétrie structurelle), Σ=5 (données quantitatives)
- **Trace** : 27 faits F-AR2-01..F-AR2-27

---

## 2. Faits atomiques préservés

- F-AR2-01 | Macron : 1164h54 de temps de parole sur chaînes info (CNews + BFM TV + France Info + LCI) | ✦ | [§2]
- F-AR2-02 | Le Pen : 968h40 | ✦ | [§2]
- F-AR2-03 | Pécresse : 583h24 | ✧ | [§2]
- F-AR2-04 | Zemmour : 450h07 | ✧ | [§2]
- F-AR2-05 | Jadot : 238h22 | ✧ | [§2]
- F-AR2-06 | Hidalgo : 208h45 | ✧ | [§2]
- F-AR2-07 | Roussel : 155h19 | ✧ | [§2]
- F-AR2-08 | Dupont-Aignan : 81h25 (CNews 19h30, BFM TV 8h08, France Info 27h39, LCI 26h07) | ✦ | [§2]
- F-AR2-09 | Lassalle : 59h26 (CNews 10h00, BFM TV 5h52, France Info 21h20, LCI 22h13) | ✦ | [§2]
- F-AR2-10 | Arthaud : 59h05 | ✧ | [§2]
- F-AR2-11 | Poutou : 57h48 | ✧ | [§2]
- F-AR2-12 | Asselineau : 4h24 (CNews 0h31, BFM TV 0h35, France Info 1h59, LCI 1h18) | ✦ | [§2]
- F-AR2-13 | Macron/Asselineau = 264:1 | ✦ | [§3]
- F-AR2-14 | Le Pen/Asselineau = 219:1 | ✦ | [§3]
- F-AR2-15 | Zemmour/Asselineau = 102:1 | ✧ | [§3]
- F-AR2-16 | Macron/Dupont-Aignan = 14:1 | ✦ | [§3]
- F-AR2-17 | Macron/Lassalle = 20:1 | ✦ | [§3]
- F-AR2-18 | Pécresse/Dupont-Aignan = 7:1 | ✧ | [§3]
- F-AR2-19 | P1 : Asselineau 0h31 sur CNews = 1 seul passage ; Dupont-Aignan 6h45 sur CNews ; Macron 110h34 | ✦ | [§4]
- F-AR2-20 | P3 (égalité) : 11 candidats entre 34h47 et 40h29 | ✦ | [§5]
- F-AR2-21 | P3 : Asselineau ABSENT de la période d'égalité | ✦ | [§5]
- F-AR2-22 | Asselineau P1 tous médias (radio+TV) : 11h15, dont Europe 1 1h31, Sud Radio 1h31, CNews 0h31 | ✦ | [§6]
- F-AR2-23 | Asselineau P1 tous médias = ~10 min/jour ; Macron = ~8h30/jour | ✦ | [§6]
- F-AR2-24 | Sud Radio et Europe 1 sont les deux plus gros pourvoyeurs d'Asselineau (1h31 chacun) ; CNews 9e (0h31) | ✧ | [§6]
- F-AR2-25 | Dupont-Aignan : CNews 24 %, BFM TV 10 %, France Info 34 %, LCI 33 % | ✦ | [§7]
- F-AR2-26 | CNews donne PROPORTIONNELLEMENT plus de temps aux souverainistes que BFM TV (24 % vs 10 % pour NDA) | ✦ | [§7]
- F-AR2-27 | Lassalle : CNews 17 %, BFM TV 10 % | ✧ | [§7]

---

## 3. Acteurs nominaux

- **François Asselineau** (UPR) : 4h24, ratio 264:1 vs Macron, structurellement invisible — [§2:F-AR2-12]
- **Nicolas Dupont-Aignan** (DLF) : 81h25, peloton des petits, ratio 14:1 — [§2:F-AR2-08]
- **Jean Lassalle** (Résistons !) : 59h26, peloton des petits, ratio 20:1 — [§2:F-AR2-09]
- **ARCOM** : régulateur, définit le seuil d'égalité qui exclut Asselineau — [§1, §5]
- **CNews** : 24 % du temps NDA, 17 % du temps Lassalle — [§7:F-AR2-25]
- **BFM TV** : 10 % du temps NDA, 10 % du temps Lassalle, plus restrictif que CNews — [§7:F-AR2-26]
- **France Info** : 34-36 % pour NDA et Lassalle (inclut probablement radio+TV agrégées) — [§2, §7]
- **Sud Radio** : premier pourvoyeur d'Asselineau (1h31 en P1) — [§6:F-AR2-22]

---

## 4. Sources externes citées

- ARCOM via data.gouv.fr : dataset 67ee89ca16ae74bc0756195c, « Temps de parole des candidats — Élection présidentielle 2022 »
- 4 CSV : P1 (1er janvier-7 mars), P2 (8-27 mars, v2), P3 (28 mars-8 avril), P4 (11-22 avril)
- Extraction Python/pandas (~50 lignes), 2026-08-04, machine locale

---

## 5. Chronologie datée

- 01/01/2022 : début P1 (équité) — Asselineau reçoit 0h31 sur CNews, 0h35 sur BFM TV — [§4:F-AR2-19]
- 07/03/2022 : fin P1 — Asselineau cumule 4h24 sur chaînes info, Dupont-Aignan 32h02 — [§4]
- 08/03/2022 : début P2 (équité) — Asselineau disparaît des données (absent) — [§2]
- 27/03/2022 : fin P2 — Dupont-Aignan cumule 14h35, Lassalle 10h10 — [§2]
- 28/03/2022 : début P3 (égalité stricte) — 11 candidats reçoivent ~35h chacun ; Asselineau EXCLU — [§5:F-AR2-21]
- 08/04/2022 : fin P3 — [§5]
- 10/04/2022 : premier tour — Dupont-Aignan 2,06 %, Lassalle 3,13 %, Asselineau non candidat — [§0]
- 11-22/04/2022 : P4 (second tour) — uniquement Macron (398h) et Le Pen (398h) — [§2]

---

## 6. Mécanismes / chaînes causales

**M1 — Invisibilisation par seuil ARCOM** : le régulateur applique l'égalité stricte (P3) aux seuls candidats ayant franchi un seuil de « reconnaissance » (500 parrainages, actualité électorale). Asselineau, n'ayant pas franchi ce seuil, est EXCLU de la seule période où les « petits » candidats reçoivent un temps équitable (~35h). Mécanisme : L1=seuil ARCOM (cause immédiate), L2=invisibilisation structurelle (effet médiatique), L3=non-existence électorale (effet politique). [§5, §8]

**M2 — Plafonnement par catégorie « petit candidat »** : Dupont-Aignan et Lassalle reçoivent ~60-80h, soit 2-3× moins que Hidalgo/Jadot/Roussel (~155-238h). Le mécanisme n'est pas un blackout mais un plafonnement : ils existent médiatiquement, mais dans une catégorie « petit candidat » qui ne leur permet pas de percer. L'égalité stricte (P3) est la SEULE période où ils rattrapent. [§8]

**M3 — Distribution radio > TV pour les « très petits »** : pour Asselineau (11h15 tous médias en P1), les deux plus gros pourvoyeurs sont Sud Radio (1h31) et Europe 1 (1h31). Les chaînes TV info sont loin derrière. Le média radio est structurellement plus accessible aux candidats marginaux. [§6, §8]

---

## 7. Verbatim et citations

- « Temps de parole des candidats — Élection présidentielle 2022 » — ARCOM, dataset data.gouv.fr 67ee89ca16ae74bc0756195c [§1]
- 4h24 sur 112 jours = ~2 minutes 20 secondes par jour pour François Asselineau — extraction Python 2026-08-04 [§2:F-AR2-12]
- 264:1 = le ratio Macron/Asselineau, le plus élevé de tous les candidats — extraction Python 2026-08-04 [§3:F-AR2-13]
- « CNews n'est PAS le média qui invisibilise le plus les souverainistes — c'est BFM TV qui est le plus restrictif » — conclusion §7 [F-AR2-26]

---

## 8. Notes méthodologiques source

- **Statut source** : extraction quantitative reproductible. Données ARCOM/data.gouv.fr, 4 CSV, parsing Python/pandas.
- **Test de partialité** : source institutionnelle (ARCOM, A). Données brutes non retraitées par des intermédiaires. Fiabilité maximale pour la donnée quantitative.
- **Biais potentiel** : France Info agrège probablement radio + FranceinfoTV, rendant les comparaisons inter-chaînes fragiles. Les données CNews/BFM TV/LCI sont homogènes (TV uniquement).
- **Limite temporelle** : données 2022 uniquement. Aucune donnée individuelle post-2022 (Philippot, figures non-candidates).
- **Temps de parole ≠ temps d'antenne** : l'ARCOM mesure les interventions DES candidats, pas le temps où l'on PARLE d'eux.

---

## 9. Limites connues de cette extraction (case-limites)

- [L1] Données 2022 uniquement. La situation 2025-2026 peut avoir évolué (CNews a gagné en audience, le paysage médiatique a changé).
- [L2] France Info : agrégation radio+TV probable, faussant les comparaisons inter-chaînes pour ce média.
- [L3] Qualitatif absent : 35h d'égalité en P3 ne dit rien sur le CADRAGE (favorable/hostile/neutre).
- [L4] Philippot absent : non-candidat en 2022, il n'apparaît pas dans les données ARCOM.
- [L5] Extraction P1 format v1 (Durée unique), P2-P4 format v2 (4 tranches). Cohérence vérifiée par sommation.
