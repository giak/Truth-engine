# FACT_VERIFICATION v2.10.6 — Échelle de vérification, registre des faits, contrat de confiance

> Protocole canonique. Chargé explicitement par KERNEL §10 (CONSTRUCTION), puis autorité sémantique pour §13 (VERIFICATION) et §19b (FACT_WRITEBACK),
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

Un candidat-fait monte l'échelle. Chaque niveau est mécanique et falsifiable. On enregistre toujours le niveau maximal atteint, jamais une plage : `L2`, et non `L1/L2`. Un fait ne reçoit ✦ et `status:CONFIRME` qu'à L4.

| Niveau | Nom | Condition | Statut Mnemolite résultant |
|--------|-----|-----------|------------------------------|
| L0 | CANDIDAT | assertion LLM (rappel ou snippet), aucune URL lue | rien (pas de write) |
| L1 | FETCHÉ | @FETCH de l'URL primaire + EXCERPT_OK (extrait borné, exact, autonome) | `status:VERIFIE` |
| L2 | ANCRÉ | ANCHOR_OK : SRC-ID + locator exact et rejouable + URL canonique + date | `status:VERIFIE` |
| L3 | RECOUPÉ | ≥2 sources de **familles de provenance distinctes** (A/B/C/D/E, cf. KERNEL §0 BIAS_PREFLIGHT) affirment le même fait, chacune FETCHÉE | `status:VERIFIE` (en attente de gate EPI) |
| L4 | CONFIRMÉ | L3 + gate EPI = FACT + REFUTATION_SEARCHED (≥1 contre-requête explicite) sans réfutation trouvée | `status:CONFIRME` + `verifie-YYYY-MM-DD` |

```
BLOCK_IF[✦ attribué sans L4].  ✦ auto-attribué := FAUTE (déclasser en ⁅ ou ❧).
BLOCK_IF[✦ attribué sans REFUTATION_SEARCHED].  ✦ sans contre-requête explicite := non confirmable, déclasser ✧.
DEGRADE_IF[source unique] → ✧ (tier 2), jamais ✦.
DEGRADE_IF[URL présente mais non lue] → ⁅ ; [aucune URL] → ❧.

Réfutation active (V3 adversarial) : la contre-requête n'est pas « je n'ai rien trouvé », c'est
« j'ai cherché à me faire mentir ». Sans elle, ✦ mesure l'absence passive de contradiction dans les
sources de soutien, pas la recherche active de contre-preuve. `REFUTATION_SEARCHED:{QRY-ID}→{FOUND|NONE}`
est tracé par fait ; `FOUND` interdit ✦ (déclasser ou re-scoper le claim), `NONE` autorise ✦ avec la trace.
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

Chaque fait FACT écrit à L1-L4 l'est une seule fois, avec clé déterministe et niveau maximal explicite :

```
title            = {fait condensé, ≤200 chars, forme interrogable}
content          = "FAIT VÉRIFIÉ : {énoncé factuel exactement borné par l'extrait}\n\n"
                   "SOURCE_ORIGINALE : {url initiale ou -}\n"
                   "SOURCE_UTILISÉE : {institution/auteur} ({date de publication})\n"
                   "URL : {url canonique}\n"
                   "LOCATOR : {locator exact ou NON ÉTABLI}\n"
                   "EXCERPT : {extrait verbatim borné + méthode d'accès}\n"
                   "CROSS-CHECK : {source 2 et famille, ou NON EFFECTUÉ}\n"
                   "EPI : FACT\n"
                   "VERIFICATION_LEVEL : {L1|L2|L3|L4}\n"
                   "UPSTREAM_ID : {identifiant amont ou -}\n"
                   "UPSTREAM_KEY : {clé amont ou -}\n"
memory_type      = "note"
tags             = [ "status:VERIFIE|status:CONFIRME", "source:"+{hash10},
                     "project:truth-engine", {tags domaine/entité SANS « : »} ]
