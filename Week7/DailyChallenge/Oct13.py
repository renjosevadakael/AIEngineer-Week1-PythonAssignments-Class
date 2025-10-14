""" NumPy Array Filtering """
import numpy as np

def filterGreaterThanMean(arr):
    mean = np.mean(arr)
    print(mean)
    mask = arr > mean
    print (mask)
    filteredarray= arr[mask]
    return filteredarray

arr = np.array([10,20,30,40,50])
print(filterGreaterThanMean(arr))