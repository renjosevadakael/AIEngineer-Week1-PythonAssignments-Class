""" For the give data set using IQR technique  
a) find out the outliers and write it to CSV 
b) write the cleaned data to CSV by excludig the outliers """

import pandas as pd


df = pd.read_csv("C:\AIEngineer\Class1_Python\Week6\Class\SalesDataSet_updated.csv")
Q1= df['Total Amount'].quantile(0.25)

Q3= df['Total Amount'].quantile(0.75)
IQR = Q3 - Q1

lower_outlier = Q1 - 1.5 * IQR
print("lower_outlier" ,lower_outlier)
upper_outlier = Q3 + 1.5 * IQR
print("upper_outlier" ,upper_outlier)
# Extract outliers

outliers = df[( df['Total Amount'] < lower_outlier ) | (df['Total Amount'] > upper_outlier )]
print(outliers)
outliers.to_csv('C:\AIEngineer\Class1_Python\Week6\Class\SalesDataSet_outliers.csv')

#Exclude outliers
exclude_outliers= df[( df['Total Amount'] >= lower_outlier ) & (df['Total Amount'] <=upper_outlier )]
print(exclude_outliers)
exclude_outliers.to_csv('C:\AIEngineer\Class1_Python\Week6\Class\SalesDataSet_excludeoutliers.csv')


