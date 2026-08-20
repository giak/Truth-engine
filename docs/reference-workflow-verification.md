# Référence maître : du KERNEL à Mnemolite, workflow de vérification

> Document de référence absolue du workflow. Il répond aux questions récurrentes :
> « où va la donnée ? », « qu'est-ce qui est vérifié ? », « pourquoi tel résultat de recherche ? ».
> Fichiers canoniques complémentaires : `truth-engine-v2/KERNEL.md` (orchestration),
> `truth-engine-v2/protocol/FACT_VERIFICATION.md` (échelle L0-L4 et registre),
> `docs/besoin_factchecking.md` (besoin et brèches), `knowledge.md` (règles projet).
> Écrit après le constat du dossier `investigations/2026-08/2026-08-13_conspiracywatch-info` (2026-08-20).

---

## 1. Le workflow en une page

```text
KERNEL (1 investigation)
   │
   ├──> 1 mémoire Mnemolite de type investigation   (SAUVEGARDE, pas de vérification)
   │        = le markdown final, retrouvé par contexte
   │
   └──> faits + URL du registre de l'investigation
        │
        └──> SYSTÈME DE VÉRIFICATION (fact-checker, L0 → L4)
             │
             ├──> fetch source primaire + extrait verbatim
             ├──> ancrage (URL + locator + date)
             ├──> recoupement (≥ 2 familles indépendantes)
             ├──> gate EPI (FACT uniquement)
             └──> write_memory atomique (type note, status:CONFIRME|VERIFIE)
                  │
                  └──> memory_id rebouclé dans FACT_REGISTRY_V1 (colonne mem:)
                       │
                       └──> consommé en aval : search_memory / read_memory(id), ZÉRO re-recherche
```

### Ce que cela fait, pourquoi, comment

| Étape | Ce que cela fait | Pourquoi | Comment |
|---|---|---|---|
| Sauvegarde investigation | indexe le dossier complet dans Mnemolite | conserver le contexte d'enquête, le raisonnement, les limites | `@MNEMO_S` = `write_memory(memory_type="investigation")` au SAVE (KERNEL §19) ; pas de vérification nécessaire, ce n'est pas un fait |
| Vérification des faits | transforme une recherche web en fait VÉRIFIÉ et persisté | un fait ne se vérifie pas sans lire la source ; le LLM seul hallucine | échelle L0→L4 de `FACT_VERIFICATION.md` §2, par l'agent principal à outils (web_search + read_url + MCP) |
| Write-back | écrit le fait atomique dans Mnemolite | permettre à tout consommateur de s'appuyer dessus sans refaire la vérification | `write_memory(memory_type="note", content="FAIT VÉRIFIÉ : ...", tags=[...])` (KERNEL §19b) |
| Rebouclage | rattache le fait à son registre | fermer la boucle EPI/mem : l'aval lit `mem:<uuid>` verbatim | colonne `mem` du bloc `FACT_REGISTRY_V1`, remplie avec le memory_id retourné (jamais inventé) |
| Consommation | retrouve les faits vérifiés | ne pas refaire le travail de vérification | `search_memory(query, search_mode="hybrid", tags=["project:truth-engine","status:CONFIRME"])` ou `read_memory(id)` via `mem:` |

---

## 2. Les deux rôles distincts de Mnemolite

Ne pas confondre. C'est la source de la plupart des malentendus.

| Rôle | Type de mémoire | Contenu | Vérifié ? | Usage |
|---|---|---|---|---|
| Contexte d'enquête | `investigation` | le dossier markdown complet (analyse, raisonnement, limites, WOLVES) | NON (sauvegarde) | retrouver un dossier, reprendre une piste, lire le raisonnement |
| Fait vérifié | `note` | un fait atomique borné : « FAIT VÉRIFIÉ : ... » + SOURCE + URL | OUI (L1-L4) | citation en aval sans re-recherche ; seule source de `status:CONFIRME` |

### Règles qui en découlent

1. Une mémoire `investigation` ne doit **jamais** porter `status:CONFIRME` : c'est un dossier, pas un fait (`EPI != FACT`).
2. Une mémoire `note` sans `status:` n'est pas un fait vérifié : c'est un lead ou une note de travail.
3. `status:CONFIRME` = L4 : source primaire lue, ancrée, recoupée ≥ 2 familles, EPI=FACT, datée.
4. `status:VERIFIE` = L1-L3 : vérifié mais à re-questionner en aval (source unique, niveau inférieur).
5. `mem:<uuid>` dans un registre = la clé qui relie le fait local au fait Mnemolite ; il se lit verbatim, jamais par recherche sémantique.

