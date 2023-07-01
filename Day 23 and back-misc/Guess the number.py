#Guess the number
import random
print("pick a number between 1-100")
number = random.randint(1,100)
mode = input("Type easy or hard: ")
print("Hint:", number)
def game(mode, x):
    win = False
    if mode == 'easy':
        tries = 10
    if mode =='hard':
        tries = 5
    while win == False and tries != 0:
        guess = int(input("Guess a number: "))
        if guess == x:
            print("You win!")
            break
        elif guess < x:
            print("Guess too low")
            tries -= 1
        elif guess > x:
            print("Guess too high")
            tries -= 1
        print("tries:",tries)
    if tries == 0:
        print("You lost, good luck next time")
game(mode, number)
    