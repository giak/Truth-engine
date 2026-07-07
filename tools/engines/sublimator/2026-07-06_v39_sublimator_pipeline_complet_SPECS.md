# SPECS v39 - Sublimator Pipeline Complet (5 phases + 3 checkpoints)

> **Version** : v39 v1 (2026-07-06, 23 h 30)
> **Statut** : Spec contractuelle du pilote `prompt-v35.md` (Phases 1-3 + CP1, CP2, alignés avec le pilote).
> **Étend** : SPECS v38 v3 (Phase 1 dossier forensique uniquement) au pipeline complet.
> **Remplace** : néant (SPECS v38 v3 reste canonique pour Phase 1).

---

## 1. Vue d'ensemble du pipeline

### 1.1 Cartographie phases / livrables / checkpoints

| Phase | Type | Livrable | Emplacement | Auditeur |
|---|---|---|---|---|
| 1 | Densiification | `<...>_dossier_v38.md` | `investigations/<sujet>/_quintessence/` | M1-M8 (cf. SPECS v38 §6.1) |
| 2 | Synthèse | `synthese_clusters.json` + `synthese.json` | `investigations/<sujet>/_synthese/` | CP1 (humain) |
| 2.5 | Rapport | `rapport_synthese.md` | `investigations/<sujet>/_synthese/` | auto-audit antagoniste |
| 2.6 | Plan | `plan_article.md` | `investigations/<sujet>/_synthese/` | auto-audit antagoniste |
| 3 | Rédaction | `<date>_<sujet>_ARTICLE.md` | `articles/` | CP2 (humain) + LOI L8 |

### 1.2 Pourquoi SPECS v39

SPECS v38 (v3, 2026-07-06) couvre uniquement la Phase 1. Or :

- `prompt-v35.md` orchestre 5 phases (1, 2, 2.5, 2.6, 3) + 2 checkpoints humains (CP1, CP2) + auto-audit antagoniste Phase 3 (LOI L8).
- En l'absence de SPECS pour Phases 2-3, le pilote `prompt-v35.md` est ambigu, les seuils non vérifiables, les anti-patterns bout-en-bout non énoncés.
- SPECS v39 formalise le contrat des Phases 2-3 sans dupliquer Phase 1 (référencée par ancres SPECS v38 §X.Y).

### 1.3 Cadre général

But : 1 article Substack (3000-5000 mots, format ARTICLE) issu de N enquêtes journalistiques.

Architecture : 5 phases séquentielles + 2 checkpoints humains (CP1, CP2) + 1 auto-audit antagoniste (LOI L8).

### 1.4 Convention de référence

Tout au long de SPECS v39, les références à SPECS v38 utilisent la notation `§X.Y` (ex : `§3.1`). Aucune duplication.

**Précision LOI L9 (post-audit L8 NF3)** : les références LOI L9 aux sections SPECS v38 utilisent le schéma **`§3.1 list-index`** (1 à 10 : 1=Métadonnées, 2=Thèse, 3=Verrouillage, 4=Acteurs, 5=Mécanismes, 6=Faits, 7=Scénarios, 8=Perspectives, 9=Historique, 10=Recommandations), pas le schéma `§12.1 dossier-§X` qui offset de +2 (Métadonnées=§3, Verrouillage=§4, etc.) et omet §5. Ce choix garantit que LOI L9 réfère directement aux 10 sections canoniques du dossier forensique.

---

## 2. Phase 1 : Dossier forensique (ancrage SPECS v38)

### 2.1 Rappel SPECS v38 §3.1 (10 sections obligatoires)

