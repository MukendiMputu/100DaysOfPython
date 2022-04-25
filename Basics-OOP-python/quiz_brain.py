class QuizBrain:
    def __init__(self, q_list, q_number=0):
        self.question_number = q_number
        self.question_list = q_list
        self.score = 0

    # TODO: asking the question
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    # TODO: checking the correctness
    def check_answer(self, u_answer, correct_answer):
        if u_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print(f"Sorry, wrong answer!")
        print(f"The correct one is {correct_answer}")
        print(f"Current score: {self.score}/{self.question_number}")

    # TODO: checking if it's the end of the quiz
    def still_has_question(self):
        return self.question_number < len(self.question_list)

