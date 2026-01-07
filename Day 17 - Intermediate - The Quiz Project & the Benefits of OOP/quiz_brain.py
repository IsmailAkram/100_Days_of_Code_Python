# TODO: asking the question
# TODO: checking if the answer was correct
# TODO: checking if we're at the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        # print(self.question_number)
        # print(len(self.question_list))
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number] # indexing the number of a question in the list and assigning it as the current question.
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"Correct!")
        else:
            print(f"Incorrect!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number} \n")