from turtle import Screen, Turtle
from ball import Pong
import time
from pong import Paddle
from scoreboard import Scoreboard
scoreb = Scoreboard()

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
game_is_on = True


pong = Pong()
l = Paddle(-350, 0)
r = Paddle(350, 0)


def end_game():
    global game_is_on
    game_is_on = False
    screen.exit()

screen.listen()
screen.onkey(key="Up", fun=r.go_up)
screen.onkey(key="Down", fun=r.go_down)
screen.onkey(key="w", fun=l.go_up)
screen.onkey(key="s", fun=l.go_down)
screen.onkey(key="e", fun=end_game)




while game_is_on == True:
    time.sleep(.1)
    pong.move()
    screen.update()
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_y()
    if (pong.xcor() > 320 and pong.distance(r) < 50) or (pong.xcor() < -320 and pong.distance(l) < 50):
        pong.bounce_x()
        pong.speedinc()
    if pong.xcor() > 380:
        scoreb.l_score += 1
        pong.speedreset()
        pong.reset_position()
    if pong.xcor() < -380:
        scoreb.r_score += 1
        pong.speedreset()
        pong.reset_position()
    scoreb.updateboard()
