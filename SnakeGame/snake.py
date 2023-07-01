#SnakeClass
from turtle import Turtle
poslist = [(0,0),(-20,0),(-40,0)]
movefor = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.turtles = []
        self.create()
        self.head = self.turtles[0]

    def reset(self):
        for t in self.turtles:
            t.goto(1000,1000)
        self.turtles.clear()
        self.create()
        self.head = self.turtles[0]


    def create(self):
        for pos in poslist:
            self.add_seg(pos)
            
    def add_seg(self, pos):
        t = Turtle("square")
        t.speed(0)
        t.color("white")
        t.penup()
        t.goto(pos)
        self.turtles.append(t)

    def extend(self):
        self.add_seg(self.turtles[-1].pos())

    def move(self):
        for seg in range(len(self.turtles) -1, 0,-1):
            new_x = self.turtles[seg-1].xcor()
            new_y = self.turtles[seg-1].ycor()
            self.turtles[seg].goto(new_x, new_y)
        self.head.forward(movefor)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)