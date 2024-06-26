# list are mutable(changebale) where tuple are immutable(which cannot be changed) once declared cannot be changed
# valid tuple is with "()" with "," inside

tuple = (2, 1, 3, 4, 5, 2)

print(tuple)
print(tuple[1:3]) # slicing
# methods
print(tuple.index(3)) # here the index of element 3 is 2 i.e is in 2nd index

print(tuple.count(2)) # it counts how many times two is appeared in tuples

print(type(tuple))
