import json
import random
from enum import Enum

WELCOME_MSG = """
日本語の単語クイズへようこそ！
問題は「対義語」「類義語」「読み方」の3種類です。
全部で15問あります。がんばってください！

"""
QUESTIONS = {
    "reading": "の言葉はどう読みますか。",
    "antonym": "の言葉と反対の意味の言葉はどれですか。",
    "synonym": "の言葉と意味が一番近いものはどれですか。",
}


class QuestionType(Enum):
    reading = "reading.json"
    antonym = "antonym.json"
    synonym = "synonym.json"


def load_data_in_var(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        var = json.load(f)
    return var


def get_kanji_and_answers(q_type: str) -> dict:
    if q_type == "reading":
        return reading
    elif q_type == "antonym":
        return antonym
    return synonym


def print_question():
    type = question_types[actual_question_type]
    kanji_and_answers = get_kanji_and_answers(type)
    kanji = random.choice(list(kanji_and_answers))
    print(f"{QUESTION_NUMBER}. [{kanji}]{QUESTIONS[type]}")
    for i, o in enumerate(kanji_and_answers[kanji], 1):
        print(f"{i}. {o}", end="  ")


reading = load_data_in_var(Q_TYPE.reading.value)


question_types = ("reading", "antonym", "synonym")


def main() -> None:
    Q_TYPE = QuestionType
    reading = json.load(Q_TYPE.reading.value)
    antonym = json.load(Q_TYPE.antonym.value)
    synonym = json.load(Q_TYPE.synonym.value)


question_number = 1

print_question()
