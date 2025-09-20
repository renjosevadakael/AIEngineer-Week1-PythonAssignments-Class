""" Assignment Details:
     Create a Python script named pandas_series_times.py that:
1.	Creates a Pandas Series representing test execution times:
2.	[12, 15, 20, 18, 25, 30, 22]
with labels: ['TC1','TC2','TC3','TC4','TC5','TC6','TC7']
3.	Prints the Series.
4.	Displays the first 3 test times.
5.	Finds the mean execution time.
6.	Uses iloc to print the 2nd test time.
7.	Uses loc to print execution time of TC3
 Hints to Solve:

•  Use pd.Series([...], index=[...]).
•  Use .head(3), .mean().
•  Use .iloc[n] (index-based), .loc['label'] (label-based).

 """
import pandas as pd
test_execution_times=pd.Series([12, 15, 20, 18, 25, 30, 22],index=[['TC1','TC2','TC3','TC4','TC5','TC6','TC7']])
print("test_execution_times ", test_execution_times)
print("first 3 test times " ,test_execution_times.head(3))
print("mean execution time " , test_execution_times.mean())
print("iloc to print the 2nd test time", test_execution_times.iloc[1] )
print(f"Uses loc to print execution time of TC3 {test_execution_times.loc['TC3']}")
