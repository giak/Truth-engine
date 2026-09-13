---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "investigation"
inv_id: "INV-156"
run_id: "20260911-2136-procurement-intermediaires-commissions"
status: "FINAL"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
execution_context: "PROTOCOL_RECONSTRUCTION_NOT_CANONICAL_REGISTRY_APPLY"
as_of: "2026-09-11"
---

# INV-156 — Marchés publics, intermédiaires, commissions et offsets

## Executive forensic verdict

**DELIVERY PASS protocolaire reconstruit.** Le corpus ferme un mécanisme réel et répétable `marché public/stratégique -> intermédiaire/consultant -> avantage illicite -> décideur/influenceur -> assistance ou traitement favorable -> contrat/effet`, mais refuse l'équivalence générique `agent = corruption`, `commission = pot-de-vin` ou `offset = corruption`.

Airbus, Alstom et Siemens fournissent trois familles corporate indépendantes où des partenaires, consultants ou commissions ont servi à acheminer/dissimuler des paiements corruptifs afin d'obtenir des avantages commerciaux ou l'assistance d'agents publics. L'EPPO apporte un mécanisme distinct de trafic d'influence/abus de fonction dans une procédure d'achat croate. En sens inverse, le BIS montre que les offsets sont des mécanismes industriels formels et reportables, tandis que le cadre des fees/commissions distingue des paiements proportionnés pour des services réellement fournis.

## Chaîne causale certifiée

```text
PUBLIC / STRATEGIC PROCUREMENT
-> THIRD PARTY / CONSULTANT / AGENT / COMMISSION
-> PAYMENT / BENEFIT / INDUSTRIAL COMMITMENT
-> [LEGITIMATE SERVICE] OR [ILLICIT CONDUIT / IMPROPER ADVANTAGE]
-> OFFICIAL / INFLUENCER / PROCUREMENT PROCESS
-> ASSISTANCE / PRIVILEGE / AWARD / CONDITIONS
-> ECONOMIC EFFECT
```

### Edges

1. `third-party intermediary -> corrupt payment conduit -> official assistance/business winning` = **SUPPORTED, case-specific**.
2. `official manipulation/trading in influence -> bidder privilege -> procurement award/process effect` = **SUPPORTED, case-specific**.
3. `agent/consultant/commission -> corruption` = **REFUTED as automatic rule**.
4. `offset -> corruption` = **REFUTED as automatic rule**.
5. `illicit payment linked to contract -> counterfactual award causation` = **PARTIAL / case-specific; no generic rule**.
6. `offset mechanism itself -> improper influence` = **UNRESOLVED / RECHECK**.
7. `foreign intermediary -> foreign interference` = **REFUTED as automatic rule**.
8. `representative France/EU prevalence/success denominator` = **GAP**.

## Evidence facts

