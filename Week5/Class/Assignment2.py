"""  Assignment Details: 
  Create a Python script named matplotlib_defect_trends.py that: 
1. Stores the number of defects logged each week in a project: 
2. Weeks = [1, 2, 3, 4, 5, 6]   
3. Defects = [5, 8, 6, 10, 7, 4] 
4. Plot a line chart with Weeks on the X-axis and Defects on the Y-axis. 
5. Add chart title: "Defect Trend Over Time" 
6. Add axis labels: 
a. X-axis → "Week Number" 
b. Y-axis → "Number of Defects" 
7. Add markers on the line to highlight each data point. 
8. Display the chart. 
 Hints to Solve: 
  Use plt.plot(x, y, marker='o'). 
  Use plt.grid(True) to show a grid. 
  Use plt.show() to display. """


import matplotlib.pyplot as plt
Weeks = [1, 2, 3, 4, 5, 6] 
Defects = [5, 8, 6, 10, 7, 4] 

plt.plot(Weeks, Defects, marker='o',linestyle='dotted', color='r')
plt.title('Defect Trend Over Time')
plt.xlabel('Week Number')
plt.ylabel('Number of Defects')
plt.legend(loc='upper center', ncol=1, shadow=True, fontsize='large')
plt.grid(True)
plt.savefig('Chart.png')
plt.show()

