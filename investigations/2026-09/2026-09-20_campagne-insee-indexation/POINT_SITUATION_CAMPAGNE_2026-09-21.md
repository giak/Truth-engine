# Point de situation consolidé — Campagne INSEE / indexation

**Dossier** : `investigations/2026-09/2026-09-20_campagne-insee-indexation/`
**Date du rapport** : 2026-09-21
**Cadre d'exécution** : KERNEL Truth Engine v2.10.6 (`truth-engine-v2/KERNEL.md`) — gates déterministes `verify.py --kernel-contract`, certification delivery archivée par run
**Mode de production des chiffres** : totaux dérivés programmatiquement des `*_RUN_STATE.json` et `*_CERTIFICATION.json` (registres canoniques), sans recomptage manuel

---

## 1. Synthèse

| Catégorie | Nombre |
|---|---|
| Dossiers présents dans la campagne | 22 |
| Runs KERNEL tracés (RUN_STATE présent) | 21 |
| Investigations certifiées **DELIVERY PASS** | 14 |
| — dont flux initial du 21 (matin) | 5 |
| — dont runs OPEN du 20 repris en RESUME | 2 |
| — dont revalidations UPDATE du 21 | 7 |
| Parents du 20 laissés en FINAL non certifié (historique) | 7 |
| Dossiers orphelins (sans RUN_STATE) | 1 |
| **Faits enregistrés (tous runs)** | **147** |
| **Requêtes tracées (tous runs)** | **349** |

**Sujet-socle de la campagne** : la chaîne INSEE de l'indexation — IPC et ses modes de calcul, conventions d'indexation (SMIC, IRL, retraites, barème IR), populations légales et dotations (DGF), jusqu'au récit public (biais de perception, révisions des comptes, gouvernance).

---

## 2. Investigations certifiées DELIVERY PASS (14)

Colonnes : faits / requêtes / checkpoints issus des RUN_STATE ; `state_id` issu de la certification delivery (16 premiers caractères).

### 2.1 Flux initial certifié — 5 runs (matinée du 21)

| RUN_ID | faits | requêtes | CP | state_id |
|---|---|---|---|---|
| `20260921-0255-insee-taux-de-reponse-par-vague-p` | 9 | 11 | 7 | `c335cdde7394302d…` |
| `20260921-0314-insee-avis-conformite-cnis-eec-ga` | 9 | 7 | 7 | `16efda9d605e73a8…` |
| `20260921-0347-insee-effet-controle-externe-et-a` | 10 | 9 | 7 | `514b848d477c07b1…` |
| `20260921-0428-insee-chiffrage-indexation-effet-` | 9 | 19 | 8 | `fb081bcb76132b72…` |
| `20260921-0446-insee-comparaison-internationale-` | 9 | 15 | 8 | `479fc53698bbcf6e…` |

### 2.2 Runs OPEN du 20 repris en RESUME — 2 runs

Repositionnés à leur emplacement canonique (les chemins internes des états pointaient vers l'emplacement d'origine, antérieur au regroupement en campagne), repris via le contrat RESUME 2.10.6 et menés jusqu'à certification sous leurs RUN_ID d'origine.

| RUN_ID | faits | requêtes | CP | state_id | objet |
|---|---|---|---|---|---|
| `20260920-2050-dgcl-notes-elasticite-part-popula` | 5 | 11 | 7 | `515fb4767d08024b…` notes DGCL : mécanique part population, écrêtement PF > 85 %, élasticités Metzing |
| `20260920-2155-cui-bono-quantification-gap-closu` | 5 | 22 | 6 | `2847768ce2703853…` closure du gap IRL du parent : série ELC 001763530 extraite, chiffrage du cui bono |

**Incident de parcours (résolu)** : les FETCH initiaux du run cui-bono avaient été journalisés avec `result=OK` (hors vocabulaire runtime, qui attend `FOUND`). Réparation par **ré-exécution réelle** des 7 FETCH (QRY-014…020, tous 200) puis liage — jamais par édition d'état. Les 2 échecs CSV (HTTP 500) restent tracés comme observés.

### 2.3 Revalidations UPDATE — 7 runs (après-midi du 21)

