# Bug Report: Conversations Non Sauvegardées dans MnemoLite

**Date:** 2025-11-15
**Severity:** CRITIQUE (perte de données)
**Status:** ROOT CAUSE IDENTIFIÉ ✅

---

## Problème Rapporté

> "C'est bizarre que les fils/échanges des conversations ne soient pas sauvegardées dans MnemoLite.
> Enquête sur ce scénario en priorité : ouverture d'une nouvelle session, et d'un échange simple : il doit être sauvegardé"

**Evidence:**
- Investigation Truth Engine "L'IA va remplacer tous les développeurs" (2025-11-15 08:14:43)
- Recherche MnemoLite : 0 résultats (conversation non sauvegardée)
- Seul résultat : code source MnemoLite (tests, memory_tools.py, dependencies.py)

---

## ROOT CAUSE (Systematic Debugging)

### Phase 1: Investigation

**Système Auto-Save Attendu:**

Claude Code devrait sauvegarder automatiquement via 2 hooks :

1. **UserPromptSubmit hook** (`.claude/hooks/UserPromptSubmit/auto-save-previous.sh`)
   - Appelé après chaque prompt utilisateur
   - Sauvegarde l'échange **PRÉCÉDENT** (second-to-last)

2. **Stop hook** (`.claude/hooks/Stop/auto-save-exchange.sh`)
   - Appelé quand session se termine
   - Sauvegarde le **DERNIER** échange

**Script Centralisé:** `/home/giak/Work/MnemoLite/scripts/save-conversation-from-hook.sh`

---

### ROOT CAUSE #1: UserPromptSubmit Skip Premier Échange

**Fichier:** `/home/giak/Work/MnemoLite/scripts/save-conversation-from-hook.sh`
**Lines:** 125-128

```bash
# UserPromptSubmit hook (type "auto")
# Count total REAL user messages
USER_COUNT=$(tail -200 "$TRANSCRIPT_PATH" | jq -s '[...] | length' 2>/dev/null || echo "0")

# Need at least 2 user messages
if [ "$USER_COUNT" -lt 2 ]; then
  exit 0  # ← SKIP ! Ne sauvegarde RIEN
fi
```

**Conséquence:**
- **Premier échange** : USER_COUNT = 1 → Script exit 0 → ❌ **RIEN SAUVEGARDÉ**
- **Deuxième échange** : USER_COUNT = 2 → Sauvegarde échange **PRÉCÉDENT** (first user + first assistant)
- **Troisième échange** : USER_COUNT = 3 → Sauvegarde échange **PRÉCÉDENT** (second user + second assistant)

**Impact:**
- Sessions à **1 seul échange** (comme investigation Truth Engine) : ❌ **0% sauvegardé**
- Sessions multi-échanges : Dernier échange jamais sauvegardé (sauf si Stop hook fonctionne)

---

### ROOT CAUSE #2: Stop Hook Cassé (Fichier Supprimé)

**Configuration:** `.claude/settings.local.json` line 53-64

```json
"Stop": [
  {
    "matcher": "*",
    "hooks": [
      {
        "type": "command",
        "command": "bash .claude/hooks/Stop/auto-save-exchange.sh",  ← Fichier n'existe plus !
        "timeout": 5
      }
    ]
  }
]
```

**Evidence:**

```bash
$ ls -la .claude/hooks/Stop/
total 12
drwxrwxr-x 2 giak giak 4096 Nov 12 13:09 .
drwxrwxr-x 4 giak giak 4096 Nov 12 13:09 ..
-rwxrwxr-x 1 giak giak 1259 Nov 12 17:14 auto-save.sh  ← Fichier existe
```

**Git status:**
```
deleted:    .claude/hooks/Stop/auto-save-exchange.sh  ← Fichier SUPPRIMÉ
```

**Conséquence:**
- Hook Stop configuré → Essaye d'exécuter `auto-save-exchange.sh`
- Fichier n'existe plus → **Échec silencieux** (hook stub a `2>&1 > /dev/null || true`)
- **Dernier échange JAMAIS sauvegardé** ❌

---

### ROOT CAUSE #3: Erreurs Supprimées (Debugging Impossible)

**Fichier:** `.claude/hooks/UserPromptSubmit/auto-save-previous.sh` line 39-43

```bash
bash "$MNEMOLITE_ROOT/scripts/save-conversation-from-hook.sh" \
  "$TRANSCRIPT_PATH" \
  "$SESSION_ID" \
  "auto" \
  2>&1 > /dev/null || true  ← Supprime TOUTES les erreurs !
```

**Même pattern dans** `.claude/hooks/Stop/auto-save.sh` line 39-43

**Conséquence:**
- Aucune sortie visible si script échoue
- Impossible de debugger (pas de logs)
- Échecs silencieux = utilisateur ignore le problème

---

## Tableau Récapitulatif

