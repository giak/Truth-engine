# Audit Adversarial — Orchestrateur v3 (Anti-Fragile)

**Date** : 2026-06-14 (v2 post-mortem → v3 design)
**Statut** : Spec — pré-implantation
**Système cible** : Ryzen 7 7840HS / Radeon 780M iGPU / 54GB DDR5 / Linux Mint 22.2
**Contexte** : v2 exécuté sur 1 article, 6/8 phases ont des défaillances qualitatives. v3 = refonte structurelle.

---

## §0 POST-MORTEM v2 — 8 défaillances diagnostiquées

L'audit v2 a été exécuté sur `2026-06-13_11-16_eloge_surface_levier_V2_ARTICLE.md` (4260 mots).
Résultat : 8 phases ont tourné mécaniquement, mais **6/8 produisent un output inutilisable**. Voici pourquoi.

### §0.1 Échec #1 — Phase 0 (phi4-mini) : confusion de rôle

**Symptôme** : Au lieu d'extraire `{genre, thèse, domaines critiques, audience, structure}`, le modèle produit un tableau "Problèmes identifiés" vide suivi de commentaires génériques en français approximatif.

**Cause racine** : Le prompt BLOCK:phase0_metatexte ne dit JAMAIS ce qu'il ne faut PAS faire. Le modèle reçoit SHARED:taxonomy (tableau des codes) + SHARED:rules (format de sortie avec tableau) + son BLOCK. Le format des SHARED blocks est tellement saillant que le modèle l'applique par défaut, même quand le BLOCK demande autre chose.

**Correction v3** : Phase 0 reçoit ZÉRO SHARED block. Son prompt est isolé, avec une instruction-barrière explicite : "NE PRODUIS PAS de tableau. NE PRODUIS PAS de codes FACT/LACUNA/etc. Extrais UNIQUEMENT les métadonnées listées ci-dessous."

### §0.2 Échec #2 — G2 (qwen3:8b think) : boucle de répétition

