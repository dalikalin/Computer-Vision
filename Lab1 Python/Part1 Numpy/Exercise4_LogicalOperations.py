# Exercise 4: Logical Operations
# 1. Create a NumPy array of integers from 1 to 10. Find all even numbers in the array.
# 2. Create a boolean mask for values greater than 5 in the array.
# 3. Replace all values greater than 5 with -1
import numpy as np

#Create a NumPy array of integers from 1 to 10
arr = np.arange(1,11)
print(arr)

#Find all even numbers in the array
arr_even = arr[arr % 2 == 0]
print(arr_even)

#Create a boolean mask for values greater than 5 in the array
arr_mask = arr > 5
print(arr_mask)

#Replace all values greater than 5 with -1
arr[arr > 5] = -1
print(arr)