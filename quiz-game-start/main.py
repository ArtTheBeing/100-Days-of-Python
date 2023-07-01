from data import question_data as data
from question_model import Question as Question
from quiz_brain import *
qbank = []
for line in data:
    q = Question(line["text"], line["answer"])
    qbank.append(q)

quiz = Quiz_brain(qbank)   
total = 0
while quiz.still_has_questions() == True:
    quiz.next_question()
    print()
print(f"You finished with: {quiz.score}/{quiz.question_number} Good Job!")