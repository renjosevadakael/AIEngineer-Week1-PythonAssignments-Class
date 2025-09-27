"""  Create a Python script named matplotlib_test_histogram.py that: 
1. Store execution times of 12 test cases: 
2. [12, 15, 20, 18, 22, 30, 25, 16, 19, 28, 24, 14] 
3. Plot a histogram with bins=5. 
4. Add chart title: "Distribution of Test Execution Times". 
5. Add axis labels: 
o X-axis = "Duration (seconds)" 
o Y-axis = "Number of Test Cases" 
 Hints to Solve: 
  Use plt.hist(values, bins=5, color='skyblue', edgecolor='black'). 
  More bins = more detailed distribution. """

import matplotlib.pyplot as plt

execution_times= [12, 15, 20, 18, 22, 30, 25, 16, 19, 28, 24, 14] 
plt.xlabel='Duration (seconds)'
plt.ylabel='Number of Test Cases'

plt.hist(execution_times, bins=5, color='skyblue', edgecolor='black')

plt.show()