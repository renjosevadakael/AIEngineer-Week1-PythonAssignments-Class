"""  Assignment Details: 
1. Create a CSV file named test_results_missing.csv with missing values: 
TestCase Module Status Duration Defects 
TC1 Login Passed 12 0 
TC2 Login Failed NaN 2 
TC3 Payment Passed 20 NaN 
TC4 Payment Failed 18 3 
TC5 Reports NaN 25 0 
2. Write a Python script pandas_missing_data.py that: 
o Reads the CSV into a DataFrame. 
o Use .isnull().sum() to count missing values in each column. 
o Use .fillna(value) to: 
 Replace missing Duration with the mean duration. 
 Replace missing Status with "Unknown". 
o Use .dropna() to drop any row that still contains missing values. 
o Print the cleaned DataFrame. 
Hints to Solve: 
  Use pd.read_csv("test_results_missing.csv"). 
  Use .fillna(df['Duration'].mean()). 
  Use .dropna(inplace=True) to remove rows.
 """


import pandas as pd
import numpy as np

data = {
    "TestCase": ["TC1", "TC2", "TC3", "TC4", "TC5"],
    "Module": ["Login", "Login", "Payment", "Payment", "Reports"],
    "Status": ["Passed", "Failed", "Passed", "Failed", np.nan],
    "Duration": [12, np.nan, 20, 18, 25],
    "Defects": [0, 2, np.nan, 3, 0]
}

# Create the DataFrame
df = pd.DataFrame(data)
print(df)
df_columns=['TestCase' , 'Module', 'Status','Duration','Defects']
print(df[df_columns].isnull().sum())

df_mean= df['Duration'].fillna(df['Duration'].mean())
print(df_mean)

df["Status"] = df["Status"].fillna("Unknown")
print(df)
df.dropna(inplace=True)
print(df)





