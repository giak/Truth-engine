from tools.engines.extractors.parse_atomic import parse_f001, parse_f_civ, parse_items

def test_parse_f001_basic():
    text = "F001 dette annulée par Urukagina. F002 autre fait."
    result = parse_f001(text)
    assert len(result) == 2
    assert result[0]["id_old"] == "F001"
    assert "dette" in result[0]["contexte_brut"]
    assert result[0]["line_no"] > 0

def test_parse_f_civ_basic():
    text = "F-S001 annulation. F-MA005 serment."
    result = parse_f_civ(text)
    assert len(result) == 2
    assert result[0]["id_old"] == "F-S001"
    assert result[1]["id_old"] == "F-MA005"

def test_parse_items_basic():
    text = "1. **Premier item**\n2. **Second item**\n3. **Troisième**"
    result = parse_items(text)
    assert len(result) == 3
    assert result[0]["num"] == 1
    assert result[0]["item_brut"] == "Premier item"
    assert result[2]["num"] == 3
