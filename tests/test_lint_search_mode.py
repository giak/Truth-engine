"""Tests de lint_search_mode.py (P7 : garde-fou search_mode=hybrid des call sites)."""

import os

from tools.lint_search_mode import check_file, count_sites, find_md, main


def test_check_file_conforme(tmp_path):
    f = tmp_path / "ok.md"
    f.write_text('search_memory(q, search_mode="hybrid", tags=[...])\n')
    assert check_file(str(f)) == []


def test_check_file_non_conforme(tmp_path):
    f = tmp_path / "bad.md"
    f.write_text('search_memory(query="x", limit=10)\n')
    assert check_file(str(f)) == [(1, 'search_memory(query="x", limit=10)')]


def test_count_sites(tmp_path):
    f = tmp_path / "c.md"
    f.write_text("search_memory(a)\nsearch_memory(b)\npas de call\n")
    assert count_sites(str(f)) == 2


def test_find_md_dedup(tmp_path):
    (tmp_path / "a.md").write_text("x")
    (tmp_path / "b.txt").write_text("x")
    files = find_md([str(tmp_path), str(tmp_path / "a.md")])
    assert [os.path.basename(x) for x in files] == ["a.md"]


def test_main_conforme_0(tmp_path, capsys):
    (tmp_path / "ok.md").write_text('search_memory(q, search_mode="hybrid")\n')
    assert main([str(tmp_path)]) == 0


def test_main_non_conforme_1(tmp_path, capsys):
    (tmp_path / "bad.md").write_text("search_memory(q)\n")
    assert main([str(tmp_path)]) == 1


def test_main_aucun_2(tmp_path, capsys):
    (tmp_path / "v.md").write_text("rien\n")
    assert main([str(tmp_path)]) == 2
