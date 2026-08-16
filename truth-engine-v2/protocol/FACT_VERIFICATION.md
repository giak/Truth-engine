# FACT_VERIFICATION — Échelle de vérification, registre des faits, contrat de confiance

> Protocole canonique. Se branche sur KERNEL §10 (CONSTRUCTION), §13 (VERIFICATION), §19a (FACT_WRITEBACK),
> et sur le skill global `mnemolite-mem-first`. Consommé en aval par SUBLIMATOR Phase 1/2/3.
> But unique : transformer une recherche web en fait VÉRIFIÉ, le persister dans Mnemolite,
> et permettre à tout consommateur de s'appuyer dessus sans refaire la vérification.

## 0. Principe : la vérité est un processus enregistré, pas une certitude

Aucun fait n'est « sûr » au sens absolu. Le maximum atteignable, et le seul garant exploitable, est :

> un fait **tracé** (URL primaire lue), **daté** (verifie-YYYY-MM-DD), **recoupé** (≥2 familles de provenance
> indépendantes), **classé** (FACT, pas inference), et **rejouable** (extrait verbatim + hash source).

La confiance aval porte sur CE PROCESSUS enregistré, pas sur l'LLM. Un fait `status:CONFIRME`
n'est pas « infaillible » : il est « vérifié contre sources primaires à telle date ». C'est la seule
garantie honnête, et c'est elle qui permet la non-re-vérification en aval.

## 1. Règle zéro : le fait vient du fetch, jamais de la mémoire paramétrique

```
NEVER: produire un FCT-### depuis le rappel (recall) du LLM, un snippet, ou une copie interne.
MUST : tout FCT-### provient d'un @FETCH (lecture effective de l'URL) produisant un EXCERPT_OK.
```

Toutes les erreurs observées (dates Squarcini, CNIL 5/19 déc, art. 89 al. 4/5, interceptions
judiciaires/sécurité, DGSI 5 500 cible vs 5 000 réel) sont du **rappel plausible** déguisé en fait.
Un snippet Google ou une phrase « qui sonne juste » n'est jamais une source : c'est un candidat L0.

## 2. L'échelle de vérification (machine à états, L0 → L4)

Un candidat-fait monte l'échelle. Chaque niveau est mécanique et falsifiable. Un fait ne reçoit ✦
et `status:CONFIRME` qu'à L4.

| Niveau | Nom | Condition | Statut Mnemolite résultant |
|--------|-----|-----------|------------------------------|
| L0 | CANDIDAT | assertion LLM (rappel ou snippet), aucune URL lue | rien (pas de write) |
| L1 | FETCHÉ | @FETCH de l'URL primaire + EXCERPT_OK (extrait borné, exact, autonome) | `status:VERIFIE` |
| L2 | ANCRÉ | ANCHOR_OK : SRC-ID + locator exact + URL canonique + date | `status:VERIFIE` |
| L3 | RECOUPÉ | ≥2 sources de **familles de provenance distinctes** (A/B/C/D/E, cf. KERNEL §0 BIAS_PREFLIGHT) affirment le même fait, chacune FETCHÉE | `status:VERIFIE` (en attente de gate EPI) |
| L4 | CONFIRMÉ | L3 + gate EPI = FACT + aucun contre-exemple trouvé dans les sources fetchées | `status:CONFIRME` + `verifie-YYYY-MM-DD` |

```
BLOCK_IF[✦ attribué sans L4].  ✦ auto-attribué := FAUTE (déclasser en ⁅ ou ❧).
DEGRADE_IF[source unique] → ✧ (tier 2), jamais ✦.
DEGRADE_IF[URL présente mais non lue] → ⁅ ; [aucune URL] → ❧.
```

## 3. Gate EPI (classification, obligatoire avant tout write-back)

```
EPI := FACT != EVIDENCE != INFERENCE != HYPOTHESIS != SPECULATION != UNKNOWN
```

- **FACT** : observation sourcée, directement vérifiable, non interprétée (« le 7 mars 2025, X est
  condamné à 4 ans dont 2 ferme »). Seul FACT peut atteindre L4 / `status:CONFIRME` / ✦.
- **EVIDENCE** : pièce qui étaye un fait mais n'est pas le fait lui-même (un extrait, un chiffre
  intermédiaire). Persistée en `memory_type=note`, `status:VERIFIE`. Jamais CONFIRME seule.
