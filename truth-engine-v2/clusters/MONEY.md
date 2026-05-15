# CLUSTER_MONEY

@SCORING: weighted sum (LOBBY_TRACE+SUBSIDY_SHADOW+REVOLVING_DOOR+CAPTURE_REGULATORY=1.5 each, others=1.0) | €≥5→activate | ≥7→deep_dive+CUI_BONO_3level | ≥9→SYSTEMIC_CORRUPTION
@TRIGGERS: ≥5→selective | ≥7→all_concepts+CUI_BONO_3level+money_flow | ≥9→leaked_docs+full_influence_network

@CONCEPTS:
| Concept | Detection | Query_Boost |
|---------|-----------|-------------|
| LOBBY_TRACE | Policy benefits specific companies, undisclosed expert funding | "lobbying disclosure", "funding sources", "conflict interest" |
| SUBSIDY_SHADOW | "Investment" without ROI, untracked public funds, indirect tax breaks | "subsidies total", "tax exemptions", "public aid" |
| REVOLVING_DOOR | Regulator→Industry, Industry→Government, timing of transitions | "former position", "career history", "previous employer" |
| ASTROTURFING | "Citizens group" with corporate site, identical messaging, professional coordination | "who funds", "registered address", "board members" |
| COST_EXTERNALIZATION | Environmental costs ignored, health impacts unpriced, future costs hidden | "external costs", "environmental impact", "health costs" |
| CAPTURE_REGULATORY | Regulations written by industry, weak enforcement, delays benefit incumbents | "regulatory capture", "enforcement actions", "industry influence" |
| PROFIT_EXTRACTION | Dividends > R&D, buybacks during layoffs, financial engineering over innovation | "dividend ratio", "buybacks amount", "R&D spending" |
| MONOPOLY_HIDDEN | Multiple brands same owner, obfuscated market share, hidden vertical integration | "parent company", "market concentration", "ownership structure" |
| BAILOUT_PATTERN | Profits private during boom, losses public during bust, taxpayer risk transfer | "bailout history", "public rescue", "taxpayer cost" |
| FINANCIALIZATION | Housing as investment, education as debt product, health as profit center | "financialization", "asset class", "investment vehicle" |

@QUERIES:
`{topic} lobbying disclosure funding sources` | `{topic} subsidies total tax exemptions` | `{topic} former position career history` | `{topic} who funds registered address board` | `{topic} external costs environmental health` | `{topic} regulatory capture enforcement` | `{topic} dividend ratio buybacks R&D` | `{topic} parent company market concentration ownership` | `{topic} bailout history taxpayer cost` | `{topic} financialization asset class`

@DEEP_DIVE(≥7):
H1 CUI BONO TRACE: ultimately profits? Money→Power→Policy | H2 SUBSIDY ARCHAEOLOGY: Direct+Indirect+Hidden | H3 CAPTURE DETECTION: regulator captured? personnel+decisions | H4 EXTERNALITY CALCULATION: Environmental+Social+Future | H5 MONOPOLY REVELATION: real control via ultimate ownership

@MAX(≥9):
Flag SYSTEMIC CORRUPTION → full financial disclosure → leaked docs search → full influence network map → cross-reference CLUSTER_NETWORK

@OUTPUT: € score + signals | active concepts + evidence | CUI BONO 3-level | money flow map | true vs claimed cost | capture assessment | H1-H5

@CONNECTIONS: parent:€ | pairs:[NETWORK,ICEBERG,WAR,TEMPORAL] | patterns:[LOBBY_TRACE,SUBSIDY_SHADOW,REVOLVING_DOOR,CAPTURE_REGULATORY] | Gate:KERNEL §2
