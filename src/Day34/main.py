from Question import Question
from data import data
from Quiz_Brain import QuizBrain
from ui import QuizInterface
question_bank=[]
#
# print(questions_data[0])
# print(questions_data[0]["results"])

for question in data[0]["results"]:
    question_text = question["question"]
    question_ans = question["correct_answer"]
    next_question = Question(question_text, question_ans)
    question_bank.append(next_question)
    # # print(question_bank)
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
# while quiz.stil_has_question():
#     quiz.next_question()