#Playaround

def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(add(3,5,6,7))

def calculate(n ,**kwargs):
    print(kwargs)
    #print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["mult"]
    print(n)

calculate(2, add = 3, mult = 5)


class Car:
    def __init__(self, **kw):

        #doing .get instead of brackets allow for it to return "none" instead of an error
        self.make = kw.get('male')
        self.model = kw.get('model')
        self.color = kw.get('color')

car = Car(make = "Dodge", color = "black")
print(car.model)

