# to create an empty dictionary '{}' or 'variable_name = dict()'
# heterogeneous is different and homo => same
# key must be unique

dictionary = {
    "name" : "sanjay",
    "age" : 30,
    "address" : {"city" : "balaju"}
}                        

# Accessing elements
print(dictionary['name'])  
print(dictionary.get('age'))  

print(dictionary['address']['city'])

# Modifying elements
dictionary['age'] = 31
dictionary.update({'gender': 'male'})
print(dictionary)

# Removing elements
removed_value = dictionary.pop('address')
print(removed_value)  
print(dictionary)  


# Dictionary views
print(dictionary.keys())  
print(dictionary.values())  
print(dictionary.items())  

# Clearing the dictionary
dictionary.clear()
print(dictionary)  # Output: {}

# typecasting
print(list(dictionary))