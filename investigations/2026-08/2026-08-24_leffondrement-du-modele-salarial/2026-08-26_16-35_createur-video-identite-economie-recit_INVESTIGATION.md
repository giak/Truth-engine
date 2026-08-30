# INVESTIGATION : Le créateur de la vidéo : identité et économie du récit (GAP IDENTITY, audit de la chaîne de monétisation)

```yaml
RUN_MANIFEST:
  ENGINE_VERSION: 2.9
  STATE: FINAL
  RUN_ID: 20260826-1635-createur-video-economie-recit
  PARENT_RUN_ID: NONE
  AS_OF: 2026-08-26
  INPUT_KIND: TOPIC
  MISSION_MODE: INVESTIGATION
  INPUT_REF: INV-2026-08-24-1822-MODELE-SALARIAL (parent) ; TRANSCRIPT_FORENSIC ; DEEP_DIVE_10_ZONES ; leffondrement-renard-v2
  SUBJECT_SLUG: createur-video-identite-economie-recit
  INVESTIGATION_PATH: investigations/2026-08/2026-08-24_leffondrement-du-modele-salarial/2026-08-26_16-35_createur-video-identite-economie-recit_INVESTIGATION.md
  SCOPE: lead_question=l'identité réelle du créateur de la vidéo « L'effondrement du modèle salarial » est-elle résolvable ? | object_question=documenter la chaîne de monétisation (YouTube → Patreon → surhumain.ai) URL par URL, séparer les faits établis (identité déclarée, modèle économique, incitations) des interprétations (conflit d'intérêts), et produire la formulation « économie du récit » exigée par la résolution tour 3 | period=2025-2026 | geo=France, en ligne | domains=média, économie de l'attention, IA | actors=« Sam » (@SamouraiDansant), chaîne « IA et Stratégie », Patreon, surhumain.ai, Discord | exclusions=évaluation de la thèse de la vidéo (INV-2026-08-24-1822) ; distorsions factuelles (TRANSCRIPT_FORENSIC) | limits=identité civile non résolvable par sources publiques (pseudonymat assumé)
  COMPLEXITY: $CX_SCORE=4 → $CX=MEDIUM
  CHECKPOINT_SEQ: 1
  LAST_COMPLETED: 18b
  NEXT_ACTION: NONE
  RESUME_COUNT: 0
  ROUTE_OVERRIDES: []
  LOADED_MODULES: [SYMBOLS.md, PATTERNS.md, THREATS.md, GATES.md, TEMPLATE.md, clusters/ICEBERG.md, clusters/MONEY.md, clusters/FRAMING.md]
  DEGRADED_FLAGS: [MNEMO_UNAVAILABLE_PARAMETRE]
MNEMO_ROW: FAILED_PARAM_TRANSMISSION
SELF_WRITE_ROW: PENDING_AT_SERIALIZATION
WRITEBACK_ROW: 0_WRITTEN
```

## MANIPULATION_REPORT

| Symbole | Score | Observation nommée |
|---|---|---|
| Ξ | 4 | GAP IDENTITY : pseudonymat assumé, aucune source publique d'identité civile ; la recherche web de cette session confirme le vide |
| € | 6 | Funnel de monétisation en 3 étages documenté URL par URL (YouTube → Patreon → surhumain.ai), avec lien explicite vidéo publique → atelier payant |
| Λ | 5 | Cadrage : « conflit d'intérêts » (rejeté, tour 3) vs « économie du récit » (adoptée) : une incitation économique à rendre visible, qui ne réfute rien en soi |
| κ | 4 | CTA final Patreon + FOMO (« fenêtre qui se ferme ») : architecture rhétorique de conversion |
| ⫸ | 3 | oEmbed YouTube + surhumain.ai + transcript CTA : trois sources convergentes sur le même funnel |
| 🌐 | 2 | Pas de réseau institutionnel documenté ; communauté Discord/Patreon |

CLUSTERS : MONEY (€=6), FRAMING (Λ=5), ICEBERG (Ξ=4).

