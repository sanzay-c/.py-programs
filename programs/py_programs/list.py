info = ['Dororo', 20, 'kathmandu']
print(type(info)) #shows the type 
print(info[0])    #returns the 0 index that is dororo 

myList = [5, 8, 7, 2, 9]
print(myList.append(1)) # adds and put it in the last
print(myList.sort())
print(myList) 

# function to add a tolal elements of list (python class question answer)

def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [1, 2, 3, 4, 5, 6, 6]
total = sum_of_list(numbers)
print(total)