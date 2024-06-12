# words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# words_count = {}

# for word in words:
#     words_count[word] = words.count(word)

# print(words_count)


# def count_number_of_words(list_of_string):
#     words_count = {}

#     for word in list_of_string:
#         words_count[word] = list_of_string.count(word)

#     print(words_count)

# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# count_number_of_words(words)



def count_frequencies(words):
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies

# Test the function
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(count_frequencies(words))



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




