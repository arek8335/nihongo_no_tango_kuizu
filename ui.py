from colors import Color


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
        self.QUESTION_READING_MSG = "の読み方は何ですか？"
        self.QUESTION_SYNONYM_MSG = "の類義語は何ですか？"
        self.QUESTION_ANTONYM_MSG = "の対義語は何ですか？"
        self.SEPARATOR_MSG = "–" * 10
        self.WRONG_ANSWER_MSG = f"{Color.Red}不正解です。正解は{Color.Reset}"
        self.CORRECT_ANSWER_MSG = f"{Color.Green}正解です！{Color.Reset}"
        self.RETAKE_QUIZ_MSG = (
            f"{Color.Yellow}新しいクイズを始めますか？：{Color.Reset}"
        )
        self.BYE_MSG = "さようなら！"

    def print_msg_with_new_line(msg: str):
        print(msg)

    def print_msg_same_line(msg: str):
        print(msg, end="")

    def print_msg_with_space(msg: str):
        print(msg, end=" ")
