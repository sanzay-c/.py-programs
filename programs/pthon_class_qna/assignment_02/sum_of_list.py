# Write a Python program that takes a list of numbers and returns the sum of all the numbers.
list = [1, 3, 4]

count = 0

for i in range(len(list)):
    count += list[i]

print(count)


# -------or
list = []
count = 0

for i in range(3):
    user_input = input("enter a number in list to add: ")
    list.append(int(user_input))
    count += int(user_input)

print(count)
