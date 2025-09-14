""" Assignment Details:
  Create a Python script named numpy_array_basics.py that demonstrates the following:
1.	Creating
o	Create a 1D NumPy array with execution times of 8 test cases:
o	[10, 15, 20, 25, 30, 35, 40, 45]
2.	Indexing & Shaping
o	Access the first, last, and 3rd element of the array.
o	Print the shape of the array.
3.	Slicing
o	Print execution times of the first 3 tests.
o	Print every alternate test time.
4.	Iteration
o	Iterate through the array and print each execution time with a message:
"Test X execution time: Y seconds".
5.	Reshaping
o	Reshape the 1D array (8 elements) into a 2D array of shape (2,4).
o	Print the reshaped array.
6.	Joining
o	Create another NumPy array with 4 more execution times:
o	[50, 55, 60, 65]
o	Join (concatenate) this with the first array to form a longer array.
7.	Splitting
o	Split the final array into 3 smaller arrays (equal parts if possible).
o	Print each split.
 Requirements:

•  Use numpy.array() to create arrays.
•  Use indexing (arr[0], arr[-1]) for access.
•  Use slicing (arr[0:3], arr[::2]) for subsets.
•  Use .shape, .reshape(), np.concatenate(), and np.array_split().

 Hints to Solve:

•  Reshaping requires compatible dimensions (8 elements → (2,4) works).


•  np.concatenate([arr1, arr2]) merges arrays.
•  np.array_split(arr, 3) splits into 3 parts.
 """

import numpy as np

executionTime=np.array([10, 15, 20, 25, 30, 35, 40, 45])
print("Array is ",executionTime)
#Access the first, last, and 3rd element of the array.
print("First Element is ", executionTime[0], " Last Element is " ,executionTime[-1] , "Third Element is ",executionTime[2] )
print("Shape of Array is ", executionTime.shape)

#Slicing
#Print execution times of the first 3 tests.
#Print every alternate test time.

print("Execution times of the first 3 tests is ",executionTime[0:3])
print("Print every alternate test time ",executionTime[0:8:2])

#4.	Iteration
#Iterate through the array and print each execution time with a message:
#"Test X execution time: Y seconds".

#5.	Reshaping
#Reshape the 1D array (8 elements) into a 2D array of shape (2,4).
#Print the reshaped array.
reshapedArray= executionTime.reshape(2,4)
print("Reshaped array is ",reshapedArray)

#6.	Joining
#Create another NumPy array with 4 more execution times:
##[50, 55, 60, 65]
#Join (concatenate) this with the first array to form a longer array.
executionTime2=np.array([50, 55, 60, 65])
combinedArray= np.concatenate((executionTime,executionTime2))
print("combinedArray after concatenation", combinedArray)

#7.	Splitting
#Split the final array into 3 smaller arrays (equal parts if possible).
#Print each split.


splits = np.split(combinedArray, 3)
print(splits)