---

## 3. Le schéma du fait vérifié (contrat de confiance)

Tout fait FACT écrit à L1-L4 l'est **une seule fois**, avec cette forme (extrait de `FACT_VERIFICATION.md` §4) :

```text
title            = {fait condensé, ≤200 chars, forme interrogable}
content          = "FAIT VÉRIFIÉ : {énoncé exactement borné par l'extrait}
                    SOURCE_ORIGINALE : {url initiale ou -}
                    SOURCE_UTILISÉE : {institution/auteur} ({date})
                    URL : {url canonique}
                    LOCATOR : {locator exact ou NON ÉTABLI}
                    EXCERPT : {extrait verbatim borné + méthode}
                    CROSS-CHECK : {source 2 et famille, ou NON EFFECTUÉ}
                    EPI : FACT
                    VERIFICATION_LEVEL : {L1|L2|L3|L4}
                    UPSTREAM_ID : {identifiant amont ou -}
                    UPSTREAM_KEY : {clé amont ou -}"
memory_type      = "note"
tags             = [ "status:CONFIRME|status:VERIFIE", "source:"+{hash10},
                     "project:truth-engine", {tags domaine SANS « : »} ]
```

Points non négociables :

- L'énoncé écrit est strictement borné par l'extrait : pas de qualificatif causal, temporel ou quantitatif absent de l'extrait.
- L'URL cliquable est obligatoire, jamais un domaine nu.
- `source:{hash10}` = hash de la clé de preuve (URL+locator), pour la déduplication.
- Un fait qui existerait déjà → `update_memory`, jamais un second write (pas de doublon).

---

## 4. Le bloc machine FACT_REGISTRY_V1

