import numpy as np

def unique(arr):
    unique_arr=np.unique(arr)
    return np.sort(unique_arr)
            
   

arr = np.array([1,2,6,4,3,2,8,1,9])
print("Original Array is \n" , arr)
print("Unique Sorted Array ", unique(arr))