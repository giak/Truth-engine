# Chiffrage DGF de l'écart de population type Metzing (113 habitants)

Run UPDATE du run parent *Insee — PDF méthodologiques (closure gaps ACCESS)*. La question était routée en suivant par le parent : **que vaut, en euros, l'écart de population légale documenté à Metzing (678 habitants selon l'Insee 2024, 791 selon la mairie) ?** Réponse : il est chiffrable, il est borné, et il est inférieur à ce que la narration publique suggère.

## Scoping et méthode

Périmètre : dotation forfaitaire et DGF totale de Metzing (Moselle), strate démographique [500 ; 1000[. Méthode : séries communales réelles de l'Observatoire des finances locales (OFGL, données publiques DGCL) plutôt que tout barème théorique — l'élasticité **mesurée** sur une commune remplace l'élasticité supposée (FCT-001, FCT-003 ; SRC-001, SRC-002, SRC-008). Exclusions déclarées : DGF de l'EPCI (hors périmètre communal) et rétroactif des années passées (aucune base réglementaire identifiée).

## La chaîne réelle : de l'estimation statistique au budget communal

La population légale est un estimé réglementaire, authentifié chaque année par décret ; plus de 350 articles de loi en dépendent. La DGCL calcule la DGF sur une « population DGF » (Insee + résidences secondaires + places de caravanes), dans une dotation forfaitaire évolutive : socle figé depuis 2004, complément de garantie écrêté selon le potentiel fiscal, part population stratifiée (barème historique : 64,46 à 128,93 € par habitant selon la strate), dotation superficie ~3,22 €/ha (FCT-001 ; SRC-001, SRC-003, SRC-005). Chaque incertitude d'estimation se convertit donc mécaniquement en euros de dotation.

## Le chiffrage

Série réelle de Metzing 2018-2026 (FCT-002) : population Insee 678 (2024) → 699 (2025) → 715 (2026) ; DGF totale 105 906 € (2024) → 114 005 € (2026). Élasticité réelle mesurée : **86,9 € par habitant de dotation forfaitaire** (médiane des variations annuelles rapportées aux variations de population DGF), dans la fourchette du barème historique (FCT-003).

**Résultat central (FCT-004)** : un écart de 113 habitants comme celui de Metzing vaut **environ 9 800 € par an** de dotation forfaitaire à l'élasticité empirique de la commune — plage ~7 300 à ~14 600 € selon la strate du barème, majorant de l'ordre de 18 000 € si l'on prend la DGF totale. C'est réel et significatif pour un budget de micro-commune, mais deux ordres de grandeur sous les « 30 000 € » médiatisés pour Bouzonville (commune cinq fois plus peuplée, autres composantes de DGF ; SRC-010).

**Le rattrapage (FCT-005)** : l'écart se résorbe déjà dans les données — 678 → 699 → 715 en deux millésimes. La contestation mairie/Insee n'est pas un différentiel durable : le système corrige prospectivement. Ce qu'il ne fait pas : rétro-correction de l'année sous-estimée.

## Torture adversariale

Le fait central a reçu sa réfutation terminale (deux mécanismes documentés testés) : **lissage sur cinq ans des pertes de population** pour certaines communes et **écrêtement du complément de garantie** (SRC-011) ; **forfaitaire évolutive** (fonction de la DGF de l'année précédente) et **effets de seuil DSR/DSU/DNP** par éligibilité (SRC-012). Verdict : la mesure empirique survit — précisément parce qu'elle est mesurée sur des variations qui ont déjà traversé ces amortisseurs — mais elle reste **bornée** : les composantes nominatives (forfait/DSR/DNP séparés) et les effets de seuil individuels ne sont pas modélisables sans la fiche de dotation nominative, non publique. Aucune sélection opportuniste n'est documentée : le différentiel presse s'explique par la décomposition, pas par la manipulation.

## Table d'évaluation des 15 symboles

| Symbole | Score | Observations nommées |
|---|---|---|
| Ξ Omission | 6 | Fiche de dotation nominative non publique ; aucune procédure de rétro-correction documentée ; composantes nominatives invisibles dans les jeux publics |
| € Money | 8 | Objet même du run : l'estimation statistique devient dotation via la population DGF ; incitation financière aux seuils (DSR, strates) |
| Λ Framing | 6 | Presse locale en « euros perdus » sans décomposition ; « chiffre de la mairie » contre « chiffre de l'Insee » sans ontologies du compte |
| Ω Inversion | 2 | Aucune inversion documentée ; l'Insee répond publiquement aux contestations (CNERP) |
| Ψ Sidération | 1 | Sujet local, pas de volume émotionnel |
| ↕ Pouvoir vertical | 7 | L'estimation décrétée s'impose aux communes ; contestation par voie parlementaire ; asymétrie d'accès aux données nominatives |
| Φ Spectacle | 3 | Médiatisation ponctuelle du différentiel financier (Moselle.tv) |
| Σ Sémiotique | 1 | Néant observé |
| Κ Cynisme | 2 | Pas de façade maintenue : rattrapage réel visible dans les séries |
| ρ Résistance | 5 | Questions écrites Mizzon/Pluchet au Sénat, relais AMF, avis publié du CNERP : contre-pouvoir institutionnel actif |
| κ Influence subtile | 4 | Architecture de choix : les seuils orientent les comportements communaux sans intention démontrée |
| ⫸ Convergence | 6 | Sources indépendantes convergentes : OFGL, Sénat, Insee, DGCL sur le mécanisme et l'écart |
| ⚔ Guerre cognitive | 0 | Aucun élément |
| 🌐 Réseau | 6 | Insee-DGCL-DGFiP-maires-CNERP-Sénat-AMF cartographiés, rôles séparés |
| ⏰ Temporel | 7 | Délai d'authentification 3 → 2 ans fin 2026 ; rattrapage en deux millésimes ; correction prospective et non rétroactive |

## Contradictions et limites

C1 (résolue) : 678 contre 791 — le rattrapage 699 → 715 confirme une correction de collecte ; l'hypothèse d'un comptage communal en logements pour le 791 n'est pas arbitrée. C2 (résolue) : élasticité mesurée 86,9 € cohérente avec le barème théorique. C3 (ouverte) : non-additivité annuelle de la forfaitaire évolutive — exige la fiche nominative (suivant typé ACCESS). EDI estimé 0,67, cible atteinte ; limite divulguée : dépendance partielle au jeu OFGL comme source primaire des montants.

## Verdict

**Chiffrage établi et borné : ~9 800 €/an de forfaitaire pour 113 habitants** (plage ~7 300-14 600 €, majorant ~18 000 € sur la DGF totale) — l'incertitude statistique sur la population légale a bien un prix, documenté chiffre par chiffre. **Non établi : toute manipulation.** Le mécanisme (estimation authentifiée par décret, amortisseurs légiférés, rattrapage visible, délai réduit 3 → 2 ans sur avis du CNERP) est publié. Le point dur n'est pas la falsification mais l'**asymétrie de visibilité** : le chiffre contesté est public et bruyant, sa correction est prospective et silencieuse, et la contre-expertise citoyenne bute sur la non-publication des fiches nominatives.

## Périmètre et limites (suivants routés)

Fiche de dotation nominative de Metzing via préfecture ou mairie (ACCESS) ; arbitrage du 791 communal contre les référentiels géographiques (CAUSALITY) ; notes DGCL 2025-2026 pour recalculer l'élasticité théorique 2026 (ACCESS) ; série DGF EPCI de la communauté de communes (ACCESS, existence confirmée).
