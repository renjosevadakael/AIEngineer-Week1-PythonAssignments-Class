""" Assignment Details:
  Create a Python script named pandas_series_passrate.py that:
1.	Creates a Series for test pass percentage across 5 builds:
2.	[80, 85, 78, 90, 88]
with labels: ['B1','B2','B3','B4','B5']
3.	Prints the Series.
4.	Calculates and prints the average pass rate.
5.	Finds which build had the highest pass rate.
6.	Uses iloc to print pass rate of the last build.
7.	Uses loc to print pass rate of Build B3.
8.	Normalizes values by subtracting average from each pass rate.
  Hints to Solve:
•  Use .mean(), .idxmax().
•  Use .iloc[-1], .loc['B3'].
•  Use series - series.mean().
 """
import pandas as pd
test_pass_percentage_5days=pd.Series([80, 85, 78, 90, 88], index=['B1','B2','B3','B4','B5'])
print(test_pass_percentage_5days)
average_pass_rate = test_pass_percentage_5days.mean()

print("the average pass rate",average_pass_rate )
print("the highest pass rate",test_pass_percentage_5days.idxmax() )
print("iloc to print pass rate of the last build",test_pass_percentage_5days.iloc[-1] )
print("loc to print pass rate of Build B3",test_pass_percentage_5days.loc['B3'] )

normalized_pass_rates = test_pass_percentage_5days - average_pass_rate
print("\nNormalized Pass Rates (Deviation from Average):")
print(normalized_pass_rates)