Le dossier `dossier_v38.md` comprend 10 sections obligatoires (Métadonnées, Thèse centrale verbatim, Verrouillage, Acteurs nominaux, Mécanismes, Faits atomiques F-###, Scénarios et prédictions, Perspectives dialectiques, Profondeur historique, Recommandations) + 2 sections obligatoirement complémentaires (`## Sources externes` ≥ 8 rows + ≥ 6 références F-###, et `## Audit GATE_G` qui valide l'intégralité).

### 2.2 Rappel SPECS v38 §6.1 (audit M1-M8)

8 métriques à valider avant émission : volume, traçabilité reverse, sources externes, dates préservées, mécanismes, sections obligatoires, em-dashes U+2014, pseudo-invents. Seuils GO / HARD_FAIL détaillés (cf. SPECS v38 §6.1).

### 2.3 Rappel SPECS v38 §7.2 (pipeline 9 étapes)

9 étapes opérationnelles : mesurer positions (`grep -n`), lire source, mapper sections, rédiger 10 sections, insérer marqueurs `[Lxx]`, vérifier absence em-dash, compléter Sources externes, lancer audit M1-M8, émettre.

### 2.4 Rappel SPECS v38 §7.3 (emplacement)

`investigations/<sujet>/_quintessence/<YYYY-MM-DD_HH-MM>_<sujet>_dossier_v38.md`. Le répertoire `_quintessence/` est distinct de `_validation/`.

### 2.5 Production operationalisée

Le pilote `prompt-v35.md` (§Phase 1) implémente le pipeline SPECS v38 §7.2 en mode operational. Le pilote ne duplique pas les invariants SPECS v38 §3.1 + §6.1 + §10 : il pointe vers eux via le bloc `### Renvoi canonique et témoin validé`. Toute investigation ultérieure suit ce même pipeline.

---

## 3. Phase 2 : Synthèse par cluster

### 3.1 Définition opérationnelle du cluster

Un cluster est un regroupement de 2-N enquêtes partageant un verrouillage, un mécanisme ou une chronologie commune. Identification manuelle par l'opérateur après synthèse des dossiers Phase 1.

### 3.2 Format et contraintes

Sortie : `investigations/<sujet>/_synthese/synthese_clusters.json` + `investigations/<sujet>/_synthese/synthese.json`.

**Schéma `synthese_clusters.json` (clé requise)** :

```json
{
  "clusters": [
    {
      "cluster_id": "verrouillage-constitutionnel",
      "these_cluster": "Le verrouillage constitutionnel 1958 bloque l'initiative populaire",
      "f_partages": ["F-002", "F-011", "F-013"],
      "transversalite_intra": "..."
    }
  ]
}
```

**Schéma `synthese.json` (clé requise)** :

```json
{
  "these_fil_rouge": "...",
  "theses_secondaires": ["...", "...", "..."],
  "transversalites_inter_clusters": ["...", "..."]
}
```

### 3.3 Mini-synthèse par cluster

Pour chaque cluster, le pilote génère :

- 1 phrase `these_cluster` (30-100 chars).
- 3-5 F-### partagés (identifiants).
- 1 transversalité intra-cluster (mécanisme transversal entre F-### du cluster).

### 3.4 Mnemolite `[ASPIRATIONNEL]`

1 requête cross-cluster par Phase 2. Log dans `mnemo_context.searches` (aspirationnel : à brancher, contrat documenté dans §7.5 et §10.1 de SPECS v39 ; non documenté dans SPECS v38).

### 3.5 Métriques Phase 2

| Métrique | Critère | Seuil GO |
|---|---|---|
| N2.1 | Tout cluster a ≥ 3 F-### partagés | GO si N >= 9 dans cumul |
| N2.2 | Transversalité intra-cluster documentée | GO par cluster |
| N2.3 | `synthese_clusters.json` parse OK | GO si JSON valide |
| N2.4 | `synthese.json` parse OK | GO si JSON valide |

---

## 4. Phase 2.5 : Rapport de Synthèse (lisible humain)

### 4.1 Définition opérationnelle

Document Markdown servant de rempart contre les hallucinations algorithmiques des phases suivantes. Lisible par un humain sans formation préalable au pipeline.

### 4.2 Format et contraintes

Sortie : `investigations/<sujet>/_synthese/rapport_synthese.md`. 5 sections obligatoires :

1. **Vue d'ensemble** (5-10 lignes).
2. **Thèse fil rouge + 2-4 thèses secondaires** : solidité, étendue, pourquoi / pourquoi pas, réfutation, confiance.
3. **Transversalités** (≥ 3 fiches par transversalité inter-cluster).
4. **Surprises, angles morts, apport Mnemolite**.
5. **Recommandation article** : Oui/Non, angle, ton, thèse fil rouge.

### 4.3 Métriques Phase 2.5

| Métrique | Critère | Seuil GO |
|---|---|---|
| N2.5.1 | Thèse fil rouge explicite (non tautologique) | GO si 30-500 chars |
| N2.5.2 | ≥ 3 transversalités inter-clusters identifiées | GO |
| N2.5.3 | Recommandation Oui/Non claire | GO |
| N2.5.4 | Volume 5 sections présentes | 5/5 |

---

## 5. Phase 2.6 : Plan d'Article

### 5.1 Définition opérationnelle

Document Markdown spécifiant la structure cible de l'article final. Chaque section H2 reçoit une sous-thèse défendant la thèse fil rouge + liste de marqueurs `[Lxx]` cibles.

### 5.2 Format et contraintes

Sortie : `investigations/<sujet>/_synthese/plan_article.md`. Spécifications :

- 3-5 sections H2 (peut aller jusqu'à 7 si transversalités multiples).
- Thèse centrale (1 phrase, 30-500 chars).
- Angle/ton : factuel, forensique ou conceptuel (réf. §6.3).
- Public cible : lecteurs Substack cible (ex : « lectorat politisé non-spécialiste »).
- Vérifications : liste des F-### dont l'absence invaliderait le plan.
- `## Sources` en fin, groupées par `### §1`, `### §2`, etc.

Chaque § défend la thèse fil rouge ; chaque § cite ≥ 1 fait sourcé.

### 5.3 Mapping SPECS v38 §12.1 (dossier → article)

| Section dossier (SPECS v38 §3.1) | Section article cible |
|---|---|
| §3 Métadonnées & index | (intro méta supprimée) |
| §4 Verrouillage | Sous-titre |
| §6 Acteurs nominaux | Corps §1 |
| §7 Mécanismes | Corps §2 |
| §8 Faits atomiques | Annexe inline §3 |
| §9 Scénarios | Corps §4 |
| §10 Dialectique | Corps §5 |
| §11 Historique | Encadré |
| §12 Recommandations | Conclusion |

### 5.4 Métriques Phase 2.6

| Métrique | Critère | Seuil GO |
|---|---|---|
| N2.6.1 | Thèse centrale explicite (30-500 chars) | GO |
| N2.6.2 | Chaque section a ≥ 1 fait sourcé | GO |
| N2.6.3 | Mapping SPECS v38 §12.1 respecté | GO |
| N2.6.4 | 3-5 sections H2 | GO |

---

## 6. Phase 3 : Article publié (3000-5000 mots)

### 6.1 Définition opérationnelle

Document Markdown final destiné à publication Substack. Format ARTICLE (introduction narrative → sections emboîtées → conclusion). Volume cible : 3000-5000 mots.

### 6.2 Les 9 LOI de Phase 3

| # | LOI | Description | Seuil |
|---|---|---|---|
| L1 | Accroche immédiate | Stat, citation ou question en ouverture. Pas de `§0 Méthodologie` (méthodologie en note FIN). | 1ère phrase ≤ 50 chars |
| L2 | Thèse unique | Chaque § défend la thèse fil rouge (validée CP1). Coupe les §§ qui dévient. | 1 thèse centrale + 0 digression |
| L3 | Sources fin d'article | URLs groupées `### §1`, `### §2`. Pas de glyphes `✦ / ✧ / ⁅ / ❧` visibles. Pas de `[n]` dans corps. Wiki < 50 %. | Tous §§ ont `### §X` |
| L4 | Ton clinique + lexique verrouillé | INTERDIT : « conçu pour », « choisi de », « protège », « laisse tuer », « sacrifie », « complique », « vidé », « enterrement », « dissidence », « ordre établi », « répression de ». Remplacer par constats : « aboutit mécaniquement à », « produit », « documente une inertie ». | 0 occurrence lexique interdit |
| L5 | Gras stratégique | ≤ 1 % du texte. | Compte `**` ≤ Volume × 0.01 |
| L6 | Compression | Zéro transition faible (Cependant, Mais, Voici, « Il est important de »). Sources ≤ 10 %. | 0 occurrence faible |
| L7 | Cross-links + navigation série | Inline : « comme démontré dans [Titre](url) ». Navigation série : *Article précédent/suivant*. Section « À voir aussi » 3-5 liens. | ≥ 3 cross-links + nav série |
| L8 | Auto-audit antagoniste | 6 types de failles : logique, mots-tic, micro-définitions, équation synthèse, sourcing, ton. | Audit GO post-rédaction |
| L9 | 3-éléments-minimum | Pour chaque section H2 d'article, piocher au moins 3 parmi les 5 catégories dérivées de SPECS v38 §3.1 list-index : positions (§4 Acteurs nominaux) ; causalités (§5 Mécanismes + §6 Faits atomiques) ; verrouillage structurel (§3 Verrouillage + §8 Perspectives dialectiques) ; projections (§7 Scénarios & prédictions + §9 Profondeur historique) ; recommandations (§10 Recommandations). Si une catégorie vide dans le dossier Phase 1, signaler explicitement dans la section. | Chaque §H2 : ≥ 3 catégories couvertes |

### 6.3 9 titres alternatifs

3 factuels/narratifs + 3 forensiques + 3 conceptuels. Pas de « choc ». Zéro pathos.

### 6.4 Métriques Phase 3

| Métrique | Critère | Seuil GO | Seuil HARD_FAIL |
|---|---|---|---|
| M3.1 Volume | `len(article.split())` | 3000 ≤ V ≤ 5000 | V < 2500 ou V > 6000 |
| M3.2 Sources | Comptage `### §X.md` groupées | ≥ 5 §§ sourcés | aucune source |
| M3.3 Cross-links | Compte `[Titre](url)` inline | ≥ 3 | 0 |
| M3.4 Gras stratégique | Compte `**` | ≤ Volume × 0.01 | > Volume × 0.05 |
| M3.5 Lexique L4 | grep lexique interdit | 0 | > 5 occurrences |
| M3.6 Compliance LOI L9 | Pour chaque §H2, ≥ 3 catégories présentes | 100% | < 50% |

### 6.5 Chemin de sortie

`articles/<date>_<sujet>_ARTICLE.md`. Substack publication après CP2 validation humaine.

---

## 7. Pipeline intégré (5 phases + 2 checkpoints)

### 7.1 Enchaînement opérationnel

Phase 1 × N enquêtes (N = nombre de dossiers Phase 1 produits) → Phase 2 × 1 (synthèse clusters) → Phase 2.5 × 1 (rapport lisible) → Phase 2.6 × 1 (plan cible) → Phase 3 × 1 (article).

### 7.2 CP1 (entre Phase 2 et Phase 2.5) : thèse fil rouge

Position : après Phase 2 (clusters identifiés + synthese_clusters.json + synthese.json produits). Output demandé : 1 phrase thèse fil rouge (30-500 chars) + 3-5 thèses secondaires (chacune F-### ancrés).

**Une seule passe** : le pilote notifie CP1 et attend l'action humaine `[V/M/R/E]`.

### 7.3 Validation interne Phases 2.5 et 2.6 (auto-audit, sans CP humain)

Position : entre Phase 2.5 (rapport_synthese.md) et Phase 2.6 (plan_article.md), et entre Phase 2.6 et Phase 3. Le pilote `prompt-v35.md` ne définit pas de CP humain à ces endroits : la validation passe par auto-audit antagoniste (LOI L8) + sub-agent CRITIQUE ou checklist manuelle du pilote.

Contrôles automatiques :
- **Après Phase 2.5** : thèmes `## ` présents (5 sections), thèse fil rouge non tautologique (30-500 chars), recommandation binaire (Oui/Non).
- **Après Phase 2.6** : `### §1` à `### §N` présents (3-5 sections), ≥ 1 fait sourcé par §, thèse centrale explicite, mapping SPECS v38 §12.1 respecté (cf. §5.3).

Si l'auto-audit retourne NO-GO sur l'un de ces points : le pilote produit un correctif automatique (sans rejeu complet) et re-soumettra au contrôle.

### 7.4 CP2 (après Phase 3) : article fini + auto-audit

Position : après Phase 3 (article_ARTICLE.md produit). Output : résumé (mots, thèse, URLs vérifiées, audit L8) → Action humaine `[V/M/R/E]`.

**Une seule passe** : pas d'aller-retour entre CP2 et un CP antérieur sans rejeu complet du segment.

### 7.5 Mnemolite, contrat inter-phases

Si Mnemolite UP : requêtes cross-phase log dans `mnemo_context.searches` (aspirationnel). Si Mnemolite DOWN : HALTE inconditionnel sans produire de fichier (réf. SPECS v39 §10.1 Backlog vague 2).

### 7.6 Arrêt pipeline

À chaque CP, l'opérateur peut répondre R (refus). Le pipeline s'arrête. **Aucun rejeu partiel n'est autorisé dans ce cas : le pilote redémarre depuis la phase correspondante avec consigne explicite.** Cette règle s'applique aux refus CP1 / CP2 uniquement. Les validations internes entre Phases 2.5 et 2.6 (auto-audit antagoniste, cf. §7.3) tolèrent un correctif automatique partiel, sans rejeu complet.

---

## 8. Métriques bout-en-bout (KPI pipeline complet)

### 8.1 Métriques Phase 1 (rappel SPECS v38 §6.1)

Inchangé : M1-M8 (volume, traçabilité, sources, dates, mécanismes, sections, em-dashes, pseudo-invents). Cf. SPECS v38 §6.1.

### 8.2 Métriques Phase 2 à 2.6

| Phase | Métrique | Cible |
|---|---|---|
| Phase 2 | N2.1 F-### partagés par cluster | ≥ 3 |
| Phase 2 | N2.3+N2.4 JSONs valides | 100% |
| Phase 2.5 | N2.5.1 thèse fil rouge explicite | 100% |
| Phase 2.6 | N2.6.1 thèse centrale explicite | 100% |

### 8.3 Métriques Phase 3

Cf. §6.4 : M3.1 à M3.6.

### 8.4 Métriques end-to-end (KPI pipeline complet)

| Métrique | Critère | Cible |
|---|---|---|
| E2E.1 Latence totale | Phase 1 → Phase 3 | ≤ 5 min / enquête |
| E2E.2 Réutilisation F-### | Compte F-### dossier → F-### cité article | ≥ 70% |
| E2E.3 Transversalités inter-clusters | transversalités dans rapport_synthese | ≥ 3 |
| E2E.4 Conformité LOI L9 | % §§H2 avec ≥ 3 catégories | 100% |

---

## 9. Anti-patterns pipeline intégré

### 9.1 Anti-patterns Phase 1 (rappel SPECS v38 §10)

Pas de fabrication `[Lxx]`. Pas d'anglais. 1 `Source :` par dossier. 1 dossier = 1 source unique.

### 9.2 Anti-patterns Phase 2

- Clusters trop larges (> 10 enquêtes) : dilution de la `these_cluster`.
- Clusters trop étroits (1 enquête) : masquer un cluster via un singleton.
- Absence de transversalité intra-cluster : F-### juxtaposés sans causalité.

### 9.3 Anti-patterns Phase 2.5

- Thèse fil rouge floue (multi-thèses sans pivot).
- Transversalités inter-clusters sans matérialité (≥ 3 fiches non justifiées).
- Recommandation ambiguë (Oui/Non/Peut-être).
- Volume d'une section > 50% du rapport.

### 9.4 Anti-patterns Phase 2.6

- Section sans fait sourcé : `### §X` valide mais corps vide.
- Plan sans thèse centrale explicite.
- Mapping SPECS v38 §12.1 non respecté : cellules de mapping manquantes.
- Plus de 7 sections H2 (sur-découpage).

### 9.5 Anti-patterns Phase 3

- **Pathos** dans le ton (LEXIQUE L4).
- **Absence de sources** (`### §X` vide ou manquant).
- **Mélange factuel/conceptuel** dans le même § : un §H2 doit avoir un type dominant.
- **Dilution thèse** : sections qui dévient du fil rouge.
- **Gras excessif** (> 1 % du texte).

---

## 10. Backlog vague 2 (à venir)

### 10.1 Stabilisation Mnemolite

Mnemolite n'est pas documenté dans SPECS v38 ; son contrat aspirationnel est centralisé dans SPECS v39 §1.4 (cadre) et §7.5 (Mnemolite inter-phases). Tant que Mnemolite n'est pas branché, la validation pipeline repose sur checklists manuelles + sub-agent CRITIQUE.

### 10.2 Industrialisation validation algorithmique

Action : après stabilisation Sublimator + LLM hôte sur 5+ enquêtes (cf. SPECS v37 v2 §12 Test A/B juge de paix), reconsidérer la validation algorithmique Python si elle redevient utile.

### 10.3 Auto-audit antagoniste inter-phases

Action : étendre le sub-agent CRITIQUE pour couvrir Phases 2-3 (actuellement limité à Phase 1 M1-M8).

### 10.4 Métriques end-to-end (E2E.1 à E2E.4)

Action : instrumenter les métriques E2E.1 à E2E.4 sur Substack multi-utilisateurs. Aucun déploiement industriel sans cette instrumentation.

---

## 11. Application à l'enquête Substack (transition bout-en-bout)

### 11.1 Workflow type

1 enquête Substack = 1 dossier Phase 1 (cf. SPECS v38 §7.2) + 1 entrée dans Phase 2 (cluster individuel ou partagée).

### 11.2 N enquêtes → 1 article

N enquêtes (chacune avec son dossier Phase 1) → Phase 2 (clusters + transverses) → Phase 2.5 (rapport) → Phase 2.6 (plan) → Phase 3 (article Substack 3000-5000 mots).

### 11.3 Pipeline complet = 1 article depuis N enquêtes

Le pipeline complet produit 1 article final prêt à publication Substack. Volume cible article (LOI M3.1) : 3000-5000 mots. Le ratio rétention Phase 1 → Phase 3 doit être ≥ 70% (cf. E2E.2).

---

## 12. Exemple de référence : Pipeline RIC 18:00

### 12.1 Témoin Phase 1 (validé)

`investigations/2026-07-04-RIC/_quintessence/2026-07-04_18-00_referendum_initiative_citoyenne_dossier_v38.md` (3 533 mots, audit M1-M8 dont M1-M7 PASS, M8 NOGO soft noté dans SPECS v38 §9.1).

### 12.2 Témoin Phase 2 (à produire)

Le RIC 18:00 forme un cluster singleton « verrouillage constitutionnel 1958-RIC » dans `synthese_clusters.json`. Si d'autres enquêtes partagent le verrouillage constitutionnel 1958, fusion cluster possible.

### 12.3 Témoin Phase 2.5 (à produire)

Rapport lisible humain du RIC : `investigations/2026-07-04-RIC/_synthese/rapport_synthese.md`. Doit contenir les 5 sections obligatoires (cf. §4.2) avec thèse fil rouge « Le verrouillage constitutionnel 1958 bloque l'initiative populaire RIC depuis 2018 ».

### 12.4 Témoin Phase 2.6 (à produire)

Plan cible : `investigations/2026-07-04-RIC/_synthese/plan_article.md`. Mapping SPECS v38 §12.1 + 3-5 sections H2 + thèse centrale 30-500 chars.

### 12.5 Témoin Phase 3 (à produire)

Article : `articles/2026-07-XX_ric-verrouillage-constitutionnel_ARTICLE.md` (3000-5000 mots). Publication Substack après CP2.

---

## 13. Glossaire SPECS v39

### 13.1 Termes hérités de SPECS v38

Dossier forensique : livrable Markdown 1500-4000 mots à 10 sections préservant la trace vers la source. F-### : identifiant de fait atomique unique. Tier X : niveau de fiabilité de la source (1 = primaire, 2 = secondaire, 3+ = commentaire). Trace `[Lxx]` : référence forensique vers une ligne. Vecteurs Κ/Ψ/⏰/↕/🌐/€ : glyphes SYMBOLS.md. `@FETCH` : commande interne pour valider une URL. `grep -n` : commande shell pour mesurer la position exacte d'une ligne. Auto-Audit : validation des 8 métriques M1-M8.

### 13.2 Termes ajoutés par SPECS v39

- **Cluster** : regroupement manuel de 2-N enquêtes partageant un verrouillage ou un mécanisme.
- **Mini-synthèse** : 1 phrase `these_cluster` + 3-5 F-### partagés + 1 transversalité intra-cluster.
- **Transversalité intra-cluster** : mécanisme transversal entre F-### d'un même cluster.
- **Transversalité inter-cluster** : mécanisme transversal entre F-### de clusters différents.
- **Thèse fil rouge** : 1 phrase pivot défendue par l'article entier.
- **Plan d'article** : document Markdown spécifiant la structure cible de l'article final.
- **Cross-link** : lien inline `comme démontré dans [Titre](url)` vers un autre article Substack.
- **9 LOI Phase 3** : L1-L9, règles impératives de rédaction Phase 3 (cf. §6.2).
- **LOI L9 « 3-éléments-minimum »** : règle métier Round 4 (post-audit L8) : pour chaque §H2 d'article Phase 3, piocher au moins 3 parmi les 5 catégories dérivées de SPECS v38 §3.1 list-index : (1) positions via §4 Acteurs nominaux, (2) causalités via §5 Mécanismes + §6 Faits atomiques, (3) verrouillage structurel via §3 Verrouillage + §8 Perspectives dialectiques, (4) projections via §7 Scénarios & prédictions + §9 Profondeur historique, (5) recommandations via §10 Recommandations. Si une catégorie est vide dans le dossier Phase 1, signaler explicitement dans la section.
- **Auto-audit antagoniste** : 6 types de failles (logique, mots-tic, micro-définitions, équation synthèse, sourcing, ton) vérifiés après rédaction Phase 3 (cf. §6.2 LOI L8).

---

## Annexe - Historique des versions

| Version | Date | Changement principal |
|---|---|---|
| v37 v2 | 2026-06-15 | compress_summary ≤ 320 mots (échec rétention 5 %) |
| v38 v1 | 2026-07-06 15:00 | Dossier forensique Phase 1 (10 sections, traces `[filename.md:Lxx]`) |
| v38 v2 | 2026-07-06 18:30 | Fix bugs 1-5 (regex M2/M8, M3 sources externes, em-dash) |
| v38 v3 | 2026-07-06 21:45 | Traces courts `[Lxx]`, dossier dans `_quintessence/`, MAX_VOL=4000, résultats test A/B intégrés |
| v38 v3.1 | 2026-07-06 22:00 | §6 transformée en checklist manuelle (abandon validation algorithmique Python) |
| v39 v1 | 2026-07-06 23:30 | Pipeline complet : Phases 1-3 + 2 checkpoints (CP1, CP2) alignés avec le pilote + KPIs bout-en-bout + LOI Phase 3 formalisées + 9 titres alternatifs + Anti-patterns Phases 2-3 |
| v39 v1.1 | 2026-07-06 23:55 | Post-audit L8 antagoniste : NF1 (5ème catégorie LOI L9 `verrouillage structurel` couvrant §3 Verrouillage + §8 Perspectives dialectiques, mapping 4→5 catégories) ; NF2 (re-badge `impact` → `projections` couvrant §7 Scénarios + §9 Profondeur historique) ; NF3 (note §1.4 déclarant §3.1 list-index canonique, écartant §12.1 dossier-§X). Trace étendue à `prompt-v35.md` (LOI L9 round 3 → round 4) |