Chaque parent du 20 resté FINAL non certifié a été repris en **UPDATE + nouveau RUN_ID** (jamais de re-certificat rétroactif, non conforme au KERNEL) : re-FETCH réel de chaque source web mappée, ré-inspection des PDF cités en chemin, réfutation adversariale exécutée pour chaque fait ✦, writeback Mnemo avec règle UPDATE (mémoire parent retrouvée) / WRITE (fait nouveau).

| RUN_ID (UPDATE) | faits | requêtes | CP | state_id | parent revalidé |
|---|---|---|---|---|---|
| `20260921-0826-irl-ecart-loyers-reels-elc` | 3 | 8 | 7 | `380c725139791502…` `20260920-2154-irl-ecart-loyers-reels-elc` |
| `20260921-0830-dgf-impact-ecart-population-metzi` | 5 | 8 | 7 | `ad83326e6380fce0…` `20260920-2008-dgf-impact-ecart-population-metzi` |
| `20260921-1000-indexation-conventions-gains-mill` | 6 | 9 | 7 | `495ab51e10d2e9f6…` `20260920-2110-indexation-conventions-gains-mill` |
| `20260921-1015-insee-biais-modes-calcul-fresque-` | 9 | 20 | 7 | `a406962b995b222a…` `20260920-1704-insee-biais-modes-calcul-fresque-` |
| `20260921-1030-insee-chaine-donnee-indicateur-cl` | 9 | 16 | 7 | `dc90dcaeb9149418…` `20260920-1812-insee-chaine-donnee-indicateur-cl` |
| `20260921-1045-insee-pdf-methodo-gap-access-clos` | 8 | 16 | 7 | `5f188ba79cfe3097…` `20260920-1921-insee-pdf-methodo-gap-access-clos` |
| `20260921-1100-prosopographie-dirigeants-insee-e` | 6 | 9 | 7 | `9375458ce6f71e42…` `20260920-2105-prosopographie-dirigeants-insee-e` |

---

## 3. Parents du 20 laissés en FINAL non certifié (7)

Conservés tels quels comme historique du flux antérieur (livrés avant la mise en place du flux 19a/19b avec certification). Leur contenu est revalidé fact par fact par leur UPDATE certifié ci-dessus — aucun n'est contredit.

| RUN_ID (parent) | faits | requêtes | revalidé par |
|---|---|---|---|
| `20260920-1704-insee-biais-modes-calcul-fresque-` | 9 | 47 | `20260921-1015-insee-biais-modes-calcul-fresque-` |
| `20260920-1812-insee-chaine-donnee-indicateur-cl` | 9 | 38 | `20260921-1030-insee-chaine-donnee-indicateur-cl` |
| `20260920-1921-insee-pdf-methodo-gap-access-clos` | 8 | 37 | `20260921-1045-insee-pdf-methodo-gap-access-clos` |
| `20260920-2008-dgf-impact-ecart-population-metzi` | 5 | 12 | `20260921-0830-dgf-impact-ecart-population-metzi` |
| `20260920-2105-prosopographie-dirigeants-insee-e` | 6 | 12 | `20260921-1100-prosopographie-dirigeants-insee-e` |
| `20260920-2110-indexation-conventions-gains-mill` | 6 | 12 | `20260921-1000-indexation-conventions-gains-mill` |
| `20260920-2154-irl-ecart-loyers-reels-elc` | 2 | 11 | `20260921-0826-irl-ecart-loyers-reels-elc` |

---

## 4. Orphelin (1)

- **`2026-09-20_prosopographie-dg-insee`** : contient uniquement un `_NARRATIVE.tmp.md` (57 lignes), sans RUN_STATE, ni INPUT, ni INVESTIGATION. Brouillon résiduel redondant : le sujet a été relancé le soir sous le slug complet (`prosopographie-dirigeants-insee-ecoles-bercy-conflits`), livré puis revalidé/certifié. Non certifiable en l'état ; suppression ou archivage à trancher.

---

## 5. Ajustements matériels documentés pendant les revalidations

Aucun ajustement n'est masqué ; tous sont tracés dans les RUN_STATE et les récits :

