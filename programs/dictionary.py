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