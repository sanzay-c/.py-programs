class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"
    

dog = Dog("Doggy")
cat = Cat("Catty")

print(f"{dog.name} says: {dog.speak()}")
print(f"{cat.name} says: {cat.speak()}")