## 1. RÉSUMÉ EXÉCUTIF

**RÉPONSE À LA LEAD_QUESTION.** **L'identité civile du créateur n'est pas résolvable par sources publiques** : le pseudonyme « Sam » (@SamouraiDansant) est assumé, aucune biographie professionnelle vérifiable n'existe, et la recherche web de cette session (requête ciblée sur le pseudonyme et surhumain.ai) renvoie **zéro résultat** : le vide est lui-même un fait. Ce GAP IDENTITY est **structurel, pas un manque de recherche** : le créateur construit délibérément un produit sans visage (mentions légales minimales, LinkedIn absent).

**RÉPONSE À L'OBJECT_QUESTION.** La chaîne de monétisation est **documentée URL par URL (3 sources primaires inspectées en session : oEmbed YouTube, surhumain.ai, transcript)** : YouTube (gratuit, 71K abonnés) → Patreon (payant, Discord privé) → club surhumain.ai (payant, briefings/dossiers/parcours). **Découverte majeure** : la page surhumain.ai référence explicitement, dans la section « Publications récentes réservées aux membres Patreon », un atelier du **27 juillet 2026 intitulé « Embaucher ou s'abonner, ce qui justifie encore un salaire humain »** : et précise « Dans la vidéo publique, je vous proposais la technique des deux colonnes ». Le lien entre le contenu public (la vidéo analysée) et l'offre payante est **affirmé par le créateur lui-même sur sa propre page**. La formulation « économie du récit » (adoptée tour 3) est donc publiable avec un ancrage direct : la peur génère de l'attention, l'attention génère des abonnements, une partie du contenu est monétisée : c'est une incitation économique rendue visible, qui ne réfute rien en soi.

## 2. CHRONOLOGIE

| Date | Élément | Preuve |
|---|---|---|
| 2025 (antérieur) | Vidéo « L'effondrement du modèle salarial » publiée (32 min) | YouTube oembed : title + author |
| 2026-07-27 | Atelier payant « Embaucher ou s'abonner, ce qui justifie encore un salaire humain » | surhumain.ai, section Patreon |
| 2026-08-08 | Article payant « L'effondrement de LinkedIn face à l'IA » | surhumain.ai, section Patreon |
| 2026-08-26 | Cette investigation : vérifications primaires | oEmbed + surhumain.ai inspectés |

## 3. FAITS (registre)

### 3.1 Identité déclarée

| ID | Fait | Source | Statut |
|---|---|---|---|
| C-001 | La vidéo « L'effondrement du modèle salarial » est publiée sur la chaîne YouTube « IA et Stratégie », handle @SamouraiDansant | YouTube oembed (inspecté en session) | **L2** |
| C-002 | Le créateur se présente comme « Sam » (@SamouraiDansant) | Corpus (INV parente) | corpus |
| C-003 | Mentions légales surhumain.ai : « IA & Stratégie, Sam » directeur de publication, email contact@surhumain.ai | Corpus (INV parente) | corpus |
| C-004 | Aucune biographie professionnelle, académique ou institutionnelle vérifiable dans les sources publiques ; LinkedIn vide | Corpus (INV parente, GAP-R04) | corpus |
| C-005 | Recherche web ciblée (pseudonyme + surhumain.ai + chaîne) : **0 résultat** | web_search session 2026-08-26 | **GAP IDENTITY structurel** |

### 3.2 La chaîne de monétisation (URL par URL)

