""" Matrix Element-wise Operations
You are given two NumPy 2D arrays of the same shape. Your task is to perform the following element-wise operations and return the results in a tuple:
 """

import numpy as np


def matrixOperations(arr1,arr2):
    product_matrix= arr1 * arr2
    #print(product_matrix)
    sum_matrix= arr1 + arr2
   # print(sum_matrix)
    diff_matrix= arr1 - arr2
    #print(diff_matrix)
    return (sum_matrix,diff_matrix,product_matrix)




arr1= np.array([
    [1,2],
    [3,4]
]
)

arr2= np.array([
    [5,6],
    [7,8]
]
)

print("matrixOperations" , matrixOperations(arr1,arr2) )
