# Exercise 2: Array Indexing and Slicing
# 1. Extract the elements from index 2 to 6 from a 1D array: arr = np.arange(10).
# 2. Given arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]].
# • Extract the second row from a 3x3 array.
# • Replace the last column of arr2d with 0.
import numpy as np

arr = np.arange(10)
#Extract the elements from index 2 to 6 from a 1D array
arr_ex = arr[2:6]
print(arr_ex)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#Extract the second row from a 3x3 array
arr2d_ex = arr2d[1, :]
print(arr2d_ex)

#Replace the last column of arr2d with 0
arr2d[:,-1] = 0
print(arr2d)