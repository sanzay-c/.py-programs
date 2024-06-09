def std_mark(key, value):
    std_info = {
        "student1" : {
            "subjects" : {
                "math" : 50,
                "science" : 60,
                "social" : 70
            }
        },

        "student2" : {
            "subjects" : {
                "math" : 60,
                "science" : 66,
                "social" : 50
            }
        }
    }

    if key in std_info:
        student_subject = std_info[key]["subjects"]
        return student_subject
    else:
        print("The student not found")


stundent_subject = std_mark("student1", "subject")
print(stundent_subject)

