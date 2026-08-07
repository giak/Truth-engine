# MÉMO — La loi Nuñez déposée dans un vide de désinformation

**Date** : 2026-08-06_20-37 CEST | **Type** : MEMO | **Source** : investigations A-v2, A-v3 (analyse locale des données DSA Transparency Database, pyarrow) | **$TAGS** : `["project:truth-engine","kernel","status:confirme","verifie-2026-08-06","iceberg-max","dsa","memo"]`

## La phrase centrale

**La loi Nuñez (n° 913, déposée au Sénat le 22 juillet 2026) est votée pour lutter contre un phénomène qui totalise 542 déclarations de « désinformation » sur 24 302 119 décisions de modération enregistrées ce jour-là dans la base officielle de l'UE (0,002 %).**

## Les 3 chiffres qui font le résultat

| # | Chiffre | Portée | Source |
|:--|:--|:--|:--|
| 1 | **0 déclaration** de désinformation (KEYWORD_DISINFORMATION) sur **491 M décisions/mois** | Monde, mars-mai 2026 (3 mois) | Agrégats DSA TDB (bucket officiel) |
| 2 | **542 / 24 302 119** (0,002 %) désinformation déclarée | Monde, **22/07/2026 = jour du dépôt de la loi Nuñez** | Fichier brut officiel du jour, total validé = chiffre de la page download |
| 3 | **Arrêt de publication des agrégats publics au 12 juin 2026** (13/06 = 403) | La fenêtre Soulard/Heitz (25/06) → avis CE (16/07) → dépôt Nuñez (22/07) est la seule sans données agrégées | Tests bucket CloudFront dsa-tdb |

**Contre-point de contexte** : la machine DSA mesure le commerce, pas le débat — Amazon = 55 % du volume FR, Google Shopping = 96 % du contenu francophone (fiches produits), contenus électoraux retirés pour la France = 14 434/mois (agrégats, 0,003 %) et 59 251 le 22/07 (bruts, 0,24 %).

## Lecture honnête : deux hypothèses, même conclusion

1. **Soit la désinformation retirée est réellement résiduelle** — les plateformes jugent que presque rien ne tombe dans la catégorie (au vu de leurs CGU).
2. **Soit les plateformes ne la déclarent presque jamais** — catégorisation inadéquate, risque juridique, ou choix.

**Les données ne permettent pas de trancher entre « désinformation absente » et « désinformation non déclarée ».** Mais dans les deux cas, le prétexte quantitatif de la loi est invisible dans la base que l'UE et la France citent comme cadre de la lutte anti-ingérence : l'outil est étendu (référé à toutes les élections, triplement des peines, ARCOM) **au-delà de tout usage documenté**.

## Limites méthodologiques (à citer systématiquement)

1. **Double encodage de territorial_scope** : les agrégats transforment la liste des 27 pays UE en « EEA » (filtre FR = **borne basse**, FR noyée) ; les bruts listent les 27 pays (filtre FR = **borne haute**). Facteur ~185 (123 428 FR strict vs 22,9 M FR-liste le 22/07). **Toute affirmation « X retraits en France » doit préciser sa borne.**
2. **Les mois juin-juillet n'ont pas d'agrégats publics** : les chiffres du 22/07 proviennent du zip quotidien brut (1,66 GB, 24 302 119 lignes, total validé). La panne/arrêt de publication est un fait mesuré, pas une preuve d'intention.
3. **Pas une preuve de complot** : un système peut émerger par opportunisme et panique. Le résultat documente un **décalage mesurable** entre la rhétorique (« ingérence menaçant l'élection ») et les données (« retraits de produits Amazon »), indépendamment des intentions.
4. **Données primaires, reproductibles** : agrégats + fichier brut du jour téléchargés, analysés localement en pyarrow ; aucune dépendance à Viginum, aux médias ou à la narration officielle.

## Verdict

Le 22 juillet 2026, la loi qui étend le plus l'appareil de contrôle de l'information français depuis 2018 est déposée le jour où la base de données officielle enregistre 542 déclarations de désinformation sur 24,3 millions de décisions. La menace invoquée ne se mesure nulle part ; la machine, elle, s'étend. **Une machine en construction, pas une menace avérée.**

---
**Fichiers sources** : `2026-08-06_19-50_KERNEL-investigation-A-DSA-donnees-reelles_INVESTIGATION.md` (borne basse, 17 faits ✦) · `2026-08-06_20-30_KERNEL-investigation-A-v3-jour-depot-nunez_INVESTIGATION.md` (22/07 brut, bornes haute/basse, 11 faits ✦) · `2026-08-07_00-00_KERNEL-piste5-angles-convergents_INVESTIGATION.md` (P5F7-P5F9, Angle 7)