1. **`fiche-precision.pdf` (HTTP 500 à l'inspection)** — substituée par la page canonique vivante « Populations de référence » (Insee 8680694), re-fetchée ; l'énoncé du fait FCT-004 du parent pdf-méthodo a été **ajusté honnêtement** (méthodes d'estimation confirmées sur la page ; coefficient de variation par strate porté par l'inspection parent du 20).
2. **legifrance.gouv.fr et economie.gouv.fr (HTTP 403 pour l'agent curl)** — inspection réelle via le lecteur d'URL de session (loi du 7 juin 1951, art. 1er, re-inspectée in extenso), tracée FETCH/FOUND dans les registres.
3. **4 sources PATH du parent indexation** (COR doc07, DT Insee 2025-08, circulaire CNAV, rapport Cour des comptes) — re-extraction locale réelle (pdftotext), hors périmètre web (pas de QRY FETCH, conformément au contrat).
4. **Colloque Académie des sciences morales et politiques (source morte apparente)** — l'URL complète mappée par le parent répond HTTP 200 ; re-fetchée telle quelle (aucune substitution).
5. **Réfutations adversariales réellement exécutées** pour les 8 faits ✦ concernés (aucune contradiction trouvée ; pour le canal « direction de la Prévision », le PDF de l'Autorité de la statistique publique documentant la dualité DG-ministre est identifié comme matériel adversarial et porté en limite du fait).

---

## 6. Apports matériels notables de la campagne

- **Écrêtement DGF** : le seuil courant vise les communes dont le potentiel fiscal dépasse **85 % de la moyenne nationale** (la note DGCL 2015 reprise par le parent décrivait 0,75 × PF) — divergence documentée et confirmée par sources 2026 (DGCL/Landes, AMF, Sénat) ; part CPS intégralement transférée aux EPCI depuis la LF 2024.
- **Chiffrage DGF Metzing** : élasticités forfait/population DGF mesurées 12,9–94,6 EUR/hab ; écart de 113 habitants ≈ 9 800 EUR/an (corroboré Sénat + presse régionale) ; rattrapage +37 hab. INSEE en deux ans.
- **Cui bono IRL vs loyers effectifs (closure du gap)** : série Insee BDM 001763530 (IPC 04.1 « loyers effectifs ») extraite et recombinée en moyennes annuelles — cumuls 2022-2025 : IRL **+10,9 %** vs ELC **+7,7 %** vs IPC hors tabac **+13,2 %** ; bascule 2025 (ELC > IRL, première de la série, corroborée par l'IR Insee n° 8 du 15/01/2026). Verdict : cui bono **conjoncturel, non structurel** ; la thèse « gagnant structurel » est REFUTED.
- **Conventions d'indexation chiffrées** : retraites indexées sur les prix (1987 privé / 2003 public) ≈ 3,7 pts de PIB d'écart de niveau à horizon 2070 ; barème IR indexé sur l'inflation **estimée** de septembre n-1 sans régularisation (8 années sur 13 en défaveur du contribuable, trop-payé estimé 2,8–6 Md€).
- **Biais documentés de la statistique publique** : biais moyen haussier des révisions de croissance +0,34 pt (2005-2024, Rexecode) ; pauvreté facteur 5 selon le seuil choisi (2,84 M à 40 % → 14,58 M à 70 %) ; exclusion des loyers imputés de l'IPC français (méthode qualifiée de trop étroite par Eurostat).
- **Gouvernance** : prosopographie des 10 DG de l'Insee — 8/10 X-ENSAE, canal Bercy (direction de la Prévision) traversant au moins 5 mandats ; aucun conflit d'intérêts documenté ; débats d'indépendance politiques en 2012 et 2025.

---

## 7. Conformité KERNEL

- Chaque run certifié dispose : du dossier forensique co-localisé complet (INPUT, RUN_STATE, NARRATIVE, MNEMO_SNAPSHOT, INVESTIGATION, CERTIFICATION), d'un stamp `DELIVERY_PASS`, et d'une certification `verify.py --kernel-contract delivery` verdict PASS.
- Gates PRE (19a) et DELIVERY (19b) passées sur chaque livraison ; writebacks Mnemo exécutés uniquement après PRE_GATE PASS ; `state_id` de delivery identifie le fichier livré.
- Aucun FINAL/provisional-final non certifié n'a été produit par le flux 2.10.6 ; les 7 parents non certifiés datent du flux antérieur et restent hors périmètre de livraison certifiée.