embedding_source = {résumé structuré 200-400 mots : sujet, thèmes, entités, période}  # pour la recherche sémantique
```

Un fait L1 peut être écrit `status:VERIFIE` sans locator L2, mais il ne doit pas être décrit comme ancré. Un fait L2 doit porter son locator ; un fait L3 doit porter les sources et familles distinctes ; un fait L4 doit en plus porter la contre-recherche. L'énoncé écrit doit être réduit à ce que l'extrait établit : un qualificatif temporel, causal ou quantitatif non présent dans l'extrait devient une réserve ou un claim séparé.

Clé de déduplication (`evidence_key`, KERNEL §19b) : `canonical_url + locator` ou `canonical_id` stable. `source:{hash10}` est le hash de cette clé de preuve pour la déduplication ; ce n'est pas un hash du contenu de la page. Un hash de contenu peut être ajouté séparément lorsqu'il est calculable. Duplicate → `update_memory` (jamais de doublon). L'URL **cliquable** est obligatoire, jamais un domaine.

## 4.5 Bloc machine-readable FACT_REGISTRY_V1 (markdown)

Le dossier d'investigation **doit** émettre un bloc déterministe, parsable par script, dans
CARTE DES PREUVES. Une ligne par fait, champs séparés par ` | ` :

```
<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://url/canonique | A,E | 2024-03-07 | dgsi-effectif | 5000 | <uuid>
FCT-002 | FACT | ✧ | https://url/secondaire | D | - | dgsi-effectif | 5500 | <uuid-verifie>
FCT-003 | FACT | ❧ | - | - | - | - | - | -
<!-- /FACT_REGISTRY_V1 -->
```

Champs : `id` (FCT-###) | `epi` (FACT|EVIDENCE|INFERENCE|HYPOTHESIS|SPECULATION|UNKNOWN) |
`tier` (✦✧⁅❧) | `url` (http(s), `sha256:<64 hex>` pour artefact local, ou `-`) | `familles` (A-E séparées par virgule, ou `-`) | `date` (optionnel) |
`sujet` (optionnel : slug sujet+attribut, ex. `dgsi-effectif`, `squarcini-dst-periode`, ou `-`) |
`valeur` (optionnel : valeur normalisée — nombre, date, chaîne courte — ou `-`) |
`mem` (memory_id Mnemolite du fait écrit `status:CONFIRME` (✦) ou `status:VERIFIE` (✧), ou `-` pour les faits non écrits ⁅/❧).

`tier` n'admet QUE {✦,✧,⁅,❧}. Les statuts épistémiques de SYMBOLS.md (⁕ CLAIMED, ⁂ SPECULATED, ⊗ CONTRADICTED, ⊙ PARTIAL) ne sont PAS des tiers : les reporter en `epi` texte (⁕→UNKNOWN, ⁂→HYPOTHESIS), jamais dans la colonne `tier`.

`url` admet deux formes de localisateur : une URL http(s) (source web, HEAD-checkée) ou
`sha256:<64 hex>` (artefact local téléchargé, ex. vidéo, audio). Le hash est un localisateur de
contenu, inviolable et insensible à la pourriture d'URL. ✧ requiert l'une des deux formes ;
✦ requiert une URL http(s) (jamais un hash seul : il ne prouve ni recoupement ni vivacité).

Le champ `mem` est renseigné au write-back (KERNEL §19b) avec le memory_id retourné par `write_memory`,
pour chaque fait écrit ✦/L4 (`status:CONFIRME`) et ✧/L1-L3 (`status:VERIFIE`) ; `-` pour les faits non écrits (⁅/❧). Phase 1 (v36) le lit **verbatim** depuis le bloc,
jamais par recherche sémantique : c'est le lien porteur qui ferme la boucle EPI/mem (P6b).

Ce bloc est ce que `tools/verify_facts.py` vérifie de façon **déterministe** (anti-SSRF, HEAD-check,
compte des familles, gate EPI). Le script vérifie la STRUCTURE, jamais la VÉRITÉ du contenu
(cf. AGENTS.md §4 : « un script déterministe ne doit pas traiter du texte produit par un LLM »).

`tools/detect_contradictions.py` (P5) exploite `sujet`/`valeur` : même sujet normalisé + valeurs
divergentes → signal pour la gate humaine (le script ne tranche pas quelle valeur est vraie).

```bash
python3 tools/verify_facts.py <investigation.md> [--offline]   # exit 0 ok / 1 violations / 2 aucun registre
python3 tools/detect_contradictions.py [chemin...] [--json]    # exit 0 ok / 1 contradictions / 2 aucun registre
```

### 4.5b Provenance machine-readable `FCT_SOURCE_MAP_V1`

KERNEL émet exactement une ligne par FCT :

```text
## FCT_SOURCE_MAP_V1
FCT-001 | SRC-002,SRC-003
FCT-002 | SRC-004
FCT-003 | -
```

Le mapping contient uniquement les **sources de support** du fait. Les contre-sources restent dans TRACE/CONTRADICTION.
Chaque ligne SRC canonique porte un `fam:<token>` explicite. Le champ `families` de `FACT_REGISTRY_V1` est dérivé
exactement de l’union des familles des SRC mappés : il n’est jamais saisi ou compté à la main. Une source web mappée
à un fait ✦/✧ doit avoir été FETCHée. Le `url` canonique du FCT doit correspondre à au moins une source mappée.
`✦` exige au moins deux familles indépendantes **dérivées** ; une famille unique est compatible avec `✧`.

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
violation. La distinction auto/manuel est une marque **humaine** portée par l'extrait
(date + méthode), rejouable mais non vérifiable par script sans accès au contenu : c'est l'invariant
de discipline, pas de code (AGENTS.md §4).

## 4.7 Récupération alternative et dérive de contenu

Cette section s'applique si un outil échoue, si l'URL est déplacée ou si la page ne porte plus le
claim. Séparer l'accès de la preuve :

```text
ACCÈS   : ALIVE | REDIRECTED | HEAD_BLOCKED | DEAD | UNREACHABLE | UNKNOWN
PREUVE  : SUPPORTS | CONTRADICTS | PARTIAL | NO_ASSERTION | DRIFT | GAP
```

1. **Échec d'outil != verdict.** `403`, `401`, `405`, `429`, timeout, JavaScript, paywall et résultat
   vide de `web_search` ne prouvent ni source morte, ni donnée absente, ni claim réfuté. `DEAD` exige
   un constat de disparition ou d'erreur définitive.
2. **Fallback borné.** Après `read_url`, essayer l'URL canonique ou sa redirection, puis un navigateur
   ou Chrome headless. Si la page est déplacée, modifiée ou insuffisante, lancer jusqu'à trois requêtes
   ciblées : citation ou titre exact, entité + claim + date, domaine officiel. Arrêter dès qu'une source
   de remplacement lisible est trouvée ; sinon classer `GAP`.
3. **Lecture manuelle.** Si seul l'utilisateur ou un navigateur interactif lit la page, conserver un
   extrait verbatim borné avec URL, titre ou section, date et méthode `(fetché manuel)`. « La page
   fonctionne » ne constitue pas `EXCERPT_OK` sans cet extrait.
4. **Remplacement, dérive et portée.** Une nouvelle URL est une nouvelle pièce : conserver URL initiale,
   URL utilisée, motif du remplacement, émetteur, date, locator et extrait séparément. Une page actuelle qui
   ne mentionne plus un fait ancien produit `DRIFT` ou `NO_ASSERTION`, jamais `CONTRADICTS` si la page n'est
   pas exhaustive. Ne jamais écraser silencieusement une citation ou un `memory_id`. Le claim écrit doit
   être strictement borné par l'extrait : la provenance du candidat ne transfère pas ses qualificatifs au fait.
5. **Preuve et écriture.** Snippet, résultat de recherche, mémoire Mnemolite, synthèse et copie interne
   sont des leads, pas des extraits primaires. Sans `EXCERPT_OK`, le candidat reste L0 ; sans `ANCHOR_OK`,
   il reste L1 au maximum. `VERIFIE` est autorisé à L1-L3 ; `CONFIRME` exige L4. Aucun write-back à L0.

Trace minimale :

```text
URL_ORIGINALE | URL_UTILISÉE | REASON_REPLACED | ACCESS_METHOD | ACCESS_STATE | ACCESSED_AT | LOCATOR | EXCERPT | EVIDENCE_STATE | NEXT_ACTION
```

## 4.8 Import contrôlé d'un candidat structuré hors dossier KERNEL

Ce profil sert uniquement à tester ou importer exceptionnellement un candidat atomique provenant d'un
corpus structuré externe (par exemple SQLite, CSV ou registre local). Il ne remplace pas le dossier KERNEL
ni sa gate de livraison.

Avant `write_memory`, le manifeste local doit contenir :

```text
UPSTREAM_ID + UPSTREAM_KEY stables, ou justification de leur absence
EPI=FACT
SOURCE_REF_ORIGINALE + SOURCE_REF_UTILISÉE + motif du remplacement éventuel
EXCERPT_OK + ACCESS_METHOD + ACCESSED_AT
VERIFICATION_LEVEL = niveau maximal unique (L1, L2, L3 ou L4)
LOCATOR exact si L2+
FAMILIES et contre-requête si L3/L4
```

Le write-back est autorisé seulement si ces champs sont cohérents. Il écrit `status:VERIFIE` à L1-L3 et
`status:CONFIRME` à L4, capture l'identifiant réellement retourné, puis reboucle `UPSTREAM_ID → memory_id`
dans le manifeste. Le compteur avant/après est contrôlé. Une erreur de niveau, de portée du claim, de
locator ou d'identifiant bloque l'écriture et laisse le candidat `NOT_VERIFIED`.

Un import hors KERNEL ne doit pas être présenté comme une investigation certifiée. Pour un dossier KERNEL,
la séquence §19a PRE_GATE puis §19b PERSIST_REBIND/DELIVERY_GATE reste obligatoire.

## 5. Contrat de confiance (ce que `status:CONFIRME` garantit, et ne garantit pas)

**Garantit** :
1. la source primaire a été **lue** (fetch), pas juste listée ;
2. le fait est **recoupé** par ≥2 familles de provenance **indépendantes** ;
3. il porte une **date de vérification** et un **hash source** rejouable ;
4. il est classé **FACT** (pas inference ni hypothèse) ;
5. il est **atomique** (pas une chaîne causale, pas une thèse).

**Ne garantit pas** : l'infaillibilité, l'absence de contradiction future, la causalité, l'intention.

## 6. Règle de consommation et warm route

Deux contextes doivent rester séparés : consommation aval et construction d'un FCT KERNEL courant.

```
CONSOMMATION_AVAL (article/synthèse, aucune revalidation demandée) :
  search_memory(... status:CONFIRME) avant toute discovery.
  HIT + status:CONFIRME → citer {source + URL + memory_id}; zéro recherche de redécouverte.
  HIT + status:VERIFIE  → ne pas présenter comme CONFIRME; re-vérifier si le livrable exige une preuve courante.
  MISS                  → discovery/fetch normal.

