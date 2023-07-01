#Hangman
import random
lives = 5
wordlist = ['superman', 'coolio', 'imhim', 'minecraft', 'awesomesauce']
playagain = input("Would you like to play some hangman? (enter 'yes') ")
while playagain == 'yes':
    lives = 5
    userguess = []
    word = random.choice(wordlist)
    word = list(word)
    for w in word:
        userguess.append('_')
    print(word)
    while lives != 0 or userguess == word:
        guess = input("guess a letter")
        for i in range(len(word)):
            print(word[i])
            if lives <= 0:
                print("game over")
                break
            if guess == word[i]:
                print('worked')
                userguess[runner] = guess
            else:
                print()
                lives -= 1
                break
            runner = runner + 1
        print(userguess)

        
    playagain = input("Would you like to play again? (enter 'yes') ")


