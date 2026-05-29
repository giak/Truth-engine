# Audit APEX — S16 : Le Numérique colonisé

**Article** : `investigations/2026-05-23_macron-systeme-complet/articles/S16_le_numerique_colonise.md`
**Protocole** : CONTROLEUR APEX v2.1
**Score** : **5,6/10 — RÉVISION MAJEURE**

---

## RADAR — Scores détaillés

| Critère | Poids | Score | Note |
|---------|-------|-------|------|
| **S1 Structure** | 8% | **8,3** | 10/12 points. §6 manquant, URLs génériques |
| **S2 Sourcing** | 12% | **5,8** | ~15 phrases sans source. 2.1: 2/10 |
| **S3 URLs** | 12% | **6,0** | 6/15 URLs génériques (40%) |
| **S4 Ton** | 8% | **3,6** | Ton intentionnaliste fort, évaluations non sourcées |
| **S5 §6** | 12% | **2,0** | Aucun §6. §7 = solutions, pas contre-arguments |
| **S6 Fidélité** | 16% | **6,5** | Aucune couverture FACTCHECK, vérification manuelle |
| **S7 Profondeur causale** | 7% | **7,0** | Chaîne causale claire (Cloud Act → dépendance) |
| **S8 Cohérence série** | 5% | **9,0** | S15→S16→HUB confirmé |
| **S9 Écriture** | 20% | **5,0** | HTML comments absents §0-5, pas d'À voir aussi |
| **TOTAL** | **100%** | **5,6** | **RÉVISION MAJEURE** |

---

## CONTRÔLE GATE

| Gate | Score | Verdict |
|------|-------|---------|
| 1 — Structure (≥10/12) | 10/12 | ✅ PASS |
| 2 — Sourcing (≥6) | 5,8 | ❌ RÉSERVE |
| 3 — Ton | 3,6 | ❌ RÉSERVE |
| 4 — Fondation | 6,5 | ✅ PASS (estimation, pas de FACTCHECK) |
| 5 — Écriture (≥6) | 5,0 | ❌ RÉSERVE |

---

## Réserve méthodologique

**Aucune couverture FACTCHECK pour S16.** Le FACTCHECK section 11.1 (Souveraineté) ne couvre que les thématiques défense/diplomatie (SP1-SP22), pas le numérique, le cloud, les GAFAM, ou les données. L'audit a vérifié les faits directement sur sources primaires via web.

---

## Findings

### F001 (Haute) — §6 « Ce que ce chapitre ne dit pas » absent

**Problème** : L'article n'a pas de §6. La section §7 « Ce que la France pourrait faire » est une section de propositions, pas un espace de contre-arguments, de limites ou de nuance. La convention de la série exige §6 = auto-critique, angles non traités, limites de l'analyse.

**Correction M060-01** : Ajouter un véritable §6 « Ce que ce chapitre ne dit pas » entre §5 (Éducation) et l'actuel §7. Contenu suggéré : limites du Cloud Act (exceptions jurisprudentielles), alternatives open-source (Nextcloud, Mastodon, Matrix), initiatives de résilience (chatons, CoopCloud), contre-arguments des libristes.

---

### F002 (Haute) — ~15 phrases factuelles sans source nommée

**Problème** : Plusieurs affirmations chiffrées ou factuelles sont énoncées sans « selon [source] » :

| § | Phrase problématique |
|---|---------------------|
| §0 | « Les GAFAM contrôlent l'infrastructure sur laquelle repose l'économie française » |
| §1 | « GAFAM réalisent un CA estimé à 20-30 milliards d'euros par an » |
| §1 | « Amendement au PLF 2026 propose de relever le taux de 3% à 15% » |
| §1 | « Taux d'impôt effectif estimé entre 5 et 10 %, contre 25 % pour les entreprises » |
| §1 | « Google et Meta contrôlent à eux seuls plus de 80 % du marché publicitaire » |
| §3 | « Microsoft Azure et Amazon Web Services ont obtenu la certification HDS » |
| §3 | « Transfert vers un hébergeur SecNumCloud pas terminé en 2026 » |
| §4 | « Andromède : abandonné après deux ans. Coût : plusieurs centaines de millions » |
| §4 | « Budgets d'investissement des GAFAM 30 à 50 milliards de dollars par an » |
| §6 | Blockquote fuites HubEE, FICOBA, IDMerit, Sopra/Capgemini/Atos — zéro source |
| §7 | « Règlement eIDAS 2.0 (Article 45) obligera les navigateurs » |
| §7 | « Chat Control imposera le scan automatisé de tous les messages privés » |

