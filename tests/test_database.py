import pytest
from database import Database
from enums import LEVELS, QUESTIONS


def test_is_loading_db():
    db = Database()
    db.load_data()
    assert set(db.questions) == set(LEVELS), "足りないレベルがあります"
    for level in LEVELS:
        assert set(db.questions[level]) == set(QUESTIONS), f"{level}に足りないファイルがあります"


@pytest.mark.xfail(reason="バグ#4: Path('data')はカレントディレクトリに依存しています")
def test_load_data_from_other_directory_work(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    Database().load_data()