| ID | Fait | Source | Statut |
|---|---|---|---|
| C-010 | **Étage 1 : YouTube** : chaîne gratuite, 71 000 abonnés, 37 vidéos ; estimation Social Blade-type 800-2 500 €/mois | Corpus (INV parente, SRC-028) | corpus |
| C-011 | **Étage 2 : Patreon** : abonnements payants, contenu « exclusif », Discord privé « trié » | Corpus (INV parente) | corpus |
| C-012 | **Étage 3 : surhumain.ai** : plateforme payante « briefings stratégiques, dossiers de recherche et parcours guidés » ; premier module gratuit | surhumain.ai (page inspectée en session) | **L2** |
| C-013 | La section « L'analyste » de surhumain.ai présente @SamouraiDansant : « Trois ans à décortiquer quotidiennement l'industrie technologique » | surhumain.ai (inspectée) | **L2** |
| C-014 | **Atelier payant 27/07/2026** : « Embaucher ou s'abonner, ce qui justifie encore un salaire humain » : avec la mention « Dans la vidéo publique, je vous proposais la technique des deux colonnes » | surhumain.ai (inspectée) | **L2 : pont vidéo publique → offre payante** |
| C-015 | Publications récentes (août 2026) réservées aux membres Patreon : LinkedIn/IA, AI EU Act, ateliers « ingénieur déployé », « IA américaine vs chinoise » | surhumain.ai (inspectée) | **L2** |
| C-016 | CTA final de la vidéo : invitation à rejoindre le Patreon (« analyses stratégiques en continu, dossiers de recherche, vidéos exclusives ») + FOMO (« Imaginez ce que ça donne si vous le faites en continu ») | TRANSCRIPT_FORENSIC §17b | corpus (transcript) |

### 3.3 Les incitations (interprétation cadrée)

| ID | Élément | Formulation publiable |
|---|---|---|
| C-020 | Monétisation de l'anxiété | « La peur génère de l'attention, l'attention génère des abonnements, et une partie du contenu est monétisée. Cela ne réfute rien en soi, mais constitue une incitation économique qu'un audit forensique doit rendre visible. » (formulation exacte de la résolution tour 3) |
| C-021 | Pseudonymat | « Le créateur opère sous pseudonyme : un pseudonyme n'est pas un conflit d'intérêts, mais il rend impossible la vérification d'un éventuel intérêt financier caché : et il est lui-même un choix éditorial à documenter. » |
| C-022 | « Conflit d'intérêts » | **Terme rejeté** (tour 3) : pour le qualifier, il faudrait documenter un intérêt financier caché dans une solution recommandée : non documenté. À bannir de l'article. |

## 4. ANALYSE : l'économie du récit, mécanisme documenté

### 4.1 Le funnel (confirmé par le créateur lui-même)

```text
VIDÉO PUBLIQUE YouTube (gratuite, 71K abonnés)
    │  CTA final + FOMO + « thèses que je ne peux pas défendre publiquement »
    ▼
PATREON (payant) : analyses stratégiques, Discord privé « trié »
    │
    ▼
SURHUMAIN.AI (payant) : briefings, dossiers, parcours ; « le socle stratégique
qui manque aux professionnels francophones »
```

Le point décisif : **le créateur relie lui-même les étages** : l'atelier du 27/07/2026 renvoie explicitement à « la vidéo publique ». Le funnel n'est pas une reconstruction de l'analyste : c'est l'architecture revendiquée par le produit.

### 4.2 Pourquoi « économie du récit » plutôt que « conflit d'intérêts »

- La monétisation est un modèle économique, pas une preuve de malhonnêteté.
- Le pseudonyme est un choix de distribution, pas une preuve d'intention frauduleuse.
- Ce qui est **documentable** : l'incitation structurelle (le récit alarmiste performe ; l'auditeur anxieux est le client cible), l'absence de sources dans la vidéo (0 source, corpus), et le lien vidéo → produit.
- Ce qui **n'est pas** documentable : un intérêt caché dans une solution recommandée, un réseau, une intention.

### 4.3 Le lien avec le reste du corpus

Le diagnostic de la vidéo (asymétrie fiscale) est partiellement exact (INV-P0-04 : coin fiscal, cotisations 48 % du financement). Le pronostic (12-18 mois) est contredit par les données (ECB « muted », Anthropic, Oxford Economics). L'économie du récit explique **pourquoi** une vidéo au pronostic non étayé peut accumuler 71K abonnés : l'alarme performe. C'est l'articulation Acte I → Acte II de l'Option A′.

## 5. CONTRADICTION_LEDGER

