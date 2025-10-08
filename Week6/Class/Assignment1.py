""" Assignment Details: 
 
Dataset Provided 
File Name: SalesDataSet.csv 
 Create a Python script named sales_dataset_analysis.py that reads the CSV and answers the 
following questions. 
1. What is the 25th percentile of the Total Amount? 
2. What is the median (50th percentile) of the Total Amount? 
3. What is the 75th percentile of the Total Amount? 
4. What is the variance in Total Amount across all transactions? 
5. What is the variance in Quantity sold? 
6. What is the correlation between Age and Total Amount? 
7. What is the correlation between Quantity and Total Amount? 
8. What is the correlation between Price per Unit and Total Amount? 
 Hints to Solve: 
  Import Libraries 
  Load Dataset. 
  Perform Analysis: Apply the functions mentioned above. 
  Display Results: Print each result clearly with labels.  """

import pandas as pd


df = pd.read_csv("C:\AIEngineer\Class1_Python\Week6\Class\SalesDataSet.csv")
print("1. 25th percentile of the Total Amount", df['Total Amount'].quantile(0.25))
print("2. median (50th percentile) of the Total Amount", df['Total Amount'].quantile(0.50))
print("2. median (50th percentile) of the Total Amount", df['Total Amount'].median())
print("3. 75th percentile of the Total Amount", df['Total Amount'].quantile(0.75))
variance = df['Total Amount'].var()
print("4. Variance in Total Amount:", variance)
variance_quantity = df['Quantity'].var()
print("5. Variance in Quantity sold:", variance_quantity)
correlation = df['Age'].corr(df['Total Amount'])
print("6. Correlation between Age and Total Amount:", correlation)
correlation = df['Quantity'].corr(df['Total Amount'])
print("7. Correlation between Quantity and Total Amount:\n", correlation)
correlation = df[['Quantity', 'Total Amount']].corr()
print("7. Correlation between Quantity and Total Amount:", correlation)
correlation = df['Price per Unit'].corr(df['Total Amount'])
print("8. Correlation between Price per Unit and Total Amount:", correlation)




