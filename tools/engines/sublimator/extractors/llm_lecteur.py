import json
import os

PROMPT_TEMPLATE = """Tu es un agent d'extraction atomique. Lis cette enquête et extrais 11 sections de quintessence.

Sections à extraire :
1. these_centrale (1 phrase)
2. theses_implicites (3 bullets)
3. acteurs (5-15 noms propres, pas catégories)
4. causalites (3-5 chaînes ≥3 liens)
5. perspectives_dialectiques (3 perspectives : auteur, adverse, arbitre, forces égales)
6. limites (3-5 limites méthodologiques)
7. wolves (3-5 acteurs malveillants nommés)
8. iceberg (3-5 angles morts/auto-critiques)
9. chronologie (5-10 dates clés)
10. domaines (5-7 thématiques)
11. urls_prioritaires (5-10 sources)

Enquête :
{text}

Réponds UNIQUEMENT en JSON valide avec ces 11 clés."""


def call_llm(prompt: str) -> str:
    """Appel LLM réel (Claude, GPT, ou autre). À implémenter."""
    api_key = os.environ.get("LLM_API_KEY")
    if not api_key:
        raise NotImplementedError(
            "LLM_API_KEY non défini. Définir LLM_API_KEY ou mocker call_llm()."
        )
    raise NotImplementedError("Appel API réel à implémenter (cf. Task 10)")


def lecteur_cursif(text: str, civ_prefix: str) -> dict:
    """Agent B : lit l'enquête intégralement et extrait 11 sections."""
    prompt = PROMPT_TEMPLATE.format(text=text[:50000])
    response = call_llm(prompt)
    return json.loads(response)
