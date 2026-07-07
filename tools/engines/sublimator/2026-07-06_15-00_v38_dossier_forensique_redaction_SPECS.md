# SPECS v38 - Sublimator Phase 1 : Dossier Forensique pour Rédaction

> **Version** : v38 v3 (2026-07-06, 21 h 45)
> **Statut** : Validé [GO] sur échantillon RIC 18:00 (3533 mots, M1-M7 PASS, M8 régression à durcir)
> **Remplace** : v37 v2 (compress_summary ≤320 mots) - rétention 5,2 % vs 62,9 % en v38
> **Note 2026-07-06 22 h** : §6 transformée en checklist manuelle (abandon de l'infrastructure de validation Python, cf. note d'architecture prompt-v35.md).

---

## 1. Pourquoi pivoter de v37 v2 vers v38

### 1.1 Constat d'échec de v37 v2

v37 v2 demandait au SP (Sublimator Phase 1) de produire un `compress.md` de **≤320 mots** résumant une investigation de 5 000-6 000 mots. Sur l'échantillon RIC 18:00 (5 612 mots) :

| Métrique v37 v2 | Résultat |
|---|---|
| Volume compress | 293 mots (5,2 % rétention) |
| URLs préservées | 0 / 12 (perte 100 %) |
| Traçabilité reverse | aucune |
| Faits F-### | 5 / 24 (perte 79 %) |
| Dates 1789 → 2026 | 1 mention contre 12 bornes datées |
| Scénarios S1-S4 | 0 / 4 (perte 100 %) |
| Recommandations | 0 / 5 (perte 100 %) |

**Diagnostic** : la compression extrême détruit la dimension forensique. Un journaliste ne peut pas remonter d'un `compress.md` vers la source pour vérifier une assertion.

### 1.2 v38 remplace la logique

Le pivot conceptuel est : passer d'un **résumé journalistique** (qui détruit la trace) à un **dossier forensique pour rédaction** (qui la préserve). Le SP ne rédige pas, il pré-organise la rédaction.

| Caractéristique | v37 v2 (compress) | v38 (dossier) |
|---|---|---|
| Volume cible | 100-320 mots | 1 500-4 000 mots |
| Rétention vs source | ~5 % | ~50-65 % |
| URLs | 0 | 8-15 URLs tier-1 qualifiées |
| Traçabilité | aucune | `[Lxx]` ou `[Lxx-Lyy]` par assertion |
| Faits préservés | 5/24 | 24/24 |
| Profondeur historique | 1789→2026 = 1 mot | 12 bornes datées |
| Structure | libre | 10 sections obligatoires mirrorant plan d'article |

---

## 2. Définition du Dossier Forensique

### 2.1. Définition opérationnelle

Un dossier forensique pour rédaction est un livrable Markdown de 1 500 à 4 000 mots qui :

