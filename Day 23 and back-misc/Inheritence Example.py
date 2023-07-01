#Inheritence Example:

class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Inhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Moving in water")

    def breathe(self):
        super().breathe()
        print("Doing this underwater")

nemo = Fish()

nemo.breathe()