""" 
 Assignment Details: 
  Create a Python script named pandas_dataframe_tests.py that: 
1. Creates a DataFrame with the following data: 
TestCase Status Duration 
TC1 Passed 12 
TC2 Failed 15 
TC3 Passed 20 
TC4 Failed 18 
TC5 Passed 25 
2. Prints the DataFrame. 
3. Selects and prints only the Status column. 
4. Filters and prints only Failed test cases. 
5. Saves the DataFrame as test_results.csv. 
6. Reads back the CSV into a new DataFrame. 
Hints to Solve: 
  Use pd.DataFrame({}). 
  Use .to_csv("file.csv", index=False) and pd.read_csv("file.csv"). 
  Use .fillna(df['Duration'].mean()).  """



import numpy as np
import pandas as pd

data = {
    'TestCase': ['TC1', 'TC2', 'TC3', 'TC4', 'TC5'],
     'Status': ['Passed', 'Failed', 'Passed', 'Failed', 'Passed'],
    'Duration': [12, 15, 20, 18, 25]
} 
df = pd.DataFrame(data)

print(" Prints the DataFrame", df)
print("Selects and prints only the Status column ::", df['Status'])
print("Filters and prints only Failed test cases ::", df[df['Status']=="Failed"])

df.to_csv('test_results.csv', index=False)
print("Saves the DataFrame as test_results.csv")

new_df = pd.read_csv('test_results.csv')
print("Reads back the CSV into a new DataFrame\n",new_df)

df = pd.read_csv("test_results.csv", usecols=['TestCase', 'Status'])  # Selective column read
print(df[df['TestCase'] == 'TC1'])  # Row filter by value




