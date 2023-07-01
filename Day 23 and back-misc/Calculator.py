#Calculator
runagain = True
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1/n2
opps = {'+': add, '-': subtract, "/": divide, "*": multiply}


def calculation(n1, opp, n2):
    cal = opps[opp]
    return cal(n1, n2)

while runagain == True:
    num1 = int(input("First Number: "))
    for sym in opps:
        print(sym)
    oper = input("Opperator?:")
    num2 = int(input("Second Number: "))
    print(calculation(num1, oper, num2))
    runa = input("Run again? (y/n): ")
    if runa == "n":
        runagain = False
