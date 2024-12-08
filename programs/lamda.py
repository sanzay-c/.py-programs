# lamda function takes "lambda argument: expression"
# -- filter(function, iterable), The filter() function in Python takes two arguments
#    The filter will only "keep" the items that meet the condition and ignore the others.

number = [1, 2, 3, 4, 5, 6]

even_number = list(filter(lambda x: x % 2 == 0, number))

print(even_number)


sum_of_two_number = lambda a, b: a + b
print(sum_of_two_number(10,20))



# number = [1, 2, 3, 4, 5]

# my_num = map(lambda num : num + num, number)

# print(list(my_num))

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_num = map(lambda x : x % 2 == 0, number)

print(list(even_num))