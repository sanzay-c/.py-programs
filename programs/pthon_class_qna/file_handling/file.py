# can use r as the prefix because it denotes "raw" string literal or double slashes to ignore escape character

file_path = "D:\\python_programmes\\python_programs\\programs\\pthon_class_qna\\file_handling\\info.txt"

with open(file_path, "r") as f: # for reading the file
    data = f.read()
    print(data)
    f.close()

with open(file_path, "r") as f: # to read a line
    read_line = f.readline()
    print(read_line)
    f.close()

with open(file_path, "w") as f: # for writing in the text file, write override the entire whera "a" add appends
    for i in range(100):
        f.write("Hello world \n")
    f.close()
    print(type(f))

#---------------------------------------
import os

file_path01 = "D:\\python_programmes\\python_programs\\programs\\pthon_class_qna\\file_handling\\"
file01 = "new_file.txt"

# with open(file_path01, 'w') as f:
#     f.write("new file created")

with open(file_path01 + "\\" + file01, "w") as f:
    f.write("new file created")

# os.remove(file_path01 ) # for removing the file


#---------------------------------------
# --- program to create a multiple file 
import os

file_path02 = "D:\\python_programmes\\python_programs\\programs\\pthon_class_qna\\file_handling\\txt_files"

for i in range(1,10):
    file = f"file_{i}.txt"
    with open(file_path02 + "\\" + file, 'a') as f:  # Open file in append mode, the specified filename (file_path02 + "\\" + file) in the specified directory 
        f.write(f"This is file number {i}.\n")
    print(f"created {file_path02}\\{file}")  # Print the created file path, printing the file in the terminal like showing in the terminal  
    # os.remove(file_path02 + "\\" + file) # for removing the existing file
    