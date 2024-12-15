class Employee:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def __str__(self):
        return f" The name is: {self.name} \n The age is: {self.age} \n The address is: {self.address}"

class Person(Employee):
    def __init__(self, name, age, address, salary, education):
        super().__init__(name, age, address)
        self.salary = salary
        self.education = education
    
    def __str__(self):
        return f"{super().__str__()} \n The salary: {self.salary} \n The Education is: {self.education}"

person = Person(name="Sanjay", age=23, address="kathmandu", salary=20000, education="Bachelor(BCA)")
print(person)