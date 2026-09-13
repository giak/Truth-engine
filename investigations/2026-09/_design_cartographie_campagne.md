# DESIGN — Cartographie de la campagne d'investigation 2026-09

> Conception validée le 2026-09-05. Périmètre : dossier `investigations/2026-09/` seul.
> Tous les livrables et l'outillage sont regroupés dans ce dossier.

## 1. Objectif

Produire un **état des lieux exhaustif et régénérable** de la campagne « Influence &
Ingérences sur les démocraties » menée dans `investigations/2026-09/`, capable de :

1. **Inventorier les sujets traités** — chaque dossier, son état, son capital probatoire ;
2. **Détecter les gaps** — angles morts, investigations planifiées non exécutées, faits ✧ à élever,
   actions en attente, questions causales ouvertes ;
3. Servir de **boussole pour lancer les prochaines investigations**.

Règle d'honnêteté absolue : le script **n'invente rien**. Il agrège ce qui existe et
étiquette systématiquement ce qui manque (dossier hors-protocole, vide, non certifié).

## 2. Livrables et emplacements (tout dans investigations/2026-09/)

| Fichier | Rôle |
|---|---|
| `mapper_cartographie.py` | Script Python 3, offline, déterministe, sans réseau |
| `campagne_classes.json` | Table de mapping 7 classes (heuristique + surcharge manuelle) |
| `campagne_cartographie.json` | Données agrégées machine-readable (généré) |
| `campagne_cartographie.md` | Rapport lisible (généré, régénéré à chaque exécution) |
| `_design_cartographie_campagne.md` | Ce document |

## 3. Données d'entrée (lues par le script)

Balayage du dossier `2026-09/` :

- **Runs KERNEL certifiés** : dossier contenant `*_INVESTIGATION.md`, `*_RUN_STATE.json`,
  `*_MNEMO_SNAPSHOT.json`, `*_CERTIFICATION.json`, `*_INPUT.txt`, `*_NARRATIVE.tmp.md`
  (observé : ~24 dossiers sur 39, mais **le script compte, il ne suppose pas**) ;
- **Fichiers .md isolés** (hors protocole, observés : 6) ;
- **RUN_STATE / parts de dossiers partiels** ;
- **Dossiers vides** (observés : 8, tous `uk-brexit-*`).

Structure de sortie dans `campagne_cartographie.json` :

```json
{
  "generated_at": "…",
  "source_dir": "investigations/2026-09",
  "counts": { "dirs": 0, "with_run_state": 0, "with_full_kernel": 0, "empty_dirs": 0 },
  "facts_total": { "n": 0, "tiers": {"✦": 0, "✧": 0, "⁅": 0, "❧": 0}, "with_url": 0, "with_memory_id": 0 },
  "subjects": [ { "dir", "title", "kind": "kernel|partial|bare|empty",
                  "run_id", "n_facts", "tiers", "n_leads", "n_actions",
                  "actions_pending", "classes": [] } ],
  "facts": [ { "key", "value", "tier", "families", "url", "memory_id",
               "origin_run", "subject_dir" } ],
  "matrix_classes": { "transactionnelle": ["dir1", …], … },
  "gaps": { "empty_dirs": [], "bare_md": [], "facts_candidates_elevation": [],
            "actions_pending": [], "evidence_gaps": [] },
  "runs_topology": [ { "run_id", "subject_dir", "facts_n", "leads_n" } ]
}
```

## 4. Structure du rapport `campagne_cartographie.md`

| § | Contenu |
|---|---|
| §1 Vue d'ensemble | nb dossiers, nb runs certifiés, totaux faits par tier, nb URLs, nb memory_id |
| §2 Inventaire des 39 sujets | tableau : dossier / type / état / nb faits / tiers / classes |
| §3 Atlas des faits | les faits agrégés (tier, familles, URL, memory_id, run d'origine) |
| §4 Matrice 7 classes × dossiers | croisement visible des classes couvertes |
| §5 Gaps & leads | les 5 catégories de gaps (voir §6) |
| §6 Topographie des runs | chaîne des vagues (runs 1-20, élévations seconde-vague / vague3) |

## 5. Mapping aux 7 classes

Taxonomie de référence : classes issues du dossier fondateur
`2026-09-05_cartographie-mecanismes-influence-democraties` :

`transactionnelle` · `informationnelle` · `lobbying` · `reseau` · `etrangere_etatique` ·
`coercitive` · `effet_asymetrie`

**Méthode, en deux volets :**

1. **Heuristique automatique** : grille de mots-clés par classe, appliquée au nom du dossier +
   aux champs `leads` / `claims` / `axes` / `facts[*].key` du RUN_STATE. Le script marque chaque
   attribution `auto:true` et le **score de confiance** de la correspondance.
2. **Surcharge manuelle** (`campagne_classes.json`) : mapping explicite pour les cas ambigus.
   L'entrée manuelle **prime** sur l'auto. La table manuelle est éditée à la main au premier
   passage de validation humaine.

**Limite assumée** : le mapping auto est heuristique, signalé comme tel — jamais présenté
comme une vérité certifiée. Le rapport expose la part auto vs manuelle dans §4.

## 6. Dérivation des gaps (règles explicites)

| Règle | Condition | Type de gap |
|---|---|---|
| G1 | Dossier vide (0 fichier) | `planifie_non_execute` |
| G2 | Dossier avec uniquement des .md (pas de RUN_STATE) | `hors_protocole` (sujet connu, faits non certifiés) |
| G3 | Fait avec `tier == ✧` | `candidat_elevation` |
| G4 | Action avec `status == PENDING` dans RUN_STATE | `action_pending` |
| G5 | Entrée CAU avec `status == GAP` ou `gap_type == EVIDENCE_GAP` | `question_ouverte` |
| G6 | Classe ne mappant qu'0 ou 1 dossier | `angle_mort_classe` |
| G7 | Lead non-saturé (`status != SATURATED`) | `lead_a_traiter` |

## 7. Contraintes

- Python 3, stdlib uniquement, aucun appel réseau, aucune dépendance MCP/MnemoLite.
- Déterministe : même entrée → même sortie (tri stable, horodatage seul non déterministe).
- Ne modifie **aucun** fichier d'investigation existant (lecture seule).
- Le script scande **uniquement les sous-dossiers** de `2026-09/`. Les fichiers de niveau racine
  (ex. `2026-09-05_seconde-vague-faits-non-confirmes.md`) ne sont pas des investigations : ils ne
  sont pas scannés comme sujets, mais peuvent être référencés dans la topographie (§6).
- Le script **ignore ses propres sorties** (`campagne_cartographie.*`) — il n'agrège jamais
  l'agrégat.
- Les schémas de sortie ne ré-inventent pas KERNEL : le script **lit** les RUN_STATE qui suivent
  déjà le schéma canonique de `tools/runtime/run_state.py`.

## 8. Vérification

- Exécution sur le dossier réel → contrôler que les comptes du rapport correspondent à
  l'inventaire manuel : 39 dossiers, ~24 runs certifiés, 167 faits connus (119 ✦ / 48 ✧) —
  **chiffres indicatifs à recouper à la génération**.
- Ré-exécution → sortie identique (hors horodatage).
- La matrice §4 et les gaps §5 font l'objet d'une **validation humaine** au premier passage
  (surcharge de mapping), puisque la détection des angles morts conditionne les prochaines
  investigations.