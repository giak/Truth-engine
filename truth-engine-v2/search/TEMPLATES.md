# QUERY TEMPLATES v2.8 — Auditable investigation-first search

Templates are starting points. Replace placeholders, use the subject’s language and shorten until results are precise. Search for evidence objects, not confirmation of a preferred story.

## §1 Domain routes

| Domain | Direct objects to seek | Query forms |
|---|---|---|
| Political/public | law, vote, budget, hearing, audit, declaration | `{entity} {act} vote/report/budget filetype:pdf`; official legislative register |
| Legal | operative text, docket, filing, judgment | `{case/law} judgment/docket/full text`; court database |
| Corporate | filing, accounts, beneficial owner, contract, court record | `{company} annual report/filing`; `{company} contract/lawsuit/owner` |
| Economic | dataset, method note, budget, trade/tax series | `{indicator} dataset methodology`; `{jurisdiction} budget csv/pdf` |
| Scientific/health | protocol, article, data, registry, review | `{topic} DOI/protocol/trial registry`; `{claim} systematic review` |
| Conflict/geopolitical | treaty, order, imagery, log, contemporaneous record | `{event} official document/archive`; `{location date} imagery/report` |
| Social/humanitarian | census/survey microdata, definitions, local testimony | `{population} dataset methodology`; `{event} local testimony` |
| Technical | source, commit, spec, RFC, advisory, configuration | `{product version} source/spec/advisory`; `{bug} commit/issue` |
| Historical | archive, original correspondence, contemporaneous record | `{event/person} archive original document {year}` |
| Media/narrative | full transcript, original post/video, correction history | `"{exact phrase}"`; `{speaker date} transcript`; archived URL |

Institutional repositories can contain direct evidence, but their interpretations remain claims. Always classify per fact.

## §2 Investigation axes

Use these routes for `OBJECT_INVESTIGATION`; adapt them to the jurisdiction and object. One query may serve several axes, but a source-audit result cannot silently stand in for them.

| Axis | Objects to seek | Compact query stems |
|---|---|---|
| SCOPE_HISTORY | definitions, boundaries, chronology, versions, comparisons, denominators | `{object} definition history timeline methodology`; `{object} comparison by period/context` |
| EVIDENCE_CASES | data, instances, records, experiments, judgments, audits, filings or primary artifacts | `{object} dataset evidence case record`; `{entity/event} exact document` |
| RESOURCES_FLOWS | money, data, material, authority, access, transfers and beneficiaries | `{entity/object} funding data access transfer`; `{resource} source recipient amount volume` |
| MECHANISMS | process, rule, incentive, enabling condition, competing cause | `{object} mechanism process system failure`; `{object} competing explanation` |
| ACTORS_RELATIONS | entities, governance, dependencies, meetings, appointments, interests, typed relations | `{decision/event} participants relations`; `{entity} role interests dependency register` |
| RULES_CONTROLS | rules, constraints, standards, oversight, tests, detection, correction and response | `{object} rule control audit test evaluation`; `{entity/system} duty response outcome` |
| IMPACT_RESPONSIBILITY | distribution, loss/benefit, affected populations, documented decisions/actions | `{object} impact evaluation cost beneficiaries`; `{decision} signatory vote implementation` |
| COUNTER_HYPOTHESES | negative cases, effective controls, alternative mechanisms, disconfirming data | `{object} decline effective prevention evaluation`; `{claim} alternative explanation rebuttal` |

When public-integrity/corruption is applicable, seek judgments/case files, procurement records, audits, declarations, registers, enforcement statistics and control evaluations. Recorded offences, perceptions, modeled macro-losses, diversion and overcharge remain different measures; never substitute them silently.

## §3 Counter and falsification routes

```text
{claim} criticism OR rebuttal OR methodological limitation
{entity} audit OR court OR inspector report OR conflict of interest
{event} competing explanation OR alternative cause
{statistic} definition denominator revision limitations
{document} correction retraction amended version
{subject} opposition/watchdog/local-language terms
```

Search both the strongest counterargument and evidence that could falsify it. `NONE_FOUND` is valid after a logged reasonable search.

## §4 Money, network, time and omission

```text
MONEY:   {entity} funder owner subsidy contract donation lobbying disclosure
NETWORK: {person/entity} board adviser employer partner register
TIME:    {event} timeline archive announcement deletion correction
OMIT:    {metric} methodology exclusions denominator full dataset
BIO:     {person} mandate board interests declaration vote decision
```

For network edges, seek a registry, filing, meeting record or direct statement. A co-occurrence page is only a lead.

## §5 Geographic and linguistic diversification

- Search affected locality first, then involved actors, neighbors/comparables and relevant outside perspectives.
- Use native names, transliterations, local date formats and jurisdiction-specific repository terms.
- Preserve original URL/text and note translation path.
- Do not add distant sources merely to raise EDI; material relevance is required.

## §6 Execution

```text
1. Start: entity + evidence object + date/jurisdiction.
2. @WEB for discovery; @FETCH the exact useful URL.
3. Validate object, author, date/version, scope and upstream provenance.
4. Link each executed QRY/SRC to affected AXS `ATTEMPT_IDS`; record result/perimeter in REQUEST_LOG.
5. Deduplicate by evidence object/family.
6. If noisy/empty, load OPTIMIZATION.md.
7. Stop LEAD_AUDIT when its material claims resolve/saturate; this does not stop OBJECT_INVESTIGATION.
8. Stop only when every LED is terminal and every applicable AXS meets canonical SATURATED/GAP semantics; a bare status without auditable attempts cannot close an axis.
```

_Canonical authority: domain query templates._
