class Quiz_brain:
    def __init__(self, question_list):
        self.question_number = 0
        self.qlist = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number  < len(self.qlist):
            return True
        else:
            return False

    def next_question(self):
        cq = self.qlist[self.question_number]
        self.question_number += 1
        answer = input(f"Q. {self.question_number}: {cq.q} (True/False): ")
        self.check_answer(answer, cq.a)

    def check_answer(self, answer, qa):
        if answer == qa:
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
        print(f"The correct answer was: {qa}")
        print(f"You got {self.score}/{self.question_number} right")