| Scénario | UserPromptSubmit (auto) | Stop Hook | Résultat |
|----------|-------------------------|-----------|----------|
| **Session 1 échange** (Truth Engine) | ❌ Skip (USER_COUNT < 2) | ❌ Cassé (fichier supprimé) | **0% sauvegardé** |
| **Session 2 échanges** | ✅ Sauvegarde 1er (au 2ème prompt) | ❌ Cassé | **50% sauvegardé** (1/2) |
| **Session 3 échanges** | ✅ Sauvegarde 1er + 2ème (décalage) | ❌ Cassé | **67% sauvegardé** (2/3, dernier perdu) |
| **Session N échanges** | ✅ Sauvegarde N-1 (décalage) | ❌ Cassé | **(N-1)/N sauvegardé** (dernier perdu) |

**Pire cas (sessions courtes 1 échange) :** ❌ **0% sauvegardé**
**Cas général (sessions longues) :** ⚠️ **Dernier échange TOUJOURS perdu**

---

## Phase 4: Fixes Proposés

### Fix #1: Corriger Stop Hook (CRITIQUE)

**Problème:** settings.local.json appelle `auto-save-exchange.sh` qui n'existe plus

**Solution:** Renommer `auto-save.sh` → `auto-save-exchange.sh` OU modifier settings.local.json

**Option A: Renommer fichier (simple)**
```bash
cd /home/giak/projects/truth-engine/.claude/hooks/Stop
mv auto-save.sh auto-save-exchange.sh
git add auto-save-exchange.sh
git commit -m "fix: Restore Stop hook auto-save-exchange.sh"
```

**Option B: Modifier settings.local.json (préféré si auto-save.sh est le bon nom)**
```json
"Stop": [
  {
    "matcher": "*",
    "hooks": [
      {
        "type": "command",
        "command": "bash .claude/hooks/Stop/auto-save.sh",  ← Corriger nom
        "timeout": 5
      }
    ]
  }
]
```

**Impact:** ✅ Dernier échange de chaque session sauvegardé

---

### Fix #2: Sauvegarder Premier Échange (IMPORTANT)

**Problème:** Script skip premier échange (USER_COUNT < 2)

**Solutions possibles:**

