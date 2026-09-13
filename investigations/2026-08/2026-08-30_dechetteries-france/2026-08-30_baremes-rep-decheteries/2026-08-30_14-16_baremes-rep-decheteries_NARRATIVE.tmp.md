# Passe KERNEL — Barèmes REP : suivre l'argent dans les déchèteries (cui bono)

**Run** : 20260830-1416-baremes-rep-decheteries · **As-of** : 2026-08-30 · **Mode** : INVESTIGATION · **Complexité** : COMPLEX

## Question pilote

> Cui bono : qui capte la valeur économique des flux accueillis en déchèterie, mesurée par les barèmes (€/t ou forfaits) des soutiens REP versés aux collectivités ?

## Méthode

1. **Mémoire d'abord** (`MNEMO_Q`, mémoire saine 200-healthy, probe NONE) — pas d'état pré-restauré, run neuf.
2. **Axes** (`AXS-001` barèmes réels €/t/forfaits par filière ; `AXS-002` qui capte la valeur/économie de la reprise).
3. **Sources primaires inspectées** (familles A et D) : barème aval Citeo OCAPEM 2025, Convention EcoDDS (annexe 3), délibération Ecomaison, rapport IGEEDD §4.3.3, cadre REP ecologie.gouv.
4. **Réfutation systématique** : contre-requêtes adverses posées pour chaque FCT (aucune contradiction trouvée ; Citeo corroboré indépendamment par >3 sources).
5. **Causation** : chaîne ENABLER→CAUSE→EFFECT posée, AXS/CLM/LED SATURATED.

## Faits retenus (FCT, tier ✧, source inspectée)

- **FCT-001 · Citéo (barème aval OCAPEM 2025)** — soutien par tonne recyclée : Acier **73 €/t**, Aluminium **470 €/t**, PCNC **177 €/t**, PCC **352 €/t**, PCM **107 €/t**, Plastique **776 €/t**, Verre **8 €/t** ; valorisation organique papier **80 €/t**. Corroboré indépendamment (AMORCE barème G, délibération Tri-Action).
- **FCT-002 · EcoDDS (convention, annexe 3)** — soutien annuel fixe par déchèterie (forfaitaire + variable) sel tonnage : Cat A (>48 t) **3 413 €** ; B (24–48 t) **1 895 €** ; C (12–24 t) **1 334 €** ; D (<12 t) **923 €** + communication **0,03 €/hab**.
- **FCT-003 · Ecomaison — mobilier & équipements (délibération SGC)** — soutien collecte déchèterie **24,4 €/t** ; recyclage EA en collecte non séparée **140 €/t** ; part forfaitaire déchèterie **1 525 €/an** ; soutien information **0,01 €/hab** ; enlèvement non conforme **0 €/t**.
- **FCT-004 · IGEEDD (rapport 2024, §4.3.3)** — les éco-organismes deviennent **propriétaires des déchets** par leurs contrats avec les opérateurs et **captent le produit de la revente des matériaux**, privant la collectivité/l'opérateur ; pouvoir de structuration **supérieur** à celui des opérateurs.
- **FCT-005 · Cadre REP** — deux modèles de financement : **contributif/financier** (l'éco-org reverse des soutiens à la collectivité collectrice) vs **opérationnel** (l'éco-org garde les fonds, contractualise ses propres prestataires).

## Réfutation (toutes NONE)

Queries adverses littérales posées par FCT : aucune source contradictoire découverte. Le montant Citeo (73/470/177/352/107/776/8 €/t) est **retrouvé identique dans 3 sources indépendantes** → corroboration croisée famille A.

## Chaîne causale (CAU-001→003)

- **ENABLER** : les éco-organismes REP collectent les éco-contributions des producteurs et utilisent les déchèteries comme points de captage des flux.
- **CAUSE** : par contrats avec les opérateurs, l'éco-organisme devient propriétaire des déchets et vend les matériaux traités.
- **EFFECT** : cette propriété prive la collectivité de la revente et structure le marché de la reprise au profit de l'éco-organisme.

## Conclusion — qui capte la valeur ?

La déchèterie est un **point de captage**. La collectivité exploite/collecte (coût supporté), reçoit des soutiens **hétérogènes et jugés nettement insuffisants** (audition AN, IGEEDD), et **perd une part de la valeur de revente des matériaux** captée par l'éco-organisme — lui-même financé par les producteurs par éco-contributions (~6 Md€/an), le tout payé au bout de la chaîne par l'usager via TEOM/REOM + éco-participation. **Le bénéficiaire structurel est l'éco-organisme** (propriété des déchets, pouvoir de structuration), avec l'asymétrie documentée IGEEDD.

## Gaps & prochaines requêtes (OPEN)

- **LST_TYPE_DECHET SINOE vide sur 100 % des sites** → impossibilité de croiser les flux réellement acceptés par site avec les soutiens.
- **Barèmes €/t « par site » non publiés** (le barème national existe, la ventilation territoriale par site non).
- **DEEE** : reprise sans frais ; montant €/t net non publié par site.
- PMCB Valobat / Ecominero : barèmes officiels détaillés à confirmer.

## Soumission

Faisceau d'indices → convergence : cross-corroboration Citeo + 2 modèles REP + propriété IGEEDD pointent collectivement vers une **captation de la valeur par les éco-organismes**, au détriment de la collectivité exploitante.