Emis par KERNEL §10 dans la CARTE DES PREUVES, **seulement si le run écrit des faits en Mnemolite** (décision tranchée 2026-08-19 : règle souple, la prose exploratoire APPROFONDISSEMENT/GAPS/BLUEPRINT n'en a pas besoin).

```text
<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://url/canonique | A,E | 2024-03-07 | dgsi-effectif | 5000 | <uuid>
FCT-002 | FACT | ✧ | https://url/secondaire | D | - | dgsi-effectif | 5500 | <uuid-verifie>
FCT-003 | FACT | ❧ | - | - | - | - | - | -
<!-- /FACT_REGISTRY_V1 -->
```

Champs : `id | epi | tier | url | familles | date | sujet | valeur | mem`

- `tier` ∈ {✦,✧,⁅,❧} UNIQUEMENT. `✦` = L4 CONFIRME, `✧` = L1-L3 VERIFIE, `⁅` = URL non lue, `❧` = pas d'URL.
- Les statuts épistémiques `⁕ ⁂ ⊗ ⊙` (SYMBOLS.md) vont dans le champ `epi` en texte, jamais dans `tier`.
- `mem` = memory_id réellement retourné par `write_memory` ; `-` pour les faits non écrits.
- `mem:` est le lien porteur : Phase 1 (v36) le lit verbatim, Phase 3 (v38) fait `read_memory(id)` dessus.

---

## 5. La règle de consommation (ne pas refaire les vérifications)

Extrait de `FACT_VERIFICATION.md` §6 :

```text
LECTURE  : search_memory(query, search_mode="hybrid", tags=["project:truth-engine","status:CONFIRME"]) AVANT tout @WEB.
  HIT + status:CONFIRME → citer {source + URL + memory_id}, ZÉRO appel web.
  HIT + status:VERIFIE  → traiter comme NON CONFIRMÉ, reprendre l'échelle L0→L4.
  MISS                  → @WEB → échelle → write-back obligatoire.

RACCOURCI : si un F-## circule avec mem:<uuid> → read_memory(id) DIRECTEMENT.
            ZÉRO re-recherche, ZÉRO re-vérification : le write-back fait foi.
```

### Les pièges de recherche, à connaître par cœur

| Situation | Ce que cela donne | Leçon |
|---|---|---|
| `search_memory` sans `search_mode` | tombe en mode tag | toujours passer `search_mode="hybrid"` |
| Requête avec faute de frappe (ex. « wacfh ») | 50 résultats de bruit, des mémoires « test » | la recherche sémantique ne corrige pas l'orthographe |
| `total` / `has_more` retournés par le serveur | peut être incohérent (total = taille de page, has_more=false alors qu'il reste des résultats) | paginer par offset et ne pas se fier aux métadonnées seules |
| Recherche libre sans tag | mélange faits, investigations, notes de test, bruit | filtrer par tag + `memory_type` + `status:` |
| Filtre `memory_type=quintessence` | 0 résultat pour un dossier dont les quintessences n'ont pas été indexées | une absence n'est pas une preuve d'absence : vérifier l'ingestion |
| `export_memories` | peut échouer sur des mémoires anciennes (schéma `entities` en drift) | l'inventaire complet passe par des recherches taguées, pas par l'export |

---

## 6. Le constat mesuré sur le dossier Conspiracy Watch (2026-08-20)

C'est le cas d'école qui a révélé le décalage entre le workflow théorique et la réalité. Aucune écriture Mnemolite n'a été faite pendant ce constat.

### Ce que contient le dossier

```text
fichiers .md au total                      116
fichiers racine (investigations, etc.)      60
quintessences dans _quintessence/           56
occurrences FCT-### dans les fichiers       ~200
URLs distinctes dans les fichiers          131
```

### Ce que contient Mnemolite pour ce dossier (par tags cumulés)

```text
mémoires uniques trouvées       67
investigation                   63
note                             3
reference                        1
```

- **3 faits atomiques existent** (notes « FCT vérifié : ... », status:CONFIRME, URLs Sénat/Conspiracy Watch). Format antérieur au schéma §3 : pas de `source:<hash>`, pas de `UPSTREAM_ID`, pas de bloc `mem:`.
- **11 mémoires de type investigation portent `status:CONFIRME`** : pollution. Ce sont des dossiers narratifs, pas des faits. À corriger (retirer le tag ou convertir en faits atomiques).
- **0 bloc FACT_REGISTRY_V1 dans les 116 fichiers** du dossier : le registre n'a jamais été émis ni rebouclé pour cette série.
- **0 `mem:<uuid>`** dans les 116 fichiers.
- Aucune mémoire ne porte `investigation:conspiracywatch-info` : l'appartenance au dossier n'est pas taguée.

### Les 3 questions à se poser avant de conclure « il manque des données »

1. **Y a-t-il eu une écriture atomique ?** Une investigation peut être entièrement rédigée sans qu'aucun fait n'ait été écrit dans Mnemolite (la prose n'écrit rien).
2. **Le registre existe-t-il ?** Sans bloc `FACT_REGISTRY_V1` avec `mem:`, il n'y a pas de lien local → Mnemolite.
3. **Est-ce une absence ou une invisibilité ?** Une recherche sémantique ratée ne prouve pas l'absence : vérifier par tag, par `memory_type`, par offset, et par ingestion.

---

## 7. Les décisions déjà tranchées (ne pas re-débattre)

| Décision | Date | Teneur |
|---|---|---|
| Règle souple FACT_REGISTRY_V1 | 2026-08-19 | le registre n'est exigé que pour les runs qui écrivent en Mnemolite, pas pour la prose exploratoire |
| EPI et tier séparés | 2026-08-19 | `epi` = texte, `tier` ∈ {✦,✧,⁅,❧} ; les glyphs épistémiques ne vont jamais dans `tier` |
| `search_mode="hybrid"` obligatoire | 2026-08-15/16 | sans lui, recherche tag-only, zéro similarité sémantique |
| Pas d'expiration automatique des CONFIRME | canonique | re-vérification à la demande seulement |
| Reviewer local Ollama supprimé | 2026-08-18 | un LLM sans outils ne peut pas fact-checker ; gate déterministe seule |
| `mem:` lu verbatim | 2026-08-18 | plus aucune re-recherche sémantique pour un fait portant un memory_id |
| Dédoublonnage au write-back | 2026-08-18 | duplicate → update_memory, jamais un second write |
| Pas de mapping C1 « Confirmé » → status:CONFIRME | 2026-08-16 | le statut legacy ne vaut pas une vérification par fetch |

---

## 7bis. La règle d'enforcement (ajoutée 2026-08-20)

Pour que le workflow ne dépende plus de la discipline de l'agent, un **contrôle déterministe structurel** a été ajouté à la gate (`verify.py` + `.verify/config.json`) :

```text
check_fact_registry

1. tout INVESTIGATION / HYPER_MATRICE / REGISTRE contenant des faits
   (FCT-### ou CARTE DES PREUVES) DOIT émettre un bloc <!-- FACT_REGISTRY_V1 --> ;
2. toute ligne tier ✦/✧ du bloc DOIT porter un memory_id (mem: ou mem:<uuid>) ;
3. ligne mal formée (≠ 9 champs) = violation ;
4. prose sans fait : marqueur explicite NO_FACTS autorisé ;
5. le contrôle vérifie la STRUCTURE seulement, jamais la vérité (AGENTS.md §4).
```

Le check est déclaré dans `.verify/config.json` (section `fact_registry`, `enabled: true`) et tourne dans `verify.py check`/`gate`. Il scanne les dossiers d'investigation datés ; le dossier `2026-08-13_conspiracywatch-info` est exclu temporairement en attendant la remédiation de ses faits, puis l'exclusion sera retirée.

**Constat après activation (2026-08-20)** : 110 violations sur 331 fichiers scannés, tous des investigations legacy sans bloc de registre. C'est le signal attendu : la série Conspiracy Watch n'était pas un cas isolé, c'était la norme. Le check transforme désormais cette absence en échec de gate, donc en travail à faire avant livraison.

## 8. Les brèches ouvertes (état au 2026-08-20, après corrections)

1. **Aucun run réel n'a rebouclé `mem:`** : les 56 quintessences Conspiracy Watch portent 0 `mem:<uuid>` ; les 3 blocs FACT_REGISTRY_V1 du repo (pauvrete-monetaire, trinquier, cas-macron) portent 0 memory_id. Le mécanisme est câblé (et désormais enforced par la gate), jamais exécuté en production.
2. **Facts non écrits** : ~200 occurrences FCT-### dans les investigations Conspiracy Watch, mais seulement 3 faits atomiques en Mnemolite. Le write-back n'a pas suivi la rédaction. (En traitement : remédiation par lots, la matière est dans les markdowns.)
3. ~~**Pollution de tags** : 11 investigations portent `status:CONFIRME`.~~ **CORRIGÉ (2026-08-20)** : 37 mises à jour Mnemolite, 0 investigation restante avec `status:*`, tag nu `confirme` retiré.
4. ~~**Tags non normalisés** : `conspiracy-watch` vs `conspiracywatch`.~~ **CORRIGÉ (2026-08-20)** : les 26 mémoires `conspiracywatch` portent désormais aussi `conspiracy-watch` (0 restante). Reste : ajouter `investigation:<slug>` sur les mémoires dont la provenance dossier est prouvée.
5. **Ancien format** : les 3 notes existantes ne suivent pas le schéma §3 (pas de source hash, pas de UPSTREAM).
6. **Export global cassé** : `export_memories` échoue (champ `entities` en chaînes sur des mémoires anciennes).

### Correction recommandée (à faire quand le chantier sera lancé)

```text
1. normaliser les tags : investigation:conspiracywatch-info + un seul tag domaine
2. corriger les 11 investigations : retirer status:CONFIRME
3. extraire les faits FCT-### + URL des investigations (le SQLite n'est pas nécessaire : la matière est dans les markdowns)
4. vérifier chaque fait L0→L4 (fetch primaire, extrait, locator, familles)
5. écrire chaque fait au schéma §3 (note, status, source hash, UPSTREAM_ID = FCT-###)
6. reboucler mem:<uuid> dans un FACT_REGISTRY_V1 émis dans l'investigation
```

---

## 9. Rappels opératoires

- Avant d'interroger : `get_system_snapshot` ; si DOWN, pas de recherche web ni de conclusion (protocole mem-first).
- Pour retrouver un fait : `search_memory(query, search_mode="hybrid", tags=["project:truth-engine","status:CONFIRME"])`.
- Pour retrouver un dossier : tag `investigation:<slug>` ou `memory_type="investigation"`.
- Pour retrouver une quintessence : il faut qu'elle ait été indexée (type `quintessence`) ; vérifier l'ingestion, pas seulement la recherche.
- Pour lire un fait depuis un registre : `read_memory(id)` avec le `mem:<uuid>` verbatim.
- Jamais d'invention : ni memory_id, ni URL, ni extrait, ni statut.
- Un fait `status:VERIFIE` se cite comme vérifié L1-L3, jamais comme confirmé.
- Un dossier `investigation` ne se cite jamais comme un fait confirmé.
