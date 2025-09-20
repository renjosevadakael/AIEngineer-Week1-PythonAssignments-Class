""" Assignment Details:
  Create a Python script named pandas_series_defects.py that:
1.	Creates a Pandas Series for defects logged across 7 days:
2.	[5, 8, 3, 6, 10, 2, 7]
with labels: ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
3.	Prints the Series.
4.	Prints the maximum defects logged in a single day.
5.	Prints the day with minimum defects.
6.	Uses iloc to print defect count of Day5.
7.	Uses loc to print defect count on "Wed".
8.	Prints the total defects logged in the week.
 Hints to Solve:

•  Use .max(), .idxmin(), .sum().
•  Use .iloc[n] for numeric index, .loc['Wed'] for label. """
import pandas as pd

defects_logged_7days=pd.Series([5, 8, 3, 6, 10, 2, 7], index=[['Mon','Tue','Wed','Thu','Fri','Sat','Sun']])
print("defects_logged_7days ", defects_logged_7days)
print("maximum defects logged in a single day ", defects_logged_7days.max())
print("Prints the day with minimum defects ", defects_logged_7days.idxmin())
print("iloc to print defect count of Day5 ", defects_logged_7days.iloc[4])
print("loc to print defect count on 'Wed' ", defects_logged_7days.loc['Wed'])



