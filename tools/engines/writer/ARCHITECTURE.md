# WRITER : Architecture et graphe de dépendances

**Rôle :** source unique de vérité sur le fonctionnement du moteur Writer : mission, pipeline, standard de prose, relecture et validation technique.
**Dernière mise à jour :** 2026-08-03
**Position dans la chaîne :** Truth Engine (enquête) → Sublimator (condensation) → **Writer (rédaction et audits)**

---

## §1 Mission et position

Writer produit la **prose forensique de blog** : ciselée, claire, pédagogique, rythmée, honnête, ancrée. Son objet est la **langue**, pas les faits : le fact-checking est fait en amont par KERNEL (enquête) et Sublimator (condensation). Ici, on travaille la langue.

**Le principe cardinal :** toute phrase doit justifier son existence par une information, une distinction conceptuelle ou un raisonnement. Les 9 principes du standard déclinent cette exigence.

**Délimitation des responsabilités :**
- Le moteur Writer **n'enquête pas** (KERNEL), **ne condense pas** (Sublimator), **ne vérifie pas les faits** (fait en amont, pont KERNEL-Writer à l'étape 2 du pipeline).
- Le reviewer **ne vérifie pas les faits**, ne juge pas la thèse : il vérifie la **conformité au standard**.
- La validation technique automatisée (`validate.py`) porte sur la typographie et les contraintes projet (em-dash, NBSP, guillemets).

---

## §2 Inventaire des fichiers

| Fichier | Rôle | Chargé par |
|---------|------|------------|
| `ORCHESTRATEUR.md` | Pipeline du moteur (5 étapes), règles, définition de la « critique fondée », pont KERNEL-Writer | Buffy, au début de chaque tâche d'écriture |
| `STANDARD.md` | Les 9 principes de la prose forensique, chacun avec exemple, contre-exemple et question d'auto-contrôle | Buffy avant d'écrire ; le reviewer pour vérifier |
| `prompts/review.md` | Prompt du relecteur de conformité (spawné via `code-reviewer-deepseek`) | Étape 4 Relecture |
| `validate.py` | Validation technique automatisée (8 contrôles) | Étape 5 Corriger, maximum 3 tentatives |