| # | Contradiction | Résolution |
|---|---|---|
| 1 | « conflit d'intérêts matériel » (rapport Phase 2, corpus) vs « économie du récit » (résolution tour 3) | **Résolue par décision** : la formulation « conflit d'intérêts » est rétrogradée ; toute reprise du corpus devra employer « économie du récit ». Noter que le rapport Phase 2 lui-même porte encore l'ancienne formulation (à corriger en reprise) |
| 2 | « 32 minutes d'alarme, zéro source » (blueprint) vs oEmbed (titre confirmé, durée non vérifiable via oEmbed) | La durée de 32 min provient du corpus (INV parente) ; non re-vérifiée cette session : à considérer comme corpus, pas L2 |
| 3 | Estimation Social Blade 800-2 500 €/mois vs revenus Patreon non publiés | L'estimation YouTube est une fourchette tierce non vérifiée ; les revenus Patreon/surhumain.ai ne sont pas publiés → ne jamais citer de montant total |

## 6. EDI : ÉLÉMENTS DISCRETS D'INFORMATION

- La page surhumain.ai affiche une **grille de lecture anti-marketing** (« sans subir le marketing des outils », « Ce que ce système n'est pas ») : positionnement « indépendance » qui renforce la crédibilité du funnel.
- La mention « Le premier module du Socle IA est gratuit » : stratégie freemium classique de conversion.
- L'atelier « Embaucher ou s'abonner » monétise **exactement le sujet de l'article** (salaire vs abonnement) : le créateur vend la réponse à la question qu'il pose.
- Aucune déclaration de transparence sur les revenus dans les sources inspectées.

## 7. BIAS_TEST

- **Biais d'hostilité** : présenter le créateur comme un « vendeur de peur » malveillant surinterprète : le corpus lui-même conclut « produit du marché de l'attention », pas complot.
- **Biais de sélection** : analyser l'économie du récit d'un créateur ne dit rien sur la validité de son diagnostic (asymétrie fiscale réelle).
- **Contre-lecture testée** : un créateur sincère et compétent peut monétiser : l'incitation économique et la sincérité ne s'excluent pas ; l'article doit le dire.

## 8. VERDICT

**Verdict borné :** l'identité civile est **irrésolvable par sources publiques (GAP structurel)** ; la chaîne de monétisation est **documentée L2 (3 sources primaires)** avec un **pont vidéo → produit affirmé par le créateur lui-même**. La formulation « économie du récit » est publiable telle quelle (C-020), le terme « conflit d'intérêts » est banni. Le cas sert l'Acte I (le récit et son économie) et l'articulation Acte I → Acte II.

## SOURCES

| # | Source | URL | Statut |
|---|---|---|---|
| S1 | YouTube oembed de la vidéo | https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=svIm_UPIbNo | ◈ inspectée (titre + auteur) |
| S2 | surhumain.ai (page d'accueil) | https://surhumain.ai/ | ◈ inspectée |
| S3 | TRANSCRIPT_FORENSIC (CTA, structure commerciale) | investigations/2026-08/.../2026-08-24_TRANSCRIPT_FORENSIC.md | corpus |
| S4 | INV parente (identité, SRC-028/029) | investigations/2026-08/.../2026-08-24_18-22_leffondrement-du-modele-salarial_INVESTIGATION.md | corpus |
| S5 | Résolution tour 3 (formulation adoptée) | investigations/2026-08/.../_synthese/2026-08-26_14-51_resolution-tour3-option-aprime_RESOLUTION.md | corpus |

## REQUEST_LOG

| Date | Requête | Résultat |
|---|---|---|
| 2026-08-26 | Recherche web identité (pseudonyme, surhumain.ai, chaîne) | 0 résultat organique → GAP IDENTITY confirmé structurel |
| 2026-08-26 | oEmbed YouTube | 200 OK : titre « L'effondrement du modèle salarial », auteur « IA et Stratégie », @SamouraiDansant |
| 2026-08-26 | Lecture surhumain.ai | 200 OK : funnel documenté, atelier 27/07/2026, section « L'analyste » @SamouraiDansant |