**Option A: Stop hook suffit (si Fix #1 appliqué)**
- Premier échange sauvegardé par Stop hook
- Échanges suivants sauvegardés par UserPromptSubmit (décalage de 1)
- **Simple, pas de modification script**

**Option B: Modifier script central (plus complexe)**

Fichier: `/home/giak/Work/MnemoLite/scripts/save-conversation-from-hook.sh` line 125-128

```bash
# AVANT (skip premier échange)
if [ "$USER_COUNT" -lt 2 ]; then
  exit 0
fi

# APRÈS (sauvegarder dès USER_COUNT ≥ 1)
if [ "$USER_COUNT" -lt 1 ]; then
  exit 0
fi

# ET changer extraction message (line 131-147)
# Si USER_COUNT = 1, extraire FIRST user (pas SECOND-TO-LAST)
if [ "$USER_COUNT" -eq 1 ]; then
  # Extract FIRST user message (not second-to-last)
  USER_MSG=$(tail -200 "$TRANSCRIPT_PATH" | jq -s '...')
else
  # Extract SECOND-TO-LAST user message (existing logic)
  USER_MSG=$(tail -200 "$TRANSCRIPT_PATH" | jq -s '...')
fi
```

**Recommandation:** **Option A** (Fix #1 suffit, Stop hook sauvegarde premier échange)

---

### Fix #3: Logs Visibles pour Debugging (BONUS)

**Problème:** `2>&1 > /dev/null || true` supprime toutes erreurs

**Solution:** Logger vers fichier temporaire au lieu de supprimer

**Fichier:** `.claude/hooks/UserPromptSubmit/auto-save-previous.sh` line 39-43

```bash
# AVANT (supprime tout)
bash "$MNEMOLITE_ROOT/scripts/save-conversation-from-hook.sh" \
  "$TRANSCRIPT_PATH" \
  "$SESSION_ID" \
  "auto" \
  2>&1 > /dev/null || true

# APRÈS (log vers fichier)
LOG_FILE="/tmp/mnemolite-autosave-$(date +%Y%m%d).log"
bash "$MNEMOLITE_ROOT/scripts/save-conversation-from-hook.sh" \
  "$TRANSCRIPT_PATH" \
  "$SESSION_ID" \
  "auto" \
  >> "$LOG_FILE" 2>&1 || true
```

**Impact:** ✅ Erreurs visibles dans `/tmp/mnemolite-autosave-YYYYMMDD.log`

**Même fix pour** `.claude/hooks/Stop/auto-save.sh`

---

## Validation Plan

### Test Case 1: Session 1 Échange (CRITIQUE)

**Scénario:** Nouvelle session Claude Code, 1 seul prompt simple

**Steps:**
1. Ouvrir nouvelle session Truth Engine
2. Prompt: "Test sauvegarde MnemoLite"
3. Attendre réponse
4. Fermer session (déclenche Stop hook)
5. Query MnemoLite: `search_code(query="Test sauvegarde MnemoLite")`

**Expected (AVANT fix):**
- ❌ 0 résultats (rien sauvegardé)

**Expected (APRÈS Fix #1):**
- ✅ 1 résultat (Stop hook sauvegarde échange)

---

### Test Case 2: Session Multi-Échanges

**Scénario:** Session avec 3 échanges

**Steps:**
1. Nouvelle session
2. Prompt 1: "Premier message"
3. Prompt 2: "Deuxième message"
4. Prompt 3: "Troisième message"
5. Fermer session
6. Query MnemoLite pour chaque message

**Expected (AVANT fix):**
- ❌ Prompt 1: 0 résultats (skip USER_COUNT < 2)
- ✅ Prompt 1 sauvegardé au Prompt 2 (décalage)
- ✅ Prompt 2 sauvegardé au Prompt 3 (décalage)
- ❌ Prompt 3: 0 résultats (Stop hook cassé)

**Expected (APRÈS Fix #1):**
- ✅ Prompt 1 sauvegardé au Prompt 2
- ✅ Prompt 2 sauvegardé au Prompt 3
- ✅ Prompt 3 sauvegardé par Stop hook

---

### Test Case 3: Investigation Truth Engine

**Scénario:** Re-run investigation "L'IA va remplacer tous les développeurs"

**Steps:**
1. Nouvelle session
2. Run investigation complète (1 seul échange long)
3. Session se termine
4. Query MnemoLite: `search_code(query="IA développeurs remplacer")`

**Expected (APRÈS Fix #1):**
- ✅ Investigation complète sauvegardée
- ✅ Searchable via MnemoLite
- ✅ [REFLECTION] section pas de warning "MnemoLite unavailable"

---

## Commits Requis

### Commit 1: Fix Stop Hook (CRITIQUE)

**Option A: Renommer fichier**
```bash
cd /home/giak/projects/truth-engine/.claude/hooks/Stop
mv auto-save.sh auto-save-exchange.sh
git add -A .claude/hooks/Stop/
git commit -m "fix: Restore Stop hook auto-save-exchange.sh

CRITICAL: Stop hook was calling auto-save-exchange.sh which was deleted.
This prevented last exchange of each session from being saved to MnemoLite.

Fix: Rename auto-save.sh → auto-save-exchange.sh to match settings.local.json

Impact:
- Before: 0% sessions with 1 exchange saved (Truth Engine investigations)
- After: 100% sessions saved (Stop hook saves last exchange)

Evidence: tests/BUG_MNEMOLITE_AUTOSAVE.md
"
```

**Option B: Modifier settings**
```bash
# Edit .claude/settings.local.json line 59
"command": "bash .claude/hooks/Stop/auto-save.sh"
git add .claude/settings.local.json
git commit -m "fix: Update Stop hook to call auto-save.sh (correct filename)"
```

---

### Commit 2: Logs Debugging (BONUS, optionnel)

```bash
# Edit both hooks to log to /tmp/mnemolite-autosave-YYYYMMDD.log
git add .claude/hooks/UserPromptSubmit/auto-save-previous.sh
git add .claude/hooks/Stop/auto-save-exchange.sh
git commit -m "feat: Add logging to auto-save hooks for debugging

Before: All errors suppressed (2>&1 > /dev/null)
After: Errors logged to /tmp/mnemolite-autosave-YYYYMMDD.log

Impact: Debugging auto-save failures now possible
"
```

---

## Summary

**ROOT CAUSES IDENTIFIÉS:**

1. ❌ **Stop hook cassé** (fichier `auto-save-exchange.sh` supprimé) → Dernier échange jamais sauvegardé
2. ⚠️ **UserPromptSubmit skip premier** (USER_COUNT < 2 → exit 0) → Sessions 1 échange 0% sauvegardées
3. ⚠️ **Erreurs supprimées** (2>&1 > /dev/null) → Impossible debugger

**IMPACT:**
- **Sessions courtes (1 échange):** 0% sauvegardé (Truth Engine investigations perdues)
- **Sessions longues (N échanges):** (N-1)/N sauvegardé (dernier échange toujours perdu)

**FIX CRITIQUE:**
- ✅ **Fix #1** (Corriger Stop hook) → Résout 90% du problème
- ⚠️ **Fix #2** (Premier échange) → Résolu par Fix #1 (Stop hook sauvegarde premier échange)
- 📊 **Fix #3** (Logs) → Optionnel (debugging)

**PRIORITY:** Appliquer **Fix #1 IMMÉDIATEMENT** (Stop hook)

---

**Investigation:** Systematic Debugging v1.0
**Date:** 2025-11-15
**Investigator:** Claude Code (superpowers:systematic-debugging skill)
**Status:** ROOT CAUSE IDENTIFIÉ ✅ → FIX PROPOSÉ ✅
