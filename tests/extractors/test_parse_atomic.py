from tools.engines.sublimator.extractors.parse_atomic import parse_f001, parse_f_civ, parse_items, parse_all

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

def test_parse_all_combines_3_formats():
    text = """
    F001 annulation dette.
    F-S001 autre fait.
    1. **Item un**
    F002 deuxième fait.
    2. **Item deux**
    """
    result = parse_all(text, civ_prefix="S")
    formats = {r["input_format"] for r in result}
    assert "F001" in formats
    assert "F-CIV-XXX" in formats
    assert "item" in formats

def test_parse_all_maps_f001_to_civ():
    text = "F001 fait ancien. F002 deuxième."
    result = parse_all(text, civ_prefix="MA")
    f001_targets = [r["id_target"] for r in result if r["input_format"] == "F001"]
    assert "F-MA001" in f001_targets
    assert "F-MA002" in f001_targets
