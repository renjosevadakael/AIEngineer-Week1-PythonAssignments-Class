# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load Dataset
data_dict = {
    'x1': [1, 2, 3],
    'x2': [2, 1, 4],
    'Output': [6, 8, 14]   # Dependent variable
}
data = pd.DataFrame(data_dict)

# 2. Define Features (X) and Target (y)
X = data[['x1', 'x2']]
y = data['Output']

# 3. Create and Fit the Model
model = LinearRegression()
model.fit(X, y)

# 4. Print Model Parameters
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# 5. Predictions
predictions = model.predict(X)
print("Predictions:", predictions)

# 6. Evaluation Metrics
mse = mean_squared_error(y, predictions)
r2 = r2_score(y, predictions)
print("Mean Squared Error:", mse)
print("R² Score:", r2)

# 7. Visualization (3D plot with regression plane)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter actual points
ax.scatter(data['x1'], data['x2'], data['Output'], color='red', label='Actual')

# Labels
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('Output')

# Meshgrid for regression plane ie for the prediction 
x1_range = np.linspace(min(data['x1']), max(data['x1']), 10)
x2_range = np.linspace(min(data['x2']), max(data['x2']), 10)
x1_mesh, x2_mesh = np.meshgrid(x1_range, x2_range)
output_mesh = model.intercept_ + model.coef_[0]*x1_mesh + model.coef_[1]*x2_mesh

# Plot regression plane
ax.plot_surface(x1_mesh, x2_mesh, output_mesh, alpha=0.5, color='blue',label='Regression Plane')
plt.legend()
plt.show()