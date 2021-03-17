from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for number in range(question_data.shape[0]):
    new_question = Question(question_data.question[number], question_data.answer[number])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
    print("\n")

