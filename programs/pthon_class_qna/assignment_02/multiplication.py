# Write a Python program that prints the multiplication table of a given number.

number = int(input("Enter a number for multiply: "))
limit = int(input("Enter a limit: "))

def multiplication():
    for i in range(1, limit + 1):
        total = number * i
        print(f"{number} x {i} = {total}")

multiplication()
