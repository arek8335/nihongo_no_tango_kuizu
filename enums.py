from enum import StrEnum


class Level(StrEnum):
    N5 = "N5"
    N4 = "N4"
    N3 = "N3"
    N2 = "N2"
    N1 = "N1"


class QuestionType(StrEnum):
    READING = "reading"
    ANTONYM = "antonym"
    SYNONYM = "synonym"
