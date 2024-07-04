# 01. write a function that takes number as an argument and return true  if even or false 
def check_even_odd(number):
    if number % 2 == 0:
        print(f"The {number} is a even")
    else:
        print(f"The {number} is odd")

user_input = input("enter a number: ")

check_even_odd(user_input)

# 02. write a function that takes string as an argument and return reversed of string
def reversed(string):
    for i in range(len(string) -1, -1, -1):
        print(string[i], end=", ")

user_input01 = input("enter a string: ")

reversed(user_input01)

# 03. write a function that takes string as an argument and return length of string
def length_str(string):
    count = 0

    for i in range(len(string)):
        count += i
    print(f"The length of the entered string is: {count}")

user_input03 = input("enter a string: ")

length_str(user_input03)

# 04. write a function that takes string as an argument and return first char of string
def first_char(string):  # milenah
    for i in range(len(string)):
        first_char = string[i][0]
        first_char = [0]

user_input = input("Enter a string: ")

first_char(user_input)

# 05. write a function that takes string and returns true if first char is upper case else return false

# 06. write a function that takes string as an argument and return last char of string

# 07. write a function that takes string as an argument and check if digit is present in the string

# 08. write a function that takes string as an argument and check if palindrome or not disregarding case sensitivity 
def check_string_palindrome_or_not(string):
    # rev_str = string[::-1] # you can use slicing to reverse the string

    rev_str = ""
    for i in range(len(string)-1, -1, -1):
        rev_str += string[i]

    if string == rev_str:
        print(f"{string} is palindrome")
    else:
        print(f"{string} is not a palindrome")

user_input = input("Enter a string: ")

check_string_palindrome_or_not(user_input)

# 09. write a function that takes string as argument the count of the letter U present in the string without using count disregarding case sens
def count_u(string):
    letter = 'uU'
    count = 0

    for char in range(len(string)):
        if string[char] in letter:
            count += 1    
    print("The sentence does not contain any 'u' character")
    print(f"The number 'u' present in the {string} is: {count}")

user_input09 = input("Enter a string: ")

count_u(user_input09)

# 10. write a function that takes string as argument whether letter u is present or not

# 11. write a function that takes list of numbers as argument  and return list of number with only even number
def even_only(even_list):
    new_list = []

    for i in range(len(even_list)):
        if even_list[i] % 2 == 0:
            new_list.append(even_list[i])
    print(f"old list: {even_list}, with even only are: {new_list}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_only(numbers)

# 12. write a function that takes multiple number and return maximum of those number
def max_number(number):
    max_num = 0

    for num in number:
        if num > max_num:
            max_num = num

    print(f"The max num for {number} is: {max_num}")

numbers = [12, 19, 10, 11, 9, 2]

max_number(numbers)

# 13. write a function that takes a string as a argument and check whether vowels are present
def vowels_present(string):
    vowels = 'aeiouAEIOU'
    count = 0
    new_string = []
    
    for char in range(len(string)):
        if string[char] in vowels:
            count += 1
            new_string += string[char]
    print(f"The number of vowels are: {count}")
    print(f"The vowels in the letter '{string}' are: {new_string}")

user_input13 = input("Enter a string: ")

vowels_present(user_input13)

# 14. write a function that takes a string as a argument and check whether consonant is present or not
def consonants(string):
    vowels = 'aeiouAEIOU'
    count = 0
    new_string = []
    
    for char in range(len(string)):
        if string[char] not in vowels:
            count += 1
            new_string += string[char]
    print(f"The number of consonants are: {count}")
    print(f"The consonants in the letter '{string}' are: {new_string}")

user_input14 = input("Enter a string: ")

consonants(user_input14)

# 15. write a function that takes a string as a argument and returns the first vowel present in string
def first_vowel(string):
    vowels = 'aeiouAEIOU'

    for char in string:
        if char in vowels:
            return char

user_input15 = input("Enter a string: ")

vowel = first_vowel(user_input15)
print(f"first vowels in the string is: {vowel}")

# 16. write a function that takes a string as a argument and returns the first consonant present in string
def consonants(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for char in string:
        if char not in vowels:
            return char

user_input16 = input("Enter a string: ")
conso = consonants(user_input16)
print(f"first consonants present in string is: {conso}")


# 17. write a function that takes a string as a argument and returns the total number of vowels present in string
# Qno.17 = 13

# 18. write a function that takes a string as a argument and returns the total number of consonant present in string
# Qno.18 = 14

# 19. write a function that takes a number and returns list of even number upto that number without using range
# 20. write a function that takes a number as argument and returns list of even and odd  number upto that number without using range
   