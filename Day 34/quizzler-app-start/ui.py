from tkinter import *
import time
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, 'italic')

class QuizInterface:
    #The colon says what data type it is
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window =Tk()
        self.window.title( "Quizzler")
        self.window.config(padx= 20, pady= 20, bg= THEME_COLOR,)
        #Score
        self.score = Label(text= f"Score: {self.quiz.score}", bg = THEME_COLOR, fg = 'white')
        self.score.grid(column=1, row=0, pady= 20)
        #Canvas
        self.canvas = Canvas(height= 250, width= 300)
        self.canvas.grid(column=0,row=1, columnspan= 2, pady=20)
        self.question_text = self.canvas.create_text(150,125,
                                                     text = "text",
                                                     fill= THEME_COLOR,
                                                     font= FONT,
                                                     width= 280)
        #Buttons
        check = PhotoImage(file = "Day 34/quizzler-app-start/images/true.png")
        self.right = Button(image= check, command = self.clicked_true)
        self.right.grid(column=0, row=2, pady= 20)

        x = PhotoImage(file = "Day 34/quizzler-app-start/images/false.png")
        self.wrong = Button(image= x, command= self.clicked_false)
        self.wrong.grid(column=1, row=2, pady= 20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg = 'white')
        if self.quiz.still_has_questions():
            self.score.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "This is the end of the quiz")
            self.clicked_true.config(state = 'disabled')
            self.clicked_false.config(state = 'disabled')

    def clicked_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def clicked_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg = 'green')
        else:
            self.canvas.config(bg = 'red')
        self.window.after(1000, self.get_next_question)
            
