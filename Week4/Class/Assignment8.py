"""  Assignment Details: 
  Create a Python script named pandas_dataframe_grouping.py that: 
1. Creates a DataFrame: 
TestCase Module Status Duration 
TC1 Login Passed 12 
TC2 Login Failed 15 
TC3 Payment Passed 20 
TC4 Payment Failed 18 
TC5 Reports Passed 25 
TC6 Reports Passed 22 
2. Groups by Status and counts Passed vs Failed. 
3. Groups by Module and finds average Duration per module. 
 Hints to Solve: 
  Use .groupby("Status")["TestCase"].count(). 
  Use .groupby("Module")["Duration"].mean().  """

import numpy as np
import pandas as pd
#Dictionary with series - Data Framme

data = {
    'TestCase': ['TC1', 'TC2', 'TC3', 'TC4', 'TC5', 'TC6'],
    'Module': ['Login', 'Login', 'Payment', 'Payment', 'Reports', 'Reports'],
    'Status': ['Passed', 'Failed', 'Passed', 'Failed', 'Passed', 'Passed'],
    'Duration': [12, 15, 20, 18, 25, 22]
} 

# Convert to DataFrame with Dictionary of List
df = pd.DataFrame(data)
print(df)
print("Groups by Status and counts Passed vs Failed", df.groupby("Status")["TestCase"].count())
print("Groups by Module and finds average Duration per module", df.groupby("Module")["Duration"].mean())




data = {
    'TestCase': pd.Series(['TC1', 'TC2', 'TC3', 'TC4', 'TC5', 'TC6']),
    'Module': pd.Series(['Login', 'Login', 'Payment', 'Payment', 'Reports', 'Reports']),
    'Status': pd.Series(['Passed', 'Failed', 'Passed', 'Failed', 'Passed', 'Passed']),
    'Duration': pd.Series([12, 15, 20, 18, 25, 22])
}


# Convert to DataFrame with Dictionary of Seies
df = pd.DataFrame(data)
print(df)
print("Groups by Status and counts Passed vs Failed", df.groupby("Status")["TestCase"].count())
print("Groups by Module and finds average Duration per module", df.groupby("Module")["Duration"].mean())