- **INFERENCE / HYPOTHESIS / SPECULATION** : interprétation, prédiction, conjecture. Persistées avec
  `lifecycle_state=doubt`. **Jamais CONFIRME, jamais ✦, jamais citées comme fait en Phase 3.**
- **UNKNOWN** : invérifiable → pas de write, log GAP.

```
NEVER: écrire une mémoire `status:CONFIRME` pour un objet EPI != FACT.
```

## 4. Registre des faits Mnemolite (schéma unique, « registre des faits »)

Chaque fait L4 est écrit une seule fois, avec clé déterministe :

```
title            = {fait condensé, ≤200 chars, forme interrogable}
content          = "FAIT VÉRIFIÉ : {énoncé factuel exact}\n\n"
                   "SOURCE : {institution/auteur} ({date de publication})\n"
                   "URL : {url canonique}\n"
                   "EXCERPT : {extrait verbatim borné}\n"
                   "CROSS-CHECK : {source 2, famille de provenance}\n"
                   "EPI : FACT\n"
memory_type      = "note"
tags             = [ "status:CONFIRME", "verifie-YYYY-MM-DD",
                     "source:"+{hash10}, "project:truth-engine", {tags domaine/entité SANS « : »} ]
embedding_source = {résumé structuré 200-400 mots : sujet, thèmes, entités, période}  # pour la recherche sémantique
```

Clé de déduplication (`evidence_key`, KERNEL §19a) : `canonical_url + locator` ou `hash`.
Duplicate → `update_memory` (jamais de doublon). L'URL **cliquable** est obligatoire, jamais un domaine.

## 4.5 Bloc machine-readable FACT_REGISTRY_V1 (markdown)

Le dossier d'investigation **doit** émettre un bloc déterministe, parsable par script, dans
CARTE DES PREUVES. Une ligne par fait, champs séparés par ` | ` :

```
<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://url/canonique | A,E | 2024-03-07 | dgsi-effectif | 5000
FCT-002 | FACT | ✧ | https://url/secondaire | D | - | dgsi-effectif | 5500
FCT-003 | FACT | ❧ | - | - | - | - | -
<!-- /FACT_REGISTRY_V1 -->
```

Champs : `id` (FCT-###) | `epi` (FACT|EVIDENCE|INFERENCE|HYPOTHESIS|SPECULATION|UNKNOWN) |
`tier` (✦✧⁅❧) | `url` (ou `-`) | `familles` (A-E séparées par virgule, ou `-`) | `date` (optionnel) |
`sujet` (optionnel : slug sujet+attribut, ex. `dgsi-effectif`, `squarcini-dst-periode`, ou `-`) |
`valeur` (optionnel : valeur normalisée — nombre, date, chaîne courte — ou `-`).

Ce bloc est ce que `tools/verify_facts.py` vérifie de façon **déterministe** (anti-SSRF, HEAD-check,
compte des familles, gate EPI). Le script vérifie la STRUCTURE, jamais la VÉRITÉ du contenu
(cf. AGENTS.md §4 : « un script déterministe ne doit pas traiter du texte produit par un LLM »).

`tools/detect_contradictions.py` (P5) exploite `sujet`/`valeur` : même sujet normalisé + valeurs
divergentes → signal pour la gate humaine (le script ne tranche pas quelle valeur est vraie).

```bash
python3 tools/verify_facts.py <investigation.md> [--offline]   # exit 0 ok / 1 violations / 2 aucun registre
python3 tools/detect_contradictions.py [chemin...] [--json]    # exit 0 ok / 1 contradictions / 2 aucun registre
```

## 4.6 Source primaire non fetchable automatiquement (HEAD/GET bloqués)

Certaines sources primaires bloquent les requêtes automatisées : **Légifrance répond 403 au HEAD
ET au GET** (constaté 2026-08-16). L'URL est **vivante** (`classify_url` → `head_blocked`), mais le
contenu n'est pas lisible par le bot. Ce n'est ni `alive` confirmé, ni `dead` : c'est `head_blocked`.

Règles :

1. **Jamais `dead`** : un 403/405/429 n'est pas une source morte. Ne pas déclencher la re-vérification.
2. **Fetch manuel obligatoire pour L1** : pour qu'un fait sourcé sur une telle source atteigne L1
   (« fetché »), un humain (ou un outil à contexte navigateur) **lit la page** et fournit l'extrait
   verbatim. Cet extrait porte le marqueur `(fetché manuel)` + date d'accès, au lieu de `(fetché auto)`.
3. **`tier` inchangé** : un fetch manuel compte comme « fetché ». Le fait peut donc rester `✦`/`✧`
   selon le recoupement (§7), et n'est pas rétrogradé `⁅`.
4. **`⁅` seulement si illisible** : si la source n'est lisible ni par bot ni manuellement (paywall,
   JS requis, accès refusé), alors le fait est réellement non fetché → `⁅`, et ne peut atteindre `✦`.
