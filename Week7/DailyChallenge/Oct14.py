"""Transpose 2D Array and Flatten it"""

import numpy as np

def transpose_and_flatten(arr):
    transposed = arr.T
    flattened = arr.flatten()
    return (transposed,flattened)

arr = np.array([[1,2,3],[4,5,6]])
output_tuple= transpose_and_flatten(arr)
print("Original Array", arr)
print("Transposed Array", output_tuple[0])
print("Flattened Array", output_tuple[1])