**Symptôme** : 53+ entrées identiques "17 milliards d'euros de concessions arrachées" avec numéros de ligne incrémentés mécaniquement (ligne 15, 36, 65, 73, 81... jusqu'à 296). Le modèle a "trouvé" la même critique partout et l'a régurgitée en boucle.

**Cause racine** : Absence de `num_predict` plafonné + mode "think" de Qwen3 qui amplifie la persévération. Le prompt dit "3-7 problèmes" mais ne donne pas de stop explicite. Le modèle, en mode raisonnement, associe chaque occurrence du motif "17 milliards" à une nouvelle ligne et produit une entrée.

**Correction v3** : 
1. `num_predict` plafonné à 300 tokens pour les phases 8B (assez pour 7 entrées, pas assez pour 53)
2. Anti-loop guard dans l'orchestrateur : si >12 entrées de tableau détectées dans l'output, tronquer et marquer comme [DÉGÉNÉRÉ]
3. Instruction-barrière dans le prompt : "Maximum 7 problèmes. Si tu dépasses, arrête-toi immédiatement."
4. Mode "think" désactivé pour G2 (le mode standard suffit pour la détection de problèmes logiques)

### §0.3 Échec #3 — G3 (35B MoE) : output tronqué

**Symptôme** : `[TRONQUÉ: length]` — le modèle a atteint la limite de `num_predict=4096` sans produire de contenu utile.

**Cause racine** : `num_predict=4096` est trop bas pour un deep-dive qui doit analyser un domaine entier. Le 35B MoE, avec sa verbosité naturelle, dépasse rapidement cette limite. De plus, `num_ctx=16384` dans l'audit.py (au lieu de 8192 documenté dans le design) force un KV cache 2× plus gros, potentiellement instable.

**Correction v3** :
1. `num_predict` porté à 2048 pour le deep-dive (suffisant pour ~600 tokens de contenu dense)
2. `num_ctx` uniformisé à 8192 pour TOUS les modèles (cohérent avec le design doc)
3. Si l'output se termine sans phrase complète, l'orchestrateur ajoute `[TRONQUÉ — reprise nécessaire]` et propose `--resume`

### §0.4 Échec #4 — Ph3 (35B MoE) : synthèse tronquée

**Symptôme** : `[TRONQUÉ: length]` — idem G3.

**Cause racine** : La synthèse reçoit TOUS les outputs précédents en EXTRA (~4000 tokens), plus le prompt système (~1500 tokens), plus l'article (~5500 tokens). Total entrée ≈ 11000 tokens, dont seuls 8192 sont utilisables (num_ctx). Le modèle tronque silencieusement le contexte OU dépasse sa limite de génération.

**Correction v3** :
1. EXTRA pour Ph3 = résumés des phases précédentes, pas les outputs complets (compression automatique par l'orchestrateur)
2. `num_ctx=8192` strict
3. `num_predict=1500` pour la synthèse

### §0.5 Échec #5 — Ph4 (35B MoE) : CANNOT_ASSESS final tronqué

**Symptôme** : `[TRONQUÉ: length]`.

**Cause racine** : Même problème que Ph3. De plus, le prompt synthesis2 est un CLONE de synthesis — les instructions sont identiques. Ph4 ne devrait pas refaire la synthèse ; elle devrait uniquement évaluer ce qui est CANNOT_ASSESS.

**Correction v3** : Ph4 reçoit un BLOCK dédié `cannot_assess_final` (pas un clone de synthesis) qui demande UNIQUEMENT d'évaluer les zones CANNOT_ASSESS identifiées par les phases précédentes.

### §0.6 Échec #6 — G4 (granite3.2:8b) : format de tableau corrompu

**Symptôme** : Les colonnes "Ligne" et "Citation" sont fusionnées/inversées. Le contenu de "Citation" contient l'analyse au lieu de la citation. Le modèle paraphrase l'article au lieu de le critiquer. 30 entrées sans substance.

**Cause racine** : Le persona "Contrebandier" (pragmatique) demande une analyse stratégique nuancée, mais le format de sortie impose un tableau rigide. Le modèle ne peut pas exprimer une analyse stratégique dans un tableau à 6 colonnes — il force le contenu dans le moule, produisant du non-sens. De plus, granite3.2 est entraîné sur des données enterprise, pas sur l'analyse stratégique de mouvements sociaux.

**Correction v3** : G4 change de format — sortie en prose structurée (pas de tableau), avec sections "Weaponization", "Second-order effects", "Contrat de confiance", "Emotional design", "Risques de récupération". Le persona Contrebandier est maintenu mais le format est adapté à sa tâche.

### §0.7 Échec #7 — SHARED blocks toxiques pour Ph0/Ph1

**Cause racine** : L'orchestrateur envoie TOUS les SHARED blocks à TOUTES les phases. Ph0 et Ph1 reçoivent donc SHARED:taxonomy (tableau des codes) et SHARED:rules (format de sortie attendu) — qui contiennent le template de tableau que Ph0 reproduit par erreur.

**Correction v3** : SHARED blocks sont tiered :
- `SHARED:taxonomy` → G1, G2, G3, G4, Ph3, Ph4, Ph5, Ph6 uniquement
- `SHARED:rules` → G1, G2, G3, G4 uniquement
- Ph0 et Ph1 reçoivent ZÉRO SHARED block

### §0.8 Échec #8 — 4 Regards → 2 Regards dans l'implémentation

**Cause racine** : Le design documente 4 Regards (Greffier, Logicien, Cartographe, Contrebandier) mais PHASE_CONFIG n'en utilise que 2 (Logicien → G2, Contrebandier → G4). G1 utilise le prompt Greffier mais est nommé "Domaine Verification" — confusion de rôle.

**Correction v3** : Restauration des 4 Regards :
- G1 = Greffier (factuel) — prompt `regard_greffier`
- G2 = Logicien (structurel) — prompt `regard_logicien`
- G3 = Cartographe (représentationnel) — prompt `regard_cartographe`
- G4 = Contrebandier (pragmatique) — prompt `regard_contrebandier` (format prose, pas tableau)

Le Deep Dive (ex-G3) devient une phase post-regards dédiée, exécutée par le 35B MoE sur les domaines critiques identifiés par le Cartographe.

### §0.9 Bugs mineurs dans l'orchestrateur v2

1. **`num_predict` en double** : `"num_predict": 4096` apparaît deux fois dans le dict `options` — la 2e occurrence écrase la 1ère, mais c'est un défaut de code.
2. **`'data' in dir()`** : La vérification `if 'data' in dir()` est invalide en Python — `dir()` retourne les noms du scope LOCAL, pas les variables. La variable `data` est définie dans la boucle `for line in resp.iter_lines()`, mais après la boucle elle peut ne pas exister si le stream était vide. Correction : `except (NameError, UnboundLocalError)` ou initialisation `data = {}` avant la boucle.
3. **`num_ctx=16384` vs design `8192`** : L'orchestrateur utilise 16384 alors que le design doc spécifie 8192. Le KV cache 2× plus gros peut causer des instabilités mémoire sur l'iGPU.

---

## §1 ARCHITECTURE v3 — 10 phases, 5 modèles

### §1.1 Tableau d'assignation

| # | Phase | Rôle | Modèle | Famille | num_predict | Format sortie |
|---|-------|------|--------|---------|-------------|---------------|
| 0 | Ph0 | Métatexte | `phi4-mini:latest` | Phi | 200 | Prose structurée (PAS de tableau) |
| 1 | Ph1 | Cold Read | `qwen3:8b` | Qwen | 150 | 5 réponses brutes |
| 2 | G1 | Greffier (factuel) | `granite3.2:8b` | IBM | 300 | Tableau 6 colonnes |
| 3 | G2 | Logicien (structurel) | `qwen3:8b` | Qwen | 300 | Tableau 6 colonnes |
| 4 | G3 | Cartographe (représentationnel) | `phi4-mini:latest` | Phi | 300 | Tableau 6 colonnes |
| 5 | G4 | Contrebandier (pragmatique) | `granite3.2:8b` | IBM | 500 | Prose structurée (5 sections) |
| 6 | Ph3 | Deep Dive (domaines critiques) | `Qwen3.6-35b-MoE` | Qwen MoE | 2000 | Tableau + verdict |
| 7 | Ph4 | Synthèse (convergence) | `Qwen3.6-35b-MoE` (KV warm) | Qwen MoE | 1500 | Format synthèse v5 |
| 8 | Ph5 | CANNOT_ASSESS Final | `Qwen3.6-35b-MoE` (KV hottest) | Qwen MoE | 800 | Verdict structuré |
| 9 | Ph6 | Critical Flaw Veto | `qwen3:8b` | Qwen | 300 | OUI/NON + justification |

**Pourquoi 10 phases au lieu de 8** :
- Les 4 Regards sont restaurés (G1-G4)
- Le Deep Dive (Ph3) est séparé des Regards
- La Synthèse (Ph4) et CANNOT_ASSESS Final (Ph5) ont des prompts distincts (plus de clone)
- Ph6 (Critical Flaw Veto) est un dernier regard indépendant avant verdict final

### §1.2 Séquencement KV cache

```
[phi4-mini] Ph0 ──► [qwen3:8b] Ph1 ──► [granite3.2] G1 ──► [qwen3:8b] G2
    │                                        │
    └──► [phi4-mini] G3                      └──► [granite3.2] G4
                                                  │
    ┌─────────────────────────────────────────────┘
    ▼
[35B MoE] Ph3 ──► [35B MoE KV warm] Ph4 ──► [35B MoE KV hottest] Ph5
                                                      │
    ┌─────────────────────────────────────────────────┘
    ▼
[qwen3:8b] Ph6
```

Les 3 phases 35B MoE sont groupées en séquence continue pour le KV cache reuse.

**Note sur phi4-mini** : Ph0 et G3 utilisent toutes les deux phi4-mini, mais 3 autres modèles sont chargés entre les deux (qwen3:8b, granite3.2, qwen3:8b). Le KV cache de phi4-mini est donc évincé — pas de reuse entre Ph0 et G3. Le seul KV cache reuse effectif est sur le bloc 35B MoE (Ph3→Ph4→Ph5).

### §1.3 Budget tokens par phase

| Phase | Entrée estimée | Sortie max | Total |
|-------|---------------|-----------|-------|
| Ph0 | 5700 (article + prompt isolé) | 200 | 5900 |
| Ph1 | 5700 | 150 | 5850 |
| G1-G3 | 6500 (article + SHARED + BLOCK) | 300 | 6800 |
| G4 | 6500 | 500 | 7000 |
| Ph3 | 7500 (article + SHARED + BLOCK + domaines Ph0) | 2000 | 9500 |
| Ph4 | 4000 (résumés compressés + BLOCK) | 1500 | 5500 |
| Ph5 | 3000 (résumés + BLOCK dédié) | 800 | 3800 |
| Ph6 | 4000 (résumés + BLOCK dédié) | 300 | 4300 |

`num_ctx=8192` suffit pour toutes les phases. Ph3 est la plus proche de la limite (9500 tokens demandés, 8192 utilisables — le reste est tronqué par Ollama sans erreur, le KV cache gère).

---

## §2 PROMPT v5 — Anti-fragile

### §2.1 Structure SHARED tiered

```
SHARED:taxonomy     → G1, G2, G3, G4, Ph3, Ph4, Ph5, Ph6
SHARED:rules        → G1, G2, G3, G4
SHARED:format_table → G1, G2, G3
SHARED:format_prose → G4
```

Ph0 et Ph1 ne reçoivent AUCUN SHARED block — leurs prompts sont auto-suffisants.

### §2.2 BLOCK:phase0_metatexte v5 (réécrit)

```
## BLOCK:phase0_metatexte Phase 0 — Métatexte

⚠️  TU ES PHASE 0. Ta seule tâche est d'extraire des métadonnées.
⚠️  INTERDICTION ABSOLUE : tu ne produis PAS de tableau.
⚠️  INTERDICTION ABSOLUE : tu n'utilises PAS les codes FACT/LACUNA/etc.
⚠️  INTERDICTION ABSOLUE : tu n'évalues PAS la qualité de l'article.
⚠️  Tu te contentes de DÉCRIRE ce que tu lis.

Réponds EXACTEMENT dans ce format (remplace les [...] par ton analyse) :

GENRE: [Enquête|Analyse|Essai|Manifeste|Récit|Reportage|Critique|Synthèse académique]
THÈSE: [une phrase assertive qui capture la thèse centrale]
TYPE_VÉRITÉ: [Empirique|Logique|Normative|Interprétative|Programmatique]
DOMAINE_1: [nom du domaine de connaissance principal]
DOMAINE_2: [nom du second domaine, ou "AUCUN"]
AUDIENCE: [Grand public|Experts|Communauté spécifique|Décideurs|Mixte]
LONGUEUR: [Court <1500 mots|Moyen 1500-4000|Long >4000]
SECTIONS:
- [Section 1] → [fonction: poser|prouver|nuancer|appliquer|conclure] (lignes ~X-Y)
- [Section 2] → [...]
```

### §2.3 BLOCK:phase1_coldread v5 (réécrit)

```
## BLOCK:phase1_coldread Phase 1 — Cold Read

⚠️  TU ES PHASE 1. Lecture instinctive UNIQUEMENT.
⚠️  INTERDICTION : pas de tableau. Pas de codes. Pas d'analyse structurée.

Lis l'article d'un trait. Puis réponds INSTINCTIVEMENT. Maximum 2 phrases par question.

Q1_RALENTI: [où as-tu ralenti ou décroché ?]
Q2_MANIPULATION: [où as-tu senti une manipulation rhétorique ?]
Q3_GÊNE: [la seule chose qui te gêne le plus, sans pouvoir la formuler]
Q4_FAIBLE: [le passage le plus faible intuitivement]
Q5_MONTRER: [à qui montrerais-tu cet article ?... ET à qui PAS ?]
```

### §2.4 BLOCK:regard_contrebandier v5 (format prose)

```
## BLOCK:regard_contrebandier Regard 4 — LE CONTREBANDIER (pragmatique)

*Que fera ce texte une fois libéré dans le monde ?*

⚠️  Format de sortie : prose structurée. PAS de tableau. Chaque section = 2-4 phrases.

### WEAPONIZATION
[Si un opposant voulait utiliser ce texte contre son propos, comment ferait-il ? Cite les passages vulnérables.]

### SECOND-ORDER EFFECTS
[Quels effets indirects ce texte peut-il produire, au-delà de l'intention de l'auteur ?]

### CONTRAT DE CONFIANCE
[Sur quelle base le lecteur doit-il faire confiance à l'auteur ? Ce contrat est-il solide ?]

### EMOTIONAL DESIGN
[Quelles émotions le texte cherche-t-il à produire ? Sont-elles alignées avec le propos ?]

### RISQUES DE RÉCUPÉRATION
[Qui d'autre que le public visé pourrait utiliser ce texte, et comment ?]
```

### §2.5 BLOCK:cannot_assess_final v5 (nouveau — remplace synthesis2)

```
## BLOCK:cannot_assess_final Phase 5 — CANNOT_ASSESS Final

Tu reçois les synthèses des phases précédentes. Ta tâche UNIQUE : évaluer les zones
que les modèles précédents ont marquées CANNOT_ASSESS.

Pour chaque zone CANNOT_ASSESS :
1. Avec les informations disponibles dans l'article et les analyses précédentes,
   peux-tu maintenant évaluer cet aspect ?
2. Si OUI → donne ton évaluation avec confiance (1-5)
3. Si NON → explique pourquoi c'est structurellement inévaluable

### Zones CANNOT_ASSESS à évaluer
[EXTRA: zones CANNOT_ASSESS extraites automatiquement par l'orchestrateur]

### Verdict final
[Pour chaque zone : ÉVALUABLE/CONFIRMÉ ou INÉVALUABLE]
```

### §2.6 BLOCK:critical_flaw_veto v5 (nouveau)

```
## BLOCK:critical_flaw_veto Phase 6 — Critical Flaw Veto

Tu es le dernier rempart. Tu reçois :
- Les 4 Regards (G1-G4)
- Le Deep Dive (Ph3)
- La Synthèse (Ph4)
- Le CANNOT_ASSESS Final (Ph5)

Ta tâche : UNE seule décision binaire.
"Y a-t-il une erreur factuelle, logique ou éthique qui invalide la publication ?"

### VETO: [OUI|NON]
### JUSTIFICATION: [si OUI : quelle erreur exacte. si NON : pourquoi l'article tient]
### CONFIANCE: [1-5]
```

---

## §3 ORCHESTRATEUR v3 — Garde-fous

### §3.1 Détection de boucle de répétition

```python
def detect_loop(output: str, threshold: int = 12) -> bool:
    """Détecte si le modèle a bouclé sur la même critique."""
    # Compte les lignes de tableau
    table_lines = [l for l in output.split('\n') if l.startswith('|') and '|' in l[2:]]
    if len(table_lines) > threshold:
        return True
    # Détecte les répétitions de citation identique
    citations = re.findall(r'«\s*(.+?)\s*»', output)
    if len(citations) > 5:
        from collections import Counter
        most_common = Counter(citations).most_common(1)[0]
        if most_common[1] > 5:  # même citation >5 fois
            return True
    return False
```

### §3.2 Compression EXTRA pour Ph4/Ph5

```python
def compress_phase_output(output: str, max_chars: int = 500) -> str:
    """Compresse un output de phase en résumé pour EXTRA."""
    # Extrait les lignes de tableau uniquement (pas la prose)
    table_lines = [l for l in output.split('\n') if l.startswith('|')]
    if table_lines:
        # Garde header + 5 premières entrées max
        header = table_lines[0] if table_lines else ''
        body = table_lines[1:6]  # max 5 entrées
        return '\n'.join([header] + body)
    # Pour la prose, garde les premières lignes
    return output[:max_chars] + ('...' if len(output) > max_chars else '')
```

### §3.3 num_predict par phase (plafonds stricts)

```python
PHASE_NUM_PREDICT = {
    "phase0_metatexte": 200,
    "phase1_single_model": 150,
    "g1_greffier": 300,
    "g2_logicien": 300,
    "g3_cartographe": 300,
    "g4_contrebandier": 500,
    "phase3_deepdive": 2000,
    "phase4_synthesis": 1500,
    "phase5_cannot_assess": 800,
    "phase6_veto": 300,
}
```

### §3.4 SHARED block routing (tiered)

```python
SHARED_ROUTING = {
    "shared_taxonomy":  ["g1_greffier","g2_logicien","g3_cartographe",
                          "g4_contrebandier","phase3_deepdive","phase4_synthesis",
                          "phase5_cannot_assess","phase6_veto"],
    "shared_rules":     ["g1_greffier","g2_logicien","g3_cartographe",
                          "g4_contrebandier"],
    "shared_format_table": ["g1_greffier","g2_logicien","g3_cartographe"],
    "shared_format_prose": ["g4_contrebandier"],
}

def build_messages_v3(blocks, block, article, extra, phase_id):
    shared_parts = []
    for sid, phases in SHARED_ROUTING.items():
        if phase_id in phases and sid in blocks:
            shared_parts.append(blocks[sid]["content"])
    # ... (reste identique)
```

### §3.5 Marqueur de complétion + vérification d'intégrité

Chaque phase réussie écrit `__AUDIT_COMPLETE__\n` comme dernière ligne du fichier.
L'orchestrateur vérifie ce marqueur avant de passer à la phase suivante.
Si absent → l'output est considéré comme incomplet/tronqué.

```python
COMPLETION_MARKER = "__AUDIT_COMPLETE__"

def save_phase_output(outdir, phase_id, output, is_complete=True):
    fpath = outdir / f"{phase_id}.txt"
    content = output
    if is_complete:
        content = output.rstrip() + f"\n{COMPLETION_MARKER}\n"
    fpath.write_text(content, encoding="utf-8")

def is_phase_complete(outdir, phase_id):
    fpath = outdir / f"{phase_id}.txt"
    if not fpath.exists():
        return False
    content = fpath.read_text(encoding="utf-8")
    return content.rstrip().endswith(COMPLETION_MARKER)
```

### §3.6 Mode think désactivé pour G2

```python
# G2 utilise qwen3:8b SANS mode think
# Le mode think amplifie la persévération sur les modèles Qwen3
# Payload pour G2 uniquement :
if phase_id == "g2_logicien":
    payload["options"]["enable_thinking"] = False
```

### §3.7 Detection de dégénérescence post-phase

```python
def validate_output(phase_id, output):
    """Retourne (is_valid, warning_message)."""
    warnings = []
    
    # G1/G2/G3: max 12 entrées de tableau
    if phase_id in ("g1_greffier","g2_logicien","g3_cartographe"):
        if detect_loop(output, threshold=12):
            warnings.append("DÉGÉNÉRESCENCE: boucle de répétition détectée")
    
    # Toute phase: output non-vide
    if len(output.strip()) < 20:
        warnings.append("VIDE: output < 20 caractères")
    
    # Ph0: ne doit PAS contenir de tableau markdown
    if phase_id == "phase0_metatexte" and "|---" in output:
        warnings.append("ERREUR: Ph0 a produit un tableau (confusion de rôle)")
    
    return (len(warnings) == 0, "; ".join(warnings))
```

---

## §4 CONFIGURATION OLLAMA UNIFORMISÉE

### §4.1 num_ctx unique

Tous les modèles utilisent `num_ctx=8192` (pas 16384). Cohérent avec le design doc §1.4.

### §4.2 Options par phase

```python
def build_options(phase_id, model, num_predict):
    opts = {
        "temperature": 0.2,
        "num_predict": num_predict,
        "num_ctx": 8192,
        "num_batch": 2048,
    }
    # Mode think désactivé pour les phases 8B (prévient la persévération)
    if phase_id in ("g2_logicien",):
        opts["enable_thinking"] = False
    return opts
```

---

## §5 FORMAT DE SORTIE

### §5.1 Fichiers de phase

```
_audit_<article>/
├── phase0_metatexte.txt         # Ph0 — Métatexte (phi4-mini)
├── phase1_single_model.txt      # Ph1 — Cold Read (qwen3:8b)
├── g1_greffier.txt           # G1 — Greffier (granite3.2:8b)
├── g2_logicien.txt           # G2 — Logicien (qwen3:8b)
├── g3_cartographe.txt        # G3 — Cartographe (phi4-mini)
├── g4_contrebandier.txt      # G4 — Contrebandier (granite3.2:8b)
├── phase3_deepdive.txt          # Ph3 — Deep Dive (35B MoE)
├── phase4_synthesis.txt         # Ph4 — Synthèse (35B MoE, KV warm)
├── phase5_cannot_assess.txt     # Ph5 — CANNOT_ASSESS Final (35B MoE, KV warm)
├── phase6_veto.txt              # Ph6 — Critical Flaw Veto (qwen3:8b)
├── meta.json                    # timing, modèle, token count, warnings
└── audit_<article>.md           # rapport final
```

### §5.2 Rapport final v3

Structure enrichie avec verdict exécutif en tête :

```markdown
# Audit Adversarial v3 — <article>
**Date** : ... | **10 phases, 5 modèles** | **Temps total** : ...

## VERDICT EXÉCUTIF
**Niveau** : Sommital / Très bon / Bon / Passable / À réécrire
**Veto** : OUI / NON
**Publiable** : OUI / AVEC RÉSERVES / NON
**Top 3 corrections urgentes** :
1. ...
2. ...
3. ...

---
[Phases détaillées...]
```

---

## §6 INTERFACE

```bash
# Usage
python3 audit.py [--dry-run] [--resume] [--benchmark] <article.md>

# --dry-run : estimation seule, pas d'appels LLM
# --resume  : reprendre un audit interrompu (vérifie __AUDIT_COMPLETE__)
# --benchmark : calibrer tok/s
```

---

## §7 PLAN D'IMPLANTATION

### Phase A — Prompt v5 (1h)
1. Réécrire `2026-06-14_audit_adversarial_prompt.md` → `_v5.md`
2. Ajouter SHARED:format_table, SHARED:format_prose
3. Réécrire BLOCK:phase0_metatexte (instructions-barrières)
4. Réécrire BLOCK:phase1_coldread (format balisé Q1_RALENTI...)
5. Réécrire BLOCK:regard_contrebandier (format prose)
6. Ajouter BLOCK:cannot_assess_final (nouveau)
7. Ajouter BLOCK:critical_flaw_veto (nouveau)

### Phase B — Orchestrateur v3 (3h)
1. SHARED_ROUTING (tiered)
2. PHASE_NUM_PREDICT par phase
3. `detect_loop()` + `validate_output()`
4. `compress_phase_output()` pour EXTRA Ph4/Ph5
5. `build_options()` avec enable_thinking=False pour G2
6. `__AUDIT_COMPLETE__` marker
7. `--resume` avec vérification d'intégrité
8. Suppression du clone synthesis2

### Phase C — Test (1h)
1. `--dry-run` sur l'article éloge_surface_levier (vérifier estimation)
2. Run complet sur l'article (vérifier qualité des 10 phases)
3. Vérifier que Ph0 ne produit PAS de tableau
4. Vérifier que G2 ne boucle pas
5. Vérifier que Ph3/Ph4/Ph5 ne sont pas tronqués
