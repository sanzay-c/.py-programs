# list 
list1 = [1, 2, 4, 2, 1]

# copy of the list
list1_copy = list1.copy()
# reverse the copied list
list1_copy.reverse()

# check if the reversed list is equal to the original list
if list1_copy == list1:
    print(f"{list1}: It is a palindrome") 
else:
    print(f"{list1}: It is not the palindrome")