words = ["apple", "banana", "apple", "orange", "banana", "apple"]

words_count = {}

for word in words:
    words_count[word] = words.count(word)

print(words_count)





# grades = {
#     "A" : 80,
#     "B" : 70,
#     "C" : 60,
#     "D" : 88,
# }

# def names(grades):
#     max = 80

#     for key, values in grades.items():
#         if values > max:
#             max = values
#             print(f"The heighest ranked stdudent name is: {key}, and the grade is: {values}")

# names(grades)


# def count_frequencies(list_of_string):
#     total_list = ""

#     for list in list_of_string:
#         total_list += list
#     return total_list

# lists = ['apple', 'banana', 'orange', 'kiwi']
# total_list = count_frequencies(lists)
# print(total_list)




