def reverse_string(string):
    for i in range(len(string)-1, -1, -1):
        print(string[i], end=" ")

user_input = str(input("Enter a string to reverse: "))

reverse_string(user_input)
