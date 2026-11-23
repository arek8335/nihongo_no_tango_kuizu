from database import Database
from enums import LEVELS, QUESTIONS


def test_is_loading_db():
    db = Database()
    db.load_data()
    assert set(db.questions) == set(LEVELS), "足りないレベルがあります"
    for level in LEVELS:
        assert set(db.questions[level]) == set(QUESTIONS), f"{level}に足りないファイルがあります"


def test_running_db_from_other_dir(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    Database().load_data()
