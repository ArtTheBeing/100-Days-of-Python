from gamedata1 import data
import random
lost = False
points = 0
first = random.choice(data)
while lost == False:
    print('\n\n')
    print("Name: ", first['name'], "\nDescription: ", first['description'], "\nCountry:", first['country'])
    firstval = first['follower_count']
    print()
    print("VS")
    print()
    data.remove(first)
    second = random.choice(data)
    secval = second['follower_count']
    print("Name: ", second['name'], "\nDescription: ", second['description'], "\nCountry:", second['country'])
    print()
    #CHEAT print(firstval)
    #CHEAT print(secval)
    userguess = int(input("Who do you think has more follower? (1 for top, 2 for bottom)"))
    if (len(data) < 2):
        print("You have beaten the game")
        lost = True
        break
    if (userguess == 1 and firstval > secval) or (userguess == 2 and firstval < secval):
        points += 1
        print("Great Job, Heres a point! points:", points)
        first = second
    else:
        print("YOU LOSE!")
        lost = True
print("Final Score:", points)