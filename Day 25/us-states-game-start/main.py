from turtle import Screen, Turtle
import pandas

data = pandas.read_csv("Day 25/us-states-game-start/50_states.csv")

#print(data)

writer = Turtle()
writer.penup()
writer.hideturtle()
#Writing Turtle Functions


screen = Screen()
screen.setup(width = 725, height = 491)
screen.bgpic("Day 25/us-states-game-start/blank_states_img.gif")
#Initialize Screen


game_is_on = True
lives = 5
while lives > 0 and game_is_on == True:
    user_bet = screen.textinput(title = f"You have {lives} lives", prompt = f"Enter a state name, you have {len(data.index)} to go:")
    if user_bet != None:
        user_bet = user_bet.title()

    #print(data.state)    This shows all the values in the state column

    if (user_bet in data.state.values) == True: #Checks for if data.state.values contains user_bet
        info = (data[data.state == user_bet])
        x = int(info.x)
        y = int(info.y)
        #Collect Index
        index = info.index
        writer.goto(x,y)
        writer.write(user_bet)
        #Drop Index
        data = data.drop(info.index)
    else:
        lives -= 1
print(f"Missed States\n {data.state}")

data.state.to_csv("Day 25/us-states-game-start/states_to_learn")

    #DONT MIND THIS WAS TESTING
    # state = data[data.state == "Alabama"]
    # print(state)

screen.exitonclick()

