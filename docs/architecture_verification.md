# Architecture de la vérification des faits (fact-checking)

> Document d'architecture, complément du besoin `docs/besoin_factchecking.md`.
> État réel au 2026-08-19. Remplace l'ancienne « architecture de la boucle de vérification »
> (gate + reviewer local Ollama), obsolète depuis la suppression d'Ollama (2026-08-18).
> Principes : KISS, DRY, YAGNI, Freebuff d'abord, pas de LLM local.

## 1. Deux problèmes orthogonaux

Le chantier « vérification » mélangeait deux natures différentes. Elles sont séparées.

| | Fact-checking (le besoin) | Gate de livraison (orthogonal) |
|---|---|---|
| Vérifie | la vérité : URL vivante, source lue, chiffre/date/% exact, recoupement | la forme : nommage, em-dash, tests, branche, horodatage |
| Exige | un agent avec outils (fetch + lire) | un script déterministe |
| Acteur | agent principal Freebuff + spawn `truth-reviewer` | `verify.py check` / `certify` |
| Référence | ce document + `FACT_VERIFICATION.md` | `tools/verify/README.md` |

Règle : la vérité se vérifie avec un agent à outils ; la forme avec un script.
Un LLM sans outils ne fact-checke pas. Un script ne juge pas la vérité (AGENTS.md §4).

## 2. Acteurs : Freebuff d'abord

```
                       FREEBUFF (runtime hôte)
   ┌───────────────────────────────────────────────────────────────┐
   │  agent principal              sous-agent spawn                │
   │  (KERNEL = fact-checker)      truth-reviewer                  │
   │  outils : web_search,         clean-room, lecture seule,      │
   │  read_url, read_files,        contexte neuf, indépendant      │
   │  MCP Mnemolite                                                 │
   └───────────────────────────────────────────────────────────────┘
          │  fetch + lire + recouper + classer + écrire
          ▼
   Mnemolite (pierre angulaire des données)
```

- **Agent principal Freebuff** : produit l'enquête (KERNEL) ET fact-checke (L0→L4).
  C'est le fact-checker : il fetch, lit, recoupe, classe, écrit.
- **Sous-agent `truth-reviewer`** : second avis indépendant (clean-room, lecture seule),
  spawné quand le runtime expose `spawn_agents`. Non exposé dans cette session : l'agent
  principal joue les deux rôles (limite « auto-juge », §8).
- **Scripts déterministes** : `verify_facts.py` (structure du registre),
  `detect_contradictions.py` (valeurs divergentes), `monitor_urls.py` (URLs mortes),
  `verify.py` (gate de forme). Ils vérifient la STRUCTURE, jamais la VÉRITÉ.

## 3. La chaîne complète : du KERNEL à l'article