- **FCT-001** — Airbus third-party bribery scheme: Airbus agreed to a coordinated global resolution after admissions that third-party business partners were used in schemes to offer/pay bribes to decision makers and officials to obtain improper business advantages and win business.
- **FCT-002** — Airbus China business-partner payments: The DOJ described payments to a China business partner intended to be used as bribes to government officials in connection with approvals related to aircraft sales to state-owned/state-controlled airlines.
- **FCT-003** — Airbus multi-jurisdiction resolution: UK SFO and French PNF official channels document coordinated Airbus anti-corruption resolutions; the conduct was treated as corruption/business-winning misconduct, not as ordinary lobbying.
- **FCT-004** — Alstom contracts and bribery: Alstom admitted bribing government officials in multiple countries; in Indonesia bribes were paid in exchange for assistance securing power contracts for state-owned entities.
- **FCT-005** — Alstom consultants as conduits: Alstom used consultants purportedly providing consulting services who actually served as conduits for corrupt payments to government officials.
- **FCT-006** — Tarahan procurement chain: Evidence at trial linked consultants used to conceal bribes to Indonesian officials with assistance securing the $118m Tarahan project.
- **FCT-007** — Siemens public-contract corruption: Siemens entities admitted corrupt payments through purported consultants in exchange for favorable treatment in public contracts or bidding processes in several countries.
- **FCT-008** — Siemens commissions as disguise: In Iraq-related contracts, kickbacks were improperly characterized as commissions to business consultants; in Argentina/Bangladesh/Venezuela purported consultants or conduit entities were used to route corrupt payments.
- **FCT-009** — Croatia procurement manipulation: EPPO reported conviction of a former Croatian minister for abuse of office/authority and trading in influence after actions in a public procurement procedure to ensure a privileged position for a business owner and companies.
- **FCT-010** — Croatia additional conviction: EPPO later reported an additional conviction in the same software procurement case, corroborating the actor/procedure/company chain without generalizing beyond the case.
- **FCT-011** — Offsets defined as industrial compensation: BIS defines defense offsets as industrial compensation arrangements required by foreign governments as a condition of purchasing defense articles/services from foreign suppliers.
- **FCT-012** — Offsets are regulated/reportable: BIS annually collects and reports offset agreements and transactions under the Defense Production Act framework; offset existence is therefore not itself evidence of corruption.
- **FCT-013** — Fee/commission can have legitimate service basis: 22 CFR 130.5 defines fees/commissions tied to securing defense sales but excludes payments solely for specific goods or technical/operational/advisory services when not disproportionate to the value actually furnished.
- **FCT-014** — World Bank Alstom improper consultancy payment: The World Bank reported an improper €110,000 payment to an entity controlled by a former senior government official for consultancy services linked to the Zambia Power Rehabilitation Project.
- **FCT-015** — Award causation ceiling: Official Alstom records establish corrupt payments intended to obtain officials’ assistance in securing contracts; they do not license a generic inference that every award involving an intermediary was counterfactually caused by a payment.
- **FCT-016** — Offset negative control: Because offsets are a recognized, reportable industrial-compensation mechanism, the proposition offset = corruption is refuted as a categorical rule.
- **FCT-017** — Commission negative control: Because regulation expressly distinguishes proportionate payment for actual services from covered fees/commissions, the proposition commission = bribe is refuted as a categorical rule.
- **FCT-018** — Representative denominator gap: The bounded official-source corpus provides strong case evidence but no representative France/EU denominator for the prevalence or success rate of procurement corruption mediated by agents, commissions or offsets.

## Claim registry

- **CLM-001 — SUPPORTED** — Third-party consultants/intermediaries can be used as conduits for corrupt payments tied to public or state-linked contract acquisition.
- **CLM-002 — REFUTED** — The mere presence of an agent, consultant or commission proves bribery.
- **CLM-003 — REFUTED** — A defense offset is inherently a corrupt payment.
- **CLM-004 — SUPPORTED** — A public official can manipulate a procurement procedure to privilege a bidder, producing a case-specific influence/award chain.
- **CLM-005 — NOT_ESTABLISHED_AS_GENERAL_RULE** — Illicit payment linked to a contract automatically proves the payment counterfactually caused the award.
- **CLM-006 — SUPPORTED** — Airbus, Alstom and Siemens provide independent corporate families supporting the intermediary/consultant -> corrupt payment -> business-winning mechanism.
- **CLM-007 — UNRESOLVED** — This run closes an offsets-specific misconduct mechanism independent of agents/commissions.
- **CLM-008 — GAP** — A representative France/EU prevalence or success-rate denominator is established.
- **CLM-009 — SUPPORTED** — Corruption and trading in influence are evidentially separable in procurement analysis.
- **CLM-010 — REFUTED** — Use of a foreign intermediary in a procurement process is automatically foreign interference/ingérence.

## Sources

