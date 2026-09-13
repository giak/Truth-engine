---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-152"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "POST_RUN_RECLASSIFICATION_PENDING"
updated: "2026-09-11"
---

# RUN_HANDOFF — INV-152

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260911-2109-dollar-clearing-extraterritorialite`
- Deliverable: `2026-09-11_21-09_dollar-clearing-extraterritorialite_INVESTIGATION.md`
- Deliverable SHA-256: `c0faf46891870b89c2767b181f21b02600d15ead6ef310e02e7ffeb0b9b2e2b8`
- Corpus runtime: `QRY=14 / SRC=14 / FCT=17 / provenance_families=5`
- Persistence: `PASS / eligible=17 / blocked=17 / success=0 / failure=0 / fabricated_memory_ids=0`
- Kernel PRE gate: `PASS`
- Kernel DELIVERY gate: `PASS`

## Delta central

INV-152 isole un mécanisme distinct des sanctions/debanking génériques déjà couverts par INV-124 : le contrôle d'une juridiction, d'une monnaie de règlement ou de rails de correspondent banking peut rendre un risque juridique/enforcement étranger matériellement contraignant pour un acteur européen. BNP Paribas ferme un cas d'enforcement exercé avec nexus direct au système financier américain; il ne prouve donc pas à lui seul une extraterritorialité sans nexus. Total/SP11 ferme un cas plus discriminant `secondary-sanctions risk -> retrait/adaptation commerciale d'une entreprise UE`, tandis que Bank Melli/Telekom ferme le rôle autonome du calcul de risque privé : un effet commercial européen peut apparaître sans ordre américain individuel adressé à l'entreprise concernée. Le Blocking Statute et INSTEX ferment une réponse institutionnelle européenne à cette tension. Le corpus ne ferme toutefois ni `adaptation commerciale -> concession souveraine UE`, ni un dénominateur représentatif de fréquence/succès.

## Registre causal certifié

- `transaction dollar / système US -> juridiction/enforcement -> sanction + suspension de clearing -> adaptation bancaire` = **SUPPORTED** — nexus direct au système américain; ne vaut pas preuve d'une théorie purement extraterritoriale sans nexus.
- `contrôle d'accès aux correspondent/payable-through accounts -> conditions/interdiction -> pression sur banque étrangère` = **SUPPORTED** — levier juridique/infrastructurel documenté.
- `risque de secondary sanctions -> exposition financement USD/US -> retrait d'un projet par entreprise UE` = **SUPPORTED** — Total/SP11 fournit le cas borné le plus net.
- `secondary-sanctions risk -> private risk calculus/de-risking -> effet commercial UE sans ordre individuel` = **SUPPORTED_BOUNDED** — Bank Melli/Telekom; médiation privée distincte du commandement étatique.
- `pression extraterritoriale perçue -> Blocking Statute / canal alternatif INSTEX` = **SUPPORTED** — adaptation institutionnelle européenne, pas preuve d'efficacité générale.
- `financial-rail leverage -> specific sovereign EU policy concession` = **UNRESOLVED** — aucune concession souveraine précise causalement fermée dans ce run.
- `representative France/EU success-rate denominator` = **GAP** — aucun dénominateur représentatif identifié dans les 14 sources inspectées.

## Gardes

`DOLLAR_USE != PURE_EXTRATERRITORIALITY`

`LEGAL_REACH != EXERCISED_ENFORCEMENT`

`PUBLIC_ENFORCEMENT != PRIVATE_DE_RISKING`

`PRIVATE_DE_RISKING != STATE_COMMAND`

`COMMERCIAL_ADAPTATION != SOVEREIGN_CONCESSION`

`EXTRATERRITORIALITY != AUTOMATIC_INGERENCE`

## RENARD

`NO` — les gaps résiduels demandent soit un dataset comparatif représentatif, soit une chaîne actor-specific fermant une concession souveraine; davantage de cas génériques de sanctions/compliance serait cumulatif et chevaucherait INV-124.

## Transition attendue

`INV-152 ACTIVE_PRECOLLECTION -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis reclassification mécanisme-first séparée. Aucune investigation suivante n'est lancée par ce handoff.
