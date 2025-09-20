""" create series - scalar - 
1.     Creates a Pandas Series representing test execution times: 
2.  [12, 15, 20, 18, 25, 30, 22]
slice the midle three execution times
 """
import pandas as pd

scalarArray= [12, 15, 20, 18, 25, 30, 22]

pandasSeries= pd.Series(scalarArray)


print(pandasSeries)

length= len(scalarArray)


print("slice the middle three execution times" ,pandasSeries[2:5])