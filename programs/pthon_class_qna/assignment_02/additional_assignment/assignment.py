# Write a Python program to create a list containing the first 10 natural numbers.
list = []

begin = int(input("Enter a starting range: "))
end = int(input("Enter a ending range: "))

def print_natural_number(start, end): 
    for i in range(start, end):
        list.append(i)
    print(f"The natural number from {start} and {end}: {list}")

print_natural_number(begin, end)

#  Write a Python function that takes a list of numbers as input and returns the sum of all the elements.
list = [1, 2, 3]

def print_sum(list):
    sum = 0

    for i in range(len(list)):
        sum += list[i]

    print(f"The sum of {list} is: {sum}")

print_sum(list)

#  Write a Python program to append an element to an existing list.
list = [4, 5, 6] # existing list

list.insert(0, 7) # to insert into the 0'th  index and so on..

list.append(7) # append to the existing list

print(list)

# Write a Python program to find the factorial of a given number using a while loop.
fact = 1             # Initialize 
number = 5           # to find factorial

while number > 0:    # Start a while loop that continues while number is greater than 0
    fact *= number   # Multiply fact by the current value of number
    number -= 1      # Decrement number by 1 in each iteration of the loop

print(f"The factorial is: {fact}")  # Print the computed factorial after the loop terminates


# Write a Python program to print the multiplication table of a given number using a for loop.
number = int(input("Enter a number to multiply: "))
limit = int(input("Enter a limit: "))

def multiplication(number, limit):
    for i in range(1, limit + 1):
        total = number * i
        print(f"{number} x {i} = {total}")

multiplication(number, limit)

# Write a Python function that checks whether a given string is a palindrome (reads the same forward and backward).
string = input("Enter a String to check palindrome: ")

def palindrome(string):
    rev_str = ""

    for i in range(len(string)-1, -1, -1):
        rev_str += string[i]

    if rev_str == string:
        print(f"Entered string i.e '{string}' is palindrome")
    else:
        print(f"Entered string i.e '{string}' is not palindrome")

palindrome(string)


# Write a Python program to count the number of times a specific character appears in a given string.
def count_specific_char(name, char):
    if len(char) > 1 or len(char) == 0:
        print("You enterd more than one character")
        return

    count = 0
    
    for i in range(len(name)):
        if name[i] == char:
            count += 1

    print(f"The number of times '{char}' appeared is {count} time")

name = input("Ente a string: ")
char = input("Enter a single char: ")

count_specific_char(name, char)

# Write a Python program to update the value associated with a specific key in a dictionary.
dict = {}

dict.update({
    "name": "my-name",
    "age" : 23,
    "address" : "kathmandu",
    "faculty" : "BCA",
    "hobbies" : ['singing', 'dancing', 'travelling']
})

for key, values in dict.items():
    print(key, values)

hobby = dict["hobbies"][0]
print(hobby)

file_path = "D:\\python_programmes\\python_programs\\programs\\pthon_class_qna\\file_handling\\txt_files\\hello.txt"

with open(file_path, "w") as file: # 'w' to write and 'r' to read
    # file.write() # to wrte in the file
    read = file.read() # for reading
    print(read)
