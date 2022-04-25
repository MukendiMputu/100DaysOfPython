from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    question_bank.append(QuestionModel(q["question"], q["correct_answer"]))

trivia = QuizBrain(question_bank)

while trivia.still_has_question():
    trivia.next_question()

print("You made it!")
print(f"Your final score is: {trivia.score}/{len(question_bank)}")