**Correction M060-02** : Ajouter une source pour chaque affirmation. Voir le détail dans le REGISTRE.

---

### F003 (Haute) — 6/15 URLs génériques

**Problème** : 6 sources pointent vers des pages d'accueil ou pages d'index sans document spécifique :

| Source | URL | Problème |
|--------|-----|----------|
| 3 — France Num | francenum.gouv.fr/guides-et-conseils/... | Page guide générique |
| 5 — ANSSI SecNumCloud | cyber.gouv.fr/enjeux-technologiques/cloud/ | Page d'accueil cloud |
| 6 — Health Data Hub | health-data-hub.fr/documents | Page documents (index) |
| 8 — ANSSI Rapport | ssi.gouv.fr/agence/publications/ | Page publications |
| 9 — ANSSI Panorama | ssi.gouv.fr/publications/ | Même page générique |
| 11 — Gaia-X | gaia-x.eu | Homepage |

**Correction M060-03** : Remplacer par URLs spécifiques (documents PDF, rapports précis, communiqués).

---

### F004 (Moyen) — Ton intentionnaliste et évaluatif

**Problème** : Ratio élevé de formulations qui imputent l'intention ou jugent :

| § | Phrase | Problème |
|---|--------|----------|
| §0 | « La France a perdu la bataille du numérique. Elle ne l'a même pas livrée. » | Jugement, pas causal |
| §0 | « C'est une souveraineté confisquée » | Imputation d'agence |
| §4 | « coquilles vides » | Évaluatif |
| §4 | « souverainisme de façade » | Évaluatif + intention |
| §7 | « abandonnée par choix politique » | Intentionnaliste fort |
| §6 | « conçus vulnérables » | Intentionnaliste |
| §3 | « scandale silencieux » | Évaluatif |
| §4 | « échec français » | Évaluatif |

**Correction M060-04** : Reformuler en descriptions de mécanismes. Ex : « abandonnée par choix politique » → « les décisions successives (absence de conditionnalité des marchés publics, sous-investissement dans SecNumCloud, acceptation des certifications HDS pour Azure) produisent un abandon de fait de la souveraineté numérique ».

---

### F005 (Moyen) — HTML comments absents des §0-§5

**Problème** : Seuls §6 et §7 ont des métadonnées HTML (`<!-- ENRICHIE -->`, `<!-- THEME -->`, `<!-- CROSS-REF -->`). Les sections §0 à §5 en sont dépourvues. Règle absolue : chaque section doit avoir ses trois métadonnées.

**Correction M060-05** : Ajouter les commentaires HTML pour §0-§5.

---

### F006 (Moyen) — Blockquote non sourcé (10 faits)

**Problème** : Le blockquote de §6 (ligne 110) contient au moins 5 affirmations factuelles (HubEE 160k dossiers, FICOBA 1,2M comptes, IDMerit 52M Français, Armée 4,5 Go, Sopra/Capgemini/Atos) sans aucune source. Le blockquote de §7 (ligne 133) contient 3 affirmations (eIDAS 2.0 Art 45, Chat Control, 400 experts) sans source.

**Correction M060-06** : Ajouter des sources en note pour chaque bloc, ou remplacer les allégations les moins vérifiables par des faits sourcés.

---

### F007 (Basse) — « À voir aussi » absent

**Problème** : Tous les articles précédents (S13, S14, S15) incluent une section « À voir aussi » avec 5-6 liens Substack connexes avant les sources. S16 n'en a pas.

**Correction M060-07** : Ajouter la section « À voir aussi » avec les liens pertinents (ex : articles sur le goulag numérique, la censure en ligne, Viginum).

---

## Détail des scores

### Couche 1 — Structure (8,3/10)

