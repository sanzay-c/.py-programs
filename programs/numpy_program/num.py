import numpy as np

# creating a 2D array
array2d = [[1,2], [3, 4], [5,6]]
arr1 = np.array(array2d)
print(f"2D array: \n {arr1}")


# -- Both lists [] and tuples () are acceptable for defining the shape,
#    but it's generally more common to use a tuple () when working with numpy functions.

# array of zeros
array_zeros = np.zeros((2,3)) # (2,3) => 2x3 matrix
print(f"array of zeros: \n {array_zeros}")

# array of ones
array_ones = np.ones((2,3)) # (2,3) => 2x3 matrix
print(f"array of ones: \n {array_ones}")

# array of zero
array_list = [[1, 2, 3], 
              [4, 5, 6],
              [7, 8, 9],]
print(f"transpose: \n {np.transpose((array_list))}")

# generating the random number
random_array = np.random.rand(2,3) # (2,3) => 2x3 matrix, random from 0 to 1
print(random_array)

# generating custom random number -- using .randint 
# -- generate random number form 0 to 10 and matrix is (3,3) => 3x3 matrix
random_array01 = np.random.randint(0, 10, size=(3,3))
print(random_array01)


# .dot matrix meaning multiplication
a = [[1, 5, 6],
    [7, 8, 9],
    [2, 0, 1],]

b = [[1, 5, 6],
    [7, 8, 9],
    [2, 0, 1],]

dot_matrix = np.dot(a, b)
print(f"Multiplication matrix{a} and {b}: \n {dot_matrix}")

# ------ mean, min, max, sum, exp, sqrt
arr = [1, 3, 5, 6, 9]

# mean
array_mean = np.mean(arr)
print(f"The mean array of {arr} is: {array_mean}")

# min => minimum
array_min = np.min(arr)
print(f"The min array of {arr} is: {array_min}")

# max => maximum
array_max = np.max(arr)
print(f"The max array of {arr} is: {array_max}")

# sum
array_sum = np.sum(arr)
print(f"The sum of {arr} is: {array_sum}")

# exp => exponential
array_exp = np.exp(arr)
print(f"The exponential of {arr} is: {array_exp}")

# sqrt => square root
array_sqrt = np.sqrt(arr)
print(f"The sqrt of {arr} is: \n {array_sqrt}")

# ----------------------------------------------

# array in a single row
array_falttern = np.array([[1, 2, 3], [4, 5, 6]])
# Flatten the 2D array into 1D
flattened_arr = array_falttern.flatten()
print(f"falttern array of {array_falttern} is: \n{flattened_arr}")


