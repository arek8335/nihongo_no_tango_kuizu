import json
from pathlib import Path

from enums import LEVELS, QUESTIONS


class Database:
    def __init__(self):
        self.path = Path("data")
        self.questions: dict[LEVELS, dict[QUESTIONS, list[dict]]] = {}
        self.kanji_key = "kanji"
        self.answers_key = "questions"
        self.correct_answer_key = "answer"

    def load_data(self) -> None:
        for level in LEVELS:
            self.questions[level] = {}
            for question_type in QUESTIONS:
                with open(
                    f"{self.path}/{level}/{question_type}.json", encoding="utf-8"
                ) as f:
                    self.questions[level][question_type] = json.load(f)
