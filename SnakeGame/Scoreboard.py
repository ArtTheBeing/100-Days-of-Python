from turtle import Turtle


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.numscore = 0
        with open("SnakeGame/score") as data:
            self.z = int(data.read())
        self.setpos(0,280)
        self.color("white")
        self.score()
        self.hideturtle()

    def score(self):
        self.clear()
        self.write(arg = f"Score: {self.numscore} High Score: {self.z}", font = ('Arial', 8, 'bold'), align="center")

    def reset(self):
        if self.numscore > self.z:
            with open("SnakeGame/score", 'w') as data:
                data.write(str(self.numscore))
            self.z = self.numscore
        self.numscore = 0
        self.score()

    # def game_over(self):
    #     self.setpos(0,0)
    #     self.write(arg = f"GAME OVER.", font = ('Arial', 30, 'bold'), align="center")

    def touch(self):
        self.numscore +=1