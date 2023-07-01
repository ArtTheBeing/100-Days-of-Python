from turtle import Turtle
paddlespeed = 20

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.left(90)
        self.shape("square")
        self.shapesize(1, 5)
        self.color("white")
        self.penup()
        self.goto(x,y)


    def go_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), (self.ycor() + 20))
    def go_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), (self.ycor() - 20))


