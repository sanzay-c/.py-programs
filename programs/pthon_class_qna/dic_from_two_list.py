list1 = ["name", "age", "adddress", "faculty"]
list2 = ["sanjay", 23, "kathmandu", "BCA"]

dictionary = {}

dictionary.update(zip(list1, list2))

print(dictionary)

# zip => the first element of list1 is paired with the first element of list2 and so on.
# or you can use dict keyword instead