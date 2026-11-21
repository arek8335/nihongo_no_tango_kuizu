import json
import pytest
from pathlib import Path
from enums import LEVELS, QUESTIONS

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
ALL_FILES = sorted(DATA_DIR.glob("*/*.json"))


def load(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_is_all_files_exists():
    missing = [
        f"{level}/{question}.json"
        for level in LEVELS
        for question in QUESTIONS
        if not (DATA_DIR / level / f"{question}.json").exists()
    ]
    assert missing == []


@pytest.mark.parametrize("path", ALL_FILES, ids=lambda p: f"{p.parent.name}/{p.name}.json")
def test_is_file_data_valid(path: Path):
    entries = load(path)
    assert isinstance(entries, list) and entries, "データが空であるか、リストではありません"
    for entry in entries:
        word = entry.get("kanji", "<empty>")
        qsts = entry["questions"]
        assert word not in qsts, "問題の単語が選択肢に含まれています"
        assert word != entry["answer"], "問題と正解が同じになっています"
        assert len(qsts) == 4, "選択肢の数が4つではありません"
        assert len(set(qsts)) == 4, "選択肢に重複があります"
        assert entry["answer"] in qsts, "正解が選択肢に含まれていません"


@pytest.mark.parametrize("path", ALL_FILES, ids=lambda p: f"{p.parent.name}/{p.name}.json")
def test_is_has_doubles(path: Path):
    entries = [e["kanji"] for e in load(path)]
    dupes = {w for w in entries if entries.count(w) > 1}
    assert not dupes, f"重複している問題があります: {dupes}"
