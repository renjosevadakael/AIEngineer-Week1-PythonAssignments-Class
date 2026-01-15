import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  
y = np.array([2, 4, 5, 4, 5])                

# Create training 
model = LinearRegression()
model.fit(X, y)

print("=== Model Parameters ===")
print(f"Slope: {model.coef_[0]:.2f}")      # ← Part of model.fit()
print(f"Intercept: {model.intercept_:.2f}") # ← Part of model.fit()

predictions = model.predict(X)

print("\n=== Model Evaluation ===")
print(f"MSE: {mean_squared_error(y, predictions):.2f}")    # ← Uses predict output
print(f"R²: {r2_score(y, predictions):.4f}")              # ← Uses predict output


print("Predictions:", predictions)

# Step 5: Visualize the regression line
plt.scatter(X, y, color="blue", label="Actual data")
plt.plot(X, predictions, color="red", label=" Predictions")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
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
        
        # Make prediction (reshape to 2D array)
        x_input = np.array([[x_new]])
        prediction = model.predict(x_input)[0]
        
        print(f"For X = {x_new}: Predicted y = {prediction:.2f}")
        
        # Store for visualization
        user_x_values.append(x_new)
        user_predictions.append(prediction)
        
    except ValueError:
        print("Please enter a valid number or 'done' to finish.")