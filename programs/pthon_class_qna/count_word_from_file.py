file_path = r"D:\python_programmes\python_programs\programs\pthon_class_qna\file_handling\txt_files\words.txt"

word_arr = []
word_count = {}

with open(file_path, 'r') as f:
    for file in f.readlines():
        word_arr += file.split()
        for word in word_arr:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        
        print(word_count)


