# The input() function is used to accept user input
# The input() function always returns a string, even if the user enters a number

# accept user input
name = input("Enter your name: ")
print(f"Hello {name}")

# accepting int or float
# without typecasting it will return str, 
# same typecasting is done for flaot as well,
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# or typecasting can also be done like this,
# --------- total = int(num1) + int(num2)
total = num1 + num2

print(f"The sum of {num1} and {num2} is: {total}")


string = "string"

for i in range(len(string) -1, -1, -1):
    print(string[i], end="  ")

print(2 % 2 == 0)

num = float(input("Enter number: "))

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


   