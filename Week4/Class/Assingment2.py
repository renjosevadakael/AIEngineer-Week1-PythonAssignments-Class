""" 2. Create with numpy array of number of defects [10,20,23,45,50]
 convert to series """

import numpy as np
import pandas as pd
defectArray = np.array([10,20,23,45,50])
defectArray_PandasSeries= pd.Series(defectArray)
print (defectArray_PandasSeries)
