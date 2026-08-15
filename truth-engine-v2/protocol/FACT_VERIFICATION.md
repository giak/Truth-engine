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
| L1 | FETCHÉ | @FETCH de l'URL primaire + EXCERPT_OK (extrait borné, exact, autonome) | `status:PLAUSIBLE` |
| L2 | ANCRÉ | ANCHOR_OK : SRC-ID + locator exact + URL canonique + date | `status:PLAUSIBLE` |
| L3 | RECOUPÉ | ≥2 sources de **familles de provenance distinctes** (A/B/C/D/E, cf. KERNEL §0 BIAS_PREFLIGHT) affirment le même fait, chacune FETCHÉE | `status:PLAUSIBLE` (en attente de gate EPI) |
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
  intermédiaire). Persistée en `memory_type=note`, `status:PLAUSIBLE`. Jamais CONFIRME seule.
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
  HIT + status:PLAUSIBLE           → traiter comme NON VÉRIFIÉ, reprendre l'échelle L0→L4.
  MISS                             → @WEB → échelle → write-back obligatoire.
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
| SUBLIMATOR Phase 2/3 (v37/v38) | lire Mnemolite (hybrid) au lieu de « DOWN/INDISPONIBLE » ; citer les faits CONFIRME sans re-vérifier (à la demande seulement) |
| skill mnemolite-mem-first | appliquer §6 (consommation) ; le reste du skill fait déjà foi |

## 9. Conformité au canon (double-check 2026-08-15)

- Statuts : `status:CONFIRME` / `status:PLAUSIBLE` uniquement (namespaces réservés : `status`, `fact`,
  `project`, `sys`, `session`, `date`, `source`). Pas de `status:CANDIDATE` (invention corrigée).
- Pas d'expiration automatique des CONFIRME (règle du skill) ; re-vérification à la demande seulement.
- Le **recoupement L3 est un renforcement délibéré** du canon (qui exige 1 source primaire lue) : il
  répond à la demande « croiser les données » et tue la fausse corroboration par copies internes.
- `search_mode:"hybrid"` est supporté ET actif via l'outil MCP (testé 2026-08-15 : `hybrid` renvoie
  `similarity_score` + `embedding_time_ms≈498ms` ; le défaut est `text`, lexical, `similarity_score:null`).
  Toujours passer `search_mode:"hybrid"` explicitement.
- Les namespaces `kernel:` et `acteur:` ne sont PAS réservés (warnings observés) : utiliser des tags
  plats sans « : » pour les domaines/entités.

## 10. Limite honnête (anti-hallucination)

`status:CONFIRME` = « vérifié contre sources primaires, recoupé, daté ». Ce n'est pas « vrai pour
toujours », ni « certain ». Tout consommateur qui présente un fait CONFIRME doit citer sa source et
sa date de vérification, pas la certitude. Si une contradiction apparaît après coup, le fait est
rétrogradé (update_memory → `lifecycle_state=doubt` + note de contradiction), jamais défendu.
