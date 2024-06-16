# Write a Python program that prints all the numbers from 1 to 20 that are divisible by 3.
# for i in range(1, 21): 
#     if i % 3 == 0:
#         print(i)

# --------or

def number_divide_by_three(begin, end):
    list = [] 

    for i in range(begin, end):
        if i % 3 == 0:
            list.append(i) # appending numbers in empty list to show the entered number

    print(f"the numbet divided by 3 are: \n{list}")

start = int(input("Enter the beginning range: "))
end = int(input("Enter the ending range: "))

number_divide_by_three(start, end)