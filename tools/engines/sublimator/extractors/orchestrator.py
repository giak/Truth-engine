"""Orchestrateur cellule v33.2 — Architecture RÉELLE.

Python pur (mécanique) + LLM hôte (qui dialogue avec l'utilisateur via
opencode) + humain (validation finale).

AUCUNE clé API requise. Le LLM hôte = l'agent conversationnel qui
exécute ce code (moi, en l'occurrence).

Pipeline :
1. Agent A (parse_atomic) : regex 3 formats → F### candidats
2. Agent A++ (extract_utile) : patterns article-utile → dates, sommes, citations, URLs, acteurs, sections
3. Agent C (curator) : fusion + Jaccard + scoring URLs
4. GATE_G : audit complétude (SIMPLE 70 / MEDIUM 80 / COMPLEX 85 / APEX 90)
5. PROMPT STRUCTURÉ : généré pour le LLM hôte qui produit 11 sections de quintessence
6. Agent E (humain) : valide la fiche finale
"""
import yaml
from pathlib import Path
from .parse_atomic import parse_all
from .extract_utile import extract_utile_all
from .curator import curator_fusion
from .gate_g import compute_completude, gate_g_pass


def run_cellule(
    input_path: str,
    civ_prefix: str,
    output_path: str,
    complexity: str = "MEDIUM",
) -> dict:
    """Orchestre le pipeline mécanique d'extraction.

    Returns dict avec :
      - exit_code: 0 (succès) / 1 (GATE_G fail)
      - matrice: F### candidats
      - utile: extractions article-utile
      - score: complétude %
      - gate_pass: bool
      - prompt_hote: prompt structuré à passer au LLM hôte pour les 11 sections
    """
    text = Path(input_path).read_text()

    # Agent A : parse_all (3 formats)
    candidats_a = parse_all(text, civ_prefix=civ_prefix)

    # Agent A++ : extraction article-utile (8 catégories)
    utile = extract_utile_all(text)

    # Agent C : curator (Jaccard + scoring URLs)
    matrice = curator_fusion(candidats_a, [], civ_prefix=civ_prefix)

    # GATE_G
    score = compute_completude(text, matrice)
    gate_pass = gate_g_pass(score, complexity)

    # Génération du prompt structuré pour le LLM hôte (Agent B + D)
    prompt_hote = _build_prompt_hote(
        text=text,
        candidats_a=candidats_a,
        utile=utile,
        matrice=matrice,
        civ_prefix=civ_prefix,
        complexity=complexity,
        score=score,
        gate_pass=gate_pass,
    )

    fiche = {
        "civ_prefix": civ_prefix,
        "complexity": complexity,
        "n_f_candidats": len(candidats_a),
        "n_matrice_fusionnee": len(matrice),
        "completude_pct": score,
        "gate_g_pass": gate_pass,
        "f_atomiques": matrice,
        "utile": {
            "n_dates": len(utile["dates"]),
            "n_sommes": len(utile["sommes"]),
            "n_citations": len(utile["citations"]),
            "n_urls": len(utile["urls"]),
            "n_acteurs_nommes": len(utile["acteurs_nommes"]),
            "n_marqueurs_causalite": len(utile["marqueurs_causalite"]),
            "n_marqueurs_rhetorique": len(utile["marqueurs_rhetorique"]),
            "n_sections_plan": len(utile["sections_plan"]),
            "sections_plan": utile["sections_plan"],
            "dates": utile["dates"][:20],
            "sommes": utile["sommes"][:30],
            "citations": utile["citations"][:10],
            "urls": utile["urls"][:30],
            "acteurs_nommes": utile["acteurs_nommes"][:50],
        },
        "prompt_hote": prompt_hote,
    }

    Path(output_path).write_text(
        yaml.dump(fiche, allow_unicode=True, sort_keys=False)
    )

    return {
        "exit_code": 0 if gate_pass else 1,
        "output": output_path,
        "matrice": matrice,
        "utile": utile,
        "score": score,
        "gate_pass": gate_pass,
        "prompt_hote": prompt_hote,
    }


