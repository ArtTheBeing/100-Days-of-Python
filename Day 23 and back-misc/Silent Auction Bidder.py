#Silent Auction Bidder
import os
print("Welcome to the silent auction!")
run = True
bids = {}
while run == True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bids[name] = bid
    runagain = input("Is there another bidder?: ")
    if runagain == 'yes':
        os.system('cls')
    else:
        run = False
currentmax = 0
topdawg = ""
for n in bids:
    if bids[n] > currentmax:
        currentmax = bids[n]
        topdawg = n
print(topdawg, "wins with", currentmax)