""" Assignment Details: 
1. Load the Dataset 
o Load the provided dataset using Pandas. 
o Retain only the columns Square Footage and Price for model building. 
2. Exploratory Data Analysis (EDA) 
o Display the first few rows of the dataset. 
o Check for missing or null values and handle them appropriately. 
o Visualize the relationship between Square Footage and Price using a scatter 
plot. 
3. Feature and Target Selection 
o Assign Square Footage as the independent variable (X). 
o Assign Price as the dependent variable (Y). 
4. Train-Test Split 
o Split the dataset into training and testing sets using an 80-20 ratio. 
5. Model Building 
o Create a Linear Regression model using LinearRegression from 
sklearn.linear_model. 
o Fit the model on the training data. 
o Display the intercept (b₀) and coefficient (b₁) of the regression line. 
6. Prediction and Evaluation 
o Predict the house prices for the test set. 
o Calculate and print the following evaluation metrics: 
 Mean Squared Error (MSE) 
 Root Mean Squared Error (RMSE) 
 R² Score (Coefficient of Determination) 
7. Visualization 
o Plot the regression line along with the actual data points. 
o Visualize actual vs predicted prices to assess model performance.  """

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import  train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
"""
1. Load the Dataset 
o Load the provided dataset using Pandas. 
o Retain only the columns Square Footage and Price for model building. 
"""
df=pd.read_csv("Week7\\Home\\house_price_regression_dataset.csv")
# Retain only the relevant columns
df_model = df[['Square_Footage', 'House_Price']]
# Display the first few rows to confirm
print(df_model.head())

""" 
2. Exploratory Data Analysis (EDA) 
o Display the first few rows of the dataset. 
o Check for missing or null values and handle them appropriately. 
o Visualize the relationship between Square Footage and Price using a scatter 
plot.  
"""
print("\nMissing values in each column:")
print(df_model.isnull().sum())
df_cleaned = df_model.dropna()

##Scatter Plot
plt.scatter(df_cleaned['Square_Footage'],df_cleaned['House_Price'],color='green',label='Square Footage and Price')
plt.xlabel(' Square_Footage')
plt.ylabel(' House_Price')
plt.title('Relationship Between Square Footage and House Price')
plt.legend()

plt.tight_layout()
plt.show()

""" 
3. Feature and Target Selection 
o Assign Square Footage as the independent variable (X). 
o Assign Price as the dependent variable (Y). 
"""
X= df_cleaned[['Square_Footage']] # Requires 2 D array as per  - This is feature
Y= df_cleaned['House_Price']  # Label

""" 
4. Train-Test Split 
o Split the dataset into training and testing sets using an 80-20 ratio. 
 """


X_train, X_test, Y_train, Y_test= train_test_split(X,Y,test_size=0.2,random_state=11)
"""
 5. Model Building 
o Create a Linear Regression model using LinearRegression from 
sklearn.linear_model. 
o Fit the model on the training data. 
o Display the intercept (b₀) and coefficient (b₁) of the regression line.  """
model= LinearRegression()
model.fit(X_train,Y_train)
print("Intercept (b₀):", model.intercept_)
print("Coefficient (b₁):", model.coef_[0])

""" 
6. Prediction and Evaluation 
o Predict the house prices for the test set. 
o Calculate and print the following evaluation metrics: 
 Mean Squared Error (MSE) 
 Root Mean Squared Error (RMSE) 
 R² Score (Coefficient of Determination)  """

# Predict Y with the X_test ( Y=mx+C)

Y_predict = model.predict(X_test)

# Evaluate - MSE /R2
print("MSE ", mean_squared_error(Y_test,Y_predict))
print("R2",r2_score(Y_test,Y_predict))

""" 
7. Visualization 
o Plot the regression line along with the actual data points. 
"""

plt.scatter(X_test,Y_test,color='green',label='Actual Prices')
plt.plot(X_test,Y_predict, color ='blue', label=' Model Predicted Data')
plt.xlabel('Square Footage')
plt.ylabel('House Price')
plt.title('Regression Line vs Actual Data')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

"""
 7. Visualization 
o Visualize actual vs predicted prices to assess model performance.  
"""
# Scatter plot of actual vs predicted
plt.scatter(Y_test, Y_predict, color='purple', alpha=0.6)

# Diagonal reference line (perfect prediction)
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()])

# Labels and layout
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted Prices')
plt.grid(True)
plt.tight_layout()
plt.show()