**Versioning.** La tête de `ORCHESTRATEUR.md` porte « v4.0 ». Le moteur a évolué au fil des audits : standard enrichi de contre-exemples (pédagogie par l'échec), définition explicite de la « critique fondée », et pont KERNEL-Writer (chaque fait du texte doit correspondre à un fait du dossier). L'historique des versions est porté par les commits et les audits du dossier.

---

## §3 Pipeline (5 étapes)

```
Demande d'écriture (article, page, réponse, essai)
   │
   ▼
Étape 1  Lire le standard      STANDARD.md + knowledge.md (contraintes projet)
   │
   ▼
Étape 2  Vérifier les faits    lire le FACT_REGISTRY du dossier (pont KERNEL-Writer)
   │                          si aucun dossier : étape optionnelle
   ▼
Étape 3  Écrire                appliquer le standard, chaque phrase gagne sa place
   │                          puis re-vérifier les faits (retour étape 2)
   ▼
Étape 4  Relecture             spawner code-reviewer-deepseek + prompts/review.md
   │                          conformité aux 9 principes (pas les faits, pas la thèse)
   ▼
Étape 5  Corriger + valider    intégrer les critiques fondées, une seule passe
                              python3 tools/engines/writer/validate.py <fichier>
```

**Étape 2 : le pont KERNEL-Writer.** Si le texte s'appuie sur un dossier d'enquête, lire le FACT_REGISTRY avant d'écrire. Après l'écriture, revenir ici : chaque fait affirmé dans le texte correspond-il à un fait du dossier ? Si un fait du texte ne correspond à aucun fait du dossier, le retirer ou le sourcer. Si un fait du dossier est absent du texte, c'est acceptable (le texte n'est pas tenu d'être exhaustif).

**Étape 5 : la « critique fondée ».** Une critique est fondée si elle identifie un écart précis au standard ET propose une amélioration sans affaiblir le sens. Sinon, l'écarter. À Buffy de proposer la correction. Une seule passe de correction, pas de boucle. Maximum 3 tentatives de validation ; au-delà, signaler à l'utilisateur.

---

## §4 Le standard de prose (9 principes)

| # | Principe | Question d'auto-contrôle | Exemple de violation |
|---|----------|--------------------------|----------------------|
| 0 | **Exact** | La phrase dit-elle exactement ce qui est vrai, ou arrondit-elle pour l'effet ? | « L'IA contrôle tous les médias » (absolus, terme impropre) |
| 1 | **Ciselé** | Si je retire ce mot, la phrase perd-elle une information ? | « Il est important de souligner que… » (remplissage) |
| 2 | **Soutenu, contemporain, naturel** | Cette phrase pourrait-elle être prononcée par un journaliste du Monde sans rupture de registre ? | « Force est de constater que… » (formule « écriture IA ») |
| 3 | **Forensique** | Le lecteur voit-il le mécanisme ou seulement les faits ? | « Les médias mentent » (aucune chaîne causale) |
| 4 | **Clair** | Une lecture à voix haute buterait-elle sur un passage ? | Pronom sans référent, nominalisations en cascade |
| 5 | **Pédagogique** | Un lecteur qui découvre le sujet comprendrait-il ce paragraphe ? | Concept abstrait jamais ancré (« hétérotélie » non défini) |
| 6 | **Rythmé** | Les trois dernières phrases ont-elles la même structure et la même longueur ? | Trois phrases identiques accumulées sans progression |
| 7 | **Intraitable** | Cette phrase affirme-t-elle plus que ce que les faits permettent ? | Prudence bureaucratique, grandiloquence non méritée |
| 8 | **Ancré** | Depuis combien de paragraphes le lecteur n'a-t-il pas touché du concret ? | Trois paragraphes abstraits sans fait, chiffre, date, lieu |

Chaque principe du `STANDARD.md` est enseigné par **l'exemple et le contre-exemple** : la phrase qui viole le principe, pourquoi, et comment la corriger. Cette pédagogie double (positif + négatif) est la moitié de l'apprentissage du modèle.

---

## §5 Flux de données

```
Demande utilisateur (texte français publiable)
   │
   ▼
FACT_REGISTRY du dossier (si enquête) ──► contexte factuel de référence
   │
   ▼
WRITER : prose (article, page, réponse, essai)
   │
   ▼
code-reviewer-deepseek + prompts/review.md : conformité au standard
   │
   ▼
validate.py : typographie et contraintes projet (0 em-dash, NBSP, guillemets)
   │
   ▼
Texte final publiable
```

**Contraintes projet appliquées en permanence** (depuis `knowledge.md`) : 0 em-dash (U+2014) dans les articles publiés, espaces insécables avant « : ; ! ? », guillemets français équilibrés (« »), anti-sycophancy, pas d'anglicisme non justifié.

---

## §6 Validation

1. **Relecture de conformité** (étape 4) : le reviewer reçoit le texte + le standard. Il traque les écarts aux 9 principes. Il ne vérifie pas les faits, ne juge pas la thèse, ne propose pas de correction : il signale le défaut et le principe violé. Format : deux listes, maximum 12 observations (Bloquants / Majeurs), une liste « À conserver », une question ouverte en clôture.
2. **Validation technique automatisée** (étape 5) : `validate.py` vérifie 8 contrôles :
   - 0 em-dash (U+2014) et 0 en-dash (U+2013) ;
   - 0 espace simple avant « : ; ! ? » (NBSP exigée) ;
   - guillemets français équilibrés (« = ») ;
   - compte de mots dans la cible (± 15 %) si `--cible-mots` fourni ;
   - chiffres clés présents si `--chiffres` fourni ;
   - liens/emails présents si `--liens` fourni ;
   - 0 double espace.
   Exit code : 0 si tout est OK, 1 si au moins une violation.

---

## §7 Problèmes connus et dette technique

- **La vérification factuelle reste manuelle.** Le pont KERNEL-Writer (étape 2) repose sur la lecture du FACT_REGISTRY par le pilote. Il n'existe pas de script automatisé croisant chaque fait du texte avec le registre du dossier. Le reviewer ne vérifie pas les faits par construction : la responsabilité factuelle incombe au pilote.
- **Une seule passe de correction.** La boucle est volontairement limitée (pas de régression infinie). En contrepartie, un texte complexe peut conserver des écarts mineurs non traités dans la passe.
- **Versioning non unifié.** La tête de `ORCHESTRATEUR.md` porte v4.0 ; l'historique des évolutions (contre-exemples, critique fondée, pont KERNEL-Writer) n'est pas tracé dans un changelog formel au sein du dossier.
- **`validate.py` ne couvre pas la Phase 3 complète.** Il vérifie la typographie et les contraintes projet, mais pas la conformité aux 9 principes (qui relève du reviewer LLM) ni les KO sentences, la densité des sources ou les liens internes d'un article long.

---

## §8 Recommandations

| ID | Action | Effort | Impact |
|----|--------|--------|--------|
| R1 | Ajouter un script automatisé de croisement fait du texte ↔ FACT_REGISTRY du dossier (pont KERNEL-Writer mécanisable) | 2 h | HAUT |
| R2 | Documenter le changelog des versions du moteur (v4.0 → v4.x) dans `ORCHESTRATEUR.md` | 20 min | MOYEN |
| R3 | Étendre `validate.py` avec un contrôle des liens internes relatifs d'un article (résolution de chemins) | 30 min | MOYEN |
| R4 | Créer `tools/audit_phase3_em_dash.py` (audit zéro em-dash des articles publiés, cf. `knowledge.md`) et le brancher au pipeline Writer | 30 min | HAUT |
| R5 | Prévoir une passe de relecture ciblée sur les textes longs (article > 3 000 mots) pour compenser la limite de la passe unique | 30 min | MOYEN |

---

*Architecture v1 : Writer. Dernière mise à jour : 2026-08-03. Source vivante : `tools/engines/writer/`. Les copies figées dans un dossier d'enquête (`10_protocole/`) sont des instantanés datés.*
