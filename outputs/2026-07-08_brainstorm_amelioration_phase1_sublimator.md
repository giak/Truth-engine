# Brainstorm : Amélioration Phase 1 Sublimator (prompt-v35.md)

**Date :** 2026-07-08
**Source diagnostic :** Audit n=42 v3 (cf. `outputs/2026-07-08_audit_phase1_sublimator_v35.md`)
**Cible :** Produire des quintessences « parfaites » (6/6 sur tous les critères objectifs + C4/C8/C9 validés)

---

## 0. Cadre du brainstorm

L'audit automatisé sur 42 quintessences réelles révèle :

- **C10 (9 noms H2 canoniques) = 23.8%** : seuls 10/42 fichiers ont leurs 9 sections alignées sur les noms canoniques
- **C7 (§7-§8 canoniques) = 50%** : la moitié des fichiers n'ont pas Verbatim/Notes canoniques
- **C2 (F-##/M1-M4) = 73.8%** : 11/42 fichiers sans aucun identifiant préservé
- **C6 (traçabilité [Lxx]) = 76.2%** : 10/42 fichiers sans trace
- **2 clusters révélés** : A « Volumétrie » (15 fichiers, 3.3/6) vs B « Canonique » (27 fichiers, 4.2/6)
- **Plafond de verre : 0/42 fichier parfaitement canonique**, max 5.5/6
- **Bug C5** : regex source unique inadapté au format frontmatter

**Contraintes absolues préservées** : zéro hallucination, zéro em-dash, refus Phase 1 (pas d'angle/thèse/anticipation Phase 2), français soutenu, convention `[Lxx]` ou `(estimé)`.

---

## 1. 22 améliorations catégorisées (P1-P7)

### Catégorie A : Structuration du prompt (P1 critique)

#### A1. Verrouillage des 9 noms H2 en bloc de code copiable (P1, CRITIQUE)
- **Description** : Remplacer la liste numérotée actuelle par un bloc de code littéral copiable, qui force le LLM à utiliser ces chaînes exactes.
- **Cible** : `tools/engines/sublimator/prompt-v35.md` §Dimensions canoniques.
- **Impact attendu** : C10 passe de 23.8% à ≥80% (réduction écart type sur les noms H2).
- **Coût** : Faible (modification texte).
- **Validation** : re-run `tools/audit_phase1_sublimator_v35.py` post-refonte sur 5 quintessences pilote.

#### A2. Bloc « synonymes INTERDITS » (P1, CRITIQUE)
- **Description** : Ajouter un glossaire explicite des renommages à proscrire :
  - « Volumétrie & structure » → « Faits atomiques préservés »
  - « Cœur de l'enquête » → « Acteurs nominaux »
  - « 4 recommandations §8 » → « Notes méthodologiques source »
  - « Réponse SQ1-SQ6 » → « Verbatim et citations »
  - « Calendrier législatif T0-T+48 » → « Chronologie datée »
  - « Architecture triple » → « Mécanismes / chaînes causales »
  - « Mensonges §7 » → « Verbatim et citations »
  - « Héritages consolidés » → « Notes méthodologiques source »
- **Cible** : nouvelle section §Synonymes interdits dans prompt-v35.md.
- **Impact attendu** : C10 passe de 23.8% à ≥85% (les 15 fichiers Cluster A ne dévient plus).
- **Coût** : Faible (ajout section ~15 lignes).
- **Validation** : grep `## 2\. Volumétrie` sur 42 fichiers doit retourner 0 post-refonte.

#### A3. Suppression de la ligne parasite « ## 8. Format standardisé Phase 1 KISS » (P1, CRITIQUE)
- **Description** : 3/42 fichiers (bce_euro_verrou, referendum_initiative_citoyenne, external_legal_audit) ont une ligne H2 « ## 8. Format standardisé Phase 1 KISS » qui DÉVIE le §8 canonique. C'est un defect du prompt lui-même : il suggère implicitement que cette ligne peut exister.
- **Cible** : `tools/engines/sublimator/prompt-v35.md` §Workflow Phase 1 + §Dimensions canoniques.
- **Impact attendu** : C7 passe de 50% à ≥60% (les 3 fichiers où §8 est « Format standardisé » redeviennent conformes).
- **Coût** : Très faible (suppression texte).
- **Validation** : grep `Format standardisé Phase 1 KISS` dans corpus → 0 occurrence dans H2.

#### A4. Directive §7 et §8 obligatoire avec gabarit minimum (P1, CRITIQUE)
- **Description** : Imposer un contenu minimum par section :
  - §7 ≥ 3 citations verbatim avec auteur/contexte/source
  - §8 ≥ 3 notes méthodologiques (statut, GATE_G, BIAS TEST, loups, lièvres)
- **Cible** : `tools/engines/sublimator/prompt-v35.md` §Dimensions canoniques, sous-sections 7 et 8.
- **Impact attendu** : C7 passe de 50% à ≥85% (les 21 fichiers qui n'ont pas Verbatim/Notes sont contraints à les inclure).
- **Coût** : Faible (ajout 10 lignes de gabarit).
- **Validation** : grep `## 7\. Verbatim` ET `## 8\. Notes` → ≥42 fichiers chacun.

#### A5. Renforcement de l'unicité de la numérotation 1-9 (P2, HAUTE)
- **Description** : Préciser que les sections H2 doivent être EXACTEMENT numérotées 1 à 9 (pas 1-10, pas 1-8, pas 1-9 + 10bis). Le fichier `external_legal_audit_quintessence` a 10 H2 (⚠️).
- **Cible** : §Format standardisé Phase 1 KISS.
- **Impact attendu** : C1 passe de 97.6% à 100%.
- **Coût** : Très faible (1 ligne).
- **Validation** : regex `^## 1[0-9]\. ` → 0 match.

### Catégorie B : Validation / Quality Gates (P1-P2)

#### B1. Sub-agent CRITIQUE rendu obligatoire (P1, CRITIQUE)
- **Description** : Le prompt mentionne CRITIQUE comme « en option ». Le rendre OBLIGATOIRE post-EXTRACTEUR avec sortie verdict [GO/NO-GO] + score.
- **Cible** : §Orchestration Sublimator étape C.
- **Impact attendu** : 100% des quintessences passent par une validation experte ; ramène les 18 fichiers Cluster A partiels vers 4+/6.
- **Coût** : Moyen (modifie workflow opérationnel + tokens LLM).
- **Validation** : journaliser `critique_verdict` dans frontmatter des quintessences.

#### B2. Auto-évaluation 5 critères [GO] avant émission (P2, HAUTE)
- **Description** : Imposer au pilote de s'auto-évaluer sur 5 critères avant d'écrire le fichier :
  1. 9 sections H2 numérotées 1-9 ?
  2. F-## et M## source tous préservés ?
  3. §7 et §8 remplies avec contenu minimum ?
  4. ≥ 1 trace [Lxx] par fait non trivial ?
  5. Pas de phrase narrative/angle ?
  Si une réponse est NON → retour à l'extraction.
- **Cible** : nouvelle section §Auto-évaluation obligatoire dans §Workflow Phase 1.
- **Impact attendu** : C2 (73.8%) et C6 (76.2%) passent à ≥90% par double-pass.
- **Coût** : Faible (ajout 20 lignes + doublement du temps LLM).
- **Validation** : audit des 42 fichiers post-refonte.

#### B3. Validation algorithmique (re-grep [Lxx] vs source) (P2, HAUTE)
- **Description** : Script `tools/quintessence_validate.py` qui vérifie pour chaque `[Lxx]` qu'il existe dans le fichier source. Sortie : exit 0 si 100% valides, exit 1 sinon.
- **Cible** : nouvelle section §Outillage de validation.
- **Impact attendu** : hallucination [Lxx] → 0 (vs détection manuelle actuelle).
- **Coût** : Moyen (script Python ~100 lignes).
- **Validation** : exécution sur les 42 fichiers, 0 fichier ne devrait avoir de [Lxx] invalide.

#### B4. Seuil de rejet (P3, MOYENNE)
- **Description** : Si auto-évaluation < 4/5 sur les critères critiques → HALTE explicite, ne pas produire le fichier.
- **Cible** : §Cas-limites Phase 1 (ajouter ce cas).
- **Impact attendu** : élimine les 5 fichiers à 3/6 et le 1 fichier à 3.5/6 (passage à reformulation).
- **Coût** : Aucun (instruction texte).

### Catégorie C : Anti-hallucination (P1-P2)

#### C1. Extraction exhaustive F-## (P1, CRITIQUE)
- **Description** : Workflow impose l'étape intermédiaire : « lister TOUS les F-## de la source (FACT_REGISTRY §X), puis COPIER verbatim dans §2 de la quintessence. Aucun F-## ne doit être omis ».
- **Cible** : §Workflow Phase 1, étape 2.
- **Impact attendu** : C2 passe de 73.8% à ≥95% (les 11 fichiers sans F-##/M## sont régénérés exhaustifs).
- **Coût** : Faible (modification workflow).
- **Validation** : `diff <(grep -oE 'F-[A-Z]+-\d+' source | sort -u) <(grep -oE 'F-[A-Z]+-\d+' quintessence | sort -u)` doit retourner vide.

#### C2. Marque `(estimé)` obligatoire sur positions de ligne non mesurées (P2, HAUTE)
- **Description** : Le prompt dit « omettre ou marquer (estimé) » → le LLM omet souvent. Imposer (estimé) systématique pour toute référence [Lxx] non mesurée par `grep -n`.
- **Cible** : §Convention de trace [Lxx].
- **Impact attendu** : 0 référence inventée ; audit pass à 100%.
- **Coût** : Faible (précision texte).
- **Validation** : regex `\[L\d+\]` sans `(estimé)` ni `(mesuré)` → réduit fortement.

#### C3. Diff binaire automatique contre source (P3, MOYENNE)
- **Description** : Script `tools/quintessence_diff.py` qui compare chaque F-## de la quintessence avec la source (extraction verbatim, pas paraphrase). Sortie : taux de fidélité.
- **Cible** : nouvelle section §Outillage de validation.
- **Impact attendu** : garantit la fidélité verbatim des F-## (actuellement non vérifiable sans diff).
- **Coût** : Moyen (script Python + heuristiques de paraphrase).
- **Validation** : taux de fidélité ≥ 95% sur les 42 fichiers post-refonte.

### Catégorie D : Comparabilité inter-batchs (P1-P2)

#### D1. Variante §9 unique autorisée (P1, CRITIQUE)
- **Description** : Actuellement 5 variantes §9 sont tolérées. N'en autoriser qu'UNE seule : « ## 9. Limites connues de cette extraction (case-limites) ».
- **Cible** : §Dimensions canoniques + §Format standardisé.
- **Impact attendu** : C10 strict passe de 0% à ≥50% (les fichiers qui matchaient en lenient matchent aussi en strict).
- **Coût** : Faible.
- **Validation** : regex `## 9\. Limites` → 42 fichiers.

#### D2. Interdiction des noms H2 longs (descriptifs) (P1, CRITIQUE)
- **Description** : Le Cluster A (15 fichiers) utilise des noms H2 longs type « ## 3. Cœur de l'enquête : 12 faits canoniques F-PRES## (verbatim §12 source) ». Imposer : « nom H2 = nom canonique EXACT, pas de suffixe, pas d'annotation entre parenthèses ».
- **Cible** : §Format standardisé Phase 1 KISS.
- **Impact attendu** : C10 passe de 23.8% à ≥80%.
- **Coût** : Faible.
- **Validation** : regex `## \d\. [A-ZÉÈÀ][^()\n]{0,80}$` (nom ≤ 80 char sans parenthèse) sur 42 fichiers.

#### D3. Caractères de tier (✦ ✧ ⁅ ❧) exclus du H2 (P2, HAUTE)
- **Description** : Certains H2 incluent des glyphes de tier. Imposer : « nom H2 = texte ASCII/UTF-8 alphabétique, pas de glyphe ».
- **Cible** : §Format standardisé.
- **Impact attendu** : parsing plus robuste, C10 facilité.
- **Coût** : Très faible.

### Catégorie E : Workflow / Process (P2-P3)

#### E1. Workflow 6 étapes explicite (P2, HAUTE)
- **Description** : Le workflow actuel est en 4 étapes. Le décomposer en 6 :
  1. `grep -n '^## ' source` pour mesurer les sections
  2. `grep -oE 'F-[A-Z]+-\d+|M[1-9]' source` pour lister TOUS les F-##/M1-M4
  3. Capturer verbatim chaque F-## avec sa position [Lxx]
  4. Construire §1-§9 selon le gabarit canonique
  5. Auto-évaluer les 5 critères [GO] (cf. B2)
  6. Émettre le fichier Markdown
- **Cible** : §Workflow Phase 1.
- **Impact attendu** : garantit l'exhaustivité (C2) et la conformité (C7, C10).
- **Coût** : Faible.
- **Validation** : trace des 6 étapes dans frontmatter YAML (timestamp par étape).

#### E2. Double-pass extraction + vérification (P3, MOYENNE)
- **Description** : Imposer 2 passes :
  - Passe 1 : extraction brute §1-§9
  - Passe 2 : vérification croisée (auto-audit antagoniste, détection des F-## oubliés, vérification des [Lxx])
- **Cible** : §Workflow Phase 1.
- **Impact attendu** : C2 et C6 passent à ≥95%.
- **Coût** : Élevé (doublement tokens LLM).

### Catégorie F : Métadonnées & traçabilité (P2-P3)

#### F1. Frontmatter YAML obligatoire (P2, HAUTE)
- **Description** : Imposer un frontmatter YAML en tête de quintessence :
  ```yaml
  ---
  source: <path>
  date_source: <YYYY-MM-DD>
  date_quintessence: <YYYY-MM-DD>
  investigateur: <name>
  complexite: <X>/18
  confiance_globale: <0.0-1.0>
  n_faits: <int>
  n_mecanismes: <int>
  n_citations: <int>
  score_phase1_v35: <X>/6
  sub_agent_critique_verdict: [GO|NO-GO]
  ---
  ```
- **Cible** : §Workflow Phase 1 + §Format standardisé.
- **Impact attendu** : traçabilité industrielle, base pour C5 (source unique via champ `source:`).
- **Coût** : Faible.
- **Validation** : tous les 42 fichiers doivent avoir frontmatter YAML valide.

#### F2. Footer de validation sub-agent CRITIQUE (P3, MOYENNE)
- **Description** : Imposer un footer de validation :
  ```
  ---
  ## 10. Validation sub-agent CRITIQUE (option §13.3.3)
  - Verdict: [GO|NO-GO]
  - Score: X/6
  - Itération: 1/3 max
  - Date: 2026-07-XX
  ```
- **Cible** : nouvelle section §10 dans le gabarit.
- **Impact attendu** : B1 opérationnalisé.
- **Coût** : Faible.

### Catégorie G : Pièges connus (P1-P3)

#### G1. Anti-tentation anticipation Phase 2 (P1, CRITIQUE)
- **Description** : 5/42 fichiers (cnr_1944, ric_histoire_longue, ric_referendums_ive, ric_lois_civictech, ric_protocole_pnred) ont des sections « Calendrier législatif T0-T+48 » ou « Architecture triple » qui sont des anticipations Phase 2 (clustering/synthèse). Ajouter un REFUS EXPLICITE : « ne JAMAIS produire de calendrier législatif, de transposition de modèles étrangers, de recommandations opérationnelles, de plan d'action ; ce sont des livrables Phase 2/3 ».
- **Cible** : §Anti-patterns Phase 1 (renforcement).
- **Impact attendu** : 5 fichiers Cluster A passent de 3/6 à 4+/6.
- **Coût** : Faible.
- **Validation** : grep `Calendrier législatif` dans 42 fichiers → 0 occurrence.

#### G2. Anti-tentation doxa/contre-doxa (P2, HAUTE)
- **Description** : Le prompt interdit la hiérarchisation doxa/contre-doxa. Ajouter un contre-exemple explicite : « ne JAMAIS écrire 'les détracteurs affirment que... les partisans répondent que...' ».
- **Cible** : §Anti-patterns Phase 1.
- **Impact attendu** : C4 maintenu à 100% sur 42 fichiers.

#### G3. Anti-invention [Lxx] renforcée (P1, CRITIQUE)
- **Description** : Le prompt interdit d'inventer des [Lxx]. Le renforcer par : « chaque [Lxx] doit être le résultat d'un `grep -n` réel sur la source, ET doit être suivi de `(mesuré)` ou `(estimé)` ».
- **Cible** : §Règle absolue.
- **Impact attendu** : 0 référence inventée.

### Catégorie H : Spécificités par type d'enquête (P3)

#### H1. Garde-fou enquêtes sensibles (P3, MOYENNE)
- **Description** : Pour les enquêtes sur la franc-maçonnerie, cultes, extrême-orient : ajouter un §Notes déontologiques (sources d'autorité religieuse respect, pas d'insinuation sur des personnes physiques nominatives hors propos).
- **Cible** : §Cas-limites Phase 1.
- **Impact attendu** : qualité éthique maintenue.

#### H2. Sous-structure pour enquêtes méthodologiques (P3, BASSE)
- **Description** : Pour les enquêtes type « sondages IFOP/IPSOS » : ajouter un §10 (optionnel) « Méthodologie de la mesure » avec sous-champs : institut, échantillon, marge d'erreur, biais identifiés.
- **Cible** : §Cas-limites.
- **Impact attendu** : qualité pour les enquêtes data-lourdes.

---

## 2. 5 Quick Wins (impact élevé, coût faible, applicables immédiatement)

| # | Quick win | Impact | Coût | Priorité |
|---|-----------|--------|------|----------|
| **QW1** | **Verrouillage des 9 noms H2 en bloc de code copiable** (A1) | C10 : 23.8% → ≥80% | Faible (texte) | P1 critique |
| **QW2** | **Glossaire de synonymes INTERDITS** (A2) | C10 : 23.8% → ≥85% | Faible (15 lignes) | P1 critique |
| **QW3** | **Suppression de la ligne parasite « ## 8. Format standardisé Phase 1 KISS »** (A3) | C7 : 50% → ≥60% | Très faible (suppression) | P1 critique |
| **QW4** | **Variante §9 unique autorisée** (D1) | C10 strict : 0% → ≥50% | Faible (précision) | P1 critique |
| **QW5** | **Anti-tentation anticipation Phase 2 renforcée** (G1) | 5 fichiers Cluster A : 3/6 → 4+/6 | Faible (ajout contre-exemples) | P1 critique |

**Effet combiné QW1-QW5 attendu** : score moyen passe de 3.86/6 (64.3%) à ≥5.0/6 (83.3%) sur les 42 fichiers.

---

## 3. 5 Améliorations long terme (refonte profonde, validation empirique)

| # | Amélioration | Description | Coût | Validation |
|---|--------------|-------------|------|------------|
| **LT1** | **Frontmatter YAML obligatoire** (F1) | Standardisation industrielle, base pour C5 | Faible | Tous les 42 fichiers |
| **LT2** | **Workflow 6 étapes explicite** (E1) | Garantit exhaustivité F-## et conformité structurelle | Moyen (refonte §Workflow) | Double-pass sur 5 fichiers pilote |
| **LT3** | **Sub-agent CRITIQUE obligatoire** (B1) | Validation experte systématique | Élevé (orchestration) | Test A/B sur 10 quintessences |
| **LT4** | **Validation algorithmique (re-grep [Lxx])** (B3) | Script `tools/quintessence_validate.py` | Moyen (script 100 lignes) | Tous les 42 fichiers, 0 erreur |
| **LT5** | **Double-pass extraction + vérification** (E2) | Garantit C2 ≥95% et C6 ≥95% | Élevé (doublement tokens) | Test A/B vs single-pass |

**Effet combiné LT1-LT5 attendu** : plafond de verre actuel 5.5/6 brisé, 6/6 atteignable sur ≥80% des fichiers.

---

## 4. Prompt refondu (extrait illustrant l'intégration des QW)

### §Dimensions canoniques de la quintessence (version refondue)

```python
# BLOC COPIABLE : Les 9 sections H2 sont EXACTEMENT celles-ci, dans cet ordre.
# Aucune variation, aucun suffixe, aucune annotation entre parenthèses.

## 1. Métadonnées & trace source
## 2. Faits atomiques préservés
## 3. Acteurs nominaux
## 4. Sources externes citées
## 5. Chronologie datée
## 6. Mécanismes / chaînes causales
## 7. Verbatim et citations
## 8. Notes méthodologiques source
## 9. Limites connues de cette extraction (case-limites)
```

### §Synonymes INTERDITS (NOUVELLE section)

Les renommages suivants sont INTERDITS. Tout synonyme doit être remplacé par le nom canonique :

| INTERDIT | REMPLACÉ PAR |
|----------|--------------|
| Volumétrie & structure | Faits atomiques préservés |
| Cœur de l'enquête | Acteurs nominaux |
| 4 recommandations §8 | Notes méthodologiques source |
| Réponse SQ1-SQ6 | Verbatim et citations |
| Calendrier législatif T0-T+48 | Chronologie datée |
| Architecture triple | Mécanismes / chaînes causales |
| Mensonges §7 | Verbatim et citations |
| Héritages consolidés | Notes méthodologiques source |
| Format standardisé Phase 1 KISS | (à supprimer ; ne pas avoir de §8 bis) |

### §Workflow Phase 1 (refondu 6 étapes)

1. `grep -n '^## ' source` pour mesurer les sections
2. `grep -oE 'F-[A-Z]+-\d+|M[1-9]' source` pour lister TOUS les F-##/M1-M4
3. Capturer verbatim chaque F-## avec sa position `[Lxx]` ou `(estimé)`
4. Construire §1-§9 selon le gabarit canonique (cf. bloc copiable ci-dessus)
5. Auto-évaluer les 5 critères [GO] (cf. §Auto-évaluation)
6. Émettre le fichier Markdown dans `investigations/<sujet>/_quintessence/`

### §Auto-évaluation obligatoire (NOUVELLE section)

Avant émission, le pilote doit s'auto-évaluer :

- [ ] Les 9 sections H2 sont numérotées 1-9 avec les noms canoniques EXACTS ?
- [ ] Tous les F-## et M## de la source sont préservés verbatim ?
- [ ] §7 contient ≥ 3 citations verbatim avec auteur/contexte/source ?
- [ ] §8 contient ≥ 3 notes méthodologiques (statut, GATE_G, BIAS TEST, loups, lièvres) ?
- [ ] Aucune phrase narrative, aucun angle, aucune anticipation Phase 2 ?

Si une réponse est NON : retour à l'étape 4 (workflow).

---

## 5. Métriques cibles (quintessence « parfaite » = 6/6)

| Critère | Cible 6/6 | Critère opérationnellement vérifiable |
|---------|-----------|---------------------------------------|
| C1 | 9 sections H2 numérotées 1-9 EXACT | `grep -cE '^## [1-9]\. '` = 9 |
| C2 | ≥ 1 F-## ou M## préservé | `grep -cE 'F-[A-Z]+-\d+\|M[1-9]'` ≥ 1 |
| C3 | 0 em-dash | `grep -c $'\xe2\x80\x94'` = 0 |
| C6 | ≥ 10 traces [Lxx] | `grep -cE '\[.*L\d+.*\]'` ≥ 10 |
| C7 | §7 + §8 canoniques | `grep -E '^## 7\. Verbatim et citations'` ET `^## 8\. Notes méthodologiques source` |
| C10 | 9 noms canoniques EXACTS | match exact des 9 chaînes du bloc copiable |

**Cible opérationnelle** : 80% des quintessences ≥ 5.5/6, 50% ≥ 6/6, 0% < 4/6.

**Plafond de verre actuel** : 0/42 fichier 6/6. Briser ce plafond = preuve que les améliorations fonctionnent.

---

## 6. Plan d'implémentation séquentiel (8 semaines)

| Semaine | Action | Livrable |
|---------|--------|----------|
| S1 | Appliquer QW1-QW5 au prompt-v35.md | `tools/engines/sublimator/prompt-v35.md` v2.0 |
| S2 | Re-générer 5 quintessences pilote (mélange Cluster A + B) | 5 fichiers test |
| S3 | Re-run audit n=42 sur les 5 fichiers + comparer | `outputs/audit_phase1_v35_v2_pilot.md` |
| S4 | Si gain ≥ +1.0/6 : appliquer à 42 fichiers | 42 fichiers re-générés |
| S5 | Implémenter LT1 (frontmatter YAML) | 42 fichiers reformatés |
| S6 | Implémenter LT2 (workflow 6 étapes) + LT4 (script validate) | `tools/quintessence_validate.py` |
| S7 | Implémenter LT3 (sub-agent CRITIQUE obligatoire) | Workflow orchestration mis à jour |
| S8 | Audit final n=42 + rapport impact | `outputs/audit_phase1_v35_v3.md` |

**Critère d'arrêt S3** : si gain < +0.5/6 sur les 5 pilotes, itérer le prompt avant de généraliser.

---

## 7. Limites du brainstorm

1. **Pas de validation empirique** : les 22 améliorations sont proposées sur la base du diagnostic n=42 et de l'expertise LLM, pas testées sur des quintessences réelles post-refonte.
2. **Pas de pondération coûts/bénéfices validée** : les classements P1-P3 sont des hypothèses de l'auditeur, pas des mesures objectives.
3. **QW3 (suppression §8 parasite) est CONTRE-INTUITIVE** : elle supprime une section explicitement nommée dans le prompt actuel. Risque de régression si l'audit révèle que d'autres fichiers s'appuient sur elle.
4. **LT3 (sub-agent CRITIQUE obligatoire) modifie l'orchestration** : peut ralentir le pipeline et augmenter les coûts LLM.
5. **Frontmatter YAML (LT1) peut casser les outils existants** : `tools/audit_ric_mapping.py` et `tools/audit_phase1_sublimator_v35.py` doivent être adaptés pour parser le YAML.
6. **Pas d'audit pair** : ce brainstorm n'a pas été relu par un évaluateur indépendant.

---

## 8. Verdict du brainstorm

**22 améliorations identifiées** dont **5 quick wins** (P1 critique, coût faible) et **5 long terme** (refonte, validation empirique requise).

**Effet combiné attendu** : score moyen passe de **3.86/6 (64.3%)** à **≥5.0/6 (83.3%)** avec les QW seuls, et **6/6 atteignable** sur ≥50% des fichiers avec les LT.

**Le plafond de verre actuel (5.5/6 max)** est brisable par l'application des QW1-QW5 sans modification du workflow LLM.

**Prochaine action recommandée** : implémenter QW1 (bloc copiable) + QW2 (glossaire synonymes) + QW3 (suppression §8 parasite) en S1, puis re-audit sur 5 pilotes en S2-S3.

---

*Brainstorm généré le 2026-07-08 par Truth Engine v2.0 selon méthodologie audit-driven (n=42) + 10 catégories d'amélioration + 5 QW + 5 LT + prompt refondu + plan 8 semaines. Limites : pas de validation empirique, pas d'audit pair, pondérations subjectives.*
