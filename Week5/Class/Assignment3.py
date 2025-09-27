""" Create a Python script named matplotlib_defect_pie.py that: 
1. Stores defect counts by severity: 
      High = 10, Medium = 15, Low = 5 
2. Create a pie chart showing this distribution. 
3. Add labels: ["High", "Medium", "Low"]. 
4. Add a title: "Defect Distribution by Severity". 
5. Display percentages in the chart using autopct. 
 Hints to Solve: 
  Use plt.pie(values, labels=labels, autopct='%1.1f%%'). 
  Use plt.title("..."). """


import matplotlib.pyplot as plt
values=[10,15,5]
labels=["High", "Medium", "Low"]
plt.title='Defect Distribution by Severity'
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.show()



