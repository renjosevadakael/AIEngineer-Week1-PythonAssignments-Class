""" 3. Create series with the help of dictionary for
 the foll test cases executed by Engineers as key
Alex - 500
Steve - 200
Bob - 300 """

import pandas as pd

testExecution ={
'Alex' : 500,
'Steve' : 200,
'Bob' : 300
}

testExecution_PandasSeries = pd.Series(testExecution)

print(testExecution_PandasSeries)