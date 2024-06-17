# Write a Python program that takes a string as input and prints its reverse.
string_to_reverse = input("Enter a string to reverse: ")

def reverse(string):
    #using for loop to reverse
    for i in range(len(string)-1, -1, -1):
        print(string[i], end="")

    #using slicing to reverse the string
    new_string = string[::-1]
    print(new_string)

reverse(string_to_reverse)


# Write a Python program that counts the number of vowels in a given string.
sentence = 'Education'
count = 0
list = []

for char in range(len(sentence)):
    if sentence[char] == "a" or sentence[char] == "e" or sentence[char] == "i" or sentence[char] == "o" or sentence[char] == "u" or sentence[char] == "A" or sentence[char] == "E" or sentence[char] == "I" or sentence[char] == "O" or sentence[char] == "U":
        list.append(sentence[char])
        count += 1

print(list)
# # --------- you can also count in another way give below
sentence = input("Enter a sentence to count number of vowels: ")
list = []
vowel = "aeiouAEIOU"

def count_vowel(sentence):
    count = 0

    for char in range(len(sentence)):
        if sentence[char] in vowel:
            list.append(sentence[char])
            count += 1

    print(count)

count_vowel(sentence)

# Write a Python program that takes a string and returns a new string with all the vowels removed.
user_input = input("Enter a string: ")
vowels = "aeiouAEIOU"

def remove_vowels(string):
    new_string = ""

    for char in string:
        if char not in vowels:
            new_string += char

    print(f"The new string the vowels removed is: {new_string}")

remove_vowels(user_input)
        

