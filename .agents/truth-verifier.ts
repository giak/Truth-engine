/**
 * truth-verifier — Gate de livraison déterministe.
 *
 * handleSteps impose l'ordre des opérations, au lieu de compter sur un rappel
 * de prompt :
 *   1. check   : contrôles déterministes + STATE_ID  (écrit .verify/pending.json)
 *   2. review  : truth-reviewer en contexte neuf (seulement si déterministe == PASS)
 *   3. certify : comparaison STATE_ID + enregistrement du verdict final
 *
 * L'artefact d'autorité est `.verify/result.json` (PASS / FAIL / BLOCKED).
 * Le parent (auteur / orchestrateur) lit ce fichier ; il ne dépend d'aucune
 * forme fragile de set_output.
 *
 * Fail-safe : si le verdict du reviewer est illisible dans le résultat du
 * spawn, la valeur par défaut est BLOCKED, jamais PASS. Aucune incertitude
 * n'est convertie en assurance.
 *
 * @type {import('../config/agents/types/agent-definition').AgentDefinition}
 */

function extractField(res, field) {
  const s = (typeof res === 'string' ? res : JSON.stringify(res ?? {})).replace(/\\/g, '')
  const m = s.match(new RegExp('"' + field + '"\\s*:\\s*"([A-Z]+)"'))
  return m ? m[1] : null
}

export default {
  id: 'truth-verifier',
  displayName: 'Truth Verifier',
  model: 'anthropic/claude-haiku-4.5',

  spawnerPrompt:
    'Spawn this agent to verify a worktree before delivery: deterministic checks, independent clean-room review, and state certification. The verdict (PASS/FAIL/BLOCKED) is written to .verify/result.json.',

  includeMessageHistory: false,

  toolNames: ['run_terminal_command', 'spawn_agents', 'read_files', 'end_turn'],

  spawnableAgents: ['truth-reviewer'],

  inputSchema: {
    prompt: {
      type: 'string',
      description: 'Mission et périmètre du chantier à vérifier, transmis au reviewer',
    },
  },

  handleSteps: function* ({ prompt, logger }) {
    // 1. Contrôles déterministes + STATE_ID (avant review).
    logger.info('verify: deterministic checks + state-id')
    const pre = yield {
      toolName: 'run_terminal_command',
      input: {
        command: 'python3 tools/verify/verify.py check',
        timeout_seconds: 600,
      },
    }
    const detVerdict = extractField(pre && pre.toolResult, 'deterministic') ?? 'BLOCKED'

    let reviewVerdict = 'BLOCKED'
    if (detVerdict === 'PASS') {
      // 2. Revue clean-room, uniquement si le déterministe passe (pas de review inutile).
      logger.info('verify: spawning truth-reviewer (clean-room)')
      const rev = yield {
        toolName: 'spawn_agents',
        input: {
          agents: [
            {
              agent_type: 'truth-reviewer',
              prompt:
                (prompt || 'Review the current working-tree changes against the project contract.') +
                '\n\nRead-only. Render PASS, FAIL or BLOCKED as structured output.',
            },
          ],
        },
      }
      reviewVerdict = extractField(rev && rev.toolResult, 'verdict') ?? 'BLOCKED'
    } else {
      logger.info({ detVerdict }, 'verify: deterministic not PASS, skipping review')
    }

    // 3. Certificat : re-compute STATE_ID, détecte toute modification post-review,
    //    enregistre le verdict final dans .verify/result.json.
    logger.info({ reviewVerdict }, 'verify: certify')
    yield {
      toolName: 'run_terminal_command',
      input: {
        command: `python3 tools/verify/verify.py certify --review ${reviewVerdict}`,
        timeout_seconds: 120,
      },
    }

    // 4. Lire le certificat final et le rendre visible dans le message de fin.
    yield {
      toolName: 'read_files',
      input: { paths: ['.verify/result.json'] },
    }
    yield 'STEP'
  },
}
