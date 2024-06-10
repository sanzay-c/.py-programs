file_path = "D:\\python_programmes\\python_programs\\programs\\pthon_class_qna\\file_handling\\txt_files\\new_file001.txt"

def append_text(file_path, text):
    with open(file_path, "a") as f:
        f.write(text)
    print("Text append successful")

text_to_append = 'This is the new text to append'
append_text(file_path, text_to_append)
