"""
Create arrays manually with np.array()

Generate arrays using  .arange(), .random(), and .linspace()

Analyse the shape and dimensions of a ndarray

Slice and subset a ndarray based on its indices

Do linear algebra like operations with scalars and matrix multiplication

Use NumPys broadcasting to make ndarray shapes compatible

Manipulate images in the form of ndarrays

"""

import numpy as np
from scipy import misc
# from PIL import Image
from numpy.random import random

# create a 1-dimensional array
my_array = np.array([1.1, 9.2, 8.1, 4.7])
# print(my_array[2])

# heck the dimensions of my_array
# print(my_array.ndim)

# Show rows and colums
# print(my_array.shape)

# create a 2-dimensional array (i.e., a “matrix”)
array_2d = np.array([[1, 2, 3, 9], [5, 6, 7, 8]])
# print(f'array_2d has {array_2d.ndim} dimensions')
# print(f'Its shape is {array_2d.shape}')
# print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
# print(array_2d)


# access the 3rd value in the 2nd row
# print(array_2d[1, 2])

# access an entire row and all the values therein
# print(array_2d[0, :])

# N-dimensional array
mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[7, 86, 6, 98],
                           [5, 1, 0, 4]],

                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])

# How many dimensions
# print(f'mystery_array has {mystery_array.ndim} dimensions')

# What is its shape (i.e., how many elements are along each axis
# print(f'Its shape is {mystery_array.shape}')

# Try to access the value 18 in the last line of code
# print(mystery_array[2, 1, 3])

# Try to retrieve a 1-dimensional vector with the values [97, 0, 27, 18]
# print(mystery_array[2, 1])

# Try to retrieve a (3,2) matrix with the values [[ 0, 4], [ 7, 5], [ 5, 97]]
# print(mystery_array[:, :, 0])

# Use .arange()to createa a vector a with values ranging from 10 to 29
a = np.arange(10, 30)
print(a)

# Create an array containing only the last 3 values of a
print(a[-3:])

# Create a subset with only the 4th, 5th, and 6th values
print(a[3:6])

# Create a subset of a containing all the values except for the first
print(a[1:])

# Create a subset that only contains the even numbers (i.e, every second number
print(a[::2])

# Reverse the order of the values in a, so that the first element comes last
print(np.flip(a))
print(a[::-1])

# Print out all the indices of the non-zero elements in this array: [6,0,9,0,0,5,0]
b = np.array([6, 0, 9, 0, 0, 5, 0])
nz_indices = np.nonzero(b)
# note this is a tuple
print(nz_indices)

# Use NumPy to generate a 3x3x3 array with random numbers
z = random((3, 3, 3))
print(z)

# Use .linspace() to create a vector x of size 9 with values spaced out evenly between 0 to 100 (both included).
x = np.linspace(0, 100, num=9)
print(x)
print(x.shape)

# Use .linspace() to create another vector y of size 9 with values between -3 to 3 (both included).
# Then plot x and y on a line chart using Matplotlib

y = np.linspace(-3, 3, num=9)
# plt.plot(x, y)
# plt.show()

# broadcasting and expanding / the result of a MUl in arrays is to expand smaller to bigger
# so 2 by 3 in 1 by 5 result in 2 by 5
a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])

b1 = np.array([[4, 1, 3],
               [5, 8, 5]])
c = np.matmul(a1, b1)
print(f"Matrix C has {c.shape[0]} rows and {c.shape[1]} columns")
