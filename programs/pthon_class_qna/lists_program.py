def sum_of_list(list_of_array):
    total = 0
    for num in list_of_array:
        total += num
    return total

array = [1, 3, 6, 7, 2, 4, 3]
sum = sum_of_list(array)
print(f"the sum of elements of array is {sum}")


#*Concatenate Two Lists in a Specific Order*:

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

# result = [f"{x} {y}" for x in list1 for y in list2]

# print(result)

# for i in range(len(list1)):
#     new_list = list1[i] + list2[i]
#     print(new_list)

result = []

for x in list1:
    for y in list2:
        result.append(f"{x}{y}")

print(result)


# *Square Each Item in a List*:

numbers = [1, 2, 3, 4, 5, 6, 7]

new_list = []

for num in range(len(numbers)):
    square = numbers[num] ** 2
    new_list.append(square)

print(f"the new list is: {new_list}")


# list2 in reverse order and display items from list1

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

list2.reverse()

for i in range(len(list1)):
    print(str(list1[i]) + " " + str(list2[i]))
