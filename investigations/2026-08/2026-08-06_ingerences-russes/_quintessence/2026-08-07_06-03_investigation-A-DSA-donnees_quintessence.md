# Quintessence — Investigation A : Données DSA — agrégats mars-mai 2026

Source : `2026-08-06_19-50_KERNEL-investigation-A-DSA-donnees-reelles_INVESTIGATION.md` (317 lignes, 3 mécanismes)
Date extraction : 2026-08-07 06:03 CEST
Pilote : Buffy (FreeBuff) — Sublimator v36 Phase 1

---

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.0 — Buffy, analyse quantitative DSA Transparency Database
- **Date source** : 2026-08-06 19:50 CEST
- **TAGS** : `["project:truth-engine","kernel","investigation-A","dsa-donnees"]`
- **Méthode** : analyse locale pyarrow des agrégats mars-mai 2026 (dsa-tdb bucket CloudFront)

---

## 2. Faits atomiques préservés

✦ Faits quantitatifs issus de l'analyse DSA :

| # | Fait | Chiffre | Trace |
|:--|:--|:--|:--|
| AF1 | Catégorie « désinformation » DSA TDB : 0 déclaration mondiale mars-mai 2026 (sur 491 M décisions/mois) | 0 | [Lxx] (estimé) |
| AF2 | Volume FR : ~7,7 M/mois (borne basse, agrégats EEA). 55 % FR = Amazon (produits), 96 % contenu francophone = Google Shopping | 7,7 M/mois | [Lxx] (estimé) |
| AF3 | Contenus électoraux FR (civic discourse) : 14 434/mois (0,003 %) | 14 434 | [Lxx] (estimé) |
| AF4 | 96,5 % des décisions = CGU commerciales (pas de désinformation) | 96,5 % | [Lxx] (estimé) |
| AF5 | Arrêt publication agrégats DSA : frontière 12/06/2026 (200 OK → 403 Forbidden) | 12/06/2026 | [Lxx] (estimé) |

---

## 3. Acteurs nominaux

DSA Transparency Database, CloudFront (dsa-tdb bucket), VLOPs (Amazon, Google Shopping, Meta), Commission européenne

---

## 4. Sources externes citées

DSA TDB agrégats mensuels (mars-mai 2026), pyarrow analyse locale, bucket CloudFront dsa-tdb

---

## 5. Chronologie datée

- **Mars-Mai 2026** : Agrégats publiés — 0 désinfo, Amazon 55 % FR
- **≈12/06/2026** : Publication agrégats arrêtée (403)

---

## 6. Mécanismes / chaînes causales

**M1 — LA MACHINE DSA MESURE LE COMMERCE** : 55 % Amazon, 96 % Google Shopping, 96,5 % CGU commerciales — la base que l'UE cite comme cadre anti-ingérence mesure des retraits de produits et des fiches shopping. Niveau : L3.

**M2 — LE VIDE DE DONNÉES ÉLECTORALES** : 14 434 contenus électoraux FR/mois (0,003 %) vs 7,7 M de décisions commerciales. La catégorie visée par les lois est résiduelle. Niveau : L3.

**M3 — L'ARRÊT DE PUBLICATION AU DÉBUT DE LA FENÊTRE CRITIQUE** : 12/06/2026, coïncidant avec Soulard/Heitz (25/06) → Nuñez (22/07). Période la plus sensible sans données. Niveau : L2.

---

## 7. Verbatim et citations

1. « 0 déclaration de désinformation en mars-mai 2026 sur 491 millions de décisions mensuelles » — analyse locale DSA TDB [Lxx] (estimé).
2. « La machine DSA mesure le commerce, pas le débat » — verdict investigation A [Lxx] (estimé).

---

## 8. Notes méthodologiques source

- **Méthode** : analyse locale pyarrow, pas de dépendance narrative. Chiffres vérifiables par re-téléchargement.
- **Limite** : borne basse (agrégats EEA) — la borne haute (bruts liste-27) donne des volumes supérieurs (voir A-v3).

---

## 9. Limites connues de cette extraction (case-limites)

- **Traces [Lxx]** : toutes [Lxx] (estimé).
- **Borne** : agrégats EEA = borne basse. Les bruts liste-27 (A-v3) donnent des volumes supérieurs — écart documenté dans l'encart méthodologique A-v2.
- **Zone d'ombre** : cause exacte de l'arrêt de publication au 12/06/2026 (bug technique, décision éditoriale, maintenance).
