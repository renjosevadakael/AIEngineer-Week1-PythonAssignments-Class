import pandas as pd 
import numpy as np
data = { 'Name': ['Alice','Bob','Charlie'], 'Age':[25,30,35] } 
df = pd.DataFrame(data) 
print('✅ pandas is working!') 
print(df)
""" Series - like an array - 1 D array
DataFrame - 2 D - like table format
Panel - MultiDimensional used in Image processing / Video ( this is deprecated)

Extended DataFrame, XArray are used now instead of Panel

"""

a=[1,7,20]
series= pd.Series(a)
print(series)


b= pd.Series([2,3,4],index=['name','age','id'])
print(b)

c= pd.Series([1,2,3,4,5,6,7,8,9], index=[10,20,30,40,50,60,70,80,90])
print(c.loc[30:50]) # custom index
print(c.iloc[1:4]) # base index

emp_exper={

    'renju' :10,
    'anu' :9,
    'joel' :8
}

emp_series = pd.Series(emp_exper)
print(emp_series)
print(emp_series['renju'])

print("head(1)", emp_series.head(1))
print("head(-1)", emp_series.head(-1))
print("tail(-1)",emp_series.tail(-1))
print("tail(1)",emp_series.tail(1))

print("info()------",emp_series.info())
print("describe()------",emp_series.describe())


