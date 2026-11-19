from colors import Color
from enums import QUESTIONS, SCORING


class UI:
    def __init__(self):
        self.WELCOME_MSG = f"""
{Color.Blue}日本語の単語のクイズへようこそ！{Color.Reset}
各クイズは15問で構成されています。
テストを中断する場合は（{Color.Yellow}stop{Color.Reset}）、終了する場合は（{Color.Yellow}exit{Color.Reset}）と入力してください。
        """
        self.JAPANESE_LEVEL_MSG = (
            "どの日本語レベルを選びますか？（N1、N2、N3、N4、N5）："
        )
        self.WRONG_COMMAND = f"{Color.Red}コマンドを認識できません。{Color.Reset}"
        self.QUESTION_TYPE_MSG: dict[QUESTIONS, str] = {
            QUESTIONS.Reading: "の読み方は何ですか？",
            QUESTIONS.Antonym: "の対義語は何ですか？",
            QUESTIONS.Synonym: "の類義語は何ですか？",
        }
        self.SCORING_MSG: dict[SCORING, str] = {
            SCORING.Really_Bad: "もう少し勉強したほうがいいですね。",
            SCORING.Bad: "少しはわかっているけど、まだまだですね。",
            SCORING.Good: "なかなかいいですね！でも、完璧まであと一歩です",
            SCORING.Cool: "よく知っていますね！",
            SCORING.Super: "すごい！満点です！",
        }
        self.USER_ANSWER_MSG = "答えは何ですか？："
        self.SEPARATOR_MSG = "–" * 10
        self.WRONG_ANSWER_MSG = f"{Color.Red}不正解です。正解は{Color.Reset}"
        self.CORRECT_ANSWER_MSG = f"{Color.Green}正解です！{Color.Reset}"
        self.RETAKE_QUIZ_MSG = (
            f"{Color.Blue}新しいクイズを始めますか？（Y/N）：{Color.Reset}"
        )
        self.SCORRED_POINTS_MSG = "点を獲得しました！"
        self.BYE_MSG = "さようなら！"

    def print_msg_with_new_line(self, msg: str = "") -> None:
        print(msg)

    def print_msg_same_line(self, msg: str) -> None:
        print(msg, end="")

    def print_msg_with_space(self, msg: str) -> None:
        print(msg, end=" ")

    def print_wrong_command_msg(self) -> None:
        print(self.WRONG_COMMAND)

    def print_correct_question(
        self, kanji: str, question_type: QUESTIONS, question_num: int
    ) -> None:
        print(f"{question_num}.({kanji}){self.QUESTION_TYPE_MSG[question_type]}")

    def print_answers(self, answers: list) -> None:
        for i, answer in enumerate(answers):
            print(f"{i + 1}.{answer}", end=" ")
        print()

    def print_wrong_answer_msg(self, correct_answer: str) -> None:
        print(f"{self.WRONG_ANSWER_MSG}（{correct_answer}）")

    def print_scoring_summary_note(self, score: SCORING) -> None:
        print(Color.Yellow + self.SCORING_MSG[score] + Color.Reset)
