# for *args 
# -- *args works similarly to **kwargs, 
#     but it is used to capture positional arguments and stores them as a tuple.
#     - *args handles positional arguments and stores them in a tuple, 
#     - Lets you pass multiple values to a function without naming them.--
def print_args(*args):
    print(args)

print_args(1, 34, 56)

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(1, 2, 3))  
print(add_numbers(5, 10))    

# for **kwargs
# -- The **kwargs parameter in Python functions allows you to pass multiple keyword arguments, 
#    which are stored in a dictionary 
#    - *kwargs handles named multiple arguments and stores them in a dictionary, 
#    - Lets you pass multiple values to a function without naming them and stores them in dictionary--
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(name="hello", age=25, city="Kathmandu")
