# QUERY TEMPLATES v2.1 — Evidence-object search

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

## §2 Counter and falsification routes

```text
{claim} criticism OR rebuttal OR methodological limitation
{entity} audit OR court OR inspector report OR conflict of interest
{event} competing explanation OR alternative cause
{statistic} definition denominator revision limitations
{document} correction retraction amended version
{subject} opposition/watchdog/local-language terms
```

Search both the strongest counterargument and evidence that could falsify it. `NONE_FOUND` is valid after a logged reasonable search.

## §3 Money, network, time and omission

```text
MONEY:   {entity} funder owner subsidy contract donation lobbying disclosure
NETWORK: {person/entity} board adviser employer partner register
TIME:    {event} timeline archive announcement deletion correction
OMIT:    {metric} methodology exclusions denominator full dataset
BIO:     {person} mandate board interests declaration vote decision
```

For network edges, seek a registry, filing, meeting record or direct statement. A co-occurrence page is only a lead.

## §4 Geographic and linguistic diversification

- Search affected locality first, then involved actors, neighbors/comparables and relevant outside perspectives.
- Use native names, transliterations, local date formats and jurisdiction-specific repository terms.
- Preserve original URL/text and note translation path.
- Do not add distant sources merely to raise EDI; material relevance is required.

## §5 Execution

```text
1. Start: entity + evidence object + date/jurisdiction.
2. @WEB for discovery; @FETCH the exact useful URL.
3. Validate object, author, date/version, scope and upstream provenance.
4. Deduplicate by evidence object/family.
5. If noisy/empty, load OPTIMIZATION.md.
6. Stop when material claims are resolved/saturated or access is exhausted; log gaps.
```

_Canonical authority: domain query templates._
