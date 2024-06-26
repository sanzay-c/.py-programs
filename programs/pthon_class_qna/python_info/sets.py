# set is the collection of the unordered items. there is no index
# each element in the set must be unique and immutable
# repeated elements stored only once
# set is with "{}"
# duplicate values are ignored in sets
# to create an empty set "variable_name = set()"
# sets is mutable and the elements in sets are immutable

sets = {1, 2, 3, 4, "hello", "world", 2, 2}

empty_set = set() # create and empty set

print(sets)

print(len(sets)) # output returns ignoring duplicate values

print(type(sets))

# --------------------------------------

# methods
set = set()
set.add(1)
set.add(2)
set.add(3)
set.add(4)
set.add("hello")
set.add((1, 2, 1)) # adding tuple but cannot add the lists

set.remove(4) # remove the element

set.clear() # it empties the set

print(set)

my_set = {"hello", "world", "python"}
print(my_set.pop()) # pop the random element

# --------------------------------------

# set.union() combines both set values and returns new
# set.intersection() combines commoon values and returns new

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2)) # combine and remove duplicates and return new

print(set1.intersection(set2)) # retuns common element

# --------------------------------------

subjects = {
    "python", "java", "c++", "python", "javascript",
    "java", "python", "java", "c++", 'c'
}

print(subjects)
print(len(subjects))
