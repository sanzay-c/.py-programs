# # Write a Python program that takes a list of numbers and returns a new list with only the even numbers.

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []

def list_of_number():
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] % 2 == 0:
            new_list.append(list_of_numbers[i])

    print(new_list)

list_of_number()

# # Write a Python program that takes a list of strings and returns a new list with the strings in reverse order.

list_of_string = ['name', 'age', 'gender']
new_list = []

for i in range(len(list_of_string)-1, -1, -1):
    new_list.append(list_of_string[i])

print(f"The original list: {list_of_string}")
print(f"The reversed list: {new_list}")


# Write a Python program that takes a list of numbers and returns the average of the numbers
list_of_num = [1, 2, 3, 4, 5, 6]

def average_from_list(list_of_num):
    count = 0

    for i in range(len(list_of_num)):
        count += list_of_num[i]
        total_num = count
        result = total_num / len(list_of_num)

    print(f"the average of {list_of_num} is: {result}")

average_from_list(list_of_num)
