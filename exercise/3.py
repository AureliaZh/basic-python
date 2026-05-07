class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    def is_puppy(self):
        return self.age < 2


my_dog = Dog("Buddy", 1)

print(my_dog.bark())
print(my_dog.is_puppy())