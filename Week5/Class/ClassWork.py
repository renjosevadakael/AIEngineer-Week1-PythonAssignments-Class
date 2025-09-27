""" import matplotlib
import matplotlib.pyplot as plt """

""" print(matplotlib.__version__)  # Correct way to print the version

x = [10, 20]
y = [10, 20]

plt.plot(x, y)
plt.show()
 """
import numpy as np
import matplotlib.pyplot as plt

# Data for line plot
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])

plt.plot(x, y, marker='o')  # Optional: add markers to highlight points
plt.grid(True)              # Show grid for better readability
plt.show()                  # Display the plot


x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
z = np.array([1, 3, 5, 7, 9])
w = np.array([3, 6, 9, 12, 15])
plt.plot(x, y, marker='o', linestyle='dotted', color='r', label='Data Points 1')
plt.plot(z, w, marker='s', linestyle='dotted', color='b', label='Data Points 2')
plt.title("Line Plot (with Markers)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(loc='upper center', ncol=2, shadow=True, fontsize='large')
plt.grid(True)
plt.show()

# Define data
cohort = ['Cohort1', 'Cohort2', 'Cohort3', 'Cohort4']
values = [30, 40, 30, 45]

# Create the bar chart
plt.bar(cohort, values, color='skyblue', width=0.5, align='edge')

# Add labels and title
plt.xlabel('Cohort')
plt.ylabel('Problems Solved')
plt.title('Cohort Problem Solution Status')

# Display the plot
plt.show()

# Define categories and data
categories = ['Ford', 'Honda', 'Hyundai']
data1 = np.array([20, 30, 40])
data2 = np.array([30, 20, 10])

# Create stacked bar chart
plt.bar(categories, data1, label='Series 1', width=0.5)
plt.bar(categories, data2, bottom=data1, label='Series 2', width=0.5)

# Add labels and title
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Stacked Bar Chart')
plt.legend()

# Display the plot
plt.show()




