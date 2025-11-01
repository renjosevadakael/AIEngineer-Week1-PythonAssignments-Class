""" Assignment Details: 
1. You are provided with a dataset named Student_Performance.csv. 
The dataset contains multiple features (such as hours studied, sleep hours, attendance, 
etc.) and a target column Performance Index. 
2. Your task is to build a Multiple Linear Regression model to predict Performance 
Index. 
o Steps to Perform: 
1. Import Required Libraries 
2. Create a Class StudentPerformanceModel 
3. Data Preprocessing 
4. Train-Test Split 
5. Model Training 
6. Model Evaluation 
7. User Input Prediction - After evaluating the model, allow the user to enter values for all 
independent variables (for example: study hours, sleep hours, attendance 
%). - Convert the input values into a 2-D array and use the trained model to 
predict the Performance Index. - Display the predicted result clearly. 
8. Visualization  """

#Step 1 - Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score


# Step 2 - Import the data set

data_set= pd.read_csv("Week9-ML-MultipleLinearRegression\\Home\\Student_Performance.csv")

# Step 3 - Define Features and Target
X=data_set.drop(columns="Performance Index")
Y=data_set["Performance Index"]

# Step 4 - Split the data
X_encoded = pd.get_dummies(X, drop_first=True)
print(X_encoded)


X_train, X_test, Y_train, Y_test= train_test_split(X_encoded,Y,test_size=0.2,random_state=10)


#Step 5- Fit
model = LinearRegression()
model.fit(X_train,Y_train)

# Step 6- View the Model Parameters
print("--- Model Coefficients ---")
print(f"Intercept (β0): {model.intercept_:.1f}")
print(f"Coefficients (β1, β2): {model.coef_}")
#print(f"Model Equation: y = {model.intercept_:.1f} + {model.coef_[0]:.1f}*x1 + {model.coef_[1]:.1f}*x2\n")
print("--- Model Coefficients ---")
print(f"Intercept (β₀): {model.intercept_:.2f}")

# Generate equation using a basic for loop
equation = f"y = {model.intercept_:.2f}"
for i in range(len(model.coef_)):
    equation += f" + {model.coef_[i]:.2f}*{X_encoded.columns[i]}"

print("Model Equation:")
print(equation)

#Step 7 - Predict 
Y_predict= model.predict(X_test)

# Step 8 - MSE , R2 - Evaluate Model

mse= mean_squared_error(Y_test,Y_predict)
rmse=np.sqrt(mse)
r2=r2_score(Y_test,Y_predict)
print("Model Evaluation")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R² Score: {r2:.2f}")


# Step 10 - Predict New Values 
##  A ---- Hard Coded
# Replace these with actual input values in the correct order
new_values = [[7, 99, 9, 1, 1]]  # Example: [Hours Studied, Previous Scores, Sleep Hours,Sample Papers,Extracurricular]

# Create DataFrame with same column structure as X_encoded
new_data = pd.DataFrame(new_values, columns=X_encoded.columns)

# Make prediction
new_prediction = model.predict(new_data)[0]

# Display result with RMSE as uncertainty margin
print("\n--- New Prediction ---")
print(f"Input: {new_data.values.tolist()[0]}")
print(f"Predicted Performance Index: {new_prediction:.2f} ± {rmse:.2f}")

#  User Input Prediction
""" 
#  B --- Prompt user for input values
hours_studied = float(input("Enter hours studied: "))
previous_scores = float(input("Enter previous scores (out of 100): "))
sleep_hours = float(input("Enter average sleep hours: "))
sample_papers = int(input("Enter number of sample question papers practiced: "))
extracurricular = input("Participated in extracurricular activities? (Yes/No): ")

# Encode categorical input
extracurricular_encoded = 1 if extracurricular.lower() == "yes" else 0

# Create input array in correct order
user_input = [[hours_studied, previous_scores, sleep_hours, sample_papers, extracurricular_encoded]]

# Convert to DataFrame with same column names as training data
user_df = pd.DataFrame(user_input, columns=X_encoded.columns)

# Predict using trained model
predicted_index = model.predict(user_df)[0]

# Display result with RMSE margin
print("\n--- Predicted Performance Index ---")
print(f"Input: {user_df.values.tolist()[0]}")
print(f"Predicted Performance Index: {predicted_index:.2f} ± {rmse:.2f}") """


# Scatter Plot
# Choose one feature for x-axis
x_feature = 'Hours Studied'

# Sort values for smoother line plot
sorted_idx = X_test[x_feature].argsort()
x_sorted = X_test[x_feature].iloc[sorted_idx]
y_actual_sorted = Y_test.iloc[sorted_idx]
y_pred_sorted = Y_predict[sorted_idx]

# Plot actual data points
plt.scatter(x_sorted, y_actual_sorted, color='green', label='Actual Performance Index')

# Plot predicted line
plt.plot(x_sorted, y_pred_sorted, color='blue', label='Predicted Performance Index')

# Labels and title
plt.xlabel(x_feature)
plt.ylabel('Performance Index')
plt.title('Actual vs Predicted Performance Index')
plt.legend()
plt.tight_layout()
plt.show()


# Predicted vs Actual Performance Index
plt.scatter(Y_test, Y_predict, color='purple', alpha=0.6)
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], color='black', linestyle='--', label='Perfect Prediction')

plt.xlabel('Actual Performance Index')
plt.ylabel('Predicted Performance Index')
plt.title('Model Accuracy: Actual vs Predicted')
plt.legend()
plt.tight_layout()
plt.show()




 

