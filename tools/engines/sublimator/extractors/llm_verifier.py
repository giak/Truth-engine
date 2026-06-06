import json
import os

PROMPT_VERIFIER = """Tu es un agent verifier. Reprends cette matrice F### et signale les trous par rapport au texte source.

Matrice :
{matrice}

Texte source (extrait) :
{text}

Signale :
- f001_manquants : F### qui devraient être listés
- incoherences : claims mal sourcés
- acteurs_oublies : acteurs cités dans texte mais absents matrice
- fausses_urls : URLs qui semblent inventées
- iceberg_sous_exploite : angles morts non capturés

Réponds en JSON."""


def call_llm(prompt: str) -> str:
    """Appel LLM réel. Stub partagé avec llm_lecteur."""
    api_key = os.environ.get("LLM_API_KEY")
    if not api_key:
        raise NotImplementedError("LLM_API_KEY non défini.")
    raise NotImplementedError("Appel API réel à implémenter (cf. Task 10)")


def verifier(matrice: list, text: str) -> dict:
    """Agent D : relit et signale les trous."""
    matrice_str = "\n".join(f"{m['id']}: {m.get('fait', '')}" for m in matrice)
    prompt = PROMPT_VERIFIER.format(matrice=matrice_str, text=text[:30000])
    response = call_llm(prompt)
    return json.loads(response)
