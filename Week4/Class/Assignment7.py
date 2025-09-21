""" array 1 = [10,20,30] array 2 = [30,40,50] using numpy arrays

series1 = [100,200,300] series 2 = [400,500] using series

3. Dictionary with series - Mani : [10,20,30], Alex : [20,30] """

import numpy as np
import pandas as pd

#Array Value - Data Framme
array1= np.array([10,20,30])
array2= np.array([30,40,50])
dframe = pd.DataFrame([array1,array2],columns=['A','B','C'])
print(dframe)

#Series Value - Data Framme

series1= pd.Series([100,200,300],index=['a','b','c'])
series2= pd.Series([400,500],index=['a','b'])
dframe = pd.DataFrame({

    'Series1' :series1,
    'Series2' :series2,
})
print(dframe)

#Dictionary with series - Data Framme

data = {
    'Mani': pd.Series([10, 20, 30]),
    'Alex': pd.Series([20, 30])
}

# Convert to DataFrame
df = pd.DataFrame(data)

print(df)
