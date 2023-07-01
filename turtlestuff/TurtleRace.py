from turtle import Turtle, Screen
import random
screen = Screen()
"""red = Turtle()
blue = Turtle()
green = Turtle()
orange = Turtle()
purple = Turtle()
pink = Turtle()"""
turtles = []
colors = ["red", "blue", "green", "orange", "purple", "pink"]
for c in colors:
    a = Turtle()
    a.color(c)
    a.shape("turtle")
    turtles.append(a)

#print(turtles)
starty = 100
incy = 200/6
startx = -200
screen.setup(width = 500, height = 400)

for t in turtles:
    t.penup()
    t.setpos(x = startx, y = starty)
    t.x = startx
    starty -= incy




user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color:")

if user_bet:
    winner = False
while winner == False:
    for t in turtles:
        t.forward(random.randint(1,10))
        if t.xcor() > 200:
            wincol = t.pencolor()
            winner = True
            if t == user_bet:
                print(f"You win, {wincol} is the winner")
            else:
                print(f"You lose, {wincol} was the winner")
            screen.bye()
            break