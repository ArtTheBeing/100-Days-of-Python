from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
men = Menu()
cofmaker = CoffeeMaker()
moneymach = MoneyMachine()
on = True
while on == True:
    print(men.get_items())
    drink = input("Which choice would you like? ")
    if drink == "off":
        on = False
        break
    elif drink == "report":
        cofmaker.report()
        moneymach.report()
    elif men.find_drink != "None":
        order = men.find_drink(drink)
        if cofmaker.is_resource_sufficient(order) == False:
            print("insufficient ingredients")
        else:
            if moneymach.make_payment(order.cost) == True:
                cofmaker.make_coffee(order)
        