5. **EXCERPT** : toujours indiquer la méthode — `EXCERPT (fetché auto)` / `EXCERPT (fetché manuel,
   <date>)` / `(non fetché)`.

Conséquence déterministe : `verify_facts.py` traite 403 comme `head_blocked` (ni vivant ni mort), sans
violation — c'est correct. La distinction auto/manuel est une marque **humaine** portée par l'extrait
(date + méthode), rejouable mais non vérifiable par script sans accès au contenu : c'est l'invariant
de discipline, pas de code (AGENTS.md §4).

## 5. Contrat de confiance (ce que `status:CONFIRME` garantit, et ne garantit pas)

**Garantit** :
1. la source primaire a été **lue** (fetch), pas juste listée ;
2. le fait est **recoupé** par ≥2 familles de provenance **indépendantes** ;
3. il porte une **date de vérification** et un **hash source** rejouable ;
4. il est classé **FACT** (pas inference ni hypothèse) ;
5. il est **atomique** (pas une chaîne causale, pas une thèse).

**Ne garantit pas** : l'infaillibilité, l'absence de contradiction future, la causalité, l'intention.

## 6. Règle de consommation (aval : ne pas refaire les vérifications)

```
LECTURE  : search_memory(query, search_mode="hybrid", tags=["project:truth-engine", "status:CONFIRME"]) AVANT tout @WEB.
  HIT + status:CONFIRME            → citer {source + URL + memory_id}, ZÉRO appel web.
  HIT + status:VERIFIE            → traiter comme NON CONFIRMÉ, reprendre l'échelle L0→L4 (monter à L4 = CONFIRME).
  MISS                             → @WEB → échelle → write-back obligatoire.

RACCOURCI (artefact amont porteur) : si un F-## circule déjà avec `mem:<uuid>` (quintessence §2,
rapport Phase 2), l'aval n'appelle PAS search_memory : il appelle `read_memory(id)` DIRECTEMENT →
{source + URL + citation verbatim + verifie-date}. ZÉRO re-recherche, ZÉRO re-vérification : le
write-back fait foi. C'est la boucle EPI/mem qui ferme Phase 1 → 3 (P6b).
```

**Pas d'expiration automatique** (règle canonique `mnemolite-mem-first`) : un fait `status:CONFIRME`
n'est jamais automatiquement périmé. On re-vérifie **à la demande seulement** : fait contesté, donnée
nouvelle contradictoire, source défunte (URL morte) → re-fetch puis `update_memory` (nouvelle verifie-date).

## 7. Règle d'indépendance du recoupement (anti-propagation)

```
2 URL du même émetteur := 1 source. Exemple vérifié 2026-08-16 : Légifrance et Service-Public sont
tous deux édités par la DILA (Direction de l'information légale et administrative, Premier ministre)
→ 1 seul émetteur, 1 famille A. Deux URLs du même émetteur ne sont PAS une corroboration, quel que
soit leur nombre.
Copies internes (article + quintessence + blueprint + synthèse) := 0 source.
Le recoupement L3 exige ≥2 FAMILLES de provenance DISTINCTES (A/B/C/D/E), chacune fetchée indépendamment.

`✦` (L4) = recoupé par ≥2 RÔLES distincts (ex. officiel + audit indépendant, ou officiel + académique).
Un fait sourcé uniquement à des sources officielles (famille A), même à 2 institutions différentes, reste
`✧` : ce n'est pas un échec, c'est le tier honnête d'un fait à perspective unique. `✦` n'est pas « mieux
sourcé », c'est « recoupé à travers des rôles différents ».
```

La cohérence interne n'est jamais une preuve : c'est une erreur copiée N fois.

## 8. Points de câblage (où cette spec s'exécute)

