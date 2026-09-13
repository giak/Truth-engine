# 🦊 Axe D — Démographie du parc : 506 fermetures de déchèteries depuis 2013, mais un solde net positif

**Run `20260830-2045-audit-demographie-parc-fermetures`** — investigation démographique du réseau : comptabiliser les fermetures depuis 2013 via le champ `date_fermeture_service` SINOE (le « D_FERM » officiel), croisé presse.

## Verdict

| # | Fait | Statut |
|---|---|---|
| **FCT-001** | **Le champ D_FERM officiel existe — mais sur un autre portail** : `date_fermeture_service` dans le dataset « Liste des services de déchèterie par année » (62 330 lignes, data.sinoe-dechets.ademe.fr) — **740 services distincts avec date de fermeture**, ABSENT de l'annuaire data.ademe.fr (35 colonnes) | ✦ (A+B, réfutation NONE) |
| **FCT-002** | **506 fermetures de services SINOE depuis 2013** (date_fermeture ≥ 2013-01-01) : 486 déchèteries, 17 plateformes apports verts, 2 déchèteries pros, 1 CAV ; pics 2016 (63) et 2021 (60) ; top régions Nouvelle-Aquitaine 89, Grand Est 56, Pays de la Loire 55 | ✦ (B+D, réfutation NONE) |
| **FCT-003** | **Solde net POSITIF : 540 ouvertures vs 506 fermetures = +34** — le réseau ne se rétracte PAS à l'échelle nationale (4 532 services en 2013, 4 551 puis 4 630 dans l'annuaire) | ✦ (B+D, réfutation NONE) |
| **FCT-004** | **Cas type de fermeture-remplacement documenté par acte officiel** : Provence Verdon ferme Barjols (25/07/2026) et Fox-Amphoux Trois Croix (11/07/2026), ouvre Tavernes (27/07/2026) — **rationalisation 2 vers 1** (13 quais, 15 filières, ICPE, espace réemploi) | ✦ (C+B, réfutation NONE) |
| **FCT-005** | **Croisement interne valide le comptage** : 5172 La Haye-Fouassière date_fermeture = **2013-11-18** (= date exacte établie passe 1955), 4482 Randan = **2018-12-31** (service FERMÉ) ; proxy de disparition (423) surestime (135 réapparitions = renumérotations) | ✦ (B+D, réfutation NONE) |

## Découvertes clés

1. **Le « paradis de la data » inversé : le champ D_FERM existait, il était juste ailleurs.** L'annuaire data.ademe.fr (45 169 records, celui analysé depuis la passe P0) n'a aucun champ de fermeture — c'est sur le portail **data.sinoe-dechets.ademe.fr**, dataset « Liste des services de déchèterie par année » (62 330 lignes, mis à jour 30/08/2026), que `date_fermeture_service` est exposé (740 services fermés). La donnée n'était pas absente : elle était **dispersée entre deux portails ADEME**.
2. **Le réseau ne se rétracte pas** : 506 fermetures depuis 2013 (≈39/an) sont **plus que compensées** par 540 ouvertures (+34 net). La courbe du parc reste stable — c'est l'inverse du récit « le réseau se rétracte » qui ressort de la presse.
3. **La rationalisation locale est réelle mais compensée** : cas Tavernes (2→1, Provence Verdon 2026, acte officiel INSPECTED) illustre la logique de modernisation par fermeture-remplacement. Mais elle est globalement compensée par les ouvertures.
4. **Limite honnêteté épistémique** : lag de déclaration documenté — dernières années déclarées 2023 (551 services), 2024 (2177), 2025 (1974) ; les fermetures 2025-2026 (19) sont **sous-déclarées** ; le solde réel 2026 est donc à la baisse par rapport à +34 mais reste vraisemblablement positif ou nul.

## Sources INSPECTED

- Dataset SINOE « Liste des services de déchèterie par année » (data.sinoe-dechets.ademe.fr, 62 330 lignes) + API data-fair paginée (63 pages × 1000) — champ `date_fermeture_service`
- Annuaire SINOE data.ademe.fr (CSV local 45 169 records, 35 colonnes SANS D_FERM) — proxy de disparition persistante
- Acte officiel Provence Verdon (provenceverdon.fr, INSPECTED) : Barjols 25/07/2026, Fox-Amphoux 11/07/2026, Tavernes 27/07/2026
- Presse : Nice-Matin 17/07/2026 (snippet), Var-Matin (snippet)

## Réfutations (5 NONE)

- FCT-001 : aucun champ de fermeture totalement absent de SINOE, ni < 740 services avec date de fermeture
- FCT-002 : aucune preuve de < 506 fermetures depuis 2013 ni de répartition par type différente
- FCT-003 : aucune preuve d'un solde net négatif ou d'un rétrécissement du parc national
- FCT-004 : aucune preuve de maintien de Barjols/Fox-Amphoux ouvertes après le 27/07/2026, ni que Tavernes ne les remplace pas
- FCT-005 : aucune preuve que les dates de fermeture 5172 (2013-11-18) ou 4482 (2018-12-31) soient différentes de celles établies par les passes 1955/1945

## Gaps ouverts

1. Données 2026 complètes (le millésime 2026 est partiel : 5 fermetures déclarées, ~2 000 services à remonter)
2. Croiser les 506 fermetures avec les actes délibératifs EPCI (échantillon) pour qualifier le motif (conformité, rationalisation, fusion)
3. Mesurer le lag presse→SINOE sur les cas 2025-2026 (Tavernes : Barjols non encore marquée fermée dans le dataset)
4. Cartographier la rationalisation (2→1) par EPCI pour quantifier la concentration du maillage

## Conséquence sur la fresque

L'axe D clôt la question « le réseau se rétracte-t-il ? » : **non** — 506 fermetures depuis 2013, mais 540 ouvertures et un solde net +34. La donnée officielle D_FERM existait mais était dispersée sur un second portail SINOE (découverte data). Le récit médiatique de « fermetures de déchèteries » (axe A : exclusion des pros, dépôts sauvages) doit être nuancé : la démographie du parc reste stable, la mutation est dans l'accès et le financement, pas dans le nombre de sites.
