'''Matrix reshaping'''
import numpy as np

def reshapeMatrix(arr, rows,cols):
    size= np.size(arr)
    if(rows*cols != size):
        print("Reshape not possible!")
    else:
        reshapedArray= arr.reshape(rows, cols)
        print(reshapedArray)

    
arr=np.array([1,2,3,4,5,6])
reshapeMatrix(arr,2,3)
reshapeMatrix(arr,3,2)
reshapeMatrix(arr,4,2)