# Passe KERNEL — Ventilation des barèmes REP par déchèterie : contourner SINOE via délibérations et conventions par EPCI

**Run** : 20260830-1454-baremes-par-site-epci · **As-of** : 2026-08-30 · **Mode** : INVESTIGATION · **Complexité** : COMPLEX

## Question pilote

> Peut-on reconstituer la ventilation réelle des soutiens REP (€/t ou forfaits) par déchèterie, malgré le champ SINOE `LST_TYPE_DECHET` vide sur 100 % des sites, à partir des délibérations territoriales et conventions éco-organismes par EPCI ?

## Méthode

1. **Mémoire d'abord** (`MNEMO_Q`, mémoire saine 200-healthy, probe NONE — pas de snapshot exact à hydrater) ; les FCT de la passe barèmes (20260830-1416) restent des références chaudes.
2. **Axes** : AXS-001 (documents territoriaux par EPCI) ; AXS-002 (reconstitution de la ventilation par site + cui bono).
3. **Sources primaires inspectées** (4 documents territoriaux réels, famille A) : PV Comité Syndical **Emeraude** 10/02/2025 (bilan 2024), contrat-type **Ecomaison ABJ** v18/04/2025 (SIEDMTO, annexe 3B), délibération **SEROC** CS/2025-028 (reversement soutiens Citeo), délibérations **Tri-Action** CS 02/07/2025.
4. **Réfutation systématique** : contre-requêtes adverses par FCT (toutes NONE ; le 776 €/t plastique Tri-Action confirme indépendamment le barème OCAPEM de la passe précédente).
5. **Causation** : chaîne ENABLER→CAUSE→EFFECT posée ; AXS/CLM/LED SATURATED.

## Faits retenus (FCT, tier ✧, source territoriale inspectée)

- **FCT-001 · Emeraude (PV CS 10/02/2025)** — déchèterie du syndicat : **11 073 t en 2024** ; recettes de revente matériaux **1 201 k€** (pic 1 617 k€ en 2022) ; recettes éco-organismes **réalisées à 138,8 %** de la prévision (+897 k€ Citeo, +75 k€ Ecomaison) ; verre soutenu **18,15 €/t au T4 2024** (28,36 €/t T1 2024 → 10 €/t T1 2025).
- **FCT-002 · Ecomaison ABJ (contrat-type v18/04/2025, SIEDMTO annexe 3B)** — barème par déchèterie : **forfait 2 700 €/contenant >30 m³** (1 350 € si <30 m³), part variable **20 €/t enlèvement**, collecte + recyclage en déchèterie **65 €/t** (19 €/t inertes, 0 €/t ferrailles), zone réemploi **200 €**, communication **100 €** ; versements semestriels sur déclaration.
- **FCT-003 · SEROC (délib. CS/2025-028)** — chaîne de reversement Citeo→syndicat→adhérents : **10 000 €/ambassadeur de tri** (1 ADT/8 000 hab ; 16 ADT pour 130 645 hab), **SCC = +3 % du soutien à la tonne** ; reversement au prorata de la population.
- **FCT-004 · Tri-Action (délib. CS 02/07/2025)** — déchèterie de Bessancourt : **91 461 entrées / 10 443 t en 2024** (hors DT/REP) ; plastique **660 €/t avec extension vs 600 €/t hors extension, revalorisé 776 €/t pour 2025** (corrobore OCAPEM) ; contrat Ecomaison ABJ forfait 2 700 €/contenant.
- **FCT-005 · Captation territoriale (Emeraude, même PV)** — flux développement plastique : **Citeo fera son affaire du surtri/valorisation et en percevra les recettes** (collectivité soutenue 776 €/t) ; machines de déconsigne : la collectivité **« ne perçoit, ni recette matériaux, ni soutien au tri »** sur ces tonnages (8-12 t/an/machine).

## Réfutation (toutes NONE)

Contre-requêtes adverses littérales par FCT avec discriminants numériques : aucune contradiction découverte. Le montant **776 €/t plastique** (Tri-Action 2025) recoupe le barème aval OCAPEM déjà corroboré à la passe précédente → indépendance croisée famille A.

## Chaîne causale (CAU-001→003)

- **ENABLER** : les barèmes €/t et forfaits par déchèterie sont fixés par contrats-types des éco-organismes (Ecomaison ABJ 2 700 €/contenant + 20-65 €/t ; Citeo €/t par matériau) et versés semestriellement.
- **CAUSE** : les collectivités déclarent tonnages et entrées par site (Emeraude 11 073 t ; Bessancourt 91 461 entrées) → **la ventilation par site est reconstituable malgré SINOE vide**.
- **EFFECT** : sur certains flux (déconsigne, flux développement), l'éco-organisme capte les recettes de revente ; la collectivité ne perçoit ni recette matériaux ni soutien au tri.

## Conclusion — ventilation reconstituable, captation confirmée au niveau territorial

**Le contournement fonctionne** : les délibérations territoriales et conventions par EPCI permettent de reconstituer une ventilation concrète par déchèterie (tonnages/entrées × barèmes €/t/forfaits), là où SINOE `LST_TYPE_DECHET` reste vide. Trois EPCI témoins documentés : **Emeraude** (11 073 t, 1 201 k€ revente, soutiens 138,8 %), **Tri-Action** (10 443 t, 91 461 entrées), **SEROC** (mécanique de reversement Citeo→adhérents).

**Cui bono au point de captage** : la collectivité perçoit des soutiens (fixés par contrat-type, versés semestriellement) mais, sur les flux où l'éco-organisme organise le traitement (flux développement) ou sur les dispositifs qu'il ne soutient pas (déconsigne), **la valeur de revente échappe au service public** — documenté mot pour mot au PV Emeraude. Les montants sont volatils (verre 28,36→18,15→10 €/t en un an) et les recettes de revente dépendent de marchés (EMR 175,20→43,10 €/t en 2022).

## Gaps & limites (OPEN)

- **Échantillon limité** : 3 EPCI témoins (Emeraude, Tri-Action, SEROC) — pas de ventilation nationale par site.
- **Annexe 1 des contrats (liste des déchèteries)** : version publiée du contrat-type SIEDMTO sans conditions particulières → la ventilation exacte par site exige les conventions signées (portail TERRITEO).
- **Montants Citeo par déchèterie** : non publiés individuellement (reversement au syndicat, puis prorata population).
- SINOE `LST_TYPE_DECHET` vide : l'opacité de la donnée officielle demeure, contournée mais non comblée.

## Soumission

Faisceau convergent : barèmes contrat-type (T1) + tonnages/entrées déclarés par site + mécanique de reversement + captation documentée (flux développement, déconsigne) → la ventilation par déchèterie est **matériellement reconstituable** et la **captation de la valeur par l'éco-organisme est confirmée au niveau territorial**, pas seulement au niveau national (IGEEDD).
