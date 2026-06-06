import re


def parse_f001(text: str) -> list[dict]:
    """Parse F001-F099 format ancien depuis texte enquête."""
    results = []
    for m in re.finditer(r"\bF0(\d{2})\b", text):
        line_no = text[: m.start()].count("\n") + 1
        start_ctx = max(0, m.start() - 50)
        end_ctx = min(len(text), m.end() + 50)
        contexte = text[start_ctx:end_ctx].strip()
        results.append(
            {
                "id_old": f"F0{m.group(1)}",
                "contexte_brut": contexte,
                "line_no": line_no,
            }
        )
    return results


def parse_f_civ(text: str) -> list[dict]:
    """Parse F-CIV-XXX format nouveau."""
    results = []
    for m in re.finditer(r"F-([A-Z]+)(\d+)", text):
        line_no = text[: m.start()].count("\n") + 1
        start_ctx = max(0, m.start() - 50)
        end_ctx = min(len(text), m.end() + 50)
        contexte = text[start_ctx:end_ctx].strip()
        results.append(
            {
                "id_old": m.group(0),
                "contexte_brut": contexte,
                "line_no": line_no,
            }
        )
    return results


def parse_items(text: str) -> list[dict]:
    """Parse items numérotés 'N. **item**' (tolère indent)."""
    results = []
    pattern = re.compile(r"^\s*(\d+)\.\s+\*\*([^*]+)\*\*", re.MULTILINE)
    for m in pattern.finditer(text):
        line_no = text[: m.start()].count("\n") + 1
        results.append(
            {
                "num": int(m.group(1)),
                "item_brut": m.group(2).strip(),
                "line_no": line_no,
            }
        )
    return results


def parse_all(text: str, civ_prefix: str, civ_f001_offset: int = 0) -> list[dict]:
    """Parse tous les formats et unifie avec mapping F001→F-CIV-XXX.

    Args:
        text: contenu enquête
        civ_prefix: préfixe civilisation (S, R, C, MA, I, IN, AM, A)
        civ_f001_offset: décalage pour F001 (ex: M-A 0, Islam 0, Inde 0)
    """
    results = []

    f001_results = parse_f001(text)
    for r in f001_results:
        old_num = int(r["id_old"][1:])
        new_num = old_num
        results.append(
            {
                "id_old": r["id_old"],
                "id_target": f"F-{civ_prefix}{new_num:03d}",
                "contexte_brut": r["contexte_brut"],
                "line_no": r["line_no"],
                "input_format": "F001",
            }
        )

    f_civ_results = parse_f_civ(text)
    for r in f_civ_results:
        results.append(
            {
                "id_old": r["id_old"],
                "id_target": r["id_old"],
                "contexte_brut": r["contexte_brut"],
                "line_no": r["line_no"],
                "input_format": "F-CIV-XXX",
            }
        )

    items_results = parse_items(text)
    base_num = max(
        (
            int(r["id_target"].split(civ_prefix)[1])
            for r in results
            if civ_prefix in r.get("id_target", "")
        ),
        default=0,
    ) + 1
    for r in items_results:
        results.append(
            {
                "id_old": f"item_{r['num']}",
                "id_target": f"F-{civ_prefix}{base_num:03d}",
                "contexte_brut": r["item_brut"],
                "line_no": r["line_no"],
                "input_format": "item",
            }
        )
        base_num += 1

    return results
