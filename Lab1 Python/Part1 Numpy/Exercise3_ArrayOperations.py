# Exercise 3: Array Operations
# 1. Find the sum of all elements in this 2D array:
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).
# 2. Find the maximum value in each row of the array.
# 3. Compute the mean of all elements.
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#Sum all elements
arr_sum = np.sum(arr)
#Sum each row
arr_sum_row = np.sum(arr, axis=1)
#Sum each column
arr_sum_col = np.sum(arr, axis=0)
print(arr_sum, arr_sum_row, arr_sum_col)

#Find the maximum value in each row
arrmax = arr.max(axis=1)
print(arrmax)

#Compute the mean of all elements
arr_mean = np.mean(arr)
#Compute the mean of each row
arr_mean_row = np.mean(arr, axis=1)
#Compute the mean of each column
arr_mean_col = np.mean(arr, axis=0)
print(arr_mean, arr_mean_row, arr_mean_col)