from enum import StrEnum


class Color(StrEnum):
    Reset = "\033[0m"
    Blue = "\033[34m"
    Green = "\033[32m"
    Red = "\033[31m"
    Yellow = "\033[33m"
