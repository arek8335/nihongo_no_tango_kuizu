from enums import QUESTIONS, LEVELS, SCORING
from database import Database
from ui import UI
import sys
import random


class System:
    def __init__(self):
        self.exit = "exit"
        self.stop = "stop"
        self.actual_level = LEVELS
        self.actual_question_type = QUESTIONS
        self.actual_mondai = {}
        self.seen_questions: set = []
        self.number_of_questions = 15
        self.questions_done = 0
        self.points = 0
        self.db = Database()
        self.ui = UI()

    def run(self) -> bool:
        self.db.load_data()
        self.ui.print_msg_with_new_line(self.ui.WELCOME_MSG)
        while True:
            self.user_chosing_level()
            self.handle_questions()
            if self.number_of_questions == self.questions_done:
                self.summarize_the_answers()
            if not self.user_want_to_continue():
                self.exit_program()
            self.reset_questions()

    def user_want_to_exit(self, user_input: str) -> None:
        if user_input == self.exit:
            self.exit_program()

    def exit_program(self) -> None:
        self.ui.print_msg_with_new_line(self.ui.BYE_MSG)
        sys.exit()

    def user_chosing_level(self) -> None:
        while True:
            user_input = input(self.ui.JAPANESE_LEVEL_MSG).strip().lower()
            self.user_want_to_exit(user_input)
            if user_input.upper() in LEVELS:
                self.actual_level = user_input.upper()
                return
            self.ui.print_wrong_command_msg()

    def handle_questions(self):
        for question_num in range(self.number_of_questions):
            self.actual_question_type = self.get_random_question_type()
            self.set_random_mondai()
            self.ui.print_correct_question(
                self.actual_mondai[self.db.kanji_key],
                self.actual_question_type,
                question_num + 1,
            )
            self.ui.print_answers(self.actual_mondai[self.db.answers_key])
            self.ui.print_msg_with_new_line()
            user_input = self.get_user_answer()
            if self.check_if_user_want_to_stop_kuizu(user_input):
                self.questions_done = question_num + 1
                break
            self.check_user_answer(user_input)
            self.ui.print_msg_with_new_line(self.ui.SEPARATOR_MSG)

        self.questions_done = self.number_of_questions

    def get_random_question_type(self) -> QUESTIONS:
        return random.choice(list(QUESTIONS))

    def set_random_mondai(self) -> None:
        while True:
            new_mondai = random.choice(
                list(self.db.questions[self.actual_level][self.actual_question_type])
            )
            if new_mondai[self.db.kanji_key] not in self.seen_questions:
                self.seen_questions.append(new_mondai)
                break

        self.actual_mondai = new_mondai

    def check_if_user_want_to_stop_kuizu(self, user_input: str) -> bool:
        self.user_want_to_exit(user_input)
        return user_input == self.stop

    def reset_questions(self) -> None:
        self.actual_level = LEVELS
        self.actual_question_type = QUESTIONS
        self.actual_mondai.clear()
        self.seen_questions.clear()
        self.points = 0

    def get_user_answer(self) -> str:
        while True:
            user_input = input(self.ui.USER_ANSWER_MSG).strip().lower()
            if user_input == self.stop:
                return self.stop
            elif user_input == self.exit:
                self.exit_program()
            int_user_input = 0
            if user_input.isdigit():
                int_user_input = int(user_input)
            if int_user_input > 0 and int_user_input <= 4:
                return self.actual_mondai[self.db.answers_key][int_user_input - 1]
            self.ui.print_wrong_command_msg()

    def check_user_answer(self, user_answer: int) -> None:
        correct_answer = self.actual_mondai[self.db.correct_answer_key]
        if correct_answer == user_answer:
            self.points += 1
            self.ui.print_msg_with_new_line(self.ui.CORRECT_ANSWER_MSG)
        else:
            self.ui.print_wrong_answer_msg(correct_answer)

    def summarize_the_answers(self) -> None:
        self.ui.print_msg_with_new_line(f"{self.points}{self.ui.SCORRED_POINTS_MSG}")
        self.ui.print_scoring_summary_note(self.get_scoring_from_points())
        self.ui.print_msg_with_new_line()

    def get_scoring_from_points(self) -> SCORING:
        if self.points == SCORING.Super:
            return SCORING.Super
        elif self.points >= SCORING.Cool:
            return SCORING.Cool
        elif self.points >= SCORING.Good:
            return SCORING.Good
        elif self.points >= SCORING.Bad:
            return SCORING.Bad
        return SCORING.Really_Bad

    def user_want_to_continue(self) -> bool:
        while True:
            user_input = input(self.ui.RETAKE_QUIZ_MSG).strip().upper()
            if user_input == "Y":
                return True
            elif user_input == "N":
                return False
            self.ui.print_wrong_command_msg()
