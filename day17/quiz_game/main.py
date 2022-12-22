from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from os import system

question_bank = []
for item in question_data:
    new_question = Question(q_text=item["question"], q_answer=item["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()


system("cls")
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
