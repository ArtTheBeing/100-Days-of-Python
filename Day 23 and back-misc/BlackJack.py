#BlackJack
import random
repeat = True
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

while repeat == True:
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    re = input("Would you like to play a game of blackjack? ('y' for yes): ")
    if re != 'y':
        repeat = False
        break
    print(logo)
    yours = [random.choice(cards), random.choice(cards)]
    dealer = [random.choice(cards)]
    print(yours, "Your cards")
    print(dealer, "Dealer cards")
    hit_bool = True
    if sum(yours) == 21:
        print("YOU WON!")
        break
    hit = input("Would you like to hit? ('y'/'n')")
    lost = False
    while hit_bool == True:
        #hit = input("Would you like to hit? ('y'/'n')")
        if hit == 'n':
            hit_bool = False
            break
        else:
            yours.append(random.choice(cards))
            if sum(yours) < 21:
                print('Your hand', yours)
                hit = input("Would you like to hit again? ('y'/'n')")
                continue
            elif sum(yours) > 21:
                hit_bool = False
                print("You got", sum(yours))
                print("You lose")
                lost = True

            elif sum(yours) == 21:
                print(sum(yours))
                print("you hit", sum(yours))
                print("You win!")
        #print(yours)
    if lost == False:
        while sum(yours) > sum(dealer) and sum(dealer) <= 21:
            dealer.append(random.choice(cards))
        if sum(dealer) == sum(yours):
            print(dealer, "Dealers hand")
            print(yours, "Your hand")
            print("Its a tie!")
        elif sum(dealer) > sum(yours) and sum(dealer) <= 21:
            print(dealer, "Dealers hand")
            print(yours, "Your hand")
            print("Dealer wins!")
        else:
            print(dealer, "Dealers hand")
            print(yours, "Your hand")
            print("You win!")

        
    


        
