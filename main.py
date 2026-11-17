import random

from database import Database
from enums import Level, QuestionType

db = Database("data")
db.load_data()
q = random.choice(db.get(Level.N5, QuestionType.READING))
print(q["kanji"])
for i, option in enumerate(q["questions"], start=1):
    print(f"{i}. {option}")

choice = int(input("Twoja odpowiedź: "))
if q["questions"][choice - 1] == q["answer"]:
    print("Dobrze!")
else:
    print(f"Źle, poprawna odpowiedź: {q['answer']}")
