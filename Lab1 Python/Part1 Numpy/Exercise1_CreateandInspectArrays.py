# Exercise 1: Create and Inspect Arrays
# 1. Create a 1D NumPy array of integers from 0 to 9.
# 2. Create a 3x3 NumPy array with random integers between 1 and 20.
# 3. Get the shape and data type of both arrays.
import numpy as np

#Create a 1D NumPy array of integers from 0 to 9
arr1d= np.arange(10)
print(arr1d)

#Create a 3x3 NumPy array with random integers between 1 and 20
arr3x3= np.random.randint(1,20,(3,3))
print(arr3x3)

#Get the shape and data type of both arrays
print(arr1d.shape, arr1d.dtype)
print(arr3x3.shape, arr3x3.dtype)