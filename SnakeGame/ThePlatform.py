from turtle import Screen
from snake import Snake
from food import Food
from Scoreboard import scoreboard
import time
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)
turtles = []


s = Snake()
food = Food()
scoreb = scoreboard()



screen.listen()
screen.onkey(key = "Up", fun =s.up)
screen.onkey(key="Down", fun=s.down)
screen.onkey(key="Left", fun=s.left)
screen.onkey(key="Right", fun=s.right)



game_is_on = True
while game_is_on:
    s.move()
    #s.checkcol()
    #Detect collision with food
    if s.head.distance(food) < 15:
        print("nom nom nom")
        s.extend()
        scoreb.clear()
        scoreb.touch()
        scoreb.score()
        food.refresh()

    if abs(s.head.xcor()) > 280 or abs(s.head.ycor()) > 280:
        scoreb.reset()
        s.reset()

    #Detect collision with tail
    for snakes in s.turtles[1:]:
        if s.head.distance(snakes) < 15:
            scoreb.reset()
            s.reset()

    
    screen.update()
    time.sleep(.08)








screen.exitonclick()