- **SRC-001** [US DOJ — Airbus global foreign bribery resolution](https://www.justice.gov/usao-dc/pr/airbus-agrees-pay-over-39-billion-global-penalties-resolve-foreign-bribery-and-itar-case) — third-party business partners; bribes to decision makers/officials; business winning
- **SRC-002** [UK SFO — Airbus Deferred Prosecution Agreement landing page](https://www.gov.uk/government/publications/sfo-deferred-prosecution-agreement-with-airbus) — official DPA materials; statement of facts and judgment
- **SRC-003** [Tribunal judiciaire de Paris — communiqués PNF, CJIP Airbus](https://www.tribunal-de-paris.justice.fr/75/communiques-de-presse-0) — official listing of Airbus CJIP communiqué
- **SRC-004** [US DOJ — Alstom guilty plea and $772m criminal penalty](https://www.justice.gov/archives/opa/pr/alstom-pleads-guilty-and-agrees-pay-772-million-criminal-penalty-resolve-foreign-bribery) — consultants as conduits; bribes for assistance securing state-owned-entity contracts
- **SRC-005** [US DOJ — Former senior Alstom executive convicted](https://www.justice.gov/archives/opa/pr/former-senior-alstom-executive-convicted-trial-violating-foreign-corrupt-practices-act-money) — Tarahan $118m; consultants used to conceal bribes
- **SRC-006** [US DOJ — Siemens AG and subsidiaries FCPA resolution](https://www.justice.gov/archive/opa/pr/2008/December/08-crm-1105.html) — consultants/commissions and corrupt payments linked to public contracts/bidding
- **SRC-007** [EPPO — Croatia former minister convicted for procurement abuse/trading in influence](https://www.eppo.europa.eu/media/news/croatia-former-minister-sentenced-two-years-imprisonment-abuse-office-and-authority-2025-06-12_en) — procurement launched; privileged bidder/company; trading in influence
- **SRC-008** [EPPO — Croatia additional conviction in software procurement case](https://www.eppo.europa.eu/media/news/croatia-additional-conviction-investigation-software-purchase-ministry-regional-development-and-eu-2025-09-12_en) — same procurement chain; company-owner conviction
- **SRC-009** [US BIS — Offsets in Defense Trade](https://www.bis.gov/about-bis/bis-leadership-and-offices/SIES/offsets-defense-trade) — offsets are industrial compensation arrangements required as a condition of defense purchases; regulated/reportable
- **SRC-010** [22 CFR 130.5 — Fee or commission (LII rendering of CFR)](https://www.law.cornell.edu/cfr/text/22/130.5) — fee/commission definition and exclusion for proportionate actual goods/services
- **SRC-011** [World Bank — Debarment of Alstom Hydro France / Alstom Network Schweiz](https://www.worldbank.org/en/news/press-release/2012/02/22/enforcing-accountability-world-bank-debars-alstom-hydro-france-alstom-network-schweiz-ag-and-their-affiliates) — improper €110k consultancy payment in World Bank-financed Zambia project

## Contradictory review

The strongest rival is ordinary commercial intermediation. It survives whenever the intermediary supplies specific, proportionate services and no illicit benefit, concealment, official tasking or manipulation of the award process is established. The offset control is stronger still: the mechanism is institutionally recognized and reportable, so corruption must be proved by an additional edge rather than inferred from the offset label.

The strongest positive cases have explicit admissions/convictions describing the purpose of payments and the desired assistance. Even there, the correct ceiling is `corrupt intent/assistance linked to procurement`, not a universal but-for proof that the award could not have occurred absent the payment.

## Scope closure

**Covered by INV-156:** procurement intermediaries/consultants/commissions used as corrupt conduits; procurement trading-in-influence comparator; negative controls for legitimate commission/offset.

**Not closed:** offset-specific improper-influence chain independent of a separate bribe/intermediary; representative France/EU denominator; generic counterfactual success rate.

## RENARD

`NO`. Generic additional bribery cases would be cumulative. A material upgrade requires either (a) a primary-source offset-specific misconduct case that isolates the offset mechanism, or (b) a representative procurement denominator/causal design.

## Canonicality / execution boundary

Le présent livrable a été reconstruit et vérifié dans ce runtime à partir du corpus Library et de sources primaires publiques. Le dépôt local complet du programme n'est pas monté ici. `control.py` est disponible en Library, mais le `INVESTIGATION_REGISTRY.csv` actuellement publié n'inclut pas la branche mécanisme-first `INV-148+`, donc **aucun `control.py apply` canonique n'est revendiqué pour INV-156**. Le verdict `DELIVERY_PASS_R3P1` ci-dessus qualifie le contrat/artefact reconstruit, pas une mutation du registre canonique.

## Runtime accounting

`QRY=11 / SRC=11 / FCT=18 / provenance_families=7`

Persistence: `PASS / eligible=18 / blocked=18 / success=0 / failure=0 / MNEMO_UNAVAILABLE`.
