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

