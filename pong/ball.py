#ball
from turtle import Turtle
ytop = 290 
ybot = -290
ys = 10


class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.ys = 10
        self.xs = 10

    def bounce_y(self):
        self.ys *= -1

    def bounce_x(self):
        self.xs *= -1

    def move(self):
        x = self.xcor() + self.xs
        y = self.ycor() + self.ys
        self.goto(x,y)
    
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()

    def speedinc(self):
        self.xs *= 1.1
        self.ys *= 1.1
    
    def speedreset(self):
        self.ys = 10
        self.xs = 10

