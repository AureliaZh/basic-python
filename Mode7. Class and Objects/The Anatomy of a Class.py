class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + " says: Bark!")

#Functions do something.
#Classes represent something.

#When a class is defined, every instance created from that class automatically has access to the class’s attributes and methods, 
# and each instance maintains its own state.
#Function is like a calculator that performs a task and forgets everything after.
#Class is like an object that owns data, keeps state, and knows how to act on itself.