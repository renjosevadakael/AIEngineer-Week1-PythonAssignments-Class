import numpy as np

def process_matrix(arr):
    row_sums=np.sum(arr,axis=1)
    col_max =np.max(arr,axis=0)
    return (row_sums,col_max)

arr = np.array([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ])
print("Array is \n" , arr)
print("row_sums , col_max" , process_matrix(arr))