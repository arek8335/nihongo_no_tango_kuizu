import json
from pathlib import Path

from enums import LEVELS, QUESTIONS


class Database:
    def __init__(self):
        self.path = Path("data")
        self.questions: dict[LEVELS, dict[QUESTIONS, list[dict]]] = {}

    def load_data(self) -> None:
        for level in LEVELS:
            self.questions[level] = {}
            for question_type in QUESTIONS:
                with open(
                    f"{self.path}/{level}/{question_type}.json", encoding="utf-8"
                ) as f:
                    self.questions[level][question_type] = json.load(f)

    def get(self, level: LEVELS, question_type: QUESTIONS) -> dict:
        return self.questions[level][question_type]
