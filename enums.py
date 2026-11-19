from enum import StrEnum, IntEnum


class LEVELS(StrEnum):
    N5 = "N5"
    N4 = "N4"
    N3 = "N3"
    N2 = "N2"
    N1 = "N1"


class QUESTIONS(StrEnum):
    Reading = "reading"
    Antonym = "antonym"
    Synonym = "synonym"


class SCORING(IntEnum):
    Super = 15
    Cool = 12
    Good = 7
    Bad = 4
    Really_Bad = 0
