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

const FINDINGS_PATH = '.verify/findings.json'

function extractField(res, field) {
  const s = (typeof res === 'string' ? res : JSON.stringify(res ?? {})).replace(/\\/g, '')
  const m = s.match(new RegExp('"' + field + '"\\s*:\\s*"([A-Z]+)"'))
  return m ? m[1] : null
}

function extractFindings(res) {
  // Le reviewer rend un structured_output { verdict, findings: [...] }.
  // Le toolResult du spawn peut être une chaîne JSON (nested) ou un objet.
  let s = typeof res === 'string' ? res : JSON.stringify(res ?? {})
  try {
    const parsed = JSON.parse(s)
    if (Array.isArray(parsed) && parsed.length > 0 && typeof parsed[0] === 'object') {
      for (const item of parsed) {
        if (Array.isArray(item?.findings)) return item.findings
      }
      return parsed.find((x) => x && typeof x === 'object' && 'findings' in x)?.findings ?? []
    }
    if (Array.isArray(parsed?.findings)) return parsed.findings
    // Chaîne JSON imbriquée dans le toolResult (ex: content[0].value)
    const m = s.match(/"findings"\s*:\s*(\[[\s\S]*?\])\s*(?:,"|,\s*"|})/)
    if (m) {
      try {
        return JSON.parse(m[1])
      } catch {
        /* fallthrough */
      }
    }
  } catch {
    /* chaîne non-JSON : regex de secours ci-dessous */
  }
  const m = s.match(/"findings"\s*:\s*(\[[\s\S]*?\])\s*(?:,"|,\s*"|})/)
  return m ? (() => { try { return JSON.parse(m[1]) } catch { return [] } })() : []
}

export default {
  id: 'truth-verifier',
  displayName: 'Truth Verifier',
  model: 'anthropic/claude-haiku-4.5',

  spawnerPrompt:
    'Spawn this agent to verify a worktree before delivery: deterministic checks, independent clean-room review, and state certification. The verdict (PASS/FAIL/BLOCKED) is written to .verify/result.json.',

  includeMessageHistory: false,

  toolNames: ['run_terminal_command', 'spawn_agents', 'read_files', 'write_file', 'end_turn'],

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
    let findings = []
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
      findings = extractFindings(rev && rev.toolResult)
      if (findings.length > 0) {
        logger.info({ n: findings.length }, 'verify: reviewer findings captured')
      }
    } else {
      logger.info({ detVerdict }, 'verify: deterministic not PASS, skipping review')
    }

    // 3. Certificat : re-compute STATE_ID, détecte toute modification post-review,
    //    persiste les findings du reviewer, enregistre le verdict final dans .verify/result.json.
    logger.info({ reviewVerdict, nFindings: findings.length }, 'verify: certify')
    let findingsArg = ''
    if (findings.length > 0) {
      findingsArg = ` --findings-file ${FINDINGS_PATH}`
      yield {
        toolName: 'write_file',
        input: { path: FINDINGS_PATH, content: JSON.stringify(findings, null, 2) },
      }
    }
    yield {
      toolName: 'run_terminal_command',
      input: {
        command: `python3 tools/verify/verify.py certify --review ${reviewVerdict}${findingsArg}`,
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
