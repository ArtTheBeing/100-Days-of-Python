# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# ##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)

# result = calculate(add, 2, 3)
# print(result)

# ##Functions can be nested in other functions

# def outer_function():
#     print("I'm outer")

#     def nested_function():
#         print("I'm inner")

#     nested_function()

# outer_function()

# ## Functions can be returned from other functions
# def outer_function():
#     print("I'm outer")

#     def nested_function():
#         print("I'm inner")

#     return nested_function

# inner_function = outer_function()
# inner_function


#Python Decorator
import time

def delay_decorator(function):
    def wrapper_functions():
        time.sleep(2)
        #Do something before function
        function()
        #Do something after function
    return wrapper_functions

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator  #Syntactic Sugar
def say_bye():
    print('Bye')

def say_greeting():
    print('How are you?')

say_hello()
say_bye()

decfunc = delay_decorator(say_greeting)
decfunc()