Le fait est vérifié UNE fois (au KERNEL), puis circule PAR RÉFÉRENCE (l'id Mnemolite).
L'aval ne refait ni recherche web, ni vérification.

```
KERNEL (investigation)
  §10 CONSTRUCTION   FCT-### = @FETCH + EXCERPT_OK ; tag EPI (texte) + tier (glyphe)
  §13 VERIFICATION   ré-ouvrir les sources ; recoupement ≥2 familles indépendantes
  §19b FACT_WRITEBACK  écrit les ✦/L4 dans Mnemolite ; capture memory_id → mem:
       FACT_REGISTRY_V1 : id|epi|tier|url|familles|date|sujet|valeur|mem
      │
      ▼  (écriture unique, au write-back, après gate 19a PASS)
┌────────────────────── MNEMOLITE (pierre angulaire) ──────────────────────┐
│ status:CONFIRME (L4, ✦)   = « sans question » → cité par read_memory(id) │
│ status:VERIFIE  (L1-L3, ✧) = « vérifié, source unique » → re-questionnable│
│ sans status: / legacy      = candidat L0        → re-vérifier L0→L4       │
└───────────────────────────────────────────────────────────────────────────┘
      │
      ▼  (référence par ID, ZÉRO re-recherche web)
Phase 1 (v36, quintessence) : §2 « Faits atomiques » + EPI:<classe> + mem:<uuid> (verbatim)
Phase 2 (v37, rapport)      : §2 « F-## sous-jacents » propage EPI + mem:
Phase 3 (v38, article)      : read_memory(id) → {source + URL + verbatim + date}
```

## 4. L'échelle de vérification L0→L4 (machine à états)

```
L0 CANDIDAT   assertion LLM (rappel/snippet), aucune URL lue     → rien (pas de write)
   │  @FETCH + EXCERPT_OK (extrait borné, exact, autonome)
   ▼
L1 FETCHÉ     source primaire lue                                → status:VERIFIE
   │  ANCHOR_OK (SRC-ID + locator exact + URL canonique + date)
   ▼
L2 ANCRÉ      source localisée précisément                       → status:VERIFIE
   │  ≥2 familles de provenance indépendantes (A/B/C/D/E), chacune fetchée
   ▼
L3 RECOUPÉ    corroboration par des rôles distincts              → status:VERIFIE
   │  gate EPI = FACT + REFUTATION_SEARCHED (contre-requête, zéro réfutation)
   ▼
L4 CONFIRMÉ   ✦ + status:CONFIRME + verifie-YYYY-MM-DD + hash    → « sans question »
```

Dégradations mécaniques : source unique → ✧ ; URL présente mais non lue → ⁅ ; aucune URL → ❧.
`✦` auto-attribué sans L4 = FAUTE (déclasser en ⁅ ou ❧).

## 5. EPI vs tier (séparation, décidée 2026-08-19)

Deux dimensions distinctes, jamais mélangées dans la colonne `tier`.

```
EPI (nature de l'énoncé, TEXTE)            tier (qualité de source, GLYPHE)
  FACT        observation sourcée           ✦   L4, recoupé ≥2 familles → CONFIRME
  EVIDENCE    pièce, pas le fait lui-même   ✧   L1-L3, source unique → VERIFIE
  INFERENCE   interprétation                 ⁅   URL présente mais non lue
  HYPOTHESIS  conjecture                     ❧   aucune URL
  SPECULATION prédiction
  UNKNOWN     invérifiable

Seul EPI=FACT peut atteindre ✦/L4/status:CONFIRME.
Les statuts épistémiques SYMBOLS.md (⁕ CLAIMED, ⁂ SPECULATED, ⊗ CONTRADICTED, ⊙ PARTIAL)
ne sont PAS des tiers : ils se reportent en EPI texte (⁕→UNKNOWN, ⁂→HYPOTHESIS).
```

## 6. Le registre FACT_REGISTRY_V1 (le lien porteur)

```
<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://url/canonique | A,E | 2024-03-07 | sujet | valeur | <uuid>
FCT-002 | FACT | ✧ | https://url/secondaire | D   | -         | sujet | valeur | <uuid-verifie>
<!-- /FACT_REGISTRY_V1 -->
   id      epi   tier   url                familles  date       sujet   valeur   mem
```

- `mem` = memory_id Mnemolite du fait écrit (`status:CONFIRME` ✦ ou `status:VERIFIE` ✧), renseigné au write-back (§19b), `-` pour les faits non écrits (⁅/❧).
- Lu VERBATIM par Phase 1 (jamais par recherche sémantique) : c'est le lien qui ferme la boucle.
- Règle souple : le bloc n'est exigé QUE pour les runs qui écrivent en Mnemolite (write-back ✦/L4 ou ✧/L1-L3).
- Vérifié par `verify_facts.py` (structure, jamais vérité ; anti-SSRF + HEAD-check + familles + EPI).

## 7. La boucle complète (vue d'ensemble)

```
 ┌──────────────┐   ┌────────────────┐   ┌─────────────────────┐   ┌──────────────────┐
 │  KERNEL      │   │  VÉRIFICATION  │   │  WRITE-BACK         │   │  CONSOMMATION    │
 │  §10-13      │──►│  L0→L4         │──►│  §19b Mnemolite     │──►│  Phase 1/2/3      │
 │  fetch +     │   │  fetch→ancrer→ │   │  status:CONFIRME    │   │  read_memory(id) │
 │  classer     │   │  recouper→EPI  │   │  capture mem:<uuid> │   │  zéro re-fetch   │
 └──────────────┘   └────────────────┘   └─────────────────────┘   └──────────────────┘
        │                   │                      │                        │
        │ écrit le          │ classe EPI +         │ écrit le fait          │ cite {source+URL
        │ registre          │ tier                 │ + source + URL         │ +verbatim+date}
        ▼                   ▼                      ▼                        ▼
   FACT_REGISTRY_V1     ✦✧⁅❧ / EPI texte      Mnemolite               article publié
```

Chaque maillon est mécanique et rejouable. Aucun maillon ne requiert de re-vérifier ce
qu'un maillon amont a déjà enregistré.

## 8. Limites honnêtes

1. **Auto-juge** : l'agent principal produit ET vérifie. Le second avis (`truth-reviewer` spawn)
   n'est pas exposé dans cette session. `status:CONFIRME` = déclaration honnête « j'ai fetché
   et lu », pas une preuve indépendante. Le HEAD-check 200 prouve que l'URL est vivante, pas
   que le contenu appuie l'affirmation : le contenu est vérifié par le fetch (L1), pas par script.
2. **CONFIRME est rare** : un fait à émetteur unique (INSEE, taux de pauvreté) reste ✧/VERIFIE,
   car ✦ exige ≥2 familles indépendantes. Le tier « sans question » couvre une minorité des faits.
   La règle est juste ; la conséquence (la plupart des faits restent « à questionner ») est assumée.
3. **`mem:` ne vaut que pour les prochains runs** : les quintessences existantes restent sans
   `mem:` tant que leur investigation n'a pas été re-vérifiée.

## 9. Backlog : le chantier qui manque

La production (KERNEL) est câblée. La masse existante ne l'est pas.

```
 Mnemolite (total 40 107 mémoires)
 ├── 33 612 conversation  → non factuelles, exclues de la vérification
 └── 6 436 factuelles     → investigation(5 091) + note(1 019) + reference(180)
                            + article(52) + quintessence(94)
        │
        ├── status:CONFIRME  → « sans question », rien à faire
        ├── status:VERIFIE   → re-questionnable, à recouper si cité
        └── sans status: / legacy livre-cst (~3 942 claims, au mieux L0)
             └──► CAMPAGNE DE RE-VÉRIFICATION L0→L4 (par lots, agent principal)
```

La campagne re-vérifie chaque candidat : fetch de la source primaire, ancrage, recoupement,
gate EPI, write-back `status:CONFIRME` / `VERIFIE` / `REFUTE`. C'est de la main-d'œuvre
(agent principal Freebuff), pas du code.

---

## Références

- Besoin : `docs/besoin_factchecking.md`
- Protocole canonique : `truth-engine-v2/protocol/FACT_VERIFICATION.md` (échelle L0→L4, registre)
- Pipeline : `truth-engine-v2/KERNEL.md` (§10, §13, §19b)
- Template de sortie : `truth-engine-v2/output/TEMPLATE.md`
- Ontologie : `truth-engine-v2/definitions/SYMBOLS.md` (§2 statuts épistémiques)
- Gate de forme (orthogonale) : `tools/verify/README.md`
- Agents : `.agents/truth-verifier.ts`, `.agents/truth-reviewer.ts`
- Consommation aval : `tools/engines/sublimator/prompt-v36.md` (Phase 1), `prompt-v37_phase2.md`
  (Phase 2), `prompt-v38_phase3.md` (Phase 3)