| Où | Ce qui change |
|----|---------------|
| KERNEL §10 | FCT-### construit depuis @FETCH+EXCERPT_OK, avec champ EPI ; ✦ réservé à EPI=FACT+L4 ; ÉMETTRE le bloc FACT_REGISTRY_V1 |
| tools/verify_facts.py | vérificateur déterministe du bloc (anti-SSRF + HEAD-check + familles + gate EPI) |
| tools/monitor_urls.py | moniteur périodique d'URLs mortes (P4) : scanne les registres, trie dead/unsafe/unreachable/head_blocked, déclenche la re-vérification |
| tools/detect_contradictions.py | détecteur de contradictions (P5) : même sujet normalisé + valeurs divergentes → signal pour la gate humaine |
| KERNEL §13 | VERIFICATION exige le recoupement L3 (≥2 familles) pour ✦ ; source unique → ✧ |
| KERNEL §19a | inchangé (déjà correct) ; gate : n'écrire CONFIRME que pour EPI=FACT+L4 |
| SUBLIMATOR Phase 1 (v36) | préserver ✦ ET reporter EPI + memory_id du fait CONFIRME |
| SUBLIMATOR Phase 2/3 (v37/v38) | v37 propage `EPI`+`mem:` des quintessences vers le rapport (§2 « F-## sous-jacents ») ; v38 consomme `read_memory(id)` sur les faits `mem:<uuid>` au lieu de re-chercher (P6b) |
| skill mnemolite-mem-first | appliquer §6 (consommation) ; le reste du skill fait déjà foi |

## 9. Conformité au canon (double-check 2026-08-15)

- Statuts : `status:CONFIRME` (L4) / `status:VERIFIE` (L1-L3). **Vocabulaire serveur réel** constaté
  2026-08-16 : CONFIRME, DOUTE, REFUTE, VERIFIE. Le serveur rejette `status:PLAUSIBLE` (statut inconnu)
  — drift corrigé : L1-L3 s'écrivent désormais `status:VERIFIE`. Namespaces réservés : `status`, `fact`,
  `project`, `sys`, `session`, `date`, `source`. Pas de `status:CANDIDATE` (invention corrigée).
- Pas d'expiration automatique des CONFIRME (règle du skill) ; re-vérification à la demande seulement.
- Le **recoupement L3 est un renforcement délibéré** du canon (qui exige 1 source primaire lue) : il
  répond à la demande « croiser les données » et tue la fausse corroboration par copies internes.
- `search_mode:"hybrid"` est supporté ET actif via l'outil MCP (testé 2026-08-15 : `hybrid` renvoie
  `similarity_score` + `embedding_time_ms≈498ms` ; sans paramètre, la recherche est lexicale,
  `similarity_score:null`). Toujours passer `search_mode:"hybrid"` explicitement.
- **Fix serveur (P7) FAIT 2026-08-16** : le défaut `search_mode: str = "tag"` a été changé en
  `"hybrid"` dans le code source Mnemolite (`/home/giak/Work/MnemoLite`, commit `b4be1f2`) —
  `server.py:1231` et `tools/memory_tools.py:810` — puis le conteneur `mnemo-mcp` redémarré.
  Vérifié live : une recherche sans `search_mode` renvoie `metadata.search_mode="hybrid"` +
  `similarity_score` (embedding_failed:false). Le code est **monté en volume** (`./api:/app`) donc
  pas de rebuild d'image requis pour la prise d'effet. `tools/lint_search_mode.py` reste le
  garde-fou client (exit 0 = tous `hybrid`).
- Les namespaces `kernel:` et `acteur:` ne sont PAS réservés (warnings observés) : utiliser des tags
  plats sans « : » pour les domaines/entités.

## 10. Limite honnête (anti-hallucination)

`status:CONFIRME` = « vérifié contre sources primaires, recoupé, daté ». Ce n'est pas « vrai pour
toujours », ni « certain ». Tout consommateur qui présente un fait CONFIRME doit citer sa source et
sa date de vérification, pas la certitude. Si une contradiction apparaît après coup, le fait est
rétrogradé (update_memory → `lifecycle_state=doubt` + note de contradiction), jamais défendu.

## 11. Réconciliation avec le corpus legacy `livre-cst` (2026-08-16)

Le livre (`project:book`) porte un corpus hérité tagué `livre-cst` (schéma `source-chatgpt-csv` +
`source-web-recherche`, produit par `book/book/audit-apex-v8/archive/index_csv_to_mnemolite.py`).
Ses enregistrements classent les claims dans le **corps** (champs `Statut canonique` et
`Classe source`), **sans tag `status:`**, sans `source:<hash>`, sans `verifie-YYYY-MM-DD`.

