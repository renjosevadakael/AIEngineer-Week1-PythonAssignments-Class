"""  Assignment Details: 
  Create a Python script named matplotlib_test_results.py that: 
1. Stores the number of test cases executed in a release: 
o Passed = 45 
o Failed = 10 
o Skipped = 5 
2. Use Matplotlib to plot a bar chart showing these results. 
3. Add chart title: "Test Execution Results" 
4. Add axis labels: 
o X-axis → "Test Status" 
o Y-axis → "Number of Test Cases" 
5. Display the chart.. 
 Hints to Solve: 
 Use import matplotlib.pyplot as plt. 
 Use plt.bar(x, y) for bar chart. 
 Use plt.title(), plt.xlabel(), plt.ylabel(). """


import matplotlib.pyplot as plt
TestStatus=['Passed','Failed','Skipped']
NumTestCases=[45,10,5]

plt.bar(TestStatus, NumTestCases,width=0.5, align='center',color=['green','red','yellow'])
plt.title('Test Execution Results')
plt.xlabel('Test Status')
plt.ylabel('Number of Test Cases')

plt.show()