def _build_prompt_hote(
    text: str,
    candidats_a: list,
    utile: dict,
    matrice: list,
    civ_prefix: str,
    complexity: str,
    score: float,
    gate_pass: bool,
) -> str:
    """Génère le prompt structuré que le LLM hôte doit compléter.

    Le LLM hôte (moi, en tant qu'agent conversationnel opencode) lit ce
    prompt, lit l'enquête, et produit les 11 sections de quintessence.
    """
    return f"""# PROMPT STRUCTURÉ POUR LLM HÔTE (Agent B + D)

Tu es le LLM hôte de Truth Engine. Tu reçois une enquête Sumer/Rome/Chine/etc.
et tu dois produire une fiche de quintessence de 12 sections.

## Contexte mécanique (déjà extrait par Python pur)

- Civ_prefix : {civ_prefix}
- Complexité : {complexity}
- Score GATE_G actuel : {score}% ({"PASS" if gate_pass else "FAIL"})
- F### candidats (Agent A) : {len(candidats_a)}
- F### matrice fusionnée (Agent C) : {len(matrice)}
- Dates extraites : {len(utile["dates"])}
- Sommes extraites : {len(utile["sommes"])}
- Citations extraites : {len(utile["citations"])}
- URLs extraites : {len(utile["urls"])}
- Acteurs nommés (heuristique) : {len(utile["acteurs_nommes"])}
- Sections du plan SUBLIMATOR : {len(utile["sections_plan"])}/{18}

## Sections du plan SUBLIMATOR détectées

{chr(10).join(f"  - §{s['section_num']} {s['section_titre']} (L{s['line_no']})" for s in utile["sections_plan"])}

## Quelques sommes extraites (échantillon)

{chr(10).join(f"  - {s['montant']} ({s['format']}) L{s['line_no']}: {s['contexte_brut'][:80]}" for s in utile["sommes"][:10])}

## Quelques URLs extraites

{chr(10).join(f"  - {u['url']} (L{u['line_no']})" for u in utile["urls"][:10])}

## F### candidats

{chr(10).join(f"  - {c['id_target']} (L{c['line_no']}): {c['contexte_brut'][:80]}" for c in candidats_a[:20])}

## 12 sections à produire

1. **these_centrale** : 1 phrase résumant la thèse centrale
2. **theses_implicites** : 3 thèses implicites (non explicites mais sous-jacentes)
3. **f_atomiques** : compléter la matrice F### (les candidats ci-dessus + ajouts)
4. **acteurs_network** : 5-15 acteurs principaux (à filtrer depuis la liste)
5. **causalites** : 3-5 chaînes de causalité (≥3 liens chacune)
6. **perspectives_dialectiques** : 3 perspectives (auteur, adverse, arbitre)
7. **limites** : 3-5 limites méthodologiques
8. **wolves** : 3-5 acteurs malveillants identifiés
9. **iceberg** : 3-5 angles morts / auto-critiques
10. **chronologie** : 5-10 dates clés (depuis les dates extraites + ajouts)
11. **domaines** : 5-7 thématiques couvertes
12. **urls_prioritaires** : 5-10 sources clés (depuis les URLs extraites + ajouts)

## Méthode

1. Lis l'enquête complète ({len(text):,} chars, en sections §1 à §18).
2. Pour chaque section, croise les extractions mécaniques avec ta lecture cursive.
3. Pour F###, enrichis chaque candidat avec date/acteur/chiffre/source/notes.
4. Pour les acteurs, distingue les VRAIS acteurs (personnes/institutions) des expressions incidentes.
5. Pour les URLs, classe par tier (1=primaire, 2=secondaire, 3=inconnu).

## Output attendu

YAML valide, UTF-8, structuré selon les 12 sections. Pas de Markdown.
"""
