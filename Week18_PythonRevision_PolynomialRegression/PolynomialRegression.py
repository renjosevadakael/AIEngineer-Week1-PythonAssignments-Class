import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score


# Sample data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
print(X)
y = np.array([1, 4, 9, 16, 25])  

# Transform 
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)
print(X_poly)

# Fit 
model = LinearRegression()
model.fit(X_poly, y)

# Print coefficients
print("=== Model Coefficients ===")
print(f"Intercept (a0): {model.intercept_:.2f}")
print(f"Coefficients (a1, a2): {model.coef_[1]:.2f}, {model.coef_[2]:.2f}")


# Predict
y_pred = model.predict(X_poly)

# Calculate metrics
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print("=== Model Evaluation ===")
print(f"MSE: {mse:.2f}")
print(f"R²: {r2:.4f}")



# Plotting
plt.scatter(X, y, color='red', label='Original')
plt.plot(X, y_pred, color='blue', label='Polynomial ')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polynomial Regression Eg')
plt.legend()
plt.grid(True)
plt.show()

# Interactive prediction section
print("\n=== Interactive Predictions ===")
print("Enter X values to get predictions (type 'done' to finish)")

user_predictions = []
user_x_values = []


while True:
    user_input = input("\nEnter X value (or 'done' to finish): ")
    
    if user_input.lower() in ['done', 'quit', 'exit']:
        break
    
    try:
        # Convert input to float
        x_new = float(user_input)
        
        # Make prediction (reshape to 2D array and transform)
        x_input = np.array([[x_new]])
        x_input_poly = poly.transform(x_input)  # Transform to polynomial features
        prediction = model.predict(x_input_poly)
        
        print(f"For X = {x_new}: Predicted y = {prediction[0]:.2f}")
        
        # Store for visualization
        user_x_values.append(x_new)
        user_predictions.append(prediction)
        
    except ValueError:
        print("Please enter a valid number or 'done' to finish.")