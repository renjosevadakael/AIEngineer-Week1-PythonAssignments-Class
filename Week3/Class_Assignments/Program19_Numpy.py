import numpy as np

""" 1. numpy array of elements 10,20,30,40,50,60. 
Create single dimensional array and slice [2:], [3:5],[-4], 
reverse array """

# One Dimensional Array
oneDArray = np.array([10,20,30,40,50,60])
print("Dimension of the array is ",oneDArray.ndim)
print("Slicing [2:] ",oneDArray[2:])
print("Slicing [3:5] ",oneDArray[3:5])
print("Slicing [-4] ",oneDArray[-4])

""" 2.  create 2 dim array with your own list and 
access samplearray[0][1], samplearray[1][1],samplearray[0][3]. 
Sum of all the 2 dimensional elements """
# Two Dimensional Array
samplearray = np.array([[10,20,30,40],[50,60,70,80]])
print("Dimension of the array is ",samplearray.ndim)
print("samplearray[0][1] ",samplearray[0][1])
print("samplearray[1][1] ",samplearray[1][1])
print("samplearray[0][3] ",samplearray[0][3])
""" sum=0
sum = np.sum(samplearray)
print("Sum of elements in the array is", sum) """

sum=0
for row in samplearray:
    print("row-->",row)
    for column in row:
        print("column-->",column)
        sum = sum+column
print("Sum of all elements", sum)

""" 3. Take a 3 dim array in name sample3dim. 
print[0][0][0],[0][1][2] , [1][1][2]. Use ndim and show the dimensions """

# Three Dimensional Array

sample3dim = np.array([[[10,20,30,40],[50,60,70,80]],[[90,100,110,120],[130,140,150,160]]])
print("Dimension of the array is ",sample3dim.ndim)
print("sample3dim[0][0][0] ",sample3dim[0][0][0])
print("sample3dim[0][1][2] ",sample3dim[0][1][2])
print("sample3dim[1][1][2] ",sample3dim[1][1][2])


