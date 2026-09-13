# INV-001-R1 — Replay après reconstruction de baseline

**Date :** 2026-09-05  
**Baseline :** `SUBSTACK_BASELINE_2026-08-26`  
**Gel :** 2026-08-26  
**Source :** `substack-online(5).zip`  
**SHA-256 source :** `84f3174f473bbfab6ee55aa516de613b30f35822d8779e6a71afc830bdb5d1b5`

## Verdict

**PASS**

La baseline a été reconstruite sans modifier le contenu des HTML retenus. Le périmètre canonique est désormais explicite et reproductible : **121 articles publiés analysables**, en correspondance 1:1 entre `index.md`, `posts.csv` et `posts/*.html`.

## Contrôles replay

| Contrôle | Résultat |
|---|---:|
| CSV rows | 121 |
| HTML files | 121 |
| Index canonical rows | 121 |
| Unique numeric IDs | 121 |
| CSV stems == HTML stems | True |
| Index post IDs == CSV stems | True |
| Malformed canonical index rows | 0 |
| Non UTF-8 HTML | 0 |
| HTML with NUL | 0 |
| Quasi-empty HTML | 0 |
| Exact duplicate HTML groups | 0 |
| All CSV published | True |

## Résolution des anomalies du FAIL initial

| Objet | Résolution |
|---|---|
| Snapshot non courant | **Gel explicite au 2026-08-26** ; aucune prétention de couvrir les publications ultérieures. |
| `194518266` double HTML | `lingenierie-de-lenclos` canonique ; `3b3` classé `REVISION_ORPHAN`. |
| `191030786.linflation-normative-francaise` | `DRAFT_UNPUBLISHED`, exclu. |
| `181863121.truth-engine-lia-qui-revolutionne` | `DRAFT_EXCLUDED`, brouillon confirmé par l’utilisateur ; exclu définitivement de cette baseline publiée. |
| `206006558.police-francaise-anatomie-dun-systeme` | Réintégré : CSV `is_published=true` + HTML exact. |
| `140803312.coming-soon` | `PLACEHOLDER_EXCLUDED`. |
| 4 entrées index-only | Tracées dans `EXCLUSIONS.csv`, exclues car contenu absent du snapshot. |
| 16 lignes index malformées | Index entièrement régénéré ; **0** ligne canonique malformée. |
| Date `la-fabrique-de-la-menace-comment` | Corrigée à **2026-07-29** selon `posts.csv` ; contrôle public antérieur concordant. |
| Date `machine` | Fixée à **2026-08-02** selon le timestamp export `posts.csv`; l’ancienne valeur manuelle n’est plus canonique. |

## Invariants obtenus

```text
CANONICAL_COUNT = 121
INDEX_COUNT = CSV_COUNT = HTML_COUNT = 121
UNIQUE_SUBSTACK_ID = 121
INDEX_POST_IDS == CSV_POST_IDS == HTML_STEMS
PUBLISHED_ONLY = true
MALFORMED_INDEX_ROWS = 0
EXACT_HTML_DUPLICATES = 0
```

## Limite explicite

Cette baseline est **un snapshot de contenu gelé**, pas un miroir du Substack public au 5 septembre 2026. Les publications postérieures au 26 août doivent appartenir à une baseline ultérieure, pas être ajoutées silencieusement à celle-ci.

## Décision

**INV-001 = CLOSED / PASS.**  
**INV-002 peut passer à READY**, mais ne doit pas être exécutée dans ce replay.

RENARD : **NO** — aucun gap épistémique ne subsiste dans le contrôle structurel ; les objets exclus sont explicitement dispositionnés.


## Addendum disposition

Le 2026-09-05, l’utilisateur a confirmé que `181863121.truth-engine-lia-qui-revolutionne` est un brouillon. Sa disposition passe de `ORPHAN_UNVERIFIED_PUBLICATION` à `DRAFT_EXCLUDED`. Cette clarification ne change aucun invariant structurel ni le verdict **PASS**.
