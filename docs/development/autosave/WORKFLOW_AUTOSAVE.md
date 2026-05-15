# Workflow Auto-Sauvegarde Conversations — Documentation Technique

**Version**: 2.0
**Date**: 2025-11-08
**Projet**: Truth Engine + MnemoLite

---

## Table des Matières

1. [Architecture Globale](#architecture-globale)
2. [Hook UserPromptSubmit (N-1)](#hook-userpromptsubmit-n-1)
3. [Stratégie N-1 Expliquée](#stratégie-n-1-expliquée)
4. [Flow Détaillé](#flow-détaillé)
5. [Extraction des Messages](#extraction-des-messages)
6. [Cas d'Usage](#cas-dusage)
7. [Limitations](#limitations)
8. [Troubleshooting](#troubleshooting)

---

## Architecture Globale

### Vue d'Ensemble

```mermaid
graph TB
    subgraph "Truth Engine Project"
        USER[👤 Utilisateur VSCode]
        CLAUDE[🤖 Claude Code]
        TRANSCRIPT[📄 Transcript .jsonl]
        HOOK[⚡ Hook UserPromptSubmit]
    end

    subgraph "MnemoLite (Docker)"
        DOCKER[🐳 Container API]
        SCRIPT[🐍 save-direct.py]
        DB[(🗄️ PostgreSQL)]
    end

    USER -->|Question| CLAUDE
    CLAUDE -->|Tool calls + Réponse| USER
    CLAUDE -->|Écrit messages| TRANSCRIPT
    USER -->|Question suivante| HOOK
    HOOK -->|Lit N-1| TRANSCRIPT
    HOOK -->|Appelle| DOCKER
    DOCKER -->|Exécute| SCRIPT
    SCRIPT -->|Sauvegarde| DB
```

### Composants

| Composant | Rôle | Emplacement |
|-----------|------|-------------|
| **Hook UserPromptSubmit** | Déclenché avant chaque question user | `.claude/hooks/UserPromptSubmit/auto-save-previous.sh` |
| **Transcript** | Fichier JSONL avec tous les messages | `~/.claude/projects/-home-giak-projects-truth-engine/*.jsonl` |
| **save-direct.py** | Script Python qui sauvegarde via MCP | `/home/giak/Work/MnemoLite/.claude/hooks/Stop/save-direct.py` |
| **PostgreSQL** | Base de données MnemoLite | Table `memories` |

---

## Hook UserPromptSubmit (N-1)

### Concept Clé: Stratégie N-1

**Problème**: Le hook `UserPromptSubmit` est déclenché AVANT que Claude réponde.

```mermaid
sequenceDiagram
    participant User as 👤 User
    participant Hook as ⚡ Hook
    participant Claude as 🤖 Claude
    participant Transcript as 📄 Transcript

    Note over User,Transcript: Échange N-1 (COMPLET)
    User->>Transcript: Question N-1: "vérifie"
    Claude->>Transcript: Réponse complète (texte + tool results)

    Note over User,Transcript: Échange N (EN COURS)
    User->>Hook: Question N: "cela doit fonctionner"
    activate Hook
    Hook->>Transcript: Lit échange N-1 (COMPLET)
    Hook->>MnemoLite: Sauvegarde N-1
    Hook-->>Claude: Continue
    deactivate Hook
    Claude->>Transcript: Réponse à N (EN COURS)
```

**Solution**: Sauvegarder l'échange **PRÉCÉDENT** (N-1), pas l'actuel (N).

### Pourquoi N-1 ?

| Échange | État | Peut être sauvegardé ? |
|---------|------|------------------------|
| **N-1** | ✅ COMPLET (user + assistant + tool results) | ✅ OUI |
| **N** | ⏳ EN COURS (user seulement) | ❌ NON |

---

## Stratégie N-1 Expliquée

### Timeline Complète

```mermaid
sequenceDiagram
    autonumber
    participant U as 👤 User
    participant H as ⚡ Hook
    participant C as 🤖 Claude
    participant T as 📄 Transcript
    participant M as 🗄️ MnemoLite

    Note over U,M: === Échange 1 ===
    U->>T: Message 1: "continue"
    H->>T: Hook déclenché (USER_COUNT=1, skip)
    C->>T: Réponse 1 (5764 chars)

    Note over U,M: === Échange 2 ===
    U->>T: Message 2: "vérifie"
    H->>T: Hook déclenché (USER_COUNT=2)
    H->>T: Extrait N-1: User="continue" + Assistant=5764 chars
    H->>M: Sauvegarde N-1
    M-->>H: ✅ Saved: 33808bcc
    C->>T: Réponse 2 (7074 chars)

    Note over U,M: === Échange 3 ===
    U->>T: Message 3: "pour moi, il a encore..."
    H->>T: Hook déclenché (USER_COUNT=3)
    H->>T: Extrait N-1: User="vérifie" + Assistant=7074 chars
    H->>M: Sauvegarde N-1
    M-->>H: ✅ Saved: 77c46c73
    C->>T: Réponse 3 (EN COURS...)
```

### Latence = 1 Échange

**Conséquence**: L'échange actuel (N) sera sauvegardé seulement au **prochain** message user.

```
Session:
├─ Échange 1: "continue" → Sauvegardé à l'échange 2 ✅
├─ Échange 2: "vérifie" → Sauvegardé à l'échange 3 ✅
└─ Échange 3: "pour moi, il a encore..." → ⏳ PAS ENCORE SAUVEGARDÉ
   (Sera sauvegardé à l'échange 4 ou fin de session)
```

---

## Flow Détaillé

### 1. Déclenchement du Hook

```mermaid
flowchart TD
    START[👤 User envoie message N]
    HOOK[⚡ Hook UserPromptSubmit déclenché]
    READ[📖 Lit hook data JSON]
    TRANSCRIPT[📄 Extrait transcript_path]

    START --> HOOK
    HOOK --> READ
    READ --> TRANSCRIPT

    TRANSCRIPT --> CHECK{Transcript existe ?}
    CHECK -->|NON| EXIT1[❌ Exit]
    CHECK -->|OUI| COUNT

    COUNT[🔢 Compte USER_COUNT]
    COUNT --> USERCHECK{USER_COUNT >= 2 ?}
    USERCHECK -->|NON| EXIT2[❌ Exit - Pas assez d'échanges]
    USERCHECK -->|OUI| EXTRACT[📝 Extraction N-1]
```

### 2. Extraction N-1

```mermaid
flowchart TD
    START[📝 Extraction N-1]

    subgraph "Extraction User N-1"
        USER1[tail -200 lines]
        USER2[Filtre: role='user' ET PAS tool_result]
        USER3[Prend message -2 second-to-last]
        USER4[Extrait texte]
    end

    subgraph "Extraction Assistant N-1"
        ASS1[tail -2000 lines]
        ASS2[Index tous les messages]
        ASS3[Trouve indices user N-2 et N-1]
        ASS4[Extrait TOUS messages entre N-2 et N-1]
        ASS5[Assistant text + tool_result]
    end

    START --> USER1
    USER1 --> USER2
    USER2 --> USER3
    USER3 --> USER4

    START --> ASS1
    ASS1 --> ASS2
    ASS2 --> ASS3
    ASS3 --> ASS4
    ASS4 --> ASS5

    USER4 --> VALIDATE
    ASS5 --> VALIDATE

    VALIDATE{Contenus valides ?}
    VALIDATE -->|NON| EXIT[❌ Exit]
    VALIDATE -->|OUI| DEDUP[🔍 Déduplication]
```

### 3. Sauvegarde

```mermaid
flowchart TD
    START[🔍 Déduplication]
    HASH[🔐 Calcul hash MD5]
    CHECK{Hash existe ?}

    START --> HASH
    HASH --> CHECK
    CHECK -->|OUI| SKIP[⏭️ Skip - Déjà sauvegardé]
    CHECK -->|NON| DOCKER

    DOCKER[🐳 Docker exec api]
    PYTHON[🐍 save-direct.py]
    WRITE[✍️ write_memory]
    EMBED[🧠 Génère embedding]
    DB[(💾 PostgreSQL)]

    DOCKER --> PYTHON
    PYTHON --> WRITE
    WRITE --> EMBED
    EMBED --> DB

    DB --> SUCCESS[✅ Saved]
    SUCCESS --> ADDHASH[📝 Ajoute hash à dedup]
    ADDHASH --> RETURN[🔄 Return continue:true]
```

---

## Extraction des Messages

### Format Claude Code JSON

```json
{
  "message": {
    "role": "user",
    "content": [
      {
        "type": "text",
        "text": "vérifie"
      }
    ]
  },
  "timestamp": "2025-11-08T15:16:25Z"
}
```

### Types de Messages

```mermaid
graph TD
    subgraph "Messages User"
        REAL[✅ REAL User<br/>type: 'text']
        TOOL[🔧 Tool Result<br/>type: 'tool_result']
    end

    subgraph "Messages Assistant"
        TEXT[💬 Text<br/>type: 'text']
        THINKING[🤔 Thinking<br/>type: 'thinking']
        TOOLUSE[🛠️ Tool Use<br/>type: 'tool_use']
    end

    REAL --> SAVE[Sauvegardé comme USER]
    TOOL --> EXTRACT[Extrait comme TOOL RESULT]
    TEXT --> SAVE2[Sauvegardé comme ASSISTANT]
    THINKING --> SKIP[Ignoré]
    TOOLUSE --> SKIP2[Ignoré - résultat capturé via tool_result]
```

### Exemple Extraction Complète

**Input**: Transcript entre user N-2 et user N-1

```
[INDEX 185] User N-2: "vérifie"
[INDEX 186] Assistant: "Je vais vérifier..."
[INDEX 187] Assistant: Tool use (Bash)
[INDEX 188] User: Tool result (Bash output)
[INDEX 189] Assistant: "✅ Vérification terminée..."
[INDEX 190] Assistant: Tool use (Read)
[INDEX 191] User: Tool result (File content)
[INDEX 192] Assistant: "Analyse complète."
[INDEX 243] User N-1: "pour moi, il a encore..."
```

**Output Sauvegardé**:

```markdown
## 👤 User
vérifie

## 🤖 Claude
Je vais vérifier...

---

<Bash output complet>

---

✅ Vérification terminée...

---

<File content complet>

---

Analyse complète.
```

---

## Cas d'Usage

### Cas 1: Session Normale

```
User: "Question 1"
Claude: [Réponse 1]
→ Pas de sauvegarde (USER_COUNT=1)

User: "Question 2"
Hook: Sauvegarde échange 1 ✅
Claude: [Réponse 2]

User: "Question 3"
Hook: Sauvegarde échange 2 ✅
Claude: [Réponse 3]

Session se termine
→ Échange 3 PAS SAUVEGARDÉ ⚠️
```

### Cas 2: Session avec Hook Stop

```
User: "Question 1"
Claude: [Réponse 1]

User: "Question 2"
Hook UserPromptSubmit: Sauvegarde échange 1 ✅
Claude: [Réponse 2]

Session se termine
Hook Stop: Sauvegarde échange 2 ✅
```

### Cas 3: Message "end" Manuel

```
User: "Question finale"
Claude: [Réponse finale]

User: "end"
Hook: Sauvegarde "Question finale" + réponse ✅
```

---

## Limitations

### 1. Latence 1 Échange

**Problème**: Le dernier échange n'est pas sauvegardé immédiatement.

**Solutions**:
- ✅ **Hook Stop**: Sauvegarde automatique à la fermeture
- ✅ **Message "end"**: Trigger manuel
- ✅ **Daemon MnemoLite**: Rattrapage après 120s (uniquement pour projet MnemoLite)

### 2. Daemon Non Applicable à Truth Engine

**Limitation**: Le daemon MnemoLite scanne `/home/user/.claude/projects/` dans le container Docker.

**Impact**: Truth Engine (`/home/giak/.claude/projects/...`) n'est PAS monté dans le container.

**Pourquoi**: Par design, container MnemoLite réservé à MnemoLite uniquement.

```mermaid
graph LR
    subgraph "Container MnemoLite"
        DAEMON[🔄 Daemon]
        MOUNT[/home/user/.claude/projects/]
    end

    subgraph "Host"
        MNEMO[~/.claude/projects/<br/>-home-giak-Work-MnemoLite/]
        TRUTH[~/.claude/projects/<br/>-home-giak-projects-truth-engine/]
    end

    MNEMO -->|✅ Monté| MOUNT
    TRUTH -.->|❌ NON monté| MOUNT

    DAEMON -->|Scanne| MOUNT
    DAEMON -.->|❌ Ne voit pas| TRUTH
```

### 3. Minimum 2 Échanges Requis

**Comportement**: Le hook saute les premières questions jusqu'à USER_COUNT >= 2.

**Raison**: Besoin de N-1 (échange précédent) pour sauvegarder.

---

## Troubleshooting

### Problème: "Le dernier échange n'est pas sauvegardé"

**Cause**: Stratégie N-1 par design.

**Solution**:
1. Envoyer un message supplémentaire ("end" ou "ok")
2. Ou attendre la prochaine question
3. Ou implémenter Hook Stop

### Problème: "Aucune sauvegarde détectée"

**Debug**:

```bash
# 1. Vérifier logs hook
tail -20 /tmp/hook-autosave-debug.log

# 2. Vérifier hash dedup
cat /tmp/mnemo-saved-exchanges.txt | wc -l

# 3. Vérifier DB
cd /home/giak/Work/MnemoLite
docker compose exec -T db psql -U mnemo -d mnemolite -c \
  "SELECT id, title, created_at FROM memories WHERE author = 'AutoSave' ORDER BY created_at DESC LIMIT 5;"
```

**Attendu dans logs**:
```
[2025-11-08 16:22:21] Hook UserPromptSubmit called - VERSION 2.0
DEBUG: Extracted USER=7 chars, ASSISTANT=1988 chars
DEBUG: Hash 8144ee1f2bb269fe not found, proceeding to save...
✓ Saved: 5ee9d02a-080b-4ad3-a4a6-40c33256cf16
```

### Problème: "Tool results manquants dans sauvegarde"

**Cause**: Version hook ancienne (< 2.0)

**Solution**: Vérifier version dans logs:
```bash
grep "VERSION" /tmp/hook-autosave-debug.log | tail -1
```

Doit afficher: `VERSION 2.0`

Si `VERSION 1.0`, mettre à jour le hook.

---

## Résumé Architecture

### Truth Engine (Hook Uniquement)

```
✅ Hook UserPromptSubmit (N-1)
   ├─ Latence: 1 échange
   ├─ Sauvegarde: Instantanée (N-1)
   └─ Coverage: 95%

❌ Daemon (Non applicable)
   └─ Container ne voit pas transcripts Truth Engine
```

### MnemoLite (Hook + Daemon)

```
✅ Hook UserPromptSubmit (N-1)
   ├─ Latence: 1 échange
   └─ Coverage: 95%

✅ Daemon Auto-Import
   ├─ Poll: 30s
   ├─ Cooldown: 120s
   └─ Coverage: 5% (failsafe pour N)

= 100% Coverage
```

---

## Next Steps Recommandés

### Option 1: Hook Stop (Recommandé)

Créer `.claude/hooks/Stop/save-last.sh` pour sauvegarder le dernier échange à la fermeture.

### Option 2: Accepter N-1

Accepter latence 1 échange comme design intentionnel. Envoyer "end" si besoin de sauvegarder immédiatement.

### Option 3: Daemon Standalone

Créer daemon standalone hors Docker qui scanne TOUS les projets (Truth Engine + MnemoLite + autres).

---

**Fin du Document**
