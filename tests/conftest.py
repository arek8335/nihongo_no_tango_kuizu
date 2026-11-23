import pytest
from system import System


@pytest.fixture
def system():
    s = System()
    return s


@pytest.fixture
def type_in(monkeypatch):
    def _type_in(*inputs: str) -> None:
        remaining = iter(inputs)

        def fake_input(prompt: str = ""):
            try:
                return next(remaining)
            except StopIteration:
                raise f"{prompt!r}" \
                    from None

        monkeypatch.setattr("builtins.input", fake_input)

    return _type_in


@pytest.fixture
def sample_mondai() -> dict:
    return {
        "kanji": "安堵",
        "questions": ["うんど", "あんどう", "あんと", "あんど"],
        "answer": "あんど",
    }
