def second_largest_number(number):
    max_num = 0
    second_max = 0

    for num in numbers:
        if num > max_num:
            second_max = max_num
            max_num = num
        if num > second_max and num != max_num:
            second_max = num
    
    return second_max


numbers = [1, 3, 4, 5, 6]
second_largest_num = second_largest_number(numbers)
print(second_largest_num)