# nested dictionary, dictionary inside a dictionary
student = {
    "name" : "light yagami",
    "subjects" : {
        "math" : 71,
        "science" : 80,
    } 
}

print(student)
print(student["name"])
print(student["subjects"])
print(student["subjects"]["math"])


# adding items in the empty dictionary
student = {}

name = input("Enter your name: ")
student.update({"name": name})

age = int(input("Enter your age: "))
student.update({"age": age})

student["hobbies"] = []  # Initialize hobbies as an empty list
for i in range(5):
    hobby = input("Enter hobby {}: ".format(i+1))  # Prompt user for hobby input
    student["hobbies"].append(hobby)  # Append hobby to the list

print(student)

# '.format()' allows you to insert values into a string in a specified format.