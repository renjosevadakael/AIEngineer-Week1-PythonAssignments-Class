"""
Robust Scalar and MinMax scalar

"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import MinMaxScaler

data = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10]  
]

df = pd.DataFrame(data)
#df1 = pd.DataFrame(data, columns=['First', 'Second'])

# Calculate Q1 
q1_first = df[0].quantile(0.25)
#q1_first = df1['First'].quantile(0.25)
q1_second = df[1].quantile(0.25)

print("Q1 for first column:", q1_first)
print("Q1 for sec column:", q1_second)

# Calculate Q3 
q1_first = df[0].quantile(0.75)
q1_second = df[1].quantile(0.75)

print("Q3 for first column:", q1_first)
print("Q3 for sec column:", q1_second)

# Robust Scaler

scaler = RobustScaler()
scaled_data = scaler.fit_transform(data)
print("Original Data", data )
print("RobustScaler Data",scaled_data)


# Min Max Scaler

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)
print("Original Data", data )
print("MinMaxScaler Data",scaled_data)

