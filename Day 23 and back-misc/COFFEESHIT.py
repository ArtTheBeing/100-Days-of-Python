#COFFEE SHIT
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    for item in resources:
        print(item, resources[item])
    print("Profit:", profit)

def check_ingredients(order, enough = True):
    drink = MENU[order]
    mats = drink["ingredients"]
    for item in mats:
        if mats[item] > resources[item]:
            print("Insufficient", item)
            enough = False
    if enough == True:
        payment(order)

def payment(order):
    global profit
    drink = MENU[order]
    cost = drink["cost"]
    q = int(input("Insert quarters please: "))
    d = int(input("Insert dimes please: "))
    n = int(input("Insert nickels please: "))
    p = int(input("Insert pennies please: "))
    total = q * .25 + d * .10 + n * .05 + p * .01
    if total > cost:
        print("Here's your", order)
        print("Your change is", round(total-cost, 2))
        purchase(order)
        profit = profit + cost
    else:
        print("Insufficient Funds, you have been refunded", total)
        payment(order)


def purchase(order):
    drink = MENU[order]
    mats = drink["ingredients"]
    for item in mats:
        resources[item] = resources[item]- mats[item]


on = True

while on == True:
    cof = input("What coffe would you like?: ")
    if cof == "off":
        on = False
        break
    elif cof == "report":
        report()
    elif cof == "espresso" or cof == "cappuccino" or cof == "latte":
        check_ingredients(cof)
    elif cof == "refill":
         for item in resources:
            add = int(input("How much " + str(item) + " would you like to deposit? "))
            resources[item] = resources[item] + add

    else:
        print("Incorrect Command, Try again!")
            
