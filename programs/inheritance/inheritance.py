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


# another example of inheritance

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"


class Student(Person):
    def __init__(self, name, age, address, faculty):
        self.faculty = faculty
        super().__init__(name, age, address)

    def __str__(self):
        return f"{super().__str__()}, faculty: {self.faculty}"


student = Student("sanjay", 23, "Kathmandu", "BCA")
print(student)