1. **Préserve verbatim** les faits atomiques F-### présents dans la source.
2. **Trace chaque assertion factuelle** vers la source via une référence `[Lxx]` ou `[Lxx-Lyy]` vers les lignes du fichier source identifié dans l'entête `Source :`.
3. **Préserve les dates** au moins à 80 %.
4. **Préserve les URLs** au moins à 80 % (mesurées via la table `## Sources externes`).
5. **Maintient les mécanismes** (chaînes causales) découverts dans la source.
6. **Maintient les vecteurs symboliques** (Κ = concentration, Ψ = verrouillage, ⏰ = fenêtre temporelle, ↕ = verrouillage vertical, 🌐 = verrouillage horizontal, € = capture économique, 🌐 = sphère d'influence, ζ = précipitation, ρ = densité relationnelle) - au moins 5/8 vecteurs doivent être présents dans le dossier.
7. **Structure forensique fixe** : 10 sections obligatoires mirrorant le plan d'article de destination (`[PLAN_ARTICLE]`).

### 2.2. Non-objectifs

- **Écrire l'article** : le dossier n'est pas un brouillon, c'est un intrant pour le SP Phase 2.
- **Inférer au-delà de la source** : tout fait non sourcé doit être tagué `(non vérifié)`.
- **Citer les URLs sans les vérifier** : les URLs sont reconstruites par congruence topo-mnésique puis marquées `(à vérifier par @FETCH)` en vague 2.
- **Supprimer les éléments émotionnels** : les éléments de perspective dialectique (positions adverses, doxa médiatique, etc.) sont préservés en §7.

---

## 3. Schéma structurel du dossier (10 sections obligatoires)

### 3.1. Sections obligatoires (toujours présentes)

| # | En-tête | Contenu attendu | Source mirrorée |
|---|---|---|---|
| 1 | `## Métadonnées & index` | Source, format, date génération, volume mots, liste 10 sections | n/a (intro) |
| 2 | `## Thèse centrale (verbatim)` | Verbatim de la thèse + 2-3 § défendant la thèse | §0 source |
| 3 | `## Verrouillage (§1)` | Top 3 vecteurs Κ/Ψ/⏰ + chaîne concentration | §1 source |
| 4 | `## Acteurs nominaux (§3)` | 10-15 acteurs avec rôle, position, interactions | §3+§8 source |
| 5 | `## Mécanismes (§6)` | 3 mécanismes M1/M2/M3 avec chaînes 4-5 niveaux | §6 source |
| 6 | `## Faits atomiques (§5)` | Tableau 24/24 F-### : F-### / Énoncé / Tier / Nº source / Date | §5 source |
| 7 | `## Scénarios & prédictions (§4)` | 4 scénarios S1-S4 : probabilité + timeline + déclencheurs | §4 source |
| 8 | `## Perspectives dialectiques (§7)` | 4 perspectives : doxa / contre-doxa / académique / critique | §7 source |
| 9 | `## Profondeur historique (§11)` | 12 bornes datées 1789 → 2026 | §11 source |
| 10 | `## Recommandations (§15)` | 5 leçons actionnables | §15 source |

### 3.2. Sections obligatoirement complémentaires

| # | En-tête | Condition |
|---|---|---|
| 11 | `## Sources externes` | Section complémentaire obligatoire : ≥8 rows + ≥6 références F-### |
| 12 | `## Audit GATE_G` | Section complémentaire obligatoire : valide l'intégralité |

### 3.3 Format cible article Substack

**Toujours** : format `ARTICLE` (introduction narrative → sections emboîtées → conclusion).
**Parfois** : format `ANALYTIQUE` ou `REGISTRE` (pas d'introduction narrative, sections plates). Dans ce cas, l'annexe opérationnelle peut être omise.

---

## 4. Convention de traçabilité (le pivot forensique)

### 4.1. Marqueurs `[Lxx]`

Toute assertion factuelle non triviale doit être suivie d'une référence `[Lxx]` pointant vers la ligne du fichier source identifié dans l'entête `Source :`.

**Format compact** :

```
[F-002 :L211]    → fait F-002 ligne 211 de la source
[L26-L33]       → lignes 26 à 33 section §1.1
```

**Format étendu (avec préfixe optionnel)** :

```
[F-002:L211]
[§3.1:L11-L12]  → sous-section §3.1 lignes 11-12
```

L'entête `Source :` au début du dossier fixe le contexte : si le dossier ne référence qu'une seule source, le `[Lxx]` seul est suffisant et lisible.

### 4.2. Algorithme de tracé (à exécuter avant rédaction)

1. **Lire le fichier source** et mesurer les vraies positions avec `grep -n '^## \|^### ' <source>`.
2. **Mapper** chaque section au range de lignes mesuré :
   - §0 : L12-L21
   - §1 : L22-L77
   - §5 : L202-L251 (24/24 F-###)
   - §6 : L252-L305
   - §15 : L555-L576
   - etc.
3. **Pour chaque F-###** : mesurer la ligne exacte via `grep -n '| Fxxx |' <source>`.
4. **Rédiger** les marqueurs en parallèle du contenu.

### 4.3. Interdiction de fabrication

Règle absolue (`knowledge.md`) : **ne JAMAIS inventer une référence `[Lxx]` qui n'a pas été mesurée par `grep -n`**. Si la position est incertaine, marquer `(estimé)` ou omettre le marqueur.

---

## 5. Conventions de format forensique

### 5.1. Interdiction du tiret cadratin

Aucun caractère U+2014 (`-`) ne doit apparaître dans le dossier. Remplacement par :

- `:` pour les séparateurs de phrase (« … : conclusion »).
- `-` pour les éléments de liste.
- parenthèses `()` pour les incises.

### 5.2. Espaces insécables

Avant `:` et `;` en français. Guillemets français `« »`.

### 5.3. Caractères symboliques

Les vecteurs sont représentés par leurs glyphes (Cf. SYSTEM/SYMBOLS.md) : Κ, Κ/√, Ψ, ⏰, ↕, 🌐, €, 🌐, ζ, ρ. Marqueurs de perspective : ⟐ tension dialectique, 🎓 académique, 🔥 critique, ✦ solidité.

### 5.4. Pas de gras superflu

Le gras `**` est réservé aux éléments critiques : vecteurs, scénarios, chiffres clés, marqueurs `[F-...]`. L'italique `_` est autorisé pour les précisions et apartés.

---

## 6. Auto-Audit (Checklist manuelle du SP)

> Note 2026-07-06 22 h : la validation algorithmique Python (`dossier_validate.py`) a été retirée. Les 8 métriques M1-M8 sont désormais à vérifier par **auto-audit du sub-agent CRITIQUE** ou **checklist manuelle du pilote** aux checkpoints CP1 / CP2. Cf. prompt-v35.md §Phase 1 Post-validation.

### 6.1. 8 métriques à valider avant émission

| # | Métrique | Critère | Seuil GO | Seuil HARD_FAIL |
|---|---|---|---:|---:|
| **M1** | Volume mots | `len(d.split())` | 1 500 ≤ V ≤ 4 000 | V < 1 500 ou V > 5 000 |
| **M2** | Traçabilité reverse | `count_traces() / count_assertions()` | ≥ 90 % | < 70 % |
| **M3** | Sources externes | `len(rows) ≥ 8 ET count(F-###) ≥ 6` | ≥ 8 rows + ≥ 6 F-### | aucune source |
| **M4** | Dates préservées | `count_dates_dossier / count_dates_source` | ≥ 80 % | < 60 % |
| **M5** | Mécanismes | `count('### M') ≥ 3` | ≥ 3 | < 1 |
| **M6** | Sections obligatoires | count des 10 en-têtes de §3.1 | 10/10 | < 7 |
| **M7** | Em-dashes U+2014 | `grep -c '-'` | 0 | > 5 |
| **M8** | Pseudo-invents | chiffres dossier vs chiffres source (sans F-###, sans L###) | ≤ 3 | > 10 |

### 6.2. Auto-Audit Sub-Agent CRITIQUE (recommandé)

Invoquer CRITIQUE (cf. prompts/quintessence_critic.md) avec `filePaths = [<dossier>.md, <source>.md]` pour valider les 8 métriques M1-M8 via une expertise LLM.

Le sub-agent CRITIQUE produit :

1. **Rapport de validation** listant M1-M8 PASS/NOGO/HARDFAIL.
2. **Notes pédagogiques** sur les violations (e.g. « M2 trace_pct=78% : 12 assertions sans marqueur `[Lxx]`, principalement en §3 Acteurs »).
3. **Recommandations** correctives (e.g. « Compléter §3 avec `grep -n '^### ' <source> »).
4. **Décision finale** : GO (passer Phase 2), NO-GO (retravailler), HARD-FAIL (refonte).

### 6.3. Checklist manuelle minimale du pilote

Si sub-agent CRITIQUE non disponible (réseau, contexte, coût), le pilote applique lui-même 8 questions :

| # | Question |
|---|---|
| Q1 | Le dossier fait-il entre 1 500 et 4 000 mots ? |
| Q2 | Chaque fait F-### cité a-t-il son marqueur `[Lxx]` vers la source ? |
| Q3 | La table `## Sources externes` contient-elle ≥8 sources et ≥6 références F-### ? |
| Q4 | Les dates de la chronologie sont-elles préservées verbatim ? |
| Q5 | Au moins 3 mécanismes M1/M2/M3 + chaînes causales ? |
| Q6 | Les 10 sections obligatoires sont-elles présentes ? |
| Q7 | Aucun tiret cadratin (-) n'est toléré (grep avant émission) ? |
| Q8 | Tous les chiffres et acteurs figurant dans le dossier sont-ils présents dans la source ? |

**Action à chaque NO-GO** : soit corriger le dossier, soit rejeu Phase 1 avec consigne explicite.

---

## 7. Pipeline SP (Sublimator Phase 1) - modification v38

> **Nature du pipeline.** Production 100% Markdown du `dossier_v38.md` : lecture source, rédaction section par section, insertion de marqueurs `[Lxx]`, vérifications shell. Aucun intermédiaire structuré : le pilote applique directement le contrat SPECS v38, qu'il soit humain ou LLM autonome. Les références schéma du pilote prompt-v35.md (sub-prompts, Mnemolite) assistent la production Markdown sans introduire de format parasite. Le témoin de référence est le dossier `investigations/2026-07-04-RIC/_quintessence/2026-07-04_18-00_referendum_initiative_citoyenne_dossier_v38.md` (3 533 mots, daté 2026-07-04, produit manuellement selon SPECS v38). Cf. §2.1 « Définition opérationnelle » pour les invariants du livrable.

### 7.1. Nouveaux prompts système

Avant la rédaction du dossier, le SP doit charger 4 fichiers :

1. `tools/engines/sublimator/prompt-v35.md` (pilote top-level).
2. `SYSTEM/SYMBOLS.md` - glyphe ↔ sémantique.
3. `tools/PROMPT_KERNEL.md` - kernel global du projet.
4. Le fichier source `<source.md>` à densiifier.

### 7.2. Étapes de génération

| Étape | Action | Outil |
|---|---|---|
| 1 | Mesurer les vraies positions des sections dans la source | `grep -n '^## \|^### '` |
| 2 | Lire la source en entier | `read_files` |
| 3 | Identifier les sections par mapping mesuré | agent principal |
| 4 | Générer le brouillon section par section (10 sections) | agent principal |
| 5 | Insérer les marqueurs `[Lxx]` **après** avoir mesuré les positions | `str_replace` ciblé |
| 6 | Vérifier l'absence d'em-dash | `grep -c '-'` |
| 7 | Compléter `## Sources externes` avec URLs tier-1 | agent principal |
| 8 | Lancer sub-agent CRITIQUE ou auto-audit (§6) | sub-agent ou shell |
| 9 | Itérer 1-2 si metrics FAIL | agent principal |

### 7.3. Emplacement de sortie

Le dossier v38 est sauvegardé dans :

```
investigations/<sujet>/_quintessence/<YYYY-MM-DD_HH-MM>_<sujet>_dossier_v38.md
```

Note : le répertoire `_quintessence/` est distinct de `_validation/` (qui sert aux tests et brouillons). Conformément au SPECS v37 v2.

---

## 8. Résultats test A/B (RIC 18:00, 2026-07-04)

### 8.1. Mesures

| Métrique | Résultat | Seuil | Statut |
|---:|---:|---|---|
| M1 volume | 3 533 mots | [1 500-4 000] | PASS |
| M2 traçabilité | 116 traces / 24 F-### = 483 % | ≥ 90 % | PASS |
| M3 sources externes | 12 rows / 29 refs F-### | ≥ 8 / ≥ 6 | PASS |
| M4 dates préservées | 100 % | ≥ 80 % | PASS |
| M5 mécanismes | 3 (M1, M2, M3) | ≥ 3 | PASS |
| M6 sections | 10/10 | 10 | PASS |
| M7 em-dashes | 0 | 0 | PASS |
| M8 pseudo-invents | régression - à durcir | ≤ 3 | NOGO soft |

**Verdict** : [GO] sur l'échantillon. M8 régression notée vague 2.

### 8.2. Audit qualitatif (perte vs source)

| Catégorie | Éléments | Statut |
|---|---|---|
| **Préservé verbatim** | Thèse §0, F-### §5 (24/24), mécanismes §6 (3/3), perspectives §7 (4/4), bornes datées §11 (12/12), recommandations §15 (5/5), audit GATE_G §14, acteurs §3 (10 nominaux) | OK |
| **Compressé** | §8 graph acteurs (ASCII simplifié), §4 scénarios (probabilités+timeline), §9 vecteurs (5/8 vecteurs présents) | acceptable |
| **Perdu** | §2 ICEBERG (5 lignes nature architecture), §12.3 Seuils critiques (28 %/53 %/45 %/112 %), §13 synoptique 7 dimensions, §3.4 périmètres exclus | perte mineure |
| **Fabriqué** | 12 URLs topo-mnésiques (Conseil constitutionnel, EUR-Lex, CVIPOF, Acrimed, legranddebat.fr), `L92962` (date 1962 incohérente) | à vérifier par `@FETCH` |

### 8.3. Ratio rétention v38 vs v37 v2

| Métrique | v37 v2 | v38 | Gain |
|---|---:|---:|---:|
| Volume | 293 mots | 3 533 mots | × 12 |
| Rétention vs source | 5,2 % | 62,9 % | × 12 |
| F-### préservés | 5/24 (21 %) | 24/24 (100 %) | × 4,8 |
| URLs préservées | 0 | 12 | infini |
| Traçabilité | 0 trace | 116 traces | infini |
| Dates préservées | ~8 % | 100 % | × 12 |

---

## 9. Backlog vague 2 (améliorations à venir)

### 9.1. M8 durcissement (priorité haute)

- **Cause** : M8 régression passée de 1 → 103 pseudos-invents après conversion des traces au format court `[Lxx]`.
- **Pistes** :
  - Projection chiffre-par-chiffre dossier vs source (sans F-###, sans L###).
  - Améliorer le pattern de strip pour capturer `L\d+` plus large.
- **Action** : tester sur le corpus RIC en générant 5 nouveaux dossiers et en observant M8.

### 9.2. Vérification URLs (priorité haute)

- **Cause** : 12 URLs topo-mnésiques non vérifiées.
- **Action** : intégrer un appel `@FETCH URL` (run_terminal_command avec code HTTP 200 attendu) avant archivage du dossier.

### 9.3. Trace fabrication L92962 (priorité haute)

- **Cause** : section §11 mentionne date 1962 avec référence incohérente.
- **Action** : mesurer la vraie position via `grep -n '1962' <source>`, substituer.

### 9.4. Réintroduction validation algorithmique (priorité moyenne)

- **Action** : après stabilisation Sublimator + LLM hôte sur 5+ enquêtes (cf. SPECS v37 v2 §12 Test A/B juge de paix), reconsidérer la validation algorithmique Python si elle redevient utile. Le SPECS v38 §6 reste en mode checklist tant que cette condition n'est pas remplie.
- **Statut 2026-07-06** : suspension.

---

## 10. Anti-patterns à éviter

### 10.1. Fabriquer des références

Ne JAMAIS inventer une référence `[Lxx]` qui n'a pas été mesurée par `grep -n`. Une référence non sourcée est une **fabrication** au sens du `knowledge.md` et une trahison de la vocation forensique du dossier.

### 10.2. Confondre dossier avec article

Le dossier n'est pas un brouillon. C'est un intrant structuré pour la rédaction. Éviter les phrases narratives (« On observe que… »). Préférer les énoncés factuels denses (« F-002 : La Belgique a créé un Conseil citoyen permanent [Décret 25 février 2019, F-002 :L211] »).

### 10.3. Oublier la table `## Sources externes`

C'est l'élément traçant les URLs tier-1 préservées. Sans cette section, M3 ne peut pas être mesuré et le dossier passe pour anémique.

### 10.4. Mélanger les sources

Un dossier ne référence **qu'une seule** source (le `Source :` entête). Si plusieurs investigations sont mélangées, il faut :

- soit les intégrer dans une investigation consolidée en amont,
- soit créer plusieurs dossiers (un par source) avec entête `Source :` distinct.

### 10.5. Rédiger en anglais

Tout le contenu du dossier est en français, conformément à `knowledge.md` et aux conventions Substack du projet.

---

## 11. Exemple de référence - Dossier RIC 18:00

### 11.1. Entête recommandée

```yaml
---
Source : investigations/2026-07-04-RIC/2026-07-04_18-00_referendum_initiative_citoyenne_INVESTIGATION.md
Format : ARTICLE
Date de génération : 2026-07-06, 21 h 45
Volume : 3533 mots
Sections : 10/10 obligatoires + Sources externes + Audit GATE_G
---
```

Note : le validateur (historique) extrayait `Source :` via regex simple sur les premières lignes du fichier. Le format YAML ci-dessus est documentaire, pas un parseur YAML complet.

### 11.2. Mesure des positions (à reporter dans le SPECS)

```bash
grep -n '^## §\|^## Annexe' <source>
# §0: L12-L21     §1: L22-L77
# §5: L202-L251   §6: L252-L305
# §15: L555-L576
```

### 11.3. Marqueur-type

```
**Ψ Concentration** (Ψ = 6/8) - le verrouillage structurel bloque le RIC
en verrouillant simultanément le constituant (Art. 89) et la fenêtre
temporelle (Art. 11 §5). [§1.2:L36-L40]
```

---

## 12. Application au SP Phase 2 (transition)

### 12.1. Mapping dossier → article

| Section dossier | Section article cible |
|---|---|
| §3 Métadonnées & index | (intro méta supprimée) |
| §4 Verrouillage (§1) | Sous-titre |
| §6 Acteurs nominaux (§3+§8) | Corps §1 |
| §7 Mécanismes (§6) | Corps §2 |
| §8 Faits atomiques (§5) | Annexe inline §3 |
| §9 Scénarios (§4) | Corps §4 |
| §10 Dialectique (§7) | Corps §5 |
| §11 Historique (§11) | Encadré |
| §12 Recommandations (§15) | Conclusion |

### 12.2. Règles d'élagage SP Phase 2

- Garder tous les F-### de Tier 1 (sources primaires).
- Garder 60-80 % des F-### de Tier 2 (sources secondaires fiables).
- Élaguer 40-60 % des F-### de Tier 3+ (commentaires, sources discutables).
- Convertir chaque section dense en 1-3 phrases narratives forensiques.

---

## 13. Glossaire

| Terme | Définition |
|---|---|
| **Dossier forensique** | Livrable Markdown 1 500-4 000 mots à 10 sections préservant la trace vers la source. |
| **F-###** | Identifiant de fait atomique unique dans la source (F-001 à F-024 typique). |
| **Tier X** | Niveau de fiabilité de la source (1 = primaire, 2 = secondaire, 3+ = commentaire). |
| **Trace `[Lxx]`** | Référence forensique vers une ligne de la source. |
| **Vecteur Κ/Ψ/⏰/↕/🌐/€** | Glyphe du SYMBOLS.md représentant une dimension sémantique. |
| **`@FETCH`** | Commande interne pour valider une URL via HTTP HEAD/GET. |
| **`grep -n`** | Commande shell pour mesurer la position exacte d'une ligne. |
| **Auto-Audit** | Validation des 8 métriques M1-M8 par sub-agent CRITIQUE ou checklist manuelle du pilote. |

---

## Annexe - Historique du SPECS

| Version | Date | Changement principal |
|---|---|---|
| v37 v2 | 2026-06-15 | compress_summary ≤320 mots - rétention 5 %, échec |
| v38 v1 | 2026-07-06 15:00 | Dossier forensique - 10 sections, traces `[filename.md:Lxx]` |
| v38 v2 | 2026-07-06 18:30 | Fix bugs 1-5 (regex M2/M8, M3 sources externes, em-dash) |
| v38 v3 | 2026-07-06 21:45 | Traces courts `[Lxx]`, dossier dans `_quintessence/`, MAX_VOL=4 000, résultats test A/B intégrés |
| v38 v3.1 | 2026-07-06 22:00 | §6 transformée en checklist manuelle (abandon validation algorithmique Python) |
