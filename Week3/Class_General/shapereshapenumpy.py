import numpy as np
arr1= np.array([[1,2,3],[4,5,6]])
print("Shaping Dimension " , arr1.ndim)
print("Shape",arr1.shape)

arr12=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr12)
print("Before reshaping ",arr12.ndim)
newarr= arr12.reshape(3,4)
print(newarr)
print("After reshaping ",newarr.ndim)