### 11.1 Le constat qui interdit le mapping naïf

Le `Statut canonique` legacy est une **classification éditoriale produite par un LLM lisant les
atlas** (`source-chatgpt-csv`), **pas** une vérification par fetch de la source primaire. Un
`C1 — Confirmé` n'a ni EXCERPT, ni preuve de fetch, ni recoupement ≥2 familles : il équivaut au
mieux à un **L0 CANDIDAT** avec une source revendiquée.

> Règle cardinale : **`C1 — Confirmé` ≠ `status:CONFIRME`.** Mapper C1 → CONFIRME réintroduirait
> exactement la confiance auto-attribuée sans fetch que toute cette spec combat. Le corpus legacy
> est une **couche candidate**, consommable seulement après re-vérification par l'échelle L0→L4.

### 11.2 Table de mapping `Statut canonique` → verdict FACT_VERIFICATION

Distribution mesurée sur le CSV source (backup 2026-07-23, 3 942 lignes T-code) :

| `Statut canonique` legacy | Verdict | tag `status:` | EPI | Action |
|---|---|---|---|---|
| `C1 — Confirmé` (523) | CANDIDAT | — (pas de write) | — | re-fetch → L0→L4 |
| `C2 — Confirmé à périmétrer` (84) | CANDIDAT | — | — | re-fetch + fixer le périmètre |
| `C3 — Plausible / à tester` (724) | HYPOTHESIS | — | HYPOTHESIS | `lifecycle_state=doubt` |
| `C4 — Non établi / preuve insuffisante` (488) | UNKNOWN | — | UNKNOWN | pas de write |
| `C5 — Faux / invalide` (790) | REFUTE | `status:REFUTE` | FACT (réfuté) | citable **uniquement comme faux** |
| `C6 — Bloqué / source absente` (32) | UNKNOWN | — | UNKNOWN | pas de write, log GAP |
| `WEB` / `WEB — Source externe à arbitrer` (44/393) | CANDIDAT | — | — | arbitrer → re-fetch |
| `ENFANCE*` / `LOOP — à arbitrer` (546) | CANDIDAT | — | — | arbitrer → re-fetch |

Seuls deux mappings sont **sûrs en direct** : `C5 — Faux` → `status:REFUTE` (signal négatif réel)
et `C6`/`S0` → pas de write (source absente). Tout le reste exige le passage par l'échelle.

### 11.3 Table `Classe source` → famille de provenance

| `Classe source` legacy | Famille FACT_VERIFICATION |
|---|---|
| `S0 — Absente` (1 551) | aucune (pas de write) |
| `S1 — Interne / registre` (211) | INTERNE — **non indépendant** (0 source) |
| `S2 — Externe secondaire` (220+) | secondaire (C média / D ONG / E académique selon l'émetteur) |
| `S3 — Primaire / officielle` (696+) | A (officiel) |

`S1 — Interne / registre` est le piège du corpus : un claim sourcé au registre interne du livre n'est
pas une corroboration (même émetteur que le manuscrit). C'est l'équivalent de la règle §7 « copies
internes = 0 source ».

### 11.4 Consommation (comment lire le corpus legacy)

```
LEGACY : search_memory(query, search_mode="hybrid", tags=["livre-cst"])   # PAS de filtre status:
  → lire `Statut canonique` + `Classe source` + `Source` dans le corps
  → mapper via §11.2/§11.3 (ou tools/classify_legacy.py)
  → C5 → citer comme faux (status:REFUTE) ; SINON → re-vérifier via l'échelle L0→L4
  → `Source` legacy (URL) = indice de re-vérification, JAMAIS preuve de fetch.
```

Le filtre P3 (`status:CONFIRME`) ne remonte **pas** le legacy : c'est correct, le legacy n'est pas
confirmé. Le legacy se lit via `livre-cst` seul, puis est re-vérifié et **réécrit** sous le schéma
canonique §4 (nouvelle mémoire `status:*`, jamais mutation rétroactive du legacy).

`tools/classify_legacy.py` applique §11.2/§11.3 de façon déterministe (parse des champs structurés
legacy, jamais la prose LLM) :

```bash
python3 tools/classify_legacy.py [--json] <fichier-legacy.md...>   # ou contenu via stdin
```
