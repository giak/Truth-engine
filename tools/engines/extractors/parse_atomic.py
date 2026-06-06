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
    """Parse items numérotés 'N. **item**'."""
    results = []
    pattern = re.compile(r"^(\d+)\.\s+\*\*([^*]+)\*\*", re.MULTILINE)
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
