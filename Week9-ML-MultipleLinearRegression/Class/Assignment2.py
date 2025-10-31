import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from mpl_toolkits.mplot3d import Axes3D 

# Load Data Set
data_set = pd.read_csv("C:\\AIEngineer\\Class1_Python\\Week9-ML-MultipleLinearRegression\\Class\\salary.csv")
# Feature and Label Setting
X=data_set[['YearsExperience','Rating']]
Y= data_set['Salary']

# Train Test Split
X_train, X_test, Y_train, Y_test= train_test_split(X,Y,test_size=0.2,random_state=11)

# Model Training
model= LinearRegression()
model.fit(X_train,Y_train)

# Coeff and Intercepts
#print("B1 and B2" , model.coef_)
#print(model.intercept_)

print(f"B1 (YearsExperience): {model.coef_[0]:.1f}")
print(f"B2 (Rating): {model.coef_[1]:.1f}")
print(f"Intercept (B0): {model.intercept_:.1f}")

# Model Equation
print("Y = B0 +B1X1 + B2X2")
print(f"Y = {model.intercept_:.1f} + {model.coef_[0]:.1f} * YearsExperience + {model.coef_[1]:.1f} * Rating")

#Make predictions
Y_pred = model.predict(X_test)

# Evaluate model performance
print("\nModel Evaluation:")
print(f"Mean Squared Error (MSE): {mean_squared_error(Y_test, Y_pred): .2f}")
print(f"Root Mean Squared Error (RMSE): {mean_squared_error(Y_test, Y_pred)**0.5: .2f}")
print(f"R² Score: {r2_score(Y_test, Y_pred): .2f}")




# Single prediction input
new_data = pd.DataFrame([[4.7, 3]], columns=['YearsExperience', 'Rating'])

# Predict salary
predicted_salary = model.predict(new_data)

# Single prediction input
new_data = pd.DataFrame([[4.7, 3]], columns=['YearsExperience', 'Rating'])
predicted_salary = model.predict(new_data)[0]
rmse = mean_squared_error(Y_test, Y_pred)**0.5

print(f"\nPredicted Salary for 4.7 years experience and 3 rating: ₹{predicted_salary:.2f} ± ₹{rmse:.2f}")

