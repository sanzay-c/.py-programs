# normal one
def even_number():
    for i in range(0, 100):
        if i % 2 == 0:
            print(i)

even_number()

# function one
def check_even_number(number):
    if number % 2 == 0:
        print(f"The number {number} is the even number")
    else:
        print(f"The number {number} is not the even number")

user_input = int(input("Enter a number: "))

check_even_number(user_input)

# note: 'input()' is by default a str -> string so if you are taking a number you must type cast into a int -> interger
