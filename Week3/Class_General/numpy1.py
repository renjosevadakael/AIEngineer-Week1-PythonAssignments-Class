import numpy as np
oneDArray = np.array([1,2,3,4,5])
twoDArray = np.array([[1,2,3],[4,5,6]])
threeDArray = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(oneDArray)


a=9
print(type(a))
b='renju'
print(type(b))
print(oneDArray)
print(type(oneDArray))
print(oneDArray.ndim)

print(twoDArray)
print(type(twoDArray))
print(twoDArray.ndim)
print(threeDArray)
print(type(threeDArray))
print(threeDArray.ndim)
print(threeDArray[1,0,1])
print(threeDArray[1,1,2])