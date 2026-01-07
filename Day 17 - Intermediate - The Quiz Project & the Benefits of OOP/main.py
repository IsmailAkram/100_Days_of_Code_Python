from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# populating question_bank with data from question_data
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer) # creating a new_question object using the Question class (blueprint), with text and answer from data as arguments.
    question_bank.append(new_question)

# print(question_bank)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the question")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
# print(quiz.still_has_questions())