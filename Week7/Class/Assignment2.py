"""Linear Regression Model"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import  train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score


# Read Data Set 

data = pd.read_csv("C:\AIEngineer\Class1_Python\Week7\Class\salary.csv")
# X Value ( Feature - YearsExperience)

X= data[['YearsExperience']] # Requires 2 D array as per 

# Y Value ( Label - Salary)

Y= data['Salary']

X_train, X_test, Y_train, Y_test= train_test_split(X,Y,test_size=0.2,random_state=11)

# Apply Regression Technique for Learning
model= LinearRegression()
model.fit(X_train,Y_train)

# Predict Y with the X_test ( Y=mx+C)

Y_predict = model.predict(X_test)

# Evaluate - MSE /R2
print("MSE ", mean_squared_error(Y_test,Y_predict))
print("R2",r2_score(Y_test,Y_predict))

plt.scatter(X_test,Y_test,color='green',label='Test - Actual Data')
plt.plot(X_test,Y_predict, color ='blue', label=' Model Predicted Data')
plt.xlabel(' Years of Exp')
plt.ylabel(' Sal')
plt.tight_layout()
plt.show()