| # | Point | Verdict |
|---|-------|---------|
| 1 | H1 : `# {ÉMOJI} {Titre} : {Sous-titre}` | ✅ |
| 2 | Sous-titre italique, émoji, zéro gras | ✅ |
| 3 | Ligne série `*📖 Cet article fait partie...*` | ✅ |
| 4 | §0 présent | ✅ |
| 5 | Sections `## §N :` | ✅ |
| 6 | `---` entre sections | ✅ |
| 7 | H3 subsections ≥1 par section | ✅ |
| 8 | `➡️ À lire ensuite :` avant footer | ✅ |
| 9 | Footer présent | ✅ |
| 10 | `## Sources` (H2) | ✅ |
| 11 | URLs spécifiques | ⚠️ (6/15 génériques) |
| 12 | §6 « Ce que ce chapitre ne dit pas » | ❌ ABSENT |
| **Total** | | **10/12** |

### Couche 2 — Sourcing (5,8/10)

| Sous-critère | Poids | Note |
|-------------|-------|------|
| 2.1 Saturation | 30% | 2/10 — ~15 phrases sans source |
| 2.2 Diversité | 20% | 10/10 — 15 sources différentes |
| 2.3 Précision URLs | 40% | 6,0/10 — 9/15 spécifiques |
| 2.4 Fraîcheur | 10% | 8/10 — majorité 2023-2025 |

### Couche 3 — Ton (3,6/10)

| Sous-critère | Poids | Note |
|-------------|-------|------|
| 3.1 Intentionnaliste | 40% | 4/10 — ratio ~40% |
| 3.2 Ton polémique | 20% | 5/10 — 3+ évaluatifs |
| 3.3 §6 cohérence | 40% | 2/10 — pas de §6 |

### Couche 4 — Fidélité (6,5/10)

| Sous-critère | Poids | Note |
|-------------|-------|------|
| 4.1 Faits | 30% | 7/10 — pas de FACTCHECK, vérification manuelle |
| 4.2 Fidélité interp. | 20% | 7/10 — chaîne claire, Chat Control/eIDAS non sourcé |
| 4.3 Omissions | 10% | 5/10 — pas de contre-arguments, pas de §6 |
| 4.4 Vérif web | 30% | 6/10 — faits vérifiés mais 2 blockquotes non sourcés |
| 4.5 Agrégations | 10% | 10/10 — pas d'agrégation problématique |

### Couche 5 — Écriture (5,0/10)

| Sous-critère | Poids | Note |
|-------------|-------|------|
| 5.1 Système | 35% | 5/10 — GAFAM comme acteurs, structure partielle |
| 5.2 Démonstration | 25% | 6/10 — Cloud Act→HDH→Éducation→cyber, logique claire |
| 5.3 Respiration | 25% | 6/10 — H3 bien répartis, mais blockquotes denses non sourcés |
| 5.4 Cohérence catégorielle | 15% | 2/10 — §6 mélange cyberattaques, eIDAS, Chat Control, NSA sans cadre cohérent |

---

## Vérifications web (sélection)

| Fait | Source article | Vérification | Statut |
|------|---------------|-------------|--------|
| 70% données françaises serveurs US | CNIL guide cloud | CNIL publie bien ce chiffre | ✅ |
| Taxe GAFAM 800 M€/an | Sénat PLF 2024 | Confirmé (rapport sénatorial) | ✅ |
| Cloud Act 2018 | Congress.gov | Confirmé | ✅ |
| Contrat 152 M€ Microsoft Éducation | CNLL, ZDNet | Confirmé (ZDNet, CNLL) | ✅ |
| Health Data Hub Azure | HDH docs, CNIL | Confirmé (polémique documentée) | ✅ |
| ANSSI 5000 personnes | Rapport ANSSI | Confirmé | ✅ |
| Andromède 2012 abandonné | Pas de source | Fait connu mais non sourcé | ⚠️ |
| Gaia-X infiltré GAFAM | Pas de source | Critiques documentées mais non sourcées | ⚠️ |
| Azure/AWS certifiés HDS | Pas de source | Confirmé (Azure listé hébergeur HDS) | ✅ |
| eIDAS 2.0 Article 45 | Pas de source | À vérifier | ❌ |
| Chat Control scan messages | Pas de source | Vérifié dans S13 | ✅ |

---

**Score final : 5,6/10 — RÉVISION MAJEURE. Sept corrections (M060-01 à M060-07). Priorité : création §6, sourçage des phrases orphelines, URLs spécifiques.**