KERNEL_NEW_OR_UPDATE (fait décisif/current FCT) :
  HIT + canonical URL/key → WARM_ROUTE; utiliser mémoire comme pointeur non fiable, puis @FETCH direct de l'URL canonique.
  NEVER: transformer le HIT mémoire en preuve courante ou en INSPECTED.
  @WEB seulement si URL absente/morte/stale/hors-scope, pour corroboration indépendante, réfutation, nouvel objet ou gap matériel.
  Un web-backed ✦/✧ courant exige toujours un @FETCH observé dans le run courant (INSPECTED_TRACE_OK).

RACCOURCI ARTEFACT AMONT : un `mem:<uuid>` permet `read_memory(id)` direct au lieu de search_memory, mais ne remplace pas le @FETCH
si ce fait devient un FCT décisif d'une nouvelle investigation KERNEL.
```

**Pas d'expiration automatique** de la mémoire : `status:CONFIRME` conserve son historique. La fraîcheur de preuve est néanmoins une propriété du run courant :
une revalidation explicite, un fait évolutif/contesté, une source morte ou tout FCT web-backed courant impose la route KERNEL ci-dessus.

Principe performance : **MEMORY saves discovery, never inspection.**

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
| KERNEL §19b | FACT_WRITEBACK : CONFIRME seulement pour EPI=FACT+L4 ; VERIFIE pour EPI=FACT+L1-L3 ; PRE_GATE §19a doit déjà être PASS ; sérialiser `WRITEBACK_EXECUTION_V1`, `WRITEBACK_ROW` structuré et le `memory_id` retourné dans `FACT_REGISTRY_V1.mem` |
| SUBLIMATOR Phase 1 (v36) | préserver ✦ ET reporter EPI + memory_id du fait CONFIRME |
| SUBLIMATOR Phase 2/3 (v37/v38) | v37 propage `EPI`+`mem:` des quintessences vers le rapport (§2 « F-## sous-jacents ») ; v38 consomme `read_memory(id)` sur les faits `mem:<uuid>` au lieu de re-chercher (P6b) |
| skill mnemolite-mem-first | appliquer §6 (consommation) ; le reste du skill fait déjà foi |

`WRITEBACK_EXECUTION_V1` est de la métadonnée d'exécution, pas une preuve. Il contient exactement une ligne par FCT éligible et uniquement des compteurs observés :

```text
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
```

Un succès sans `memory_id` retourné est un échec de writeback et ne peut jamais laisser `FACT_REGISTRY_V1.mem=-` tout en comptant `success:1`.

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


## Warm-memory canonical update (2.10.6)

A current revalidation of an already hydrated canonical fact does not create a second canonical note. Runtime `MEMORY_WRITE_MODE_V1` decides mechanically:

- `origin_memory_id` present => `UPDATE` that memory record after PRE_GATE PASS;
- no origin memory => `WRITE` a new canonical record;
- current returned memory id is rebound into `FACT_REGISTRY_V1.mem`;
- provenance fields remain lineage metadata, never evidence.

This changes persistence mechanics only. Current ✦/✧ still require current evidence and INSPECTED_TRACE_OK.


## Legal-status source hierarchy (2.10.6)

For a fact whose material proposition is the legal identity, adoption, applicability, expiry, amendment or replacement of a regulation/directive/law:

- prefer the exact official legal act or official institutional procedure page as mapped support;
- when an accessible official family-A source exists, a ✦ legal-status fact must include at least one such source; secondary analysis alone is insufficient for ✦;
- canonical fact content should name the operative instrument identifier when it is material to distinguish extension, replacement, amendment or a new act;
- a remembered legal basis that is missing, superseded or contradictory forces `RECHECK`, never silent `REUSE`;
- when an official summary/landing page conflicts with the operative legal act or a newer official correction/procedure page, treat the stale summary as historical evidence and resolve the current proposition from the operative/newer official source; never serialize the conflict as “unresolved” merely because both pages are official.

This rule exists to prevent an old memory from preserving a correct date while silently carrying an obsolete legal basis.
