# here self represent object/ instance of the class

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print("the student is studying")

    def __str__(self):
        return f"The name is {self.name} and the age is {self.age}"

std = Student(name="sanjay", age=23)
# print(f"the name is {std.name} and the age is {std.age}")
print(std)
std.study()


#  static method => it uses a decorator called @staticmethod which doesnt't use (self) as parameter
class Student:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def print_hello():
        print("hello")

    def __str__(self) -> str:
        return f"The name is {self.name}"

std = Student(name="sanzay-c")
print(std)
std.print_hello()

# anothe program
class Account:
    def __init__(self, bal, acc): 
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print(f"Rs. {amount} was debited from account number {self.account_no}")
        print(f"Total balance = {self.get_balance()} \n")

    def credit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} is credited from account number {self.account_no}")
        print(f"Total balance = {self.get_balance()} \n")

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(4000)
        