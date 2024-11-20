# lamda function takes "lambda argument: expression"
# -- filter(function, iterable), The filter() function in Python takes two arguments

number = [1, 2, 3, 4, 5, 6]

even_number = list(filter(lambda x: x % 2 == 0, number))

print(even_number)


sum_of_two_number = lambda a, b: a + b
print(sum_of_two_number(10,20))
