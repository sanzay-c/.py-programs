# program to find the even number
def even_number(start, end):
    for i in range(start, end):
        if i % 2 == 0:
            print(i, end=", ")

begin = int(input("Enter a number of stating range to find even number: "))
end = int(input("Enter a number of ending range to find even number: "))
even_number(begin, end)

# ---------------------------------------------

# python function to find the largest/max num number from the list
def max_number(number):
    max_num = 0

    for num in number:
        if num > max_num:
            max_num = num
    
    print(f"The max num from the {number} is: {max_num}")

numbers = [1, 2, 5, 3, 4]

max_number(numbers)

# ---------------------------------------------

# program to reverse a string
def rev_name(name):
    # Remove all whitespace characters from the string
    name = name.replace(" ", "") 

    stored_str = []

    for string in range(len(name)-1, -1, -1):
        # print(name[string], end=" ")
        stored_str.append(name[string])
    print(stored_str)

name = input("Enter a string: ").strip()

rev_name(name)


