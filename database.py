import json
from enums import Level, QuestionType
from pathlib import Path


class Database:
    def __init__(self, path: str = "data"):
        self.path = Path(path)
        self.questions: dict[Level, dict[QuestionType, list[dict]]] = {}

    def load_data(self) -> None:
        for level in Level:
            self.questions[level] = {}
            for question_type in QuestionType:
                file = self.path / level / f"{question_type}.json"
                with open(file, encoding="utf-8") as f:
                    self.questions[level][question_type] = json.load(f)

    def get(self, level: Level, question_type: QuestionType) -> list(dict):
        return self.questions[level][question_type]
