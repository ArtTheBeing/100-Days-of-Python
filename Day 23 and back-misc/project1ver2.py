import random
lives = 5
wordlist = ['superman', 'coolio', 'imhim', 'minecraft', 'awesomesauce', 'jamorant']
playagain = input("Would you like to play some hangman? (enter 'yes') ")
while playagain == 'yes':
    lives = 5
    userguess = []
    word = random.choice(wordlist)
    word = list(word)
    for w in word:
        userguess.append('_')
    print(word)
    while lives != 0 and userguess != word:
        guess = input("Guess cracka ")
        counter = 0
        for i in range(len(word)):
            if guess == word[i]:
                userguess[i] = guess
            else:
                counter += 1
            #print(counter)
        if counter == len(word):
            lives -= 1
        print("Lives: ", lives)
        print((userguess))
        #print(word)
    if userguess == word:
        print("Congratulations on winning!")
    else:
        print("Better luck next time")
    playagain = input("Would you like to play again? (enter 'yes') ")